# Protocolo de Extração de Inteligência — Knowledge Updater

> Este documento define o protocolo PADRONIZADO de extração para o corpus de criativos do `ads-builder`. Toda sessão Claude que roda o Knowledge Updater usa EXATAMENTE este protocolo — garantindo que o output seja consistente, independente de quando ou por quem é executado. Adaptado do protocolo equivalente do projeto irmão `adv-agent` (`skills/knowledge-updater/extraction-protocol.md`) para o domínio de criativos de anúncio (vídeo + imagem estática).

---

## Princípio de Design

O protocolo usa DEFINIÇÕES PRECISAS com EXEMPLOS e CONTRA-EXEMPLOS para cada categoria. Quando as definições são suficientemente específicas, a classificação se torna determinística — não varia entre sessões Claude.

---

## PASSO A: Schema de Saída (Obrigatório)

Todo material processado DEVE gerar uma entrada `corpus/entries/[slug].json` com EXATAMENTE este schema:

```json
{
  "schema_version": "1.0",
  "file": "nome do arquivo/fonte original, ou null se colado diretamente na conversa",
  "slug": "NNN_slug-descritivo",
  "processed_at": "YYYY-MM-DD",

  "metadata": {
    "type": "video_script | static_image | hook_pattern | structure_pattern | bestpractice",
    "author": "nome ou null",
    "year": 2026,
    "source": "user-created | swiper | external | competitor",
    "title": "headline/hook principal ou título descritivo",
    "post_url": "https://... ou null",
    "word_count": 1500
  },

  "classification": {
    "hook": {
      "archetype": "ID da tabela B1, ou null se o material não é sobre gancho",
      "archetype_variant": "nome da variante se não é o arquétipo base, ou null",
      "psychological_trigger": "ID da tabela B2",
      "template_extracted": "template niche-agnostic extraído deste gancho específico"
    },
    "ad_type": {
      "primary": "ID da tabela B3",
      "secondary": "ID secundário se híbrido, ou null"
    },
    "emotion": {
      "dominant": "ID da tabela B4",
      "secondary": "ID secundário ou null"
    },
    "structure_or_style": {
      "id": "ID da tabela B5 (depende de ad_type.primary), ou null",
      "context": "video | image | analysis"
    },
    "platform": ["IDs da tabela B7"],
    "niches": ["saude_emagrecimento", "saude_feminina", "..."],
    "editor_format": "ID da tabela B6, ou null (só aplicável a video_script)"
  },

  "intelligence": {
    "unique_mechanism": "O mecanismo/padrão central deste criativo em 1-2 frases. O QUE faz funcionar, não QUAL o produto",
    "villain": "O 'vilão' nomeado, ou null se não há",
    "hero_character": "Quem é o narrador/protagonista",
    "most_teachable_moment": {
      "quote": "frase exata mais ensinável do material",
      "principle": "o princípio de copywriting que ela exemplifica"
    },
    "niche_agnostic_insight": "O que este material ensina que funciona em QUALQUER nicho",
    "extrapolations": [
      {"niche": "outro_nicho_1", "application": "como a lógica se aplicaria"},
      {"niche": "outro_nicho_2", "application": "como a lógica se aplicaria"}
    ]
  },

  "kb_contribution": {
    "new_archetype_proposed": null,
    "new_technique_proposed": null,
    "existing_archetype_expanded": "nome do arquivo/seção do knowledge base + o que adicionaria",
    "quality_flag": "high | medium | low",
    "quality_reason": "por que este nível de qualidade"
  }
}
```

---

## PASSO B: Tabelas de IDs Padronizados

### B1 — Arquétipos de Gancho (10 IDs fixos)

Ref. completa com fórmulas e exemplos: `knowledge/hook-taxonomy.md`.

| ID | Nome | Gatilho Central |
|----|------|----------------|
| `aviso_reverso` | Aviso Reverso | Curiosidade + Aversão à perda |
| `conspiracao_revelada` | Conspiração Revelada | Raiva externa + FOMO |
| `injustica_comparativa` | Injustiça Comparativa | Identificação + Inveja construtiva |
| `transformacao_visual_especifica` | Transformação Visual Específica | Praticidade + Autoridade confiada |
| `ouch_factor` | Ouch Factor | Vergonha social + Identificação |
| `contrarian` | Contrarian | Curiosidade + Raiva externa |
| `story_tease` | Story Tease | Curiosidade |
| `visual_shock_asmr` | Choque Visual / ASMR | Curiosidade pré-cognitiva |
| `revolta_financeira` | Revolta Financeira | Raiva externa + Aversão à perda |
| `identidade_vulnerabilidade` | Identidade / Vulnerabilidade | Identificação + Pertencimento |

**REGRA DE CLASSIFICAÇÃO:** use só o arquétipo MAIS DOMINANTE. Se o gancho combina dois, escolha o mais saliente e anote o outro em `archetype_variant`.

**TESTE:** se você pode substituir o nicho/produto no gancho mantendo a mesma lógica → o arquétipo está certo.

---

### B2 — Gatilhos Psicológicos (12 IDs)

> Vocabulário **idêntico** ao do `adv-agent` (`knowledge-updater/extraction-protocol.md`, tabela B2) — mantido de propósito para que os dois grafos de referência sejam compatíveis.

| ID | Definição |
|----|-----------|
| `curiosidade` | O espectador quer saber mais — lacuna de informação |
| `aversao_a_perda` | Teme perder algo que tem ou poderia ter |
| `identificacao` | Se reconhece na situação descrita |
| `pertencimento` | Quer fazer parte do grupo descrito |
| `fomo` | Teme ficar de fora de algo que outros já têm |
| `inveja_construtiva` | Quer o que outras pessoas similares já conseguiram |
| `vergonha_social` | Teme ser julgado ou visto negativamente |
| `esperanca` | Vê possibilidade real de mudança |
| `raiva_externa` | Se sente traído por sistema, indústria, ou informação |
| `orgulho_aspiracional` | Quer ser a pessoa que conseguiu o resultado |
| `praticidade` | Quer o caminho mais simples e direto |
| `autoridade_confiada` | Confia na fonte que está falando |

---

### B3 — Tipo de Criativo (2 IDs)

| ID | Nome |
|----|------|
| `video_script` | Roteiro de Vídeo (Reels/TikTok/UGC) |
| `static_image` | Imagem Estática (Meta) |

---

### B4 — Emoções Dominantes (10 IDs)

> Vocabulário idêntico ao do `adv-agent`.

| ID | Quando usar |
|----|------------|
| `medo` | Ação motivada por evitar perda/dano |
| `vergonha` | Preocupação com julgamento social |
| `raiva` | Há "vilão" externo nomeado |
| `desejo` | Visão do futuro ideal é o motor principal |
| `inveja` | Comparação com quem já tem o resultado é central |
| `esperanca` | Possibilidade de mudança após fracassos é central |
| `curiosidade` | Mistério ou lacuna de informação é o motor |
| `orgulho` | Identidade aspiracional/pertencimento são centrais |
| `inspiracao` | Exemplo de quem conseguiu motiva ação |
| `culpa_absolvida` | O material remove culpa do avatar e transfere ao vilão |

---

### B5 — Estrutura / Estilo (depende de B3)

**Se `ad_type.primary = video_script`** — ref. `knowledge/structure-library.md`:

| ID | Foco |
|----|------|
| `logica_dopamina` | Retenção alta (hold rate) |
| `jornada_redencao` | Conversão / ROAS |
| `prova_visual` | Resultado rápido, baixa fricção |
| `estrutura_8_blocos` | A estrutura base (use quando o material documenta o esqueleto inteiro, não uma das 3 variações de ritmo) |

**Se `ad_type.primary = static_image`** — ref. `knowledge/static-image-psychology.md`:

| ID | Foco |
|----|------|
| `realistic_photography` | Âncora de confiança |
| `documentary_raw` | Identificação máxima |
| `editorial_illustration` | Mecanismo/contraste visualizado |
| `cartoon` | Novidade e paradoxo |
| `infographic` | Cético analítico + retargeting |

---

### B6 — Formato de Execução / Edição (3 IDs, só vídeo)

Ref. completa: `knowledge/editor-formats.md`.

| ID | Nome |
|----|------|
| `cinematografico` | Tela preta, lettering, legenda palavra-por-palavra |
| `caixinha_perguntas` | UGC respondendo pergunta de caixinha do Instagram |
| `ugc_normal` | Default, sem formato específico |

---

### B7 — Plataforma (5 IDs)

`meta_feed` | `reels` | `tiktok` | `pinterest` | `stories`

---

## PASSO C: Protocolo de Classificação (Como Decidir)

### C1 — Classificar o Arquétipo de Gancho

1. Leia só o gancho (primeiras 1-3 frases ou primeiros 3 segundos de vídeo)
2. Pergunte: "Qual é o ÚNICO gatilho principal aqui?"
3. Mapeie para o ID da tabela B1
4. Teste de niche-agnosticidade: substitua o nicho/produto — a lógica ainda funciona? Se não, revise
5. Anote se é variante de um arquétipo base

### C2 — Classificar Tipo + Estrutura/Estilo

1. O material é roteiro falado/filmado (`video_script`) ou copy+descrição de imagem estática (`static_image`)?
2. Se vídeo: a estrutura documenta o esqueleto de 8 blocos inteiro, ou só uma das 3 variações de ritmo (dopamina/redenção/prova)? Classifique conforme B5.
3. Se imagem: qual dos 5 estilos visuais fixos o material descreve? Se descreve o framework completo (todos os 5), classifique como `bestpractice` em vez de um estilo único.

### C3 — Identificar o Formato de Execução (só vídeo)

Pergunta de validação: o material especifica uma forma de filmagem/edição específica (tela preta+lettering, caixinha de pergunta)? Se não, classifique como `ugc_normal` ou deixe `null` se o material é puramente sobre estrutura/copy, não sobre execução visual.

### C4 — Determinar Emoção Dominante

Use o que o próprio material aponta como sentimento central do avatar/leitor. Se não estiver explícito, infira da combinação Problema+Agitação+Vilão — e marque a classificação como `[INFERÊNCIA]` no relatório da sessão.

---

## PASSO D: Protocolo de Atualização do Knowledge Base

### D1 — Quando atualizar um arquivo KB existente

Só atualize se:
- O novo material adiciona algo genuinamente não presente (não só confirma o que já existe)
- Ou corrige algo impreciso

**Tipos de adição aceitáveis:** novo exemplo do corpus para arquétipo/estrutura já documentada; nova variante de um arquétipo já documentado; novo formato de execução; extrapolação para nicho não documentado.

**NÃO atualize se:** o material só repete o que já está lá com outras palavras; a adição seria mais específica que o nível de abstração do arquivo KB.

### D2 — Quando criar novo conteúdo no KB

Só crie nova entrada se:
- O padrão apareceu em pelo menos 2 materiais diferentes
- Não é sub-variante de algo já existente
- Tem aplicação em pelo menos 2 nichos diferentes

### D3 — Formato de adição ao KB (obrigatório)

```markdown
### [Nome do item]
**Fonte no corpus:** `corpus/entries/arquivo1.json`, `corpus/entries/arquivo2.json`
**Validado em produção:** Não (ainda sem dados) / Sim — [marca + referência de teste trazida pelo usuário, ver knowledge-updater/SKILL.md#retroalimentação]

[Definição]

**Por que funciona:** [mecanismo psicológico]

**Template:**
- `"[template niche-agnostic]"`

**Exemplos do corpus:**
- *"[frase exata]"* — `corpus/entries/arquivo.json`
```

---

## PASSO E: Controle de Qualidade

Antes de finalizar qualquer sessão, verifique:

**Checklist por material:**
- [ ] `title`/`hook` contém o texto exato, não uma paráfrase
- [ ] `hook.archetype` é um dos 10 IDs fixos (B1) ou `null` (não foi inventado)
- [ ] `ad_type.primary` é um dos 2 IDs fixos (B3)
- [ ] `emotion.dominant` é um dos 10 IDs fixos (B4)
- [ ] `structure_or_style.id`, se preenchido, é coerente com `ad_type.primary` (B5)
- [ ] `unique_mechanism` descreve o MECANISMO/PADRÃO, não o produto
- [ ] `niche_agnostic_insight` é genuinamente transferível para outro nicho

**Checklist por sessão:**
- [ ] Todas as entradas usam IDs das tabelas B (sem IDs inventados)
- [ ] Nenhuma entrada duplica o que já estava no `corpus/index.json`
- [ ] Todas as propostas de atualização do KB foram apresentadas ao usuário antes de aplicadas
- [ ] `corpus/index.json` foi atualizado com as novas entradas ao final

---

## PASSO F: Arquivo de Log da Sessão

Após cada sessão, salve em `corpus/updater-log.json`:

```json
{
  "sessions": [
    {
      "date": "2026-06-30",
      "session_number": 2,
      "files_processed": ["material1", "material2"],
      "entries_added": 3,
      "kb_updates": [
        {"file": "knowledge/hook-taxonomy.md", "type": "new_archetype | new_example", "name": "...", "source_files": ["..."]}
      ],
      "new_archetypes_proposed": [],
      "pending_review": [],
      "notes": "observações do operador"
    }
  ]
}
```

---

## Adaptadores por Tipo de Material

O domínio nativo deste protocolo já é "criativo de anúncio" (vídeo + imagem). Ver `adapters/social-creative.md` para as nuances específicas de cada subtipo (vídeo vs. imagem). Para tipos de conteúdo fora do escopo atual (ex.: email marketing, carrossel multi-slide, UGC longo de testemunho), criar um novo arquivo em `adapters/` seguindo o mesmo formato antes de processar esse material — não improvise classificação fora das tabelas B sem um adapter documentado.
