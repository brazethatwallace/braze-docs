---
nav_title: Looker
article_title: Looker
alias: /partners/looker/
description: "이 참조 문서에서는 비즈니스 인텔리전스 및 빅데이터 분석 플랫폼인 Braze와 Looker 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/looker-integration-with-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Looker {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomlooker-integration-with-braze-stylefloatrightwidth120pxborder0-classnoimgborderlooker}

> 비즈니스 인텔리전스 및 빅데이터 분석 플랫폼인 [Looker](https://looker.com/)를 사용하면 실시간 비즈니스 분석을 원활하게 탐색, 분석 및 공유할 수 있습니다.

Braze와 Looker 통합을 통해 회사 사용자는 REST API를 통한 퍼스트파티 [Looker Blocks](#looker-blocks) 및 [Looker 작업](#looker-actions) 사용자 플래깅을 활용할 수 있습니다. 플래그가 지정된 사용자를 Segments에 추가하여 향후 Braze Campaigns 또는 Canvases를 [타겟팅](#segment-users)할 수 있습니다. Braze와 함께 Looker를 사용하려면 [Braze 커런츠를 사용하여 데이터 웨어하우스]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners)로 Braze 데이터를 전송한 다음, Braze Looker Blocks를 사용하여 Looker에서 Braze 데이터를 빠르게 모델링하고 시각화하는 것을 권장합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Looker 계정 | 이 파트너십을 활용하려면 [Looker 계정](https://looker.com/)이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents)에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

### 고려 사항 {#considerations}

- 이 프로세스는 피벗되지 않은 데이터에서만 작동합니다.
- API는 한 번에 최대 100,000개의 행을 처리합니다.
- 중복 또는 비사용자로 인해 사용자 플래그의 최종 수가 더 낮을 수 있습니다.

## 통합 {#integration}

### Looker Blocks {#looker-blocks}

Looker Blocks는 Braze 고객이 [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)를 통해 제공하는 세분화된 데이터 뷰에 빠르게 접근할 수 있도록 도와줍니다. 블록은 Currents 데이터에 대한 사전 제작된 시각화 및 모델링을 제공하므로 Braze 고객은 유지와 같은 분석 패턴을 쉽게 구현하고, 메시지 전달 가능성을 평가하고, 사용자 동작을 더 자세히 살펴볼 수 있습니다.

Looker Blocks를 구현하려면 GitHub 코드의 README 파일에 있는 지침을 따르세요.
- [메시지 인게이지먼트 분석 블록 README](https://github.com/llooker/braze_message_engagement_block/blob/master/README.md)
- [사용자 동작 분석 블록 README](https://github.com/llooker/braze_retention_block/blob/master/README.md)

두 통합 모두 [초기 Braze 통합]({{site.baseurl}}/user_guide/get_started/sdk_overview)과 Looker 호환 [데이터 웨어하우스](https://looker.com/solutions/other-databases?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)와의 Braze 통합이 필요한 데이터를 캡처하고 전송하도록 적절히 구성되어 있다고 가정합니다.


{% alert important %}
Braze는 [Snowflake](https://www.snowflake.com/)를 데이터 웨어하우스로 사용하여 Looker Blocks를 구축했습니다. 가능한 한 많은 데이터 웨어하우스에서 블록이 작동하도록 하는 것을 목표로 하지만, 일부 SQL 함수는 방언에 따라 가용성, 구문 또는 동작이 다를 수 있습니다.
{% endalert %}

{% alert warning %}
다른 명명 규칙에 유의하세요! 커스텀 이름은 모든 해당 이름을 변경하지 않으면 데이터 불일치를 유발할 수 있습니다. View/테이블 또는 모델 이름을 커스터마이징한 경우 LookML에서 각각을 선택한 이름으로 변경하세요.
{% endalert %}

### 사용 가능한 블록 {#available-blocks}

| 블록 | 설명 |
|---|---|
| 메시지 인게이지먼트 분석 블록 | 이 블록에는 푸시, 이메일, 인앱 메시지, 웹훅, 전환, Canvas 진입 및 Campaign 대조군 등록 이벤트에 대한 데이터가 포함됩니다. <br><br>이 [Looker 블록](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)에 대해 자세히 알아보거나 [GitHub 코드](https://github.com/llooker/braze_message_engagement_block)를 확인하세요. |
| 사용자 동작 분석 블록 | 이 블록에는 커스텀 이벤트, 구매, 세션, 위치 이벤트 및 제거에 대한 데이터가 포함됩니다.<br><br>이 [Looker 블록](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)에 대해 자세히 알아보거나 [GitHub 코드](https://github.com/llooker/braze_retention_block)를 확인하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용 가능한 블록" }

### Looker 작업 {#looker-actions}

Looker 작업을 사용하면 Looker Look에서 REST API 엔드포인트를 통해 Braze 내 사용자에게 플래그를 지정할 수 있습니다. 작업을 사용하려면 차원에 `braze_id` 태그가 지정되어 있어야 합니다. 작업은 플래그가 지정된 값을 사용자의 `looker_export` 커스텀 속성에 추가합니다.

{% alert important %}
기존 사용자만 플래그가 지정됩니다. Braze에서 데이터에 플래그를 지정할 때 피벗된 Look은 사용할 수 없습니다.
{% endalert %}

#### 1단계: Braze Looker 작업 설정 {#step-1-set-up-a-braze-looker-action}

Braze REST API 키와 REST 엔드포인트를 사용하여 Braze Looker 작업을 설정합니다.

![Looker Braze 구성 페이지. 여기에서 Braze API 키와 Braze REST API 엔드포인트에 대한 필드를 찾을 수 있습니다.]({% image_buster /assets/img/braze-looker-action.png %})

#### 2단계: Looker Develop 설정 {#step-2-set-up-looker-develop}

Looker Develop 내에서 적절한 뷰를 선택합니다. 차원 태그에 `braze_id`를 추가하고 변경 사항을 커밋합니다.
이 `braze_id` 태그는 어떤 필드가 고유 키인지 결정하는 데 사용됩니다.

```lookml
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

**변경 사항을 반드시 커밋하세요. Looker 작업은 프로덕션 설정에서만 작동합니다.**

#### 3단계: 태그에서 사용자 속성 설정 {#step-3-set-user-attributes-in-tags}

선택적으로, 괄호 안에 속성 이름이 포함된 `braze[]` 태그를 사용하여 모든 속성을 설정할 수 있습니다. 예를 들어, 커스텀 속성 `user_segment`를 전송하려면 태그는 `braze[user_segment]`가 됩니다.

다음 제한 사항에 유의하세요:
- 속성은 **Look 내에 필드로 포함된** 경우에만 전송됩니다.
- 지원되는 유형은 `Strings`, `Boolean`, `Numbers`, `Dates`입니다.
- 속성 이름은 대소문자를 구분합니다.
- [표준 고객 프로필]({{site.baseurl}}/api/endpoints/user_data#braze-user-profile-fields) 이름과 정확히 일치하는 한 표준 속성도 설정할 수 있습니다.
- 전체 태그는 따옴표 안에 형식화되어야 합니다. 예: `tags: ["braze[first_name]"]`. 다른 태그도 할당할 수 있지만 무시됩니다.
- 추가 정보는 [GitHub](https://github.com/looker/actions/tree/master/src/actions/braze)에서 확인할 수 있습니다.

#### 4단계: Looker 작업 전송 {#step-4-send-the-looker-action}

1. `braze_id` 차원이 선택된 Look 내에서 도구 모음의 설정 기어(<i class="fas fa-cog"></i>)를 클릭하고 **Send...**를 선택합니다.
2. 커스텀 Braze 작업을 선택합니다.
3. **Unique Key** 아래에서 Braze 계정의 기본 사용자 매핑 키(`external_id` 또는 `braze_id`)를 제공합니다.
4. 내보내기에 이름을 지정합니다. 이름을 지정하지 않으면 `LOOKER_EXPORT`가 사용됩니다.
5. **Advanced Options** 아래에서 **Results in Table** 또는 **All Results**를 선택한 다음 **Send**를 클릭합니다.<br><br>![Braze 작업과 고급 옵션이 선택된 Looker 전송 대화 상자.]({% image_buster /assets/img/send-looker-action.png %})<br><br>내보내기가 올바르게 전송되면 `LOOKER_EXPORT`가 작업에서 입력한 값과 함께 사용자 프로필에 커스텀 속성으로 나타납니다.<br><br>![LOOKER_EXPORT 커스텀 속성 값이 표시된 Braze 사용자 프로필.]({% image_buster /assets/img/custom-attributes-looker.png %})

##### 발신 API 예시 {#example-outgoing-api}

다음은 [`/users/track/` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)로 전송되는 발신 API 호출의 예시입니다.

###### 헤더 {#header}
```
Authorization: Bearer [API_KEY]
```

###### 본문 {#body}
```json
{
   "attributes" : [
      {
        "external_id" : "user_01",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_02",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_03",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      .....
   ]
}
```

### Braze에서 사용자 세그먼팅 {#segment-users}

Braze에서 플래그가 지정된 사용자의 Segment를 생성하려면 **인게이지먼트** 아래의 **Segments**로 이동하여 Segment 이름을 지정하고 필터로 **Looker_Export**를 선택합니다. 그런 다음 "includes value" 옵션을 사용하고 Looker에서 할당한 커스텀 속성 플래그를 제공합니다.

![Braze Segment 빌더에서 "looker_export" 필터가 "includes_value" 및 "Looker"로 설정되어 있습니다.]({% image_buster /assets/img/braze_segments.png %})

저장한 후 타겟팅 사용자 단계에서 Canvas 또는 Campaign 생성 시 이 Segment를 참조할 수 있습니다.

## 문제 해결 {#troubleshooting}
Looker 작업에 문제가 있는 경우 [내부 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups)에 테스트 사용자를 추가하고 다음 사항을 확인하세요:

* API 키에 `users.track` 권한이 있는지 확인합니다.
* `https://rest.iad-01.braze.com`과 같이 올바른 REST 엔드포인트가 입력되었는지 확인합니다.
* 차원 뷰에 `braze_id` 태그가 설정되어 있는지 확인합니다.
* 쿼리에 ID 차원 또는 속성이 열로 포함되어 있는지 확인합니다.
* Looker 결과가 피벗되지 않았는지 확인합니다.
* 고유 키가 올바르게 선택되었는지 확인합니다. 일반적으로 `external_id`입니다.
* 차원의 `braze_id`는 API의 `braze_id`와 다릅니다. 차원의 `braze_id`는 Braze API의 `id` 필드임을 나타내는 데 사용됩니다. 대부분의 경우 전송 시 `external_id`가 기본 키입니다.
* `external_id` 사용자가 Braze 플랫폼에 존재하는지 확인합니다.
* `looker_export` 필드가 `Braze Platform > Settings > Manage Settings > Custom Attributes`에서 `Automatically Detect`로 설정되어 있는지 확인합니다.
* 변경 사항이 프로덕션에 커밋되었는지 확인합니다. Looker 작업은 프로덕션 설정에서 작동합니다.