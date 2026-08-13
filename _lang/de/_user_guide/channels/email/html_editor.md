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
2. Wählen Sie **E-Mail** oder, für Campaigns, die auf mehrere Kanäle abzielen, **Multichannel**.
3. Geben Sie Ihrer Campaign einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu.
   * Tags erleichtern das Auffinden Ihrer Campaigns und das Erstellen von Berichten. Wenn Sie beispielsweise den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder) verwenden, können Sie nach bestimmten Tags filtern.
5. Fügen Sie so viele Varianten hinzu und benennen Sie sie, wie Sie für Ihre Campaign benötigen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Wenn alle Nachrichten in Ihrer Campaign ähnlich sein oder denselben Inhalt haben werden, verfassen Sie Ihre Nachricht, bevor Sie weitere Varianten hinzufügen. Sie können dann **Aus Variante kopieren** aus dem Dropdown **Variante hinzufügen** auswählen.
{% endalert %}
{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Wenn Sie benutzerdefiniertes HTML erstellen möchten und Hintergründe in der mobilen Gmail-App bei aktiviertem Dark Mode des Geräts konsistent bleiben sollen, lesen Sie [Mobile Gmail-App und Dark-Mode-Hintergrundfarben](#gmail-dark-mode).
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

## 3. Schritt: E-Mail verfassen {#step-3-compose-your-email}

Nachdem Sie Ihr Template ausgewählt haben, sehen Sie eine Übersicht Ihrer E-Mail, von der aus Sie direkt zum Vollbild-Editor springen können, um Ihre E-Mail zu entwerfen, Ihre Versandinformationen zu ändern und Warnungen zur Zustellbarkeit oder Rechtskonformität einzusehen. Sie können beim Verfassen zwischen den Tabs HTML, Klassisch, Klartext und [AMP]({{site.baseurl}}/user_guide/channels/email/customize/amp_for_email) wechseln.

![Der Button „Aus HTML regenerieren“.]({% image_buster /assets/img_archive/regenerate_from_html.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;" }

Braze aktualisiert die Klartextversion automatisch aus der HTML-Version, bis eine Bearbeitung am Klartext erkannt wird. Sobald Braze eine Bearbeitung erkennt, wird die automatische Aktualisierung gestoppt, da davon ausgegangen wird, dass Sie absichtliche Änderungen vorgenommen haben. Um die automatische Synchronisierung wiederherzustellen, gehen Sie zu **Klartext** und wählen Sie **Aus HTML regenerieren** (nur sichtbar, wenn der Klartext nicht synchronisiert wird).

{% alert tip %}
Um Bewegung in einer E-Mail mit einer korrekten Vorschau hinzuzufügen, verwenden Sie GIFs anstelle von Elementen, die JavaScript erfordern, da die meisten Posteingänge JavaScript nicht unterstützen.
{% endalert %}


{% alert important %}
Braze entfernt automatisch HTML-Event-Handler, die als Attribute referenziert werden. Dadurch wird das HTML verändert – überprüfen Sie die E-Mail daher erneut, nachdem Sie fertig sind. Erfahren Sie mehr über [HTML-Handler](https://www.w3schools.com/tags/ref_eventattributes.asp).
{% endalert %}

{% alert tip %}
Brauchen Sie Hilfe beim Erstellen überzeugender Texte? Probieren Sie den [KI-Textassistenten]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy) aus. Geben Sie einen Produktnamen oder eine Beschreibung ein, und die KI generiert menschenähnliche Marketingtexte zur Verwendung in Ihren Nachrichten.

![Button „KI-Texter starten“ im Tab „Body“ des E-Mail-Composers.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

Brauchen Sie Hilfe beim Erstellen von Nachrichten mit Rechts-nach-links-Schrift für Sprachen wie Arabisch und Hebräisch? Lesen Sie [Rechts-nach-links-Nachrichten erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages) für Best Practices.

### Gmail-App für Mobilgeräte und Dark Mode {#gmail-dark-mode}

Die Gmail-App für Mobilgeräte (Android und iOS) kann Hintergrundfarben invertieren, wenn sich das Gerät im Dark Mode befindet. Das kann Layouts beeinträchtigen, bei denen der E-Mail-Hintergrund mit einer Bildkante oder einer bestimmten Markenfarbe übereinstimmen soll.

Um dies zu vermeiden, verwenden Sie in der Tabellenzelle, die einen stabilen Hintergrund benötigt, einen einfarbigen CSS-`linear-gradient` anstelle von `background-color`. Gmail invertiert diese Behandlung weniger wahrscheinlich als eine flache Hintergrundfarbe.

Um beispielsweise einen weißen Hintergrund in einer Zelle beizubehalten, verwenden Sie Folgendes:

```html
<td style="background-image: linear-gradient(#ffffff, #ffffff);">
```

Ersetzen Sie `#ffffff` durch Ihre gewünschte Farbe.

{% alert note %}
Dieser Ansatz funktioniert nicht zuverlässig bei `<table aria-label="Gmail mobile app and dark mode #gmail-dark-mode">`-Elementen allein. Setzen Sie den Gradienten daher auf die Zelle statt nur auf die Tabelle.
  <caption>Gmail-App für Mobilgeräte und Dark Mode</caption>
{% endalert %}

Weitere Informationen zur Gradient-Syntax finden Sie unter [CSS-Gradienten auf W3Schools](https://www.w3schools.com/css/css3_gradients.asp).

### Schritt 3.1: Versandinformationen hinzufügen {#step-31-add-your-sending-information}

Nachdem Sie Ihre E-Mail-Nachricht entworfen und erstellt haben, fügen Sie Ihre Versandinformationen unter **Versandeinstellungen** hinzu.

{% multi_lang_include email/sending_info_steps.md %}

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Eine Vorschau im rechten Panel wird mit den von Ihnen hinzugefügten Versandinformationen befüllt. Diese Informationen können auch aktualisiert werden, indem Sie zu **Einstellungen** > **E-Mail-Präferenzen** > **Versandkonfiguration** gehen.

#### Erweitert {#advanced}

Aktivieren Sie unter **Versandeinstellungen** > **Erweitert** die Option **Inline-CSS** für die breiteste Client-Unterstützung. Wenn Nachrichten abgeschnitten werden oder Bilder auf Zeilenhöhe gestreckt werden, versuchen Sie, Inline-CSS vorübergehend **auszuschalten**. Einige Templates verhalten sich ohne Inlining besser.

Sie können auch Personalisierung für E-Mail-Header und E-Mail-Extras hinzufügen, um zusätzliche Daten an andere E-Mail-Anbieter zurückzusenden.

##### E-Mail-Anhänge {#email-attachments}

Sie können E-Mail-Anhänge auch mit den folgenden Methoden hinzufügen:

{% multi_lang_include email/attachment_upload_options.md %}

Lesen Sie die [E-Mail-Richtlinien]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines) für spezifische Best Practices, die Sie berücksichtigen sollten.

##### E-Mail-Header {#email-headers}

Um E-Mail-Header hinzuzufügen, wählen Sie **Neuen Header hinzufügen**. E-Mail-Header enthalten Informationen über die gesendete E-Mail. Diese [Schlüssel-Wert-Paare]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) umfassen in der Regel Absender-, Empfänger:innen-, Authentifizierungsprotokoll- und Routing-Informationen. Braze fügt automatisch die gemäß RFC erforderlichen Header-Informationen hinzu, damit E-Mails die Posteingangsanbieter erreichen.

Braze bietet Ihnen die Flexibilität, bei Bedarf zusätzliche E-Mail-Header für erweiterte Anwendungsfälle hinzuzufügen. Es gibt einige reservierte Felder, die die Braze-Plattform beim Versand überschreibt.

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

Um E-Mail-Extras hinzuzufügen, gehen Sie zu **Versandinformationen** und wählen Sie **Neues Extra hinzufügen**.

{% alert warning %}
Die Gesamtmenge der hinzugefügten Schlüssel-Wert-Paare sollte 1 KB nicht überschreiten. Andernfalls werden die Nachrichten abgebrochen.
{% endalert %}

E-Mail-Extra-Werte werden nicht an Currents oder Snowflake veröffentlicht. Wenn Sie zusätzliche Metadaten oder dynamische Werte an Currents oder Snowflake senden möchten, verwenden Sie stattdessen [`message_extras`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras).

### Schritt 3.2: Nachricht in der Vorschau anzeigen und testen {#step-3b-preview-and-test-your-message}

Nachdem Sie Ihre E-Mail fertig verfasst haben, testen Sie sie vor dem Versand. Wählen Sie am unteren Rand des Übersichtsbildschirms **Vorschau und Test**.

Hier können Sie eine Vorschau anzeigen, wie Ihre E-Mail im Posteingang von Kund:innen erscheint. Mit der ausgewählten Option **Als Nutzer:in anzeigen** können Sie Ihre E-Mail als zufällige:r Nutzer:in in der Vorschau anzeigen, eine:n bestimmte:n Nutzer:in auswählen oder eine:n angepasste:n Nutzer:in erstellen. So können Sie testen, ob Ihre Connected-Content- und Personalisierungsaufrufe wie erwartet funktionieren.

Anschließend können Sie **Vorschau-Link kopieren**, um einen teilbaren Vorschau-Link zu generieren und zu kopieren, der zeigt, wie die E-Mail für eine:n zufällige:n Nutzer:in aussehen wird. Weitere Informationen finden Sie unter [Teilbare Vorschau]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).

Sie können auch zwischen Desktop-, Mobil- und Klartextansichten wechseln, um ein Gefühl dafür zu bekommen, wie Ihre Nachricht in verschiedenen Kontexten erscheint.

{% alert tip %}
Neugierig, wie Ihre E-Mail für Dark-Mode-Nutzer:innen aussieht? Wählen Sie den Umschalter **Dark-Mode-Vorschau** im Bereich **Vorschau und Test** (nur Drag-and-Drop-Editor). Wenn Sie den HTML-Editor verwenden, können Sie das Gmail-Dark-Mode-Rendering für Mobilgeräte dennoch mit [Gmail-App für Mobilgeräte und Dark Mode](#gmail-dark-mode) adressieren.
{% endalert %}

Wenn Sie für eine abschließende Prüfung bereit sind, wählen Sie **Testversand** und senden Sie eine Testnachricht an sich selbst oder eine Testergruppe, um zu bestätigen, dass die E-Mail auf verschiedenen Geräten und Clients korrekt angezeigt wird.

![Option „Testversand“ und Beispiel-E-Mail-Vorschau beim Verfassen Ihrer E-Mail.]({% image_buster /assets/img_archive/newEmailTest.png %})

Wenn Sie Probleme mit Ihrer E-Mail feststellen oder Änderungen vornehmen möchten, wählen Sie **E-Mail bearbeiten**, um zum Editor zurückzukehren.

{% alert tip %}
E-Mail-Clients, die Vorschautext unterstützen, ziehen immer genügend Zeichen ein, um den gesamten verfügbaren Vorschautextbereich zu füllen. Dies kann jedoch dazu führen, dass der Vorschautext unvollständig oder nicht optimal ist.
<br><br>Um dies zu vermeiden, können Sie nach Ihrem gewünschten Vorschautext Leerraum erstellen, damit E-Mail-Clients keinen anderen ablenkenden Text oder Zeichen in den Umschlaginhalt ziehen. Im Bereich **Versandeinstellungen** können Sie das Kontrollkästchen **Leerraum nach Preheader hinzufügen** aktivieren, um automatisch Leerraum hinzuzufügen. <br><br>Alternativ können Sie, wenn Sie mehr Kontrolle benötigen, manuell eine Kette von breitenlosen Nicht-Verbindern (‌`&zwnj;`) und geschützten Leerzeichen (`&nbsp;`) nach dem Vorschautext hinzufügen, der angezeigt werden soll. <br><br>Wenn Sie den folgenden Code am Ende Ihres Vorschautexts im Preheader-Bereich für den HTML-Editor hinzufügen, wird der gewünschte Leerraum erzeugt:<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```

Für den Drag-and-Drop-Editor fügen Sie nur die breitenlosen Nicht-Verbinder (‌`&zwnj;`) ohne die `<div>`-Formatierung direkt im Preheader im Bereich **Versandeinstellungen** hinzu.
{% endalert %}

{% alert note %}
In der Apple-Mail-App müssen Bild-Links in HTML-E-Mails `https://`-URLs verwenden, um klickbar zu sein. Verwenden Sie sichere Links für jedes Bild, das in einem Anker-Tag eingebettet ist, wenn Sie Klicks von Apple-Mail-Empfänger:innen erwarten.
{% endalert %}

### Schritt 3.3: Auf E-Mail-Fehler prüfen {#step-33-check-for-email-errors}

Vor dem Versand markiert der Editor häufige Probleme:

- Absender-Anzeigename und Header nicht gemeinsam festgelegt
- Ungültige Absender- oder Antwortadressen
- Doppelte Header-Schlüssel
- Liquid-Syntaxfehler
- Content Blocks, die ein vollständiges `<!DOCTYPE html>` enthalten
- E-Mail-Body ist über 400&nbsp;KB groß
  - Streben Sie [weniger als 102&nbsp;KB]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips#email-size) an, um ein Abschneiden zu vermeiden.
- Leerer Body oder Betreff
- Fehlender Abmeldelink
- Absender-Domain nicht auf der Allowlist (Versand wird stark gedrosselt)

## Schritt 4: Den Rest Ihrer Campaign oder Ihres Canvas erstellen {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}
Erstellen Sie als Nächstes den Rest Ihrer Campaign. In den folgenden Abschnitten erfahren Sie, wie Sie die Braze-Tools zum Erstellen Ihrer E-Mail-Campaign verwenden.

### Zustellungszeitplan oder Trigger wählen {#choose-delivery-schedule-or-trigger}

Stellen Sie E-Mails basierend auf einem geplanten Zeitpunkt, einer Aktion oder einem API-Trigger zu. Weitere Informationen finden Sie unter [Ihre Campaign planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

{% alert note %}
Wenn bei API-getriggerten Campaigns die Trigger-Aktion auf **Mit Campaign interagieren** eingestellt ist, bewirkt die Auswahl einer **Empfangen**-Option als Interaktion, dass Ihre neue Campaign ausgelöst wird, sobald Braze die ausgewählte Campaign als gesendet markiert – auch wenn die Nachricht einen Bounce verursacht oder nicht zugestellt werden kann.
{% endalert %}

Sie können auch die Dauer der Campaign festlegen, [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) angeben und Regeln für das [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping) einrichten.

### Zielgruppe zusammenstellen {#choose-users-to-target}

Als Nächstes können Sie [Nutzer:innen ansprechen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users), indem Sie Segments oder Filter auswählen. Braze zeigt eine Live-Vorschau der Segment-Population an, einschließlich der Anzahl der Nutzer:innen, die per E-Mail erreichbar sind. Die genaue Segment-Zugehörigkeit wird unmittelbar vor dem Versand berechnet.

{% multi_lang_include audience/target_audiences.md %}

Sie können auch festlegen, dass Ihre Campaign nur an Nutzer:innen mit einem bestimmten [Abo-Status]({{site.baseurl}}/user_guide/channels/email/subscriptions) gesendet wird, z. B. an diejenigen, die abonniert und für E-Mails angemeldet sind.

Optional können Sie die Zustellung auch auf eine bestimmte Anzahl von Nutzer:innen innerhalb des Segments beschränken oder Nutzer:innen erlauben, dieselbe Nachricht bei einer Wiederholung der Campaign erneut zu erhalten.

{% alert note %}
Beim Erstellen einer neuen E-Mail-Campaign ist die Kontrollgruppe standardmäßig auf 20 % eingestellt und kann je nach Bedarf für Ihre Campaign angepasst oder entfernt werden.
{% endalert %}

#### Multichannel-Campaigns mit E-Mail und Push {#multichannel-campaigns-with-email-and-push}

Bei Multichannel-Campaigns, die sowohl E-Mail- als auch Push-Kanäle ansprechen, möchten Sie Ihre Campaign möglicherweise so einschränken, dass nur Nutzer:innen, die ausdrücklich angemeldet sind, die Nachricht erhalten (unter Ausschluss von abonnierten oder abgemeldeten Nutzer:innen). Angenommen, Sie haben drei Nutzer:innen mit unterschiedlichem Opt-in-Status:

{% multi_lang_include messaging/intelligent_channel_user_examples.md %}

Wählen Sie dazu unter **Zielgruppenübersicht** aus, diese Campaign nur an „nur angemeldete Nutzer:innen“ zu senden. Diese Option stellt sicher, dass nur angemeldete Nutzer:innen Ihre E-Mail erhalten, und Braze sendet Ihre Push-Nachricht standardmäßig nur an Nutzer:innen, die Push aktiviert haben.

{% alert important %}
Fügen Sie bei dieser Konfiguration im Schritt **Zielgruppen** keine Filter hinzu, die die Zielgruppe auf einen einzelnen Kanal beschränken (z. B. `Foreground Push Enabled = True` oder `Email Subscription = Opted-In`).
{% endalert %}

### Konversions-Events auswählen {#choose-conversion-events}

Braze ermöglicht es Ihnen, nachzuverfolgen, wie oft Nutzer:innen bestimmte Aktionen, sogenannte [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), nach dem Empfang einer Campaign ausführen. Sie können jede der folgenden Aktionen als Konversions-Event festlegen:

- App öffnen
- Kauf tätigen (Dies kann ein allgemeiner Kauf oder ein bestimmter Artikel sein)
- Bestimmtes angepasstes Event ausführen
- E-Mail öffnen

Sie können ein Zeitfenster von bis zu 30 Tagen festlegen, in dem Braze eine Konversion zählt, wenn Nutzer:innen die angegebene Aktion ausführen. Obwohl Braze Öffnungen und Klicks automatisch erfasst, können Sie das Konversions-Event auf eine Öffnung oder einen Klick setzen, um die [intelligente Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection) zu verwenden.
{% endtab %}

{% tab Canvas %}
Falls noch nicht geschehen, vervollständigen Sie die verbleibenden Abschnitte Ihrer Canvas-Komponenten. Weitere Informationen zum Aufbau des restlichen Canvas, zur Implementierung multivariater Tests und der intelligenten Auswahl und mehr finden Sie im Schritt [Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas) unserer Canvas-Dokumentation.
{% endtab %}
{% endtabs %}

## 5. Schritt: Überprüfen und bereitstellen {#step-5-review-and-deploy}

Der letzte Abschnitt fasst die von Ihnen gestaltete Campaign zusammen. Bestätigen Sie alle relevanten Details und wählen Sie **Campaign starten**.

Informationen darüber, wie Sie auf die Ergebnisse Ihrer E-Mail-Campaigns zugreifen können, finden Sie unter [E-Mail-Reporting]({{site.baseurl}}/user_guide/channels/email/reporting).