<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "default" %}
Aplicamos o limite de frequência padrão da Braze de 250.000 solicitações por hora a esse endpoint, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!---PUT /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "update dashboard user" %}
Esse endpoint tem um limite de frequência de 5.000 solicitações por dia, por empresa. Esse limite de frequência é compartilhado com os endpoints `/scim/v2/Users/` GET, DELETE e POST, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!---GET /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "look up dashboard user" %}
Esse endpoint tem um limite de frequência de 5.000 solicitações por dia, por empresa. Esse limite de frequência é compartilhado com os endpoints `/scim/v2/Users/` PUT, GET, DELETE e POST, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!---DELETE /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "delete dashboard user" %}
Esse endpoint tem um limite de frequência de 5.000 solicitações por dia, por empresa. Esse limite de frequência é compartilhado com os endpoints `/scim/v2/Users/` PUT, GET e POST, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!---POST /scim/v2/Users--->
{% elsif include.endpoint == "create dashboard user" %}
Esse endpoint tem um limite de frequência de 5.000 solicitações por dia, por empresa. Esse limite de frequência é compartilhado com os endpoints `/scim/v2/Users/` PUT, GET e DELETE, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!---GET /scim/v2/Users--->
{% elsif include.endpoint == "look up dashboard user email" %}
Esse endpoint tem um limite de frequência de 5.000 solicitações por dia, por empresa. Esse limite de frequência é compartilhado com os endpoints `/scim/v2/Users/` PUT, GET, DELETE e POST, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!---/users/external_id/rename-->
<!---/users/external_id/remove-->

{% elsif include.endpoint == "external id migration" %}
Aplicamos um limite de frequência de 1.000 solicitações por minuto a esse endpoint, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!---/users/track-->

{% elsif include.endpoint == "users track" %}
Os limites de frequência desse endpoint variam de acordo com o seu contrato. Para clientes com pontos de dados em seus preços, a Braze aplica um limite de pico de 3.000 solicitações a cada três segundos. Para todos os outros clientes, os limites são configurados de acordo com os termos do seu contrato. Os limites atuais da sua conta podem ser encontrados no dashboard em **Configurações** > **APIs e identificadores** > **Dashboard de uso da API**.

Cada solicitação `/users/track` pode conter até 75 objetos no total, combinados entre `attributes`, `events` e `purchases`. Cada objeto pode atualizar um usuário. Um único perfil de usuário pode ser atualizado por múltiplos objetos.

Para clientes que adquiriram Monthly Active Users CY 24-25, Universal MAU, Web MAU ou Mobile MAU, limites de frequência adicionais se aplicam. Para saber mais, consulte [Limites do Monthly Active Users CY 24-25]({{site.baseurl}}/api/endpoints/user_data/post_user_track#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau).

{% details Limites de frequência legados %}
Para clientes com limites de frequência legados, cada solicitação `/users/track` pode conter até 75 objetos de atributo, 75 objetos de evento e 75 objetos de compra. Cada objeto pode atualizar um usuário, para um máximo combinado de até 225 objetos por solicitação. Um único perfil de usuário pode ser atualizado por múltiplos objetos.
{% enddetails %}

Para saber mais, consulte [Limites de frequência da API]({{site.baseurl}}/api/api_limits). Entre em contato com seu gerente de sucesso do cliente para solicitar um aumento.

<!---/users/export/ids-->

{% elsif include.endpoint == "users export ids" %}
Se sua integração com a Braze ocorreu em 22 de agosto de 2024 ou após essa data, esse endpoint tem um limite de frequência de 250 solicitações por minuto, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

Você também pode aumentar o limite de frequência desse endpoint para 40 solicitações por segundo atendendo aos seguintes requisitos:

- Seu espaço de trabalho tem o limite de frequência padrão (250 solicitações por minuto) ativado. Entre em contato com seu gerente de conta da Braze para mais assistência na remoção de qualquer limite de frequência pré-existente que você possa ter.
- Sua solicitação inclui o parâmetro `fields_to_export` para listar todos os campos que você deseja receber.

{% alert important %}
Se você incluir `canvases_received` ou `campaigns_received` no parâmetro `fields_to_export`, sua solicitação não será elegível para o limite de frequência mais rápido. Recomendamos incluir esses campos apenas se você tiver um caso de uso específico para eles.
{% endalert %}

<!---/users/delete-->

{% elsif include.endpoint == "users delete" %}
Aplicamos um limite de frequência compartilhado de 20.000 solicitações por minuto a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/users/alias/new`, `/users/identify`, `/users/merge` e `/users/alias/update`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!---/users/alias/new-->

{% elsif include.endpoint == "users alias new" %}
Aplicamos um limite de frequência compartilhado de 20.000 solicitações por minuto a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/users/delete`, `/users/identify`, `/users/merge` e `/users/alias/update`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!---/users/alias/update-->

{% elsif include.endpoint == "users alias update" %}
Aplicamos um limite de frequência compartilhado de 20.000 solicitações por minuto a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/users/delete`, `/users/alias/new`, `/users/identify` e `/users/merge`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!---/users/identify-->

{% elsif include.endpoint == "users identify" %}
Aplicamos um limite de frequência compartilhado de 20.000 solicitações por minuto a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/users/delete`, `/users/alias/new`, `/users/merge` e `/users/alias/update`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!---/users/merge-->

{% elsif include.endpoint == "users merge" %}
Aplicamos um limite de frequência compartilhado de 20.000 solicitações por minuto a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/users/delete`, `/users/alias/new`, `/users/identify` e `/users/alias/update`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!---/custom_attributes-->

{% elsif include.endpoint == "custom_attributes" %}
Aplicamos um limite de frequência compartilhado de 1.000 solicitações por hora a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/events`, `/events/list` e `/purchases/product_list`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!---/events-->

{% elsif include.endpoint == "events" %}
Aplicamos um limite de frequência compartilhado de 1.000 solicitações por hora a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/custom_attributes`, `/events/list` e `/purchases/product_list`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!---/events/list-->

{% elsif include.endpoint == "events list" %}
Aplicamos um limite de frequência compartilhado de 1.000 solicitações por hora a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/custom_attributes`, `/events` e `/purchases/product_list`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!---/purchases/product_list-->

{% elsif include.endpoint == "purchases product list" %}
Aplicamos um limite de frequência compartilhado de 1.000 solicitações por hora a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/custom_attributes`, `/events` e `/events/list`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "send endpoints" %}
Ao usar filtros de Connected Audience em sua solicitação, aplicamos um limite de frequência de 250 solicitações por minuto a esse endpoint. Caso contrário, se estiver especificando um `external_id`, esse endpoint tem um limite de frequência padrão de 250.000 solicitações por hora compartilhado entre os endpoints documentados em [Limites de frequência da API]({{site.baseurl}}/api/api_limits#requests-with-shared-rate-limits).

Os endpoints da Braze aceitam [solicitações de API em lote]({{site.baseurl}}/api/api_limits#batching-api-requests). Uma única solicitação para os endpoints de envio de mensagens pode alcançar qualquer um dos seguintes itens:

- Até 50 `external_ids` específicos, cada um com parâmetros de mensagem individuais
- Um segmento de público de qualquer tamanho, definido na solicitação como um objeto de [Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience)

<!---/transactional/v1/campaigns/{campaign_id}/send -->

{% elsif include.endpoint == "transactional email" %}
O endpoint `/transactional/v1/campaigns/{campaign_id}/send` é um endpoint pago em unidades por hora (por exemplo, 50.000 por hora, dependendo do seu pacote). Não há limite de frequência separado por endpoint: você pode enviar além do seu volume alocado, mas apenas o volume alocado é coberto pelo SLA. As solicitações para esse endpoint contam para o seu [limite geral de frequência da API externa]({{site.baseurl}}/api/api_limits). Se você exceder esse limite (por exemplo, 250.000 solicitações por hora em todos os endpoints), a Braze retorna 429 e as solicitações são limitadas. A contagem do volume transacional é redefinida a cada hora, então após uma hora, outra alocação fica disponível. Dentro do volume coberto pelo SLA, 99,9% dos e-mails serão enviados em menos de um minuto.

<!---POST /preference_center/v1 and PUT /preference_center/v1/{preferenceCenterExternalID}-->
{% elsif include.endpoint == "post or put preference center" %}
Esse endpoint tem um limite de frequência de 10 solicitações por minuto, por espaço de trabalho, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!---GET /preference_center/v1-->
{% elsif include.endpoint == "get preference center" %}
Esse endpoint tem um limite de frequência de 1.000 solicitações por minuto, por espaço de trabalho, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!---/sends/id/create-->

{% elsif include.endpoint == "sends id create" %}
Você pode criar até 100 identificadores de envio personalizados por dia usando esse endpoint para um determinado espaço de trabalho. Cada combinação de `send_id` e `campaign_id` que você criar contará para o seu limite diário. Os cabeçalhos de resposta para qualquer solicitação válida incluem o status atual do limite de frequência. Consulte [Limites de frequência da API]({{site.baseurl}}/api/api_limits) para mais detalhes.

<!---/subscription/status/set-->
{% elsif include.endpoint == "subscription status set" %}
Esse endpoint tem um limite de frequência de 5.000 solicitações por minuto compartilhado entre os endpoints `/subscription/status/set` e `/v2/subscription/status/set`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

<!-- Add this phrase back ", as documented in [API rate limits]({{site.baseurl}}/api/api_limits)" to CDI endpoints for GA -->

<!---GET /cdi/integrations--->
{% elsif include.endpoint == "cdi list integrations" %}
Esse endpoint tem um limite de frequência de 50 solicitações por minuto.

<!---POST /cdi/integrations/{integration_id}/sync--->
{% elsif include.endpoint == "cdi job sync" %}
Esse endpoint tem um limite de frequência de 20 solicitações por minuto.

<!---POST /cdi/integrations/{integration_id}/job_sync_status--->
{% elsif include.endpoint == "cdi job sync status" %}
Esse endpoint tem um limite de frequência de 100 solicitações por minuto.

<!---/media_library/create, /media_library/replace_file--->
{% elsif include.endpoint == "media_library" %}
Esse endpoint tem um limite de frequência de 100 solicitações por hora, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "message endpoints" %}

Os endpoints da Braze aceitam [solicitações de API em lote]({{site.baseurl}}/api/api_limits#batching-api-requests). Uma única solicitação para os endpoints de envio de mensagens pode alcançar qualquer um dos seguintes itens:

- Até 50 `external_ids` específicos, cada um com parâmetros de mensagem individuais
- Um segmento de qualquer tamanho criado no dashboard da Braze, especificado por seu `segment_id`
- Um segmento de público de qualquer tamanho, definido na solicitação como um objeto de [Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience)

{% endif %}

{% if include.category == "send messages endpoints" %}

Os endpoints da Braze aceitam [solicitações de API em lote]({{site.baseurl}}/api/api_limits#batching-api-requests). Uma única solicitação para os endpoints de envio de mensagens pode alcançar qualquer um dos seguintes itens:

- Até 50 `external_ids` específicos, cada um com parâmetros de mensagem individuais
- Um segmento de público de qualquer tamanho, definido na solicitação como um objeto de [Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience)

{% endif %}

<!---Additional if statement for Translation endpoints-->

{% if include.endpoint == "translation endpoints" %}

Esse endpoint tem um limite de frequência de 250.000 solicitações por minuto.

{% endif %}

<!---Additional if statement for /messages/send endpoint-->

{% if include.category == "message send endpoint" %}

Os endpoints da Braze aceitam [solicitações de API em lote]({{site.baseurl}}/api/api_limits#batching-api-requests). Uma única solicitação para os endpoints de envio de mensagens pode alcançar qualquer um dos seguintes itens:

- Até 50 `external_ids` específicos
- Um segmento de qualquer tamanho criado no dashboard da Braze, especificado por seu `segment_id`
- Um segmento de público de qualquer tamanho, definido na solicitação como um objeto de [Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience)

{% endif %}

{% if include.endpoint == "asynchronous catalog item" %}

Esse endpoint tem um limite de frequência compartilhado de 16.000 solicitações por minuto entre todos os endpoints assíncronos de itens de catálogo, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

{% endif %}

{% if include.endpoint == "synchronous catalog item" %}

Esse endpoint tem um limite de frequência compartilhado de 50 solicitações por minuto entre todos os endpoints síncronos de itens de catálogo, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

{% endif %}

{% if include.endpoint == "synchronous catalog" %}

Esse endpoint tem um limite de frequência compartilhado de 50 solicitações por minuto entre todos os endpoints de catálogo síncronos, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

{% endif %}

{% if include.endpoint == "asynchronous catalog fields" or include.endpoint == "asynchronous catalog selections" %}

Esse endpoint tem um limite de frequência compartilhado de 50 solicitações por minuto entre todos os endpoints assíncronos de campos e seleções de catálogo, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits).

{% endif %}

{% if include.endpoint == "export campaign analytics" %}

Esse endpoint tem um limite de frequência de 50.000 solicitações por minuto.

{% endif %}