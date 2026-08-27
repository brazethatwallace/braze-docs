---
nav_title: Enregistrer des événements personnalisés
article_title: Enregistrer des événements personnalisés
page_order: 3.1
description: "Découvrez comment enregistrer des événements personnalisés via le SDK Braze."
---

# Enregistrer des événements personnalisés {#log-custom-events}

> Découvrez comment enregistrer des événements personnalisés via le SDK Braze.

{% alert note %}
Pour les SDK wrapper non répertoriés, utilisez plutôt la méthode native Android ou Swift correspondante.
{% endalert %}

Pour les événements eCommerce recommandés, consultez [Enregistrer des événements eCommerce]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

## Enregistrer un événement personnalisé {#logging-a-custom-event}

Pour enregistrer un événement personnalisé, utilisez la méthode d'enregistrement d'événement suivante.

{% tabs %}
{% tab web %}
Pour un déploiement standard du SDK Web, vous pouvez utiliser la méthode suivante :

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

Si vous préférez utiliser Google Tag Manager, vous pouvez utiliser le type d'étiquette **Custom Event** pour appeler la [méthode `logCustomEvent`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) et envoyer des événements personnalisés à Braze, avec en option des propriétés d'événement personnalisées. Pour ce faire :

1. Saisissez le **Event Name** en utilisant une variable ou en tapant un nom d'événement.
2. Utilisez le bouton **Add Row** pour ajouter des propriétés d'événement.

![Boîte de dialogue affichant les paramètres de configuration de l'étiquette d'action Braze. Les paramètres incluent « tag type » (custom event), « event name » (button click) et « event properties ».]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

{% tab android %}
Pour Android natif, vous pouvez utiliser la méthode suivante :

{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME);
```
{% endsubtab %}
{% subtab kotlin %}
```kotlin
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME)
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.logCustomEvent(name: "YOUR_EVENT_NAME")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze logCustomEvent:@"YOUR_EVENT_NAME"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab flutter %}
```dart
braze.logCustomEvent('YOUR_EVENT_NAME');
```
{% endtab %}

{% tab cordova %}
Utilisez la méthode du plugin Braze Cordova :

```javascript
BrazePlugin.logCustomEvent("YOUR_EVENT_NAME");
```

L'API `logCustomEvent` accepte :
- `eventName` (chaîne de caractères requise) : utilisez jusqu'à 255 caractères. Ne commencez pas le nom par `$`. Utilisez des caractères alphanumériques et de la ponctuation.
- `eventProperties` (objet optionnel) : ajoutez des paires clé-valeur pour les métadonnées de l'événement. Utilisez des clés de 255 caractères maximum et ne commencez pas les clés par `$`.

Pour les valeurs de propriété, utilisez `string` (jusqu'à 255 caractères), `numeric`, `boolean`, des tableaux ou des objets JSON imbriqués.

Pour les détails de déploiement, consultez le code source du SDK Braze Cordova :
- [Méthode `logCustomEvent` dans `www/BrazePlugin.js` (lignes 138-140)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L138-L140)
- [JSDoc dans `www/BrazePlugin.js` (lignes 128-140)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L128-L140)
- [Gestionnaire Android dans `src/android/BrazePlugin.kt` (lignes 108-115)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/android/BrazePlugin.kt#L108-L115)
- [Gestionnaire iOS dans `src/ios/BrazePlugin.m` (lignes 308-313)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.m#L308-L313)
- [Déclaration de méthode iOS dans `src/ios/BrazePlugin.h` (ligne 24)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.h#L24)
{% endtab %}

{% tab infillion %}
Si vous avez intégré les [Infillion Beacons](https://infillion.com/software/beacons/) dans votre application Android, vous pouvez éventuellement utiliser `visit.getPlace()` pour enregistrer des événements spécifiques à un emplacement. `requestImmediateDataFlush` vérifie que votre événement sera enregistré même si votre application est en arrière-plan.

{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}
```javascript
Braze.logCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```
{% endtab %}

{% tab unity %}
```csharp
AppboyBinding.LogCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}
{% endtabs %}

## Ajout de propriétés de métadonnées {#adding-metadata-properties}

Lorsque vous enregistrez un événement personnalisé, vous avez la possibilité d'ajouter des métadonnées à cet événement en transmettant un objet de propriétés avec l'événement. Les propriétés sont définies sous forme de paires clé-valeur. Les clés sont des chaînes de caractères et les valeurs peuvent être de type `string`, `numeric`, `boolean`, objets [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp), tableaux ou objets JSON imbriqués.

Pour ajouter des propriétés de métadonnées, utilisez la méthode d'enregistrement d'événement suivante.

{% tabs %}
{% tab web %}
```javascript
braze.logCustomEvent("YOUR-EVENT-NAME", {
  you: "can",
  pass: false,
  orNumbers: 42,
  orDates: new Date(),
  or: ["any", "array", "here"],
  andEven: {
     deeply: ["nested", "json"]
  }
});
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}
```java
Braze.logCustomEvent("YOUR-EVENT-NAME",
    new BrazeProperties(new JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", new Date())
        .put("or", new JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", new JSONObject()
            .put("deeply", new JSONArray()
                .put("nested")
                .put("json"))
        )
));
```
{% endsubtab %}
{% subtab kotlin %}
```kotlin
Braze.logCustomEvent("YOUR-EVENT-NAME",
    BrazeProperties(JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", Date())
        .put("or", JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", JSONObject()
            .put("deeply", JSONArray()
                .put("nested")
                .put("json"))
        )
))
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.logCustomEvent(
  name: "YOUR-EVENT-NAME",
  properties: [
    "you": "can",
    "pass": false,
    "orNumbers": 42,
    "orDates": Date(),
    "or": ["any", "array", "here"],
    "andEven": [
      "deeply": ["nested", "json"]
    ]
  ]
)
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze logCustomEvent:@"YOUR-EVENT-NAME"
                       properties:@{
  @"you": @"can",
  @"pass": @(NO),
  @"orNumbers": @42,
  @"orDates": [NSDate date],
  @"or": @[@"any", @"array", @"here"],
  @"andEven": @{
    @"deeply": @[@"nested", @"json"]
  }
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab flutter %}
```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```
{% endtab %}

{% tab cordova %}
Enregistrez des custom events avec un objet de propriétés :

```javascript
var properties = {};
properties["key1"] = "value1";
properties["key2"] = ["value2", "value3"];
properties["key3"] = false;
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", properties);
```

Vous pouvez également transmettre les propriétés en ligne :

```javascript
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", {
  "key": "value",
  "amount": 42,
});
```

L'application exemple officielle Cordova inclut des propriétés de type chaîne de caractères, numérique, booléen, tableau et objet imbriqué :
- [`sample-project/www/js/index.js` (lignes 230-251)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/sample-project/www/js/index.js#L230-L251)

Extrait du projet exemple :

```javascript
var properties = {};
properties["One"] = "That's the Way of the World";
properties["Two"] = "After the Love Has Gone";
properties["Three"] = "Can't Hide Love";
BrazePlugin.logCustomEvent("cordovaCustomEventWithProperties", properties);
BrazePlugin.logCustomEvent("cordovaCustomEventWithoutProperties");
BrazePlugin.logCustomEvent("cordovaCustomEventWithFloatProperties", {
  "Cart Value": 4.95,
  "Cart Item Name": "Spicy Chicken Bites 5 pack"
});
BrazePlugin.logCustomEvent("cordovaCustomEventWithNestedProperties", {
  "array key": [1, "2", false],
  "object key": {
    "k1": "1",
    "k2": 2,
    "k3": false,
  },
  "deep key": {
    "key": [1, "2", true]
  }
});
```

Pour plus de détails sur l'API et le pont natif, consultez :
- [`www/BrazePlugin.js` JSDoc (lignes 128-140)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L128-L140)
- [Gestionnaire Android dans `src/android/BrazePlugin.kt` (lignes 108-115)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/android/BrazePlugin.kt#L108-L115)
- [Gestionnaire iOS dans `src/ios/BrazePlugin.m` (lignes 308-313)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.m#L308-L313)
{% endtab %}

{% tab react native %}
```javascript
Braze.logCustomEvent("custom_event_with_properties", {
    key1: "value1",
    key2: ["value2", "value3"],
    key3: false,
});
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME", {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```
{% endtab %}

{% tab unity %}
```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```
{% endtab %}
{% endtabs %}

{% alert important %}
Les clés `time` et `event_name` sont réservées et ne peuvent pas être utilisées comme propriétés d'événement personnalisé.
{% endalert %}

## Bonnes pratiques {#best-practices}

Il y a trois vérifications importantes à effectuer pour vous assurer que vos propriétés d'événement personnalisé sont enregistrées comme prévu :

* [Établir quels événements sont enregistrés](#verify-events)
* [Vérifier le journal](#verify-log)
* [Vérifier les valeurs](#verify-values)

Plusieurs propriétés peuvent être enregistrées à chaque fois qu'un événement personnalisé est consigné.

### Vérifier les événements {#verify-events}

Vérifiez auprès de vos développeurs quelles propriétés d'événement sont suivies. Gardez à l'esprit que toutes les propriétés d'événement sont sensibles à la casse. Pour plus d'informations sur le suivi des événements personnalisés, consultez ces articles en fonction de votre plateforme :

* [Android]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
* [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
* [Web]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)

### Vérifier le journal {#verify-log}

Pour confirmer que les propriétés d'événement sont correctement suivies, vous pouvez consulter toutes les propriétés d'événement depuis la page **Custom Events**.

1. Accédez à **Data Settings** > **Custom Events**.
2. Localisez votre événement personnalisé dans la liste.
3. Pour votre événement, sélectionnez **Manage Properties** pour afficher les noms des propriétés associées à un événement.

### Vérifier les valeurs {#verify-values}

Après avoir [ajouté votre utilisateur en tant qu'utilisateur test]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups), suivez ces étapes pour vérifier vos valeurs :

1. Effectuez l'événement personnalisé dans l'application.
2. Attendez environ 10 secondes pour que les données soient transmises.
3. Actualisez le [journal des événements utilisateurs]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) pour voir l'événement personnalisé et la valeur de la propriété d'événement qui a été transmise avec.

## Résolution des problèmes liés aux événements personnalisés {#troubleshooting-custom-events}

Utilisez ces scénarios pour résoudre les problèmes de journalisation des événements personnalisés dans les différents SDK.

### Vérifier le déclencheur de l'événement personnalisé {#verifying-the-custom-event-trigger}

Si un événement personnalisé n'apparaît pas, il se peut que l'action suivie dans votre application ne corresponde pas à l'action que vous testez.

- Confirmez avec votre équipe de développement quelle action de l'application déclenche l'événement personnalisé.
- Vérifiez s'il existe des chemins de code obsolètes après les mises à jour du SDK, tels que des références à `appboy` au lieu de `braze`.

### Les événements personnalisés sont enregistrés sur un profil anonyme {#custom-events-are-logged-to-an-anonymous-profile}

Si vous n'identifiez pas un utilisateur avant de journaliser un événement personnalisé, Braze peut associer cet événement à un profil anonyme.

- Appelez `changeUser()` avant d'effectuer l'événement personnalisé afin que Braze l'enregistre sur un profil utilisateur identifié.
- Testez avec un utilisateur test identifié, puis consultez le [journal des événements utilisateurs]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log).

### Vérifier la configuration de la journalisation des événements personnalisés {#verifying-custom-event-logging-setup}

Si les événements personnalisés n'apparaissent pas comme prévu, confirmez que votre équipe de développement a implémenté la journalisation des événements personnalisés pour la bonne action de l'application.

- Demandez à votre équipe de développement de vérifier que l'événement est correctement journalisé et déclenché par l'action utilisateur attendue.
- Lorsque votre équipe ouvre un ticket auprès du support Braze, incluez les [logs détaillés]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) et les extraits de code pertinents.
- Si votre application utilise Swift ou Android, votre équipe de développement peut utiliser les [prérequis du débogueur SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging#prerequisites) pour générer des logs détaillés.
- Si votre équipe de développement ne parvient pas à identifier le problème, ouvrez un [ticket auprès du support Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).