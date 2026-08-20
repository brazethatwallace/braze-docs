---
nav_title: 인증된 도메인
article_title: 인증된 도메인
page_order: 0
page_type: tutorial
channel: email
description: "이 사용 방법 문서에서는 Braze가 이메일 발송 및 HTTPS 클릭 추적을 위한 DNS를 관리할 수 있도록 인증된 도메인을 설정하는 방법을 다룹니다."
toc_headers: h2
---

# 인증된 도메인 {#verified-domains}

> 인증된 도메인을 사용하면 특정 하위 도메인에 대한 제어 권한을 Braze에 부여하여 이메일 설정 및 HTTPS 추적을 자동화할 수 있습니다. DNS 도메인 위임을 통해 Braze는 이메일 발송 및 클릭 추적에 필요한 DNS 레코드를 관리합니다. 예를 들어, 하위 도메인이 "mail.example.com"인 경우 이를 Braze에 위임하여 발송 및 추적 도메인을 설정할 수 있습니다.

{% alert important %}
인증된 도메인은 현재 Amazon SES만 지원합니다. SendGrid 또는 SparkPost를 사용하는 경우 이 기능을 사용할 수 없습니다.<br><br>인증된 도메인은 이메일에서만 지원됩니다. {% multi_lang_include product_feedback_cta.md context="gap" feature="verified domains for channels other than email" %}
{% endalert %}

## 이점 {#benefits}

- 더 빠른 온보딩: 이러한 단계를 자동화하면 이메일 온보딩 시간이 단축됩니다.
- 조율 감소: 더 이상 도메인 구성 작업을 위해 Braze 지원팀과 협력할 필요가 없으므로 완전한 셀프 서비스 경험에 가까워집니다.
- 자동화된 SSL 관리: Braze가 SSL 인증서 생성 및 갱신을 처리하여 일반적인 장애 지점과 수동 오버헤드를 제거합니다. SSL로 링크를 보호하는 것은 표준 모범 사례입니다. 수신자는 보안된 링크를 더 신뢰할 가능성이 높으며, 추가 인증 계층이 데이터를 보호하는 데 도움이 됩니다.
- 구성 오류 감소: 가이드 온보딩 흐름과 자동화된 유효성 검사가 오류가 발생하기 쉬운 수동 DNS 설정을 대체하므로 레코드를 잘못 구성하여 이메일 설정을 중단할 가능성이 줄어듭니다.
- 사전 모니터링: Braze는 DNS 레코드를 모니터링하고 문제를 감지하면 알려주므로 장애가 표면화될 때까지 기다릴 필요가 없습니다.

## 고려 사항 {#considerations}

시작하기 전에 다음 사항을 염두에 두세요.

- 전용 하위 도메인을 선택하세요. 도메인 위임을 완료하면 Braze가 해당 하위 도메인의 모든 DNS 레코드를 관리합니다. Braze는 브랜드의 상위 도메인이 아닌 하위 도메인을 위임할 것을 권장합니다. 상위 도메인을 위임하면 해당 도메인에 대한 가시성과 제어 권한을 잃게 되기 때문입니다. 상위 도메인을 사용하려면 다른 곳에서 사용되지 않는 도메인을 사용하세요.
- Braze가 SPF, DKIM, HTTPS 추적 등 하위 도메인의 DNS 레코드를 관리할 수 있도록 NS(네임서버) 위임이 필요합니다. 이를 통해 각 레코드를 수동으로 구성할 필요가 없습니다.

{% alert note %}
CNAME 위임은 지원되지 않습니다. {% multi_lang_include product_feedback_cta.md context="gap" feature="CNAME delegation for verified domains" %}
{% endalert %}

- 최소 3단계 발송 하위 도메인을 계획하세요. Braze는 위임된 도메인 아래에 하위 도메인을 생성하므로(예: "mail.example.com") 발송 도메인은 최소 3단계 깊이여야 합니다. 예를 들어 "e.mail.example.com"입니다.
- Braze가 DNS 레코드를 관리합니다. 위임이 완료되면 Braze가 위임된 하위 도메인의 DNS 레코드를 관리합니다. 이러한 레코드를 직접 수정하지 마세요. 이메일 발송에 문제가 발생할 수 있습니다.
- 인증된 도메인을 설정하려면 "도메인 설정 편집" 권한이 필요합니다.

## 1단계: 인증된 도메인 추가 {#step-1-add-the-verified-domain}

1. **설정** > **인증된 도메인** > **인증된 도메인 추가**로 이동합니다.
2. 하위 도메인과 루트 이름을 입력합니다. 예를 들어, 하위 도메인 "mail.example.com"을 Braze에 위임하는 경우 루트 이름은 "example.com"이고 하위 도메인은 "mail"입니다.
3. 선택한 하위 도메인이 다른 곳에서 사용되지 않으며 충돌하는 DNS 레코드가 없는지 확인합니다.
4. **추가**를 선택하여 TXT 및 NS 레코드를 받습니다.

## 2단계: DNS 레코드 구성 {#step-2-configure-dns-records}

인증된 도메인을 제출하면 Braze가 DNS 공급자에 추가해야 하는 필수 DNS 레코드를 생성합니다. 이 단계에서는 IT 또는 DNS 팀과 조율이 필요할 수 있습니다. 레코드가 만료되기 전에 인증을 완료할 수 있는 기간은 30일입니다. 그 이후에는 설정을 다시 진행해야 합니다.

{% alert tip %}
`dig` 명령을 사용하여 4개의 NS 레코드가 모두 명시적으로 존재하는지 확인하고, 설정이 완료된 것으로 간주하기 전에 대시보드에서 도메인이 유효성 검사를 통과하는지 확인하세요. DNS 인증은 30일 후에 만료됩니다.
{% endalert %}

## 3단계: 도메인 인증 {#step-3-verify-the-domain}

DNS 레코드가 전파된 후 Braze는 24시간 이내에 레코드가 존재하고 올바르게 구성되었는지 확인합니다. 인증이 성공하면 다음과 같이 됩니다.

- 도메인 상태가 **인증됨**으로 업데이트됩니다.
- Braze가 도메인이 준비되었음을 알리는 이메일을 보냅니다.
- 도메인이 **인증된 도메인** 목록에 활성 상태로 표시됩니다.

하위 도메인이 성공적으로 위임된 후 **커스텀 도메인 추가**로 이동하여 발송 및 추적 도메인과 같은 이메일 도메인을 생성합니다. 그러면 설정을 완료하기 위해 **발신자 인증** 페이지로 이동합니다. 자세한 단계는 [이메일 셀프 서비스]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/email_self_serve)를 참조하세요.