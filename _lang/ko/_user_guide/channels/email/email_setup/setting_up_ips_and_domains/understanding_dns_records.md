---
nav_title: DNS 레코드 이해하기
article_title: DNS 레코드 이해하기
page_order: 2
page_type: reference
description: "이 참조 문서에서는 SPF, DKIM, DMARC 및 ESP별 레코드 구조를 포함하여 Braze 이메일 서비스 공급자 전반에서 DNS 레코드가 어떻게 작동하는지 설명합니다."
channel: email
---

# DNS 레코드 이해하기 {#understanding-dns-records}

> 이 참조 문서에서는 세 가지 주요 이메일 서비스 공급자(ESP)인 SparkPost, SendGrid, Amazon Simple Email Service(SES)에서 Braze의 DNS 레코드가 어떻게 작동하는지 설명합니다. 올바른 DNS 구성은 이메일 인증(SPF, DKIM, DMARC)과 브랜드 정렬에 필수적이며, 전달 가능성에 직접적인 영향을 미칩니다.

자세한 내용은 [이메일 인증]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication)을 참조하세요.

## 핵심 이메일 인증 기본 사항 {#core-email-authentication-fundamentals}

공급자별 구조를 살펴보기 전에, 이러한 레코드가 무엇을 하는지 그리고 Braze가 적절한 정렬을 달성하기 위해 어떻게 사용하는지 이해해야 합니다.

### Sender Policy Framework (SPF) {#spf}

SPF는 도메인에 설정하는 DNS 레코드로, 해당 도메인을 대신하여 이메일을 보낼 수 있도록 승인된 IP 주소를 지정합니다.

Braze는 회사의 루트 도메인(예: `example.com`)에서 SPF 레코드를 수정하거나 추가하도록 요청하지 않습니다. 대신 Braze는 `bounce.mail.example.com`과 같은 전용 커스텀 Return-Path 도메인(바운스 도메인, MAIL FROM 도메인 또는 봉투 From 도메인이라고도 함)을 사용하여 전달을 분리합니다.

수신 메일박스 공급자는 표시되는 `From:` 헤더 도메인이 아닌 이 Return-Path 도메인을 기준으로 SPF를 검증하므로, SPF 구성은 전적으로 하위 도메인 수준에서 이루어집니다. 기반 ESP에 따라 Braze는 다음 두 가지 방법 중 하나로 이 검증을 처리합니다:

- CNAME 위임(SendGrid 및 SparkPost): 하위 도메인을 ESP로 다시 가리키는 `CNAME`을 생성합니다. ESP가 자체 인프라에서 SPF 정책을 호스팅하고 업데이트하여 SPF 검사를 자동으로 통과시킵니다.
- 명시적 TXT 레코드(Amazon SES): 바운스 하위 도메인에 명시적 승인 문자열(예: `v=spf1 include:amazonses.com ~all`)이 포함된 하드코딩된 `TXT` 레코드를 직접 게시하여 AWS에 해당 영역에서 메일을 보낼 수 있는 권한을 부여합니다.

### Domain Keys Identified Mail (DKIM) {#dkim}

DKIM은 이메일 헤더에 암호화 디지털 서명을 추가합니다. 수신 서버는 발신자의 공개 키(DNS에 게시됨)를 사용하여 이메일이 도메인 소유자로부터 발송되었으며 전송 중에 변경되지 않았는지 확인합니다.

Braze는 수신 ISP가 ESP에서 생성한 암호화 서명을 검증할 수 있도록 `TXT` 또는 `CNAME` 레코드를 통해 공개 DKIM 키를 게시하도록 요구합니다.

### DMARC 정렬 {#dmarc}

이메일이 DMARC를 통과하려면, 사용자에게 표시되는 `From:` 헤더의 도메인이 SPF(Return-Path) 또는 DKIM에 의해 검증된 도메인과 일치(정렬)해야 합니다. Braze 설정은 SPF와 DKIM 모두를 통해 정렬을 달성하므로, DMARC 정책이 안전하게 충족됩니다.

Braze는 기본적으로 SPF 및 DKIM 인증을 처리하지만, 발신 도메인에 DMARC 레코드를 추가해야 합니다. DMARC는 거의 모든 주요 받은편지함 공급자가 요구하는 필수 인증 도구입니다. 이메일이 합법적임을 증명하고, 도메인 평판을 구축하며, 시간이 지남에 따라 전달 가능성을 건강하게 유지합니다.

이를 위해서는 회사의 도메인 레지스트리에 대한 접근 권한이 필요하므로, 본인 또는 네트워크 관리자가 루트 도메인 수준에서 이 레코드를 추가해야 합니다. 처음 시작하는 경우, `p=none`과 같은 기본 정책이 최소 받은편지함 요구 사항을 충족합니다. DMARC에 대한 자세한 내용은 [DMARC.org](https://dmarc.org/)를 참조하세요. Braze 관련 DMARC 가이드는 [이메일 인증]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication#dmarc)을 참조하세요.

## ESP별 DNS 아키텍처 {#esp-specific-dns-architecture}

ESP 아키텍처마다 DNS 위임을 처리하는 방식이 다릅니다. 환경을 프로비저닝할 때 특정 ESP 클러스터에 매핑된 정확한 레코드를 사용하세요.

### SparkPost 아키텍처 {#sparkpost-architecture}

SparkPost는 하이브리드 설정을 사용합니다. 명시적 `CNAME` 레코드를 사용하여 추적 기술 및 Return-Path 인프라를 SparkPost로 연결하고, DKIM 인증에는 원시 `TXT` 레코드를 사용합니다.

- SPF 및 Return-Path 구성: SparkPost는 반송 처리를 위해 지정된 하위 도메인(예: `mail.example.com`)을 요청합니다. `CNAME` 레코드가 이 하위 도메인을 SparkPost의 인바운드 반송 프로세서로 연결합니다. 이를 통해 반송 트래픽이 올바르게 라우팅되고, SparkPost의 대상 서버가 프로토콜을 관리하므로 SPF가 자동으로 검증됩니다.
- DKIM 구성: SparkPost는 특정 셀렉터에 매핑된 정확한 공개 키 문자열이 포함된 `TXT` 레코드를 필요로 합니다.
- 클릭 및 열람 추적: SparkPost 추적 엔드포인트(또는 SSL 추적이 요청된 경우 CDN 프록시)를 가리키는 `CNAME`으로 추적 하위 도메인을 구성합니다.

#### SparkPost DNS 테이블 예시 {#example-sparkpost-dns-table}

다음 테이블은 SparkPost 설정에 대한 DNS 레코드 예시를 보여줍니다.

| 레코드 유형 | 호스트/이름 | 값/대상 | 용도 |
| --- | --- | --- | --- |
| CNAME | mail.example.com | smtp.sparkpostmail.com | Return-Path / SPF 정렬 |
| TXT | scph1226._domainkey.mail.example.com | v=DKIM1; k=rsa; p=... | 암호화 DKIM 인증 |
| CNAME | click.mail.example.com | spgo.io (또는 CDN 엔드포인트) | 클릭 및 열람 추적 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="SparkPost DNS 테이블 예시" }

### SendGrid 아키텍처 {#sendgrid-architecture}

SendGrid는 도메인 인증이라고 하는 자동화된 인프라를 사용합니다. 원시 `TXT` 키를 제공하는 대신, SendGrid는 SendGrid 관리 서버를 직접 가리키는 일련의 `CNAME` 레코드를 제공합니다.

- SPF 및 Return-Path 구성: SendGrid는 발신 하위 도메인을 `uXXXXXX.wl.sendgrid.net`에 매핑하는 특정 `CNAME`(보통 `em` 접두사 사용)을 사용합니다. SendGrid는 해당 엔드포인트에서 SPF 레코드를 호스팅하고 동적으로 업데이트합니다.
- DKIM 구성: SendGrid는 DKIM용으로 두 개의 별도 `CNAME` 레코드를 생성합니다(보통 `s1` 및 `s2`와 같은 셀렉터 사용). 이 레코드들은 SendGrid의 키를 가리킵니다.
- SendGrid는 두 개의 DKIM `CNAME` 레코드를 제공하여 DNS를 수동으로 업데이트할 필요 없이 암호화 키를 자동으로 교체할 수 있도록 합니다.

#### SendGrid DNS 테이블 예시 {#example-sendgrid-dns-table}

다음 테이블은 SendGrid 설정에 대한 DNS 레코드 예시를 보여줍니다.

| 레코드 유형 | 호스트/이름 | 값/대상 | 용도 |
| --- | --- | --- | --- |
| CNAME | em.mail.example.com | u123456.wl.sendgrid.net | Return-Path / 동적 SPF |
| CNAME | s1._domainkey.mail.example.com | s1.domainkey.u123456.wl.sendgrid.net | 기본 DKIM 키 (교체형) |
| CNAME | s2._domainkey.mail.example.com | s2.domainkey.u123456.wl.sendgrid.net | 보조 DKIM 키 (교체형) |
| CNAME | email.mail.example.com | sendgrid.net (또는 CDN 엔드포인트) | 클릭 및 열람 추적 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="SendGrid DNS 테이블 예시" }

### Amazon SES 아키텍처 {#amazon-ses-architecture}

Amazon SES는 커스텀 반송 추적을 위한 명시적 `MX` 및 `TXT` 라우팅과 함께 `CNAME` 레코드를 사용하는 Easy DKIM을 사용합니다.

- DKIM 구성: Amazon SES는 Easy DKIM을 사용하여 세 개의 `CNAME` 레코드를 제공합니다. 이 레코드들은 공개 키가 포함된 AWS 관리 하위 도메인을 가리킵니다. SES는 보안 규정 준수를 유지하기 위해 이러한 키를 투명하게 자동 교체합니다.
- SPF 및 커스텀 MAIL FROM 구성: SendGrid와 SparkPost는 `CNAME`을 통해 반송 도메인 라우팅을 관리합니다. Amazon SES는 지정된 MAIL FROM 하위 도메인에 직접 배치되는 명시적 `MX` 레코드와 `TXT` 레코드를 필요로 합니다. `MX` 레코드는 반송 알림이 Amazon 서버로 반환되도록 보장하고, `TXT` 레코드에는 승인된 하드코딩된 SPF 문자열이 포함됩니다.

자세한 내용은 [Amazon SES 설정]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses)을 참조하세요.

#### Amazon SES DNS 테이블 예시 {#example-amazon-ses-dns-table}

다음 테이블은 Amazon SES 설정에 대한 DNS 레코드 예시를 보여줍니다.

| 레코드 유형 | 호스트/이름 | 값/대상 | 용도 |
| --- | --- | --- | --- |
| CNAME | sel1._domainkey.mail.example.com | sel1.dkim.amazonses.com | Easy DKIM 키 1 (교체형) |
| CNAME | sel2._domainkey.mail.example.com | sel2.dkim.amazonses.com | Easy DKIM 키 2 (교체형) |
| CNAME | sel3._domainkey.mail.example.com | sel3.dkim.amazonses.com | Easy DKIM 키 3 (교체형) |
| MX | bounce.mail.example.com | 10 feedback-smtp.us-east-1.amazonses.com | 반송 처리를 AWS로 라우팅 |
| TXT | bounce.mail.example.com | v=spf1 include:amazonses.com ~all | 명시적 SPF 승인 |
| CNAME | track.mail.example.com | r.us-east-1.awstrack.me (또는 CDN) | 클릭 및 열람 추적 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Amazon SES DNS 테이블 예시" }

## 고급 DNS 고려 사항 {#advanced-dns-considerations}

### TXT DKIM 레코드 문자열 분할 {#txt-dkim-record-string-splitting}

SparkPost 또는 수동 DKIM 설정을 배포할 때 긴 암호화 키(2048비트 DKIM 키)를 접할 수 있습니다.

핵심 DNS 사양(RFC 1035)은 `TXT` 레코드 내 단일 문자열을 최대 255자로 제한합니다. 2048비트 공개 키는 일반적으로 400자를 초과하므로, 도메인 레지스트리에서 단일 문자열을 거부하거나 잘라내어 서명이 무효화될 수 있습니다.

문자열 분할은 이 문제를 해결합니다. 문자열을 255자 미만의 청크로 나누세요. 동일한 `TXT` 레코드 내에서 각 청크를 직선 따옴표로 감싸고 공백으로 구분합니다.

{% alert note %}
Cloudflare나 AWS Route 53과 같은 DNS 공급자를 사용하면, 긴 문자열을 붙여넣을 때 이러한 인터페이스가 자동으로 분할을 처리합니다. 레거시 시스템(예: GoDaddy 또는 Network Solutions)에서는 큰따옴표 기법을 사용하여 수동으로 분할 형식을 지정해야 합니다.
{% endalert %}

### 전용 하위 도메인 사용 {#dedicated-subdomains}

온보딩 중 흔히 발생하는 실수는 최상위 조직 도메인(예: `example.com`)을 Braze에서 발신 도메인으로 직접 사용하도록 요청하는 것입니다. Braze는 전용 하위 도메인(예: `mail.example.com` 또는 `engage.example.com`)을 사용해야 합니다.

상위 도메인을 사용하면 다음과 같은 방식으로 기업 인프라에 문제가 발생할 수 있습니다.

#### MX 레코드 충돌 {#mx-record-conflicts}

도메인은 하나의 기본 라우팅 `MX` 레코드 세트만 지원할 수 있습니다. 상위 도메인(`example.com`)을 Braze의 ESP 인프라에 매핑하면, 반송 처리에 필요한 커스텀 `MX` 레코드가 기업 이메일 레코드를 덮어씁니다. 이로 인해 Google Workspace나 Microsoft 365와 같은 기업 내부 메시징 플랫폼이 중단될 수 있습니다.

#### SPF include 비대화 및 10회 조회 제한 {#spf-include-bloat-and-the-10-lookup-limit}

SPF 사양(RFC 7208)은 수신 메일 서버가 SPF 레코드를 검증할 때 최대 10회의 DNS 조회로 제한합니다.

- 상위 도메인에 Braze의 ESP 메커니즘(`include:sparkpostmail.com` 또는 `include:amazonses.com`)을 추가하면, 해당 제한에 크게 영향을 미칩니다.
- 제한을 초과하면 영구적인 SPF PermError가 트리거되어 모든 기업 이메일의 인증이 실패합니다.

#### IP 및 도메인 평판 격리 {#ip-and-domain-reputation-isolation}

마케팅 Campaigns, 트랜잭션 영수증, 내부 직원 이메일이 동일한 루트 도메인 공간을 공유하면, 마케팅 스팸 불만이 급증할 경우 상위 도메인의 평판이 손상될 수 있습니다. 이로 인해 중요한 기업 커뮤니케이션이 스팸 폴더로 분류될 위험이 있습니다. 별도의 하위 도메인을 사용하면 마케팅 발신의 평판을 격리할 수 있습니다.

## 구현 워크플로 {#implementation-workflow}

원활한 인수인계와 구현을 위해 다음 순서를 따르세요:

1. 구조화된 레코드를 IT 또는 네트워크 관리자에게 제공하여 호스팅 플랫폼(Cloudflare, Route 53 등)에 추가하도록 합니다.
2. 초기 테스트를 위해 TTL(Time-To-Live) 값을 낮게 설정합니다(예: 300초 또는 5분). 이렇게 하면 입력 중 오타가 발생했을 때 빠르게 복구할 수 있습니다.
3. DNS 조회(예: `dig CNAME mail.example.com`)를 실행하거나 유효성 검사 도구를 사용하여 레코드가 올바르게 확인되는지 검증한 후 워밍 단계로 진행합니다.

## DNS 공급자 설명서 {#dns-provider-documentation}

모든 DNS 공급자는 고유한 인터페이스를 가지고 있습니다. 이러한 사양을 네트워크 관리자와 공유하거나 특정 공급자의 설명서를 참조하여 존 파일에 항목을 올바르게 매핑하세요.

다음 표에는 일반적으로 사용되는 DNS 공급자의 공식 설명서가 나열되어 있습니다.

| DNS 공급자 | 리소스 |
| --- | --- |
| Cloudflare | [DNS 레코드 관리](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) |
| Amazon Route 53 | [리소스 레코드 세트 생성](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) |
| GoDaddy | [DNS 레코드 관리](https://www.godaddy.com/help/manage-dns-records-680) |
| Google Cloud DNS | [도메인 이름에 대한 DNS 레코드 설정](https://cloud.google.com/dns/docs/set-up-dns-records-domain-name) |
| Microsoft Azure DNS | [Azure 포털을 사용하여 DNS 레코드 관리](https://learn.microsoft.com/en-us/azure/dns/dns-operations-recordsets-portal) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="DNS 공급자 설명서" }

추가 도메인 공급자 리소스는 [IP 및 도메인 설정]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains#step-2-add-and-verify-a-sending-domain)을 참조하세요.