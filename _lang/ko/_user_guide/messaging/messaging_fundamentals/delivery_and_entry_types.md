---
nav_title: 전달 및 진입 유형
article_title: 전달 및 진입 유형
page_order: 5
page_type: reference
description: "이 참조 문서에서는 Campaign의 전달 유형, Canvas의 진입 유형, 그리고 Campaign 또는 Canvas를 설정할 때 사용하는 시간 기반 기능에 대해 설명합니다."
tool:
    - Campaigns
    - Canvas
---

# 전달 및 진입 유형 {#delivery-and-entry-types}

> Braze에서는 메시지를 스케줄하는 세 가지 방법이 있습니다: 스케줄, 실행 기반, API 트리거. 메시지가 전달되는 방법과 시기를 선택하는 것은 효과적인 메시지를 개발하는 데 매우 중요합니다.

Campaign의 경우, 전달 유형에 따라 사용자가 Campaign에 진입하는 시점과 메시지가 발송되는 시점이 결정됩니다. Canvas는 지속적인 사용자 여정으로 구성되므로, 스케줄링이라는 메시징 개념은 진입 유형이라고 합니다.

| 전달<nobr> 및 진입 유형 | 설명                                                                                                                                                                                                                                                                                                                                      |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **스케줄**       | 이 스케줄 유형은 현재 이벤트에 대한 Campaign처럼 즉시 발송하려는 일회성 메시지를 위해 설계되었습니다. <br><br>본인이나 팀만을 대상으로 테스트 메시지를 발송할 때, 이 옵션을 사용하면 즉시 전달할 수 있습니다.                                                                                   |
| **실행 기반**    | 실행 기반 전달 메시지, 즉 이벤트 트리거 Campaign 및 Canvases는 트랜잭션 또는 성과 기반 메시지에 매우 효과적입니다. 특정 날짜에 메시지를 발송하는 대신, 사용자가 특정 이벤트를 완료한 후 발송하도록 트리거할 수 있습니다.                                                                                           |
| **API 트리거**   | API 트리거 메시지를 사용하면 Braze 대시보드에서 메시지 문구, 다변량 테스트, 재자격 규칙을 관리하면서 자체 서버 및 시스템에서 해당 콘텐츠의 전달을 트리거할 수 있습니다. <br><br>메시지를 트리거하는 API 요청에는 실시간으로 메시지에 템플릿화할 추가 데이터를 포함할 수도 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Delivery and entry types" }

## 시간 기반 옵션 {#time-based-options}

{% tabs %}
{% tab campaign %}
스케줄 전달을 사용할 때 다음 옵션 중에서 선택할 수 있습니다:

- Campaign이 시작되는 즉시 발송
- 지정된 시간에 발송
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/)
{% endtab %}

{% tab canvas %}
스케줄 전달을 사용하면, Campaign을 스케줄하는 것과 유사하게 사용자가 시간 스케줄에 따라 진입합니다. Canvas가 시작되는 즉시 또는 지정된 시간에 사용자를 Canvas에 등록할 수 있습니다.

### 지정된 시간 {#designated-times}

Canvas를 특정 진입 빈도로 발송하도록 선택할 수 있으며, 한 번만, 매일, 매주 또는 매월 등의 옵션이 있습니다. 반복 스케줄 전달이 설정된 Canvases의 경우, 사용자가 최대 30회의 지정된 시간에 Canvas에 진입할 수 있도록 반복을 설정할 수 있습니다.
{% endtab %}
{% endtabs %}

## 실행 기반 옵션 {#action-based-options}

{% tabs %}
{% tab campaign %}
실행 기반 전달은 특정 동작을 수행하는 사용자에게 Campaign을 발송합니다. 이 동작이 발생한 후, Campaign을 발송할 시점을 결정할 수 있습니다: 즉시, 특정 시간 후, 특정 시간에, 또는 미래의 특정 시점에 발송할 수 있습니다.
{% endtab %}

{% tab canvas %}
실행 기반 옵션은 사용자가 Canvas에 진입하기 위해 수행해야 하는 동작(또는 트리거)과 진입이 허용되는 특정 시간을 결정합니다. 예를 들어, 다음과 같은 동작으로 사용자를 평가할 수 있습니다:

- 앱 열기
- 이메일 주소 추가
- 위치 진입

### 진입 기간 {#entry-window}

Canvas의 진입 기간은 지정된 시작 시간(및 선택적 종료 시간)에 어떤 사용자가 Canvas에 진입할 수 있는지를 결정합니다. 실행 기반 Campaign과 마찬가지로, 사용자의 현지 시간대에 맞춰 진입시킬 수 있습니다.
{% endtab %}
{% endtabs %}

## API 트리거 옵션 {#api-trigger-options}

{% tabs %}
{% tab campaign %}
전달 옵션으로 API 트리거를 선택하면, [`/campaigns/trigger/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#prerequisites)에서 발송할 Campaign을 식별하기 위한 Campaign ID를 받게 됩니다.
{% endtab %}

{% tab canvas %}
진입 유형으로 API 트리거를 선택하면, [`/canvas/trigger/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)에서 발송할 Canvas를 식별하기 위한 Canvas ID를 받게 됩니다.
{% endtab %}
{% endtabs %}