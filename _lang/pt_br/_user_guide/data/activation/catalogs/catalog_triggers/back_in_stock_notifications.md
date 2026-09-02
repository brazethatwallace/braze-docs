---
nav_title: Notificações de reposição de estoque
article_title: Configurar notificações de reposição de estoque
page_order: 2
description: "Aprenda a configurar notificações de reposição de estoque usando seu catálogo e eventos personalizados, para que você possa inscrever automaticamente os clientes para receber notificações quando um item estiver de volta ao estoque."
---

# Notificações de reposição de estoque {#back-in-stock-notifications}

> Aprenda a configurar notificações de reposição de estoque usando seu catálogo e eventos personalizados, para que você possa inscrever automaticamente os clientes para receber notificações quando um item estiver de volta ao estoque. Lembre-se de que isso se aplica apenas a usuários que já optaram por receber notificações.

## Como funciona {#how-it-works}

Você pode configurar um evento personalizado para usar como evento de inscrição, como um evento `product_clicked`. Esse evento deve conter uma propriedade com o ID do item (IDs de itens do catálogo). Sugerimos que você inclua o nome do catálogo, mas isso não é obrigatório. Você também fornecerá o nome de um campo de quantidade em estoque, que deve ser do tipo de dados numérico.

Note que o estoque de um item do catálogo deve estar zerado para que um usuário consiga se inscrever nele com sucesso. Quando um item tem uma quantidade em estoque maior que zero, a Braze buscará todos os usuários inscritos naquele item e enviará um evento personalizado que você pode usar para disparar uma Campaign ou um Canvas.

As propriedades do evento são enviadas junto com o usuário, então você pode usar templates com os detalhes do item na Campaign ou no Canvas que faz o envio.

## Configurando notificações de volta ao estoque {#setting-up-back-in-stock-notifications}

Siga estas etapas para configurar notificações de volta ao estoque em um catálogo específico.

1. Acesse seu catálogo e selecione a guia **Settings**.
2. Selecione o toggle **Back in stock**.
3. Se as configurações globais de volta ao estoque não tiverem sido definidas, você será solicitado a configurar os eventos personalizados e as propriedades que serão usados para disparar notificações de volta ao estoque:
    <br> ![Gaveta de configurações do catálogo.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}
    - **Fallback Catalog** é o catálogo que será usado para a inscrição de volta ao estoque, caso não haja uma propriedade `catalog_name` presente no evento personalizado.
    - **Custom event for subscriptions** é o evento personalizado da Braze que será usado para inscrever um usuário nas notificações de volta ao estoque. Quando esse evento ocorrer, o usuário que realizou o evento será inscrito.
    - **Custom event for unsubscribing** é o evento personalizado da Braze que será usado para cancelar a inscrição de um usuário nas notificações de volta ao estoque. Esse evento é opcional. Se o usuário não realizar esse evento, a inscrição será cancelada após 90 dias ou quando o evento de volta ao estoque for disparado, o que ocorrer primeiro.
    - **Item ID event property** é a propriedade no evento personalizado mencionado anteriormente nesta seção que será usada para determinar o item para uma inscrição ou cancelamento de inscrição de volta ao estoque. Essa propriedade no evento personalizado deve conter um ID de item (`id`) que esteja presente em um catálogo. O ID do item deve ser enviado como uma string para que corresponda ao tipo de dados `id` armazenado no catálogo de destino. O evento personalizado também deve conter uma propriedade `catalog_name` para especificar em qual catálogo esse item está.

    - O exemplo a seguir mostra um evento personalizado de amostra enviado pela REST or transferir estado representacional API or interface de programação do aplicativo (API):

```json
{
    "events": [
        {
            "external_id": "<external_id>",
            "name": "subscription",
            "time": "2024-04-15T19:22:28Z",
            "properties": {
                "id": "shirt-xl",
                "catalog_name": "on_sale_products",
                "type": ["back_in_stock"]
            }
        }
    ]
}
```

Para rastrear o mesmo evento de inscrição usando os SDKs da Braze, use o seguinte código:

{% tabs %}
{% tab Web SDK or kit de desenvolvimento de software %}

```javascript
import { logCustomEvent } from "@braze/web-sdk";

logCustomEvent("subscription", {
  id: "shirt-xl",
  catalog_name: "on_sale_products",
  type: ["back_in_stock"]
});
```

{% endtab %}
{% tab Swift %}

```swift
AppDelegate.braze?.logCustomEvent(
  name: "subscription",
  properties: [
    "id": "shirt-xl",
    "catalog_name": "on_sale_products",
    "type": ["back_in_stock"]
  ]
)
```

{% endtab %}
{% tab Android %}

```kotlin
Braze.getInstance(context).logCustomEvent(
  "subscription",
  BrazeProperties(
    JSONObject()
      .put("id", "shirt-xl")
      .put("catalog_name", "on_sale_products")
      .put("type", JSONArray().put("back_in_stock")),
  ),
)
```

{% endtab %}
{% endtabs %}

{% alert note %}
Os disparadores de volta ao estoque e de queda de preço usam o mesmo evento para inscrever o usuário na notificação, então você pode usar a propriedade `type` para definir notificações de queda de preço e de volta ao estoque no mesmo evento. Note que a propriedade `type` deve ser um array.
{% endalert %}

{: start="4"}
4. Selecione **Save** e continue para a página de **Settings** do catálogo.
5. Defina sua regra de notificação. Existem duas opções:
    - **Notify all subscribed users** notifica todos os clientes que estão aguardando quando o item volta ao estoque.
    - **Set notification limits** notifica um número especificado de clientes a cada 10 minutos. A Braze notificará o número especificado de clientes em incrementos até que não haja mais clientes para notificar ou até que o item fique fora de estoque. Sua taxa de notificação não pode exceder a notificação de 10.000 usuários por minuto.
6. Defina o **Inventory field in catalog**. Esse campo do catálogo será usado para determinar se o item está fora de estoque. O campo deve ser do tipo número.
7. Selecione **Save settings**.

![Configurações do catálogo mostrando o recurso de volta ao estoque ativado. As regras de notificação são para notificar mil usuários a cada dez minutos.]({% image_buster /assets/img/back_in_stock_settings.png %})

{% alert important %}
As regras de notificação nessas configurações não substituem as configurações de notificação do Canvas, como o horário de silêncio.
{% endalert %}

## Usando notificações de volta ao estoque em um Canvas {#using-back-in-stock-notifications-in-a-canvas}

Depois de configurar o recurso de volta ao estoque em um catálogo, siga estas etapas para usá-lo com o Canvas.

1. Configure um Canvas baseado em ação.
2. Selecione **Volta ao estoque** como o disparador.
3. Selecione o nome do catálogo com as notificações de volta ao estoque.
4. Continue [configurando]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) seu Canvas normalmente.

Agora, seus clientes podem ser notificados quando um item estiver de volta ao estoque.

### Usando Liquid {#using-liquid}

Para incluir detalhes sobre o item do catálogo que voltou ao estoque, você pode usar a Liquid tag `context` para acessar o `item_id`.

Usar {%raw%}``{{context.${catalog_update}.item_id}}``{%endraw%} retornará o ID do item que voltou ao estoque. {%raw%}``{{context.${catalog_update}.previous_value}}``{%endraw%} retornará o valor do inventário do item antes da atualização, e {%raw%}``{{context.${catalog_update}.new_value}}``{%endraw%} retornará o novo valor do inventário após a atualização.

Use a Liquid tag {%raw%}``{% catalog_items <name_of_your_catalog> {{context.${catalog_update}.item_id}} %}``{%endraw%} no topo da sua mensagem e, em seguida, use {%raw%}``{{ items[0].<field_name> }}``{%endraw%} para acessar dados sobre esse item ao longo da mensagem.

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}

## Considerações {#considerations}

- Os usuários ficam inscritos por apenas 90 dias. Se o item não voltar ao estoque em 90 dias, o usuário terá sua inscrição cancelada.
- Ao usar a regra de notificação **Notify all subscribed users**, a Braze notificará 100.000 usuários ao longo de 10 minutos.
- A Braze suporta até 50.000 itens atualizados diariamente que são elegíveis para disparar notificações de volta ao estoque. Você pode ter até 100 milhões de inscrições ativas em um determinado momento, onde cada inscrição representa um perfil de usuário inscrito para monitorar um item do catálogo.