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

> El creador de plantillas de WhatsApp te permite crear y enviar plantillas de mensajes de WhatsApp directamente en Braze, sin necesidad de alternar entre Braze y Meta Business Manager. Una vez que Meta apruebe tu plantilla, úsala en tantas Campaigns y Canvas como quieras.

## Requisitos previos {#prerequisites}

{% multi_lang_include whatsapp/template_prerequisites.md %}

## Crear una plantilla {#create-a-template}

### Paso 1: Ve a las plantillas de WhatsApp {#step-1-go-to-whatsapp-templates}

Ve a **Contenido** > **WhatsApp** y selecciona **Crear nueva plantilla**.

![Página de plantillas de WhatsApp con botón para crear una nueva plantilla.]({% image_buster /assets/img/whatsapp/templates/create_whatsapp_template.png %})

### Paso 2: Configura los ajustes de la plantilla {#step-2-configure-template-settings}

Completa los siguientes campos:

| Campo | Descripción |
| ----- | ----- |
| **Cuenta** | La cuenta de WhatsApp Business (WABA) a la que deseas enviar la plantilla. Todos los grupos de suscripción y números de teléfono dentro de una WABA compartirán el acceso a la plantilla. |
| **Idioma** | El idioma de esta plantilla. WhatsApp requiere una plantilla separada para cada idioma. |
| **Nombre de la plantilla** | Un nombre único para tu plantilla. Los nombres de plantilla solo pueden contener letras minúsculas, números y guiones bajos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Configura los ajustes de la plantilla" }

### Paso 3: Elige un diseño {#step-3-choose-a-layout}

En **Diseño**, selecciona el tipo de plantilla:

- **Predeterminado:** Un mensaje estándar de WhatsApp. Este es el diseño que se cubre en este artículo.
- **Carrusel:** Un mensaje con tarjetas desplazables horizontalmente. Para más información, consulta [Plantillas de carrusel]({{site.baseurl}}/whatsapp_carousel_templates).

### Paso 4: Construye tu plantilla {#step-4-build-your-template}

#### Encabezado (opcional) {#header-optional}

Añade un encabezado que aparezca antes del cuerpo del mensaje. Puedes elegir:

- **Texto:** Un encabezado de texto corto.
- **Multimedia:** Una imagen, video o documento (solo URL). Braze almacena la referencia multimedia y envía una muestra a Meta para su aprobación.
- **Ninguno:** Sin encabezado

#### Cuerpo {#body}

Introduce el contenido principal de tu mensaje y personaliza el cuerpo según sea necesario usando Liquid o variables genéricas:

{% raw %}
- Usa etiquetas de Liquid (por ejemplo, `{{${first_name}}}`). Braze guarda tu Liquid y lo muestra cuando usas la plantilla en el creador de mensajes de una Campaign o Canvas.
- Usa variables genéricas, como marcadores de posición numerados (por ejemplo, `{{1}}`), si prefieres añadir la personalización más adelante al construir tu mensaje.
{% endraw %}

Puedes añadir personalización donde aparezca el botón **+** (más). No todos los campos admiten personalización.

#### Pie de página (opcional) {#footer-optional}

Añade un pie de página corto que aparezca después del cuerpo del mensaje.

#### Botones (opcional) {#buttons-optional}

Añade hasta 10 botones a tu plantilla. Los tipos de botones tienen diferentes categorías y especificaciones.

| Tipo de botón | Categoría | Especificaciones |
| --- | --- | --- |
| Respuesta rápida | Botones de respuesta rápida |{::nomarkdown}<ul><li><b>Cantidad máxima:</b> 10</li><li><b>Texto del botón:</b> Hasta 25 caracteres</li></ul> {:/}|
| Número de teléfono | Botones de llamada a la acción | {::nomarkdown}<ul><li><b>Cantidad máxima:</b> 1</li><li><b>Texto del botón:</b> Hasta 25 caracteres</li><li><b>Número de teléfono:</b> Número de teléfono válido con código de país, sin + (como "14155552671")</li></ul> {:/}|
| Visitar sitio web | Botones de llamada a la acción | {::nomarkdown}<ul><li><b>Cantidad máxima:</b> 2</li><li><b>Texto del botón:</b> Hasta 25 caracteres</li><li><b>URL del sitio web:</b> Hasta 2000 caracteres</li></ul> {:/}|
| Copiar código de oferta | Botones de llamada a la acción | {::nomarkdown}<ul><li><b>Cantidad máxima:</b> 1</li><li><b>Texto del botón:</b> "Copy offer code" (no se puede editar)</li><li><b>Código de oferta:</b> Hasta 15 caracteres</li></ul> {:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Botones (opcional)" }

![Creador de plantillas de WhatsApp con botones de respuesta rápida y llamada a la acción.]({% image_buster /assets/img/whatsapp/templates/buttons.png %})

### Paso 5: Previsualiza tu plantilla {#step-5-preview-your-template}

Antes de enviar, previsualiza cómo aparecerá tu mensaje para los destinatarios:

- **Vista previa como usuario:** Ve una vista previa genérica del mensaje.
- **Vista previa como un usuario específico:** Selecciona un perfil de usuario para previsualizar cómo se renderizará la plantilla con los datos de ese usuario.

### Paso 6: Envía para revisión {#step-6-submit-for-review}

Selecciona **Enviar** para enviar tu plantilla a Meta para su revisión, lo que normalmente tarda unos minutos pero puede tardar hasta 24 horas. La plantilla aparece en tu página de **Plantillas de WhatsApp** cuando se envía, y el estado se actualiza cuando actualizas la página de **Plantillas de WhatsApp**.

## Categorías de plantillas compatibles {#supported-template-categories}

Actualmente, solo las plantillas de marketing son compatibles con el creador de plantillas de WhatsApp.

## Usar una plantilla aprobada en una campaña {#use-an-approved-template-in-a-campaign}

Una vez que Meta apruebe tu plantilla, puedes usarla en una Campaign o Canvas de WhatsApp.

1. Ve a **Campaigns** y selecciona **Create Campaign** > **WhatsApp**.
2. En el creador de mensajes, selecciona tu plantilla aprobada.
3. Braze completa automáticamente el contenido de la plantilla, incluidos los multimedia y Liquid que ingresaste durante la creación de la plantilla, para que no tengas que volver a introducirlos.
4. Actualiza cualquier contenido variable o personalización según sea necesario. Los campos bloqueados por Meta (mostrados en gris) no se pueden editar. Para cambiar contenido bloqueado, debes editar y volver a enviar la plantilla para su aprobación.
5. Usa la pestaña **Test** para previsualizar el mensaje, actualizar las variables del cuerpo y confirmar que el mensaje se ve como se espera antes del lanzamiento.

Para más información sobre cómo crear Campaigns de WhatsApp, consulta [Crear un mensaje de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuánto tarda la revisión de plantillas de Meta? {#how-long-does-meta-template-review-take}

Las revisiones normalmente se completan en cinco minutos, pero pueden tardar hasta 24 horas.

### ¿Puedo editar una plantilla después de que ha sido aprobada? {#can-i-edit-a-template-after-its-been-approved}

Cualquier cambio en el contenido bloqueado (texto del cuerpo u otros campos controlados por Meta) requiere volver a enviar la plantilla para su aprobación, lo cual debe hacerse desde WhatsApp Business Manager. Puedes actualizar el contenido y la personalización al construir tu Campaign o Canvas.

### ¿Qué pasa con las plantillas que envié antes de que el creador de plantillas estuviera disponible? {#what-happens-to-templates-i-submitted-before-the-template-builder-was-available}

Las plantillas creadas en Meta Business Manager siguen disponibles para usar en Braze. El creador de plantillas es una forma adicional de crear y administrar plantillas sin salir del panel de Braze.

### ¿Por qué no puedo añadir personalización a todos los campos? {#why-cant-i-add-personalization-to-every-field}

Meta restringe qué partes de una plantilla se pueden personalizar. El botón **+** (más) solo aparece en los campos que admiten contenido variable.