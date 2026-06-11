---
nav_title: 위치 추적
article_title: 위치 추적
page_order: 0
page_type: reference
description: "이 참조 문서에서는 앱에서 위치 추적 및 위치 타겟팅을 사용하는 방법과 위치 추적을 지원하는 파트너에 대해 설명합니다."
tool: Location
search_rank: 2
---

# 위치 추적 {#location-tracking}

> 위치 수집은 GPS 위치 데이터를 사용하여 앱이 열렸을 때 사용자의 가장 최근 위치를 캡처합니다. 이 정보를 사용하여 정의된 위치에 있었던 사용자를 기반으로 데이터를 세분화할 수 있습니다.

## 위치 추적 활성화 {#enabling-location-tracking}

앱에서 위치 수집을 활성화하려면 사용 중인 플랫폼에 대한 개발자 가이드를 참조하세요:

- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=android)
- [웹]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=web)

일반적으로 모바일 앱은 기기의 GPS 칩과 기타 시스템(예: Wi-Fi 스캐닝)을 사용하여 사용자의 위치를 추적합니다. 웹 앱은 WPS(Wi-Fi 포지셔닝 시스템)를 사용하여 사용자의 위치를 추적합니다. 이러한 모든 플랫폼에서는 사용자가 위치 추적에 옵트인해야 합니다. 위치 추적 데이터의 정확도는 사용자가 기기에서 Wi-Fi를 활성화했는지 여부에 따라 영향을 받을 수 있습니다. Android 사용자는 다양한 위치 모드를 선택할 수도 있습니다. "배터리 절약" 또는 "기기만" 모드를 사용하는 사용자는 부정확한 데이터를 가질 수 있습니다.

### IP 주소를 통한 SDK 사용자 위치 {#sdk-user-location-by-ip-address}

Braze는 첫 번째 SDK 세션 시작 시 IP 주소에서 지리적으로 위치가 파악된 국가를 사용하여 사용자 위치를 감지합니다.

이전에는 Braze가 SDK 사용자 생성 시 및 첫 번째 세션 동안 기기 로캘의 국가 코드를 사용했습니다. 첫 번째 세션 시작이 처리된 후에야 IP 주소를 사용하여 사용자에게 더 신뢰할 수 있는 국가를 설정했습니다. 이는 사용자 국가가 두 번째 세션부터, 즉 첫 번째 세션 시작이 처리된 후에야 더 높은 정확도로 설정되었음을 의미합니다.

현재 Braze는 SDK를 통해 생성된 사용자 프로필에 국가 값을 설정하기 위해 IP 주소를 사용하며, 이 IP 기반 국가 설정은 첫 번째 세션 중 및 이후에 사용할 수 있습니다.

#### 자동 위치 수집 {#automatic-location-collection}

활성화된 경우, SDK의 자동 위치 수집은 IP 기반 국가 동작과 별개입니다. 이는 사용자가 권한을 부여한 경우 GPS와 같은 기기 위치 신호와 관련되며, `Most Recent Location`과 같은 필터를 지원합니다. IP만으로 도시와 같은 세분화된 필드를 자동으로 채우지는 않습니다.

도시 또는 우편번호 수준의 타겟팅을 위해서는 [`setLastKnownLocation()`]({{site.baseurl}}/developer_guide/analytics/tracking_location/)(해당 플랫폼의 SDK 문서 참조), 커스텀 속성을 작성하는 자체 IP 지리 위치 서비스, 또는 수집한 데이터를 사용한 [위치 타겟팅]({{site.baseurl}}/user_guide/audience/segments/location_targeting/)을 사용하세요.

## 위치 타겟팅 {#location-targeting}

위치 추적 데이터와 세그먼트를 사용하여 위치 기반 Campaign과 전략을 설정할 수 있습니다. 예를 들어, 특정 지역에 거주하는 사용자를 대상으로 프로모션 Campaign을 실행하거나 더 엄격한 규정이 있는 지역의 사용자를 제외할 수 있습니다.

위치 세그먼트 생성에 대한 자세한 내용은 [위치 타겟팅]({{site.baseurl}}/user_guide/audience/segments/location_targeting/)을 참조하세요.

## 기본 위치 속성 하드 설정 {#hard-setting-the-default-location-attribute}

API의 [`users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 사용하여 [`current_location`]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens) 표준 속성을 업데이트할 수도 있습니다. 예시는 다음과 같습니다:

```
https://[your_braze_rest_endpoint]/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [
 	{
 	  "external_id" : "XXX",
 	  "current_location" : {"longitude":-0.118092, "latitude": 51.509865}
      }
   ]
}
```

## 비콘 및 지오펜스에 대한 파트너 지원 {#partnership-support-for-beacon-and-geofence}

기존 비콘 또는 지오펜스 지원을 타겟팅 및 메시징 기능과 결합하면 사용자의 물리적 행동에 대한 더 많은 정보를 얻을 수 있으므로 그에 맞게 메시지를 보낼 수 있습니다. 일부 파트너와 함께 위치 추적을 활용할 수 있습니다:

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

## 지오펜스와 위치 추적의 차이점 {#differences-between-geofences-and-location-tracking}

{% multi_lang_include locations_and_geofences/geofences_vs_location_tracking.md %}

## 자주 묻는 질문 {#frequently-asked-questions}

### Braze는 언제 위치 데이터를 수집하나요? {#when-does-braze-collect-location-data}

Braze는 애플리케이션이 포그라운드에서 열려 있을 때만 위치를 수집합니다. 따라서 `Most Recent Location` 필터는 사용자가 마지막으로 애플리케이션을 연 위치(세션 시작이라고도 함)를 기반으로 사용자를 타겟팅합니다.

다음 사항도 유의해야 합니다:

- 위치가 비활성화된 경우, `Most Recent Location` 필터는 마지막으로 기록된 위치를 표시합니다.
- 사용자의 프로필에 위치가 저장된 적이 있다면, 이후 위치 추적을 옵트아웃하더라도 `Location Available` 필터에 해당됩니다.

### Most Recent Device Locale 필터와 Most Recent Location 필터의 차이점은 무엇인가요? {#whats-the-difference-between-the-most-recent-device-locale-and-most-recent-location-filters}

`Most Recent Device Locale`은 사용자의 기기 설정에서 가져옵니다. 예를 들어, iPhone 사용자의 경우 기기에서 **설정** > **일반** > **언어 및 지역**에 표시됩니다. 이 필터는 날짜 및 주소와 같은 언어 및 지역 형식을 캡처하는 데 사용되며, `Most Recent Location` 필터와는 독립적입니다.

`Most Recent Location`은 기기의 마지막으로 알려진 GPS 위치입니다. 이는 세션 시작 시 업데이트되며 사용자의 프로필에 저장됩니다.

### 사용자가 위치 추적을 옵트아웃하면 이전 위치 데이터가 Braze에서 제거되나요? {#if-a-user-opts-out-of-location-tracking-is-their-previous-location-data-removed-from-braze}

아니요. 사용자의 프로필에 위치가 저장된 적이 있다면, 이후 위치 추적을 옵트아웃하더라도 해당 데이터는 자동으로 제거되지 않습니다.

## 문제 해결 {#troubleshooting}

### 사용 가능한 위치가 있는 사용자가 없음 {#no-users-have-available-locations}

Braze는 기본적으로 SDK를 통해 사용자의 가장 최근 위치를 캡처합니다. 이는 일반적으로 "최근 위치"가 사용자가 가장 최근에 앱을 사용한 위치임을 의미합니다. Braze에 백그라운드 위치 데이터를 전송하면 더 세분화된 데이터를 사용할 수 있습니다.

사용 가능한 위치가 있는 사용자가 없는 경우, 두 가지 빠른 확인을 통해 데이터 수집 및 데이터 전송을 확인할 수 있습니다.

#### 데이터 수집 {#data-collection}

앱이 위치 데이터를 수집하고 있는지 확인합니다:

- iOS의 경우, 이는 사용자가 사용자 여정의 특정 시점에서 프롬프트를 통해 위치 데이터 공유에 옵트인하는 것을 의미합니다.
- Android의 경우, 앱이 설치 시 세밀한 또는 대략적인 위치 권한을 요청하는지 확인합니다.

사용자 위치 데이터가 Braze로 전송되고 있는지 확인하려면 **Location Available** 필터를 사용하세요. 이 필터를 사용하면 "가장 최근 위치"가 있는 사용자의 비율을 확인할 수 있습니다.

!["Location Available" 필터를 사용하는 "Test Location" Segment.]({% image_buster /assets/img_archive/trouble7.png %})

#### 데이터 전송 {#data-transfer}

개발자가 Braze에 위치 데이터를 전달하고 있는지 확인합니다. 일반적으로 위치 데이터 전달은 사용자가 권한을 부여한 후 SDK에 의해 자동으로 처리되지만, 개발자가 Braze에서 위치 추적을 비활성화했을 수 있습니다. 위치 추적에 대한 자세한 내용은 다음에서 확인할 수 있습니다:
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=swift)
- [웹]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=web)