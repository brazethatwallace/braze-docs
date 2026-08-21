---
nav_title: 이메일 셀프서비스
article_title: 이메일 셀프서비스
page_order: 0
page_type: tutorial
channel: email
description: "이 사용 방법 문서에서는 Braze의 이메일 셀프서비스를 사용하여 발신 도메인과 추적 도메인을 설정하는 방법을 다룹니다."
toc_headers: h2
---

# 이메일 셀프서비스 {#email-self-serve}

> 이 페이지에서는 Braze에서 발신 도메인과 추적 도메인을 설정하여 From 도메인과 추적 링크가 동일한 하위 도메인을 공유하도록 하는 방법을 다룹니다.

## 전제 조건 {#prerequisites}

셀프서비스 이메일 설정을 사용하려면 다음 전제 조건을 충족해야 합니다.

- 온보딩 중인 신규 고객이어야 합니다
- "Edit Domain Settings" 회사 수준 권한이 있어야 합니다
- IP 풀, IP 주소, 인증된 도메인이 있어야 합니다

## 고려 사항 {#considerations}

- 최소 3단계 발신 하위 도메인을 계획하세요. Braze는 위임된 도메인(예: "marketing.example.com") 아래에 하위 도메인을 생성하므로, 발신 도메인은 최소 3단계 깊이(예: "e.marketing.example.com")여야 합니다.
- 발신 도메인은 소유한 도메인의 하위 도메인이어야 합니다. 예를 들어, "example.com"을 소유하고 있다면 하위 도메인은 "mail.example.com"이 될 수 있으며, 이를 통해 "@mail.example.com" 발신 주소를 사용할 수 있습니다.
- 도메인 제한이 적용됩니다. 추적 도메인의 총 수는 계약에 포함된 인증된 도메인 수의 2배로 제한됩니다. 더 많은 도메인이 필요한 경우 계정 매니저에게 문의하세요.

## 설정 {#setup}

### 1단계: 발신 도메인 추가 {#step-1-add-a-sending-domain}

발신 하위 도메인은 이메일이 발송되는 주소입니다. 수신자가 보는 "from" 주소를 결정합니다.

1. **Domains** 섹션에서 **Add domain**을 선택합니다.
2. IP 풀의 **Mail from** 및 **Sending domain** 필드에 발신 도메인을 추가합니다.
    - **Mail from**(봉투 발신자 또는 반환 경로) 주소는 백그라운드에서 반송을 처리하는 주소입니다. 수신자는 이메일에서 이 주소를 볼 수 없습니다. 예를 들어, "bounce"를 하위 도메인으로 사용하면 커스텀 mail from 이메일은 "bounce.mail.example.com"이 됩니다. 이 하위 도메인을 사용하는 것은 DMARC SPF 정렬을 위한 모범 사례입니다.
    - **Sending domain**은 수신자가 받은편지함에서 보는 From 주소의 도메인입니다. 예를 들어, From 주소가 "hello@e.mail.example.com"이면 "e.mail.example.com"이 발신 도메인입니다.
{: start="3"}
3. 드롭다운에서 인증된 도메인을 선택합니다.

발신 도메인은 제출 후 변경할 수 없습니다. Braze는 인증 및 확인을 위한 DNS 레코드를 생성하고 DNS 설정에 추가합니다. 발신 도메인을 삭제해야 하는 경우 [Braze 지원팀]({{site.baseurl}}/user_guide/administer/personal/braze_support)에 문의하세요.

### 2단계: 추적 도메인 추가 {#step-2-add-a-tracking-domain}

추적 도메인은 클릭 추적 및 브랜딩 목적으로 이메일의 링크를 래핑하는 데 사용됩니다. 수신자가 이메일의 링크 위에 마우스를 올리거나 클릭할 때 이 도메인이 표시됩니다. 적절한 DNS 위임을 위해 발신 도메인 또는 인증된 도메인의 하위 도메인이어야 합니다.

1. 추적 도메인의 하위 도메인으로 사용할 **Verified domain** 또는 **Sending domain** 중 하나를 선택합니다.
    - 브랜드 일관성을 위해 추적 URL이 발신 도메인과 일치하도록 하려면 **Sending domain**을 선택합니다.
    - 더 짧은 추적 URL을 원하면 **Verified domain**을 선택합니다.

{: start="2"}
2. 추적 하위 도메인을 입력합니다. 이전에 선택한 하위 도메인 앞에 추가됩니다.

다음 예시는 선택에 따라 이메일에 추적 도메인이 어떻게 표시되는지 보여줍니다.

|  | 선택 | 추적 도메인 |
| --- | --- | ---|
| 인증된 도메인 | mail.example.com | links.mail.example.com |
| 발신 도메인 | marketing.mail.example.com | links.marketing.mail.example.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="선택에 따른 추적 도메인" }

{: start="3"}
3. 드롭다운에서 사용할 연결된 인증 또는 발신 하위 도메인을 선택합니다.
4. **Submit**을 선택합니다. **Pending** 상태의 발신 및 추적 도메인을 확인할 수 있습니다.

발신 도메인의 DNS 레코드가 전파되는 데 5~10분이 소요될 수 있습니다. 도메인을 사용할 준비가 되면 알림 이메일을 받게 됩니다. 추적 도메인의 DNS 레코드는 전파에 최대 24시간이 걸릴 수 있지만, 보통 그보다 짧습니다. 추적 도메인보다 발신 하위 도메인이 먼저 준비될 수 있습니다.

### 3단계: 워크스페이스 선택 {#step-3-select-workspaces}

도메인에 접근할 수 있는 워크스페이스를 선택한 다음 **Confirm**을 선택합니다. 새 워크스페이스가 생성될 때 발신 도메인을 자동으로 추가하도록 선택할 수도 있습니다.

### 4단계: 유니버설 링크 설정(선택 사항) {#step-4-set-up-universal-links-optional}

유니버설 링크를 사용하면 메시지의 링크가 모바일 브라우저 대신 모바일 앱에서 직접 열립니다. Braze는 사용자를 대신하여 추적 도메인에 연결 파일을 호스팅할 수 있습니다.

{% alert note %}
유니버설 링크는 추적 도메인별로 적용됩니다. 동일한 파일 내용을 여러 도메인에서 공유할 수 있지만, 각 도메인은 자체 사본을 호스팅합니다.
{% endalert %}

1. **Settings** > **Company Settings** > **Verified Domains** > **Universal Links**로 이동합니다.
2. **Set up universal links**를 선택합니다.
3. 유니버설 링크 세트 이름을 입력합니다.
4. iOS 구성을 켜고 AASA 파일을 추가합니다. JSON만 허용되는 파일 형식입니다. Braze는 파일을 읽고 발견된 앱 ID 및 구성 요소 수와 생성된 파일의 미리보기를 표시합니다.
5. Android 구성을 켜고 동일한 방식으로 Digital Asset Links 파일을 추가합니다. Braze는 패키지 이름, SHA-256 인증서 지문, 명령문 수 및 미리보기를 표시합니다.
6. 각 미리보기를 확인하여 내용이 올바른지 확인한 다음 **Next: Select tracking domains**를 선택합니다. 인증된 추적 도메인만 표시됩니다. 하나의 세트를 여러 추적 도메인에 적용할 수 있습니다.
7. 세트가 추적 도메인, 채널, iOS 상태, Android 상태 및 생성 날짜와 함께 Universal Links 페이지에 표시됩니다. Braze는 각 도메인에 대해 AASA 파일이 올바르게 호스팅되었는지 확인하고 상태 열에 결과를 보고합니다.

### 5단계: 이메일 발송 테스트 {#step-5-test-your-email-sending}

발신 도메인과 추적 도메인 모두 **Ready for use** 상태가 표시되면 설정을 테스트합니다.

1. 워크스페이스에서 **Settings** > **Email Settings**로 이동합니다.
2. **Display Name Address** 섹션에 새 발신 도메인이 나열되어 있는지 확인합니다.
3. 새 도메인을 사용하여 From 주소를 추가합니다(예: "hello@e.mail.example.com").
4. **Save**를 선택합니다.
5. 테스트 이메일 Campaign을 만들어 자신에게 발송합니다. 그런 다음 다음 사항을 확인합니다.
    - 이메일이 성공적으로 전달되었는지 확인합니다.
    - From 주소가 올바른지 확인합니다.
    - 클릭 추적 링크가 추적 도메인을 사용하는지 확인합니다.
    - 유니버설 링크가 수신자의 기기에 따라 예상대로 앱 또는 웹사이트를 여는지 확인합니다.
    - 이메일 헤더가 올바르게 표시되는지 확인합니다.

## 다음 단계 {#next-steps}

발신자 인증이 완료되면 Braze는 메시지가 지속적으로 높은 비율로 수신자의 받은편지함에 도달할 수 있도록 IP 워밍을 권장합니다. 이 설정을 완료한 후 Braze 온보딩 팀에 문의하여 도메인과 [IP 워밍]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)이 정상적으로 작동하는지 확인하세요.

## 문제 해결 {#troubleshooting}

### DNS 전파가 예상보다 오래 걸리는 경우 {#dns-propagation-is-taking-longer-than-expected}

발신 도메인 레코드는 일반적으로 5~10분 이내에 전파됩니다. 추적 도메인 레코드는 DNS 공급자의 TTL 설정에 따라 최대 24시간이 걸릴 수 있습니다. 전파가 더 오래 걸리는 경우 먼저 NS 레코드가 올바르게 추가되었는지 확인한 다음 Braze 지원팀에 문의하세요.

### 인증된 도메인을 제거할 수 없는 경우 {#im-not-able-to-remove-a-verified-domain}

인증된 도메인은 적절한 검토 없이 제거하면 발송에 문제가 발생할 수 있으므로 대시보드에서 직접 제거할 수 없습니다. Braze 지원팀에 문의하여 계정에서 도메인을 제거하세요.

### 유니버설 링크가 앱을 열지 않는 경우 {#my-universal-links-arent-opening-the-app}

먼저 Universal Links 페이지에서 iOS 및 Android 상태를 확인하세요. 도메인이 유효한 파일을 호스팅하지 않는 경우 세트를 열고 구성을 수정한 다음 다시 저장하세요. 상태가 정상으로 보이면 브라우저 주소 표시줄에 URL을 붙여넣는 대신 실제 기기에서 이메일의 링크를 통해 테스트하고 있는지 확인하세요.

## 자주 묻는 질문 {#frequently-asked-questions}

### Braze가 NS 위임 없이 SSL 인증서를 관리할 수 있나요? {#can-braze-manage-my-ssl-certificate-without-ns-delegation}

Verified Domains는 Braze에 DNS 소유권을 위임하기 위해 NS(네임 서버) 레코드가 필요합니다. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="Braze-hosted SSL certificates without NS delegation" %}

### 루트 도메인을 대신 위임할 수 있나요? {#can-i-delegate-a-root-domain-instead}

Verified Domains는 주로 하위 도메인과 함께 사용하도록 설계되고 권장됩니다. 보안상의 이유로 브랜드의 기본 상위 도메인을 위임하는 것은 권장하지 않습니다. 가시성과 제어권을 잃게 되기 때문입니다. 상위 도메인을 위임하려면 Braze 외에 다른 곳에서 사용하지 않는 상위 도메인을 사용하세요.

### 인증된 도메인이 발신 도메인이 될 수 없는 이유는 무엇인가요? {#why-cant-my-verified-domain-also-be-the-sending-domain}

Braze는 인증된 도메인 아래에만 발신 하위 도메인을 생성할 수 있으며, 인증된 도메인은 일반적으로 상위 도메인의 하위 도메인(`mail.example.com`)입니다. 따라서 이 경우 발신 도메인의 최소 깊이는 일반적인 2단계 대신 3단계(`e.mail.example.com`)입니다.

### 설정 후 NS 레코드를 수정하면 어떻게 되나요? {#what-happens-if-i-modify-any-of-my-ns-records-after-setup}

인증된 도메인은 NS 레코드가 온전한 상태에 완전히 의존합니다. NS 레코드를 변경하면 이메일 발송 및 추적이 중단될 수 있습니다.

### dig 명령이 4개의 레코드를 모두 표시하므로 NS 레코드 4줄 중 하나만 추가해도 되나요? {#can-i-add-only-one-of-four-ns-record-lines-since-my-dig-command-shows-all-four-records}

`dig` 명령을 사용하여 4개의 NS 레코드가 모두 명시적으로 존재하는지 확인하고, 설정 완료로 간주하기 전에 대시보드에서 도메인이 유효한지 확인하세요.