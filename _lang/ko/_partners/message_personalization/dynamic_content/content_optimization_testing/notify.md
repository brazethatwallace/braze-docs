---
nav_title: Notify
article_title: Notify
description: "이 참조 문서에서는 고객 생애주기 전반에 걸쳐 개인화를 제공하는 실시간 옴니채널 개인화 솔루션인 Notify와 Braze 간의 파트너십을 설명합니다."
alias: /partners/notify/
page_type: partner
search_tag: Partner
---

# Notify

> [Notify](https://fr.notify-group.com/)는 고객 관계 관리 툴과 원활하게 통합되어 마케팅 전략을 강화하고 여러 채널에서 참여를 촉진하는 AI 기반 소프트웨어 솔루션입니다.

Braze와 Notify 통합을 통해 마케터는 다양한 플랫폼에서 효과적으로 참여를 유도할 수 있습니다. 기존 마케팅 방식에 의존하는 대신, Braze API로 트리거된 Campaign은 Notify의 기능을 사용하여 이메일, SMS, 푸시 알림 등 여러 채널을 통해 개인화된 메시징을 전달할 수 있습니다.

## 필수 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다.

| 요구 사항 | 설명 |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Braze REST API 키 | `users.export.segment` 및 `campaigns.trigger.send` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| CNAME 구성 | Notify가 메시징에 대한 사용자 참여를 추적하여 모델에 추가 정보를 제공할 수 있도록 이메일에 사용되는 추적 픽셀을 위한 하위 도메인을 생성해야 합니다. 하위 도메인 URL을 생성한 후 Notify와 공유하세요. |
| 데이터베이스 옵트인 내보내기 | 지난 1년(12개월)간의 Campaign 및 구매 데이터를 Notify에 전송합니다. 이 내보내기는 Notify 예측 모델을 학습시키는 데 사용됩니다. <br><br> **필드:** <br><br> **이메일:** 이메일의 SHA256 해시로, 소문자로 변환하고 앞뒤 공백을 제거한 것입니다.<br><br>**Segment:** 활동 수준(활성 또는 비활성)을 정의하는 세그먼트 정보입니다.<br><br>**하위 세그먼트:** 구매 활동 수준 등 기타 관련 활동 정보입니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

### 1단계: Campaign 생성 {#step-1-create-your-campaign}

Braze에서 [API 트리거 Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/)을 생성합니다. 그런 다음 Campaign `api_identifier`를 Notify와 공유합니다.

### 2단계: Braze에서 Segment 생성 {#step-2-create-your-segment-in-braze}

다음으로, [1단계](#step-1-create-your-campaign)에서 생성한 Campaign으로 타겟팅할 사용자 Segment를 생성합니다. 그런 다음 Segment ID를 Notify와 공유합니다.

### 3단계: Segment 가져오기 {#step-3-fetch-your-segment}

그런 다음 Notify가 Campaign에 연결된 Segment의 사용자를 내보냅니다.

### 4단계: Notify가 Campaign을 트리거 {#step-4-notify-triggers-the-campaign}

`/campaigns/trigger/send` 엔드포인트를 사용하여 Notify의 AI가 [1단계](#step-1-create-your-campaign)에서 생성한 Braze Campaign을 트리거하여 사용자가 참여할 가능성이 가장 높은 시간에 전송합니다.