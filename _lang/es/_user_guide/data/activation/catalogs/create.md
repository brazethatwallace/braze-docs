---
nav_title: Crear un catálogo
article_title: Crear un catálogo
alias: "/catalogs/"
page_order: 1
description: "En este artículo de referencia se explica cómo crear catálogos que hagan referencia a datos de no usuarios en tus campañas de Braze a través de Liquid."
---

# Crear un catálogo {#create-a-catalog}

> La creación de un catálogo implica la importación a Braze de un archivo CSV de datos no relativos al usuario. Esto te permite acceder a esa información para enriquecer tus mensajes. Puedes introducir cualquier tipo de datos en un catálogo. Estos datos suelen ser algún tipo de metadatos de tu empresa, como información sobre productos para una empresa de comercio electrónico, o información sobre cursos para un proveedor de educación.

## Casos de uso {#use-cases}

Los casos de uso habituales de los catálogos incluyen:

- Productos
- Servicios
- Alimentación
- Próximos eventos
- Música
- Paquetes

Una vez importada esta información, puedes empezar a acceder a ella en los mensajes de forma similar a como accedes a los atributos personalizados o a las propiedades del evento personalizado a través de Liquid.

## Tipos de datos compatibles {#supported-data-types}

La siguiente tabla enumera los tipos de datos de catálogo compatibles y cómo se pueden crear o actualizar.

| Tipo de datos | Descripción | Disponible mediante carga CSV | Disponible mediante API y CDI |
|--------------|-----------------------------------------------|:------------------------:|:-------------------------:|
| Cadena | Una secuencia de caracteres. | ✅ Sí | ✅ Sí |
| Número | Un valor numérico, ya sea entero o decimal. | ✅ Sí | ✅ Sí |
| Booleano | Un valor `true` o `false`. | ✅ Sí | ✅ Sí |
| Hora | Una cadena con formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | ✅ Sí | ✅ Sí |
| Geolocalización | Una matriz de coordenadas `[longitude, latitude]`. La latitud debe estar entre -90 y 90; la longitud debe estar entre -180 y 180. Por ejemplo, `[-73.988103, 40.779109]`. | ✅ Sí | ✅ Sí |
| Objeto JSON | Un objeto anidado con pares clave-valor. Se puede mostrar en la plataforma, pero solo se puede crear o actualizar a través de la API o CDI. | ⛔ No | ✅ Sí |
| Matriz de cadenas | Una lista de cadenas. Se puede mostrar en la plataforma, pero solo se puede crear o actualizar a través de la API o CDI. Máximo de 100 elementos. | ⛔ No | ✅ Sí |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Crear un catálogo {#creating-a-catalog}

Para crear un catálogo, ve a **Configuración de datos** > **Catálogos**, selecciona **Crear nuevo catálogo** y elige una de las siguientes opciones:

{% tabs local %}
{% tab Upload CSV %}
### Paso 1: Revisa tu archivo CSV {#step-1-review-your-csv-file}

Antes de cargar tu archivo CSV, asegúrate de que cumple los siguientes requisitos:

| Requisito CSV | Detalles |
|-----------------|---------|
| Encabezados | La primera columna del archivo CSV debe llamarse `id`, y cada fila debe tener un valor `id` único. |
| Columnas | Un archivo CSV puede tener un máximo de 1000 campos (columnas) y cada nombre de columna puede tener hasta 250 caracteres. |
| Tamaño del archivo | En los planes gratuitos, el tamaño total de todos los archivos CSV de una empresa está limitado a 100 MB. Para los planes Pro, el tamaño máximo de un solo archivo CSV es de 2 GB. |
| Valores de campo | Cada celda (valor de campo) puede contener hasta 5000 caracteres. |
| Caracteres válidos | La columna `id` y todos los valores del encabezado solo pueden contener letras, números, guiones y guiones bajos. |
| Tipos de datos | Los tipos de datos compatibles para las cargas CSV incluyen cadenas, números, valores booleanos, horas y geolocalización. Para obtener la lista completa de tipos de datos, incluidos los que solo están disponibles a través de la API y CDI, consulta [Tipos de datos compatibles](#supported-data-types). |
| Formato | Formatea todo el texto en minúsculas para mantener la coherencia. |
| Codificación | Guarda y carga el archivo CSV utilizando la codificación UTF-8. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
¿Necesitas más espacio para tus archivos CSV? Ponte en contacto con tu director de cuentas de Braze para obtener más información sobre la actualización de tus catálogos.
{% endalert %}

### Paso 2: Cargar CSV {#step-2-upload-csv}

Arrastra y suelta tu archivo en la zona de carga, o selecciona **Upload CSV** y elige tu archivo.

![Arrastra y suelta tu archivo en la zona de carga, o selecciona Upload CSV y elige tu archivo.]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}

Selecciona un tipo de datos para cada columna.

{% alert note %}
Este tipo de datos no se puede editar una vez configurado el catálogo. Además, un valor `NULL` no es compatible con la carga de CSV y se tratará como una cadena.
{% endalert %}

![Selección de tipo de datos para cada columna del catálogo. Un valor NULL no es compatible con la carga de CSV y se tratará como una cadena.]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}

Introduce un nombre y una descripción opcional para tu catálogo. Ten en cuenta los siguientes requisitos al nombrar tu catálogo:

  - Debe ser único
  - 250 caracteres como máximo
  - Solo puede incluir números, letras, guiones y guiones bajos

{% alert tip %}
También puedes [utilizar plantillas en el nombre del catálogo](#template-catalog-names), lo que te permite generar dinámicamente nombres de catálogo basados en variables como el idioma o la campaña.
{% endalert %}

![Un catálogo llamado "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

Selecciona **Process Catalog** para crear el catálogo.

{% alert important %}
Tu archivo CSV puede ser rechazado si superas tu [nivel](#tiers).
{% endalert %}

### Tutorial: Creación de un catálogo a partir de un archivo CSV {#tutorial-creating-a-catalog-from-a-csv-file}

Para este tutorial, vamos a utilizar un catálogo que enumera dos juegos, su coste y un enlace de imagen.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg" aria-label="Tutorial: Creación de un catálogo a partir de un archivo CSV">
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">title</th>
    <th class="tg-0pky">price</th>
    <th class="tg-0pky">image_link</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">1234</td>
    <td class="tg-0pky">Tales</td>
    <td class="tg-0pky">7.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
  <tr>
    <td class="tg-0pky">1235</td>
    <td class="tg-0pky">Regeneration</td>
    <td class="tg-0pky">22.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
</tbody>
</table>

Crearemos el catálogo cargando un archivo CSV. Los tipos de datos de `id`, `title`, `price` y `image_link` son cadena, cadena, número y cadena, respectivamente.

{% alert note %}
Este tipo de datos no se puede editar una vez configurado el catálogo.
{% endalert %}

![Cuatro nombres de columna del catálogo: "id", "title", "price", "image_link".]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:85%;"}

A continuación, daremos a este catálogo el nombre "games_catalog" y seleccionaremos el botón **Process Catalog**. Braze comprobará si hay errores en el catálogo antes de crearlo.

![Un catálogo llamado "games_catalog".]({% image_buster /assets/img_archive/catalog_new_name.png %}){: style="max-width:85%;"}

Ten en cuenta que no podrás editar este nombre una vez creado el catálogo. Puedes eliminar un catálogo y volver a cargar una versión actualizada utilizando el mismo nombre de catálogo.

Una vez creado el catálogo, puedes empezar a hacer referencia al [catálogo en una campaña]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs).
{% endtab %}

{% tab Crear en el navegador %}
### Requisitos previos {#prerequisites}

Antes de poder editar o crear catálogos en el navegador, necesitas los siguientes [permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para tu espacio de trabajo:

- Ver catálogos
- Editar catálogos
- Exportar catálogos
- Eliminar catálogos

### Paso 1: Introduce los detalles del catálogo {#step-1-enter-catalog-details}

Introduce un nombre y una descripción opcional para tu catálogo. Ten en cuenta los siguientes requisitos al nombrar tu catálogo:

- Debe ser único
- 250 caracteres como máximo
- Solo puede incluir números, letras, guiones y guiones bajos

{% alert tip %}
También puedes [utilizar plantillas en el nombre del catálogo](#template-catalog-names), lo que te permite generar dinámicamente nombres de catálogo basados en variables como el idioma o la campaña.
{% endalert %}

![Un catálogo llamado "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

### Paso 2: Crea tu catálogo {#step-2-create-your-catalog}

Selecciona tu catálogo de la lista y, a continuación, selecciona **Update Catalog** > **Add fields**. Introduce el **Field name** y utiliza el menú desplegable para seleccionar el tipo de datos. Repite la operación según sea necesario.

![Dos campos de ejemplo "rating" y "name".]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}

Selecciona **Update Catalog** > **Add items** para añadir un elemento a tu catálogo introduciendo la información en función de los campos que hayas añadido previamente. A continuación, selecciona **Save Item** o **Save and Add Another** para seguir añadiendo tus elementos.

![Añadir un elemento al catálogo.]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

{% alert note %}
Braze procesa los valores de tiempo basándose en la marca de tiempo del panel. Por ejemplo, si una columna tiene el valor "03/13/2024" y tu zona horaria es la zona horaria del Pacífico, esta hora se importaría a Braze como "Mar 12, 2024, 5:00 PM".
{% endalert %}
{% endtab %}
{% endtabs %}

## Tipos de datos de catálogo {#catalog-data-types}

Los catálogos admiten varios tipos de datos para ayudarte a organizar y estructurar tus datos de forma eficaz. La siguiente tabla describe cada tipo de datos compatible y cómo se corresponde con los nombres de tipo en CSV y API:

| Tipo de datos | Formato | Ejemplo | Descripción |
|-----------|--------|---------|-------------|
| Cadena | Texto | `"Hello World"` | Cualquier secuencia de caracteres utilizada para datos de texto como nombres, descripciones e ID. Equivalente al tipo `string` en las importaciones CSV y API. |
| Hora | ISO 8601 o marca de tiempo Unix (segundos) | `"2024-03-15T14:30:00Z"` | Valores de fecha y hora con formato ISO 8601 o marca de tiempo Unix en segundos. Equivalente al tipo `time` en la API y al tipo `datetime` en las importaciones CSV. |
| Booleano | `true` o `false` | `true` | Valores lógicos que representan estados verdadero o falso. Equivalente al tipo `boolean` en las importaciones CSV y API. |
| Número | Entero o decimal | `42` o `19.99` | Valores numéricos que incluyen enteros y números de punto flotante para precios, cantidades, calificaciones y más. Equivalente a los tipos `integer` y `float` en las importaciones CSV y al tipo `number` en la API. |
| Geolocalización | Matriz `[longitude, latitude]` | `[-73.988103, 40.779109]` | Un par de coordenadas que representa una ubicación geográfica. La longitud debe estar entre -180 y 180; la latitud debe estar entre -90 y 90. El valor de `type` en la API es `geo`. Se puede añadir a través del panel **Add Fields** en la interfaz de catálogos, la carga CSV o la REST API. |
| Objeto | Objeto JSON | `{"key": "value", "price": 10}` | Estructuras de datos anidadas complejas. El valor de `type` en la API es `object`. Se muestra como objeto JSON en el panel. Solo disponible a través de la API o la ingesta de datos en la nube (CDI). |
| Matriz | Matriz de cadenas | `["red", "blue", "green"]` | Listas de valores de cadena. El valor de `type` en la API es `array`. Se muestra como matriz de cadenas en el panel. Solo disponible a través de la API o CDI. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## Uso de plantillas en los nombres de los catálogos {#template-catalog-names}

Al nombrar tu catálogo, también puedes utilizar plantillas en el nombre del catálogo. Esto te permite generar dinámicamente nombres de catálogos basados en variables como el idioma o la campaña. Por ejemplo, puedes utilizar lo siguiente:

{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

## Administración de catálogos {#managing-catalogs}

### En el panel {#in-the-dashboard}

Para actualizar tu catálogo después de cargar un archivo CSV o crear un catálogo en el navegador, selecciona **Update Catalog** > **Upload CSV** y, a continuación, selecciona si deseas actualizar, añadir o eliminar elementos de tu catálogo.

### Uso de la REST API {#using-the-rest-api}

A medida que crees más catálogos, también puedes utilizar el [endpoint Listar catálogos]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) para obtener una lista de los catálogos de un espacio de trabajo.

La REST API admite todos los [tipos de datos de catálogo](#supported-data-types), incluidos los objetos JSON y las matrices de cadenas. Los objetos JSON y las matrices de cadenas solo se pueden crear o actualizar a través de la REST API.

### Uso de la ingesta de datos en la nube {#using-cloud-data-ingestion}

Puedes mantener catálogos a través de la [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) sincronizando los datos del catálogo directamente desde tu almacén de datos (como Snowflake, Redshift, BigQuery, Databricks, Microsoft Fabric o S3) de forma programada.

## Gestión de los elementos del catálogo {#managing-catalog-items}

Además de gestionar tus catálogos, también puedes utilizar endpoints asíncronos y síncronos para gestionar los elementos del catálogo. Esto incluye la posibilidad de editar y eliminar elementos del catálogo, y de listar los detalles de los elementos del catálogo.

Por ejemplo, si quieres editar un elemento individual del catálogo, puedes utilizar el [endpoint `/catalogs/catalog_name/items/item_id`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item).

## Almacenamiento de catálogos {#tiers}

La versión gratuita de catálogos admite tamaños de archivo CSV de hasta 100 MB para todos los archivos CSV combinados de tu empresa, mientras que la versión Catalogs Pro admite tamaños de archivo CSV de hasta 2 GB para un único archivo CSV.

{% alert important %}
El derecho a paquete que se muestra en el panel de Braze se redondea a la unidad más próxima por motivos visuales; sin embargo, sigues teniendo derecho a la totalidad del derecho adquirido. Para solicitar una actualización del almacenamiento de catálogos, ponte en contacto con tu director de cuentas de Braze.
{% endalert %}

### Versión gratuita {#free-version}

El tamaño de almacenamiento para la versión gratuita de los catálogos es de hasta 100&nbsp;MB. Puedes tener un número ilimitado de elementos, siempre que no superen los 100&nbsp;MB.

#### Catalogs Pro {#catalogs-pro}

A nivel de empresa, el almacenamiento máximo para Catalogs Pro se basa en el tamaño de los datos del catálogo. Las opciones de tamaño de almacenamiento son: 5&nbsp;GB, 10&nbsp;GB o 15&nbsp;GB. Ten en cuenta que el almacenamiento de la versión gratuita (100&nbsp;MB) está incluido en cada uno de estos planes.

## Especificaciones {#specifications}

La siguiente tabla resume las especificaciones de lo que puedes incluir en los catálogos.

| Área | Especificaciones |
|------|-----------|
| Caracteres del valor de un elemento | Hasta 5000 caracteres en un solo valor. Por ejemplo, si tienes un campo llamado `description`, el número máximo de caracteres dentro del campo es 5000. |
| Caracteres del nombre de columna de un elemento | Hasta 250 caracteres |
| Selecciones por catálogo | Hasta 30 selecciones por catálogo |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Las etiquetas de Liquid de catálogos no se pueden utilizar de forma recursiva, lo que significa que no puedes hacer referencia a un elemento del catálogo que a su vez llame a un segundo elemento del catálogo dentro de la misma evaluación de Liquid.
{% endalert %}