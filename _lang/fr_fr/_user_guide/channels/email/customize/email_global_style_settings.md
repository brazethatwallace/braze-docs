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

Pour le **Basic Styling**, vous pouvez définir les couleurs d'arrière-plan par défaut de l'e-mail et du contenu pour vos Campaigns et Canvas. Vous pouvez également sélectionner une police par défaut, ajouter une police personnalisée et modifier les couleurs des liens.

![Options de style de base incluant les options de modification des couleurs d'arrière-plan de l'e-mail et du contenu, du nom de la police par défaut et de la couleur de lien par défaut.]({% image_buster /assets/img_archive/dnd_basic_styling.png %})

## Police personnalisée {#custom-font}

Avec les polices personnalisées, vous pouvez ajouter manuellement une police web pour assurer la cohérence de votre image de marque sur les différentes plateformes d'e-mail. Vous pouvez ajouter une police personnalisée pour chaque section de style.

{% alert note %}
Les paramètres de graisse (font-weight) dans le CSS sont ignorés. Sélectionnez plutôt l'une des graisses prédéfinies lors de la composition du message.
{% endalert %}

### Conditions requises {#requirements}

Avant d'ajouter une police personnalisée, vérifiez que le fichier de police personnalisée répond aux exigences suivantes :

- Le CORS doit être activé sur le serveur qui fournit le fichier de police personnalisée. Cela est généralement géré par votre équipe informatique.
  - Le fichier de police personnalisée doit comporter l'en-tête : `Access-Control-Allow-Origin: *`
- L'URL du fichier doit pointer vers un fichier CSS (et non WOFF ou OTF).
- Le nom de la police personnalisée doit correspondre au nom de la police (font face) dans le fichier CSS.

{% alert important %}
Le fournisseur de polices personnalisées peut collecter des données personnelles de vos destinataires. Nous vous recommandons de consulter les politiques de votre fournisseur de polices avant toute utilisation.
{% endalert %}

### Ajouter une police personnalisée {#adding-a-custom-font}

Pour ajouter une police personnalisée, procédez comme suit :

1. Dans la section **Default Font Name** de **Basic Styling**, sélectionnez **Add a custom font**.
2. Dans le champ **Font Name**, saisissez le même nom de police que celui qui apparaît dans votre fichier source de police personnalisée. Assurez-vous que ce nom est correctement mis en majuscule et espacé.
3. Saisissez l'URL correspondante dans le champ **Font URL**.
4. Vérifiez que l'aperçu affiche votre police personnalisée.
5. Sélectionnez **Save** pour utiliser la police personnalisée comme police d'e-mail par défaut.

{% alert important %}
Gmail ne prend pas en charge les polices personnalisées, de sorte que votre police personnalisée peut s'afficher comme une police système par défaut. Pour les autres plateformes d'e-mail, vérifiez que votre police personnalisée s'affiche correctement avant d'envoyer vos communications par e-mail.
{% endalert %}

Pour utiliser d'autres polices personnalisées dans vos Campaigns par e-mail, vous pouvez créer un [modèle d'e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template) ou des [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) qui incluent la police personnalisée. Par exemple, vous pouvez créer un modèle d'e-mail spécifique conçu avec des polices personnalisées festives adaptées au thème de vos promotions. Assurez-vous de vérifier que la police choisie est compatible avec le web et prise en charge par vos plateformes d'e-mail.

### Police de substitution {#fallback-font}

Les polices de substitution sont utilisées pour le titre, l'en-tête et le corps du texte lorsque votre police par défaut n'est pas prise en charge par le fournisseur de boîte de réception ou le système d'exploitation. Par défaut, Braze définit automatiquement Arial comme police de substitution lorsque les paramètres de style globaux sont enregistrés. Vous avez également la possibilité d'ajouter des options serif ou sans-serif pour votre famille de polices par défaut.

![Un exemple avec « Arial » comme police de substitution et « Sans-serif » comme famille de polices.]({% image_buster /assets/img_archive/dnd_fallbacks.png %})

Vous pouvez ajouter jusqu'à 17 polices de substitution. La première police de substitution sélectionnée sera celle qui sera tentée en premier. La police de substitution ne s'appliquera qu'aux modèles, Campaigns par e-mail et composants Canvas nouvellement créés. La police de substitution n'est pas automatiquement définie pour les messages créés avant la configuration de la police de substitution. Nous vous recommandons vivement de sélectionner des polices de substitution similaires à celles de vos communications par e-mail afin de maintenir la cohérence de votre image de marque.

## Style de titre {#title-styling}

Ici, vous pouvez ajuster les styles des titres de vos e-mails en modifiant la taille de police, la couleur de police et l'alignement du texte.

![Paramètres de style de titre pour un en-tête principal et un en-tête secondaire alignés au centre.]({% image_buster /assets/img_archive/dnd_title_styling.png %})

Vous pouvez également remplacer le style par défaut du thème de votre éditeur par glisser-déposer. Sélectionnez **Remplacer le style par défaut** pour appliquer votre choix de style de titre. Cela peut inclure la définition d'une police et d'une couleur de lien différentes.

## Style de paragraphe {#paragraph-styling}

Pour définir un style de paragraphe par défaut, accédez à **Paragraph Styling**, saisissez la **Font Size** et sélectionnez **Font Color** pour choisir une couleur de police. Vous pouvez également ajuster le style du bloc pour le corps du texte en modifiant les valeurs **Padding Top**, **Padding Right**, **Padding Bottom** et **Padding Left**. Cela s'appliquera à l'espacement autour des quatre zones entourant le bloc de paragraphe.

![Paramètres de style de paragraphe pour le texte avec une police de 14 pt.]({% image_buster /assets/img_archive/dnd_paragraph_styling.png %})

## Style de liste {#list-styling}

Lorsque vous ajoutez des listes à vos messages, la section **List Styling** permet de garantir la cohérence du style de vos listes. Elle inclut des paramètres tels que :

- La taille de police
- La couleur de police
- L'épaisseur de police
- La hauteur de ligne
- L'alignement
- La direction du texte
- L'espacement des lettres
- L'espacement des éléments de liste
- L'indentation des éléments de liste
- Le type de liste
- Le style de type de liste

Vous pouvez définir le **List Type** sur numéroté ou à puces. Le **List Style Type** offre des options de personnalisation supplémentaires pour le style de vos listes. Par exemple, vous pouvez configurer les listes pour qu'elles soient toujours à puces et que chaque puce soit un carré.

![Paramètres de style de liste pour une liste à puces.]({% image_buster /assets/img_archive/dnd_list_styling.png %})

## Style des boutons {#button-styling}

Dans la section **Style des boutons**, vous pouvez modifier les styles par défaut suivants pour le bouton :
- Couleur d'arrière-plan
- Taille de police
- Couleur de police
- Rayon de bordure
- Couleur de bordure
- Épaisseur de bordure
- Espacement intérieur du bouton

![Paramètres de style des boutons pour un bouton rectangulaire avec un arrière-plan bleu.]({% image_buster /assets/img_archive/dnd_button_styling.png %})

Comme pour toutes les autres sections de style, vous pouvez ajuster le style du bloc en modifiant les valeurs **Padding Top**, **Padding Right**, **Padding Bottom** et **Padding Left**.

## Largeur du modèle d'e-mail {#email-template-width}

En utilisant la largeur du modèle d'e-mail, vous pouvez ajuster et définir une largeur pour assurer la cohérence de vos Campaigns d'e-mail.

![Largeur du modèle d'e-mail définie à 600 px.]({% image_buster /assets/img_archive/dnd_email_template_width.png %})

## Largeur des Content Blocks {#content-block-width}

Ce paramètre sera préconfiguré pour tous les futurs Content Blocks. Les Content Blocks existants ne seront pas mis à jour. Vous pouvez définir tous les Content Blocks à 100 %, en respectant la largeur de l'emplacement où un Content Block est inséré, ou définir une valeur spécifique en pixels.

Nous recommandons de faire correspondre la largeur du Content Block à la largeur du modèle d'e-mail.

![Largeur du Content Block définie à 600 px.]({% image_buster /assets/img_archive/dnd_content_block_width_update.png %})