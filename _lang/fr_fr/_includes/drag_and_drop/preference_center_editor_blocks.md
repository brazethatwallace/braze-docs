## Blocs de l'éditeur du centre de préférences {#preference-center-editor-blocks}

Faites glisser les blocs depuis la section **Créer** dans une ligne de l'éditeur de centre de préférences par glisser-déposer. Chaque bloc possède ses propres paramètres ; le panneau de droite affiche les propriétés ou le style de l'élément sélectionné.

Avant de modifier les blocs, ajoutez des groupes d'abonnement et configurez le **smart block** d'abonnement (voir ci-dessous). Pour le flux de configuration complet, consultez [Créer un centre de préférences e-mail par glisser-déposer]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center/).

### Titre et paragraphe {#title-and-paragraph}

Ajoute un titre ou du texte avec des options de mise en forme enrichie.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Bouton {#button}

Ajoute un bouton cliquable (par exemple **Save** ou navigation).

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

### Image

Affiche une image provenant de la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/) ou d'une URL.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

### Espacement {#spacer}

Ajoute un espacement vertical entre les blocs.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Groupes d'abonnement (smart block) {#subscription-groups-smart-block}

Ajoute un bloc modèle qui répertorie les groupes d'abonnement, des contrôles facultatifs **Subscribe to all** / **Unsubscribe from all**, ainsi que des descriptions. Configurez-le après avoir ajouté des groupes dans le flux du centre de préférences.

Après avoir [ajouté des groupes d'abonnement]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center/#step-3-add-subscription-groups-to-the-preference-center), sélectionnez le smart block dans le canvas pour :

- Réorganiser les groupes d'abonnement
- Ajouter ou supprimer des groupes
- Ajouter ou supprimer des descriptions
- Basculer **Subscribe to all** et **Unsubscribe from all** pour les groupes de ce bloc

Le contrôle **Unsubscribe from all** en bas du modèle par défaut est obligatoire et effectue un [désabonnement global]({{site.baseurl}}/user_guide/channels/email/subscriptions/#subscription-states) des e-mails.

## Bon à savoir {#things-to-know}

- **Styles communs :** vous pouvez définir des valeurs par défaut pour l'ensemble de la page sous **Common Styles** avant d'ajuster les blocs individuels. Pour plus d'informations, consultez [Personnaliser le centre de préférences à l'aide de l'éditeur par glisser-déposer]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center/#step-4-customize-the-preference-center-using-the-drag-and-drop-editor).
- **Page de confirmation :** passez à **Confirmation Page** en haut de l'éditeur pour styliser l'expérience post-enregistrement en utilisant les mêmes types de blocs.