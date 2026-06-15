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

> LINE 사용자에게는 가입됨과 가입 취소됨, 두 가지 구독 상태가 있습니다. LINE은 워크스페이스당 최대 100개의 구독 그룹을 가질 수 있으며, 각 구독 그룹은 고유한 LINE 채널에 연결됩니다.

| 상태 | 정의 |
| --- | --- |
| 가입됨 | 사용자가 LINE 앱 내에서 LINE 채널을 팔로우한 상태입니다. 통합 단계를 완료한 후 사용자가 팔로우하면 자동으로 가입됩니다. |
| 가입 취소됨 | 사용자가 LINE 앱 내에서 LINE 채널을 팔로우하지 않았거나, 사용자가 명시적으로 LINE 채널을 언팔로우한 상태입니다. <br><br> LINE 구독 그룹에서 탈퇴한 사용자는 해당 구독 그룹에 속한 발송 채널로부터 더 이상 LINE 메시지를 수신하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE subscription groups" }

## 사용자의 LINE 구독 그룹 설정하기 {#setting-a-users-line-subscription-group}

LINE이 사용자의 구독 상태를 호스팅합니다. Braze는 구독 상태를 업데이트하는 팔로우 및 언팔로우 이벤트를 처리합니다.