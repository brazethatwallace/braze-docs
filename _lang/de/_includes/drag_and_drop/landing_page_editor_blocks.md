## Editor-Blöcke für Landing-Pages {#landing-page-editor-blocks}

Editor-Blöcke für Landing-Pages befinden sich im Abschnitt **Erstellen** des **Drag-and-Drop-Editors** unter **Zeilen** und Blockkategorien. Ziehen Sie einen Block in eine Zeilenspalte – er passt sich automatisch an die Spaltenbreite an. Wählen Sie einen Block aus, um seine Einstellungen im Eigenschaftenpanel auf der rechten Seite zu bearbeiten.

Weitere Informationen zum Erstellen und Veröffentlichen von Landing-Pages finden Sie unter [Landing-Pages erstellen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/).

### Titel und Absatz {#title-and-paragraph}

Fügt Überschriften- oder Fließtext hinzu. Nützlich zum Strukturieren von Abschnitten und zur Verbesserung der Lesbarkeit.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Button

Fügt ein klickbares Element für Aktionen wie das Öffnen eines Links oder das Absenden eines Formulars hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Verhalten bei Klick {#on-click-behavior}

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

{% alert important %}
Wenn Sie einen Button mit **Submit form when button is clicked** konfigurieren und eine Web-URL in einem neuen Tab öffnen, blockiert iOS Safari möglicherweise die Navigation. Öffnen Sie die URL nach dem Absenden im selben Tab, wenn Sie Formulare absenden. Weitere Informationen finden Sie unter [Landing-Pages erstellen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/).
{% endalert %}

### Optionsfeld {#radio-button}

Fügt eine Liste von Optionen hinzu, aus der Nutzer:innen eine auswählen können. Verwenden Sie das Eigenschaftenpanel, um die verfügbaren Optionen und das angepasste Attribut zu konfigurieren, das den ausgewählten Wert empfängt. Das Nutzerprofil protokolliert den ausgewählten Wert als [angepasstes String-Attribut]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/), wenn das Formular abgesendet wird. Angepasste Attribute mit anderen Datentypen werden nicht im Nutzerprofil gespeichert.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### Bild {#image}

Zeigt ein Bild aus einem Upload oder einer externen URL an.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### Verhalten bei Klick

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Link

Fügt einen Hyperlink hinzu, den Nutzer:innen auswählen können, um zu einer URL zu gelangen. Kann in Text eingebettet oder eigenständig stehen.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Verhalten bei Klick

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Abstandshalter {#spacer}

Fügt vertikalen Abstand zwischen Elementen hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Benutzerdefinierter Code {#custom-code}

Fügt benutzerdefiniertes HTML, CSS oder JavaScript für erweiterte Anpassungen ein, z. B. [Google Tag Manager]({{site.baseurl}}/user_guide/messaging/landing_pages/#google-tag-manager).

| Eigenschaft | Beschreibung |
| --- | --- |
| Benutzerdefinierter Code | Ermöglicht das Hinzufügen, Bearbeiten oder Löschen von HTML, CSS und JavaScript. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Benutzerdefinierter Code" }

<!-- Countdown timer is not yet released. Uncomment when available.
### Countdown timer

Displays a countdown to a date and time you set. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager.

After you add a **Countdown timer** block, use the properties panel to set the target date and time, labels, and styling.
-->

### E-Mail-Erfassung {#email-capture}

Fügt ein Formularfeld für E-Mail-Adressen hinzu. Beim Absenden wird die Adresse im Braze-Profil der Nutzer:innen gespeichert.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Telefonnummer-Erfassung {#phone-capture}

Fügt ein Formularfeld für Telefonnummern hinzu. Beim Absenden werden die Nutzer:innen für Ihre ausgewählte [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/)- oder [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/)-Abo-Gruppe angemeldet.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Eingabefeld {#input-field}

Fügt ein Formularfeld für Standardattribute (z. B. Vor- oder Nachname) oder einen angepassten String-Attributwert hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### Dropdown

Eine vordefinierte Liste von Elementen, aus der Nutzer:innen eines auswählen. Sie können Werte angepassten String-Attributen zuordnen.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### Kontrollkästchen {#checkbox}

Wenn aktiviert, wird das [angepasste boolesche Attribut]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types) des Blocks auf `true` gesetzt; wenn deaktiviert, auf `false`.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Kontrollkästchengruppe {#checkbox-group}

Nutzer:innen wählen mehrere Optionen aus; die Werte werden in einem definierten [angepassten Array-Attribut]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types) gesetzt oder angehängt.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Langer Text {#long-text}

Mehrzeiliges Textfeld für umfrageähnliche Abläufe. Wenn Sie diesen Block nicht sehen, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) oder Ihren Customer-Success-Manager. Dieser Block ist für Standard-Landing-Pages nicht verfügbar.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager.
-->

## Wissenswertes {#things-to-know}

- **Video:** Der Standard-Composer enthält keinen dedizierten Video-Block. Verwenden Sie **Benutzerdefinierter Code**, um bei Bedarf einen Player einzubetten. Weitere Informationen finden Sie unter [Landing-Pages]({{site.baseurl}}/user_guide/messaging/landing_pages/).