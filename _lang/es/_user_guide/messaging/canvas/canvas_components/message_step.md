---
nav_title: Mensaje
article_title: Mensaje
alias: "/message_step/"
page_order: 11
page_type: reference
description: "Este artículo de referencia explica cómo crear un mensaje independiente utilizando el paso Mensaje."
tool: Canvas

---

# Mensaje {#message}

> Los pasos de mensaje te permiten añadir un mensaje independiente donde quieras en tu Canvas.

![Un paso de mensaje llamado "Lunch promo" que utiliza el canal push.]({% image_buster /assets/img/canvas_components/message_step1.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

## Crear un mensaje {#create-a-message}

Para crear un componente de mensaje, primero añade un paso a tu Canvas. Arrastra y suelta el componente desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> de signo más en la parte inferior de un paso y selecciona **Message**.

### Paso 1: Selecciona tu canal de mensajería {#step-1-select-your-messaging-channel}

Puedes seleccionar entre los siguientes canales de mensajería:
- Banners
- Content Cards
- Correo electrónico
- LINE
- Notificaciones push
- SMS/MMS/RCS
- Mensajes dentro de la aplicación
- Webhook
- WhatsApp

![Una lista de canales de mensajería disponibles para seleccionar en el paso Mensaje.]({% image_buster /assets/img/canvas_components/message_step2.png %})

### Paso 2: Edita los ajustes de entrega {#step-2-edit-delivery-settings}

A continuación, puedes editar los ajustes de Intelligent Delivery, las anulaciones de horas tranquilas y la validación de entrega.

#### Intelligent Timing {#intelligent-timing}

Puedes habilitar [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) con una opción alternativa cuando el perfil de un usuario no tiene suficientes datos para calcular un momento óptimo. Recomendamos habilitar Intelligent Timing y el [límite de velocidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#rate-limiting-and-frequency-capping) como una comprobación adicional para cualquier retraso entre el momento en que los usuarios entran en el paso Mensaje y el envío real del mensaje.

Selecciona **Using Intelligent Timing** en la pestaña **Delivery Settings**. Aquí puedes seleccionar la hora más popular o una hora alternativa específica. Si las horas tranquilas están habilitadas, el paso Mensaje también te permite anular este ajuste.

![La pestaña Delivery Settings para los ajustes del componente Mensaje. Las horas tranquilas están habilitadas y la casilla Using Intelligent Timing está seleccionada para entregar el mensaje en el momento óptimo.]({% image_buster /assets/img/canvas_components/message_step4.png %}){: style="max-width:90%;"}

#### Validaciones de entrega {#delivery-validations}

Las validaciones de entrega proporcionan una comprobación adicional en el momento del envío del mensaje para confirmar que tu audiencia aún cumple tus criterios. Recomendamos usarlas cuando las horas tranquilas, Intelligent Timing o el límite de velocidad están habilitados. Selecciona **Validate audience at message send**, luego añade un segmento o filtros adicionales. Si un usuario no cumple las validaciones, elige si sale del Canvas o avanza al siguiente paso.

Las validaciones de entrega evalúan los criterios del perfil de usuario en el momento del envío. Los filtros relacionados con la aplicación comprueban si un usuario usó recientemente o alguna vez una aplicación específica, pero no confirman qué aplicación está usando el usuario en su sesión actual.

Si tu espacio de trabajo tiene múltiples aplicaciones y un paso Mensaje debe dirigirse a una aplicación específica, usa uno de los siguientes enfoques en su lugar:

- Al componer el mensaje, [especifica tus plataformas de entrega]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#step-2-specify-delivery-platforms), como **Mobile Apps** o **Web Browsers**.
- Usa Liquid para comprobar el dispositivo o la aplicación de destino en el momento del envío:
  - {% raw %}`{{targeted_device.${platform}}}`{% endraw %} evalúa la plataforma de la sesión actual del usuario. Para más información, consulta [Información del dispositivo de destino]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#targeted-device-information).
  - {% raw %}`{{app.${api_id}}}`{% endraw %} evalúa qué aplicación está solicitando el mensaje. Combina esta etiqueta con `abort_message()` para evitar envíos a la aplicación incorrecta. Para más información, consulta [Información de la aplicación de destino]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#targeted-app-information).

![Las validaciones de entrega están habilitadas para validar la audiencia en el envío del mensaje. El comportamiento de avance de las validaciones de entrega está configurado para hacer avanzar al usuario al siguiente paso en el Canvas si no se cumplen las validaciones de entrega.]({% image_buster /assets/img/canvas_components/message_step5.png %}){: style="max-width:90%;"}

## Cómo avanzan los usuarios {#how-users-advance}

Todos los usuarios que entran en el paso Mensaje avanzan al siguiente paso cuando se cumple cualquiera de las siguientes condiciones:

- Se envía cualquier mensaje
- Un mensaje tiene un límite de frecuencia y no se envía
- Un mensaje se cancela
- Un usuario no es alcanzable por el canal, por lo que el mensaje no se envía
- Un usuario no cumple los criterios en **Delivery validations**

{% raw %}
Si un Canvas basado en acciones se desencadena por un mensaje SMS de entrada, puedes hacer referencia a las propiedades de SMS en el primer paso (paso Mensaje) o en un paso Mensaje anidado bajo un paso de ruta de acción. Por ejemplo, en el paso Mensaje, podrías usar `{{sms.${inbound_message_body}}}` o `{{sms.${inbound_media_urls}}}`.
{% endraw %}

## Propiedades de contexto de referencia {#reference-context-properties}

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

Las propiedades de entrada se configuran en el paso **Entry Schedule** al crear un Canvas e indican el desencadenante que hace que un usuario entre en un Canvas. Estas propiedades también pueden acceder a las propiedades de las cargas útiles de entrada en Canvas activados por API. Ten en cuenta que el objeto `context` tiene un límite de tamaño máximo de 50 KB.

Las propiedades de entrada se pueden usar en Liquid en cualquier paso Mensaje. Usa el siguiente Liquid cuando hagas referencia a estas propiedades de entrada: {% raw %}``{context.${property_name}}``{% endraw %}. Los eventos deben ser eventos personalizados o eventos de compra para poder usarse de esta manera.

{% alert note %}
Específicamente para los canales de mensajes dentro de la aplicación, `context` solo se puede referenciar en Canvas.
{% endalert %}

Usa el siguiente Liquid cuando hagas referencia a estas propiedades de entrada: {% raw %}``context.${property_name}``{% endraw %}. Ten en cuenta que los eventos deben ser eventos personalizados o eventos de compra para poder usarse de esta manera.

{% raw %}
Por ejemplo, considera la siguiente solicitud: `"context" : {"product_name" : "shoes", "product_price" : 79.99}`. Podrías añadir la palabra "shoes" a un mensaje con el Liquid `{{context.${product_name}}}`.
{% endraw %}

También puedes aprovechar las [propiedades de entrada persistentes]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties) en cualquier paso Mensaje para guiar a tus usuarios a través de pasos personalizados en todo el flujo de trabajo de tu Canvas.

### Propiedades del evento {#event-properties}

Las propiedades del evento se refieren a las propiedades que configuras para eventos personalizados y eventos de compra. Estas propiedades del evento se pueden usar en Campaigns con entrega basada en acciones, así como en Canvas.

En Canvas, las propiedades de eventos personalizados y eventos de compra se pueden usar en Liquid en cualquier paso Mensaje que siga a un paso de [Rutas de acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths). Por ejemplo, cuando hagas referencia a `event_properties`, usa este fragmento de Liquid: {% raw %}``{{event_properties.${property_name}}}``{% endraw %}

{% alert important %}
`event_properties` no se puede usar de forma independiente de los pasos de Rutas de acción.
{% endalert %}

En el primer paso Mensaje que sigue a una ruta de acción, puedes usar `event_properties` relacionadas con el evento referenciado en esa ruta de acción. Puedes tener otros pasos (que no sean otro paso de Rutas de acción o Mensaje) entre este paso de Rutas de acción y el paso Mensaje. Ten en cuenta que solo tendrás acceso a `event_properties` si tu paso Mensaje se puede rastrear hasta una ruta que no sea El resto en un paso de ruta de acción.

{% alert important %}
No puedes usar `event_properties` en el paso Mensaje principal. En su lugar, debes usar `context` o añadir un paso de Rutas de acción con el evento correspondiente antes del paso Mensaje que incluye `event_properties`.
{% endalert %}

{% details Expandir para el editor de Canvas original %}

Ya no puedes crear ni duplicar Canvas usando el editor original. Esta sección está disponible solo como referencia.

- `event_properties` no se puede usar en pasos completos planificados. Sin embargo, puedes usar `event_properties` en el primer paso completo de un Canvas basado en acciones, incluso si el paso completo está planificado.
- `context` solo se puede referenciar en el primer paso completo de un Canvas.
- Específicamente para los canales de mensajes dentro de la aplicación, `context` se puede referenciar en el editor de Canvas original si tienes las propiedades de entrada persistentes habilitadas como parte del acceso anticipado anterior.

{% enddetails %}

## Análisis {#analytics}

Consulta la siguiente tabla para las definiciones de las métricas del componente Mensaje:

| Métrica | Descripción |
| --- | --- |
| _Entradas_ | El número de veces que se ha entrado en el paso. Si tu Canvas tiene reelegibilidad y un usuario entra en un paso Mensaje dos veces, se registrarán dos entradas. |
| _Avanzó al siguiente paso_ | El número de entradas que avanzaron al siguiente paso en el Canvas. |
| _Envíos_ | El número total de mensajes que el paso ha enviado. Si tu Canvas tiene reelegibilidad y un usuario entra en un paso Mensaje dos veces, se registrarán dos entradas. |
| _Destinatarios únicos_ | El número de usuarios que han recibido mensajes de este paso. |
| _Evento de conversión primaria_ | El número de veces que ocurrió un evento definido después de interactuar con o ver un mensaje recibido de una Campaign de Braze. Defines este evento al crear la Campaign. |
| _Ingresos_ | Los ingresos totales en dólares de los destinatarios de la Campaign dentro de la ventana de conversión primaria establecida. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Análisis" }