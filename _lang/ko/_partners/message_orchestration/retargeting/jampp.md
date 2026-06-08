---
nav_title: Jampp
article_title: Jampp
alias: /partners/jampp/
description: "이 참조 문서에서는 모바일 고객 확보 및 리타겟팅에 사용되는 성과 마케팅 플랫폼인 Jampp와 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Jampp

> [Jampp](https://www.jampp.com/)는 모바일 고객 확보 및 리타겟팅에 사용되는 성과 마케팅 플랫폼입니다. Jampp는 행동 데이터와 예측 및 프로그래매틱 기술을 결합하여 소비자가 처음 또는 더 자주 구매하도록 영감을 주는 개인화된 관련 광고를 표시함으로써 광고주에게 매출을 창출합니다.

_이 통합은 Jampp에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Jampp 통합을 통해 회사 사용자는 Braze 웹훅 이벤트를 사용하여 Jampp로 이벤트를 동기화할 수 있습니다. 이를 통해 고객은 모바일 광고 에코시스템 내에서 리타겟팅 이니셔티브에 더 풍부한 데이터 세트를 추가할 수 있습니다.

광고로 고객을 리타겟팅하려는 경우의 몇 가지 예시:
- 고객의 이메일 또는 푸시 구독 상태가 변경되었을 때.
- 고객이 Braze 메시징 캠페인과 어떻게 상호작용했는지.
- 고객이 특정 지오펜스를 트리거했는지 여부.

## 필수 조건 {#prerequisites}

이 통합은 iOS 및 Android 앱을 지원합니다.

| 요구 사항 | 설명 |
|---|---|
| Jampp 계정 | 이 파트너십을 활용하려면 [Jampp 계정](https://www.jampp.com/)이 필요합니다. |
| Android 앱 ID | Android용 고유 Braze 애플리케이션 식별자(예: "com.example"). |
| iOS 앱 ID | iOS용 고유 Braze 애플리케이션 식별자(예: "012345678"). |
| Braze SDK에서 IDFA 수집 활성화 | IDFA 수집은 Braze SDK 내에서 선택 사항이며 기본적으로 비활성화되어 있습니다. |
| 커스텀 속성을 통한 Google 광고 ID 수집 | Google 광고 ID 수집은 고객에게 선택 사항이며 [커스텀 속성]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types)으로 수집할 수 있습니다.
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

### 1단계: Braze에서 웹훅 템플릿 생성 {#step-1-create-a-webhook-template-in-braze}

향후 Campaigns 또는 Canvases에서 사용할 Jampp 웹훅 템플릿을 생성하려면 Braze 대시보드에서 **콘텐츠** > **웹훅**으로 이동합니다. 그런 다음 **웹훅 템플릿 생성**을 선택합니다.

일회성 Jampp 웹훅 Campaign을 만들거나 기존 템플릿을 사용하려면 새 Campaign을 생성할 때 Braze에서 **웹훅**을 선택합니다.

새 웹훅 템플릿에서 다음 필드를 입력합니다:
- **Request Body**: Raw Text
- **Webhook URL**:
{% raw %}
```liquid
{% assign event_name = 'your_jampp_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'{{event_name}}','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

http://tracking.jampp.com/event?kind={{event_name}}&rnd={{rnd}}&app={% if {{most_recently_used_device.${idfa}}} == blank %}{{android_app_id}}{% else %}{{iOS_app_id}}{% endif %}&apple_ifa={{most_recently_used_device.${idfa}}}&google_advertising_id={{custom_attribute.${aaid}}}&user_agent={user-agent}&prtnr=braze

{% if {{most_recently_used_device.${idfa}}} == blank and {{custom_attribute.${aaid}}} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

웹훅 URL에서 다음을 수행해야 합니다:
- 이벤트 이름을 설정합니다. 이 이름은 Jampp 대시보드에 표시됩니다.
- Android(예: "com.example") 및 iOS(예: "012345678")용 앱의 고유 애플리케이션 식별자를 전달합니다.
- Google 광고 ID로 추적하는 적절한 커스텀 속성에 대한 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid)를 삽입합니다. Google 광고 ID는 이 예제에서 `aaid`로 나열되지만, 개발자가 설정한 커스텀 속성 이름으로 바꿔야 합니다.

![Braze 웹훅 빌더에 표시된 웹훅 URL 및 메시지 미리보기.]({% image_buster /assets/img/jampp_webhook.png %})

{% alert important %}
Braze는 기기 IDFA/AAID를 자동으로 수집하지 않으므로 이러한 값을 직접 저장해야 합니다. 이 데이터를 수집하려면 사용자 동의가 필요할 수 있다는 점에 유의하세요.
{% endalert %}

#### 요청 헤더 및 메서드 {#request-headers-and-method}

Jampp 웹훅에는 HTTP 메서드와 요청 헤더가 필요합니다.

- **HTTP Method**: GET
- **Request Headers**:
  - **Content-Type**: application/json

![Braze 웹훅 빌더에 표시되는 요청 헤더, HTTP 메서드 및 메시지 미리보기.]({% image_buster /assets/img/jampp_method.png %})

#### 요청 본문 {#request-body}

이 웹훅에 대한 요청 본문을 정의할 필요가 없습니다.

### 2단계: 요청 미리보기 {#step-2-preview-your-request}

메시지를 미리보기하여 다양한 사용자에 대해 요청이 올바르게 렌더링되는지 확인합니다. Android 및 iOS 사용자 모두에 대해 미리보기 및 테스트 요청을 보내는 것을 권장합니다. 요청이 성공하면 API는 `HTTP 204`로 응답합니다.

{% alert important %}
페이지를 떠나기 전에 템플릿을 저장하세요! <br>업데이트된 웹훅 템플릿은 새 [웹훅 Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)을 생성할 때 **저장된 웹훅 템플릿** 목록에서 찾을 수 있습니다.
{% endalert %}