---
nav_title: API 사용량
article_title: API 사용량 대시보드
alias: "/api_usage/"
page_order: 5
description: "이 문서에서는 API 사용량 대시보드에 대한 개요를 제공합니다."
---

# API 사용량 대시보드 {#api-usage-dashboard}

> API 사용량 대시보드를 사용하면 Braze로 들어오는 REST API 트래픽을 모니터링하여 REST API 사용 추세를 파악하고 잠재적인 문제를 해결할 수 있습니다.

## API 사용량 대시보드 소개 {#about-the-api-usage-dashboard}

API 사용량 대시보드를 보려면 **설정** > **API 키**로 이동한 다음 **대시보드**를 선택합니다.

기본 대시보드는 지난 하루(24시간) 동안 워크스페이스에 들어온 모든 REST API 요청을 보여줍니다. 사용 사례에 따라 대시보드 컨트롤을 조정하여 트래픽을 필터링하거나 그룹화하고, 대시보드의 시간 범위를 설정할 수 있습니다.

![총 130건의 요청이 있으며, 성공률 70%, 실패율 30%를 보여주는 API 사용량 대시보드.]({% image_buster /assets/img/api_usage_dashboard/api_usage_dashboard.png %})

## 사용 가능한 측정기준 {#available-metrics}

API 사용량 대시보드에는 다음 통계가 포함됩니다:

| 측정기준 | 설명 |
|----------------|-------------|
| 총 요청 수 | 대시보드에 적용된 필터 및 컨트롤 기준으로, 현재 워크스페이스에서 Braze로 전송된 총 요청 수입니다. |
| 성공률 | Braze가 `2XX` 성공 응답을 반환한 총 요청의 비율입니다. |
| 오류율 | Braze가 `4XX` 또는 `5XX` 오류 응답을 반환한 총 요청의 비율입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용 가능한 측정기준" }

## 대시보드 사용하기 {#using-the-dashboard}

![API 키, 엔드포인트, 응답 코드, 데이터 그룹화, 날짜 등 대시보드에 적용할 수 있는 필터.]({% image_buster /assets/img/api_usage_dashboard/filters.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

### 필터 {#filters}

**필터**를 선택하여 워크스페이스의 REST API 트래픽 보기를 좁힐 수 있는 필터를 적용합니다. 사용 가능한 필터는 다음과 같습니다:

- API 키
- 엔드포인트
- 응답 코드

### 데이터 그룹화 {#group-data}

데이터를 다양한 데이터 시리즈로 그룹화하여 사용 패턴을 탐색할 수 있습니다. 그룹화 옵션은 다음과 같습니다:

- 응답 코드(기본값)
- API 엔드포인트
- API 키
- 성공 및 실패만

### 날짜 {#date}

필요에 따라 날짜 필터를 조정하여 더 짧거나 긴 시간 범위를 표시할 수 있습니다. 옵션은 다음과 같습니다:

- 오늘(기본값)
- 커스텀
- 최근 3시간
- 최근 6시간
- 최근 12시간
- 최근 24시간
- 어제
- 최근 7일
- 최근 14일
- 최근 30일
- 이번 달 현재까지

{% alert note %}
**최근 3시간** 및 **최근 6시간** 옵션은 분 단위로 트래픽을 표시합니다. 더 긴 기간은 5분, 시간 또는 일 단위로 트래픽을 표시합니다.
{% endalert %}

## 고려 사항 {#considerations}

API 사용량 대시보드에는 Braze가 수신하여 `2XX`, `4XX` 또는 `5XX` 응답을 반환한 모든 REST API 요청이 포함됩니다. 여기에는 데이터 변환 출력과 클라우드 데이터 수집 동기화가 포함됩니다. SDK 트래픽과 사용자 업데이트 단계는 이 대시보드에 포함되지 않습니다.

대시보드에 표시되는 데이터는 최근 트래픽을 반영하는 데 약간의 지연이 있을 수 있습니다. 사용량이 많은 기간에는 분당 최대 4회까지 대시보드를 새로고침할 수 있습니다. 다시 새로고침하기 전에 몇 분 정도 기다려야 할 수 있습니다.

### 요청 본문의 API 키 {#api-keys-in-request-body}

API 키를 요청 헤더가 아닌 요청 본문에 포함하여 전송하면 일부 요청이 API 사용량 대시보드에 표시되지 않을 수 있습니다. 이로 인해 대시보드의 데이터가 불완전해지고 API 사용량을 정확하게 모니터링하기 어려울 수 있습니다.

API 사용량 대시보드에서 가장 정확한 보고를 위해 API 키를 요청 본문이 아닌 [요청 헤더에 포함]({{site.baseurl}}/api/basics#bearer-token-authentication)하세요.

## 관련 문서 {#related-articles}

- [API 사용량 알림]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts)
- [사용량 제한]({{site.baseurl}}/api/api_limits)
- [Bearer 토큰 인증]({{site.baseurl}}/api/basics#bearer-token-authentication)