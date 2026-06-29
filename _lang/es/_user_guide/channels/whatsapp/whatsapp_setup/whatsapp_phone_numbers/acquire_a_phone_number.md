---
nav_title: "Adquirir un número"
article_title: "Adquirir un número de teléfono de WhatsApp"
page_order: 1
description: "Este artículo de referencia explica cómo adquirir un número de teléfono de Twilio e Infobip."
page_type: reference
channel:
  - WhatsApp
---

# Adquirir un número de teléfono de WhatsApp {#acquire-a-whatsapp-phone-number}

> Para usar el canal de mensajería de WhatsApp, necesitarás un número de teléfono que cumpla con los requisitos de WhatsApp para su [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) o [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers).

Debes adquirir tu número de teléfono por tu cuenta, ya que Braze no lo proporcionará por ti. Puedes comprar un teléfono físico con una tarjeta SIM a través de tu proveedor de telefonía empresarial o usar uno de nuestros socios: Twilio o Infobip. **Debes tener tu propia cuenta de Twilio o Infobip, ya que esto no se puede hacer a través de Braze.**

## Requisitos de la API de WhatsApp {#whatsapp-api-requirements}

Tu número de teléfono debe cumplir con estos requisitos de la API de WhatsApp:

- Ser propiedad de tu empresa
- Tener un código de país y de área (como los números fijos y móviles)
- Poder recibir llamadas de voz o SMS
- Ser accesible durante la configuración de la cuenta (para recibir códigos de verificación)
- No ser un código abreviado
- No haber sido utilizado previamente con la plataforma WhatsApp Business
- No estar conectado a una cuenta personal de WhatsApp

## Adquirir un número de teléfono de Twilio {#acquiring-a-twilio-phone-number}

### Paso 1: Comprar un número de teléfono desde la consola o API de Twilio {#step-1-buy-a-phone-number-from-the-twilio-console-or-api}

1. Desde la consola de Twilio, ve a **Develop** > **Phone Numbers** > **Manage** > **Buy a number**. Si no ves esta opción, selecciona **Explore Products**, desplázate hasta **Super Networks** y luego selecciona **Phone Number** > **Buy a number**. <br><br>![Consola de Twilio con la pestaña "Develop" abierta y la opción "Buy a number".]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. Introduce el código de área o localidad que desees (si tienes uno). Encuentra un número y selecciona **Buy**. <br><br> ![Un botón para comprar el número de teléfono listado.]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. Después de comprar tu número de teléfono, ve a **Active Numbers** y selecciona el número de teléfono que acabas de comprar. <br><br>!["Active Numbers" mostrando el número de teléfono comprado.]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### Paso 2: Configurar tu número de teléfono {#step-2-configure-your-phone-number}

Configura tu número de teléfono de Twilio para recibir códigos de verificación por correo electrónico. **No vincules tu número de teléfono a WhatsApp en la consola de Twilio.**

{% alert warning %}
No vincules tu número de teléfono a WhatsApp en la consola de Twilio. Si lo haces, el número se registrará en la cuenta de WhatsApp Business de Twilio, lo que te impedirá conectarlo a Braze a través del flujo de registro integrado.
{% endalert %}

1. En la consola de Twilio, ve a la [página de Active Numbers](https://www.twilio.com/console/phone-numbers/incoming) y selecciona el número de teléfono que compraste.
2. Ve a la sección **Voice Configuration** y en el menú desplegable **Configure with**, selecciona **Webhook, TwiML Bin, Function, Studio Flow, Proxy Service**.
3. En la fila **A call comes in**, selecciona **Webhook** y establece la URL como `https://twimlets.com/voicemail?Email=YOUR_EMAIL_ADDRESS`, reemplazando `YOUR_EMAIL_ADDRESS` con tu dirección de correo electrónico.

### Paso 3: Completar el flujo de registro integrado {#step-3-complete-the-embedded-sign-up-workflow}

1. Una vez configurado Twilio, ve a tu panel de Braze > **Socios tecnológicos** > **WhatsApp** y selecciona **Begin integration** o **Add WhatsApp Business Account**, según lo que aparezca, para iniciar el [flujo de registro integrado]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup/).<br><br>En el paso **Add a phone number for WhatsApp**, selecciona **Phone call** para elegir cómo deseas verificar tu número de teléfono. <br><br>![Sección con las opciones para verificar tu número de teléfono mediante mensaje de texto o llamada telefónica.]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. Espera unos minutos a que el código de verificación llegue a tu buzón de entrada de correo electrónico, luego introduce el código de verificación y completa tu configuración.

## Adquirir un número de teléfono de Infobip {#acquiring-an-infobip-phone-number}

1. En la consola de Infobip, ve a **Channels and Numbers** y selecciona **Numbers**.<br><br>![Sección "Channels and Numbers" de Infobip con "Numbers" listado debajo.]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. Selecciona **Buy Number** > el país donde deseas enviar mensajes > **SMS**.<br><br>![Botón para comprar un número.]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. Dependiendo del país seleccionado, es posible que debas completar un proceso de registro adicional (como seleccionar una opción 10DLC o de número gratuito para números de teléfono de EE. UU.). Asegúrate de seleccionar la opción disponible.<br><br>![Una página que solicita seleccionar el tipo de número: 10DLC o número gratuito.]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. Selecciona la oferta disponible, luego continúa con el resto de los pasos y espera a que se procese tu solicitud. Puedes verificar el estado yendo a **Numbers** > **My Request**. <br><br>![Una oferta con información que incluye tarifas y cobertura.]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. Dependiendo del país seleccionado, espera a que el equipo de Infobip se ponga en contacto contigo para los detalles de registro (como para 10DLC en EE. UU.).<br><br>

6. Cuando tu número de teléfono esté listo en Infobip, ve a tu panel de Braze > **Socios tecnológicos** > **WhatsApp** y selecciona **Begin integration** o **Add WhatsApp Business Account**, según lo que aparezca, para iniciar el [flujo de registro integrado]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup/).<br><br> En el paso **Add a phone number for WhatsApp**, selecciona **Text message** para elegir cómo deseas verificar tu número de teléfono.<br><br>![Sección con las opciones para verificar tu número de teléfono mediante mensaje de texto o llamada telefónica.]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Revisa los [registros de análisis](https://www.infobip.com/docs/analyze/analyze-logs) de Infobip en su portal de clientes para obtener el código de verificación, que puede tardar unos minutos en aparecer, luego introduce el código de verificación y completa la configuración.