---
nav_title: Traditioneller Editor
article_title: Eine In-App-Nachricht im traditionellen Editor erstellen
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie eine In-App-Nachricht mit der Braze-Plattform über Campaigns oder Canvas erstellen."
channel:
  - in-app messages
tool:
  - Campaigns
search_rank: 4.8
toc_headers: h2
---

# Eine In-App-Nachricht mit dem traditionellen Editor erstellen {#create-an-in-app-message-with-the-traditional-editor}

> Sie können eine In-App-Nachricht oder In-Browser-Nachricht mit der Braze-Plattform über Campaigns, Canvas oder als API-Kampagne erstellen. Wir empfehlen dringend, Ihre Nachrichten im Voraus zu planen und alle Materialien mithilfe unseres praktischen [Leitfadens zur Vorbereitung von In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices) vorzubereiten.

## Schritt 1: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten {#create-new-campaign-in-app}

Sind Sie unsicher, ob Ihre Nachricht über eine Campaign oder ein Canvas gesendet werden sollte? Campaigns eignen sich besser für einzelne, gezielte Messaging-Kampagnen, während Canvases besser für mehrstufige User-Journeys geeignet sind.

{% tabs %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Kampagne erstellen**.
2. Wählen Sie **In-App-Nachricht**. Beachten Sie, dass In-App-Nachrichten nicht in Multichannel-Campaigns verfügbar sind.
3. Geben Sie Ihrer Campaign einen klaren und aussagekräftigen Namen.
4. Fügen Sie bei Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu.
   * Tags erleichtern das Auffinden Ihrer Campaigns und das Erstellen von Berichten. Wenn Sie beispielsweise den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder) verwenden, können Sie nach bestimmten Tags filtern.
5. Fügen Sie so viele Varianten hinzu und benennen Sie sie, wie Sie für Ihre Campaign benötigen. Sie können für jede hinzugefügte Variante verschiedene Plattformen, Nachrichtentypen und Layouts wählen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Wenn alle Nachrichten in Ihrer Campaign ähnlich sein oder denselben Inhalt haben werden, verfassen Sie Ihre Nachricht, bevor Sie zusätzliche Varianten hinzufügen. Anschließend können Sie **Aus Variante kopieren** aus dem Dropdown-Menü **Variante hinzufügen** wählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) mit dem Canvas-Composer.
2. Nachdem Sie Ihr Canvas eingerichtet haben, fügen Sie im Canvas-Builder einen Schritt hinzu. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie einen [Schritt-Zeitplan]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types#schedule-delay) und legen Sie bei Bedarf eine Verzögerung fest. Beachten Sie, dass Schritte mit In-App-Nachrichten nicht aktionsbasiert sein können.
4. Filtern Sie bei Bedarf Ihre Zielgruppe für diesen Schritt. Sie können die Empfänger:innen dieses Schritts weiter eingrenzen, indem Sie Segmente angeben und zusätzliche Filter hinzufügen. Die Zielgruppenoptionen werden nach der Verzögerung zum Zeitpunkt des Nachrichtenversands überprüft.
5. Wählen Sie Ihr [Fortschrittsverhalten]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases).
6. Wählen Sie alle weiteren Messaging-Kanäle, die Sie mit Ihrer Nachricht kombinieren möchten.

{% alert important %}
Sie können nicht mehrere In-App-Nachrichtenvarianten in einem einzelnen Schritt haben.
{% endalert %}

Weitere Canvas-spezifische Informationen finden Sie unter [In-App-Nachrichten in Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas).

{% endtab %}
{% endtabs %}

## Schritt 2: Zustellungsplattformen festlegen {#step-2-specify-delivery-platforms}

Wählen Sie zunächst aus, welche Plattformen die Nachricht erhalten sollen. Verwenden Sie diese Auswahl, um die Zustellung einer Campaign auf eine bestimmte Gruppe von Apps zu beschränken. Sie könnten beispielsweise **Webbrowser** für eine In-Browser-Nachricht wählen, die Nutzer:innen dazu ermutigt, Ihre mobile App herunterzuladen, um sicherzustellen, dass sie die Nachricht nicht erhalten, nachdem sie Ihre App bereits installiert haben. Da die Plattformauswahl für jede Variante spezifisch ist, können Sie das Nachrichten-Engagement pro Plattform testen.

| Plattform | Nachrichtenzustellung |
|---------------------------------|------------------------------|
| Mobile Apps | iOS-, Android- und Vega-SDKs |
| Webbrowser | Web-SDK |
| Sowohl Mobile Apps als auch Webbrowser | iOS-, Android-, Vega- und Web-SDKs |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zustellungsplattformen festlegen" }

## Schritt 3: Nachrichtentypen festlegen {#step-3-specify-your-message-types}

Nachdem Sie eine Versandplattform ausgewählt haben, durchsuchen Sie die damit verbundenen Nachrichtentypen, Layouts und weiteren Optionen. Erfahren Sie mehr über das erwartete Verhalten und Aussehen jeder dieser Nachrichten auf unserer Seite [Nachrichtentypen]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types) oder klicken Sie auf die verlinkten Nachrichtentypen in den folgenden Tabellen.

Berücksichtigen Sie bei der Entscheidung, welchen Nachrichtentyp Sie verwenden möchten, wie viel Platz Ihre Nachricht einnimmt und wie störend sie für die Nutzererfahrung sein könnte.

- **Slideup**-Nachrichten sind am wenigsten aufdringlich und erscheinen dezent, ohne Inhalte zu verdecken.
- **Modale** Nachrichten liegen in der Mitte – auffällig genug, um Aufmerksamkeit zu erregen, ohne den Bildschirm vollständig zu übernehmen.
- **Vollbild**-Nachrichten erregen die meiste Aufmerksamkeit und eignen sich am besten für wichtige Ankündigungen oder Aktionen.

Je komplexer Ihr Inhalt ist, desto mehr Platz benötigen Sie – und desto wahrscheinlicher wird Ihre Nachricht den Ablauf der Nutzer:innen unterbrechen.

### Nachrichtentypen {#message-types}

Diese In-App-Nachrichten werden sowohl von mobilen Apps als auch von Webanwendungen unterstützt.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table aria-label="Nachrichtentypen" class="tg">
  <caption>Nachrichtentypen</caption>
<thead>
  <tr>
    <th>Nachrichtentyp</th>
    <th>Typbeschreibung</th>
    <th>Verfügbare Layouts</th>
    <th>Weitere Optionen</th>
    <th>Empfohlene Verwendung</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/fullscreen'>Vollbild</a></td>
    <td>Nachrichten, die den gesamten Bildschirm mit einem Nachrichtenblock abdecken.</td>
    <td>
      <ul>
      <li>Bild und Text</li>
      <li>Nur Bild</li>
      </ul>
    </td>
    <td>Erzwungene Geräteausrichtung (Hochformat oder Querformat)</td>
    <td>Groß und auffällig! Verwenden Sie diesen Typ, wenn Sie sicherstellen möchten, dass Nutzer:innen Ihren Inhalt sehen, z. B. bei Ihren wichtigsten Campaigns, wichtigen Benachrichtigungen oder großen Aktionen.<br><br>Beachten Sie, dass auf Mobilgeräten Hoch- und Querformatnachrichten nicht angezeigt werden, wenn die Ausrichtung des Geräts nicht mit der Ausrichtung der Nachricht übereinstimmt.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/modal'>Modal</a></td>
    <td>Nachrichten, die den gesamten Bildschirm mit einem Bildschirm-Overlay und einem Nachrichtenblock abdecken.</td>
    <td>
      <ul>
      <li>Text (mit optionalem Bild)</li>
      <li>Nur Bild</li>
      </ul>
    </td>
    <td>N/A</td>
    <td>Ein guter Mittelweg. Verwenden Sie diesen Typ, wenn Sie die Aufmerksamkeit Ihrer Nutzer:innen auf offensichtliche Weise erregen möchten, z. B. um sie zu ermutigen, ein neues Feature auszuprobieren oder eine Aktion zu nutzen.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/slideup'>Slideup</a></td>
    <td>Nachrichten, die an einer bestimmten Stelle ins Sichtfeld gleiten, ohne den Rest des Bildschirms zu blockieren.</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Unauffällig – nimmt am wenigsten Bildschirmfläche ein. Verwenden Sie diesen Typ, um Nutzer:innen über kleine Informationshäppchen zu informieren, z. B. neue Features, Ankündigungen, Verwendung von Cookies usw.<br></td>
  </tr>
</tbody>
</table>

### Erweiterte Nachrichtentypen {#advanced-message-types}

Diese In-App-Nachrichten sind an Ihre Bedürfnisse anpassbar.

<table aria-label="Erweiterte Nachrichtentypen" class="tg">
  <caption>Erweiterte Nachrichtentypen</caption>
<thead>
  <tr>
    <th>Nachrichtentyp</th>
    <th>Typbeschreibung</th>
    <th>Verfügbare Layouts</th>
    <th>Anforderungen</th>
    <th>Empfohlene Verwendung</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/customize#custom-html-messages'>Benutzerdefinierte HTML-Nachricht</a></td>
    <td>Benutzerdefinierte Nachrichten, die wie in Ihrem benutzerdefinierten Code (HTML, CSS und/oder JavaScript) definiert funktionieren.</td>
    <td>N/A</td>
    <td>Die Initialisierungsoption <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> muss auf <code>true</code> gesetzt werden, damit Ihre In-App-Nachricht funktioniert.</td>
    <td>Dies ist eine gute Option, wenn Sie alle Vorteile von In-App-Nachrichten nutzen möchten, aber zusätzliche Funktionalität benötigen oder das Erscheinungsbild „markenkonform“ bleiben soll. Sie können jedes Detail der Nachricht anpassen – Schriftart, Farbe, Form, Größe, Buttons usw. <br><br>Beispielhafte Anwendungsfälle umfassen das Einholen von App-Feedback, E-Mail-Erfassungsformulare oder paginierte Nachrichten.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/customize#email-capture-form'>E-Mail-Erfassungsformular</a></td>
    <td>Wird typischerweise verwendet, um die E-Mail-Adresse der Betrachter:innen zu erfassen.</td>
    <td>N/A</td>
    <td>Die Initialisierungsoption <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> muss auf <code>true</code> gesetzt werden, damit Ihre In-App-Nachricht funktioniert.</td>
    <td>Wenn Sie Nutzer:innen auffordern, ihre E-Mail-Adresse einzugeben.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/customize#web-modal-css'>Web-Modal mit CSS</a></td>
    <td>Modale Nachrichten für das Web mit anpassbarem CSS.</td>
    <td>
      <ul>
      <li>Text (mit optionalem Bild)</li>
      <li>Nur Bild</li>
      </ul>
    </td>
    <td>Web-Modal mit CSS ist exklusiv für das Web-SDK und kann nur nach Auswahl von <b>Webbrowser</b> verwendet werden.</td>
    <td>Wenn Sie benutzerdefiniertes CSS hochladen oder schreiben möchten, um ansprechende, rundum individuell gestaltete Nachrichten zu erstellen.</td>
  </tr>
</tbody>
</table>

{% alert important %}
Wenn Braze erkennt, dass Ihr Code keinen Schließen- oder Verwerfen-Button enthält, werden wir Sie bitten, einen hinzuzufügen. Zu Ihrer Bequemlichkeit haben wir ein Snippet bereitgestellt, das Sie kopieren und in Ihren Code einfügen können: <br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## Schritt 4: Ihre In-App-Nachricht verfassen {#step-4-compose-your-in-app-message}

Der Tab **Verfassen** ermöglicht es Ihnen, alle Aspekte des Inhalts und Verhaltens Ihrer Nachricht zu bearbeiten.

![Ein Beispiel einer In-App-Nachricht einer Marke, die neue Kund:innen begrüßt und sie auffordert, ein Nutzerprofil einzurichten.]({% image_buster /assets/img_archive/iam_compose.png %}){: style="max-width:85%" }

Der Inhalt des Tabs **Verfassen** variiert je nach den im vorherigen Schritt gewählten Nachrichtenoptionen, kann aber eine der folgenden Optionen umfassen:

### Sprache {#language}

Wählen Sie **Sprachen hinzufügen** und wählen Sie die gewünschten Sprachen aus der bereitgestellten Liste. Dadurch wird [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) in Ihre Nachricht eingefügt. Wir empfehlen, Ihre Sprachen auszuwählen, bevor Sie Ihren Inhalt verfassen, damit Sie Ihren Text an der richtigen Stelle im Liquid einfügen können. Sehen Sie unsere [vollständige Liste der verfügbaren Sprachen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported).

### Bild {#image}

Je nach Nachrichtentyp können Sie ein **Bild hochladen**, ein **Badge auswählen** oder **Font Awesome** verwenden. Um ein Bild hochzuladen, wählen Sie **Bild hinzufügen** oder geben Sie eine Bild-URL an. Wenn Sie **Bild hinzufügen** wählen, öffnet sich die **Medienbibliothek**, in der Sie ein zuvor hochgeladenes Bild auswählen oder ein neues hinzufügen können. Jeder Nachrichtentyp und jede Plattform kann eigene empfohlene Proportionen und Anforderungen haben – prüfen Sie diese unbedingt, bevor Sie ein Bild in Auftrag geben oder von Grund auf erstellen.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### Überschrift und Textkörper {#header-and-body}

Schreiben Sie, was Sie möchten! Fügen Sie vollständig benutzerdefinierten Text (oft mit benutzerdefinierten HTML-Funktionen) mit den Optionen zur Einbindung von [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) und anderen Arten der Personalisierung ein. Je schneller Sie Ihre Nachricht vermitteln und Ihre Kund:innen zum Klicken bringen können, desto besser! Wir empfehlen klare und prägnante Überschriften und Nachrichteninhalte.

Einige Nachrichtentypen benötigen keine Überschriften und fragen daher auch nicht danach.

#### Tipps {#tips}

##### KI-generierten Text erstellen {#generating-ai-copy}

Brauchen Sie Hilfe beim Erstellen großartiger Texte? Probieren Sie den [KI-Textassistenten]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy) aus. Geben Sie einen Produktnamen oder eine Beschreibung ein, und die KI generiert menschenähnlichen Marketingtext zur Verwendung in Ihren Nachrichten.

![Button „KI-Textassistent starten“ im Nachrichtenfeld des In-App-Nachrichten-Composers.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### Rechts-nach-links-Nachrichten erstellen {#creating-right-to-left-messages}

Brauchen Sie Hilfe beim Erstellen von Rechts-nach-links-Nachrichten für Sprachen wie Arabisch und Hebräisch? Lesen Sie [Rechts-nach-links-Nachrichten erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages) für Best Practices.

### Button-Text {#buttons}

Wenn für Ihren Nachrichtentyp verfügbar, können bis zu zwei Buttons unter Ihrem Textkörper erscheinen. Sie können benutzerdefinierten Button-Text und -Farbe erstellen und bearbeiten. Sie können auch einen Link zu den Nutzungsbedingungen in E-Mail-Erfassungsformularen hinzufügen.

Wenn Sie sich entscheiden, nur einen Button zu verwenden, passt sich dieser automatisch an, um den verfügbaren Platz am unteren Rand Ihrer Nachricht einzunehmen, anstatt Platz für einen zusätzlichen Button freizulassen.

#### Einen primären Button wählen {#choosing-a-primary-button}

Wenn Sie diese Buttons mit Ihren eigenen Farben formatieren, empfehlen wir, Button 2 für Ihr bevorzugtes Ergebnis zu verwenden.

Mit anderen Worten: Wenn Sie möchten, dass Ihre Nutzer:innen einen Button häufiger anklicken als den anderen, stellen Sie sicher, dass er sich auf der rechten Seite befindet. Der rechte Button hat oft ein besseres Klickpotenzial gezeigt, insbesondere wenn er eine etwas kontrastierende oder anderweitig auffällige Farbe im Vergleich zum Rest der Nachricht hat. Dies wird nur verstärkt, wenn der Button auf der linken Seite visuell stärker mit der Nachricht verschmilzt.

![Primärer und sekundärer Button in einer In-App-Nachricht]({% image_buster /assets/img/primary-secondary-buttons.png %})

### Klickverhalten {#button-actions}

Wenn Ihre Kund:innen auf einen Button in Ihrer In-App-Nachricht klicken, stehen die folgenden Aktionen zur Verfügung.

| Aktion | Beschreibung |
|---|---|
| Weiterleitung zu Web-URL | Öffnet eine nicht-native Webseite. |
| [Deeplink in die App]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | Deeplink zu einem bestehenden Bildschirm in Ihrer App. |
| Nachricht schließen | Schließt die aktuell aktive Nachricht. |
| Angepasstes Event protokollieren | Wählen Sie ein [angepasstes Event]({{site.baseurl}}/user_guide/data/activation/events/custom_events) zum Auslösen. Kann verwendet werden, um eine weitere In-App-Nachricht anzuzeigen oder zusätzliches Messaging auszulösen. |
| Angepasstes Attribut protokollieren | Wählen Sie ein [angepasstes Attribut]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), das für die aktuelle Nutzerin oder den aktuellen Nutzer gesetzt werden soll. |
| Push-Berechtigung anfordern | Zeigt die native Push-Berechtigungsabfrage an. Lesen Sie mehr über [Push-Priming]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) sowie [Best Practices]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#best-practices) zur Vorbereitung von Nutzer:innen auf Push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Klickverhalten" }

Hinweis: Die Optionen __Push-Berechtigung anfordern__, __Angepasstes Event protokollieren__ und __Angepasstes Attribut protokollieren__ erfordern die folgenden SDK-Mindestversionen:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

### iOS-Geräteoptionen {#ios-device-options}

Falls gewünscht, können Sie Ihre In-App-Nachricht so einschränken, dass sie nur an iOS-Geräte gesendet wird. Klicken Sie dazu auf **Ändern** und wählen Sie **Nur an iOS-Geräte senden**.

### Nachricht schließen {#message-close}

Wählen Sie zwischen den folgenden Optionen:

- **Automatisch verwerfen:** Wählen Sie, wie viele Sekunden die Nachricht auf dem Bildschirm verbleiben soll.
- **Auf Wischen oder Tippen warten:** Erfordert eine Verwerfungs- oder Schließen-Option.

### Slideup-Position {#slide-up-position}

Diese Einstellung gilt nur für den Slideup-Nachrichtentyp. Wählen Sie, ob Ihr Slideup **Vom unteren Bildschirmrand** oder **Vom oberen Bildschirmrand** erscheinen soll.

### HTML und Assets {#html-and-assets}

Diese Einstellung gilt nur für den Nachrichtentyp „Benutzerdefinierter Code“. Kopieren Sie HTML in den verfügbaren Bereich und laden Sie Ihre Assets über eine ZIP-Datei hoch.

### Platzhalter für E-Mail-Erfassungseingabe {#email-capture-input-placeholder}

Diese Einstellung gilt nur für den Nachrichtentyp „E-Mail-Erfassungsformular“. Geben Sie benutzerdefinierten Text ein, der als Platzhaltertext für das E-Mail-Eingabefeld angezeigt wird. Standardmäßig steht dort „Geben Sie Ihre E-Mail-Adresse ein“.

## Schritt 5: Ihre In-App-Nachricht gestalten {#step-5-style-your-in-app-message}

Der Tab **Stil** ermöglicht es Ihnen, alle visuellen Aspekte Ihrer Nachricht anzupassen. Laden Sie ein Bild oder Badge hoch oder wählen Sie ein vorgefertigtes Badge-Symbol. Ändern Sie die Farben von Überschrift und Textkörper, Buttons und Hintergrund, indem Sie aus einer Palette wählen oder einen Hex-, RGB- oder HSB-Code eingeben.

Der Inhalt des Tabs **Stil** variiert je nach den im vorherigen Schritt gewählten Nachrichtenoptionen, kann aber eine der folgenden Optionen umfassen:

| Formatierung | Eingabe | Beschreibung |
|---|---|---|
| [Farbprofil]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/in_app_message_template#reusable-color-profiles) | Aus der In-App-Nachrichten-Vorlagengalerie anwenden. | Wählen Sie **Vorlage anwenden** und wählen Sie aus der Galerie. Wählen Sie dann **Speichern**. |
| Textausrichtung | Links, Zentriert oder Rechts. | Nur für neuere Braze-SDK-Versionen verfügbar. |
| Überschrift | HEX-Farbcode. | Ihre gewünschte HEX-Farbe wird angezeigt. Sie können auch die Deckkraft der Farbe wählen. |
| Text | HEX-Farbcode. | Ihre gewünschte HEX-Farbe wird angezeigt. Sie können auch die Deckkraft der Farbe wählen. |
| Buttons | HEX-Farbcode. | Ihre gewünschten HEX-Farben werden angezeigt. Sie können auch die Deckkraft der Farben wählen. Sie können Farben wählen für: den Hintergrund des Schließen-Buttons der Nachricht sowie den Hintergrund, Text und Rahmen jedes Buttons. |
| Button-Rahmen | HEX-Farbcode. | Neu! Damit können Sie Ihre primären und sekundären Buttons voneinander abheben. Wir empfehlen, Buttons mit kontrastierenden Farben zu umranden. |
| Hintergrundfarbe | HEX-Farbcode. | Ihre gewünschte HEX-Farbe wird angezeigt. Sie können auch die Deckkraft der Farbe wählen. Dies ist der Hintergrund der gesamten Nachricht und wird deutlich hinter Ihrem Textkörper angezeigt. |
| Bildschirm-Overlay | HEX-Farbcode. | Ihre gewünschte HEX-Farbe wird angezeigt. Sie können auch die Deckkraft der Farbe wählen. Nur für neuere Braze-SDK-Versionen verfügbar. Dies ist der Rahmen um die gesamte Nachricht. |
| Chevron oder andere Nachricht-schließen-Option | HEX-Farbcode. | Ihre gewünschte HEX-Farbe wird angezeigt. Sie können auch die Deckkraft der Farbe wählen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Ihre In-App-Nachricht gestalten" }

[Zeigen Sie immer eine Vorschau an und testen Sie]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) Ihre Nachricht, bevor Sie sie senden.

{% alert important %}
Einige In-App-Nachrichtentypen bieten keine Gestaltungsoptionen über das Hochladen von benutzerdefiniertem HTML (oder CSS oder JavaScript) und Assets über eine ZIP-Datei hinaus. [Web-Modal mit CSS]({{site.baseurl}}/user_guide/channels/in_app_messages/customize#web-modal-css) ermöglicht es Ihnen, benutzerdefiniertes CSS hochzuladen oder zu schreiben, um ansprechende, rundum individuell gestaltete Nachrichten zu erstellen.
{% endalert %}

## Schritt 6: Zusätzliche Einstellungen konfigurieren (optional) {#step-6-configure-additional-settings-optional}

### Schlüssel-Wert-Paare {#key-value-pairs}

Sie können [Schlüssel-Wert-Paare]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) hinzufügen, um zusätzliche benutzerdefinierte Felder an Nutzergeräte zu senden.

## Schritt 7: Den Rest Ihrer Campaign oder Ihres Canvas erstellen {#step-7-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Erstellen Sie den Rest Ihrer Campaign; in den folgenden Abschnitten finden Sie weitere Anleitungen zur optimalen Nutzung unserer Tools zum Erstellen von In-App-Nachrichten.

### Einen Trigger wählen {#choose-a-trigger}

Wählen Sie die Aktion, die Ihre Nachricht auslösen soll, sowie die Start- und Endzeiten für Ihre Campaign oder Ihr Canvas.

{% alert important %}
Beachten Sie: Wenn Sie Ihre In-App-Nachricht basierend auf einem angepassten Event auslösen möchten, muss dieses angepasste Event über das SDK gesendet werden.
{% endalert %}

![Aktionsbasierte Campaign mit der Trigger-Aktion „Sitzung starten“.]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

Die Zustellung von In-App-Nachrichten basiert vollständig auf den folgenden Aktions-Triggern:

- Einen Kauf tätigen
- Die App/Webseite öffnen
- Ein angepasstes Event ausführen (funktioniert nur mit Events, die über das SDK gesendet werden)
- Eine bestimmte Push-Nachricht öffnen
- Campaigns automatisch so planen, dass sie zu einer bestimmten Zeit in Bezug auf die Ortszeit jeder Nutzerin und jedes Nutzers gesendet werden.
- Nachrichten können auch so konfiguriert werden, dass sie täglich, wöchentlich (optional an bestimmten Tagen) oder monatlich wiederholt werden.

Ein Startdatum und eine Startzeit müssen ausgewählt werden; ein Enddatum ist jedoch optional. Ein Enddatum verhindert, dass diese bestimmte In-App-Nachricht nach dem angegebenen Datum/der angegebenen Uhrzeit auf Geräten angezeigt wird.

Weitere Informationen finden Sie in unserer Entwicklerdokumentation zu [serverseitigem Event-Triggering]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web) und [lokaler In-App-Nachrichtenzustellung]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery#local-in-app-messages).

#### Online- versus Offline-Triggering {#online-versus-offline-triggering}

In-App-Nachrichten funktionieren, indem die Nachricht und die Trigger an das Gerät der Nutzerin oder des Nutzers gesendet werden. Sobald die In-App-Nachrichten auf einem Gerät sind, wartet es mit der Anzeige, bis die Trigger-Bedingung erfüllt ist. Wenn die In-App-Nachrichten bereits auf dem Gerät der Nutzerin oder des Nutzers zwischengespeichert sind, können Sie In-App-Nachrichten sogar offline ohne Verbindung zu Braze auslösen (z. B. im Flugmodus).

{% alert important %}
Nachdem eine In-App-Nachricht gestoppt wurde, kann es vorkommen, dass einige Nutzer:innen die Nachricht weiterhin sehen, wenn sie eine Sitzung gestartet haben, bevor die Nachricht gestoppt wurde, und anschließend das Trigger-Event ausführen. Diese Nutzer:innen werden als einzigartige Impression gezählt, auch nachdem die Campaign gestoppt wurde.
{% endalert %}

### Eine Priorität wählen {#choose-a-priority}

Nachdem Sie die Aktion ausgewählt haben, die die In-App-Nachricht auslöst, sollten Sie auch eine Priorität festlegen. Wenn zwei Nachrichten durch dieselbe Aktion ausgelöst werden, werden Nachrichten mit hoher Priorität vor Nachrichten mit niedrigerer Priorität auf den Geräten der Nutzer:innen angezeigt.

Sie können zwischen den folgenden Nachrichtenprioritäten wählen:

- Hohe Priorität (wird vor anderen Nachrichten angezeigt)
- Mittlere Priorität (Standard)
- Niedrige Priorität (wird nach anderen Nachrichten angezeigt)

Die Optionen für hohe, mittlere und niedrige Priorität bei getriggerten Nachrichten sind Buckets, und daher können mehrere Nachrichten dieselbe ausgewählte Priorität haben. Wenn mehrere Nachrichten dieselbe Priorität teilen, hat die zuletzt erstellte oder zugewiesene Nachricht Vorrang und wird zuerst angezeigt:

- **Standard-Prioritäts-Bucket:** Wenn zwei Campaigns denselben Trigger teilen und die Standard-Priorität (mittel) verwenden, erhält die zuletzt erstellte Campaign den Trigger.
- **Spezifischer Prioritäts-Bucket:** Wenn mehrere Campaigns denselben Trigger teilen und einem bestimmten Prioritäts-Bucket zugewiesen sind, erhält die Campaign, die diesem Bucket zuletzt zugewiesen wurde, den Trigger.

Um Prioritäten innerhalb dieser Buckets festzulegen, klicken Sie auf **Genaue Priorität festlegen**, und Sie können Campaigns per Drag-and-Drop in die richtige Reihenfolge bringen.

![Ein Beispiel, wie die Priorität für eine In-App-Nachrichten-Campaign und ein Canvas festgelegt wird.]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

### Zielgruppe zusammenstellen {#choose-users-to-target}

Als Nächstes müssen Sie die [Zielgruppe zusammenstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users), indem Sie Segmente oder Filter auswählen, um Ihre Zielgruppe einzugrenzen. Sie erhalten automatisch einen Überblick darüber, wie die ungefähre Segment-Population aussieht. Beachten Sie, dass die genaue Segment-Zugehörigkeit immer berechnet wird, bevor die Nachricht gesendet wird.

{% alert note %}
Wenn es eine Verzögerung beim In-App-Nachrichten-Schritt gibt, wird die Segment-Zugehörigkeit nach der Verzögerung ausgewertet. Wenn die Nutzerin oder der Nutzer berechtigt ist, wird die In-App-Nachricht bei der nächsten verfügbaren Sitzung synchronisiert.
{% endalert %}

#### Campaign-Berechtigung und Liquid erneut auswerten {#re-evaluate-campaign-eligibility-and-liquid}

In einigen Szenarien möchten Sie möglicherweise die Berechtigung einer Nutzerin oder eines Nutzers erneut auswerten, wenn eine In-App-Nachricht zur Anzeige ausgelöst wird. Beispiele hierfür sind Campaigns, die auf ein angepasstes Attribut abzielen, das sich häufig ändert, oder Nachrichten, die kurzfristige Profiländerungen widerspiegeln sollen.

![Kontrollkästchen „Campaign-Berechtigung vor der Anzeige erneut auswerten“ ist ausgewählt.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}){:style="max-width:60%"}

Wenn Sie **Campaign-Berechtigung vor der Anzeige erneut auswerten** auswählen, wird eine zusätzliche Anfrage an Braze gesendet, um zu bestätigen, dass die Nutzerin oder der Nutzer weiterhin für diese Nachricht berechtigt ist, bevor sie gesendet wird. Zusätzlich werden alle [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)-Variablen oder [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) zu diesem Zeitpunkt vor der Anzeige der Nachricht aufgelöst.

Dies verhindert, dass In-App-Nachrichten an Nutzer:innen innerhalb abgelaufener oder archivierter Campaigns gesendet werden. Wenn Sie die Berechtigung einer Nutzerin oder eines Nutzers nicht erneut auswerten, erhält sie oder er die In-App-Nachricht auch nach Ablauf oder Archivierung der Campaign, da die Nachricht in Ihrem SDK gespeichert ist und darauf wartet, dass Nutzer:innen sie auslösen.

{% alert note %}
Die Aktivierung dieser Option führt zu einer leichten Verzögerung (< 100 ms) zwischen dem Auslösen einer In-App-Nachricht und der Anzeige der Nachricht aufgrund der zusätzlichen Berechtigungs- und Templating-Anfrage.
<br><br>
Verwenden Sie diese Option nicht für Nachrichten, die ausgelöst werden können, während eine Nutzerin oder ein Nutzer offline ist, oder wenn eine erneute Auswertung der Berechtigung und von Liquid nicht erforderlich ist.
{% endalert %}

#### Über die REST API hinzugefügte Daten in einer Nachricht verwenden {#use-data-added-by-rest-api-in-a-message}

Nutzerdaten, die der [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) in derselben Sitzung hinzufügt, können manchmal in der In-App-Nachricht dieser Nutzerin oder dieses Nutzers verwendet werden. Wenn sich beispielsweise eine Nutzerin oder ein Nutzer in der Zielgruppe für eine In-App-Nachricht befindet, die auf einen Trigger wartet, eine Sitzung startet und in derselben Sitzung die REST API ihr oder sein Profil aktualisiert, können diese neuen Daten in der In-App-Nachricht erscheinen, wenn **Campaign-Berechtigung vor der Anzeige erneut auswerten** ausgewählt ist. Braze löst das Template der In-App-Nachricht erst auf, wenn es Zeit zum Rendern ist.

Wenn ein Trigger sowohl Daten an Braze sendet als auch die In-App-Nachricht auslöst, kann die Nachricht diese neu aktualisierten Profildaten nicht verwenden, selbst mit einer geplanten Verzögerung. Verwenden Sie stattdessen zwei separate Trigger: einen zum Senden der Daten und einen zum Auslösen der In-App-Nachricht.

### Konversions-Events wählen {#choose-conversion-events}

Braze ermöglicht es Ihnen zu verfolgen, wie oft Nutzer:innen bestimmte Aktionen, [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), nach Erhalt einer Campaign ausführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen festzulegen, in dem eine Conversion gezählt wird, wenn die Nutzerin oder der Nutzer die angegebene Aktion ausführt.

{% endtab %}
{% tab Canvas %}

Wenn Sie es noch nicht getan haben, vervollständigen Sie die verbleibenden Abschnitte Ihrer Canvas-Komponente. Weitere Details zum Aufbau des restlichen Canvas, zur Implementierung von multivariaten Tests und intelligenter Auswahl und mehr finden Sie im Schritt [Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-3-build-your-canvas) unserer Canvas-Dokumentation.

Informationen zu Canvas-spezifischen In-App-Nachrichten-Optionen finden Sie unter [In-App-Nachrichten in Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas).

{% endtab %}
{% endtabs %}

## Schritt 8: Überprüfen und bereitstellen {#step-8-review-and-deploy}

Nachdem Sie den letzten Teil Ihrer Campaign oder Ihres Canvas fertiggestellt haben, überprüfen Sie die Details, [testen Sie sie]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) und senden Sie sie ab!

Sehen Sie sich als Nächstes [In-App-Nachrichten-Reporting]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) an, um zu erfahren, wie Sie auf die Ergebnisse Ihrer Messaging-Campaigns zugreifen können.

## Wissenswertes {#things-to-know}

### Limits für aktive In-App-Nachrichten-Campaigns {#active-in-app-message-campaign-limits}

Braze legt Wert auf Zuverlässigkeit und Geschwindigkeit. Wir empfehlen, nur die Daten an Braze zu senden, die Sie benötigen, und alle Campaigns zu deaktivieren, die keinen Mehrwert mehr für Ihre Marke bieten.

Die Verarbeitung aktionsbasierter In-App-Nachrichten-Campaigns, die sich noch im aktiven Status befinden, aber keine Nachrichten mehr senden oder nicht mehr benötigt werden, verlangsamt die Gesamtleistung der Braze-Dienste für Sie und andere Kund:innen. Diese zusätzliche Zeit für die Verarbeitung dieser großen Anzahl inaktiver Campaigns bedeutet, dass In-App-Nachrichten länger brauchen, um auf den Geräten der Endnutzer:innen zu erscheinen, was die Nutzererfahrung beeinträchtigt.

{% alert important %}
Sie können bis zu 200 aktive, aktionsbasierte In-App-Nachrichten-Campaigns pro Workspace haben, um die Geschwindigkeit der Nachrichtenzustellung zu optimieren und Timeouts zu vermeiden. Dies gilt nicht für Canvases.
{% endalert %}

Die 200 umfassen aktive In-App-Nachrichten-Campaigns, die ihre Endzeit noch nicht erreicht haben, sowie solche ohne Endzeit. Aktive In-App-Nachrichten-Campaigns, deren Endzeit überschritten ist, werden nicht gezählt. Der durchschnittliche Braze-Kunde hat insgesamt 26 gleichzeitig aktive Campaigns – es ist daher unwahrscheinlich, dass diese Beschränkung Sie betrifft.

### Auswertung der Zustellung zur Ortszeit {#local-time-delivery-evaluation}

Wenn eine In-App-Nachrichten-Campaign mit der Ortszeit der Nutzerin oder des Nutzers geplant ist, wird die Auswertung der Start- und Endzeit der Campaign auf dem Gerät selbst durchgeführt.

In-App-Nachrichten-Campaigns werden typischerweise an das Gerät der Nutzerin oder des Nutzers übermittelt, wenn die App-Sitzung startet oder aktualisiert wird. In diesem Moment:

1. Das SDK prüft, ob die Nutzerin oder der Nutzer für triggerbasierte In-App-Nachrichten qualifiziert ist.
2. Das Gerät prüft, ob das Trigger-Event der Nutzerin oder des Nutzers innerhalb der Start- und Endzeit der Campaign (definiert durch die Ortszeit der Nutzerin oder des Nutzers) aufgetreten ist.
3. Wenn beide Bedingungen erfüllt sind, ist die In-App-Nachricht zur Anzeige berechtigt.

#### Hinweise {#considerations}

- Wenn eine Nutzerin oder ein Nutzer ein Event auslöst (z. B. einen Button-Tipp) kurz nachdem die In-App-Nachricht zugestellt wurde, wird die Nachricht möglicherweise erst bei der nächsten Sitzungsaktualisierung angezeigt – vorausgesetzt, alle Berechtigungskriterien sind weiterhin erfüllt.
- Ähnlich wie bei anderen Kanaltypen sollten In-App-Nachrichten-Campaigns idealerweise 24–48 Stunden im Voraus gestartet werden. Dieser Puffer gibt Nutzer:innen ausreichend Zeit, die Berechtigungskriterien zu erfüllen und eine Sitzung zu starten, damit die Nachricht ausgewertet und angezeigt werden kann.