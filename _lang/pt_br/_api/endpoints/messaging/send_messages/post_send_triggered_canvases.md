---
nav_title: "POST: Enviar mensagens do Canvas usando entrega acionada por API"
article_title: "POST: Enviar mensagens do Canvas usando entrega acionada por API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para envio de Canvas usando entrega acionada por API."

---
{% api %}
# Enviar mensagens do Canvas usando entrega acionada por API {#send-canvas-messages-using-api-triggered-delivery}
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/send
{% endapimethod %}

> Use este endpoint para enviar mensagens do Canvas com entrega acionada por API.

A entrega acionada por API permite que você armazene o conteúdo da mensagem no dashboard da Braze enquanto determina quando uma mensagem é enviada e para quem usando sua API.

Antes de enviar mensagens com esse endpoint, você deve ter um [ID do Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier) (que é criado quando você constrói um Canvas).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `canvas.trigger.send`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "context": (optional, object) Canvas context properties that apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if `recipients` is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message sends to the entire segment targeted by the Canvas)
    [{
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "context": (optional, object) Canvas context properties for this user; key-value pairs override any keys that conflict with the parent `context`,
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an `attributes` object must also be included,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }],
    ...
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | Obrigatória | String | Consulte [Identificador do Canvas]({{site.baseurl}}/api/identifier_types/). |
| `context` | Opcional | Objeto | Propriedades de contexto do Canvas para todos os destinatários nesta solicitação. Os pares de chave-valor de personalização se aplicam a todos os usuários, a menos que um `context` por destinatário substitua uma chave. O objeto `context` pode ter até 50 KB. |
| `broadcast` | Opcional | Booleano | Você deve definir `broadcast` como true ao enviar uma mensagem para todo o segmento configurado como o público-alvo do Canvas no dashboard da Braze. O padrão desse parâmetro é false (a partir de 31 de agosto de 2017). <br><br> Se `broadcast` estiver definido como true, uma lista `recipients` não poderá ser incluída. No entanto, tenha cuidado ao definir `broadcast: true`, pois definir essa flag inadvertidamente pode fazer com que você envie sua mensagem para um público maior do que o esperado. |
| `audience` | Opcional | Objeto de público conectado | Consulte [Público conectado]({{site.baseurl}}/api/objects_filters/connected_audience/). Quando você inclui `audience`, a mensagem é enviada apenas para usuários que correspondem aos filtros definidos, como atributos personalizados e status de inscrição. |
| `recipients` | Opcional | Vetor | Consulte o [objeto Recipients]({{site.baseurl}}/api/objects_filters/recipient_object/). <br><br> Se `send_to_existing_only` for `false`, um objeto `attributes` deve ser incluído no destinatário. <br><br> Se não fornecido e `broadcast` estiver definido como `true`, a mensagem é enviada para todo o segmento configurado como o público-alvo do Canvas no dashboard da Braze.<br><br> O vetor `recipients` pode conter até 50 objetos. Cada objeto deve incluir exatamente um entre `external_user_id`, `user_alias` ou `email`, e pode incluir um objeto `context` por destinatário para propriedades de contexto do Canvas (as chaves por destinatário substituem o `context` de nível superior quando há conflito). <br><br> Se `email` for o identificador, você deve incluir [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email) no objeto de destinatários. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## Exemplo de solicitação {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "context": {"product_name" : "shoes", "product_price" : 79.99},
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
      "external_user_id": "user_identifier",
      "send_to_existing_only": true,
      "attributes": {
          "first_name" : "Alex"
      }
    }
  ]
}'
```

## Detalhes da resposta {#response-details}

As respostas do endpoint de envio de mensagens incluem o `dispatch_id` da mensagem para referência ao despacho da mensagem. O `dispatch_id` é o ID do despacho de mensagens (ID exclusivo para cada "transmissão" enviada da plataforma Braze). Para saber mais, consulte [Comportamento do Dispatch ID]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id/).

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `201` pode retornar o seguinte corpo de resposta. Se o Canvas estiver arquivado, parado ou pausado, ele não é enviado por meio deste endpoint.

```
{
  "notice": "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.",
  "dispatch_id": "example_dispatch_id",
  "message": "success"
}
```

Se o seu Canvas estiver arquivado, você verá esta mensagem `notice`: "The Canvas is archived. Unarchive the Canvas to ensure trigger requests will take effect." Se o seu Canvas não estiver ativo, você verá esta mensagem `notice`: "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect."

Se sua solicitação encontrar um erro fatal, consulte [Erros e respostas]({{site.baseurl}}/api/errors/#fatal-errors) para obter o código e a descrição do erro.

## Considerações {#considerations}

Considere o seguinte ao fazer chamadas de API para enviar mensagens do Canvas usando entrega acionada por API:

- **Envio para usuários existentes**: Quando `send_to_existing_only` está definido como `true` (o padrão), a mensagem é enviada apenas para usuários existentes na Braze.
- **Criação de novos usuários**: Quando `send_to_existing_only` está definido como `false`, você deve incluir um objeto `attributes`. Se um usuário com o ID especificado não existir, a Braze cria um usuário com esse ID e atributos antes de enviar a mensagem.
- **Perfis novos precisam de `attributes` com `send_to_existing_only: false`.** A Braze executa a criação ou atualização pré-envio a partir do objeto `attributes` no mesmo destinatário. Se você definir `send_to_existing_only` como `false`, mas omitir `attributes` (ou enviar um objeto vazio), a Braze não hidrata os dados do perfil da mesma forma, então você não obtém o comportamento combinado de "criar ou atualizar usuário e depois enviar" para o qual esse padrão foi projetado.
- **Endereçamento de e-mail e SMS.** Para a maioria dos envios de e-mail ou SMS acionados por API para alguém que ainda não está na Braze, inclua os campos de entrega necessários dentro de `attributes` (por exemplo, `email` ou os atributos de telefone que seu espaço de trabalho usa para SMS). Você também pode definir a associação ao grupo de inscrições ou o status de inscrição quando o estado de opt-in precisa mudar na mesma chamada.
- **Elegibilidade do Canvas.** Depois que o perfil existe ou é atualizado, esse usuário ainda deve corresponder ao público-alvo do Canvas no dashboard e às regras de envio do canal (por exemplo, ter opt-in para e-mail) para que a Braze envie a mensagem.
- **Limitação de alias de usuário**: A flag `send_to_existing_only` não pode ser usada com aliases de usuário. Para enviar para um usuário que possui apenas um alias, o usuário já deve existir na Braze.
- **Direcionamento de segmento**: O parâmetro `segment_id` não é suportado para este endpoint. Para direcionar um segmento, configure o segmento nas configurações de público-alvo do Canvas no dashboard da Braze e use `broadcast: true`, ou use o parâmetro `audience` com filtros de [Público conectado]({{site.baseurl}}/api/objects_filters/connected_audience/).
- **Direcionamento combinado**: Quando você inclui tanto o parâmetro `recipients` quanto configura um segmento alvo no dashboard, a mensagem é enviada apenas para os perfis de usuário que estão especificados na chamada da API e que também correspondem aos filtros do segmento.
- **Chamadas de servidor para servidor**: Se você estiver fazendo chamadas de servidor para servidor, pode ser necessário adicionar a URL da API apropriada à lista de permissões se você estiver atrás de um firewall.

## Objeto de atributos para Canvas {#attributes-object-for-canvas}

Use o objeto de envio de mensagens `attributes` para adicionar, criar ou atualizar atributos e valores para um usuário antes de enviar um Canvas acionado por API usando o endpoint `canvas/trigger/send`. Esta chamada de API processa o objeto de atributos do usuário antes de processar e enviar o Canvas. Isso ajuda a minimizar o risco de problemas causados por [condições de corrida]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions/). No entanto, por padrão, os grupos de inscrições não podem ser atualizados dessa forma.

{% alert note %}
Procurando a versão de Campaign deste endpoint? Confira [Envio de mensagens de Campaign usando entrega acionada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).
{% endalert %}

{% endapi %}