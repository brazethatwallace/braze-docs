---
nav_title: Projeção de testes A/B
article_title: Projeção de Testes A/B
page_order: 20
hidden: true
page_type: reference
description: "Este artigo explica como a projeção de testes A/B funciona, como executar uma projeção e como a Braze usa seus dados."
---

# Projeção de testes A/B

> A projeção de testes A/B usa redes neurais para prever quais linhas de assunto têm melhor desempenho. Nosso modelo extrai características linguísticas de testes A/B vencedores realizados na Braze e usa esses padrões estatísticos de linguagem para ensinar nossa IA o que torna as linhas de assunto melhores.

{% alert important %} 
Esse recurso está atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente ou gerente de conta da Braze se tiver interesse em participar do acesso antecipado.
{% endalert %}

## Executando uma projeção

Na composição da campanha, insira suas variantes de mensagem e suas linhas de assunto no editor. Quando estiver tudo pronto, acesse a etapa **Público-alvo** do fluxo de criação de campanha. No painel **Testes A/B**, selecione **Run Projection**.

<img width="518" alt="image" src="https://github.com/braze-inc/braze-docs/assets/17167198/8e74835c-76e4-4241-9763-c4f86a622c75">

Um modal será aberto com as linhas de assunto de todas as variantes de mensagem que você já criou. Opcionalmente, você pode inserir linhas de assunto adicionais (até no máximo dez) digitando manualmente no campo e executando a projeção. Selecione **Run Projection**.

<img width="722" alt="image" src="https://github.com/braze-inc/braze-docs/assets/17167198/f9ad45a3-6565-467b-a7f6-35277bef7699">

A linha de assunto que nossa IA prevê como a melhor será destacada com o rótulo **Projected Winner**.

{% alert note %}
Para [campanhas de push rápido]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/quick_push_messages/), os testes A/B são compatíveis quando você seleciona múltiplas plataformas.
{% endalert %}

### Qual é a precisão das projeções?

Em testes, descobrimos que as projeções têm cerca de 70% de precisão ao escolher entre pares de mensagens em testes A/B reais. Leve isso em consideração ao interpretar as mensagens que o modelo projeta como vencedoras.

### Como usamos seus dados?

Esse recurso aprende com testes A/B anteriores realizados na Braze. O conteúdo real das suas mensagens ou de qualquer outro cliente da Braze nunca é fornecido ao modelo. Primeiro, extraímos os padrões linguísticos de alto nível que preveem mensagens vencedoras em testes A/B. Em seguida, fornecemos esses padrões à nossa IA para ensiná-la a identificar quais características linguísticas constituem linhas de assunto superiores.