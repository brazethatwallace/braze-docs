---
nav_title: "API 식별자 유형"
article_title: API 식별자 유형
page_order: 2.2
toc_headers: h2
description: "이 참조 문서에서는 Braze 대시보드에 존재하는 다양한 유형의 API 식별자, 해당 식별자를 찾을 수 있는 위치 및 용도에 대해 설명합니다."
page_type: reference

---

# API 식별자 유형 {#api-identifier-types}

> 이 참조 가이드에서는 Braze 대시보드 내에서 찾을 수 있는 다양한 유형의 API 식별자, 그 목적, 어디서 찾을 수 있는지, 일반적으로 어떻게 사용되는지에 대해 설명합니다. REST API 키 또는 워크스페이스 API 키에 대한 자세한 내용은 [API 개요]({{site.baseurl}}/api/api_key/)를 참조하세요.

다음 식별자는 Braze 외부 API에서 템플릿, Canvas, Campaign 또는 Segment에 액세스하는 데 사용할 수 있습니다. 모든 메시지는 [UTF-8](https://en.wikipedia.org/wiki/UTF-8) 인코딩을 따라야 합니다.

## 앱 식별자 {#app-identifier}

앱 식별자 또는 `app_id`는 워크스페이스 내 특정 앱에 활동을 연결하는 매개변수입니다. 워크스페이스 내에서 어떤 앱과 상호작용하고 있는지를 지정합니다. 예를 들어 iOS 앱의 `app_id`, Android 앱의 `app_id`, 웹 통합의 `app_id`가 있을 수 있습니다. Braze에서는 Braze가 지원하는 다양한 플랫폼 유형에 걸쳐 동일한 플랫폼용 앱이 여러 개 있을 수 있습니다.

### 어디서 찾을 수 있나요? {#where-can-i-find-it}

`app_id`를 찾는 방법은 두 가지가 있습니다:

{% tabs local %}
{% tab App Identifiers %}
**설정** > **API 키** > **앱 식별자**로 이동합니다. 각 앱의 API 키는 **식별자** 열 아래에 나열됩니다.
{% endtab %}

{% tab App Settings %}
**설정** > **앱 설정**으로 이동합니다. API 키는 설정 섹션의 **API 키** 필드 옆에 나열됩니다.

{% endtab %}
{% endtabs %}

### 어떤 용도로 사용할 수 있나요? {#what-can-it-be-used-for}

Braze의 앱 식별자는 SDK를 통합할 때 사용되며 REST API 호출에서 특정 앱을 참조하는 데에도 사용됩니다. `app_id`를 사용하면 특정 앱에서 발생한 커스텀 이벤트에 대한 데이터 가져오기, 특정 앱의 제거 통계, 신규 사용자 통계, DAU 통계 및 세션 시작 통계 검색 등 다양한 작업을 수행할 수 있습니다.

{% alert tip %}
`app_id`를 입력하라는 메시지가 표시되지만 앱이 아닌 경우가 있습니다. 이는 특정 플랫폼에 한정된 레거시 필드이므로, 이 필수 매개변수의 입력 안내로 임의의 문자열을 포함하여 이 필드를 생략할 수 있습니다.
{% endalert %}

### 여러 앱 식별자 {#multiple-app-identifiers}

SDK 설정 중에 여러 앱 식별자를 사용하는 가장 일반적인 사용 사례는 디버그 및 릴리스 빌드 배리언트를 위해 해당 식별자를 분리하는 것입니다.

빌드에서 여러 앱 식별자 간에 쉽게 전환하려면 각 관련 [빌드 배리언트](https://developer.android.com/studio/build/build-variants.html)에 대해 별도의 `braze.xml` 파일을 만드는 것이 좋습니다. 빌드 배리언트는 빌드 유형과 제품 플레이버의 조합입니다. 기본적으로 새 Android 프로젝트는 `debug` 및 `release` 빌드 유형으로 구성되며 제품 플레이버는 없습니다.

각 관련 빌드 배리언트에 대해 `src/<build variant name>/res/values/`에서 새 `braze.xml`을 생성하세요:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">{YOUR_BUILD_VARIANT_API_KEY}</string>
</resources>
```
빌드 배리언트가 컴파일될 때 새 식별자를 사용합니다.

## 템플릿 식별자 {#template-identifier}

[템플릿]({{site.baseurl}}/api/endpoints/templates/) 식별자 또는 템플릿 ID는 대시보드 내에서 특정 템플릿에 대해 Braze가 생성한 임의의 키입니다. 템플릿 ID는 각 템플릿마다 고유하며 API를 통해 템플릿을 참조하는 데 사용할 수 있습니다.

템플릿은 회사에서 Campaign용 HTML 디자인을 외주하는 경우에 유용합니다. 템플릿이 만들어지면 특정 Campaign에 국한되지 않고 뉴스레터와 같은 일련의 Campaign에 적용할 수 있는 템플릿을 갖게 됩니다.

### 어디서 찾을 수 있나요? {#where-can-i-find-it}

템플릿 ID는 다음 두 가지 방법 중 하나로 찾을 수 있습니다:

{% tabs local %}
{% tab Templates %}
**템플릿**으로 이동하여 템플릿 페이지를 선택한 다음 기존 템플릿을 선택합니다. 원하는 템플릿이 아직 없는 경우 템플릿을 만들어 저장하세요. 개별 템플릿 페이지 하단에서 템플릿 식별자를 찾을 수 있습니다.
{% endtab %}

{% tab API Keys %}
**설정** > **API 키**로 이동합니다. 여기에서 Braze는 특정 식별자를 조회할 수 있는 **추가 API 식별자** 검색을 제공합니다.

{% endtab %}
{% endtabs %}

### 어떤 용도로 사용할 수 있나요? {#what-can-it-be-used-for}

- API를 사용하여 템플릿 업데이트
- 특정 템플릿에 대한 정보 가져오기

## Canvas 식별자 {#canvas-identifier}

[Canvas]({{site.baseurl}}/user_guide/messaging/canvas/) 식별자 또는 Canvas ID는 대시보드 내의 특정 Canvas에 대해 Braze에서 생성한 임의의 키입니다. Canvas ID는 각 Canvas마다 고유하며 API를 통해 Canvases를 참조하는 데 사용할 수 있습니다.

배리언트가 있는 Canvas의 경우 전체 Canvas ID와 기본 Canvas 아래에 중첩된 개별 배리언트 Canvas ID가 있다는 점에 유의하세요.

### 어디서 찾을 수 있나요? {#where-can-i-find-it}

대시보드에서 Canvas ID를 찾을 수 있습니다. **메시징** > **Canvas**로 이동하여 기존 Canvas를 선택합니다. 원하는 Canvas가 아직 존재하지 않으면 Canvas를 만들어 저장하세요. 개별 Canvas 페이지 하단에서 **배리언트 분석**을 클릭합니다. 하단에 Canvas API 식별자가 있는 창이 나타납니다.

### 어떤 용도로 사용할 수 있나요? {#what-can-it-be-used-for}

- 특정 메시지에 대한 분석 추적
- Canvas 성과에 대한 높은 수준의 집계 통계 가져오기
- 특정 Canvas에 대한 세부 정보 가져오기
- Canvases에 대한 "더 큰 그림" 접근 방식을 위해 사용자 수준 데이터를 가져오기 위한 Currents 사용
- 트랜잭션 메시지에 대한 통계를 수집하기 위한 API 트리거 전달 사용

## Campaign 식별자 {#campaign-identifier}

[Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/) 식별자 또는 Campaign ID는 대시보드 내에서 특정 Campaign에 대해 Braze가 생성한 임의의 키입니다. Campaign ID는 각 Campaign마다 고유하며 API를 통해 Campaign을 참조하는 데 사용할 수 있습니다.

배리언트가 있는 Campaign의 경우 전체 Campaign ID와 기본 Campaign 아래에 중첩된 개별 배리언트 Campaign ID가 모두 있다는 점에 유의하세요.

### 어디서 찾을 수 있나요? {#where-can-i-find-it}

Campaign ID는 다음 두 가지 방법 중 하나로 찾을 수 있습니다:

{% tabs local %}
{% tab Campaigns %}
**메시징** > **Campaigns**로 이동하여 기존 Campaign을 선택합니다. 원하는 Campaign이 아직 존재하지 않으면 Campaign을 만들어 저장하세요. 개별 Campaign 페이지 하단에서 **Campaign API Identifier**를 찾을 수 있습니다.

{% endtab %}

{% tab API Keys %}
**설정** > **API 키**로 이동합니다. 여기에서 Braze는 특정 식별자를 조회할 수 있는 **추가 API 식별자** 검색을 제공합니다.

{% endtab %}
{% endtabs %}

### 어떤 용도로 사용할 수 있나요? {#what-can-it-be-used-for}

- 특정 메시지에 대한 분석 추적
- Campaign 성과에 대한 높은 수준의 집계 통계 가져오기
- 특정 Campaign에 대한 세부 정보 가져오기
- Campaign에 대한 "더 큰 그림" 접근 방식을 위해 사용자 수준 데이터를 가져오기 위한 Currents 사용
- 트랜잭션 메시지에 대한 통계를 수집하기 위한 API 트리거 전달 사용
- **Campaigns** 페이지에서 `api_id:YOUR_API_ID` 필터를 사용하여 [특정 Campaign 검색]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/#search-syntax)

## Segment 식별자 {#segment-identifier}

[Segment]({{site.baseurl}}/user_guide/audience/segments/) 식별자 또는 Segment ID는 대시보드 내의 특정 Segment에 대해 Braze에서 생성한 임의의 키입니다. Segment ID는 각 Segment마다 고유하며 API를 통해 Segment를 참조하는 데 사용할 수 있습니다.

### 어디서 찾을 수 있나요? {#where-can-i-find-it}

Segment ID는 다음 두 가지 방법 중 하나로 찾을 수 있습니다:

{% tabs local %}
{% tab Segments %}
**오디언스** > **Segments**로 이동하여 기존 Segment를 선택합니다. 원하는 Segment가 아직 존재하지 않으면 Segment를 생성하여 저장합니다. 개별 Segment 페이지 하단에서 Segment 식별자를 찾을 수 있습니다.

{% endtab %}

{% tab API Keys %}
**설정** > **API 키**로 이동합니다. 여기에서 Braze는 특정 식별자를 조회할 수 있는 **추가 API 식별자** 검색을 제공합니다.

{% endtab %}
{% endtabs %}

### 어떤 용도로 사용할 수 있나요? {#what-can-it-be-used-for}

- 특정 Segment에 대한 세부 정보 가져오기
- 특정 Segment에 대한 분석 검색
- 특정 Segment에 대해 커스텀 이벤트가 기록된 횟수 가져오기
- API 내에서 Segment의 멤버에게 Campaign을 지정하여 보내기

## 발신 식별자 {#send-identifier}

발신 식별자 또는 발신 ID는 분석을 추적해야 하는 특정 메시지 발신에 대해 Braze에서 생성하거나 사용자가 생성한 키입니다. 발신 식별자를 사용하면 [`/sends/data_series` 엔드포인트]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/)를 통해 Campaign 발신의 특정 인스턴스에 대한 분석을 가져올 수 있습니다.

### 어디서 찾을 수 있나요? {#where-can-i-find-it}

브로드캐스트로 전송되는 API 및 API 트리거 Campaign은 발신 식별자가 제공되지 않으면 자동으로 발신 식별자를 생성합니다. 고유한 발신 식별자를 지정하려면 먼저 [`/sends/id/create` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)를 통해 식별자를 생성해야 합니다. 식별자는 모두 ASCII 문자여야 하며 최대 64자여야 합니다. 동일한 Campaign의 여러 발신에 대한 분석을 그룹화하려는 경우 발신 식별자를 여러 발신에 재사용할 수 있습니다.

### 어떤 용도로 사용할 수 있나요? {#what-can-it-be-used-for}
각 발신에 대해 Campaign을 만들지 않고 프로그래밍 방식으로 메시지 성과를 발신하고 추적할 수 있습니다.

## 구독 그룹 식별자 {#subscription-group-identifier}

구독 그룹 식별자 또는 구독 그룹 ID는 특정 구독 그룹에 대해 Braze에서 생성한 키입니다. ID는 각 구독 그룹에 고유하며 API를 통해 구독 그룹을 참조하는 데 사용할 수 있습니다.

### 어디서 찾을 수 있나요? {#where-can-i-find-it}

**오디언스** > **구독**으로 이동하여 각 구독 그룹 옆에 있는 ID를 복사합니다.

### 어떤 용도로 사용할 수 있나요? {#what-can-it-be-used-for}

- 사용자의 구독 그룹 나열
- 사용자의 구독 그룹 상태 가져오기
- 사용자의 구독 그룹 상태 업데이트