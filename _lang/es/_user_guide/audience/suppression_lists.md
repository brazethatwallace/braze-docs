---
nav_title: Listas de supresión
article_title: Listas de supresión
page_order: 7
page_type: reference
tool: Segments
description: "Esta página explica cómo utilizar las listas de supresión para especificar qué usuarios no deben recibir nunca tus mensajes."

---

# Listas de supresión {#suppression-lists}

> Las listas de supresión son grupos de usuarios que automáticamente no reciben ninguna Campaign ni Canvas. Las listas de supresión se definen mediante filtros de segmento, y los usuarios entran y salen de las listas de supresión a medida que cumplen los criterios de los filtros. También puedes establecer etiquetas de excepción para que la lista de supresión no se aplique a Campaigns o Canvas con esas etiquetas. Los mensajes de Campaigns o Canvas con etiquetas de excepción seguirán llegando a los usuarios de la lista de supresión que estén en los segmentos objetivo.

## ¿Por qué usar listas de supresión? {#why-use-suppression-lists}

Las listas de supresión son dinámicas y se aplican automáticamente a todas las formas de mensajería, pero puedes establecer excepciones para etiquetas seleccionadas. Si tus etiquetas de excepción seleccionadas se utilizan en una Campaign o Canvas, entonces esa lista de supresión no se aplicará a esa Campaign o Canvas. Los mensajes de Campaigns o Canvas con etiquetas de excepción seguirán llegando a cualquier usuario de la lista de supresión que forme parte de tus segmentos objetivo.

### Tipos de mensajes y canales afectados por las listas de supresión {#message-types-and-channels-affected-by-suppression-lists}

Las listas de supresión se aplican a todos los tipos de mensajes y canales excepto a los [conmutadores de características]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags). Esto significa que las listas de supresión se aplican de forma predeterminada a todos los canales, Campaigns y Canvas, incluyendo:
- [Campaigns de API]({{site.baseurl}}/api/api_campaigns)
- Campaigns y Canvas activados por API
- [Correos electrónicos transaccionales]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email)

El único tipo de mensaje al que no se aplican las listas de supresión son los conmutadores de características. Los usuarios en una lista de supresión no serán suprimidos de los conmutadores de características, pero sí de todos los demás canales.

Puedes usar etiquetas de excepción para que los usuarios de la lista de supresión sigan siendo objetivo de Campaigns y Canvas específicos. Para más detalles, consulta el paso 4 en [Configurar listas de supresión](#setup). Si no añades etiquetas de excepción a una lista de supresión, los usuarios de esa lista de supresión no serán objetivo de ninguna mensajería aparte de los conmutadores de características.

{% alert note %}
Las listas de supresión se aplican a las Campaigns de API que se crean en el dashboard de Braze con un `campaign_id`. Las listas de supresión no se aplican a los mensajes enviados a través de los [puntos de conexión de mensajería de Braze]({{site.baseurl}}/api/endpoints/messaging) sin un `campaign_id` asociado.
{% endalert %}

![La sección "Configuración de excepciones" con una casilla de verificación para no aplicar la lista de supresión a Campaigns y Canvas activados por API.]({% image_buster /assets/img/suppression_list_checkbox.png %}){: style="max-width:70%;"}

## Configurar listas de supresión {#setup}

{% alert note %}
Todos los usuarios pueden ver las listas de supresión, pero solo los usuarios con [permisos de administrador]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions?tab=admin) pueden crear y administrar listas de supresión.
{% endalert %}

1. Ve a **Audiencia** > **Listas de supresión**.
2. Selecciona **Crear lista de supresión** y añade un nombre.
3. Usa filtros de segmento para identificar a los usuarios en tus listas de supresión. Debes seleccionar al menos uno.

{% alert important %}
Aunque el proceso de configuración parece similar a la [creación de segmentos]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), una lista de supresión es un grupo de usuarios a los que **no** quieres enviar mensajes independientemente de su pertenencia a un segmento.
{% endalert %}

![Un constructor de listas de supresión con un filtro para usuarios que abrieron un correo electrónico por última vez hace más de 90 días.]({% image_buster /assets/img/suppression_list_filters.png %})

{: start="4"}
4. Determina si deseas tener excepciones basadas en etiquetas marcando la casilla debajo del nombre de tu segmento (consulta [¿Por qué usar listas de supresión?](#why-use-suppression-lists) para más información), y luego añade las etiquetas de Campaigns o Canvas que los usuarios de esta lista de supresión deberían seguir recibiendo. <br><br>En otras palabras, si añades la etiqueta de excepción "Confirmación de envío", los usuarios de tu lista de supresión serán excluidos de toda la mensajería excepto de aquella que use la etiqueta "Confirmación de envío".<br><br>![La sección "Detalles de la lista de supresión" con una etiqueta de excepción aplicada llamada "Confirmación de envío".]({% image_buster /assets/img/exception_tags.png %})<br><br>
5. Guarda o activa tu lista de supresión.
- Cuando guardas, tu lista de supresión se guardará pero no se activará, lo que significa que no entrará en vigor. Tu lista de supresión permanecerá inactiva hasta que la actives, y las listas de supresión inactivas no afectarán a la mensajería (los usuarios no serán excluidos de los mensajes).
- Cuando activas, tu lista de supresión se guardará e inmediatamente entrará en vigor, lo que significa que los usuarios de tu lista de supresión serán excluidos inmediatamente de Campaigns o Canvas (excepto de aquellos que contengan una etiqueta de excepción).

{% alert note %}
Solo los administradores pueden guardar o activar listas de supresión. Puedes tener hasta cinco listas de supresión activas a la vez en la beta.
{% endalert %}

Puedes desactivar o archivar las listas de supresión cuando ya no las necesites.
- Para desactivar, selecciona una lista de supresión activa y selecciona **Desactivar**. Las listas de supresión desactivadas se pueden reactivar más tarde.
- Para archivar, hazlo desde la página **Listas de supresión**.

## Uso de las listas de supresión {#suppression-list-usage}

Para comprobar si tu lista de supresión impidió que un usuario recibiera un mensaje, usa **Búsqueda de usuarios** en el paso **Público objetivo** dentro de tu Campaign o Canvas. Aquí podrás ver a qué lista de supresión pertenece.

{% alert note %}
Las listas de supresión se actualizan antes de que se envíe un mensaje, no después de que se lance una Campaign. Esto significa que un usuario que se añade a una lista de supresión después del lanzamiento de la Campaign pero antes del envío del mensaje podría seguir recibiendo el mensaje.
{% endalert %}

![Ventana de "Búsqueda de usuarios" que muestra que un usuario está en una lista de supresión.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

{% alert tip %}
También puedes encontrar las listas de supresión aplicadas en el paso **Resumen**.
{% endalert %}

Mientras creas una Campaign o Canvas, usa **Búsqueda de usuarios** dentro del paso **Público objetivo** para buscar un usuario, y si no está en la audiencia objetivo, puedes ver la lista de supresión a la que pertenece.

![Ventana de "Búsqueda de usuarios" que muestra que un usuario está en una lista de supresión.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

### Campaign

Si un usuario está en una lista de supresión, no recibirá una Campaign a la que se aplique esa lista de supresión. Consulta [Tipos de mensajes y canales afectados por las listas de supresión](#message-types-and-channels-affected-by-suppression-lists) para los casos en que una lista de supresión no se aplique.

![La sección "Listas de supresión" con una lista de supresión activa, llamada "Puntuaciones bajas de salud de marketing".]({% image_buster /assets/img/active_suppression_list.png %})

### Canvas

Desde el momento en que un usuario se añade a una lista de supresión, no entrará en Canvas. Si ya ha entrado en un Canvas, no recibirá los pasos de mensaje. Esto significa que si un usuario ya está dentro de un Canvas cuando se le añade a una lista de supresión, avanzará a través del Canvas hasta el siguiente paso de mensaje, momento en el que saldrá sin recibir el paso de mensaje.

Por ejemplo, supongamos que un Canvas tiene un paso de Actualización de usuario seguido de un paso de mensaje. Si un usuario entra en el Canvas y luego se le añade a una lista de supresión, ese usuario seguirá avanzando a través del paso de Actualización de usuario (donde puede ser actualizado), y luego saldrá en el paso de mensaje, momento en el que se incluirá en las métricas de salida.