---
nav_title: Crear un mensaje de WhatsApp
article_title: Crear un mensaje de WhatsApp
page_order: 1
description: "Este artículo de referencia cubre los pasos necesarios para crear y configurar un mensaje de WhatsApp."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
search_rank: 1
---

# Crear un mensaje de WhatsApp {#create-a-whatsapp-message}

> Las campañas de WhatsApp son ideales para comunicarte directamente con tus clientes y conversar con ellos de forma programática. Puedes usar Liquid y otro contenido dinámico para crear una experiencia personalizada con tus usuarios y fomentar un entorno que mejore una experiencia de usuario discreta con tu marca.

## Requisitos previos {#prerequisites}

Antes de poder crear mensajes de WhatsApp, debes revisar y completar lo siguiente desde el [resumen de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/):
  - Aceptar las políticas, límites y reglas de contenido
  - Configurar tu conexión de WhatsApp
  - Crear plantillas iniciales en Meta para usar en tus mensajes

## Crear un mensaje {#creating-a-message}

### Paso 1: Elige dónde crear tu mensaje {#step-1-choose-where-to-build-your-message}

{% alert note %}
WhatsApp crea diferentes [plantillas de mensaje](#template-messages) para cada idioma. Crea una campaña para cada idioma con segmentación para servir la plantilla correcta a los usuarios, o usa Canvas.
{% endalert %}

¿No estás seguro de si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para envíos de mensajería únicos y dirigidos, mientras que los Canvas son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaign %}

**Pasos:**

1. Ve a la página **Campaigns** y haz clic en <i class="fas fa-plus"></i> **Create Campaign**.
2. Selecciona **WhatsApp** o, para campañas dirigidas a múltiples canales, selecciona **Multichannel Campaign**.
3. Dale a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) según sea necesario.
   * Las etiquetas facilitan encontrar tus campañas y generar informes a partir de ellas. Por ejemplo, al usar el [Generador de informes]({{site.baseurl}}/user_guide/analytics/reports/report_builder/), puedes filtrar por etiquetas específicas.
5. Añade y nombra tantas variantes como necesites para tu campaña. Puedes elegir diferentes plataformas, tipos de mensaje y diseños para cada una de las variantes añadidas. Para más información sobre este tema, consulta [Pruebas multivariante y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% alert tip %}
Si todos los mensajes de tu campaña son similares o tienen el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. Luego puedes elegir **Copy from Variant** en el desplegable **Add Variant**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Pasos:**

1. [Crea tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) usando el compositor de Canvas.
2. Después de configurar tu Canvas, añade un paso en el constructor de Canvas. Dale a tu paso un nombre claro y significativo.
3. Elige una [planificación de paso]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#schedule-delay) y especifica un retraso según sea necesario.
4. Filtra tu audiencia para este paso según sea necesario. Puedes refinar aún más los destinatarios de este paso especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se verificarán después del retraso en el momento en que se envíen los mensajes.
5. Elige tu [comportamiento de avance]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/).
6. Elige cualquier otro canal de mensajería que quieras combinar con tu mensaje.

{% alert tip %}
Si un Canvas basado en acciones se desencadena por un mensaje entrante de WhatsApp, puedes hacer referencia a las propiedades de WhatsApp en cualquier paso del Canvas hasta la siguiente ruta de acción.
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 2: Redacta tu mensaje de WhatsApp {#step-2-compose-your-whatsapp-message}

Selecciona si deseas crear un [mensaje de plantilla](#template-messages) de WhatsApp o un mensaje de respuesta, según tu caso de uso. Cualquier conversación iniciada por la empresa debe comenzar con una plantilla aprobada, mientras que los mensajes de respuesta pueden usarse en respuestas a mensajes entrantes de los usuarios dentro de una ventana de 24 horas.

![La sección Variantes de mensaje te permite seleccionar un grupo de suscripción y uno de dos tipos de mensaje: mensaje de plantilla de WhatsApp y mensaje de respuesta.]({% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Mensajes de plantilla %}

Puedes usar [plantillas de mensaje de WhatsApp aprobadas]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/#step-3-create-whatsapp-templates
) para iniciar conversaciones con tus usuarios en WhatsApp. Estos mensajes se envían previamente a WhatsApp para aprobación de contenido, lo que puede tardar hasta 24 horas. Cualquier edición que hagas en el texto debe editarse y reenviarse a WhatsApp.

Los campos de texto deshabilitados (resaltados en gris) no se pueden editar, ya que forman parte de la plantilla de WhatsApp aprobada. Para actualizar el texto deshabilitado, debes editar tu plantilla y obtener una nueva aprobación.

#### Idiomas {#languages}

Cada plantilla tiene un idioma asignado, por lo que necesitas crear una campaña o un paso de Canvas para cada idioma para configurar correctamente la coincidencia de usuarios. Por ejemplo, si estás creando un Canvas que usa plantillas asignadas con indonesio e inglés, necesitas crear un paso de Canvas para la plantilla en indonesio y un paso de Canvas para la plantilla en inglés.

![Lista de plantillas que incluye vistas previas de sus mensajes, sus idiomas asignados y su estado de aprobación.]({% image_buster /assets/img/whatsapp/whatsapp_templates.png %}){: style="max-width:80%;"}

Si estás añadiendo texto en un idioma que se escribe de derecha a izquierda, ten en cuenta que la apariencia final de los mensajes de derecha a izquierda depende en gran medida de cómo los proveedores de servicios los renderizan. Para conocer las mejores prácticas sobre cómo crear mensajes de derecha a izquierda que se muestren con la mayor precisión posible, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/).

#### Variables {#variables}

Si añadiste variables al crear la plantilla de WhatsApp en el Meta Business Manager, esas variables aparecerán como espacios en blanco en el creador de mensajes. Reemplaza estos espacios en blanco con Liquid o texto plano. Para usar texto plano, utiliza el formato "texto aquí" encerrado entre llaves dobles. Si optaste por incluir imágenes al crear tu plantilla, puedes cargar o añadir imágenes desde la biblioteca de medios o haciendo referencia a una URL de imagen. Cuando sea posible, recomendamos cargar las imágenes directamente en tu biblioteca de medios para garantizar consistencia y fiabilidad.

Ten en cuenta que los campos de texto deshabilitados (resaltados en gris) no se pueden editar, ya que forman parte de la plantilla de WhatsApp aprobada. Si deseas actualizar el texto deshabilitado, debes editar tu plantilla y obtener una nueva aprobación.

{% alert tip %}
{% raw %}
Si planeas usar Liquid, asegúrate de incluir un valor predeterminado para la personalización elegida, de modo que, en caso de que el perfil de usuario del destinatario esté incompleto, no reciba un mensaje. WhatsApp no enviará ningún mensaje con variables de Liquid faltantes.
{% endraw %}
{% endalert %}

![La herramienta Añadir personalización con el atributo "first_name" y el valor predeterminado "you".]({% image_buster /assets/img/whatsapp/whatsapp7.png %}){: style="max-width:80%;"}

### Enlaces dinámicos {#dynamic-links}

Las URL de llamada a la acción pueden contener variables, aunque Meta requiere que estén al final de la URL, como `{% raw %}https://example.com/{{variable}}{% endraw %}`, donde la variable puede reemplazarse en Braze con Liquid. Los enlaces también pueden incluirse como texto del cuerpo como parte de la plantilla. Ambos tipos de enlaces pueden acortarse y rastrearse usando el [seguimiento de clics]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/click_tracking/).

### Imágenes dinámicas {#dynamic-images}

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% tab Mensajes de respuesta %}

Puedes usar mensajes de respuesta para responder a mensajes entrantes de tus usuarios. Estos mensajes se crean dentro de la aplicación en Braze durante tu experiencia de composición y pueden editarse en cualquier momento. Puedes usar Liquid para hacer coincidir el idioma del mensaje de respuesta con los usuarios apropiados.

Hay cinco diseños de mensajes de respuesta que puedes usar:
- Respuesta rápida
- Mensaje de texto
- Mensaje multimedia
- Botón de llamada a la acción
- Mensaje de lista

![El compositor de mensajes de respuesta para un mensaje de respuesta que da la bienvenida a nuevos usuarios con un código de descuento.]({% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Paso 3: Previsualiza y prueba tu mensaje {#step-3-preview-and-test-your-message}

Braze siempre recomienda previsualizar y probar tu mensaje antes de enviarlo. Cambia a la pestaña **Test** para enviar un mensaje de prueba de WhatsApp a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/#content-test-groups) o usuarios individuales, o previsualiza el mensaje como un usuario directamente en Braze.

![Un mensaje de vista previa para un usuario personalizado llamado Max.]({% image_buster /assets/img/whatsapp/whatsapp8.png %}){: style="max-width:80%;"}

{% alert note %}
Se requiere una ventana de conversación para enviar mensajes de respuesta, incluidos los mensajes de prueba. Para iniciar una ventana de conversación, envía un mensaje de WhatsApp al número de teléfono asociado con el grupo de suscripción que estás usando para este mensaje. El número de teléfono asociado aparece en la alerta de la pestaña **Test**.
{% endalert %}

![Una alerta que dice: "Para probar, primero abre una ventana de conversación enviando un mensaje de WhatsApp al +1 217-582-9414. Luego, envía tu mensaje de respuesta al usuario de prueba."]({% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}){: style="max-width:70%;"}

Para más información, consulta [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=whatsapp).

### Paso 4: Construye el resto de tu campaña o Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

A continuación, construye el resto de tu campaña. Consulta las siguientes secciones para más detalles sobre cómo usar mejor nuestras herramientas para crear mensajes de WhatsApp.

#### Elige una planificación de entrega o desencadenante {#choose-a-delivery-schedule-or-trigger}

Los mensajes de WhatsApp pueden entregarse según un horario planificado, una acción o un desencadenante de API. Para más información, consulta [Planificar tu campaña]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).

Para la entrega basada en acciones, también puedes establecer la duración de la campaña y las [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/).

En este paso también puedes especificar controles de entrega, como permitir que los usuarios vuelvan a ser [elegibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/#campaigns) para recibir la campaña, o habilitar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping).

#### Elige los usuarios objetivo {#choose-users-to-target}

A continuación, debes [dirigirte a los usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/) eligiendo segmentos o filtros para reducir tu audiencia. Ya deberías haber elegido el grupo de suscripción, que filtra a los usuarios por el nivel o categoría de comunicación que desean tener contigo. En este paso, seleccionas la audiencia más amplia de tus segmentos y la reduces aún más con nuestros filtros. Recibirás automáticamente una instantánea de cómo se ve aproximadamente la población de ese segmento. Recuerda que la membresía exacta del segmento siempre se calcula antes de enviar el mensaje.

{% multi_lang_include target_audiences.md %}

#### Elige eventos de conversión {#choose-conversion-events}

Braze te permite rastrear con qué frecuencia los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), después de recibir una campaña. Puedes permitir una ventana de hasta 30 días durante la cual se contará una conversión si el usuario realiza la acción especificada.

También puedes establecer eventos de conversión personalizados según tu caso de uso específico. Sé creativo y piensa en cómo realmente quieres medir el éxito de esta campaña.

{% endtab %}

{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu componente de Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, implementar pruebas multivariante e Intelligent Selection, y más, consulta el paso [Construir tu Canvas]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/) de nuestra documentación de Canvas.

Dado que las ventanas de conversación solo pueden durar 24 horas por mensaje entrante, Braze verificará que no haya retrasos que excedan las 24 horas entre un mensaje entrante y un mensaje de respuesta.

{% endtab %}
{% endtabs %}

### Paso 5: Revisa y despliega {#step-5-review-and-deploy}

Después de terminar de construir tu campaña o Canvas, revisa sus detalles, pruébalo y luego ¡envíalo!

A continuación, consulta [Informes de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/reporting/) para aprender cómo puedes acceder a los resultados de tus campañas de WhatsApp.

## Características de WhatsApp compatibles {#supported-whatsapp-features}

### Mensajes salientes {#outbound-messages}

Las siguientes características son compatibles con los mensajes salientes de WhatsApp que envías a través de Braze:

| Característica | Detalles | Tamaño máximo | Formatos compatibles |
| ------- | ------- | ------------- | ---------------------- |
| Texto de encabezado | Se admiten cadenas y parámetros de variables. | — | —
| Texto del cuerpo | Se admiten cadenas y parámetros de variables. | — | — |
| Texto de pie de página | Se admiten cadenas y parámetros de variables. | — | — |
| Enlaces CTA | Se admiten varios tipos de llamada a la acción (CTA). Para más detalles, consulta [Tipos de llamada a la acción](#ctas). | — | — |
| Imágenes | Las imágenes pueden incrustarse dentro del texto del cuerpo. Deben ser de 8 bits y usar un modelo de color RGB o RGBA. | < 5 MB | `.png`, `.jpg`, `.jpeg` |
| Documentos | Los documentos pueden incrustarse dentro del texto del cuerpo. Los archivos deben estar alojados mediante URL. | < 100 MB | `.txt`, `.xls`, `.xlsx`, `.doc`, `.docx`, `.ppt`, `.pttx`, `.pdf` |
| Videos | Los videos pueden incrustarse dentro del texto del cuerpo. Los archivos deben estar alojados mediante URL o en la [biblioteca de medios de Braze]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/). | < 16 MB | `.3gp`, `.mp4` |
| Audio | El audio solo es compatible a través de mensajes de respuesta. Los archivos deben estar alojados mediante URL. | < 16 MB | `.aac`, `.amr`, `.mp3`, `.mp4`, `.ogg` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Outbound messages" }

{% multi_lang_include alerts/important_alerts.md alert='Meta MP4 video issue' %}

### Mensajes entrantes {#inbound-messages}

Las siguientes características son compatibles con los mensajes entrantes de WhatsApp que recibes a través de Braze:

| Característica | Detalles | Formatos compatibles |
| ------- | ------- | ------------------ |
| Texto del cuerpo | Solo se admiten cadenas estándar. | — |
| Imágenes | Las imágenes deben ser de 8 bits y usar un modelo de color RGB o RGBA. Los archivos deben pesar menos de 5 MB. | `.jpg`, `.png` |
| Audio | Solo se admiten archivos Ogg codificados con el códec Opus. Otros formatos Ogg no son compatibles. | `.aac`, `.mp4`, `.mpeg`, `.amr`, `.ogg (solo Opus)` |
| Documentos | Los documentos son compatibles a través de archivos adjuntos de mensaje. | `.txt`, `.pdf`, `.ppt`, `.doc`, `.xls`, `.docx`, `.pptx`, `.xlsx` |
| Video | Solo se admiten el códec de video H.264 y el códec de audio AAC. Los videos deben tener una sola pista de audio o ninguna. | `.mp4`, `.3gp` |
| Enlaces CTA | Se admiten varios tipos de llamada a la acción (CTA). Para más detalles, consulta [Tipos de llamada a la acción](#ctas). | — |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Inbound messages" }

### Tipos de llamada a la acción {#ctas}

Los siguientes tipos de llamada a la acción son compatibles con los mensajes de WhatsApp que envías a través de Braze:

| Tipo de CTA | Detalles |
| ----------- |---------------- |
| Visitar sitio web | Un botón máximo (incluidos parámetros de variables). |
| Llamar a número de teléfono | Disponible solo para plantillas de mensaje. <br>Un botón máximo. |
| Botones de respuesta rápida personalizados | Tres botones máximo. |
| Botón de exclusión de marketing | De forma predeterminada, los estados de suscripción no se actualizan automáticamente. Para un recorrido completo, consulta [Adhesiones y exclusiones]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs/#marketing-opt-out-selection). |
| Plantillas de mensaje con código de cupón | Disponible solo para plantillas de mensaje. <br>Pueden abrirse y editarse como otras plantillas de mensaje, y son compatibles con Liquid y códigos promocionales de Braze. |
| Mensajes de respuesta con CTA | Crea un mensaje de respuesta que incluya un botón de llamada a la acción. |
| [Mensajes de respuesta con lista]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users/#list-messages) | Crea un mensaje de respuesta que incluya una lista de hasta 10 opciones para que los usuarios elijan. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Call-to-action types #ctas" }