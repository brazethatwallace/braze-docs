---
nav_title: Peak
article_title: Peak
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Peak, einer Plattform für Entscheidungsintelligenz, die es Ihnen ermöglicht, prognostizierte Churn-Wahrscheinlichkeiten und Attribute basierend auf Kundenverhalten und -interaktionen in Braze zu importieren, um sie für die Segmentierung und das Targeting zu verwenden."
alias: /partners/Peak/
page_type: partner
search_tag: Partner

---

# Peak

> [Peak](https://peak.ai/), eine Plattform für Entscheidungsintelligenz, ist ein End-to-Outcome-System, bei dem Entscheidungsintelligenz die kommerzielle Anwendung von KI ist, um die Entscheidungsfindung in Unternehmen zu verbessern und Umsatz und Gewinne zu steigern.

_Diese Integration wird von Peak gepflegt._

## Über die Integration {#about-the-integration}

Die Partnerschaft zwischen Braze und Peak ermöglicht es Ihnen, prognostizierte Churn-Wahrscheinlichkeiten und Attribute basierend auf Kundenverhalten und -interaktionen in Braze zu importieren, um sie für die Segmentierung und das Targeting zu verwenden.

## Voraussetzungen {#prerequisites}

Als Ausgangspunkt muss ein Peak-Tenant die Integration zwischen Peak und Braze hosten. Dieser wird üblicherweise während des Onboardings von Peak-Kund:innen erstellt. Darüber hinaus ist zunächst eine Lösung für Entscheidungsintelligenz erforderlich, da diese die KI-gesteuerten Ausgaben generiert, die anschließend in Braze integriert werden.

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Peak-Tenant | Für das Hosting und die Orchestrierung der Integration ist eine Instanz der Peak-Plattform, ein sogenannter Tenant, erforderlich. |
| Decision-Intelligence-Lösung | Die Integration zwischen Peak und Braze basiert auf KI-gesteuerten Ausgaben und erfordert daher eine von Peak oder Kund:innen bereitgestellte Lösung innerhalb Ihres Tenants. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

Die Peak-Lösung Customer Intelligence nutzt ein Modell zur Prognose einer Reihe zukunftsorientierter Attribute basierend auf Kundenverhalten und -interaktionen. Diese Attribute werden in Peak gespeichert und können für eine prädiktive Segmentierung verwendet werden, einschließlich der Churn-Wahrscheinlichkeit von Kund:innen. Die Aktualisierung dieser prognostischen Attribute erfolgt in einem konfigurierbaren Rhythmus (täglich oder wöchentlich).

### 1. Schritt: Modell ausführen und Kund:innen extrahieren {#step-1-run-model-and-extract-customers}

Die Integration wird durch den Lauf des KI-Modells und die Neuberechnung der prognostizierten Attribute der Kund:innen ausgelöst. Diese KI-Ausgaben werden in Peak gespeichert – auch wenn ein Attribut mit einem neuen Status oder Wert aktualisiert wird.

Basierend darauf, wann Attribute aktualisiert wurden, wird eine Auswahl getroffen, um alle Kund:innen mit aktualisierten prognostischen Attributen seit der letzten Synchronisierung zwischen Peak und Braze zu erfassen.

### 2. Schritt: Braze aktualisieren {#step-2-update-braze}

Mit den aktualisierten Kund:innen und den zugehörigen Attributen sendet Peak diese über den [`/user/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) unter Verwendung des [Bulk-Headers]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#making-bulk-updates) per POST an Braze.

Bei Erhalt erfolgreicher Statuscodes von der API zeichnet Peak die erfolgreiche Synchronisierung zwischen Peak und Braze auf.

### 3. Schritt: Verwendung dieser Integration {#step-3-using-this-integration}

Sobald die Synchronisierung zwischen Peak und Braze erfolgreich war, enthalten die aktualisierten Nutzer:innen die neuen Attribute. Verwenden Sie diese Attribute in Campaigns und Canvases, um Nutzer:innen gezielt anzusprechen und Nachrichten zu personalisieren.