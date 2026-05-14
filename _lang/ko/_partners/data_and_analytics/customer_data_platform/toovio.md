---
nav_title: Toovio
article_title: Toovio
description: "이 참조 문서에서는 Braze와 Toovio의 파트너십에 대해 설명합니다. Toovio는 데이터 서비스(data-as-a-service) 회사로, 실행 가능한 데이터를 발견하고 사전 정의된 목표에 기반하여 점진적인 결과를 이끌어내는 데 가장 중요한 요소를 활용할 수 있도록 도와줍니다."
alias: /partners/toovio/
page_type: partner
search_tag: Partner

---

# Toovio

> [Toovio](https://toovio.com/)는 인공지능 기반의 데이터 서비스(data-as-a-service) 회사로, 실행 가능한 데이터를 발견하고 사전 정의된 목표에 기반하여 점진적인 결과를 이끌어내는 데 가장 중요한 요소를 활용할 수 있도록 도와줍니다.

_이 통합은 Toovio에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Toovio의 파트너십은 거의 실시간에 가까운 메시지 트리거링, 점진적인 성과를 이끌어내는 도구, 그리고 Toovio의 고급 캠페인 측정 도구에 대한 액세스를 제공합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Toovio 계정 | 이 파트너십을 활용하려면 Toovio 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze 커런츠 | Braze 커런츠를 사용하면 Braze 클라이언트가 이벤트 또는 동작 데이터를 Braze 데이터 파트너(AWS S3, Google Cloud Storage 또는 Microsoft Azure Blob Storage)로 스트리밍하여 Braze 플랫폼 외부에서 처리할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

다음 통합을 통해 Toovio는 특정 고객을 타겟팅하는 트리거를 생성하고 거의 실시간으로 커뮤니케이션할 수 있습니다. Toovio가 결정한 트리거는 Braze [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 통해 Braze로 전송됩니다.

### 1단계: 데이터 파트너 정의 {#step-1-define-data-partner}

Currents 피드의 드롭 위치를 Toovio와 공유해야 합니다. 이를 통해 Toovio가 사용자 이벤트 및 동작 데이터에 액세스하고 처리할 수 있습니다.

### 2단계: 트리거 캠페인 설정 {#step-2-set-up-a-triggered-campaign}

Toovio가 타겟팅할 고객 이벤트를 기반으로 Braze [API 트리거 캠페인]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)을 생성합니다. 또한 캠페인을 트리거할 타겟 사용자 속성과 값을 정의해야 합니다.

### 3단계: Toovio 계정 설정 {#step-3-set-up-your-toovio-account}

[info@toovio.com](mailto:info@toovio.com?subject=New%20Customer%20Request)으로 제목을 "New Customer Request"로 하여 Toovio에 연락하면 계정을 설정할 수 있습니다. Toovio는 클라이언트와 협력하여 트리거와 기반 모델을 설정합니다.