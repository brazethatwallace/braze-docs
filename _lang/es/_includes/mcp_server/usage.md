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
![«¿Cuáles son mis funciones disponibles de Braze?», pregunta y respuesta en Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![«¿Cuáles son mis funciones disponibles de Braze?», pregunta y respuesta en Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

Para obtener más información sobre la función `list_functions`, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#general-functions){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#general-functions){% endif %}.

### Obtener detalles sobre un ID de Canvas {#get-details-about-a-canvas-id}

{% tabs %}
{% tab Claude %}
![«Obtener detalles sobre un ID de Canvas», pregunta y respuesta en Claude.]({% image_buster /assets/img/mcp_server/claude/get_details_about_a_canvas_id.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![«Obtener detalles sobre un ID de Canvas», pregunta y respuesta en Cursor.]({% image_buster /assets/img/mcp_server/cursor/get_details_about_a_canvas_id.png %})
{% endtab %}
{% endtabs %}

Para obtener más información sobre la función `get_canvas_details`, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Muéstrame mis Canvas recientes {#show-me-my-recent-canvases}

{% tabs %}
{% tab Claude %}
![«Muéstrame mis Canvas recientes», pregunta y respuesta en Claude.]({% image_buster /assets/img/mcp_server/claude/show_my_recent_canvases.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![«Muéstrame mis Canvas recientes», pregunta y respuesta en Cursor.]({% image_buster /assets/img/mcp_server/cursor/show_me_my_recent_canvases.png %})
{% endtab %}
{% endtabs %}

Para obtener más información sobre la función `get_canvas_list`, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Crear una plantilla de correo electrónico {#create-an-email-template}

{% tabs %}
{% tab Cursor %}
![«Crear una plantilla de correo electrónico», pregunta y respuesta en Cursor.]({% image_buster /assets/img/mcp_server/cursor/create_an_email_template.png %})
{% endtab %}
{% endtabs %}

Para obtener más información sobre la función `create_email_template`, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}.

### Actualizar un bloque de contenido {#update-a-content-block}

{% tabs %}
{% tab Cursor %}
![«Actualizar un bloque de contenido», pregunta y respuesta en Cursor.]({% image_buster /assets/img/mcp_server/cursor/update_a_content_block.png %})
{% endtab %}
{% endtabs %}

Para obtener más información sobre la función `update_content_block`, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#content-blocks){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#content-blocks){% endif %}.

{% multi_lang_include mcp_server/legal_disclaimer.md %}