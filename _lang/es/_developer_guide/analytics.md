---
nav_title: Análisis
article_title: Acerca del análisis del SDK de Braze
page_order: 2.6
description: "Obtén información sobre el análisis del SDK de Braze para comprender mejor qué datos recopila Braze, la diferencia entre eventos personalizados y atributos personalizados, y las prácticas recomendadas para gestionar los análisis."
platform:
  - Android
  - Swift
  - Web
  - Cordova
  - FireOS
  - Flutter
  - React Native
  - Roku
  - Unity
  - .NET MAUI
---

# Análisis {#analytics}

> Obtén información sobre el análisis del SDK de Braze para comprender mejor qué datos recopila Braze, la diferencia entre eventos personalizados y atributos personalizados, y las prácticas recomendadas para gestionar los análisis.

{% alert tip %}
Durante la implementación de Braze, asegúrate de hablar sobre los objetivos de marketing con tu equipo, para que puedas decidir mejor qué datos deseas rastrear y cómo deseas rastrearlos con Braze. Para ver un ejemplo, consulta nuestro caso de estudio [sobre aplicaciones de taxi/transporte compartido](#example-case) al final de esta guía.
{% endalert %}

## Datos recopilados automáticamente {#automatically-collected-data}

Ciertos datos de usuario se recopilan automáticamente a través de nuestro SDK, por ejemplo, primera vez que se usó la aplicación, última vez que se usó la aplicación, recuento total de sesiones, sistema operativo del dispositivo, etc. Si sigues nuestras guías de integración para implementar nuestros SDK, podrás aprovechar esta [recopilación de datos predeterminada]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection). Revisar esta lista puede ayudarte a evitar almacenar la misma información sobre los usuarios más de una vez. Con la excepción del inicio y fin de sesión, todos los demás datos rastreados automáticamente no cuentan para tu uso de puntos de datos.

Consulta nuestro artículo [Introducción al SDK]({{site.baseurl}}/developer_guide/getting_started/sdk_overview) para incluir en la lista de permitidos los procesos que bloquean la recopilación predeterminada de ciertos elementos de datos.

## Eventos personalizados {#custom-events}

Los eventos personalizados son acciones realizadas por tus usuarios; son los más adecuados para hacer seguimiento de las interacciones de alto valor de los usuarios con tu aplicación. Registrar un evento personalizado puede desencadenar cualquier cantidad de campañas de seguimiento con retrasos configurables, y habilita los siguientes filtros de segmentación en torno a la frecuencia y la antigüedad de ese evento:

| Opciones de segmentación | Filtro desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprobar si el evento personalizado ha ocurrido **más de X veces** | **MÁS DE** | **NÚMERO** |
| Comprobar si el evento personalizado ha ocurrido **menos de X veces** | **MENOS DE** | **NÚMERO** |
| Comprobar si el evento personalizado ha ocurrido **exactamente X veces** | **EXACTAMENTE** | **NÚMERO** |
| Comprobar si el evento personalizado ocurrió por última vez **después de la fecha X** | **DESPUÉS DE** | **HORA** |
| Comprobar si el evento personalizado ocurrió por última vez **antes de la fecha X** | **ANTES DE** | **HORA** |
| Comprobar si el evento personalizado ocurrió por última vez **hace más de X días** | **MÁS DE** | **NÚMERO DE DÍAS ATRÁS** (número positivo) |
| Comprobar si el evento personalizado ocurrió por última vez **hace menos de X días** | **MENOS DE** | **NÚMERO DE DÍAS ATRÁS** (número positivo) |
| Comprobar si el evento personalizado ocurrió **más de X (máx. = 50) veces** | **MÁS DE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
| Comprobar si el evento personalizado ocurrió **menos de X (máx. = 50) veces** | **MENOS DE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
| Comprobar si el evento personalizado ocurrió **exactamente X (máx. = 50) veces** | **EXACTAMENTE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Eventos personalizados" }

Braze registra la cantidad de veces que estos eventos han ocurrido, así como la última vez que cada usuario los realizó, para fines de segmentación. En la página de análisis de **Custom Events**, puedes ver de forma agregada con qué frecuencia ocurre cada evento personalizado, así como por segmento a lo largo del tiempo para un análisis más detallado. Esto es particularmente útil para ver cómo tus campañas han afectado la actividad de eventos personalizados, observando las líneas grises que Braze superpone en la serie temporal para indicar la última vez que se envió una campaña.

![Un gráfico de análisis de eventos personalizados que muestra estadísticas sobre usuarios que agregaron una tarjeta de crédito e hicieron una búsqueda durante un período de treinta días.]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

{% alert note %}
Los [atributos personalizados incrementales]({{site.baseurl}}/api/endpoints/messaging) se pueden usar para mantener un contador de una acción del usuario similar a un evento personalizado. Sin embargo, no podrás ver los datos de atributos personalizados en una serie temporal. Las acciones de usuario que no necesitan analizarse en series temporales deben registrarse mediante este método.
{% endalert %}

### Almacenamiento de eventos personalizados {#custom-event-storage}

Todos los datos del perfil de usuario (eventos personalizados, atributos personalizados, datos personalizados) se almacenan mientras esos perfiles estén activos.

### Propiedades de eventos personalizados {#custom-event-properties}

Con las propiedades de eventos personalizados, Braze te permite establecer propiedades en eventos personalizados y compras. Estas propiedades se pueden usar para calificar aún más las condiciones de activación, aumentar la personalización en la mensajería y generar análisis más sofisticados a través de la exportación de datos sin procesar. Los valores de las propiedades pueden ser cadenas, números, booleanos u objetos de tiempo. Sin embargo, los valores de las propiedades no pueden ser objetos de tipo array.

Por ejemplo, si una aplicación de comercio electrónico quisiera enviar un mensaje a un usuario cuando abandona su carrito, podría mejorar adicionalmente su público objetivo y permitir una mayor personalización de la campaña añadiendo una propiedad de evento personalizado del `cart_value` de los carritos de los usuarios.

![Un ejemplo de evento personalizado que enviará una campaña a un usuario que ha abandonado su carrito y dejó el valor del carrito en más de 100 y menos de 200.]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png")

Las propiedades de eventos personalizados también se pueden usar para la personalización dentro de la plantilla de mensajería. Cualquier campaña que use [entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) con un evento desencadenante puede usar las propiedades de eventos personalizados de ese evento para la personalización de la mensajería. Si una aplicación de juegos quisiera enviar un mensaje a los usuarios que completaron un nivel, podría personalizar aún más el mensaje con una propiedad del tiempo que les tomó a los usuarios completar ese nivel. En este ejemplo, el mensaje se personaliza para tres segmentos diferentes usando [lógica condicional]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic). La propiedad de evento personalizado llamada ``time_spent`` se puede incluir en el mensaje llamando a ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Congratulations on beating that level so fast! Check out our online portal where you can play against top players from around the world!
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Talk to villagers for essential tips on how to beat levels!
{% endif %}
```
{% endraw %}

Las propiedades de eventos personalizados están diseñadas para ayudarte a personalizar tu mensajería o crear campañas granulares de entrega basada en acciones. Si deseas crear segmentos basados en la frecuencia y la antigüedad de las propiedades de eventos, ponte en contacto con tu administrador de éxito de cliente o con nuestro equipo de soporte.

## Atributos personalizados {#custom-attributes}

Los atributos personalizados son herramientas extraordinariamente flexibles que te permiten dirigirte a los usuarios con mayor especificidad de la que tendrías con los atributos estándar. Los atributos personalizados son ideales para almacenar información específica de tu marca sobre tus usuarios. Ten en cuenta que no almacenamos información de series temporales para los atributos personalizados, por lo que no obtendrás gráficos basados en ellos como en el ejemplo anterior de eventos personalizados.

### Almacenamiento de atributos personalizados {#custom-attribute-storage}

Todos los datos del perfil de usuario (eventos personalizados, atributos personalizados, datos personalizados) se almacenan mientras esos perfiles estén activos.

### Tipos de datos de atributos personalizados {#custom-attribute-data-types}

Los siguientes tipos de datos pueden almacenarse como atributos personalizados:

#### Cadenas (caracteres alfanuméricos) {#strings-alphanumeric-characters}

Los atributos de cadena son útiles para almacenar la entrada del usuario, como una marca favorita, un número de teléfono o la última cadena de búsqueda dentro de tu aplicación. Los atributos de cadena están sujetos a las [restricciones de longitud](#length-constraints) para datos personalizados (479 bytes; aproximadamente 479 caracteres de un solo byte o aproximadamente 160 caracteres para scripts multibyte como el japonés).

La siguiente tabla describe las opciones de segmentación disponibles para los atributos de cadena.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprobar si el atributo de cadena **coincide exactamente** con una cadena introducida | **EQUALS** | **STRING** |
| Comprobar si el atributo de cadena **coincide parcialmente** con una cadena introducida **O** una expresión regular | **MATCHES REGEX** | **STRING** **O** **REGULAR EXPRESSION** |
| Comprobar si el atributo de cadena **no coincide parcialmente** con una cadena introducida **O** una expresión regular | **DOES NOT MATCH REGEX** | **STRING** **O** **REGULAR EXPRESSION** |
| Comprobar si el atributo de cadena **no coincide** con una cadena introducida | **DOES NOT EQUAL** | **STRING** |
| Comprobar si el atributo de cadena **existe** en el perfil de un usuario | **IS BLANK** | **N/A** |
| Comprobar si el atributo de cadena **no existe** en el perfil de un usuario | **IS NOT BLANK** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cadenas (caracteres alfanuméricos)" }

{% alert important %}
Al segmentar con el filtro **DOES NOT MATCH REGEX**, es necesario que ya exista un atributo personalizado con un valor asignado en ese perfil de usuario. Braze sugiere utilizar la lógica "OR" para comprobar si un atributo personalizado está en blanco con el fin de dirigirte correctamente a los usuarios.
{% endalert %}

{% alert tip %}
Para más información sobre cómo utilizar nuestro filtro de expresiones regulares, consulta esta documentación sobre [expresiones regulares compatibles con Perl (PCRE)](http://www.regextester.com/pregsyntax.html).
<br>
Más recursos sobre regex:
- [Regex con Braze]({{site.baseurl}}/user_guide/audience/segments/regex)
- [Depurador y probador de regex](https://regex101.com/)
- [Tutorial de regex](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

#### Arrays {#arrays}

Los atributos de array son útiles para almacenar listas de información relacionada sobre tus usuarios. Por ejemplo, almacenar las últimas 100 piezas de contenido que un usuario vio dentro de un array permitiría una segmentación por intereses específicos.

Los arrays de atributos personalizados son conjuntos unidimensionales; no se admiten arrays multidimensionales. **Añadir un elemento a un array de atributos personalizados lo agrega al final del array, a menos que ya esté presente, en cuyo caso se mueve de su posición actual al final del array.** Por ejemplo, si se importa un array `['hotdog','hotdog','hotdog','pizza']`, se mostrará en el atributo de array como `['hotdog', 'pizza']` porque solo se admiten valores únicos.

Si el array contiene su cantidad máxima de elementos, el primer elemento se descartará y el nuevo elemento se añadirá al final. La siguiente lista muestra un ejemplo de código que ilustra el comportamiento del array en el SDK web:

```js
var abUser = appboy.getUser();
// initialize array for this user, assuming max length of favorite_foods is set to 4.
abUser.setCustomUserAttribute('favorite_foods', ['pizza', 'wings', 'pasta']); // => ['pizza', 'wings', 'pasta']
abUser.addToCustomAttributeArray('favorite_foods', 'fries'); // => ['pizza', 'wings', 'pasta', 'fries']
abUser.addToCustomAttributeArray('favorite_foods', 'pizza'); // => ['wings', 'pasta', 'fries', 'pizza']
abUser.addToCustomAttributeArray('favorite_foods', 'ice cream'); // => ['pasta', 'fries', 'pizza', 'ice cream']
```

La cantidad predeterminada y máxima de elementos en un array es 500. Puedes actualizar la cantidad máxima de arrays en el panel de Braze, en **Data Settings** > **Custom Attributes**. Los arrays que excedan la cantidad máxima de elementos se truncan para contener la cantidad máxima de elementos.

{% alert note %}
Si un atributo personalizado de array aparece en un perfil de usuario pero no muestra valores, comprueba la **Max Length** del atributo en **Data Settings** > **Custom Attributes**. Una **Max Length** de `0` impide que los valores se muestren en el perfil. Para los pasos de solución de problemas, consulta [Tipos de datos de atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#arrays).
{% endalert %}

La siguiente tabla describe las opciones de segmentación disponibles para los atributos de array.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprobar si el atributo de array **incluye un valor que coincide exactamente** con un valor introducido | **INCLUDES VALUE** | **STRING** |
| Comprobar si el atributo de array **no incluye un valor que coincide exactamente** con un valor introducido | **DOESN'T INCLUDE VALUE** | **STRING** |
| Comprobar si el atributo de array **contiene un valor que coincide parcialmente** con un valor introducido **O** una expresión regular | **MATCHES REGEX** | **STRING** **O** **REGULAR EXPRESSION** |
| Comprobar si el atributo de array **tiene algún valor** | **HAS A VALUE** | **N/A** |
| Comprobar si el atributo de array **está vacío** | **IS EMPTY** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Arrays" }

{% alert note %}
Utilizamos [expresiones regulares compatibles con Perl (PCRE)](http://www.regextester.com/pregsyntax.html).
{% endalert %}

#### Fechas {#dates}

Los atributos de tiempo son útiles para almacenar la última vez que se realizó una acción específica, de modo que puedas ofrecer mensajes de reactivación con contenido específico a tus usuarios.

{% alert note %}
La última fecha en que ocurrió un evento personalizado o un evento de compra se registra automáticamente y no debe registrarse de forma duplicada mediante un atributo de tiempo personalizado.
{% endalert %}

Los filtros de fecha que utilizan fechas relativas (por ejemplo, hace más de 1 día, hace menos de 2 días) miden 1 día como 24 horas. Cualquier campaña que ejecutes con estos filtros incluirá a todos los usuarios en incrementos de 24 horas. Por ejemplo, "última vez que usó la aplicación hace más de 1 día" capturará a todos los usuarios que "usaron la aplicación por última vez hace más de 24 horas" desde el momento exacto en que se ejecuta la campaña. Lo mismo se aplica a las campañas configuradas con rangos de fechas más largos, por lo que cinco días desde la activación significarán las 120 horas anteriores.

La siguiente tabla describe las opciones de segmentación disponibles para los atributos de tiempo.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprobar si el atributo de tiempo **es anterior** a una **fecha seleccionada** | **BEFORE** | **CALENDAR DATE SELECTOR** |
| Comprobar si el atributo de tiempo **es posterior** a una **fecha seleccionada** | **AFTER** | **CALENDAR DATE SELECTOR** |
| Comprobar si el atributo de tiempo es **más de X número** de **días atrás** | **MORE THAN** | **NUMBER OF DAYS AGO** |
| Comprobar si el atributo de tiempo es **menos de X número** de **días atrás** | **LESS THAN** | **NUMBER OF DAYS AGO** |
| Comprobar si el atributo de tiempo es **en más de X número** de **días en el futuro** | **IN MORE THAN** | **NUMBER OF DAYS IN FUTURE** |
| Comprobar si el atributo de tiempo es **menos de X número** de **días en el futuro** | **IN LESS THAN** | **NUMBER OF DAYS IN FUTURE**  |
| Comprobar si el atributo de tiempo **existe** en el perfil de un usuario | **BLANK** | **N/A** |
| Comprobar si el atributo de tiempo **no existe** en el perfil de un usuario | **IS NOT BLANK** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fechas" }

#### Números {#integers}

Los atributos numéricos tienen una amplia variedad de casos de uso. Los atributos personalizados de números incrementales son útiles para almacenar la cantidad de veces que se ha producido una acción o evento determinado. Los números estándar tienen todo tipo de usos, como registrar la talla de zapato, la talla de cintura o la cantidad de veces que un usuario ha visto una determinada característica o categoría de producto.

{% alert note %}
El dinero gastado no debe registrarse con este método. Más bien, debe registrarse a través de nuestros [métodos de compra]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview#purchase-events--revenue-tracking).
{% endalert %}

La siguiente tabla describe las opciones de segmentación disponibles para los atributos numéricos.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprobar si el atributo numérico **es mayor que** un **número** | **MORE THAN** | **NUMBER** |
| Comprobar si el atributo numérico **es menor que** un **número** | **LESS THAN** | **NUMBER** |
| Comprobar si el atributo numérico **es exactamente** un **número** | **EXACTLY** | **NUMBER** |
| Comprobar si el atributo numérico **no es igual a** un **número** | **DOES NOT EQUAL** | **NUMBER** |
| Comprobar si el atributo numérico **existe** en el perfil de un usuario | **EXISTS** | **N/A** |
| Comprobar si el atributo numérico **no existe** en el perfil de un usuario | **DOES NOT EXIST** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Números #integers" }

#### Booleanos (verdadero/falso) {#booleans-truefalse}

Los atributos booleanos son útiles para almacenar estados de suscripción y otros datos binarios simples sobre tus usuarios. Las opciones de entrada que proporcionamos te permiten encontrar usuarios que tienen una variable explícitamente establecida como booleana, además de aquellos que aún no tienen ningún registro de ese atributo.

La siguiente tabla describe las opciones de segmentación disponibles para los atributos booleanos.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprobar si el valor booleano **es** | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET** o **FALSE OR NOT SET** |
| Comprobar si el valor booleano **existe** en el perfil de un usuario | **EXISTS**  | **N/A** |
| Comprobar si el valor booleano **no existe** en el perfil de un usuario | **DOES NOT EXIST**  | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Booleanos (verdadero/falso)" }

## Eventos de compra / seguimiento de ingresos {#purchase-events-revenue-tracking}

Usar nuestros métodos de compra para registrar compras dentro de la aplicación establece el valor del ciclo de vida (LTV) para cada perfil de usuario individual. Estos datos se pueden ver en nuestra página de ingresos en gráficos de series temporales.

La siguiente tabla describe las opciones de segmentación disponibles para los eventos de compra.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprobar si el total de dólares gastados **es mayor que** un **número** | **GREATER THAN** | **NUMBER** |
| Comprobar si el total de dólares gastados **es menor que** un **número** | **LESS THAN** | **NUMBER** |
| Comprobar si el total de dólares gastados **es exactamente** un **número** | **EXACTLY** | **NUMBER** |
| Comprobar si la última compra ocurrió **después de la fecha X** | **AFTER** | **TIME** |
| Comprobar si la última compra ocurrió **antes de la fecha X** | **BEFORE** | **TIME** |
| Comprobar si la última compra ocurrió **hace más de X días** | **MORE THAN** | **TIME** |
| Comprobar si la última compra ocurrió **hace menos de X días** | **LESS THAN** | **TIME** |
| Comprobar si la compra ocurrió **más de X (máx. = 50) veces** | **MORE THAN** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
| Comprobar si la compra ocurrió **menos de X (máx. = 50) veces** | **LESS THAN** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
| Comprobar si la compra ocurrió **exactamente X (máx. = 50) veces** | **EXACTLY** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Eventos de compra / seguimiento de ingresos" }

{% alert note %}
Si deseas segmentar por el número de veces que ha ocurrido una compra específica, también debes registrar esa compra individualmente como un [atributo personalizado incremental](#integers).
{% endalert %}

## Caso de uso de aplicación de taxi/transporte compartido {#example-case}

Para este ejemplo, consideremos una aplicación de transporte compartido que quiere decidir qué datos de usuario recopilar. Las siguientes preguntas y el proceso de lluvia de ideas son un gran modelo a seguir por los equipos de marketing y desarrollo. Al final de este ejercicio, ambos equipos deberían tener una comprensión sólida de qué eventos y atributos personalizados tiene sentido recopilar para ayudar a cumplir su objetivo.

**Pregunta del caso nº 1: ¿Cuál es el objetivo?**

Su objetivo es sencillo: quieren que los usuarios pidan taxis a través de su aplicación.

**Pregunta del caso nº 2: ¿Cuáles son los pasos intermedios en el camino hacia ese objetivo desde la instalación de la aplicación?**

1. Necesitan que los usuarios inicien el proceso de registro y rellenen sus datos personales.
2. Necesitan que los usuarios completen y verifiquen el proceso de registro introduciendo un código en la aplicación que reciben por SMS.
3. Tienen que intentar pedir un taxi.
4. Para pedir un taxi, debe haber uno disponible cuando lo busquen.

Estas acciones podrían entonces etiquetarse como los siguientes eventos personalizados:

- Inicio del registro
- Registro completado
- Solicitudes de taxi exitosas
- Solicitudes de taxi fallidas

Después de implementar los eventos, ahora puedes ejecutar las siguientes campañas:

1. Envía mensajes a los usuarios que iniciaron el registro, pero no desencadenaron el evento de registro completado en un plazo de tiempo determinado.
2. Envía mensajes de felicitación a los usuarios que completen el registro.
3. Envía disculpas y crédito promocional a los usuarios que hayan tenido solicitudes de taxi fallidas que no hayan ido seguidas de una solicitud de taxi exitosa en un plazo de tiempo determinado.
4. Envía promociones a usuarios avanzados con muchas solicitudes de taxi exitosas para agradecerles su fidelización.

¡Y muchas más!

**Pregunta del caso nº 3: ¿Qué otra información podríamos querer saber sobre nuestros usuarios para orientar nuestra mensajería?**

- ¿Tienen o no créditos promocionales?
- ¿La calificación promedio que dan a sus conductores?
- ¿Códigos promocionales únicos para el usuario?

Estas características podrían etiquetarse como los siguientes atributos personalizados:

- Saldo de crédito promocional (tipo decimal)
- Calificación promedio de los conductores (tipo numérico)
- Código promocional único (tipo de cadena)

Añadir estos atributos te permitiría enviar campañas a los usuarios, por ejemplo:

1. Recordar a los usuarios que no se han conectado en siete días, pero que tienen un crédito promocional, que su crédito existe y que deberían volver a la aplicación para utilizarlo.
2. Enviar mensajes a los usuarios que dan calificaciones bajas a los conductores para obtener opiniones directas de los clientes y saber por qué no disfrutaron de sus viajes.
3. Utilizar nuestras [características de plantilla y personalización de mensajes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) para incluir el atributo de código promocional único en la mensajería dirigida a los usuarios.

## Buenas prácticas {#best-practices}

### Buenas prácticas generales {#general-best-practices}

#### Usa propiedades del evento {#use-event-properties}

- Nombra un evento personalizado con algo que describa una acción que realiza un usuario.
- Haz un uso generoso de las propiedades de eventos personalizados para representar datos importantes sobre un evento.
- Por ejemplo, en lugar de capturar un evento personalizado separado para ver cada una de 50 películas diferentes, sería más eficaz capturar simplemente ver una película como un evento y tener una propiedad del evento que incluya el nombre de la película.

### Buenas prácticas de desarrollo {#development-best-practices}

#### Establece ID de usuario para cada usuario {#set-user-ids-for-every-user}

Los ID de usuario deben establecerse para cada uno de tus usuarios. Estos deben ser inmutables y accesibles cuando un usuario abre la aplicación. **Recomendamos encarecidamente** proporcionar este identificador, ya que te permitirá:

- Hacer seguimiento de tus usuarios en distintos dispositivos y plataformas, mejorando la calidad de tus datos de comportamiento y demográficos.
- Importar datos sobre tus usuarios utilizando nuestra [API de datos de usuario]({{site.baseurl}}/api/endpoints/user_data).
- Dirigirte a usuarios específicos con nuestra [API de mensajería]({{site.baseurl}}/api/endpoints/messaging) tanto para mensajes generales como transaccionales.

Los ID de usuario deben tener menos de 512 caracteres y deben ser privados y no fáciles de obtener (por ejemplo, no una dirección de correo electrónico o un nombre de usuario en texto plano). Si dicho identificador no está disponible, Braze asignará un identificador único a tus usuarios, pero carecerás de las capacidades enumeradas para los ID de usuario. Debes evitar establecer ID de usuario para usuarios para los que no dispongas de un identificador único vinculado a ellos como individuo. Pasar un identificador de dispositivo no ofrece ningún beneficio en comparación con el seguimiento automático de usuarios anónimos que Braze ofrece de forma predeterminada. Los siguientes son algunos ejemplos de ID de usuario adecuados e inadecuados.

Buenas opciones para ID de usuario:

- Dirección de correo electrónico con hash o nombre de usuario único
- Identificador único de base de datos

Estos no deben usarse como ID de usuario:

- ID de dispositivo
- Número aleatorio o ID de sesión
- Cualquier ID no único
- Dirección de correo electrónico
- ID de usuario de otro proveedor externo

{% multi_lang_include alerts/important_alerts.md alert='SDK auth' %}

#### Asigna nombres legibles a los eventos y atributos personalizados {#give-custom-events-and-attributes-readable-names}

Imagina que eres un especialista en marketing que empieza a usar Braze uno o dos años después de la implementación; leer una lista desplegable llena de nombres como "usr_no_acct" sin más contexto puede resultar intimidante. Dar a tus eventos y atributos nombres identificables y legibles facilitará las cosas a todos los usuarios de tu plataforma. Ten en cuenta las siguientes buenas prácticas:

- No comiences un evento personalizado con un carácter numérico. La lista desplegable se ordena alfabéticamente y comenzar con un carácter numérico dificulta la segmentación por el filtro de tu elección.
- Intenta no usar abreviaturas oscuras o jerga técnica cuando sea posible.
  - Ejemplo: `usr_ctry` puede estar bien como nombre de variable para el país de un usuario dentro de un fragmento de código, pero el atributo personalizado debe enviarse a Braze como algo similar a `user_country` para aportar claridad a un especialista en marketing que use el panel más adelante.

#### Solo registra atributos cuando cambien {#only-log-attributes-when-they-change}

Contamos cada atributo enviado a Braze como un punto de datos, incluso si el atributo enviado contiene el mismo valor que el guardado previamente. Registrar datos solo cuando cambian ayuda a evitar el uso redundante de puntos de datos y favorece una experiencia más fluida al evitar llamadas a la API innecesarias.

#### Evita generar nombres de eventos de forma programática {#avoid-programmatically-generating-event-names}

Si estás creando constantemente nuevos nombres de eventos, será imposible segmentar a tus usuarios de forma significativa. En general, debes capturar eventos genéricos ("Vio un video" o "Leyó un artículo") en lugar de eventos muy específicos como ("Vio Gangnam Style" o "Leyó artículo: Los 10 mejores lugares para almorzar en Midtown Manhattan"). Los datos específicos sobre el evento deben incluirse como una propiedad del evento, no como parte del nombre del evento.

### Limitaciones y restricciones técnicas {#technical-limitations-and-constraints}

Ten en cuenta las siguientes limitaciones y restricciones al implementar eventos personalizados:

#### Restricciones de longitud {#length-constraints}

Braze aplica un límite de longitud en bytes (479 bytes) para los nombres de eventos personalizados, los nombres de atributos personalizados (claves) y los valores de cadena de eventos personalizados. Los valores que excedan este límite se truncan. Expresado en caracteres, esto equivale aproximadamente a 479 caracteres de un solo byte (por ejemplo, ASCII), o aproximadamente 160 caracteres para scripts multibyte como el japonés (asumiendo unos 3 bytes por carácter en UTF-8). Idealmente, mantén los nombres y valores lo más cortos posible para mejorar el rendimiento de red y batería de tu aplicación; si es posible, limítalos a 50 caracteres.

#### Restricciones de contenido {#content-constraints}
El siguiente contenido se recortará programáticamente de tus atributos y eventos. Ten cuidado de no usar lo siguiente:

- Espacios en blanco al inicio y al final
- Saltos de línea
- Todos los caracteres que no sean dígitos dentro de los números de teléfono
  - Ejemplo: "(732) 178-1038" se condensará a "7321781038"
- Los caracteres que no sean espacios en blanco deben convertirse en espacios
- $ no debe usarse como prefijo para ningún evento personalizado
- Cualquier valor de codificación UTF-8 no válido
  -  "My \x80 Field" se condensaría a "My Field"

#### Claves reservadas {#reserved-keys}

Las siguientes claves están reservadas y no pueden usarse como propiedades de eventos personalizados:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

#### Definiciones de valores {#value-definitions}

- Los valores enteros son de 64 bits
- Los decimales tienen 15 dígitos decimales de forma predeterminada

### Análisis de un campo de nombre genérico {#parsing-a-generic-name-field}

Si solo existe un único campo de nombre genérico para un usuario (por ejemplo, 'JohnDoe'), puedes asignar este título completo al atributo de nombre de tu usuario. Además, puedes intentar separar tanto el nombre como el apellido del usuario usando espacios, pero este último método conlleva el riesgo potencial de nombrar incorrectamente a algunos de tus usuarios.