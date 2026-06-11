---
page_order: 1.5
nav_title: Lecture des journaux détaillés
article_title: Lecture des journaux détaillés
description: "Apprenez à lire et à interpréter les journaux détaillés générés par le SDK Braze, y compris les entrées clés pour les notifications push, les messages in-app, les Content Cards et les liens profonds."
---

# Lecture des journaux détaillés {#reading-verbose-logs}

> Cette page explique comment interpréter les journaux détaillés générés par le SDK Braze. Pour chaque canal de communication, vous trouverez les entrées de journal importantes à rechercher, leur signification et les problèmes courants à surveiller.

Avant de commencer, assurez-vous d'avoir [activé la journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/) et de savoir comment collecter les journaux sur votre plateforme.

## Sessions {#sessions}

Les sessions constituent la base de l'analytique et de la distribution des messages de Braze. De nombreuses fonctionnalités d'envoi de messages, notamment les messages in-app et les Content Cards, nécessitent qu'une session valide soit démarrée avant de pouvoir fonctionner. Si les sessions ne sont pas enregistrées correctement, examinez ce point en priorité. Pour plus d'informations sur l'activation du suivi des sessions, consultez [Étape 5 : Activer le suivi des sessions utilisateur]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_step-5-enable-user-session-tracking).

### Entrées de journal clés {#key-log-entries}

{% tabs %}
{% tab Swift %}

**Début de session :**

```
Started user session (id: <SESSION_ID>)
```

**Fin de session :**

```
Ended user session (id: <SESSION_ID>, duration: <DURATION>s)
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: sessionEnd(duration: <DURATION>)
```

{% endtab %}
{% tab Android %}

**Début de session :**

Recherchez les entrées suivantes :

```
New session created with ID: <SESSION_ID>
Session start event for new session received
Completed the openSession call
Opened session with activity: <ACTIVITY_NAME>
```

Filtrez les requêtes réseau vers votre endpoint Braze configuré (par exemple, sdk.iad-01.braze.com) pour voir l'événement de début de session (`ss`).

**Fin de session :**

```
Closed session with activity: <ACTIVITY_NAME>
Closed session with session ID: <SESSION_ID>
Requesting data flush on internal session close flush timer.
```

{% endtab %}
{% endtabs %}

### Éléments à vérifier {#what-to-check}

- Vérifiez qu'un journal de début de session apparaît lorsque l'application est lancée.
- Si vous ne voyez pas de début de session, vérifiez que le SDK est correctement initialisé et que `openSession` (Android) est bien appelé.
- Sur Android, confirmez qu'une requête réseau est envoyée à l'endpoint Braze. Si vous ne la voyez pas, vérifiez votre clé API et la configuration de l'endpoint.

## Notifications push {#push-notifications}

Les journaux des notifications push vous permettent de vérifier que les jetons d'appareil sont enregistrés, que les notifications sont distribuées et que les événements de clic sont suivis.

### Enregistrement du jeton {#token-registration}

Lorsqu'une session démarre, le SDK enregistre le jeton push de l'appareil auprès de Braze.

{% tabs %}
{% tab Swift %}

```
Updated push notification authorization:
- authorization: authorized

Received remote notifications device token: <PUSH_TOKEN>
```

Filtrez les requêtes vers votre endpoint Braze configuré (par exemple, sdk.iad-01.braze.com) et recherchez `push_token` dans les attributs du corps de la requête :

```
"attributes": [
  {
    "push_token": "<PUSH_TOKEN>",
    "user_id": "<USER_ID>"
  }
]
```

Confirmez également que les informations de l'appareil incluent :

```
"device": {
  "ios_push_auth": "authorized",
  "remote_notification_enabled": 1
}
```

{% endtab %}
{% tab Android %}

Recherchez le journal d'enregistrement FCM :

```
Registering for Firebase Cloud Messaging token using sender id: <SENDER_ID>
```

Vérifiez les éléments suivants :

- `com_braze_firebase_cloud_messaging_registration_enabled` est `true`.
- L'ID d'expéditeur FCM correspond à votre projet Firebase.

Une erreur courante est `SENDER_ID_MISMATCH`, ce qui signifie que l'ID d'expéditeur configuré ne correspond pas à votre projet Firebase.

{% endtab %}
{% endtabs %}

### Éléments à vérifier

- Si `push_token` est absent du corps de la requête, le jeton n'a pas été capturé. Vérifiez la configuration push dans les paramètres de votre application.
- Si `ios_push_auth` affiche `denied` ou `provisional`, l'utilisateur n'a pas accordé l'autorisation push complète.
- Sur Android, si vous voyez `SENDER_ID_MISMATCH`, mettez à jour votre ID d'expéditeur FCM pour qu'il corresponde à votre projet Firebase.

### Distribution et clic push {#push-delivery-and-click}

Lorsqu'une notification push est sélectionnée, le SDK enregistre les événements de traitement et de clic.

{% tabs %}
{% tab Swift %}

```
Processing push notification:
- date: <TIMESTAMP>
- silent: false
- userInfo: {
  "ab": { ... },
  "ab_uri": "<DEEP_LINK_OR_URL>",
  "aps": {
    "alert": {
      "body": "<MESSAGE_BODY>",
      "title": "<MESSAGE_TITLE>"
    }
  }
}
```

Suivi de l'événement de clic :

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: pushClick(campaignId: ...)
```

Si la notification contient un lien profond, vous verrez également :

```
Opening '<URL>':
- channel: notification
- useWebView: false
- isUniversalLink: false
```

{% endtab %}
{% tab Android %}

```
BrazeFirebaseMessagingService: Got Remote Message from FCM
```

Suivi du payload push et des journaux d'affichage. Pour les liens profonds, recherchez les entrées **Deep Link Delegate** ou **UriAction**.

{% endtab %}
{% endtabs %}

### Éléments à vérifier

- Vérifiez que le payload de la notification push contient les éléments attendus : `title`, `body` et les liens profonds éventuels (`ab_uri`).
- Confirmez qu'un événement `pushClick` est enregistré après l'appui.
- Si l'événement de clic est manquant, vérifiez que votre délégué d'application ou votre gestionnaire de notifications transmet correctement les événements push au SDK Braze.

## Messages in-app {#in-app-messages}

Les journaux des messages in-app vous montrent l'ensemble du cycle de vie : distribution depuis le serveur, déclenchement en fonction des événements, affichage, enregistrement des impressions et suivi des clics.

### Distribution des messages {#message-delivery}

Lorsqu'un utilisateur démarre une session et est éligible à un message in-app, le SDK reçoit le payload du message depuis le serveur.

{% tabs %}
{% tab Swift %}

Filtrez les réponses provenant de votre endpoint Braze configuré (par exemple, sdk.iad-01.braze.com) contenant les données du message in-app.

Le corps de la réponse contient le payload du message, notamment :

```
"templated_message": {
  "data": {
    "message": "...",
    "type": "HTML",
    "message_close": "SWIPE",
    "trigger_id": "<TRIGGER_ID>"
  },
  "type": "inapp"
}
```

{% endtab %}
{% tab Android %}

Recherchez le journal de correspondance de l'événement déclencheur :

```
Triggering action: <CAMPAIGN_BSON_ID>
```

Cela confirme que le message in-app a été associé à un événement déclencheur.

{% endtab %}
{% endtabs %}

### Affichage et impression du message {#message-display-and-impression}

{% tabs %}
{% tab Swift %}

```
In-app message ready for display:
- triggerId: (campaignId: <CAMPAIGN_ID>, ...)
- extras: { ... }
```

Suivi du journal d'impression :

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageImpression(triggerIds: [...])
```

{% endtab %}
{% tab Android %}

```
handleExistingInAppMessagesInStackWithDelegate:: Displaying in-app message
```

{% endtab %}
{% endtabs %}

### Événements de clic et de bouton {#click-and-button-events}

Lorsqu'un utilisateur appuie sur un bouton ou ferme le message :

{% tabs %}
{% tab Swift %}

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageButtonClick(triggerIds: [...], buttonId: "<BUTTON_ID>")
```

Si aucun autre message déclenché ne correspond, vous verrez également :

```
No matching trigger for event.
```

Ce comportement est normal lorsqu'aucun message in-app supplémentaire n'est configuré pour l'événement.

{% endtab %}
{% tab Android %}

Filtrez les requêtes vers votre endpoint Braze configuré (par exemple, sdk.iad-01.braze.com) et recherchez les événements portant le nom `sbc` (clic sur bouton) ou `si` (impression) dans le corps de la requête.

{% endtab %}
{% endtabs %}

### Éléments à vérifier

- Si le message in-app ne s'affiche pas, vérifiez qu'un début de session a bien été enregistré au préalable.
- Filtrez les réponses provenant de votre endpoint Braze configuré pour confirmer que le payload du message a bien été distribué.
- Si les impressions ne sont pas enregistrées, vérifiez que vous n'avez pas implémenté un délégué `inAppMessageDisplay` personnalisé qui supprime l'enregistrement.
- Si « No matching trigger for event » apparaît, c'est normal et cela indique qu'aucun message in-app supplémentaire n'est configuré pour cet événement.

## Content Cards

Les journaux des Content Cards vous permettent de vérifier que les cartes sont synchronisées avec l'appareil, affichées à l'utilisateur et que les interactions (impressions, clics, rejets) sont suivies.

### Synchronisation des cartes {#card-sync}

Les Content Cards se synchronisent au début de la session et lorsqu'une actualisation manuelle est demandée. Si aucune session n'est enregistrée, aucune Content Card n'est affichée.

{% tabs %}
{% tab Swift %}

Filtrez les réponses provenant de votre endpoint Braze configuré (par exemple, sdk.iad-01.braze.com) contenant les données des cartes.

Le corps de la réponse contient les données des cartes, notamment :

```
"cards": [
  {
    "id": "<CARD_ID>",
    "tt": "<CARD_TITLE>",
    "ds": "<CARD_DESCRIPTION>",
    "tp": "short_news",
    "v": 0,
    "cl": 0,
    "p": 1
  }
]
```

Champs clés :
- `v` (vu) : `0` = non vu, `1` = vu
- `cl` (cliqué) : `0` = non cliqué, `1` = cliqué
- `p` (épinglé) : `0` = non épinglé, `1` = épinglé
- `tp` (type) : `short_news`, `captioned_image`, `classic`, etc.

{% endtab %}
{% tab Android %}

```
Requesting content cards sync.
```

Suivi d'une requête POST vers votre endpoint Braze configuré (par exemple, sdk.iad-01.braze.com) contenant les informations de l'utilisateur et de l'appareil.

{% endtab %}
{% endtabs %}

### Impressions, clics et rejets {#impressions-clicks-and-dismissals}

{% tabs %}
{% tab Swift %}

**Impression :**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardImpression(cardIds: [...])
```

**Clic :**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardClick(cardIds: [...])
```

Si la carte comporte une URL, vous verrez également :

```
Opening '<URL>':
- channel: contentCard
- useWebView: true
```

**Rejet :**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardDismissed(cardIds: [...])
```

{% endtab %}
{% tab Android %}

Filtrez les requêtes vers votre endpoint Braze configuré (par exemple, sdk.iad-01.braze.com) et recherchez les noms d'événements dans le corps de la requête :
- `cci` — Impression de Content Card
- `ccc` — Clic sur Content Card
- `ccd` — Content Card rejetée

{% endtab %}
{% endtabs %}

### Éléments à vérifier

- **Aucune carte affichée** : vérifiez qu'un début de session est bien enregistré. Les Content Cards nécessitent une session active pour se synchroniser.
- **Cartes manquantes pour les nouveaux utilisateurs** : les nouveaux utilisateurs lors de leur première session peuvent ne pas voir les Content Cards avant la session suivante. Il s'agit d'un comportement normal.
- **La carte dépasse la limite de taille** : les Content Cards de plus de 2 Ko ne sont pas affichées et le message est abandonné.
- **La carte persiste après l'arrêt de la campagne** : vérifiez que la synchronisation s'est terminée après l'arrêt de la campagne. Les Content Cards sont supprimées de l'appareil après une synchronisation réussie. Lorsque vous arrêtez une campagne, assurez-vous que l'option permettant de supprimer les cartes actives des flux des utilisateurs est sélectionnée.

## Liens profonds {#deep-links}

Les journaux de liens profonds apparaissent dans les notifications push, les messages in-app et les Content Cards. La structure du journal est cohérente quel que soit le canal source.

{% tabs %}
{% tab Swift %}

Lorsque le SDK traite un lien profond :

```
Opening '<DEEP_LINK_URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: false
- isUniversalLink: false
- extras: { ... }
```

Où `<SOURCE_CHANNEL>` est l'un des suivants : `notification`, `inAppMessage` ou `contentCard`.

{% endtab %}
{% tab Android %}

Pour les liens profonds, recherchez les entrées **Deep Link Delegate** ou **UriAction** dans Logcat. Pour tester la résolution des liens profonds de manière indépendante, exécutez la commande suivante :

```bash
adb shell am start -W -a android.intent.action.VIEW -d "<YOUR_DEEP_LINK>" "<YOUR_PACKAGE_NAME>"
```

Cela permet de vérifier si le lien profond fonctionne correctement en dehors du SDK Braze.

{% endtab %}
{% endtabs %}

### Éléments à vérifier

- Vérifiez que l'URL du lien profond correspond à celle que vous avez configurée dans la campagne.
- Si le lien profond fonctionne depuis un canal (par exemple, push) mais pas depuis un autre (par exemple, Content Cards), vérifiez que votre implémentation de gestion des liens profonds prend en charge tous les canaux.
- Sur iOS, les liens universels nécessitent un traitement supplémentaire. Si les liens universels ne fonctionnent pas depuis les canaux Braze, vérifiez que votre application implémente le protocole `BrazeDelegate` pour la gestion des URL.
- Sur Android, vérifiez que la gestion automatique des liens profonds est désactivée si vous utilisez un gestionnaire personnalisé. Sinon, le gestionnaire par défaut pourrait entrer en conflit avec votre implémentation.

## Identification de l'utilisateur {#user-identification}

Lorsqu'un utilisateur est identifié avec un `external_id`, le SDK enregistre un événement de changement d'utilisateur.

{% tabs %}
{% tab Android %}

```
changeUser called with: <EXTERNAL_ID>
```

Points importants à connaître :
- Appelez `changeUser` dès que l'utilisateur se connecte — le plus tôt sera le mieux.
- Si un utilisateur se déconnecte, il n'est pas possible d'appeler `changeUser` pour le ramener à un utilisateur anonyme.
- Si vous ne souhaitez pas d'utilisateurs anonymes, appelez `changeUser` au début de la session ou au démarrage de l'application.

{% endtab %}
{% tab Swift %}

Filtrez les requêtes vers votre endpoint Braze configuré (par exemple, sdk.iad-01.braze.com) et recherchez l'identification de l'utilisateur dans le corps de la requête :

```
"user_id": "<EXTERNAL_ID>"
```

{% endtab %}
{% endtabs %}

## Requêtes réseau {#network-requests}

Les journaux détaillés incluent l'ensemble des détails des requêtes et réponses HTTP pour la communication du SDK avec les serveurs Braze. Ces informations sont utiles pour diagnostiquer les problèmes de connectivité.

### Structure de la requête {#request-structure}

Filtrez les requêtes vers votre endpoint Braze configuré (par exemple, sdk.iad-01.braze.com). La structure de la requête comprend :

{% tabs %}
{% tab Swift %}

```
[http] request POST: <YOUR_BRAZE_ENDPOINT>
- Headers:
  - Content-Type: application/json
  - X-Braze-Api-Key: <REDACTED>
  - X-Braze-Req-Attempt: 1
  - X-Braze-Req-Tokens-Remaining: <COUNT>
- Body: { ... }
```

{% endtab %}
{% tab Android %}

```
Making request(id = <REQUEST_ID>) to <YOUR_BRAZE_ENDPOINT>
```

{% endtab %}
{% endtabs %}

### Éléments à vérifier

- **Clé API** : vérifiez que `X-Braze-Api-Key` correspond à la clé API de votre espace de travail.
- **Endpoint** : confirmez que l'URL de la requête correspond à l'endpoint SDK que vous avez configuré.
- **Tentatives de réessai** : une valeur de `X-Braze-Req-Attempt` supérieure à 1 indique que le SDK réessaie une requête échouée, ce qui peut signaler des problèmes de connectivité.
- **Limite de débit** : `X-Braze-Req-Tokens-Remaining` affiche les jetons de requête restants. Un nombre faible peut indiquer que le SDK approche des limites de débit.
- **Requêtes manquantes** : sur Android, si vous ne voyez aucune requête vers l'endpoint Braze après le début de la session, vérifiez votre clé API et la configuration de l'endpoint.

## Abréviations courantes des événements {#common-event-abbreviations}

Dans les payloads des journaux détaillés, Braze utilise des noms d'événements abrégés. Voici une référence :

| Abréviation | Événement |
|---|---|
| `ss` | Début de session |
| `se` | Fin de session |
| `si` | Impression de message in-app |
| `sbc` | Clic sur bouton de message in-app |
| `cci` | Impression de Content Card |
| `ccc` | Clic sur Content Card |
| `ccd` | Content Card rejetée |
| `lr` | Localisation enregistrée |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }