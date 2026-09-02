---
nav_title: FAQ
article_title: 자주 묻는 질문
page_order: 50
description: "이 페이지에서는 기능 플래그에 대해 자주 묻는 질문에 대한 답변을 제공합니다."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web
---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 문서에서는 기능 플래그에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## 기능 및 지원 {#functionality-and-support}

### Braze 기능 플래그는 어떤 플랫폼에서 지원되나요? {#platforms}

Braze는 다음 SDK 버전 요구 사항에 따라 iOS, Android, 웹 플랫폼에서 기능 플래그를 지원합니다:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

다른 플랫폼에 대한 지원이 필요하신가요? 저희 팀에 이메일을 보내주세요: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### 기능 플래그를 구현할 때 필요한 작업 수준은 어느 정도인가요? {#level-of-effort}

기능 플래그는 몇 분 안에 생성하고 통합할 수 있습니다.

대부분의 작업은 엔지니어링 팀이 출시할 새로운 기능을 구축하는 데 관련됩니다. 하지만 기능 플래그를 추가하는 것은 앱이나 웹사이트 코드에서 `IF`/`ELSE` 구문을 작성하는 것만큼 간단합니다:

{% tabs %}
{% tab JavaScript %}

```javascript
import { getFeatureFlag } from "@braze/web-sdk";

if (getFeatureFlag("new_shopping_cart").enabled) {
    // Show the new homepage your team has built
}
else {
    // Show the old homepage
}
```

{% endtab %}
{% tab Java %}

```java
if (braze.getFeatureFlag("new_shopping_cart").getEnabled()) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
if (braze.getFeatureFlag("new_shopping_cart")?.enabled == true) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% endtabs %}

### 기능 플래그는 마케팅 팀에 어떤 도움이 되나요? {#marketing-teams}

마케팅 팀은 기능이 소수의 사용자에게만 활성화된 상태에서 제품 발표(예: 제품 출시 이메일)를 조율하기 위해 기능 플래그를 사용할 수 있습니다.

예를 들어, Braze 기능 플래그를 사용하면 앱 사용자의 10%에게 새로운 고객 로열티 프로그램을 출시하고, Canvas 기능 플래그 단계를 사용하여 동일한 10%의 활성화된 사용자에게 이메일, 푸시 또는 기타 메시지를 보낼 수 있습니다.

### 기능 플래그는 프로덕트 팀에 어떤 도움이 되나요? {#product-teams}

프로덕트 팀은 기능 플래그를 사용하여 새로운 기능의 점진적 출시 또는 소프트 런칭을 수행하고, 모든 사용자에게 제공하기 전에 KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or 핵심 성과 지표(KPI or 핵심 성과 지표(KPI))와 고객 피드백을 모니터링할 수 있습니다.

프로덕트 팀은 [기능 플래그 속성]({{site.baseurl}}/developer_guide/feature_flags/create#accessing-properties)을 사용하여 딥링크, 텍스트, 이미지 또는 기타 동적 콘텐츠와 같은 앱 내 콘텐츠를 원격으로 채울 수 있습니다.

Canvas 기능 플래그 단계를 사용하면 프로덕트 팀은 A/B 분할 테스트를 실행하여 새로운 기능이 기능이 비활성화된 사용자 대비 전환율에 어떤 영향을 미치는지 측정할 수도 있습니다.

### 기능 플래그는 엔지니어링 팀에 어떤 도움이 되나요? {#engineering-teams}

엔지니어링 팀은 기능 플래그를 사용하여 새로운 기능 출시에 내재된 위험을 줄이고, 한밤중에 급하게 코드 수정을 배포하는 상황을 방지할 수 있습니다.

기능 플래그 뒤에 새로운 코드를 숨겨서 배포하면, 팀은 새 코드를 푸시하거나 앱 스토어 업데이트 승인을 기다리는 지연 없이 Braze 대시보드에서 원격으로 기능을 켜거나 끌 수 있습니다.

## 기능 출시 및 타겟팅 {#feature-rollouts-and-targeting}

### 기능 플래그를 특정 사용자 그룹에만 출시할 수 있나요? {#target-users}

네, Braze에서 이메일 주소, `user_id` 또는 고객 프로필의 기타 속성을 기준으로 특정 사용자를 타겟팅하는 Segment를 생성하세요. 그런 다음 해당 Segment의 100%에 기능 플래그를 배포합니다.

### 출시 비율을 조정하면 이전에 활성화 그룹에 버킷된 사용자에게 어떤 영향이 있나요? {#random-buckets}

기능 플래그 출시는 기기 및 세션 전반에서 사용자에게 일관되게 유지됩니다.

- 기능 플래그가 무작위 사용자의 10%에게 출시되면, 해당 10%는 활성화 상태로 유지되며 해당 기능 플래그의 수명 기간 동안 지속됩니다.
- 출시를 10%에서 20%로 늘리면 동일한 10%는 활성화 상태로 유지되고, 새로운 추가 10%의 사용자가 활성화 그룹에 추가됩니다.
- 출시를 20%에서 10%로 줄이면 원래의 10% 사용자만 활성화 상태로 유지됩니다.

이 전략은 사용자가 앱에서 일관된 경험을 제공받고 세션 간에 상태가 왔다 갔다 변경되지 않도록 하는 데 도움이 됩니다. 물론 기능을 0%로 비활성화하면 기능 플래그에서 모든 사용자가 제거되며, 이는 버그를 발견하거나 기능을 완전히 비활성화해야 할 때 유용합니다.

## 기술 관련 주제 {#technical-topics}

### 기능 플래그를 사용하여 Braze SDK 초기화 시점을 제어할 수 있나요? {#initialization}

아니요, SDK는 현재 사용자의 기능 플래그를 다운로드하고 동기화하기 위해 초기화되어야 합니다. 따라서 기능 플래그를 사용하여 Braze에서 생성되거나 추적되는 사용자를 제한할 수 없습니다.

### SDK는 얼마나 자주 기능 플래그를 새로고침하나요? {#refresh-frequency}

기능 플래그는 세션 시작 시 및 활성 사용자를 변경할 때 새로고침됩니다. 또한 SDK의 [새로고침 메서드]({{site.baseurl}}/developer_guide/feature_flags/create#refreshing)를 사용하여 수동으로 새로고침할 수도 있습니다. 기능 플래그 새로고침은 5분에 한 번으로 사용량 제한이 적용됩니다(변경될 수 있음).

올바른 데이터 사용 관행에 따라 기능 플래그를 너무 빈번하게 새로고침하지 않는 것이 좋습니다(너무 자주 수행하면 사용량 제한이 적용될 수 있음). 따라서 사용자가 새로운 기능과 상호 작용하기 전에 새로고침하거나, 필요한 경우 앱 내에서 주기적으로 새로고침하는 것이 가장 좋습니다.

### 사용자가 오프라인 상태일 때 기능 플래그를 사용할 수 있나요? {#offline}

네, 기능 플래그가 새로고침된 후에는 사용자의 기기에 로컬로 저장되며 오프라인 상태에서도 접근할 수 있습니다.

### 세션 중간에 기능 플래그가 새로고침되면 어떻게 되나요? {#listen-for-updates}

기능 플래그는 세션 중간에 새로고침될 수 있습니다. 특정 변수나 구성이 변경되어야 할 때 앱을 업데이트하고 싶은 경우가 있을 수 있습니다. 반면에, UI 렌더링 방식이 갑자기 변경되는 것을 방지하기 위해 앱을 업데이트하지 않으려는 경우도 있습니다.

이를 제어하려면, 기능 플래그의 [업데이트를 수신]({{site.baseurl}}/developer_guide/feature_flags/create#updates)하고 어떤 기능 플래그가 변경되었는지에 따라 앱을 다시 렌더링할지 결정하세요.

### 글로벌 컨트롤 그룹에 속한 사용자가 기능 플래그 실험을 수신하지 못하는 이유는 무엇인가요? {#why-arent-users-in-my-global-control-group-receiving-feature-flags-experiments}

[글로벌 컨트롤 그룹]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts)에 속한 사용자에 대해서는 기능 플래그를 활성화할 수 없습니다. 이는 글로벌 컨트롤 그룹의 사용자가 기능 플래그 실험에 참여할 수 없음을 의미합니다.

### 이메일 기반 수신자 식별은 Braze 기능 플래그에 포함되나요? {#is-email-based-recipient-identification-part-of-braze-feature-flags}

아니요. 메시지를 발송할 때 이메일로 수신자를 식별하는 것은 이 페이지의 기능 플래그 제품에 포함되지 않습니다. 기능 플래그는 Braze SDK를 통해 앱 내 또는 사이트 내 경험을 제어합니다.

API 트리거 Campaign 및 Canvas 발송 시 `external_user_id` 대신 [수신자 객체]({{site.baseurl}}/api/objects_filters/recipient_object)에 `email`을 포함할 수 있습니다. `email`을 사용하는 경우, Braze가 일치하는 사용자 프로필을 선택할 수 있도록 `prioritization`을 포함하세요. 이 발송 옵션은 모든 워크스페이스에서 사용할 수 있는 것은 아닙니다.

요청 형식에 대해서는 [POST: API 트리거 전달을 사용하여 Campaign 발송]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) 및 [POST: API 트리거 전달을 사용하여 Canvas 메시지 발송]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)을 참조하세요.

## 추가 질문이 있으신가요? {#additional-questions}

질문이나 피드백이 있으시면 저희 팀에 이메일을 보내주세요: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).