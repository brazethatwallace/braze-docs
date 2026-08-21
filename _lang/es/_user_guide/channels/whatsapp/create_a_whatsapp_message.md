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

Antes de poder crear mensajes de WhatsApp, debes revisar y completar lo siguiente desde el [resumen de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup):
  - Aceptar las políticas, los límites y las reglas de contenido
  - Configurar tu conexión de WhatsApp
  - Crear plantillas iniciales en Meta para usar en tus mensajes

## Creación de un mensaje {#creating-a-message}

### Paso 1: Elige dónde crear tu mensaje {#step-1-choose-where-to-build-your-message}

{% alert note %}
WhatsApp crea diferentes [plantillas de mensaje](#template-messages) para cada idioma. Crea una Campaign para cada idioma con segmentación para servir la plantilla correcta a los usuarios, o usa Canvas.
{% endalert %}

¿No estás seguro de si tu mensaje debe enviarse mediante una Campaign o un Canvas? Las Campaigns son mejores para campañas de mensajería únicas y dirigidas, mientras que los Canvas son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaign %}

**Pasos:**

1. Ve a la página **Campaigns** y haz clic en <i class="fas fa-plus"></i> **Crear Campaign**.
2. Selecciona **WhatsApp** o, para Campaigns dirigidas a múltiples canales, selecciona **Campaign multicanal**.
3. Dale a tu Campaign un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) y [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) según sea necesario.
   * Las etiquetas facilitan encontrar tus Campaigns y generar informes a partir de ellas. Por ejemplo, al usar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reports/report_builder), puedes filtrar por etiquetas específicas.
5. Añade y nombra tantas variantes como necesites para tu Campaign. Puedes elegir diferentes plataformas, tipos de mensaje y diseños para cada una de las variantes añadidas. Para más información sobre este tema, consulta [Pruebas multivariante y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si todos los mensajes de tu Campaign son similares o tienen el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. Luego puedes elegir **Copiar de variante** en el menú desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Pasos:**

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% alert tip %}
Si un Canvas basado en acciones se desencadena por un mensaje entrante de WhatsApp, puedes hacer referencia a las propiedades de WhatsApp en cualquier paso del Canvas hasta la siguiente ruta de acción.
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 2: Redacta tu mensaje de WhatsApp {#step-2-compose-your-whatsapp-message}

Selecciona si deseas crear un [mensaje de plantilla](#template-messages) de WhatsApp o un mensaje de respuesta, según tu caso de uso. Cualquier conversación iniciada por la empresa debe comenzar con una plantilla aprobada, mientras que los mensajes de respuesta se pueden usar en respuestas a mensajes entrantes de los usuarios dentro de una ventana de 24 horas.

![La sección Variantes de mensaje te permite seleccionar un grupo de suscripción y uno de dos tipos de mensaje: mensaje de plantilla de WhatsApp y mensaje de respuesta.]({% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Mensajes de plantilla %}

Puedes usar [plantillas de mensaje de WhatsApp aprobadas]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#step-3-create-whatsapp-templates
) para iniciar conversaciones con tus usuarios en WhatsApp. Estas se envían previamente a WhatsApp para la aprobación de contenido, lo que puede tardar hasta 24 horas. Cualquier edición que hagas en el texto debe editarse y reenviarse a WhatsApp.

Para crear y enviar una nueva plantilla sin salir del creador de Campaign o Canvas, selecciona **Crear nueva plantilla**. Para categorías, tipos y el proceso completo de creación, consulta [Creador de plantillas de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder).

Los campos de texto deshabilitados (resaltados en gris) no se pueden editar, ya que forman parte de la plantilla de WhatsApp aprobada. Para actualizar el texto deshabilitado, debes editar tu plantilla y obtener una nueva aprobación.

#### Idiomas {#languages}

Cada plantilla tiene un idioma asignado, por lo que necesitas crear una Campaign o un paso en Canvas para cada idioma a fin de configurar correctamente la coincidencia de usuarios. Por ejemplo, si estás creando un Canvas que usa plantillas asignadas con indonesio e inglés, necesitas crear un paso en Canvas para la plantilla en indonesio y un paso en Canvas para la plantilla en inglés.

![Lista de plantillas que incluye vistas previas de sus mensajes, sus idiomas asignados y su estado de aprobación.]({% image_buster /assets/img/whatsapp/whatsapp_templates.png %}){: style="max-width:80%;"}

Si estás añadiendo texto en un idioma que se escribe de derecha a izquierda, ten en cuenta que la apariencia final de los mensajes de derecha a izquierda depende en gran medida de cómo los proveedores de servicios los rendericen. Para conocer las mejores prácticas sobre cómo redactar mensajes de derecha a izquierda que se muestren con la mayor precisión posible, consulta [Creación de mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Variables {#variables}

Si añadiste variables al crear la plantilla de WhatsApp en el Meta Business Manager, esas variables aparecerán como espacios en blanco en el creador de mensajes. Reemplaza estos espacios en blanco con Liquid o texto plano. Para usar texto plano, utiliza el formato "texto aquí" encerrado entre llaves dobles. Si optaste por incluir imágenes al crear tu plantilla, puedes subir o añadir imágenes desde la biblioteca de medios o haciendo referencia a una URL de imagen. Cuando sea posible, recomendamos subir las imágenes directamente a tu biblioteca de medios para garantizar la consistencia y fiabilidad.

Ten en cuenta que los campos de texto deshabilitados (resaltados en gris) no se pueden editar, ya que forman parte de la plantilla de WhatsApp aprobada. Si deseas actualizar el texto deshabilitado, debes editar tu plantilla y obtener una nueva aprobación.

{% alert tip %}
{% raw %}
Si planeas usar Liquid, asegúrate de incluir un valor predeterminado para la personalización elegida, de modo que, en caso de que el perfil de usuario del destinatario esté incompleto, no reciba un mensaje. WhatsApp no enviará ningún mensaje con variables de Liquid faltantes.
{% endraw %}
{% endalert %}

![La herramienta Añadir personalización con el atributo "first_name" y el valor predeterminado "you".]({% image_buster /assets/img/whatsapp/whatsapp7.png %}){: style="max-width:80%;"}

### Enlaces dinámicos {#dynamic-links}

Las URL de llamada a la acción pueden contener variables, aunque Meta requiere que estén al final de la URL, como `{% raw %}https://example.com/{{variable}}{% endraw %}`, donde la variable puede reemplazarse en Braze con Liquid. Los enlaces también pueden incluirse como texto del cuerpo como parte de la plantilla. Ambos tipos de enlaces pueden acortarse y rastrearse usando el [seguimiento de clics]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/click_tracking).

### Imágenes dinámicas {#dynamic-images}

Puedes añadir imágenes desde la biblioteca de medios o por URL. Cuando usas una URL, puedes personalizar la imagen con [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) o [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), incluyendo lógica completa de Liquid en cualquier parte de la URL. Las imágenes dinámicas son compatibles con los mensajes de plantilla y los mensajes de respuesta (mensajes multimedia y diseños de respuesta rápida).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% tab Mensajes de respuesta %}

Puedes usar mensajes de respuesta para responder a mensajes entrantes de tus usuarios. Estos mensajes se crean en la aplicación en Braze durante tu experiencia de composición y se pueden editar en cualquier momento. Puedes usar Liquid para hacer coincidir el idioma del mensaje de respuesta con los usuarios apropiados.

Hay cinco diseños de mensajes de respuesta que puedes usar:
- Respuesta rápida
- Mensaje de texto
- Mensaje multimedia
- Botón de llamada a la acción
- Mensaje de lista

![El creador de mensajes de respuesta para un mensaje de respuesta que da la bienvenida a nuevos usuarios con un código de descuento.]({% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Paso 3: Previsualiza y prueba tu mensaje {#step-3-preview-and-test-your-message}

Braze siempre recomienda previsualizar y probar tu mensaje antes de enviarlo. Cambia a la pestaña **Prueba** para enviar un mensaje de prueba de WhatsApp a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) o usuarios individuales, o previsualiza el mensaje como un usuario directamente en Braze.

![Un mensaje de vista previa para un usuario personalizado llamado Max.]({% image_buster /assets/img/whatsapp/whatsapp8.png %}){: style="max-width:80%;"}

{% alert note %}
Se requiere una ventana de conversación para enviar mensajes de respuesta, incluidos los mensajes de prueba. Para iniciar una ventana de conversación, envía un mensaje de WhatsApp al número de teléfono asociado con el grupo de suscripción que estás usando para este mensaje. El número de teléfono asociado aparece en la alerta de la pestaña **Prueba**.
{% endalert %}

![Una alerta que indica que abras una ventana de mensaje enviando un mensaje de WhatsApp y luego envíes un mensaje al usuario de prueba.]({% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}){: style="max-width:70%;"}

Para más información, consulta [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=whatsapp).

### Paso 4: Ver los resultados del envío de prueba {#step-4-view-test-send-results}

Después de enviar un mensaje de prueba de WhatsApp, puedes ver un informe de entrega detallado directamente en el creador de mensajes. Esto te ayuda a confirmar que tu mensaje llegó al destinatario previsto y a solucionar fallos antes del lanzamiento.

El botón **Ver resultados de prueba** aparece cuando hay datos de envío de prueba disponibles para la Campaign o el paso en Canvas actual. Selecciónalo para abrir el panel de resultados.

El panel de resultados muestra cada etapa por la que pasó tu mensaje en su camino hacia el destinatario:
- **Braze:** Si Braze procesó y envió el mensaje correctamente
- **Meta:** Si Meta aceptó el mensaje para su entrega
- **Dispositivo del usuario:** Si el mensaje se entregó al dispositivo del destinatario

Cada etapa muestra su estado actual. Si una etapa falló, el panel muestra el error encontrado y orientación sobre cómo resolverlo. Los resultados persisten si cierras y vuelves a abrir la misma Campaign o Canvas.

![Panel de resultados de prueba que muestra dos envíos de prueba exitosos y un envío de prueba fallido.]({% image_buster /assets/img/whatsapp/whatsapp_test_results.png %}){: style="max-width:80%;"}

#### Reintentos e intentos anteriores {#retries-and-past-attempts}

Si un envío de prueba falla, Braze reintenta automáticamente la entrega durante un máximo de 24 horas. El panel de resultados refleja esto con dos pestañas:

- **Más reciente:** El intento de entrega más reciente, actualizado en tiempo real a medida que ocurren los reintentos
- **Intentos anteriores:** Un historial de ejecuciones de reintentos previas, cada una mostrando los estados de las etapas y los errores encontrados

Cuando se determina el resultado final (entrega exitosa, reintentos agotados o un fallo que los reintentos no resolverán), las pestañas se renombran respectivamente a **Resultado** e **Historial de reintentos**.

{% alert note %}
Dado que los reintentos pueden continuar durante un máximo de 24 horas, es posible que no veas un resultado final inmediatamente después de un envío fallido.
{% endalert %}

#### Solución de problemas de fallos {#troubleshoot-failures}

Si una etapa muestra un fallo, el panel muestra el error y los pasos sugeridos a seguir. Las razones comunes por las que un envío de prueba puede fallar incluyen:

- La plantilla de mensaje está pausada o aún no ha sido aprobada en Meta
- El número de teléfono del destinatario tiene limitación de tasa
- Las variables de Liquid en el mensaje no se completaron para el usuario de prueba seleccionado

Para problemas persistentes, verifica el estado de tu plantilla en el Meta Business Manager o comprueba que tu destinatario de prueba tenga los atributos de usuario requeridos completados en Braze.

### Paso 5: Construye el resto de tu Campaign o Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

A continuación, construye el resto de tu Campaign. Consulta las siguientes secciones para más detalles sobre cómo usar mejor nuestras herramientas para crear mensajes de WhatsApp.

#### Elige un horario de entrega o desencadenante {#choose-a-delivery-schedule-or-trigger}

Los mensajes de WhatsApp se pueden entregar según un horario programado, una acción o un desencadenante de API. Para más información, consulta [Programar tu Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Para la entrega basada en acciones, también puedes establecer la duración de la Campaign y las [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

En este paso también puedes especificar controles de entrega, como permitir que los usuarios vuelvan a ser [elegibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) para recibir la Campaign, o habilitar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping).

#### Elige los usuarios a los que dirigirte {#choose-users-to-target}

A continuación, debes [dirigirte a los usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) eligiendo Segments o filtros para reducir tu audiencia. Ya deberías haber elegido el grupo de suscripción, que filtra a los usuarios por el nivel o categoría de comunicación que desean tener contigo. En este paso, seleccionas la audiencia más amplia de tus Segments y la reduces aún más con nuestros filtros. Recibirás automáticamente una instantánea de cómo se ve aproximadamente la población de ese Segment. Recuerda que la membresía exacta del Segment siempre se calcula antes de que se envíe el mensaje.

{% multi_lang_include audience/target_audiences.md %}

#### Elige eventos de conversión {#choose-conversion-events}

Braze te permite rastrear con qué frecuencia los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), después de recibir una Campaign. Puedes permitir una ventana de hasta 30 días durante la cual se contará una conversión si el usuario realiza la acción especificada.

También puedes establecer eventos de conversión personalizados según tu caso de uso específico. Sé creativo y piensa en cómo realmente deseas medir el éxito de esta Campaign.

{% endtab %}

{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu componente de Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, implementar pruebas multivariante y selección inteligente, y más, consulta el paso [Construir tu Canvas]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message) de nuestra documentación de Canvas.

Dado que las ventanas de conversación solo pueden durar 24 horas por mensaje entrante, Braze verificará que no haya retrasos que excedan las 24 horas entre un mensaje entrante y un mensaje de respuesta.

{% endtab %}
{% endtabs %}

### Paso 5: Revisa y despliega {#step-5-review-and-deploy}

Después de terminar de construir la última parte de tu Campaign o Canvas, revisa sus detalles, pruébala y luego ¡envíala!

A continuación, consulta [Informes de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/reporting) para aprender cómo puedes acceder a los resultados de tus Campaigns de WhatsApp.

## Características de WhatsApp compatibles {#supported-whatsapp-features}

### Mensajes salientes {#outbound-messages}

Las siguientes características son compatibles con los mensajes salientes de WhatsApp que envías a través de Braze:

| Característica | Detalles | Tamaño máximo | Formatos compatibles |
| ------- | ------- | ------------- | ---------------------- |
| Texto de encabezado | Se admiten cadenas y parámetros variables. | — | —
| Texto del cuerpo | Se admiten cadenas y parámetros variables. | — | — |
| Texto de pie de página | Se admiten cadenas y parámetros variables. | — | — |
| Enlaces CTA | Se admiten varios tipos de llamada a la acción (CTA). Para más detalles, consulta [Tipos de llamada a la acción](#ctas). | — | — |
| Imágenes | Las imágenes pueden incrustarse dentro del texto del cuerpo. Deben ser de 8 bits y usar un modelo de color RGB o RGBA. | < 5 MB | `.png`, `.jpg`, `.jpeg` |
| Documentos | Los documentos pueden incrustarse dentro del texto del cuerpo. Los archivos deben estar alojados a través de URL. | < 100 MB | `.txt`, `.xls`, `.xlsx`, `.doc`, `.docx`, `.ppt`, `.pttx`, `.pdf` |
| Videos | Los videos pueden incrustarse dentro del texto del cuerpo. Los archivos deben estar alojados a través de URL o en la [biblioteca de medios de Braze]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library). | < 16 MB | `.3gp`, `.mp4` |
| Audio | El audio solo es compatible a través de mensajes de respuesta. Los archivos deben estar alojados a través de URL. | < 16 MB | `.aac`, `.amr`, `.mp3`, `.mp4`, `.ogg` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Mensajes salientes" }

{% multi_lang_include alerts/important_alerts.md alert='Meta MP4 video issue' %}

### Mensajes entrantes {#inbound-messages}

Las siguientes características son compatibles con los mensajes entrantes de WhatsApp que recibes a través de Braze:

| Característica | Detalles | Formatos compatibles |
| ------- | ------- | ------------------ |
| Texto del cuerpo | Solo se admiten cadenas estándar. | — |
| Imágenes | Las imágenes deben ser de 8 bits y usar un modelo de color RGB o RGBA. Los archivos deben pesar menos de 5 MB. | `.jpg`, `.png` |
| Audio | Solo se admiten archivos Ogg codificados con el códec Opus. Otros formatos Ogg no son compatibles. | `.aac`, `.mp4`, `.mpeg`, `.amr`, `.ogg (Opus only)` |
| Documentos | Los documentos son compatibles a través de archivos adjuntos de mensajes. | `.txt`, `.pdf`, `.ppt`, `.doc`, `.xls`, `.docx`, `.pptx`, `.xlsx` |
| Video | Solo se admiten el códec de video H.264 y el códec de audio AAC. Los videos deben tener una sola pista de audio o no tener pista de audio. | `.mp4`, `.3gp` |
| Enlaces CTA | Se admiten varios tipos de llamada a la acción (CTA). Para más detalles, consulta [Tipos de llamada a la acción](#ctas). | — |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mensajes entrantes" }

### Tipos de llamada a la acción {#ctas}

Los siguientes tipos de llamada a la acción son compatibles con los mensajes de WhatsApp que envías a través de Braze:

| Tipo de CTA | Detalles |
| ----------- |---------------- |
| Visitar sitio web | Un botón como máximo (incluidos parámetros variables). |
| Llamar a un número de teléfono | Disponible solo para plantillas de mensajes. <br>Un botón como máximo. |
| Botones de respuesta rápida personalizados | Tres botones como máximo. |
| Botón de exclusión de marketing | De forma predeterminada, los estados de suscripción no se actualizan automáticamente. Para un tutorial completo, consulta [Adhesiones y exclusiones voluntarias]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#marketing-opt-out-selection). |
| Plantillas de mensajes con código de cupón | Disponible solo para plantillas de mensajes. <br>Se pueden abrir y editar como otras plantillas de mensajes, y son compatibles con Liquid y los códigos promocionales de Braze. |
| Mensajes de respuesta con CTA | Crea un mensaje de respuesta que incluya un botón de llamada a la acción. |
| [Mensajes de respuesta con lista]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#list-messages) | Crea un mensaje de respuesta que incluya una lista de hasta 10 opciones entre las que los usuarios pueden elegir. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de llamada a la acción" }