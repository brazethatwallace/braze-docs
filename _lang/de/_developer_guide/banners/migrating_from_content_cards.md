---
nav_title: "Von Content Cards migrieren"
article_title: "Von Content Cards zu Banner migrieren"
description: "Erfahren Sie, wie Sie von Content Cards zu Banner migrieren können, einschließlich Code-Beispielen für alle unterstützten SDKs, Einschränkungen und Vorteilen."
page_order: 5
toc_headers: h2
channel:
  - banners
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Von Content Cards zu Banner migrieren {#migrate-from-content-cards-to-banners}

> Dieser Leitfaden unterstützt Sie bei der Migration von Content Cards zu Bannern für Anwendungsfälle im Bereich des bannerartigen Messaging. Banner eignen sich ideal für Inline-Anzeigen, persistente In-App- und Web-Nachrichten, die an bestimmten Stellen in Ihrer App erscheinen.

## Warum zu Banner migrieren? {#why-migrate-to-banners}

- Wenn Ihr Entwicklerteam angepasste Content Cards erstellt oder pflegt, kann die Migration zu Banner diesen laufenden Aufwand reduzieren. Banner ermöglichen es Marketern, die UI direkt zu steuern, sodass Entwickler:innen für andere Aufgaben frei werden.
- Wenn Sie neue Homepage-Nachrichten, Onboarding-Flows oder persistente Ankündigungen einführen, starten Sie mit Banner anstatt auf Content Cards aufzubauen. Sie profitieren von Anfang an von Realtime-Personalisierung, keiner 30-Tage-Ablaufbegrenzung, keiner Größenbeschränkung und nativer Priorisierung.
- Wenn Sie die 30-Tage-Ablaufbegrenzung umgehen, komplexe Logik für erneute Berechtigung verwalten oder von veralteter Personalisierung frustriert sind – Banner löst diese Probleme nativ.

Banner bieten gegenüber Content Cards für bannerartige Nachrichten mehrere Vorteile:

### Beschleunigte Produktion {#accelerated-production}

- **Weniger laufender Engineering-Aufwand erforderlich**: Marketer können angepasste Nachrichten mit einem Drag-and-Drop-Editor und benutzerdefiniertem HTML erstellen, ohne Unterstützung von Entwickler:innen für die Anpassung zu benötigen.
- **Flexible Anpassungsoptionen**: Gestalten Sie direkt im Editor, verwenden Sie HTML oder nutzen Sie bestehende Datenmodelle mit angepassten Eigenschaften.

### Bessere UX {#better-ux}

- **Dynamische Content-Aktualisierungen**: Banner aktualisieren Liquid-Logik und Berechtigung bei jedem Refresh, sodass Nutzer:innen immer den relevantesten Content sehen.
- **Native Platzierungsunterstützung**: Nachrichten erscheinen in bestimmten Kontexten statt in einem Feed und bieten so eine bessere kontextuelle Relevanz.
- **Native Priorisierung**: Kontrolle über die Anzeigereihenfolge ohne angepasste Logik, was die Verwaltung der Nachrichtenhierarchie erleichtert.

### Persistenz {#persistence}

- **Keine Ablaufbegrenzung**: Banner-Campaigns haben keine 30-Tage-Ablaufbegrenzung wie Content Cards, was eine echte Persistenz von Nachrichten ermöglicht.

## Wann Sie migrieren sollten {#when-to-migrate}

Ziehen Sie eine Migration zu Banner in Betracht, wenn Sie Content Cards für Folgendes verwenden:

- Hero-Bereiche auf der Startseite, Aktionen auf Produktseiten, Angebote im Checkout
- Persistente Navigationshinweise oder Sidebar-Nachrichten
- Always-on-Nachrichten, die länger als 30 Tage laufen
- Nachrichten, bei denen Sie Realtime-Personalisierung und Berechtigungsprüfung wünschen

## Wann Sie Content Cards weiterhin verwenden sollten {#when-to-keep-content-cards}

Verwenden Sie weiterhin Content Cards, wenn Sie Folgendes benötigen:

- **Feed-Erlebnisse:** Jeder Anwendungsfall, der mehrere scrollbare Nachrichten oder einen kartenbasierten „Posteingang“ umfasst.
- **Bestimmte Features:** Nachrichten, die Aktionscodes erfordern, da Banner diese nicht nativ unterstützen. Banner unterstützen [Connected Content]({{site.baseurl}}/developer_guide/banners#connected-content) im Early Access.
- **Getriggerte Zustellung:** Anwendungsfälle, die zwingend eine API-getriggerte oder aktionsbasierte Zustellung erfordern. Obwohl Banner keine API-getriggerte oder aktionsbasierte Zustellung unterstützen, bedeutet die Echtzeit-Eignungsbewertung, dass Nutzer:innen bei jeder Aktualisierung sofort basierend auf der Segmentzugehörigkeit qualifiziert oder disqualifiziert werden.

## Migrationsleitfaden {#migration-guide}

### Voraussetzungen {#prerequisites}

Stellen Sie vor der Migration sicher, dass Ihr Braze SDK die Mindestversionsanforderungen erfüllt:

{% multi_lang_include developer_guide/sdk_versions.md feature='banners' %}

Für Dismissals und erneute Berechtigung sind die folgenden SDK-Mindestversionen erforderlich:

{% sdk_min_versions swift:14.1.0 android:42.1.0 web:6.7.1 %}

### Updates abonnieren {#subscribe-to-updates}

#### Content-Cards-Ansatz {#content-cards-approach}

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((cards) => {
  // Handle array of cards
  cards.forEach(card => {
    console.log("Card:", card.id);
  });
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToContentCardsUpdates { cards ->
  // Handle array of cards
  cards.forEach { card ->
    Log.d(TAG, "Card: ${card.id}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.contentCards.subscribeToUpdates { cards in
  // Handle array of cards
  for card in cards {
    print("Card: \(card.id)")
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
  const cards = update.cards;
  // Handle array of cards
  cards.forEach(card => {
    console.log("Card:", card.id);
  });
});
```
{% endtab %}
{% tab Flutter %}
```dart
StreamSubscription contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle array of cards
  for (final card in contentCards) {
    print("Card: ${card.id}");
  }
});
```
{% endtab %}
{% endtabs %}

#### Banner-Ansatz {#banners-approach}

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  // Get banner for specific placement
  const banner = braze.getBanner("sample_placement_id");
  if (banner) {
    console.log("Banner received for placement:", banner.placementId);
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  // Get banner for specific placement
  val banner = Braze.getInstance(context).getBanner("sample_placement_id")
  if (banner != null) {
    Log.d(TAG, "Banner received for placement: ${banner.placementId}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.subscribeToUpdates { banners in
  // Get banner for specific placement
  braze.banners.getBanner(for: "sample_placement_id") { banner in
    guard let banner = banner else { return }

    print("Banner received for placement: \(banner.placementId)")
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.BANNER_CARDS_UPDATED, (data) => {
  const banners = data.banners;
  // Get banner for specific placement
  Braze.getBanner("sample_placement_id").then(banner => {
    if (banner) {
      console.log("Banner received for placement:", banner.placementId);
    }
  });
});
```
{% endtab %}
{% tab Flutter %}
```dart
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
  // Get banner for specific placement
  braze.getBanner("sample_placement_id").then((banner) {
    if (banner != null) {
      print("Banner received for placement: ${banner.placementId}");
    }
  });
});
```
{% endtab %}
{% endtabs %}

### Inhalte anzeigen {#display-content}

{% alert note %}
Content Cards können manuell mit benutzerdefinierter UI-Logik gerendert werden, während Banner nur mit den mitgelieferten SDK-Methoden gerendert werden können.
{% endalert %}

#### Content-Cards-Ansatz

{% tabs %}
{% tab Web %}
```javascript
// Show default feed UI
braze.showContentCards(document.getElementById("feed"));

// Or manually render cards
const cards = braze.getCachedContentCards();
cards.forEach(card => {
  // Custom rendering logic
  if (card instanceof braze.ClassicCard) {
    // Render classic card
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
// Using default fragment
val fragment = ContentCardsFragment()
supportFragmentManager.beginTransaction()
  .replace(R.id.content_cards_container, fragment)
  .commit()

// Or manually render cards
val cards = Braze.getInstance(context).getCachedContentCards()
cards.forEach { card ->
  when (card) {
    is ClassicCard -> {
      // Render classic card
    }
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
// Using default view controller
let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
navigationController?.pushViewController(contentCardsController, animated: true)

// Or manually render cards
let cards = braze.contentCards.cards
for card in cards {
  switch card {
  case let card as Braze.ContentCard.Classic:
    // Render classic card
  default:
    break
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
// Launch default feed
Braze.launchContentCards();

// Or manually render cards
const cards = await Braze.getCachedContentCards();
cards.forEach(card => {
  if (card.type === 'CLASSIC') {
    // Render classic card
  }
});
```
{% endtab %}
{% tab Flutter %}
```dart
// Launch default feed
braze.launchContentCards();

// Or manually render cards
final cards = await braze.getContentCards();
for (final card in cards) {
  if (card.type == 'CLASSIC') {
    // Render classic card
  }
}
```
{% endtab %}
{% endtabs %}

#### Banner-Ansatz

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const banner = braze.getBanner("sample_placement_id");
  if (!banner) {
    return;
  }

  const container = document.getElementById("global-banner-container");
  braze.insertBanner(banner, container);

  if (banner.isControl) {
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% tab Android %}
```kotlin
// Using BannerView in XML
// <com.braze.ui.banners.BannerView
//     android:id="@+id/banner_view"
//     android:layout_width="match_parent"
//     android:layout_height="wrap_content"
//     app:placementId="sample_placement_id" />

// Or programmatically
val bannerView = BannerView(context).apply {
  placementId = "sample_placement_id"
}
container.addView(bannerView)

Braze.getInstance(context).requestBannersRefresh(listOf("sample_placement_id"))
```
{% endtab %}
{% tab Swift %}
```swift
// Using BannerUIView
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "sample_placement_id",
  braze: braze,
  processContentUpdates: { result in
    switch result {
    case .success(let updates):
      if let height = updates.height {
        // Update height constraint
      }
    case .failure:
      break
    }
  }
)
view.addSubview(bannerView)

braze.banners.requestBannersRefresh(placementIds: ["sample_placement_id"])
```
{% endtab %}
{% tab React Native %}
```javascript
// Using BrazeBannerView component
<Braze.BrazeBannerView
  placementId='sample_placement_id'
/>

// Or get banner data
const banner = await Braze.getBanner("sample_placement_id");
if (banner) {
  // Render custom banner UI
}

Braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% tab Flutter %}
```dart
// Using BrazeBannerView widget
BrazeBannerView(
  placementId: "sample_placement_id",
)

// Or get banner data
final banner = await braze.getBanner("sample_placement_id");
if (banner != null) {
  // Render custom banner UI
}

braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% endtabs %}

### Analytics protokollieren (benutzerdefinierte Implementierungen) {#log-analytics-custom-implementations}

{% alert note %}
Sowohl Content Cards als auch Banner erfassen Analytics automatisch, wenn ihre Standard-UI-Komponenten verwendet werden. Die folgenden Beispiele gelten für benutzerdefinierte Implementierungen, bei denen Sie Ihre eigene UI erstellen.
{% endalert %}

#### Content-Cards-Ansatz

{% tabs %}
{% tab Web %}
```javascript
// Manual impression logging required for custom implementations
cards.forEach(card => {
  braze.logContentCardImpressions([card]);
});

// Manual click logging required for custom implementations
card.logClick();
```
{% endtab %}
{% tab Android %}
```kotlin
// Manual impression logging required for custom implementations
cards.forEach { card ->
  card.logImpression()
}

// Manual click logging required for custom implementations
card.logClick()
```
{% endtab %}
{% tab Swift %}
```swift
// Manual impression logging required for custom implementations
for card in cards {
  card.context?.logImpression()
}

// Manual click logging required for custom implementations
card.context?.logClick()
```
{% endtab %}
{% tab React Native %}
```javascript
// Manual impression logging required for custom implementations
cards.forEach(card => {
  Braze.logContentCardImpression(card.id);
});

// Manual click logging required for custom implementations
Braze.logContentCardClicked(card.id);
```
{% endtab %}
{% tab Flutter %}
```dart
// Manual impression logging required for custom implementations
for (final card in cards) {
  braze.logContentCardImpression(card);
}

// Manual click logging required for custom implementations
braze.logContentCardClicked(card);
```
{% endtab %}
{% endtabs %}

#### Banner-Ansatz

{% tabs %}
{% tab Web %}

{% alert important %}
Analytics werden automatisch erfasst, wenn `insertBanner()` verwendet wird. Manuelles Logging sollte bei Verwendung von `insertBanner()` nicht eingesetzt werden.
{% endalert %}

```javascript
// Analytics are automatically tracked when using insertBanner()
// Manual logging should not be used when using insertBanner()

// For custom implementations, use manual logging methods:
// Log impression
braze.logBannerImpressions([banner]);

// Log click (with optional buttonId)
braze.logBannerClick("sample_placement_id", buttonId);
```
{% endtab %}
{% tab Android %}

{% alert important %}
Analytics werden automatisch erfasst, wenn BannerView verwendet wird. Manuelles Logging sollte bei Verwendung von BannerView nicht eingesetzt werden.
{% endalert %}

```kotlin
// Analytics are automatically tracked when using BannerView
// Manual logging should not be used for default BannerView

// For custom implementations, use manual logging methods:
// Log impression
Braze.getInstance(context).logBannerImpression("sample_placement_id");

// Log click (with optional buttonId)
Braze.getInstance(context).logBannerClick("sample_placement_id", buttonId);
```
{% endtab %}
{% tab Swift %}

{% alert important %}
Analytics werden automatisch erfasst, wenn BannerUIView verwendet wird. Manuelles Logging sollte bei der Standard-BannerUIView nicht eingesetzt werden.
{% endalert %}

```swift
// Analytics are automatically tracked when using BannerUIView
// Manual logging should not be used for default BannerUIView

// For custom implementations, use manual logging methods:
// Get banner for specific placement
braze.banners.getBanner(for: "sample_placement_id") { banner in
  guard let banner = banner else { return }

  // Log impression
  banner.context?.logImpression()

  // Log click (with optional buttonId)
  banner.context?.logClick(buttonId: buttonId)
}

// Control groups are automatically handled by BannerUIView
```
{% endtab %}
{% tab React Native %}

{% alert important %}
Analytics werden automatisch erfasst, wenn BrazeBannerView verwendet wird. Manuelles Logging ist nicht erforderlich.
{% endalert %}

```javascript
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in React Native
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% tab Flutter %}

{% alert important %}
Analytics werden automatisch erfasst, wenn BrazeBannerView verwendet wird. Manuelles Logging ist nicht erforderlich.
{% endalert %}

```dart
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in Flutter
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% endtabs %}

### Eigenschaften abrufen {#getting-properties}

#### Content-Cards-Ansatz

{% tabs %}
{% tab Web %}
```javascript
cards.forEach(card => {
  console.log("Card id:", card.id, "Extras:", card.extras);
});
```
{% endtab %}
{% tab Android %}
```kotlin
cards.forEach { card ->
  Log.d(TAG, "Card id: ${card.id} Extras: ${card.extras}")
}
```
{% endtab %}
{% tab Swift %}
```swift
for card in cards {
  print("Card id: \(card.id) Extras: \(card.extras)")
}
```
{% endtab %}
{% tab React Native %}
```javascript
cards.forEach(card => {
  console.log("Card id:", card.id, "Extras:", card.extras);
});
```
{% endtab %}
{% tab Flutter %}
```dart
for (final card in cards) {
  print("Card id: ${card.id} Extras: ${card.extras}");
}
```
{% endtab %}
{% endtabs %}

#### Banner-Ansatz

{% tabs %}
{% tab Web %}
```javascript
const banner = braze.getBanner("sample_placement_id");
if (!banner) {
  return;
}

console.log("Banner placement:", banner.placementId, "Properties:", banner.properties);
```
{% endtab %}
{% tab Android %}
```kotlin
val banner = Braze.getInstance(context).getBanner("sample_placement_id")
if (banner != null) {
  Log.d(TAG, "Banner placement: ${banner.placementId} Properties: ${banner.properties}")
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.getBanner(for: "sample_placement_id") { banner in
  guard let banner = banner else { return }

  print("Banner placement: \(banner.placementId) Properties: \(banner.properties)")
}
```
{% endtab %}
{% tab React Native %}
```javascript
const banner = await Braze.getBanner("sample_placement_id");
if (banner) {
  console.log("Banner placement:", banner.placementId, "Properties:", banner.properties);
}
```
{% endtab %}
{% tab Flutter %}
```dart
final banner = await braze.getBanner("sample_placement_id");
if (banner != null) {
  print("Banner placement: ${banner.placementId} Properties: ${banner.properties}");
}
```
{% endtab %}
{% endtabs %}

### Kontrollgruppen handhaben {#handling-control-groups}

#### Content-Cards-Ansatz

{% tabs %}
{% tab Web %}
```javascript
cards.forEach(card => {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
cards.forEach { card ->
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
for card in cards {
  if card.isControl {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
cards.forEach(card => {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
});
```
{% endtab %}
{% tab Flutter %}
```dart
for (final card in cards) {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% endtabs %}

#### Banner-Ansatz

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const banner = braze.getBanner("sample_placement_id");
  if (!banner) {
    return;
  }

  const container = document.getElementById("global-banner-container");

  // Always call insertBanner to track impression (including control)
  braze.insertBanner(banner, container);

  // Hide if control group
  if (banner.isControl) {
    container.style.display = "none";
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
// BannerView automatically handles control groups
// No additional code needed
val bannerView = BannerView(context).apply {
  placementId = "sample_placement_id"
}
```
{% endtab %}
{% tab Swift %}
```swift
// BannerUIView automatically handles control groups
// No additional code needed
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "sample_placement_id",
  braze: braze
)
```
{% endtab %}
{% tab React Native %}
```javascript
// BrazeBannerView automatically handles control groups
// No additional code needed
<Braze.BrazeBannerView
  placementId='sample_placement_id'
/>
```
{% endtab %}
{% tab Flutter %}
```dart
// BrazeBannerView automatically handles control groups
// No additional code needed
BrazeBannerView(
  placementId: "sample_placement_id",
)
```
{% endtab %}
{% endtabs %}

## Einschränkungen {#limitations}

Beachten Sie bei der Migration von Content Cards zu Banner die folgenden Einschränkungen:

### Migration getriggerter Nachrichten {#migrating-triggered-messages}

Banner unterstützen nur Campaigns mit geplanter Zustellung. Um eine Nachricht zu migrieren, die zuvor API-getriggert oder aktionsbasiert war, konvertieren Sie sie in segmentbasiertes Targeting:

- **Beispiel:** Anstatt eine „Profil vervollständigen“-Karte über die API zu triggern, erstellen Sie ein Segment für Nutzer:innen, die sich in den letzten 7 Tagen registriert, aber ihr Profil noch nicht vervollständigt haben.
- **Realtime-Berechtigung:** Nutzer:innen qualifizieren oder disqualifizieren sich bei jeder Aktualisierung sofort für das Banner, basierend auf ihrer Segmentzugehörigkeit.

### Feature-Unterschiede {#feature-differences}

| Feature | Content Cards | Banner |
|---------|--------------|---------|
| **Content-Struktur** |
| Mehrere Karten im Feed | ✅ Unterstützt | ✅ Es können mehrere Placements erstellt werden, um eine Karussell-ähnliche Implementierung zu erreichen. Pro Placement wird nur ein Banner zurückgegeben. |
| Mehrere Placements | N/A | ✅ Mehrere Placements unterstützt |
| Kartentypen (Classic, Captioned, Image Only) | ✅ Mehrere vordefinierte Typen | ✅ Einzelnes HTML-basiertes Banner (flexibler) |
| **Content-Verwaltung** |
| Drag-and-Drop-Editor | ❌ Erfordert Entwickler:in für Anpassungen | ✅ Marketer können ohne Entwicklerteam erstellen/aktualisieren |
| Benutzerdefiniertes HTML/CSS | ❌ Auf Kartenstruktur beschränkt | ✅ Volle HTML/CSS-Unterstützung |
| Schlüssel-Wert-Paare für Anpassungen | ✅ Erforderlich für erweiterte Anpassungen | ✅ Stark typisierte Schlüssel-Wert-Paare namens „Properties“ für erweiterte Anpassungen |
| Message Extras | ✅ Unterstützt | ❌ Derzeit nicht unterstützt |
| **Persistenz und Ablauf** |
| Kartenablauf | ✅ Unterstützt (30-Tage-Limit) | ✅ Unterstützt (kein Ablauflimit) |
| Echte Persistenz | ❌ Maximal 30 Tage | ✅ Unbegrenzte Persistenz |
| **Anzeige und Targeting** |
| Feed-UI | ✅ Standard-Feed verfügbar | ❌ Nur Placement-basiert |
| Kontextspezifisches Placement | ❌ Feed-basiert | ✅ Natives Placement unterstützt |
| Priorisierung | ❌ Erfordert benutzerdefinierte Logik | ✅ Native Priorisierung |
| **Nutzer:innen-Interaktion** |
| Manuelles Schließen | ✅ Unterstützt | ✅ Unterstützt |
| Erneute Berechtigung nach Schließen | ❌ Erfordert benutzerdefinierte Filter oder Campaign-Logik | ✅ Standard-Wartezeit |
| Gepinnte Karten | ✅ Unterstützt | N/A |
| **Analytics** |
| Automatische Analytics (Standard-UI) | ✅ Unterstützt | ✅ Unterstützt |
| Prioritätssortierung | ❌ Nicht unterstützt | ✅ Unterstützt |
| **Content-Aktualisierungen** |
| Liquid-Templating-Aktualisierung | ❌ Einmal pro Karte beim Senden/Start | ✅ Aktualisiert bei jeder Aktualisierung |
| Berechtigungsaktualisierung | ❌ Einmal pro Karte beim Senden/Start | ✅ Aktualisiert bei jeder Sitzung |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Feature-Unterschiede" }

### Produkteinschränkungen {#product-limitations}

- Bis zu 25 aktive Nachrichten pro Placement.
- Bis zu 10 Placement-IDs pro Aktualisierungsanfrage; darüber hinausgehende Anfragen werden abgeschnitten.

### SDK-Einschränkungen {#sdk-limitations}

- Banner werden derzeit nicht auf .NET MAUI (Xamarin), Cordova, Unity, Vega oder TV-Plattformen unterstützt.
- Stellen Sie sicher, dass Sie die in den Voraussetzungen aufgeführten Mindest-SDK-Versionen verwenden.

## Verwandte Artikel {#related-articles}

- [Banner-Platzierungen]({{site.baseurl}}/developer_guide/banners/placements)
- [Tutorial: Ein Banner anhand der Platzierungs-ID anzeigen]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Banner-Analytics]({{site.baseurl}}/developer_guide/banners/analytics)
- [Banner-FAQ]({{site.baseurl}}/developer_guide/banners/faq)