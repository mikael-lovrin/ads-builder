# Fase 1 — Extração de Produto

Objetivo: extrair, de forma estritamente factual (sem interpretar, sem inventar), os dados de produto que toda fase seguinte vai usar como insumo obrigatório. Resultado: completa `briefing.md` (parte 2).

---

## Setup

Peça ao usuário o material-fonte: um VSL, uma página de vendas, um briefing de produto já escrito, ou respostas diretas às perguntas abaixo se nada disso existir ainda.

Regras estritas (não negociáveis):
- Responda apenas o que foi pedido.
- Se uma informação não estiver explícita no material/resposta do usuário, registre **"Não mencionado"** — nunca preencha com suposição.
- Use apenas texto simples e bullet points.
- Seja conciso e direto.

---

## Estrutura de Extração

Extraia e registre, exatamente nesta ordem:

1. **Mecanismo Único** — qual a explicação lógica/científica de por que o produto funciona?
2. **UMP (Mecanismo Único do Problema)** — qual a causa real/escondida do problema que ninguém conta?
3. **UMS (Mecanismo Único da Solução)** — como o produto resolve o UMP de forma específica?
4. **Abordagens Tradicionais** — quais métodos comuns (dietas, exercícios, remédios etc.) o material cita?
5. **Falha das Abordagens** — por que essas abordagens tradicionais falham, segundo o material?
6. **Autoridade** — quais nomes de médicos, estudos ou mídias são citados?
7. **O Inimigo** — o que ou quem é especificamente o culpado pelo problema do avatar? (Regra: vilão vago como "o sistema" ou "big pharma" não serve — precisa ser específico e checável, ex.: "a indústria americana que trocou óleo de coco por óleos vegetais processados nos anos 80")
8. **Oferta** — qual o preço final, desconto ou bônus mencionado?
9. **Garantia** — qual o tempo de cobertura e a condição principal?

Se o usuário não tiver material-fonte (Cenário B, do zero), faça as 9 perguntas diretamente e registre as respostas como fornecidas — nunca complete lacunas com suposição, mesmo no modo autônomo. Falta de dado de produto real é sempre motivo de pausa, mesmo em modo autônomo (ver `SKILL.md`, Regras Críticas #6).

---

## Salvar

Anexe a extração a `projects/[marca]/briefing.md`, como uma seção `## Extração de Produto`:

```markdown
## Extração de Produto

**Mecanismo Único:** [...]
**UMP:** [...]
**UMS:** [...]
**Abordagens Tradicionais:** [...]
**Falha das Abordagens:** [...]
**Autoridade:** [...]
**O Inimigo:** [...]
**Oferta:** [...]
**Garantia:** [...]
```

Atualize `progress.md` (Última fase: Fase 1, Próxima fase: conforme tabela de avanço da Fase 0 — lateralização se Cenário A, senão Fase 2).
