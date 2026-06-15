{% multi_lang_include developer_guide/prerequisites/android.md %}

## Déclencheurs de messages {#message-triggers}

### Types de déclencheurs {#trigger-types}

Les messages in-app sont automatiquement déclenchés lorsque le SDK enregistre l'un des types d'événements personnalisés suivants : `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` et `Push Click`. Notez que les déclencheurs `Specific Purchase` et `Custom Event` contiennent également des filtres de propriétés robustes.

{% alert note %}
Les messages in-app ne peuvent pas être déclenchés par l'API ou par des événements de l'API — uniquement par des événements personnalisés enregistrés par le SDK. Pour en savoir plus sur la journalisation, consultez la section [Journalisation des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

### Sémantique de distribution {#delivery-semantics}

Tous les messages in-app éligibles sont envoyés sur l'appareil de l'utilisateur au début de sa session. À la réception, le SDK précharge les ressources afin qu'elles soient disponibles au moment du déclenchement, ce qui minimise la latence d'affichage. Si l'événement déclencheur comporte plusieurs messages in-app éligibles, seul le message ayant la priorité la plus élevée sera distribué.

Pour plus d'informations sur la sémantique de démarrage de session du SDK, consultez la section [Cycle de vie de la session]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android).

### Limite de débit {#rate-limit}

Par défaut, le SDK limite le débit des messages in-app déclenchés à une fois toutes les 30 secondes afin de garantir une expérience utilisateur de qualité.

Pour les applications en production, ne définissez pas cette valeur en dessous de 10 secondes, afin d'éviter que les utilisateurs ne soient submergés par des messages in-app successifs. Pour les tests et les flux d'applications de démonstration, 5 secondes est un réglage courant.

Vous pouvez définir cet intervalle à `0` pour les tests. Cependant, un intervalle de `0` seconde ne force pas l'affichage simultané de plusieurs messages in-app. Si un message est encore visible, le message suivant ne s'affichera pas tant que le message en cours n'aura pas été fermé.

Pour remplacer cette valeur, définissez `com_braze_trigger_action_minimum_time_interval_seconds` dans votre `braze.xml` via :

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## Paires clé-valeur {#key-value-pairs}

Lorsque vous créez une campagne dans Braze, vous pouvez définir des paires clé-valeur en tant qu'`extras`, que l'objet de message in-app peut utiliser pour envoyer des données à votre application. Par exemple :

{% tabs %}
{% tab JAVA %}
```java
Map<String, String> getExtras()
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endtab %}
{% endtabs %}

{% alert note %}
Pour plus d'informations, consultez le [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721).
{% endalert %}

## Désactivation des déclencheurs automatiques {#disabling-automatic-triggers}

Pour empêcher les messages in-app de se déclencher automatiquement :

1. Assurez-vous d'utiliser l'initialiseur d'intégration automatique, activé par défaut à partir de la version `2.2.0`.
2. Définissez l'opération par défaut des messages in-app sur `DISCARD` en ajoutant la ligne suivante à votre fichier `braze.xml`.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

## Déclenchement manuel des messages {#manually-triggering-messages}

Par défaut, les messages in-app sont automatiquement déclenchés lorsque le SDK enregistre un événement personnalisé. Cependant, vous pouvez déclencher manuellement un message en utilisant les méthodes suivantes.

### Utilisation d'un événement côté serveur {#using-a-server-side-event}

Pour déclencher un message in-app à l'aide d'un événement envoyé par le serveur, envoyez une notification push silencieuse à l'appareil, ce qui permet à un rappel push personnalisé d'enregistrer un événement basé sur le SDK. Cet événement déclenchera ensuite le message in-app destiné à l'utilisateur.

#### Étape 1 : Créer un rappel push pour recevoir la notification push silencieuse {#step-1-create-a-push-callback-to-receive-the-silent-push}

Enregistrez [votre rappel push personnalisé]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#push-callback) pour écouter une notification push silencieuse spécifique.

Dans l'exemple suivant, deux événements seront enregistrés pour que le message in-app soit distribué : l'un par le serveur et l'autre depuis votre rappel push personnalisé. Pour éviter que le même événement ne soit dupliqué, l'événement enregistré depuis votre rappel push doit suivre une convention de nommage générique, par exemple « événement déclencheur de message in-app », et ne pas porter le même nom que l'événement envoyé par le serveur. Si cette précaution n'est pas respectée, la segmentation et les données utilisateur peuvent être affectées par des événements enregistrés en double pour une seule action utilisateur.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endtab %}
{% endtabs %}

#### Étape 2 : Créer une campagne de notification push {#step-2-create-a-push-campaign}

Créez une [campagne de push silencieuse]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) déclenchée par l'événement envoyé par le serveur.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

La campagne de notification push doit inclure des paires clé-valeur supplémentaires indiquant que cette campagne push est envoyée pour enregistrer un événement personnalisé SDK. Cet événement sera utilisé pour déclencher le message in-app.

![Deux ensembles de paires clé-valeur : IS_SERVER_EVENT défini sur « true » et CAMPAIGN_NAME défini sur « nom de campagne à titre d'exemple ».]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

Le code exemple de rappel push ci-dessus reconnaît les paires clé-valeur et enregistre l'événement personnalisé SDK approprié.

Si vous souhaitez inclure des propriétés d'événement à joindre à votre événement « déclencheur de message in-app », vous pouvez les transmettre dans les paires clé-valeur du payload push. Dans cet exemple, le nom de la campagne du message in-app suivant a été inclus. Votre rappel push personnalisé peut ensuite transmettre la valeur comme paramètre de la propriété d'événement lors de l'enregistrement de l'événement personnalisé.

#### Étape 3 : Créer une campagne de message in-app {#step-3-create-an-in-app-message-campaign}

Créez votre campagne de message in-app visible par l'utilisateur dans le tableau de bord de Braze. Cette campagne doit avoir une livraison par événement et être déclenchée par l'événement personnalisé enregistré depuis votre rappel push personnalisé.

Dans l'exemple suivant, le message in-app spécifique à déclencher a été configuré en envoyant la propriété d'événement dans le cadre de la notification push silencieuse initiale.

![Une campagne de livraison par événement où un message in-app se déclenchera lorsque « campaign_name » est égal à « IAM campaign name example ».]({% image_buster /assets/img_archive/iam_event_trigger.png %})

Si un événement envoyé par le serveur est enregistré alors que l'application n'est pas au premier plan, l'événement sera enregistré, mais le message in-app ne s'affichera pas. Si vous souhaitez que l'événement soit retardé jusqu'à ce que l'application soit au premier plan, une vérification doit être incluse dans votre récepteur push personnalisé pour rejeter ou retarder l'événement jusqu'à ce que l'application passe au premier plan.

### Affichage d'un message prédéfini {#displaying-a-pre-defined-message}

Pour afficher manuellement un message in-app prédéfini, utilisez la méthode suivante :

{% tabs %}
{% tab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endtab %}
{% endtabs %}

### Affichage d'un message en temps réel {#displaying-a-message-in-real-time}

Vous pouvez également créer et afficher des messages in-app locaux en temps réel, en utilisant les mêmes options de personnalisation que celles disponibles sur le tableau de bord. Pour ce faire :

{% tabs %}
{% tab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endtab %}
{% endtabs %}

{% alert important %}
N'affichez pas de messages in-app lorsque le clavier virtuel est affiché à l'écran, car le rendu n'est pas défini dans ce cas.
{% endalert %}