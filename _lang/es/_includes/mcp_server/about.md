# El servidor MCP de Braze {#the-braze-mcp-server}

> Descubre el servidor MCP de Braze, una conexión segura que permite a herramientas de IA como Claude y Cursor acceder a datos de Braze que no son PII para responder preguntas, analizar tendencias y proporcionar información.

{% multi_lang_include mcp_server/beta_alert.md %}

{% alert important %}
## Fin del soporte del servidor MCP de Braze alojado localmente {#sunsetting-the-locally-hosted-braze-mcp-server}

Este verano, Braze lanzará un servidor MCP remoto, alojado por Braze, en acceso anticipado. Sustituye al servidor beta alojado localmente (`braze-mcp-server` en [PyPI](https://pypi.org/project/braze-mcp-server/) y el directorio de extensiones de Claude Desktop).

**Qué significa esto para ti:**

- El servidor alojado localmente seguirá funcionando, pero ya no cuenta con soporte. No añadiremos nuevos puntos finales ni corregiremos problemas en la versión beta.
- Cuando el servidor remoto esté disponible en acceso anticipado, tendrás que migrar a él. El servidor remoto no requiere instalación local, utiliza OAuth en lugar de claves de API estáticas y funciona con clientes MCP como Claude, Copilot, Gemini CLI, Codex y Cursor.
- Consulta esta página para conocer la disponibilidad del acceso anticipado, o ponte en contacto con tu equipo de cuentas de Braze para expresar tu interés.
{% endalert %}

## ¿Qué es el protocolo de contexto de modelo (MCP)? {#what-is-model-context-protocol-mcp}

​​El protocolo de contexto de modelo, o MCP, es un estándar que permite a los agentes de IA conectarse y trabajar con datos de otra plataforma. Tiene dos partes principales:

- **Cliente MCP:** La aplicación en la que se ejecuta el agente de IA, como Cursor o Claude.
- **Servidor MCP:** Un servicio proporcionado por otra plataforma, como Braze, que define qué herramientas puede utilizar la IA y a qué datos puede acceder.

## Acerca del servidor MCP de Braze {#about-the-braze-mcp-server}

Después de [configurar el servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, puedes conectar herramientas de IA como agentes, asistentes y chatbots directamente a Braze, lo que les permite leer datos agregados como análisis de Canvas y Campaign, atributos personalizados, Segments y mucho más. El servidor MCP de Braze es ideal para:

- Crear herramientas basadas en IA que necesitan el contexto de Braze.
- Ingenieros de CRM que crean flujos de trabajo de agentes de varios pasos.
- Especialistas en marketing técnicos que experimentan con consultas en lenguaje natural.

El servidor MCP de Braze incluye puntos finales de solo lectura y de escritura. No devuelven datos de los perfiles de usuario de Braze. Tú eliges qué puntos finales asignar a tu clave de API de Braze, y esa elección controla lo que un agente puede leer, crear o actualizar. Para ver la lista completa de puntos finales disponibles y sus permisos requeridos, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}.

{% alert warning %}
Asigna solo los permisos de clave de API que quieras que tenga tu agente. Si no quieres que tu agente realice cambios en Braze, asegúrate de dejar desactivados los permisos de escritura cuando crees tu clave de API. Los agentes pueden intentar escribir datos a través de cualquier permiso de escritura que concedas.
{% endalert %}

## Ejemplo de uso {#usage-example}

Puedes interactuar con Braze mediante lenguaje natural utilizando herramientas como Claude o Cursor. Para ver otros ejemplos y prácticas recomendadas, consulta [Uso del servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
**Ejemplo de prompt:** `What are my available Braze functions?`
**Ejemplo de respuesta:** Utilizó `list_functions` y devolvió las categorías de funciones MCP de Braze disponibles.
{% endtab %}

{% tab Cursor %}
**Ejemplo de prompt:** `What are my available Braze functions?`
**Ejemplo de respuesta:** Consultó `list_functions` y listó funciones como `get_canvas_list`.
{% endtab %}
{% endtabs %}

## Preguntas más frecuentes (FAQ) {#faq}

### ¿Qué clientes MCP son compatibles? {#which-mcp-clients-are-supported}

Solo [Claude](https://claude.ai/) y [Cursor](https://cursor.com/) son oficialmente compatibles. Debes tener una cuenta en uno de estos clientes para poder utilizar el servidor MCP de Braze.

### ¿A qué datos de Braze puede acceder mi cliente MCP? {#what-braze-data-can-my-mcp-client-access}

Los clientes MCP pueden acceder a puntos finales que no devuelven PII. Tú controlas qué puntos finales puede utilizar un agente a través de los permisos que asignas a tu clave de API.

### ¿Mi cliente MCP puede modificar datos de Braze? {#can-my-mcp-client-change-braze-data}

Sí. El servidor expone un conjunto específico de puntos finales de escritura que permiten a los agentes crear o actualizar contenido en tu espacio de trabajo, como activos de la Biblioteca de medios, plantillas de correo electrónico y Content Blocks. Cada punto final de escritura requiere su propio permiso de clave de API. Si no quieres que tu agente realice un cambio determinado en Braze, deja sin marcar ese permiso cuando crees tu clave de API. Para ver la lista completa de funciones de escritura y sus permisos requeridos, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}.

### ¿Puedo utilizar un servidor MCP de terceros para Braze? {#can-i-use-a-third-party-mcp-server-for-braze}

No se recomienda utilizar un servidor MCP de terceros para los datos de Braze. Utiliza únicamente el servidor oficial MCP de Braze alojado en [PyPi](https://pypi.org/project/braze-mcp-server/).

### ¿Por qué el servidor MCP de Braze no ofrece acceso a PII? {#why-doesnt-the-braze-mcp-server-offer-pii-access}

Para proteger los datos de usuario y al mismo tiempo respaldar casos de uso valiosos, el servidor se limita a puntos finales que normalmente no devuelven PII. Esto reduce el riesgo para tu espacio de trabajo y las personas que lo utilizan.

### ¿Puedo reutilizar mis claves de API? {#can-i-reuse-my-api-keys}

No. Tendrás que crear una nueva clave de API para tu cliente MCP. Recuerda dar acceso a tus herramientas de IA solo a aquello con lo que te sientas cómodo y evita conceder permisos elevados.

### ¿El servidor MCP de Braze está alojado localmente o de forma remota? {#is-the-braze-mcp-server-hosted-locally-or-remotely}

El servidor MCP de Braze actualmente disponible está alojado localmente. Este verano llegará en acceso anticipado un servidor MCP remoto, alojado por Braze, que sustituirá al servidor beta alojado localmente.

### ¿Por qué Cursor solo muestra funciones? {#why-is-cursor-only-listing-functions}

Comprueba si estás en modo de consulta o en modo de agente. Para utilizar el servidor MCP, debes estar en modo agente.

### ¿Qué hago cuando el agente devuelve una respuesta que parece incorrecta? {#what-do-i-do-when-the-agent-returns-an-answer-that-looks-incorrect}

Cuando trabajes con herramientas como Cursor, es posible que quieras probar a cambiar el modelo utilizado. Por ejemplo, si lo tienes configurado en automático, prueba a cambiarlo a un modelo específico y experimenta para descubrir cuál es el modelo con mejor rendimiento para tu caso de uso. También puedes intentar iniciar un nuevo chat y volver a intentar el prompt.

Si los problemas persisten, puedes enviarnos un correo electrónico a [mcp-product@braze.com](mailto:mcp-product@braze.com) para informarnos. Si es posible, incluye un video y amplía las funciones de llamada para que podamos ver qué llamadas intentó realizar el agente.

{% multi_lang_include mcp_server/legal_disclaimer.md %}