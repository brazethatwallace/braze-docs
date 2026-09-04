## Blocs éditeur d'e-mail {#email-editor-blocks}

Les blocs éditeur se trouvent dans la section **Contenu** pour les messages e-mail. Faites glisser un bloc à l'intérieur d'une colonne dans l'**éditeur par glisser-déposer** ; il s'ajuste automatiquement à la largeur de la colonne.

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
| Graisse de police | L'épaisseur globale de la police. |
| Taille de police | Détermine la taille de votre texte. |
| Couleur du texte | Modifie la couleur du titre. |
| Couleur du lien | Modifie la couleur du lien. |
| Alignement | Déplace le titre pour un alignement à gauche, au centre ou à droite. |
| Hauteur de ligne | Modifie la distance entre les lignes de texte. |
| Espacement des lettres | Modifie la distance entre chaque caractère. |
| Direction du texte | Par défaut de gauche à droite, mais peut être modifié en [droite à gauche]({{site.baseurl}}/right_to_left_messages). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Titre" }

### Paragraphe {#paragraph}

Permet de saisir du texte dans le message. Une barre d'outils facilite la mise en forme de la police et du texte.

| Propriété | Description |
|---|---|
| Famille de polices | Le style de police pour le texte de votre paragraphe. |
| Graisse de police | L'épaisseur globale de la police. |
| Taille de police | Détermine la taille de votre texte. |
| Couleur du texte | Modifie la couleur du texte. |
| Couleur du lien | Modifie la couleur du lien. |
| Alignement | Déplace le texte pour un alignement à gauche, au centre ou à droite. |
| Espacement des paragraphes | Modifie l'espace entre les paragraphes. |
| Hauteur de ligne | Modifie la distance entre les lignes de texte. |
| Espacement des lettres | Modifie la distance entre chaque caractère. |
| Direction du texte | Par défaut de gauche à droite, mais peut être modifié en [droite à gauche]({{site.baseurl}}/right_to_left_messages). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paragraphe" }

### Liste {#list}

Ajoute une liste à puces.

| Propriété | Description |
|---|---|
| Type de liste | Le type de liste. Peut être à puces ou numérotée. |
| Style de liste | Détermine le style de votre liste. |
| Commencer la liste à partir de | Détermine le numéro de départ de votre liste. |
| Famille de polices | Le style de police pour le texte de votre paragraphe. |
| Graisse de police | L'épaisseur globale de la police. |
| Taille de police | Détermine la taille de votre texte. |
| Couleur du texte | Modifie la couleur du texte. |
| Couleur du lien | Modifie la couleur du lien. |
| Alignement | Déplace le texte pour un alignement à gauche, au centre ou à droite. |
| Espacement des éléments de liste | Modifie l'espace entre les éléments de la liste. |
| Indentation des éléments de liste | Modifie l'indentation des éléments de la liste. |
| Hauteur de ligne | Modifie la distance entre les lignes de texte. |
| Espacement des lettres | Modifie la distance entre chaque caractère. |
| Direction du texte | Par défaut de gauche à droite, mais peut être modifié en [droite à gauche]({{site.baseurl}}/right_to_left_messages). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liste" }

### Bouton {#button}

Ajoute un bouton standard. Les propriétés permettent de modifier le style et de définir le comportement du lien.

| Propriété | Description |
|---|---|
| Options du bouton | Définit les différentes options du bouton, telles que la police, la taille, la largeur, la couleur et l'espacement intérieur. |
| Survol du bouton | Le style du bouton lorsqu'un utilisateur le survole avec une souris ou un pavé tactile. Inclut la couleur d'arrière-plan, la couleur de police et les styles de bordure du bouton. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bouton" }

#### Comportement au clic {#on-click-behavior}

| Propriété | Description |
|---|---|
| Type de lien | Détermine l'action effectuée lors du clic sur le bouton et définit le protocole approprié. |
| URL | Dynamique en fonction du type de lien **Ouvrir une page web**. |
| Destinataire, objet et corps | Pour le type de lien **Envoyer un e-mail**, définit l'adresse e-mail du destinataire, l'objet et le contenu qui seront pré-remplis dans un brouillon d'e-mail lorsque l'utilisateur sélectionne le bouton. |
| Tél | Pour les types de lien **Passer un appel** et **Envoyer un SMS**, définit le numéro de téléphone que l'utilisateur appellera ou auquel il enverra un message lorsqu'il sélectionnera le bouton. |
| Message | Pour le type de lien **Envoyer un SMS**, définit le contenu qui sera pré-rempli dans un brouillon de message SMS lorsque l'utilisateur sélectionne le bouton. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportement au clic" }

### Séparateur {#divider}

Insère une ligne continue, pointillée ou en tirets pour faciliter l'espacement.

| Propriété | Description |
|---|---|
| Transparent | Si activé, les options de ligne et de largeur sont supprimées. |
| Ligne | Les différents formats de ligne, qu'ils soient pointillés, en tirets ou continus. Vous pouvez également modifier l'épaisseur et la couleur de la ligne de séparation. |
| Largeur | Ajuste l'étendue du séparateur par incréments de 5. |
| Alignement | Déplace la ligne pour un alignement à gauche, au centre ou à droite. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Séparateur" }

### Espaceur {#spacer}

Ajoute de l'espace ou de l'espacement intérieur entre d'autres blocs.

| Propriété | Description |
|---|---|
| Hauteur | Ajuste la hauteur du bloc espaceur. La valeur par défaut est de 60 px. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Espaceur" }

### Image

Insère une image depuis la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library). Pour les images dynamiques (images avec Liquid ou contenu connecté), vous devez définir une image de secours pour utiliser les paramètres de largeur automatique. Pour les spécifications d'image, consultez les [spécifications des images d'e-mail]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications#email).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

| Propriété | Description |
|---|---|
| Largeur automatique | Modifie la largeur de l'image en pixels. |
| Alignement | Définit l'alignement de l'image à gauche, au centre ou à droite dans le bloc. |
| Image avec Liquid | Utilisez la logique [Liquid]({{site.baseurl}}/liquid) pour afficher dynamiquement différentes images dans le même bloc de contenu. |
| URL | Définit une image à l'aide de l'adresse de son hébergement. |
| Texte alternatif | Une brève description de l'image qui fournit aux utilisateurs les mêmes informations que l'image. Essentiel pour l'accessibilité des lecteurs d'écran ou lorsque l'image ne se charge pas. |
| Image aux coins arrondis | Affiche l'image avec des coins arrondis. Par défaut, les images sont affichées avec des coins carrés. |
| Action | Déclenche une action lorsque l'utilisateur clique sur l'image. |
| Options du bloc | Définit l'espacement intérieur autour du bloc image. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image" }

{% alert tip %}
Pour la **largeur automatique**, le redimensionnement automatique des images choisit la meilleure taille pour l'image en fonction d'une combinaison de la largeur de l'image et de l'espace disponible dans la mise en page :
- Les images plus larges que l'espace disponible sont définies à 100 % de la largeur et conservent ce ratio sur mobile, utilisant toute la largeur d'affichage de l'appareil.
- Les images plus petites que l'espace disponible utilisent la taille naturelle de l'image pour éviter les effets de distorsion ou les images floues.
{% endalert %}

#### Comportement du bouton de téléchargement Gmail {#gmail-download-button-behavior}

Gmail ajoute automatiquement un bouton de téléchargement aux images qui n'ont pas de lien hypertexte (`href`) associé. Toutefois, si le rapport hauteur/largeur de l'image est de 299 x 524 px ou moins, Gmail n'affichera pas le bouton de téléchargement.

Pour empêcher le bouton de téléchargement d'apparaître sur les images plus grandes, vous pouvez appliquer la solution de contournement avec le lien « # » :

1. Sélectionnez le bloc **Image**.
2. Dans le panneau **Options du bloc**, accédez à la section **Lien**.
3. Définissez le **Type de lien** sur **Ouvrir une page web**.
4. Saisissez un signe dièse (`#`) dans le champ **URL**.

L'ajout de ce lien empêche Gmail d'afficher le bouton de téléchargement sans affecter l'expérience utilisateur.

### Vidéo {#video}

Crée un lien vers du contenu vidéo. Seuls YouTube et Vimeo sont pris en charge.

| Propriété | Description |
|---|---|
| URL | L'URL de la vidéo. |
| Titre | Généré automatiquement à partir des métadonnées de la vidéo ou peut être personnalisé. |
| Style de l'icône de lecture | Inclut différentes options pour le bouton de lecture situé en haut de l'image vidéo. |
| Couleur de l'icône de lecture | Option pour sélectionner **Clair** ou **Sombre** pour le bouton de lecture. |
| Taille de l'icône de lecture | Choisissez la taille en pixels du bouton de lecture. Plage prédéfinie de 50&nbsp;px à 80&nbsp;px (incrémentée de 5&nbsp;px). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vidéo" }

{% alert tip %}
Les vidéos hébergées par Vimeo ne fonctionnent que si elles sont définies comme publiques. Tous les autres paramètres de sécurité disponibles dans Vimeo (par exemple, « Masquer de Vimeo.com ») génèrent un format de lien différent qui n'est pas pris en charge par ce bloc de contenu. Ces types de liens sont modifiés par le générateur, ce qui empêche Braze de générer une vignette.
{% endalert %}

### Réseaux sociaux {#social}

Insère des icônes de plateformes de réseaux sociaux. Vous pouvez charger des images personnalisées pour des icônes propres à votre marque.

| Propriété | Description |
|---|---|
| Sélectionner la collection d'icônes | Définit le style de votre collection d'icônes. |
| Configurer la collection d'icônes | Définit l'URL pour chaque icône de réseau social. Inclut le basculeur **Plus d'options** pour modifier le titre et le texte alternatif. |
| Alignement | Déplace l'icône de réseau social pour un alignement à gauche, au centre ou à droite. |
| Espacement des icônes | Détermine l'espacement entre chaque icône de réseau social. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Réseaux sociaux" }

### Icônes {#icons}

Insère une icône. Vous pouvez charger des images personnalisées. Braze utilise une icône de marque substitutive surdimensionnée jusqu'à ce que vous chargiez une image.

| Propriété | Description |
|---|---|
| Famille de polices | Le style de police pour le texte de votre paragraphe. |
| Graisse de police | L'épaisseur globale de la police. |
| Taille de police | Détermine la taille de votre texte. |
| Couleur du texte | Modifie la couleur du titre. |
| Couleur du lien | Modifie la couleur du lien. |
| Alignement | Déplace l'icône pour un alignement à gauche, au centre ou à droite. |
| Espacement des lettres | Modifie la distance entre chaque caractère. |
| Taille de l'icône | Détermine la taille de votre icône. |
| Espacement de l'icône | Modifie l'espacement de l'icône. |
| Espacement intérieur de l'icône | Modifie l'espacement intérieur de l'icône. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Icônes" }

### HTML

Insère du HTML brut. Recommandé pour le [Liquid]({{site.baseurl}}/liquid), comme le contenu connecté ou les instructions conditionnelles.

| Propriété | Description |
|---|---|
| HTML | Ajoutez ou modifiez du HTML brut, y compris le [Liquid]({{site.baseurl}}/liquid) pour la personnalisation ou la logique conditionnelle. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTML" }

### Menu

Crée un menu flexible pour le message que vous concevez.

| Propriété | Description |
|---|---|
| Configurer les éléments du menu | Ajoutez un élément de menu. |
| Famille de polices | Le style de police pour le menu. |
| Taille de police | La taille de votre menu. |
| Couleur du texte | Modifie la couleur du menu. |
| Couleur du lien | Modifie la couleur du texte du menu. |
| Alignement | Déplace le menu pour un alignement à gauche, au centre ou à droite. |
| Espacement des lettres | Modifie la distance entre chaque caractère. |
| Disposition | Détermine si la disposition est horizontale ou verticale. |
| Séparateur | Ajoute un ou plusieurs caractères entre les options du menu. |
| Menu mobile | Inclut des options pour modifier la taille, la couleur et le type de l'icône lorsqu'elle est affichée sur un appareil mobile. |
| Espacement intérieur des éléments | Modifie l'espacement intérieur en utilisant le bouton **+** ou **-**, ou en saisissant un nombre spécifique. |
| Tous les côtés | Définit un espacement intérieur uniforme si l'espacement intérieur des éléments est désactivé. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Menu" }

### Produit {#product}

Affiche des lignes de produits à partir d'un [catalogue de produits]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks), soit en tant qu'éléments statiques issus d'une sélection de catalogue (jusqu'à 12), soit en tant que produits dynamiques alimentés par un [déclencheur eCommerce Canvas]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases) (jusqu'à 24).

| Propriété | Description |
| --- | --- |
| Type de contenu | Définit si les produits proviennent d'une **sélection** fixe de catalogue (**Statique**, jusqu'à 12 produits) ou d'un déclencheur de recommandation eCommerce Canvas (**Dynamique**, jusqu'à 24 produits). **Dynamique** n'est disponible que dans les étapes de message Canvas. |
| Catalogue | Sélectionne le catalogue de produits qui fournit les données et les mappages de champs des produits. |
| Sélection | *(Statique uniquement)* Sélectionne le jeu filtré du catalogue définissant les produits affichés. |
| Afficher les détails de la source | Active le texte d'aide indiquant le champ du catalogue ou de l'événement sous-jacent mappé à chaque champ de produit. |
| Image de variante | Affiche ou masque l'image de variante pour chaque tuile de produit. |
| Titre du produit | Affiche ou masque le titre du produit pour chaque tuile. |
| Prix | Affiche ou masque le prix du produit. |
| Bouton pour l'URL du produit | Affiche ou masque un bouton d'appel à l'action renvoyant vers l'URL du produit. |
| Quantité | *(Dynamique, Canvas uniquement, lorsque le déclencheur d'entrée n'est pas un événement de consultation de produit)* Affiche ou masque la quantité du produit provenant de l'événement déclencheur. |
| Orientation du produit | Définit la position de l'image dans chaque tuile : **Image à gauche**, **Image au centre** ou **Image à droite**. |
| Alignement | Définit l'alignement horizontal du contenu dans chaque tuile. |
| Nombre max de produits par ligne | Définit le nombre de produits affichés par ligne : **1**, **2** ou **3** (**3** n'est disponible que lorsque l'orientation est **Image au centre**). |
| Espacement des produits | Définit l'espacement entre les produits : **Automatique** ou **Personnalisé**. |
| Espacement personnalisé | *(Lorsque **Personnalisé** est sélectionné)* Définit l'écart en pixels entre les produits. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Produit" }

## Personnalisation {#personalization}

Vous pouvez ajouter de la personnalisation à votre e-mail en utilisant Liquid ou le contenu connecté.

- **Liquid :** Sous **Content** > **Personalization**, sélectionnez un attribut, copiez l'extrait de code et collez-le dans un bloc Title, Paragraph ou List (Liquid de base) ou dans un bloc HTML (Liquid avancé). De manière générale, bien que vous puissiez utiliser du Liquid de base dans les blocs Title, Paragraph et List, nous recommandons d'utiliser des blocs HTML pour les logiques plus complexes afin d'éviter les problèmes de mise en page. Notez que Liquid n'est pas pris en charge dans les blocs image ni dans les champs d'URL des boutons.
- **[Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) :** Ajoutez un bloc **HTML** et placez-y votre appel {% raw %}`{% connected_content %}`{% endraw %}.