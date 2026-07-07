# Extensiones de segmentos SQL {#sql-segment-extensions}

> Puedes generar una extensión de segmento utilizando consultas SQL de Snowflake sobre datos de [Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). SQL puede ayudarte a desbloquear nuevos casos de uso de segmentos, ya que ofrece la flexibilidad necesaria para describir las relaciones entre los datos de formas que no son posibles con otras características de segmentación.
>
> Al igual que las extensiones de segmento estándar, puedes consultar eventos de hasta los dos últimos años (730 días) en tu extensión de segmento SQL. A diferencia de las extensiones de segmento estándar, las extensiones de segmento SQL [consumen créditos](#credits).

## Requisitos previos {#prerequisites}

Dado que esta característica permite acceder a datos PII, debes disponer de permisos PII para ejecutar consultas de segmentos SQL.

## Crear una extensión de segmento {#creating-a-segment-extension}

### Paso 1: Elige un editor {#step-1-choose-an-editor}

Hay dos tipos de editores SQL entre los que puedes elegir para crear tu extensión de segmento SQL: el editor SQL y el editor SQL incremental.

- **Actualización completa:** Cada vez que tu segmento se actualice, Braze consultará todos los datos disponibles para actualizarlo, lo que consumirá más créditos que las actualizaciones incrementales. Las extensiones de actualización completa pueden regenerar automáticamente la membresía a diario, pero no pueden actualizarse mediante la actualización incremental.
- **Actualización incremental:** La actualización incremental es una forma más rentable de configurar tu consulta, aunque la configuración implica algunos [pasos](#step-2-write-your-sql) adicionales. Si puedes completar estos pasos adicionales al crear tu segmento, vale la pena elegir esta opción, ya que tu consulta se ejecutará utilizando menos créditos.
- **Generador SQL con IA:** El generador SQL con IA te permite escribir una indicación en lenguaje sencillo y la convierte en una consulta SQL para tu segmento. Es una forma rápida de empezar sin necesidad de escribir el código SQL tú mismo.

{% alert tip %}
Puedes realizar una actualización manual completa de todos los segmentos SQL creados en cualquiera de los dos editores SQL.
{% endalert %}

{% tabs local %}
{% tab Full refresh %}

Para crear una extensión de segmento SQL de actualización completa:

1. Ve a **Audiencia** > **Extensiones de segmento**.
2. Selecciona **Crear nueva extensión** y, a continuación, selecciona **Actualización completa**.<br><br>
   ![Modal de crear nueva extensión con las opciones de actualización completa y actualización incremental.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Añade un nombre para tu extensión de segmento e introduce tu SQL. Consulta el [paso 2](#step-2-write-your-sql) para conocer los requisitos y recursos necesarios.<br><br>
   ![Editor SQL que muestra un ejemplo de extensión de segmento SQL.]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. Guarda tu extensión de segmento.

{% endtab %}
{% tab Incremental refresh %}

Para crear una extensión de segmento SQL de actualización incremental:

1. Ve a **Audiencia** > **Extensiones de segmento**.
2. Selecciona **Crear nueva extensión** y selecciona **Actualización incremental**.<br><br>
   ![Modal de crear nueva extensión con las opciones de actualización completa y actualización incremental.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Añade un nombre para tu extensión de segmento e introduce tu SQL. Consulta la sección [Escribir SQL](#writing-sql) para conocer los requisitos y recursos.<br><br>
   ![Editor SQL que muestra un ejemplo de extensión incremental de segmento SQL.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4. Si lo deseas, selecciona **Regenerar extensión diariamente**.<br><br>
   ![Casilla para regenerar la extensión diariamente.]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   Si se selecciona esta opción, Braze actualizará automáticamente la membresía del segmento cada día. Esto significa que cada día a medianoche en la zona horaria de tu empresa (con un posible retraso de una hora), Braze comprobará si hay nuevos usuarios en tu segmento y los añadirá automáticamente. Si una extensión de segmento no se ha utilizado en 7 días, Braze pausará automáticamente la regeneración diaria. Una extensión de segmento no utilizada es aquella que no forma parte de una campaña o Canvas (la campaña o Canvas no necesita estar activa para que la extensión se considere «utilizada»).<br><br>
5. Guarda tu extensión de segmento.

{% endtab %}

{% tab AI SQL Generator %}

{% alert note %}
El generador SQL con IA está disponible actualmente como característica beta. Ponte en contacto con tu administrador del éxito del cliente si te interesa participar en esta prueba beta.
{% endalert %}

El generador SQL con IA aprovecha [GPT](https://openai.com/gpt-4), impulsado por OpenAI, para recomendar SQL para tu segmento SQL.

![Generador SQL con IA con la indicación «Usuarios que recibieron una notificación el mes pasado»]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

Para utilizar el generador SQL con IA, haz lo siguiente:

1. Selecciona **Lanzar generador SQL con IA** después de crear un [segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) utilizando la actualización completa o incremental.
2. Escribe tu indicación y selecciona **Generar** para traducirla a SQL.
3. Revisa el SQL generado para asegurarte de que es correcto y, a continuación, guarda tu segmento.

#### Ejemplos de indicaciones {#example-prompts}

- Usuarios que recibieron un correo electrónico en el último mes
- Usuarios que realizaron menos de cinco compras en el último año

#### Consejos {#tips}

- Familiarízate con las [tablas de datos de Snowflake]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables) disponibles. Pedir datos que no existen en estas tablas puede hacer que ChatGPT invente una tabla falsa.
- Familiarízate con las [reglas de escritura SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql) para esta característica. No seguir estas reglas provocará un error. Por ejemplo, tu código SQL debe seleccionar la columna `user_id`. Empezar tu indicación con «usuarios que» puede ayudar.
- Puedes enviar hasta 20 indicaciones por minuto con el generador SQL con IA.

##{% multi_lang_include brazeai/generative_ai/policy.md %}

{% endtab %}
{% endtabs %}

{% alert note %}
Las consultas SQL que tarden más de 20 minutos en ejecutarse agotarán el tiempo de espera.
{% endalert %}

Cuando la extensión termine de procesarse, puedes [crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment) utilizando tu extensión de segmento y dirigir este nuevo segmento con tus campañas y Canvas.

### Paso 2: Escribe tu SQL {#step-2-write-your-sql}

Tu consulta SQL debe escribirse utilizando [la sintaxis de Snowflake](https://docs.snowflake.com/en/sql-reference.html). Consulta la [referencia de tablas]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables) para obtener una lista completa de las tablas y columnas disponibles para consultar.

{% alert important %}
Ten en cuenta que las tablas disponibles para consultar solo contienen datos de eventos. Si deseas consultar atributos de usuario, deberás combinar tu segmento SQL con filtros de atributos personalizados del [segmentador clásico]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment).
{% endalert %}

{% tabs %}
{% tab SQL Editor %}

Además, tu SQL debe cumplir las siguientes reglas:

- Escribe una única sentencia SQL. No incluyas ningún punto y coma.
- Tu SQL debe seleccionar solo una columna: la columna `user_id`. Esto significa que tu SQL debe contener:

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- No es posible consultar usuarios con cero eventos, lo que significa que cualquier consulta de usuarios que hayan realizado un evento menos de X veces tendría que seguir esta solución alternativa:
   1. Escribe una consulta para seleccionar los usuarios que tienen el evento MÁS de X veces.
   2. Cuando hagas referencia a tu extensión de segmento en tu segmento, selecciona `doesn't include` para invertir el resultado.

#### Reglas adicionales {#additional-rules}

Además, tu consulta SQL estándar debe cumplir las siguientes reglas:

- No puedes utilizar sentencias `DECLARE`.
{% endtab %}
{% tab Incremental SQL Editor %}

Todas las consultas de actualización incremental constan de dos partes: una consulta y los detalles del esquema.

1. En el editor, escribe una consulta que seleccione `user_id`s de la tabla que desees.
2. Añade detalles del esquema seleccionando un **Operator**, **Number of times** y **Time period** en los campos situados encima del editor. La consulta comprobará si la suma de la columna agregada cumple una determinada condición especificada por los marcadores de posición {% raw %}`{{operator}}` y `{{number of times}}`{% endraw %}. Esto funciona de forma similar al flujo de trabajo para crear extensiones de segmento clásicas.<br><br>
   - **Operator:** Indica si el evento ha ocurrido más, menos o igual que un número de veces.<br>
   ![Campo del operador con «More than» seleccionado.]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **Number of times:** Cuántas veces quieres evaluar el evento en relación con el operador.<br>
   ![Número de veces con «5» introducido.]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **Time period:** Número de días de 1 a 730 en los que deseas comprobar las instancias del evento. Este periodo de tiempo se refiere a días pasados en relación con el día actual. El siguiente ejemplo muestra la consulta de usuarios que realizaron el evento más de 5 veces en los últimos 365 días.<br>
   ![Campo de periodo de tiempo con «365» introducido.]({% image_buster /assets/img_archive/sql_segments_period.png %})

En el siguiente ejemplo, el segmento resultante contendría los usuarios que realizaron el evento `favorited` más de 3 veces durante los últimos 30 días, después de una fecha especificada.

![Editor SQL que muestra un ejemplo de extensión incremental de segmento SQL.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![Vista previa SQL de una extensión incremental de segmento SQL.]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

{% alert tip %}
Los segmentos de actualización incremental tienen en cuenta los eventos tardíos, que son eventos que ocurrieron hace más de 2 días (por ejemplo, eventos del SDK que no se enviaron en el momento en que se capturaron).
{% endalert %}

#### Reglas adicionales

Además, tu consulta de actualización incremental debe cumplir las siguientes reglas:

- Escribe una única sentencia SQL. No incluyas ningún punto y coma.
- Tu segmento SQL incremental solo puede hacer referencia a un único evento. Los desplegables de fecha y recuento hacen referencia al evento elegido.
- Tu SQL debe tener las siguientes columnas: `user_id`, `$start_date` y una función de agregación (como `COUNT`). Cualquier SQL guardado sin estos tres campos dará lugar a un error.
- No puedes utilizar sentencias `DECLARE`.
{% endtab %}
{% endtabs %}

{% alert note %}
Si estás creando un segmento SQL que utiliza la tabla `CATALOGS_ITEMS_SHARED`, debes especificar un ID de catálogo. Por ejemplo:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### Paso 3: Vista previa de la consulta {#step-3-preview-the-query}

Antes de guardar, puedes ejecutar una vista previa de tu consulta. Las vistas previas de consultas se limitan automáticamente a 100 filas y expiran a los 60 segundos. El requisito de la columna `user_id` no se aplica cuando se ejecuta una vista previa.

En el caso de las extensiones incrementales de segmentos SQL, la vista previa no incluirá los criterios adicionales de los campos operador, número de veces y periodo de tiempo.

### Paso 4: Determina si necesitas invertir SQL {#step-4-determine-if-you-need-to-invert-sql}

A continuación, determina si necesitas invertir SQL. Aunque no es posible consultar directamente usuarios con cero eventos, puedes utilizar **Invertir SQL** para dirigirte a estos usuarios.

{% alert note %}
De forma predeterminada, **Invertir SQL** no está activado. Sin embargo, si utilizas el generador SQL con IA para generar una sentencia SQL que necesita ser negada, ChatGPT podría devolver un resultado que active automáticamente esta característica.
{% endalert %}

Por ejemplo, para dirigirte a usuarios que hayan realizado menos de tres compras, primero escribe una consulta para seleccionar a los usuarios que hayan realizado tres o más compras. A continuación, selecciona **Invertir SQL** para dirigirte a los usuarios con menos de tres compras (incluidos aquellos con cero compras).

{% alert important %}
A menos que tu objetivo específico sea dirigirte a usuarios sin eventos, no necesitarás invertir SQL. Si **Invertir SQL** está seleccionado, confirma que la característica es necesaria y que el segmento coincide con la audiencia deseada. Por ejemplo, si una consulta se dirige a usuarios con al menos un evento, solo se dirigirá a usuarios con cero eventos cuando se invierta.
{% endalert %}

![Extensión de segmento denominada «Clicked 1-4 emails in the last 30 days» con la opción de invertir SQL seleccionada.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:90%;"}

## Actualizar la membresía de segmentos {#refreshing-segment-membership}

Para actualizar la membresía de cualquier extensión de segmento creada mediante SQL, abre la extensión de segmento y selecciona **Actualizar**.

{% alert tip %}
Si has creado un segmento en el que esperas que los usuarios entren y salgan con regularidad, actualiza manualmente la extensión de segmento que utiliza antes de dirigirte a ese segmento en una campaña o Canvas.
{% endalert %}

## Gestionar tus extensiones de segmento {#managing-your-segment-extensions}

En la página **Extensiones de segmento**, los segmentos generados mediante SQL se indican con <i class="fas fa-code" alt="Extensión de segmento SQL"></i> junto a su nombre.

Selecciona una extensión de segmento SQL para ver dónde se está utilizando la extensión, archivar la extensión o [actualizar manualmente la membresía del segmento](#refreshing-segment-membership).

![Sección de uso de mensajería del editor SQL que muestra dónde se está utilizando el segmento SQL.]({% image_buster /assets/img_archive/sql_segments_usage.png %}){: style="max-width:70%;"}

### Configurar los ajustes de actualización {#designating-refresh-settings}

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

- Todas las extensiones de segmento SQL configuradas para actualizarse automáticamente dejarán de actualizarse, lo que afectará a la membresía de estos segmentos y a cualquier campaña o Canvas que se dirija a estos segmentos.
- Solo podrás guardar nuevas extensiones de segmento SQL como borradores durante el resto del mes.

Todos los usuarios de la empresa que hayan creado un segmento SQL y los administradores de la empresa recibirán una notificación por correo electrónico cuando se haya utilizado el 50 %, el 80 % y el 100 % de los créditos. Después de que tus créditos se restablezcan al inicio del mes siguiente, podrás crear más segmentos SQL y se reanudarán las actualizaciones automáticas.

Si deseas adquirir más créditos de segmento SQL o extensiones de segmento adicionales, ponte en contacto con tu director de cuentas.