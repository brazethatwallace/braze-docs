{% multi_lang_include developer_guide/prerequisites/android.md %} Il vous sera également nécessaire de [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Utilisation d'un rappel pour les événements push {#push-callback}

Braze propose une fonction de rappel [`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html) pour la réception, l'ouverture ou le rejet des notifications push. Nous vous recommandons de placer cette fonction de rappel dans votre `Application.onCreate()` pour ne manquer aucun événement survenant lorsque votre application n'est pas en fonctionnement.

{% alert note %}
Si vous utilisiez un récepteur de diffusion personnalisé pour cette fonctionnalité dans votre application, vous pouvez le supprimer en toute sécurité pour adopter cette option d'intégration.
{% endalert %}

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final BrazeNotificationPayload parsedData = event.getNotificationPayload();

  //
  // The type of notification itself
  //
  final boolean isPushOpenEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_OPENED;
  final boolean isPushReceivedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_RECEIVED;
  // Sent when a user has dismissed a notification
  final boolean isPushDeletedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_DELETED;

  //
  // Notification data
  //
  final String pushTitle = parsedData.getTitleText();
  final Long pushArrivalTimeMs = parsedData.getNotificationReceivedTimestampMillis();
  final String deeplink = parsedData.getDeeplink();

  //
  // Custom KVP data
  //
  final String myCustomKvp1 = parsedData.getBrazeExtras().getString("my first kvp");
  final String myCustomKvp2 = parsedData.getBrazeExtras().getString("my second kvp");
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).subscribeToPushNotificationEvents { event ->
    val parsedData = event.notificationPayload

    //
    // The type of notification itself
    //
    val isPushOpenEvent = event.eventType == BrazePushEventType.NOTIFICATION_OPENED
    val isPushReceivedEvent = event.eventType == BrazePushEventType.NOTIFICATION_RECEIVED
    // Sent when a user has dismissed a notification
    val isPushDeletedEvent = event.eventType == BrazePushEventType.NOTIFICATION_DELETED

    //
    // Notification data
    //
    val pushTitle = parsedData.titleText
    val pushArrivalTimeMs = parsedData.notificationReceivedTimestampMillis
    val deeplink = parsedData.deeplink

    //
    // Custom KVP data
    //
    val myCustomKvp1 = parsedData.brazeExtras.getString("my first kvp")
    val myCustomKvp2 = parsedData.brazeExtras.getString("my second kvp")
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Avec les boutons d'action de notification, les intentions `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` se déclenchent lorsque les boutons avec les actions `opens app` ou `deep link` sont cliqués. La gestion des deep links et des compléments reste la même. Les boutons avec des actions `close` ne déclenchent pas les intentions `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` et rejettent automatiquement la notification.
{% endalert %}

{% alert important %}
Créez votre listener de notification push dans `Application.onCreate` pour vous assurer que votre listener est déclenché après qu'un utilisateur final a appuyé sur une notification alors que votre application est dans un état terminé.
{% endalert %}

## Personnalisation de l'affichage des notifications {#customization-display}

### Étape 1 : Créer votre fabrique de notification personnalisée {#step-1-create-your-custom-notification-factory}

Dans certains scénarios, vous pourriez souhaiter personnaliser les notifications push d'une manière qui serait complexe ou non disponible côté serveur. Pour vous donner un contrôle complet de l'affichage des notifications, nous avons ajouté la possibilité de définir votre propre [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) pour créer des objets de notification qui seront affichés par Braze.

Si une `IBrazeNotificationFactory` personnalisée est définie, Braze appellera la méthode `createNotification()` de votre fabrique lors de la réception de la notification push, avant qu'elle ne soit affichée à l'utilisateur. Braze transmettra un `Bundle` contenant les données de notification push Braze et un autre `Bundle` contenant les paires clé-valeur personnalisées envoyées soit via le tableau de bord, soit par les API de messagerie :

Braze transmettra un [`BrazeNotificationPayload`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/index.html) contenant les données de la notification push de Braze.

{% tabs %}
{% tab JAVA %}

```java
// Factory method implemented in your custom IBrazeNotificationFactory
@Override
public Notification createNotification(BrazeNotificationPayload brazeNotificationPayload) {
  // Example of getting notification title
  String title = brazeNotificationPayload.getTitleText();

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  String customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Factory method implemented in your custom IBrazeNotificationFactory
override fun createNotification(brazeNotificationPayload: BrazeNotificationPayload): Notification {
  // Example of getting notification title
  val title = brazeNotificationPayload.getTitleText()

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  val customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key")
}
```

{% endtab %}
{% endtabs %}

Vous pouvez renvoyer `null` à partir de votre méthode `createNotification()` personnalisée pour ne pas afficher du tout la notification, utiliser `BrazeNotificationFactory.getInstance().createNotification()` pour obtenir notre objet `notification` par défaut pour ces données et le modifier avant l'affichage, ou générer un objet `notification` complètement séparé pour l'affichage.

{% alert note %}
Pour obtenir de la documentation sur les clés de données push de Braze, reportez-vous au [SDK Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html).
{% endalert %}

### Étape 2 : Définir votre fabrique de notification personnalisée {#step-2-set-your-custom-notification-factory}

Pour demander à Braze d'utiliser votre fabrique de notification personnalisée, utilisez la méthode `setCustomBrazeNotificationFactory` afin de définir votre [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) :

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(IBrazeNotificationFactory brazeNotificationFactory);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(brazeNotificationFactory: IBrazeNotificationFactory)
```

{% endtab %}
{% endtabs %}

L'endroit recommandé pour définir votre `IBrazeNotificationFactory` personnalisée est dans la méthode de cycle de vie de l'application `Application.onCreate()` (pas l'activité). Cela permettra à la fabrique de notification d'être correctement définie chaque fois que le processus de votre application est actif.

{% alert important %}
La création de votre propre notification à partir de zéro est un cas d'usage avancé et ne doit être effectuée qu'après des tests approfondis et une compréhension approfondie de la fonctionnalité push de Braze. Par exemple, vous devez vous assurer que votre notification enregistre correctement les ouvertures push.
{% endalert %}

Pour annuler la définition de votre [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) personnalisée et revenir à la gestion par défaut de Braze pour les notifications push, transmettez `null` au setter de fabrique de notification personnalisée :

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(null);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(null)
```

{% endtab %}
{% endtabs %}

## Rendu de texte multicolore {#rendering-multicolor-text}

Dans la version 3.1.1 du SDK Braze, du HTML peut être envoyé à un appareil pour afficher du texte multicolore dans les notifications push.

![Un message push Android « Multicolor Push test message » où les lettres sont de différentes couleurs, en italique et avec une couleur d'arrière-plan.]({% image_buster /assets/img/multicolor_android_push.png %}){: style="max-width:40%;"}

Cet exemple est rendu avec le HTML suivant :

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>

<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

Gardez à l'esprit qu'Android limite les éléments et balises HTML valides dans vos notifications push. Par exemple, `marquee` n'est pas autorisé.

{% alert important %}
Le rendu de texte multicolore est spécifique à l'appareil et peut ne pas s'afficher selon l'appareil ou la version Android.
{% endalert %}

Pour afficher du texte multicolore dans une notification push, vous pouvez mettre à jour votre `braze.xml` ou `BrazeConfig` :

{% tabs local %}
{% tab braze.xml %}
Ajoutez ce qui suit dans votre `braze.xml` :

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```
{% endtab %}

{% tab BrazeConfig %}
Ajoutez ce qui suit dans votre [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration#runtime-configuration) :

{% subtabs local %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setPushHtmlRenderingEnabled(true)
  .build();
Braze.configure(this, brazeConfig);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setPushHtmlRenderingEnabled(true)
    .build()
Braze.configure(this, brazeConfig)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Balises HTML prises en charge {#supported-html-tags}

Actuellement, Google ne liste pas directement les balises HTML prises en charge pour Android dans sa documentation&#8212;cette information ne se trouve que dans le [fichier `Html.java` de son dépôt Git](https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/text/Html.java). Gardez cela à l'esprit lorsque vous consultez le tableau suivant, car ces informations proviennent de ce fichier et les balises HTML prises en charge sont susceptibles d'évoluer.

<table aria-label="Balises HTML prises en charge">
  <thead>
    <tr>
      <th>Catégorie</th>
      <th>Balise HTML</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">Mise en forme de texte de base</td>
      <td><code>&lt;b&gt;</code>, <code>&lt;strong&gt;</code></td>
      <td>Texte en gras</td>
    </tr>
    <tr>
      <td><code>&lt;i&gt;</code>, <code>&lt;em&gt;</code></td>
      <td>Texte en italique</td>
    </tr>
    <tr>
      <td><code>&lt;u&gt;</code></td>
      <td>Texte souligné</td>
    </tr>
    <tr>
      <td><code>&lt;s&gt;</code>, <code>&lt;strike&gt;</code>, <code>&lt;del&gt;</code></td>
      <td>Texte barré</td>
    </tr>
    <tr>
      <td><code>&lt;sup&gt;</code></td>
      <td>Texte en exposant</td>
    </tr>
    <tr>
      <td><code>&lt;sub&gt;</code></td>
      <td>Texte en indice</td>
    </tr>
    <tr>
      <td><code>&lt;tt&gt;</code></td>
      <td>Texte à chasse fixe</td>
    </tr>
    <tr>
      <td rowspan="3">Taille/Police</td>
      <td><code>&lt;big&gt;</code>, <code>&lt;small&gt;</code></td>
      <td>Changements relatifs de taille de texte</td>
    </tr>
    <tr>
      <td><code>&lt;font color="..."&gt;</code></td>
      <td>Définit la couleur de premier plan</td>
    </tr>
    <tr>
      <td><code>&lt;span&gt;</code> (avec CSS en ligne)</td>
      <td>Styles en ligne (par ex., couleur, arrière-plan)</td>
    </tr>
    <tr>
      <td rowspan="4">Paragraphe et bloc</td>
      <td><code>&lt;p&gt;</code>, <code>&lt;div&gt;</code></td>
      <td>Sections de niveau bloc</td>
    </tr>
    <tr>
      <td><code>&lt;br&gt;</code></td>
      <td>Saut de ligne</td>
    </tr>
    <tr>
      <td><code>&lt;blockquote&gt;</code></td>
      <td>Bloc de citation</td>
    </tr>
    <tr>
      <td><code>&lt;ul&gt;</code> + <code>&lt;li&gt;</code></td>
      <td>Liste non ordonnée avec puces</td>
    </tr>
    <tr>
      <td>Titres</td>
      <td><code>&lt;h1&gt;</code> - <code>&lt;h6&gt;</code></td>
      <td>Titres (différentes tailles)</td>
    </tr>
    <tr>
      <td rowspan="2">Liens et images</td>
      <td><code>&lt;a href="..."&gt;</code></td>
      <td>Lien cliquable</td>
    </tr>
    <tr>
      <td><code>&lt;img src="..."&gt;</code></td>
      <td>Image en ligne</td>
    </tr>
    <tr>
      <td>Autres éléments en ligne</td>
      <td><code>&lt;em&gt;</code>, <code>&lt;strong&gt;</code>, <code>&lt;dfn&gt;</code>, <code>&lt;cite&gt;</code></td>
      <td>Synonymes pour italique ou gras</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Balises HTML prises en charge" }

## Rendu des images en ligne {#rendering-inline-images}

### Comment ça fonctionne {#how-it-works}

Vous pouvez mettre en avant une image plus grande dans votre notification push Android en utilisant les notifications push avec image en ligne. Avec ce design, les utilisateurs n'ont pas besoin de développer manuellement la notification push pour agrandir l'image. Contrairement aux notifications push Android classiques, les images des notifications push en ligne ont un rapport hauteur/largeur de 3:2.

![Aperçu d'une notification push Android montrant le rendu d'une notification push avec image en ligne.]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="max-width:50%;"}

### Compatibilité {#compatibility}

Bien que vous puissiez envoyer des images en ligne à n'importe quel appareil, les appareils et SDK qui ne répondent pas aux versions minimales afficheront une image standard à la place. Pour que les images en ligne s'affichent correctement, le SDK Braze pour Android v10.0.0+ et un appareil fonctionnant sous Android M+ sont requis. Le SDK doit également être activé pour que l'image soit rendue.

{% alert note %}
Les appareils fonctionnant sous Android 12 s'afficheront différemment en raison de modifications apportées aux styles de notifications push personnalisées.
{% endalert %}

### Envoyer une notification push avec image en ligne {#sending-an-inline-image-push}

Lors de la création d'un message de notification push Android, cette fonctionnalité est disponible dans le menu déroulant **Notification Type**.

![L'éditeur de Campaign de notification push montrant l'emplacement du menu déroulant « Notification Type » à côté de l'aperçu standard de la notification push.]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})

## Paramètres {#settings}

De nombreux paramètres avancés sont disponibles pour les notifications push Android envoyées via le tableau de bord de Braze. Cet article décrit ces fonctionnalités et comment les utiliser efficacement.

![Panneau des paramètres avancés du compositeur de notifications push Android de Braze.]({% image_buster /assets/img_archive/android_advanced_settings.png %})

### ID de notification {#notification-id}

Un **ID de notification** est un identifiant unique pour une catégorie de messages de votre choix qui indique au service de messagerie de ne prendre en compte que le message le plus récent portant cet ID. Définir un ID de notification vous permet d'envoyer uniquement le message le plus récent et le plus pertinent, plutôt qu'un empilement de messages obsolètes et non pertinents.

#### Empêcher les notifications identiques de se remplacer mutuellement {#preventing-duplicate-notifications-from-overwriting}

Par défaut, lorsque des notifications push ont des titres et des corps de texte identiques, Android génère le même ID de notification pour les deux messages en hachant ensemble les chaînes de titre et de corps. Cela entraîne le remplacement de la première notification par la seconde, ce qui fait qu'une seule notification apparaît dans le volet de notifications.

Pour empêcher les notifications identiques de se remplacer mutuellement, vous pouvez spécifier des valeurs d'ID de notification uniques dans les paramètres de vos notifications push Android. Voici quelques options :

- **Utiliser le templating Liquid avec un horodatage :** Générez une valeur unique basée sur l'heure actuelle.

{% raw %}
```liquid
{% assign random_number = 'now' | date: '%s' | plus: 1000000 %}
{{random_number}}
```
{% endraw %}

- **Génération côté serveur :** Pour des valeurs véritablement aléatoires, générez l'ID de notification sur votre serveur et transmettez-le via Liquid. Cela garantit que chaque notification possède un identifiant distinct, permettant à plusieurs notifications de s'afficher simultanément.

### Priorité de distribution Firebase Messaging {#fcm-priority}

Le champ [Priorité de distribution Firebase Messaging](https://firebase.google.com/docs/cloud-messaging/android/message-priority#setting-priority-for-messages) vous permet de contrôler si une notification push est envoyée avec une priorité « normale » ou « élevée » à Firebase Cloud Messaging.

### Durée de vie (TTL) {#ttl}

Le champ **Durée de vie** (TTL) vous permet de définir une durée personnalisée de stockage des messages auprès du service de notifications push. Les valeurs par défaut de la durée de vie sont de quatre semaines pour FCM et de 31 jours pour ADM.

### Texte récapitulatif {#summary-text}

Le texte récapitulatif vous permet de définir du texte supplémentaire dans la vue étendue de la notification. Il sert également de légende pour les notifications contenant des images.

![Un message Android avec le titre « Ceci est le titre de la notification. » et le texte récapitulatif « Ceci est le texte récapitulatif de la notification. »]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

Le texte récapitulatif s'affiche sous le corps du message dans la vue étendue.

![Un message Android avec le titre « Ceci est le titre de la notification. » et le texte récapitulatif « Ceci est le texte récapitulatif de la notification. »]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Pour les notifications push contenant des images, le texte du message s'affiche dans la vue réduite, tandis que le texte récapitulatif est affiché comme légende de l'image lorsque la notification est étendue.

### URI personnalisés {#custom-uri}

La fonctionnalité **URI personnalisé** vous permet de spécifier une URL Web ou une ressource Android vers laquelle naviguer lorsque la notification est cliquée. Si aucun URI personnalisé n'est spécifié, cliquer sur la notification redirige les utilisateurs vers votre application. Vous pouvez utiliser l'URI personnalisé pour créer un deep link à l'intérieur de votre application et diriger les utilisateurs vers des ressources situées en dehors de votre application. Cela peut être spécifié via l'[API de messagerie]({{site.baseurl}}/api/endpoints/messaging) ou dans notre tableau de bord sous **Paramètres avancés** dans le compositeur de notifications push, comme illustré :

![Le paramètre avancé de deep linking dans le compositeur de notifications push de Braze.]({% image_buster /assets/img_archive/deep_link.png %})

### Priorité d'affichage des notifications {#notification-priority}

{% alert important %}
Le paramètre de priorité d'affichage des notifications n'est plus utilisé sur les appareils exécutant Android O ou une version ultérieure. Pour les appareils plus récents, définissez la priorité via la [configuration des canaux de notification](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

Le niveau de priorité d'une notification push affecte la façon dont votre notification est affichée dans le volet de notifications par rapport aux autres notifications. Il peut également affecter la vitesse et le mode de distribution, car les messages de priorité normale et inférieure peuvent être envoyés avec une latence légèrement plus élevée ou regroupés pour préserver l'autonomie de la batterie, tandis que les messages de priorité élevée sont toujours envoyés immédiatement.

Sous Android O, la priorité des notifications est devenue une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir la priorité d'un canal lors de sa configuration, puis utiliser le tableau de bord pour sélectionner le canal approprié lors de l'envoi de vos sons de notification. Pour les appareils exécutant des versions d'Android antérieures à O, il est possible de spécifier un niveau de priorité pour les notifications Android via le tableau de bord de Braze et l'API de messagerie.

Pour envoyer un message à l'ensemble de votre base d'utilisateurs avec une priorité spécifique, nous recommandons de spécifier indirectement la priorité via la [configuration des canaux de notification](https://developer.android.com/training/notify-user/channels#importance) (pour cibler les appareils O+) *et* d'envoyer la priorité individuelle depuis le tableau de bord (pour cibler les appareils &#60;O).

Les niveaux de priorité que vous pouvez définir pour les notifications push Android ou Fire OS sont :

| Priorité | Description/Utilisation prévue | Valeur `priority` (pour les messages API) |
|----------|-------------------------------|-------------------------------------------|
| Max      | Messages urgents ou critiques en termes de temps | `2` |
| Élevée   | Communication importante, comme un nouveau message d'un ami | `1` |
| Par défaut | La plupart des notifications — à utiliser si votre message ne correspond explicitement à aucun des autres types de priorité | `0` |
| Basse    | Informations que vous souhaitez porter à la connaissance des utilisateurs mais qui ne nécessitent pas d'action immédiate | `-1` |
| Min      | Informations contextuelles ou d'arrière-plan. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Priorité d'affichage des notifications" }

Pour plus d'informations, consultez la documentation Google sur les [notifications Android](http://developer.android.com/design/patterns/notifications.html).

### Sons {#sounds}

Sous Android O, les sons de notification sont devenus une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir le son d'un canal lors de sa configuration, puis utiliser le tableau de bord pour sélectionner le canal approprié lors de l'envoi de vos notifications.

Pour les appareils exécutant des versions d'Android antérieures à O, Braze vous permet de définir le son d'un message push individuel via le compositeur du tableau de bord. Vous pouvez le faire en spécifiant une ressource sonore locale sur l'appareil (par exemple, `android.resource://com.mycompany.myapp/raw/mysound`). Spécifier « default » dans ce champ jouera le son de notification par défaut de l'appareil. Cela peut être spécifié via l'[API de messagerie]({{site.baseurl}}/api/endpoints/messaging) ou dans le tableau de bord sous **Paramètres avancés** dans le compositeur de notifications push.

![Le paramètre avancé de son dans le compositeur de notifications push de Braze.]({% image_buster /assets/img_archive/sound_android.png %})

Saisissez l'URI complet de la ressource sonore (par exemple, `android.resource://com.mycompany.myapp/raw/mysound`) dans le champ du tableau de bord.

Pour envoyer un message à l'ensemble de votre base d'utilisateurs avec un son spécifique, nous recommandons de spécifier indirectement le son via la [configuration des canaux de notification](https://developer.android.com/training/notify-user/channels) (pour cibler les appareils O+) *et* d'envoyer le son individuel depuis le tableau de bord (pour cibler les appareils &#60;O).