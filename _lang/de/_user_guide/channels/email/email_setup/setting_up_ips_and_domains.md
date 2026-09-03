---
nav_title: IPs und Domains einrichten
article_title: IPs und Domains einrichten
page_order: 0
page_type: tutorial
channel: email
description: "Dieser Artikel erklärt Ihnen, wie Sie IP-Adressen, IP-Pools, Domains und Subdomains für den E-Mail-Versand über Braze einrichten."
---

# IPs und Domains einrichten {#set-up-ips-and-domains}

> Dieser Artikel beschreibt die Voraussetzungen und Schritte, die erforderlich sind, um Ihre IP-Adressen und -Pools sowie die Domains und Subdomains einzurichten, bevor Sie mit dem E-Mail-Versand über Braze beginnen können.

{% multi_lang_include video.html id="iTm3yQkJ0UU" align="right"  %}

<br>

{% alert important %}
Ab 2026 nutzt Braze Amazon Simple Email Service (SES) als Standard-E-Mail-Anbieter (E-Mail-Anbieter) für neue E-Mail-Einrichtungen. Weitere Details finden Sie unter [Amazon SES einrichten]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses).
{% endalert %}

## Methode 1: Self-Service-E-Mail-Einrichtung {#method-1-self-service-email-setup}

Diese Methode richtet Ihre Versand- und Tracking-Domains für ein Unternehmen ein. Sie müssen sich zunächst an das Braze-Onboarding-Team wenden und die folgenden Informationen an Ihre Braze-Vertretung senden, damit Ihre IP-Pools und IP-Adressen hinzugefügt werden:

- Ihre gewählten Domains und Subdomains
- Die ungefähre Anzahl der E-Mails, die Sie pro Monat versenden, um die benötigte Anzahl an IPs zu bestimmen
- Wie Sie Ihre Versand-Domains Ihren zugewiesenen IP-Pools zuordnen möchten

### Voraussetzungen {#prerequisites}

Um die Self-Service-E-Mail-Einrichtung zu nutzen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllen:

- Sie sind ein:e neue:r Kund:in im Onboarding.
- Sie verfügen über die Berechtigung „Edit Domain Settings“ auf Unternehmensebene.

### Schritt 1: Einrichtung starten {#step-1-begin-setup}

1. Gehen Sie zu **Einstellungen** > **E-Mail-Self-Service** unter **Unternehmenseinstellungen**.
2. Wählen Sie **Einrichtung starten** aus.

### Schritt 2: Versand-Domain hinzufügen und verifizieren {#step-2-add-and-verify-a-sending-domain}

Eine Versand-Domain wird in der „Von“-Adresse beim Versenden einer E-Mail verwendet.

1. Geben Sie eine Versand-Domain ein und wählen Sie **Absenden** aus.
2. Fügen Sie die TXT- und CNAME-Einträge am unteren Rand der Seite bei Ihrem DNS-Anbieter hinzu.

![Abschnitt „DNS-Einträge“ mit TXT- und CNAME-Einträgen zum Kopieren in Ihr Domain-Verwaltungssystem.]({% image_buster /assets/img/email_setup/dns_records.png %})

{: start="3"}
3. Kehren Sie zum Braze-Dashboard zurück und wählen Sie **Verifizieren** aus.

Bitten Sie Ihre Entwickler:innen, diese DNS-Einträge dort hinzuzufügen, wo sie benötigt werden. Ausführliche Erklärungen zur Funktionsweise von DNS-Einträgen bei den E-Mail-Anbietern von Braze, einschließlich SPF, DKIM, DMARC und E-Mail-Anbieter-spezifischer Eintragsstrukturen, finden Sie unter [DNS-Einträge verstehen]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/understanding_dns_records).

{% multi_lang_include channels/email/dns_records.md %}

Wenn die Verifizierung fehlschlägt und Sie sicher sind, dass Ihre DNS-Einträge korrekt sind, wenden Sie sich an den Braze Support.

{% alert important %}
Die Versand-Domain muss einer Domain untergeordnet sein, die Ihnen gehört. Wenn Sie beispielsweise „example.com“ besitzen, könnte eine Subdomain „mail.example.com“ sein, sodass Sie die Absenderadresse „@mail.example.com“ verwenden können.
{% endalert %}

### Schritt 3: Tracking-Domain hinzufügen und verifizieren {#step-3-add-and-verify-a-tracking-domain}

Eine Tracking-Domain wird verwendet, um Links in Ihren E-Mails für Klick-Tracking und Branding-Zwecke zu umschließen. Sie ist für Ihre Empfänger:innen sichtbar, wenn diese mit der Maus über Ihre E-Mail-Links fahren oder darauf klicken. Braze empfiehlt, diese an Ihre Versand-Domain anzupassen.

1. Geben Sie eine Tracking-Domain ein und wählen Sie **Absenden** aus.
2. Fügen Sie die CNAME-Einträge am unteren Rand der Seite bei Ihrem DNS-Anbieter hinzu.
3. Kehren Sie zum Braze-Dashboard zurück und wählen Sie **Verifizieren** aus.

### Schritt 4: IP-Adresse hinzufügen {#step-4-add-an-ip-address}

Braze generiert einen A-Eintrag, um Ihre IP-Adresse mit Ihrer Versand-Subdomain in einer Konfiguration namens Reverse DNS (rDNS) zu verknüpfen. Fügen Sie den A-Eintrag bei Ihrem DNS-Anbieter hinzu und wählen Sie dann **rDNS einrichten** aus, um die Zustellbarkeit zu unterstützen.

Um Ihre IP-Adressen für einen IP-Pool hinzuzufügen oder zu bearbeiten, wenden Sie sich an den Braze Support.

#### IP-Pools mit mehr als einer dedizierten IP {#ip-pools-with-more-than-one-dedicated-ip}

Wenn ein IP-Pool mehrere dedizierte IP-Adressen enthält, verteilen Braze und Ihr E-Mail-Anbieter große Sendungen auf diese IPs, um Kapazität und Zustellbarkeit zu optimieren. Die Verteilung ist ungefähr – nicht jede Nachricht in einer Campaign nutzt jede IP, und kleinere Sendungen können ungleichmäßig über die Adressen verteilt erscheinen. SendGrid verarbeitet E-Mails häufig in Blöcken (in der Größenordnung von etwa 1.500 Nachrichten pro Block), sodass das Volumen nicht immer in einem strikten Eins-zu-eins-Verhältnis auf die IPs aufgeteilt wird. Wenn Sie regelmäßig sehr hohe tägliche Volumina versenden, besprechen Sie die Pool-Dimensionierung mit Ihrem Braze-Onboarding- oder Customer-Success-Kontakt.

### Nächste Schritte {#next-steps}

Nachdem Ihre Absenderverifizierung abgeschlossen ist, empfiehlt Braze IP-Warming, damit Ihre Nachrichten mit einer konstant hohen Rate in den Posteingängen ankommen. Verwenden Sie [automatisiertes IP-Warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming), um Ihren Aufwärmzeitplan einzurichten und zu überwachen.

Wenden Sie sich nach Abschluss dieser Einrichtung an das Braze-Onboarding-Team, um zu bestätigen, ob Ihre Domains und das [IP-Warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) funktionieren.

## Methode 2: Verifizierte Domains {#method-2-verified-domains}

Verifizierte Domains ermöglichen es Ihnen, Braze die Kontrolle über eine bestimmte Subdomain zu übertragen, sodass Braze die E-Mail-Einrichtung und das HTTPS-Klick-Tracking automatisieren kann. Mit DNS-Domain-Delegation verwaltet Braze die DNS-Einträge, die für den E-Mail-Versand und das Klick-Tracking erforderlich sind. Wenn Ihre Subdomain beispielsweise „mail.example.com“ lautet, können Sie sie an Braze delegieren, um Ihre Versand- und Tracking-Domains einzurichten.

{% alert important %}
Verifizierte Domains unterstützen derzeit nur Amazon SES. Wenn Sie SendGrid oder SparkPost verwenden, ist dieses Feature nicht verfügbar.<br><br>Verifizierte Domains werden nur für E-Mail unterstützt. {% multi_lang_include product_feedback_cta.md context="gap" feature="verified domains for channels other than email" %}
{% endalert %}

### Einrichtung {#setup}

#### Schritt 1: Abstimmung mit Braze {#step-1-coordinate-with-braze}

Senden Sie die folgenden Informationen an Ihre Braze-Vertretung:

- Ihre gewählten Domains und Subdomains
- Wie Sie Ihre Domains Ihren IP-Pools zuordnen möchten
- Die ungefähre Anzahl der E-Mails, die Sie pro Monat über jede Subdomain versenden möchten, um die benötigte Anzahl an IPs für Ihre IP-Pools zu bestimmen
- Etwaige frühere Zustellbarkeitsprobleme, die berücksichtigt werden sollten

#### Schritt 2: Braze konfiguriert die Informationen {#step-2-braze-configures-information}

Nach Erhalt Ihrer E-Mail fügt Braze die erwartete Anzahl an IPs und IP-Pools hinzu. Nachdem die IP-Pools und IP-Adressen hinzugefügt wurden, folgen Sie den Schritten unter [Verifizierte Domains]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/verified_domains).