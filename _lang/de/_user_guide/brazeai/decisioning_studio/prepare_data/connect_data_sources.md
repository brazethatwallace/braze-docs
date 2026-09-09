---
nav_title: Datenquellen verbinden
article_title: Datenquellen verbinden
page_order: 6
description: "Erfahren Sie, wie Sie Kundendatenquellen mit BrazeAI Decisioning Studio für personalisierte KI-Entscheidungsfindung verbinden."
---

# Datenquellen verbinden {#connect-your-data}

> BrazeAI Decisioning Studio™-Agenten müssen den Kundenkontext vollständig verstehen, um effektive Entscheidungen treffen zu können. Dieser Artikel erläutert, wie Sie Kundendatenquellen mit Decisioning Studio verbinden.

{% alert tip %}
Ihr KI-Decisioning-Services-Team unterstützt Sie bei der Konfiguration von Datenverbindungen für eine optimale Performance.
{% endalert %}

## Unterstützte Integrationsmuster {#supported-integration-patterns}

Decisioning Studio unterstützt mehrere Integrationsmuster zur Anbindung von Kundendaten:

| Integrationsmuster | Am besten geeignet für | Einrichtungskomplexität |
|---------------------|------------------------|-------------------------|
| **Braze Data Platform** | Kund:innen, die Braze bereits nutzen | Niedrig |
| **Braze Cloud Data Ingestion (CDI)** | Anbindung externer Data Warehouses | Mittel |
| **Cloud Storage (GCS, AWS, Azure)** | Direkter Datenexport von anderen Plattformen | Mittel |
| **CEP-Integrationen** | SFMC, Klaviyo Data Extensions | Mittel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Unterstützte Integrationsmuster" }

## Arten von Kundendaten {#customer-data-types}

Die folgenden Kundendaten helfen Agents, effektiver zu personalisieren:

| Datentyp | Beschreibung | Beispiele |
|-----------|-------------|----------|
| **Kundenprofil** | Statische und sich langsam ändernde Attribute | Jahre als Kund:in, Geografie, Akquisitionskanal, Zufriedenheitsniveau, geschätzter Lifetime-Value |
| **Kundenverhalten** | Aktivitäts- und Engagement-Muster | Konto-Anmeldungen, Gerätetyp, Kundenservice-Interaktionen, Produktnutzung |
| **Transaktionsverlauf** | Kauf- und Konversionsdaten | Gekaufte Produkte, Transaktionsbeträge, Zahlungsmethoden, Kaufkanäle |
| **Marketing-Engagement** | Reaktionen auf Kommunikation | E-Mail-Öffnungen/Klicks, SMS-Engagement, Web- und Mobile-Aktivität, Umfrageantworten |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Arten von Kundendaten" }

{% alert tip %}
Je mehr Informationen Agents über Ihre Kund:innen haben, desto besser werden sie arbeiten. Erwägen Sie, Daten zu allen Insights einzubeziehen, die für Ihr Unternehmen besonders wichtig wären (möchten Sie beispielsweise sehen, wie die KI Ihre treuen Kund:innen anders behandelt? Stellen Sie sicher, dass der Kundenbindungsstatus in den Kundendaten enthalten ist).
{% endalert %}

## Daten nach Plattform verbinden {#connect-data-by-platform}

{% tabs %}
{% tab Braze %}

### Kundendaten über Braze senden {#send-customer-data-through-braze}

BrazeAI Decisioning Studio kann alle Daten nutzen, die Sie bereits an die Braze-Datenplattform senden.

Für Kundendaten, die sich nicht im Nutzerprofil oder in angepassten Attributen befinden, haben Sie zwei Möglichkeiten, sie mit [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) einzubringen:

- In die Braze-Datenplattform aufnehmen. Synchronisieren Sie Data-Warehouse-Daten in Braze-Nutzerprofile, angepasste Attribute oder Events. Wählen Sie diese Option, wenn Sie die Daten auch in Braze für Segmentierung und Messaging verfügbar haben möchten. Unterstützt Snowflake, Redshift, BigQuery, Databricks, Microsoft Fabric, AWS S3 und Google Cloud Storage.
- Direkt an Decisioning Studio senden (Early Access). Synchronisieren Sie Data-Warehouse-Daten direkt mit Decisioning Studio, ohne sie dem Braze-Nutzerprofil oder angepassten Attributen hinzuzufügen. Wählen Sie diese Option für Daten, die Decisioning Studio nutzen soll, die Sie aber nicht an anderer Stelle in Braze benötigen. Diese Option befindet sich im Early Access. Informationen zur Einrichtung finden Sie unter [Cloud Data Ingestion: Decisioning-Studio-Daten synchronisieren]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/decisioning_studio).

Sobald Sie mit den Daten zufrieden sind, die Sie an die Braze-Datenplattform senden, wenden Sie sich an Ihr AI-Decisioning-Services-Team, um zu besprechen, welche Felder im Nutzerprofil oder welche angepassten Attribute für AI Decisioning verwendet werden sollen.

Um diesen Prozess zu optimieren, erstellen Sie eine Liste von Braze-Nutzerprofilattributen, die Ihrer Meinung nach das Kundenverhalten am besten repräsentieren und in Decisioning Studio verwendet werden sollten (siehe die [Liste der verfügbaren Felder]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#fields-to-export)). Ihr Services-Team kann Ihnen auch dabei helfen, Discovery-Sessions durchzuführen, um zu entscheiden, welche Felder für AI Decisioning am besten geeignet sind.

Weitere Optionen zum Senden von Daten sind:

- Braze angepasste Events über das SDK senden
- Events über den REST-Endpunkt senden ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))

Diese Muster erfordern mehr Engineering-Aufwand, sind aber je nach Ihrer aktuellen Braze-Konfiguration manchmal vorzuziehen. Wenden Sie sich an das AI-Decisioning-Services-Team, um mehr zu erfahren.

{% endtab %}
{% tab SFMC %}

### Kundendaten über SFMC senden {#send-customer-data-through-sfmc}

Für Salesforce Marketing Cloud-Integrationen:

1. Konfigurieren Sie SFMC Data Extension(s) für Ihre Kundendaten.
2. Richten Sie ein SFMC Installed Package für die API-Integration mit den entsprechenden Berechtigungen ein, die Decisioning Studio benötigt.
3. Stellen Sie sicher, dass Data Extensions täglich aktualisiert werden, da Decisioning Studio die neuesten inkrementellen Daten abruft.

Stellen Sie Ihrem AI-Decisioning-Services-Team die Extension-ID und den API-Schlüssel bereit. Das Team unterstützt Sie bei den nächsten Schritten zur Aufnahme von Kundendaten.

{% endtab %}
{% tab Klaviyo %}

### Kundendaten über Klaviyo senden {#send-customer-data-through-klaviyo}

Für Klaviyo-Integrationen:

1. Bestätigen Sie, dass Kundenprofile in Klaviyo-Profilen verfügbar sind.
2. Generieren Sie einen privaten API-Schlüssel mit Vollzugriff auf Profile.
3. Stellen Sie Ihrem AI-Decisioning-Services-Team den API-Schlüssel bereit.

Weitere Informationen zur Einrichtung des API-Schlüssels finden Sie in der [Klaviyo-Dokumentation](https://help.klaviyo.com/hc/en-us/articles/115005237908).

{% endtab %}
{% tab Cloud Storage %}

### Andere Cloud-Lösungen (Google Cloud Storage, Azure, AWS) {#other-cloud-solutions-google-cloud-storage-azure-aws}

Wenn Kundendaten derzeit nicht in Braze, SFMC oder Klaviyo gespeichert sind, besteht der nächste Schritt darin, einen automatisierten Export direkt in einen von Braze verwalteten Google Cloud Storage-Bucket zu konfigurieren. Wir können auch Exporte nach AWS oder Azure unterstützen (wobei GCS bevorzugt wird). Für diese Plattformen exportieren Sie in den jeweiligen internen Cloud-Speicher, und Braze kann die Daten anschließend abrufen.

Um zu prüfen, ob dies möglich ist, lesen Sie die Dokumentation Ihrer MarTech-Plattform. Zum Beispiel:

- mParticle bietet eine [native Integration mit Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/)
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

Wenn dies möglich ist, können wir einen GCS-Bucket bereitstellen, in den Kundendaten exportiert werden können und der für Decisioning Studio isoliert ist.

{% endtab %}
{% endtabs %}

## Best Practices {#best-practices}

- **Beschreibende Spaltennamen:** Kundendaten sollten klare, beschreibende Spaltennamen haben. Idealerweise sollte ein Datenwörterbuch bereitgestellt werden.
- **Inkrementelle Updates:** Inkrementelle Dateien sind gegenüber täglichen Snapshots der gesamten Kundenhistorie vorzuziehen.
- **Konsistente Bezeichner:** Jeder Datensatz muss einen eindeutigen Kundenbezeichner enthalten, der über alle Datenbestände hinweg konsistent ist.
- **Zeitstempel einbeziehen:** Datensätze sollten zugehörige Zeitstempel für eine genaue Attribution und das Training von Agents enthalten.

## Angepasste Integrationen {#custom-integrations}

Andere Optionen oder vollständig angepasste Datenpipelines sind möglich. Diese erfordern möglicherweise zusätzliche Serviceleistungen oder Engineering-Arbeit von Ihrem Team. Um herauszufinden, was machbar und optimal ist, arbeiten Sie mit Ihrem AI Decisioning Services-Team zusammen.

{% alert important %}
Dieser Leitfaden erläutert die gängigsten Integrationsmuster. Die Informationssicherheit muss weiterhin alle Verbindungspunkte prüfen, und Solutions Consultants stehen für die Beratung bei der Implementierung zur Verfügung.
{% endalert %}

## Nächste Schritte {#next-steps}

Nachdem Sie Ihre Datenquellen verbunden haben, fahren Sie mit der Einrichtung der Orchestrierung fort:

{% article_tiles %}
- name: Orchestrierung einrichten
  link: /docs/user_guide/brazeai/decisioning_studio/orchestration_setup
{% endarticle_tiles %}