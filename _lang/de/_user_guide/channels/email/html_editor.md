---
nav_title: HTML-Editor
article_title: Eine E-Mail mit angepasstem HTML erstellen
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie eine E-Mail mit der Braze-Plattform erstellen. Enthalten sind Best Practices zum Verfassen Ihrer Nachrichten, zur Vorschau Ihrer Inhalte und zur Planung Ihrer Kampagne oder Ihres Canvas."
tool:
  - Campaigns
channel:
  - email
search_rank: 1
---

# Eine E-Mail mit angepasstem HTML erstellen {#create-an-email-with-custom-html}

> E-Mail-Nachrichten eignen sich hervorragend, um Ihren Nutzer:innen Inhalte nach deren Wünschen zu liefern. Sie sind auch ausgezeichnete Werkzeuge, um Nutzer:innen erneut zu aktivieren, die Ihre App möglicherweise sogar deinstalliert haben. Das Senden von individuell angepassten E-Mail-Nachrichten verbessert das Nutzererlebnis und hilft Ihren Nutzer:innen, den größtmöglichen Mehrwert aus Ihrer App zu ziehen.

Beispiele für E-Mail-Kampagnen finden Sie in unseren [Fallstudien](https://www.braze.com/customers).

{% alert tip %}
Wenn Sie zum ersten Mal eine E-Mail-Kampagne erstellen, empfehlen wir Ihnen dringend, diese Braze-Lernkurse zu absolvieren:<br><br>
- [E-Mail-Opt-ins und Berechtigungen](https://learning.braze.com/messaging-channels-email)
- [Projekt: Ein einfaches E-Mail-Marketing-Programm erstellen](https://learning.braze.com/project-build-a-basic-email-marketing-program)
{% endalert %}

## Schritt 1: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten {#step-1-choose-where-to-build-your-message}

Verwenden Sie Campaigns für einfache, einzelne Nachrichten. Verwenden Sie Canvases für mehrstufige Nutzer-Journeys.

{% tabs %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Create Campaign**.
2. Wählen Sie **Email** oder, für Campaigns, die mehrere Kanäle ansprechen, **Multichannel**.
3. Geben Sie Ihrer Campaign einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) hinzu.
   * Tags erleichtern das Auffinden Ihrer Campaigns und das Erstellen von Berichten. Wenn Sie beispielsweise den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder/) verwenden, können Sie nach bestimmten Tags filtern.
5. Fügen Sie so viele Varianten hinzu und benennen Sie sie, wie Sie für Ihre Campaign benötigen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% alert tip %}
Wenn alle Nachrichten in Ihrer Campaign ähnlich sein oder denselben Inhalt haben werden, verfassen Sie Ihre Nachricht, bevor Sie zusätzliche Varianten hinzufügen. Anschließend können Sie im Dropdown **Variante hinzufügen** die Option **Von Variante kopieren** wählen.
{% endalert %}
{% endtab %}
{% tab Canvas %}

1. [Erstellen Sie Ihren Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) mit dem Canvas-Composer.
2. Nachdem Sie Ihren Canvas eingerichtet haben, fügen Sie im Canvas-Builder einen Schritt hinzu. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie einen [Schritt-Zeitplan]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#schedule-delay) und legen Sie bei Bedarf eine Verzögerung fest.
4. Filtern Sie die Zielgruppe für diesen Schritt nach Bedarf. Sie können die Empfänger:innen dieses Schritts weiter eingrenzen, indem Sie Segmente angeben und zusätzliche Filter hinzufügen. Die Zielgruppenoptionen werden nach der Verzögerung zum Zeitpunkt des Nachrichtenversands überprüft.
5. Wählen Sie Ihr [Fortschrittsverhalten]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/).
6. Wählen Sie alle weiteren Messaging-Kanäle, die Sie mit Ihrer Nachricht kombinieren möchten.
{% endtab %}
{% endtabs %}

{% alert tip %}
Wenn Sie angepasstes HTML erstellen möchten und Hintergründe in der Gmail-Mobil-App bei aktiviertem Dark Mode des Geräts konsistent bleiben sollen, lesen Sie [Gmail-Mobil-App und Dark-Mode-Hintergrundfarben](#gmail-dark-mode).
{% endalert %}

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='email html editor' %}

## Schritt 2: Wählen Sie Ihre Bearbeitungserfahrung {#step-2-choose-your-template-and-compose-your-email}

Braze bietet zwei Bearbeitungserfahrungen beim Erstellen einer E-Mail-Kampagne: unseren [Drag-and-Drop-Editor]({{site.baseurl}}/dnd/) und unseren Standard-HTML-Editor. Wählen Sie die entsprechende Kachel für die Bearbeitungserfahrung, die Sie bevorzugen.

![Auswahl zwischen dem Drag-and-Drop-Editor, dem HTML-Editor oder Templates für Ihre E-Mail-Bearbeitungserfahrung.]({% image_buster /assets/img_archive/choose_email_creation.png %}){: style="max-width:75%" }

Anschließend können Sie entweder ein vorhandenes [E-Mail-Template]({{site.baseurl}}/user_guide/channels/email/html_editor/#creating-an-email-template) auswählen, ein [Template hochladen]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template/) (nur HTML-Editor) oder ein leeres Template verwenden.

Wenn Sie den HTML-Editor verwenden und Hintergrundfarben in der Gmail-Mobil-App bei aktiviertem Dark Mode des Geräts konsistent bleiben sollen, lesen Sie [Gmail-Mobil-App und Dark-Mode-Hintergrundfarben](#gmail-dark-mode).

{% alert tip %}
Wir empfehlen, pro E-Mail-Kampagne eine Bearbeitungserfahrung auszuwählen. Wählen Sie beispielsweise entweder den **HTML Classic**- oder den **Block-Editor** in einer einzelnen E-Mail-Kampagne, anstatt zwischen Editoren zu wechseln.
{% endalert %}

## Schritt 3: Verfassen Sie Ihre E-Mail {#step-3-compose-your-email}

Nachdem Sie Ihr Template ausgewählt haben, sehen Sie eine Übersicht Ihrer E-Mail, von der aus Sie direkt zum Vollbild-Editor springen können, um Ihre E-Mail zu entwerfen, Ihre Sendeinformationen zu ändern und Warnungen zur Zustellbarkeit oder Rechtskonformität einzusehen. Sie können beim Verfassen zwischen den Tabs HTML, Classic, Klartext und [AMP]({{site.baseurl}}/user_guide/channels/email/customize/amp_for_email/) wechseln.

![Der Button „Aus HTML regenerieren“.]({% image_buster /assets/img_archive/regenerate_from_html.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;" }

Braze aktualisiert die Klartext-Version automatisch aus der HTML-Version, bis eine Bearbeitung am Klartext erkannt wird. Sobald Braze eine Bearbeitung erkennt, wird die automatische Aktualisierung gestoppt, da davon ausgegangen wird, dass Sie absichtliche Änderungen vorgenommen haben. Um die automatische Synchronisierung wiederherzustellen, gehen Sie zu **Plaintext** und wählen Sie **Regenerate from HTML** (nur sichtbar, wenn der Klartext nicht synchronisiert wird).

{% alert tip %}
Um Bewegung in einer E-Mail mit genauer Vorschau hinzuzufügen, verwenden Sie GIFs anstelle von Elementen, die JavaScript erfordern, da die meisten Postfächer JavaScript nicht unterstützen.
{% endalert %}


{% alert important %}
Braze entfernt automatisch HTML-Event-Handler, die als Attribute referenziert werden. Dadurch wird das HTML modifiziert – überprüfen Sie die E-Mail daher erneut, nachdem Sie fertig sind. Erfahren Sie mehr über [HTML-Handler](https://www.w3schools.com/tags/ref_eventattributes.asp).
{% endalert %}

{% alert tip %}
Brauchen Sie Hilfe beim Erstellen großartiger Texte? Probieren Sie den [KI-Textassistenten]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/) aus. Geben Sie einen Produktnamen oder eine Beschreibung ein, und die KI generiert menschenähnliche Marketingtexte für Ihre Nachrichten.

![Button „KI-Texter starten“ im Tab „Body“ des E-Mail-Composers.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

Brauchen Sie Hilfe beim Erstellen von Rechts-nach-Links-Nachrichten für Sprachen wie Arabisch und Hebräisch? Lesen Sie [Rechts-nach-Links-Nachrichten erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/) für Best Practices.

### Gmail-Mobil-App und Dark Mode {#gmail-dark-mode}

Die Gmail-Mobil-App (Android und iOS) kann Hintergrundfarben invertieren, wenn sich das Gerät im Dark Mode befindet. Das kann Layouts beeinträchtigen, bei denen der E-Mail-Hintergrund mit einer Bildkante oder einer bestimmten Markenfarbe übereinstimmen soll.

Um dies zu vermeiden, verwenden Sie in der Tabellenzelle, die einen stabilen Hintergrund benötigt, einen einfarbigen CSS-`linear-gradient` anstelle von `background-color`. Gmail invertiert diese Behandlung weniger wahrscheinlich als eine flache Hintergrundfarbe.

Um beispielsweise einen weißen Hintergrund auf einer Zelle beizubehalten, verwenden Sie Folgendes:

```html
<td style="background-image: linear-gradient(#ffffff, #ffffff);">
```

Ersetzen Sie `#ffffff` durch Ihre gewünschte Farbe.

{% alert note %}
Dieser Ansatz funktioniert nicht zuverlässig allein auf `<table>`-Elementen. Setzen Sie den Gradienten daher auf die Zelle statt nur auf die Tabelle.
{% endalert %}

Weitere Informationen zur Gradient-Syntax finden Sie unter [CSS-Gradienten auf W3Schools](https://www.w3schools.com/css/css3_gradients.asp).

### Schritt 3.1: Sendeinformationen hinzufügen {#step-31-add-your-sending-information}

Nachdem Sie Ihre E-Mail-Nachricht fertig gestaltet und erstellt haben, fügen Sie Ihre Sendeinformationen unter **Sending Settings** hinzu.

1. Wählen Sie unter **Sending Info** eine E-Mail als **From Display Name + Address** aus. Sie können dies auch anpassen, indem Sie **Customize From Display Name + Address** wählen.
2. Wählen Sie eine E-Mail als **Reply-To Address** aus. Sie können dies auch anpassen, indem Sie **Customize Reply-To Address** wählen.
3. Wählen Sie als Nächstes eine E-Mail als **BCC Address** aus, um Ihre E-Mail für diese Adresse sichtbar zu machen.
4. Fügen Sie Ihrer E-Mail eine Betreffzeile hinzu. Optional können Sie auch einen Preheader und Leerraum nach dem Preheader hinzufügen.

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Eine Vorschau im rechten Panel wird mit den von Ihnen hinzugefügten Sendeinformationen befüllt. Diese Informationen können auch aktualisiert werden, indem Sie zu **Settings** > **Email Preferences** > **Sending Configuration** gehen.

#### Erweitert {#advanced}

Unter **Sending Settings** > **Advanced** aktivieren Sie **Inline-CSS** für die breiteste Client-Unterstützung. Wenn Nachrichten abgeschnitten werden oder Bilder auf Zeilenhöhe gestreckt werden, versuchen Sie, Inline-CSS vorübergehend zu **deaktivieren**. Einige Templates verhalten sich ohne Inlining besser.

Sie können auch Personalisierung für E-Mail-Header und E-Mail-Extras hinzufügen, um zusätzliche Daten an andere E-Mail-Anbieter zurückzusenden.

##### E-Mail-Anhänge {#email-attachments}

Sie können E-Mail-Anhänge auch mit den folgenden Methoden hinzufügen:

- **Datei hochladen:** Ziehen Sie eine Datei per Drag-and-Drop oder durchsuchen Sie Ihren Computer, um eine Datei direkt hochzuladen. Braze validiert den Dateityp und die Größe (standardmäßig bis zu 2&nbsp;MB) vor dem Hochladen, anschließend werden diese Dateien in die Medienbibliothek hochgeladen. Dateien, die das Limit von 2&nbsp;MB überschreiten, können nicht hochgeladen werden.
- **Medienbibliothek verwenden:** Durchsuchen und wählen Sie aus bereits in der [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/) gespeicherten Assets. PDFs, Word-Dokumente, Excel-Dateien und PowerPoint-Präsentationen werden unterstützt.
- **Von URL hinzufügen:** Geben Sie eine URL ein, die auf die Datei verweist, und geben Sie einen Anzeige-Dateinamen an. Da Braze beliebige URLs während der E-Mail-Erstellung nicht auf ihre Größe prüfen kann, wird die Dateigröße zum Sendezeitpunkt erzwungen. Beachten Sie, dass Liquid in diesem Feld nicht unterstützt wird.

Spezifische Best Practices finden Sie unter [E-Mail-Richtlinien]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines/).

##### E-Mail-Header {#email-headers}

Um E-Mail-Header hinzuzufügen, wählen Sie **Add New Header**. E-Mail-Header enthalten Informationen über die gesendete E-Mail. Diese [Schlüssel-Wert-Paare]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs/) umfassen typischerweise Absender, Empfänger:in, Authentifizierungsprotokoll und Routing-Informationen. Braze fügt automatisch die RFC-erforderlichen Header-Informationen hinzu, damit E-Mails die Postfach-Anbieter erreichen.

Braze bietet Ihnen die Flexibilität, bei Bedarf zusätzliche E-Mail-Header für erweiterte Anwendungsfälle hinzuzufügen. Es gibt einige reservierte Felder, die die Braze-Plattform beim Senden überschreibt.

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
Die Gesamtmenge der hinzugefügten Schlüssel-Wert-Paare sollte 1 KB nicht überschreiten. Andernfalls werden die Nachrichten abgebrochen.
{% endalert %}

E-Mail-Extra-Werte werden nicht an Currents oder Snowflake veröffentlicht. Wenn Sie zusätzliche Metadaten oder dynamische Werte an Currents oder Snowflake senden möchten, verwenden Sie stattdessen [`message_extras`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras/).

### Schritt 3.2: Vorschau und Test Ihrer Nachricht {#step-3b-preview-and-test-your-message}

Nachdem Sie Ihre E-Mail fertig verfasst haben, testen Sie sie vor dem Senden. Wählen Sie am unteren Rand des Übersichtsbildschirms **Preview and Test**.

Hier können Sie eine Vorschau sehen, wie Ihre E-Mail im Postfach erscheint. Mit der ausgewählten Option **Preview as User** können Sie Ihre E-Mail als zufällige:r Nutzer:in anzeigen, eine:n bestimmte:n Nutzer:in auswählen oder eine:n angepasste:n Nutzer:in erstellen. So können Sie testen, ob Ihre Connected-Content- und Personalisierungsaufrufe wie erwartet funktionieren.

Anschließend können Sie **Copy preview link** wählen, um einen teilbaren Vorschau-Link zu generieren und zu kopieren, der zeigt, wie die E-Mail für eine:n zufällige:n Nutzer:in aussehen wird. Der Link ist sieben Tage gültig, bevor er neu generiert werden muss.

Sie können auch zwischen Desktop-, Mobil- und Klartext-Ansichten wechseln, um ein Gefühl dafür zu bekommen, wie Ihre Nachricht in verschiedenen Kontexten erscheint.

{% alert tip %}
Möchten Sie wissen, wie Ihre E-Mail für Dark-Mode-Nutzer:innen aussieht? Wählen Sie den Schalter **Dark Mode Preview** im Bereich **Preview and Test** (nur Drag-and-Drop-Editor). Wenn Sie den HTML-Editor verwenden, können Sie das Gmail-Mobil-Dark-Mode-Rendering dennoch mit [Gmail-Mobil-App und Dark Mode](#gmail-dark-mode) adressieren.
{% endalert %}

Wenn Sie bereit für eine abschließende Prüfung sind, wählen Sie **Test Send** und senden Sie eine Testnachricht an sich selbst oder eine Testergruppe, um zu bestätigen, dass die E-Mail auf verschiedenen Geräten und Clients korrekt angezeigt wird.

![Test-Send-Option und Beispiel-E-Mail-Vorschau beim Verfassen Ihrer E-Mail.]({% image_buster /assets/img_archive/newEmailTest.png %})

Wenn Sie Probleme mit Ihrer E-Mail feststellen oder Änderungen vornehmen möchten, wählen Sie **Edit Email**, um zum Editor zurückzukehren.

{% alert tip %}
E-Mail-Clients, die Vorschautext unterstützen, ziehen immer genügend Zeichen ein, um den gesamten verfügbaren Vorschautext-Bereich zu füllen. Dies kann jedoch dazu führen, dass der Vorschautext unvollständig oder nicht optimal ist.
<br><br>Um dies zu vermeiden, können Sie nach Ihrem gewünschten Vorschautext Leerraum erstellen, damit E-Mail-Clients keinen anderen ablenkenden Text oder Zeichen in den Umschlaginhalt ziehen. Fügen Sie dazu eine Kette von Zero-Width-Non-Joinern (‌`&zwnj;`) und geschützten Leerzeichen (`&nbsp;`) nach dem Vorschautext hinzu, der angezeigt werden soll. <br><br>Wenn Sie den folgenden Code am Ende Ihres Vorschautexts im Preheader-Bereich des HTML-Editors hinzufügen, wird der gewünschte Leerraum erzeugt:<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```

Für den Drag-and-Drop-Editor fügen Sie nur die Zero-Width-Non-Joiner (‌`&zwnj;`) ohne die `<div>`-Formatierung direkt im Preheader im Bereich **Sending Settings** hinzu.
{% endalert %}

{% alert note %}
In der Apple-Mail-App müssen Bild-Links in HTML-E-Mails `https://`-URLs verwenden, um klickbar zu sein. Verwenden Sie sichere Links für jedes Bild, das in einem Anker-Tag eingebettet ist, wenn Sie Klicks von Apple-Mail-Empfänger:innen erwarten.
{% endalert %}

### Schritt 3.3: Auf E-Mail-Fehler prüfen {#step-33-check-for-email-errors}

Vor dem Senden markiert der Editor häufige Probleme:

- Anzeigename und Header des Absenders nicht gemeinsam festgelegt
- Ungültige Absender- oder Antwort-Adressen
- Doppelte Header-Schlüssel
- Liquid-Syntaxfehler
- Content Blocks, die ein vollständiges `<!DOCTYPE html>` enthalten
- E-Mail-Body ist über 400&nbsp;KB groß
  - Streben Sie [weniger als 102&nbsp;KB]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#email-size) an, um Abschneiden zu vermeiden.
- Leerer Body oder Betreff
- Fehlender Abmeldelink
- Absender-Domain nicht auf der Allowlist (Versand wird stark gedrosselt)

## Schritt 4: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}
Erstellen Sie als Nächstes den Rest Ihrer Campaign. In den folgenden Abschnitten finden Sie Details zur Verwendung der Braze-Tools zum Erstellen Ihrer E-Mail-Kampagne.

#### Zustellungszeitplan oder Trigger wählen {#choose-delivery-schedule-or-trigger}

Liefern Sie E-Mails basierend auf einem geplanten Zeitpunkt, einer Aktion oder einem API-Trigger. Weitere Informationen finden Sie unter [Ihre Campaign planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).

{% alert note %}
Bei API-getriggerten Campaigns, bei denen die Trigger-Aktion auf **Mit Campaign interagieren** eingestellt ist, führt die Auswahl einer **Empfangen**-Option als Interaktion dazu, dass Ihre neue Campaign ausgelöst wird, sobald Braze die ausgewählte Campaign als gesendet markiert, selbst wenn diese Nachricht bounct oder nicht zugestellt werden kann.
{% endalert %}

Sie können auch die Dauer der Campaign festlegen, [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/) angeben und [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping)-Regeln einrichten.

#### Zielnutzer:innen auswählen {#choose-users-to-target}

Als Nächstes [stellen Sie Ihre Zielgruppe zusammen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/), indem Sie Segmente oder Filter auswählen. Braze zeigt eine Live-Vorschau der Segment-Population an, einschließlich der Anzahl der per E-Mail erreichbaren Nutzer:innen. Die genaue Segment-Zugehörigkeit wird kurz vor dem Versand berechnet.

{% multi_lang_include target_audiences.md %}

Sie können auch wählen, Ihre Campaign nur an Nutzer:innen mit einem bestimmten [Abo-Status]({{site.baseurl}}/user_guide/channels/email/subscriptions/) zu senden, z. B. an diejenigen, die abonniert und für E-Mail angemeldet sind.

Optional können Sie die Zustellung auch auf eine bestimmte Anzahl von Nutzer:innen innerhalb des Segments begrenzen oder Nutzer:innen erlauben, dieselbe Nachricht bei einer Wiederholung der Campaign zweimal zu erhalten.

{% alert note %}
Beim Erstellen einer neuen E-Mail-Kampagne ist die Kontrollgruppe standardmäßig auf 20 % eingestellt und kann je nach Bedarf für Ihre Campaign angepasst oder entfernt werden.
{% endalert %}

##### Multichannel-Campaigns mit E-Mail und Push {#multichannel-campaigns-with-email-and-push}

Bei Multichannel-Campaigns, die sowohl E-Mail- als auch Push-Kanäle ansprechen, möchten Sie Ihre Campaign möglicherweise so einschränken, dass nur Nutzer:innen die Nachricht erhalten, die ausdrücklich angemeldet sind (unter Ausschluss von abonnierten oder abgemeldeten Nutzer:innen). Nehmen wir beispielsweise an, Sie haben drei Nutzer:innen mit unterschiedlichem Opt-in-Status:

- **Nutzer:in A** ist für E-Mail abonniert und Push-aktiviert. Diese Person erhält die E-Mail nicht, wird aber den Push erhalten.
- **Nutzer:in B** ist für E-Mail angemeldet, aber nicht Push-aktiviert. Diese Person wird die E-Mail erhalten, erhält aber nicht den Push.
- **Nutzer:in C** ist für E-Mail angemeldet und Push-aktiviert. Diese Person wird sowohl die E-Mail als auch den Push erhalten.

Wählen Sie dazu unter **Audience Summary** aus, diese Campaign nur an „nur angemeldete Nutzer:innen“ zu senden. Diese Option stellt sicher, dass nur angemeldete Nutzer:innen Ihre E-Mail erhalten, und Braze sendet Ihren Push standardmäßig nur an Nutzer:innen, die Push-aktiviert sind.

{% alert important %}
Fügen Sie bei dieser Konfiguration keine Filter im Schritt **Target Audiences** hinzu, die die Zielgruppe auf einen einzelnen Kanal beschränken (z. B. `Foreground Push Enabled = True` oder `Email Subscription = Opted-In`).
{% endalert %}

#### Konversions-Events wählen {#choose-conversion-events}

Braze ermöglicht es Ihnen zu verfolgen, wie oft Nutzer:innen bestimmte Aktionen, [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), nach Erhalt einer Campaign ausführen. Sie können jede der folgenden Aktionen als Konversions-Event festlegen:

- App öffnen
- Kauf tätigen (Dies kann ein allgemeiner Kauf oder ein bestimmter Artikel sein)
- Bestimmtes angepasstes Event ausführen
- E-Mail öffnen

Sie können ein Zeitfenster von bis zu 30 Tagen festlegen, in dem Braze eine Conversion zählt, wenn die Person die angegebene Aktion ausführt. Obwohl Braze Öffnungen und Klicks automatisch verfolgt, können Sie das Konversions-Event auf eine Öffnung oder einen Klick setzen, um die [Intelligente Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/) zu nutzen.
{% endtab %}

{% tab Canvas %}
Falls noch nicht geschehen, vervollständigen Sie die verbleibenden Abschnitte Ihrer Canvas-Komponenten. Weitere Details zum Aufbau des restlichen Canvas, zur Implementierung von multivariaten Tests und Intelligenter Auswahl und mehr finden Sie im Schritt [Ihren Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas) unserer Canvas-Dokumentation.
{% endtab %}
{% endtabs %}

## Schritt 5: Überprüfen und bereitstellen {#step-5-review-and-deploy}

Der letzte Abschnitt fasst die von Ihnen entworfene Campaign zusammen. Bestätigen Sie alle relevanten Details und wählen Sie **Launch Campaign**.

Um zu erfahren, wie Sie auf die Ergebnisse Ihrer E-Mail-Kampagnen zugreifen können, lesen Sie [E-Mail-Reporting]({{site.baseurl}}/user_guide/channels/email/reporting/).