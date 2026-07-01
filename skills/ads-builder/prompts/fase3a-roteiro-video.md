# Fase 3a — Roteiro de Vídeo

Objetivo: roteiro completo de vídeo (Reels/TikTok/UGC), bloco a bloco, com ganchos multi-angulares e instruções de cena/edição para o editor. Resultado salvo em `roteiros-video.md`.

Consulte `projects/[marca]/briefing.md`, `estrategia-criativa.md`, `pattern-brief.md` (se existir) e `kill-list.md` antes de escrever. Leia `knowledge/structure-library.md` e `knowledge/editor-formats.md` no momento de escrever — não reproduza de memória.

**Escreva o roteiro inteiro no idioma e na voz do mercado-alvo** definido na Fase 0 (ver `prompts/fase4-revisao-traducao.md` se o mercado-alvo for diferente do idioma desta conversa).

---

## Regras de Tom (sempre)

- Linguagem coloquial, "papo reto" — como um influenciador do nicho fala, não como um redator publicitário
- Tom agressivo e confiante, com empatia cirúrgica nas dores ("Tough Love")
- Nunca chamar o produto de "produto" — sempre truque, segredo, descoberta ou método
- Sem aspas, sem travessões, sem expressões pouco acessíveis ao público geral
- Toda instrução de cena/edição entre colchetes: `[ASSIM]`

---

## Passo 1 — Checklist de Validação

Antes de escrever, confirme que há insumo suficiente:
- Ângulo e UMP/UMS definidos (Fase 1 + 2)
- Pelo menos 2 hook archetypes escolhidos (Fase 2)
- Avatar e dor/vergonha específicas conhecidas (não genéricas)
- O Inimigo nomeado especificamente (Fase 1)
- Entregáveis/preço/garantia reais, se forem aparecer no CTA

Para cada item incompleto, aponte o que falta e pare — não escreva com lacuna.

---

## Passo 2 — Bloco 1: Ganchos Multi-Angulares

Gere **4-5 ganchos** cobrindo arquétipos diferentes de `knowledge/hook-taxonomy.md`, priorizando os escolhidos na Fase 2:
- Opção A (Visual/Shock ou Contrarian)
- Opção B (Ouch Factor)
- Opção C (Contrarian ou Conspiração)
- Opção D (Story Tease)
- [Opção E, se fizer sentido]

**2 dos ganchos gerados devem usar um formato de execução fixo** de `knowledge/editor-formats.md` (cinematográfico, caixinha de perguntas, twitter screenshot ou ranking), com a instrução de cena correspondente entre colchetes. Os demais ficam `ugc_normal`.

Se um gancho usa `caixinha_perguntas`, gere também a pergunta exibida na tela. Se usa `twitter_screenshot`, gere o texto do tweet e o nome/handle da autoridade (coerente com o briefing).

**Pare e aguarde aprovação do(s) gancho(s)** antes de escrever o corpo — a menos que modo autônomo, caso em que você escolhe o gancho mais forte e registra por quê.

---

## Passo 3 — Corpo do Roteiro (blocos 2-8)

Depois do gancho aprovado, escreva o restante seguindo `knowledge/structure-library.md` à risca, na ordem:

2. Delimitação (O Filtro)
3. Sanduíche de Valor
4. PAS + Viés Financeiro
5. Absolvição
6. Storytelling Micro (exatamente 2 frases, reação de terceiro)
7. Empilhamento de Benefícios (3-4 ganhos, físicos + emocionais)
8. CTA Triplo (White → Gray → Black)

Aplique a estrutura invisível escolhida na Fase 2 (`logica_dopamina` \| `jornada_redencao` \| `prova_visual`) para o ritmo de revelação dentro destes blocos.

**Não escreva dois roteiros completos seguidos sem aprovação intermediária** (modo passo-a-passo). No modo autônomo, escreva o roteiro completo e avise ao final.

---

## Passo 4 — Múltiplos Corpos (se solicitado)

Se o usuário pedir mais de um corpo de anúncio (corpos diferentes para o mesmo ângulo, testando ênfases distintas — ex.: um corpo focado em revolta financeira, outro em identidade/vulnerabilidade), repita o Passo 2-3 para cada corpo, mantendo o mesmo ângulo central mas variando hook archetype e foco emocional dominante.

---

## Passo 5 — Salvar

Salve `projects/[marca]/roteiros-video.md`:

```markdown
# Roteiros de Vídeo — [Marca]

## Corpo 1 — [foco emocional/hook dominante]

### Ganchos (escolher 1 para produção, ou testar todos)
**Gancho A** [editor_format, se aplicável]
[texto do gancho]
[instruções de cena entre colchetes]

**Gancho B** ...

### Roteiro Completo
[blocos 2-8, com instruções de cena entre colchetes ao longo do texto]

---

## Corpo 2 — [se aplicável]
...
```

Atualize `kill-list.md` (ver `prompts/kill-list.md`) e `tracking/test-matrix.json` (ver `prompts/combinacoes.md`) para cada roteiro aprovado pelo usuário. Atualize `progress.md`.
