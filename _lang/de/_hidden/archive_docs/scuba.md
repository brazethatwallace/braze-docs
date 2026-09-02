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

| Voraussetzung | Beschreibung |
|---|---|
| Scuba-API-Token / Textbaustein | Ein Scuba-API-Token / Textbaustein, das Sie vom Endpunkt `https://{scuba_hostname}/api/create_token` abrufen können. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-REST-Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz](https://scuba.io) ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Hochladen Ihrer Scuba-Daten in Braze {#uploading-your-scuba-data-to-braze}

{% alert important %}
Die folgende Anfrage verwendet curl. Für ein besseres API-Anfragemanagement empfehlen wir die Verwendung eines API-Clients wie Postman.
{% endalert %}

Um Ihre Scuba-Daten in Braze hochzuladen, senden Sie eine POST-Anfrage an `https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation` mit dem Content-Typ `application/json`:

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

Ersetzen Sie die folgenden Werte:

| Platzhalter             | Beschreibung                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | Die Braze-REST-Endpunkt-URL Ihrer aktuellen Braze-Instanz. Weitere Informationen finden Sie unter [REST-API-Schlüssel]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). |
| `BRAZE_API_KEY`         | Ihr Braze-REST-API-Schlüssel mit der Berechtigung `users.track`.                                                                                                                                      |
| `HOSTNAME`              | Der Hostname Ihrer aktuellen Scuba-Instanz.                                                                                                                                                    |
| `SCUBA_API_TOKEN`       | Ihr Scuba-API-Token / Textbaustein.                                                                                                                                                                           |
| `TABLE_NAME`            | Die Tabelle, zu der Ihr Datensatz gehört. Weitere Informationen finden Sie unter [Glossary: Dataset table](https://docs.scuba.io/glossary/dataset-table).                                                                                                      |
| `ACTOR_PROPERTY_NAME`   | Die Actor-Eigenschaft, zu der Ihr Datensatz gehört. Es werden nur Daten zurückgegeben, die mit diesem Namen übereinstimmen. Weitere Informationen finden Sie unter [Glossary: Actor property](https://docs.scuba.io/glossary/actor-property).                                             |
| `ACTOR_PROPERTY_FILTER` | Der Zielgruppen-Suchfilter für Ihre Actor-Eigenschaft.                                                                                                                                             |
| `ACTOR_ID`              | Die ID der Actor-Eigenschaft, zu der Ihr Datensatz gehört. Diese ID stimmt mit Ihrer `external_id` in Braze überein. Weitere Informationen finden Sie unter [Glossary: Actor](https://docs.scuba.io/glossary/actor).                                              |
| `PERIOD_START`          | Das Startdatum als BQL-kompatibles Datum. Weitere Informationen finden Sie unter [BQL syntax and usage](https://docs.scuba.io/guides/bql-syntax-and-usage).                                                                                                 |
| `PERIOD_END`            | Das Enddatum als BQL-kompatibles Datum. Weitere Informationen finden Sie unter [BQL syntax and usage](https://docs.scuba.io/guides/bql-syntax-and-usage).                                                                                                   |
| `RECORD_LIMIT`          | **Optional**: Die maximale Anzahl der zurückzugebenden Datensätze. Wenn `scuba_record_limit` weggelassen wird, gibt Scuba maximal 100 Datensätze zurück. Um dies zu ändern, weisen Sie `scuba_record_limit` eine beliebige nicht-negative Zahl zu.    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Hochladen Ihrer Scuba-Daten in Braze" }

### Standardverhalten {#default-behavior}

Standardmäßig ist `update_existing_only` auf `false` gesetzt, wodurch Ihre bestehenden Datensätze in Braze aktualisiert und neue Datensätze für nicht vorhandene Einträge erstellt werden. Um zu verhindern, dass Scuba neue Datensätze erstellt, setzen Sie `update_existing_only` auf `true`.

### Rate-Limits {#rate-limit}

Scuba wendet auf diesen Endpunkt ein Rate-Limit von 50.000 Anfragen pro Minute an.

## Segments mit Scubas Verhaltensdaten erstellen {#creating-segments-using-scubas-behavioral-data}

Nachdem Sie [Ihre Daten hochgeladen haben](#uploading-your-scuba-data-to-braze), können Sie in Braze Nutzer:innen-Segments mit Scubas Verhaltensdaten erstellen.

### Schritt 1: Neues Segment erstellen {#step-1-create-a-new-segment}

Gehen Sie in Braze zu **Zielgruppe** > **Segments** und wählen Sie **Segment erstellen** aus. Geben Sie dann einen Namen für Ihr Segment ein.

![Erstellen eines neuen Segments in Braze.]({% image_buster /assets/img/scuba/analytics/segment_name.png %})

### Schritt 2: Scuba-Attribut suchen und auswählen {#step-2-find-and-select-the-scuba-attribute}

Wählen Sie unter **Segmentdetails** > **Filter** die Option **Angepasste Attribute** aus.

![Auswahl des Filters „Angepasstes Attribut“ unter „Segmentdetails“.]({% image_buster /assets/img/scuba/analytics/filter_attribute.png %})

Wählen Sie **Angepasste Attribute durchsuchen** und dann den Actor-Property-Namen aus, den Sie in Ihrer vorherigen POST-Anfrage verwendet haben.

![Auswahl der Actor-Eigenschaft als angepasstes Attribut.]({% image_buster /assets/img/scuba/analytics/select_property.png %})

### Schritt 3: Attribut konfigurieren {#step-3-configure-the-attribute}

Wählen Sie neben Ihrem Actor-Property-Namen einen Operator und einen Wert (falls zutreffend). Diese Werte werden durch die Actor-Eigenschaften bestimmt, die Sie in Scuba definiert haben. Wenn Sie fertig sind, wählen Sie **Speichern**.

![Auswahl eines Operators und eines Werts für das ausgewählte Attribut.]({% image_buster /assets/img/scuba/analytics/operator_end.png %})