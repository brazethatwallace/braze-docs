---
page_order: 6
nav_title: 소프트 푸시 프롬프트
article_title: 웹용 소프트 푸시 프롬프트
description: "Braze 웹 SDK에서 브라우저 기본 알림 권한 프롬프트 전에 소프트 푸시 프롬프트를 설정하는 방법을 알아보세요."
channel:
  - push notifications
---

# 웹용 소프트 푸시 프롬프트 {#soft-push-prompts-for-web}

> 소프트 푸시 프롬프트는 브라우저의 기본 알림 권한 프롬프트가 표시되기 전에 보여주는 커스텀 메시지입니다. 사용자에게 푸시 알림을 활성화해야 하는 이유를 설명하고, 첫 방문 시 시스템 프롬프트를 바로 표시하는 것보다 옵트인 비율을 높일 수 있습니다. 이 가이드에서는 Braze 웹 SDK로 소프트 푸시 프롬프트를 구현하는 방법을 다루며, 프롬프트를 트리거하는 시점, 메시지 콘텐츠를 커스터마이징하는 방법, 사용자가 푸시의 가치를 이해한 후 요청 타이밍에 대한 모범 사례를 포함합니다.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications/soft_push_prompts.md %}
{% endsdktab %}
{% endsdktabs %}

## 자주 묻는 질문 {#frequently-asked-questions}

### 소프트 푸시 프롬프트란 무엇인가요? {#what-is-a-soft-push-prompt}

소프트 푸시 프롬프트는 브라우저의 기본 알림 권한 대화 상자가 표시되기 전에 보여주는 커스텀 인앱 또는 온사이트 메시지입니다. 푸시의 가치를 설명하여 시스템 프롬프트가 나타났을 때 사용자가 수락할 가능성을 높여줍니다.

### 소프트 푸시 프롬프트를 언제 표시해야 하나요? {#when-should-i-show-a-soft-push-prompt}

사용자가 제품의 가치를 이해한 후에 소프트 푸시 프롬프트를 표시하세요. 예를 들어, 온보딩을 완료한 후 또는 의미 있는 인앱 액션을 수행한 후가 적절하며, 첫 페이지 로드 시에는 표시하지 않는 것이 좋습니다. 구현 세부 사항은 이 가이드의 웹 SDK 단계를 참조하세요.