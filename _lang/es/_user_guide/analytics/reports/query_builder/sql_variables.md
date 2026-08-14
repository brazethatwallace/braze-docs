---
nav_title: Variables SQL
article_title: Variables SQL del Generador de consultas
page_order: 2
page_type: reference
description: "Aprende a usar variables en el Generador de consultas para reutilizar tus consultas y evitar codificar datos de forma fija en tu código."
tool: Reports
---

# Variables SQL del Generador de consultas {#query-builder-sql-variables}

> Aprende a usar variables SQL en el Generador de consultas para reutilizar tus consultas y evitar codificar datos de forma fija en tu código.

## ¿Por qué usar variables SQL? {#why-use-sql-variables}

Los beneficios de usar variables SQL incluyen:

{% multi_lang_include analytics/sql_variables_benefits.md %}

## Uso de variables {#using-variables}

### Paso 1: Añadir una variable {#step-1-add-a-variable}

Para añadir una variable a tu consulta, usa la siguiente sintaxis:

{% raw %}
```sql
{{variable_type.${custom_label}}}
```
{% endraw %}

Reemplaza lo siguiente:

| Marcador de posición | Descripción |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `variable_type`   | El tipo de variable predefinido que deseas usar, como `campaign` o `catalog_fields`. Para la lista completa, consulta [Tipos de variables compatibles](#variable-types). |
| `custom_label` | La etiqueta utilizada para identificar la variable en la pestaña **Variables** de tu Generador de consultas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 1: Añadir una variable" }

En el siguiente ejemplo, se consulta el número total de usuarios entre el primer y el último día de un mes para una Campaign. A cada variable se le asignará un valor en el siguiente paso.

{% raw %}
```sql
SELECT COUNT(*) AS total_users
FROM USERS_CAMPAIGNS_REVENUE_SHARED
WHERE campaign_id = '{{campaign.${Campaign}}}'
  AND TIME > '{{start_date.${Month First Day}}}'
  AND TIME < '{{end_date.${Month Last Day}}}';
```
{% endraw %}

### Paso 2: Asignar un valor {#step-2-assign-a-value}

De forma predeterminada, la pestaña **Variables** no se muestra en el Generador de consultas. Solo aparece después de añadir tu primera variable a la consulta. Allí podrás asignarle un valor. Los valores específicos que puedes elegir dependerán del [tipo](#variable-types) de esa variable en particular.

En el siguiente ejemplo, la Campaign "Summer Feature Launch" se asigna como valor, junto con el primer y último día de junio de 2025.

![La pestaña "Variables" en el Generador de consultas mostrando el ejemplo dado.]({% image_buster /assets/img/query_builder_example.png %})

## Tipos de variables generales {#variable-types}

### Número {#number}

`number` se puede usar en combinación con otras variables que no sean de cadena. Acepta cualquier número positivo o negativo, incluidos números decimales, como `5.5`.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
some_number_column < {{number.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Cadena {#string}

Para cambiar valores de cadena repetitivos entre ejecuciones de informes. Usa esta variable para evitar codificar de forma fija un valor varias veces en tu SQL.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
'{{string.${add a string here.}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Lista {#list}

Para seleccionar de una lista de opciones.

{% tabs local %}
{% tab elegir una %}
{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab elegir múltiples %}
{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Botón de radio {#radio-button}

Para mostrar opciones como botones de radio en lugar de un menú desplegable en la pestaña **Variables**. No se puede usar por sí solo&#8212;debe usarse en combinación con una [lista](#list).

{% tabs %}
{% tab uso %}
```sql
is_radio_button: 'true'
```
{% endtab %}
{% endtabs %}

![Un ejemplo de botón de radio renderizado en Braze.]({% image_buster /assets/img_archive/sql_variables_campaigns.png %}){: style="max-width:50%;"}

#### Selección múltiple {#multi-select}

Para determinar si el menú desplegable permite una selección única o múltiple. No se puede usar por sí solo&#8212;debe usarse en combinación con una [lista](#list).

{% tabs %}
{% tab uso %}
```sql
is_multi_select: 'true'
```
{% endtab %}
{% endtabs %}

![Un ejemplo de lista de selección múltiple renderizada en Braze.]({% image_buster /assets/img_archive/sql_variables_productname.png %}){: style="max-width:50%;"}

#### Opciones {#options}

Para proporcionar la lista de opciones seleccionables en forma de etiqueta y valor. La etiqueta es lo que se muestra y el valor es con lo que se reemplaza la variable cuando se selecciona la opción. No se puede usar por sí solo&#8212;debe usarse en combinación con una [lista](#list).

{% tabs %}
{% tab uso %}
```sql
options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'
```
{% endtab %}
{% endtabs %}

## Tipos de variables específicos de Braze {#braze-specific-variable-types}

### Rango de fechas {#date-range}

Para mostrar un calendario del cual seleccionar fechas. Reemplaza `start_date` y `end_date` con una marca de tiempo Unix en segundos para una fecha especificada en UTC, como `1696517353`. Opcionalmente, puedes establecer solo un `start_date` o `end_date` para mostrar solo una fecha única en el calendario. Si las etiquetas de tu `start_date` y `end_date` no coinciden, se tratarán como dos fechas separadas, en lugar de un rango de fechas.

{% tabs %}
{% tab uso %}
{% raw %}
```
time > {{start_date.${custom_label}}} AND time < {{end_date.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

Puedes establecer el rango de fechas en cualquiera de las siguientes opciones. Si se usan tanto `start_date` como `end_date` y comparten la misma etiqueta, se mostrarán todas las opciones. De lo contrario, si solo se usa uno, solo se mostrará la opción especificada.

| Opción | Descripción | Valores obligatorios |
| --- | --- | --- |
| Relativo | Especifica los últimos X días | Requiere `start_date` |
| Fecha de inicio | Especifica una fecha de inicio | Requiere `start_date` |
| Fecha de fin | Especifica una fecha de fin | Requiere `end_date` |
| Rango de fechas | Especifica tanto una fecha de inicio como de fin | Requiere tanto `start_date` como `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Rango de fechas" }

Tu Liquid se usará para mostrar un calendario dentro del rango de fechas dado:

![Un ejemplo de calendario renderizado en Braze.]({% image_buster /assets/img_archive/query_builder_time_range.png %}){: style="max-width:50%;"}

### Campaigns {#campaigns}

{% tabs local %}
{% tab una Campaign %}
Para seleccionar una Campaign. Compartir la misma etiqueta con un Canvas resultará en un botón de radio dentro de la pestaña **Variables** para seleccionar Canvas o Campaign.

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
campaign_id = '{{campaign.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab múltiples Campaigns %}
Para seleccionar múltiples Campaigns. Compartir la misma etiqueta con un Canvas resultará en un botón de radio dentro de la pestaña **Variables** para seleccionar Canvas o Campaign.

- **Valor de reemplazo:** ID BSON de Campaigns

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
campaign_id IN ({{campaigns.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab variantes de Campaign %}
Para seleccionar variantes de Campaign que pertenezcan a la Campaign seleccionada. Debe usarse junto con una variable de Campaign o Campaigns.

- **Valor de reemplazo:** ID de API de variantes de Campaign, cadenas delimitadas por comas como `api-id1, api-id2`.

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
message_variation_api_id IN ({{campaign_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
Todas las variables de Campaign y Canvas deben usar los mismos identificadores para sincronizar estados dentro de un solo grupo.
{% endalert %}

### Canvas {#canvases}

{% tabs local %}
{% tab un Canvas %}
Para seleccionar un Canvas. Compartir la misma etiqueta con una Campaign resultará en un botón de radio dentro de la pestaña **Variables** para seleccionar Canvas o Campaign.

- **Valor de reemplazo:** ID BSON de Canvas

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
canvas_id = '{{canvas.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab múltiples Canvas %}
Para seleccionar múltiples Canvas. Compartir la misma etiqueta con una Campaign resultará en un botón de radio dentro de la pestaña **Variables** para seleccionar Canvas o Campaign.

- **Valor de reemplazo:** ID BSON de Canvas

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
canvas_id IN ({{canvases.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab variantes de Canvas %}
Para seleccionar variantes de Canvas que pertenezcan a un Canvas elegido. Debe usarse con una variable de Canvas. Se establece en uno o más ID de API de variantes de Canvas, como una cadena separada por comas, como en `api-id1, api-id2`.

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
canvas_variation_api_id IN ({{canvas_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab un paso en Canvas %}
Para seleccionar un paso en Canvas que pertenezca a un Canvas elegido. Debe usarse con una variable de Canvas.

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
canvas_step_api_id = '{{canvas_step.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab múltiples pasos en Canvas %}
Para seleccionar pasos en Canvas que pertenezcan a los Canvas elegidos. Debe usarse con una variable de Canvas.

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
canvas_step_api_id IN ({{canvas_steps.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
Todas las variables de Campaign y Canvas deben usar los mismos identificadores para sincronizar estados dentro de un solo grupo.
{% endalert %}

### Productos {#products}

`products` se usa para seleccionar uno o más productos del panel de Braze.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
({{products.${custom_label}}})
```
{% endraw %}
{% endtab %}

{% tab ejemplo %}
{% raw %}
```sql
SELECT product_name
FROM FULL_GAME_AND_DLC
WHERE product_id IN ({{products.${Games with DLC}}});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Eventos personalizados {#custom-events}

Selecciona uno o más eventos personalizados o propiedades de eventos personalizados de una lista.

{% tabs local %}
{% tab evento %}
`custom_events` se usa para seleccionar uno o más eventos personalizados del panel de Braze.

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
'{{custom_events.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}

{% subtab ejemplo %}
{% raw %}
```sql
SELECT event_name
FROM CUSTOM_EVENTS_TABLE
WHERE event_name IN ({{custom_events.${Purchased Game}}});
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab propiedades %}
`custom_event_properties` se usa para seleccionar una o más propiedades del evento personalizado actualmente seleccionado. Requiere una variable `custom_events` establecida.

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
name = '{{custom_event_properties.${property names)}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Espacio de trabajo {#workspace}

`workspace` se usa para seleccionar un único espacio de trabajo del panel de Braze.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
workspace_id = '{{workspace.${app_group_id}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Catálogos {#catalogs}

Selecciona uno o más catálogos o campos de catálogo de una lista.

{% tabs local %}
{% tab catálogos %}
`catalogs` se usa para seleccionar uno o más catálogos del panel de Braze.

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
catalog_id = '{{catalogs.${catalog}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab campos de catálogo %}
`catalog_fields` se usa para establecer uno o más campos del catálogo actualmente seleccionado. Requiere una variable `catalogs` establecida.

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
field_name = '{{catalog_fields.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Segments {#segments}

Para seleccionar Segments que tengan activado el [seguimiento de análisis]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking). Se establece con el ID de análisis del Segment, que corresponde a los ID almacenados en la columna `user_segment_membership_ids` en las tablas donde esta columna está disponible.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
{{segments.${analytics_segments}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Etiquetas {#tags}

Para seleccionar etiquetas para Campaigns y Canvas. Se establece con Campaigns y Canvas con ID BSON separados por comas entre comillas simples que están asociados con las etiquetas seleccionadas.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
{{tags.${some tags}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Metadatos de variables {#variable-metadata}

Los metadatos se pueden adjuntar a una variable para cambiar su comportamiento añadiendo los metadatos con un carácter de barra vertical ( &#124; ) después de la etiqueta de la variable. El orden de los metadatos no importa y puedes añadir cualquier cantidad de ellos. Además, todos los tipos de metadatos se pueden usar para cualquier variable, excepto los metadatos especiales que son específicos de ciertas variables (esto se indicará en esos casos). El uso de todos los metadatos es opcional y se utiliza para cambiar el comportamiento predeterminado de la variable.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
{{string.${my var}| is_required: 'false' | description: 'My optional string var'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Booleano {#boolean}

Para saber si el valor de una variable está completado. Esto es útil para variables opcionales donde deseas cortocircuitar una condición si el valor de una variable no está completado. Se puede establecer en `true` o `false` dependiendo del valor de la otra variable.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

`type` y `name` se refieren a la variable referenciada. Por ejemplo, para cortocircuitar la siguiente variable opcional: {% raw %}`{{campaigns.${messaging}}`{% endraw %}:

{% raw %}
```sql
{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: 'false'}})
```
{% endraw %}

### Visible {#visible}

Para determinar si las variables son visibles. Todas las variables son visibles de forma predeterminada en la pestaña **Variables**, donde puedes ingresar valores.

Hay varias variables especiales cuyo valor depende de otra variable, como si otra variable tiene un valor. Estas variables especiales se marcan como no visibles para que no aparezcan en la pestaña **Variables**.

{% tabs %}
{% tab uso %}
```sql
visible: 'false'
```
{% endtab %}
{% endtabs %}

### Obligatoria {#required}

Para determinar si las variables son obligatorias de forma predeterminada. Un valor vacío para una variable generalmente conduce a una consulta incorrecta.

{% tabs %}
{% tab uso %}
```sql
required: 'false'
```
{% endtab %}
{% endtabs %}

### Orden {#order}

Para seleccionar la posición de la variable en la pestaña **Variables**.

{% tabs %}
{% tab uso %}
```sql
order: '1'
```
{% endtab %}
{% endtabs %}

### Incluir comillas {#include-quotes}

{% tabs local %}
{% tab comillas simples %}
Para rodear los valores de una variable con comillas simples.

{% subtabs %}
{% subtab uso %}
```sql
include_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab comillas dobles %}
Para rodear los valores de una variable con comillas dobles.

{% subtabs %}
{% subtab uso %}
```sql
include_double_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Marcador de posición {#placeholder}

Para especificar el texto del marcador de posición que se muestra en el campo de entrada de la variable.

{% tabs %}
{% tab uso %}
```sql
placeholder: 'enter some value'
```
{% endtab %}
{% endtabs %}

### Descripción {#description}

Para especificar el texto de descripción que se muestra debajo del campo de entrada de la variable.

{% tabs %}
{% tab uso %}
```sql
description: 'some description'
```
{% endtab %}
{% endtabs %}

### Valor predeterminado {#default-value}

Para especificar el valor predeterminado de la variable cuando no se especifica ningún valor.

{% tabs %}
{% tab uso %}
```sql
default_value: '5'
```
{% endtab %}
{% endtabs %}

### Ocultar etiqueta {#hide-label}

Para ocultar la etiqueta de la variable.

{% tabs %}
{% tab uso %}
```sql
hide_label: 'true'
```
{% endtab %}
{% endtabs %}