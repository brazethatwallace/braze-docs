---
nav_title: IP 주소 및 도메인 설정
article_title: IP 주소 및 도메인 설정
page_order: 0
page_type: tutorial
channel: email
description: "이 도움말 문서에서는 Braze를 통해 이메일을 보내기 위한 IP 주소, IP 풀, 도메인 및 하위 도메인을 설정하는 방법을 안내합니다."
---

# IP 주소 및 도메인 설정 {#set-up-ips-and-domains}

> 이 문서에서는 Braze로 이메일을 보내기 전에 필요한 IP 주소와 풀, 그리고 도메인과 하위 도메인을 설정하는 데 필요한 요구 사항과 단계를 안내합니다.

{% multi_lang_include video.html id="iTm3yQkJ0UU" align="right"  %}

<br>

{% alert important %}
2026년부터 Braze는 새로운 이메일 설정에 대해 Amazon Simple Email Service(SES)를 기본 이메일 서비스 공급자(ESP)로 사용합니다. 자세한 내용은 [Amazon SES 설정]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses)을 참조하세요.
{% endalert %}

## 방법 1: 셀프서비스 이메일 설정 {#method-1-self-service-email-setup}

이 방법은 회사의 발신 도메인과 추적 도메인을 설정합니다. 먼저 Braze 온보딩 팀과 상의하고, IP 풀 및 IP 주소를 추가하기 위해 다음 정보를 Braze 담당자에게 전달해야 합니다:

- 선택한 도메인 및 하위 도메인
- 월별 대략적인 이메일 발송량(필요한 IP 수를 결정하는 데 도움이 됩니다)
- 발신 도메인을 할당된 IP 풀에 매핑하는 방식에 대한 선호도

### 전제 조건 {#prerequisites}

셀프서비스 이메일 설정을 사용하려면 다음 전제 조건을 충족하는지 확인하세요:

- 온보딩 중인 신규 고객이어야 합니다.
- "Edit Domain Settings" 회사 수준 권한이 있어야 합니다.

### 1단계: 설정 시작 {#step-1-begin-setup}

1. **Settings** > **Company Settings** 아래의 **Email Self Serve**로 이동합니다.
2. **Start setup**을 선택합니다.

### 2단계: 발신 도메인 추가 및 인증 {#step-2-add-and-verify-a-sending-domain}

발신 도메인은 이메일을 보낼 때 "from" 주소에 사용됩니다.

1. 발신 도메인을 입력하고 **Submit**을 선택합니다.
2. 페이지 하단의 TXT 및 CNAME 레코드를 DNS 공급자에 추가합니다.

![도메인 관리 시스템에 복사할 TXT 및 CNAME 레코드를 보여주는 DNS 레코드 섹션.]({% image_buster /assets/img/email_setup/dns_records.png %})

{: start="3"}
3. Braze 대시보드로 돌아가서 **Verify**를 선택합니다.

엔지니어와 개발자에게 필요한 곳에 이러한 DNS 레코드를 추가하도록 요청하세요. SPF, DKIM, DMARC 및 ESP별 레코드 구조를 포함하여 Braze 이메일 서비스 공급자 전반에서 DNS 레코드가 어떻게 작동하는지에 대한 자세한 설명은 [DNS 레코드 이해하기]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/understanding_dns_records)를 참조하세요.

{% multi_lang_include channels/email/dns_records.md %}

인증에 실패하고 DNS 레코드가 올바르다고 생각되면 Braze 지원팀에 문의하여 도움을 받으세요.

{% alert important %}
발신 도메인은 소유한 도메인의 하위 도메인이어야 합니다. 예를 들어, "example.com"을 소유하고 있다면 하위 도메인은 "mail.example.com"이 될 수 있으며, 이를 통해 발신 주소 "@mail.example.com"을 사용할 수 있습니다.
{% endalert %}

### 3단계: 추적 도메인 추가 및 인증 {#step-3-add-and-verify-a-tracking-domain}

추적 도메인은 클릭 추적 및 브랜딩 목적으로 이메일의 링크를 래핑하는 데 사용됩니다. 수신자가 이메일 링크 위에 마우스를 올리거나 클릭할 때 이 도메인이 표시됩니다. Braze는 이를 발신 도메인과 일치시키는 것을 권장합니다.

1. 추적 도메인을 입력하고 **Submit**을 선택합니다.
2. 페이지 하단의 CNAME 레코드를 DNS 공급자에 추가합니다.
3. Braze 대시보드로 돌아가서 **Verify**를 선택합니다.

### 4단계: IP 주소 추가 {#step-4-add-an-ip-address}

Braze는 역방향 DNS(rDNS)라는 설정에서 IP 주소를 발신 하위 도메인에 연결하기 위한 A 레코드를 생성합니다. DNS 공급자에 A 레코드를 추가한 다음 **Set up rDNS**를 선택하여 전달 가능성을 지원합니다.

IP 풀의 IP 주소를 추가하거나 수정하려면 Braze 지원팀에 문의하세요.

#### 전용 IP가 두 개 이상인 IP 풀 {#ip-pools-with-more-than-one-dedicated-ip}

IP 풀에 여러 전용 IP 주소가 포함된 경우, Braze와 이메일 서비스 공급자는 용량과 전달 가능성을 위해 대량 발송을 해당 IP들에 분산합니다. 분산은 대략적이며, Campaign의 모든 메시지가 모든 IP를 사용하는 것은 아니고 소규모 발송은 주소 간에 불균등하게 보일 수 있습니다. SendGrid는 종종 메일을 청크 단위(대략 청크당 약 1,500개 메시지)로 처리하므로 볼륨이 항상 IP 간에 엄격한 일대일 비율로 분할되지는 않습니다. 일상적으로 매우 높은 일일 볼륨을 발송하는 경우, Braze 온보딩 또는 고객 성공 담당자와 풀 크기에 대해 논의하세요.

### 다음 단계 {#next-steps}

발신자 인증이 완료되면, 메시지가 지속적으로 높은 비율로 수신자의 받은편지함에 도달할 수 있도록 Braze는 IP 워밍을 권장합니다.

{% article_tiles %}
- name: 자동 IP 워밍
  link: /docs/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming
- name: IP 워밍
  link: /docs/user_guide/channels/email/email_setup/ip_warming
{% endarticle_tiles %}

이 설정을 완료한 후, Braze 온보딩 팀과 상의하여 도메인 및 IP 워밍이 정상적으로 작동하는지 확인하세요.

## 방법 2: 인증된 도메인 {#method-2-verified-domains}

인증된 도메인을 사용하면 특정 하위 도메인에 대한 제어 권한을 Braze에 부여하여 이메일 설정 및 HTTPS 클릭 추적을 자동화할 수 있습니다. DNS 도메인 위임을 통해 Braze는 이메일 발송 및 클릭 추적에 필요한 DNS 레코드를 관리합니다. 예를 들어, 하위 도메인이 "mail.example.com"인 경우 이를 Braze에 위임하여 발송 및 추적 도메인을 설정할 수 있습니다.

{% alert important %}
인증된 도메인은 현재 Amazon SES만 지원합니다. SendGrid 또는 SparkPost를 사용하는 경우 이 기능을 사용할 수 없습니다.<br><br>인증된 도메인은 이메일에서만 지원됩니다. {% multi_lang_include product_feedback_cta.md context="gap" feature="verified domains for channels other than email" %}
{% endalert %}

### 설정 {#setup}

#### 1단계: Braze와 조율 {#step-1-coordinate-with-braze}

다음 정보를 Braze 담당자에게 보내세요:

- 선택한 도메인 및 하위 도메인
- 도메인을 IP 풀에 매핑하는 방식에 대한 선호 사항
- 각 하위 도메인에서 매월 발송할 예상 이메일 수(IP 풀에 필요한 IP 수를 결정하는 데 도움이 됩니다)
- 사전에 알려야 할 전달 가능성 관련 우려 사항

#### 2단계: Braze에서 정보 구성 {#step-2-braze-configures-information}

이메일을 수신한 후 Braze는 예상 IP 수와 IP 풀을 추가합니다. IP 풀과 IP 주소가 추가된 후 [인증된 도메인]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/verified_domains)의 단계를 따르세요.