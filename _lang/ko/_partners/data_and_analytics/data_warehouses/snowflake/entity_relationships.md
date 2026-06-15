---
nav_title: "엔티티 관계"
article_title: Snowflake와 Braze의 엔티티 관계
page_order: 10
search_tag: Partner
---

# Snowflake와 Braze의 엔티티 관계 {#entity-relationships-for-snowflake-and-braze}

> 각 메시징 채널에 대한 Snowflake와 Braze 간의 엔티티 관계 목록입니다.

{% alert important %}
엔티티 관계 다이어그램은 테이블 간의 공유 필드와 관계를 강조하며, 전체 테이블 스키마가 아닙니다. 전체 필드 목록은 [개별 테이블 스키마]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt)를 참조하세요.
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