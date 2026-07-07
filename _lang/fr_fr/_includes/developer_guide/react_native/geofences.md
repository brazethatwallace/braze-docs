{% alert important %}
Les géorepérages sont pris en charge **à la fois sur iOS et Android** dans le SDK React Native. La méthode `requestLocationInitialization` est réservée à Android et n'est pas nécessaire pour iOS. La méthode `requestGeofences` est disponible sur les deux plateformes. Par défaut, le SDK peut automatiquement demander et surveiller les géorepérages lorsque l'emplacement est disponible ; vous pouvez vous fier à cette configuration automatique ou appeler `requestGeofences` pour effectuer une demande manuellement.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Configuration des géorepérages {#setting-up-geofences}

### Étape 1 : Activer dans Braze {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Étape 2 : Effectuer la configuration Android native {#step-2-complete-native-android-setup}

Étant donné que le SDK React Native utilise le SDK Android natif de Braze, effectuez la configuration native du géorepérage Android pour votre projet. L'équivalent iOS de ces étapes est décrit dans le guide des géorepérages du SDK Swift natif ([étapes 2.2 à 3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module) ; l'étape 2.1 (Ajouter le module BrazeLocation) n'est pas nécessaire pour React Native, car BrazeLocation est déjà inclus implicitement dans le SDK Braze React Native.

1. **Mettre à jour `build.gradle` :** Ajoutez `android-sdk-location` et les services de localisation Google Play. Consultez [les géorepérages Android]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).
2. **Mettre à jour le manifeste :** Ajoutez les autorisations de localisation et le récepteur de démarrage Braze. Consultez [les géorepérages Android]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).
3. **Activer la collecte de données d'emplacement Braze :** Mettez à jour votre fichier `braze.xml`. Consultez [les géorepérages Android]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).

### Étape 3 : Effectuer la configuration iOS native {#step-3-complete-native-ios-setup}

Étant donné que le SDK React Native utilise le SDK iOS natif de Braze, effectuez la configuration native du géorepérage iOS pour votre projet en suivant les instructions du SDK Swift natif à partir de l'étape 2.2 : mettez à jour votre `Info.plist` avec les descriptions d'utilisation de la localisation (étape 2.2), et activez les géorepérages dans votre configuration Braze en incluant `automaticGeofenceRequests = true` (étape 3) ; vous pouvez également activer les rapports en arrière-plan (étape 3.1). L'étape 2.1 (Ajouter le module BrazeLocation) n'est pas nécessaire — BrazeLocation est déjà inclus implicitement dans le SDK Braze React Native. Consultez [les géorepérages iOS, étapes 2.2 à 3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module).

### Étape 4 : Demander des géorepérages depuis JavaScript {#step-4-request-geofences-from-javascript}

**Sur Android :** Une fois que l'utilisateur a accordé les autorisations de localisation, appelez `requestLocationInitialization()` pour initialiser les fonctionnalités de localisation de Braze et demander des géorepérages aux serveurs Braze. Cette méthode n'est pas prise en charge sur iOS et n'est pas requise pour iOS.

**Sur iOS :** L'équivalent consiste à activer la configuration `automaticGeofenceRequests` dans votre configuration native Swift ou Objective-C de Braze (voir étape 3). Lorsque cette option est activée, le SDK demande et surveille automatiquement les géorepérages lorsque l'emplacement est disponible ; aucun appel JavaScript équivalent à `requestLocationInitialization` n'est nécessaire.

```javascript
import Braze from '@braze/react-native-sdk';

// Android only: call this after the user grants location permission
Braze.requestLocationInitialization();
```

### Étape 5 : Demander manuellement des géorepérages (facultatif) {#step-5-manually-request-geofences-optional}

Sur iOS et Android, vous pouvez demander manuellement une mise à jour du géorepérage pour une coordonnée GPS spécifique en utilisant `requestGeofences`. Par défaut, Braze récupère automatiquement l'emplacement de l'appareil et demande des géorepérages. Pour fournir manuellement une coordonnée à la place :

1. Désactivez les demandes automatiques de géorepérage. Sur Android, définissez `com_braze_automatic_geofence_requests_enabled` sur `false` dans votre `braze.xml`. Sur iOS, définissez `automaticGeofenceRequests` sur `false` dans votre configuration Braze.
2. Appelez `requestGeofences` en indiquant la latitude et la longitude souhaitées :

```javascript
import Braze from '@braze/react-native-sdk';

Braze.requestGeofences(33.078947, -116.601356);
```

{% alert important %}
Les géorepérages ne peuvent être demandés qu'une seule fois par session, soit automatiquement par le SDK, soit manuellement avec cette méthode.
{% endalert %}