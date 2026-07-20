---
nav_title: Agenten konzipieren
article_title: Agenten konzipieren
page_order: 3
description: "Erfahren Sie, wie Sie einen BrazeAI Decisioning Studio Go-Agenten konzipieren, einschließlich Zielgruppendefinition, Dimensionen und Go-spezifischer Einschränkungen."
---

# Agenten konzipieren {#design-your-agent}

> Dieser Artikel behandelt die Konzeption Ihres Decisioning Studio Go-Agenten, einschließlich der Definition Ihrer Zielgruppe, der Auswahl von Dimensionen und des Verständnisses der Go-spezifischen Funktionen und Einschränkungen.

Grundlegende Konzepte zu Entscheidungsagenten – einschließlich Erfolgsmetriken, Dimensionen, Aktionsbanken und Einschränkungen – finden Sie unter [Entscheidungsagenten konzipieren]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/design_agents).

## Funktionen von Go im Vergleich zu Pro {#go-versus-pro-capabilities}

Decisioning Studio Go ist eine Self-Service-Plattform mit im Vergleich zu Decisioning Studio Pro vereinfachten Funktionen. Das Verständnis dieser Unterschiede unterstützt Sie dabei, einen effektiven Agenten im Rahmen von Go zu entwickeln.

| Fähigkeit | Decisioning Studio Go | Decisioning Studio Pro |
|-----------|----------------------|------------------------|
| **Erfolgsmetrik** | Nur Klicks | Jede Geschäftsmetrik (Umsatz, Conversions oder ARPU) |
| **Dimensionen** | Begrenzte Aktionsbank | Unbegrenzte Dimensionen |
| **Unterstützte CEPs** | Braze, SFMC | Jeder CEP (nativ und angepasst) |
| **Kundendaten** | Nur Engagement | Alle 1P-Daten |
| **Einrichtung** | Self-Service | Unterstützung durch KI-Entscheidungsdienste |
| **Versuchsgruppen** | Go + zufällige Kontrollgruppe + optionales BAU | Vollständig anpassbar |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Funktionen von Go im Vergleich zu Pro" }

## Ihren Go-Agenten konzipieren {#design-your-go-agent}

Bei der Konzeption eines Decisioning Studio Go-Agenten treffen Sie Entscheidungen in den folgenden Bereichen:

### Schritt 1: Definieren Sie Ihre Zielgruppe {#step-1-define-your-audience}

Ihre Zielgruppe ist die Gruppe von Kund:innen, die der Agent ansprechen wird. In Go werden Zielgruppen in Ihrem CEP definiert:

{% tabs %}
{% tab Braze %}

**Zielgruppe in Braze definieren:**

1. Erstellen Sie in Braze ein Segment, das die Kund:innen definiert, die der Agent ansprechen soll.
2. Wählen Sie bei der Konfiguration Ihres Experimentators im Decisioning Studio Go-Portal dieses Segment als Zielgruppe aus.

{% alert tip %}
Erwägen Sie, ein eigenes Segment für Ihren Decisioning Studio Go-Experimentator zu erstellen, um Ihre Tests isoliert und messbar zu halten.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

**Zielgruppe in SFMC definieren:**

1. Konfigurieren Sie eine Data Extension, die Ihre Zielgruppe enthält.
2. Aktualisieren Sie diese Data Extension täglich mit den neuesten Kundendaten.
3. Referenzieren Sie diese Data Extension im Decisioning Studio Go-Portal bei der Konfiguration Ihres Experimentators.

{% endtab %}
{% endtabs %}

### Schritt 2: Wählen Sie Ihre Dimensionen aus {#step-2-select-your-dimensions}

Dimensionen sind die „Hebel“, die der Agent betätigen kann, um das Kundenerlebnis zu personalisieren. Dazu gehören kreative Dimensionen wie Betreffzeile und Hero-Bild sowie Versandtyp-Dimensionen wie die Häufigkeit von E-Mails oder die Tageszeit.

{% alert note %}
Die verfügbaren spezifischen Dimensionen hängen von Ihrem CEP und der Konfiguration Ihrer Kampagnen ab. Verwenden Sie die Templates und Inhalte, die bereits in Ihrem CEP eingerichtet sind.
{% endalert %}

### Schritt 3: Konfigurieren Sie Ihre Aktionsbank {#step-3-configure-your-action-bank}

Die Aktionsbank definiert die spezifischen Optionen, aus denen der Agent für jede Dimension auswählen kann. Zum Beispiel:

- **E-Mail-Templates:** Wählen Sie aus, welche Templates der Agent verwenden darf (diese müssen zuvor in Ihrem CEP konfiguriert werden).
- **Betreffzeilen:** Definieren Sie die Betreffzeilen-Varianten, die der Agent testen kann.
- **Versandzeiten:** Geben Sie die Zeitfenster an, aus denen der Agent auswählen kann.

### Schritt 4: Versuchsgruppen einrichten {#step-4-set-up-experiment-groups}

Decisioning Studio Go erstellt automatisch Versuchsgruppen, um die Performance zu messen:

| Gruppe | Beschreibung |
|-------|-------------|
| **Decisioning Studio Go** | Kund:innen, die KI-optimierte Empfehlungen erhalten |
| **Zufällige Kontrollgruppe** | Kund:innen, die zufällig ausgewählte Optionen erhalten (Basisvergleich) |
| **Business as Usual (optional)** | Kund:innen, die Ihre bestehende Campaign erhalten (zum Vergleich mit der aktuellen Performance) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Versuchsgruppen einrichten" }

{% alert important %}
Für einen genauen Vergleich darf keine Kund:in mehr als einer Versuchsgruppe angehören, und die Zuweisung zu den Gruppen erfolgt zufällig und ohne Verzerrung.
{% endalert %}

## Zu berücksichtigende Einschränkungen {#limitations-to-consider}

Beachten Sie bei der Konzeption Ihres Go-Agenten die folgenden Einschränkungen:

- **Nur Klicks:** Go optimiert für Click-through-Raten. Wenn Sie für Umsatz, Conversions oder andere Geschäftsmetriken optimieren möchten, empfehlen wir Decisioning Studio Pro.
- **Begrenzte Dimensionen:** Go unterstützt eine vordefinierte Reihe von Dimensionen. Für angepasste Dimensionen oder komplexe Personalisierung empfehlen wir Decisioning Studio Pro.
- **Begrenzte CEP-Unterstützung:** Go lässt sich nur mit Braze und Salesforce Marketing Cloud integrieren. Für andere Plattformen empfehlen wir Decisioning Studio Pro.

## Best Practices {#best-practices}

- **Beginnen Sie mit einem engen Fokus:** Verwenden Sie zwei bis drei Templates oder Betreffzeilen-Varianten. Dies gibt dem Agenten genügend Optionen zum Lernen, während das Experiment überschaubar bleibt.
- **Geben Sie dem Ganzen Zeit:** Der Agent benötigt ausreichend Daten, um zu lernen. Warten Sie mindestens zwei bis vier Wochen, bevor Sie Schlussfolgerungen zur Performance ziehen.
- **Sorgen Sie für abwechslungsreiche Inhalte:** Verwenden Sie Optionen, die sich deutlich voneinander unterscheiden. Das Testen geringfügiger Abweichungen liefert möglicherweise keine aussagekräftigen Insights.
- **Überwachen Sie regelmäßig:** Überprüfen Sie das Decisioning Studio Go-Portal, um den Fortschritt des Experiments und die Engagement-Metriken zu überwachen.

## Nächste Schritte {#next-steps}

Nachdem Sie Ihren Agenten konzipiert haben, können Sie ihn im Braze-Dashboard konfigurieren und starten:

- [Ihren Decisioning Studio Go-Agenten einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup)