---
nav_title: SSL bei Braze
article_title: SSL-Übersicht
page_order: 5
page_type: reference
description: "Dieser Referenzartikel behandelt SSL, wofür es verwendet wird und wie es bei Braze eingesetzt wird."
channel: email

---

# SSL bei Braze {#ssl-at-braze}

> Eine SSL-Verschlüsselung (Secure Socket Layer) verschlüsselt eine URL mit HTTPS anstelle von HTTP. HTTPS zeigt an, dass ein gültiges und vertrauenswürdiges SSL- oder TLS-Zertifikat vorhanden ist und dass die Website sicher besucht werden kann.

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

## Warum ist SSL wichtig? {#why-is-ssl-important}

Die meisten Domains erfordern kein SSL, jedoch empfiehlt Braze aus den folgenden Gründen dringend die Verwendung von SSL.

Die Sicherung Ihrer Website und Links mit SSL ist eine gängige Praxis, selbst für Unternehmen, die nicht direkt mit sensiblen Kundendaten arbeiten. Nutzer:innen vertrauen Links, die mit SSL gesichert sind, eher, und die zusätzliche Authentifizierungsebene trägt zum Schutz Ihrer Daten bei.

### Erforderlich für das Tracking von Klicks und Öffnungen {#necessary-for-click-and-open-tracking}

Braze transformiert Ihre Links mithilfe Ihrer markenspezifischen Link-Tracking-Subdomain, um Klicks und Öffnungen zu verfolgen. Standardmäßig beginnen diese Links mit HTTP. Nutzer:innen mit Browsern oder Erweiterungen, die nicht sicheren Datenverkehr einschränken, könnten Schwierigkeiten haben, die Weiterleitung vor der Ziel-URL zu passieren, selbst wenn die URL sicher ist. Dies kann zu fehlerhaften Bildern und ungenauem Tracking führen. Wenden Sie SSL auf die Subdomain für das Link-Tracking an, um sichere Weiterleitungen zu gewährleisten.

## Anforderungen {#requirements}

### Browser {#browser}

Große Browser wie Google Chrome schränken den Datenverkehr über unsichere URLs ein, um Nutzer:innen zu schützen. Die Verwendung von SSL hilft sicherzustellen, dass Inhalte als vertrauenswürdig eingestuft werden, und minimiert Probleme wie fehlerhafte Links und Bilder in E-Mails.

### HSTS-Domains {#hsts-domains}

Wenn Sie eine HTTP Strict Transport Security (HSTS)-Domain haben, richten Sie SSL ein und konfigurieren Sie ein CDN, um die erforderlichen Sicherheitszertifikate zu senden. Ohne SSL funktionieren Bild- und Web-Links nicht.

## Ein SSL-Zertifikat erwerben {#acquire-an-ssl-certificate}

Erwerben Sie ein SSL-Zertifikat über einen Drittanbieter, in der Regel ein Content Delivery Network (CDN). Ein CDN hostet das Zertifikat und stellt es dem Browser bereit, wenn ein:e Nutzer:in auf einen Link klickt, indem der Datenverkehr über das CDN umgeleitet wird, um Zertifikate anzuwenden, bevor er an SendGrid oder SparkPost weitergeleitet wird.

Um die SSL-Einrichtung zu starten, kontaktieren Sie Ihren Braze Customer-Success-Manager, um eine vollständige Braze-E-Mail-Einrichtung einzuleiten.

Nachdem Braze die Einrichtung eingeleitet hat, folgen Sie diesen Schritten:

1. Braze stellt DNS-Einträge bereit, die Sie zu Ihrer Domain-Registrierung hinzufügen müssen.
2. Braze überprüft, ob die Einträge korrekt zu Ihrer Registrierung hinzugefügt wurden.
3. Danach wählen Sie ein CDN aus und erhalten SSL-Zertifikate von einem Drittanbieter.
4. An diesem Punkt richten Sie Ihr CDN ein. Beachten Sie, dass Braze bei der Fehlerbehebung der CDN-Konfiguration nicht helfen kann. Kontaktieren Sie Ihren CDN-Anbieter für weitere Unterstützung.
5. Kontaktieren Sie Ihren Customer-Success-Manager, um SSL aktivieren zu lassen.

## Was ist ein CDN und warum brauche ich es? {#what-is-a-cdn-and-why-do-i-need-it}

Ein Content Delivery Network (CDN) ist eine Plattform aus Servern, die schnelle Ladezeiten von Inhalten über verschiedene Medien hinweg sicherstellt und gleichzeitig Sicherheitszertifikate verwaltet.

{% alert important %}
Die CDN-Konfiguration erfolgt immer erst, nachdem Ihre DNS-Einträge von Braze validiert wurden. Wenn Sie diesen Schritt noch nicht eingeleitet haben, kontaktieren Sie Ihren Customer-Success-Manager für weitere Informationen zum Einstieg.
{% endalert %}

Für das Klick- und Öffnungs-Tracking transformieren Zustellungspartner Links mithilfe einer markenspezifischen Subdomain, und das CDN wendet das SSL-Zertifikat auf diese transformierten Links an. Partner müssen dem Browser der Empfänger:innen häufig gültige Zertifikate vorlegen, damit Links und Bilder korrekt angezeigt werden. Da Braze keine Zertifikate anfordert oder verwaltet, müssen Sie dies über ein CDN einrichten.

{% alert note %}
Wenn Sie die aufgeführten CDNs nicht für SSL-Klick- und Öffnungs-Tracking verwenden können oder möchten, können Sie eine angepasste SSL-Konfiguration einrichten. Alternative CDNs oder angepasste Proxys können zu einer komplexeren Einrichtung führen. Weitere Informationen finden Sie in der Dokumentation von [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) und [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/).
{% endalert %}

### Zusätzliche Ressourcen {#additional-resources}

{% alert important %}
Kontaktieren Sie bei der Fehlerbehebung Ihrer CDN-Konfiguration Ihren CDN-Anbieter oder lesen Sie die [Fehlerbehebung]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting/) für allgemeine Hinweise.
{% endalert %}

Sehen Sie sich die folgenden Ressourcen der ESP-Partner an, um bestimmte CDNs zu konfigurieren. Auch wenn Ihr spezifisches CDN möglicherweise nicht aufgeführt ist, müssen Sie sicherstellen, dass Ihr CDN die Möglichkeit hat, SSL-Zertifikate anzuwenden.

Wenn Sie die Klick-Tracking-Domain Ihres CDN konfigurieren, aktivieren Sie den `X-Forwarded-Host`-Header, um potenzielle Sicherheitsprobleme wie Host-Header-Angriffe zu verhindern. Weitere Schritte finden Sie in der CDN-Dokumentation oder bei Ihrem Support-Team.

| Partner | CDN | Dokumentation |
| --- | --- | --- |
| Amazon SES | AWS CloudFront | [Using HTTPS with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) |
| Amazon SES | CloudFlare | [Get started with SSL/TLS](https://developers.cloudflare.com/ssl/get-started/) |
| Amazon SES | Fastly | [Setting up TLS with certificates Fastly manages](https://www.fastly.com/documentation/guides/getting-started/domains/securing-domains/setting-up-tls-with-certificates-fastly-manages/) |
| Amazon SES | KeyCDN | [How to set up custom SSL](https://www.keycdn.com/support/how-to-setup-custom-ssl) |
| Amazon SES | Google Cloud | [Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) |
| SendGrid | AWS CloudFront | [How to configure SSL for click tracking using CloudFront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront) |
| SendGrid | CloudFlare | [Using CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare) |
| SendGrid | Fastly | [Using Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly) |
| SendGrid | KeyCDN | [Using KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) |
| SparkPost | AWS CloudFront | [Step-by-step guide with AWS CloudFront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront) |
| SparkPost | CloudFlare | [Step-by-step guide with Cloudflare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare) |
| SparkPost | Fastly | [Step-by-step guide with Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly) |
| SparkPost | Google Cloud Platform | [Step-by-step guide with Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform) |
| SparkPost | Microsoft Azure | [Step-by-step guide with Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Zusätzliche Ressourcen" }

### Amazon SES

Wenn Sie Amazon SES als Ihren ESP verwenden, lesen Sie **Option 2: Configuring an HTTPS domain** in der [Dokumentation von Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) und geben Sie die AWS-Tracking-Domain nach Region basierend auf Ihrem Braze-Cluster an:

- **Braze US-Cluster:** `r.us-east-1.awstrack.me`
- **Braze EU-Cluster:** `r.eu-central-1.awstrack.me`

{% alert important %}
Wenn Sie die Klick-Tracking-Domain Ihres CDN konfigurieren, aktivieren Sie den `X-Forwarded-Host`-Header, um potenzielle Sicherheitsprobleme wie Host-Header-Angriffe zu verhindern. Weitere Schritte finden Sie bei Ihrem CDN-Anbieter.
{% endalert %}

## Fehlerbehebung {#troubleshooting}

Obwohl Sie die CDN-Konfiguration, Zertifikate und Proxy-Probleme mit Ihrem CDN-Anbieter klären sollten, können Ihnen diese Tipps helfen, häufige SSL-Klick-Tracking-Probleme zu identifizieren. Hinweise zur Fehlerbehebung finden Sie unter [Fehlerbehebung]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting/).