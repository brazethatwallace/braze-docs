> Aprende a utilizar el Generador de consultas, para que puedas generar informes utilizando datos de Braze en Snowflake. El Generador de consultas incluye [plantillas de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates) SQL predefinidas para empezar, o puedes escribir tus propias consultas SQL personalizadas para obtener aún más información.

## Requisitos previos {#prerequisites}

Necesitarás [permisos de "Ver PII"]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para usar el Generador de consultas, ya que permite el acceso directo a algunos datos de clientes.

## Uso del Generador de consultas {#using-the-query-builder}

### Paso 1: Crear una consulta SQL {#step-1-create-an-sql-query}

Para crear una nueva consulta, ve a **Analytics** > **Query Builder** y selecciona **Create SQL Query**.

![Las opciones "Query Template" y "SQL Editor" que se encuentran en el menú desplegable "Create SQL Query".]({% image_buster /assets/img_archive/create_sql_query_button.png %}){: style="max-width:60%;"}

Si necesitas inspiración o ayuda para elaborar tu consulta, elige **Query Template** y selecciona una [plantilla prediseñada]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates). Para comenzar con una consulta en blanco, selecciona **SQL Editor**.

Tu informe recibe automáticamente un nombre con la fecha y hora actuales. Pasa el cursor sobre el nombre y selecciona <i class="fas fa-pencil" alt="Editar"></i> para darle a tu consulta SQL un nombre significativo.

![Un ejemplo de nombre de informe "Channel engagement for May 2025".]({% image_buster /assets/img_archive/report_name_example.png %}){: style="max-width:80%;"}

### Paso 2: Construir tu consulta {#step-2-build-your-query}

Al construir tu consulta, puedes elegir obtener ayuda de la IA o hacerlo por tu cuenta.

{% tabs local %}
{% tab Usando BrazeAI %}
El Generador de consultas con IA aprovecha [GPT](https://openai.com/gpt-4), impulsado por OpenAI, para recomendar SQL para tu consulta. Para generar SQL con el Generador de consultas con IA:

1. Después de crear un informe en el Generador de consultas, selecciona la pestaña **AI Query Builder**.
2. Escribe tu indicación o selecciona una indicación de ejemplo y selecciona **Generate** para traducir tu indicación a SQL.
3. Revisa el SQL generado para asegurarte de que se ve correcto y luego selecciona **Insert into Editor**.

![El generador de consultas SQL con IA.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

#### Consejos {#tips}

- Familiarízate con las [tablas de datos de Snowflake]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) disponibles. Solicitar datos que no existen en estas tablas puede hacer que ChatGPT invente una tabla falsa.
- Familiarízate con las [reglas de escritura SQL]({{site.baseurl}}/user_guide/data_and_analytics/query_builder#custom-sql) para esta característica. No seguir estas reglas provocará un error.
- Puedes enviar hasta 20 indicaciones por minuto con el Generador de consultas con IA.

##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}

{% tab Por mi cuenta %}
Escribe tu consulta SQL usando la [sintaxis de Snowflake](https://docs.snowflake.com/en/sql-reference). Consulta la [referencia de tablas]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) para obtener una lista completa de tablas y columnas disponibles para consultar.

Para ver los detalles de las tablas dentro del Generador de consultas:

1. Desde la página del **Generador de consultas**, abre el panel **Reference** y selecciona **Available Data Tables** para ver las tablas de datos disponibles y sus nombres.
3. Selecciona <i class="fas fa-chevron-down" alt=""></i> **See Details** para ver la descripción de la tabla e información sobre las columnas de la tabla, como los tipos de datos.
4. Para insertar el nombre de la tabla en tu SQL, selecciona <i class="fas fa-copy" title="Copiar nombre de tabla al editor SQL"></i>.

Restringir tu consulta a un período de tiempo específico te ayudará a generar resultados más rápido. El siguiente es un ejemplo de consulta que obtiene el número de compras y los ingresos generados en la última hora.

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

Esta consulta obtiene el número de envíos de correo electrónico en el último mes:

```sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

Si consultas por `CANVAS_ID`, `CANVAS_VARIATION_API_ID` o `CAMPAIGN_ID`, sus columnas de nombre asociadas se incluirán automáticamente en la tabla de resultados. No necesitas incluirlas en la propia consulta `SELECT`.

| Nombre del ID | Columna de nombre asociada |
| --- | --- |
| `CANVAS_ID` | Canvas Name |
| `CANVAS_VARIATION_API_ID` | Canvas Variant Name |
| `CAMPAIGN_ID` | Campaign Name |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Consejos" }

Esta consulta obtiene los tres ID y sus columnas de nombre asociadas con un máximo de 100 filas:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

#### Solución de problemas {#troubleshooting}

Tu consulta puede fallar por cualquiera de las siguientes razones:

- Errores de sintaxis en tu consulta SQL
- Tiempo de espera de procesamiento agotado (después de 6 minutos)
    - Los informes que tardan más de 6 minutos en ejecutarse agotarán el tiempo de espera.
    - Si un informe agota el tiempo de espera, intenta limitar el rango de tiempo en el que estás consultando datos o consulta un conjunto de datos más específico.
{% endtab %}
{% endtabs %}

### Paso 3: Generar tu informe {#step-3-generate-your-report}

Cuando hayas terminado de construir tu consulta, selecciona **Run Query**. Si no hay errores ni [tiempos de espera de informe agotados](#report-timeouts), se generará un archivo CSV a partir de la consulta.

Para descargar el informe CSV, selecciona **Export**.

![Generador de consultas mostrando los resultados de la consulta basada en plantilla "Channel engagement and revenue for the last 30 days".]({% image_buster /assets/img_archive/query_builder.png %})

{% alert important %}
Cada informe solo puede generar resultados una vez al día. Si ejecutas el mismo informe varias veces en un solo día calendario, verás los mismos resultados en cada informe.
{% endalert %}

## Tiempos de espera en informes {#report-timeouts}

Los informes que tardan más de seis minutos en ejecutarse agotarán el tiempo de espera. Si es la primera consulta que ejecutas en un tiempo, puede tardar más en procesarse y, por lo tanto, tiene una mayor probabilidad de agotar el tiempo de espera. Si esto sucede, intenta ejecutar el informe de nuevo.

Si tu informe sigue agotando el tiempo de espera después de varios intentos, [contacta con Soporte]({{site.baseurl}}/help/support#braze-support).

## Consultar motivos de cancelación {#querying-abort-reasons}

Puedes consultar la columna `ABORT_TYPE` en cualquier tabla `USERS_MESSAGES_*_ABORT_SHARED` para analizar por qué no se enviaron los mensajes. El campo `ABORT_TYPE` contiene un valor de cadena que describe el motivo específico de la cancelación, y el campo complementario `ABORT_LOG` contiene detalles adicionales (como la regla de limitación de frecuencia que se activó).

Por ejemplo, para contar las cancelaciones de correo electrónico por tipo en los últimos 30 días:

```sql
SELECT ABORT_TYPE, COUNT(*) as abort_count
FROM USERS_MESSAGES_EMAIL_ABORT_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('day', -30, CURRENT_DATE())
GROUP BY ABORT_TYPE
ORDER BY abort_count DESC
```

Para ver la lista completa de valores de `ABORT_TYPE` y sus descripciones, consulta [Tipos de cancelación]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables#abort-types).

## Datos y resultados {#data-and-results}

Todas las consultas muestran datos de los últimos 60 días. Cuando exportas tus resultados, solo contendrán hasta 1000 filas. Para informes que requieran mayores cantidades de datos, puedes usar herramientas como [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) o el [endpoint de API de exportación]({{site.baseurl}}/api/endpoints/export).

## Créditos de Snowflake {#snowflake-credits}

Cada empresa tiene 5 créditos de Snowflake disponibles por mes, compartidos entre todos los espacios de trabajo. Se utiliza una pequeña porción de un crédito de Snowflake cada vez que ejecutas una consulta o previsualizas una tabla.

{% alert note %}
Los créditos de Snowflake no se comparten entre características. Por ejemplo, los créditos de las extensiones de segmento SQL y del Generador de consultas son independientes entre sí.
{% endalert %}

El uso de créditos está correlacionado con el tiempo de ejecución de tu consulta SQL. Cuanto mayor sea el tiempo de ejecución, mayor será la porción de un crédito de Snowflake que costará una consulta. El tiempo de ejecución puede variar dependiendo de la complejidad y el tamaño de tus consultas a lo largo del tiempo. Cuanto más complejas y frecuentes sean las consultas que ejecutes, mayor será tu asignación de recursos y más rápido será tu tiempo de ejecución.

Los créditos no se utilizan al escribir, editar o guardar informes dentro del editor SQL de Braze. Tus créditos se restablecerán a 5 el primer día de cada mes a las 12 am UTC. Puedes monitorear tu uso mensual de créditos en la parte superior de la página del Generador de consultas.

![El Generador de consultas mostrando la cantidad de créditos usados en el mes actual.]({% image_buster /assets/img_archive/query_builder_credits.png %}){: style="max-width:60%;"}

Cuando alcances el límite de créditos, no podrás ejecutar consultas, pero podrás crear, editar y guardar informes SQL. Si deseas comprar más créditos del Generador de consultas, ponte en contacto con tu director de cuentas.