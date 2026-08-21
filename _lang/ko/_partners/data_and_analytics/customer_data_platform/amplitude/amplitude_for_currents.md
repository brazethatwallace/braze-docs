---
nav_title: Currents용 Amplitude
article_title: Currents용 Amplitude
page_order: 0
description: "이 참조 문서에서는 제품 분석 및 비즈니스 인텔리전스 플랫폼인 Amplitude와 Braze 커런츠 간의 파트너십에 대해 설명합니다."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Currents용 Amplitude {#amplitude-for-currents}

> [Amplitude](https://amplitude.com/)는 제품 분석 및 비즈니스 인텔리전스 플랫폼입니다.

Braze와 Amplitude의 양방향 통합을 통해 [Amplitude 코호트를 동기화]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences)하고, 사용자 특성 및 이벤트를 Braze로 가져올 수 있으며, Braze 커런츠를 활용하여 [Braze 이벤트를 Amplitude로 내보내](#data-export-integration) 제품 및 마케팅 데이터에 대한 심층 분석을 수행할 수 있습니다.

## 전제 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Amplitude 계정 | 이 파트너십을 활용하려면 [Amplitude 계정](https://amplitude.com/)이 필요합니다. |
| Currents | 데이터를 다시 Amplitude로 내보내려면 계정에 [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents)가 설정되어 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 데이터 내보내기 통합 {#data-export-integration}

Braze에서 Amplitude로 내보낼 수 있는 이벤트 및 이벤트 속성정보의 전체 목록은 다음 섹션에서 확인할 수 있습니다. Amplitude로 전송되는 모든 이벤트에는 사용자의 `external_user_id`가 Amplitude 사용자 ID로 포함됩니다. Braze 전용 이벤트 속성정보는 Amplitude로 전송되는 데이터의 `event_properties` 키 아래에 전송됩니다.

{% alert important %}
이 기능을 사용하려면 Amplitude 사용자 ID가 Braze 외부 ID와 일치해야 합니다.
{% endalert %}

Braze는 `external_user_id`가 설정된 사용자 또는 `device_id`가 설정된 익명 사용자의 이벤트 데이터만 전송합니다. 익명 사용자의 경우 SDK에서 Amplitude 기기 ID를 Braze 기기 ID와 동기화해야 합니다. 예시:

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Amplitude로 두 가지 유형의 이벤트를 내보낼 수 있습니다: 메시지 전송과 직접 관련된 Braze 이벤트로 구성된 [메시지 인게이지먼트 이벤트](#supported-currents-events)와 세션, 커스텀 이벤트, 플랫폼을 통해 추적된 구매 등 기타 앱 또는 웹사이트 활동을 포함하는 [고객 행동 이벤트](#supported-currents-events)입니다. 모든 일반 이벤트에는 `[Appboy]` 접두사가 붙고, 모든 커스텀 이벤트에는 `[Appboy] [Custom Event]` 접두사가 붙습니다. 커스텀 이벤트 및 구매 이벤트 속성정보에는 각각 `[Custom event property]`와 `[Purchase property]` 접두사가 붙습니다.

{% alert note %}
Braze 커런츠는 이벤트를 Amplitude로 내보낼 때 `[Appboy]` 접두사를 적용합니다. 이 레이블은 Braze의 이전 제품명을 참조합니다. 이는 정상적인 동작이며 SDK 또는 통합 문제를 나타내는 것이 아닙니다.
{% endalert %}

Braze로 이름이 지정되어 가져온 모든 코호트에는 `[Amplitude]` 접두사와 `cohort_id` 접미사가 붙습니다. 즉, `cohort_id`가 "abcd1234"인 "TEST_COHORT"라는 코호트는 Braze 필터에서 `[Amplitude] TEST_COHORT: abcd1234`로 표시됩니다.

추가 이벤트 권한에 대한 액세스가 필요한 경우 계정 매니저에게 문의하거나 [지원 티켓]({{site.baseurl}}/braze_support)을 열어주세요.

### 1단계: Braze에서 Amplitude 통합 구성 {#step-1-configure-amplitude-integration-in-braze}

Amplitude에서 Amplitude 내보내기 API 키를 찾습니다.

{% alert warning %}
Amplitude API 키를 최신 상태로 유지하세요. 커넥터의 자격 증명이 만료되면 커넥터가 이벤트 전송을 중지합니다. 이 상태가 **48시간** 이상 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

### 2단계: Braze Current 생성 {#step-2-create-braze-current}

Braze에서 **Currents > + Create Current > Create Amplitude Export**로 이동합니다. 나열된 필드에 통합 이름, 연락처 이메일, Amplitude 내보내기 API 키 및 Amplitude 지역을 입력합니다. 다음으로 추적할 이벤트를 선택합니다. 사용 가능한 이벤트 목록이 제공됩니다. 마지막으로 **Launch Current**를 클릭합니다.

{% alert note %}
Braze 커런츠에서 Amplitude로 전송된 이벤트는 Amplitude 이벤트 볼륨 할당량에 포함됩니다.
{% endalert %}

![Braze Amplitude Currents 페이지. 이 페이지에는 통합 이름, 연락처 이메일, API 키 및 US 지역에 대한 필드가 포함되어 있습니다. Currents 페이지의 하단에는 전송할 수 있는 사용 가능한 Currents 이벤트가 나열되어 있습니다.]({% image_buster /assets/img/amplitude4.png %})

{% alert tip %}
Amplitude API 키를 붙여넣을 때 "Invalid API key" 오류가 발생하면 키를 직접 수동으로 입력해 보세요. 일부 브라우저는 복사 및 붙여넣기 시 숨겨진 문자를 추가하여 유효성 검사 오류를 일으킬 수 있습니다.
{% endalert %}

{% tab note %}
자세한 내용은 Amplitude의 [Appboy Amplitude Integration](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration)을 참조하세요.
{% endtab %}

## 사용량 제한 {#rate-limits}

Currents는 Amplitude의 HTTP API에 연결되며, 이 API에는 기기당 초당 30개 이벤트의 [사용량 제한](https://developers.amplitude.com/docs/http-api-v2#upload-limit)과 기기당 일일 500K 이벤트의 문서화되지 않은 제한이 있습니다. 이러한 임계값을 초과하면 Amplitude는 Currents를 통해 기록된 이벤트를 제한합니다. 통합의 기기가 이 사용량 제한을 초과하면 모든 기기의 이벤트가 Amplitude에 표시되는 시점이 지연될 수 있습니다.

정상적인 상황에서 기기는 초당 30개 이벤트 또는 일일 500K 이벤트 이상을 보고하지 않아야 하며, 이러한 이벤트 패턴은 잘못 구성된 통합으로 인해서만 발생해야 합니다. 이러한 유형의 지연을 방지하려면 SDK 통합이 SDK 통합 지침에 명시된 대로 정상적인 속도로 이벤트를 보고하도록 하고, 단일 기기에 대해 많은 이벤트를 생성하는 자동화된 테스트를 실행하지 마세요.

## 지원되는 Currents 이벤트 {#supported-currents-events}

Braze는 다음 이벤트를 Amplitude로 내보내는 것을 지원합니다:

- [메시지 인게이지먼트 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [고객 행동 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

각 이벤트의 페이로드 구조는 [메시지 인게이지먼트 이벤트 용어집]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) 및 [고객 행동 이벤트 용어집]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)에서 **Amplitude** 탭을 선택하여 확인할 수 있습니다.