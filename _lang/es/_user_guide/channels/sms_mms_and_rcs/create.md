---
nav_title: Crear un mensaje
article_title: Crear un mensaje SMS, MMS o RCS
page_order: 1
description: "Crea un mensaje SMS, MMS o RCS y configura los tipos de mensaje específicos del canal, campos, acortamiento de enlaces, configuración de entrega y comportamiento."
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

# Crear un mensaje SMS, MMS o RCS {#create-an-sms-mms-or-rcs-message}

> Crea mensajes SMS, MMS y Rich Communication Services (RCS) personalizados en Campaigns o Canvas. El grupo de suscripción seleccionado determina qué tipos de mensaje y remitentes están disponibles.

## Requisitos previos {#prerequisites}

Antes de empezar, asegúrate de tener lo siguiente:

| Requisito | Descripción |
| --- | --- |
| Configuración del remitente | Completa la [configuración del remitente]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup). Para enviar MMS, tu grupo de suscripción necesita un número de teléfono habilitado para MMS. Para enviar RCS, completa la [configuración de RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup) y añade un remitente RCS verificado. |
| Grupo de suscripción | Crea un [grupo de suscripción]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) que contenga los remitentes para este mensaje. |
| Números de teléfono y consentimiento de los usuarios | Importa los números de teléfono de los usuarios y recopila las [adhesiones voluntarias de SMS, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins) correspondientes. |
| Campaign o Canvas | Usa una Campaign para un mensaje único dirigido o un Canvas para un recorrido de usuario de varios pasos. |
| Créditos de mensaje o de acción | Confirma que tu cuenta tiene créditos disponibles. El envío de mensajes SMS, MMS y RCS desde Braze utiliza estos créditos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos de mensajes SMS, MMS y RCS" }

## Crear un mensaje {#create-a-message}

### Paso 1: Elige dónde crear tu mensaje {#step-1-choose-where-to-build-your-message}

{% tabs %}
{% tab Campaign %}

1. Ve a **Mensajería** > **Campaigns** y selecciona **Crear Campaign**.
2. Selecciona **SMS/MMS/RCS** o, para Campaigns dirigidas a varios canales, selecciona **Campaign multicanal**.
3. Asigna a tu Campaign un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) y [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) según sea necesario.
  - Las etiquetas facilitan encontrar tus Campaigns y usarlas en informes.
5. Añade y nombra las variantes de tu Campaign. Puedes incluir variantes de SMS/MMS y RCS en la misma Campaign. Para más información, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si las variantes de tu Campaign tienen contenido similar, redacta el primer mensaje antes de añadir más variantes. Luego puedes seleccionar **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

### Paso 2: Selecciona un grupo de suscripción y tipo de mensaje {#step-2-select-a-subscription-group-and-message-type}

Selecciona el **grupo de suscripción** que contiene el remitente para este mensaje. Braze utiliza el grupo seleccionado para calcular la audiencia alcanzable y determinar la elegibilidad en el momento del envío.

El grupo de suscripción que selecciones determina qué tipos de mensaje están disponibles en el creador:

| Tipo de grupo de suscripción | Tipos de mensaje disponibles |
| --- | --- |
| Solo SMS | SMS |
| SMS con números habilitados para MMS | SMS y MMS |
| Habilitado para RCS con un remitente RCS verificado | RCS y SMS cuando el grupo también contiene un remitente SMS. MMS también está disponible cuando ese remitente está habilitado para MMS. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de mensaje disponibles por grupo de suscripción" }

{% alert tip %}
Añade al menos un remitente SMS a un grupo de suscripción RCS para poder enviar un SMS alternativo cuando falle la entrega RCS.
{% endalert %}

Si el grupo de suscripción admite ambos protocolos, selecciona **SMS/MMS** o **RCS**. Para RCS, selecciona **Texto**, **Multimedia** o **Tarjeta**.

### Paso 3: Redacta tu mensaje {#step-3-compose-your-message}

Los campos y límites en el creador dependen del tipo de mensaje que hayas seleccionado.

{% tabs local %}
{% tab SMS y MMS %}

#### Campos y configuración de SMS y MMS {#sms-and-mms-fields-and-settings}

| Campo o configuración | Descripción |
| --- | --- |
| **Idioma** | Inserta contenido específico del idioma en el mensaje. |
| **Mensaje** | Introduce hasta 1600 caracteres, incluyendo Liquid, contenido conectado y emojis. El creador estima la codificación, el recuento de caracteres y el número de segmentos de SMS facturables. Un mensaje MMS puede contener multimedia sin cuerpo de mensaje. |
| **Multimedia** | Para un grupo de suscripción habilitado para MMS, añade una imagen PNG, JPEG o GIF desde la biblioteca de medios o por URL. Puedes añadir una vCard en lugar de una imagen. |
| **Acortamiento de enlaces** | Acorta URLs HTTP y HTTPS y realiza seguimiento de la participación. Para el acortamiento de enlaces heredado, selecciona seguimiento básico o avanzado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos y configuración de SMS y MMS" }

Los mensajes SMS utilizan codificación GSM-7 o UCS-2 y se cobran por segmento de mensaje. Un solo carácter puede cambiar la codificación y aumentar el número de segmentos facturables. Para las reglas de codificación, tamaños de segmento y la calculadora de segmentos, consulta [Calculadoras de facturación de SMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator).

![Creador de SMS que muestra el texto del mensaje y sus recuentos estimados de caracteres y segmentos.]({% image_buster /assets/img/sms_campaign_compose.png %})

#### Especificaciones de multimedia MMS {#mms-media-specifications}

{% multi_lang_include channels/image_specs.md variable_name='sms and mms' %}

Para enviar datos de contacto empresarial que los usuarios puedan guardar en los contactos de su dispositivo, consulta [Tarjetas de contacto]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card). El envío de una tarjeta de contacto se cobra como un MMS.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

La disponibilidad y representación de MMS dependen del operador receptor. Cuando un operador no puede aceptar MMS, la multimedia se convierte en un enlace en el cuerpo del SMS a través del proveedor. Evita enviar MMS a números de Google Voice porque su soporte limitado de MMS puede causar entregas poco fiables.

Cuando un usuario envía multimedia entrante, Braze expone sus URLs en los [eventos entrantes de SMS en Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) y a través de {% raw %}`{{sms.${inbound_media_urls}}}`{% endraw %} en Liquid.

{% endtab %}
{% tab RCS %}

#### Tipos de mensaje RCS {#rcs-message-types}

| Tipo de mensaje | Campos y configuración | Límites y comportamiento |
| --- | --- | --- |
| **Texto** | Cuerpo de mensaje obligatorio, respuestas sugeridas opcionales o acciones de abrir URL, alternativa SMS opcional y acortamiento de enlaces | El cuerpo del mensaje puede contener hasta 1600 o 3072 caracteres, según el proveedor de servicio de SMS. Añade hasta cinco sugerencias. |
| **Multimedia** | Imagen, video, documento o audio obligatorio; cuerpo de mensaje opcional; sugerencias opcionales, alternativa SMS y acortamiento de enlaces | El cuerpo del mensaje puede contener hasta 1600 o 3072 caracteres, según el proveedor, y se factura como un mensaje RCS adicional. Añade hasta cinco sugerencias. No todos los proveedores admiten mensajes de **multimedia** independientes (por ejemplo, Twilio). |
| **Tarjeta** | Tarjeta multimedia o tarjeta solo texto, título, descripción, botones, sugerencias opcionales y alternativa SMS opcional | El título puede contener hasta 200 caracteres. La descripción puede contener hasta 1600 o 2000 caracteres, según el proveedor. Añade entre uno y cuatro botones. Consulta [Soporte del proveedor para mensajes de tarjeta](#provider-support-for-card-messages) para disponibilidad de diseño y campos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipos de mensaje RCS, campos y límites" }

#### Diseños de tarjeta {#card-layouts}

Los mensajes de **tarjeta** RCS combinan multimedia, texto y botones en una sola unidad. Elige un diseño en el creador:

| Diseño de tarjeta | Campos obligatorios | Campos opcionales |
| --- | --- | --- |
| **Solo texto** | Título, descripción y al menos un botón de tarjeta | Hasta tres botones de tarjeta adicionales, sugerencias fuera de la tarjeta (cuando se admiten) y alternativa SMS |
| **Multimedia** | Imagen, GIF o video y al menos un botón de tarjeta | Título, descripción, hasta tres botones de tarjeta adicionales, sugerencias fuera de la tarjeta (cuando se admiten) y alternativa SMS |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Diseños de tarjeta RCS" }

Usa Liquid para personalizar títulos, descripciones, multimedia y botones de tarjeta. Las URLs introducidas como texto plano en el título o la descripción no son clicables: añade un botón de tarjeta **Abrir URL** en su lugar.

Las sugerencias pueden ser respuestas sugeridas, que rellenan previamente la entrada de texto del usuario, o acciones de abrir URL. Añade hasta 25 caracteres de texto a cada sugerencia y una URL de hasta 2048 caracteres a cada acción de abrir URL. Activa **Enviar SMS si RCS falla** para añadir un mensaje alternativo de hasta 1600 caracteres cuando falle la entrega RCS. El grupo de suscripción seleccionado debe contener un remitente SMS. El acortamiento de enlaces se aplica solo a los enlaces en el cuerpo del SMS alternativo, no a las URLs de los botones de tarjeta.

La facturación de mensajes RCS depende del tipo de mensaje y el contenido. Para las reglas de facturación de mensajes básicos, enriquecidos y de tarjeta enriquecida, consulta [Facturación de mensajes RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#rcs-message-billing).

#### Soporte del proveedor para mensajes de tarjeta {#provider-support-for-card-messages}

La disponibilidad de tipos de mensaje RCS y opciones de tarjeta depende de tu proveedor de servicio de SMS. El creador muestra solo los tipos y campos admitidos.

| Capacidad | Infobip | Twilio |
| --- | --- | --- |
| Tipo de mensaje **multimedia** independiente | Admitido | No admitido |
| Diseño de tarjeta solo texto | Admitido | No admitido |
| Diseño de tarjeta multimedia | Admitido | Admitido |
| Sugerencias fuera de la tarjeta | Admitidas | No admitidas |
| Botones de tarjeta | Admitidos (1–4) | Admitidos (1–4) |
| Límite de caracteres de descripción | Hasta 2000 caracteres | Hasta 1600 caracteres |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Soporte del proveedor para mensajes de tarjeta RCS" }

#### Especificaciones de multimedia RCS {#rcs-media-specifications}

El creador acepta una URL de multimedia con hasta 1000 caracteres. Los formatos disponibles y el tamaño máximo de archivo dependen del proveedor de servicio de SMS.

| Tipo de archivo | Especificaciones |
| --- | --- |
| Todos | El tamaño máximo de archivo es de 16&nbsp;MB o 100&nbsp;MB, según el proveedor. |
| Imagen | JPEG, JPG, GIF, PNG |
| Video | H263, M4V, MP4, MPEG, MPEG-4, WEBM |
| Documento | PDF. Disponible para mensajes **multimedia**, pero no para tarjetas multimedia. |
| Audio | AAC, MP3, MPEG, MP4, 3GPP, OGG. El soporte del proveedor varía. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Especificaciones de multimedia RCS" }

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% endtabs %}

#### Personalización {#personalization}

Usa [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), emojis y contenido específico del idioma para personalizar tu mensaje. Incluye un valor predeterminado para la personalización con Liquid para que los perfiles con datos incompletos no reciban contenido en blanco.

Para crear el texto del mensaje a partir de una indicación, usa [Generar texto]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy) con Operator.

Para idiomas escritos de derecha a izquierda, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Crear flujos de trabajo de mensajes conversacionales (RCS) {#create-conversational-message-workflows-rcs}

Los flujos de trabajo de mensajes conversacionales te permiten responder dinámicamente a los usuarios, creando una experiencia de mensajería bidireccional. Para crear un flujo de trabajo, crea un Canvas y luego combina respuestas sugeridas con [Rutas de Acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) para dirigir tu flujo de trabajo en función de la respuesta que seleccione el usuario.

1. En el constructor de Canvas, crea un paso de mensaje RCS con múltiples respuestas sugeridas.

![Creador de mensajes RCS con respuestas sugeridas.]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. Conecta ese mensaje a una Ruta de Acción con un grupo de acción para cada respuesta sugerida.
3. Para cada grupo de acción:
   - Selecciona el desencadenante **Enviar un mensaje SMS entrante**.
   - Configura el cuerpo del mensaje para que sea igual a la respuesta sugerida correspondiente.

![Paso de Ruta de Acción configurado con tres grupos de acción, uno para cada respuesta sugerida.]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. Conecta cada grupo de acción a un paso de mensaje RCS y luego añade contenido basado en la respuesta sugerida asociada.
5. Continúa el flujo de trabajo conversacional añadiendo respuestas sugeridas a cualquier mensaje de seguimiento.
6. Repite los pasos 2 a 4 hasta que el flujo de trabajo esté completo.

![Canvas que muestra un flujo de trabajo conversacional con dos Rutas de Acción.]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

### Paso 4: Configura el acortamiento de enlaces {#step-4-configure-link-shortening}

Activa **Acortamiento de enlaces** para acortar URLs HTTP y HTTPS y realizar seguimiento de clics para enlaces de SMS, MMS y RCS compatibles. Según la versión disponible en tu espacio de trabajo, selecciona seguimiento básico o avanzado, o usa el acortamiento de enlaces unificado.

El seguimiento avanzado añade datos de clics a nivel de usuario para la segmentación y reorientación. El acortamiento de enlaces unificado combina los enlaces acortados de SMS y RCS en un formato personalizado. Para URLs admitidas, comportamiento de Liquid, requisitos de prueba, dominios personalizados y reorientación, consulta [Acortamiento de enlaces]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening).

Braze acorta hasta 25 enlaces en un mensaje. Una URL de más de 4000 caracteres no se puede acortar y provoca que el mensaje falle en el momento del envío.

### Paso 5: Previsualiza y prueba tu mensaje {#step-5-preview-and-test-your-message}

Ve a la pestaña **Prueba** para previsualizar el mensaje como un usuario o enviar un SMS, MMS o mensaje RCS de prueba a un [grupo de prueba de contenido]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) o a un usuario individual.

{% alert tip %}
Usa la [calculadora de segmentos de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator) para estimar cuántos segmentos contiene tu mensaje.
{% endalert %}

![Vista previa del texto del SMS desde la pestaña Prueba del creador. En la sección del perfil, el campo nombre está configurado como "James". En la sección de vista previa, el SMS ahora dice "Hi James, we appreciate your support!"]({% image_buster /assets/img/sms_campaign_test.png %})

Para MMS, el teléfono receptor determina si la multimedia aparece antes o después del cuerpo del mensaje.

{% alert note %}
Dado que la representación de RCS está controlada por el sistema operativo del usuario, el fabricante del dispositivo, el operador y la aplicación de mensajería (por ejemplo, Google Messages frente a Apple Messages), la apariencia del mensaje puede variar. La vista previa que se muestra en Braze puede no coincidir exactamente con lo que recibe un usuario final. Valida la representación final en dispositivos reales siempre que sea posible. Para más detalles sobre la representación de RCS en dispositivos iOS, consulta [¿Por qué mi mensaje RCS no se representa con precisión en dispositivos iOS?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-doesnt-my-rcs-message-render-accurately-on-ios-devices). Para GIFs en tarjetas enriquecidas, consulta [¿Por qué los GIFs en tarjetas enriquecidas RCS aparecen estáticos en iOS?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-do-gifs-in-rcs-rich-cards-appear-static-on-ios).
{% endalert %}

Para más información, consulta [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=sms%2Fmms%20and%20rcs).

### Paso 6: Construye el resto de tu Campaign o Canvas {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Elige un programa de entrega o desencadenante {#choose-a-delivery-schedule-or-trigger}

Entrega mensajes en un momento programado o en respuesta a una acción o desencadenante de API. Para opciones de programación y desencadenantes, consulta [Programa tu Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Configura controles de entrega como la [reelegibilidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) y la [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping). Para la entrega basada en acciones, configura la duración de la Campaign y las [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

#### Elige los usuarios a los que dirigirte {#choose-users-to-target}

[Segmenta a los usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) seleccionando Segments y filtros. Braze calcula la membresía exacta del Segment antes de enviar el mensaje.

El grupo de suscripción seleccionado filtra a los usuarios suscritos. Los destinatarios de SMS y MMS también necesitan un número de teléfono válido. Los destinatarios de RCS necesitan un dispositivo y conexión de operador compatibles con RCS; usa una alternativa SMS para llegar a los usuarios elegibles cuando falle la entrega RCS.

{% multi_lang_include audience/target_audiences.md %}

Para la segmentación por clics e interacciones, consulta [Reorientación de usuarios]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting).

#### Elige eventos de conversión {#choose-conversion-events}

Usa [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) para medir acciones después de que un usuario reciba la Campaign. Configura una ventana de conversión de hasta 30 días.

{% endtab %}
{% tab Canvas %}

Completa las secciones restantes de tu Canvas. Para programas de entrada, configuración de audiencia y controles de envío, consulta [Crear un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).

{% endtab %}
{% endtabs %}

### Paso 7: Revisa e implementa {#step-7-review-and-deploy}

Después de terminar de crear tu Campaign o Canvas, revisa sus detalles y prueba el mensaje antes de enviarlo.

Después del lanzamiento, usa los [informes de SMS, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting) para revisar el rendimiento del mensaje.

## Aspectos a tener en cuenta {#things-to-know}

- El servicio de mensajes cortos se cobra por segmento del mensaje, los MMS tienen su propia tarifa y los RCS se cobran por tipo de mensaje. Revisa las [calculadoras de facturación de SMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator) antes de enviar.
- Los MMS admiten una imagen o una vCard. La compatibilidad del operador determina si los destinatarios reciben el contenido multimedia o un enlace a la imagen.
- Las capacidades y límites de RCS varían según el proveedor de servicios de SMS. El creador muestra solo las opciones disponibles para el grupo de suscripción seleccionado.
- Puedes enviar un mensaje de voz pregrabado como audio en un mensaje RCS de tipo **Multimedia**.
- El comportamiento de visualización e interacción varía según el dispositivo, el operador, el sistema operativo y la aplicación de mensajería.