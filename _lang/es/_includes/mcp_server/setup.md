# Configurar el servidor Braze MCP {#setting-up-the-braze-mcp-server}

> Aprende a configurar el servidor MCP de Braze para poder interactuar con tus datos de Braze utilizando herramientas de lenguaje natural como Claude y Cursor. Para obtener información más general, consulta [Servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Requisitos previos {#prerequisites}

Antes de empezar, necesitarás lo siguiente:

| Requisito previo | Descripción |
|--------------|-------------|
| Clave de API de Braze | Una clave de API de Braze con los permisos necesarios. Crearás una nueva clave cuando [configures tu servidor Braze MCP](#create-api-key). |
| Cliente MCP | [Claude](https://claude.ai/), [Cursor](https://cursor.com/) y [Google Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli) son oficialmente compatibles. Debes tener una cuenta en uno de estos clientes para poder utilizar el servidor Braze MCP. |
| Terminal | Una aplicación de terminal para que puedas ejecutar comandos e instalar herramientas. Utiliza tu aplicación de terminal preferida o la que venga preinstalada en tu computadora. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Configuración del servidor Braze MCP

### Paso 1: Instalar `uv` {#step-1-install-uv}

En primer lugar, instala `uv`&#8212;una [herramienta de línea de comandos de Astral](https://docs.astral.sh/uv/getting-started/installation/) para la administración de dependencias y el manejo de paquetes Python.

{% tabs local %}
{% tab MacOS and Linux %}
Abre tu aplicación de terminal, pega el siguiente comando y pulsa <kbd>Intro</kbd>.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

El resultado es similar al siguiente:

```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh

downloading uv 0.8.9 aarch64-apple-darwin
no checksums to verify
installing to /Users/Isaiah.Robinson/.local/bin
  uv
  uvx
everything's installed!
```
{% endtab %}

{% tab Windows %}
 Abre Windows PowerShell, pega el siguiente comando y pulsa <kbd>Intro</kbd>.

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

El resultado es similar al siguiente:

```powershell
PS C:\Users\YourUser> irm https://astral.sh/uv/install.ps1 | iex

Downloading uv 0.8.9 (x86_64-pc-windows-msvc)
no checksums to verify
installing to C:\Users\YourUser\.local\bin
  uv.exe
  uvx.exe
everything's installed!
```
{% endtab %}
{% endtabs %}

### Paso 2: Crear una clave de API {#create-api-key}

El servidor Braze MCP incluye puntos de conexión de solo lectura y de escritura. No devuelven datos de los perfiles de usuario de Braze. Los puntos de conexión de escritura permiten a los agentes crear o actualizar contenido en tu espacio de trabajo.

Para crear tu clave de API:

1. Ve a **Configuración** > **API e identificadores** > **Claves de API**.
2. Crea una nueva clave.
3. Asigna algunos o todos los permisos siguientes a tu clave.

{% alert important %}
Asigna únicamente los permisos que quieras que tu agente utilice. Para evitar que tu agente realice cambios en Braze, no incluyas ningún permiso de escritura al crear tu clave de API.
{% endalert %}

{% details Lista de permisos compatibles %}
#### Campaigns

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | `campaigns.data_series` |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | `campaigns.details` |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | `campaigns.list` |
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaigns" }

#### Canvas

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | `canvas.data_series` |
| [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | `canvas.data_summary` |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | `canvas.details` |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) | `canvas.list` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas" }

#### Catalogs

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | `catalogs.get` |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | `catalogs.get_items` |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | `catalogs.get_item` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Catalogs" }

#### Cloud Data Ingestion

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/) | `cdi.integration_list` |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/) | `cdi.integration_job_status` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cloud Data Ingestion" }

#### Content Blocks

Los permisos `content_blocks.create` y `content_blocks.update` son permisos de escritura. Añádelos solo si quieres que tu agente cree o actualice Content Blocks en tu espacio de trabajo.

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | `content_blocks.list` |
| [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | `content_blocks.info` |
| [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | `content_blocks.create` |
| [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | `content_blocks.update` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

#### Custom Attributes

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes/) | `custom_attributes.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom Attributes" }

#### Events

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | `events.list` |
| [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | `events.data_series` |
| [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data/) | `events.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Events" }

#### KPIs

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | `kpi.new_users.data_series` |
| [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) | `kpi.dau.data_series` |
| [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | `kpi.mau.data_series` |
| [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | `kpi.uninstalls.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="KPIs" }

#### Media Library

El permiso `media_library.create` es un permiso de escritura. Añádelo solo si quieres que tu agente cargue activos a tu biblioteca de medios.

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create/) | `media_library.create` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Media Library" }

#### Messages

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | `messages.schedule_broadcasts` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Messages" }

#### Preference Center

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | `preference_center.list` |
| [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) | `preference_center.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Preference Center" }

#### Purchases

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | `purchases.product_list` |
| [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | `purchases.revenue_series` |
| [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | `purchases.quantity_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Purchases" }

#### Segments

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | `segments.list` |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | `segments.data_series` |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | `segments.details` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segments" }

#### Sends

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sends" }

#### Sessions

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | `sessions.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sessions" }

#### SDK Authentication Keys

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys/) | `sdk_authentication.keys` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SDK Authentication Keys" }

#### Subscription

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | `subscription.status.get` |
| [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | `subscription.groups.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Subscription" }

#### Templates

Los permisos `templates.email.create` y `templates.email.update` son permisos de escritura. Añádelos solo si quieres que tu agente cree o actualice plantillas de correo electrónico en tu espacio de trabajo.

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | `templates.email.list` |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | `templates.email.info` |
| [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | `templates.email.create` |
| [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | `templates.email.update` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Templates" }
{% enddetails %}

{% alert warning %}
No reutilices una clave de API existente. Crea una específicamente para tu cliente MCP. Asigna únicamente los permisos que tu agente necesite. Los agentes pueden intentar utilizar cualquier permiso que les concedas, así que deja desactivados los permisos de escritura si no quieres que tu agente realice cambios en Braze.
{% endalert %}

### Paso 3: Obtén tu identificador y punto de conexión {#step-3-get-your-identifier-and-endpoint}

Cuando configures tu cliente MCP, necesitarás el identificador de tu clave de API y el punto de conexión REST de tu espacio de trabajo. Para obtener estos datos, vuelve a la página **Claves de API** en el dashboard&#8212;mantén esta página abierta para poder consultarla durante [el siguiente paso](#configure-client).

![La página «Claves de API» en Braze mostrando una clave de API recién creada y el punto de conexión REST del usuario.]({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### Paso 4: Configura tu cliente MCP {#configure-client}

Configura tu cliente MCP utilizando el archivo de configuración proporcionado previamente.

{% tabs %}
{% tab Claude %}
Configura tu servidor MCP utilizando el directorio de conectores de [Claude Desktop](https://claude.ai/download).

1. En Claude Desktop, ve a **Settings** > **Connectors** > **Browse Connectors** > **Desktop Extensions** > **Braze MCP Server** > **Install**.
2. Introduce tu clave de API y la URL base.
3. Guarda la configuración y reinicia Claude Desktop.

{% endtab %}

{% tab Cursor %}
En [Cursor](https://cursor.com/), ve a **Settings** > **Tools and Integrations** > **MCP Tools** > **Add Custom MCP** y, a continuación, añade el siguiente fragmento de código:

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "your-braze-api-key",
        "BRAZE_BASE_URL": "your-braze-endpoint-url"
      }
    }
  }
}
```

Reemplaza `key-identifier` y `rest-endpoint` con los valores correspondientes de la página **Claves de API** en Braze. Tu configuración debería ser similar a la siguiente:

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

Cuando hayas terminado, guarda la configuración y reinicia Cursor.
{% endtab %}
{% tab Gemini CLI %}
Gemini CLI lee la configuración del usuario desde `~/.gemini/settings.json`. Si no existe, puedes crearlo ejecutando lo siguiente en tu terminal:

```powershell
mkdir -p ~/.gemini
nano ~/.gemini/settings.json
```

A continuación, sustituye `yourname` por la cadena exacta que aparece antes de `@BZXXXXXXXX` en el indicador de tu terminal. Luego, sustituye `key-identifier` y `rest-endpoint` por los valores correspondientes de la página **Claves de API** en Braze.

Tu configuración debería ser similar a la siguiente:

```json
{
  "mcpServers": {
    "braze": {
      "command": "/Users/yourname/.local/bin/uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

Cuando hayas terminado, guarda la configuración y reinicia Gemini CLI. A continuación, en Gemini, ejecuta los siguientes comandos para verificar que el servidor Braze MCP aparece en la lista y que las herramientas y el esquema están disponibles para su uso:

```powershell
gemini
/mcp
/mcp desc
/mcp schema
```

Deberías ver el servidor `braze` en la lista con las herramientas y el esquema disponibles para su uso.

{% endtab %}
{% endtabs %}

### Paso 5: Enviar una solicitud de prueba {#step-5-send-a-test-prompt}

Después de configurar el servidor Braze MCP, intenta enviar una solicitud de prueba a tu cliente MCP. Para ver otros ejemplos y prácticas recomendadas, consulta [Uso del servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
**Solicitud de ejemplo:** `What are my available Braze functions?`
**Respuesta de ejemplo:** Se utilizó `list_functions` y se devolvieron las categorías de funciones disponibles del servidor Braze MCP.
{% endtab %}

{% tab Cursor %}
**Solicitud de ejemplo:** `What are my available Braze functions?`
**Respuesta de ejemplo:** Se consultó `list_functions` y se listaron funciones como `get_canvas_list`.
{% endtab %}

{% tab Gemini CLI %}
**Solicitud de ejemplo:** `What are my available Braze functions?`
**Respuesta de ejemplo:** Se consultó `list_functions` en Gemini CLI y se devolvieron las categorías de funciones disponibles del servidor Braze MCP junto con funciones de ejemplo.
{% endtab %}
{% endtabs %}

## Solución de problemas {#troubleshooting}

### Errores de terminal {#terminal-errors}

#### Comando `uvx` no encontrado {#uvx-command-not-found}

Si recibes un error que indica que no se encuentra el comando `uvx`, vuelve a instalar `uv` y reinicia tu terminal.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Error `spawn uvx ENOENT` {#spawn-uvx-enoent-error}

Si recibes un error `spawn uvx ENOENT`, es posible que necesites actualizar la ruta del archivo en el archivo de configuración de tu cliente. Primero, abre tu terminal y ejecuta el siguiente comando:

```bash
which uvx
```

El comando debería devolver un mensaje similar al siguiente:

```bash
/Users/alex-lee/.local/bin/uvx
```

Copia el mensaje en el portapapeles y abre [el archivo de configuración de tu cliente](#configure-client). Reemplaza `"command": "uvx"` con la ruta que copiaste y, a continuación, reinicia tu cliente. Por ejemplo:

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### Error en la instalación del paquete {#package-installation-fails}

Si la instalación del paquete falla, intenta instalar una versión específica de Python.

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### Configuración del cliente {#client-configuration}

#### «Esta extensión no es compatible con tu dispositivo» {#this-extension-is-not-compatible-with-your-device}

Si ves este error al instalar la extensión del servidor Braze MCP, puede indicar una de las siguientes situaciones:

- **Tu dispositivo no cumple los requisitos**: algunas extensiones de servidor MCP requieren versiones específicas del sistema operativo o hardware.
- **Faltan herramientas de desarrollo (solo macOS)**: en macOS, la instalación de la extensión requiere herramientas de desarrollo de línea de comandos para ejecutar comandos de Python. Si estas herramientas no están instaladas, la instalación fallará con este error.

Para instalar las herramientas de desarrollo de línea de comandos en macOS, ejecuta lo siguiente en tu terminal:

```bash
xcode-select --install
```

Una vez completada la instalación, reinicia tu cliente MCP e intenta instalar la extensión de nuevo.

#### El cliente MCP no puede encontrar el servidor Braze {#mcp-client-cant-find-the-braze-server}

1. Verifica que la sintaxis de configuración de tu cliente MCP sea correcta.
2. Reinicia tu cliente MCP después de realizar cambios en la configuración.
3. Comprueba que `uvx` está en el `PATH` de tu sistema.

#### Errores de autenticación {#authentication-errors}

1. Verifica que tu `BRAZE_API_KEY` sea correcto y esté activo.
2. Asegúrate de que `BRAZE_BASE_URL` coincida con tu instancia de Braze.
3. Comprueba que tu clave de API tiene los [permisos correctos](#create-api-key).

#### Tiempo de espera de conexión agotado o errores de red {#connection-timeouts-or-network-errors}

1. Verifica que tu `BRAZE_BASE_URL` sea correcto para tu instancia.
2. Comprueba tu conexión de red y la configuración del cortafuegos.
3. Asegúrate de utilizar HTTPS en tu URL base.

{% multi_lang_include mcp_server/legal_disclaimer.md %}