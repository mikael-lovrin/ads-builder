# Ads Builder — Direct Response Creative Builder

**Autor:** Mikael Lovrin
**Licença:** [CC BY-NC-ND 4.0](LICENSE) — uso não comercial, sem obras derivadas, com atribuição obrigatória ao autor.

Agente de IA (construído sobre [Claude Code](https://claude.com/claude-code)) que cria criativos de anúncio de Direct Response — roteiros de vídeo (Reels/TikTok/UGC) e briefings de imagem estática para Meta — a partir de um framework proprietário de copywriting de saúde/emagrecimento/suplementos. O agente mantém um corpus/knowledge base vivo, trabalha por marca/produto com kill list (nunca repete um ângulo já usado) e uma matriz de testes que transforma cada criativo numa hipótese rastreável.

Opcionalmente, o agente também **gera as imagens de fato** (não só o prompt) via API da OpenAI e/ou via conector Higgsfield, se configurados.

Este repositório é o **repo-fonte** da skill — instale uma vez, depois trabalhe em pastas dedicadas por marca, em qualquer lugar da sua máquina (ver abaixo).

---

## Requisitos

- [Claude Code](https://claude.com/claude-code) instalado (`claude --version` deve funcionar)
- Python 3.10+ (para os scripts, usados só se for gerar imagens de fato ou fazer triagem em lote do corpus)
- Opcional, só se for gerar imagens de fato:
  - Conta OpenAI com billing ativo (ver [Conectar OpenAI](#conectar-openai-geração-de-imagem))
  - Conta paga na Higgsfield (ver [Conectar Higgsfield](#conectar-higgsfield-imagem--vídeo))

---

## Instalação

1. Baixe/clone este repositório
2. Rode `Install.bat` (duplo clique, ou `.\Install.bat` num terminal). Ele copia as 3 skills (`ads-builder`, `creative-pattern-analysis`, `knowledge-updater`) para `%USERPROFILE%\.claude\skills\` — disponíveis a partir de agora em qualquer pasta, junto com seus outros agentes.

Sempre que você atualizar `knowledge/` neste repo-fonte (novos arquétipos de gancho, estruturas, etc.), rode `Install.bat` de novo para propagar a atualização a todas as marcas já criadas — elas leem a mesma cópia compartilhada, não precisam ser recriadas.

---

## Como usar (por marca)

1. Crie uma pasta vazia dedicada para a marca/produto (ex. `minhas-marcas/acme/`), fora deste repo — **nunca dentro de `ads-builder/`**
2. Abra um terminal dentro dela e rode `claude`
3. Peça em linguagem natural, por exemplo:
   - *"quero criar um anúncio pra essa marca"* → dispara o onboarding (Fase 0)
   - *"continua o projeto"* → o agente lê `progress.md` (na pasta atual) e retoma de onde parou
   - *"analisa esses anúncios de concorrente"* / *"lateraliza isso"* → dispara o skill de análise de padrão isoladamente
   - *"adiciona esse criativo ao corpus"* → dispara o knowledge-updater (corpus local desta marca)

Não existe comando de barra dedicado — o roteamento é feito pelo próprio Claude Code lendo `SKILL.md` de cada skill instalada, pela descrição da tarefa pedida. Todos os arquivos gerados (`briefing.md`, `kill-list.md`, `tracking/`, `output/imagens/`) ficam centralizados nesta mesma pasta — nada é escrito de volta neste repo-fonte.

---

## Estrutura — repo-fonte vs. pasta de marca

```
ads-builder/  (repo-fonte — onde a skill é mantida, não onde você trabalha)
├── CLAUDE.md
├── README.md                         ← este arquivo
├── LICENSE                           ← CC BY-NC-ND 4.0
├── Install.bat                       ← copia as skills para ~/.claude/skills/
├── .mcp.json                         ← config de conectores MCP deste repo (ex.: higgsfield) — versionável, sem segredo
│
└── skills/
    ├── ads-builder/
    │   ├── SKILL.md                      ← orquestrador principal
    │   ├── knowledge/                    ← base de conhecimento (bundled, compartilhada entre marcas)
    │   ├── corpus-seed/                  ← baseline de exemplos (bundled, somente leitura em runtime)
    │   ├── scripts/                      ← generate_images.py, build_corpus_index.py (rodam na pasta da marca)
    │   ├── requirements.txt
    │   ├── .env.example
    │   └── prompts/                      ← fase0 a fase4, kill-list.md, combinacoes.md
    ├── creative-pattern-analysis/
    │   └── SKILL.md                      ← lateralização — analisa referências → Lateralization Brief
    └── knowledge-updater/
        ├── SKILL.md                      ← extração/curadoria — compartilhada (aqui) ou local (numa marca)
        ├── extraction-protocol.md
        ├── export-prompt.md              ← prompt pronto para minerar conversas antigas de outro projeto
        └── adapters/social-creative.md
```

```
[pasta da marca, ex. minhas-marcas/acme/]  (onde você trabalha, criada por você)
├── progress.md                       ← estado atual (gerenciado silenciosamente pelo agente)
├── briefing.md                       ← Fase 0 + Fase 1 (dados reais do produto)
├── pattern-brief.md                  ← se veio de lateralização (Cenário A)
├── estrategia-criativa.md            ← Fase 2 (ângulo, gancho, estrutura escolhidos)
├── roteiros-video.md                 ← Fase 3a, se o tipo de anúncio inclui vídeo
├── briefing-imagem.md                ← Fase 3b, se o tipo de anúncio inclui imagem
├── kill-list.md                      ← ângulos/ganchos/histórias já usados — nunca repetir
├── brand/                            ← opcional — logo, fotos de produto, paleta (Fase 3c modo mockup)
├── corpus/                            ← opcional — corpus específico desta marca, isolado (via knowledge-updater)
├── output/imagens/                   ← PNGs gerados de fato (Fase 3c) + manifest.json
└── tracking/
    ├── test-matrix.json              ← matriz de combinações testadas + backlog
    ├── insights.md                   ← biblioteca de aprendizados desta marca
    └── sugestoes-log.json            ← histórico de sugestões feitas
```

Nada na pasta da marca precisa ser criado manualmente — o agente cuida disso ao longo do fluxo, a partir da pasta vazia do Passo 1.

---

## Todas as formas que o agente atua

### 1. Fluxo principal — criar um criativo do zero (`ads-builder`)
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

### 2. Lateralização de anúncios (`creative-pattern-analysis`)
Roda standalone (você manda criativos e pede análise) ou automaticamente como pré-passo da Fase 2. Faz engenharia reversa da estrutura invisível de criativos de referência (11 dimensões: ângulo de venda, disfarce, mecanismo, sequenciamento de blocos, etc.), separa `[OBSERVAÇÃO]` de `[INFERÊNCIA]` de `[HIPÓTESE]`, e entrega um brief para escrever algo com o mesmo DNA estrutural — **nunca um clone**. Pergunta de verificação central: *"se eu trocasse o produto, o avatar e a história, essa estrutura ainda faria sentido?"*

### 3. Crescimento do corpus (`knowledge-updater`)
Extrai, classifica e propõe atualizações a partir de novos criativos validados (colados na conversa ou salvos em `corpus/raw/`). Tem dois escopos (pergunta no início da sessão, ver `SKILL.md` > Passo -1):
- **Local** — rodando dentro da pasta de uma marca: cria/atualiza um `corpus/` isolado daquela marca só.
- **Compartilhado** — rodando aqui no repo-fonte: atualiza `skills/ads-builder/knowledge/` e `corpus-seed/`, que todas as marcas passam a ler assim que você rodar `Install.bat` de novo.

Para minerar conversas antigas fora deste projeto (sempre em escopo Compartilhado), usa `skills/knowledge-updater/export-prompt.md`.

### 4. Gestão automática de estado
- `progress.md` por marca — atualizado silenciosamente a cada fase, permite retomar sessões
- `kill-list.md` por marca — nunca repete ângulo/gancho/narrativa já usado
- `tracking/test-matrix.json` — cada criativo aprovado vira uma hipótese rastreável (ângulo × tipo × hook × emoção × estrutura × plataforma); ao reportar resultado, o agente atualiza a matriz e sugere o próximo teste

---

## Conexões possíveis (geração de imagem/vídeo de fato)

Por padrão o agente só **escreve o brief** (prompt de imagem, roteiro de vídeo) — a geração do arquivo final é opcional e depende de você conectar um provedor. Sem nenhuma conexão configurada, o fluxo funciona normalmente até a Fase 3b/3a e você copia o prompt manualmente para onde quiser.

### Conectar OpenAI (geração de imagem)

1. Crie uma chave em [platform.openai.com](https://platform.openai.com) → Settings → API keys (exige billing ativo e, para `gpt-image-1`, verificação de organização em Settings → Organization → General → Verify Organization)
2. `pip install -r ~/.claude/skills/ads-builder/requirements.txt` (uma vez só, não por marca)
3. Na pasta da marca, copie `~/.claude/skills/ads-builder/.env.example` para `.env` e cole a chave: `OPENAI_API_KEY=sk-...` (o `.env` fica só naquela pasta, não é commitado em lugar nenhum)
4. Use a Fase 3c (`skills/ads-builder/prompts/fase3c-geracao-imagem.md`) ou rode direto, de dentro da pasta da marca:
   ```bash
   python "$HOME/.claude/skills/ads-builder/scripts/generate_images.py" dr --corpo 1 --estilo realistic_photography
   python "$HOME/.claude/skills/ads-builder/scripts/generate_images.py" mockup --prompt "..." --ref brand/logo.png
   ```
   (No Windows: `%USERPROFILE%\.claude\skills\ads-builder\scripts\generate_images.py`.)
   - Modo `dr` — gera os image ads do `briefing-imagem.md` sem assets de marca (regra do framework: produto/logo não aparecem no frame desses criativos, é isso que os faz parecer nativos)
   - Modo `mockup` — criativo pontual com logo/produto de verdade, usando os assets de `brand/` (na pasta da marca)

### Conectar Higgsfield (imagem + vídeo)

Se você tem conta paga na Higgsfield, dá para conectar o servidor MCP dela direto no Claude Code — sem gerenciar API key, autenticação é OAuth com a própria conta. Como a conexão é `--scope project`, rode isto **de dentro da pasta da marca** (não deste repo-fonte):

```bash
claude mcp add --transport http --scope project higgsfield https://mcp.higgsfield.ai/mcp
```

Depois, dentro de uma sessão `claude` naquela pasta: aprove o servidor quando o prompt aparecer, rode `/mcp` → selecione `higgsfield` → `Authenticate`, faça login no navegador. Confirme com `claude mcp list` (deve mostrar `✔ Connected`).

**Com a conta Higgsfield conectada, o agente ganha ferramentas diretas de geração** — ele mesmo escreve o prompt final e chama a geração de imagem (até 4K) ou vídeo (até 15s por clipe, vários estilos cinematográficos, inclusive personagem consistente via "Soul") sem sair da conversa. Importante: a integração precisa de uma sessão do Claude Code iniciada **depois** que a conexão foi estabelecida — conectores MCP não aparecem em sessões que já estavam abertas antes. Se quiser Higgsfield disponível em toda marca nova, repita o comando `claude mcp add` em cada pasta (ou use `--scope user` para deixar disponível globalmente, em vez de por pasta).

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
