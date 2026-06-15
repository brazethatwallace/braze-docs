---
nav_title: Registro de correo electrónico con oferta
article_title: Registro de correo electrónico con oferta especial
alias: "/email_offer/"
page_order: 6
description: "Esta página explica cómo usar el editor de arrastrar y soltar de mensajes dentro de la aplicación para crear tu lista de correo electrónico ofreciendo un descuento especial en el registro."
---

# Registro de correo electrónico con oferta especial {#email-sign-up-with-special-offer}

> Usa el editor de arrastrar y soltar de mensajes dentro de la aplicación para crear tu lista de correo electrónico ofreciendo un descuento especial en el registro.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Creando un formulario de registro de correo electrónico con una oferta especial {#creating-an-email-sign-up-form-with-a-special-offer}

### Paso 1: Elige tu plantilla {#step-1-choose-your-template}

Al crear un mensaje dentro de la aplicación de arrastrar y soltar, selecciona **Email sign-up with special offer** como tu plantilla y luego selecciona **Build message**. Esta plantilla es compatible tanto con aplicaciones móviles como con navegadores web.

![El editor de mensajes dentro de la aplicación con la plantilla para un formulario de registro de correo electrónico con una oferta especial.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_offer.png %})

### Paso 2: Configura los estilos de tu mensaje {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Paso 3: Personaliza tu componente de registro de correo electrónico {#step-3-customize-your-email-sign-up-component}

Para empezar a crear tu formulario de registro de correo electrónico, selecciona la página **Email sign-up** y luego selecciona el elemento de captura de correo electrónico en el editor. De forma predeterminada, las direcciones de correo electrónico recopiladas tendrán el grupo de suscripción global **Suscrito**. Para dar de alta a usuarios en grupos de suscripción específicos, consulta [Actualización de los estados de suscripción de correo electrónico]({{site.baseurl}}/user_guide/channels/email/subscriptions/#updating-email-subscription-states).

Puedes personalizar el texto del marcador de posición y el texto de la etiqueta del elemento de captura de correo electrónico.

![El editor de mensajes dentro de la aplicación con un menú lateral para personalizar el elemento de captura de correo electrónico.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field_offer.png %})

#### Validación de correo electrónico {#email-validation}

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### Paso 4: Añade un texto de exención de responsabilidad (opcional) {#step-4-add-disclaimer-language-optional}

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Paso 5: Dale estilo a tu mensaje {#step-5-style-your-message}

Personaliza la apariencia de tu oferta especial usando los [componentes de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/#message-components) de arrastrar y soltar.

## Análisis de los resultados {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Mejores prácticas {#best-practices}

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}