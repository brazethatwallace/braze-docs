---
nav_title: IPs und Domains einrichten
article_title: IPs und Domains einrichten
page_order: 0
page_type: tutorial
channel: email
description: "Dieser Artikel erklärt Ihnen, wie Sie Ihre IPs und Domains für den E-Mail-Versand über Braze einrichten."

---

# IPs und Domains einrichten {#set-up-ips-and-domains}

> Dieser Artikel beschreibt die Voraussetzungen und Schritte, die erforderlich sind, um Ihre IP-Adressen und -Pools sowie die Domains und Subdomains einzurichten, bevor Sie mit dem E-Mail-Versand über Braze beginnen können.

{% multi_lang_include video.html id="iTm3yQkJ0UU" align="right"  %}

<br>

{% alert important %}
Sie können SendGrid, SparkPost oder Amazon Simple Email Service (SES) als E-Mail-Anbieter (ESP) verwenden. Ab 2026 nutzt Braze Amazon SES als Standard-ESP für neue E-Mail-Einrichtungen. Weitere Details finden Sie unter [Amazon SES einrichten]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses).
{% endalert %}

## Methode 1: Abstimmung mit Braze (empfohlen) {#method-1-coordinate-with-braze-recommended}

### Schritt 1: Informationen zusammenstellen {#step-1-outline-information}

Senden Sie die folgenden Informationen an Ihre Braze-Vertretung:

* Ihre gewählten Domains und Subdomains
* Die ungefähre Anzahl der E-Mails, die Sie pro Monat versenden werden, um zu bestimmen, wie viele IPs Sie benötigen
* Wie Sie Ihre Versand-Domains Ihren zugewiesenen IPs zuordnen möchten

### Schritt 2: Braze konfiguriert die Informationen {#step-2-braze-configures-information}

Nachdem wir Ihre E-Mail erhalten haben, beginnen wir mit der Konfiguration Ihrer IPs, Domains und Subdomains sowie IP-Pools.

### Schritt 3: DNS-Einträge hinzufügen {#step-3-add-dns-records}

Nachdem Ihre IPs, Domains, Subdomains und IP-Pools konfiguriert sind, senden wir Ihnen eine Liste mit DNS-Einträgen. Bitten Sie Ihr Entwicklerteam und Ihre Entwickler:innen, diese DNS-Einträge an den entsprechenden Stellen hinzuzufügen, und informieren Sie anschließend das Braze-Onboarding-Team, sobald die Einträge hinzugefügt wurden.

Ausführliche Erklärungen zur Funktionsweise von DNS-Einträgen bei den verschiedenen E-Mail-Anbietern von Braze, einschließlich SPF, DKIM, DMARC und ESP-spezifischer Eintragsstrukturen, finden Sie unter [DNS-Einträge verstehen]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/understanding_dns_records).

{% multi_lang_include channels/email/dns_records.md %}

Nachdem Braze Ihnen Ihre DNS-Einträge bereitgestellt hat, fügen Sie diese hinzu, sobald Ihr DNS- oder IT-Team dazu in der Lage ist. Die Domain-Verifizierung ist zeitlich begrenzt, und wenn Einträge zu spät hinzugefügt werden, kann die Verifizierung fehlschlagen, selbst wenn die DNS-Einträge später korrekt aufgelöst werden. Falls Ihre DNS-Einträge korrekt erscheinen, die Verifizierung aber dennoch fehlschlägt, wenden Sie sich an das Braze-Onboarding- oder Support-Team, um die Verifizierung erneut einzuleiten.

### Nächste Schritte {#next-steps}

Wir überprüfen Ihre Einrichtung und validieren alle Informationen in unseren internen Systemen. Das Braze-Onboarding-Team informiert Sie, sobald alles bereit ist oder ob es Probleme mit Ihren DNS-Einträgen gibt, die Sie mit Ihrem Entwicklerteam klären müssen.

## Methode 2: Self-Service-E-Mail-Einrichtung {#method-2-self-service-email-setup}

Bei dieser Methode werden insgesamt eine Versand-Domain, eine Tracking-Domain und eine IP-Adresse für ein Unternehmen eingerichtet. Wenn Sie mehr einrichten möchten, wenden Sie sich an das Braze-Onboarding-Team (Methode 1).

{% multi_lang_include alerts/early_access_beta_alert.md feature='This self-service email setup feature' type='beta' %}
<br>Wenn Sie das Self-Service-Feature zur E-Mail-Einrichtung verwenden, sollten Sie sich auch mit dem Braze-Onboarding-Team abstimmen.

### Voraussetzungen {#prerequisites}

Um die Self-Service-E-Mail-Einrichtung zu verwenden, müssen die folgenden Voraussetzungen erfüllt sein:

1. Sie sind ein:e neue:r Kund:in im Onboarding.
2. Sie verfügen über die Unternehmensberechtigung „Unternehmenseinstellungen verwalten“.

### Schritt 1: Einrichtung starten {#step-1-begin-setup}

1. Gehen Sie zu **Einstellungen** > **Administratoreinstellungen** unter **Unternehmenseinstellungen**.
2. Wählen Sie dann den Tab **Sender Verification** aus. Um diesen Tab anzuzeigen, benötigen Sie die Unternehmensberechtigung „Unternehmenseinstellungen verwalten“.
3. Wählen Sie **Start setup** aus.

### Schritt 2: Versand-Domain hinzufügen und überprüfen {#step-2-add-and-verify-a-sending-domain}

Eine Versand-Domain wird in der „Von“-Adresse beim Versand einer E-Mail verwendet. Geben Sie eine Versand-Domain ein und klicken Sie auf **Submit**.

Fügen Sie anschließend die TXT- und CNAME-Einträge vom unteren Bereich der Seite bei Ihrem DNS-Anbieter hinzu. Kehren Sie dann zum Braze-Dashboard zurück und klicken Sie auf **Verify**.

![E-Mail-Einrichtungsseite mit TXT- und CNAME-DNS-Einträgen zur Überprüfung einer Versand-Domain.]({% image_buster /assets/img_archive/email_setup_rdns_records.png %})

Wenn die Überprüfung fehlschlägt und Sie der Meinung sind, dass Ihre DNS-Einträge korrekt sind, wenden Sie sich an den Braze Support.

{% alert important %}
Die Versand-Domain muss eine Subdomain einer Domain sein, die Ihnen gehört. Wenn Sie beispielsweise „example.com“ besitzen, könnte eine Subdomain „mail.example.com“ sein, sodass Sie die Absenderadresse „@mail.example.com“ verwenden können.
{% endalert %}

### Schritt 3: Tracking-Domain hinzufügen und überprüfen {#step-3-add-and-verify-a-tracking-domain}

Eine Tracking-Domain wird verwendet, um Links in Ihren E-Mails für Klick-Tracking und Branding-Zwecke zu umschließen. Sie ist für Ihre Nutzer:innen sichtbar, wenn sie mit der Maus über Ihre E-Mail-Links fahren oder darauf klicken. Wir empfehlen, diese an Ihre Versand-Domain anzupassen.

1. Geben Sie eine Tracking-Domain ein und wählen Sie **Submit** aus.
2. Fügen Sie anschließend die CNAME-Einträge vom unteren Bereich der Seite bei Ihrem DNS-Anbieter hinzu.
3. Kehren Sie dann zum Braze-Dashboard zurück und wählen Sie **Verify** aus.

### Schritt 4: IP-Adresse hinzufügen {#step-4-add-an-ip-address}

Braze generiert einen A-Eintrag, um Ihre IP-Adresse mit Ihrer Versand-Subdomain in einer Konfiguration namens Reverse DNS (rDNS) zu verknüpfen. Fügen Sie den A-Eintrag bei Ihrem DNS-Anbieter hinzu und klicken Sie dann auf **Set up rDNS**, um die Zustellbarkeit zu unterstützen.

Beachten Sie, dass zusätzliche Domains, die hinzugefügt wurden, nicht im Bereich **Sender Verification** angezeigt werden. Um weitere Domains hinzuzufügen, wenden Sie sich an das Braze-Support-Team.

### IP-Pools mit mehr als einer dedizierten IP {#ip-pools-with-more-than-one-dedicated-ip}

Wenn ein IP-Pool mehrere dedizierte IP-Adressen enthält, verteilen Braze und Ihr E-Mail-Anbieter große Sendungen auf diese IPs, um Kapazität und Zustellbarkeit zu optimieren. Die Verteilung ist ungefähr – nicht jede Nachricht in einer Campaign verwendet jede IP, und kleinere Sendungen können ungleichmäßig über die Adressen verteilt wirken. SendGrid verarbeitet E-Mails häufig in Blöcken (in der Größenordnung von etwa 1.500 Nachrichten pro Block), sodass das Volumen nicht immer in einem strikten Eins-zu-eins-Verhältnis auf die IPs aufgeteilt wird. Wenn Sie regelmäßig sehr hohe tägliche Volumina versenden, besprechen Sie die Pool-Dimensionierung mit Ihrem Braze-Onboarding- oder Customer-Success-Kontakt.

### Nächste Schritte

Nachdem Ihre Absenderverifizierung abgeschlossen ist, empfehlen wir IP-Warming, damit Ihre Nachrichten mit einer konstant hohen Rate in den Posteingängen ankommen. Stellen Sie nach Abschluss dieser Einrichtung sicher, dass Sie sich auch mit dem Braze-Onboarding-Team abstimmen, um zu bestätigen, dass Ihre Domains und Ihre [IP-Adresse]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) funktionieren.