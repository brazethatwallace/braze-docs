---
nav_title: Atualização de usuário
article_title: Atualização de usuário
alias: "/user_update/"
page_order: 12
page_type: reference
description: "Este artigo de referência aborda o componente Atualização de usuário e como usá-lo nos seus Canvas."
tool: Canvas
---

# Atualização de usuário {#user-update}

> O componente Atualização de usuário permite atualizar atributos, eventos e compras de um usuário em um editor JSON, sem a necessidade de incluir informações sensíveis como chaves de API or interface de programação do aplicativo (API).

## Como esse componente funciona {#how-this-component-works}

![Uma etapa de Atualização de Usuário chamada "Update loyalty" que atualiza um atributo "Is Premium Member" para "true".]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Ao usar esse componente no seu Canvas, as atualizações não contam para o limite de frequência de solicitações por minuto de `/users/track`. Em vez disso, essas atualizações são agrupadas em lotes para que a Braze possa processá-las de forma mais eficiente do que um webhook Braze-para-Braze. Esse componente não registra [pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points) quando usado para atualizar pontos de dados não faturáveis (como grupos de inscrições).

Depois que os usuários entram na etapa de Atualização de Usuário e o processamento é concluído, eles avançam para a próxima etapa. Isso significa que qualquer envio de mensagens subsequente que dependa dessas atualizações de usuário estará atualizado quando a próxima etapa for executada.

## Criando uma atualização de usuário {#creating-a-user-update}

Arraste e solte o componente da barra lateral, ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior da variante ou etapa e selecione **User Update**.

Existem três opções que permitem atualizar informações existentes do perfil de usuário, adicionar novas informações ou remover informações do perfil de usuário. No total, as etapas de User Update em um espaço de trabalho podem atualizar até 200.000 perfis de usuário por minuto.

{% alert tip %}
Você também pode testar as alterações feitas com este componente pesquisando um usuário e aplicando a alteração a ele. Isso atualizará o usuário.
{% endalert %}

## Atualização de atributos personalizados {#updating-custom-attributes}

Para atualizar ou remover um atributo personalizado, selecione o nome de um atributo na sua lista de atributos e insira o valor.

![Etapa de Atualização de Usuário que atualiza os dois atributos "Loyalty Member" e "Loyalty Program" para "true".]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

## Removendo atributos personalizados {#removing-custom-attributes}

Para remover um atributo personalizado, selecione o nome de um atributo usando o menu suspenso. Você pode alternar para o [editor JSON avançado](#advanced-json-editor) para editar ainda mais.

![Etapa de Atualização do Usuário que remove um atributo "Loyalty Member".]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### Aumentando e diminuindo valores {#increasing-and-decreasing-values}

A etapa de Atualização do Usuário pode aumentar ou diminuir o valor de um atributo. Selecione o atributo, selecione **Increment By** ou **Decrement By** e insira um número.

#### Acompanhar o progresso semanal {#track-weekly-progress}

Ao incrementar um atributo personalizado que rastreia um evento, você pode acompanhar o número de aulas que um usuário concluiu em uma semana. Usando esse componente, a contagem de aulas pode ser redefinida no início da semana e começar a rastrear novamente.

![Etapa de Atualização do Usuário que incrementa o atributo "class_count" em um.]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### Atualizando um array de objetos {#updating-an-array-of-objects}

Um [array de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects) é um atributo personalizado rico em dados armazenado no perfil de um usuário. Você pode usá-lo para criar um histórico das interações do usuário com a sua marca e para criar segmentos com base em um campo calculado, como histórico de compras ou valor do tempo de vida total.

Usando a opção **Advanced JSON Editor**, você pode inserir JSON para adicionar ou remover itens desse array de objetos.

#### Caso de uso: Atualizando a lista de desejos de um usuário {#use-case-updating-a-users-wishlist}

Acompanhe a lista de desejos de um usuário para segmentar ou personalizar com base nos itens salvos.

1. Crie um atributo personalizado que seja um array de objetos, por exemplo, `wishlist`. Cada objeto pode incluir campos como `product_id`, `product_name` e `added_at`.
2. Na etapa de Atualização do Usuário, selecione **Advanced JSON Editor**. Em seguida, na seção **Compose**, use a operação `$add` para adicionar um item ou a operação `$remove` para remover um item pelo valor.

A seguir, um exemplo de adição de um item à lista de desejos:

{% raw %}
```json
{
  "attributes": [
    {
      "wishlist": {
        "$add": [
          {
            "product_id": "SKU-123",
            "product_name": "Wireless Headphones",
            "added_at": "{{$isoTimestamp}}"
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

Para remover um item, use `"wishlist": { "$remove": [ { "product_id": "SKU-123", ... } ] }` com a mesma estrutura de objeto para que a Braze possa encontrá-lo e removê-lo.

#### Caso de uso: Calculando o total do carrinho de compras {#use-case-calculating-the-shopping-cart-total}

Acompanhe quando um usuário tem itens no carrinho de compras, quando adiciona ou remove itens e qual é o valor total do carrinho.

1. Crie um array de objetos personalizado chamado `shopping_cart`. O exemplo a seguir mostra como esse atributo pode ficar. Cada item tem um `product_id` único que possui dados adicionais em seu próprio array de objetos aninhado, incluindo `price`.

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": number,
         "shipping": number,
         "items_in_cart": number,
         "product_id": array,
         "gift": boolean,
         "discount_code": "enum",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

{:start="2"}
2. Crie um [evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events) chamado `add_item_to_cart` que é registrado quando um usuário adiciona um item ao carrinho.
3. Crie um Canvas direcionado aos usuários que realizam esse evento personalizado. Agora, quando um usuário adicionar um item ao carrinho, esse Canvas será disparado. Você pode então direcionar mensagens diretamente a esse usuário, oferecendo códigos de cupom quando ele atingir um determinado valor de gastos, abandonar o carrinho por um determinado período de tempo ou qualquer outra ação que esteja alinhada ao seu caso de uso.

O atributo `shopping_cart` carrega o total de vários eventos personalizados: o custo total de todos os itens, o número total de itens no carrinho, se o carrinho contém um presente e assim por diante. Isso pode ter a seguinte aparência:

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": 22.99,
         "shipping": 4.99,
         "items_in_cart": 2,
         "product_id": ["1001", "1002"],
         "gift": true,
         "discount_code": "flashsale1000",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

## Definindo a propriedade de entrada do Canvas como um atributo {#setting-canvas-entry-property-as-an-attribute}

Você pode usar a etapa de atualização do usuário para persistir uma `canvas_entry_property`. Digamos que você tenha um evento que é disparado quando um item é adicionado ao carrinho. Você pode armazenar o ID do item mais recente adicionado ao carrinho e usá-lo para uma campanha de remarketing. Use o recurso de personalização para recuperar uma propriedade de entrada do Canvas e armazená-la em um atributo.

![Etapa de atualização do usuário que atualiza o atributo "most_recent_cart_item" com um ID de item.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

### Personalização {#personalization}

Para armazenar a propriedade do evento-gatilho de um Canvas como um atributo, use o modal de personalização para extrair e armazenar a propriedade de entrada do Canvas. A etapa de atualização do usuário também oferece suporte aos seguintes recursos de personalização:

* [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
* [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
* [Propriedades de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties)
* Lógica Liquid (incluindo [interrupção de mensagens]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages))
* Múltiplas atualizações de atributos ou eventos por objeto

{% alert warning %}
Recomendamos o uso cuidadoso da personalização Liquid com Connected Content nas etapas de atualização do usuário, pois esse tipo de etapa tem um limite de frequência de 200.000 solicitações por minuto. Esse limite de frequência substitui o limite de frequência do Canvas.
{% endalert %}

## Editor JSON avançado {#advanced-json-editor}

Adicione um objeto JSON de atributo, evento ou compra de até 65.536 caracteres ao editor JSON. O [estado de inscrição global]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) e o estado do [grupo de inscrições]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups) de um usuário também podem ser definidos.

![Adicione um objeto JSON de atributo, evento ou compra de até 65.536 caracteres ao editor JSON. O estado de inscrição global e o estado do grupo de inscrições de um usuário também podem ser definidos.]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

Usando o editor JSON, você também pode pré-visualizar e testar se o perfil de usuário foi atualizado com suas alterações na guia **Prévia e teste**. Você pode selecionar um usuário aleatório ou buscar um usuário específico. Depois de enviar um teste para um usuário, visualize o perfil de usuário usando o link gerado.

![Usando o editor JSON, você também pode pré-visualizar e testar se o perfil de usuário foi atualizado com suas alterações na guia Prévia e teste. Você pode selecionar um usuário aleatório ou buscar um usuário específico. Depois de enviar um teste para um usuário, visualize o perfil de usuário usando o link gerado.]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### Considerações {#considerations}

Você não precisa incluir dados sensíveis, como sua chave de API or interface de programação do aplicativo (API), ao usar o editor JSON, pois isso é fornecido automaticamente pela plataforma. Os campos a seguir não devem ser incluídos no editor JSON:
* ID de usuário externo
* Chave de API or interface de programação do aplicativo (API)
* URL do cluster da Braze
* Campos relacionados à importação de tokens por push

{% alert important %}
As propriedades do Canvas (como as Liquid tags `canvas_id`, `canvas_name` e `canvas_variant_name`) não são compatíveis com etapas de Atualização do Usuário.
{% endalert %}

{% raw %}
### Registrar eventos personalizados {#log-custom-events}

Usando o editor JSON, você também pode registrar eventos personalizados. Isso requer um timestamp no formato ISO, então é necessário atribuir uma data e hora com Liquid no início. Considere este exemplo que registra um evento com um horário.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "name": "logged_user_event",
      "time": "{{timestamp}}"
    }
  ]
}
```

Este próximo exemplo vincula um evento a um app específico usando um evento personalizado com propriedades opcionais e o `app_id`.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "app_id": "insert_app_id",
      "name": "rented_movie",
      "time": "{{timestamp}}",
      "properties": {
        "release": {
          "studio": "FilmStudio",
          "year": "2022"
        },
        "cast": [
          {
            "name": "Actor1"
          },
          {
            "name": "Actor2"
          }
        ]
      }
    }
  ]
}
```

### Editar estado de inscrição {#edit-subscription-state}

No editor JSON, você também pode editar o estado de inscrição de um usuário. Por exemplo, o trecho a seguir mostra o estado de inscrição de um usuário atualizado para `opted_in`.

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### Atualizar grupos de inscrições {#update-subscription-groups}

Você também pode atualizar grupos de inscrições usando esta etapa do Canvas. O exemplo a seguir mostra como atualizar um ou mais grupos de inscrições.

```
{
  "attributes": [
    {
      "subscription_groups": [
        {
          "subscription_group_id": "subscription_group_identifier_1",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_2",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}
```
{% endraw %}