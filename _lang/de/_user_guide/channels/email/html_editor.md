---
nav_title: HTML-Editor
article_title: Eine E-Mail mit angepasstem HTML erstellen
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie eine E-Mail mit der Braze-Plattform erstellen. Enthalten sind Best Practices zum Verfassen Ihrer Nachrichten, zur Vorschau Ihrer Inhalte und zur Planung Ihrer Campaign oder Ihres Canvas."
tool:
  - Campaigns
channel:
  - email
search_rank: 1
---

# Eine E-Mail mit angepasstem HTML erstellen {#create-an-email-with-custom-html}

> E-Mail-Nachrichten eignen sich hervorragend, um Ihren Nutzer:innen Inhalte nach deren Wünschen zu liefern. Sie sind auch ausgezeichnete Werkzeuge, um Nutzer:innen erneut zu aktivieren, die Ihre App möglicherweise sogar deinstalliert haben. Das Senden von individuell angepassten E-Mail-Nachrichten verbessert das Nutzererlebnis und hilft Ihren Nutzer:innen, den größtmöglichen Mehrwert aus Ihrer App zu ziehen.

Beispiele für E-Mail-Campaigns finden Sie in unseren [Fallstudien](https://www.braze.com/customers).

{% alert tip %}
Wenn Sie zum ersten Mal eine E-Mail-Campaign erstellen, empfehlen wir Ihnen dringend, diese Braze-Lernkurse zu absolvieren:<br><br>
- [E-Mail-Opt-ins und Berechtigungen](https://learning.braze.com/messaging-channels-email)
- [Projekt: Ein einfaches E-Mail-Marketing-Programm erstellen](https://learning.braze.com/project-build-a-basic-email-marketing-program)
{% endalert %}

## Schritt 1: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten {#step-1-choose-where-to-build-your-message}

Verwenden Sie Campaigns für einzelne, einfache Nachrichten. Verwenden Sie Canvases für mehrstufige User-Journeys.

{% tabs %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Campaign erstellen**.
2. Wählen Sie **E-Mail** oder, für Campaigns, die auf mehrere Kanäle abzielen, wählen Sie **Multichannel**.
3. Geben Sie Ihrer Campaign einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu.
   * Tags erleichtern das Auffinden und Erstellen von Berichten über Ihre Campaigns. Wenn Sie zum Beispiel den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder) verwenden, können Sie nach bestimmten Tags filtern.
5. Fügen Sie so viele Varianten hinzu und benennen Sie diese, wie Sie für Ihre Campaign benötigen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Wenn alle Nachrichten in Ihrer Campaign ähnlich sein oder denselben Inhalt haben werden, verfassen Sie Ihre Nachricht, bevor Sie zusätzliche Varianten hinzufügen. Anschließend können Sie im Dropdown **Variante hinzufügen** die Option **Von Variante kopieren** auswählen.
{% endalert %}
{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Wenn Sie benutzerdefiniertes HTML erstellen möchten und Hintergründe in der mobilen Gmail-App bei aktiviertem Dark Mode des Geräts konsistent bleiben sollen, lesen Sie [Mobile Gmail-App und Hintergrundfarben im Dark Mode](#gmail-dark-mode).
{% endalert %}

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='email html editor' %}

## Schritt 2: Wählen Sie Ihre Bearbeitungserfahrung {#step-2-choose-your-template-and-compose-your-email}

Braze bietet zwei Bearbeitungserfahrungen beim Erstellen einer E-Mail-Campaign: unseren [Drag-and-Drop-Editor]({{site.baseurl}}/dnd) und unseren Standard-HTML-Editor. Wählen Sie die entsprechende Kachel für die Bearbeitungserfahrung, die Sie bevorzugen.

![Auswahl zwischen dem Drag-and-Drop-Editor, dem HTML-Editor oder Templates für Ihre E-Mail-Bearbeitungserfahrung.]({% image_buster /assets/img_archive/choose_email_creation.png %}){: style="max-width:75%" }

Anschließend können Sie entweder ein vorhandenes [E-Mail-Template]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template) auswählen, ein [Template hochladen]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template) (nur HTML-Editor) oder ein leeres Template verwenden.

Wenn Sie den HTML-Editor verwenden und Hintergrundfarben in der Gmail-Mobil-App bei aktiviertem Dark Mode des Geräts konsistent bleiben sollen, lesen Sie [Gmail-Mobil-App und Dark-Mode-Hintergrundfarben](#gmail-dark-mode).

{% alert tip %}
Wir empfehlen, pro E-Mail-Campaign eine Bearbeitungserfahrung auszuwählen. Wählen Sie beispielsweise entweder den **HTML Classic**- oder den **Block-Editor** in einer einzelnen E-Mail-Campaign, anstatt zwischen Editoren zu wechseln.
{% endalert %}

## Schritt 3: E-Mail verfassen {#step-3-compose-your-email}

Nachdem Sie Ihr Template ausgewählt haben, sehen Sie eine Übersicht Ihrer E-Mail, von der aus Sie direkt zum Vollbild-Editor springen können, um Ihre E-Mail zu entwerfen, Ihre Versandinformationen zu ändern und Warnungen zur Zustellbarkeit oder Rechtskonformität einzusehen. Sie können beim Verfassen zwischen den Tabs HTML, Klassisch, Nur-Text und [AMP]({{site.baseurl}}/user_guide/channels/email/customize/amp_for_email) wechseln.

![Der Button „Aus HTML regenerieren“.]({% image_buster /assets/img_archive/regenerate_from_html.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;" }

Braze aktualisiert die Nur-Text-Version automatisch aus der HTML-Version, bis eine Bearbeitung der Nur-Text-Version erkannt wird. Nachdem Braze eine Bearbeitung erkannt hat, stoppt es die automatische Aktualisierung, da davon ausgegangen wird, dass Sie beabsichtigte Änderungen vorgenommen haben. Um die automatische Synchronisierung wiederherzustellen, gehen Sie zu **Plaintext** und wählen Sie **Regenerate from HTML** (nur sichtbar, wenn die Nur-Text-Version nicht synchronisiert wird).

{% alert tip %}
Um Bewegung in einer E-Mail mit genauer Vorschau hinzuzufügen, verwenden Sie GIFs anstelle von Elementen, die JavaScript erfordern, da die meisten Posteingänge JavaScript nicht unterstützen.
{% endalert %}


{% alert important %}
Braze entfernt automatisch HTML-Event-Handler, die als Attribute referenziert werden. Dadurch wird das HTML modifiziert, überprüfen Sie die E-Mail daher nach der Fertigstellung erneut. Erfahren Sie mehr über [HTML-Handler](https://www.w3schools.com/tags/ref_eventattributes.asp).
{% endalert %}

{% alert tip %}
Brauchen Sie Hilfe beim Erstellen überzeugender Texte? Nutzen Sie den [KI-Textassistenten]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Geben Sie einen Produktnamen oder eine Beschreibung ein, und die KI generiert menschenähnliche Marketingtexte zur Verwendung in Ihren Nachrichten.

![Button „KI-Textassistent starten“ auf dem Tab „Body“ des E-Mail-Composers.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

Brauchen Sie Hilfe beim Erstellen von Rechts-nach-links-Nachrichten für Sprachen wie Arabisch und Hebräisch? Lesen Sie [Rechts-nach-links-Nachrichten erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages) für Best Practices.

### Gmail-Mobile-App und Dark Mode {#gmail-dark-mode}

Die Gmail-Mobile-App (Android und iOS) kann Hintergrundfarben invertieren, wenn das Gerät im Dark Mode ist. Das kann Layouts beeinträchtigen, bei denen der E-Mail-Hintergrund mit einer Bildkante oder einer bestimmten Markenfarbe übereinstimmen sollte.

Um dies zu vermeiden, verwenden Sie in der Tabellenzelle, die einen stabilen Hintergrund benötigt, einen einfarbigen CSS-`linear-gradient` anstelle von `background-color`. Gmail invertiert diese Behandlung weniger wahrscheinlich als eine flache Hintergrundfarbe.

Um beispielsweise einen weißen Hintergrund in einer Zelle beizubehalten, verwenden Sie Folgendes:

```html
<td style="background-image: linear-gradient(#ffffff, #ffffff);">
```

Ersetzen Sie `#ffffff` durch Ihre gewünschte Farbe.

{% alert note %}
Dieser Ansatz funktioniert nicht zuverlässig bei `<table aria-label="Gmail mobile app and dark mode #gmail-dark-mode">`-Elementen allein. Setzen Sie den Gradienten daher auf die Zelle statt nur auf die Tabelle.
  <caption>Gmail-Mobile-App und Dark Mode</caption>
{% endalert %}

Weitere Informationen zur Gradient-Syntax finden Sie unter [CSS-Gradienten auf W3Schools](https://www.w3schools.com/css/css3_gradients.asp).

### Schritt 3.1: Versandinformationen hinzufügen {#step-31-add-your-sending-information}

Nachdem Sie Ihre E-Mail-Nachricht entworfen und erstellt haben, fügen Sie Ihre Versandinformationen unter **Sending Settings** hinzu.

{% multi_lang_include email/sending_info_steps.md %}

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Eine Vorschau im rechten Panel wird mit den von Ihnen hinzugefügten Versandinformationen befüllt. Diese Informationen können auch aktualisiert werden, indem Sie zu **Einstellungen** > **E-Mail-Präferenzen** > **Versandkonfiguration** gehen.

#### Erweitert {#advanced}

Aktivieren Sie unter **Sending Settings** > **Advanced** die Option **Inline-CSS** für die breiteste Client-Unterstützung. Wenn Nachrichten abgeschnitten werden oder Bilder auf Zeilenhöhe gedehnt werden, versuchen Sie, Inline-CSS vorübergehend **auszuschalten**. Einige Templates funktionieren ohne Inlining besser.

Sie können auch Personalisierung für E-Mail-Header und E-Mail-Extras hinzufügen, um zusätzliche Daten an andere E-Mail-Anbieter zurückzusenden.

##### E-Mail-Anhänge {#email-attachments}

Sie können E-Mail-Anhänge auch mit den folgenden Methoden hinzufügen:

{% multi_lang_include email/attachment_upload_options.md %}

Lesen Sie die [E-Mail-Richtlinien]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines) für spezifische Best Practices.

##### E-Mail-Header {#email-headers}

Um E-Mail-Header hinzuzufügen, wählen Sie **Add New Header**. E-Mail-Header enthalten Informationen über die gesendete E-Mail. Diese [Schlüssel-Wert-Paare]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) umfassen typischerweise Sender, Empfänger:in, Authentifizierungsprotokoll und Routing-Informationen. Braze fügt automatisch die RFC-erforderlichen Header-Informationen für E-Mails hinzu, damit diese die Posteingangsanbieter erreichen.

Braze bietet Ihnen die Flexibilität, bei Bedarf zusätzliche E-Mail-Header für erweiterte Anwendungsfälle hinzuzufügen. Es gibt einige reservierte Felder, die von der Braze-Plattform beim Versand überschrieben werden.

Vermeiden Sie die Verwendung der folgenden Schlüssel:

<style>
#reserved-fields td {
    word-break: break-word;
    width: 33%;
}
</style>

<table aria-label="E-Mail-Header" id="reserved-fields">
  <caption>E-Mail-Header</caption>
<thead>
  <tr>
    <th>Reservierte Felder</th>
    <th></th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>BCC</td>
    <td>dkim-signature</td>
    <td>Reply-To</td>
  </tr>
  <tr>
    <td>CC</td>
    <td>From</td>
    <td>Subject</td>
  </tr>
  <tr>
    <td>Content-Transfer-Encoding</td>
    <td>MIME-Version</td>
    <td>To</td>
  </tr>
  <tr>
    <td>Content-Type</td>
    <td>Received</td>
    <td>x-sg-eid</td>
  </tr>
  <tr>
    <td>DKIM-Signature</td>
    <td>received</td>
    <td>x-sg-id</td>
  </tr>
</tbody>
</table>

##### E-Mail-Extras hinzufügen {#adding-email-extras}

E-Mail-Extras ermöglichen es Ihnen, zusätzliche Daten an andere E-Mail-Anbieter zurückzusenden. Dies ist nur für erweiterte Anwendungsfälle relevant, daher sollten Sie E-Mail-Extras nur verwenden, wenn Ihr Unternehmen dies bereits eingerichtet hat.

Um E-Mail-Extras hinzuzufügen, gehen Sie zu **Sending Info** und wählen Sie **Add New Extra**.

{% alert warning %}
Die Gesamtheit der hinzugefügten Schlüssel-Wert-Paare sollte 1 KB nicht überschreiten. Andernfalls werden die Nachrichten abgebrochen.
{% endalert %}

E-Mail-Extra-Werte werden nicht an Currents oder Snowflake veröffentlicht. Wenn Sie zusätzliche Metadaten oder dynamische Werte an Currents oder Snowflake senden möchten, verwenden Sie stattdessen [`message_extras`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras).

### Schritt 3.2: Vorschau und Test Ihrer Nachricht {#step-3b-preview-and-test-your-message}

Nachdem Sie Ihre E-Mail fertiggestellt haben, testen Sie sie vor dem Versand. Wählen Sie am unteren Rand des Übersichtsbildschirms **Preview and Test**.

Hier können Sie eine Vorschau anzeigen, wie Ihre E-Mail im Posteingang von Kund:innen erscheinen wird. Mit der ausgewählten Option **Preview as User** können Sie eine Vorschau Ihrer E-Mail als zufällige:r Nutzer:in anzeigen, eine:n bestimmte:n Nutzer:in auswählen oder eine:n benutzerdefinierte:n Nutzer:in erstellen. So können Sie testen, ob Ihre Connected-Content- und Personalisierungsaufrufe wie erwartet funktionieren.

Anschließend können Sie über **Copy preview link** einen teilbaren Vorschaulink generieren und kopieren, der zeigt, wie die E-Mail für eine:n zufällige:n Nutzer:in aussehen wird. Weitere Informationen finden Sie unter [Teilbare Vorschau]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).

Sie können auch zwischen Desktop-, Mobil- und Nur-Text-Ansichten wechseln, um ein Gefühl dafür zu bekommen, wie Ihre Nachricht in verschiedenen Kontexten erscheinen wird.

{% alert tip %}
Neugierig, wie Ihre E-Mail für Nutzer:innen im Dark Mode aussieht? Wählen Sie den Umschalter **Dark Mode Preview** im Bereich **Preview and Test** (nur im Drag-and-Drop-Editor). Wenn Sie den HTML-Editor verwenden, können Sie das Rendering im Dark Mode der Gmail-Mobile-App dennoch mit [Gmail-Mobile-App und Dark Mode](#gmail-dark-mode) adressieren.
{% endalert %}

Wenn Sie für eine abschließende Prüfung bereit sind, wählen Sie **Test Send** und senden Sie eine Testnachricht an sich selbst oder eine Testergruppe, um zu bestätigen, dass die E-Mail auf verschiedenen Geräten und Clients korrekt angezeigt wird.

![Option „Test Send“ und Beispiel einer E-Mail-Vorschau beim Verfassen Ihrer E-Mail.]({% image_buster /assets/img_archive/newEmailTest.png %})

Wenn Sie Probleme mit Ihrer E-Mail feststellen oder Änderungen vornehmen möchten, wählen Sie **Edit Email**, um zum Editor zurückzukehren.

{% alert tip %}
E-Mail-Clients, die Vorschautext unterstützen, ziehen immer genügend Zeichen ein, um den gesamten verfügbaren Vorschautextbereich zu füllen. Das kann jedoch dazu führen, dass der Vorschautext unvollständig oder nicht optimal erscheint.
<br><br>Um dies zu vermeiden, können Sie nach Ihrem gewünschten Vorschautext Leerraum erstellen, damit E-Mail-Clients keine anderen ablenkenden Texte oder Zeichen in den Umschlaginhalt einziehen. Im Bereich **Sending Settings** können Sie das Kontrollkästchen **Add whitespace after preheader** aktivieren, um automatisch Leerraum hinzuzufügen. <br><br>Alternativ können Sie, wenn Sie mehr Kontrolle benötigen, nach dem gewünschten Vorschautext manuell eine Kette von breitenlosen Nicht-Verbindern (‌`&zwnj;`) und geschützten Leerzeichen (`&nbsp;`) hinzufügen. <br><br>Wenn der folgende Code für den HTML-Editor am Ende Ihres Vorschautexts im Preheader-Bereich hinzugefügt wird, fügt er den gewünschten Leerraum hinzu:<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```

Für den Drag-and-Drop-Editor fügen Sie nur die breitenlosen Nicht-Verbinder (‌`&zwnj;`) ohne die `<div>`-Formatierung direkt im Preheader im Bereich **Sending Settings** hinzu.
{% endalert %}

{% alert note %}
In der Apple-Mail-App müssen Bildlinks in HTML-E-Mails `https://`-URLs verwenden, um anklickbar zu sein. Verwenden Sie sichere Links für jedes Bild, das in ein Anker-Tag eingebettet ist, wenn Sie Klicks von Apple-Mail-Empfänger:innen erwarten.
{% endalert %}

### Schritt 3.3: E-Mail auf Fehler prüfen {#step-33-check-for-email-errors}

Vor dem Versand hebt der Editor häufige Probleme hervor:

- Anzeigename des Absenders und Header nicht gemeinsam festgelegt
- Ungültige Absender- oder Antwortadressen
- Doppelte Header-Schlüssel
- Liquid-Syntaxfehler
- Content Blocks, die ein vollständiges `<!DOCTYPE html>` enthalten
- E-Mail-Text überschreitet 400&nbsp;KB
  - Streben Sie [weniger als 102&nbsp;KB]({{site.baseurl}}/user_guide/channels/email/best_practices/email_styling#email-size) an, um ein Abschneiden zu vermeiden.
- Leerer Text oder Betreff
- Fehlender Abmeldelink
- Absender-Domain nicht auf der Allowlist (Versand wird stark gedrosselt)

## Schritt 4: Erstellen Sie den Rest Ihrer Campaign oder Ihres Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}
Erstellen Sie als Nächstes den Rest Ihrer Campaign. In den folgenden Abschnitten erfahren Sie, wie Sie Braze-Tools zur Erstellung Ihrer E-Mail-Campaign verwenden.

### Zustellungszeitplan oder Trigger wählen {#choose-delivery-schedule-or-trigger}

Stellen Sie E-Mails basierend auf einem geplanten Zeitpunkt, einer Aktion oder einem API-Trigger zu. Weitere Informationen finden Sie unter [Ihre Campaign planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

{% alert note %}
Wenn bei API-getriggerten Campaigns die Trigger-Aktion auf **Mit Campaign interagieren** eingestellt ist, wird durch die Auswahl der Option **Empfangen** als Interaktion Ihre neue Campaign ausgelöst, sobald Braze die ausgewählte Campaign als gesendet markiert – auch wenn die Nachricht bounct oder nicht zugestellt werden kann.
{% endalert %}

Sie können auch die Dauer der Campaign festlegen, [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) angeben und [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)-Regeln einrichten.

### Zielgruppe zusammenstellen {#choose-users-to-target}

Als Nächstes [stellen Sie Ihre Zielgruppe zusammen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users), indem Sie Segments oder Filter auswählen. Braze zeigt eine Live-Vorschau der Segment-Population an, einschließlich der Anzahl der Nutzer:innen, die per E-Mail erreichbar sind. Die genaue Segment-Zugehörigkeit wird unmittelbar vor dem Versand berechnet.

{% multi_lang_include audience/target_audiences.md %}

Sie können die Campaign auch so konfigurieren, dass sie nur an Nutzer:innen mit einem bestimmten [Abo-Status]({{site.baseurl}}/user_guide/channels/email/subscriptions) gesendet wird, z. B. an Nutzer:innen, die E-Mails abonniert haben und per Opt-in zugestimmt haben.

Optional können Sie die Zustellung auch auf eine bestimmte Anzahl von Nutzer:innen innerhalb des Segments begrenzen oder Nutzer:innen erlauben, dieselbe Nachricht bei einer Wiederholung der Campaign erneut zu erhalten.

{% alert note %}
Beim Erstellen einer neuen E-Mail-Campaign ist die Kontrollgruppe standardmäßig auf 20 % eingestellt und kann je nach Bedarf angepasst oder entfernt werden.
{% endalert %}

#### Mehrkanalige Campaigns mit E-Mail und Push {#multichannel-campaigns-with-email-and-push}

Bei mehrkanaligen Campaigns, die sowohl E-Mail- als auch Push-Kanäle ansprechen, möchten Sie Ihre Campaign möglicherweise so einschränken, dass nur Nutzer:innen, die ausdrücklich per Opt-in zugestimmt haben, die Nachricht erhalten (ohne abonnierte oder abgemeldete Nutzer:innen). Angenommen, Sie haben drei Nutzer:innen mit unterschiedlichen Opt-in-Status:

{% multi_lang_include messaging/intelligent_channel_user_examples.md %}

Wählen Sie dazu unter **Zielgruppen-Zusammenfassung** aus, dass diese Campaign nur an „Nur Nutzer:innen mit Opt-in“ gesendet werden soll. Dadurch wird sichergestellt, dass nur Nutzer:innen mit Opt-in Ihre E-Mail erhalten, und Braze sendet Ihre Push-Nachricht standardmäßig nur an Nutzer:innen, die Push aktiviert haben.

{% alert important %}
Schließen Sie bei dieser Konfiguration im Schritt **Zielgruppen** keine Filter ein, die die Zielgruppe auf einen einzelnen Kanal einschränken (z. B. `Foreground Push Enabled = True` oder `Email Subscription = Opted-In`).
{% endalert %}

### Konversions-Events auswählen {#choose-conversion-events}

Braze ermöglicht es Ihnen zu verfolgen, wie oft Nutzer:innen bestimmte Aktionen, sogenannte [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), nach dem Empfang einer Campaign ausführen. Sie können jede der folgenden Aktionen als Konversions-Event festlegen:

- App öffnen
- Kauf tätigen (Dies kann ein allgemeiner Kauf oder ein bestimmter Artikel sein)
- Bestimmtes angepasstes Event ausführen
- E-Mail öffnen

Sie können ein Zeitfenster von bis zu 30 Tagen festlegen, in dem Braze eine Konversion zählt, wenn Nutzer:innen die angegebene Aktion ausführen. Obwohl Braze Öffnungen und Klicks automatisch verfolgt, können Sie das Konversions-Event auf eine Öffnung oder einen Klick setzen, um [Mit BrazeAI<sup>TM</sup> optimieren]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) zu nutzen.
{% endtab %}

{% tab Canvas %}
Wenn Sie es noch nicht getan haben, vervollständigen Sie die verbleibenden Abschnitte Ihrer Canvas-Komponenten. Weitere Informationen zum Aufbau Ihres Canvas, einschließlich multivariatem Testen und [Mit BrazeAI<sup>TM</sup> optimieren]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai), finden Sie unter [Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas).
{% endtab %}
{% endtabs %}

## 5. Schritt: Überprüfen und bereitstellen {#step-5-review-and-deploy}

Im letzten Abschnitt wird die von Ihnen erstellte Campaign zusammengefasst. Bestätigen Sie alle relevanten Details und wählen Sie **Campaign starten** aus.

Informationen darüber, wie Sie auf die Ergebnisse Ihrer E-Mail-Campaigns zugreifen können, finden Sie unter [E-Mail-Berichterstattung]({{site.baseurl}}/user_guide/channels/email/reporting).