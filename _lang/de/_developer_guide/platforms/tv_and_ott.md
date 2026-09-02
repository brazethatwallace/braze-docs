---
nav_title: TV und OTT
article_title: TV- und OTT-Integrationen für Braze
page_order: 15

description: "In diesem Artikel erfahren Sie mehr über die TV- und OTT-Features von Braze, Integrationen, verfügbare Plattformen und weitere Möglichkeiten."
platform:
  - tvOS
  - Roku
  - Web
  - Android
  - FireOS
---

# TV- und OTT-Integrationen {#tv-and-ott-integrations}

> So wie sich die Technologie mit neuen Plattformen und Geräten weiterentwickelt, kann auch Ihr Messaging mit Braze mitwachsen! Braze bietet verschiedene Engagement-Kanäle für eine Reihe von TV-Betriebssystemen und Over-the-Top (OTT)-Methoden zur Inhaltsbereitstellung.

## Plattformen und Features {#platforms-and-features}

Die folgende Tabelle fasst die Unterstützung von Messaging-Kanälen für gängige TV- und OTT-Plattformen zusammen. Alle Plattformen unterstützen außerdem Daten und Analytics, Canvas sowie Feature-Flags. Für Kindle Fire gelten dieselben Hinweise wie für Amazon Fire TV. Für Apple Vision Pro siehe [visionOS-Unterstützung]({{site.baseurl}}/developer_guide/platforms/swift/visionos).

<style>
#tv-feature-table td,
#tv-feature-table th {
    text-align: center;
    vertical-align: middle;
    word-break: normal;
    overflow-wrap: normal;
    hyphens: none;
}

#tv-feature-table td:first-child,
#tv-feature-table th:first-child {
    text-align: left;
}

</style>
<table aria-label="Unterstützung von TV- und OTT-Messaging-Kanälen" id="tv-feature-table">
  <caption>Unterstützung von TV- und OTT-Messaging-Kanälen</caption>
    <thead>
        <tr>
            <th>Gerätetyp</th>
            <th>SDK</th>
            <th>In-App-Nachrichten</th>
            <th>Content Cards</th>
            <th>Push-Benachrichtigungen</th>
            <th>Banner</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amazon Fire TV</td>
            <td><a href="https://github.com/braze-inc/braze-vega-sdk">Vega SDK</a></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Unterstützt</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Unterstützt</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Unterstützt</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Nur Headless</span></td>
        </tr>
        <tr>
            <td>Android TV</td>
            <td><a href="https://github.com/braze-inc/braze-android-sdk">Android SDK</a></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Unterstützt</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Unterstützt</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Unterstützt</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Nur Headless</span></td>
        </tr>
        <tr>
            <td>LG TV (webOS)</td>
            <td><a href="https://github.com/braze-inc/braze-web-sdk">Web SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Nur Headless</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Nur Headless</span></td>
            <td><span aria-hidden="true">➖</span><span class="sr-only">Von der OTT-Plattform nicht unterstützt</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Nur Headless</span></td>
        </tr>
        <tr>
            <td>Samsung Tizen TV</td>
            <td><a href="https://github.com/braze-inc/braze-web-sdk">Web SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Nur Headless</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Nur Headless</span></td>
            <td><span aria-hidden="true">➖</span><span class="sr-only">Von der OTT-Plattform nicht unterstützt</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Nur Headless</span></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td><a href="https://github.com/braze-inc/braze-roku-sdk">Roku SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Nur Headless</span></td>
            <td><span aria-hidden="true">❌</span><span class="sr-only">Von Braze nicht unterstützt</span></td>
            <td><span aria-hidden="true">➖</span><span class="sr-only">Von der OTT-Plattform nicht unterstützt</span></td>
            <td><span aria-hidden="true">❌</span><span class="sr-only">Von Braze nicht unterstützt</span></td>
        </tr>
        <tr>
            <td>Apple TV OS (tvOS)</td>
            <td><a href="https://github.com/braze-inc/braze-swift-sdk">Swift SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Nur Headless</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Nur Headless</span></td>
            <td><span aria-hidden="true">❌</span><span class="sr-only">Von Braze nicht unterstützt</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Nur Headless</span></td>
        </tr>
    </tbody>
</table>

- <span aria-hidden="true">✅</span> = Unterstützt
- <span aria-hidden="true">🔧</span> = Nur Headless (Sie müssen eine angepasste UI erstellen)
- <span aria-hidden="true">➖</span> = Von der OTT-Plattform nicht unterstützt
- <span aria-hidden="true">❌</span> = Von Braze nicht unterstützt

## Integrationsleitfäden {#integration-guides}

### Amazon Fire TV {#fire-tv}

Verwenden Sie das Braze Fire OS SDK zur Integration mit Amazon Fire TV-Geräten.

Zu den Features gehören:

- Daten- und Analytics-Erfassung für kanalübergreifendes Engagement
- Push-Benachrichtigungen (bekannt als [„Heads Up Notifications“](https://developer.amazon.com/docs/fire-tv/notifications.html#headsup))
  - Die Priorität muss auf „HIGH“ gesetzt werden, damit diese angezeigt werden. Alle Benachrichtigungen erscheinen im Fire TV-Einstellungsmenü.
- Content Cards
- Feature-Flags
- In-App-Nachrichten
  - Um HTML-Nachrichten in Umgebungen ohne Touchscreen wie Fernsehern anzuzeigen, setzen Sie `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` auf `false` (verfügbar ab [Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))
- Banner
  - Verwenden Sie [Banner-Platzierungen]({{site.baseurl}}/developer_guide/banners/placements), um Nachrichten direkt in Ihre Fire TV-App einzubetten.

Weitere Informationen finden Sie im [Fire OS-Integrationsleitfaden]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android).

### Kindle Fire {#kindle-fire}

Verwenden Sie das Braze Fire OS SDK zur Integration mit Amazon Kindle Fire-Geräten.

Zu den Features gehören:

- Daten- und Analytics-Erfassung für kanalübergreifendes Engagement
- Push-Benachrichtigungen
- Content Cards
- Feature-Flags
- In-App-Nachrichten
- Banner
  - Verwenden Sie [Banner-Platzierungen]({{site.baseurl}}/developer_guide/banners/placements), um Nachrichten direkt in Ihr Kindle Fire einzubetten.

Weitere Informationen finden Sie im [Fire OS-Integrationsleitfaden]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android).

### Android TV {#android-tv}

Verwenden Sie das Braze Android SDK zur Integration mit Android TV-Geräten.

Zu den Features gehören:

- Daten- und Analytics-Erfassung für kanalübergreifendes Engagement
- Content Cards
- Feature-Flags
- In-App-Nachrichten
  - Um HTML-Nachrichten in Umgebungen ohne Touchscreen wie Fernsehern anzuzeigen, setzen Sie `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` auf `false` (verfügbar ab [Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))
- &#42; Push-Benachrichtigungen (manuelle Integration erforderlich)
  - Push-Benachrichtigungen werden auf Android TV nicht nativ unterstützt. Warum das so ist, erfahren Sie in Googles [Design Guidelines](https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html). Sie können jedoch **eine manuelle Integration der Push-Benachrichtigungs-UI vornehmen, um dies zu erreichen**. In unserer [Dokumentation]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android%20tv) erfahren Sie, wie Sie dies einrichten.
- Banner
  - Verwenden Sie [Banner-Platzierungen]({{site.baseurl}}/developer_guide/banners/placements), um Nachrichten direkt in Ihre Android TV-App einzubetten.

Weitere Informationen finden Sie im [Android SDK-Integrationsleitfaden]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android).

{% alert note %}
Stellen Sie sicher, dass Sie im Dashboard eine neue Android-App für Ihre Android-OTT-Integration erstellen.
{% endalert %}

### LG webOS {#lg-webos}

Verwenden Sie das Braze Web SDK zur Integration mit [LG webOS-Fernsehern](https://webostv.developer.lge.com/discover).

Zu den Features gehören:

- Daten- und Analytics-Erfassung für kanalübergreifendes Engagement
- Content Cards (über [Headless UI](#custom-ui))
- Feature-Flags
- In-App-Nachrichten (über [Headless UI](#custom-ui))
- Banner
  - Verwenden Sie [Banner-Platzierungen]({{site.baseurl}}/developer_guide/banners/placements), um Nachrichten direkt in Ihre webOS-App einzubetten.

Weitere Informationen finden Sie im [Web-Smart-TV-Integrationsleitfaden]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs).

### Samsung Tizen {#tizen}

Verwenden Sie das Braze Web SDK zur Integration mit [Samsung Tizen-Fernsehern](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html).

Zu den Features gehören:

- Daten- und Analytics-Erfassung für kanalübergreifendes Engagement
- Content Cards (über [Headless UI](#custom-ui))
- Feature-Flags
- In-App-Nachrichten (über [Headless UI](#custom-ui))
- Banner
  - Verwenden Sie [Banner-Platzierungen]({{site.baseurl}}/developer_guide/banners/placements), um Nachrichten direkt in Ihre Tizen-App einzubetten.

Weitere Informationen finden Sie im [Web-Smart-TV-Integrationsleitfaden]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs).

### Roku {#roku}

Verwenden Sie das Braze Roku SDK zur Integration mit [Roku-Fernsehern](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md).

Zu den Features gehören:

- Daten- und Analytics-Erfassung für kanalübergreifendes Engagement
- In-App-Nachrichten (über [Headless UI](#custom-ui))
  - Webviews werden von der Roku-Plattform nicht unterstützt, daher werden HTML-In-App-Nachrichten ebenfalls nicht unterstützt.
- Feature-Flags

Weitere Informationen finden Sie im [Roku-Integrationsleitfaden]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=roku).

### Apple TV OS {#tvos}

Verwenden Sie das Braze Swift SDK zur Integration mit tvOS. Beachten Sie, dass das Swift SDK keine Standard-UI oder -Views für tvOS enthält, sodass Sie Ihre eigene Implementierung erstellen müssen.

Zu den Features gehören:

- Daten- und Analytics-Erfassung für kanalübergreifendes Engagement
- Content Cards (über [Headless UI](#custom-ui))
- Feature-Flags
- In-App-Nachrichten (über [Headless UI](#custom-ui))
  - Webviews werden von der tvOS-Plattform nicht unterstützt, daher werden HTML-In-App-Nachrichten ebenfalls nicht unterstützt.
  - Sehen Sie sich unsere [Beispiel-App](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui) an, um mehr über die Verwendung einer Headless UI für angepasstes Messaging auf tvOS zu erfahren.
- Stille Push-Benachrichtigungen und Badge-Aktualisierung
- Banner
  - Verwenden Sie [Banner-Platzierungen]({{site.baseurl}}/developer_guide/banners/placements), um Nachrichten direkt in Ihre tvOS-App einzubetten.

Weitere Informationen finden Sie im [iOS Swift SDK-Integrationsleitfaden](https://github.com/braze-inc/braze-swift-sdk).

{% alert note %}
Um zu vermeiden, dass Ihren TV-Nutzer:innen mobile In-App-Nachrichten angezeigt werden, richten Sie entweder [App Targeting](#app-targeting) ein oder verwenden Sie Schlüssel-Wert-Paare, um Nachrichten herauszufiltern. Zeigen Sie beispielsweise tvOS-Nachrichten nur an, wenn sie ein spezielles Schlüssel-Wert-Paar `tv = true` enthalten.
{% endalert %}

### Apple Vision Pro {#vision-pro}

Verwenden Sie das Braze Swift SDK zur Integration mit visionOS. Die meisten auf iOS verfügbaren Features sind auch auf visionOS verfügbar, darunter:

- Analytics (Sitzungen, angepasste Events, Käufe usw.)
- In-App-Nachrichten (Datenmodelle und UI)
- Content Cards (Datenmodelle und UI)
- Push-Benachrichtigungen (für Nutzer:innen sichtbar mit Aktions-Buttons und stille Benachrichtigungen)
- Feature-Flags
- Standort-Analytics
- Banner
  - Verwenden Sie [Banner-Platzierungen]({{site.baseurl}}/developer_guide/banners/placements), um Nachrichten direkt in Ihre visionOS-App einzubetten.

Weitere Informationen finden Sie im [iOS Swift SDK-Integrationsleitfaden](https://github.com/braze-inc/braze-swift-sdk).

{% alert important %}
Einige iOS-Features werden nur teilweise oder gar nicht unterstützt. Die vollständige Liste finden Sie unter [visionOS-Unterstützung]({{site.baseurl}}/developer_guide/platforms/swift/visionos).
{% endalert %}

## App-Targeting {#app-targeting}

Für das Targeting von OTT-Apps für Messaging empfehlen wir die Erstellung eines Segments speziell für Ihre OTT-App.

![Ein Segment, das mit der Android-OTT-App erstellt wurde.]({% image_buster /assets/img/android_ott.png %})

## Headless UI {#custom-ui}

{% alert important %}
Plattformen, die In-App-Nachrichten oder Content Cards über eine Headless UI unterstützen, enthalten **keine** Standard-UI oder -Ansichten. Erstellen Sie Ihre eigene angepasste Benutzeroberfläche (z. B. für In-App-Nachrichten) und verwenden Sie anschließend die vom SDK bereitgestellten Datenmodelle, um diese Benutzeroberflächen zu befüllen.
{% endalert %}

Mit Headless UI stellt Braze ein Datenmodell bereit, z. B. JSON, das Ihre App lesen und innerhalb einer UI verwenden kann, die Ihre App steuert. Diese Daten enthalten die im Dashboard konfigurierten Felder (Titel, Textkörper, Button-Text, Farben usw.), die Ihre App lesen und entsprechend anzeigen kann. Weitere Informationen zum angepassten Handling von Nachrichten finden Sie unter:

**Android SDK**
- [In-App-Nachrichten anpassen]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android#android_setting-custom-manager-listeners)
- [Content Cards anpassen]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style)

**Swift SDK**
- [In-App-Nachrichten anpassen](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/)
- [Beispiel-App für Headless UI](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui)
- [Content Cards anpassen](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/)

**Web SDK**
- [In-App-Nachrichten anpassen]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web)
- [Content Cards anpassen]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style)