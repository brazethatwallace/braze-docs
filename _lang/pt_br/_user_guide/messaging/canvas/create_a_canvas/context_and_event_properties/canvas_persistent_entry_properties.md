---
nav_title: Propriedades de entrada persistentes
article_title: Propriedades de entrada persistentes
alias: "/persistent_entry/"
page_type: reference
description: "Este artigo de referência descreve como usar propriedades de entrada persistentes no seu Canvas para enviar mensagens mais curadas e criar uma experiência refinada para o usuário final."
tool: Canvas
page_order: 5
---

# Propriedades de entrada persistentes {#persistent-entry-properties}

> Quando um Canvas é disparado por um evento personalizado, uma compra ou uma chamada de API or interface de programação do aplicativo (API), você pode usar metadados da chamada de API or interface de programação do aplicativo (API), do evento personalizado ou do evento de compra para personalização em cada etapa do fluxo de trabalho do seu Canvas. Você pode usar essas propriedades para enviar mensagens mais curadas.

{% alert important %}
As propriedades de entrada persistentes são um artefato do editor original do Canvas, então existem referências depreciadas a termos como propriedades de entrada do Canvas que permanecem para referência histórica. Para o editor atual do Canvas, consulte [Propriedades de contexto e evento]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties).<br><br>Para usar propriedades de entrada persistentes no editor atual do Canvas, você deve criar um novo Canvas ou [clonar]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases) um existente para o editor atual.
{% endalert %}

## Usando propriedades de entrada {#using-entry-properties}

As propriedades de entrada podem ser usadas em Canvas baseados em ação e disparados por API or interface de programação do aplicativo (API). Essas propriedades de entrada são definidas quando um Canvas é disparado por um evento personalizado, compra ou chamada de API or interface de programação do aplicativo (API). Consulte os seguintes artigos para saber mais:

- [Objeto de propriedades de entrada do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)
- [Objeto de propriedades de evento]({{site.baseurl}}/api/objects_filters/event_object)
- [Objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object#purchase-product-id)

As propriedades passadas a partir desses objetos podem ser referenciadas usando a Liquid tag `canvas_entry_properties`. Por exemplo, uma solicitação com `"canvas_entry_properties": {"product_name": "shoes", "product_price": 79.99}` poderia adicionar a palavra "shoes" a uma mensagem adicionando o Liquid {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}.

Quando um Canvas inclui uma mensagem com a Liquid tag `canvas_entry_properties`, os valores associados a essas propriedades serão salvos durante toda a jornada do usuário no Canvas e excluídos quando o usuário sair do Canvas. As propriedades de entrada do Canvas estão disponíveis apenas para referência em Liquid. Para filtrar pelas propriedades dentro do Canvas, use a [segmentação por propriedade de evento]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

{% alert note %}
O objeto de propriedades de entrada do Canvas tem um limite máximo de tamanho de 50 KB.
{% endalert %}

## Atualizando o Canvas para usar propriedades de entrada {#updating-canvas-to-use-entry-properties}

Se um Canvas ativo que anteriormente não incluía nenhuma mensagem usando `canvas_entry_properties` for editado para incluir `canvas_entry_properties`, o valor correspondente a essa propriedade não estará disponível para usuários que entraram no Canvas antes de `canvas_entry_properties` ser adicionado. Os valores serão salvos apenas para usuários que entrarem no Canvas após a alteração ser feita.

Por exemplo, se você lançou inicialmente um Canvas que não usava nenhuma propriedade de entrada em 3 de novembro e depois adicionou uma nova propriedade `product_name` ao Canvas em 11 de novembro, os valores de `product_name` seriam salvos apenas para usuários que entraram no Canvas a partir de 11 de novembro.

Caso uma propriedade de entrada do Canvas seja nula ou esteja em branco, você pode interromper mensagens usando condicionais. O snippet de código a seguir é um exemplo de como usar Liquid para interromper uma mensagem.
{%raw%}
```
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}
```
{%endraw%}

Para saber mais sobre a interrupção de mensagens com Liquid, confira nossa [documentação sobre Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).

## Propriedades globais de entrada do Canvas {#global-canvas-entry-properties}

Com `canvas_entry_properties`, você pode definir propriedades globais que se aplicam a todos os usuários ou propriedades específicas do usuário que se aplicam apenas ao usuário especificado. A propriedade específica do usuário substituirá a propriedade global para esse usuário.

### Exemplo de solicitação {#example-request}

```bash
curl -X POST \
-H 'Content-Type: application/json' \
-d '{
      "api_key": "a valid rest api key",
      "canvas_id": "the ID of your Canvas",
      "canvas_entry_properties": {
        "food_allergies": "none"
      },
      "recipients": [
        {
          "external_user_id": "Customer_123",
          "canvas_entry_properties": {
            "food_allergies": ["dairy", "soy"],
            "nutrition": {
              "calories_per_serving": 200,
              "serving_size_in_ounces": 4
            }
          }
        }
      ]
    }'
```

Nessa solicitação, o valor global para "food allergies" é "none". Para Customer_123, o valor é "dairy". As mensagens nesse Canvas que contêm o Liquid snippet {%raw%}`{{canvas_entry_properties.${food_allergies}}}`{%endraw%} serão renderizadas com "dairy" para Customer_123 e "none" para todos os demais.

## Caso de uso {#use-case}

Se você tem um Canvas que é disparado quando um usuário navega por um item no seu site de eCommerce, mas não o adiciona ao carrinho, a primeira etapa do Canvas pode ser uma notificação por push perguntando se ele tem interesse em comprar o item. Você pode referenciar o nome do produto usando {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}

![Se você tem um Canvas que é disparado quando um usuário navega por um item no seu site de eCommerce, mas não o adiciona ao carrinho, a primeira etapa do Canvas pode ser uma notificação por push perguntando se ele tem interesse em comprar o item. Você pode referenciar o nome do produto usando {% raw %}{{canvas_entry_properties.${product_name}}}{% endraw %}.]({% image_buster /assets/img/persistent_entry_properties/PEP1.png %}){: style="border:0;margin-left:15px;"}

A segunda etapa pode enviar outra notificação por push incentivando o usuário a finalizar a compra caso ele tenha adicionado o item ao carrinho, mas ainda não tenha concluído a compra. Você pode continuar referenciando a propriedade de entrada `product_name` usando {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}.

![Captura de tela relacionada ao caso de uso.]({% image_buster /assets/img/persistent_entry_properties/PEP12.png %}){: style="border:0;margin-left:15px;"}

## Solução de problemas {#troubleshooting}

### Propriedades de entrada estão em branco com múltiplos disparadores de entrada {#entry-properties-are-blank-with-multiple-entry-triggers}

A Braze armazena `canvas_entry_properties` do disparador que inseriu o usuário, e não de todos os disparadores configurados no Canvas. Se esse disparador não tiver evento ou carga útil de API or interface de programação do aplicativo (API) — por exemplo, **Start Session** ou **Change Custom Attribute Value** — o Liquid `canvas_entry_properties` ficará em branco para essa jornada. Usuários que entram no mesmo Canvas por meio de um evento personalizado, compra ou chamada de API or interface de programação do aplicativo (API) ainda terão as propriedades dessa carga útil.

Para manter as propriedades de entrada preenchidas para todos os usuários, use apenas tipos de entrada que transmitam essas propriedades (evento personalizado, compra ou disparo via API or interface de programação do aplicativo (API)). Para personalização no editor atual do Canvas, use [propriedades de contexto e evento]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties). Para filtrar por propriedades, use a [segmentação por propriedades de evento]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects) em vez do Liquid `canvas_entry_properties`.