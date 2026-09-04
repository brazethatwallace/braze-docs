---
nav_title: API 사용 알림
article_title: API 사용 알림
description: "이 문서는 예상치 못한 트래픽을 사전에 탐지할 수 있도록 지원하는 API 사용량 알림에 대한 개요를 제공합니다."
page_order: 0
---

# API 사용 알림 {#api-usage-alerts}

> API 사용 알림은 API 사용 현황에 대한 중요한 가시성을 제공하여 예상치 못한 트래픽을 사전에 탐지할 수 있게 합니다. 이러한 알림을 설정하여 주요 API 요청량을 추적하면 실시간으로 알림을 받고, 문제가 마케팅 캠페인에 영향을 미치기 전에 해결할 수 있습니다.

## API 사용량 알림 정보 {#about-api-usage-alerts}

API 사용량 알림을 사용하면 다음 카테고리에 대한 요청 볼륨을 모니터링할 수 있습니다.

| API 카테고리 | 세부 정보 |
|--------------|---------|
| REST API 엔드포인트 | 메시지 전송, Campaigns 생성, 사용자 내보내기 등 Braze 백엔드에 대한 모든 REST API 호출 사용량을 추적합니다. |
| SDK API 요청 | 인앱 메시지 트리거 또는 사용자 데이터 동기화 등 클라이언트 앱에서 Braze SDK를 통해 이루어진 API 요청을 추적합니다.<br><br>_*월간 활성 사용자(MAU) – CY 24-25를 구매한 고객에게만 제공됩니다._ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="API 사용량 알림 정보" }

## API 사용량 알림 만들기 {#creating-an-api-usage-alert}

API 사용량 알림을 만들려면:

1. **설정** > **API 및 식별자** > **API 사용량 알림**으로 이동한 다음, 새 알림을 만듭니다.
2. 알림 이름을 입력하고 알림을 받을 REST API 엔드포인트와 API 키를 선택합니다.
3. 하나 이상의 응답 코드를 선택하고 [알림 임계값](#api-usage-alert-thresholds)을 지정하여 알림 기준을 정의합니다.
4. 설정을 마쳤으면 **알림 활성화**를 토글합니다.
    ![1시간 이내에 Track users 엔드포인트가 100% 증가할 때 알림을 보내는 API 사용량 알림 예시]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## 알림 임계값 {#api-usage-alert-thresholds}

알림 기준을 정의할 때 다음 임계값을 조정할 수 있습니다:

<table aria-label="알림 임계값">
  <caption>알림 임계값</caption>
  <thead>
    <tr>
      <th>필드</th>
      <th>설명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>임계값 조건</td>
      <td>
        알림을 받고자 하는 임계값에 도달하기까지의 조건을 정의합니다. 다음이 지원됩니다:<br><br>
        <ul>
          <li><strong>Increased by</strong> 또는 <strong>Decreased by</strong>: 요청을 이전 시간 창과 비교합니다.</li>
          <li><strong>Increased by percentage</strong> 또는 <strong>Decreased by percentage</strong>: 이전 시간 창 대비 요청의 백분율 변화를 비교합니다.</li>
          <li><strong>Greater than or equal</strong> 또는 <strong>less than or equal</strong>: 시간 창 내의 요청 수를 계산합니다.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>임계값 볼륨</td>
      <td>임계값 조건과 함께 사용됩니다.</td>
    </tr>
    <tr>
      <td>범위</td>
      <td>알림 평가를 위한 시간 창입니다.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 aria-label="알림 임계값" }

## 알림 경고 설정하기 {#setting-up-alert-notifications}

이메일 알림, 웹훅 알림 또는 둘 다 설정할 수 있습니다. 웹훅 알림은 Slack 채널과 같은 외부 플랫폼으로 알림을 보내는 것과 같은 사용 사례에 매우 유용합니다. 예시는 알림 기본 설정에 대해 Slack과 알림을 통합하는 방법에 대한 [설명서]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences)를 참조하세요.

![알림 조건이 충족되면 선택한 이메일로 이메일이 전송됩니다.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### 샘플 페이로드 {#payload}

다음은 API 사용량 알림 웹훅의 본문에 대한 샘플 페이로드입니다.

```json
{
  "text": "Your My First API Usage Alert alert has triggered. Please note that this alert is reset every 8 hours, and only one notification will be sent per reset period. You can view your alert and usage here: <link>.",
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "app_group_name": "My Workspace",
    "alert_criteria": {
      "response_codes": "201, 202 and 203",
      "threshold_condition": "increase by",
      "threshold_volume": "50%",
      "within": "1 hour"
    },
    "timeframe_start": "2025-03-20 15:35:00",
    "timeframe_end": "2025-03-20 16:35:00",
    "volume": 1500,
    "previous_timeframe_start": "2025-03-20 14:35:00",
    "previous_timeframe_end": "2025-03-20 15:35:00",
    "previous_volume": 1000
  }
}
```

{% alert note %}
`previous_timeframe_start`, `previous_timeframe_end`, `previous_volume` 필드는 선택 사항이며, 알림이 비교 임계값 조건(`increase by`, `decrease by`)을 사용하는 경우에만 나타납니다. `greater than or equal` 또는 `less than or equal` 알림에서는 이 필드가 생략됩니다.
{% endalert %}

#### 페이로드 필드 세부 사항 {#payload-field-details}

| 필드 | 유형 | 설명 |
|-------|------|-------------|
| `text` | 문자열 | 사람이 읽을 수 있는 알림 메시지입니다. |
| `data.alert_name` | 문자열 | 알림의 이름입니다. |
| `data.alert_type` | 문자열 | 알림 유형입니다(항상 `"API Usage Alert"`). |
| `data.app_group_name` | 문자열 | 워크스페이스 이름입니다. |
| `data.alert_criteria.response_codes` | 문자열 | 알림에 대해 선택된 응답 코드입니다. 선택하지 않은 경우 `"all response codes"`를, 단일 코드의 경우 `"201"`을, 여러 코드의 경우 `"201, 202 and 203"`을 반환합니다. |
| `data.alert_criteria.threshold_condition` | 문자열 | 조건 유형: `"increase by"`, `"decrease by"`, `"greater than or equal"` 또는 `"less than or equal"`. |
| `data.alert_criteria.threshold_volume` | 문자열 또는 숫자 | 임계값입니다. 조건이 백분율을 사용하는 경우 `%`로 끝나는 문자열입니다(예: `"50%"`). 조건이 숫자 값을 사용하는 경우 숫자입니다(예: `50`). |
| `data.alert_criteria.within` | 문자열 | 알림 평가 시간 범위입니다(예: `"1 day"`). |
| `data.timeframe_start` | 문자열 | UTC 형식 `YYYY-MM-DD HH:MM:SS`로 된 알림 기간의 시작 시점입니다. |
| `data.timeframe_end` | 문자열 | UTC 형식 `YYYY-MM-DD HH:MM:SS`로 된 알림 기간의 종료 시점입니다. |
| `data.volume` | 숫자 | 알림 기간 동안의 요청량입니다. |
| `data.previous_timeframe_start` | 문자열 | (선택 사항) 이전 기간의 시작 시점입니다. 비교 임계값 조건에서만 나타납니다. |
| `data.previous_timeframe_end` | 문자열 | (선택 사항) 이전 기간의 종료 시점입니다. 비교 임계값 조건에서만 나타납니다. |
| `data.previous_volume` | 숫자 | (선택 사항) 이전 기간 동안의 요청량입니다. 비교 임계값 조건에서만 나타납니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="페이로드 필드 세부 사항" }

### 알림 예시 {#example-alerts}

다음 시나리오에서 알림을 받을 수 있도록 API 사용량 알림 구성을 설정하는 몇 가지 방법을 소개합니다.

{% tabs local %}
{% tab API 상태 %}
API의 전반적인 상태를 모니터링하기 위한 알림을 설정할 수 있습니다. 예를 들어, 이전 시간 대비 API 오류가 20%와 같이 급격하게 증가할 때 알림을 설정할 수 있습니다.

| 엔드포인트 | API 키 | 응답 코드 | 임계값 조건 | 임계값 | 기간 |
| --- | --- | --- | --- | --- | --- |
| 모든 엔드포인트 | 모든 API 키 | `4XX` 및 `5XX` | 10% 증가 | 10 | 1시간 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="알림 예시" }
{% endtab %}

{% tab 엔드포인트 사용량 제한 %}
워크스페이스가 `/users/track` 엔드포인트의 사용량 제한에 도달하면 알림을 받을 수 있습니다. 이 구성을 다른 Braze 엔드포인트에도 적용할 수 있습니다.

| 엔드포인트 | API 키 | 응답 코드 | 임계값 조건 | 임계값 | 기간 |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | 모든 API 키 | `429` | 이상 | 100 | 1시간 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="알림 예시" }
{% endtab %}

{% tab API 트리거 Campaigns %}
이 알림 구성은 API 트리거 Campaigns 및 Canvases에서 오류가 발생할 때 알림을 보내며, 이 중 일부는 우선순위가 높을 수 있습니다.

| 엔드포인트 | API 키 | 응답 코드 | 임계값 조건 | 임계값 | 기간 |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | 모든 API 키 | `4XX` 및 `5XX` | 이상 | 1 | 1시간 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="알림 예시" }
{% endtab %}

{% tab 파트너 통합 %}
파트너 통합이 Braze로 데이터 전송을 중단할 때 알림을 받으려면 다음 알림 구성을 사용하세요.

| 엔드포인트 | API 키 | 응답 코드 | 임계값 조건 | 임계값 | 기간 |
| --- | --- | --- | --- | --- | --- |
| 모든 엔드포인트 | 파트너 통합에 사용되는 API 키 | 모든 응답 코드 | 이하 | 0 | 1일 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="알림 예시" }
{% endtab %}
{% endtabs %}

## 고려 사항 {#considerations}

- 각 활성 알림은 8시간마다 이메일 또는 웹훅 알림을 한 번만 전송합니다. 이는 단일 알림에서 너무 많은 알림이 발생하는 것을 방지하기 위한 것입니다. 알림이 너무 일찍 전송되는 경우, 사용 사례에 더 적합하도록 알림 기준을 편집하는 것을 고려해 보세요.
- 워크스페이스당 최대 10개의 알림을 설정할 수 있습니다.