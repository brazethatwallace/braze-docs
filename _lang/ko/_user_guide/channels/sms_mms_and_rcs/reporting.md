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

## SMS 옵트인 및 옵트아웃 추적 {#track-sms-opt-ins-and-opt-outs}

다음 방법을 사용하여 SMS 옵트인 및 옵트아웃을 추적할 수 있습니다.

| 방법 | 설명 |
|--------|-------------|
| 세그먼터 | 세그먼터는 특정 [구독 그룹]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#subscription-group)에 속한 사용자 수를 표시합니다. 전화번호 기준으로 중복을 제거하지 않으므로, 여러 사용자가 동일한 전화번호를 공유하는 경우 각 인스턴스가 별도로 집계됩니다. |
| 구독 그룹 시계열 | 이메일 및 전화번호에 대한 구독의 일별 스냅샷을 제공합니다. 시계열은 구독, 구독 취소, 재구독을 집계합니다. 예를 들어, 사용자가 구독한 후 구독을 취소하고 다시 구독하면 구독 사용자 1명으로 집계됩니다. |
| Currents | Currents를 사용하여 자체 보고서를 위한 [구독 및 참여 이벤트]({{site.baseurl}}/message_events_glossary/)를 내보낼 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
**SMS/MMS/RCS 성과** 패널의 _옵트인_ 및 _옵트아웃_ 통계는 인바운드 키워드를 통해 옵트인 또는 옵트아웃한 사용자를 반영합니다(예: 옵트인의 경우 "START", 옵트아웃의 경우 "STOP" 문자 발송). 이 수치는 일반적으로 세그먼터에 표시되는 수치보다 낮습니다. 이는 SMS에 가입한 총 사용자 수가 아니라 해당 키워드가 문자로 발송된 횟수를 집계하기 때문입니다.
{% endalert %}

### SMS 캠페인 옵트아웃 추적 {#track-sms-campaign-opt-outs}

구독 그룹 상태 변경 테이블 대신 인바운드 수신 테이블을 사용하여 캠페인 수준에서 SMS 옵트아웃을 추적할 수 있습니다. 예를 들어, [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/query_builder/) 또는 데이터 웨어하우스에서 `USERS_MESSAGES_SMS_INBOUNDRECEIVE` 또는 [`USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED`]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables/#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) 테이블을 참조하는 쿼리를 실행할 수 있습니다.

이 예시 쿼리는 `USERS_MESSAGES_SMS_INBOUNDRECEIVE` 테이블을 참조합니다:

```sql
SELECT *
FROM USERS_MESSAGES_SMS_INBOUNDRECEIVE
WHERE app_group_id = 'app-group-id'
AND subscription_group_api_id = 'subscription_group_api_id'
AND action = 'Unsubscribed'
AND (campaign_id IS NOT NULL OR canvas_id IS NOT NULL);
```

이 쿼리는 지정된 워크스페이스 및 구독 그룹에서 SMS 커뮤니케이션을 옵트아웃한 사용자를 반환하며, Campaign 또는 Canvases와 연결된 사용자로 필터링됩니다.

## SMS 발송 결과에 적용되는 요금 {#charges-applied-to-sms-sending-outcomes}

이 표는 Braze 청구를 반영하며, 제공업체의 청구와는 다릅니다. Braze에서 요금이 부과되지 않는 결과도 제공업체에서는 요금이 부과될 수 있습니다.

| 결과 | 정의 | Braze 요금 부과 |
|--------|------------|--------|
| 발송됨 | Campaign 또는 캔버스 단계가 시작되거나 트리거되어 SMS 페이로드가 SMS 제공업체로 전송되었습니다. | 요금 없음 |
| 전달 실패 | SMS 페이로드를 SMS 제공업체로 전송할 수 없었습니다. 대기줄 초과, 계정 정지 또는 미디어 오류(MMS의 경우) 등으로 인해 발생할 수 있습니다. | 요금 없음 |
| 전달됨 | SMS 제공업체가 업스트림 통신사로부터(가능한 경우 대상 기기로부터) 메시지 전달 확인을 수신했습니다. | 요금 부과 |
| 거부됨 | SMS 제공업체가 메시지가 전달되지 않았음을 나타내는 거부 수신 확인을 받았습니다. 통신사 콘텐츠 필터링 또는 대상 기기의 가용성 등 여러 이유로 발생할 수 있습니다. | 요금 부과 |
| 통신사로 발송됨 | {% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} | 개별 메시지 발송 결과에 따라 요금이 부과될 수 있음 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }