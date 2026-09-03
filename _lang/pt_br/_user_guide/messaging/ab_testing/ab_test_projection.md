---
nav_title: Projeção de testes A/B
article_title: Projeção de testes A/B
page_order: 20
hidden: true
page_type: reference
description: "Este artigo explica como funciona a projeção de testes A/B, como executar uma projeção e como a Braze usa seus dados."
---

# Projeção de testes A/B {#ab-test-projection}

> A projeção de testes A/B usa redes neurais para prever quais linhas de assunto têm melhor desempenho. Nosso modelo extrai recursos linguísticos dos testes A/B vencedores realizados na Braze e usa esses padrões linguísticos estatísticos para ensinar à nossa IA o que torna as linhas de assunto melhores.

{% alert important %}
Esse recurso está atualmente em acesso antecipado. Entre em contato com seu CSM ou gerente de conta da Braze se tiver interesse em participar do acesso antecipado.
{% endalert %}

## Execução de uma projeção {#running-a-projection}

Na composição da campanha, insira suas variantes de mensagens e suas linhas de assunto no editor. Quando estiver pronto, acesse a etapa **Target Audience** do fluxo de criação da campanha. No painel **Testes A/B**, selecione **Run Projection**.

<img width="518" alt="image" src="https://github.com/braze-inc/braze-docs/assets/17167198/8e74835c-76e4-4241-9763-c4f86a622c75">

Um modal será aberto com as linhas de assunto de quaisquer variantes de mensagens que você já tenha criado. Opcionalmente, você pode inserir linhas de assunto adicionais (até no máximo dez) digitando manualmente no campo e executando a projeção. Selecione **Run Projection**.

<img width="722" alt="image" src="https://github.com/braze-inc/braze-docs/assets/17167198/f9ad45a3-6565-467b-a7f6-35277bef7699">

A linha de assunto que nossa IA prevê como a melhor será destacada com o rótulo **Projected Winner**.

{% alert note %}
Para [Campaigns de push para múltiplas plataformas]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push), os testes A/B são compatíveis quando você seleciona múltiplas plataformas.
{% endalert %}

### Qual é a precisão das projeções? {#how-accurate-are-the-projections}

Em testes, descobrimos que as projeções têm cerca de 70% de precisão ao escolher entre pares de mensagens em testes A/B reais. Leve isso em consideração ao interpretar as mensagens que o modelo projeta como vencedoras.

### Como usamos seus dados? {#how-do-we-use-your-data}

Esse recurso aprende com testes A/B anteriores realizados na Braze. O conteúdo real das suas mensagens ou de qualquer outro cliente da Braze nunca é fornecido ao modelo. Primeiro, extraímos os padrões linguísticos de alto nível que preveem mensagens vencedoras em testes A/B. Em seguida, fornecemos esses padrões à nossa IA para ensiná-la a identificar quais características linguísticas constituem linhas de assunto superiores.