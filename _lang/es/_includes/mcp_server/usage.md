# Utiliza el servidor MCP de Braze {#using-the-braze-mcp-server}

> Aprende a interactuar con tus datos de Braze utilizando herramientas de lenguaje natural como Claude y Cursor. Para obtener información más general, consulta [Servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Requisitos previos {#prerequisites}

Antes de poder utilizar esta característica, tendrás que [configurar el servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Buenas prácticas {#best-practices}

Cuando utilices el servidor MCP de Braze a través de herramientas de lenguaje natural como Claude y Cursor, ten en cuenta estos consejos para obtener los mejores resultados:

- Los LLM pueden cometer errores, así que asegúrate siempre de verificar sus respuestas.
- Para el análisis de datos, ten claro el intervalo de tiempo que necesitas. Los rangos más cortos suelen dar resultados más precisos.
- Utiliza la [terminología exacta de Braze](https://www.braze.com/resources/articles/glossary) para que tu LLM llame a la función correcta.
- Si los resultados parecen incompletos, pide a tu LLM que continúe o profundice más.
- ¡Prueba con indicaciones creativas! Dependiendo de tu cliente MCP, es posible que puedas exportar un archivo CSV u otros archivos útiles.

## Ejemplos de uso {#usage-examples}

Después de [configurar el servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, puedes interactuar con Braze mediante lenguaje natural utilizando herramientas como Claude o Cursor. Aquí tienes algunos ejemplos para empezar:

### ¿Cuáles son mis funciones disponibles de Braze? {#what-are-my-available-braze-functions}

{% tabs %}
{% tab Claude %}
**Indicación de ejemplo**

`What are my available Braze functions?`

**Respuesta de ejemplo**

Consulté el servidor MCP de Braze con `list_functions` y encontré 38 funciones de API disponibles.

Aquí tienes algunos ejemplos por categoría:

- **Análisis y gestión de Campaigns**
  - `get_campaign_dataseries`
  - `get_campaign_details`
  - `get_campaign_list`
- **Análisis y gestión de Canvas**
  - `get_canvas_data_series`
  - `get_canvas_data_summary`
  - `get_canvas_list`
  - `get_canvas_details`
- **Plantillas**
  - `create_email_template`
- **Content Blocks**
  - `create_content_block`
  - `get_content_blocks`
  - `get_content_block_info`
  - `update_content_block`
{% endtab %}

{% tab Cursor %}
**Indicación de ejemplo**

`What are my available Braze functions?`

**Respuesta de ejemplo**

Voy a comprobar tus funciones disponibles utilizando el servidor MCP de Braze.

- Se llamó a `list_functions`

Según ese resultado, tienes 38 funciones de API de Braze organizadas en categorías como:

- Análisis y gestión de Campaigns
- Análisis y gestión de Canvas
- Plantillas
- Content Blocks

Algunos ejemplos de funciones incluyen:

- `get_campaign_list`
- `get_canvas_list`
- `get_canvas_details`
- `create_email_template`
- `update_content_block`
{% endtab %}
{% endtabs %}

Para obtener más información sobre la función `list_functions`, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#general-functions){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#general-functions){% endif %}.

### Obtener detalles sobre un ID de Canvas {#get-details-about-a-canvas-id}

{% tabs %}
{% tab Claude %}
**Indicación de ejemplo**

`Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Respuesta de ejemplo**

Obtuve los detalles de `YOUR-TEST-CANVAS-ID-123` utilizando `get_canvas_details`.

- **Nombre del Canvas:** `YOUR-TEST-CANVAS-NAME`
- **ID:** `YOUR-TEST-CANVAS-ID-123`
- **Estado:** Borrador (no habilitado)
- **Creado el:** 15 ene 2026, 10:30 AM UTC
- **Última actualización:** 16 ene 2026, 02:45 PM UTC
- **Tipo de planificación:** Basado en tiempo
- **Canal principal:** Correo electrónico

Detalles del mensaje de correo electrónico:

- **Asunto:** `YOUR-TEST-SUBJECT-LINE`
- **De:** `YOUR-TEST-SENDER@example.com`
- **ID del mensaje:** `YOUR-TEST-MESSAGE-ID-123`
{% endtab %}

{% tab Cursor %}
**Indicación de ejemplo**

`Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Respuesta de ejemplo**

Obtuve este Canvas utilizando `get_canvas_details`:

- **ID del Canvas:** `YOUR-TEST-CANVAS-ID-123`
- **Nombre del Canvas:** `YOUR-TEST-CANVAS-NAME`
- **Estado:** Borrador
- **Canal:** Correo electrónico
- **ID del mensaje:** `YOUR-TEST-MESSAGE-ID-123`

Resumen del contenido del correo electrónico:

1. Sección de encabezado con imagen de marca
2. Sección de título principal
3. Sección hero con botón CTA
4. Sección de características con contenido de apoyo
{% endtab %}
{% endtabs %}

Para obtener más información sobre la función `get_canvas_details`, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Muéstrame mis Canvas recientes {#show-me-my-recent-canvases}

{% tabs %}
{% tab Claude %}
**Indicación de ejemplo**

`Show me my recent Canvases`

**Respuesta de ejemplo**

Comprobé tus herramientas disponibles con `list_functions` y luego utilicé `get_canvas_list` para obtener tus Canvas editados más recientemente.

Canvas más recientes:

1. **YOUR-TEST-CANVAS-ALPHA**
   - ID: `YOUR-TEST-ID-123`
   - Última edición: 16 ene 2026, 02:45 PM UTC
2. **YOUR-TEST-CANVAS-BETA**
   - ID: `YOUR-TEST-ID-456`
   - Última edición: 15 ene 2026, 11:10 AM UTC
3. **YOUR-TEST-CANVAS-GAMMA**
   - ID: `YOUR-TEST-ID-789`
   - Última edición: 14 ene 2026, 08:25 PM UTC
{% endtab %}

{% tab Cursor %}
**Indicación de ejemplo**

`Show me my recent Canvases`

**Respuesta de ejemplo**

Voy a obtener tu lista de Canvas recientes del servidor MCP de Braze.

- Se llamó a `list_functions`
- Se llamó a `get_canvas_list`

Canvas recientes (ordenados por edición más reciente):

- **Nombre del Canvas:** `YOUR-TEST-CANVAS-ALPHA`
  - **Última edición:** 16 ene 2026, 02:45 PM UTC
  - **ID del Canvas:** `YOUR-TEST-ID-123`
  - **Etiquetas:** `lifecycle`, `email`
- **Nombre del Canvas:** `YOUR-TEST-CANVAS-BETA`
  - **Última edición:** 15 ene 2026, 11:10 AM UTC
  - **ID del Canvas:** `YOUR-TEST-ID-456`
  - **Etiquetas:** `promo`
{% endtab %}
{% endtabs %}

Para obtener más información sobre la función `get_canvas_list`, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Crear una plantilla de correo electrónico {#create-an-email-template}

{% tabs %}
{% tab Claude %}
**Indicación de ejemplo**

`Create an email template named "YOUR-TEST-TEMPLATE-NAME" for onboarding messages.`

**Respuesta de ejemplo**

Creé tu plantilla con `create_email_template`.

- **Nombre de la plantilla:** `YOUR-TEST-TEMPLATE-NAME`
- **ID de la plantilla:** `YOUR-TEST-TEMPLATE-ID-123`
- **Línea del asunto:** `YOUR-TEST-SUBJECT-LINE`
- **Preencabezado:** `YOUR-TEST-PREHEADER`
- **Creada el:** 16 ene 2026, 03:10 PM UTC

Ahora puedes hacer referencia a `YOUR-TEST-TEMPLATE-ID-123` al crear o actualizar Campaigns y Canvas.
{% endtab %}

{% tab Cursor %}
**Indicación de ejemplo**

`Create an email template named "YOUR-TEST-TEMPLATE-NAME" for onboarding messages.`

**Respuesta de ejemplo**

Utilicé `create_email_template` y creé una nueva plantilla correctamente.

- **ID de la plantilla:** `YOUR-TEST-TEMPLATE-ID-123`
- **Nombre de la plantilla:** `YOUR-TEST-TEMPLATE-NAME`
- **Asunto:** `YOUR-TEST-SUBJECT-LINE`
- **Descripción:** `Onboarding lifecycle template`

Si lo deseas, también puedo generar un cuerpo HTML inicial y una alternativa en texto plano para esta plantilla.
{% endtab %}
{% endtabs %}

Para obtener más información sobre la función `create_email_template`, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}.

### Actualizar un bloque de contenido {#update-a-content-block}

{% tabs %}
{% tab Claude %}
**Indicación de ejemplo**

`Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123" with new body copy for our spring promotion.`

**Respuesta de ejemplo**

Actualicé tu bloque de contenido utilizando `update_content_block`.

- **ID del bloque de contenido:** `YOUR-TEST-CONTENT-BLOCK-ID-123`
- **Nombre:** `YOUR-TEST-CONTENT-BLOCK-NAME`
- **Estado:** Actualizado
- **Actualizado el:** 16 ene 2026, 03:25 PM UTC

Vista previa:

`YOUR-TEST-CONTENT-BLOCK-BODY-V2`
{% endtab %}

{% tab Cursor %}
**Indicación de ejemplo**

`Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123" with new body copy for our spring promotion.`

**Respuesta de ejemplo**

Ejecuté `update_content_block` y confirmé que la actualización se completó.

- **ID del bloque de contenido:** `YOUR-TEST-CONTENT-BLOCK-ID-123`
- **Versión anterior:** `v1`
- **Versión actual:** `v2`
- **Última actualización:** 16 ene 2026, 03:25 PM UTC

Vista previa del contenido actualizado:

`YOUR-TEST-CONTENT-BLOCK-BODY-V2`
{% endtab %}
{% endtabs %}

Para obtener más información sobre la función `update_content_block`, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#content-blocks){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#content-blocks){% endif %}.

{% multi_lang_include mcp_server/legal_disclaimer.md %}