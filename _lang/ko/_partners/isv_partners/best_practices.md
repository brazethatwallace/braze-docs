---
nav_title: 모범 사례
hidden: true
---

# 고객 프로필 수명주기 및 식별자 모범 사례 {#user-lifecycle-and-identifiers-best-practices}

## 데이터 수집 {#data-collection}

Braze가 데이터를 수집하는 방법에 대해 자세히 알아보세요:
- [SDK 데이터 수집]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection)
- [데이터 수집 모범 사례]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices)
- [고객 프로필 수명주기]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)

## Braze 식별자 {#braze-identifiers}

- `braze_id`: Braze에서 할당한 식별자로, 변경할 수 없으며 데이터베이스에서 생성될 때 특정 사용자와 연결됩니다.
- `external_id`: 고객이 할당하는 식별자로, 일반적으로 UUID입니다. 사용자를 고유하게 식별할 수 있는 경우 `external_id`를 할당하는 것이 좋습니다. 사용자가 식별된 후에는 익명 사용자로 되돌릴 수 없습니다.
- `user_alias`: `external_id`가 할당되기 전에 ID로 사용자를 참조하기 위한 수단으로 고객이 할당할 수 있는 고유한 대체 식별자입니다. 사용자 별칭은 나중에 Braze [사용자 식별]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) 엔드포인트를 통해 `external_id`가 사용 가능해지면 다른 별칭이나 `external_id`와 병합할 수 있습니다.
    - [사용자 식별]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) 엔드포인트 내에서 `merge_behavior` 필드를 사용하여 알려진 고객 프로필에 유지되어야 하는 사용자 별칭 프로필의 데이터를 지정할 수 있습니다.
    - 사용자 별칭이 발송 가능한 프로필이 되려면 프로필에 이메일 및/또는 전화번호를 표준 속성으로 포함해야 합니다.
- `device_id`: 자동으로 생성되는 기기별 식별자입니다. 고객 프로필에는 여러 개의 `device_ids`를 연결할 수 있습니다. 예를 들어, 회사 컴퓨터, 집 컴퓨터, 태블릿, iOS 앱에서 계정에 로그인한 사용자는 프로필에 4개의 `device_ids`가 연결됩니다.
- 이메일 주소 및 전화번호:
    - Braze 사용자 추적 엔드포인트에서 식별자로 지원됩니다.
    - 요청 내에서 이메일 주소 또는 전화번호를 식별자로 사용하는 경우 세 가지 결과가 발생할 수 있습니다:
        1. 이 이메일/전화번호를 가진 사용자가 Braze 내에 존재하지 않는 경우, 이메일 전용/전화번호 전용 고객 프로필이 생성되며 요청의 모든 데이터가 프로필에 추가됩니다.
        2. 이 이메일/전화번호가 포함된 프로필이 이미 Braze 내에 존재하는 경우, 요청 내에서 전송된 모든 데이터를 포함하도록 업데이트됩니다.
        3. 이 이메일/전화번호를 사용하는 프로필이 두 개 이상인 사용 사례에서는 가장 최근에 업데이트된 프로필이 우선됩니다.
    - 이메일 전용/전화번호 전용 고객 프로필이 존재하는 상태에서 동일한 이메일/전화번호로 식별된 프로필이 생성되면(예: 동일한 이메일 주소와 외부 ID를 가진 다른 프로필), Braze는 두 번째 프로필을 생성합니다. 이후 업데이트는 외부 ID가 있는 프로필로 전달됩니다.
        - 두 프로필은 Braze [/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) 엔드포인트를 사용하여 병합할 수 있습니다.

## 익명 사용자 처리 {#handling-anonymous-users}

`external_id`에 액세스하지 않고 Braze에서 고객 프로필을 생성하거나 업데이트해야 하는 사용 사례의 경우, 이메일 주소나 전화번호와 같은 다른 식별자를 Braze [식별자로 사용자 내보내기]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) 엔드포인트에 전달하여 해당 사용자의 프로필이 Braze에 존재하는지 확인할 수 있습니다.

```json
{
 "email_address": "test@example.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

해당 이메일 또는 전화번호를 가진 사용자가 Braze 내에 존재하는 경우 해당 프로필이 반환됩니다. 그렇지 않으면 빈 "users" 배열이 반환됩니다. 내보내기 엔드포인트를 사용하여 해당 이메일 주소를 가진 사용자가 이미 존재하는지 확인하면, 익명 사용자 프로필이 해당 사용자와 연결되어 있는지 확인할 수 있다는 이점이 있습니다. 예를 들어, SDK를 통해 생성된 익명 프로필(`braze_id` 포함)이나 이전에 생성된 사용자 별칭 프로필이 있을 수 있습니다.

요청이 고객 프로필을 반환하지 않으면 사용자 별칭을 생성하거나 이메일 전용 사용자를 생성할 수 있습니다:

### 사용자 별칭 {#user-alias}

사용자 추적 엔드포인트를 사용하여 선택한 식별자를 별칭 이름으로 사용하여 사용자 별칭을 생성합니다. 새 사용자 별칭이 정의된 속성, 이벤트 또는 구매 오브젝트 내에서 `_update_existing_only`를 `false`로 포함하면 별칭 프로필을 생성하고 해당 프로필에 속성, 이벤트 및 구매를 동시에 추가할 수 있습니다.

사용자 별칭이 발송 가능한 프로필이 되려면 아래와 같이 `email` 필드에 이메일 주소를 포함해야 합니다.

```json
{
   "attributes": [
   {
     "user_alias" : {
       "alias_name" : "test@example.com",
       "alias_label" : "email"
     },
     "email": "test@example.com",
     "_update_existing_only": false,
     "string_attribute": "sherman",
     "boolean_attribute_1": true,
     "integer_attribute": 25,
     "array_attribute": ["banana", "apple"]
   }
   ]
}
```

나중에 [사용자 식별]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) 엔드포인트를 통해 `external_id`가 사용 가능해지면 이 사용자 별칭을 식별하고 병합할 수 있습니다.

### 이메일 전용 사용자 생성 {#creating-an-email-only-user}

사용자 추적 엔드포인트에서 이메일 주소를 식별자로 사용합니다.

```json
{
    "attributes": [
        {
            "email": "test@example.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}
```
{% alert important %}
이 기능은 현재 얼리 액세스 중입니다.
{% endalert %}

## 고객 프로필에 데이터 동기화 {#syncing-data-to-user-profiles}

[사용자 추적]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
- 고객 프로필에 속성을 기록하는 등 Braze에서 사용자를 생성하고 업데이트할 수 있는 공개적으로 액세스 가능한 엔드포인트입니다. 이 엔드포인트에는 워크스페이스 수준에서 분당 50,000건의 요청으로 사용량 제한이 적용됩니다.
- 이 엔드포인트를 사용할 때는 파트너 설명서에 표시된 대로 `partner` 키를 포함합니다.

[클라우드 데이터 수집]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview#what-is-cloud-data-ingestion)
- 사용자 추적 엔드포인트와 마찬가지로 클라우드 데이터 수집을 통해 데이터를 고객 프로필에 동기화할 수 있습니다. 이 도구를 사용할 때 동기화하려는 데이터 웨어하우스 테이블 또는 뷰를 설정하고 원하는 Braze 워크스페이스에 연결하여 속성, 이벤트 및 구매를 프로필에 기록합니다.

[데이터 포인트]({{site.baseurl}}/user_guide/data/infrastructure/data_points)
- Braze에는 값의 변경 여부와 관계없이 고객 프로필에 "쓰기"될 때마다 데이터 포인트가 기록되는 데이터 포인트 모델이 있습니다. 따라서 변경된 속성만 Braze에 전송하는 것이 좋습니다.

## 사용자 오디언스를 Braze로 보내기 {#sending-audiences-of-users-to-braze}

[코호트 가져오기 동기화 파트너 설명서]({{site.baseurl}}/partners/isv_partners/cohort_import)<br>
- Braze 코호트 가져오기 API 엔드포인트를 사용하여 사용자 오디언스를 코호트로 Braze에 동기화할 수 있습니다. 이러한 오디언스가 고객 프로필에 사용자 속성으로 저장되는 대신, 고객은 세분화 툴 내의 파트너 브랜드 필터를 통해 이 코호트를 구축하고 타겟팅할 수 있습니다. 이를 통해 특정 사용자 세그먼트를 보다 효율적으로 찾고 타겟팅할 수 있습니다.
- 코호트 가져오기 엔드포인트는 공개되지 않으며 각 파트너에 따라 다릅니다. 따라서 코호트 엔드포인트에 대한 동기화는 고객의 워크스페이스 사용량 제한에 포함되지 않습니다.

[사용자 추적]({{site.baseurl}}/api/endpoints/user_data/post_user_track)<br>
- 사용자 속성을 통해 특정 오디언스에서 사용자를 표시하여 Braze에서 사용자를 즉시 생성하는 데 사용할 수 있는 공개적으로 액세스 가능한 엔드포인트입니다. 이 엔드포인트와 코호트 가져오기 엔드포인트의 주요 차이점은, 이 엔드포인트를 사용하여 전송된 오디언스는 고객 프로필에 저장되는 반면 코호트 가져오기 엔드포인트는 세분화 툴에 필터로 표시된다는 점입니다. 이 엔드포인트에는 워크스페이스 수준에서 분당 50,000건의 요청으로 사용량 제한이 적용됩니다.
- 이 엔드포인트를 사용할 때는 [파트너 설명서]({{site.baseurl}}/partners/isv_partners/api_partner)에 표시된 대로 `partner` 키를 포함해야 합니다.

[데이터 포인트]({{site.baseurl}}/user_guide/data/infrastructure/data_points)<br>
- Braze에는 값의 변경 여부와 관계없이 고객 프로필에 "쓰기"될 때마다 데이터 포인트가 기록되는 데이터 포인트 모델이 있습니다.
- 데이터 포인트는 코호트 가져오기와 사용자 추적 엔드포인트 모두에서 발생합니다.

## 파트너로 참여 분석 스트리밍 {#engagement-analytics-streaming-to-partner}

### Currents

Currents는 Braze의 거의 실시간 메시지 참여 분석 스트리밍 도구입니다. 고객의 워크스페이스에서 전송된 Campaigns 및 Canvases에 대한 모든 발송, 전달, 열람, 클릭 등의 사용자 수준 데이터를 스트리밍합니다. 몇 가지 주의할 사항이 있습니다: Currents는 고객의 커넥터당 가격이 책정되므로 모든 신규 Currents 파트너는 EA 프로세스를 거쳐야 합니다. 커스텀 브랜드 UI를 구축하고 커넥터를 공개적으로 제공하기 전에 파트너에게 5명의 고객을 EA의 일부로 확보할 것을 요청합니다.
- [파트너 설명서]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)
- [메시지 참여 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) - Currents 커넥터를 구매한 모든 고객은 이러한 이벤트에 액세스할 수 있습니다.
- [사용자 행동 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) - Currents 커넥터를 구매하는 모든 고객이 이러한 이벤트를 포함하는 "모든 이벤트" 커넥터를 구매하는 것은 아닙니다.

### Snowflake 데이터 공유 {#snowflake-data-share}

Snowflake 데이터 공유 커넥터를 구매한 고객은 자동으로 메시지 참여 및 사용자 행동 이벤트에 모두 액세스할 수 있습니다. Snowflake 데이터 공유를 파트너 통합으로 사용하는 경우, Braze는 고객을 대신하여 파트너의 Snowflake 인스턴스에 공유를 프로비저닝합니다. 참고로, 리전 간 데이터 공유는 고객에게 더 높은 비용을 요구하므로, Snowflake와 통합하려는 파트너에게 `US-EAST-1` 및/또는 `EU-CENTRAL-1`에 계정이 필요하다는 안내를 요청합니다.
- [파트너 설명서]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)

## Campaigns 및 Canvases 구축 및 트리거 {#building-and-triggering-campaigns-and-canvases}

### Braze에서 자산 생성 {#creating-assets-in-braze}
Braze는 고객과 파트너가 고객의 워크스페이스 내에서 이메일 템플릿과 Content Blocks를 생성/업데이트할 수 있는 다양한 엔드포인트를 제공합니다. 이러한 템플릿과 Content Blocks는 고객의 Braze Campaigns 및 Canvases 전반에 걸쳐 사용할 수 있습니다.
- 이메일 템플릿
    - [템플릿 생성 엔드포인트]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template)
    - [템플릿 업데이트 엔드포인트]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template#rate-limit)
- [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks)
    - [Content Block 생성 엔드포인트]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block)
    - [Content Block 업데이트 엔드포인트]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block)

### API 트리거 Campaigns 및 Canvases {#api-triggered-campaigns-and-canvases}

고객은 Campaigns 및 Canvases가 API로 트리거되도록 설정할 수 있습니다. 이러한 Campaigns를 트리거하는 API 요청은 API 트리거 속성정보 및 오디언스 또는 수신자 매개변수를 전달하여 Campaign을 더욱 개인화하고 세분화하는 데 사용할 수 있습니다.
- [API를 통한 Campaigns 트리거]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#request-body)
    - Campaigns는 개별 이메일과 같은 단일 메시지입니다.
- [API를 통한 Canvases 트리거]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases#request-body)
    - Canvas는 마케터가 여러 메시지와 단계로 캠페인을 만들어 일관된 여정을 구성할 수 있는 통합 인터페이스입니다. Canvas를 트리거하면 사용자가 Canvas 흐름에 진입하며, Canvas 기준에 더 이상 맞지 않을 때까지 메시징을 계속 수신합니다.
- [API 트리거 속성정보/Canvas 진입 속성정보]({{site.baseurl}}/api/objects_filters/trigger_properties_object)
    - 발송 시점에 메시지에 동적으로 채워질 수 있는 데이터입니다.

### API Campaigns
API Campaigns를 생성할 때(위에서 언급한 API 트리거 Campaigns와는 다름), Braze 대시보드는 고객이 Campaign 보고를 위한 분석을 추적할 수 있는 `campaign_id`를 생성하는 데만 사용됩니다. Campaign 메시지 자체는 API 요청 내에서 정의됩니다.
- [즉시 API Campaign 보내기]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)
- [API Campaign 예약하기]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)

### 발송 ID {#send-ids}
Braze 엔드포인트를 사용하여 발송별로 Campaign 분석을 세분화하는 데 사용할 수 있는 발송 ID를 생성합니다. 예를 들어, 위치별로 `campaign_id`(API Campaign)가 생성된 경우 특정 위치에 대한 다양한 메시징의 성과를 추적하기 위해 발송별로 발송 ID를 생성할 수 있습니다.
- [발송 ID]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids)

## 연결된 콘텐츠 {#connected-content}

연결된 콘텐츠는 모든 채널 유형 내에서 발송 시점에 지정된 엔드포인트로 API 요청을 수행하고 응답으로 반환된 내용을 메시지에 채우는 데 사용할 수 있습니다.

연결된 콘텐츠의 다양한 기능 덕분에 많은 고객이 Braze에 존재하지 않거나 존재할 수 없는 콘텐츠를 삽입하는 데 이 기능을 사용하고 있습니다. 보다 일반적인 사용 사례는 다음과 같습니다:
- 블로그 또는 문서 콘텐츠를 메시지로 템플릿화
- 콘텐츠 추천
- 제품 메타데이터
- 현지화 및 번역

주의해야 할 사항:
- Braze는 API 호출에 대해 요금을 부과하지 않으며 데이터 포인트 사용량에 포함되지 않습니다.
- 연결된 콘텐츠 응답에는 1MB의 제한이 있습니다.
- 연결된 콘텐츠 호출은 메시지가 발송될 때 발생하지만, 인앱 메시지는 메시지를 볼 때 이 호출을 수행합니다.
- 연결된 콘텐츠 호출은 리디렉션을 따르지 않습니다. Braze는 성능상의 이유로 서버 응답 시간이 2초 미만이어야 합니다. 서버가 응답하는 데 2초 이상 걸리면 콘텐츠가 삽입되지 않습니다.
- Braze 시스템은 수신자당 동일한 연결된 콘텐츠 API 호출을 두 번 이상 수행할 수 있습니다. 이는 Braze가 메시지 페이로드를 렌더링하기 위해 연결된 콘텐츠 API 호출을 해야 할 수 있으며, 유효성 검사, 재시도 로직 또는 기타 내부 목적을 위해 수신자당 메시지 페이로드가 여러 번 렌더링될 수 있기 때문입니다.

연결된 콘텐츠에 대해 자세히 알아보려면 다음 문서를 참조하세요:
- [연결된 콘텐츠 호출하기]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)
- [연결된 콘텐츠 중단하기]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content)
- [연결된 콘텐츠 재시도]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries)