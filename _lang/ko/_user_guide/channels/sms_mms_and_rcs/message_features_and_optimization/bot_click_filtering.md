---
nav_title: "봇 클릭 필터링"
article_title: "SMS 및 RCS 봇 클릭 필터링"
description: "이 참조 문서에서는 SMS 및 RCS 봇 클릭 필터링에 대해 다룹니다."
alias: /sms_rcs_bot_click_filtering/
page_type: reference
page_order: 5
channel:
  - SMS
  - RCS
---

# SMS 및 RCS 봇 클릭 필터링 {#sms-and-rcs-bot-click-filtering}

> SMS 및 RCS 봇 클릭 필터링은 의심되는 봇 클릭을 제외하여 Campaign 분석 및 워크플로를 향상시킵니다. "봇 클릭"이란 SMS 및 RCS 메시지의 단축 링크에 대한 자동화된 클릭을 의미하며, 웹 크롤러, Android 및 iOS 링크 미리보기, CPaaS 보안 소프트웨어 등이 이에 해당합니다. 이 기능은 실제 사용자와의 참여를 위해 정확한 보고, 세분화 및 오케스트레이션을 지원합니다. <br><br> 이메일 Campaign 봇 클릭 필터링에 대해서는 [이메일 봇 필터링]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/bot_filtering)을 참조하세요.

## 작동 방식 {#how-it-works}

Braze는 여러 입력을 사용하여 비인간 상호작용(NHI)이라고도 하는 의심되는 봇 클릭을 식별하는 독자적인 감지 시스템을 보유하고 있습니다. 봇 클릭은 클릭률을 부풀려 참여 측정기준을 왜곡할 수 있습니다. 이를 필터링함으로써 Braze는 의사 결정을 위한 신뢰할 수 있는 데이터 수집을 지원합니다.

Braze 시스템은 웹 크롤러, Android 및 iOS 링크 미리보기, CPaaS 보안 소프트웨어와 관련된 사용자 에이전트를 분석합니다. 필터링되는 사용자 에이전트의 몇 가지 예로는 `GoogleBot`, `GoogleMessages/20`, `python-requests/2.32.3`, `Barracuda Sentinel (EE)` 등이 있습니다.

## 영향을 받는 측정기준 및 워크플로 {#affected-metrics-and-workflows}

다음 Braze 측정기준 및 워크플로가 봇 클릭의 영향을 받습니다:

- **_총 클릭 수_:** Campaign 분석 및 Canvas 분석에서 봇 클릭이 제외되어 실제 사용자 상호작용만 반영됩니다.
- **세분화 필터:** SMS 링크 상호작용을 참조하는 Segment 필터에서 봇 클릭이 제외되어 Campaigns 및 Canvases에서 더 정확한 리타겟팅이 가능합니다.
- **오케스트레이션:** SMS 링크 상호작용을 참조하는 행동 기반 트리거 및 Canvas 행동 경로에서 봇 클릭이 필터링되어 트리거가 실제 사용자 행동을 반영합니다.
- **Braze 인텔리전스:**
    - **지능형 선택:** 배리언트 선택을 최적화할 때 봇 클릭을 제외합니다.
    - **인텔리전트 채널:** 정확한 채널 선택을 위해 SMS 또는 RCS가 선택될 때 봇 클릭을 제외합니다.
    - **실험 단계:** 신뢰할 수 있는 실험 결과를 위해 봇 클릭을 제외합니다.
    - **Currents 데이터 내보내기:** 사용자 클릭과 봇 클릭을 분석하는 데 도움이 되는 `is_suspected_bot_click` 및 `suspected_bot_click_reason` 필드를 포함합니다. 이 필드는 [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), [Snowflake 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake), [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder)에서 사용할 수 있습니다.

의심되는 봇 클릭으로 인한 탈퇴는 영향을 받지 않습니다. Braze는 모든 탈퇴 요청을 평소와 같이 처리합니다. 이러한 탈퇴를 차단하려면 [제품 피드백을 제출]({{site.baseurl}}/user_guide/administer/personal/braze_support)하세요.

## SMS 클릭 이벤트의 Currents 필드 {#currents-fields-in-sms-click-events}

Braze는 SMS 클릭 이벤트에 대해 다음 Currents 필드를 포함합니다:

| 필드 | 데이터 유형 | 설명 |
| --- | --- | --- |
| `is_suspected_bot_click` | 부울 | 클릭이 의심되는 봇 클릭인지 여부를 나타냅니다. 봇 클릭 필터링이 회사에 활성화될 때까지 모든 사용자에 대해 `null`을 반환합니다. 활성화되면 이후 모든 새 클릭에 대해 `true` 또는 `false`로 채워집니다. |
| `suspected_bot_click_reason` | 문자열, 배열 | 의심되는 봇 클릭의 이유를 나타냅니다(예: `user_agent`). 필터링이 비활성화된 경우에도 채워져 잠재적인 봇 활동에 대한 인사이트를 제공합니다. 이 필드는 전역적으로 사용 가능하며, 봇 클릭 필터링이 아직 활성화되지 않은 경우에도 모든 사용자에 대해 이유가 채워집니다. 이를 통해 봇 클릭 필터링을 활성화하기 전에 잠재적인 봇 활동에 대한 인사이트를 얻을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMS 클릭 이벤트의 Currents 필드" }

## 쿼리 빌더 템플릿 {#query-builder-template}

데이터 분석에 도움이 필요하면 [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates)에서 미리 구축된 모바일 템플릿 **SMS click events by bots**를 사용할 수 있습니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### 봇 클릭 필터링은 Campaign 성과에 어떤 영향을 미치나요? {#how-does-bot-click-filtering-impact-campaign-performance}

필터링은 이전에 발송된 Campaigns에는 영향을 미치지 않습니다. 활성화되면 해당 시점부터 봇 클릭을 제외하여 클릭률이 감소합니다.

### 봇 클릭 필터링은 봇이 탈퇴 링크를 클릭하는 것을 방지하나요? {#does-bot-click-filtering-prevent-bots-from-clicking-unsubscribe-links}

아니요. 모든 탈퇴 요청은 평소와 같이 처리됩니다.

### 링크 미리보기도 봇 클릭 필터링에 포함되나요? {#are-link-previews-included-in-bot-click-filtering}

네. 링크 미리보기(예: Android 및 iOS 링크 미리보기)는 봇 클릭으로 표시되어 필터링됩니다.

### 봇 클릭 필터링을 어떻게 활성화하나요? {#how-do-i-enable-bot-click-filtering}

얼리 액세스 기간 동안 봇 클릭 필터링을 활성화하려면 Braze 계정 팀에 문의해야 합니다. 봇 클릭 필터링이 정식 출시되면 모든 SMS 및 RCS 사용자에게 기본적으로 이 기능이 활성화됩니다.

또한 [링크 단축]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening)에 대한 고급 클릭 추적을 활성화했는지 확인하세요. 이를 통해 개별 사용자 수준에서 데이터를 추적하므로 봇 클릭 분석을 받을 수 있습니다.

{% alert note %}
추가 지원이 필요하면 [고객지원에 문의]({{site.baseurl}}/braze_support)하세요.
{% endalert %}