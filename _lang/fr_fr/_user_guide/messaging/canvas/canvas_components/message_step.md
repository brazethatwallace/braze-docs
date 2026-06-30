---
nav_title: Message
article_title: Message
alias: "/message_step/"
page_order: 11
page_type: reference
description: "Cet article de référence explique comment créer un message autonome à l'aide de l'étape Message."
tool: Canvas

---

# Message {#message}

> Les étapes Message vous permettent d'ajouter un message autonome à l'endroit de votre choix dans votre Canvas.

![Une étape Message nommée « Lunch promo » utilisant le canal push.]({% image_buster /assets/img/canvas_components/message_step1.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

## Créer un message {#create-a-message}

Pour créer un composant Message, commencez par ajouter une étape à votre Canvas. Glissez-déposez le composant depuis la barre latérale, ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape et sélectionnez **Message**.

### Étape 1 : Sélectionnez votre canal de communication {#step-1-select-your-messaging-channel}

Vous pouvez choisir parmi les canaux de communication suivants :
- Bannières
- Content Cards
- E-mail
- LINE
- Notifications push
- SMS/MMS/RCS
- Messages in-app
- Webhook
- WhatsApp

![Une liste des canaux de communication disponibles à sélectionner pour l'étape Message.]({% image_buster /assets/img/canvas_components/message_step2.png %})

### Étape 2 : Modifiez les paramètres de distribution {#step-2-edit-delivery-settings}

Ensuite, vous pouvez modifier les paramètres de timing intelligent, de remplacement des heures calmes et de validation de la distribution.

#### Timing intelligent {#intelligent-timing}

Vous pouvez activer le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) avec une option de repli lorsque le profil d'un utilisateur ne dispose pas de suffisamment de données pour calculer un horaire optimal. Nous recommandons d'activer le timing intelligent et la [limite de débit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#rate-limiting-and-frequency-capping) comme vérification supplémentaire pour tout délai entre le moment où les utilisateurs entrent dans l'étape Message et l'envoi effectif du message.

Sélectionnez **Using Intelligent Timing** dans l'onglet **Delivery Settings**. Vous pouvez choisir l'heure la plus populaire ou une heure de repli spécifique. Si les heures calmes sont activées, l'étape Message vous permet également de remplacer ce paramètre.

![L'onglet Delivery Settings pour les paramètres du composant Message. Les heures calmes sont activées et la case Using Intelligent Timing est cochée pour distribuer le message à un horaire optimal.]({% image_buster /assets/img/canvas_components/message_step4.png %}){: style="max-width:90%;"}

#### Validations de distribution {#delivery-validations}

Les validations de distribution fournissent une vérification supplémentaire au moment de l'envoi du message pour confirmer que votre audience remplit toujours vos critères. Nous recommandons de les utiliser lorsque les heures calmes, le timing intelligent ou la limite de débit sont activés. Sélectionnez **Validate audience at message send**, puis ajoutez un segment ou des filtres supplémentaires. Si un utilisateur ne remplit pas les validations, choisissez s'il quitte le Canvas ou passe à l'étape suivante.

Les validations de distribution évaluent les critères du profil utilisateur au moment de l'envoi. Les filtres liés aux applications vérifient si un utilisateur a récemment utilisé ou a déjà utilisé une application spécifique, mais ils ne confirment pas quelle application l'utilisateur utilise dans sa session en cours.

Si votre espace de travail comporte plusieurs applications et qu'une étape Message doit cibler une application spécifique, utilisez plutôt l'une des approches suivantes :

- Lors de la composition du message, [spécifiez vos plateformes de distribution]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#step-2-specify-delivery-platforms), telles que **Mobile Apps** ou **Web Browsers**.
- Utilisez Liquid pour vérifier l'appareil ou l'application ciblé(e) au moment de l'envoi :
  - {% raw %}`{{targeted_device.${platform}}}`{% endraw %} évalue la plateforme de la session en cours de l'utilisateur. Pour en savoir plus, consultez [Informations sur l'appareil ciblé]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#targeted-device-information).
  - {% raw %}`{{app.${api_id}}}`{% endraw %} évalue quelle application demande le message. Combinez cette balise avec `abort_message()` pour empêcher les envois vers la mauvaise application. Pour en savoir plus, consultez [Informations sur l'application ciblée]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#targeted-app-information).

![Les validations de distribution sont activées pour valider l'audience à l'envoi du message. Le comportement d'avancement des validations de distribution est configuré pour faire passer l'utilisateur à l'étape suivante du Canvas si les validations de distribution ne sont pas remplies.]({% image_buster /assets/img/canvas_components/message_step5.png %}){: style="max-width:90%;"}

## Comment les utilisateurs progressent {#how-users-advance}

Tous les utilisateurs qui entrent dans l'étape Message passent à l'étape suivante lorsque l'une des conditions suivantes est remplie :

- Un message est envoyé
- Un message est limité en fréquence et n'est pas envoyé
- Un message est abandonné
- Un utilisateur n'est pas joignable par le canal, le message n'est donc pas envoyé
- Un utilisateur ne remplit pas les critères des **validations de distribution**

{% raw %}
Si un Canvas basé sur une action est déclenché par un message SMS entrant, vous pouvez référencer les propriétés SMS dans la première étape (étape Message) ou dans une étape Message imbriquée sous une étape Parcours d'actions. Par exemple, dans l'étape Message, vous pouvez utiliser `{{sms.${inbound_message_body}}}` ou `{{sms.${inbound_media_urls}}}`.
{% endraw %}

## Référencer les propriétés de contexte {#reference-context-properties}

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

Les propriétés d'entrée sont configurées dans l'étape **Planification d'entrée** lors de la création d'un Canvas et indiquent le déclencheur qui fait entrer un utilisateur dans un Canvas. Ces propriétés permettent également d'accéder aux propriétés des payloads d'entrée dans les Canvas déclenchés par API. Notez que l'objet `context` a une taille maximale de 50 Ko.

Les propriétés d'entrée peuvent être utilisées en Liquid dans n'importe quelle étape Message. Utilisez le Liquid suivant pour référencer ces propriétés d'entrée : {% raw %}``{context.${property_name}}``{% endraw %}. Les événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière.

{% alert note %}
Pour les canaux de messages in-app en particulier, `context` ne peut être référencé que dans Canvas.
{% endalert %}

Utilisez le Liquid suivant pour référencer ces propriétés d'entrée : {% raw %}``context.${property_name}``{% endraw %}. Notez que les événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière.

{% raw %}
Par exemple, considérez la requête suivante : `"context" : {"product_name" : "shoes", "product_price" : 79.99}`. Vous pouvez ajouter le mot « shoes » à un message avec le Liquid `{{context.${product_name}}}`.
{% endraw %}

Vous pouvez également tirer parti des [propriétés d'entrée persistantes]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties) dans n'importe quelle étape Message pour guider vos utilisateurs à travers des étapes personnalisées tout au long de votre workflow Canvas.

### Propriétés d'événement {#event-properties}

Les propriétés d'événement font référence aux propriétés que vous définissez pour les événements personnalisés et les événements d'achat. Ces propriétés d'événement peuvent être utilisées dans les campagnes avec livraison par événement ainsi que dans les Canvas.

Dans Canvas, les propriétés d'événements personnalisés et d'événements d'achat peuvent être utilisées en Liquid dans n'importe quelle étape Message qui suit une étape [Parcours d'actions]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths). Par exemple, pour référencer `event_properties`, utilisez cet extrait Liquid : {% raw %}``{{event_properties.${property_name}}}``{% endraw %}

{% alert important %}
`event_properties` ne peut pas être utilisé indépendamment des étapes Parcours d'actions.
{% endalert %}

Dans la première étape Message suivant un parcours d'action, vous pouvez utiliser `event_properties` en lien avec l'événement référencé dans ce parcours d'action. Vous pouvez avoir d'autres étapes (qui ne sont pas un autre parcours d'action ou une étape Message) entre cette étape Parcours d'actions et l'étape Message. Notez que vous n'aurez accès à `event_properties` que si votre étape Message peut être retracée jusqu'à un parcours autre que Tous les autres dans une étape Parcours d'actions.

{% alert important %}
Vous ne pouvez pas utiliser `event_properties` dans la première étape Message. Vous devez plutôt utiliser `context` ou ajouter une étape Parcours d'actions avec l'événement correspondant avant l'étape Message qui inclut `event_properties`.
{% endalert %}

{% details Développer pour l'éditeur Canvas d'origine %}

Vous ne pouvez plus créer ni dupliquer de Canvas avec l'éditeur d'origine. Cette section est disponible à titre de référence uniquement.

- `event_properties` ne peut pas être utilisé dans les étapes complètes planifiées. Cependant, vous pouvez utiliser `event_properties` dans la première étape complète d'un Canvas basé sur une action, même si l'étape complète est planifiée.
- `context` ne peut être référencé que dans la première étape complète d'un Canvas.
- Pour les canaux de messages in-app en particulier, `context` peut être référencé dans l'éditeur Canvas d'origine si les propriétés d'entrée persistantes sont activées dans le cadre de l'accès anticipé précédent.

{% enddetails %}

## Analytique {#analytics}

Consultez le tableau suivant pour les définitions des indicateurs du composant Message :

| Indicateur | Description |
| --- | --- |
| _Entrées_ | Le nombre de fois où l'étape a été atteinte. Si votre Canvas autorise la rééligibilité et qu'un utilisateur entre deux fois dans une étape Message, deux entrées seront enregistrées. |
| _Passé à l'étape suivante_ | Le nombre d'entrées qui sont passées à l'étape suivante du Canvas. |
| _Envois_ | Le nombre total de messages envoyés par l'étape. Si votre Canvas autorise la rééligibilité et qu'un utilisateur entre deux fois dans une étape Message, deux entrées seront enregistrées. |
| _Destinataires uniques_ | Le nombre d'utilisateurs ayant reçu des messages de cette étape. |
| _Événement de conversion principal_ | Le nombre de fois où un événement défini s'est produit après une interaction avec un message reçu d'une campagne Braze ou après sa consultation. Vous définissez cet événement lors de la création de la campagne. |
| _Chiffre d'affaires_ | Le chiffre d'affaires total en dollars provenant des destinataires de la campagne dans la fenêtre de conversion principale définie. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytique" }