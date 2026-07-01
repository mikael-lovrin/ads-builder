# Fase 3b — Briefing de Imagem Estática

Objetivo: brief completo de criativos de imagem estática (Meta), com pesquisa de psicologia aplicada ao avatar específico, 2 corpos x 5 estilos visuais fixos = 10 image ads (prompt de imagem + hook + body copy cada), e notas de produção. Resultado salvo em `briefing-imagem.md`.

Consulte `projects/[marca]/briefing.md`, `estrategia-criativa.md`, `pattern-brief.md` (se existir) e `kill-list.md` antes de escrever. Leia `knowledge/static-image-psychology.md` no momento de escrever — não reproduza de memória.

**Escreva todo o brief no idioma e na voz do mercado-alvo** definido na Fase 0.

---

## Passo 1 — Confirmar Extração

Releia o que foi extraído na Fase 1 (`briefing.md`, seção Extração de Produto) e apresente de volta ao usuário em lista limpa:

```
Confirmando os dados que vou usar neste brief:
- UMP: [...]
- UMS: [...]
- Autoridade: [...]
- O Inimigo: [...]
- Número-herói (resultado mais forte): [extrair do briefing, ou perguntar se não há]
- Oferta e Garantia: [...]

Está correto? Alguma correção antes de eu escrever o brief?
```

Só prossiga após confirmação (ou, em modo autônomo, prossiga e registre que a extração foi assumida como está em `briefing.md`).

---

## Passo 2 — Seção de Pesquisa de Psicologia

Antes de escrever qualquer hook ou prompt de imagem, escreva uma seção de pesquisa que:
- Aplique pelo menos 6 dos 10 princípios de `knowledge/static-image-psychology.md`
- Conecte cada princípio diretamente a ESTE avatar, dor e categoria de produto — nunca observação genérica
- Identifique o ponto de entrada emocional dominante para este avatar (vergonha, raiva, esperança, curiosidade, FOMO) e por quê
- Identifique o pivô emocional secundário (o que a imagem precisa fazer o espectador sentir DEPOIS do scroll-stop)
- Defina a linguagem visual do estado-problema vs. estado-solução para este produto específico
- Aponte restrições específicas da plataforma definida na Fase 0

Esta seção não é decoração — é a base que justifica cada escolha criativa do brief.

---

## Passo 3 — Os Dois Corpos

Produza **2 corpos completos**, cada um com 5 image ads (um por estilo visual fixo, sempre nesta ordem: `realistic_photography` → `documentary_raw` → `editorial_illustration` → `cartoon` → `infographic`):

- **Corpo 1** — primeira pessoa, voz da figura de autoridade (médico, fundadora, especialista) que descobriu a solução e está tentando compartilhar
- **Corpo 2** — terceira pessoa, a autoridade é um personagem sendo apresentado; o espectador está prestes a descobrir algo que foi escondido dele

Para cada um dos 10 image ads, gere:
1. **Prompt de imagem** — seguindo as 12 regras obrigatórias de `knowledge/static-image-psychology.md` (estilo, dimensões, sujeito, ação, ambiente, iluminação, paleta nomeada, o que não está no frame, texto na imagem se houver, câmera/composição, tom emocional, aspect ratio 1:1)
2. **Hook** — usando os arquétipos de `knowledge/hook-taxonomy.md` escolhidos na Fase 2
3. **Body copy completo** — seguindo as 8 partes obrigatórias de `knowledge/static-image-psychology.md` (Hook/Scroll Stop → Delimitação → Sanduíche de Valor → PAS+Dor Financeira → Absolvição → Storytelling Micro → Empilhamento → CTA), em prosa corrida, sem rótulos visíveis, respeitando todas as regras de copy (sem aspas, sem travessões, sem "jornada", sem exclamação genérica, todo número vem do briefing real)

**Pare após o Corpo 1** e aguarde aprovação antes de escrever o Corpo 2 (modo passo-a-passo). Modo autônomo: escreva os dois e avise ao final.

---

## Passo 4 — Production Notes

Encerre o brief com:
- Sequência de teste recomendada (quais 2 imagens rodar primeiro e por quê, quais guardar para retargeting)
- Sugestão de teste A/B (uma variável específica para a primeira semana)
- Restrições da plataforma definida na Fase 0
- Uma flag honesta de claim que precisa de revisão legal, se houver
- Uma observação criativa não usada neste brief mas com potencial futuro

---

## Passo 5 — Salvar

Salve `projects/[marca]/briefing-imagem.md` com a estrutura: Pesquisa de Psicologia → Corpo 1 (5 image ads) → Corpo 2 (5 image ads) → Production Notes.

**Cada um dos 10 image ads precisa usar exatamente este cabeçalho de seção** (é o formato que `scripts/generate_images.py` faz parsing para a Fase 3c — geração de imagem):

```markdown
### Corpo 1 — realistic_photography

**Prompt de Imagem:**
[prompt completo seguindo as 12 regras obrigatórias, nesta ordem]

**Hook:**
[texto do hook]

**Body copy:**
[corpo completo em prosa corrida]
```

Repita para os 5 estilos (`realistic_photography`, `documentary_raw`, `editorial_illustration`, `cartoon`, `infographic`) dentro de cada corpo, sempre `### Corpo N — [estilo_id]`, usando o `estilo_id` exato (sem espaços, snake_case).

Atualize `kill-list.md` (ver `prompts/kill-list.md`) e `tracking/test-matrix.json` (ver `prompts/combinacoes.md`) para cada brief aprovado pelo usuário. Atualize `progress.md`.

Depois de aprovado, ofereça a Fase 3c (`prompts/fase3c-geracao-imagem.md`) para gerar as imagens de fato via API.
