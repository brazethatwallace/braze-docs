---
nav_title: Scuba
article_title: Scuba Analytics
description: "Diese technische Referenz von Scuba und Braze beschreibt, wie Sie die Realtime-Daten-Insights von Scuba mit Segmenten von Braze aktivieren."
page_type: partner
search_tag: Partner
noindex: true
hidden: true
---

# Scuba Analytics

>[Scuba Analytics](https://scuba.io) ist eine Full-Stack-Plattform für die Zusammenarbeit mit maschinellem Lernen, die für schnelle Zeitreihendaten entwickelt wurde. Scuba erlaubt es Ihnen, Nutzer:innen (auch Akteure genannt) selektiv zu exportieren und in Ihre Braze-Plattform zu laden. In Scuba werden angepasste Eigenschaften von Akteuren verwendet, um Verhaltenstrends zu analysieren, Ihre Daten über verschiedene Plattformen hinweg zu aktivieren und mithilfe von maschinellem Lernen Prognosen zu erstellen.

_Diese Integration wird von Scuba Analytics gepflegt._

## Voraussetzungen {#prerequisites}

Um Scuba Analytics mit Braze zu verwenden, benötigen Sie Folgendes:

| Anforderung | Beschreibung |
|---|---|
| Scuba API-Token | Ein Scuba API-Token, das Sie über den Endpunkt `https://{scuba_hostname}/api/create_token` abrufen können. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST-Endpunkt  | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz](https://scuba.io) ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Hochladen Ihrer Scuba-Daten auf Braze {#uploading-your-scuba-data-to-braze}

{% alert important %}
Die folgende Anfrage verwendet curl. Für eine bessere Verwaltung von API-Anfragen empfehlen wir die Verwendung eines API-Clients, wie z. B. Postman.
{% endalert %}

Um Ihre Scuba-Daten auf Braze hochzuladen, stellen Sie eine POST-Anfrage an `https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation` unter Verwendung des Content-Typs `application/json`:

```bash
curl -X POST "https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation" \
-H "content-type: application/json" \
-d '{"braze_host":"BRAZE_API_ENDPOINT", \
"braze_api_key":"BRAZE_API_KEY", \
"scuba_host":"HOSTNAME", \
"scuba_token":"SCUBA_API_TOKEN", \
"scuba_table_name":"TABLE_NAME", \
"scuba_actor_property_name":"ACTOR_PROPERTY_NAME", \
"scuba_actor_property_value_filter":"ACTOR_PROPERTY_FILTER" \
"scuba_actor_id":"ACTOR_ID", \
"scuba_period_start":"PERIOD_START", \
"scuba_period_end":"PERIOD_END", \
"scuba_record_limit":"RECORD_LIMIT"}'
```

Ersetzen Sie Folgendes:

| Platzhalter             | Beschreibung                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | Die URL des Braze REST-Endpunkts Ihrer aktuellen Braze-Instanz. Weitere Informationen finden Sie unter [REST-API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys). |
| `BRAZE_API_KEY`         | Ihr Braze REST-API-Schlüssel mit der Berechtigung `users.track`.                                                                                                                                      |
| `HOSTNAME`              | Der Hostname Ihrer aktuellen Scuba-Instanz.                                                                                                                                                    |
| `SCUBA_API_TOKEN`       | Ihr Scuba API-Token.                                                                                                                                                                           |
| `TABLE_NAME`            | Die Tabelle, zu der Ihr Datensatz gehört. Weitere Informationen finden Sie unter [Glossar: Datensatz-Tabelle](https://docs.scuba.io/glossary/dataset-table).                                                                                                      |
| `ACTOR_PROPERTY_NAME`   | Die Eigenschaft des Akteurs, zu der Ihr Datensatz gehört. Nur Daten, die diesem Namen entsprechen, werden zurückgegeben. Weitere Informationen finden Sie unter [Glossar: Akteur-Eigenschaft](https://docs.scuba.io/glossary/actor-property).                                             |
| `ACTOR_PROPERTY_FILTER` | Der Zielgruppen-Suchfilter für die Eigenschaft Ihres Akteurs.                                                                                                                                             |
| `ACTOR_ID`              | Die ID der Akteur-Eigenschaft, zu der Ihr Datensatz gehört. Diese ID entspricht Ihrer `external_id` in Braze. Weitere Informationen finden Sie unter [Glossar: Akteur](https://docs.scuba.io/glossary/actor).                                              |
| `PERIOD_START`          | Der Startzeitraum als BQL-kompatibles Datum. Weitere Informationen finden Sie unter [BQL-Syntax und Verwendung](https://docs.scuba.io/guides/bql-syntax-and-usage).                                                                                                 |
| `PERIOD_END`            | Der Endzeitraum als BQL-kompatibles Datum. Weitere Informationen finden Sie unter [BQL-Syntax und Verwendung](https://docs.scuba.io/guides/bql-syntax-and-usage).                                                                                                   |
| `RECORD_LIMIT`          | **Optional**: Die maximale Anzahl von Datensätzen, die zurückgegeben werden sollen. Wenn Sie `scuba_record_limit` weglassen, gibt Scuba maximal 100 Datensätze zurück. Um dies zu ändern, weisen Sie `scuba_record_limit` eine beliebige nicht-negative Zahl zu.    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Hochladen Ihrer Scuba-Daten auf Braze" }

### Standardverhalten {#default-behavior}

Standardmäßig ist `update_existing_only` auf `false` eingestellt. Dadurch werden Ihre bestehenden Datensätze in Braze aktualisiert und neue Datensätze für noch nicht vorhandene Einträge erstellt. Um Scuba daran zu hindern, neue Datensätze zu erstellen, setzen Sie `update_existing_only` auf `true`.

### Rate-Limit

Scuba wendet ein Rate-Limit von 50.000 Anfragen pro Minute auf diesen Endpunkt an.

## Segmente mit den Verhaltensdaten von Scuba erstellen {#creating-segments-using-scubas-behavioral-data}

Nachdem Sie [Ihre Daten hochgeladen](#uploading-your-scuba-data-to-braze) haben, können Sie in Braze mit den Verhaltensdaten von Scuba Nutzer:innen-Segmente erstellen.

### 1. Schritt: Ein neues Segment erstellen {#step-1-create-a-new-segment}

Gehen Sie in Braze zu **Audience** > **Segments**, wählen Sie dann **Create Segment** und geben Sie einen Namen für Ihr Segment ein.

![Erstellen eines neuen Segments in Braze.]({% image_buster /assets/img/scuba/analytics/segment_name.png %})

### 2. Schritt: Scuba-Attribut suchen und auswählen {#step-2-find-and-select-the-scuba-attribute}

Wählen Sie unter **Segment Details** > **Filters** die Option **Custom Attributes**.

![Auswählen des Filters „Custom Attribute“ unter „Segment Details“.]({% image_buster /assets/img/scuba/analytics/filter_attribute.png %})

Wählen Sie **Search custom attributes** und wählen Sie dann den Namen der Akteur-Eigenschaft aus, die Sie in Ihrer vorherigen POST-Anfrage verwendet haben.

![Auswählen der Akteur-Eigenschaft als angepasstes Attribut.]({% image_buster /assets/img/scuba/analytics/select_property.png %})

### 3. Schritt: Attribut konfigurieren {#step-3-configure-the-attribute}

Wählen Sie neben dem Namen der Eigenschaft Ihres Akteurs einen Operator und einen Wert (falls zutreffend). Diese Werte werden von den Akteur-Eigenschaften bestimmt, die Sie in Scuba definiert haben. Wenn Sie fertig sind, wählen Sie **Save**.

![Auswählen eines Operators und eines Werts für das ausgewählte Attribut.]({% image_buster /assets/img/scuba/analytics/operator_end.png %})