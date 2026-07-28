---
nav_title: Otimizações
article_title: Otimize testes A/B com variante vencedora ou variantes personalizadas
page_order: 1
page_type: reference
description: "Aprenda a usar variante vencedora ou variante personalizada ao criar testes multivariantes e A/B."
---

# Otimize testes A/B {#optimize-ab-tests}

> Aprenda a usar a otimização de variantes ao criar testes multivariantes e A/B.

## Push {#push}

Ao [criar um teste A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests) para push, há uma opção de otimização: [Seleção de Variante BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection). Esse recurso permite que seus testes A/B de envio único ou recorrentes executem automaticamente um experimento e otimizem para os melhores resultados de engajamento.

## E-mail, webhook, SMS e WhatsApp {#email-webhook-sms-and-whatsapp}

Ao [criar um teste A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests) para Campaigns de e-mail, webhook, SMS e WhatsApp agendadas para envio único, você pode selecionar entre duas opções de otimização: **Variante Vencedora** e **Variante Personalizada**.

![Opções de otimização listadas na seção de testes A/B ao escolher seu público-alvo. Três opções estão listadas: sem otimização, Variante Vencedora e Variante Personalizada. A Variante Personalizada está selecionada.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Ambas as opções funcionam enviando um teste inicial para uma porcentagem do seu segmento alvo. Após o teste terminar, os usuários restantes do seu público recebem a variante de melhor desempenho (Variante Vencedora) ou a variante com a qual eles têm mais probabilidade de se engajar (Variante Personalizada).

{% alert tip %}
As otimizações estão localizadas na etapa **Públicos-alvo** da criação da campanha, em **A/B Testing**.
{% endalert %}

## Variante Vencedora {#winning-variant}

Enviar a Variante Vencedora é semelhante a um teste A/B padrão. Os usuários deste grupo receberão a Variante Vencedora quando o teste inicial estiver completo.

1. Selecione **Winning Variant** e especifique qual porcentagem do público da sua campanha deve ser atribuída ao grupo da Variante Vencedora.
2. Configure as seguintes definições adicionais.

| Campo | Descrição |
| --- | --- |
| Determine Winning Variant | A métrica a ser otimizada. Escolha entre *Unique Opens* ou *Clicks* para e-mail, *Opens* para push, ou *Primary Conversion Rate* para todos os canais. Selecionar *Opens* ou *Clicks* para determinar a vencedora não afeta o que você escolhe para os [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) da campanha. <br><br>Lembre-se de que, se você estiver usando um grupo de controle, os usuários no grupo de controle não podem realizar *Opens* ou *Clicks*, então o desempenho do grupo de controle será garantidamente `0`. Como resultado, o grupo de controle não pode vencer o teste A/B. No entanto, você ainda pode querer usar um grupo de controle para acompanhar outras métricas de usuários que não recebem uma mensagem. |
| Winning Variant Send Time | A data e o horário em que a variante vencedora será enviada. |
| If No Winning Variant Can Be Determined | O que acontece se nenhuma variante vencer por uma margem estatisticamente significativa. Escolha entre enviar a variante com melhor desempenho mesmo assim ou encerrar o teste sem enviar mais mensagens. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variante Vencedora" }

{% alert note %}
Para variantes vencedoras e variantes personalizadas, a Braze executa uma verificação de elegibilidade novamente no segundo envio. Usuários que não estavam no segmento alvo (ou que não estavam acessíveis de outra forma) no primeiro envio podem entrar depois; usuários que saíram do segmento podem não receber mais o acompanhamento. Planeje seu segmento e agendamento para que o público que você pretende incluir seja elegível em ambos os envios.
{% endalert %}

## Variante Personalizada {#personalized-variant}

Use variantes personalizadas para enviar a cada usuário do seu segmento alvo a variante com a qual ele tem maior probabilidade de se engajar.

Para determinar a melhor variante para cada usuário, a Braze enviará um teste inicial para uma parte do seu público-alvo a fim de identificar associações entre características dos usuários e preferências de mensagem. Com base em como os usuários respondem a cada variante no teste inicial, essas características são usadas para determinar qual variante os usuários restantes receberão. Se nenhuma associação for encontrada e nenhuma personalização puder ser feita, a Variante Vencedora será enviada automaticamente para os usuários restantes. Para saber mais sobre como as variantes personalizadas são determinadas, consulte [Análise de dados de testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#personalized-variant).

1. Selecione **Personalized Variant** e especifique qual porcentagem do público da sua campanha deve ser atribuída ao grupo da Variante Personalizada.
2. Configure as seguintes definições adicionais.

| Campo | Descrição |
| --- | --- |
| Determine Personalized Variant | A métrica a ser otimizada. Escolha entre *Unique Opens* ou *Clicks* para e-mail, *Opens* para push, ou *Primary Conversion Rate* para todos os canais. Selecionar *Opens* ou *Clicks* para determinar a vencedora não afeta o que você escolhe para os [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) da campanha. <br><br>Lembre-se de que, se você estiver usando um grupo de controle, os usuários no grupo de controle não podem realizar *Opens* ou *Clicks*, então o desempenho do grupo de controle será garantidamente `0`. Como resultado, o grupo de controle não pode vencer o teste A/B. No entanto, você ainda pode querer usar um grupo de controle para acompanhar outras métricas de usuários que não recebem uma mensagem. |
| Personalized Variant Send Time | A data e o horário em que a variante personalizada será enviada. |
| If No Personalized Variant Can Be Determined | O que acontece se nenhuma variante personalizada for encontrada. Escolha entre enviar a Variante Vencedora no lugar ou encerrar o teste sem enviar mais mensagens. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variante Personalizada" }

## Análise de dados {#analytics}

Para saber mais sobre os resultados do seu teste A/B com otimização, consulte [Análise de dados de testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics).