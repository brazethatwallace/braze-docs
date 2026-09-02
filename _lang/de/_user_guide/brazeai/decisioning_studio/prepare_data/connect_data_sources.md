---
nav_title: Datenquellen verbinden
article_title: Datenquellen verbinden
page_order: 6
description: "Erfahren Sie, wie Sie Kundendatenquellen mit BrazeAI Decisioning Studio für personalisierte KI or künstliche Intelligenz-Entscheidungsfindung verbinden."
---

# Datenquellen verbinden {#connect-your-data}

> BrazeAI Decisioning Studio™-Agenten müssen den Kundenkontext vollständig verstehen, um effektive Entscheidungen treffen zu können. Dieser Artikel erläutert, wie Sie Kundendatenquellen mit Decisioning Studio verbinden.

{% alert tip %}
Ihr KI or künstliche Intelligenz-Decisioning-Services-Team unterstützt Sie bei der Konfiguration von Datenverbindungen für eine optimale Performance.
{% endalert %}

## Unterstützte Integrationsmuster {#supported-integration-patterns}

Decisioning Studio unterstützt mehrere Integrationsmuster für die Anbindung von Kundendaten:

| Integrationsmuster | Ideal für | Einrichtungskomplexität |
|---------------------|----------|------------------|
| **Braze Data Platform** | Kund:innen, die Braze bereits nutzen | Niedrig |
| **Braze Cloud Data Ingestion (CDI)** | Anbindung externer Data Warehouses | Mittel |
| **Cloud Storage (GCS, AWS, Azure)** | Direkte Datenexporte von anderen Plattformen | Mittel |
| **CEP-Integrationen** | SFMC, Klaviyo Data Extensions | Mittel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Unterstützte Integrationsmuster" }

## Kundendatentypen {#customer-data-types}

Die folgenden Kundendaten-Assets helfen Agents, effektiver zu personalisieren:

| Datentyp | Beschreibung | Beispiele |
|-----------|-------------|----------|
| **Kundenprofil or Kundenprofil or Nutzerprofil** | Statische und sich langsam ändernde Attribute | Jahre als Kund:in, Geografie, Akquisitionskanal, Zufriedenheitsniveau, geschätzter LTV or Lifetime-Value or Lifetime-Value |
| **Kundenverhalten** | Aktivitäts- und Engagement-Muster | Kontoanmeldungen, Gerätetyp, Kundenservice-Interaktionen, Produktnutzung |
| **Transaktionsverlauf** | Kauf- und Konversionsdaten | Gekaufte Produkte, Transaktionsbeträge, Zahlungsmethoden, Kaufkanäle |
| **Marketing-Engagement** | Reaktionen auf Kommunikation | E-Mail-Öffnungen/Klicks, Kurzmitteilungsdienst or SMS-Engagement, Web- und Mobile-Aktivität, Umfrageantworten |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Kundendatentypen" }

{% alert tip %}
Je mehr Informationen Agents über Ihre Kund:innen haben, desto besser werden sie arbeiten. Erwägen Sie, Daten zu allen Insights einzubeziehen, die für Ihr Unternehmen besonders wichtig wären (möchten Sie zum Beispiel sehen, wie die KI or künstliche Intelligenz Ihre treuen Kund:innen anders behandelt? Stellen Sie sicher, dass der Kundenbindungsstatus in den Kundendaten enthalten ist).
{% endalert %}

## Daten nach Plattform verbinden {#connect-data-by-platform}

{% tabs %}
{% tab Braze %}

### Kundendaten über Braze senden {#send-customer-data-through-braze}

BrazeAI Decisioning Studio kann alle Daten nutzen, die Sie bereits an die Braze-Datenplattform senden.

Für Kundendaten, die sich nicht im Kundenprofil or Nutzerprofil oder in angepassten Attributen befinden, gibt es zwei Möglichkeiten, sie mit [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) einzubringen:

- In die Braze-Datenplattform aufnehmen. Synchronisieren Sie Data-Warehouse-Daten in Braze-Nutzerprofile, angepasste Attribute oder Events. Wählen Sie diese Option, wenn Sie die Daten auch in Braze für Segmentierung und Messaging verfügbar haben möchten. Unterstützt werden Snowflake, Redshift, BigQuery, Databricks, Microsoft Fabric, AWS S3 und Google Cloud Storage.
- Direkt an Decisioning Studio senden (Early Access). Synchronisieren Sie Data-Warehouse-Daten direkt mit Decisioning Studio, ohne sie dem Braze-Kundenprofil or Nutzerprofil oder angepassten Attributen hinzuzufügen. Wählen Sie diese Option für Daten, die Decisioning Studio verwenden soll, die Sie aber an anderer Stelle in Braze nicht benötigen. Diese Option befindet sich im Early Access – siehe [Cloud Data Ingestion: Decisioning-Studio-Daten synchronisieren]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/decisioning_studio), um sie einzurichten.

Sobald Sie mit den Daten zufrieden sind, die Sie an die Braze-Datenplattform senden, wenden Sie sich an Ihr KI or künstliche Intelligenz-Decisioning-Services-Team, um zu besprechen, welche Felder im Kundenprofil or Nutzerprofil oder welche angepassten Attribute für KI or künstliche Intelligenz Decisioning verwendet werden sollen.

Um diesen Prozess zu vereinfachen, erstellen Sie eine Liste von Braze-Nutzerprofilattributen, die Ihrer Meinung nach das Kundenverhalten am besten abbilden und in Decisioning Studio verwendet werden sollten (siehe die [Liste der verfügbaren Felder]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#fields-to-export)). Ihr Services-Team kann Ihnen auch dabei helfen, Discovery-Sitzungen durchzuführen, um zu entscheiden, welche Felder für KI or künstliche Intelligenz Decisioning am besten geeignet sind.

Weitere Optionen zum Senden von Daten sind:

- Braze-angepasste Events über das SDK or Software-Development-Kit senden
- Events über den Representational State Transfer-Endpunkt senden ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))

Diese Ansätze erfordern mehr Engineering-Aufwand, sind aber je nach Ihrer aktuellen Braze-Konfiguration manchmal vorzuziehen. Wenden Sie sich an das KI or künstliche Intelligenz-Decisioning-Services-Team, um mehr zu erfahren.

{% endtab %}
{% tab SFMC %}

### Kundendaten über SFMC senden {#send-customer-data-through-sfmc}

Für Salesforce-Marketing-Cloud-Integrationen:

1. Konfigurieren Sie SFMC-Data-Extension(s) für Ihre Kundendaten.
2. Richten Sie ein SFMC Installed Package für die API-Integration mit den von Decisioning Studio benötigten Berechtigungen ein.
3. Stellen Sie sicher, dass die Data Extensions täglich aktualisiert werden, da Decisioning Studio die neuesten inkrementellen Daten abruft.

Stellen Sie Ihrem KI or künstliche Intelligenz-Decisioning-Services-Team die Extension-ID und den API-Schlüssel zur Verfügung. Das Team unterstützt Sie bei den nächsten Schritten zur Aufnahme der Kundendaten.

{% endtab %}
{% tab Klaviyo %}

### Kundendaten über Klaviyo senden {#send-customer-data-through-klaviyo}

Für Klaviyo-Integrationen:

1. Bestätigen Sie, dass Kundenprofile in Klaviyo-Profilen verfügbar sind.
2. Generieren Sie einen privaten API-Schlüssel mit Vollzugriff auf Profile.
3. Stellen Sie Ihrem KI or künstliche Intelligenz-Decisioning-Services-Team den API-Schlüssel zur Verfügung.

Weitere Informationen zur Einrichtung des API-Schlüssels finden Sie in der [Klaviyo-Dokumentation](https://help.klaviyo.com/hc/en-us/articles/115005237908).

{% endtab %}
{% tab Cloud Storage %}

### Andere Cloud-Lösungen (Google Cloud Storage, Azure, AWS) {#other-cloud-solutions-google-cloud-storage-azure-aws}

Wenn Kundendaten derzeit nicht in Braze, SFMC oder Klaviyo gespeichert sind, ist der nächste empfohlene Schritt, einen automatisierten Export direkt in einen von Braze verwalteten Google Cloud Storage-Bucket einzurichten. Wir unterstützen auch den Export nach AWS oder Azure (wobei GCS bevorzugt wird). Für diese Plattformen exportieren Sie in deren internen Cloud-Speicher, und Braze kann die Daten dann von dort abrufen.

Um festzustellen, ob dies machbar ist, lesen Sie die Dokumentation Ihrer MarTech-Plattform. Zum Beispiel:

- mParticle bietet eine [native Integration mit Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/)
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

Wenn dies machbar ist, können wir einen GCS-Bucket bereitstellen, in den Kundendaten exportiert werden können und der für Decisioning Studio isoliert ist.

{% endtab %}
{% endtabs %}

## Best Practices {#best-practices}

- **Beschreibende Spaltennamen:** Kundendaten sollten klare, beschreibende Spaltennamen haben. Idealerweise sollte ein Datenwörterbuch bereitgestellt werden.
- **Inkrementelle Aktualisierungen:** Inkrementelle Dateien sind gegenüber täglichen Snapshots der gesamten Kundenhistorie vorzuziehen.
- **Konsistente Bezeichner:** Jeder Datensatz muss einen eindeutigen Kundenbezeichner enthalten, der über alle Datenbestände hinweg konsistent ist.
- **Zeitstempel einbeziehen:** Datensätze sollten zugehörige Zeitstempel für eine genaue Attribution und das Trainieren von Agents enthalten.

## Angepasste Integrationen {#custom-integrations}

Andere Optionen oder vollständig angepasste Datenpipelines sind möglich. Diese erfordern möglicherweise zusätzliche Serviceleistungen oder Engineering-Arbeit von Ihrem Team. Um herauszufinden, was machbar und optimal ist, arbeiten Sie mit Ihrem KI or künstliche Intelligenz Decisioning Services-Team zusammen.

{% alert important %}
Dieser Leitfaden erläutert die gängigsten Integrationsmuster. Die Informationssicherheit muss weiterhin alle Verbindungspunkte prüfen, und Solutions Consultants stehen zur Beratung bei der Implementierung zur Verfügung.
{% endalert %}

## Nächste Schritte {#next-steps}

Nachdem Sie Ihre Datenquellen verbunden haben, fahren Sie mit der Einrichtung der Orchestrierung fort:

- [Orchestrierung einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/orchestration_setup)