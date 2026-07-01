# Ads Builder — Direct Response Creative Builder
> Autor: Mikael Lovrin · Copyright (c) 2026 Mikael Lovrin · Licenciado sob [CC BY-NC-ND 4.0](LICENSE) (uso não comercial, sem derivações, com atribuição)

## O que é este projeto

Sistema de IA para criação de criativos de anúncio de Direct Response (roteiros de vídeo Reels/TikTok e briefings de imagem estática para Meta), fundamentado num framework próprio de copywriting "black hat" de saúde/emagrecimento/suplementos, com um corpus/knowledge base vivo que cresce a cada criativo validado — no mesmo modelo do projeto irmão `adv-agent` (advertoriais).

Trabalha por **marca/produto**, com aprovação humana em cada etapa-chave (ou modo autônomo), kill list por marca para nunca repetir ângulo, e uma matriz de testes que transforma cada criativo numa hipótese rastreável.

## Estrutura do Projeto

```
ads-builder/
├── CLAUDE.md                         ← este arquivo
├── COPY PROMPTS.docx                 ← fonte original dos prompts (não editar)
├── referencias/
│   └── copy-prompts-extraido.md      ← transcrição organizada do docx (leitura humana)
├── corpus/
│   ├── index.json                    ← índice com metadados de todas as entries
│   ├── entries/                      ← JSONs de intelligence extraída (hook, estrutura, estilo)
│   └── updater-log.json              ← log de sessões do knowledge-updater
├── knowledge/                        ← base de conhecimento estruturada
│   ├── hook-taxonomy.md              ← arquétipos de gancho (niche-agnostic)
│   ├── structure-library.md          ← estrutura de 8 blocos + 3 estruturas invisíveis + CTA triplo
│   ├── static-image-psychology.md    ← 10 princípios de conversão + 5 estilos visuais fixos
│   └── editor-formats.md             ← formatos de execução/edição (cinematográfico, caixinha de perguntas...)
├── projects/                         ← um subdiretório por marca/produto
│   └── [marca]/
│       ├── progress.md               ← estado atual (gerenciado silenciosamente)
│       ├── briefing.md               ← Fase 0 + Fase 1
│       ├── pattern-brief.md          ← se Cenário A (lateralização)
│       ├── estrategia-criativa.md    ← Fase 2
│       ├── roteiros-video.md         ← Fase 3a (se aplicável)
│       ├── briefing-imagem.md        ← Fase 3b (se aplicável)
│       ├── kill-list.md              ← ângulos/ganchos/histórias já usados, nunca repetir
│       ├── brand/                    ← logo, fotos de produto, paleta (opcional, Fase 3c modo mockup)
│       ├── output/imagens/           ← PNGs gerados na Fase 3c + manifest.json
│       └── tracking/
│           ├── test-matrix.json      ← matriz de combinações testadas + backlog (lida pela IA)
│           ├── insights.md           ← biblioteca de aprendizados (lida por humanos)
│           └── sugestoes-log.json    ← histórico de sugestões feitas
├── scripts/
│   ├── build_corpus_index.py         ← regenera corpus/index.json a partir de corpus/entries/
│   └── generate_images.py            ← Fase 3c: gera imagens via OpenAI (gpt-image-1) a partir do briefing
└── skills/
    ├── ads-builder/
    │   ├── SKILL.md                      ← orquestrador principal (ler primeiro)
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
        ├── SKILL.md                      ← manutenção e extração do corpus
        ├── extraction-protocol.md
        └── adapters/
            └── social-creative.md
```

## Modelo operacional

Diferente do `vsl-builder` (skill global e portátil, sem estado compartilhado), o `ads-builder` segue o modelo do `adv-agent`: **abra o Claude Code direto nesta pasta** — não precisa instalar nada. O corpus e o knowledge base são compartilhados entre todos os projetos/marcas dentro deste mesmo repositório.

## Como usar o Ads Builder

1. Leia `skills/ads-builder/SKILL.md`
2. Verifique se existe `projects/[marca]/progress.md` para continuar sessão anterior
3. Se não existe, execute a Fase 0 (`prompts/fase0-onboarding.md`)
4. Siga as fases: Onboarding → Extração de Produto → [Lateralização] → Estratégia Criativa → Roteiro de Vídeo e/ou Briefing de Imagem → [Revisão/Tradução]
5. A escrita final atualiza `kill-list.md` e registra o teste em `tracking/test-matrix.json`
6. Quando o usuário reportar resultado, atualizar a matriz e sugerir próximo teste
7. Para lateralizar a partir de referências: sub-agente `skills/creative-pattern-analysis/SKILL.md`

## Como adicionar novos materiais ao corpus

1. Cole o criativo (roteiro, imagem analisada, ou print de briefing) na conversa, ou salve em texto numa pasta de trabalho
2. Use o skill `skills/knowledge-updater/SKILL.md` para extrair, classificar e propor atualizações ao `knowledge/`
3. Rode `python scripts/build_corpus_index.py` para regenerar o índice

**Minerando conversas antigas (fora deste projeto) que renderam criativos bons:** não cole a conversa crua aqui — use `skills/knowledge-updater/export-prompt.md`, que tem um prompt pronto para colar na conversa antiga e pedir pro Claude de lá fazer a curadoria (criativo final + contexto + classificação + por que funcionou), já num formato que o `knowledge-updater` consome direto.

## Princípios fundamentais

- **Ganchos e estruturas são niche-agnostic** — o gatilho psicológico é universal, o nicho/produto é substituível
- **Sempre consultar `kill-list.md`** (por marca) antes de sugerir ângulo/gancho — nunca repetir uma narrativa já usada para a mesma marca
- **Progresso silencioso** — `progress.md` é atualizado automaticamente sem anúncio a cada fase
- **Corpus como fundação** — nunca invente ganchos/estruturas; derive-os do corpus validado em `knowledge/` e `corpus/`
- **Nunca inventar dado de produto** — UMP, UMS, autoridade, oferta, garantia só entram se confirmados pelo usuário ou extraídos do briefing real
- **Output em duas camadas** — `roteiros-video.md` / `briefing-imagem.md` para revisão humana; nada é "produção" final automática (o usuário sempre aprova antes de mandar pro editor/gerador de imagem)
- **Iteração sistemática** — cada criativo testa uma hipótese específica (ângulo × tipo × gancho × emoção × estrutura/estilo × plataforma); cada resultado atualiza a matriz e informa o próximo teste
- **Biblioteca viva** — `tracking/insights.md` cresce a cada teste e documenta o que funciona para cada marca

## Scripts úteis

```bash
# Regenerar o índice do corpus
python scripts/build_corpus_index.py

# Gerar imagens via OpenAI a partir do briefing aprovado (Fase 3c)
# requer OPENAI_API_KEY em .env (copie de .env.example) — pip install -r requirements.txt
python scripts/generate_images.py dr --marca [marca] --corpo 1 --estilo realistic_photography
python scripts/generate_images.py mockup --marca [marca] --prompt "..." --name capa
```
