---
nav_title: Notifications push
article_title: Notifications push pour Windows Universal
platform: Windows Universal
page_order: 1
description: "Cet article couvre les instructions d'intégration des notifications push pour la plateforme Windows Universal."
channel: push
hidden: true
---

# Intégration des notifications push {#push-notification-integration}
{% multi_lang_include archive/windows_deprecation.md %}

![Exemple de notification push pour Windows Universal.]({% image_buster /assets/img_archive/windows_uni_push_sample.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Une notification push est une alerte hors application qui apparaît sur l'écran de l'utilisateur lorsqu'une mise à jour importante se produit. Les notifications push constituent un moyen précieux de fournir à vos utilisateurs un contenu urgent et pertinent, ou de les réengager dans votre application.

Consultez notre [documentation]({{site.baseurl}}/user_guide/channels/push/best_practices/) pour connaître les bonnes pratiques.

## Étape 1 : Configurer votre application pour les notifications push {#step-1-configure-your-application-for-push}

Assurez-vous que les paramètres suivants sont configurés dans votre fichier `Package.appxmanifest` :

Dans l'onglet **Application**, assurez-vous que `Toast Capable` est défini sur `YES`.

## Étape 2 : Configurer le tableau de bord de Braze {#step-2-configure-the-braze-dashboard}

1. [Trouvez votre SID et votre secret client](http://msdn.microsoft.com/en-us/library/windows/apps/hh465407.aspx)
2. Dans la page **Paramètres** du tableau de bord de Braze, ajoutez le SID et le secret client dans vos paramètres.<br>![]({% image_buster /assets/img_archive/windows_sid.png %} "Windows SID dashboard")

## Étape 3 : Mettre à jour pour l'enregistrement des ouvertures en arrière-plan {#step-3-update-for-background-open-logging}

Dans votre méthode `OnLaunched`, une fois que vous avez appelé `OpenSession`, ajoutez l'extrait de code suivant.

```
string campaignId = e.Arguments.Split(new[] { "_ab_pn_cid" }, StringSplitOptions.None)[0];
if (!string.IsNullOrEmpty(campaignId))
{
Appboy.SharedInstance.PushManager.LogPushNotificationOpened(campaignId);
}
```

## Étape 4 : Créer des gestionnaires d'événements {#step-4-creating-event-handlers}

Pour écouter les événements déclenchés lorsqu'une notification push est reçue et activée (l'utilisateur a cliqué dessus), créez des gestionnaires d'événements et ajoutez-les aux événements `PushManager` :

- `Appboy.SharedInstance.PushManager.PushReceivedEvent += YourPushReceivedEventHandler;`
- `Appboy.SharedInstance.PushManager.ToastActivatedEvent += YourToastActivatedEventHandler;`

Vos gestionnaires d'événements doivent avoir les signatures suivantes :

- `void YourPushReceivedEventHandler(PushNotificationChannel sender, AppboyPushNotificationReceivedEventArgs args);`
- `void YourToastActivatedEventHandler(ToastNotification sender, AppboyToastActivatedEventArgs args);`

## Étape 5 : Créer des liens profonds entre la notification push et l'application {#step-5-deep-linking-from-push-into-your-app}

### Partie 1 : Créer des liens profonds pour votre application {#part-1-creating-deep-links-for-your-app}

Les liens profonds permettent de diriger les utilisateurs depuis l'extérieur de votre application directement vers un écran ou une page spécifique de celle-ci. En règle générale, cela se fait en enregistrant un schéma d'URL (par exemple, myapp://mypage) auprès d'un système d'exploitation et en enregistrant votre application pour gérer ce schéma ; lorsque le système d'exploitation est invité à ouvrir une URL de ce format, il transfère le contrôle à votre application.

La prise en charge des liens profonds WNS fonctionne différemment : elle lance votre application avec des données indiquant où diriger l'utilisateur. Lorsqu'une notification push WNS est créée, elle peut inclure une chaîne de caractères de lancement transmise au `OnLaunched` de votre application quand l'utilisateur clique sur la notification push et que votre application s'ouvre. Nous utilisons déjà cette chaîne de caractères de lancement pour le suivi de Campaign et nous donnons aux utilisateurs la possibilité d'ajouter leurs propres données, qui peuvent être analysées et utilisées pour diriger l'utilisateur lorsque l'application est lancée.

Si vous spécifiez une chaîne de caractères de lancement supplémentaire dans le tableau de bord ou la REST API, elle sera ajoutée à la fin de celle que nous créons, après la clé « abextras= ». Par exemple, une chaîne de caractères de lancement peut ressembler à `ab_cn_id=_trackingid_abextras=page=settings`, dans laquelle vous avez spécifié `page=settings` dans le paramètre de chaîne de caractères de lancement supplémentaire afin de pouvoir l'analyser et diriger l'utilisateur vers la page des paramètres.

### Partie 2 : Créer des liens profonds via le tableau de bord {#part-2-deep-linking-through-the-dashboard}

Spécifiez la chaîne de caractères à ajouter à la chaîne de caractères de lancement dans le champ « Additional Launch String Configuration » au sein des paramètres de notification push.

![]({% image_buster /assets/img_archive/windows_deep_link_click_action.png %} "Deep Link Click Action")

### Partie 3 : Créer des liens profonds via la REST API {#part-3-deep-linking-through-the-rest-api}

Braze permet également d'envoyer des liens profonds via la REST API. Les [objets push Windows Universal]({{site.baseurl}}/api/objects_filters/) acceptent un paramètre facultatif `extra_launch_string`.