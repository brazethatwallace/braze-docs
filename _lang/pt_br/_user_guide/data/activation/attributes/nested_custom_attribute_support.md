---
nav_title: Atributos personalizados aninhados
article_title: Atributos personalizados aninhados
alias: "/nested_custom_attribute_support/"
page_order: 3
page_type: reference
description: "Este artigo de referência aborda o uso de atributos personalizados aninhados como um tipo de dados para atributos personalizados, incluindo limitações e exemplos de uso."
---

# Atributos personalizados aninhados {#nested-custom-attributes}

> Esta página aborda os atributos personalizados aninhados, que permitem definir um conjunto de atributos como uma propriedade de outro atributo. Em outras palavras, quando você define um objeto de atributo personalizado, pode definir um conjunto de atributos adicionais para esse objeto.

{% multi_lang_include nested_attribute_objects/about_nested_attributes.md %}

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## Considerações {#considerations}

- Os atributos personalizados aninhados destinam-se a atributos personalizados enviados por meio do SDK ou da API da Braze.
- Os objetos têm um tamanho máximo de 100&nbsp;KB. Se uma atualização fizer com que o objeto exceda 100&nbsp;KB, a Braze descarta a atualização e o atributo permanece inalterado.
- Os nomes das chaves e os valores das strings têm um limite de tamanho de 255 caracteres.
- Os nomes das chaves não podem conter espaços.
- Pontos (`.`) e sinais de dólar (`$`) não são caracteres suportados em uma carga útil de API se você estiver tentando enviar um atributo personalizado aninhado para um perfil de usuário.
- Nem todos os parceiros da Braze suportam atributos personalizados aninhados. Consulte a [documentação do parceiro]({{site.baseurl}}/partners/home/) para confirmar se integrações com parceiros específicos suportam esse recurso.
- Os atributos personalizados aninhados não podem ser usados como filtro ao fazer uma chamada à API do Connected Audience.
- Por padrão, o filtro de Segment **Nested Custom Attributes** inclui atributos personalizados do tipo objeto, atributos de vetor de objetos e atributos personalizados do tipo vetor. Quando você seleciona um atributo, o seletor de esquema de propriedades inclui caminhos de vetor (usando a notação `[]`) para campos de vetor aninhados. Para ocultar atributos personalizados de vetor de nível superior desse filtro, entre em contato com o [suporte da Braze]({{site.baseurl}}/braze_support/).
- Ao pré-visualizar mensagens no dashboard usando **Preview as a Custom User**, você pode inserir dados simulados apenas como uma string ou vetor de strings — objetos aninhados não são suportados. Para pré-visualizar uma mensagem que referencia atributos personalizados aninhados, selecione um usuário existente que já tenha o atributo aninhado em seu perfil. Para propriedades de eventos personalizados aninhados, você deve lançar uma campanha ativa direcionada a um usuário teste para verificar a renderização.

## Exemplo de API {#api-example}

{% tabs local %}
{% tab Criar %}
A seguir, um exemplo de `/users/track` com um objeto "Most Played Song". Para capturar as propriedades da música, enviaremos uma solicitação de API que lista `most_played_song` como um objeto, junto com um conjunto de propriedades do objeto.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Atualizar %}
Para atualizar um objeto existente, envie um POST para `users/track` com o parâmetro `_merge_objects` na solicitação. Isso fará um deep merge da sua atualização com os dados existentes do objeto. O deep merge garante que todos os níveis de um objeto sejam mesclados em outro objeto, em vez de apenas o primeiro nível. Neste exemplo, já temos um objeto `most_played_song` na Braze e agora estamos adicionando um novo campo, `year_released`, ao objeto `most_played_song`.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "most_played_song": {
          "year_released": 1960
      }
    }
  ]
}
```

Após o recebimento dessa solicitação, o objeto de atributo personalizado ficará assim:

```json
{"most_played_song": {
  "song_name": "Solea",
  "artist_name" : "Miles Davis",
  "album_name": "Sketches of Spain",
  "year_released": 1960,
  "genre": "Jazz",
  "play_analytics": {
     "count": 1000,
     "top_10_listeners": true
  }
}}
```

{% alert warning %}
Você deve definir `_merge_objects` como `true`, caso contrário seus objetos serão sobrescritos. `_merge_objects` é `false` por padrão.
{% endalert %}

{% endtab %}
{% tab Excluir %}
Para excluir um objeto de atributo personalizado, envie um POST para `users/track` com o objeto de atributo personalizado definido como `null`.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": null
    }
  ]
}
```

{% alert note %}
Essa abordagem não pode ser usada para excluir uma chave aninhada dentro de um [vetor de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects/).
{% endalert %}

{% endtab %}
{% endtabs %}

## Exemplo de SDK {#sdk-example}

{% sdk_min_versions android:25.0.0 ios:6.1.0 web:4.7.0 %}

{% tabs local %}
{% tab Android SDK %}

**Criar**
```kotlin
val json = JSONObject()
    .put("song_name", "Solea")
    .put("artist_name", "Miles Davis")
    .put("album_name", "Sketches of Spain")
    .put("genre", "Jazz")
    .put(
        "play_analytics",
        JSONObject()
            .put("count", 1000)
            .put("top_10_listeners", true)
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json)
}
```

**Atualizar**
```kotlin
val json = JSONObject()
    .put("year_released", 1960)

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json, true)
}
```

**Excluir**
```kotlin
braze.getCurrentUser { user ->
    user.unsetCustomUserAttribute("most_played_song")
}
```

{% endtab %}
{% tab Swift SDK %}

**Criar**
```swift
let json: [String: Any?] = [
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": [
    "count": 1000,
    "top_10_listeners": true,
  ],
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json)
```

**Atualizar**
```swift
let json: [String: Any?] = [
  "year_released": 1960
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json, merge: true)
```

**Excluir**
```swift
braze.user.unsetCustomAttribute(key: "most_played_song")
```

{% endtab %}
{% tab Web SDK %}

**Criar**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": {
    "count": 1000,
    "top_10_listeners": true
  }
};
braze.getUser().setCustomUserAttribute("most_played_song", json);
```

**Atualizar**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "year_released": 1960
};
braze.getUser().setCustomUserAttribute("most_played_song", json, true);

```

**Excluir**
```javascript
import * as braze from "@braze/web-sdk";
braze.getUser().setCustomUserAttribute("most_played_song", null);
```

{% endtab %}
{% endtabs %}

## Capturando datas como propriedades de objetos {#capturing-dates-as-object-properties}

Para capturar datas como propriedades de objetos, você deve usar a chave `$time`. No exemplo a seguir, um objeto "Important Dates" é usado para capturar o conjunto de propriedades do objeto, `birthday` e `wedding_anniversary`. Os valores dessas datas são objetos com uma chave `$time`, que não pode ser um valor nulo.

{% alert note %}
Se você não capturou datas como propriedades de objetos inicialmente, recomendamos reenviar esses dados usando a chave `$time` para todos os usuários. Caso contrário, isso pode resultar em segmentos incompletos ao usar o atributo `$time`. No entanto, se o valor de `$time` em um atributo personalizado aninhado não estiver formatado corretamente, o atributo personalizado aninhado inteiro não será atualizado.
{% endalert %}

```json
{
  "attributes": [
    {
      "external_id": "time_with_nca_test",
      "important_dates": {
        "birthday": {"$time" : "1980-01-01"},
        "wedding_anniversary": {"$time" : "2020-05-28"}
      }
    }
  ]
}
```

{% alert note %}
Para atributos personalizados aninhados, se o ano for menor que 0 ou maior que 3000, a Braze não armazena esses valores no usuário.
{% endalert %}

## Templates com Liquid {#liquid-templating}

O exemplo de template Liquid a seguir mostra como referenciar as propriedades do objeto de atributo personalizado salvas na solicitação de API anterior e usá-las no seu envio de mensagens.

Use a tag de personalização `custom_attribute` e a notação de ponto para acessar propriedades em um objeto. Especifique o nome do objeto (e a posição no vetor, se estiver referenciando um vetor de objetos), seguido de um ponto, seguido do nome da propriedade.

{% raw %}
`{{custom_attribute.${most_played_song}[0].artist_name}}` — "Miles Davis"
<br> `{{custom_attribute.${most_played_song}[0].song_name}}` — "Solea"
<br> `{{custom_attribute.${most_played_song}[0].play_analytics.count}}` — "1000"
{% endraw %}

![Usando Liquid para inserir o nome de uma música e o número de vezes que um ouvinte reproduziu essa música em uma mensagem]({% image_buster /assets/img_archive/nca_liquid_2.png %})

### Personalização {#personalization}

Usando o modal **Add Personalization**, você também pode inserir atributos personalizados aninhados no seu envio de mensagens. Selecione **Nested Custom Attributes** como o tipo de personalização. Em seguida, selecione o atributo de nível superior e a chave do atributo.

Por exemplo, no modal de personalização abaixo, isso insere o atributo personalizado aninhado de um escritório de bairro local com base nas preferências do usuário.

![O modal Add Personalization com o tipo de personalização definido como "Nested Custom Attrib...", o atributo de nível superior definido como "preferences" e a chave do atributo definida como "neighborhood_office", mostrando uma pré-visualização Liquid da tag resultante.]({% image_buster /assets/img_archive/nca_personalization.png %}){: style="max-width:70%" }

{% alert tip %}
Verifique se um esquema foi gerado caso você não veja a opção de inserir atributos personalizados aninhados.
{% endalert %}

## Regenerar esquemas {#regenerate-schema}

Após um esquema ser gerado, ele pode ser regenerado **uma vez por dia corrido** (com base no fuso horário da sua empresa). Esta seção descreve como regenerar seu esquema. Para informações mais detalhadas sobre esquemas, consulte [Gerar um esquema usando o explorador de objetos aninhados]({{site.baseurl}}/user_guide/audience/segments/segment_with_nested_custom_attributes/#generate-schema).

Para regenerar o esquema do seu atributo personalizado aninhado:

1. Acesse **Configurações de dados** > **Atributos personalizados**.
2. Pesquise seu atributo personalizado aninhado.
3. Na coluna **Attribute Name** do seu atributo, selecione <i class="fas fa-plus" aria-label="Gerenciar esquema"></i> **Manage schema** para gerenciar o esquema.
4. Um modal será exibido. Selecione **Regenerate Schema**.

A ação **Regenerate Schema** é limitada a **uma vez por dia corrido** no fuso horário da sua empresa. Não é possível iniciar outra regeneração enquanto um trabalho de esquema já estiver **em andamento** (a opção fica indisponível enquanto o status for **Generating**). Regenerar o esquema detecta apenas novos objetos e não exclui objetos que já existem no esquema.

{% alert important %}
Para redefinir o esquema de um vetor de objetos com um objeto existente, você precisa criar um novo atributo personalizado. A regeneração do esquema não exclui objetos existentes.
{% endalert %}

Se os dados não aparecerem como esperado após regenerar o esquema, o atributo pode não estar sendo ingerido com frequência suficiente. Os dados de usuários são amostrados com base em dados anteriores enviados à Braze para o atributo aninhado em questão. Se o atributo não for ingerido com frequência suficiente, ele não será capturado para o esquema.

## Disparar alterações em atributos personalizados aninhados {#trigger-nested-custom-attribute-changes}

Você pode disparar ações quando um objeto de atributo personalizado aninhado é alterado. Essa opção não está disponível para alterações em vetores de objetos. Se você não vir a opção de visualizar o explorador de jornadas, verifique se você gerou um esquema.

Por exemplo, em uma Campaign baseada em ação, você pode adicionar uma nova ação-gatilho para **Change Custom Attribute Value** para direcionar usuários que alteraram suas preferências de escritório de bairro.

![Configurações de entrega de Campaign baseada em ação com um gatilho de Change Custom Attribute Value para preferências aninhadas.]({% image_buster /assets/img_archive/nca_triggered_changes.png %})

## Comportamento de segmentação com vetores de objetos {#segmentation-behavior-with-arrays-of-objects}

Quando você usa múltiplos filtros de `Nested Custom Attribute` com lógica AND para segmentar em um vetor de objetos, cada filtro é avaliado independentemente em todos os itens do vetor. Um usuário se qualifica para o Segment se *qualquer* item no vetor satisfizer cada filtro individual — os filtros não precisam corresponder ao *mesmo* item.

Por exemplo, suponha que um usuário tenha o seguinte vetor:

```json
{
  "orders": [
    {"product": "Shoes", "price": 80},
    {"product": "Hat", "price": 25}
  ]
}
```

Um Segment com os seguintes filtros AND:

- `orders[].price` é maior que 50
- `orders[].price` é menor que 30

Esse usuário se qualificaria porque o primeiro filtro corresponde ao item "Shoes" (80 > 50) e o segundo filtro corresponde ao item "Hat" (25 < 30). Mesmo que nenhum item individual satisfaça ambas as condições, o usuário ainda entra no Segment.

Se você precisar que todas as condições correspondam ao mesmo item dentro de um vetor, use [segmentação multicritério]({{site.baseurl}}/user_guide/audience/segments/segment_with_nested_custom_attributes/#use-multi-criteria-segmentation) na mesma jornada, ou reestruture seus dados para evitar correspondência entre itens diferentes.

## Pontos de dados {#data-points}

Qualquer chave enviada consome um ponto de dados. Por exemplo, este objeto inicializado no perfil de usuário conta como sete (7) pontos de dados:

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "year_released": 1960,
        "genre": "Jazz",
        "play_analytics": {
          "count": 1000,
          "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% alert note %}
Atualizar um objeto de atributo personalizado para `null` também consome um ponto de dados.
{% endalert %}