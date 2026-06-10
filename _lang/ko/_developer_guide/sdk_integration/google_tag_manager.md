---
nav_title: Google 태그 관리자
article_title: Google Tag Manager와 Braze SDK 사용하기
platform:
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "런타임 초기화, 지연 초기화 또는 Google Tag Manager와 같은 방법을 사용하여 Braze SDK를 초기화하는 방법을 알아보세요."

---

# Google Tag Manager와 Braze SDK 사용하기 {#google-tag-manager-with-the-braze-sdk}

> [Google Tag Manager(GTM)](https://developers.google.com/tag-platform/tag-manager)를 Braze SDK와 함께 사용하는 방법을 알아보세요. 이를 통해 코드 변경이나 새로운 앱 릴리스 없이 Braze 이벤트 추적 및 사용자 속성 업데이트를 원격으로 제어할 수 있습니다.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/google_tag_manager.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/google_tag_manager.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/google_tag_manager.md %}
{% endsdktab %}
{% endsdktabs %}

## 문제 해결 {#troubleshooting}

Braze가 초기화되지 않거나 이벤트가 예상대로 표시되지 않는 경우, GTM 컨테이너가 게시되었는지, 트리거 및 태그 실행 순서가 SDK [라이프사이클 및 초기화 전략]({{site.baseurl}}/developer_guide/sdk_integration/)과 일치하는지, 테스트 기기가 Braze 엔드포인트를 차단하고 있지 않은지 확인하세요.

초기화 실패의 경우, Braze 태그 또는 커스텀 태그 제공업체가 예상되는 `actionType` 및 파라미터를 수신하는지 확인하세요(이 페이지의 Android, Swift, 웹 탭 참조). GTM에서 실행된 이벤트를 검증하는 동안 상세 로깅을 활성화하려면 해당 탭에서 링크된 플랫폼 통합 가이드에 설명된 대로 플랫폼의 SDK 디버그 로깅을 활성화하세요.