# Fase 3c — Geração de Imagem (opcional)

Objetivo: transformar prompts aprovados de `briefing-imagem.md` em arquivos PNG de fato, via API da OpenAI (`gpt-image-1`), sem gerar as 10 imagens automaticamente (custo). Executada via `scripts/generate_images.py` (bundled na skill, não no diretório do projeto) — você (Claude) monta o comando, explica o que vai acontecer, e roda com aprovação do usuário.

Só entra depois que o usuário aprovou o `briefing-imagem.md` (Fase 3b) por escrito.

---

## Dois modos — não confundir

### Modo `dr` (default — os 10 image ads do brief)
Gera a partir dos prompts já escritos em `briefing-imagem.md` (na pasta do projeto atual), texto puro, **sem anexar nenhum asset de marca**. Isso é proposital: a regra 8 das "Regras Obrigatórias de Prompt de Imagem" (`knowledge/static-image-psychology.md`) exige que produto e logo NÃO apareçam no frame — é o que faz a imagem parecer nativa/orgânica e parar o scroll. Anexar o logo aqui quebraria a lógica do criativo.

### Modo `mockup` (criativo pontual com marca)
Para quando o usuário quer um criativo com produto/logo de fato visível (embalagem em cima de mesa, print de app, mockup de página de vendas) — fora da lógica "black hat" do brief de 10 imagens. Aqui sim os assets de `brand/` (logo, fotos de produto, paleta, na pasta do projeto atual) entram como referência via `images.edit`.

---

## Passo 1 — Confirmar assets de marca (uma vez por projeto)

Se `brand/` não existir na pasta do projeto e o usuário mencionar que vai precisar de criativos com logo/mockup, peça os arquivos (logo em PNG/SVG, fotos do produto, paleta de cores/brandbook) e salve ali. Não é obrigatório para o modo `dr`.

---

## Passo 2 — Escolher o que gerar

Nunca gere as 10 imagens de uma vez sem perguntar. Depois do brief aprovado, pergunte:

```
Brief aprovado. Quer que eu já gere alguma imagem via OpenAI?
- Eu recomendaria começar por [corpo X, estilo Y] e [corpo X, estilo Z] — são as
  duas indicadas na Sequência de Teste Recomendada das Production Notes.
- Cada imagem tem custo na API (gpt-image-1). Posso gerar só essas 2, todas as 10,
  ou você me diz quais.
```

Modo autônomo: gere apenas as 2 recomendadas na Sequência de Teste, avise o custo aproximado, e pare — não gere as 10 sem pedido explícito.

---

## Passo 3 — Rodar o script

O script vive dentro da skill instalada, não no diretório do projeto — rode-o sempre com o caminho completo, mas ele opera sobre os arquivos da pasta atual (onde o Claude Code foi aberto). No Windows, o caminho é `%USERPROFILE%\.claude\skills\ads-builder\scripts\generate_images.py`.

```bash
# modo dr — uma imagem específica
python "$HOME/.claude/skills/ads-builder/scripts/generate_images.py" dr --corpo 1 --estilo realistic_photography

# modo dr — todas as do corpo 1
python "$HOME/.claude/skills/ads-builder/scripts/generate_images.py" dr --corpo 1 --estilo all

# modo mockup — criativo com logo/produto
python "$HOME/.claude/skills/ads-builder/scripts/generate_images.py" mockup --prompt "[prompt livre]" --name capa-mockup
```

Pré-requisito: `OPENAI_API_KEY` em `.env` na pasta do projeto atual (copie de `~/.claude/skills/ads-builder/.env.example`) ou como variável de ambiente. Se faltar, o script avisa e para — não invente uma chave nem peça pra rodar sem uma. Pacote `openai` precisa estar instalado (`pip install -r ~/.claude/skills/ads-builder/requirements.txt`, uma vez só, não por projeto).

O script depende do brief estar salvo no formato de seções do Passo 5 de `fase3b-briefing-imagem.md` (`### Corpo N — estilo_id` seguido de `**Prompt de Imagem:**`). Se o parsing falhar, é sinal de que o brief não seguiu o formato — corrija antes de tentar gerar.

---

## Passo 4 — Registrar

Cada geração já cria/atualiza `output/imagens/manifest.json` automaticamente (arquivo, corpo, estilo, prompt, timestamp), na pasta do projeto atual. Depois de gerar:

- Aponte ao usuário onde os arquivos ficaram salvos
- Se o teste já tem uma entrada em `tracking/test-matrix.json` (ver `prompts/combinacoes.md`), referencie o nome do arquivo gerado nela
- Atualize `progress.md`

Regeneração/iteração: se o usuário quiser ajustar uma imagem específica, edite o prompt correspondente em `briefing-imagem.md` e rode o mesmo comando de novo — o script versiona automaticamente (`-v1`, `-v2`...), nunca sobrescreve.
