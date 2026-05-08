---
nav_title: Stockage
article_title: Stockage pour iOS
platform: iOS
page_order: 8.9
page_type: reference
description: "Cet article de référence décrit les propriétés au niveau de l'appareil capturées par le SDK Braze pour iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Stockage {#storage}

Cet article décrit les différentes propriétés au niveau de l'appareil capturées lors de l'utilisation du SDK Braze pour iOS.

## Propriétés de l'appareil {#device-properties}

Par défaut, Braze collecte les propriétés suivantes [au niveau de l'appareil](https://github.com/Appboy/appboy-ios-sdk/blob/16e893f2677af7de905b927505d4101c6fb2091d/AppboyKit/headers/AppboyKitLibrary/Appboy.h#L181) pour permettre la personnalisation des messages en fonction de l'appareil, de la langue et du fuseau horaire :

* Résolution de l'appareil
* Opérateur mobile
* Paramètres régionaux de l'appareil
* Modèle de l'appareil
* Version du système d'exploitation de l'appareil
* IDFV (facultatif avec [iOS SDK v5.7.0+](https://github.com/braze-inc/braze-swift-sdk))
* Notifications push activées
* Fuseau horaire de l'appareil
* État de l'autorisation des notifications push
* Suivi publicitaire activé

{% alert note %}
Le SDK Braze ne collecte pas automatiquement l'IDFA. Les applications peuvent éventuellement transmettre l'IDFA à Braze en implémentant notre protocole `ABKIDFADelegate`. Les applications doivent obtenir le consentement explicite de l'utilisateur final au suivi via le framework App Tracking Transparency avant de transmettre l'IDFA à Braze.
{% endalert %}

Les champs configurables de l'appareil sont définis dans l'enum [`ABKDeviceOptions`](https://github.com/Appboy/appboy-ios-sdk/blob/4390e9eac8401bccdb81b053fa54eb87b1f6fcaa/Appboy-tvOS-SDK/AppboyTVOSKit.framework/Headers/Appboy.h#L179). Pour désactiver ou spécifier le champ de l'appareil que vous souhaitez autoriser, affectez le `OR` au niveau du bit des champs souhaités à [`ABKDeviceAllowlistKey`](https://github.com/Appboy/appboy-ios-sdk/blob/fed071000722673754da288cace15c1ff8aca432/AppboyKit/include/Appboy.h#L148) dans `appboyOptions` de `startWithApiKey:inApplication:withAppboyOptions:`.

Par exemple, pour spécifier que le fuseau horaire et les paramètres régionaux doivent être autorisés, définissez :
```
appboyOptions[ABKDeviceAllowlistKey] = @(ABKDeviceOptionTimezone | ABKDeviceOptionLocale);
```

Par défaut, tous les champs sont activés. Notez que sans certaines propriétés, toutes les fonctionnalités ne fonctionneront pas correctement. Par exemple, la distribution selon le fuseau horaire local ne fonctionnera pas sans le fuseau horaire.

Pour en savoir plus sur les propriétés de l'appareil collectées automatiquement, consultez notre article sur la [collecte de données du SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/).