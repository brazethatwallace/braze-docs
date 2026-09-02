---
nav_title: Crear un mensaje
article_title: Crear un mensaje servicio de mensajes cortos, MMS o RCS
page_order: 1
description: "Crea un mensaje servicio de mensajes cortos, MMS o RCS y configura los tipos de mensaje específicos del canal, campos, acortamiento de enlaces, configuración de entrega y comportamiento."
page_type: reference
alias: /create_sms_mms_rcs_message/
tool:
  - Campaigns
  - Canvas
channel:
  - SMS
  - MMS
  - RCS
search_rank: 1
---

# Crear un mensaje servicio de mensajes cortos, MMS o RCS {#create-an-sms-mms-or-rcs-message}

> Crea mensajes servicio de mensajes cortos, MMS y Rich Communication Services (RCS) personalizados en Campaigns o Canvas. El grupo de suscripción seleccionado determina qué tipos de mensaje y remitentes están disponibles.

## Requisitos previos {#prerequisites}

Antes de empezar, asegúrate de tener lo siguiente:

| Requisito | Descripción |
| --- | --- |
| Configuración del remitente | Completa la [configuración del remitente]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup). Para enviar MMS, tu grupo de suscripción necesita un número de teléfono habilitado para MMS. Para enviar RCS, completa la [configuración de RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup) y añade un remitente de RCS verificado. |
| Grupo de suscripción | Crea un [grupo de suscripción]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) que contenga los remitentes para este mensaje. |
| Números de teléfono y consentimiento de los usuarios | Importa los números de teléfono de los usuarios y recoge las [adhesiones voluntarias de servicio de mensajes cortos, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins) correspondientes. |
| Campaign o Canvas | Usa una Campaign para un mensaje único dirigido o Canvas para un recorrido de usuario con varios pasos. |
| Créditos de mensajes o de acción | Confirma que tu cuenta tiene créditos disponibles. El envío de mensajes servicio de mensajes cortos, MMS y RCS desde Braze utiliza estos créditos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos de mensajes servicio de mensajes cortos, MMS y RCS" }

## Crear un mensaje {#create-a-message}

### Paso 1: Elige dónde crear tu mensaje {#step-1-choose-where-to-build-your-message}

{% tabs %}
{% tab Campaign %}

1. Ve a **Mensajería** > **Campaigns** y selecciona **Crear Campaign**.
2. Selecciona **servicio de mensajes cortos/MMS/RCS** o, para campañas dirigidas a múltiples canales, selecciona **Campaign multicanal**.
3. Dale a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) y [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) según sea necesario.
  - Las etiquetas facilitan encontrar y usar tus campañas en los informes.
5. Añade y nombra las variantes de tu campaña. Puedes incluir variantes de servicio de mensajes cortos/MMS y RCS en la misma campaña. Para más información, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si las variantes de tu campaña tienen contenido similar, redacta primero el mensaje antes de añadir más variantes. Luego puedes seleccionar **Copiar de variante** en el menú desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

### Paso 2: Selecciona un grupo de suscripción y tipo de mensaje {#step-2-select-a-subscription-group-and-message-type}

Selecciona el **Grupo de suscripción** que contiene el remitente para este mensaje. Braze utiliza el grupo seleccionado para calcular la audiencia alcanzable y determinar la elegibilidad en el momento del envío.

El grupo de suscripción que selecciones determina qué tipos de mensaje están disponibles en el creador:

| Tipo de grupo de suscripción | Tipos de mensaje disponibles |
| --- | --- |
| Solo servicio de mensajes cortos | servicio de mensajes cortos |
| servicio de mensajes cortos con números habilitados para MMS | servicio de mensajes cortos y MMS |
| Habilitado para RCS con un remitente RCS verificado | RCS y servicio de mensajes cortos cuando el grupo también contiene un remitente servicio de mensajes cortos. MMS también está disponible cuando ese remitente está habilitado para MMS. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de mensaje disponibles por grupo de suscripción" }

{% alert tip %}
Añade al menos un remitente servicio de mensajes cortos a un grupo de suscripción RCS para poder enviar un servicio de mensajes cortos alternativo cuando la entrega de RCS falle.
{% endalert %}

Si el grupo de suscripción admite ambos protocolos, selecciona **servicio de mensajes cortos/MMS** o **RCS**. Para RCS, selecciona **Texto**, **Multimedia** o **Tarjeta**.

### Paso 3: Redacta tu mensaje {#step-3-compose-your-message}

Los campos y límites en el creador dependen del tipo de mensaje que hayas seleccionado.

{% tabs local %}
{% tab servicio de mensajes cortos y MMS %}

#### Campos y configuración de servicio de mensajes cortos y MMS {#sms-and-mms-fields-and-settings}

| Campo o configuración | Descripción |
| --- | --- |
| **Idioma** | Inserta contenido específico del idioma en el mensaje. |
| **Mensaje** | Introduce hasta 1600 caracteres, incluyendo Liquid, contenido conectado y emojis. El creador estima la codificación, el recuento de caracteres y el número de segmentos servicio de mensajes cortos facturables. Un mensaje MMS puede contener multimedia sin cuerpo del mensaje. |
| **Multimedia** | Para un grupo de suscripción habilitado para MMS, añade una imagen PNG, JPEG o GIF desde la biblioteca de medios o mediante URL. Puedes añadir una vCard en lugar de una imagen. |
| **Acortamiento de enlaces** | Acorta URLs HTTP y HTTPS y realiza un seguimiento de la participación. Para el acortamiento de enlaces heredado, selecciona seguimiento básico o avanzado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos y configuración de servicio de mensajes cortos y MMS" }

Los mensajes servicio de mensajes cortos utilizan la codificación GSM-7 o UCS-2 y se cobran por segmento de mensaje. Un solo carácter puede cambiar la codificación y aumentar el número de segmentos facturables. Para las reglas de codificación, tamaños de segmento y la calculadora de segmentos, consulta [Calculadoras de facturación de servicio de mensajes cortos y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator).

![Creador de SMS que muestra el texto del mensaje y sus recuentos estimados de caracteres y segmentos.]({% image_buster /assets/img/sms_campaign_compose.png %})

#### Especificaciones multimedia de MMS {#mms-media-specifications}

{% multi_lang_include channels/image_specs.md variable_name='servicio de mensajes cortos and mms' %}

Para enviar datos de la empresa que los usuarios puedan guardar en los contactos de su dispositivo, consulta [Tarjetas de contacto]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card). El envío de una tarjeta de contacto se cobra como un MMS.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

La disponibilidad y renderizado de MMS dependen del operador receptor. Cuando un operador no puede aceptar MMS, la multimedia se convierte en un enlace en el cuerpo del servicio de mensajes cortos a través del proveedor. Evita enviar MMS a números de Google Voice porque su soporte limitado de MMS puede causar entregas poco confiables.

Cuando un usuario envía multimedia entrante, Braze expone sus URLs en los [eventos de entrada de servicio de mensajes cortos en Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) y a través de {% raw %}`{{sms.${inbound_media_urls}}}`{% endraw %} en Liquid.

{% endtab %}
{% tab RCS %}

#### Tipos de mensaje RCS {#rcs-message-types}

| Tipo de mensaje | Campos y configuración | Límites y comportamiento |
| --- | --- | --- |
| **Texto** | Cuerpo del mensaje obligatorio, respuestas sugeridas opcionales o acciones de abrir URL, servicio de mensajes cortos alternativo opcional y acortamiento de enlaces | El cuerpo del mensaje puede contener hasta 1600 o 3072 caracteres, según el proveedor de servicios servicio de mensajes cortos. Añade hasta cinco sugerencias. |
| **Multimedia** | Imagen, video, documento o audio obligatorio; cuerpo del mensaje opcional; sugerencias opcionales, servicio de mensajes cortos alternativo y acortamiento de enlaces | El cuerpo del mensaje puede contener hasta 1600 o 3072 caracteres, según el proveedor, y se factura como un mensaje RCS adicional. Añade hasta cinco sugerencias. |
| **Tarjeta** | Tarjeta multimedia o tarjeta solo de texto, título, descripción, botones, sugerencias opcionales y servicio de mensajes cortos alternativo opcional | El título puede contener hasta 200 caracteres. La descripción puede contener hasta 1600 o 2000 caracteres, según el proveedor. Añade entre uno y cuatro botones. El soporte del proveedor determina si las tarjetas solo de texto y las sugerencias fuera de la tarjeta están disponibles. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipos de mensaje RCS, campos y límites" }

Las sugerencias pueden ser respuestas sugeridas, que prellenan la entrada de texto del usuario, o acciones de abrir URL. Añade hasta 25 caracteres de texto a cada sugerencia y una URL de hasta 2048 caracteres a cada acción de abrir URL.

Para cualquier tipo de mensaje RCS, activa **Enviar servicio de mensajes cortos si RCS falla** para añadir un mensaje alternativo de hasta 1600 caracteres. El grupo de suscripción seleccionado debe contener un remitente servicio de mensajes cortos. Para mensajes de tipo **Tarjeta**, los enlaces en la descripción no son clicables; usa un botón de abrir URL en su lugar.

Algunos proveedores de servicios servicio de mensajes cortos no admiten mensajes **Multimedia** independientes o tarjetas solo de texto. El creador muestra solo los tipos de mensaje RCS compatibles. Para mensajes de tipo **Tarjeta**, el acortamiento de enlaces se aplica solo a los enlaces en el servicio de mensajes cortos alternativo.

La facturación de mensajes RCS depende del tipo de mensaje y el contenido. Para las reglas de facturación de mensajes básicos, enriquecidos y tarjetas enriquecidas, consulta [Facturación de mensajes RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#rcs-message-billing).

#### Especificaciones multimedia de RCS {#rcs-media-specifications}

El creador acepta una URL multimedia de hasta 1000 caracteres. Los formatos disponibles y el tamaño máximo del archivo dependen del proveedor de servicios servicio de mensajes cortos.

| Tipo de archivo | Especificaciones |
| --- | --- |
| Todos | El tamaño máximo del archivo es de 16&nbsp;MB o 100&nbsp;MB, según el proveedor. |
| Imagen | JPEG, JPG, GIF, PNG |
| Video | H263, M4V, MP4, MPEG, MPEG-4, WEBM |
| Documento | PDF. Disponible para mensajes **Multimedia**, pero no para tarjetas multimedia. |
| Audio | AAC, MP3, MPEG, MP4, 3GPP, OGG. El soporte varía según el proveedor. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Especificaciones multimedia de RCS" }

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% endtabs %}

#### Personalización {#personalization}

Usa [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), emojis y contenido específico del idioma para personalizar tu mensaje. Incluye un valor predeterminado para la personalización de Liquid para que los perfiles con datos incompletos no reciban contenido en blanco.

Para crear texto del mensaje a partir de un prompt, usa [Generar texto]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy) con Operator.

Para idiomas que se escriben de derecha a izquierda, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Crear flujos de trabajo de mensajes conversacionales (RCS) {#create-conversational-message-workflows-rcs}

Los flujos de trabajo de mensajes conversacionales te permiten responder dinámicamente a los usuarios, creando una experiencia de mensajería de ida y vuelta. Para construir un flujo de trabajo, crea un Canvas y luego combina respuestas sugeridas con [Rutas de Acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) para dirigir tu flujo de trabajo según la respuesta que seleccione el usuario.

1. En el constructor de Canvas, crea un paso de mensaje RCS con múltiples respuestas sugeridas.

![Creador de mensajes RCS con respuestas sugeridas.]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. Conecta ese mensaje a una Ruta de Acción con un grupo de acción para cada respuesta sugerida.
3. Para cada grupo de acción:
   - Selecciona el desencadenador **Enviar un mensaje servicio de mensajes cortos entrante**.
   - Establece el cuerpo del mensaje para que sea igual a la respuesta sugerida correspondiente.

![Paso de Ruta de Acción configurado con tres grupos de acción, uno para cada respuesta sugerida.]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. Conecta cada grupo de acción a un paso de mensaje RCS, y luego añade contenido basado en la respuesta sugerida asociada.
5. Continúa el flujo de trabajo conversacional añadiendo respuestas sugeridas a cualquier mensaje de seguimiento.
6. Repite los pasos 2-4 hasta que el flujo de trabajo esté completo.

![Canvas que muestra un flujo de trabajo conversacional con dos Rutas de Acción.]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

### Paso 4: Configura el acortamiento de enlaces {#step-4-configure-link-shortening}

Activa **Acortamiento de enlaces** para acortar URLs HTTP y HTTPS y realizar el seguimiento de clics para enlaces de servicio de mensajes cortos, MMS y RCS compatibles. Según la versión disponible en tu espacio de trabajo, selecciona seguimiento básico o avanzado, o usa el acortamiento de enlaces unificado.

El seguimiento avanzado añade datos de clics a nivel de usuario para segmentación y reorientación. El acortamiento de enlaces unificado combina los enlaces acortados de servicio de mensajes cortos y RCS en un formato personalizado único. Para URLs compatibles, comportamiento de Liquid, requisitos de prueba, dominios personalizados y reorientación, consulta [Acortamiento de enlaces]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening).

Braze acorta hasta 25 enlaces en un mensaje. Una URL de más de 4000 caracteres no se puede acortar y provoca que el mensaje falle en el momento del envío.

### Paso 5: Previsualiza y prueba tu mensaje {#step-5-preview-and-test-your-message}

Ve a la pestaña **Prueba** para previsualizar el mensaje como un usuario o enviar un servicio de mensajes cortos, MMS o RCS de prueba a un [grupo de prueba de contenido]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) o a un usuario individual.

{% alert tip %}
Usa la [calculadora de segmentos servicio de mensajes cortos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator) para estimar cuántos segmentos contiene tu mensaje.
{% endalert %}

![Vista previa del texto SMS desde la pestaña Prueba del creador. En la sección de perfil, el campo Nombre está configurado como "James". En la sección de vista previa, el SMS ahora dice "Hi James, we appreciate your support!"]({% image_buster /assets/img/sms_campaign_test.png %})

Para MMS, el teléfono receptor determina si la multimedia aparece antes o después del cuerpo del mensaje.

{% alert note %}
Dado que el renderizado de RCS está controlado por el sistema operativo del usuario, el fabricante del dispositivo, el operador y la aplicación de mensajería (por ejemplo, Google Messages vs. Apple Messages), la apariencia del mensaje puede variar. La vista previa que se muestra en Braze puede no coincidir exactamente con lo que recibe un usuario final. Valida el renderizado final en dispositivos reales siempre que sea posible. Para detalles sobre el renderizado de RCS en dispositivos iOS, consulta [¿Por qué mi mensaje RCS no se renderiza con precisión en dispositivos iOS?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-doesnt-my-rcs-message-render-accurately-on-ios-devices). Para GIFs en tarjetas enriquecidas, consulta [¿Por qué los GIFs en tarjetas enriquecidas RCS aparecen estáticos en iOS?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-do-gifs-in-rcs-rich-cards-appear-static-on-ios).
{% endalert %}

Para más información, consulta [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=sms%2Fmms%20and%20rcs).

### Paso 6: Construye el resto de tu campaña o Canvas {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Elige un horario de entrega o desencadenador {#choose-a-delivery-schedule-or-trigger}

Entrega mensajes en un horario programado o en respuesta a una acción o un desencadenador de API. Para las opciones de programación y desencadenadores, consulta [Programar tu campaña]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Configura controles de entrega como la [reelegibilidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) y la [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping). Para la entrega basada en acciones, establece la duración de la campaña y las [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

#### Elige los usuarios a los que dirigirte {#choose-users-to-target}

[Dirige a los usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) seleccionando Segments y filtros. Braze calcula la pertenencia exacta al Segment antes de enviar el mensaje.

El grupo de suscripción seleccionado filtra los usuarios suscritos. Los destinatarios de servicio de mensajes cortos y MMS también necesitan un número de teléfono válido. Los destinatarios de RCS necesitan un dispositivo y una conexión de operador compatibles con RCS; usa un servicio de mensajes cortos alternativo para llegar a los usuarios elegibles cuando la entrega de RCS falle.

{% multi_lang_include audience/target_audiences.md %}

Para la segmentación por clics e interacciones, consulta [Reorientación de usuarios]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting).

#### Elige eventos de conversión {#choose-conversion-events}

Usa [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) para medir las acciones después de que un usuario reciba la campaña. Establece una ventana de conversión de hasta 30 días.

{% endtab %}
{% tab Canvas %}

Completa las secciones restantes de tu Canvas. Para horarios de entrada, configuración de audiencia y controles de envío, consulta [Crear un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).

{% endtab %}
{% endtabs %}

### Paso 7: Revisa y despliega {#step-7-review-and-deploy}

Una vez que hayas terminado de construir tu campaña o Canvas, revisa sus detalles y prueba el mensaje antes de enviarlo.

Después del lanzamiento, usa los [informes de servicio de mensajes cortos, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting) para revisar el rendimiento del mensaje.

## Cosas que debes saber {#things-to-know}

- Los servicio de mensajes cortos se cobran por segmento del mensaje, los MMS a su propia tarifa y los RCS por tipo de mensaje. Revisa las [calculadoras de facturación de servicio de mensajes cortos y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator) antes de enviar.
- MMS admite una imagen o vCard. La compatibilidad del operador determina si los destinatarios reciben el medio o un enlace a la imagen.
- Las capacidades y los límites de RCS varían según el proveedor de servicios de servicio de mensajes cortos. El creador muestra solo las opciones disponibles para el grupo de suscripción seleccionado.
- Puedes enviar un correo de voz pregrabado como audio en un mensaje RCS de tipo **Multimedia**.
- El renderizado y el comportamiento de interacción varían según el dispositivo, el operador, el sistema operativo y la aplicación de mensajería.