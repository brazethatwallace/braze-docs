---
nav_title: Multiplied Media
article_title: Multiplied Media
description: "Multiplied Media를 Braze와 함께 사용하여 이메일, 푸시 알림, 인앱 메시지, Content Cards, WhatsApp을 통해 개인화된 이미지, GIF, 비디오를 전송하는 방법을 알아보세요."
alias: /partners/multiplied_media/
page_type: partner
search_tag: Partner
---

# Multiplied Media

> [Multiplied Media](https://multiplied.media)는 CRM 데이터를 활용하여 각 고객에게 고유한 개인화된 이미지, GIF, 비디오를 제작하는 크리에이티브 및 자동화 스튜디오입니다. Multiplied Media와 Braze 통합을 통해 이메일, 푸시 알림, 인앱 메시지, Content Cards, WhatsApp으로 이러한 미디어를 전송할 수 있습니다.
>
> Multiplied Media는 소프트웨어 도구가 아닌 매니지드 서비스입니다. Multiplied Media 팀이 컨셉, 디자인, 애니메이션, 데이터 연결, 렌더링을 모두 처리합니다. 이 통합을 사용하려면 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) 병합 태그가 포함된 미디어 URL을 Campaign 또는 Canvas에 삽입하세요.

_이 통합은 Multiplied Media에서 유지 관리합니다._

## 이 통합에 대하여 {#about-this-integration}

Multiplied Media 팀은 최초 컨셉부터 출시까지 함께 작업합니다. 브랜드에 맞는 미디어를 디자인하고 애니메이션화하며, 데이터를 연결하고, 렌더링을 자동화합니다. 새로운 소프트웨어를 배울 필요가 없습니다.

이 통합은 Braze 데이터(고객 속성 및 Segments)를 Multiplied Media에 연결합니다. Multiplied Media는 각 고객에 대해 고유한 미디어 에셋을 렌더링하고, 해당 고객의 식별자가 포함된 URL에 호스팅합니다. Braze 메시지에서 Liquid 병합 태그를 사용하여 해당 URL을 참조합니다. 이를 통해 각 고객은 자신만의 이미지, GIF 또는 비디오를 볼 수 있습니다.

이 통합은 두 가지 흐름을 지원합니다:

- **일괄 Campaign:** CSV, S3 또는 API를 통해 데이터를 전송합니다. Multiplied Media가 발송 전에 모든 미디어를 렌더링하고 호스팅합니다.
- **실시간 Canvas 자동화:** Canvas의 [웹훅]({{site.baseurl}}/user_guide/channels/webhooks) 단계가 고객이 해당 단계에 도달할 때 렌더링을 트리거합니다.

## 사용 사례 {#use-cases}

- **개인화된 캠페인:** 제품 출시, "래핑" 및 연말 리뷰 캠페인, 시즌 프로모션, 개인 데이터 시각화.
- **상시 자동화:** 환영 플로우, 온보딩, 마일스톤 축하, 윈백 이메일, 유기한 장바구니, 배송 알림, 재입고 알림, 로열티 업데이트.
- **옴니채널 여정:** 하나의 콘셉트를 모든 채널에 맞게 렌더링합니다. 동일한 고객 데이터를 이메일 히어로 이미지, 푸시 이미지, 인앱 비주얼, WhatsApp 비디오로 활용할 수 있어, 모든 터치포인트에서 하나의 비주얼 아이덴티티를 유지할 수 있습니다.

## 전제 조건 {#prerequisites}

Multiplied Media 아키텍처는 S3 또는 API를 통한 배치 기반 Campaigns와 웹훅을 통한 실시간 Canvas 자동화를 지원합니다. 전송 전에 고유한 미디어 자산을 미리 생성하고 호스팅함으로써, Multiplied Media는 메시지가 트리거되는 순간 Liquid 태그 또는 커스텀 속성을 사용하여 원활한 일대일 시각적 경험을 템플릿에 병합할 수 있도록 준비합니다.

시작하기 전에 다음 사항을 확인하세요.

| 요구 사항 | 설명 |
| --- | --- |
| 활성화된 Multiplied Media 계약 | Multiplied Media는 관리형 서비스입니다. Braze에서 시작하기 전에, Multiplied Media 팀이 캠페인의 범위를 설정하고, 미디어 템플릿을 디자인 및 구축하며, 렌더링을 설정합니다. 시작하려면 [multiplied.media](https://multiplied.media)를 방문하거나 [hello@multiplied.media](mailto:hello@multiplied.media)로 이메일을 보내세요. |
| 데이터 소스 | CSV, S3, API 또는 Braze 웹훅을 통해 고객 데이터를 Multiplied Media에 연결합니다. Multiplied Media 팀이 온보딩 과정에서 이를 함께 설정합니다. |
| 통합 식별자 | 데이터에는 `external_id`와 같이 Braze와 Multiplied Media 간에 공유되는 식별자가 포함되어야 합니다. 이 식별자는 각 고객의 미디어 URL의 일부를 구성하며, Braze 메시지에서 Liquid를 사용하여 참조합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## Braze에서 Multiplied Media 사용하기 {#use-multiplied-media-with-braze}

Multiplied Media는 개인화된 미디어를 디자인, 구축, 렌더링하고 데이터를 연결하는 데 도움을 줍니다. 다음 단계는 Braze에서 수행해야 할 나머지 작업입니다.

### 1단계: 미디어가 준비되었는지 확인하기 {#step-1-confirm-your-media-is-ready}

실행 전에 Multiplied Media 팀이 미디어가 렌더링되었는지(배치 Campaign) 또는 렌더링 엔드포인트가 활성화되었는지(실시간 Canvas 플로우) 확인합니다. 그런 다음 Campaign의 미디어 URL을 제공합니다. 예시:

{% raw %}
```
https://cdn.multiplied.media/yourbrand/campaign-name/{{${user_id}}}.gif
```
{% endraw %}

URL 경로의 식별자는 설정 시 합의한 통합 식별자입니다.

### 2단계: Campaign 또는 Canvas에 URL 삽입하기 {#step-2-insert-the-url-into-your-campaign-or-canvas}

Liquid 병합 태그가 포함된 Multiplied Media URL을 채널에 해당하는 필드에 붙여넣습니다.

- **이메일:** 이메일 템플릿의 이미지 소스.
- **푸시 알림:** 푸시 메시지의 이미지 필드.
- **인앱 메시지 및 Content Cards:** 미디어 필드.
- **WhatsApp:** 미디어 헤더 필드.

실시간 Canvas 자동화의 경우, 메시지 단계 전에 Multiplied Media 웹훅 단계(온보딩 시 함께 설정)와 지연 노드를 추가합니다. 이렇게 하면 각 고객에게 전달되기 전에 미디어가 렌더링됩니다.

### 3단계: 미리보기, 테스트 및 실행하기 {#step-3-preview-test-and-launch}

Braze 미리보기와 테스트 발송을 사용하여 Liquid 태그가 올바르게 해석되는지, 각 테스트 사용자가 자신의 미디어를 볼 수 있는지 확인합니다. Multiplied Media 팀은 실행 전에 테스트 발송을 함께 검토합니다.

## 고려 사항 {#considerations}

- 각 고객의 미디어 에셋은 고유합니다. 고객이 연결된 데이터 소스에 없는 경우, URL은 미디어의 기본값(대체) 버전을 제공합니다. Multiplied Media는 모든 인게이지먼트의 일부로 대체 버전을 디자인합니다.
- Multiplied Media는 전달 전에 에셋을 렌더링하고 호스팅하며, 열람 시점에 렌더링하지 않습니다. 미디어는 열람 즉시 로드되며 렌더링 시점의 고객 데이터를 표시합니다. 발송 시점에 데이터가 최신이어야 하는 경우(예: 트리거된 Canvas 플로우), 실시간 웹훅 단계를 사용하세요.
- 예약된 배치 Campaigns의 경우, 모든 에셋을 렌더링할 수 있도록 발송 시간 전에 데이터가 Multiplied Media에 도달해야 합니다. Multiplied Media 팀은 설정 과정에서 마감 시간을 합의합니다.

## 문제 해결 {#troubleshooting}

Multiplied Media는 매니지드 서비스이므로, Multiplied Media 팀이 첫 번째 지원 창구입니다. [hello@multiplied.media](mailto:hello@multiplied.media)로 문의하세요.

동적 이미지가 표시되지 않는 경우 다음 표를 참조하세요.

| 문제 | 해결 방법 |
| --- | --- |
| 동적 이미지가 표시되지 않음 | URL의 Liquid 태그가 설정 시 합의한 통합 식별자(예: `user_id` 또는 커스텀 속성)와 일치하는지 확인합니다. 연결된 데이터 소스에 고객이 존재하는지 확인합니다. 식별자가 확인되었지만 개인화된 에셋이 없는 경우, 대체 미디어가 표시됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="문제 해결" }