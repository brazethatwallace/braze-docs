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

Bevor Sie Ihr Banner starten können, muss Ihr Entwicklungsteam [Placements in Ihrer App oder Website einrichten]({{site.baseurl}}/developer_guide/banners/placements). Sie können Ihre Banner-Campaign in der Zwischenzeit trotzdem entwerfen, aber Sie können die Campaign erst starten, wenn die Placements konfiguriert sind.

## Eine Banner-Nachricht erstellen {#create-a-banner-message}

{% multi_lang_include banners/creating_placements.md section="user" %}

### 2. Schritt: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten {#step-2-choose-where-to-build-your-message}

Sind Sie unsicher, ob Ihre Nachricht über eine Campaign oder ein Canvas gesendet werden soll? Campaigns eignen sich besser für einzelne, gezielte Messaging-Kampagnen, während Canvases besser für mehrstufige User-Journeys geeignet sind.

{% tabs %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Create Campaign**.
2. Wählen Sie **Banner**.
3. Geben Sie Ihrer Campaign einen klaren und aussagekräftigen Namen.
4. Fügen Sie bei Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu. Tags erleichtern das Auffinden Ihrer Campaigns und das Erstellen von Berichten. Wenn Sie beispielsweise den Berichts-Builder verwenden, können Sie nach den relevanten Tags filtern.
5. Wählen Sie das zuvor erstellte Placement aus, um es mit Ihrer Campaign zu verknüpfen.
6. Fügen Sie bei Bedarf Varianten hinzu. Sie können für jede Variante einen anderen Nachrichtentyp und ein anderes Layout wählen. Weitere Informationen zu Varianten finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).
7. Wählen Sie ein Startdatum und eine Startzeit für Ihre Banner-Campaign. Standardmäßig laufen Banner unbegrenzt. Sie können dies ändern, indem Sie **End Time** auswählen und ein Enddatum und eine Endzeit angeben.

{% alert tip %}
Wenn alle Nachrichten in Ihrer Campaign ähnlich sein oder denselben Inhalt haben werden, verfassen Sie Ihre Nachricht, bevor Sie weitere Varianten hinzufügen. Anschließend können Sie **Copy from Variant** aus dem Dropdown **Add Variant** auswählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) mit dem Canvas-Composer.
2. Nachdem Sie Ihr Canvas eingerichtet haben, fügen Sie im Canvas-Builder einen Nachrichten-Schritt hinzu. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie **Banner** als Ihren Messaging-Kanal.
4. Wählen Sie ein Placement für das Banner.
5. Legen Sie die Priorität fest. Die [Banner-Priorität]({{site.baseurl}}/user_guide/channels/banners#priority) bestimmt die Reihenfolge, in der Banner angezeigt werden, wenn sie dasselbe Placement teilen.
6. Legen Sie eine Ablaufzeit für das Banner fest. Dies kann nach einer bestimmten Zeitdauer nach Verfügbarkeit des Schritts oder zu einem bestimmten Datum und einer bestimmten Uhrzeit sein. Die maximale Ablaufdauer beträgt 31 Tage, nachdem der Schritt für die Nutzer:innen verfügbar wird.

{% endtab %}
{% endtabs %}

### 3. Schritt: Banner verfassen {#compose-a-banner}

Wählen Sie als Nächstes, wie Sie mit dem Erstellen beginnen möchten:

- **Drag-and-Drop-Editor:** Beginnen Sie mit einem leeren Banner und erstellen Sie es visuell mit Blöcken und Zeilen.
- **HTML-Editor:** Beginnen Sie mit einem leeren Banner und arbeiten Sie direkt in HTML.
- **Templates:** Öffnen Sie die Template-Bibliothek und wählen Sie ein Design aus **Braze Templates** oder **Your Templates**. Templates werden im Drag-and-Drop-Editor zur Anpassung geöffnet.

![Optionen zur Auswahl des Drag-and-Drop-Editors, HTML-Editors oder von Templates für Ihr Banner.]({% image_buster /assets/img/banners/choose_banner_editing_experience.png %})

#### Schritt 3.1: Banner gestalten {#step-31-style-the-banner}

{% tabs %}
{% tab Drag-and-Drop-Editor %}

Sie können Blöcke und Zeilen per Drag-and-Drop in den Canvas-Bereich ziehen, um mit dem Erstellen Ihrer Nachricht zu beginnen. Eine Referenz der Banner-Editor-Blöcke und Links zu gemeinsamen Eigenschaftsdetails finden Sie unter [Editor-Blöcke (Banner)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=banners).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Um die Hintergrundeigenschaften, Rahmeneinstellungen und mehr Ihrer Nachricht anzupassen, wählen Sie **Styles**. Wenn Sie nur den Stil für einen bestimmten Block oder eine bestimmte Zeile anpassen möchten, wählen Sie das Element aus, um Änderungen vorzunehmen.

![Style-Panel des Banner-Composers.]({% image_buster /assets/img/banners/banner_card_styles.png %})

{% multi_lang_include drag_and_drop/hide_rows_and_blocks_by_device.md channel='banner' %}

{% endtab %}
{% tab HTML-Editor %}

Der HTML-Editor eignet sich am besten für Teams, die bereits eigene HTML-Templates pflegen oder die volle Kontrolle über Markup und Styling wünschen. Sie können angepasstes HTML direkt in den Editor schreiben oder einfügen. Liquid-Personalisierungs-Tags werden vollständig unterstützt, sodass Sie auf Nutzer:innen-Attribute, angepasste Attribute, Katalogartikel und mehr verweisen können.

{% alert tip %}
Benötigen Sie Hilfe beim Erstellen Ihres Banner-HTML? Wählen Sie **Ask Operator** im HTML-Editor und beschreiben Sie das gewünschte Banner. [BrazeAI<sup>TM</sup> Operator]({{site.baseurl}}/user_guide/brazeai/operator) generiert HTML, das Sie überprüfen und in den Editor einfügen können. Weitere Informationen finden Sie unter [Nachrichten generieren]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages).
{% endalert %}

Für Klick- und Schließ-Tracking in Ihrem angepassten HTML müssen Sie JavaScript-Bridge-Methoden explizit aufrufen. Die vollständige Referenz finden Sie unter [Angepasster Code und JavaScript-Bridge für Banner]({{site.baseurl}}/user_guide/channels/banners/custom_code).

{% endtab %}
{% endtabs %}

{% alert note %}
Um Nutzer:innen in verschiedenen Sprachen innerhalb einer einzelnen Banner-Campaign anzusprechen, lesen Sie [Mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).
{% endalert %}

#### Schritt 3.2: Klickverhalten definieren (optional) {#step-32-define-on-click-behavior-optional}

{% tabs %}
{% tab Drag-and-Drop-Editor %}

Wenn Nutzer:innen auf einen Link im Banner klicken, können Sie sie tiefer in Ihre App navigieren oder auf eine andere Webseite weiterleiten. Zusätzlich können Sie [ein angepasstes Attribut oder Ereignis protokollieren]({{site.baseurl}}/developer_guide/analytics), wodurch das Profil der Nutzer:innen mit angepassten Daten aktualisiert wird, wenn sie auf das Banner klicken. Für ein detaillierteres Klick-Tracking weisen Sie jedem interaktiven Element über das Feld **Identifier for Reporting** in dessen Eigenschaftenpanel einen angepassten Bezeichner zu.

{% alert important %}
{::nomarkdown}
Das Klickverhalten kann überschrieben werden, wenn ein bestimmtes Element (z. B. ein Button, Link oder Bild des Banners) ein eigenes Klickverhalten hat. Beispiel bei folgenden Klickverhalten:<br><ul><li>Ein Banner hat ein Klickverhalten, das zur Startseite einer Website weiterleitet.</li><li>Ein Bild im Banner hat ein Klickverhalten, das zur Produktseite einer Website weiterleitet.</li></ul>Wenn Nutzer:innen auf das Bild klicken, werden sie zur Produktseite weitergeleitet. Ein Klick auf den umgebenden Bereich des Banners leitet sie jedoch zur Startseite weiter.
{:/}
{% endalert %}

{% endtab %}
{% tab HTML-Editor %}

Im HTML-Editor erfolgt das Klick-Tracking nicht automatisch. Sie müssen `brazeBridge.logClick()` in Ihrem HTML für jedes klickbare Element aufrufen, das Sie tracken möchten. Beispiel:

```html
<a href="https://example.com" onclick="brazeBridge.logClick()">Shop now</a>
```

Die vollständige JavaScript-Bridge-Referenz finden Sie unter [Angepasster Code und JavaScript-Bridge für Banner]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge).

{% endtab %}
{% endtabs %}

#### Schritt 3.3: Schließverhalten konfigurieren (optional) {#dismiss-behavior}

{% tabs %}
{% tab Drag-and-Drop-Editor %}

Aktivieren Sie das Kontrollkästchen **Banner can be dismissed** im Abschnitt **Dismiss behavior**, um Nutzer:innen das Schließen des Banners zu ermöglichen. Diese Option ist nützlich, wenn Sie ein zeitlich begrenztes Angebot für eine breite Zielgruppe bewerben, aber nicht interessierten Nutzer:innen erlauben möchten, die Nachricht auszublenden.

Wenn das Schließen aktiviert ist, können Sie den Schließen-Button im Abschnitt **Dismiss behavior** anpassen:

| Einstellung | Beschreibung |
|---------|-------------|
| **Button size** | Die Größe des Schließen-Buttons, der auf dem Banner angezeigt wird. |
| **Button color** | Die Farbe des Schließen-Buttons. |
| **ARIA label** | Das barrierefreie Label für den Schließen-Button, das von Screenreadern verwendet wird. Standardmäßig „Close“, wenn leer gelassen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Einstellungen für den Schließen-Button" }

Wenn Nutzer:innen ein Banner schließen, wird es für diese Nutzer:innen nicht erneut angezeigt, selbst wenn sie weiterhin die Targeting-Kriterien der Campaign erfüllen.

{% endtab %}
{% tab HTML-Editor %}

Im HTML-Editor wird das Schließen in Ihrem HTML über `brazeBridge.closeMessage()` gesteuert. Kombinieren Sie es mit `brazeBridge.logClick()`, um die Schließaktion auch als Klick-Ereignis zu tracken. Beispiel:

```html
<a href="#" onclick="brazeBridge.logClick(); brazeBridge.closeMessage();">&#x2715; Close</a>
```

Wenn Nutzer:innen ein Banner auf diese Weise schließen, wird es für diese Nutzer:innen nicht erneut angezeigt, selbst wenn sie weiterhin die Targeting-Kriterien der Campaign erfüllen.

Die vollständige JavaScript-Bridge-Referenz finden Sie unter [Angepasster Code und JavaScript-Bridge für Banner]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge).

{% endtab %}
{% endtabs %}

#### Schritt 3.4: Angepasste Eigenschaften hinzufügen (optional) {#custom-properties}

Sie können einem Banner angepasste Eigenschaften hinzufügen, um strukturierte Metadaten wie Strings oder JSON-Objekte anzuhängen. Diese Eigenschaften beeinflussen nicht die Darstellung des Banners, können aber [über das Braze SDK abgerufen werden]({{site.baseurl}}/developer_guide/banners/placements), um das Verhalten oder Erscheinungsbild Ihrer App zu ändern. Beispielsweise könnten Sie:

{% multi_lang_include banners/metadata_use_cases.md %}

Angepasste Eigenschaften funktionieren im Drag-and-Drop-Editor und im HTML-Editor gleich. Um eine angepasste Eigenschaft hinzuzufügen, wählen Sie **Settings** > **Properties** > **Add property**.

![Die Eigenschaftenseite mit der Option, die erste angepasste Eigenschaft zu einer Banner-Campaign hinzuzufügen.]({% image_buster /assets/img/banners/add_property.png %})

Füllen Sie für jede Eigenschaft, die Sie hinzufügen möchten, Folgendes aus:

| Feld | Beschreibung | Beispiel |
|------|-------------|---------|
| Eigenschaftstyp | Der Datentyp für die Eigenschaft. Unterstützte Typen sind String, Boolescher Wert, Zahl, Zeitstempel, Bild-URL und JSON-Objekt. | String |
| Eigenschaftsschlüssel | Der eindeutige Bezeichner für die Eigenschaft. Dieser Schlüssel wird im SDK verwendet, um auf die Eigenschaft zuzugreifen. | `color` |
| Wert | Der der Eigenschaft zugewiesene Wert. Muss dem ausgewählten Eigenschaftstyp entsprechen. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Angepasste Eigenschaften hinzufügen" }

Wenn Sie fertig sind, wählen Sie **Done**.

![Die Eigenschaftenseite mit einer String-Eigenschaft mit dem Schlüssel „color“ und dem Wert #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

### 4. Schritt: Erstellen Sie den Rest Ihrer Campaign oder Ihres Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Banner-Priorität festlegen (optional) {#set-banner-priority-optional}

Die [Banner-Priorität]({{site.baseurl}}/user_guide/channels/banners#priority) bestimmt die Reihenfolge, in der Banner angezeigt werden, wenn sie dasselbe Placement teilen. Um die Priorität manuell festzulegen:

1. Wählen Sie **Set exact priority**.
2. Ordnen Sie die Campaigns per Drag-and-Drop in der richtigen Prioritätsreihenfolge an.
3. Wählen Sie **Apply Sort**.

{% alert tip %}
Wenn Sie mehrere Banner-Campaigns mit derselben Placement-ID haben, empfehlen wir die Verwendung des Drag-and-Drop-Prioritätssortierers, um die genaue Priorität festzulegen.
{% endalert %}

#### Erneute Berechtigung konfigurieren (optional) {#re-eligibility}

Standardmäßig sind Nutzer:innen, die ein Banner geschlossen haben, nie erneut für diese Campaign berechtigt. Um Nutzer:innen, die das Banner geschlossen haben, das Banner erneut anzuzeigen, gehen Sie zum Schritt **Delivery Controls** und wählen Sie **Allow users to become re-eligible to receive campaign**. Wenn aktiviert, legen Sie ein Abklingfenster in Minuten, Stunden, Tagen oder Wochen fest.

Der Countdown beginnt, wenn Nutzer:innen das Banner schließen. Nach Ablauf des Fensters sind die Nutzer:innen automatisch erneut berechtigt – ein Neustart der Campaign ist nicht erforderlich. Die erneute Berechtigung wird pro Nutzer:in und pro Campaign verfolgt.

#### Zielgruppe auswählen {#choose-your-audience}

1. Wählen Sie unter **Target Audiences** Segmente oder Filter aus, um Ihre Zielgruppe einzugrenzen. Sie erhalten automatisch eine Vorschau der ungefähren Segment-Population. Die genaue Segment-Zugehörigkeit wird berechnet, bevor die Nachricht gesendet wird.

{% multi_lang_include audience/target_audiences.md %}

{:start="2"}
2. Verfolgen Sie unter **Assign Conversions**, wie oft Nutzer:innen bestimmte Aktionen nach Erhalt einer Campaign ausführen, indem Sie Konversions-Events mit einem Zeitfenster von bis zu 30 Tagen definieren, um die Aktion als Conversion zu zählen.

#### Konversions-Events auswählen {#choose-conversion-events}

Braze ermöglicht es Ihnen, [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) zu verfolgen – also wie oft Nutzer:innen bestimmte Aktionen nach Erhalt einer Campaign ausführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen festzulegen, in dem eine Conversion gezählt wird, wenn die Nutzer:innen die angegebene Aktion ausführen.

{% endtab %}

{% tab Canvas %}

Falls noch nicht geschehen, vervollständigen Sie die verbleibenden Abschnitte Ihrer Canvas-Komponente. Weitere Details zum Aufbau des restlichen Canvas, zur Implementierung von [multivariaten Tests]({{site.baseurl}}/user_guide/messaging/ab_testing) und [intelligenter Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection) und mehr finden Sie im Schritt [Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas) unserer Canvas-Dokumentation.

Um die erneute Berechtigung für Canvas-Banner-Schritte zu steuern, verwenden Sie die Canvas-Wiedereintrittseinstellungen. Weitere Informationen finden Sie unter [Erneute Berechtigung für Campaigns und Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).

{% endtab %}
{% endtabs %}

### 5. Schritt: Nachricht testen (optional) {#step-5-test-your-message-optional}

{% multi_lang_include banners/testing.md page="campaigns" %}

### 6. Schritt: Überprüfen und bereitstellen {#step-6-review-and-deploy}

Nachdem Sie Ihre Campaign oder Ihr Canvas fertiggestellt haben, überprüfen Sie die Details, [testen Sie sie]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) und senden Sie sie, wenn Sie bereit sind.