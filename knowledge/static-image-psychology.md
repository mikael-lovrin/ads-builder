# Static Image Psychology — Fundamentos e Estilos Visuais

> Base de conhecimento para a Fase 3b (Briefing de Imagem Estática). Destilada de `referencias/copy-prompts-extraido.md` (seção 5) — o "Master Prompt — Image Ads Creative Brief Generator". Usada em `skills/ads-builder/prompts/fase3b-briefing-imagem.md`. IDs de estilo visual usados em `corpus/entries/*.json` e na matriz de testes (dimensão D5 para imagem).

---

## Os 10 Princípios de Conversão (a fundação estratégica)

Antes de escrever um hook ou um prompt de imagem, toda decisão criativa deve conseguir se justificar por pelo menos um destes princípios. Não é decoração — é o argumento por trás de cada escolha do brief.

1. **The 3-Second Rule** (Nielsen / Meta) — 80% dos espectadores nunca lê além da headline se a imagem não para o scroll. O olho vai pro rosto/olhos primeiro, depois para elementos de alto contraste. Um único ponto focal dominante bate composições cheias em 38%.
2. **Emotional Valence Before Logic** (Kahneman, *Thinking Fast and Slow*) — anúncios que disparam emoção antes de pensamento consciente convertem 2x mais. Emoções negativas (vergonha, constrangimento, medo de ser invisível) param o scroll mais rápido — mas precisam pivotar imediatamente para esperança/possibilidade. O estado emocional "antes" deve ser SENTIDO na imagem, não descrito em texto.
3. **Tension Architecture** (Berger, *Contagious*) — o cérebro não resiste a uma tensão visual não resolvida. A melhor imagem estática cria uma pergunta que só o body copy responde. A resolução deve ser implícita, nunca mostrada — o espectador precisa clicar para completar a história.
4. **Faces and Mirror Neurons** (Nielsen eye-tracking) — rosto olhando direto pra câmera = desafio direto = para o scroll, é confrontacional, CTR alto. Rosto olhando pra longe = o espectador segue o olhar = direciona atenção pro texto/elemento de apoio. Emoção genuína (não sorriso de banco de imagens) ativa neurônios-espelho = resposta de empatia = identificação.
5. **Color Psychology** (Whitman, *Ca$hvertising*) — tons dessaturados/cinza/frios = estado do problema (isolamento, estagnação, vergonha). Tons quentes, luz dourada, verdes = estado da solução (vitalidade, liberdade, natureza). Alto contraste entre sujeito e fundo aumenta recall em 47%.
6. **Specificity = Credibility** (Whitman) — números específicos na imagem (53 lbs, 16 dias, 343%) batem claims vagos disparado. Rosto + número específico = a combinação de maior conversão em DR de saúde.
7. **Pattern Interrupt** (Meta Creative Research 2022-2024) — estética documental/crua bate estética polida/banco de imagens em 41% de CTR. Justaposições inesperadas param o scroll. Anotações ou setas à mão na imagem = gatilho de curiosidade (parece que alguém está te mostrando um segredo). Imperfeição autêntica bate fotografia polida em 31% no público feminino de 35-55 anos em saúde.
8. **Text on Image Rules** (Ogilvy / Meta) — 5 palavras ou menos na imagem = recall máximo. Formato de pergunta aumenta engajamento 23% sobre afirmação. Primeira pessoa ("Eu") cria identificação imediata. CAPS só para 1-3 palavras — urgência sem cansar.
9. **Image Style Performance** (Meta / WordStream):
   - Fotografia realista: confiança máxima, CTR mais alto para emagrecimento no público 40-55F
   - Ilustração/desenho: para o scroll por novidade, boa para explicar mecanismo, confiança mais baixa
   - Infográfico: forte para dados e antes/depois, alta taxa de compartilhamento
   - Documentário/estética crua de celular: identificação emocional máxima, maior taxa de comentários
   - Cartoon: novidade e humor máximos, funciona para ângulos de paradoxo, confiança mais baixa em claims de saúde
10. **O insight central** — a imagem não vende o produto. A imagem vende o CLIQUE. O único trabalho dela é fazer o espectador sentir algo não resolvido que o body copy precisa responder.

---

## Os 5 Estilos Visuais Fixos

Todo brief de imagem usa os 5 estilos, um por imagem, sempre nesta ordem. IDs: `realistic_photography` | `documentary_raw` | `editorial_illustration` | `cartoon` | `infographic`.

### `realistic_photography` — Fotografia Realista
**Função:** âncora de confiança.
Rosto real com emoção genuína (não sorriso de banco de imagens), luz natural, detalhe ambiental específico que ancora a cena num momento de vida real. Rosto olhando direto pra câmera (confrontacional, para o scroll) OU olhando pra um elemento específico (direciona o olhar do espectador). Precisa parecer que foi tirada por um fotógrafo habilidoso que estava na sala — não por uma agência de publicidade. O formato de maior confiança para o público feminino 35-55 em saúde.

### `documentary_raw` — Documentário Cru
**Função:** identificação máxima.
Estética simulada de câmera de celular — leve superexposição, luz natural indoor/outdoor, leve distorção de lente, grão visível, composição levemente imperfeita. Precisa parecer uma captura acidental de um momento privado que o espectador não deveria estar vendo. Sem cara de estúdio. Sem pele perfeita. Sem filtro. O sujeito num momento de honestidade emocional quieta — não dramático, não encenado. Gera a maior taxa de comentários e a resposta mais forte de "essa sou eu" no público-alvo.

### `editorial_illustration` — Ilustração Editorial
**Função:** visualização de mecanismo ou contraste.
Precisa nomear uma publicação de referência de estilo (New Yorker, The Atlantic, capa da Time, infográfico de dados da Bloomberg). Visualiza o mecanismo biológico do UMP/UMS, o contraste entre o mundo-problema e o mundo-solução, ou o "vilão" do briefing. Paleta de cores limitada — declarar o número exato de cores e nomeá-las. Sem decoração — todo elemento precisa justificar a presença. Para o scroll por novidade e constrói credibilidade intelectual.

### `cartoon` — Cartoon
**Função:** novidade e paradoxo.
Precisa usar uma justaposição, absurdo ou contraste inesperado como conceito central. Tom editorial, não fofo — pensar em charge política, não ilustração infantil. Máximo 5 cores, declaradas explicitamente. Precisa fazer o espectador sentir uma mistura de reconhecimento e leve raiva ou humor. Maior taxa de scroll-stop por novidade; funciona muito bem para o ângulo "eles sabiam e não te contaram" (gancho `conspiracao_revelada`).

### `infographic` — Infográfico
**Função:** cético analítico + camada de retargeting mais forte.
Precisa contar uma história sequencial em 3-4 seções claramente separadas. Precisa incluir pelo menos 2 números específicos dos dados do produto. Precisa parecer uma página de uma fonte editorial confiável (seção de saúde do Guardian, matéria de dados da Bloomberg) — não um anúncio. Sem pessoas, sem rostos, sem produto. Arquitetura de informação pura que faz o espectador sentir que finalmente entendeu algo que ninguém tinha explicado antes.

---

## Estrutura de Copy Obrigatória (8 partes — todo body copy de imagem)

Mesma lógica do roteiro de vídeo (ver `structure-library.md`), adaptada para prosa corrida sem rótulos visíveis — fluem como texto natural, na ordem abaixo:

1. **Hook e Scroll Stop** — primeira linha cria tensão não resolvida, curiosidade proibida, desafio direto ou fato inesperado. A próxima frase precisa parecer inevitável.
2. **Delimitação de Audiência** — nas primeiras 3 frases, deixa claro exatamente quem é (e quem não é) o leitor. Idade, fase de vida, experiência específica.
3. **Sanduíche de Valor (UMS como atalho)** — entrega o mecanismo central como um atalho científico nunca ouvido antes. Não é pitch de produto — é revelação.
4. **PAS + Dor Financeira** — Problema: nomeia a quebra biológica exata. Agitação: conecta à vergonha emocional específica e ao dinheiro já gasto em coisas que não funcionaram. Apresenta: posiciona o produto como alternativa lógica, acessível e permanente.
5. **Absolvição** — remove a culpa do leitor completamente. O UMP é a prova de que nunca foi culpa dele. Nomeia o inimigo externo especificamente.
6. **Storytelling Micro** — exatamente 2 frases. Um momento específico de reação social — alguém mais notando a mudança. Nunca o próprio sujeito descrevendo o que sentiu. Cinematicamente específico (marido, colega, filha, médico, ex).
7. **Empilhamento de Benefícios** — 3-4 ganhos tangíveis, mistura física e emocional. Como coisas que voltam a ser possíveis, não como features. Estrutura paralela, linhas curtas.
8. **CTA** — urgência via escassez ou supressão, nunca entusiasmo genérico. Pressão da indústria farmacêutica. Conteúdo sendo removido. Acesso limitado. Nunca termina com exclamação genérica.

---

## Regras Obrigatórias de Prompt de Imagem

Todo prompt de geração de imagem precisa especificar, **nesta ordem**:

1. Declaração de estilo (ex.: "fotografia editorial hiper-realista" ou "ilustração de cartoon editorial plano")
2. Dimensões e formato (1080x1080, quadrado)
3. Sujeito central e aparência específica — idade, etnia se relevante, roupa, expressão, linguagem corporal
4. O que o sujeito está fazendo — ação específica, não pose
5. Detalhe ambiental — onde está, o que tem ao redor, o que tem nas superfícies próximas
6. Iluminação — direção, qualidade, temperatura de cor
7. Paleta de cores — nomear 4-5 cores/tons específicos
8. O que NÃO está no frame — sem produto, sem logo, sem split antes/depois
9. Texto dentro da imagem — se houver (bilhete escrito à mão, post-it, placa), declarar as palavras exatas
10. Especificações de câmera/composição — lente, ângulo, profundidade de campo, grão, regra de composição
11. O tom emocional que a imagem precisa produzir no espectador — uma frase
12. Aspect ratio 1:1

---

## Regras de Copy (toda peça de imagem)

- Sem aspas em nenhum lugar
- Sem travessões em nenhum lugar
- Sem expressões que exigem conhecimento especialista — escrever para público geral
- Soar como especialista falando com um amigo, não apresentando numa conferência
- A anedota de storytelling micro precisa ter exatamente 2 frases e mostrar transformação através da reação de outra pessoa, nunca do próprio sujeito descrevendo seus sentimentos
- Nunca usar a palavra "jornada"
- Nunca usar "nunca me senti melhor" ou "eu me sinto incrível"
- Nunca terminar com exclamação genérica
- Todo número, estatística ou claim precisa vir do briefing/produto real — nenhum dado inventado

---

## Production Notes (seção final obrigatória de todo brief)

Todo brief de imagem termina com:
- **Sequência de teste recomendada** — quais 2 imagens rodar primeiro e por quê, quais estilos guardar para retargeting e por quê
- **Sugestão de teste A/B** — uma variável específica para testar na primeira semana
- **Restrições específicas da plataforma** declarada no briefing
- **Uma flag honesta** — se algum claim do copy precisa de revisão legal antes de rodar, nomear especificamente e explicar por quê
- **Uma observação criativa** — algo notado no briefing/produto que não foi usado neste brief mas pode virar um ângulo forte numa iteração futura
