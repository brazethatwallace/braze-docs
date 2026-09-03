---
nav_title: Crear un mensaje LINE
article_title: Crear un mensaje LINE
page_order: 1
description: "Crea un mensaje LINE y configura tipos de mensaje específicos del canal, campos, seguimiento de clics, configuración de entrega y comportamiento."
page_type: reference
tool:
  - Campaigns
  - Canvas
channel:
  - LINE
alias: /line/create/
---

# Crear un mensaje LINE {#create-a-line-message}

> Crea mensajes LINE personalizados en Campaigns o Canvas. Elige entre mensajes de texto, imagen, enriquecidos y basados en tarjetas, y combina hasta cinco mensajes en un solo envío.

## Requisitos previos {#prerequisites}

Antes de empezar, asegúrate de tener lo siguiente:

| Requisito | Descripción |
| --- | --- |
| Conexión con LINE | Completa la [configuración de LINE]({{site.baseurl}}/user_guide/channels/line/line_setup) y revisa las políticas, los límites y las reglas de contenido del canal. |
| Campaign o Canvas | Usa una Campaign para un único mensaje dirigido o un Canvas para un recorrido de usuario con varios pasos. |
| Plan de mensaje | Prepara tu contenido, imágenes, enlaces y grupo de suscripción. |
| Créditos de mensajes o acciones | Confirma que tu cuenta tiene créditos disponibles. El envío de mensajes de LINE desde Braze consume estos créditos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos de mensajes de LINE" }

## Crear un mensaje {#create-a-message}

### Paso 1: Elige dónde crear tu mensaje {#step-1-choose-where-to-build-your-message}

{% tabs %}
{% tab Campaign %}

1. Ve a **Messaging** > **Campaigns** y selecciona **Create Campaign**.
2. Selecciona **LINE** o, para campañas dirigidas a varios canales, selecciona **Multichannel Campaign**.
3. Asigna a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) y [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) según sea necesario.
   * Las etiquetas facilitan encontrar y usar tus campañas en los informes.
5. Añade y nombra las variantes de tu campaña. Cada variante puede usar diferentes tipos de mensaje y diseños. Para más información, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si las variantes de tu campaña tienen contenido similar, redacta el primer mensaje antes de añadir más variantes. Luego puedes seleccionar **Copy from Variant** en el desplegable **Add Variant**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

### Paso 2: Selecciona un grupo de suscripción {#step-2-select-a-subscription-group}

Selecciona el **grupo de suscripción** asociado al canal LINE que envía el mensaje. Se requiere un grupo de suscripción antes de poder abrir el editor.

Todas las variantes en una campaña de LINE deben usar el mismo grupo de suscripción. Para más información sobre los estados de suscripción de LINE, consulta [Grupos de suscripción de LINE]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups).

### Paso 3: Redacta tu mensaje de LINE {#step-3-compose-your-line-message}

Selecciona **Launch editor** y luego arrastra los tipos de mensaje al editor. Combina hasta cinco mensajes en un solo envío y ordénalos en el orden en que los usuarios los recibirán.

![Creador de LINE con un mensaje mostrado en la vista previa.]({% image_buster /assets/img/line/line_composer.png %})

#### Tipos de mensaje {#message-types}

| Tipo de mensaje | Campos y configuración | Límites y comportamiento |
| --- | --- | --- |
| **Texto** | Cuerpo del mensaje con emojis, Liquid y URL | Hasta 5000 caracteres. |
| **Imagen** | Imagen de la biblioteca de medios o una URL, incluida una URL dinámica | Las URL de imagen pueden contener hasta 2000 caracteres. Los mensajes de imagen independientes no admiten acciones de clic. |
| **Mensaje enriquecido** | Imagen, texto alternativo, plantilla y áreas interactivas con acciones URI | El texto alternativo puede contener hasta 400 caracteres. Añade entre una y 50 áreas interactivas. Las etiquetas de acción pueden contener hasta 100 caracteres, y cada URI puede contener hasta 1000 caracteres. |
| **Mensaje basado en tarjetas** | Hasta 10 tarjetas con una imagen y encabezado opcionales, cuerpo obligatorio y acciones URI | El texto alternativo puede contener hasta 400 caracteres. Un encabezado puede contener hasta 40 caracteres. Un cuerpo puede contener hasta 60 caracteres con imagen o encabezado, o 120 caracteres sin ninguno de los dos. Cada tarjeta requiere entre una y tres acciones con etiquetas de hasta 20 caracteres. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipos de mensaje de LINE, campos y límites" }

Los límites de caracteres excluyen la sintaxis Liquid.

Para especificaciones de imagen, plantillas de mensajes enriquecidos, configuraciones de imágenes de carrusel y ejemplos, consulta [Tipos de mensaje de LINE]({{site.baseurl}}/user_guide/channels/line/create_a_line_message/message_types).

{% alert note %}
Los mensajes basados en tarjetas aplican los mismos campos opcionales y número de acciones a cada tarjeta. Por ejemplo, si una tarjeta incluye una imagen y dos acciones, todas las tarjetas deben incluir una imagen y dos acciones.
{% endalert %}

#### Comportamiento al hacer clic {#on-click-behavior}

Para las áreas interactivas en mensajes enriquecidos y tarjetas, selecciona **URI** en **On-click behavior** y luego introduce el destino en **Open URL**. Elige si la URL se abre dentro de LINE.

#### Personalización {#personalization}

Usa [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) o [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) para personalizar texto, imágenes y URL. Incluye un valor predeterminado para la personalización con Liquid para que los perfiles con datos incompletos no reciban contenido en blanco.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Para idiomas escritos de derecha a izquierda, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

### Paso 4: Configura el seguimiento de clics {#step-4-configure-click-tracking}

En la pestaña **Settings**, usa **Click Tracking** para acortar y rastrear enlaces en el momento del envío. El seguimiento de clics está activado de forma predeterminada para los mensajes nuevos y se aplica a las URL HTTP y HTTPS en mensajes de texto, enriquecidos y basados en tarjetas.

Braze usa `https://brz.ai` o el dominio personalizado configurado para el grupo de suscripción. Puedes personalizar las URL rastreadas con Liquid. Para la configuración por tipo de mensaje, el comportamiento de pruebas, los dominios personalizados y la reorientación, consulta [Seguimiento de clics en LINE]({{site.baseurl}}/user_guide/channels/line/create_a_line_message/line_click_tracking).

### Paso 5: Previsualiza y prueba tu mensaje {#step-5-preview-and-test-your-message}

Ve a la pestaña **Preview & Test** para previsualizar el mensaje como un usuario o enviar un mensaje de prueba de LINE a un grupo de prueba de contenido o a un usuario individual.

![La pestaña Preview & Test mostrando una vista previa de un mensaje de prueba.]({% image_buster /assets/img/line/test_preview.png %})

Para los requisitos y pasos de prueba, consulta [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=line).

### Paso 6: Completa el resto de tu campaña o Canvas {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Elige un horario de entrega o desencadenante {#choose-a-delivery-schedule-or-trigger}

Entrega mensajes de LINE a una hora programada o en respuesta a una acción o desencadenante de API. Para las opciones de programación y desencadenantes, consulta [Programar tu campaña]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Configura los controles de entrega, como la [reelegibilidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) y la [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping). Para la entrega basada en acciones, configura la duración de la campaña y las [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

#### Elige los usuarios a los que dirigirte {#choose-users-to-target}

[Segmenta a los usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) seleccionando segmentos y filtros. Braze calcula la pertenencia exacta al segmento antes de enviar el mensaje.

LINE controla el estado de suscripción de cada usuario. Un usuario debe tener un `native_line_id` y seguir el canal LINE asociado al grupo de suscripción seleccionado para recibir el mensaje. Para más detalles, consulta [Estado de suscripción de LINE]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#line).

#### Elige los eventos de conversión {#choose-conversion-events}

Usa los [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) para medir las acciones realizadas después de que un usuario reciba la campaña. Establece una ventana de conversión de hasta 30 días.

{% endtab %}
{% tab Canvas %}

Completa las secciones restantes de tu Canvas. Para los horarios de entrada, la configuración de audiencia y los controles de envío, consulta [Crear un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).

Puedes usar mensajes entrantes de LINE para iniciar o ramificar un Canvas basándote en palabras desencadenantes. Para los requisitos de comportamiento y uso de mayúsculas, consulta [Enviar mensajes a usuarios de LINE]({{site.baseurl}}/user_guide/channels/line/message_users).

{% endtab %}
{% endtabs %}

### Paso 7: Revisa y despliega {#step-7-review-and-deploy}

Cuando hayas terminado de crear tu campaña o Canvas, revisa los detalles y prueba el mensaje antes de enviarlo.

Después del lanzamiento, usa los [informes de LINE]({{site.baseurl}}/user_guide/channels/line/reporting) para revisar el rendimiento de los mensajes.

## Cosas que debes saber {#things-to-know}

- Un mensaje de LINE puede contener entre una y cinco burbujas de mensaje.
- Un grupo de suscripción se asigna a un canal de LINE, y todas las variantes de una campaña deben usar el mismo grupo de suscripción.
- LINE es la fuente de verdad para el estado de suscripción. Los usuarios que no siguen el canal de LINE seleccionado no reciben el mensaje.
- LINE calcula las estadísticas de aperturas y clics solo cuando más de 20 usuarios realizan el evento en un día determinado.