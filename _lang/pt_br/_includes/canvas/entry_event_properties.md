Você pode usar as propriedades de entrada do Canvas e as propriedades de evento nas jornadas de usuário do Canvas.

{% tabs local %}
{% tab Canvas Entry Properties %}

[As propriedades de entrada do Canvas]({{site.baseurl}}/api/objects_filters/context_object) são as propriedades que você mapeia para Canvas que são baseados em ações ou disparados por API. Note que o objeto `canvas_entry_properties` tem um limite máximo de tamanho de 50 KB.

{% alert note %}
Para canais de mensagem no app especificamente, `context` só pode ser referenciado no Canvas.
{% endalert %}

Você pode referenciar `context` em qualquer etapa de Mensagem com este formato Liquid: ``{% raw %} context.${property_name} {% endraw %}``. Note que os eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma.

#### Caso de uso {#use-case}

{% raw %}
Digamos que uma loja de varejo, RetailApp, tenha a seguinte solicitação: `"context" : {"product_name" : "shoes", "product_price" : 79.99}`.

A RetailApp pode puxar o nome do produto (shoes) para uma mensagem com este Liquid: `{{context.${product_name}}}`.
{% endraw %}

A RetailApp também pode disparar o envio de mensagens específicas para diferentes propriedades de `product_name` em um Canvas que direciona os usuários depois que eles acionam um evento de compra. Por exemplo, eles podem enviar mensagens diferentes para os usuários que compraram sapatos e para os usuários que compraram outra coisa, adicionando o seguinte Liquid em uma etapa de Mensagem.

{% raw %}
```markdown
{% if  {{context.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Expandir para o editor original do Canvas %}

Não é mais possível criar ou duplicar Canvas usando o editor original. Esta seção está disponível apenas para referência. Para os Canvas construídos com o editor original, as propriedades de entrada do Canvas podem ser referenciadas apenas na primeira etapa completa de um Canvas.

{% enddetails %}
{% endtab %}

{% tab Event Properties %}

As propriedades de evento referem-se às propriedades que você define para eventos personalizados e compras. Esses `event_properties` podem ser usados em Campaigns com entrega baseada em ação e Canvas.

{% alert important %}
Você não pode usar `event_properties` na primeira etapa de Mensagem do seu Canvas. Em vez disso, você deve usar `context` ou adicionar uma etapa de jornadas de ação com o evento correspondente **antes** da etapa de Mensagem que inclui `event_properties`.
{% endalert %}

No Canvas, propriedades de evento personalizado e de evento de compra podem ser usadas em Liquid em qualquer etapa de Mensagem que siga uma etapa de jornadas de ação. Certifique-se de usar {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} se você estiver referenciando essas propriedades de evento. Esses eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma no componente de Mensagem.

Na primeira etapa de Mensagem que segue uma jornada de ação, você pode usar propriedades de evento relacionadas ao evento referenciado nessa jornada de ação. No entanto, essas propriedades de evento só podem ser usadas se o usuário realmente realizou a ação (e não foi classificado no grupo Restante do público). Você pode ter outras etapas (que não sejam outra etapa de jornadas de ação ou de Mensagem) entre essa jornada de ação e a etapa de Mensagem.

{% details Expandir para o editor original do Canvas %}

Não é mais possível criar ou duplicar Canvas usando o editor original. Esta seção está disponível apenas para referência. Para o editor original do Canvas, propriedades de evento não podem ser usadas em etapas completas agendadas. No entanto, você pode usar propriedades de evento na primeira etapa completa de um Canvas baseado em ação, mesmo que a etapa completa esteja agendada.

{% enddetails %}

{% endtab %}
{% endtabs %}

Consulte [Propriedades de entrada do Canvas e propriedades de evento]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) para saber mais e ver exemplos.