---
nav_title: Stayfilm
article_title: Stayfilm
description: "Aprende a integrar la renderización de video personalizado de Stayfilm con Braze utilizando Campaigns de webhook, contenido conectado y transformación de datos."
alias: /partners/stayfilm/
page_type: partner
search_tag: Partner
---

# Stayfilm

> [Stayfilm](https://www.stayfilm.com/) es una REST API para la producción automatizada y personalizada de video a escala. La plataforma integra datos, imágenes, texto, bandas sonoras, narración y efectos visuales para generar contenido de video personalizado para eCommerce, marketplaces, flujos de trabajo de CRM y campañas de marketing.
>
> Esta integración envía trabajos de renderización desde Braze a la API de Stayfilm, recibe devoluciones de llamada cuando los videos están listos y almacena las URL de los videos y el estado en los perfiles de usuario para su uso en Campaigns y Canvas.

_Esta integración es mantenida por Stayfilm._

## Ejemplos {#use-cases}

Stayfilm admite la entrega de videos personalizados a lo largo del ciclo de vida del cliente, incluyendo:

- **Incorporación y recorridos de bienvenida:** Da la bienvenida a nuevos usuarios con videos personalizados según su perfil o contexto de registro
- **Contenido de productos y marketplace:** Genera videos centrados en productos a partir de catálogos o contenido multimedia proporcionado por el usuario
- **Conversión y activación:** Refuerza acciones clave con mensajería de video contextual
- **Fidelización y upsell:** Destaca ofertas personalizadas o hitos de uso en formato de video
- **Recuperación y prevención de cancelación:** Vuelve a captar usuarios inactivos con contenido de video personalizado

## Requisitos previos {#prerequisites}

Antes de comenzar, confirma que tienes lo siguiente:

| Requisito | Descripción |
| ----------- | ----------- |
| Acceso a la API de Stayfilm | Ponte en contacto con Stayfilm para obtener las credenciales de tu proyecto, incluyendo `idproject`, `Subscription-Key`, credenciales de cliente OAuth y la URL base de la API de Stayfilm. Para detalles sobre autenticación y endpoints, consulta la [documentación de la API de Stayfilm](https://apidoc.stayfilm.com). |
| Braze Data Transformation | Utiliza [Braze Data Transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation) para recibir devoluciones de llamada de Stayfilm y mapearlas a perfiles de usuario de Braze a través del [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). |
| Identificador de usuario de Braze | Este tutorial utiliza `external_id` para correlacionar los trabajos de Stayfilm con los perfiles de usuario de Braze. El valor que pases en `CallbackRelayData` debe coincidir con el `external_id` del usuario en Braze. |
| Sandbox de Braze (recomendado) | Prueba la integración en un espacio de trabajo sandbox de Braze antes de desplegar en producción. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Cómo funciona la integración {#how-the-integration-works}

Esta integración utiliza un flujo de webhook bidireccional:

1. **Salida:** Una [Campaign de webhook]({{site.baseurl}}/user_guide/channels/webhooks) de Braze envía un trabajo de renderizado al endpoint `POST /Job` de Stayfilm. La solicitud incluye los medios del usuario, la configuración de la plantilla y `CallbackRelayData` establecido con el `external_id` del usuario de Braze.
2. **Entrada:** Cuando Stayfilm termina el renderizado, envía una devolución de llamada a la URL de tu webhook de transformación de datos de Braze. La transformación mapea la respuesta a [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) y eventos personalizados en el perfil de usuario correspondiente.
3. **Entrega:** Usa el atributo almacenado `stayfilm_video_url` en canales de mensajería, como un [mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages) con HTML personalizado.

La transformación de datos en este tutorial escribe los siguientes atributos personalizados:

| Atributo | Descripción |
| --------- | ----------- |
| `stayfilm_video_status` | `ready` cuando el renderizado se completa correctamente, o `failed` cuando Stayfilm reporta un error |
| `stayfilm_video_url` | URL del video MP4 renderizado |
| `stayfilm_job_id` | Identificador del trabajo de Stayfilm |
| `stayfilm_render_error` | Mensaje de error cuando el renderizado falla |
| `stayfilm_callback_received_at` | Marca de tiempo ISO de la devolución de llamada |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos personalizados" }

La transformación también registra eventos personalizados llamados `stayfilm_video_ready` o `stayfilm_video_failed`.

## Integración {#integration}

Los siguientes pasos te guían a través de una prueba de concepto. Después de validar el flujo, adapta la carga útil del trabajo, los atributos y la mensajería a tu caso de uso.

### Paso 1: Crear un usuario de prueba {#step-1-create-a-test-user}

Crea un perfil de usuario de prueba para usar mientras construyes y validas la integración. Para más información, consulta [Importar usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/import_users).

1. Ve a **Audiencia** > **Importar usuarios**.
2. Selecciona **Adición rápida de usuario**.
3. Introduce un `external_id` y cualquier otro campo obligatorio, luego selecciona **Crear nuevo usuario**.

{% alert important %}
No utilices datos personales, como correo electrónico, número de teléfono, nombre completo, documento de identidad, dirección o detalles de pedidos, como `external_id`. Trata `external_id` como sensible a mayúsculas y minúsculas durante toda esta integración.
{% endalert %}

Este tutorial usa `stayfilm-poc-001` como ejemplo de `external_id`. Toma nota del valor que elijas, ya que lo usarás en pasos posteriores.

### Paso 2: Crear una transformación de datos {#step-2-create-a-data-transformation}

Crea una transformación de datos para recibir las devoluciones de llamada de Stayfilm y actualizar los perfiles de usuario.

1. Ve a **Configuración de datos** > **Transformación de datos**.
2. Selecciona **Crear transformación**.
3. Introduce un nombre, como `Stayfilm Callback Data Transformation`.
4. En **Experiencia de edición**, selecciona **Empezar desde cero**.
5. En **Seleccionar destino** > **Destino**, selecciona **POST: Rastrear usuarios**.
6. Selecciona **Crear transformación**.
7. Reemplaza el código de transformación predeterminado con el siguiente:

```javascript
const brazeExternalId = payload.RelayedData;
if (!brazeExternalId) {
  throw new Error("Missing RelayedData. Expected Stayfilm callback to relay the Braze external_id from CallbackRelayData.");
}

const idJob = payload.IdJob || null;
const producedFiles = payload.ProducedFiles || {};
const videoUrl = producedFiles?.Videos?.VideoMP4?.Url || null;
const errorMessage = payload.ErrorMessage || null;
const hasError = payload.HasError === true || Boolean(errorMessage);
const isReady = !hasError && Boolean(videoUrl);
const now = new Date().toISOString();

let brazecall = {
  attributes: [
    {
      external_id: brazeExternalId,
      _update_existing_only: true,
      stayfilm_video_status: isReady ? "ready" : "failed",
      stayfilm_video_url: videoUrl || null,
      stayfilm_job_id: idJob,
      stayfilm_render_error: errorMessage,
      stayfilm_callback_received_at: now
    }
  ],
  events: [
    {
      external_id: brazeExternalId,
      _update_existing_only: true,
      name: isReady ? "stayfilm_video_ready" : "stayfilm_video_failed",
      time: now,
      properties: {
        stayfilm_job_id: idJob,
        stayfilm_video_url: videoUrl || null,
        stayfilm_render_error: errorMessage,
        stayfilm_status: payload.Status || payload.status || null
      }
    }
  ]
};

return brazecall;
```

{: start="8"}
8. Selecciona **Guardar** y luego copia la URL del webhook generada.
9. Envía una solicitud `POST` de prueba a la URL del webhook con el siguiente JSON de devolución de llamada de ejemplo de Stayfilm. Establece `RelayedData` con el `external_id` del usuario de prueba que creaste en el paso 1.

```json
{
  "IdJob": "debug-job-001",
  "HasError": false,
  "Status": "DRAFT_DONE",
  "ProducedFiles": {
    "Videos": {
      "VideoMP4": {
        "Url": "https://example.com/stayfilm-poc-video.mp4"
      }
    }
  },
  "RelayedData": "stayfilm-poc-001"
}
```

Envía la solicitud con cURL, Postman o una herramienta similar. Una respuesta exitosa devuelve el estado HTTP `201` con `{"message": "success"}`.

{: start="10"}
10. Ve a **Configuración de datos** > **Transformación de datos** y recarga la página si tu transformación no aparece en la lista.
11. Abre la transformación y selecciona **Validar**. Confirma que la validación se completa correctamente en **Salida**.
12. Selecciona **Activar**.
13. Proporciona la URL del webhook copiada a Stayfilm como tu URL de devolución de llamada.

{% alert note %}
Si almacenas más que el `external_id` de Braze en `CallbackRelayData`, actualiza el código de transformación para analizar `RelayedData` en consecuencia.
{% endalert %}

### Paso 3: Crear una campaña webhook para enviar trabajos a Stayfilm {#step-3-create-a-webhook-campaign-to-send-jobs-to-stayfilm}

Crea una [campaña webhook]({{site.baseurl}}/user_guide/channels/webhooks) que envíe trabajos de renderizado a Stayfilm.

{% alert important %}
Antes de probar la campaña, confirma que Stayfilm ha configurado tu proyecto con la URL de devolución de llamada de la transformación de datos del paso 2.
{% endalert %}

1. Ve a **Mensajería** > **Campaigns**.
2. Selecciona **Crear campaña** > **Webhook**.
3. Introduce un nombre para la campaña, como `Stayfilm Webhook Integration`.
4. Selecciona **Componer webhook** > **Empezar desde cero**.
5. En **Componer webhook** > **URL del webhook**, introduce la URL del endpoint `POST /Job` de Stayfilm proporcionada por Stayfilm. Reemplaza *`{BASE_URL}`* en el siguiente ejemplo: `https://{BASE_URL}/stg/v3/job`
6. Establece **Método HTTP** en **POST**.
7. En **Cuerpo de la solicitud**, selecciona **Texto sin formato** y luego pega la carga útil del trabajo que Stayfilm proporciona. Puedes usar [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) para hacer el cuerpo dinámico.

Incluye `CallbackRelayData` establecido con el `external_id` del usuario de Braze. Stayfilm devuelve este valor en la devolución de llamada como `RelayedData`.

{% raw %}
```json
{
  "SmartTags": ["Setup-Template"],
  "Medias": [
    {
      "Group": "userMedia",
      "URL": "https://{BASE_URL}/some_media.png"
    }
  ],
  "Videos": [{}],
  "CallbackRelayData": "stayfilm-poc-001"
}
```
{% endraw %}

Añade los siguientes encabezados de solicitud:

| Clave | Valor |
| --- | ----- |
| `idproject` | El valor de `idproject` proporcionado por Stayfilm |
| `Subscription-Key` | La `Subscription-Key` proporcionada por Stayfilm |
| `Content-Type` | `application/json` |
| `Authorization` | Token de portador OAuth obtenido a través de contenido conectado (consulta el siguiente ejemplo) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Encabezados de solicitud" }

En el siguiente bloque de contenido conectado, reemplaza *`{TENANT_ID}`*, *`{CLIENT_ID}`*, *`{CLIENT_SECRET_URL_ENCODED}`* y *`{SCOPE_URL_ENCODED}`* con los valores que Stayfilm proporciona. Codifica en URL *`{CLIENT_SECRET_URL_ENCODED}`* y *`{SCOPE_URL_ENCODED}`* antes de pegarlos en el bloque. Para los requisitos de OAuth, consulta la [documentación de la API de Stayfilm](https://apidoc.stayfilm.com).

{% raw %}
```
{% connected_content https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token
  :method post
  :body grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET_URL_ENCODED}&scope={SCOPE_URL_ENCODED}
  :content_type application/x-www-form-urlencoded
  :cache_max_age 3000
  :save stayfilm_auth
%}Bearer {{stayfilm_auth.access_token}}
```
{% endraw %}

{: start="8"}
8. Selecciona **Guardar borrador**.

{% alert note %}
Si sales de la página de Campaigns y regresas, establece **Estado** en **Todos** para encontrar las campañas que aún están en **Borrador**.
{% endalert %}

### Paso 4: Probar la campaña webhook {#step-4-test-the-webhook-campaign}

1. Desde el creador de webhooks, selecciona la pestaña **Prueba**.
2. En **Vista previa del mensaje como usuario**, selecciona **Seleccionar usuario existente** y luego busca tu usuario de prueba (por ejemplo, `stayfilm-poc-001`).
3. Selecciona **Enviar prueba**.

Una respuesta exitosa devuelve el estado HTTP `201` con un cuerpo JSON similar al siguiente:

```json
{
  "IdJob": "4557a77e-f56c-48be-81f7-2d8c5e558cb1",
  "Videos": [
    {
      "IdVideo": "87287b25-7814-4fa1-ad1a-f2ea89822d0f",
      "IdGenre": "f07a1334-5904-420a-9f31-92644f245c5a",
      "IdVideoTemplate": "7b77c3df-12a1-4636-a9b4-bc227f4c233f",
      "IdProject": "73ea3e73-b41e-4676-b674-51731d3bf49c",
      "Status": "DRAFT_RENDERING_PENDING",
      "DurationInSeconds": null,
      "URL": null,
      "ErrorMessage": null,
      "CreatedAt": "2026-06-16T00:35:28.7736263Z",
      "UpdatedAt": "2026-06-16T00:35:28.7736264Z",
      "IdVideoFather": null,
      "IdVideoSon": null,
      "ProducingStatus": "PENDING"
    }
  ],
  "Images": []
}
```

### Paso 5: Confirmar la devolución de llamada de Stayfilm {#step-5-confirm-the-stayfilm-callback}

Stayfilm renderiza el video de forma asíncrona y envía una devolución de llamada a tu transformación de datos cuando el procesamiento se completa. Monitoriza el estado del trabajo a través de los endpoints de la API de Stayfilm descritos en la [documentación de la API de Stayfilm](https://apidoc.stayfilm.com).

1. Ve a **Configuración de datos** > **Transformación de datos**.
2. Selecciona la pestaña **Registros** de tu transformación.
3. Confirma que aparece una devolución de llamada con el estado **Éxito**.

### Paso 6: Mostrar el video en un mensaje dentro de la aplicación {#step-6-display-the-video-in-an-in-app-message}

Después de que `stayfilm_video_url` se haya rellenado en el perfil de usuario, muestra el video renderizado en una campaña o Canvas.

1. Ve a **Mensajería** > **Campaigns**.
2. Selecciona **Crear campaña** > **Mensaje dentro de la aplicación**.
3. Introduce un nombre para la campaña, como `Stayfilm Video Show`.
4. En el creador de mensajes, selecciona **Editor tradicional**.
5. En **Enviar a**, selecciona **Navegadores web**.
6. Establece **Tipo de mensaje** en **Código personalizado**.
7. Pega el siguiente HTML en el campo **HTML**:

{% raw %}
```html
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
<div id="stayfilm-video-url" style="display: none;">{{custom_attribute.${stayfilm_video_url}}}</div>
<video id="stayfilm-video" controls preload="metadata" playsinline style="width: 100%; max-width: 420px; border-radius: 12px; background: #000;">
Your browser does not support HTML5 video.
</video>
<script>
(function () {
  var urlElement = document.getElementById("stayfilm-video-url");
  var video = document.getElementById("stayfilm-video");
  var videoUrl = urlElement ? urlElement.textContent.trim() : "";
  if (!videoUrl || videoUrl.indexOf("http") !== 0) {
    return;
  }
  var source = document.createElement("source");
  source.src = videoUrl;
  source.type = "video/mp4";
  video.appendChild(source);
  video.load();
})();
</script>
</body>
</html>
```
{% endraw %}

{: start="8"}
8. Selecciona **Guardar borrador**.
9. Selecciona la pestaña **Prueba**.
10. En **Vista previa del mensaje como usuario**, selecciona **Seleccionar usuario existente** y luego busca el `external_id` de tu usuario de prueba.

El video renderizado aparece y se reproduce en la vista previa cuando `stayfilm_video_url` está establecido en el perfil.

## Ampliar la integración {#extend-the-integration}

Este recorrido cubre un subconjunto de la API de Stayfilm. Para adaptar plantillas de trabajo, entradas de medios o mensajería posterior, consulta la [documentación de la API de Stayfilm](https://apidoc.stayfilm.com) y actualiza la carga útil de tu webhook, el mapeado de Data Transformation y la lógica de tu Campaign en consecuencia.

## Consideraciones {#considerations}

- **Renderizado asíncrono:** La generación de video no es inmediata. Desencadena mensajes de seguimiento a partir del evento personalizado `stayfilm_video_ready` o del Segment basado en `stayfilm_video_status` en lugar de enviar el mensaje dentro de la aplicación en el mismo flujo que el webhook.
- **Consistencia del identificador:** El valor en `CallbackRelayData` debe coincidir exactamente con el `external_id` del usuario de Braze.
- **Almacenamiento en caché del token OAuth:** El ejemplo de contenido conectado almacena en caché el token OAuth durante 3000 segundos. Ajusta `cache_max_age` si Stayfilm cambia los requisitos de duración del token.
- **Pruebas en sandbox:** Valida el ciclo completo de devolución de llamada en un sandbox de Braze antes de lanzar en producción.
- **Capacidad de atributos personalizados:** Confirma que tu espacio de trabajo tiene capacidad para los atributos personalizados y eventos de Stayfilm que crea esta integración.

## Solución de problemas {#troubleshooting}

Consulta la siguiente tabla si experimentas problemas con la integración de Stayfilm.

| Problema | Resolución |
| ----- | ---------- |
| La validación de Data Transformation falla | Confirma que `RelayedData` en tu carga útil de prueba coincide con un `external_id` válido de Braze, luego recarga la página de **Data Transformation** antes de seleccionar **Validate**. |
| La prueba del webhook devuelve una respuesta diferente a 201 | Verifica las credenciales de Stayfilm en tus encabezados de solicitud, confirma que el bloque de contenido conectado OAuth usa valores codificados para URL y comprueba que tu URL de `POST /Job` sea correcta. |
| La devolución de llamada no aparece en los registros de transformación | Confirma que Stayfilm tiene tu URL de webhook de Data Transformation activa y espera a que el renderizado del video se complete. |
| La vista previa dentro de la aplicación no muestra el video | Confirma que `stayfilm_video_url` está configurado en el perfil de usuario de prueba y que el mensaje dentro de la aplicación apunta a **Web Browsers** con **Custom Code**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas" }