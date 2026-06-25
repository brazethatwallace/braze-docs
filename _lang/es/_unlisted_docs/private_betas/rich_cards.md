---
nav_title: "Crear un mensaje RCS"
article_title: "Crear un mensaje RCS"
permalink: /create_rcs_message/
description: "Este artículo explica cómo crear un mensaje RCS."
hidden: true
---

# Crear un mensaje RCS {#creating-an-rcs-message}

> Las campañas RCS son ideales para comunicarte directamente con tus clientes y conversar con ellos de forma programática. Puedes usar Liquid y otro contenido dinámico para crear una experiencia personalizada con tus usuarios y fomentar una experiencia de usuario discreta y enriquecedora con tu marca.

## Crear un mensaje RCS

### Paso 1: Elige dónde crear tu mensaje {#step-1-choose-where-to-build-your-message}

¿No tienes claro si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para envíos de mensajería sencillos y únicos, mientras que los Canvas son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaign %}
1. Ve a **Mensajería** > **Campaigns** y selecciona **Crear campaña**.
2. Selecciona **SMS/MMS/RCS** o, para campañas dirigidas a varios canales, selecciona **Multicanal**.
3. Ponle a tu campaña un nombre claro y significativo.
4. Añade [equipos](https://braze.com/docs/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas](https://braze.com/docs/user_guide/administrative/app_settings/tags/) según sea necesario.
   * Las etiquetas facilitan encontrar tus campañas y generar informes a partir de ellas. Por ejemplo, al usar el [Generador de informes](https://braze.com/docs/user_guide/analytics/reporting/report_builder/), puedes filtrar por etiquetas específicas.

{: start="5"}
5. Añade y nombra tantas variantes como necesites para tu campaña. Puedes elegir diferentes plataformas, tipos de mensaje y diseños para cada una de las variantes añadidas. Para más información sobre este tema, consulta [Pruebas multivariantes y A/B](https://braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing/).
- **Pruebas de variantes SMS y RCS**: Braze te permite incluir variantes tanto de SMS como de RCS dentro de una sola campaña, lo que te permite comparar el rendimiento de cada una. Puedes añadir variantes de SMS y RCS durante el primer paso de la composición del mensaje.

{: start="6"}
6. Selecciona un [grupo de suscripción](https://braze.com/docs/sms_rcs_subscription_groups/) habilitado para RCS. Al seleccionar un grupo de suscripción, Braze añadirá automáticamente un filtro de segmentación, asegurando que solo los usuarios suscritos reciban la campaña. Solo se usarán los códigos largos y códigos abreviados que pertenezcan a ese grupo de suscripción para enviar SMS a los usuarios objetivo.
- **Alternativa SMS**: Braze recomienda encarecidamente que cada grupo de suscripción que contenga un remitente RCS incluya también al menos un código SMS como alternativa. Esto es importante para la capacidad de entrega en casos en que los mensajes RCS no se entreguen. Algunas razones pueden incluir incompatibilidad del dispositivo del usuario y cobertura incompleta del operador en un país o región determinados. Al habilitar la alternativa SMS, tu mensaje se entregará igualmente a tu usuario y nunca perderás esa oportunidad de conectar con ellos.

{: start="7"}
7. Elige entre SMS y RCS. Antes de redactar mensajes RCS, elige el canal con el que envías. Generalmente recomendamos usar RCS siempre que sea posible, ya que ofrece beneficios significativos de interacción del usuario sobre SMS; sin embargo, siempre proporcionamos la opción de enviar con SMS para que tengas la máxima flexibilidad y control.

![Opciones para seleccionar un tipo de mensaje RCS o SMS/MMS.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% alert tip %}
Si todos los mensajes de tu campaña van a ser similares o tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. Luego puedes elegir **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Crea tu Canvas](https://braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando el compositor de Canvas.
2. Después de configurar tu Canvas, añade un paso de mensaje **SMS/MMS/RCS** en el constructor de Canvas.
3. Ponle a tu paso un nombre claro y significativo.
4. Selecciona un [grupo de suscripción](https://braze.com/docs/sms_rcs_subscription_groups/) habilitado para RCS. Al seleccionar un grupo de suscripción, Braze añadirá automáticamente un filtro de segmentación, asegurando que solo los usuarios suscritos reciban la campaña. Solo se usarán los códigos largos y códigos abreviados que pertenezcan a ese grupo de suscripción para dirigirse a los usuarios.
- **Alternativa SMS**: Braze recomienda encarecidamente que cada grupo de suscripción que contenga un remitente RCS incluya también al menos un código SMS como alternativa. Esto es importante para la capacidad de entrega en casos en que los mensajes RCS no se entreguen. Algunas razones pueden incluir incompatibilidad del dispositivo del usuario y cobertura incompleta del operador en un país o región determinados. Al habilitar la alternativa SMS, tu mensaje se entregará igualmente a tu usuario y nunca perderás esa oportunidad de conectar con ellos.

{: start="5"}
5. Elige entre SMS y RCS. Antes de redactar mensajes RCS, elige el canal con el que envías. Generalmente recomendamos usar RCS siempre que sea posible, ya que ofrece beneficios significativos de interacción del usuario sobre SMS; sin embargo, siempre proporcionamos la opción de enviar con SMS para que tengas la máxima flexibilidad y control.

![Opciones para seleccionar un tipo de mensaje RCS o SMS/MMS.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Paso 2: Selecciona tu tipo de mensaje RCS {#step-2-select-your-rcs-message-type}

Durante la creación de campañas y Canvas, elige entre tres tipos de mensajes RCS (texto, multimedia, tarjeta enriquecida) para configurar mensajes que se adapten mejor a tus objetivos.

![Opciones para seleccionar un tipo de mensaje de texto, multimedia o tarjeta.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% tabs local %}
{% tab Texto %}
Como su nombre indica, los mensajes de texto RCS se centran en el texto como medio. Si escribes hasta 160 caracteres, el mensaje RCS se factura como un mensaje de solo texto (o "básico"). Si superas los 160 caracteres o usas un elemento enriquecido, el mensaje se factura como un mensaje RCS enriquecido (o "único") (y el límite de caracteres aumenta a 3072 caracteres).

#### Características {#features}

- Los tipos de mensajes de texto incluyen todas las características de SMS. Solo el seguimiento avanzado es posible para el seguimiento de clics en URL, lo que te ofrece granularidad de informes a nivel de usuario.
- Además, ahora tienes la opción de incluir botones de **Respuestas sugeridas** y **Acciones sugeridas** atractivos que impulsan acciones de usuario de alta interacción, como visitar una página de inicio o realizar un pedido.
    - Las **Respuestas sugeridas** son botones que contienen respuestas sugeridas para que los usuarios hagan clic y las completen previamente en su campo de texto, eliminando la fricción de tener que pensar en una respuesta al proporcionar un conjunto limitado de opciones.
    - Las **Acciones sugeridas** son botones que inician una acción en el dispositivo del usuario. Normalmente consisten en una o dos palabras descriptivas y un icono visual para ayudar al usuario a entender qué hace el botón. Braze actualmente admite Acciones sugeridas de tipo OpenURL. Esto funciona de manera similar a una URL, donde los usuarios que seleccionan el botón son redirigidos a una página web u otra ubicación identificada por URL.

![Un GIF de tres Acciones sugeridas para un mensaje RCS que promociona estilos de moda en tendencia: "Realeza de cuento de hadas", "Academia atrevida" y "Muéstrame tus otros estilos".]({% image_buster /assets/unlisted_docs/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

#### Consideraciones {#considerations}

- Para los límites de caracteres en texto, puedes escribir hasta 160 caracteres para un mensaje RCS de solo texto (básico) o hasta 3072 para un mensaje RCS enriquecido (único).
- Para los límites de botones, puedes añadir hasta cinco botones por mensaje. Estos botones pueden ser acciones sugeridas o respuestas sugeridas.
- Los bloques de texto largos y demasiados botones pueden frustrar a los usuarios, así que siempre que sea posible, recomendamos apostar por la simplicidad.
- En algunos casos, puede ser más rentable enviar mensajes de solo texto más largos a través de RCS que con SMS. Esto se debe a que los mensajes SMS más largos se dividen en múltiples segmentos, cada uno de los cuales es facturable, mientras que los mensajes RCS se facturan por mensaje. Ponte en contacto con tu director de cuentas de Braze para más detalles y orientación.
{% endtab %}

{% tab Multimedia %}
Los mensajes multimedia RCS te permiten usar formatos multimedia atractivos que no son posibles con SMS. Estos incluyen archivos de imagen, video y documentos. Estas opciones multimedia existen para ayudarte a interactuar con tu audiencia de forma aún más profunda y habilitar casos de uso completamente nuevos. Por el momento, solo se admite la carga de imágenes a través de la [Biblioteca de medios](https://braze.com/docs/user_guide/engagement_tools/templates_and_media/media_library/).

#### Características

- Los tipos de mensajes multimedia admiten todo lo disponible en los tipos de mensajes de texto, lo que incluye texto, respuestas sugeridas y acciones sugeridas.
- Admite archivos de imagen, incluidos los formatos JPEG y PNG. Los archivos de imagen están disponibles mediante carga desde la Biblioteca de medios.
- Admite archivos de video, incluidos los formatos MP4, MPEG y MV4. Los archivos de video se pueden añadir por URL directamente en el creador de mensajes.
- Admite archivos de documentos en formato PDF. Los archivos de documentos se pueden añadir a través de la URL directamente en el creador de mensajes.

![Compositor RCS con una opción para cargar un archivo multimedia.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_media_type.png %})

#### Especificaciones de archivos {#file-specifications}

| Tipo de archivo | Especificaciones |
| --- | --- |
| Todos | - El tamaño del archivo está limitado a 100 MB <br><br>- La URL del archivo puede tener hasta 2048 caracteres |
| Archivos de imagen | Los formatos de archivo admitidos incluyen JPG, JPEG y GIF |
| Archivos de video | Los formatos de archivo admitidos incluyen H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Archivos de documentos | Formatos de archivo admitidos: PDF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Consideraciones

La experiencia del usuario al recibir mensajes RCS puede variar ligeramente en función de varios factores, incluida la cobertura del operador en el país de destino, el hardware del dispositivo móvil y el sistema operativo del dispositivo móvil.

En general, RCS se integra de forma más natural con dispositivos Android (este método fue implementado en gran parte por Google, y la mensajería RCS entre pares está ampliamente adoptada en la comunidad Android). Diferentes dispositivos pueden renderizar la experiencia a diferentes velocidades y calidades.
{% endtab %}

{% tab Tarjeta enriquecida %}

{% alert important %}
Las tarjetas enriquecidas están en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente de Braze si te interesa participar en este acceso anticipado.
{% endalert %}

Una tarjeta enriquecida combina multimedia, texto y botones en un solo mensaje, creando una experiencia más intuitiva y atractiva para tus clientes. Puedes crear dos subtipos de tarjetas enriquecidas: texto y multimedia.

{% subtabs %}
{% subtab Texto %}
Una tarjeta enriquecida de texto es un mensaje conciso centrado en el texto. Debe incluir los siguientes elementos:

- **Título:** Hasta 200 caracteres. Se puede personalizar con Liquid.
- **Descripción:** Hasta 2000 caracteres. Se puede personalizar con Liquid.
- **Botones:** Se requiere al menos un botón. Puedes añadir hasta cuatro botones con acciones de **Respuesta sugerida** o **Abrir URL web**.

{% endsubtab %}
{% subtab Multimedia %}

Una tarjeta enriquecida multimedia es un mensaje visual que contiene una imagen o video. Debe incluir los siguientes elementos:

- **Multimedia:** Una imagen, GIF o video.
    - Las miniaturas de video personalizadas no son compatibles en el acceso anticipado. El acceso anticipado solo admite un diseño vertical con una altura de multimedia alta tanto para archivos de imagen como de video.
- **Botones:** Se requiere al menos un botón. Puedes añadir hasta cuatro botones con acciones de **Respuesta sugerida** o **Abrir URL web**.

{% endsubtab %}
{% endsubtabs %}

### Características
- **Botones de tarjeta** y **Sugerencias:** Puedes añadir hasta cuatro botones y cinco sugerencias (hasta 25 caracteres cada una) en la parte inferior de la tarjeta enriquecida (botones) o en la parte inferior de la pantalla del mensaje (sugerencias). Un usuario puede seleccionar estas opciones de clic para enviar una respuesta específica o realizar una acción específica.
- **Personalización:** Puedes usar Liquid para personalizar todos los elementos de la tarjeta enriquecida, incluidos el título, la descripción, el multimedia y los botones.
- **Facturación:** Las tarjetas enriquecidas se facturan como un solo mensaje RCS enriquecido (o "único").
- **Orientación sobre URL:** Las URL introducidas como texto plano en el título o la descripción no serán clicables. Debes usar un **botón OpenURL** para dirigir a los usuarios a un sitio web.

![Panel con opciones para seleccionar una tarjeta enriquecida de multimedia o texto.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_media_text.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Paso 3: Redacta tu mensaje RCS {#step-3-compose-your-rcs-message}

Escribe tu mensaje usando idiomas y personalización ([Liquid](https://braze.com/docs/user_guide/personalization_and_dynamic_content/liquid/), [Contenido conectado](https://braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/) y emojis) según sea necesario. Asegúrate de respetar nuestros límites de texto del mensaje para reducir las posibilidades de cargos por excedente.

{% alert important %}
Antes de continuar, lee nuestras [directrices sobre los límites de mensajes RCS](#step-2-select-your-rcs-message-type). Los mensajes RCS se [cobran por mensaje](https://braze.com/docs/sms_rcs_billing_calculators/), por lo que es buena idea entender los matices de lo que se puede incluir en cada tipo de mensaje RCS.
{% endalert %}

### Paso 4: Previsualiza y prueba tu mensaje {#step-4-preview-and-test-your-message}

Braze siempre recomienda previsualizar y probar tu mensaje antes de enviarlo. Ve a la pestaña **Prueba** para enviar un RCS de prueba a grupos de prueba de contenido o a usuarios individuales, o previsualiza el mensaje como un usuario directamente en Braze.

### Paso 5: Construye el resto de tu campaña o Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

A continuación, construye el resto de tu campaña o Canvas. Consulta las siguientes secciones para más detalles sobre cómo usar mejor nuestras herramientas para crear mensajes RCS.

#### Paso 5.1: Elige la planificación de entrega o el desencadenante {#step-51-choose-delivery-schedule-or-trigger}

Los mensajes RCS se pueden entregar en función de una hora planificada, una acción o un desencadenante de API. Para más información, consulta [Planificar tu campaña](https://braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para la entrega basada en acciones, también puedes establecer la duración de la campaña y las horas tranquilas.

Especifica tus controles de entrega, como permitir que los usuarios vuelvan a ser elegibles para recibir la campaña o habilitar reglas de limitación de frecuencia.

#### Paso 5.2: Elige los usuarios objetivo {#step-52-choose-users-to-target}

Dirige a los usuarios eligiendo segmentos o filtros para acotar tu audiencia. Ya deberías haber seleccionado el grupo de suscripción, que filtra a los usuarios por el nivel o categoría de comunicación que desean tener contigo.

{% multi_lang_include target_audiences.md %}

A continuación, seleccionarás la audiencia más amplia de tus segmentos y la acotarás aún más con [filtros](https://braze.com/docs/user_guide/engagement_tools/segments/segmentation_filters/) opcionales. Obtendrás automáticamente una vista previa de cómo se ve aproximadamente la población de ese segmento en este momento. Ten en cuenta que la pertenencia exacta al segmento siempre se calcula justo antes de que se envíe el mensaje.

{% alert tip %}
¿Te interesa usar la reorientación RCS para dirigirte a usuarios en función de sus interacciones con SMS y RCS? Consulta [Reorientación](https://braze.com/docs/sms_mms_rcs_user_retargeting/).
{% endalert %}

#### Paso 5.3: Elige eventos de conversión {#step-53-choose-conversion-events}

Braze te permite hacer seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, o eventos de conversión, después de recibir una campaña. Puedes permitir una ventana de hasta 30 días durante la cual se contará una conversión si el usuario realiza la acción especificada.

Los eventos de conversión te ayudan a medir el éxito de tu campaña. Por ejemplo:
- Si estás usando geolocalización para desencadenar un mensaje RCS cuyo objetivo final es que el usuario realice una compra, establece el evento de conversión en **Compra**.
- Si intentas llevar al usuario a tu aplicación, establece el evento de conversión en **Inicia sesión**.

También puedes establecer eventos de conversión personalizados según tu caso de uso específico. Sé creativo con la forma en que realmente quieres medir el éxito de tu campaña.

### Paso 6: Revisa y despliega {#step-6-review-and-deploy}

Después de terminar de construir tu campaña o Canvas, revisa sus detalles, pruébala y luego envíala.

A continuación, consulta [Informes para SMS, MMS y RCS](https://braze.com/docs/sms_mms_rcs_reporting/) para aprender cómo puedes acceder a los resultados de tus campañas RCS.

## Análisis e informes {#analytics-and-reporting}

Los análisis de tu campaña o Canvas incluyen:

- Estadísticas de _Clics totales_ que incluyen todas las interacciones con la tarjeta enriquecida, como clics en botones y respuestas sugeridas o acciones.
- Una tabla desglosada que proporciona una vista más detallada de estas interacciones.

{% alert note %}
El acceso anticipado no incluye seguimiento de clics a nivel de usuario. Los _Clics totales_ se incrementarán cada vez que se haga clic en un botón. Por ejemplo, si un usuario hace clic en el mismo botón tres veces, el conteo de clics aumentará en tres.
{% endalert %}

## Consejos {#tips}

### Usar Liquid para la personalización de mensajes {#using-liquid-for-message-personalization}

Si planeas usar Liquid, asegúrate de incluir un valor predeterminado para la personalización elegida para que, si el perfil de usuario del destinatario está incompleto, no reciba un marcador de posición en blanco `Hi, !` en lugar de su nombre o una frase coherente.

### Generar texto con IA {#generating-ai-copy}

¿Necesitas ayuda para crear textos atractivos? Prueba a usar el [asistente de redacción con inteligencia artificial](https://braze.com/docs/user_guide/brazeai/operator/capabilities/#generate-copy). Introduce un nombre o descripción de producto, y la IA generará textos de marketing similares a los escritos por humanos para usar en tu mensajería.

![Compositor de mensajes con un icono para abrir el asistente de redacción con inteligencia artificial.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_ai_copywriter.png %}){: style="max-width:70%;"}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Puedo enviar mensajes de voz pregrabados con RCS? {#can-i-send-pre-recorded-voicemails-with-rcs}

Sí, puedes usar mensajes multimedia para admitir archivos de audio.