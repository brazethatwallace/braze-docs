---
nav_title: "Paramètres de style globaux des e-mails"
article_title: "Paramètres de style globaux des e-mails"
alias: "/dnd/global_style_settings/"
channel: email
page_order: 3
description: "Cet article de référence explique comment définir les paramètres de style globaux des e-mails dans l'éditeur par glisser-déposer pour vos campagnes et Canvas."
tool:
  - Campaigns
  - Canvas
---

# Paramètres de style globaux des e-mails {#email-global-style-settings}

> Les paramètres de style globaux vous permettent de personnaliser l'apparence de vos campagnes e-mail et Canvas. Vous pouvez ajouter et personnaliser un thème par défaut pour votre éditeur par glisser-déposer. Cela inclut la modification de vos styles pour les titres d'e-mails, le texte, les boutons, et bien plus encore. L'utilisation combinée de ces paramètres peut vous aider à créer une apparence cohérente dans l'ensemble de vos envois de messages par e-mail.

Pour modifier vos paramètres de style globaux, accédez à **Paramètres** > **Préférences des e-mails** > **Préférences des e-mails par glisser-déposer**. Après avoir modifié les styles dans l'éditeur d'e-mails par glisser-déposer, sélectionnez **Enregistrer**. Pour personnaliser davantage vos campagnes e-mail et Canvas, découvrez comment intégrer les [blocs de l'éditeur (e-mail)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email).

![Section des paramètres de style globaux des e-mails dans l'onglet des paramètres de l'éditeur d'e-mails par glisser-déposer.]({% image_buster /assets/img_archive/dnd_global_style_settings.png %})

{% alert note %}
Les modifications apportées aux paramètres de style globaux s'appliqueront à toutes les futures campagnes e-mail et Canvas.
{% endalert %}

## Style de base {#basic-styling}

Pour le **Style de base**, vous pouvez définir les couleurs d'arrière-plan par défaut de l'e-mail et du contenu pour vos campagnes e-mail et Canvas. Vous pouvez également sélectionner une police par défaut, ajouter une police personnalisée et modifier les couleurs des liens.

![Options de style de base incluant des options pour modifier les couleurs d'arrière-plan de l'e-mail et du contenu, le nom de la police par défaut et la couleur de lien par défaut.]({% image_buster /assets/img_archive/dnd_basic_styling.png %})

## Police personnalisée {#custom-font}

Les polices personnalisées vous permettent d'ajouter manuellement une police web pour assurer la cohérence de votre image de marque sur les différentes plateformes de messagerie. Vous pouvez ajouter une police personnalisée pour chaque section de style.

### Prérequis {#requirements}

Avant d'ajouter une police personnalisée, vérifiez que le fichier de police personnalisée répond aux exigences suivantes :

- Le CORS doit être activé sur le serveur qui fournit le fichier de police personnalisée. Cela est généralement géré par votre équipe informatique.
  - Le fichier de police personnalisée doit comporter l'en-tête : `Access-Control-Allow-Origin: *`
- L'URL du fichier doit pointer vers un fichier CSS (et non WOFF ou OTF).
- Le nom de la police personnalisée doit correspondre au nom de la police défini dans le fichier CSS.

Notez que le fournisseur de polices personnalisées peut collecter des données personnelles auprès de vos destinataires. Nous vous recommandons de consulter les politiques de votre fournisseur de polices avant utilisation.

### Ajouter une police personnalisée {#adding-a-custom-font}

Pour ajouter une police personnalisée, procédez comme suit :

1. Dans la section **Nom de la police par défaut** du **Style de base**, sélectionnez **Ajouter une police personnalisée**.
2. Dans le champ **Nom de la police**, saisissez le même nom de police que celui qui apparaît dans votre fichier source de police personnalisée. Assurez-vous que ce nom respecte les majuscules et les espaces.
3. Saisissez l'URL correspondante dans le champ **URL de la police**.
4. Vérifiez que la prévisualisation affiche votre police personnalisée.
5. Sélectionnez **Enregistrer** pour utiliser la police personnalisée comme police par défaut de vos e-mails.

{% alert important %}
Gmail ne prend pas en charge les polices personnalisées, votre police personnalisée peut donc s'afficher comme une police système par défaut. Pour les autres plateformes de messagerie, vérifiez que votre police personnalisée s'affiche correctement avant d'envoyer vos e-mails.
{% endalert %}

Pour utiliser d'autres polices personnalisées dans vos campagnes e-mail, vous pouvez créer un [modèle d'e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template) ou des [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) incluant la police personnalisée. Par exemple, vous pouvez créer un modèle d'e-mail spécifique conçu avec des polices personnalisées festives adaptées à votre thème de promotion. Assurez-vous de vérifier que votre choix de police est compatible avec le web et pris en charge par vos plateformes de messagerie.

### Police de secours {#fallback-font}

Les polices de secours sont utilisées pour le titre, l'en-tête et le corps du texte lorsque votre police par défaut n'est pas prise en charge par le fournisseur de boîte de réception ou le système d'exploitation. Par défaut, Braze définit automatiquement Arial comme police de secours lorsque les paramètres de style globaux sont enregistrés. Vous avez également la possibilité d'ajouter des polices serif ou sans serif comme options pour votre famille de polices par défaut.

![Exemple avec « Arial » comme police de secours et « Sans-serif » comme famille de polices.]({% image_buster /assets/img_archive/dnd_fallbacks.png %})

Vous pouvez ajouter jusqu'à 17 polices de secours. La première police de secours sélectionnée sera celle utilisée en priorité. La police de secours ne sera appliquée qu'aux modèles, campagnes e-mail et composants Canvas nouvellement créés. La police de secours n'est pas automatiquement définie pour les messages créés avant la spécification de la police de secours. Nous vous recommandons vivement de sélectionner des polices de secours similaires à celles de vos e-mails afin de maintenir la cohérence de votre image de marque.

## Style des titres {#title-styling}

Ici, vous pouvez ajuster les styles de vos titres d'e-mails en modifiant la taille de la police, la couleur de la police et l'alignement du texte.

![Paramètres de style des titres pour un en-tête principal et un en-tête secondaire alignés au centre.]({% image_buster /assets/img_archive/dnd_title_styling.png %})

Vous pouvez éventuellement remplacer le style par défaut de votre thème d'éditeur par glisser-déposer. Sélectionnez **Remplacer le style par défaut** pour appliquer votre choix de style de titre. Cela peut inclure la définition d'une police et d'une couleur de lien différentes.

## Style des paragraphes {#paragraph-styling}

Pour définir un style de paragraphe par défaut, accédez à **Style des paragraphes**, saisissez la **Taille de la police** et sélectionnez **Couleur de la police** pour choisir une couleur de police. Vous pouvez également ajuster le style du bloc pour le corps du texte en modifiant les valeurs **Marge intérieure haute**, **Marge intérieure droite**, **Marge intérieure basse** et **Marge intérieure gauche**. Cela s'appliquera à l'espacement autour des quatre zones entourant le bloc de paragraphe.

![Paramètres de style des paragraphes pour un texte avec une police de 14 pt.]({% image_buster /assets/img_archive/dnd_paragraph_styling.png %})

## Style des listes {#list-styling}

Lorsque vous ajoutez des listes à vos messages, la section **Style des listes** assure la cohérence du style de vos listes. Cela inclut des détails tels que :

- Taille de la police
- Couleur de la police
- Graisse de la police
- Hauteur de ligne
- Alignement
- Direction du texte
- Espacement des lettres
- Espacement des éléments de liste
- Retrait des éléments de liste
- Type de liste
- Style du type de liste

Vous pouvez définir le **Type de liste** comme numéroté ou à puces. Le **Style du type de liste** offre une personnalisation supplémentaire du style de vos listes. Par exemple, vous pouvez définir les types de liste pour qu'ils soient toujours à puces et que chaque puce soit un carré.

![Paramètres de style des listes pour une liste à puces.]({% image_buster /assets/img_archive/dnd_list_styling.png %})

## Style des boutons {#button-styling}

Dans la section **Style des boutons**, vous pouvez modifier les styles par défaut suivants pour le bouton :
- Couleur d'arrière-plan
- Taille de la police
- Couleur de la police
- Rayon de bordure
- Couleur de bordure
- Épaisseur de bordure
- Marge intérieure du bouton

![Paramètres de style des boutons pour un bouton rectangulaire avec un arrière-plan bleu.]({% image_buster /assets/img_archive/dnd_button_styling.png %})

Comme pour toutes les autres sections de style, vous pouvez ajuster le style du bloc en modifiant les valeurs **Marge intérieure haute**, **Marge intérieure droite**, **Marge intérieure basse** et **Marge intérieure gauche**.

## Largeur du modèle d'e-mail {#email-template-width}

La largeur du modèle d'e-mail vous permet d'ajuster et de définir une largeur pour assurer la cohérence de vos campagnes e-mail.

![Largeur du modèle d'e-mail définie à 600 px.]({% image_buster /assets/img_archive/dnd_email_template_width.png %})

## Largeur des Content Blocks {#content-block-width}

Ce paramètre sera préconfiguré pour tous les futurs Content Blocks. Les Content Blocks existants ne seront pas mis à jour. Vous pouvez définir tous les Content Blocks à 100 %, en respectant la largeur à l'endroit où un Content Block est inséré, ou définir une valeur spécifique en pixels.

Nous recommandons de faire correspondre la largeur des Content Blocks à la largeur du modèle d'e-mail.

![Largeur des Content Blocks définie à 600 px.]({% image_buster /assets/img_archive/dnd_content_block_width_update.png %})