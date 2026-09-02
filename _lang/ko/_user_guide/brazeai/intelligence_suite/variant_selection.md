---
nav_title: BrazeAI<sup>TM</sup>로 최적화
article_title: BrazeAI<sup>TM</sup>로 A/B 테스트 최적화
page_order: 1.6
description: "BrazeAI<sup>TM</sup>로 최적화 기능이 단일 발송 및 다중 발송 Campaign에서 가장 성과가 좋은 배리언트를 자동으로 선택하고 배분하는 방법을 알아보세요."
search_rank: 10
toc_headers: h2
---

# BrazeAI<sup>TM</sup>로 A/B 테스트 최적화 {#optimizing-ab-tests-with-brazeai}

> **BrazeAI<sup>TM</sup>로 최적화**를 켜면 여러 배리언트가 포함된 Campaign을 자동으로 최적화할 수 있습니다. 최적화 방법은 Campaign이 한 번 발송되는지 또는 여러 번 발송되는지에 따라 달라집니다.

## 전제 조건 {#prerequisites}

**BrazeAI<sup>TM</sup>로 최적화**를 사용하려면 Campaign에 최소 두 개의 메시지 배리언트가 포함되어야 합니다.

다중 발송 Campaign의 경우 다음 조건도 충족해야 합니다:

- 최소 하나의 전환 이벤트를 정의합니다.
- 재자격 기간을 24시간 이상으로 설정합니다.

## 최적화 켜기 {#turn-on-optimization}

**타겟 오디언스** 단계에서 **A/B 테스트**으로 이동한 다음, **Optimize with BrazeAI<sup>TM</sup>**를 켜세요.

## 단일 발송 Campaign {#single-send-campaigns}

단일 발송 Campaign의 경우, Braze는 오디언스의 초기 일부를 각 배리언트에 발송합니다. 실험 기간이 종료되면 BrazeAI<sup>TM</sup>가 가장 성능이 좋은 배리언트를 선택하여 나머지 오디언스에게 발송합니다.

최적화를 켜면 Braze가 권장 설정을 적용합니다. 이 설정을 변경하려면 **고급 컨트롤**을 여세요:

- **최적화 목표:** BrazeAI<sup>TM</sup>가 배리언트를 비교하는 데 사용하는 측정기준을 선택합니다. 사용 가능한 목표는 채널에 따라 다릅니다.
- **실험 기간:** 4시간, 24시간, 72시간을 선택하거나 커스텀 기간을 입력합니다.
- **배리언트 분배:** 각 배리언트 또는 대조군에 할당된 비율을 변경합니다.

기본 실험 기간은 4시간입니다. 주요 전환 이벤트에 대해 최적화하는 경우 기본값은 24시간입니다.

### 채널별 기본 최적화 목표 {#default-optimization-goals-by-channel}

| 채널 | 기본 목표 |
|---|---|
| 푸시 알림 | *열람* |
| 이메일 | *고유 클릭* |
| 단문 메시지 서비스, MMS, RCS, WhatsApp | *클릭* |
| 기타 지원 채널 | *주요 전환 이벤트 - A* |
{: .reset-td-br-1 .reset-td-br-2 aria-label="채널별 기본 최적화 목표" }

## 다중 발송 Campaign {#multi-send-campaigns}

반복, 행동 기반, API 트리거 Campaign 등 여러 번 발송하는 Campaign의 경우, BrazeAI<sup>TM</sup>가 오디언스 배분을 지속적으로 최적화합니다. 초기 전환 마감 이후 Braze는 12시간마다 성능을 검토하고 더 높은 성능을 보이는 배리언트에 더 많은 사용자를 보냅니다.

BrazeAI<sup>TM</sup>가 성능 데이터를 수집하는 동안 초기 배분은 균등할 수 있습니다. 최적화가 성능 추세를 파악함에 따라 배분이 변경됩니다.

**고급 제어**를 열어 대조군을 추가하거나 제거할 수 있습니다. 대조군은 Campaign 성능을 측정하기 위한 기준선을 제공하며 메시지를 수신하지 않습니다.

## 리포팅 {#reporting}

단일 발송 실험이 완료되거나, 다중 발송 Campaign이 충분한 데이터를 수집한 후 **Campaign 분석** 페이지에서 최적화를 통해 달성된 상승 효과를 확인할 수 있습니다.

![BrazeAI<sup>TM</sup>로 최적화를 통한 상승 효과를 보여주는 Campaign 분석, 실험 기간 이후의 비교 측정기준 포함.]({% image_buster /assets/img_archive/braze_ai_variant_selection_reporting.png %})

자세한 내용은 [A/B 테스트 분석]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics)을 참조하세요.

## 자주 묻는 질문 {#frequently-asked-questions}

### BrazeAI<sup>TM</sup>로 최적화를 켤 수 없는 이유는 무엇인가요? {#why-cant-i-turn-on-optimize-with-brazeai}

다음과 같은 경우 최적화를 사용할 수 없습니다:

- Campaign에 활성 배리언트가 두 개 미만인 경우.
- 다중 발송 Campaign에 전환 이벤트가 없는 경우.
- 다중 발송 Campaign의 재자격 기간이 24시간 미만인 경우.

### 처음에 배리언트의 발송 수가 비슷한 이유는 무엇인가요? {#why-do-my-variants-have-similar-send-counts-at-first}

BrazeAI<sup>TM</sup>는 성능 데이터를 수집하기 위해 초기 분배로 시작합니다. 시간이 지남에 따라 성능 추세를 파악하면서 분배를 조정합니다.

### 다중 발송 Campaign이 하나의 배리언트를 선택하지 않고도 최적화를 중단할 수 있나요? {#can-a-multi-send-campaign-stop-optimizing-without-selecting-one-variant}

네. BrazeAI<sup>TM</sup>가 실험을 계속해도 전환율이 현재 비율의 1% 이상 개선되지 않을 것이라고 95% 신뢰도를 확보하면 최적화가 중단됩니다.