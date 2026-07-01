# Hook Taxonomy — Arquétipos de Gancho (niche-agnostic)

> 10 arquétipos de gancho para os primeiros 1-3 segundos de um criativo (vídeo ou headline de imagem estática). Destilados de `referencias/copy-prompts-extraido.md` (seção 8) e generalizados para qualquer nicho/produto. IDs usados em `corpus/entries/*.json` e em `skills/ads-builder/prompts/fase2-estrategia-criativa.md`.
>
> **Teste de niche-agnosticidade:** se você substituir o nicho/produto e a lógica do gancho continua de pé, o arquétipo está certo.

---

### `aviso_reverso` — Aviso Reverso
**Gatilho psicológico:** `curiosidade` + `aversao_a_perda`
**Fórmula:** `[Comando Negativo] + [Ingrediente/Objeto Comum] + [Consequência Irônica/Exagerada]`
**Por que funciona:** o cérebro paralisa com "não faça" e fica confuso quando a consequência apresentada como negativa é, na verdade, positiva (ex.: calça caindo de magreza). A contradição força o espectador a continuar assistindo para resolver a confusão.
**Template:** `"Não misture/faça [X comum] com [Y comum] se você não quiser [resultado positivo disfarçado de ameaça]."`
**Exemplo do corpus:** *"Não misture chocolate com esses 3 ingredientes se você não quiser ver suas calças caindo em 15 dias."*
**Quando usar:** campanhas de retenção alta (vídeo) — funciona melhor como gancho de abertura do que como headline estática, porque depende do timing da virada.

---

### `conspiracao_revelada` — Conspiração Revelada
**Gatilho psicológico:** `raiva_externa` + `fomo`
**Fórmula:** `[Inimigo Poderoso] + [Descobriu/Escondeu a Solução] + [Ancoragem de Preço Alto] + [Prova]`
**Por que funciona:** cria cenário "nós contra eles" — o espectador se sente parte de um grupo informado contra uma instituição que lucra com a ignorância dele. A ancoragem de preço caro valoriza a solução barata que vem a seguir.
**Template:** `"Em [ano], [inimigo] descobriu [mecanismo/ingrediente]... e escondeu de você para vender [alternativa cara] por [preço]."`
**Exemplo do corpus:** *"Em 2015, a Big Pharma descobriu 3 ingredientes naturais... e escondeu de você para vender canetas de $2.000."*
**Quando usar:** melhor em campanhas de escala/ROAS — funciona em vídeo e em imagem estática (Style 3 Editorial Illustration combina bem com este gancho).

---

### `injustica_comparativa` — Injustiça Comparativa
**Gatilho psicológico:** `identificacao` + `inveja_construtiva`
**Fórmula:** `[Cenário Injusto (Você vs. Outra Pessoa)] + [Causa Raiz / Mecanismo "Desligado"]`
**Por que funciona:** valida a frustração do espectador comparando-o a alguém parecido que não sofre o mesmo problema, e tira a culpa dele colocando-a num mecanismo biológico/externo "desligado" — não é falta de esforço.
**Template:** `"Por que você [esforço X] e [resultado ruim], enquanto [pessoa similar] [esforço oposto] e [resultado bom]? O segredo está em [mecanismo desligado]."`
**Exemplo do corpus:** *"Por que você come pouco e engorda, enquanto sua amiga come muito e emagrece? O segredo está nos 3 hormônios que você tem DESLIGADOS..."*
**Quando usar:** qualquer nicho com comparação social forte (saúde, dinheiro, relacionamento, beleza).

---

### `transformacao_visual_especifica` — Transformação Visual Específica
**Gatilho psicológico:** `praticidade` + `autoridade_confiada`
**Fórmula:** `[Ponto A → Ponto B com Métrica Visual] + [Ação Contra-Intuitiva] + [Autoridade Chocada]`
**Por que funciona:** é tangível e visual — números específicos funcionam como prova implícita (ver `static-image-psychology.md`, princípio 6), e a reação de uma autoridade (médico, treinador) valida o resultado sem o espectador precisar confiar cegamente no narrador.
**Template:** `"De [estado A] para [estado B] em [prazo] fazendo [ação contra-intuitiva]. [Autoridade] não acreditou."`
**Exemplo do corpus:** *"De L para S em 60 dias comendo chocolate diariamente. Meu médico não acreditou nos exames."*
**Quando usar:** o gancho mais forte para o estilo visual `infographic` e `realistic_photography` em imagem estática; em vídeo, funciona bem com o formato de execução `antes_depois`.

---

### `ouch_factor` — Ouch Factor
**Gatilho psicológico:** `vergonha_social` + `identificacao`
**Fórmula:** toca diretamente na ferida física, de vergonha corporal ou de intimidade — sem metáfora, sem rodeio.
**Por que funciona:** a especificidade da dor (não genérica) faz o espectador sentir que o anúncio "sabe" exatamente o que ele vive — identificação imediata e visceral.
**Template:** `"[Frase mais dolorosa que o avatar já pensou ou ouviu sobre si mesmo]."`
**Exemplos do corpus:** *"Minhas pernas roçavam até sangrar."* / *"Eu senti inveja da minha filha."* / *"Eu odiava meu marido me tocando."*
**Quando usar:** quando o briefing/VOC do avatar tem confissões reais e específicas disponíveis — nunca inventar a dor, extrair do briefing/pesquisa de voz do cliente.

---

### `contrarian` — Contrarian
**Gatilho psicológico:** `curiosidade` + `raiva_externa`
**Fórmula:** ataca um método tradicional amplamente aceito como perda de tempo ou crença ultrapassada.
**Por que funciona:** quebra a expectativa do espectador sobre o que "todo mundo sabe" — gera dissonância cognitiva que só se resolve assistindo/lendo o resto.
**Template:** `"[Crença popular] está errado. Pare de [comportamento comum]."`
**Exemplos do corpus:** *"Calorias não importam."* / *"Salada te engorda."* / *"Amor próprio não paga a conta da minha tristeza."*
**Quando usar:** avatares com awareness alto (já tentaram o método tradicional e falharam) — não funciona em awareness baixo, onde o método tradicional ainda não foi testado pelo avatar.

---

### `story_tease` — Story Tease
**Gatilho psicológico:** `curiosidade`
**Fórmula:** começa "in media res" — no meio do caos, do drama ou da virada — sem contexto inicial.
**Por que funciona:** abre um loop narrativo (tensão não resolvida) que o cérebro não consegue ignorar; a falta de contexto força o espectador a continuar para entender "como cheguei aqui".
**Template:** `"[Frase que só faz sentido completo depois de assistir o resto]..."`
**Exemplos do corpus:** *"Quando o policial pediu meu passaporte..."* / *"Eu entrei na farmácia e comecei a rir na cara do atendente..."* / *"Meu médico olhou meus exames e disse que era impossível..."*
**Quando usar:** melhor formato para vídeo com narrativa storytelling completa (ver `structure-library.md`, Estrutura B); fraco em imagem estática, que não tem tempo de resolver o loop.

---

### `visual_shock_asmr` — Choque Visual / ASMR
**Gatilho psicológico:** `curiosidade` (via interrupção sensorial)
**Fórmula:** prop incomum em cena ou ASMR agressivo (som de batida, textura, pote deslizando) + declaração polêmica simultânea.
**Por que funciona:** interrupção sensorial (som ou imagem inesperada) quebra o scroll antes mesmo da frase ser processada — o gatilho é pré-cognitivo, a frase reforça depois.
**Template:** visual: `[ação física inusitada com objeto comum]` + copy: `[declaração polêmica/contrarian simultânea]`.
**Quando usar:** só em vídeo — depende do componente sonoro/visual, não tem equivalente direto em imagem estática (usar `pattern_interrupt` da imagem como substituto, ver `static-image-psychology.md` princípio 7).

---

### `revolta_financeira` — Revolta Financeira
**Gatilho psicológico:** `raiva_externa` + `aversao_a_perda`
**Fórmula:** ação física de indignação (rasgar uma conta, jogar remédio caro no lixo, mostrar fatura) + declaração de revolta financeira.
**Por que funciona:** combina a dor de ter sido enganado financeiramente com a indignação moral — o espectador se sente "feito de bobo" e quer a alternativa que devolve esse controle.
**Template:** `"Pare de ser feito(a) de [bobo/otário] por [indústria/sistema]."`
**Exemplo do corpus:** *"Pare de ser feita de otária pela farmácia."*
**Quando usar:** nichos onde existe alternativa cara e estabelecida pra comparar (medicamentos de marca, procedimentos estéticos, serviços financeiros).

---

### `identidade_vulnerabilidade` — Identidade / Vulnerabilidade
**Gatilho psicológico:** `identificacao` + `pertencimento`
**Fórmula:** confissão chocante e vulnerável sobre a própria identidade ou autoimagem.
**Por que funciona:** a vulnerabilidade genuína (não a dor física, mas a dor de identidade) desarma o ceticismo do espectador — ele baixa a guarda porque reconhece um sentimento que tem vergonha de admitir em voz alta.
**Template:** `"Eu [confissão vulnerável que a maioria não admitiria em voz alta]."`
**Exemplos do corpus:** *"Eu senti inveja da minha filha."* / *"Eu odiava meu marido me tocando."*
**Quando usar:** junto com o bloco de Absolvição (ver `structure-library.md`) — a confissão só funciona se for seguida de uma explicação que tira a culpa do espectador.

---

## Tabela de Gatilhos Psicológicos (vocabulário compartilhado)

Os IDs de gatilho abaixo são os mesmos usados no `adv-agent` (`knowledge-updater/extraction-protocol.md`, tabela B2) — mantidos idênticos de propósito, para que o vocabulário de emoção/gatilho seja compatível entre os dois grafos de referência.

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
