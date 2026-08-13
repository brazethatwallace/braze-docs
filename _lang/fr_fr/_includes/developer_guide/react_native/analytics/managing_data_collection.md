{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Désactivation du suivi des données {#disabling-data-tracking}

Pour désactiver la collecte de données, utilisez la méthode `disableSDK`. Après l'appel de cette méthode, le SDK Braze cesse d'envoyer des données aux serveurs Braze.

```javascript
Braze.disableSDK();
```

## Reprise du suivi des données {#resuming-data-tracking}

Pour reprendre la collecte de données après l'avoir désactivée, utilisez la méthode `enableSDK`.

```javascript
Braze.enableSDK();
```

## Effacer les données {#wiping-data}

Pour supprimer toutes les données du SDK Braze stockées localement sur l'appareil, utilisez la méthode `wipeData`. Après avoir appelé cette méthode, le SDK est désactivé et doit être réactivé avec `enableSDK`.

```javascript
Braze.wipeData();
```

## Envoi immédiat des données {#flushing-data}

Pour demander un envoi immédiat de toutes les données en attente vers les serveurs Braze, utilisez `requestImmediateDataFlush`.

```javascript
Braze.requestImmediateDataFlush();
```

## Définition de l'activation du suivi publicitaire {#setting-ad-tracking-enabled}

Pour indiquer à Braze si le suivi publicitaire est activé pour cet appareil, utilisez la méthode `setAdTrackingEnabled`. Le SDK ne collecte pas automatiquement ces données.

```javascript
Braze.setAdTrackingEnabled(true, "GOOGLE_ADVERTISING_ID");
```

Le second paramètre est l'ID publicitaire Google et n'est utilisé que sur Android.

## Mise à jour de la liste d'autorisation des propriétés de suivi (iOS uniquement) {#updating-the-tracking-property-allow-list-ios-only}

Pour mettre à jour la liste des types de données déclarés pour le suivi, utilisez `updateTrackingPropertyAllowList`. Cette méthode est sans effet sur Android.

```javascript
Braze.updateTrackingPropertyAllowList({
  adding: [Braze.TrackingProperty.EMAIL, Braze.TrackingProperty.FIRST_NAME],
  removing: [],
  addingCustomEvents: ["my_custom_event"],
  removingCustomEvents: [],
  addingCustomAttributes: ["my_custom_attribute"],
  removingCustomAttributes: []
});
```

Pour plus d'informations, consultez [Manifeste de confidentialité]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest).

## Déconnexion et désinscription des notifications push {#logout-and-unregister-push}

Cette fonctionnalité n'est pas encore prise en charge par le SDK React Native.