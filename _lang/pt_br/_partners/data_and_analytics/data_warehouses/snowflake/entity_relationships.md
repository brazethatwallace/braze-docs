---
nav_title: "Relacionamentos entre entidades"
article_title: Relacionamentos de entidades para Snowflake e Braze
page_order: 10
search_tag: Partner
---

# Relacionamentos de entidades para Snowflake e Braze {#entity-relationships-for-snowflake-and-braze}

> Esta é a lista de relacionamentos de entidades entre o Snowflake e a Braze para cada canal de envio de mensagens.

{% alert important %}
Os diagramas de relacionamento de entidades destacam campos compartilhados e relacionamentos entre tabelas, e não são esquemas completos de tabelas. Para uma lista completa de campos, consulte os [esquemas individuais de tabelas]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt).
{% endalert %}

{% sdktabs %}
{% sdktab Content Cards %}
{% multi_lang_include snowflake_users_messages/contentcard.md %}
{% endsdktab %}

{% sdktab Email %}
{% multi_lang_include snowflake_users_messages/email.md %}
{% endsdktab %}

{% sdktab Feature Flags %}
{% multi_lang_include snowflake_users_messages/featureflag.md %}
{% endsdktab %}

{% sdktab In-App Messages %}
{% multi_lang_include snowflake_users_messages/inappmessage.md %}
{% endsdktab %}

{% sdktab Push Notifications %}
{% multi_lang_include snowflake_users_messages/pushnotification.md %}
{% endsdktab %}

{% sdktab SMS %}
{% multi_lang_include snowflake_users_messages/sms.md %}
{% endsdktab %}

{% sdktab Webhook %}
{% multi_lang_include snowflake_users_messages/webhook.md %}
{% endsdktab %}

{% sdktab WhatsApp %}
{% multi_lang_include snowflake_users_messages/whatsapp.md %}
{% endsdktab %}
{% endsdktabs %}