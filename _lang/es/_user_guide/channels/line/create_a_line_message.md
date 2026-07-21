---
nav_title: Crear un mensaje LINE
article_title: Crear un mensaje LINE
page_order: 1
description: "Este artículo explica cómo crear una campaña de mensajes LINE o un Canvas."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/
---

# Crear un mensaje LINE {#create-a-line-message}

> Las campañas de LINE pueden llegar directamente a tus clientes y chatear con ellos de forma programática. Puedes usar Liquid y otro contenido dinámico para crear una experiencia personal con tus usuarios y fomentar una experiencia de usuario discreta y enriquecedora con tu marca.

## Requisitos previos {#prerequisites}

Antes de crear un mensaje LINE, haz lo siguiente:

1. Lee el resumen de LINE.
2. Revisa las políticas, los límites y las reglas de contenido.
3. [Configura tu conexión LINE]({{site.baseurl}}/user_guide/channels/line/line_setup).

El envío de mensajes LINE desde Braze consumirá los créditos de mensajes o de acciones de tu cuenta.

## Paso 1: Elige dónde crear tu mensaje {#step-1-choose-where-to-build-your-message}

¿No estás seguro de si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para campañas de mensajería únicas y dirigidas, mientras que los Canvas son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaign %}

**Pasos:**

1. Ve a **Mensajería** > **Campaigns** y selecciona **Crear campaña**.
2. Selecciona **LINE** o, para campañas dirigidas a múltiples canales, selecciona **Campaña multicanal**.
3. Ponle a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) y [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) según sea necesario.
   * Las etiquetas facilitan encontrar tus campañas y generar informes a partir de ellas.
5. Añade y nombra tantas variantes como necesites para tu campaña. Puedes elegir diferentes plataformas, tipos de mensaje y diseños para cada una de las variantes añadidas. Para más información sobre este tema, consulta [Pruebas multivariante y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si todos los mensajes de tu campaña van a ser similares o tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. Luego puedes elegir **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Pasos:**

1. [Crea tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) usando el compositor de Canvas.
2. Después de configurar tu Canvas, añade un paso en el constructor de Canvas. Ponle a tu paso un nombre claro y significativo.
3. Elige una [planificación de paso]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) y especifica un retraso según sea necesario.
4. Filtra tu audiencia para este paso según sea necesario. Puedes refinar aún más los destinatarios de este paso especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se verificarán después del retraso, en el momento en que se envíen los mensajes.
5. Elige tu [comportamiento de avance]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases).
6. Elige cualquier otro canal de mensajería que desees combinar con tu mensaje.

{% endtab %}
{% endtabs %}

## Paso 2: Redacta tu mensaje LINE {#step-2-compose-your-line-message}

Escribe tu mensaje usando personalización (como Liquid o contenido conectado) según sea necesario. LINE permite hasta cinco burbujas de mensaje en cada mensaje, que pueden ser cualquiera de los diseños de mensaje disponibles: texto, imagen, enriquecido o basado en tarjetas.

![Compositor de LINE con un mensaje mostrado en la vista previa.]({% image_buster /assets/img/line/line_composer.png %})

### Consejos {#tips}

#### Uso de Liquid {#using-liquid}

Si planeas usar Liquid, asegúrate de incluir un valor predeterminado para tu personalización. Esto evitará que los destinatarios con perfiles de usuario incompletos reciban un marcador de posición en blanco. Por ejemplo, en lugar de que un usuario reciba el mensaje "¡Hola, !", podría recibir el mensaje "¡Hola, nuevo suscriptor!".

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Creación de mensajes de derecha a izquierda {#creating-right-to-left-messages}

La apariencia final de los mensajes de derecha a izquierda depende en gran medida de cómo los proveedores de servicios los renderizan. Para conocer las mejores prácticas sobre cómo crear mensajes de derecha a izquierda que se muestren con la mayor precisión posible, consulta [Creación de mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

## Paso 3: Previsualiza y prueba tu mensaje {#step-3-preview-and-test-your-message}

Cambia a la pestaña **Test** para enviar un mensaje LINE de prueba a grupos de prueba de contenido o a usuarios individuales, o previsualiza el mensaje como un usuario directamente en Braze.

![La pestaña "Tests" mostrando una vista previa de un mensaje de prueba.]({% image_buster /assets/img/line/test_preview.png %})

Para más información, consulta [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=line).

## Paso 4: Construye el resto de tu campaña o Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Construye el resto de tu campaña. Consulta las siguientes secciones para más detalles sobre cómo usar mejor nuestras herramientas para crear mensajes LINE.

### Elige la planificación de entrega o el desencadenante {#choose-delivery-schedule-or-trigger}

Los mensajes LINE pueden entregarse según un horario planificado, una acción o un desencadenante de API. Para más información sobre las opciones de planificación y desencadenantes, consulta [Planificar tu campaña]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Puedes especificar controles de entrega, como permitir que los usuarios vuelvan a ser [elegibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) para recibir la campaña, o activar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping). Para la entrega basada en acciones, también puedes establecer la duración de la campaña y las [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

### Elige los usuarios objetivo {#choose-users-to-target}

[Dirige a los usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) eligiendo segmentos o filtros para delimitar tu audiencia. Ya deberías haber elegido el grupo de suscripción, que filtra a los usuarios por el nivel o categoría de comunicación que desean tener contigo.

Selecciona la audiencia más amplia de tus segmentos y, opcionalmente, refina ese segmento aún más con nuestros [filtros]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters). Recibirás automáticamente una instantánea de cómo se ve aproximadamente la población de ese segmento. Ten en cuenta que la pertenencia exacta al segmento siempre se calcula antes de que se envíe el mensaje.

### Elige eventos de conversión {#choose-conversion-events}

Braze te permite rastrear con qué frecuencia los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), después de recibir una campaña. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se contará una conversión si el usuario realiza la acción especificada.

Los eventos de conversión te ayudan a medir el éxito de tu campaña. Por ejemplo:

- Si estás usando geotargeting para desencadenar un mensaje LINE cuyo objetivo final es que el usuario realice una compra, establece el evento de conversión como `Purchase`.
- Si estás intentando dirigir al usuario a tu aplicación, establece el evento de conversión como `Starts Session`.

También puedes establecer eventos de conversión personalizados según tu caso de uso específico. Sé creativo y piensa en cómo quieres medir el éxito de esta campaña.

{% endtab %}
{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, usar pruebas multivariante y selección inteligente, y más, consulta [Crear un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).

{% endtab %}
{% endtabs %}

## Paso 5: Revisa y despliega {#step-5-review-and-deploy}

Después de terminar de construir tu campaña o Canvas, revisa sus detalles, pruébala y luego ¡envíala!

A continuación, consulta [Informes de LINE]({{site.baseurl}}/line/reporting) para aprender cómo puedes acceder a los resultados de tus campañas de LINE.