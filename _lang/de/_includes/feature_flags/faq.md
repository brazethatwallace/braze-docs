# Häufig gestellte Fragen {#frequently-asked-questions}

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu Feature-Flags.

## Funktionalität und Support {#functionality-and-support}

### Auf welchen Plattformen werden Braze Feature-Flags unterstützt? {#platforms}

Braze unterstützt Feature-Flags auf iOS, Android und Web-Plattformen mit den folgenden SDK-Versionsanforderungen:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

Benötigen Sie Unterstützung auf anderen Plattformen? Schreiben Sie unserem Team: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### Wie hoch ist der Aufwand bei der Implementierung eines Feature-Flags? {#level-of-effort}

Ein Feature-Flag kann in wenigen Minuten erstellt und integriert werden.

Der größte Teil des Aufwands entsteht durch Ihr Entwicklerteam, das das neue Feature entwickelt, das Sie ausrollen möchten. Was das Hinzufügen eines Feature-Flags betrifft, ist es so einfach wie eine `IF`/`ELSE`-Anweisung im Code Ihrer App oder Website:

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

### Wie können Feature-Flags Marketing-Teams zugutekommen? {#marketing-teams}

Marketing-Teams können Feature-Flags nutzen, um Produktankündigungen (wie E-Mails zum Produktlaunch) zu koordinieren, wenn ein Feature nur für einen kleinen Prozentsatz der Nutzer:innen aktiviert ist.

Beispielsweise können Sie mit Braze Feature-Flags ein neues Kundenbindungs-Programm für 10 % der Nutzer:innen in Ihrer App ausrollen und eine E-Mail, Push-Nachricht oder andere Nachrichten an dieselben 10 % der aktivierten Nutzer:innen senden – mithilfe des Canvas Feature-Flag-Schritts.

### Wie können Feature-Flags Produkt-Teams zugutekommen? {#product-teams}

Produkt-Teams können Feature-Flags für schrittweise Rollouts oder Soft-Launches neuer Features verwenden, um KPI und Kundenfeedback zu beobachten, bevor das Feature allen Nutzer:innen zur Verfügung gestellt wird.

Produkt-Teams können [Feature-Flag-Eigenschaften]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#properties) nutzen, um Inhalte in einer App remote bereitzustellen, wie z. B. Deeplinks, Texte, Bilder oder andere dynamische Inhalte.

Mithilfe des Canvas Feature-Flag-Schritts können Produkt-Teams außerdem einen A/B-Splittest durchführen, um zu messen, wie sich ein neues Feature auf die Konversionsraten im Vergleich zu Nutzer:innen mit deaktiviertem Feature auswirkt.

### Wie können Feature-Flags Entwicklerteams zugutekommen? {#engineering-teams}

Entwicklerteams können Feature-Flags nutzen, um das Risiko beim Launch neuer Features zu reduzieren und zu vermeiden, mitten in der Nacht überstürzt Code-Fixes deployen zu müssen.

Indem neuer Code hinter einem Feature-Flag veröffentlicht wird, kann Ihr Team das Feature remote über das Braze-Dashboard ein- oder ausschalten – ohne die Verzögerung durch das Ausliefern von neuem Code oder das Warten auf eine App-Store-Update-Genehmigung.

## Feature-Rollouts und Targeting {#feature-rollouts-and-targeting}

### Kann ein Feature-Flag nur für eine ausgewählte Gruppe von Nutzer:innen ausgerollt werden? {#target-users}

Ja, erstellen Sie in Braze ein Segment, das bestimmte Nutzer:innen anspricht – nach E-Mail-Adresse, `user_id` oder einem beliebigen anderen Attribut in Ihren Nutzerprofilen. Aktivieren Sie dann das Feature-Flag für 100 % dieses Segments.

### Wie wirkt sich die Anpassung des Rollout-Prozentsatzes auf Nutzer:innen aus, die zuvor der aktivierten Gruppe zugeordnet wurden? {#random-buckets}

Feature-Flag-Rollouts bleiben für Nutzer:innen geräte- und sitzungsübergreifend konsistent.

- Wenn ein Feature-Flag für 10 % zufälliger Nutzer:innen ausgerollt wird, bleiben diese 10 % aktiviert und bestehen für die gesamte Lebensdauer dieses Feature-Flags.
- Wenn Sie den Rollout von 10 % auf 20 % erhöhen, bleiben dieselben 10 % aktiviert, und weitere 10 % der Nutzer:innen werden der aktivierten Gruppe hinzugefügt.
- Wenn Sie den Rollout von 20 % auf 10 % senken, bleiben nur die ursprünglichen 10 % der Nutzer:innen aktiviert.

Diese Strategie stellt sicher, dass Nutzer:innen in Ihrer App ein konsistentes Erlebnis erhalten und nicht sitzungsübergreifend hin und her wechseln. Natürlich werden durch das Deaktivieren eines Features auf 0 % alle Nutzer:innen aus dem Feature-Flag entfernt, was hilfreich ist, wenn Sie einen Fehler entdecken oder das Feature vollständig deaktivieren müssen.

## Technische Themen {#technical-topics}

### Können Feature-Flags steuern, wann das Braze SDK initialisiert wird? {#initialization}

Nein, das SDK muss initialisiert werden, um Feature-Flags für die aktuelle:n Nutzer:in herunterzuladen und zu synchronisieren. Das bedeutet, dass Sie Feature-Flags nicht verwenden können, um einzuschränken, welche Nutzer:innen in Braze erstellt oder getrackt werden.

### Wie häufig aktualisiert das SDK Feature-Flags? {#refresh-frequency}

Feature-Flags werden bei Sitzungsbeginn und beim Wechsel aktiver Nutzer:innen aktualisiert. Feature-Flags können auch manuell über die [Aktualisierungsmethode]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#refreshing) des SDK aktualisiert werden. Aktualisierungen von Feature-Flags unterliegen einem Rate-Limit von einmal alle fünf Minuten (Änderungen vorbehalten).

Beachten Sie, dass gute Datenpraktiken empfehlen, Feature-Flags nicht zu häufig zu aktualisieren (mit möglichem Rate-Limiting bei zu häufiger Aktualisierung). Daher sollten Sie Feature-Flags am besten nur aktualisieren, bevor Nutzer:innen mit neuen Features interagieren, oder regelmäßig in der App, falls erforderlich.

### Sind Feature-Flags verfügbar, wenn Nutzer:innen offline sind? {#offline}

Ja, nachdem Feature-Flags aktualisiert wurden, werden sie lokal auf dem Gerät gespeichert und sind auch offline zugänglich.

### Was passiert, wenn Feature-Flags während einer Sitzung aktualisiert werden? {#listen-for-updates}

Feature-Flags können während einer Sitzung aktualisiert werden. Es gibt Szenarien, in denen Sie Ihre App aktualisieren möchten, wenn sich bestimmte Variablen oder Ihre Konfiguration ändern sollten. In anderen Szenarien möchten Sie Ihre App möglicherweise nicht aktualisieren, um eine überraschende Änderung in der Darstellung Ihrer UI zu vermeiden.

Um dies zu steuern, [überwachen Sie Aktualisierungen]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#updates) von Feature-Flags und entscheiden Sie, ob Ihre App basierend auf den geänderten Feature-Flags neu gerendert werden soll.

### Warum erhalten Nutzer:innen in meiner globalen Kontrollgruppe keine Feature-Flag-Experimente? {#why-arent-users-in-my-global-control-group-receiving-feature-flags-experiments}

Sie können Feature-Flags für Nutzer:innen in Ihrer [globalen Kontrollgruppe]({{site.baseurl}}/user_guide/audience/global_control_group) nicht aktivieren. Das bedeutet, dass Nutzer:innen in Ihrer globalen Kontrollgruppe auch nicht an Feature-Flag-Experimenten teilnehmen können.

## Weitere Fragen? {#additional-questions}

Haben Sie Fragen oder Feedback? Schreiben Sie unserem Team eine E-Mail: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).