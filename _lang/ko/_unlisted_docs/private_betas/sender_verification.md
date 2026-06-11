---
nav_title: "발송자 확인"
article_title: "발송자 확인"
permalink: /sender_verification/
description: "이 문서에서는 발송자 확인을 설정하고 자체 하위 도메인을 Braze에 위임하는 방법을 다룹니다."
hidden: true
---

# 발송자 확인 {#sender-verification}

> 이 페이지에서는 자체 하위 도메인을 Braze에 위임하는 방법을 다룹니다. 발송자 확인을 사용하면 전용 발송 하위 도메인의 제어를 Braze에 설정 및 위임할 수 있으며, From 도메인과 추적 링크가 동일한 하위 도메인 아래에 위치하여 더 강력한 브랜드 일관성을 확보할 수 있습니다.

{% alert important %}
이 기능은 베타 버전이며 Braze 내부 팀에서만 사용할 수 있습니다.
{% endalert %}

## 발송자 확인 작동 방식 {#how-sender-verification-works}

도메인 위임은 특정 발송 하위 도메인의 제어를 Braze에 위임할 수 있는 DNS 설정 옵션입니다. 예를 들어, "marketing.example.com"을 하위 도메인으로 사용하는 경우, Braze가 이메일 등 메시징 기능에 필요한 DNS 레코드를 관리합니다.

### 장점 {#benefits}

발송자 확인을 사용하면 설정과 유지 관리가 간소화됩니다. Braze가 필요한 항목을 생성하고 업데이트하므로 DNS 구성 오류가 발생할 가능성이 줄어듭니다.

### 고려 사항 {#considerations}

- 전용 하위 도메인을 선택하세요.
- 도메인 위임을 완료하면 Braze가 위임된 하위 도메인의 DNS 레코드를 관리합니다.
- 여러 브랜드 또는 Braze 워크스페이스가 있는 경우, 브랜드당 하나의 위임된 하위 도메인을 선택할 수 있습니다.
- 발송자 확인에는 발송 도메인 50개와 추적 도메인 50개의 제한이 있습니다. 더 추가해야 하는 경우 Braze 고객지원 팀에 문의하세요.

## 1단계: 필수 조건 완료 {#step-1-complete-prerequisites}

Braze 대시보드에서 **설정** > **회사 설정** 아래의 **발송자 확인**으로 이동하여 온보딩 매니저와 함께 다음 필수 조건을 완료하세요:

- IP 풀 추가
- IP 주소 추가
- 위임된 도메인 추가 및 NS 레코드 확인

## 2단계: 발송 하위 도메인 추가 {#step-2-add-your-sending-subdomain}

1. **발송 도메인** 섹션에서 **발송 도메인 추가**를 선택합니다.
2. IP 풀의 발송 하위 도메인으로 **Mail from** 및 **발송 도메인** 필드를 입력합니다. 예시: "marketing.mail.example.com"
3. 드롭다운에서 위임된 도메인을 선택합니다.
4. 그런 다음 **제출**을 선택합니다.

![Mail from 주소와 발송 도메인 필드, 위임된 도메인 드롭다운 및 제출 버튼이 표시된 양식.]({% image_buster /assets/unlisted_docs/img/sender_verification/sending_subdomain.png %}){: style="max-width:85%;"}

DNS 레코드가 전파되는 데 5~10분이 소요됩니다. 완료되면 도메인을 사용할 준비가 되었다는 알림 이메일을 받게 됩니다.

{% alert important %}
도메인은 제출 후 변경할 수 없습니다. Braze가 확인 및 인증을 위한 DNS 레코드를 생성하고 DNS 설정에 추가합니다.
{% endalert %}

## 3단계: 추적 하위 도메인 추가 {#step-3-add-your-tracking-subdomain}

하위 도메인을 생성하고 확인이 완료된 후:

1. **추적 도메인 추가**를 선택합니다.
2. 추적 하위 도메인을 입력합니다. 예를 들어, 추적 하위 도메인이 "click"인 경우 하위 도메인은 "click.marketing.mail.example.com"이 됩니다.
3. 드롭다운에서 연결된 발송 도메인을 선택합니다.
4. 그런 다음 **제출**을 선택합니다.

![추가할 추적 도메인 예시.]({% image_buster /assets/unlisted_docs/img/sender_verification/tracking_domain.png %}){: style="max-width:85%;"}

이러한 DNS 레코드가 전파되는 데 최대 24시간이 소요될 수 있지만, 보통 더 짧은 시간이 걸립니다. 완료되면 도메인을 사용할 준비가 되었다는 알림 이메일을 받게 됩니다.

{% alert important %}
적절한 DNS 위임을 위해 추적 도메인은 발송 도메인의 하위 도메인이어야 합니다.
{% endalert %}

## 4단계: 워크스페이스 선택 {#step-4-select-the-workspaces}

다음으로, 도메인에 접근할 수 있어야 하는 워크스페이스를 선택하고 **확인**을 선택합니다. 선택적으로 새 워크스페이스가 생성될 때 발송 도메인을 자동으로 추가할 수 있습니다.

![워크스페이스 선택 체크박스와 새 워크스페이스에 발송 도메인을 자동으로 추가하는 옵션, 확인 버튼이 표시된 대화 상자.]({% image_buster /assets/unlisted_docs/img/sender_verification/select_workspaces_domain.png %}){: style="max-width:85%;"}

## 5단계: 이메일 발송 테스트 {#step-5-test-your-email-sending}

발송 도메인과 추적 도메인이 **사용 준비 완료** 상태가 되면 다음을 수행하여 이메일 발송을 테스트할 수 있습니다:

1. 워크스페이스에서 **설정** > **이메일 설정**으로 이동합니다.
2. **표시 이름 주소** 섹션에 새 발송 도메인이 나열되어 있는지 확인합니다.
3. 새 도메인을 사용하여 이메일 주소를 추가합니다(예: "marketing@marketing.mail.example.com").
4. **저장**을 선택합니다.
5. 다음으로, 테스트 이메일 Campaign을 생성하고 자신에게 이메일을 보내 다음 사항을 확인합니다:
- 이메일이 성공적으로 전달되었는지 확인합니다.
- From 주소가 올바른지 확인합니다.
- 클릭 추적 링크가 추적 도메인을 사용하는지 확인합니다.
- 이메일 헤더가 올바르게 표시되는지 확인합니다.