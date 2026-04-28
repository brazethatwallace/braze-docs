---
nav_title: Perfiles de color y plantillas CSS
article_title: Perfiles de color y plantillas CSS
page_order: 3
page_type: reference
description: "Este artículo ofrece un resumen de los perfiles de color y las plantillas CSS de los mensajes dentro de la aplicación."
channel:
  - in-app messages
---

# Perfiles de color y plantillas CSS {#reusable-color-profiles}

> Puedes guardar plantillas de mensajes dentro de la aplicación y mensajes en el explorador en el dashboard para crear rápidamente nuevas campañas y mensajes usando tu estilo. Este artículo aplica al [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/). Si estás usando el editor de arrastrar y soltar, consulta [Configuración de estilo]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/) en su lugar.

Ve a **Plantillas** > **Plantillas de mensajes dentro de la aplicación**.

Desde esta página, puedes editar plantillas existentes o hacer clic en **+ Crear** y elegir **Perfil de color** o **Plantilla CSS** para crear nuevas plantillas y usarlas en tus mensajes dentro de la aplicación.

## Perfil de color {#color-profile}

Puedes personalizar la combinación de colores de tu plantilla de mensaje ingresando un código de color HEX o haciendo clic en el cuadro de color y seleccionando un color con el selector de colores.

Haz clic en **Guardar perfil de color** cuando hayas terminado.

### Gestión de perfiles de color {#managing-color-profiles}

También puedes [duplicar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/) y [archivar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/) plantillas. Obtén más información sobre cómo crear y gestionar plantillas y contenido creativo en [Plantillas y medios]({{site.baseurl}}/user_guide/messaging/templates/).

## Plantilla CSS {#in-app-message-templates}

Puedes personalizar una plantilla CSS completa para tu [mensaje dentro de la aplicación de tipo modal web](#web-modal-css).

Nombra y etiqueta tu plantilla CSS, luego elige si será o no tu plantilla predeterminada. Puedes escribir tu propio CSS en el espacio proporcionado. Este espacio ya está prellenado con el CSS que se muestra en la vista previa de tu mensaje, y puedes ajustarlo libremente para que se adapte a tus necesidades.

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

Como puedes ver, puedes editar todo, desde el color de fondo hasta el tamaño y peso de la fuente, y mucho más.

### Gestión de plantillas CSS {#managing-css-templates}

También puedes [duplicar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/) y [archivar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/) plantillas. Obtén más información sobre cómo crear y gestionar plantillas y contenido creativo en [Plantillas y medios]({{site.baseurl}}/user_guide/messaging/templates/).

## Modal con CSS (solo web) {#web-modal-css}

Si eliges usar un mensaje de tipo modal web solo para web con CSS, puedes aplicar tu propia plantilla o escribir tu propio CSS en el espacio proporcionado. Este espacio ya está prellenado con el CSS que se muestra en la vista previa de tu mensaje, pero puedes ajustarlo libremente para que se adapte a tus necesidades.

Si eliges aplicar tu propia plantilla, haz clic en **Aplicar plantilla** y elige de la galería de plantillas de mensajes dentro de la aplicación. Si no tienes ninguna opción, puedes cargar una [plantilla CSS]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/color_profiles_and_css_templates/#in-app-message-templates) usando el constructor de plantillas CSS.