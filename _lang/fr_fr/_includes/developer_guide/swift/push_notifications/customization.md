{% multi_lang_include developer_guide/prerequisites/swift.md %} Il vous sera également nécessaire de [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Personnalisation des boutons d'action {#push-action-buttons-integration}

Le SDK Braze Swift offre une prise en charge de la gestion des URL pour les boutons d'action push. Il existe quatre ensembles de boutons d'action push par défaut pour les catégories de notification push par défaut de Braze : `Accept/Decline`, `Yes/No`, `Confirm/Cancel` et `More`.

![Un GIF d'un message push tiré vers le bas pour afficher deux boutons d'action personnalisables.]({% image_buster /assets/img_archive/iOS8Action.gif %}){: style="max-width:60%"}

### Enregistrement manuel des boutons d'action {#manually-registering-action-buttons}

{% alert important %}
L'enregistrement manuel des boutons d'action push n'est pas recommandé.
{% endalert %}

Si vous [configurez les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) à l'aide de l'option de configuration `configuration.push.automation`, Braze enregistre automatiquement les boutons d'action pour les catégories push par défaut et gère l'analyse des clics sur les boutons d'action push et le routage des URL.

Cependant, vous pouvez choisir d'enregistrer manuellement les boutons d'action push à la place.

#### Étape 1 : Ajout des catégories de notification push par défaut de Braze {#registering}

Utilisez le code suivant pour vous inscrire aux catégories push par défaut lorsque vous [vous inscrivez aux notifications push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-4-register-push-tokens-with-braze) :

{% tabs %}
{% tab swift %}
a
```swift
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:BRZNotifications.categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
Cliquer sur les boutons d'action push avec le mode d'activation en arrière-plan ne fera que rejeter la notification sans ouvrir l'application. Lorsque l'utilisateur ouvrira à nouveau l'application, l'analyse des clics de bouton pour ces actions sera transmise au serveur.
{% endalert %}

#### Étape 2 : Activer la gestion interactive des notifications push {#enable-push-handling}

Pour activer la gestion de nos boutons d'action push, y compris l'analyse des clics et le routage des URL, ajoutez le code suivant à la méthode de délégation `didReceive(_:completionHandler:)` de votre application :

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.notifications.handleUserNotification(response: response, withCompletionHandler: completionHandler)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                              withCompletionHandler:completionHandler];
```

{% endtab %}
{% endtabs %}

Si vous utilisez le framework `UNNotification` et que vous avez implémenté les [méthodes de notification]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-5-enable-push-handling) de Braze, vous devriez déjà avoir intégré cette méthode.

## Personnalisation des catégories de notification push {#customizing-push-categories}

En plus de fournir un ensemble de catégories de notification push par défaut, Braze prend en charge les catégories et actions de notification personnalisées. Après avoir enregistré des catégories dans votre application, vous pouvez utiliser le tableau de bord de Braze pour envoyer ces catégories de notification personnalisées à vos utilisateurs.

Voici un exemple qui tire parti du `LIKE_CATEGORY` affiché sur l'appareil :

![Un message de notification push affichant deux boutons d'action push « unlike » et « like ».]({% image_buster /assets/img_archive/push_example_category.png %})

### Étape 1 : Enregistrer une catégorie {#step-1-register-a-category}

Pour enregistrer une catégorie dans votre application, utilisez une approche similaire à la suivante :

{% tabs %}
{% tab swift %}

```swift
Braze.Notifications.categories.insert(
  .init(identifier: "LIKE_CATEGORY",
        actions: [
          .init(identifier: "LIKE_IDENTIFIER", title: "Like", options: [.foreground]),
          .init(identifier: "UNLIKE_IDENTIFIER", title: "Unlike", options: [.foreground])
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
NSMutableSet<UNNotificationCategory *> *categories = [BRZNotifications.categories mutableCopy];

UNNotificationAction *likeAction = [UNNotificationAction actionWithIdentifier:@"LIKE_IDENTIFIER"
                                                                        title:@"Like"
                                                                      options:UNNotificationActionOptionForeground];

UNNotificationAction *unlikeAction = [UNNotificationAction actionWithIdentifier:@"UNLIKE_IDENTIFIER"
                                                                          title:@"Unlike"
                                                                        options:UNNotificationActionOptionForeground];

UNNotificationCategory *likeCategory = [UNNotificationCategory categoryWithIdentifier:@"LIKE_CATEGORY"
                                                                              actions:@[likeAction, unlikeAction]
                                                                    intentIdentifiers:@[]
                                                                              options:UNNotificationCategoryOptionNone];

[categories addObject:likeCategory];
[UNUserNotificationCenter.currentNotificationCenter setNotificationCategories:categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
Lorsque vous créez une `UNNotificationAction`, vous pouvez spécifier une liste d'options d'action. Par exemple, `.foreground` permet à vos utilisateurs d'ouvrir votre application après avoir appuyé sur le bouton d'action. Ceci est nécessaire pour les comportements de navigation au clic, tels que « Ouvrir l'application » et « Deep link dans l'application ». Si vous souhaitez un bouton d'action qui ferme simplement la notification sans ouvrir l'application, n'incluez pas `.foreground` dans le tableau `options` de l'action. Pour plus d'informations, consultez [`UNNotificationActionOptions`](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions).
{% endalert %}

### Étape 2 : Sélectionner vos catégories {#step-2-select-your-categories}

Après avoir enregistré une catégorie, utilisez le tableau de bord de Braze pour envoyer des notifications de ce type aux utilisateurs.

{% alert tip %}
Il est nécessaire de définir des boutons d'action sur le tableau de bord de Braze uniquement pour les comportements qui ne peuvent pas être créés localement dans votre code Swift, tels que la création de deep links vers votre application ou les redirections vers une URL web. Ces actions doivent être configurées sur le tableau de bord afin de pouvoir définir l'URL ou le deep link à ouvrir. Pour les boutons d'action qui ferment simplement la notification sans ouvrir l'application, il n'est pas nécessaire de les configurer sur le tableau de bord : le comportement de fermeture est géré automatiquement par iOS. Enregistrez simplement votre catégorie personnalisée et ses actions dans le code de votre application, puis saisissez le nom de catégorie correspondant dans le tableau de bord.
{% endalert %}

1. Dans le tableau de bord de Braze, sélectionnez **Messaging** > **Push Notifications**, puis choisissez votre [Campaign push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message) iOS.
2. Sous **Compose push notification**, activez les **Action Buttons**.
3. Dans le menu déroulant **iOS Notification Category**, sélectionnez **Enter pre-registered custom iOS Category**.
4. Enfin, entrez l'une des catégories que vous avez créées plus tôt. L'exemple suivant utilise la catégorie personnalisée : `LIKE_CATEGORY`.

![Le tableau de bord de la Campaign de notification push avec la configuration des catégories personnalisées.]({% image_buster /assets/img_archive/ios-notification-category.png %})

### Exemple : catégorie de notification push personnalisée {#example-custom-push-category}

Supposons que vous souhaitiez créer une notification push avec deux boutons d'action : **Manage**, qui crée un deep link vers votre application, et **Keep**, qui ferme simplement la notification.

Dans l'exemple suivant, l'action `MANAGE_IDENTIFIER` inclut l'option `.foreground`, qui ouvre l'application lorsqu'on appuie dessus. Cela est nécessaire, car elle crée un deep link vers une partie spécifique de l'application. L'action `KEEP_IDENTIFIER` utilise un tableau d'options vide, ce qui signifie qu'elle fermera la notification sans ouvrir l'application.

{% tabs %}
{% tab swift %}

```swift
Braze.Notifications.categories.insert(
  .init(identifier: "YOUR_CATEGORY",
        actions: [
          .init(identifier: "KEEP_IDENTIFIER", title: "Keep", options: []),
          .init(identifier: "MANAGE_IDENTIFIER", title: "Manage", options: [.foreground])
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% endtabs %}

Étant donné que `MANAGE_IDENTIFIER` crée un deep link vers l'application, vous devez configurer ce bouton d'action sur le tableau de bord de Braze avec l'URL du deep link associé. Cependant, il n'est pas nécessaire de définir un bouton sur le tableau de bord pour `KEEP_IDENTIFIER`, car il ne fait que fermer la notification. Sur le tableau de bord, il vous suffit de saisir le nom de la catégorie (par exemple, `YOUR_CATEGORY`) correspondant à celui que vous avez enregistré dans le code de votre application.

## Personnaliser les badges {#customizing-badges}

Les badges sont de petites icônes idéales pour attirer l'attention d'un utilisateur. Vous pouvez spécifier un nombre de badges dans l'onglet [**Paramètres**]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_settings) lorsque vous composez une notification push à l'aide du tableau de bord de Braze. Vous pouvez également mettre à jour manuellement le nombre de badges via la propriété [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) de votre application ou le [payload de notification à distance](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1).

Braze efface automatiquement le nombre de badges lorsqu'une notification Braze est reçue alors que l'application est au premier plan. Définir manuellement le nombre de badges à 0 efface également les notifications dans le centre de notifications.

Si vous n'avez pas prévu de mécanisme pour effacer les badges dans le cadre du fonctionnement normal de l'application ou en envoyant des notifications push qui effacent le badge, vous devez effacer le badge lorsque l'application devient active en ajoutant le code suivant dans la méthode `sceneDidBecomeActive(_:)` du fichier `SceneDelegate.swift` (ou dans la méthode déléguée `applicationDidBecomeActive:` de votre application, si celle-ci n'a pas encore adopté le [cycle de vie `UIScene`](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle)) :

{% tabs %}
{% tab swift %}

```swift
// For iOS 16.0+
let center = UNUserNotificationCenter.current()
do {
  try await center.setBadgeCount(0)
} catch {
  // Handle errors
}

// Prior to iOS 16. Deprecated in iOS 17+.
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// For iOS 16.0+
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
[center setBadgeCount:0 withCompletionHandler:^(NSError * _Nullable error) {
    if (error != nil) {
        // Handle errors
    }
}];

// Prior to iOS 16. Deprecated in iOS 17+.
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% endtabs %}

## Personnaliser les sons {#customizing-sounds}

### Étape 1 : Héberger le son dans votre application {#step-1-host-the-sound-in-your-app}

Les sons personnalisés pour les notifications push doivent être hébergés localement dans le bundle principal de votre application. Les formats de données audio suivants sont acceptés :

- PCM linéaire
- MA4
- µLaw
- aLaw

Vous pouvez empaqueter les données audio dans un fichier AIFF, WAV ou CAF. Dans Xcode, ajoutez le fichier son à votre projet en tant que ressource non localisée du bundle de l'application.

{% alert note %}
Les sons personnalisés doivent durer moins de 30 secondes lors de la lecture. Si un son personnalisé dépasse cette limite, le son système par défaut est joué à la place.
{% endalert %}

#### Convertir des fichiers son {#converting-sound-files}

Vous pouvez utiliser l'outil afconvert pour convertir des sons. Par exemple, pour convertir le son système PCM linéaire 16 bits Submarine.aiff en audio IMA4 dans un fichier CAF, utilisez la commande suivante dans le terminal :

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

{% alert tip %}
Vous pouvez inspecter un son pour déterminer son format de données en l'ouvrant dans QuickTime Player et en choisissant **Afficher l'inspecteur du film** dans le menu **Film**.
{% endalert %}

### Étape 2 : Fournir une URL de protocole pour le son {#step-2-provide-a-protocol-url-for-the-sound}

Vous devez spécifier une URL de protocole qui pointe vers l'emplacement du fichier son dans votre application. Il existe deux méthodes pour ce faire :

* Utiliser le paramètre `sound` de l'[objet push Apple]({{site.baseurl}}/api/objects_filters/messaging/apple_object) pour transmettre l'URL à Braze.
* Spécifier l'URL dans le tableau de bord. Dans le [composeur de notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message#step-3-select-notification-type-ios-and-android), sélectionnez **Settings** et saisissez l'URL de protocole dans le champ **Sound**.

![Le composeur de notifications push dans le tableau de bord de Braze]({% image_buster /assets/img_archive/sound_push_ios.png %})

Si le fichier son spécifié n'existe pas ou si le mot-clé « default » est saisi, Braze utilisera le son d'alerte par défaut de l'appareil. En plus de notre tableau de bord, le son peut également être configuré via notre [API de messaging][12].

Consultez la documentation Apple Developer concernant la [préparation de sons d'alerte personnalisés](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html) pour plus d'informations.

## Réglages {#settings}

Lors de la création d'une campagne push via le tableau de bord, cliquez sur l'onglet **Réglages** à l'étape **Composer** pour afficher les réglages avancés disponibles.

![Onglet des réglages de composition d'une campagne push iOS dans Braze avec les options avancées.]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

### Paires clé-valeur {#key-value-pairs}

Braze vous permet d'envoyer des paires clé-valeur de chaînes de caractères personnalisées, appelées `extras`, avec une notification push vers votre application. Les extras peuvent être définis via le tableau de bord ou l'API et seront disponibles en tant que paires clé-valeur dans le dictionnaire `notification` transmis aux implémentations de votre délégué push.

### Options d'alerte {#alert-options}

Cochez la case **Alert Options** pour afficher un menu déroulant de clés-valeurs disponibles permettant d'ajuster la façon dont la notification apparaît sur les appareils.

### Ajout du drapeau content-available {#adding-content-available-flag}

Cochez la case **Add Content-Available Flag** pour demander aux appareils de télécharger du nouveau contenu en arrière-plan. Le plus souvent, cette option peut être cochée si vous souhaitez envoyer des [notifications silencieuses]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift).

### Ajout du drapeau mutable-content {#adding-mutable-content-flag}

Cochez la case **Add Mutable-Content Flag** pour activer la personnalisation avancée du récepteur. Ce drapeau sera automatiquement envoyé lors de la composition d'une [notification enrichie]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift), quelle que soit la valeur de cette case.

### ID de regroupement {#collapse-id}

Spécifiez un ID de regroupement pour fusionner les notifications similaires. Si vous envoyez plusieurs notifications avec le même ID de regroupement, l'appareil n'affichera que la notification la plus récemment reçue. Consultez la documentation d'Apple sur les [notifications regroupées](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

### Expiration {#expiry}

Cochez la case **Expiry** pour définir un délai d'expiration pour votre message. Si l'appareil d'un utilisateur perd la connectivité, Braze continuera d'essayer d'envoyer le message jusqu'à l'heure spécifiée. Si cette option n'est pas définie, la plateforme appliquera par défaut une expiration de 30 jours. Notez que les notifications push qui expirent avant la réception ne sont pas considérées comme échouées et ne seront pas enregistrées comme un rebond.