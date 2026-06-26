---
nav_title: Gestión personalizada de palabras clave
article_title: Gestión personalizada de palabras clave
page_order: 2
description: "Este artículo de referencia cubre cómo Braze gestiona la mensajería bidireccional de SMS, MMS y RCS y las respuestas automáticas. Incluye explicaciones sobre cómo funciona la activación por palabras clave, así como las categorías de palabras clave personalizadas y la asistencia en varios idiomas."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS

---

# Gestión personalizada de palabras clave {#custom-keyword-handling}

> Este artículo de referencia cubre cómo Braze gestiona la mensajería bidireccional de SMS, MMS y RCS y las respuestas automáticas. Incluye explicaciones sobre cómo funciona la activación por palabras clave, así como las categorías de palabras clave personalizadas y la asistencia en varios idiomas.

## Mensajería bidireccional (respuestas personalizadas por palabras clave) {#two-way-messaging-custom-keyword-responses}

La mensajería bidireccional te permite enviar mensajes y procesar las respuestas a esos mensajes. Requiere que los usuarios finales envíen una palabra clave a Braze, tras lo cual recibirán una respuesta automática. Aplicada correctamente, la mensajería bidireccional puede ser una solución sencilla, inmediata y dinámica para el marketing del cliente, ahorrando tiempo y recursos en el proceso.

## Administración de palabras clave y respuestas automáticas {#managing-keywords-and-auto-responses}

SMS, MMS y RCS con Braze te ofrecen la opción de crear activadores de palabras clave, respuestas personalizadas, definir conjuntos de palabras clave para varios idiomas y establecer categorías de palabras clave personalizadas.

{% alert note %}
Braze utiliza tu conjunto completo de palabras clave de cancelación de suscripción ([palabras clave predeterminadas]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout/) y [palabras clave personalizadas]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling/)) para la gestión exacta de cancelación de suscripción y la [cancelación de suscripción aproximada]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out/).
{% endalert %}

{% tabs %}
{% tab Añadir activadores de palabras clave %}

### Añadir activadores de palabras clave {#add-keyword-triggers}

Además de las palabras clave predeterminadas de adhesión voluntaria y cancelación de suscripción, también puedes definir tus propias palabras clave para activar respuestas de adhesión voluntaria, cancelación de suscripción y ayuda.

Para definir tus propias palabras clave, haz lo siguiente:

1. En el panel de Braze, ve a **Audience** > **Subscription Group Management** y selecciona un grupo de suscripción **SMS/MMS/RCS**.
2. En **Global Keywords**, selecciona el icono de lápiz junto a la categoría de palabras clave a la que quieras añadir una palabra clave. ![Palabras clave de adhesión voluntaria con el icono de lápiz visible.]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. En la pestaña que se abre, añade una palabra clave que quieras que active esta categoría de palabras clave. Ten en cuenta que las palabras clave no distinguen entre mayúsculas y minúsculas, y que las palabras clave universales como `START`, `YES` y `UNSTOP` no se pueden cambiar. ![Edición de palabras clave para la categoría "Opt-In". Las palabras clave añadidas son "START", "UNSTOP" y "YES". El campo del mensaje de respuesta dice "Has cancelado la suscripción a los mensajes de este número. Responde HELP para obtener ayuda. Responde STOP para cancelar la suscripción. Pueden aplicarse tarifas de mensajes y datos."]({% image_buster /assets/img/sms/keyword_edit2.png %})

Las siguientes reglas se aplican a las palabras clave y las respuestas de palabras clave:

| Palabras clave | Respuestas de palabras clave |
| -------- | ----------------- |
| - Caracteres válidos codificados en UTF-8<br>- Máximo de 20 palabras clave por categoría en total<br>- Longitud máxima de 34 caracteres<br>- Longitud mínima de 1 carácter<br>- No pueden contener espacios<br>- Deben ser insensibles a mayúsculas y únicas en todo el grupo de suscripción | - No pueden estar en blanco<br>- Longitud máxima de 300 caracteres<br>- Caracteres válidos UTF-8 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Añadir activadores de palabras clave" }

{% alert tip %}
¿Te interesa ver cómo se pueden usar estas palabras clave en tus Campaigns y Canvas para reorientar y activar mensajes? Visita [Reorientación de usuarios]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/) para más información.
{% endalert %}
{% endtab %}

{% tab Administrar respuestas %}

### Administrar respuestas {#manage-responses}

Puedes administrar tus propias respuestas que se envían a los usuarios después de que envíen un mensaje de texto con una palabra clave a una categoría de palabras clave específica.

1. En el panel de Braze, ve a **Audience** > **Subscription Group Management** y selecciona un grupo de suscripción **SMS/MMS/RCS**. <br><br>
2. En **Global Keywords**, selecciona una categoría de palabras clave para editar una respuesta seleccionando el icono de lápiz. ![Palabras clave de adhesión voluntaria con el icono de lápiz visible.]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. En la pestaña que se abre, edita tu respuesta. Ten en cuenta nuestras [seis reglas para cumplir correctamente con la normativa]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/#the-six-rules-to-get-compliance-right) mientras creas tu respuesta, y lee las siguientes reglas que se aplican a las palabras clave y las respuestas de palabras clave.<br><br>
4. Para acortar automáticamente las URL estáticas en tu respuesta, selecciona el conmutador **Link Shortening**. El contador de caracteres se actualizará para mostrar la longitud esperada de la URL acortada. ![Un GIF que muestra cómo se actualiza el contador de caracteres cuando el conmutador "Link Shortening" está activado.]({% image_buster /assets/img/sms/link_shortening.gif %}){: style="max-width:60%;"}

#### Consideraciones {#considerations}

| Palabras clave | Respuestas de palabras clave |
| -------- | ----------------- |
| - Caracteres válidos codificados en UTF-8<br>- Máximo de 20 palabras clave por categoría en total<br>- Longitud máxima de 34 caracteres<br>- Longitud mínima de 1 carácter<br>- No pueden contener espacios<br>- Deben ser insensibles a mayúsculas y únicas en todo el grupo de suscripción | - No pueden estar en blanco<br>- Longitud máxima de 300 caracteres<br>- Caracteres válidos UTF-8 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Consideraciones" }

{% endtab %}
{% endtabs %}

{% alert tip %}
Si un Canvas basado en acciones se activa mediante un mensaje SMS, MMS o RCS de entrada, puedes hacer referencia a las propiedades de SMS, MMS o RCS en el primer [paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) del Canvas.
{% endalert %}

## Asistencia en varios idiomas {#multi-language-support}

Al enviar a ciertos países, es posible que se requiera que un remitente admita palabras clave de entrada y respuestas de salida en un idioma local. Para esto, Braze te permite crear una configuración de palabras clave específica por idioma. Una vez creada, la configuración de palabras clave específica por idioma se aplicará a todos los números de envío dentro del grupo de suscripción.
![Menú desplegable que muestra los idiomas disponibles para añadir como configuración de palabras clave.]({% image_buster /assets/img/sms/multi-language.png %}){: style="float:right;max-width:50%;margin-left:10px;"}

### Creación de palabras clave específicas por idioma {#creating-language-specific-keywords}

Selecciona **Add a Language** y elige tu idioma de destino o busca un idioma en el menú desplegable.

{% alert important %}
Los idiomas distintos del inglés no incluyen palabras clave ni respuestas preconfiguradas, por lo que los remitentes deberán trabajar con sus equipos de marketing y legal para añadir las palabras clave necesarias a este conjunto. De lo contrario, Braze no gestionará los mensajes entrantes localizados para esos idiomas.
{% endalert %}

Si necesitas eliminar un idioma, selecciona el botón **Delete Language** en la parte inferior derecha.

![Página de palabras clave globales con la pestaña "Italian" seleccionada. Existen pestañas adicionales para cada idioma añadido.]({% image_buster /assets/img/sms/multi-language2.png %})

## Categorías de palabras clave personalizadas {#custom-keyword-categories}

Además de las tres categorías de palabras clave predeterminadas (adhesión voluntaria, cancelación de suscripción y ayuda), también puedes crear hasta 25 categorías de palabras clave propias. Esto te permite identificar palabras clave arbitrarias y configurar respuestas específicas para tu negocio. Un ejemplo de categoría podría ser "PROMO" o "DESCUENTO", que podría generar una respuesta sobre las promociones vigentes este mes.

Estas palabras clave personalizadas funcionan en modo "siempre activo", lo que significa que cualquier usuario suscrito a tu servicio de mensajería puede enviar palabras clave y recibir una respuesta en cualquier momento. Además de este comportamiento, también tienes la opción de definir palabras clave específicas que solo se pueden enviar en [ciertos momentos](#lifecycle-specific-keywords) del ciclo de vida de tu usuario.

![Palabras clave para una categoría "Promo". Si un usuario envía "YO", recibe el mensaje con un código promocional.]({% image_buster /assets/img/sms/sms_custom_keyword.png %})

### Creación de una categoría personalizada {#creating-a-custom-category}

Para crear una categoría de palabras clave personalizada, haz lo siguiente:

1. Edita el grupo de suscripción correspondiente.
2. Selecciona **Add custom keyword**. ![Campos para añadir nuevas palabras clave.]({% image_buster /assets/img/sms/sms_custom_step.png %}){: style="max-width:90%;"}
3. Proporciona un nombre para la categoría de palabras clave y define qué palabras clave puede enviar un usuario para recibir el mensaje de respuesta.

Una vez creada esta categoría de palabras clave, estará disponible para [filtrar y activar]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/) en tus Campaigns y Canvas.

Las palabras clave creadas en categorías de palabras clave personalizadas se rigen por todas las reglas y validaciones para la creación de nuevas palabras clave.

### Palabras clave específicas del ciclo de vida {#lifecycle-specific-keywords}

Si tienes un caso de uso en el que deseas limitar cuándo un cliente puede enviar una palabra clave específica durante su ciclo de vida (por ejemplo, durante su incorporación inicial) para recibir una respuesta, puedes usar el activador **Sent inbound SMS to subscription group within keyword category OTHER** en tu Campaign o Canvas y definir las palabras clave que tus usuarios pueden enviar en un momento determinado.

Este activador admite el filtrado del mensaje de entrada específico mediante comparaciones de es o no es del mensaje, así como reglas de coincide o no coincide con regex para validar la entrada del usuario.

#### Canvas

![Paso de Canvas basado en acciones con el activador Enviar SMS de entrada al grupo de suscripción "Messaging Service" dentro de la categoría de palabras clave "Other" donde el cuerpo del mensaje coincide con la expresión regular "símbolo de intercalación skip."]({% image_buster /assets/img/sms/canvas_trigger.png %}){: style="max-width:90%;"}

#### Campaign

![Campaign basada en acciones con el activador Enviar SMS de entrada al grupo de suscripción "Marketing Message Service A" dentro de la categoría de palabras clave "Other" donde el cuerpo del mensaje es "Keyword1" o es "Keyword2" o no es "Keyword A".]({% image_buster /assets/img/sms/campaign_trigger.png %}){: style="max-width:90%;"}

### Gestión de palabras clave desconocidas {#dealing-with-unknown-keywords}

Recomendamos encarecidamente configurar una respuesta automática cuando los usuarios suscritos envíen algo que no coincida con ninguna de tus palabras clave definidas (gestionado bajo la categoría de palabras clave **OTHER**).

Para enviar una respuesta predeterminada, por ejemplo, "¡Lo sentimos! No reconocimos esa palabra clave.", haz lo siguiente:

1. Crea una [Campaign de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/).
2. Para **Público objetivo**, elige **Todos los usuarios** (el activador aún limita quién recibe el mensaje).
3. Para **Planificación**, elige **Entrega basada en acciones**.
4. Configura el activador como **Send inbound SMS** al grupo de suscripción correspondiente **within keyword category OTHER**.
5. En el paso **Messaging**, introduce el cuerpo de la respuesta que quieres que reciban los usuarios.

Para saber cómo Braze gestiona los mensajes entrantes de números de teléfono **desconocidos** (antes de que exista un perfil), consulta [Gestión de números de teléfono desconocidos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/unknown_phone_numbers/).

{% alert tip %}
¿Te interesa ver cómo se pueden usar estas palabras clave y categorías de palabras clave en tus Campaigns y Canvas para reorientar y activar mensajes? Visita [Reorientación de usuarios]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/) para más información.
{% endalert %}