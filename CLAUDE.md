# Ads Builder — Direct Response Creative Builder
> Autor: Mikael Lovrin · Copyright (c) 2026 Mikael Lovrin · Licenciado sob [CC BY-NC-ND 4.0](LICENSE) (uso não comercial, sem derivações, com atribuição)

## O que é este projeto

Sistema de IA para criação de criativos de anúncio de Direct Response (roteiros de vídeo Reels/TikTok e briefings de imagem estática para Meta), fundamentado num framework próprio de copywriting "black hat" de saúde/emagrecimento/suplementos, com um corpus/knowledge base vivo que cresce a cada criativo validado — no mesmo espírito do projeto irmão `adv-agent` (advertoriais), mas empacotado como **skill portátil** (modelo do `vsl-builder`).

Trabalha por **marca/produto** (uma pasta dedicada por marca, fora deste repo), com aprovação humana em cada etapa-chave (ou modo autônomo), kill list por marca para nunca repetir ângulo, e uma matriz de testes que transforma cada criativo numa hipótese rastreável.

## Modelo Operacional — Duas Camadas

Este repositório (`ads-builder/`) é o **repo-fonte**: onde a skill é mantida e onde o `knowledge/` + `corpus-seed/` compartilhados crescem com o tempo. Ele **não** é onde você trabalha dia a dia numa marca específica.

1. **Instalar** (uma vez, ou de novo após atualizar o repo-fonte): rode `Install.bat`. Ele copia `skills/ads-builder/`, `skills/creative-pattern-analysis/` e `skills/knowledge-updater/` para `%USERPROFILE%\.claude\skills\` — disponíveis em qualquer pasta, para qualquer outro agente que você já tenha instalado ali.
2. **Trabalhar numa marca**: crie uma pasta dedicada para ela em qualquer lugar (ex. `FEG/Ferramentas/badrock/`), abra o Claude Code dentro dela, e digite `/ads-builder`. Todo o output daquela marca (`briefing.md`, `kill-list.md`, `tracking/`, `output/imagens/`) fica centralizado ali — nunca dentro deste repo.
3. **Conhecimento compartilhado**: `knowledge/` (taxonomias) e `corpus-seed/` (baseline de exemplos) vivem dentro do pacote da skill instalada (`~/.claude/skills/ads-builder/`) — a mesma cópia física é lida por todas as marcas. Atualizar esse conhecimento aqui no repo-fonte e rodar `Install.bat` de novo propaga a atualização para todas as marcas já criadas, sem precisar recriar nada nelas.
4. **Corpus específico de marca**: se uma marca acumular material próprio (via `knowledge-updater` rodando dentro da pasta dela), isso cria um `corpus/` local, isolado — não retroalimenta o `corpus-seed/` compartilhado automaticamente. Para promover um aprendizado de uma marca para o conhecimento compartilhado, traga o material de volta manualmente numa sessão aqui no repo-fonte (ver `skills/knowledge-updater/SKILL.md` > Passo -1).

## Estrutura do Repo-Fonte

```
ads-builder/
├── CLAUDE.md                         ← este arquivo
├── Install.bat                       ← copia as 3 skills para ~/.claude/skills/
└── skills/
    ├── ads-builder/
    │   ├── SKILL.md                      ← orquestrador principal (ler primeiro)
    │   ├── knowledge/                    ← base de conhecimento estruturada (bundled, compartilhada)
    │   │   ├── hook-taxonomy.md          ← arquétipos de gancho (niche-agnostic)
    │   │   ├── structure-library.md      ← estrutura de 8 blocos + 3 estruturas invisíveis + CTA triplo
    │   │   ├── static-image-psychology.md ← 10 princípios de conversão + 5 estilos visuais fixos
    │   │   └── editor-formats.md         ← formatos de execução/edição (cinematográfico, caixinha de perguntas)
    │   ├── corpus-seed/                  ← baseline compartilhada (bundled, somente leitura em runtime)
    │   │   ├── index.json                ← índice com metadados de todas as entries
    │   │   ├── entries/                   ← JSONs de intelligence extraída (hook, estrutura, estilo)
    │   │   └── updater-log.json          ← log de sessões do knowledge-updater no repo-fonte
    │   ├── scripts/
    │   │   ├── build_corpus_index.py     ← triagem do corpus LOCAL de uma marca (roda em cwd)
    │   │   └── generate_images.py        ← Fase 3c: gera imagens via OpenAI (gpt-image-1), roda em cwd
    │   ├── requirements.txt
    │   ├── .env.example
    │   └── prompts/
    │       ├── fase0-onboarding.md       ← SEMPRE primeiro
    │       ├── fase1-extracao-produto.md
    │       ├── fase2-estrategia-criativa.md
    │       ├── fase3a-roteiro-video.md
    │       ├── fase3b-briefing-imagem.md
    │       ├── fase3c-geracao-imagem.md  ← opcional, gera PNGs de fato via OpenAI
    │       ├── fase4-revisao-traducao.md ← opcional
    │       ├── kill-list.md              ← protocolo de atualização da kill list
    │       └── combinacoes.md            ← protocolo da matriz de testes (central)
    ├── creative-pattern-analysis/
    │   └── SKILL.md                      ← lateralização: analisa criativos de referência → Lateralization Brief
    └── knowledge-updater/
        ├── SKILL.md                      ← manutenção e extração do corpus (compartilhado ou local, ver Passo -1)
        ├── extraction-protocol.md
        ├── export-prompt.md              ← minerar conversas antigas → corpus-seed compartilhado
        └── adapters/
            └── social-creative.md
```

## Estrutura de uma Pasta de Marca (fora deste repo)

```
[pasta dedicada da marca, ex. FEG/Ferramentas/badrock/]
├── progress.md                ← estado atual (gerenciado silenciosamente)
├── briefing.md                ← Fase 0 + Fase 1
├── pattern-brief.md           ← se Cenário A (lateralização)
├── estrategia-criativa.md     ← Fase 2
├── roteiros-video.md          ← Fase 3a (se aplicável)
├── briefing-imagem.md         ← Fase 3b (se aplicável)
├── kill-list.md                ← ângulos/ganchos/histórias já usados, nunca repetir
├── brand/                     ← logo, fotos de produto, paleta (opcional, Fase 3c modo mockup)
├── corpus/                    ← (opcional) corpus específico desta marca, isolado
├── output/imagens/             ← PNGs gerados na Fase 3c + manifest.json
└── tracking/
    ├── test-matrix.json       ← matriz de combinações testadas + backlog (lida pela IA)
    ├── insights.md            ← biblioteca de aprendizados (lida por humanos)
    └── sugestoes-log.json     ← histórico de sugestões feitas
```

## Como usar o Ads Builder

1. (Uma vez) Rode `Install.bat` neste repo
2. Crie/abra a pasta dedicada da marca, rode o Claude Code nela, digite `/ads-builder`
3. Verifique se existe `progress.md` para continuar sessão anterior
4. Se não existe, execute a Fase 0 (`prompts/fase0-onboarding.md`)
5. Siga as fases: Onboarding → Extração de Produto → [Lateralização] → Estratégia Criativa → Roteiro de Vídeo e/ou Briefing de Imagem → [Revisão/Tradução]
6. A escrita final atualiza `kill-list.md` e registra o teste em `tracking/test-matrix.json`
7. Quando o usuário reportar resultado, atualizar a matriz e sugerir próximo teste
8. Para lateralizar a partir de referências: sub-agente `../creative-pattern-analysis/SKILL.md`

## Como adicionar novos materiais ao corpus

**Específico de uma marca** (fica isolado naquela pasta): dentro da pasta da marca, use `knowledge-updater` normalmente (Passo -1 → Escopo Local) e rode `python "$HOME/.claude/skills/ads-builder/scripts/build_corpus_index.py"` se quiser triagem em lote de `corpus/raw/`.

**Compartilhado entre todas as marcas** (vira parte do `corpus-seed/`/`knowledge/` bundled): só roda aqui no repo-fonte.
1. Cole o criativo (roteiro, imagem analisada, ou print de briefing) numa sessão aberta aqui
2. Use `skills/knowledge-updater/SKILL.md` (Passo -1 → Escopo Compartilhado) para extrair, classificar e propor atualizações ao `skills/ads-builder/knowledge/`
3. Rode `Install.bat` de novo para propagar a atualização para todas as marcas já instaladas

**Minerando conversas antigas (fora deste projeto) que renderam criativos bons:** use `skills/knowledge-updater/export-prompt.md`, que tem um prompt pronto para colar na conversa antiga e pedir pro Claude de lá fazer a curadoria (criativo final + contexto + classificação + por que funcionou), já num formato que o `knowledge-updater` consome direto — sempre em Escopo Compartilhado, aqui no repo-fonte.

## Princípios fundamentais

- **Ganchos e estruturas são niche-agnostic** — o gatilho psicológico é universal, o nicho/produto é substituível
- **Sempre consultar `kill-list.md`** (por marca, na pasta da marca) antes de sugerir ângulo/gancho — nunca repetir uma narrativa já usada para a mesma marca
- **Progresso silencioso** — `progress.md` é atualizado automaticamente sem anúncio a cada fase
- **Corpus como fundação** — nunca invente ganchos/estruturas; derive-os do conhecimento validado em `knowledge/` e `corpus-seed/` (compartilhados) ou no `corpus/` local da marca
- **Nunca inventar dado de produto** — UMP, UMS, autoridade, oferta, garantia só entram se confirmados pelo usuário ou extraídos do briefing real
- **Output em duas camadas** — `roteiros-video.md` / `briefing-imagem.md` para revisão humana; nada é "produção" final automática (o usuário sempre aprova antes de mandar pro editor/gerador de imagem)
- **Iteração sistemática** — cada criativo testa uma hipótese específica (ângulo × tipo × gancho × emoção × estrutura/estilo × plataforma); cada resultado atualiza a matriz e informa o próximo teste
- **Biblioteca viva** — `tracking/insights.md` cresce a cada teste e documenta o que funciona para cada marca; aprendizados que valem pra qualquer marca são promovidos ao conhecimento compartilhado (ver acima)

## Scripts úteis

Os scripts vivem dentro da skill instalada e sempre operam sobre a pasta atual (cwd) — rode-os de dentro da pasta da marca:

```bash
# Triagem heurística do corpus local (corpus/raw/ da marca atual)
python "$HOME/.claude/skills/ads-builder/scripts/build_corpus_index.py"

# Gerar imagens via OpenAI a partir do briefing aprovado (Fase 3c)
# requer OPENAI_API_KEY em .env (na pasta da marca, copie de ~/.claude/skills/ads-builder/.env.example)
# pip install -r ~/.claude/skills/ads-builder/requirements.txt (uma vez só)
python "$HOME/.claude/skills/ads-builder/scripts/generate_images.py" dr --corpo 1 --estilo realistic_photography
python "$HOME/.claude/skills/ads-builder/scripts/generate_images.py" mockup --prompt "..." --name capa
```

No Windows, o caminho equivalente é `%USERPROFILE%\.claude\skills\ads-builder\scripts\...`.
