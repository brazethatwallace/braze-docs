---
nav_title: E-Mail-Präferenzen
article_title: E-Mail-Präferenzen
page_type: reference
page_order: 2
description: "Dieser Referenzartikel behandelt E-Mail-Präferenzen im Braze-Dashboard, einschließlich Sendekonfigurationen, Open-Tracking-Pixel, Abo-Seiten und -Fußzeilen und mehr."
tool: Dashboard
channel: email
alias: /email_preferences/
toc_headers: h2

---

# E-Mail-Präferenzen {#email-preferences}

> Unter E-Mail-Präferenzen können Sie spezifische Einstellungen für ausgehende E-Mails festlegen, wie angepasste Fußzeilen, angepasste Opt-in- und Opt-out-Seiten und mehr. Die Einbindung dieser Optionen in Ihre ausgehenden E-Mails sorgt für ein nahtloses und einheitliches Erlebnis für Ihre Nutzer:innen.

**E-Mail-Präferenzen** finden Sie im Dashboard unter **Einstellungen** > **Workspace-Einstellungen**.

## Sendekonfiguration {#sending-configuration}

Die E-Mail-Einstellungen im Abschnitt **Sendekonfiguration** bestimmen, welche Details in Ihren E-Mail-Campaigns enthalten sind. Diese Einstellungen beziehen sich insbesondere darauf, was Ihre Nutzer:innen sehen, wenn sie eine E-Mail von Braze erhalten.

### Einstellungen für ausgehende E-Mails {#outbound-email-settings}

Wenn Sie Ihre E-Mail-Einstellungen konfigurieren, legen die Einstellungen für ausgehende E-Mails fest, welche Namen und E-Mail-Adressen verwendet werden, wenn Braze E-Mails an Ihre Nutzer:innen sendet.

Wenn Sie eine neue Domain oder einen neuen IP-Pool (Sendeanbieter) zu Ihrem Workspace hinzufügen oder aus der verfügbaren Liste entfernen möchten, wenden Sie sich an Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in.

{% tabs local %}
{% tab Anzeigename und Adresse %}

In diesem Abschnitt können Sie die Namen und E-Mail-Adressen hinzufügen, die Sie verwenden können, wenn Braze E-Mails an Ihre Nutzer:innen sendet. Die Anzeigenamen und E-Mail-Adressen stehen in den **Absenderinformationen** zur Verfügung, wenn Sie Ihre E-Mail-Campaign erstellen. Beachten Sie, dass Änderungen an den Einstellungen für ausgehende E-Mails keine rückwirkende Auswirkung auf bestehende Sendungen haben.

![Abschnitt „Einstellungen für ausgehende E-Mails“ mit Feldern für verschiedene Anzeigenamen und Domains.]({% image_buster /assets/img/email_settings/display_name_address.png %})

{% alert note %}
Apple-Mail-Clients erkennen das `@`-Symbol nicht, wenn es in einem benutzerdefinierten Anzeigenamen verwendet wird. Verschiedene Postfach-Anbieter steuern, wie die Anzeigenamen-Adresse für ihre Nutzer:innen angezeigt wird, sodass der Anzeigename je nach E-Mail-Client unterschiedlich erscheinen kann.
{% endalert %}

#### Mit Liquid personalisieren {#personalize-with-liquid}

Sie können auch [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) in den Feldern **Absender-Anzeigename**, **Lokaler Teil** und **Domain** verwenden, um den Absendernamen und die E-Mail-Adresse dynamisch auf Basis angepasster Attribute zu erstellen. Beachten Sie, dass Sie zur Verwendung von Liquid im Feld **Domain** zu den **Absenderinformationen** einer E-Mail-Campaign navigieren und das Kontrollkästchen **Absender-Anzeigename + Adresse anpassen** aktivieren müssen.

![Sendeeinstellungen mit Feldern zum Anpassen des Absender-Anzeigenamens, der Adresse und der Domain.]({% image_buster /assets/img/email_settings/email_campaign_domain.png %})

Zum Beispiel können Sie bedingte Logik verwenden, um von verschiedenen Marken oder Regionen aus zu senden:

{% raw %}
```liquid
{% if ${language} == 'en' %}
English Display Name
{% elsif ${language} == 'de' %}
German Display Name
{% else %}
Default to English Display Name
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab Antwortadresse %}

Wenn Sie in diesem Abschnitt eine E-Mail-Adresse hinzufügen, können Sie diese als Antwortadresse für Ihre E-Mail-Campaign auswählen. Sie können eine E-Mail-Adresse auch als Standard festlegen, indem Sie **Als Standard festlegen** auswählen. Diese E-Mail-Adressen stehen in den **Absenderinformationen** zur Verfügung, wenn Sie Ihre E-Mail-Campaign erstellen.

![Abschnitt „Antwortadresse“ mit Feldern zur Eingabe mehrerer Antwortadressen.]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

{% alert note %}
Braze-Sendedomains akzeptieren keine eingehenden E-Mails. Wenn ein:e Empfänger:in auf eine E-Mail antwortet, die von einer in Braze konfigurierten Sendedomain gesendet wurde, wird die Antwort mit dem Fehler `550 5.7.1 relaying denied` zurückgewiesen. Die Antwortadresse muss nicht dieselbe Domain wie die Absenderadresse verwenden. Wenn Sie Antworten empfangen müssen – beispielsweise um Bestätigungen für Kalendereinladungen zu sammeln – verwenden Sie eine Subdomain, die nicht für den Versand konfiguriert ist und über ein Postfach zum Empfang von E-Mails verfügt.
{% endalert %}

#### Mit Liquid personalisieren

Sie können auch [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) im Feld **Antwortadresse** verwenden, um die Antwortadresse dynamisch auf Basis angepasster Attribute zu erstellen. Zum Beispiel können Sie bedingte Logik verwenden, um Antworten an verschiedene Regionen oder Abteilungen zu senden:

{% raw %}
```liquid
{% if {{custom_attribute.${region}}} == 'US' %}
{% assign address = "us-support@example.com" %}
{% elsif {{custom_attribute.${region}}} == 'EU' %}
{% assign address = "eu-support@example.com" %}
{% else %}
{% assign address = "global-support@example.com" %}{% endif %}{{address}}
```
{% endraw %}

{% alert tip %}
Wenn Sie einen Content-Block verwenden, um die **Antwortadresse** zu befüllen, stellen Sie sicher, dass der final gerenderte Wert eine gültige E-Mail-Adresse ist und ein `@` enthält. Braze kann dies beim Speichern der Einstellung nicht validieren, da der endgültige Wert erst zum Sendezeitpunkt bekannt ist.

- Wenn Ihr Content-Block den lokalen Teil (den Text vor `@`) und die Domain separat speichert, erstellen Sie das Feld als eine Adresse (zum Beispiel {% raw %}`{{content_blocks.${reply_to_local}}}@{{content_blocks.${reply_to_domain}}}`{% endraw %}).
{% endalert %}

{% endtab %}
{% tab BCC or Banner-Content-Card-Adresse %}

In diesem Abschnitt können Sie BCC or Banner-Content-Card-Adressen verwalten, die Sie an ausgehende E-Mail-Nachrichten anhängen können, die von Braze gesendet werden. Wenn Sie einer E-Mail-Nachricht eine BCC or Banner-Content-Card-Adresse hinzufügen, wird eine identische Kopie der Nachricht, die Ihre Nutzer:innen erhalten, an Ihr BCC or Banner-Content-Card-Postfach gesendet. Dies ist ein nützliches Tool, um Kopien von Nachrichten aufzubewahren, die Sie an Ihre Nutzer:innen gesendet haben – etwa für Compliance-Anforderungen oder Kundenservice-Angelegenheiten. BCC or Banner-Content-Card-E-Mails sind nicht in den E-Mail-Berichten und Analytics enthalten.

BCC or Banner-Content-Card-Adressen sind für Amazon SES, SendGrid und SparkPost verfügbar. Als Alternative zu BCC or Banner-Content-Card-Adressen empfehlen wir die Verwendung der [Nachrichtenarchivierung]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving), um eine Kopie von Nachrichten zu speichern, die zu Archivierungs- oder Compliance-Zwecken an Nutzer:innen gesendet wurden.

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

Nachdem Sie eine Adresse hinzugefügt haben, steht die Adresse zur Auswahl bereit, wenn Sie eine E-Mail in Campaigns oder Canvas-Schritten erstellen. Wählen Sie **Als Standard festlegen** neben einer Adresse, um diese Adresse standardmäßig beim Starten einer neuen E-Mail-Campaign oder Canvas-Komponente auszuwählen. Um dies auf Nachrichtenebene zu überschreiben, können Sie beim Einrichten Ihrer Nachricht **Kein BCC or Banner-Content-Card** auswählen.

Wenn alle E-Mail-Nachrichten, die von Braze gesendet werden, eine BCC or Banner-Content-Card-Adresse enthalten sollen, können Sie die Option **BCC or Banner-Content-Card-Adresse für alle Ihre E-Mail-Campaigns erforderlich** umschalten. Dadurch müssen Sie eine Standardadresse auswählen, die automatisch für neue E-Mail-Campaigns oder Canvas-Schritte ausgewählt wird. Die Standardadresse wird auch automatisch allen Nachrichten hinzugefügt, die über unsere Representational State Transfer API ausgelöst werden. Es ist nicht erforderlich, die bestehende API-Anfrage zu ändern, um die Adresse einzuschließen.

#### Dynamisches BCC or Banner-Content-Card {#dynamic-bcc}

Mit dynamischem BCC or Banner-Content-Card können Sie Liquid in Ihrer BCC or Banner-Content-Card-Adresse verwenden. Beachten Sie, dass dieses Feature nur in den **E-Mail-Präferenzen** verfügbar ist und nicht in der Campaign selbst festgelegt werden kann. Nur eine BCC or Banner-Content-Card-Adresse pro E-Mail-Empfänger:in ist zulässig.

Zum Beispiel können Sie {% raw %}`{{custom_attribute.${support_agent}}}`{% endraw %} als BCC or Banner-Content-Card-Adresse für E-Mails Ihres Support-Teams hinzufügen.

![BCC-Adresse-Abschnitt des Tabs „E-Mail-Einstellungen“ mit einer BCC-Adresse, die Liquid verwendet.]({% image_buster /assets/img/email_settings/dynamic_bcc.png %}){: style="max-width:90%;" }

{% endtab %}
{% endtabs %}

## Tracking-Pixel für Öffnungen {#open-tracking-pixel}

[![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

Das Tracking-Pixel für E-Mail-Öffnungen ist ein unsichtbares 1 x 1&nbsp;px großes Bild und wird automatisch in Ihr E-Mail-HTML eingefügt. Dieses Pixel hilft Braze zu erkennen, ob Ihre Nutzer:innen Ihre E-Mail geöffnet haben. Wenn der E-Mail-Client einer Nutzerin oder eines Nutzers eine Anfrage an unser Tracking-Pixel sendet, kann die Anfrage Informationen wie die IP-Adresse, den User Agent und den Zeitstempel enthalten. Informationen zu E-Mail-Öffnungen können sehr nützlich sein und helfen Ihnen, effektive Marketingstrategien zu ermitteln, indem Sie die entsprechenden Öffnungsraten analysieren.

### Platzierung {#placement}

Das Standardverhalten in Braze besteht darin, das Tracking-Pixel am Ende Ihrer E-Mail anzufügen, in der Regel in einem `<body>`-Tag. Für die meisten Nutzer:innen ist dies der ideale Ort für das Pixel.

Obwohl das Pixel bereits so gestylt ist, dass es möglichst wenige visuelle Änderungen verursacht, wären unbeabsichtigte visuelle Änderungen am Ende einer E-Mail am wenigsten sichtbar. Dies ist auch der Standard bei E-Mail-Anbietern wie SendGrid und SparkPost.

Um unerwartetes Verhalten zu vermeiden, sollten Sie Liquid innerhalb von `<html>`-Tags verwenden. Verschachtelte oder doppelte Tags auf Dokumentebene können beeinflussen, wie die E-Mail geparst wird und wo das Pixel platziert wird, was das Öffnungs-Tracking und das Layout beeinträchtigen kann. Weitere Informationen finden Sie unter [Liquid verwenden]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid).

### Platzierung Update or aktualisieren or aktualisieren {#update-the-placement}

Braze unterstützt derzeit die Möglichkeit, die standardmäßige Platzierung des Öffnungs-Tracking-Pixels des E-Mail-Anbieter or ESP (das letzte Tag im `<body>` einer E-Mail) zu überschreiben und es an das erste Tag im `<body>` zu verschieben.

![Bereich „Open Tracking Pixel“ mit den Optionen zum Verschieben für SendGrid, SparkPost oder Amazon SES.]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

So ändern Sie die Platzierung:

1. Gehen Sie in Braze zu **Einstellungen** > **Workspace-Einstellungen** > **E-Mail-Einstellungen**.
2. Wählen Sie eine der folgenden Optionen aus: **Move for SendGrid**, **Move for SparkPost** oder **Move for Amazon SES**
3. Wählen Sie **Speichern** aus.

Nach dem Speichern sendet Braze spezielle Anweisungen an den E-Mail-Anbieter or ESP, um das Öffnungs-Tracking-Pixel am Anfang aller HTML-E-Mails zu platzieren.

{% alert important %}
Die SSL-Aktivierung umschließt die URL des Tracking-Pixels mit HTTPS anstelle von HTTP. Wenn Ihr SSL falsch konfiguriert ist, kann dies die Wirksamkeit des Tracking-Pixels beeinträchtigen.
{% endalert %}

{% alert important %}
Klick-Tracking gilt nur für Links, die mit `http://` oder `https://` beginnen. `mailto:`-Links (z. B. `mailto:support@example.com`) werden nicht für das Tracking umgeschrieben.
{% endalert %}

## List-Unsubscribe-Header {#list-unsubscribe}

{% alert note %}
Seit dem 15. Juni 2026 fügt Braze den Mailto-Header nicht mehr in E-Mails ein, wenn der One-Klick, der or klicken-List-Unsubscribe-Header so konfiguriert ist, dass er auf eine bestimmte Abo-Gruppe beschränkt ist. Nutzer:innen, die sich über den List-Unsubscribe-Header abmelden, werden nur von dieser bestimmten Abo-Gruppe abgemeldet, nicht global.
{% endalert %}

Die Verwendung eines List-Unsubscribe-Headers ermöglicht es Ihren Empfänger:innen, sich einfach von Marketing-E-Mails abzumelden, indem ein **Unsubscribe**-Button in der Postfach-Oberfläche angezeigt wird, und nicht im Nachrichtentext.

Testsendungen enthalten in der Regel keine List-Unsubscribe-Header. Ob der Live-Header angezeigt wird, liegt beim Postfach-Anbieter und ist reputationsbasiert – eine stärkere Absender-Reputation verbessert in der Regel die Sichtbarkeit.

![E-Mail-Client-Postfach-Oberfläche mit einer Abmeldeoption neben der Nachricht, wobei List-Unsubscribe außerhalb des Nachrichtentexts erscheint.]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

Wenn eine Empfängerin oder ein Empfänger **Unsubscribe** auswählt, sendet der Postfach-Anbieter die Abmeldeanfrage an das im E-Mail-Header definierte Ziel.

Die Aktivierung von List-Unsubscribe ist eine Best Practice für die Zustellbarkeit und eine Anforderung bei einigen der führenden Postfach-Anbieter. Sie ermutigt Endnutzer:innen, sich sicher von unerwünschten Nachrichten abzumelden, anstatt den Spam-Button in einem E-Mail-Client zu drücken, was sich nachteilig auf die Absender-Reputation und die E-Mail-Zustellbarkeit auswirkt.

Beim [Verwalten Ihrer Abos in Gmail](https://support.google.com/mail/answer/15621070?sjid=2292320204527911296-NC) kann Gmail auch den Abmeldelink aus dem Nachrichtentext übernehmen, priorisiert jedoch den List-Unsubscribe, wenn er im Header vorhanden ist.

### Entfernt das Deaktivieren des List-Unsubscribe-Headers den Gmail-Abmelde-Button? {#does-turning-off-the-list-unsubscribe-header-remove-the-gmail-unsubscribe-button}

Nein. Das Deaktivieren der Braze-List-Unsubscribe-Header-Einstellung entfernt den `List-Unsubscribe`-Header aus den von Braze gesendeten Nachrichten, steuert jedoch nicht, ob Gmail eine **Unsubscribe**-Option in der Postfach-Oberfläche anzeigt. Wie im vorherigen Abschnitt erwähnt, kann Gmail weiterhin eine Abmeldeoption aus Links im Nachrichtentext anzeigen oder andere Anbieterlogik verwenden. Ob der Header in der Rohnachricht erscheint, ist unabhängig davon, ob Gmail den Empfänger:innen eine Abmeldeoption anzeigt. Weitere Informationen finden Sie in den [FAQ zu Gmails E-Mail-Absenderrichtlinien](https://support.google.com/a/answer/14229414).

### Unterstützung durch Postfach-Anbieter {#mailbox-provider-support}

Die folgende Tabelle fasst die Unterstützung der Postfach-Anbieter für den „mailto:“-Header, die List-Unsubscribe-URL und die One-Klick, der or klicken-Abmeldung ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) zusammen.

| List-Unsubscribe-Header | Mailto:-Header | List-Unsubscribe-URL | One-Klick, der or klicken-Abmeldung (RFC 8058) |
| ----- | --- | --- | --- |
| Gmail | Unterstützt* | Unterstützt | Unterstützt |
| Gmail Mobile | Nicht unterstützt | Nicht unterstützt | Nicht unterstützt |
| Apple Mail | Unterstützt | Nicht unterstützt | Nicht unterstützt |
| Outlook.com | Unterstützt | Nicht unterstützt | Nicht unterstützt |
| Yahoo! Mail | Unterstützt* | Nicht unterstützt | Unterstützt |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Unterstützung durch Postfach-Anbieter" }

_*Yahoo und Gmail stellen den „mailto:“-Header schrittweise ein und werden nur noch One-Klick, der or klicken unterstützen._

Ob der Header angezeigt wird, entscheidet letztlich der Postfach-Anbieter. Um zu prüfen, ob der List-Unsubscribe-Header in der Roh-E-Mail (Text) für die Empfängerin oder den Empfänger in Gmail enthalten ist, gehen Sie wie folgt vor:

1. Wählen Sie **Show Original** in der E-Mail. Dies öffnet einen neuen Tab mit der Rohversion der E-Mail und ihren Headern.
2. Suchen Sie nach „List-Unsubscribe“. Bei der One-Klick, der or klicken-Abmeldung fügen viele Anbieter auch einen „List-Unsubscribe-Post“-Header hinzu. Bestätigen Sie, dass beide in der Rohnachricht erscheinen, wenn Sie erwarten, dass One-Klick, der or klicken verfügbar ist.

Wenn der Header in der Rohversion der E-Mail vorhanden ist, aber nicht angezeigt wird, hat der Postfach-Anbieter entschieden, die Abmeldeoption nicht anzuzeigen, was bedeutet, dass wir keine weiteren Erkenntnisse darüber haben, warum der Postfach-Anbieter den Header nicht anzeigt. Die Anzeige des List-Unsubscribe-Headers ist letztlich reputationsbasiert. In den meisten Fällen gilt: Je besser Ihre Absender-Reputation beim Postfach-Anbieter ist, desto wahrscheinlicher wird der List-Unsubscribe-Header angezeigt.

### E-Mail-Abmelde-Header in Workspaces {#email-unsubscribe-header-in-workspaces}

![Auswahl von „Nutzer:innen, die abonniert oder angemeldet sind“ für den Versand.]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Wenn das Feature für den E-Mail-Abmelde-Header aktiviert ist, gilt diese Einstellung für den gesamten Workspace, nicht auf Unternehmensebene. Sie wird zu Campaigns und Canvase hinzugefügt, die so konfiguriert sind, dass sie an Nutzer:innen gesendet werden, die abonniert oder angemeldet sind, oder an angemeldete Nutzer:innen im Schritt **Target Audience** der Campaign- und Canvas-Builder.

Bei Verwendung des „Workspace-Standards“ fügt Braze den One-Klick, der or klicken-Abmelde-Header nicht für Campaigns hinzu, die als transaktional gelten und so konfiguriert sind, dass sie „an alle Nutzer:innen, einschließlich abgemeldeter Nutzer:innen“ gesendet werden. Um dies zu überschreiben und den One-Klick, der or klicken-Abmelde-Header beim Senden an abgemeldete Nutzer:innen hinzuzufügen, können Sie **Unsubscribe globally from all emails** in den One-Klick, der or klicken-List-Unsubscribe-Einstellungen auf Nachrichtenebene auswählen.

### Standard-List-Unsubscribe-Header {#default-list-unsubscribe-header}

{% alert important %}
Gmail beabsichtigt, dass Absender die One-Klick, der or klicken-Abmeldung für alle ihre ausgehenden kommerziellen und werblichen Nachrichten ab dem 1. Juni 2024 implementieren. Weitere Informationen finden Sie in den [Gmail-Absenderrichtlinien](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) und den [FAQ zu Gmails E-Mail-Absenderrichtlinien](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages). Yahoo hat einen Zeitplan für Anfang 2024 für die aktualisierten Anforderungen angekündigt. Weitere Informationen finden Sie unter [More Secure, Less Spam: Enforcing Email Standards for a Better Experience](https://blog.postmaster.yahooinc.com/).
{% endalert %}

Um die Braze-Abmeldefunktion zur direkten Verarbeitung von Abmeldungen zu verwenden, wählen Sie **Include a one-Klick, der or klicken list-unsubscribe (mailto and HTTP) email header for emails sent to subscribed or opted-in users** und wählen Sie **Braze default** als Standard-Braze-URL und Mail-to.

![Option zum automatischen Einschließen eines List-Unsubscribe-Headers für E-Mails an abonnierte oder angemeldete Nutzer:innen.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Braze unterstützt die folgenden Versionen des List-Unsubscribe-Headers:

| List-Unsubscribe-Version | Beschreibung |
| ----- | --- |
| One-Klick, der or klicken (RFC 8058) | Bietet Empfänger:innen eine unkomplizierte Möglichkeit, sich mit einem einzigen Klick von E-Mails abzumelden. Dies ist eine Anforderung von Yahoo und Gmail für Massenversender. |
| List-Unsubscribe-URL oder HTTPS | Stellt Empfänger:innen einen Link bereit, der sie zu einer Webseite weiterleitet, auf der sie sich abmelden können. |
| Mailto | Gibt eine E-Mail-Adresse als Ziel für die Abmeldeanfrage an, die von der Empfängerin oder dem Empfänger an die Marke gesendet wird. <br><br> _Zur Verarbeitung von Mailto-List-Unsubscribe-Anfragen müssen solche Abmeldeanfragen die in Braze gespeicherte E-Mail-Adresse der Endnutzerin oder des Endnutzers enthalten, die bzw. der sich abmeldet. Diese kann durch die „Absenderadresse“ der E-Mail, von der aus sich die Endnutzerin oder der Endnutzer abmeldet, den codierten Betreff oder den codierten Text der empfangenen E-Mail bereitgestellt werden. In sehr seltenen Fällen halten sich einige Postfach-Anbieter nicht an das [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368)-Protokoll, was dazu führt, dass die E-Mail-Adresse nicht korrekt übergeben wird. Dies kann dazu führen, dass eine Abmeldeanfrage in Braze nicht verarbeitet werden kann._ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Standard-List-Unsubscribe-Header" }

Wenn Braze eine List-Unsubscribe-Anfrage von einer Nutzerin oder einem Nutzer über eine der [Standard-List-Unsubscribe-Header](#default-list-unsubscribe-header)-Methoden erhält, wird der globale E-Mail-Abo-Status dieser Person auf „Abgemeldet“ gesetzt. Wenn keine Übereinstimmung vorliegt, verarbeitet Braze diese Anfrage nicht.

### One-Klick, der or klicken-Abmeldung {#one-click-unsubscribe}

Die Verwendung der One-Klick, der or klicken-Abmeldung für den List-Unsubscribe-Header ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) konzentriert sich darauf, Empfänger:innen eine einfache Möglichkeit zu bieten, sich von E-Mails abzumelden.

### One-Klick, der or klicken-List-Unsubscribe auf Nachrichtenebene {#message-level-one-click-list-unsubscribe}

Die Einstellung für One-Klick, der or klicken-List-Unsubscribe auf Nachrichtenebene überschreibt das für Workspaces festgelegte E-Mail-Abmelde-Header-Feature. Wenden Sie das One-Klick, der or klicken-Abmeldeverhalten pro Campaign oder Canvas-Schritt für die folgenden Anwendungsfälle an:

- Fügen Sie eine Braze-One-Klick, der or klicken-Abmeldung für eine bestimmte Abo-Gruppe hinzu, um mehrere Marken/Listen innerhalb eines Workspace zu unterstützen
- Wechseln Sie zwischen der Standard-Braze-Abmeldung oder einer angepassten URL
- Fügen Sie Ihre angepasste One-Klick, der or klicken-Abmelde-URL hinzu
- Lassen Sie die One-Klick, der or klicken-Abmeldung für diese Nachricht weg

{% alert note %}
Die Einstellung für One-Klick, der or klicken-List-Unsubscribe auf Nachrichtenebene ist nur bei Verwendung des Drag-and-Drop-Editors und des aktualisierten HTML-Editors verfügbar. Wenn Sie den vorherigen HTML-Editor verwenden, wechseln Sie zum aktualisierten HTML-Editor, um dieses Feature zu nutzen.
{% endalert %}

Gehen Sie in Ihrem E-Mail-Editor zu **Sending Settings** > **Sending Info**. Wählen Sie aus den folgenden Optionen:

- **Use workspace default**: Verwendet die in den **E-Mail-Präferenzen** festgelegten Einstellungen für den **E-Mail-Abmelde-Header**. Alle Änderungen an dieser Einstellung gelten für alle Nachrichten.
- **Unsubscribe globally from all emails**: Verwendet den Braze-Standard-One-Klick, der or klicken-Abmelde-Header. Nutzer:innen, die den Abmelde-Button klicken, erhalten den globalen E-Mail-Abo-Status „Abgemeldet“.
- **Unsubscribe from specific subscription group**: Verwendet die angegebene Abo-Gruppe. Braze meldet Nutzer:innen, die den Abmelde-Button klicken, von der ausgewählten Abo-Gruppe ab.
    - Wenn Sie eine Abo-Gruppe auswählen, fügen Sie den Filter **Subscription Group** unter **Target Audiences** hinzu, um nur Nutzer:innen anzusprechen, die diese bestimmte Gruppe abonniert haben. Die für die One-Klick, der or klicken-Abmeldung ausgewählte Abo-Gruppe muss mit der Abo-Gruppe übereinstimmen, die Sie ansprechen. Bei einer Nichtübereinstimmung der Abo-Gruppe riskieren Sie, an Nutzer:innen zu senden, die versuchen, sich von einer Abo-Gruppe abzumelden, von der sie bereits abgemeldet sind.

{% alert important %}
Die Einstellung **Unsubscribe from specific subscription group** gilt nur für den One-Klick, der or klicken-List-Unsubscribe-Header. Der Mailto-List-Unsubscribe-Header wird bei Auswahl dieser Option nicht beeinflusst. Das bedeutet, dass eine Empfängerin oder ein Empfänger, die bzw. der sich über diese Methode abmeldet, eine globale Abmeldung protokolliert, nicht eine Abmeldung von der bestimmten Abo-Gruppe. Um den Mailto-List-Unsubscribe-Header von der globalen Abmeldung von Nutzer:innen auszuschließen, wenden Sie sich bei Auswahl dieser Einstellung an den [Support]({{site.baseurl}}/support_contact).
{% endalert %}

- **Custom**: Fügt Ihre angepasste One-Klick, der or klicken-Abmelde-URL hinzu, damit Sie Abmeldungen direkt verarbeiten können.
- **Exclude unsubscribe**

{% alert important %}
Das Ausschließen der One-Klick, der or klicken-Abmeldung oder jeglicher Abmeldemechanismen sollte nur für transaktionale Nachrichten erfolgen, wie Passwortzurücksetzungen, Quittungen und Bestätigungs-E-Mails.
{% endalert %}

Das Anpassen dieser Einstellung überschreibt das Standardverhalten für die One-Klick, der or klicken-List-Unsubscribe in dieser E-Mail.

![Sendeeinstellungen im E-Mail-Editor mit One-Click-List-Unsubscribe-Optionen auf Nachrichtenebene, einschließlich Workspace-Standard und angepasster URL.]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### Anforderungen {#requirements}

Wenn Sie E-Mails mit Ihrer eigenen angepassten Abmeldefunktion senden, müssen Sie die folgenden Anforderungen erfüllen, um sicherzustellen, dass die von Ihnen eingerichtete One-Klick, der or klicken-Abmelde-URL RFC 8058 entspricht:

* Die URL muss in der Lage sein, Abmelde-POST-Anfragen zu verarbeiten.
* Die URL muss mit `https://` beginnen.
* Die URL darf keine HTTPS-Weiterleitung oder einen Body zurückgeben. One-Klick, der or klicken-Abmeldelinks, die zu einer Landingpage oder einer anderen Art von Webseite führen, entsprechen nicht RFC 8058.
* POST-Anfragen dürfen keine Cookies setzen.

Wählen Sie **Custom list-unsubscribe header**, um Ihren eigenen konfigurierten One-Klick, der or klicken-Abmelde-Endpunkt und ein optionales „mailto:“ hinzuzufügen. Braze erfordert eine URL-Eingabe zur Unterstützung eines angepassten List-Unsubscribe-Headers, da die One-Klick, der or klicken-Abmeldung per HTTP eine Anforderung von Yahoo und Gmail für Massenversender ist.

![E-Mail-Präferenzen mit Feldern für einen angepassten List-Unsubscribe-Header für eine One-Click-Abmelde-URL und ein optionales Mailto.]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## E-Mail-Betreffzeilen ergänzen {#append-email-subject-lines}

Verwenden Sie den Umschalter, um „[TEST]“ und „[SEED]“ in Ihre Test- und Seed-E-Mail-Betreffzeilen aufzunehmen. Dies kann helfen, E-Mail-Campaigns zu identifizieren, die als Tests gesendet wurden.

![Workspace-E-Mail-Einstellung mit Umschalter, der TEST- und SEED-Präfixe zu Test- und Seed-E-Mail-Betreffzeilen hinzufügt.]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## Inline-CSS bei neuen E-Mails standardmäßig {#inline-css-on-new-emails-by-default}

CSS-Inlining ist eine Technik, die CSS-Stile automatisch in Ihre E-Mails und neue E-Mails einbettet. Bei einigen E-Mail-Clients kann dies das Rendering Ihrer E-Mails verbessern.

Das Ändern dieser Einstellung hat keine Auswirkungen auf Ihre bestehenden E-Mail-Nachrichten oder Templates. Sie können diesen Standard jederzeit beim Verfassen von Nachrichten oder Templates überschreiben. Weitere Informationen finden Sie unter [CSS-Inlining]({{site.baseurl}}/user_guide/channels/email/html_editor/css_inline).

## Nutzer:innen bei Änderung ihrer E-Mail-Adresse erneut anmelden {#resubscribe-users-when-their-email-changes}

Sie können Nutzer:innen automatisch erneut anmelden, wenn sie ihre E-Mail-Adresse ändern. Wenn beispielsweise ein:e zuvor abgemeldete:r Workspace-Nutzer:in ihre oder seine E-Mail-Adresse in eine Adresse ändert, die nicht auf der Abmeldeliste für Braze steht, wird sie oder er automatisch wieder angemeldet.

![Workspace-Einstellung, die Nutzer:innen bei Änderung ihrer E-Mail-Adresse automatisch erneut anmeldet.]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## Abo-Seiten und Fußzeilen {#subscription-pages-and-footers}

{% tabs local %}
{% tab Angepasste Fußzeile %}

Für kommerzielle E-Mails schreibt der [CAN-SPAM Act](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003) vor, dass alle kommerziellen E-Mails eine Abmeldeoption enthalten müssen. Mit den Einstellungen für angepasste Fußzeilen können Sie CAN-SPAM-konform bleiben und gleichzeitig Ihre E-Mail-Abmelde-Fußzeile anpassen. Um konform zu bleiben, müssen Sie Ihre angepasste Fußzeile zu allen E-Mails hinzufügen, die im Rahmen von Campaigns für diesen Workspace versendet werden.

Beachten Sie die folgenden Anforderungen beim Erstellen einer angepassten Fußzeile für Ihr E-Mail-Messaging:
- Muss eine Abmelde-URL und eine physische Postanschrift enthalten.
- Sollte weniger als 100 KB groß sein.

![Editor für angepasste E-Mail-Fußzeilen mit Feldern für Abmeldelink und Postanschrift zur CAN-SPAM-Konformität.]({% image_buster /assets/img/email_settings/custom_footer.png %})

Informationen zu Liquid-Templates für angepasste Fußzeilen finden Sie unter [Angepasste Fußzeilen]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions).

{% endtab %}
{% tab Angepasste Abmeldeseite %}

In Braze können Sie eine **angepasste Abmeldeseite** mit eigenem HTML erstellen. Diese Seite wird angezeigt, nachdem sich Nutzer:innen über den Link am Ende einer E-Mail abgemeldet haben. Beachten Sie, dass diese Seite weniger als 750 KB groß sein sollte.

![HTML-Editor und Vorschau für eine angepasste Abmeldeseite, die nach der Abmeldung von E-Mails angezeigt wird.]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

{% multi_lang_include email/external_font_domains.md page_type='unsubscribe' %}

{% endtab %}
{% tab Angepasste Opt-in-Seite %}

Sie können eine angepasste Opt-in-Seite mit eigenem HTML erstellen. Diese in Ihre E-Mails einzubinden kann besonders vorteilhaft sein, wenn Ihr Branding und Ihre Botschaft während des gesamten Lebenszyklus Ihrer Nutzer:innen konsistent bleiben sollen. Beachten Sie, dass diese Seite weniger als 750 KB groß sein sollte.

![HTML-Editor und Vorschau für eine angepasste Opt-in-Seite zur Bestätigung des E-Mail-Abos im eigenen Branding.]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

{% multi_lang_include email/external_font_domains.md page_type='opt-in' %}

{% endtab %}
{% endtabs %}

{% alert tip %}
Wählen Sie im Bereich **Vorschau** einer Abo-Seite oder Fußzeile die Option **Vorschau-Link kopieren**, um einen teilbaren Vorschau-Link zu generieren und zu kopieren, der zeigt, wie die E-Mail-Fußzeile, die Abmeldeseite oder die Opt-in-Seite für zufällig ausgewählte Nutzer:innen aussieht. Weitere Informationen finden Sie unter [Teilbare Vorschau]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).
{% endalert %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Ein-Klick-Abmeldung

{% details Kann die Ein-Klick-Abmelde-URL (über den List-Unsubscribe-Header) auf ein Präferenzcenter verlinken? %}
Nein, das entspricht nicht RFC 8058, was bedeutet, dass Sie die Anforderungen von Yahoo und Gmail für die Ein-Klick-Abmeldung nicht erfüllen.
{% enddetails %}

{% details Warum erhalte ich die Fehlermeldung „Your email body does not include an unsubscribe link“, wenn ich mein Präferenzcenter erstelle? %}
Ein Präferenzcenter wird nicht als Abmeldelink betrachtet. Ihre E-Mail-Empfänger:innen müssen die Möglichkeit haben, sich von allen kommerziellen E-Mails abzumelden, um CAN-SPAM-konform zu bleiben.
{% enddetails %}

{% details Muss ich vergangene E-Mail-Campaigns und Canvase bearbeiten, um die Ein-Klick-Abmelde-Einstellung nach der Aktivierung anzuwenden? %}
Wenn Sie keinen der Anwendungsfälle für die Ein-Klick-List-Unsubscribe-Einstellung auf Nachrichtenebene haben, sind keine weiteren Maßnahmen erforderlich, solange die Einstellung unter **E-Mail-Präferenzen** aktiviert ist. Braze fügt automatisch die Ein-Klick-Abmelde-Header zu allen ausgehenden Marketing- und Werbenachrichten hinzu. Wenn Sie jedoch das Ein-Klick-Abmeldeverhalten auf Nachrichtenebene konfigurieren müssen, müssen Sie vorherige E-Mail-Campaigns und Canvas-Schritte entsprechend Update or aktualisieren or aktualisieren.
{% enddetails %}

{% details Ich kann den List-Unsubscribe- und Ein-Klick-Abmelde-Header in der Originalnachricht oder den Rohdaten sehen, aber warum wird der Abmelde-Button in Gmail oder Yahoo nicht angezeigt? %}
Gmail und Yahoo entscheiden letztendlich, ob der List-Unsubscribe- oder Ein-Klick-Abmelde-Header angezeigt wird oder nicht. Bei neuen Absendern oder Absendern mit niedriger Absender-Reputation kann es gelegentlich vorkommen, dass der Abmelde-Button nicht angezeigt wird.
{% enddetails %}

{% details Unterstützt der benutzerdefinierte Ein-Klick-Abmelde-Header Liquid? %}
Ja, Liquid und bedingte Logik werden unterstützt, um dynamische Ein-Klick-Abmelde-URLs für den Header zu ermöglichen.
{% enddetails %}

{% alert tip %}
Wenn Sie bedingte Logik hinzufügen, vermeiden Sie Ausgabewerte, die Leerzeichen zu Ihrer URL hinzufügen, da Braze diese Leerzeichen nicht entfernt.
{% endalert %}

### Ein-Klick-List-Unsubscribe auf Nachrichtenebene

{% details Wenn ich die E-Mail-Header für die Ein-Klick-Abmeldung manuell hinzufüge und der E-Mail-Unsubscribe-Header aktiviert ist, was ist das erwartete Verhalten? %}
Die für die Ein-Klick-List-Unsubscribe hinzugefügten E-Mail-Header gelten für alle zukünftigen Sendungen dieser Campaign.
{% enddetails %}

{% details Warum müssen Abo-Gruppen über Nachrichtenvarianten hinweg übereinstimmen, um den Versand zu starten? %}
Bei einer Campaign mit A/B-Tests sendet Braze zufällig eine der Varianten an Nutzer:innen. Wenn Sie zwei verschiedene Abo-Gruppen für dieselbe Campaign festgelegt haben (Variante A ist auf Abo-Gruppe A eingestellt und Variante B ist auf Abo-Gruppe B eingestellt), können wir nicht garantieren, dass Nutzer:innen, die nur Abo-Gruppe B abonniert haben, Variante B erhalten. Es kann vorkommen, dass sich Nutzer:innen von einer Abo-Gruppe abmelden, aus der sie sich bereits abgemeldet haben.
{% enddetails %}

{% details Die E-Mail-Unsubscribe-Header-Einstellung ist in den E-Mail-Präferenzen deaktiviert, aber in den Versandinformationen meiner Campaign ist die Ein-Klick-List-Unsubscribe-Einstellung auf „Workspace-Standard verwenden“ gesetzt. Ist das ein Fehler? %}
Nein. Wenn die Workspace-Einstellung deaktiviert ist und die Nachrichteneinstellung auf **Workspace-Standard verwenden** gesetzt ist, folgt Braze der Konfiguration in den **E-Mail-Präferenzen**. Das bedeutet, dass wir den Ein-Klick-Abmelde-Header für die Campaign nicht hinzufügen.
{% enddetails %}

{% details Was passiert, wenn eine Abo-Gruppe archiviert wird? Bricht das die Ein-Klick-Abmeldung bei bereits gesendeten E-Mails? %}
Wenn eine in den **Versandinformationen** für die Ein-Klick-Abmeldung referenzierte Abo-Gruppe archiviert wird, verarbeitet Braze die Abmeldungen über die Ein-Klick-Funktion weiterhin. Die Abo-Gruppe wird im Dashboard nicht mehr angezeigt (Segment-Filter, Kundenprofil or Nutzerprofil und ähnliche Bereiche).
{% enddetails %}

{% details Ist die Ein-Klick-Abmelde-Einstellung für E-Mail-Templates verfügbar? %}
Nein, wir planen derzeit nicht, diese Funktion für E-Mail-Templates hinzuzufügen, da diesen Templates keine Versanddomain zugewiesen ist. {% multi_lang_include product_feedback_cta.md context="gap" feature="per-domain sending for email templates" %}
{% enddetails %}

{% details Prüft diese Funktion, ob die zur benutzerdefinierten Option hinzugefügte Ein-Klick-Abmelde-URL gültig ist? %}
Nein, wir prüfen oder validieren keine Links im Braze-Dashboard. Stellen Sie sicher, dass Sie Ihre URL vor dem Start ordnungsgemäß testen.
{% enddetails %}