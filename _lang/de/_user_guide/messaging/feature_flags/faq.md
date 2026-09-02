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

Braze unterstützt Feature-Flags auf iOS, Android und Web-Plattformen mit den folgenden SDK-Versionsanforderungen:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

Benötigen Sie Unterstützung auf anderen Plattformen? Kontaktieren Sie unser Team per E-Mail: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### Wie hoch ist der Aufwand bei der Implementierung eines Feature-Flags? {#level-of-effort}

Ein Feature-Flag kann in wenigen Minuten erstellt und integriert werden.

Der größte Teil des Aufwands entfällt auf Ihr Entwicklerteam, das das neue Feature entwickelt, das Sie ausrollen möchten. Was das Hinzufügen eines Feature-Flags betrifft, ist es so einfach wie eine `IF`/`ELSE`-Anweisung im Code Ihrer App oder Website:

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

### Welchen Nutzen haben Feature-Flags für Marketing-Teams? {#marketing-teams}

Marketing-Teams können Feature-Flags nutzen, um Produktankündigungen (wie z. B. Produktstart-E-Mails) mit dem Zeitpunkt zu koordinieren, an dem ein Feature nur für einen kleinen Prozentsatz der Nutzer:innen aktiviert ist.

Mit Braze Feature-Flags können Sie beispielsweise ein neues Kundenbindungs-Programm für 10 % der Nutzer:innen in Ihrer App ausrollen und gleichzeitig eine E-Mail, Push-Nachricht oder andere Nachrichten an dieselben 10 % der aktivierten Nutzer:innen über den Canvas Feature-Flag-Schritt senden.

### Welchen Nutzen haben Feature-Flags für Produkt-Teams? {#product-teams}

Produkt-Teams können Feature-Flags für schrittweise Rollouts oder Soft Launches neuer Features nutzen, um Leistungskennzahlen und Kundenfeedback zu überwachen, bevor das Feature allen Nutzer:innen zur Verfügung gestellt wird.

Produkt-Teams können [Feature-Flag-Eigenschaften]({{site.baseurl}}/developer_guide/feature_flags/create#accessing-properties) verwenden, um Inhalte in einer App aus der Ferne zu befüllen, wie z. B. Deeplinks, Text, Bilder oder andere dynamische Inhalte.

Mithilfe des Canvas Feature-Flag-Schritts können Produkt-Teams auch einen A/B-Split-Test durchführen, um zu messen, wie sich ein neues Feature auf die Konversionsraten im Vergleich zu Nutzer:innen auswirkt, bei denen das Feature deaktiviert ist.

### Welchen Nutzen haben Feature-Flags für Entwicklerteams? {#engineering-teams}

Entwicklerteams können Feature-Flags nutzen, um das Risiko beim Launch neuer Features zu reduzieren und zu vermeiden, mitten in der Nacht eilig Code-Fixes deployen zu müssen.

Indem neuer Code hinter einem Feature-Flag veröffentlicht wird, kann Ihr Team das Feature aus der Ferne über das Braze-Dashboard ein- oder ausschalten und so die Verzögerung durch das Ausliefern von neuem Code oder das Warten auf eine App-Store-Update-Genehmigung umgehen.

## Feature-Rollouts und Targeting {#feature-rollouts-and-targeting}

### Kann ein Feature-Flag nur einer bestimmten Gruppe von Nutzer:innen zur Verfügung gestellt werden? {#target-users}

Ja, erstellen Sie ein Segment in Braze, das bestimmte Nutzer:innen anspricht – nach E-Mail-Adresse, `user_id` oder einem anderen Attribut in Ihren Nutzerprofilen. Stellen Sie dann das Feature-Flag für 100 % dieses Segments bereit.

### Wie wirkt sich die Anpassung des Rollout-Prozentsatzes auf Nutzer:innen aus, die zuvor der aktivierten Gruppe zugewiesen wurden? {#random-buckets}

Feature-Flag-Rollouts bleiben für Nutzer:innen über Geräte und Sitzungen hinweg konsistent.

- Wenn ein Feature-Flag für 10 % zufälliger Nutzer:innen ausgerollt wird, bleiben diese 10 % aktiviert und bestehen für die gesamte Lebensdauer dieses Feature-Flags.
- Wenn Sie den Rollout von 10 % auf 20 % erhöhen, bleiben dieselben 10 % aktiviert, und zusätzlich werden weitere 10 % der Nutzer:innen zur aktivierten Gruppe hinzugefügt.
- Wenn Sie den Rollout von 20 % auf 10 % senken, bleiben nur die ursprünglichen 10 % der Nutzer:innen aktiviert.

Diese Strategie stellt sicher, dass Nutzer:innen in Ihrer App ein konsistentes Erlebnis haben und nicht sitzungsübergreifend hin- und hergeschaltet werden. Natürlich werden durch das Deaktivieren eines Features auf 0 % alle Nutzer:innen aus dem Feature-Flag entfernt, was hilfreich ist, wenn Sie einen Fehler entdecken oder das Feature vollständig deaktivieren müssen.

## Technische Themen {#technical-topics}

### Können Feature-Flags verwendet werden, um zu steuern, wann das Braze SDK initialisiert wird? {#initialization}

Nein, das SDK muss initialisiert werden, um Feature-Flags für die aktuellen Nutzer:innen herunterzuladen und zu synchronisieren. Das bedeutet, dass Sie Feature-Flags nicht verwenden können, um einzuschränken, welche Nutzer:innen in Braze erstellt oder getrackt werden.

### Wie häufig aktualisiert das SDK Feature-Flags? {#refresh-frequency}

Feature-Flags werden beim Sitzungsstart und beim Wechsel aktiver Nutzer:innen aktualisiert. Feature-Flags können auch manuell über die [Aktualisierungsmethode]({{site.baseurl}}/developer_guide/feature_flags/create#refreshing) des SDK aktualisiert werden. Die Aktualisierung von Feature-Flags unterliegt einem Rate-Limiting von einmal alle fünf Minuten (Änderungen vorbehalten).

Beachten Sie, dass gute Datenpraktiken empfehlen, Feature-Flags nicht zu häufig zu aktualisieren (da bei zu häufiger Aktualisierung Rate-Limiting greifen kann). Es ist daher am besten, nur vor einer Interaktion der Nutzer:innen mit neuen Features oder bei Bedarf in regelmäßigen Abständen in der App zu aktualisieren.

### Sind Feature-Flags verfügbar, wenn Nutzer:innen offline sind? {#offline}

Ja, nachdem Feature-Flags aktualisiert wurden, werden sie lokal auf dem Gerät der Nutzer:innen gespeichert und können auch offline abgerufen werden.

### Was passiert, wenn Feature-Flags mitten in einer Sitzung aktualisiert werden? {#listen-for-updates}

Feature-Flags können mitten in einer Sitzung aktualisiert werden. Es gibt Szenarien, in denen Sie Ihre App aktualisieren möchten, wenn sich bestimmte Variablen oder Ihre Konfiguration ändern sollten. Es gibt andere Szenarien, in denen Sie Ihre App nicht aktualisieren möchten, um eine abrupte Änderung in der Darstellung Ihrer UI zu vermeiden.

Um dies zu steuern, [überwachen Sie Aktualisierungen]({{site.baseurl}}/developer_guide/feature_flags/create#updates) von Feature-Flags und entscheiden Sie, ob Ihre App basierend auf den geänderten Feature-Flags neu gerendert werden soll.

### Warum erhalten Nutzer:innen in meiner globalen Kontrollgruppe keine Feature-Flag-Experimente? {#why-arent-users-in-my-global-control-group-receiving-feature-flags-experiments}

Sie können Feature-Flags für Nutzer:innen in Ihrer [globalen Kontrollgruppe]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts) nicht aktivieren. Das bedeutet, dass Nutzer:innen in Ihrer globalen Kontrollgruppe auch nicht Teil von Feature-Flag-Experimenten sein können.

### Ist die E-Mail-basierte Empfängeridentifikation Teil von Braze Feature-Flags? {#is-email-based-recipient-identification-part-of-braze-feature-flags}

Nein. Die Identifizierung von Empfänger:innen per E-Mail beim Senden einer Nachricht ist nicht Teil des Feature-Flags-Produkts auf dieser Seite. Feature-Flags steuern In-App- oder On-Site-Erlebnisse über das Braze SDK.

API-getriggerte Campaign- und Canvas-Sendungen können `email` im [Empfängerobjekt]({{site.baseurl}}/api/objects_filters/recipient_object) anstelle einer `external_user_id` enthalten. Wenn Sie `email` verwenden, fügen Sie `prioritization` hinzu, damit Braze das passende Nutzerprofil auswählen kann. Diese Sendeoption ist nicht in jedem Workspace verfügbar.

Informationen zur Anfrage-Struktur finden Sie unter [POST: Campaigns über API-getriggerte Zustellung senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) und [POST: Canvas-Nachrichten über API-getriggerte Zustellung senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).

## Weitere Fragen? {#additional-questions}

Haben Sie Fragen oder Feedback? Schreiben Sie unserem Team: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).