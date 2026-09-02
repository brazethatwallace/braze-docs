{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Deaktivieren des Daten-Trackings {#disabling-data-tracking}

Um die Datenerfassung zu deaktivieren, verwenden Sie die Methode `disableSDK`. Nach dem Aufruf dieser Methode sendet das Braze SDK or Software-Development-Kit keine Daten mehr an die Braze-Server.

```javascript
Braze.disableSDK();
```

## Daten-Tracking wieder aufnehmen {#resuming-data-tracking}

Um die Datenerfassung nach dem Deaktivieren wieder aufzunehmen, verwenden Sie die Methode `enableSDK`.

```javascript
Braze.enableSDK();
```

## Daten löschen {#wiping-data}

Um alle lokal gespeicherten Braze-SDK or Software-Development-Kit-Daten auf dem Gerät zu löschen, verwenden Sie die Methode `wipeData`. Nach dem Aufruf dieser Methode ist das SDK or Software-Development-Kit deaktiviert und muss mit `enableSDK` wieder aktiviert werden.

```javascript
Braze.wipeData();
```

## Daten sofort senden {#flushing-data}

Um ein sofortiges Senden aller ausstehenden Daten an die Braze-Server anzufordern, verwenden Sie `requestImmediateDataFlush`.

```javascript
Braze.requestImmediateDataFlush();
```

## Aktivierung des Ad-Trackings festlegen {#setting-ad-tracking-enabled}

Um Braze darüber zu informieren, ob Ad-Tracking für dieses Gerät aktiviert ist, verwenden Sie die Methode `setAdTrackingEnabled`. Das SDK or Software-Development-Kit erfasst diese Daten nicht automatisch.

```javascript
Braze.setAdTrackingEnabled(true, "GOOGLE_ADVERTISING_ID");
```

Der zweite Parameter ist die Google Advertising ID und wird nur auf Android verwendet.

## Update or aktualisieren or aktualisieren der Tracking-Eigenschaft-Zulassungsliste (nur iOS) {#updating-the-tracking-property-allow-list-ios-only}

Um die Liste der für das Tracking deklarierten Datentypen zu Update or aktualisieren or aktualisieren, verwenden Sie `updateTrackingPropertyAllowList`. Auf Android hat dies keine Auswirkung.

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

Weitere Informationen finden Sie unter [Datenschutzmanifest]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=swift#swift_privacy-manifest).

## Abmeldung und Push-Deregistrierung {#logout-and-unregister-push}

Dieses Feature wird im React Native SDK or Software-Development-Kit noch nicht unterstützt.