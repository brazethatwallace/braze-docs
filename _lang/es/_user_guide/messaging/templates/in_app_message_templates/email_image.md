---
nav_title: Registro de correo electrónico con imagen
article_title: Registro de correo electrónico con imagen de fondo
alias: "/email_image/"
page_order: 5
description: "Esta página explica cómo usar el editor de arrastrar y soltar de mensajes dentro de la aplicación para mostrar el estilo de tu marca con un mensaje sencillo y crear tu lista de correo electrónico."
---

# Registro de correo electrónico con imagen de fondo {#email-sign-up-with-background-image}

> Usa el editor de arrastrar y soltar de mensajes dentro de la aplicación para mostrar el estilo de tu marca con un mensaje sencillo y crear tu lista de correo electrónico.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Crear un formulario de registro de correo electrónico con una imagen de fondo {#creating-an-email-sign-up-form-with-a-background-image}

### Paso 1: Elige tu plantilla {#step-1-choose-your-template}

Al crear un mensaje dentro de la aplicación de arrastrar y soltar, selecciona **Email sign-up with background image** como plantilla y luego selecciona **Build message**. Esta plantilla es compatible tanto con aplicaciones móviles como con navegadores web.

![El editor de mensajes dentro de la aplicación con la plantilla para un formulario de registro de correo electrónico con una imagen de fondo.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_image.png %})

### Paso 2: Configura los estilos de tu mensaje {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Paso 3: Personaliza tu componente de registro de correo electrónico {#step-3-customize-your-email-sign-up-component}

Para empezar a crear tu formulario de registro de correo electrónico, selecciona el elemento de captura de correo electrónico en el editor. De forma predeterminada, las direcciones de correo electrónico recopiladas tendrán el grupo de suscripción global **Suscrito**. Para que los usuarios se adhieran a grupos de suscripción específicos, consulta [Actualizar los estados de suscripción de correo electrónico]({{site.baseurl}}/user_guide/channels/email/subscriptions/#updating-email-subscription-states).

Puedes personalizar el texto del marcador de posición y el texto de la etiqueta del elemento de captura de correo electrónico.

![El editor de mensajes dentro de la aplicación con un menú lateral para personalizar el elemento de captura de correo electrónico.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field_image.png %})

#### Validación de correo electrónico {#email-validation}

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### Paso 4: Añade un texto de exención de responsabilidad (opcional) {#step-4-add-disclaimer-language-optional}

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Paso 5: Dale estilo a tu mensaje {#step-5-style-your-message}

Personaliza la apariencia de tu formulario de registro usando los [componentes de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/#message-components) de arrastrar y soltar. Añade tu propia imagen de fondo reemplazando la URL de la imagen de fondo predeterminada en el menú **Message container** o elimina la URL y selecciona tu imagen desde la [Biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/).

## Análisis de los resultados {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Prácticas recomendadas {#best-practices}

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}