## Blocs éditeur de bannière {#banner-editor-blocks}

Dans le compositeur de bannière, faites glisser des lignes et des blocs depuis la section **Build** dans le canevas pour disposer votre message. Sélectionnez **Styles** pour ajuster le style au niveau de la page, ou sélectionnez un bloc ou une ligne pour modifier ses propriétés dans le panneau latéral.

Pour le flux complet de création de bannière, consultez [Créer une bannière]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#compose-a-banner).

Le compositeur de bannière propose les mêmes types de blocs de disposition que les autres surfaces de glisser-déposer, mais pas l'ensemble complet des blocs de formulaire (par exemple, pas de bouton radio, de texte court, de liste déroulante ou de case à cocher). Vous pouvez ajouter des blocs **Phone capture** et **Email capture** ; un seul bloc de capture de téléphone et un seul bloc de capture d'e-mail sont autorisés par message.

### Titre et paragraphe {#title-and-paragraph}

Ajoute un titre ou du texte de corps avec des options de texte enrichi.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Bouton {#button}

Ajoute un bouton cliquable. Vous pouvez définir les liens et les options d'analyse dans le panneau des propriétés.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Comportement au clic {#on-click-behavior}

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

Pour en savoir plus, consultez [Définir le comportement au clic]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#step-32-define-on-click-behavior-optional) dans l'article sur les bannières.

### Image

Affiche une image à partir d'une URL hébergée. Configurez les options d'affichage dans le panneau des propriétés.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### Comportement au clic

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Lien {#link}

Insère un lien hypertexte que les utilisateurs peuvent sélectionner.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Comportement au clic

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Espacement {#spacer}

Ajoute un espacement vertical entre les blocs.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Code personnalisé {#custom-code}

Insère du HTML personnalisé pour des dispositions avancées ou du contenu intégré (par exemple une vidéo). Les clics à l'intérieur du HTML personnalisé ne sont pas suivis, sauf si vous appelez `brazeBridge.logClick()` — consultez [Code personnalisé et pont JavaScript pour les bannières]({{site.baseurl}}/user_guide/channels/banners/custom_code/).

| Propriété | Description |
| --- | --- |
| Code personnalisé | Ajoutez ou modifiez le HTML (et les ressources associées) pour la bannière. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Code personnalisé" }

### Capture de téléphone {#phone-capture}

Collecte un numéro de téléphone. Lors de l'envoi, abonne l'utilisateur au groupe d'abonnement [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) ou [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/) sélectionné. Un seul par bannière.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Capture d'e-mail {#email-capture}

Collecte une adresse e-mail et l'ajoute au profil Braze de l'utilisateur lors de l'envoi. Un seul par bannière.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Texte long {#long-text}

Champ de texte multiligne pour les flux de type enquête. Si vous ne voyez pas ce bloc, contactez l'[assistance Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support/) ou votre gestionnaire de la satisfaction client Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze CSM.
-->

## Bon à savoir {#things-to-know}

- **Vidéo :** le compositeur standard n'inclut pas de bloc vidéo dédié. Utilisez **Custom code** pour intégrer un lecteur si nécessaire. Pour en savoir plus, consultez [Bannières : foire aux questions]({{site.baseurl}}/user_guide/channels/banners/faq/).
- **Liquid :** la plupart du Liquid est pris en charge ; il existe des exceptions telles que les balises de re-rendu de Catalogue. Pour en savoir plus, consultez [Bannières : foire aux questions]({{site.baseurl}}/user_guide/channels/banners/faq/).