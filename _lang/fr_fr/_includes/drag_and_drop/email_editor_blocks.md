## Utilisation des blocs éditeurs d'e-mails {#using-email-editor-blocks}

Les blocs éditeurs se trouvent dans la section **Contenu** des messages e-mail. Pour utiliser un bloc éditeur, glissez-le à l'intérieur d'une colonne dans l'éditeur par glisser-déposer. Il s'ajuste automatiquement à la largeur de la colonne. Chaque bloc éditeur possède ses propres paramètres, comme le contrôle granulaire de la marge intérieure.

Pour en savoir plus sur l'utilisation et la personnalisation de ces blocs éditeurs dans vos e-mails, consultez la section [Autres personnalisations]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/#other-customizations).

{% alert tip %}
Vous pouvez également ajouter des [attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/) à n'importe quelle URL dans les blocs éditeurs `Image`, `Button` ou `Text`.
{% endalert %}

## Types {#types}

Le tableau suivant décrit comment les utilisateurs peuvent exploiter chaque type de bloc éditeur.

| Nom | Description |
|---|---|
|Titre| Ajoute du texte pour les en-têtes dans l'e-mail. |
|Paragraphe| Permet de saisir du texte dans le message. Une barre d'outils facilite la mise en forme des polices et du texte. |
|Liste| Ajoute une liste à puces. |
|Bouton| Ajoute un bouton standard. Les propriétés de ce bloc permettent de modifier et de configurer facilement les liens. |
|Ligne de séparation| Insère une ligne continue, en pointillés ou en tirets pour faciliter l'espacement.|
|Espaceur| Ajoute de l'espace, ou une « marge intérieure », entre les autres blocs. |
|Image| Insère une image provenant de la [bibliothèque multimédia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). |
|Vidéo| Crée un lien vers le contenu vidéo. |
|Réseaux sociaux| Insère l'icône d'une plateforme de réseaux sociaux. Vous pouvez télécharger des images personnalisées pour les icônes spécifiques à votre marque. |
|Icônes| Insère une icône. Vous pouvez télécharger des images personnalisées. Braze utilise une icône de marque substitutive surdimensionnée jusqu'à ce que vous téléchargiez une image. |
|HTML| Insère du HTML brut. Recommandé pour [Liquid]({{site.baseurl}}/liquid/), comme le contenu connecté ou les instructions conditionnelles. |
|Menu| Crée un menu flexible pour le message que vous concevez. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Personnalisation dans les e-mails {#personalization-in-email}

- **Liquid :** Sous **Contenu** > **Personnalisation**, sélectionnez un attribut, copiez l'extrait de code et collez-le dans un bloc de texte (Liquid de base) ou un bloc HTML (Liquid avancé). De manière générale, bien que vous puissiez utiliser du Liquid de base dans les blocs de texte, nous recommandons d'utiliser les blocs HTML pour les logiques plus complexes afin d'éviter les problèmes de mise en page. Notez que Liquid n'est pas pris en charge dans les blocs d'image ni dans les champs d'URL des boutons.
- **Contenu connecté :** Ajoutez un bloc **HTML** et placez-y votre appel {% raw %}`{% connected_content %}`{% endraw %}.

## Propriétés {#properties}

Les détails des propriétés de chaque bloc éditeur sont fournis dans les tableaux suivants.

### Titre {#title}
Reportez-vous au tableau suivant pour plus de détails sur les propriétés du bloc éditeur `Title`.

| Propriétés | Description |
|---|---|
|Titre| Sélectionne le style de titre. |
|Famille de polices| Le style de police de votre titre. |
|Graisse de la police| L'épaisseur globale de la police. |
|Taille de police| Détermine la taille de votre texte. |
|Couleur du texte| Modifie la couleur du titre. |
|Couleur du lien| Modifie la couleur du lien. |
|Alignement| Déplace le titre vers la gauche, le centre ou la droite. |
|Hauteur de ligne| Modifie l'espace entre les lignes de texte. |
|Espacement des lettres| Modifie l'espace entre chaque caractère. |
|Sens du texte| Par défaut de gauche à droite, mais peut être modifié pour être [de droite à gauche]({{site.baseurl}}/right_to_left_messages/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paragraphe {#paragraph}

Reportez-vous au tableau suivant pour plus de détails sur les propriétés du bloc éditeur `Paragraph`.

| Propriétés | Description |
|---|---|
|Famille de polices| Le style de police de votre paragraphe. |
|Graisse de la police| L'épaisseur globale de la police. |
|Taille de police| Détermine la taille de votre texte. |
|Couleur du texte| Modifie la couleur du texte. |
|Couleur du lien| Modifie la couleur du lien. |
|Alignement| Déplace le texte vers la gauche, le centre ou la droite. |
|Espacement des paragraphes| Modifie l'espace entre les paragraphes. |
|Hauteur de ligne| Modifie l'espace entre les lignes de texte. |
|Espacement des lettres| Modifie l'espace entre chaque caractère. |
|Sens du texte| Par défaut de gauche à droite, mais peut être modifié pour être [de droite à gauche]({{site.baseurl}}/right_to_left_messages/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Liste {#list}

Reportez-vous au tableau suivant pour plus de détails sur les propriétés du bloc éditeur `List`.

| Propriétés | Description |
|---|---|
|Type de liste| Le type de liste. Peut être à puces ou numérotée. |
|Style de liste| Détermine le style de votre liste. |
|Commencer la liste à partir de| Détermine le numéro de départ de votre liste. |
|Famille de polices| Le style de police de votre texte. |
|Graisse de la police| L'épaisseur globale de la police. |
|Taille de police| Détermine la taille de votre texte. |
|Couleur du texte| Modifie la couleur du texte. |
|Couleur du lien| Modifie la couleur du lien. |
|Alignement| Déplace le texte vers la gauche, le centre ou la droite. |
|Espacement des éléments de liste| Modifie l'espace entre les éléments de liste. |
|Indentation des éléments de liste| Modifie l'indentation des éléments de liste. |
|Hauteur de ligne| Modifie l'espace entre les lignes de texte. |
|Espacement des lettres| Modifie l'espace entre chaque caractère. |
|Sens du texte| Par défaut de gauche à droite, mais peut être modifié pour être [de droite à gauche]({{site.baseurl}}/right_to_left_messages/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Ligne de séparation {#divider}

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur `Divider`.

| Propriétés | Description |
|---|---|
|Transparent| Si activé, les options « ligne » et « largeur » sont supprimées. |
|Ligne| Les différents formats de lignes : pointillés, tirets ou trait continu. Vous pouvez également modifier l'épaisseur et la couleur de la ligne de séparation. |
|Largeur| Ajuste l'étendue de la ligne de séparation par incréments de 5. |
|Alignement| Déplace la ligne vers la gauche, le centre ou la droite. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Espaceur {#spacer}

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur `Spacer`.

| Propriétés | Description |
|---|---|
|Hauteur| Ajuste la hauteur du bloc d'espacement. La valeur par défaut est 60 px.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image {#image}

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur `Image`. Pour les images dynamiques (images avec Liquid ou contenu connecté), vous devez définir une image de secours afin d'utiliser les paramètres de largeur automatique. Pour les spécifications relatives aux images, consultez nos [spécifications relatives aux images dans les e-mails]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/image_specs/#email).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

| Propriétés | Description |
|---|---|
|Largeur automatique| Modifie la largeur de l'image en pixels. |
|Alignement| Oriente l'image vers la gauche, le centre ou la droite du bloc. |
|Image avec Liquid| Utilisez la logique [Liquid]({{site.baseurl}}/liquid/) pour définir dynamiquement différentes images au sein d'un même bloc de contenu. |
|URL| Définissez une image en utilisant l'adresse de l'endroit où elle est hébergée. |
|Texte alternatif| Une courte description de l'image qui fournit aux utilisateurs les mêmes informations que celles présentées dans l'image. Essentiel pour l'accessibilité des lecteurs d'écran ou lorsque l'image ne parvient pas à se charger. |
|Image aux coins arrondis| Affiche l'image avec des coins arrondis. Par défaut, les images sont affichées avec des coins carrés. |
|Action| Déclenche une action lorsque l'utilisateur clique sur l'image.|
|Options du bloc| Définit la marge intérieure autour du bloc d'image. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Pour `Auto Width`, le redimensionnement automatique choisit la meilleure taille pour l'image en combinant la largeur de l'image et l'espace disponible dans la mise en page :
- Les images plus larges que l'espace disponible seront définies à 100 % de largeur et conserveront ce ratio sur mobile, utilisant ainsi toute la largeur de l'écran de l'appareil.
- Les images plus petites que l'espace disponible utiliseront leur taille naturelle pour éviter les effets de distorsion ou les images floues.
{% endalert %}

### Vidéo {#video}

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur `Video`.

| Propriétés | Description |
|---|---|
|URL| L'URL de la vidéo. Notez que seuls YouTube et Vimeo sont pris en charge. |
|Titre| Généré automatiquement à partir des métadonnées de la vidéo ou peut être personnalisé. |
|Style de l'icône de lecture| Propose différentes options pour le bouton de lecture situé en haut d'une image vidéo. |
|Couleur de l'icône de lecture| Permet de sélectionner **Clair** ou **Foncé** pour le bouton de lecture. |
|Taille de l'icône de lecture| Choisissez la taille en pixels du bouton de lecture. Plage prédéfinie de 50&nbsp;px à 80&nbsp;px (par incréments de 5&nbsp;px). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Les vidéos hébergées par Vimeo ne fonctionneront que si elles sont définies comme publiques. Tous les autres paramètres de sécurité disponibles dans Vimeo (par exemple, « Masquer sur Vimeo.com ») génèrent un format de lien différent qui n'est pas pris en charge par ce bloc de contenu. Ces types de liens sont modifiés par le générateur, ce qui empêche Braze de générer une miniature.
{% endalert %}

### Réseaux sociaux {#social}

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur `Social`.

| Propriétés | Description |
|---|---|
|Sélectionner une collection d'icônes| Définit le style de votre collection d'icônes. |
|Configurer la collection d'icônes| Définit l'URL pour chaque icône sociale. Inclut le basculeur **Plus d'options** pour modifier le titre et le texte alternatif. |
|Alignement| Déplace l'icône sociale vers la gauche, le centre ou la droite. |
|Espacement des icônes| Détermine l'espacement entre chaque icône sociale. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Icônes {#icons}

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur `Icons`.

| Propriétés | Description |
|---|---|
|Famille de polices| Le style de police de votre texte. |
|Graisse de la police| L'épaisseur globale de la police. |
|Taille de police| Détermine la taille de votre texte. |
|Couleur du texte| Modifie la couleur du texte. |
|Couleur du lien| Modifie la couleur du lien. |
|Alignement| Déplace l'icône vers la gauche, le centre ou la droite. |
|Espacement des lettres| Modifie l'espace entre chaque caractère. |
|Taille de l'icône| Détermine la taille de votre icône. |
|Espacement des icônes| Modifie l'espacement de l'icône. |
|Marge intérieure de l'icône| Modifie la marge intérieure de l'icône. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### HTML {#html}

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur `HTML`.

| Propriétés | Description |
|---|---|
|Éditeur HTML| Saisissez le HTML brut. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Menu {#menu}

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur `Menu`.

| Propriétés | Description |
|---|---|
|Configurer les éléments du menu| Ajoute un élément de menu. |
|Famille de polices| Le style à utiliser pour votre menu. |
|Taille de police| La taille de votre menu. |
|Couleur du texte| Modifie la couleur du menu. |
|Couleur du lien| Modifie la couleur du texte du menu. |
|Alignement| Déplace le menu vers la gauche, le centre ou la droite. |
|Espacement des lettres| Modifie l'espace entre chaque caractère. |
|Disposition| Détermine si la mise en page est horizontale ou verticale. |
|Séparateur| Ajoute un ou plusieurs caractères entre les options de menu. |
|Menu mobile| Propose des options pour modifier la taille, la couleur et le type d'icône sur un appareil mobile. |
|Marge intérieure des éléments| Modifie la marge intérieure en utilisant le bouton **+** ou **-**, ou en saisissant un nombre spécifique. |
|Tous les côtés| Définit une marge intérieure uniforme si la marge intérieure des éléments est désactivée. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Actions {#actions}

Vous pouvez affecter une action qui se déclenche lorsqu'un utilisateur appuie sur un bouton, un lien ou une image dans le message. Vous pouvez également utiliser [Liquid]({{site.baseurl}}/liquid/) pour personnaliser les actions. Les tableaux suivants détaillent les actions de chaque bloc éditeur.

### Bouton {#button}

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur `Button`.

| Propriétés | Description |
|---|---|
|Type de lien| Détermine l'action effectuée lors du clic sur le bouton et définit le protocole approprié. |
|URL| Dynamique selon le type de lien **Ouvrir la page Web**.|
|Destinataire, Objet et Corps du message| Pour le type de lien **Envoyer un e-mail**, définit l'adresse e-mail du destinataire, l'objet et le contenu qui seront pré-remplis dans un brouillon d'e-mail lorsque l'utilisateur sélectionne le bouton.|
|Tél.| Pour les types de lien **Passer un appel** et **Envoyer un SMS**, définit le numéro de téléphone que l'utilisateur appellera ou auquel il enverra un SMS en sélectionnant le bouton.|
|Message| Pour le type de lien **Envoyer un SMS**, définit le contenu qui sera pré-rempli dans un brouillon de SMS lorsque l'utilisateur sélectionne le bouton.|
|Options du bouton| Définit diverses options du bouton, telles que la police, la largeur, la couleur et autres.|
|Bouton au survol| Le style du bouton lorsqu'un utilisateur le survole avec une souris ou un trackpad. Cela inclut la couleur d'arrière-plan du bouton, la couleur de la police et les styles de bordure.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }