---
nav_title: "Caso de uso: Atributos personalizados anidados"
article_title: "Caso de uso: Segmentar con atributos personalizados anidados"
page_order: 10
page_type: tutorial
tool: Segments
description: "Crea segmentos usando atributos personalizados anidados: el filtro de atributos personalizados anidados, rutas y comparadores, filtros de tiempo, segmentación multicriterio, generación de esquemas y el explorador de objetos anidados."
---

# Caso de uso: Segmentar con atributos personalizados anidados {#use-case-segment-with-nested-custom-attributes}

> Estos casos de uso muestran cómo segmentar usuarios con atributos personalizados anidados en Braze, e incluyen ejemplos de JSON y flujos de trabajo del dashboard que puedes adaptar a tus propios datos.

Supongamos que formas parte de un equipo de marketing de una aplicación de streaming de música y quieres enviar mensajes basados en los atributos personalizados anidados de un usuario, como objetos de cuenta con saldos y tipos. Estos casos de uso demuestran diversas formas en que tu equipo puede usar atributos personalizados anidados en segmentos, y te enseñan a:

- Configurar un filtro de segmento con atributos personalizados anidados, validar rutas y elegir comparadores que coincidan con el tipo de datos de cada propiedad.
- Saber cuándo usar los operadores **Day of Year** frente a **Time** para valores de fecha anidados, y cómo la **segmentación multicriterio** coincide con usuarios cuando al menos un objeto en una matriz cumple todos los criterios listados.
- Generar un esquema para un objeto o una matriz de objetos, explorarlo en el dashboard y completar un segmento (por ejemplo, usuarios con saldo inferior a 100) usando el SELECTOR de rutas en lugar de escribir las rutas de memoria.

## Filtrar por atributos personalizados anidados {#filter-by-nested-custom-attributes}

Vamos a crear un Segment basado en un atributo personalizado anidado para dirigirnos a los usuarios que reprodujeron su canción más escuchada más de 300 veces.

### Paso 1: Añadir el filtro {#step-1-add-the-filter}

Selecciona el filtro **Atributos personalizados anidados** para mostrar un menú desplegable desde el que puedes seleccionar un atributo personalizado anidado específico. Seleccionaremos `most_played_song`, que contiene datos sobre la canción más escuchada de un usuario.

### Paso 2: Seleccionar la propiedad {#step-2-select-the-property}

Selecciona la **propiedad** dentro del atributo personalizado anidado por la que quieres filtrar. Seleccionaremos `play_analytics.count`, que registra cuántas veces un usuario reprodujo su canción más escuchada.

### Paso 3: Seleccionar una comparación y un valor de atributo personalizado anidado {#step-3-select-a-comparison-and-nested-custom-attribute-value}

Al filtrar por atributos personalizados anidados, el tipo de datos de tu propiedad determina los comparadores por los que puedes filtrar. Por ejemplo, como `play_analytics.count` es un número, puedes seleccionar un comparador en la categoría **Número**.

Para filtrar por usuarios que reprodujeron su canción más escuchada al menos 300 veces, selecciona la comparación **Más que** y luego introduce "300" como valor.

![Un usuario eligiendo un operador basado en el tipo de datos del atributo personalizado anidado]({% image_buster /assets/img_archive/nca_comparator.png %})

## Filtrar por tipos de datos de tiempo {#filter-for-time-data-types}

Al filtrar un atributo personalizado anidado de tipo tiempo, puedes elegir filtrar con operadores de las categorías **Día del año** o **Tiempo** al comparar el valor de fecha.

Si seleccionas un operador de la categoría **Día del año**, solo se comparan el mes y el día en lugar de la marca de tiempo completa del valor del atributo personalizado anidado. Seleccionar un operador de la categoría **Tiempo** compara la marca de tiempo completa, incluido el año.

{% alert note %}
Al usar operadores de **Tiempo** que admiten unidades de días y semanas (como **es más de**, **es menos de**, **exactamente** y **después de**), Braze convierte automáticamente el valor a semanas cuando guardas el Segment. Por ejemplo, 91 días se convierten en 13 semanas. Tanto las unidades de días como de semanas son compatibles con estos filtros.
{% endalert %}

## Usa la segmentación multicriterio {#use-multi-criteria-segmentation}

Usa la **segmentación multicriterio** para crear un Segment que coincida con múltiples criterios dentro de un solo objeto. Esto cualifica al usuario en el Segment si tiene al menos un objeto en la matriz que coincida con todos los criterios especificados. Por ejemplo, los usuarios solo coinciden con este Segment si su clave no está en blanco y si su número es mayor que 0.

### Copiar Liquid para Segment {#copy-liquid-for-segment}

También puedes usar la característica **Copiar Liquid para Segment** para generar código Liquid para este Segment y usarlo en un mensaje. Por ejemplo, supongamos que tienes una matriz de objetos de cuenta y un Segment que se dirige a clientes con cuentas gravables activas. Para lograr que los clientes contribuyan al objetivo de cuenta asociado con una de sus cuentas activas y gravables, querrás crear un mensaje para motivarlos.

![Un ejemplo de Segment con la casilla de verificación seleccionada para la segmentación multicriterio.]({% image_buster /assets/img_archive/nca_multi_criteria.png %})

Cuando seleccionas **Copiar Liquid para Segment**, Braze genera automáticamente código Liquid que devuelve una matriz de objetos que solo contiene cuentas que están activas y son gravables.

{% raw %}

```
{% assign segmented_nested_objects = '' | split: '' %}
{% assign obj_array = {{custom_attribute.${accounts}}} %}
{% for obj in obj_array %}
  {% if obj["account_type"] == 'taxable' and obj["active"] == true %}
    {% assign segmented_nested_objects = obj_array | slice: forloop.index0 | concat: segmented_nested_objects | reverse %}
  {% endif %}
{% endfor %}
```

A partir de aquí, puedes usar `segmented_nested_objects` y personalizar tu mensaje. En este ejemplo, queremos tomar un objetivo de la primera cuenta gravable activa y personalizarlo:

```
Get to your {{segmented_nested_objects[0].goal}} goal faster, make a deposit using our new fast deposit feature!
```

{% endraw %}

Esto devuelve el siguiente mensaje a tu cliente: "Get to your retirement goal faster, make a deposit using our new fast deposit feature!"

## Generar un esquema usando el explorador de objetos anidados {#generate-schema}

Puedes generar un esquema para tus objetos y crear filtros de segmento sin necesidad de memorizar las rutas de objetos anidados.

### Paso 1: Generar un esquema {#step-1-generate-a-schema}

Por ejemplo, supongamos que tenemos una matriz de objetos `accounts` que acabamos de enviar a Braze:

```json
{"accounts": [
  {"type": "taxable",
  "balance": 22500,
  "active": true},
  {"type": "non-taxable",
  "balance": 0,
  "active": true}
]}
```

En el dashboard de Braze, ve a **Data Settings** > **Custom Attributes**.

Busca tu objeto o matriz de objetos. En la columna **Attribute Name**, selecciona **Generate Schema**.

![Una lista de atributos personalizados con la opción de generar el esquema para el atributo de cuentas.]({% image_buster /assets/img_archive/nca_generate_schema.png %})

{% alert tip %}
Puede tardar unos minutos en generarse tu esquema dependiendo de la cantidad de datos que nos hayas enviado.
{% endalert %}

Después de que se haya generado el esquema, aparece un nuevo botón <i class="fas fa-plus"></i> de más en lugar del botón **Generate Schema**. Puedes hacer clic en él para ver lo que Braze sabe sobre este atributo personalizado anidado.

Durante la generación del esquema, Braze examina los datos enviados anteriormente y construye una representación ideal de tus datos para este atributo. Braze también analiza y añade un tipo de datos para tus valores anidados. Esto se hace muestreando los datos enviados previamente a Braze para el atributo anidado dado.

Para nuestra matriz de objetos `accounts`, puedes ver que dentro de la matriz de objetos hay un objeto que contiene lo siguiente:

- Un tipo booleano con una clave de `active` (independientemente de si la cuenta está activa o no)
- Un tipo numérico con una clave de `balance` (monto del saldo en la cuenta)
- Un tipo cadena con una clave de `type` (cuenta no gravable o gravable)

![Esquema para la matriz de objetos de cuentas con tres valores anidados: active, balance y type.]({% image_buster /assets/img_archive/nca_schema.png %}){: style="max-width:70%" }

Ahora que hemos analizado y construido una representación de los datos, vamos a crear un segmento.

### Paso 2: Crear un segmento {#step-2-build-a-segment}

Vamos a dirigirnos a clientes que tienen un saldo inferior a 100 para poder enviarles un mensaje motivándolos a hacer un depósito.

Crea un segmento y añade el filtro `Nested Custom Attribute`, luego busca y selecciona tu objeto o matriz de objetos. Aquí hemos añadido la matriz de objetos `accounts`.

![Filtrado de atributos personalizados anidados para la matriz de objetos de cuentas.]({% image_buster /assets/img_archive/nca_segment_schema.png %})

Selecciona el botón <i class="fas fa-plus"></i> de más en el campo de ruta. Esto abre una representación de tu objeto o matriz de objetos. Puedes seleccionar cualquiera de los elementos listados y Braze los inserta en el campo de ruta por ti. En este ejemplo, necesitamos obtener el saldo. Selecciona el saldo como ruta (en este caso, `[].balance`) que se completa automáticamente en el campo de ruta.

![Esquema de cuentas con lista de rutas con búsqueda.]({% image_buster /assets/img_archive/nca_segment_schema2.png %}){: style="max-width:70%" }

Selecciona **less than** como comparador y luego introduce "100" como valor de saldo.

![Un filtro para usuarios con un saldo de cuenta inferior a 100.]({% image_buster /assets/img_archive/nca_segment_schema_3.png %})

¡Eso es todo! Acabas de crear un segmento usando un atributo personalizado anidado, todo sin necesidad de saber cómo están estructurados los datos. El explorador de objetos anidados en Braze generó una representación visual de tus datos y te permitió explorar y seleccionar exactamente lo que necesitabas para crear un segmento.