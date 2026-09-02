---
nav_title: Platzierungen verwalten
article_title: Bannerplatzierungen verwalten
description: "Erfahren Sie, wie Sie Bannerplatzierungen im Braze SDK erstellen und verwalten, einschließlich des Zugriffs auf deren eindeutige Eigenschaften und der Protokollierung von Impressionen."
page_order: 2
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Bannerplatzierungen verwalten {#manage-banner-placements}

> Erfahren Sie, wie Sie Bannerplatzierungen im Braze SDK erstellen und verwalten, einschließlich des Zugriffs auf deren eindeutige Eigenschaften und der Protokollierung von Impressionen. Weitere allgemeine Informationen finden Sie unter [Über Banner]({{site.baseurl}}/developer_guide/banners).

## Über Platzierungsanfragen {#requests}

{% multi_lang_include banners/placement_requests.md %}

## Placement erstellen {#create-a-placement}

### Voraussetzungen {#prerequisites}

Dies sind die mindestens erforderlichen SDK-Versionen, um Banner-Placements zu erstellen:

{% multi_lang_include developer_guide/sdk_versions.md feature='banners' %}

{% multi_lang_include banners/creating_placements.md section="developer" %}

### Schritt 2: Placements in Ihrer App aktualisieren {#requestBannersRefresh}

Um Placements zu aktualisieren, rufen Sie die Aktualisierungsmethode für Ihr SDK auf (`requestBannersRefresh()` bei Web und Android oder `requestRefresh()` bei Swift).

Das Aktualisierungsverhalten von Bannern hat zwei Pfade:

1. **Explizite Aktualisierung:** Sie können die Aktualisierungsmethode jederzeit während einer aktiven Sitzung aufrufen.
2. **Automatische Aktualisierung bei einer neuen Sitzung:** Nachdem Sie mindestens eine explizite Aktualisierungsanfrage gestellt haben, kann das SDK die zuletzt angeforderten Placement-IDs erneut anfordern, wenn eine neue Braze-Sitzung beginnt (zum Beispiel nach `changeUser()` oder nach einem Sitzungs-Timeout).

Die Rolle von `subscribeToBannersUpdates()` unterscheidet sich je nach Plattform:

- **iOS und Android:** `subscribeToBannersUpdates()` (oder `subscribeToUpdates()` bei Swift) registriert einen Update-Callback. Die automatische Aktualisierung beim Sitzungsstart ist nicht davon abhängig, dass das Abo aktiv ist.
- **Web:** Die automatische Aktualisierung beim Sitzungsstart ist an die Registrierung von `subscribeToBannersUpdates()` gebunden. Ohne ein aktives Abo wiederholt das SDK die Aktualisierung bei einer neuen Sitzung nicht automatisch.

In allen Fällen müssen Sie mindestens eine explizite Aktualisierungsanfrage pro App-Lebenszyklus stellen, damit das SDK weiß, welche Placement-IDs aktuell gehalten werden sollen. Banner werden beim ersten Start nicht automatisch abgerufen, wenn dieser initiale Aufruf fehlt, und die verfolgten Placement-IDs werden nach einem Neustart der App zurückgesetzt.

Automatische Aktualisierungen beim Sitzungsstart verbrauchen kein Rate-Limiting-Token / Textbaustein.

{% alert tip %}
Aktualisieren Sie Placements so früh wie möglich, um Verzögerungen beim Herunterladen oder Anzeigen von Bannern zu vermeiden.
{% endalert %}

{% tabs %}
{% tab Web %}

```javascript
import * as braze from "@braze/web-sdk";

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Swift %}

```swift
AppDelegate.braze?.banners.requestRefresh(placementIds: ["global_banner", "navigation_square_banner"])
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
ArrayList<String> listOfBanners = new ArrayList<>();
listOfBanners.add("global_banner");
listOfBanners.add("navigation_square_banner");
Braze.getInstance(context).requestBannersRefresh(listOfBanners);
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).requestBannersRefresh(listOf("global_banner", "navigation_square_banner"))
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
Braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}

```dart
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Schritt 3: Auf Updates lauschen {#subscribeToBannersUpdates}

{% alert tip %}
Wenn Sie Banner mithilfe der SDK-Methoden in dieser Anleitung einfügen, werden alle Analytics-Ereignisse (wie Impressionen und Klicks) automatisch verarbeitet, und Impressionen werden nur protokolliert, wenn das Banner sichtbar ist.
{% endalert %}

{% tabs %}
{% tab Web %}
{% subtabs %}
{% subtab JavaScript %}
Wenn Sie Vanilla JavaScript mit dem Web-Braze-SDK verwenden, nutzen Sie [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates), um auf Placement-Updates zu lauschen, und rufen Sie dann [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh) auf, um sie abzurufen.

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  console.log("Banners were updated");
});

// always refresh after your subscriber function has been registered
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}
{% subtab React %}
Wenn Sie React mit dem Web-Braze-SDK verwenden, richten Sie [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates) innerhalb eines `useEffect`-Hooks ein und rufen Sie [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh) nach der Registrierung Ihres Listeners auf.

```typescript
import * as braze from "@braze/web-sdk";

useEffect(() => {
  const subscriptionId = braze.subscribeToBannersUpdates((banners) => {
    console.log("Banners were updated");
  });

  // always refresh after your subscriber function has been registered
  braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);

  // cleanup listeners
  return () => {
    braze.removeSubscription(subscriptionId);
  }
}, []);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Swift %}

{% alert note %}
Ihr Banner-Update-Listener spiegelt den In-Memory-Banner-Zustand des SDK wider. Ein einzelnes Update kann Placements enthalten, die bereits zwischengespeichert waren (zum Beispiel von einer früheren Aktualisierung, einem anderen Bildschirm oder automatischer SDK-Arbeit), nicht nur die Placement-IDs aus Ihrem letzten `requestRefresh`-Aufruf. Wenn Sie sich nur für bestimmte Placements interessieren, prüfen Sie die Placement-ID jedes Banners in Ihrem Listener und überspringen Sie den Rest. Nachdem Sie Ihren Listener registriert haben, rufen Sie `requestRefresh` für die Placements auf, die Sie von Braze synchronisieren möchten.
{% endalert %}

```swift
let placementIds = ["global_banner", "navigation_square_banner"]
let cancellable = brazeClient.braze()?.banners.subscribeToUpdates { banners in
  banners.forEach { placementId, banner in
    print("Received banner: \(banner) with placement ID: \(placementId)")
  }
}
// Always refresh after your subscriber is registered
brazeClient.braze()?.banners.requestRefresh(placementIds: placementIds)
```

{% endtab %}
{% tab Android %}

{% alert note %}
Ihr Banner-Update-Listener spiegelt den In-Memory-Banner-Zustand des SDK wider. Ein einzelnes Update kann Placements enthalten, die bereits zwischengespeichert waren (zum Beispiel von einer früheren Aktualisierung, einem anderen Bildschirm oder automatischer SDK-Arbeit), nicht nur die Placement-IDs aus Ihrem letzten `requestBannersRefresh`-Aufruf. Wenn Sie sich nur für bestimmte Placements interessieren, prüfen Sie die Placement-ID jedes Banners in Ihrem Listener und überspringen Sie den Rest. Nachdem Sie Ihren Listener registriert haben, rufen Sie `requestBannersRefresh` für die Placements auf, die Sie von Braze synchronisieren möchten.
{% endalert %}

{% subtabs %}
{% subtab Java %}

```java
ArrayList<String> placementIds = new ArrayList<>();
placementIds.add("global_banner");
placementIds.add("navigation_square_banner");
Braze.getInstance(context).subscribeToBannersUpdates(banners -> {
  for (Banner banner : banners.getBanners()) {
    Log.d(TAG, "Received banner: " + banner.getPlacementId());
  }
});
// Always refresh after your subscriber is registered
Braze.getInstance(context).requestBannersRefresh(placementIds);
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val placementIds = listOf("global_banner", "navigation_square_banner")
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  for (banner in update.banners) {
    Log.d(TAG, "Received banner: " + banner.placementId)
  }
}
// Always refresh after your subscriber is registered
Braze.getInstance(context).requestBannersRefresh(placementIds)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
const bannerCardsSubscription = Braze.addListener(
  Braze.Events.BANNER_CARDS_UPDATED,
  (data) => {
    const banners = data.banners;
    console.log(
      `Received ${banners.length} Banner Cards with placement IDs:`,
      banners.map((banner) => banner.placementId)
    );
  }
);
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}

```dart
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
  for (final banner in banners) {
    print("Received banner: " + banner.toString());
  }
});
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Schritt 4: Mithilfe der Placement-ID einfügen {#insertBanner}

{% alert tip %}
Eine vollständige Schritt-für-Schritt-Anleitung finden Sie unter [Ein Banner anhand der Placement-ID anzeigen]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners).
{% endalert %}

{% tabs %}
{% tab Web %}

Erstellen Sie ein Container-Element für das Banner. Stellen Sie sicher, dass Sie dessen Breite und Höhe festlegen.

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

{% subtabs local %}
{% subtab JavaScript %}
Wenn Sie Vanilla JavaScript mit dem Web-Braze-SDK verwenden, rufen Sie die Methode [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) auf, um das innere HTML des Container-Elements zu ersetzen.

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("sdk-api-key", {
  baseUrl: "sdk-base-url",
  allowUserSuppliedJavascript: true, // banners require you to opt-in to user-supplied javascript
});

braze.subscribeToBannersUpdates((banners) => {
  // get this placement's banner. If it's `null` the user did not qualify for one.
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  // choose where in the DOM you want to insert the banner HTML
  const container = document.getElementById("global-banner-container");

  // Insert the banner which replaces the innerHTML of that container
  braze.insertBanner(globalBanner, container);

  // Special handling if the user is part of a Control Variant
  if (globalBanner.isControl) {
    // hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}

{% subtab React %}
Wenn Sie React mit dem Web-Braze-SDK verwenden, rufen Sie die Methode [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) mit einer `ref` auf, um das innere HTML des Container-Elements zu ersetzen.

```tsx
import { useRef } from 'react';
import * as braze from "@braze/web-sdk";

export default function App() {
    const bannerRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
       const globalBanner = braze.getBanner("global_banner");
       if (!globalBanner || globalBanner.isControl) {
           // hide the container
       } else {
           // insert the banner to the container node
           braze.insertBanner(globalBanner, bannerRef.current);
       }
    }, []);
    return <div ref={bannerRef}></div>
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Um Impressionen zu erfassen, stellen Sie sicher, dass Sie `insertBanner` auch für `isControl` aufrufen. Sie können den Container danach ausblenden oder zusammenklappen.
{% endalert %}

{% endtab %}
{% tab Swift %}

```swift
// To get access to the Banner model object:
let globalBanner: Braze.Banner?
AppDelegate.braze?.banners.getBanner(for: "global_banner", { banner in
  self.globalBanner = banner
})

// UIKit implementation:
// If you simply want the Banner view, initialize a `UIView` with the placement ID:
if let braze = AppDelegate.braze {
  let bannerUIView = BrazeBannerUI.BannerUIView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
}

// SwiftUI implementation:
// Similarly, if you want a Banner view in SwiftUI, use the corresponding `BannerView` initializer:
if let braze = AppDelegate.braze {
  let bannerView = BrazeBannerUI.BannerView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height according to your parent controller.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
}
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}
Um das Banner in Java-Code zu erhalten, verwenden Sie:

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

Sie können Banner in Ihren Android-Views-Layouts erstellen, indem Sie dieses XML einbinden:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```
{% endsubtab %}

{% subtab Kotlin %}
Wenn Sie Android Views verwenden, nutzen Sie dieses XML:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

Um Jetpack Compose zu verwenden, fügen Sie das Artefakt `com.braze:android-sdk-jetpack-compose` zu Ihrem App-Modul hinzu. Verwenden Sie die gleiche Version wie Ihre anderen Braze Android SDK-Abhängigkeiten. Dieses Modul ist von `android-sdk-ui` getrennt und stellt das [`Banner`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.banners/-banner.html)-Composable unter `com.braze.jetpackcompose.banners` bereit.

{% alert note %}
Einige Compose-UI-Bibliotheken definieren ihr eigenes `Banner`-Composable. Importieren Sie `com.braze.jetpackcompose.banners.Banner` explizit, damit Sie die API von Braze aufrufen.
{% endalert %}

```kotlin
import com.braze.jetpackcompose.banners.Banner

@Composable
fun myBannerSlot() {
    Banner(placementId = "global_banner")
}
```

Optional können Sie `heightCallback` übergeben, um die gerenderte Höhe in dp zu erhalten, wenn sich die Bannergröße ändert. Weitere Informationen finden Sie in der [KDoc für `Banner`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.banners/-banner.html).

Wenn Sie das Jetpack-Compose-Modul nicht hinzufügen, umschließen Sie [`BannerView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/index.html) mit [`AndroidView`](https://developer.android.com/reference/kotlin/androidx/compose/ui/viewinterop/AndroidView):

```kotlin
import android.view.ViewGroup
import androidx.compose.runtime.Composable
import androidx.compose.ui.viewinterop.AndroidView
import com.braze.ui.banners.BannerView

@Composable
fun myBannerSlot() {
    AndroidView(
        factory = { context ->
            BannerView(context, "global_banner").apply {
                layoutParams = ViewGroup.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    ViewGroup.LayoutParams.WRAP_CONTENT
                )
            }
        },
        update = { it.placementId = "global_banner" }
    )
}
```

Um das Banner in Kotlin zu erhalten, verwenden Sie:
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

Wenn Sie die [New Architecture von React Native](https://reactnative.dev/architecture/landing-page) verwenden, müssen Sie `BrazeBannerView` als Fabric-Komponente in Ihrer `AppDelegate.mm` registrieren.

```swift
#ifdef RCT_NEW_ARCH_ENABLED
/// Register the `BrazeBannerView` for use as a Fabric component.
- (NSDictionary<NSString *,Class<RCTComponentViewProtocol>> *)thirdPartyFabricComponents {
  NSMutableDictionary * dictionary = [super thirdPartyFabricComponents].mutableCopy;
  dictionary[@"BrazeBannerView"] = [BrazeBannerView class];
  return dictionary;
}
#endif
```
Für die einfachste Integration fügen Sie das folgende JavaScript-XML-Snippet (JSX) in Ihre View-Hierarchie ein und geben Sie lediglich die Placement-ID an.

```javascript
<Braze.BrazeBannerView
  placementId='global_banner'
/>
```

Um das Datenmodell des Banners in React Native zu erhalten oder zu prüfen, ob dieses Placement im Cache Ihrer Nutzer:innen vorhanden ist, verwenden Sie:

```javascript
const banner = await Braze.getBanner("global_banner");
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}
Für die einfachste Integration fügen Sie das folgende Widget in Ihre View-Hierarchie ein und geben Sie lediglich die Placement-ID an.

```dart
BrazeBannerView(
  placementId: "global_banner",
),
To get the Banner's data model in Flutter, use:
```

Sie können die Methode `getBanner` verwenden, um zu prüfen, ob dieses Placement im Cache Ihrer Nutzer:innen vorhanden ist.

```dart
braze.getBanner("global_banner").then((banner) {
  if (banner == null) {
    // Handle null cases.
  } else {
    print(banner.toString());
  }
});
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Schritt 5: Ein Test-Banner senden (optional) {#handling-test-cards}

Bevor Sie eine Banner-Campaign starten, können Sie [ein Test-Banner senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=banners), um Ihre Integration zu überprüfen. Test-Banner werden in einem separaten In-Memory-Cache gespeichert und bleiben nicht über App-Neustarts hinweg bestehen. Es ist kein zusätzliches Setup erforderlich, aber Ihr Testgerät muss in der Lage sein, Push-Benachrichtigungen im Vordergrund zu empfangen, damit der Test angezeigt werden kann.

{% alert note %}
Test-Banner verhalten sich wie alle anderen Banner, werden jedoch bei der nächsten App-Sitzung entfernt.
{% endalert %}

## Impressionen protokollieren {#log-impressions}

Braze protokolliert automatisch Impressionen für Banner, die sichtbar sind, wenn Sie SDK-Methoden verwenden, um ein Banner einzufügen&#8212;eine manuelle Erfassung von Impressionen ist daher nicht erforderlich.

## Klicks protokollieren {#logging-clicks}

Welche Methode zum Protokollieren von Banner-Klicks verwendet wird, hängt davon ab, wie Ihr Banner gerendert wird und wo sich Ihr Klick-Handler befindet.

### Standard-Banner-Inhalte (automatisch) {#standard-banner-content-automatic}

Wenn Sie standardmäßige, sofort einsatzbereite SDK-Methoden zum Einfügen von Bannern verwenden und Ihr Banner Standard-Editor-Komponenten (Bilder, Buttons, Text) nutzt, werden Klicks automatisch erfasst. Das SDK fügt diesen Elementen Klick-Listener hinzu, und es ist kein zusätzlicher Code erforderlich.

### Custom-Code-Blöcke {#custom-code-blocks}

Wenn Ihr Banner den **Custom Code**-Editor-Block im Braze-Dashboard verwendet, müssen Sie `brazeBridge.logClick()` nutzen, um Klicks aus diesem angepassten HTML heraus zu protokollieren. Dies gilt auch dann, wenn Sie SDK-Methoden zum Rendern des Banners verwenden, da das SDK keine Listener automatisch an Elemente innerhalb Ihres angepassten Codes anhängen kann.

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

Die vollständige Referenz finden Sie unter [Angepasster Code und JavaScript-Pont für Banner]({{site.baseurl}}/user_guide/channels/banners/custom_code). Die `brazeBridge` stellt eine Kommunikationsschicht zwischen dem internen HTML des Banners und dem übergeordneten Braze SDK bereit.

### Angepasste UI-Implementierungen (Headless) {#custom-ui-implementations-headless}

Wenn Sie eine vollständig angepasste UI auf Basis der [angepassten Eigenschaften](#custom-properties) des Banners erstellen, anstatt das Banner-HTML zu rendern, müssen Sie Klicks und Impressionen manuell aus Ihrem Anwendungscode protokollieren. Da das SDK das Banner nicht rendert, kann es Interaktionen mit Ihren angepassten UI-Elementen nicht automatisch erfassen.

Methodensignaturen und vollständige Details finden Sie in der [Braze SDK-Referenzdokumentation]({{site.baseurl}}/developer_guide/references).

#### Impressionen protokollieren {#logging-impressions}

Rufen Sie die plattformspezifische Methode für Banner-Impressionen auf, wenn Ihre angepasste UI das Banner als „angesehen“ betrachtet. Implementieren Sie eine robuste Logik dafür, was als Impression zählt, um doppelte Ereignisse zu vermeiden – protokollieren Sie beispielsweise nur, wenn das Banner in den sichtbaren Bereich gelangt (oder ein Äquivalent), und protokollieren Sie nicht erneut, wenn dasselbe Banner zurück in den sichtbaren Bereich gescrollt wird oder wenn Ihre Komponente ohne ein neues Anzeigeereignis neu gerendert wird.

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
const banner = braze.getBanner("placement_id_homepage_top");
if (banner) {
  braze.logBannerImpressions([banner]);
}
```
[Web SDK-Referenz](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logbannerimpressions)
{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Kotlin %}
```kotlin
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.getInstance(context).logBannerImpression("placement_id_homepage_top")
```
{% endsubtab %}
{% subtab Java %}
```java
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.getInstance(context).logBannerImpression("placement_id_homepage_top");
```
{% endsubtab %}
{% endsubtabs %}
[Android SDK-Referenz](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-banner-impression.html)
{% endtab %}
{% tab Swift %}
```swift
// Retrieve a banner and log an impression on it (for example, once when it enters viewport)
braze.banners.getBanner(for: "placement_id_homepage_top") { banner in
  banner?.context.logImpression()
}
```
[Swift SDK-Referenz](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/banner/context-swift.class/logimpression())
{% endtab %}
{% tab React Native %}
```javascript
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.logBannerImpression("placement_id_homepage_top");
```
Die aktuellen Methodensignaturen finden Sie im [React Native SDK-Repository](https://github.com/braze-inc/braze-react-native-sdk).
{% endtab %}
{% tab Flutter %}
```dart
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
braze.logBannerImpression("placement_id_homepage_top");
```
[Flutter SDK-Referenz](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazePlugin/logBannerImpression.html)
{% endtab %}
{% endtabs %}

#### Klicks protokollieren

Rufen Sie die plattformspezifische Methode für Banner-Klicks auf, wenn Nutzer:innen auf Ihr angepasstes Banner (oder einen bestimmten Button) tippen. Übergeben Sie die optionale `buttonId`, wenn der Klick auf einen bestimmten Button erfolgt, damit die Analytics den Klick korrekt zuordnen können.

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

// Log click
braze.logBannerClick("placement_id_homepage_top", buttonId);  // buttonID is optional
```
[Web SDK-Referenz](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logbannerclick)
{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Kotlin %}
```kotlin
// Log click
Braze.getInstance(context).logBannerClick("placement_id_homepage_top", buttonId)  // buttonID parameter can be null
```
{% endsubtab %}
{% subtab Java %}
```java
// Log click
Braze.getInstance(context).logBannerClick("placement_id_homepage_top", buttonId);  // buttonID parameter can be null
```
{% endsubtab %}
{% endsubtabs %}
[Android SDK-Referenz](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-banner-click.html)
{% endtab %}
{% tab Swift %}
```swift
// Retrieve a banner and log a click on it
braze.banners.getBanner(for: "placement_id_homepage_top") { banner in
  banner?.context.logClick(buttonId: buttonId)  // buttonID is optional
}
```
[Swift SDK-Referenz](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/banner/context-swift.class/logclick(buttonid:))
{% endtab %}
{% tab React Native %}
```javascript
// Log click
Braze.logBannerClick("placement_id_homepage_top", buttonId);  // buttonID is optional
```
Die aktuellen Methodensignaturen finden Sie im [React Native SDK-Repository](https://github.com/braze-inc/braze-react-native-sdk).
{% endtab %}
{% tab Flutter %}
```dart
// Log click
braze.logBannerClicked("placement_id_homepage_top", buttonId);  // buttonID parameter can be null
```
[Flutter SDK-Referenz](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazePlugin/logBannerClicked.html)
{% endtab %}
{% endtabs %}

## Schließen protokollieren {#log-dismissals}

Das Schließen von Bannern entfernt ein Banner programmatisch von einer Platzierung, wenn Nutzer:innen es aktiv schließen. Nach dem Schließen wird das Banner für diese:n Nutzer:in unterdrückt. Beim nächsten Aktualisieren der Platzierungsliste wird ein neues Banner zurückgegeben, wenn die:der Nutzer:in für eines berechtigt ist.

### Voraussetzungen

Dies sind die Mindestversionen des SDK, die zum Protokollieren des Schließens von Bannern erforderlich sind:

{% sdk_min_versions swift:14.1.0 android:42.1.0 web:6.7.1 %}

### Integrationen {#integrations}

#### Standard-Banner-Integrationen (Drag-and-Drop-Editor) {#standard-banner-integrations-drag-and-drop-editor}

Wenn Ihr Banner den Drag-and-Drop-Editor verwendet und eine Schließen-Button-Komponente enthält, ist kein zusätzlicher Code erforderlich. Wenn Nutzer:innen auf den Schließen-Button klicken, wird die Nachricht ausgeblendet, ein Schließen-Ereignis ausgelöst und anschließend ein Schließen-Ereignis für Analytics aufgezeichnet.

#### Benutzerdefinierte Code-Blöcke

Wenn Ihr Banner den **Custom Code**-Editor-Block verwendet, können Sie ein Schließen direkt aus dem HTML des Banners mit `brazeBridge.closeMessage()` auslösen.

```html
<button onclick="brazeBridge.closeMessage()">
  Dismiss
</button>
```

#### Ein Banner programmatisch schließen {#dismiss-a-banner-programmatically}

Wenn Sie die Standard-`BrazeBannerView` mit dem im Drag-and-Drop-Editor erstellten Schließen-Button verwenden, ist kein zusätzlicher Code erforderlich; das Schließen wird automatisch behandelt.

Für benutzerdefinierte UI-Integrationen können Sie die Dismiss-Methode direkt auf Ihrer Braze-Instanz aufrufen, um ein Banner programmatisch zu schließen und ein Schließen-Ereignis zu protokollieren. Die Dismiss-Methode kann sicher mehrfach aufgerufen werden – das SDK ignoriert doppelte Aufrufe für dasselbe Banner.

Dies sind die Mindestversionen des SDK, die zum programmatischen Schließen eines Banners erforderlich sind:

{% sdk_min_versions swift:15.1.0 android:42.3.0 web:6.9.0 reactnative:22.0.0 flutter:20.0.0 %}

{% tabs %}
{% tab Web %}
Übergeben Sie das `Banner`-Objekt an `braze.dismissBanner()`. Sie können das `Banner`-Objekt von `braze.getAllBanners()` oder aus einem `subscribeToBannersUpdates`-Callback erhalten.

{% subtabs %}
{% subtab JavaScript %}
```javascript
import * as braze from "@braze/web-sdk";

const banners = braze.getAllBanners();
const banner = banners["global_banner"];

if (banner) {
  braze.dismissBanner(banner);
}
```
{% endsubtab %}
{% subtab React %}
```typescript
import * as braze from "@braze/web-sdk";

const banners = braze.getAllBanners();
const banner = banners["global_banner"];

if (banner) {
  braze.dismissBanner(banner);
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Android %}
{% subtabs %}
{% subtab Java %}
```java
Braze.getInstance(context).dismissBanner("your-placement-id");
```
{% endsubtab %}
{% subtab Kotlin %}
```kotlin
Braze.getInstance(context).dismissBanner("your-placement-id")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift %}

Verwenden Sie `dismiss()` auf dem Kontext des Banners, wenn verfügbar. Diese Methode ist idempotent und löst den `onDismiss`-Callback automatisch aus. Wenn der Kontext nicht verfügbar ist, rufen Sie `dismiss(using:)` direkt auf dem Banner auf. Beide Methoden müssen vom Hauptthread aufgerufen werden.

```swift
// Preferred: dismiss via context.
banner.context?.dismiss()

// Fallback: if context is unavailable.
banner.dismiss(using: braze)
```

In Objective-C sind diese als `[banner.context dismiss]` und `[banner dismissUsing:braze]` verfügbar.

{% endtab %}

{% tab React Native %}
```javascript
Braze.dismissBanner("your-placement-id");
```
{% endtab %}

{% tab Flutter %}
```dart
braze.dismissBanner("your-placement-id");
```
{% endtab %}
{% endtabs %}

### Benutzerdefinierte Analytics beim Schließen eines Banners protokollieren {#log-custom-analytics-on-banner-dismissal}

Um benutzerdefinierte Logik auszuführen, wenn ein Banner geschlossen wird – beispielsweise das Protokollieren von Analytics – verwenden Sie den Dismiss-Callback für Ihr SDK. Der Callback erhält ein Ereignisobjekt mit der `placementId`, dem `stableKey` und der `trackingId` des Banners.

{% tabs %}
{% tab Web %}
Verwenden Sie [`Banner.subscribeToDismissedEvent()`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.banner.html#subscribetodismissedevent), um benutzerdefinierte Logik auszuführen, wenn ein bestimmtes Banner geschlossen wird. Abonnieren Sie das Ereignis, bevor Sie das Banner anzeigen.

{% alert note %}
`Banner.subscribeToDismissedEvent()` erfordert Web SDK 6.9.0 oder höher. Bei früheren Versionen verwenden Sie `braze.subscribeToBannersUpdates()` und erkennen das Schließen, indem Sie prüfen, ob das Banner in der aktualisierten Banner-Map nicht mehr vorhanden ist.
{% endalert %}

{% subtabs %}
{% subtab JavaScript %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  const banner = banners["global_banner"];

  if (banner) {
    banner.subscribeToDismissedEvent(() => {
      // Run any custom logic here, such as logging custom analytics
      console.log("Banner was dismissed");
    });
  }
});

braze.requestBannersRefresh(["global_banner"]);
```
{% endsubtab %}
{% subtab React %}
```typescript
import { useEffect } from "react";
import * as braze from "@braze/web-sdk";

useEffect(() => {
  const subscriptionId = braze.subscribeToBannersUpdates((banners) => {
    const banner = banners["global_banner"];

    if (banner) {
      banner.subscribeToDismissedEvent(() => {
        // Run any custom logic here, such as logging custom analytics
        console.log("Banner was dismissed");
      });
    }
  });

  braze.requestBannersRefresh(["global_banner"]);

  return () => {
    braze.removeSubscription(subscriptionId);
  };
}, []);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Android %}
Setzen Sie die optionale [`onDismissCallback`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/on-dismiss-callback.html)-Eigenschaft auf [`BannerView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/index.html).

{% subtabs %}
{% subtab Java %}

```java
import android.util.Log;
import com.braze.ui.banners.BannerView;
import kotlin.Unit;

// After obtaining your BannerView instance (for example from XML via findViewById, or `new BannerView(context, "global_banner")`)

bannerView.setOnDismissCallback((snapshot) -> {
  Log.d(TAG, "placementId: " + snapshot.getPlacementId()
    + ", stableKey: " + snapshot.getStableKey()
    + ", trackingId: " + snapshot.getTrackingId());

  // Run any custom logic here, such as logging custom analytics
  return Unit.INSTANCE;
});
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
import android.util.Log
import com.braze.ui.banners.BannerView

// After obtaining your BannerView instance (for example via findViewById or `BannerView(context, "global_banner")`)

bannerView.onDismissCallback = { snapshot ->
  Log.d(TAG, "placementId: ${snapshot.placementId}, stableKey: ${snapshot.stableKey}, trackingId: ${snapshot.trackingId}")

  // Run any custom logic here, such as logging custom analytics
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift %}
```swift
// After initializing your banner view instance using UIKit or SwiftUI

bannerView.onDismiss = { event in
  print("Banner dismissed — placementId: \(event.placementId ?? "unknown")")
  print("  stableKey: \(event.stableKey ?? "unknown")")
  print("  trackingId: \(event.trackingId ?? "unknown")")

  // Run any custom logic here, such as logging custom analytics
}
```
{% endtab %}

{% tab React Native %}
Setzen Sie die `onDismiss`-Prop auf `Braze.BrazeBannerView`, um benutzerdefinierte Logik auszuführen, wenn ein Banner geschlossen wird.

```javascript
import Braze from "@braze/react-native-sdk";

<Braze.BrazeBannerView
  placementId="global_banner"
  onDismiss={(event) => {
    console.log("placementId:", event.placementId, "stableKey:", event.stableKey, "trackingId:", event.trackingId);
    // Run any custom logic here, such as logging custom analytics
  }}
/>
```
{% endtab %}

{% tab Flutter %}
Setzen Sie den `onDismiss`-Parameter auf `BrazeBannerView`, um benutzerdefinierte Logik auszuführen, wenn ein Banner geschlossen wird.

```dart
BrazeBannerView(
  placementId: 'global_banner',
  onDismiss: (BrazeBannerDismissEvent event) {
    print('placementId: ${event.placementId}, stableKey: ${event.stableKey}, trackingId: ${event.trackingId}');
    // Run any custom logic here, such as logging custom analytics
  },
)
```
{% endtab %}
{% endtabs %}

### Speicherlimit für ausstehende Schließen-Ereignisse {#pending-dismissal-storage-cap}

Schließen-Ereignisse werden lokal als ausstehende Einträge gespeichert, bis sie beim nächsten `requestBannersRefresh`-Aufruf mit dem Braze-Server synchronisiert werden können.

{% alert warning %}
In seltenen Fällen, in denen eine große Anzahl von Schließen-Ereignissen ohne erfolgreiche Synchronisierung anfällt, können ältere ausstehende Schließen-Ereignisse verworfen werden. In diesem Fall können zuvor geschlossene Banner wieder erscheinen, bis die nächste erfolgreiche Synchronisierung abgeschlossen ist. Um dieses Risiko zu minimieren, rufen Sie `requestBannersRefresh` auf, wenn Ihre App die Netzwerkverbindung wiederherstellt.
{% endalert %}

## Abmessungen und Größe {#dimensions-and-sizing}

Folgendes sollten Sie über die Abmessungen und Größe von Bannern wissen:

- Der Composer ermöglicht zwar eine Vorschau von Bannern in verschiedenen Abmessungen, diese Informationen werden jedoch weder gespeichert noch an das SDK gesendet.
- Das HTML nimmt die volle Breite des Containers ein, in dem es gerendert wird.
- Wir empfehlen, ein Element mit festen Abmessungen zu erstellen und diese Abmessungen im Composer zu testen.

## Benutzerdefinierte Eigenschaften {#custom-properties}

Sie können benutzerdefinierte Eigenschaften aus Ihrer Banner-Campaign verwenden, um Schlüssel-Wert-Daten über das SDK abzurufen und das Verhalten oder das Erscheinungsbild Ihrer App anzupassen. Beispielsweise könnten Sie:

{% multi_lang_include banners/metadata_use_cases.md %}

### Voraussetzungen

Sie müssen Ihrer Banner-Campaign [benutzerdefinierte Eigenschaften hinzufügen]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#custom-properties). Darüber hinaus sind dies die erforderlichen Mindestversionen des SDK, um auf benutzerdefinierte Eigenschaften zugreifen zu können:

{% sdk_min_versions swift:13.1.0 android:38.0.0 web:6.1.0 reactnative:17.0.0 flutter:15.1.0 %}

### Auf benutzerdefinierte Eigenschaften zugreifen {#access-custom-properties}

Um auf die benutzerdefinierten Eigenschaften eines Banners zuzugreifen, verwenden Sie eine der folgenden Methoden basierend auf dem im Dashboard definierten Typ der Eigenschaft. Wenn der Schlüssel nicht mit einer Eigenschaft dieses Typs übereinstimmt oder nicht existiert, gibt die Methode `null` zurück.

{% tabs local %}
{% tab Web %}
```javascript
// Returns the Banner instance
const banner = braze.getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner) {

  // Returns the string property
  const stringProperty = banner.getStringProperty("color");

  // Returns the boolean property
  const booleanProperty = banner.getBooleanProperty("expanded");

  // Returns the number property
  const numberProperty = banner.getNumberProperty("height");

  // Returns the timestamp property (as a number)
  const timestampProperty = banner.getTimestampProperty("account_start");

  // Returns the image URL property as a string of the URL
  const imageProperty = banner.getImageProperty("homepage_icon");

  // Returns the JSON object property
  const jsonObjectProperty = banner.getJsonProperty("footer_settings");
}
```
{% endtab %}

{% tab Swift %}
```swift
// Passes the specified banner to the completion handler
AppDelegate.braze?.banners.getBanner(for: "placement_id_homepage_top") { banner in
  // Returns the string property
  let stringProperty: String? = banner.stringProperty(key: "color")

  // Returns the boolean property
  let booleanProperty: Bool? = banner.boolProperty(key: "expanded")

  // Returns the number property as a double
  let numberProperty: Double? = banner.numberProperty(key: "height")

  // Returns the Unix UTC millisecond timestamp property as an integer
  let timestampProperty: Int? = banner.timestampProperty(key: "account_start")

  // Returns the image property as a String of the image URL
  let imageProperty: String? = banner.imageProperty(key: "homepage_icon")

  // Returns the JSON object property as a [String: Any] dictionary
  let jsonObjectProperty: [String: Any]? = banner.jsonObjectProperty(key: "footer_settings")
}
```
{% endtab %}

{% tab Android %}
{% subtabs %}
{% subtab Java %}
```java
// Returns the Banner instance
Banner banner = Braze.getInstance(context).getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner != null) {
  // Returns the string property
  String stringProperty = banner.getStringProperty("color");

  // Returns the boolean property
  Boolean booleanProperty = banner.getBooleanProperty("expanded");

  // Returns the number property
  Number numberProperty = banner.getNumberProperty("height");

  // Returns the timestamp property (as a Long)
  Long timestampProperty = banner.getTimestampProperty("account_start");

  // Returns the image URL property as a String of the URL
  String imageProperty = banner.getImageProperty("homepage_icon");

  // Returns the JSON object property as a JSONObject
  JSONObject jsonObjectProperty = banner.getJSONProperty("footer_settings");
}
```
{% endsubtab %}

{% subtab Kotlin %}
```kotlin
// Returns the Banner instance
val banner: Banner = Braze.getInstance(context).getBanner("placement_id_homepage_top") ?: return

// Returns the string property
val stringProperty: String? = banner.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = banner.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = banner.getNumberProperty("height")

// Returns the timestamp property (as a Long)
val timestampProperty: Long? = banner.getTimestampProperty("account_start")

// Returns the image URL property as a String of the URL
val imageProperty: String? = banner.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = banner.getJSONProperty("footer_settings")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab React Native %}

```javascript
// Get the Banner instance
const banner = await Braze.getBanner('placement_id_homepage_top');
if (!banner) return;

// Get the string property
const stringProperty = banner.getStringProperty('color');

// Get the boolean property
const booleanProperty = banner.getBooleanProperty('expanded');

// Get the number property
const numberProperty = banner.getNumberProperty('height');

// Get the timestamp property (as a number)
const timestampProperty = banner.getTimestampProperty('account_start');

// Get the image URL property as a string
const imageProperty = banner.getImageProperty('homepage_icon');

// Get the JSON object property
const jsonObjectProperty = banner.getJSONProperty('footer_settings');
```

{% endtab %}
{% tab Flutter %}

```dart
// Fetch the banner asynchronously
_braze.getBanner(placementId).then(('placement_id_homepage_top') {
  // Get the string property
  final String? stringProperty = banner?.getStringProperty('color');

  // Get the boolean property
  final bool? booleanProperty = banner?.getBooleanProperty('expanded');

  // Get the number property
  final num? numberProperty = banner?.getNumberProperty('height');

  // Get the timestamp property
  final int? timestampProperty = banner?.getTimestampProperty('account_start');

  // Get the image URL property
  final String? imageProperty = banner?.getImageProperty('homepage_icon');

  // Get the JSON object property
  final Map<String, dynamic>? jsonObjectProperty = banner?.getJSONProperty('footer_settings');

  // Use these properties as needed in your UI or logic
});
```

{% endtab %}
{% endtabs %}