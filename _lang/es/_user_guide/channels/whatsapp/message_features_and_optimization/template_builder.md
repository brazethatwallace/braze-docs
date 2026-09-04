---
nav_title: Creador de plantillas de WhatsApp
article_title: Creador de plantillas de WhatsApp
description: "Aprende a crear, configurar y enviar plantillas de mensajes de WhatsApp directamente en Braze usando el creador de plantillas de WhatsApp."
alias: /whatsapp_template_builder/
page_type: reference
channel:
  - WhatsApp
---

# Creador de plantillas de WhatsApp {#whatsapp-template-builder}

> El creador de plantillas de WhatsApp te permite crear y enviar plantillas de mensajes de WhatsApp directamente en Braze, sin necesidad de alternar entre Braze y Meta Business Administrador. Una vez que Meta apruebe tu plantilla, úsala en tantas Campaigns y Canvas como quieras.

## Requisitos previos {#prerequisites}

{% multi_lang_include whatsapp/template_prerequisites.md %}

## Crear una plantilla {#create-a-template}

### Paso 1: Ir a las plantillas de WhatsApp {#step-1-go-to-whatsapp-templates}

Ve a **Contenido** > **Plantillas** > **WhatsApp** y selecciona **Crear nueva plantilla**.

![Página de plantillas de WhatsApp con un botón para crear una nueva plantilla.]({% image_buster /assets/img/whatsapp/templates/create_whatsapp_template.png %})

También puedes crear una plantilla mientras compones una Campaign o un Canvas de WhatsApp. Para más información, consulta [Crear una plantilla desde una Campaign o un Canvas](#create-a-template-from-a-campaign-or-canvas).

### Paso 2: Elegir una categoría y un tipo {#step-2-choose-a-category-and-type}

Selecciona una categoría de plantilla y un tipo de plantilla, y luego selecciona **Continuar a la plantilla** cuando estés listo.

{% alert note %}
Meta revisa las plantillas según las [directrices de categoría](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization) y el contenido.
{% endalert %}

#### Marketing {#marketing}

Las plantillas de marketing son para mensajes promocionales y de participación (por ejemplo, mensajes de bienvenida, promociones, ofertas, cupones, boletines y anuncios).

| Tipo | Descripción |
| --- | --- |
| **Personalizado** | Un mensaje de WhatsApp estándar que construyes desde cero. Este es el diseño cubierto en [Construir tu plantilla](#step-4-build-your-template). |
| **Carrusel** | Un mensaje con tarjetas desplazables horizontalmente. Para más información, consulta [Plantillas de carrusel]({{site.baseurl}}/whatsapp_carousel_templates). |
| **Oferta por tiempo limitado** | Una oferta promocional con tiempo limitado. Para más información, consulta [Plantillas de oferta por tiempo limitado]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/message_and_image_formats#limited-time-offer-templates). |
| **Flujo** | Una plantilla que abre un flujo de WhatsApp (por ejemplo, cuestionarios o reservas de citas). Crea y administra el flujo en el WhatsApp Administrador de Meta, y luego selecciónalo cuando construyas la plantilla. Para más información, consulta [Flujos de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/whatsapp_flows). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de plantillas de marketing" }

#### Utilidad {#utility}

Las plantillas de utilidad son para mensajes no promocionales (por ejemplo, confirmaciones de pedidos, actualizaciones de cuenta, recibos, recordatorios de citas y facturación). Meta reclasifica el contenido promocional como marketing.

| Tipo | Descripción |
| --- | --- |
| **Personalizado** | Un mensaje de utilidad estándar que construyes desde cero. Sigue los mismos pasos de composición que en [Construir tu plantilla](#step-4-build-your-template). |
| **Flujo** | Una plantilla de flujo de utilidad (por ejemplo, recordatorios, comentarios o gestión de pedidos). Crea y administra el flujo en el WhatsApp Administrador de Meta, y luego selecciónalo cuando construyas la plantilla. Para más información, consulta [Flujos de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/whatsapp_flows). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de plantillas de utilidad" }

{% alert note %}
Los diseños de carrusel y oferta por tiempo limitado solo están disponibles para las plantillas de marketing.
{% endalert %}

### Paso 3: Configurar los ajustes de la plantilla {#step-3-configure-template-settings}

Completa los siguientes campos:

| Campo | Descripción |
| ----- | ----- |
| **Cuenta** | La cuenta de WhatsApp Business (WABA) a la que deseas enviar la plantilla. Todos los grupos de suscripción y números de teléfono dentro de una WABA comparten el acceso a las plantillas. |
| **Idioma** | El idioma de esta plantilla. WhatsApp requiere una plantilla separada para cada idioma. |
| **Nombre de la plantilla** | Un nombre único para tu plantilla. Los nombres de plantilla solo pueden contener letras minúsculas, números y guiones bajos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 3: Configurar los ajustes de la plantilla" }

### Paso 4: Construir tu plantilla {#step-4-build-your-template}

#### Encabezado (opcional) {#header-optional}

Agrega un encabezado para que aparezca antes del cuerpo del mensaje. Puedes elegir:

- **Texto:** Un encabezado de texto corto.
- **Multimedia:** Una imagen, video o documento (solo URL). Braze almacena la referencia multimedia y envía una muestra a Meta para su aprobación.
- **Ninguno:** Sin encabezado

#### Cuerpo {#body}

Introduce el contenido principal de tu mensaje y personaliza el cuerpo según sea necesario usando Liquid o variables genéricas:

{% raw %}
- Usa etiquetas de Liquid (por ejemplo, `{{${first_name}}}`). Braze guarda tu Liquid y lo muestra cuando usas la plantilla en el creador de una Campaign o un Canvas.
- Usa variables genéricas, como marcadores de posición numerados (por ejemplo, `{{1}}`), si prefieres agregar personalización más adelante al construir tu mensaje.
{% endraw %}

Puedes agregar personalización donde aparezca el botón **+** más. No todos los campos admiten personalización.

#### Límites de caracteres de Liquid {#liquid-character-limits}

Meta aplica límites de caracteres a la estructura de plantilla que envías para aprobación (por ejemplo, 1024 caracteres para el cuerpo y 60 caracteres para un encabezado de texto). En el constructor de plantillas, estos límites se aplican a la plantilla enviada a Meta, no al mensaje final renderizado en el momento del envío.

- **Variables {% raw %}`{{ }}`{% endraw %}:** Braze convierte las variables de Liquid en marcadores de posición numerados ({% raw %}`{{1}}`, `{{2}}`{% endraw %}) antes de verificar la longitud. Una expresión larga como {% raw %}`{{${first_name}}}`{% endraw %} cuenta como un marcador de posición corto, no como la sintaxis completa de Liquid.
- **Etiquetas {% raw %}`{% %}`{% endraw %}:** Las etiquetas de lógica de Liquid cuentan como texto literal en toda su longitud y aparecen como texto no editable en los mensajes de plantilla.

Para personalización compleja, usa un [paso de contexto]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) para calcular valores, y luego haz referencia a variables más cortas en la plantilla. Para las restricciones de Message Extras y lógica condicional, consulta [Liquid en el constructor de plantillas de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder/template_builder_liquid).

#### Pie de página (opcional) {#footer-optional}

Agrega un pie de página corto para que aparezca después del cuerpo del mensaje.

#### Botones (opcional) {#buttons-optional}

Agrega hasta 10 botones a tu plantilla. Los tipos de botones tienen diferentes categorías y especificaciones, y se agrupan por categoría después del cuerpo del mensaje. De forma predeterminada, los botones de respuesta rápida aparecen primero. Para cambiar el orden en que aparecen, como mover los botones de respuesta rápida después de los botones de llamada a la acción, selecciona **Cambiar orden de grupo**.

| Tipo de botón | Categoría | Especificaciones |
| --- | --- | --- |
| Respuesta rápida | Botones de respuesta rápida |{::nomarkdown}<ul><li><b>Cantidad máxima:</b> 10</li><li><b>Texto del botón:</b> Hasta 25 caracteres</li></ul> {:/}|
| Número de teléfono | Botones de llamada a la acción | {::nomarkdown}<ul><li><b>Cantidad máxima:</b> 1</li><li><b>Texto del botón:</b> Hasta 25 caracteres</li><li><b>Número de teléfono:</b> Número de teléfono válido con código de país, sin + (como "14155552671")</li></ul> {:/}|
| Visitar sitio web | Botones de llamada a la acción | {::nomarkdown}<ul><li><b>Cantidad máxima:</b> 2</li><li><b>Texto del botón:</b> Hasta 25 caracteres</li><li><b>URL del sitio web:</b> Hasta 2000 caracteres</li></ul> {:/}|
| Copiar código de oferta | Botones de llamada a la acción | {::nomarkdown}<ul><li><b>Cantidad máxima:</b> 1</li><li><b>Texto del botón:</b> "Copy offer code" (no se puede editar)</li><li><b>Código de oferta:</b> Hasta 15 caracteres</li></ul> {:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Botones (opcional)" }

Para las plantillas de flujo, configura el botón de flujo y selecciona un flujo existente de Meta en lugar de agregar botones estándar de llamada a la acción.

### Paso 5: Previsualizar tu plantilla {#step-5-preview-your-template}

Antes de enviar, previsualiza cómo aparece tu mensaje para los destinatarios:

- **Previsualizar como usuario:** Ve una vista previa genérica del mensaje.
- **Previsualizar como un usuario específico:** Selecciona un perfil de usuario para previsualizar cómo se renderiza la plantilla con los datos de ese usuario.

### Paso 6: Enviar para revisión {#step-6-submit-for-review}

Selecciona **Enviar** para enviar tu plantilla a Meta para revisión, lo que generalmente toma unos minutos pero puede tardar hasta 24 horas. La plantilla aparece en tu página de **plantillas de WhatsApp** cuando se envía, y el estado se actualiza cuando actualizas la página de **plantillas de WhatsApp**.

## Crear una plantilla desde una campaña o Canvas {#create-a-template-from-a-campaign-or-canvas}

Puedes crear y enviar una plantilla de WhatsApp sin salir de una campaña o un paso de mensaje de Canvas.

1. En una [campaña]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message) de WhatsApp o un paso de mensaje de Canvas, selecciona el tipo de mensaje **WhatsApp Template Message**.
2. Selecciona **Crear nueva plantilla**.
3. Elige una categoría y un tipo, luego crea y envía la plantilla de la misma forma que lo harías en la página de plantillas de WhatsApp.
4. Después de enviarla, Braze vincula la plantilla pendiente al mensaje. Continúa redactando la personalización mientras la plantilla está pendiente y luego lánzala después de que Meta la apruebe.

Selecciona **Elegir plantilla de la biblioteca** para salir del constructor y elegir una plantilla existente.

{% alert note %}
Cuando creas una plantilla desde una campaña o Canvas, Braze puede guardar tu trabajo como borrador para que se conserve si sales del paso de mensaje.
{% endalert %}

## Usar una plantilla aprobada en una Campaign {#use-an-approved-template-in-a-campaign}

Después de que Meta apruebe tu plantilla, puedes usarla en una Campaign de WhatsApp o en un Canvas.

1. Ve a **Campaigns** y selecciona **Crear Campaign** > **WhatsApp**.
2. En el creador de mensajes, selecciona tu plantilla aprobada.
3. Braze rellena automáticamente el contenido de la plantilla, incluidos los medios y el Liquid que introdujiste durante la creación de la plantilla, para que no tengas que volver a ingresarlo.
4. Actualiza cualquier contenido de variables o personalización según sea necesario. Los campos bloqueados por Meta (que se muestran en gris) no se pueden editar. Para cambiar contenido bloqueado, debes editar y volver a enviar la plantilla para su aprobación.
5. Usa la pestaña **Test** para previsualizar el mensaje, actualizar las variables del cuerpo y confirmar que el mensaje se ve como esperabas antes de lanzarlo.

Para más información sobre cómo crear Campaigns de WhatsApp, consulta [Crear un mensaje de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuánto tarda la revisión de plantillas de Meta? {#how-long-does-meta-template-review-take}

Las revisiones suelen completarse en cinco minutos, pero pueden tardar hasta 24 horas.

### ¿Puedo editar una plantilla después de que ha sido aprobada? {#can-i-edit-a-template-after-its-been-approved}

Puedes actualizar el contenido variable y la personalización al crear una Campaign o un Canvas. Los cambios en el contenido bloqueado (texto del cuerpo, disposición de botones u otros campos controlados por Meta) requieren crear una nueva plantilla en el constructor de plantillas o editar la plantilla en el WhatsApp Administrador de Meta y esperar la re-aprobación de Meta. Si usas [seguimiento de clics]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/click_tracking), consulta ese artículo antes de editar plantillas creadas en Braze en el WhatsApp Administrador de Meta.

### ¿Qué pasa con las plantillas que envié antes de que el constructor de plantillas estuviera disponible? {#what-happens-to-templates-i-submitted-before-the-template-builder-was-available}

Las plantillas creadas en Meta Business Administrador siguen disponibles para su uso en Braze. El constructor de plantillas es una forma adicional de crear y gestionar plantillas sin salir del panel de Braze.

### ¿Por qué no puedo añadir personalización a todos los campos? {#why-cant-i-add-personalization-to-every-field}

Meta restringe qué partes de una plantilla pueden personalizarse. El botón **+** solo aparece en los campos que admiten contenido variable.