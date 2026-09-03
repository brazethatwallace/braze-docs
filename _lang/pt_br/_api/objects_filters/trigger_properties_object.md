---
nav_title: "Objeto de propriedades do gatilho"
article_title: Objeto de propriedades do gatilho da API
page_order: 11
page_type: reference
description: "Este artigo de referência explica os diferentes componentes do objeto de propriedades do gatilho."
tool: Campaigns

---

# Objeto de propriedades do gatilho {#trigger-properties-object}

> Ao usar um dos endpoints para enviar uma Campaign com entrega disparada por API, você pode fornecer um mapa de chaves e valores para personalizar sua mensagem.

Se você fizer uma solicitação de API que contenha um objeto em `trigger_properties`, os valores desse objeto poderão ser referenciados no seu modelo de mensagem no namespace `api_trigger_properties`. Por exemplo, uma solicitação como a seguinte poderia adicionar a palavra `"shoes"` a uma mensagem, incluindo {% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %}.

Observe que, embora as propriedades de gatilho possam ser usadas como modelo em mensagens, elas não são armazenadas automaticamente no perfil do usuário por padrão.

{% alert note %}
O objeto `trigger_properties` e a sintaxe {% raw %}`api_trigger_properties.${product_name}`{% endraw %} são compatíveis apenas com Campaigns. Para personalizar mensagens com chaves e valores de uma solicitação de gatilho de API para o Canvas, use o [objeto de propriedades de entrada do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context). O objeto `trigger_properties` tem um limite máximo de tamanho de 50 KB.
{% endalert %}

## Corpo do objeto {#object-body}

O objeto `trigger_properties` suporta strings, números, booleanos, datas, objetos e arrays como tipos de dados.

```json
{
  "trigger_properties" : {
    "product_name" : "shoes",
    "product_price" : 79.99,
    "details" : {
      "color" : "red",
      "size" : {
        "numerical" : 10,
        "country" : "US"
      }
    },
    "related_skus": ["123", "456", "789"]
  }
}
```

## Exemplos de modelos Liquid {#liquid-templating-examples}

Faça referência às propriedades de disparo nos seus modelos de mensagem usando o namespace `api_trigger_properties`:

- Strings: {% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %} retorna `"shoes"`
- Números: {% raw %}`{{api_trigger_properties.${product_price}}}`{% endraw %} retorna `79.99`
- Objetos aninhados: {% raw %}`{{api_trigger_properties.${details}.${color}}}`{% endraw %} retorna `"red"`
- Elementos de array: {% raw %}`{{api_trigger_properties.${related_skus}[0]}}`{% endraw %} retorna `"123"`