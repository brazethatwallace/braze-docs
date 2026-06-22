---
nav_title: Microsoft Azure Blob-Speicher
article_title: Microsoft Azure Blob-Speicher
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze-Currents und Microsoft Azure Blob Storage, einem massiv skalierbaren Objektspeicher für unstrukturierte Daten."
page_type: partner
tool: Currents
search_tag: Partner

---

# Microsoft Azure Blob-Speicher {#microsoft-azure-blob-storage}

> [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) ist ein massiv skalierbarer Objektspeicher für unstrukturierte Daten, der von Microsoft als Teil der Azure-Produkt-Suite angeboten wird.

{% alert important %}
Wenn Sie zwischen Cloud-Speicheranbietern wechseln, wenden Sie sich an Ihren Customer-Success-Manager von Braze, um weitere Unterstützung bei der Einrichtung und Validierung Ihrer neuen Integration zu erhalten.
{% endalert %}

Die Integration von Braze und Microsoft Azure Blob Storage erlaubt es Ihnen, Daten zurück nach Azure zu exportieren und Currents-Daten zu streamen. Später können Sie einen ETL-Prozess (Extract, Transform, Load) verwenden, um Ihre Daten an andere Standorte zu übertragen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Microsoft Azure und Azure-Speicherkonto | Um die Vorteile dieser Partnerschaft nutzen zu können, benötigen Sie ein Microsoft Azure- und Azure-Storage-Konto. |
| Currents | Um Daten nach Currents zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. Currents ist nicht erforderlich, wenn Sie nur die Nachrichtenarchivierung einrichten möchten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Für die Integration mit Microsoft Azure Blob Storage benötigen Sie ein Speicherkonto und einen Verbindungs-String, damit Braze entweder Daten zurück nach Azure exportieren oder Currents-Daten streamen kann.

### 1. Schritt: Speicherkonto erstellen {#step-1-create-a-storage-account}

Navigieren Sie in Microsoft Azure in der Seitenleiste zu **Storage Accounts** und klicken Sie auf **+ Add**, um ein neues Speicherkonto zu erstellen. Geben Sie als Nächstes einen Namen für das Speicherkonto an. Andere Standardeinstellungen müssen nicht aktualisiert werden. Wählen Sie abschließend **Review + create**.

Auch wenn Sie bereits ein Speicherkonto haben, empfehlen wir Ihnen, ein neues Konto speziell für Ihre Braze-Daten anzulegen.

![Die Seite „Speicherkonto erstellen“ in Microsoft Azure auf dem Tab „Grundlagen“ mit hervorgehobenem Feld für den Speicherkontonamen.]({% image_buster /assets/img/azure-currents-step-1.png %})

### 2. Schritt: Verbindungs-String abrufen {#step-2-get-the-connection-string}

Sobald das Speicherkonto bereitgestellt ist, navigieren Sie vom Speicherkonto aus zum Menü **Access Keys** und notieren Sie sich den Verbindungs-String.

Microsoft stellt zwei Zugriffsschlüssel zur Verfügung, um Verbindungen mit einem Schlüssel aufrechtzuerhalten, während der andere regeneriert wird. Sie benötigen nur den Verbindungs-String von einem der beiden.

{% alert note %}
Braze verwendet den Verbindungs-String aus diesem Menü, nicht den Schlüssel.
{% endalert %}

![Die Seite „Access Keys“ für ein Azure-Speicherkonto mit hervorgehobenem Verbindungs-String-Feld unter „key1“.]({% image_buster /assets/img/azure-currents-step-2.png %})

### 3. Schritt: Blob-Service-Container erstellen {#step-3-create-a-blob-service-container}

Navigieren Sie zum Menü **Blobs** unter dem Abschnitt **Blob Service** Ihres Speicherkontos. Erstellen Sie einen Blob-Service-Container in dem Speicherkonto, das Sie zuvor angelegt haben.

Geben Sie einen Namen für Ihren Blob-Service-Container an. Andere Standardeinstellungen müssen nicht aktualisiert werden.

![Die Seite „Blobs“ für ein Azure-Speicherkonto unter „Blob Service“ mit der Option, einen Container hinzuzufügen.]({% image_buster /assets/img/azure-currents-step-3.png %})

### 4. Schritt: Currents einrichten {#step-4-set-up-currents}

Navigieren Sie in Braze zu **Currents > + Create Current > Azure Blob Data Export** und geben Sie den Namen Ihrer Integration und eine Kontakt-E-Mail an.

Geben Sie als Nächstes Ihren Verbindungs-String, den Containernamen und das BlobStorage-Präfix (optional) an.

![Die Microsoft Azure Blob-Speicher-Currents-Seite in Braze. Auf dieser Seite gibt es Felder für den Integrationsnamen, die Kontakt-E-Mail, den Verbindungs-String, den Containernamen und das Präfix.]({% image_buster /assets/img/maz.png %})

Scrollen Sie schließlich zum Ende der Seite und wählen Sie aus, welche Nachrichten-Engagement-Events oder Kundenverhalten-Events Sie exportieren möchten. Wenn Sie fertig sind, starten Sie Ihren Current.

### 5. Schritt: Azure-Datenexport einrichten {#step-5-set-up-azure-data-export}

Im Folgenden werden die Zugangsdaten konfiguriert, die für Folgendes verwendet werden:
1. Segmentexporte über die API
2. CSV-Exporte (Export von Campaign-, Segment- und Canvas-Nutzerdaten über das Dashboard)
3. Engagement-Berichte

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** > **Microsoft Azure** und geben Sie Ihren Verbindungs-String, den Namen des Azure-Speichercontainers und das Azure-Speicherpräfix an.

Vergewissern Sie sich als Nächstes, dass das Kästchen **Make this the default data export destination** markiert ist. Dadurch wird sichergestellt, dass Ihre exportierten Daten an Azure gesendet werden. Wenn Sie fertig sind, speichern Sie Ihre Integration.

![Die Microsoft Azure-Datenexportseite in Braze. Auf dieser Seite gibt es Felder für den Verbindungs-String, den Containernamen und das Präfix.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
Es ist wichtig, Ihren Verbindungs-String auf dem neuesten Stand zu halten. Wenn die Zugangsdaten Ihres Konnektors ablaufen, sendet der Konnektor keine Events mehr. Wenn dieser Zustand länger als **48 Stunden** anhält, werden die Events des Konnektors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

## Exportverhalten {#export-behavior}

Nutzer:innen, die eine Cloud-Datenspeicherlösung integriert haben und versuchen, APIs, Dashboard-Berichte oder CSV-Berichte zu exportieren, werden Folgendes feststellen:

- Alle API-Exporte geben keine Download-URL im Antwortkörper zurück und müssen über den Datenspeicher abgerufen werden.
- Alle Dashboard-Berichte und CSV-Berichte werden zum Download an die E-Mail der Nutzer:innen gesendet (keine Speicherberechtigungen erforderlich) und auf dem Datenspeicher gesichert.

{% alert important %}
**JSON-Format erforderlich**: Für JSON-Exporte verwendet Braze das [JSONL](https://jsonlines.org/)-Format (Newline-delimited JSON), bei dem jede Zeile ein eigenes JSON-Objekt enthält. Dieses Format unterscheidet sich vom Standard-JSON, das ein einzelnes JSON-Array oder -Objekt ist. Jede Zeile in der exportierten Datei ist ein gültiges JSON-Objekt, aber die Datei als Ganzes ist kein einzelnes gültiges JSON-Dokument. Wenn Sie diese Dateien verarbeiten, parsen Sie jede Zeile einzeln als separates JSON-Objekt, anstatt zu versuchen, die gesamte Datei als ein einziges JSON-Dokument zu parsen. <br><br> Currents-Exporte verwenden das [Apache Avro](https://avro.apache.org/)-Format (`.avro`-Dateien), nicht JSON. Diese Anforderung an das JSON-Format gilt für Dashboard-Datenexporte und API-Exporte, die das JSON-Format verwenden.
{% endalert %}

## FAQ

### Kann Braze IP-Adressen für die Freigabeliste von Azure Blob Storage bereitstellen? {#can-braze-provide-ip-addresses-to-allowlist-for-azure-blob-storage}

Braze veröffentlicht keine feste IP-Freigabeliste für Currents oder Dashboard-Exporte nach Azure Blob Storage. Braze schreibt in Ihren Container unter Verwendung des Verbindungs-Strings und Containernamens, den Sie angeben, und Azure steuert den Netzwerkzugriff über Ihre Speicherkontoeinstellungen (z. B. Firewallregeln für das Speicherkonto oder private Endpunkte).

Wenn Ihr Sicherheitsteam IP-basierte Einschränkungen benötigt, verwenden Sie die Azure-Netzwerkfunktionen für Ihr Speicherkonto anstelle einer IP-Liste von Braze. Informationen zu den Einrichtungsschritten finden Sie in der [Microsoft-Dokumentation zur Absicherung von Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security).