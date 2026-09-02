## Push-Abo-Status {#push-sub-states}

Ein „Push-Abo-Status“ in Braze identifiziert die globale Präferenz **einer Nutzer:in** für den Empfang von Push-Benachrichtigungen. Da der Abo-Status nutzerbasiert ist, ist er nicht auf eine bestimmte App begrenzt. Abo-Status werden zu hilfreichen Kennzeichnungen, wenn Sie entscheiden, welche Nutzer:innen Sie für Push-Benachrichtigungen ansprechen möchten.

{% alert note %}
Der Push-Abo-Status einer Nutzer:in gilt für das gesamte Kundenprofil or Nutzerprofil, das alle Geräte der Nutzer:in umfasst.
{% endalert %}

Die folgenden Abo-Statusoptionen sind verfügbar: `Subscribed`, `Opted-In` und `Unsubscribed`.

Standardmäßig muss der Push-Abo-Status Ihrer Nutzer:innen entweder `Subscribed` oder `Opted-In` sein und sie müssen Push-Benachrichtigungen im Vordergrund aktiviert haben, damit sie Ihre Nachrichten per Push erhalten können. Sie können diese Einstellung bei Bedarf beim Verfassen einer Nachricht außer Kraft setzen.

| Einwilligungsstatus | Beschreibung |
|---|---|
| `Subscribed` | Standard-Push-Abo-Status, wenn ein Kundenprofil or Nutzerprofil in Braze erstellt wird. |
| `Opted-In` | Eine Nutzer:in hat sich ausdrücklich für den Erhalt von Push-Benachrichtigungen entschieden. Braze setzt den Opt-in-Status einer Nutzer:in automatisch auf `Opted-In`, wenn die Nutzer:in eine Push-Aufforderung auf Betriebssystemebene akzeptiert.<br><br>Dies gilt nicht für Nutzer:innen von Android 12 oder darunter. |
| `Unsubscribed` | Eine Nutzer:in hat sich über Ihre Anwendung oder andere von Ihrer Marke angebotene Methoden explizit von Push abgemeldet. Standardmäßig richten sich Braze-Push-Campaigns nur an Nutzer:innen, die für Push `Subscribed` oder `Opted-in` sind. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push-Abo-Status" }

{% alert important %}
Braze ändert den Push-Abo-Status einer Nutzer:in nicht automatisch in `Unsubscribed`. Beachten Sie, dass wenn der Push-Abo-Status einer Nutzer:in `Unsubscribed` ist, der Filter `Foreground Push Enabled` der Nutzer:in in der Segmentierung `false` ist.
{% endalert %}

### Push-Registrierung und erreichbare Nutzer:innen {#push-registration-and-reachable-users}

Der Push-Abo-Status spiegelt die Präferenz einer Nutzer:in wider, aber ob sie im Dashboard als **erreichbar** für Push gezählt wird, hängt auch von der [Push-Registrierung]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle) ab – also davon, ob ein gültiges Vordergrund-Push-Token / Textbaustein in ihrem Profil vorhanden ist. Informationen dazu, wie Braze kanalspezifische Zählungen berechnet, finden Sie unter [Segmentgröße messen]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

- **Push-Campaigns und Canvase:** Nutzer:innen, die nicht für Push registriert sind, werden in den Zielgruppenstatistiken nicht unter **Erreichbare Nutzer:innen** für Android-Push oder iOS-Push aufgeführt, selbst wenn ihr Push-Abo-Status `Subscribed` oder `Opted-In` ist.
- **Andere Kanäle:** Dieselben Nutzer:innen können weiterhin als erreichbar für andere Kanäle gezählt werden, für die sie qualifiziert sind (zum Beispiel E-Mail oder In-App-Nachrichten).
- **Segments:** Die Segment-Zugehörigkeit richtet sich nach Ihren Filtern. Nutzer:innen ohne Push-Registrierung bleiben im Segment, es sei denn, ein Filter schließt sie aus (zum Beispiel **Foreground Push Enabled**). Die Gesamtzahl der Segment-Mitglieder kann höher sein als die Summe der Nutzer:innen, die in den Push-spezifischen Zeilen **Erreichbare Nutzer:innen** angezeigt werden.

Ein Kundenprofil or Nutzerprofil kann den Push-Abo-Status `Subscribed` anzeigen, obwohl kein Push-Token / Textbaustein zugewiesen ist. Diese Nutzer:innen werden erst dann unter **Erreichbare Nutzer:innen** für Android-Push oder iOS-Push gezählt, wenn Braze ein gültiges Token / Textbaustein erfasst.

Filterdefinitionen finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

### Push-Abo-Status Update or aktualisieren or aktualisieren {#update-push-subscription-state}

Im Folgenden finden Sie die verschiedenen Möglichkeiten, den Push-Abo-Status einer Nutzer:in zu Update or aktualisieren or aktualisieren:

#### Automatisches Opt-in (Standard) {#automatic-opt-in-default}

Standardmäßig setzt Braze den Push-Abo-Status einer Nutzer:in auf `Opted-In`, wenn sie zum ersten Mal Push-Benachrichtigungen für Ihre App autorisiert. Braze tut dies auch, wenn eine Nutzer:in die Push-Berechtigungen in den Systemeinstellungen wieder aktiviert, nachdem sie diese zuvor deaktiviert hatte.

{% tabs local %}
{% tab android %}
Um dieses Standardverhalten zu deaktivieren, fügen Sie die folgende Eigenschaft in die Datei `braze.xml` Ihres Android Studio-Projekts ein:

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
Bei iOS zeigt eine Neuinstallation den Push-Abo-Status in der Regel als **`Subscribed`** an, bis die Nutzer:in Benachrichtigungen erlaubt. Nachdem die Nutzer:in **Erlauben** in der Betriebssystem-Aufforderung ausgewählt hat, setzt Braze den Status auf **`Opted-In`**, wenn das automatische Opt-in aktiviert ist. Wenn die Nutzer:in **Nicht erlauben** auswählt und Push später in den iOS-Einstellungen aktiviert, wird der Status aktualisiert, nachdem die Nutzer:in eine Sitzung protokolliert – nicht in dem Moment, in dem sie die Einstellungen ändert.

Ab [Braze Swift SDK or Software-Development-Kit Version 7.5.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0) können Sie dieses Verhalten deaktivieren oder weiter anpassen, indem Sie die Konfiguration `optInWhenPushAuthorized` zur Datei `AppDelegate.swift` Ihres Xcode-Projekts hinzufügen:

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### SDK or Software-Development-Kit-Integration

Sie können den Abo-Status einer Nutzer:in mit dem Braze SDK or Software-Development-Kit über die Methode `setPushNotificationSubscriptionType` auf [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html) oder [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:)) Update or aktualisieren or aktualisieren. Sie können diese Methode zum Beispiel verwenden, um eine Einstellungsseite in Ihrer App zu erstellen, auf der Nutzer:innen Push-Benachrichtigungen manuell aktivieren oder deaktivieren können.

#### Representational State Transfer API

Sie können den Abo-Status einer Nutzer:in mit der Braze Representational State Transfer API Update or aktualisieren or aktualisieren, indem Sie den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) verwenden, um das [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object)-Attribut zu Update or aktualisieren or aktualisieren.

### Unterschiede zwischen Push-Aktivierung und Push-Abo-Status {#differences-between-push-enablement-and-push-subscription-status}

Push-Aktivierung bezieht sich darauf, ob eine Nutzer:in auf Betriebssystem- oder Browserebene die Berechtigung erteilt hat, Benachrichtigungen auf einem bestimmten Gerät zu empfangen. Der Push-Abo-Status ist eine Einstellung auf Braze-Ebene, die die globale Präferenz einer Nutzer:in für den Empfang von Push-Benachrichtigungen über ihr gesamtes Profil hinweg darstellt.

Wenn das automatische Opt-in aktiviert ist (Standard), aktualisiert Braze den Push-Abo-Status einer Nutzer:in auf `Opted-In`, wenn sie Push-Benachrichtigungen für Ihre App autorisiert oder die Berechtigungen in den Systemeinstellungen wieder aktiviert (zum Beispiel unter iOS, Android 13+ und unterstützten Webbrowsern). Andernfalls bleibt der Push-Abo-Status der Nutzer:in `Subscribed`, bis Sie ihn explizit über eine SDK or Software-Development-Kit-Methode oder einen Representational State Transfer-API-Aufruf ändern.

Braze ändert den Push-Abo-Status einer Nutzer:in nicht automatisch in `Unsubscribed`, wenn sie sich auf Betriebssystem-, Browser- oder App-Ebene von Benachrichtigungen abmeldet. Um den Push-Abo-Status einer Nutzer:in zu Update or aktualisieren or aktualisieren, müssen Sie ihn in Braze Update or aktualisieren or aktualisieren. Wenn eine Nutzer:in beispielsweise Push über ein In-App-Präferenzzentrum deaktiviert, Update or aktualisieren or aktualisieren Sie den Push-Abo-Status in Braze auf `Unsubscribed`. Braze aktualisiert Nutzerprofile nicht basierend auf Ihrem Präferenzzentrum. Um Abo-Status mit den In-App-Präferenzen einer Nutzer:in abzugleichen, rufen Sie die entsprechenden Methoden über das SDK or Software-Development-Kit (iOS oder Android) oder die Representational State Transfer API auf. Weitere Informationen finden Sie unter [Push-Abo-Status Update or aktualisieren or aktualisieren]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#update-push-subscription-state).

### Importierte Push-Token / Textbaustein (iOS) {#imported-push-tokens-ios}

Wenn Sie [iOS-Push-Token / Textbaustein importieren]({{site.baseurl}}/api/objects_filters/user_attributes_object#push-token-import) mit `push_token_import`, ist der Push-Abo-Status der Nutzer:in in der Regel **`Subscribed`**, bis sie eine Sitzung in Ihrer Braze-integrierten App protokolliert. Nach der ersten Sitzung kann Braze den Status auf **`Opted-In`** Update or aktualisieren or aktualisieren, wenn das [automatische Opt-in](#automatic-opt-in-default) greift (zum Beispiel wenn die Nutzer:in Push unter iOS autorisiert und `optInWhenPushAuthorized` aktiviert ist).

Überprüfen Sie die **Kontakteinstellungen** im Profil der Nutzer:in nach dem Import und erneut nach der ersten In-App-Sitzung der Nutzer:in, um den erwarteten Status zu bestätigen.

### Push-Abo-Status prüfen {#checking-push-subscription-state}

![Nutzerprofil von John Doe, dessen Push-Abo-Status auf „Subscribed“ gesetzt ist.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Sie können den Push-Abo-Status einer Nutzer:in mit Braze auf eine der folgenden Arten überprüfen:

* **Kundenprofil or Nutzerprofil:** Sie können über das Braze-Dashboard auf der Seite **[Nutzersuche]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles)** auf einzelne Nutzerprofile zugreifen. Nachdem Sie das Profil einer Nutzer:in gefunden haben (über E-Mail-Adresse, Telefonnummer oder externe Nutzer-ID), können Sie den Tab **Engagement** auswählen, um den Abo-Status der Nutzer:in anzuzeigen und manuell anzupassen.
* **Representational State Transfer-API-Export:** Mit den Endpunkten [Nutzer:innen nach Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) oder [Nutzer:innen nach Bezeichner]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) können Sie einzelne Nutzerprofile im JSON-Format exportieren. Braze gibt ein Push-Token / Textbaustein-Objekt zurück, das Push-Enablement-Informationen pro Gerät enthält.