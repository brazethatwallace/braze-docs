---
nav_title: Éditeur par glisser-déposer
article_title: Créer un e-mail par glisser-déposer
alias: /dnd/
page_order: 1
description: "Cet article explique comment configurer et utiliser correctement l'éditeur par glisser-déposer pour les e-mails."
channel: email
tool:
- Campaigns
- Canvas
---

# Créer un e-mail par glisser-déposer {#create-an-email-with-drag-and-drop}

> L'éditeur par glisser-déposer vous permet de créer des e-mails entièrement personnalisés pour vos Campaigns ou Canvas, sans avoir à utiliser de HTML pour construire le corps de votre e-mail.

## À propos de l'éditeur {#about-the-editor}

L'éditeur par glisser-déposer utilise le [Contenu](#content) et les [Lignes](#rows) comme deux composants clés pour simplifier votre flux de travail, sans utilisation supplémentaire de HTML.

<table aria-label="À propos de l'éditeur" style="width: 100%; table-layout: fixed;">
    <caption>Composants de l'éditeur : Contenu et Lignes</caption>
    <thead>
    <tr>
        <th style="width: 50%;">Contenu</th>
        <th style="width: 50%;">Lignes</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_content.png %}" alt="L'onglet « Lignes » qui comprend différentes combinaisons structurelles pour la mise en page de votre e-mail." style="max-width: 100%; height: auto;">
        </td>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_rows.png %}" alt="L'onglet « Contenu » qui comprend les blocs de base, les médias et les options avancées." style="max-width: 100%; height: auto;">
        </td>
    </tr>
    </tbody>
</table>
{: .reset-td-br-1 aria-label="À propos de l'éditeur" }

### Contenu {#content}

Le **Contenu** comprend une série de tuiles représentant différents types de contenu que vous pouvez utiliser dans votre message. Ceux-ci sont organisés en trois catégories : basique, média et avancé.

{% tabs %}
{% tab Basique %}

Les blocs basiques constituent la base de votre e-mail. Grâce à ces blocs, vous pouvez ajouter l'un des éléments suivants dans le corps de votre e-mail :

- Titre
- Paragraphe
- Liste
- Bouton
- Séparateur
- Espacement

{% endtab %}
{% tab Média %}

Les blocs média vous permettent d'ajouter différents contenus visuels tels que des images, des vidéos, des icônes et des liens vers les réseaux sociaux, ainsi que des icônes personnalisables.

{% endtab %}
{% tab Avancé %}

Bien que l'éditeur par glisser-déposer simplifie votre flux de travail avec ces blocs, vous pouvez également utiliser des blocs avancés pour insérer du HTML ou ajouter un menu au corps de votre e-mail. Notez que l'utilisation de votre propre HTML peut affecter le rendu du message.

{% endtab %}
{% endtabs %}

### Lignes {#rows}

Les **Lignes** sont des unités structurelles qui définissent la composition horizontale d'une section du message à l'aide de colonnes. Vous pouvez utiliser des lignes vides ou des [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). L'utilisation de plusieurs colonnes vous permet de placer différents éléments de contenu côte à côte. De cette manière, vous pouvez ajouter tous les éléments structurels nécessaires à votre message, quel que soit le modèle sélectionné au départ.

#### Imbriquer des images dans des blocs de texte {#nesting-images-inside-text-blocks}

Vous ne pouvez pas imbriquer une image à l'intérieur d'un paragraphe ou d'un autre bloc de texte dans l'éditeur par glisser-déposer. Pour placer une image à côté ou au sein d'une mise en page textuelle, utilisez les colonnes dans une **Ligne** : par exemple, une ligne à plusieurs colonnes sur ordinateur avec **Masquer sur mobile** pour cette ligne, et une ligne distincte réservée au mobile (avec **Masquer sur ordinateur** et **Ne pas empiler sur mobile** selon les besoins) afin que l'image et le texte s'alignent correctement sur les petits écrans.

#### Style Cartes {#cards-style}

Le **Style Cartes** est une propriété de ligne qui permet d'ajouter des espacements entre les colonnes et d'arrondir leurs coins. Grâce au formatage de style carte, vous pouvez créer des mises en page plus attrayantes visuellement pour mettre en valeur votre contenu le plus important, comme les nouvelles fonctionnalités produit, les témoignages, les offres spéciales, les actualités, et bien plus encore.

## Utiliser l'éditeur par glisser-déposer {#using-the-drag-and-drop-editor}

Vous ne savez pas si votre e-mail doit être envoyé via une Campaign ou un Canvas ? Les Campaigns sont plus adaptées aux campagnes de communication ciblées et ponctuelles, tandis que les Canvas sont plus adaptés aux parcours utilisateur en plusieurs étapes.

{% alert note %}
Vous ne pouvez pas enregistrer un e-mail par glisser-déposer depuis une Campaign ou un Canvas directement dans **Modèles** > **Modèles d'e-mail** en tant que modèle d'e-mail. Créez d'abord dans **Modèles**, ou consultez [Puis-je enregistrer mon e-mail par glisser-déposer en tant que modèle après l'avoir créé dans ma Campaign ou mon Canvas ?]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/faq#can-i-save-my-drag-and-drop-email-as-a-template-after-i-build-it-within-my-campaign-or-canvas) pour recréer un modèle par glisser-déposer ou exporter le HTML avec **Télécharger le fichier**.
{% endalert %}

Après avoir choisi où créer votre message, passons aux étapes de création d'un e-mail par glisser-déposer.

### Étape 1 : Sélectionner votre modèle {#step-1-select-your-template}

Après avoir sélectionné l'éditeur par glisser-déposer comme expérience d'édition, vous pouvez choisir de :

- Commencer avec un modèle vierge.
- Utiliser un modèle d'e-mail par glisser-déposer préconçu par Braze.
- Utiliser un modèle d'e-mail par glisser-déposer enregistré.

{% alert note %}
Pour utiliser un modèle HTML personnalisé existant ou des modèles créés par un tiers, vous devez recréer le modèle en accédant à **Contenu** > **E-mail** et en sélectionnant **Éditeur par glisser-déposer** comme expérience d'édition.
{% endalert %}

Vous pouvez également accéder à tous les modèles depuis la section **Modèles**.

Après avoir sélectionné votre modèle, vous verrez un aperçu de votre e-mail sous **Variantes d'e-mail** qui inclut les informations d'envoi et le corps de l'e-mail.

Ensuite, sélectionnez **Modifier le corps de l'e-mail** pour commencer à concevoir la structure de l'e-mail dans l'éditeur par glisser-déposer.

![La section « Variantes d'e-mail » avec un exemple de corps d'e-mail.]({% image_buster /assets/img/dnd/dnd_emailvariant.png %})

### Étape 2 : Créer votre e-mail {#step-2-build-your-email}

L'expérience d'édition par glisser-déposer est divisée en trois sections : **Paramètres d'envoi**, **Contenu** et **Aperçu et test**. La magie de la création du corps de votre e-mail se produit dans la section **Contenu**. Avant de créer votre e-mail, il est important de comprendre les composants clés qui guident votre expérience de création d'e-mail. Si vous avez besoin de revoir ces éléments, consultez [À propos de l'éditeur](#about-the-editor).

Lorsque vous êtes prêt, utilisez les blocs de contenu par glisser-déposer pour créer votre e-mail.

1. Sélectionnez le panneau **Lignes**. Glissez-déposez les configurations de lignes dans l'éditeur principal. Cela définit la mise en page du contenu de votre e-mail.
- Notez que les nouvelles configurations doivent être glissées en haut ou en bas d'une section existante.
- Lorsque vous sélectionnez une configuration de ligne, les paramètres **Propriétés de ligne** apparaissent pour une personnalisation plus poussée des couleurs d'arrière-plan, des images et des tailles de colonnes personnalisées.
2. Sélectionnez le panneau **Contenu**. Glissez-déposez les tuiles de contenu souhaitées dans les composants de ligne.
- Vous pouvez également faire glisser n'importe quelle tuile de **Contenu** dans l'éditeur principal. Cela crée une ligne pour la tuile.
- Vous pouvez affiner davantage la tuile en la sélectionnant et en ajustant les champs dans **Propriétés du contenu** et **Options de bloc**. Cela inclut la modification de l'espacement des lettres, du remplissage, de la hauteur de ligne, et plus encore.

Consultez [Autres personnalisations](#other-customizations) pour d'autres moyens de personnaliser davantage votre e-mail par glisser-déposer.

Pendant la création de votre e-mail, vous pouvez basculer entre une vue bureau et mobile pour prévisualiser l'apparence de votre e-mail pour vos groupes d'utilisateurs. Cela vérifiera que votre contenu est responsive, et vous pourrez effectuer les ajustements nécessaires en cours de route.

{% alert tip %}
Besoin d'aide pour rédiger un texte accrocheur ? Essayez d'utiliser l'[assistant de rédaction IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Saisissez un nom de produit ou une description, et l'IA générera un texte marketing de qualité humaine à utiliser dans vos communications.

![Le bouton de rédaction, situé dans le panneau Contenu à côté des paramètres de style dans l'éditeur par glisser-déposer.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### Étape 3 : Ajouter vos informations d'envoi {#step-3-add-your-sending-information}

Une fois que vous avez terminé la conception et la création de votre e-mail, il est temps d'ajouter vos informations d'envoi dans la section **Paramètres d'envoi**.

{% multi_lang_include email/sending_info_steps.md %}

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Un aperçu dans le panneau de droite se remplira avec les informations d'envoi que vous avez ajoutées. Ces informations peuvent également être mises à jour en accédant à **Paramètres** > **Préférences e-mail** > **Configuration d'envoi**.

#### Ajouter des pièces jointes à l'e-mail {#add-email-attachments}

Dans **Paramètres d'envoi** > **Avancé**, vous pouvez ajouter des pièces jointes à l'e-mail par les méthodes suivantes :

{% multi_lang_include email/attachment_upload_options.md %}

Consultez les [Bonnes pratiques e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines) pour les bonnes pratiques spécifiques à prendre en compte.

#### Personnaliser l'en-tête de votre e-mail (avancé) {#personalize-your-email-header-advanced}

Sous **Paramètres d'envoi**, vous pouvez ajouter une personnalisation pour les en-têtes d'e-mail et les extras d'e-mail, ce qui vous permet d'envoyer des données supplémentaires à d'autres fournisseurs de services d'e-mail marketing. La personnalisation d'un en-tête d'e-mail, comme l'inclusion du nom du destinataire, peut également contribuer à augmenter la probabilité que votre e-mail soit ouvert.

{% alert note %}
La fonctionnalité avancée apparaîtra dans le composeur de Campaign ou de Canvas. Dans la fonctionnalité avancée, vous pouvez modifier votre paramètre CSS en ligne et saisir un en-tête ou des paires clé-valeur supplémentaires (si configuré).
{% endalert %}

### Étape 4 : Tester votre e-mail {#step-4-test-your-email}

Après avoir ajouté vos informations d'envoi, il est temps de tester votre e-mail.

{% alert tip %}
Si l'e-mail semble différent dans l'éditeur par rapport à l'aperçu ou à l'envoi test, vérifiez que toutes les balises sont fermées, que les attributs d'image ont des valeurs et que les images d'arrière-plan ne sont pas floues sur les bords.
{% endalert %}

Accédez à la section **Aperçu et test**. Vous avez ici la possibilité de prévisualiser votre e-mail en tant qu'utilisateur ou d'envoyer un message test. Cette section inclut également [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision), qui vous permet de vérifier que votre e-mail s'affiche correctement sur différents clients mobiles et web.

{% alert tip %}
Vous pouvez également utiliser le bouton **Aperçu en mode sombre** dans le panneau d'aperçu pour visualiser le corps de votre e-mail en mode sombre et ajuster votre e-mail si nécessaire.
{% endalert %}

Étant donné que vous pouvez visualiser trois versions différentes du même e-mail dans l'éditeur, dans Inbox Vision et en tant qu'e-mail test réel, il est important d'aligner les détails sur l'ensemble de vos plateformes.

#### Aperçu et envoi test {#preview-and-test-send}

Sous l'onglet **Prévisualiser en tant qu'utilisateur**, vous pouvez sélectionner les types d'utilisateurs suivants pour prévisualiser votre message.

- **Utilisateur aléatoire :** Braze sélectionnera aléatoirement un utilisateur dans la base de données et prévisualisera l'e-mail en fonction de ses attributs ou informations d'événements.
- **Sélectionner un utilisateur :** Vous pouvez sélectionner un utilisateur spécifique en fonction de son adresse e-mail ou de son ID externe. L'e-mail sera prévisualisé en fonction des attributs et des informations d'événements de cet utilisateur.
- **Utilisateur personnalisé :** Vous pouvez personnaliser un utilisateur. Braze proposera des champs pour tous les attributs et événements disponibles. Vous pouvez saisir toutes les informations que vous souhaitez voir dans l'aperçu de l'e-mail.

{% alert note %}
L'utilisateur aléatoire peut ou non faire partie de vos critères de segmentation. La segmentation est sélectionnée par la suite, donc Braze n'a pas connaissance de votre audience cible à ce stade.
{% endalert %}

Vous pouvez également sélectionner **Copier le lien d'aperçu** pour générer et copier un lien d'aperçu partageable qui montre à quoi ressemblera l'e-mail pour un utilisateur aléatoire. Pour plus d'informations, consultez [Aperçu partageable]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).

![Aperçu de l'e-mail avec un bouton pour « Copier le lien d'aperçu » et copier le lien généré.]({% image_buster /assets/img/dnd_email_link_preview.png %})

#### Utiliser Inbox Vision {#use-inbox-vision}

Inbox Vision vous permet de visualiser vos Campaigns d'e-mail du point de vue des clients de messagerie et des appareils mobiles. Pour tester votre e-mail à l'aide d'Inbox Vision, sélectionnez **Inbox Vision** dans la section **Aperçu et test** et sélectionnez **Lancer Inbox Vision**.

Il est important de tester et de vérifier les détails les plus fins de votre e-mail. Par exemple, les images d'arrière-plan dans les e-mails peuvent parfois provoquer l'apparition de lignes blanches ou de coupures entre les images, ou des clients tels que Windows Outlook peuvent ne pas afficher les images d'arrière-plan. L'utilisation d'Inbox Vision peut aider à identifier ces écarts entre les clients. Dans ce scénario, définissez une couleur d'arrière-plan de secours afin que ces images puissent s'afficher comme prévu.

Pour plus d'informations, consultez [Envoyer des messages test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=email).

Après avoir utilisé l'éditeur par glisser-déposer pour concevoir et créer votre e-mail, continuez à [créer]({{site.baseurl}}/user_guide/channels/email/html_editor#step-4-build-the-remainder-of-your-campaign-or-canvas) le reste de votre Campaign ou Canvas.

{% details À propos du moteur HTML mis à jour %}
Le moteur sous-jacent qui produit le HTML à partir de l'éditeur par glisser-déposer a été optimisé et mis à jour, offrant des avantages liés à la compression des fichiers HTML et au rendu.

La taille moyenne de nos données HTML exportées a été réduite, ce qui entraîne un chargement et un rendu plus rapides, une réduction du découpage sur mobile et une consommation de bande passante réduite.

Le rendu HTML a été amélioré grâce aux mises à jour suivantes qui minimisent le nombre de commentaires conditionnels et de requêtes média CSS. Par conséquent, les fichiers HTML sont plus petits et codés de manière plus efficace.
- Migration d'une conception basée sur des éléments `<div>` vers un code standard au format `<table aria-label="Utiliser Inbox Vision">`
  <caption>Utiliser Inbox Vision</caption>
- Les [blocs éditeur (e-mail)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email) ont été recodés pour plus de concision
- Le code HTML final est compressé pour supprimer les espaces entre les balises
- Les séparateurs transparents sont automatiquement convertis en remplissage de contenu
{% enddetails %}

## Autres personnalisations {#other-customizations}

Au fur et à mesure que vous construisez vos e-mails par glisser-déposer, vous pouvez personnaliser davantage le corps de chaque e-mail en utilisant une combinaison de ces détails créatifs pour capter l'attention de votre audience et susciter son intérêt pour votre message.

{% alert tip %}
Vous pouvez créer un thème personnalisé pour votre éditeur par glisser-déposer en utilisant les [paramètres de style globaux]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings).
{% endalert %}

### Images en largeur automatique {#auto-width-images}

Les images ajoutées à votre e-mail seront automatiquement définies sur **Largeur automatique**. Pour ajuster ce paramètre, désactivez **Largeur automatique** et modifiez le pourcentage de largeur selon vos besoins.

![Option de largeur automatique dans l'onglet Contenu de l'éditeur par glisser-déposer.]({% image_buster /assets/img/dnd/dnd1.png %})

### Superposition de couleurs {#color-layering}

Grâce à la superposition de couleurs, vous pouvez modifier la couleur de l'arrière-plan de l'e-mail, de la zone de contenu et des différents composants de contenu. L'ordre des couleurs de l'avant vers l'arrière est : couleur du composant de contenu, couleur d'arrière-plan de la zone de contenu et couleur d'arrière-plan.

![Exemple de superposition de couleurs dans l'éditeur par glisser-déposer.]({% image_buster /assets/img/dnd/dnd2.png %})

### Espacement du contenu {#content-padding}

![Options de bloc pour l'éditeur par glisser-déposer.]({% image_buster /assets/img/dnd/dnd3.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Pour ajuster l'espacement, faites défiler vers le bas jusqu'à **Options de bloc** et sélectionnez **Plus d'options**. Vous pouvez affiner votre espacement pour obtenir un e-mail parfaitement mis en forme.

### Arrière-plan du contenu {#content-background}

Vous pouvez ajouter une image d'arrière-plan à la configuration de votre ligne, ce qui vous permet d'intégrer davantage d'éléments de design et de contenu visuel dans votre campagne d'e-mail marketing.

### Attribut de langue {#language-attribute}

Vous pouvez définir l'attribut de langue en accédant à l'onglet **Paramètres** et en sélectionnant la langue souhaitée. Vous pouvez également cibler l'attribut utilisateur {%raw%} `{{${language}}}` {%endraw%} si le message est destiné à des utilisateurs avec des valeurs de langue dynamiques.

![Définition de la valeur « Langue » pour un e-mail.]({% image_buster /assets/img/dnd/language_setting_dnd.png %}){: style="max-width:70%;"}

### Personnalisation {#personalization}

![Options d'ajout de personnalisation pour l'éditeur par glisser-déposer.]({% image_buster /assets/img/dnd/dnd4.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Le Liquid de base est pris en charge dans l'éditeur d'e-mails par glisser-déposer. Pour ajouter de la personnalisation à votre e-mail :

1. Sélectionnez **Personnalisation** dans la section **Contenu**.
2. Sélectionnez le type de personnalisation. Cela inclut les attributs par défaut (standard), les attributs d'appareil, les attributs personnalisés, et plus encore.
3. Recherchez l'attribut à ajouter.
4. Copiez l'extrait Liquid généré et collez-le dans le corps de votre e-mail.

La personnalisation Liquid n'est pas prise en charge pour les blocs d'images ni pour les champs de type lien des boutons.

#### Images dynamiques {#dynamic-images}

Vous pouvez choisir d'inclure des images dynamiques dans vos e-mails en intégrant du [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) ou du [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) dans l'attribut source de votre image. Par exemple, au lieu d'une image statique, vous pouvez insérer {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} comme URL d'image pour inclure le prénom d'un utilisateur dans l'image. Cela permet de personnaliser vos e-mails pour chaque utilisateur.

{% alert important %}
L'URL de votre image doit commencer par `https://`. L'utilisation de `http://` provoque un plantage de votre application.
{% endalert %}

### Direction du texte {#text-direction}

Lors de la rédaction de votre message, vous pouvez basculer la direction du texte entre gauche-à-droite et droite-à-gauche en sélectionnant le bouton **Direction du texte** correspondant. Vous pouvez utiliser cette option lors de la création de messages dans des langues comme l'arabe et l'hébreu.

![Menu de l'éditeur d'e-mails par glisser-déposer avec un bouton pour basculer l'alignement du texte entre droite-à-gauche et gauche-à-droite.]({% image_buster /assets/img/dnd/dnd_template1.png %}){: style="max-width:50%;"}

L'apparence finale des messages de droite à gauche dépend en grande partie de la manière dont les fournisseurs de services les affichent. Pour les bonnes pratiques sur la création de messages de droite à gauche qui s'affichent aussi fidèlement que possible, consultez [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

### HTML

#### Attributs HTML pour les liens {#html-attributes-to-links}

![La section « Attributs » avec l'attribut « clicktracking » désactivé pour un lien.]({% image_buster /assets/img/dnd_custom_attributes.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Lorsque vous utilisez des liens, des boutons, des images et des vidéos dans l'éditeur par glisser-déposer, sélectionnez **Ajouter un nouvel attribut** sous **Attributs** dans la section **Contenu** pour ajouter des informations supplémentaires aux balises HTML dans les e-mails. Cela peut être particulièrement utile pour la personnalisation des messages, la segmentation et la mise en forme.

Un cas d'usage courant est de désactiver le suivi des clics pour des liens spécifiques lors de l'envoi via Braze. Vous pouvez le faire de deux manières :

- **Utiliser les attributs du module de lien :** Sélectionnez un élément de lien (comme un bouton ou un module de lien), puis utilisez **Ajouter un nouvel attribut** sous **Attributs** pour ajouter :
  - Pour SendGrid, utilisez `clicktracking` comme nom et `off` comme valeur.
  - Pour SparkPost, utilisez `data-msys-clicktrack` comme nom et `0` comme valeur.
- **Utiliser un bloc HTML :** Insérez un bloc HTML et incluez l'attribut de suivi des clics directement dans le code de votre balise d'ancrage :
  - Pour SendGrid, utilisez `<a href="your-url" clicktracking="off">Texte du lien</a>`.
  - Pour SparkPost, utilisez `<a href="your-url" data-msys-clicktrack="0">Texte du lien</a>`.

Un autre cas d'usage courant est de marquer des liens spécifiques comme liens universels. Les liens universels sont des liens qui redirigent vers votre application, offrant à vos utilisateurs une expérience intégrée.

* **SendGrid :** `universal = "true"`
* **SparkPost :** `data-msys-sublink = "open-in-app"` (un [sous-chemin personnalisé](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths) doit être configuré)

Pour configurer les liens universels, consultez [Liens universels et App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).

Vous pouvez également intégrer l'un de nos partenaires d'attribution, tels que [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking) ou [AppsFlyer]({{site.baseurl}}/partners/message_orchestration/deeplinking/appsflyer/appsflyer#integrate-appsflyer-with-braze-for-deep-linking), pour gérer les liens universels.

Enfin, des attributs prédéfinis sont disponibles pour rendre votre message accessible. Pour en savoir plus, consultez notre article dédié [Créer des messages accessibles dans Braze]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility), y compris [comment les clients de messagerie affichent le texte alternatif]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text).

#### Balises head personnalisées {#custom-head-tags}

Utilisez les balises `<head>` pour ajouter du CSS et des métadonnées dans votre e-mail. Par exemple, vous pouvez utiliser ces balises pour ajouter une feuille de style ou un favicon. Le Liquid est pris en charge dans les balises `<head>`.

Tout ce qui est ajouté en dehors des balises `<head>` sera ajouté après la balise `<body>` dans votre e-mail. Cela signifie que le contenu ajouté s'affichera dans l'e-mail.

##### Balises et attributs autorisés par balise {#allowed-tags-and-attributes-by-tag}

| Nom de la balise | Description | Exemple |
| --- | --- | --- |
| `base` | Spécifie l'URL de base pour toutes les URL relatives dans le message. | `<base href="https://example.com" target="_blank">` |
| `link`| Définit les relations entre le message et les ressources externes. | `<link href="styles.css" rel="stylesheet" type="text/css">` |
| `meta` | Fournit des métadonnées telles que la description de la page ou les mots-clés. | `<meta name="description" content="Free Web tutorials">` |
| `style` | Intègre des styles CSS internes. | `<style type="text/css" media="screen">body { font-size: 16px; }</style>` |
| `title` | Définit le titre du document affiché dans les onglets du navigateur. | `<title>StyleRyde</title>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Balises et attributs autorisés par balise" }

| Balise | Attribut | Description | Exemple |
| --- | --- | --- | --- |
| `base` | `href` | URL de base à utiliser pour les URL relatives. | ```<base href="https://braze.com">``` |
| `base` | `target`| Cible par défaut pour tous les hyperliens et formulaires. | ```<base target="_blank">``` |
| `link` | `href` | URL vers la ressource externe. | ```<link href="style.css">``` |
| `link` | `rel` | Définit les relations entre le message actuel et le message lié. | ```<link rel="stylesheet">``` |
| `link` | `type` | Type de ressource liée. | ```<link type="text/css">``` |
| `link` | `sizes` | Spécifie les tailles des icônes. | ```<link rel="icon" sizes="32x32" href="favicon-32.png">``` |
| `link` | `media` | Spécifie le média ou l'appareil pour lequel les styles s'appliquent. | ```<link rel="stylesheet" media="screen" href="style.css">``` |
| `meta` | `name` | Définit le titre du document affiché dans les onglets du navigateur. | ```<meta name="viewport" content="width=device-width, initial-scale=1">``` |
| `meta` | `content` | Définit le titre du document affiché dans les onglets du navigateur. | ```<meta name="description" content="Page about our newest products">``` |
| `meta` | `charset` | Déclare l'encodage des caractères. | ```<meta charset="UTF-8">``` |
| `meta` | `property` | Définit le titre du document affiché dans les onglets du navigateur. | ```<meta property="og:title" content="Website title">``` |
| `style` | `type` | Type MIME du contenu de style. | {% raw %}```<style type="text/css">p { color: red; }</style>```{% endraw %} |
| `style` | `media` | Spécifie le média ou l'appareil pour lequel les styles s'appliquent. | ```<style media="print">body { font-size: 12pt; }</style>``` |
| `title` | Aucun attribut | La balise `title` n'accepte aucun attribut. | ```<title>Kitchenerie</title>``` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Balises et attributs autorisés par balise" }

{% alert note %}
Les noms de liens peuvent contenir jusqu'à 63 octets et sont automatiquement tronqués s'ils dépassent cette limite.
{% endalert %}