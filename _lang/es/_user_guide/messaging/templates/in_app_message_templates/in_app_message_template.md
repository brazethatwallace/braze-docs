---
nav_title: Crear una plantilla de mensaje dentro de la aplicación
article_title: Crear una plantilla de mensaje dentro de la aplicación
page_order: 0
description: "Este artículo de referencia explica cómo crear, guardar y administrar plantillas de mensajes dentro de la aplicación desde la sección Contenido del panel de Braze, incluidos los perfiles de color y las plantillas CSS para el editor tradicional."
tool:
  - Templates
channel:
  - in-app messages
search_rank: 1
---

# Crear una plantilla de mensaje dentro de la aplicación {#create-an-in-app-message-template}

> Usa **Contenido** > **Mensaje dentro de la aplicación** para crear una biblioteca reutilizable de diseños de mensajes dentro de la aplicación y en el explorador. Puedes guardar diseños del editor de arrastrar y soltar o crear activos de **Perfil de color** y **Plantilla CSS** para el [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).

## Paso 1: Abre las plantillas de mensajes dentro de la aplicación {#step-1-open-in-app-message-templates}

En el panel de Braze, ve a **Contenido** > **Mensaje dentro de la aplicación**.

## Paso 2: Elige cómo crear una plantilla {#step-2-choose-how-to-create-a-template}

La forma de añadir una plantilla depende de tu objetivo:

| Objetivo | Qué hacer |
|----------|-----------|
| Guardar un diseño de arrastrar y soltar para reutilizarlo | En el [creador de mensajes dentro de la aplicación de arrastrar y soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop), selecciona **Guardar como plantilla** después de salir del editor (primero debes lanzar la campaña O guardarla como borrador). La plantilla aparecerá en **Plantillas** > **Plantillas de mensajes dentro de la aplicación** para tu próximo mensaje. |
| Crear un perfil de color o una plantilla CSS (editor tradicional) | En la página **Plantillas de mensajes dentro de la aplicación**, selecciona **+ Crear** y luego elige **Perfil de color** o **Plantilla CSS**. Para más detalles, consulta [Perfiles de color y plantillas CSS](#reusable-color-profiles). |
| Personalizar una plantilla de Braze | [Crea un mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) en el editor de arrastrar y soltar, elige una plantilla de Braze, realiza tus personalizaciones y selecciona **Guardar como plantilla**. Para descripciones de cada plantilla de Braze, consulta [Plantillas de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Elige cómo crear una plantilla" }

{% alert note %}
Los perfiles de color y las plantillas CSS se aplican al editor tradicional. Si usas el editor de arrastrar y soltar, utiliza la [Configuración de estilo]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings) para el estilo a nivel de mensaje.
{% endalert %}

## Paso 3: Administra tus plantillas {#step-3-manage-your-templates}

En **Contenido** > **Mensaje dentro de la aplicación**, filtra, busca o abre una plantilla para editarla. Puedes [duplicar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#duplicating-templates) y [archivar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#archiving-templates) plantillas como cualquier otro tipo de plantilla. Para un resumen de los flujos de trabajo de plantillas y medios, consulta [Plantillas]({{site.baseurl}}/user_guide/messaging/templates).

Para acceder a las plantillas de mensajes dentro de la aplicación, necesitas [permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para ver o editar plantillas de mensajes dentro de la aplicación.

### Crear perfiles de color y plantillas CSS {#reusable-color-profiles}

{% alert note %}
Las siguientes opciones se aplican al [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional). Si usas el editor de arrastrar y soltar, utiliza la [Configuración de estilo]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings) en su lugar.
{% endalert %}

Puedes editar plantillas existentes o seleccionar **+ Crear** y elegir **Perfil de color** o **Plantilla CSS** para crear nuevas plantillas para tus mensajes dentro de la aplicación.

#### Perfil de color {#color-profile}

Puedes personalizar la combinación de colores de tu plantilla de mensaje introduciendo un código de color HEX o seleccionando el cuadro de color y eligiendo un color con el SELECTOR de colores. Si quieres que este perfil se aplique de forma predeterminada cuando crees nuevos mensajes dentro de la aplicación en el editor tradicional, selecciona **Usar como perfil predeterminado**.

Selecciona **Guardar perfil de color** cuando hayas terminado.

![El editor de plantillas de perfil de color para mensajes dentro de la aplicación.]({% image_buster /assets/img/drag_and_drop/templates/color_profile_template.png %})

#### Plantilla CSS {#in-app-message-templates}

Puedes personalizar una plantilla CSS completa para tu [mensaje dentro de la aplicación de tipo modal web](#web-modal-css).

Nombra y etiqueta tu plantilla CSS, luego elige si será tu plantilla predeterminada. Puedes escribir tu propio CSS en el espacio proporcionado. Este espacio ya está rellenado con el CSS que se muestra en la vista previa de tu mensaje, y puedes ajustarlo según tus necesidades.

```css
.ab-message-header, .ab-message-text {
  color: #333333;
  text-align: center;
}

.ab-message-header {
  font-size: 20px;
  font-weight: bold;
}

.ab-message-text {
  font-size: 14px;
  font-weight: normal;
}

.ab-close-button svg {
  fill: #9b9b9b;
}

.ab-message-button {
  border: 1px solid #1b78cf;
  font-size: 14px;
  font-weight: bold;
}
.ab-message-button:first-of-type {
  background-color: white;
  color: #1b78cf;
}
.ab-message-button:last-of-type, .ab-message-button:first-of-type:last-of-type {
  background-color: #1b78cf;
  color: white;
}

.ab-background {
  background-color: white;
}

.ab-icon {
  background-color: #0073d5;
  color: white;
}

.ab-page-blocker {
  background-color: rgba(51, 51, 51, .75);
}
```

Puedes editar todo, desde el color de fondo hasta el tamaño y peso de la fuente, y más.

#### Modal con CSS (solo web) {#web-modal-css}

Si eliges usar un mensaje de tipo modal web solo para web con CSS, puedes aplicar tu propia plantilla o escribir tu propio CSS en el espacio proporcionado. Este espacio ya está rellenado con el CSS que se muestra en la vista previa de tu mensaje, pero puedes ajustarlo según tus necesidades.

Si eliges aplicar tu propia plantilla, selecciona **Aplicar plantilla** y elige de la galería de plantillas de mensajes dentro de la aplicación. Si no tienes ninguna opción, puedes añadir una [plantilla CSS](#in-app-message-templates) usando el constructor de plantillas CSS en **Plantillas** > **Plantillas de mensajes dentro de la aplicación**.