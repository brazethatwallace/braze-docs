---
nav_title: 옵트인 및 옵트아웃 키워드
article_title: SMS 옵트인 및 옵트아웃 키워드
page_order: 0
description: "이 참조 문서에서는 Braze가 SMS 메시징에 대한 기본 옵트인 및 옵트아웃 키워드를 처리하는 방법을 다룹니다."
page_type: reference
alias: /optin_optout/
tool:
  - Dashboard

channel:
  - SMS
---

# 옵트인 및 옵트아웃 키워드 {#opt-in-and-opt-out-keywords}

> 규정에 따라 모든 옵트인, 옵트아웃, 도움말/정보 키워드 응답에 대한 회신이 있어야 합니다. Braze는 다음과 같은 _정확한 단일 단어, 대소문자 구분 없는_ 메시지를 자동으로 처리하며, 모든 수신 요청에 대해 사용자 및 관련 전화번호의 [구독 그룹 상태]({{site.baseurl}}/sms_rcs_subscription_groups/)를 자동으로 업데이트합니다.

## 기본 키워드 {#default-keywords}

Braze는 다음 키워드를 자동으로 처리하고 모든 수신 요청에 대해 전화번호의 구독 그룹 상태를 업데이트합니다. 이러한 기본 키워드와 응답은 커스터마이즈할 수도 있으며, [커스텀 키워드]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling/)를 추가할 수도 있습니다.

{% alert tip %}
옵트아웃 처리를 확장하고 싶으신가요? [유사 옵트아웃]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out/)을 사용해 보세요. 이 기능은 수신 메시지가 옵트아웃 키워드와 정확히 일치하지 않지만 옵트아웃 의도를 나타내는 경우를 인식하려고 시도합니다.
{% endalert %}

| 유형 | 키워드 | 변경 사항 |
|-|-------|---|
| 옵트인 | `START`<br> `YES`<br> `UNSTOP` | 이러한 `Opt-In` 키워드 중 하나가 포함된 수신 요청은 구독 그룹 상태가 `subscribed`로 변경됩니다. 또한 해당 구독 그룹에 연결된 발신자 풀이 해당 고객에게 SMS, MMS 또는 RCS 메시지를 보낼 수 있게 됩니다(발신자가 지원하는 메시징 유형에 따라 다름). <br><br>사용자는 정의된 옵트인 자동 응답을 수신합니다.  |
| 옵트아웃 | `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | 이러한 `Opt-Out` 키워드 중 하나가 포함된 수신 요청은 구독 그룹 상태가 `unsubscribed`로 변경됩니다. 또한 해당 구독 그룹에 연결된 번호 풀이 더 이상 해당 고객에게 메시지를 보낼 수 없게 됩니다.<br><br>사용자는 정의된 옵트아웃 자동 응답을 수신합니다. |
| 도움말 | `HELP`<br> `INFO` | 사용자는 정의된 도움말 자동 응답을 수신합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Default keywords" }

**정확한 단일 단어 메시지**만 처리됩니다(대소문자 구분 없음). `STOP PLEASE`와 같은 키워드는 [유사 옵트아웃]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out/)이 활성화되지 않은 경우 무시됩니다.

수신자가 `HELP` 또는 `INFO` 키워드를 사용하면 자동으로 응답이 트리거됩니다. 이러한 자동 응답 메시지의 기본 응답은 [온보딩]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/) 및 전화번호 확보 기간 동안 설정됩니다. 초기 온보딩 기간 이후에도 이러한 응답을 계속 업데이트할 수 있습니다.

{% alert tip %}
옵트아웃 처리를 확장하고 싶으신가요? [유사 옵트아웃]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out/)을 사용해 보세요. 이 기능은 수신 메시지가 옵트아웃 키워드와 정확히 일치하지 않지만 옵트아웃 의도를 나타내는 경우를 인식하려고 시도합니다.
{% endalert %}

## 자연어 옵트아웃 처리 {#handle-natural-language-opt-outs}

감성 분석을 사용하여 표준 또는 커스텀 키워드 외의 옵트아웃 의도를 캡처하는 [Braze 에이전트]({{site.baseurl}}/user_guide/brazeai/agents/)를 생성할 수 있습니다(예: "더 이상 문자 보내지 마세요"). 단계별 안내는 [에이전트 콘솔에서 자연어 옵트아웃 처리]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/#handle-natural-language-opt-outs-in-the-agent-console)를 참조하세요.