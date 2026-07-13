---
nav_title: Amplitude
article_title: Amplitude
page_order: 0
alias: /partners/amplitude_recommend/
description: "이 참조 문서에서는 제품 분석 및 비즈니스 인텔리전스 플랫폼인 Braze와 Amplitude 간의 파트너십에 대해 설명합니다."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomamplitude-integration-with-braze-stylefloatrightwidth120pxborder0-classnoimgborderamplitude}

> [Amplitude](https://amplitude.com/)는 제품 분석 및 비즈니스 인텔리전스 플랫폼입니다.

Braze와 Amplitude의 양방향 통합을 통해 [Amplitude 코호트를 가져오고]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import), 사용자 특성 및 이벤트를 Braze로 가져올 수 있으며, 향후 Campaigns 또는 Canvases에서 사용자를 타겟팅할 수 있는 Segments를 생성할 수 있습니다. 또한 Braze Currents를 활용하여 [Braze 이벤트를 Amplitude로 내보내]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents#data-export-integration) 제품 및 마케팅 데이터에 대한 심층 분석을 수행할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Amplitude 계정 | 이 파트너십을 활용하려면 [Amplitude 계정](https://amplitude.com/)이 필요합니다. |
| Currents | 데이터를 Amplitude로 다시 내보내려면 계정에 [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents)가 설정되어 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 선택 {#choose-an-integration}

Amplitude와 Braze는 두 가지 통합 방법을 제공합니다. 다음 설명서를 읽고 어떤 방법이 필요에 맞는지 결정하세요.

- Braze 이벤트 스트리밍: 원시 Amplitude 이벤트 데이터를 Braze로 직접 전달할 수 있는 통합입니다.
- [코호트 가져오기]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import): Amplitude 코호트를 Braze로 전달할 수 있는 통합입니다.

## Braze 이벤트 스트리밍 {#braze-event-streaming}

### 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Braze REST API 키 | 모든 권한이 있는 Braze REST API 키.<br><br> 이 키는 Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL][1]. 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| Braze 앱 식별자 | Amplitude 이벤트를 수신할 앱의 식별자입니다. **Braze 대시보드 > 개발자 콘솔 > 설정**에서 확인할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

### Amplitude 설정 {#amplitude-setup}

1. Amplitude에서 **Data Destinations**로 이동한 다음 "Braze - Event Stream"을 검색합니다.
2. 동기화 이름을 입력한 다음 **Create Sync**를 클릭합니다.
3. **Edit**를 클릭하고 Braze REST API 엔드포인트, REST API 키 및 Braze 앱 식별자를 입력합니다.
4. 이벤트 전송 필터를 사용하여 전송할 이벤트를 선택합니다. 모든 이벤트를 전송할 수 있지만, Amplitude에서는 가장 중요한 이벤트를 선택할 것을 권장합니다.
5. 완료되면 대상을 활성화하고 저장합니다.

이 통합에 대한 자세한 내용은 [Braze 이벤트 스트리밍](https://www.docs.developers.amplitude.com/data/destinations/braze/)을 참조하세요.

## 사용자 특성 및 계산 동기화 {#sync-user-traits-and-computations}

Audiences를 사용하여 사용자 속성정보 및 계산을 커스텀 속성으로 Braze에 전송합니다. 최근 90일 동안 활성 상태였던 사용자의 사용자 속성정보 또는 계산된 속성정보를 동기화할 수 있습니다.

사용자의 속성정보 또는 계산이 업데이트되면 Amplitude는 해당 사용자 속성정보 또는 계산과 동일한 이름으로 Braze의 커스텀 속성을 업데이트합니다.

사용자 특성 및 계산 동기화는 Braze에 아직 존재하지 않는 사용자 식별자에 대해 새 사용자를 생성합니다. 계산 및 사용자 특성은 사용자 식별자를 사용해서만 동기화할 수 있습니다. 사용자 식별자는 다음 중 하나일 수 있습니다.
- 외부 ID
- Braze ID
- 사용자 별칭
- 이메일 주소

속성정보, 추천 및 코호트를 서드파티 대상에 동기화하는 방법에 대해 자세히 알아보려면 Amplitude의 [속성정보, 추천 및 코호트를 서드파티 대상에 동기화](https://help.amplitude.com/hc/en-us/articles/360060055531) 설명서를 참조하세요.

### 사용자 속성정보 및 계산을 동기화하는 방법 {#how-to-sync-user-properties-and-computations}

Amplitude Audiences에서 **Syncs > Create Sync**를 선택합니다.

![Create Sync가 선택된 Amplitude Audiences 동기화 페이지.]({% image_buster /assets/img/amplitude11.png %})

다음으로, 사용자 속성정보, 계산, 코호트 또는 추천 중 동기화할 항목을 선택합니다.

{% tabs %}
{% tab 사용자 속성정보 동기화 %}

**User Property**를 선택한 다음 동기화할 사용자 속성정보를 선택합니다.

![동기화할 사용자 속성정보를 선택하는 Amplitude 동기화 설정 단계.]({% image_buster /assets/img/amplitude7.png %})

다음으로, 사용자 속성정보를 동기화할 대상을 선택합니다.

![속성정보를 Braze로 동기화하기 위한 Amplitude 대상 선택기.]({% image_buster /assets/img/amplitude8.png %})

마지막으로, 동기화 빈도를 정의합니다.

![케이던스를 일회성 동기화 또는 예약 동기화로 정의합니다.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% tab 계산 동기화 %}

**Computation**을 선택한 다음 동기화할 계산을 선택합니다.

![동기화할 계산을 선택하는 Amplitude 동기화 설정 단계.]({% image_buster /assets/img/amplitude10.png %})

다음으로, 계산을 동기화할 대상을 선택합니다.

![계산을 Braze로 동기화하기 위한 Amplitude 대상 선택기.]({% image_buster /assets/img/amplitude8.png %})

마지막으로, 동기화 빈도를 정의합니다.

![케이던스를 일회성 동기화 또는 예약 동기화로 정의합니다.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% endtabs %}

## 문제 해결 {#troubleshooting}

### 코호트 동기화 시 "이 필터에 대한 데이터가 아직 충분하지 않습니다" 오류 {#we-do-not-have-enough-data-yet-for-this-filter-when-syncing-a-cohort}

[Amplitude 코호트를 Braze로 가져올]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import) 때 이 오류가 발생하면 다음을 시도해 보세요.

1. **사용자 ID 정렬을 확인합니다.** Amplitude의 사용자 ID(Amplitude ID가 아님)가 Braze의 외부 사용자 ID(Braze 또는 BSON ID가 아님)와 정확히 일치해야 합니다. 예를 들어, Amplitude의 사용자 ID `12345`는 Braze의 외부 사용자 ID `12345`와 일치해야 합니다.
2. **Braze API 키를 재생성합니다.** Braze 대시보드에서 **파트너 통합** > **기술 파트너** > **Amplitude**로 이동하여 **Generate New Key**를 선택합니다. 그런 다음 새 API 키를 사용하여 Amplitude 코호트 동기화를 다시 시도합니다.
3. **Amplitude에서 코호트가 동기화되었는지 확인합니다.** Braze에서 추가 문제 해결을 진행하기 전에 [Amplitude 고객지원](https://help.amplitude.com/)에 문의하여 Amplitude 측에서 코호트가 성공적으로 동기화되었는지 확인합니다.

## Amplitude 고객 프로필 API 엔드포인트 {#amplitude-user-profile-api-endpoints}

연결된 콘텐츠와 함께 사용할 수 있는 일반적인 Amplitude API 엔드포인트를 확인하려면 전용 [Amplitude API 설명서]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_user_profile_api)를 참조하세요.