---
nav_title: 문제 해결
article_title: Segment 문제 해결
page_order: 9
page_type: reference
tool:
  - Segments
description: "이 참조 문서에서는 Segment를 사용할 때 염두에 두어야 할 문제 해결 단계와 고려 사항을 다룹니다."
---

# Segment 문제 해결 {#troubleshoot-segments}

> 이 페이지에서는 Braze에서 Segment를 생성하고 관리할 때 발생할 수 있는 일반적인 문제와 질문을 다룹니다.

## 오류 {#errors}

### 타겟 오디언스가 너무 복잡하여 시작할 수 없음 {#target-audience-is-too-complex-to-launch}

이 드문 오류는 타겟 오디언스에 너무 많은 정규식 값, 지나치게 긴 정규식 값, 지나치게 상세한 필터(예: "30,000개의 우편번호 중 하나에 해당")가 포함되어 있거나 필터가 너무 많을 때 발생합니다. 여기에는 참조된 Segment 내의 필터이든 **타겟 오디언스** 단계에서 필터로 추가된 것이든 Campaign 또는 Canvas 오디언스의 모든 필터가 포함됩니다.

![복잡도 임계값에 도달한 타겟 오디언스에 대한 오류.]({% image_buster /assets/img/segment/target_audience_too_complex_error.png %})

Campaign 또는 Canvas에 Segment 필터를 추가하면 해당 필터는 Braze에서 쿼리로 변환됩니다(이러한 쿼리의 문자 수는 대시보드 사용자가 보는 문자 수와 1:1로 대응하지 않습니다). Braze가 Campaign 또는 Canvas를 발송할 때, 타겟 오디언스의 모든 필터를 결합하는 쿼리를 실행합니다. 타겟 오디언스에 대한 결과 쿼리의 문자 수를 제한하는 임계값이 적용됩니다. 주어진 Campaign 또는 Canvas에 대해, 모든 추가 필터를 포함하여 참조된 모든 Segment의 문자 수를 합산합니다. 주어진 Segment에 대해, 모든 필터와 필터 값의 문자 수를 합산합니다.

Campaign, Canvas 또는 Segment가 임계값을 초과하여 시작할 수 없는 경우 대시보드에 오류가 표시됩니다. 이 오류가 발생하면 다시 시작하기 전에 타겟 오디언스를 단순화하세요:

- 오디언스가 여러 Segment를 참조하는 경우, 동일한 필터가 여러 Segment에 나타나는 등의 중복이 없는지 확인하세요.
- Segment 필터에서 오래된 데이터를 참조하고 있지 않은지 확인하세요. 예를 들어, Canvas가 몇 달 전에 중지되었음에도 불구하고 지난 주에 특정 캔버스 단계를 받지 않은 사용자를 찾는 오래된 필터가 있을 수 있습니다.
- 사용자 ID 또는 이메일 목록에 불과한 Segment(주로 정규식 필터를 사용하는 경우)는 [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/)로 변환하여 단일 CSV 필터로 단순화할 수 있습니다.
- CDI를 사용하는 경우, 데이터 웨어하우스에서 직접 그룹을 가져오는 CDI Segment를 생성할 수 있습니다.

필터 최적화에 대한 추가 지원이 필요하면 [고객지원에 문의]({{site.baseurl}}/braze_support/)할 수도 있습니다.

{% alert note %}
문자 수 제한은 2025년 4월부터 적용되기 시작했습니다. 2025년 4월 이전에 시작된 Campaigns 및 Canvases는 면제되어 제한을 계속 초과할 수 있지만, 새로 생성된 Campaigns 및 Canvases는 제한을 초과할 수 없습니다. 면제된 Campaign 또는 Canvas를 편집하거나 복제하는 경우, 오디언스가 제한 이하로 업데이트될 때까지 시작할 수 **없습니다**.
{% endalert %}

### X개의 활성 또는 중지된 Campaigns 또는 Canvases가 오디언스 복잡도 임계값을 초과함 {#x-active-or-stopped-campaigns-or-canvases-exceed-the-audience-complexity-threshold}

이 배너는 활성 또는 중지된 Campaigns 또는 Canvases의 오디언스가 오디언스 복잡도 임계값을 초과할 때마다 Campaign 또는 Canvas 목록 상단에 표시됩니다. 배너를 선택하면 임계값을 초과하는 Campaigns 또는 Canvases만 필터링하여 표시한 다음, [타겟 오디언스가 너무 복잡하여 시작할 수 없음](#target-audience-is-too-complex-to-launch)의 문제 해결 단계를 따르세요.

![4개의 활성 또는 중지된 Canvases가 오디언스 복잡도 임계값을 초과한다는 오류 배너.]({% image_buster /assets/img/segment/audience_complexity_threshold_banner.png %})

### 필터가 10,000바이트를 초과하거나 너무 길어서 저장할 수 없음 {#filter-exceeds-10000-bytes-or-is-too-long-to-save}

Braze는 개별 Segment 필터를 최대 10,000바이트로 제한하며, 이는 영문 10,000자 또는 일본어 3,333자에 해당합니다. 개별 필터가 10,000바이트를 초과하면 해당 필터가 Segment 내에 있든 Campaign 또는 Canvas에 직접 추가되었든 경고가 나타납니다.

![10,000자를 초과하는 값을 가진 필터에 대한 오류 배너.]({% image_buster /assets/img/segment/filter_error.png %})

![속성 값이 10,000자를 초과하는 커스텀 속성 필터 `menu_item`에 대한 오류.]({% image_buster /assets/img/segment/segment_filter_error.png %})

이 오류는 매우 드물게 발생하지만, 발생할 경우 일반적으로 사용자 ID 또는 이메일 주소 목록을 대상으로 하는 정규식 필터에서 나타납니다. 이 경우 다음 단계에 따라 필터를 CSV로 변환할 수 있습니다:

1. 영향을 받는 Segment 또는 특정 정규식 필터에서 사용자를 내보냅니다.
2. 필요에 따라 CSV를 정리합니다. Braze ID 또는 Appboy ID가 필요하지만, 필요하지 않은 다른 열은 모두 제거할 수 있습니다. 또한 데이터가 최신인지 확인하는 것이 좋습니다(예: 더 이상 타겟팅하지 않는 사용자를 제거).
3. CSV 파일을 다시 [가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/)하면 사용자가 자동으로 단일의 매우 효율적인 CSV 기반 필터로 그룹화됩니다.

## 사용자 동작 {#user-behavior}

### 사용자가 더 이상 Segment에 포함되지 않음 {#user-is-no-longer-in-a-segment}

Segment를 생성할 때 사용자를 찾을 수 없는 경우, Segment 자격을 결정하는 사용자 데이터가 해당 사용자의 자체 활동이나 이전에 상호작용한 다른 Campaigns 및 Canvases의 결과로 변경되었을 수 있습니다. 재자격이 활성화되어 있으면 고객 프로필에 수신된 Campaign의 최신 데이터가 표시됩니다.

### 특정 앱으로 필터링할 때 다른 앱의 사용자 정보가 표시됨 {#info-displays-for-users-of-other-apps-when-i-filter-for-a-specific-app}

사용자는 여러 앱을 가질 수 있으므로, 세분화 페이지의 **사용한 앱** 섹션에서 특정 앱을 선택하면 해당 앱을 최소한 하나 가지고 있는 사용자에 대한 결과가 표시됩니다. 이 필터는 해당 앱만 독점적으로 가지고 있는 사용자에 대한 결과를 표시하지 않습니다.

## 필터링 {#filtering}

### 필터 옵션이 변경됨 {#filter-options-changed}

필터 옵션은 커스텀 속성에 대해 Braze에 전달하는 형식(데이터 유형)과 관련이 있습니다. Braze가 커스텀 속성에 대해 인식하는 데이터 유형을 확인하려면 **데이터 설정** > **커스텀 속성**으로 이동하세요.

필터 옵션이 변경된 경우, 이는 데이터가 이전과 다른 형식(데이터 유형)으로 Braze에 전달되고 있음을 나타냅니다. 다양한 데이터 유형과 필터링 옵션에 대한 자세한 설명은 [커스텀 속성 데이터 유형]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types)을 참조하세요.

대시보드에서 커스텀 속성의 데이터 유형을 변경하면 다른 형식으로 Braze에 전송되는 데이터가 거부된다는 점에 유의하세요.

## 분석 및 보고 {#analytics-and-reporting}

### Campaign 분석의 *발송된 메시지* 또는 *고유 수신자*가 Segment 수와 일치하지 않음 {#message-sent-or-unique-recipients-in-campaign-analytics-doesnt-match-segment-count}

Campaign 분석의 *발송된 메시지* 또는 *고유 수신자* 수가 Segment 필터 `Campaign X에서 메시지를 수신함`의 사용자 수와 일치하지 않는 경우, 세 가지 가능한 이유가 있습니다.

1. **Campaign 시작 이후 사용자가 아카이브, 분리 또는 삭제되었을 수 있습니다**<br><br>예를 들어, 1,000명의 사용자가 Campaign을 수신하고 같은 날 CSV 내보내기를 수행한다고 가정합니다. 1,000명의 사용자가 보고됩니다. 다음 달 동안 해당 1,000명 중 50명이 삭제됩니다(예: `users/delete` 엔드포인트에 의해). 다시 CSV 내보내기를 수행하면 950명의 사용자가 보고되지만, **Campaign 분석**의 *고유 수신자* 수는 여전히 1,000입니다.<br><br>즉, *고유 수신자* 측정기준은 누적 카운트인 반면, 세분화 도구와 CSV 내보내기는 현재 존재하는 사용자의 수를 제공합니다.<br><br>

2. **Campaign에 재자격이 설정되어 사용자가 Campaign에 여러 번 재진입할 수 있습니다**<br><br>예를 들어, 이메일 Campaign에 재자격이 0분으로 설정되어 있고(사용자가 오디언스 Segment 요구 사항을 충족하는 한 Campaign에 재진입할 수 있음), Campaign이 한 달 이상 실행되고 있다고 가정합니다. **Campaign 분석**의 *발송된 메시지* 수는 이 필드에 중복 사용자에게 발송된 메시지가 포함되므로 Segment의 수와 일치하지 않습니다.<br><br>이는 Braze가 고유 사용자를 *일일 고유 수신자*, 즉 하루에 특정 메시지를 수신한 사용자 수로 계산하기 때문입니다. 이는 재자격 사용자가 "고유" 기간이 하루에 불과하므로 고유 수신자로 두 번 이상 계산됨을 의미합니다. 이로 인해 *일일 고유 수신자* 수가 CSV 내보내기의 고객 프로필 수보다 높을 수 있습니다. CSV 파일의 고객 프로필은 진정한 고유 사용자입니다.<br><br>

3. **채널 식별자를 공유하는 사용자가 필터에 일치했습니다**<br><br>`Campaign X에서 메시지를 수신함` 필터(및 기타 "수신" 필터)는 메시지를 수신, 열람 또는 클릭한 사람과 채널 식별자를 공유하는 사용자와 일치할 수 있습니다.

### 사용자가 하나의 앱에서만 세션을 기록했음에도 두 개의 앱에 할당됨 {#user-is-assigned-to-two-apps-despite-logging-a-session-in-only-one-app}

Segment를 생성할 때 [특정 앱을 사용한]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#step-3-choose-your-app-or-platform) 사용자를 타겟팅할 수 있습니다. 사용자가 특정 앱에 할당되려면 해당 앱에서 세션이 있어야 하지만, 앱에서 세션을 기록하지 않고도 특정 앱에 할당될 수 있는 두 가지 시나리오가 있습니다.

첫 번째 시나리오는 `/users/track` 엔드포인트를 사용할 때 `app_id` 필드가 채워지는 경우입니다. 구체적으로 다음 예시와 같이 [이벤트]({{site.baseurl}}/api/objects_filters/event_object/) 또는 [구매 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object/)를 사용할 때입니다:

```json
{
    "events": [
    {
      "external_id": "john_doe123",
      "app_id": "my_web_app_id",
      "name": "Custom Event",
      "time": "2025-08-17T19:20:30+1:00"
    }
  ]
}
```

두 번째 시나리오는 `/users/track` 엔드포인트를 사용하여 푸시 토큰을 마이그레이션할 때 `app_id` 필드가 채워지는 경우입니다. 다음 예시와 같습니다:

```json
{
"app_group_id": "{YOUR_APP_GROUP_ID}",
"attributes": [
{
      "push_token_import": false,
      "external_id": "external_id1",
      "country": "US",
      "language": "en",
      "{YOUR_CUSTOM_ATTRIBUTE}": "{YOUR_VALUE}",
      "push_tokens": [
        {"app_id": "{APP_ID_OF_OS}", "token": "{PUSH_TOKEN_STRING}"}
      ]
  }
]
}
```
