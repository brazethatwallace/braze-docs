## Blocs éditeur pour les pages d'accueil {#landing-page-editor-blocks}

Les blocs éditeur pour les pages d'accueil se trouvent dans la section **Build** de l'**éditeur par glisser-déposer**, sous **Rows** et les catégories de blocs. Faites glisser un bloc dans la colonne d'une ligne ; il s'ajuste automatiquement à la largeur de la colonne. Sélectionnez un bloc pour modifier ses paramètres dans le panneau de propriétés situé à droite.

Pour plus d'informations sur la création et la publication de pages d'accueil, consultez [Créer des pages d'accueil]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/).

### Titre et paragraphe {#title-and-paragraph}

Ajoute un titre ou du texte de corps. Utile pour structurer les sections et améliorer la lisibilité.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Bouton {#button}

Ajoute un élément cliquable pour des actions telles que l'ouverture d'un lien ou l'envoi d'un formulaire.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Comportement au clic {#on-click-behavior}

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

{% alert important %}
Si vous configurez un bouton avec **Submit form when button is clicked** et ouvrez une URL web dans un nouvel onglet, iOS Safari peut bloquer la navigation. Ouvrez l'URL post-envoi dans le même onglet lors de l'envoi de formulaires. Pour plus d'informations, consultez [Créer des pages d'accueil]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/).
{% endalert %}

### Bouton radio {#radio-button}

Ajoute une liste d'options parmi lesquelles les utilisateurs peuvent en sélectionner une. Utilisez le panneau de propriétés pour configurer les options disponibles et l'attribut personnalisé qui reçoit la valeur sélectionnée. Le profil utilisateur enregistre la valeur sélectionnée en tant qu'[attribut personnalisé de type chaîne de caractères]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) lors de l'envoi du formulaire. Les attributs personnalisés avec d'autres types de données ne sont pas enregistrés dans le profil utilisateur.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### Image

Affiche une image à partir d'un téléchargement ou d'une URL externe.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### Comportement au clic

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Lien {#link}

Ajoute un lien hypertexte que les utilisateurs peuvent sélectionner pour accéder à une URL. Peut être intégré dans du texte ou utilisé de manière autonome.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Comportement au clic

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Espacement {#spacer}

Ajoute un espacement vertical entre les éléments.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Code personnalisé {#custom-code}

Insère du code HTML, CSS ou JavaScript personnalisé pour une personnalisation avancée, comme [Google Tag Manager]({{site.baseurl}}/user_guide/messaging/landing_pages/#google-tag-manager).

| Propriété | Description |
| --- | --- |
| Code personnalisé | Vous permet d'ajouter, de modifier ou de supprimer du HTML, du CSS et du JavaScript. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom code" }

<!-- Countdown timer is not yet released. Uncomment when available.
### Countdown timer

Displays a countdown to a date and time you set. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager.

After you add a **Countdown timer** block, use the properties panel to set the target date and time, labels, and styling.
-->

### Capture d'e-mail {#email-capture}

Ajoute un champ de formulaire pour les adresses e-mail. Lors de l'envoi, l'adresse est enregistrée dans le profil Braze de l'utilisateur.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Capture de téléphone {#phone-capture}

Ajoute un champ de formulaire pour les numéros de téléphone. Lors de l'envoi, l'utilisateur est abonné au groupe d'abonnement [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) ou [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/) que vous avez sélectionné.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Champ de saisie {#input-field}

Ajoute un champ de formulaire pour les attributs standard (par exemple, prénom ou nom) ou un attribut personnalisé de type chaîne de caractères.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### Liste déroulante {#dropdown}

Une liste prédéfinie d'éléments ; les utilisateurs en choisissent un. Vous pouvez associer les valeurs à des attributs personnalisés de type chaîne de caractères.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### Case à cocher {#checkbox}

Lorsqu'elle est cochée, l'[attribut personnalisé de type booléen]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types) du bloc est défini sur `true` ; lorsqu'elle est décochée, sur `false`.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Groupe de cases à cocher {#checkbox-group}

Les utilisateurs sélectionnent plusieurs options ; les valeurs définissent ou s'ajoutent à un [attribut personnalisé de type tableau]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types) défini.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Texte long {#long-text}

Champ de texte multiligne pour les flux de type enquête. Si vous ne voyez pas ce bloc, contactez l'[assistance Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support/) ou votre gestionnaire de la satisfaction client Braze. Ce bloc n'est pas disponible pour les pages d'accueil standard.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager.
-->

## Bon à savoir {#things-to-know}

- **Vidéo :** le compositeur standard n'inclut pas de bloc vidéo dédié. Utilisez **Custom code** pour intégrer un lecteur si nécessaire. Pour plus d'informations, consultez [Pages d'accueil]({{site.baseurl}}/user_guide/messaging/landing_pages/).