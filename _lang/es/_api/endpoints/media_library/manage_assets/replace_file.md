---
nav_title: "PUT: Reemplazar un activo en la biblioteca de medios"
article_title: "PUT: Reemplazar un activo en la biblioteca de medios"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Este artículo describe los detalles del punto de conexión `PUT /media_library/replace_file`."
---

{% api %}
# Reemplazar un activo en la biblioteca de medios {#replace-an-asset-in-the-media-library}
{% apimethod put %}
/media_library/replace_file
{% endapimethod %}

> Utiliza este punto de conexión para reemplazar el archivo de un activo existente en la [Biblioteca de medios de Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library) conservando su ID de activo y su URL. Puedes proporcionar el archivo de reemplazo mediante una URL alojada externamente (`asset_url`) o datos de archivo binario enviados en el cuerpo de la solicitud (`asset_file`).

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key) con el permiso `media_library.replace`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='media_library' %}

## Cuerpo de la solicitud {#request-body}

Cuando incluyes `asset_url`, el punto de conexión descarga el archivo desde la URL. Cuando incluyes `asset_file`, el punto de conexión utiliza los datos binarios del cuerpo de la solicitud.

Ejemplo de cuerpo de solicitud para `asset_url`:

```json
{
  "asset_id": "your-asset-id",
  "asset_url": "https://cdn.example.com/assets/cat.jpg"
}
```

Ejemplo de cuerpo de solicitud para `asset_file`:

```json
{
  "asset_id": "your-asset-id",
  "asset_file": <BINARY FILE DATA>
}
```

El cuerpo de la solicitud incluye los siguientes parámetros:

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `asset_id` | Obligatorio | Cadena | El ID del activo que se va a reemplazar. |
| `asset_url` | Opcional | Cadena | Una URL de acceso público para el archivo de reemplazo. |
| `asset_file` | Opcional | Binario | Datos de archivo binario para el archivo de reemplazo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Cuerpo de la solicitud" }

{% alert important %}
`asset_url` y `asset_file` son mutuamente excluyentes; solo debes incluir uno de ellos en tu solicitud de API.
{% endalert %}

### Requisitos del archivo de reemplazo {#replacement-file-requirements}

- La extensión del archivo de reemplazo debe coincidir exactamente con la extensión del activo existente. Por ejemplo, no puedes reemplazar un activo `.png` con un archivo `.jpg`.
- El reemplazo de archivos es compatible con imágenes, SVG, documentos, fuentes, tarjetas de contacto y archivos de código. Los activos de video no se pueden reemplazar.

## Ejemplo de solicitud {#example-request}

Esta sección incluye dos ejemplos de solicitudes `curl`, una para reemplazar un activo mediante una URL y otra mediante datos de archivo binario.

Esta solicitud muestra un ejemplo de reemplazo de un activo en la Biblioteca de medios mediante un `asset_url`.

```
curl -X PUT --location 'https://rest.iad-01.braze.com/media_library/replace_file' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_id": "your-asset-id", "asset_url": "https://cdn.example.com/assets/cat.jpg"}'
```

Esta solicitud muestra un ejemplo de reemplazo de un activo en la Biblioteca de medios mediante un `asset_file`.

```
curl -X PUT --location 'https://rest.iad-01.braze.com/media_library/replace_file' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_id": "your-asset-id", "asset_file":<BINARY FILE DATA>}'
```

### Respuestas de error {#error-responses}

Esta sección enumera los posibles errores con sus mensajes y descripciones correspondientes.

#### Errores de validación {#validation-errors}

Los errores de validación devuelven una estructura como esta:

```json
{
  "message": (String) Human-readable error description
}
```

Esta tabla enumera los posibles errores de validación.

| Estado HTTP | Mensaje | Descripción |
| --- | --- | --- |
| 400 | "asset_id is required." | No se proporcionó un ID de activo en la solicitud. |
| 400 | "Either file or asset_url is required." | No se proporcionó ni `asset_file` ni `asset_url`; se requiere uno de los dos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de validación" }

#### Errores de procesamiento {#processing-errors}

Los errores de procesamiento devuelven una respuesta diferente con códigos de error:

```json
{
  "message": (String) Human-readable error description,
  "error_code": (String) error code,
  "meta": { }
}
```

Esta tabla enumera los posibles errores de procesamiento.

| Código de error | Estado HTTP | Descripción |
| --- | --- | --- |
| `ASSET_NOT_FOUND` | 404 | No existe ningún activo con el `asset_id` proporcionado en este espacio de trabajo. El objeto `meta` incluye `asset_id`. |
| `INVALID_ASSET_URL` | 400 | El valor de `asset_url` no es un URI válido. El objeto `meta` incluye `asset_url`. |
| `EXTENSION_MISMATCH` | 400 | La extensión del archivo de reemplazo no coincide con la extensión del activo existente. El objeto `meta` incluye `expected_extension` y `received_extension`. |
| `UNSUPPORTED_ASSET_TYPE_FOR_REPLACE` | 400 | El reemplazo de archivos no es compatible con este tipo de activo (por ejemplo, video). El objeto `meta` incluye `asset_type`. |
| `ASSET_SIZE_EXCEEDS_LIMIT` | 400 | El archivo supera el tamaño máximo permitido. El objeto `meta` incluye `size_limit_bytes` y `file_size_bytes`. |
| `CORRUPT_FILE` | 400 | El archivo de imagen está dañado o no se puede leer. El objeto `meta` incluye `file_name`. |
| `GENERIC_ERROR` | 500 | Se produjo un error inesperado durante el reemplazo del archivo. El objeto `meta` incluye `original_error` para depuración. Inténtalo de nuevo o [ponte en contacto con Soporte]({{site.baseurl}}/support_contact). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de procesamiento" }

## Respuesta {#response}

Hay cinco respuestas de código de estado para este punto de conexión: `200`, `400`, `404`, `429` y `500`.

El siguiente JSON muestra la estructura esperada de la respuesta.

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