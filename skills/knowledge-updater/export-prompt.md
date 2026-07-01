# Export Prompt — Minerar Conversas Antigas para o Corpus

> Use isto quando você tem uma conversa antiga do Claude (fora deste projeto) que resultou num criativo bom/vencedor, e quer trazer o que for reaproveitável para o corpus do `ads-builder`. Em vez de colar a conversa inteira aqui (ruído alto, contexto perdido), peça para o **Claude daquela própria conversa** fazer a curadoria — ele tem o contexto completo e ainda lembra o raciocínio por trás das escolhas.

---

## Por que pedir pra ele exportar, e não copiar a conversa crua

1. **Ele tem o contexto que se perdeu para você** — por que aquele gancho foi escolhido, o que foi testado e descartado, qual objeção o usuário levantou no meio do caminho. Resumir isso de fora é mais pobre do que pedir pra quem "estava lá".
2. **O corpus não quer a conversa, quer a inteligência extraída dela** — texto final + por que funcionou + classificação. Isso é exatamente o schema de `extraction-protocol.md`, então pedir já nesse formato economiza um passo.
3. **Separa sinal de ruído automaticamente** — tentativas descartadas, idas e vindas de aprovação, etc. não interessam ao corpus; só o que foi aprovado/rodou interessa.

---

## O Prompt (copie e cole na conversa antiga)

```
Você é o Claude desta conversa, que me ajudou a escrever um criativo de anúncio (vídeo ou
imagem) que considerei muito bom / que rodou bem. Quero levar o que for reaproveitável
desta conversa para um corpus de referência de criativos de Direct Response que mantenho
em outro projeto (um agente chamado "Ads Builder").

Esse corpus não guarda a conversa em si — guarda o criativo final classificado e a
inteligência por trás dele, de forma que sirva de referência para outros nichos/produtos
no futuro, não só para repetir este produto específico.

Releia esta conversa inteira e me devolva um export estruturado com exatamente isto:

1. CRIATIVO(S) FINAL(IS) — o texto completo e exato do que foi aprovado/usado: roteiro de
   vídeo (com os ganchos e qualquer instrução de cena/edição), ou o brief de imagem
   (prompt de imagem + hook + body copy). Sem resumir, sem editar — texto exato.

2. CONTEXTO/BRIEFING — produto, nicho, avatar (quem é, idade, dor), plataforma-alvo, e se
   discutimos UMP (causa do problema) e UMS (mecanismo da solução), inclua os dois.

3. DADO DE PERFORMANCE — qualquer métrica ou resultado mencionado nesta conversa (CTR,
   ROAS, "rodou bem", etc.). Se nada foi mencionado, diga explicitamente "sem dado de
   performance" — não invente.

4. SUA CLASSIFICAÇÃO (faça o seu melhor esforço, em português, sem precisar adivinhar IDs
   ou nomenclatura específica de outro sistema — só descreva):
   - Arquétipo de gancho dominante (ex.: "aviso negativo com consequência irônica",
     "comparação injusta entre duas pessoas", "confissão vulnerável")
   - Tipo: vídeo ou imagem estática
   - Emoção dominante no criativo
   - Estrutura/ritmo usado (se vídeo) ou estilo visual (se imagem)
   - Plataforma-alvo

5. POR QUE FUNCIONOU (2-3 frases) — o princípio reaproveitável, descrito de forma que
   funcionasse em OUTRO nicho/produto, não só descrevendo este produto específico.

6. PADRÃO POSSIVELMENTE NOVO — se algo nesta conversa não é só uma variação do óbvio
   (um gancho, formato de execução ou estrutura que pareceu original), aponte
   especificamente. Se não houver nada assim, diga "nenhum padrão novo identificado".

Regra: não invente nem suavize nada. Se não souber ou não lembrar algo, escreva
"não determinável" em vez de supor.

Formate tudo em markdown limpo, pronto para eu salvar como arquivo.
```

---

## O Que Fazer Com o Export

1. Salve o markdown retornado em `corpus/raw/[nome-descritivo].md` (crie a pasta `corpus/raw/` se ainda não existir)
2. Repita para cada conversa antiga que valer a pena minerar
3. Quando tiver alguns acumulados, rode `python scripts/build_corpus_index.py` (faz uma triagem rápida por palavra-chave, marca `needs_knowledge_updater: true`)
4. Depois, rode `skills/knowledge-updater/SKILL.md` numa sessão aqui no `ads-builder` — ele lê cada export, faz a extração completa seguindo `extraction-protocol.md`, propõe atualizações ao `knowledge/` (com sua aprovação) e atualiza `corpus/index.json`

Você também pode pular o `corpus/raw/` e colar o export direto numa sessão do `knowledge-updater` — funciona igual, só não fica salvo em disco como backup do material bruto.
