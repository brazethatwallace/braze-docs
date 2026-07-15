## Editor-Blöcke im Präferenzzentrum {#preference-center-editor-blocks}

Ziehen Sie Blöcke aus dem Abschnitt **Build** in eine Zeile im Drag-and-Drop-Editor des Präferenzzentrums. Jeder Block hat eigene Einstellungen; das rechte Panel wechselt zu den Eigenschaften oder dem Styling des ausgewählten Elements.

Bevor Sie Blöcke bearbeiten, fügen Sie Abo-Gruppen hinzu und konfigurieren Sie den **Smart Block** für Abos (siehe folgenden Abschnitt). Den vollständigen Einrichtungsablauf finden Sie unter [Ein E-Mail-Präferenzzentrum mit Drag-and-Drop erstellen]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center).

### Titel und Absatz {#title-and-paragraph}

Fügt eine Überschrift oder Fließtext mit Rich-Text-Optionen hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Button

Fügt einen klickbaren Button hinzu (zum Beispiel **Speichern** oder Navigation).

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

### Bild {#image}

Zeigt ein Bild aus der [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) oder von einer URL an.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

### Abstandshalter {#spacer}

Fügt vertikalen Abstand zwischen Blöcken hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Abo-Gruppen (Smart Block) {#subscription-groups-smart-block}

Fügt einen Template-Block hinzu, der Abo-Gruppen, optionale Steuerelemente für **Alle abonnieren** / **Alle abmelden** sowie Beschreibungen auflistet. Konfigurieren Sie ihn, nachdem Sie Gruppen im Workflow des Präferenzzentrums hinzugefügt haben.

Nachdem Sie [Abo-Gruppen hinzugefügt]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#step-3-add-subscription-groups-to-the-preference-center) haben, wählen Sie den Smart Block im Canvas aus, um:

- Abo-Gruppen neu anzuordnen
- Gruppen hinzuzufügen oder zu entfernen
- Beschreibungen hinzuzufügen oder zu entfernen
- **Alle abonnieren** und **Alle abmelden** für die Gruppen in diesem Block umzuschalten

Das Steuerelement **Alle abmelden** am unteren Rand des Standard-Templates ist erforderlich und führt eine [globale Abmeldung]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) von E-Mails durch.

## Wissenswertes {#things-to-know}

- **Gemeinsame Stile:** Sie können seitenweite Standardwerte unter **Common Styles** festlegen, bevor Sie einzelne Blöcke anpassen. Weitere Informationen finden Sie unter [Das Präferenzzentrum mit dem Drag-and-Drop-Editor anpassen]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#step-4-customize-the-preference-center-using-the-drag-and-drop-editor).
- **Bestätigungsseite:** Wechseln Sie oben im Editor zu **Confirmation Page**, um das Erlebnis nach dem Speichern mit denselben Blocktypen zu gestalten.