---
nav_title: Vetor de objetos
article_title: Vetor de objetos
alias: "/array_of_objects/"
page_order: 2
page_type: reference
description: "Este artigo de referência aborda o uso de um vetor de objetos como um tipo de dados para atributos personalizados, incluindo limitações e exemplos de uso."
---

# Vetor de objetos {#array-of-objects}

> Esta página aborda como usar um vetor de objetos para agrupar atributos relacionados. Por exemplo, você pode ter um grupo de objetos de animais de estimação, objetos de música e objetos de conta que pertencem a um único usuário. Esses vetores de objetos podem ser usados para personalizar o envio de mensagens com Liquid ou criar segmentos de público se algum elemento de um objeto corresponder aos critérios.

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## Considerações {#considerations}

- Os vetores de objetos destinam-se a atributos personalizados enviados por meio da API. Não há suporte para upload de CSV. Isso ocorre porque as vírgulas no arquivo CSV serão interpretadas como separadores de coluna, e as vírgulas nos valores causarão erros de análise.
- Os vetores de objetos não têm limite para o número de itens, mas têm um tamanho máximo de 100&nbsp;KB. Se uma atualização (como `$add` ou `$update`) fizer o vetor exceder esse limite, a Braze descarta a atualização e o atributo permanece inalterado. A requisição da API ainda retorna uma resposta de sucesso. Para manter o vetor dentro do limite e permitir a adição de novos itens, use `$remove` para excluir itens do vetor primeiro.
- Nem todos os parceiros da Braze suportam vetores de objetos. Consulte a [documentação do parceiro]({{site.baseurl}}/partners/home) para confirmar se a integração suporta esse recurso.

A atualização ou remoção de itens em um vetor exige a identificação do item por chave e valor, portanto, considere incluir um identificador exclusivo para cada item do vetor. A exclusividade tem escopo apenas para o vetor e é útil se você quiser atualizar e remover objetos específicos do vetor. Isso não é imposto pela Braze.

{% alert important %}
Quando um atributo personalizado aninhado na sua requisição contém valores inválidos (como formatos de hora inválidos ou valores `null`), a Braze descarta todas as atualizações de atributos personalizados aninhados da requisição durante o processamento. Isso se aplica a todas as estruturas aninhadas dentro desse atributo específico. Verifique se todos os valores dentro dos atributos personalizados aninhados são válidos antes de enviar. Para saber mais, consulte [Criar e atualizar usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_track#how-does-userstrack-handle-invalid-nested-custom-attributes).
{% endalert %}

{% alert tip %}
Para saber mais sobre o uso de vetores de objetos para objetos de atributos de usuário, consulte [Objeto de atributos de usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object).
{% endalert %}

## Exemplo de API {#api-example}

Use estes exemplos ao enviar requisições `/users/track` que criam ou atualizam atributos personalizados aninhados armazenados como vetores de objetos. A carga útil usa os operadores `$add`, `$remove` e `$update` para que você possa alterar objetos específicos sem reconstruir o vetor inteiro a cada requisição.

{% tabs local %}
{% tab Criar %}

A seguir, um exemplo de `/users/track` com um vetor `pets`. Para capturar as propriedades dos animais de estimação, envie uma requisição de API que liste `pets` como um vetor de objetos. Observe que cada objeto recebeu um `id` único que pode ser referenciado posteriormente ao fazer atualizações.

Use este formato quando quiser criar o atributo pela primeira vez ou substituir o vetor inteiro por um novo conjunto base de objetos.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Mochi"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Pixel"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Adicionar %}

Adicione outro item ao vetor usando o operador `$add`. O exemplo a seguir mostra a adição de mais três objetos de animais de estimação ao vetor `pets` do usuário.

Use `$add` quando precisar anexar um ou mais novos objetos e manter os objetos existentes inalterados.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$add": [
          {
            "id": 3,
            "type": "dog",
            "breed": "corgi",
            "name": "Biscuit"
          },
          {
            "id": 4,
            "type": "fish",
            "breed": "salmon",
            "name": "Pepper"
          },
           {
            "id": 5,
            "type": "bird",
            "breed": "parakeet",
            "name": "Noodle"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Atualizar %}

Atualize valores de objetos específicos dentro de um vetor usando o parâmetro `_merge_objects` e o operador `$update`. Semelhante às atualizações de outros objetos de [atributos personalizados aninhados]({{site.baseurl}}/nested_custom_attribute_support#api-request-body), isso realiza um merge profundo.

Observe que `$update` não pode ser usado para remover uma propriedade aninhada de um objeto dentro de um vetor. Para isso, você precisará remover o item inteiro do vetor e depois adicionar o objeto sem essa chave específica (usando uma combinação de `$remove` e `$add`).

Use `$update` quando o objeto já existir e você quiser alterar um ou mais campos fazendo a correspondência por `$identifier_key` e `$identifier_value`.

O exemplo a seguir mostra a atualização da propriedade `breed` para `goldfish` no objeto com `id` igual a `4`. Este exemplo de requisição também atualiza o objeto com `id` igual a `5` com um novo `name` de `Annette`. Como o parâmetro `_merge_objects` está definido como `true`, todos os outros campos desses dois objetos permanecem inalterados.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```

{% alert warning %}
Você deve definir `_merge_objects` como true, caso contrário seus objetos serão sobrescritos. `_merge_objects` é false por padrão.
{% endalert %}

{% endtab %}
{% tab Remover %}

Remova objetos de um vetor usando o operador `$remove` em combinação com uma chave correspondente (`$identifier_key`) e valor (`$identifier_value`).

Use `$remove` quando quiser excluir todos os objetos correspondentes para um par de identificador conhecido, como `id = 2` ou `type = dog`.

O exemplo a seguir mostra a remoção de qualquer objeto no vetor `pets` que tenha um `id` com valor `1`, um `id` com valor `2` e um `type` com valor `dog`. Se houver múltiplos objetos com o valor de `type` igual a `dog`, todos os objetos correspondentes serão removidos.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

### Ordem de processamento {#processing-order}

Quando uma única requisição `/users/track` inclui operações `$add`, `$remove` e `$update` para o mesmo atributo de vetor, a Braze as processa nesta ordem:

1. `$add`
2. `$remove`
3. `$update`

Essa ordem se aplica dentro de um único objeto de atualização de atributo em uma requisição e determina o estado final do vetor após todas as operações serem avaliadas.

Como `$add` é executado antes de `$remove`, você não pode usar um `$remove` seguido de `$add` como mecanismo de upsert em uma única requisição. O `$add` é processado primeiro e, em seguida, o `$remove` exclui o item. Para fazer upsert, envie o `$remove` em uma requisição separada antes do `$add`.

### Timestamps {#timestamps}

Ao incluir campos como timestamps em um vetor de objetos, use o formato `$time` em vez de strings simples ou inteiros de época Unix.

```json
{
  "attributes": [
    {
      "external_id": "user123",
      "purchases": [
        {
          "item_name": "T-shirt",
          "price": 19.99,
          "purchase_time": {
            "$time": "2020-05-28"
          }
        }
      ]
    }
  ]
}
```

{% alert tip %}
Para saber mais, consulte [Atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).
{% endalert %}

## Exemplo de SDK {#sdk-example}

{% tabs local %}
{% tab Android SDK %}
{% subtabs %}
{% subtab Criar %}
```kotlin
val json = JSONArray()
    .put(JSONObject()
        .put("id", 1)
        .put("type", "dog")
        .put("breed", "beagle")
        .put("name", "Gus"))
    .put(JSONObject()
        .put("id", 2)
        .put("type", "cat")
        .put("breed", "calico")
        .put("name", "Pixel")
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json)
}
```
{% endsubtab %}

{% subtab Adicionar %}
```kotlin
val json = JSONObject()
    .put("\$add", JSONArray()
        .put(JSONObject()
            .put("id", 3)
            .put("type", "dog")
            .put("breed", "corgi")
            .put("name", "Doug"))
        .put(JSONObject()
            .put("id", 4)
            .put("type", "fish")
            .put("breed", "salmon")
            .put("name", "Pepper"))
        .put(JSONObject()
            .put("id", 5)
            .put("type", "bird")
            .put("breed", "parakeet")
            .put("name", "Noodle")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab Atualizar %}
```kotlin
val json = JSONObject()
    .put("\$update", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 4)
            .put("\$new_object", JSONObject()
                .put("breed", "goldfish")
            )
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 5)
            .put("\$new_object", JSONObject()
                .put("name", "Annette")
            )
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab Excluir %}
```kotlin
val json = JSONObject()
    .put("\$remove", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 1)
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 2)
        )
        .put(JSONObject()
            .put("\$identifier_key", "type")
            .put("\$identifier_value", "dog")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift SDK %}
{% subtabs %}
{% subtab Criar %}
```swift
let json: [[String: Any?]] = [
  [
    "id": 1,
    "type": "dog",
    "breed": "beagle",
    "name": "Mochi"
  ],
  [
    "id": 2,
    "type": "cat",
    "breed": "calico",
    "name": "Pixel"
  ]
]

braze.user.setCustomAttribute(key: "pets", array: json)
```
{% endsubtab %}

{% subtab Adicionar %}
```swift
let json: [String: Any?] = [
  "$add": [
    [
      "id": 3,
      "type": "dog",
      "breed": "corgi",
      "name": "Biscuit"
    ],
    [
      "id": 4,
      "type": "fish",
      "breed": "salmon",
      "name": "Pepper"
    ],
    [
      "id": 5,
      "type": "bird",
      "breed": "parakeet",
      "name": "Noodle"
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab Atualizar %}
```swift
let json: [String: Any?] = [
  "$update": [
    [
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": [
        "breed": "goldfish"
      ]
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": [
        "name": "Annette"
      ]
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab Excluir %}
```swift
let json: [String: Any?] = [
  "$remove": [
    [
      "$identifier_key": "id",
      "$identifier_value": 1,
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 2,
    ],
    [
      "$identifier_key": "type",
      "$identifier_value": "dog",
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Atributos personalizados aninhados não são compatíveis com o AppboyKit.
{% endalert %}
{% endtab %}

{% tab Web SDK %}
{% subtabs local %}
{% subtab Criar %}
```javascript
import * as braze from "@braze/web-sdk";
const json = [{
  "id": 1,
  "type": "dog",
  "breed": "beagle",
  "name": "Mochi"
}, {
  "id": 2,
  "type": "cat",
  "breed": "calico",
  "name": "Pixel"
}];
braze.getUser().setCustomUserAttribute("pets", json);
```
{% endsubtab %}

{% subtab Adicionar %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$add": [{
    "id":  3,
    "type":  "dog",
    "breed":  "corgi",
    "name":  "Doug",
  }, {
    "id":  4,
    "type":  "fish",
    "breed":  "salmon",
    "name":  "Pepper",
  }, {
    "id":  5,
    "type":  "bird",
    "breed":  "parakeet",
    "name":  "Noodle",
  }]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab Atualizar %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$update": [
    {
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": {
        "breed": "goldfish"
      }
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": {
        "name": "Annette"
      }
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab Excluir %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$remove": [
    {
      "$identifier_key": "id",
      "$identifier_value": 1,
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 2,
    },
    {
      "$identifier_key": "type",
      "$identifier_value": "dog",
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Templates com Liquid {#liquid-templating}

Você pode usar esse vetor `pets` para personalizar uma mensagem. O exemplo de template Liquid a seguir mostra como referenciar as propriedades do objeto de atributo personalizado salvas na requisição de API anterior e usá-las no envio de mensagens.

{% raw %}
```liquid
{% assign pets = {{custom_attribute.${pets}}} %}

{% for pet in pets %}
I have a {{pet.type}} named {{pet.name}}! They are a {{pet.breed}}.
{% endfor %}
```
{% endraw %}

Nesse cenário, você pode usar Liquid para percorrer o vetor `pets` e imprimir uma frase para cada animal de estimação. [Atribua uma variável]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/dashboard_tools#assign-variables) ao atributo personalizado `pets` e use a notação de ponto para acessar propriedades de um objeto. Especifique o nome do objeto, seguido de um ponto `.`, seguido do nome da propriedade.

## Segmentação {#segmentation}

Ao segmentar usuários com base em vetores de objetos, um usuário se qualificará para o segmento se qualquer objeto no vetor corresponder aos critérios.

Crie um novo segmento e selecione **Nested Custom Attribute** como seu filtro. Em seguida, pesquise e selecione o nome do seu vetor de objetos.

![Filtrar por vetor de objetos.]({% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %})

Use a notação de ponto para especificar qual campo no vetor de objetos você deseja usar. Comece o campo de texto com um par vazio de colchetes `[]` para indicar à Braze que você está buscando dentro de um vetor de objetos. Depois, adicione um ponto `.`, seguido do nome do campo que deseja usar.

Por exemplo, se você quiser filtrar um vetor de objetos `top_3_movies` com base no campo `type`, insira `[].type` e escolha os filmes para filtrar, como `Fantasy Movie`.


### Níveis de aninhamento {#levels-of-nesting}

Você pode criar um segmento com até um nível de aninhamento de vetor (vetor dentro de outro vetor). Por exemplo, considerando os atributos a seguir, você pode criar um segmento para `pets[].name` contém `Mochi`, mas não pode criar um segmento para `pets[].nicknames[]` contém `Gugu`.

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Mochi",
          "nicknames": [
            "MoMo",
            "Mochi"
          ]
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Pixel",
          "nicknames": [
            "PiPi",
            "Pixel"
          ]
        }
      ]
    }
  ]
}
```
{% endraw %}

## Pontos de dados {#data-points}

Os pontos de dados são registrados de forma diferente dependendo se você cria, atualiza ou remove uma propriedade.

{% tabs local %}
{% tab Criar %}

Criar um novo vetor registra um ponto de dados para cada atributo em um objeto. Este exemplo custa oito pontos de dados — cada objeto de animal de estimação tem quatro atributos e há dois objetos.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Mochi"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Pixel"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Atualizar %}

Atualizar um vetor existente registra um ponto de dados para cada propriedade adicionada. Este exemplo custa dois pontos de dados, pois atualiza apenas uma propriedade em cada um dos dois objetos.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Remover %}

Remover um objeto de um vetor registra um ponto de dados para cada critério de remoção enviado. Este exemplo custa três pontos de dados, mesmo que você possa estar removendo múltiplos cachorros com essa instrução.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}