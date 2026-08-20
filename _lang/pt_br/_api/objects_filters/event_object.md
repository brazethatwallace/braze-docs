---
nav_title: "Objeto de evento"
article_title: Objeto de evento da API
page_order: 6
page_type: reference
description: "Este artigo de referência aborda o objeto de evento, o que ele é e como é uma parte crucial das estratégias de Campaign baseadas em eventos."

---

# Objeto de evento {#event-object}

> Este artigo explica os diferentes componentes de um objeto de evento, como você pode usar esse objeto e exemplos para se basear.

## O que é um objeto de evento? {#what-is-an-event-object}

Um objeto de evento é um objeto que é passado pela API quando um evento específico ocorre. Os objetos de evento ficam armazenados em um array de eventos. Cada objeto de evento no array de eventos representa uma única ocorrência de um evento personalizado por um usuário específico no valor de tempo designado. O objeto de evento tem muitos campos diferentes que permitem personalizar configurando e usando propriedades de evento em mensagens, coleta de dados e personalização.

Para ver as etapas de como configurar eventos personalizados para uma plataforma específica, consulte o Guia de Integração de Plataforma no [Guia do Desenvolvedor]({{site.baseurl}}/developer_guide/home). Consulte o artigo relevante com base na sua plataforma:

- [Android]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)

### Corpo do objeto {#object-body}

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  "name" : (required, string) the name of the event,
  "time" : (required, datetime as string in ISO 8601 or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format),
  "properties" : (optional, Properties Object) properties of the event
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
  // See following notes regarding anonymous push token imports
}
```

{% alert note %}
Eventos com timestamps no futuro usam como padrão o horário atual. Isso garante que os eventos personalizados sejam registrados com a temporização correta.
{% endalert %}

- [ID de usuário externo]({{site.baseurl}}/api/basics#user-ids)
- [Identificador do app]({{site.baseurl}}/api/identifier_types)
- [Código de tempo ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)

{% alert note %}
Alguns pares de identificadores não podem ser usados juntos em uma única solicitação. Quando `email` e `phone` são fornecidos ao mesmo tempo, `email` tem precedência sobre `phone`. Para mais detalhes, consulte [Resolução de identificadores]({{site.baseurl}}/api/objects_filters/user_attributes_object#identifier-resolution).
{% endalert %}

#### Atualizar apenas perfis existentes {#update-existing-profiles-only}

Para atualizar apenas perfis de usuário existentes na Braze, você deve passar a chave `_update_existing_only` com o valor `true` no corpo da sua solicitação. Se esse valor for omitido, a Braze criará um novo perfil de usuário caso o `external_id` ainda não exista.

{% alert note %}
Se você estiver criando um perfil de usuário somente com alias por meio do endpoint `/users/track`, `_update_existing_only` deve ser definido como `false`. Se esse valor for omitido, o perfil somente com alias não será criado.
{% endalert %}

## Objeto de propriedades de evento {#event-properties-object}

Eventos personalizados e compras podem ter propriedades de evento. Os valores de "properties" devem ser um objeto em que as chaves são os nomes das propriedades e os valores são os valores das propriedades. Os nomes das propriedades devem ser strings não vazias com 255 caracteres ou menos, sem cifrões ($) no início.

Os valores das propriedades podem ser qualquer um dos seguintes tipos de dados:

| Tipo de dados | Descrição |
| --- | --- |
| Números | Como [inteiros](https://en.wikipedia.org/wiki/Integer) ou [pontos flutuantes](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booleanos | `true` ou `false` |
| Datas e horas | Devem ser formatados como strings no formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) ou em qualquer um dos seguintes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Não suportado dentro de arrays. <br><br>Nota: "T" é um designador de hora, não um espaço reservado, e não deve ser alterado ou removido. <br><br> Atributos de hora sem fuso horário serão definidos como meia-noite UTC por padrão (e serão formatados no dashboard como o equivalente à meia-noite UTC no fuso horário da empresa). <br><br> Eventos com timestamps no futuro serão definidos como a hora atual por padrão.  |
| Strings | 255 caracteres ou menos. |
| Arrays | Arrays não podem incluir datas e horas. |
| Objetos | Objetos serão ingeridos como strings. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Objeto de propriedades de evento" }

Objetos de propriedades de evento que contêm valores de array ou objeto podem ter uma carga útil de propriedade de evento de até 100&nbsp;KB.

### Chaves reservadas {#reserved-keys}

As seguintes chaves são reservadas e não podem ser usadas como propriedades de eventos personalizados:

- `time`
- `event_name`

{% alert important %}
Usar chaves reservadas como nomes de propriedades de eventos personalizados resultará em erros de API ao enviar solicitações para o endpoint `/users/track`.
{% endalert %}

### Persistência de propriedades de evento {#event-property-persistence}

As propriedades de evento são projetadas para filtragem e personalização com Liquid em mensagens disparadas por seus eventos de origem. Por padrão, elas não são persistidas no perfil de usuário da Braze. Para usar valores de propriedades de evento em segmentação, consulte [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events), que detalha as diversas abordagens para armazenar valores de propriedades de evento a longo prazo.

#### Exemplo de solicitação de evento {#event-example-request}

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "events" : [
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:30+01:00"
    },
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "rented_movie",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "movie": "The Sad Egg",
        "director": "Alex Smith"
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:50+01:00"
    }
  ]
}
```
- [Wiki do código de hora ISO 8601](http://en.wikipedia.org/wiki/ISO_8601)

## Objetos de evento {#event-objects}

Usando o exemplo fornecido, podemos ver que alguém assistiu a um trailer recentemente e depois alugou um filme. Embora não seja possível entrar em uma Campaign e segmentar os usuários com base nessas propriedades, podemos usá-las estrategicamente na forma de um recibo, para enviar uma mensagem personalizada por meio de um canal usando Liquid. Por exemplo, "Olá **Alex**, Obrigado por alugar **The Sad Egg** de **Alex Smith**, aqui estão alguns filmes recomendados com base no seu aluguel..."