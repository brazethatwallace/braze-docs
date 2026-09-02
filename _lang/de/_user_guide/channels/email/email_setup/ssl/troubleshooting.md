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
| DNS oder CNAME verweist auf den E-Mail-Anbieter statt auf das CDN | [Probleme mit der Domain-Registrierung](#domain-registry-issues) |
| „Verbindung ist nicht privat“ oder Links funktionieren während der Einrichtung nicht | [CDN-Probleme](#cdn-issues) |
| SSL-Einrichtung abgeschlossen, aber Links zeigen weiterhin HTTP | [SSL-Aktivierungsstatus](#ssl-enablement-status) |
| Getrackte URL schlägt fehl, aber ungetrackte URL funktioniert | [Probleme mit dem Klick-Tracking](#click-tracking-issues) |
| Amazon-SES-spezifische SSL-Aktivierungsfehler | [Amazon SES](#amazon-ses) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SSL-Symptom" }

## Standardmäßiger Untersuchungspfad {#standard-investigation-path}

1. Vergewissern Sie sich, dass Ihre Klick-Tracking-Subdomain auf Ihr [Content Delivery Network (CDN)]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#what-is-a-cdn-and-why-do-i-need-it) verweist – nicht direkt auf Ihren E-Mail-Anbieter (SendGrid, SparkPost oder Amazon SES). Bitten Sie Ihr IT- oder Web-Team zu überprüfen, ob Ihre Domain-Einstellungen mit Ihrem Braze-Setup übereinstimmen. Informationen zu den Braze-Anforderungen finden Sie unter [SSL-Zertifikat erwerben]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate).
2. Vergewissern Sie sich, dass Ihr SSL-Zertifikat für die Tracking-Domain aktiv ist. Bitten Sie Ihr IT- oder Web-Team zu bestätigen, dass das Zertifikat aktuell ist und Ihre Klick-Tracking-Subdomain abdeckt. Informationen zu den Einrichtungsschritten und CDN-spezifischen Anleitungen finden Sie unter [SSL-Zertifikat erwerben]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate) und [Zusätzliche Ressourcen]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#additional-resources).
3. Senden Sie eine Test-E-Mail mit dem [Template zur Fehlerbehebung bei Klick-Tracking](#click-tracking-issues). Vergleichen Sie getrackte und nicht getrackte URLs.
4. Wenn getrackte Links mit einem 403-Fehler fehlschlagen, überprüfen Sie die CDN- und WAF-Regeln (User-Agents, Query-Strings, Redirect-Muster).
5. Wenn die Einrichtung abgeschlossen ist, Links aber weiterhin HTTP verwenden, kontaktieren Sie Ihren Braze-CSM, um zu bestätigen, dass Braze SSL aktiviert hat.
6. Koordinieren Sie sich bei anhaltenden Problemen mit Ihrem CDN- oder IT-Team und kontaktieren Sie den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) mit Fehlercodes und allen Details von Ihrem CDN- oder Domain-Anbieter.

## Schlüsselkonzepte {#key-concepts}

- **Klick, der-Tracking-Domain (CTD):** Die gebrandete Subdomain, die Braze zum Umschließen von Links für das Klick-Tracking verwendet (zum Beispiel `clicks.mail.yourbrand.com`).
- **Getrackte URL:** Umschließt den ursprünglichen HTTPS-Link in Ihrer Tracking-Domain. Wenn eine:r Nutzer:in darauf klickt, löst die Tracking-Domain die Anfrage auf und leitet zum endgültigen Ziel weiter. Ein CDN ermöglicht es Ihnen, sichere (HTTPS) URLs zu tracken. Ohne CDN kann es vorkommen, dass Nutzer:innen die Datenschutzwarnung „Verbindung ist nicht sicher“ sehen.
- **Ungetrackte URL:** Behält die ursprüngliche URL unverändert bei und umgeht das CDN, um als Kontrollumgebung zu dienen.
- **Phase-1- und Phase-2-Routing:** Phase 1 verweist den CNAME Ihrer Klick, der-Tracking-Domain direkt auf Ihren E-Mail-Anbieter (E-Mail-Anbieter) für die anfängliche HTTP-Verifizierung. Phase 2 verweist den CNAME auf Ihr CDN oder Ihre Web Application Firewall (WAF), die SSL terminiert und Anfragen mit den erforderlichen Headern an den E-Mail-Anbieter weiterleitet. Informationen zu E-Mail-Anbieter-spezifischen CNAME-Zielen finden Sie unter [E-Mail-Anbieter Phase-1- und Phase-2-Routing](#esp-phase-1-and-phase-2-routing).

## Klick-Tracking-Domains und DNS-Phasen {#click-tracking-domains-and-dns-phases}

SSL-Klick-Tracking erfordert ein zweiphasiges DNS-Setup, da Braze keine externen Sicherheitszertifikate in Ihrem Namen bereitstellt oder erneuert.

1. **Phase 1 (Ersteinrichtung):** Ihr Klick-Tracking-Domain-CNAME verweist direkt auf Ihren E-Mail-Anbieter-Endpunkt für die unverschlüsselte HTTP-Verifizierung.
2. **Phase 2 (SSL-Bereitstellung):** Sie aktualisieren den CNAME auf Ihren CDN- oder WAF-Edge, der Ihr benutzerdefiniertes SSL-Zertifikat hält und Anfragen mit den erforderlichen Headern an den E-Mail-Anbieter weiterleitet. Der E-Mail-Anbieter protokolliert den Klick und leitet die Empfänger:innen zum endgültigen Ziel weiter.

{% alert important %}
Braze aktiviert SSL-Klick-Tracking erst, nachdem die Verifizierung von Phase 1 abgeschlossen ist. Wenn SSL aktiviert ist, Ihr DNS aber noch auf den E-Mail-Anbieter verweist (Phase 1), können Empfänger:innen [SSL-Namenskonfliktfehler](#ssl-name-mismatch-errors) sehen.
{% endalert %}

## E-Mail-Anbieter Phase 1 und Phase 2 Routing {#esp-phase-1-and-phase-2-routing}

Prüfen Sie bei der Fehlerbehebung von Link-Tracking-Fehlern, ob Ihr DNS-Eintrag auf das unverschlüsselte E-Mail-Anbieter-Netzwerk (Phase 1) oder Ihr CDN (Phase 2) verweist.

| E-Mail-Anbieter | Phase 1 CNAME-Ziel (direkt zum E-Mail-Anbieter) | Phase 2 CNAME-Ziel | Erforderliche CDN-Konfiguration |
| --- | --- | --- | --- |
| Amazon SES | `r.us-east-1.awstrack.me` (US)<br>`r.eu-central-1.awstrack.me` (EU) | Ihr CDN-Endpunkt (zum Beispiel `d123.cloudfront.net`, `ssl.fastly.net` oder Cloudflare) | Aktivieren Sie den `X-Forwarded-Host`-Header mit Ihrem Klick-Tracking-Domainnamen |
| SendGrid | `sendgrid.net` | Ihr CDN-Endpunkt | Leiten Sie die ursprünglichen `Host`-Header (oder angepasste Marken-Tracking-IDs) ohne Parameterverlust an den Ursprung weiter |
| SparkPost | `spgo.io` | Ihr CDN-Endpunkt | Aktivieren Sie `X-Forwarded-Host` und leiten Sie den ursprünglichen `User-Agent`-Header unverändert weiter |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="E-Mail-Anbieter Phase 1 und Phase 2 Routing" }

Informationen zu CDN-Einrichtungsschritten und Partner-Dokumentation finden Sie unter [SSL bei Braze]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl).

## SSL-Namensabweichungsfehler {#ssl-name-mismatch-errors}

Eine SSL-Namensabweichung ist ein Fehler bei der Identitätsauthentifizierung während des TLS-Handshakes. Sie tritt auf, wenn ein Browser eine verschlüsselte Verbindung herstellt, die Domain in der Adressleiste jedoch mit keinem Eintrag in den Feldern „Common Name“ (CN) oder „Subject Alternative Names“ (SAN) des Zertifikats übereinstimmt.

### DNS verweist noch auf den E-Mail-Anbieter (Phase 1) {#dns-still-points-to-the-esp-phase-1}

Wenn Sie Braze anweisen, SSL-Klick-Tracking zu aktivieren, Ihren DNS-CNAME aber weiterhin direkt auf den E-Mail-Anbieter verweisen lassen (zum Beispiel auf SendGrids `sendgrid.net`), öffnet der Browser der Empfänger:innen Ihre Klick-Tracking-Domain und erreicht die Infrastruktur des E-Mail-Anbieter. Der E-Mail-Anbieter hat keinen Eintrag für Ihr benutzerdefiniertes Zertifikat und liefert sein eigenes Fallback-Zertifikat aus (zum Beispiel `*.sendgrid.net`). Die Namensabweichung lässt die Verbindung fehlschlagen und gibt eine Warnung zu einer privaten Verbindung zurück.

### Zertifikat deckt die Tracking-Subdomain nicht ab (Phase 2) {#certificate-does-not-cover-the-tracking-subdomain-phase-2}

Wenn Ihr DNS auf Ihr CDN verweist (Cloudflare, CloudFront usw.), Ihr Sicherheitsteam jedoch ein Zertifikat angewendet hat, das nur primäre Web-Assets abdeckt (zum Beispiel `yourbrand.com` und `www.yourbrand.com`), ist die spezifische Klick-Tracking-Subdomain (zum Beispiel `clicks.mail.yourbrand.com`) nicht enthalten. Das CDN liefert ein Zertifikat aus, das nicht mit der Tracking-Domain übereinstimmt, und Browser zeigen einen Datenschutzfehler an.

## Triage-Workflow {#triage-workflow}

### Schritt 1: Einen autoritativen CNAME-Lookup durchführen {#step-1-run-an-authoritative-cname-lookup}

Öffnen Sie Ihr Terminal und überprüfen Sie das DNS-Routing für Ihre Klick-Tracking-Domain:

```bash
dig CNAME clicks.mail.yourbrand.com
```

Überprüfen Sie im `ANSWER SECTION`, wohin der CNAME aufgelöst wird:

| Ergebnis | Bedeutung | Nächster Schritt |
| --- | --- | --- |
| Wird zu einem E-Mail-Anbieter-Endpunkt aufgelöst (`sendgrid.net`, `spgo.io` oder `awstrack.me`) | DNS befindet sich noch in Phase 1 | Aktualisieren Sie Ihre Domain-Registrierung, um den Traffic über Ihr CDN zu leiten. Siehe [E-Mail-Anbieter Phase 1 und Phase 2 Routing](#esp-phase-1-and-phase-2-routing). |
| Wird zu einem CDN-Distributions-Endpunkt aufgelöst | Phase-2-DNS-Routing ist korrekt | Fahren Sie mit Schritt 2 fort |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CNAME-Lookup-Ergebnisse" }

### Schritt 2: Das TLS-Zertifikat validieren {#step-2-validate-the-tls-certificate}

Erzwingen Sie eine Live-TLS-Validierung gegen Ihre Klick-Tracking-Domain, um genau zu sehen, welches Zertifikat Browser erhalten. Geben Sie Ihre Klick-Tracking-Domain in einen externen SSL-Checker ein, z. B. den [SSL Checker von SSL Shopper](https://www.sslshopper.com/ssl-checker.html#hostname=clicks.mail.yourbrand.com) (ersetzen Sie `clicks.mail.yourbrand.com` durch Ihre Domain).

Bestätigen Sie Folgendes:

- Das Zertifikat ist gültig und nicht abgelaufen
- Ihre Klick-Tracking-Domain erscheint im Common Name oder in den Subject Alternative Names
- Die Zertifikatskette ist vollständig, ohne Warnungen zu nicht vertrauenswürdigen Zwischenzertifikaten

{% alert tip %}
Für einen detaillierteren TLS-Bericht können Sie auch den [Qualys SSL Labs SSL Server Test](https://www.ssllabs.com/ssltest/) verwenden.
{% endalert %}

### Schritt 3: CDN-Konfigurationsprobleme überprüfen {#step-3-review-cdn-configuration-issues}

Wenn Live-E-Mail-Links während der Einrichtung nicht funktionieren, überprüfen Sie, ob DNS nicht auf Ihr CDN verwiesen wurde, bevor die Konfiguration abgeschlossen war. Dies kann sich als fehlerhafter Link oder Verbindungsfehler äußern. Kontaktieren Sie Ihren CDN-Anbieter und lesen Sie dessen Dokumentation, um Proxy- und Origin-Einstellungen zu überprüfen. Koordinieren Sie sich mit dem Team, das Ihre SSL- und CDN-Konfiguration verwaltet, um weitere Unterstützung zu erhalten.

## Niedrige E-Mail-Öffnungsraten {#low-email-open-rates}

**Symptom:** Die E-Mail-Öffnungsraten sind nach SSL- oder CDN-Änderungen plötzlich gesunken.

Wenn Sie plötzlich niedrige E-Mail-Öffnungsraten feststellen, überprüfen Sie, ob das SSL-Zertifikat aktuell ist. Wenn es abgelaufen ist, müssen Sie das SSL-Zertifikat bei Ihrem CDN- oder Zertifikatsanbieter erneuern.

## HTTP 403 bei Weiterleitungslinks {#http-403-on-redirect-links}

**Symptom:** Getrackte E-Mail-Links geben „403 Forbidden“ zurück.

Wenn getrackte Weiterleitungslinks `403 Forbidden` zurückgeben, tritt der Fehler häufig bei Ihrem Content Delivery Network (CDN) oder Ihrer Web Application Firewall (WAF) auf – beispielsweise durch Regeln in AWS WAF oder Amazon CloudFront, die bestimmte User-Agents, Query-Strings oder Weiterleitungsmuster blockieren. Überprüfen Sie die Protokolle und Metriken blockierter Anfragen bei Ihrem CDN- oder Cloud-Anbieter. Für AWS siehe [Troubleshooting issues with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/troubleshooting.html).

Um festzustellen, ob das Problem spezifisch für das Klick-Tracking ist, deaktivieren Sie das Klick-Tracking für einen Testlink (siehe [Klick-Tracking auf Link-Ebene deaktivieren]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis)). Wenn die Ziel-URL geladen wird, wenn das Klick-Tracking deaktiviert ist, aber `403` zurückgibt, wenn das Tracking aktiviert ist, konzentrieren Sie sich auf die Konfiguration Ihrer Klick-Tracking-Domain, Ihres CDN und Ihrer WAF. Wenn Ihr CNAME noch auf den E-Mail-Anbieter verweist, während SSL aktiviert ist, wird möglicherweise ein [SSL-Namenskonfliktfehler](#ssl-name-mismatch-errors) angezeigt – beginnen Sie in diesem Fall mit dem [Triage-Workflow](#triage-workflow).

## Probleme mit der Domain-Registrierung {#domain-registry-issues}

**Symptom:** DNS oder CNAME für Ihre Tracking-Subdomain verweist auf Ihren E-Mail-Anbieter statt auf Ihr CDN.

Führen Sie einen dig-Befehl aus, um zu bestätigen, dass Ihr Link-Tracking auf das CDN verweist. Führen Sie in Ihrem Terminal `dig CNAME link_tracking_subdomain` aus. Unter `ANSWER SECTION` wird aufgelistet, wohin Ihr CNAME verweist. Wenn er auf den E-Mail-Anbieter (SendGrid, SparkPost oder Amazon SES) und nicht auf Ihr CDN verweist, konfigurieren Sie Ihre Domain-Registrierung so um, dass sie auf Ihr CDN verweist.

## CDN-Probleme {#cdn-issues}

**Symptom:** Nutzer:innen sehen Fehler wie „Verbindung ist nicht privat“, oder Links funktionieren während der CDN-Einrichtung nicht.

Wenn Live-E-Mail-Links während der Einrichtung nicht funktionieren, haben Sie wahrscheinlich DNS vor der ordnungsgemäßen Konfiguration auf Ihr CDN verwiesen. Dies kann als „falscher Link“-Fehler erscheinen. Kontaktieren Sie Ihren CDN-Anbieter und lesen Sie dessen Dokumentation zur Fehlerbehebung bei der Konfiguration.

Wenn eine Fehlermeldung angezeigt wird, dass Ihre Verbindung nicht privat ist, kann dies darauf hindeuten, dass Ihr SSL oder CDN nicht korrekt konfiguriert ist. Führen Sie einen `dig`-Befehl in Ihrem Terminal aus (z. B. `dig CNAME your_link_tracking_subdomain`). Wenn das Ergebnis in der `ANSWER SECTION` auf Ihren E-Mail-Anbieter statt auf Ihr CDN verweist, liegt eine Fehlkonfiguration vor. Damit das Braze-SSL-Klick-Tracking funktioniert, sollte der CNAME auf Ihr CDN verweisen. Koordinieren Sie sich mit dem Team, das Ihre SSL- und CDN-Konfiguration verwaltet, für weitere Unterstützung.

## SSL-Aktivierungsstatus {#ssl-enablement-status}

**Symptom:** Die SSL-Einrichtung ist abgeschlossen, aber getrackte Links erscheinen weiterhin als HTTP.

Wenn Sie die SSL-Einrichtung abgeschlossen haben und Links weiterhin als HTTP erscheinen, kontaktieren Sie Ihren Braze CSM, um zu bestätigen, dass Braze SSL aktiviert hat. Braze aktiviert SSL erst, nachdem alle Einrichtungsschritte abgeschlossen sind.

### Amazon SES {#amazon-ses}

Wenn Sie Amazon SES als E-Mail-Anbieter verwenden, können die folgenden Konfigurationsprobleme verhindern, dass Braze SSL aktiviert, oder Fehler während der Einrichtung verursachen:

- **Regionsabweichung:** Bestätigen Sie, dass Ihr CDN-Origin auf die AWS-Tracking-Domain für Ihren Braze-Cluster verweist. US-Cluster verwenden `r.us-east-1.awstrack.me`. EU-Cluster verwenden `r.eu-central-1.awstrack.me`. Die Verwendung der falschen Region kann die SSL-Aktivierung blockieren.
- **Host-Header:** Amazon SES erfordert, dass Ihr CDN den korrekten Host-Header weiterleitet. Aktivieren Sie den `X-Forwarded-Host`-Header auf Ihrer Klick-Tracking-Domain. Informationen zu den Routing-Anforderungen für Phase 1 und Phase 2 finden Sie unter [E-Mail-Anbieter Phase 1 und Phase 2 Routing](#esp-phase-1-and-phase-2-routing).
- **Proxy-Konfiguration:** Ein Proxy- oder CDN-Setup, das den Host-Header überschreibt oder damit in Konflikt steht, kann dazu führen, dass die SSL-Aktivierung fehlschlägt. Überprüfen Sie die Proxy-Einstellungen mit Ihrem CDN-Anbieter, um sicherzustellen, dass sie die Host-Header-Weiterleitung nicht beeinträchtigen.
- **Route-53-Alias-Eintrag:** Wenn Sie Route 53 zur Verwaltung des DNS für Ihre Domain verwenden, erstellen Sie einen [Alias-Eintrag in Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html), der auf Ihre CDN-Distribution verweist (z. B. `d111111abcdef8.cloudfront.net`). Die Verwendung eines Standard-CNAME anstelle eines Alias-Eintrags kann HTTP-400-Fehler zurückgeben.
- **Header-Weiterleitung deaktiviert:** Wenn die SSL-Aktivierung nach der Konfiguration von `X-Forwarded-Host` weiterhin fehlschlägt, versuchen Sie, die Header-Weiterleitung auf Ihrem CDN oder Proxy zu deaktivieren. Einige Setups lösen das Problem, wenn die Weiterleitung vollständig deaktiviert wird. Arbeiten Sie mit Ihrem IT-Team oder CDN-Anbieter zusammen, um diese Konfiguration zu testen.

## Probleme beim Klick-Tracking {#click-tracking-issues}

**Symptom:** Getrackte E-Mail-Links schlagen fehl, aber ungetrackte Links funktionieren, oder Nutzer:innen sehen Zertifikats- oder DNS-Fehler nach dem Klicken.

Häufige Weiterleitungsprobleme resultieren typischerweise aus einer fehlerhaften Konfiguration zwischen dem CDN, das die Tracking-Domain hostet, und den zugehörigen SSL-Zertifikaten oder DNS-CNAME-Einträgen. Diese Fehlkonfigurationen führen häufig dazu, dass Nutzer:innen einen Datenschutzfehler „Verbindung ist nicht sicher“ oder einen `404`-Fehler erhalten, nachdem sie auf einen getrackten E-Mail-Link geklickt haben.

### Anforderungen an die HTML-Link-Formatierung {#html-link-formatting-requirements}

Damit Klick-Tracking funktioniert, muss Ihr E-Mail-Anbieter (SendGrid, SparkPost oder Amazon SES) Links in Ihrem HTML finden und ersetzen können. Bei all diesen Anbietern müssen Links folgende Formatierungsanforderungen erfüllen:

- Links müssen sich in einem HTML-`<a>`-Tag mit einem `href`-Attribut befinden.
- Die URL muss mit `http://` oder `https://` beginnen.

Zusätzliche anbieterspezifische Regeln:

- **SendGrid:** Schließen Sie die URL in einfache oder doppelte Anführungszeichen ein und fügen Sie keine Leerzeichen um das `=` im `href`-Attribut ein.
- **Amazon SES:** URLs müssen [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986) entsprechen. Nicht kodierte Leerzeichen in einer URL verhindern, dass Amazon SES den Link trackt.

Weitere Informationen zu den von Braze unterstützten URL-Schemata für Klick-Tracking finden Sie unter [Anforderungen an Klick-Tracking-Links]({{site.baseurl}}/user_guide/channels/email/email_setup/open_pixel_and_click_tracking#click-tracking-link-requirements). Anbieterspezifische HTML-Details finden Sie unter [SendGrid Klick, der Tracking HTML Best Practices](https://www.twilio.com/docs/sendgrid/ui/analytics-and-reporting/click-tracking-html-best-practices), [SparkPost Template Language](https://developers.sparkpost.com/api/template-language/) und [Amazon SES Email Sending Metrics FAQs](https://docs.aws.amazon.com/ses/latest/dg/faqs-metrics.html).

Gültige Beispiele sind:

```html
<a href="http://www.example.com">Link</a>
<a href='https://example.com'>Link</a>
<a target="_blank" href="https://example.com">Link</a>
```

Die folgenden Beispiele lassen `http://` oder `https://` weg und werden nicht getrackt:

```html
<a href="example.com">Link</a>
<a href="www.example.com">Link</a>
```

Wenn Sie SendGrid verwenden, werden die folgenden Beispiele ebenfalls nicht getrackt:

```html
<a href= http://www.example.com>Link</a>
<a href = "https://example.com">Link</a>
```

{% alert note %}
Obwohl eine `www`-Subdomain optional ist, wird `http://` oder `https://` benötigt, damit Klick-Tracking korrekt funktioniert.
{% endalert %}

### Klick-Tracking testen {#testing-click-tracking}

Nachdem Sie den [Triage-Workflow](#triage-workflow) abgeschlossen haben, verwenden Sie das folgende Template, um die CDN-Konfiguration Ihrer Tracking-Domain zu testen – den Mechanismus, der Analytics für Links in Ihren E-Mails unterstützt.

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

Wenn Ihre ungetrackte URL funktioniert, aber Ihre getrackte URL fehlschlägt, liegt möglicherweise eine Konfigurationslücke vor. Lesen Sie die Dokumentation Ihres jeweiligen E-Mail-Anbieter- und CDN-Anbieters. Detaillierte Anforderungen zur Zertifikatsbereitstellung finden Sie unter [SSL bei Braze]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl).

Verwenden Sie die folgende Tabelle, um häufige Fehler beim Testen des Klick-Trackings zu diagnostizieren.

| Fehlercode | Fehlerbehebung |
| --- | --- |
| `"Your connection is not private" (NET::ERR_CERT_COMMON_NAME_INVALID)` | Führen Sie den [Triage-Workflow](#triage-workflow) durch und lesen Sie [SSL-Namensabweichungsfehler](#ssl-name-mismatch-errors). Überprüfen Sie, ob Ihre Klick-Tracking-Domain im Common Name oder in den Subject Alternative Names des Zertifikats aufgeführt ist. |
| `"This site can't be reached" (DNS_PROBE_FINISHED_NXDOMAIN)` | Überprüfen Sie Ihre DNS-Einstellungen. Stellen Sie sicher, dass Ihre Tracking-Subdomain gemäß der empfohlenen Konfiguration Ihres CDN und E-Mail-Anbieter konfiguriert ist. |
| `525 / 526 SSL Error` | Überprüfen Sie, ob die SSL-Einstellung in Ihrem CDN (z. B. Cloudflare) mit den Fähigkeiten Ihres Origins übereinstimmt. |
| `404 Not Found` | Überprüfen Sie, ob Ihr CDN so konfiguriert ist, dass der gesamte URL-Pfad an den E-Mail-Anbieter weitergeleitet wird, anstatt auf ein leeres Stammverzeichnis zu verweisen. |
| `400 Bad Request: Request Header or Cookie Too Large` | Dieser Fehler tritt typischerweise auf, wenn die Klick-Tracking-Domain zu viele große Cookies von der Domain Ihrer Website erbt. Braze setzt oder blockiert keine Cookies auf der Tracking-Domain. Konfigurieren Sie Ihr CDN so, dass diese Cookies beim Reverse-Proxying der Klick-Tracking-Anfrage nicht an den E-Mail-Anbieter gesendet werden. Möglicherweise müssen Sie auch die Einstellung `large_client_header_buffers` in Ihrer nginx-Konfiguration erhöhen (z. B. `large_client_header_buffers 4 32k;`, um Header bis zu 32&nbsp;KB zuzulassen). Weitere Informationen erhalten Sie von Ihrem CDN-Anbieter oder Ihrem Entwicklerteam. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlercodes und Fehlerbehebung" }