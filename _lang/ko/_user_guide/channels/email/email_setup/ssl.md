---
nav_title: Braze의 SSL
article_title: SSL 개요
page_order: 5
page_type: reference
description: "이 참조 문서에서는 SSL의 정의, 용도, 그리고 Braze에서의 사용 방법에 대해 다룹니다."
channel: email

---

# Braze의 SSL {#ssl-at-braze}

> 보안 소켓 계층(SSL)은 HTTP 대신 HTTPS로 URL을 암호화합니다. HTTPS는 유효하고 신뢰할 수 있는 SSL 또는 TLS 인증서가 존재하며 해당 웹사이트를 안전하게 방문할 수 있음을 나타냅니다.

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

## SSL이 왜 중요한가요? {#why-is-ssl-important}

대부분의 도메인은 SSL이 필요하지 않지만, Braze는 다음과 같은 이유로 SSL 사용을 강력히 권장합니다.

SSL로 웹사이트와 링크를 보호하는 것은 민감한 고객 정보를 직접 다루지 않는 회사에서도 일반적인 관행입니다. 사용자는 SSL로 보호된 링크를 더 신뢰하며, 추가 인증 계층은 데이터를 보호하는 데 도움이 됩니다.

### 클릭 및 열람 추적에 필요 {#necessary-for-click-and-open-tracking}

Braze는 클릭 및 열람을 추적하기 위해 브랜드 링크 추적 서브도메인을 사용하여 링크를 변환합니다. 기본적으로 이러한 링크는 HTTP로 시작합니다. 비보안 트래픽을 제한하는 브라우저나 확장 프로그램을 사용하는 사용자는 대상 URL이 보안 URL이라 하더라도 리디렉션을 통과하는 데 어려움을 겪을 수 있습니다. 이로 인해 이미지가 깨지거나 추적이 부정확해질 수 있습니다. 링크 추적 서브도메인에 SSL을 적용하여 안전한 리디렉션을 보장하세요.

## 요구 사항 {#requirements}

### 브라우저 {#browser}

Google Chrome과 같은 주요 브라우저는 사용자를 보호하기 위해 비보안 URL을 통한 트래픽을 제한합니다. SSL을 사용하면 콘텐츠가 신뢰할 수 있음을 확인하는 데 도움이 되며, 이메일 내 깨진 링크나 이미지 같은 문제를 최소화합니다.

### HSTS 도메인 {#hsts-domains}

HTTP Strict Transport Security(HSTS) 도메인이 있는 경우 SSL을 설정하고 CDN을 구성하여 필요한 보안 인증서를 전송하도록 해야 합니다. SSL이 없으면 이미지 및 웹 링크가 깨집니다.

## SSL 인증서 획득 {#acquire-an-ssl-certificate}

제3자(일반적으로 콘텐츠 전달 네트워크(CDN))를 통해 SSL 인증서를 획득합니다. CDN은 인증서를 호스팅하며, 사용자가 링크를 클릭할 때 트래픽을 CDN을 통해 리디렉트하여 인증서를 적용한 후 SendGrid 또는 SparkPost로 전송함으로써 브라우저에 인증서를 제공합니다.

SSL 설정을 시작하려면 Braze 고객 성공 매니저에게 문의하여 Braze 이메일 설정 전체를 시작하세요.

Braze가 설정을 시작한 후 다음 단계를 따르세요:

1. Braze가 도메인 레지스트리에 추가할 DNS 레코드를 제공합니다.
2. Braze가 레코드가 레지스트리에 올바르게 추가되었는지 확인합니다.
3. 이후 CDN을 선택하고 타사 제공업체로부터 SSL 인증서를 발급받습니다.
4. 이 시점에서 CDN을 설정합니다. Braze는 CDN 구성 문제 해결을 도와드릴 수 없습니다. 추가 지원이 필요하면 CDN 공급자에게 문의하세요.
5. 고객 성공 매니저에게 연락하여 SSL을 활성화하세요.

## CDN이란 무엇이며, 왜 필요한가요? {#what-is-a-cdn-and-why-do-i-need-it}

콘텐츠 전달 네트워크(CDN)는 보안 인증서를 처리하면서 여러 매체에서 콘텐츠의 빠른 로드 시간을 보장하는 서버 플랫폼입니다.

{% alert important %}
CDN 구성은 항상 Braze에서 DNS 레코드를 검증한 후에 진행합니다. 아직 이 단계를 시작하지 않았다면 고객 성공 매니저에게 연락하여 시작 방법에 대한 추가 정보를 확인하세요.
{% endalert %}

클릭 및 열람 추적을 위해 전달 파트너는 브랜드 서브도메인을 사용하여 링크를 변환하고 CDN은 변환된 링크에 SSL 인증서를 적용합니다. 파트너는 링크와 이미지가 올바르게 표시되려면 수신자의 브라우저에 유효한 인증서를 제시해야 하는 경우가 많습니다. Braze는 인증서를 요청하거나 관리하지 않으므로 CDN을 통해 직접 설정해야 합니다.

{% alert note %}
SSL 클릭 및 열람 추적에 나열된 CDN을 사용할 수 없거나 사용하고 싶지 않은 경우, 커스텀 SSL 구성을 설정할 수 있습니다. 대체 CDN이나 커스텀 프록시를 사용하면 설정이 더 복잡해질 수 있습니다. [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) 및 [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) 설명서를 참조하세요.
{% endalert %}

### 추가 리소스 {#additional-resources}

{% alert important %}
CDN 구성 문제 해결은 CDN 공급자에게 문의하거나 일반적인 안내는 [문제 해결]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting)을 참조하세요.
{% endalert %}

특정 CDN을 구성하는 방법에 대한 ESP 파트너의 다음 리소스를 참조하세요. 사용 중인 CDN이 목록에 없더라도 해당 CDN이 SSL 인증서를 적용할 수 있는지 확인해야 합니다.

CDN의 클릭 추적 도메인을 구성할 때 호스트 헤더 공격과 같은 잠재적 보안 문제를 방지하기 위해 `X-Forwarded-Host` 헤더를 활성화하세요. 자세한 단계는 CDN 설명서 또는 고객지원 팀을 참조하세요.

| 파트너 | CDN | 설명서 |
| --- | --- | --- |
| Amazon SES | AWS CloudFront | [CloudFront에서 HTTPS 사용](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) |
| Amazon SES | CloudFlare | [SSL/TLS 시작하기](https://developers.cloudflare.com/ssl/get-started/) |
| Amazon SES | Fastly | [Fastly가 관리하는 인증서로 TLS 설정](https://www.fastly.com/documentation/guides/getting-started/domains/securing-domains/setting-up-tls-with-certificates-fastly-manages/) |
| Amazon SES | KeyCDN | [커스텀 SSL 설정 방법](https://www.keycdn.com/support/how-to-setup-custom-ssl) |
| Amazon SES | Google Cloud | [Google 관리 SSL 인증서](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) |
| SendGrid | AWS CloudFront | [CloudFront를 사용하여 클릭 추적용 SSL 구성 방법](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront) |
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

Amazon SES를 ESP로 사용하는 경우, [Amazon SES 설명서](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html)의 **옵션 2: HTTPS 도메인 구성**을 참조하고 Braze 클러스터에 따라 리전별 AWS 추적 도메인을 지정하세요:

- **Braze US 클러스터:** `r.us-east-1.awstrack.me`
- **Braze EU 클러스터:** `r.eu-central-1.awstrack.me`

{% alert important %}
CDN의 클릭 추적 도메인을 구성할 때 호스트 헤더 공격과 같은 잠재적 보안 문제를 방지하기 위해 `X-Forwarded-Host` 헤더를 활성화하세요. 자세한 단계는 CDN 공급자에게 문의하세요.
{% endalert %}

## 문제 해결 {#troubleshooting}

CDN 구성, 인증서 및 프록시 문제는 CDN에서 처리해야 하지만, 다음 팁을 사용하여 일반적인 SSL 클릭 추적 문제를 식별할 수 있습니다. 문제 해결 안내는 [문제 해결]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting)을 참조하세요.