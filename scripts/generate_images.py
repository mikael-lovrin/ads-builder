"""
generate_images.py
Gera imagens via API da OpenAI (gpt-image-1) a partir dos briefs escritos pelo
ads-builder. Ver skills/ads-builder/prompts/fase3c-geracao-imagem.md para o
protocolo completo (quando rodar, como escolher o que gerar, como registrar).

Dois modos:

  dr      — gera 1+ dos 10 image ads de projects/[marca]/briefing-imagem.md,
            texto puro (images.generate), SEM anexar assets de marca. É o modo
            default: a regra 8 do prompt (knowledge/static-image-psychology.md)
            proíbe logo/produto no frame desses criativos de propósito — é o
            que faz a imagem parecer nativa e parar o scroll.

  mockup  — gera uma imagem pontual com prompt livre, anexando os assets de
            projects/[marca]/brand/ (logo, paleta, fotos de produto/mockup)
            como referência via images.edit. Para criativos de produto/branded,
            fora da lógica "black hat" do briefing-imagem.md.

Requer OPENAI_API_KEY no ambiente (ou em .env na raiz do projeto).

Uso:
  python scripts/generate_images.py dr --marca acme --corpo 1 --estilo realistic_photography
  python scripts/generate_images.py dr --marca acme --corpo all --estilo all
  python scripts/generate_images.py mockup --marca acme --prompt "produto em cima de bancada de mármore, luz natural" --ref brand/logo.png brand/produto.png

Saída: projects/[marca]/output/imagens/*.png + manifest.json (histórico de gerações).
"""

import argparse
import base64
import datetime
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE_DIR = Path(__file__).parent.parent
PROJECTS_DIR = BASE_DIR / "projects"

STYLE_ORDER = [
    "realistic_photography",
    "documentary_raw",
    "editorial_illustration",
    "cartoon",
    "infographic",
]

SIZE_1_1 = "1024x1024"


def load_api_key() -> str:
    import os
    key = os.environ.get("OPENAI_API_KEY")
    if key:
        return key
    env_file = BASE_DIR / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("OPENAI_API_KEY"):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    print("ERRO: OPENAI_API_KEY não encontrada no ambiente nem em .env na raiz do projeto.")
    print("Crie um .env (copie de .env.example) com sua chave, ou exporte a variável de ambiente.")
    sys.exit(1)


def get_client():
    try:
        from openai import OpenAI
    except ImportError:
        print("ERRO: pacote 'openai' não instalado. Rode: pip install -r requirements.txt")
        sys.exit(1)
    return OpenAI(api_key=load_api_key())


# ── Modo dr: parsing de briefing-imagem.md ──────────────────────────────

SECTION_RE = re.compile(
    r"###\s*Corpo\s*(\d+)\s*[—\-]\s*(\w+)\s*\n(.*?)(?=\n###\s*Corpo|\Z)",
    re.DOTALL,
)
FIELD_RE = re.compile(
    r"\*\*Prompt de Imagem:\*\*\s*\n(.*?)(?=\n\*\*|\Z)",
    re.DOTALL,
)


def parse_briefing(marca: str) -> dict:
    path = PROJECTS_DIR / marca / "briefing-imagem.md"
    if not path.exists():
        print(f"ERRO: {path} não existe. Rode a Fase 3b primeiro.")
        sys.exit(1)
    content = path.read_text(encoding="utf-8")

    entries = {}
    for m in SECTION_RE.finditer(content):
        corpo, estilo, body = m.group(1), m.group(2), m.group(3)
        prompt_m = FIELD_RE.search(body)
        if not prompt_m:
            continue
        entries[(corpo, estilo)] = prompt_m.group(1).strip()

    if not entries:
        print(f"ERRO: nenhum bloco '### Corpo N — estilo' encontrado em {path}.")
        print("Verifique se o brief foi salvo com o formato descrito em fase3c-geracao-imagem.md.")
        sys.exit(1)
    return entries


def select_entries(entries: dict, corpo_arg: str, estilo_arg: str) -> list:
    corpos = sorted({c for c, _ in entries}) if corpo_arg == "all" else [corpo_arg]
    estilos = STYLE_ORDER if estilo_arg == "all" else [estilo_arg]
    selected = []
    for c in corpos:
        for e in estilos:
            if (c, e) in entries:
                selected.append((c, e, entries[(c, e)]))
            else:
                print(f"AVISO: Corpo {c} / estilo {e} não encontrado no brief — pulando.")
    return selected


def next_version(out_dir: Path, stem: str) -> int:
    existing = list(out_dir.glob(f"{stem}-v*.png"))
    if not existing:
        return 1
    versions = [int(re.search(r"-v(\d+)\.png$", f.name).group(1)) for f in existing]
    return max(versions) + 1


def update_manifest(out_dir: Path, entry: dict):
    manifest_path = out_dir / "manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    else:
        manifest = {"generated": []}
    manifest["generated"].append(entry)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def run_dr(args):
    entries = parse_briefing(args.marca)
    selected = select_entries(entries, args.corpo, args.estilo)
    if not selected:
        print("Nada para gerar.")
        return

    out_dir = PROJECTS_DIR / args.marca / "output" / "imagens"
    out_dir.mkdir(parents=True, exist_ok=True)

    client = get_client()

    print(f"Gerando {len(selected)} imagem(ns) para '{args.marca}' (modo dr, sem assets de marca)...\n")
    for corpo, estilo, prompt in selected:
        stem = f"corpo{corpo}-{estilo}"
        version = next_version(out_dir, stem)
        filename = f"{stem}-v{version}.png"
        print(f"  → {filename}")

        resp = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size=SIZE_1_1,
            quality=args.quality,
            n=1,
        )
        image_bytes = base64.b64decode(resp.data[0].b64_json)
        (out_dir / filename).write_bytes(image_bytes)

        update_manifest(out_dir, {
            "file": filename,
            "mode": "dr",
            "corpo": corpo,
            "estilo": estilo,
            "prompt": prompt,
            "generated_at": datetime.datetime.now().isoformat(timespec="seconds"),
        })

    print(f"\n✓ Concluído. Arquivos em {out_dir}")


def run_mockup(args):
    marca_dir = PROJECTS_DIR / args.marca
    out_dir = marca_dir / "output" / "imagens"
    out_dir.mkdir(parents=True, exist_ok=True)

    ref_paths = []
    if args.ref:
        for r in args.ref:
            p = Path(r)
            if not p.is_absolute():
                p = marca_dir / r
            if not p.exists():
                print(f"AVISO: referência não encontrada: {p} — pulando.")
                continue
            ref_paths.append(p)
    else:
        brand_dir = marca_dir / "brand"
        if brand_dir.exists():
            ref_paths = [
                p for p in brand_dir.iterdir()
                if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")
            ]

    if not ref_paths:
        print(f"AVISO: nenhum asset de marca encontrado (nem --ref, nem {marca_dir / 'brand'}).")
        print("Gerando sem referência (equivalente a images.generate).")

    client = get_client()
    stem = args.name or "mockup"
    version = next_version(out_dir, stem)
    filename = f"{stem}-v{version}.png"
    print(f"Gerando {filename} (modo mockup, {len(ref_paths)} asset(s) de referência)...")

    if ref_paths:
        files = [open(p, "rb") for p in ref_paths]
        try:
            resp = client.images.edit(
                model="gpt-image-1",
                image=files,
                prompt=args.prompt,
                size=SIZE_1_1,
                quality=args.quality,
                n=1,
            )
        finally:
            for f in files:
                f.close()
    else:
        resp = client.images.generate(
            model="gpt-image-1",
            prompt=args.prompt,
            size=SIZE_1_1,
            quality=args.quality,
            n=1,
        )

    image_bytes = base64.b64decode(resp.data[0].b64_json)
    (out_dir / filename).write_bytes(image_bytes)

    update_manifest(out_dir, {
        "file": filename,
        "mode": "mockup",
        "prompt": args.prompt,
        "refs": [str(p.relative_to(marca_dir)) if p.is_relative_to(marca_dir) else str(p) for p in ref_paths],
        "generated_at": datetime.datetime.now().isoformat(timespec="seconds"),
    })

    print(f"\n✓ Concluído. Arquivo em {out_dir / filename}")


def main():
    parser = argparse.ArgumentParser(description="Gera imagens via OpenAI para o ads-builder.")
    sub = parser.add_subparsers(dest="mode", required=True)

    p_dr = sub.add_parser("dr", help="Gera image ads do briefing-imagem.md (sem assets de marca).")
    p_dr.add_argument("--marca", required=True)
    p_dr.add_argument("--corpo", default="all", help="1, 2 ou all (default: all)")
    p_dr.add_argument("--estilo", default="all", help="ID do estilo ou all (default: all)")
    p_dr.add_argument("--quality", default="high", choices=["low", "medium", "high", "auto"])
    p_dr.set_defaults(func=run_dr)

    p_mock = sub.add_parser("mockup", help="Gera criativo pontual com assets de marca (logo/mockup).")
    p_mock.add_argument("--marca", required=True)
    p_mock.add_argument("--prompt", required=True)
    p_mock.add_argument("--ref", nargs="*", help="Paths de imagens de referência (default: projects/[marca]/brand/*)")
    p_mock.add_argument("--name", help="Prefixo do arquivo de saída (default: mockup)")
    p_mock.add_argument("--quality", default="high", choices=["low", "medium", "high", "auto"])
    p_mock.set_defaults(func=run_mockup)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
