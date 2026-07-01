# Ads Builder — Direct Response Creative Builder

**Autor:** Mikael Lovrin
**Licença:** [CC BY-NC-ND 4.0](LICENSE) — uso não comercial, sem obras derivadas, com atribuição obrigatória ao autor.

Agente de IA (construído sobre [Claude Code](https://claude.com/claude-code)) que cria criativos de anúncio de Direct Response — roteiros de vídeo (Reels/TikTok/UGC) e briefings de imagem estática para Meta — a partir de um framework proprietário de copywriting de saúde/emagrecimento/suplementos. O agente mantém um corpus/knowledge base vivo, trabalha por marca/produto com kill list (nunca repete um ângulo já usado) e uma matriz de testes que transforma cada criativo numa hipótese rastreável.

Opcionalmente, o agente também **gera as imagens de fato** (não só o prompt) via API da OpenAI e/ou via conector Higgsfield, se configurados.

---

## Requisitos

- [Claude Code](https://claude.com/claude-code) instalado (`claude --version` deve funcionar)
- Python 3.10+ (para os scripts em `scripts/`)
- Opcional, só se for gerar imagens de fato:
  - Conta OpenAI com billing ativo (ver [Conectar OpenAI](#conectar-openai-geração-de-imagem))
  - Conta paga na Higgsfield (ver [Conectar Higgsfield](#conectar-higgsfield-imagem--vídeo))

---

## Como chamar o agente

1. Abra um terminal **dentro desta pasta** (`ads-builder/`) — o agente não precisa de instalação, o corpus e o knowledge base já vivem aqui
2. Rode `claude`
3. Peça em linguagem natural, por exemplo:
   - *"quero criar um anúncio para a marca X"* → dispara o onboarding (Fase 0)
   - *"continua o projeto da marca X"* → o agente lê `projects/X/progress.md` e retoma de onde parou
   - *"analisa esses anúncios de concorrente"* / *"lateraliza isso"* → dispara o skill de análise de padrão isoladamente
   - *"adiciona esse criativo ao corpus"* → dispara o knowledge-updater

Não existe comando de barra dedicado — o roteamento é feito pelo próprio Claude Code lendo `skills/ads-builder/SKILL.md` (e os outros `SKILL.md`) pela descrição da tarefa pedida.

---

## Estrutura de pastas — o que precisa existir

```
ads-builder/
├── CLAUDE.md                         ← instruções do projeto para o agente (não editar sem entender o impacto)
├── README.md                         ← este arquivo
├── LICENSE                           ← CC BY-NC-ND 4.0
├── COPY PROMPTS.docx                 ← fonte original dos prompts (não editar)
├── requirements.txt                  ← dependências Python (openai)
├── .env.example                      ← modelo de variáveis de ambiente (copiar para .env)
├── .mcp.json                         ← config de conectores MCP do projeto (ex.: higgsfield) — versionável, sem segredo
│
├── referencias/
│   └── copy-prompts-extraido.md      ← transcrição legível do docx original
│
├── corpus/                           ← banco de criativos validados (cresce com o uso)
│   ├── index.json                    ← índice com metadados de todas as entries
│   ├── entries/                      ← JSONs de intelligence extraída (hook, estrutura, estilo)
│   ├── raw/                          ← (criado sob demanda) materiais crus aguardando triagem
│   └── updater-log.json              ← log de sessões do knowledge-updater
│
├── knowledge/                        ← base de conhecimento estruturada (fundação do framework)
│   ├── hook-taxonomy.md              ← arquétipos de gancho (niche-agnostic)
│   ├── structure-library.md          ← estrutura de 8 blocos + 3 estruturas invisíveis + CTA triplo
│   ├── static-image-psychology.md    ← 10 princípios de conversão + 5 estilos visuais fixos
│   └── editor-formats.md             ← formatos de execução/edição
│
├── projects/                         ← criado sob demanda, um subdiretório por marca/produto
│   └── [marca]/
│       ├── progress.md               ← estado atual (gerenciado silenciosamente pelo agente)
│       ├── briefing.md               ← Fase 0 + Fase 1 (dados reais do produto)
│       ├── pattern-brief.md          ← se veio de lateralização (Cenário A)
│       ├── estrategia-criativa.md    ← Fase 2 (ângulo, gancho, estrutura escolhidos)
│       ├── roteiros-video.md         ← Fase 3a, se o tipo de anúncio inclui vídeo
│       ├── briefing-imagem.md        ← Fase 3b, se o tipo de anúncio inclui imagem
│       ├── kill-list.md              ← ângulos/ganchos/histórias já usados — nunca repetir
│       ├── brand/                    ← opcional — logo, fotos de produto, paleta (Fase 3c modo mockup)
│       ├── output/imagens/           ← PNGs gerados de fato (Fase 3c) + manifest.json
│       └── tracking/
│           ├── test-matrix.json      ← matriz de combinações testadas + backlog
│           ├── insights.md           ← biblioteca de aprendizados por marca
│           └── sugestoes-log.json    ← histórico de sugestões feitas
│
├── scripts/
│   ├── build_corpus_index.py         ← regenera corpus/index.json a partir de corpus/entries|raw
│   └── generate_images.py            ← gera imagens de fato via OpenAI (Fase 3c)
│
└── skills/
    ├── ads-builder/
    │   ├── SKILL.md                      ← orquestrador principal — leia primeiro para entender o fluxo
    │   └── prompts/
    │       ├── fase0-onboarding.md       ← sempre roda primeiro num projeto novo
    │       ├── fase1-extracao-produto.md
    │       ├── fase2-estrategia-criativa.md
    │       ├── fase3a-roteiro-video.md
    │       ├── fase3b-briefing-imagem.md
    │       ├── fase3c-geracao-imagem.md  ← opcional — gera PNGs de fato (OpenAI)
    │       ├── fase4-revisao-traducao.md ← opcional
    │       ├── kill-list.md              ← protocolo de atualização da kill list
    │       └── combinacoes.md            ← protocolo da matriz de testes
    ├── creative-pattern-analysis/
    │   └── SKILL.md                      ← lateralização — analisa referências → Lateralization Brief
    └── knowledge-updater/
        ├── SKILL.md                      ← extração/curadoria de novos materiais para o corpus
        ├── extraction-protocol.md
        ├── export-prompt.md              ← prompt pronto para minerar conversas antigas de outro projeto
        └── adapters/social-creative.md
```

**Únicas pastas que não vêm prontas** (o agente cria sob demanda): `corpus/raw/`, `projects/`, e dentro de cada marca, `brand/` e `output/`. Nada disso precisa ser criado manualmente — o agente cuida disso ao longo do fluxo.

> **Nota:** `projects/` (dados reais de marca/cliente) está no `.gitignore` — não é enviado a este repositório público. Cada marca fica só na máquina local de quem está rodando o agente.

---

## Todas as formas que o agente atua

### 1. Fluxo principal — criar um criativo do zero (`skills/ads-builder`)
Por marca/produto, em fases sequenciais (aprovação humana em cada uma, ou modo autônomo escolhido na Fase 0):

| Fase | O que faz | Sempre roda? |
|---|---|---|
| 0 — Onboarding | Define marca, mercado, plataforma, tipo de anúncio, modo (passo-a-passo/autônomo) | Sim |
| 1 — Extração de Produto | Extrai UMP, UMS, autoridade, inimigo, oferta, garantia — só dados reais, nunca inventados | Sim |
| Lateralização (pré-passo) | Se você tem referências (concorrente ou vencedores próprios), analisa e gera `pattern-brief.md` | Só Cenário A |
| 2 — Estratégia Criativa | Propõe ângulo, arquétipo(s) de gancho e estrutura — consultando `kill-list.md` e o corpus | Sim |
| 3a — Roteiro de Vídeo | Roteiro completo bloco a bloco, 4-5 ganchos multi-angulares, quantos corpos você pedir | Se tipo inclui vídeo |
| 3b — Briefing de Imagem | 2 corpos × 5 estilos visuais fixos = 10 image ads (prompt + hook + body copy cada) | Se tipo inclui imagem |
| 3c — Geração de Imagem | Gera os PNGs de fato via API (opcional, só com aprovação explícita de quais) | Opcional |
| 4 — Revisão/Tradução | Revisa ou traduz o material gerado | Sob pedido |

### 2. Lateralização de anúncios (`skills/creative-pattern-analysis`)
Roda standalone (você manda criativos e pede análise) ou automaticamente como pré-passo da Fase 2. Faz engenharia reversa da estrutura invisível de criativos de referência (11 dimensões: ângulo de venda, disfarce, mecanismo, sequenciamento de blocos, etc.), separa `[OBSERVAÇÃO]` de `[INFERÊNCIA]` de `[HIPÓTESE]`, e entrega um brief para escrever algo com o mesmo DNA estrutural — **nunca um clone**. Pergunta de verificação central: *"se eu trocasse o produto, o avatar e a história, essa estrutura ainda faria sentido?"*

### 3. Crescimento do corpus (`skills/knowledge-updater`)
Extrai, classifica e propõe atualizações ao `knowledge/` a partir de novos criativos validados (colados na conversa ou salvos em `corpus/raw/`). Roda `scripts/build_corpus_index.py` para triagem rápida por palavra-chave; a extração profunda (schema completo) é feita pelo skill. Para minerar conversas antigas fora deste projeto, usa `skills/knowledge-updater/export-prompt.md`.

### 4. Gestão automática de estado
- `progress.md` por marca — atualizado silenciosamente a cada fase, permite retomar sessões
- `kill-list.md` por marca — nunca repete ângulo/gancho/narrativa já usado
- `tracking/test-matrix.json` — cada criativo aprovado vira uma hipótese rastreável (ângulo × tipo × hook × emoção × estrutura × plataforma); ao reportar resultado, o agente atualiza a matriz e sugere o próximo teste

---

## Conexões possíveis (geração de imagem/vídeo de fato)

Por padrão o agente só **escreve o brief** (prompt de imagem, roteiro de vídeo) — a geração do arquivo final é opcional e depende de você conectar um provedor. Sem nenhuma conexão configurada, o fluxo funciona normalmente até a Fase 3b/3a e você copia o prompt manualmente para onde quiser.

### Conectar OpenAI (geração de imagem)

1. Crie uma chave em [platform.openai.com](https://platform.openai.com) → Settings → API keys (exige billing ativo e, para `gpt-image-1`, verificação de organização em Settings → Organization → General → Verify Organization)
2. `pip install -r requirements.txt`
3. Copie `.env.example` para `.env` e cole a chave: `OPENAI_API_KEY=sk-...` (o `.env` já está no `.gitignore` — nunca é commitado)
4. Use a Fase 3c (`skills/ads-builder/prompts/fase3c-geracao-imagem.md`) ou rode direto:
   ```bash
   python scripts/generate_images.py dr --marca [marca] --corpo 1 --estilo realistic_photography
   python scripts/generate_images.py mockup --marca [marca] --prompt "..." --ref brand/logo.png
   ```
   - Modo `dr` — gera os image ads do `briefing-imagem.md` sem assets de marca (regra do framework: produto/logo não aparecem no frame desses criativos, é isso que os faz parecer nativos)
   - Modo `mockup` — criativo pontual com logo/produto de verdade, usando os assets de `projects/[marca]/brand/`

### Conectar Higgsfield (imagem + vídeo)

Se vocês têm conta paga na Higgsfield, dá para conectar o servidor MCP dela direto no Claude Code — sem gerenciar API key, autenticação é OAuth com a própria conta:

```bash
claude mcp add --transport http --scope project higgsfield https://mcp.higgsfield.ai/mcp
```

Depois, dentro de uma sessão `claude` nesta pasta: aprove o servidor quando o prompt aparecer, rode `/mcp` → selecione `higgsfield` → `Authenticate`, faça login no navegador. Confirme com `claude mcp list` (deve mostrar `✔ Connected`).

**Com a conta Higgsfield conectada, o agente ganha ferramentas diretas de geração** — ele mesmo escreve o prompt final e chama a geração de imagem (até 4K) ou vídeo (até 15s por clipe, vários estilos cinematográficos, inclusive personagem consistente via "Soul") sem sair da conversa. Importante: a integração precisa de uma sessão do Claude Code iniciada **depois** que a conexão foi estabelecida — conectores MCP não aparecem em sessões que já estavam abertas antes.

---

## Princípios fundamentais

- Ganchos e estruturas são niche-agnostic — o gatilho psicológico é universal, o nicho/produto é substituível
- Sempre consulta `kill-list.md` por marca antes de sugerir ângulo/gancho — nunca repete uma narrativa já usada
- Nunca inventa dado de produto (UMP, UMS, autoridade, oferta, garantia) — só entra se confirmado pelo usuário ou extraído do briefing real
- Nunca inventa performance — sem métrica reportada, resultado fica `null`/`"draft"` na matriz
- Saída em duas camadas — o brief escrito é sempre revisado por humano antes de qualquer geração/produção final

---

## Copyright

© 2026 Mikael Lovrin. Este trabalho é licenciado sob [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/) — dê crédito ao autor, não use para fins comerciais, não distribua versões modificadas.
