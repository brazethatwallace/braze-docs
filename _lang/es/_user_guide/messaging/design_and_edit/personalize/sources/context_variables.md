---
nav_title: Variables de contexto
article_title: Variables de contexto
page_type: reference
description: "Este artículo de referencia explica las variables de contexto en los Canvas de Braze, incluyendo sus tipos, uso y mejores prácticas."
---

# Variables de contexto {#context-variables}

> Las variables de contexto son datos temporales que puedes crear y utilizar dentro del recorrido de un usuario a través de un Canvas específico. Te permiten personalizar retrasos, segmentar usuarios de forma dinámica y enriquecer la mensajería sin alterar permanentemente la información del perfil de usuario. Las variables de contexto solo existen dentro de la sesión del Canvas y no persisten entre diferentes Canvas ni fuera de la sesión.

## Cómo funcionan las variables de contexto {#how-context-variables-work}

Las variables de contexto se pueden establecer de dos formas:

- **En la entrada del Canvas:** Cuando los usuarios entran en un Canvas, los datos del evento o del desencadenador de API pueden rellenar automáticamente las variables de contexto.
- **En un paso de contexto:** Puedes definir o actualizar variables de contexto manualmente dentro del Canvas añadiendo un [paso de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context).

Cada variable de contexto incluye:

- Un nombre (como `flight_time` o `subscription_renewal_date`)
- Un tipo de datos (como número, cadena, hora o matriz)
- Un valor que asignas usando [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) o a través de la herramienta **Add Personalization**.

Una vez definida, puedes usar una variable de contexto en todo el Canvas haciendo referencia a ella en este formato: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Por ejemplo, {% raw %}`{{context.${flight_time}}}`{% endraw %} podría devolver la hora de vuelo programada del usuario.

Cada vez que un usuario entra en el Canvas —incluso si ya ha entrado antes— las variables de contexto se redefinirán en función de los datos de entrada más recientes y la configuración del Canvas. Este enfoque con estado permite que cada entrada al Canvas mantenga su propio contexto independiente, lo que permite a los usuarios tener múltiples estados activos dentro del mismo recorrido mientras conservan el contexto específico de cada estado.

Por ejemplo, si un cliente tiene dos vuelos próximos, tendrá dos estados de recorrido separados ejecutándose simultáneamente, cada uno con sus propias variables de contexto específicas del vuelo, como la hora de salida y el destino. Esto te permite enviar recordatorios personalizados sobre su vuelo de las 2 pm a Nueva York mientras envías actualizaciones diferentes sobre su vuelo de las 8 am a Los Ángeles de mañana, de modo que cada mensaje sea relevante para la reserva específica.

## Consideraciones {#considerations}

Puedes definir hasta 10 variables de contexto por [paso de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context). Cada nombre de variable puede tener hasta 100 caracteres y solo debe usar letras, números o guiones bajos.

Las definiciones de variables de contexto pueden tener hasta 10 240 caracteres. Si pasas variables de contexto a un Canvas desencadenado por API, comparten el mismo espacio de nombres que las variables creadas en un paso de contexto. Por ejemplo, si envías una variable `purchased_item` en el [endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) dentro del objeto de contexto, puedes hacer referencia a ella como {% raw %}`{{context.${purchased_item}}}`{% endraw %}. Si redefines esa variable en un paso de contexto, el nuevo valor sobrescribirá el valor de la API para el recorrido de ese usuario.

Puedes almacenar hasta 50 KB por paso de contexto, distribuidos en un máximo de 10 variables. Si el tamaño total de todas las variables en un paso supera los 50 KB, las variables que excedan el límite no se evaluarán ni almacenarán. Por ejemplo, si tienes tres variables en un paso de contexto:

- Variable 1: 30 KB
- Variable 2: 19 KB
- Variable 3: 2 KB

La variable 3 no se evaluará ni almacenará porque la suma de las variables anteriores supera los 50 KB.

## Tipos de datos {#data-types}

A las variables de contexto que se crean o actualizan en el paso se les pueden asignar los siguientes tipos de datos.

{% alert note %}
Las variables de contexto tienen los mismos formatos esperados para los tipos de datos que las [propiedades del evento]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#expected-format). <br><br>Al usar el tipo de matriz, Braze intenta analizar el valor como JSON, lo que permite crear matrices de objetos correctamente. Si los objetos dentro de tus matrices no son JSON válido, el resultado será una simple matriz de cadenas. <br><br>Para objetos anidados y matrices de objetos, usa el [filtro Liquid `as_json_string`](#converting-connected-content-strings-to-json). Si estás creando el mismo objeto en un paso de contexto, necesitarás renderizar el objeto usando `as_json_string`, como {%raw%}`{{context.${object_array} | as_json_string }}`{%endraw%}
{% endalert %}

| Tipo de datos | Nombre de variable de ejemplo | Valor de ejemplo |
|---|---|---|
| Booleano | loyalty_program |{% raw %}<code>true</code>{% endraw %}|
| Número | credit_score |{% raw %}<code>740</code>{% endraw %}|
| Cadena | product_name |{% raw %}<code>green_tea</code>{% endraw %} |
| Matriz | favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
| Matriz (de objetos) | pet_details |{% raw %}<code>[<br>&emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }<br>&emsp;,<br>&emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }<br>]</code>{% endraw %}|
| Hora (en UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
| Objeto (aplanado) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de datos" }

De forma predeterminada, el tipo de datos de hora está en UTC. Si usas un tipo de datos de cadena para almacenar un valor de hora, puedes definir la hora en una zona horaria diferente como PST.

Por ejemplo, si estás enviando un mensaje a un usuario el día antes de su cumpleaños, guardarías la variable de contexto como un tipo de datos de hora porque hay lógica Liquid asociada con el envío del día anterior. Sin embargo, si estás enviando un mensaje festivo el día de Navidad (25 de diciembre), no necesitarías hacer referencia a la hora como una variable dinámica, por lo que usar un tipo de datos de cadena sería preferible.

Para los tipos de datos de objeto, puedes usar la notación de punto para especificar una ruta a través de los datos. Por ejemplo, si tu paso de contexto define una variable de contexto `order_summary` con esta estructura:

```json
{
  "shipping": {
    "carrier": "overnight"
  }
}
```

En un filtro de [Rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) o [División de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split), introduce la ruta como el nombre de la variable de contexto usando notación de punto (por ejemplo, `order_summary.shipping.carrier`). Cuando se evalúa el filtro, Braze resuelve esa ruta al valor `overnight`.

En Liquid (como en un paso de [Mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)), usa {% raw %}`{{context.${order_summary}.shipping.carrier}}`{% endraw %} en su lugar.

## Uso de las variables de contexto {#using-context-variables}

Puedes usar variables de contexto en cualquier lugar donde uses Liquid en un Canvas, como en los pasos de [Mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) y [Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update), seleccionando **Add Personalization**. Para los mensajes dentro de la aplicación y los Banners en los pasos de mensaje, puedes seleccionar variables de contexto para determinar cuándo debe expirar el mensaje.

Por ejemplo, supongamos que quieres notificar a los pasajeros sobre su acceso al salón VIP antes de su próximo vuelo. Este mensaje solo debe enviarse a los pasajeros que compraron un boleto de primera clase. Una variable de contexto es una forma flexible de rastrear esta información.

Los usuarios entrarán en el Canvas cuando compren un boleto de avión. Para determinar la elegibilidad de acceso al salón, crearemos una variable de contexto llamada `lounge_access_granted` en un paso de contexto, y luego haremos referencia a esa variable de contexto en los pasos posteriores del recorrido del usuario.

![Variable de contexto configurada para rastrear si un pasajero califica para el acceso al salón VIP.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

En este paso de contexto, usaremos {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} para determinar si el tipo de vuelo que compraron es `first_class`.

A continuación, crearemos un paso de mensaje para dirigirnos a los usuarios donde {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} sea `true`. Este mensaje será una notificación push que incluye información personalizada del salón. Basándose en esta variable de contexto, los pasajeros elegibles recibirán los mensajes relevantes antes de su vuelo.

- Los pasajeros con boleto de primera clase recibirán: "¡Disfruta del acceso exclusivo al salón VIP!"
- Los pasajeros de clase ejecutiva y económica recibirán: "Mejora tu vuelo para obtener acceso exclusivo al salón VIP."

![Un paso de mensaje con diferentes mensajes a enviar, dependiendo del tipo de boleto de avión comprado.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
Puedes añadir [opciones de retraso personalizadas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step#personalized-delays) con la información del paso de contexto, lo que significa que puedes seleccionar la variable que retrasa a los usuarios.
{% endalert %}

### Para Rutas de Acción y criterios de salida {#for-action-paths-and-exit-criteria}

Puedes aprovechar la comparación de filtros de propiedades con variables de contexto o atributos personalizados en estas acciones desencadenantes: **Realizar evento personalizado** y **Realizar compra**. Estos desencadenadores de acción también admiten filtros de propiedades tanto para propiedades básicas como anidadas.

- Al comparar con propiedades básicas, las comparaciones disponibles coincidirán con el tipo de propiedad definido por el evento personalizado. Por ejemplo, las propiedades de cadena tendrán coincidencia exacta y coincidencia regex. Las propiedades booleanas serán verdadero o falso.
- Al comparar con propiedades anidadas, los tipos no están predefinidos, por lo que puedes seleccionar comparaciones entre múltiples tipos de datos para booleanos, números, cadenas, hora y día del año, de forma similar a las comparaciones para atributos personalizados anidados. Si seleccionas un tipo de datos que no coincide con el tipo de datos real de la propiedad anidada en el momento de la comparación, el usuario no coincidirá con la Ruta de Acción o los criterios de salida.

#### Ejemplos de Rutas de Acción {#action-path-examples}

{% alert important %}
Para las comparaciones de atributos personalizados, se usará el valor del atributo personalizado en el momento en que se realiza la acción. Esto significa que un usuario no coincidirá con el grupo de la Ruta de Acción si no tiene este atributo personalizado rellenado en el momento de la comparación, o si el valor del atributo personalizado no coincide con las comparaciones de propiedades definidas. Esto aplica incluso si el usuario habría coincidido cuando entró en el paso de Ruta de Acción.
{% endalert %}

{% tabs %}
{% tab Realizar evento personalizado %}

La siguiente Ruta de Acción está configurada para clasificar a los usuarios que realizaron el evento personalizado `Account_Created` con la propiedad básica `source` respecto a la variable de contexto `app_source_variable`.

![Un ejemplo de Ruta de Acción que hace referencia a una variable de contexto al realizar un evento personalizado.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Realizar compra %}

La siguiente Ruta de Acción está configurada para hacer coincidir la propiedad básica `brand` para el nombre de producto específico `shoes` con una variable de contexto `promoted_shoe_brand`.

![Un ejemplo de Ruta de Acción que hace referencia a una variable de contexto al realizar una compra.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### Ejemplos de criterios de salida {#exit-criteria-examples}

{% tabs %}
{% tab Realizar evento personalizado %}

Los criterios de salida establecen que en cualquier punto del recorrido de un usuario en el Canvas, saldrá del Canvas si:

- Realiza el evento personalizado **Abandon Cart**, y
- La propiedad básica **Item in Cart** coincide con el valor de cadena de la variable de contexto `cart_item_threshold`.

![Criterios de salida configurados para que un usuario salga si realiza un evento personalizado basado en la variable de contexto.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Realizar compra %}

Los criterios de salida establecen que en cualquier punto del recorrido de un usuario en el Canvas, saldrá del Canvas si:

- Realiza una compra específica para el nombre de producto "book", y
- La propiedad anidada de esa compra "loyalty_program" es igual al atributo personalizado del usuario "VIP".

![Criterios de salida configurados para que un usuario salga si realiza una compra.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Establecer una expiración {#set-an-expiration}

Para [Banners]({{site.baseurl}}/user_guide/channels/banners) y [mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages) en un paso de [Mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) de Canvas, selecciona **A duration after the step is available** para la expiración, luego activa **Personalize duration** para controlar la ventana de disponibilidad desde una variable de contexto; por ejemplo, para que coincida con la duración de una promoción o reserva de un paso de contexto.

**Personalize duration** se aplica a esa opción de expiración basada en duración. Si en su lugar eliges **On a specific date and time**, configura la expiración usando los controles de fecha y hora.

### Retrasos en Rutas de Acción {#action-path-delays}

En un paso de [Rutas de Acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), en **Evaluation Window**, activa **Personalize delay** para establecer cuánto tiempo se retiene a los usuarios en el paso a partir de una variable de contexto. Usa esto cuando el período de espera deba diferir por usuario según detalles como el nivel o la región.

### Filtros de variables de contexto {#context-variable-filters}

Puedes crear filtros que usen variables de contexto declaradas previamente en los pasos de [Rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) y [División de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split).

{% alert note %}
Los filtros de variables de contexto solo están disponibles para los pasos de rutas de audiencia y división de decisiones.
{% endalert %}

Las variables de contexto se declaran y solo son accesibles dentro del alcance de un Canvas, lo que significa que no se pueden referenciar en segmentos. Los filtros de variables de contexto funcionan de manera similar en los pasos de rutas de audiencia y división de decisiones: los pasos de rutas de audiencia representan múltiples grupos, mientras que los pasos de división de decisiones representan decisiones binarias.

![Ejemplo de paso de división de decisiones con la opción de crear un filtro con una variable de contexto.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

De manera similar a cómo las variables de contexto de Canvas tienen tipos predefinidos, las comparaciones entre variables de contexto y valores estáticos deben tener [tipos de datos coincidentes]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support). El filtro de variable de contexto permite comparaciones entre múltiples tipos de datos para booleanos, números, cadenas, hora y día del año, de forma similar a las comparaciones para [atributos personalizados anidados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).

{% alert note %}
Usa el mismo tipo de datos para tu variable de contexto y la comparación. Por ejemplo, si tu variable de contexto es un tipo de datos de hora, usa comparaciones de hora (como "antes" o "después"). Usar tipos de datos que no coinciden (como comparaciones de cadena con una variable de contexto de hora) puede causar un comportamiento inesperado.
{% endalert %}

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

Aquí tienes un ejemplo de un filtro de variable de contexto que compara la variable de contexto `product_name` con la regex `/braze/`.

![Una configuración de filtro para la variable de contexto "product_name" que coincida con la regex "/braze/".]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Comparar con variables de contexto o atributos personalizados {#comparing-to-context-variables-or-custom-attributes}

Al seleccionar el interruptor **Compare to a context variable or custom attribute**, puedes construir filtros de variables de contexto que comparen con variables de contexto definidas previamente o atributos personalizados del usuario. Esto puede ser útil para realizar comparaciones dinámicas por usuario, como el `context` desencadenado por API, o para condensar lógica de comparación compleja definida entre variables de contexto.

{% tabs %}
{% tab Ejemplo 1 %}

Supongamos que quieres enviar un recordatorio personalizado a los usuarios después de un período dinámico de inactividad, que incluye a cualquiera que no haya iniciado sesión en tu aplicación en los últimos tres días y deba recibir un mensaje.

Tienes una variable de contexto `re_engagement_date` que se define como {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %}. Ten en cuenta que `3 days` puede ser una cantidad variable que también se almacena como atributo personalizado del usuario. Entonces, si la `re_engagement_date` es posterior a la `last_login_date` (almacenada como atributo personalizado en el perfil de usuario), se les enviará un mensaje.

![Una configuración de filtro con atributos personalizados como tipo de personalización para la variable de contexto "re_engagement_date" después del atributo personalizado "last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Ejemplo 2 %}

El siguiente filtro compara la variable de contexto `reminder_date` para que sea anterior a la variable de contexto `appointment_deadline`. Esto puede ayudar a agrupar usuarios en un paso de rutas de audiencia para determinar si deben recibir recordatorios adicionales antes de la fecha límite de su cita.

![Una configuración de filtro con variables de contexto como tipo de personalización para la variable de contexto "reminder_date" sobre la variable de contexto "appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## Estandarización de consistencia de zona horaria {#time-zone-consistency-standardization}

Aunque la mayoría de las propiedades de eventos que usan el tipo de marca de tiempo ya están en UTC en Canvas, hay algunas excepciones. Con la adición del contexto de Canvas, todas las propiedades de eventos de marca de tiempo predeterminadas en Canvas basados en acciones estarán consistentemente en UTC. Este cambio es parte de un esfuerzo más amplio para garantizar una experiencia más predecible y consistente al editar pasos y mensajes de Canvas. Ten en cuenta que este cambio afectará a todos los Canvas basados en acciones, independientemente de si el Canvas específico está usando un paso de contexto o no.

{% alert important %}
En todas las circunstancias, recomendamos encarecidamente usar [filtros Liquid de time_zone]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties#things-to-know) para que las marcas de tiempo se representen en la zona horaria deseada. Puedes consultar esta [pregunta frecuente en el artículo del paso de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#faq-example) para ver un ejemplo.
{% endalert %}

## Artículos relacionados {#related-articles}

- [Paso de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)
- [Personalización y contenido dinámico con Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)