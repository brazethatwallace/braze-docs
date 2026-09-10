---
nav_title: Limites de taxa
article_title: Limites de taxa
page_order: 4.5
description: "Este artigo de referência aborda os limites de taxa da API para a infraestrutura da API da Braze."
page_type: reference
---

# Limites de taxa {#rate-limits}

> A infraestrutura da API da Braze foi projetada para lidar com grandes volumes de dados de nossa base de clientes. Para isso, aplicamos limites de taxa de API por espaço de trabalho.

Um limite de taxa é o número de solicitações que a API pode receber em um determinado período. Muitos incidentes de negação de serviço baseados em carga em grandes sistemas não são intencionais — causados por erros no software ou nas configurações — e não por ataques mal-intencionados. Os limites de taxa garantem que esses erros não privem nossos clientes dos recursos da API da Braze. Se muitas solicitações forem enviadas em um determinado período, você poderá ver respostas de erro com um código de status `429`, o que indica que o limite de taxa foi atingido.

{% alert warning %}
Os limites de taxa da API estão sujeitos a alterações, dependendo do uso adequado de nosso sistema. Incentivamos limites sensatos ao fazer uma chamada à API para evitar danos ou uso indevido.
{% endalert %}

## Limites de frequência por tipo de requisição {#rate-limits-by-request-type}

Consulte a seguir os limites de frequência padrão da API para diferentes tipos de requisição. Esses limites padrão podem ser aumentados mediante solicitação. Entre em contato com seu gerente de sucesso do cliente para saber mais.

### Requisições com limites de frequência diferentes {#requests-with-different-rate-limits}

| Tipo de requisição                                                                                                                                                                                                                                           | Limite de frequência padrão da API                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)                                                                                                                                                                                                                                   | **Requisições:** Os limites de frequência variam dependendo do seu contrato. Para clientes com pontos de dados em seus preços, a Braze aplica um limite de burst de 3.000 requisições a cada três segundos. Para todos os outros clientes, os limites são configurados de acordo com os termos do seu contrato. Entre em contato com o suporte da Braze ou com seu gerente de sucesso do cliente para dúvidas sobre seus limites.<br><br>**Agrupamento:** Até 75 objetos no total combinados entre `attributes`, `events` e `purchases` por requisição de API. Clientes com limites de frequência legados podem incluir até 75 objetos por array de forma independente. Para saber mais, consulte [Agrupamento de requisições User Track](#batch-user-track).<br><br>**Limites para Monthly Active Users CY 24-25, Universal MAU, Web MAU e Mobile MAU:** Consulte [Limites de Monthly Active Users CY 24-25]({{site.baseurl}}/api/endpoints/user_data/post_user_track#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau). |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)                                                                                                                                                                                                                              | **Se você fez a integração em ou após 22 de agosto de 2024:** 250 requisições por minuto. <br><br> **Se você fez a integração antes de 22 de agosto de 2024:** 2.500 requisições por minuto.                                                                                                                                                               |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)<br>[`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias)<br>[`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update)<br>[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)<br>[`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)                                                                                                                    | 20.000 requisições por minuto, compartilhadas entre os endpoints.                                                                                                                                                                                                                                                                                                                                 |
| [`/users/external_id/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename)                                                                                                                                                                                                                      | 1.000 requisições por minuto.                                                                                                                                                                                                                                                                                                                                                                |
| [`/users/external_id/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove)                                                                                                                                                                                                                      | 1.000 requisições por minuto.                                                                                                                                                                                                                                                                                                                                                                |
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events)                                                                                                                                                                                                                                   | 1.000 requisições por hora, compartilhadas com o endpoint `/purchases/product_list`.                                                                                                                                                                                                                                                                                                              |
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id)                                                                                                                                                                                                                        | 1.000 requisições por hora, compartilhadas com o endpoint `/events/list`.                                                                                                                                                                                                                                                                                                                         |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics)                                                                                                                                                                                                                       | 50.000 requisições por minuto.                                                                                                                                                                                                                                                                                                                                                               |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)<br>[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)<br>[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)<br>[`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns)<br>[`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)                                                                                                                                                          | Para chamadas de broadcast (direcionamento amplo a Segments, filtros ou um público conectado), 250 requisições por minuto em todos os públicos, e 10 requisições por minuto por [público único]({{site.baseurl}}/api/api_limits#what-counts-as-the-same-unique-audience) (o que for atingido primeiro).<br><br>Caso contrário, ao direcionar destinatários individuais, a requisição é incluída no [limite de frequência compartilhado]({{site.baseurl}}/api/api_limits#requests-with-shared-rate-limits) de 250.000 requisições por hora.                                                                                                                                                                                                                    |
| [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids)                                                                                                                                                                                                                               | 100 requisições por dia.                                                                                                                                                                                                                                                                                                                                                                     |
| [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)                                                                                                                                                                                                                       | 5.000 requisições por minuto.                                                                                                                                                                                                                                                                                                                                                                |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center)<br>[`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center)                                                                            | 1.000 requisições por minuto.                                                                                                                                                                                                                                                                                                                                                 |
| [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center)                                                                                                                                                            | 10 requisições por minuto.                                                                                                                                                                                                                                                                                                                                                    |
| [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)                                                                                                                                                                             | 50 requisições por minuto compartilhadas entre os endpoints.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk)                                                                                                                             | 16.000 requisições por minuto compartilhadas entre os endpoints.                                                                                                                                                                                                                                                                                                                                  |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item) | 50 requisições por minuto compartilhadas entre os endpoints.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)<br>[`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)<br>[`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)<br>[`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | 50 requisições por minuto compartilhadas entre os endpoints. |
| [`/scim/v2/Users/{id}`]({{site.baseurl}}/get_see_user_account_information)<br>[`/scim/v2/Users?filter={userName@example.com}`]({{site.baseurl}}/get_search_existing_dashboard_user_email)<br>[`/scim/v2/Users/{id}`]({{site.baseurl}}/post_update_existing_user_account)<br>[`/scim/v2/Users/{id}}`]({{site.baseurl}}/delete_existing_dashboard_user)<br>[`/scim/v2/Users/`]({{site.baseurl}}/post_create_user_account)                                                                          | 20.000 requisições por dia, por empresa, compartilhadas entre os endpoints.                                                                                                                                                                                                                                                                                                                        |
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list)                                                                                                                                                                                                                              | 50 requisições por minuto.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status)                                                                                                                                                                                                        | 20 requisições por minuto.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync)                                                                                                                                                                                             | 100 requisições por minuto.                                                                                                                                                                                                                                                                                                                                                                  |
| [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | 100 requisições por hora. |
| [`/media_library/replace_file`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/replace_file) | 100 requisições por hora. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisições com limites de frequência diferentes" }

### Requisições com limites de frequência compartilhados {#requests-with-shared-rate-limits}

As seguintes requisições possuem um limite de frequência de 250.000 requisições por hora, compartilhado entre elas.

- [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key)
- [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys)
- [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details)
- [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) (apenas para chamadas que não sejam broadcast, ou seja, que especifiquem `external_user_ids` ou `aliases`)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns) (apenas para chamadas que não sejam broadcast)
- [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages)
- [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns)
- [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics)
- [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary)
- [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details)
- [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) (apenas para chamadas que não sejam broadcast)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases) (apenas para chamadas que não sejam broadcast)
- [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases)
- [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases)
- [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block)
- [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information)
- [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks)
- [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block)
- [`/email/blocklist`]({{site.baseurl}}/api/endpoints/email/post_blocklist)
- [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist)
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)
- [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status)
- [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses)
- [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics)
- [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date)
- [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days)
- [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date)
- [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date)
- [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start)
- [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) (apenas para chamadas que não sejam broadcast)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)
- [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages)
- [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages)
- [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled)
- [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics)
- [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details)
- [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment)
- [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics)
- [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics)
- [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers)
- [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers)
- [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status)
- [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups)
- [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template)
- [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information)
- [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates)
- [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group)
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

### O que conta como o mesmo público único? {#what-counts-as-the-same-unique-audience}

Isso se aplica aos seguintes endpoints: [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages), [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns), [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases), [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns) e [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases).

Para esses endpoints, as requisições de broadcast são consideradas como direcionadas ao mesmo público único quando todos os itens a seguir coincidem:

- A Campaign ou o Canvas sendo disparado (o `campaign_id` ou `canvas_id` na sua requisição de API, se especificado)
- O público sendo direcionado (os Segments ou filtros, ou para Campaigns de API, o `segment_id` na sua requisição de API)
- Os filtros de público conectado (o objeto `audience` na sua requisição de API, se especificado)

Cada combinação única desses atributos conta como um público distinto, então o limite de frequência adicional para cada público único se aplica a cada combinação de forma independente.

## Agrupamento de solicitações de API em lote {#batching-api-requests}

As APIs da Braze são projetadas para oferecer suporte ao agrupamento em lote (batching). Com o agrupamento em lote, a Braze pode receber o máximo de dados possível em uma única chamada de API, para que você não precise fazer muitas chamadas. É mais eficiente para a Braze processar dados em lotes do que processar dados uma chamada de cada vez. Por exemplo, processar 1.000 chamadas de API em lote requer menos recursos do que processar 75.000 chamadas individuais. O agrupamento em lote é extremamente importante para qualquer aplicação que possa exigir mais de 75.000 chamadas por hora.

{% alert note %}
Aumentos no limite de frequência da REST API são considerados com base na necessidade de clientes que estejam fazendo uso dos recursos de agrupamento em lote da API.
{% endalert %}

### Agrupamento de solicitações em lote para o endpoint Criar e atualizar usuários {#batch-user-track}

Cada solicitação `/users/track` pode conter até 75 objetos no total, combinados entre `attributes`, `events` e `purchases`. Cada objeto pode atualizar um usuário. Um único perfil de usuário pode ser atualizado por vários objetos.

{% details Limites de frequência legados %}
Para clientes com limites de frequência legados, cada array (`attributes`, `events` e `purchases`) pode conter até 75 objetos de forma independente, para um máximo combinado de até 225 objetos por solicitação.
{% enddetails %}

Para saber mais sobre os limites de frequência do `/users/track`, consulte [POST: Criar e atualizar usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

As solicitações feitas a esse endpoint geralmente começam a ser processadas nesta ordem:

1. Atributos
2. Eventos
3. Compras

### Agrupamento de solicitações de endpoints de envio de mensagens em lote {#batching-messaging-endpoint-requests}

Uma única solicitação aos [endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging) pode alcançar qualquer um dos seguintes:

- Até 50 `external_ids` específicos, cada um com parâmetros de mensagem individuais
- Um Segment de qualquer tamanho criado no dashboard da Braze, especificado pelo seu `segment_id`
- Usuários que correspondam a filtros de público adicionais de qualquer tamanho, definidos na solicitação como um objeto de [público conectado]({{site.baseurl}}/api/objects_filters/connected_audience)

### Exemplo de solicitação em lote {#example-batch-request}

O exemplo a seguir usa `external_id` para fazer uma única chamada de API para e-mail e SMS.

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@example.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@example.com"]
    }
  ]
}
```

## Monitorando seus limites de frequência {#monitoring-your-rate-limits}

Cada solicitação de API enviada à Braze retorna as seguintes informações nos cabeçalhos da resposta:

| Nome do cabeçalho       | Descrição                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | O número máximo de solicitações que você pode fazer em um intervalo especificado (seu limite de frequência). |
| `X-RateLimit-Remaining` | O número de solicitações restantes na janela atual do limite de frequência.                  |
| `X-RateLimit-Reset`     | O horário em que a janela atual do limite de frequência será redefinida, em segundos epoch UTC. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Monitorando seus limites de frequência" }

Essas informações são incluídas intencionalmente no cabeçalho da resposta à solicitação de API, e não no dashboard da Braze. Isso permite que seu sistema reaja melhor em tempo real enquanto você interage com nossa API. Por exemplo, se o valor de `X-RateLimit-Remaining` cair abaixo de um determinado limite, pode ser interessante reduzir a velocidade de envio para garantir que todos os e-mails de transação sejam entregues. Ou, se chegar a zero, pode ser necessário pausar todos os envios até que o tempo especificado em `X-RateLimit-Reset` tenha passado.

{% alert note %}
Os cabeçalhos HTTP serão retornados com todos os caracteres em letras minúsculas. Esse comportamento está alinhado com o protocolo HTTP/2, que exige que todos os nomes de campos de cabeçalho sejam em letras minúsculas. Isso difere do HTTP/1.X, em que os nomes dos cabeçalhos não diferenciavam maiúsculas de minúsculas, mas eram comumente escritos com diversas capitalizações.
{% endalert %}

Se você tiver dúvidas sobre limites de API, entre em contato com seu gerente de sucesso do cliente ou abra um [ticket de suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).

{% alert tip %}
Você pode usar o [dashboard de uso de API]({{site.baseurl}}/user_guide/analytics/dashboards/api_usage) para visualizar e comparar o tráfego de entrada em relação aos seus limites de frequência.
{% endalert %}

### Intervalo ideal entre endpoints {#optimal-delay-between-endpoints}

{% alert note %}
Recomendamos que você permita um intervalo de 5 minutos entre chamadas consecutivas a endpoints para minimizar erros.
{% endalert %}

Entender o intervalo ideal entre endpoints é crucial ao fazer chamadas consecutivas à API da Braze. Problemas surgem quando endpoints dependem do processamento bem-sucedido de outros endpoints e, se chamados cedo demais, podem gerar erros. Por exemplo, se você está atribuindo um alias a usuários pelo endpoint `/user/alias/new` e, em seguida, usando esse alias para enviar um evento personalizado pelo endpoint `/users/track`, quanto tempo você deve esperar?

Em condições normais, o tempo para que a consistência eventual dos nossos dados ocorra é de 10 a 100 ms (1/10 de segundo). No entanto, pode haver casos em que essa consistência leve mais tempo. Por isso, recomendamos que você permita um intervalo de 5 minutos entre chamadas subsequentes para minimizar a probabilidade de erro.

## Limites de tamanho da carga útil {#payload-size-limits}

As requisições à API da Braze estão sujeitas a limites de tamanho da carga útil, separados dos limites de frequência. A maioria dos endpoints aceita corpos de requisição de até 4&nbsp;MB. Quando uma requisição excede o limite aplicável, a Braze pode rejeitá-la com HTTP `413 Request Entity Too Large` ou HTTP `400 Bad Request`, dependendo do endpoint.

O endpoint [`/users/track/bulk`]({{site.baseurl}}/api/endpoints/user_data/post_user_track_bulk) tem um limite de carga útil de 2&nbsp;MB e retorna HTTP `400` quando o corpo da requisição excede esse limite. Para limites específicos de cada endpoint e tratamento de erros, consulte [Endpoints de dados de usuários]({{site.baseurl}}/api/endpoints/user_data).

### Redefinição do limite de frequência {#rate-limit-reset}

Os limites de frequência são redefinidos na hora cheia do relógio, não em uma janela contínua. Por exemplo, se o limite é de 250.000 requisições por hora, você poderia fazer 50.000 requisições entre 22h00 e 22h59 e outras 250.000 requisições entre 23h00 e 23h59, porque o contador é redefinido no início de cada hora.