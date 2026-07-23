---
nav_title: 푸시 알림
article_title: Braze SDK를 통해 푸시 알림 데이터 기록하기
page_order: 7.2
description: "Braze SDK를 통해 푸시 알림 데이터를 기록하는 방법을 알아보세요."
noindex: true
---

# 푸시 알림 데이터 기록하기 {#log-push-notification-data}

> Braze SDK를 통해 푸시 알림 데이터를 기록하는 방법을 알아보세요.

{% sdktabs %}
{% sdktab android %}
## Braze API를 사용한 데이터 기록(권장) {#logging-data-with-the-braze-api-recommended}

[`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 호출하여 실시간으로 분석 데이터를 기록할 수 있습니다. 분석 데이터를 기록하려면 Braze 대시보드에서 `braze_id` 값을 전송하여 업데이트할 고객 프로필을 식별합니다.

![개인화된 푸시 대시보드 예시]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:79%;"}

## 수동으로 데이터 기록하기 {#manually-logging-data}

페이로드의 세부 사항에 따라 `FirebaseMessagingService.onMessageReceived` 구현 또는 시작 액티비티 내에서 수동으로 분석 데이터를 기록할 수 있습니다. `FirebaseMessagingService` 서브클래스는 Android 시스템에 의해 [플래그 지정되거나 종료](https://firebase.google.com/docs/cloud-messaging/android/receive)되지 않도록 호출 후 9초 이내에 실행을 완료해야 합니다.

{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/analytics/logging_push_data.md %}
{% endsdktab %}
{% endsdktabs %}