---
nav_title: "Banner erstellen"
article_title: "Banner erstellen"
page_order: 1
description: "Dieser Referenzartikel beschreibt, wie Sie Banner mit Braze-Campaigns und Canvases erstellen, verfassen, konfigurieren und senden."
tool:
  - Campaigns
channel:
  - banners
---

# Banner erstellen {#create-a-banner}

> Erfahren Sie, wie Sie Banner erstellen, wenn Sie Campaigns und Canvases in Braze aufbauen. Allgemeine Informationen finden Sie unter [Über Banner]({{site.baseurl}}/user_guide/channels/banners).

## Voraussetzungen {#prerequisites}

Bevor Sie Ihr Banner starten können, muss Ihr Entwicklungsteam [Placements in Ihrer App oder Website einrichten]({{site.baseurl}}/developer_guide/banners/placements). Sie können in der Zwischenzeit trotzdem Ihre Banner-Campaign entwerfen, aber Sie können die Campaign erst starten, wenn die Placements konfiguriert sind.

## Banner-Nachricht erstellen {#create-a-banner-message}

{% multi_lang_include banners/creating_placements.md section="user" %}

### Schritt 2: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten {#step-2-choose-where-to-build-your-message}

Sie sind nicht sicher, ob Ihre Nachricht als Campaign oder Canvas gesendet werden sollte? Campaigns eignen sich besser für einzelne, gezielte Messaging-Kampagnen, während Canvases besser für mehrstufige User Journeys geeignet sind.

{% tabs %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Campaign erstellen**.
2. Wählen Sie **Banner**.
3. Geben Sie Ihrer Campaign einen klaren und aussagekräftigen Namen.
4. Fügen Sie bei Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu. Tags erleichtern das Auffinden Ihrer Campaigns und das Erstellen von Berichten. Wenn Sie beispielsweise den Berichts-Builder verwenden, können Sie nach den relevanten Tags filtern.
5. Wählen Sie das zuvor erstellte Placement aus, um es mit Ihrer Campaign zu verknüpfen.
6. Fügen Sie bei Bedarf Varianten hinzu. Sie können für jede Variante einen anderen Nachrichtentyp und ein anderes Layout wählen. Weitere Informationen zu Varianten finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).
7. Wählen Sie ein Startdatum und eine Startzeit für Ihre Banner-Campaign. Standardmäßig laufen Banner unbegrenzt. Sie können dies ändern, indem Sie **Endzeit** auswählen und ein Enddatum sowie eine Endzeit festlegen.

{% alert tip %}
Wenn alle Nachrichten in Ihrer Campaign ähnlich sein oder denselben Inhalt haben werden, verfassen Sie Ihre Nachricht, bevor Sie zusätzliche Varianten hinzufügen. Anschließend können Sie **Von Variante kopieren** aus dem Dropdown **Variante hinzufügen** auswählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Erstellen Sie Ihren Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) mit dem Canvas-Composer.
2. Nachdem Sie Ihren Canvas eingerichtet haben, fügen Sie im Canvas-Builder einen Nachrichtenschritt hinzu. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie **Banner** als Ihren Messaging-Kanal.
4. Wählen Sie ein Placement für das Banner.
5. Legen Sie die Priorität fest. Die [Banner-Priorität]({{site.baseurl}}/user_guide/channels/banners#priority) bestimmt die Reihenfolge, in der Banner angezeigt werden, wenn sie dasselbe Placement nutzen.
6. Legen Sie eine Ablaufzeit für das Banner fest. Dies kann nach einer bestimmten Dauer, nachdem der Schritt verfügbar ist, oder zu einem bestimmten Datum und einer bestimmten Uhrzeit erfolgen. Die maximale Ablaufdauer beträgt 31 Tage, nachdem der Schritt für die Nutzer:innen verfügbar wird.

{% endtab %}
{% endtabs %}

### Schritt 3: Banner verfassen {#compose-a-banner}

Wählen Sie als Nächstes, wie Sie mit dem Erstellen beginnen möchten:

- **Drag-and-drop-Editor:** Beginnen Sie mit einem leeren Banner und erstellen Sie es visuell mit Blöcken und Zeilen.
- **HTML-Editor:** Beginnen Sie mit einem leeren Banner und arbeiten Sie direkt in HTML.
- **Templates:** Öffnen Sie die Template-Bibliothek und wählen Sie ein Design aus **Braze-Templates** oder **Ihre Templates**. Templates werden im Drag-and-drop-Editor zur Anpassung geöffnet.

![Optionen zur Auswahl des Drag-and-drop-Editors, HTML-Editors oder von Templates für Ihr Banner.]({% image_buster /assets/img/banners/choose_banner_editing_experience.png %})

#### Schritt 3.1: Banner gestalten {#step-31-style-the-banner}

{% tabs %}
{% tab Drag-and-drop-Editor %}

Sie können Blöcke und Zeilen per Drag-and-drop in den Canvas-Bereich ziehen, um mit dem Erstellen Ihrer Nachricht zu beginnen. Eine Referenz der Banner-Editor-Blöcke und Links zu gemeinsamen Eigenschaftsdetails finden Sie unter [Editor-Blöcke (Banner)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=banners).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Um die Hintergrund-Eigenschaften, Rahmeneinstellungen und mehr Ihrer Nachricht anzupassen, wählen Sie **Styles**. Wenn Sie nur den Stil für einen bestimmten Block oder eine bestimmte Zeile anpassen möchten, wählen Sie ihn aus, um Änderungen vorzunehmen.

![Styles-Panel des Banner-Composers.]({% image_buster /assets/img/banners/banner_card_styles.png %})

{% endtab %}
{% tab HTML-Editor %}

Der HTML-Editor eignet sich am besten für Teams, die bereits eigene HTML-Templates pflegen oder die volle Kontrolle über Markup und Styling wünschen. Sie können benutzerdefiniertes HTML direkt in den Editor schreiben oder einfügen. Liquid-Personalisierungs-Tags werden vollständig unterstützt, sodass Sie auf Nutzerattribute, angepasste Attribute, Katalogartikel und mehr verweisen können.

{% alert tip %}
Benötigen Sie Hilfe beim Erstellen Ihres Banner-HTMLs? Wählen Sie **Ask Operator** im HTML-Editor und beschreiben Sie das gewünschte Banner. [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator) generiert HTML, das Sie überprüfen und in den Editor einfügen können. Weitere Informationen finden Sie unter [Nachrichten generieren]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages).
{% endalert %}

Für Klick- und Schließen-Tracking in Ihrem benutzerdefinierten HTML müssen Sie JavaScript-Bridge-Methoden explizit aufrufen. Die vollständige Referenz finden Sie unter [Benutzerdefinierter Code und JavaScript-Bridge für Banner]({{site.baseurl}}/user_guide/channels/banners/custom_code).

{% endtab %}
{% endtabs %}

{% alert note %}
Um Nutzer:innen in verschiedenen Sprachen innerhalb einer einzelnen Banner-Campaign anzusprechen, lesen Sie [Mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).
{% endalert %}

#### Schritt 3.2: Klick-Verhalten definieren (optional) {#step-32-define-on-click-behavior-optional}

{% tabs %}
{% tab Drag-and-drop-Editor %}

Wenn Nutzer:innen auf einen Link im Banner klicken, können Sie wählen, ob sie tiefer in Ihre App navigiert oder auf eine andere Webseite weitergeleitet werden. Zusätzlich können Sie wählen, ein [angepasstes Attribut oder Event zu protokollieren]({{site.baseurl}}/developer_guide/analytics), wodurch das Profil der Nutzer:innen mit benutzerdefinierten Daten aktualisiert wird, wenn sie auf das Banner klicken. Für eine detailliertere Klick-Verfolgung weisen Sie jedem interaktiven Element eine benutzerdefinierte Kennung über das Feld **Bezeichner für Berichterstellung** in dessen Eigenschafts-Panel zu.

{% alert important %}
{::nomarkdown}
Das Klick-Verhalten kann überschrieben werden, wenn ein bestimmtes Element (z. B. ein Button, Link oder Bild des Banners) ein eigenes Klick-Verhalten hat. Zum Beispiel bei folgenden Klick-Verhalten:<br><ul><li>Ein Banner hat ein Klick-Verhalten, das zur Startseite einer Website weiterleitet.</li><li>Ein Bild im Banner hat ein Klick-Verhalten, das zur Produktseite einer Website weiterleitet.</li></ul>Wenn Nutzer:innen auf das Bild klicken, werden sie zur Produktseite weitergeleitet. Ein Klick auf den umgebenden Bereich im Banner leitet sie jedoch zur Startseite weiter.
{:/}
{% endalert %}

{% endtab %}
{% tab HTML-Editor %}

Im HTML-Editor erfolgt das Klick-Tracking nicht automatisch. Sie müssen `brazeBridge.logClick()` innerhalb Ihres HTMLs für jedes klickbare Element aufrufen, das Sie verfolgen möchten. Beispiel:

```html
<a href="https://example.com" onclick="brazeBridge.logClick()">Shop now</a>
```

Die vollständige JavaScript-Bridge-Referenz finden Sie unter [Benutzerdefinierter Code und JavaScript-Bridge für Banner]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge).

{% endtab %}
{% endtabs %}

#### Schritt 3.3: Schließen-Verhalten konfigurieren (optional) {#dismiss-behavior}

{% alert important %}
Für das Schließen von Bannern sind die folgenden Mindest-SDK-Versionen erforderlich. Ältere SDK-Versionen rendern keine Banner mit aktiviertem Schließen.
{% sdk_min_versions swift:14.1.0 android:42.1.0 web:6.7.1 reactnative:22.0.0 flutter:20.0.0 %}
{% endalert %}

{% tabs %}
{% tab Drag-and-drop-Editor %}

Aktivieren Sie das Kontrollkästchen **Banner kann geschlossen werden** im Abschnitt **Schließen-Verhalten**, um Nutzer:innen das Schließen des Banners zu ermöglichen. Dies ist nützlich, wenn Sie einem breiten Publikum ein zeitlich begrenztes Angebot präsentieren, aber nicht interessierten Nutzer:innen trotzdem ermöglichen möchten, die Nachricht auszublenden.

Wenn das Schließen aktiviert ist, können Sie den Schließen-Button im Abschnitt **Schließen-Verhalten** anpassen:

| Einstellung | Beschreibung |
|---------|-------------|
| **Button-Größe** | Die Größe des Schließen-Buttons, der auf dem Banner angezeigt wird. |
| **Button-Farbe** | Die Farbe des Schließen-Buttons. |
| **ARIA-Label** | Das barrierefreie Label für den Schließen-Button, das von Screenreadern verwendet wird. Standardmäßig „Schließen“, wenn leer gelassen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Einstellungen für den Schließen-Button" }

Wenn Nutzer:innen ein Banner schließen, wird es für diese Nutzer:innen nicht erneut angezeigt, selbst wenn sie weiterhin die Targeting-Kriterien der Campaign erfüllen.

{% endtab %}
{% tab HTML-Editor %}

Im HTML-Editor wird das Schließen in Ihrem HTML über `brazeBridge.closeMessage()` gesteuert. Kombinieren Sie es mit `brazeBridge.logClick()`, um die Schließen-Aktion auch als Klick-Event zu verfolgen. Beispiel:

```html
<a href="#" onclick="brazeBridge.logClick(); brazeBridge.closeMessage();">&#x2715; Close</a>
```

Wenn Nutzer:innen ein Banner auf diese Weise schließen, wird es für diese Nutzer:innen nicht erneut angezeigt, selbst wenn sie weiterhin die Targeting-Kriterien der Campaign erfüllen.

Die vollständige JavaScript-Bridge-Referenz finden Sie unter [Benutzerdefinierter Code und JavaScript-Bridge für Banner]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge).

{% endtab %}
{% endtabs %}

#### Schritt 3.4: Benutzerdefinierte Eigenschaften hinzufügen (optional) {#custom-properties}

Sie können einem Banner benutzerdefinierte Eigenschaften hinzufügen, um strukturierte Metadaten wie Strings oder JSON-Objekte anzuhängen. Diese Eigenschaften beeinflussen nicht die Darstellung des Banners, können jedoch [über das Braze SDK abgerufen werden]({{site.baseurl}}/developer_guide/banners/placements), um das Verhalten oder Erscheinungsbild Ihrer App zu verändern. Beispielsweise könnten Sie:

{% multi_lang_include banners/metadata_use_cases.md %}

Benutzerdefinierte Eigenschaften funktionieren im Drag-and-drop-Editor und im HTML-Editor auf dieselbe Weise. Um eine benutzerdefinierte Eigenschaft hinzuzufügen, wählen Sie **Einstellungen** > **Eigenschaften** > **Eigenschaft hinzufügen**.

![Die Eigenschaftenseite mit der Option, die erste benutzerdefinierte Eigenschaft zu einer Banner-Campaign hinzuzufügen.]({% image_buster /assets/img/banners/add_property.png %})

Füllen Sie für jede Eigenschaft, die Sie hinzufügen möchten, die folgenden Felder aus:

| Feld | Beschreibung | Beispiel |
|-------|-------------|---------|
| Eigenschaftstyp | Der Datentyp für die Eigenschaft. Unterstützte Typen sind String, Boolean, Nummer, Zeitstempel, Bild-URL und JSON-Objekt. | String |
| Eigenschaftsschlüssel | Der eindeutige Bezeichner für die Eigenschaft. Dieser Schlüssel wird im SDK verwendet, um auf die Eigenschaft zuzugreifen. | `color` |
| Wert | Der der Eigenschaft zugewiesene Wert. Muss zum ausgewählten Eigenschaftstyp passen. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 3.4: Benutzerdefinierte Eigenschaften hinzufügen (optional)" }

Wenn Sie fertig sind, wählen Sie **Fertig**.

![Die Eigenschaftenseite mit einer String-Eigenschaft mit dem Schlüssel „color“ und dem Wert #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

#### Schritt 3.5: Mit Connected Content personalisieren (optional) {#step-35-personalize-with-connected-content-optional}

{% multi_lang_include alerts/early_access_beta_alert.md feature='Connected Content for Banners' %}

Da Banner inline während einer Session-Aktualisierung gerendert werden, funktioniert Connected Content in diesem Kanal anders als in anderen Kanälen:

- Es werden nur GET-Anfragen unterstützt.
- Alle Placements in einer einzelnen Aktualisierung (bis zu 10) teilen sich ein Rendering-Budget von etwa zwei Sekunden. Wenn ein Aufruf langsam ist, das Zeitlimit überschreitet oder das Budget überschritten wird, wird das Connected-Content-Ergebnis für dieses Placement als null behandelt. Banner führen keine Wiederholungsversuche durch.

Für beste Ergebnisse:

- Halten Sie Ihre Endpunkte schnell und [cachen Sie Antworten]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) wann immer möglich.
- Begrenzen Sie die Anzahl eindeutiger Connected-Content-URLs über die Placements hinweg, die zusammen gerendert werden.
- Vermeiden Sie verkettete Aufrufe, bei denen eine Connected-Content-Antwort die URL für den nächsten bestimmt. Jeder zusätzliche Aufruf trägt zum gemeinsamen Budget bei.
- Verwenden Sie Liquid-Guard-Anweisungen oder den [`default`-Filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values), um null-Ergebnisse zu behandeln und leere Banner zu vermeiden.

### Schritt 4: Erstellen Sie den Rest Ihrer Campaign oder Ihres Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Banner-Priorität festlegen (optional) {#set-banner-priority-optional}

Die [Banner-Priorität]({{site.baseurl}}/user_guide/channels/banners#priority) bestimmt die Reihenfolge, in der Banner angezeigt werden, wenn sie dasselbe Placement nutzen. Um die Priorität manuell festzulegen:

1. Wählen Sie **Set exact priority**.
2. Ziehen Sie die Campaigns per Drag-and-drop in die richtige Prioritätsreihenfolge.
3. Wählen Sie **Apply Sort**.

{% alert tip %}
Wenn Sie mehrere Banner-Campaigns mit derselben Placement-ID haben, empfehlen wir die Verwendung des Drag-and-drop-Prioritätssortierers, um die genaue Priorität festzulegen.
{% endalert %}

#### Wiederberechtigung konfigurieren (optional) {#re-eligibility}

Standardmäßig sind Nutzer:innen, die ein Banner geschlossen haben, nie wieder für diese Campaign berechtigt. Um geschlossenen Nutzer:innen das erneute Anzeigen des Banners zu ermöglichen, gehen Sie zum Schritt **Zustellungskontrollen** und wählen Sie **Nutzer:innen erlauben, wieder für die Campaign berechtigt zu werden**. Wenn aktiviert, legen Sie ein Abklingfenster in Minuten, Stunden, Tagen oder Wochen fest.

Der Countdown beginnt, wenn die Nutzer:innen das Banner schließen. Nach Ablauf des Fensters sind die Nutzer:innen automatisch wieder berechtigt – kein Neustart der Campaign erforderlich. Die Wiederberechtigung wird pro Nutzer:in und Campaign verfolgt.

#### Zielgruppe auswählen {#choose-your-audience}

1. Wählen Sie unter **Zielgruppen** Segmente oder Filter, um Ihre Zielgruppe einzugrenzen. Sie erhalten automatisch eine Vorschau der ungefähren Segment-Größe. Die genaue Segment-Zugehörigkeit wird berechnet, bevor die Nachricht gesendet wird.

{% multi_lang_include audience/target_audiences.md %}

{:start="2"}
2. Verfolgen Sie unter **Konversionen zuweisen**, wie oft Nutzer:innen nach Erhalt einer Campaign bestimmte Aktionen ausführen, indem Sie Konversions-Events mit einem Zeitfenster von bis zu 30 Tagen definieren, innerhalb dessen die Aktion als Konversion gezählt wird.

#### Konversions-Events auswählen {#choose-conversion-events}

Braze ermöglicht es Ihnen, [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) zu verfolgen – wie oft Nutzer:innen nach Erhalt einer Campaign bestimmte Aktionen ausführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen festzulegen, in dem eine Konversion gezählt wird, wenn die Nutzer:innen die angegebene Aktion ausführen.

{% endtab %}

{% tab Canvas %}

Falls noch nicht geschehen, vervollständigen Sie die verbleibenden Abschnitte Ihrer Canvas-Komponente. Details zum Erstellen des restlichen Canvas, einschließlich multivariatem Testen und [Optimieren mit BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai), finden Sie unter [Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas).

Um die Wiederberechtigung für Canvas-Banner-Schritte zu steuern, verwenden Sie die Canvas-Wiedereintrittseinstellungen. Weitere Informationen finden Sie unter [Wiederberechtigung für Campaigns und Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).

{% endtab %}
{% endtabs %}

### Schritt 5: Nachricht testen (optional) {#step-5-test-your-message-optional}

{% multi_lang_include banners/testing.md page="campaigns" %}

### Schritt 6: Überprüfen und bereitstellen {#step-6-review-and-deploy}

Nachdem Sie Ihre Campaign oder Ihren Canvas fertig erstellt haben, überprüfen Sie die Details, [testen Sie sie]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) und senden Sie sie, wenn Sie bereit sind.