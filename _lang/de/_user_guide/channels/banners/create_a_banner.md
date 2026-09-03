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

Bevor Sie Ihr Banner starten können, muss Ihr Entwicklungsteam [Placements in Ihrer App oder Website einrichten]({{site.baseurl}}/developer_guide/banners/placements). Sie können in der Zwischenzeit trotzdem Ihren Entwurf für die Banner-Campaign erstellen, aber Sie können die Campaign erst starten, wenn die Placements konfiguriert sind.

## Eine Banner-Nachricht erstellen {#create-a-banner-message}

{% multi_lang_include banners/creating_placements.md section="user" %}

### Schritt 2: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten {#step-2-choose-where-to-build-your-message}

Sie sind sich nicht sicher, ob Ihre Nachricht über eine Campaign oder ein Canvas gesendet werden soll? Campaigns eignen sich besser für einzelne, gezielte Messaging-Kampagnen, während Canvases besser für mehrstufige User Journeys geeignet sind.

{% tabs %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Campaign erstellen**.
2. Wählen Sie **Banner**.
3. Geben Sie Ihrer Campaign einen eindeutigen und aussagekräftigen Namen.
4. Fügen Sie bei Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu. Tags erleichtern das Auffinden Ihrer Campaigns und das Erstellen von Berichten. Wenn Sie beispielsweise den Berichts-Builder verwenden, können Sie nach den relevanten Tags filtern.
5. Wählen Sie die zuvor erstellte Platzierung aus, um sie mit Ihrer Campaign zu verknüpfen.
6. Fügen Sie bei Bedarf Varianten hinzu. Sie können für jede Variante einen anderen Nachrichtentyp und ein anderes Layout wählen. Weitere Informationen zu Varianten finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).
7. Wählen Sie ein Startdatum und eine Startzeit für Ihre Banner-Campaign. Standardmäßig laufen Banner unbegrenzt. Sie können dies ändern, indem Sie **Endzeit** auswählen und ein Enddatum mit Uhrzeit festlegen.

{% alert tip %}
Wenn alle Nachrichten in Ihrer Campaign ähnlich sein oder denselben Inhalt haben werden, verfassen Sie Ihre Nachricht, bevor Sie weitere Varianten hinzufügen. Anschließend können Sie im Dropdown-Menü **Variante hinzufügen** die Option **Von Variante kopieren** auswählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) mit dem Canvas-Composer.
2. Nachdem Sie Ihr Canvas eingerichtet haben, fügen Sie im Canvas-Builder einen Nachrichtenschritt hinzu. Geben Sie Ihrem Schritt einen eindeutigen und aussagekräftigen Namen.
3. Wählen Sie **Banner** als Ihren Messaging-Kanal.
4. Wählen Sie eine Platzierung für das Banner aus.
5. Legen Sie die Priorität fest. Die [Banner-Priorität]({{site.baseurl}}/user_guide/channels/banners#priority) bestimmt die Reihenfolge, in der Banner angezeigt werden, wenn sie dieselbe Platzierung teilen.
6. Legen Sie eine Ablaufzeit für das Banner fest. Dies kann nach einer bestimmten Dauer nach Verfügbarkeit des Schritts oder zu einem bestimmten Datum und einer bestimmten Uhrzeit sein. Die maximale Ablaufdauer beträgt 31 Tage, nachdem der Schritt für die Nutzer:innen verfügbar wird.

{% endtab %}
{% endtabs %}

### Schritt 3: Ein Banner verfassen {#compose-a-banner}

Wählen Sie als Nächstes, wie Sie mit der Erstellung beginnen möchten:

- **Drag-and-drop-Editor:** Beginnen Sie mit einem leeren Banner und erstellen Sie es visuell mit Blöcken und Zeilen.
- **HTML-Editor:** Beginnen Sie mit einem leeren Banner und arbeiten Sie direkt in HTML.
- **Templates:** Öffnen Sie die Template-Bibliothek und wählen Sie ein Design aus **Braze-Templates** oder **Ihre Templates**. Templates werden im Drag-and-drop-Editor zur Anpassung geöffnet.

![Optionen zur Auswahl des Drag-and-drop-Editors, HTML-Editors oder von Templates für Ihr Banner.]({% image_buster /assets/img/banners/choose_banner_editing_experience.png %})

#### Schritt 3.1: Das Banner gestalten {#step-31-style-the-banner}

{% tabs %}
{% tab Drag-and-drop-Editor %}

Sie können Blöcke und Zeilen per Drag-and-drop in den Canvas-Bereich ziehen, um mit der Erstellung Ihrer Nachricht zu beginnen. Eine Referenz der Banner-Editor-Blöcke und Links zu gemeinsamen Eigenschaftsdetails finden Sie unter [Editor-Blöcke (Banner)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=banners).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Um die Hintergrundeigenschaften, Rahmeneinstellungen und mehr Ihrer Nachricht anzupassen, wählen Sie **Stile**. Wenn Sie nur den Stil eines bestimmten Blocks oder einer bestimmten Zeile anpassen möchten, wählen Sie das Element aus, um Änderungen vorzunehmen.

![Stil-Panel des Banner-Composers.]({% image_buster /assets/img/banners/banner_card_styles.png %})

{% multi_lang_include drag_and_drop/hide_rows_and_blocks_by_device.md channel='banner' %}

{% endtab %}
{% tab HTML-Editor %}

Der HTML-Editor eignet sich am besten für Teams, die bereits eigene HTML-Templates pflegen oder die volle Kontrolle über Markup und Styling haben möchten. Sie können benutzerdefiniertes HTML direkt in den Editor schreiben oder einfügen. Liquid-Personalisierungs-Tags werden vollständig unterstützt, sodass Sie auf Nutzer:innen-Attribute, angepasste Attribute, Katalogartikel und mehr verweisen können.

{% alert tip %}
Brauchen Sie Hilfe beim Erstellen Ihres Banner-HTMLs? Wählen Sie **Ask Operator** im HTML-Editor und beschreiben Sie das gewünschte Banner. [BrazeAI<sup>TM</sup> Operator]({{site.baseurl}}/user_guide/brazeai/operator) generiert HTML, das Sie überprüfen und in den Editor einfügen können. Weitere Informationen finden Sie unter [Nachrichten generieren]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages).
{% endalert %}

Für Klick- und Schließen-Tracking in Ihrem benutzerdefinierten HTML müssen Sie JavaScript-Bridge-Methoden explizit aufrufen. Die vollständige Referenz finden Sie unter [Benutzerdefinierter Code und JavaScript-Bridge für Banner]({{site.baseurl}}/user_guide/channels/banners/custom_code).

{% endtab %}
{% endtabs %}

{% alert note %}
Um Nutzer:innen in verschiedenen Sprachen innerhalb einer einzelnen Banner-Campaign anzusprechen, lesen Sie [Mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).
{% endalert %}

#### Schritt 3.2: Klickverhalten definieren (optional) {#step-32-define-on-click-behavior-optional}

{% tabs %}
{% tab Drag-and-drop-Editor %}

Wenn Nutzer:innen auf einen Link im Banner klicken, können Sie sie tiefer in Ihre App navigieren oder auf eine andere Webseite weiterleiten. Zusätzlich können Sie festlegen, dass ein [angepasstes Attribut oder Event protokolliert wird]({{site.baseurl}}/developer_guide/analytics), wodurch das Profil der Nutzer:innen mit benutzerdefinierten Daten aktualisiert wird, wenn sie auf das Banner klicken. Für granulareres Klick-Tracking weisen Sie jedem interaktiven Element über das Feld **Bezeichner für Berichte** in dessen Eigenschafts-Panel einen benutzerdefinierten Bezeichner zu.

{% alert important %}
{::nomarkdown}
Das Klickverhalten kann überschrieben werden, wenn ein bestimmtes Element (z. B. ein Button, ein Link oder ein Bild des Banners) ein eigenes Klickverhalten hat. Beispiel bei folgenden Klickverhalten:<br><ul><li>Ein Banner hat ein Klickverhalten, das zur Startseite einer Website weiterleitet.</li><li>Ein Bild im Banner hat ein Klickverhalten, das zur Produktseite einer Website weiterleitet.</li></ul>Wenn Nutzer:innen auf das Bild klicken, werden sie zur Produktseite weitergeleitet. Ein Klick auf den umgebenden Bereich im Banner leitet sie jedoch zur Startseite weiter.
{:/}
{% endalert %}

{% endtab %}
{% tab HTML-Editor %}

Im HTML-Editor erfolgt das Klick-Tracking nicht automatisch. Sie müssen `brazeBridge.logClick()` in Ihrem HTML für jedes klickbare Element aufrufen, das Sie tracken möchten. Beispiel:

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

Aktivieren Sie das Kontrollkästchen **Banner kann geschlossen werden** im Abschnitt **Schließen-Verhalten**, um Nutzer:innen das Schließen des Banners zu ermöglichen. Dies ist nützlich, wenn Sie ein zeitlich begrenztes Angebot einem breiten Publikum präsentieren, aber uninteressierten Nutzer:innen das Ausblenden der Nachricht ermöglichen möchten.

Wenn das Schließen aktiviert ist, können Sie den Schließen-Button im Abschnitt **Schließen-Verhalten** anpassen:

| Einstellung | Beschreibung |
|---------|-------------|
| **Buttongröße** | Die Größe des Schließen-Buttons, der auf dem Banner angezeigt wird. |
| **Buttonfarbe** | Die Farbe des Schließen-Buttons. |
| **ARIA-Label** | Das barrierefreie Label für den Schließen-Button, das von Screenreadern verwendet wird. Standardmäßig „Schließen“, wenn leer gelassen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Einstellungen für den Schließen-Button" }

Wenn Nutzer:innen ein Banner schließen, wird es für diese Nutzer:innen nicht erneut angezeigt, auch wenn sie weiterhin den Targeting-Kriterien der Campaign entsprechen.

{% endtab %}
{% tab HTML-Editor %}

Im HTML-Editor wird das Schließen in Ihrem HTML mit `brazeBridge.closeMessage()` gesteuert. Kombinieren Sie es mit `brazeBridge.logClick()`, um die Schließen-Aktion auch als Klick-Event zu tracken. Beispiel:

```html
<a href="#" onclick="brazeBridge.logClick(); brazeBridge.closeMessage();">&#x2715; Close</a>
```

Wenn Nutzer:innen ein Banner auf diese Weise schließen, wird es für diese Nutzer:innen nicht erneut angezeigt, auch wenn sie weiterhin den Targeting-Kriterien der Campaign entsprechen.

Die vollständige JavaScript-Bridge-Referenz finden Sie unter [Benutzerdefinierter Code und JavaScript-Bridge für Banner]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge).

{% endtab %}
{% endtabs %}

#### Schritt 3.4: Benutzerdefinierte Eigenschaften hinzufügen (optional) {#custom-properties}

Sie können einem Banner benutzerdefinierte Eigenschaften hinzufügen, um strukturierte Metadaten wie Strings oder JSON-Objekte anzuhängen. Diese Eigenschaften beeinflussen nicht die Darstellung des Banners, können aber [über das Braze SDK abgerufen werden]({{site.baseurl}}/developer_guide/banners/placements), um das Verhalten oder Erscheinungsbild Ihrer App zu ändern. Sie könnten zum Beispiel:

{% multi_lang_include banners/metadata_use_cases.md %}

Benutzerdefinierte Eigenschaften funktionieren im Drag-and-drop-Editor und im HTML-Editor identisch. Um eine benutzerdefinierte Eigenschaft hinzuzufügen, wählen Sie **Einstellungen** > **Eigenschaften** > **Eigenschaft hinzufügen**.

![Die Eigenschaftsseite mit der Option, die erste benutzerdefinierte Eigenschaft zu einer Banner-Campaign hinzuzufügen.]({% image_buster /assets/img/banners/add_property.png %})

Füllen Sie für jede Eigenschaft, die Sie hinzufügen möchten, folgende Felder aus:

| Feld | Beschreibung | Beispiel |
|-------|-------------|---------|
| Eigenschaftstyp | Der Datentyp für die Eigenschaft. Unterstützte Typen sind String, Boolean, Nummer, Zeitstempel, Bild-URL und JSON-Objekt. | String |
| Eigenschaftsschlüssel | Der eindeutige Bezeichner für die Eigenschaft. Dieser Schlüssel wird im SDK verwendet, um auf die Eigenschaft zuzugreifen. | `color` |
| Wert | Der der Eigenschaft zugewiesene Wert. Muss dem ausgewählten Eigenschaftstyp entsprechen. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 3.4: Benutzerdefinierte Eigenschaften hinzufügen (optional)" }

Wenn Sie fertig sind, wählen Sie **Fertig**.

![Die Eigenschaftsseite mit einer String-Eigenschaft mit dem Schlüssel „color“ und dem Wert #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

#### Schritt 3.5: Mit Connected Content personalisieren (optional) {#step-35-personalize-with-connected-content-optional}

{% multi_lang_include alerts/early_access_beta_alert.md feature='Connected Content for Banners' %}

Da Banner während einer Session-Aktualisierung inline gerendert werden, funktioniert Connected Content in diesem Kanal anders als in anderen Kanälen:

- Es werden nur GET-Anfragen unterstützt.
- Alle Platzierungen in einer einzelnen Aktualisierung (bis zu 10) teilen sich ein Rendering-Budget von etwa zwei Sekunden. Wenn ein Aufruf langsam ist, ein Timeout auftritt oder das Budget überschritten wird, wird das Connected-Content-Ergebnis für diese Platzierung als null behandelt. Banner führen keine Wiederholungsversuche durch.

Für optimale Ergebnisse:

- Halten Sie Ihre Endpunkte schnell und [cachen Sie Antworten]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) wann immer möglich.
- Begrenzen Sie die Anzahl eindeutiger Connected-Content-URLs über die Platzierungen hinweg, die gemeinsam gerendert werden.
- Vermeiden Sie verkettete Aufrufe, bei denen eine Connected-Content-Antwort die URL für den nächsten Aufruf bestimmt. Jeder zusätzliche Aufruf belastet das gemeinsame Budget.
- Verwenden Sie Liquid-Schutzanweisungen oder den [`default`-Filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values), um null-Ergebnisse zu behandeln und leere Banner zu vermeiden.

### Schritt 4: Den Rest Ihrer Campaign oder Ihres Canvas erstellen {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Banner-Priorität festlegen (optional) {#set-banner-priority-optional}

Die [Banner-Priorität]({{site.baseurl}}/user_guide/channels/banners#priority) bestimmt die Reihenfolge, in der Banner angezeigt werden, wenn sie dieselbe Platzierung teilen. So legen Sie die Priorität manuell fest:

1. Wählen Sie **Set exact priority**.
2. Ziehen Sie die Campaigns per Drag-and-drop in die richtige Reihenfolge.
3. Wählen Sie **Apply Sort**.

{% alert tip %}
Wenn Sie mehrere Banner-Campaigns mit derselben Platzierungs-ID haben, empfehlen wir die Verwendung des Drag-and-drop-Prioritätssortierers, um die genaue Priorität festzulegen.
{% endalert %}

#### Erneute Berechtigung konfigurieren (optional) {#re-eligibility}

Standardmäßig sind Nutzer:innen, die ein Banner schließen, nie erneut für diese Campaign berechtigt. Um geschlossenen Nutzer:innen das Banner erneut anzuzeigen, gehen Sie zum Schritt **Zustellungskontrollen** und wählen Sie **Nutzer:innen erlauben, erneut berechtigt zu werden, die Campaign zu erhalten**. Wenn aktiviert, legen Sie ein Abklingfenster in Minuten, Stunden, Tagen oder Wochen fest.

Der Countdown beginnt, wenn die Nutzer:innen das Banner schließen. Nach Ablauf des Fensters sind die Nutzer:innen automatisch erneut berechtigt — ein Neustart der Campaign ist nicht erforderlich. Die erneute Berechtigung wird pro Nutzer:in und pro Campaign verfolgt.

#### Ihre Zielgruppe auswählen {#choose-your-audience}

1. Wählen Sie unter **Zielgruppen** Segmente oder Filter aus, um Ihre Zielgruppe einzugrenzen. Sie erhalten automatisch eine Vorschau der ungefähren Segment-Population. Die genaue Segment-Zugehörigkeit wird vor dem Versand der Nachricht berechnet.

{% multi_lang_include audience/target_audiences.md %}

{:start="2"}
2. Weisen Sie unter **Konversionen zuweisen** Konversions-Events zu und verfolgen Sie, wie oft Nutzer:innen bestimmte Aktionen nach Erhalt einer Campaign ausführen, mit einem Fenster von bis zu 30 Tagen, um die Aktion als Konversion zu zählen.

#### Konversions-Events auswählen {#choose-conversion-events}

Mit Braze können Sie [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) verfolgen — wie oft Nutzer:innen bestimmte Aktionen nach Erhalt einer Campaign ausführen. Sie haben die Möglichkeit, ein Fenster von bis zu 30 Tagen festzulegen, in dem eine Konversion gezählt wird, wenn die Nutzer:innen die angegebene Aktion ausführen.

{% endtab %}

{% tab Canvas %}

Wenn Sie es noch nicht getan haben, vervollständigen Sie die verbleibenden Abschnitte Ihrer Canvas-Komponente. Weitere Informationen zum Erstellen des restlichen Canvas, einschließlich multivariater Tests und [Optimierung mit BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai), finden Sie unter [Ihr Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas).

Um die erneute Berechtigung für Canvas-Banner-Schritte zu steuern, verwenden Sie die Canvas-Wiedereintrittseinstellungen. Weitere Informationen finden Sie unter [Erneute Berechtigung für Campaigns und Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).

{% endtab %}
{% endtabs %}

### Schritt 5: Ihre Nachricht testen (optional) {#step-5-test-your-message-optional}

{% multi_lang_include banners/testing.md page="campaigns" %}

### Schritt 6: Überprüfen und bereitstellen {#step-6-review-and-deploy}

Nachdem Sie Ihre Campaign oder Ihr Canvas fertig erstellt haben, überprüfen Sie die Details, [testen Sie sie]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) und senden Sie sie, wenn Sie bereit sind.