---
page_order: 2.0
nav_title: Rate-Limits
article_title: Braze SDK or Software-Development-Kit-Rate-Limits
description: "Erfahren Sie mehr über das intelligente, clientseitige Rate-Limiting des Braze SDK or Software-Development-Kit, das die Akkulaufzeit optimiert, die Bandbreitennutzung reduziert und eine zuverlässige Zustellung der Daten gewährleistet."
---

# Braze SDK or Software-Development-Kit-Rate-Limits {#braze-sdk-rate-limits}

> Erfahren Sie mehr über das intelligente, clientseitige Rate-Limiting des Braze SDK or Software-Development-Kit, das die Akkulaufzeit optimiert, die Bandbreitennutzung reduziert und eine zuverlässige Zustellung der Daten gewährleistet.

## SDK or Software-Development-Kit-Rate-Limits verstehen {#understanding-sdk-rate-limits}

Das Rate-Limiting des Braze SDK or Software-Development-Kit nutzt die folgenden Features, um die Performance zu optimieren, den Batterieverbrauch zu minimieren, die Datennutzung zu reduzieren und eine zuverlässige Zustellung der Daten zu gewährleisten:

### Asynchrone Verarbeitung {#asynchronous-processing}

Das Braze SDK or Software-Development-Kit verwendet einen Token / Textbaustein-Bucket-Algorithmus für Rate-Limiting. Dieser Ansatz ermöglicht Aktivitätsschübe bei gleichzeitiger Aufrechterhaltung einer langfristigen Ratenkontrolle. Anstatt Anfragen in einer strengen Warteschlange zu verarbeiten, arbeitet der Token / Textbaustein-Bucket asynchron:

- **Token / Textbaustein-Generierung**: Die Token / Textbaustein werden kontinuierlich in den Bucket nachgefüllt.
- **Bearbeitung von Anfragen**: Jeder SDK or Software-Development-Kit-Aufruf, der eingeht, wenn ein Token / Textbaustein verfügbar ist, wird sofort ausgeführt – unabhängig davon, wann andere Aufrufe eingegangen sind.
- **Keine strenge Reihenfolge**: Anfragen warten nicht in einer Warteschlange; mehrere Aufrufe können um das nächste verfügbare Token / Textbaustein konkurrieren.
- **Burst-Verarbeitung**: Kurze Aktivitätsausbrüche sind zulässig, sofern zum Zeitpunkt der Anfragen ausreichend Token / Textbaustein verfügbar sind.
- **Ratenkontrolle**: Der langfristige Durchsatz wird durch die konstante Nachfüllrate der Token / Textbaustein begrenzt.

Dieser asynchrone Ablauf unterstützt das SDK or Software-Development-Kit dabei, schnell auf die verfügbare Netzwerkkapazität zu reagieren und gleichzeitig ein vorhersehbares Gesamtverkehrsaufkommen aufrechtzuerhalten.

### Adaptives Rate-Limiting {#adaptive-rate-limiting}

Das Braze SDK or Software-Development-Kit kann Rate-Limits in Echtzeit anpassen, um die Netzwerk-Infrastruktur zu schützen und eine optimale Performance aufrechtzuerhalten. Dieser Ansatz:

- **Verhindert Überlastung**: Passt die Limits an, um Netzwerküberlastungen zu vermeiden.
- **Optimiert die Performance**: Gewährleistet einen reibungslosen Betrieb des SDK or Software-Development-Kit unter unterschiedlichen Bedingungen.
- **Reagiert auf Bedingungen**: Passt sich an das aktuelle Netzwerk und die Nutzungsmuster an.

{% alert note %}
Da sich die Limits in Echtzeit anpassen, werden keine genauen Bucket-Größen und statischen Werte angegeben. Diese können sich je nach Netzwerkbedingungen und Nutzung ändern.
{% endalert %}

### Netzwerkoptimierungen {#networking-optimizations}

Das Braze SDK or Software-Development-Kit enthält mehrere integrierte Funktionen zur Verbesserung der Effizienz, zur Reduzierung des Batterieverbrauchs und zur Bewältigung unterschiedlicher Netzwerkbedingungen:

- **Automatische Bündelung**: Stellt Ereignisse in eine Warteschlange und sendet sie in effizienten Stapeln.
- **Netzwerkbewusstes Verhalten**: Passt die Flush-Raten basierend auf der Verbindungsqualität an.
- **Batterieoptimierung**: Minimiert Funkaktivierungen und Netzwerkaufrufe.
- **Graceful Degradation**: Gewährleistet die Funktionalität auch bei schlechten Netzwerkbedingungen.
- **Hintergrund-/Vordergrund-Erkennung**: Optimiert das Verhalten, wenn sich der Lebenszyklus der App ändert.

## Best Practices {#best-practices}

Befolgen Sie diese Best Practices, um Probleme mit Rate-Limits zu vermeiden:

| Empfohlen | Nicht empfohlen |
| --- | --- |
| Verfolgen Sie relevante Nutzeraktionen und Meilensteine | Verfolgen Sie jede kleine Interaktion oder jedes UI-Ereignis |
| Update or aktualisieren or aktualisieren Sie Inhalte nur bei Bedarf | Update or aktualisieren or aktualisieren Sie Inhalte bei jeder Nutzeraktion (z. B. bei Scroll-Ereignissen) |
| Lassen Sie das SDK or Software-Development-Kit die Stapelverarbeitung automatisch durchführen | Erzwingen Sie eine sofortige Übertragung der Daten (sofern nicht unbedingt erforderlich) |
| Konzentrieren Sie sich auf Ereignisse, die einen Mehrwert für Analytics bieten | Rufen Sie SDK or Software-Development-Kit-Methoden in schneller Folge auf, ohne die Häufigkeit zu berücksichtigen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Best Practices" }

## Hilfe erhalten {#getting-help}

Sollten Sie Probleme mit den SDK or Software-Development-Kit-Rate-Limits haben, überprüfen Sie bitte die folgenden Netzwerkmethoden:

- `requestImmediateDataFlush()`
- `requestContentCardsRefresh()`
- `refreshFeatureFlags()`
- `logCustomEvent()`
- `logPurchase()`

Wenn Sie den [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) kontaktieren, geben Sie bitte die folgenden Details für jede der von Ihnen verwendeten Netzwerk-SDK or Software-Development-Kit-Methoden an:

```plaintext
Method name:

Frequency:
[Describe how often this is called, e.g., at every app launch, once per session]

Trigger/context:
[Describe what causes it to be called, e.g., button click, scroll event]

Code snippet:
[Paste the exact code where this method is called, one snippet for each time it is called]

Patterns in user flow that may cause bursts or excessive calls:
[Describe here]
```
