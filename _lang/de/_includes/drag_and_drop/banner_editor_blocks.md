## Editor-Blöcke für Banner {#banner-editor-blocks}

Ziehen Sie im Banner-Composer Zeilen und Blöcke aus dem Abschnitt **Build** auf die Arbeitsfläche, um Ihre Nachricht zu gestalten. Wählen Sie **Styles** aus, um das Styling auf Seitenebene anzupassen, oder wählen Sie einen Block oder eine Zeile aus, um deren Eigenschaften im Seitenpanel zu bearbeiten.

Den vollständigen Ablauf zur Banner-Erstellung finden Sie unter [Ein Banner erstellen]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#compose-a-banner).

Der Banner-Composer bietet dieselben Layout-Blöcke wie andere Drag-and-drop-Oberflächen, jedoch nicht den vollständigen Satz an Formularblöcken (z. B. keine Optionsfeld-, Kurztext-, Dropdown- oder Kontrollkästchen-Blöcke). Sie können **Phone capture**- und **Email capture**-Blöcke hinzufügen; pro Nachricht ist nur **ein** Phone-capture- und **ein** Email-capture-Block zulässig.

### Titel und Absatz {#title-and-paragraph}

Fügt Überschriften- oder Fließtext mit Rich-Text-Optionen hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Button

Fügt einen klickbaren Button hinzu. Links und Analytics-Optionen können im Eigenschaftenpanel festgelegt werden.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Klickverhalten {#on-click-behavior}

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

Weitere Informationen finden Sie unter [Klickverhalten definieren]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#step-32-define-on-click-behavior-optional) im Banner-Artikel.

### Bild {#image}

Zeigt ein Bild von einer gehosteten URL an. Anzeigeoptionen können im Eigenschaftenpanel konfiguriert werden.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### Klickverhalten

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Link

Fügt einen Hyperlink ein, den Nutzer:innen auswählen können.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Klickverhalten

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Abstandshalter {#spacer}

Fügt vertikalen Abstand zwischen Blöcken hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Benutzerdefinierter Code {#custom-code}

Fügt benutzerdefiniertes HTML für erweiterte Layouts oder eingebettete Inhalte (z. B. Video) ein. Klicks innerhalb von benutzerdefiniertem HTML werden nicht getrackt, es sei denn, Sie rufen `brazeBridge.logClick()` auf – siehe [Benutzerdefinierter Code und JavaScript-Bridge für Banner]({{site.baseurl}}/user_guide/channels/banners/custom_code/).

| Eigenschaft | Beschreibung |
| --- | --- |
| Benutzerdefinierter Code | HTML (und zugehörige Assets) für das Banner hinzufügen oder bearbeiten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Telefonnummernerfassung {#phone-capture}

Erfasst eine Telefonnummer. Beim Absenden werden die Nutzer:innen in Ihre ausgewählte [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/)- oder [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/)-Abo-Gruppe eingetragen. Nur eine pro Banner.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### E-Mail-Erfassung {#email-capture}

Erfasst eine E-Mail-Adresse und fügt sie beim Absenden dem Braze-Profil der Nutzer:innen hinzu. Nur eine pro Banner.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Langer Text {#long-text}

Mehrzeiliges Textfeld für umfrageähnliche Abläufe. Wenn Sie diesen Block nicht sehen, kontaktieren Sie den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) oder Ihren Braze geschäftskunden-Success-Manager.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Gespeicherte Zeile {#saved-row}

Fügt eine wiederverwendbare Zeile ein, die Sie zuvor als Drag-and-drop-Content-Block gespeichert haben. Gespeicherte Zeilen sind **nicht verknüpft** mit dem ursprünglichen Content Block – wenn das Original aktualisiert wird, müssen Sie es erneut in den Editor ziehen, um die neueste Version zu erhalten. Weitere Informationen finden Sie unter [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). Wenn Sie **Gespeicherte Zeile** unter **Zeilen** nicht sehen, kontaktieren Sie den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) oder Ihren Braze geschäftskunden-Success-Manager.
-->

## Wissenswertes {#things-to-know}

- **Video:** Der Standard-Composer enthält keinen dedizierten Video-Block. Verwenden Sie **Benutzerdefinierter Code**, um bei Bedarf einen Player einzubetten. Weitere Informationen finden Sie unter [Banner: Häufig gestellte Fragen]({{site.baseurl}}/user_guide/channels/banners/faq/).
- **Liquid:** Die meisten Liquid-Funktionen werden unterstützt; es gibt Ausnahmen wie Katalog-Rerender-Tags. Weitere Informationen finden Sie unter [Banner: Häufig gestellte Fragen]({{site.baseurl}}/user_guide/channels/banners/faq/).