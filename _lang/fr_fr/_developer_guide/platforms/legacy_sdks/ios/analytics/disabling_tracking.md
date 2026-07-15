---
nav_title: Désactiver le suivi SDK iOS
article_title: Désactiver le suivi SDK pour iOS
platform: iOS
page_order: 8
description: "Cet article montre comment désactiver la collecte de données pour votre application iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Désactiver la collecte de données pour iOS {#disable-data-collection-for-ios}

Pour vous conformer aux réglementations sur la confidentialité des données, l'activité de suivi des données sur le SDK iOS peut être entièrement arrêtée à l'aide de la méthode [`disableSDK`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a8d3b78a98420713d8590ed63c9172733). Cette méthode entraînera l'annulation de toutes les connexions réseau, et le SDK Braze ne transmettra aucune donnée à nos serveurs. Si vous souhaitez reprendre la collecte des données ultérieurement, vous pouvez utiliser la méthode [`requestEnableSDKOnNextAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a781078a40a3db0de64ac82dcae3b595b) pour reprendre la collecte des données.

En outre, vous pouvez utiliser la méthode [`wipeDataAndDisableForAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8d580f60ec0608cd91240a8a3aa23a3) pour effacer entièrement toutes les données côté client stockées sur l'appareil.

À moins qu'un utilisateur ne désinstalle toutes les applications d'un fournisseur sur un appareil donné, les prochaines exécutions du SDK Braze et de l'application après l'appel de `wipeDataAndDisableForAppRun()` entraîneront la réidentification de cet utilisateur par notre serveur via son identifiant d'appareil (IDFV). Afin de supprimer complètement toutes les données utilisateur, vous devez combiner un appel à `wipeDataAndDisableForAppRun` avec une demande de suppression des données sur le serveur via la [REST API]({{site.baseurl}}/developer_guide/rest_api/user_data#user-delete-endpoint) de Braze.

## SDK iOS v5.7.0+ {#ios-sdk-v570}
Pour les appareils utilisant le SDK iOS v5.7.0 ou version ultérieure, lorsque [vous désactivez la collecte IDFV]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#optional-idfv-collection---swift), l'appel de [`wipeData`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) n'entraînera pas la réidentification de cet utilisateur par notre serveur via son identifiant d'appareil (IDFV).