---
nav_title: Atributos personalizados
article_title: Atributos personalizados
page_order: 1
page_type: reference
description: "Esta página describe los atributos personalizados y explica los distintos tipos de datos de atributos personalizados."
search_rank: 1
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Atributos personalizados

> Esta página cubre los atributos personalizados, que son una colección de rasgos únicos de tus usuarios. Los atributos personalizados son ideales para almacenar atributos sobre tus usuarios o información sobre acciones de bajo valor dentro de tu aplicación. 

Cuando se almacenan en Braze, los atributos personalizados se pueden usar para crear segmentos de audiencia y personalizar la mensajería con Liquid. Ten en cuenta que Braze no almacena información de series temporales para los atributos personalizados, por lo que no puedes obtener gráficos basados en ellos como sí puedes hacerlo con los eventos personalizados.

## Casos de uso

Algunos casos de uso comunes de atributos personalizados incluyen:

- Segmentar y suprimir audiencias segmentando usuarios según rasgos como nivel de fidelización, estado de suscripción, idioma preferido o tipo de plan
- Personalizar mensajes con [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) haciendo referencia a atributos como el nombre del usuario, puntos de recompensa o categoría favorita
- Rastrear etapas del ciclo de vida y estados del usuario, como etapa de incorporación, estado de la cuenta o fecha de fin de prueba
- Contar acciones de bajo valor con [atributos numéricos]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#numbers), como incrementar un atributo `feature_views_count` cada vez que un usuario visualiza una característica
- Registrar cuándo ocurrieron por última vez acciones de bajo valor usando [atributos de tiempo]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#time), como `last_support_ticket_at` o `last_password_reset_at`
- Almacenar intereses e historial del usuario como [arrays]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#arrays), como géneros favoritos o contenido visto recientemente, para segmentación basada en intereses
- Almacenar datos de perfil más completos como [objetos]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/) o [arrays de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects/), como preferencias estructuradas o múltiples direcciones guardadas
- Desencadenar mensajes basados en acciones cuando cambia el valor de un atributo usando [desencadenadores de atributos]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers/), como enviar una notificación de subida de nivel cuando cambia el `rewards_tier` de un usuario

## Administrar atributos personalizados {#managing-custom-attributes}

Para crear y administrar atributos personalizados en el dashboard, ve a **Configuración de datos** > **Atributos personalizados**. 

![Cuatro atributos personalizados que son booleanos.]({% image_buster /assets/img/export_custom_attributes.png %})

La columna **Última actualización** muestra la última vez que se editó el atributo personalizado, como cuándo se añadió a la lista de bloqueo o se activó por última vez.

{% alert important %}
Para una segmentación correcta de los mensajes, asegúrate de que el tipo de datos de tu atributo personalizado coincida con el atributo personalizado real. <br><br>Por ejemplo, si `newsletter_subscribed` está definido como una cadena, tu sintaxis Liquid debería verse así: {% raw %}```{% if {{custom_attribute.${newsletter_subscribed}}} == 'true' %}```{% endraw %}. Si `newsletter_subscribed` está definido como Booleano, la sintaxis Liquid no debería tener comillas simples: {% raw %}```{% if {{custom_attribute.${newsletter_subscribed}}} == true %}```{% endraw %}.
{% endalert %}

Desde esta página, puedes ver, administrar, crear o bloquear atributos personalizados existentes. Selecciona el menú junto a un atributo personalizado para las siguientes acciones:

### Lista de bloqueo {#blocklisting}

Puedes bloquear atributos personalizados individuales a través del menú de acciones, o seleccionar y bloquear hasta 100 atributos de forma masiva.

Cuando bloqueas un atributo personalizado:

- No se recopilarán datos futuros para ese atributo.
- Los datos existentes no estarán disponibles a menos que se desbloquee ese atributo.
- Ese atributo no aparecerá en filtros ni gráficos.

Además, si un atributo personalizado bloqueado está actualmente referenciado por filtros o desencadenadores en otras áreas de Braze, aparecerá un modal de advertencia explicando que todas las instancias de los filtros o desencadenadores que lo referencian serán eliminadas y archivadas.

Para más detalles sobre el bloqueo y la eliminación de datos personalizados, consulta [Bloquear datos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).

### Marcar como información de identificación personal (PII)

Los administradores también pueden crear atributos personalizados y marcarlos como PII desde esta página. Estos atributos solo son visibles para administradores y usuarios del dashboard con el permiso "Ver atributos personalizados marcados como PII".

### Añadir descripciones

Puedes añadir una descripción a un atributo personalizado después de crearlo si tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) `Manage Events, Attributes, Purchases`. Selecciona **Editar descripción** para el atributo personalizado e introduce lo que desees, como una nota para tu equipo.

### Añadir etiquetas

Puedes añadir etiquetas a un atributo personalizado después de crearlo si tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) "Manage Events, Attributes, Purchases". Las etiquetas se pueden usar para filtrar la lista de atributos. 

### Eliminar atributos personalizados

Hay dos formas de eliminar atributos personalizados de los perfiles de usuario:

* Selecciona el nombre del atributo personalizado a eliminar en un [paso de Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#removing-custom-attributes).
* Establece el valor `null` en tu solicitud de API al [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track).

### Exportar datos

Para exportar la lista de atributos personalizados como un archivo CSV, selecciona **Exportar todo** en la parte superior de la página. Se generará el archivo CSV y se te enviará un enlace de descarga por correo electrónico.

## Cambiar el tipo de atributo personalizado

### Requisitos previos

El atributo personalizado no debe estar actualmente en uso en ninguna campaña, Canvas o segmento activo. Si intentas cambiar el tipo de datos mientras el atributo aún está referenciado, el dashboard mostrará un error y bloqueará el cambio.

### Cambiar el tipo de datos

1. Detén cualquier campaña o Canvas activo que use el atributo en segmentos o filtros.
2. Elimina el atributo de todos los filtros de segmentos, campañas y Canvas.
3. Ve a **Configuración de datos** > **Atributos personalizados** (o **Eventos personalizados**), busca el atributo y actualízalo al tipo de datos deseado.
4. Actualiza los valores del atributo en los perfiles de usuario existentes para que coincidan con el nuevo tipo de datos (por ejemplo, usando el [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)).
5. Vuelve a aplicar el atributo a los segmentos, campañas y Canvas relevantes, y luego reactiva cualquier campaña o Canvas detenido.

### Cosas a tener en cuenta

- **Los datos de usuario no se actualizan retroactivamente.** Si un perfil de usuario tenía el atributo con el tipo de datos anterior, ese valor permanece sin cambios. El filtro de segmentación busca el nuevo tipo de datos, por lo que los usuarios con el valor anterior quedan excluidos de los segmentos coincidentes hasta que se actualice su perfil.
- **Los nuevos datos deben coincidir con el nuevo tipo de datos.** Después del cambio, las llamadas a la API o los eventos del SDK que envíen el tipo de datos anterior para este atributo no serán aceptados. Solo se ingieren valores que coincidan con el nuevo tipo de datos.
- **Los filtros no se actualizan automáticamente.** Los segmentos y filtros de campañas que referencian el atributo modificado no se actualizan retroactivamente. Debes eliminarlos y volver a añadirlos después del cambio.

## Ver informes de uso

El informe de uso muestra todos los Canvas, campañas y segmentos que utilizan un atributo personalizado específico. Esta lista no incluye usos de Liquid. 

Puedes ver hasta 100 informes de uso a la vez seleccionando las casillas de verificación junto a los atributos personalizados correspondientes y luego seleccionando **Ver informe de uso**.

### Pestaña Valores

Al ver un informe de uso, selecciona la pestaña **Valores** para ver los valores principales de los atributos personalizados seleccionados basados en una muestra de aproximadamente 250,000 usuarios. Ten en cuenta que, dado que los resultados se obtienen de un subconjunto de usuarios, la muestra no incluirá todos los valores existentes. Esto significa que la pestaña **Valores** no debe usarse para solución de problemas ni para casos de uso que requieran incorporar datos de todos los usuarios.

![Informe de uso para atributos personalizados seleccionados con una pestaña "Valores" abierta que muestra un gráfico circular de valores del atributo de país, como "US" y "PR".]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## Establecer atributos personalizados

A continuación se listan los métodos en varias plataformas que se usan para establecer atributos personalizados.

{% details Expandir para ver la documentación por plataforma %}

- [Android y FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [.NET MAUI (anteriormente Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)

{% enddetails %}

## Almacenamiento de atributos personalizados

Todos los datos almacenados en el **perfil de usuario**, incluidos los datos de atributos personalizados, se conservan indefinidamente mientras cada perfil esté [activo]({{site.baseurl}}/user_archival#active-users).

Para una referencia completa de todos los tipos de datos que puedes almacenar como atributos personalizados, incluyendo booleanos, números, cadenas, arrays, tiempo, objetos y arrays de objetos, consulta [Tipos de datos de atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/).