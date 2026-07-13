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

Decisioning Studio unterstützt mehrere Integrationsmuster für die Verbindung von Kundendaten:

| Integrationsmuster | Geeignet für | Einrichtungskomplexität |
|---------------------|----------|------------------|
| **Braze-Datenplattform** | Kund:innen, die Braze bereits nutzen | Niedrig |
| **Braze-Cloud-Datenaufnahme (CDI)** | Anbindung externer Data Warehouses | Mittel |
| **Cloud Storage (GCS, AWS, Azure)** | Direkte Datenexporte von anderen Plattformen | Mittel |
| **CEP-Integrationen** | SFMC, Klaviyo-Datenerweiterungen | Mittel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Unterstützte Integrationsmuster" }

## Kundendatentypen {#customer-data-types}

Die folgenden Kundendaten-Assets helfen Agenten, effektiver zu personalisieren:

| Datentyp | Beschreibung | Beispiele |
|-----------|-------------|----------|
| **Kundenprofil** | Statische und sich langsam ändernde Attribute | Jahre als Kund:in, Geografie, Akquisitionskanal, Zufriedenheitsniveau, geschätzter Lifetime-Value |
| **Kundenverhalten** | Aktivitäts- und Engagement-Muster | Kontoanmeldungen, Gerätetyp, Kundenservice-Interaktionen, Produktnutzung |
| **Transaktionsverlauf** | Kauf- und Conversion-Daten | Gekaufte Produkte, Transaktionsbeträge, Zahlungsmethoden, Kaufkanäle |
| **Marketing-Engagement** | Reaktionen auf Kommunikation | E-Mail-Öffnungen/-Klicks, SMS-Engagement, Web- und Mobilaktivität, Umfrageantworten |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Kundendatentypen" }

{% alert tip %}
Je mehr Informationen Agenten über Ihre Kund:innen haben, desto besser werden sie arbeiten. Erwägen Sie, Daten zu allen Insights einzubeziehen, die für Ihr Unternehmen besonders wichtig wären (möchten Sie beispielsweise sehen, wie die KI Ihre Treuekund:innen anders behandelt? Stellen Sie sicher, dass der Treuestatus in den Kundendaten enthalten ist).
{% endalert %}

## Daten nach Plattform verbinden {#connect-data-by-platform}

{% tabs %}
{% tab Braze %}

### Kundendaten über Braze senden {#send-customer-data-through-braze}

BrazeAI Decisioning Studio kann alle Daten nutzen, die Sie bereits an die Braze-Datenplattform senden.

Wenn es Kundendaten gibt, die Sie für Decisioning Studio verwenden möchten, die derzeit nicht im Nutzerprofil oder in angepassten Attributen gespeichert sind, empfiehlt es sich, die [Braze-Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) zu verwenden, um Daten aus anderen Quellen aufzunehmen.

CDI unterstützt direkte Integrationen mit:

- Snowflake
- Redshift
- BigQuery
- Databricks
- Microsoft Fabric
- AWS S3

Die vollständige Liste der unterstützten Quellen finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Sobald Sie mit den Daten zufrieden sind, die Sie an die Braze-Datenplattform senden, kontaktieren Sie Ihr KI-Decisioning-Services-Team, um zu besprechen, welche Felder im Nutzerprofil oder in angepassten Attributen für die KI-Entscheidungsfindung verwendet werden sollen.

Um diesen Prozess zu optimieren, erstellen Sie eine Liste von Braze-Nutzerprofilattributen, die Ihrer Meinung nach das Verhalten Ihrer Kund:innen am besten repräsentieren und in Decisioning Studio verwendet werden sollten (siehe die [Liste der verfügbaren Felder]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#fields-to-export)). Ihr Services-Team kann Ihnen auch dabei helfen, Discovery-Sitzungen durchzuführen, um zu entscheiden, welche Felder für die KI-Entscheidungsfindung am besten geeignet sind.

Weitere Optionen zum Senden von Daten umfassen:

- Senden von angepassten Braze-Events über das SDK
- Senden von Events über den REST-Endpunkt ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))

Diese Muster erfordern mehr Engineering-Aufwand, sind aber je nach Ihrer aktuellen Braze-Konfiguration manchmal vorzuziehen. Wenden Sie sich an das KI-Decisioning-Services-Team, um mehr zu erfahren.

{% endtab %}
{% tab SFMC %}

### Kundendaten über SFMC senden {#send-customer-data-through-sfmc}

Für Salesforce Marketing Cloud-Integrationen:

1. Konfigurieren Sie SFMC-Datenerweiterung(en) für Ihre Kundendaten.
2. Richten Sie ein SFMC Installed Package für die API-Integration mit den von Decisioning Studio benötigten Berechtigungen ein.
3. Stellen Sie sicher, dass die Datenerweiterungen täglich aktualisiert werden, da Decisioning Studio die neuesten inkrementellen Daten abruft.

Stellen Sie Ihrem KI-Decisioning-Services-Team die Erweiterungs-ID und den API-Schlüssel zur Verfügung. Das Team unterstützt Sie bei den nächsten Schritten zur Aufnahme von Kundendaten.

{% endtab %}
{% tab Klaviyo %}

### Kundendaten über Klaviyo senden {#send-customer-data-through-klaviyo}

Für Klaviyo-Integrationen:

1. Bestätigen Sie, dass Kundenprofildaten in Klaviyo-Profilen verfügbar sind.
2. Generieren Sie einen privaten API-Schlüssel mit Vollzugriff auf Profile.
3. Stellen Sie Ihrem KI-Decisioning-Services-Team den API-Schlüssel zur Verfügung.

Weitere Informationen zur Einrichtung von API-Schlüsseln finden Sie in der [Klaviyo-Dokumentation](https://help.klaviyo.com/hc/en-us/articles/115005237908).

{% endtab %}
{% tab Cloud Storage %}

### Andere Cloud-Lösungen (Google Cloud Storage, Azure, AWS) {#other-cloud-solutions-google-cloud-storage-azure-aws}

Wenn Kundendaten derzeit nicht in Braze, SFMC oder Klaviyo gespeichert sind, ist der nächste beste Schritt, einen automatisierten Export direkt in einen von Braze kontrollierten Google Cloud Storage-Bucket zu konfigurieren. Wir können auch den Export nach AWS oder Azure unterstützen (obwohl GCS bevorzugt wird). Für diese Plattformen exportieren Sie in deren internen Cloud Storage, und Braze kann die Daten dann abrufen.

Um festzustellen, ob dies machbar ist, lesen Sie die Dokumentation Ihrer MarTech-Plattform. Zum Beispiel:

- mParticle bietet eine [native Integration mit Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/)
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

Wenn dies machbar ist, können wir einen GCS-Bucket bereitstellen, in den Kundendaten exportiert werden können, der für Decisioning Studio isoliert ist.

{% endtab %}
{% endtabs %}

## Best Practices {#best-practices}

- **Beschreibende Spaltennamen:** Kundendaten sollten klare, beschreibende Spaltennamen haben. Idealerweise sollte ein Datenwörterbuch bereitgestellt werden.
- **Inkrementelle Updates:** Inkrementelle Dateien sind gegenüber täglichen Snapshots des gesamten Kundenverlaufs vorzuziehen.
- **Konsistente Bezeichner:** Jeder Datensatz muss einen eindeutigen Kundenbezeichner enthalten, der über alle Daten-Assets hinweg konsistent ist.
- **Zeitstempel einbeziehen:** Datensätze sollten zugehörige Zeitstempel für eine genaue Attribution und das Training von Agenten enthalten.

## Angepasste Integrationen {#custom-integrations}

Andere Optionen oder vollständig angepasste Datenpipelines sind möglich. Diese erfordern möglicherweise zusätzliche Services-Arbeit oder Engineering-Arbeit von Ihrem Team. Um festzustellen, was machbar und optimal ist, arbeiten Sie mit Ihrem KI-Decisioning-Services-Team zusammen.

{% alert important %}
Dieser Leitfaden erläutert die gängigsten Integrationsmuster. Die Informationssicherheit muss weiterhin alle Verbindungspunkte prüfen, und Solutions Consultants stehen zur Beratung bei der Implementierung zur Verfügung.
{% endalert %}

## Nächste Schritte {#next-steps}

Nachdem Sie Ihre Datenquellen verbunden haben, fahren Sie mit der Einrichtung der Orchestrierung fort:

- [Orchestrierung einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/orchestration_setup)