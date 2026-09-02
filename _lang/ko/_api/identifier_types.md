---
nav_title: "API 식별자 유형"
article_title: "API 식별자 유형"
page_order: 2.2
toc_headers: h2
description: "이 참조 문서에서는 Braze 대시보드에 존재하는 다양한 유형의 API 식별자, 해당 식별자를 찾을 수 있는 위치 및 용도에 대해 설명합니다."
page_type: reference
---

# API 식별자 유형 {#api-identifier-types}

> 이 참조 가이드에서는 Braze 대시보드 내에서 찾을 수 있는 다양한 유형의 API 식별자, 그 목적, 어디서 찾을 수 있는지, 일반적으로 어떻게 사용되는지에 대해 설명합니다. REST API 키 또는 워크스페이스 API 키에 대한 자세한 내용은 [API 개요]({{site.baseurl}}/api/basics)를 참조하세요.

다음 식별자는 Braze 외부 API에서 템플릿, Canvas, Campaign 또는 Segment에 액세스하는 데 사용할 수 있습니다. 모든 메시지는 [UTF-8](https://en.wikipedia.org/wiki/UTF-8) 인코딩을 따라야 합니다.

## 앱 식별자 {#app-identifier}

앱 식별자 또는 `app_id`는 워크스페이스 내 특정 앱에 활동을 연결하는 매개변수입니다. 워크스페이스 내에서 어떤 앱과 상호작용하고 있는지를 지정합니다. 예를 들어, iOS 앱용 `app_id`, Android 앱용 `app_id`, 웹 통합용 `app_id`가 각각 있을 수 있습니다. Braze에서는 Braze가 지원하는 다양한 플랫폼 유형에 걸쳐 동일한 플랫폼에 대해 여러 앱이 있을 수 있습니다.

### 어디에서 찾을 수 있나요? {#where-can-i-find-it}

`app_id`를 찾는 방법은 두 가지가 있습니다.

{% tabs local %}
{% tab 앱 식별자 %}
**설정** > **API 및 식별자** > **앱 식별자**로 이동합니다. 각 앱의 API 키는 **식별자** 열에 나열되어 있습니다.
{% endtab %}

{% tab 앱 설정 %}
**설정** > **앱 설정**으로 이동합니다. API 키는 설정 섹션의 **API Key** 필드 옆에 나열되어 있습니다.

{% endtab %}
{% endtabs %}

### 어떤 용도로 사용할 수 있나요? {#what-can-it-be-used-for}

Braze의 앱 식별자는 SDK를 통합할 때 사용되며, REST API 호출에서 특정 앱을 참조하는 데에도 사용됩니다. `app_id`를 사용하면 특정 앱에 대해 발생한 커스텀 이벤트의 데이터를 가져오거나, 앱 삭제 통계, 신규 사용자 통계, 일일 활성 사용자 통계, 세션 시작 통계를 조회하는 등 다양한 작업을 수행할 수 있습니다.

{% alert tip %}
때때로 `app_id`를 입력하라는 메시지가 표시되지만 실제로 앱을 사용하지 않는 경우가 있을 수 있습니다. 이는 특정 플랫폼에 한정된 레거시 필드이므로, 이 필수 매개변수의 입력 안내로 임의의 문자열을 포함하여 이 필드를 생략할 수 있습니다.
{% endalert %}

### 여러 앱 식별자 {#multiple-app-identifiers}

SDK 설정 시 여러 앱 식별자의 가장 일반적인 사용 사례는 디버그와 릴리스 빌드 배리언트에 대한 식별자를 분리하는 것입니다.

빌드에서 여러 앱 식별자를 쉽게 전환하려면, 관련된 각 [빌드 배리언트](https://developer.android.com/studio/build/build-variants.html)에 대해 별도의 `braze.xml` 파일을 만드는 것을 권장합니다. 빌드 배리언트는 빌드 유형과 제품 플레이버의 조합입니다. 기본값으로 새 Android 프로젝트는 `debug`와 `release` 빌드 유형으로 구성되며, 제품 플레이버는 없습니다.

관련된 각 빌드 배리언트에 대해 `src/<build variant name>/res/values/`에 새 `braze.xml`을 만듭니다:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">{YOUR_BUILD_VARIANT_API_KEY}</string>
</resources>
```
빌드 배리언트가 컴파일되면 새 식별자를 사용합니다.

## 템플릿 식별자 {#template-identifier}

[템플릿]({{site.baseurl}}/api/endpoints/templates) 식별자 또는 템플릿 ID는 대시보드 내 특정 템플릿에 대해 Braze에서 생성하는 임의의 키입니다. 템플릿 ID는 각 템플릿마다 고유하며 API를 통해 템플릿을 참조하는 데 사용할 수 있습니다.

회사에서 Campaigns용 HTML 디자인을 외주 제작하는 경우 템플릿이 유용합니다. 템플릿을 구축한 후에는 특정 Campaign에 한정되지 않고 뉴스레터와 같은 일련의 Campaigns에 적용할 수 있는 템플릿을 갖게 됩니다.

### 어디에서 찾을 수 있나요?

템플릿 ID는 다음 두 가지 방법 중 하나로 찾을 수 있습니다.

{% tabs local %}
{% tab 템플릿 %}
**템플릿**으로 이동하여 템플릿 페이지를 선택한 다음 기존 템플릿을 선택합니다. 원하는 템플릿이 아직 없는 경우 새로 만들어 저장합니다. 개별 템플릿 페이지 하단에서 템플릿 식별자를 찾을 수 있습니다.
{% endtab %}

{% tab API 키 %}
**설정** > **API 및 식별자**로 이동합니다. 여기에서 Braze가 제공하는 **추가 API 식별자** 검색을 통해 특정 식별자를 조회할 수 있습니다.

{% endtab %}
{% endtabs %}

### 어떤 용도로 사용할 수 있나요?

- API를 사용하여 템플릿 업데이트
- 특정 템플릿에 대한 정보 가져오기

## Canvas 식별자 {#canvas-identifier}

[Canvas]({{site.baseurl}}/user_guide/messaging/canvas) 식별자 또는 Canvas ID는 대시보드 내에서 특정 Canvas에 대해 Braze가 생성하는 랜덤 키입니다. Canvas ID는 각 Canvas마다 고유하며, API를 통해 Canvases를 참조하는 데 사용할 수 있습니다.

배리언트가 있는 Canvas의 경우, 전체 Canvas ID뿐만 아니라 메인 Canvas 아래에 중첩된 개별 배리언트 Canvas ID도 존재한다는 점을 유의하세요.

### 어디에서 찾을 수 있나요?

Canvas ID는 대시보드에서 찾을 수 있습니다. **메시징** > **Canvas**로 이동하여 기존 Canvas를 선택하세요. 원하는 Canvas가 아직 없다면 새로 생성하고 저장하세요. 개별 Canvas 페이지 하단에서 **Analyze Variants**를 클릭하세요. Canvas API 식별자가 하단에 표시된 창이 나타납니다.

### 어떤 용도로 사용할 수 있나요?

- 특정 메시지에 대한 분석 추적
- Canvas 성능에 대한 상위 수준의 집계 통계 확인
- 특정 Canvas에 대한 세부 정보 확인
- Currents와 함께 사용하여 Canvases에 대한 "전체적인 관점"의 사용자 수준 데이터 수집
- API 트리거 전달과 함께 사용하여 트랜잭션 메시지에 대한 통계 수집

## Campaign 식별자 {#campaign-identifier}

[Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) 식별자 또는 Campaign ID는 대시보드 내 특정 Campaign에 대해 Braze가 생성하는 무작위 키입니다. Campaign ID는 각 Campaign에 고유하며, API를 통해 Campaign을 참조하는 데 사용할 수 있습니다.

배리언트가 있는 Campaign의 경우, 전체 Campaign ID뿐만 아니라 메인 Campaign 아래에 중첩된 개별 배리언트 Campaign ID도 있다는 점을 유의하세요.

### 어디에서 찾을 수 있나요?

Campaign ID는 두 가지 방법으로 찾을 수 있습니다.

{% tabs local %}
{% tab Campaigns %}
**메시징** > **Campaigns**로 이동하여 기존 Campaign을 선택합니다. 원하는 Campaign이 아직 없는 경우 새로 만들고 저장합니다. 개별 Campaign 페이지 하단에서 **Campaign API Identifier**를 찾을 수 있습니다.

{% endtab %}

{% tab API 키 %}
**설정** > **API 및 식별자**로 이동합니다. 여기에서 Braze는 특정 식별자를 검색할 수 있는 **Additional API Identifiers** 검색 기능을 제공합니다.

{% endtab %}
{% endtabs %}

### 어떤 용도로 사용할 수 있나요?

- 특정 메시지에 대한 분석 추적
- Campaign 성능에 대한 상위 수준의 집계 통계 확인
- 특정 Campaign의 세부 정보 확인
- Currents와 함께 사용하여 Campaign에 대한 "전체적인" 접근 방식으로 사용자 수준 데이터 수집
- API 트리거 전달과 함께 사용하여 트랜잭션 메시지에 대한 통계 수집
- **Campaigns** 페이지에서 `api_id:YOUR_API_ID` 필터를 사용하여 [특정 Campaign 검색]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/search_campaigns)

## Segment 식별자 {#segment-identifier}

[Segment]({{site.baseurl}}/user_guide/audience/segments) 식별자 또는 Segment ID는 대시보드 내 특정 Segment에 대해 Braze가 생성하는 무작위 키입니다. Segment ID는 각 Segment마다 고유하며, API를 통해 Segment를 참조하는 데 사용할 수 있습니다.

### 어디에서 찾을 수 있나요?

Segment ID는 두 가지 방법으로 찾을 수 있습니다.

{% tabs local %}
{% tab Segments %}
**오디언스** > **Segments**로 이동하여 기존 Segment를 선택합니다. 원하는 Segment가 아직 없는 경우 새로 생성하고 저장합니다. 개별 Segment 페이지 하단에서 Segment 식별자를 확인할 수 있습니다.

{% endtab %}

{% tab API 키 %}
**설정** > **API 및 식별자**로 이동합니다. 여기에서 Braze는 특정 식별자를 검색할 수 있는 **추가 API 식별자** 검색 기능을 제공합니다.

{% endtab %}
{% endtabs %}

### 어떤 용도로 사용할 수 있나요?

- 특정 Segment의 세부 정보 조회
- 특정 Segment의 분석 데이터 검색
- 특정 Segment에서 커스텀 이벤트가 기록된 횟수 확인
- API에서 Segment 멤버를 지정하고 Campaign 전송

## 전송 식별자 {#send-identifier}

전송 식별자(전송 ID)는 특정 메시지 전송에 대해 분석을 추적하기 위해 Braze가 생성하거나 사용자가 직접 만든 키입니다. 전송 식별자를 사용하면 [`/sends/data_series` 엔드포인트]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics)를 통해 Campaign 전송의 특정 인스턴스에 대한 분석 데이터를 가져올 수 있습니다.

### 어디에서 찾을 수 있나요?

API 및 API 트리거 Campaigns가 브로드캐스트로 전송될 때, 전송 식별자가 제공되지 않으면 자동으로 전송 식별자가 생성됩니다. 직접 전송 식별자를 지정하려면 먼저 [`/sends/id/create` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids)를 통해 생성해야 합니다. 식별자는 모두 ASCII 문자여야 하며 최대 64자까지 가능합니다. 동일한 Campaign의 여러 전송에 대한 분석을 그룹화하려면 전송 식별자를 여러 전송에서 재사용할 수 있습니다.

### 어떤 용도로 사용할 수 있나요?
전송마다 Campaign을 생성하지 않고도 프로그래밍 방식으로 메시지 성능을 전송하고 추적할 수 있습니다.

## 구독 그룹 식별자 {#subscription-group-identifier}

구독 그룹 식별자, 즉 구독 그룹 ID는 Braze에서 특정 구독 그룹에 대해 생성하는 키입니다. ID는 각 구독 그룹에 고유하며, API를 통해 구독 그룹을 참조하는 데 사용할 수 있습니다.

### 어디에서 찾을 수 있나요?

**오디언스** > **구독**으로 이동하여 해당 구독 그룹 옆에 있는 ID를 복사합니다.

### 어떤 용도로 사용할 수 있나요?

- 사용자의 구독 그룹 목록 조회
- 사용자의 구독 그룹 상태 가져오기
- 사용자의 구독 그룹 상태 업데이트