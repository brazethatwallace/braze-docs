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

## Funktionalität und Unterstützung {#functionality-and-support}

### Auf welchen Plattformen werden Braze-Feature-Flags unterstützt? {#platforms}

Braze unterstützt Feature-Flags auf iOS-, Android- und Web-Plattformen mit den folgenden SDK-Versionsanforderungen:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

Benötigen Sie Unterstützung auf anderen Plattformen? Schreiben Sie unserem Team eine E-Mail: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### Wie hoch ist der Aufwand für die Implementierung eines Feature-Flags? {#level-of-effort}

Ein Feature-Flag kann in wenigen Minuten erstellt und integriert werden.

Der Großteil des Aufwands bezieht sich auf Ihr Entwicklerteam, das das neue Feature entwickelt, das Sie ausrollen möchten. Was das Hinzufügen eines Feature-Flags betrifft, ist es so einfach wie eine `IF`/`ELSE`-Anweisung im Code Ihrer App oder Website:

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

Marketing-Teams können Feature-Flags nutzen, um Produktankündigungen (wie E-Mails zum Produktlaunch) zu koordinieren, wenn ein Feature nur für einen kleinen Prozentsatz der Nutzer:innen aktiviert ist.

Mit Braze-Feature-Flags können Sie beispielsweise ein neues Kundenbindungs-Programm für 10 % der Nutzer:innen in Ihrer App ausrollen und eine E-Mail, einen Push oder andere Nachrichten an dieselben 10 % der aktivierten Nutzer:innen über den Canvas-Feature-Flag-Schritt senden.

### Welchen Nutzen haben Feature-Flags für Produkt-Teams? {#product-teams}

Produkt-Teams können Feature-Flags für schrittweise Rollouts oder Soft-Launches neuer Features verwenden, um Leistungskennzahlen und Kundenfeedback zu überwachen, bevor das Feature allen Nutzer:innen zur Verfügung gestellt wird.

Produkt-Teams können [Feature-Flag-Eigenschaften]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#properties) verwenden, um Inhalte in einer App remote zu befüllen, wie zum Beispiel Deeplinks, Text, Bilder oder andere dynamische Inhalte.

Mit dem Canvas-Feature-Flag-Schritt können Produkt-Teams außerdem einen A/B-Splittest durchführen, um zu messen, wie sich ein neues Feature im Vergleich zu Nutzer:innen mit deaktiviertem Feature auf die Konversionsraten auswirkt.

### Welchen Nutzen haben Feature-Flags für Entwicklerteams? {#engineering-teams}

Entwicklerteams können Feature-Flags nutzen, um das Risiko beim Launch neuer Features zu reduzieren und es zu vermeiden, mitten in der Nacht hektisch Code-Fixes deployen zu müssen.

Indem neuer Code hinter einem Feature-Flag veröffentlicht wird, kann Ihr Team das Feature remote über das Braze-Dashboard ein- oder ausschalten – ohne die Verzögerung durch das Ausrollen neuen Codes oder das Warten auf eine App-Store-Update-Freigabe.

## Feature-Rollouts und Targeting {#feature-rollouts-and-targeting}

### Kann ein Feature-Flag nur für eine bestimmte Gruppe von Nutzer:innen ausgerollt werden? {#target-users}

Ja, erstellen Sie ein Segment in Braze, das bestimmte Nutzer:innen anspricht – nach E-Mail-Adresse, `user_id` oder einem anderen Attribut in Ihren Nutzerprofilen. Stellen Sie das Feature-Flag dann für 100 % dieses Segments bereit.

### Wie wirkt sich die Anpassung des Rollout-Prozentsatzes auf Nutzer:innen aus, die zuvor in die aktivierte Gruppe eingeteilt wurden? {#random-buckets}

Feature-Flag-Rollouts bleiben für Nutzer:innen geräte- und sitzungsübergreifend konsistent.

- Wenn ein Feature-Flag für 10 % zufälliger Nutzer:innen ausgerollt wird, bleiben diese 10 % aktiviert und bestehen für die gesamte Lebensdauer dieses Feature-Flags.
- Wenn Sie den Rollout von 10 % auf 20 % erhöhen, bleiben die gleichen 10 % aktiviert, und zusätzlich werden weitere 10 % der Nutzer:innen zur aktivierten Gruppe hinzugefügt.
- Wenn Sie den Rollout von 20 % auf 10 % senken, bleiben nur die ursprünglichen 10 % der Nutzer:innen aktiviert.

Diese Strategie stellt sicher, dass Nutzer:innen in Ihrer App ein konsistentes Erlebnis erhalten und nicht sitzungsübergreifend hin und her wechseln. Natürlich werden bei einer Reduzierung eines Features auf 0 % alle Nutzer:innen aus dem Feature-Flag entfernt, was hilfreich ist, wenn Sie einen Fehler entdecken oder das Feature vollständig deaktivieren müssen.

## Technische Themen {#technical-topics}

### Können Feature-Flags verwendet werden, um zu steuern, wann das Braze SDK initialisiert wird? {#initialization}

Nein, das SDK muss initialisiert werden, um Feature-Flags für die aktuellen Nutzer:innen herunterzuladen und zu synchronisieren. Das bedeutet, dass Sie Feature-Flags nicht verwenden können, um einzuschränken, welche Nutzer:innen in Braze erstellt oder erfasst werden.

### Wie häufig aktualisiert das SDK Feature-Flags? {#refresh-frequency}

Feature-Flags werden beim Sitzungsstart und beim Wechsel aktiver Nutzer:innen aktualisiert. Feature-Flags können auch manuell über die [Aktualisierungsmethode]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#refreshing) des SDK aktualisiert werden. Die Aktualisierung von Feature-Flags ist auf einmal alle fünf Minuten begrenzt (Änderungen vorbehalten).

Beachten Sie, dass gute Datenpraktiken empfehlen, Feature-Flags nicht zu häufig zu aktualisieren (da bei zu schneller Aktualisierung Rate-Limiting greifen kann). Am besten aktualisieren Sie nur dann, wenn Nutzer:innen mit neuen Features interagieren, oder bei Bedarf in regelmäßigen Abständen in der App.

### Sind Feature-Flags verfügbar, wenn Nutzer:innen offline sind? {#offline}

Ja, nach der Aktualisierung werden Feature-Flags lokal auf dem Gerät der Nutzer:innen gespeichert und können auch im Offlinemodus abgerufen werden.

### Was passiert, wenn Feature-Flags während einer Sitzung aktualisiert werden? {#listen-for-updates}

Feature-Flags können während einer Sitzung aktualisiert werden. Es gibt Szenarien, in denen Sie Ihre App aktualisieren möchten, wenn sich bestimmte Variablen oder Ihre Konfiguration ändern sollten. Es gibt auch Szenarien, in denen Sie Ihre App nicht aktualisieren möchten, um eine unerwartete Änderung der UI-Darstellung zu vermeiden.

Um dies zu steuern, [registrieren Sie sich für Aktualisierungen]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#updates) von Feature-Flags und entscheiden Sie, ob Ihre App basierend auf den geänderten Feature-Flags neu gerendert werden soll.

### Warum erhalten Nutzer:innen in meiner globalen Kontrollgruppe keine Feature-Flag-Experimente? {#why-arent-users-in-my-global-control-group-receiving-feature-flags-experiments}

Sie können Feature-Flags nicht für Nutzer:innen in Ihrer [globalen Kontrollgruppe]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts) aktivieren. Das bedeutet, dass Nutzer:innen in Ihrer globalen Kontrollgruppe auch nicht an Feature-Flag-Experimenten teilnehmen können.

### Ist die E-Mail-basierte Empfängeridentifikation Teil von Braze Feature-Flags? {#is-email-based-recipient-identification-part-of-braze-feature-flags}

Nein. Die Identifikation von Empfänger:innen per E-Mail beim Nachrichtenversand ist nicht Teil des Feature-Flags-Produkts auf dieser Seite. Feature-Flags steuern In-App- oder On-Site-Erlebnisse über das Braze SDK.

API-getriggerte Campaign- und Canvas-Sendungen können `email` im [Recipients-Objekt]({{site.baseurl}}/api/objects_filters/recipient_object) anstelle einer `external_user_id` angeben. Wenn Sie `email` verwenden, geben Sie `prioritization` an, damit Braze das passende Nutzerprofil auswählen kann. Diese Sendeoption ist nicht in jedem Workspace verfügbar.

Informationen zum Anfrageformat finden Sie unter [POST: Campaigns mit API-getriggerter Zustellung senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) und [POST: Canvas-Nachrichten mit API-getriggerter Zustellung senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).

## Weitere Fragen? {#additional-questions}

Haben Sie Fragen oder Feedback? Schreiben Sie unserem Team: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).