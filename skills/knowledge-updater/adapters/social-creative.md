# Adapter: Social Creative (Ads)

> Nuances específicas para classificar criativos de anúncio (vídeo e imagem estática) dentro do protocolo geral em `../extraction-protocol.md`. Este é o adapter "nativo" do corpus do `ads-builder` — os campos abaixo já estão embutidos no schema principal (Passo A), este arquivo documenta como decidir entre eles na prática.

---

## Sub-schema: `video_script`

Campos do schema principal especialmente relevantes:
- `classification.structure_or_style.id` — uma das 3 estruturas de ritmo (`logica_dopamina`/`jornada_redencao`/`prova_visual`) ou `estrutura_8_blocos` se o material documenta o esqueleto completo
- `classification.editor_format` — preencher sempre que o material especificar uma forma de filmagem/edição (ver tabela B6); `ugc_normal` é o default explícito, não deixar `null` exceto quando o material é puramente sobre copy/estrutura
- `intelligence.most_teachable_moment` — para vídeo, priorize o momento de virada de chave ("Aha!") ou a frase do bloco de Absolvição, que costumam ser os blocos mais ensináveis

**Pergunta de triagem:** o material tem instruções de cena/câmera/edição explícitas? Se sim, é candidato a também alimentar `editor-formats.md` (não só `hook-taxonomy.md`/`structure-library.md`).

---

## Sub-schema: `static_image`

Campos do schema principal especialmente relevantes:
- `classification.structure_or_style.id` — um dos 5 estilos visuais fixos (`realistic_photography`/`documentary_raw`/`editorial_illustration`/`cartoon`/`infographic`)
- `classification.editor_format` — sempre `null` para imagem (campo é só de vídeo)
- `intelligence.unique_mechanism` — para imagem, descreva o que a IMAGEM faz (gera tensão, ancora confiança, mostra paradoxo) separado do que o BODY COPY faz (resolve a tensão) — os dois são funções diferentes, não misture na mesma frase

**Pergunta de triagem:** o material descreve um prompt de geração de imagem completo (estilo, sujeito, ambiente, paleta), ou só o conceito da imagem em texto? Se só conceito, marque `quality_flag: "medium"` — falta a camada de execução que `static-image-psychology.md` exige.

---

## Diferença entre `hook_pattern`, `structure_pattern` e `bestpractice`

Ao classificar `metadata.type`, use esta ordem de decisão:

1. O material é principalmente sobre a **abertura/gancho** (1-3 segundos ou primeira frase)? → `hook_pattern`
2. O material é principalmente sobre **ordem/ritmo dos blocos** depois do gancho? → `structure_pattern`
3. O material é um **framework completo** (combina pesquisa + múltiplas dimensões + regras de execução, ex.: o master prompt de imagem)? → `bestpractice`
4. O material é um **roteiro ou brief específico já escrito** para um produto real? → `video_script` ou `static_image`

---

## Quando propor novo arquétipo de gancho (B1) ou estilo (B5)

Antes de propor um ID novo (em vez de encaixar num existente), confirme:
- O padrão não é uma variante de um arquétipo/estilo já existente (anote como `archetype_variant` em vez de criar novo ID)
- Apareceu em pelo menos 2 materiais/criativos diferentes
- Passa o teste de niche-agnosticidade (`extraction-protocol.md`, C1)
- Tem pelo menos 1 contra-exemplo de quando NÃO se aplica

Se as 4 condições passarem, proponha ao usuário a adição à tabela B1/B5 correspondente — nunca adicione um ID novo a `knowledge/` sem essa aprovação explícita.
