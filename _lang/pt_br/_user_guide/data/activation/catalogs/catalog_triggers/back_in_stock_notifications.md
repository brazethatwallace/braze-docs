---
nav_title: Notificações de reposição de estoque
article_title: Configurar notificações de reposição de estoque
page_order: 2
description: "Aprenda a configurar notificações de reposição de estoque usando seu catálogo e eventos personalizados, para que você possa inscrever automaticamente os clientes para receber notificações quando um item estiver de volta ao estoque."
---

# Notificações de reposição de estoque {#back-in-stock-notifications}

> Aprenda a configurar notificações de reposição de estoque usando seu catálogo e eventos personalizados, para que você possa inscrever automaticamente os clientes para receber notificações quando um item estiver de volta ao estoque. Lembre-se de que isso se aplica apenas a usuários que já optaram por receber notificações.

## Como funciona {#how-it-works}

Você pode configurar um evento personalizado para usar como evento de inscrição, como um evento `product_clicked`. Esse evento deve conter uma propriedade com o ID do item (IDs de itens do catálogo). Sugerimos que você inclua um nome de catálogo, mas isso não é obrigatório. Você também fornecerá o nome de um campo de quantidade em estoque, que deve ser do tipo numérico.

O estoque de um item do catálogo deve estar em zero para que um usuário consiga se inscrever com sucesso. Quando um item tem uma quantidade em estoque maior que zero, a Braze procurará todos os usuários inscritos naquele item e enviará um evento personalizado que você pode usar para disparar uma Campaign ou Canvas.

As propriedades do evento são enviadas junto com o usuário, para que você possa incluir os detalhes do item na Campaign ou Canvas que faz o envio.

## Configurando notificações de reposição de estoque {#setting-up-back-in-stock-notifications}

Siga estas etapas para configurar notificações de reposição de estoque em um catálogo específico.

1. Acesse seu catálogo e selecione a guia **Settings**.
2. Selecione a opção **Back in stock**.
3. Se as configurações globais de reposição de estoque não tiverem sido definidas, será solicitado que você configure os eventos e propriedades personalizados que serão usados para disparar notificações de reposição de estoque:
    <br> ![Gaveta de configurações do catálogo.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}
    - **Fallback Catalog** é o catálogo que será usado para a inscrição de reposição de estoque, caso não haja uma propriedade `catalog_name` presente no evento personalizado.
    - **Custom event for subscriptions** é o evento personalizado da Braze que será usado para inscrever um usuário nas notificações de reposição de estoque. Quando esse evento ocorrer, o usuário que o realizou será inscrito.
    - **Custom event for unsubscribing** é o evento personalizado da Braze que será usado para cancelar a inscrição de um usuário nas notificações de reposição de estoque. Esse evento é opcional. Se o usuário não realizar esse evento, sua inscrição será cancelada após 90 dias ou quando o evento de reposição de estoque for disparado, o que ocorrer primeiro.
    - **Item ID event property** é a propriedade do evento personalizado acima que será usada para determinar o item para uma inscrição ou cancelamento de inscrição de reposição de estoque. Essa propriedade no evento personalizado deve conter um ID de item (`id`) que esteja presente em um catálogo. O ID do item deve ser enviado como uma string para que corresponda ao tipo de dado `id` armazenado no catálogo de destino. O evento personalizado também deve conter uma propriedade `catalog_name` para especificar em qual catálogo esse item está.

    - Um exemplo de evento personalizado seria:

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

{% alert note %}
Os gatilhos de reposição de estoque e queda de preço usam o mesmo evento para inscrever o usuário na notificação. Portanto, você pode usar a propriedade `type` para definir tanto as notificações de queda de preço quanto as de reposição de estoque no mesmo evento. Observe que a propriedade `type` deve ser um array.
{% endalert %}

{: start="4"}
4. Selecione **Save** e continue para a página de **Settings** do catálogo.
5. Defina sua regra de notificação. Existem duas opções:
    - **Notify all subscribed users** notifica todos os clientes que estão aguardando quando o item estiver novamente em estoque.
    - **Set notification limits** notifica um número específico de clientes a cada 10 minutos. A Braze notificará o número especificado de clientes em incrementos até que não haja mais clientes para notificar ou até que o item fique fora de estoque. Sua taxa de notificação não pode exceder 10.000 usuários por minuto.
6. Defina o **Inventory field in catalog**. Esse campo do catálogo será usado para determinar se o item está fora de estoque. O campo deve ser do tipo numérico.
7. Selecione **Save settings**.

![Configurações do catálogo que mostram o recurso de reposição de estoque ativado. As regras de notificação são para notificar mil usuários a cada dez minutos.]({% image_buster /assets/img/back_in_stock_settings.png %})

{% alert important %}
As regras de notificação nestas configurações não substituem as configurações de notificação do Canvas, como o horário de silêncio.
{% endalert %}

## Usando notificações de reposição de estoque em um Canvas {#using-back-in-stock-notifications-in-a-canvas}

Após configurar o recurso de reposição de estoque em um catálogo, siga estas etapas para usá-lo com o Canvas.

1. Configure um Canvas baseado em ação.
2. Selecione **Back in stock** como o gatilho.
3. Selecione o nome do catálogo com as notificações de reposição de estoque.
4. Continue [configurando]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) seu Canvas como de costume.

Agora, seus clientes podem ser notificados quando um item estiver novamente em estoque.

### Usando Liquid {#using-liquid}

Para incluir detalhes sobre o item do catálogo que voltou ao estoque, use a Liquid tag `context` para acessar o `item_id`.

O uso de {%raw%}``{{context.${catalog_update}.item_id}}``{%endraw%} retornará o ID do item que voltou ao estoque. {%raw%}``{{context.${catalog_update}.previous_value}}``{%endraw%} retornará o valor do estoque do item antes da atualização, e {%raw%}``{{context.${catalog_update}.new_value}}``{%endraw%} retornará o novo valor do estoque após a atualização.

Use a Liquid tag {%raw%}``{% catalog_items <name_of_your_catalog> {{context.${catalog_update}.item_id}} %}``{%endraw%} no topo da sua mensagem e depois use {%raw%}``{{ items[0].<field_name> }}``{%endraw%} para acessar dados sobre esse item ao longo da mensagem.

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}

## Considerações {#considerations}

- Os usuários ficam inscritos por apenas 90 dias. Se o item não voltar ao estoque em 90 dias, o usuário terá sua inscrição cancelada.
- Ao usar a regra de notificação **Notify all subscribed users**, a Braze notificará 100.000 usuários em 10 minutos.
- A Braze suporta até 50.000 itens atualizados diariamente que são elegíveis para disparar notificações de reposição de estoque. Você pode ter até 100 milhões de inscrições ativas ao mesmo tempo, onde cada inscrição representa um perfil de usuário inscrito para acompanhar um item do catálogo.