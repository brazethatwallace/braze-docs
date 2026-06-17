# Uso del servidor MCP de Braze {#using-the-braze-mcp-server}

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
**Example prompt:** `What are my available Braze functions?`

**Example response:** Called `list_functions` and returned categories like Campaign, Canvas, Templates, and Content Blocks with sample functions such as `get_canvas_list` and `create_email_template`.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `What are my available Braze functions?`

**Example response:** Queried `list_functions`, confirmed available function groups, and listed examples including `get_canvas_details` and `update_content_block`.
{% endtab %}
{% endtabs %}

Para obtener más información sobre la función `list_functions`, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#general-functions){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#general-functions){% endif %}.

### Obtener detalles sobre un ID de Canvas {#get-details-about-a-canvas-id}

{% tabs %}
{% tab Claude %}
**Example prompt:** `Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Example response:** Used `get_canvas_details` and returned sample metadata (status, channel, created/updated time) for `YOUR-TEST-CANVAS-ID-123`.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Example response:** Returned Canvas and message details with dummy values like `YOUR-TEST-MESSAGE-ID-123` and `YOUR-TEST-SUBJECT-LINE`.
{% endtab %}
{% endtabs %}

Para obtener más información sobre la función `get_canvas_details`, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Muéstrame mis Canvas recientes {#show-me-my-recent-canvases}

{% tabs %}
{% tab Claude %}
**Example prompt:** `Show me my recent Canvases`

**Example response:** Called `get_canvas_list` and returned recent items such as `YOUR-TEST-CANVAS-ALPHA` with IDs like `YOUR-TEST-ID-123`.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `Show me my recent Canvases`

**Example response:** Listed recently edited Canvases with sample values for name, last edited time, ID, and tags.
{% endtab %}
{% endtabs %}

Para obtener más información sobre la función `get_canvas_list`, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Crear una plantilla de correo electrónico {#create-an-email-template}

{% tabs %}
{% tab Cursor %}
**Example prompt:** `Create an email template named "YOUR-TEST-TEMPLATE-NAME".`

**Example response:** Created a template via `create_email_template` and returned `YOUR-TEST-TEMPLATE-ID-123`.
{% endtab %}
{% endtabs %}

Para obtener más información sobre la función `create_email_template`, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}.

### Actualizar un bloque de contenido {#update-a-content-block}

{% tabs %}
{% tab Cursor %}
**Example prompt:** `Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123".`

**Example response:** Updated the block with `update_content_block` and confirmed `YOUR-TEST-CONTENT-BLOCK-ID-123` moved to a new version.
{% endtab %}
{% endtabs %}

Para obtener más información sobre la función `update_content_block`, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#content-blocks){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#content-blocks){% endif %}.

{% multi_lang_include mcp_server/legal_disclaimer.md %}