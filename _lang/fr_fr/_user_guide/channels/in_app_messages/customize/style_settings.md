---
nav_title: Paramètres de style
article_title: "Paramètres de style des messages in-app"
description: "Cet article de référence couvre les options de style disponibles lors de la création d'un message in-app avec l'éditeur par glisser-déposer."
page_order: 1
---

# Paramètres de style des messages in-app {#in-app-message-style-settings}

> L'expérience d'édition par glisser-déposer est divisée en deux sections : **Build** et **Preview & Test**. Cet article couvre ce que vous devez savoir pour travailler dans l'onglet **Build** de l'éditeur et suppose que vous avez déjà [créé un message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop).

![Onglet « Message Styles ».]({% image_buster /assets/img_archive/dnd_iam_message_styles.png %}){: style="float:right;max-width:25%;margin-left:15px;max-width:30%"}

## Styles au niveau du message {#message-level-styles}

Vous pouvez définir certains styles à appliquer à tous les blocs pertinents de votre message in-app depuis l'onglet **Message Styles**. Par exemple, vous pouvez personnaliser la police de tout le texte ou la couleur de tous les liens de votre message.

Les styles de cette section sont utilisés partout dans votre message, sauf lorsque vous les remplacez pour un bloc spécifique. Si votre message comporte [plusieurs pages]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop#multi-page), vous pouvez également remplacer les styles au niveau du message pour des pages individuelles, à l'exception du type d'affichage et de la largeur maximale.

Pour une expérience de conception plus simple, nous vous recommandons de configurer les styles au niveau du message avant de personnaliser les styles au niveau des blocs.

Pour revenir à l'onglet **Message Styles** à tout moment :

- Cliquez sur le bouton de fermeture X dans les propriétés de chaque bloc
- Sélectionnez le conteneur du message, le bouton de fermeture X du message ou l'arrière-plan de l'éditeur

### Polices personnalisées {#custom-fonts}

Nous acceptons les types de fichiers suivants pour les polices : `.ttf`, `.woff`, `.otf` et `.woff2`. Pour plus d'informations, consultez [Fichiers de ressources]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#asset-files).

Vous pouvez ajouter plusieurs variantes d'une famille de polices, car certaines options de style peuvent ne pas être disponibles pour les polices personnalisées. Actuellement, nous ne prenons pas en charge l'ajout de polices via URL.

Pour ajouter une police personnalisée :

1. Accédez à la section **Content** dans l'onglet **Message styles**.
2. Cliquez sur **Add custom font**.
3. Téléchargez votre police à l'aide de la bibliothèque multimédia.

{% alert note %}
La police au niveau du message s'appliquera uniquement au message actuel et à tous les messages dupliqués, mais pas aux modèles futurs.
{% endalert %}

## Composants du message {#message-components}

![GIF montrant la création d'un message in-app promotionnel.]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

L'éditeur par glisser-déposer utilise deux composants clés pour composer les messages in-app : les **lignes** et les **blocs**. Tous les blocs doivent être placés dans une ligne.

### Bouton de fermeture X {#close-x-button}

Pour les messages in-app de type fenêtre modale et plein écran, vous pouvez personnaliser le bouton de fermeture affiché sous la forme <i class="fa-solid fa-xmark"></i> en haut de votre message. Les options de personnalisation incluent la position du bouton, la taille, la couleur de remplissage, la couleur d'arrière-plan, le style de bordure et le rayon de bordure.

![Options de personnalisation du bouton de fermeture X dans les messages in-app, incluant la taille du bouton, la couleur de remplissage, la couleur d'arrière-plan, le style de bordure et le rayon de bordure.]({% image_buster /assets/img_archive/close_x_button.png %}){: style="max-width:40%"}

### Style span {#span-styling}

L'ajout d'un style span au texte dans les messages in-app permet une personnalisation avancée de l'apparence du message, en permettant l'utilisation de différentes couleurs de texte, polices et tailles. Le style span offre à vos utilisateurs une expérience plus engageante et visuellement attrayante en attirant leur attention sur les informations clés et en améliorant la clarté globale du message.

![Option affichée lors de la sélection de texte dans un message in-app. Une petite icône de pinceau indique que vous pouvez encadrer avec un span pour le style.]({% image_buster /assets/img_archive/span_1.png %}){: style="max-width:40%"}

![Panneau latéral « Span Properties » permettant à l'utilisateur final de personnaliser la famille de police, la graisse, la taille, l'espacement des lettres et la couleur du texte.]({% image_buster /assets/img_archive/span_2.png %}){: style="max-width:40%"}

### Lignes {#rows}

Les lignes sont des unités structurelles qui définissent la composition horizontale d'une section du message à l'aide de cellules.

![Lignes que vous pouvez ajouter dans votre message in-app.]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

Lorsqu'une ligne est sélectionnée, vous pouvez ajouter ou supprimer le nombre de colonnes dont vous avez besoin depuis la section **Column customization** pour placer différents éléments de contenu côte à côte.

Vous pouvez également faire glisser pour ajuster la taille des colonnes existantes.

![Ajustement des colonnes depuis la section « Column customization ».]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

En tant que bonne pratique, formatez les propriétés de vos lignes et colonnes avant de formater les blocs à l'intérieur des lignes. Il existe de nombreux endroits où vous pouvez ajuster l'espacement et l'alignement, donc commencer par les fondations facilite les modifications au fur et à mesure.

#### Image d'arrière-plan {#background-image}

Vous pouvez ajouter une image d'arrière-plan à une ligne dans le panneau **Row properties**. Activez **Background image**, puis fournissez une URL d'image ou sélectionnez une image depuis la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library). Enfin, configurez votre texte alternatif, la taille, la position et si l'image se répète pour créer des motifs sur toute la ligne.

![Image d'arrière-plan d'une ligne représentant une pizza avec un motif de répétition horizontal.]({% image_buster /assets/img_archive/background_row.png %})

### Blocs {#blocks}

Les blocs représentent différents types de contenu que vous pouvez utiliser dans votre message. Faites-en glisser un dans un segment de ligne existant, et il s'ajustera automatiquement à la largeur de la cellule.

{% alert tip %}
Avant d'ajouter des blocs, configurez les [styles au niveau du message](#set-message-level-styles) pour le conteneur du message, la police, les couleurs et tout ce que vous souhaitez personnaliser. Vous pouvez ensuite personnaliser les blocs individuels selon vos besoins. Le **bouton de fermeture** restera dans la section supérieure de votre message afin que les utilisateurs aient toujours la possibilité de fermer le message.
{% endalert %}

![Boîtes de glisser-déposer à sélectionner.]({% image_buster /assets/img_archive/dnd_iam_editor_blocks.png %}){: style="max-width:40%"}

Chaque bloc possède ses propres paramètres, comme un contrôle granulaire du remplissage. Le panneau de droite bascule automatiquement vers un panneau de style pour l'élément de contenu sélectionné. Pour plus d'informations, consultez [Propriétés des blocs éditeur]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=in-app%20messages#inappmessages_properties).

Lors de la création de votre message in-app, vous pouvez sélectionner une vue mobile, tablette ou ordinateur de bureau dans la barre d'outils pour prévisualiser l'apparence de votre message in-app pour vos groupes d'utilisateurs. Cela garantit que votre contenu est responsive, et vous pouvez effectuer les ajustements nécessaires au fur et à mesure.

{% multi_lang_include drag_and_drop/hide_rows_and_blocks_by_device.md channel='in_app_message' %}

## Détails créatifs {#creative-details}

### Plein écran sur les écrans plus grands {#fullscreen}

Sur une tablette ou un navigateur de bureau, un message in-app en plein écran s'affichera au centre de l'écran de l'application. Toute modification de la largeur maximale du message en plein écran ne s'appliquera qu'aux appareils tablette et ordinateur de bureau.

![Exemple de message in-app en plein écran.]({% image_buster /assets/img_archive/dnd_iam_fullscreen_example.png %}){: style="border:none"}

### Ajouter une image d'arrière-plan {#add-a-background-image}

Vous pouvez ajouter une image à l'arrière-plan de votre message depuis l'onglet **Message styles**.

1. Dans la zone de Canvas, sélectionnez le conteneur d'arrière-plan. Il s'agit de la section défilable de votre message.
2. Dans l'onglet **Message styles**, activez **Background image**.
3. Ajoutez une image depuis votre bibliothèque multimédia, ou saisissez l'URL où votre image est hébergée.

{% alert tip %}
Si vous avez du mal à sélectionner un bloc spécifique, vous pouvez utiliser la flèche vers le haut dans la barre d'outils intégrée du bloc pour déplacer le focus vers chaque bloc parent.
{% endalert %}

#### Permuter les images d'arrière-plan avec Liquid {#swap-background-images-with-liquid}

Pour permuter dynamiquement les images d'arrière-plan en fonction des données utilisateur (comme les attributs personnalisés ou les propriétés utilisateur), utilisez des blocs Liquid {% raw %}`{% capture %}`{% endraw %} pour assigner l'URL d'image correcte à une variable avant le chargement du HTML et du CSS.

Placez votre logique Liquid au début de votre message, puis référencez la variable capturée dans le champ URL de l'image d'arrière-plan. Cela sélectionne l'image correcte en fonction des données de chaque utilisateur.

Après avoir capturé l'URL de l'image, utilisez {% raw %}`{{ image_url | strip }}`{% endraw %} pour afficher l'URL sans espaces superflus. Vous pouvez ensuite coller ce Liquid dans le champ URL de l'image d'arrière-plan pour afficher dynamiquement différentes images pour différents utilisateurs.

##### Exemple {#example}

{% raw %}
```liquid
{% capture image_url %}
{% if {{custom_attribute.${membership_tier}}} == 'gold' %}
https://example.com/images/gold-background.png
{% elsif {{custom_attribute.${membership_tier}}} == 'silver' %}
https://example.com/images/silver-background.png
{% else %}
https://example.com/images/default-background.png
{% endif %}
{% endcapture %}
{{ image_url | strip }}
```
{% endraw %}

### Ajouter du Liquid {#add-liquid}

![Icône pour ajouter la personnalisation Liquid.]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

Pour ajouter du [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) dans votre message in-app, sélectionnez <i class="fa-solid fa-circle-plus"></i> **Add Personalization** depuis la barre d'outils de l'éditeur. Ici, vous pouvez ajouter différents types de personnalisation tels que les attributs par défaut, les attributs d'appareil, les attributs personnalisés, et plus encore.

Ensuite, prenez votre extrait de code Liquid généré et insérez-le dans votre message. Après avoir conçu et créé votre message in-app, accédez à **Preview & Test** pour prévisualiser votre message.

### Utiliser le rédacteur IA {#use-the-ai-copywriter}

Lorsqu'un bloc de texte est sélectionné dans votre message in-app, sélectionnez <i class="fa-solid fa-wand-magic-sparkles" title="Rédacteur IA"></i> **AI copywriter** dans la barre d'outils du bloc pour lancer l'[assistant de rédaction alimenté par l'IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). L'assistant de rédaction IA transmet un bref nom ou une description de produit à l'outil de génération de texte GPT3 d'OpenAI pour générer un texte marketing au ton naturel pour vos messages.

{% alert tip %}
Vous pouvez gagner quelques clics en surlignant le texte à l'intérieur du bloc avant de cliquer sur l'icône. Le texte surligné sera ajouté à l'outil, et le texte sera généré immédiatement.
{% endalert %}

![GIF du rédacteur IA.]({% image_buster /assets/img_archive/dnd_iam_ai_copywriter.gif %})

### Réinitialiser les styles par défaut {#reset-styles-to-default}

Les propriétés que vous avez modifiées par rapport à leur style par défaut sont marquées d'un point orange. Pour réinitialiser une propriété spécifique à son style par défaut, survolez le champ et sélectionnez **Reset to default**.

![Point orange qui réinitialise la taille du texte à sa taille par défaut.]({% image_buster /assets/img_archive/dnd_iam_reset_styles.gif %}){: style="max-width:45%"}

Vous pouvez également réinitialiser tous les styles d'un élément sélectionné en cliquant sur <i class="fas fa-paintbrush" title="Copier ou coller les styles"></i> à côté du nom du panneau de propriétés et en sélectionnant **Reset to default styles**.

### Copier et coller des styles {#copy-and-paste-styles}

Après avoir modifié le style d'un élément, vous pouvez copier et coller ces styles sur un autre élément. Lors du collage des styles, seules les propriétés pertinentes pour cet élément sont appliquées.

![Menu déroulant avec l'option de copier les styles.]({% image_buster /assets/img_archive/dnd_iam_copypaste_styles.png %}){: style="float:right;margin-left:15px;max-width:35%"}

1. Avec l'élément sélectionné, cliquez sur <i class="fas fa-paintbrush" title="Copier ou coller les styles"></i> **Copy or paste styles** à côté du nom du panneau de propriétés (par exemple, si vous avez un bouton sélectionné, à côté de « Button properties »).
2. Cliquez sur **Copy styles** et sélectionnez l'élément sur lequel vous souhaitez appliquer le style copié.
3. Cliquez à nouveau sur <i class="fas fa-paintbrush" title="Copier ou coller les styles"></i> **Copy or paste styles** et choisissez **Paste styles**.

#### Raccourcis clavier {#keyboard-shortcuts}

Vous pouvez également utiliser des raccourcis clavier pour copier et coller des styles :

| Action | Mac | Windows |
| ------------ | ---------------------------------------------- | ------------------------------------------------- |
| Copier les styles | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> |
| Coller les styles | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Raccourcis clavier" }