---
nav_title: Aperçu du SDK
article_title: Présentation du SDK pour les développeurs
description: "Cet article de référence d'onboarding fournit un aperçu technique du SDK Braze pour les développeurs. Il aborde les analyses par défaut suivies par le SDK."
page_order: 0
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}Aperçu du SDK pour les développeurs

> Avant de commencer à intégrer les SDK Braze, vous vous demandez peut-être exactement ce que vous concevez et intégrez. Vous pourriez être curieux de savoir comment personnaliser davantage le SDK pour mieux répondre à vos besoins. Cet article peut vous aider à répondre à toutes vos questions concernant le SDK.

Vous êtes marketeur et cherchez un aperçu de base du SDK ? Consultez plutôt notre [présentation pour les marketeurs]({{site.baseurl}}/user_guide/get_started/sdk_overview).

Le SDK Braze en bref :
* Collecte et synchronise les données de l'utilisateur dans un profil utilisateur consolidé
* Recueille automatiquement les données de session, les informations sur l'appareil et les jetons de notification push
* Capture les données d'engagement marketing et les données personnalisées spécifiques à votre entreprise
* Alimente les canaux de communication de notifications push, de messages in-app et de Content Card

Regardez la vidéo suivante pour une brève introduction aux bases de l'intégration du SDK Braze et à ses fonctionnalités principales.

{% multi_lang_include video.html id="il152jayp0" source="wistia" %}

## Performance de l'application

Braze ne devrait avoir aucun impact négatif sur les performances de votre application.

Les SDK Braze ont une empreinte très réduite. Nous ajustons automatiquement la fréquence d'envoi des données utilisateur en fonction de la qualité du réseau, en plus de permettre un contrôle manuel du réseau. Nous regroupons automatiquement les requêtes API du SDK pour garantir que les données sont enregistrées rapidement tout en maintenant une efficacité réseau maximale. Enfin, la quantité de données envoyées du client vers Braze dans chaque appel API est extrêmement faible.

Le SDK Braze est conçu pour être très bien intégré et ne pas interférer avec les autres SDK présents dans votre application. Si vous rencontrez des problèmes que vous pensez être liés à une incompatibilité avec un autre SDK, contactez le support Braze.

## Analyse par défaut et gestion des sessions

Certaines données utilisateur sont collectées automatiquement par notre SDK — par exemple, première utilisation de l'application, dernière utilisation de l'application, nombre total de sessions, système d'exploitation de l'appareil, etc. Si vous suivez nos guides d'intégration pour implémenter nos SDK, vous pourrez tirer parti de cette [collecte de données par défaut]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection). Consulter cette liste peut vous aider à éviter de stocker les mêmes informations sur les utilisateurs en double. À l'exception du début et de la fin de session, toutes les autres données suivies automatiquement ne sont pas comptabilisées dans votre consommation de points de donnée.

{% alert note %}
Toutes nos fonctionnalités sont configurables, mais il est recommandé d'implémenter intégralement le modèle de collecte de données par défaut.

<br>Si nécessaire pour votre cas d'usage, vous pouvez [limiter la collecte de certaines données](#blocking-data-collection) une fois l'intégration terminée.
{% endalert %}

## Chargement et téléchargement des données

Le SDK Braze met en cache les données (sessions, événements personnalisés, etc.) et les charge périodiquement. Les valeurs ne seront mises à jour sur le tableau de bord qu'une fois les données chargées. L'intervalle de chargement prend en compte l'état de l'appareil et dépend de la qualité de la connexion réseau :

|Qualité de la connexion réseau |    Intervalle d'envoi des données|
|---|---|
|Excellente    |10 secondes|
|Bonne    |30 secondes|
|Faible    |60 secondes|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Chargement et téléchargement des données" }

En l'absence de connexion réseau, les données sont mises en cache localement sur l'appareil jusqu'à ce que la connexion soit rétablie. Une fois la connexion rétablie, les données sont chargées vers Braze.

Braze envoie des données au SDK au début d'une session en fonction des Segments auxquels l'utilisateur appartient au moment de la session. Les nouveaux messages in-app ne seront pas mis à jour pendant la session. Cependant, les données utilisateur collectées pendant la session continuent d'être traitées au fur et à mesure qu'elles sont envoyées par le client. Par exemple, un utilisateur inactif (qui n'a pas utilisé l'application depuis plus de 7 jours) recevra tout de même du contenu ciblant les utilisateurs inactifs dès sa première session de retour dans l'application.

## Bloquer la collecte de données

Il est possible (mais pas recommandé) de bloquer la collecte automatique de certaines données provenant de votre intégration SDK, ou de mettre en liste autorisée les processus qui le font.

Bloquer la collecte de données n'est pas recommandé car la suppression de données analytiques réduit la capacité de votre plateforme en matière de personnalisation et de ciblage. Par exemple :

- Si vous choisissez de ne pas intégrer complètement la localisation sur l'un des SDK, vous ne pourrez pas personnaliser vos messages en fonction de la langue ou de l'emplacement.
- Si vous choisissez de ne pas intégrer le fuseau horaire, vous pourriez ne pas être en mesure d'envoyer des messages dans le fuseau horaire de l'utilisateur.
- Si vous choisissez de ne pas intégrer certaines informations visuelles spécifiques à l'appareil, le contenu des messages pourrait ne pas être optimisé pour cet appareil.

Nous recommandons vivement d'intégrer complètement les SDK pour tirer pleinement parti des capacités de notre produit.

{% tabs %}
{% tab SDK Web %}

Vous pouvez simplement ne pas intégrer certaines parties du SDK, ou utiliser [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) pour un utilisateur. Cette méthode synchronisera les données enregistrées avant l'appel de `disableSDK()`, et tous les appels ultérieurs au SDK Web de Braze pour cette page et les chargements de pages futurs seront ignorés. Si vous souhaitez reprendre la collecte de données ultérieurement, vous pouvez utiliser la méthode [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) pour reprendre la collecte de données. Vous pouvez en savoir plus à ce sujet dans notre article [Désactiver le suivi Web]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=web).

{% endtab %}
{% tab SDK Android %}

Vous pouvez utiliser [`setDeviceObjectAllowlist`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html?query=fun%20setDeviceObjectAllowlist(deviceObjectAllowlist:%20EnumSet%3CDeviceKey%3E):%20BrazeConfig.Builder) pour configurer le SDK afin qu'il n'envoie qu'un sous-ensemble des clés ou valeurs de l'objet appareil conformément à une liste autorisée définie. Cela doit être activé via [`setDeviceObjectAllowlistEnabled`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html?query=fun%20setDeviceObjectAllowlistEnabled(enabled:%20Boolean):%20BrazeConfig.Builder).

{% alert important %}
Une liste autorisée vide entraînera l'envoi d'**aucune** donnée d'appareil à Braze.
{% endalert %}

{% endtab %}
{% tab SDK Swift %}

Vous pouvez attribuer un ensemble de champs éligibles à [`configuration.devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) sur votre `Braze.Configuration` pour spécifier une liste autorisée des champs d'appareil collectés par le SDK. La liste complète des champs est définie dans [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty). Pour désactiver la collecte de tous les champs d'appareil, définissez la valeur de cette propriété sur un ensemble vide (`[]`).

{% alert important %}
Par défaut, tous les champs sont collectés par le SDK Swift de Braze. La suppression de certaines propriétés d'appareil peut désactiver des fonctionnalités du SDK.
{% endalert %}

Pour plus de détails sur l'utilisation, consultez [Stockage]({{site.baseurl}}/developer_guide/storage?tab=swift) dans la documentation du SDK Swift.

{% endtab %}
{% endtabs %}

## Quelle version du SDK est-ce que j'utilise ?

Vous pouvez utiliser le tableau de bord pour consulter la version du SDK d'une application spécifique en accédant à **Paramètres > Paramètres de l'application**. La **version du SDK en direct or en ligne/en production/instantané** indique la version la plus élevée du SDK Braze utilisée par votre application en direct or en ligne/en production/instantané la plus récente pour au moins 5 % de vos utilisateurs.

![Une application nommée Swifty dans un espace de travail. La version du SDK en direct est 6.6.0.]({% image_buster /assets/img/live-sdk-version.png %}){: style="max-width:80%"}

{% alert tip %}
Si vous disposez d'une application iOS, vous pouvez vérifier que vous utilisez le [SDK Swift]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift) plutôt que l'ancien [SDK iOS Objective-C]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview) si votre **version du SDK en direct or en ligne/en production/instantané** est égale ou supérieure à 5.0.0, qui était la première version publiée du SDK Swift.
{% endalert %}