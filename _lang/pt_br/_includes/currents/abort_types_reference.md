A tabela a seguir lista os possíveis valores de `abort_type`. Um tipo de interrupção descreve o motivo específico pelo qual uma mensagem não foi enviada.

{% if include.channel %}
{% assign ch = include.channel %}
{% else %}
{% assign ch = "all" %}
{% endif %}

### Geral {#general}

Esses tipos de interrupção podem ocorrer em qualquer canal de envio de mensagens.

| Valor de `abort_type` | Descrição |
| --- | --- |
| `liquid_abort_message` | A Liquid tag [abort_message]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) foi chamada, então o envio foi cancelado. |
| `template_parse_error` | O modelo de mensagem não pôde ser analisado devido a um erro de sintaxe ou renderização, então o envio foi cancelado. |
| `rate_limit` | A mensagem foi cancelada porque excedeu o [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) configurado. |
| `campaign_disabled` | A Campaign foi desativada antes que a mensagem pudesse ser enviada. |
| `campaign_does_not_exist` | A Campaign associada a esta mensagem não existe mais. |
| `campaign_action_does_not_exist` | A ação de Campaign associada a esta mensagem não existe mais. |
| `message_variation_does_not_exist` | A variação de mensagem atribuída a este usuário não existe mais. |
| `user_not_in_segment` | O usuário não está no Segment de destino, então a mensagem não foi enviada. |
| `trigger_event_blacklisted` | O evento-gatilho está na lista de proibições, então a mensagem não foi enviada. |
| `exhausted_retries` | A mensagem não pôde ser enviada após o número máximo de tentativas. |
| `frequency_capped` | O usuário já recebeu o número máximo de mensagens permitido pelas regras de [limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#about-frequency-capping) do seu espaço de trabalho. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Geral" }

{% unless ch == "newsfeedcard" or ch == "rcs" %}

### Conteúdo e renderização {#content-and-rendering}

{% if include.combined_content_rendering %}

| Valor de `abort_type` | Descrição |
| --- | --- |
| `exhausted_cc_retries` | O Connected Content falhou após o número máximo de tentativas, então a mensagem foi cancelada. |
| `connected_content_not_supported` | O [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) não é compatível neste contexto, então a mensagem foi cancelada. |
| `promo_codes_not_supported` | Códigos de promoção não são compatíveis neste contexto, então a mensagem foi cancelada. |
| `catalog_items_rerender_not_supported` | A re-renderização de itens do catálogo não é compatível neste contexto, então a mensagem foi cancelada. |
| `blacklisted_media_url` | A URL de mídia está na lista de proibições e não pode ser usada em mensagens. |
| `blocked_media_url` | A URL de mídia foi bloqueada por políticas de segurança. |
| `invalid_media_url` | A URL de mídia não é válida ou não pôde ser resolvida. |
| `ssl_error` | Ocorreu um erro de SSL ao fazer uma solicitação. |
| `invalid_http_status` | Uma solicitação HTTP retornou um código de status sem sucesso. |
| `http_timeout` | Uma solicitação HTTP expirou antes de receber uma resposta. |
| `missing_hostname` | A URL da solicitação não contém um hostname. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conteúdo e renderização" }

{% else %}

| Valor de `abort_type` | Descrição |
| --- | --- |
| `exhausted_cc_retries` | O Connected Content falhou após o número máximo de tentativas, então a mensagem foi cancelada. |
| `connected_content_not_supported` | O [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) não é compatível neste contexto, então a mensagem foi cancelada. |
| `promo_codes_not_supported` | Códigos de promoção não são compatíveis neste contexto, então a mensagem foi cancelada. |
| `catalog_items_rerender_not_supported` | A re-renderização de itens do catálogo não é compatível neste contexto, então a mensagem foi cancelada. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conteúdo e renderização" }

{% endif %}

{% if ch == "all" or ch == "email" or ch == "push" or ch == "inappmessage" or ch == "contentcard" or ch == "webhook" or ch == "banner" %}
{% unless include.combined_content_rendering %}

| Valor de `abort_type` | Descrição |
| --- | --- |
| `exhausted_cc_retries` | O Connected Content falhou após o número máximo de tentativas, então a mensagem foi cancelada. |
| `connected_content_not_supported` | O [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) não é compatível neste contexto, então a mensagem foi cancelada. |
| `promo_codes_not_supported` | Códigos de promoção não são compatíveis neste contexto, então a mensagem foi cancelada. |
| `catalog_items_rerender_not_supported` | A re-renderização de itens do catálogo não é compatível neste contexto, então a mensagem foi cancelada. |
| `blacklisted_media_url` | A URL de mídia está na lista de proibições e não pode ser usada em mensagens. |
| `blocked_media_url` | A URL de mídia foi bloqueada por políticas de segurança. |
| `invalid_media_url` | A URL de mídia não é válida ou não pôde ser resolvida. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URLs de mídia de conteúdo e renderização" }

{% endunless %}
{% endif %}

{% if ch == "all" or ch == "email" or ch == "webhook" %}
{% unless include.combined_content_rendering %}

| Valor de `abort_type` | Descrição |
| --- | --- |
| `exhausted_cc_retries` | O Connected Content falhou após o número máximo de tentativas, então a mensagem foi cancelada. |
| `connected_content_not_supported` | O [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) não é compatível neste contexto, então a mensagem foi cancelada. |
| `promo_codes_not_supported` | Códigos de promoção não são compatíveis neste contexto, então a mensagem foi cancelada. |
| `catalog_items_rerender_not_supported` | A re-renderização de itens do catálogo não é compatível neste contexto, então a mensagem foi cancelada. |
| `ssl_error` | Ocorreu um erro de SSL ao fazer uma solicitação. |
| `invalid_http_status` | Uma solicitação HTTP retornou um código de status sem sucesso. |
| `http_timeout` | Uma solicitação HTTP expirou antes de receber uma resposta. |
| `missing_hostname` | A URL da solicitação não contém um hostname. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTTP e SSL de conteúdo e renderização" }

{% endunless %}
{% endif %}

{% endunless %}

{% if ch == "all" or ch == "email" %}

### E-mail {#email}

| Valor de `abort_type` | Descrição |
| --- | --- |
| `exhausted_link_shortening_retries` | O encurtamento de link falhou após o número máximo de tentativas. |
| `missing_email` | O usuário não tem um endereço de e-mail no perfil. |
| `invalid_domain` | O endereço de e-mail tem um domínio inválido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="E-mail" }

{% endif %}

{% if ch == "all" or ch == "push" %}

### Push

| Valor de `abort_type` | Descrição |
| --- | --- |
| `invalid_push_payload` | A carga útil da notificação por push é inválida ou está malformada. |
| `sdk_not_supported` | A versão do SDK no dispositivo do usuário não é compatível com esse tipo de notificação por push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push" }

{% endif %}

{% if ch == "all" or ch == "sms" %}

### SMS/MMS

| Valor de `abort_type` | Descrição |
| --- | --- |
| `exhausted_link_shortening_retries` | O encurtamento de link falhou após o número máximo de tentativas. |
| `sms_empty_payload` | O corpo da mensagem SMS está vazio. |
| `sms_no_sending_numbers` | Não há números de telefone de envio disponíveis para este grupo de inscrições. |
| `sms_fatal_provider_error` | Ocorreu um erro fatal com o provedor de SMS, impedindo a entrega da mensagem. |
| `sms_gateway_domain_not_allowed` | O domínio do gateway SMS não está na lista de permissões. |
| `blocked_recipient_country` | O número de telefone do destinatário está em um país bloqueado pelas suas [permissões geográficas]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions). |
| `mms_not_supported` | MMS não é compatível com este destinatário ou número de envio. |
| `no_current_messaging_service` | Nenhum serviço de envio de mensagens ativo está configurado para este grupo de inscrições. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS/MMS" }

{% endif %}

{% if ch == "all" or ch == "whatsapp" %}

### WhatsApp

| Valor de `abort_type` | Descrição |
| --- | --- |
| `whats_app_no_sending_numbers` | Não há números de telefone de envio disponíveis para este grupo de inscrições do WhatsApp. |
| `whats_app_invalid_template_message` | O modelo de mensagem do WhatsApp é inválido ou não foi aprovado. |
| `whats_app_invalid_response_message` | A mensagem de resposta do WhatsApp é inválida. |
| `whats_app_fatal_provider_error` | Ocorreu um erro fatal com o provedor do WhatsApp, impedindo a entrega da mensagem. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="WhatsApp" }

{% endif %}

{% if ch == "all" or ch == "line" %}

### LINE

| Valor de `abort_type` | Descrição |
| --- | --- |
| `line_fatal_provider_error` | Ocorreu um erro fatal com o provedor do LINE, impedindo a entrega da mensagem. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE" }

{% endif %}

{% if ch == "all" or ch == "kakao" %}

### Kakao

| Valor de `abort_type` | Descrição |
| --- | --- |
| `kakao_fatal_provider_error` | Ocorreu um erro fatal com o provedor do Kakao, impedindo a entrega da mensagem. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Kakao" }

{% endif %}

{% if ch == "all" or ch == "contentcard" %}

### Content Cards

| Valor de `abort_type` | Descrição |
| --- | --- |
| `content_card_size_exceeded` | A carga útil do Content Card excede o limite máximo de tamanho (2 KB). |
| `content_card_content_invalid` | O conteúdo do Content Card é inválido ou contém caracteres não compatíveis. |
| `content_card_expiration_invalid` | A data de expiração do Content Card é inválida. |
| `content_card_general` | O Content Card não pôde ser criado devido a um erro geral. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Cards" }

{% endif %}

{% if ch == "all" or ch == "inappmessage" %}

### Mensagens no app {#in-app-messages}

| Valor de `abort_type` | Descrição |
| --- | --- |
| `no_longer_in_availability_window` | A mensagem não pôde ser enviada dentro do período de disponibilidade configurado, então foi cancelada. |
| `maximum_impressions_reached` | A mensagem no app já atingiu o número máximo de impressões. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mensagens no app" }

{% endif %}

{% if ch == "all" or ch == "webhook" %}

### Webhooks

| Valor de `abort_type` | Descrição |
| --- | --- |
| `blocked_webhook_url` | A URL do webhook foi bloqueada por políticas de segurança. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhooks" }

{% endif %}