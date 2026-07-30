# El servidor MCP de Braze {#the-braze-mcp-server}

> Descubre el servidor MCP de Braze, una conexión remota segura que permite a herramientas de IA como Claude y Cursor acceder a datos de Braze que no son PII para responder preguntas, analizar tendencias, proporcionar información y crear contenido.

{% alert important %}
El servidor MCP remoto se encuentra en acceso anticipado. Ponte en contacto con tu director de cuentas para solicitar acceso.
{% endalert %}

## ¿Qué es Model Context Protocol (MCP)? {#what-is-model-context-protocol-mcp}

​​Model Context Protocol, o MCP, es un estándar que permite a los agentes de IA conectarse y trabajar con datos de otra plataforma. Tiene dos partes principales:

- **Cliente MCP:** La aplicación donde se ejecuta el agente de IA, como Cursor o Claude.
- **Servidor MCP:** Un servicio proporcionado por otra plataforma, como Braze, que define qué herramientas puede utilizar la IA y a qué datos puede acceder.

## Acerca del servidor MCP de Braze {#about-the-braze-mcp-server}

Después de [configurar el servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, puedes conectar herramientas de IA como agentes, asistentes y chatbots directamente a Braze, permitiéndoles leer datos agregados como análisis de Canvas y Campaign, atributos personalizados, Segments y más. El servidor MCP de Braze es ideal para:

- Crear herramientas impulsadas por IA que necesiten contexto de Braze.
- Ingenieros de CRM que crean flujos de trabajo de agentes con múltiples pasos.
- Especialistas en marketing técnico que experimentan con consultas en lenguaje natural.

El servidor MCP de Braze incluye herramientas de lectura y escritura. Estas herramientas no devuelven datos de los perfiles de usuario de Braze. Tus agentes heredan los permisos de usuario del panel de Braze. Para ver la lista completa de herramientas disponibles, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}.

{% alert warning %}
Las herramientas que exponen PII a nivel de usuario no están disponibles.
{% endalert %}

Usa el servidor MCP para hacer preguntas sobre el rendimiento de Campaign y Canvas, explorar tus Segments y atributos personalizados, generar informes y crear contenido como plantillas de correo electrónico, Content Blocks y activos de la biblioteca de medios a través de lenguaje natural.

## ¿El servidor MCP beta está obsoleto? {#is-the-beta-mcp-server-deprecated}

Sí. El servidor MCP alojado localmente lanzado en agosto de 2025 está obsoleto y no recibirá actualizaciones adicionales. Puedes seguir usándolo, pero Braze recomienda migrar a la versión alojada de forma remota.

### ¿En qué se diferencia el servidor remoto? {#how-is-the-remote-server-different}

El servidor MCP de Braze anterior se ejecutaba localmente en tu máquina. Necesitabas instalar un paquete, gestionar un archivo de configuración y crear una clave de API de Braze con los permisos adecuados. El servidor MCP remoto elimina esa configuración local.

Conéctate desde un cliente MCP compatible en menos de un minuto. La autenticación utiliza OAuth. El acceso está vinculado a tu cuenta de usuario del panel de Braze, no a una clave de API compartida, por lo que lo que un agente puede ver y hacer refleja tus permisos del panel. Si un usuario del panel pierde el acceso en Braze, el cliente también pierde el acceso.

Las diferencias principales son:

- **Configuración:** Pega una URL de Braze en lugar de instalar un paquete y editar archivos de configuración.
- **Autenticación:** Inicia sesión con tu cuenta de Braze en lugar de crear una clave de API.
- **Permisos:** El acceso se basa en tu cuenta de usuario del panel en lugar de en los permisos de la clave de API.
- **Selección de espacio de trabajo:** El contexto del espacio de trabajo se pasa por solicitud en lugar de estar fijado en la configuración local.

## Preguntas más frecuentes (FAQ) {#faq}

### ¿Qué clientes MCP son compatibles? {#which-mcp-clients-are-supported}

Cualquier cliente MCP que admita servidores MCP remotos con OAuth puede funcionar. Braze ha verificado:

- Claude a través de conectores personalizados
- ChatGPT a través de conectores personalizados
- Cursor
- OpenAI Codex
- Claude Code
- Visual Studio Code

### ¿A qué datos de Braze puede acceder mi cliente MCP? {#what-braze-data-can-my-mcp-client-access}

Los clientes MCP pueden acceder a herramientas que no devuelven PII a nivel de usuario.

### ¿Mi cliente MCP puede modificar datos de Braze? {#can-my-mcp-client-change-braze-data}

Sí, si tu usuario del panel tiene esos permisos.

### ¿Sigo necesitando una clave de API de Braze? {#do-i-still-need-a-braze-api-key}

No para MCP. Las claves de API siguen funcionando para la REST API y no se van a descontinuar.

### ¿Qué regiones son compatibles? {#which-regions-are-supported}

Ambos clústeres de Braze son compatibles. Actualmente hay dos endpoints disponibles:

- `https://mcp.braze.com/mcp` (EE. UU.)
- `https://mcp.braze.eu/mcp` (UE)

Cualquiera de los dos endpoints puede conectarse a cualquier clúster de Braze.

### ¿Puedo utilizar el servidor MCP remoto de Braze con herramientas distintas a las de la lista verificada? {#can-i-use-the-braze-remote-mcp-server-with-tools-other-than-the-verified-list}

Puedes intentarlo, pero la autenticación podría bloquearse. Actualmente, Braze mantiene una lista de dominios permitidos por seguridad. Si tu herramienta no está en la lista y tienes problemas de autenticación, ponte en contacto con [mcp-product@braze.com](mailto:mcp-product@braze.com).

### ¿El servidor remoto admite múltiples espacios de trabajo? {#does-the-remote-server-support-multiple-workspaces}

Sí. Especifica el espacio de trabajo por conversación o por solicitud. Una sola conexión cubre todos los espacios de trabajo a los que tienes acceso autorizado.

### ¿Mi agente puede acceder a PII a nivel de usuario? {#can-my-agent-access-user-level-pii}

No. Actualmente, las herramientas que exponen PII no están disponibles.

### ¿Qué sucede cuando cambian mis permisos? {#what-happens-when-my-permissions-change}

El acceso del agente cambia con el usuario del panel. Los cambios de permisos se aplican en la siguiente solicitud. Los usuarios del panel desactivados pierden el acceso a MCP.

### ¿Por qué no veo el conector de Braze en el directorio de mi cliente? {#why-do-i-not-see-the-braze-connector-in-my-clients-directory}

Los listados del directorio se implementan después de que comience el acceso anticipado. Siempre puedes conectarte manualmente utilizando la URL de MCP de Braze.

### Mi empresa utiliza listas de IP permitidas. ¿Podemos usar el servidor MCP remoto? {#my-company-uses-ip-allowlisting-can-we-use-the-remote-mcp-server}

No por el momento. Los clientes que utilizan [listas de IP permitidas](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#dashboard-ip-allowlisting) no pueden participar en el programa de acceso anticipado.

{% multi_lang_include mcp_server/legal_disclaimer.md %}