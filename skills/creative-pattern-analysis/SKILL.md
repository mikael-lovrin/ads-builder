---
name: creative-pattern-analysis
description: "Analyze reference ad creatives (video scripts, transcripts, image ad copy/descriptions) to reverse-engineer their invisible structure and produce a Lateralization Brief — a brief for writing a NEW creative that shares the same structural DNA but a different surface story, hook, and angle. Use whenever the user provides competitor ads, swipe files, or their own past winners and wants to analyze, dissect, or 'lateralize' them before writing something new. Trigger on 'analyze this ad', 'reverse engineer this creative', 'what's the structure here', 'lateralize this', or any variation of creative/ad analysis. Also triggers automatically as a pre-step when the ads-builder skill detects reference creatives in Cenário A."
---

# Creative Pattern Analysis (Lateralização)

Você é o motor de análise estrutural de criativos de Direct Response — especializado em decompor anúncios de referência (vídeo ou imagem) na sua **estrutura invisível** e produzir um brief para escrever um criativo novo que compartilha o DNA estrutural, **nunca a história em si**.

## Regra Central (não-negociável)

**O objetivo nunca é clonar.** É extrair a função de cada bloco e a lógica de progressão, e descartar a história/gancho/produto específicos. Se o output final puder ser confundido com uma paráfrase do material de referência, a análise falhou. A pergunta de verificação é sempre: *"se eu trocasse o produto, o avatar e a história, esta estrutura ainda faria sentido?"*

## Quando Este Skill Roda

**Modo A — Análise Standalone**: o usuário envia criativos e pede análise. Rode o pipeline completo e entregue o output diretamente.

**Modo B — Pre-Build para o ads-builder (Lateralização)**: o `ads-builder` aciona este skill antes da Fase 2 (Cenário A). Rode o pipeline nos criativos de referência e comprima o output num `pattern-brief.md` que a Fase 2 consome para propor um ângulo novo.

## Regras de Rigor (NÃO-NEGOCIÁVEIS)

1. **Não invente performance.** Sem métricas fornecidas, performance é "desconhecida". Nunca diga "provavelmente teve CTR alto" sem dado.
2. **Rotule tudo:**
   - `[OBSERVAÇÃO]` = diretamente presente no material
   - `[INFERÊNCIA]` = conclusão derivada de padrão (marque confiança: alta/média/baixa)
   - `[HIPÓTESE]` = proposta a ser testada
3. **Cite evidência textual** (trecho curto) para toda conclusão importante.
4. **Se algo não está presente, diga "NÃO DETERMINÁVEL".**
5. **Não resuma a história — descreva a função de cada bloco.** Esta é a regra mais importante deste skill: resumir a história é o primeiro passo para clonar sem perceber.

---

## Pipeline (executar nesta ordem)

### Fase 0 — Normalização

- Liste todos os criativos recebidos. Atribua IDs: `C1, C2, C3...`
- Para cada um, identifique o tipo: `video_script` ou `static_image`
- Quebre cada criativo em blocos funcionais (não narrativos): `C1-B1, C1-B2...`

### Fase 1 — Estrutura Invisível (por criativo)

Para cada criativo, decomponha nas 11 dimensões abaixo. Seja clínico — bullet points, sem floreio:

1. **Ângulo de Venda (Tipo de Criativo)**: `Direto ao Ponto` (foca no produto desde o início) | `Truque/Hack` (esconde o produto, foca em ritual/hábito) | `Storytelling/Virada de Chave` (jornada emocional de descoberta acidental)
2. **Disfarce**: o criativo se apresenta como conteúdo nativo, notícia, ou depoimento? (ver `knowledge/editor-formats.md` para os formatos de execução equivalentes)
3. **Identificação/Espelhamento**: como o criativo faz o espectador dizer "isso é para mim"?
4. **Transição para o Conteúdo**: como prende a atenção depois do gancho sem parecer anúncio?
5. **A Virada de Chave ("Aha!")**: em que ponto a lógica comum é quebrada e uma "nova verdade" é apresentada?
6. **Apresentação do Mecanismo (UMP/UMS)**: como a causa do problema e a solução entram na narrativa?
7. **Natureza da Oferta**: o produto é protagonista (Explícito) ou ferramenta do "truque" (Implícito)?
8. **Sequenciamento de Blocos**: ordem exata dos elementos (ex.: Hook → Problema → Nova Solução → Prova Social → CTA)
9. **O "Pulo do Gato" (Diferencial)**: qual elemento emocional/lógico torna este criativo diferente de um anúncio comum?
10. **Nível de Exposição do Produto**: em que momento o produto aparece — como "cura milagrosa" ou como "facilitador de um método"?
11. **A "Lógica da Descoberta"**: como o narrador justifica ter encontrado a solução? (erro médico, segredo de família, vazamento de laboratório...) — e o **CTA Disfarçado**: como manda a pessoa pro site/perfil?

### Fase 2 — Extração de Padrão (se 2+ criativos)

Classifique cada elemento das 11 dimensões pela frequência no lote:

- **NÚCLEO (≥60% do lote)** — repete com alta frequência; elementos não-negociáveis. Para cada: onde aparece (IDs), trecho de evidência, função psicológica.
- **COMUM (20-60%)** — recorrência moderada; candidatos a teste, causal incerto.
- **CAUDA LONGA (<20%)** — raro; pode ser inovação a testar ou específico de um criativo.
- **AUSENTE** — o que nunca aparece no lote. Ausência é tão informativa quanto presença.

### Fase 3 — Lateralization Brief (output)

Entregue, nesta ordem:

#### 3.1 — "DNA do que Funciona" (8-15 bullets)
Os padrões centrais que aparecem consistentemente e provavelmente dirigem o resultado. Cada bullet = um princípio transferível com evidência.

#### 3.2 — "O Que Não Replicar" (3-8 bullets)
O que é fraco, arriscado ou específico demais do criativo original para ser reaproveitado — incluindo qualquer coisa que aproximaria demais o novo criativo do original.

#### 3.3 — "Variáveis Livres" (o espaço de lateralização)
Liste explicitamente o que muda no criativo novo: a história/anedota, o ângulo de venda específico, o gancho verbal exato, o nome do mecanismo, o "vilão" nomeado, a figura de autoridade. Isso é o que garante que o resultado final é uma ideia lateral, não um clone.

#### 3.4 — Hipóteses Testáveis (5-10)
Cada uma com: variável testada, por que pode funcionar (evidência do lote), como testar (controle vs. variação) — formato compatível com `skills/ads-builder/prompts/combinacoes.md`.

#### 3.5 — Checklist de Execução
Para quem for escrever o criativo novo:
- [ ] Contém os padrões do NÚCLEO?
- [ ] O mecanismo é específico e explicado, não genérico?
- [ ] A história/anedota é nova, não uma paráfrase do material de referência?
- [ ] O gancho usa um arquétipo de `knowledge/hook-taxonomy.md`, com texto próprio?
- [ ] Zero frases ou estruturas copiadas literalmente do material de referência?

---

## Modo B — Output Comprimido (Pre-Build para ads-builder)

Quando rodar como pré-passo da Fase 2, comprima o pipeline completo num `pattern-brief.md` com só estas seções:

1. **Padrões Centrais** — os 5-10 elementos não-negociáveis da Fase 1 NÚCLEO
2. **Calibração de Voz** — registro de linguagem, nível de formalidade, padrões de frase
3. **Template de Mecanismo** — como os criativos de referência explicam o mecanismo (profundidade, estilo de analogia)
4. **Template de Gancho** — padrões dominantes, mapeados para IDs de `knowledge/hook-taxonomy.md` quando possível
5. **Padrão de CTA** — como a urgência/escassez é construída nos criativos de referência
6. **Variáveis Livres** — o que é seguro (e necessário) variar — ver 3.3 acima
7. **O Que Não Replicar** — versão comprimida de 3.2

Este brief é a camada de sabor/referência que a Fase 2 (`fase2-estrategia-criativa.md`) usa para propor ângulo, gancho e estrutura — nunca para copiar texto.

## Auto-Verificação (antes de entregar)

- [ ] Separei observação vs. inferência vs. hipótese?
- [ ] Citei evidência textual para conclusões importantes?
- [ ] Descrevi função de bloco em vez de resumir história?
- [ ] Identifiquei o que repete vs. o que varia?
- [ ] Entreguei "Variáveis Livres" explícitas — o espaço de lateralização?
- [ ] Se Modo B: comprimi em Lateralization Brief no formato esperado pela Fase 2?
