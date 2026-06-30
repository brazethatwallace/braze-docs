---
nav_title: Déclenchement personnalisé
article_title: Personnaliser le déclenchement des messages in-app pour iOS
platform: iOS
page_order: 7
description: "Cet article de référence couvre le déclenchement personnalisé des messages in-app pour votre application iOS."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Déclenchement personnalisé de messages in-app {#custom-in-app-message-triggering}

Par défaut, les messages in-app sont déclenchés par des types d'événements enregistrés par le SDK. Si vous souhaitez déclencher des messages in-app par des événements envoyés par le serveur, vous pouvez également le faire.

Pour activer cette fonctionnalité, vous enverrez une notification push silencieuse à l'appareil, ce qui lui permet d'enregistrer un événement basé sur le SDK. Cet événement SDK déclenchera ensuite le message in-app visible par l'utilisateur.

## Étape 1 : Gérer les notifications push silencieuses et les paires clé-valeur {#step-1-handle-silent-push-and-key-value-pairs}

Ajoutez le code suivant dans la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [[Appboy sharedInstance] logCustomEvent:@"IAM Trigger" withProperties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
 };
```

{% endtab %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  NSLog("A push was received");
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    Appboy.sharedInstance()?.logCustomEvent("IAM Trigger", withProperties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% endtabs %}

Lorsque la notification push silencieuse est reçue, un événement enregistré par le SDK « in-app message trigger » sera consigné dans le profil utilisateur. Notez que ces messages in-app ne se déclencheront que si la notification push silencieuse est reçue pendant que l'application se trouve au premier plan.

## Étape 2 : Créer une campagne de notification push {#step-2-create-a-push-campaign}

Créez une campagne de notification push silencieuse déclenchée par l'événement envoyé par le serveur. Pour plus de détails sur la création d'une campagne de notification push silencieuse, reportez-vous aux [notifications push silencieuses]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications).

![Une campagne de messages in-app basée sur la livraison par événement, qui sera envoyée aux utilisateurs qui effectuent l'événement personnalisé « server_event ».]({% image_buster /assets/img_archive/iosServerSentPush.png %})

La campagne de notification push doit inclure des extras de paires clé-valeur, qui indiquent que cette campagne de notification push est envoyée pour enregistrer un événement personnalisé SDK. Cet événement sera utilisé pour déclencher le message in-app :

![Une campagne de messages in-app basée sur la livraison par événement, comportant deux paires clé-valeur. « CAMPAIGN_NAME » défini sur « Exemple de nom de message in-app » et « IS_SERVER_EVENT » défini sur « true ».]({% image_buster /assets/img_archive/iOSServerPush.png %})

Le code de la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` vérifie la clé `IS_SERVER_EVENT` et enregistrera un événement personnalisé SDK si celle-ci est présente.

Vous pouvez modifier le nom de l'événement ou les propriétés d'événement en envoyant la valeur souhaitée dans les extras de paires clé-valeur du payload de la notification push. Lors de l'enregistrement de l'événement personnalisé, ces extras peuvent être utilisés comme paramètre du nom de l'événement ou comme propriété d'événement.

## Étape 3 : Créer une campagne de messages in-app {#step-3-create-an-in-app-message-campaign}

Créez votre campagne de messages in-app visible par l'utilisateur depuis le tableau de bord de Braze. Cette campagne doit avoir une livraison par événement et être déclenchée par l'événement personnalisé enregistré depuis la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

Dans l'exemple suivant, le message in-app spécifique à déclencher a été configuré en envoyant la propriété d'événement dans le cadre de la notification push silencieuse initiale.

![Une campagne de messages in-app basée sur la livraison par événement, qui sera envoyée aux utilisateurs qui effectuent l'événement personnalisé « In-app message trigger » où « campaign_name » est égal à « Exemple de nom de message in-app ».]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

Étant donné qu'une notification push est utilisée pour enregistrer un événement personnalisé consigné par le SDK, Braze devra stocker un jeton de notification push pour chaque utilisateur afin de permettre cette solution. Pour iOS et Android, Braze ne stocke un jeton qu'à partir du moment où l'utilisateur a reçu l'invite de notification push du système d'exploitation. Avant cela, l'utilisateur ne sera pas joignable par notification push, et la solution précédente ne sera pas possible.