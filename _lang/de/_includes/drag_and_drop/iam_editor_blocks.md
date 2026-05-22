## Editor-Blöcke für In-App-Nachrichten {#in-app-message-editor-blocks}

Editor-Blöcke befinden sich im Abschnitt **Build** für In-App-Nachrichten. Ziehen Sie einen Block in eine Spalte – er passt sich automatisch an die Spaltenbreite an. Wählen Sie einen Block aus, um seine Einstellungen im rechten Panel zu bearbeiten.

Weitere Informationen zum Erstellen von In-App-Nachrichten im **Drag-and-Drop-Editor** finden Sie unter [In-App-Nachricht per Drag-and-Drop erstellen]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/).

### Titel und Absatz {#title-and-paragraph}

Fügt Titel- oder Absatztext in die Nachricht ein.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Button

Fügt einen Standard-Button mit konfigurierbarem Styling, Links und Analytics hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### On-Click-Verhalten {#on-click-behavior}

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

### Radio-Button

Fügt eine Liste von Optionen hinzu, aus der Nutzer:innen eine auswählen können. Bei der Übermittlung protokolliert das Nutzerprofil das zugehörige [angepasste Attribut]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/), das ein String sein muss, um gespeichert zu werden. Angepasste Attribute mit anderen Datentypen werden nicht im Nutzerprofil gespeichert.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### Bild {#image}

Fügt ein Bild aus der [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/) ein.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

Informationen zu Bildspezifikationen finden Sie in unseren [Bildspezifikationen für In-App-Nachrichten]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications/#in-app-messages).

#### On-Click-Verhalten

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Link

Fügt einen Hyperlink ein, auf den Nutzer:innen klicken können, um zu einer bestimmten URL zu navigieren. Kann in Text eingebettet oder eigenständig verwendet werden.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### On-Click-Verhalten

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Spacer

Fügt Leerraum oder Padding zwischen anderen Blöcken hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Angepasster Code {#custom-code}

Fügt angepasstes HTML, CSS oder JavaScript für erweiterte Anpassungen ein.

| Eigenschaft | Beschreibung |
| --- | --- |
| Angepasster Code | Ermöglicht es Ihnen, HTML, CSS und JavaScript für eine In-App-Nachricht hinzuzufügen, zu bearbeiten oder zu löschen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Angepasster Code" }

### Telefonerfassung {#phone-capture}

Fügt ein Formularfeld für Telefonnummern ein. Nach der Übermittlung wird der/die Nutzer:in in die [SMS-]({{site.baseurl}}/sms_rcs_subscription_groups/) oder [WhatsApp-Abo-Gruppe]({{site.baseurl}}/whatsapp_subscription_groups/) aufgenommen.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### E-Mail-Erfassung {#email-capture}

Fügt ein Formularfeld für E-Mail-Adressen ein. Nach der Übermittlung wird die E-Mail-Adresse dem Nutzerprofil in Braze hinzugefügt.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Kurztext {#short-text}

Fügt ein Formularfeld ein, das Standardattribute (wie Vor- und Nachname) oder einen angepassten Attribut-String Ihrer Wahl unterstützt.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### Dropdown

Fügt ein Dropdown-Menü mit einer vordefinierten Liste von Elementen ein, aus der Nutzer:innen eines auswählen können. Sie können der Liste beliebige angepasste Attribut-Strings hinzufügen.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### Kontrollkästchen {#checkbox}

Fügt ein Kontrollkästchen ein. Wenn der/die Nutzer:in das Kästchen markiert, wird das [angepasste boolesche Attribut]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types) des Blocks auf `true` gesetzt. Wenn es nicht markiert ist, wird das Attribut auf `false` gesetzt.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Kontrollkästchen-Gruppe {#checkbox-group}

Nutzer:innen können aus mehreren vorgegebenen Optionen auswählen. Die Werte werden festgelegt oder zu einem definierten [angepassten Array-Attribut]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types) hinzugefügt.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Langtext {#long-text}

Mehrzeiliges Textfeld für umfrageähnliche Abläufe. Wenn Sie diesen Block nicht sehen, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) oder Ihren Customer-Success-Manager.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager.
-->

## Wissenswertes {#things-to-know}

- **Video:** Der Standard-Composer enthält keinen dedizierten Video-Block. Verwenden Sie **Angepasster Code**, um bei Bedarf einen Player einzubetten. Weitere Informationen finden Sie unter [In-App-Nachrichten: Häufig gestellte Fragen]({{site.baseurl}}/user_guide/channels/in_app_messages/faq/).