## Blocs éditeurs de messages in-app {#in-app-message-editor-blocks}

Les blocs éditeurs se trouvent dans la section **Build** pour les messages in-app. Faites glisser un bloc dans une colonne ; il s'ajuste automatiquement à la largeur de la colonne. Sélectionnez un bloc pour modifier ses paramètres dans le panneau latéral droit.

Pour en savoir plus sur la création de messages in-app dans l'**éditeur par glisser-déposer**, consultez [Créer un message in-app par glisser-déposer]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/).

### Titre et paragraphe {#title-and-paragraph}

Ajoute un titre ou un paragraphe au message.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Bouton {#button}

Ajoute un bouton standard avec un style, des liens et des analyses configurables.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Comportement au clic {#on-click-behavior}

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

### Bouton radio {#radio-button}

Ajoute une liste d'options parmi lesquelles les utilisateurs peuvent en choisir une. Lors de l'envoi du formulaire, le profil utilisateur enregistre l'[attribut personnalisé]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) associé, qui doit être une chaîne de caractères pour être sauvegardé. Les attributs personnalisés avec d'autres types de données ne sont pas enregistrés dans le profil utilisateur.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### Image

Insère une image provenant de la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

Pour les spécifications relatives aux images, consultez nos [spécifications relatives aux images des messages in-app]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications/#in-app-messages).

#### Comportement au clic

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Lien {#link}

Insère un lien hypertexte sur lequel les utilisateurs peuvent cliquer pour accéder à une URL spécifiée. Il peut être intégré dans un texte ou utilisé de manière autonome.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Comportement au clic

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Espaceur {#spacer}

Ajoute de l'espace ou une marge intérieure entre les autres blocs.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Code personnalisé {#custom-code}

Insère du code HTML, CSS ou JavaScript personnalisé pour une personnalisation avancée.

| Propriété | Description |
| --- | --- |
| Code personnalisé | Permet d'ajouter, de modifier ou de supprimer du code HTML, CSS et JavaScript pour un message in-app. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Code personnalisé" }

### Capture de numéro de téléphone {#phone-capture}

Insère un champ de formulaire pour les numéros de téléphone. Une fois le formulaire envoyé, l'utilisateur est abonné au groupe d'abonnement [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) ou [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/).

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Capture d'adresse e-mail {#email-capture}

Insère un champ de formulaire pour les adresses e-mail. Une fois le formulaire envoyé, l'adresse e-mail est ajoutée au profil de l'utilisateur dans Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Texte court {#short-text}

Insère un champ de formulaire prenant en charge les attributs standard (tels que le prénom et le nom) ou une chaîne de caractères d'attribut personnalisé de votre choix.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### Liste déroulante {#dropdown}

Insère une liste déroulante avec une liste prédéfinie d'éléments parmi lesquels les utilisateurs peuvent en sélectionner un. Vous pouvez ajouter à la liste des chaînes de caractères d'attributs personnalisés.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### Case à cocher {#checkbox}

Insère une case à cocher. Si l'utilisateur coche la case, l'[attribut personnalisé booléen]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types) du bloc est défini sur `true`. Si la case reste décochée, l'attribut est défini sur `false`.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Groupe de cases à cocher {#checkbox-group}

Les utilisateurs peuvent choisir parmi plusieurs options proposées. Les valeurs sont définies ou ajoutées à un [attribut personnalisé de type tableau]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types).

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Texte long {#long-text}

Champ de texte multiligne pour les flux de type enquête. Si vous ne voyez pas ce bloc, contactez l'[assistance Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support/) ou votre gestionnaire de la satisfaction client Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager.
-->

## Bon à savoir {#things-to-know}

- **Vidéo :** le compositeur standard n'inclut pas de bloc vidéo dédié. Utilisez le bloc **Code personnalisé** pour intégrer un lecteur si nécessaire. Pour en savoir plus, consultez [Messages in-app : questions fréquentes]({{site.baseurl}}/user_guide/channels/in_app_messages/faq/).