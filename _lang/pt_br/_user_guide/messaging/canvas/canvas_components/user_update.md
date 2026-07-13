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

> O componente Atualização de usuário permite atualizar atributos, eventos e compras de um usuário em um editor JSON, sem a necessidade de incluir informações sensíveis como chaves de API.

## Como este componente funciona {#how-this-component-works}

![Uma etapa de Atualização de usuário chamada "Update loyalty" que atualiza o atributo "Is Premium Member" para "true".]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Ao usar este componente no seu Canvas, as atualizações não contam para o limite de taxa de solicitações por minuto do `/users/track`. Em vez disso, essas atualizações são agrupadas em lotes para que a Braze possa processá-las de forma mais eficiente do que um webhook Braze-para-Braze. Observe que este componente não registra [pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points) quando usado para atualizar pontos de dados não faturáveis (como grupos de inscrições).

Depois que os usuários entram na etapa de Atualização de usuário e o processamento é concluído, eles avançam para a próxima etapa. Isso significa que qualquer envio de mensagens subsequente que dependa dessas atualizações estará atualizado quando a próxima etapa for executada.

## Criando uma atualização de usuário {#creating-a-user-update}

Arraste e solte o componente da barra lateral, ou selecione o botão de mais <i class="fas fa-plus-circle"></i> na parte inferior da variante ou etapa e selecione **User Update**.

Existem três opções que permitem atualizar informações existentes do perfil de usuário, adicionar novas informações ou remover informações do perfil de usuário. Combinadas, as etapas de Atualização de usuário em um espaço de trabalho podem atualizar até 200.000 perfis de usuário por minuto.

{% alert tip %}
Você também pode testar as alterações feitas com este componente pesquisando um usuário e aplicando a alteração a ele. Isso atualizará o usuário.
{% endalert %}

## Atualizando atributos personalizados {#updating-custom-attributes}

Para atualizar ou remover um atributo personalizado, selecione um nome de atributo na sua lista de atributos e insira o valor.

![Etapa de Atualização de usuário que atualiza os dois atributos "Loyalty Member" e "Loyalty Program" para "true".]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

## Removendo atributos personalizados {#removing-custom-attributes}

Para remover um atributo personalizado, selecione um nome de atributo usando o menu suspenso. Você pode alternar para o [editor JSON avançado](#advanced-json-editor) para edições adicionais.

![Etapa de Atualização de usuário que remove o atributo "Loyalty Member".]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### Incrementando e decrementando valores {#increasing-and-decreasing-values}

A etapa de Atualização de usuário pode incrementar ou decrementar o valor de um atributo. Selecione o atributo, selecione **Increment By** ou **Decrement By** e insira um número.

#### Acompanhar o progresso semanal {#track-weekly-progress}

Ao incrementar um atributo personalizado que rastreia um evento, você pode acompanhar o número de aulas que um usuário fez em uma semana. Usando este componente, a contagem de aulas pode ser redefinida no início da semana e começar a rastrear novamente.

![Etapa de Atualização de usuário que incrementa o atributo "class_count" em um.]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### Atualizando um array de objetos {#updating-an-array-of-objects}

Um [array de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects) é um atributo personalizado rico em dados armazenado no perfil de um usuário. Você pode usá-lo para criar um histórico das interações do usuário com sua marca e para criar segmentos com base em um campo calculado, como histórico de compras ou lifetime value total.

Usando a opção **Advanced JSON Editor**, você pode inserir JSON para adicionar ou remover itens desse array de objetos.

#### Caso de uso: Atualizando a lista de desejos de um usuário {#use-case-updating-a-users-wishlist}

Acompanhe a lista de desejos de um usuário para que você possa segmentar ou personalizar com base nos itens salvos.

1. Crie um atributo personalizado que seja um array de objetos, por exemplo `wishlist`. Cada objeto pode incluir campos como `product_id`, `product_name` e `added_at`.
2. Na etapa de Atualização de usuário, selecione **Advanced JSON Editor**. Em seguida, na seção **Redigir**, use a operação `$add` para adicionar um item ou a operação `$remove` para remover um item por valor.

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

Para remover um item, use `"wishlist": { "$remove": [ { "product_id": "SKU-123", ... } ] }` com a mesma estrutura de objeto para que a Braze possa encontrar e removê-lo.

#### Caso de uso: Calculando o total do carrinho de compras {#use-case-calculating-the-shopping-cart-total}

Acompanhe quando um usuário tem itens no carrinho de compras, quando adiciona ou remove itens e qual é o valor total do carrinho.

1. Crie um array de objetos personalizado chamado `shopping_cart`. O exemplo a seguir mostra como esse atributo pode ser. Cada item tem um `product_id` único que possui dados adicionais em seu próprio array de objetos aninhado, incluindo `price`.

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
3. Crie um Canvas direcionado a usuários que realizam esse evento personalizado. Agora, quando um usuário adiciona um item ao carrinho, esse Canvas é disparado. Você pode então direcionar mensagens diretamente a esse usuário, oferecendo códigos de cupom quando ele atingir um determinado valor de gasto, abandonar o carrinho por um certo período de tempo ou qualquer outra ação que se alinhe ao seu caso de uso.

O atributo `shopping_cart` carrega o total de muitos eventos personalizados: o custo total de todos os itens, o número total de itens no carrinho, se o carrinho contém um presente, e assim por diante. Isso pode ser algo como o seguinte:

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

Você pode usar a etapa de Atualização de usuário para persistir uma `canvas_entry_property`. Digamos que você tenha um evento que é disparado quando um item é adicionado ao carrinho. Você pode armazenar o ID do item mais recente adicionado ao carrinho e usá-lo para uma campanha de remarketing. Use o recurso de personalização para recuperar uma propriedade de entrada do Canvas e armazená-la em um atributo.

![Etapa de Atualização de usuário que atualiza o atributo "most_recent_cart_item" com um ID de item.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

### Personalização {#personalization}

Para armazenar a propriedade do evento de gatilho de um Canvas como um atributo, use o modal de personalização para extrair e armazenar a propriedade de entrada do Canvas. A Atualização de usuário também suporta os seguintes recursos de personalização:

* [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
* [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
* [Propriedades de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties)
* Lógica Liquid (incluindo [cancelamento de mensagens]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages))
* Múltiplas atualizações de atributos ou eventos por objeto

{% alert warning %}
Recomendamos cautela ao usar personalização Liquid com Conteúdo conectado nas etapas de Atualização de usuário, pois esse tipo de etapa tem um limite de taxa de 200.000 solicitações por minuto. Esse limite de taxa substitui o limite de taxa do Canvas.
{% endalert %}

## Editor JSON avançado {#advanced-json-editor}

Adicione um objeto JSON de atributo, evento ou compra com até 65.536 caracteres ao editor JSON. O [estado de inscrição global]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) e o estado do [grupo de inscrições]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups) de um usuário também podem ser definidos.

![Adicione um objeto JSON de atributo, evento ou compra com até 65.536 caracteres ao editor JSON. O estado de inscrição global e o estado do grupo de inscrições de um usuário também podem ser definidos.]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

Usando o editor JSON, você também pode pré-visualizar e testar se o perfil do usuário é atualizado com suas alterações na guia **Preview and test**. Você pode selecionar um usuário aleatório ou pesquisar um usuário específico. Depois de enviar um teste para um usuário, visualize o perfil do usuário usando o link gerado.

![Usando o editor JSON, você também pode pré-visualizar e testar se o perfil do usuário é atualizado com suas alterações na guia Preview and test. Você pode selecionar um usuário aleatório ou pesquisar um usuário específico. Depois de enviar um teste para um usuário, visualize o perfil do usuário usando o link gerado.]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### Considerações {#considerations}

Você não precisa incluir dados sensíveis como sua chave de API ao usar o editor JSON, pois isso é fornecido automaticamente pela plataforma. Os seguintes campos não devem ser incluídos no editor JSON:
* ID de usuário externo
* Chave de API
* URL do cluster da Braze
* Campos relacionados a importações de token por push

{% alert important %}
As propriedades do Canvas (como as Liquid tags `canvas_id`, `canvas_name` e `canvas_variant_name`) não são suportadas nas etapas de Atualização de usuário.
{% endalert %}

{% raw %}
### Registrar eventos personalizados {#log-custom-events}

Usando o editor JSON, você também pode registrar eventos personalizados. Observe que isso requer um timestamp no formato ISO, então é necessário atribuir uma data e hora com Liquid no início. Considere este exemplo que registra um evento com um horário.

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

O próximo exemplo vincula um evento a um app específico usando um evento personalizado com propriedades opcionais e o `app_id`.

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

No editor JSON, você também pode editar o estado de inscrição de um usuário. Por exemplo, o seguinte mostra o estado de inscrição de um usuário atualizado para `opted_in`.

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