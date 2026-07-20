---
nav_title: Datenquellen verbinden
article_title: Datenquellen verbinden
page_order: 1
description: "Erfahren Sie, wie BrazeAI Decisioning Studio Go über Ihre Customer-Engagement-Plattform eine Verbindung zu Ihren Kundendaten herstellt."
---

# Datenquellen verbinden {#connect-data-sources}

> BrazeAI Decisioning Studio™ Go stellt über Ihre Customer-Engagement-Plattform (CEP) eine Verbindung zu Ihren Kundendaten her. Dieser Artikel erläutert, welche Daten verwendet werden und wie die Verbindung funktioniert.

## Wie Go auf Kundendaten zugreift {#how-go-accesses-customer-data}

Im Gegensatz zu Decisioning Studio Pro, das die direkte Datenintegration mit verschiedenen Quellen unterstützt, greift Decisioning Studio Go über Ihre CEP auf Kundendaten zu. Dies bedeutet:

- **Zielgruppendaten** werden direkt aus den in Ihrer CEP (Braze oder Salesforce Marketing Cloud) definierten Segmenten oder Listen abgerufen und können nur bestimmte vordefinierte Attribute enthalten (keine 1P-Daten).
- **Engagement-Daten** (Öffnungen, Klicks, Sendungen) werden durch automatisierte Abfragen oder native Integrationen mit Ihrer CEP erfasst.
- Es ist **keine zusätzliche Einrichtung der Datenpipeline** erforderlich, die über die Konfiguration in Ihrer CEP hinausgeht.

## Unterstützte Integrationsmuster {#supported-integration-patterns}

Decisioning Studio Go unterstützt die folgenden CEPs für den Zugriff auf Daten:

| CEP | Zielgruppenquelle | Engagement-Daten |
|-----|-----------------|-----------------|
| **Braze** | Segments | Braze-Currents-Export |
| **Salesforce Marketing Cloud** | Datenerweiterungen | Automatisierung von SQL-Anfragen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Unterstützte Integrationsmuster" }

## Datenanforderungen nach CEP {#data-requirements-by-cep}

{% tabs %}
{% tab Braze %}

### Anforderungen an Braze-Daten {#braze-data-requirements}

Für Braze-Integrationen erfordert Decisioning Studio Go Folgendes:

1. **Braze-Currents:** Braze-Currents muss aktiviert und konfiguriert sein, um Engagement-Daten in Decisioning Studio Go exportieren zu können. Dadurch kann der Agent aus den Reaktionen der Kund:innen lernen.

2. **Segmentzugang:** Der von Ihnen erstellte API-Schlüssel muss über Berechtigungen für den Zugriff auf Segments verfügen, die Ihre Zielgruppe definieren.

3. **Nutzerprofil-Daten:** Alle Nutzerprofil-Attribute oder angepassten Attribute, die der Agent berücksichtigen soll, müssen über die Braze-API zugänglich sein.

{% alert important %}
Stellen Sie sicher, dass Ihr Braze-Currents-Export Daten aus allen Campaigns enthält, die Sie vergleichen möchten (einschließlich BAU-Campaigns).
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

### SFMC-Datenanforderungen {#sfmc-data-requirements}

Für Salesforce Marketing Cloud-Integrationen erfordert Decisioning Studio Go Folgendes:

1. **Datenerweiterungen:** Ihre Zielgruppe muss in einer Datenerweiterung definiert sein, auf die Decisioning Studio Go zugreifen kann. Verwenden Sie den SubscriberKey als primären Bezeichner für Nutzer:innen.
2. **Zugriff auf Tracking-Ereignisse:** Solange das installierte App-Paket eine End-to-End-Automatisierung der Einrichtung unterstützt, ist keine zusätzliche Konfiguration erforderlich.

Die Datenerweiterungen und SQL-Anfragen werden im Rahmen von [Decisioning Studio Go-Agent einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup) konfiguriert.

{% endtab %}
{% endtabs %}

## Best Practices {#best-practices}

- **Daten aktuell halten:** Aktualisieren Sie Ihre Zielgruppensegmente und Kundendaten regelmäßig (mindestens einmal täglich), damit der Agent mit aktuellen Informationen arbeitet.
- **Relevante Attribute einbeziehen:** Überlegen Sie, welche Kundenmerkmale Einfluss darauf haben könnten, welche Nachrichten Anklang finden – demografische Daten, Engagement-Historie, Kaufverhalten und Lebenszyklusphase sind allesamt wertvolle Indikatoren.

## Nächste Schritte {#next-steps}

Nachdem Sie nun verstanden haben, wie Go eine Verbindung zu Daten herstellt, richten Sie Ihren Agenten im Braze-Dashboard ein:

- [Decisioning Studio Go-Agent einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup)