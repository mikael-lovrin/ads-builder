# Fase 0 — Onboarding

> Esta fase roda SEMPRE primeiro, antes de qualquer outra. Ela define como o projeto vai operar e inicializa a matriz de testes.

---

## Passo 1 — Verificar Projeto Existente

Verifique se `projects/[marca]/progress.md` existe.

- **Sim** → Leia-o. Informe: *"Encontrei progresso salvo para [marca]: [última fase concluída], próximo passo: [próxima fase]. Quer continuar daqui ou recomeçar do zero?"*
  - Continuar → vá direto para a fase indicada. Pule os passos abaixo.
  - Recomeçar → continue com Passo 2.
- **Não** → Continue com Passo 2.

---

## Passo 2 — Selecionar Cenário

```
Para começar, onde você está neste projeto?

A) Tenho criativos de referência (concorrentes ou meus próprios vencedores) para analisar e lateralizar
B) Criando do zero — sem referências externas disponíveis
C) Já tenho ângulo e gancho definidos — quero ir direto para o roteiro/briefing

Qual se aplica?
```

---

## Passo 3 — Tipo de Anúncio

```
Que tipo de criativo você precisa?

1) Roteiro de vídeo (Reels/TikTok/UGC)
2) Briefing de imagem estática (Meta)
3) Ambos
```

Guarde a escolha — define se as Fases 3a, 3b ou as duas vão rodar.

---

## Passo 4 — Modo de Execução

```
Como quer trabalhar?

1) Passo-a-passo (recomendado para projetos novos): paro após cada fase para aprovação
2) Autônomo: rodo as fases sem parar, decido sozinho nas escolhas que normalmente apresentaria,
   e só aviso ao final de cada fase. Paro apenas se precisar de dados que só você tem.
```

Guarde o modo em `progress.md`. No modo autônomo, registre no documento de cada fase o que escolheu e por quê.

---

## Passo 5 — Mercado e Idioma

```
Em que mercado/idioma o criativo vai rodar?
Exemplos: Brasil, português | EUA, inglês | México, espanhol
```

Isso define o idioma do roteiro/briefing final. Se o usuário colar materiais em outro idioma (referências, VSL), use-os normalmente — o output final fica no idioma do mercado-alvo. Se o mercado-alvo não for o idioma desta conversa, mantenha a voz nativa do mercado (ver `prompts/fase4-revisao-traducao.md`).

---

## Passo 6 — Plataforma(s)

```
Em que plataforma(s) este criativo vai rodar?
(Meta Feed, Reels, TikTok, Pinterest, Stories — pode ser mais de uma)
```

Plataforma muda restrições de formato e é uma das 6 dimensões da matriz de testes — guarde explicitamente.

---

## Passo 7 — Briefing

Colete (ou extraia do que o usuário já forneceu):

```
1. Nome da marca/produto
2. Produto ou serviço (descrição em 2-3 linhas)
3. Nicho principal
4. Avatar: quem é a pessoa que compra? (idade, situação, problema principal, o que já tentou)
5. Tem ângulo em mente? (ou deixa o agente sugerir na Fase 2)
6. O que já foi testado antes para esta marca? (ou "nenhum histórico ainda" — vale checar projects/[marca]/kill-list.md se já existir)
```

**Se Cenário C**, adicione:
```
7. Descreva o ângulo/gancho aprovado
8. Já tem estrutura/formato definido ou prefere que o agente sugira?
```

---

## Passo 8 — Salvar

**Salve `projects/[marca]/briefing.md`** (parte 1 — a parte 2 é completada na Fase 1):

```markdown
# Briefing — [Nome da Marca]
**Data:** [data]
**Modo:** [Passo-a-passo / Autônomo]
**Cenário:** [A / B / C]
**Mercado:** [país, idioma]
**Tipo de anúncio:** [Vídeo / Imagem / Ambos]
**Plataforma(s):** [lista]

## Produto/Serviço
[descrição em 2-3 linhas]

## Nicho
[nicho]

## Avatar
[descrição: idade, situação, problema principal, o que já tentou]

## Ângulo Inicial
[descrição se fornecida | "a definir na Fase 2"]

## Histórico de Testes
[o que o usuário informou | "nenhum teste anterior registrado"]
```

**Inicialize `projects/[marca]/tracking/test-matrix.json`** seguindo o protocolo de inicialização em `prompts/combinacoes.md`. Se já existe e o usuário escolheu continuar (não recomeçar), preserve o JSON existente.

**Crie/atualize `progress.md`:**
```markdown
# Progresso — [Nome da Marca]
Modo: [modo]
Cenário: [cenário]
Mercado: [país, idioma]
Tipo de anúncio: [vídeo/imagem/ambos]
Última fase: Fase 0 — Onboarding | Arquivo: briefing.md
Próxima fase: Fase 1 — Extração de Produto
```

---

## Passo 9 — Avançar

**Tabela de avanço:**

| Cenário | Próximo passo |
|---|---|
| A | Fase 1 (Extração de Produto) → `skills/creative-pattern-analysis/SKILL.md` (Pre-Build Mode) → Fase 2 |
| B | Fase 1 (Extração de Produto) → Fase 2 |
| C, sem dado de produto completo | Fase 1 → Fase 3a/3b direto (pula Fase 2) |
| C, com tudo definido | Fase 3a/3b diretamente |

**Se Cenário A**, antes de seguir, peça os materiais de referência:
```
Cole aqui os criativos de referência (roteiros/transcrições de vídeo, ou copy + descrição da imagem),
um de cada vez. Pode ser de concorrentes ou seus próprios vencedores anteriores.
```
Esses materiais serão usados pela `skills/creative-pattern-analysis/SKILL.md` depois da Fase 1.
