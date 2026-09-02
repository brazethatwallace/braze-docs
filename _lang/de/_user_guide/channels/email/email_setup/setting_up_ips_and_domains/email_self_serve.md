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

Um die Self-Service-E-Mail-Einrichtung zu nutzen, müssen Sie die folgenden Voraussetzungen erfüllen:

- Sie sind ein:e neue:r Kund:in im Onboarding
- Sie verfügen über die Berechtigung „Edit Domain Settings“ auf Unternehmensebene
- Sie haben einen IP-Pool, IP-Adressen und eine verifizierte Domain

## Hinweise {#considerations}

- Planen Sie eine Versand-Subdomain mit mindestens drei Ebenen. Da Braze eine Subdomain unter Ihrer delegierten Domain erstellt (z. B. „marketing.example.com“), muss Ihre Versand-Domain mindestens drei Ebenen tief sein (z. B. „e.marketing.example.com“).
- Die Versand-Domain muss einer Domain untergeordnet sein, die Ihnen gehört. Wenn Sie beispielsweise „example.com“ besitzen, könnte eine Subdomain „mail.example.com“ sein, sodass Sie die Absenderadresse „@mail.example.com“ verwenden können.
- Es gelten Domain-Limits. Die Gesamtzahl der Tracking-Domains ist auf das 2-Fache der Anzahl verifizierter Domains in Ihrem Vertrag begrenzt. Wenn Sie mehr benötigen, wenden Sie sich an Ihren Account Manager:in.

## Einrichtung {#setup}

### Schritt 1: Versand-Domain hinzufügen {#step-1-add-a-sending-domain}

Ihre Versand-Subdomain ist die Adresse, von der Ihre E-Mails gesendet werden. Sie bestimmt die Absenderadresse, die Ihre Empfänger:innen sehen.

1. Wählen Sie im Bereich **Domains** die Option **Add domain** aus.
2. Fügen Sie Ihre Versand-Domain in die Felder **Mail from** und **Sending domain** für den IP-Pool ein.
    - Die **Mail from**-Adresse (Envelope-Sender oder Return-Path) verarbeitet Bounces im Hintergrund. Ihre Empfänger:innen sehen diese Adresse nicht in einer E-Mail. Sie könnten beispielsweise „bounce“ als Subdomain verwenden, sodass die benutzerdefinierte Mail-from-Adresse „bounce.mail.example.com“ lautet. Die Verwendung dieser Subdomain ist eine Best Practice für die DMARC-SPF-Ausrichtung.
    - Die **Sending domain** ist die Domain in der Absenderadresse, die Empfänger:innen in ihrem Posteingang sehen. Wenn die Absenderadresse beispielsweise „hello@e.mail.example.com“ lautet, ist „e.mail.example.com“ die Versand-Domain.
{: start="3"}
3. Wählen Sie Ihre verifizierte Domain aus dem Dropdown-Menü aus.

Versand-Domains können nach dem Absenden nicht mehr geändert werden. Braze erstellt DNS-Einträge zur Verifizierung und Authentifizierung und fügt sie Ihren DNS-Einstellungen hinzu. Wenn Sie eine Versand-Domain löschen müssen, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Schritt 2: Tracking-Domain hinzufügen {#step-2-add-a-tracking-domain}

Eine Tracking-Domain wird verwendet, um Links in Ihren E-Mails für Klick-Tracking und Branding-Zwecke zu umschließen. Empfänger:innen sehen diese, wenn sie mit der Maus über Links in Ihren E-Mails fahren oder darauf klicken. Sie muss eine Subdomain Ihrer Versand- oder verifizierten Domain sein, damit die DNS-Delegation korrekt funktioniert.

1. Wählen Sie aus, ob Sie eine **Verified domain** oder **Sending domain** als Subdomain für Ihre Tracking-Domain verwenden möchten:
    - Wenn die Tracking-URL aus Gründen der Markenkonsistenz mit der Versand-Domain übereinstimmen soll, wählen Sie **Sending domain**.
    - Wenn Sie eine kürzere Tracking-URL wünschen, wählen Sie die **Verified domain**.

{: start="2"}
2. Geben Sie Ihre Tracking-Subdomain ein. Diese wird der zuvor ausgewählten Subdomain vorangestellt.

Das folgende Beispiel zeigt, wie die Tracking-Domain je nach Auswahl in der E-Mail angezeigt wird:

|  | Auswahl | Tracking-Domain |
| --- | --- | ---|
| Verifizierte Domain | mail.example.com | links.mail.example.com |
| Versand-Domain | marketing.mail.example.com | links.marketing.mail.example.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tracking-Domain nach Auswahl" }

{: start="3"}
3. Wählen Sie die zugehörige verifizierte oder Versand-Subdomain aus dem Dropdown-Menü aus.
4. Wählen Sie **Submit**. Sie können die Versand- und Tracking-Domains mit dem Status **Pending** sehen.

Es kann 5 bis 10 Minuten dauern, bis die DNS-Einträge für Versand-Domains propagiert werden. Wenn Ihre Domain einsatzbereit ist, erhalten Sie eine Benachrichtigungs-E-Mail. DNS-Einträge für Tracking-Domains können bis zu 24 Stunden für die Propagierung benötigen, obwohl es in der Regel weniger dauert. Möglicherweise wird die Versand-Subdomain vor der Tracking-Domain als bereit angezeigt.

### Schritt 3: Workspaces auswählen {#step-3-select-workspaces}

Wählen Sie die Workspaces aus, die Zugriff auf die Domain haben sollen, und wählen Sie dann **Confirm**. Sie können auch festlegen, dass die Versand-Domain automatisch zu neuen Workspaces hinzugefügt wird, wenn diese erstellt werden.

### Schritt 4: Universal Links einrichten (optional) {#step-4-set-up-universal-links-optional}

Universal Links ermöglichen es, dass die Links in Ihren Nachrichten direkt in Ihrer mobilen App statt in einem mobilen Browser geöffnet werden. Braze kann die Zuordnungsdateien auf Ihren Tracking-Domains in Ihrem Auftrag hosten.

{% alert note %}
Universal Links werden pro Tracking-Domain angewendet. Dieselben Dateiinhalte können domainübergreifend geteilt werden, aber jede Domain hostet ihre eigene Kopie.
{% endalert %}

1. Gehen Sie zu **Settings** > **Company Settings** > **Verified Domains** > **Universal Links**.
2. Wählen Sie **Set up universal links**.
3. Geben Sie einen Namen für das Universal-Links-Set ein.
4. Aktivieren Sie die iOS-Konfiguration und fügen Sie Ihre AASA-Datei hinzu. JSON ist der einzige akzeptierte Dateityp. Braze liest die Datei und zeigt die Anzahl der gefundenen App-IDs und Komponenten sowie eine Vorschau der generierten Datei an.
5. Aktivieren Sie die Android-Konfiguration und fügen Sie Ihre Digital-Asset-Links-Datei auf die gleiche Weise hinzu. Braze zeigt die Paketnamen, den SHA-256-Zertifikats-Fingerabdruck und die Anzahl der Anweisungen sowie eine Vorschau an.
6. Überprüfen Sie jede Vorschau, um sicherzustellen, dass die Inhalte korrekt aussehen, und wählen Sie dann **Next: Select tracking domains**. Es werden nur verifizierte Tracking-Domains angezeigt. Ein Set kann auf mehrere Tracking-Domains angewendet werden.
7. Ihr Set erscheint auf der Seite „Universal Links“ zusammen mit seinen Tracking-Domains, Kanälen, iOS-Status, Android-Status und Erstellungsdatum. Braze prüft, ob die AASA-Datei für jede Domain korrekt gehostet wird, und meldet das Ergebnis in der Statusspalte.

### Schritt 5: E-Mail-Versand testen {#step-5-test-your-email-sending}

Nachdem sowohl die Versand- als auch die Tracking-Domains den Status **Ready for use** anzeigen, testen Sie Ihre Einrichtung:

1. Gehen Sie in Ihrem Workspace zu **Settings** > **Email Settings**.
2. Überprüfen Sie, ob die neue Versand-Domain im Bereich **Display Name Address** aufgeführt ist.
3. Fügen Sie eine Absenderadresse mit der neuen Domain hinzu (z. B. „hello@e.mail.example.com“).
4. Wählen Sie **Save**.
5. Erstellen Sie eine Test-E-Mail-Campaign und senden Sie sie an sich selbst. Bestätigen Sie dann, dass:
    - Ihre E-Mail erfolgreich zugestellt wurde.
    - Die Absenderadresse korrekt ist.
    - Klick-Tracking-Links die Tracking-Domain verwenden.
    - Universal Links die App oder Website wie erwartet basierend auf dem Gerät der Empfänger:innen öffnen.
    - E-Mail-Header korrekt angezeigt werden.

## Nächste Schritte {#next-steps}

Nachdem Ihre Absenderverifizierung abgeschlossen ist, empfiehlt Braze IP-Warming, damit Ihre Nachrichten mit einer konstant hohen Rate in den Posteingängen ankommen. Wenden Sie sich nach Abschluss dieser Einrichtung an das Braze-Onboarding-Team, um zu bestätigen, ob Ihre Domains und das [IP-Warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) funktionieren.

## Fehlerbehebung {#troubleshooting}

### Die DNS-Propagierung dauert länger als erwartet {#dns-propagation-is-taking-longer-than-expected}

DNS-Einträge für Versand-Domains werden in der Regel innerhalb von 5 bis 10 Minuten propagiert. DNS-Einträge für Tracking-Domains können je nach TTL-Einstellungen Ihres DNS-Anbieters bis zu 24 Stunden dauern. Wenn die Propagierung länger dauert, überprüfen Sie zunächst, ob die NS-Einträge korrekt hinzugefügt wurden, und wenden Sie sich dann an den Braze-Support.

### Ich kann eine verifizierte Domain nicht entfernen {#im-not-able-to-remove-a-verified-domain}

Verifizierte Domains können nicht direkt im Dashboard entfernt werden, da dies Ihren Versand potenziell beeinträchtigen kann, wenn es nicht ordnungsgemäß überprüft wird. Wenden Sie sich an den Braze-Support, um die Domain aus Ihrem Konto entfernen zu lassen.

### Meine Universal Links öffnen die App nicht {#my-universal-links-arent-opening-the-app}

Überprüfen Sie zunächst die iOS- und Android-Status auf der Seite „Universal Links“. Wenn eine Domain keine gültige Datei hostet, öffnen Sie das Set, korrigieren Sie die Konfiguration und speichern Sie erneut. Wenn die Status in Ordnung aussehen, stellen Sie sicher, dass Sie den Test über einen Link in einer E-Mail auf einem echten Gerät durchführen, anstatt die URL in die Adressleiste des Browsers einzufügen.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Kann Braze mein SSL-Zertifikat ohne NS-Delegation verwalten? {#can-braze-manage-my-ssl-certificate-without-ns-delegation}

Verifizierte Domains erfordern NS-Einträge (Name Server) für die DNS-Eigentumsdelegation an Braze. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="Braze-hosted SSL certificates without NS delegation" %}

### Kann ich stattdessen eine Root-Domain delegieren? {#can-i-delegate-a-root-domain-instead}

Verifizierte Domains sind in erster Linie für die Verwendung mit Subdomains konzipiert und empfohlen. Wir empfehlen nicht, die primäre übergeordnete Domain Ihrer Marke aus Sicherheitsgründen zu delegieren, da Sie die Sichtbarkeit und Kontrolle darüber verlieren. Wenn Sie eine übergeordnete Domain delegieren möchten, verwenden Sie eine übergeordnete Domain, die nirgendwo anders außer bei Braze verwendet wird.

### Warum kann meine verifizierte Domain nicht gleichzeitig die Versand-Domain sein? {#why-cant-my-verified-domain-also-be-the-sending-domain}

Braze kann nur eine Versand-Subdomain unter Ihrer verifizierten Domain erstellen, die in der Regel eine Subdomain der übergeordneten Domain ist (`mail.example.com`). Daher beträgt die Mindesttiefe der Versand-Domain in diesem Fall drei Ebenen (`e.mail.example.com`) anstelle der üblichen zwei Ebenen.

### Was passiert, wenn ich nach der Einrichtung meine NS-Einträge ändere? {#what-happens-if-i-modify-any-of-my-ns-records-after-setup}

Verifizierte Domains sind vollständig von intakten NS-Einträgen abhängig. Wenn Sie Änderungen an Ihren NS-Einträgen vornehmen, kann dies Ihren E-Mail-Versand und Ihr Tracking beeinträchtigen.

### Kann ich nur eine von vier NS-Eintragszeilen hinzufügen, da mein dig-Befehl alle vier Einträge anzeigt? {#can-i-add-only-one-of-four-ns-record-lines-since-my-dig-command-shows-all-four-records}

Bestätigen Sie mit dem `dig`-Befehl, dass alle vier NS-Einträge explizit vorhanden sind und dass die Domain im Dashboard validiert wird, bevor Sie die Einrichtung als abgeschlossen betrachten.