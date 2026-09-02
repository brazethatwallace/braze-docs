---
nav_title: SSL bei Braze
article_title: SSL bei Braze
page_order: 5
page_type: reference
description: "Dieser Referenzartikel behandelt SSL, wofür es verwendet wird und wie es bei Braze eingesetzt wird."
channel: email
---

# SSL bei Braze {#ssl-at-braze}

> Eine SSL-Verschlüsselung (Secure Socket Layer) verschlüsselt eine URL mit HTTPS anstelle von HTTP. HTTPS zeigt an, dass ein gültiges und vertrauenswürdiges SSL- oder TLS-Zertifikat vorhanden ist und dass die Website sicher besucht werden kann.

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

## Warum ist SSL wichtig? {#why-is-ssl-important}

Die meisten Domains erfordern kein SSL, aber Braze empfiehlt aus folgenden Gründen dringend die Verwendung von SSL.

Die Absicherung Ihrer Website und Ihrer Links mit SSL ist eine gängige Praxis, selbst für Unternehmen, die nicht direkt mit sensiblen Kund:inneninformationen umgehen. Nutzer:innen vertrauen eher Links, die mit SSL gesichert sind, und die zusätzliche Authentifizierungsebene hilft, Ihre Daten zu schützen.

### Erforderlich für Klick- und Öffnungs-Tracking {#necessary-for-click-and-open-tracking}

Braze wandelt Ihre Links mithilfe Ihrer gebrandeten Link-Tracking-Subdomain um, um Klicks und Öffnungen zu verfolgen. Standardmäßig beginnen diese Links mit HTTP. Nutzer:innen mit Browsern oder Erweiterungen, die unsicheren Datenverkehr einschränken, können Schwierigkeiten haben, die Weiterleitung zu durchlaufen, bevor die Ziel-URL erreicht wird – selbst wenn die URL sicher ist. Dies kann zu fehlerhaften Bildern und ungenauem Tracking führen. Wenden Sie SSL auf die Link-Tracking-Subdomain an, um sichere Weiterleitungen sicherzustellen.

## Anforderungen {#requirements}

### Browser {#browser}

Wichtige Browser wie Google Chrome schränken den Datenverkehr über unsichere URLs ein, um Nutzer:innen zu schützen. Die Verwendung von SSL hilft dabei, zu bestätigen, dass Inhalte vertrauenswürdig sind, und minimiert Probleme wie defekte Links und Bilder in E-Mails.

### HSTS-Domains {#hsts-domains}

Wenn Sie eine HTTP-Strict-Transport-Security-Domain (HSTS) verwenden, richten Sie SSL ein und konfigurieren Sie ein CDN, um die erforderlichen Sicherheitszertifikate zu senden. Ohne SSL funktionieren Bild- und Web-Links nicht.

## Ein SSL-Zertifikat erwerben {#acquire-an-ssl-certificate}

Erwerben Sie ein SSL-Zertifikat über einen Drittanbieter, in der Regel ein Content Delivery Network (CDN). Ein CDN hostet das Zertifikat und stellt es dem Browser bereit, wenn Nutzer:innen auf einen Link klicken, indem es den Datenverkehr über das CDN umleitet, um Zertifikate anzuwenden, bevor er an SendGrid oder SparkPost weitergeleitet wird.

Um die SSL-Einrichtung zu starten, wenden Sie sich an Ihren CSM, um eine vollständige Braze E-Mail-Einrichtung einzuleiten.

Nachdem Braze die Einrichtung eingeleitet hat, führen Sie die folgenden Schritte aus:

1. Braze stellt DNS-Einträge bereit, die Sie zu Ihrer Domain-Registrierung hinzufügen müssen.
2. Braze überprüft, ob die Einträge korrekt zu Ihrer Registrierung hinzugefügt wurden.
3. Wählen Sie anschließend ein CDN aus und beziehen Sie SSL-Zertifikate von einem Drittanbieter.
4. An diesem Punkt richten Sie Ihr CDN ein. Beachten Sie, dass Braze bei der Fehlerbehebung der CDN-Konfiguration nicht helfen kann. Wenden Sie sich bei weiteren Fragen an Ihren CDN-Anbieter.
5. Kontaktieren Sie Ihren CSM, um SSL aktivieren zu lassen.

## Was ist ein CDN, und warum brauche ich eines? {#what-is-a-cdn-and-why-do-i-need-it}

Ein Content Delivery Network (CDN) ist eine Plattform aus Servern, die schnelle Ladezeiten von Inhalten über verschiedene Medien hinweg sicherstellt und gleichzeitig Sicherheitszertifikate verwaltet.

{% alert important %}
Die CDN-Konfiguration erfolgt immer erst, nachdem Ihre DNS-Einträge von Braze validiert wurden. Falls Sie diesen Schritt noch nicht eingeleitet haben, wenden Sie sich an Ihren CSM, um weitere Informationen zum Einstieg zu erhalten.
{% endalert %}

Für Klick- und Öffnungs-Tracking wandeln Zustellungspartner Links mithilfe einer gebrandeten Subdomain um, und das CDN wendet das SSL-Zertifikat auf diese umgewandelten Links an. Partner müssen häufig gültige Zertifikate im Browser der Empfänger:innen vorlegen, damit Links und Bilder korrekt angezeigt werden. Da Braze keine Zertifikate anfordert oder verwaltet, müssen Sie dies über ein CDN einrichten.

{% alert note %}
Wenn Sie die aufgeführten CDNs nicht für SSL-Klick- und Öffnungs-Tracking verwenden können oder möchten, können Sie eine benutzerdefinierte SSL-Konfiguration einrichten. Alternative CDNs oder benutzerdefinierte Proxys können zu einem komplexeren Setup führen. Weitere Informationen finden Sie in der Dokumentation von [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) und [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/).
{% endalert %}

### Zusätzliche Ressourcen {#additional-resources}

{% alert important %}
Zur Fehlerbehebung Ihrer CDN-Konfiguration wenden Sie sich an Ihren CDN-Anbieter oder lesen Sie den Abschnitt [Fehlerbehebung]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting) für allgemeine Hinweise.
{% endalert %}

In den folgenden Ressourcen der E-Mail-Anbieter-Partner erfahren Sie, wie Sie bestimmte CDNs konfigurieren. Auch wenn Ihr spezifisches CDN möglicherweise nicht aufgeführt ist, müssen Sie sicherstellen, dass Ihr CDN die Möglichkeit bietet, SSL-Zertifikate anzuwenden.

Wenn Sie die Klick-Tracking-Domain Ihres CDNs konfigurieren, aktivieren Sie den `X-Forwarded-Host`-Header, um potenzielle Sicherheitsprobleme wie Host-Header-Angriffe zu vermeiden. Weitere Schritte finden Sie in der CDN-Dokumentation oder bei Ihrem Support-Team.

| Partner | CDN | Dokumentation |
| --- | --- | --- |
| Amazon SES | AWS CloudFront | [Using HTTPS with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) |
| Amazon SES | CloudFlare | [Get started with SSL/TLS](https://developers.cloudflare.com/ssl/get-started/) |
| Amazon SES | Fastly | [Setting up TLS with certificates Fastly manages](https://www.fastly.com/documentation/guides/getting-started/domains/securing-domains/setting-up-tls-with-certificates-fastly-manages/) |
| Amazon SES | KeyCDN | [How to set up custom SSL](https://www.keycdn.com/support/how-to-setup-custom-ssl) |
| Amazon SES | Google Cloud | [Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) |
| SendGrid | AWS CloudFront | [How to configure SSL for Klick, der tracking using CloudFront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront) |
| SendGrid | CloudFlare | [Using CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare) |
| SendGrid | Fastly | [Using Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly) |
| SendGrid | KeyCDN | [Using KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) |
| SparkPost | AWS CloudFront | [Step-by-step guide with AWS CloudFront](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-aws-cloudfront) |
| SparkPost | CloudFlare | [Step-by-step guide with Cloudflare](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-cloudflare) |
| SparkPost | Fastly | [Step-by-step guide with Fastly](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-fastly) |
| SparkPost | Google Cloud Platform | [Step-by-step guide with Google Cloud Platform](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-google-cloud-platform) |
| SparkPost | Microsoft Azure | [Step-by-step guide with Microsoft Azure](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Zusätzliche Ressourcen" }

### Amazon SES

Wenn Sie Amazon SES als Ihren E-Mail-Anbieter verwenden, lesen Sie **Option 2: Configuring an HTTPS domain** in der [Dokumentation von Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) und geben Sie die AWS-Tracking-Domain nach Region basierend auf Ihrem Braze-Cluster an:

- **Braze US-Cluster:** `r.us-east-1.awstrack.me`
- **Braze EU-Cluster:** `r.eu-central-1.awstrack.me`

{% alert important %}
Wenn Sie die Klick-Tracking-Domain Ihres CDNs konfigurieren, aktivieren Sie den `X-Forwarded-Host`-Header, um potenzielle Sicherheitsprobleme wie Host-Header-Angriffe zu vermeiden. Weitere Schritte erfahren Sie bei Ihrem CDN-Anbieter.
{% endalert %}

## Klick- und Open-Tracking-URL-Muster {#click-and-open-tracking-url-patterns}

Ihr E-Mail-Anbieter (E-Mail-Anbieter) schreibt jeden getrackten Link so um, dass er auf Ihre Klick-Tracking-Domain verweist, und fügt dann ein Pfadpräfix hinzu, das die Anfrage als getrackten Klick oder getracktes Öffnen kennzeichnet. Braze erstellt diese Pfade nicht. Ihr E-Mail-Anbieter fügt sie hinzu, wenn er den Link umschreibt. Für CDN- oder Proxy-Regeln, Sicherheits-Allowlists oder die Link-Behandlung in mobilen Apps nutzen Sie die Dokumentation Ihres E-Mail-Anbieter als maßgebliche Quelle.

| E-Mail-Anbieter | Pfadmuster | E-Mail-Anbieter-Dokumentation |
| --- | --- | --- |
| SendGrid | `/wf/click?upn=...` für getrackte Klicks und `/uni/wf/click?upn=...` für Links, die Sie als universelle Links kennzeichnen. Je nach Konfiguration können gebrandete Links auch `/ls/click` (lang signiert) oder `/ss/` (gekürzt) verwenden. | [Universal Links](https://www.twilio.com/docs/sendgrid/ui/sending-email/universal-links) und [gekürzte Links](https://support.sendgrid.com/hc/en-us/articles/44375837088795-How-to-Know-if-my-Links-Are-Shortened-by-SendGrid) |
| SparkPost | `/f/` für getrackte Klicks und `/q/` für getrackte Öffnungen. Links, die einen benutzerdefinierten Pfad über `data-msys-sublink` festlegen, folgen dem Muster `/f/{custom_path}/`. | [Deeplinks](https://docs.sparkpost.com/docs/tech-resources/deep-links-self-serve) |
| Amazon SES | `/CL0/{encodedUrl}/{index}/{messageId}/{hmac}` für getrackte Klicks. Links, die das Attribut `ses:custom-path` festlegen, folgen dem Muster `/CL1/{customPath}/{encodedUrl}/...`. | [Benutzerdefinierte Open- und Klick-Domains](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Klick- und Open-Tracking-URL-Muster nach E-Mail-Anbieter" }

Wenn Ihre Klick-Tracking-Domain beispielsweise `clicks.example.com` ist und Ihr E-Mail-Anbieter SparkPost ist, wird ein getrackter Klick zu einer URL aufgelöst, die mit `https://clicks.example.com/f/` beginnt.

{% alert important %}
Ihr E-Mail-Anbieter besitzt diese Pfadpräfixe und kann sie ändern oder neue hinzufügen. Daher kann Braze keine permanente oder vollständige Liste garantieren. Wenn Ihre Sicherheitstools dies unterstützen, setzen Sie Ihre gesamte Klick-Tracking-Domain auf die Allowlist, anstatt einzelne Pfade freizugeben, und bestätigen Sie die aktuellen Muster in der Dokumentation Ihres E-Mail-Anbieter.
{% endalert %}

Um diese Pfade in Ihrer mobilen App zu behandeln, lesen Sie [Universal Links und App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).

## Fehlerbehebung {#troubleshooting}

Obwohl Sie CDN-Konfiguration, Zertifikate und Proxy-Probleme mit Ihrem CDN klären sollten, können Sie diese Tipps nutzen, um häufige SSL-Klick-Tracking-Probleme zu identifizieren. Hinweise zur Fehlerbehebung finden Sie unter [Fehlerbehebung]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting).