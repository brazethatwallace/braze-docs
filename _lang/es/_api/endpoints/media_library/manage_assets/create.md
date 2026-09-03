---
nav_title: "POST: Cargar un activo en la biblioteca de medios"
article_title: "POST: Cargar un activo en la biblioteca de medios"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el endpoint `POST /media_library/create`."
---

{% api %}
# Cargar un activo en la biblioteca de medios {#upload-an-asset-to-the-media-library}
{% apimethod post %}
/media_library/create
{% endapimethod %}

> Utiliza este endpoint para añadir un activo a la [biblioteca de medios de Braze]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) utilizando una URL alojada externamente (`asset_url`) o datos de archivo binario enviados en el cuerpo de la solicitud (`asset_file`). Este endpoint admite imágenes, documentos y archivos ZIP que los contengan. Para ver la lista completa, consulta [Tipos de archivo compatibles](#supported-file-types).

## Tipos de archivo compatibles {#supported-file-types}

Este endpoint admite los siguientes tipos de archivo, tanto si los cargas a través de `asset_url` como de `asset_file`.

| Tipo de activo | Tipos de archivo compatibles | Tamaño máximo |
| --- | --- | --- |
| Imagen | GIF, ICO, JPEG, JPG, PNG, WebP | 5&nbsp;MB |
| Imagen vectorial | SVG | 5&nbsp;MB |
| Documento | DOC, DOCX, PDF, PPT, PPTX, XLS, XLSX | 5&nbsp;MB |
| Archivo comprimido | ZIP | 50&nbsp;MB en total, 5&nbsp;MB por archivo dentro del ZIP |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 style="table-layout: fixed; width: 100%;" aria-label="Tipos de archivo compatibles" }

Si cargas un tipo de archivo que no aparece aquí, el endpoint devuelve un error `UNSUPPORTED_FILE_TYPE`.

Para archivos ZIP, cada archivo dentro del archivo comprimido también debe ser uno de los tipos de archivo compatibles enumerados aquí, y todos los archivos deben estar en la raíz del archivo ZIP (sin subdirectorios). Cualquier archivo no compatible se omite y se devuelve en el array `errors` de la respuesta, y el resto del archivo comprimido se carga igualmente.

{% alert note %}
Los archivos de contacto virtual (.vcf) y los archivos de video se pueden cargar en la biblioteca de medios, pero solo a través de la interfaz del panel (**Contenido** > **Biblioteca de medios**), no a través de este endpoint de API.
{% endalert %}

{% alert tip %}
También puedes llamar a este endpoint a través del [servidor MCP de Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server) utilizando la función [`create_media_library_asset`]({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions#media-library). Esto permite que herramientas de IA como Claude y Cursor carguen activos en tu biblioteca de medios mediante indicaciones en lenguaje natural.
{% endalert %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `media_library.create`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='media_library' %}

## Cuerpo de la solicitud {#request-body}

Cuando incluyes `asset_url`, el endpoint descarga el archivo desde la URL. Cuando incluyes `asset_file`, el endpoint utiliza los datos binarios del cuerpo de la solicitud.

Ejemplo de cuerpo de solicitud para `asset_url`:

```json
{
  "asset_url": "https://cdn.example.com/assets/cat.jpg",
  "name": "Cat Graphic"
}
```

Ejemplo de cuerpo de solicitud para `asset_file`:

```json
{
  "asset_file": <BINARY FILE DATA>,
  "name": "Cat Graphic"
}
```

El cuerpo de la solicitud incluye los siguientes parámetros:

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `asset_url` | Opcional | Cadena | Una URL de acceso público para el activo que se va a cargar en Braze. |
| `asset_file` | Opcional | Binario | Datos de archivo binario. |
| `name` | Opcional | Cadena | Nombre que aparecerá en la biblioteca de medios para este activo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Cuerpo de la solicitud" }

{% alert important %}
`asset_url` y `asset_file` son mutuamente excluyentes; solo debes incluir uno de ellos en tu solicitud de API.
{% endalert %}

### Nombres de los archivos cargados {#uploaded-file-names}

En esta sección se explica cómo el endpoint asigna nombres a los archivos cargados en función de si incluyes el parámetro `name`.

#### Cargas de archivos individuales {#single-file-uploads}

| Escenario | Resultado |
| --- | --- |
| `name` proporcionado | El valor de `name` se utiliza como nombre del activo en la biblioteca de medios. |
| `name` excluido | Se utiliza el nombre de archivo original de la URL o del archivo cargado. |
{: .reset-td-br-1 .reset-td-br-2 style="table-layout: fixed; width: 100%;" aria-label="Cargas de archivos individuales" }

#### Cargas de archivos ZIP {#zip-file-uploads}

| Escenario | Resultado |
| --- | --- |
| `name` proporcionado | El valor de `name` se utiliza como prefijo, con un número incremental añadido como sufijo (por ejemplo, "Mi archivo 1", "Mi archivo 2", "Mi archivo 3"). |
| `name` excluido | Cada archivo conserva su nombre original dentro del archivo ZIP. |
{: .reset-td-br-1 .reset-td-br-2 style="table-layout: fixed; width: 100%;" aria-label="Cargas de archivos ZIP" }

## Ejemplo de solicitud {#example-request}

Esta sección incluye dos ejemplos de solicitudes `curl`, una para añadir un activo utilizando una URL y otra utilizando datos de archivo binario.

Esta solicitud muestra un ejemplo de cómo añadir un activo a la biblioteca de medios utilizando un `asset_url`.

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_url": "https://cdn.example.com/assets/cat.jpg", "name": "Cat Graphic"}'
```

Esta solicitud muestra un ejemplo de cómo añadir un activo a la biblioteca de medios utilizando un `asset_file`.

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_file":<BINARY FILE DATA>, "name":"Cat Graphic"}'
```

### Respuestas de error {#error-responses}

En esta sección se enumeran los posibles errores y sus correspondientes mensajes y descripciones.

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
| 400 | "Either asset_url or asset_file must be provided." | No se proporcionó ningún parámetro de activo en la solicitud. |
| 400 | "Both asset_url and asset_file cannot be provided. Please provide only one." | Se proporcionaron ambos parámetros de activo; solo se permite uno. |
| 403 | "Media Library Public APIs are not enabled for this company." | La característica de biblioteca de medios no está habilitada para este espacio de trabajo. |
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
| `UNSUPPORTED_FILE_TYPE` | 400 | El tipo de archivo cargado no es compatible. Consulta [Tipos de archivo compatibles](#supported-file-types). El objeto `meta` incluye el `file_type` que fue rechazado. |
| `ASSET_SIZE_EXCEEDS_LIMIT` | 400 | El archivo supera el tamaño máximo permitido de 5&nbsp;MB. |
| `MEDIA_LIBRARY_LIMIT_REACHED` | 400 | El espacio de trabajo ha alcanzado su número máximo de activos (200 de forma predeterminada para las empresas con versión de prueba gratuita, ilimitado en los demás casos). El objeto `meta` incluye el `limit` actual. |
| `ASSET_UPLOAD_FAILED` | 400 | El activo no se pudo cargar debido a problemas de procesamiento. |
| `INVALID_ASSET_URL` | 400 | El valor de `asset_url` no es un URI válido. El objeto `meta` incluye `asset_url`. |
| `ZIP_UPLOAD_ERROR` | 400 | El archivo ZIP está dañado o no se puede abrir. El objeto `meta` incluye el mensaje `original_error`. |
| `ZIP_FILE_TOO_LARGE` | 400 | El tamaño total sin comprimir del archivo ZIP supera el límite de 50&nbsp;MB. El objeto `meta` incluye el `zip_file_name` y el `zip_file_size`. |
| `ZIPPED_ENTITY_HAS_NO_NAME` | 400 | Una entrada de archivo dentro del ZIP no tiene nombre. Asegúrate de que el archivo ZIP no esté dañado y añade un nombre a cualquier entrada de archivo sin nombre. |
| `ZIPPED_ENTITY_CANNOT_HAVE_NESTED_DIRECTORY` | 400 | El archivo ZIP contiene directorios anidados, que no son compatibles. Todos los archivos deben estar en el nivel raíz del ZIP. |
| `GENERIC_ERROR` | 500 | Se produjo un error inesperado durante la carga. El objeto `meta` incluye el mensaje `original_error` para la depuración. Vuelve a intentarlo o ponte en contacto con [Soporte]({{site.baseurl}}/support_contact). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de procesamiento" }


## Respuesta {#response}

Hay cinco respuestas de código de estado para este endpoint: `200`, `400`, `403`, `429` y `500`.

El siguiente JSON muestra el formato esperado de la respuesta.

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