---
nav_title: 구독 그룹
article_title: 구독 그룹
page_order: 1
description: "이 문서에서는 LINE 메시지 구독 그룹에 대해 설명합니다."
page_type: reference
channel:
 - LINE
alias: /line/subscription_groups/
---

# LINE 구독 그룹 {#line-subscription-groups}

> LINE 사용자에게는 가입됨과 가입 취소됨, 두 가지 구독 상태가 있습니다. 각 구독 그룹은 고유한 LINE 채널에 연결됩니다. 크로스채널 구독 그룹 개요는 [구독 그룹]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups)을 참조하세요.

| 상태 | 정의 |
| --- | --- |
| 가입됨 | 사용자가 LINE 앱 내에서 LINE 채널을 팔로우한 상태입니다. 통합 단계를 완료한 후 사용자가 팔로우하면 자동으로 가입됩니다. |
| 가입 취소됨 | 사용자가 LINE 앱 내에서 LINE 채널을 팔로우하지 않았거나, 사용자가 명시적으로 LINE 채널을 언팔로우한 상태입니다. <br><br> LINE 구독 그룹에서 탈퇴한 사용자는 해당 구독 그룹에 속한 발송 채널로부터 더 이상 LINE 메시지를 수신하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE 구독 그룹" }

## 사용자의 LINE 구독 그룹 설정하기 {#set-a-users-line-subscription-group}

LINE이 사용자의 구독 상태를 호스팅합니다. Braze는 구독 상태를 업데이트하는 팔로우 및 언팔로우 이벤트를 처리합니다.

{% alert important %}
LINE 구독 그룹은 워크스페이스 간에 이동할 수 없습니다. 구독 그룹을 보관한 후 다른 워크스페이스에서 LINE 채널을 다시 통합하면, Braze는 대상 워크스페이스에 새로운 구독 그룹을 생성하며, 원래 구독 그룹은 첫 번째 워크스페이스에 그대로 남아 있습니다.
{% endalert %}

## 보관 동작 {#archive-behavior}

- **일반 보관:** LINE 구독 그룹을 보관하고 해당 채널을 다른 워크스페이스에 재통합하지 않으면, 나중에 구독 그룹의 보관을 해제할 수 있습니다.
- **영구 보관:** 구독 그룹을 보관한 후 LINE 채널을 다른 워크스페이스에 재통합하면, 원래 구독 그룹은 영구적으로 보관되며 대시보드에서 보관을 해제할 수 없습니다.

채널 재통합 단계는 [LINE 설정]({{site.baseurl}}/user_guide/channels/line/line_setup#re-integrate-a-line-channel-in-another-workspace)을 참조하세요.