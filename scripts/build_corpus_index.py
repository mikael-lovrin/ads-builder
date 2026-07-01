"""
build_corpus_index.py
Triagem rápida de novos materiais crus em corpus/raw/ (.md ou .txt) para o corpus
de criativos do ads-builder. Classifica por palavra-chave (hook archetype, tipo de
anúncio, emoção dominante, nicho, plataforma) e faz merge ADITIVO em corpus/index.json
— nunca sobrescreve entradas existentes (inclusive as 6 entries seed, que foram
extraídas manualmente a partir de COPY PROMPTS.docx e não têm arquivo correspondente
em corpus/raw/).

Esta classificação é só TRIAGEM — uma heurística rápida para saber o que existe.
Para extração profunda (schema completo de corpus/entries/*.json), use
skills/knowledge-updater/SKILL.md, que é quem preenche o campo "intelligent_entry".

Run: python scripts/build_corpus_index.py
"""

import json
import re
import sys
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE_DIR    = Path(__file__).parent.parent
RAW_DIR     = BASE_DIR / "corpus" / "raw"
CORPUS_DIR  = BASE_DIR / "corpus"
OUTPUT_FILE = CORPUS_DIR / "index.json"

# IDs vêm de skills/knowledge-updater/extraction-protocol.md — manter sincronizado.

HOOK_ARCHETYPE_KEYWORDS = {
    "aviso_reverso":                  ["não misture", "não faça", "não use", "se você não quiser"],
    "conspiracao_revelada":           ["escondeu", "esconderam", "big pharma", "indústria sabia", "vazou"],
    "injustica_comparativa":          ["enquanto você", "enquanto sua amiga", "por que você", "desligado"],
    "transformacao_visual_especifica":["de l para s", "em 60 dias", "em 90 dias", "meu médico não acreditou", "antes e depois"],
    "ouch_factor":                    ["vergonha", "inveja da minha", "odiava meu", "roçavam até"],
    "contrarian":                     ["pare de", "está errado", "não importa", "perda de tempo"],
    "story_tease":                    ["quando o", "eu entrei na", "meu médico olhou"],
    "visual_shock_asmr":              ["asmr", "textura", "pote deslizando", "batida"],
    "revolta_financeira":             ["otária", "fatura", "boleto", "rasguei", "joguei no lixo"],
    "identidade_vulnerabilidade":     ["eu senti inveja", "eu odiava", "confissão"],
}

AD_TYPE_KEYWORDS = {
    "video_script":  ["roteiro", "gancho", "[instruções de cena", "cta triplo", "reels", "tiktok", "ugc"],
    "static_image":  ["prompt de imagem", "image prompt", "estilo visual", "1080x1080", "aspect ratio", "body copy"],
}

EMOTION_KEYWORDS = {
    "medo":            ["medo", "risco", "perigo", "antes que"],
    "vergonha":        ["vergonha", "envergonhar", "julgam"],
    "raiva":           ["enganaram", "escondem", "não te contam", "indignação"],
    "desejo":          ["imagine", "sonho", "deseja"],
    "inveja":          ["enquanto você", "outros já", "amiga invejosa"],
    "esperanca":       ["finalmente", "ainda dá tempo", "é possível"],
    "curiosidade":     ["segredo", "descubra", "por que"],
    "orgulho":         ["merece", "grupo seleto", "pessoas como você"],
    "inspiracao":      ["transformação", "virada", "consegui"],
    "culpa_absolvida": ["não é culpa sua", "a culpa não é sua", "não foi você"],
}

NICHE_KEYWORDS = {
    "saude_emagrecimento": ["emagrecer", "peso", "gordura", "dieta", "metabolismo", "barriga"],
    "saude_feminina":      ["perimenopausa", "menopausa", "hormônio", "ciclo"],
    "beleza_skincare":     ["pele", "rosto", "rugas", "colágeno", "skincare"],
    "financas_renda":      ["dinheiro", "renda", "investimento", "patrimônio"],
    "outros":              [],
}

PLATFORM_KEYWORDS = {
    "reels":     ["reels"],
    "tiktok":    ["tiktok"],
    "meta_feed": ["feed", "facebook"],
    "pinterest": ["pinterest"],
    "stories":   ["stories", "story"],
}


def classify_single(text: str, keyword_map: dict) -> str | None:
    text_lower = text.lower()
    scores = {}
    for category, keywords in keyword_map.items():
        score = sum(1 for kw in keywords if kw in text_lower)
        if score > 0:
            scores[category] = score
    return max(scores, key=scores.get) if scores else None


def classify_multi(text: str, keyword_map: dict, top_n: int = 2) -> list:
    text_lower = text.lower()
    scores = {}
    for category, keywords in keyword_map.items():
        score = sum(1 for kw in keywords if kw in text_lower)
        if score > 0:
            scores[category] = score
    ranked = sorted(scores, key=scores.get, reverse=True)
    return ranked[:top_n] if ranked else []


def extract_title(content: str) -> str:
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    for line in content.split("\n"):
        line = line.strip()
        if line:
            return line[:120]
    return ""


def extract_word_count(content: str) -> int:
    text = re.sub(r'[#>*\[\]`\-\|]', ' ', content)
    return len(text.split())


def process_file(path: Path) -> dict:
    content = path.read_text(encoding="utf-8", errors="replace")
    title = extract_title(content)

    ad_type = classify_single(content, AD_TYPE_KEYWORDS) or "video_script"
    hook_archetypes = classify_multi(content, HOOK_ARCHETYPE_KEYWORDS, top_n=2)
    dominant_emotion = classify_single(content, EMOTION_KEYWORDS)
    niches = classify_multi(content, NICHE_KEYWORDS, top_n=2) or ["outros"]
    platforms = classify_multi(content, PLATFORM_KEYWORDS, top_n=3) or ["meta_feed"]

    return {
        "file": path.name,
        "slug": path.stem,
        "type": ad_type,
        "title": title,
        "post_url": None,
        "hook_archetype": hook_archetypes,
        "ad_type": ad_type,
        "niches": niches,
        "dominant_emotion": dominant_emotion,
        "structure_or_style": None,
        "platform": platforms,
        "mechanism_hint": "",
        "notable_technique": hook_archetypes[0] if hook_archetypes else None,
        "word_count": extract_word_count(content),
        "intelligent_entry": None,
        "needs_knowledge_updater": True,
    }


def main():
    CORPUS_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    if OUTPUT_FILE.exists():
        existing = json.loads(OUTPUT_FILE.read_text(encoding="utf-8"))
    else:
        existing = {"total": 0, "last_updated": None, "entries": []}

    existing_slugs = {e["slug"] for e in existing["entries"]}

    raw_files = sorted(
        [f for f in RAW_DIR.glob("*") if f.suffix in (".md", ".txt") and f.parent == RAW_DIR]
    )

    print(f"Entradas existentes em corpus/index.json: {len(existing['entries'])}")
    print(f"Arquivos encontrados em corpus/raw/: {len(raw_files)}\n")

    new_entries = []
    errors = []
    for f in raw_files:
        if f.stem in existing_slugs:
            continue
        try:
            new_entries.append(process_file(f))
        except Exception as e:
            errors.append({"file": f.name, "error": str(e)})
            print(f"  ERRO {f.name}: {e}")

    if not new_entries:
        print("Nenhum arquivo novo para processar em corpus/raw/.")
        if not raw_files:
            print("(corpus/raw/ está vazio — solte .md/.txt de novos criativos lá para a próxima triagem,")
            print(" ou peça ao skills/knowledge-updater/SKILL.md para extrair direto de texto colado na conversa.)")
        return

    merged_entries = existing["entries"] + new_entries
    import datetime
    OUTPUT_FILE.write_text(
        json.dumps(
            {"total": len(merged_entries), "last_updated": datetime.date.today().isoformat(), "entries": merged_entries},
            ensure_ascii=False, indent=2
        ),
        encoding="utf-8"
    )

    print(f"✓ {len(new_entries)} entradas novas adicionadas (triagem heurística, intelligent_entry=null).")
    print(f"✓ corpus/index.json agora tem {len(merged_entries)} entradas no total.")
    print("→ Rode skills/knowledge-updater/SKILL.md para fazer a extração profunda destas entradas novas")
    print("  (elas ficam marcadas com needs_knowledge_updater=true até lá).")

    if errors:
        print(f"\n✗ {len(errors)} erros:")
        for e in errors:
            print(f"  {e['file']}: {e['error']}")

    archetypes = Counter(a for e in new_entries for a in e["hook_archetype"])
    if archetypes:
        print("\n── Arquétipos de Gancho Detectados (novos arquivos) ──")
        for arch, count in archetypes.most_common(10):
            print(f"  {arch}: {count}")


if __name__ == "__main__":
    main()
