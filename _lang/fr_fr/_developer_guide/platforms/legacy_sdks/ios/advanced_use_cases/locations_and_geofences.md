---
nav_title: Emplacements et géorepérage
article_title: Emplacements et géorepérage pour iOS
platform: iOS
page_order: 6
description: "Cet article de référence explique comment mettre en œuvre les emplacements et le géorepérage dans votre application iOS."
tool:
  - Location

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Emplacements et géorepérage {#locations-and-geofences}

Pour prendre en charge les géorepérages pour iOS :

1. Votre intégration doit prendre en charge les notifications push en arrière-plan.
2. Les géorepérages Braze [doivent être activés]({{site.baseurl}}/developer_guide/geofences?sdktab=swift) via le SDK, soit implicitement en activant la collecte des données de localisation, soit explicitement en activant la collecte des géorepérages. Ils ne sont pas activés par défaut.

{% alert important %}
Depuis iOS 14, les géorepérages ne fonctionnent pas de manière fiable pour les utilisateurs qui choisissent de donner leur autorisation de localisation approximative.
{% endalert %}

## Étape 1 : Activer les notifications push en arrière-plan {#step-1-enable-background-push}

Pour exploiter pleinement notre stratégie de synchronisation des géorepérages, vous devez activer les [notifications push en arrière-plan]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications#use-silent-push-notifications-to-trigger-background-work) en plus de compléter l'intégration push standard.

## Étape 2 : Activer les géorepérages {#step-2-enable-geofences}

Par défaut, les géorepérages sont activés en fonction de l'activation ou non de la collecte automatique de localisation. Vous pouvez activer les géorepérages à l'aide du fichier `Info.plist`. Ajoutez le dictionnaire `Braze` à votre fichier `Info.plist`. À l'intérieur du dictionnaire `Braze`, ajoutez la sous-entrée booléenne `EnableGeofences` et définissez la valeur sur `YES`. Notez qu'avant la version v4.0.2 du SDK iOS de Braze, la clé de dictionnaire `Appboy` doit être utilisée à la place de `Braze`.

Vous pouvez également activer les géorepérages au démarrage de l'application en utilisant la méthode [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). Dans le dictionnaire `appboyOptions`, définissez `ABKEnableGeofencesKey` sur `YES`. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableGeofencesKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableGeofencesKey : true ])
```

{% endtab %}
{% endtabs %}

## Étape 3 : Vérifier les notifications push en arrière-plan de Braze {#step-3-check-for-braze-background-push}

Braze synchronise les géorepérages sur les appareils à l'aide de notifications push en arrière-plan. Consultez l'article sur la [personnalisation iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push) pour vous assurer que votre application n'effectue aucune action indésirable lors de la réception des notifications de synchronisation des géorepérages de Braze.

## Étape 4 : Ajouter NSLocationAlwaysUsageDescription à votre Info.plist {#step-4-add-nslocationalwaysusagedescription-to-your-infoplist}

Ajoutez les clés `NSLocationAlwaysUsageDescription` et `NSLocationAlwaysAndWhenInUseUsageDescription` à votre fichier `info.plist` avec une valeur de type `String` contenant une description expliquant pourquoi votre application a besoin de suivre la localisation. Ces deux clés sont requises par iOS 11 ou version ultérieure.
Cette description s'affichera lorsque l'invite système de localisation demandera l'autorisation, et elle devrait expliquer clairement les avantages du suivi de localisation à vos utilisateurs.

## Étape 5 : Demander l'autorisation de l'utilisateur {#step-5-request-authorization-from-the-user}

La fonctionnalité de géorepérage n'est opérationnelle que lorsque l'autorisation de localisation `Always` est accordée.

Pour demander l'autorisation de localisation `Always`, utilisez le code suivant :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```

{% endtab %}
{% tab swift %}

```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```

{% endtab %}
{% endtabs %}

## Étape 6 : Activer les géorepérages sur le tableau de bord {#step-6-enable-geofences-on-the-dashboard}

iOS n'autorise le stockage que de 20 géorepérages maximum pour une application donnée. L'utilisation des emplacements consommera une partie de ces 20 emplacements de géorepérage disponibles. Pour éviter toute perturbation accidentelle ou indésirable d'autres fonctionnalités liées au géorepérage dans votre application, les géorepérages de localisation doivent être activés individuellement pour chaque application sur le tableau de bord.

Pour que les emplacements fonctionnent correctement, vous devez également vérifier que votre application n'utilise pas tous les emplacements de géorepérage disponibles.

### Activer les géorepérages depuis la page des emplacements : {#enable-geofences-from-the-locations-page}

![Les options de géorepérage sur la page des emplacements de Braze.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Activer les géorepérages depuis la page des paramètres : {#enable-geofences-from-the-settings-page}

![La case à cocher de géorepérage sur les pages de paramètres de Braze.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## Désactiver les requêtes automatiques de géorepérage {#disabling-automatic-geofence-requests}

À partir de la version 3.21.3 du SDK iOS, vous pouvez désactiver la demande automatique de géorepérages. Pour ce faire, utilisez le fichier `Info.plist`. Ajoutez le dictionnaire `Braze` à votre fichier `Info.plist`. À l'intérieur du dictionnaire `Braze`, ajoutez la sous-entrée booléenne `DisableAutomaticGeofenceRequests` et définissez la valeur sur `YES`.

Vous pouvez également désactiver les requêtes automatiques de géorepérage au démarrage de l'application via la méthode [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). Dans le dictionnaire `appboyOptions`, définissez `ABKDisableAutomaticGeofenceRequestsKey` sur `YES`. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKDisableAutomaticGeofenceRequestsKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKDisableAutomaticGeofenceRequestsKey : true ])
```

{% endtab %}
{% endtabs %}

Si vous choisissez d'utiliser cette option, vous devrez demander manuellement les géorepérages pour que la fonctionnalité fonctionne.

## Demander manuellement des géorepérages {#manually-requesting-geofences}

Lorsque le SDK Braze demande au backend les géorepérages à surveiller, il transmet la localisation actuelle de l'utilisateur et reçoit les géorepérages considérés comme les plus pertinents en fonction de la localisation transmise. Il existe une limite de débit d'une actualisation de géorepérage par session.

Pour contrôler la localisation que le SDK transmet afin de recevoir les géorepérages les plus pertinents, à partir de la version 3.21.3 du SDK iOS, vous pouvez demander manuellement des géorepérages en fournissant la latitude et la longitude d'un emplacement. Il est recommandé de désactiver les demandes automatiques de géorepérage lorsque vous utilisez cette méthode. Pour ce faire, utilisez le code suivant :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] requestGeofencesWithLongitude:longitude
                                              latitude:latitude];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestGeofences(withLongitude: longitude, latitude: latitude)
```

{% endtab %}
{% endtabs %}