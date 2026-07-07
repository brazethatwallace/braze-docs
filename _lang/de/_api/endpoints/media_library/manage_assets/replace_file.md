---
nav_title: "PUT: Asset in der Medienbibliothek ersetzen"
article_title: "PUT: Asset in der Medienbibliothek ersetzen"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt `PUT /media_library/replace_file`."
---

{% api %}
# Asset in der Medienbibliothek ersetzen {#replace-an-asset-in-the-media-library}
{% apimethod put %}
/media_library/replace_file
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die Datei eines vorhandenen Assets in der [Braze-Medienbibliothek]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library) zu ersetzen und dabei die Asset-ID und URL beizubehalten. Sie können die Ersatzdatei entweder über eine extern gehostete URL (`asset_url`) oder als binäre Dateidaten im Anfragekörper (`asset_file`) bereitstellen.

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key) mit der Berechtigung `media_library.replace`.

## Rate-Limits {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='media_library' %}

## Anfragekörper {#request-body}

Wenn Sie `asset_url` angeben, lädt der Endpunkt die Datei von der URL herunter. Wenn Sie `asset_file` angeben, verwendet der Endpunkt die binären Daten im Anfragekörper.

Beispiel-Anfragekörper für `asset_url`:

```json
{
  "asset_id": "your-asset-id",
  "asset_url": "https://cdn.example.com/assets/cat.jpg"
}
```

Beispiel-Anfragekörper für `asset_file`:

```json
{
  "asset_id": "your-asset-id",
  "asset_file": <BINARY FILE DATA>
}
```

Der Anfragekörper enthält die folgenden Parameter:

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | -------- | --------- | ----------- |
| `asset_id` | Erforderlich | String | Die ID des zu ersetzenden Assets. |
| `asset_url` | Optional | String | Eine öffentlich zugängliche URL für die Ersatzdatei. |
| `asset_file` | Optional | Binär | Binäre Dateidaten für die Ersatzdatei. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfragekörper" }

{% alert important %}
`asset_url` und `asset_file` schließen sich gegenseitig aus. Sie dürfen nur einen der beiden Parameter in Ihrer API-Anfrage angeben.
{% endalert %}

### Anforderungen an die Ersatzdatei {#replacement-file-requirements}

- Die Dateierweiterung der Ersatzdatei muss exakt mit der Erweiterung des vorhandenen Assets übereinstimmen. Beispielsweise können Sie ein `.png`-Asset nicht durch eine `.jpg`-Datei ersetzen.
- Der Dateiaustausch wird für Bilder, SVGs, Dokumente, Schriftarten, Kontaktkarten und Code-Dateien unterstützt. Video-Assets können nicht ersetzt werden.

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält zwei Beispiel-`curl`-Anfragen: eine zum Ersetzen eines Assets über eine URL und eine weitere mit binären Dateidaten.

Diese Anfrage zeigt ein Beispiel für das Ersetzen eines Assets in der Medienbibliothek unter Verwendung einer `asset_url`.

```
curl -X PUT --location 'https://rest.iad-01.braze.com/media_library/replace_file' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_id": "your-asset-id", "asset_url": "https://cdn.example.com/assets/cat.jpg"}'
```

Diese Anfrage zeigt ein Beispiel für das Ersetzen eines Assets in der Medienbibliothek unter Verwendung einer `asset_file`.

```
curl -X PUT --location 'https://rest.iad-01.braze.com/media_library/replace_file' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_id": "your-asset-id", "asset_file":<BINARY FILE DATA>}'
```

### Fehlerantworten {#error-responses}

Dieser Abschnitt listet mögliche Fehler mit den zugehörigen Meldungen und Beschreibungen auf.

#### Validierungsfehler {#validation-errors}

Validierungsfehler geben eine Struktur wie diese zurück:

```json
{
  "message": (String) Human-readable error description
}
```

Diese Tabelle listet mögliche Validierungsfehler auf.

| HTTP-Status | Meldung | Beschreibung |
| --- | --- | --- |
| 400 | "asset_id is required." | In der Anfrage wurde keine Asset-ID angegeben. |
| 400 | "Either file or asset_url is required." | Weder `asset_file` noch `asset_url` wurde angegeben; einer der beiden ist erforderlich. |
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
| `ASSET_NOT_FOUND` | 404 | In diesem Workspace existiert kein Asset mit der angegebenen `asset_id`. Das `meta`-Objekt enthält `asset_id`. |
| `INVALID_ASSET_URL` | 400 | Der Wert von `asset_url` ist kein gültiger URI. Das `meta`-Objekt enthält `asset_url`. |
| `EXTENSION_MISMATCH` | 400 | Die Dateierweiterung der Ersatzdatei stimmt nicht mit der Erweiterung des vorhandenen Assets überein. Das `meta`-Objekt enthält `expected_extension` und `received_extension`. |
| `UNSUPPORTED_ASSET_TYPE_FOR_REPLACE` | 400 | Der Dateiaustausch wird für diesen Asset-Typ nicht unterstützt (z. B. Video). Das `meta`-Objekt enthält `asset_type`. |
| `ASSET_SIZE_EXCEEDS_LIMIT` | 400 | Die Datei überschreitet die maximal zulässige Größe. Das `meta`-Objekt enthält `size_limit_bytes` und `file_size_bytes`. |
| `CORRUPT_FILE` | 400 | Die Bilddatei ist beschädigt oder nicht lesbar. Das `meta`-Objekt enthält `file_name`. |
| `GENERIC_ERROR` | 500 | Beim Dateiaustausch ist ein unerwarteter Fehler aufgetreten. Das `meta`-Objekt enthält `original_error` zur Fehlersuche. Versuchen Sie es erneut oder kontaktieren Sie den [Support]({{site.baseurl}}/support_contact). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Verarbeitungsfehler" }

## Antwort {#response}

Für diesen Endpunkt gibt es fünf Statuscode-Antworten: `200`, `400`, `404`, `429` und `500`.

Das folgende JSON zeigt die erwartete Struktur der Antwort.

```json
{
  "info": "Asset file updated successfully.",
  "new_image_asset": {
    "name": (String) the name of the asset,
    "size": (Integer) the byte size of the asset,
    "url": (String) the URL to access the asset,
    "ext": (String) the file extension (e.g., "png", "jpg", "gif")
  }
}
```

{% endapi %}