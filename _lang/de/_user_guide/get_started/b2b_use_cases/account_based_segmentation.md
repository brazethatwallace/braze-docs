---
nav_title: Kontobasierte Segmentierung
article_title: Kontobasierte Segmentierung einrichten
page_order: 2
page_type: reference
description: "Erfahren Sie, wie Sie verschiedene Features von Braze nutzen können, um Ihre Anwendungsfälle für die kontobasierte B2B-Segmentierung umzusetzen."
---

# Kontobasierte Segmentierung einrichten {#set-up-account-based-segmentation}

> Auf dieser Seite erfahren Sie, wie Sie verschiedene Features von Braze nutzen können, um Ihre Anwendungsfälle für die kontobasierte B2B-Segmentierung umzusetzen.

Sie können die kontobasierte B2B-Segmentierung auf zwei Arten durchführen, je nachdem, wie Sie Ihr [B2B-Datenmodell]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models) eingerichtet haben:

- Wenn Sie [Kataloge für Ihre Geschäftsobjekte](#option-1-when-using-catalogs-for-your-business-objects) verwenden
- Wenn Sie [verbundene Quellen für Ihre Geschäftsobjekte](#option-2-when-using-connected-sources-for-your-business-objects) verwenden

## Kontobasierte B2B-Segmentierung einrichten {#setting-up-b2b-account-based-segmentation}

### Option 1: Wenn Sie Kataloge für Ihre Geschäftsobjekte verwenden {#option-1-when-using-catalogs-for-your-business-objects}

#### Grundlegende SQL-Template-Segmentierung {#basic-sql-template-segmentation}

Um Ihnen den Einstieg zu erleichtern, haben wir grundlegende SQL-Templates für eine einfache kontobasierte Segmentierung erstellt.

Nehmen wir an, Sie möchten Nutzer:innen segmentieren, die Mitarbeitende eines Ziel-Unternehmenskontos sind.

1. Gehen Sie zu **Zielgruppe** > **Segmenterweiterungen** > **Neue Erweiterung erstellen** > **Mit einem Template beginnen** und wählen Sie das Template **Katalogsegment für Events** aus. <br><br> ![Modal „Template auswählen“ mit Katalogsegment-Optionen für Events oder Käufe.]({% image_buster /assets/img/b2b/select_a_template.png %})<br><br>Der SQL-Editor wird automatisch mit einem Template befüllt, das Nutzer:innen-Event-Daten mit Katalogdaten verknüpft, um Nutzer:innen zu segmentieren, die mit bestimmten Katalogartikeln interagieren. <br><br>![Ein SQL-Editor für eine neue Erweiterung mit einem geöffneten Tab „Variablen“.]({% image_buster /assets/img/b2b/enter_new_name.png %})<br><br>
2. Verwenden Sie den Tab **Variablen**, um die erforderlichen Felder für Ihr Template bereitzustellen, bevor Sie Ihr Segment generieren.<br><br>Damit Braze Nutzer:innen anhand ihres Engagements mit Katalogartikeln identifizieren kann, müssen Sie Folgendes tun:
- Einen Katalog auswählen, der ein Katalogfeld enthält
- Ein angepasstes Event auswählen, das eine Event-Eigenschaft enthält
- Die Werte Ihres Katalogfelds und Ihrer Event-Eigenschaft abgleichen

##### Leitlinien für Variablen bei B2B-Anwendungsfällen {#variables-guidelines-for-b2b-use-cases}

Wählen Sie die folgenden Variablen für einen Anwendungsfall der kontobasierten B2B-Segmentierung aus:

| Variable | Eigenschaft |
| --- | --- |
| Katalog | Konto-Katalog |
| Katalogfeld | ID |
| Angepasstes Event | account_linked |
| Angepasste Event-Eigenschaft | account_id |
| (Unter SQL-Ergebnisse filtern) Katalogfeld | Klassifizierung |
| (Unter SQL-Ergebnisse filtern) Wert | Enterprise |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Leitlinien für Variablen bei B2B-Anwendungsfällen" }

#### Ausgefeilte SQL-Segmentierung {#sophisticated-sql-segmentation}

Für eine ausgefeiltere oder komplexere Segmentierung lesen Sie den Abschnitt [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments). Um Ihnen den Einstieg zu erleichtern, finden Sie hier einige SQL-Templates, die Ihnen einen Vorsprung bei der kontobasierten B2B-Segmentierung verschaffen:

1. Erstellen Sie ein Segment, das zwei Filter in einem einzigen Katalog vergleicht (z. B. Nutzer:innen, die in der Gastronomie für ein Unternehmenskonto arbeiten). Sie müssen die Katalog-ID und die Artikel-ID angeben.

```sql
WITH salesforce_accounts AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
       MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
   GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_accounts.Classification = 'Enterprise'
;
```

{: start="2"}
2. Erstellen Sie ein Segment, das zwei Filter in zwei separaten Katalogen vergleicht (z. B. Nutzer:innen, die mit Unternehmens-Zielkonten verknüpft sind, die eine offene „Stage 3“-Opportunity haben).

```sql
-- Reformat catalog data into a table with columns for each field
WITH salesforce_accounts AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
       MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
   GROUP BY ITEM_ID
),
salesforce_opportunities AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Account_ID' THEN FIELD_VALUE END) AS Account_ID,
       MAX(CASE WHEN FIELD_NAME = 'Stage' THEN FIELD_VALUE END) AS Stage,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655f84a348f0f0059ad0627' -- salesforce_opportunities
   GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
JOIN salesforce_opportunities
ON salesforce_accounts.id = salesforce_opportunities.Account_ID
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_opportunities.Stage = 'Closed Won'
;
```

### Option 2: Wenn Sie verbundene Quellen für Ihre Geschäftsobjekte verwenden {#option-2-when-using-connected-sources-for-your-business-objects}

Grundlegende Informationen zur Verwendung verbundener Quellen bei der Segmentierung finden Sie unter [CDI-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments). Lassen Sie sich von den Templates unter [Bei der Verwendung von Katalogen](#option-1-when-using-catalogs-for-your-business-objects) inspirieren, wie Sie die Quelltabellen formatieren können – Sie können sie beliebig gestalten.

## Verwendung Ihrer kontobasierten Erweiterung in einem Segment {#using-your-account-based-extension-in-a-segment}

Nachdem Sie Ihre Segmentierung auf Kontoebene in den vorherigen Schritten dieses Abschnitts erstellt haben, können Sie diese Segmenterweiterungen direkt in Ihre Targeting-Kriterien übernehmen. Darüber hinaus lassen sich ganz einfach zusätzliche demografische Kriterien für Nutzer:innen hinzufügen, wie z. B. die Rolle, das Engagement bei früheren Kampagnen und mehr. Weitere Informationen finden Sie unter [Verwendung Ihrer Erweiterung in einem Segment]({{site.baseurl}}/user_guide/audience/segments/segment_extension#step-6-use-your-extension-in-a-segment).