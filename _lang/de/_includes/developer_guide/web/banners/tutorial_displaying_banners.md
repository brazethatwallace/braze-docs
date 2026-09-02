## Voraussetzungen {#prerequisites}

Bevor Sie mit diesem Tutorial beginnen, überprüfen Sie, ob Ihr Braze SDK die Mindestanforderungen erfüllt:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Anzeige von Bannern für das Web SDK {#displaying-banners-for-the-web-sdk}

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Displaying Banners Web" %}

{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToBannersUpdates((banners) => {
  // Get this placement's banner. If it's `null`, the user did not qualify for any banners.
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  const container = document.getElementById("global-banner-container");

  braze.insertBanner(globalBanner, container);

  if (globalBanner.isControl) {
    // Hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

```html file=main.html
<!-- your html -->

<div id="global-banner-container" style="width: 100%; height: 450px;"></div>

<!-- ...the rest of your html -->
```

!!step
lines-index.js=5

### 1. Debugging aktivieren (optional) {#1-enable-debugging-optional}

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!!step
lines-index.js=8-23

### 2. Banner-Updates abonnieren {#2-subscribe-to-banner-updates}

Verwenden Sie `subscribeToBannersUpdates()`, um einen Handler zu Registrierung, der immer dann ausgeführt wird, wenn ein Banner aktualisiert wird. Rufen Sie innerhalb des Handlers `braze.getBanner("global_banner")` auf, um die neueste Platzierung abzurufen.

!!step
lines-index.js=15-22

### 3. Banner einfügen und Kontrollgruppen behandeln {#3-insert-the-banner-and-handle-control-groups}

Verwenden Sie `braze.insertBanner(banner, container)`, um ein Banner einzufügen, wenn es zurückgegeben wird. Damit Ihr Layout übersichtlich bleibt, blenden Sie Banner aus oder reduzieren Sie sie, die Teil einer Kontrollgruppe sind (zum Beispiel wenn `isControl` den Wert `true` hat).

!!step
lines-index.js=25

### 4. Banner aktualisieren {#4-refresh-your-banners}

Rufen Sie nach der Initialisierung des SDK `requestBannersRefresh(["global_banner", ...])` auf, um sicherzustellen, dass die Banner zu Beginn jeder Sitzung aktualisiert werden.

Sie können diese Funktion auch jederzeit aufrufen, um die Bannerplatzierungen später zu aktualisieren.

!!step
lines-main.html=3

### 5. Einen Container für Ihr Banner hinzufügen {#5-add-a-container-for-your-banner}

Fügen Sie in Ihrem HTML ein neues `<div>`-Element hinzu und geben Sie ihm eine kurze, bannerbezogene `id`, wie z. B. `global-banner-container`. Braze verwendet dieses `<div>`, um Ihr Banner auf der Seite einzufügen.

{% endscrolly %}