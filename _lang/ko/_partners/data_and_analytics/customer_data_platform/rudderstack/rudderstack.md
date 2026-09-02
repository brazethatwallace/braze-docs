---
nav_title: RudderStack
article_title: RudderStack
description: "이 문서에서는 Android, iOS 및 웹 애플리케이션에 원활한 Braze 통합을 제공하는 오픈소스 고객 데이터 인프라인 Braze와 RudderStack 간의 파트너십에 대해 설명합니다. RudderStack을 사용하면 인앱 고객 이벤트 데이터를 상황별 분석을 위해 Braze로 직접 전송할 수 있습니다."
page_type: partner
search_tag: Partner

---

# RudderStack

> [RudderStack](https://rudderstack.com/)은 고객 이벤트 데이터를 수집하여 선호하는 데이터 웨어하우스 및 Braze를 비롯한 수십 개의 분석 제공업체로 라우팅하기 위한 오픈소스 고객 데이터 인프라입니다. 엔터프라이즈급으로 설계되었으며, 이벤트 데이터를 실시간으로 처리할 수 있는 강력한 변환 프레임워크를 제공합니다.

Braze와 RudderStack 통합은 Android, iOS 및 웹 애플리케이션을 위한 네이티브 SDK 통합과 백엔드 서비스에서의 서버 간 통합을 제공합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| RudderStack 계정 | 이 파트너십을 활용하려면 [RudderStack 계정](https://app.rudderstack.com/)이 필요합니다. |
| 구성된 소스 | [소스](https://www.rudderstack.com/docs/dashboard-guides/sources/)는 본질적으로 웹사이트, 모바일 앱 또는 백엔드 서버와 같이 RudderStack으로 전송되는 모든 데이터의 Origin입니다. RudderStack에서 Braze를 대상으로 설정하기 전에 소스를 구성해야 합니다. |
| Braze REST API 키 | `users.track`, `users.identify`, `users.delete`, `users.alias.new` 권한이 있는 Braze REST API 키.<br><br>이 키는 Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze 앱 키 | 앱 키를 가져오려면 Braze 대시보드에서 **설정** > **앱 설정** > **식별**으로 이동하여 앱 이름을 찾으세요. 연결된 식별자 문자열을 저장합니다. |
| 데이터 센터 | 데이터 센터는 Braze 대시보드 [인스턴스]({{site.baseurl}}/api/basics#endpoints)에 맞춰 정렬됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

### 1단계: 소스 추가 {#step-1-add-a-source}

Braze로 데이터를 전송하려면 먼저 RudderStack 앱에 소스가 설정되어 있는지 확인해야 합니다. 데이터 소스를 설정하는 방법은 [RudderStack](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started)에서 확인할 수 있습니다.

### 2단계: 대상 구성 {#step-2-configure-destination}

데이터 소스 설정이 완료되면 RudderStack 대시보드에서 **Destinations** 아래의 **ADD DESTINATION**을 선택합니다. 사용 가능한 대상 목록에서 **Braze**를 선택하고 **Next**를 클릭합니다.

Braze 대상에서 앱 키, Braze REST API 키, 데이터 클러스터 및 네이티브 SDK 옵션(기기 모드 전용)을 입력합니다. 네이티브 SDK 옵션을 토글하면 Braze 네이티브 SDK를 사용하여 이벤트를 전송합니다.

### 3단계: 통합 유형 선택 {#step-3-choose-the-type-of-integration}

다음 방법 중 하나를 사용하여 RudderStack의 웹 및 네이티브 클라이언트 측 라이브러리를 Braze와 통합할 수 있습니다.

- [병렬 통합 / 기기 모드](#device-mode)**:** RudderStack이 클라이언트(브라우저 또는 모바일 앱)에서 직접 Braze로 이벤트 데이터를 전송합니다.
- [서버 간 통합 / 클라우드 모드](#cloud-mode)**:** Braze SDK가 이벤트 데이터를 RudderStack으로 직접 전송한 후, RudderStack이 데이터를 변환하고 Braze로 라우팅합니다.
- [하이브리드 모드](#hybrid-mode)**:** 하이브리드 모드를 사용하여 단일 연결로 iOS 및 Android 자동 생성 이벤트와 사용자 생성 이벤트를 Braze로 전송합니다.

{% alert note %}
RudderStack의 [연결 모드](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/)와 각 모드의 장점에 대해 자세히 알아보세요.
{% endalert %}

#### 병렬 통합(기기 모드) {#device-mode}

이 모드에서는 웹사이트 또는 모바일 앱에 설정된 Braze SDK를 사용하여 이벤트를 Braze로 전송할 수 있습니다.

[지원되는 메서드](#supported-methods)에 설명된 대로 Braze GitHub 리포지토리에서 플랫폼에 맞는 RudderStack SDK 매핑을 설정합니다.

- [Android](https://github.com/rudderlabs/rudder-integration-braze-android)
- [iOS](https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master)
- [Swift](https://github.com/rudderlabs/rudder-integration-braze-swift)
- [웹](https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/Braze)
- [React Native](https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native)
- [Flutter](https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter)

기기 모드 통합을 완료하려면 [프로젝트에 Braze 추가](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration)에 대한 자세한 RudderStack 안내를 참조하세요.

#### 서버 간 통합(클라우드 모드) {#cloud-mode}

이 모드에서는 SDK가 이벤트 데이터를 RudderStack 서버로 직접 전송합니다. 그런 다음 RudderStack이 이 데이터를 변환하여 원하는 대상으로 라우팅합니다. 이 변환은 RudderStack 백엔드에서 RudderStack의 트랜스포머 모듈을 사용하여 수행됩니다.

통합을 활성화하려면 [지원되는 메서드](#supported-methods)에 설명된 대로 RudderStack 메서드를 Braze에 매핑해야 합니다.

{% alert note %}
RudderStack의 서버 측 SDK(Java, Python, Node.js, Go, Ruby)는 클라우드 모드만 지원합니다. 서버 측 SDK는 RudderStack 백엔드에서 작동하며 Braze 전용 SDK를 로드할 수 없기 때문입니다.
{% endalert %}

{% alert important %}
서버 간 통합은 푸시 알림이나 인앱 메시징과 같은 Braze UI 기능을 지원하지 않습니다. 하지만 이러한 기능은 기기 모드 통합에서 지원됩니다.
{% endalert %}

#### 하이브리드 모드 {#hybrid-mode}

하이브리드 모드를 사용하여 iOS 및 Android 소스에서 모든 이벤트를 Braze로 전송합니다.

하이브리드 모드를 선택하여 이벤트를 Braze로 전송하면 RudderStack은 다음과 같이 작동합니다.
1. Braze SDK를 초기화합니다.
2. 모든 사용자 생성 이벤트(identify, track, page, screen, group)를 클라우드 모드를 통해서만 Braze로 전송하고, 기기 모드를 통한 전송은 차단합니다.
3. 자동 생성 이벤트(Braze SDK가 필요한 인앱 메시지, 푸시 알림)는 기기 모드를 통해 전송합니다.

[하이브리드 모드로 이벤트를 전송](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode)하려면 소스를 Braze 대상에 연결할 때 하이브리드 모드 옵션을 사용합니다. 그런 다음 프로젝트에 Braze 통합을 추가합니다.

## 4단계: 추가 설정 구성 {#step-4-configure-additional-settings}

초기 설정을 완료한 후, Braze에서 데이터를 올바르게 수신하기 위해 다음 설정을 구성합니다:

- **그룹 호출에서 구독 그룹 활성화**: 이 설정을 활성화하면 그룹 이벤트에서 구독 그룹 상태를 전송할 수 있습니다. 자세한 내용은 [그룹](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group)을 참조하세요.
- **커스텀 속성 작업 사용**: Braze의 [중첩 커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects) 기능을 사용하여 커스텀 속성 오브젝트로 Segments를 생성하고 메시지를 개인화하려면 이 설정을 활성화합니다. 자세한 내용은 [사용자 특성을 중첩 커스텀 속성으로 전송](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes)을 참조하세요.
- **익명 사용자 이벤트 추적**: 이 설정을 활성화하면 익명 사용자 활동을 추적하고 해당 정보를 Braze로 전송할 수 있습니다.

### 기기 모드 설정 {#device-mode-settings}

다음 설정은 [기기 모드](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode)를 통해 Braze로 이벤트를 전송하는 경우에만 적용됩니다:

- **클라이언트 사이드 이벤트 필터링**: 이 설정을 사용하면 Braze로 전달되는 이벤트를 차단하거나 허용할 이벤트를 지정할 수 있습니다. 이 설정에 대한 자세한 내용은 [클라이언트 사이드 이벤트 필터링](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/)을 참조하세요.
- **특성 중복 제거**: 이 설정을 활성화하면 [`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify) 호출에서 사용자 특성의 중복을 제거할 수 있습니다.
- **Braze 로그 표시**: 이 설정은 [JavaScript SDK](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/)를 소스로 사용하는 경우에만 적용됩니다. 이 설정을 활성화하면 사용자에게 Braze 로그를 표시할 수 있습니다.
- **OneTrust 쿠키 카테고리**: 이 설정을 사용하면 [OneTrust](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/) 쿠키 동의 그룹을 Braze에 연결할 수 있습니다.

## 지원되는 메서드 {#supported-methods}

Braze는 RudderStack의 identify, track, screen, page, group, alias 메서드를 지원합니다.

{% tabs %}
{% tab Identify %}

RudderStack의 [`identify` 메서드](https://rudderstack.com/docs/destinations/marketing/braze/#identify)는 사용자를 해당 사용자의 행동과 연결합니다. RudderStack은 고유한 사용자 ID와 이름, 이메일, IP 주소 등과 같은 해당 사용자와 관련된 선택적 특성을 캡처합니다.

**identify 호출에 대한 델타 관리**<br>
디바이스 모드를 통해 Braze로 이벤트를 전송하는 경우, `identify` 호출을 중복 제거하여 비용을 절감할 수 있습니다. 이를 위해 대시보드 설정에서 Deduplicate Traits를 활성화하세요. 그러면 RudderStack은 변경되거나 수정된 속성(특성)만 Braze로 전송합니다.

**사용자 삭제**<br>
RudderStack의 [Data Regulation API](https://www.rudderstack.com/docs/api/data-regulation-api/)에서 [Suppression with Delete regulation](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation)을 사용하여 Braze에서 사용자를 삭제할 수 있습니다.

{% endtab %}
{% tab Track %}

RudderStack의 [`track` 메서드](https://rudderstack.com/docs/destinations/marketing/braze/#track)는 모든 사용자 활동과 해당 활동에 관련된 속성을 캡처합니다.

**주문 완료**<br>
[RudderStack 이커머스 API](https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/)를 사용하여 `Order Completed`라는 이름의 이벤트에 대해 track 메서드를 호출하면, RudderStack은 해당 이벤트에 나열된 제품을 [`purchases`]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data)로 Braze에 전송합니다.

{% endtab %}
{% tab Screen %}

RudderStack의 [`screen` 메서드](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen)를 사용하면 조회한 화면에 대한 추가 정보와 함께 사용자의 모바일 화면 조회를 기록할 수 있습니다.

{% endtab %}
{% tab Page %}

RudderStack의 [`page` 메서드](https://rudderstack.com/docs/destinations/marketing/braze/#page)를 사용하면 웹사이트의 페이지 조회를 기록할 수 있습니다. 또한 해당 페이지에 대한 기타 관련 정보도 캡처합니다.

{% endtab %}
{% tab Group %}

RudderStack의 [`group` 메서드](https://rudderstack.com/docs/destinations/marketing/braze/#group)를 사용하면 사용자를 그룹과 연결할 수 있습니다.

**구독 그룹 상태**<br>
구독 그룹 상태를 업데이트하려면 RudderStack 대시보드에서 "Enable subscription groups in group call" 설정을 활성화하고 group 호출에서 구독 그룹 상태를 전송하세요.

{% endtab %}
{% tab Alias %}

RudderStack의 [`alias` 메서드](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias)를 사용하면 알려진 사용자의 서로 다른 ID를 병합할 수 있습니다. RudderStack은 Braze에 대해 클라우드 모드에서만 alias 호출을 지원한다는 점에 유의하세요.

{% endtab %}
{% endtabs %}

## 사용자 특성을 중첩 커스텀 속성으로 전송하기 {#send-user-traits-as-nested-custom-attributes}

사용자 특성을 Braze에 중첩 커스텀 속성으로 전송하고, 이에 대해 추가, 업데이트 및 제거 작업을 수행할 수 있습니다. 이를 위해 Braze 대상을 설정할 때 RudderStack에서 "Use 커스텀 속성 Operation dashboard" 설정을 활성화합니다. 이 기능은 클라우드 모드에서만 사용할 수 있습니다.

다음 형식으로 `identify` 이벤트에서 사용자 특성을 중첩 커스텀 속성으로 전송할 수 있습니다:
```javascript
rudderanalytics.identify("1hKOmRA4GRlm", {
  "cars": {
    "add": [{
      "age": 27,
      "id": 1,
      "name": "Alex Keener"
    }],
    "update": [{
        "age": 30,
        "id": 2,
        "identifier": "id",
        "name": "Rowan"
      },
      {
        "age": 27,
        "id": 1,
        "identifier": "id",
        "name": "Alex"
      }
    ]
  },
  "country": "USA",
  "email": "alex@example.com",
  "firstName": "Alex",
  "gender": "M",
  "pets": [{
      "breed": "beagle",
      "id": 1,
      "name": "Scooby",
      "type": "dog"
    },
    {
      "breed": "calico",
      "id": 2,
      "name": "Garfield",
      "type": "cat"
    }
  ]
})
```

`track`, `page` 또는 `screen` 호출을 통해 사용자 특성을 커스텀 사용자 속성으로 전송하려면, 이벤트에서 `traits`를 컨텍스트 필드로 전달합니다:
```javascript
rudderanalytics.track("Product Viewed", {
    revenue: 8.99,
    currency: "USD",
 },{
  "traits": {
    "cars": {
      "add": [{
        "age": 27,
        "id": 1,
        "name": "Alex Keener"
      }],
      "update": [{
          "age": 30,
          "id": 2,
          "identifier": "id",
          "name": "Alex"
        },
        {
          "age": 27,
          "id": 1,
          "identifier": "id",
          "name": "Rowan"
        }
      ]
    },
    "city": "Disney",
    "country": "USA",
    "email": "alexa@example.com",
    "firstName": "Alexa",
    "gender": "woman",
    "pets": [{
        "breed": "beagle",
        "id": 1,
        "name": "Scooby",
        "type": "dog"
      },
      {
        "breed": "calico",
        "id": 2,
        "name": "Garfield",
        "type": "cat"
      }
    ]
  }
});
```

{% alert note %}
업데이트 및 제거 작업의 경우, `identifier`는 필수 키입니다. 중첩 배열에 추가, 업데이트 또는 제거 작업이 없는 경우, RudderStack은 기본적으로 생성 작업을 사용하여 속성을 생성합니다. 중첩 커스텀 속성 전송에 대한 자세한 내용은 [객체 배열]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)을 참조하세요.
{% endalert %}

## 문제 해결 {#troubleshooting}

### RudderStack 로그에 "[Braze Deduplication]: Duplicate user detected, the user is dropped"가 표시됩니다 {#i-see-braze-deduplication-duplicate-user-detected-the-user-is-dropped-in-rudderstack-logs}

이 메시지는 **Deduplicate Traits**가 활성화된 상태에서 RudderStack이 변경되지 않은 사용자 특성을 Braze로 전달하기 전에 삭제할 때 RudderStack에서 발생하는 메시지입니다. Braze 오류가 아닙니다.

RudderStack은 수신되는 `identify` 및 `track` 특성을 사용자 프로필과 비교하여 변경 사항이 없는 속성을 건너뛰어 Braze 데이터 포인트 사용량을 줄입니다. 자세한 내용은 RudderStack의 [User Trait Deduplication in Braze](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/trait-deduplication/) 가이드를 참조하세요.

모든 특성을 매 호출마다 전송해야 하는 경우, RudderStack Braze 대상 설정에서 **Deduplicate Traits**를 비활성화하세요. 이 경우 Braze 데이터 포인트 소비량이 증가할 수 있다는 점에 유의하세요.