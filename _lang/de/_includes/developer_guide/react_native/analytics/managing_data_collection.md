{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Deaktivieren des Trackings von Daten {#disabling-data-tracking}

Um die Datenerfassung zu deaktivieren, verwenden Sie die Methode `disableSDK`. Nach dem Aufruf dieser Methode sendet das Braze SDK keine Daten mehr an Braze-Server.

```javascript
Braze.disableSDK();
```

## Datenerfassung fortsetzen {#resuming-data-tracking}

Um die Datenerfassung nach dem Deaktivieren fortzusetzen, verwenden Sie die Methode `enableSDK`.

```javascript
Braze.enableSDK();
```

## Gespeicherte Daten löschen {#wiping-data}

Um alle lokal gespeicherten Braze-SDK-Daten auf dem Gerät zu löschen, verwenden Sie die Methode `wipeData`. Nach dem Aufruf dieser Methode ist das SDK deaktiviert und muss mit `enableSDK` wieder aktiviert werden.

```javascript
Braze.wipeData();
```

## Daten sofort senden {#flushing-data}

Um ein sofortiges Senden aller ausstehenden Daten an die Braze-Server anzufordern, verwenden Sie `requestImmediateDataFlush`.

```javascript
Braze.requestImmediateDataFlush();
```

## Aktivierung des Ad-Trackings festlegen {#setting-ad-tracking-enabled}

Um Braze mitzuteilen, ob Ad-Tracking für dieses Gerät aktiviert ist, verwenden Sie die Methode `setAdTrackingEnabled`. Das SDK erfasst diese Daten nicht automatisch.

```javascript
Braze.setAdTrackingEnabled(true, "GOOGLE_ADVERTISING_ID");
```

Der zweite Parameter ist die Google Advertising ID und wird nur auf Android verwendet.

## Aktualisieren der Tracking-Eigenschaft-Zulassungsliste (nur iOS) {#updating-the-tracking-property-allow-list-ios-only}

Um die Liste der für das Tracking deklarierten Datentypen zu aktualisieren, verwenden Sie `updateTrackingPropertyAllowList`. Auf Android hat dies keine Auswirkung.

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

Weitere Informationen finden Sie unter [Datenschutzmanifest]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest).

## Abmelden und Push-Registrierung aufheben {#logout-and-unregister-push}

Dieses Feature wird vom React Native SDK noch nicht unterstützt.