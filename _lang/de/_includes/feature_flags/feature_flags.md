# Feature-Flags

> Feature-Flags ermöglichen es Ihnen, Funktionen für eine bestimmte oder zufällige Auswahl von Nutzer:innen aus der Ferne zu aktivieren oder zu deaktivieren. Wichtig ist, dass Sie damit ein Feature in der Produktion ein- und ausschalten können, ohne zusätzlichen Code zu implementieren oder Updates im App Store durchzuführen. Dies erlaubt es Ihnen, neue Features sicher und zuverlässig einzuführen.

{% alert tip %}
Wenn Sie bereit sind, Ihre eigenen Feature-Flags zu erstellen, lesen Sie den Abschnitt [Feature-Flags erstellen]({{site.baseurl}}/developer_guide/feature_flags/create).
{% endalert %}

## Voraussetzungen {#prerequisites}

Dies sind die erforderlichen SDK-Mindestversionen, um Feature-Flags nutzen zu können:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## Anwendungsfälle {#use-cases}

### Schrittweise Einführung {#gradual-rollouts}

Verwenden Sie Feature-Flags, um Features schrittweise für eine Stichprobe Ihrer Nutzer:innen zu aktivieren. So können Sie beispielsweise ein neues Feature zunächst nur für Ihre VIP-Nutzer:innen freigeben. Diese Strategie hilft, Risiken zu minimieren, die mit der gleichzeitigen Bereitstellung neuer Features für alle Nutzer:innen verbunden sind, und ermöglicht es, Fehler frühzeitig zu erkennen.

![Animiertes Bild eines Rollout-Reglers, der von 0 % auf 100 % verschoben wird.]({% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %})

Angenommen, wir haben beschlossen, einen neuen Link „Live-Chat-Support“ in unserer App hinzuzufügen, um einen schnelleren Kundenservice zu ermöglichen. Wir könnten dieses Feature für alle Kund:innen gleichzeitig freigeben. Eine breite Freigabe birgt jedoch Risiken, wie zum Beispiel:

* Unser Support-Team befindet sich noch in der Schulung, und Kund:innen können nach der Freigabe bereits Support-Tickets erstellen. Das lässt uns keinen Spielraum, falls das Support-Team mehr Zeit benötigt.
* Wir sind uns über das tatsächliche Volumen neuer Support-Anfragen nicht sicher, sodass wir möglicherweise nicht angemessen besetzt sind.
* Wenn unser Support-Team überlastet ist, haben wir keine Strategie, um dieses Feature schnell wieder zu deaktivieren.
* Es könnten Fehler im Chat-Widget auftreten, und wir möchten nicht, dass Kund:innen eine negative Erfahrung machen.

Mit Braze Feature-Flags können wir das Feature stattdessen schrittweise einführen und all diese Risiken minimieren:

* Wir werden das Feature „Live-Chat-Support“ aktivieren, wenn das Support-Team bereit ist.
* Wir werden dieses neue Feature nur für 10 % der Nutzer:innen aktivieren, um zu prüfen, ob wir angemessen besetzt sind.
* Falls Fehler auftreten, können wir das Feature schnell deaktivieren, anstatt überstürzt ein neues Release zu veröffentlichen.

Für die schrittweise Einführung dieses Features können wir ein [Feature-Flag erstellen]({{site.baseurl}}/developer_guide/feature_flags/create) mit dem Namen „Live Chat Widget“.

![Feature-Flag-Details für ein Beispiel mit dem Namen „Live Chat Widget“. Die ID ist enable_live_chat. Die Beschreibung des Feature-Flags lautet, dass das Live-Chat-Widget auf der Support-Seite angezeigt wird.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %})

In unserem App-Code zeigen wir den Button **Start Live Chat** nur an, wenn das Braze Feature-Flag aktiviert ist:

{% tabs %}
{% tab JavaScript %}

```javascript
import {useState} from "react";
import * as braze from "@braze/web-sdk";

// Get the initial value from the Braze SDK
const featureFlag = braze.getFeatureFlag("enable_live_chat");
const [liveChatEnabled, setLiveChatEnabled] = useState(featureFlag.enabled);

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(() => {
    const newValue = braze.getFeatureFlag("enable_live_chat").enabled;
    setLiveChatEnabled(newValue);
});

// Only show the Live Chat if the Braze SDK determines it is enabled
return (<>
  Need help? <button>Email Our Team</button>
  {liveChatEnabled && <button>Start Live Chat</button>}
</>)
```

{% endtab %}
{% tab Java %}

```java
// Get the initial value from the Braze SDK
FeatureFlag featureFlag = braze.getFeatureFlag("enable_live_chat");
Boolean liveChatEnabled = featureFlag != null && featureFlag.getEnabled();

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(event -> {
  FeatureFlag newFeatureFlag = braze.getFeatureFlag("enable_live_chat");
  Boolean newValue = newFeatureFlag != null && newFeatureFlag.getEnabled();
  liveChatEnabled = newValue;
});

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
// Get the initial value from the Braze SDK
val featureFlag = braze.getFeatureFlag("enable_live_chat")
var liveChatEnabled = featureFlag?.enabled

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates() { event ->
  val newValue = braze.getFeatureFlag("enable_live_chat")?.enabled
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}

```

{% endtab %}
{% tab Swift %}

{% alert note %}
Das Lesen von `braze.featureFlags.featureFlags` oder `braze.featureFlags.featureFlag(id:)` blockiert den aufrufenden Thread, bis das SDK seine Post-Initialisierungsoperationen abgeschlossen hat. Für Main-Thread- oder latenzempfindliche Kontexte verwenden Sie stattdessen [`getAllFeatureFlags(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/featureflags-swift.class/getallfeatureflags(_:)).

```swift
// Non-blocking — completion handler always delivers on the main thread.
braze.featureFlags.getAllFeatureFlags { flags in
  let liveChatEnabled = flags.first(where: { $0.id == "enable_live_chat" })?.enabled ?? false
  liveChatView.isHidden = !liveChatEnabled
}
```

In Objective-C:

```objc
[braze.featureFlags getAllFeatureFlagsWithCompletion:^(NSArray<BRZFeatureFlag *> *flags) {
  // Use `flags` here.
}];
```
{% endalert %}

```swift
// Get the initial value from the Braze SDK
let featureFlag = braze.featureFlags.featureFlag(id: "enable_live_chat")
var liveChatEnabled = featureFlag?.enabled ?? false

// Listen for updates from the Braze SDK
braze.featureFlags.subscribeToUpdates() { _ in
  let newValue = braze.featureFlags.featureFlag(id: "enable_live_chat")?.enabled ?? false
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
liveChatView.isHidden = !liveChatEnabled
```

{% endtab %}
{% endtabs %}

### App-Variablen per Fernzugriff steuern {#remotely-control-app-variables}

Verwenden Sie Feature-Flags, um die Funktionalität Ihrer App in der Produktion zu ändern. Dies kann besonders für mobile Apps wichtig sein, da App-Store-Freigaben ein schnelles Ausrollen von Änderungen an alle Nutzer:innen verhindern.

Nehmen wir zum Beispiel an, unser Marketing-Team möchte unsere aktuellen Angebote und Aktionen in der Navigation unserer App auflisten. Normalerweise benötigen unsere Entwickler:innen eine Woche Vorlaufzeit für Änderungen und drei Tage für eine App-Store-Überprüfung. Aber mit Thanksgiving, Black Friday, Cyber Monday, Chanukka, Weihnachten und Neujahr innerhalb von zwei Monaten werden wir diese engen Fristen nicht einhalten können.

Mit Feature-Flags können wir Braze den Inhalt des Navigationslinks unserer App steuern lassen, sodass unser Marketing-Manager Änderungen in Minuten statt in Tagen vornehmen kann.

Um dieses Feature per Fernzugriff zu konfigurieren, erstellen wir ein neues Feature-Flag namens `navigation_promo_link` und definieren die folgenden anfänglichen Eigenschaften:

![Feature-Flag mit Link- und Text-Eigenschaften, die auf eine allgemeine Angebotsseite verweisen.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %})

In unserer App verwenden wir Getter-Methoden von Braze, um die Eigenschaften dieses Feature-Flags abzurufen und die Navigationslinks basierend auf diesen Werten aufzubauen:

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";
import {useState} from "react";

const featureFlag = braze.getFeatureFlag("navigation_promo_link");
// Check if the feature flag is enabled
const [promoEnabled, setPromoEnabled] = useState(featureFlag.enabled);
// Read the "link" property
const [promoLink, setPromoLink] = useState(featureFlag.getStringProperty("link"));
// Read the "text" property
const [promoText, setPromoText] = useState(featureFlag.getStringProperty("text"));

return (<>
  <div>
    <a href="/">Home</a>
    { promoEnabled && <a href={promoLink}>{promoText}</a> }
    <a href="/products">Products</a>
    <a href="/categories">Categories
  </div>
</>)
```

{% endtab %}
{% tab Java %}

```java
// liveChatView is the View container for the Live Chat UI
FeatureFlag featureFlag = braze.getFeatureFlag("navigation_promo_link");
if (featureFlag != null && featureFlag.getEnabled()) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
liveChatView.setPromoLink(featureFlag.getStringProperty("link"));
liveChatView.setPromoText(featureFlag.getStringProperty("text"));

```

{% endtab %}
{% tab Kotlin %}

```kotlin
// liveChatView is the View container for the Live Chat UI
val featureFlag = braze.getFeatureFlag("navigation_promo_link")
if (featureFlag?.enabled == true) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}
liveChatView.promoLink = featureFlag?.getStringProperty("link")
liveChatView.promoText = featureFlag?.getStringProperty("text")
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "navigation_promo_link")
if let featureFlag {
  liveChatView.isHidden = !featureFlag.enabled
} else {
  liveChatView.isHidden = true
}
liveChatView.promoLink = featureFlag?.stringProperty("link")
liveChatView.promoText = featureFlag?.stringProperty("text")
```

{% endtab %}
{% endtabs %}

Am Tag vor Thanksgiving müssen wir nun nur diese Eigenschaftswerte im Braze-Dashboard ändern.

![Feature-Flag mit Link- und Text-Eigenschaften, die auf eine Thanksgiving-Angebotsseite verweisen.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %})

Wenn jemand das nächste Mal die App lädt, sieht diese Person die neuen Thanksgiving-Angebote.

### Nachrichtenkoordination {#message-coordination}

Verwenden Sie Feature-Flags, um die Einführung eines Features und das zugehörige Messaging zu synchronisieren und die Zusammenarbeit zwischen Produkt- und Marketing-Teams zu stärken. Durch die Koordination von Feature-Releases und Messaging über Feature-Flags können beide Teams ihre Strategien aufeinander abstimmen und konsistente Nutzererlebnisse schaffen.

Angenommen, wir führen ein neues Kundenbindungs-Programm mit Rewards für unsere Nutzer:innen ein. Es kann schwierig sein, das Timing von Werbebotschaften mit der Einführung eines Features zwischen Marketing- und Produkt-Teams perfekt zu koordinieren. Mit Feature-Flags in Canvas kann unser Produkt-Team jedoch eine ausgefeilte Logik anwenden, um ein Feature für eine bestimmte Zielgruppe zu aktivieren, während unser Marketing-Team das zugehörige Messaging an dieselben Nutzer:innen steuert.

Um die Feature-Einführung und das Messaging effektiv zu koordinieren, erstellen wir ein neues Feature-Flag namens `show_loyalty_program`. Für unsere anfängliche schrittweise Freigabe lassen wir Canvas steuern, wann und für wen das Feature-Flag aktiviert wird. Vorerst belassen wir den Rollout-Prozentsatz bei 0 % und wählen keine Zielgruppen-Segmente aus.

![Ein Feature-Flag mit dem Namen „Loyalty Rewards Program“. Die ID ist show_loyalty_program, und die Beschreibung lautet, dass dieses Feature das neue Kundenbindungs-Programm mit Rewards auf dem Startbildschirm und der Profilseite anzeigt.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %})

Anschließend erstellen wir in Canvas einen [Feature-Flag-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags), der das Feature-Flag `show_loyalty_program` für unser Segment „High Value Customers“ aktiviert:

![Ein Beispiel für einen Canvas mit einem Zielgruppen-Split-Schritt, bei dem das Segment „High Value Customers“ das Feature-Flag show_loyalty_program aktiviert.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %})

Jetzt sehen Nutzer:innen in diesem Segment das neue Kundenbindungs-Programm, und nach der Aktivierung werden automatisch eine E-Mail und eine Umfrage gesendet, um unserem Team Feedback zu ermöglichen.

### Feature-Experimente {#feature-experimentation}

Verwenden Sie Feature-Flags, um Ihre Hypothesen rund um neue Features zu testen und zu bestätigen. Indem Sie den Traffic in zwei oder mehr Gruppen aufteilen, können Sie die Auswirkung eines Feature-Flags gruppenübergreifend vergleichen und auf Basis der Ergebnisse die beste Vorgehensweise bestimmen.

Für Feature-Flag-Experimente können Sie insgesamt bis zu neun Gruppen haben: eine Kontrollgruppe plus bis zu acht Varianten.

Ein [A/B-Test]({{site.baseurl}}/user_guide/messaging/ab_testing) ist ein leistungsstarkes Werkzeug, das die Reaktionen von Nutzer:innen auf mehrere Versionen einer Variable vergleicht.

In diesem Beispiel hat unser Team einen neuen Checkout-Ablauf für unsere E-Commerce-App entwickelt. Obwohl wir zuversichtlich sind, dass er das Nutzererlebnis verbessert, möchten wir einen A/B-Test durchführen, um die Auswirkungen auf den Umsatz unserer App zu messen.

Zunächst erstellen wir ein neues Feature-Flag namens `enable_checkout_v2`. Wir fügen weder eine Zielgruppe noch einen Rollout-Prozentsatz hinzu. Stattdessen verwenden wir ein Feature-Flag-Experiment, um den Traffic aufzuteilen, das Feature zu aktivieren und das Ergebnis zu messen.

In unserer App prüfen wir, ob das Feature-Flag aktiviert ist oder nicht, und tauschen den Checkout-Ablauf entsprechend aus:

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

const featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag?.enabled) {
  return <NewCheckoutFlow />
} else {
  return <OldCheckoutFlow />
}
```

{% endtab %}
{% tab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewCheckoutFlow();
} else {
  return new OldCheckoutFlow();
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("enable_checkout_v2")
braze.logFeatureFlagImpression("enable_checkout_v2")
if (featureFlag?.enabled == true) {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "enable_checkout_v2")
braze.featureFlags.logFeatureFlagImpression(id: "enable_checkout_v2")
if let featureFlag, featureFlag.enabled {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% endtabs %}

Wir richten unseren A/B-Test in einem [Feature-Flag-Experiment]({{site.baseurl}}/developer_guide/feature_flags/experiments) ein.

Nun sehen 50 % der Nutzer:innen das alte Erlebnis, während die anderen 50 % das neue Erlebnis sehen. Anschließend können wir die beiden Varianten analysieren, um zu bestimmen, welcher Checkout-Ablauf zu einer höheren Konversionsrate geführt hat. {% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

![Ein Feature-Flag-Experiment, das den Traffic in zwei 50-Prozent-Gruppen aufteilt.]({% image_buster /assets/img/feature_flags/feature-flag-use-case-campaign-experiment.png %})

Sobald wir einen Gewinner ermittelt haben, können wir diese Campaign stoppen und den Rollout-Prozentsatz des Feature-Flags auf 100 % für alle Nutzer:innen erhöhen, während unser Entwicklerteam dies fest in unser nächstes App-Release einbaut.

### Segmentierung {#segmentation}

Verwenden Sie den Filter **Feature-Flag**, um ein Segment zu erstellen oder Messaging an Nutzer:innen zu richten, basierend darauf, ob bei ihnen ein Feature-Flag aktiviert ist. Angenommen, Sie haben ein Feature-Flag, das Premium-Inhalte in Ihrer App steuert. Sie könnten ein Segment erstellen, das nach Nutzer:innen filtert, bei denen das Feature-Flag nicht aktiviert ist, und diesem Segment dann eine Nachricht senden, die zum Upgrade ihres Kontos auffordert, um Premium-Inhalte zu sehen.

1. Öffnen Sie Ihr Segment oder Ihre Nachrichtenzielgruppe.
2. Fügen Sie den Filter **Feature-Flag** hinzu.
3. Wählen Sie das Feature-Flag aus.
4. Setzen Sie den Vergleichsoperator auf **ist**, um Nutzer:innen einzuschließen, bei denen das Feature-Flag aktiviert ist, oder auf **ist nicht**, um Nutzer:innen einzuschließen, bei denen es nicht aktiviert ist.
![Braze Segment Builder mit einem Feature-Flag-Aktiviert-Filter.]({% image_buster /assets/img/feature_flags/feature_flag_segmentation_filter.png %})

Weitere Informationen zum Filtern in Segments finden Sie unter [Segment erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

{% alert note %}
Um rekursive Segments zu vermeiden, ist es nicht möglich, ein Segment zu erstellen, das auf andere Feature-Flags verweist.
{% endalert %}

## Einschränkungen nach Tarif {#plan-limitations}

Dies sind die Feature-Flag-Einschränkungen für kostenlose und kostenpflichtige Tarife.

| Feature                                                                                                   | Kostenlose Version     | Kostenpflichtige Version      |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| [Aktive Feature-Flags](#active-feature-flags)                                                                     | 10 pro Workspace | 110 pro Workspace |
| [Aktive Campaign-Experimente]({{site.baseurl}}/developer_guide/feature_flags/experiments)          | 1 pro Workspace  | 100 pro Workspace |
| [Feature-Flag-Canvas-Schritte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags) | Unbegrenzt        | Unbegrenzt         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Einschränkungen nach Tarif" }

Ein Feature-Flag gilt als aktiv und wird auf Ihr Limit angerechnet, wenn eine der folgenden Bedingungen zutrifft:

- Der Rollout beträgt mehr als 0 %
- Es wird in einem aktiven Canvas verwendet
- Es wird in einem aktiven Experiment verwendet

Auch wenn dasselbe Feature-Flag mehrere Kriterien erfüllt – zum Beispiel wenn es in einem Canvas verwendet wird und der Rollout bei 50 % liegt –, wird es nur als 1 aktives Feature-Flag auf Ihr Limit angerechnet.

{% alert note %}
Um die kostenpflichtige Version der Feature-Flags zu erwerben, wenden Sie sich an Ihren Braze Account Manager oder fordern Sie ein Upgrade im Braze-Dashboard an.
{% endalert %}