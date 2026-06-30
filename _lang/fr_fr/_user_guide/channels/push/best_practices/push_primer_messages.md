---
nav_title: Messages in-app de push primer
article_title: Messages in-app de push primer
page_order: 1
page_type: reference
description: "Cet article couvre les conditions préalables pour les messages in-app de push primer et comment les configurer."
channel: push

---

# Messages in-app de push primer {#push-primer-in-app-messages}

> Vous n'avez qu'une seule chance de demander aux utilisateurs l'autorisation d'envoyer des notifications push. Il est donc crucial d'optimiser votre inscription push pour maximiser la portée de vos notifications push. Utilisez les messages in-app pour expliquer quel type de messages vos utilisateurs peuvent s'attendre à recevoir s'ils choisissent de s'abonner, avant de leur montrer l'invite push native. C'est ce qu'on appelle un push primer.

![Message in-app de push primer pour une application de streaming. La notification indique « Recevoir des notifications push de Movie Cannon ? Les notifications peuvent inclure de nouveaux films, séries TV ou d'autres avis et peuvent être désactivées à tout moment. »]({% image_buster /assets/img_archive/push_primer_iam.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

Pour créer un message in-app de push primer dans Braze, vous pouvez utiliser le comportement au clic du bouton « Request Push Permission » lors de la création d'un message in-app pour iOS, Android ou le Web.

## Conditions préalables {#prerequisites}

Cette fonctionnalité nécessite un [comportement au clic du bouton](#button-actions), qui est pris en charge dans les versions minimales suivantes ou ultérieures :

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

De plus, notez les détails spécifiques à chaque plateforme suivants :

{% tabs local %}
{% tab android %}
| Version de l'OS | Informations supplémentaires |
|----------|----------------------|
| **Android 12 et versions antérieures** | L'implémentation de push primers n'est pas recommandée car le push est activé par défaut. |
| **Android 13+** | Si un utilisateur refuse votre invite d'autorisation push deux fois, Android bloque les invites ultérieures, y compris les messages de push primer de Braze. Pour accorder l'autorisation après cela, les utilisateurs doivent activer manuellement le push pour votre application dans les paramètres de leur appareil. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }
{% endtab %}

{% tab swift %}
### Informations générales {#general-information}

- L'invite push ne peut être affichée qu'une seule fois par installation, ce qui est imposé par le système d'exploitation.
- L'invite ne s'affiche pas si le paramètre push de l'application est explicitement activé ou désactivé. Elle ne s'affiche que pour les utilisateurs disposant d'une [autorisation provisoire](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - **Le paramètre push de l'application est activé :** Braze n'affiche pas le message in-app, car l'utilisateur s'est déjà abonné.
  - **Le paramètre push de l'application est désactivé :** Vous devez rediriger l'utilisateur vers les paramètres de notification push de votre application dans les paramètres de l'appareil.
- **Retester après un refus :** Si un utilisateur refuse l'invite native, iOS ne l'affiche plus pour cette installation de l'application. Pour retester le flux de push primer, les utilisateurs doivent généralement désinstaller et réinstaller l'application, ou modifier l'autorisation de notification pour votre application dans **Réglages**.

### Suppression manuelle du code {#manual-code-removal}

Le message in-app que vous configurez à l'aide de ce tutoriel appelle automatiquement le code d'invite push native lorsqu'un utilisateur clique sur le bouton du message in-app. Pour éviter de demander l'autorisation de notification push deux fois, ou au mauvais moment, un développeur doit modifier toute intégration de notification push existante qu'il a implémentée pour s'assurer que votre message in-app est le premier push primer que vos utilisateurs voient.

Votre équipe de développement doit examiner votre implémentation des notifications push pour votre application ou site et supprimer manuellement tout code qui demande l'autorisation push. Par exemple, supprimez les références au code suivant :

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
requestAuthorizationWithOptions
```
{% endsubtab %}
{% subtab swift %}
```swift
requestAuthorization
```
{% endsubtab %}
{% subtab JavaScript %}
```javascript
braze.requestPushPermission()
// or
appboy.registerAppboyPushMessages()
```
{% endsubtab %}
{% subtab Java %}
```java
android.permission.POST_NOTIFICATIONS
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Étape 1 : Créer un message in-app {#step-1-create-an-in-app-message}

Tout d'abord, [créez un message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional), puis sélectionnez votre type de message et votre disposition.

Pour vous assurer d'avoir suffisamment d'espace pour votre message et vos boutons, utilisez une disposition de message en plein écran ou en fenêtre modale. Si vous choisissez le plein écran, notez qu'une image est requise.

## Étape 2 : Rédiger votre message {#step-2-build-your-message}

Il est maintenant temps d'ajouter votre texte ! N'oubliez pas qu'un push primer est censé préparer l'utilisateur à activer les notifications push. Dans le corps de votre message, nous vous suggérons de mettre en avant les raisons pour lesquelles vos utilisateurs devraient activer les notifications push. Soyez précis sur le type de notifications que vous souhaitez envoyer et la valeur qu'elles peuvent apporter.

Par exemple, une application d'actualités pourrait utiliser le push primer suivant :

```plaintext
Breaking news on the go! Enable push notifications to get alerts for major stories and topics that matter to you.
```

Tandis qu'une application de streaming pourrait utiliser le suivant :

```plaintext
Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time.
```

Pour les bonnes pratiques et les ressources supplémentaires, consultez [Créer des invites d'abonnement personnalisées]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

## Étape 3 : Spécifier le comportement des boutons {#button-actions}

Pour ajouter des boutons à votre message in-app, faites glisser deux blocs **Button** dans votre message, qui servent de boutons principal et secondaire dans votre message in-app. Vous pouvez également faire glisser une ligne dans votre message, puis faire glisser les boutons dans la ligne, afin que les boutons soient sur la même ligne horizontale (au lieu d'être empilés l'un sur l'autre). Nous recommandons « Allow notifications » et « Not now » comme boutons de départ, mais il existe de nombreuses invites de boutons différentes que vous pouvez attribuer.

Après avoir ajouté le texte des boutons, spécifiez le comportement au clic pour chaque bouton :

- **Button 1 :** Définissez-le sur « Close Message ». C'est votre bouton secondaire, ou l'option « Not now ».
- **Button 2 :** Définissez-le sur « Request Push Permission ». C'est votre bouton principal, ou l'option « Allow notifications ».

![Compositeur de message in-app avec deux boutons : « Allow notifications » et « Not now ».]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## Étape 4 : Planifier la réception {#step-4-schedule-delivery}

Pour configurer l'envoi de votre push primer à un moment pertinent, vous devez planifier votre message in-app comme un message par événement avec **Perform Custom Event** comme action de déclenchement.

Bien que le moment idéal varie, Braze suggère d'attendre qu'un utilisateur effectue une [action à forte valeur](https://www.braze.com/resources/videos/mapping-high-value-actions), indiquant qu'il commence à percevoir la valeur de votre application ou site, ou lorsqu'il y a un besoin impérieux auquel les notifications push peuvent répondre (par exemple, après avoir passé une commande et que vous souhaitez lui proposer des informations de suivi de livraison). De cette façon, l'invite est bénéfique pour le client plutôt que seulement pour votre marque.

![Paramètres de livraison par événement pour envoyer aux utilisateurs qui ont effectué l'événement personnalisé « Add to Watch List ».]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## Étape 5 : Cibler les utilisateurs {#step-5-target-users}

L'objectif d'une campagne de push primer est d'inviter les utilisateurs sur tout appareil où ils n'ont pas encore accordé les autorisations push. Cela peut inclure les nouveaux utilisateurs ou les utilisateurs existants qui obtiennent un nouvel appareil ou réinstallent votre application.

{% alert important %}
**Suppression automatique avec le push primer sans code** : Si vous utilisez le push primer sans code (l'action de bouton « Request Push Permission »), vous n'avez pas besoin d'ajouter de filtres d'abonnement push à votre segmentation. Le SDK supprime automatiquement le message in-app sur les appareils qui disposent déjà d'un jeton de notification push actif, quel que soit le statut push de l'utilisateur sur d'autres appareils. Pour plus d'informations sur le ciblage des utilisateurs avec plusieurs appareils, consultez [Cibler les utilisateurs avec plusieurs appareils](#targeting-users-with-multiple-devices).
{% endalert %}

Si vous n'utilisez pas le push primer sans code, ajoutez un filtre où `Foreground Push Enabled For App is false`. Ce filtre identifie les installations d'applications individuelles qui ne sont pas encore abonnées aux notifications push de premier plan.

{% alert important %}
L'utilisation d'un filtre au niveau utilisateur comme `Push Subscription Status is not Opted In` exclut les utilisateurs qui sont déjà abonnés sur un autre appareil, les empêchant de recevoir l'invite sur leur nouvel appareil.
{% endalert %}

Au-delà de cela, vous pouvez décider quels segments supplémentaires vous jugez les plus appropriés. Par exemple, vous pourriez cibler les utilisateurs qui ont effectué un deuxième achat, les utilisateurs qui viennent de créer un compte pour devenir membre, ou même les utilisateurs qui visitent votre application plus de deux fois par semaine. Cibler les utilisateurs pour ces segments cruciaux augmente la probabilité que les utilisateurs s'abonnent et activent les notifications push.

### Cibler les utilisateurs avec plusieurs appareils {#targeting-users-with-multiple-devices}

Étant donné que Braze capture les données utilisateur au niveau du profil plutôt qu'au niveau de l'appareil, cibler les utilisateurs qui possèdent plusieurs appareils peut être complexe. Les filtres d'abonnement push dans la segmentation incluent ou excluent les utilisateurs en fonction de l'état d'abonnement d'un seul appareil plutôt que de l'état d'abonnement de l'appareil spécifiquement ciblé. De plus, les états provisoires sur iOS ajoutent de la complexité, car ces appareils disposent techniquement de jetons de notification push de premier plan, mais les utilisateurs ne sont pas explicitement abonnés.

#### Le problème avec les filtres d'abonnement push {#the-problem-with-push-subscription-filters}

Lorsqu'un utilisateur possède plusieurs appareils avec des états d'abonnement push différents, les filtres d'abonnement push dans votre segmentation peuvent ne pas cibler certains appareils. Considérez ces scénarios :

{% details Scénario 1 : L'utilisateur possède deux appareils sur des plateformes différentes %}

**L'utilisateur possède deux appareils :**
- Appareil A : Android, abonné aux notifications push
- Appareil B : iOS, non abonné aux notifications push

**Filtres de segment qui ne fonctionnent pas :**
- `Push enabled = false` – L'utilisateur est activé pour le push sur son appareil Android, il n'entre donc pas dans le segment. Le segment n'inclut pas l'appareil iOS.
- `Push subscription status is not opted in` – L'utilisateur est activé pour le push sur son appareil Android, il n'entre donc pas dans le segment. Le segment n'inclut pas l'appareil iOS.

**Filtres de segment qui fonctionnent :**
- `Push enabled for iOS = false` – L'utilisateur est activé pour le push sur son appareil Android, mais nous ne ciblons que les appareils iOS, donc l'utilisateur entre dans le segment. Le segment inclut l'appareil iOS.

{% enddetails %}

{% details Scénario 2 : L'utilisateur possède deux appareils iOS avec des états différents %}

**L'utilisateur possède deux appareils iOS :**
- Appareil A : Abonné aux notifications push
- Appareil B : Provisoirement activé mais non abonné

**Filtres de segment qui ne fonctionnent pas :**
- `Push enabled = false` – L'appareil A est abonné aux notifications push, donc l'utilisateur n'entre pas dans le segment. Le segment n'inclut pas l'appareil B.
- `Provisionally opted in = true` – L'appareil A est entièrement abonné, ce qui signifie qu'il n'est pas dans un état provisoire. L'utilisateur n'entre pas dans le segment. Le segment n'inclut pas l'appareil B.
- `Push enabled for app > iOS = false` – L'appareil A est abonné aux notifications push sur iOS, donc l'utilisateur n'entre pas dans le segment. Le segment n'inclut pas l'appareil B.
- `Push subscription status is not opted in` – L'appareil A est abonné aux notifications push, donc l'utilisateur n'entre pas dans le segment. Le segment n'inclut pas l'appareil B.

**Résultat :** L'utilisation de toute combinaison de ces filtres push entraîne l'exclusion d'au moins un appareil du segment.

{% enddetails %}

{% details Scénario 3 : L'utilisateur possède trois appareils ou plus sur le même OS %}

**L'utilisateur possède trois appareils :**
- Appareil A : Abonné aux notifications push
- Appareil B : Non abonné aux notifications push
- Appareil C : Non abonné aux notifications push

**Filtres de segment qui ne fonctionnent pas :**
- `Push enabled = false` – L'appareil A est abonné aux notifications push, donc l'utilisateur n'entre pas dans le segment. Le segment n'inclut pas les appareils B et C.
- `Push enabled for app > X = false` – L'appareil A est abonné aux notifications push sur l'application spécifiée, donc l'utilisateur n'entre pas dans le segment. Le segment n'inclut pas les appareils B et C.
- `Push subscription status is not opted in` – L'appareil A est abonné aux notifications push, donc l'utilisateur n'entre pas dans le segment. Le segment n'inclut pas les appareils B et C.

**Résultat :** L'utilisation de toute combinaison de ces filtres push laisse au moins un appareil non ciblé.

{% enddetails %}

#### Solution : utiliser le push primer sans code {#solution-use-the-no-code-push-primer}

La solution recommandée est d'utiliser le push primer sans code (l'action de bouton « Request Push Permission ») sans filtres de segmentation supplémentaires sur le statut push.

{% alert important %}
**Suppression automatique** : Le push primer sans code se supprime automatiquement sur les appareils qui disposent déjà d'un jeton de notification push actif. Le SDK vérifie si un utilisateur sur son appareil spécifique dispose déjà d'un jeton de notification push. Si le SDK constate que l'utilisateur s'est déjà abonné (par exemple, suite à une demande précédente ou via les paramètres de l'appareil), le SDK supprime automatiquement le message in-app sans nécessiter de filtres de segmentation supplémentaires. Le primer s'affiche dans tous les autres scénarios, y compris si un utilisateur est provisoirement abonné aux notifications push.
{% endalert %}

L'avantage d'utiliser le push primer sans code est que la fonctionnalité est prise en charge par le SDK Braze. Étant donné que le SDK peut détecter le statut du jeton de notification push sur l'appareil spécifique qui affiche le message, vous n'avez pas besoin de vous appuyer sur des filtres de segmentation au niveau du profil qui pourraient exclure les utilisateurs avec plusieurs appareils.

#### Considérations {#considerations}

**Push primer sans code requis** : Vous devez utiliser le push primer sans code pour que la suppression automatique fonctionne. Si vous configurez une logique personnalisée ou des liens profonds au lieu d'utiliser l'action de bouton « Request Push Permission », le SDK ne peut pas identifier que vous essayez d'afficher un push primer. Cela entraîne l'affichage du message quel que soit l'état d'abonnement de cet appareil.

**Suppression pour les utilisateurs qui se sont désabonnés** : Vous pouvez souhaiter supprimer le message in-app pour les utilisateurs qui se sont explicitement désabonnés des notifications push (par exemple, depuis la demande native ou les paramètres de l'appareil) et recibler ces utilisateurs avec une campagne de nurture séparée. Pour ce faire, utilisez la logique Liquid suivante en combinaison avec le push primer sans code :

{% raw %}
```liquid
{% if targeted_device.${foreground_push_enabled} == false %}
{% abort_message('user turned off push notifications') %}
{% endif %}
- message goes here -
```
{% endraw %}

Le filtre Liquid `targeted_device` examine uniquement l'appareil sur lequel le message est affiché, plutôt que le profil utilisateur. Sur cet appareil, `foreground_push_enabled` est défini sur `true` lorsqu'il y a un jeton de notification push de premier plan actif et défini sur `false` lorsque le système d'exploitation signale que les notifications push ont été désactivées (par exemple, l'utilisateur les a explicitement désactivées). Pour les appareils entièrement nouveaux qui n'ont pas encore répondu à un état d'autorisation push, `foreground_push_enabled` n'est pas défini et n'a aucune valeur. Étant donné que la condition Liquid vérifie spécifiquement {% raw %}`false`{% endraw %}, elle supprime le primer uniquement pour les appareils avec un désabonnement explicite, tandis que les appareils dans cet état inconnu sont toujours éligibles et peuvent recevoir le push primer.

## Étape 6 : Événements de conversion {#step-6-conversion-events}

Braze suggère des paramètres par défaut pour les conversions, mais vous pouvez configurer des [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) autour des push primers.