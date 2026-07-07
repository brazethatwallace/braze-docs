---
nav_title: Créer des pages d'accueil
article_title: Créer des pages d'accueil
description: "Cet article explique comment créer et personnaliser des pages d'accueil Braze avec l'éditeur par glisser-déposer."
page_order: 0
---

# Créer des pages d'accueil {#create-landing-pages}

> Découvrez comment créer et personnaliser une page d'accueil à l'aide de l'éditeur par glisser-déposer, afin de développer votre audience et de collecter les préférences directement dans Braze.

## Conditions préalables {#prerequisites}

Pour accéder au générateur de pages d'accueil, vous avez besoin de [certaines autorisations]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites). Si vous n'avez pas accès, demandez de l'aide à votre administrateur Braze.

## Créer une page d'accueil {#creating-a-landing-page}

### Étape 1 : Créer un nouveau brouillon {#step-1-create-a-new-draft}

Accédez à **Messaging** > **Landing Pages**, puis sélectionnez **Create landing page**. Vous pouvez également sélectionner le nom d'une page d'accueil existante pour la dupliquer ou y apporter des modifications.

### Étape 2 : Saisir les détails de la page {#step-2-enter-the-page-details}

Ajoutez des détails internes et publics qui vous aident à organiser, personnaliser et partager votre page d'accueil.

#### Détails généraux {#general-details}

Saisissez un nom et une description pour la page d'accueil. Ces détails sont utilisés pour rechercher la page dans votre espace de travail interne. Ils ne seront pas visibles par vos clients.

#### Détails du site {#site-details}

Configurez les balises méta pour personnaliser l'apparence de votre page dans l'onglet du navigateur et optimiser les résultats des moteurs de recherche. Elles seront visibles par vos clients.

Nous vous recommandons de suivre ces bonnes pratiques :

| Champ | Description | Recommandations |
| --- | --- | --- |
| Titre du site | Le titre qui s'affiche dans l'onglet du navigateur. | Utilisez jusqu'à 60 caractères. |
| Méta-description | Un extrait de texte qui s'affiche dans les résultats de recherche. | Utilisez entre 140 et 160 caractères. |
| Favicon | L'icône qui apparaît à côté du titre du site dans l'onglet du navigateur. | Utilisez un rapport hauteur/largeur de 1:1 et un type de fichier pris en charge : PNG, JPEG ou ICO. |
| URL de la page | Il s'agit du chemin URL vers votre page d'accueil. Cette valeur est également référencée lors de l'utilisation des [étiquettes Liquid de page d'accueil]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) que vous pouvez intégrer dans un message pour identifier automatiquement les utilisateurs lorsqu'ils soumettent votre formulaire. | Cette valeur doit être unique dans votre espace de travail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Détails du site" }

### Étape 3 : Personnaliser la page {#step-3-customize-the-page}

Si ce n'est pas déjà fait, sélectionnez **Enregistrer en tant que brouillon**. Pour commencer à personnaliser votre page, sélectionnez **Edit landing page**. L'éditeur par glisser-déposer préchargera un modèle par défaut que vous pouvez personnaliser selon votre cas d'utilisation.

![Un exemple de page d'accueil en cours de création dans l'éditeur par glisser-déposer.]({% image_buster /assets/img/landing_pages/template.png %})

L'éditeur utilise deux types de composants pour la composition des pages d'accueil : les blocs de base et les blocs de formulaire. Tous les blocs doivent être placés dans une ligne. Pour une référence dédiée de chaque bloc et de ses propriétés, consultez [Blocs de l'éditeur (pages d'accueil)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).

![La section « Build » contenant « Rows » et « Form Blocks ».]({% image_buster /assets/img/landing_pages/dnd.png %}){: style="max-width:35%;"}

{% tabs %}
{% tab Blocs de base %}

Vous pouvez utiliser ces blocs pour ajouter du contenu et personnaliser la disposition de votre page d'accueil.

| Type de bloc | Description |
|-------------|-------------|
| Titre | Un bloc de texte pour ajouter un en-tête ou un titre à votre contenu. Utile pour structurer les sections et améliorer la lisibilité. |
| Paragraphe | Un bloc de texte pour des descriptions plus longues ou du contexte supplémentaire. Prend en charge le formatage de texte enrichi. |
| Bouton | Un élément cliquable qui dirige les utilisateurs vers une action spécifiée, comme ouvrir un lien ou soumettre un formulaire. |
| Bouton radio | Ajoute une liste d'options parmi lesquelles les utilisateurs peuvent en sélectionner une. Lors de la soumission, le profil utilisateur enregistre l'attribut personnalisé associé. |
| Image | Un bloc pour afficher des images. Vous pouvez télécharger une image ou fournir une URL pour référencer une source externe. |
| Lien | Un lien hypertexte sur lequel les utilisateurs peuvent cliquer pour accéder à une URL spécifiée. Peut être intégré dans du texte ou autonome. |
| Espacement | Un bloc invisible qui ajoute un espacement vertical entre les éléments pour améliorer la disposition et la lisibilité. |
| Code personnalisé | Un bloc qui vous permet d'insérer et d'exécuter du HTML, CSS ou JavaScript personnalisé pour une personnalisation avancée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 3 : Personnaliser la page" }

#### Span text {#span-text}

{% multi_lang_include drag_and_drop/span_text.md %}

{% endtab %}
{% tab Blocs de formulaire %}

Vous pouvez utiliser ces blocs pour créer un formulaire qui relie les données soumises par les utilisateurs à leur profil dans Braze. Gardez à l'esprit que si vous utilisez des blocs de formulaire, vous devrez également créer une page d'accueil supplémentaire pour l'état de confirmation.

![Un bloc de formulaire qui enregistre un nouveau client et enverra un code de réduction à son adresse e-mail.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

| Type de bloc | Description |
|---------------|-------------|
| Capture d'e-mail | Un champ de formulaire pour les adresses e-mail. Lors de la soumission, l'adresse e-mail est ajoutée au profil de cet utilisateur dans Braze. |
| Capture de téléphone | Un champ de formulaire pour les numéros de téléphone. Lors de la soumission, l'utilisateur est abonné à votre groupe d'abonnement SMS ou WhatsApp. |
| Champ de saisie | Un champ de formulaire qui prend en charge les attributs standard (tels que le prénom et le nom) ou une chaîne de caractères d'attribut personnalisé de votre choix. |
| Menu déroulant | Les utilisateurs peuvent sélectionner un élément dans une liste prédéfinie. Vous pouvez ajouter n'importe quelle chaîne de caractères d'attribut personnalisé à la liste. |
| Case à cocher | Si un utilisateur coche la case, l'attribut du bloc est défini sur `true`. Si elle n'est pas cochée, son attribut est défini sur `false`. |
| Groupe de cases à cocher | Les utilisateurs peuvent sélectionner parmi plusieurs choix présentés. Les valeurs sont soit définies, soit ajoutées à un attribut personnalisé de type tableau défini. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Span text" }

{% alert important %}
Après avoir créé une page d'accueil avec un formulaire, assurez-vous d'intégrer son [étiquette Liquid de page d'accueil]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) dans votre message. Grâce à cette étiquette, Braze peut automatiquement identifier et mettre à jour les profils utilisateurs existants lorsqu'ils soumettent le formulaire.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Styles du conteneur de page {#page-container-styles}

Vous pouvez définir des styles à appliquer à tous les blocs de composants pertinents de votre page d'accueil depuis l'onglet **Page container**. Ces styles seront utilisés partout sur votre page, sauf là où vous les remplacez par un bloc spécifique.

Nous vous recommandons de configurer les styles au niveau du conteneur de page avant de personnaliser les styles au niveau des blocs. Vous pouvez également ajouter une image d'arrière-plan pour l'ensemble de la page.

![La section « Page container » avec des options pour personnaliser les images d'arrière-plan, les couleurs, les détails de bordure et le style du contenu.]({% image_buster /assets/img/landing_pages/page_container.png %}){: style="max-width:40%;"}

#### Adaptation aux appareils des utilisateurs {#responsive-to-user-devices}

Vous pouvez rendre votre page d'accueil adaptative à la taille de l'appareil d'un utilisateur en empilant verticalement les colonnes sur les écrans plus petits. Pour activer cette fonctionnalité, ajoutez une colonne dans la ligne que vous souhaitez rendre adaptative, puis activez **Vertically stack on smaller screens** dans la section **Customize columns**.

Lorsque cette option est activée, vous pouvez également inverser l'empilement des colonnes pour contrôler l'ordre vertical du contenu multi-colonnes sur les écrans plus petits. Cela améliore l'apparence et l'expérience sur mobile sans code personnalisé.

![Le bouton bascule « Vertically stack on smaller screens » dans la section « Customize columns ».]({% image_buster /assets/img/landing_pages/device_responsive_toggle.png %}){: style="max-width:50%;"}

#### Champs facultatifs et obligatoires {#optional-and-required-fields}

Vous pouvez choisir si un champ de formulaire est obligatoire ou facultatif. Les champs obligatoires doivent être remplis avant que le formulaire puisse être soumis. Les champs facultatifs peuvent être laissés vides ou non sélectionnés par un utilisateur.

Par exemple, pour imposer la capture du consentement avant la soumission du formulaire, vous pouvez activer **Required field input** pour définir une case à cocher comme obligatoire avec le texte de clause de non-responsabilité approprié.

![Un champ de formulaire de type case à cocher avec le bouton bascule « Required input field » sélectionné.]({% image_buster /assets/img/landing_pages/lp-optional-required.png %}){: style="max-width:50%;"}

### Étape 4 : Créer une page de confirmation (facultatif) {#step-4-create-a-confirmation-page-optional}

Si votre page d'accueil n'inclut pas de formulaire, passez à l'étape suivante.

Si votre page d'accueil inclut un [formulaire](#form-blocks), créez une deuxième page d'accueil pour servir d'expérience de confirmation. Cette page devrait remercier les utilisateurs ou fournir une prochaine étape après la soumission du formulaire.

Pour lier la page de confirmation :
- Sélectionnez le bouton **Submit** sur votre formulaire
- Utilisez l'action **Open web URL** pour créer un lien vers votre page de confirmation

Si vous n'incluez pas de page de confirmation, les utilisateurs pourraient ne pas savoir que leur formulaire a été soumis avec succès. Incluez toujours une expérience de confirmation pour compléter le parcours.

{% alert note %}
Si votre page de confirmation s'ouvre dans un nouvel onglet, un utilisateur qui revient à la page d'accueil d'origine et soumet à nouveau avec des informations mises à jour peut écraser la soumission précédente, ce qui entraîne des données incohérentes.
{% endalert %}

### Étape 5 : Prévisualiser la page {#step-5-preview-the-page}

Vous pouvez prévisualiser votre page d'accueil dans l'onglet **Preview** de l'éditeur. Après avoir enregistré votre page d'accueil en tant que brouillon, vous pouvez visiter l'URL en accédant à **Landing Pages** et en sélectionnant **Copy URL** à côté de votre page d'accueil. Vous pouvez également partager l'URL avec des collaborateurs.

![Une page d'accueil avec le menu ouvert montrant l'option « Copy URL ».]({% image_buster /assets/img/landing_pages/copy-url.png %})

Avant de publier, assurez-vous que :

- Vous n'avez pas dépassé la limite de pages d'accueil publiées de votre forfait
- Chaque page basée sur un formulaire est liée à une [page de confirmation](#step-4-create-a-confirmation-page) en utilisant l'action **Open web URL**
- Tous les champs de page obligatoires (comme le chemin URL et le titre) sont complets

Lorsque vous êtes prêt, sélectionnez **Publish Landing Page**.

{% alert note %}
Les bloqueurs de pop-ups et de publicités agressifs sur iOS et dans Safari (y compris les contrôles intégrés de Safari et les extensions tierces) peuvent avoir un impact négatif sur le comportement des pages d'accueil lorsqu'un bouton **Submit** de formulaire ouvre également une autre URL, que cette URL s'ouvre dans le même onglet ou dans un nouvel onglet.
{% endalert %}

## Utiliser des modèles {#using-templates}

Utilisez les modèles de pages d'accueil pour créer des modèles pour vos prochaines campagnes. Ces modèles sont accessibles et gérables à la fois dans l'éditeur de pages d'accueil et depuis la page **Landing Page Templates** (**Content** > **Landing Page**). Les modèles de pages d'accueil nécessitent un nom et acceptent facultativement une description.

## Gérer les modèles {#managing-templates}

Vous pouvez prévisualiser, archiver ou modifier les modèles de pages d'accueil. Vous pouvez dupliquer vos propres modèles de pages d'accueil (situés dans **Your Templates**), mais pas les modèles Braze. Lors de la modification d'une page d'accueil, vous pouvez enregistrer votre page d'accueil en tant que modèle, apporter des modifications au modèle ou supprimer le contenu de la page d'accueil.

![Un menu déroulant avec des options pour enregistrer, modifier et supprimer une page d'accueil.]({% image_buster /assets/img/landing_pages/manage-lp-template.png %}){: style="max-width:60%;"}

## Consulter les analyses {#viewing-analytics}

Pour analyser l'efficacité de votre page d'accueil, accédez à **Messaging** > **Landing Pages**, puis sélectionnez une page d'accueil que vous avez publiée. Ici, vous pouvez suivre le nombre de vues de page, de clics sur la page, de soumissions de page et les taux de soumission de votre page d'accueil.

![La section d'analyse pour une page d'accueil.]({% image_buster /assets/img/landing_pages/analytics.png %})

## Gestion des erreurs de soumission de formulaire {#handling-form-submission-errors}

Si un utilisateur tente de soumettre un formulaire avec des données manquantes ou non prises en charge, il verra un message d'erreur générique et ne pourra pas soumettre.

Causes courantes :

- Les champs obligatoires sont laissés vides
- Des caractères spéciaux sont utilisés dans les champs de texte
- Une case à cocher obligatoire n'est pas sélectionnée

Les messages d'erreur affichés aux utilisateurs ne peuvent pas être personnalisés. Prévisualisez votre page d'accueil pour confirmer le comportement des champs avant de publier.