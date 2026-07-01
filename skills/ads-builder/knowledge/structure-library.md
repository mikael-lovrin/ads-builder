# Structure Library — Estruturas de Roteiro de Vídeo

> Estruturas narrativas para roteiros de vídeo (Reels/TikTok/UGC), destiladas de `referencias/copy-prompts-extraido.md` (seções 3 e 9). Usadas em `skills/ads-builder/prompts/fase3a-roteiro-video.md`. IDs usados em `corpus/entries/*.json` e na matriz de testes (`skills/ads-builder/prompts/combinacoes.md`, dimensão D5 para vídeo).
>
> Para a engenharia reversa de criativos de referência (decompor um anúncio existente em sua estrutura), ver `skills/creative-pattern-analysis/SKILL.md` — esse é o processo inverso (análise), este arquivo é o processo direto (construção).

---

## A Estrutura Obrigatória de 8 Blocos ("Roteiro de Elite")

Estrutura padrão para qualquer roteiro de vídeo gerado por este agente, independente do ângulo/gancho escolhido. Tom de voz: "Tough Love" — agressivo e confiante, com empatia cirúrgica nas dores; linguagem coloquial, nunca chamar o produto de "produto" (sempre truque/segredo/descoberta/método); sem aspas, sem travessões.

### 1. Bloco de Ganchos Multi-Angulares
Gere 4-5 opções de abertura para o mesmo roteiro, cobrindo arquétipos diferentes de `hook-taxonomy.md`:
- **Opção A (Visual/Shock):** declaração polêmica/contrarian, ou `visual_shock_asmr`
- **Opção B (Ouch Factor):** toque direto na ferida de vergonha corporal/intimidade
- **Opção C (Contrarian):** ataque a um método tradicional como perda de tempo
- **Opção D (Story Tease):** início in media res, no meio de uma história/drama

2 das 4-5 opções devem usar um dos formatos de execução fixos de `editor-formats.md` (cinematográfico, caixinha de perguntas); as demais ficam como UGC normal, sem formato específico.

### 2. Delimitação (O Filtro)
Chama o público específico (idade, condição, dor) de forma imediata e explícita — ex.: "Se você é mãe e tem pochete...", "Se você já tentou academia e salada e nada funcionou...".

### 3. Sanduíche de Valor
Entrega uma dica científica/genérica primeiro (ex.: "baixar cortisol") → apresenta o produto imediatamente como o "atalho/ferramenta" para conseguir isso sem esforço. O UMS (Mecanismo Único da Solução, ver `fase1-extracao-produto.md`) entra aqui como revelação, não como pitch.

### 4. PAS + Viés Financeiro
- **Problema:** nomeia o problema real (ex.: dietas falhas)
- **Agitação:** dor emocional (vergonha) + dor financeira (dinheiro já gasto em soluções caras/inúteis)
- **Solução:** o produto como alternativa barata e definitiva

### 5. A Absolvição ("Não é culpa sua")
Tira o peso das costas do cliente. Usa o UMP (Mecanismo Único do Problema) para culpar a biologia, a indústria ou os hormônios — nunca o esforço ou caráter do avatar. Valida o fracasso anterior dele para baixar a guarda. Este bloco é o que mais constrói confiança — é também o mais comumente esquecido; nunca pular.

### 6. Storytelling Micro (Prova Social)
Exatamente uma anedota de 2 frases sobre **outra pessoa** notando a mudança (marido, amiga invejosa, ex-namorado, médico) — nunca o próprio sujeito descrevendo o que sentiu. Cinematicamente específico, não genérico.

### 7. Empilhamento de Benefícios
Lista rápida (bullet points falados) de 3-4 ganhos tangíveis, misturando físicos e emocionais. Estrutura paralela, frases curtas. Regra dos três (Steve Jobs): três exemplos batem mais forte que um ou dois.

### 8. CTA Triplo (Sequência Lógica)
Sempre nesta ordem, nunca pular etapa:
1. **White (Convite suave):** "Veja o vídeo..."
2. **Gray (Escassez/Medo da Perda):** "Antes que saia do ar..."
3. **Black (Ultimato/Desafio):** "Ou mude de vida ou continue sofrendo. Clica."

---

## As 3 Estruturas Invisíveis (camada de ritmo/narrativa sobre os 8 blocos)

Estas três estruturas descrevem **como o ritmo e a ordem de revelação** se organizam dentro dos 8 blocos acima — escolha uma por roteiro, de acordo com o objetivo do teste (retenção vs conversão vs velocidade de resultado). ID usado na matriz de testes: `logica_dopamina` | `jornada_redencao` | `prova_visual`.

### `logica_dopamina` — A Lógica da Dopamina
**Foco:** retenção alta (hold rate).
1. Gancho Negativo — proíbe o uso do produto se a pessoa não quiser um resultado exagerado
2. Validação Imediata (fast-paced) — pula a história longa, vai direto pro resultado ("eu testei e perdi X em Y dias")
3. Desafio Lógico — cria dissonância cognitiva ("se você faz dieta e não emagrece, está fazendo errado")
4. Autoridade Externa — introduzida rapidamente para dar credibilidade ao absurdo
5. CTA de Curiosidade — "assista para ver os 3 ingredientes"

**Quando usar:** quando o objetivo do teste é maximizar tempo assistido / hold rate, não necessariamente conversão direta.

### `jornada_redencao` — A Jornada da Redenção
**Foco:** conversão/ROAS.
1. Validação de Ceticismo — "eu sei que parece loucura/impossível..." (desarma a defesa)
2. O Paradoxo Geográfico/Contextual — contraste entre a realidade local (falha) e uma realidade "especial" (sucesso)
3. O Mecanismo Único (a chave) — explica que o problema não é o óbvio, é o processamento/mecanismo escondido
4. A Solução Acessível — ancoragem de preço ("o mesmo efeito de [alternativa cara], mas natural/acessível")
5. Escassez por Conspiração — "a indústria está tentando derrubar este vídeo, assista antes que saia do ar"

**Quando usar:** quando o objetivo é conversão direta e o produto tem uma alternativa cara estabelecida para ancorar.

### `prova_visual` — A Prova Visual
**Foco:** resultado rápido, baixa fricção cognitiva.
1. Afirmação de Resultado — "de XL para M em 90 dias"
2. Prova Social/Médica — "meu médico viu os exames", "meu marido virou guarda-costas"
3. Facilidade de Uso — eliminação de esforço ("sem academia, sem cortar pizza")
4. Passo a Passo Simplificado — menciona que existe um método com N ingredientes/passos
5. Garantia Ousada (opcional) — "se não funcionar, eu devolvo o dinheiro"

**Quando usar:** avatares com baixa paciência para narrativa longa, ou quando o produto tem prova visual forte disponível (antes/depois real).

---

## Regra de combinação

A estrutura invisível (`logica_dopamina`/`jornada_redencao`/`prova_visual`) escolhe **o ritmo de revelação**; os 8 blocos seguem sendo o esqueleto fixo por baixo. Na prática: mapeie os passos da estrutura invisível escolhida dentro dos blocos 1-8 — por exemplo, em `jornada_redencao`, "Validação de Ceticismo" entra no Bloco 2 (Delimitação) e "Escassez por Conspiração" reforça o Bloco 8 (CTA Gray).
