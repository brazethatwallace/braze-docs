---
nav_title: "POST: Asset in die Medienbibliothek hochladen"
article_title: "POST: Asset in die Medienbibliothek hochladen"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel enthält detaillierte Informationen zum Endpunkt `POST /media_library/create`."
---

{% api %}
# Asset in die Medienbibliothek hochladen {#upload-an-asset-to-the-media-library}
{% apimethod post %}
/media_library/create
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein Asset zur [Braze-Medienbibliothek]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library) hinzuzufügen, entweder über eine extern gehostete URL (`asset_url`) oder über Binärdaten, die im Anfragetext (`asset_file`) gesendet werden. Dieser Endpunkt unterstützt Bilder und ZIP-Dateien, die Bilder enthalten.

{% alert tip %}
Sie können diesen Endpunkt auch über den [Braze-MCP-Server]({{site.baseurl}}/user_guide/brazeai/mcp_server) mit der Funktion [`create_media_library_asset`]({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions#media-library) aufrufen. So können KI-Tools wie Claude und Cursor Assets über natürlichsprachliche Eingaben in Ihre Medienbibliothek hochladen.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `media_library.create`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='media_library' %}

## Anfragetext {#request-body}

Wenn Sie `asset_url` angeben, lädt der Endpunkt die Datei von der URL herunter. Wenn Sie `asset_file` angeben, verwendet der Endpunkt die Binärdaten im Anfragetext.

Beispiel für einen Anfragetext mit `asset_url`:

```json
{
  "asset_url": "https://cdn.example.com/assets/cat.jpg",
  "name": "Cat Graphic"
}
```

Beispiel für einen Anfragetext mit `asset_file`:

```json
{
  "asset_file": <BINARY FILE DATA>,
  "name": "Cat Graphic"
}
```

Der Anfragetext enthält die folgenden Parameter:

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | -------- | --------- | ----------- |
| `asset_url` | Optional | String | Eine öffentlich zugängliche URL für das Asset, das in Braze hochgeladen werden soll. |
| `asset_file` | Optional | Binär | Binärdatei-Daten. |
| `name` | Optional | String | Ein Name, der in der Medienbibliothek für dieses Asset angezeigt werden soll. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfragetext" }

{% alert important %}
`asset_url` und `asset_file` schließen sich gegenseitig aus. Sie dürfen nur eines davon in Ihre API-Anfrage aufnehmen.
{% endalert %}

### Namen der hochgeladenen Dateien {#uploaded-file-names}

In diesem Abschnitt wird erläutert, wie der Endpunkt hochgeladenen Dateien Namen zuweist, je nachdem, ob Sie den Parameter `name` angeben.

#### Einzelne Datei-Uploads {#single-file-uploads}

| Szenario | Ergebnis |
| --- | --- |
| `name` angegeben | Der `name`-Wert wird als Asset-Name in der Medienbibliothek verwendet. |
| `name` nicht angegeben | Der ursprüngliche Dateiname aus der URL oder der hochgeladenen Datei wird verwendet. |
{: .reset-td-br-1 .reset-td-br-2 style="table-layout: fixed; width: 100%;" aria-label="Einzelne Datei-Uploads" }

#### ZIP-Datei-Uploads {#zip-file-uploads}

| Szenario | Ergebnis |
| --- | --- |
| `name` angegeben | Der `name`-Wert wird als Präfix verwendet, wobei eine aufsteigende Zahl als Suffix angehängt wird (z. B. „Meine Datei 1“, „Meine Datei 2“, „Meine Datei 3“). |
| `name` nicht angegeben | Jede Datei behält ihren ursprünglichen Dateinamen aus der ZIP-Datei bei. |
{: .reset-td-br-1 .reset-td-br-2 style="table-layout: fixed; width: 100%;" aria-label="ZIP-Datei-Uploads" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält zwei `curl`-Beispielanfragen: eine zum Hinzufügen eines Assets über eine URL und eine weitere über Binärdaten.

Diese Anfrage zeigt ein Beispiel für das Hinzufügen eines Assets zur Medienbibliothek mithilfe einer `asset_url`.

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_url": "https://cdn.example.com/assets/cat.jpg", "name": "Cat Graphic"}'
```

Diese Anfrage zeigt ein Beispiel für das Hinzufügen eines Assets zur Medienbibliothek mithilfe einer `asset_file`.

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_file":<BINARY FILE DATA>, "name":"Cat Graphic"}'
```

### Fehlerantworten {#error-responses}

In diesem Abschnitt werden mögliche Fehler sowie die entsprechenden Nachrichten und Beschreibungen aufgeführt.

#### Validierungsfehler {#validation-errors}

Validierungsfehler geben eine Struktur wie die folgende zurück:

```json
{
  "message": (String) Human-readable error description
}
```

Diese Tabelle listet mögliche Validierungsfehler auf.

| HTTP-Status | Nachricht | Beschreibung |
| --- | --- | --- |
| 400 | "Either asset_url or asset_file must be provided." | In der Anfrage wurde kein Asset-Parameter angegeben. |
| 400 | "Both asset_url and asset_file cannot be provided. Please provide only one." | Beide Asset-Parameter wurden angegeben; es ist jedoch nur einer zulässig. |
| 403 | "Media Library Public APIs are not enabled for this company." | Das Feature der Medienbibliothek ist für diesen Workspace nicht aktiviert. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Validierungsfehler" }

#### Verarbeitungsfehler {#processing-errors}

Verarbeitungsfehler geben eine andere Antwort mit Fehlercodes zurück:

```json
{
  "message": (String) Human-readable error description,
  "error_code": (String) error code,
  "meta": { }
}
```

Diese Tabelle listet mögliche Verarbeitungsfehler auf.

| Fehlercode | HTTP-Status | Beschreibung |
| --- | --- | --- |
| `UNSUPPORTED_FILE_TYPE` | 400 | Der hochgeladene Dateityp wird nicht unterstützt. Das `meta`-Objekt enthält den abgelehnten `file_type`. |
| `ASSET_SIZE_EXCEEDS_LIMIT` | 400 | Die Datei überschreitet die maximal zulässige Größe. Bilder dürfen maximal 5 MB groß sein. |
| `MEDIA_LIBRARY_LIMIT_REACHED` | 400 | Der Workspace hat die maximale Anzahl an Assets erreicht (Standard: 200 für Unternehmen mit kostenloser Demo, ansonsten unbegrenzt). Das `meta`-Objekt enthält das aktuelle `limit`. |
| `ASSET_UPLOAD_FAILED` | 400 | Das Asset konnte aufgrund von Verarbeitungsproblemen nicht hochgeladen werden. |
| `INVALID_ASSET_URL` | 400 | Der `asset_url`-Wert ist kein gültiger URI. Das `meta`-Objekt enthält `asset_url`. |
| `ZIP_UPLOAD_ERROR` | 400 | Die ZIP-Datei ist beschädigt oder konnte nicht geöffnet werden. Das `meta`-Objekt enthält die `original_error`-Nachricht. |
| `ZIP_FILE_TOO_LARGE` | 400 | Die unkomprimierte Gesamtgröße der ZIP-Datei überschreitet das Limit von 5 MB. Das `meta`-Objekt enthält `zip_file_name` und `zip_file_size`. |
| `ZIPPED_ENTITY_HAS_NO_NAME` | 400 | Ein Dateieintrag innerhalb der ZIP-Datei hat keinen Namen. Stellen Sie sicher, dass die ZIP-Datei nicht beschädigt ist, und benennen Sie alle unbenannten Dateieinträge. |
| `ZIPPED_ENTITY_CANNOT_HAVE_NESTED_DIRECTORY` | 400 | Die ZIP-Datei enthält verschachtelte Verzeichnisse, die nicht unterstützt werden. Alle Dateien müssen sich im Stammverzeichnis der ZIP-Datei befinden. |
| `GENERIC_ERROR` | 500 | Beim Hochladen ist ein unerwarteter Fehler aufgetreten. Das `meta`-Objekt enthält die `original_error`-Nachricht zur Fehlerbehebung. Versuchen Sie es erneut oder wenden Sie sich an den [Support]({{site.baseurl}}/support_contact). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Verarbeitungsfehler" }


## Antwort {#response}

Für diesen Endpunkt gibt es fünf Statuscode-Antworten: `200`, `400`, `403`, `429` und `500`.

Das folgende JSON zeigt die erwartete Struktur der Antwort.

```json
{
    "new_assets": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "url": (String) the URL to access the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif")
        }
    ],
    "errors": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif"),
            "error": (String) the error that occurred
        }
    ],
    "dashboard_url": (String) the URL to view this asset in the Braze dashboard
}
```

{% endapi %}