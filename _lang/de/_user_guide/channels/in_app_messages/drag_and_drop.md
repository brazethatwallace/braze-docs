---
nav_title: Drag-and-Drop-Editor
article_title: Eine In-App-Nachricht im Drag-and-Drop-Editor erstellen
alias: /iam_drag_and_drop/
page_order: 1
description: "Dieser Referenzartikel behandelt das Erstellen einer In-App-Nachricht mit dem Drag-and-Drop-Editor, Voraussetzungen, kreative Details und mehr."
local_redirect: #set-message-level-styles, #add-a-custom-font, #drag-and-drop-in-app-message-components, #creative-details
  set-message-level-styles: '/docs/user_guide/channels/in_app_messages/customize/style_settings#message-level-styles'
  add-a-custom-font: '/docs/user_guide/channels/in_app_messages/customize/style_settings#custom-fonts'
  drag-and-drop-in-app-message-components: '/docs/user_guide/channels/in_app_messages/customize/style_settings#message-components'
  creative-details: '/docs/user_guide/channels/in_app_messages/customize/style_settings#creative-details'
---

# Eine In-App-Nachricht mit Drag-and-Drop erstellen {#create-an-in-app-message-with-drag-and-drop}

> Mit dem Drag-and-Drop-Editor können Sie vollständig angepasste und personalisierte In-App-Nachrichten in Campaigns oder Canvases erstellen – ganz mit der Drag-and-Drop-Bearbeitungserfahrung. Weitere Informationen zu den verfügbaren Bausteinen im Editor finden Sie unter [Editor-Blöcke]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=in-app%20messages).


{% multi_lang_include video.html id="j94omgo73o" align="right" source="wistia" %}

Wenn Sie Ihre vorhandenen benutzerdefinierten HTML-Templates oder von Drittanbietern erstellte Templates verwenden möchten, müssen diese im Drag-and-Drop-Editor neu erstellt werden.

Sie sind sich nicht sicher, ob Ihre In-App-Nachricht über eine Campaign oder einen [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas) gesendet werden soll? Campaigns eignen sich besser für einzelne, gezielte Messaging-Kampagnen, während Canvases besser für mehrstufige User-Journeys geeignet sind. Nachdem Sie ausgewählt haben, wo Sie Ihre Nachricht erstellen möchten, gehen wir die Schritte zum Erstellen einer Drag-and-Drop-In-App-Nachricht durch.

## Voraussetzungen {#prerequisites}

### SDK-Anforderungen {#sdk-requirements}

| Mindest-SDK-Version                                                          | Empfohlene SDK-Version                                                       |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}{:/} | {::nomarkdown}{% sdk_min_versions swift:6.5.0 android:26.0.0 web:4.8.1 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SDK-Anforderungen" }

{% details Weitere Informationen zu Mindest-SDKs %}

Nachrichten, die mit dem Drag-and-Drop-Editor erstellt wurden, können nur an Nutzer:innen gesendet werden, die die Mindest-SDK-Versionen verwenden (siehe Tabelle im vorherigen Abschnitt). Wenn Nutzer:innen ihre Anwendung nicht aktualisiert haben (d. h. sie verwenden eine ältere SDK-Version), erhalten sie die In-App-Nachricht nicht.

Um alle im Drag-and-Drop-Editor verfügbaren Features nutzen zu können, aktualisieren Sie Ihre SDKs auf die empfohlenen SDK-Versionen. Dadurch können Sie die folgenden zusätzlichen Features nutzen:

- Textlinks, die die Nachricht nicht schließen
- Button-Aktion zur Anforderung eines Push-Primers

Im Folgenden sind die einzelnen Mindest-SDK-Anforderungen für diese Features aufgeführt:

| Textlinks*                                                          | Push-Primer anfordern                                                         |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:6.2.0 android:26.0.0 %}{:/} | {::nomarkdown}{% sdk_min_versions web:4.8.1 swift:6.5.0 android:26.0.0 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SDK-Anforderungen" }

*Wenn Sie einen Link in Ihre In-App-Nachricht einfügen, der zu einer URL weiterleitet, und die Endnutzer:innen nicht die angegebenen Mindest-SDK-Versionen verwenden, wird durch Auswählen des Links die Nachricht geschlossen und die Nutzer:innen können nicht zur Nachricht zurückkehren, um das Formular abzusenden.

{% enddetails %}

### Weitere Voraussetzungen {#additional-prerequisites}

- Für das Web-SDK muss die Initialisierungsoption [`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) auf `true` gesetzt sein. Die Option `enableHtmlInAppMessages` ermöglicht ebenfalls die Funktion dieser Nachrichten, ist jedoch veraltet und sollte auf `allowUserSuppliedJavascript` aktualisiert werden.
- Wenn Sie Google Tag Manager verwenden, müssen Sie in der GTM-Konfiguration „Allow HTML In-App Messages“ aktivieren.

## Schritt 1: Eine In-App-Nachricht erstellen {#step-1-create-an-in-app-message}

Erstellen Sie eine neue In-App-Nachricht oder einen Canvas-Schritt und wählen Sie dann **Drag-and-Drop-Editor** als Bearbeitungsoberfläche aus.

## Schritt 2: Template auswählen {#step-2-select-your-template}

Nachdem Sie den Drag-and-Drop-Editor als Bearbeitungsmethode ausgewählt haben, können Sie:

- Mit einem leeren Modal-Template beginnen
- Ein Braze Drag-and-Drop-In-App-Nachrichten-Template verwenden
- Ein gespeichertes Drag-and-Drop-In-App-Nachrichten-Template auswählen

Wählen Sie **Nachricht erstellen**, um mit der Gestaltung Ihrer In-App-Nachricht im Drag-and-Drop-Editor zu beginnen.

![Der Bereich „Braze Templates“, in dem Sie ein Basis-, Hintergrundbild-, Telefonnummernerfassungs- oder leeres Template auswählen können.]({% image_buster /assets/img_archive/dnd_iam_select_template.png %})

Sie können auch über den Bereich **Templates** im Dashboard auf alle Templates zugreifen.

## 3. Schritt: Zusätzliche Seiten hinzufügen (optional) {#multi-page}

Durch das Hinzufügen von Seiten zu Ihrer In-App-Nachricht können Sie Nutzer:innen durch einen sequenziellen Ablauf führen, z. B. einen Onboarding-Ablauf oder eine Willkommens-Journey. Sie können Seiten im Abschnitt **Pages** des Tabs **Build** verwalten.

![Eine In-App-Nachricht für ein Gesundheitsunternehmen, die aus drei Seiten besteht.]({% image_buster /assets/img_archive/dnd_iam_mockup.png %})

{% tabs %}
{% tab Seiten hinzufügen %}

In-App-Nachrichten beginnen standardmäßig mit einer Seite. So fügen Sie eine neue Seite hinzu:

1. Wählen Sie **+ Add page**.
2. Wählen Sie aus der Liste der benutzerdefinierten oder von Braze bereitgestellten Templates.
3. Geben Sie der Seite einen aussagekräftigen Namen. Dies hilft Ihnen beim Verbinden der Seiten.

{% alert tip %}
Sie können bis zu 10 Seiten pro In-App-Nachricht hinzufügen.
{% endalert %}

So duplizieren Sie eine vorhandene Seite:

1. Bewegen Sie den Mauszeiger über die Seite in der Liste und wählen Sie <i class="fas fa-ellipsis-vertical" aria-label="Weitere Optionen"></i> **More options**.
2. Wählen Sie **Duplicate**.
3. Geben Sie der Seite einen aussagekräftigen Namen. Dies hilft Ihnen beim Verbinden der Seiten.

{% endtab %}
{% tab Seiten löschen oder umbenennen %}

So löschen oder benennen Sie eine Seite um:

1. Bewegen Sie den Mauszeiger über die Seite in der Liste und wählen Sie <i class="fas fa-ellipsis-vertical" aria-label="Weitere Optionen"></i> **More options**.
2. Wählen Sie **Rename** oder **Delete**.

{% endtab %}
{% endtabs %}

### Schritt 3a: Seiten miteinander verbinden {#step-3a-connect-pages-together}

Mehrseitige In-App-Nachrichten sind sequenziell, d. h. Nutzer:innen interagieren mit der Nachricht, indem sie tippen oder klicken, um zur nächsten Seite im Ablauf zu gelangen.

So verbinden Sie Seiten miteinander:

1. Wählen Sie Ihre Startseite aus.
2. Wählen Sie ein Button- oder Bildelement im Canvas aus.
3. Setzen Sie **On-click behavior** auf **Go to page**.
4. Wählen Sie die Seite aus, zu der Sie von der Startseite aus verlinken möchten.
5. Fahren Sie fort, bis alle Seiten verknüpft sind.

![Nutzer:innen bearbeiten den primären Aktions-Button, um zu Seite 2 der In-App-Nachricht zu gelangen.]({% image_buster/assets/img_archive/dnd_iam_multipage.gif %})

Wenn eine Seite nicht mit einer anderen Seite verknüpft ist, kann die Nachricht nicht gestartet werden.

{% alert note %}
Nutzer:innen können jederzeit den Schließen-X-Button auswählen, um die Nachricht zu verlassen. Dieser Button kann nicht entfernt werden.
{% endalert %}

## Schritt 4: Erstellen und gestalten Sie Ihre In-App-Nachricht {#step-4-build-and-design-your-in-app-message}

Hier darf Ihre Nachricht über den Laufsteg schreiten – ganz im unverwechselbaren Stil Ihrer Marke. Mit einer Kombination aus Editor-Blöcken und Stileinstellungen können Sie Ihre In-App-Nachricht individuell anpassen und gestalten.

- Eine Liste der verfügbaren Editor-Blöcke und ihrer Eigenschaften finden Sie unter [Editor-Blöcke]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=in-app%20messages).
- Hilfe beim Anpassen des Erscheinungsbilds Ihrer Nachricht finden Sie unter [Stileinstellungen]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings).
- Best Practices für die Erstellung von Nachrichten mit Rechts-nach-links-Schrift finden Sie unter [Rechts-nach-links-Nachrichten erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

## Schritt 5: Testen Sie Ihre In-App-Nachricht {#step-5-test-your-in-app-message}

Im Abschnitt **Vorschau und Test** können Sie Ihre In-App-Nachrichten auf verschiedenen Geräten in der Vorschau anzeigen und eine Testnachricht an Ihr Gerät senden. Hier können Sie sicherstellen, dass die Details auf allen Ihren Plattformen für Ihre Drag-and-Drop-In-App-Nachricht-Campaign aufeinander abgestimmt sind.

Es ist wichtig, Ihre In-App-Nachrichten immer zu testen, bevor Sie Ihre Campaigns senden, damit Sie sich ein Bild davon machen können, wie Ihre endgültige Nachricht aus der Perspektive Ihrer Nutzer:innen aussehen wird.

### Nachricht als Nutzer:in in der Vorschau anzeigen {#preview-message-as-a-user}

{% alert warning %}
Um einen Test an Content-Test-Gruppen oder einzelne Nutzer:innen zu senden, muss Push auf Ihren Testgeräten aktiviert sein, bevor Sie den Test senden.
{% endalert %}

Sie können Nachrichten im Tab **Vorschau und Test** in der Vorschau anzeigen, als wären Sie eine Nutzer:in. Sie können eine:n bestimmte:n Nutzer:in, eine:n zufällige:n Nutzer:in auswählen oder eine:n angepasste:n Nutzer:in erstellen:

- **Zufällige:r Nutzer:in:** Braze wählt zufällig eine:n Nutzer:in aus der Datenbank aus und zeigt die In-App-Nachricht basierend auf deren Attributen oder Ereignisinformationen in der Vorschau an.
- **Nutzer:in auswählen:** Sie können eine:n bestimmte:n Nutzer:in anhand der E-Mail-Adresse oder `external_id` auswählen. Die In-App-Nachricht wird basierend auf den Attributen und Ereignisinformationen dieser Nutzer:in in der Vorschau angezeigt.
- **Angepasste:r Nutzer:in:** Sie können eine:n Nutzer:in anpassen. Braze bietet Eingabefelder für alle verfügbaren Attribute und Ereignisse. Geben Sie alle Informationen ein, die Sie in der Vorschau-E-Mail sehen möchten.

### Test-Checkliste {#test-checklist}

Berücksichtigen Sie die folgenden Fragen, wenn Sie Ihre In-App-Nachricht testen:

- Haben Sie die Nachricht auf verschiedenen Geräten getestet?
- Werden die Bilder und Medien wie erwartet angezeigt und funktionieren sie korrekt?
- Funktioniert Liquid wie erwartet? Haben Sie einen Standardattributwert für den Fall berücksichtigt, dass Liquid keine Informationen zurückgibt?
- Ist Ihr Text klar, prägnant und korrekt?
- Leiten Ihre Buttons die Nutzer:innen dorthin, wo sie hingelangen sollen?

## Häufig gestellte Fragen {#frequently-asked-questions}

### Warum werden Body-Klicks nicht auf meiner Analytics-Seite angezeigt? {#why-are-body-clicks-not-appearing-on-my-analytics-page}

Body-Klicks werden für In-App-Nachrichten, die mit dem Drag-and-Drop-Editor erstellt wurden, nicht automatisch erfasst. Weitere Informationen finden Sie in den SDK-Changelogs für [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) und [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

### Kann ich basierend auf Button-Klicks segmentieren? {#can-i-segment-based-on-button-clicks}

Ja, Sie können basierend auf Button-Klicks für bis zu zwei Buttons in Ihrer Nachricht segmentieren. Setzen Sie dazu den **Identifier for Reporting** für Ihre Buttons auf „0“ und „1“, was den Segmentierungsfiltern „Clicked in-app message button 1“ bzw. „Clicked in-app message button 2“ entspricht.

![Das Feld „Identifier for Reporting“ mit dem Wert „0“.]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}

### Kann ich meine In-App-Nachricht mit benutzerdefiniertem HTML oder JavaScript anpassen oder bestehende HTML-Nachrichten in den Editor übertragen? {#can-i-customize-my-in-app-message-using-custom-html-or-javascript-or-transfer-existing-html-messages-into-the-editor}

Sie können bestehende HTML-Nachrichten nicht direkt in den Editor übertragen, aber Sie können rohes HTML, CSS und JavaScript in einen **Custom code**-Block einfügen. Sie können **Custom code**-Blöcke verwenden, um Videos von Drittanbietern und erweitertes Liquid einzubetten, z. B. Connected-Content oder bedingte Anweisungen. Für `brazeBridge`-JavaScript-Methoden und Beispiele zum Klick-Tracking siehe [Benutzerdefinierte HTML-In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html).

### Wie kann ich eine Slideup-In-App-Nachricht erstellen? {#how-can-i-create-a-slideup-in-app-message}

Derzeit ist der Editor auf Modal- und Vollbildnachrichten beschränkt. Sie können im Abschnitt **Message container** des Panels **Message styles** zwischen den Anzeigetypen wechseln.

### Kann ich meine In-App-Nachricht als Template speichern, nachdem ich sie in meiner Campaign oder meinem Canvas erstellt habe? {#can-i-save-my-in-app-message-as-a-template-after-i-build-it-within-my-campaign-or-canvas}

Ja. Für jede In-App-Nachricht, die Sie in einer zukünftigen Campaign oder einem Canvas-Schritt wiederverwenden möchten, können Sie sie als benutzerdefiniertes Template speichern, indem Sie den Button **Save as template** verwenden, der nach dem Verlassen des Editors verfügbar ist. Bevor Sie sie als Template speichern können, müssen Sie die Campaign zuerst starten ODER als Entwurf speichern.

![Eine Vorschau einer In-App-Nachricht für eine Produkttour.]({% image_buster /assets/img_archive/dnd_iam_save_as_template.png %})

Sie können auch In-App-Nachrichten-Templates erstellen und speichern, indem Sie zu **Content** > **In-App Message** navigieren.

### Warum wird meine Liquid-Syntax als Klartext in meiner paginierten In-App-Nachricht angezeigt? {#why-is-my-liquid-syntax-appearing-as-plain-text-in-my-paginated-in-app-message}

Wenn Sie beim Testen einer paginierten In-App-Nachricht Liquid-Syntax als Klartext sehen (anstelle des personalisierten Inhalts), liegt möglicherweise ein Liquid-Syntaxfehler auf einer der Seiten vor. Wenn auf einer Seite ein Syntaxfehler vorliegt, wirkt sich dies auf das Rendering von Liquid auf allen Seiten der Nachricht aus – die Seiten sind nicht unabhängig voneinander.

Zur Fehlerbehebung:

1. Überprüfen Sie jede Seite Ihrer Nachricht auf Liquid-Syntaxfehler. Eine fehlerhafte Vorschau auf einer Seite bedeutet nicht, dass der Fehler auf dieser Seite liegt – da die Seiten nicht unabhängig sind, kann der Syntaxfehler an jeder Stelle in der Nachricht auftreten.
2. Stellen Sie sicher, dass alle Liquid-Tags ordnungsgemäß geschlossen und korrekt formatiert sind.