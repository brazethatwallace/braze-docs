## Push-Abo-Status {#push-sub-states}

Ein „Push-Abo-Status“ in Braze identifiziert die globale Präferenz **einer Nutzer:in** für den Empfang von Push-Benachrichtigungen. Da der Abo-Status nutzerbasiert ist, ist er nicht auf eine bestimmte App begrenzt. Abo-Status werden zu hilfreichen Kennzeichnungen, wenn Sie entscheiden, welche Nutzer:innen Sie für Push-Benachrichtigungen ansprechen möchten.

{% alert note %}
Der Push-Abo-Status einer Nutzer:in gilt für das gesamte Nutzerprofil, das alle Geräte der Nutzer:in umfasst.
{% endalert %}

Die folgenden Abo-Statusoptionen sind verfügbar: `Subscribed`, `Opted-In` und `Unsubscribed`.

Standardmäßig muss der Push-Abo-Status Ihrer Nutzer:innen entweder `Subscribed` oder `Opted-In` sein und sie müssen Push-Benachrichtigungen im Vordergrund aktiviert haben, damit sie Ihre Nachrichten per Push erhalten können. Sie können diese Einstellung bei Bedarf beim Verfassen einer Nachricht außer Kraft setzen.

| Einwilligungsstatus | Beschreibung |
|---|---|
| `Subscribed` | Standard-Push-Abo-Status, wenn ein Nutzerprofil in Braze erstellt wird. |
| `Opted-In` | Eine Nutzer:in hat sich ausdrücklich für den Erhalt von Push-Benachrichtigungen entschieden. Braze setzt den Opt-in-Status einer Nutzer:in automatisch auf `Opted-In`, wenn die Nutzer:in eine Push-Aufforderung auf Betriebssystemebene akzeptiert.<br><br>Dies gilt nicht für Nutzer:innen von Android 12 oder darunter. |
| `Unsubscribed` | Eine Nutzer:in hat sich über Ihre Anwendung oder andere von Ihrer Marke angebotene Methoden explizit von Push abgemeldet. Standardmäßig richten sich Braze-Push-Campaigns nur an Nutzer:innen, die für Push `Subscribed` oder `Opted-in` sind. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push subscription states #push-sub-states" }

{% alert important %}
Braze ändert den Push-Abo-Status einer Nutzer:in nicht automatisch in `Unsubscribed`. Beachten Sie, dass wenn der Push-Abo-Status einer Nutzer:in `Unsubscribed` ist, der Filter `Foreground Push Enabled` der Nutzer:in in der Segmentierung `false` ist.
{% endalert %}

### Push-Abo-Status aktualisieren {#update-push-subscription-state}

Im Folgenden finden Sie die verschiedenen Möglichkeiten, den Push-Abo-Status einer Nutzer:in zu aktualisieren:

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
Ab [Braze Swift SDK Version 7.5.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0) können Sie dieses Verhalten deaktivieren oder weiter anpassen, indem Sie die Konfiguration `optInWhenPushAuthorized` zur Datei `AppDelegate.swift` Ihres Xcode-Projekts hinzufügen:

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### SDK-Integration

Sie können den Abo-Status einer Nutzer:in mit dem Braze SDK über die Methode `setPushNotificationSubscriptionType` auf [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html) oder [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:)) aktualisieren. Sie können diese Methode zum Beispiel verwenden, um eine Einstellungsseite in Ihrer App zu erstellen, auf der Nutzer:innen Push-Benachrichtigungen manuell aktivieren oder deaktivieren können.

#### REST API

Sie können den Abo-Status einer Nutzer:in mit der Braze REST API aktualisieren, indem Sie den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) verwenden, um das [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object/)-Attribut zu aktualisieren.

### Unterschiede zwischen Push-Aktivierung und Push-Abo-Status {#differences-between-push-enablement-and-push-subscription-status}

Push-Aktivierung bezieht sich darauf, ob eine Nutzer:in auf Betriebssystem- oder Browserebene die Berechtigung erteilt hat, Benachrichtigungen auf einem bestimmten Gerät zu empfangen. Der Push-Abo-Status ist eine Einstellung auf Braze-Ebene, die die globale Präferenz einer Nutzer:in für den Empfang von Push-Benachrichtigungen über das gesamte Profil hinweg darstellt.

Wenn das automatische Opt-in aktiviert ist (Standard), aktualisiert Braze den Push-Abo-Status einer Nutzer:in auf `Opted-In`, wenn sie Push-Benachrichtigungen für Ihre App autorisiert oder die Berechtigungen in den Systemeinstellungen wieder aktiviert (zum Beispiel unter iOS, Android 13+ und unterstützten Webbrowsern). Andernfalls bleibt der Push-Abo-Status der Nutzer:in `Subscribed`, bis Sie ihn explizit über eine SDK-Methode oder einen REST API-Aufruf ändern.

Braze ändert den Push-Abo-Status einer Nutzer:in nicht automatisch in `Unsubscribed`, wenn sie Benachrichtigungen auf Betriebssystem-, Browser- oder App-Ebene deaktiviert. Um den Push-Abo-Status einer Nutzer:in zu aktualisieren, müssen Sie ihn in Braze aktualisieren. Wenn eine Nutzer:in beispielsweise Push über ein In-App-Präferenzzentrum deaktiviert, aktualisieren Sie den Push-Abo-Status in Braze auf `Unsubscribed`. Braze aktualisiert Nutzerprofile nicht basierend auf Ihrem Präferenzzentrum. Um Abo-Status mit den In-App-Präferenzen einer Nutzer:in abzugleichen, rufen Sie die entsprechenden Methoden über das [SDK]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/#sdk-integration) (iOS oder Android) oder die [REST API]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/#rest-api) auf.

### Push-Abo-Status prüfen {#checking-push-subscription-state}

![Nutzerprofil von John Doe, dessen Push-Abo-Status auf „Subscribed“ gesetzt ist.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Sie können den Push-Abo-Status einer Nutzer:in mit Braze auf eine der folgenden Arten überprüfen:

* **Nutzerprofil:** Sie können über das Braze-Dashboard auf der Seite **[Nutzersuche]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)** auf einzelne Nutzerprofile zugreifen. Nachdem Sie das Profil einer Nutzer:in gefunden haben (über E-Mail-Adresse, Telefonnummer oder externe Nutzer-ID), können Sie den Tab **Engagement** auswählen, um den Abo-Status der Nutzer:in anzuzeigen und manuell anzupassen.
* **REST API-Export:** Mit den Endpunkten [Nutzer:innen nach Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) oder [Nutzer:innen nach Bezeichner]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) können Sie einzelne Nutzerprofile im JSON-Format exportieren. Braze gibt ein Push-Token-Objekt zurück, das Push-Enablement-Informationen pro Gerät enthält.