---
nav_title: "Crear un mensaje RCS"
article_title: "Crear un mensaje RCS"
permalink: /create_rcs_message/
description: "Este artículo explica cómo crear un mensaje RCS."
hidden: true
---

# Crear un mensaje RCS {#creating-an-rcs-message}

> Las campañas RCS son ideales para comunicarte directamente con tus clientes y conversar con ellos de forma programática. Puedes usar Liquid y otro contenido dinámico para crear una experiencia personalizada con tus usuarios y fomentar una experiencia de usuario discreta y enriquecedora con tu marca.

## Creación de un mensaje RCS

### Paso 1: Elige dónde crear tu mensaje {#step-1-choose-where-to-build-your-message}

¿No tienes claro si tu mensaje debe enviarse mediante una Campaign o un Canvas? Las Campaigns son mejores para campañas de mensajería sencillas y únicas, mientras que los Canvas son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaign %}
1. Ve a **Mensajería** > **Campaigns** y selecciona **Crear Campaign**.
2. Selecciona **SMS/MMS/RCS** o, para Campaigns dirigidas a varios canales, selecciona **Multicanal**.
3. Asigna a tu Campaign un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) y [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) según sea necesario.
   * Las etiquetas facilitan la búsqueda de tus Campaigns y la elaboración de informes. Por ejemplo, al utilizar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reports/report_builder), puedes filtrar por etiquetas concretas.

{: start="5"}
5. Añade y nombra tantas variantes como necesites para tu Campaign. Puedes elegir diferentes plataformas, tipos de mensaje y diseños para cada una de las variantes añadidas. Para más información sobre este tema, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).
- **Pruebas de variantes SMS y RCS**: Braze te permite incluir variantes tanto de SMS como de RCS dentro de una sola Campaign, lo que te permite comparar el rendimiento de cada una. Puedes añadir variantes de SMS y RCS durante el primer paso de la composición del mensaje.

{: start="6"}
6. Selecciona un [grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups) habilitado para RCS. Al seleccionar un grupo de suscripción, Braze añadirá automáticamente un filtro de segmentación, lo que garantiza que solo los usuarios suscritos recibirán la Campaign. Solo se utilizarán los códigos largos y códigos abreviados que pertenezcan a ese grupo de suscripción para enviar SMS a los usuarios objetivo.
- **Alternativa de SMS**: Braze recomienda encarecidamente que cada grupo de suscripción que contenga un remitente RCS incluya también al menos un código SMS como alternativa. Esto es importante para la capacidad de entrega en caso de que los mensajes RCS no se entreguen. Algunas razones pueden incluir la incompatibilidad del dispositivo del usuario y la cobertura incompleta del operador en un país o región determinados. Al habilitar la alternativa de SMS, tu mensaje seguirá llegando a tu usuario y nunca perderás esa oportunidad de conectar con ellos.

{: start="7"}
7. Elige entre SMS y RCS. Antes de redactar mensajes RCS, elige el canal con el que envías. Generalmente recomendamos usar RCS siempre que sea posible, ya que ofrece beneficios significativos de participación del usuario respecto a SMS; sin embargo, siempre proporcionamos la opción de enviar con SMS para que tengas la máxima flexibilidad y control.

![Opciones para seleccionar entre un tipo de mensaje RCS o SMS/MMS.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% alert tip %}
Si todos los mensajes de tu Campaign van a ser similares o tienen el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. Después puedes elegir **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Crea tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) utilizando el creador de Canvas.
2. Después de configurar tu Canvas, añade un paso de mensaje **SMS/MMS/RCS** en el generador de Canvas.
3. Asigna a tu paso un nombre claro y significativo.
4. Selecciona un [grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups) habilitado para RCS. Al seleccionar un grupo de suscripción, Braze añadirá automáticamente un filtro de segmentación, lo que garantiza que solo los usuarios suscritos recibirán la Campaign. Solo se utilizarán los códigos largos y códigos abreviados que pertenezcan a ese grupo de suscripción para dirigirse a los usuarios.
- **Alternativa de SMS**: Braze recomienda encarecidamente que cada grupo de suscripción que contenga un remitente RCS incluya también al menos un código SMS como alternativa. Esto es importante para la capacidad de entrega en caso de que los mensajes RCS no se entreguen. Algunas razones pueden incluir la incompatibilidad del dispositivo del usuario y la cobertura incompleta del operador en un país o región determinados. Al habilitar la alternativa de SMS, tu mensaje seguirá llegando a tu usuario y nunca perderás esa oportunidad de conectar con ellos.

{: start="5"}
5. Elige entre SMS y RCS. Antes de redactar mensajes RCS, elige el canal con el que envías. Generalmente recomendamos usar RCS siempre que sea posible, ya que ofrece beneficios significativos de participación del usuario respecto a SMS; sin embargo, siempre proporcionamos la opción de enviar con SMS para que tengas la máxima flexibilidad y control.

![Opciones para seleccionar entre un tipo de mensaje RCS o SMS/MMS.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Paso 2: Selecciona tu tipo de mensaje RCS {#step-2-select-your-rcs-message-type}

Durante la creación de una Campaign o un Canvas, elige entre tres tipos de mensajes RCS (Texto, Multimedia, Tarjeta enriquecida) para configurar mensajes que se adapten mejor a tus objetivos.

![Opciones para seleccionar entre un tipo de mensaje de Texto, Multimedia o Tarjeta.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% tabs local %}
{% tab Texto %}
Como su nombre indica, los mensajes de texto RCS se centran en el texto como medio. Si escribes hasta 160 caracteres, el mensaje RCS se factura como un mensaje de solo texto (o "básico"). Si superas los 160 caracteres o usas un elemento enriquecido, el mensaje se factura como un mensaje RCS enriquecido (o "individual") (y el límite de caracteres aumenta a 3072 caracteres).

#### Características {#features}

- Los tipos de mensajes de texto incluyen todas las características de SMS. Solo el seguimiento avanzado es posible para el seguimiento de clics en URL, lo que te ofrece granularidad de informes a nivel de usuario.
- Además, ahora tienes la opción de incluir botones de **Respuestas sugeridas** y **Acciones sugeridas** atractivos que impulsan acciones de alta participación del usuario, como visitar una página de destino o realizar un pedido.
    - Las **Respuestas sugeridas** son botones que contienen respuestas sugeridas para que los usuarios hagan clic y se autocompleten en su campo de texto, eliminando la fricción de tener que pensar en una respuesta al proporcionar un conjunto limitado de opciones para ellos.
    - Las **Acciones sugeridas** son botones que inician una acción en el dispositivo del usuario. Normalmente consisten en una o dos palabras descriptivas y un icono visual para ayudar al usuario a entender qué hace el botón. Actualmente, Braze es compatible con las Acciones sugeridas OpenURL. Esta función es similar a una URL, donde los usuarios que seleccionan el botón son redirigidos a una página web u otra ubicación identificada por URL.

![Un GIF de tres acciones sugeridas para un mensaje RCS que promociona estilos de moda en tendencia: "Realeza de cuento", "Academia atrevida" y "Muéstrame tus otros estilos".]({% image_buster /assets/unlisted_docs/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

#### Consideraciones {#considerations}

- Para los límites de caracteres en texto, puedes escribir hasta 160 caracteres para un mensaje RCS de solo texto (básico) o hasta 3072 para un mensaje RCS enriquecido (individual).
- Para los límites de botones, puedes añadir hasta cinco botones por mensaje. Estos botones pueden ser acciones sugeridas o respuestas sugeridas.
- Los bloques de texto largos y demasiados botones pueden frustrar a los usuarios, por lo que siempre que sea posible, recomendamos apostar por la simplicidad.
- En algunos casos, puede ser más rentable enviar mensajes de solo texto más largos a través de RCS que con SMS. Esto se debe a que los mensajes SMS más largos se dividen en varios segmentos, cada uno de los cuales es facturable, mientras que los mensajes RCS se facturan por mensaje. Contacta con tu director de cuentas de Braze para más detalles y orientación.
{% endtab %}

{% tab Multimedia %}
Los mensajes multimedia RCS te permiten usar formatos multimedia atractivos que no son posibles con SMS. Estos incluyen archivos de imagen, video y documentos. Estas opciones multimedia existen para ayudarte a involucrar a tu audiencia de forma aún más profunda y habilitar casos de uso completamente nuevos. Por el momento, solo se admite la carga de imágenes a través de la [biblioteca multimedia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications).

#### Características

- Los tipos de mensajes multimedia son compatibles con todo lo disponible en los tipos de mensajes de texto, lo que incluye texto, respuestas sugeridas y acciones sugeridas.
- Son compatibles con archivos de imagen, incluidos los formatos JPEG y PNG. Los archivos de imagen están disponibles a través de la carga desde la biblioteca multimedia.
- Son compatibles con archivos de video, incluidos los formatos MP4, MPEG y MV4. Los archivos de video se pueden añadir por URL directamente en el creador de mensajes.
- Son compatibles con archivos de documentos en formato PDF. Los archivos de documentos se pueden añadir a través de la URL directamente en el creador de mensajes.

![Creador de RCS con una opción para cargar un archivo multimedia.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_media_type.png %})

#### Especificaciones de archivos {#file-specifications}

| Tipo de archivo | Especificaciones |
| --- | --- |
| Todos | - El tamaño del archivo está limitado a 100 MB <br><br>- La URL del archivo puede tener hasta 2048 caracteres |
| Archivos de imagen | Los formatos de archivo compatibles incluyen JPG, JPEG y GIF |
| Archivos de video | Los formatos de archivo compatibles incluyen H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Archivos de documentos | Formatos de archivo compatibles: PDF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Consideraciones

La experiencia de usuario al recibir mensajes RCS puede variar ligeramente en función de varios factores, incluida la cobertura del operador en el país de destino, el hardware del dispositivo móvil y el sistema operativo del dispositivo móvil.

En general, RCS se integra de forma más natural con dispositivos Android (este método fue implementado en gran medida por Google, y la mensajería RCS entre pares está ampliamente adoptada en la comunidad Android). Diferentes dispositivos pueden ofrecer la experiencia a diferentes velocidades y calidades.
{% endtab %}

{% tab Tarjeta enriquecida %}

{% alert important %}
Las tarjetas enriquecidas están en acceso anticipado. Contacta con tu CSM de Braze si te interesa participar en este acceso anticipado.
{% endalert %}

Una tarjeta enriquecida combina multimedia, texto y botones en un solo mensaje, creando una experiencia más intuitiva y atractiva para tus clientes. Puedes crear dos subtipos de tarjetas enriquecidas: Texto y Multimedia.

{% subtabs %}
{% subtab Texto %}
Una tarjeta enriquecida de texto es un mensaje conciso centrado en el texto. Debe incluir los siguientes elementos:

- **Título:** Hasta 200 caracteres. Se puede personalizar con Liquid.
- **Descripción:** Hasta 2000 caracteres. Se puede personalizar con Liquid.
- **Botones:** Se requiere al menos un botón. Puedes añadir hasta cuatro botones con acciones de **Respuesta sugerida** o **Abrir URL web**.

{% endsubtab %}
{% subtab Multimedia %}

Una tarjeta enriquecida multimedia es un mensaje visual que contiene una imagen o un video. Debe incluir los siguientes elementos:

- **Multimedia:** Una imagen, GIF o video.
    - Las miniaturas de video personalizadas no son compatibles en el acceso anticipado. El acceso anticipado solo admite un diseño vertical con una altura multimedia alta tanto para archivos de imagen como de video.
- **Botones:** Se requiere al menos un botón. Puedes añadir hasta cuatro botones con acciones de **Respuesta sugerida** o **Abrir URL web**.

{% alert note %}
En iOS, los GIF en las tarjetas enriquecidas se muestran como imágenes estáticas. En Android, se animan como se espera. Para enviar contenido animado a iOS, usa un mensaje **Multimedia** de RCS o incluye un video en la tarjeta enriquecida. Un GIF puede seguir animándose en la vista previa de Braze, así que envía una prueba a un dispositivo iOS.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}

### Características
- **Botones de tarjeta** y **Sugerencias:** Puedes añadir hasta cuatro botones y cinco sugerencias (de hasta 25 caracteres cada una) en la parte inferior de la tarjeta enriquecida (botones) o en la parte inferior de la pantalla del mensaje (sugerencias). Un usuario puede seleccionar estas opciones de clic para enviar una respuesta específica o realizar una acción específica.
- **Personalización:** Puedes usar Liquid para personalizar todos los elementos de la tarjeta enriquecida, incluidos el título, la descripción, el contenido multimedia y los botones.
- **Facturación:** Las tarjetas enriquecidas se facturan como un solo mensaje RCS enriquecido (o "individual").
- **Orientación sobre URL:** Las URL introducidas como texto plano en el título o la descripción no serán clicables. Debes usar un **botón OpenURL** para dirigir a los usuarios a un sitio web.

![Panel con opciones para seleccionar una tarjeta enriquecida de Multimedia o Texto.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_media_text.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Paso 3: Redacta tu mensaje RCS {#step-3-compose-your-rcs-message}

Escribe tu mensaje usando idiomas y personalización ([Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) y emojis) según sea necesario. Asegúrate de respetar nuestros límites de texto de mensajes para reducir tus posibilidades de cargos por excedente.

{% alert important %}
Antes de continuar, lee nuestras [directrices sobre los límites de los mensajes RCS](#step-2-select-your-rcs-message-type). Los mensajes RCS se [cobran por mensaje]({{site.baseurl}}/sms_rcs_billing_calculators), por lo que es buena idea comprender los matices de lo que se puede incluir en cada tipo de mensaje RCS.
{% endalert %}

### Paso 4: Previsualiza y prueba tu mensaje {#step-4-preview-and-test-your-message}

Braze siempre recomienda previsualizar y probar tu mensaje antes de enviarlo. Ve a la pestaña **Prueba** para enviar un RCS de prueba a grupos de prueba de contenido o a usuarios individuales, o previsualiza el mensaje como un usuario directamente en Braze.

### Paso 5: Crea el resto de tu Campaign o Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

A continuación, crea el resto de tu Campaign o Canvas. Consulta las siguientes secciones para más detalles sobre cómo utilizar mejor nuestras herramientas para crear mensajes RCS.

#### Paso 5.1: Elige la programación o el desencadenante de entrega {#step-51-choose-delivery-schedule-or-trigger}

Los mensajes RCS se pueden entregar en función de una hora programada, una acción o un desencadenante de API. Para más información, consulta [Programar tu Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Para la entrega basada en acciones, también puedes establecer la duración de la Campaign y las horas tranquilas.

Especifica tus controles de entrega, como permitir que los usuarios vuelvan a ser elegibles para recibir la Campaign o habilitar reglas de limitación de frecuencia.

#### Paso 5.2: Elige a los usuarios objetivo {#step-52-choose-users-to-target}

Segmenta a los usuarios eligiendo Segments o filtros para acotar tu audiencia. Ya deberías haber seleccionado el grupo de suscripción, que filtra a los usuarios por el nivel o categoría de comunicación que desean tener contigo.

{% multi_lang_include audience/target_audiences.md %}

A continuación, seleccionarás la audiencia más amplia de tus Segments y acotarás aún más ese Segment con [filtros]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) opcionales. Obtendrás automáticamente una vista previa de la población aproximada de ese Segment en ese momento. Ten en cuenta que la pertenencia exacta al Segment siempre se calcula justo antes de enviar el mensaje.

{% alert tip %}
¿Te interesa utilizar la reorientación RCS para dirigirte a usuarios en función de sus interacciones de SMS y RCS? Consulta [Reorientación]({{site.baseurl}}/sms_mms_rcs_user_retargeting).
{% endalert %}

#### Paso 5.3: Elige eventos de conversión {#step-53-choose-conversion-events}

Braze te permite rastrear con qué frecuencia los usuarios realizan acciones específicas, o eventos de conversión, después de recibir una Campaign. Puedes permitir una ventana de hasta 30 días durante la cual se contará una conversión si el usuario realiza la acción especificada.

Los eventos de conversión te ayudan a medir el éxito de tu Campaign. Por ejemplo:
- Si estás utilizando geolocalización para desencadenar un mensaje RCS con el objetivo final de que el usuario realice una compra, establece el evento de conversión en **Compra**.
- Si intentas dirigir al usuario a tu aplicación, establece el evento de conversión en **Inicia sesión**.

También puedes establecer eventos de conversión personalizados en función de tu caso de uso específico. Sé creativo con la forma en que realmente quieres medir el éxito de tu Campaign.

### Paso 6: Revisa y despliega {#step-6-review-and-deploy}

Cuando hayas terminado de crear tu Campaign o Canvas, revisa sus detalles, pruébala y envíala.

A continuación, consulta [Informes para SMS, MMS y RCS]({{site.baseurl}}/sms_mms_rcs_reporting) para saber cómo puedes acceder a los resultados de tus Campaigns de RCS.

## Análisis e informes {#analytics-and-reporting}

Los análisis de tu Campaign o Canvas incluyen:

- Estadísticas de _Total de clics_ que incluyen todas las interacciones con la Rich Card, como clics en botones y respuestas o acciones sugeridas.
- Una tabla desglosada que proporciona una vista más detallada de estas interacciones.

{% alert note %}
El acceso anticipado no incluye el seguimiento de clics a nivel de usuario. _Total de clics_ se incrementará cada vez que se haga clic en un botón. Por ejemplo, si un usuario hace clic en el mismo botón tres veces, el conteo de clics aumentará en tres.
{% endalert %}

## Consejos {#tips}

### Uso de Liquid para la personalización de mensajes {#using-liquid-for-message-personalization}

Si planeas usar Liquid, asegúrate de incluir un valor predeterminado para la personalización que hayas elegido, de modo que, si el perfil de usuario del destinatario está incompleto, no reciba un marcador de posición en blanco como `Hi, !` en lugar de su nombre o una frase coherente.

### Generación de textos con IA {#generating-ai-copy}

¿Necesitas ayuda para crear textos atractivos? Prueba a usar el [asistente de redacción con IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Introduce el nombre o la descripción de un producto, y la IA generará textos de marketing similares a los escritos por personas para usar en tu mensajería.

![Creador de mensajes con un icono para abrir el asistente de redacción con IA.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_ai_copywriter.png %}){: style="max-width:70%;"}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Puedo enviar mensajes de voz pregrabados con RCS? {#can-i-send-pre-recorded-voicemails-with-rcs}

Sí, puedes usar mensajes multimedia para admitir archivos de audio.