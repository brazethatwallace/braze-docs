---
nav_title: E-Mail-Self-Service
article_title: E-Mail-Self-Service
page_order: 0
page_type: tutorial
channel: email
description: "Dieser Artikel beschreibt, wie Sie Versand- und Tracking-Domains mit dem E-Mail-Self-Service in Braze einrichten."
toc_headers: h2
---

# E-Mail-Self-Service {#email-self-serve}

> Auf dieser Seite erfahren Sie, wie Sie Versand- und Tracking-Domains in Braze einrichten, damit Ihre Absender-Domain und Tracking-Links dieselbe Subdomain verwenden.

## Voraussetzungen {#prerequisites}

Um die Self-Service-E-Mail-Einrichtung zu verwenden, müssen Sie die folgenden Voraussetzungen erfüllen:

- Neue:r Kund:in im Onboarding sein
- Über die Unternehmensberechtigung „Edit Domain Settings“ verfügen
- Über einen IP-Pool, IP-Adressen und eine verifizierte Domain verfügen

## Überlegungen {#considerations}

- Planen Sie eine Sende-Subdomain mit mindestens drei Ebenen. Da Braze eine Subdomain unter Ihrer delegierten Domain erstellt (z. B. „marketing.example.com“), muss Ihre Sende-Domain mindestens drei Ebenen tief sein (z. B. „e.marketing.example.com“).
- Die Sende-Domain muss einer Domain untergeordnet sein, die Ihnen gehört. Wenn Sie beispielsweise „example.com“ besitzen, könnte eine Subdomain „mail.example.com“ sein, sodass Sie die Sendeadresse „@mail.example.com“ verwenden können.
- Es gelten Domain-Beschränkungen. Die Gesamtanzahl der Tracking-Domains ist auf das 2-Fache der Anzahl verifizierter Domains in Ihrem Vertrag begrenzt. Wenn Sie mehr benötigen, wenden Sie sich an Ihren Account Manager.

## Einrichtung {#setup}

### Schritt 1: Eine Versanddomain hinzufügen {#step-1-add-a-sending-domain}

Ihre Versand-Subdomain ist die Adresse, von der aus Ihre E-Mails gesendet werden. Sie bestimmt die „Von“-Adresse, die Ihre Empfänger:innen sehen.

1. Wählen Sie im Abschnitt **Domains** die Option **Add domain** aus.
2. Fügen Sie Ihre Versanddomain in den Feldern **Mail from** und **Sending domain** für den IP-Pool hinzu.
    - Die **Mail from**-Adresse (Envelope-Sender oder Return-Path) verarbeitet Bounces im Hintergrund. Ihre Empfänger:innen sehen diese nicht in einer E-Mail. Sie könnten beispielsweise „bounce“ als Subdomain verwenden, sodass die benutzerdefinierte Mail-from-Adresse „bounce.mail.example.com“ lautet. Die Verwendung dieser Subdomain ist eine Best Practice für DMARC-SPF-Alignment.
    - Die **Sending domain** ist die Domain in der Von-Adresse, die Empfänger:innen in ihrem Posteingang sehen. Wenn die Von-Adresse beispielsweise „hello@e.mail.example.com“ lautet, dann ist „e.mail.example.com“ die Versanddomain.
{: start="3"}
3. Wählen Sie Ihre verifizierte Domain aus dem Dropdown-Menü aus.

Versanddomains können nach dem Absenden nicht mehr geändert werden. Braze erstellt DNS-Einträge zur Verifizierung und Authentifizierung und fügt sie Ihren DNS-Einstellungen hinzu. Wenn Sie eine Versanddomain löschen müssen, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Schritt 2: Eine Tracking-Domain hinzufügen {#step-2-add-a-tracking-domain}

Eine Tracking-Domain wird verwendet, um Links in Ihren E-Mails für Klick-Tracking und Branding-Zwecke zu umschließen. Empfänger:innen sehen diese, wenn sie mit der Maus über Links in Ihren E-Mails fahren oder darauf klicken. Sie muss eine Subdomain Ihrer Versand- oder verifizierten Domain sein, damit die DNS-Delegation ordnungsgemäß funktioniert.

1. Wählen Sie aus, ob Sie eine **Verified domain** oder eine **Sending domain** als Subdomain für Ihre Tracking-Domain verwenden möchten:
    - Wenn die Tracking-URL mit der Versanddomain übereinstimmen soll, um Markenkonsistenz zu gewährleisten, wählen Sie **Sending domain**.
    - Wenn Sie eine kürzere Tracking-URL möchten, wählen Sie die **Verified domain**.

{: start="2"}
2. Geben Sie Ihre Tracking-Subdomain ein. Diese wird der zuvor ausgewählten Subdomain vorangestellt.

Das folgende Beispiel zeigt, wie die Tracking-Domain in der E-Mail basierend auf Ihrer Auswahl angezeigt wird:

|  | Auswahl | Tracking-Domain |
| --- | --- | ---|
| Verifizierte Domain | mail.example.com | links.mail.example.com |
| Versanddomain | marketing.mail.example.com | links.marketing.mail.example.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tracking-Domain nach Auswahl" }

{: start="3"}
3. Wählen Sie die zugehörige verifizierte oder Versand-Subdomain aus dem Dropdown-Menü aus.
4. Wählen Sie **Submit**. Sie können die Versand- und Tracking-Domains mit dem Status **Pending** sehen.

Es kann 5 bis 10 Minuten dauern, bis die DNS-Einträge für Versanddomains propagiert werden. Wenn Ihre Domain einsatzbereit ist, erhalten Sie eine Benachrichtigungs-E-Mail. DNS-Einträge für Tracking-Domains können bis zu 24 Stunden für die Propagierung benötigen, obwohl es in der Regel weniger dauert. Möglicherweise wird die Versand-Subdomain vor der Tracking-Domain einsatzbereit.

### Schritt 3: Workspaces auswählen {#step-3-select-workspaces}

Wählen Sie die Workspaces aus, die Zugriff auf die Domain haben sollen, und wählen Sie dann **Confirm**. Sie können auch festlegen, dass die Versanddomain automatisch zu neuen Workspaces hinzugefügt wird, wenn diese erstellt werden.

### Schritt 4: Universal Links einrichten (optional) {#step-4-set-up-universal-links-optional}

Universal Links ermöglichen es, dass die Links in Ihren Nachrichten direkt in Ihrer mobilen App statt in einem mobilen Browser geöffnet werden. Braze kann die Zuordnungsdateien in Ihrem Namen auf Ihren Tracking-Domains hosten.

{% alert note %}
Universal Links werden pro Tracking-Domain angewendet. Dieselben Dateiinhalte können domainübergreifend geteilt werden, aber jede Domain hostet ihre eigene Kopie.
{% endalert %}

1. Gehen Sie zu **Settings** > **Company Settings** > **Verified Domains** > **Universal Links**.
2. Wählen Sie **Set up universal links**.
3. Geben Sie einen Namen für das Universal-Links-Set ein.
4. Aktivieren Sie die iOS-Konfiguration und fügen Sie Ihre AASA-Datei hinzu. JSON ist der einzige akzeptierte Dateityp. Braze liest die Datei und zeigt die Anzahl der gefundenen App-IDs und Komponenten sowie eine Vorschau der generierten Datei an.
5. Aktivieren Sie die Android-Konfiguration und fügen Sie Ihre Digital-Asset-Links-Datei auf die gleiche Weise hinzu. Braze zeigt die Paketnamen, den SHA-256-Zertifikat-Fingerprint und die Anzahl der Anweisungen sowie eine Vorschau an.
6. Überprüfen Sie jede Vorschau, um sicherzustellen, dass die Inhalte korrekt aussehen, und wählen Sie dann **Next: Select tracking domains**. Es werden nur verifizierte Tracking-Domains angezeigt. Ein Set kann auf mehrere Tracking-Domains angewendet werden.
7. Ihr Set erscheint auf der Seite „Universal Links“ zusammen mit seinen Tracking-Domains, Kanälen, dem iOS-Status, dem Android-Status und dem Erstellungsdatum. Braze prüft, ob die AASA-Datei für jede Domain ordnungsgemäß gehostet wird, und gibt das Ergebnis in der Statusspalte an.

### Schritt 5: Ihren E-Mail-Versand testen {#step-5-test-your-email-sending}

Nachdem sowohl die Versand- als auch die Tracking-Domains den Status **Ready for use** anzeigen, testen Sie Ihre Einrichtung:

1. Gehen Sie in Ihrem Workspace zu **Settings** > **Email Settings**.
2. Überprüfen Sie, ob die neue Versanddomain im Abschnitt **Display Name Address** aufgeführt ist.
3. Fügen Sie eine Von-Adresse mit der neuen Domain hinzu (zum Beispiel „hello@e.mail.example.com“).
4. Wählen Sie **Save**.
5. Erstellen Sie eine Test-E-Mail-Campaign und senden Sie sie an sich selbst. Bestätigen Sie dann, dass:
    - Ihre E-Mail erfolgreich zugestellt wurde.
    - Die Von-Adresse korrekt ist.
    - Klick-Tracking-Links die Tracking-Domain verwenden.
    - Universal Links die App oder Website wie erwartet öffnen, abhängig vom Gerät der Empfänger:innen.
    - E-Mail-Header korrekt angezeigt werden.

## Nächste Schritte {#next-steps}

Nachdem Ihre Sender-Verifizierung abgeschlossen ist, empfiehlt Braze das [IP-Warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming), damit Ihre Nachrichten mit einer gleichbleibend hohen Rate in den Posteingängen ankommen.

Wenden Sie sich nach Abschluss dieser Einrichtung an das Braze-Onboarding-Team, um zu bestätigen, dass Ihre Domains und das IP-Warming ordnungsgemäß funktionieren.

## Fehlerbehebung {#troubleshooting}

### DNS-Propagierung dauert länger als erwartet {#dns-propagation-is-taking-longer-than-expected}

Einträge für Versand-Domains werden in der Regel innerhalb von 5 bis 10 Minuten propagiert. Einträge für Tracking-Domains können je nach den TTL-Einstellungen Ihres DNS-Anbieters bis zu 24 Stunden dauern. Falls die Propagierung länger dauert, überprüfen Sie zunächst, ob die NS-Einträge korrekt hinzugefügt wurden, und wenden Sie sich dann an den Braze-Support.

### Ich kann eine verifizierte Domain nicht entfernen {#im-not-able-to-remove-a-verified-domain}

Verifizierte Domains können nicht direkt im Dashboard entfernt werden, da dies Ihren Versand potenziell beeinträchtigen kann, wenn es nicht ordnungsgemäß geprüft wurde. Wenden Sie sich an den Braze-Support, um die Domain aus Ihrem Konto entfernen zu lassen.

### Meine Universal Links öffnen die App nicht {#my-universal-links-arent-opening-the-app}

Überprüfen Sie zunächst die iOS- und Android-Status auf der Seite „Universal Links“. Falls eine Domain keine gültige Datei hostet, öffnen Sie den Satz, korrigieren Sie die Konfiguration und speichern Sie erneut. Falls die Status in Ordnung aussehen, stellen Sie sicher, dass Sie den Test über einen Link in einer E-Mail auf einem echten Gerät durchführen, anstatt die URL in die Adressleiste des Browsers einzufügen.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Kann Braze mein SSL-Zertifikat ohne NS-Delegation verwalten? {#can-braze-manage-my-ssl-certificate-without-ns-delegation}

Verifizierte Domains erfordern NS-Einträge (Name Server) für die DNS-Eigentumsdelegation an Braze. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="Braze-hosted SSL certificates without NS delegation" %}

### Kann ich stattdessen eine Root-Domain delegieren? {#can-i-delegate-a-root-domain-instead}

Verifizierte Domains sind in erster Linie für die Verwendung mit Subdomains konzipiert und empfohlen. Wir empfehlen nicht, die primäre übergeordnete Domain Ihrer Marke aus Sicherheitsgründen zu delegieren, da Sie die Transparenz und Kontrolle darüber verlieren. Wenn Sie eine übergeordnete Domain delegieren möchten, verwenden Sie eine übergeordnete Domain, die nirgendwo anders außer bei Braze verwendet wird.

### Warum kann meine verifizierte Domain nicht gleichzeitig die Sende-Domain sein? {#why-cant-my-verified-domain-also-be-the-sending-domain}

Braze kann nur eine Sende-Subdomain unter Ihrer verifizierten Domain erstellen, die in der Regel eine Subdomain der übergeordneten Domain ist (`mail.example.com`). Daher beträgt die Mindesttiefe der Sende-Domain in diesem Fall drei Ebenen (`e.mail.example.com`) statt der üblichen zwei Ebenen.

### Was passiert, wenn ich nach der Einrichtung einen meiner NS-Einträge ändere? {#what-happens-if-i-modify-any-of-my-ns-records-after-setup}

Verifizierte Domains sind vollständig davon abhängig, dass die NS-Einträge intakt sind. Wenn Sie Änderungen an Ihren NS-Einträgen vornehmen, kann dies Ihren E-Mail-Versand und Ihr Tracking beeinträchtigen.

### Kann ich nur eine der vier NS-Eintragszeilen hinzufügen, da mein dig-Befehl alle vier Einträge anzeigt? {#can-i-add-only-one-of-four-ns-record-lines-since-my-dig-command-shows-all-four-records}

Bestätigen Sie mit dem `dig`-Befehl, dass alle vier NS-Einträge explizit vorhanden sind, und stellen Sie sicher, dass die Domain im Dashboard validiert wird, bevor Sie die Einrichtung als abgeschlossen betrachten.