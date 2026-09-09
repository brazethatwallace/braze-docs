# Extensiones de segmentos SQL {#sql-segment-extensions}

> Puedes generar una extensión de segmento utilizando consultas SQL de Snowflake sobre datos de [Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). SQL puede ayudarte a desbloquear nuevos casos de uso de segmentos, ya que ofrece la flexibilidad necesaria para describir las relaciones entre los datos de formas que no son posibles con otras características de segmentación.
>
> Al igual que las extensiones de segmento estándar, puedes consultar eventos de hasta los dos últimos años (730 días) en tu extensión de segmento SQL. A diferencia de las extensiones de segmento estándar, las extensiones de segmento SQL [consumen créditos](#credits).

## Requisitos previos {#prerequisites}

Dado que es posible acceder a datos PII a través de esta característica, debes tener permisos de PII para ejecutar consultas SQL de segmento.

## Crear una extensión de segmento {#creating-a-segment-extension}

### Paso 1: Elige un editor {#step-1-choose-an-editor}

Hay dos tipos de editores SQL entre los que puedes elegir al crear tu extensión de segmento SQL: el editor SQL y el editor SQL incremental.

- **Actualización completa:** Cada vez que tu segmento se actualiza, Braze consultará todos los datos disponibles para actualizar tu segmento, lo que consumirá más créditos que las actualizaciones incrementales. Las extensiones de actualización completa pueden regenerar automáticamente la membresía diariamente, pero no pueden actualizarse mediante actualización incremental.
- **Actualización incremental:** La actualización incremental es una forma más eficiente en costos de configurar tu consulta, aunque la configuración implica algunos [pasos](#step-2-write-your-sql) adicionales. Si puedes completar estos pasos adicionales al construir tu segmento, vale la pena elegir esta opción porque tu consulta se ejecutará utilizando menos créditos.
- **Generador de SQL con IA:** El generador de SQL con IA te permite escribir un prompt en lenguaje natural y lo convierte en una consulta SQL para tu segmento. Es una forma rápida de empezar sin necesidad de escribir el SQL tú mismo.

{% alert tip %}
Puedes realizar una actualización completa manual en todos los Segments SQL creados en cualquiera de los editores SQL.
{% endalert %}

{% tabs local %}
{% tab Actualización completa %}

Para crear una extensión de segmento SQL con actualización completa:

1. Ve a **Audiencia** > **Extensiones de segmento**.
2. Selecciona **Crear nueva extensión** y luego selecciona **Actualización completa**.<br><br>
   ![Modal para crear nueva extensión con opciones de actualización completa y actualización incremental.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Añade un nombre para tu extensión de segmento e introduce tu SQL. Consulta el [paso 2](#step-2-write-your-sql) para requisitos y recursos.<br><br>
   ![Editor SQL mostrando un ejemplo de extensión de segmento SQL.]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. Guarda tu extensión de segmento.

{% endtab %}
{% tab Actualización incremental %}

Para crear una extensión de segmento SQL con actualización incremental:

1. Ve a **Audiencia** > **Extensiones de segmento**.
2. Selecciona **Crear nueva extensión** y selecciona **Actualización incremental**.<br><br>
   ![Modal para crear nueva extensión con opciones de actualización completa y actualización incremental.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Añade un nombre para tu extensión de segmento e introduce tu SQL. Consulta la sección [Escribir SQL](#writing-sql) para requisitos y recursos.<br><br>
   ![Editor SQL mostrando un ejemplo de extensión de segmento SQL incremental.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4. Si lo deseas, selecciona **Regenerar extensión diariamente**.<br><br>
   ![Casilla de verificación para regenerar la extensión diariamente.]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   Cuando se selecciona, Braze actualizará automáticamente la membresía del segmento cada día. Esto significa que cada día a medianoche en la zona horaria de tu empresa (con un posible retraso de una hora), Braze verificará si hay nuevos usuarios en tu segmento y los añadirá automáticamente a tu segmento. Si una extensión de segmento no se ha utilizado en 7 días, Braze pausará automáticamente la regeneración diaria. Una extensión de segmento no utilizada es aquella que no forma parte de una Campaign o Canvas (la Campaign o el Canvas no necesitan estar activos para que la extensión se considere "utilizada").<br><br>
5. Guarda tu extensión de segmento.

{% endtab %}

{% tab Generador de SQL con IA %}

{% alert note %}
El generador de SQL con IA está disponible actualmente como característica en fase beta. Contacta con tu administrador de éxito de cliente si te interesa participar en esta prueba beta.
{% endalert %}

El generador de SQL con IA aprovecha [GPT](https://openai.com/gpt-4), de OpenAI, para recomendar SQL para tu segmento SQL.

![Generador de SQL con IA con el prompt "Usuarios que recibieron una notificación el mes pasado"]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

Para usar el generador de SQL con IA, haz lo siguiente:

1. Selecciona **Iniciar generador de SQL con IA** después de crear un [segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) utilizando actualización completa o incremental.
2. Escribe tu prompt y selecciona **Generar** para traducir tu prompt a SQL.
3. Revisa el SQL generado para asegurarte de que es correcto y luego guarda tu segmento.

#### Ejemplos de prompts {#example-prompts}

- Usuarios que recibieron un correo electrónico en el último mes
- Usuarios que realizaron menos de cinco compras en el último año

#### Consejos {#tips}

- Familiarízate con las [tablas de datos de Snowflake]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) disponibles. Solicitar datos que no existan en estas tablas puede hacer que ChatGPT invente una tabla falsa.
- Familiarízate con las [reglas de escritura SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql) para esta característica. No seguir estas reglas provocará un error. Por ejemplo, tu código SQL debe seleccionar la columna `user_id`. Comenzar tu prompt con "usuarios que" puede ayudar.
- Puedes enviar hasta 20 prompts por minuto con el generador de SQL con IA.

##{% multi_lang_include brazeai/generative_ai/policy.md %}

{% endtab %}
{% endtabs %}

{% alert note %}
Las consultas SQL que tarden más de 20 minutos en ejecutarse se agotarán por tiempo de espera.
{% endalert %}

Cuando la extensión termine de procesarse, puedes [crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment) usando tu extensión de segmento y dirigir este nuevo segmento con tus Campaigns y Canvas.

### Paso 2: Escribe tu SQL {#step-2-write-your-sql}

Tu consulta SQL debe escribirse utilizando la [sintaxis de Snowflake](https://docs.snowflake.com/en/sql-reference.html). Consulta la [referencia de tablas]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) para una lista completa de tablas y columnas disponibles para consultar.

{% alert important %}
Ten en cuenta que las tablas disponibles para consultar solo contienen datos de eventos. Si deseas consultar atributos de usuario, debes combinar tu segmento SQL con filtros de atributos personalizados del [segmentador clásico]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).
{% endalert %}

{% tabs %}
{% tab Editor SQL %}

Tu SQL también debe cumplir las siguientes reglas:

- Escribe una única sentencia SQL. No incluyas punto y coma.
- Tu SQL debe seleccionar solo una columna: la columna `user_id`. Esto significa que tu SQL debe contener:

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- No es posible consultar usuarios con cero eventos, lo que significa que cualquier consulta para usuarios que hayan realizado un evento menos de X veces debe seguir esta solución alternativa:
   1. Escribe una consulta para seleccionar usuarios que tengan el evento MÁS de X veces.
   2. Al hacer referencia a tu extensión de segmento en tu segmento, selecciona `doesn't include` para invertir el resultado.

#### Reglas adicionales {#additional-rules}

Además, tu consulta SQL estándar debe cumplir las siguientes reglas:

- No puedes usar sentencias `DECLARE`.
{% endtab %}
{% tab Editor SQL incremental %}

Todas las consultas de actualización incremental constan de dos partes: una consulta y detalles del esquema.

1. En el editor, escribe una consulta que seleccione `user_id` de la tabla deseada.
2. Añade detalles del esquema seleccionando un **Operador**, **Número de veces** y **Período de tiempo** en los campos de la parte superior del editor. La consulta verifica si la suma de la columna agregada cumple la condición que estableciste con esos campos. Esto funciona de manera similar al flujo de trabajo para crear extensiones de segmento clásicas.<br><br>
   - **Operador:** Indica si el evento ha ocurrido más de, menos de o igual a un número de ocurrencias.<br>
   ![Campo de operador con "Más de" seleccionado.]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **Número de veces:** Cuántas veces deseas evaluar el evento en relación con el operador.<br>
   ![Número de veces con "5" ingresado.]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **Período de tiempo:** Número de días de 1 a 730 en los que deseas verificar instancias del evento. Este período de tiempo se refiere a días pasados en relación con el día actual. El siguiente ejemplo muestra la consulta de usuarios que realizaron el evento más de 5 veces en los últimos 365 días.<br>
   ![Campo de período de tiempo con "365" ingresado.]({% image_buster /assets/img_archive/sql_segments_period.png %})

En el siguiente ejemplo, el segmento resultante contendría usuarios que realizaron el evento `favorited` más de 3 veces durante los últimos 30 días, después de una fecha especificada.

![Editor SQL mostrando un ejemplo de extensión de segmento SQL incremental.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![Vista previa SQL de una extensión de segmento SQL incremental.]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

{% alert tip %}
La actualización incremental tiene en cuenta los eventos tardíos: eventos que llegan después de la ventana de actualización diaria, como eventos del SDK que no se enviaron cuando se capturaron. Cuando el segmento se actualiza, Braze reprocesa las fechas a las que pertenecen esos eventos tardíos.
{% endalert %}

#### Cómo la actualización incremental rastrea usuarios a lo largo del tiempo {#how-incremental-refresh-tracks-users-over-time}

Cuando usas la actualización incremental, Braze almacena conteos diarios para cada usuario en una tabla interna de conteos para poder evaluar tu segmento durante todo tu período de tiempo sin volver a consultar todos los datos históricos cada día.

**Qué se almacena:** Braze mantiene una tabla de conteos (similar a una tabla de cohortes de segmentos) que acumula conteos diarios de cualificación de usuarios en el formato `(date, user_id, count)`. Esta tabla conserva datos históricos fuera de la ventana de actualización continua de dos días.

**Qué sucede en cada actualización:** Cuando se ejecuta una actualización incremental, Braze borra solo los registros de la ventana de actualización continua de dos días de la tabla de conteos. Luego vuelve a ejecutar tu consulta SQL con parámetros de tiempo actualizados (usando `$start_date`) para insertar filas nuevas para esas fechas. Las filas históricas fuera de la ventana de actualización continua de dos días permanecen intactas en la tabla de conteos.

**Cómo Braze decide quién está en el segmento:** Braze evalúa los criterios de membresía de tu segmento contra toda la tabla de conteos acumulada, no solo contra la carga útil más reciente de la ventana de actualización continua de dos días. Esto significa que los usuarios que se cualificaron hace más de dos días permanecen en el segmento a menos que los conteos agregados ya no cumplan tus criterios.

**Escritura de SQL que se actualice de forma fiable:** Al escribir SQL para actualización incremental, evita patrones de consulta que puedan producir resultados inconsistentes durante actualizaciones parciales. Por ejemplo, las agregaciones con ventana como `MAX(time)` que dependen de datos a través de los límites de `$start_date` pueden alterar el estado de las filas de forma inesperada cuando solo se recalcula un subconjunto de fechas. Estructura tus consultas de modo que la salida de cada fecha dependa únicamente de eventos de esa fecha, lo que mantiene resultados consistentes ya sea que la consulta procese dos días o 730 días de datos.

#### Reglas adicionales

Además, tu consulta de actualización incremental debe cumplir las siguientes reglas:

- Escribe una única sentencia SQL. No incluyas punto y coma.
- Tu segmento SQL incremental solo puede referirse a un evento. Tus menús desplegables de fecha y conteo se aplican a ese evento.
- Tu SQL debe incluir el alias `$date()` (por ejemplo, `$date(time)`), seleccionar `user_id` y una agregación `COUNT()`, agrupar por fecha y `user_id`, y filtrar con `$start_date` en tu columna de tiempo (por ejemplo, `time > $start_date`). Guardar SQL sin `$date()` o estos campos genera un error.
- No puedes usar sentencias `DECLARE`.
{% endtab %}
{% endtabs %}

{% alert note %}
Si estás creando un segmento SQL que usa la tabla `CATALOGS_ITEMS_SHARED`, debes especificar un ID de catálogo. Por ejemplo:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### Paso 3: Previsualiza la consulta {#step-3-preview-the-query}

Antes de guardar, puedes ejecutar una vista previa de tu consulta. Las vistas previas de consultas están limitadas automáticamente a 100 filas y se agotarán por tiempo de espera después de 60 segundos. El requisito de la columna `user_id` no se aplica al ejecutar una vista previa.

Para extensiones de segmento SQL incrementales, la vista previa no incluirá los criterios adicionales de tus campos de operador, número de veces y período de tiempo.

### Paso 4: Determina si necesitas invertir SQL {#step-4-determine-if-you-need-to-invert-sql}

A continuación, determina si necesitas invertir SQL. Si bien no es posible consultar directamente usuarios con cero eventos, puedes usar **Invertir SQL** para dirigirte a estos usuarios.

{% alert note %}
De forma predeterminada, **Invertir SQL** no está activado. Sin embargo, si usas el generador de SQL con IA para generar una sentencia SQL que necesite ser negada, ChatGPT podría devolver un resultado que active automáticamente esta característica.
{% endalert %}

Por ejemplo, para dirigirte a usuarios que tienen menos de tres compras, primero escribe una consulta para seleccionar usuarios que tengan tres o más compras. Luego, selecciona **Invertir SQL** para dirigirte a usuarios con menos de tres compras (incluyendo aquellos con cero compras).

{% alert important %}
A menos que estés buscando específicamente dirigirte a usuarios con cero eventos, no necesitarás invertir SQL. Si **Invertir SQL** está seleccionado, confirma que la característica es necesaria y que el segmento coincide con la audiencia deseada. Por ejemplo, si una consulta se dirige a usuarios con al menos un evento, solo se dirigirá a usuarios con cero eventos cuando esté invertida.
{% endalert %}

![Extensión de segmento denominada "Hicieron clic en 1-4 correos electrónicos en los últimos 30 días" con la opción de invertir SQL seleccionada.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:90%;"}

## Actualización de la membresía de segmento {#refreshing-segment-membership}

Para actualizar la membresía de segmento de cualquier extensión de segmento creada mediante SQL, abre la extensión de segmento y selecciona **Actualizar**.

{% alert tip %}
Si creaste un segmento en el que esperas que los usuarios entren y salgan con regularidad, actualiza manualmente la extensión de segmento que utiliza antes de segmentar ese segmento en una Campaign o Canvas.
{% endalert %}

## Gestión de las extensiones de segmento {#managing-your-segment-extensions}

En la página **Extensiones de segmento**, los segmentos generados con SQL se indican con <i class="fas fa-code" alt="Extensión de segmento SQL"></i> junto a su nombre.

Selecciona una extensión de segmento SQL para ver dónde se está utilizando la extensión, archivarla o [actualizar manualmente la membresía del segmento](#refreshing-segment-membership).

![Sección de uso de mensajería del editor SQL que muestra dónde se está utilizando el segmento SQL.]({% image_buster /assets/img_archive/sql_segments_usage.png %}){: style="max-width:70%;"}

### Designar la configuración de actualización {#designating-refresh-settings}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

## Créditos de Snowflake {#credits}

Cada espacio de trabajo de Braze dispone de 5 créditos de Snowflake al mes. Si necesitas más créditos, ponte en contacto con tu director de cuentas. Los créditos se utilizan cada vez que actualizas, o guardas y actualizas, la membresía de un segmento SQL. Los créditos no se utilizan cuando ejecutas vistas previas dentro de un segmento SQL o guardas o actualizas una extensión de segmento clásica.

{% alert note %}
Los créditos de Snowflake no se comparten entre características. Por ejemplo, los créditos de las extensiones de segmento SQL y del Generador de consultas son independientes entre sí.
{% endalert %}

El uso de créditos está correlacionado con el tiempo de ejecución de tu consulta SQL. Cuanto mayor sea el tiempo de ejecución, más créditos costará una consulta. El tiempo de ejecución puede variar en función de la complejidad y el tamaño de tus consultas a lo largo del tiempo. Cuanto más complejas y frecuentes sean las consultas que ejecutes, mayor será la asignación de recursos y más rápido será el tiempo de ejecución.

Para ahorrar créditos, previsualiza tu consulta para asegurarte de que es correcta antes de guardar la extensión de segmento SQL.

Tus créditos se restablecerán a 5 el primer día de cada mes a las 12 am UTC. Puedes monitorizar el uso de tus créditos a lo largo del mes en el panel de uso de créditos. Desde la página **Extensiones de segmento**, haz clic en <i class="fa-solid fa-chart-column"></i> **Ver uso de créditos SQL**.

![Panel de uso de créditos SQL en la página de extensiones de segmento SQL]({% image_buster /assets/img_archive/sql_segments_credits.png %}){: style="max-width:60%"}

Cuando tus créditos lleguen a cero, ocurrirá lo siguiente:

- Todas las extensiones de segmento SQL configuradas para actualizarse automáticamente dejarán de actualizarse, lo que afectará a la membresía de estos segmentos y a cualquier Campaign o Canvas que se dirija a estos segmentos.
- Solo podrás guardar nuevas extensiones de segmento SQL como borradores durante el resto del mes.

Todos los usuarios de la empresa que hayan creado un segmento SQL y los administradores de la empresa recibirán una notificación por correo electrónico cuando se haya utilizado el 50 %, el 80 % y el 100 % de los créditos. Después de que tus créditos se restablezcan al inicio del mes siguiente, podrás crear más segmentos SQL y se reanudarán las actualizaciones automáticas.

Si deseas adquirir más créditos de segmento SQL o extensiones de segmento adicionales, ponte en contacto con tu director de cuentas.