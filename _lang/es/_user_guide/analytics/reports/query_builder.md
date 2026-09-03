---
nav_title: Generador de consultas
article_title: Generador de consultas
page_order: 4
description: "Este artículo de referencia describe cómo crear informes utilizando datos de Braze desde Snowflake en el Generador de consultas."
tool: Reports
alias: /query_builder/
---

# Generador de consultas {#query-builder}

> El Generador de consultas genera informes utilizando datos de Braze en Snowflake. El Generador de consultas incluye [plantillas de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates) SQL predefinidas para que puedas empezar, o puedes escribir tus propias consultas SQL personalizadas para obtener aún más información.

Dado que el Generador de consultas permite el acceso directo a algunos datos de clientes, solo puedes acceder al Generador de consultas si tienes el [permiso]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) "Ver PII".

## Tablas de datos disponibles {#available-data-tables}

El Generador de consultas utiliza las mismas tablas SQL de Snowflake que las [extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) y [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). Para obtener una lista completa de las tablas disponibles y sus columnas, consulta la [referencia de tablas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables).

### Vistas de atributos de perfil de usuario {#user-profile-attribute-views}

El Generador de consultas y las extensiones de segmento SQL incluyen la mayoría de las [vistas de atributos de perfil de usuario]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#user-profile-attribute-views), como instantáneas periódicas e historial de atributos predeterminados.

Dos vistas de atributos personalizados solo están disponibles a través de [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes):

- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`
- `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`

Braze excluye estas vistas del Generador de consultas y de las extensiones de segmento SQL porque son lentas de consultar a escala de espacio de trabajo y a menudo agotan el tiempo de espera. Usa `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` para instantáneas de atributos personalizados en el Generador de consultas. Si necesitas datos históricos o casi en tiempo real de atributos personalizados, consulta las vistas excluidas a través de Snowflake Data Sharing.

## Ejecutar informes en el Generador de consultas {#running-reports-in-the-query-builder}

Para ejecutar un informe del Generador de consultas:

1. Ve a **Analytics** > **Query Builder**.
2. Selecciona **Create SQL Query**. Si necesitas inspiración o ayuda para elaborar tu consulta, selecciona **Query Template** y elige una plantilla de la lista. De lo contrario, selecciona **SQL Editor** para ir directamente al editor.
3. Tu informe recibe automáticamente un nombre con la fecha y hora actuales. Pasa el cursor sobre el nombre y selecciona <i class="fas fa-pencil" alt="Editar"></i> para darle a tu consulta SQL un nombre significativo.
4. Escribe tu consulta SQL en el editor u [obtén ayuda de la IA](#ai-query-builder) desde la pestaña **AI Query Builder**. Si escribes tu propio SQL, consulta [Escribir consultas SQL personalizadas](#custom-sql) para conocer los requisitos y recursos.
5. Selecciona **Run Query**.
6. Guarda tu consulta.
7. Para descargar un CSV de tu informe, selecciona **Export**.

![Generador de consultas mostrando los resultados de la consulta con plantilla "Participación del canal e ingresos de los últimos 30 días".]({% image_buster /assets/img_archive/query_builder.png %})

Los resultados de cada informe se pueden generar una vez al día. Si ejecutas el mismo informe más de una vez en un mismo día calendario, verás los mismos resultados en ambos informes.

### Plantillas de consultas {#query-templates}

Accede a las plantillas de consultas seleccionando **Create SQL Query** > **Query Template** al crear un informe por primera vez.

Consulta [Plantillas de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates) para ver una lista de las plantillas disponibles.

### Periodo de tiempo de los datos {#data-timeframe}

Las consultas devuelven datos de los últimos 60 días. Si usas Currents o [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake), es posible que puedas consultar hasta dos años de datos, que es el tiempo que se retienen tus datos en Snowflake. Para más detalles sobre la retención extendida de datos, contacta a tu CSM.

### Zona horaria del Generador de consultas {#query-builder-time-zone}

La zona horaria predeterminada para consultar nuestra base de datos de Snowflake es UTC. Como resultado, puede haber algunas discrepancias de datos entre tu página de **Email Channel Engagement** (que sigue la zona horaria de tu empresa) y los resultados de tu Generador de consultas.

Para convertir la zona horaria en los resultados de tu consulta, añade el siguiente SQL a tu consulta y personalízalo para la zona horaria de tu empresa:

{% raw %}
```sql
SELECT
DATE_TRUNC(
'day',
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME))
) AS send_date_sydney,
COUNT(ID) AS emails_sent
USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE
-- Apply the date range in Sydney time as well
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) >= '2025-03-25 00:00:00'
AND CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) < '2025-03-29 00:00:00'
AND APP_GROUP_ID = 'your app group ID'
GROUP BY
send_date_sydney
ORDER BY
send_date_sydney;
```
{% endraw %}

### Historial de consultas {#query-history}

La sección **Query history** en el Generador de consultas muestra tus consultas ejecutadas anteriormente para ayudarte a rastrear y reutilizar tu trabajo. El historial de consultas se retiene durante siete días, lo que significa que las consultas con más de siete días de antigüedad se eliminan automáticamente.

Si necesitas auditar el uso de consultas durante periodos más largos o mantener registros más allá de siete días, te recomendamos exportar o guardar los resultados de consultas importantes antes de que expiren.

### Comparar el Generador de consultas con otras fuentes de informes {#comparing-query-builder-with-other-reporting-sources}

Los resultados del Generador de consultas pueden diferir de otras herramientas de informes porque utilizan diferentes orígenes de datos y métodos de procesamiento.

Por ejemplo, los recuentos de rebotes blandos en el Generador de consultas pueden ser más altos que en los informes de capacidad de entrega de SendGrid. El Generador de consultas cuenta todas las ocurrencias de rebotes blandos sin deduplicación. Si un usuario rebota de forma blanda varias veces antes de la entrega final (o después de reintentos prolongados), cada intento de rebote blando se cuenta. SendGrid Deliverability utiliza sus propios datos y lógica, sobre los cuales Braze no tiene visibilidad, por lo que los recuentos entre los dos informes pueden no coincidir.

Para más información sobre cómo se rastrean los rebotes blandos en diferentes fuentes de informes, consulta [Rebote blando]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#soft-bounce) en el glosario de análisis de correo electrónico.

## Generar SQL con el generador de consultas con IA {#generating-sql-with-the-ai-query-builder}

El generador de consultas con IA aprovecha [GPT](https://openai.com/gpt-4), con tecnología de OpenAI, para recomendar SQL para tu consulta.

![El generador de consultas SQL con IA.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

Para generar SQL con el generador de consultas con IA:

1. Después de crear un informe en el Generador de consultas, selecciona la pestaña **AI Query Builder**.
2. Escribe tu indicación o selecciona una indicación de ejemplo y selecciona **Generate** para traducir tu indicación a SQL.
3. Revisa el SQL generado para asegurarte de que es correcto y, a continuación, selecciona **Insert into Editor**.

### Consejos {#tips}

- Familiarízate con las tablas y columnas disponibles en la [referencia de tablas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables). Solicitar datos que no existen en estas tablas puede hacer que ChatGPT invente una tabla ficticia.
- Familiarízate con las [reglas de escritura SQL]({{site.baseurl}}/user_guide/analytics/reports/query_builder#custom-sql) de esta característica. No seguir estas reglas provocará un error.
- Puedes enviar hasta 20 indicaciones por minuto con el generador de consultas con IA.

#{% multi_lang_include brazeai/generative_ai/policy.md %}

## Escritura de consultas SQL personalizadas {#custom-sql}

Escribe tu consulta SQL utilizando la [sintaxis de Snowflake](https://docs.snowflake.com/en/sql-reference). Consulta la [referencia de tablas]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) para obtener una lista completa de las tablas y columnas disponibles para consultar.

Para ver los detalles de las tablas dentro del Generador de consultas:

1. Desde la página del **Query Builder**, abre el panel **Reference** y selecciona **Available Data Tables** para ver las tablas de datos disponibles y sus nombres.
3. Selecciona <i class="fas fa-chevron-down" alt=""></i> **See Details** para ver la descripción de la tabla e información sobre las columnas de la tabla, como los tipos de datos.
4. Para insertar el nombre de la tabla en tu SQL, selecciona <i class="fas fa-copy" title="Copiar nombre de tabla al editor SQL"></i> **Copy table name to SQL editor**.

Para utilizar consultas preescritas proporcionadas por Braze, selecciona **Query Template** al crear un informe por primera vez en el Generador de consultas.

Restringir tu consulta a un periodo de tiempo específico te ayudará a generar resultados más rápido. El siguiente es un ejemplo de consulta que obtiene el número de compras y los ingresos generados en la última hora.

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

Esta consulta recupera el número de envíos de correo electrónico en el último mes:

```sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

Si consultas `CANVAS_ID`, `CANVAS_VARIATION_API_ID` o `CAMPAIGN_ID`, sus columnas de nombre asociadas se incluirán automáticamente en la tabla de resultados. No necesitas incluirlas en la propia consulta `SELECT`.

| Nombre del ID | Columna de nombre asociada |
| --- | --- |
| `CANVAS_ID` | Canvas Name |
| `CANVAS_VARIATION_API_ID` | Canvas Variant Name |
| `CAMPAIGN_ID` | Campaign Name |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Escritura de consultas SQL personalizadas" }

Esta consulta recupera los tres ID y sus columnas de nombre asociadas con un máximo de 100 filas:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

### Rellenar automáticamente el nombre de la variante de campaña {#automatically-populate-the-campaign-variant-name}

Si deseas que el nombre de la variante de campaña se rellene automáticamente, incluye el nombre de columna `MESSAGE_VARIATION_API_ID` en tu consulta, como en este ejemplo:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID, MESSAGE_VARIATION_API_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

### Solución de problemas {#troubleshooting}

Tu consulta puede fallar por cualquiera de las siguientes razones:

- Errores de sintaxis en tu consulta SQL
- Tiempo de espera de procesamiento agotado (después de 6 minutos)
    - Los informes que tardan más de 6 minutos en ejecutarse agotarán el tiempo de espera.
    - Si un informe agota el tiempo de espera, intenta limitar el rango de tiempo en el que consultas los datos o consulta un conjunto de datos más específico.

## Uso de variables {#using-variables}

Usa variables para utilizar tipos de variables predefinidos en SQL y hacer referencia a valores sin necesidad de copiar manualmente el valor. Por ejemplo, en lugar de copiar manualmente el ID de una campaña en el editor SQL, puedes usar {% raw %}`{{campaign.${My campaign}}}`{% endraw %} para seleccionar directamente una campaña desde un desplegable en la pestaña **Variables**.

Después de crear una variable, aparecerá en la pestaña **Variables** de tu informe del Generador de consultas. Los beneficios de usar variables SQL incluyen:

{% multi_lang_include analytics/sql_variables_benefits.md %}

### Directrices {#guidelines}

Las variables deben seguir la siguiente sintaxis de Liquid: {% raw %}`{{ type.${name}}}`{% endraw %}, donde `type` debe ser uno de los tipos aceptados y `name` puede ser cualquier nombre que elijas. Las etiquetas de estas variables se establecen de forma predeterminada con el nombre de la variable.

De forma predeterminada, todas las variables son obligatorias (y tu informe no se ejecutará a menos que se seleccionen valores de variables), excepto el rango de fechas, que se establece de forma predeterminada en los últimos 30 días cuando no se proporciona un valor.

### Tipos de variables {#variable-types}

Se aceptan los siguientes tipos de variables:

- [Número](#number)
- [Rango de fechas](#date-range)
- [Mensajería](#messaging)
- [Productos](#products)
- [Eventos personalizados](#custom-events)
- [Propiedades de eventos personalizados](#custom-event-properties)
- [Espacio de trabajo](#workspace)
- [Catálogos](#catalogs)
- [Campos de catálogo](#catalog-fields)
- [Opciones](#options)
- [Segments](#segments)
- [Cadena](#string)
- [Etiquetas](#tags)

#### Número {#number}

- **Valor de reemplazo:** El valor proporcionado, como `5.5`
- **Ejemplo de uso:** {% raw %}`some_number_column < {{number.${some name}}}`{% endraw %}

#### Rango de fechas {#date-range}

Si usas tanto `start_date` como `end_date`, deben tener el mismo nombre para que puedas usarlos como un rango de fechas.

##### Valores de ejemplo {#example-values}

El tipo de rango de fechas puede ser relativo, fecha de inicio, fecha de fin o rango de fechas.

Los cuatro tipos se muestran si se usan tanto `start_date` como `end_date` con el mismo nombre. Si solo se usa uno, entonces solo se mostrarán los tipos relevantes.

| Tipo de rango de fechas | Descripción | Valores requeridos |
| --- | --- | --- |
| Relativo | Especifica los últimos X días | Requiere `start_date` |
| Fecha de inicio | Especifica una fecha de inicio | Requiere `start_date` |
| Fecha de fin | Especifica una fecha de fin | Requiere `end_date` |
| Rango de fechas | Especifica tanto una fecha de inicio como una de fin | Requiere tanto `start_date` como `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Valores de ejemplo" }

- **Valor de reemplazo:** Reemplaza `start_date` y `end_date` con una marca de tiempo Unix en segundos para una fecha especificada en UTC, como `1696517353`.
- **Ejemplo de uso:** Para todas las variables de tipo relativo, fecha de inicio, fecha de fin y rango de fechas:
    - {% raw %}`time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}` {% endraw %}
        - Puedes usar `start_date` o `end_date` si no necesitas un rango de fechas.

#### Mensajería {#messaging}

Todas las variables de mensajería deben compartir el mismo identificador cuando quieras vincular su estado en un grupo.

##### Canvas {#canvas}

Para seleccionar un Canvas. Compartir el mismo nombre con una Campaign dará como resultado un botón de opción en la pestaña **Variables** para seleccionar Canvas o Campaign.

- **Valor de reemplazo:** ID BSON de Canvas
- **Ejemplo de uso:** {% raw %}`canvas_id = '{{canvas.${some name}}}'`{% endraw %}

##### Canvas (múltiples) {#canvases}

Para seleccionar múltiples Canvas. Compartir el mismo nombre con una Campaign dará como resultado un botón de opción en la pestaña **Variables** para seleccionar Canvas o Campaign.

- **Valor de reemplazo:** IDs BSON de Canvas
- **Ejemplo de uso:** {% raw %}`canvas_id IN ({{canvases.${some name}}})`{% endraw %}

##### Campaign {#campaign}

Para seleccionar una Campaign. Compartir el mismo nombre con un Canvas dará como resultado un botón de opción en la pestaña **Variables** para seleccionar Canvas o Campaign.

- **Valor de reemplazo:** ID BSON de Campaign
- **Ejemplo de uso:** {% raw %}`campaign_id = '{{campaign.${some name}}}'`{% endraw %}

##### Campaigns {#campaigns}

Para seleccionar múltiples Campaigns. Compartir el mismo nombre con un Canvas dará como resultado un botón de opción en la pestaña **Variables** para seleccionar Canvas o Campaign.

- **Valor de reemplazo:** IDs BSON de Campaigns
- **Ejemplo de uso:** {% raw %}`campaign_id IN ({{campaigns.${some name}}})`{% endraw %}

##### Variantes de Campaign {#campaign-variants}

Para seleccionar variantes de Campaign que pertenezcan a la Campaign seleccionada. Debe usarse junto con una variable de Campaign o Campaigns.

- **Valor de reemplazo:** IDs de API de variantes de Campaign, cadenas delimitadas por comas como `api-id1, api-id2`.
- **Ejemplo de uso:** {% raw %}`message_variation_api_id IN ({{campaign_variants.${some name}}})`{% endraw %}

##### Variantes de Canvas {#canvas-variants}

Para seleccionar variantes de Canvas que pertenezcan a un Canvas elegido. Debe usarse con una variable de Canvas o Canvas (múltiples).

- **Valor de reemplazo:** IDs de API de variantes de Canvas, cadenas delimitadas por comas como `api-id1, api-id2`.
- **Ejemplo de uso:** {% raw %}`canvas_variation_api_id IN ({{canvas_variants.${some name}}})`{% endraw %}

##### Paso en Canvas {#canvas-step}

Para seleccionar un paso en Canvas que pertenezca a un Canvas elegido. Debe usarse con una variable de Canvas.

- **Valor de reemplazo:** ID de API del paso en Canvas
- **Ejemplo de uso:** {% raw %}`canvas_step_api_id = '{{canvas_step.${some name}}}'`{% endraw %}

##### Pasos en Canvas {#canvas-steps}

Para seleccionar pasos en Canvas que pertenezcan a los Canvas elegidos. Debe usarse con una variable de Canvas o Canvas (múltiples).

- **Valor de reemplazo:** IDs de API de pasos en Canvas
- **Ejemplo de uso:** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}