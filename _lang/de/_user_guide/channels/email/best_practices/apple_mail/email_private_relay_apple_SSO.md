---
nav_title: E-Mails an Apple Private Relay senden
article_title: E-Mails an Apple Private Relay senden
alias: /email_relay/
page_order: 0
description: "Dieser Artikel beschreibt den Vorgang des Versendens von E-Mails an Apple Private Relay."
channel:
  - email
toc_headers: h2
---

# E-Mails an Apple Private Relay senden {#send-emails-to-apple-private-relay}

> Das Single Sign-on (Single Sign-on)-Feature von Apple erlaubt es Nutzer:innen, ihre E-Mail-Adressen (`example@icloud.com`) zu teilen oder ihre E-Mail-Adressen auszublenden, indem anstelle der persönlichen E-Mail-Adresse eine maskierte Adresse (`tq1234snin@privaterelay.appleid.com`) an Marken weitergegeben wird. Apple leitet dann die an die Relay-Adressen gesendeten Nachrichten an die tatsächliche E-Mail-Adresse der Nutzer:innen weiter.

Um E-Mails an das private E-Mail-Relay von Apple zu senden, Registrieren Sie Ihre Versanddomains bei Apple. Wenn Sie Ihre Domains nicht bei Apple konfigurieren, führen E-Mails an Relay-Adressen zu Bounces.

Wenn Nutzer:innen beschließen, die E-Mail-Weiterleitung an die Relay-E-Mail Ihrer App zu deaktivieren, erhält Braze wie gewohnt die Bounce-Informationen. Diese Nutzer:innen können Apps, die „Mit Apple anmelden“ verwenden, über die Einstellungsseite ihrer Apple-ID verwalten (siehe [Dokumentation von Apple](https://support.apple.com/en-us/HT210426)).

## E-Mail-Anbieter konfigurieren {#configure-your-email-provider}

{% tabs %}
{% tab SendGrid %}

Wenn Sie SendGrid als E-Mail-Anbieter verwenden, können Sie E-Mails an Apple senden, ohne DNS-Änderungen vorzunehmen.

1. Melden Sie sich beim [Apple Developer Portal](https://developer.apple.com/) an.
2. Gehen Sie zur Seite **Certificates, Identifiers & Profiles**.
3. Wählen Sie **Services** > **Sign in with Apple for Email Communication** aus.
4. Fügen Sie im Bereich **Email Sources** die Domains und Subdomains hinzu.
- Die Adresse sollte folgendes Format haben: `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>` (ein Beispiel ist: `bounces+1234567@braze.online.docs.com`).

Wenn Ihre gewünschte „Von“-Adresse eine `abmail`-Adresse ist, nehmen Sie diese in Ihre Subdomain auf. Verwenden Sie zum Beispiel `abmail.docs.braze.com` statt `docs.braze.com`.

{% endtab %}
{% tab SparkPost %}

Um Apple Private Relay für SparkPost einzurichten, führen Sie die folgenden Schritte aus:

1. Melden Sie sich bei Apple an.
2. Folgen Sie der [Apple-Dokumentation](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service), um die E-Mail-Domains zu registrieren.
3. Apple prüft die Domains automatisch, zeigt an, welche verifiziert sind, und bietet die Möglichkeit, die Domains erneut zu verifizieren oder zu löschen.

### Wenn die Versanddomain gleichzeitig die Bounce-Domain ist {#when-the-sending-domain-is-also-the-bounce-domain}

Wenn eine Versanddomain auch als Bounce-Domain verwendet wird, können Sie keine Einträge speichern und müssen die folgenden zusätzlichen Schritte ausführen:

1. Wenn die Domain bereits auf SparkPost verifiziert wurde, **müssen** Sie MX- und TXT-Einträge erstellen:

| Instanz | MX-Eintrag                   | TXT-Eintrag                                    |
|---------|------------------------------|-------------------------------------------------|
| US      | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| EU      | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Wenn die Versanddomain gleichzeitig die Bounce-Domain ist" }

{% alert important %}
Um SPF-Fehler zu vermeiden, müssen Sie die MX- und TXT-Einträge erstellen und im DNS propagieren lassen, **bevor** Sie den CNAME-Eintrag löschen.
{% endalert %}

{:start="2"}
2. Löschen Sie den CNAME-Eintrag.
3. Ersetzen Sie ihn durch die MX- und TXT-Einträge für die korrekte Weiterleitung.
4. Erstellen Sie Ihren A-Eintrag, der auf Ihr CDN oder Ihr Datei-Hosting verweist.

{% endtab %}
{% tab Amazon SES %}

Um Apple Private Relay einzurichten, sollten Sie idealerweise eine benutzerdefinierte MAIL FROM-Domain eingerichtet haben.

1. Melden Sie sich bei Apple an.
2. Folgen Sie der [Apple-Dokumentation](https://developer.apple.com/help/account/capabilities/configure-private-email-relay-service), um die E-Mail-Domains zu registrieren.

{% alert important %}
Stellen Sie sicher, dass Ihr DKIM/SPF mit dem übereinstimmt, was Sie gemäß den verlinkten Anweisungen registrieren.
{% endalert %}

{:start="3"}
3. Apple prüft die Domains automatisch, zeigt an, welche verifiziert sind, und bietet die Möglichkeit, die Domains erneut zu verifizieren oder zu löschen.

{% endtab %}
{% endtabs %}

Wenn Sie weitere Fragen haben, eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support).