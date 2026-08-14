# Configurar el servidor Braze MCP {#setting-up-the-braze-mcp-server}

> Aprende a conectarte al servidor remoto Braze MCP, autenticarte con OAuth y empezar a utilizar las herramientas de Braze desde tu cliente MCP. Para más información, consulta [Servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Requisitos previos {#prerequisites}

Antes de empezar, asegúrate de tener lo siguiente:

| Requisito previo | Descripción |
|--------------|-------------|
| Inscripción en acceso anticipado | Tu director de cuentas puede inscribir a tu empresa en el programa de acceso anticipado. |
| Cliente MCP compatible | Cualquier cliente que admita servidores MCP remotos con OAuth puede funcionar. Braze ha verificado Claude, ChatGPT, Cursor, OpenAI Codex, Claude Code y Visual Studio Code. |
| Cuenta en el panel de Braze | Inicias sesión con tus credenciales normales de Braze, incluido SSO o SAML si tu empresa lo utiliza. No hay un inicio de sesión MCP independiente. |
| Selección del endpoint del servidor | Elige `https://mcp.braze.com/mcp` (EE. UU.) o `https://mcp.braze.eu/mcp` (UE). Cualquiera de los dos endpoints puede llegar a cualquier clúster de Braze. |
| Sin lista de IP permitidas | Los clientes que utilizan la [lista de IP permitidas](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#dashboard-ip-allowlisting) no pueden participar en el acceso anticipado en este momento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

{% alert note %}
El acceso de tu agente refleja tus permisos del panel. Si tu acceso al panel está limitado a un equipo en lugar de a un espacio de trabajo completo, es posible que algunas herramientas no funcionen durante el acceso anticipado.
{% endalert %}

## Gestión de acceso (para administradores) {#managing-access-for-admins}

### Conceder acceso {#grant-access}

Los administradores controlan el acceso al servidor MCP a través del permiso **Use MCP Server**. De forma predeterminada, los usuarios no tienen este permiso y debe concederse explícitamente.

Si un administrador no ve este permiso, contacta a tu director de cuentas de Braze para solicitar la inscripción en el Acceso Anticipado.

### Revocar acceso {#revoke-access}

Para revocar el acceso, elimina el permiso **Use MCP Server** del usuario. Eliminar los permisos del panel de un usuario también elimina esas capacidades de cualquier agente conectado en la siguiente solicitud.

### Auditar el uso {#audit-usage}

Cuando un usuario se conecta correctamente a través de OAuth, se registra un evento en el [informe de eventos de seguridad](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#security-event-report).

## Conecta tu cliente {#connect-your-client}

### Paso 1: Confirma los permisos y el acceso al espacio de trabajo {#step-1-confirm-permissions-and-workspace-access}

1. Tú o el administrador de tu empresa deben confirmar que tienes el permiso **Use MCP Server**.
2. Si necesitas acceso a varios espacios de trabajo, asegúrate de que el permiso esté habilitado para todos los espacios de trabajo relevantes.

### Paso 2: Añade Braze como conector MCP remoto {#step-2-add-braze-as-a-remote-mcp-connector}

En tu cliente MCP, añade un nuevo servidor remoto o conector personalizado e introduce tu URL de Braze MCP. Por ejemplo, en Claude puedes ir a **Settings** > **Connectors** > **Add custom connector** y pegar la URL.

No se requiere ID de cliente, secreto de cliente ni clave de API. Tu cliente se registra con Braze automáticamente.

Opciones de endpoint de Braze MCP:

- `https://mcp.braze.com/mcp` (US)
- `https://mcp.braze.eu/mcp` (EU)

{% alert tip %}
Los clientes de la UE deben usar el endpoint de la UE. Los clientes fuera de la UE pueden usar cualquiera de los dos endpoints.
{% endalert %}

Guías de configuración de clientes:

- [Claude](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [Claude Code](https://code.claude.com/docs/en/mcp-quickstart)
- [ChatGPT](https://developers.openai.com/api/docs/guides/developer-mode)
- [Cursor](https://cursor.com/docs/mcp#using-mcpjson)
- [OpenAI Codex](https://developers.openai.com/codex/mcp)
- [Visual Studio Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers)

### Paso 3: Inicia sesión en Braze a través de OAuth {#step-3-sign-in-to-braze-through-oauth}

La primera vez que tu agente llame a una herramienta de Braze, tu cliente abrirá una ventana del navegador y te dirigirá a Braze para iniciar sesión.

1. Inicia sesión en Braze como lo harías normalmente, incluyendo SSO si es necesario.
2. Si tu inicio de sesión puede acceder a más de una empresa en el mismo clúster, selecciona la empresa que deseas usar.
3. En la pantalla de consentimiento, revisa el acceso que la aplicación está solicitando.
4. Selecciona la casilla de verificación de aceptación para aceptar la Política de privacidad de Braze y luego selecciona **Continue** para volver a tu cliente MCP.

![La pantalla de consentimiento de Braze que muestra que Claude Desktop está solicitando acceso a la información de la cuenta de Braze y acceso amplio a los datos de Braze, con una casilla de verificación de aceptación de la Política de privacidad y los botones Cancel y Continue.]({% image_buster /assets/img/mcp_server/oauth_consent_screen.png %}){: style="max-width:65%;"}

Tu sesión utiliza tokens de acceso de corta duración que se actualizan automáticamente. Es posible que ocasionalmente necesites iniciar sesión de nuevo.

### Paso 4: Indica a tu agente qué espacio de trabajo usar {#step-4-tell-your-agent-which-workspace-to-use}

Si tu cuenta puede acceder a más de un espacio de trabajo, especifica el espacio de trabajo en tu prompt. Por ejemplo:

- `I'd like to look at campaign analytics for the past week in the Production workspace.`
- `Can you compare this week's analytics between my prod-1 workspace and my prod-2 workspace?`

Si no especificas un espacio de trabajo, tu agente puede pedirte que lo aclares.

### Paso 5: Envía un prompt de prueba {#step-5-send-a-test-prompt}

Después de la configuración, envía un prompt de validación rápido como:

- `List the Braze tools available in this workspace.`
- `Show my recent Canvases from the Production workspace.`

Para más ejemplos, consulta [Uso del servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

## Ejemplo: Conectar con Claude {#example-connect-with-claude}

Conectar un cliente solo requiere unos pocos pasos. El siguiente tutorial usa Claude, pero el flujo es similar para otros clientes compatibles.

1. En Claude, ve a **Settings** > **Connectors** > **Add custom connector**.
2. Introduce un nombre, como `Braze`, y luego pega tu URL de Braze MCP: `https://mcp.braze.com/mcp` para US o `https://mcp.braze.eu/mcp` para EU. No necesitas un ID de cliente, un secreto de cliente ni una clave de API.
3. Selecciona **Add** para guardar el conector. Claude se registra automáticamente con Braze.
4. Selecciona **Connect** para iniciar la autenticación. Claude abre una ventana del navegador y te redirige a Braze para iniciar sesión.
5. Inicia sesión en Braze con tus credenciales habituales, incluyendo SSO si tu empresa lo utiliza. Si tu inicio de sesión puede acceder a más de una empresa en el mismo clúster, selecciona la empresa que deseas usar.
6. En la pantalla de consentimiento, revisa el acceso solicitado, selecciona la casilla de verificación de reconocimiento y luego selecciona **Continue**. Claude regresa a tu chat y tu agente ya puede usar las herramientas de Braze.

Para confirmar la conexión, envía un mensaje de prueba como `Show my recent Canvases from the Production workspace`.

## Migración desde el servidor beta local {#migrating-from-the-local-beta-server}

Puedes ejecutar el servidor beta local y el servidor alojado de forma remota en paralelo durante la migración. Es posible que necesites indicar explícitamente a tu agente cuál utilizar.

El servidor alojado de forma remota incluye nuevas herramientas que no existen en el servidor beta local. Si creaste habilidades para el servidor local, es posible que necesites actualizar esas habilidades para hacer referencia a los nuevos nombres y comportamientos de las herramientas.

Después de confirmar que tus flujos de trabajo y habilidades funcionan en el servidor remoto, desactiva el servidor alojado localmente.

## Solución de problemas {#troubleshooting}

### La autenticación falla en un cliente compatible {#authentication-fails-in-a-supported-client}

1. Confirma que tu empresa está inscrita en el Acceso Anticipado.
2. Confirma que tu usuario tiene el permiso **Use MCP Server**.
3. Vuelve a intentar el inicio de sesión y la autorización.

### La autenticación está bloqueada en un cliente no verificado {#authentication-is-blocked-in-an-unverified-client}

Durante el Acceso Anticipado, Braze mantiene una lista de dominios de clientes compatibles permitidos por seguridad. Si te conectas desde un cliente que no está en la lista de permitidos, la autenticación puede bloquearse. Si crees que tu cliente debería ser compatible, contacta a [mcp-product@braze.com](mailto:mcp-product@braze.com).

Los clientes que se ejecutan localmente en tu máquina sin un esquema personalizado, como Claude Code y OpenAI Codex, también deberían funcionar.

### Las herramientas no aparecen en tu cliente {#tools-dont-appear-in-your-client}

Si tu agente no puede listar las herramientas de Braze, espera unos minutos e inténtalo de nuevo. Estos problemas suelen ser temporales y se resuelven por sí solos.

Si el problema continúa, graba un video y envíalo a [mcp-product@braze.com](mailto:mcp-product@braze.com) para su investigación.

### El agente no puede acceder a las herramientas esperadas {#agent-cannot-access-expected-tools}

1. Confirma que tu usuario del panel tiene los permisos necesarios. Tu agente solo puede usar herramientas que coincidan con tu propio acceso al panel.
2. Confirma que seleccionaste el espacio de trabajo esperado en tu prompt.
3. Pide a tu agente que llame a `get_workspaces` y verifica los ID de espacios de trabajo disponibles.

### El agente usa el espacio de trabajo incorrecto {#agent-uses-the-wrong-workspace}

Si tu cuenta puede acceder a más de un espacio de trabajo, nombra el espacio de trabajo en tu prompt usando el nombre exacto que se muestra en el panel de Braze. Si no especificas un espacio de trabajo, tu agente puede pedirte que aclares o usar uno inesperado.

{% alert important %}
Antes de que tu agente comience a trabajar, confirma siempre qué espacio de trabajo está usando. En algunos casos, un agente puede seleccionar un espacio de trabajo diferente al que pretendías.
{% endalert %}

### Cambiar a una empresa diferente {#switching-to-a-different-company}

Tu empresa se establece cuando autorizas por primera vez. Para trabajar en una empresa diferente en el mismo clúster, desconecta el conector de Braze en tu cliente, vuelve a autorizar y selecciona la otra empresa durante el inicio de sesión.

{% multi_lang_include mcp_server/legal_disclaimer.md %}