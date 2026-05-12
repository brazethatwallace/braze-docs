---
nav_title: 셀프서비스 커스텀 도메인
article_title: 셀프서비스 커스텀 도메인
page_order: 2
description: "이 페이지에서는 링크 단축과 함께 커스텀 도메인을 사용하여 단축 URL의 모양과 느낌을 개인화하는 방법을 다룹니다."
page_type: reference
alias: "/custom_domains/"
tool:
  - Campaigns
channel:
  - SMS
---

# 셀프서비스 커스텀 도메인 {#self-serve-custom-domains}

> 이 페이지에서는 Braze 대시보드에서 자체 커스텀 도메인을 설정하는 방법을 다룹니다. 커스텀 도메인을 사용하면 일반적인 단축 링크나 Braze 도메인(`brz.ai`) 대신 브랜드 아이덴티티를 반영하는 브랜드 단축 링크를 사용할 수 있어, SMS 링크에 대한 사용자 신뢰도와 Campaign 참여도를 높일 수 있습니다.

셀프서비스 커스텀 도메인을 사용하면 SMS, RCS, WhatsApp용 커스텀 도메인을 Braze 대시보드에서 직접 구성하고 관리할 수 있습니다. 한 곳에서 최대 10개의 커스텀 도메인을 쉽게 추가, 모니터링 및 관리할 수 있습니다.

## 셀프서비스 커스텀 도메인의 이점 {#benefits-of-self-serve-custom-domains}

- **간소화된 설정:** **회사 설정** 페이지에서 도메인을 구성하여 설정 시간을 단축합니다.
- **향상된 투명성:** 대시보드의 배너를 통해 도메인 설정 상태에 대한 실시간 업데이트를 받을 수 있습니다.
- **사전 알림:** 커스텀 도메인이 연결되거나 구성 오류가 발생하면 즉시 알림을 받습니다.

## 도메인 요구 사항 {#domain-requirements}

- 도메인은 사용자가 직접 구매, 소유 및 관리해야 합니다. GoDaddy, Amazon Route 53, Google Domains와 같은 도메인 등록 기관을 통해 할 수 있습니다.
- 이 기능에 사용되는 도메인은 다음 조건을 충족해야 합니다:
  - 고유해야 합니다(웹사이트 도메인과 다른 도메인)
  - 웹 콘텐츠를 호스팅하는 데 사용할 수 없습니다
    - 고유한 하위 도메인을 사용할 수도 있습니다. 예를 들어, `braze.com` 도메인에 `sms.braze.com` 또는 `whatsapp.braze.com`과 같은 하위 도메인을 사용할 수 있습니다.

## 커스텀 도메인 위임 {#delegating-your-custom-domain}

Braze의 링크 단축 및 클릭 추적 서비스와의 적절한 라우팅 및 인프라 호환성을 보장하기 위해 커스텀 도메인을 Braze에 위임해야 합니다. 도메인을 Braze에 위임하면 서비스 중단을 방지하기 위해 인증서 갱신을 자동으로 처리합니다.

## 커스텀 도메인 추가 {#adding-a-custom-domain}

1. Braze에서 **Company Settings** > **SMS/RCS and Messaging Apps Domains**로 이동합니다.
![여러 도메인이 나열된 "SMS/RCS and Messaging Apps Domains" 페이지.]({% image_buster /assets/img/main_page.png %})

{: start="2"}
2. **Add Domain**을 선택하여 새 커스텀 도메인 설정을 시작합니다.
3. 구매한 커스텀 도메인을 인앱 입력란에 입력합니다. 기존 유효성 검사 로직을 사용하여 올바른 형식을 확인한 후 **Next**를 선택하고 **Submit**을 선택합니다.

!["SMS/RCS and Messaging Apps Domains" 페이지의 "Add Domain" 버튼.]({% image_buster /assets/img/custom_domain_button.png %}){: style="max-width:70%;"}

{: start="4"}
4. 기술 팀(엔지니어링 또는 IT 등)에 표시되는 Cloudflare DNS 레코드 세부 정보로 DNS 구성을 업데이트하도록 요청합니다. 기술 팀은 45일 이내에 이 세부 정보로 DNS 레코드를 업데이트해야 합니다.
  - DNS 레코드를 업데이트하는 데 추가 시간이 필요한 경우, 프로세스를 다시 시작하여 도메인에 대한 새 DNS 레코드 세트를 생성할 수 있습니다.

Braze는 약 30분마다 DNS 구성을 폴링하여 업데이트를 확인합니다.

![도메인 설정을 완료하기 위한 3단계가 포함된 "DNS record" 섹션.]({% image_buster /assets/img/dns_record.png %})

{% alert note %}
도메인 진행 상황은 자동으로 저장됩니다. 중간에 나가야 하는 경우, **SMS/RCS and Messaging Apps Domains** 페이지에서 보류 중인 도메인 항목을 선택하여 나중에 다시 시작할 수 있습니다.
{% endalert %}

### 지속적인 관리 및 사용 {#ongoing-management-and-usage}

도메인이 확인되면 커스텀 도메인이 **SMS/RCS and Messaging Apps Domains** 페이지의 테이블에 상태 표시기와 함께 나타납니다. 연결된 도메인은 여러 구독 그룹, 워크스페이스, SMS, RCS, WhatsApp 채널에서 즉시 사용할 수 있습니다.

![커스텀 도메인 및 상태 목록.]({% image_buster /assets/img/custom_domain_statuses.png %}){: style="max-width:60%;"}

실시간 모니터링을 통해 활성 도메인에 문제가 발생하면 Braze 대시보드에서 알림을 받아 커스텀 링크를 계속 사용할 수 있습니다. 문제가 발생하면 인앱 오류 세부 정보를 참조하거나 Braze [고객지원]({{site.baseurl}}/braze_support/)에 문의하세요.

## 구독 그룹에 커스텀 도메인 할당 {#assigning-custom-domains-to-subscription-groups}

구성이 완료되면 커스텀 도메인을 하나 또는 여러 SMS, RCS, WhatsApp 구독 그룹에 할당할 수 있습니다.

1. **Audience** > **Subscription Group Management**로 이동합니다.
2. 목록에서 구독 그룹을 찾아 선택합니다.
3. **Subscription Group Details**에서 커스텀 도메인을 **Link Shortening Domain**으로 선택합니다.

![링크 단축 도메인을 선택할 수 있는 구독 그룹 설정.]({% image_buster /assets/img/custom_domain.png %})

링크 단축이 활성화된 상태로 전송된 Campaigns는 SMS, RCS 또는 WhatsApp 구독 그룹에 연결된 할당 도메인을 사용합니다.

!["Message" 상자의 도메인과 다른 단축 링크 도메인이 표시된 SMS 메시지 작성기 미리보기.]({% image_buster /assets/img/custom_domain2.png %})

## 자주 묻는 질문 {#frequently-asked-questions}

### 위임된 도메인을 여러 구독 그룹에서 공유할 수 있나요? {#can-delegated-domains-be-shared-across-multiple-subscription-groups}

네. 단일 도메인을 여러 구독 그룹에서 사용할 수 있습니다. 이를 위해 연결할 각 구독 그룹에 대해 도메인을 선택하세요.

### 위임된 도메인을 여러 워크스페이스에서 공유할 수 있나요? {#can-delegated-domains-be-shared-across-multiple-workspaces}

네. 워크스페이스가 동일한 회사 내에 포함되어 있다면 여러 워크스페이스의 구독 그룹에 도메인을 연결할 수 있습니다.

### 커스텀 도메인을 몇 개까지 추가할 수 있나요? {#how-many-custom-domains-can-i-add}

대시보드당 최대 10개의 커스텀 도메인을 추가할 수 있습니다.

### 45일 이내에 DNS 레코드를 업데이트하지 않으면 어떻게 되나요? {#what-happens-if-i-dont-update-my-dns-records-within-45-days}

Cloudflare DNS 레코드 세부 정보는 45일 후에 만료되지만, 동일한 도메인으로 설정 프로세스를 다시 시작할 수 있으며 Braze가 새 DNS 레코드 세트를 생성하여 설정 기간을 연장합니다.

### DNS 업데이트 과정에서 오류가 발생하면 알림을 받을 수 있나요? {#will-i-be-notified-if-there-is-an-error-during-the-dns-update-process}

네. 오류가 발생하면 Braze 대시보드에 문제 내용과 해결 단계가 포함된 배너가 표시됩니다.

### 여러 채널에서 커스텀 도메인을 사용할 수 있나요? {#can-i-use-a-custom-domain-across-multiple-channels}

네. 커스텀 도메인이 확인되면 대시보드 내 모든 워크스페이스의 모든 SMS, RCS, WhatsApp 구독 그룹에서 사용할 수 있습니다.

### 질문이 있거나 추가 지원이 필요하면 어떻게 하나요? {#what-if-i-have-questions-or-need-further-support}

커스텀 도메인 설정 및 관리에 대한 자세한 안내(문제 해결 단계 및 기술 요구 사항 포함)는 [고객지원에 문의]({{site.baseurl}}/braze_support/)하세요.