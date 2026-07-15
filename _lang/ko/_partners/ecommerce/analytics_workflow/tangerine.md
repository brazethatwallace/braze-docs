---
nav_title: Tangerine
article_title: Tangerine
description: "이 문서에서는 오프라인 매장과 온라인 매장을 연결하여 소비자와 매장 직원에게 우수한 매장 내 경험을 제공하는 옴니채널 플랫폼인 Tangerine Store360과 Braze 간의 파트너십을 설명합니다. 이 통합을 통해 Braze의 원시 캠페인 및 노출 횟수 데이터를 Snowflake Secure Data Sharing을 통해 Store360에서 사용할 수 있으며, 브랜드는 캠페인이 매장 내 참여 및 매장 방문에 미치는 영향을 측정할 수 있습니다."
alias: /partners/tangerine/
page_type: partner
search_tag: Partner

---

# Tangerine Store360

> Tangerine은 Store360이라는 옴니채널 플랫폼을 설계, 구축 및 운영합니다. Store360은 오프라인 매장과 온라인 매장을 연결하여 소비자와 매장 직원의 매장 내 경험을 개선하는 옴니채널 지원 플랫폼입니다. Store360은 리테일러의 모바일 앱 사용자와 매장 내 참여를 포함하여 오프라인 매장 방문 트래픽을 추적하고 분석합니다.

Braze와 Tangerine 통합을 사용하면 Snowflake Secure Data Sharing을 통해 Braze의 원시 캠페인 및 노출 횟수 데이터를 Store360에 통합할 수 있습니다. 이제 브랜드는 이러한 캠페인이 오프라인 매장 방문 및 매장 내 참여에 미치는 영향을 측정할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Store360 계정 | 이 파트너십을 활용하려면 Store360 계정이 필요합니다. |
| Braze 계정 ID | Braze 앱 그룹 ID입니다. |
| 일치하는 사용자 ID | Store360과 Braze의 고객 데이터에는 두 플랫폼 간에 일치하는 사용자 ID가 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 활용 사례 {#use-cases}

### 오프라인 매장 방문에 대한 캠페인 영향 분석 {#analyze-campaign-impact-on-physical-store-visit}

브랜드는 Braze를 사용하여 소비자에게 캠페인 메시지를 보내 매장 방문을 늘립니다. 캠페인 기간 동안 Store360은 사용자 ID로 식별된 모바일 앱 사용자 방문을 캡처합니다.

Store360 Insight 분석 기능을 사용하면 브랜드는 발송 및 읽은 메시지(Braze 데이터)부터 오프라인 매장을 방문한 수신자의 수와 대상(Store360 데이터)까지 캠페인 영향 세부 정보를 시각화할 수 있습니다.

## 통합 {#integration}

### 1단계: Snowflake Secure Data Share 활성화 {#step-1-enable-snowflake-secure-data-share}

Braze 팀과 협력하여 Snowflake Secure Data Share를 활성화하고 구성합니다.

### 2단계: Braze 데이터를 가져오도록 Store360 구성 {#step-2-configure-store360-to-get-braze-data}

Store360 관리자 매니저 웹 콘솔을 사용하여 Braze 앱 그룹 ID를 Store360 서비스 계정에 구성합니다. 이렇게 하면 Tangerine 관리 팀에 Snowflake Data Sharing을 사용하여 Braze 데이터를 Store360에 동기화하도록 요청됩니다.

### 3단계: 모바일 앱에 Store360 SDK 통합 {#step-3-integrate-store360-sdks-to-mobile-app}

Braze 캠페인 및 노출 횟수 데이터와 함께 모바일 앱 사용자의 매장 방문 및 매장 내 활동을 추적하고 분석하려면 Store360 SDK 설치 설명서에 제공된 단계를 사용하여 모바일 앱에 Store360 SDK를 통합해야 합니다. 이 설명서는 Tangerine Store 360과의 클라이언트 계약 체결 후 제공됩니다.

## Store360에서 Braze 데이터 분석 {#analyze-braze-data-in-store360}

Snowflake Secure Data Sharing을 활용하여 Braze의 원시 캠페인 및 노출 횟수 데이터를 Store360 Insight 분석과 공유하면 온라인에서 오프라인까지 사용자의 전체 라이프사이클과 활동을 파악할 수 있습니다.

참고로, Store360 분석에 통합할 수 있는 모든 [Braze 필드](/docs/assets/download_file/data-sharing-raw-table-schemas.txt)는 여기에서 확인할 수 있습니다. 이 단계의 세부 사항은 고객별로 매우 다르며 특별한 구성이 필요합니다. 자세한 내용은 Store360 계정 매니저 또는 support@tangerine.io에 문의하세요.

## 중요 정보 및 제한 사항 {#important-information-and-limitations}

### 서비스 가용성 {#service-availability}

현재 Store360 서비스는 일본과 인도네시아에서 상업적으로 이용 가능합니다.

Tangerine은 2023년에 다음 국가에서 Store360 제품 출시를 계획하고 있습니다.
- 미국
- 태국
- 싱가포르
- 베트남
- 한국

### 데이터 보존 {#data-retention}

Snowflake 데이터 공유를 위한 Braze 데이터에는 2년 보존 정책이 적용됩니다.

### Braze 이벤트 데이터 채우기 시 시간 지연 {#time-lag-in-populating-braze-event-data}

Braze 이벤트는 스트리밍 기술로 처리되며 거의 실시간으로 사용할 수 있습니다. 일반적으로 이벤트는 발생 후 30분 이내에 사용할 수 있습니다.