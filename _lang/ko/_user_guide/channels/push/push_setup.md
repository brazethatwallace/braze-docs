---
nav_title: "설정"
article_title: 푸시 설정
page_order: 0
layout: dev_guide
guide_top_header: "푸시 설정"
guide_top_text: "푸시 토큰 수명 주기와 구독 상태를 이해하여 푸시 알림이 적절한 사용자에게 도달하도록 하세요."

page_type: landing
description: "Braze에서 푸시 알림을 위한 푸시 토큰 수명 주기와 구독 상태에 대해 알아보세요."

guide_featured_title: "섹션 문서"
guide_featured_list:
  - name: 푸시 토큰 수명 주기
    link: /docs/user_guide/channels/push/push_setup/push_token_lifecycle
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: 푸시 구독 상태
    link: /docs/user_guide/channels/push/push_setup/push_subscription_states
    image: /assets/img/braze_icons/users-01.svg
---

## 사전 요구 사항 {#prerequisites}

Braze를 사용하여 푸시 메시지를 만들고 보내려면 먼저 개발자와 협력하여 웹사이트 또는 앱에 푸시를 통합해야 합니다. 자세한 단계는 각 플랫폼의 통합 가이드를 참조하세요:

- [iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android)
- [웹]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web)

## 푸시 프라이밍 {#push-priming}

사용자가 메시지를 받으려면 푸시에 옵트인해야 한다는 점을 기억하세요. 따라서 인앱 메시지를 활용하여 푸시 알림을 보내려는 이유와 푸시를 활성화하면 어떤 이점이 있는지 고객에게 설명하는 것이 좋습니다. 이 과정을 [푸시 프라이밍]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)이라고 합니다.