---
nav_title: Segment
article_title: Segment
page_order: 1
alias: /partners/segment/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Segment, einer geschäftskunden Data Platform, die Informationen zwischen den Quellen in Ihrem Marketing-Stack sammelt und weiterleitet."
page_type: partner
search_tag: Partner

---

# Segment

{% multi_lang_include video.html id="RfOHfZ34hYM" align="right" %}

> [Segment](https://segment.com) ist eine geschäftskunden Data Platform, mit der Sie Ihre Kundendaten sammeln, bereinigen und aktivieren können.

Die Integration von Braze und Segment ermöglicht es Ihnen, Ihre Nutzer:innen zu tracken und Daten an verschiedene Anbieter von Analytics weiterzuleiten. Segment ermöglicht Ihnen:

- [Segment Engage]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_engage) mit Braze zu synchronisieren, um es in Braze-Campaigns und Canvas-Segmentierung zu verwenden.
- [Daten zwischen den beiden Plattformen zu importieren](#integration-options). Wir bieten eine Side-by-side-SDK-Integration für Ihre Android-, iOS- und Web-Anwendungen sowie eine Server-zu-Server-Integration zur Synchronisierung Ihrer Daten mit den Braze REST APIs.
- [Daten über Currents mit Segment zu verbinden]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents).

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Segment-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein [Segment-Konto](https://app.segment.com/login) erforderlich. |
| Installierte Quelle und Segment-Quell-[Bibliotheken](https://segment.com/docs/sources/) | Die Herkunft der Daten, die an Segment gesendet werden, wie z. B. mobile Apps, Websites oder Backend-Server.<br><br>Sie müssen die Bibliotheken in Ihrer App, Ihrer Website oder Ihrem Server installieren, bevor Sie einen erfolgreichen `Source > Destination`-Ablauf einrichten können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Um Braze und Segment zu integrieren, müssen Sie [Braze als Ziel](#connection-settings) entsprechend dem [von Ihnen gewählten Integrationstyp](#integration-options) (Verbindungsmodus) festlegen. Wenn Sie ein neuer Braze-Kunde sind, können Sie historische Daten mithilfe von [Segment Replays](#segment-replays) an Braze weitergeben. Als Nächstes müssen Sie [Abbildungen](#methods) einrichten und [Ihre Integration testen](#step-4-test-your-integration), um einen reibungslosen Datenfluss zwischen Braze und Segment zu gewährleisten.

### Schritt 1: Ein Braze-Ziel erstellen {#connection-settings}

Nachdem Sie Ihre Quellen erfolgreich eingerichtet haben, müssen Sie Braze als [Ziel](https://segment.com/docs/destinations/) für jede Quelle (iOS, Android, Web usw.) konfigurieren. Sie haben viele Möglichkeiten, den Datenfluss zwischen Braze und Segment über die Verbindungseinstellungen anzupassen.

### Schritt 2: Ziel-Framework und Verbindungstyp wählen {#integration-options}

Navigieren Sie in Segment zu **Destinations** > **Braze** > **Configure Braze** > **Select your Source** > **Setup**.

![Die Seite zur Einrichtung der Quelle. Diese Seite enthält Einstellungen, um das Ziel-Framework als „actions“ oder „classic“ und den Verbindungsmodus als „cloud mode“ oder „device mode“ festzulegen.]({% image_buster /assets/img/segment/setup.png %})

Sie können die Web-Quelle von Segment (Analytics.js) und die nativen clientseitigen Bibliotheken mit Braze integrieren, indem Sie entweder eine Side-by-side-Integration (Gerätemodus) oder eine Server-zu-Server-Integration (Cloud-Modus) verwenden.

Die Wahl des Verbindungsmodus hängt von der Art der Quelle ab, für die das Ziel konfiguriert ist.

| Integration | Details |
| ----------- | ------- |
| [Side-by-side<br>(Gerätemodus)](#side-by-side-sdk-integration) | Verwendet das SDK von Segment, um Events in native Braze-Aufrufe zu übersetzen, was den Zugriff auf tiefere Features und eine umfassendere Nutzung von Braze als bei der Server-zu-Server-Integration ermöglicht.<br><br>Beachten Sie, dass Segment nicht alle Braze-Methoden unterstützt (z. B. Content Cards). Um eine Braze-Methode zu verwenden, die nicht durch eine entsprechende Abbildung abgedeckt ist, müssen Sie die Methode aufrufen, indem Sie Ihrer Codebasis nativen Braze-Code hinzufügen. |
| [Server-zu-Server<br>(Cloud-Modus)](#server-to-server-integration) | Leitet Daten von Segment an Braze REST API-Endpunkte weiter.<br><br>Unterstützt keine Braze-UI-Features wie In-App-Nachrichten, Content Cards oder Push-Benachrichtigungen. Es gibt auch automatisch erfasste Daten, wie z. B. Felder auf Geräteebene, die mit dieser Methode nicht verfügbar sind.<br><br>Ziehen Sie eine Side-by-side-Integration in Betracht, wenn Sie diese Features nutzen möchten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: Ziel-Framework und Verbindungstyp wählen" }

{% alert note %}
Besuchen Sie [Segment](https://segment.com/docs/destinations/#connection-modes), um mehr über die beiden Integrationsmöglichkeiten (Verbindungsmodi) zu erfahren, einschließlich der jeweiligen Vorteile.
{% endalert %}

#### Side-by-side-SDK-Integration {#side-by-side-sdk-integration}

Diese Integration, die auch als Gerätemodus bezeichnet wird, bildet das SDK und die [Methoden](#methods) von Segment auf das Braze SDK ab und ermöglicht so den Zugriff auf alle Features, die unser SDK bietet, wie Push, In-App-Nachrichten und andere native Braze-Methoden.

{% alert note %}
Wenn Sie den Gerätemodus von Segment verwenden, müssen Sie das Braze SDK nicht direkt integrieren. Wenn Sie Braze als Gerätemodus-Ziel für Segment hinzufügen, initialisiert das Segment SDK das Braze SDK und ruft die entsprechenden abgebildeten Braze-Methoden auf.
{% endalert %}

{% alert important %}
Für Gerätemodus-Integrationen auf Mobilgeräten müssen Sie das Braze-Ziel-Plugin zusätzlich zur Konfiguration des Ziels im Segment-Dashboard zu Ihrer App hinzufügen. Das Segment SDK enthält das Braze-Plugin nicht standardmäßig – ohne dieses kann das Segment SDK keine Daten oder abgebildeten Methodenaufrufe an Braze weiterleiten, und Features wie Push, In-App-Nachrichten und Content Cards funktionieren nicht. Installationsanweisungen finden Sie in den plattformspezifischen Tabs in diesem Abschnitt.
{% endalert %}

Bei der Verwendung einer Gerätemodus-Verbindung weist das Braze SDK, ähnlich wie bei der nativen Integration des Braze SDK, jedem/jeder Nutzer:in eine `device_id` und einen Backend-Bezeichner, `braze_id`, zu. Dies ermöglicht es Braze, anonyme Aktivitäten des Geräts zu erfassen, indem diese Bezeichner anstelle von `userId` abgeglichen werden.

{% alert note %}
Wenn Sie [Zielfilter](https://segment.com/docs/connections/destinations/destination-filters/) mit Gerätemodus-Zielen (Kotlin oder Swift) verwenden, müssen Sie das Ziel-Plugin mit aktivierter Filterunterstützung konfigurieren. Weitere Informationen zu unterstützten Plugin-Versionen finden Sie in der [Dokumentation zu Zielfiltern](https://segment.com/docs/connections/destinations/destination-filters/) von Segment.
{% endalert %}

{% tabs local %}
{% tab Android %}

{% alert important %}
Der Quellcode für die Android-Gerätemodus-Integration wird von Braze gepflegt und regelmäßig aktualisiert, um neue Braze SDK-Versionen zu berücksichtigen.

<br>
Welches Braze SDK Sie verwenden, hängt davon ab, welches Segment SDK Sie verwenden:

| | Segment SDK | Braze SDK |
| - | ----------- | --------- |
| Bevorzugt | [Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin) | [Braze Segment Kotlin](https://github.com/braze-inc/braze-segment-kotlin) |
| Legacy | [Analytics-Android](https://github.com/segmentio/analytics-android) | [Braze Segment Android](https://github.com/braze-inc/braze-segment-android) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Side-by-side-SDK-Integration" }


{% endalert %}

Um Braze als Gerätemodus-Ziel für Ihre Android-Quelle einzurichten, wählen Sie **Actions** als **Destination framework** und dann **Save**.

Um die Side-by-side-Integration abzuschließen, müssen Sie das [Braze Kotlin-Ziel-Plugin](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/) zu Ihrer Android-App hinzufügen. Dieses Plugin verbindet das Segment SDK mit dem Braze SDK und ermöglicht den Datenfluss im Gerätemodus zu Braze. Folgen Sie den Installationsanweisungen von Segment, um die Plugin-Abhängigkeit hinzuzufügen und es mit Ihrer Segment-Analytics-Instanz zu initialisieren.

Der Quellcode für die [Android-Gerätemodus](https://github.com/braze-inc/braze-segment-kotlin)-Integration wird von Braze gepflegt und regelmäßig aktualisiert, um neue Braze SDK-Versionen zu berücksichtigen.

{% endtab %}
{% tab iOS %}

{% alert important %}
Der Quellcode für die iOS-Gerätemodus-Integration wird von Braze gepflegt und regelmäßig aktualisiert, um neue Braze SDK-Versionen zu berücksichtigen.

<br>
Welches Braze SDK Sie verwenden, hängt davon ab, welches Segment SDK Sie verwenden:

| | Segment SDK | Braze SDK |
| - | ----------- | --------- |
| Bevorzugt | [Analytics-Swift](https://github.com/segmentio/analytics-swift) | [Braze Segment Swift](https://github.com/braze-inc/braze-segment-swift) |
| Legacy | [Analytics-iOS](https://github.com/segmentio/analytics-ios) | [Braze Segment iOS](https://github.com/Appboy/appboy-segment-ios) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Side-by-side-SDK-Integration" }
{% endalert %}

Um Braze als Gerätemodus-Ziel für Ihre iOS-Quelle einzurichten, wählen Sie **Actions** als **Destination framework** und dann **Save**.

Um die Side-by-side-Integration abzuschließen, müssen Sie das [Braze Swift-Ziel-Plugin](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/) zu Ihrer iOS-App hinzufügen. Dieses Plugin verbindet das Segment SDK mit dem Braze SDK und ermöglicht den Datenfluss im Gerätemodus zu Braze. Folgen Sie den Installationsanweisungen von Segment, um die Plugin-Abhängigkeit (über den Swift-Paketmanager oder CocoaPods) hinzuzufügen und es mit Ihrer Segment-Analytics-Instanz zu initialisieren.

Der Quellcode für die [iOS-Gerätemodus](https://github.com/braze-inc/braze-segment-swift)-Integration wird von Braze gepflegt und regelmäßig aktualisiert, um neue Braze SDK-Versionen zu berücksichtigen.

{% endtab %}
{% tab Web oder JavaScript %}

Das Braze Web Mode (Actions) Framework von Segment wird empfohlen, um Braze als Gerätemodus-Ziel für Ihre Web-Quelle einzurichten.

Wählen Sie in Segment **Actions** als Ziel-Framework und **Device Mode** als Verbindungsmodus.

![Segment-Zieleinrichtung mit ausgewähltem Actions-Framework und Device Mode.]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab React Native %}
Der Quellcode für das [React Native Braze Plugin](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze) wird von Segment gepflegt und regelmäßig aktualisiert, um neue Braze SDK-Versionen zu berücksichtigen.

Wenn Sie eine React Native Segment-Quelle mit Braze verbinden, müssen Sie eine Quelle und ein Ziel pro Betriebssystem einrichten. Zum Beispiel die Einrichtung eines iOS-Ziels und eines Android-Ziels.

Innerhalb Ihrer App-Codebasis initialisieren Sie das Segment SDK bedingt nach Gerätetyp, indem Sie den jeweiligen, mit jeder App verbundenen Quell-Schreibschlüssel verwenden.

Wenn ein Push-Token von einem Gerät registriert und an Braze gesendet wird, wird es mit dem App-Bezeichner verknüpft, der bei der Initialisierung des SDK verwendet wurde. Die gerätetypabhängige Initialisierung stellt sicher, dass alle an Braze gesendeten Push-Token mit der entsprechenden App verknüpft sind.

{% alert important %}
Wenn die React Native App Braze mit demselben Braze-App-Bezeichner für alle Geräte initialisiert, werden alle React Native Nutzer:innen in Braze als Android- oder iOS-Nutzer:innen betrachtet und alle Push-Token werden mit diesem Betriebssystem assoziiert.
{% endalert %}

Um Braze als Gerätemodus-Ziel für jede Quelle einzurichten, wählen Sie **Actions** als **Destination framework** und dann **Save**.

{% endtab %}
{% endtabs %}

#### Server-zu-Server-Integration {#server-to-server-integration}

Diese auch als Cloud-Modus bezeichnete Integration leitet Daten von Segment an die Braze REST APIs weiter. Verwenden Sie das [Braze Cloud Mode (Actions)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/) Framework von Segment, um ein Cloud-Modus-Ziel für jede Ihrer Quellen einzurichten.

Im Gegensatz zur Side-by-side-Integration unterstützt die Server-zu-Server-Integration keine Braze-UI-Features wie In-App-Nachrichten, Content Cards oder die automatische Registrierung von Push-Token. Es gibt auch [automatisch erfasste]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection#user-data-collection) Daten (wie anonyme Nutzer:innen und Felder auf Geräteebene), die nicht über den Cloud-Modus verfügbar sind.

Wenn Sie diese Daten und Features nutzen möchten, sollten Sie die Side-by-side-SDK-Integration (Gerätemodus) verwenden.

Der Quellcode für das [Braze Cloud Mode (Actions)-Ziel](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze) wird von Segment verwaltet.

### Schritt 3: Einstellungen {#step-3-settings}

Definieren Sie die Einstellungen für Ihr Ziel. Nicht alle Einstellungen gelten für alle Zieltypen.

{% tabs local %}
{% tab Mobile Device-Mode %}

| Einstellung | Beschreibung |
| ------- | ----------- |
| App-Bezeichner | Der App-Bezeichner, der verwendet wird, um die spezifische App zu referenzieren. Diesen finden Sie im Braze-Dashboard unter **Einstellungen verwalten**. |
| Angepasster API-Endpunkt<br>(SDK-Endpunkt) | Ihr Braze SDK-Endpunkt, der Ihrer Instanz entspricht (z. B. `sdk.iad-01.braze.com`) |
| Endpunkt-Region | Ihre Braze-Instanz (z. B. US 01, US 02, EU 01 usw.) |
| Automatische Registrierung von In-App-Nachrichten aktivieren | Deaktivieren Sie dies, wenn Sie In-App-Nachrichten manuell registrieren möchten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 3: Einstellungen" }

{% endtab %}
{% tab Web Device-Mode %}

| Einstellung | Beschreibung |
| ------- | ----------- |
| App-Bezeichner | Der App-Bezeichner, der verwendet wird, um die spezifische App zu referenzieren. Diesen finden Sie im Braze-Dashboard unter **Einstellungen verwalten**. |
| Angepasster API-Endpunkt<br>(SDK-Endpunkt) | Ihr Braze SDK-Endpunkt, der Ihrer Instanz entspricht (z. B. `sdk.iad-01.braze.com`) |
| Safari Website Push ID | Wenn Sie Safari Push unterstützen, müssen Sie diese Option mit der Website Push ID angeben, die Sie Apple bei der Erstellung Ihres Safari Push-Zertifikats mitgeteilt haben (beginnt mit `web`, zum Beispiel `web.com.example.domain`). |
| Braze Web SDK Version | Die Version des Braze Web SDK, die Sie verwenden möchten |
| In-App-Nachrichten automatisch senden | Standardmäßig werden alle In-App-Nachrichten, für die Nutzer:innen berechtigt sind, automatisch zugestellt. Deaktivieren Sie dies, wenn Sie In-App-Nachrichten manuell anzeigen möchten. |
| Font Awesome nicht laden | Braze verwendet Font Awesome für In-App-Nachrichten-Symbole. Standardmäßig lädt Braze FontAwesome automatisch aus dem FontAwesome CDN. Um dieses Verhalten zu deaktivieren (z. B. weil Ihre Website eine angepasste Version von FontAwesome verwendet), setzen Sie diese Option auf `TRUE`. Beachten Sie, dass Sie in diesem Fall dafür verantwortlich sind, dass FontAwesome auf Ihrer Website geladen ist – andernfalls werden In-App-Nachrichten möglicherweise nicht korrekt dargestellt. |
| HTML-In-App-Nachrichten aktivieren | Wenn Sie diese Option aktivieren, können Nutzer:innen des Braze-Dashboards HTML-In-App-Nachrichten verwenden. |
| In-App-Nachrichten in einem neuen Tab öffnen | Standardmäßig werden Links von In-App-Nachrichten-Klicks im aktuellen Tab oder in einem neuen Tab geladen, wie im Dashboard für jede Nachricht angegeben. Setzen Sie diese Option auf `TRUE`, um zu erzwingen, dass alle Links von In-App-Nachrichten-Klicks in einem neuen Tab oder Fenster geöffnet werden. |
| In-App-Nachrichten z-index | Geben Sie einen Wert für diese Option an, um die Standard-Z-Indizes von Braze zu überschreiben. |
| Explizites Schließen von In-App-Nachrichten verlangen | Standardmäßig wird eine In-App-Nachricht durch Drücken der Escape-Taste oder einen Klick auf den ausgegrauten Hintergrund der Seite geschlossen. Setzen Sie diese Option auf true, um dieses Verhalten zu verhindern und einen expliziten Button-Klick zum Schließen von Nachrichten zu verlangen. |
| Mindestabstand zwischen triggernden Aktionen in Sekunden | Der Standardwert ist 30.<br>Standardmäßig wird eine triggernde Aktion nur ausgelöst, wenn seit der letzten triggernden Aktion mindestens 30 Sekunden vergangen sind. Geben Sie einen Wert für diese Konfigurationsoption an, um diesen Standard mit einem eigenen Wert zu überschreiben. Wir empfehlen, diesen Wert nicht kleiner als 10 zu wählen, um Nutzer:innen nicht mit Benachrichtigungen zu überhäufen. |
| Service-Worker-Speicherort | Standardmäßig sucht Braze bei der Registrierung von Nutzer:innen für Web-Push-Benachrichtigungen nach der erforderlichen Service-Worker-Datei im Stammverzeichnis Ihres Webservers unter `/service-worker.js`. Wenn Sie Ihren Service Worker unter einem anderen Pfad auf diesem Server hosten möchten, geben Sie für diese Option einen Wert an, der dem absoluten Pfad zur Datei entspricht (zum Beispiel `/mycustompath/my-worker.js`). Beachten Sie, dass die Festlegung eines Wertes hier den Umfang der Push-Benachrichtigungen auf Ihrer Website einschränkt. Im obigen Beispiel kann `requestPushPermission`, da sich die Service-Worker-Datei im Verzeichnis `/mycustompath/` befindet, nur von Webseiten aufgerufen werden, die mit `http://yoursite.com/mycustompath/` beginnen. |
| Push-Token-Wartung deaktivieren | Standardmäßig synchronisieren Nutzer:innen, die bereits eine Web-Push-Berechtigung erteilt haben, ihr Push-Token bei neuen Sitzungen automatisch mit dem Braze-Backend, um die Zustellbarkeit zu gewährleisten. Um dieses Verhalten zu deaktivieren, setzen Sie diese Option auf `FALSE`. |
| Service Worker extern verwalten | Wenn Sie Ihren eigenen Service Worker haben, den Sie registrieren und dessen Lebenszyklus Sie kontrollieren, setzen Sie diese Option auf `TRUE`, und das Braze SDK wird keinen Service Worker registrieren oder deregistrieren. Wenn Sie diese Option auf `TRUE` setzen, müssen Sie den Service Worker selbst registrieren, bevor Sie `requestPushPermission` aufrufen, und sicherstellen, dass er den Braze-Service-Worker-Code enthält, entweder mit `self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');` oder indem Sie den Inhalt dieser Datei direkt einfügen. Wenn diese Option `TRUE` ist, ist die Option `serviceWorkerLocation` irrelevant und wird ignoriert. |
| Content-Security-Nonce | Wenn Sie einen Wert für diese Option angeben, fügt das Braze SDK die Nonce zu allen vom SDK erstellten `<script>`- und `<style>`-Elementen hinzu. Dies ermöglicht es dem Braze SDK, mit der Content-Security-Policy Ihrer Website zu arbeiten. Zusätzlich zur Einstellung dieser Nonce müssen Sie eventuell auch das Laden von FontAwesome zulassen. Dies können Sie tun, indem Sie `use.fontawesome.com` zur Zulässigkeitsliste Ihrer Content-Security-Policy hinzufügen oder indem Sie die Option `doNotLoadFontAwesome` verwenden und FontAwesome manuell laden. |
| Crawler-Aktivität zulassen | Standardmäßig ignoriert das Braze Web SDK Aktivitäten von bekannten Spidern oder Web-Crawlern, wie z. B. Google, basierend auf dem User-Agent-String. Dies spart Datenpunkte, macht Analytics genauer und kann das Seitenranking verbessern. Wenn Sie jedoch möchten, dass Braze stattdessen die Aktivitäten dieser Crawler protokolliert, können Sie diese Option auf `TRUE` setzen. |
| Protokollierung aktivieren | Setzen Sie diese Option auf `TRUE`, um die Protokollierung standardmäßig zu aktivieren. Beachten Sie, dass Braze dadurch in der JavaScript-Konsole protokolliert, was für alle Nutzer:innen sichtbar ist. Bevor Sie Ihre Seite in Produktion bringen, sollten Sie dies entfernen oder einen alternativen Logger mit `setLogger` bereitstellen. |
| Vom/von der Nutzer:in bereitgestelltes JavaScript zulassen | Standardmäßig lässt das Braze Web SDK keine vom/von der Nutzer:in bereitgestellten JavaScript-Klick-Aktionen zu, da es Nutzer:innen des Braze-Dashboards erlaubt, JavaScript auf Ihrer Website auszuführen. Um anzugeben, dass Sie den Nutzer:innen des Braze-Dashboards zutrauen, nicht bösartige JavaScript-Klick-Aktionen zu schreiben, setzen Sie diese Eigenschaft auf `TRUE`. Wenn `enableHtmlInAppMessages` auf `TRUE` steht, wird diese Option ebenfalls auf `TRUE` gesetzt. |
| App-Version | Wenn Sie einen Wert für diese Option angeben, werden an Braze gesendete Nutzer:innen-Events mit der angegebenen Version assoziiert, die für die Segmentierung von Nutzer:innen verwendet werden kann. |
| Sitzungs-Timeout in Sekunden | Der Standardwert ist 30.<br>Standardmäßig werden Sitzungen nach 30 Minuten Inaktivität beendet. Geben Sie einen Wert für diese Konfigurationsoption an, um diesen Standard mit einem eigenen Wert zu überschreiben. |
| Geräteeigenschaften-Allowlist | Standardmäßig erkennt und sammelt das Braze SDK automatisch alle Geräteeigenschaften in `DeviceProperties`. Um dieses Verhalten zu überschreiben, geben Sie ein Array von `DeviceProperties` an. Beachten Sie, dass ohne einige Eigenschaften nicht alle Features ordnungsgemäß funktionieren. Zum Beispiel funktioniert die Zustellung zur Ortszeit nicht ohne die Zeitzone. |
| Lokalisierung | Standardmäßig werden alle vom SDK erzeugten, für Nutzer:innen sichtbaren Nachrichten in der Browsersprache angezeigt. Geben Sie einen Wert für diese Option an, um dieses Verhalten zu überschreiben und eine bestimmte Sprache zu erzwingen. Der Wert für diese Option sollte ein ISO 639-1 Sprachcode sein. |
| Keine Cookies | Standardmäßig speichert das Braze SDK kleine Datenmengen (Nutzer-IDs, Sitzungs-IDs) in Cookies. Dies ermöglicht es Braze, Nutzer:innen und Sitzungen über verschiedene Subdomänen Ihrer Website hinweg zu erkennen. Wenn dies für Sie ein Problem darstellt, geben Sie `TRUE` für diese Option ein, um die Cookie-Speicherung zu deaktivieren und sich vollständig auf HTML 5 localStorage zu verlassen, um Nutzer:innen und Sitzungen zu identifizieren. |
| Alle Seiten tracken | **Nur klassisches Ziel Web-Gerätemodus (Wartung)**<br><br>Segment empfiehlt die Migration zum Web Actions Framework-Ziel, wo diese Einstellung [durch Abbildungen aktiviert](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping) werden kann.<br><br>Dadurch werden alle [Seitenaufrufe](https://segment.com/docs/spec/page/) an Braze als Event „Loaded/Viewed a Page“ gesendet. |
| Nur benannte Seiten tracken | **Nur klassisches Ziel Web-Gerätemodus (Wartung)**<br><br>Segment empfiehlt die Migration zum Web Actions Framework-Ziel, wo diese Einstellung [durch Abbildungen aktiviert](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping) werden kann.<br><br>Dadurch werden nur Seitenaufrufe an Braze gesendet, die mit einem Namen verknüpft sind. |
| Kauf protokollieren, wenn Umsatz vorhanden ist | **Nur klassisches Ziel Web-Gerätemodus (Wartung)**<br><br>Segment empfiehlt die Migration zum Web Actions Framework-Ziel, wo diese Einstellung [durch Abbildungen aktiviert](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping) werden kann.<br><br>Wenn diese Option aktiviert ist, triggern alle Track-Aufrufe mit der Umsatz-Eigenschaft ein Kauf-Event. |
| Nur bekannte Nutzer:innen tracken | **Nur klassisches Ziel Web-Gerätemodus (Wartung)**<br><br>Segment empfiehlt die Migration zum Web Actions Framework-Ziel, wo diese Einstellung durch Abbildungen aktiviert werden kann.<br><br>Falls aktiviert, verzögert diese Einstellung den Aufruf von `window.braze.initialize`, bis eine gültige `userId` vorliegt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 3: Einstellungen" }

{% endtab %}
{% tab Cloud-Mode %}

| Einstellung | Beschreibung |
| ------- | ----------- |
| App-Bezeichner | Der App-Bezeichner, der verwendet wird, um die spezifische App zu referenzieren. Diesen finden Sie im Braze-Dashboard unter **Einstellungen verwalten**. |
| REST-API-Schlüssel | Diesen finden Sie in Ihrem Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. |
| Angepasster REST API-Endpunkt | Ihr Braze REST-Endpunkt, der Ihrer Instanz entspricht (z. B. rest.iad-01.braze.com). |
| Nur vorhandene Nutzer:innen aktualisieren | **Nur klassisches Ziel Cloud-Modus (Wartung)**<br><br>Segment empfiehlt die Migration zum Cloud Actions Framework-Ziel, wo diese Einstellung [durch Abbildungen aktiviert](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping) werden kann.<br><br>Legt fest, ob nur bestehende Nutzer:innen aktualisiert werden sollen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 3: Einstellungen" }

{% endtab %}
{% endtabs %}

### Schritt 4: Methoden abbilden {#methods}

Braze unterstützt die Segment-Methoden [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page), [Identify](https://segment.com/docs/spec/identify/) und [Track](https://segment.com/docs/spec/track/). Welche Arten von Bezeichnern bei diesen Methoden verwendet werden, hängt davon ab, ob die Daten über eine Server-zu-Server-Integration (Cloud-Modus) oder eine Side-by-side-Integration (Gerätemodus) gesendet werden. In den Zielen Braze Web Mode Actions und Cloud Mode Actions können Sie auch eine Abbildung für einen [Segment-Alias-Aufruf](https://segment.com/docs/connections/spec/alias/) einrichten.

{% alert note %}
Obwohl Nutzer-Aliase als Bezeichner im Ziel Braze Cloud Mode (Actions) unterstützt werden, ist zu beachten, dass der Alias-Aufruf von Segment nicht direkt mit Braze-Nutzer-Aliasen zusammenhängt.
{% endalert %}

| Bezeichner-Typ | Unterstütztes Ziel |
| --------------- | --------------------- |
| `userId` (`external_id`) | Alle |
| Anonyme Nutzer:innen | Gerätemodus-Ziele |
| Nutzer-Alias | Cloud-Modus-Ziele |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 4: Methoden abbilden" }

Das Cloud-Modus (Actions)-Ziel bietet eine [Aktion „Alias erstellen“](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#create-alias), mit der Sie einen reinen Alias-Nutzer:in erstellen oder einen Alias zu einem bestehenden `external_id`-Profil hinzufügen können. Die [Aktion „Nutzer:in identifizieren“](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#identify-user) kann zusammen mit der Aktion „Alias erstellen“ verwendet werden, um einen reinen Alias-Nutzer:in mit einer `external_id` zusammenzuführen, nachdem eine solche für den/die Nutzer:in verfügbar geworden ist.

Es ist auch möglich, einen Workaround zu entwickeln und `braze_id` zu verwenden, um anonyme Nutzerdaten im Cloud-Modus zu senden. Dies erfordert die manuelle Aufnahme der `braze_id` des Nutzers/der Nutzerin in alle Ihre Segment API-Aufrufe. In der [Dokumentation von Segment](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users) erfahren Sie mehr darüber, wie Sie diesen Workaround einrichten können.

An Braze gesendete Zieldaten können im Rahmen von Cloud-Modus-Aktionen gebündelt werden. Die Batch-Größe ist auf 75 Events begrenzt, und diese Batches sammeln sich über einen Zeitraum von 30 Sekunden an, bevor sie gesendet werden. Das Batching von Anfragen erfolgt pro Aktion. Zum Beispiel werden Identify-Aufrufe (Attribute) in einer Anfrage und Track-Aufrufe (angepasste Events) in einer zweiten Anfrage zusammengefasst. Braze empfiehlt, dieses Feature zu aktivieren, da es die Anzahl der Anfragen reduziert, die von Segment an Braze gesendet werden. Dadurch verringert sich das Risiko, dass das Ziel auf die Rate-Limits von Braze stößt und Anfragen wiederholt werden müssen.

Sie können das Batching für eine Aktion aktivieren, indem Sie zu Ihrem Braze-Ziel > **Mappings** navigieren. Klicken Sie dort auf das 3-Punkte-Symbol neben der Abbildung und wählen Sie **Edit Mapping**. Scrollen Sie zum Ende des Abschnitts **Select mappings** und vergewissern Sie sich, dass **Batch Data to Braze** auf **Yes** gesetzt ist.


{% tabs local %}
{% tab Identify %}
#### Identify

Der [Identify](https://segment.com/docs/spec/identify/)-Aufruf ermöglicht es Ihnen, Nutzer:innen mit ihren Aktionen zu verknüpfen und Attribute über sie aufzuzeichnen.

Bestimmte spezielle Segment-Traits werden Standard-Attribut-Profilfeldern in Braze zugeordnet:

| Spezielle Segment-Traits | Braze-Standardattribute |
| ------------- | ----------- |
| `userId` | `external_id` |
| `firstName` | `first_name` |
| `lastName` | `last_name` |
| `email` | `email` |
| `birthday` | `dob` |
| `address.country` | `country` |
| `address.city` | `home_city` |
| `gender` | `gender` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identify" }

Andere reservierte Braze-Profilfelder wie `email_subscribe` und `push_subscribe` können gesendet werden, indem Sie die Braze-Namenskonvention für diese Felder verwenden und sie als Traits innerhalb eines Identify-Aufrufs übergeben.

##### Nutzer:in zu einer Abo-Gruppe hinzufügen {#adding-a-user-to-a-subscription-group}

Sie können Nutzer:innen auch über die folgenden Felder im Traits-Parameter für eine bestimmte Abo-Gruppe abonnieren oder abmelden.

Verwenden Sie das reservierte Braze-Profilfeld namens `braze_subscription_groups`, das mit einem Array von Objekten verknüpft werden kann. Jedes Objekt im Array sollte zwei reservierte Schlüssel haben:

1. `subscription_group_state`: Gibt an, ob der/die Nutzer:in für eine bestimmte Abo-Gruppe `"subscribed"` oder `"unsubscribed"` ist.
2. `subscription_group_id`: Stellt die eindeutige ID der Abo-Gruppe dar. Sie finden diese ID im Braze-Dashboard unter **Abo-Gruppen-Verwaltung**.

{% subtabs %}
{% subtab Swift %}
```swift
analytics.identify(
  userId: "{your-user}",
  traits: [
    "braze_subscription_groups": [
      [
        "subscription_group_id": "{your-group-id}",
        "subscription_group_state": "subscribed"
      ],
      [
        "subscription_group_id", "{your-group-id}",
        "subscription_group_state": "unsubscribed"
      ]
    ]
  ]
)
```
{% endsubtab %}
{% subtab Kotlin %}
```kotlin
analytics.identify(
  "{your-user}",
  buildJsonObject {
    put("braze_subscription_groups", buildJsonArray {
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "subscribed")
          }
        )
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "unsubscribed")
          }
        )
      }
    )
  }
)
```
{% endsubtab %}
{% subtab TypeScript %}
```typescript
analytics.identify(
  "{your-user}",
  {
    braze_subscription_groups: [
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "subscribed"
      },
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "unsubscribed"
      }
    ]
  }
)
```
{% endsubtab %}
{% endsubtabs %}

##### Angepasste Attribute {#custom-attributes}

Alle anderen Traits werden als [angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) aufgezeichnet.

| Segment-Methode | Braze-Methode | Beispiel |
|---|---|---|
| Identify mit Nutzer-ID | Externe ID setzen | Segment: `analytics.identify("dawei");`<br>Braze: `Braze.changeUser("dawei")` |
| Identify mit reservierten Traits | Nutzer:innen-Attribute setzen | Segment: `analytics.identify({email: "dawei@braze.com"});`<br> Braze: `Braze.getUser().setEmail("dawei@braze.com");`
| Identify mit angepassten Traits | Angepasste Attribute setzen | Segment: `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze: `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")`;
| Identify mit Nutzer-ID und Traits | Segment: Externe ID und Attribut setzen | Kombinieren Sie die vorangegangenen Methoden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Angepasste Attribute" }

In den Zielen [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile) und [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile) können diese Abbildungen mit der Aktion „Nutzerprofil aktualisieren“ eingestellt werden.

{% alert important %}
Stellen Sie bei der Übergabe von Nutzer:innen-Attributdaten sicher, dass Sie nur Werte für Attribute übergeben, die sich seit dem letzten Update geändert haben. So stellen Sie sicher, dass Sie nicht unnötigerweise Datenpunkte protokollieren. Für clientseitige Quellen verwenden Sie das Open-Source-[Middleware](https://github.com/segmentio/segment-braze-mobile-middleware)-Tool von Segment, um Ihre Integration zu optimieren und die Datenpunkt-Nutzung zu begrenzen, indem Sie doppelte `identify()`-Aufrufe von Segment entprellen.

{% endalert %}
{% endtab %}

{% tab Track %}
#### Track

Wenn Sie ein Event tracken, erfassen wir dieses Event als [angepasstes Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events) unter dem angegebenen Namen.

Metadaten, die innerhalb des Eigenschaften-Objekts des Track-Aufrufs gesendet werden, werden in Braze als angepasste Event-Eigenschaften für das zugehörige Event protokolliert. Es werden alle [Datentypen für angepasste Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) unterstützt.

In den Zielen [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event) und [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event) können diese Abbildungen mit der Aktion „Track Event“ eingestellt werden.

| Segment-Methode | Braze-Methode | Beispiel |
|---|---|---|
| [Track](https://segment.com/docs/spec/track/) | Als [angepasstes Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events) protokolliert. | Segment: `analytics.track("played_game");` <br>Braze: `Braze.logCustomEvent("played_game");` |
| [Track mit Eigenschaften](https://segment.com/docs/spec/track/) | Als [Event-Eigenschaft]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) protokolliert. | Segment: `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Braze: `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [Track mit Produkt](https://segment.com/docs/spec/track/) | Als [Kauf-Event]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web) protokolliert. | Segment: `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});` <br>Braze: `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Track" }

##### Bestellung abgeschlossen {#order-completed}

Wenn Sie ein Event mit dem Namen `Order Completed` unter Verwendung des in der [E-Commerce API](https://segment.com/docs/spec/ecommerce/v2/) von Segment beschriebenen Formats tracken, erfassen wir die Produkte, die Sie als [Käufe]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data) aufgeführt haben.

In den Zielen [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase) und [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase) kann die Standardabbildung über die Aktion „Track Purchase“ angepasst werden.

{% endtab %}

{% tab Page %}
#### Page {#page}

Der [Page](https://segment.com/docs/spec/page/)-Aufruf ermöglicht es Ihnen, aufzuzeichnen, wann immer Nutzer:innen eine Seite Ihrer Website sehen, zusammen mit allen optionalen Eigenschaften der Seite.

Dieser Event-Typ kann als Trigger in den Zielen Web Mode Actions und Cloud Actions verwendet werden, um ein angepasstes Event in Braze zu protokollieren.
{% endtab %}

{% endtabs %}

### Schritt 5: Integration testen {#step-5-test-your-integration}

Wenn Sie die Side-by-side-Integration (Gerätemodus) verwenden, können Ihre [Übersichtsmetriken]({{site.baseurl}}/user_guide/analytics/dashboards/home) (Lifetime-Sitzungen, MAU, DAU, Kundenbindung, tägliche Sitzungen und tägliche Sitzungen pro MAU) verwendet werden, um sicherzustellen, dass Braze Daten von Segment erhält.

Sie können Ihre Daten auf den Seiten für [angepasste Events]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data#custom-event-data) oder [Umsatz]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data) einsehen oder [ein Segment erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment). Auf der Dashboard-Seite **Angepasste Events** können Sie die Anzahl der angepassten Events im Zeitverlauf anzeigen. Beachten Sie, dass Sie keine [Formeln]({{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula#creating-a-formula) verwenden können, die MAU- und DAU-Statistiken enthalten, wenn Sie eine Server-zu-Server-Integration (Cloud-Modus) verwenden.

Wenn Sie Kaufdaten an Braze senden (siehe „Bestellung abgeschlossen“ im Tab **Track** in [Schritt 4](#methods)), können Sie auf der [Umsatz]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data)-Seite Daten zu Umsatz oder Käufen in bestimmten Zeiträumen oder den Gesamtumsatz Ihrer App einsehen.

[Ein Segment erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment) ermöglicht es Ihnen, Ihre Nutzer:innen auf der Grundlage der angepassten Event- und Attributdaten zu filtern.

{% alert important %}
Wenn Sie eine Server-zu-Server-Integration (Cloud-Modus) verwenden, funktionieren Filter, die sich auf automatisch gesammelte Sitzungsdaten beziehen (z. B. „App zuerst verwendet“ und „App zuletzt verwendet“), nicht. Verwenden Sie eine Side-by-side-Integration (Gerätemodus), wenn Sie diese in Ihrer Segment- und Braze-Integration verwenden möchten.
{% endalert %}

## Nutzer:innen löschen und unterdrücken {#user-deletion-and-suppression}

Wenn Sie Nutzer:innen löschen oder unterdrücken müssen, beachten Sie, dass das [Feature zum Löschen von Nutzer:innen](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to) von Segment auf den Braze-[`/users/delete`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) **abgebildet wird**. Beachten Sie, dass die Überprüfung dieser Löschungen bis zu 30 Tage dauern kann.

Sie müssen sicherstellen, dass Sie einen gemeinsamen Nutzer:innen-Bezeichner zwischen Braze und Segment auswählen (wie `external_id`). Nachdem Sie eine Löschanfrage mit Segment initiiert haben, können Sie den Status im Tab „Löschanfragen“ in Ihrem Segment-Dashboard einsehen.

## Segment Replays {#segment-replays}

Segment bietet einen Dienst für Kund:innen an, um alle historischen Daten an einen neuen Technologiepartner weiterzugeben. Neue Braze-Kund:innen, die alle relevanten historischen Daten importieren möchten, können dies über Segment tun. Sprechen Sie mit Ihrem Segment-Ansprechpartner, wenn Sie daran interessiert sind.

Segment stellt eine Verbindung zu unserem [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) her, um Nutzerdaten in Ihrem Namen in Braze zu importieren.

{% alert important %}
Alle Bezeichner, die im Cloud Mode Actions-Ziel unterstützt werden, werden als Teil von Segment Replays unterstützt.
{% endalert %}

## Bewährte Praktiken {#best-practices}

{% details Anwendungsfälle prüfen, um Mehrkosten bei den Daten zu vermeiden. %}

Segment schränkt die Anzahl der Datenelemente, die Kund:innen an sie senden, **nicht** ein. Segment ermöglicht es Ihnen, alle Events zu senden oder zu entscheiden, welche Events Sie an Braze senden. Anstatt alle Ihre Events über Segment zu senden, empfehlen wir Ihnen, mit Ihren Marketing- und Redaktionsteams Anwendungsfälle zu besprechen, um festzulegen, welche Events Sie an Braze senden, um Mehrkosten bei den Daten zu vermeiden.

{% enddetails %}

{% details Den Unterschied zwischen dem angepassten API-Endpunkt und dem angepassten REST API-Endpunkt in den Einstellungen des Mobile-Gerätemodus-Ziels verstehen. %}

| Braze-Terminologie | Segment-Äquivalent |
| ----------------- | ------------------ |
| Braze SDK-Endpunkt | Angepasster API-Endpunkt |
| Braze REST-Endpunkt | Angepasster REST API-Endpunkt |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bewährte Praktiken" }

Ihr Braze API-Endpunkt (in Segment als „Custom API Endpoint“ bezeichnet) ist der SDK-Endpunkt, den Braze für Ihr SDK einrichtet (zum Beispiel `sdk.iad-03.braze.com`). Ihr Braze REST API-Endpunkt (in Segment als „Custom REST API Endpoint“ bezeichnet) ist der REST API-Endpunkt (zum Beispiel `https://rest.iad-03.braze.com`).
{% enddetails %}

{% details Sicherstellen, dass der angepasste API-Endpunkt korrekt in den Einstellungen des Mobile-Gerätemodus-Ziels eingegeben wird. %}

| Braze-Terminologie | Segment-Äquivalent |
| ----------------- | ------------------ |
| Braze SDK-Endpunkt | Angepasster API-Endpunkt |
| Braze REST-Endpunkt | Angepasster REST API-Endpunkt |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bewährte Praktiken" }

Um sicherzustellen, dass Sie Ihren Braze SDK-Endpunkt korrekt eingeben, müssen Sie das richtige Format einhalten. Ihr Braze SDK-Endpunkt darf nicht `https://` enthalten (z. B. `sdk.iad-03.braze.com`), da sonst die Braze-Integration fehlschlägt. Dies ist erforderlich, da Segment Ihrem Endpunkt automatisch `https://` voranstellt, was dazu führt, dass Braze mit einem ungültigen Endpunkt `https://https://sdk.iad-03.braze.com` initialisiert wird.

{% enddetails %}

{% details Besonderheiten bei der Datenabbildung. %}

Szenarien, in denen die Daten nicht wie erwartet weitergeleitet werden:

1. Verschachtelte angepasste Attribute
  - Obwohl [verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support) technisch über Segment an Braze gesendet werden können, wird jedes Mal die **gesamte Nutzlast** gesendet. Dadurch entstehen jedes Mal, wenn die Nutzlast gesendet wird, [Datenpunkte]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support#data-points) pro im verschachtelten Objekt übergebenen Schlüssel.<br><br> Um nur eine Teilmenge der Datenpunkte beim Senden der Nutzlast auszugeben, können Sie das Feature der angepassten [Zielfunktionen](https://segment.com/docs/connections/functions/destination-functions/) von Segment verwenden. Dieses Feature in der Segment-Plattform ermöglicht es Ihnen, die Art und Weise, wie Daten an nachgelagerte Ziele gesendet werden, anzupassen.

  {% alert note %}
  Die Funktionen für angepasste Ziele werden innerhalb von Segment gesteuert, und Braze hat nur begrenzten Einblick in Funktionen, die extern konfiguriert wurden.
  {% endalert %}

{: start="2"}
2. Weitergabe anonymer Daten von Server zu Server.
  - Kund:innen können die Server-zu-Server-Bibliotheken von Segment nutzen, um anonyme Daten in andere Systeme zu leiten. Lesen Sie den Abschnitt zu Abbildungsmethoden, um mehr darüber zu erfahren, wie Sie Nutzer:innen ohne `external_id` über eine Server-zu-Server-Integration (Cloud-Modus) an Braze senden können.

{% enddetails %}

{% details Anpassung der Braze-Initialisierung. %}

Es gibt verschiedene Möglichkeiten, Braze anzupassen: Push, In-App-Nachrichten, Content Cards und Initialisierung. Bei einer Side-by-side-Integration können Sie Push, In-App-Nachrichten und Content Cards wie bei einer direkten Braze-Integration anpassen.

Die Anpassung der Integration des Braze SDK oder die Festlegung von Initialisierungskonfigurationen kann jedoch schwierig und manchmal nicht möglich sein. Das liegt daran, dass Segment das Braze SDK für Sie initialisiert, wenn die Segment-Initialisierung erfolgt.

{% enddetails %}

{% details Nur Änderungen (Deltas) an Braze senden. %}

Stellen Sie bei der Übergabe von Nutzer:innen-Attributdaten sicher, dass Sie nur Werte für Attribute übergeben, die sich seit dem letzten Update geändert haben. Dadurch wird die Aufzeichnung unnötiger Datenpunkte verhindert. Für clientseitige Quellen verwenden Sie das Open-Source-[Middleware](https://github.com/segmentio/segment-braze-mobile-middleware)-Tool von Segment, um Ihre Integration zu optimieren und die Datenpunkt-Nutzung zu begrenzen, indem Sie doppelte `identify()`-Aufrufe von Segment entprellen.

{% enddetails %}

{% details Das richtige Braze-Datenzentrum verwenden. %}

Segment verwendet Ihr Braze-Datenzentrum, um den entsprechenden Braze REST-Endpunkt (z. B. `https://rest.iad-01.braze.com`) für Server-zu-Server-Aufrufe abzurufen.

{% enddetails %}

{% details Den angepassten REST API-Endpunkt entfernen, wenn Sie den Event Tester von Segment verwenden. %}

Der Event Tester von Segment sendet Events an den Braze `/users/track` REST API-Endpunkt und gibt einen `401 Invalid API Key`-Fehler aus, wenn ein angepasster REST API-Endpunkt in den Braze-Zieleinstellungen festgelegt ist, selbst wenn dieser Endpunkt korrekt ist. Entfernen Sie den Wert des angepassten REST API-Endpunkts in Segment, damit der Event Tester ordnungsgemäß funktioniert.

{% enddetails %}

{% details Nach der Konfiguration einer neuen Quelle Zeit für Aktualisierungen einplanen. %}

Segment speichert Ihre Konfigurationseinstellungen lange im Cache. Wenn Sie eine neue Quelle konfigurieren (z. B. von Cloud- auf Gerätemodus wechseln), zeigt Ihre App möglicherweise erst dann neues Verhalten oder neue Daten, wenn der Cache erneuert wird. Berücksichtigen Sie diese Verzögerung, wenn Sie eine Quelle hinzufügen möchten.

{% enddetails %}