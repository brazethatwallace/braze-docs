---
nav_title: "エンティティのリレーションシップ"
article_title: SnowflakeとBrazeのエンティティのリレーションシップ
page_order: 10
search_tag: Partner
---

# SnowflakeとBrazeのエンティティのリレーションシップ {#entity-relationships-for-snowflake-and-braze}

> 各メッセージングチャネルにおけるSnowflakeとBrazeの間のエンティティリレーションシップの一覧です。

{% alert important %}
エンティティリレーションシップ図は、テーブル間の共有フィールドとリレーションシップを示したものであり、完全なテーブルスキーマではありません。フィールドの完全なリストについては、[個別のテーブルスキーマ]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt)を参照してください。
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