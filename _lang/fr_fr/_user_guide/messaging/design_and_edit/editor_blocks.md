---
nav_title: Blocs éditeur
article_title: Blocs éditeur par glisser-déposer
alias: "/dnd/editor_blocks/"
channel:
- email
- in-app messages
- landing pages
- banners
- preference center
page_order: 3
page_type: reference
description: "Cet article de référence couvre les blocs éditeur dans l'éditeur par glisser-déposer pour les e-mails, les messages in-app, les pages de destination, les bannières et les centres de préférences des e-mails par glisser-déposer."
tool: Media
---

# Blocs de l'éditeur par glisser-déposer {#drag-and-drop-editor-blocks}

> Les blocs éditeur sont les tuiles que vous glissez dans les lignes et les colonnes de l'éditeur par glisser-déposer.

Sélectionnez l'éditeur que vous utilisez :

{% sdktabs %}

{% sdktab email %}
## Blocs éditeur pour les e-mails {#email-editor-blocks}

Les blocs éditeur se trouvent dans la section **Contenu** pour les e-mails. Glissez un bloc dans une colonne de l'**éditeur par glisser-déposer** ; il s'ajuste automatiquement à la largeur de la colonne.

Pour plus d'informations sur la création d'e-mails dans l'**éditeur par glisser-déposer**, consultez [Créer un e-mail par glisser-déposer]({{site.baseurl}}/user_guide/channels/email/drag_and_drop) et <a href="{{site.baseurl}}/user_guide/channels/email/drag_and_drop/#other-customizations">Autres personnalisations</a> dans cet article.

{% alert tip %}
Vous pouvez également ajouter des [attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types) à n'importe quelle URL dans les blocs éditeur `Image`, `Button` ou `Text`.
{% endalert %}

### Titre {#title}

Ajoute du texte pour les en-têtes dans l'e-mail.

| Propriété | Description |
|---|---|
| Titre | Sélectionne le style de titre. |
| Famille de polices | Le style de police pour votre titre. |
| Graisse de police | La graisse globale de la police. |
| Taille de police | Détermine la taille de votre texte. |
| Couleur du texte | Modifie la couleur du titre. |
| Couleur du lien | Modifie la couleur du lien. |
| Alignement | Déplace le titre pour qu'il soit aligné à gauche, au centre ou à droite. |
| Hauteur de ligne | Modifie la distance entre les lignes de texte. |
| Espacement des lettres | Modifie la distance entre chaque caractère. |
| Direction du texte | Par défaut de gauche à droite, mais peut être modifié pour être [de droite à gauche]({{site.baseurl}}/right_to_left_messages). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Titre" }

### Paragraphe {#paragraph}

Insère du texte dans le message. Une barre d'outils aide à la mise en forme de la police et du texte.

| Propriété | Description |
|---|---|
| Famille de polices | Le style de police pour le texte de votre paragraphe. |
| Graisse de police | La graisse globale de la police. |
| Taille de police | Détermine la taille de votre texte. |
| Couleur du texte | Modifie la couleur du texte. |
| Couleur du lien | Modifie la couleur du lien. |
| Alignement | Déplace le texte pour qu'il soit aligné à gauche, au centre ou à droite. |
| Espacement des paragraphes | Modifie l'espace entre les paragraphes. |
| Hauteur de ligne | Modifie la distance entre les lignes de texte. |
| Espacement des lettres | Modifie la distance entre chaque caractère. |
| Direction du texte | Par défaut de gauche à droite, mais peut être modifié pour être [de droite à gauche]({{site.baseurl}}/right_to_left_messages). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paragraphe" }

### Liste {#list}

Ajoute une liste à puces.

| Propriété | Description |
|---|---|
| Type de liste | Le type de liste. Peut être à puces ou numérotée. |
| Style de liste | Détermine le style de votre liste. |
| Commencer la liste à partir de | Détermine le numéro de départ de votre liste. |
| Famille de polices | Le style de police pour le texte de votre paragraphe. |
| Graisse de police | La graisse globale de la police. |
| Taille de police | Détermine la taille de votre texte. |
| Couleur du texte | Modifie la couleur du texte. |
| Couleur du lien | Modifie la couleur du lien. |
| Alignement | Déplace le texte pour qu'il soit aligné à gauche, au centre ou à droite. |
| Espacement des éléments de liste | Modifie l'espace entre les éléments de la liste. |
| Indentation des éléments de liste | Modifie l'indentation des éléments de la liste. |
| Hauteur de ligne | Modifie la distance entre les lignes de texte. |
| Espacement des lettres | Modifie la distance entre chaque caractère. |
| Direction du texte | Par défaut de gauche à droite, mais peut être modifié pour être [de droite à gauche]({{site.baseurl}}/right_to_left_messages). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liste" }

### Bouton {#button}

Ajoute un bouton standard. Les propriétés permettent de modifier le style et de définir le comportement du lien.

| Propriété | Description |
|---|---|
| Options du bouton | Définit diverses options du bouton, telles que la police, la taille, la largeur, la couleur et le remplissage. |
| Survol du bouton | Le style du bouton lorsqu'un utilisateur le survole avec une souris ou un pavé tactile. Inclut la couleur d'arrière-plan du bouton, la couleur de la police et les styles de bordure. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bouton" }

#### Comportement au clic {#on-click-behavior}

| Propriété | Description |
|---|---|
| Type de lien | Détermine l'action lors du clic sur le bouton et définit le protocole approprié. |
| URL | Dynamique en fonction du type de lien **Ouvrir une page web**. |
| Destinataire, objet et corps | Pour le type de lien **Envoyer un e-mail**, définit l'adresse e-mail du destinataire, l'objet et le contenu qui seront pré-remplis dans un brouillon d'e-mail lorsque l'utilisateur sélectionne le bouton. |
| Tél | Pour les types de lien **Passer un appel** et **Envoyer un SMS**, définit le numéro de téléphone que l'utilisateur appellera ou auquel il enverra un SMS en sélectionnant le bouton. |
| Message | Pour le type de lien **Envoyer un SMS**, définit le contenu qui sera pré-rempli dans un brouillon de SMS lorsque l'utilisateur sélectionne le bouton. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportement au clic" }

### Séparateur {#divider}

Insère une ligne continue, pointillée ou en tirets pour aider à l'espacement.

| Propriété | Description |
|---|---|
| Transparent | Si activé, les options de ligne et de largeur sont supprimées. |
| Ligne | Les différents formats de ligne, qu'ils soient pointillés, en tirets ou continus. Vous pouvez également modifier l'épaisseur et la couleur de la ligne de séparation. |
| Largeur | Ajuste l'étendue du séparateur par incréments de 5. |
| Alignement | Déplace la ligne pour qu'elle soit alignée à gauche, au centre ou à droite. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Séparateur" }

### Espacement {#spacer}

Ajoute de l'espace ou du remplissage entre les autres blocs.

| Propriété | Description |
|---|---|
| Hauteur | Ajuste la hauteur du bloc d'espacement. La valeur par défaut est 60 px. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Espacement" }

### Image {#image}

Insère une image depuis la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library). Pour les images dynamiques (images avec Liquid ou contenu connecté), vous devez définir une image de secours pour utiliser les paramètres de largeur automatique. Pour les spécifications d'image, consultez les [spécifications d'image pour les e-mails]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications#email).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

| Propriété | Description |
|---|---|
| Largeur automatique | Modifie la largeur de l'image en pixels. |
| Alignement | Définit l'alignement de l'image à gauche, au centre ou à droite dans le bloc. |
| Image avec Liquid | Utilise la logique [Liquid]({{site.baseurl}}/liquid) pour définir dynamiquement différentes images dans le même bloc de contenu. |
| URL | Définit une image en utilisant l'adresse de son hébergement. |
| Texte alternatif | Une courte description de l'image qui fournit aux utilisateurs les mêmes informations que celles affichées dans l'image. Essentiel pour l'accessibilité des lecteurs d'écran ou lorsque l'image ne se charge pas. |
| Image avec coins arrondis | Affiche l'image avec des coins arrondis. Par défaut, les images sont affichées avec des coins carrés. |
| Action | Déclenche une action lorsque l'utilisateur clique sur l'image. |
| Options du bloc | Définit le remplissage autour du bloc d'image. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image" }

{% alert tip %}
Pour la **largeur automatique**, le redimensionnement automatique de l'image choisit la meilleure taille pour l'image en fonction d'une combinaison de la largeur de l'image et de l'espace disponible dans la mise en page :
- Les images plus larges que l'espace disponible sont définies à 100 % de largeur et conservent ce ratio sur mobile, utilisant toute la largeur d'affichage de l'appareil.
- Les images plus petites que l'espace disponible utilisent la taille naturelle de l'image pour éviter les effets de distorsion ou les images floues.
{% endalert %}

#### Comportement du bouton de téléchargement Gmail {#gmail-download-button-behavior}

Gmail ajoute automatiquement un bouton de téléchargement aux images qui n'ont pas de lien hypertexte (`href`) associé. Cependant, si le rapport hauteur/largeur de l'image est de 299 x 524 px ou moins, Gmail n'affichera pas le bouton de téléchargement.

Pour empêcher le bouton de téléchargement d'apparaître sur les images plus grandes, vous pouvez appliquer la solution de contournement avec le lien « # » :

1. Sélectionnez le bloc **Image**.
2. Dans le panneau **Options du bloc**, accédez à la section **Lien**.
3. Définissez le **Type de lien** sur **Ouvrir une page web**.
4. Saisissez un signe dièse (`#`) dans le champ de saisie **URL**.

L'ajout de ce lien empêche Gmail d'afficher le bouton de téléchargement sans affecter l'expérience utilisateur.

### Vidéo {#video}

Crée un lien vers du contenu vidéo. Seuls YouTube et Vimeo sont pris en charge.

| Propriété | Description |
|---|---|
| URL | L'URL de la vidéo. |
| Titre | Généré automatiquement à partir des métadonnées de la vidéo ou peut être personnalisé. |
| Style de l'icône de lecture | Inclut différentes options pour le bouton de lecture situé en haut d'une image vidéo. |
| Couleur de l'icône de lecture | Option pour sélectionner **Clair** ou **Foncé** pour le bouton de lecture. |
| Taille de l'icône de lecture | Choisissez la taille en pixels du bouton de lecture. Plage prédéfinie de 50&nbsp;px à 80&nbsp;px (par incréments de 5&nbsp;px). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vidéo" }

{% alert tip %}
Les vidéos hébergées par Vimeo ne fonctionnent que si elles sont définies comme publiques. Tous les autres paramètres de sécurité disponibles dans Vimeo (par exemple, « Masquer de Vimeo.com ») génèrent un format de lien différent qui n'est pas pris en charge par ce Content Block. Ces types de liens sont modifiés par le générateur, ce qui empêche Braze de générer une miniature.
{% endalert %}

### Réseaux sociaux {#social}

Insère des icônes de plateformes de réseaux sociaux. Vous pouvez télécharger des images personnalisées pour des icônes spécifiques à votre marque.

| Propriété | Description |
|---|---|
| Sélectionner la collection d'icônes | Définit le style de votre collection d'icônes. |
| Configurer la collection d'icônes | Définit l'URL pour chaque icône de réseau social. Inclut le bouton bascule **Plus d'options** pour modifier le titre et le texte alternatif. |
| Alignement | Déplace l'icône de réseau social pour qu'elle soit alignée à gauche, au centre ou à droite. |
| Espacement des icônes | Détermine l'espacement entre chaque icône de réseau social. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Réseaux sociaux" }

### Icônes {#icons}

Insère une icône. Vous pouvez télécharger des images personnalisées. Braze utilise une icône de marque substitutive surdimensionnée jusqu'à ce que vous téléchargiez une image.

| Propriété | Description |
|---|---|
| Famille de polices | Le style de police pour le texte de votre paragraphe. |
| Graisse de police | La graisse globale de la police. |
| Taille de police | Détermine la taille de votre texte. |
| Couleur du texte | Modifie la couleur du titre. |
| Couleur du lien | Modifie la couleur du lien. |
| Alignement | Déplace l'icône pour qu'elle soit alignée à gauche, au centre ou à droite. |
| Espacement des lettres | Modifie la distance entre chaque caractère. |
| Taille de l'icône | Détermine la taille de votre icône. |
| Espacement de l'icône | Modifie l'espacement de l'icône. |
| Remplissage de l'icône | Modifie le remplissage de l'icône. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Icônes" }

### HTML

Insère du HTML brut. Recommandé pour [Liquid]({{site.baseurl}}/liquid), comme le contenu connecté ou les instructions conditionnelles.

| Propriété | Description |
|---|---|
| HTML | Ajoutez ou modifiez du HTML brut, y compris [Liquid]({{site.baseurl}}/liquid) pour la personnalisation ou la logique conditionnelle. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTML" }

### Menu {#menu}

Crée un menu flexible pour le message que vous concevez.

| Propriété | Description |
|---|---|
| Configurer les éléments du menu | Ajouter un élément de menu. |
| Famille de polices | Le style de police pour le menu. |
| Taille de police | La taille de votre menu. |
| Couleur du texte | Modifie la couleur du menu. |
| Couleur du lien | Modifie la couleur du texte du menu. |
| Alignement | Déplace le menu pour qu'il soit aligné à gauche, au centre ou à droite. |
| Espacement des lettres | Modifie la distance entre chaque caractère. |
| Disposition | Détermine si la disposition est horizontale ou verticale. |
| Séparateur | Ajoute un ou plusieurs caractères entre les options du menu. |
| Menu mobile | Inclut des options pour modifier la taille de l'icône, la couleur et le type d'icône lorsqu'il est affiché sur un appareil mobile. |
| Remplissage des éléments | Modifie le remplissage en utilisant les boutons **+** ou **-**, ou en saisissant un nombre spécifique. |
| Tous les côtés | Définit un remplissage uniforme si le remplissage des éléments est désactivé. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Menu" }

### Produit {#product}

Affiche des lignes de produits à partir d'un [catalogue de produits]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks), soit sous forme d'éléments statiques à partir d'une sélection de catalogue (jusqu'à 12), soit sous forme de produits dynamiques pilotés par un [déclencheur eCommerce Canvas]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases) (jusqu'à 24).

| Propriété | Description |
| --- | --- |
| Type de contenu | Définit si les produits proviennent d'une **sélection** de catalogue fixe (**Statique**, jusqu'à 12 produits) ou d'un déclencheur de recommandation eCommerce Canvas (**Dynamique**, jusqu'à 24 produits). **Dynamique** n'est disponible que dans les étapes de message Canvas. |
| Catalogue | Sélectionne le catalogue de produits qui fournit les données et les mappages de champs des produits. |
| Sélection | *(Statique uniquement)* Sélectionne l'ensemble filtré du catalogue qui définit les produits affichés. |
| Afficher les détails de la source | Active le texte d'aide affichant le catalogue sous-jacent ou le champ d'événement mappé à chaque champ de produit. |
| Image de la variante | Affiche ou masque l'image de la variante pour chaque tuile de produit. |
| Titre du produit | Affiche ou masque le titre du produit pour chaque tuile. |
| Prix | Affiche ou masque le prix du produit. |
| Bouton pour l'URL du produit | Affiche ou masque un bouton d'appel à l'action renvoyant vers l'URL du produit. |
| Quantité | *(Dynamique, Canvas uniquement, lorsque le déclencheur d'entrée n'est pas un événement de consultation de produit)* Affiche ou masque la quantité du produit provenant de l'événement déclencheur. |
| Orientation du produit | Définit la position de l'image dans chaque tuile : **Image à gauche**, **Image au centre** ou **Image à droite**. |
| Alignement | Définit l'alignement horizontal du contenu dans chaque tuile. |
| Nombre max. de produits par ligne | Définit le nombre de produits affichés par ligne : **1**, **2** ou **3** (**3** n'est disponible que lorsque l'orientation est **Image au centre**). |
| Espacement des produits | Définit l'espacement entre les produits : **Auto** ou **Personnalisé**. |
| Espacement personnalisé | *(Lorsque **Personnalisé** est sélectionné)* Définit l'écart en pixels entre les produits. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Produit" }

## Personnalisation {#personalization}

Vous pouvez ajouter de la personnalisation à votre e-mail en utilisant Liquid ou le contenu connecté.

- **Liquid :** Sous **Contenu** > **Personnalisation**, sélectionnez un attribut, copiez l'extrait de code et collez-le dans un bloc HTML. Bien que les extraits Liquid de base puissent fonctionner dans les blocs Titre, Paragraphe et Liste, placer du Liquid dans ces blocs peut provoquer un comportement inattendu et des problèmes de mise en page. Pour éviter les problèmes, utilisez les blocs HTML pour toute logique Liquid. Notez que Liquid n'est pas pris en charge dans les blocs d'image ni dans les champs d'URL des boutons.
- **[Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) :** Ajoutez un bloc **HTML** et placez-y votre appel {% raw %}`{% connected_content %}`{% endraw %}.

{% endsdktab %}

{% sdktab in-app messages %}
## Blocs éditeur pour les messages in-app {#in-app-message-editor-blocks}

Les blocs éditeur se trouvent dans la section **Créer** pour les messages in-app. Glissez un bloc dans une colonne ; il s'ajuste automatiquement à la largeur de la colonne. Sélectionnez un bloc pour modifier ses paramètres dans le panneau latéral droit.

Pour plus d'informations sur la création de messages in-app dans l'**éditeur par glisser-déposer**, consultez [Créer un message in-app par glisser-déposer]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop).

### Titre et paragraphe {#title-and-paragraph}

Ajoute du texte de titre ou de paragraphe au message.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Bouton

Ajoute un bouton standard avec un style, des liens et des analyses configurables.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Comportement au clic

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

### Bouton radio {#radio-button}

Ajoute une liste d'options parmi lesquelles les utilisateurs peuvent en sélectionner une. Lors de la soumission, le profil utilisateur enregistre l'[attribut personnalisé]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) associé, qui doit être une chaîne de caractères pour être enregistré. Les attributs personnalisés avec d'autres types de données ne sont pas enregistrés dans le profil utilisateur.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### Image

Insère une image depuis la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

Pour les spécifications d'image, consultez nos [spécifications d'image pour les messages in-app]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications#in-app-messages).

#### Comportement au clic

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Lien {#link}

Insère un lien hypertexte sur lequel les utilisateurs peuvent cliquer pour accéder à une URL spécifiée. Peut être intégré dans du texte ou autonome.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Comportement au clic

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Espacement

Ajoute de l'espace ou du remplissage entre les autres blocs.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Code personnalisé {#custom-code}

Insère du HTML, CSS ou JavaScript personnalisé pour une personnalisation avancée.

| Propriété | Description |
| --- | --- |
| Code personnalisé | Vous permet d'ajouter, de modifier ou de supprimer du HTML, du CSS et du JavaScript pour un message in-app. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Code personnalisé" }

### Capture de téléphone {#phone-capture}

Insère un champ de formulaire pour les numéros de téléphone. Lors de la soumission, l'utilisateur est abonné au groupe d'abonnement [SMS]({{site.baseurl}}/sms_rcs_subscription_groups) ou [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups).

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Capture d'e-mail {#email-capture}

Insère un champ de formulaire pour les adresses e-mail. Lors de la soumission, l'adresse e-mail est ajoutée au profil de cet utilisateur dans Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Texte court {#short-text}

Insère un champ de formulaire qui prend en charge les attributs standard (tels que le prénom et le nom) ou une chaîne d'attribut personnalisé de votre choix.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### Liste déroulante {#dropdown}

Insère une liste déroulante avec une liste prédéfinie d'éléments parmi lesquels les utilisateurs peuvent en sélectionner un. Vous pouvez ajouter n'importe quelle chaîne d'attribut personnalisé à la liste.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### Case à cocher {#checkbox}

Insère une case à cocher. Si l'utilisateur coche la case, l'[attribut personnalisé booléen]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) du bloc est défini sur `true`. Si elle n'est pas cochée, son attribut est défini sur `false`.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Groupe de cases à cocher {#checkbox-group}

Les utilisateurs peuvent sélectionner parmi plusieurs choix. Les valeurs sont définies ou ajoutées à un [attribut personnalisé de type tableau]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) défini.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Texte long {#long-text}

Champ de texte multiligne pour les flux de type enquête. Si vous ne voyez pas ce bloc, contactez le [support Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) ou votre gestionnaire du succès des clients Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Ligne enregistrée {#saved-row}

Insère une ligne réutilisable que vous avez enregistrée précédemment en tant que Content Block par glisser-déposer. Les lignes enregistrées ne sont **pas liées** au Content Block d'origine — si l'original est mis à jour, vous devrez le glisser à nouveau dans l'éditeur pour obtenir la dernière version. Pour plus d'informations, consultez [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). Si vous ne voyez pas **Ligne enregistrée** sous **Lignes**, contactez le [support Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) ou votre gestionnaire du succès des clients Braze.
-->

## Bon à savoir {#things-to-know}

- **Vidéo :** Le compositeur standard n'inclut pas de bloc vidéo dédié. Utilisez le **code personnalisé** pour intégrer un lecteur si nécessaire. Pour plus d'informations, consultez [Messages in-app : questions fréquentes]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

{% endsdktab %}

{% sdktab landing pages %}
## Blocs éditeur pour les pages de destination {#landing-page-editor-blocks}

Les blocs éditeur pour les pages de destination se trouvent dans la section **Créer** de l'**éditeur par glisser-déposer**, sous **Lignes** et les catégories de blocs. Glissez un bloc dans une colonne de ligne ; il s'ajuste automatiquement à la largeur de la colonne. Sélectionnez un bloc pour modifier ses paramètres dans le panneau de propriétés latéral droit.

Pour plus d'informations sur la création et la publication de pages de destination, consultez [Créer des pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages).

### Titre et paragraphe

Ajoute du texte de titre ou de corps. Utile pour structurer les sections et améliorer la lisibilité.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Bouton

Ajoute un élément cliquable pour des actions telles que l'ouverture d'un lien ou la soumission d'un formulaire.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Comportement au clic

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

{% alert important %}
Si vous configurez un bouton avec **Soumettre le formulaire lorsque le bouton est cliqué** et ouvrez une URL web dans un nouvel onglet, iOS Safari peut bloquer la navigation. Ouvrez l'URL post-soumission dans le même onglet lors de la soumission de formulaires. Pour plus d'informations, consultez [Créer des pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages).
{% endalert %}

### Bouton radio

Ajoute une liste d'options parmi lesquelles les utilisateurs peuvent en sélectionner une. Utilisez le panneau de propriétés pour configurer les options disponibles et l'attribut personnalisé qui reçoit la valeur sélectionnée. Le profil utilisateur enregistre la valeur sélectionnée en tant qu'[attribut personnalisé de type chaîne de caractères]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) lors de la soumission du formulaire. Les attributs personnalisés avec d'autres types de données ne sont pas enregistrés dans le profil utilisateur.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### Image

Affiche une image à partir d'un téléchargement ou d'une URL externe.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### Comportement au clic

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Lien

Ajoute un lien hypertexte que les utilisateurs peuvent sélectionner pour accéder à une URL. Peut être intégré dans du texte ou autonome.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Comportement au clic

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Espacement

Ajoute un espacement vertical entre les éléments.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Code personnalisé

Insère du HTML, CSS ou JavaScript personnalisé pour une personnalisation avancée, comme [Google Tag Manager]({{site.baseurl}}/user_guide/messaging/landing_pages#adding-google-tag-manager-to-a-landing-page).

| Propriété | Description |
| --- | --- |
| Code personnalisé | Vous permet d'ajouter, de modifier ou de supprimer du HTML, du CSS et du JavaScript. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Code personnalisé" }

<!-- Countdown timer is not yet released. Uncomment when available.
### Compte à rebours {#countdown-timer}

Affiche un compte à rebours jusqu'à une date et une heure que vous définissez. Si vous ne voyez pas ce bloc, contactez le [support Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) ou votre gestionnaire du succès des clients Braze.

Après avoir ajouté un bloc **Compte à rebours**, utilisez le panneau de propriétés pour définir la date et l'heure cibles, les libellés et le style.
-->

### Capture d'e-mail

Ajoute un champ de formulaire pour les adresses e-mail. Lors de la soumission, l'adresse est enregistrée dans le profil Braze de l'utilisateur.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Capture de téléphone

Ajoute un champ de formulaire pour les numéros de téléphone. Lors de la soumission, l'utilisateur est abonné au groupe d'abonnement [SMS]({{site.baseurl}}/sms_rcs_subscription_groups) ou [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups) que vous avez sélectionné.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Champ de saisie {#input-field}

Ajoute un champ de formulaire pour les attributs standard (par exemple, le prénom ou le nom) ou une chaîne d'attribut personnalisé.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### Liste déroulante

Une liste prédéfinie d'éléments ; les utilisateurs en choisissent un. Vous pouvez mapper les valeurs à des chaînes d'attribut personnalisé.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### Case à cocher

Lorsqu'elle est cochée, définit l'[attribut personnalisé booléen]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) du bloc sur `true` ; lorsqu'elle n'est pas cochée, sur `false`.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Groupe de cases à cocher

Les utilisateurs choisissent plusieurs options ; les valeurs sont définies ou ajoutées à un [attribut personnalisé de type tableau]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) défini.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Gestion des abonnements {#manage-subscriptions}

Ajoute une liste de [groupes d'abonnement e-mail]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups) afin que les visiteurs puissent s'abonner ou gérer leurs abonnements lors de la soumission du formulaire. Configurez-le après avoir ajouté des groupes d'abonnement au bloc. Ce bloc ne prend en charge que les groupes d'abonnement e-mail ; il ne prend pas en charge les groupes d'abonnement SMS, RCS ou WhatsApp.

Pour les utilisateurs identifiés qui ouvrent la page via l'[étiquette Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) de la page de destination, le bloc pré-remplit chaque case à cocher avec l'état d'abonnement actuel de l'utilisateur, ce qui permet également de l'utiliser comme page de gestion des préférences.

Sélectionnez le bloc dans l'éditeur pour :

- Réorganiser les groupes d'abonnement
- Ajouter ou supprimer des groupes d'abonnement
- Ajouter ou supprimer des descriptions
- Ajouter ou supprimer une case à cocher « S'abonner à tous » qui sélectionne tous les groupes d'abonnement du bloc

| Propriété | Description |
| --- | --- |
| Groupes d'abonnement | Ajoutez, supprimez ou réorganisez les groupes d'abonnement affichés dans le bloc. |
| Inclure les descriptions | Affiche la description de chaque groupe d'abonnement à côté de son nom. |
| Case à cocher **S'abonner à tous** | Ajoute une case à cocher qui sélectionne tous les groupes d'abonnement du bloc. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gestion des abonnements" }

Pour le flux de configuration complet, consultez [Bloc Gestion des abonnements]({{site.baseurl}}/user_guide/messaging/landing_pages/manage_subscriptions).

### Texte long

Champ de texte multiligne pour les flux de type enquête. Si vous ne voyez pas ce bloc, contactez le [support Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) ou votre gestionnaire du succès des clients Braze. Ce bloc n'est pas disponible pour les pages de destination standard.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Ligne enregistrée

Insère une ligne réutilisable que vous avez enregistrée précédemment en tant que Content Block par glisser-déposer. Les lignes enregistrées ne sont **pas liées** au Content Block d'origine — si l'original est mis à jour, vous devrez le glisser à nouveau dans l'éditeur pour obtenir la dernière version. Pour plus d'informations, consultez [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). Si vous ne voyez pas **Ligne enregistrée** sous **Lignes**, contactez le [support Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) ou votre gestionnaire du succès des clients Braze.
-->

## Bon à savoir

- **Vidéo :** Le compositeur standard n'inclut pas de bloc vidéo dédié. Utilisez le **code personnalisé** pour intégrer un lecteur si nécessaire. Pour plus d'informations, consultez [Pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages).

{% endsdktab %}

{% sdktab banners %}
## Blocs éditeur pour les bannières {#banner-editor-blocks}

Dans le compositeur de bannières, glissez des lignes et des blocs depuis la section **Créer** dans le canevas pour disposer votre message. Sélectionnez **Styles** pour ajuster le style au niveau de la page, ou sélectionnez un bloc ou une ligne pour modifier ses propriétés dans le panneau latéral.

Pour le flux complet de création de bannières, consultez [Créer une bannière]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#compose-a-banner).

Le compositeur de bannières offre les mêmes types de blocs de mise en page que les autres surfaces par glisser-déposer, mais pas l'ensemble complet de blocs de formulaire (par exemple, pas de bouton radio, de texte court, de liste déroulante ni de case à cocher). Vous pouvez ajouter des blocs **Capture de téléphone** et **Capture d'e-mail** ; un seul bloc de capture de téléphone et un seul bloc de capture d'e-mail sont autorisés par message.

### Titre et paragraphe

Ajoute du texte de titre ou de corps avec des options de texte enrichi.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Bouton

Ajoute un bouton cliquable. Vous pouvez définir les liens et les options d'analyse dans le panneau de propriétés.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Comportement au clic

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

Pour plus d'informations, consultez [Définir le comportement au clic]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#step-32-define-on-click-behavior-optional) dans l'article sur les bannières.

### Image

Affiche une image à partir d'une URL hébergée. Configurez les options d'affichage dans le panneau de propriétés.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### Comportement au clic

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Lien

Insère un lien hypertexte que les utilisateurs peuvent sélectionner.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Comportement au clic

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Espacement

Ajoute un espacement vertical entre les blocs.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Code personnalisé

Insère du HTML personnalisé pour des mises en page avancées ou du contenu intégré (par exemple, une vidéo). Les clics à l'intérieur du HTML personnalisé ne sont pas suivis sauf si vous appelez `brazeBridge.logClick()` — consultez [Code personnalisé et pont JavaScript pour les bannières]({{site.baseurl}}/user_guide/channels/banners/custom_code).

| Propriété | Description |
| --- | --- |
| Code personnalisé | Ajoutez ou modifiez du HTML (et les ressources associées) pour la bannière. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Code personnalisé" }

### Capture de téléphone

Collecte un numéro de téléphone. Lors de la soumission, l'utilisateur est abonné au groupe d'abonnement [SMS]({{site.baseurl}}/sms_rcs_subscription_groups) ou [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups) que vous avez sélectionné. Un seul par bannière.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Capture d'e-mail

Collecte une adresse e-mail et l'ajoute au profil Braze de l'utilisateur lors de la soumission. Un seul par bannière.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Texte long

Champ de texte multiligne pour les flux de type enquête. Si vous ne voyez pas ce bloc, contactez le [support Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) ou votre gestionnaire du succès des clients Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Ligne enregistrée

Insère une ligne réutilisable que vous avez enregistrée précédemment en tant que Content Block par glisser-déposer. Les lignes enregistrées ne sont **pas liées** au Content Block d'origine — si l'original est mis à jour, vous devrez le glisser à nouveau dans l'éditeur pour obtenir la dernière version. Pour plus d'informations, consultez [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). Si vous ne voyez pas **Ligne enregistrée** sous **Lignes**, contactez le [support Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) ou votre gestionnaire du succès des clients Braze.
-->

## Bon à savoir

- **Vidéo :** Le compositeur standard n'inclut pas de bloc vidéo dédié. Utilisez le **code personnalisé** pour intégrer un lecteur si nécessaire. Pour plus d'informations, consultez [Bannières : questions fréquentes]({{site.baseurl}}/user_guide/channels/banners/faq).
- **Liquid :** La plupart du Liquid est pris en charge ; il existe des exceptions telles que les balises de re-rendu de catalogue. Pour plus d'informations, consultez [Bannières : questions fréquentes]({{site.baseurl}}/user_guide/channels/banners/faq).

{% endsdktab %}

{% sdktab preference center %}
## Blocs éditeur pour le centre de préférences {#preference-center-editor-blocks}

Glissez des blocs depuis la section **Créer** dans une ligne de l'éditeur par glisser-déposer du centre de préférences. Chaque bloc a ses propres paramètres ; le panneau latéral droit bascule vers les propriétés ou le style de l'élément sélectionné.

Avant de modifier les blocs, ajoutez des groupes d'abonnement et configurez le **bloc intelligent** d'abonnement (voir la section suivante). Pour le flux de configuration complet, consultez [Créer un centre de préférences e-mail par glisser-déposer]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center).

### Titre et paragraphe

Ajoute du texte de titre ou de corps avec des options de texte enrichi.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Bouton

Ajoute un bouton cliquable (par exemple **Enregistrer** ou navigation).

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

### Image

Affiche une image depuis la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) ou une URL.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

### Espacement

Ajoute un espacement vertical entre les blocs.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Groupes d'abonnement (bloc intelligent) {#subscription-groups-smart-block}

Ajoute un bloc modèle qui liste les groupes d'abonnement, des contrôles optionnels **S'abonner à tous** / **Se désabonner de tous**, et des descriptions. Configurez-le après avoir ajouté des groupes dans le flux du centre de préférences.

Après avoir [ajouté des groupes d'abonnement]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#step-3-add-subscription-groups-to-the-preference-center), sélectionnez le bloc intelligent dans le canevas pour :

- Réorganiser les groupes d'abonnement
- Ajouter ou supprimer des groupes
- Ajouter ou supprimer des descriptions
- Activer ou désactiver **S'abonner à tous** et **Se désabonner de tous** pour les groupes de ce bloc

Le contrôle **Se désabonner de tous** en bas du modèle par défaut est obligatoire et effectue un [désabonnement global]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) des e-mails.

## Bon à savoir

- **Styles communs :** Vous pouvez définir des valeurs par défaut à l'échelle de la page sous **Styles communs** avant d'ajuster les blocs individuels. Pour plus d'informations, consultez [Personnaliser le centre de préférences à l'aide de l'éditeur par glisser-déposer]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#step-4-customize-the-preference-center-using-the-drag-and-drop-editor).
- **Page de confirmation :** Basculez vers **Page de confirmation** en haut de l'éditeur pour styliser l'expérience post-enregistrement en utilisant les mêmes types de blocs.

{% endsdktab %}

{% endsdktabs %}