---
nav_title: 워크스페이스 간 전환
article_title: 워크스페이스 간 전화번호 및 구독 그룹 전환
page_order: 3
description: "이 참조 문서에서는 WhatsApp 전화번호와 구독 그룹을 워크스페이스 간에 전환하는 방법을 다룹니다."
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp 전화번호 및 구독 그룹을 워크스페이스 간에 전환하기 {#transfer-whatsapp-phone-numbers-and-subscription-groups-between-workspaces}

> 이 페이지에서는 WhatsApp Business Account(WABA) 전화번호와 관련 구독 그룹을 Braze 내에서 한 워크스페이스에서 다른 워크스페이스로 이동하는 방법을 설명합니다. 이 프로세스를 통해 Braze에서 WhatsApp을 사용하는 경험이 간소화되며, 엔지니어링 지원의 필요성이 줄어듭니다.

## 필수 조건 {#prerequisites}

- 원래 워크스페이스와 새 워크스페이스 모두에서 [사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) "구독 그룹 관리"가 있는지 확인하세요.
- WABA는 여러 [Braze 클러스터]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)에 걸쳐 사용할 수 없습니다. 하나의 회사 내에서 작업하는 경우 이런 상황이 발생할 가능성은 낮습니다.

## 전화번호 및 구독 그룹 전환하기 {#transferring-a-phone-number-and-subscription-group}

### 1단계: 구독 그룹 아카이브하기 {#step-1-archive-the-subscription-group}

WhatsApp 구독 그룹을 아카이브하려면 다음 단계를 따르세요:

1. 구독 그룹이 현재 존재하는 워크스페이스로 이동합니다.
2. **오디언스** > **구독 그룹 관리**로 이동하여 이동하려는 WhatsApp 전화번호와 연결된 구독 그룹을 찾습니다.
3. 구독 그룹의 상태 위에 마우스를 올리고 <i class="fa-solid fa-box-archive" aria-label="아카이브"></i> **아카이브**를 선택합니다. 이렇게 하면 구독 그룹이 비활성으로 표시되지만 삭제되지는 않습니다.

![구독 그룹의 '활성' 상태 위에 마우스를 올렸을 때 나타나는 '아카이브' 버튼.]({% image_buster /assets/img/whatsapp/archive_subscription_group.png %}){: style="max-width:70%;"}

### 2단계: WhatsApp 전화번호를 새 워크스페이스에 통합하기 {#step-2-integrate-the-whatsapp-phone-number-into-the-new-workspace}

1. WhatsApp 전화번호를 이동하려는 워크스페이스로 이동합니다.
2. **파트너 통합** > **기술 파트너** > **WhatsApp**으로 이동한 다음 **WhatsApp Messaging Integration** 섹션으로 스크롤합니다.
3. **새 구독 그룹 및 전화번호 생성** 옵션을 선택합니다.
4. 통합 프로세스를 시작합니다. 이 과정에서 아카이브된 구독 그룹의 전화번호를 선택할 수 있습니다.

### 3단계: 통합 확인하기 {#step-3-verify-the-integration}

1. 통합을 완료한 후, WhatsApp 전화번호가 새 워크스페이스의 구독 그룹과 연결되었는지 확인합니다.
2. 해당 WhatsApp 전화번호를 통해 메시지를 보내고 받을 수 있는지 테스트하여 확인합니다.

## 고려 사항 {#considerations}

- WhatsApp 전화번호를 원래 워크스페이스로 다시 전환해야 하는 경우, 동일한 단계를 반복하세요. 대상 워크스페이스에서 구독 그룹을 아카이브한 다음, 원래 워크스페이스에 통합합니다.
- 전환 과정에서 Meta Business Manager에서 WhatsApp 전화번호를 제거할 필요는 없습니다.