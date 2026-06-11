---
nav_title: 문제 해결
article_title: SSL 문제 해결
page_order: 5
page_type: reference
description: "이 참조 문서에서는 SSL 문제 해결 팁을 다룹니다."
channel: email
---

# 문제 해결 {#troubleshooting}

> 이 팁을 사용하여 일반적인 SSL 클릭 추적 문제를 식별하세요. 모든 CDN은 고유하므로 문제 해결 안내는 일반적인 내용입니다. CDN 구성, 인증서 또는 프록시 문제는 Braze 생태계 외부에서 이루어지는 구성이므로 CDN 고객지원 팀에 문의하세요.

## 주요 개념 {#key-concepts}

- **추적 URL:** 원래 HTTPS 링크를 추적 도메인으로 래핑합니다. 사용자가 클릭하면 추적 도메인이 요청을 해석하고 최종 대상으로 리디렉션합니다. CDN을 사용하면 보안(HTTPS) URL을 추적할 수 있습니다. CDN이 없으면 사용자에게 "연결이 안전하지 않습니다" 개인정보 보호 오류가 표시될 수 있습니다.
- **비추적 URL:** 원래 URL을 그대로 유지하며, CDN을 우회하여 제어 환경으로 사용됩니다.

## 낮은 이메일 열람률 {#low-email-open-rates}

갑자기 이메일 열람률이 낮아진 경우, SSL 인증서가 최신 상태인지 확인하세요. 만료된 경우 CDN 또는 인증서 공급자를 통해 SSL 인증서를 갱신해야 합니다.

## 리디렉션 링크에서 HTTP 403 {#http-403-on-redirect-links}

추적 리디렉션 링크가 **403 Forbidden**을 반환하는 경우, 이 오류는 콘텐츠 전송 네트워크(CDN) 또는 웹 애플리케이션 방화벽(WAF)에서 발생하는 경우가 많습니다. 예를 들어, 특정 사용자 에이전트, 쿼리 문자열 또는 리디렉션 패턴을 차단하는 AWS WAF 또는 Amazon CloudFront 규칙이 원인일 수 있습니다. CDN 또는 클라우드 공급자와 함께 차단된 요청 로그 및 측정기준을 검토하세요. AWS의 경우 [CloudFront 문제 해결](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/troubleshooting.html)을 참조하세요.

문제가 클릭 추적에 한정된 것인지 확인하려면 테스트 링크 하나에 대해 클릭 추적을 끄세요([링크별 클릭 추적 끄기]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/#turning-off-click-tracking-on-a-link-to-link-basis) 참조). 클릭 추적이 꺼져 있을 때 대상 URL이 로드되지만 추적이 켜져 있을 때 403을 반환하면, 클릭 추적 도메인, CDN 및 WAF 구성에 집중하세요.

## 도메인 레지스트리 문제 {#domain-registry-issues}

dig 명령을 실행하여 링크 추적이 CDN을 가리키는지 확인하세요. 터미널에서 `dig CNAME link_tracking_subdomain`을 실행합니다. `ANSWER SECTION`에 CNAME이 가리키는 위치가 나열됩니다. CDN이 아닌 이메일 서비스 공급자(SendGrid, SparkPost 또는 Amazon SES)를 가리키는 경우, 도메인 레지스트리를 CDN을 가리키도록 재구성하세요.

## CDN 문제 {#cdn-issues}

설정 중에 라이브 이메일 링크가 깨지는 경우, 적절한 구성 전에 DNS를 CDN으로 지정했을 가능성이 높습니다. 이는 "잘못된 링크" 오류로 나타날 수 있습니다. CDN 공급자에 문의하고 해당 설명서를 검토하여 구성 문제를 해결하세요.

연결이 비공개가 아니라는 오류 메시지가 표시되면, SSL 또는 CDN이 올바르게 구성되지 않았을 수 있습니다. 터미널에서 `dig` 명령을 실행하세요(예: `dig CNAME your_link_tracking_subdomain`). `ANSWER SECTION`에서 결과가 CDN이 아닌 이메일 서비스 공급자를 가리키면 잘못된 구성 문제입니다. Braze SSL 클릭 추적이 작동하려면 CNAME이 CDN을 가리켜야 합니다. 추가 지원이 필요하면 SSL 및 CDN 구성을 관리하는 팀과 협력하세요.

## SSL 활성화 상태 {#ssl-enablement-status}

SSL 설정을 완료했는데도 링크가 여전히 HTTP로 표시되는 경우, Braze 고객 성공 매니저에게 연락하여 Braze에서 SSL이 활성화되었는지 확인하세요. Braze는 모든 설정 단계가 완료된 후에만 SSL을 활성화합니다.

### Amazon SES {#amazon-ses}

이메일 서비스 공급자로 Amazon SES를 사용하는 경우, 다음 구성 문제로 인해 Braze에서 SSL을 활성화하지 못하거나 설정 중 오류가 발생할 수 있습니다:

- **리전 불일치:** CDN 오리진이 Braze 클러스터의 AWS 추적 도메인을 가리키는지 확인하세요. US 클러스터는 `r.us-east-1.awstrack.me`를 사용합니다. EU 클러스터는 `r.eu-central-1.awstrack.me`를 사용합니다. 잘못된 리전을 사용하면 SSL 활성화가 차단될 수 있습니다.
- **호스트 헤더:** Amazon SES는 CDN이 올바른 호스트 헤더를 전달하도록 요구합니다. 클릭 추적 도메인에서 `X-Forwarded-Host` 헤더를 활성화하세요. 자세한 내용은 [Amazon SES](#amazon-ses) 섹션을 참조하세요.
- **프록시 구성:** 호스트 헤더를 재정의하거나 충돌하는 프록시 또는 CDN 설정은 SSL 활성화 실패를 유발할 수 있습니다. CDN 공급자와 함께 프록시 설정을 검토하여 호스트 헤더 전달을 방해하지 않는지 확인하세요.
- **Route 53 별칭 레코드:** Route 53을 사용하여 도메인의 DNS를 관리하는 경우, CDN 배포(예: `d111111abcdef8.cloudfront.net`)를 가리키는 [Route 53 별칭 레코드](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html)를 생성하세요. 별칭 레코드 대신 표준 CNAME을 사용하면 HTTP 400 오류가 반환될 수 있습니다.
- **헤더 전달 비활성화:** `X-Forwarded-Host`를 구성한 후에도 SSL 활성화가 실패하면, CDN 또는 프록시에서 헤더 전달을 비활성화해 보세요. 일부 설정에서는 전달을 완전히 끄면 문제가 해결됩니다. IT 팀 또는 CDN 공급자와 협력하여 이 구성을 테스트하세요.

## 클릭 추적 문제 {#click-tracking-issues}

일반적인 리디렉션 문제는 추적 도메인을 호스팅하는 CDN과 관련 SSL 인증서 또는 DNS CNAME 레코드 간의 부적절한 구성에서 발생합니다. 이러한 잘못된 구성으로 인해 사용자가 추적된 이메일 링크를 클릭한 후 "연결이 안전하지 않습니다" 개인정보 보호 오류 또는 `404` 실패를 경험하는 경우가 많습니다.

다음 템플릿을 사용하여 추적 도메인의 CDN 구성을 테스트하세요. 이는 이메일 내 링크에 대한 분석을 지원하는 메커니즘입니다.

1. 다음 템플릿을 복사하여 Braze HTML 이메일 Campaign에 붙여넣으세요.

{% details 클릭 추적 문제 해결 템플릿 %}
{% raw %}
```html
<!DOCTYPE html>
<html lang="en" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="color-scheme" content="light dark">
    <meta name="supported-color-schemes" content="light dark">
    <title>Click Tracking Test</title>
    <style>
        /* Base Dark Mode (Default) */
        body {
            margin: 0;
            padding: 0;
            background-color: #2b0562;
            font-family: 'Helvetica Neue', Arial, sans-serif;
            color: #ffd1e9;
        }

        .email-container {
            width: 100%;
            max-width: 600px;
            margin: 40px auto;
            background-color: rgba(255, 255, 255, 0.05);
            border: 1px solid #F3697F;
            border-radius: 16px;
            overflow: hidden;
        }

        .header {
            background: linear-gradient(135deg, #E83F21 0%, #F3697F 100%);
            padding: 40px 20px 50px 20px;
            text-align: center;
        }

        .logo {
            display: block;
            margin: 0 auto 25px auto;
            border: 0;
            outline: none;
            text-decoration: none;
        }

        .header h1 {
            color: #ffffff;
            margin: 0;
            font-size: 26px;
            font-weight: 800;
            letter-spacing: -0.5px;
        }

        .content {
            padding: 40px 40px 20px 40px;
            line-height: 1.8;
            font-size: 15px;
        }

        .troubleshoot {
            margin: 0 40px 40px 40px;
            padding: 25px;
            background-color: rgba(253, 167, 216, 0.1);
            border-radius: 12px;
            font-size: 14px;
            border: 1px dashed #F3697F;
        }

        .troubleshoot h2 {
            margin-top: 0;
            font-size: 18px;
            color: #ffffff;
        }

        .btn-section {
            padding: 0 40px 40px 40px;
            text-align: center;
        }

        .btn {
            display: inline-block;
            padding: 16px 32px;
            border-radius: 12px;
            font-weight: 700;
            text-decoration: none;
            margin: 10px;
            font-size: 14px;
        }

        .btn-tracked {
            background-color: #F3697F;
            color: #ffffff;
        }

        .btn-untracked {
            border: 2px solid #FDA7D8;
            color: #FDA7D8;
            background-color: transparent;
        }

        .footer {
            text-align: center;
            font-size: 12px;
            color: #FDA7D8;
            padding-bottom: 40px;
            opacity: 0.6;
        }

        /* Light Mode Overrides */
        @media (prefers-color-scheme: light) {
            body { background-color: #F7FCFF !important; color: #2b0562 !important; }
            .email-container { background-color: #ffffff !important; border: 1px solid #FDA7D8 !important; box-shadow: 0 4px 20px rgba(43, 5, 98, 0.1); }
            .content { color: #2b0562 !important; }
            .troubleshoot { background-color: #F7FCFF !important; border-color: #F3697F !important; color: #2b0562 !important; }
            .troubleshoot h2 { color: #E83F21 !important; }
            .btn-untracked { color: #F3697F !important; border-color: #F3697F !important; }
            .footer { color: #2b0562 !important; }
            strong { color: #E83F21 !important; }
        }

        /* Mobile Optimization */
        @media only screen and (max-width: 480px) {
            .btn { display: block !important; margin: 10px 0 !important; width: auto !important; }
            .content, .troubleshoot { padding: 25px !important; }
        }
    </style>
</head>
{%- capture url -%}https://example.com{%- endcapture -%}
<body>
    <center>
        <table class="email-container" role="presentation" width="600" border="0" cellpadding="0" cellspacing="0">
            <tr>
                <td class="header">
                    <img src="https://cdn-staging.braze.com/appboy/communication/assets/image_assets/images/60aecba96a93150c749b4d57/original.png?1622068137"
                         width="150"
                         alt="Logo"
                         class="logo">
                    <h1>Testing Click Tracking Functionality</h1>
                </td>
            </tr>
            <tr>
                <td class="content">
                    <p>
                        Use this template to test the <strong>CDN configuration</strong> of your tracking domain—the mechanism supporting analytics for links within your emails.
                    </p>
                    <p>
                        A <strong>Tracked URL</strong> wraps the original HTTPS link in your tracking domain. When a user clicks it, the tracking domain resolves the request and redirects to the final destination. A CDN allows you to track secure (HTTPS) URLs; without it, users may encounter a "connection is not secure" privacy error. An <strong>Untracked URL</strong> maintains the original URL intact, bypassing the CDN to serve as a control environment.
                    </p>
                    <p>
                        Common redirection issues typically result from an improper configuration between the CDN hosting the tracking domain and the <strong>associated SSL certificate or DNS CNAME records.</strong>
                    </p>
                    <p>
                        <i style="font-size: 13px;">This template uses "example.com" as the destination URL. To test your own domain, replace the URL in the <strong>capture</strong> tag located on line 125.</i>
                    </p>
                </td>
            </tr>
            <tr>
                <td class="btn-section">
                    <a href="{{url}}" class="btn btn-tracked">Tracked URL</a>

                    <a href="{{url}}"
                       class="btn btn-untracked"
                       clicktracking="off"
                       data-msys-clicktrack="0"
                       ses:no-track="true">
                       Untracked URL
                    </a>
                </td>
            </tr>
            <tr>
                <td>
                    <div class="troubleshoot">
                        <h2>Troubleshooting the Test</h2>
                        <ul>
                            <li><strong>Tracked URL Fails / Untracked Works:</strong> This indicates a CDN or SSL certificate issue. Verify that your SSL certificate is valid and correctly bound to your tracking domain.</li>
                            <li><strong>Privacy Error (HTTPS):</strong> Ensure your CDN is configured to handle port 443 traffic and that the certificate matches your tracking CNAME.</li>
                            <li><strong>Both URLs Fail:</strong> Check the destination URL or your internal network firewall settings.</li>
                            <li>For more information, visit: <a href="https://www.braze.com/docs/user_guide/channels/email/email_setup/ssl">SSL at Braze</a></li>
                        </ul>
                    </div>
                </td>
            </tr>
        </table>
        <div class="footer">
            Braze :: 63 Madison Avenue, 13th Floor :: New York, NY 10016
        </div>
    </center>
</body>
</html>
```
{% endraw %}
{% enddetails %}

{: start="2"}
2. URL을 구성합니다. 템플릿 본문 상단 근처의 `capture` 태그에 있는 URL을 교체하세요(`https://example.com`이 설정된 곳). 예를 들어, `https://example.com`을 `https://braze.com/docs`로 교체합니다.
3. 자신에게 테스트 이메일을 보내고 두 버튼을 모두 선택하세요.
4. 예상 동작과 성공 기준이 템플릿에 설명된 대로인지 확인하세요.

비추적 URL은 작동하지만 추적 URL이 실패하는 경우, 구성 차이가 있을 수 있습니다. 문제를 해결하려면 사용 중인 이메일 서비스 공급자 및 CDN 공급자의 설명서를 참조하세요. 인증서 프로비저닝에 대한 자세한 요구 사항은 [Braze의 SSL]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/)을 검토할 수도 있습니다.

다음 표를 사용하여 클릭 추적 테스트 시 일반적인 오류를 진단하세요.

| 오류 코드 | 문제 해결 |
| --- | --- |
| `"Your connection is not private" (NET::ERR_CERT_COMMON_NAME_INVALID)` | 추적 도메인에 유효한 SSL 인증서가 있는지 확인하세요. |
| `"This site can't be reached" (DNS_PROBE_FINISHED_NXDOMAIN)` | DNS 설정을 확인하세요. CDN 및 이메일 서비스 공급자 권장 구성에 따라 추적 하위 도메인이 구성되어 있는지 확인하세요. |
| `525 / 526 SSL Error` | CDN(예: Cloudflare)의 SSL 설정이 오리진의 기능과 일치하는지 확인하세요. |
| `404 Not Found` | CDN이 빈 루트 디렉토리를 가리키는 대신 전체 URL 경로를 이메일 서비스 공급자에게 전달하도록 구성되어 있는지 확인하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="오류 코드 및 문제 해결" }