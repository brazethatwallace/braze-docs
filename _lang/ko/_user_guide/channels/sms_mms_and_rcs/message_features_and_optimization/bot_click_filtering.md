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

Braze는 봇 클릭(비인간 상호작용(NHI)이라고도 함)으로 의심되는 항목을 식별하기 위해 여러 입력을 사용하는 독자적인 감지 시스템을 보유하고 있습니다. 봇 클릭은 클릭률을 부풀려 인게이지먼트 측정기준을 왜곡할 수 있습니다. Braze는 이를 필터링하여 의사 결정에 필요한 신뢰할 수 있는 데이터를 확보할 수 있도록 지원합니다.

이 시스템은 웹 크롤러, Android 및 iOS 링크 미리보기 또는 CPaaS 보안 소프트웨어와 관련된 사용자 에이전트를 분석합니다. 필터링되는 사용자 에이전트의 몇 가지 예로는 `GoogleBot`, `GoogleMessages/20`, `python-requests/2.32.3`, `Barracuda Sentinel (EE)` 등이 있습니다.

## 영향을 받는 측정기준 및 워크플로 {#affected-metrics-and-workflows}

다음 Braze 측정기준 및 워크플로는 봇 클릭의 영향을 받습니다:

- **_총 클릭수_:** Campaign 분석 및 Canvas 분석에서 봇 클릭을 제외하여 사람의 상호작용만 반영합니다.
- **세분화 필터:** SMS 링크 상호작용을 참조하는 Segment 필터는 봇 클릭을 제외하여 Campaigns 및 Canvases에서 보다 정확한 리타겟팅을 지원합니다.
- **오케스트레이션:** SMS 링크 상호작용을 참조하는 행동 기반 트리거 및 Canvas 작업 경로에서 봇 클릭이 필터링되어 트리거가 사람의 행동을 반영할 수 있습니다.
- **Braze 인텔리전스:**
    - **지능형 선택:** 배리언트 선택을 최적화할 때 봇 클릭을 제외합니다.
    - **인텔리전트 채널:** SMS 또는 RCS가 선택된 경우 봇 클릭을 제외하여 정확한 채널 선택을 지원합니다.
    - **실험 단계:** 신뢰할 수 있는 실험 성과를 위해 봇 클릭을 제외합니다.
    - **Currents 데이터 내보내기:** 사람과 봇 클릭을 분석하는 데 도움이 되도록 `is_suspected_bot_click` 및 `suspected_bot_click_reason` 필드를 포함합니다. 이 필드는 [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), [Snowflake 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake), [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder)에서 사용할 수 있습니다.

의심되는 봇 클릭으로 인한 탈퇴는 영향을 받지 않습니다. Braze는 모든 탈퇴 요청을 평소와 같이 처리합니다. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="blocking unsubscribes from suspected bot clicks" %}

## SMS 클릭 이벤트의 Currents 필드 {#currents-fields-in-sms-click-events}

Braze는 SMS 클릭 이벤트에 대해 다음과 같은 Currents 필드를 포함합니다:

| 필드 | 데이터 유형 | 설명 |
| --- | --- | --- |
| `is_suspected_bot_click` | Boolean | 클릭이 봇 클릭으로 의심되는지 여부를 나타냅니다. SMS 및 RCS 단축 링크 클릭의 경우, Braze는 모든 클릭에 대해 봇 감지를 평가하고 이 필드에 `true` 또는 `false`를 채웁니다. |
| `suspected_bot_click_reason` | 문자열, Array | 봇 클릭으로 의심되는 이유를 나타냅니다(예: `user_agent`). SMS 및 RCS 단축 링크 클릭에 대해 봇 감지가 실행될 때 채워집니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMS 클릭 이벤트의 Currents 필드" }

## 쿼리 빌더 템플릿 {#query-builder-template}

데이터 분석에 도움이 필요하면 [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates)에서 미리 만들어진 모바일 템플릿 **SMS click events by bots**를 사용할 수 있습니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### 봇 클릭 필터링은 Campaign 성능에 어떤 영향을 미치나요? {#how-does-bot-click-filtering-impact-campaign-performance}

봇 클릭 필터링은 SMS 및 RCS 단축 링크 클릭에 대해 자동으로 실행됩니다. 대시보드 클릭률에서는 봇으로 의심되는 클릭이 제외되므로, 보고되는 수치는 자동화된 링크 미리보기나 크롤러 트래픽이 아닌 실제 사용자의 상호작용을 반영합니다.

### 봇 클릭 필터링이 봇의 탈퇴 링크 클릭을 방지하나요? {#does-bot-click-filtering-prevent-bots-from-clicking-unsubscribe-links}

아니요. 모든 탈퇴 요청은 평소와 동일하게 처리됩니다.

### 링크 미리보기도 봇 클릭 필터링에 포함되나요? {#are-link-previews-included-in-bot-click-filtering}

네. 링크 미리보기(예: Android 및 iOS 링크 미리보기)는 봇 클릭으로 표시되어 필터링됩니다.