# Utiliza el servidor MCP de Braze {#using-the-braze-mcp-server}

> Aprende a interactuar con tus datos de Braze mediante lenguaje natural después de conectarte al servidor MCP remoto de Braze. Para más información, consulta [Servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Requisitos previos {#prerequisites}

Antes de poder utilizar esta característica, necesitarás [configurar el servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Buenas prácticas {#best-practices}

Cuando utilices el servidor MCP de Braze a través de herramientas de lenguaje natural, ten en cuenta estos consejos:

- Confirma el espacio de trabajo en tu prompt, especialmente cuando tengas acceso a varios espacios de trabajo.
- Sé específico con los rangos de fechas y las métricas al solicitar análisis.
- Pide al agente que confirme qué herramientas utilizó al validar los resultados.
- Compara las recomendaciones de alto impacto con los datos de origen en el panel de Braze.

## Ejemplos de uso {#usage-examples}

Después de [configurar el servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, puedes interactuar con Braze a través de lenguaje natural. Aquí tienes algunos ejemplos para empezar.

### ¿A qué espacios de trabajo puedo acceder? {#which-workspaces-can-i-access}

{% tabs %}
{% tab Ejemplo de prompt %}

`Muéstrame mis espacios de trabajo de Braze disponibles y dime cuál usar para análisis de Campaigns en producción.`
{% endtab %}
{% tab Ejemplo de respuesta %}

Llamé a `get_workspaces` y encontré estos espacios de trabajo:

- `Marketing - Production` (`app_group_id`: `YOUR-APP-GROUP-ID-1`)
- `Marketing - Staging` (`app_group_id`: `YOUR-APP-GROUP-ID-2`)

Usa `Marketing - Production` para los prompts de análisis de Campaigns en producción.
{% endtab %}
{% endtabs %}

Para más información, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#workspaces){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#workspaces){% endif %}.

### Muéstrame el rendimiento de Campaigns de la última semana {#show-me-campaign-performance-for-last-week}

{% tabs %}
{% tab Ejemplo de prompt %}

`En el espacio de trabajo Marketing - Production, muéstrame el rendimiento de Campaigns de los últimos siete días, incluyendo envíos, aperturas, clics y las de mejor rendimiento.`
{% endtab %}
{% tab Ejemplo de respuesta %}

Usé `get_campaign_list` y `get_campaign_dataseries` para el espacio de trabajo y el rango de fechas solicitados.

Resumen:

- Total de envíos: `YOUR-TEST-SENDS`
- Total de aperturas: `YOUR-TEST-OPENS`
- Total de clics: `YOUR-TEST-CLICKS`
- Campaign con más aperturas: `YOUR-TEST-CAMPAIGN-NAME`

Puedo desglosar esto por Campaign, canal o día si lo necesitas.
{% endtab %}
{% endtabs %}

Para más información, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#campaigns){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#campaigns){% endif %}.

### Crear una plantilla de correo electrónico {#create-an-email-template}

{% tabs %}
{% tab Ejemplo de prompt %}

`En el espacio de trabajo Marketing - Production, crea una plantilla de correo electrónico de incorporación llamada "YOUR-TEST-TEMPLATE-NAME".`
{% endtab %}
{% tab Ejemplo de respuesta %}

Usé `create_email_template` y creé tu plantilla.

- **ID de plantilla:** `YOUR-TEST-TEMPLATE-ID-123`
- **Nombre de plantilla:** `YOUR-TEST-TEMPLATE-NAME`
- **Espacio de trabajo:** `Marketing - Production`
{% endtab %}
{% endtabs %}

Para más información, consulta [Funciones de API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}.

## Flujos de trabajo de ejemplo {#example-workflows}

Estos ejemplos combinan múltiples herramientas para completar una tarea de principio a fin.

### Informe en múltiples espacios de trabajo {#report-across-multiple-workspaces}

{% tabs %}
{% tab Ejemplo de indicación %}

`Get me an analytics report for the past week from my US Prod workspace and my EU Prod workspace, and compare total sends and open rates.`
{% endtab %}
{% tab Ejemplo de respuesta %}

Llamé a `get_workspaces` para confirmar el acceso y luego ejecuté `get_campaign_dataseries` para cada espacio de trabajo durante los últimos siete días.

- `US Prod`: `YOUR-TEST-SENDS` envíos, `YOUR-TEST-OPEN-RATE` tarifa abierta
- `EU Prod`: `YOUR-TEST-SENDS` envíos, `YOUR-TEST-OPEN-RATE` tarifa abierta

`US Prod` envió más mensajes esta semana, mientras que `EU Prod` tuvo la tarifa abierta más alta. Puedo desglosar cualquiera de los espacios de trabajo por Campaign o canal.
{% endtab %}
{% endtabs %}

### Copiar plantillas de staging a producción {#copy-templates-from-staging-to-production}

{% tabs %}
{% tab Ejemplo de indicación %}

`Copy the email templates from my Staging workspace to my Production workspace.`
{% endtab %}
{% tab Ejemplo de respuesta %}

Usé `get_email_templates` y `get_email_template_info` para leer las plantillas en `Staging`, y luego `create_email_template` para recrear cada una en `Production`.

- `YOUR-TEST-TEMPLATE-NAME-1`: creada en `Production` (`YOUR-TEST-TEMPLATE-ID-1`)
- `YOUR-TEST-TEMPLATE-NAME-2`: creada en `Production` (`YOUR-TEST-TEMPLATE-ID-2`)

Omití las plantillas del editor de arrastrar y soltar, que `get_email_template_info` no admite. Avísame si quieres que revise las plantillas copiadas.
{% endtab %}
{% endtabs %}

### Resumen semanal del estado de las Campaigns {#summarize-weekly-campaign-health}

{% tabs %}
{% tab Ejemplo de indicación %}

`Give me a weekly campaign health summary for the Production workspace.`
{% endtab %}
{% tab Ejemplo de respuesta %}

Usé `get_campaign_list` y `get_campaign_dataseries` para obtener los últimos siete días de actividad en `Production`.

- Envíos totales: `YOUR-TEST-SENDS`
- Tarifa abierta: `YOUR-TEST-OPEN-RATE`
- Tasa de clics: `YOUR-TEST-CLICK-RATE`
- Campaign principal por conversiones: `YOUR-TEST-CAMPAIGN-NAME`

Los envíos aumentaron semana tras semana. Puedo agregar un desglose por canal o señalar cualquier Campaign con participación en descenso.
{% endtab %}
{% endtabs %}

## Cómo funciona el servidor MCP remoto {#how-the-remote-mcp-server-works}

Cuando envías una solicitud, ocurren algunos pasos detrás de escena:

1. **Envías un prompt a tu cliente.** Escribes una solicitud en lenguaje natural, como pedir el rendimiento de Campaigns de la semana pasada.
2. **El modelo del cliente selecciona herramientas.** El modelo de IA de tu cliente interpreta tu solicitud y la traduce en una o más llamadas a herramientas de Braze, como `get_campaign_list` y `get_campaign_dataseries`.
3. **Braze ejecuta la llamada a la herramienta.** El servidor MCP remoto recibe cada llamada a la herramienta a través de tu sesión OAuth autenticada, aplica el espacio de trabajo que especificaste y la ejecuta contra el endpoint de la REST or transferencia de estado representacional API de Braze correspondiente.
4. **Braze devuelve el resultado.** El servidor envía los datos de vuelta a tu cliente, que los formatea y te los presenta.

Tu acceso es la intersección de dos cosas:

- **Los alcances otorgados cuando autorizaste la conexión**, como `mcp:tools`.
- **Tus propios permisos de usuario en el panel.** Si no puedes ver Campaigns en el panel, tu agente tampoco puede. Si puedes crear plantillas de correo electrónico, tu agente también puede. Un agente nunca puede exceder tu propio acceso.

El contexto del espacio de trabajo se pasa con cada solicitud en lugar de almacenarse en un archivo de configuración local, por lo que una sola conexión puede funcionar en todos los espacios de trabajo a los que tengas acceso autorizado.

{% multi_lang_include mcp_server/legal_disclaimer.md %}