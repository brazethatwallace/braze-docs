---
nav_title: Tipos de datos
article_title: Tipos de datos
page_order: 1
page_type: reference
description: "Referencia de los tipos de datos compatibles con atributos personalizados, propiedades del evento y catálogos en Braze."
toc_headers: h2
---

# Tipos de datos {#data-types}

> Esta página consolida los tipos de datos compatibles con atributos personalizados, propiedades del evento y catálogos. Cada tipo de datos personalizado tiene un soporte y restricciones ligeramente diferentes.

## Definiciones {#definitions}

Usa esta tabla para ver qué tipos de datos puedes utilizar para atributos del perfil de usuario, datos de eventos o elementos de catálogo. Consulta las secciones siguientes para conocer el uso y las restricciones de cada tipo.

<table role="presentation" class="definitions-table reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4 reset-td-br-5">
  <thead>
    <tr>
      <th>Tipo de datos</th>
      <th>Definición</th>
      <th>Atributos personalizados</th>
      <th>Propiedades del evento</th>
      <th>Catálogos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Booleano</td>
      <td>Valor <code>true</code> o <code>false</code></td>
      <td>✅ Compatible</td>
      <td>✅ Compatible</td>
      <td>✅ Compatible</td>
    </tr>
    <tr>
      <td>Número</td>
      <td>Número entero o decimal</td>
      <td>✅ Compatible</td>
      <td>✅ Compatible</td>
      <td>✅ Compatible</td>
    </tr>
    <tr>
      <td>Cadena</td>
      <td>Texto; 255 caracteres o menos</td>
      <td>✅ Compatible</td>
      <td>✅ Compatible</td>
      <td>✅ Compatible</td>
    </tr>
    <tr>
      <td>Hora</td>
      <td>Fecha y hora en un formato estándar (<a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a>)</td>
      <td>✅ Compatible</td>
      <td>✅ Compatible</td>
      <td>✅ Compatible</td>
    </tr>
    <tr>
      <td>Matriz</td>
      <td>Lista ordenada de valores</td>
      <td>✅ Compatible</td>
      <td>✅ Compatible</td>
      <td>✅ Compatible</td>
    </tr>
    <tr>
      <td>Objeto</td>
      <td>Datos estructurados con campos con nombre (par clave-valor anidado)</td>
      <td>✅ Compatible</td>
      <td>✅ Compatible</td>
      <td>✅ Compatible</td>
    </tr>
    <tr>
      <td>Matriz de objetos</td>
      <td>Lista de objetos</td>
      <td>✅ Compatible</td>
      <td>❌ No compatible</td>
      <td>❌ No compatible</td>
    </tr>
  </tbody>
</table>

### Consideraciones importantes {#important-considerations}

- **Matriz:** Los atributos personalizados y las propiedades del evento tienen límites de tamaño. Las fechas y horas no son compatibles dentro de matrices en las propiedades del evento. Los catálogos solo admiten matrices de cadenas, con un máximo de 100 elementos.
- **Objeto:** En Braze, esto aparece como "atributos personalizados anidados" para atributos personalizados, "objetos anidados" para propiedades del evento y "objeto JSON" para catálogos.
- **Hora:** En las propiedades del evento, este tipo se etiqueta como "Datetime".

## Tipos de datos de atributos personalizados {#custom-attribute-data-types}

Los atributos personalizados admiten los tipos de datos enumerados en la tabla de [Definiciones](#definitions). A continuación se describe el uso y la segmentación para cada tipo de datos compatible.

{% tabs %}
{% tab Booleano %}

Puedes bloquear atributos personalizados individualmente en el menú de acciones, o puedes seleccionar y bloquear hasta 100 atributos de forma masiva. Si bloqueas un atributo personalizado, no se recopilan datos sobre ese atributo, los datos existentes no están disponibles a menos que se reactive, y los atributos bloqueados no aparecen en filtros ni gráficos. Además, si el atributo está actualmente referenciado por filtros o desencadenantes en otras áreas del panel de Braze, aparece un modal de advertencia explicando que todas las instancias de los filtros o desencadenantes que lo referencian se eliminan y archivan.

### Marcar como información de identificación personal (PII) {#marking-as-personally-identifiable-information-pii}

Los administradores también pueden crear atributos personalizados y marcarlos como PII desde esta página. Estos atributos solo son visibles para administradores y usuarios del panel con el permiso "View Custom Attributes Marked as PII".

### Añadir descripciones {#adding-descriptions}

Puedes añadir una descripción a un atributo personalizado después de crearlo si tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions) `Manage Events, Attributes, Purchases`. Edita el atributo personalizado e introduce lo que desees, como una nota para tu equipo.

### Añadir etiquetas {#adding-tags}

Puedes añadir etiquetas a un atributo personalizado después de crearlo si tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions) "Manage Events, Attributes, Purchases". Luego puedes usar las etiquetas para filtrar la lista de atributos.

### Eliminar atributos personalizados {#removing-custom-attributes}

Hay dos formas de eliminar atributos personalizados de los perfiles de usuario:

- Selecciona el nombre del atributo personalizado a eliminar en un [paso de Actualización de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update#removing-custom-attributes).
- Establece el valor `null` en tu solicitud de API al [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

#### Establecer el valor `null` {#setting-the-null-value}

{% alert important %}
Establecer un atributo como `null` y establecerlo como `""` (cadena vacía) no es lo mismo.
{% endalert %}

- `null` elimina el atributo del perfil de usuario por completo. No aparece en el perfil ni coincide con ningún filtro **IS NOT BLANK**.
- `""` establece el atributo como un valor de cadena vacía. El atributo aparece en el perfil con un valor de cadena vacía, pero no coincide con los filtros **IS NOT BLANK** (se trata como vacío).

Además, `""` solo es válido para atributos de tipo cadena. Si el tipo de datos del atributo está configurado como un tipo que no es cadena (como booleano, número u hora) en el panel, enviar `""` no borra el valor; usa `null` en su lugar.

### Exportar datos {#exporting-data}

Para exportar la lista de atributos personalizados como un archivo CSV, selecciona **Export all** en la parte superior de la página. El sistema genera un archivo CSV y te envía un enlace de descarga por correo electrónico.

## Ver informes de uso {#viewing-usage-reports}

El informe de uso enumera todos los Canvas, Campaigns y Segments que utilizan un atributo personalizado específico. Esta lista no incluye usos de Liquid.

Puedes ver hasta 100 informes de uso a la vez seleccionando las casillas de verificación junto a los atributos personalizados correspondientes y luego seleccionando **View usage report**.

### Pestaña de valores {#values-tab}

Al ver un informe de uso, selecciona la pestaña **Values** para ver los valores principales de los atributos personalizados seleccionados basándose en una muestra de aproximadamente 250.000 usuarios. Ten en cuenta que, dado que los resultados se muestrean de un subconjunto de usuarios, la muestra no incluye todos los valores existentes. Esto significa que la pestaña **Values** no debe usarse para solución de problemas ni para casos de uso que requieran incorporar datos de todos los usuarios.

![Informe de uso para atributos personalizados seleccionados con una pestaña "Values" abierta que muestra un gráfico circular de valores del atributo de país, como "US" y "PR".]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## Configurar atributos personalizados {#setting-custom-attributes}

A continuación se enumeran los métodos en varias plataformas que se utilizan para configurar atributos personalizados.

{% details Expandir para ver la documentación por plataforma %}

- [Android y FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=unity)
- [.NET MAUI (anteriormente Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes)

{% enddetails %}

## Almacenamiento de atributos personalizados {#custom-attribute-storage}

Todos los datos almacenados en el **perfil de usuario**, incluidos los datos de atributos personalizados, se conservan indefinidamente mientras cada perfil esté [activo]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#active-users).

## Tipos de datos de atributos personalizados

Los atributos personalizados son herramientas extraordinariamente flexibles que permiten una gran capacidad de segmentación.

Los siguientes tipos de datos pueden almacenarse como atributos personalizados:

- [Booleanos](#booleans)
- [Números](#numbers)
- [Cadenas](#strings)
- [Matrices](#arrays)
- [Hora](#time)
- [Objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support)
- [Matrices de objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects)

### Booleanos (verdadero/falso) {#booleans}

Los atributos booleanos son útiles para almacenar datos binarios simples sobre tus usuarios, como estados de suscripción. Puedes encontrar usuarios que tienen explícitamente una variable establecida como verdadera o falsa, además de aquellos que aún no tienen ningún registro de ese atributo.

Para los atributos **booleanos**, están disponibles las siguientes opciones de segmentación.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada | Ejemplos |
| ---------------------| --------------- | ------------- | -------- |
| Comprobar si el valor booleano **es** verdadero, falso, verdadero o no establecido, o falso o no establecido | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET** o **FALSE OR NOT SET** | Si este filtro especifica `coffee_drinker`, un usuario coincidirá con este filtro en las siguientes circunstancias: <br> {::nomarkdown}<ul><li>Si este filtro es <code>true</code> y el usuario tiene el valor <code>coffee_drinker</code></li><li>Si este filtro es <code>false</code> y el usuario no tiene el valor <code>coffee_drinker</code></li><li>Si este filtro es <code>true or not set</code> y el usuario tiene el valor <code>coffee_drinker</code> o ningún valor</li><li>Si este filtro es <code>false or not set</code> y el usuario no tiene <code>coffee_drinker</code> o ningún valor</li></ul>{:/} |
| Comprobar si el valor booleano **existe** en el perfil de un usuario y no es nulo | **IS NOT BLANK**  | **N/A** | Si este filtro especifica `coffee_drinker` y un usuario tiene un valor para el atributo `coffee_drinker`, el usuario coincidirá con este filtro. |
| Comprobar si el valor booleano **no existe** en el perfil de un usuario o es nulo | **IS BLANK**  | **N/A** | Si este filtro especifica `coffee_drinker` y un usuario no tiene el atributo `coffee_drinker` o el valor de `coffee_drinker` es nulo, el usuario coincidirá con este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Booleans (true/false) #booleans" }

{% endtab %}
{% tab Números %}

{% alert tip %}
El dinero gastado no debe registrarse con este método. Más bien, debe registrarse a través de [eventos de compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events).
{% endalert %}

Para los atributos **numéricos**, están disponibles las siguientes opciones de segmentación.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada | Ejemplos |
| ---------------------| --------------- | ------------- | -------- |
| Comprobar si el atributo numérico **es exactamente** un **número**| **EXACTLY** | **NUMBER** | Si este filtro especifica `10` y un perfil de usuario tiene el valor `10`, el usuario coincidirá con este filtro. |
| Comprobar si el atributo numérico **no es igual a** un **número**| **DOES NOT EQUAL** | **NUMBER** | Si este filtro especifica `10` y un perfil de usuario no tiene el valor `10`, el usuario coincidirá con este filtro. |
| Comprobar si el atributo numérico **es mayor que** un **número**| **MORE THAN** | **NUMBER** | Si este filtro especifica `10` y un perfil de usuario tiene un valor mayor que `10`, el usuario coincidirá con este filtro. |
| Comprobar si el atributo numérico **es menor que** un **número**| **LESS THAN** | **NUMBER** | Si este filtro especifica `10` y un perfil de usuario tiene un valor menor que `10`, el usuario coincidirá con este filtro. |
| Comprobar si el atributo numérico **existe** en el perfil de un usuario y no es nulo | **IS NOT BLANK** | **N/A** | Si un perfil de usuario contiene el atributo numérico especificado, independientemente del valor, el usuario coincidirá con este filtro. |
| Comprobar si el atributo numérico **no existe** en el perfil de un usuario o es nulo | **IS BLANK** | **N/A** | Si un perfil de usuario no contiene el atributo numérico especificado o el valor del atributo es nulo, el usuario coincidirá con este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

#### Detalles de atributos numéricos {#number-attribute-details}

- Los filtros "Exactamente 0" y "Menor que" incluyen usuarios con campos NULL
  - Para excluir usuarios sin un valor para atributos personalizados, necesitas incluir el filtro **is not blank**.

{% endtab %}
{% tab Cadenas %}

Los atributos de cadena pueden tener hasta 255 caracteres de longitud. Ten en cuenta que si introduces valores con espacios entre, antes o después de las palabras, Braze también comprobará esos mismos espacios.

Para los atributos de **cadena**, están disponibles las siguientes opciones de segmentación.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada | Ejemplos |
| ---------------------| --------------- | ------------- | -------- |
| Comprobar si el atributo de cadena **coincide parcialmente** con una cadena introducida **O** expresión regular | **MATCHES REGEX** | **STRING** **O** **REGULAR EXPRESSION** <br>No distingue entre mayúsculas y minúsculas; máximo de 32.764 caracteres |
| Comprobar si el atributo de cadena **no coincide parcialmente** con una cadena introducida **O** expresión regular | **DOES NOT MATCH REGEX** * | **STRING** **O** **REGULAR EXPRESSION**<br>No distingue entre mayúsculas y minúsculas; máximo de 32.764 caracteres |
| Comprobar si el atributo de cadena **existe** en el perfil de un usuario y no es una cadena vacía | **IS NOT BLANK** | **N/A** | Si este filtro especifica `favorite_genre` y un perfil de usuario tiene el atributo `favorite_genre`, el usuario coincidirá con este filtro independientemente del valor del atributo. Por ejemplo, el usuario puede tener `sci-fi`, `romance` u otro valor.|
| Comprobar si el atributo de cadena **no existe** en el perfil de un usuario | **BLANK** | **N/A** | Si este filtro especifica `favorite_genre` y un perfil de usuario no tiene el atributo `favorite_genre`, el usuario coincidirá con este filtro.|
| Comprobar si la cadena coincide exactamente con **alguna** de las cadenas introducidas | **IS ANY OF** | **STRING**<br>Distingue entre mayúsculas y minúsculas; se permiten múltiples cadenas (máximo 256) | Si este filtro especifica `book`, `bookmark` y `reading light`, y un perfil de usuario tiene al menos una de esas cadenas, el usuario coincidirá con este filtro. |
| Comprobar si el atributo de cadena **no coincide exactamente con ninguna** de las cadenas introducidas | **IS NONE OF** |**STRING**<br>Distingue entre mayúsculas y minúsculas; se permiten múltiples cadenas (máximo 256) | Si este filtro especifica `book`, `bookmark` y `reading light`, y un perfil de usuario no contiene ninguna de esas cadenas, el usuario coincidirá con el filtro.|
| Comprobar si el atributo de cadena **coincide parcialmente con alguna** de las cadenas introducidas | **CONTAINS ANY OF** | **STRING**<br>Distingue entre mayúsculas y minúsculas; se permiten múltiples cadenas (máximo 256) | Si este filtro especifica `gold` y un perfil de usuario contiene `gold` en cualquier cadena, como `gold_tier` o `former_gold_tier`, el usuario coincidirá con el filtro. |
| Comprobar si el atributo de cadena **no coincide parcialmente con ninguna** de las cadenas introducidas | **DOESN'T CONTAIN ANY OF** | **STRING**<br>Distingue entre mayúsculas y minúsculas; se permiten múltiples cadenas (máximo 256) | Si este filtro especifica `gold` y un perfil de usuario no contiene `gold` en ninguna cadena, el usuario coincidirá con este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

{% multi_lang_include alerts/note_alerts.md alert='Custom Attributes time attribute' %}

{% alert important %}
Al segmentar usando el filtro **DOES NOT MATCH REGEX**, ya debes tener un atributo personalizado con un valor asignado en ese perfil de usuario. Braze sugiere usar la lógica "OR" para comprobar si un atributo personalizado está vacío y así asegurar que los usuarios se segmenten correctamente.
{% endalert %}

{% endtab %}
{% tab Matrices %}

Las matrices tienen un tamaño máximo de 100&nbsp;KB. La longitud predeterminada de un atributo es de hasta 500 elementos (por ejemplo, si envías un atributo como "Películas vistas" configurado en 500, cuando un usuario vea una película número 501, la primera película se elimina y se añade la más reciente). Ten en cuenta que si introduces valores con espacios entre, antes o después de las palabras, Braze también comprobará esos mismos espacios.

Los atributos personalizados de tipo matriz no se pueden importar mediante [importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import). Para cargar valores de matriz, usa el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) o la [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/cloud_ingestion).

{% alert note %}
La opción de aumentar la longitud máxima no estará disponible si el atributo está configurado para detectar automáticamente el tipo de datos; el tipo de datos debe establecerse como matriz.
{% endalert %}

Para los atributos de **matriz**, están disponibles las siguientes opciones de segmentación.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada | Ejemplos |
| ---------------------| --------------- | ------------- | -------- |
| Comprobar si el atributo de matriz **incluye un valor que coincide exactamente** con un valor introducido| **INCLUDES VALUE** | **STRING** | Si este filtro especifica `sci-fi` y un perfil de usuario tiene el valor `sci-fi`, el usuario coincidirá con este filtro.|
| Comprobar si el atributo de matriz **no incluye un valor que coincida exactamente** con un valor introducido| **DOESN'T INCLUDE VALUE** | **STRING** | Si este filtro especifica `sci-fi` y un perfil de usuario no tiene el valor `sci-fi`, el usuario coincidirá con este filtro.|
| Comprobar si el atributo de matriz **contiene un valor que coincide parcialmente** con un valor introducido **O** expresión regular | **MATCHES REGEX** | **STRING** **O** **REGULAR EXPRESSION**<br>Máximo de 32.764 caracteres | |
| Comprobar si el atributo de matriz **tiene algún valor** o no está vacío | **HAS A VALUE** | **N/A** | Si este filtro especifica `favorite_genres` y un perfil de usuario contiene `favorite_genres` con cualquier valor, el usuario coincidirá con este filtro. |
| Comprobar si el atributo de matriz **está vacío** o no existe | **IS EMPTY** | **N/A** | Si este filtro especifica `favorite_genres` y un perfil de usuario no contiene `favorite_genres` o contiene `favorite_genres` pero no tiene valores, el usuario coincidirá con este filtro.|
| Comprobar si el atributo de matriz **incluye un valor que coincide exactamente con alguno** de los valores introducidos | **INCLUDES ANY OF** | **STRING**<br>Distingue entre mayúsculas y minúsculas; se permiten múltiples valores (máximo 256) | Si este filtro especifica `sci-fi, fantasy, romance` y un perfil de usuario tiene cualquier combinación de `sci-fi`, `fantasy` o `romance`, incluyendo solo uno de ellos (como solo `sci-fi`). Un usuario puede tener `horror` u otro valor en su cadena si también tiene alguno de `sci-fi`, `fantasy` y `romance`.|
| Comprobar si el atributo de matriz **no incluye un valor que coincida exactamente con ninguno** de los valores introducidos | **INCLUDES NONE OF** | **STRING**<br>Distingue entre mayúsculas y minúsculas; se permiten múltiples valores (máximo 256) | Si este filtro especifica `sci-fi, fantasy, romance` y un perfil de usuario no tiene ninguna combinación de `sci-fi`, `fantasy` o `romance`, el usuario coincidirá con este filtro. El usuario puede tener `horror` u otro valor si no tiene ninguno de `sci-fi`, `fantasy` o `romance`.|
| Comprobar si el atributo de matriz **contiene un valor que coincide parcialmente con alguno** de los valores introducidos | **VALUES CONTAIN ANY OF** | **STRING**<br>Distingue entre mayúsculas y minúsculas; se permiten múltiples valores (máximo 256) | Si este filtro especifica `gold` y una matriz del perfil de usuario contiene `gold` en al menos una cadena, el usuario coincidirá con este filtro. Esto incluye valores de cadena como `gold_tier`, `former_gold_tier` y otros.|
| Comprobar si el atributo de matriz **no incluye un valor que coincida parcialmente con ninguno** de los valores introducidos | **VALUES DON'T CONTAIN ANY OF** | **STRING**<br>Distingue entre mayúsculas y minúsculas; se permiten múltiples valores (máximo 256) | Si este filtro especifica `gold` y una matriz del perfil de usuario no contiene `gold` en ninguna cadena, el usuario coincidirá con este filtro. Esto significa que los usuarios con valores de cadena como `gold_tier` y `former_gold_tier` no coincidirán con este filtro.|
| Comprobar si el atributo de matriz **incluye todos** los valores introducidos | **IS ALL OF** | **STRING**<br>Distingue entre mayúsculas y minúsculas; se permiten múltiples valores (máximo 256) | Si este filtro especifica `sci-fi, fantasy, romance` y un perfil de usuario tiene todos esos valores, el usuario coincidirá con este filtro. El usuario también puede tener `horror` u otros valores y coincidir con este filtro.|
| Comprobar si el atributo de matriz **no incluye todos** los valores introducidos | **ISN'T ALL OF** | **STRING**<br>Distingue entre mayúsculas y minúsculas; se permiten múltiples valores (máximo 256)|  Si este filtro especifica `sci-fi, fantasy, romance` y un perfil de usuario no tiene todos esos valores, el usuario coincidirá con este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

{% alert tip %}
Para más información sobre cómo usar expresiones regulares (regex), consulta estos recursos:

- [Expresiones regulares compatibles con Perl (PCRE)](https://www.regextester.com/pregsyntax.html)
- [Regex con Braze]({{site.baseurl}}/user_guide/audience/segments/regex)
- [Depurador y probador de regex](https://www.regex101.com/)
- [Tutorial de regex](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

{% endtab %}
{% tab Hora %}

Los atributos de hora son útiles para almacenar la última vez que se realizó una acción específica, de modo que puedas ofrecer mensajería de reactivación con contenido específico a tus usuarios.

Los filtros de hora que usan fechas relativas (por ejemplo, hace más de 1 día, hace menos de 2 días) miden 1 día como 24 horas. Cualquier campaña que ejecutes usando estos filtros incluirá a todos los usuarios en incrementos de 24 horas. Por ejemplo, `last used app more than 1 day ago` capturará a todos los usuarios que "usaron la aplicación por última vez hace más de 24 horas" desde el momento exacto en que se ejecuta la campaña. Lo mismo se aplica a campañas configuradas con rangos de fechas más largos, por lo que cinco días desde la activación significarán las 120 horas anteriores.

Para segmentar usuarios que tienen un atributo de hora dentro de un rango de tiempo, usa dos filtros de audiencia: `in more than` para el límite inferior e `in less than` para el límite superior. Un solo filtro no puede expresar ambos lados de ese rango. Por ejemplo, para segmentar usuarios con un atributo de hora en las próximas 24 horas (entre ahora y un día a partir de ahora), aplica `in more than 0 days` e `in less than 1 day`.

{% alert warning %}
La última fecha en que ocurrió un evento personalizado o un evento de compra se registra automáticamente y no debe registrarse de nuevo a través de un atributo personalizado de hora.
{% endalert %}

Para los atributos de **hora**, están disponibles las siguientes opciones de segmentación.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada | Ejemplos |
| ---------------------| --------------- | ------------- | -------- |
| Comprobar si el atributo de hora **es anterior a** una **fecha seleccionada**| **BEFORE** | **CALENDAR DATE SELECTOR** | Si este filtro especifica `2024-01-31` y un perfil de usuario tiene una fecha anterior a `2024-1-31`, el usuario coincidirá con este filtro. |
| Comprobar si el atributo de hora **es posterior a** una **fecha seleccionada**| **AFTER** | **CALENDAR DATE SELECTOR** | Si este filtro especifica `2024-01-31` y un perfil de usuario tiene una fecha posterior a `2024-1-31`, el usuario coincidirá con este filtro. |
| Comprobar si el atributo de hora es **hace más de X número** de **días** | **MORE THAN** | **NUMBER OF DAYS AGO** | Si este filtro especifica `7` y un perfil de usuario tiene una fecha de hace más de siete días, el usuario coincidirá con este filtro. |
| Comprobar si el atributo de hora es **hace menos de X número** de **días**| **LESS THAN** | **NUMBER OF DAYS AGO** | Si este filtro especifica `7` y un perfil de usuario tiene una fecha de hace menos de siete días, el usuario coincidirá con este filtro.|
| Comprobar si el atributo de hora es **en más de X número** de **días en el futuro** | **IN MORE THAN** | **NUMBER OF DAYS IN FUTURE** | Si este filtro especifica `7` y un perfil de usuario tiene una fecha de más de siete días en el futuro, el usuario coincidirá con este filtro.|
| Comprobar si el atributo de hora es **en menos de X número** de **días en el futuro** | **IN LESS THAN** | **NUMBER OF DAYS IN FUTURE**  | Si este filtro especifica `7` y un perfil de usuario tiene una fecha de menos de siete días en el futuro, el usuario coincidirá con este filtro.|
| Comprobar si el atributo de hora **existe** en el perfil de un usuario y no es nulo | **IS NOT BLANK** | **N/A** | Si este filtro especifica un atributo de hora que está en un perfil de usuario, el usuario coincidirá con este filtro.|
| Comprobar si el atributo de hora **no existe** en el perfil de un usuario o es nulo | **IS BLANK** | **N/A** | Si este filtro especifica un atributo de hora que no está en un perfil de usuario, el usuario coincidirá con este filtro. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

#### Detalles de atributos de hora {#time-attribute-details}

- Día de evento recurrente
  - Al usar el filtro "Día de evento recurrente" y luego se te solicita seleccionar el "Día del calendario del evento recurrente", si seleccionas `IS LESS THAN` o `IS MORE THAN`, la fecha actual se contará para ese filtro de segmentación.
  - Por ejemplo, si el 10 de marzo de 2020 seleccionaste la fecha del atributo como `LESS THAN ... March 10, 2020`, los atributos se considerarán para los días hasta e incluyendo el 10 de marzo de 2020.
- Hace menos de X días: el filtro "Hace menos de X días" incluye fechas entre hace X días y la fecha/hora actual.
- En menos de X días en el futuro: incluye fechas entre la fecha/hora actual y X días en el futuro.

{% endtab %}
{% tab Objetos %}

Puedes usar atributos personalizados anidados para enviar objetos como tipo de datos para atributos personalizados. Para más información, consulta [Atributos personalizados anidados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).

{% endtab %}
{% tab Matrices de objetos %}

Usa una matriz de objetos para agrupar atributos relacionados. Para más detalles, consulta [Matriz de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects).

{% endtab %}
{% endtabs %}

Puedes cambiar el tipo de datos de tu atributo personalizado, pero debes tener en cuenta los impactos. Consulta [Cambiar el tipo de datos de un atributo personalizado o evento](#changing-custom-attribute-or-event-data-type) para más información.

### Operadores consolidados {#consolidated-operators}

Hemos consolidado la lista de operadores disponibles para usar en filtros de atributos, filtros de atributos personalizados y filtros de atributos personalizados anidados. Si tienes filtros existentes que usan estos operadores, se actualizarán automáticamente para usar los nuevos operadores.

| Tipo de datos | Operador anterior | Nuevo operador | Valor |
| --- | --- | --- | --- |
| Cadena | equals | is any of | Al menos 1 valor |
| Cadena | does not equal | is none of | Al menos 1 valor |
| Matriz | includes value | includes any of | Al menos 1 valor |
| Matriz | doesn't include value | includes none of | Al menos 1 valor |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Consolidated operators #consolidated-operators" }

## Tipos de datos de propiedades del evento {#event-property-data-types}

Cuando registras un evento, puedes adjuntar información adicional (por ejemplo, nombre del producto o precio) como propiedades del evento. Cada propiedad tiene un nombre y un valor. Los valores de las propiedades del evento admiten los tipos de datos de la tabla de [Definiciones](#definitions) (Hora se etiqueta como "Datetime" en las propiedades del evento).

### Formato esperado {#expected-format}

Los valores de las propiedades se envían como un objeto: las claves son los nombres de las propiedades y los valores son los valores de las propiedades. Los nombres de las propiedades deben ser cadenas no vacías, de 255 caracteres o menos, sin signos de dólar iniciales (`$`).

Reglas específicas de las propiedades del evento:

- **Hora (Datetime):** Usa el formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) o `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. No es compatible dentro de matrices.
- **Matriz:** Las fechas y horas no son compatibles dentro de matrices.
- **Objeto anidado:** Consulta [Objetos anidados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).
- **Carga útil:** Los objetos de propiedades del evento que contienen valores de matriz u objeto pueden tener hasta 102.400 bytes (100&nbsp;KiB).

Puedes cambiar el tipo de datos de tu propiedad de evento personalizado, pero ten en cuenta los impactos de [cambiar los tipos de datos](#changing-custom-attribute-or-event-data-type) después de que se hayan recopilado datos.

Para conocer el comportamiento completo de las propiedades del evento, las claves reservadas y el uso en desencadenantes y personalización, consulta [Propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties).

## Eventos de compra e ingresos {#purchase-events-and-revenue}

Los datos de compras e ingresos se registran a través de [eventos de compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) o eventos recomendados de comercio electrónico.

{% alert note %}
Los eventos recomendados tienen esquemas predefinidos con tipos de datos establecidos. Para más detalles, consulta [Eventos recomendados de comercio electrónico]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events).
{% endalert %}

Registrar eventos de compra establece el valor de duración del ciclo de vida (LTV) para cada perfil de usuario, y estos datos se pueden ver en la página de ingresos en series temporales. Puedes segmentar por dinero gastado, fecha de última compra, número de compras en un período de tiempo y más.

### Tipos de datos de propiedades de eventos de compra {#purchase-event-property-data-types}

Los valores de las propiedades de eventos de compra (el objeto `properties` en una compra) admiten los tipos de datos de la tabla de [Definiciones](#definitions), con la misma estructura y reglas de nomenclatura que las [propiedades del evento](#expected-format).

{% include data_activation/purchase_event_property_data_types.md %}

Para el esquema completo del objeto de compra y ejemplos, consulta [Objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object). Para registrar eventos de compra, filtros de segmentación y detalles completos, consulta [Eventos de compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events).

## Cambiar el tipo de datos de un atributo personalizado o evento {#changing-custom-attribute-or-event-data-type}

Para cambiar el tipo de datos de un atributo personalizado o evento:

1. Ve a **Data Settings** y selecciona **Custom Attributes** o **Custom Events**.
2. Busca tu atributo o evento en la lista y selecciona <i class="fa fa-ellipsis-v" aria-hidden="true"></i> **Más acciones**.
3. Selecciona un nuevo **Tipo de datos** en el desplegable.
4. Selecciona **Guardar**.

Si cambias el tipo de datos de un atributo personalizado o evento (por ejemplo, cambiar `time` a `string`), ten en cuenta lo siguiente:

- **Los filtros no se actualizan automáticamente.** Los Segments, las campañas, los Canvas u otras ubicaciones que usen el atributo o evento modificado no se actualizan. Antes de cambiar el tipo de datos, detén cualquier campaña o Canvas que use el atributo en Segments o filtros, y elimina el atributo de los filtros que lo referencian.
- **Los datos de usuario existentes no se actualizan retroactivamente.** Si el atributo modificado estaba en un perfil de usuario antes del cambio, ese valor permanece con el tipo de datos anterior. Los usuarios pueden salir de Segments que contienen el atributo modificado porque el filtro busca el nuevo tipo de datos. Actualiza esos perfiles de usuario (por ejemplo, con el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)) para que coincidan con el nuevo tipo y vuelvan a entrar en el Segment si es necesario.
- **Los nuevos datos deben coincidir con el nuevo tipo.** Las llamadas a la API que envíen el tipo de datos anterior para el atributo modificado no se aceptan. Envía el nuevo tipo de datos.

{% alert important %}
La capacidad de evitar que la detección automática actualice el tipo de datos del atributo personalizado está actualmente en acceso anticipado. Ponte en contacto con tu administrador de éxito de cliente si te interesa participar.
{% endalert %}

## Tipos de datos de catálogos {#catalog-data-types}

Los catálogos admiten los tipos enumerados en la tabla de [Definiciones](#definitions). La siguiente tabla enumera cada tipo, cómo se puede crear o actualizar, y el formato y ejemplos.

| Tipo de datos | Descripción | Disponible mediante carga CSV | Disponible mediante API y CDI |
| --- | --- | --- | --- |
| Cadena | Una secuencia de caracteres (por ejemplo, nombres, descripciones, ID). | ✅ Sí | ✅ Sí |
| Número | Un valor numérico, ya sea entero o decimal (por ejemplo, precios, cantidades, calificaciones). | ✅ Sí | ✅ Sí |
| Booleano | Un valor `true` o `false`. | ✅ Sí | ✅ Sí |
| Hora | Fecha y hora en formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) o marca de tiempo Unix en segundos. | ✅ Sí | ✅ Sí |
| Objeto JSON (Objeto) | Objeto anidado con pares clave-valor. Se muestra en la plataforma pero solo se puede crear o actualizar a través de la API o CDI. | ❌ No | ✅ Sí |
| Matriz de cadenas (Matriz) | Una lista de cadenas. Se muestra en la plataforma pero solo se puede crear o actualizar a través de la API o CDI. Máximo de 100 elementos. | ❌ No | ✅ Sí |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tipos de datos de catálogos #catalog-data-types" }

### Formato y ejemplos {#format-and-examples}

| Tipo de datos | Formato | Ejemplo |
| --- | --- | --- |
| Cadena | Texto | <code>"Hello World"</code> |
| Hora | ISO 8601 o marca de tiempo Unix (segundos) | <code>"2024-03-15T14:30:00Z"</code> |
| Booleano | <code>true</code> o <code>false</code> | <code>true</code> |
| Número | Entero o decimal | <code>42</code> o <code>19.99</code> |
| Objeto | Objeto JSON | <code>{"key": "value", "price": 10}</code> |
| Matriz | Matriz de cadenas | <code>["red", "blue", "green"]</code> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Formato y ejemplos" }

Para crear y actualizar catálogos, consulta [Crear un catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create).