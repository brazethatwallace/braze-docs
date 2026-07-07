---
nav_title: Correspondência de critérios de saída com eventos de entrada
article_title: Correspondência de critérios de saída com eventos de entrada
page_order: 5
page_type: tutorial
description: "Saiba como configurar critérios de saída e jornadas de ação que comparam propriedades de eventos com propriedades de entrada do Canvas, para que os usuários só saiam ou sigam uma ramificação quando concluírem a ação específica com a qual entraram."
tool: Canvas
---

# Correspondência de critérios de saída com eventos de entrada {#matching-exit-criteria-to-entry-events}

> Este artigo explica como configurar critérios de saída e jornadas de ação que se correlacionam diretamente com o evento de entrada do Canvas, para que os usuários só saiam ou sigam uma ramificação quando realizarem uma ação específica relacionada ao motivo pelo qual entraram no Canvas.

Ao comparar propriedades de eventos com [propriedades de entrada do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties), você pode criar fluxos altamente direcionados. Por exemplo, em um Canvas de checkout abandonado, você pode configurar um usuário para sair somente quando ele comprar o item exato que abandonou, enquanto continua recebendo mensagens de lembrete se comprar um item diferente.

Essa abordagem usa [variáveis de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) para comparar propriedades entre eventos. O padrão se aplica a muitos cenários além do eCommerce, incluindo renovações de apólices, lembretes de reservas e gerenciamento de inscrições.

## Critérios de saída: saindo do Canvas quando uma ação correspondente ocorre {#exit-criteria-exiting-the-canvas-when-a-matching-action-occurs}

Use [critérios de saída]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria) quando quiser que um usuário saia completamente do Canvas após realizar uma ação que corresponda ao evento de entrada.

### Exemplo: compra de ingresso abandonada {#example-abandoned-ticket-purchase}

Neste cenário, um usuário entra no Canvas quando realiza o evento personalizado `Selected Ticket`, que contém uma propriedade chamada `event_id`. Os critérios de saída são configurados para que, quando um usuário acionar o evento personalizado `Purchased Ticket` — que também inclui uma propriedade chamada `event_id` —, a propriedade do evento de saída seja comparada com a propriedade do evento de entrada. Se as duas corresponderem, o usuário sai do Canvas.

Isso significa que:

- Se o usuário comprar o mesmo ingresso que selecionou originalmente, ele sai do Canvas e para de receber lembretes.
- Se o usuário comprar um ingresso diferente, ele permanece no Canvas e continua recebendo mensagens de acompanhamento sobre o ingresso original.

Para configurar isso:

1. Configure uma entrada de Canvas baseada em ação com o evento personalizado de gatilho (como `Selected Ticket`) e sua propriedade relevante (como `event_id`).
2. Na etapa **Público-alvo**, configure o evento de exceção dos critérios de saída com o evento personalizado de conclusão (como `Purchased Ticket`).
3. Selecione **Add property filters** e adicione um filtro onde a comparação da propriedade básica `event_id` esteja definida como `equals`.
4. Ative o toggle **Personalize value**, defina o **Personalization type** como `Context Variables` e defina o **Attribute** como `event_id`.

Isso compara o `event_id` do evento `Purchased Ticket` com o `event_id` armazenado do evento de entrada original do Canvas. Para mais detalhes sobre como configurar esses filtros, consulte [Exemplos de critérios de saída]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#exit-criteria-examples).

## Jornadas de ação: ramificação com base em uma ação correspondente {#action-paths-branching-based-on-a-matching-action}

Use [Jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) quando quiser que um usuário permaneça no Canvas, mas siga uma jornada diferente dependendo de a ação subsequente corresponder ou não ao evento de entrada.

### Exemplo: checkout abandonado com jornadas ramificadas {#example-abandoned-checkout-with-branching-paths}

Neste cenário, um usuário que selecionou um item mas não concluiu a compra primeiro recebe uma mensagem de checkout abandonado. Em seguida, o usuário é mantido em uma etapa de Jornadas de ação por uma semana antes de ser direcionado para três jornadas com base no que fez durante esse período:

- **Concluiu a compra original:** o ID da propriedade do evento personalizado é igual ao ID da propriedade de entrada. Esses usuários podem receber uma mensagem de agradecimento ou uma recomendação de venda cruzada.
- **Fez uma compra diferente:** o ID da propriedade do evento personalizado não é igual ao ID da propriedade de entrada. Esses usuários podem receber um lembrete sobre o item original.
- **Não fez nenhuma compra:** cai no grupo **Restante do público**. Esses usuários podem receber um incentivo mais forte ou um lembrete final.

Para configurar isso:

1. Adicione uma etapa de [Jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) e defina o período de avaliação (como uma semana).
2. Para o primeiro grupo de ação (compra original), adicione um gatilho para o evento personalizado de conclusão (como `Purchased_Ticket`). Selecione **Add property filters** e adicione um filtro onde a comparação da propriedade básica `event_id` esteja definida como `equals`. Ative **Personalize value**, defina o **Personalization type** como `Context Variables` e defina o **Attribute** como `event_id`.
3. Para o segundo grupo de ação (compra diferente), adicione o mesmo evento de gatilho, mas defina a comparação como `does not equal` com a mesma configuração de variável de contexto.
4. Use o grupo **Restante do público** para usuários que não realizaram o evento de conclusão.

Para mais detalhes sobre como configurar esses filtros, consulte [Exemplos de Jornadas de ação]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#action-path-examples).

## Outras aplicações {#other-applications}

Embora este artigo use um exemplo de compra abandonada, você pode aplicar o mesmo padrão a qualquer cenário em que uma ação de conclusão precise se correlacionar com a ação de entrada, incluindo:

- **Renovações de apólices:** remova do Canvas os usuários que renovarem a apólice específica que acionou o Canvas.
- **Lembretes de reservas:** ramifique usuários com base em se confirmaram ou modificaram a reserva original.
- **Gerenciamento de inscrições:** direcione usuários de forma diferente dependendo de terem feito upgrade do plano específico sobre o qual foram notificados.
- **Registros em eventos:** remova do Canvas os usuários que concluírem o registro para o evento específico no qual demonstraram interesse.

## Informações importantes {#things-to-know}

- As configurações neste artigo são exemplos ilustrativos. Teste todos os componentes no seu ambiente de desenvolvimento antes de lançar.
- Verifique se os nomes das propriedades e os tipos de dados nos seus eventos de entrada correspondem aos usados nos critérios de saída ou nas jornadas de ação.
- Consulte [variáveis de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) para detalhes sobre como as comparações de propriedades funcionam entre eventos.