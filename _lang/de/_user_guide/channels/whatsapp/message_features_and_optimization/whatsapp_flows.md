---
nav_title: WhatsApp Flows
article_title: WhatsApp Flows
page_order: 3
description: "Dieser Referenzartikel beschreibt die Schritte zum Erstellen und Aufbauen einer WhatsApp-Flows-Nachricht."
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# WhatsApp Flows

> WhatsApp Flows ist eine Erweiterung des bestehenden WhatsApp-Kanals, mit der Sie interaktive und dynamische Messaging-Erlebnisse erstellen können. Diese Seite bietet eine Schritt-für-Schritt-Anleitung zur Verwendung von WhatsApp Flows.

## WhatsApp Flows einrichten {#setting-up-whatsapp-flows}

1. Melden Sie sich bei Ihrem Meta-Konto an.
2. Erstellen Sie Flows von einem der beiden Hauptstandorte aus:
    - **Account tools:** Gehen Sie zum Tab **Flows**, um die Flow-ID anzuzeigen und einen neuen Flow zu erstellen.
    - **Manage templates:** Dies ist die empfohlene Methode zum Erstellen von Flows. Hier können Sie Templates generieren und während des Template-Erstellungsprozesses eine Flow-Option auswählen.

![WhatsApp Manager mit einer Seite zum Erstellen eines Flows-Templates.]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{: start="3"}
3. Wählen Sie einen vorhandenen Flow aus oder erstellen Sie einen neuen. Beim Erstellen eines Flows können Sie zwischen zwei Optionen wählen:
  - **Custom Form:** Für spezifische Anforderungen
  - **Pre-designed Elements:** Für eine schnellere Einrichtung

## WhatsApp-Flow-Nachrichten und -Antworten konfigurieren {#configuring-whatsapp-flow-messages-and-responses}

{% tabs local %}
{% tab Template-Nachricht %}

1. Erstellen Sie in einem Braze-Canvas einen WhatsApp-Nachrichtenschritt, der das Template mit dem entsprechenden Flow verwendet.
2. Fahren Sie mit der Erstellung Ihres Templates fort. Fügen Sie bei Bedarf Medien, variable Inhalte oder beides zu Ihrer Nachricht hinzu. Ihre Flow-Auswahl wurde beim Erstellen des Templates getroffen, sodass keine zusätzlichen Informationen für das Flow-Erlebnis erforderlich sind.

![WhatsApp-Nachrichten-Editor mit einem WhatsApp-Flow-Template.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Antwortnachricht %}

1. Erstellen Sie in einem Braze-Canvas einen WhatsApp-Nachrichtenschritt, der eine Antwortnachricht und ein Flow-Nachrichtenlayout verwendet.

![Ein Nachrichtenschritt für einen WhatsApp-Antwortnachrichtentyp und ein Flow-Nachrichtenlayout.]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2. Wählen Sie den entsprechenden Flow aus und fahren Sie dann mit der Erstellung Ihrer Nachricht fort.

![Ein Flow-Nachrichten-Antwort-Editor mit einem erweiterten Dropdown zur Auswahl eines Flows.]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Flow-Vorschau {#preview-flow}

Bevor Sie ein Canvas mit einem Flow starten, können Sie **Preview Flow** auswählen, um den Flow direkt in Braze in der Vorschau anzuzeigen und zu bestätigen, dass er sich wie erwartet verhält. Sie können auch mit dem Flow in der Vorschau interagieren, um zu erleben, wie Nutzer:innen durch den Flow navigieren würden, und dann Anpassungen in Echtzeit vornehmen. Wenn ein Flow mehrere Seiten enthält, können Sie mit jeder Seite interagieren.

![Vorschaufenster mit einem Formular, in dem Nutzer:innen die Registrierung abschließen können.]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## Die vollständige Flow-Antwort speichern {#full-flow}

Wenn Sie eine WhatsApp-Flow-Nachricht in ein Braze-Canvas oder eine Campaign einbinden, möchten Sie möglicherweise bestimmte Informationen erfassen und nutzen, die Nutzer:innen über den Flow übermitteln. Braze benötigt zusätzliche Informationen über die Struktur der Nutzerantwort, insbesondere die erwartete Form der JSON-Antwort, um das erforderliche Schema für verschachtelte angepasste Attribute (NCA) zu generieren.

### 1. Schritt: Das angepasste Flow-Attribut generieren {#step-1-generate-the-flow-custom-attribute}

{% tabs local %}
{% tab Empfohlene Methode %}

Der einfachste Weg, Braze die Informationen über die Antwortstruktur zu geben, besteht darin, die Flow-Antwort als angepasstes Attribut zu speichern und einen Testversand durchzuführen.

#### Einen Flow verwenden, der noch nicht in Braze verwendet wurde {#using-a-flow-that-hasnt-been-used-in-braze}

Wenn Sie einen Flow verwenden, der zuvor noch nicht in Braze verwendet wurde, sehen Sie beim Anzeigen des Abschnitts **Flow Custom Attribute** unter **Compose Messages** möglicherweise keine Informationen. Das bedeutet, dass das Schema noch nicht generiert wurde.

![Meta-Flow-Abschnitt mit einer Option zum Anzeigen des angepassten Flow-Attributs.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute.png %}){: style="max-width:70%;"}

Um dies zu beheben, gehen Sie wie folgt vor:

1. Schließen Sie die Einrichtung Ihres WhatsApp-Nachrichtenschritts ab.
2. Stellen Sie sicher, dass Sie **Save Flow responses as a custom attribute** aktiviert haben.
3. Senden Sie sich selbst eine Testnachricht und durchlaufen Sie den Flow als Nutzer:in.

Jetzt hat Braze die Form der Flow-Antwort-JSON und kann das angepasste Attribut generieren.

{% endtab %}
{% tab Alternative Methoden %}

Verwenden Sie den erweiterten JSON-Editor, um Attribute aus der Flow-Antwort in angepassten Attributen zu speichern, oder verwenden Sie ein mehrstufiges Canvas, um die Antwort in einem verschachtelten angepassten Attribut zu speichern.

{% subtabs %}
{% subtab Erweiterter JSON-Editor %}

Geben Sie im erweiterten JSON-Editor {% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %} ein, wobei „flow_1“ das angepasste Attribut ist, in dem der Flow gespeichert werden soll.

![Nutzeraktualisierungsschritt mit einem erweiterten JSON-Editor.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endsubtab %}
{% subtab UI-Editor %}

1. Stellen Sie sicher, dass Sie bereits ein angepasstes Attribut mit dem Objektdatentyp (in diesem Beispiel „flow_1“) in Ihren Workspace-Dateneinstellungen erstellt haben.
2. Verwenden Sie im UI-Editor das Liquid {% raw %}`{{whats_app.${inbound_flow_response}}}`{% endraw %}, um das angepasste Attribut zu befüllen und die gesamte Flow-Antwort der Nutzer:innen darin zu speichern. Sie müssen den Schlüsselwert als {% raw %}`{{whats_app.${inbound_flow_response}}}`{% endraw %} befüllen, bevor Sie das von Ihnen erstellte angepasste Attribut auswählen.

![Nutzeraktualisierungsschritt, der den UI-Editor verwendet.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Nachdem Braze eine Flow-Antwort erhalten hat, wird das verschachtelte angepasste Attribut mit der vorgegebenen Benennung im Nutzerprofil gespeichert. Dieses angepasste Attribut kann beim Erstellen von Canvases abgerufen werden.

![Ein Fenster, das den Inhalt eines angepassten Attributs „flow_1“ anzeigt.]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 2. Schritt: Die gespeicherte Flow-Antwort anzeigen {#step-2-view-the-saved-flow-response}

Wenn der Flow abgeschlossen ist, erstellt Braze automatisch ein angepasstes Flow-Attribut mit einem Namen, der auf der Flow-ID basiert. Sie können dann zum Nutzerprofil gehen, um die gespeicherte Flow-Antwort als verschachteltes Objekt im Abschnitt **Custom Attributes** anzuzeigen.

Nachdem das Schema generiert wurde, zeigt der Abschnitt **Custom Attribute** des Flows die erwartete Struktur an, einschließlich der erwarteten Datentypen für jede Antwort (zum Beispiel „String“ oder „String Array“).

![Detailfenster für angepasste Flow-Attribute mit Schema-Dropdown.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute_details.png %}){: style="max-width:80%;"}

### Hinweise {#considerations}

- **Vorhandene Attribute:** Wenn ein angepasstes Attribut für einen bestimmten Flow bereits generiert wurde, wird der Flow mit den verfügbaren Attributinformationen geladen. In diesen Fällen müssen Sie keine Testnachricht senden, um das Schema zu generieren, da Braze die erwarteten Antwortnachrichten bereits kennt.
- **Flow-Änderungen:** Wenn Sie nach der Schema-Generierung Änderungen am Flow vornehmen, müssen Sie eine zusätzliche Testnachricht senden, damit Braze erkennen kann, dass sich die Form der Flow-Antwort geändert hat, und die Attributstruktur entsprechend anpassen kann. Diese Aktion ist auf einmal alle 24 Stunden begrenzt.
- **Konsistenz:** Das generierte angepasste Flow-Attribut ist konsistent und ist dasselbe Attribut für diesen spezifischen Flow, unabhängig davon, in welchem Canvas es verwendet wird.
- **Manuelle Option:** Sie müssen das Kontrollkästchen **Save Flow responses as a custom attribute** nicht aktivieren. Sie können das angepasste Attribut manuell generieren, indem Sie [bestimmte Felder aus Flow-Antworten in einem bestimmten angepassten Attribut speichern](#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute), wodurch doppelte Nutzerschritte vermieden werden.

## Bestimmte Felder aus Flow-Antworten in einem bestimmten angepassten Attribut speichern {#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute}

### 1. Schritt: Einen Aktions-Pfad erstellen {#step-1-create-an-action-path}

Erstellen Sie einen [Aktions-Pfad]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)-Canvas-Schritt oder eine aktionsbasierte Campaign. Wählen Sie einen **Send a WhatsApp inbound message**-Trigger und die Bedingung **Responded to Flow** aus, und wählen Sie dann den relevanten Flow oder **Any Flow** aus.

![Ein Trigger für Nutzer:innen, die eine eingehende WhatsApp-Nachricht gesendet und auf einen beliebigen Flow geantwortet haben.]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### 2. Schritt: Felder aus Flow-Antworten extrahieren {#step-2-extract-fields-from-flow-responses}

Sie können verschachtelte angepasste Attribute oder den Liquid-Tag `json_parse` verwenden, um bestimmte Felder aus Flow-Antworten zu extrahieren.

{% tabs %}
{% tab Verschachtelte angepasste Attribute %}

Um bestimmte Teile der Flow-Antwort von Nutzer:innen zu speichern, führen Sie alle Schritte unter [Die vollständige Flow-Antwort speichern](#full-flow) durch, **einschließlich des Startens des Canvas**. Das Canvas muss gestartet werden, um das verschachtelte angepasste Attribut zu erstellen, auf das Sie verweisen werden. Nachdem Sie das Canvas gestartet und einen Flow abgeschlossen haben, führen Sie die folgenden Schritte aus:

1. Erstellen Sie einen nachfolgenden Nutzeraktualisierungsschritt, der den UI-Editor verwendet.
2. Wählen Sie **Add Personalization** aus, dann wählen Sie **Nested Custom Attribute** und das entsprechende übergeordnete Attribut, in dem der Flow gespeichert ist.

![Nutzeraktualisierungsschritt mit einer Personalisierung für verschachtelte angepasste Attribute.]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3. Wählen Sie das Schlüsselattribut aus, das Sie speichern möchten, und fügen Sie das Liquid in das Feld **Key Value** ein.

![Fenster für „flow_1“ mit auswählbaren Attributen.]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4. Wählen Sie das Attribut aus, in dem Sie es speichern möchten.
5. Senden Sie eine Testnachricht, um den Flow zu testen.

{% endtab %}
{% tab Parse-Funktion %}

Verwenden Sie den Liquid-Tag `json_parse`, um bestimmte Antworten aus dem Flow zu extrahieren. Sie können beispielsweise das Flow-Token und ausgewählte Optionen abrufen, um eine Folgenachricht anzupassen.

Wählen Sie im UI-Editor Folgendes aus:

- **Attribute Name:** IHR_ANGEPASSTES_ATTRIBUT (in diesem Beispiel: „First_name“)
- **Action:** Update
- **Key Value:** {% raw %} `{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}`{% endraw %}

![WhatsApp-Nachrichten-Editor mit einer „Add Personalization“-Komponente zum Einfügen einer WhatsApp-Eigenschaften-Personalisierung mit dem angepassten Attribut `inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/parsed_json.png %})

Wenn Sie bereit sind, senden Sie eine Testnachricht, um den Flow zu testen. Starten Sie dann das Canvas!

{% endtab %}
{% endtabs %}

{% alert note %}
Eine neue WhatsApp-Nachricht „löscht“ die Fähigkeit des Canvas, die Liquid-Flow-Antwort zu verwenden (und wiederzuverwenden). Stellen Sie daher sicher, dass Folgenachrichten nach allen Nutzeraktualisierungsschritten, Webhooks oder anderen Schritten stehen, die die Liquid-Flow-Antwort verwenden.
{% endalert %}

## Einen Flow-Personalisierungs-Tag hinzufügen {#adding-a-flow-personalization-tag}

Um die Flow-Antwort über Liquid mit [unterstützten Personalisierungs-Tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) zu verwenden, führen Sie die folgenden Schritte aus:

1. Wählen Sie beim Verfassen Ihrer WhatsApp-Nachricht <i class="fas fa-plus-circle" aria-label="Personalisierung hinzufügen"></i> **Add Personalization** aus, um das Fenster **Add Personalization** zu öffnen.
2. Wählen Sie **WhatsApp Properties** als Personalisierungstyp und **inbound_flow_response** als angepasstes Attribut aus. Dies kann verwendet werden, um Informationen in Nutzerprofilen zu speichern, sie in Nachrichten einzubinden oder an andere Dienste wie Webhooks weiterzuleiten.

![WhatsApp-Nachrichten-Editor mit einer „Add Personalization“-Komponente zum Einfügen einer WhatsApp-Eigenschaften-Personalisierung mit dem angepassten Attribut „inbound_flow_response“.]({% image_buster /assets/img/whatsapp/flows/inbound_flow_response.png %}){: style="max-width:80%;"}

Bei Fragen oder für weitere Unterstützung kontaktieren Sie den [Support]({{site.baseurl}}/braze_support).