---
nav_title: Campaign 자동 저장
article_title: Campaign 자동 저장
permalink: "/campaign_autosave/"
hidden: true
description: "이 참조 문서에서는 Campaign의 자동 저장 기능이 어떻게 작동하는지에 대해 설명합니다."
page_type: reference
---

# Campaign 자동 저장 {#autosaving-campaigns}

> Braze에서 Campaign을 구축할 때 변경 사항이 자동으로 저장됩니다. 이를 통해 진행 상황이 보존된다는 확신을 가지고 Campaign 세부 사항을 세밀하게 조정하는 데 집중할 수 있습니다.

{% alert important %}
자동 저장은 현재 베타 버전이며 Campaign에서만 사용할 수 있습니다. 이 베타에 참여하고 싶으시면 고객 성공 매니저에게 문의하세요.
{% endalert %}

{% alert warning %}
이메일이나 인앱 메시지와 같은 전체화면 편집기에서 메시지를 편집할 때, 메시지에 대한 변경 사항은 자동 저장되지 않습니다. **Done**을 선택하여 편집기를 종료하고 Campaign으로 돌아가면, 다음 자동 저장이 발생할 때 메시지 변경 사항이 저장됩니다. 예방 조치로 메시지를 수동으로 저장할 수도 있습니다.
{% endalert %}

## 작동 방식 {#how-it-works}

![][1]{: style="float:right;max-width:40%;margin-left:15px;"}

Campaign 편집기에서 편집하고 탭 간에 전환할 때 Campaign이 자동으로 주기적으로 저장됩니다.

변경 사항은 초안 및 활성 Campaign 모두에 대해 초안으로 저장됩니다. 중지된 Campaign의 경우 변경 사항은 저장되지만 Campaign은 중지된 상태로 유지됩니다.

다른 사용자와 함께 Campaign을 변경하는 경우, 첫 번째 변경 사항 세트가 저장됩니다. 두 번째로 변경 사항을 저장하는 사용자라면, 페이지를 새로고침하여 Campaign의 최신 업데이트를 확인해야 합니다.

[1]: {% image_buster /assets/unlisted_docs/img/campaign_autosave.png %}