---
nav_title: Formulario de registro de servicio de mensajes cortos, RCS y WhatsApp
article_title: Formulario de registro de servicio de mensajes cortos, RCS y WhatsApp
alias: "/phone_number_capture/"
page_order: 2
description: "Esta página explica cómo crear un formulario de registro de servicio de mensajes cortos, RCS y WhatsApp con el editor de arrastrar y soltar de mensajes dentro de la aplicación."
---

# Formulario de registro de servicio de mensajes cortos, RCS y WhatsApp {#sms-rcs-and-whatsapp-sign-up-form}

> Los formularios de registro de servicio de mensajes cortos, RCS y WhatsApp son plantillas disponibles en el editor de arrastrar y soltar para mensajes dentro de la aplicación. Usa estas plantillas para recopilar los números de teléfono de los usuarios y hacer crecer tus grupos de suscripción de servicio de mensajes cortos, MMS, RCS y WhatsApp.

![Tres ejemplos de mensajes dentro de la aplicación creados con la plantilla de formulario de registro telefónico.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %})

{% multi_lang_include drag_and_drop/templates.md section='SDK or kit de desarrollo de software requirements' %}

## Crear un formulario de registro de número de teléfono {#creating-a-phone-number-sign-up-form}

### Paso 1: Elige tu plantilla {#step-1-choose-your-template}

Al crear un mensaje dentro de la aplicación de arrastrar y soltar, selecciona **servicio de mensajes cortos sign-up** (esto también sirve para el registro de RCS) o **WhatsApp sign-up** como plantilla, y luego selecciona **Build message**. Estas plantillas son compatibles tanto con aplicaciones móviles como con navegadores web.

![Modal para seleccionar servicio de mensajes cortos sign-up o WhatsApp sign-up como plantilla al crear un mensaje dentro de la aplicación.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}){: style="max-width:80%"}

### Paso 2: Configura los estilos de tu mensaje {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

![Flujo de trabajo para cargar y seleccionar una fuente personalizada.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %})

### Paso 3: Personaliza el componente de entrada de número de teléfono {#step-3-customize-your-phone-number-input-component}

Para empezar a crear tu formulario de registro, selecciona el componente de entrada de número de teléfono en el editor.

![Área de vista previa al crear un formulario de registro con el componente de entrada de número de teléfono seleccionado.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%"}

Desde el menú lateral, especifica para qué grupo de suscripción esta plantilla recopilará números de teléfono. Para cumplir con las mejores prácticas de conformidad, solo puedes recopilar el consentimiento para un grupo de suscripción por formulario de registro de número de teléfono. Sin embargo, si lo deseas, puedes usar múltiples formularios para recopilar el consentimiento para otros grupos de suscripción.

![Desplegable de grupo de suscripción con un grupo de suscripción seleccionado.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}){: style="max-width:40%"}

De forma predeterminada, recopilamos números a nivel global; sin embargo, puedes limitar la cantidad de países de los que se recopilan números. Esto es útil si solo pretendes enviar mensajes a usuarios que tienen números de teléfono en países específicos, y puede ayudar con la limpieza de listas. Para hacerlo, desactiva **Collect numbers from all countries** y usa el desplegable para seleccionar países específicos. Tus usuarios solo podrán seleccionar los países que hayas añadido explícitamente.

![Desplegable de países para seleccionar los países de los que deseas recopilar números.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}){: style="max-width:40%"}

#### Números de teléfono no válidos {#invalid-phone-numbers}

Si tus usuarios introducen un número de teléfono que incluye caracteres especiales no aceptados, verán un indicador de error genérico que no es personalizable y no podrán enviar el formulario. Puedes ver el comportamiento del error en la pestaña **vista previa & Test** y en tu dispositivo de prueba. Consulta este artículo para saber [cómo Braze formatea los números de teléfono]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#import-phone-numbers).

### Paso 4: Añade el texto de exención de responsabilidad (para formularios de registro de servicio de mensajes cortos y RCS) {#step-4-add-disclaimer-language-for-sms-and-rcs-sign-up-forms}

Para los formularios de registro de servicio de mensajes cortos y RCS, es importante comunicar claramente el tipo de servicio de mensajes cortos o RCS que enviarás. Asegúrate de que el crecimiento de tu lista sea conforme incluyendo la siguiente información en tu formulario:

- Descripción de los tipos de mensajes servicio de mensajes cortos y RCS que tus clientes pueden esperar (recordatorios de carrito, promociones y ofertas, recordatorios de citas, etc.). No necesitas enumerar cada caso de uso, pero debes proporcionar una descripción de los tipos de mensajes que tu marca enviará.
- Nota de que el consentimiento no es una condición de ninguna compra (si aplica).
- Frecuencia de mensajes y recordatorio de que se aplican tarifas de mensajes y datos. Si no conoces la frecuencia exacta de mensajes, puedes indicar que la frecuencia puede variar.
- Enlaces a tus términos y condiciones y a la política de privacidad de servicio de mensajes cortos y RCS.
- Recordatorio de las palabras clave de ayuda y cancelación (HELP para ayuda; STOP para cancelar).

Hemos proporcionado un texto de exención de responsabilidad como marcador de posición en la plantilla únicamente a modo de ejemplo; no constituye asesoramiento legal y no debe utilizarse con fines de cumplimiento. Es importante trabajar con tu equipo legal para desarrollar un texto adaptado a tu marca específica.

{% alert note %}
Esta documentación no pretende proporcionar, ni se puede confiar plenamente en ella como fuente de asesoramiento legal.
{% endalert %}

Para más información sobre el cumplimiento de servicio de mensajes cortos y RCS, consulta [Leyes y regulaciones para servicio de mensajes cortos, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).

### Paso 5: Dale estilo a tu mensaje {#step-5-style-your-message}

Personaliza la apariencia de tu mensaje usando los [componentes de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#message-components) de arrastrar y soltar.

## Análisis de los resultados {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

![Panel de rendimiento de mensajes dentro de la aplicación que muestra los clics de cada enlace en el mensaje dentro de la aplicación.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %})