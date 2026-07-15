---
nav_title: Verbundene Quellen
article_title: Verbundene Quellen
description: "Auf dieser Seite erfahren Sie, wie Sie die Cloud-Datenaufnahme von Braze verwenden, um relevante Daten mit Ihrer Snowflake-, Redshift-, BigQuery- und Databricks-Integration zu synchronisieren."
page_order: 2
page_type: reference

---

# Verbundene Quellen {#connected-sources}

> Verbundene Quellen sind eine Zero-Copy-Alternative zur direkten Synchronisierung von Daten mit dem Cloud-Datenaufnahme-Feature (CDI) von Braze. Eine verbundene Quelle fragt direkt Ihr Data Warehouse ab, um neue Segmente zu erstellen, ohne die zugrunde liegenden Daten nach Braze zu kopieren.

Nachdem Sie eine verbundene Quelle zu Ihrem Braze-Workspace hinzugefügt haben, können Sie innerhalb der Segmenterweiterungen ein CDI-Segment erstellen. CDI-Segmenterweiterungen ermöglichen es Ihnen, SQL-Befehle zu schreiben, die direkt Ihr Data Warehouse abfragen (unter Verwendung der Daten, die über Ihre verbundene CDI-Quelle verfügbar sind), und eine Gruppe von Nutzer:innen zu erstellen und zu pflegen, die innerhalb von Braze angesprochen werden können.

Weitere Informationen zum Erstellen eines Segments mit dieser Quelle finden Sie unter [CDI-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments).

{% alert warning %}
Da verbundene Quellen direkt auf Ihrem Data Warehouse laufen, entstehen Ihnen alle Kosten, die mit der Ausführung dieser Abfragen in Ihrem Data Warehouse verbunden sind. Verbundene Quellen protokollieren keine Datenpunkte, und CDI-Segmenterweiterungen verbrauchen keine SQL-Segment-Credits.
{% endalert %}

## Integration verbundener Quellen {#integrating-connected-sources}

### 1. Schritt: Verbinden Sie Ihre Ressourcen {#step-1-connect-your-resources}

Verbundene Quellen für die Cloud-Datenaufnahme erfordern einige Einstellungen in Braze und in Ihrer Instanz. Folgen Sie diesen Schritten, um die Integration einzurichten&#8722;einige Schritte werden in Ihrem Data Warehouse und einige im Braze-Dashboard durchgeführt.

{% tabs %}
{% tab Snowflake %}
**In Ihrem Data Warehouse**
1. Erstellen Sie eine Rolle und erteilen Sie Berechtigungen zum Abfragen und Erstellen von Tabellen in einem Schema.
2. Richten Sie Ihr Warehouse ein und geben Sie dieser Rolle Zugriff.
3. Erstellen Sie eine Nutzer:in für diese Rolle.
4. Je nach Ihrer Konfiguration müssen Sie möglicherweise Braze-IPs in Ihrer Snowflake-Netzwerkrichtlinie zulassen.

**Im Braze-Dashboard**

{: start="5"}
5. Erstellen Sie eine neue verbundene Quelle im Braze-Dashboard.
6. Konfigurieren Sie die Synchronisierungsdetails für die verbundene Quelle.
7. Rufen Sie den im Braze-Dashboard bereitgestellten Public Key ab.

**In Ihrem Data Warehouse**

{: start="8"}
8. Hängen Sie den Public Key aus dem Braze-Dashboard an die [Snowflake-Nutzer:in zur Authentifizierung](https://docs.snowflake.com/en/user-guide/key-pair-auth.html) an. Wenn Sie fertig sind, können Sie die verbundene Quelle verwenden, um eine oder mehrere CDI-Segmenterweiterungen zu erstellen.
{% endtab %}

{% tab Redshift %}
1. Richten Sie die Quelldaten und die erforderlichen Ressourcen in Ihrer Redshift-Umgebung ein.
2. Erstellen Sie eine neue verbundene Quelle im Braze-Dashboard.
3. Testen Sie die Integration.
4. Verwenden Sie die verbundene Quelle, um eine oder mehrere CDI-Segmenterweiterungen zu erstellen.
{% endtab %}

{% tab BigQuery %}
1. Richten Sie die Quelldaten und die erforderlichen Ressourcen in Ihrer BigQuery-Umgebung ein.
2. Erstellen Sie ein Dienstkonto und erlauben Sie den Zugriff auf die BigQuery-Projekte und -Datensätze, die die zu synchronisierenden Daten enthalten.
3. Erstellen Sie eine neue verbundene Quelle im Braze-Dashboard.
4. Testen Sie die Integration.
5. Verwenden Sie die verbundene Quelle, um eine oder mehrere CDI-Segmenterweiterungen zu erstellen.
{% endtab %}

{% tab Databricks %}
1. Richten Sie die Quelldaten und die erforderlichen Ressourcen in Ihrer Databricks-Umgebung ein.
2. Erstellen Sie ein Dienstkonto und erlauben Sie den Zugriff auf die Databricks-Projekte und -Datensätze, die die zu synchronisierenden Daten enthalten.
3. Erstellen Sie eine neue verbundene Quelle im Braze-Dashboard.
4. Testen Sie die Integration.
5. Verwenden Sie die verbundene Quelle, um eine oder mehrere CDI-Segmenterweiterungen zu erstellen.

{% alert important %}
Es kann zu einer Aufwärmzeit von zwei bis fünf Minuten kommen, wenn Braze eine Verbindung zu Classic- und Pro-SQL-Instanzen herstellt. Dies kann zu Verzögerungen beim Einrichten und Testen der Verbindung sowie beim Erstellen und Aktualisieren von CDI-Segmenterweiterungen führen. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann aber zu etwas höheren Integrationskosten führen.
{% endalert %}

{% endtab %}

{% tab Microsoft Fabric %}
1. Erstellen Sie einen Dienstprinzipal und erlauben Sie den Zugriff auf den Fabric-Workspace, der für Ihre Integration verwendet werden soll.
2. Richten Sie in Ihrem Fabric-Workspace die Quelldaten ein und erteilen Sie Ihrem Dienstprinzipal Berechtigungen.
3. Erstellen Sie eine neue verbundene Quelle im Braze-Dashboard.
4. Testen Sie die Integration.
5. Verwenden Sie die verbundene Quelle, um eine oder mehrere CDI-Segmenterweiterungen zu erstellen.
{% endtab %}

{% endtabs %}

### 2. Schritt: Richten Sie Ihr Data Warehouse ein {#step-2-set-up-your-data-warehouse}

Richten Sie die Quelldaten und die erforderlichen Ressourcen in Ihrer Data-Warehouse-Umgebung ein. Die verbundene Quelle kann auf eine oder mehrere Tabellen verweisen. Stellen Sie daher sicher, dass Ihre Braze-Nutzer:in die Berechtigung hat, auf alle Tabellen zuzugreifen, die Sie in der verbundenen Quelle verwenden möchten.

{% tabs %}
{% tab Snowflake %}
#### Schritt 2.1: Rolle erstellen und Berechtigungen erteilen {#step-21-create-a-role-and-grant-permissions}

Erstellen Sie eine Rolle für Ihre verbundene Quelle. Diese Rolle wird verwendet, um die Liste der in Ihren CDI-Segmenterweiterungen verfügbaren Tabellen zu generieren und Quelltabellen abzufragen, um neue Segmente zu erstellen. Nachdem die verbundene Quelle erstellt wurde, ermittelt Braze die Namen und Beschreibungen aller Tabellen, die der Nutzer:in im Quellschema zur Verfügung stehen.

Sie können wählen, ob Sie Zugriff auf alle Tabellen in einem Schema gewähren oder nur auf bestimmte Tabellen. Alle Tabellen, auf die die Braze-Rolle Zugriff hat, können in der CDI-Segmenterweiterung abgefragt werden.

Die Berechtigung `create table` ist erforderlich, damit Braze eine Tabelle mit den Ergebnissen Ihrer CDI-Segmenterweiterungsabfrage erstellen kann, bevor das Segment in Braze aktualisiert wird. Braze erstellt eine temporäre Tabelle pro Segment, die nur so lange bestehen bleibt, wie Braze das Segment aktualisiert.

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT CREATE TABLE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to all current and future tables or views in the schema
GRANT SELECT ON ALL TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to specific tables or views in the schema
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;

```

#### Schritt 2.2: Warehouse einrichten und der Braze-Rolle Zugriff gewähren {#step-22-set-up-the-warehouse-and-give-access-to-braze-role}

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
Für das Warehouse muss die Option **Auto-Resume** aktiviert sein. Ist dies nicht der Fall, müssen Sie Braze zusätzliche `OPERATE`-Berechtigungen für das Warehouse erteilen, damit Braze es aktivieren kann, wenn die Abfrage ausgeführt werden soll.
{% endalert %}

#### Schritt 2.3: Nutzer:in einrichten {#step-23-set-up-the-user}
```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Sie teilen die Verbindungsinformationen mit Braze und erhalten einen Public Key, den Sie in einem späteren Schritt an die Nutzer:in anhängen.

{% alert note %}
Wenn Sie verschiedene Workspaces mit demselben Snowflake-Konto verbinden, müssen Sie für jeden Braze-Workspace, in dem Sie eine Integration erstellen, eine eigene Nutzer:in anlegen. Innerhalb eines Workspace können Sie dieselbe Nutzer:in für verschiedene Integrationen wiederverwenden. Die Erstellung einer Integration schlägt jedoch fehl, wenn eine Nutzer:in desselben Snowflake-Kontos in verschiedenen Workspaces dupliziert wird.
{% endalert %}

#### Schritt 2.4: Braze-IPs in Ihrer Snowflake-Netzwerkrichtlinie zulassen (optional) {#step-24-allow-braze-ips-in-your-snowflake-network-policy-optional}

Je nach Konfiguration Ihres Snowflake-Kontos müssen Sie möglicherweise die folgenden IP-Adressen in Ihrer Snowflake-Netzwerkrichtlinie zulassen. Weitere Informationen hierzu finden Sie in der entsprechenden Snowflake-Dokumentation zum [Ändern einer Netzwerkrichtlinie](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}
{% endtab %}

{% tab Redshift %}
#### Schritt 2.1: Nutzer:in anlegen und Berechtigungen erteilen {#step-21-create-user-and-grant-permissions}

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Erstellen Sie eine Nutzer:in für Ihre verbundene Quelle. Diese Nutzer:in wird verwendet, um die Liste der in Ihren CDI-Segmenterweiterungen verfügbaren Tabellen zu generieren und Quelltabellen abzufragen, um neue Segmente zu erstellen. Nachdem die verbundene Quelle erstellt wurde, ermittelt Braze die Namen und Beschreibungen aller Tabellen, die der Nutzer:in im Quellschema zur Verfügung stehen. Wenn Sie mehrere CDI-Integrationen erstellen, möchten Sie möglicherweise Berechtigungen für ein Schema erteilen oder Berechtigungen über eine Gruppe verwalten.

Sie können wählen, ob Sie Zugriff auf alle Tabellen in einem Schema gewähren oder nur auf bestimmte Tabellen. Alle Tabellen, auf die die Braze-Rolle Zugriff hat, können in der CDI-Segmenterweiterung abgefragt werden. Stellen Sie sicher, dass Sie der Nutzer:in bei der Erstellung neuer Tabellen Zugriff gewähren oder Standardberechtigungen für die Nutzer:in festlegen.

Die Berechtigung `create table` ist erforderlich, damit Braze eine Tabelle mit den Ergebnissen Ihrer CDI-Segmenterweiterungsabfrage erstellen kann, bevor das Segment in Braze aktualisiert wird. Braze erstellt eine temporäre Tabelle pro Segment, die nur so lange bestehen bleibt, wie Braze das Segment aktualisiert.


#### Schritt 2.2: Zugriff auf Braze-IPs zulassen {#step-22-allow-access-to-braze-ips}

Wenn Sie eine Firewall oder andere Netzwerkrichtlinien haben, müssen Sie Braze Netzwerkzugriff auf Ihre Redshift-Instanz gewähren. Erlauben Sie den Zugriff von den folgenden IPs, die der Region Ihres Braze-Dashboards entsprechen.

Möglicherweise müssen Sie auch Ihre Sicherheitsgruppen ändern, um Braze den Zugriff auf Ihre Daten in Redshift zu ermöglichen. Stellen Sie sicher, dass Sie eingehenden Datenverkehr auf den IPs im folgenden Abschnitt und auf dem Port, der für die Abfrage Ihres Redshift-Clusters verwendet wird (Standard ist 5439), ausdrücklich zulassen. Sie sollten Redshift-TCP-Konnektivität auf diesem Port explizit erlauben, auch wenn die eingehenden Regeln auf „alles erlauben“ eingestellt sind. Darüber hinaus ist es wichtig, dass der Endpunkt für den Redshift-Cluster öffentlich zugänglich ist, damit Braze eine Verbindung zu Ihrem Cluster herstellen kann.

Wenn Sie nicht möchten, dass Ihr Redshift-Cluster öffentlich zugänglich ist, können Sie eine VPC und eine EC2-Instanz einrichten, die einen SSH-Tunnel für den Zugriff auf die Redshift-Daten verwenden. Weitere Informationen finden Sie unter [AWS: Wie greife ich von meinem lokalen Rechner aus auf einen privaten Amazon-Redshift-Cluster zu?](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab BigQuery %}
#### Schritt 2.1: Dienstkonto erstellen und Berechtigungen erteilen {#step-21-create-a-service-account-and-grant-permissions}

Erstellen Sie ein Dienstkonto in GCP, das Braze verwenden kann, um eine Verbindung herzustellen und Daten aus Ihren Tabellen zu lesen. Das Dienstkonto sollte über die folgenden Berechtigungen verfügen:

- **BigQuery Connection User:** Ermöglicht es Braze, Verbindungen herzustellen.
- **BigQuery User:** Ermöglicht Braze den Zugriff zum Ausführen von Abfragen, Lesen von Datensatz-Metadaten und Auflisten von Tabellen.
- **BigQuery Data Viewer:** Ermöglicht Braze den Zugriff zum Anzeigen von Datensätzen und deren Inhalten.
- **BigQuery Job User:** Ermöglicht Braze den Zugriff zum Ausführen von Jobs.
- **bigquery.tables.create:** Ermöglicht Braze den Zugriff zum Erstellen temporärer Tabellen während der Segmentaktualisierung.

Erstellen Sie ein Dienstkonto für Ihre verbundene Quelle. Dieses Dienstkonto wird verwendet, um die Liste der in Ihren CDI-Segmenterweiterungen verfügbaren Tabellen zu generieren und Quelltabellen abzufragen, um neue Segmente zu erstellen. Nachdem die verbundene Quelle erstellt wurde, ermittelt Braze die Namen und Beschreibungen aller Tabellen, die dem Dienstkonto im Quellschema zur Verfügung stehen.

Sie können wählen, ob Sie Zugriff auf alle Tabellen in einem Datensatz gewähren oder nur auf bestimmte Tabellen. Alle Tabellen, auf die die Braze-Rolle Zugriff hat, können in der CDI-Segmenterweiterung abgefragt werden.

Die Berechtigung `create table` ist erforderlich, damit Braze eine Tabelle mit den Ergebnissen Ihrer CDI-Segmenterweiterungsabfrage erstellen kann, bevor das Segment in Braze aktualisiert wird. Braze erstellt eine temporäre Tabelle pro Segment, die nur so lange bestehen bleibt, wie Braze das Segment aktualisiert.

Nachdem Sie das Dienstkonto erstellt und die Berechtigungen erteilt haben, generieren Sie einen JSON-Schlüssel. Weitere Informationen finden Sie unter [Google Cloud: Schlüssel für Dienstkonten erstellen und löschen](https://cloud.google.com/iam/docs/keys-create-delete). Sie laden diesen später in das Braze-Dashboard hoch.

#### Schritt 2.2: Zugriff auf Braze-IPs zulassen

Wenn Sie Netzwerkrichtlinien eingerichtet haben, müssen Sie Braze Netzwerkzugriff auf Ihre BigQuery-Instanz gewähren. Erlauben Sie den Zugriff von den folgenden IPs, die der Region Ihres Braze-Dashboards entsprechen.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Databricks %}
#### Schritt 2.1: Zugriffstoken erstellen {#step-21-create-an-access-token}

Damit Braze auf Databricks zugreifen kann, muss ein persönliches Zugriffstoken erstellt werden.

1. Wählen Sie in Ihrem Databricks-Workspace Ihren Databricks-Benutzernamen in der oberen Leiste aus und wählen Sie dann **User Settings** aus dem Dropdown-Menü.
2. Stellen Sie sicher, dass das Dienstkonto über `CREATE TABLE`-Berechtigungen für das Schema verfügt, das für die verbundene Quelle verwendet wird.
3. Wählen Sie auf dem Tab **Access tokens** die Option **Generate new token**.
4. Geben Sie einen Kommentar ein, der Ihnen hilft, dieses Token zu identifizieren, z. B. „Braze CDI“, und ändern Sie die Lebensdauer des Tokens auf „keine Lebensdauer“, indem Sie das Feld „Lifetime (days)“ leer lassen.
5. Wählen Sie **Generate**.
6. Kopieren Sie das angezeigte Token und wählen Sie dann **Done**.

Dieses Token wird verwendet, um die Liste der in Ihren CDI-Segmenterweiterungen verfügbaren Tabellen zu generieren und Quelltabellen abzufragen, um neue Segmente zu erstellen. Nachdem die verbundene Quelle erstellt wurde, ermittelt Braze die Namen und Beschreibungen aller Tabellen, die der Nutzer:in im Quellschema zur Verfügung stehen.

Sie können wählen, ob Sie Zugriff auf alle Tabellen in einem Schema gewähren oder nur auf bestimmte Tabellen. Alle Tabellen, auf die die Braze-Rolle Zugriff hat, können in der CDI-Segmenterweiterung abgefragt werden.

Die Berechtigung `create table` ist erforderlich, damit Braze eine Tabelle mit den Ergebnissen Ihrer CDI-Segmenterweiterungsabfrage erstellen kann, bevor das Segment in Braze aktualisiert wird. Braze erstellt eine temporäre Tabelle pro Segment, die nur so lange bestehen bleibt, wie Braze das Segment aktualisiert.

Bewahren Sie das Token an einem sicheren Ort auf, bis Sie es im Braze-Dashboard während des Schritts zur Erstellung der Zugangsdaten eingeben müssen.

#### Schritt 2.2: Zugriff auf Braze-IPs zulassen

Wenn Sie Netzwerkrichtlinien eingerichtet haben, müssen Sie Braze Netzwerkzugriff auf Ihre Databricks-Instanz gewähren. Erlauben Sie den Zugriff von den folgenden IPs, die der Region Ihres Braze-Dashboards entsprechen.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Microsoft Fabric %}
#### Schritt 2.1: Zugriff auf Fabric-Ressourcen gewähren {#step-21-grant-access-to-fabric-resources}
Braze stellt die Verbindung zu Ihrem Fabric-Warehouse über einen Dienstprinzipal mit Entra-ID-Authentifizierung her. Sie erstellen einen neuen Dienstprinzipal, den Braze verwenden kann, und gewähren bei Bedarf Zugriff auf Fabric-Ressourcen. Braze benötigt für die Verbindung die folgenden Angaben:

* Tenant-ID (auch Verzeichnis-ID genannt) für Ihr Azure-Konto
* Principal-ID (auch Anwendungs-ID genannt) für den Dienstprinzipal
* Client-Secret für die Authentifizierung von Braze

1. Navigieren Sie im Azure-Portal zum Microsoft Entra Admin Center und dann zu **App Registrations**.
2. Wählen Sie **+ New registration** unter **Identity > Applications > App registrations**.
3. Geben Sie einen Namen ein und wählen Sie `Accounts in this organizational directory only` als unterstützten Kontotyp aus. Wählen Sie dann **Register**.
4. Wählen Sie die soeben erstellte Anwendung (Dienstprinzipal) aus und navigieren Sie zu **Certificates & secrets > + New client secret**.
5. Geben Sie eine Beschreibung für das Secret ein und legen Sie einen Ablaufzeitraum fest. Wählen Sie dann **Add**.
6. Notieren Sie sich das erstellte Client-Secret für die Einrichtung von Braze.

{% alert note %}
Azure erlaubt keinen unbegrenzten Ablauf von Dienstprinzipal-Secrets. Denken Sie daran, die Zugangsdaten zu aktualisieren, bevor sie ablaufen, damit der Datenfluss zu Braze aufrechterhalten wird.
{% endalert %}

#### Schritt 2.2: Zugriff auf Fabric-Ressourcen gewähren {#step-22-grant-access-to-fabric-resources}
Sie gewähren Braze den Zugriff auf Ihre Fabric-Instanz. Navigieren Sie in Ihrem Fabric-Administrationsportal zu **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**.

* Aktivieren Sie in den **Developer settings** die Option „Service principals can use Fabric APIs“, damit Braze sich über die Microsoft Entra-ID verbinden kann.
* Aktivieren Sie in den **OneLake settings** die Option „Users can access data stored in OneLake with apps external to Fabric“, damit der Dienstprinzipal auf Daten aus einer externen App zugreifen kann.

#### Schritt 2.3: Warehouse-Verbindungszeichenfolge abrufen {#step-23-get-warehouse-connection-string}

Sie benötigen den SQL-Endpunkt für Ihr Warehouse, damit Braze eine Verbindung herstellen kann. Um den SQL-Endpunkt abzurufen, rufen Sie den **Workspace** in Fabric auf. Bewegen Sie in der Liste der Elemente den Mauszeiger über den Warehouse-Namen und wählen Sie **Copy SQL connection string**.
Halten Sie diesen Wert für die Einrichtung der Zugangsdaten in Schritt 3 bereit.

#### Schritt 2.4: Braze-IPs in der Firewall zulassen (optional) {#step-24-allow-braze-ips-in-firewall-optional}

Je nach Konfiguration Ihres Microsoft-Fabric-Kontos müssen Sie möglicherweise die folgenden IP-Adressen in Ihrer Firewall zulassen, um den Datenverkehr von Braze zu ermöglichen. Weitere Informationen finden Sie in der entsprechenden Dokumentation zu [Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### 3. Schritt: Erstellen Sie eine verbundene Quelle im Braze-Dashboard {#step-3-create-a-connected-source-in-the-braze-dashboard}

{% tabs %}
{% tab Snowflake %}
#### Schritt 3.1: Snowflake-Verbindungsinformationen und Quelltabelle hinzufügen {#step-31-add-snowflake-connection-information-and-source-table}

Erstellen Sie eine verbundene Quelle im Braze-Dashboard. Gehen Sie zu **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, wählen Sie **Add data source** und dann **Snowflake**.

Geben Sie unter **Setup source** Folgendes ein:
- **Credentials:** **Account Locator**, **Username** und **Role**
- **Configuration:** **Warehouse**, **Database** und **Schema**

Wenn Sie neue Snowflake-Zugangsdaten erstellen, wählen Sie **Save credentials and generate RSA key**, bevor Sie die Verbindung testen.

#### Schritt 3.2: Synchronisierungsdetails konfigurieren {#step-32-configure-sync-details}

Wählen Sie einen Namen für die verbundene Quelle. Dieser Name wird in der Liste der verfügbaren Quellen angezeigt, wenn Sie eine neue CDI-Segmenterweiterung erstellen.

Legen Sie eine maximale Laufzeit für diese Quelle fest. Braze bricht automatisch alle Abfragen ab, die die maximale Laufzeit überschreiten. Die maximal zulässige Laufzeit beträgt 60 Minuten; eine geringere Laufzeit reduziert die Kosten für Ihr Snowflake-Konto. Diese Einstellung gilt für Abfragen, die über diese Quelle ausgeführt werden, einschließlich Synchronisierungen und CDI-Segmenterweiterungen, die sie verwenden.

{% alert note %}
Wenn Abfragen regelmäßig das Zeitlimit überschreiten und Sie eine maximale Laufzeit von 60 Minuten festgelegt haben, sollten Sie versuchen, die Ausführungszeit Ihrer Abfragen zu optimieren oder der Braze-Nutzer:in ein größeres Warehouse zuzuweisen.
{% endalert %}

#### Schritt 3.3: Public Key notieren {#step-33-note-the-public-key}

Notieren Sie sich im Schritt **Test connection** den öffentlichen RSA-Schlüssel. Sie benötigen ihn, um die Integration in Snowflake abzuschließen.

{% endtab %}
{% tab Redshift %}
#### Schritt 3.1: Redshift-Verbindungsinformationen und Quelltabelle hinzufügen {#step-31-add-redshift-connection-information-and-source-table}

Erstellen Sie eine verbundene Quelle im Braze-Dashboard. Gehen Sie zu **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, wählen Sie **Add data source** und dann **Amazon Redshift**.

Geben Sie unter **Setup source** Folgendes ein:
- **Credentials:** **Redshift Host URL**, **Username**, **Password** und **Port**
- **Configuration:** **Database** und **Schema**

Aktivieren Sie bei Bedarf **Connect with SSH Tunnel** und geben Sie **Tunnel Host**, **Tunnel Port** und **Tunnel Username** ein.

#### Schritt 3.2: Synchronisierungsdetails konfigurieren

Wählen Sie einen Namen für die verbundene Quelle. Dieser Name wird in der Liste der verfügbaren Quellen angezeigt, wenn Sie eine neue CDI-Segmenterweiterung erstellen.

Legen Sie eine maximale Laufzeit für diese Quelle fest. Braze bricht automatisch alle Abfragen ab, die die maximale Laufzeit überschreiten. Die maximal zulässige Laufzeit beträgt 60 Minuten; eine geringere Laufzeit reduziert die Kosten für Ihr Redshift-Konto.
Diese Einstellung gilt für Abfragen, die über diese Quelle ausgeführt werden, einschließlich Synchronisierungen und CDI-Segmenterweiterungen, die sie verwenden.

{% alert note %}
Wenn Abfragen regelmäßig das Zeitlimit überschreiten und Sie eine maximale Laufzeit von 60 Minuten festgelegt haben, sollten Sie versuchen, die Ausführungszeit Ihrer Abfragen zu optimieren oder der Braze-Nutzer:in ein größeres Warehouse zuzuweisen.
{% endalert %}

#### Schritt 3.3: Public Key notieren (optional) {#step-33-note-the-public-key-optional}

Wenn in Ihren Zugangsdaten die Option **Connect with SSH Tunnel** ausgewählt ist, notieren Sie sich den öffentlichen RSA-Schlüssel im Schritt **Test connection**. Sie benötigen ihn, um die Integration in Redshift abzuschließen.

{% endtab %}
{% tab BigQuery %}
#### Schritt 3.1: BigQuery-Verbindungsinformationen und Quelltabelle hinzufügen {#step-31-add-bigquery-connection-information-and-source-table}

Erstellen Sie eine verbundene Quelle im Braze-Dashboard. Gehen Sie zu **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, wählen Sie **Add data source** und dann **Google BigQuery**.

Geben Sie unter **Setup source** Folgendes ein:
- **Credentials:** **Credential name** und laden Sie Ihren **JSON key** hoch
- **Configuration:** **Project** und **Dataset**

#### Schritt 3.2: Synchronisierungsdetails konfigurieren

Wählen Sie einen Namen für die verbundene Quelle. Dieser Name wird in der Liste der verfügbaren Quellen angezeigt, wenn Sie eine neue CDI-Segmenterweiterung erstellen.

Legen Sie eine maximale Laufzeit für diese Quelle fest. Braze bricht automatisch alle Abfragen ab, die die maximale Laufzeit überschreiten. Die maximal zulässige Laufzeit beträgt 60 Minuten; eine geringere Laufzeit reduziert die Kosten für Ihr BigQuery-Konto. Diese Einstellung gilt für Abfragen, die über diese Quelle ausgeführt werden, einschließlich Synchronisierungen und CDI-Segmenterweiterungen, die sie verwenden.

{% alert note %}
Wenn Abfragen regelmäßig das Zeitlimit überschreiten und Sie eine maximale Laufzeit von 60 Minuten festgelegt haben, sollten Sie versuchen, die Ausführungszeit Ihrer Abfragen zu optimieren oder der Braze-Nutzer:in ein größeres Warehouse zuzuweisen.
{% endalert %}

#### Schritt 3.3: Verbindung testen {#step-33-test-the-connection}

Wählen Sie **Test Connection**, um zu überprüfen, ob die Liste der für die Nutzer:in sichtbaren Tabellen Ihren Erwartungen entspricht, und wählen Sie dann **Done**. Ihre verbundene Quelle ist nun erstellt und kann in CDI-Segmenterweiterungen verwendet werden.

{% endtab %}
{% tab Databricks %}
#### Schritt 3.1: Databricks-Verbindungsinformationen und Quelltabelle hinzufügen {#step-31-add-databricks-connection-information-and-source-table}

Erstellen Sie eine verbundene Quelle im Braze-Dashboard. Gehen Sie zu **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, wählen Sie **Add data source** und dann **Databricks**.

Geben Sie unter **Setup source** Folgendes ein:
- **Credentials:** **Credential Name**, **Hostname**, **HTTP Path** und **Access Token**
- **Configuration:** **Catalog** und **Schema**

#### Schritt 3.2: Synchronisierungsdetails konfigurieren

Wählen Sie einen Namen für die verbundene Quelle. Dieser Name wird in der Liste der verfügbaren Quellen angezeigt, wenn Sie eine neue CDI-Segmenterweiterung erstellen.

Legen Sie eine maximale Laufzeit für diese Quelle fest. Braze bricht automatisch alle Abfragen ab, die die maximale Laufzeit überschreiten. Die maximal zulässige Laufzeit beträgt 60 Minuten; eine geringere Laufzeit reduziert die Kosten für Ihr Databricks-Konto. Diese Einstellung gilt für Abfragen, die über diese Quelle ausgeführt werden, einschließlich Synchronisierungen und CDI-Segmenterweiterungen, die sie verwenden.

{% alert note %}
Wenn Abfragen regelmäßig das Zeitlimit überschreiten und Sie eine maximale Laufzeit von 60 Minuten festgelegt haben, sollten Sie versuchen, die Ausführungszeit Ihrer Abfragen zu optimieren oder der Braze-Nutzer:in ein größeres Warehouse zuzuweisen.
{% endalert %}

#### Schritt 3.3: Verbindung testen

Wählen Sie **Test Connection**, um zu überprüfen, ob die Liste der für die Nutzer:in sichtbaren Tabellen Ihren Erwartungen entspricht, und wählen Sie dann **Done**. Ihre verbundene Quelle ist nun erstellt und kann in CDI-Segmenterweiterungen verwendet werden.

{% endtab %}
{% tab Microsoft Fabric %}
#### Schritt 3.1: Microsoft-Fabric-Verbindungsinformationen und Quelltabelle hinzufügen {#step-31-add-microsoft-fabric-connection-information-and-source-table}

Erstellen Sie eine verbundene Quelle im Braze-Dashboard. Gehen Sie zu **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, wählen Sie **Add data source** und dann **Microsoft Fabric**.

Geben Sie unter **Setup source** Folgendes ein:
- **Credentials:** **Credentials Name**, **Tenant ID**, **Principal ID**, **Client Secret** und **Connection String**
- **Configuration:** **Database** und **Schema**

Wenn **Connect with SSH Tunnel** in Ihrem Workspace verfügbar und für Ihre Einrichtung erforderlich ist, geben Sie zusätzlich **Tunnel Host**, **Tunnel Port** und **Tunnel Username** ein.

#### Schritt 3.2: Synchronisierungsdetails konfigurieren

Wählen Sie einen Namen für die verbundene Quelle. Dieser Name wird in der Liste der verfügbaren Quellen angezeigt, wenn Sie eine neue CDI-Segmenterweiterung erstellen.

Legen Sie eine maximale Laufzeit für diese Quelle fest. Braze bricht automatisch alle Abfragen ab, die die maximale Laufzeit überschreiten. Die maximal zulässige Laufzeit beträgt 60 Minuten; eine geringere Laufzeit reduziert die Kosten für Ihr Microsoft-Fabric-Konto. Diese Einstellung gilt für Abfragen, die über diese Quelle ausgeführt werden, einschließlich Synchronisierungen und CDI-Segmenterweiterungen, die sie verwenden.

{% alert note %}
Wenn Abfragen regelmäßig das Zeitlimit überschreiten und Sie eine maximale Laufzeit von 60 Minuten festgelegt haben, sollten Sie versuchen, die Ausführungszeit der Abfrage zu optimieren oder die Fabric-Kapazität zu skalieren.
{% endalert %}

#### Schritt 3.3: Verbindung testen

Wählen Sie **Test Connection**, um zu überprüfen, ob die Liste der für die Nutzer:in sichtbaren Tabellen Ihren Erwartungen entspricht, und wählen Sie dann **Done**. Ihre verbundene Quelle ist nun erstellt und kann in CDI-Segmenterweiterungen verwendet werden.

{% endtab %}
{% endtabs %}

### 4. Schritt: Data-Warehouse-Konfiguration abschließen {#step-4-finalize-the-data-warehouse-configuration}

{% tabs %}
{% tab Snowflake %}
Fügen Sie den Public Key, den Sie im letzten Schritt notiert haben, zu Ihrer Nutzer:in in Snowflake hinzu. Dadurch kann Braze eine Verbindung zu Snowflake herstellen. Einzelheiten dazu finden Sie in der [Snowflake-Dokumentation](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).

Wenn Sie die Schlüssel irgendwann rotieren möchten, können Sie einen neuen Public Key erstellen, indem Sie unter **Data Access Management** in **Cloud Data Ingestion** die Option **Generate New Key** für das jeweilige Konto wählen.

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Nachdem Sie den Schlüssel zur Nutzer:in in Snowflake hinzugefügt haben, wählen Sie in Braze **Test Connection** und dann **Done**. Ihre verbundene Quelle ist nun erstellt und kann in CDI-Segmenterweiterungen verwendet werden.
{% endtab %}

{% tab Redshift %}
Wenn Sie eine Verbindung über einen SSH-Tunnel herstellen, fügen Sie den Public Key, den Sie im letzten Schritt notiert haben, der SSH-Tunnel-Nutzer:in hinzu.

Nachdem Sie den Schlüssel zur Nutzer:in hinzugefügt haben, wählen Sie in Braze **Test Connection** und dann **Done**. Ihre verbundene Quelle ist nun erstellt und kann in CDI-Segmenterweiterungen verwendet werden.

{% endtab %}
{% tab BigQuery %}
Dies gilt nicht für BigQuery.

{% endtab %}
{% tab Databricks %}
Dies gilt nicht für Databricks.

{% endtab %}
{% tab Microsoft Fabric %}
Dies gilt nicht für Microsoft Fabric.

{% endtab %}
{% endtabs %}

{% alert note %}
Sie müssen eine Quelle erfolgreich testen, bevor sie vom Status „Entwurf“ in den Status „Aktiv“ übergehen kann. Wenn Sie die Erstellungsseite verlassen müssen, wird Ihre Integration gespeichert, und Sie können die Detailseite erneut aufrufen, um Änderungen vorzunehmen und zu testen.
{% endalert %}

## Einrichten zusätzlicher Integrationen oder Nutzer:innen (optional) {#setting-up-additional-integrations-or-users-optional}

{% tabs %}
{% tab Snowflake %}
Sie können mehrere Integrationen mit Braze einrichten, aber jede Integration sollte so konfiguriert werden, dass sie ein anderes Schema verbindet. Wenn Sie zusätzliche Verbindungen erstellen, können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben Snowflake-Konto verbinden.

Wenn Sie dieselbe Nutzer:in und dieselbe Rolle bei verschiedenen Integrationen wiederverwenden, müssen Sie den Public Key nicht erneut hinzufügen.
{% endtab %}

{% tab Redshift %}
Sie können mit Braze mehrere Quellen einrichten, aber jede Quelle sollte so konfiguriert werden, dass sie ein anderes Schema verbindet. Wenn Sie zusätzliche Quellen erstellen, können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben Redshift-Konto verbinden.
{% endtab %}

{% tab BigQuery %}
Sie können mit Braze mehrere Quellen einrichten, aber jede Quelle sollte so konfiguriert werden, dass sie einen anderen Datensatz verbindet. Wenn Sie zusätzliche Quellen erstellen, können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben BigQuery-Konto verbinden.
{% endtab %}

{% tab Databricks %}
Sie können mit Braze mehrere Quellen einrichten, aber jede Quelle sollte so konfiguriert werden, dass sie ein anderes Schema verbindet. Wenn Sie zusätzliche Quellen erstellen, können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben Databricks-Konto verbinden.
{% endtab %}

{% tab Microsoft Fabric %}
Sie können mit Braze mehrere Quellen einrichten, aber jede Quelle sollte so konfiguriert werden, dass sie ein anderes Schema verbindet. Wenn Sie zusätzliche Quellen erstellen, können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben Azure-Konto verbinden.
{% endtab %}
{% endtabs %}

## Verwendung der verbundenen Quelle {#using-the-connected-source}

Nachdem die Quelle erstellt wurde, können Sie damit eine oder mehrere CDI-Segmenterweiterungen erstellen. Weitere Informationen zum Erstellen eines Segments mit dieser Quelle finden Sie in der [Dokumentation zu CDI-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments).

{% alert note %}
Wenn Abfragen regelmäßig das Zeitlimit überschreiten und Sie eine maximale Laufzeit von 60 Minuten festgelegt haben, sollten Sie versuchen, die Ausführungszeit Ihrer Abfragen zu optimieren oder der Braze-Nutzer:in mehr Rechenressourcen (z. B. ein größeres Warehouse) zuzuweisen.
{% endalert %}