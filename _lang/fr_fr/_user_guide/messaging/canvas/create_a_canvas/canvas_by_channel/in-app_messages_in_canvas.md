---
nav_title: Messages in-app
article_title: Messages in-app dans Canvas
alias: "/canvas_in-app_messages/"
page_order: 2
page_type: reference
description: "Cet article de référence décrit les fonctionnalités et les spécificités des messages in-app que vous pouvez ajouter à votre Canvas pour afficher des messages enrichis."
tool: Canvas
channel: in-app messages

---

# Messages in-app dans Canvas {#in-app-messages-in-canvas}

> Vous pouvez ajouter des messages in-app à votre parcours Canvas pour afficher des messages enrichis lorsque vos clients interagissent avec votre application.

## Fonctionnement {#how-it-works}

Avant de pouvoir utiliser des messages in-app dans votre Canvas, assurez-vous d'avoir configuré un [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) avec des options de délai et d'audience.

Dans le générateur de Canvas, ajoutez une étape [Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) et sélectionnez **In-App Message** comme **Messaging Channel**. Vous pouvez personnaliser [la date d'expiration de votre message](#in-app-message-expiration) et le [comportement d'avancement](#advancement-behavior) associé.

Si votre espace de travail comporte plusieurs applications, ciblez la bonne application en utilisant les **plateformes de distribution**, les étiquettes Liquid {% raw %}`{{targeted_device.${platform}}}`{% endraw %} ou {% raw %}`{{app.${api_id}}}`{% endraw %}, et non les validations de distribution. Les messages in-app ne s'affichent que lorsque l'utilisateur ouvre l'application ciblée et remplit les critères de déclenchement de l'étape. Pour plus d'informations, consultez [Validations de distribution]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).

## Ajouter un message in-app à votre parcours utilisateur {#adding-an-in-app-message-to-your-user-journey}

Pour ajouter un message in-app à votre Canvas, procédez comme suit :

1. Ajoutez une étape [Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) à votre parcours utilisateur.
2. Sélectionnez **In-App Message** pour votre **Messaging Channel**.
3. Déterminez [la date d'expiration de votre message](#in-app-message-expiration) et le [comportement d'avancement](#advancement-behavior-options) associé.

## Messages in-app déclenchés {#triggered-in-app-messages}

Vous pouvez sélectionner un déclencheur pour que vos messages in-app soient déclenchés au démarrage de la session, ou par des événements personnalisés et des achats.

Une fois les délais écoulés et les options d'audience vérifiées, les messages in-app sont activés lorsqu'un utilisateur atteint l'étape Message. Si un utilisateur démarre une session et effectue l'événement déclencheur du message in-app, il verra le message in-app.

Pour les étapes Canvas dont l'entrée est déclenchée par une action, les utilisateurs peuvent entrer dans le Canvas en cours de session. Les messages in-app ne sont activés qu'au démarrage d'une session. Par conséquent, si un utilisateur est en cours de session lorsqu'il atteint l'étape Message, il ne recevra pas le message in-app tant qu'il n'aura pas démarré une nouvelle session et effectué le déclencheur correspondant.

## Expiration des messages in-app {#in-app-message-expiration}

Vous pouvez choisir la date d'expiration du message in-app. Pendant cette période, le message in-app restera en attente d'être consulté jusqu'à la date d'expiration. Une fois le message in-app envoyé, il ne peut être consulté qu'une seule fois.

![La section Contrôles du message d'une étape Message pour un message in-app. Le message in-app expire trois jours après que l'étape est disponible.]({% image_buster /assets/img_archive/canvas_expiration2.png %}){: style="max-width:90%"}

| Option | Description | Exemple |
|---|---|---|
| **Une durée après que l'étape est disponible** | Définit l'expiration du message in-app par rapport au moment où l'étape devient disponible pour l'utilisateur. | Un message in-app avec une expiration de deux jours deviendrait disponible lorsque l'utilisateur entre dans l'étape Message et que les options d'audience sont vérifiées. Tout délai avant d'atteindre cette étape proviendrait des étapes de délai précédentes dans votre Canvas. Le message in-app serait alors disponible pendant 2 jours (48 heures) à partir du moment où l'utilisateur entre dans l'étape, et pendant ces deux jours, les utilisateurs pourraient voir le message in-app s'ils ouvrent l'application. |
| **À une date et une heure spécifiques** | Sélectionnez une date et une heure spécifiques auxquelles le message in-app ne sera plus disponible. | Si vous avez une promotion qui se termine le 30 novembre 2024, sélectionnez cette option pour que les utilisateurs ne voient plus le message in-app associé lorsque la promotion prend fin. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Expiration des messages in-app" }

Lorsqu'un utilisateur démarre une session, Braze vérifie si son éligibilité ou l'expiration de ses messages in-app a changé et envoie les informations d'expiration mises à jour à son appareil.

Si un message in-app est configuré pour expirer à une date et une heure spécifiques qui sont déjà passées lorsque l'utilisateur atteint l'étape Message, cet utilisateur ne recevra pas le message in-app. Il continuera à travers le Canvas selon votre [comportement d'avancement](#advancement-behavior) pour cette étape.

Cela se produit souvent lorsqu'une étape précédente, comme une étape de [délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), maintient les utilisateurs sur un parcours plus long. Par exemple, si vous lancez un Canvas le 22 mai avec un délai de 72 heures suivi d'un message in-app qui expire le 23 mai à minuit, les utilisateurs atteindront l'étape Message après l'heure d'expiration et ne verront pas le message in-app.

### Groupes de contrôle et test A/B {#control-groups-and-ab-testing}

Lorsque vous utilisez le test A/B Canvas avec des parcours de variantes et un parcours de contrôle, veillez à aligner les paramètres de durée d'expiration des messages in-app entre les parcours. Si le parcours de contrôle utilise une durée d'expiration plus courte que les parcours de variantes, les utilisateurs du groupe de contrôle peuvent atteindre l'étape après l'expiration, ce qui peut réduire les impressions du groupe de contrôle par rapport aux impressions des variantes et fausser les résultats de votre test.

## Cas d'utilisation {#use-cases}

Braze vous recommande d'envisager l'utilisation de cette fonctionnalité dans vos Canvas promotionnels et d'onboarding.

{% tabs %}
  {% tab Promotionnel %}

Les promotions, coupons et soldes ont souvent des dates d'expiration fixes. Le Canvas suivant devrait alerter vos utilisateurs aux moments les plus opportuns qu'une promotion est disponible, et éventuellement influencer un achat. Cette promotion expire le 28 février 2019 à 11h15 dans le fuseau horaire de votre société.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table aria-label="Cas d'utilisation" class="tg">
  <caption>Cas d'utilisation</caption>
<thead>
  <tr>
    <th>Étape Canvas</th>
    <th>Délai</th>
    <th>Audience</th>
    <th>Canal</th>
    <th>Expiration</th>
    <th>Avancement</th>
    <th>Détails</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Jour 1 : 50 % de réduction</td>
    <td>Aucun</td>
    <td>Tous depuis l'entrée</td>
    <td>Push</td>
    <td>N/A</td>
    <td>Avancer l'audience après le délai</td>
    <td>Notification push initiale qui informe vos utilisateurs de la promotion. L'objectif est d'inciter les utilisateurs à ouvrir votre application pour profiter de la promotion.</td>
  </tr>
  <tr>
    <td>In-app : 50 % de réduction</td>
    <td>Aucun</td>
    <td>Tous depuis l'entrée</td>
    <td>Message in-app</td>
    <td><b>Expire le :</b> 28/02/2019 11h15, heure de la société</td>
    <td>Message in-app consulté</td>
    <td>L'utilisateur a maintenant ouvert l'application et recevra ce message, que ce soit grâce à la notification push précédente ou non.</td>
  </tr>
  <tr>
    <td>Rappel 50 % de réduction</td>
    <td>1 jour après que l'utilisateur a reçu l'étape précédente</td>
    <td>Tous depuis l'entrée <br><br><b>Filtre :</b> Dernier achat effectué il y a plus d'une semaine</td>
    <td>Message in-app</td>
    <td><b>Expire le :</b> 28/02/2019 11h15, heure de la société</td>
    <td>Aucun (dernier message du Canvas)</td>
    <td>L'utilisateur a reçu le message in-app à l'étape précédente mais n'a pas effectué d'achat malgré sa présence dans l'application. <br><br>Ce message vise à inciter davantage l'utilisateur à effectuer un achat en utilisant la promotion.</td>
  </tr>
</tbody>
</table>

Les messages in-app expirent en même temps que la promotion pour éviter toute incohérence entre les messages et l'expérience client.

  {% endtab %}
  {% tab Onboarding utilisateur %}

La première impression que vous faites à un utilisateur est peut-être la plus importante. Elle peut déterminer ses futures visites dans votre application. Vos premières communications avec vos utilisateurs doivent être judicieusement planifiées et encourager des visites fréquentes pour favoriser l'utilisation.

<table aria-label="Cas d'utilisation" class="tg">
  <caption>Cas d'utilisation</caption>
<thead>
  <tr>
    <th>Étape Canvas</th>
    <th>Délai</th>
    <th>Audience</th>
    <th>Canal</th>
    <th>Expiration</th>
    <th>Avancement</th>
    <th>Détails</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>E-mail de bienvenue</td>
    <td>Aucun</td>
    <td>Tous depuis l'entrée</td>
    <td>E-mail</td>
    <td>N/A</td>
    <td>Avancer l'audience après le délai</td>
    <td>E-mail initial qui souhaite la bienvenue à vos utilisateurs dans un projet, un abonnement ou un autre programme d'onboarding. <br><br>L'objectif est d'inciter les utilisateurs à ouvrir votre application pour commencer leur onboarding.</td>
  </tr>
  <tr>
    <td>Message in-app jours 3-6</td>
    <td>3 jours après que l'utilisateur a reçu l'étape précédente</td>
    <td>Tous depuis l'entrée</td>
    <td>Message in-app</td>
    <td><b>Expire :</b> 3 jours après que l'étape est disponible</td>
    <td>Message in-app actif</td>
    <td>Si l'utilisateur a réagi à l'e-mail et a été dirigé vers l'application, il recevra le message in-app souhaité pour poursuivre ou lui rappeler son onboarding et les éventuelles exigences associées.</td>
  </tr>
  <tr>
    <td>Push jour 5</td>
    <td>2 jours après que l'utilisateur a reçu l'étape précédente</td>
    <td>Tous depuis l'entrée</td>
    <td>Push</td>
    <td>N/A</td>
    <td>Message envoyé</td>
    <td>Après avoir reçu leur message in-app, les utilisateurs recevront une notification push de suivi pour poursuivre leur onboarding.</td>
  </tr>
</tbody>
</table>

Ces notifications push sont espacées autour d'un message in-app pour s'assurer que l'utilisateur a visité l'application et commencé son onboarding. Cela permet d'éviter tout spam ou envoi de messages désordonné qui pourrait décourager les utilisateurs de visiter votre application, et crée plutôt un enchaînement fluide et logique pour leurs premières expériences avec votre application.

  {% endtab %}
{% endtabs %}


## Prioriser les messages in-app {#prioritizing-in-app-messages}

Un utilisateur peut déclencher deux messages in-app dans votre Canvas en même temps. Dans ce cas, Braze respectera l'ordre de priorité suivant pour déterminer quel message in-app est affiché.

Sélectionnez **Set exact priority** et faites glisser les différentes étapes Canvas pour réorganiser leur priorité au sein du Canvas. Par défaut, les étapes situées plus tôt dans une variante du Canvas s'affichent avant les étapes ultérieures. Une fois vos étapes dans l'ordre de priorité souhaité, sélectionnez **Apply sort**.

![Le trieur de priorité avec deux étapes « Welcome IAM » et « Followup IAM ».]({% image_buster /assets/img_archive/canvas_priority2.png %}){: style="max-width:85%"}

### Modifier les brouillons de Canvas actifs {#making-changes-to-drafts-of-active-canvases}

Si vous modifiez la priorité des messages in-app dans les **Paramètres d'envoi** d'un brouillon d'un Canvas actif, ces modifications sont appliquées directement au Canvas actif lorsque le trieur de priorité est fermé. Cependant, dans une étape Message, le trieur de priorité sera mis à jour lorsque le brouillon sera lancé, car les paramètres des étapes Canvas s'appliquent au niveau de l'étape.

## Comportement d'avancement {#advancement-behavior}

Les étapes Message font automatiquement avancer tous les utilisateurs qui y entrent. Notez que l'étape n'attend pas que le message in-app soit déclenché ou affiché. Il n'est pas nécessaire de spécifier un comportement d'avancement du message, ce qui simplifie la configuration globale de l'étape.

Lorsqu'un utilisateur entre dans une étape de message in-app, il en sort immédiatement au lieu d'être retenu pendant la fenêtre d'expiration. Dans ce cas, l'ajout d'une étape de délai dans votre parcours utilisateur peut être utile.

Pour utiliser l'option **Avancer lorsque le message est envoyé**, ajoutez un [parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) distinct pour filtrer les utilisateurs qui n'ont pas reçu l'étape précédente.

{% details Éditeur Canvas d'origine %}

Vous ne pouvez plus créer ni dupliquer de Canvas avec l'éditeur d'origine. Cette section est disponible à titre de référence pour comprendre le fonctionnement du comportement d'avancement pour les étapes contenant des messages in-app.

Les Canvas créés dans l'éditeur d'origine doivent spécifier un comportement d'avancement, c'est-à-dire les critères d'avancement dans votre composant Canvas. [Les étapes contenant uniquement des messages in-app](#steps-iam-only) ont des options d'avancement différentes de celles des [étapes avec plusieurs types de messages](#steps-multiple-channels) (comme les notifications push ou les e-mails). Pour les messages in-app dans le workflow Canvas actuel, cette option est configurée pour toujours faire avancer l'audience immédiatement.

La livraison par événement n'est pas disponible pour les étapes Canvas contenant des messages in-app. Les étapes Canvas avec des messages in-app doivent être planifiées. Les messages in-app Canvas apparaîtront la première fois que votre utilisateur ouvrira l'application (déclenché par le démarrage de session) après que le message planifié dans le composant Canvas lui a été envoyé.

Si vous avez plusieurs messages in-app dans un même Canvas, un utilisateur doit démarrer plusieurs sessions pour recevoir chacun de ces messages individuels.

{% alert important %}
Lorsque l'option **Advance When In-App Message en direct** est sélectionnée, le message in-app restera disponible jusqu'à son expiration, même si l'utilisateur est passé aux étapes suivantes. Si vous ne souhaitez pas que le message in-app soit actif lorsque les étapes suivantes du Canvas sont distribuées, assurez-vous que l'expiration est plus courte que le délai des étapes suivantes.
{% endalert %}

### Étapes avec plusieurs canaux {#steps-multiple-channels}

Les étapes contenant un message in-app et un autre canal disposent des options d'avancement suivantes :

| Option | Description |
|---|---|
| Advance When Message Sent | Les utilisateurs doivent recevoir un e-mail, un webhook ou une notification push, ou consulter le message in-app pour avancer aux étapes suivantes du Canvas. <br> <br> Si le message in-app expire et que l'utilisateur n'a pas reçu l'e-mail, le webhook ou la notification push, ou n'a pas consulté le message in-app, il quittera le Canvas et n'avancera pas aux étapes suivantes. |
| Immediately Advance Audience | Tous les membres de l'audience de l'étape avancent aux étapes suivantes une fois le délai écoulé, qu'ils aient vu le message mentionné ou non. <br> <br> Les utilisateurs doivent correspondre aux critères de segment et de filtre de l'étape pour avancer aux étapes suivantes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étapes avec plusieurs canaux" }

{% alert important %}
Lorsque l'option **Entire Audience** est sélectionnée, le message in-app restera disponible jusqu'à son expiration, même si l'utilisateur est passé aux étapes suivantes. Si vous ne souhaitez pas que le message in-app soit actif lorsque les étapes suivantes du Canvas sont distribuées, vérifiez que l'expiration est plus courte que le délai des étapes suivantes.
{% endalert %}

{% enddetails %}

## Actions de déclenchement {#trigger-actions}

Vous pouvez choisir parmi les actions de déclenchement suivantes pour cibler vos utilisateurs :

- **Effectuer un achat :** ciblez les utilisateurs qui effectuent un achat quelconque ou un achat spécifique.
- **Démarrer une session :** ciblez les utilisateurs qui démarrent une session dans n'importe quelle application ou une application spécifique.
- **Effectuer un événement personnalisé :** ciblez les utilisateurs qui effectuent l'événement personnalisé sélectionné (l'événement personnalisé doit être envoyé via le SDK).

Un utilisateur doit entrer dans l'étape Canvas, démarrer une session, puis effectuer le déclencheur pour recevoir un message in-app. Cela signifie que les mises à jour en cours de session ne sont pas prises en charge. Par exemple, si le déclencheur est le démarrage d'une session, l'utilisateur n'a qu'à entrer dans l'étape Canvas et démarrer une session pour recevoir le message in-app. Si le déclencheur n'est pas le démarrage d'une session, l'utilisateur doit entrer dans l'étape Canvas, démarrer une session, puis effectuer le déclencheur pour recevoir le message in-app.

![« Effectuer un achat spécifique » sélectionné comme action de déclenchement.]({% image_buster /assets/img_archive/canvas_trigger_actions.png %}){: style="max-width:90%"}

Les fonctionnalités Canvas suivantes ne sont pas disponibles avec les messages in-app et ne seront donc pas appliquées à vos messages in-app même si elles sont activées.

- Timing intelligent
- Limitation du débit
- Limite de fréquence
- Critères de sortie
- Heures calmes

## Propriétés d'événement personnalisé dans un Canvas {#custom-event-properties-in-a-canvas}

Les propriétés d'événement personnalisé dans les messages in-app pour Canvas sont prises en charge. Cependant, ces propriétés proviennent de l'événement personnalisé ou de l'achat qui déclenche le message in-app, situé dans l'étape Message, et non du parcours d'action précédent.

## Points à prendre en compte {#considerations}

Voici quelques points à prendre en compte lors de l'envoi de messages in-app dans un Canvas.

- Si l'utilisateur ne redémarre jamais l'application ou ne démarre jamais de session, l'application ne pourra pas déterminer si l'utilisateur est éligible au message in-app, ce qui signifie qu'aucun message in-app ne sera envoyé.
- Lorsque le premier clic se produit et qu'il existe une variable de contexte Canvas (propriétés d'entrée Canvas), et qu'un utilisateur entre à nouveau dans un Canvas cinq fois, Braze prendra la cinquième entrée et utilisera cette variable de contexte dans le message in-app.
- Un utilisateur peut être éligible à un maximum de 10 messages in-app au sein de la même étape Canvas. Par exemple, si un Canvas autorise la réentrée et qu'un utilisateur entre dans le Canvas 11 fois, il ne recevra que 10 messages in-app si aucun n'a expiré.