---
nav_title: "메시징 상호작용 데이터"
article_title: "메시징 상호작용 데이터"
alias: "/messaging_interaction_data/"
page_order: 1
description: "이 참조 문서에서는 Campaign 및 Canvas 상호작용 데이터와 그 가용성에 대해 다룹니다."
page_type: reference
---

# 메시징 상호작용 데이터 가용성 정보 {#about-messaging-interaction-data-availability}

> Campaign 및 Canvases의 메시징 상호작용 데이터에 대해 알아보세요. Braze가 이 데이터를 얼마나 오래 보관하는지, 그리고 리타겟팅에 어떤 기능이 이 데이터를 사용하는지 확인할 수 있습니다.

## 메시징 상호작용 데이터란 무엇인가요? {#what-is-messaging-interaction-data}

메시징 상호작용 데이터는 사용자가 수신한 Campaign 또는 Canvas와 어떻게 상호작용하는지를 나타냅니다(예: 사용자가 Campaign A를 열람하거나 배리언트 A를 수신하는 경우). 이 데이터는 리타겟팅에 사용됩니다.

## 메시징 상호작용 데이터는 언제 사용할 수 있나요? {#when-is-messaging-interaction-data-available}

상호작용 데이터는 항상 사용할 수 있습니다. 활성 Campaigns 및 Canvases의 경우, 상호작용 데이터는 항상 실시간으로 사용할 수 있습니다.

중지된 Campaigns 및 Canvases의 경우, 해당 상호작용 데이터는 활성 Campaigns 또는 Canvases의 리타겟팅 필터에서 사용되지 않으면 3개월 후에 만료됩니다. 만료된 상호작용 데이터는 장기 스토리지로 이동되며, 설명된 프로세스를 사용하여 복원하지 않는 한 사용할 수 없습니다.

만료된 상호작용 데이터는 절대 삭제되지 않으며 언제든지 복원할 수 있습니다.

### 상호작용 데이터를 사용하는 기능들 {#features-that-use-interaction-data}

다음 기능들은 메시징 상호작용 데이터를 사용합니다:

- 특정 Campaign 또는 Canvas를 리타겟하는 리타겟팅 필터
    - Clicked Alias in Campaign
    - Clicked Alias in Canvas Step
    - Clicked/Opened Campaign
    - Clicked/Opened Step
    - Converted From Campaign
    - Converted From Canvas
    - Entered Canvas Variation
    - In Campaign Control Group
    - In Canvas Control Group
    - Last Received Message from Specific Campaign
    - Last Received Message from Specific Canvas Step
    - Received Campaign Variant
    - Received Message from Campaign
    - Received Message from Canvas Step
- 특정 태그의 Campaigns 또는 Canvases를 리타겟하는 리타겟팅 필터
    - Received Message from Campaign or Canvas with Tag
    - Clicked/Opened Campaign or Canvas With Tag
    - Last Received Message from Campaign or Canvas With Tag
- 고객 프로필의 **Campaigns Received** 및 **Canvas Messages Received** 목록
- `/users/export` 엔드포인트
- Campaign 및 Canvas 요약 페이지의 **사용자 데이터** CSV 내보내기

이러한 기능들은 결과에 만료된 상호작용 데이터를 포함하지 않습니다. 이러한 기능의 결과에 만료된 상호작용 데이터를 포함하려면, 만료된 데이터가 있는 Campaign 또는 Canvas를 복원하세요.

예를 들어, 상호작용 데이터가 만료된 경우 Canvases를 실행할 수 없으며, 이는 Canvas에 팀을 추가하는 것과 같은 편집 사항을 저장할 수 없다는 것을 의미합니다.

### 상호작용 데이터를 사용하지 않는 기능들 {#features-that-dont-use-interaction-data}

다음 기능들은 메시징 상호작용 데이터를 사용하지 **않으며**, 이는 메시징 상호작용 데이터의 만료에 영향을 받지 않는다는 것을 의미합니다:

- Campaign 및 Canvas 설정
- Campaign 및 Canvas 분석
- 분석 보고서(보고서 빌더, 쿼리 빌더, 참여 보고서 등)
- Currents
- Snowflake 데이터 공유
- 세그먼트 확장
- 데이터 포인트
- 다음 리타겟팅 필터:
    - Clicked Alias in Any Campaign or Canvas Step
    - Feature Flags
    - Hard Bounced
    - Has Marked You As Spam
    - Has Never Received a Message from Campaign or Canvas Step
    - Invalid Phone Number
    - Last Engaged With Message
    - Last Enrolled in Any Control Group
    - Last In App Message Impression
    - Last Received Any Message
    - Last Received Email
    - Last Received Push
    - Last Received 단문 메시지 서비스
    - Last Received Webhook
    - Last Received WhatsApp
    - Last Sent Specific 단문 메시지 서비스 Inbound Keyword Category
    - Last Viewed News Feed
    - News Feed View Count

## 메시징 상호작용 데이터를 복원하려면 어떻게 해야 하나요? {#how-do-i-restore-messaging-interaction-data}

상호작용 데이터를 복원하려면 다음 단계를 따르세요:

1. 만료된 Campaign 또는 Canvas로 이동합니다.
2. Campaign 또는 Canvas 랜딩 페이지 상단의 배너에서 **상호작용 데이터 복원**을 선택합니다.

**Campaigns** 페이지에서 여러 Campaign의 상호작용 데이터를 복원할 수도 있습니다. Campaign을 선택한 다음 **상호작용 데이터 복원**을 선택하세요.

상호작용 데이터 복원에 걸리는 시간은 다를 수 있지만, 대부분의 경우 5~15분 정도 소요됩니다. 복원이 완료되면 이메일을 받게 됩니다.

### 태그별 복원 {#restoring-by-tag}

특정 태그가 지정된 만료된 Campaign 또는 Canvases의 상호작용 데이터를 복원할 수도 있습니다.

1. **Campaigns** 또는 **Canvas** 페이지로 이동하여 관련 태그로 검색합니다.
2. Campaign 또는 Canvases를 선택합니다.
3. **상호작용 데이터 복원**을 선택하여 해당 Campaign 또는 Canvases의 데이터를 복원합니다.

비활성 상태가 3개월 더 지속되면 해당 Campaign 또는 Canvases는 다시 만료됩니다.

### 태그별 리타겟팅 {#retargeting-by-tag}

태그별로 리타겟팅하는 리타겟팅 필터를 사용하는 Campaign은 만료에서 면제되지 않습니다. 태그별로 리타겟팅하는 리타겟팅 필터에는 다음이 포함됩니다:

- Received Message from Campaign or Canvas with Tag
- Clicked/Opened Campaign or Canvas With Tag
- Last Received Message from Campaign or Canvas With Tag

## 과거에 메시징 상호작용 데이터는 언제 사용할 수 있었나요? {#when-was-messaging-interaction-data-available-in-the-past}

이전에는 Campaign 또는 Canvas가 다음 조건을 모두 충족하면 메시지 상호작용 데이터가 삭제되었습니다:

- 25개월(캘린더 기준) 동안 메시지를 보내지 않았으며, 그리고
- 활성 Campaigns, Canvases 또는 Content Cards에서 리타겟팅에 사용되지 않은 경우.

이전에 메시징 상호작용 데이터가 삭제된 Campaigns 및 Canvases는 Campaigns, Canvases, Segments의 리타겟팅 필터에 사용할 수 없습니다.

## 문제 해결 {#troubleshooting}

### Campaign 또는 Canvas 만료일이 계속 내일로 표시되는 이유는 무엇인가요? {#why-does-a-campaign-or-canvas-expiration-date-keep-showing-tomorrow}

중지된 Campaign 또는 Canvas가 활성 리타겟팅 필터(예: 활성 Segment, Campaign, Canvas 또는 Content Cards)에서 여전히 참조되고 있는 경우, Braze는 해당 상호작용 데이터를 아직 오프로드하지 않습니다.

이 경우 UI에 표시되는 만료일은 다음 예정된 정리 실행을 반영하므로, 참조가 여전히 존재하는 동안에는 "내일"로 표시되며 계속 앞으로 이동할 수 있습니다.

모든 활성 리타겟팅 참조를 제거하면, 상호작용 데이터는 다음 정리 주기(일반적으로 다음 날)에 오프로드됩니다.

만료된 상호작용 데이터가 있는 Campaigns, Canvases 또는 Content Cards를 재개하거나 보관 해제하려고 할 때 다음과 같은 오류 메시지가 표시될 수 있습니다.

| 오류 메시지 | 표시 시점 | 문제 해결 |
| --- | --- | --- |
| "Can't resume Canvases because at least one Canvas is using filters or segments that have expired data. Remove these and try again." | 만료된 상호작용 데이터가 있는 필터 또는 Segments를 사용하는 하나 이상의 Canvases를 재개하려고 할 때(일괄 작업) | 필터에서 참조된 Campaigns 또는 Canvases의 [상호작용 데이터를 복원](#how-do-i-restore-messaging-interaction-data)하거나, Canvas에서 영향을 받는 필터를 제거하세요 |
| "Can't resume {name} because it is using filters or segments that have expired data. Remove these and try again." | 만료된 상호작용 데이터가 있는 필터 또는 Segments를 사용하는 단일 Canvas를 재개하려고 할 때 | 필터에서 참조된 Campaigns 또는 Canvases의 [상호작용 데이터를 복원](#how-do-i-restore-messaging-interaction-data)하거나, Canvas에서 영향을 받는 필터를 제거하세요 |
| "Resume is only available for stopped Canvases with available interaction data" | 일괄 작업 메뉴에서 Canvas를 재개하려고 하지만 Canvas에 만료된 상호작용 데이터가 있을 때 | Canvas의 [상호작용 데이터를 복원](#how-do-i-restore-messaging-interaction-data)하세요 |
| "You can't resume these Campaigns. One or more Campaigns include expired filters." | 만료된 상호작용 데이터가 있는 필터를 사용하는 하나 이상의 Campaigns를 재개하려고 할 때 | 필터에서 참조된 Campaigns 또는 Canvases의 [상호작용 데이터를 복원](#how-do-i-restore-messaging-interaction-data)하거나, Campaign에서 영향을 받는 필터를 제거하세요 |
| "You can't unarchive these Cards. One or more Cards include expired filters." | 만료된 상호작용 데이터가 있는 필터를 사용하는 하나 이상의 Content Cards를 보관 해제하려고 할 때 | 필터에서 참조된 Campaigns 또는 Canvases의 [상호작용 데이터를 복원](#how-do-i-restore-messaging-interaction-data)하거나, 카드에서 영향을 받는 필터를 제거하세요 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="일반적인 오류 메시지" }