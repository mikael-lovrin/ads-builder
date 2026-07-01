# COPY PROMPTS — Texto Extraído

> Fonte: `COPY PROMPTS.docx` (raiz do projeto). Este arquivo é a transcrição organizada do docx, mantida só para leitura humana / proveniência — não é lida pela skill em tempo de execução. O conteúdo reusável e niche-agnostic já foi destilado em `knowledge/` e `corpus/entries/`. Não editar como se fosse fonte de verdade operacional.

---

## 1. Extração de Dados do Produto

Prompt original (PT e EN no docx) para ler um VSL/briefing e extrair, em bullet points, sem interpretar:

- **Mecanismo Único**: explicação lógica/científica de por que o produto funciona
- **UMP (Mecanismo Único do Problema)**: causa real/escondida do problema que ninguém conta
- **UMS (Mecanismo Único da Solução)**: como o produto resolve o UMP de forma específica
- **Abordagens Tradicionais**: métodos comuns citados (dietas, exercícios etc.)
- **Falha das Abordagens**: por que essas abordagens falham segundo o texto
- **Autoridade**: nomes de médicos, estudos ou mídias citados
- **O Inimigo**: o que ou quem é o culpado pelo problema do cliente
- **Oferta**: preço final, desconto ou bônus mencionado
- **Garantia**: tempo de cobertura e condição principal

Regra: se a informação não está explícita no texto, responder "Não mencionado" — nunca inventar.

→ Destilado em `skills/ads-builder/prompts/fase1-extracao-produto.md`.

---

## 2. Estrutura Invisível (engenharia reversa de anúncio de referência)

Prompt para decompor um roteiro/transcrição de referência na sua "Estrutura Lógica Sequencial", sem resumir a história — descrevendo a função de cada bloco. Pontos analisados:

- **Ângulo de Venda**: Direto ao Ponto / Truque-Hack / Storytelling-Virada de Chave
- **Disfarce**: conteúdo nativo, notícia ou depoimento?
- **Identificação/Espelhamento**: como faz o espectador dizer "isso é para mim"
- **Transição para o Conteúdo**: como prende atenção sem parecer anúncio
- **A Virada de Chave ("Aha!")**: onde a lógica comum é quebrada
- **Apresentação do Mecanismo (UMP/UMS)**: como causa e solução entram na narrativa
- **Natureza da Oferta**: produto protagonista (Explícito) vs ferramenta do truque (Implícito)
- **Sequenciamento de Blocos**: ordem exata (ex.: Hook → Problema → Nova Solução → Prova Social → CTA)
- **O "Pulo do Gato"**: diferencial emocional/lógico
- **Nível de Exposição do Produto**: cura milagrosa vs facilitador de método
- **Lógica da Descoberta**: como o narrador justifica ter achado a solução (erro médico, segredo de família, vazamento de laboratório...)
- **CTA Disfarçado**: como manda a pessoa pro site ("Veja se ainda está no ar", "Clique para saber o ritual")

→ Destilado em `skills/creative-pattern-analysis/SKILL.md` e `corpus/entries/006_engenharia-reversa-estrutura-invisivel.json`.

---

## 3. Roteirizador de Elite — estrutura de 8 blocos

Estrutura obrigatória, bloco a bloco, para roteiro de vídeo (Reels/TikTok), tom "Tough Love" (agressivo, confiante, com empatia cirúrgica):

1. **Ganchos Multi-Angulares** (4-5 opções): Visual/Shock (contrarian), Ouch Factor (vergonha/intimidade), Contrarian (ataca método tradicional), Story Tease (in media res)
2. **Delimitação (O Filtro)**: chama o público específico (idade, dor, condição) imediatamente
3. **Sanduíche de Valor**: dica científica genérica → produto como "atalho" pra conseguir isso sem esforço
4. **PAS + Viés Financeiro**: Problema → Agitação (vergonha + dinheiro perdido em soluções caras/inúteis) → produto como alternativa barata e definitiva
5. **A Absolvição** ("não é culpa sua"): usa o UMP pra culpar biologia/indústria, tira o peso do cliente
6. **Storytelling Micro**: anedota de 2 frases sobre alguém notando a mudança (nunca o próprio sujeito descrevendo o que sentiu)
7. **Empilhamento de Benefícios**: 3-4 ganhos físicos e emocionais tangíveis, em paralelo
8. **CTA Triplo**: White (convite suave) → Gray (escassez/medo da perda) → Black (ultimato/desafio)

Regras de tom: nunca chamar de "produto" — sempre "truque/segredo/descoberta/método". Sem aspas, sem travessões, linguagem acessível a público geral, "como um influenciador do ramo fala".

→ Destilado em `knowledge/structure-library.md` e `skills/ads-builder/prompts/fase3a-roteiro-video.md`.

---

## 4. Formatos de Execução / Edição (testes de gancho)

- **Cinematográfico**: vídeo horizontal, tela preta, lettering bonito, legenda palavra por palavra (ex.: coach num cenário inspiracional)
- **Caixinha de Perguntas**: UGC respondendo a uma pergunta de caixinha do Instagram (precisa gerar as perguntas também)
- **Twitter/X Screenshot**: tela preta horizontal + print de tweet de uma autoridade (ex.: médico) acima do vídeo, como se fosse compartilhamento
- **Ranking**: números na tela, Top 3/Top 5 do que fazer ou evitar para atingir resultado X
- **UGC Stories Normal**: sem formato específico, default

Instrução original: dos 5 ganchos de um corpo, 2 usam um dos formatos de teste acima, os outros 3 ficam como UGC normal.

→ Destilado em `knowledge/editor-formats.md`.

---

## 5. Master Prompt — Image Ads Creative Brief Generator

### 5.1 Fundamentos de pesquisa (psicologia/conversão de imagem estática)

1. **The 3-Second Rule** (Nielsen/Meta) — 80% nunca lê além da headline se a imagem não para o scroll; olho vai pra rosto/olhos primeiro, depois alto contraste; foco único bate composição cheia em 38%
2. **Emotional Valence Before Logic** (Kahneman) — emoção antes de lógica converte 2x mais; emoções negativas param o scroll mas precisam pivotar pra esperança
3. **Tension Architecture** (Berger) — tensão visual não resolvida que só o body copy resolve
4. **Faces e Mirror Neurons** (Nielsen) — olhar direto = confronto/alto CTR; olhar pro lado = direciona atenção; emoção genuína ativa empatia
5. **Color Psychology** (Whitman) — tons frios/dessaturados = problema; tons quentes/dourados = solução; alto contraste sujeito/fundo aumenta recall em 47%
6. **Specificity = Credibility** (Whitman) — números específicos na imagem (53 lbs, 16 dias) batem claims vagos
7. **Pattern Interrupt** (Meta 2022-24) — documentário/cru bate polido em 41% CTR; justaposições inesperadas; anotações à mão = curiosidade
8. **Text on Image Rules** (Ogilvy/Meta) — 5 palavras ou menos = recall máximo; pergunta > afirmação (+23%); primeira pessoa cria identificação; CAPS só pra 1-3 palavras
9. **Image Style Performance**: fotografia realista = confiança máxima; ilustração = novidade/explicação de mecanismo; infográfico = dados/antes-depois; documentário cru = identificação/comentários; cartoon = humor/paradoxo
10. **Insight central**: a imagem não vende o produto — vende o clique. Job único: gerar algo não resolvido que o body copy precisa responder.

### 5.2 Os 5 Estilos Visuais Fixos (toda peça usa os 5, um por imagem)

1. **Realistic Photography** — âncora de confiança; rosto real com emoção genuína, luz natural, detalhe ambiental específico; olhar direto (confronto) ou desviado (direciona atenção)
2. **Documentary Raw** — formato de identificação máxima; estética de câmera de celular, leve superexposição, grão visível, momento "acidental"; sem filtros, sem pele perfeita
3. **Editorial Illustration** — mecanismo ou contraste visualizado; referência de publicação nomeada (New Yorker, Atlantic, Bloomberg); paleta limitada e nomeada
4. **Cartoon** — novidade e paradoxo; justaposição/absurdo; tom editorial (não fofo); máximo 5 cores
5. **Infographic** — cético analítico + camada de retargeting; história sequencial em 3-4 seções; 2+ números específicos; sem pessoas, sem produto

### 5.3 Estrutura de Copy Obrigatória (8 partes, em prosa natural, sem rotular)

1. Hook e Scroll Stop — tensão não resolvida, curiosidade proibida, desafio direto
2. Delimitação de Audiência — nas primeiras 3 frases, quem é (e quem não é) o público
3. Sanduíche de Valor (UMS como atalho) — mecanismo como revelação, não pitch
4. PAS + Dor Financeira — problema biológico exato → vergonha + dinheiro perdido → produto como alternativa lógica/barata/permanente
5. Absolvição — remove a culpa do cliente, nomeia o inimigo externo
6. Storytelling Micro — exatamente 2 frases, reação de terceiros (nunca o próprio sujeito narrando o que sentiu)
7. Empilhamento de Benefícios — 3-4 ganhos tangíveis, físicos + emocionais, estrutura paralela
8. CTA — urgência via escassez/supressão, nunca entusiasmo genérico

### 5.4 Regras obrigatórias de prompt de imagem

Toda imagem precisa especificar, nesta ordem: declaração de estilo, dimensões (1080x1080, 1:1), sujeito central e aparência específica, ação específica (não pose), detalhe ambiental, iluminação, paleta de cores (4-5 tons nomeados), o que NÃO está no frame (sem produto, sem logo, sem antes/depois), texto dentro da imagem se houver (palavras exatas), especificações de câmera/composição, tom emocional desejado.

### 5.5 Regras de copy

Sem aspas, sem travessões, sem jargão especialista, soar como especialista falando com amigo, micro-storytelling sempre 2 frases de reação de terceiro, nunca usar "journey", nunca "I never felt better"/"I feel amazing", nunca terminar com exclamação genérica, todo número/claim tem que vir do VSL/briefing — nunca inventar dado.

### 5.6 Production Notes (final de cada brief)

Sequência de teste recomendada (quais 2 imagens rodar primeiro, quais guardar pra retargeting), sugestão de teste A/B (uma variável específica), restrições da plataforma, flag honesta de claim que precisa de revisão legal, e uma observação criativa não usada no brief atual mas com potencial futuro.

→ Destilado em `knowledge/static-image-psychology.md` e `skills/ads-builder/prompts/fase3b-briefing-imagem.md`.

---

## 6. Avaliação e Tradução

- **Avaliação**: nota rigorosa para cada gancho, cada parte da estrutura, e uma nota final — apontando inconsistências sem suavizar.
- **Tradução**: ao localizar pra outro mercado/idioma, manter a estética de "criadora de conteúdo" nativa (ex.: americana, 50 anos, "relatable influencer"), formato de teleprompter (pausas naturais), sem negrito/itálico, termos comuns do nicho no mercado-alvo (ex.: "leaning out", "through the roof", "game changer").

→ Destilado em `skills/ads-builder/prompts/fase4-revisao-traducao.md`.

---

## 7. Kill List

Prompt de engenharia reversa de um roteiro já escrito, para extrair sua essência conceitual e bloquear repetição futura:

```
🚫 KILL LIST (NOVO ITEM)
Nome do Ângulo: [nome curto e memorável]
Narrativa: [história central em 1 frase]
Gancho Visual/Verbal: [cenas/frases de impacto do início]
Mecanismo: [como a solução foi apresentada]
Emoção Principal: [sentimento dominante]
```

→ Destilado em `skills/ads-builder/prompts/kill-list.md`.

---

## 8. Biblioteca de Ganchos (Choco Burn)

1. **Aviso Reverso** (campeão de retenção) — `[Comando Negativo] + [Ingrediente/Objeto Comum] + [Consequência irônica/exagerada]`. Por que funciona: o cérebro paralisa com "não faça" e fica confuso com a consequência positiva apresentada como negativa. Exemplo: "Não misture chocolate com esses 3 ingredientes se você não quiser ver suas calças caindo em 15 dias."
2. **Conspiração Revelada** (campeão de escala/ROAS) — `[Inimigo Poderoso] + [Descobriu/Escondeu Solução] + [Ancoragem de Preço Alta] + [Prova]`. Cria "nós contra eles" e valoriza a solução barata vs a cara. Exemplo: "Em 2015, a Big Pharma descobriu 3 ingredientes naturais... e escondeu de você para vender canetas de $2.000."
3. **Injustiça Metabólica** — `[Cenário Injusto (Você x Amiga)] + [Causa Raiz / Mecanismo Desligado]`. Valida a frustração e tira a culpa, coloca num "mecanismo desligado". Exemplo: "Por que você come pouco e engorda, enquanto sua amiga come muito e emagrece? O segredo está nos 3 hormônios que você tem DESLIGADOS..."
4. **Transformação Visual Específica** (campeão de ROAS) — `[Ponto A para Ponto B (métrica visual)] + [Ação Contra-Intuitiva] + [Autoridade Chocada]`. Tangível e visual. Exemplo: "De L para S em 60 dias comendo chocolate diariamente. Meu médico não acreditou nos exames."

Mais ganchos vistos nos roteiros-exemplo (não numerados na biblioteca original, mas usados consistentemente): **Ouch Factor** (toca direto na ferida física/de vergonha/intimidade), **Contrarian** (ataca um método tradicional como perda de tempo), **Story Tease** (começa in media res, no meio do caos/drama), **Visual Shock/ASMR** (prop incomum ou ASMR agressivo + declaração polêmica), **Revolta Financeira** (ação física de indignação — rasgar conta, jogar remédio no lixo), **Identidade/Vulnerabilidade** (confissão chocante e vulnerável).

→ Destilado em `knowledge/hook-taxonomy.md` e `corpus/entries/001_biblioteca-ganchos-choco-burn.json`.

---

## 9. Biblioteca de Estruturas Invisíveis de Criativos

**Estrutura A — "Lógica da Dopamina"** (foco em retenção alta): gancho negativo (proibir o uso se não quiser resultado exagerado) → validação imediata fast-paced ("eu testei e perdi X em Y") → desafio lógico (dissonância cognitiva) → autoridade externa introduzida rápido → CTA de curiosidade.

**Estrutura B — "Jornada da Redenção"** (foco em conversão/ROAS): valida o ceticismo do espectador → paradoxo geográfico/contextual (contraste realidade local vs realidade do "lugar especial") → mecanismo único como chave (explica o processo, não a comida/hábito em si) → solução acessível com ancoragem de preço → escassez por conspiração.

**Estrutura C — "Prova Visual"** (foco em resultado rápido): afirmação de resultado (A para B) → prova social/médica → facilidade de uso (eliminação de esforço) → passo a passo simplificado → garantia ousada (opcional).

→ Destilado em `knowledge/structure-library.md` e `corpus/entries/002_estruturas-invisiveis-criativos.json`.

---

## Nota sobre os exemplos de produto

O docx usa dois produtos fictícios/de teste para instanciar os prompts acima: **"Gelatin Burn"** (gelatina para emagrecimento) e **"PeriBalance"** (perimenopausa). Esses nomes e os detalhes de produto específicos **não entram** na skill nem no knowledge base — só os frameworks (estrutura, ganchos, regras) foram generalizados e destilados. Quem precisar do prompt original instanciado pode reabrir `COPY PROMPTS.docx`.
