---
nav_title: API 사용 알림
article_title: API 사용 알림
description: "이 문서는 예상치 못한 트래픽을 사전에 탐지할 수 있도록 지원하는 API 사용량 알림에 대한 개요를 제공합니다."
page_order: 0
---

# API 사용 알림 {#api-usage-alerts}

> API 사용 알림은 API 사용 현황에 대한 중요한 가시성을 제공하여 예상치 못한 트래픽을 사전에 탐지할 수 있게 합니다. 이러한 알림을 설정하여 주요 API 요청량을 추적하면 실시간으로 알림을 받고, 문제가 마케팅 캠페인에 영향을 미치기 전에 해결할 수 있습니다.

## API 사용 알림에 관하여 {#about-api-usage-alerts}

API 사용량 알림을 사용하여 다음 범주의 요청량을 모니터링할 수 있습니다:

| API 카테고리 | 세부 정보 |
|--------------|---------|
| REST API 엔드포인트 | Braze 백엔드에 대한 모든 REST API 호출(예: 메시지 전송, Campaign 생성, 사용자 내보내기 등)의 사용 내역을 추적합니다. |
| SDK API 요청 | 클라이언트 앱에서 Braze SDK를 통해 이루어지는 API 요청(예: 인앱 메시지 트리거링 또는 사용자 데이터 동기화)을 추적합니다.<br><br>_*월간 활성 사용자(MAU) – CY 24-25를 구매한 고객에게만 제공됩니다._ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="About API usage alerts" }

## API 사용량 알림 생성 {#creating-an-api-usage-alert}

API 사용량 알림을 생성하려면:

1. **설정** > **API 키** > **API 사용량 알림**으로 이동한 후 새 알림을 생성하세요.
2. 알림 이름을 입력하고 알림을 받고 싶은 REST API 엔드포인트 및 API 키를 선택하세요.
3. 하나 이상의 응답 코드를 선택하고 [알림 임계값](#api-usage-alert-thresholds)을 지정하여 알림 기준을 정의하세요.
4. 완료되면 **Alert enabled**를 토글하세요.
    ![Track users 엔드포인트가 1시간 내에 100% 증가할 때 알림을 전송하는 API 사용량 알림의 예시입니다.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## 알림 임계값 {#api-usage-alert-thresholds}

알림 기준을 정의할 때 다음 임계값을 조정할 수 있습니다:

<table aria-label="Alert thresholds #api-usage-alert-thresholds">
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Alert thresholds #api-usage-alert-thresholds" }

## 알림 설정 {#setting-up-alert-notifications}

이메일 알림, 웹훅 알림 또는 둘 다 설정할 수 있습니다. 웹훅 알림은 Slack 채널과 같은 외부 플랫폼으로 알림을 보내는 사용 사례에 매우 유용합니다. 예시는 알림 환경설정에 대한 Slack 연동에 관한 [설명서](https://www.braze.com/docs/user_guide/administer/global/admin_settings/notification_preferences#slack-incoming-webhook-integration)를 참조하세요.

![알림 기준이 충족되면 선택한 이메일로 알림이 전송됩니다.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### 샘플 페이로드 {#payload}

다음은 API 사용량 알림 웹훅 본문의 샘플 페이로드입니다.

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": {
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition": "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    },
    "timeframe_start": "2025-03-20T15:35:00Z",
    "timeframe_end": "2025-03-20T16:35:00Z",
    "volume": 1500,
    "previous_timeframe_start": "2025-03-20T14:35:00Z",
    "previous_timeframe_end": "2025-03-20T15:35:00Z",
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### 알림 예시 {#example-alerts}

다음은 아래 시나리오에서 알림을 받을 수 있도록 API 사용량 알림 구성을 설정하는 몇 가지 방법입니다.

{% tabs local %}
{% tab API 상태 %}
API의 전반적인 상태를 모니터링하기 위한 알림을 설정할 수 있습니다. 예를 들어, API 오류가 이전 시간 대비 20%와 같이 급격히 증가할 때 알림을 설정할 수 있습니다.

| 엔드포인트 | API 키 | 응답 코드 | 임계값 조건 | 임계값 볼륨 | 범위 |
| --- | --- | --- | --- | --- | --- |
| 모든 엔드포인트 | 모든 API 키 | `4XX` 및 `5XX` | 10% 증가 | 10 | 1시간 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Example alerts" }
{% endtab %}

{% tab 엔드포인트 사용량 제한 %}
워크스페이스가 `/users/track` 엔드포인트의 사용량 제한에 도달했을 때 알림을 받습니다. 이 구성은 다른 Braze 엔드포인트에도 적용할 수 있습니다.

| 엔드포인트 | API 키 | 응답 코드 | 임계값 조건 | 임계값 볼륨 | 범위 |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | 모든 API 키 | `429` | 이상 | 100 | 1시간 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Example alerts" }
{% endtab %}

{% tab API 트리거 Campaigns %}
이 알림 구성은 API 트리거 Campaigns 및 Canvases에서 오류가 발생할 때 알림을 보내며, 이 중 일부는 높은 우선순위일 수 있습니다.

| 엔드포인트 | API 키 | 응답 코드 | 임계값 조건 | 임계값 볼륨 | 범위 |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | 모든 API 키 | `4XX` 및 `5XX` | 이상 | 1 | 1시간 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Example alerts" }
{% endtab %}

{% tab 파트너 통합 %}
파트너 통합이 Braze로 데이터 전송을 중단했을 때 알림을 받으려면 다음 알림 구성을 사용하세요.

| 엔드포인트 | API 키 | 응답 코드 | 임계값 조건 | 임계값 볼륨 | 범위 |
| --- | --- | --- | --- | --- | --- |
| 모든 엔드포인트 | 파트너 통합에 사용되는 API 키 | 모든 응답 코드 | 이하 | 0 | 1일 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Example alerts" }
{% endtab %}
{% endtabs %}

## 고려 사항 {#considerations}

- 각 활성 알림은 8시간마다 한 번만 이메일 또는 웹훅 알림을 전송합니다. 이는 단일 알림에서 너무 많은 알림이 발생하는 것을 방지하기 위함입니다. 알림이 너무 일찍 발송되는 경우, 사용 사례에 더 적합하도록 알림 기준을 편집하는 것을 고려하세요.
- 워크스페이스당 최대 10개의 알림을 설정할 수 있습니다.