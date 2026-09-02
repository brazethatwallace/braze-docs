---
nav_title: "Senderüberprüfung"
article_title: "Senderüberprüfung"
permalink: /sender_verification/
description: "Dieser Artikel beschreibt, wie Sie die Senderüberprüfung einrichten und Ihre eigenen Subdomains an Braze delegieren."
hidden: true
---

# Senderüberprüfung {#sender-verification}

> Diese Seite beschreibt, wie Sie Ihre eigenen Subdomains an Braze delegieren. Verwenden Sie die Senderüberprüfung, um die Kontrolle über eine dedizierte Versand-Subdomain einzurichten und an Braze zu delegieren – so erreichen Sie eine stärkere Markenkonsistenz, da Ihre Absender-Domain und Tracking-Links unter derselben Subdomain liegen.

{% alert important %}
Dieses Feature befindet sich in der Beta-Phase und ist nur für interne Braze-Teams verfügbar.
{% endalert %}

## So funktioniert die Senderüberprüfung {#how-sender-verification-works}

Domain-Delegation ist eine DNS-Einrichtungsoption, mit der Sie die Kontrolle über eine bestimmte Versand-Subdomain an Braze delegieren können. Wenn Sie beispielsweise „marketing.example.com“ als Ihre Subdomain verwenden, verwaltet Braze die für Messaging-Features erforderlichen DNS-Einträge, z. B. für E-Mail.

### Vorteile {#benefits}

Die Senderüberprüfung vereinfacht die Einrichtung und Wartung. Braze erstellt und aktualisiert alles Notwendige, wodurch weniger Möglichkeiten für DNS-Fehlkonfigurationen bestehen.

### Hinweise {#considerations}

- Wählen Sie eine dedizierte Subdomain.
- Nach Abschluss der Domain-Delegation verwaltet Braze Ihre DNS-Einträge für die delegierte Subdomain.
- Wenn Sie mehrere Marken oder Braze-Workspaces haben, können Sie eine delegierte Subdomain pro Marke auswählen.
- Es gibt ein Limit von 50 Versand-Domains und 50 Tracking-Domains für die Senderüberprüfung. Wenn Sie mehr hinzufügen müssen, wenden Sie sich bitte an das Braze-Support-Team.

## 1. Schritt: Voraussetzungen erfüllen {#step-1-complete-prerequisites}

Gehen Sie im Braze-Dashboard zu **Einstellungen** > **Senderüberprüfung** unter **Unternehmenseinstellungen** und arbeiten Sie mit Ihrer Onboarding-Manager:in:in zusammen, um die folgenden Voraussetzungen zu erfüllen:

- Einen IP-Pool hinzufügen
- IP-Adressen hinzufügen
- Eine delegierte Domain hinzufügen und den NS-Eintrag überprüfen

## 2. Schritt: Versand-Subdomain hinzufügen {#step-2-add-your-sending-subdomain}

1. Wählen Sie im Abschnitt **Sending domains** die Option **Add sending domain** aus.
2. Geben Sie in den Feldern **Mail from** und **Sending domain** Ihre Versand-Subdomain für den IP-Pool ein. Ein Beispiel ist „marketing.mail.example.com“.
3. Wählen Sie Ihre delegierte Domain aus dem Dropdown aus.
4. Wählen Sie dann **Submit** aus.

![Formular mit Feldern für die Mail-from-Adresse und die Versand-Domain, mit einem Dropdown für die delegierte Domain und einem Submit-Button.]({% image_buster /assets/unlisted_docs/img/sender_verification/sending_subdomain.png %}){: style="max-width:85%;"}

Es dauert 5 bis 10 Minuten, bis die DNS-Einträge propagiert sind. Danach erhalten Sie eine Benachrichtigungs-E-Mail, dass Ihre Domain einsatzbereit ist.

{% alert important %}
Domains können nach dem Absenden nicht mehr geändert werden. Braze erstellt DNS-Einträge für die Überprüfung und Authentifizierung und fügt sie Ihren DNS-Einstellungen hinzu.
{% endalert %}

## 3. Schritt: Tracking-Subdomain hinzufügen {#step-3-add-your-tracking-subdomain}

Nachdem Sie eine Subdomain erstellt und überprüft haben:

1. Wählen Sie **Add tracking domain** aus.
2. Geben Sie die Tracking-Subdomain ein. Wenn Ihre Tracking-Subdomain beispielsweise „Klick, der“ ist, lautet Ihre Subdomain: „Klick, der.marketing.mail.example.com“.
3. Wählen Sie die zugehörige Versand-Domain aus dem Dropdown aus.
4. Wählen Sie dann **Submit** aus.

![Ein Beispiel für eine hinzuzufügende Tracking-Domain.]({% image_buster /assets/unlisted_docs/img/sender_verification/tracking_domain.png %}){: style="max-width:85%;"}

Es kann bis zu 24 Stunden dauern, bis diese DNS-Einträge propagiert sind, in der Regel geht es jedoch schneller. Danach erhalten Sie eine Benachrichtigungs-E-Mail, dass Ihre Domain einsatzbereit ist.

{% alert important %}
Die Tracking-Domain muss eine Subdomain der Versand-Domain sein, damit die DNS-Delegation ordnungsgemäß funktioniert.
{% endalert %}

## 4. Schritt: Workspaces auswählen {#step-4-select-the-workspaces}

Wählen Sie als Nächstes die Workspaces aus, die Zugriff auf die Domain haben sollen, und wählen Sie **Confirm** aus. Optional können Sie eine Versand-Domain automatisch zu neuen Workspaces hinzufügen, wenn diese erstellt werden.

![Dialog mit Kontrollkästchen zur Workspace-Auswahl mit der Option, die Versand-Domain automatisch zu neuen Workspaces hinzuzufügen, und einem Confirm-Button.]({% image_buster /assets/unlisted_docs/img/sender_verification/select_workspaces_domain.png %}){: style="max-width:85%;"}

## 5. Schritt: E-Mail-Versand testen {#step-5-test-your-email-sending}

Wenn die Versand- und Tracking-Domains den Status **Ready for use** haben, können Sie den E-Mail-Versand wie folgt testen:

1. Gehen Sie in Ihrem Workspace zu **Einstellungen** > **E-Mail-Einstellungen**.
2. Überprüfen Sie, ob die neue Versand-Domain im Abschnitt **Display Name Address** aufgeführt ist.
3. Fügen Sie die E-Mail-Adresse mit der neuen Domain hinzu (z. B. „marketing@marketing.mail.example.com“).
4. Wählen Sie **Save** aus.
5. Erstellen Sie als Nächstes eine Test-E-Mail-Campaign und senden Sie sich selbst eine E-Mail, um Folgendes zu bestätigen:
- Ihre E-Mail wurde erfolgreich zugestellt.
- Die Absenderadresse ist korrekt.
- Der Klick-Tracking-Link verwendet die Tracking-Domain.
- Ihre E-Mail-Header werden korrekt angezeigt.