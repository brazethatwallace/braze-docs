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

Commencez par choisir les plateformes qui doivent recevoir le message. Utilisez cette sélection pour limiter la diffusion d'une campagne à un ensemble spécifique d'applications. Par exemple, vous pouvez choisir **Web Browsers** pour un message dans le navigateur encourageant les utilisateurs à télécharger votre application mobile, afin de vous assurer qu'ils ne reçoivent pas le message après avoir déjà obtenu votre application. Étant donné que les sélections de plateformes sont spécifiques à chaque variante, vous pouvez essayer de tester l'engagement par message et par plateforme.

| Plateforme                        | Diffusion du message             |
|---------------------------------|------------------------------|
| Mobile Apps                     | SDK iOS, Android et Vega |
| Web Browsers                    | SDK Web                      |
| Both Mobile Apps & Web Browsers | SDK iOS, Android, Vega et Web |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Spécifier les plateformes de diffusion" }

## Étape 3 : Spécifier vos types de messages {#step-3-specify-your-message-types}

Une fois que vous avez sélectionné une plateforme d'envoi, parcourez les types de messages, les mises en page et les autres options qui y sont associées. Pour en savoir plus sur le comportement attendu et l'apparence de chacun de ces messages, consultez notre page [Types de messages]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types) ou cliquez sur les types de messages liés dans les tableaux suivants.

Lorsque vous choisissez le type de message à utiliser, tenez compte de l'espace que votre message occupera et de la manière dont il pourrait perturber l'expérience utilisateur.

- Les messages **contextuels** sont les moins intrusifs, apparaissant de manière subtile sans bloquer le contenu.
- Les messages **modaux** se situent au milieu : suffisamment visibles pour attirer l'attention sans prendre entièrement le contrôle de l'écran.
- Les messages **plein écran** sont les plus accrocheurs et les plus adaptés aux annonces importantes ou aux promotions.

Plus votre contenu est complexe, plus vous aurez besoin d'espace, et plus votre message risque d'interrompre le flux de l'utilisateur.

### Types de messages {#message-types}

Ces messages in-app sont acceptés à la fois par les applications mobiles et les applications web.

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
    <td>Messages qui couvrent la totalité de l'écran avec un bloc de message.</td>
    <td>
      <ul>
      <li>Image et texte</li>
      <li>Image uniquement</li>
      </ul>
    </td>
    <td>Orientation de l'appareil imposée (portrait ou paysage)</td>
    <td>Grand et audacieux ! À utiliser lorsque vous voulez vous assurer que les utilisateurs voient votre contenu, comme vos Campaigns les plus importantes, des notifications essentielles ou des promotions majeures.<br><br>Notez que sur les appareils mobiles, les messages en portrait et en paysage ne s'afficheront pas si l'orientation de l'appareil ne correspond pas à l'orientation du message.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/modal'>Fenêtre modale</a></td>
    <td>Messages qui couvrent la totalité de l'écran avec un overlay et un bloc de message.</td>
    <td>
      <ul>
      <li>Texte (avec image optionnelle)</li>
      <li>Image uniquement</li>
      </ul>
    </td>
    <td>N/A</td>
    <td>Un bon compromis. À utiliser lorsque vous avez besoin d'un moyen évident d'attirer l'attention de vos utilisateurs, comme les encourager à essayer une nouvelle fonctionnalité ou à profiter d'une promotion.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/slideup'>Contextuel</a></td>
    <td>Messages qui glissent dans la vue à un emplacement désigné sans bloquer le reste de l'écran.</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Discret : occupe le moins d'espace à l'écran. À utiliser pour alerter les utilisateurs sur de petites informations, comme de nouvelles fonctionnalités, des annonces, l'utilisation de cookies, etc.<br></td>
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
    <td>L'option d'initialisation <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> doit être définie sur <code>true</code> pour que votre message in-app fonctionne.</td>
    <td>C'est une bonne option si vous souhaitez tous les avantages des messages in-app tout en ayant besoin de fonctionnalités supplémentaires ou d'une apparence fidèle à votre marque. Vous pouvez modifier chaque détail du message : police, couleur, forme, taille, boutons, etc. <br><br>Exemples de cas d'usage : demander aux utilisateurs leur avis sur l'application, formulaires de capture d'e-mail ou messages paginés</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/email_capture_form'>Formulaire de capture d'e-mail</a></td>
    <td>Généralement utilisé pour capturer l'e-mail du visiteur.</td>
    <td>N/A</td>
    <td>L'option d'initialisation <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> doit être définie sur <code>true</code> pour que votre message in-app fonctionne.</td>
    <td>Lorsque vous invitez les utilisateurs à soumettre leur adresse e-mail.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/customize#web-modal-css'>Fenêtre modale web avec CSS</a></td>
    <td>Messages modaux pour le web avec CSS personnalisable.</td>
    <td>
      <ul>
      <li>Texte (avec image optionnelle)</li>
      <li>Image uniquement</li>
      </ul>
    </td>
    <td>La fenêtre modale web avec CSS est propre au SDK Web et ne peut être utilisée qu'après avoir sélectionné <b>Web Browsers</b>.</td>
    <td>Lorsque vous souhaitez importer ou écrire du CSS personnalisé pour créer des communications au style entièrement personnalisé et visuellement soignées.</td>
  </tr>
</tbody>
</table>

{% alert important %}
Si Braze détecte que vous n'avez pas inclus de bouton de fermeture ou de rejet dans votre code, nous vous demanderons d'en ajouter un. Pour votre commodité, nous avons fourni un extrait de code que vous pouvez copier et coller dans votre code : <br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## Étape 4 : Composez votre message in-app {#step-4-compose-your-in-app-message}

L'onglet **Composer** vous permet de modifier tous les aspects du contenu et du comportement de votre message.

![Exemple de message in-app d'une marque pour accueillir de nouveaux clients et les inviter à configurer un profil utilisateur.]({% image_buster /assets/img_archive/iam_compose.png %}){: style="max-width:85%" }

Le contenu de l'onglet **Composer** varie en fonction des options de message choisies à l'étape précédente, mais peut inclure l'une des options suivantes :

### Langue {#language}

Sélectionnez **Ajouter des langues** et choisissez les langues souhaitées dans la liste proposée. Cela insérera du [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) dans votre message. Nous vous recommandons de sélectionner vos langues avant de rédiger votre contenu afin de pouvoir remplir votre texte aux emplacements appropriés dans le Liquid. Consultez notre [liste complète des langues disponibles]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported).

### Image {#image}

Selon votre type de message, vous pouvez **Télécharger une image**, **Choisir un badge** ou utiliser **Font Awesome**. Pour télécharger une image, sélectionnez **Ajouter une image** ou fournissez une URL d'image. Sélectionner **Ajouter une image** ouvre la **bibliothèque multimédia**, où vous pouvez choisir une image précédemment téléchargée ou en ajouter une nouvelle. Chaque type de message et plateforme peut avoir ses propres proportions et exigences suggérées — assurez-vous de vérifier ces informations avant de commander ou de créer une image de zéro.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### En-tête et corps {#header-and-body}

Rédigez ce que vous souhaitez ! Incluez du texte entièrement personnalisé (souvent avec des fonctionnalités HTML personnalisées) avec les options d'inclusion de [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) et d'autres types de personnalisation. Plus vite vous transmettez votre message et incitez votre client à cliquer, mieux c'est ! Nous recommandons des en-têtes et un contenu de message clairs et concis.

Certains types de messages ne nécessitent pas d'en-tête et n'en demandent donc pas.

#### Conseils {#tips}

##### Générer du texte avec l'IA {#generating-ai-copy}

Besoin d'aide pour créer un texte percutant ? Essayez d'utiliser l'[assistant de rédaction IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Saisissez un nom ou une description de produit et l'IA générera un texte marketing au style naturel à utiliser dans vos communications.

![Bouton de lancement de l'assistant de rédaction IA, situé dans le champ Message du compositeur de messages in-app.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### Créer des messages de droite à gauche {#creating-right-to-left-messages}

Besoin d'aide pour rédiger des messages de droite à gauche pour des langues comme l'arabe et l'hébreu ? Consultez [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages) pour les bonnes pratiques.

### Texte des boutons {#buttons}

Lorsque cette option est disponible pour votre type de message, vous pouvez faire apparaître jusqu'à deux boutons sous le corps de votre texte. Vous pouvez créer et modifier le texte et la couleur des boutons personnalisés. Vous pouvez également ajouter un lien vers les conditions d'utilisation dans les formulaires de capture d'e-mail.

Si vous choisissez de n'utiliser qu'un seul bouton, il s'ajustera automatiquement pour occuper l'espace disponible en bas de votre message au lieu de laisser de la place pour un bouton supplémentaire.

#### Choisir un bouton principal {#choosing-a-primary-button}

Si vous décidez de formater ces boutons avec vos propres couleurs, nous vous recommandons d'utiliser le bouton 2 pour le résultat que vous préférez.

En d'autres termes, si vous souhaitez que votre utilisateur clique sur un bouton plutôt que sur l'autre, assurez-vous qu'il s'agit du bouton secondaire. Le bouton secondaire a souvent affiché un meilleur potentiel de clics, surtout s'il a une couleur quelque peu contrastée ou qui se démarque du reste du message. Cela est d'autant plus marqué lorsque le bouton principal se fond davantage visuellement dans le message.

![Boutons principal et secondaire dans un message in-app]({% image_buster /assets/img/primary-secondary-buttons.png %})

### Comportement au clic {#button-actions}

Lorsque votre client clique sur un bouton de votre message in-app, les actions suivantes sont disponibles.

| Action | Description |
|---|---|
| Rediriger vers une URL web | Ouvre une page web non native. |
| [Deep link vers l'application]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | Deep link vers un écran existant de votre application. |
| Fermer le message | Ferme le message actuellement actif. |
| Enregistrer un événement personnalisé | Choisissez un [événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events) à déclencher. Peut être utilisé pour afficher un autre message in-app ou déclencher des communications supplémentaires. |
| Enregistrer un attribut personnalisé | Choisissez un [attribut personnalisé]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) à définir pour l'utilisateur actuel. |
| Demander l'autorisation push | Affiche la demande d'autorisation push native. En savoir plus sur l'[amorçage push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages), ainsi que les [bonnes pratiques]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#best-practices) pour préparer les utilisateurs aux notifications push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportement au clic" }

Remarque : les options __Demander l'autorisation push__, __Enregistrer un événement personnalisé__ et __Enregistrer un attribut personnalisé__ nécessitent les versions minimales de SDK suivantes :

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Pour combiner plusieurs actions ou effectuer des actions SDK supplémentaires non disponibles dans le tableau de bord (comme l'ajout à un groupe d'abonnement ou la définition d'un type d'abonnement e-mail), vous pouvez utiliser les [deep links Braze Actions]({{site.baseurl}}/developer_guide/braze_actions).

### Options pour appareils iOS {#ios-device-options}

Si vous le souhaitez, vous pouvez restreindre votre message in-app pour qu'il ne soit envoyé qu'aux appareils iOS. Pour ce faire, cliquez sur **Modifier** et sélectionnez **Envoyer uniquement aux appareils iOS**.

### Fermeture du message {#message-close}

Choisissez parmi les options suivantes :

- **Fermeture automatique :** Sélectionnez le nombre de secondes pendant lesquelles le message restera à l'écran.
- **Attendre le balayage ou le toucher de l'utilisateur :** Nécessite une option de fermeture ou de rejet.

La fermeture d'un message enregistre une impression mais pas un clic. Pour savoir comment les clics sont suivis par action de l'utilisateur, consultez [Suivi des clics]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting#click-tracking).

### Position du contextuel {#slide-up-position}

Ce paramètre s'applique uniquement au type de message contextuel. Choisissez entre faire apparaître votre contextuel **Depuis le bas de l'écran de l'application** ou **Depuis le haut de l'écran de l'application**.

### HTML et ressources {#html-and-assets}

Ce paramètre s'applique uniquement au type de message code personnalisé. Copiez et collez du HTML dans l'espace disponible et téléchargez vos ressources à l'aide d'un fichier ZIP.

### Marque substitutive du champ de saisie de capture d'e-mail {#email-capture-input-placeholder}

Ce paramètre s'applique uniquement au type de message formulaire de capture d'e-mail. Saisissez un texte personnalisé qui apparaîtra comme texte de remplacement dans le champ de saisie de l'e-mail. Par défaut, il affiche « Enter your email address ».

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

## Étape 7 : Construire le reste de votre campagne ou Canvas {#step-7-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Construisez le reste de votre campagne ; consultez les sections suivantes pour obtenir des conseils supplémentaires sur la meilleure façon d'utiliser nos outils pour créer des messages in-app.

### Choisir un déclencheur {#choose-a-trigger}

Sélectionnez l'action à partir de laquelle vous souhaitez déclencher votre message, ainsi que les dates et heures de début et de fin de votre campagne ou Canvas.

{% alert important %}
Notez que si vous avez l'intention de déclencher votre message in-app à partir d'un événement personnalisé, cet événement personnalisé doit être envoyé via le SDK.
{% endalert %}

![Campaign basée sur une action avec l'action de déclenchement définie sur « Démarrer la session ».]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

La distribution des messages in-app repose entièrement sur les actions de déclenchement suivantes :

- Passer une commande
- Ouvrir l'application ou la page web
- Effectuer un événement personnalisé (fonctionne uniquement avec les événements envoyés via le SDK)
- Ouvrir un message push spécifique
- Planifier automatiquement l'envoi des campagnes à une heure précise en fonction de l'heure locale de chacun de vos utilisateurs.
- Les messages peuvent également être configurés pour se répéter quotidiennement, hebdomadairement (éventuellement certains jours spécifiques) ou mensuellement.

Une date et une heure de début doivent être sélectionnées ; cependant, une date de fin est facultative. Une date de fin empêchera ce message in-app spécifique de s'afficher sur les appareils après la date/heure spécifiée.

Consultez notre documentation développeur pour le [déclenchement d'événements côté serveur]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web) et la [distribution locale des messages in-app]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery#local-in-app-messages).

#### Déclenchement en ligne versus hors ligne {#online-versus-offline-triggering}

Les messages in-app fonctionnent en envoyant le message et les déclencheurs à l'appareil de l'utilisateur. Une fois les messages in-app sur un appareil, ils attendent que la condition de déclenchement soit remplie pour s'afficher. Si les messages in-app sont déjà mis en cache sur l'appareil de l'utilisateur, vous pouvez même déclencher des messages in-app hors ligne sans connexion à Braze (par exemple, en mode avion).

{% alert important %}
Une fois qu'un message in-app a été arrêté, il est possible que certains utilisateurs continuent à voir le message s'ils ont démarré une session avant l'arrêt du message et effectuent ensuite l'événement déclencheur. Ces utilisateurs seront comptabilisés comme une impression unique même après l'arrêt de la campagne.
{% endalert %}

### Choisir une priorité {#choose-a-priority}

Enfin, après avoir sélectionné l'action à partir de laquelle le message in-app sera déclenché, vous devez également définir une priorité. Si deux messages sont déclenchés par la même action, les messages à haute priorité seront programmés pour s'afficher sur les appareils des utilisateurs avant les messages à priorité inférieure.

Vous pouvez choisir parmi les priorités de message suivantes :

- Priorité haute (affiché avant les autres messages)
- Priorité moyenne (par défaut)
- Priorité basse (affiché après les autres messages)

Les options haute, moyenne et basse pour les priorités des messages déclenchés sont des compartiments, et plusieurs messages peuvent donc avoir la même priorité sélectionnée. Lorsque plusieurs messages partagent la même priorité, le message le plus récemment créé ou assigné prend le dessus et s'affiche en premier :

- **Compartiment de priorité par défaut :** lorsque deux campagnes partagent le même déclencheur et utilisent la priorité par défaut (moyenne), la campagne créée en dernier reçoit le déclencheur.
- **Compartiment de priorité spécifique :** lorsque plusieurs campagnes partagent le même déclencheur et sont assignées à un compartiment de priorité spécifique, la campagne la plus récemment assignée à ce compartiment reçoit le déclencheur.

Pour définir les priorités au sein de ces compartiments, cliquez sur **Set exact priority**, et vous pouvez glisser-déposer les campagnes pour les ordonner avec la priorité correcte.

![Exemple de la façon dont la priorité est définie pour une campagne de message in-app et un Canvas.]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

### Choisir les utilisateurs à cibler {#choose-users-to-target}

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) en choisissant des segments ou des filtres pour affiner votre audience. Vous recevez automatiquement un aperçu de la population approximative de ce segment. Gardez à l'esprit que l'appartenance exacte au segment est toujours calculée avant l'envoi du message.

{% alert note %}
S'il y a un délai sur l'étape de message in-app, l'appartenance au segment sera évaluée après le délai. Si l'utilisateur est éligible, le message in-app sera synchronisé lors de la prochaine session disponible.
{% endalert %}

#### Réévaluer l'éligibilité de la campagne et le Liquid {#re-evaluate-campaign-eligibility-and-liquid}

Dans certains scénarios, vous pouvez souhaiter réévaluer l'éligibilité d'un utilisateur lorsqu'il déclenche l'affichage d'un message in-app. Les exemples incluent les campagnes qui ciblent un attribut personnalisé qui change fréquemment ou les messages qui doivent refléter les modifications de profil de dernière minute.

![Case à cocher « Réévaluer l'éligibilité de la campagne avant l'affichage » sélectionnée.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}){:style="max-width:60%"}

Lorsque vous sélectionnez **Re-evaluate campaign eligibility before displaying**, une requête supplémentaire sera envoyée à Braze pour confirmer que l'utilisateur est toujours éligible à ce message avant l'envoi. De plus, toutes les variables [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) ou de [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) seront modélisées à ce moment-là avant l'affichage du message.

Cela empêche l'envoi de messages in-app aux utilisateurs dans le cadre de campagnes expirées ou archivées. Si vous ne réévaluez pas l'éligibilité d'un utilisateur, celui-ci recevra le message in-app même après l'expiration ou l'archivage de la campagne, car le message se trouve dans votre SDK et attend que les utilisateurs le déclenchent.

{% alert note %}
L'activation de cette option entraînera un léger délai (< 100 ms) entre le moment où un utilisateur déclenche un message in-app et le moment où le message s'affiche, en raison de la requête supplémentaire d'éligibilité et de modélisation.
<br><br>
N'utilisez pas cette option pour les messages qui peuvent être déclenchés lorsqu'un utilisateur est hors ligne ou lorsque la réévaluation de l'éligibilité et du Liquid n'est pas nécessaire.
{% endalert %}

#### Utiliser les données ajoutées par la REST API dans un message {#use-data-added-by-rest-api-in-a-message}

Les données utilisateur ajoutées par l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) au cours de la même session peuvent parfois être utilisées dans le message in-app de cet utilisateur. Par exemple, si un utilisateur fait partie de l'audience d'un message in-app en attente d'un déclencheur, démarre une session, et que dans cette même session la REST API met à jour son profil, ces nouvelles données peuvent apparaître dans le message in-app lorsque **Re-evaluate campaign eligibility before displaying** est sélectionné. Braze ne modélisera pas le message in-app tant qu'il ne sera pas temps de l'afficher.

Si un déclencheur envoie à la fois des données à Braze et déclenche le message in-app, le message ne peut pas utiliser ces données de profil nouvellement mises à jour, même avec un délai planifié. Utilisez plutôt deux déclencheurs distincts : un pour envoyer les données, et un pour déclencher le message in-app.

### Choisir les événements de conversion {#choose-conversion-events}

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre allant jusqu'à 30 jours pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

{% endtab %}
{% tab Canvas %}

Si ce n'est pas déjà fait, complétez les sections restantes de votre composant Canvas. Pour plus de détails sur la façon de construire le reste de votre Canvas, mettre en œuvre les tests multivariés et la sélection intelligente, et plus encore, consultez l'étape [Construire votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas) de notre documentation Canvas.

Pour des informations sur les options de messages in-app spécifiques à Canvas, consultez [Messages in-app dans Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas).

{% endtab %}
{% endtabs %}

## Étape 8 : Vérifier et déployer {#step-8-review-and-deploy}

Après avoir terminé la création de votre Campaign ou Canvas, vérifiez ses détails, [testez-le]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message), puis envoyez-le !

Consultez ensuite la section [Rapports sur les messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) pour découvrir comment accéder aux résultats de vos Campaigns de communication.

## Ce qu'il faut savoir {#things-to-know}

### Limites des campagnes de messages in-app actives {#active-in-app-message-campaign-limits}

Braze accorde une grande importance à la fiabilité et à la rapidité. Nous vous suggérons de n'envoyer à Braze que les données dont vous avez besoin et de désactiver toute campagne qui n'apporte plus de valeur à votre marque.

Le traitement des campagnes de messages in-app basées sur des actions qui sont toujours actives mais qui n'envoient plus de messages ou qui ne sont plus nécessaires ralentit les performances globales des services Braze pour vous et pour les autres clients. Ce temps supplémentaire nécessaire au traitement de ces grands nombres de campagnes inactives signifie que les messages in-app mettront plus de temps à apparaître sur les appareils des utilisateurs finaux, ce qui impacte leur expérience.

{% alert important %}
Vous pouvez avoir jusqu'à 200 campagnes de messages in-app actives et basées sur des actions par espace de travail afin d'optimiser la vitesse de distribution des messages et d'éviter les délais d'expiration. Cela ne s'applique pas aux Canvas.
{% endalert %}

Le compteur de 200 inclut les campagnes de messages in-app actives qui n'ont pas encore atteint leur date de fin ainsi que celles qui n'ont pas de date de fin. Les campagnes de messages in-app actives dont la date de fin est dépassée ne sont pas comptabilisées. Le client Braze moyen a un total de 26 campagnes actives simultanément, il est donc peu probable que cette limitation vous affecte.

### Évaluation de la diffusion selon l'heure locale {#local-time-delivery-evaluation}

Lorsqu'une campagne de messages in-app est planifiée en utilisant le fuseau horaire local de l'utilisateur, l'évaluation des heures de début et de fin de la campagne est gérée directement sur l'appareil.

Les campagnes de messages in-app sont généralement envoyées à l'appareil de l'utilisateur lorsque la session de l'application démarre ou s'actualise. À ce moment-là :

1. Le SDK évalue si l'utilisateur est éligible à des messages in-app basés sur des déclencheurs.
2. L'appareil vérifie si l'événement déclencheur de l'utilisateur s'est produit dans la période de début et de fin de la campagne (telle que définie par le fuseau horaire local de l'utilisateur).
3. Si les deux conditions sont remplies, le message in-app est éligible à l'affichage.

#### Considérations {#considerations}

- Si un utilisateur déclenche un événement (comme un appui sur un bouton) peu après la distribution du message in-app, le message peut ne pas apparaître avant la prochaine actualisation de session, en supposant que tous les critères d'éligibilité sont toujours remplis.
- Comme pour les autres types de canaux, les campagnes de messages in-app devraient idéalement être lancées 24 à 48 heures à l'avance. Ce délai donne aux utilisateurs suffisamment de temps pour remplir les critères d'éligibilité et initier une session afin que le message soit évalué et affiché.