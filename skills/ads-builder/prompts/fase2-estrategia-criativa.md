# Fase 2 — Estratégia Criativa

Objetivo: escolher o ângulo, o(s) arquétipo(s) de gancho e a(s) estrutura/estilo que vão guiar a escrita. Resultado salvo em `estrategia-criativa.md`.

---

## Passo 1 — Ler Insumos

Antes de propor qualquer coisa, leia:
1. `briefing.md` (produto, avatar, nicho, plataforma, tipo de anúncio), na pasta do projeto atual
2. `pattern-brief.md`, se existir (Cenário A — lateralização)
3. `kill-list.md`, se existir — **nunca proponha um ângulo/gancho/narrativa já listado lá**
4. `corpus-seed/index.json` (bundled na skill) e, se precisar de detalhe, os `corpus-seed/entries/*.json` relevantes — filtre por nicho e emoção próximos ao avatar do briefing. Se a pasta do projeto já tiver um `corpus/index.json` local (extrações específicas desta marca), consulte também
5. `knowledge/hook-taxonomy.md` e `knowledge/structure-library.md` (e `knowledge/static-image-psychology.md` se o tipo de anúncio inclui imagem)

---

## Passo 2 — Propor Ângulo

Um ângulo = a premissa central + o mecanismo único que vai sustentar o criativo. Use o UMP/UMS extraídos na Fase 1.

Apresente **2-3 opções de ângulo**, cada uma com:
- Premissa central em 1 frase
- Por que esse ângulo é forte para este avatar/nicho (cite o corpus ou o `pattern-brief.md` se aplicável)
- Confirmação explícita de que não colide com nada em `kill-list.md`

Se Cenário C (ângulo já definido pelo usuário), pule esta etapa — registre o ângulo fornecido.

---

## Passo 3 — Propor Hook Archetype(s)

Com base em `knowledge/hook-taxonomy.md`, proponha **3-4 arquétipos de gancho** compatíveis com o ângulo escolhido e o avatar. Para cada um:
- ID e nome (ex.: `ouch_factor` — Ouch Factor)
- Por que combina com este avatar/ângulo
- Um exemplo de gancho real já escrito para este produto (não genérico — usar os dados do briefing)

Se o tipo de anúncio inclui vídeo, indique também sugestão de `editor_format` (`knowledge/editor-formats.md`) por gancho.

---

## Passo 4 — Propor Estrutura/Estilo

- Se **vídeo**: proponha qual das 3 estruturas invisíveis (`logica_dopamina` \| `jornada_redencao` \| `prova_visual`, ver `knowledge/structure-library.md`) melhor serve o objetivo deste teste (retenção vs. conversão vs. resultado rápido) — pergunte ao usuário qual é o objetivo principal do teste se não estiver claro.
- Se **imagem**: lembre que o briefing de imagem sempre usa os 5 estilos fixos (não é uma escolha) — esta etapa só registra a emoção dominante e o tom (ver `knowledge/static-image-psychology.md`).

---

## Passo 5 — Aguardar Aprovação

Apresente as opções com clareza, sem escolher pelo usuário, explicando brevemente o raciocínio de cada uma. **Aguarde a escolha do usuário antes de seguir** — a menos que o modo de execução seja autônomo (Fase 0), caso em que você escolhe e registra o porquê.

---

## Passo 6 — Consolidar e Salvar

Salve `estrategia-criativa.md` na pasta do projeto atual:

```markdown
# Estratégia Criativa — [Marca]

## Ângulo
[premissa central + por que funciona para este avatar]

## Hook Archetype(s) Escolhido(s)
- [ID] — [por que] [+ editor_format sugerido, se vídeo]

## Estrutura/Estilo
[logica_dopamina | jornada_redencao | prova_visual — se vídeo]
[5 estilos fixos confirmados — se imagem]

## Decisão (se modo autônomo)
[o que foi escolhido e por quê]
```

Atualize `progress.md` (Última fase: Fase 2, Próxima fase: Fase 3a e/ou 3b conforme tipo de anúncio definido na Fase 0).
