---
nav_title: Crear un mensaje de WhatsApp
article_title: Crear un mensaje de WhatsApp
page_order: 1
description: "Este artículo de referencia cubre cómo crear un mensaje de WhatsApp y configurar los campos, la configuración y el comportamiento de los mensajes específicos de WhatsApp."
page_type: reference
tool:
  - Campaigns
  - Canvas
channel:
  - WhatsApp
search_rank: 1
---

# Crear un mensaje de WhatsApp {#create-a-whatsapp-message}

> Usa Campaigns de WhatsApp para comunicarte directamente con tus clientes. Utiliza Liquid y otro contenido dinámico para personalizar cada mensaje y crear una experiencia de marca consistente.

## Requisitos previos {#prerequisites}

Antes de empezar, asegúrate de tener lo siguiente:

| Requisito | Descripción |
| --- | --- |
| Campaign o Canvas | Configura una [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) o un [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) antes de redactar tu mensaje de WhatsApp. |
| Configuración del canal de WhatsApp | Completa el [flujo de configuración de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup): acepta las políticas, configura tu conexión y establece la infraestructura de envío. |
| Plantillas aprobadas | Para envíos iniciados por la empresa, crea y aprueba plantillas en Meta. Para más detalles, consulta el [paso 3 de la configuración de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#step-3-create-whatsapp-templates). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos de mensajes de WhatsApp" }

## Tipo de mensaje {#message-type}

WhatsApp admite dos tipos de mensajes en Braze:

- **Mensaje de plantilla:** Se usa para conversaciones iniciadas por la empresa. Las plantillas deben aprobarse en Meta antes del envío.
- **Mensaje de respuesta:** Se usa para responder a mensajes entrantes de los usuarios durante una ventana de conversación activa de 24 horas.

## Grupo de suscripción {#subscription-group}

Selecciona un grupo de suscripción de WhatsApp para cada variante de mensaje o paso en Canvas de tipo Mensaje. El grupo de suscripción determina qué configuración de remitente se utiliza y qué usuarios son elegibles para recibir el mensaje.

## Idiomas para mensajes de plantilla {#languages-for-template-messages}

Cada plantilla aprobada está vinculada a un idioma específico. Configura variantes o pasos en Canvas separados cuando necesites admitir varios idiomas de plantilla.

Si estás añadiendo texto en un idioma de derecha a izquierda, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

## Composición {#step-2-compose-your-whatsapp-message}

Redacta tu contenido de WhatsApp en el creador de mensajes. Para las opciones de configuración específicas de WhatsApp, utiliza la siguiente referencia de campos.

| Campo o configuración | Qué controla | Notas |
| --- | --- | --- |
| **Grupo de suscripción** | El remitente de WhatsApp y la audiencia elegible para el mensaje. | El número de teléfono de envío asociado aparece en la alerta de la pestaña **Prueba**. |
| **Tipo de mensaje** | Si la variante envía un mensaje de plantilla o un mensaje de respuesta. | Los envíos iniciados por la empresa requieren una plantilla. Los mensajes de respuesta requieren una ventana de conversación activa. |
| **Plantilla** (Mensajes de plantilla) | La plantilla de Meta aprobada que se usa para enviar el mensaje. | Los campos deshabilitados en el creador provienen de la plantilla aprobada y solo se pueden modificar en Meta y volver a aprobar. |
| **Idioma** (Mensajes de plantilla) | El idioma de la plantilla seleccionado para la variante o el paso. | Crea una variante de Campaign o un paso en Canvas por idioma para coincidir correctamente con los destinatarios. |
| **Variables** (Mensajes de plantilla) | Valores insertados en los marcadores de posición de las variables de la plantilla. | Usa Liquid o texto plano entre llaves dobles. Incluye valores predeterminados para Liquid para que los envíos no fallen cuando falten datos del perfil. |
| **Enlaces dinámicos** | URLs de llamada a la acción personalizadas. | Meta requiere que las variables aparezcan al final de las URLs de CTA. |
| **Imágenes dinámicas** | URL del archivo multimedia o imagen de la biblioteca multimedia utilizada en mensajes de plantilla o de respuesta. | Las imágenes dinámicas admiten Liquid y contenido conectado en las URLs. |
| **Diseño de respuesta** (Mensajes de respuesta) | El formato del contenido de respuesta. | Los diseños compatibles son Respuesta rápida, Mensaje de texto, Mensaje multimedia, Botón de llamada a la acción, Mensaje de lista, Mensaje de flujo, Mensajes de producto de Meta y Carrusel. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos y configuraciones específicos de WhatsApp" }

{% tabs %}
{% tab Mensajes de plantilla %}

### Mensajes de plantilla {#template-messages}

Utiliza [mensajes de plantilla de WhatsApp aprobados]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#step-3-create-whatsapp-templates) para iniciar conversaciones en WhatsApp. Las aprobaciones de plantillas las gestiona Meta y pueden tardar hasta 24 horas. Si editas el texto de la plantilla, actualízala en Meta y vuelve a enviarla para su aprobación.

Para crear y enviar una nueva plantilla sin salir del creador de Campaign o Canvas, selecciona **Crear nueva plantilla**. Para las categorías, tipos y el proceso de creación completo, consulta [Creador de plantillas de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder).

Los campos de texto deshabilitados (resaltados en gris) no se pueden editar, ya que forman parte de la plantilla de WhatsApp aprobada. Para hacer actualizaciones en el texto deshabilitado, debes editar tu plantilla y obtener una nueva aprobación.

#### Campos de contenido {#content-fields}

Utiliza la tabla de referencia de campos para las definiciones de variables, enlaces dinámicos e imágenes dinámicas. Esta sección cubre el comportamiento específico de las plantillas y ejemplos.

![Lista de plantillas que incluye vistas previas de sus mensajes, sus idiomas asignados y su estado de aprobación.]({% image_buster /assets/img/whatsapp/whatsapp_templates.png %}){: style="max-width:80%;"}

{% alert tip %}
Si usas Liquid, incluye valores predeterminados para los campos de personalización. WhatsApp no envía los mensajes a los que les faltan valores de personalización.
{% endalert %}

![La herramienta Añadir personalización con el atributo "first_name" y el valor predeterminado "you".]({% image_buster /assets/img/whatsapp/whatsapp7.png %}){: style="max-width:80%;"}

### Imágenes dinámicas {#dynamic-images}

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% tab Mensajes de respuesta %}

### Mensajes de respuesta {#response-messages}

Utiliza los mensajes de respuesta para responder a mensajes entrantes de los usuarios durante la ventana de conversación activa de 24 horas. Estos mensajes se crean en Braze y se pueden editar en cualquier momento.

Los mensajes de respuesta admiten estos diseños:
- Respuesta rápida
- Mensaje de texto
- Mensaje multimedia
- Botón de llamada a la acción
- Mensaje de lista
- Mensaje de flujo
- Mensajes de producto de Meta
- Carrusel

![El creador de mensajes de respuesta para un mensaje de respuesta que da la bienvenida a nuevos usuarios con un código de descuento.]({% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

## Resultados del envío de prueba de WhatsApp {#step-4-view-test-send-results}

Después de enviar un mensaje de prueba de WhatsApp, puedes ver un informe detallado de entrega directamente en el creador de mensajes. Esto te ayuda a confirmar que tu mensaje llegó al destinatario previsto y a solucionar fallos antes del lanzamiento.

El botón **Ver resultados de prueba** aparece cuando hay datos del envío de prueba disponibles para la Campaign o paso en Canvas actual. Selecciónalo para abrir el panel de resultados.

El panel de resultados muestra cada etapa por la que pasó tu mensaje en su camino hacia el destinatario:
- **Braze:** Si Braze procesó y envió el mensaje correctamente
- **Meta:** Si Meta aceptó el mensaje para su entrega
- **Dispositivo del usuario:** Si el mensaje se entregó al dispositivo del destinatario

Cada etapa muestra su estado actual. Si una etapa falló, el panel muestra el error encontrado y orientación sobre cómo resolverlo. Los resultados persisten si cierras y vuelves a abrir la misma Campaign o Canvas.

![Panel de resultados de prueba que muestra dos envíos de prueba exitosos y uno fallido.]({% image_buster /assets/img/whatsapp/whatsapp_test_results.png %}){: style="max-width:80%;"}

### Reintentos e intentos anteriores {#retries-and-past-attempts}

Si un envío de prueba falla, Braze reintenta automáticamente la entrega durante un máximo de 24 horas. El panel de resultados refleja esto con dos pestañas:

- **Más reciente:** El intento de entrega más reciente, actualizado en tiempo real a medida que ocurren los reintentos
- **Intentos anteriores:** Un historial de ejecuciones de reintento previas, cada una mostrando los estados de las etapas y los errores encontrados

Cuando se determina el resultado final (entrega exitosa, reintentos agotados o un fallo que no se resolverá reintentando), las pestañas se renombran respectivamente a **Resultado** e **Historial de reintentos**.

{% alert note %}
Dado que los reintentos pueden continuar durante un máximo de 24 horas, es posible que no veas un resultado final inmediatamente después de un envío fallido.
{% endalert %}

### Solución de problemas de fallos {#troubleshoot-failures}

Si una etapa muestra un fallo, el panel muestra el error y los pasos sugeridos a seguir. Las razones comunes por las que un envío de prueba puede fallar incluyen:

- La plantilla de mensaje está pausada o aún no ha sido aprobada en Meta
- El número de teléfono del destinatario tiene un límite de tasa aplicado
- Las variables Liquid del mensaje no se completaron para el usuario de prueba seleccionado

Para problemas persistentes, verifica el estado de tu plantilla en Meta Business Administrador o comprueba que tu destinatario de prueba tenga los atributos de usuario requeridos completados en Braze.

## Características compatibles {#supported-whatsapp-features}

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

## Próximos pasos {#next-steps}

Después de redactar tu mensaje de WhatsApp, continúa creando y validando tu envío:

- [Programa tu campaña]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign) o continúa configurando [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)
- [Segmenta usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) y configura [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)
- [Envía mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=whatsapp)
- Consulta los [informes de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/reporting)