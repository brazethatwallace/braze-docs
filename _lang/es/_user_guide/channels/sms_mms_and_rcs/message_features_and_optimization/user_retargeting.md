---
nav_title: "Reorientación de usuarios"
article_title: "Reorientación de usuarios"
description: "Este artículo de referencia cubre cómo los usuarios pueden reorientar sus mensajes según las interacciones de SMS y RCS de un usuario."
page_type: reference
page_order: 4
alias: /sms_mms_rcs_user_retargeting/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS

---

# Reorientación de usuarios {#user-retargeting}

> Además de cambiar el estado de suscripción del usuario y enviar respuestas automáticas basadas en palabras clave entrantes, Braze también registrará las interacciones en el perfil de usuario para filtrar y desencadenar mensajes.<br><br>Estos filtros y desencadenantes te permiten filtrar acciones basadas en usuarios que han recibido o han respondido a campañas de SMS, MMS y RCS, o interactuar aún más con usuarios que han hecho clic en URL acortadas.

{% alert tip %}
Para leer más sobre palabras clave personalizadas y cómo configurar la mensajería bidireccional para aprovechar estas opciones de reorientación, visita nuestro artículo sobre [palabras clave personalizadas]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling).
{% endalert %}

## Opciones de reorientación {#retargeting-options}

{% alert note %}
Al crear audiencias con reorientación de usuarios, es posible que desees incluir o excluir a ciertos usuarios en función de sus preferencias y para cumplir con las leyes de privacidad, como el derecho de "No vender ni compartir" bajo la CUP. Los especialistas en marketing deben implementar los filtros relevantes para la elegibilidad de los usuarios dentro de los criterios de entrada de su Canvas o Campaign.
{% endalert %}

### Filtrar usuarios por SMS, MMS y RCS {#filter-users-by-sms-mms-and-rcs}

Los usuarios pueden filtrarse por la última vez que recibieron un SMS, MMS o RCS o si han recibido un SMS, MMS o RCS de una campaña específica. Los filtros se pueden configurar en el paso **Target Audiences** del creador de campañas.

{% alert note %}
Cuando un mensaje es recibido, abierto o se hace clic en él, Braze actualiza los datos de todos los perfiles que comparten el mismo número de teléfono que el perfil que registró la interacción. Los usuarios que comparten un número de teléfono con alguien que recibió, abrió o hizo clic en el mensaje pueden coincidir con este filtro aunque no estuvieran originalmente en la campaña o no se les hubiera enviado el mensaje directamente.
{% endalert %}

#### Filtrar por último SMS/MMS/RCS recibido {#filter-by-last-received-smsmmsrcs}

![Filtro de segmentación Último SMS recibido después del 8 de diciembre de 2020.]({% image_buster /assets/img/sms/filter2.png %})

#### Filtrar por mensajes recibidos de una Campaign de SMS/MMS/RCS {#filter-by-received-messages-from-smsmmsrcs-campaign}

Filtra usuarios que han recibido un mensaje de una campaña específica. Con este filtro, también tienes la opción de filtrar a aquellos que no han recibido mensajes de una campaña.

![Filtro de segmentación Ha recibido mensaje de la Campaign "SMS retargeting".]({% image_buster /assets/img/sms/filter1.png %})

### Desencadenar mensajes cuando los usuarios reciben SMS, MMS o RCS {#trigger-messages}

Para desencadenar mensajes cuando los usuarios reciben mensajes de SMS, MMS o RCS de una campaña específica, selecciona **Interact with Campaign** como la acción desencadenante de una campaña basada en acciones. A continuación, selecciona **Receive SMS** y la campaña que deseas utilizar.

![Para desencadenar mensajes cuando los usuarios reciben mensajes de SMS, MMS o RCS de una campaña específica, selecciona Interact with Campaign como la acción desencadenante de una campaña basada en acciones. A continuación, selecciona Receive SMS y la Campaign de SMS, MMS o RCS que deseas utilizar.]({% image_buster /assets/img/sms/trigger.png %})

### Filtrar por enlaces de seguimiento avanzado {#filter-by-advanced-tracking-links}

Reorienta a los usuarios que han hecho clic en campañas con [enlaces de seguimiento avanzado]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening).
Solo las campañas que tienen habilitado el seguimiento avanzado aparecen en los siguientes desplegables:

#### Reorientar usuarios que han hecho clic en una Campaign de SMS, MMS o RCS específica {#retarget-users-who-have-clicked-a-specific-sms-mms-or-rcs-campaign}

1. Crea un segmento usando el filtro **Clicked/Opened Campaign**.
2. Selecciona **clicked shortened sms link**.
3. Elige la campaña deseada.

![Captura de pantalla de la reorientación de usuarios que han hecho clic en una Campaign de SMS, MMS o RCS específica.]({% image_buster /assets/img/sms/retargeting5.png %})

#### Reorientar usuarios que han hecho clic en un paso en Canvas específico {#retarget-users-who-have-clicked-a-specific-canvas-step}

1. Crea un segmento usando el filtro **Clicked/Opened Step**.
2. Selecciona **clicked shortened sms link**.
3. Elige el Canvas y el paso en Canvas deseados.

![Captura de pantalla de la reorientación de usuarios que han hecho clic en un paso en Canvas específico.]({% image_buster /assets/img/keyword_example1.jpg %})

## Reorientación específica por categoría de palabras clave {#keyword-category-specific-retargeting}

Además de las tres categorías predeterminadas de palabras clave (Adhesión voluntaria, Exclusión y Ayuda), también puedes crear hasta 25 categorías de palabras clave propias, lo que te permite identificar palabras clave y respuestas arbitrarias. Estas categorías se pueden utilizar para filtrar y reorientar. Para obtener más información sobre las categorías de palabras clave globales y cómo configurarlas, consulta [Procesamiento de palabras clave]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing).

### Filtrar por fecha reciente {#filter-by-recency}

Filtra por la fecha más reciente en que un usuario respondió a tu programa de SMS, MMS o RCS. Este filtro evaluará la última fecha en que un usuario envió un mensaje entrante que se encuentra dentro de una de las categorías de palabras clave.

![Filtro de segmentación "Último SMS enviado al grupo de suscripción" con valor "Marketing SMS", palabra clave "Opt-in" después del 11 de agosto de 2020.]({% image_buster /assets/img/sms/retargeting1.png %})

### Filtrar por atribución de Campaign o Canvas {#filter-by-campaign-or-canvas-attribution}

Filtra por usuarios que han respondido a una Campaign o componente de Canvas de SMS, MMS o RCS específico, categoría de palabras clave o etiqueta.

{% alert note %}
Estos filtros utilizan [datos de interacción de mensajería]({{site.baseurl}}/messaging_interaction_data). Para Campaigns y Canvas detenidos, esos datos expiran después de tres meses a menos que se utilicen en un filtro de reorientación activo. Los datos expirados se pueden restaurar. La ventana de retención de tu espacio de trabajo puede diferir de la predeterminada.
{% endalert %}

#### Filtrar por respuesta a una Campaign específica con categoría de palabras clave {#filter-by-replied-to-a-specific-campaign-with-keyword-category}

![Campaign con el filtro "Ha respondido a SMS" para la Campaign "SMS-283" "Promotion".]({% image_buster /assets/img/sms/clicked_opened_campaign.png %})

#### Filtrar por respuesta a una Campaign o Canvas con una etiqueta específica {#filter-by-replied-to-a-campaign-or-canvas-with-a-specific-tag}

![Campaign con el filtro "Ha respondido a SMS" para Campaign o Canvas con etiqueta "Curbside Messaging Service C".]({% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %})

#### Filtrar por respuesta a un paso específico {#filter-by-replied-to-a-specific-step}

![Campaign con el filtro "Ha respondido a SMS" para el paso "SMS Double Opt" "Step - Help".]({% image_buster /assets/img/sms/clicked_opened_step.png %})

### Desencadenar mensajes por palabra clave {#trigger-messages-by-keyword}

Los mensajes pueden desencadenarse cuando los usuarios envían mensajes entrantes según categorías de palabras clave (el usuario envió alguna de las palabras clave) u otras palabras clave (el usuario envió una palabra clave que no pertenece a una de las categorías existentes). Estos desencadenadores se configuran en el paso Entrega del creador de campañas.

Al evaluar si un mensaje entrante cumple con un evento desencadenante definido, se eliminan los espacios iniciales y finales antes de comenzar la evaluación.

{% alert tip %}
Si un Canvas basado en acciones se desencadena mediante un mensaje entrante de SMS o MMS, puedes hacer referencia a [propiedades de Liquid de SMS compatibles]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) en cualquier paso en Canvas hasta la siguiente ruta de acción.
{% endalert %}

#### Desencadenar por categoría de palabra clave entrante {#trigger-by-inbound-keyword-category}

![Campaign de SMS basada en acciones con el filtro de segmentación "Envió palabra clave" con valor "Opt-in" al grupo de suscripción "Marketing SMS".]({% image_buster /assets/img/sms/retargeting2.png %}){: style="margin-top:10px;"}

#### Desencadenar por palabras clave arbitrarias {#trigger-by-arbitrary-keywords}

Ten en cuenta que al desencadenar un mensaje con una respuesta de palabra clave "Other", tienes la oportunidad de evaluar el cuerpo de la palabra clave mediante una coincidencia exacta de texto. Esta coincidencia sigue las mismas reglas indicadas: solo se procesa el **mensaje exacto de una sola palabra** (sin distinción entre _mayúsculas y minúsculas_). Una palabra clave enviada como `Hello Braze!` no coincidiría con los criterios mostrados en el siguiente ejemplo.

![Campaign de SMS basada en acciones con categoría de palabra clave como "Other" donde el cuerpo del mensaje es exactamente "Hello" o "Hey".]({% image_buster /assets/img/sms/retargeting3.png %}){: style="margin-top:10px;"}

#### Palabras clave con plantilla {#template-keywords}

Al desencadenar una Campaign o un componente de Canvas con un SMS o MMS entrante, opcionalmente puedes incluir como plantilla el texto o los archivos multimedia adjuntos que tu usuario envió en el cuerpo de tu Campaign o Canvas con Liquid. Esto te permite acceder a la respuesta del usuario, que luego puedes incluir en tu respuesta, aplicar lógica condicional o cualquier otra cosa que puedas hacer con Liquid.

{% raw %}

```liquid
Sorry, we didn't recognize {{sms.${inbound_message_body}}}. Text HELP for help or STOP to stop.
```

```liquid
{% if {{sms.${inbound_message_body}}} == "SNEAKERS" %}
OK, you're subscribed to updates on all our sneaker deals!
{% elsif {{sms.${inbound_message_body}}} == "SHIRTS" %}
Shirt deals coming up for you!
{% else %}
Want to receive a specific deal? Just text us the category you're interested in. For example SHIRTS or SNEAKERS.
{% endif %}
```

{% endraw %}