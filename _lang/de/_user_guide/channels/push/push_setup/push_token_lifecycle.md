---
nav_title: "Lebenszyklus von Push-Token / Textbaustein"
article_title: "Lebenszyklus von Push-Token / Textbaustein"
page_order: 1
page_type: reference
description: "Dieser Referenzartikel erläutert, was es bedeutet, für Push registriert zu sein, und wie Braze Push-Nachrichten sendet und mit Push-Token / Textbaustein sowie der Push-Registrierung umgeht."
channel:
 - push

---

# Lebenszyklus von Push-Token / Textbaustein {#push-token-lifecycle}

> Dieser Artikel beschreibt den Prozess, durch den Nutzer:innen ein Push-Token / Textbaustein zugewiesen bekommen, und wie Braze Push-Nachrichten an Ihre Nutzer:innen sendet.

## Über Push-Token / Textbaustein {#push-tokens}

Wenn eine App Push-Berechtigungen von einem Gerät anfordert, generiert der Push-Dienstanbieter des Geräts ein Push-Token / Textbaustein für diese App. Jede App erhält ihr eigenes eindeutiges, anonymes Push-Token / Textbaustein, das das Gerät und die aktuelle App-Instanz beim Senden einer Push-Benachrichtigung identifiziert.

Beachten Sie, dass Push-Token / Textbaustein keine statischen Bezeichner sind, die ewig bestehen&#8212;sie können aktualisiert werden und sie können [ablaufen](#push-token-expire).

{% alert tip %}
Plattformspezifische Details finden Sie unter [Push-Token / Textbaustein-Registrierung](#push-token-registration).
{% endalert %}

### Vordergrund- vs. Hintergrund-Push {#foreground-vs-background}

Push-Token / Textbaustein werden sowohl für Vordergrund- als auch für Hintergrund-Push-Benachrichtigungen verwendet.

| Typ | Opt-in erforderlich? | Beschreibung |
|------------------|------------------|--------------------------------------------------------------------------------------------------------------|
| Vordergrund-Push | Ja | Eine Benachrichtigung wird sichtbar angezeigt, während die App im Vordergrund ist. |
| Hintergrund-Push | Nein | Eine Benachrichtigung wird im Hintergrund still zugestellt, ohne angezeigt zu werden. Wird häufig für Funktionen wie Uninstall-Tracking verwendet. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Vordergrund- vs. Hintergrund-Push" }

Wenn Nutzer:innen Push-Benachrichtigungen für Ihre App aktivieren, gelten sie als „push-registriert“, was bedeutet, dass sie mit dem Segmentierungsfilter `Foreground Push Enabled for App` in Braze angesprochen werden können.

{% alert note %}
Dies unterscheidet sich vom Segmentierungsfilter `Foreground Push Enabled`, der Nutzer:innen identifiziert, die Push für mindestens eine Ihrer Apps aktiviert haben – nicht für eine bestimmte App. Weitere Informationen finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#foreground-push-enabled).
{% endalert %}

### Mehrere Nutzer:innen auf einem Gerät {#multiple-users-on-a-device}

Push-Token / Textbaustein sind sowohl für das Gerät als auch für die App eindeutig, was bedeutet, dass Push-Token / Textbaustein nicht verwendet werden können, um bestimmte Nutzer:innen anzusprechen, wenn mehrere Nutzer:innen dasselbe Gerät verwenden.

Angenommen, Sie haben zwei Nutzer:innen: Charlie und Kim. Wenn Charlie Push-Benachrichtigungen für Ihre App auf seinem Telefon aktiviert hat und Kim Charlies Telefon nutzt, um sich aus Charlies Profil abzumelden und sich in ihr eigenes einzuloggen, wird das Push-Token / Textbaustein Kims Profil zugewiesen. Das Push-Token / Textbaustein bleibt dann Kims Profil auf diesem Gerät zugewiesen, bis sie sich abmeldet und Charlie sich wieder anmeldet.

Eine App oder Website kann nur ein Push-Abo pro Gerät haben. Wenn sich also Nutzer:innen von einem Gerät oder einer Website abmelden und neue Nutzer:innen sich anmelden, wird das Push-Token / Textbaustein den neuen Nutzer:innen zugewiesen. Dies wird im Kundenprofil im Abschnitt **Contact Settings** auf dem Tab **Engagement** angezeigt:

![Push-Token-Changelog auf dem Tab „Engagement“ eines Nutzerprofils, der anzeigt, wann das Push-Token zu anderen Nutzer:innen verschoben wurde und um welches Token es sich handelt.]({% image_buster /assets/img/push_token_changelog.png %})

Da es für Push-Anbieter (APNs/FCM) keine Möglichkeit gibt, zwischen mehreren Nutzer:innen auf einem Gerät zu unterscheiden, übergeben wir das Push-Token / Textbaustein an die zuletzt angemeldeten Nutzer:innen, um zu bestimmen, welche Nutzer:innen auf dem Gerät für Push angesprochen werden sollen.

{% alert tip %}
Wenn Sie eine Fehlermeldung unter **Contact Settings** > **Push Changelog** sehen, finden Sie unter [Häufige Push-Fehlermeldungen]({{site.baseurl}}/user_guide/channels/push/push_error_codes) Erklärungen und nächste Schritte.
{% endalert %}

## Push-Token / Textbaustein-Registrierung {#push-token-registration}

Jede Geräteplattform handhabt die Push-Token / Textbaustein-registrieren unterschiedlich. Plattformspezifische Details finden Sie im Folgenden:

{% tabs local %}
{% tab Web %}
Sie müssen ein explizites Opt-in von Nutzer:innen über den nativen Browser-Berechtigungsdialog anfordern. Ein Token / Textbaustein wird nach dem Opt-in der Nutzer:innen empfangen. Anders als bei iOS und Android, wo Ihre App die Berechtigungsabfrage jederzeit anzeigen kann, zeigen einige moderne Browser die Abfrage nur an, wenn sie durch eine „Nutzeraktion“ (Mausklick oder Tastendruck) ausgelöst wird. Wenn Ihre Website versucht, die Push-Benachrichtigungsberechtigung beim Laden der Seite anzufordern, wird dies wahrscheinlich vom Browser ignoriert oder unterdrückt.
{% endtab %}

{% tab Android %}
Wenn Ihre App installiert wird, wird automatisch ein Push-Token / Textbaustein für Ihre App generiert&#8212;es kann jedoch nur für [Hintergrund-Push-Benachrichtigungen](#foreground-vs-background) verwendet werden, bis die Nutzer:innen explizit zustimmen. Zusätzlich wird die Registrierung je nach Android-Version unterschiedlich gehandhabt:

| Version | Details |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Android 13** | Die Push-Berechtigung muss von den Nutzer:innen angefordert und gewährt werden. Ihre App kann die Berechtigung manuell anfordern, oder Nutzer:innen werden automatisch aufgefordert, nachdem ein [Benachrichtigungskanal](https://developer.android.com/reference/android/app/NotificationChannel) erstellt wurde. |
| **Android 12 und früher** | Alle Nutzer:innen gelten nach ihrer ersten Sitzung als `Subscribed`. Braze fordert zu diesem Zeitpunkt automatisch ein Push-Token / Textbaustein an, wodurch die Nutzer:innen mit einem gültigen Token / Textbaustein und dem Standard-Abo-Status `Subscribed` push-fähig werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push-Token / Textbaustein-Registrierung" }
{% endtab %}

{% tab iOS %}
iOS generiert nicht automatisch Push-Token / Textbaustein für eine App bei der Installation. Zusätzlich wird die Registrierung je nach iOS-Version unterschiedlich gehandhabt:

| Version | Vorläufige Autorisierung? | Details |
|------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **iOS 12** | Ja | Wenn Nutzer:innen Push-Benachrichtigungen aktivieren, erhalten Sie eine Standard-Autorisierung, die es Ihnen ermöglicht, [Vordergrund-Push-Benachrichtigungen](#foreground-vs-background) zu senden. Sie können jedoch auch eine [vorläufige Autorisierung]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options#provisional-push) anfordern, die es Ihnen ermöglicht, stille [Hintergrund-Push-Benachrichtigungen](#foreground-vs-background) direkt an die Mitteilungszentrale zu senden. |
| **iOS 11 oder früher** | Nein | Alle Nutzer:innen müssen explizit zustimmen, um Push-Benachrichtigungen zu erhalten. Ein Push-Token / Textbaustein wird erst nach Erteilung der Berechtigung generiert. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Push-Token / Textbaustein-Registrierung" }
{% endtab %}
{% endtabs %}

### Push-Abo-Status von Nutzer:innen prüfen {#checking-users-push-subscription-state}

![Nutzerprofil für Jane Doe mit dem Push-Abo-Status und Push-Registrierungsdetails auf dem Tab „Engagement“.]({% image_buster /assets/img/push_implementation_guide/checking-users-push-subscription-state.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Es gibt zwei Möglichkeiten, den Push-Abo-Status von Nutzer:innen mit Braze zu prüfen:

- **Kundenprofil**: Sie können auf einzelne Nutzerprofile über das Braze-Dashboard auf der Seite [Nutzersuche]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) zugreifen. Nachdem Sie ein Kundenprofil gefunden haben (über E-Mail-Adresse, Telefonnummer oder externe Nutzer-ID), können Sie den Tab **Engagement** auswählen, um den Abo-Status der Nutzer:innen einzusehen und manuell anzupassen.
- **REST-API-Export**: Sie können einzelne Nutzerprofile im JSON-Format exportieren, indem Sie die Endpunkte [Nutzer:innen nach Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) oder [Nutzer:innen nach Bezeichner]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) verwenden. Braze gibt ein Push-Token / Textbaustein-Objekt zurück, das Push-Aktivierungsinformationen pro Gerät enthält.

### Push-Registrierungsstatus prüfen {#checking-push-registration-status}

Auf dem Tab **Engagement** im Kundenprofil sehen Sie **Push Registered For** gefolgt von einem App-Namen. Wenn keine App-Informationen für dieses Gerät vorhanden sind, werden zwei Bindestriche (**&#45;&#45;**) angezeigt. Für jedes Gerät, das den Nutzer:innen gehört, gibt es einen Eintrag.

Wenn dem App-Namen des Geräteeintrags `Foreground:` vorangestellt ist, ist die App berechtigt, sowohl Vordergrund-Push-Benachrichtigungen (für Nutzer:innen sichtbar) als auch Hintergrund-Push-Benachrichtigungen (für Nutzer:innen nicht sichtbar) auf diesem Gerät zu empfangen.

![Push-Changelog mit einem Beispiel-Push-Token.]({% image_buster /assets/img/push_changelog.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

Wenn dem App-Namen des Geräteeintrags hingegen `Background:` vorangestellt ist, ist die App nur berechtigt, [Hintergrund-Push]({{site.baseurl}}/user_guide/channels/push/types#background-push-notifications) zu empfangen, und kann keine für Nutzer:innen sichtbaren Benachrichtigungen auf diesem Gerät anzeigen. Dies bedeutet in der Regel, dass die Nutzer:innen Benachrichtigungen für die App auf diesem Gerät deaktiviert haben.

Wenn ein Push-Token / Textbaustein auf demselben Gerät zu anderen Nutzer:innen verschoben wird, sind die ersten Nutzer:innen nicht mehr push-registriert.

## Push-Token / Textbaustein-Verwaltung {#push-token-management}

In der folgenden Tabelle finden Sie Aktionen, die zu Änderungen oder zur Entfernung von Push-Token / Textbaustein aus Nutzerprofilen führen.

| Aktion | Beschreibung |
| ------ | ----------- |
| Methode `changeUser()` wird aufgerufen | Die Braze-Methode `changeUser()` wechselt die Nutzer-ID, der die SDKs Nutzerverhaltens-Daten zuweisen. Diese Methode wird normalerweise aufgerufen, wenn sich Nutzer:innen in einer Anwendung anmelden. Wenn `changeUser()` mit einer anderen oder neuen Nutzer-ID auf einem bestimmten Gerät aufgerufen wird, wird das Push-Token / Textbaustein dieses Geräts zum entsprechenden Braze-Profil mit der zugehörigen Nutzer-ID verschoben. |
| Push-Fehler tritt auf | Einige häufige Push-Fehler, die zur Token / Textbaustein-Entfernung führen, sind `MismatchSenderId`, `InvalidRegistration` und andere Arten von Push-Bounces. <br><br>Sehen Sie sich unsere vollständige Liste häufiger [Push-Fehler]({{site.baseurl}}/user_guide/channels/push/push_error_codes) an. |
| Nutzer:in deinstalliert die App | Wenn Nutzer:innen die Anwendung von einem Gerät deinstallieren, entfernt Braze das Push-Token / Textbaustein aus dem Profil. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push-Token / Textbaustein-Verwaltung" }

### Wie sieht das im größeren Maßstab aus? {#what-does-this-look-like-on-a-broader-scale}

Wenn Nutzer:innen eine neue Anwendung öffnen und über eine Push-Abfrage den Push-Zugriff gewähren, wird ein Aufruf vom Braze SDK an die Push-Anbieter gesendet. Bei diesem Aufruf prüft der Push-Anbieter, ob alles korrekt eingerichtet ist. Wenn ja, wird ein Push-Token / Textbaustein an Ihr Gerät übergeben. Wenn dieses Token / Textbaustein eintrifft, kommuniziert das SDK dies an Braze. Nachdem Braze das Token / Textbaustein vom Push-Anbieter erhalten hat, aktualisieren oder erstellen wir ein neues Kundenprofil. Diese Nutzer:innen gelten nun als registriert.

Wenn wir eine Campaign starten möchten, erstellen wir eine Campaign in Braze, die einen Push-Payload generiert, der an den Push-Anbieter gesendet wird. Von dort aus liefert der Anbieter den Push-Payload an das Gerät der Nutzer:innen, und das SDK übergibt den Messaging-Status an Braze.

![Ein Flussdiagramm, das den oben beschriebenen Push-Prozess zwischen Braze, den Kund:innen und dem Apple Push Notification Service oder Firebase Cloud Messaging darstellt.]({% image_buster /assets/img/push_process.png %})

| Registrierungsschritte | Messaging-Schritte |
| ------------------ | --------------- |
| 1. Kund:in (Gerät) registriert sich beim Push-Anbieter<br>2. Anbieter generiert und liefert Push-Token / Textbaustein<br>3. Token / Textbaustein an Braze übermitteln |1. Braze sendet Push-Payload an den Anbieter<br>2. Anbieter liefert den Push-Payload an das Gerät<br>3. SDK übergibt Messaging-Statistiken an Braze |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Wie sieht das im größeren Maßstab aus?" }

## Häufig gestellte Fragen {#frequently-asked-questions}

### Was passiert, wenn Nutzer:innen mit Opt-in meine App löschen und erneut herunterladen? {#what-happens-when-an-opted-in-user-deletes-and-then-redownloads-my-app}

Angenommen, Nutzer:innen aktivieren Push, erhalten einige Push-Nachrichten und löschen dann die App. Dadurch wird die Push-Zustimmung auf Geräteebene entfernt. Ab hier führt der erste Bounce nach der Deinstallation automatisch dazu, dass diese Nutzer:innen von zukünftigen Push-Nachrichten abgemeldet werden. Wenn Nutzer:innen danach die App erneut installieren, aber nicht starten, kann Braze keinen Push an sie senden, da Push-Token / Textbaustein für Ihre App nicht erneut gewährt wurden.

Wenn Nutzer:innen den Vordergrund-Push erneut aktivieren, ist außerdem ein Sitzungsstart erforderlich, um diese Informationen in ihrem Kundenprofil zu aktualisieren und den Empfang von Push-Nachrichten zu ermöglichen.

### Wann laufen Push-Token / Textbaustein ab? {#push-token-expire}

Leider definieren APNs und FCM dies nicht genau. Push-Token / Textbaustein können ablaufen, wenn eine App aktualisiert wird, wenn Nutzer:innen ihre Daten auf ein neues Gerät übertragen oder wenn sie ein Betriebssystem neu installieren. Im Allgemeinen haben wir keinen genauen Einblick, warum Push-Anbieter bestimmte Push-Token / Textbaustein ablaufen lassen.

Um dieser Unklarheit Rechnung zu tragen, registrieren und übermitteln unsere SDK-Push-Integrationen Token immer bei Sitzungsstart, um sicherzustellen, dass wir über das aktuellste Token verfügen.