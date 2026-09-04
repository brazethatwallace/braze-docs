---
nav_title: Éditeur traditionnel
article_title: Créer un message in-app dans l'éditeur traditionnel
page_order: 2
description: "Cet article de référence explique comment créer un message in-app à l'aide de la plateforme Braze via des Campaigns ou Canvas."
channel:
  - in-app messages
tool:
  - Campaigns
search_rank: 4.8
toc_headers: h2
---

# Créer un message in-app avec l'éditeur traditionnel {#create-an-in-app-message-with-the-traditional-editor}

> Vous pouvez créer un message in-app ou un message dans le navigateur à l'aide de la plateforme Braze via des Campaigns, Canvas ou en tant que campagne API. Nous vous recommandons vivement de planifier vos messages et de préparer tous les éléments à l'avance en utilisant notre pratique [guide de préparation des messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices).

## Étape 1 : Choisir où créer votre message {#create-new-campaign-in-app}

Vous ne savez pas si votre message doit être envoyé via une Campaign ou un Canvas ? Les Campaigns sont plus adaptées aux envois de messages ciblés ponctuels, tandis que les Canvas sont plus adaptés aux parcours utilisateur en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

1. Allez dans **Messaging** > **Campaigns** et sélectionnez **Create Campaign**.
2. Sélectionnez **In-App Message**. Notez que les messages in-app ne sont pas disponibles dans les Campaigns multicanales.
3. Donnez à votre Campaign un nom clair et significatif.
4. Ajoutez des [équipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) et des [étiquettes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) selon vos besoins.
   * Les étiquettes facilitent la recherche de vos Campaigns et la création de rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reports/report_builder), vous pouvez filtrer par étiquettes spécifiques.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre Campaign. Vous pouvez choisir différentes plateformes, types de messages et dispositions pour chacune de vos variantes ajoutées. Pour en savoir plus sur ce sujet, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si tous les messages de votre Campaign sont similaires ou ont le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copy from Variant** dans le menu déroulant **Add Variant**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md in_app_message=true %}

{% alert important %}
Vous ne pouvez pas avoir plusieurs variantes de messages in-app dans une seule étape.
{% endalert %}

Vous trouverez plus d'informations spécifiques à Canvas dans [Messages in-app dans Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas).

{% endtab %}
{% endtabs %}

## Étape 2 : Spécifier les plateformes de diffusion {#step-2-specify-delivery-platforms}

Commencez par choisir les plateformes qui doivent recevoir le message. Utilisez cette sélection pour limiter la diffusion d'une campagne à un ensemble spécifique d'applications. Par exemple, vous pouvez choisir **Navigateurs web** pour un message dans le navigateur encourageant les utilisateurs à télécharger votre application mobile, afin de vous assurer qu'ils ne reçoivent pas le message après avoir déjà obtenu votre application. Étant donné que les sélections de plateformes sont spécifiques à chaque variante, vous pouvez essayer de tester l'engagement par message en fonction de la plateforme.

| Plateforme                                        | Diffusion du message             |
|---------------------------------------------------|----------------------------------|
| Applications mobiles                              | SDK iOS, Android et Vega         |
| Navigateurs web                                   | SDK Web                         |
| Applications mobiles et navigateurs web           | SDK iOS, Android, Vega et Web   |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Spécifier les plateformes de diffusion" }

## Étape 3 : Spécifier vos types de messages {#step-3-specify-your-message-types}

Une fois que vous avez sélectionné une plateforme d'envoi, parcourez les types de messages, les mises en page et les autres options qui y sont associées. Pour en savoir plus sur le comportement attendu et l'apparence de chacun de ces messages, consultez notre page [Types de messages]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types), ou cliquez sur les types de messages liés dans les tableaux suivants.

Lorsque vous choisissez le type de message à utiliser, réfléchissez à l'espace que votre message occupera et à quel point il pourrait perturber l'expérience utilisateur.

- Les messages **contextuels** sont les moins intrusifs et apparaissent de manière subtile sans bloquer le contenu.
- Les messages de type **fenêtre modale** se situent au milieu : suffisamment visibles pour attirer l'attention sans prendre complètement le contrôle de l'écran.
- Les messages **plein écran** attirent le plus l'attention et sont les plus adaptés aux annonces critiques ou aux promotions.

Plus votre contenu est complexe, plus vous aurez besoin d'espace, et plus votre message risquera d'interrompre le flux de l'utilisateur.

### Types de messages {#message-types}

Ces messages in-app sont pris en charge à la fois par les applications mobiles et les applications web.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table aria-label="Types de messages" class="tg">
  <caption>Types de messages</caption>
<thead>
  <tr>
    <th>Type de message</th>
    <th>Description du type</th>
    <th>Mises en page disponibles</th>
    <th>Autres options</th>
    <th>Utilisation recommandée</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/fullscreen'>Plein écran</a></td>
    <td>Messages qui couvrent l'intégralité de l'écran avec un bloc de message.</td>
    <td>
      <ul>
      <li>Image et texte</li>
      <li>Image uniquement</li>
      </ul>
    </td>
    <td>Orientation de l'appareil imposée (portrait ou paysage)</td>
    <td>Grand et percutant ! À utiliser lorsque vous voulez vous assurer que les utilisateurs voient votre contenu, comme vos Campaigns les plus importantes, les notifications essentielles ou les promotions majeures.<br><br>Notez que sur les appareils mobiles, les messages en portrait et en paysage ne s'afficheront pas si l'orientation de l'appareil ne correspond pas à l'orientation du message.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/modal'>Fenêtre modale</a></td>
    <td>Messages qui couvrent l'intégralité de l'écran avec un voile de superposition et un bloc de message.</td>
    <td>
      <ul>
      <li>Texte (avec image facultative)</li>
      <li>Image uniquement</li>
      </ul>
    </td>
    <td>N/A</td>
    <td>Un bon compromis. À utiliser lorsque vous avez besoin d'un moyen visible d'attirer l'attention de vos utilisateurs, par exemple pour les encourager à essayer une nouvelle fonctionnalité ou à profiter d'une promotion.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/slideup'>Contextuel</a></td>
    <td>Messages qui glissent dans la vue à un emplacement désigné sans bloquer le reste de l'écran.</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Discret : occupe le moins d'espace à l'écran. À utiliser pour alerter les utilisateurs sur de petits éléments d'information, tels que les nouvelles fonctionnalités, les annonces, l'utilisation de cookies, etc.<br></td>
  </tr>
</tbody>
</table>

### Types de messages avancés {#advanced-message-types}

Ces messages in-app sont personnalisables selon vos besoins.

<table aria-label="Types de messages avancés" class="tg">
  <caption>Types de messages avancés</caption>
<thead>
  <tr>
    <th>Type de message</th>
    <th>Description du type</th>
    <th>Mises en page disponibles</th>
    <th>Prérequis</th>
    <th>Utilisation recommandée</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/custom_html'>Message HTML personnalisé</a></td>
    <td>Messages personnalisés qui fonctionnent selon votre code personnalisé (HTML, CSS et/ou JavaScript).</td>
    <td>N/A</td>
    <td>Vous devez définir l'option d'initialisation <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> sur <code>true</code> pour que votre message in-app fonctionne.</td>
    <td>C'est une bonne option si vous souhaitez tous les avantages des messages in-app tout en ayant besoin de fonctionnalités supplémentaires ou que l'apparence reste cohérente avec votre marque. Vous pouvez modifier chaque détail du message : police, couleur, forme, taille, boutons, etc. <br><br>Exemples de cas d'usage : demander aux utilisateurs leur avis sur l'application, formulaires de collecte d'e-mails ou messages paginés</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/email_capture_form'>Formulaire de collecte d'e-mails</a></td>
    <td>Généralement utilisé pour collecter l'adresse e-mail du visiteur.</td>
    <td>N/A</td>
    <td>Vous devez définir l'option d'initialisation <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> sur <code>true</code> pour que votre message in-app fonctionne.</td>
    <td>Lorsque vous invitez les utilisateurs à soumettre leur adresse e-mail.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/customize#web-modal-css'>Fenêtre modale web avec CSS</a></td>
    <td>Messages modaux pour le web avec CSS personnalisable.</td>
    <td>
      <ul>
      <li>Texte (avec image facultative)</li>
      <li>Image uniquement</li>
      </ul>
    </td>
    <td>La fenêtre modale web avec CSS est propre au SDK web et ne peut être utilisée qu'après avoir sélectionné <b>Web Browsers</b>.</td>
    <td>Lorsque vous souhaitez télécharger ou écrire du CSS personnalisé pour créer une communication entièrement stylisée et visuellement attrayante.</td>
  </tr>
</tbody>
</table>

{% alert important %}
Si Braze détecte que vous n'avez pas inclus de bouton de fermeture ou de rejet dans votre code, nous vous demanderons d'en ajouter un. Pour plus de commodité, nous avons fourni un extrait de code que vous pouvez copier et coller dans votre code : <br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## Étape 4 : Composer votre message in-app {#step-4-compose-your-in-app-message}

L'onglet **Composer** vous permet de modifier tous les aspects du contenu et du comportement de votre message.

![Un exemple de message in-app d'une marque pour accueillir de nouveaux clients et les inciter à configurer un profil utilisateur.]({% image_buster /assets/img_archive/iam_compose.png %}){: style="max-width:85%" }

Le contenu de l'onglet **Composer** varie en fonction des options de message choisies à l'étape précédente, mais peut inclure l'une des options suivantes :

### Langue {#language}

Sélectionnez **Ajouter des langues** et choisissez les langues souhaitées dans la liste fournie. Cela insérera du [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) dans votre message. Nous vous recommandons de sélectionner vos langues avant de rédiger votre contenu afin de pouvoir remplir votre texte à l'emplacement approprié dans le Liquid. Consultez notre [liste complète des langues disponibles]({{site.baseurl}}/developer_guide/localization?tab=android).

### Image {#image}

Selon votre type de message, vous pouvez **Charger une image**, **Choisir un badge** ou utiliser **Font Awesome**. Pour charger une image, sélectionnez **Ajouter une image** ou fournissez une URL d'image. Sélectionner **Ajouter une image** ouvre la **bibliothèque multimédia**, où vous pouvez sélectionner une image précédemment chargée ou en ajouter une nouvelle. Chaque type de message et plateforme peut avoir ses propres proportions et exigences suggérées — assurez-vous de vérifier quelles sont ces spécifications avant de commander ou de créer une image de zéro.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### En-tête et corps {#header-and-body}

Rédigez ce que vous souhaitez ! Incluez du contenu entièrement personnalisé (souvent avec des fonctionnalités HTML personnalisées) avec les options d'inclusion de [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) et d'autres types de personnalisation. Plus vite vous pouvez faire passer votre message et inciter votre client à cliquer, mieux c'est ! Nous recommandons des en-têtes et un contenu de message clairs et concis.

Certains types de messages ne nécessitent pas d'en-tête et n'en demandent donc pas.

#### Conseils {#tips}

##### Générer du contenu avec l'IA {#generating-ai-copy}

Besoin d'aide pour rédiger un texte percutant ? Essayez d'utiliser l'[assistant de rédaction IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Saisissez un nom ou une description de produit et l'IA générera un texte marketing au style naturel à utiliser dans vos communications.

![Bouton Lancer le rédacteur IA, situé dans le champ Message du compositeur de messages in-app.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### Créer des messages de droite à gauche {#creating-right-to-left-messages}

Besoin d'aide pour créer des messages de droite à gauche pour des langues comme l'arabe et l'hébreu ? Consultez [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages) pour les bonnes pratiques.

### Texte des boutons {#buttons}

Lorsque cette option est disponible pour votre type de message, vous pouvez faire apparaître jusqu'à deux boutons sous le corps de votre texte. Vous pouvez créer et modifier le texte et la couleur des boutons personnalisés. Vous pouvez également ajouter un lien vers les conditions d'utilisation dans les formulaires de capture d'e-mail.

Si vous choisissez de n'utiliser qu'un seul bouton, il s'ajustera automatiquement pour occuper l'espace disponible en bas de votre message au lieu de laisser de la place pour un bouton supplémentaire.

#### Choisir un bouton principal {#choosing-a-primary-button}

Si vous décidez de formater ces boutons avec vos propres couleurs, nous vous recommandons d'utiliser le bouton 2 pour le résultat que vous préférez.

En d'autres termes, si vous souhaitez que votre utilisateur clique sur un bouton plutôt que sur l'autre, assurez-vous qu'il s'agit du bouton secondaire. Le bouton secondaire a souvent affiché un meilleur potentiel de clic, surtout s'il a une couleur quelque peu contrastée ou autrement distinctive par rapport au reste du message. Cela est d'autant plus marqué lorsque le bouton principal se fond davantage visuellement dans le message.

![Boutons principal et secondaire dans un message in-app]({% image_buster /assets/img/primary-secondary-buttons.png %})

### Comportement au clic {#button-actions}

Lorsque votre client clique sur un bouton dans votre message in-app, les actions suivantes sont disponibles.

| Action | Description |
|---|---|
| Rediriger vers une URL web | Ouvre une page web non native. |
| [Deep link dans l'application]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | Deep link vers un écran existant dans votre application. |
| Fermer le message | Ferme le message actuellement actif. |
| Enregistrer un événement personnalisé | Choisissez un [événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events) à déclencher. Peut être utilisé pour afficher un autre message in-app ou déclencher des communications supplémentaires. |
| Enregistrer un attribut personnalisé | Choisissez un [attribut personnalisé]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) à définir pour l'utilisateur actuel. |
| Demander l'autorisation push | Affiche la demande d'autorisation push native. En savoir plus sur l'[amorçage push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages), ainsi que les [bonnes pratiques]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#best-practices) pour préparer les utilisateurs aux notifications push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportement au clic #button-actions" }

Remarque : les options __Demander l'autorisation push__, __Enregistrer un événement personnalisé__ et __Enregistrer un attribut personnalisé__ nécessitent les versions minimales de SDK suivantes :

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Pour combiner plusieurs actions ou effectuer des actions SDK supplémentaires non disponibles dans le tableau de bord (telles que l'ajout à un groupe d'abonnement ou la définition d'un type d'abonnement e-mail), vous pouvez utiliser les [deep links Braze Actions]({{site.baseurl}}/developer_guide/braze_actions).

### Options d'appareils iOS {#ios-device-options}

Si vous le souhaitez, vous pouvez restreindre votre message in-app pour qu'il ne soit envoyé qu'aux appareils iOS. Pour ce faire, cliquez sur **Modifier** et sélectionnez **Envoyer uniquement aux appareils iOS**.

### Fermeture du message {#message-close}

Choisissez parmi les options suivantes :

- **Fermeture automatique :** Sélectionnez le nombre de secondes pendant lequel le message restera à l'écran.
- **Attendre un balayage ou un toucher de l'utilisateur :** Nécessite une option de fermeture.

Fermer un message enregistre une impression mais pas un clic. Pour savoir comment les clics sont suivis en fonction de l'action de l'utilisateur, consultez [Suivi des clics]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting#click-tracking).

### Position du contextuel {#slide-up-position}

Ce paramètre s'applique uniquement au type de message contextuel. Choisissez si votre contextuel doit apparaître **Depuis le bas de l'écran de l'application** ou **Depuis le haut de l'écran de l'application**.

### HTML et ressources {#html-and-assets}

Ce paramètre s'applique uniquement au type de message avec code personnalisé. Copiez et collez le HTML dans l'espace disponible et chargez vos ressources à l'aide d'un [fichier ZIP]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#zip-file-uploads).

### Marque substitutive du champ de saisie de capture d'e-mail {#email-capture-input-placeholder}

Ce paramètre s'applique uniquement au type de message de formulaire de capture d'e-mail. Saisissez un texte personnalisé qui apparaîtra comme texte de marque substitutive dans le champ de saisie de l'e-mail. Par défaut, ce texte est « Saisissez votre adresse e-mail ».

## Étape 5 : Styliser votre message in-app {#step-5-style-your-in-app-message}

L'onglet **Style** vous permet d'ajuster tous les aspects visuels de votre message. Téléchargez une image ou un badge, ou choisissez une icône de badge prédéfinie. Modifiez les couleurs de l'en-tête et du corps du texte, des boutons et de l'arrière-plan en sélectionnant dans une palette ou en saisissant un code hexadécimal, RVB ou TSL.

Le contenu de l'onglet **Style** varie en fonction des options de message choisies à l'étape précédente, mais peut inclure l'une des options suivantes :

| Mise en forme | Saisie | Description |
|---|---|---|
| [Profil de couleur]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/in_app_message_template#reusable-color-profiles) | Appliquer depuis la galerie de modèles de messages in-app. | Sélectionnez **Apply Template** et choisissez dans la galerie. Puis, sélectionnez **Save**. |
| Alignement du texte | Gauche, centre ou droite. | Disponible uniquement pour les versions plus récentes du SDK Braze. |
| En-tête | Code couleur HEX. | La couleur HEX souhaitée s'affichera. Vous pourrez également choisir l'opacité de la couleur. |
| Texte | Code couleur HEX. | La couleur HEX souhaitée s'affichera. Vous pourrez également choisir l'opacité de la couleur. |
| Boutons | Code couleur HEX. | Les couleurs HEX souhaitées s'afficheront. Vous pourrez également choisir l'opacité des couleurs. Vous pouvez choisir les couleurs pour : l'arrière-plan du bouton de fermeture du message ainsi que l'arrière-plan, le texte et la bordure de chaque bouton. |
| Bordure du bouton | Code couleur HEX. | Nouveau ! Cela vous permettra de distinguer vos boutons principal et secondaire l'un de l'autre. Nous suggérons de délimiter les boutons avec des couleurs contrastantes. |
| Couleur d'arrière-plan | Code couleur HEX. | La couleur HEX souhaitée s'affichera. Vous pourrez également choisir l'opacité de la couleur. C'est l'arrière-plan de l'ensemble du message et il s'affichera clairement derrière le corps de votre texte. |
| Overlay de l'écran | Code couleur HEX. | La couleur HEX souhaitée s'affichera. Vous pourrez également choisir l'opacité de la couleur. Disponible uniquement pour les versions plus récentes du SDK Braze. C'est le cadre autour de l'ensemble du message. |
| Chevron ou autre option de fermeture du message | Code couleur HEX. | La couleur HEX souhaitée s'affichera. Vous pourrez également choisir l'opacité de la couleur. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 5 : Styliser votre message in-app" }

[Prévisualisez et testez]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) toujours votre message avant de l'envoyer.

{% alert important %}
Certains types de messages in-app n'offrent pas d'option de style au-delà du téléchargement de HTML personnalisé (ou CSS ou JavaScript) et de ressources via un fichier ZIP. La [fenêtre modale web avec CSS]({{site.baseurl}}/user_guide/channels/in_app_messages/customize#web-modal-css) vous permet de télécharger ou d'écrire du CSS personnalisé pour créer des messages au style entièrement personnalisé et esthétique.
{% endalert %}

## Étape 6 : Configurer les paramètres supplémentaires (facultatif) {#step-6-configure-additional-settings-optional}

### Paires clé-valeur {#key-value-pairs}

Vous pouvez ajouter des [paires clé-valeur]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) pour envoyer des champs personnalisés supplémentaires aux appareils des utilisateurs.

1. Dans le compositeur de messages, sélectionnez l'onglet **Paramètres**.
2. Dans **Paires clé-valeur**, sélectionnez **Ajouter une nouvelle paire**.
3. Saisissez une clé et une valeur pour chaque paire. Pour ajouter une autre paire, sélectionnez à nouveau **Ajouter une nouvelle paire**.

## Étape 7 : Créez le reste de votre campagne ou Canvas {#step-7-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Créez le reste de votre campagne ; consultez les sections suivantes pour plus de conseils sur la meilleure façon d'utiliser nos outils pour créer des messages in-app.

### Choisir un déclencheur {#choose-a-trigger}

Sélectionnez l'action à partir de laquelle vous souhaitez déclencher votre message, ainsi que les dates et heures de début et de fin de votre campagne ou Canvas.

{% alert important %}
Notez que si vous avez l'intention de déclencher votre message in-app en fonction d'un événement personnalisé, cet événement personnalisé doit être envoyé via le SDK.
{% endalert %}

![Campaign basée sur une action avec l'action de déclenchement définie sur « Démarrer la session ».]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

La distribution des messages in-app est entièrement basée sur les actions de déclenchement suivantes :

- Passer une commande
- Ouvrir l'application ou la page web
- Effectuer un événement personnalisé (ne fonctionne qu'avec les événements envoyés via le SDK)
- Ouvrir une notification push spécifique
- Planifier automatiquement l'envoi de Campaigns à une heure précise en fonction de l'heure locale de chacun de vos utilisateurs.
- Les messages peuvent également être configurés pour se répéter sur une base quotidienne, hebdomadaire (éventuellement certains jours spécifiques) ou mensuelle.

Une date et une heure de début doivent être sélectionnées ; cependant, une date de fin est facultative. Une date de fin empêchera ce message in-app spécifique de s'afficher sur les appareils après la date/heure indiquée.

Consultez notre documentation développeur pour le [déclenchement d'événements côté serveur]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web) et la [distribution locale des messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web).

#### Déclenchement en ligne versus hors ligne {#online-versus-offline-triggering}

Les messages in-app fonctionnent en envoyant le message et les déclencheurs à l'appareil de l'utilisateur. Une fois les messages in-app sur l'appareil, ils attendent que la condition de déclenchement soit remplie pour s'afficher. Si les messages in-app sont déjà en cache sur l'appareil de l'utilisateur, vous pouvez même déclencher des messages in-app hors ligne, sans connexion à Braze (par exemple, en mode Avion).

{% alert important %}
Une fois qu'un message in-app a été arrêté, certains utilisateurs peuvent continuer à voir le message s'ils ont démarré une session avant l'arrêt du message et qu'ils effectuent ensuite l'événement déclencheur. Ces utilisateurs seront comptabilisés comme une impression unique même après l'arrêt de la campagne.
{% endalert %}

### Choisir une priorité {#choose-a-priority}

Enfin, après avoir sélectionné l'action qui déclenchera le message in-app, vous devez également définir une priorité. Si deux messages sont déclenchés par la même action, les messages à haute priorité seront programmés pour s'afficher sur les appareils des utilisateurs avant les messages de priorité inférieure.

Vous pouvez choisir parmi les priorités de message suivantes :

- Priorité élevée (affiché avant les autres messages)
- Priorité moyenne (par défaut)
- Priorité faible (affiché après les autres messages)

Les options de priorité élevée, moyenne et faible pour les messages déclenchés sont des compartiments, et en tant que tels, plusieurs messages peuvent avoir la même priorité sélectionnée. Lorsque plusieurs messages partagent la même priorité, le message le plus récemment créé ou attribué est prioritaire et s'affiche en premier :

- **Compartiment de priorité par défaut :** lorsque deux Campaigns partagent le même déclencheur et utilisent la priorité par défaut (moyenne), la Campaign créée en dernier reçoit le déclencheur.
- **Compartiment de priorité spécifique :** lorsque plusieurs Campaigns partagent le même déclencheur et sont attribuées à un compartiment de priorité spécifique, la Campaign la plus récemment attribuée à ce compartiment reçoit le déclencheur.

Pour définir les priorités au sein de ces compartiments, cliquez sur **Set exact priority**, et vous pouvez glisser-déposer les Campaigns pour les organiser dans le bon ordre de priorité.

![Un exemple de la façon dont la priorité est définie pour une Campaign et un Canvas de messages in-app.]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

### Choisir les utilisateurs à cibler {#choose-users-to-target}

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) en choisissant des Segments ou des filtres pour affiner votre audience. Vous recevez automatiquement un aperçu de la population approximative de ce Segment. Gardez à l'esprit que l'appartenance exacte au Segment est toujours calculée avant l'envoi du message.

{% alert note %}
S'il y a un délai sur l'étape de message in-app, l'appartenance au Segment sera évaluée après le délai. Si l'utilisateur est éligible, le message in-app sera synchronisé lors de la prochaine session disponible.
{% endalert %}

#### Réévaluer l'éligibilité de la Campaign et le Liquid {#re-evaluate-campaign-eligibility-and-liquid}

Dans certains cas, vous souhaiterez peut-être réévaluer l'éligibilité d'un utilisateur lorsqu'il déclenche l'affichage d'un message in-app. Par exemple, les Campaigns qui ciblent un attribut personnalisé qui change fréquemment, ou les messages qui doivent refléter les modifications de profil de dernière minute.

![Case à cocher « Réévaluer l'éligibilité de la Campaign avant l'affichage » sélectionnée.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}){:style="max-width:60%"}

Lorsque vous sélectionnez **Re-evaluate campaign eligibility before displaying**, une requête supplémentaire est envoyée à Braze pour confirmer que l'utilisateur est toujours éligible à ce message avant son envoi. De plus, toutes les variables [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) ou le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) seront mis en forme à ce moment, avant l'affichage du message.

Cela empêche l'envoi de messages in-app aux utilisateurs dans le cadre de Campaigns expirées ou archivées. Si vous ne réévaluez pas l'éligibilité d'un utilisateur, celui-ci recevra le message in-app même après l'expiration ou l'archivage de la Campaign, car le message est dans votre SDK et attend que les utilisateurs le déclenchent.

{% alert note %}
L'activation de cette option entraînera un léger délai (< 100 ms) entre le moment où un utilisateur déclenche un message in-app et celui où le message s'affiche, en raison de la requête supplémentaire d'éligibilité et de mise en forme.
<br><br>
N'utilisez pas cette option pour les messages qui peuvent être déclenchés lorsqu'un utilisateur est hors ligne ou lorsque la réévaluation de l'éligibilité et du Liquid n'est pas nécessaire.
{% endalert %}

#### Utiliser des données ajoutées par la REST API dans un message {#use-data-added-by-rest-api-in-a-message}

Les données utilisateur ajoutées par l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) au cours de la même session peuvent parfois être utilisées dans le message in-app de cet utilisateur. Par exemple, si un utilisateur fait partie de l'audience d'un message in-app en attente d'un déclencheur, démarre une session, et que durant cette même session la REST API met à jour son profil, ces nouvelles données peuvent apparaître dans le message in-app lorsque **Re-evaluate campaign eligibility before displaying** est sélectionné. Braze ne met pas en forme le message in-app avant le moment de l'affichage.

Si un déclencheur envoie à la fois des données à Braze et déclenche le message in-app, le message ne peut pas utiliser ces données de profil nouvellement mises à jour, même avec un délai planifié. Utilisez plutôt deux déclencheurs distincts : un pour envoyer les données, et un pour déclencher le message in-app.

### Choisir les événements de conversion {#choose-conversion-events}

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre allant jusqu'à 30 jours pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

{% endtab %}
{% tab Canvas %}

Si ce n'est pas encore fait, complétez les sections restantes de votre composant Canvas. Pour plus de détails sur la création du reste de votre Canvas, y compris les tests multivariés et [Optimiser avec BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai), consultez [Créer votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas).

Pour plus d'informations sur les options de messages in-app spécifiques à Canvas, consultez [Messages in-app dans Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas).

{% endtab %}
{% endtabs %}

## Étape 8 : Vérifier et déployer {#step-8-review-and-deploy}

Après avoir terminé la création de votre Campaign ou Canvas, vérifiez ses détails, [testez-le]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message), puis envoyez-le !

Ensuite, consultez [Reporting des messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) pour découvrir comment accéder aux résultats de vos Campaigns de communication.

## Informations à connaître {#things-to-know}

### Limites des campagnes de messages in-app actives {#active-in-app-message-campaign-limits}

Braze accorde une grande importance à la fiabilité et à la rapidité. Nous vous suggérons de n'envoyer que les données dont vous avez besoin à Braze et de désactiver toute campagne qui n'apporte plus de valeur à votre marque.

Le traitement des campagnes de messages in-app basées sur des actions qui sont toujours actives mais qui n'envoient plus de messages ou qui ne sont plus nécessaires ralentit les performances globales des services Braze pour vous et pour les autres clients. Ce temps supplémentaire nécessaire au traitement de ces grands nombres de campagnes inactives signifie que l'affichage de tout message in-app sur les appareils des utilisateurs finaux prendra plus de temps, ce qui impacte l'expérience de l'utilisateur final.

{% alert important %}
Vous pouvez avoir jusqu'à 200 campagnes de messages in-app actives et basées sur des actions par espace de travail afin d'optimiser la rapidité de distribution des messages et d'éviter les dépassements de délai. Cela ne s'applique pas aux Canvas.
{% endalert %}

Le comptage de 200 inclut les campagnes de messages in-app actives qui n'ont pas encore atteint leur date de fin ainsi que celles qui n'ont pas de date de fin. Les campagnes de messages in-app actives dont la date de fin est dépassée ne sont pas comptabilisées. Le client Braze moyen a un total de 26 campagnes actives simultanément, il est donc peu probable que cette limitation vous impacte.

### Évaluation de la diffusion selon l'heure locale {#local-time-delivery-evaluation}

Lorsqu'une campagne de message in-app est planifiée en fonction du fuseau horaire local de l'utilisateur, l'évaluation des heures de début et de fin de la campagne est gérée directement sur l'appareil.

Les campagnes de messages in-app sont généralement envoyées à l'appareil d'un utilisateur au démarrage ou à l'actualisation de la session de l'application. À ce moment :

1. Le SDK évalue si l'utilisateur est éligible à des messages in-app basés sur des déclencheurs.
2. L'appareil vérifie si l'événement déclencheur de l'utilisateur a eu lieu dans la période de début et de fin de la campagne (telle que définie par le fuseau horaire local de l'utilisateur).
3. Si les deux conditions sont remplies, le message in-app est éligible à l'affichage.

#### Considérations {#considerations}

- Si un utilisateur déclenche un événement (comme un appui sur un bouton) peu après la distribution du message in-app, le message peut ne pas apparaître avant la prochaine actualisation de session, en supposant que tous les critères d'éligibilité soient toujours remplis.
- Comme pour les autres types de canaux, les campagnes de messages in-app devraient idéalement être lancées 24 à 48 heures à l'avance. Ce délai donne aux utilisateurs suffisamment de temps pour remplir les critères d'éligibilité et initier une session afin que le message soit évalué et affiché.