---
nav_title: FAQ
article_title: Häufig gestellte Fragen
page_order: 50
description: "Auf dieser Seite finden Sie Antworten auf häufig gestellte Fragen zu Feature-Flags."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web
---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu Feature-Flags.

## Funktionalität und Support {#functionality-and-support}

### Auf welchen Plattformen werden Braze Feature-Flags unterstützt? {#platforms}

Braze unterstützt Feature-Flags auf iOS-, Android- und Web-Plattformen mit den folgenden SDK-Versionsanforderungen:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

Benötigen Sie Support auf anderen Plattformen? Schreiben Sie unserem Team eine E-Mail: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### Wie hoch ist der Aufwand bei der Implementierung eines Feature-Flags? {#level-of-effort}

Ein Feature-Flag kann in wenigen Minuten erstellt und integriert werden.

Der größte Teil des Aufwands entsteht durch Ihr Entwicklerteam, das das neue Feature entwickelt, das Sie ausrollen möchten. Aber wenn es darum geht, ein Feature-Flag hinzuzufügen, ist es so einfach wie eine `IF`/`ELSE`-Anweisung im Code Ihrer App oder Website:

{% tabs %}
{% tab JavaScript %}

```javascript
import { getFeatureFlag } from "@braze/web-sdk";

if (getFeatureFlag("new_shopping_cart").enabled) {
    // Show the new homepage your team has built
}
else {
    // Show the old homepage
}
```

{% endtab %}
{% tab Java %}

```java
if (braze.getFeatureFlag("new_shopping_cart").getEnabled()) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
if (braze.getFeatureFlag("new_shopping_cart")?.enabled == true) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% endtabs %}

### Wie können Feature-Flags Marketing-Teams unterstützen? {#marketing-teams}

Marketing-Teams können Feature-Flags nutzen, um Produktankündigungen (wie z. B. E-Mails zum Produktlaunch) zu koordinieren, wenn ein Feature nur für einen kleinen Prozentsatz der Nutzer:innen aktiviert ist.

Zum Beispiel können Sie mit Braze Feature-Flags ein neues Kundenbindungs-Programm für 10 % der Nutzer:innen in Ihrer App ausrollen und eine E-Mail, Push oder andere Messaging-Nachrichten an dieselben 10 % der aktivierten Nutzer:innen senden – mithilfe des Canvas Feature-Flag-Schritts.

### Wie können Feature-Flags Produkt-Teams unterstützen? {#product-teams}

Produkt-Teams können Feature-Flags nutzen, um schrittweise Rollouts oder Soft Launches neuer Features durchzuführen, um Leistungskennzahlen und Kundenfeedback zu überwachen, bevor das Feature allen Nutzer:innen zur Verfügung gestellt wird.

Produkt-Teams können [Feature-Flag-Eigenschaften]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#properties) verwenden, um Inhalte in einer App remote zu befüllen, wie z. B. Deeplinks, Text, Bilder oder anderen dynamischen Content.

Mithilfe des Canvas Feature-Flag-Schritts können Produkt-Teams auch einen A/B-Split-Test durchführen, um zu messen, wie ein neues Feature die Konversionsraten im Vergleich zu Nutzer:innen beeinflusst, bei denen das Feature deaktiviert ist.

### Wie können Feature-Flags Entwicklerteams unterstützen? {#engineering-teams}

Entwicklerteams können Feature-Flags nutzen, um das Risiko beim Launch neuer Features zu reduzieren und zu vermeiden, mitten in der Nacht überstürzt Code-Fixes deployen zu müssen.

Indem neuer Code hinter einem Feature-Flag veröffentlicht wird, kann Ihr Team das Feature remote über das Braze-Dashboard ein- oder ausschalten – ohne die Verzögerung durch das Ausliefern von neuem Code oder das Warten auf eine App-Store-Update-Genehmigung.

## Feature-Rollouts und Targeting {#feature-rollouts-and-targeting}

### Kann ein Feature-Flag nur für eine ausgewählte Gruppe von Nutzer:innen ausgerollt werden? {#target-users}

Ja, erstellen Sie ein Segment in Braze, das bestimmte Nutzer:innen anspricht – nach E-Mail-Adresse, `user_id` oder einem anderen Attribut in Ihren Nutzerprofilen. Rollen Sie dann das Feature-Flag für 100 % dieses Segments aus.

### Wie wirkt sich die Anpassung des Rollout-Prozentsatzes auf Nutzer:innen aus, die zuvor in die aktivierte Gruppe eingeteilt wurden? {#random-buckets}

Feature-Flag-Rollouts bleiben für Nutzer:innen über Geräte und Sitzungen hinweg konsistent.

- Wenn ein Feature-Flag für 10 % zufälliger Nutzer:innen ausgerollt wird, bleiben diese 10 % aktiviert und bestehen für die gesamte Lifetime dieses Feature-Flags.
- Wenn Sie den Rollout von 10 % auf 20 % erhöhen, bleiben dieselben 10 % aktiviert, und zusätzlich werden weitere 10 % der Nutzer:innen zur aktivierten Gruppe hinzugefügt.
- Wenn Sie den Rollout von 20 % auf 10 % senken, bleiben nur die ursprünglichen 10 % der Nutzer:innen aktiviert.

Diese Strategie stellt sicher, dass Nutzer:innen ein konsistentes Erlebnis in Ihrer App erhalten und nicht zwischen Sitzungen hin und her wechseln. Natürlich werden durch das Deaktivieren eines Features auf 0 % alle Nutzer:innen aus dem Feature-Flag entfernt, was hilfreich ist, wenn Sie einen Bug entdecken oder das Feature vollständig deaktivieren müssen.

## Technische Themen {#technical-topics}

### Können Feature-Flags verwendet werden, um zu steuern, wann das Braze SDK initialisiert wird? {#initialization}

Nein, das SDK muss initialisiert werden, um Feature-Flags für die aktuelle Nutzerin oder den aktuellen Nutzer herunterzuladen und zu synchronisieren. Das bedeutet, dass Sie Feature-Flags nicht verwenden können, um einzuschränken, welche Nutzer:innen in Braze erstellt oder getrackt werden.

### Wie häufig aktualisiert das SDK Feature-Flags? {#refresh-frequency}

Feature-Flags werden beim Sitzungsstart und beim Wechsel aktiver Nutzer:innen aktualisiert. Feature-Flags können auch manuell über die [Aktualisierungsmethode]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#refreshing) des SDK aktualisiert werden. Die Aktualisierung von Feature-Flags unterliegt einem Rate-Limit von einmal alle fünf Minuten (Änderungen vorbehalten).

Beachten Sie, dass gute Datenpraktiken empfehlen, Feature-Flags nicht zu häufig zu aktualisieren (mit potenziellem Rate-Limiting, falls dies geschieht). Am besten aktualisieren Sie nur, bevor Nutzer:innen mit neuen Features interagieren, oder bei Bedarf regelmäßig in der App.

### Sind Feature-Flags verfügbar, wenn Nutzer:innen offline sind? {#offline}

Ja, nachdem Feature-Flags aktualisiert wurden, werden sie lokal auf dem Gerät der Nutzerin oder des Nutzers gespeichert und können offline abgerufen werden.

### Was passiert, wenn Feature-Flags mitten in einer Sitzung aktualisiert werden? {#listen-for-updates}

Feature-Flags können mitten in einer Sitzung aktualisiert werden. Es gibt Szenarien, in denen Sie Ihre App aktualisieren möchten, wenn sich bestimmte Variablen oder Ihre Konfiguration ändern sollten. Es gibt andere Szenarien, in denen Sie Ihre App nicht aktualisieren möchten, um eine überraschende Änderung in der Darstellung Ihrer UI zu vermeiden.

Um dies zu steuern, [lauschen Sie auf Updates]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#updates) von Feature-Flags und entscheiden Sie, ob Ihre App basierend auf den geänderten Feature-Flags neu gerendert werden soll.

### Warum erhalten Nutzer:innen in meiner Globalen Kontrollgruppe keine Feature-Flag-Experimente? {#why-arent-users-in-my-global-control-group-receiving-feature-flags-experiments}

Sie können Feature-Flags nicht für Nutzer:innen in Ihrer [Globalen Kontrollgruppe]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts) aktivieren. Das bedeutet, dass Nutzer:innen in Ihrer Globalen Kontrollgruppe auch nicht an Feature-Flag-Experimenten teilnehmen können.

## Weitere Fragen? {#additional-questions}

Haben Sie Fragen oder Feedback? Schreiben Sie unserem Team eine E-Mail: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).