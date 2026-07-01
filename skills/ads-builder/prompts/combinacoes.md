# Combinações — Protocolo de Matriz de Testes

> Este arquivo define como o Ads Builder mapeia, prioriza e avalia combinações de variáveis. O objetivo é transformar a criação de criativos em iteração científica: cada criativo testa uma hipótese específica, cada resultado informa o próximo. Adaptado do protocolo equivalente do projeto irmão `adv-agent` (`skills/adv-builder/prompts/combinacoes.md`) para o domínio de criativos de anúncio.

---

## Por que uma Matriz de Combinações?

Um criativo de DR é definido por 6 variáveis independentes. Cada combinação é uma **hipótese**: "acreditamos que [ângulo X + tipo Y + gancho Z + emoção W + estrutura/estilo V + plataforma U] converte porque [razão baseada em corpus/testes anteriores]."

O processo: 1. Formular a hipótese → 2. Escrever o criativo → 3. Lançar → 4. Interpretar resultado → 5. Gerar próxima hipótese

---

## As 6 Dimensões

### D1: ÂNGULO
Definido pelo usuário por projeto. Exemplos: `"cortisol-noturno"`, `"big-pharma-escondeu"`, `"hormonio-desligado"`.
- Cada ângulo = premissa central + mecanismo único (UMP/UMS)
- É a variável mais cara de testar. Só mude de ângulo quando esgotou gancho e estrutura/estilo.

### D2: TIPO DE CRIATIVO
| ID | Nome |
|---|---|
| `video_script` | Roteiro de Vídeo (Reels/TikTok/UGC) |
| `static_image` | Imagem Estática (Meta) |

### D3: HOOK ARCHETYPE
IDs válidos — ref: `knowledge/hook-taxonomy.md` (lista completa com fórmulas e exemplos)

| ID | Gatilho principal |
|---|---|
| `aviso_reverso` | Curiosidade + Aversão à perda |
| `conspiracao_revelada` | Raiva externa + FOMO |
| `injustica_comparativa` | Identificação + Inveja construtiva |
| `transformacao_visual_especifica` | Praticidade + Autoridade confiada |
| `ouch_factor` | Vergonha social + Identificação |
| `contrarian` | Curiosidade + Raiva externa |
| `story_tease` | Curiosidade |
| `visual_shock_asmr` | Curiosidade (pré-cognitiva) |
| `revolta_financeira` | Raiva externa + Aversão à perda |
| `identidade_vulnerabilidade` | Identificação + Pertencimento |

### D4: EMOÇÃO DOMINANTE
IDs válidos (vocabulário compartilhado com o `adv-agent`, ver `knowledge/hook-taxonomy.md`):

`medo` | `vergonha` | `raiva` | `desejo` | `inveja` | `esperanca` | `curiosidade` | `orgulho` | `inspiracao` | `culpa_absolvida`

### D5: ESTRUTURA/ESTILO
Depende do tipo de criativo (D2):
- Se `video_script` — ref: `knowledge/structure-library.md`: `logica_dopamina` | `jornada_redencao` | `prova_visual`
- Se `static_image` — ref: `knowledge/static-image-psychology.md`: `realistic_photography` | `documentary_raw` | `editorial_illustration` | `cartoon` | `infographic`

### D6: PLATAFORMA
`meta_feed` | `reels` | `tiktok` | `pinterest` | `stories`

---

## Schema: tracking/test-matrix.json

```json
{
  "brand": "nome-da-marca",
  "niche": "saude_emagrecimento",
  "last_updated": "2026-06-30",
  "active_angle": "nome-do-angulo-atual",

  "tests": [
    {
      "id": "test-001",
      "date_created": "2026-06-30",
      "date_launched": null,
      "date_result": null,
      "status": "draft",
      "dimensions": {
        "angle": "hormonio-desligado",
        "ad_type": "video_script",
        "hook_archetype": "injustica_comparativa",
        "emotion": "esperanca",
        "structure_or_style": "jornada_redencao",
        "platform": "reels"
      },
      "hypothesis": "Avatar mãe 35-45 no Reels responde à injustiça comparativa via jornada da redenção. Corpus 002_estruturas-invisiveis-criativos validou esta combinação para o mesmo perfil de avatar.",
      "hook_text": "Por que você come pouco e engorda, enquanto sua amiga come muito e emagrece?",
      "editor_format": "caixinha_perguntas",
      "files": {
        "estrategia": "projects/marca/estrategia-criativa.md",
        "roteiro_ou_briefing": "projects/marca/roteiros-video.md"
      },
      "result": {
        "metric_primary": null,
        "value": null,
        "roas": null,
        "budget": null,
        "duration_days": null,
        "notes": null,
        "verdict": null
      },
      "lessons": null
    }
  ],

  "backlog": [
    {
      "id": "hypo-001",
      "priority": "P1",
      "priority_reason": "isolation_test — mesmo ângulo, mudar só hook_archetype para isolar se a injustiça comparativa foi o fator",
      "dimensions": {
        "angle": "hormonio-desligado",
        "ad_type": "video_script",
        "hook_archetype": "ouch_factor",
        "emotion": "vergonha",
        "structure_or_style": "jornada_redencao",
        "platform": "reels"
      },
      "hypothesis": "Se test-001 ganhar, testar o mesmo ângulo com ouch_factor isola se o formato comparativo foi o fator ou se o ângulo em si é o forte.",
      "depends_on": "test-001",
      "created": "2026-06-30"
    }
  ],

  "coverage": {
    "angles_active": [],
    "ad_types_tested": [],
    "hook_archetypes_tested": [],
    "emotions_tested": [],
    "structures_or_styles_tested": [],
    "platforms_tested": []
  },

  "insights_summary": {
    "validated_hooks": [],
    "failed_combinations": [],
    "winning_combinations": [],
    "pattern_notes": ""
  }
}
```

**Status válidos:** `"draft"` | `"running"` | `"winner"` | `"loser"` | `"inconclusive"` | `"paused"`
**Veredicto válido:** `"winner"` | `"loser"` | `"inconclusive"`

---

## Protocolo de Inicialização (Fase 0)

Quando criar projeto novo ou quando `test-matrix.json` não existir:

1. Crie `projects/[marca]/tracking/test-matrix.json` com o schema acima
2. Preencha `brand`, `niche`, `last_updated`, `active_angle` (se ângulo já definido)
3. `tests`, `backlog` = arrays vazios
4. `coverage` com todos os arrays vazios

Informe ao usuário (em 1 linha): "Matriz de testes iniciada para [marca]. Primeiro registro será gerado ao final da Fase 3a/3b."

---

## Protocolo de Adição de Teste (Fase 3a / 3b)

Ao salvar um roteiro de vídeo ou um corpo de imagem **aprovado pelo usuário**:

1. Crie entrada em `tests[]` com `status: "draft"`
2. Preencha `dimensions` com os valores das Fases 1-2 (mais `ad_type`/`platform` da Fase 0)
3. Preencha `hypothesis` (da Fase 2), `hook_text` (texto exato do gancho aprovado), `editor_format` se vídeo
4. Preencha `files` com os caminhos gerados
5. Atualize `coverage` adicionando IDs novos em cada array
6. Atualize `last_updated`
7. Regenere `tracking/insights.md` (ver seção abaixo)

Cada hook gerado dentro do mesmo corpo que será testado separadamente (A/B) vira uma entrada de teste própria — não agrupe variações de hook como um único teste.

---

## Protocolo de Atualização de Resultado

Quando o usuário reportar que um teste rodou ou tem resultado, pergunte:

```
1. Status: lançou mas ainda sem resultado (→ "running") | tem resultado (→ continue)
2. Métrica principal: CTR / Hold Rate / ROAS / CVR / CPA
3. Resultado: [número]
4. Budget e duração: R$X por Y dias
5. Insights qualitativos: algo que notou? (plataforma, device, horário, comentários, etc.)
```

**Classificar o teste:**
- **`winner`**: performance acima do benchmark ou meta definida pelo usuário
- **`loser`**: claramente abaixo — não vale mais rodar esta combinação
- **`inconclusive`**: sinais mistos — precisa mais budget ou tempo
- **`paused`**: parou por motivo externo, não por performance

Preencha `result`, `lessons` (aprendizado em 1-2 frases), `date_result`. Atualize `insights_summary`. Atualize `coverage` se novos IDs foram usados. Regenere `insights.md`. Gere o backlog atualizado com próximas hipóteses (ver Algoritmo abaixo).

---

## Algoritmo de Priorização do Backlog

### P1 — Teste de Isolamento (após WINNER)
Mude apenas UMA variável por vez para identificar qual dimensão causou o sucesso:
1. Mesmas dimensões, mude só `hook_archetype` → valida se o gancho foi o fator
2. Mesmo ângulo + gancho, mude `structure_or_style` → valida se a estrutura/estilo foi o fator
3. Mesmo ângulo + gancho + estrutura, mude `platform` → expansão de plataforma

Regra: nunca mude ângulo durante P1.

### P2 — Teste de Cobertura (após LOSER ou INCONCLUSIVE)
Mude pelo menos 2 variáveis para testar hipótese diferente. Priorize:
- Estrutura/estilo nunca testado para este ângulo (do coverage)
- Hook archetype com maior taxa de sucesso no corpus para este nicho (consultar `corpus/index.json`)
- Emoção não testada ainda (do coverage)
- `editor_format` recomendado por `knowledge/editor-formats.md` mas não usado ainda (se vídeo)

### P3 — Novo Ângulo (após 3+ testes sem winner)
Condição: `tests[]` com este ângulo tem 3+ entradas, nenhum `"winner"`.
Ação: Volte à Fase 2 para gerar novos ângulos. Registre o ângulo anterior como `"angle_retired"` em `insights_summary`. Verifique `kill-list.md` antes de propor o novo ângulo.

### P4 — Expansão de Plataforma/Tipo (após winner consolidado)
Condição: 2+ isolation tests (P1) confirmaram o winner.
Ação: Mesmo criativo (ou adaptação mínima de formato) em plataforma diferente, ou no outro tipo de criativo (ex.: o ângulo venceu em vídeo → testar como imagem estática).

---

## Exibição Visual da Matriz

Quando o usuário pedir status da matriz ou ao iniciar sessão com projeto existente:

```
MATRIZ DE TESTES — [Marca] | Ângulo: "[angulo]" | Nicho: [nicho]
==================================================================

Estrutura/Estilo ↓ / Hook →  | aviso_rev | conspiracao | injustica | ouch_fac | ...
logica_dopamina              |  ✅ 4.2%  |     -       |     -     |    -     |
jornada_redencao              |     -    |     -       |   🔄      |    -     |
prova_visual                  |     -    |   ❌ 0.8%  |     -     |    -     |

Legenda: ✅ winner | ❌ loser | 🔄 running | 📋 no backlog | - não testado

Cobertura: [N]/2 tipos | [N]/10 hooks | [N]/10 emoções | [N]/8 estruturas-estilos | [N]/5 plataformas
Próximo recomendado: hypo-[N] (P[1/2]) — [resumo em 1 linha]
```

---

## Formato de Recomendação do Próximo Teste

Ao final de qualquer sessão onde um resultado foi registrado:

```
PRÓXIMO TESTE RECOMENDADO — hypo-[N]

Prioridade: P[1/2/3/4] — [razão: isolation_test / coverage / new_angle / platform_expansion]

Combinação proposta:
- Ângulo: [mesmo ou novo]
- Tipo de Criativo: [video_script | static_image]
- Hook Archetype: [nome]
- Emoção: [nome]
- Estrutura/Estilo: [nome]
- Plataforma: [plataforma]

Hipótese:
[Por que testar isso agora — baseado no resultado anterior + corpus]

Referência no corpus:
[arquivo(s) que validam esta combinação para este tipo de avatar]

Para começar: confirme "escrever" e vou para a Fase 3a/3b com esta combinação.
```

---

## Schema: tracking/insights.md (human-readable)

Regenere este arquivo a cada atualização do `test-matrix.json`. É a **biblioteca de aprendizados da marca**, feita para humanos lerem.

```markdown
# Insights Library — [Marca]
*Gerado automaticamente pelo Ads Builder | Atualizado: [data]*

---

## Visão Rápida

| Métrica | Valor |
|---|---|
| Criativos testados | N |
| Winners | N |
| Losers | N |
| Em andamento | N |
| Tipos cobertos | N/2 |
| Hook archetypes cobertos | N/10 |
| Estruturas/estilos usados | N/8 |
| Plataformas testadas | N/5 |

---

## Combinações Vencedoras ✅

### Ângulo: "[nome-do-angulo]"

**test-[N]** | [data_lançamento] | Plataforma: [plataforma]
- Tipo: [video_script/static_image] + Hook: [nome] + Estrutura/Estilo: [nome]
- Gancho: "[texto completo]"
- Resultado: CTR [X%] | ROAS [Xx] | Budget R$[X] por [N] dias
- Aprendizado: [lessons em 1-2 frases]

---

## Combinações Descartadas ❌

**test-[N]** | [data] | Plataforma: [plataforma]
- Tipo + Hook + Estrutura/Estilo: [...]
- Gancho: "[texto]"
- Resultado: [métricas]
- Hipótese de falha: [lessons]

---

## Hooks Validados Para Esta Marca ✅

- **[hook_archetype]** (`hook-taxonomy.md`) — [N] uso(s), [N] winner(s).
  *[Observação específica: "funciona melhor em vídeo que em imagem para esta marca"]*

---

## Próximos 3 Testes Recomendados

1. **hypo-[N]** (P[1/2]) — [ângulo × hook × estrutura/estilo] | [hipótese em 1 linha]
2. **hypo-[N+1]** (P[2]) — [resumo]
3. **hypo-[N+2]** (P[2/3]) — [resumo]

---

## Padrões Emergentes

*[Preenchido após 3+ testes. O agente detecta padrões e os descreve aqui.]*
```

Esta seção de Padrões Emergentes só é preenchida com 3+ testes — não antes.

---

## Regras de Integridade da Matriz

1. **Um teste = uma combinação específica lançada** — variações de gancho não testadas separadamente não entram como testes próprios; só o que foi efetivamente ao ar
2. **Resultado só entra quando real** — não projete resultados; só registre o que o usuário reportou
3. **Winner não é permanente** — se o contexto muda (saturação de audiência, sazonalidade), classifique como `"paused"` e teste novamente
4. **Ângulo é sagrado por enquanto** — muda só via P3 com justificativa documentada
5. **Corpus valida, não determina** — o corpus sugere; o teste decide
6. **Kill list é checada antes de qualquer novo ângulo** — nunca proponha algo já listado em `kill-list.md`
