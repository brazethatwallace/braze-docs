---
nav_title: "보고서"
article_title: "보고서"
page_order: 21
description: "이 참조 문서에서는 Braze에서 사용되는 SMS, MMS, RCS 측정기준과 SMS, MMS, RCS 캠페인에서 이를 확인하는 방법을 다룹니다."
alias: /sms_mms_rcs_reporting/
page_type: reference
tool:
  - Reports
channel:
  - SMS
  - MMS
  - RCS

---

# SMS, MMS, RCS 보고서 {#reporting-for-sms-mms-and-rcs}

> 이 참조 문서에서는 Braze에서 사용되는 SMS, MMS, RCS 측정기준과 SMS, MMS, RCS 캠페인에서 이를 확인하는 방법을 다룹니다.

{% multi_lang_include analytics/campaign_analytics.md channel="SMS" %}

{% alert note %}
*총 클릭 수*와 같은 대시보드 클릭 측정기준에는 봇 활동으로 의심되는 항목이 제외되지만, Currents는 데이터 웨어하우스 조정을 위해 `is_suspected_bot_click` 및 `suspected_bot_click_reason`이 포함된 모든 클릭 이벤트를 내보냅니다. 영향을 받는 대시보드 측정기준, 세분화 및 오케스트레이션에 대한 자세한 내용은 [SMS/RCS 링크에 대한 봇 클릭 필터링]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/bot_click_filtering)을 참조하세요.
{% endalert %}

## SMS 옵트인 및 옵트아웃 추적 {#track-sms-opt-ins-and-opt-outs}

다음 방법을 사용하여 SMS 옵트인 및 옵트아웃을 추적할 수 있습니다.

| 방법 | 설명 |
|--------|-------------|
| 세그먼터 | 세그먼터는 특정 [구독 그룹]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#subscription-group)의 사용자 수를 표시합니다. 전화번호 기준으로 중복을 제거하지 않으므로, 여러 사용자가 동일한 전화번호를 공유하는 경우 각 인스턴스가 별도로 집계됩니다. |
| 구독 그룹 시계열 | 이메일 및 전화번호에 대한 구독의 일별 스냅샷을 제공합니다. 시계열은 구독, 탈퇴, 재구독을 집계합니다. 예를 들어, 사용자가 구독한 후 탈퇴하고 다시 재구독하면 구독 사용자 1명으로 집계됩니다. |
| Currents | Currents를 사용하여 자체 보고서를 위한 [구독 및 인게이지먼트 이벤트]({{site.baseurl}}/message_events_glossary)를 내보낼 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS 옵트인 및 옵트아웃 추적" }

{% alert note %}
**SMS/MMS/RCS 성과** 패널의 _옵트인_ 및 _옵트아웃_ 통계는 인바운드 키워드를 통해 옵트인 또는 옵트아웃한 사용자를 반영합니다(예: 옵트인의 경우 "START", 옵트아웃의 경우 "STOP" 문자 전송). 이 수치는 일반적으로 세그먼터에 표시되는 수치보다 낮습니다. 이는 SMS에 가입한 총 사용자 수가 아니라 해당 키워드가 전송된 횟수를 집계하기 때문입니다.
{% endalert %}

### SMS Campaign 옵트아웃 추적 {#track-sms-campaign-opt-outs}

구독 그룹 상태 변경 테이블 대신 인바운드 수신 테이블을 사용하여 Campaign 수준에서 SMS 옵트아웃을 추적할 수 있습니다. 예를 들어, [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/query_builder) 또는 데이터 웨어하우스에서 `USERS_MESSAGES_SMS_INBOUNDRECEIVE` 또는 [`USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED`]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) 테이블을 참조하는 쿼리를 실행할 수 있습니다.

이 예시 쿼리는 `USERS_MESSAGES_SMS_INBOUNDRECEIVE` 테이블을 참조합니다:

```sql
SELECT *
FROM USERS_MESSAGES_SMS_INBOUNDRECEIVE
WHERE app_group_id = 'app-group-id'
AND subscription_group_api_id = 'subscription_group_api_id'
AND action = 'Unsubscribed'
AND (campaign_id IS NOT NULL OR canvas_id IS NOT NULL);
```

이 쿼리는 지정된 워크스페이스 및 구독 그룹에서 SMS 커뮤니케이션을 옵트아웃한 사용자를 반환하며, Campaigns 또는 Canvases와 연결된 사용자만 필터링합니다.

### 옵트아웃 타이밍 {#opt-out-timing}

Currents 또는 데이터 웨어하우스의 키워드 및 인바운드 메시지 이벤트(예: [`users.messages.sms.InboundReceive`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events)의 타임스탬프 또는 구독 그룹 상태 변경 이벤트)는 Braze가 옵트아웃을 기록한 시점에 대한 권위 있는 소스입니다.

{% alert note %}
이벤트 타임스탬프는 Braze가 인바운드 메시지를 수신하거나 처리한 시점을 반영하며, 사용자가 SMS를 보낸 시점이나 통신사 또는 SMS 공급자가 수신한 시점과 반드시 일치하지는 않습니다. 분석에서 옵트아웃을 Braze가 인바운드 옵트아웃 경로를 처리한 시점으로 간주하는 경우, 이 타임스탬프가 해당 정의와 일치합니다.
{% endalert %}

고객 프로필에는 현재 구독 상태가 표시되지만, 옵트아웃 처리 시 [커스텀 속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes) 또는 유사한 방법을 설정하지 않는 한 단일 "SMS 탈퇴 시점" 필드가 표시되지 않을 수 있습니다.

## SMS 발송 결과에 적용되는 요금 {#charges-applied-to-sms-sending-outcomes}

이 표는 Braze 청구 기준을 반영하며, 공급자의 청구 기준과는 다를 수 있습니다. Braze에서 요금이 부과되지 않는 결과라도 공급자에 의해 요금이 부과될 수 있습니다.

| 결과 | 정의 | Braze 요금 부과 여부 |
|--------|------------|--------|
| 발송됨 | Campaign 또는 캔버스 단계가 시작되거나 트리거되어 SMS 페이로드가 SMS 공급자에게 전송되었습니다. | 요금 없음 |
| 전달 실패 | SMS 페이로드를 SMS 공급자에게 전송할 수 없었습니다. 대기줄 초과, 계정 정지 또는 미디어 오류(MMS의 경우) 등으로 인해 발생할 수 있습니다. | 요금 없음 |
| 전달됨 | SMS 공급자가 상위 통신사로부터(가능한 경우 수신 기기로부터) 메시지 전달 확인을 수신했습니다. | 요금 부과 |
| 거부됨 | SMS 공급자가 메시지가 전달되지 않았음을 나타내는 거부 수신 확인을 받았습니다. 통신사 콘텐츠 필터링 또는 수신 기기의 가용성 등 여러 이유로 발생할 수 있습니다. | 요금 부과 |
| **통신사로 발송** | {% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} 새 대시보드에서는 더 이상 사용되지 않습니다. 일부 대시보드에서는 이 측정기준이 **Sent to Carrier**로 표시될 수 있습니다. | 개별 메시지 발송 결과에 따라 요금이 부과될 수 있음 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMS 발송 결과에 적용되는 요금" }

{% alert note %}
**통신사로 발송**은 새 대시보드에서 더 이상 사용되지 않습니다. 현재 보고서에는 **발송됨**, **전달 확인됨**, **전달 실패**, **거부됨**을 사용하세요. 정의는 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data/report_metrics)을 참조하세요.
{% endalert %}

## RCS 및 SMS 대체 보고서 {#rcs-and-sms-fallback-reporting}

RCS SMS 대체 이벤트 동작(`IS_SMS_FALLBACK=TRUE` 포함)에 대한 자세한 내용은 [SMS 대체가 이벤트 및 세분화와 함께 작동하는 방식]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup#how-sms-fallback-works-with-events-and-segmentation)을 참조하세요.

{% alert note %}
대시보드 Campaign 분석과 Snowflake 내보내기는 타이밍 및 집계 방식에서 약간의 차이가 있을 수 있습니다. 데이터 웨어하우스 조정 시, 측정기준이 대시보드와 정확히 일치하지 않는 경우 Snowflake 또는 Currents 이벤트 스트림을 더 세분화된 소스로 사용하세요.
{% endalert %}

## Snowflake 또는 Currents와 *거부* 조정 {#reconcile-rejections-with-snowflake-or-currents}

대시보드의 *거부* 측정기준은 워크스페이스 전체의 집계 수치입니다. 행 수준의 내보내기가 아니므로, 각 거부를 Snowflake의 단일 행이나 Currents의 단일 `users.messages.sms.Rejection` 이벤트와 항상 일치시킬 수 있는 것은 아닙니다. 예를 들어, Braze가 데이터 웨어하우스 내보내기를 위한 거부 처리를 완료하기 전에 고객 프로필이 삭제된 경우, 해당 거부는 `USERS_MESSAGES_SMS_REJECTION_SHARED` 테이블이나 Currents 페이로드에 나타나지 않지만, 집계 SMS 보고서에는 여전히 해당 결과가 반영될 수 있습니다. 자세한 내용은 [SQL 테이블 참조]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#sms-message-events-and-deleted-user-profiles) 및 Currents 이벤트 용어집의 [SMS 거부 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-rejection-events)를 참조하세요.