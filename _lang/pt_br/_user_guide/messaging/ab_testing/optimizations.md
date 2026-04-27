---
nav_title: Otimizações
article_title: Otimize os Testes A/B com variantes vencedoras ou personalizadas
page_order: 1
page_type: reference
description: "Aprenda a usar Variante Vencedora ou Variante Personalizada ao criar testes multivariantes e A/B."
---

# Otimize os Testes A/B com Variante vencedora ou Variantes personalizadas {#optimize-ab-tests-with-winning-variant-or-personalized-variants}

> Aprenda a usar Variante Vencedora ou Variante Personalizada ao criar testes multivariantes e A/B.

Ao [criar um teste A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/) para campanhas de e-mail, push, webhook, SMS e WhatsApp programadas para enviar uma vez, você pode selecionar uma otimização. Existem duas opções de otimização: **Variante Vencedora** e **Variante Personalizada**.

![Opções de otimização listadas na seção de Testes A/B ao escolher seu público-alvo. Três opções estão listadas: Sem otimização, Variante vencedora e Variante personalizada. A variante personalizada é selecionada.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Ambas as opções funcionam enviando um teste inicial para uma porcentagem do seu segmento alvo. Após o teste terminar, os usuários restantes em seu público são enviados ou para a variante de melhor desempenho (Variante Vencedora) ou para a variante com a qual eles têm mais probabilidade de se engajar (Variante Personalizada).

{% alert tip %}
As otimizações estão localizadas na etapa **Públicos-alvo** da criação da campanha, em **Testes A/B**.
{% endalert %}

## Variante vencedora {#winning-variant}

Enviar a Variante Vencedora é semelhante a um teste A/B padrão. Os usuários deste grupo receberão a Variante Vencedora quando o teste inicial estiver completo.

1. Selecione **Variante Vencedora** e especifique qual porcentagem do público da sua campanha deve ser atribuída ao grupo da Variante Vencedora.
2. Configure as seguintes definições adicionais.

| Campo | Descrição |
| --- | --- |
| Determinar Variante Vencedora | A métrica a ser otimizada. Escolha entre *Aberturas Únicas* ou *Cliques* para e-mail, *Aberturas* para push, ou *Taxa de conversão primária* para todos os canais. Selecionar *Aberturas* ou *Cliques* para determinar a vencedora não afeta o que você escolhe para os [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) da campanha. <br><br>Lembre-se de que, se você estiver usando um grupo de controle, os usuários no grupo de controle não podem realizar *Aberturas* ou *Cliques*, então o desempenho do grupo de controle será garantidamente `0`. Como resultado, o grupo de controle não pode vencer o teste A/B. No entanto, você ainda pode querer usar um grupo de controle para acompanhar outras métricas de usuários que não recebem uma mensagem. |
| Horário de envio da Variante Vencedora | A data e o horário em que a variante vencedora será enviada. |
| Se nenhuma Variante Vencedora puder ser determinada | O que acontece se nenhuma variante vencer por uma margem estatisticamente significativa. Escolha entre enviar a variante com melhor desempenho mesmo assim ou encerrar o teste sem enviar mais mensagens. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Variante personalizada {#personalized-variant}

Use Variantes Personalizadas para enviar a cada usuário do seu segmento alvo a variante com a qual ele tem maior probabilidade de se engajar.

Para determinar a melhor variante para cada usuário, a Braze enviará um teste inicial para uma parte do seu público-alvo a fim de identificar associações entre características dos usuários e preferências de mensagem. Com base em como os usuários respondem a cada variante no teste inicial, essas características são usadas para determinar qual variante os usuários restantes receberão. Se nenhuma associação for encontrada e nenhuma personalização puder ser feita, a Variante Vencedora será enviada automaticamente para os usuários restantes. Para saber mais sobre como as Variantes Personalizadas são determinadas, consulte [Análise de dados de testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/#personalized-variant).

1. Selecione **Variante Personalizada** e especifique qual porcentagem do público da sua campanha deve ser atribuída ao grupo da Variante Personalizada.
2. Configure as seguintes definições adicionais.

| Campo | Descrição |
| --- | --- |
| Determinar Variante Personalizada | A métrica a ser otimizada. Escolha entre *Aberturas Únicas* ou *Cliques* para e-mail, *Aberturas* para push, ou *Taxa de conversão primária* para todos os canais. Selecionar *Aberturas* ou *Cliques* para determinar a vencedora não afeta o que você escolhe para os [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) da campanha. <br><br>Lembre-se de que, se você estiver usando um grupo de controle, os usuários no grupo de controle não podem realizar *Aberturas* ou *Cliques*, então o desempenho do grupo de controle será garantidamente `0`. Como resultado, o grupo de controle não pode vencer o teste A/B. No entanto, você ainda pode querer usar um grupo de controle para acompanhar outras métricas de usuários que não recebem uma mensagem. |
| Horário de envio da Variante Personalizada | A data e o horário em que a variante personalizada será enviada. |
| Se nenhuma Variante Personalizada puder ser determinada | O que acontece se nenhuma Variante Personalizada for encontrada. Escolha entre enviar a Variante Vencedora no lugar ou encerrar o teste sem enviar mais mensagens. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Análise de dados {#analytics}

Para saber mais sobre os resultados do seu teste A/B com otimização, consulte [Análise de dados de testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/).