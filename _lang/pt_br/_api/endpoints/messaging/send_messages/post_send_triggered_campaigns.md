---
nav_title: "POST: Enviar Campaigns usando entrega disparada por API"
article_title: "POST: Enviar Campaigns usando entrega disparada por API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para enviar Campaigns usando entrega disparada por API."

---
{% api %}
# Enviar mensagens de Campaign usando entrega disparada por API {#send-campaign-messages-using-api-triggered-delivery}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/trigger/send
{% endapimethod %}

> Use esse endpoint para enviar mensagens únicas e imediatas a usuários designados usando a entrega disparada por API.

A entrega disparada por API permite que você armazene o conteúdo da mensagem dentro do dashboard da Braze e, ao mesmo tempo, determine quando a mensagem será enviada e para quem, usando sua API.

Se você estiver direcionando um Segment, um registro da sua solicitação é armazenado no [Console de desenvolvedor](https://dashboard.braze.com/app_settings/developer_console/activitylog/). Para enviar mensagens com esse endpoint, você deve ter um [ID de Campaign]({{site.baseurl}}/api/identifier_types) criado ao criar uma [Campaign disparada por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `campaigns.trigger.send`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to all users in this request,
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' sends to only users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to `false`, message sends to the entire segment targeted by the campaign)
    [
      {
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "trigger_properties": (optional, object) personalization key-value pairs that apply to this user (these key-value pairs override any keys that conflict with the parent trigger_properties),
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an attributes object must also be included,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
  ],
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name", "url", and optionally "basic_auth_credential",
    [
      {
       "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
       "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension is detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
       "basic_auth_credential": (optional, string) the name of the stored basic authentication credential to use when the attachment URL requires a login,
      }
    ]
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Obrigatório | String | Consulte [identificador de Campaign]({{site.baseurl}}/api/identifier_types). |
| `send_id` | Opcional | String | Consulte [identificador de envio]({{site.baseurl}}/api/identifier_types). |
| `trigger_properties` | Opcional | Objeto | Consulte [propriedades do disparador]({{site.baseurl}}/api/objects_filters/trigger_properties_object). Os pares de chave-valor de personalização se aplicam a todos os usuários nesta solicitação. |
| `broadcast` | Opcional | Booleano | Você deve definir `broadcast` como true ao enviar uma mensagem para todo o Segment configurado como o público-alvo da Campaign no dashboard da Braze. O padrão desse parâmetro é false (a partir de 31 de agosto de 2017). <br><br> Se `broadcast` estiver definido como true, uma lista `recipients` não poderá ser incluída. No entanto, tenha cuidado ao definir `broadcast: true`, pois definir essa flag inadvertidamente pode fazer com que você envie sua mensagem para um público maior do que o esperado. |
| `audience` | Opcional | Objeto de público conectado | Consulte [público conectado]({{site.baseurl}}/api/objects_filters/connected_audience). Quando você inclui `audience`, a mensagem é enviada apenas para usuários que correspondem aos filtros definidos, como atributos personalizados e status de inscrição. |
| `recipients` | Opcional | Vetor | Consulte [objeto de destinatários]({{site.baseurl}}/api/objects_filters/recipient_object).<br><br>Se `send_to_existing_only` for `false`, um objeto `attributes` deverá ser incluído.<br><br>Você pode atualizar o status do grupo de inscrições de um usuário incluindo `subscription_groups` no objeto `attributes` aninhado. Para saber mais, consulte [Objeto de atributos do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object).<br><br>Se `recipients` não for fornecido e `broadcast` estiver definido como true, a mensagem é enviada para todo o Segment configurado como o público-alvo da Campaign no dashboard da Braze.<br><br>Se `email` for o identificador, você deve incluir [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers) no objeto de destinatários. |
| `attachments` | Opcional | Vetor | Se `broadcast` estiver definido como true, a lista `attachments` não poderá ser incluída. <br><br>Quando uma URL de anexo exigir um login, inclua `basic_auth_credential` nesse anexo e defina-o com o nome de uma credencial de autenticação básica armazenada. Para configurar uma credencial, consulte [Autenticação para anexos de arquivo de e-mail]({{site.baseurl}}/api/objects_filters/messaging/email_object#authentication-for-email-file-attachments). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

### Comportamento de resolução de destinatários {#recipient-resolution-behavior}

Esta seção explica como a Braze seleciona um perfil de usuário para envio e o que acontece quando um perfil não é selecionado.

O status do grupo de inscrições de um usuário pode ser atualizado com a inclusão de um parâmetro `subscription_groups` no objeto `attributes`. Para saber mais, consulte [Objeto de atributos do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object).

#### Limites de destinatários e criação de perfis {#recipient-limits-and-profile-creation}

Saiba mais sobre como os limites de destinatários e a criação de perfis funcionam para esse endpoint.

- O vetor `recipients` pode conter até 50 objetos, sendo que cada objeto contém uma única string `external_user_id` e um objeto `trigger_properties`.
- Quando `send_to_existing_only` é `true` (o padrão), a Braze envia a mensagem apenas para usuários existentes.
- Quando `send_to_existing_only` é `false` e um objeto `attributes` é fornecido, a Braze cria um novo usuário se ele não existir.
- **Perfis novos precisam de `attributes` com `send_to_existing_only: false`.** A Braze executa a criação ou atualização pré-envio a partir do objeto `attributes` no mesmo destinatário. Se você definir `send_to_existing_only` como `false`, mas omitir `attributes` (ou enviar um objeto vazio), a Braze não hidrata os dados do perfil da mesma forma, então você não obtém o comportamento combinado de "criar ou atualizar usuário e depois enviar" para o qual esse padrão foi projetado.
- **Endereçamento de e-mail e SMS.** Para a maioria dos envios de e-mail ou SMS disparados por API para alguém que ainda não está na Braze, inclua os campos de entrega necessários dentro de `attributes` (por exemplo, `email` ou os atributos de telefone que seu espaço de trabalho usa para SMS). Você também pode definir a associação ao grupo de inscrições ou o status de inscrição quando o estado de aceitação precisa ser alterado na mesma chamada.
- **Elegibilidade da Campaign.** Depois que o perfil existir ou for atualizado, o usuário ainda precisa corresponder ao público-alvo da Campaign no dashboard e às regras de envio do canal (por exemplo, ter aceitação para e-mail) para que a Braze envie a mensagem.
- Definir `send_to_existing_only` como `false` não é compatível com aliases de usuário. Novos usuários apenas com alias não podem ser criados por meio deste endpoint. Para enviar para um usuário apenas com alias, o usuário já deve existir na Braze.

#### Identificador de e-mail e empates de priorização {#email-identifier-and-prioritization-ties}

Quando você identifica destinatários por e-mail, a Braze usa `prioritization`. A Braze envia apenas quando `prioritization` retorna um perfil.

- Se você usar `email` como identificador, a Braze resolve o destinatário usando `prioritization`.
- Se `prioritization` retornar um empate, a Braze não envia.
- A Braze envia após o empate ser resolvido e `prioritization` retornar um perfil. Por exemplo, se atualizações de perfil alterarem os campos de ordenação de um usuário, a Braze envia assim que `prioritization` puder identificar um perfil de forma única (consulte [Comportamento de nova tentativa e `send_to_existing_only`](#retry-behavior-and-send_to_existing_only)).
- A Braze também não envia quando `prioritization` não retorna nenhum perfil.

#### Comportamento de nova tentativa e send_to_existing_only {#retry-behavior-and-send_to_existing_only}

Saiba o que acontece quando `prioritization` não retorna exatamente um perfil.

- Quando `prioritization` não retorna exatamente um perfil de usuário, a Braze tenta a resolução novamente até 40 vezes. Esse comportamento de nova tentativa é esperado.
- A configuração `send_to_existing_only` não altera o comportamento de empate de `prioritization`. O mesmo comportamento de empate e nova tentativa se aplica independentemente de essa configuração ser `true` ou `false`.

Se você disparar uma Campaign somente de e-mail para um destinatário identificado por `external_user_id` ou `user_alias`, e esse perfil de usuário não tiver um endereço de e-mail no momento da chamada, a Braze tenta o envio novamente por aproximadamente 2 horas. Isso cobre o padrão comum de criar um usuário e definir seu endereço de e-mail em sequência. Para enviar sem postergação, inclua o atributo `email` dentro de `recipients[].attributes` para que o endereço seja definido na mesma chamada do disparo.

{% alert note %}
O parâmetro `segment_id` não é compatível com este endpoint. Para direcionar um Segment, configure o Segment nas configurações de público-alvo da Campaign no dashboard da Braze e use `"broadcast": true`, ou use o parâmetro `audience` com filtros de [público conectado]({{site.baseurl}}/api/objects_filters/connected_audience).
{% endalert %}

## Exemplo de solicitação {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "trigger_properties": "",
  "broadcast": false,
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "recipients": [
    {
      "user_alias": {
        "alias_name" : "example_name",
        "alias_label" : "example_label"
      },
      "external_user_id": "external_user_identifier",
      "trigger_properties": "",
      "send_to_existing_only": true,
      "attributes": {
        "first_name" : "Alex"
      }
    }
  ],
  "attachments": [
    {
      "file_name" : "YourFileName",
      "url" : "https://exampleurl.com/YourFileName.pdf",
      "basic_auth_credential": "company_basic_auth_credential_name"
    }
  ]
}'
```

## Detalhes da resposta {#response-details}

As respostas do endpoint de envio de mensagens incluem o `dispatch_id` da mensagem para referência ao despacho da mensagem. O `dispatch_id` é o ID do despacho de mensagens, um ID exclusivo para cada transmissão enviada pela Braze. Ao usar esse endpoint, você recebe um único `dispatch_id` para um conjunto inteiro de usuários em lote. Para saber mais sobre o `dispatch_id`, consulte nossa documentação sobre o [comportamento do Dispatch ID]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id).

Se sua solicitação encontrar um erro fatal, consulte [Erros e respostas]({{site.baseurl}}/api/errors#fatal-errors) para obter o código e a descrição do erro.

## Objeto de atributos para Campaigns {#attributes-object-for-campaigns}

A Braze tem um objeto de envio de mensagens chamado `attributes` que permite adicionar, criar ou atualizar atributos e valores para um usuário antes de enviar uma Campaign disparada por API. Usar o endpoint `campaign/trigger/send` como essa chamada de API processa o objeto de atributos do usuário antes de processar e enviar a Campaign. Isso ajuda a minimizar o risco de problemas causados por [condições de corrida]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions).

{% alert tip %}
Está procurando a versão do Canvas desse endpoint? Confira [Envio de mensagens do Canvas usando entrega disparada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).
{% endalert %}

### Por que o Liquid não renderiza quando eu o coloco diretamente no corpo JSON? {#why-doesnt-liquid-render-when-i-put-it-directly-in-my-json-body}

Quando o corpo da sua solicitação é um JSON válido, a Braze avalia qualquer Liquid na carga útil no servidor. Se você incorporar Liquid como strings brutas, coloque aspas e escape essas strings para que o corpo permaneça um JSON válido — por exemplo, escape aspas duplas dentro de strings. Se o corpo falhar na análise JSON, a Braze retorna um `400` antes de avaliar qualquer Liquid. Quando possível, passe valores dinâmicos por meio de [`trigger_properties`]({{site.baseurl}}/api/objects_filters/trigger_properties_object) em vez de incorporar Liquid diretamente na carga útil.

{% endapi %}