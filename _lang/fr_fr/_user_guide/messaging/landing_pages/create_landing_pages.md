---
nav_title: Créer des pages d'accueil
article_title: Créer des pages d'accueil
description: "Cet article explique comment créer et personnaliser des pages d'accueil Braze avec l'éditeur par glisser-déposer."
page_order: 0
---

# Créer des pages d'accueil {#create-landing-pages}

> Découvrez comment créer et personnaliser une page d'accueil à l'aide de l'éditeur par glisser-déposer, afin de développer votre audience et de collecter les préférences directement dans Braze.

## Prérequis {#prerequisites}

Pour accéder au générateur de pages de destination, vous avez besoin de [certaines autorisations]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites). Si vous n'y avez pas accès, demandez de l'aide à votre administrateur Braze.

## Créer une page de destination {#create-a-landing-page}

Une page de destination est une page web publiée et accessible en direct, dotée d'une URL partageable que vos clients peuvent consulter.

{% alert note %}
Les modèles de page de destination sont des points de départ de conception non publiés, sans URL publique, ce qui signifie qu'ils ne peuvent pas être partagés avec vos clients. Pour créer une page à partir d'un modèle, consultez [Utiliser des modèles](#using-templates).
{% endalert %}

### Étape 1 : Créer un nouveau brouillon {#step-1-create-a-new-draft}

Accédez à **Messaging** > **Landing Pages**, puis sélectionnez **Create landing page**. Vous pouvez également sélectionner le nom d'une page de destination existante pour la dupliquer ou y apporter des modifications.

### Étape 2 : Saisir les détails de la page {#step-2-enter-the-page-details}

Ajoutez des détails internes et publics qui vous aident à organiser, personnaliser et partager votre page de destination.

#### Détails généraux {#general-details}

Saisissez un nom et une description pour la page de destination. Ces détails sont utilisés pour rechercher la page dans votre espace de travail interne. Ils ne seront pas visibles par vos clients.

#### Détails du site {#site-details}

Configurez les balises méta pour personnaliser l'apparence de votre page dans l'onglet du navigateur et optimiser les résultats des moteurs de recherche. Elles seront visibles par vos clients.

Nous vous recommandons de suivre ces bonnes pratiques :

| Champ | Description | Recommandations |
| --- | --- | --- |
| Titre du site | Le titre qui s'affiche dans l'onglet du navigateur. | Utilisez jusqu'à 60 caractères. |
| Méta-description | Un extrait de texte qui s'affiche dans les résultats de recherche. | Utilisez entre 140 et 160 caractères. |
| Favicon | L'icône qui apparaît à côté du titre du site dans l'onglet du navigateur. | Utilisez un rapport hauteur/largeur de 1:1 et un type de fichier pris en charge : PNG, JPEG ou ICO. |
| URL de la page | Il s'agit du chemin URL vers votre page de destination. Cette valeur est également référencée lors de l'utilisation des [étiquettes Liquid de page de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) que vous pouvez intégrer dans un message pour identifier automatiquement les utilisateurs lorsqu'ils soumettent votre formulaire. | Cette valeur doit être unique dans votre espace de travail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Détails du site" }

### Étape 3 : Personnaliser la page {#step-3-customize-the-page}

Si ce n'est pas déjà fait, sélectionnez **Save as draft**. Pour commencer à personnaliser votre page, sélectionnez **Edit landing page**. L'éditeur par glisser-déposer préchargera un modèle par défaut que vous pouvez personnaliser selon votre cas d'usage.

![Exemple de page de destination en cours de création dans l'éditeur par glisser-déposer.]({% image_buster /assets/img/landing_pages/template.png %})

L'éditeur utilise deux types de composants pour la composition des pages de destination : les blocs de base et les blocs de formulaire. Tous les blocs doivent être placés dans une ligne. Pour une référence dédiée de chaque bloc et de ses propriétés, consultez [Blocs éditeur (pages de destination)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).

![La section « Build » contenant « Rows » et « Form Blocks ».]({% image_buster /assets/img/landing_pages/dnd.png %}){: style="max-width:35%;"}

{% tabs %}
{% tab Blocs de base %}

Vous pouvez utiliser ces blocs pour ajouter du contenu et personnaliser la mise en page de votre page de destination.

| Type de bloc | Description |
|-------------|-------------|
| Titre | Un bloc de texte pour ajouter un en-tête ou un titre à votre contenu. Utile pour structurer les sections et améliorer la lisibilité. |
| Paragraphe | Un bloc de texte pour des descriptions plus longues ou du contexte supplémentaire. Prend en charge le formatage de texte enrichi. |
| Bouton | Un élément cliquable qui dirige les utilisateurs vers une action spécifique, comme ouvrir un lien ou soumettre un formulaire. |
| Bouton radio | Ajoute une liste d'options parmi lesquelles les utilisateurs doivent en sélectionner une. Lors de la soumission, le profil utilisateur enregistre l'attribut personnalisé associé. |
| Image | Un bloc pour afficher des images. Vous pouvez télécharger une image ou fournir une URL pour référencer une source externe. |
| Lien | Un lien hypertexte sur lequel les utilisateurs peuvent cliquer pour accéder à une URL spécifiée. Peut être intégré dans du texte ou utilisé de manière autonome. |
| Espacement | Un bloc invisible qui ajoute un espacement vertical entre les éléments pour améliorer la mise en page et la lisibilité. |
| Code personnalisé | Un bloc qui vous permet d'insérer et d'exécuter du HTML, CSS ou JavaScript personnalisé pour une personnalisation avancée. Pour interagir avec le SDK Braze depuis ce bloc, consultez [Pont JavaScript pour les pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge) et [Créer des blocs de formulaire personnalisés]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 3 : Personnaliser la page" }

#### Texte span {#span-text}

Pour appliquer un style spécifique aux blocs de texte sans code personnalisé, surlignez le texte que vous souhaitez styliser, puis sélectionnez **Wrap with span for style**.

![Zone de texte avec différentes sections de texte stylisées, comme des tailles et couleurs de police différentes, et une section surlignée affichant une barre d'outils avec l'option « Wrap with span for style ».]({% image_buster /assets/img/landing_pages/wrap_with_span.png %}){: style="max-width:50%;"}

Ajustez les propriétés du span pour mettre à jour le style de votre texte, notamment :

- Famille de police, graisse, taille
- Hauteur de ligne
- Espacement des lettres
- Alignement et couleur du texte
- Marge intérieure du bloc

![Panneau des propriétés du span avec différentes options à modifier.]({% image_buster /assets/img/landing_pages/span_properties.png %}){: style="max-width:35%;"}


{% endtab %}
{% tab Blocs de formulaire %}

Vous pouvez utiliser ces blocs pour créer un formulaire qui relie les données soumises par les utilisateurs à leur profil dans Braze. Gardez à l'esprit que si vous utilisez des blocs de formulaire, vous devrez également créer une page de destination supplémentaire pour l'état de confirmation.

![Un bloc de formulaire qui enregistre un nouveau client et enverra un code de réduction à son adresse e-mail.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

| Type de bloc | Description |
|---------------|-------------|
| Capture d'e-mail | Un champ de formulaire pour les adresses e-mail. Lors de la soumission, l'adresse e-mail est ajoutée au profil de cet utilisateur dans Braze. |
| Capture de téléphone | Un champ de formulaire pour les numéros de téléphone. Lors de la soumission, l'utilisateur est abonné à votre groupe d'abonnement SMS ou WhatsApp. |
| Champ de saisie | Un champ de formulaire qui prend en charge les attributs standard (comme le prénom et le nom) ou une chaîne d'attribut personnalisé de votre choix. |
| Liste déroulante | Les utilisateurs peuvent sélectionner un élément dans une liste prédéfinie. Vous pouvez ajouter n'importe quelle chaîne d'attribut personnalisé à la liste. |
| Case à cocher | Si un utilisateur coche la case, l'attribut du bloc est défini sur `true`. Si elle reste décochée, son attribut est défini sur `false`. |
| Groupe de cases à cocher | Les utilisateurs peuvent sélectionner parmi plusieurs choix présentés. Les valeurs sont soit définies, soit ajoutées à un attribut personnalisé de type tableau défini. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Blocs de formulaire" }

{% alert important %}
Après avoir créé une page de destination avec un formulaire, veillez à intégrer son [étiquette Liquid de page de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) dans votre message. Grâce à cette étiquette, Braze peut automatiquement identifier et mettre à jour les profils utilisateur existants lorsqu'ils soumettent le formulaire.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Styles du conteneur de page {#page-container-styles}

Vous pouvez définir des styles à appliquer à tous les blocs de composants pertinents de votre page de destination depuis l'onglet **Page container**. Ces styles s'appliquent partout sur votre page, sauf là où vous les remplacez par un bloc spécifique.

Nous vous recommandons de configurer les styles au niveau du conteneur de page avant de personnaliser les styles au niveau des blocs. Vous pouvez également ajouter une image d'arrière-plan pour l'ensemble de la page.

![La section « Page container » avec des options pour personnaliser les images d'arrière-plan, les couleurs, les détails de bordure et le style du contenu.]({% image_buster /assets/img/landing_pages/page_container.png %}){: style="max-width:40%;"}

#### Adaptation aux appareils des utilisateurs {#responsive-to-user-devices}

Vous pouvez rendre votre page de destination adaptative à la taille de l'appareil d'un utilisateur en empilant verticalement les colonnes sur les écrans plus petits. Pour activer cette fonctionnalité, ajoutez une colonne dans la ligne que vous souhaitez rendre adaptative, puis activez **Vertically stack on smaller screens** dans la section **Customize columns**.

Lorsque cette option est activée, vous pouvez également inverser l'empilement des colonnes pour contrôler l'ordre vertical du contenu multi-colonnes sur les écrans plus petits. Cela améliore l'apparence et l'expérience des pages sur mobile sans code personnalisé.

![Le bouton bascule « Vertically stack on smaller screens » dans la section « Customize columns ».]({% image_buster /assets/img/landing_pages/device_responsive_toggle.png %}){: style="max-width:50%;"}

{% multi_lang_include drag_and_drop/hide_rows_and_blocks_by_device.md channel='landing_page' %}

#### Champs facultatifs et obligatoires {#optional-and-required-fields}

Vous pouvez choisir si certains champs de formulaire sont obligatoires ou facultatifs. Les champs obligatoires doivent être remplis avant que le formulaire puisse être soumis. Les champs facultatifs peuvent être laissés vides ou non sélectionnés par un utilisateur.

{% alert note %}
Les boutons radio sont toujours obligatoires et ne peuvent pas être définis comme facultatifs. Si vous avez besoin d'un champ à choix unique facultatif, envisagez d'utiliser une liste déroulante à la place.
{% endalert %}

Par exemple, pour imposer la capture du consentement avant la soumission du formulaire, vous pouvez activer **Required field input** pour rendre une case à cocher obligatoire avec le texte de clause de non-responsabilité approprié.

![Un champ de formulaire de type case à cocher avec le bouton bascule « Required input field » sélectionné.]({% image_buster /assets/img/landing_pages/lp-optional-required.png %}){: style="max-width:50%;"}

### Étape 4 : Créer une page de confirmation (facultatif) {#step-4-create-a-confirmation-page-optional}

Si votre page de destination n'inclut pas de formulaire, passez à l'étape suivante.

Si votre page de destination inclut un [formulaire](#form-blocks), créez une seconde page de destination pour servir d'expérience de confirmation. Cette page devrait remercier les utilisateurs ou fournir une prochaine étape après la soumission du formulaire.

Pour lier la page de confirmation :
- Sélectionnez le bouton **Submit** sur votre formulaire
- Utilisez l'action **Open web URL** pour créer un lien vers votre page de confirmation

Si vous n'incluez pas de page de confirmation, les utilisateurs risquent de ne pas savoir que leur formulaire a été soumis avec succès. Incluez toujours une expérience de confirmation pour compléter le parcours.

{% alert note %}
Si votre page de confirmation s'ouvre dans un nouvel onglet, un utilisateur qui revient sur la page de destination d'origine et soumet à nouveau le formulaire avec des informations mises à jour peut écraser la soumission précédente, ce qui entraîne des données incohérentes.
{% endalert %}

### Étape 5 : Prévisualiser la page {#step-5-preview-the-page}

Vous pouvez prévisualiser votre page de destination dans l'onglet **Preview** de l'éditeur. Après avoir enregistré votre page de destination en tant que brouillon, vous pouvez consulter l'URL en accédant à **Landing Pages** et en sélectionnant **Copy URL** à côté de votre page de destination.

![Une page de destination avec le menu ouvert affichant l'option « Copy URL ».]({% image_buster /assets/img/landing_pages/copy-url.png %})

#### Partager un lien de prévisualisation {#sharing-a-preview-link}

Dans l'éditeur, vous pouvez également sélectionner **Copy preview link** pour partager la page avec des réviseurs qui n'ont pas accès au tableau de bord.

- Si votre page de destination n'utilise pas Liquid, ce lien est identique à l'URL directe de **Copy URL**, ouverte en mode prévisualisation.
- Si votre page de destination utilise Liquid et que vous disposez de l'offre Landing Pages Pro, le lien affiche plutôt la page en direct à la demande et reflète vos modifications actuelles plutôt qu'un instantané du moment où vous avez généré le lien. Le contenu est personnalisé par utilisateur. La prévisualisation affiche le favicon Braze et ne peut pas être modifiée.

Pour les liens de prévisualisation sur d'autres canaux, consultez [Prévisualisation partageable]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).

### Étape 6 : Publier {#step-6-publish}

Avant de publier, assurez-vous que :

- Vous n'avez pas dépassé la limite de pages de destination publiées de votre forfait
- Chaque page basée sur un formulaire est liée à une [page de confirmation](#step-4-create-a-confirmation-page) via l'action **Open web URL**
- Tous les champs de page obligatoires (comme le chemin URL et le titre) sont remplis

Lorsque vous êtes prêt, sélectionnez **Publish Landing Page**.

{% alert note %}
Les bloqueurs de pop-ups et de publicités agressifs sur iOS et dans Safari (y compris les contrôles intégrés de Safari et les extensions tierces) peuvent avoir un impact négatif sur le comportement des pages de destination lorsqu'un bouton **Submit** de formulaire ouvre également une autre URL, que cette URL s'ouvre dans le même onglet ou dans un nouvel onglet.
{% endalert %}

## Utiliser des modèles {#use-templates}

Les modèles de pages de destination sont des points de départ de conception réutilisables qui vous aident à créer des pages de destination plus rapidement. Un modèle n'a pas d'URL publique et ne peut pas être visité par les clients. Pour créer une page de destination en direct à partir d'un modèle, sélectionnez le modèle lors de la création d'une nouvelle page de destination, personnalisez-le selon vos besoins, puis publiez-le.

Les modèles sont accessibles et gérables à la fois dans l'éditeur de pages de destination et depuis la page **Landing Page Templates** (**Content** > **Landing Page**). Les modèles de pages de destination nécessitent un nom et une description facultative.

## Gérer les modèles {#manage-templates}

Vous pouvez prévisualiser, archiver ou modifier les modèles de pages de destination. Vous pouvez dupliquer vos propres modèles de pages de destination (situés dans **Vos modèles**), mais pas les modèles Braze. Lors de la modification d'une page de destination, vous pouvez enregistrer votre page de destination en tant que modèle, apporter des modifications au modèle ou supprimer le contenu de la page de destination.

![Un menu déroulant avec des options pour enregistrer, modifier et supprimer une page de destination.]({% image_buster /assets/img/landing_pages/manage-lp-template.png %}){: style="max-width:60%;"}

## Consulter les analyses {#view-analytics}

Pour analyser l'efficacité de votre page de destination, accédez à **Messaging** > **Landing Pages**, puis sélectionnez une page de destination que vous avez publiée. Vous pouvez y suivre le nombre de vues de page, de clics sur la page, de soumissions de page, ainsi que les taux de soumission de votre page de destination.

![La section d'analyse d'une page de destination.]({% image_buster /assets/img/landing_pages/analytics.png %})

## Gérer les erreurs de soumission de formulaire {#handling-form-submission-errors}

Si un utilisateur tente de soumettre un formulaire avec des données manquantes ou non prises en charge, il verra un message d'erreur générique et ne pourra pas soumettre.

Causes courantes :

- Les champs obligatoires sont laissés vides
- Des caractères spéciaux sont utilisés dans les champs de texte
- Une case à cocher obligatoire n'est pas sélectionnée

Les messages d'erreur affichés aux utilisateurs ne peuvent pas être personnalisés. Prévisualisez votre page de destination pour confirmer le comportement des champs avant de publier.