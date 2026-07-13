---
nav_title: Aperçu du SDK
article_title: Présentation du SDK pour les développeurs
description: "Cet article de référence d'onboarding fournit un aperçu technique du SDK Braze pour les développeurs. Il aborde les analyses par défaut suivies par le SDK, le blocage de la collecte automatique de données et la version du SDK en production de votre application."
page_order: 0
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}Aperçu du SDK pour les développeurs {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecompathdevelopersdk-integration-basics-stylefloatrightwidth120pxborder0-classnoimgbordersdk-overview-for-developers}

> Avant de commencer à intégrer les SDK Braze, vous vous demandez peut-être exactement ce que vous concevez et intégrez. Vous pourriez être curieux de savoir comment personnaliser davantage le SDK pour mieux répondre à vos besoins. Cet article peut vous aider à répondre à toutes vos questions concernant le SDK.

Vous êtes marketeur et cherchez un aperçu de base du SDK ? Consultez plutôt notre [présentation pour les marketeurs]({{site.baseurl}}/user_guide/get_started/sdk_overview).

Le SDK Braze en bref :
* Collecte et synchronise les données de l'utilisateur dans un profil utilisateur consolidé
* Recueille automatiquement les données de session, les informations sur l'appareil et les jetons de notification push
* Capture les données d'engagement marketing et les données personnalisées spécifiques à votre entreprise
* Alimente les canaux de communication de notifications push, de messages in-app et de carte de contenu

Regardez la vidéo suivante pour une brève introduction aux bases de l'intégration du SDK Braze et à ses fonctionnalités principales.

{% multi_lang_include video.html id="il152jayp0" source="wistia" %}

## Performances applicatives {#app-performance}

Braze ne devrait avoir aucun impact négatif sur les performances de votre application.

Les SDK Braze ont une empreinte très légère. Nous modifions automatiquement le taux auquel nous purgeons les données des utilisateurs en fonction de la qualité du réseau, en plus de permettre un contrôle manuel du réseau. Nous regroupons automatiquement les requêtes d'API depuis le SDK pour nous assurer que les données sont journalisées rapidement tout en maintenant une efficacité maximale du réseau. Enfin, la quantité de données envoyées par le client à Braze dans chaque appel d'API est extrêmement faible.

## Compatibilité du SDK {#sdk-compatibility}

Le SDK Braze est conçu pour se comporter au mieux et ne pas interférer avec les autres SDK présents dans votre application. Si vous rencontrez des difficultés qui pourraient être dues à une incompatibilité avec un autre SDK, contactez l'assistance Braze.

## Analyses par défaut et gestion de session {#default-analytics-and-session-handling}

Certaines données utilisateur sont collectées automatiquement par notre SDK, par exemple, Première application utilisée, Dernière application utilisée, Nombre total de sessions, Système d'exploitation de l'appareil, etc. Si vous suivez nos guides d'intégration pour mettre en œuvre nos SDK, vous pourrez profiter de cette [collecte de données par défaut]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection). Vérifier cette liste peut vous aider à éviter de stocker plusieurs fois les mêmes informations sur les utilisateurs. À l'exception du début et de la fin de session, toutes les autres données suivies automatiquement ne sont pas prises en compte dans votre utilisation des points de donnée.

{% alert note %}
Toutes nos fonctionnalités sont configurables, mais il est judicieux de mettre en œuvre le modèle de collecte de données par défaut.

<br>Si cela est nécessaire pour votre cas d'utilisation, vous pouvez [limiter la collecte de certaines données](#blocking-data-collection) une fois l'intégration terminée.
{% endalert %}

## Envoi et réception des données {#data-upload-and-download}

Le SDK Braze met les données en cache (sessions, événements personnalisés, etc.) et les envoie périodiquement. Les valeurs ne seront mises à jour sur le tableau de bord qu'après l'envoi des données. L'intervalle d'envoi tient compte de l'état de l'appareil et est régi par la qualité de la connexion réseau :

| Qualité de connexion réseau | Intervalle de purge des données |
|---|---|
| Excellente | 10 secondes |
| Bonne | 30 secondes |
| Mauvaise | 60 secondes |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Envoi et réception des données" }

S'il n'y a pas de connexion réseau, les données sont mises en cache localement sur l'appareil jusqu'à ce que la connexion réseau soit rétablie. Lorsque la connexion est rétablie, les données sont envoyées à Braze.

Braze envoie des données au SDK au début d'une session en fonction des segments dans lesquels l'utilisateur se trouve au moment de la session. Les nouveaux messages in-app ne seront pas mis à jour pendant la session. Cependant, les données de l'utilisateur pendant la session seront traitées en continu au fur et à mesure qu'elles seront envoyées par le client. Par exemple, un utilisateur inactif (qui a utilisé l'application pour la dernière fois il y a plus de 7 jours) recevra toujours du contenu destiné aux utilisateurs inactifs lors de sa première session de retour dans l'application.

## Blocage de la collecte des données {#blocking-data-collection}

Il est possible, bien que non recommandé, de bloquer la collecte automatique de certaines données de votre intégration SDK, ou de mettre en liste d'autorisations les processus qui le font.

Il n'est pas recommandé de bloquer la collecte de données, car la suppression des données d'analyse réduit la capacité de personnalisation et de ciblage de votre plateforme. Par exemple :

- Si vous choisissez de ne pas intégrer complètement la localisation dans l'un des SDK, vous ne pourrez pas personnaliser vos messages en fonction de la langue ou de la localisation.
- Si vous choisissez de ne pas intégrer le fuseau horaire, vous ne pourrez peut-être pas envoyer de messages dans le fuseau horaire d'un utilisateur.
- Si vous choisissez de ne pas intégrer les informations visuelles d'un appareil spécifique, le contenu du message pourrait ne pas être optimisé pour cet appareil.

Nous recommandons fortement d'intégrer pleinement les SDK pour tirer le meilleur parti des capacités de nos produits.

{% tabs %}
{% tab Web SDK %}

Vous pouvez soit simplement ne pas intégrer certaines parties du SDK, soit utiliser [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) pour un utilisateur. Cette méthode synchronisera les données enregistrées avant l'appel de `disableSDK()`, et tous les appels ultérieurs au SDK Braze pour le Web pour cette page et les chargements de page suivants seront ignorés. Si vous souhaitez reprendre la collecte de données ultérieurement, vous pouvez utiliser la méthode [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) pour reprendre la collecte des données. Pour en savoir plus, consultez notre article [Désactivation du suivi Web]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=web).

{% endtab %}
{% tab Android SDK %}

Vous pouvez utiliser [`setDeviceObjectAllowlist`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html?query=fun%20setDeviceObjectAllowlist(deviceObjectAllowlist:%20EnumSet%3CDeviceKey%3E):%20BrazeConfig.Builder) pour configurer le SDK de manière à n'envoyer qu'un sous-ensemble de clés ou de valeurs d'objets d'appareils conformément à une liste d'autorisations définie. Cette fonction doit être activée via [`setDeviceObjectAllowlistEnabled`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html?query=fun%20setDeviceObjectAllowlistEnabled(enabled:%20Boolean):%20BrazeConfig.Builder).

{% alert important %}
Si la liste d'autorisations est vide, **aucune** donnée relative à l'appareil ne sera envoyée à Braze.
{% endalert %}

{% endtab %}
{% tab Swift SDK %}

Vous pouvez attribuer un ensemble de champs éligibles à [`configuration.devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) sur votre `Braze.Configuration` pour spécifier une liste d'autorisations pour les champs de l'appareil collectés par le SDK. La liste complète des champs est définie dans [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty). Pour désactiver la collecte de tous les champs de l'appareil, définissez la valeur de cette propriété sur un ensemble vide (`[]`).

{% alert important %}
Par défaut, tous les champs sont collectés par le SDK Braze Swift. La suppression de certaines propriétés de l'appareil peut entraîner la désactivation de certaines fonctionnalités du SDK.
{% endalert %}

Pour plus de détails sur l'utilisation, reportez-vous à la rubrique [Stockage]({{site.baseurl}}/developer_guide/storage?tab=swift) dans la documentation du SDK Swift.

{% endtab %}
{% endtabs %}

## Quelle est la version du SDK que j'utilise ? {#what-version-of-the-sdk-am-i-on}

Vous pouvez utiliser le tableau de bord pour voir la version du SDK d'une application particulière en sélectionnant **Paramètres** > **Paramètres des applications**. La **version du SDK en production** indique la version la plus élevée du SDK Braze utilisée par votre application en production la plus récente pour au moins 5 % de vos utilisateurs.

![Une application nommée Swifty dans un espace de travail. La version du SDK en production est la 6.6.0.]({% image_buster /assets/img/live-sdk-version.png %}){: style="max-width:80%"}

{% alert tip %}
Si vous avez une application iOS, vous pouvez confirmer que vous utilisez le [SDK Swift]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift) au lieu de l'ancien [SDK iOS Objective-C]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview) si la **version de votre SDK en production** est égale ou supérieure à 5.0.0, qui était la première version publiée du SDK Swift.
{% endalert %}