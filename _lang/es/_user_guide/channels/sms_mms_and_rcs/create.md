---
nav_title: Crear un mensaje
article_title: Crear un mensaje SMS, MMS o RCS
page_order: 1
description: "Este artículo explica cómo crear y enviar un mensaje SMS, MMS o RCS en Braze."
page_type: reference
alias: /create_sms_mms_rcs_message/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
search_rank: 1
---

# Crear un mensaje SMS, MMS o RCS {#create-an-sms-mms-or-rcs-message}

> Las campañas de SMS, MMS y RCS son ideales para llegar directamente a tus clientes y conversar con ellos de forma programática. Puedes usar Liquid y otro contenido dinámico para crear una experiencia personal con tus usuarios y fomentar un entorno que mejore una experiencia de usuario discreta con tu marca.

## Paso 1: Elige dónde crear tu mensaje {#step-1-choose-where-to-build-your-message}

¿No tienes claro si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para envíos de mensajería únicos y dirigidos, mientras que los Canvas son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaign %}

1. Ve a **Mensajería** > **Campaigns** y selecciona **Crear campaña**.
2. Selecciona **SMS/MMS/RCS** o, para campañas dirigidas a múltiples canales, selecciona **Multicanal**.
3. Ponle a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) según sea necesario.
   * Las etiquetas facilitan encontrar tus campañas y generar informes a partir de ellas. Por ejemplo, al usar el [Generador de informes]({{site.baseurl}}/user_guide/analytics/reports/report_builder/), puedes filtrar por etiquetas concretas.
5. Añade y nombra tantas variantes como necesites para tu campaña. Puedes elegir diferentes plataformas, tipos de mensaje y diseños para cada una de las variantes añadidas. Para más información sobre este tema, consulta [Pruebas multivariante y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).
   * Braze te permite incluir variantes tanto de SMS como de RCS dentro de una misma campaña, para que puedas comparar el rendimiento de cada una.

{% alert tip %}
Si todos los mensajes de tu campaña van a ser similares o tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. Luego puedes elegir **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crea tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) usando el compositor de Canvas.
2. Después de configurar tu Canvas, añade un paso de mensaje **SMS/MMS/RCS** en el constructor de Canvas.
3. Ponle a tu paso un nombre claro y significativo.
4. Elige una [planificación de paso]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#schedule-delay) y especifica un retraso según sea necesario.
5. Filtra tu audiencia para este paso según sea necesario. Puedes refinar aún más los destinatarios de este paso especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se comprobarán después del retraso, en el momento en que se envíen los mensajes.
6. Elige tu [comportamiento de avance]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/).
7. Elige cualquier otro canal de mensajería que desees combinar con tu mensaje.

{% endtab %}
{% endtabs %}

## Paso 2: Selecciona un grupo de suscripción {#step-2-select-a-subscription-group}

Selecciona un [grupo de suscripción]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/) para asegurarte de que envías tu mensaje a los usuarios adecuados. Al seleccionar un grupo de suscripción, Braze añadirá automáticamente un filtro de segmentación, garantizando que solo los usuarios suscritos reciban la campaña.

El grupo de suscripción que selecciones determina qué tipos de mensaje están disponibles en el compositor:

| Tipo de grupo de suscripción | Tipos de mensaje disponibles |
| --- | --- |
| Solo SMS | SMS |
| SMS con números habilitados para MMS | SMS y MMS |
| Habilitado para RCS (con remitente verificado para RCS) | SMS, MMS (si está habilitado) y RCS |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Selecciona un grupo de suscripción" }

{% alert tip %}
Braze recomienda encarecidamente que cada grupo de suscripción que contenga un remitente RCS incluya también al menos un código SMS como alternativa. Esto garantiza que, si un mensaje RCS no se entrega (por ejemplo, debido a incompatibilidad del dispositivo o cobertura incompleta del operador), el mensaje llegue igualmente al usuario a través de SMS.
{% endalert %}

Después de seleccionar tu grupo de suscripción, elige el tipo de mensaje que deseas redactar. Si tu grupo de suscripción admite varios tipos, verás opciones para seleccionar entre ellos.

![Opciones para seleccionar entre un tipo de mensaje RCS o SMS/MMS.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

## Paso 3: Redacta tu mensaje {#step-3-compose-your-message}

La experiencia de redacción cambia según el tipo de mensaje que hayas seleccionado. Selecciona la pestaña correspondiente a tu tipo de mensaje.

{% tabs local %}
{% tab SMS %}

Escribe tu mensaje usando idiomas y personalización (Liquid, contenido conectado y emojis) según sea necesario. Asegúrate de respetar los límites de texto del mensaje para reducir las posibilidades de cargos por excedente.

{% alert important %}
Antes de continuar, lee las directrices sobre [segmentos de mensajes SMS y límites de texto]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/). Los segmentos de mensajes SMS son los lotes de caracteres que los operadores telefónicos utilizan para medir los mensajes de texto. Los mensajes se cobran por segmento de mensaje, por lo que es buena idea entender los matices de cómo se dividen los mensajes.
{% endalert %}

![Compositor de SMS en Braze con el mensaje "Hola first_name, ¡agradecemos tu apoyo! ¿Por qué no pasas por una de nuestras tiendas y muestras este SMS para obtener un descuento exclusivo? Responde STOP para dejar de recibir mensajes nuestros."]({% image_buster /assets/img/sms_campaign_compose.png %})

### Añadir una tarjeta de contacto {#adding-a-contact-card}

Puedes añadir una tarjeta de contacto a tu mensaje SMS para que los clientes puedan agregar la información de tu empresa y de contacto a los contactos de su dispositivo. Puedes asignar propiedades como nombre de la empresa, número de teléfono, dirección, correo electrónico y una foto pequeña. Consulta [Tarjetas de contacto]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card/) para más detalles.

{% endtab %}
{% tab MMS %}

Para enviar un mensaje MMS, tu grupo de suscripción debe tener al menos un número de teléfono habilitado para MMS. Esto se indica con una etiqueta **MMS** junto al grupo de suscripción en el compositor.

Introduce el cuerpo de tu mensaje y luego sube una imagen PNG, JPEG o GIF desde la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/) o especifica una URL de imagen. Solo se admite una imagen por mensaje.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

![La pestaña de redacción para escribir un mensaje MMS.]({% image_buster /assets/img/sms/mms_composer.png %}){: style="max-width:80%;"}

### Especificaciones de imagen {#image-specifications}

| Propiedad | Recomendación |
| --- | --- |
| Tamaño | Hasta 600&nbsp;KB |
| Tipos de archivo | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Especificaciones de imagen" }

### Tarjetas de contacto {#contact-cards}

También puedes incluir una [tarjeta de contacto]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card/) (vCard) en lugar de una imagen.

### Comportamiento del operador {#carrier-behavior}

Los mensajes MMS se facturan a una tarifa diferente que los SMS de solo texto. No todos los operadores pueden aceptar MMS. En estos casos, el MMS se convierte automáticamente en un enlace de imagen que el usuario puede seleccionar.

### MMS entrantes y personalización {#inbound-mms-and-personalization}

Cuando un cliente envía un mensaje entrante que incluye medios, Braze expone los medios en los [eventos entrantes de SMS en Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/#sms-inbound-received-events) y en Liquid como {% raw %}`{{sms.${inbound_media_urls}}}`{% endraw %} (por ejemplo, en mensajes de reorientación o seguimiento). Para más información sobre el uso de propiedades de SMS entrantes en Canvas, consulta [Paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/).

{% endtab %}
{% tab RCS %}

Mira este breve recorrido para ver cómo crear un mensaje de texto o multimedia RCS.

{% multi_lang_include video.html id="3y0iiqqygw" source="wistia" %}

Elige entre un tipo de mensaje de **Texto** o **Multimedia**.

![Opciones para seleccionar entre un tipo de mensaje de texto o multimedia.]({% image_buster /assets/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% subtabs %}
{% subtab Texto %}

Los mensajes de texto RCS se centran en el texto como medio. Si tu mensaje tiene hasta 160 caracteres sin elementos enriquecidos, se factura como un mensaje RCS básico. Si superas los 160 caracteres o usas un elemento enriquecido, se factura como un mensaje RCS enriquecido (único) con un límite de 3072 caracteres.

**Características:**

- Se incluyen todas las características de SMS, con seguimiento avanzado disponible para el seguimiento de clics en URL.
- **Respuestas sugeridas**: botones que contienen respuestas sugeridas que los usuarios pueden seleccionar para rellenar previamente en su campo de texto.
- **Acciones sugeridas**: botones que inician una acción en el dispositivo del usuario. Braze actualmente admite acciones sugeridas de tipo OpenURL, que redirigen a los usuarios a una página web u otra ubicación identificada por URL.

![Tres acciones sugeridas para un mensaje RCS que promociona estilos de moda en tendencia.]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

**Consideraciones:**

- Android e iOS pueden truncar de forma diferente: Android muestra el texto completo del mensaje enriquecido, mientras que iOS trunca después de la tercera línea.
- Puedes añadir hasta cinco botones por mensaje. Estos pueden ser acciones sugeridas o respuestas sugeridas.
- Los bloques de texto largos y muchos botones pueden abrumar a los destinatarios; opta por la simplicidad cuando sea posible.
- En algunos casos, puede ser más rentable enviar mensajes de texto largos a través de RCS que con SMS, porque los mensajes SMS más largos se dividen en múltiples segmentos facturables, mientras que los mensajes RCS se facturan por mensaje.

{% endsubtab %}
{% subtab Multimedia %}

Los mensajes multimedia RCS te permiten usar formatos de medios atractivos que no son posibles con SMS, incluyendo archivos de imagen, video y documentos.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

**Características:**

- Admite todo lo disponible en los tipos de mensaje de texto, incluyendo texto, respuestas sugeridas y acciones sugeridas.
- Archivos de imagen (JPEG, PNG) subidos desde la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/).
- Archivos de video (MP4, MPEG, MV4) añadidos por URL en el compositor de mensajes.
- Archivos de documentos (PDF) añadidos por URL en el compositor de mensajes.

![Compositor RCS con una opción para subir un archivo multimedia.]({% image_buster /assets/img/rcs/rcs_media_type.png %})

**Especificaciones de archivo:**

| Tipo de archivo | Especificaciones |
| --- | --- |
| Todos | Tamaño de archivo limitado a 100 MB. La URL del archivo puede tener hasta 2048 caracteres. |
| Imagen | Formatos admitidos: JPG, JPEG, GIF |
| Video | Formatos admitidos: H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Documento | Formato admitido: PDF |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Especificaciones de archivo" }

**Consideraciones:**

La experiencia del usuario al recibir mensajes RCS puede variar según la cobertura del operador, el hardware del dispositivo móvil y el sistema operativo. RCS se integra de forma más natural con dispositivos Android, y diferentes dispositivos pueden renderizar la experiencia a diferentes velocidades y calidades.

{% endsubtab %}
{% endsubtabs %}

Escribe tu mensaje usando idiomas y personalización ([Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/), [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) y emojis) según sea necesario. Asegúrate de respetar los límites de texto del mensaje para reducir las posibilidades de cargos por excedente.

{% alert important %}
Antes de continuar, lee las [directrices de tipos de mensaje RCS](#step-3-compose-your-message) anteriores. Los mensajes RCS se [cobran por mensaje]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/), por lo que es buena idea entender qué se puede incluir en cada tipo.
{% endalert %}

{% endtab %}
{% endtabs %}

### Consejos {#tips}

#### Uso de Liquid {#using-liquid}

{% raw %}
Si planeas usar Liquid, asegúrate de incluir un valor predeterminado para la personalización elegida, de modo que, en caso de que el perfil de tu usuario esté incompleto, no reciba un marcador de posición en blanco `Hi, !` en lugar de su nombre o una frase coherente.
{% endraw %}

#### Generar texto con IA {#generating-ai-copy}

Prueba a usar el [asistente de redacción con inteligencia artificial]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Introduce un nombre o descripción de producto, y la IA generará texto de marketing similar al humano para usar en tu mensajería.

![Botón Lanzar redactor con IA, ubicado en el campo Mensaje del compositor de SMS.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

#### Crear mensajes de derecha a izquierda {#creating-right-to-left-messages}

La apariencia final de los mensajes de derecha a izquierda depende en gran medida de cómo los rendericen los proveedores de servicios. Para conocer las mejores prácticas sobre cómo crear mensajes de derecha a izquierda que se muestren con la mayor precisión posible, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/).

#### Crear flujos de trabajo de mensajes conversacionales (RCS) {#create-conversational-message-workflows-rcs}

Los flujos de trabajo de mensajes conversacionales te permiten responder dinámicamente a los usuarios, creando una experiencia de mensajería de ida y vuelta. Para crear un flujo de trabajo, crea un Canvas y luego combina respuestas sugeridas con [Rutas de acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths/) para dirigir tu flujo de trabajo en función de la respuesta que seleccione el usuario.

1. En el constructor de Canvas, crea un paso de mensaje RCS con múltiples respuestas sugeridas.

![Compositor de mensajes RCS con respuestas sugeridas.]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. Conecta ese mensaje a una ruta de acción con un grupo de acciones para cada respuesta sugerida.
3. Para cada grupo de acciones:
   - Selecciona el desencadenante **Enviar un mensaje SMS entrante**.
   - Establece el cuerpo del mensaje para que sea igual a la respuesta sugerida correspondiente.

![Paso de ruta de acción configurado con tres grupos de acciones, uno para cada respuesta sugerida.]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. Conecta cada grupo de acciones a un paso de mensaje RCS y luego añade contenido basado en la respuesta sugerida asociada.
5. Continúa el flujo de trabajo conversacional añadiendo respuestas sugeridas a cualquier mensaje de seguimiento.
6. Repite los pasos 2–4 hasta que el flujo de trabajo esté completo.

![Canvas mostrando un flujo de trabajo conversacional con dos rutas de acción.]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

## Paso 4: Previsualiza y prueba tu mensaje {#step-4-preview-and-test-your-message}

Braze siempre recomienda previsualizar y probar tu mensaje antes de enviarlo. Cambia a la pestaña **Test** para enviar un SMS, MMS o RCS de prueba a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/#content-test-groups) o a usuarios individuales, o previsualiza el mensaje como un usuario directamente en Braze.

{% alert tip %}
Si deseas probar en cuántos segmentos se puede dividir tu SMS, prueba la longitud de tu texto con la [calculadora de segmentos SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/#segment-calculator).
{% endalert %}

![Vista previa del texto SMS desde la pestaña Test del compositor. En la sección de perfil, el campo Nombre está configurado como "James". En la sección de vista previa, el SMS ahora dice "Hola James, ¡agradecemos tu apoyo!"]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert note %}
Para MMS, el orden de los activos (imagen y cuerpo del mensaje) no se puede personalizar. El orden depende del teléfono que recibe el mensaje.
{% endalert %}

{% alert note %}
Dado que la renderización de RCS está controlada por el sistema operativo del usuario, el fabricante del dispositivo, el operador y la aplicación de mensajería (por ejemplo, Google Messages frente a Apple Messages), la apariencia del mensaje puede variar. La vista previa mostrada en Braze puede no coincidir exactamente con lo que recibe un usuario final. Valida la renderización final en dispositivos reales siempre que sea posible. Para más detalles sobre la renderización de RCS en dispositivos iOS, consulta [¿Por qué mi mensaje RCS no se renderiza correctamente en dispositivos iOS?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs/#why-doesnt-my-rcs-message-render-accurately-on-ios-devices).
{% endalert %}

Para más información, consulta [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=sms%2Fmms%20and%20rcs).

## Paso 5: Construye el resto de tu campaña o Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

A continuación, construye el resto de tu campaña. Consulta las siguientes secciones para más detalles sobre cómo usar mejor nuestras herramientas para crear tu mensaje.

### Elige la planificación de entrega o el desencadenante {#choose-delivery-schedule-or-trigger}

Los mensajes se pueden entregar en función de una hora planificada, una acción o un desencadenante de API. Para más información, consulta [Planificar tu campaña]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).

Para la entrega basada en acciones, también puedes establecer la duración de la campaña y las [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/).

En este paso también puedes especificar controles de entrega, como permitir que los usuarios vuelvan a ser [elegibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/#campaigns) para recibir la campaña, o habilitar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping).

### Elige los usuarios objetivo {#choose-users-to-target}

A continuación, [dirige a los usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/) eligiendo segmentos o filtros para acotar tu audiencia. Ya deberías haber elegido el grupo de suscripción, que filtra a los usuarios por el nivel o categoría de comunicación que desean tener contigo.

{% multi_lang_include target_audiences.md %}

Selecciona la audiencia más amplia de tus segmentos y acota ese segmento aún más con filtros opcionales. Recibirás automáticamente una vista previa de la población aproximada de ese segmento. Ten en cuenta que la pertenencia exacta al segmento siempre se calcula antes de enviar el mensaje.

{% alert tip %}
¿Te interesa la reorientación? Consulta [Reorientación de usuarios]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/) para saber más.
{% endalert %}

### Elige eventos de conversión {#choose-conversion-events}

Braze te permite hacer seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), después de recibir una campaña. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se contará una conversión si el usuario realiza la acción especificada.

Los eventos de conversión te ayudan a medir el éxito de tu campaña. Por ejemplo:

- Si estás usando geotargeting para desencadenar un mensaje cuyo objetivo final es que el usuario realice una compra, establece el evento de conversión como `Purchase`.
- Si intentas dirigir al usuario a tu aplicación, establece el evento de conversión como `Starts Session`.

También puedes establecer eventos de conversión personalizados según tu caso de uso específico.

{% endtab %}
{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu componente de Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, implementar pruebas multivariante e Intelligent Selection, y más, consulta el paso [Construir tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas) de nuestra documentación de Canvas.

{% endtab %}
{% endtabs %}

## Paso 6: Revisa y despliega {#step-6-review-and-deploy}

Cuando hayas terminado de construir tu campaña o Canvas, revisa sus detalles, pruébala y luego ¡envíala!

A continuación, consulta [Informes de SMS, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting/) para aprender cómo puedes acceder a los resultados de tus campañas.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Puedo enviar mensajes de voz pregrabados con RCS? {#can-i-send-pre-recorded-voicemails-with-rcs}

Sí, puedes usar mensajes multimedia para admitir archivos de audio.