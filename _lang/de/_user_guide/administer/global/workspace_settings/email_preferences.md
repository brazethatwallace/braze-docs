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

**E-Mail-Präferenzen** finden Sie im Dashboard unter **Einstellungen**.

## Sendekonfiguration {#sending-configuration}

Die E-Mail-Einstellungen im Abschnitt **Sendekonfiguration** bestimmen, welche Details in Ihren E-Mail-Campaigns enthalten sind. Diese Einstellungen beziehen sich insbesondere darauf, was Ihre Nutzer:innen sehen, wenn sie eine E-Mail von Braze erhalten.

### Einstellungen für ausgehende E-Mails {#outbound-email-settings}

Beim Konfigurieren Ihrer E-Mail-Einstellungen legen die Einstellungen für ausgehende E-Mails fest, welche Namen und E-Mail-Adressen verwendet werden, wenn Braze E-Mails an Ihre Nutzer:innen sendet.

{% tabs local %}
{% tab Display Name Address %}

In diesem Abschnitt können Sie die Namen und E-Mail-Adressen hinzufügen, die verwendet werden können, wenn Braze E-Mails an Ihre Nutzer:innen sendet. Die Anzeigenamen und E-Mail-Adressen stehen in den **Sendeinformationen** zur Verfügung, wenn Sie Ihre E-Mail-Campaign erstellen. Beachten Sie, dass Änderungen an den Einstellungen für ausgehende E-Mails keine rückwirkende Auswirkung auf bestehende Sendungen haben.

![Abschnitt „Einstellungen für ausgehende E-Mails“ mit Feldern für verschiedene Anzeigenamen und Domains.]({% image_buster /assets/img/email_settings/display_name_address.png %})

#### Mit Liquid personalisieren {#personalize-with-liquid}

Sie können auch [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) in den Feldern **Anzeigename des Absenders**, **Lokaler Teil** und **Domain** verwenden, um den Absendernamen und die E-Mail-Adresse dynamisch auf Basis angepasster Attribute zu erstellen. Beachten Sie, dass Sie zur Verwendung von Liquid im Feld **Domain** in den **Sendeinformationen** einer E-Mail-Campaign das Kontrollkästchen **Customize from display name + address** aktivieren müssen.

![Sendeeinstellungen mit Feldern zur Anpassung des Anzeigenamens, der Adresse und der Domain des Absenders.]({% image_buster /assets/img/email_settings/email_campaign_domain.png %})

Sie können beispielsweise bedingte Logik verwenden, um von verschiedenen Marken oder Regionen aus zu senden:

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
{% tab Reply-To Address %}

Durch das Hinzufügen einer E-Mail-Adresse in diesem Abschnitt können Sie diese als Antwortadresse für Ihre E-Mail-Campaign auswählen. Sie können eine E-Mail-Adresse auch als Standard festlegen, indem Sie **Make Default** auswählen. Diese E-Mail-Adressen stehen in den **Sendeinformationen** zur Verfügung, wenn Sie Ihre E-Mail-Campaign erstellen.

![Abschnitt „Antwortadresse“ mit Feldern zur Eingabe mehrerer Antwortadressen.]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

{% alert note %}
Braze-Sendedomains akzeptieren keine eingehenden E-Mails. Wenn eine Empfängerin oder ein Empfänger auf eine E-Mail antwortet, die von einer in Braze konfigurierten Sendedomain gesendet wurde, wird die Antwort mit einem `550 5.7.1 relaying denied`-Fehler zurückgewiesen. Die Antwortadresse muss nicht dieselbe Domain wie die Absenderadresse verwenden. Wenn Sie Antworten empfangen müssen – beispielsweise um Kalendereinladungsbestätigungen zu sammeln – verwenden Sie eine Subdomain, die nicht für den Versand konfiguriert ist und bei der ein Posteingang für den E-Mail-Empfang eingerichtet ist.
{% endalert %}

#### Mit Liquid personalisieren

Sie können auch [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) im Feld **Antwortadresse** verwenden, um die Antwortadresse dynamisch auf Basis angepasster Attribute zu erstellen. Sie können beispielsweise bedingte Logik verwenden, um Antworten an verschiedene Regionen oder Abteilungen zu senden:

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

{% endtab %}
{% tab BCC Address %}

In diesem Abschnitt können Sie BCC-Adressen verwalten, die an ausgehende E-Mail-Nachrichten von Braze angehängt werden können. Durch das Anhängen einer BCC-Adresse an eine E-Mail-Nachricht wird eine identische Kopie der Nachricht, die Ihre Nutzer:innen erhalten, an Ihren BCC-Posteingang gesendet. Dies ist ein nützliches Werkzeug, um Kopien von Nachrichten aufzubewahren, die Sie an Ihre Nutzer:innen gesendet haben, sei es für Compliance-Anforderungen oder Kundensupport-Zwecke. BCC-E-Mails sind nicht in E-Mail-Berichten und Analytics enthalten.

BCC-Adressen sind für Amazon SES, SendGrid und SparkPost verfügbar. Als Alternative zu BCC-Adressen empfehlen wir die Verwendung der [Nachrichtenarchivierung]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving), um eine Kopie der an Nutzer:innen gesendeten Nachrichten für Archivierungs- oder Compliance-Zwecke zu speichern.

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

Nachdem Sie eine Adresse hinzugefügt haben, steht diese zur Auswahl, wenn Sie eine E-Mail in Campaigns oder Canvas-Schritten erstellen. Wählen Sie **Make Default** neben einer Adresse, um diese Adresse standardmäßig beim Starten einer neuen E-Mail-Campaign oder Canvas-Komponente auszuwählen. Um dies auf Nachrichtenebene zu überschreiben, können Sie beim Einrichten Ihrer Nachricht **No BCC** auswählen.

Wenn Sie verlangen, dass alle von Braze gesendeten E-Mail-Nachrichten eine BCC-Adresse enthalten, können Sie den Schalter **Require a BCC address for all your email campaigns** aktivieren. Dadurch müssen Sie eine Standardadresse auswählen, die automatisch bei neuen E-Mail-Campaigns oder Canvas-Schritten ausgewählt wird. Die Standardadresse wird auch automatisch zu allen über unsere REST API getriggerten Nachrichten hinzugefügt. Es ist nicht erforderlich, die bestehende API-Anfrage zu ändern, um die Adresse einzuschließen.

#### Dynamisches BCC {#dynamic-bcc}

Mit dynamischem BCC können Sie Liquid in Ihrer BCC-Adresse verwenden. Beachten Sie, dass dieses Feature nur in den **E-Mail-Präferenzen** verfügbar ist und nicht in der Campaign selbst festgelegt werden kann. Pro E-Mail-Empfänger:in ist nur eine BCC-Adresse zulässig.

Sie können beispielsweise {% raw %}`{{custom_attribute.${support_agent}}}`{% endraw %} als BCC-Adresse für E-Mails Ihres Support-Teams hinzufügen.

![BCC-Adressabschnitt des Tabs „E-Mail-Einstellungen“ mit einer BCC-Adresse, die Liquid verwendet.]({% image_buster /assets/img/email_settings/dynamic_bcc.png %}){: style="max-width:90%;" }

{% endtab %}
{% endtabs %}

## Open-Tracking-Pixel {#open-tracking-pixel}

[![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

Das E-Mail-Open-Tracking-Pixel ist ein unsichtbares 1 x 1&nbsp;px großes Bild, das automatisch in Ihr E-Mail-HTML eingefügt wird. Dieses Pixel hilft Braze zu erkennen, ob Ihre Nutzer:innen Ihre E-Mail geöffnet haben. Wenn der E-Mail-Client einer Nutzerin oder eines Nutzers eine Anfrage an unser Tracking-Pixel stellt, kann die Anfrage Informationen wie die IP-Adresse, den User-Agent und den Zeitstempel enthalten. E-Mail-Öffnungsinformationen können sehr nützlich sein und Ihnen helfen, effektive Marketingstrategien zu bestimmen, indem Sie die entsprechenden Öffnungsraten verstehen.

### Platzierung {#placement}

Das Standardverhalten in Braze ist es, das Tracking-Pixel am Ende Ihrer E-Mail anzufügen, typischerweise in einem `<body>`-Tag. Für die Mehrheit der Nutzer:innen ist dies der ideale Ort für das Pixel.

Obwohl das Pixel bereits so gestaltet ist, dass es so wenige visuelle Änderungen wie möglich verursacht, wären unbeabsichtigte visuelle Änderungen am Ende einer E-Mail am wenigsten sichtbar. Dies ist auch der Standard für E-Mail-Anbieter wie SendGrid und SparkPost.

Um unerwartetes Verhalten zu reduzieren, halten Sie Liquid innerhalb von `<html>`-Tags. Verschachtelte oder doppelte Tags auf Dokumentebene können die Analyse der E-Mail und die Platzierung des Pixels verändern, was sich auf das Open-Tracking und das Layout auswirken kann. Weitere Informationen finden Sie unter [Liquid verwenden]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid).

### Platzierung aktualisieren {#update-the-placement}

Braze unterstützt derzeit das Überschreiben der Standard-Open-Tracking-Pixel-Position des ESP (das letzte Tag im `<body>` einer E-Mail), um es zum ersten Tag im `<body>` zu verschieben.

![Abschnitt „Open-Tracking-Pixel“ mit den Optionen zum Verschieben für SendGrid, SparkPost oder Amazon SES.]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

So ändern Sie die Position:

1. Gehen Sie in Braze zu **Einstellungen** > **E-Mail-Präferenzen**.
2. Wählen Sie eine der folgenden Optionen: **Move for SendGrid**, **Move for SparkPost** oder **Move for Amazon SES**.
3. Wählen Sie **Speichern**.

Nach dem Speichern sendet Braze spezielle Anweisungen an den ESP, um das Open-Tracking-Pixel am Anfang aller HTML-E-Mails zu platzieren.

{% alert important %}
Die SSL-Aktivierung umschließt die URL des Tracking-Pixels mit HTTPS anstelle von HTTP. Wenn Ihr SSL falsch konfiguriert ist, kann dies die Wirksamkeit des Tracking-Pixels beeinträchtigen.
{% endalert %}

{% alert important %}
Klick-Tracking gilt nur für Links, die mit `http://` oder `https://` beginnen. `mailto:`-Links (z. B. `mailto:support@example.com`) werden nicht für das Tracking umgeschrieben.
{% endalert %}

## List-Unsubscribe-Header {#list-unsubscribe}

{% alert note %}
Seit dem 15. Juni 2026 fügt Braze den Mailto-Header nicht mehr in E-Mails ein, wenn der One-Click-List-Unsubscribe-Header so konfiguriert ist, dass er auf eine bestimmte Abo-Gruppe beschränkt ist. Nutzer:innen, die sich über den List-Unsubscribe-Header abmelden, werden nur von dieser bestimmten Abo-Gruppe abgemeldet, nicht global.
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

Die folgende Tabelle fasst die Unterstützung der Postfach-Anbieter für den „mailto:“-Header, die List-Unsubscribe-URL und die One-Click-Abmeldung ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) zusammen.

| List-Unsubscribe-Header | Mailto:-Header | List-Unsubscribe-URL | One-Click-Abmeldung (RFC 8058) |
| ----- | --- | --- | --- |
| Gmail | Unterstützt* | Unterstützt | Unterstützt |
| Gmail Mobile | Nicht unterstützt | Nicht unterstützt | Nicht unterstützt |
| Apple Mail | Unterstützt | Nicht unterstützt | Nicht unterstützt |
| Outlook.com | Unterstützt | Nicht unterstützt | Nicht unterstützt |
| Yahoo! Mail | Unterstützt* | Nicht unterstützt | Unterstützt |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Unterstützung durch Postfach-Anbieter" }

_*Yahoo und Gmail stellen den „mailto:“-Header schrittweise ein und werden nur noch One-Click unterstützen._

Ob der Header angezeigt wird, entscheidet letztlich der Postfach-Anbieter. Um zu prüfen, ob der List-Unsubscribe-Header in der Roh-E-Mail (Text) für die Empfängerin oder den Empfänger in Gmail enthalten ist, gehen Sie wie folgt vor:

1. Wählen Sie **Show Original** in der E-Mail. Dies öffnet einen neuen Tab mit der Rohversion der E-Mail und ihren Headern.
2. Suchen Sie nach „List-Unsubscribe“. Bei der One-Click-Abmeldung fügen viele Anbieter auch einen „List-Unsubscribe-Post“-Header hinzu. Bestätigen Sie, dass beide in der Rohnachricht erscheinen, wenn Sie erwarten, dass One-Click verfügbar ist.

Wenn der Header in der Rohversion der E-Mail vorhanden ist, aber nicht angezeigt wird, hat der Postfach-Anbieter entschieden, die Abmeldeoption nicht anzuzeigen, was bedeutet, dass wir keine weiteren Erkenntnisse darüber haben, warum der Postfach-Anbieter den Header nicht anzeigt. Die Anzeige des List-Unsubscribe-Headers ist letztlich reputationsbasiert. In den meisten Fällen gilt: Je besser Ihre Absender-Reputation beim Postfach-Anbieter ist, desto wahrscheinlicher wird der List-Unsubscribe-Header angezeigt.

### E-Mail-Abmelde-Header in Workspaces {#email-unsubscribe-header-in-workspaces}

![Auswahl von „Nutzer:innen, die abonniert oder angemeldet sind“ für den Versand.]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Wenn das Feature für den E-Mail-Abmelde-Header aktiviert ist, gilt diese Einstellung für den gesamten Workspace, nicht auf Unternehmensebene. Sie wird zu Campaigns und Canvases hinzugefügt, die so konfiguriert sind, dass sie an Nutzer:innen gesendet werden, die abonniert oder angemeldet sind, oder an angemeldete Nutzer:innen im Schritt **Target Audience** der Campaign- und Canvas-Builder.

Bei Verwendung des „Workspace-Standards“ fügt Braze den One-Click-Abmelde-Header nicht für Campaigns hinzu, die als transaktional gelten und so konfiguriert sind, dass sie „an alle Nutzer:innen, einschließlich abgemeldeter Nutzer:innen“ gesendet werden. Um dies zu überschreiben und den One-Click-Abmelde-Header beim Senden an abgemeldete Nutzer:innen hinzuzufügen, können Sie **Unsubscribe globally from all emails** in den One-Click-List-Unsubscribe-Einstellungen auf Nachrichtenebene auswählen.

### Standard-List-Unsubscribe-Header {#default-list-unsubscribe-header}

{% alert important %}
Gmail beabsichtigt, dass Absender die One-Click-Abmeldung für alle ihre ausgehenden kommerziellen und werblichen Nachrichten ab dem 1. Juni 2024 implementieren. Weitere Informationen finden Sie in den [Gmail-Absenderrichtlinien](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) und den [FAQ zu Gmails E-Mail-Absenderrichtlinien](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages). Yahoo hat einen Zeitplan für Anfang 2024 für die aktualisierten Anforderungen angekündigt. Weitere Informationen finden Sie unter [More Secure, Less Spam: Enforcing Email Standards for a Better Experience](https://blog.postmaster.yahooinc.com/).
{% endalert %}

Um die Braze-Abmeldefunktion zur direkten Verarbeitung von Abmeldungen zu verwenden, wählen Sie **Include a one-click list-unsubscribe (mailto and HTTP) email header for emails sent to subscribed or opted-in users** und wählen Sie **Braze default** als Standard-Braze-URL und Mail-to.

![Option zum automatischen Einschließen eines List-Unsubscribe-Headers für E-Mails an abonnierte oder angemeldete Nutzer:innen.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Braze unterstützt die folgenden Versionen des List-Unsubscribe-Headers:

| List-Unsubscribe-Version | Beschreibung |
| ----- | --- |
| One-Click (RFC 8058) | Bietet Empfänger:innen eine unkomplizierte Möglichkeit, sich mit einem einzigen Klick von E-Mails abzumelden. Dies ist eine Anforderung von Yahoo und Gmail für Massenversender. |
| List-Unsubscribe-URL oder HTTPS | Stellt Empfänger:innen einen Link bereit, der sie zu einer Webseite weiterleitet, auf der sie sich abmelden können. |
| Mailto | Gibt eine E-Mail-Adresse als Ziel für die Abmeldeanfrage an, die von der Empfängerin oder dem Empfänger an die Marke gesendet wird. <br><br> _Zur Verarbeitung von Mailto-List-Unsubscribe-Anfragen müssen solche Abmeldeanfragen die in Braze gespeicherte E-Mail-Adresse der Endnutzerin oder des Endnutzers enthalten, die bzw. der sich abmeldet. Diese kann durch die „Absenderadresse“ der E-Mail, von der aus sich die Endnutzerin oder der Endnutzer abmeldet, den codierten Betreff oder den codierten Text der empfangenen E-Mail bereitgestellt werden. In sehr seltenen Fällen halten sich einige Postfach-Anbieter nicht an das [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368)-Protokoll, was dazu führt, dass die E-Mail-Adresse nicht korrekt übergeben wird. Dies kann dazu führen, dass eine Abmeldeanfrage in Braze nicht verarbeitet werden kann._ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Standard-List-Unsubscribe-Header" }

Wenn Braze eine List-Unsubscribe-Anfrage von einer Nutzerin oder einem Nutzer über eine der [Standard-List-Unsubscribe-Header](#default-list-unsubscribe-header)-Methoden erhält, wird der globale E-Mail-Abo-Status dieser Person auf „Abgemeldet“ gesetzt. Wenn keine Übereinstimmung vorliegt, verarbeitet Braze diese Anfrage nicht.

### One-Click-Abmeldung {#one-click-unsubscribe}

Die Verwendung der One-Click-Abmeldung für den List-Unsubscribe-Header ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) konzentriert sich darauf, Empfänger:innen eine einfache Möglichkeit zu bieten, sich von E-Mails abzumelden.

### One-Click-List-Unsubscribe auf Nachrichtenebene {#message-level-one-click-list-unsubscribe}

Die Einstellung für One-Click-List-Unsubscribe auf Nachrichtenebene überschreibt das für Workspaces festgelegte E-Mail-Abmelde-Header-Feature. Wenden Sie das One-Click-Abmeldeverhalten pro Campaign oder Canvas-Schritt für die folgenden Anwendungsfälle an:

- Fügen Sie eine Braze-One-Click-Abmeldung für eine bestimmte Abo-Gruppe hinzu, um mehrere Marken/Listen innerhalb eines Workspace zu unterstützen
- Wechseln Sie zwischen der Standard-Braze-Abmeldung oder einer angepassten URL
- Fügen Sie Ihre angepasste One-Click-Abmelde-URL hinzu
- Lassen Sie die One-Click-Abmeldung für diese Nachricht weg

{% alert note %}
Die Einstellung für One-Click-List-Unsubscribe auf Nachrichtenebene ist nur bei Verwendung des Drag-and-Drop-Editors und des aktualisierten HTML-Editors verfügbar. Wenn Sie den vorherigen HTML-Editor verwenden, wechseln Sie zum aktualisierten HTML-Editor, um dieses Feature zu nutzen.
{% endalert %}

Gehen Sie in Ihrem E-Mail-Editor zu **Sending Settings** > **Sending Info**. Wählen Sie aus den folgenden Optionen:

- **Use workspace default**: Verwendet die in den **E-Mail-Präferenzen** festgelegten Einstellungen für den **E-Mail-Abmelde-Header**. Alle Änderungen an dieser Einstellung gelten für alle Nachrichten.
- **Unsubscribe globally from all emails**: Verwendet den Braze-Standard-One-Click-Abmelde-Header. Nutzer:innen, die den Abmelde-Button klicken, erhalten den globalen E-Mail-Abo-Status „Abgemeldet“.
- **Unsubscribe from specific subscription group**: Verwendet die angegebene Abo-Gruppe. Braze meldet Nutzer:innen, die den Abmelde-Button klicken, von der ausgewählten Abo-Gruppe ab.
    - Wenn Sie eine Abo-Gruppe auswählen, fügen Sie den Filter **Subscription Group** unter **Target Audiences** hinzu, um nur Nutzer:innen anzusprechen, die diese bestimmte Gruppe abonniert haben. Die für die One-Click-Abmeldung ausgewählte Abo-Gruppe muss mit der Abo-Gruppe übereinstimmen, die Sie ansprechen. Bei einer Nichtübereinstimmung der Abo-Gruppe riskieren Sie, an Nutzer:innen zu senden, die versuchen, sich von einer Abo-Gruppe abzumelden, von der sie bereits abgemeldet sind.

{% alert important %}
Die Einstellung **Unsubscribe from specific subscription group** gilt nur für den One-Click-List-Unsubscribe-Header. Der Mailto-List-Unsubscribe-Header wird bei Auswahl dieser Option nicht beeinflusst. Das bedeutet, dass eine Empfängerin oder ein Empfänger, die bzw. der sich über diese Methode abmeldet, eine globale Abmeldung protokolliert, nicht eine Abmeldung von der bestimmten Abo-Gruppe. Um den Mailto-List-Unsubscribe-Header von der globalen Abmeldung von Nutzer:innen auszuschließen, wenden Sie sich bei Auswahl dieser Einstellung an den [Support]({{site.baseurl}}/support_contact).
{% endalert %}

- **Custom**: Fügt Ihre angepasste One-Click-Abmelde-URL hinzu, damit Sie Abmeldungen direkt verarbeiten können.
- **Exclude unsubscribe**

{% alert important %}
Das Ausschließen der One-Click-Abmeldung oder jeglicher Abmeldemechanismen sollte nur für transaktionale Nachrichten erfolgen, wie Passwortzurücksetzungen, Quittungen und Bestätigungs-E-Mails.
{% endalert %}

Das Anpassen dieser Einstellung überschreibt das Standardverhalten für die One-Click-List-Unsubscribe in dieser E-Mail.

![Sendeeinstellungen im E-Mail-Editor mit One-Click-List-Unsubscribe-Optionen auf Nachrichtenebene, einschließlich Workspace-Standard und angepasster URL.]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### Anforderungen {#requirements}

Wenn Sie E-Mails mit Ihrer eigenen angepassten Abmeldefunktion senden, müssen Sie die folgenden Anforderungen erfüllen, um sicherzustellen, dass die von Ihnen eingerichtete One-Click-Abmelde-URL RFC 8058 entspricht:

* Die URL muss in der Lage sein, Abmelde-POST-Anfragen zu verarbeiten.
* Die URL muss mit `https://` beginnen.
* Die URL darf keine HTTPS-Weiterleitung oder einen Body zurückgeben. One-Click-Abmeldelinks, die zu einer Landingpage oder einer anderen Art von Webseite führen, entsprechen nicht RFC 8058.
* POST-Anfragen dürfen keine Cookies setzen.

Wählen Sie **Custom list-unsubscribe header**, um Ihren eigenen konfigurierten One-Click-Abmelde-Endpunkt und ein optionales „mailto:“ hinzuzufügen. Braze erfordert eine URL-Eingabe zur Unterstützung eines angepassten List-Unsubscribe-Headers, da die One-Click-Abmeldung per HTTP eine Anforderung von Yahoo und Gmail für Massenversender ist.

![E-Mail-Präferenzen mit Feldern für einen angepassten List-Unsubscribe-Header für eine One-Click-Abmelde-URL und ein optionales Mailto.]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## E-Mail-Betreffzeilen ergänzen {#append-email-subject-lines}

Verwenden Sie den Schalter, um „[TEST]“ und „[SEED]“ in Ihren Test- und Seed-E-Mail-Betreffzeilen einzufügen. Dies kann helfen, E-Mail-Campaigns zu identifizieren, die als Tests gesendet wurden.

![Workspace-E-Mail-Präferenz-Schalter, der TEST- und SEED-Präfixe zu Test- und Seed-E-Mail-Betreffzeilen hinzufügt.]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## Inline-CSS bei neuen E-Mails standardmäßig {#inline-css-on-new-emails-by-default}

CSS-Inlining ist eine Technik, die CSS-Stile automatisch für Ihre E-Mails und neuen E-Mails inline einfügt. Bei einigen E-Mail-Clients kann dies die Darstellung Ihrer E-Mails verbessern.

Das Ändern dieser Einstellung hat keine Auswirkungen auf Ihre bestehenden E-Mail-Nachrichten oder Templates. Sie können diesen Standard jederzeit beim Erstellen von Nachrichten oder Templates überschreiben. Weitere Informationen finden Sie unter [CSS-Inlining]({{site.baseurl}}/user_guide/channels/email/html_editor/css_inline).

## Nutzer:innen bei E-Mail-Änderung erneut abonnieren {#resubscribe-users-when-their-email-changes}

Sie können Nutzer:innen automatisch erneut abonnieren, wenn sie ihre E-Mail-Adresse ändern. Wenn beispielsweise eine zuvor abgemeldete Workspace-Nutzerin oder ein zuvor abgemeldeter Workspace-Nutzer ihre bzw. seine E-Mail-Adresse in eine ändert, die nicht auf der Abmeldeliste von Braze steht, wird sie bzw. er automatisch erneut abonniert.

![Workspace-Einstellung, die Nutzer:innen automatisch erneut abonniert, wenn sich ihre E-Mail-Adresse ändert.]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## Abo-Seiten und -Fußzeilen {#subscription-pages-and-footers}

{% tabs local %}
{% tab Angepasste Fußzeile %}

Für kommerzielle E-Mails verlangt der [CAN-SPAM Act](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003), dass alle kommerziellen E-Mails eine Abmeldeoption enthalten. Mit den Einstellungen für angepasste Fußzeilen können Sie CAN-SPAM-konform bleiben und gleichzeitig Ihre E-Mail-Opt-out-Fußzeile anpassen. Um konform zu bleiben, müssen Sie Ihre angepasste Fußzeile zu allen E-Mails hinzufügen, die als Teil von Campaigns für diesen Workspace gesendet werden.

Beachten Sie die folgenden Anforderungen beim Erstellen einer angepassten Fußzeile für Ihre E-Mail-Nachrichten:
- Muss eine Abmelde-URL und eine physische Postanschrift enthalten.
- Sollte weniger als 100 KB groß sein.

![Editor für angepasste E-Mail-Fußzeilen mit Feldern für Abmeldelink und Postanschrift zur CAN-SPAM-Konformität.]({% image_buster /assets/img/email_settings/custom_footer.png %})

Weitere Informationen zum Liquid-Templating für angepasste Fußzeilen finden Sie unter [Angepasste Fußzeilen]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions).

{% endtab %}
{% tab Angepasste Abmeldeseite %}

Braze ermöglicht es Ihnen, eine **Angepasste Abmeldeseite** mit Ihrem eigenen HTML einzurichten. Diese Seite wird angezeigt, nachdem eine Nutzerin oder ein Nutzer sich über den unteren Bereich einer E-Mail abgemeldet hat. Beachten Sie, dass diese Seite weniger als 750 KB groß sein sollte.

![HTML-Editor und Vorschau für die angepasste Abmeldeseite, die nach der Abmeldung von E-Mails angezeigt wird.]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

{% multi_lang_include email/external_font_domains.md page_type='unsubscribe' %}

{% endtab %}
{% tab Angepasste Opt-in-Seite %}

Sie können eine angepasste Opt-in-Seite mit Ihrem eigenen HTML erstellen. Die Einbindung in Ihre E-Mails kann besonders vorteilhaft sein, wenn Sie möchten, dass Ihr Branding und Ihre Botschaft während des gesamten Nutzerlebenszyklus konsistent bleiben. Beachten Sie, dass diese Seite weniger als 750 KB groß sein sollte.

![HTML-Editor und Vorschau für die angepasste Opt-in-Seite zur gebrandeten E-Mail-Abo-Bestätigung.]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

{% multi_lang_include email/external_font_domains.md page_type='opt-in' %}

{% endtab %}
{% endtabs %}

{% alert tip %}
Wenn Sie sich im Abschnitt **Vorschau** für eine Abo-Seite oder Fußzeile befinden, wählen Sie **Copy preview link**, um einen teilbaren Vorschaulink zu generieren und zu kopieren, der zeigt, wie die E-Mail-Fußzeile, Abmeldeseite oder Opt-in-Seite für eine zufällige Nutzerin oder einen zufälligen Nutzer aussieht. Der Link ist sieben Tage gültig, bevor er neu generiert werden muss.
{% endalert %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### One-Click-Abmeldung

{% details Kann die One-Click-Abmelde-URL (über den List-Unsubscribe-Header) auf ein Präferenzzentrum verlinken? %}
Nein, das entspricht nicht RFC 8058, was bedeutet, dass Sie nicht konform mit den One-Click-Abmeldeanforderungen von Yahoo und Gmail wären.
{% enddetails %}

{% details Warum erhalte ich die Fehlermeldung „Ihr E-Mail-Text enthält keinen Abmeldelink“, wenn ich mein Präferenzzentrum erstelle? %}
Ein Präferenzzentrum gilt nicht als Abmeldelink. Ihre E-Mail-Empfänger:innen müssen die Möglichkeit haben, sich von allen kommerziellen E-Mails abzumelden, um CAN-SPAM-konform zu bleiben.
{% enddetails %}

{% details Muss ich vergangene E-Mail-Campaigns und Canvases bearbeiten, um die One-Click-Abmeldeeinstellung nach der Aktivierung anzuwenden? %}
Wenn Sie keinen der Anwendungsfälle für die One-Click-List-Unsubscribe-Einstellung auf Nachrichtenebene haben, ist keine Aktion erforderlich, solange die Einstellung unter **E-Mail-Präferenzen** aktiviert ist. Braze fügt die One-Click-Abmelde-Header automatisch zu allen ausgehenden Marketing- und Werbenachrichten hinzu. Wenn Sie jedoch das One-Click-Abmeldeverhalten auf Nachrichtenebene konfigurieren müssen, müssen Sie vorherige E-Mail-Campaigns und Canvas-Schritte entsprechend aktualisieren.
{% enddetails %}

{% details Ich kann den List-Unsubscribe- und One-Click-Abmelde-Header in der Originalnachricht oder den Rohdaten sehen, aber warum sehe ich den Abmelde-Button nicht in Gmail oder Yahoo? %}
Gmail und Yahoo entscheiden letztlich, ob der List-Unsubscribe- oder One-Click-Abmelde-Header angezeigt wird oder nicht. Bei neuen Absendern oder Absendern mit niedriger Absender-Reputation kann es gelegentlich vorkommen, dass der Abmelde-Button nicht angezeigt wird.
{% enddetails %}

{% details Unterstützt der angepasste One-Click-Abmelde-Header Liquid? %}
Ja, Liquid und bedingte Logik werden unterstützt, um dynamische One-Click-Abmelde-URLs für den Header zu ermöglichen.
{% enddetails %}

{% alert tip %}
Wenn Sie bedingte Logik hinzufügen, vermeiden Sie Ausgabewerte, die Leerzeichen zu Ihrer URL hinzufügen, da Braze diese Leerzeichen nicht entfernt.
{% endalert %}

### One-Click-List-Unsubscribe auf Nachrichtenebene

{% details Wenn ich die E-Mail-Header für One-Click manuell hinzufüge und der E-Mail-Abmelde-Header aktiviert ist, was ist das erwartete Verhalten? %}
Die für One-Click-List-Unsubscribe hinzugefügten E-Mail-Header gelten für alle zukünftigen Sendungen dieser Campaign.
{% enddetails %}

{% details Warum müssen Abo-Gruppen über Nachrichtenvarianten hinweg übereinstimmen, um zu starten? %}
Bei einer Campaign mit A/B-Tests sendet Braze einer Nutzerin oder einem Nutzer zufällig eine der Varianten. Wenn Sie zwei verschiedene Abo-Gruppen für dieselbe Campaign festgelegt haben (Variante A ist auf Abo-Gruppe A eingestellt und Variante B auf Abo-Gruppe B), können wir nicht garantieren, dass Nutzer:innen, die nur Abo-Gruppe B abonniert haben, Variante B erhalten. Es kann vorkommen, dass sich Nutzer:innen von einer Abo-Gruppe abmelden, von der sie sich bereits abgemeldet haben.
{% enddetails %}

{% details Die Einstellung für den E-Mail-Abmelde-Header ist in den E-Mail-Präferenzen deaktiviert, aber in den Sendeinformationen meiner Campaign ist die One-Click-List-Unsubscribe-Einstellung auf „Use workspace default“ gesetzt. Ist das ein Fehler? %}
Nein. Wenn die Workspace-Einstellung deaktiviert ist und die Nachrichteneinstellung auf **Use workspace default** gesetzt ist, folgt Braze dem, was in den **E-Mail-Präferenzen** konfiguriert ist. Das bedeutet, dass wir den One-Click-Abmelde-Header für die Campaign nicht hinzufügen.
{% enddetails %}

{% details Was passiert, wenn eine Abo-Gruppe archiviert wird? Unterbricht dies die One-Click-Abmeldung bei gesendeten E-Mails? %}
Wenn eine in den **Sendeinformationen** für One-Click referenzierte Abo-Gruppe archiviert wird, verarbeitet Braze weiterhin Abmeldungen über One-Click. Die Abo-Gruppe erscheint nicht mehr im Dashboard (Segment-Filter, Nutzerprofil und ähnliche Bereiche).
{% enddetails %}

{% details Ist die One-Click-Abmeldeeinstellung für E-Mail-Templates verfügbar? %}
Nein, wir planen derzeit nicht, dies für E-Mail-Templates hinzuzufügen, da diese Templates keiner Sendedomain zugewiesen sind. Wenn Sie an diesem Feature für E-Mail-Templates interessiert sind, reichen Sie [Produktfeedback]({{site.baseurl}}/user_guide/administer/personal/product_portal) ein.
{% enddetails %}

{% details Prüft dieses Feature, ob die zur angepassten Option hinzugefügte One-Click-Abmelde-URL gültig ist? %}
Nein, wir prüfen oder validieren keine Links im Braze-Dashboard. Stellen Sie sicher, dass Sie Ihre URL vor dem Start ordnungsgemäß testen.
{% enddetails %}