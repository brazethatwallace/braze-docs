---
page_order: 10.9
nav_title: 문제 해결
article_title: Braze SDK의 푸시 알림 문제 해결
channel:
  - push notifications
---

# 푸시 알림 문제 해결 {#troubleshoot-push-notifications}

> Braze SDK의 푸시 알림 문제를 해결하는 방법을 알아보세요.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab fireos %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/push_notifications/troubleshooting.md %}
{% endsdktab %}
{% endsdktabs %}

## 푸시 알림의 줄 바꿈 {#push-linebreaks}

Liquid 태그를 사용하여 푸시 알림을 작성할 때, Liquid 태그에 인접한 줄 바꿈은 메시지가 전송되기 전에 자동으로 제거됩니다. [푸시 알림 작성기]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message)에서는 편집 중 메시지의 가독성을 유지하기 위해 이러한 줄 바꿈이 다시 추가됩니다. 메시지를 저장할 때 Liquid 태그 주변에 줄 바꿈이 표시되는 경우, 이는 정상적인 동작입니다.