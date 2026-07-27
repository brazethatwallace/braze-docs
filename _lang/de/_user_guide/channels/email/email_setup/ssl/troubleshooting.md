---
nav_title: Fehlerbehebung
article_title: Fehlerbehebung für SSL-Klick-Tracking
page_order: 5
page_type: reference
description: "Diagnostizieren Sie Probleme mit SSL-Klick-Tracking und CDN-Konfiguration mithilfe eines Symptomindex und eines standardisierten Untersuchungspfads."
channel: email
---

# Fehlerbehebung für SSL-Klick-Tracking {#troubleshoot-ssl-click-tracking}

> Verwenden Sie diese Seite, um häufige Probleme beim SSL-Klick-Tracking zu identifizieren. Die folgenden Hinweise sind allgemein gehalten, da jedes CDN einzigartig ist. Bei Problemen mit der CDN-Konfiguration, Zertifikaten oder Proxy-Einstellungen wenden Sie sich an das Support-Team Ihres CDN-Anbieters, da diese Konfigurationen außerhalb von Braze stattfinden.

## Hier starten: Symptom zuordnen {#start-here-match-your-symptom}

| Symptom | Gehe zu |
| --- | --- |
| E-Mail-Öffnungsraten sind plötzlich gesunken | [Niedrige E-Mail-Öffnungsraten](#low-email-open-rates) |
| Getrackte Links geben HTTP 403 zurück | [HTTP 403 bei Weiterleitungslinks](#http-403-on-redirect-links) |
| DNS oder CNAME verweist auf ESP statt auf CDN | [Probleme mit der Domain-Registrierung](#domain-registry-issues) |
| „Verbindung ist nicht privat“ oder Links funktionieren während der Einrichtung nicht | [CDN-Probleme](#cdn-issues) |
| SSL-Einrichtung abgeschlossen, aber Links zeigen weiterhin HTTP | [SSL-Aktivierungsstatus](#ssl-enablement-status) |
| Getrackte URL schlägt fehl, aber ungetrackte URL funktioniert | [Probleme mit dem Klick-Tracking](#click-tracking-issues) |
| Amazon-SES-spezifische SSL-Aktivierungsfehler | [Amazon SES](#amazon-ses) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SSL-Symptom" }

## Standardmäßiger Untersuchungspfad {#standard-investigation-path}

1. Bestätigen Sie, dass Ihre Klick-Tracking-Subdomain auf Ihr [Content Delivery Network (CDN)]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#what-is-a-cdn-and-why-do-i-need-it) verweist – und nicht direkt auf Ihren E-Mail-Anbieter (SendGrid, SparkPost oder Amazon SES). Bitten Sie Ihr IT- oder Web-Team zu überprüfen, ob Ihre Domain-Einstellungen mit Ihrem Braze-Setup übereinstimmen. Die Braze-Anforderungen finden Sie unter [SSL-Zertifikat erwerben]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate).
2. Bestätigen Sie, dass Ihr SSL-Zertifikat für die Tracking-Domain aktiv ist. Bitten Sie Ihr IT- oder Web-Team zu bestätigen, dass das Zertifikat aktuell ist und Ihre Klick-Tracking-Subdomain abdeckt. Informationen zu den Einrichtungsschritten und CDN-spezifischen Anleitungen finden Sie unter [SSL-Zertifikat erwerben]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate) und [Zusätzliche Ressourcen]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#additional-resources).
3. Senden Sie eine Test-E-Mail mit dem [Template zur Fehlerbehebung beim Klick-Tracking](#click-tracking-issues). Vergleichen Sie getrackte und nicht getrackte URLs.
4. Wenn getrackte Links mit einem 403-Fehler fehlschlagen, überprüfen Sie die CDN- und WAF-Regeln (User-Agents, Query-Strings, Redirect-Muster).
5. Wenn die Einrichtung abgeschlossen ist, die Links aber weiterhin HTTP verwenden, wenden Sie sich an Ihren Braze-Customer-Success-Manager, um zu bestätigen, dass Braze SSL aktiviert hat.
6. Wenden Sie sich bei anhaltenden Problemen an Ihr CDN- oder IT-Team und kontaktieren Sie den [Braze-Support]({{site.baseurl}}/braze_support) mit Fehlercodes und allen Details von Ihrem CDN- oder Domain-Anbieter.

## Schlüsselkonzepte {#key-concepts}

- **Getrackte URL:** Umschließt den ursprünglichen HTTPS-Link mit Ihrer Tracking-Domain. Wenn ein:e Nutzer:in darauf klickt, löst die Tracking-Domain die Anfrage auf und leitet zum endgültigen Ziel weiter. Ein CDN ermöglicht es Ihnen, sichere (HTTPS) URLs zu tracken. Ohne CDN kann es vorkommen, dass Nutzer:innen eine Datenschutzwarnung „Verbindung ist nicht sicher“ erhalten.
- **Nicht getrackte URL:** Behält die ursprüngliche URL unverändert bei und umgeht das CDN, um als Kontrollumgebung zu dienen.

## Niedrige E-Mail-Öffnungsraten {#low-email-open-rates}

**Symptom:** Die E-Mail-Öffnungsraten sind nach SSL- oder CDN-Änderungen plötzlich gesunken.

Wenn Sie plötzlich niedrige E-Mail-Öffnungsraten feststellen, überprüfen Sie, ob das SSL-Zertifikat aktuell ist. Wenn es abgelaufen ist, müssen Sie das SSL-Zertifikat bei Ihrem CDN- oder Zertifikatsanbieter erneuern.

## HTTP 403 bei Weiterleitungslinks {#http-403-on-redirect-links}

**Symptom:** Getrackte E-Mail-Links geben „403 Forbidden“ zurück.

Wenn getrackte Weiterleitungslinks „403 Forbidden“ zurückgeben, tritt der Fehler häufig bei Ihrem Content Delivery Network (CDN) oder Ihrer Web Application Firewall (WAF) auf – beispielsweise durch Regeln in AWS WAF oder Amazon CloudFront, die bestimmte User-Agents, Query-Strings oder Weiterleitungsmuster blockieren. Überprüfen Sie die Protokolle und Metriken blockierter Anfragen bei Ihrem CDN- oder Cloud-Anbieter. Für AWS siehe [Troubleshooting issues with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/troubleshooting.html).

Um festzustellen, ob das Problem spezifisch für das Klick-Tracking ist, deaktivieren Sie das Klick-Tracking für einen Testlink (siehe [Klick-Tracking auf Link-Ebene deaktivieren]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis)). Wenn die Ziel-URL geladen wird, wenn das Klick-Tracking deaktiviert ist, aber 403 zurückgibt, wenn das Tracking aktiviert ist, konzentrieren Sie sich auf die Konfiguration Ihrer Klick-Tracking-Domain, Ihres CDN und Ihrer WAF.

## Probleme mit der Domain-Registrierung {#domain-registry-issues}

**Symptom:** DNS oder CNAME für Ihre Tracking-Subdomain verweist auf Ihren ESP statt auf Ihr CDN.

Führen Sie einen dig-Befehl aus, um zu bestätigen, dass Ihr Link-Tracking auf das CDN verweist. Führen Sie in Ihrem Terminal `dig CNAME link_tracking_subdomain` aus. Unter `ANSWER SECTION` wird aufgelistet, wohin Ihr CNAME verweist. Wenn er auf den E-Mail-Anbieter (SendGrid, SparkPost oder Amazon SES) und nicht auf Ihr CDN verweist, konfigurieren Sie Ihre Domain-Registrierung so um, dass sie auf Ihr CDN verweist.

## CDN-Probleme {#cdn-issues}

**Symptom:** Nutzer:innen sehen Fehler wie „Verbindung ist nicht privat“, oder Links funktionieren während der CDN-Einrichtung nicht.

Wenn Live-E-Mail-Links während der Einrichtung nicht funktionieren, haben Sie wahrscheinlich DNS vor der ordnungsgemäßen Konfiguration auf Ihr CDN verwiesen. Dies kann als „falscher Link“-Fehler erscheinen. Kontaktieren Sie Ihren CDN-Anbieter und lesen Sie dessen Dokumentation zur Fehlerbehebung bei der Konfiguration.

Wenn eine Fehlermeldung angezeigt wird, dass Ihre Verbindung nicht privat ist, kann dies darauf hindeuten, dass Ihr SSL oder CDN nicht korrekt konfiguriert ist. Führen Sie einen `dig`-Befehl in Ihrem Terminal aus (z. B. `dig CNAME your_link_tracking_subdomain`). Wenn das Ergebnis in der `ANSWER SECTION` auf Ihren ESP statt auf Ihr CDN verweist, liegt eine Fehlkonfiguration vor. Damit das Braze-SSL-Klick-Tracking funktioniert, sollte der CNAME auf Ihr CDN verweisen. Koordinieren Sie sich mit dem Team, das Ihre SSL- und CDN-Konfiguration verwaltet, für weitere Unterstützung.

## SSL-Aktivierungsstatus {#ssl-enablement-status}

**Symptom:** Die SSL-Einrichtung ist abgeschlossen, aber getrackte Links erscheinen weiterhin als HTTP.

Wenn Sie die SSL-Einrichtung abgeschlossen haben und Links weiterhin als HTTP erscheinen, kontaktieren Sie Ihren Braze Customer-Success-Manager, um zu bestätigen, dass Braze SSL aktiviert hat. Braze aktiviert SSL erst, nachdem alle Einrichtungsschritte abgeschlossen sind.

### Amazon SES {#amazon-ses}

Wenn Sie Amazon SES als E-Mail-Anbieter verwenden, können die folgenden Konfigurationsprobleme verhindern, dass Braze SSL aktiviert, oder Fehler während der Einrichtung verursachen:

- **Regionsabweichung:** Bestätigen Sie, dass Ihr CDN-Origin auf die AWS-Tracking-Domain für Ihren Braze-Cluster verweist. US-Cluster verwenden `r.us-east-1.awstrack.me`. EU-Cluster verwenden `r.eu-central-1.awstrack.me`. Die Verwendung der falschen Region kann die SSL-Aktivierung blockieren.
- **Host-Header:** Amazon SES erfordert, dass Ihr CDN den korrekten Host-Header weiterleitet. Aktivieren Sie den `X-Forwarded-Host`-Header auf Ihrer Klick-Tracking-Domain. Weitere Informationen finden Sie im Abschnitt [Amazon SES](#amazon-ses).
- **Proxy-Konfiguration:** Ein Proxy- oder CDN-Setup, das den Host-Header überschreibt oder damit in Konflikt steht, kann dazu führen, dass die SSL-Aktivierung fehlschlägt. Überprüfen Sie die Proxy-Einstellungen mit Ihrem CDN-Anbieter, um sicherzustellen, dass sie die Host-Header-Weiterleitung nicht beeinträchtigen.
- **Route-53-Alias-Eintrag:** Wenn Sie Route 53 zur Verwaltung des DNS für Ihre Domain verwenden, erstellen Sie einen [Alias-Eintrag in Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html), der auf Ihre CDN-Distribution verweist (z. B. `d111111abcdef8.cloudfront.net`). Die Verwendung eines Standard-CNAME anstelle eines Alias-Eintrags kann HTTP-400-Fehler zurückgeben.
- **Header-Weiterleitung deaktiviert:** Wenn die SSL-Aktivierung nach der Konfiguration von `X-Forwarded-Host` weiterhin fehlschlägt, versuchen Sie, die Header-Weiterleitung auf Ihrem CDN oder Proxy zu deaktivieren. Einige Setups lösen das Problem, wenn die Weiterleitung vollständig deaktiviert wird. Arbeiten Sie mit Ihrem IT-Team oder CDN-Anbieter zusammen, um diese Konfiguration zu testen.

## Probleme beim Klick-Tracking {#click-tracking-issues}

**Symptom:** Getrackte E-Mail-Links schlagen fehl, aber ungetrackte Links funktionieren, oder Nutzer:innen sehen Zertifikats- oder DNS-Fehler nach dem Klicken.

Häufige Weiterleitungsprobleme resultieren typischerweise aus einer fehlerhaften Konfiguration zwischen dem CDN, das die Tracking-Domain hostet, und den zugehörigen SSL-Zertifikaten oder DNS-CNAME-Einträgen. Diese Fehlkonfigurationen führen häufig dazu, dass Nutzer:innen einen Datenschutzfehler „Verbindung ist nicht sicher“ oder einen `404`-Fehler erhalten, nachdem sie auf einen getrackten E-Mail-Link geklickt haben.

Verwenden Sie das folgende Template, um die CDN-Konfiguration Ihrer Tracking-Domain zu testen – den Mechanismus, der Analytics für Links in Ihren E-Mails unterstützt.

1. Kopieren Sie das folgende Template und fügen Sie es in eine Braze-HTML-E-Mail-Campaign ein.

{% details Template zur Fehlerbehebung beim Klick-Tracking %}
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
                            <li>For more information, visit: <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/channels/email/email_setup/ssl">SSL at Braze</a></li>
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
2. Konfigurieren Sie Ihre URL. Ersetzen Sie die URL im `capture`-Tag am Anfang des Template-Bodys (wo `https://example.com` gesetzt ist). Ersetzen Sie beispielsweise `https://example.com` durch `https://braze.com/docs`.
3. Senden Sie eine Test-E-Mail an sich selbst und klicken Sie auf beide Buttons.
4. Überprüfen Sie, ob das erwartete Verhalten und die Erfolgskriterien den Beschreibungen im Template entsprechen.

Wenn Ihre ungetrackte URL funktioniert, aber Ihre getrackte URL fehlschlägt, liegt möglicherweise eine Konfigurationslücke vor. Zur Fehlerbehebung lesen Sie die Dokumentation Ihres jeweiligen ESP- und CDN-Anbieters. Sie können auch [SSL bei Braze]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl) für detaillierte Anforderungen zur Zertifikatsbereitstellung lesen.

Verwenden Sie die folgende Tabelle, um häufige Fehler beim Testen des Klick-Trackings zu diagnostizieren.

| Fehlercode | Fehlerbehebung |
| --- | --- |
| `"Your connection is not private" (NET::ERR_CERT_COMMON_NAME_INVALID)` | Überprüfen Sie, ob Ihre Tracking-Domain ein gültiges SSL-Zertifikat hat. |
| `"This site can't be reached" (DNS_PROBE_FINISHED_NXDOMAIN)` | Überprüfen Sie Ihre DNS-Einstellungen. Stellen Sie sicher, dass Ihre Tracking-Subdomain gemäß der empfohlenen Konfiguration Ihres CDN und ESP konfiguriert ist. |
| `525 / 526 SSL Error` | Überprüfen Sie, ob die SSL-Einstellung in Ihrem CDN (z. B. Cloudflare) mit den Fähigkeiten Ihres Origins übereinstimmt. |
| `404 Not Found` | Überprüfen Sie, ob Ihr CDN so konfiguriert ist, dass der gesamte URL-Pfad an den ESP weitergeleitet wird, anstatt auf ein leeres Stammverzeichnis zu verweisen. |
| `400 Bad Request: Request Header or Cookie Too Large` | Dieser Fehler tritt typischerweise auf, wenn die Klick-Tracking-Domain zu viele große Cookies von der Domain Ihrer Website erbt. Braze setzt oder blockiert keine Cookies auf der Tracking-Domain. Konfigurieren Sie Ihr CDN so, dass diese Cookies beim Reverse-Proxying der Klick-Tracking-Anfrage nicht an den ESP gesendet werden. Möglicherweise müssen Sie auch die Einstellung `large_client_header_buffers` in Ihrer nginx-Konfiguration erhöhen (z. B. `large_client_header_buffers 4 32k;`, um Header bis zu 32&nbsp;KB zuzulassen). Weitere Informationen erhalten Sie bei Ihrem CDN-Anbieter oder Ihrem Entwicklerteam. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlercodes und Fehlerbehebung" }