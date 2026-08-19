---
nav_title: "Einrichtung"
article_title: E-Mail-Einrichtung
layout: dev_guide
page_order: 0
guide_top_header: "E-Mail-Einrichtung"
guide_top_text: "Braze kann Ihnen beim Versand von E-Mail-Campaigns helfen. Folgen Sie unseren Anleitungen oder sehen Sie sich unseren <a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>E-Mail-Onboarding</a> Braze-Lernkurs an."
page_type: landing
description: "Diese Landing-Page enthält Ressourcen für den Einstieg in E-Mail-Campaigns, einschließlich der Einrichtung Ihrer IPs und Domains, IP-Warming, E-Mail-Validierung und mehr."
channel: email

guide_featured_title: "Artikel in diesem Abschnitt"
guide_featured_list:
- name: "IPs und Domains einrichten"
  link: /docs/user_guide/channels/email/email_setup/setting_up_ips_and_domains
  image: /assets/img/braze_icons/target-05.svg
- name: "IP-Warming"
  link: /docs/user_guide/channels/email/email_setup/ip_warming
  image: /assets/img/braze_icons/annotation-alert.svg
- name: "E-Mail-Validierung"
  link: /docs/user_guide/channels/email/email_setup/email_validation
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "E-Mail-Authentifizierung"
  link: /docs/user_guide/channels/email/email_setup/authentication
  image: /assets/img/braze_icons/user-square.svg
- name: "Importieren Sie Ihre E-Mail-Liste"
  link: /docs/user_guide/channels/email/email_setup/import_your_email_list
  image: /assets/img/braze_icons/list.svg
- name: "SSL-Übersicht"
  link: /docs/user_guide/channels/email/email_setup/ssl
  image: /assets/img/braze_icons/navigation-pointer-01.svg
- name: "Einverständnis und Adresserfassung"
  link: /docs/user_guide/channels/email/email_setup/consent_and_address_collection
  image: /assets/img/braze_icons/book-closed.svg
- name: "Zustellbarkeitsfallen und Spam-Traps"
  link: /docs/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps
  image: /assets/img/braze_icons/alert-triangle.svg
- name: "Öffnungspixel und Klick-Tracking"
  link: /docs/user_guide/channels/email/email_setup/open_pixel_and_click_tracking
  image: /assets/img/braze_icons/cursor-click-02.svg
- name: "Abo-Status"
  link: /docs/user_guide/audience/subscription_preferences/subscription_status
  image: /assets/img/braze_icons/check-verified-02.svg
---

## Anforderungen {#requirements}

Bevor Sie mit dem Versand von E-Mails beginnen, gibt es einige Dinge, die Sie benötigen. In der folgenden Tabelle erfahren Sie mehr über diese Anforderungen.

| Anforderung | Beschreibung | Quelle |
|---|---|---|
| Eine dedizierte IP (Internet Protocol) | Eine dedizierte IP ist eine eindeutige Internetadresse, die ausschließlich einem einzelnen Hosting-Konto zugewiesen wird. | Braze stellt Ihnen dedizierte IPs zur Verfügung, um die Kontrolle über Ihre Absender-Reputation zu gewährleisten. Das Braze-Onboarding richtet dies für Sie ein. |
| Whitelabel-Domains | Diese bestehen aus einer Domain und einer Subdomain. Durch die Verwendung von Whitelabeling können Sie E-Mail-Authentifizierungsprüfungen für DKIM und SPF bestehen. | Das Braze-Onboarding-Team generiert diese Domains für Sie, aber Sie müssen deren Namen auswählen. |
| Subdomains | Dies ist eine Unterteilung einer Domain (z. B. „@news.company.com“) innerhalb Ihrer E-Mail-Adresse. Eine Subdomain verhindert Fehler, die der offiziellen E-Mail-Reputation Ihres Unternehmens schaden könnten. | Das Onboarding-Team generiert diese für Sie, aber Sie müssen den Namen der Subdomain festlegen. Sie können keine Subdomains verwenden, die derzeit außerhalb von Braze genutzt werden. |
| IP-Pools | Dies ist eine optionale Konfiguration, die dazu dient, die Reputation verschiedener E-Mail-Typen (z. B. „Werbe-E-Mails“ und „Transaktions-E-Mails“) voneinander zu trennen, damit die Reputation des einen Typs den anderen nicht beeinflusst und eine höhere Zustellbarkeit unterstützt wird. | Das Onboarding-Team richtet die Pools für Sie ein. Beim Erstellen Ihrer E-Mail können Sie dann den IP-Pool Ihrer E-Mail im Schritt **Target Audiences** einsehen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Anforderungen" }

## IP-Warming {#ip-warming}

{% alert important %}
IP-Warming ist der **wichtigste Schritt** im E-Mail-Einrichtungsprozess. Obwohl es nicht Ihr erster Schritt ist (es ist tatsächlich der letzte), weisen wir hier darauf hin, damit Sie wissen, dass Sie Ihre IP-Adresse aufwärmen müssen – andernfalls landen Ihre E-Mails im Spam oder unterliegen anderen Zustellungseinschränkungen.
{% endalert %}

[IP-Warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) bedeutet, dass Sie in Ihrem ersten Durchgang eine relativ kleine Anzahl von E-Mails versenden und dann im Laufe der Zeit das Volumen in den folgenden Durchgängen schrittweise erhöhen, bis Sie Ihr übliches tägliches Versandvolumen erreichen. Dies geschieht ganz am Ende Ihres E-Mail-Einrichtungsprozesses.

Indem Sie mit kleineren E-Mail-Volumina beginnen, bauen Sie ein Vertrauensverhältnis zu Ihrem E-Mail-Anbieter auf und zeigen, dass Sie nur E-Mails an relevante Nutzer:innen senden. Wenn Sie Ihren ersten Durchgang an Ihre aktivsten Nutzer:innen senden, können Sie schneller Vertrauen bei Ihrem Anbieter aufbauen.

Nachdem Sie das IP-Warming abgeschlossen haben, können Sie [mit dem Erstellen und Versenden von E-Mails beginnen]({{site.baseurl}}/user_guide/channels/email/html_editor)!

## Gesetzlich vorgeschriebene Transaktions-E-Mails {#legally-required-transactional-emails}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

<br><br>