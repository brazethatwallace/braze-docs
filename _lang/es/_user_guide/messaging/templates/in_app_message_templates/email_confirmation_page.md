---
nav_title: Registro de correo electrónico con confirmación
article_title: Registro de correo electrónico con página de confirmación
alias: "/email_confirmation_page/"
page_order: 7
description: "Esta página explica cómo usar el editor de arrastrar y soltar de mensajes dentro de la aplicación para crear un formulario de registro de correo electrónico que tiene una página de confirmación."
---

# Registro de correo electrónico con página de confirmación {#email-sign-up-with-confirmation-page}

> Usa el editor de arrastrar y soltar de mensajes dentro de la aplicación para crear un formulario de registro de correo electrónico con una página de confirmación.

{% multi_lang_include drag_and_drop/templates.md section='SDK or kit de desarrollo de software requirements' %}

## Creando un formulario de registro de correo electrónico con una página de confirmación {#creating-an-email-sign-up-form-with-a-confirmation-page}

### Paso 1: Elige tu plantilla {#step-1-choose-your-template}

Al crear un mensaje dentro de la aplicación de arrastrar y soltar, selecciona **Registro de correo electrónico con página de confirmación** como tu plantilla y luego selecciona **Build message**. Esta plantilla es compatible tanto con aplicaciones móviles como con navegadores web.

![El editor de mensajes dentro de la aplicación con la plantilla para un formulario de registro de correo electrónico con página de confirmación.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_confirmation.png %})

### Paso 2: Configura los estilos de tu mensaje {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Paso 3: Personaliza tu componente de registro de correo electrónico {#step-3-customize-your-email-sign-up-component}

Para empezar a crear tu formulario de registro de correo electrónico, selecciona el elemento de captura de correo electrónico en el editor. De forma predeterminada, las direcciones de correo electrónico recopiladas tendrán el grupo de suscripción global **Suscrito**. Para incluir usuarios en grupos de suscripción específicos, consulta [Actualización de los estados de suscripción de correo electrónico]({{site.baseurl}}/user_guide/channels/email/subscriptions#updating-email-subscription-states).

Puedes personalizar el texto del marcador de posición y el texto de la etiqueta del elemento de captura de correo electrónico.

![El editor de mensajes dentro de la aplicación con un menú lateral para personalizar el elemento de captura de correo electrónico.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field_confirmation.png %})

#### Validación de correo electrónico {#email-validation}

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### Paso 4: Agrega un texto de exención de responsabilidad (opcional) {#step-4-add-disclaimer-language-optional}

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Paso 5: Dale estilo a tu mensaje {#step-5-style-your-message}

Personaliza la apariencia de tu formulario de registro de correo electrónico y de la página de confirmación usando los [componentes de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#message-components) de arrastrar y soltar.

## Análisis de los resultados {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Mejores prácticas {#best-practices}

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}