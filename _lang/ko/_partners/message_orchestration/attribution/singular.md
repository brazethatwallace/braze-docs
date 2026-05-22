---
nav_title: Singular
article_title: Singular
alias: /partners/singular/
description: "이 참조 문서에서는 유료 설치 경로 데이터를 가져올 수 있는 통합 마케팅 분석 플랫폼인 Singular와 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---

# Singular

> [Singular](https://www.singular.net/)는 기여도, 비용 집계, 마케팅 분석, 크리에이티브 보고 및 워크플로 자동화를 제공하는 통합 마케팅 분석 플랫폼입니다.

_이 통합은 Singular에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Braze와 Singular 통합을 통해 유료 설치 경로 데이터를 가져와 생애주기 캠페인 내에서 지능적으로 세그먼트할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Singular 계정 | 이 파트너십을 활용하려면 Singular 계정이 필요합니다. |
| iOS 또는 Android 앱 | 이 통합은 iOS 및 Android 앱을 지원합니다. 플랫폼에 따라 애플리케이션에 코드 스니펫이 필요할 수 있습니다. 이러한 요구 사항의 세부 정보는 통합 프로세스의 1단계에서 확인할 수 있습니다. |
| Singular SDK | 필수 Braze SDK 외에도 [Singular SDK](https://support.singular.net/hc/en-us/articles/360037640172-Getting-Started-with-the-Singular-SDK-S2S)를 설치해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합 {#integration}

### 1단계: 사용자 ID 매핑 {#step-1-map-user-ids}

#### Android

Android 앱이 있는 경우 고유한 Braze 사용자 ID를 Singular에 전달하는 다음 코드 스니펫을 포함해야 합니다.

```java
String appboyDeviceId = Braze.getInstance(context).getDeviceId();
SingularConfig config = new SingularConfig("SDK KEY", "SDK SECRET")
  .withGlobalProperty(“brazeDeviceID”, appboyDeviceId, true);
```
#### iOS

{% alert important %}
2023년 2월 이전에는 Singular 기여도 통합에서 IDFV(Identifier for Vendor)를 기본 식별자로 사용하여 iOS 기여도 데이터를 매칭했습니다. Objective-C를 사용하는 Braze 고객은 서비스 중단이 발생하지 않으므로 설치 시 Braze `device_id`를 가져와서 Singular로 전송할 필요가 없습니다.
{% endalert%}

Swift SDK v5.7.0 이상을 사용하는 경우 IDFV를 상호 식별자로 계속 사용하려면 `useUUIDAsDeviceId` 필드를 `false`로 설정하여 통합이 중단되지 않도록 해야 합니다.

`true`로 설정한 경우, 앱 설치 시 Braze `device_id`를 Singular로 전달하여 Braze가 iOS 기여도를 적절히 매칭하도록 Swift용 iOS 기기 ID 매핑을 구현해야 합니다.

{% tabs local %}
{% tab Objective-C %}

```objc
SingularConfig* config = [[SingularConfig
  alloc] initWithApiKey:SDKKEY andSecret:SDKSECRET];

  [config setGlobalProperty:@"brazeDeviceId" withValue:brazeDeviceId
  overrideExisting:YES];
  [Singular start:config];
```

{% endtab %}
{% tab Swift%}

```swift
config.setGlobalProperty("brazeDeviceId", withValue: brazeDeviceId, overrideExisting: true)
```

{% endtab %}
{% endtabs %}

### 2단계: Braze 데이터 가져오기 키 받기 {#step-2-get-the-braze-data-import-key}

Braze에서 **파트너 통합** > **기술 파트너**로 이동하여 **Singular**를 선택합니다.

여기에서 REST 엔드포인트를 확인하고 Braze 데이터 가져오기 키를 생성할 수 있습니다. 키가 생성된 후에는 새 키를 만들거나 기존 키를 무효화할 수 있습니다.

통합을 완료하려면 데이터 가져오기 키와 REST 엔드포인트를 Singular 계정 매니저에게 제공해야 합니다.<br><br>![Singular 기술 페이지에 있는 '설치 경로에 대한 데이터 가져오기' 상자를 보여주는 이미지입니다. 이 상자에 데이터 가져오기 키와 REST 엔드포인트가 표시됩니다.]({% image_buster /assets/img/attribution/singular.png %}){: style="max-width:90%;"}

### 3단계: 통합 확인 {#step-3-confirm-the-integration}

Braze가 Singular로부터 기여도 데이터를 수신하면, Braze의 Singular 기술 파트너 페이지의 연결 상태 표시기가 "연결되지 않음"에서 "연결됨"으로 변경되고 마지막으로 성공한 요청의 타임스탬프가 포함됩니다.

이 상태는 Braze가 기여도 설치에 대한 데이터를 수신한 후에만 변경됩니다. Braze는 오가닉 설치를 무시하고(Singular 포스트백에서 제외) 연결 성공 여부를 판단할 때 이를 계산하지 않습니다.

## Facebook 및 X(구 Twitter) 기여도 데이터 {#facebook-and-x-formerly-twitter-attribution-data}

Facebook 및 X(구 Twitter) 캠페인의 기여도 데이터는 파트너를 통해 제공되지 않습니다. 이러한 미디어 소스는 파트너가 서드파티와 기여도 데이터를 공유하는 것을 허용하지 않으므로 파트너는 해당 데이터를 Braze로 전송할 수 없습니다.

## Braze에서 Singular 클릭 추적 URL 사용(선택 사항) {#singular-click-tracking-urls-in-braze-optional}

Braze 캠페인에서 클릭 추적 링크를 사용하면 어떤 캠페인이 앱 설치와 재참여를 유도하는지 쉽게 파악할 수 있습니다. 그 결과, 마케팅 활동을 보다 효과적으로 측정하고 ROI를 극대화하기 위해 더 많은 리소스를 투자할 위치에 대해 데이터 중심의 의사 결정을 내릴 수 있습니다.

Singular 클릭 추적 링크를 시작하려면 Singular의 [설명서](https://support.singular.net/hc/en-us/articles/360030934212-Singular-Links-FAQ?navigation_side_bar=true)를 방문하세요. Singular 클릭 추적 링크를 Braze 캠페인에 직접 삽입할 수 있습니다. 그러면 Singular는 [확률적 기여도 방법론](https://support.singular.net/hc/en-us/articles/115000526963-Understanding-Singular-Mobile-App-Attribution?navigation_side_bar=true)을 사용하여 링크를 클릭한 사용자의 기여도를 분석합니다. Braze 캠페인에서 기여도의 정확성을 개선하기 위해 Singular 추적 링크에 기기 식별자를 추가하는 것이 좋습니다. 이렇게 하면 링크를 클릭한 사용자를 결정론적으로 기여도 분석할 수 있습니다.

{% tabs local %}
{% tab Android %}
Android의 경우, Braze에서는 고객이 [Google 광고 ID 수집(GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)에 옵트인할 수 있습니다. GAID는 Singular SDK 통합을 통해서도 기본적으로 수집됩니다. 다음 Liquid 로직을 사용하여 Singular 클릭 추적 링크에 GAID를 포함할 수 있습니다:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOS의 경우, Braze와 Singular 모두 SDK 통합을 통해 기본적으로 IDFV를 자동으로 수집합니다. 이를 기기 식별자로 사용할 수 있습니다. 다음 Liquid 로직을 사용하여 Singular 클릭 추적 링크에 IDFV를 포함할 수 있습니다:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**이 권장 사항은 순전히 선택 사항입니다.**<br>
기기 식별자(IDFV 또는 GAID 등)를 현재 클릭 추적 링크에 사용하지 않거나 앞으로도 사용할 계획이 없는 경우에도 Singular는 확률적 모델링을 통해 이러한 클릭의 기여도를 분석할 수 있습니다.
{% endalert %}