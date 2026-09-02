---
nav_title: Formulario de registro de correo electrónico
article_title: Formulario de registro de correo electrónico
alias: "/email_capture/"
page_order: 3
description: "Esta página explica cómo crear un formulario de registro de correo electrónico con el editor de arrastrar y soltar de mensajes dentro de la aplicación."
---

# Formulario de registro de correo electrónico {#email-sign-up-form}

> Usa la plantilla de mensaje dentro de la aplicación de arrastrar y soltar para registro de correo electrónico para recopilar las direcciones de correo electrónico de los usuarios y hacer crecer tus grupos de suscripción.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Crear un formulario de registro de correo electrónico {#creating-an-email-sign-up-form}

### Paso 1: Elige tu plantilla {#step-1-choose-your-template}

Al crear un mensaje dentro de la aplicación de arrastrar y soltar, selecciona **Email sign-up** como plantilla y luego selecciona **Build message**. Esta plantilla es compatible tanto con aplicaciones móviles como con navegadores web.

![El editor de mensajes dentro de la aplicación con la plantilla para un formulario de captura de correo electrónico.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_template1.png %})

### Paso 2: Configura los estilos de tu mensaje {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Paso 3: Personaliza tu componente de registro de correo electrónico {#step-3-customize-your-email-sign-up-component}

Para empezar a crear tu formulario de registro de correo electrónico, selecciona el elemento de captura de correo electrónico en el editor. De forma predeterminada, las direcciones de correo electrónico recopiladas tendrán el grupo de suscripción global **Suscrito**. Para dar de alta a usuarios en grupos de suscripción específicos, consulta [Actualizar estados de suscripción de correo electrónico]({{site.baseurl}}/user_guide/channels/email/subscriptions#updating-email-subscription-states).

Puedes personalizar el texto del marcador de posición y el texto de la etiqueta del elemento de captura de correo electrónico.

![El editor de mensajes dentro de la aplicación con un menú lateral para personalizar el elemento de captura de correo electrónico.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field1.png %})

#### Validación de correo electrónico {#email-validation}

Si el usuario introduce una dirección de correo electrónico que incluye caracteres especiales no aceptados, verá un indicador de error genérico y no podrá enviar el formulario. Este mensaje de error no es personalizable. Puedes ver el comportamiento del error en la pestaña **vista previa & Test** y en tu dispositivo de prueba. Obtén más información sobre cómo Braze formatea las direcciones de correo electrónico en [Validación de correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation).

### Paso 4: Añade un texto de exención de responsabilidad (opcional) {#step-4-add-disclaimer-language-optional}

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Paso 5: Dale estilo a tu mensaje {#step-5-style-your-message}

Personaliza la apariencia de tu formulario de registro usando los [componentes de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#message-components) de arrastrar y soltar.

## Analizar los resultados {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Buenas prácticas {#best-practices}

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}