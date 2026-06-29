---
article_title: Atributos personalizados
permalink: "/custom_attributes_entitlements/"
hidden: true
---

# [![Curso de Braze Learning]({% image_buster /assets/unlisted_docs/img/logos/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Atributos personalizados {#braze-learning-course-image_buster-assetsunlisted_docsimglogosbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-attributes}

> Esta página cubre los atributos personalizados, que son una colección de rasgos únicos de tus usuarios. Los atributos personalizados son ideales para almacenar atributos sobre tus usuarios o información sobre acciones de bajo valor dentro de tu aplicación.

Cuando se almacenan en Braze, los atributos personalizados pueden utilizarse para crear segmentos de audiencia y personalizar la mensajería con Liquid. Ten en cuenta que no almacenamos información de series temporales para los atributos personalizados, por lo que no puedes obtener gráficos basados en ellos como sí puedes hacerlo con los eventos personalizados.

## Derechos de uso {#entitlements}

Los derechos de uso determinan tu capacidad de atributos personalizados, que rastrea el número de nombres de atributos diferentes que defines. Puedes tener hasta 1000 atributos personalizados por espacio de trabajo. Si necesitas aumentar tu capacidad, ponte en contacto con tu director de cuentas de Braze para obtener más información.

A medida que tu espacio de trabajo se acerque al número máximo de atributos personalizados, recibirás notificaciones en el dashboard y por correo electrónico para ayudarte a mantenerte al día.

Incluso después de alcanzar la capacidad, los atributos personalizados existentes aún pueden recibirse. Sin embargo, no podrás crear nuevos atributos personalizados. Los datos recibidos para atributos personalizados que aún no existan no se procesarán.

## Administrar atributos personalizados {#managing-custom-attributes}

Para crear y administrar atributos personalizados en el dashboard, ve a **Configuración de datos** > **Atributos personalizados**.

![Cuatro atributos personalizados que son booleanos.]({% image_buster /assets/unlisted_docs/img/custom_attributes_entitlements/export_custom_attributes.png %})

La columna **Última actualización** muestra la última vez que se editó el atributo personalizado, como cuándo se estableció por última vez en lista de bloqueo o activo.

{% alert important %}
Para una segmentación adecuada de los mensajes, asegúrate de que el tipo de datos de tu atributo personalizado coincida con el atributo personalizado real.
{% endalert %}

Desde esta página, puedes ver, administrar, crear o bloquear atributos personalizados existentes. Selecciona el menú junto a un atributo personalizado para las siguientes acciones:

### Lista de bloqueo {#blocklisting}

Los atributos personalizados pueden bloquearse individualmente en el menú de acciones, o se pueden seleccionar hasta 100 atributos y bloquearlos de forma masiva. Si bloqueas un atributo personalizado, no se recopilarán datos sobre ese atributo, los datos existentes no estarán disponibles a menos que se reactive, y los atributos bloqueados no aparecerán en filtros ni gráficos. Además, si el atributo está actualmente referenciado por filtros o desencadenadores en otras áreas del dashboard de Braze, aparecerá un modal de advertencia explicando que todas las instancias de los filtros o desencadenadores que lo referencian serán eliminadas y archivadas.

### Marcar como información de identificación personal (PII) {#marking-as-personally-identifiable-information-pii}

Los administradores también pueden crear atributos personalizados y marcarlos como PII desde esta página. Estos atributos solo serán visibles para los administradores y los usuarios del dashboard con el permiso "Ver atributos personalizados marcados como PII".

### Añadir descripciones {#adding-descriptions}

Puedes añadir una descripción a un atributo personalizado después de crearlo si tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) `Manage Events, Attributes, Purchases`. Edita el atributo personalizado e introduce lo que desees, como una nota para tu equipo.

### Añadir etiquetas {#adding-tags}

Puedes añadir etiquetas a un atributo personalizado después de crearlo si tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) "Manage Events, Attributes, Purchases". Las etiquetas pueden utilizarse para filtrar la lista de atributos.

### Eliminar atributos personalizados {#removing-custom-attributes}

Hay dos formas de eliminar atributos personalizados de los perfiles de usuario:

* Selecciona el nombre del atributo personalizado a eliminar en un [paso de Actualización de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#removing-custom-attributes).
* Establece el valor `null` en tu solicitud de API al [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#user-track).

### Ver informes de uso {#viewing-usage-reports}

El informe de uso enumera todos los Canvas, Campaigns y Segments que utilizan un atributo personalizado específico. Esta lista no incluye usos de Liquid.

Puedes ver hasta 100 informes de uso a la vez seleccionando las casillas de verificación junto a los atributos personalizados correspondientes y luego seleccionando **Ver informe de uso**.

### Exportar datos {#exporting-data}

Para exportar la lista de atributos personalizados como un archivo CSV, selecciona **Exportar todo** en la parte superior de la página. Se generará el archivo CSV y se te enviará un enlace de descarga por correo electrónico.

## Configurar atributos personalizados {#setting-custom-attributes}

A continuación se enumeran los métodos en varias plataformas que se utilizan para configurar atributos personalizados.

{% details Expandir para ver la documentación por plataforma %}

- [Android y FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)

{% enddetails %}

## Almacenamiento de atributos personalizados {#custom-attribute-storage}

Todos los datos almacenados en el **perfil de usuario**, incluidos los datos de atributos personalizados, se conservan indefinidamente mientras cada perfil esté [activo]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

## Tipos de datos de atributos personalizados {#custom-attribute-data-types}

Los atributos personalizados son herramientas extraordinariamente flexibles que permiten una gran segmentación.

Los siguientes tipos de datos pueden almacenarse como atributos personalizados:

- [Booleanos](#booleans)
- [Números](#numbers)
- [Cadenas](#strings)
- [Arrays](#arrays)
- [Tiempo](#time)
- [Objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)
- [Arrays de objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/)

### Booleanos (verdadero/falso) {#booleans}

Los atributos booleanos son útiles para almacenar datos binarios simples sobre tus usuarios, como estados de suscripción. Puedes encontrar usuarios que tienen explícitamente una variable establecida en un valor verdadero o falso, además de aquellos que aún no tienen ningún registro de ese atributo.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada | Ejemplos |
| ---------------------| --------------- | ------------- | -------- |
| Comprobar si el valor booleano **es** verdadero, falso, verdadero o no establecido, o falso o no establecido | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET** o **FALSE OR NOT SET** | Si este filtro especifica `coffee_drinker`, un usuario coincidirá con este filtro en las siguientes circunstancias: <br> {::nomarkdown}<ul><li>Si este filtro es <code>true</code> y el usuario tiene el valor <code>coffee_drinker</code></li><li>Si este filtro es <code>false</code> y el usuario no tiene el valor <code>coffee_drinker</code></li><li>Si este filtro es <code>true or not set</code> y el usuario tiene el valor <code>coffee_drinker</code> o ningún valor</li><li>Si este filtro es <code>false or not set</code> y el usuario no tiene <code>coffee_drinker</code> o ningún valor</li></ul>{:/} |
| Comprobar si el valor booleano **existe** en el perfil de un usuario y no es nulo | **IS NOT BLANK**  | **N/A** | Si este filtro especifica `coffee_drinker` y un usuario tiene un valor para el atributo `coffee_drinker`, el usuario coincidirá con este filtro. |
| Comprobar si el valor booleano **no existe** en el perfil de un usuario o es nulo | **IS BLANK**  | **N/A** | Si este filtro especifica `coffee_drinker` y un usuario no tiene el atributo `coffee_drinker` o el valor de `coffee_drinker` es nulo, el usuario coincidirá con este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Números {#numbers}

Los atributos numéricos incluyen [enteros](https://en.wikipedia.org/wiki/Integer) y [flotantes](https://en.wikipedia.org/wiki/Floating-point_arithmetic), y tienen una amplia variedad de casos de uso. Los atributos personalizados de números incrementales son útiles para almacenar el número de veces que una acción o evento determinado ha ocurrido sin contar contra tu límite de datos. Los números estándar tienen todo tipo de usos, como registrar:

- Talla de zapato
- Talla de cintura
- Número de veces que un usuario ha visto una característica o categoría de producto determinada

{% alert tip %}
El dinero gastado no debe registrarse con este método. Más bien, debe registrarse a través de nuestros [métodos de compra](#purchase-revenue-tracking).
{% endalert %}

| Opciones de segmentación | Filtro desplegable | Opciones de entrada | Ejemplos |
| ---------------------| --------------- | ------------- | -------- |
| Comprobar si el atributo numérico **es exactamente** un **número** | **EXACTLY** | **NUMBER** | Si este filtro especifica `10` y un perfil de usuario tiene el valor `10`, el usuario coincidirá con este filtro. |
| Comprobar si el atributo numérico **no es igual a** un **número** | **DOES NOT EQUAL** | **NUMBER** | Si este filtro especifica `10` y un perfil de usuario no tiene el valor `10`, el usuario coincidirá con este filtro. |
| Comprobar si el atributo numérico **es mayor que** un **número** | **MORE THAN** | **NUMBER** | Si este filtro especifica `10` y un perfil de usuario tiene un valor mayor que `10`, el usuario coincidirá con este filtro. |
| Comprobar si el atributo numérico **es menor que** un **número** | **LESS THAN** | **NUMBER** | Si este filtro especifica `10` y un perfil de usuario tiene un valor menor que `10`, el usuario coincidirá con este filtro. |
| Comprobar si el atributo numérico **existe** en el perfil de un usuario y no es nulo | **IS NOT BLANK** | **N/A** | Si un perfil de usuario contiene el atributo numérico especificado, independientemente del valor, el usuario coincidirá con este filtro. |
| Comprobar si el atributo numérico **no existe** en el perfil de un usuario o es nulo | **IS BLANK** | **N/A** | Si un perfil de usuario no contiene el atributo numérico especificado o el valor del atributo es nulo, el usuario coincidirá con este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Detalles de atributos numéricos {#number-attribute-details}

- Los filtros "Exactamente 0" y "Menor que" incluyen usuarios con campos NULL
  - Para excluir usuarios sin un valor para atributos personalizados, necesitas incluir el filtro **is not blank**.

### Cadenas (caracteres alfanuméricos) {#strings}

Los atributos de cadena son útiles para almacenar la entrada del usuario, como una marca favorita, un número de teléfono o la última cadena de búsqueda dentro de tu aplicación. Los atributos de cadena pueden tener hasta 255 caracteres de longitud.

Ten en cuenta que si introduces valores con espacios entre, antes o después de las palabras, Braze también comprobará esos mismos espacios.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada | Ejemplos |
| ---------------------| --------------- | ------------- | -------- |
| Comprobar si el atributo de cadena **coincide exactamente** con una cadena introducida | **EQUALS** | **STRING**<br>Distingue mayúsculas y minúsculas | Si este filtro especifica `book` y un perfil de usuario tiene un atributo de cadena para `last_item_purchased` que contiene `book`, el usuario coincidirá con este filtro. |
| Comprobar si el atributo de cadena **coincide parcialmente** con una cadena introducida **O** expresión regular | **MATCHES REGEX** | **STRING** **O** **REGULAR EXPRESSION** <br>No distingue mayúsculas y minúsculas; máximo de 32 764 caracteres |
| Comprobar si el atributo de cadena **no coincide parcialmente** con una cadena introducida **O** expresión regular | **DOES NOT MATCH REGEX** * | **STRING** **O** **REGULAR EXPRESSION**<br>No distingue mayúsculas y minúsculas; máximo de 32 764 caracteres |
| Comprobar si el atributo de cadena **no coincide** con una cadena introducida | **DOES NOT EQUAL** | **STRING**<br>No distingue mayúsculas y minúsculas  | Si este filtro especifica `book` y un perfil de usuario tiene un atributo de cadena para `last_item_purchased` que no contiene `book`, el usuario coincidirá con este filtro.|
| Comprobar si el atributo de cadena **existe** en el perfil de un usuario y no es una cadena vacía | **IS NOT BLANK** | **N/A** | Si este filtro especifica `favorite_genre` y un perfil de usuario tiene el atributo `favorite_genre`, el usuario coincidirá con este filtro independientemente del valor de su atributo. Por ejemplo, el usuario puede tener `sci-fi`, `romance` u otro valor.|
| Comprobar si el atributo de cadena **no existe** en el perfil de un usuario | **BLANK** | **N/A** | Si este filtro especifica `favorite_genre` y un perfil de usuario no tiene el atributo `favorite_genre`, el usuario coincidirá con este filtro.|
| Comprobar si la cadena coincide exactamente con **cualquiera** de las cadenas introducidas | **IS ANY OF** | **STRING**<br>Distingue mayúsculas y minúsculas; se permiten múltiples cadenas (máximo 256) | Si este filtro especifica `book`, `bookmark` y `reading light`, y un perfil de usuario tiene al menos una de esas cadenas, el usuario coincidirá con este filtro. |
| Comprobar si el atributo de cadena **no coincide exactamente con ninguna** de las cadenas introducidas | **IS NONE OF** |**STRING**<br>Distingue mayúsculas y minúsculas; se permiten múltiples cadenas (máximo 256) | Si este filtro especifica `book`, `bookmark` y `reading light`, y un perfil de usuario no contiene ninguna de esas cadenas, el usuario coincidirá con el filtro.|
| Comprobar si el atributo de cadena **coincide parcialmente con alguna** de las cadenas introducidas | **CONTAINS ANY OF** | **STRING**<br>Distingue mayúsculas y minúsculas; se permiten múltiples cadenas (máximo 256) | Si este filtro especifica `gold` y un perfil de usuario contiene `gold` en cualquier cadena, como `gold_tier` o `former_gold_tier`, el usuario coincidirá con el filtro. |
| Comprobar si el atributo de cadena **no coincide parcialmente con ninguna** de las cadenas introducidas | **DOESN'T CONTAIN ANY OF** | **STRING**<br>Distingue mayúsculas y minúsculas; se permiten múltiples cadenas (máximo 256) | Si este filtro especifica `gold` y un perfil de usuario no contiene `gold` en ninguna cadena, el usuario coincidirá con este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Una cadena de fecha como "12-1-2021" o "12/1/2021" se convertirá en un objeto datetime y se tratará como un [atributo de tiempo]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time).
{% endalert %}

{% alert important %}
Al segmentar con el filtro **DOES NOT MATCH REGEX**, ya debes tener un atributo personalizado con un valor asignado en ese perfil de usuario. Braze sugiere usar la lógica "OR" para comprobar si un atributo personalizado está en blanco y así asegurar que los usuarios se segmenten correctamente.
{% endalert %}

### Arrays {#arrays}

Los atributos de array son buenos para almacenar listas de información relacionada sobre tus usuarios. Por ejemplo, almacenar las últimas 100 piezas de contenido que un usuario vio dentro de un array permitiría una segmentación específica por intereses.

De forma predeterminada, la longitud máxima de un array para un atributo está establecida en 25 y puede aumentarse hasta 100 para un array individual. Por ejemplo, si estás enviando un atributo como "Películas vistas" y está establecido en 100, cuando un usuario vea una película número 101, la primera película se eliminará del array y se añadirá la más reciente.

Si deseas que este máximo se aumente, ponte en contacto con tu administrador del éxito del cliente. Tu administrador del dashboard puede entonces aumentar la longitud máxima para arrays individuales a más de 100 desde la pestaña **Atributos personalizados** de la página **Administrar configuración**.

Ten en cuenta que si introduces valores con espacios entre, antes o después de las palabras, Braze también comprobará esos mismos espacios.

{% alert note %}
La opción de aumentar la longitud máxima no estará disponible si el atributo está configurado para detectar automáticamente el tipo de datos; el tipo de datos debe establecerse en array.
{% endalert %}

| Opciones de segmentación | Filtro desplegable | Opciones de entrada | Ejemplos |
| ---------------------| --------------- | ------------- | -------- |
| Comprobar si el atributo de array **incluye un valor que coincide exactamente** con un valor introducido | **INCLUDES VALUE** | **STRING** | Si este filtro especifica `sci-fi` y un perfil de usuario tiene el valor `sci-fi`, el usuario coincidirá con este filtro.|
| Comprobar si el atributo de array **no incluye un valor que coincida exactamente** con un valor introducido | **DOESN'T INCLUDE VALUE** | **STRING** | Si este filtro especifica `sci-fi` y un perfil de usuario no tiene el valor `sci-fi`, el usuario coincidirá con este filtro.|
| Comprobar si el atributo de array **contiene un valor que coincide parcialmente** con un valor introducido **O** expresión regular | **MATCHES REGEX** | **STRING** **O** **REGULAR EXPRESSION**<br>Máximo de 32 764 caracteres | |
| Comprobar si el atributo de array **tiene algún valor** o no está vacío | **HAS A VALUE** | **N/A** | Si este filtro especifica `favorite_genres` y un perfil de usuario contiene `favorite_genres` con cualquier valor, el usuario coincidirá con este filtro. |
| Comprobar si el atributo de array **está vacío** o no existe | **IS EMPTY** | **N/A** | Si este filtro especifica `favorite_genres` y un perfil de usuario no contiene `favorite_genres` o contiene `favorite_genres` pero no tiene valores, el usuario coincidirá con este filtro.|
| Comprobar si el atributo de array **incluye un valor que coincide exactamente con alguno** de los valores introducidos | **INCLUDES ANY OF** | **STRING**<br>Distingue mayúsculas y minúsculas; se permiten múltiples valores (máximo 256) | Si este filtro especifica `sci-fi, fantasy, romance` y un perfil de usuario tiene cualquier combinación de `sci-fi`, `fantasy` o `romance`, incluyendo solo uno de ellos (como solo `sci-fi`). Un usuario puede tener `horror` u otro valor en su cadena si también tiene alguno de `sci-fi`, `fantasy` y `romance`.|
| Comprobar si el atributo de array **no incluye un valor que coincida exactamente con ninguno** de los valores introducidos | **INCLUDES NONE OF** | **STRING**<br>Distingue mayúsculas y minúsculas; se permiten múltiples valores (máximo 256) | Si este filtro especifica `sci-fi, fantasy, romance` y un perfil de usuario no tiene ninguna combinación de `sci-fi`, `fantasy` o `romance`, el usuario coincidirá con este filtro. El usuario puede tener `horror` u otro valor si no tiene ninguno de `sci-fi`, `fantasy` o `romance`.|
| Comprobar si el atributo de array **contiene un valor que coincide parcialmente con alguno** de los valores introducidos | **VALUES CONTAIN ANY OF** | **STRING**<br>Distingue mayúsculas y minúsculas; se permiten múltiples valores (máximo 256) | Si este filtro especifica `gold` y un array del perfil de usuario contiene `gold` en al menos una cadena, el usuario coincidirá con este filtro. Esto incluye valores de cadena como `gold_tier`, `former_gold_tier` y otros.|
| Comprobar si el atributo de array **no incluye un valor que coincida parcialmente con ninguno** de los valores introducidos | **VALUES DON'T CONTAIN ANY OF** | **STRING**<br>Distingue mayúsculas y minúsculas; se permiten múltiples valores (máximo 256) | Si este filtro especifica `gold` y un array del perfil de usuario no contiene `gold` en ninguna cadena, el usuario coincidirá con este filtro. Esto significa que los usuarios con valores de cadena como `gold_tier` y `former_gold_tier` no coincidirán con este filtro.|
| Comprobar si el atributo de array **incluye todos** los valores introducidos | **IS ALL OF** | **STRING**<br>Distingue mayúsculas y minúsculas; se permiten múltiples valores (máximo 256) | Si este filtro especifica `sci-fi, fantasy, romance` y un perfil de usuario tiene todos esos valores, el usuario coincidirá con este filtro. El usuario también puede tener `horror` u otros valores y aún coincidir con este filtro.|
| Comprobar si el atributo de array **no incluye todos** los valores introducidos | **ISN'T ALL OF** | **STRING**<br>Distingue mayúsculas y minúsculas; se permiten múltiples valores (máximo 256) | Si este filtro especifica `sci-fi, fantasy, romance` y un perfil de usuario no tiene todos esos valores, el usuario coincidirá con este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Para más información sobre cómo usar expresiones regulares (regex), consulta estos recursos:
- [Expresiones regulares compatibles con Perl (PCRE)](https://www.regextester.com/pregsyntax.html)
- [Regex con Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Depurador y probador de regex](https://www.regex101.com/)
- [Tutorial de regex](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Tiempo {#time}

Los atributos de tiempo son útiles para almacenar la última vez que se realizó una acción específica, para que puedas ofrecer mensajes de reactivación de la interacción específicos a tus usuarios.

Los filtros de tiempo que usan fechas relativas (por ejemplo, hace más de 1 día, hace menos de 2 días) miden 1 día como 24 horas. Cualquier campaña que ejecutes usando estos filtros incluirá a todos los usuarios en incrementos de 24 horas. Por ejemplo, `last used app more than 1 day ago` capturará a todos los usuarios que "usaron la aplicación por última vez hace más de 24 horas" desde el momento exacto en que se ejecuta la campaña. Lo mismo será cierto para campañas configuradas con rangos de fechas más largos, por lo que cinco días desde la activación significarán las 120 horas anteriores.

Por ejemplo, para crear un segmento que se dirija a usuarios con un atributo de tiempo entre 24 y 48 horas en el futuro, aplica los filtros `in more than 1 day in the future` e `in less than 2 days in the future`.

{% alert warning %}
La última fecha en que ocurrió un evento personalizado o un evento de compra se registra automáticamente y no debe registrarse de nuevo a través de un atributo de tiempo personalizado.
{% endalert %}

| Opciones de segmentación | Filtro desplegable | Opciones de entrada | Ejemplos |
| ---------------------| --------------- | ------------- | -------- |
| Comprobar si el atributo de tiempo **es anterior a** una **fecha seleccionada** | **BEFORE** | **CALENDAR DATE SELECTOR** | Si este filtro especifica `2024-01-31` y un perfil de usuario tiene una fecha anterior a `2024-1-31`, el usuario coincidirá con este filtro. |
| Comprobar si el atributo de tiempo **es posterior a** una **fecha seleccionada** | **AFTER** | **CALENDAR DATE SELECTOR** | Si este filtro especifica `2024-01-31` y un perfil de usuario tiene una fecha posterior a `2024-1-31`, el usuario coincidirá con este filtro. |
| Comprobar si el atributo de tiempo es **hace más de X número** de **días** | **MORE THAN** | **NUMBER OF DAYS AGO** | Si este filtro especifica `7` y un perfil de usuario tiene una fecha de hace más de siete días, el usuario coincidirá con este filtro. |
| Comprobar si el atributo de tiempo es **hace menos de X número** de **días** | **LESS THAN** | **NUMBER OF DAYS AGO** | Si este filtro especifica `7` y un perfil de usuario tiene una fecha de hace menos de siete días, el usuario coincidirá con este filtro.|
| Comprobar si el atributo de tiempo es **en más de X número** de **días en el futuro** | **IN MORE THAN** | **NUMBER OF DAYS IN FUTURE** | Si este filtro especifica `7` y un perfil de usuario tiene una fecha de más de siete días en el futuro, el usuario coincidirá con este filtro.|
| Comprobar si el atributo de tiempo es **en menos de X número** de **días en el futuro** | **IN LESS THAN** | **NUMBER OF DAYS IN FUTURE**  | Si este filtro especifica `7` y un perfil de usuario tiene una fecha de menos de siete días en el futuro, el usuario coincidirá con este filtro.|
| Comprobar si el atributo de tiempo **existe** en el perfil de un usuario y no es nulo | **IS NOT BLANK** | **N/A** | Si este filtro especifica un atributo de tiempo que está en un perfil de usuario, el usuario coincidirá con este filtro.|
| Comprobar si el atributo de tiempo **no existe** en el perfil de un usuario o es nulo | **IS BLANK** | **N/A** | Si este filtro especifica un atributo de tiempo que no está en un perfil de usuario, el usuario coincidirá con este filtro. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Detalles de atributos de tiempo {#time-attribute-details}

- Día de evento recurrente
  - Al usar el filtro "Día de evento recurrente" y luego se te solicita seleccionar el "Día del calendario del evento recurrente", si seleccionas `IS LESS THAN` o `IS MORE THAN`, la fecha actual se contará para ese filtro de segmentación.
  - Por ejemplo, si el 10 de marzo de 2020 seleccionaste la fecha del atributo como `LESS THAN ... March 10, 2020`, los atributos se considerarán para los días hasta e incluyendo el 10 de marzo de 2020.
- Hace menos de X días: el filtro "Hace menos de X días" incluye fechas entre hace X días y la fecha/hora actual.
- En menos de X días en el futuro: incluye fechas entre la fecha/hora actual y X días en el futuro.

### Objetos {#objects}

Puedes usar atributos personalizados anidados para enviar objetos como tipo de datos para atributos personalizados. Para más información, consulta [Atributos personalizados anidados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/).

### Arrays de objetos {#arrays-of-objects}

Usa un array de objetos para agrupar atributos relacionados. Para más detalles, consulta nuestro artículo sobre [Array de objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/).

### Operadores consolidados {#consolidated-operators}

Hemos consolidado la lista de operadores disponibles para usar en filtros de atributos, filtros de atributos personalizados y filtros de atributos personalizados anidados. Si tienes filtros existentes que usan estos operadores, se actualizarán automáticamente para usar los nuevos operadores.

| Tipo de datos | Operador anterior | Nuevo operador | Valor |
| --- | --- | --- | --- |
| Cadena | equals | is any of | Al menos 1 valor |
| Cadena | does not equal | is none of | Al menos 1 valor |
| Array | includes value | includes any of | Al menos 1 valor |
| Array | doesn't include value | includes none of | Al menos 1 valor |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Seguimiento de compras e ingresos {#purchase-revenue-tracking}

Usar nuestros métodos de compra para registrar compras dentro de la aplicación establece el valor de duración del ciclo de vida (LTV) para cada perfil de usuario individual. Estos datos se pueden ver en nuestra página de ingresos en series temporales.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada | Ejemplos |
| ---------------------| --------------- | ------------- | -------- |
| Comprobar si el número total de dólares gastados **es mayor que** un **número** | **GREATER THAN** | **NUMBER** | Si este filtro especifica `500` y un perfil de usuario tiene un valor mayor que `500`, el usuario coincidirá con este filtro. |
| Comprobar si el número total de dólares gastados **es menor que** un **número** | **LESS THAN** | **NUMBER** | Si este filtro especifica `500` y un perfil de usuario tiene un valor menor que `500`, el usuario coincidirá con este filtro.|
| Comprobar si el número total de dólares gastados **es exactamente** un **número** | **EXACTLY** | **NUMBER** | Si este filtro especifica `500` y un perfil de usuario tiene el valor `500`, el usuario coincidirá con este filtro. |
| Comprobar si la compra ocurrió por última vez **después de la fecha X** | **AFTER** | **TIME** | Si este filtro especifica `2024/31/1` y la última compra de un usuario fue después de `2024/31/1`, el usuario coincidirá con este filtro.|
| Comprobar si la compra ocurrió por última vez **antes de la fecha X** | **BEFORE** | **TIME** | Si este filtro especifica `2024/31/1` y la última compra de un usuario fue antes de `2024/31/1`, el usuario coincidirá con este filtro.|
| Comprobar si la compra ocurrió por última vez **hace más de X días** | **MORE THAN** | **TIME** | Si este filtro especifica `7` y la última compra de un usuario fue hace más de siete días desde hoy, el usuario coincidirá con este filtro.|
| Comprobar si la compra ocurrió por última vez **hace menos de X días** | **LESS THAN** | **TIME** |  Si este filtro especifica `7` y la última compra de un usuario fue hace menos de siete días desde hoy, el usuario coincidirá con este filtro.|
| Comprobar si la compra ocurrió **más de X (máx. = 50) veces** | **MORE THAN** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |  Si este filtro especifica `7` veces y `21` días, y un usuario realizó más de siete compras en los últimos 21 días, el usuario coincidirá con este filtro.|
| Comprobar si la compra ocurrió **menos de X (máx. = 50) veces** | **LESS THAN** | en los últimos **Y días (Y = 1,3,7,14,21,30)** | Si este filtro especifica `7` veces y `21` días, y un usuario realizó menos de siete compras en los últimos 21 días, el usuario coincidirá con este filtro.|
| Comprobar si la compra ocurrió **exactamente X (máx. = 50) veces** | **EXACTLY** | en los últimos **Y días (Y = 1,3,7,14,21,30)** | Si este filtro especifica `7` veces y `21` días, y un usuario realizó siete compras en los últimos 21 días, el usuario coincidirá con este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Si deseas segmentar por el número de veces que se ha realizado una compra específica, también debes registrar esa compra individualmente como un [atributo personalizado incremental]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#incrementingdecrementing-custom-attributes).
{% endalert %}

Puedes cambiar el tipo de datos de tu atributo personalizado, pero debes tener en cuenta los impactos de [cambiar los tipos de datos]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/).