---
nav_title: Creación de tarjetas
article_title: Creación de tarjetas
alias: /card_creation/
description: "En este artículo se describen las diferencias entre la creación de Content Cards en el momento del lanzamiento de la campaña o de la entrada en el paso en Canvas y en la primera impresión."
page_order: 0
tool: Campaigns
channel:
  - content cards
toc_headers: h2
---

# Creación de tarjetas {#card-creation}

> Puedes elegir cuándo Braze evalúa la elegibilidad de la audiencia y la personalización para nuevas campañas de tarjeta de contenido y pasos en Canvas especificando cuándo se crea la tarjeta.

## Requisitos previos {#prerequisites}

Para aprovechar esta característica, debes actualizar a las siguientes versiones mínimas del SDK:

{% sdk_min_versions swift:5.2.0 android:23.0.0 web:4.2.0 %}

Tras actualizar el SDK, tus usuarios móviles deben actualizar su aplicación. Puedes filtrar la audiencia de tu campaña o Canvas para [dirigirte solo a usuarios con estas versiones mínimas de la aplicación]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).

## Resumen {#overview}

{% tabs %}
{% tab Campaign %}

Puedes elegir cuándo Braze crea una tarjeta en el paso **Delivery** al crear una nueva [campaña de tarjeta de contenido]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/) con entrega planificada.

![Sección Controles de la tarjeta de contenido al editar la entrega de una tarjeta de contenido planificada.]({% image_buster /assets/img_archive/card_creation.png %})

Las siguientes opciones están disponibles:

- **At campaign launch:** El comportamiento predeterminado anterior para las Content Cards. Braze calcula la elegibilidad de la audiencia y la personalización cuando se lanza la campaña, luego crea la tarjeta y la almacena hasta que el usuario abre tu aplicación.
- **At first impression (recomendado):** Cuando el usuario abre tu aplicación la próxima vez (inicia una nueva [sesión](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze determina para qué Content Cards es elegible el usuario, aplica las plantillas de personalización como Liquid o contenido conectado, y luego crea la tarjeta. Esta opción generalmente ofrece un mejor rendimiento.

Independientemente de la opción seleccionada, la cuenta regresiva de la fecha de expiración de la Content Card comienza cuando se lanza la campaña.

{% endtab %}
{% tab Canvas %}

Puedes elegir cuándo Braze crea una tarjeta en la pestaña **Messaging Channels** de un [paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) de Content Card.

![Sección Controles de la tarjeta de contenido al editar la entrega de una tarjeta de contenido planificada.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

Las siguientes opciones están disponibles:

- **At step entry:** El comportamiento predeterminado anterior para las Content Cards. Braze calcula la elegibilidad de la audiencia cuando el usuario entra en el paso en Canvas, luego crea la tarjeta y la almacena hasta que el usuario abre tu aplicación.
- **At first impression (recomendado):** Braze calcula la elegibilidad de la audiencia cuando el usuario entra en el paso en Canvas. Cuando el usuario abre tu aplicación la próxima vez (inicia una nueva [sesión](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze aplica las plantillas de personalización como Liquid o contenido conectado, y luego crea la tarjeta. Esta opción ofrece un mejor rendimiento en la entrega de tarjetas y una personalización más actualizada.

Independientemente de la opción seleccionada, la cuenta regresiva de la fecha de expiración de la Content Card comienza cuando el usuario entra en el paso en Canvas.

{% alert tip %}
Si quieres que los usuarios anónimos vean una Content Card en su primera sesión, usa una campaña en lugar de un Canvas. Esto se debe a que cuando un usuario anónimo entra en un Canvas, su sesión ya ha comenzado, por lo que no recibirá la Content Card hasta que inicie una nueva sesión.
{% endalert %}

### Evento de eliminación {#removal-event}

Selecciona la opción para eliminar Content Cards cuando los usuarios completan una compra o realizan un evento personalizado. Para usar **Perform Custom Event** como evento de eliminación, selecciona variables de contexto o atributos personalizados para las comparaciones al usar filtros de propiedades.

![Configuración de evento de eliminación de Content Card con Perform Custom Event seleccionado y filtros de propiedades usando variables de contexto o atributos personalizados.]({% image_buster /assets/img/content_card_removal_event.png %})

### Expiración {#expiration}

En la configuración de **Expiration (Time in Feed)**, puedes seleccionar **Personalize duration** para establecer la expiración de la Content Card usando variables de contexto.

![Configuración de expiración mostrando Personalize duration configurada con una variable de contexto para la expiración de la Content Card.]({% image_buster /assets/img/content_card_personalize_duration.png %})

{% alert important %}
Las Content Cards tienen una expiración máxima de 30 días, incluso cuando se usa la duración personalizada con variables de contexto. Cualquier valor establecido más allá de 30 días se limita a 30 días. Para más detalles, consulta [Expiración de la tarjeta]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/#card-expiration).
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
Para ambas opciones, después de que se crea una tarjeta, Braze no recalcula la elegibilidad de la audiencia ni la personalización.
{% endalert %}

### Diferencias entre crear tarjetas en el lanzamiento o entrada frente a la primera impresión {#differences}

Esta sección describe las principales diferencias entre la creación de tarjetas en el lanzamiento de la campaña o la entrada al paso frente a la primera impresión.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table aria-label="Differences between creating cards at launch or entry versus at first impression #differences" class="tg">
  <caption>Diferencias entre crear tarjetas en el lanzamiento o entrada frente a la primera impresión</caption>
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Cuando se lanza la campaña / En la entrada al paso en Canvas</th>
    <th class="tg-0pky">En la primera impresión</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">Cuándo usar esto</td>
    <td class="tg-0pky">Si necesitas que el contenido sea una instantánea en un momento específico (el momento del lanzamiento).</td>
    <td class="tg-0pky"><ul><li>Si necesitas mostrar tarjetas a usuarios nuevos o anónimos que puedan entrar en el segmento después del lanzamiento (<a href="#campaign_note">solo campañas*</a>).</li><li>Si estás usando personalización y quieres que el contenido más reciente esté disponible en la tarjeta.</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">Audiencia</td>
    <td class="tg-0pky">Braze evalúa la pertenencia a la audiencia cuando se envía la campaña.<br><br>Los usuarios nuevos o anónimos no serán evaluados para elegibilidad si intentan ver la tarjeta después de que se envíe la campaña. Para campañas recurrentes, esto será en el siguiente intervalo de recurrencia.</td>
    <td class="tg-0pky">Braze evalúa la pertenencia cuando el usuario abre tu aplicación la próxima vez (inicia una sesión, <a href="#campaign_note">solo campañas*</a>).<br><br> Esta configuración tendrá un alcance de audiencia más amplio porque cualquier usuario nuevo o anónimo siempre será evaluado para elegibilidad cuando intente ver la tarjeta. <br><br>Además, el límite de velocidad (limitar el número de personas que recibirán la tarjeta) no es aplicable cuando se configura en la primera impresión.</td>
  </tr>
  <tr>
    <td class="leftHeader">Personalización</td>
    <td class="tg-0pky">Braze evalúa Liquid, contenido conectado y Content Blocks en el momento en que se lanza la campaña o cuando un usuario entra en el paso en Canvas. Para campañas recurrentes, esto será en el siguiente intervalo de recurrencia.</td>
    <td class="tg-0pky">Braze evalúa Liquid, contenido conectado y Content Blocks en el momento de la primera impresión o después del siguiente intervalo de recurrencia.</td>
  </tr>
  <tr>
    <td class="leftHeader">Análisis</td>
  <td class="tg-0pky"><em>Messages Sent</em> se refiere al número de tarjetas que Braze creó y puso a disposición. Esto no cuenta si los usuarios vieron la tarjeta.</td>
  <td class="tg-0pky"><em>Messages Sent</em> se refiere al número de tarjetas que Braze envía a un usuario después del inicio de una sesión. En Canvas, si un usuario entra en el paso sin iniciar una sesión, Braze no envía una tarjeta, por lo que esta métrica puede no coincidir con el número de usuarios que entran en un paso.<br><br>Aunque los usuarios alcanzables y las impresiones no cambian, espera un volumen de envío más bajo (<em>Messages Sent</em>) cuando creas una tarjeta en la primera impresión en comparación con el lanzamiento de la campaña o la entrada al paso en Canvas.</td>
  </tr>
  <tr>
    <td class="leftHeader">Tiempo de procesamiento</td>
  <td class="tg-0pky">Braze crea tarjetas para cada usuario elegible en el segmento en el momento del lanzamiento. Para audiencias grandes, selecciona <b>At First Impression</b> para que las tarjetas estén disponibles más rápidamente después del lanzamiento.</td>
  <td class="tg-0pky">Braze crea una tarjeta la primera vez que un usuario intenta verla, por lo que puede tardar 1-2 segundos en mostrarse en la primera impresión.</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* Este escenario solo aplica a campañas, ya que la audiencia de Canvas se evalúa en la entrada al Canvas, no a nivel de paso.</sup></p>

## Consideraciones {#considerations}

### Campañas multicanal {#multichannel-campaigns}

Las campañas multicanal no admiten tarjetas en la primera impresión, por lo que todas las Content Cards se envían en el lanzamiento de la campaña.

### Uso de propiedades de contexto de Canvas {#using-canvas-context-properties}

Al personalizar Content Cards con [propiedades de contexto de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/), usa la sintaxis `${...}` (por ejemplo, {%raw%}`{{context.${property_name}}}`{%endraw%}). La notación de punto sin la sintaxis (por ejemplo, {%raw%}`{{context.property_name}}`{%endraw%}) puede no resolverse correctamente en las Content Cards, aunque funcione en otros canales como push y correo electrónico.

### Cambiar la creación de tarjetas después del lanzamiento {#changing-card-creation-after-launch}

Braze recomienda no cambiar cómo se crean las tarjetas después de que se haya lanzado una campaña. Debido a las diferencias en cómo se calcula *Messages Sent* entre los dos tipos de creación de tarjetas, cambiar cómo se crean las tarjetas después del lanzamiento de la campaña puede afectar la precisión de tu volumen de envío.

### Tiempo de procesamiento potencial {#potential-processing-time}

Para audiencias grandes, selecciona la opción de crear tarjetas en la primera impresión para que las tarjetas estén disponibles rápidamente después del lanzamiento. Las campañas desencadenadas al inicio de sesión también pueden beneficiarse de cambiar a la creación en la primera impresión (disponible a través de la entrega planificada) para mejorar el rendimiento.

Cuando las tarjetas se crean en la primera impresión, puede tardar unos segundos en procesarse. La duración de este tiempo de procesamiento depende de varios factores, como el tamaño de la tarjeta y la complejidad de las opciones de plantilla del mensaje. Por ejemplo, el tiempo de procesamiento para tarjetas que usan contenido conectado es al menos tan largo como el tiempo de respuesta del contenido conectado.

### Versiones anteriores del SDK {#previous-sdk-versions}

Si la aplicación de un usuario ejecuta una versión anterior del SDK, seguirá recibiendo las Content Cards que envíes. Sin embargo, las tarjetas tardarán más en aparecer y puede que no se muestren hasta la siguiente sincronización de Content Cards.