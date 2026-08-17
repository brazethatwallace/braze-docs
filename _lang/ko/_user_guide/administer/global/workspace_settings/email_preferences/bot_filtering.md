---
nav_title: 이메일에 대한 봇 필터링
article_title: 이메일용 봇 필터링
page_type: reference
page_order: 1
toc_headers: h2
alias: "/bot_filtering/"
description: "이 문서에서는 이메일용 봇 필터링에 대한 개요를 설명합니다."
---

# 이메일에 대한 봇 필터링 {#bot-filtering-for-emails}

> [이메일 환경설정]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences)에서 봇 필터링을 설정하여 의심되는 모든 컴퓨터 또는 봇 클릭을 제외하세요. 이메일에서 '봇 클릭'이란 자동화된 프로그램에 의해 생성된 이메일 내의 하이퍼링크 클릭을 말합니다. 이러한 봇 클릭을 필터링하여 참여 중인 수신자에게 의도적으로 메시지를 트리거하고 전달할 수 있습니다.

{% alert important %}
2025년 7월 9일부터 새로 생성되는 모든 워크스페이스에는 봇 필터링 설정이 활성화되어 Braze에서 보다 정확한 클릭 보고가 이루어집니다.
{% endalert %}

## 봇 클릭 정보 {#about-bot-clicks}

Braze는 봇 클릭(비인간 상호작용(NHI)이라고도 함)으로 의심되는 클릭을 식별하기 위해 여러 입력을 활용하는 탐지 시스템을 갖추고 있습니다. 봇 클릭은 클릭률을 인위적으로 부풀려 이메일 인게이지먼트 측정기준을 왜곡할 수 있습니다. 이 접근 방식을 통해 진정한 사용자 상호작용과 봇 활동으로 의심되는 행동을 구분하여 클릭 인게이지먼트 측정기준과 인사이트의 무결성을 유지할 수 있습니다.

## 봇 클릭의 영향을 받는 측정기준 {#metrics-affected-by-bot-clicks}

{% alert note %}
봇 필터링은 인게이지먼트 측정기준의 정확성을 높이기 위해 자동화된 것으로 의심되는 클릭을 적극적으로 차단합니다. 그러나 스캐너와 봇은 시간이 지남에 따라 계속 진화하므로, Braze는 모든 비인간 상호작용의 제거를 보장할 수 없습니다.
{% endalert %}

다음 Braze 측정기준은 봇 클릭의 영향을 받을 수 있습니다:

- 총 클릭률
- 고유 클릭률
- 클릭 대비 열람율
- 전환율(전환 이벤트로 "Campaign 클릭"이 선택된 경우)
- 히트맵
- 특정 Segment 필터

봇 필터링이 켜져 있으면 봇으로 의심되는 클릭이 클릭 데이터에서 제외됩니다. 그 결과 다음 [Braze 인텔리전스 기능]({{site.baseurl}}/user_guide/brazeai/intelligence_suite)에서 클릭 관련 수치가 낮게 반영될 수 있습니다:

- 지능형 선택
- 인텔리전트 채널
- Intelligent Timing
- 실험 단계
    - 위닝 경로
    - 개인화된 경로
- Campaign
    - 위닝 배리언트
    - 개인화된 배리언트
- 추정 실제 열람율

봇으로 의심되는 클릭으로 인한 탈퇴는 영향을 받지 않습니다. Braze는 모든 탈퇴 요청을 평소와 같이 계속 처리합니다. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="blocking unsubscribes from suspected bot clicks" %}

## 봇 필터링의 영향을 받는 세분화 필터 {#segmentation-filters-affected-by-bot-filtering}

다음 [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)는 이메일 메시지에 대한 봇 필터링의 영향을 받을 수 있습니다:

- [태그가 있는 Campaign 또는 Canvas 클릭/열람]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-campaign-or-canvas-with-tag)
- [단계 클릭/열람]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-step)
- [Campaign에서 별칭 클릭]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-campaign)
- [캔버스 단계에서 별칭 클릭]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-canvas-step)
- [모든 Campaign 또는 캔버스 단계에서 별칭 클릭]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-any-campaign-or-canvas-step)
- [마지막으로 메시지에 참여]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#last-engaged-with-message)
- [인텔리전트 채널]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#intelligent-channel)

## 봇 필터링 켜기 {#turning-on-bot-filtering}

**설정** > **이메일 환경설정**으로 이동합니다. 그런 다음 **봇 클릭 제거**를 선택합니다. 이 설정은 워크스페이스 수준에서 적용됩니다.

의심되는 봇 클릭은 설정이 켜진 후에만 제거되며, 워크스페이스의 측정기준에 소급 적용되지 않습니다.

![이메일 환경설정에서 봇 필터링 이메일 설정이 켜진 모습.]({% image_buster /assets/img/bot_tracking_email.png %})

{% alert important %}
이 설정을 켠 후 나중에 끄면, Braze는 이전에 제거된 봇 활동을 분석에 복원할 수 없습니다.
{% endalert %}

## Currents 및 Snowflake의 이메일 클릭 이벤트 필드 {#fields-in-email-click-events-for-currents-and-snowflake}

Braze는 이메일 클릭 이벤트에 대해 Currents 및 Snowflake에서 `is_suspected_bot_click` 및 `suspected_bot_click_reason` 필드를 전송합니다.

| 필드 | 데이터 유형 | 설명 |
| `is_suspected_bot_click` | Boolean | 봇 클릭으로 의심되는 경우를 나타냅니다. **봇 클릭 제거** 워크스페이스 설정을 켜기 전까지는 null 값으로 전송됩니다. 이 방식을 통해 워크스페이스에서 의심되는 봇 클릭 필터링이 시작된 시점을 프로그래밍 방식으로 파악할 수 있으므로, Currents 및 Snowflake의 데이터와 정확하게 비교할 수 있습니다. |
| `suspected_bot_click_reason` | Array | 봇 클릭으로 의심되는 이유를 나타냅니다. 봇 필터링 워크스페이스 설정이 비활성화되어 있더라도 `user_agent` 및 `ip_address`와 같은 값이 채워집니다. 이 필드는 의심되는 봇 클릭에서 발생한 클릭 수와 실제 사용자 상호작용을 비교하여, 이 설정을 켰을 때의 잠재적 영향에 대한 인사이트를 제공할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Currents 및 Snowflake의 이메일 클릭 이벤트 필드" }

## 자주 묻는 질문 {#frequently-asked-questions}

### 봇 필터링이 Campaign 성능에 어떤 영향을 미치나요? {#how-will-bot-filtering-impact-my-campaigns-performance}

이 기능은 이미 발송된 이전 Campaign의 측정기준에는 영향을 미치지 않습니다. 워크스페이스에서 봇 필터링을 켜면 Braze가 모든 클릭에서 봇으로 의심되는 클릭을 필터링하기 시작합니다. 클릭률이 감소하는 것을 확인할 수 있지만, 이 클릭률은 사용자가 이메일 메시지에 실제로 참여하는 정도를 더 정확하게 나타냅니다.

### 봇 필터링이 Braze 탈퇴 링크를 클릭하는 봇의 탈퇴 처리를 방지하나요? {#will-bot-filtering-prevent-bots-clicking-on-the-braze-unsubscribe-link-from-unsubscribing}

아니요. 모든 탈퇴 요청은 계속 정상적으로 처리됩니다.

### 머신 열람도 봇 클릭 필터링에 포함되나요? {#are-machine-opens-considered-in-the-bot-click-filtering}

아니요.