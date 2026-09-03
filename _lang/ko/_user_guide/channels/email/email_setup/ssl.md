---
nav_title: Braze의 SSL
article_title: Braze의 SSL
page_order: 5
page_type: reference
description: "이 참조 문서에서는 SSL의 정의, 용도, 그리고 Braze에서의 사용 방법에 대해 다룹니다."
channel: email
---

# Braze의 SSL {#ssl-at-braze}

> 보안 소켓 계층(SSL)은 HTTP 대신 HTTPS로 URL을 암호화합니다. HTTPS는 유효하고 신뢰할 수 있는 SSL 또는 TLS 인증서가 존재하며 해당 웹사이트를 안전하게 방문할 수 있음을 나타냅니다.

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

## SSL이 중요한 이유는 무엇인가요? {#why-is-ssl-important}

대부분의 도메인은 SSL을 필요로 하지 않지만, Braze는 다음과 같은 이유로 SSL 사용을 강력히 권장합니다.

SSL로 웹사이트와 링크를 보호하는 것은 민감한 고객 정보를 직접 다루지 않는 회사에서도 일반적인 관행입니다. 사용자는 SSL로 보호된 링크를 더 신뢰하며, 추가적인 인증 계층이 데이터를 보호하는 데 도움이 됩니다.

### 클릭 및 열람 추적에 필수 {#necessary-for-click-and-open-tracking}

Braze는 클릭과 열람을 추적하기 위해 브랜드 링크 추적 하위 도메인을 사용하여 링크를 변환합니다. 기본적으로 이러한 링크는 HTTP로 시작합니다. 보안되지 않은 트래픽을 제한하는 브라우저 또는 확장 프로그램을 사용하는 사용자는 목적지 URL이 보안 연결이더라도 리다이렉트를 통과하는 데 어려움을 겪을 수 있습니다. 이로 인해 이미지가 깨지거나 추적이 부정확해질 수 있습니다. 링크 추적 하위 도메인에 SSL을 적용하여 안전한 리다이렉트를 보장하세요.

## 요구 사항 {#requirements}

### 브라우저 {#browser}

Google Chrome과 같은 주요 브라우저는 사용자를 보호하기 위해 비보안 URL을 통한 트래픽을 제한합니다. SSL을 사용하면 콘텐츠가 신뢰할 수 있는 것임을 확인하고, 이메일에서 깨진 링크나 이미지와 같은 문제를 최소화하는 데 도움이 됩니다.

### HSTS 도메인 {#hsts-domains}

HTTP Strict Transport Security(HSTS) 도메인을 사용하는 경우, SSL을 설정하고 필수 보안 인증서를 전송하도록 CDN을 구성하세요. SSL이 없으면 이미지 및 웹 링크가 깨집니다.

## SSL 인증서 획득하기 {#acquire-an-ssl-certificate}

서드파티(보통 CDN(콘텐츠 전송 네트워크))를 통해 SSL 인증서를 획득하세요. CDN은 인증서를 호스팅하고, 사용자가 링크를 클릭할 때 트래픽을 CDN을 통해 리디렉션하여 인증서를 적용한 후 SendGrid 또는 SparkPost로 전송함으로써 브라우저에 인증서를 제공합니다.

SSL 설정을 시작하려면 Braze 고객 성공 매니저에게 연락하여 전체 Braze 이메일 설정을 요청하세요.

Braze에서 설정을 시작한 후 다음 단계를 따르세요:

1. Braze가 도메인 레지스트리에 추가할 DNS 레코드를 제공합니다.
2. Braze가 레코드가 레지스트리에 올바르게 추가되었는지 확인합니다.
3. 확인이 완료되면 CDN을 선택하고 서드파티 공급자로부터 SSL 인증서를 획득합니다.
4. 이 시점에서 CDN을 설정합니다. Braze는 CDN 구성에 대한 문제 해결을 지원할 수 없습니다. 추가 지원이 필요한 경우 CDN 공급자에게 문의하세요.
5. 고객 성공 매니저에게 연락하여 SSL을 활성화하세요.

## CDN이란 무엇이며, 왜 필요한가요? {#what-is-a-cdn-and-why-do-i-need-it}

콘텐츠 전송 네트워크(CDN)는 다양한 매체에서 콘텐츠의 빠른 로드 시간을 보장하는 동시에 보안 인증서를 처리하는 서버 플랫폼입니다.

{% alert important %}
CDN 구성은 항상 Braze에서 DNS 레코드 검증이 완료된 후에 진행합니다. 아직 이 단계를 시작하지 않았다면, 고객 성공 매니저에게 문의하여 시작하는 방법에 대한 자세한 정보를 확인하세요.
{% endalert %}

클릭 및 열람 추적 기술을 위해 전송 파트너는 브랜드 서브도메인을 사용하여 링크를 변환하고, CDN은 변환된 링크에 SSL 인증서를 적용합니다. 파트너는 링크와 이미지가 올바르게 표시되려면 수신자의 브라우저에 유효한 인증서를 제시해야 하는 경우가 많습니다. Braze는 인증서를 요청하거나 관리하지 않으므로, CDN을 통해 직접 설정해야 합니다.

{% alert note %}
SSL 클릭 및 열람 추적 기술에 나열된 CDN을 사용할 수 없거나 사용하고 싶지 않은 경우, 커스텀 SSL 구성을 설정할 수 있습니다. 대체 CDN이나 커스텀 프록시를 사용하면 설정이 더 복잡해질 수 있습니다. [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) 및 [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) 설명서를 참조하세요.
{% endalert %}

### 추가 리소스 {#additional-resources}

{% alert important %}
CDN 구성 문제 해결은 CDN 공급자에게 문의하거나 일반적인 안내는 [문제 해결]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting)을 참조하세요.
{% endalert %}

특정 CDN을 구성하는 방법에 대한 ESP 파트너별 리소스를 참조하세요. 사용 중인 특정 CDN이 목록에 없을 수 있지만, CDN이 SSL 인증서를 적용할 수 있는 기능을 갖추고 있는지 확인해야 합니다.

CDN의 클릭 추적 기술 도메인을 구성할 때, 호스트 헤더 공격과 같은 잠재적 보안 문제를 방지하기 위해 `X-Forwarded-Host` 헤더를 활성화하세요. 단계별 안내는 CDN 설명서 또는 지원 팀에 문의하세요.

| 파트너 | CDN | 설명서 |
| --- | --- | --- |
| Amazon SES | AWS CloudFront | [CloudFront에서 HTTPS 사용](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) |
| Amazon SES | CloudFlare | [SSL/TLS 시작하기](https://developers.cloudflare.com/ssl/get-started/) |
| Amazon SES | Fastly | [Fastly 관리 인증서로 TLS 설정](https://www.fastly.com/documentation/guides/getting-started/domains/securing-domains/setting-up-tls-with-certificates-fastly-manages/) |
| Amazon SES | KeyCDN | [커스텀 SSL 설정 방법](https://www.keycdn.com/support/how-to-setup-custom-ssl) |
| Amazon SES | Google Cloud | [Google 관리 SSL 인증서](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) |
| SendGrid | AWS CloudFront | [CloudFront를 사용한 클릭 추적용 SSL 구성 방법](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront) |
| SendGrid | CloudFlare | [CloudFlare 사용](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare) |
| SendGrid | Fastly | [Fastly 사용](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly) |
| SendGrid | KeyCDN | [KeyCDN 사용](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) |
| SparkPost | AWS CloudFront | [AWS CloudFront 단계별 가이드](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-aws-cloudfront) |
| SparkPost | CloudFlare | [Cloudflare 단계별 가이드](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-cloudflare) |
| SparkPost | Fastly | [Fastly 단계별 가이드](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-fastly) |
| SparkPost | Google Cloud Platform | [Google Cloud Platform 단계별 가이드](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-google-cloud-platform) |
| SparkPost | Microsoft Azure | [Microsoft Azure 단계별 가이드](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="추가 리소스" }

### Amazon SES

Amazon SES를 ESP로 사용하는 경우, [Amazon SES 설명서](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html)의 **Option 2: Configuring an HTTPS domain**을 참조하고, Braze 클러스터에 따라 리전별 AWS 추적 기술 도메인을 지정하세요.

- **Braze US 클러스터:** `r.us-east-1.awstrack.me`
- **Braze EU 클러스터:** `r.eu-central-1.awstrack.me`

{% alert important %}
CDN의 클릭 추적 기술 도메인을 구성할 때, 호스트 헤더 공격과 같은 잠재적 보안 문제를 방지하기 위해 `X-Forwarded-Host` 헤더를 활성화하세요. 단계별 안내는 CDN 공급자에게 문의하세요.
{% endalert %}

## 클릭 및 열람 추적 URL 패턴 {#click-and-open-tracking-url-patterns}

이메일 서비스 공급자(ESP)는 추적되는 각 링크를 클릭 추적 도메인을 가리키도록 재작성한 다음, 해당 요청이 추적 클릭인지 열람인지를 표시하는 경로 접두사를 추가합니다. Braze는 이러한 경로를 생성하지 않습니다. ESP가 링크를 재작성할 때 경로를 추가합니다. CDN 또는 프록시 규칙, 보안 허용 목록, 모바일 앱 링크 처리에 대해서는 ESP의 설명서를 신뢰할 수 있는 출처로 사용하세요.

| ESP | 경로 패턴 | ESP 설명서 |
| --- | --- | --- |
| SendGrid | 추적 클릭의 경우 `/wf/click?upn=...`, 유니버설 링크로 플래그한 링크의 경우 `/uni/wf/click?upn=...`입니다. 구성에 따라 브랜드 링크에서 `/ls/click`(장문 서명) 또는 `/ss/`(단축)를 사용할 수도 있습니다. | [유니버설 링크](https://www.twilio.com/docs/sendgrid/ui/sending-email/universal-links) 및 [단축 링크](https://support.sendgrid.com/hc/en-us/articles/44375837088795-How-to-Know-if-my-Links-Are-Shortened-by-SendGrid) |
| SparkPost | 추적 클릭의 경우 `/f/`, 추적 열람의 경우 `/q/`입니다. `data-msys-sublink` 커스텀 경로를 설정한 링크는 `/f/{custom_path}/` 형식을 따릅니다. | [딥링크](https://docs.sparkpost.com/docs/tech-resources/deep-links-self-serve) |
| Amazon SES | 추적 클릭의 경우 `/CL0/{encodedUrl}/{index}/{messageId}/{hmac}` 형식입니다. `ses:custom-path` 속성을 설정한 링크는 `/CL1/{customPath}/{encodedUrl}/...` 형식을 따릅니다. | [커스텀 열람 및 클릭 도메인](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ESP별 클릭 및 열람 추적 URL 패턴" }

예를 들어, 클릭 추적 도메인이 `clicks.example.com`이고 ESP가 SparkPost인 경우, 추적 클릭은 `https://clicks.example.com/f/`로 시작하는 URL로 해석됩니다.

{% alert important %}
이러한 경로 접두사는 ESP가 소유하며 변경하거나 새로 추가할 수 있으므로 Braze는 영구적이거나 완전한 목록을 보장할 수 없습니다. 보안 도구가 지원하는 경우 개별 경로 대신 전체 클릭 추적 도메인을 허용 목록에 추가하고, ESP 설명서에서 최신 패턴을 확인하세요.
{% endalert %}

모바일 앱에서 이러한 경로를 처리하려면 [유니버설 링크 및 App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links)를 참조하세요.

## 문제 해결 {#troubleshooting}

CDN 구성, 인증서 및 프록시 문제는 CDN에서 처리해야 하지만, 다음 팁을 사용하여 일반적인 SSL 클릭 추적 문제를 식별할 수 있습니다. 문제 해결 가이드는 [문제 해결]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting)을 참조하세요.