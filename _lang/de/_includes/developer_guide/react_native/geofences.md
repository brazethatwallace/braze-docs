{% alert important %}
Geofences werden **sowohl auf iOS als auch auf Android** im React Native SDK or Software-Development-Kit unterstützt. Die Methode `requestLocationInitialization` ist ausschließlich für Android verfügbar und für iOS nicht erforderlich. Die Methode `requestGeofences` ist auf beiden Plattformen verfügbar. Standardmäßig kann das SDK or Software-Development-Kit Geofences automatisch anfragen und überwachen, wenn der Standort verfügbar ist. Sie können sich auf diese automatische Konfiguration verlassen oder `requestGeofences` aufrufen, um Geofences manuell anzufordern.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Einrichten von Geofences {#setting-up-geofences}

### Schritt 1: Enablement in Braze {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Schritt 2: Vollständige native Android-Einrichtung {#step-2-complete-native-android-setup}

Da das React Native SDK or Software-Development-Kit das native Braze Android SDK or Software-Development-Kit verwendet, führen Sie die native Android-Geofence-Einrichtung für Ihr Projekt durch. Die entsprechenden Schritte für iOS werden im nativen Swift-SDK or Software-Development-Kit-Leitfaden zu Geofences ([Schritte 2.2 bis 3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module)) behandelt. Schritt 2.1 (Hinzufügen des BrazeLocation-Moduls) ist für React Native nicht erforderlich, da BrazeLocation bereits implizit im Braze React Native SDK or Software-Development-Kit enthalten ist.

1. **`build.gradle` Update or aktualisieren or aktualisieren:** Fügen Sie `android-sdk-location` und die Standortdienste der Google-Play-Dienste hinzu. Siehe [Android-Geofences]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).
2. **Manifest Update or aktualisieren or aktualisieren:** Fügen Sie Standortberechtigungen und den Braze-Boot-Empfänger hinzu. Siehe [Android-Geofences]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).
3. **Standortdatenerfassung von Braze aktivieren:** Update or aktualisieren or aktualisieren Sie Ihre `braze.xml`-Datei. Siehe [Android-Geofences]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).

### Schritt 3: Vollständige native iOS-Einrichtung {#step-3-complete-native-ios-setup}

Da das React Native SDK or Software-Development-Kit das native Braze iOS SDK or Software-Development-Kit verwendet, führen Sie die native iOS-Geofence-Einrichtung für Ihr Projekt durch, indem Sie die Anweisungen für das native Swift SDK or Software-Development-Kit ab Schritt 2.2 befolgen: Update or aktualisieren or aktualisieren Sie Ihre `Info.plist` mit Beschreibungen zur Standortnutzung (Schritt 2.2) und aktivieren Sie Geofences in Ihrer Braze-Konfiguration einschließlich `automaticGeofenceRequests = true` (Schritt 3); optional können Sie die Hintergrundberichterstattung aktivieren (Schritt 3.1). Schritt 2.1 (Hinzufügen des BrazeLocation-Moduls) ist nicht erforderlich – BrazeLocation ist bereits implizit im Braze React Native SDK or Software-Development-Kit enthalten. Siehe [iOS-Geofences, Schritte 2.2 bis 3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module).

### Schritt 4: Geofences über JavaScript anfordern {#step-4-request-geofences-from-javascript}

**Auf Android:** Nachdem die Nutzer:innen die Standortberechtigungen erteilt haben, rufen Sie `requestLocationInitialization()` auf, um die Standort-Features von Braze zu initialisieren und Geofences von den Braze-Servern anzufordern. Diese Methode wird unter iOS nicht unterstützt und ist für iOS nicht erforderlich.

**Auf iOS:** Das Äquivalent besteht darin, die Konfiguration `automaticGeofenceRequests` in Ihrer nativen Swift- oder Objective-C-Braze-Konfiguration zu aktivieren (siehe [Schritt 3](#schritt-3-vollständige-native-ios-einrichtung)). Wenn diese Funktion aktiviert ist, fordert das SDK or Software-Development-Kit automatisch Geofences an und überwacht sie, sobald der Standort verfügbar ist. Ein JavaScript-Aufruf, der `requestLocationInitialization` entspricht, ist nicht erforderlich.

```javascript
import Braze from '@braze/react-native-sdk';

// Android only: call this after the user grants location permission
Braze.requestLocationInitialization();
```

### Schritt 5: Geofences manuell anfordern (optional) {#step-5-manually-request-geofences-optional}

Sowohl auf iOS als auch auf Android können Sie manuell ein Geofence-Update or aktualisieren für eine bestimmte GPS-Koordinate anfordern, indem Sie `requestGeofences` verwenden. Standardmäßig ruft Braze automatisch den Standort des Geräts ab und fordert Geofences an. Um stattdessen manuell eine Koordinate anzugeben:

1. Deaktivieren Sie automatische Geofence-Anfragen. Setzen Sie auf Android `com_braze_automatic_geofence_requests_enabled` in Ihrer `braze.xml` auf `false`. Setzen Sie auf iOS `automaticGeofenceRequests` in Ihrer Braze-Konfiguration auf `false`.
2. Rufen Sie `requestGeofences` mit den gewünschten Breiten- und Längengraden auf:

```javascript
import Braze from '@braze/react-native-sdk';

Braze.requestGeofences(33.078947, -116.601356);
```

{% alert important %}
Geofences können nur einmal pro Sitzung angefordert werden – entweder automatisch durch das SDK or Software-Development-Kit oder manuell mit dieser Methode.
{% endalert %}