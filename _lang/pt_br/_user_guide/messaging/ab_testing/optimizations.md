---
nav_title: Otimizações
article_title: Otimize Testes A/B com Variante Vencedora ou Variantes Personalizadas
page_order: 1
page_type: reference
description: "Saiba como usar a Variante Vencedora ou a Variante Personalizada ao criar testes multivariantes e Testes A/B."
---

# Otimize Testes A/B com Variante Vencedora ou Variantes Personalizadas

> Saiba como usar a Variante Vencedora ou a Variante Personalizada ao criar testes multivariantes e Testes A/B.

Ao [criar um teste A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/) para campanhas de e-mail, push, webhook, SMS e WhatsApp agendadas para envio único, você pode selecionar uma otimização. Existem duas opções de otimização: **Variante Vencedora** e **Variante Personalizada**.

![Opções de otimização listadas na seção de Testes A/B ao escolher seu público-alvo. Três opções são listadas: Sem Otimização, Variante Vencedora e Variante Personalizada. Variante Personalizada está selecionada.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Ambas as opções funcionam enviando um teste inicial para uma porcentagem do seu segmento-alvo. Após o término do teste, os usuários restantes do seu público recebem a variante com melhor performance (Variante Vencedora) ou a variante com a qual têm maior probabilidade de interagir (Variante Personalizada).

{% alert tip %}
As otimizações estão localizadas na etapa **Público-alvo** da criação de campanhas, em **Testes A/B**.
{% endalert %}

## Variante Vencedora

Enviar a Variante Vencedora é semelhante a um teste A/B padrão. Os usuários neste grupo receberão a Variante Vencedora quando o teste inicial for concluído.

1. Selecione **Variante Vencedora** e especifique qual porcentagem do público da sua campanha deve ser atribuída ao grupo da Variante Vencedora.
2. Configure as seguintes definições adicionais.

| Campo | Descrição |
| --- | --- | 
| Determinar Variante Vencedora | A métrica a ser otimizada. Escolha entre *Aberturas Únicas* ou *Cliques* para e-mail, *Aberturas* para push, ou *Taxa de conversão primária* para todos os canais. Selecionar *Aberturas* ou *Cliques* para determinar a vencedora não afeta o que você escolhe para os [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) da campanha. <br><br>Lembre-se de que, se você estiver usando um grupo de controle, os usuários no grupo de controle não podem realizar *Aberturas* ou *Cliques*, então a performance do grupo de controle será garantidamente `0`. Como resultado, o grupo de controle não pode vencer o teste A/B. No entanto, você ainda pode querer usar um grupo de controle para acompanhar outras métricas de usuários que não recebem uma mensagem. |
| Horário de Envio da Variante Vencedora | A data e o horário em que a variante vencedora será enviada. |
| Se Nenhuma Variante Vencedora Puder Ser Determinada | O que acontece se nenhuma variante vencer por uma margem estatisticamente significativa. Escolha entre enviar a variante com melhor performance mesmo assim ou encerrar o teste sem enviar mais mensagens. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Variante Personalizada

Use Variantes Personalizadas para enviar a cada usuário do seu segmento-alvo a variante com a qual ele tem maior probabilidade de interagir.

Para determinar a melhor variante para cada usuário, a Braze enviará um teste inicial para uma parte do seu público-alvo a fim de identificar associações entre características dos usuários e preferências de mensagem. Com base em como os usuários respondem a cada variante no teste inicial, essas características são usadas para determinar qual variante os usuários restantes receberão. Se nenhuma associação for encontrada e nenhuma personalização puder ser feita, a Variante Vencedora será enviada automaticamente para os usuários restantes. Para saber mais sobre como as Variantes Personalizadas são determinadas, consulte [Análise de dados de testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#personalized-variant).

1. Selecione **Variante Personalizada** e especifique qual porcentagem do público da sua campanha deve ser atribuída ao grupo da Variante Personalizada.
2. Configure as seguintes definições adicionais.

| Campo | Descrição |
| --- | --- | 
| Determinar Variante Personalizada | A métrica a ser otimizada. Escolha entre *Aberturas Únicas* ou *Cliques* para e-mail, *Aberturas* para push, ou *Taxa de conversão primária* para todos os canais. Selecionar *Aberturas* ou *Cliques* para determinar a vencedora não afeta o que você escolhe para os [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) da campanha. <br><br>Lembre-se de que, se você estiver usando um grupo de controle, os usuários no grupo de controle não podem realizar *Aberturas* ou *Cliques*, então a performance do grupo de controle será garantidamente `0`. Como resultado, o grupo de controle não pode vencer o teste A/B. No entanto, você ainda pode querer usar um grupo de controle para acompanhar outras métricas de usuários que não recebem uma mensagem. |
| Horário de Envio da Variante Personalizada | A data e o horário em que a variante personalizada será enviada. |
| Se Nenhuma Variante Personalizada Puder Ser Determinada | O que acontece se nenhuma Variante Personalizada for encontrada. Escolha entre enviar a Variante Vencedora no lugar ou encerrar o teste sem enviar mais mensagens. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Análise de dados

Para saber mais sobre os resultados do seu teste A/B com otimização, consulte [Análise de dados de testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/).