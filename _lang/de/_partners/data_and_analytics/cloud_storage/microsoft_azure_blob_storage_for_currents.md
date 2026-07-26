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
Wenn Sie zwischen Cloud-Speicheranbietern wechseln, wenden Sie sich an Ihren geschäftskunden-Success-Manager von Braze, um weitere Unterstützung bei der Einrichtung und Validierung Ihrer neuen Integration zu erhalten.
{% endalert %}

Die Integration von Braze und Microsoft Azure Blob Storage erlaubt es Ihnen, Daten zurück nach Azure zu exportieren und Currents-Daten zu streamen. Später können Sie einen ETL-Prozess (Extract, Transform, Load) verwenden, um Ihre Daten an andere Standorte zu übertragen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Microsoft Azure und Azure-Speicherkonto | Ein Microsoft Azure- und Azure-Speicherkonto sind erforderlich, um diese Partnerschaft zu nutzen. |
| Currents | Um Daten nach Currents zu exportieren, muss [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) für Ihr Konto eingerichtet sein. Currents ist nicht erforderlich, wenn Sie nur die Nachrichtenarchivierung einrichten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Für die Integration mit Microsoft Azure Blob Storage benötigen Sie ein Speicherkonto und einen Container, damit Braze entweder Daten zurück nach Azure exportieren oder Currents-Daten streamen kann. Braze unterstützt zwei Authentifizierungsmethoden:

- [Verbindungs-String-Methode](#connection-string-auth-method)
- [Zertifikat-Dienstprinzipal-Methode](#certificate-service-principal-auth-method) (nur Currents)

## Authentifizierungsmethode mit Verbindungszeichenfolge {#connection-string-auth-method}

### Schritt 1: Speicherkonto erstellen {#step-1-create-a-storage-account}

Navigieren Sie in Microsoft Azure in der Seitenleiste zu **Storage Accounts** und klicken Sie auf **+ Add**, um ein neues Speicherkonto zu erstellen. Geben Sie anschließend einen Namen für das Speicherkonto an. Andere Standardeinstellungen müssen nicht geändert werden. Wählen Sie abschließend **Review + create** aus.

Auch wenn Sie bereits über ein Speicherkonto verfügen, empfehlen wir, ein neues Konto speziell für Ihre Braze-Daten zu erstellen.

![Die Seite „Speicherkonto erstellen“ in Microsoft Azure auf dem Tab „Basics“ mit hervorgehobenem Feld für den Speicherkontonamen.]({% image_buster /assets/img/azure-currents-step-1.png %})

### Schritt 2: Verbindungszeichenfolge abrufen {#step-2-get-the-connection-string}

Sobald das Speicherkonto bereitgestellt ist, navigieren Sie zum Menü **Access Keys** im Speicherkonto und notieren Sie sich die Verbindungszeichenfolge.

Microsoft stellt zwei Zugriffsschlüssel bereit, um Verbindungen mit einem Schlüssel aufrechtzuerhalten, während der andere neu generiert wird. Sie benötigen nur die Verbindungszeichenfolge von einem der beiden.

{% alert note %}
Braze verwendet die Verbindungszeichenfolge aus diesem Menü, nicht den Schlüssel.
{% endalert %}

![Die Seite „Access Keys“ für ein Azure-Speicherkonto mit hervorgehobenem Feld für die Verbindungszeichenfolge unter „key1“.]({% image_buster /assets/img/azure-currents-step-2.png %})

### Schritt 3: Blob-Service-Container erstellen {#step-3-create-a-blob-service-container}

Navigieren Sie zum Menü **Blobs** im Abschnitt **Blob Service** Ihres Speicherkontos. Erstellen Sie einen Blob-Service-Container innerhalb des zuvor erstellten Speicherkontos.

Geben Sie einen Namen für Ihren Blob-Service-Container an. Andere Standardeinstellungen müssen nicht geändert werden.

![Die Seite „Blobs“ für ein Azure-Speicherkonto unter „Blob Service“ mit der Option, einen Container hinzuzufügen.]({% image_buster /assets/img/azure-currents-step-3.png %})

### Schritt 4: Currents einrichten {#step-4-set-up-currents}

Navigieren Sie in Braze zu **Currents > + Create Current > Azure Blob Data Export** und geben Sie Ihren Integrationsnamen und Ihre Kontakt-E-Mail-Adresse an.

Geben Sie anschließend Ihre Verbindungszeichenfolge, den Containernamen und das BlobStorage-Präfix (optional) an.

![Die Seite „Microsoft Azure Blob Storage Currents“ in Braze. Auf dieser Seite befinden sich Felder für Integrationsname, Kontakt-E-Mail, Verbindungszeichenfolge, Containername und Präfix.]({% image_buster /assets/img/maz.png %})

Scrollen Sie abschließend zum Ende der Seite und wählen Sie aus, welche Engagement-Events oder Kundenverhalten-Events Sie exportieren möchten. Wenn Sie fertig sind, starten Sie Ihren Current.

### Schritt 5: Azure-Datenexport einrichten {#step-5-set-up-azure-data-export}

Im Folgenden werden die Zugangsdaten konfiguriert, die für Folgendes verwendet werden:
1. Segment-Exporte über die API
2. CSV-Exporte (Campaign-, Segment-, Canvas-Nutzerdaten-Export über das Dashboard)
3. Engagement-Berichte

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** > **Microsoft Azure** und geben Sie Ihre Verbindungszeichenfolge, den Azure-Speichercontainernamen und das Azure-Speicherpräfix an.

Stellen Sie als Nächstes sicher, dass das Kontrollkästchen **Make this the default data export destination** aktiviert ist, damit Ihre exportierten Daten an Azure gesendet werden. Wenn Sie fertig sind, speichern Sie Ihre Integration.

![Die Seite „Microsoft Azure-Datenexport“ in Braze. Auf dieser Seite befinden sich Felder für Verbindungszeichenfolge, Containername und Präfix.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
Es ist wichtig, Ihre Verbindungszeichenfolge aktuell zu halten. Wenn die Zugangsdaten Ihres Konnektors ablaufen, stellt der Konnektor das Senden von Events ein. Wenn dies länger als 48 Stunden andauert, werden die Events des Konnektors verworfen und Daten gehen dauerhaft verloren.
{% endalert %}

## Authentifizierungsmethode „Zertifikat-Dienstprinzipal“ {#certificate-service-principal-auth-method}

Diese Methode authentifiziert sich bei Microsoft Entra ID mithilfe eines Zertifikats und schreibt dann über die rollenbasierte Zugriffssteuerung (RBAC) von Azure – ohne gemeinsam genutzten Kontoschlüssel – in Ihren Container. Sie ist ausschließlich für Braze-Currents verfügbar.

{% alert note %}
Sie laden nur das öffentliche Zertifikat zu Microsoft Entra ID hoch – Ihr Private Key wird niemals an Azure gesendet. Braze speichert Ihr Zertifikat und Ihren Private Key verschlüsselt im Ruhezustand, gewährt Zugriff ausschließlich über die Rolle [Storage Blob Data Contributor](#cert-sp-4), die Sie zuweisen, und Sie können diesen Zugriff jederzeit widerrufen, indem Sie das Zertifikat aus Ihrer App-Registrierung in Azure entfernen.
{% endalert %}

Bevor Sie beginnen, [erstellen Sie ein Speicherkonto](#step-1-create-a-storage-account) und einen [Blob-Dienstcontainer](#step-3-create-a-blob-service-container) wie in der [Verbindungszeichenfolgen-Methode](#connection-string-auth-method) beschrieben.

### Schritt 1: Anwendung registrieren {#cert-sp-1}

Navigieren Sie in Microsoft Azure zu **Microsoft Entra ID** > **App-Registrierungen** > **+ Neue Registrierung**. Geben Sie einen Namen ein (zum Beispiel `braze-currents`) und wählen Sie **Registrieren**. Ausführliche Schritte finden Sie in Microsofts Dokumentation [Registrieren einer Anwendung bei der Microsoft Identity Platform](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app).

Notieren Sie sich auf der **Übersicht**-Seite Ihrer neuen App-Registrierung die folgenden Werte. Sie geben beide in [Schritt 6](#cert-sp-6) in Braze ein.

- **Anwendungs-ID (Client-ID)**
- **Verzeichnis-ID (Mandanten-ID)**

### Schritt 2: Zertifikat erstellen {#cert-sp-2}

Braze authentifiziert sich mithilfe eines Zertifikats: Sie laden das **öffentliche Zertifikat** zu Azure hoch und übergeben Braze das **Zertifikat zusammen mit seinem Private Key**.

Um ein selbstsigniertes Zertifikat und einen unverschlüsselten 2048-Bit-RSA-Private-Key zu generieren, führen Sie folgenden Befehl aus:

```bash
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem \
  -days 730 -nodes -subj "/CN=braze-currents"
```

Dadurch werden zwei Dateien erstellt:

| Datei | Zweck |
| ---- | ------- |
| `cert.pem` | Ihr öffentliches Zertifikat. Laden Sie diese Datei im nächsten Schritt zu Azure hoch. |
| `key.pem` | Ihr Private Key. Laden Sie diesen niemals zu Azure hoch. Sie übergeben ihn in [Schritt 6](#cert-sp-6) an Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zertifikatsdateien" }

{% alert important %}
Der Private Key muss unverschlüsselt sein – er darf nicht durch eine Passphrase geschützt sein. Laden Sie nur das öffentliche Zertifikat zu Azure hoch; laden Sie niemals Ihren Private Key hoch.
{% endalert %}

**Sie haben bereits ein Zertifikat?** Wenn Sie ein vorhandenes Zertifikat als `.pfx`-Datei besitzen – zum Beispiel aus Azure Key Vault, von Ihrer Zertifizierungsstelle oder über [Microsofts PowerShell-Methode](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-self-signed-certificate) – konvertieren Sie es in das von Braze benötigte Format, anstatt ein neues zu generieren:

```bash
# The public certificate to upload to Azure (Step 3)
openssl pkcs12 -in your-cert.pfx -nokeys -out cert.pem

# The certificate and its unencrypted private key to give to Braze (Step 6)
openssl pkcs12 -in your-cert.pfx -nodes -out braze-currents.pem
```

Geben Sie Ihr `.pfx`-Passwort ein, wenn Sie dazu aufgefordert werden. Das Flag `-nodes` exportiert den Private Key unverschlüsselt, wie es Braze erfordert.

### Schritt 3: Zertifikat hochladen {#cert-sp-3}

Navigieren Sie in Ihrer App-Registrierung zu **Zertifikate & Geheimnisse** > **Zertifikate** > **Zertifikat hochladen** und laden Sie die im vorherigen Schritt erstellte Datei `cert.pem` hoch. Fügen Sie eine Beschreibung hinzu und wählen Sie **Hinzufügen**. Ausführliche Schritte finden Sie in Microsofts Dokumentation [Hinzufügen und Verwalten von App-Anmeldeinformationen in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials).

Notieren Sie sich das Ablaufdatum Ihres Zertifikats. Siehe [Azure-Zugangsdaten für Currents aktualisieren](#updating-currents-credentials).

### Schritt 4: Zugriff auf Ihr Speicherkonto gewähren {#cert-sp-4}

Erteilen Sie als Nächstes Ihrer App-Registrierung die Berechtigung, in Ihren Container zu schreiben.

Navigieren Sie zu Ihrem Speicherkonto und wählen Sie **Zugriffssteuerung (IAM)** > **+ Hinzufügen** > **Rollenzuweisung hinzufügen**. Dann:

1. Wählen Sie auf dem Tab **Rolle** die Option **[Storage Blob Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/storage#storage-blob-data-contributor)**.
2. Wählen Sie auf dem Tab **Mitglieder** die Option **Benutzer, Gruppe oder Dienstprinzipal**, wählen Sie **+ Mitglieder auswählen** und suchen Sie nach dem Namen der App-Registrierung, die Sie in [Schritt 1](#cert-sp-1) erstellt haben.
3. Wählen Sie **Überprüfen + zuweisen**.

Ausführliche Schritte finden Sie in Microsofts Dokumentation [Zuweisen einer Azure-Rolle für den Zugriff auf Blobdaten](https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access).

![Der Tab „Rollenzuweisungen“ unter „Zugriffssteuerung (IAM)“ für ein Speicherkonto, der einen Dienstprinzipal und eine Gruppe mit der Rolle „Storage Blob Data Contributor“ zeigt.]({% image_buster /assets/img/azure-currents-cert-sp-1.png %})

{% alert note %}
Weisen Sie die Rolle auf der Ebene des **Speicherkontos** zu, nicht auf einem einzelnen Container.
{% endalert %}

{% alert important %}
Ohne diese Rollenzuweisung kann sich Braze zwar bei Microsoft Entra ID authentifizieren, aber nicht in Ihren Container schreiben.
{% endalert %}

### Schritt 5: Konto-Endpunkt abrufen {#cert-sp-5}

Navigieren Sie in Ihrem Speicherkonto zu **Einstellungen** > **Endpunkte** und notieren Sie sich den **Blob-Dienst**-Endpunkt. Er sieht in etwa so aus: `https://<your-storage-account>.blob.core.windows.net`.

![Die Endpunkte-Seite des Speicherkontos mit hervorgehobenem Blob-Dienst-Endpunkt.]({% image_buster /assets/img/azure-currents-cert-sp-2.png %})

{% alert note %}
Die Authentifizierung per Zertifikat-Dienstprinzipal unterstützt ausschließlich die öffentliche Azure-Cloud. Ihr Blob-Endpunkt muss auf `.blob.core.windows.net` enden.
{% endalert %}

### Schritt 6: Currents einrichten {#cert-sp-6}

Braze benötigt eine einzelne PEM-Datei, die Ihr Zertifikat und seinen unverschlüsselten Private Key enthält. Wenn Sie in [Schritt 2](#cert-sp-2) ein neues Zertifikat generiert haben, kombinieren Sie die beiden Dateien zu einer:

```bash
cat cert.pem key.pem > braze-currents.pem
```

Wenn Sie in [Schritt 2](#cert-sp-2) eine vorhandene `.pfx`-Datei konvertiert haben, besitzen Sie diese `braze-currents.pem`-Datei bereits.

Navigieren Sie in Braze zu **Currents** > **+ Current erstellen** > **Azure Blob Data Export** und geben Sie Ihren Integrationsnamen sowie Ihre Kontakt-E-Mail-Adresse ein. Wählen Sie unter **Zugangsdaten** die Option **Certificate Service Principal** und geben Sie Folgendes an:

| Feld | Wert |
| ----- | ----- |
| Tenant ID | Die **Verzeichnis-ID (Mandanten-ID)** aus [Schritt 1](#cert-sp-1). |
| Client ID | Die **Anwendungs-ID (Client-ID)** aus [Schritt 1](#cert-sp-1). |
| Account Endpoint | Der **Blob-Dienst**-Endpunkt aus [Schritt 5](#cert-sp-5). |
| Certificate | Die Datei `braze-currents.pem`, die Ihr Zertifikat und seinen unverschlüsselten Private Key enthält. |
| Container Name | Der Name Ihres Blob-Containers. |
| Prefix | Optional. Ein Pfadpräfix für Ihre exportierten Daten innerhalb des Containers. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Felder für Zertifikat-Dienstprinzipal" }

![Die Azure Blob Data Export-Seite in Braze mit ausgewähltem „Certificate Service Principal“, die die Felder „Tenant ID“, „Client ID“, „Account Endpoint“, „Certificate“, „Container Name“ und „Prefix“ zeigt.]({% image_buster /assets/img/azure-currents-cert-sp-3.png %})

Beim Speichern validiert Braze die von Ihnen eingegebenen Zugangsdaten.

Scrollen Sie abschließend zum Ende der Seite und wählen Sie aus, welche Nachricht-Engagement-Events oder Kundenverhalten-Events Sie exportieren möchten. Starten Sie anschließend Ihren Current.

## Aktualisieren der Azure-Zugangsdaten für Currents {#updating-currents-credentials}

Sie können die Azure-Zugangsdaten eines bestehenden Braze-Currents-Konnektors aktualisieren, ohne die Integration zu stoppen oder bereits in Ihren Container exportierte Daten zu verlieren.

Um Zugangsdaten zu erneuern – oder zwischen den Methoden **Connection String** und **Certificate Service Principal** zu wechseln – führen Sie zunächst die Azure-seitigen Schritte für Ihre gewählte Methode weiter oben in diesem Artikel aus. Gehen Sie dann in Braze zu **Currents**, suchen Sie Ihren Azure-Blob-Konnektor in der Liste, wählen Sie **Edit Current** aus, aktualisieren Sie die **Credentials** und wählen Sie **Update Current** aus. Braze validiert die eingegebenen Zugangsdaten; Ihr Konnektor läuft weiter und die bereits in Ihrem Container vorhandenen Daten bleiben verfügbar. Weitere Informationen finden Sie unter [Currents aktualisieren unter „Currents einrichten“]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#updating-currents).

{% alert important %}
Es ist wichtig, Ihr Zertifikat stets aktuell zu halten. Wenn Ihr Zertifikat abläuft, stellt der Konnektor den Versand von Events ein, bis Sie ein gültiges Zertifikat bereitstellen. Eine längere Unterbrechung kann zu Datenverlust führen.
{% endalert %}

## Exportverhalten {#export-behavior}

Nutzer:innen, die eine Cloud-Datenspeicherlösung integriert haben und versuchen, APIs, Dashboard-Berichte oder CSV-Berichte zu exportieren, werden Folgendes feststellen:

- Alle API-Exporte geben keine Download-URL im Antworttext zurück und müssen über den Datenspeicher abgerufen werden.
- Alle Dashboard-Berichte und CSV-Berichte werden zum Download an die E-Mail der Nutzer:innen gesendet (keine Speicherberechtigungen erforderlich) und im Datenspeicher gesichert.

{% alert important %}
**JSON-Formatanforderung**: Für JSON-Exporte verwendet Braze das [JSONL](https://jsonlines.org/)-Format (durch Zeilenumbrüche getrenntes JSON), bei dem jede Zeile ein separates JSON-Objekt enthält. Dieses Format unterscheidet sich von Standard-JSON, das ein einzelnes JSON-Array oder -Objekt ist. Jede Zeile in der exportierten Datei ist ein gültiges JSON-Objekt, aber die Datei als Ganzes ist kein einzelnes gültiges JSON-Dokument. Beim Verarbeiten dieser Dateien sollte jede Zeile einzeln als separates JSON-Objekt geparst werden, anstatt zu versuchen, die gesamte Datei als ein einzelnes JSON-Dokument zu parsen. <br><br> Currents-Exporte verwenden das [Apache Avro](https://avro.apache.org/)-Format (`.avro`-Dateien), nicht JSON. Diese JSON-Formatanforderung gilt für Dashboard-Datenexporte und API-Exporte, die das JSON-Format verwenden.
{% endalert %}

## FAQ

### Kann Braze IP-Adressen für die Freigabeliste von Azure Blob Storage bereitstellen? {#can-braze-provide-ip-addresses-to-allowlist-for-azure-blob-storage}

Braze veröffentlicht keine feste IP-Freigabeliste für Currents oder Dashboard-Exporte nach Azure Blob Storage. Braze schreibt in Ihren Container unter Verwendung der Zugangsdaten und des Containernamens, die Sie angeben, und Azure steuert den Netzwerkzugriff über Ihre Speicherkontoeinstellungen (z. B. Firewallregeln für das Speicherkonto oder private Endpunkte).

Wenn Ihr Sicherheitsteam IP-basierte Einschränkungen benötigt, verwenden Sie die Azure-Netzwerkfunktionen für Ihr Speicherkonto anstelle einer IP-Liste von Braze. Informationen zu den Einrichtungsschritten finden Sie in der [Microsoft-Dokumentation zur Absicherung von Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security).