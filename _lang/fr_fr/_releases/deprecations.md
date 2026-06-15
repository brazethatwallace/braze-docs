---
nav_title: Obsolescences
article_title: Obsolescences
page_order: 9
page_type: reference
description: "Cette page comprend des références à des articles obsolètes et fournit une liste de fonctionnalités obsolètes et non prises en charge."
---

# Obsolescences {#deprecations}

La technologie est toujours en mouvement, à l'intérieur comme à l'extérieur de Braze ! Et nous faisons de notre mieux pour tenir la cadence. Vous trouverez ici les origines de Braze et de sa technologie — comment nous avons accompagné les utilisateurs dans le passé — avant aujourd'hui, en tout cas…

Vous êtes peut-être arrivé ici en recherchant une intégration ou une fonctionnalité qui n'existe plus. C'est notre manière de vous tenir informé de nos progrès et des évolutions au sein de l'industrie technologique. Vous pouvez consulter une liste de fonctionnalités obsolètes et non prises en charge et lire les articles associés en visitant les liens suivants.

## Articles obsolètes {#deprecated-articles}

- [Récepteur de diffusion personnalisé de notifications push pour Android]({{site.baseurl}}/releases/deprecations/custom_broadcast_receiver/)
- [Configuration du SDK Eclipse]({{site.baseurl}}/releases/deprecations/eclipse_setup_deprecated/)
- [Obsolescence de TLS 1.0 et 1.1]({{site.baseurl}}/releases/deprecations/tls_deprecation/)
- [Intégration du webhook Twilio]({{site.baseurl}}/releases/deprecations/twilio/)
- [Partenariat Apptimize]({{site.baseurl}}/releases/deprecations/apptimize/)
- [Partenariat avec Grouparoo]({{site.baseurl}}/releases/deprecations/grouparoo/)
- [Obsolescence de Shopify `checkout.liquid`]({{site.baseurl}}/releases/deprecations/shopify_checkout/)

## Journal des obsolescences {#deprecations-log}

### Shopify `checkout.liquid`

**Prise en charge retirée** : août 2024 (phase 1), août 2025 (phase 2)

La prise en charge de Shopify `checkout.liquid` commencera à être abandonnée en août 2024 et sera définitivement retirée en août 2025. Shopify effectue la transition vers [Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions), qui est plus sécurisé, plus performant et plus personnalisable.

### Récepteur de diffusion personnalisé de notifications push pour Android {#custom-push-broadcast-receiver-for-android}

**Prise en charge retirée** : octobre 2022

L'utilisation d'un `BroadcastReceiver` personnalisé pour les notifications push est obsolète. Utilisez plutôt [` subscribeToPushNotificationEvents()`]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_using-a-callback-for-push-events) à la place.

### Partenariat avec Grouparoo {#grouparoo-partnership}

**Prise en charge retirée** : avril 2022

La prise en charge de Grouparoo a été arrêtée en avril 2022.

### SDK Windows de Braze {#braze-windows-sdk}

**24 mars 2022** : le SDK Windows de Braze est obsolète et aucune nouvelle application Windows ne peut être créée dans le tableau de bord de Braze.<br>
**15 septembre 2022** : aucun nouveau message ne peut être envoyé aux applications Windows. Les messages existants et la collecte de données ne sont pas affectés.<br>
**11 janvier 2024** : Braze ne diffuse plus de messages et ne collecte plus de données à partir des applications Windows.

### Intégration des notifications push baidu {#baidu-push-integration}

**24 mars 2022** : l'intégration entre les notifications push baidu et Braze est obsolète et aucune nouvelle application baidu ne peut être créée dans le tableau de bord de Braze.<br>
**15 septembre 2022** : aucun nouveau message push baidu ne peut être créé. Les messages existants et la collecte de données ne sont pas affectés.<br>
**11 janvier 2024** : Braze ne diffuse plus de messages et ne collecte plus de données à partir des applications baidu.

### Variable globale appboyBridge {#appboybridge-global-variable}

**Prise en charge retirée** : mai 2021<br>
**Remplacée par** : `brazeBridge`

La variable globale `appboyBridge` est obsolète et remplacée par `brazeBridge`. `appboyBridge` continuera à fonctionner pour les clients existants, mais nous vous recommandons de migrer vers `brazeBridge` si vous utilisez `appboyBridge`.

### Partenariat Amazon Moments {#amazon-moments-partnership}

**Prise en charge retirée** : juin 2020

La prise en charge d'Amazon Moments a été arrêtée en juin 2020. Amazon Moments est fusionné dans Amazon Advertising et a abandonné ses API ainsi que notre intégration.

### Partenariat Factual {#factual-partnership}

**Prise en charge retirée** : juin 2020

La prise en charge de Factual a été arrêtée en juin 2020. Factual a récemment été acquis par Foursquare et ne s'intègre plus à la plateforme Braze.

### Intégration du webhook Twilio {#twilio-webhook-integration}

**Prise en charge retirée** : janvier 2020

La prise en charge de l'[intégration du webhook Twilio]({{site.baseurl}}/partners/twilio/) n'est plus assurée depuis le 31 janvier 2020. Si vous souhaitez continuer à accéder aux services SMS avec Braze, consultez notre [documentation sur les SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/).

### Partenariat Apptimize {#apptimize-partnership}

**Prise en charge retirée** : août 2019

Si vous utilisez actuellement [Apptimize avec Braze]({{site.baseurl}}/releases/deprecations/apptimize/), vous ne subirez pas d'interruption de service. Vous pouvez toujours définir des attributs personnalisés Apptimize sur les profils utilisateur Braze. Cependant, aucune escalade de support formelle avec le partenaire ne sera fournie.

### Messages in-app originaux {#original-in-app-messages}

**Prise en charge retirée :** février 2019<br>
**Remplacés par** : [Messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)

Braze a amélioré l'apparence des messages in-app pour se conformer aux meilleures pratiques en matière d'UX et d'UI, et ne prend plus en charge les messages in-app originaux.

Braze est passé à une nouvelle forme de messages in-app avec les versions de SDK suivantes :
- iOS : `2.19.0`
- Android : `1.13.0`
- Web : `1.3.0`

Avant ces versions, Braze prenait en charge les « messages in-app originaux ». Auparavant, la prise en charge des messages in-app originaux était fournie à tout client ayant lancé une campagne in-app avant la nouvelle version. Toutes les statistiques de campagne n'ont pas été affectées par ce changement, et ceux qui avaient envoyé des messages in-app originaux ont eu la possibilité d'en envoyer d'autres via le bouton **Create Campaign** de la page **Campaign**.

### Widget de commentaires {#feedback-widget}

**Prise en charge retirée** : 1er juillet 2019.

Le SDK de Braze fournissait un widget de commentaires qui pouvait être ajouté à votre application pour permettre aux utilisateurs de laisser un retour à l'aide de la méthode `submitfeedback` et de le transmettre à Desk.com ou Zendesk. Il était géré depuis le tableau de bord.

### Google Cloud Messaging (GCM)

**Prise en charge retirée** : fin de prise en charge par Braze : juillet 2018, fin de prise en charge par Google : 29 mai 2019<br>
**Remplacé par** : [Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)

Google a [supprimé la prise en charge de GCM](https://developers.googleblog.com/2018/04/time-to-upgrade-from-gcm-to-fcm.html) à compter du 29 mai 2019. Braze a cessé de prendre en charge GCM à partir des SDK Android en juillet 2018, ce qui a été noté dans nos [journaux des modifications du SDK Android](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md). Cela signifie que les jetons GCM existants continueront de fonctionner et que vous pourrez envoyer des messages à vos utilisateurs existants. En revanche, vous ne pourrez pas envoyer de messages à de nouveaux utilisateurs.

Les clients qui n'ont pas encore migré vers [Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase) peuvent être concernés par ce changement.

Si vous n'avez pas effectué la transition vers FCM, tous les enregistrements de jetons push GCM échoueront. Si vos applications prennent actuellement en charge GCM, vous devrez travailler avec vos équipes de développement sur la [transition de GCM vers Firebase Cloud Messaging (FCM)](https://developers.google.com/cloud-messaging/android/android-migrate-fcm).

### Eclipse

**Prise en charge retirée** : 2014-2015<br>
**Remplacé par** : [Android Studio]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#using-android-studio)

Braze a cessé de prendre en charge l'IDE Eclipse en raison de l'[abandon](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html) par Google de la prise en charge du plugin Eclipse Android Developer Tools (ADT).

Si vous avez besoin d'aide pour votre intégration Eclipse avant la migration, contactez l'[assistance]({{site.baseurl}}/support_contact/).

### Raw Event Stream (RES) {#the-raw-event-stream-res}

**Prise en charge retirée** : juillet 2018<br>
**Remplacé par** : [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)

Le flux d'événements bruts était le prédécesseur de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) et a été abandonné pour faire place à l'avenir des données chez Braze.

### Delay While Idle — fonctionnalité GCM {#delay-while-idle-gcm-feature}

**Prise en charge retirée** : novembre 2016

Le paramètre Delay While Idle faisait auparavant partie des [options push de GCM](https://developers.google.com/cloud-messaging/http-server-ref). Google a cessé de prendre en charge cette option le 15 novembre 2016. Auparavant, lorsque cette valeur était définie sur **true**, elle indiquait que le message ne devait pas être envoyé tant que l'appareil n'était pas actif.

### Endpoints personnalisés {#custom-endpoints}

**Prise en charge retirée** : décembre 2019

Suppression des endpoints personnalisés. Si vous disposez d'un endpoint personnalisé, vous pouvez continuer à l'utiliser, mais Braze n'en fournit plus de nouveaux.