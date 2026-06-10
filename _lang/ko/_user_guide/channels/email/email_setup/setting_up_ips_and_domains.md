---
nav_title: IP 주소 및 도메인 설정
article_title: IP 및 도메인 설정
page_order: 0
page_type: tutorial
channel: email
description: "이 도움말 문서에서는 Braze를 통해 이메일을 보내기 위한 IP와 도메인을 설정하는 방법을 안내합니다."

---

# IP 주소 및 도메인 설정 {#set-up-ips-and-domains}

> 이 문서에서는 Braze로 이메일을 보내기 전에 필요한 IP 주소와 풀, 그리고 도메인과 하위 도메인을 설정하는 데 필요한 요구 사항과 단계를 안내합니다.

{% multi_lang_include video.html id="iTm3yQkJ0UU" align="right"  %}

<br>

{% alert important %}
이메일 서비스 공급자(ESP) 파트너로 SendGrid, SparkPost 또는 Amazon Simple Email Service(SES)를 사용할 수 있습니다. 2026년부터 Braze는 새로운 이메일 설정에 대해 Amazon SES를 기본 ESP로 사용합니다. 자세한 내용은 [Amazon SES 설정]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses/)을 참조하세요.
{% endalert %}

## 방법 1: Braze와 조정(권장) {#method-1-coordinate-with-braze-recommended}

### 1단계: 정보 정리 {#step-1-outline-information}

다음 정보를 Braze 담당자에게 보내주세요:

* 선택한 도메인 및 하위 도메인
* 매월 발송할 대략적인 이메일 수(필요한 IP 수를 결정하는 데 도움이 됩니다)
* 발송 도메인을 할당된 IP에 매핑하는 방법에 대한 선호 사항

### 2단계: Braze에서 정보 구성 {#step-2-braze-configures-information}

이메일을 받은 후 IP, 도메인 및 하위 도메인, IP 풀을 구성하는 작업을 시작합니다.

### 3단계: DNS 레코드 추가 {#step-3-add-dns-records}

IP, 도메인, 하위 도메인 및 IP 풀이 구성되면 DNS 레코드 목록을 보내드립니다. 엔지니어와 개발자에게 필요한 곳에 이러한 DNS 레코드를 추가하도록 요청하고, 추가가 완료되면 Braze 온보딩 팀에 알려주세요.

{% multi_lang_include dns_records.md %}

Braze에서 DNS 레코드를 제공한 후, 귀사의 DNS 또는 IT 팀이 가능한 한 빨리 추가하세요. 도메인 검증은 시간 제한이 있으며, 레코드를 너무 늦게 추가하면 DNS 레코드가 나중에 올바르게 해석되더라도 검증이 실패할 수 있습니다. DNS 레코드가 올바르게 표시되지만 검증이 실패하는 경우, Braze 온보딩 또는 고객지원 팀에 문의하여 검증 절차를 다시 시작하세요.

### 다음 단계 {#next-steps}

설정을 확인하고 내부 시스템에서 모든 정보를 검증합니다. 준비가 완료되면 Braze 온보딩 팀에서 알려드리며, DNS 레코드에 엔지니어링 팀과 함께 해결해야 하는 문제가 있는 경우에도 알려드립니다.

## 방법 2: 셀프 서비스 이메일 설정 {#method-2-self-service-email-setup}

이 방법은 회사에 대해 하나의 발송 도메인, 하나의 추적 도메인 및 총 하나의 IP를 설정합니다. 더 많은 설정을 계획하고 있다면 Braze 온보딩 팀에 문의하세요(방법 1).

{% multi_lang_include early_access_beta_alert.md feature='This self-service email setup feature' type='beta' %}
<br>셀프 서비스 이메일 설정 기능을 사용하는 경우 Braze 온보딩 팀과도 반드시 상담하세요.

### 필수 조건 {#prerequisites}

셀프 서비스 이메일 설정을 사용하려면 다음 필수 조건을 충족해야 합니다:

1. 온보딩 중인 신규 고객이어야 합니다.
2. "회사 설정 관리" 회사 수준 권한을 보유하고 있어야 합니다.

### 1단계: 설정 시작 {#step-1-begin-setup}

1. **설정** > **회사 설정** 아래의 **관리자 설정**으로 이동합니다.
2. 다음으로 **발송자 확인** 탭을 선택합니다. 이 탭을 보려면 "회사 설정 관리" 회사 수준 권한이 있어야 합니다.
3. **설정 시작**을 선택합니다.

### 2단계: 발송 도메인 추가 및 확인 {#step-2-add-and-verify-a-sending-domain}

발송 도메인은 이메일 발송 시 "보낸 사람" 주소에 사용됩니다. 발송 도메인을 입력하고 **제출**을 클릭합니다.

다음으로, 페이지 하단의 TXT 및 CNAME 레코드를 DNS 공급자에 추가합니다. 그런 다음 Braze 대시보드로 돌아가서 **확인**을 클릭합니다.

![]({% image_buster /assets/img_archive/email_setup_rdns_records.png %})

검증이 실패하고 DNS 레코드가 올바르다고 판단되는 경우, Braze 고객지원에 도움을 요청하세요.

{% alert important %}
발송 도메인은 소유한 도메인의 하위 도메인이어야 합니다. 예를 들어, "example.com"을 소유하고 있다면 하위 도메인은 "mail.example.com"이 될 수 있으며, 이를 통해 발송 주소 "@mail.example.com"을 사용할 수 있습니다.
{% endalert %}

### 3단계: 추적 도메인 추가 및 확인 {#step-3-add-and-verify-a-tracking-domain}

추적 도메인은 클릭 추적 및 브랜딩 목적으로 이메일의 링크를 래핑하는 데 사용됩니다. 사용자가 이메일 링크 위에 마우스를 올리거나 클릭할 때 이 도메인이 표시됩니다. 발송 도메인과 일치시키는 것을 권장합니다.

1. 추적 도메인을 입력하고 **제출**을 선택합니다.
2. 다음으로, 페이지 하단의 CNAME 레코드를 DNS 공급자에 추가합니다.
3. 그런 다음 Braze 대시보드로 돌아가서 **확인**을 선택합니다.

### 4단계: IP 주소 추가 {#step-4-add-an-ip-address}

Braze는 역방향 DNS(rDNS)라는 설정에서 IP 주소를 발송 하위 도메인과 연결하기 위한 A 레코드를 생성합니다. DNS 공급자에 A 레코드를 추가한 다음 **rDNS 설정**을 클릭하여 전달 가능성을 지원합니다.

추가된 도메인은 **발송자 확인** 섹션에 표시되지 않습니다. 더 많은 도메인을 추가하려면 Braze 고객지원 팀에 문의하세요.

### 전용 IP가 두 개 이상인 IP 풀 {#ip-pools-with-more-than-one-dedicated-ip}

IP 풀에 전용 IP 주소가 여러 개 포함된 경우, Braze와 이메일 서비스 공급자는 용량 및 전달 가능성을 위해 대량 발송을 해당 IP들에 분산합니다. 분산은 대략적이며, Campaign의 모든 메시지가 모든 IP를 사용하는 것은 아니고, 소규모 발송의 경우 IP 간 분배가 고르지 않을 수 있습니다. SendGrid는 일반적으로 메일을 청크 단위(대략 청크당 약 1,500개 메시지)로 처리하므로, 볼륨이 항상 IP 간에 정확히 1:1 비율로 분할되지는 않습니다. 일상적으로 매우 높은 일일 볼륨을 발송하는 경우, Braze 온보딩 또는 고객 성공 담당자와 풀 크기에 대해 논의하세요.

### 다음 단계

발송자 확인이 완료되면, 메시지가 지속적으로 높은 비율로 대상 받은편지함에 도달할 수 있도록 IP 워밍을 권장합니다. 이 설정을 완료한 후, Braze 온보딩 팀과 상담하여 도메인과 [IP 주소]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/)가 정상적으로 작동하는지 확인하세요.