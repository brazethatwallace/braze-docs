---
nav_title: Conector BYO WhatsApp
article_title: Conector Bring Your Own WhatsApp
page_order: 2
description: "Este artículo de referencia proporciona un recorrido paso a paso para configurar un conector Bring Your Own WhatsApp, que otorga a Braze acceso a tu Infobip WhatsApp Business Manager."
page_type: reference
channel:
  - WhatsApp
---

# Conector Bring Your Own WhatsApp {#bring-your-own-whatsapp-connector}

> El conector Bring Your Own (BYO) WhatsApp ofrece una asociación entre Braze e Infobip, en la que le das a Braze acceso a tu Infobip WhatsApp Business Manager (WABA). Esto te permite gestionar y pagar los costos de mensajería directamente con Infobip mientras usas Braze para segmentación, personalización y orquestación de campañas. Braze mantiene toda la funcionalidad existente que ofrece el canal de WhatsApp, como mensajes salientes, procesamiento de mensajes entrantes, flujos de WhatsApp y análisis.

{% alert note %}
Para migrar desde otros proveedores de soluciones de negocio (BSP) a la integración de Braze, consulta [Migrar desde otro proveedor de soluciones de negocio]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number#migrate-from-another-business-solution-provider).
{% endalert %}

## Requisitos {#requirements}

| Requisito | Descripción |
| --- | --- |
| Cuenta de Infobip | Se requiere una cuenta de Infobip para usar el conector BYO WhatsApp.
| Créditos de mensaje o acción | Consumes créditos de acción de Braze cuando envías mensajes de WhatsApp. |
| Requisitos de WhatsApp | Completa todos los [requisitos de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#prerequisites). |
| Número de teléfono | Te sugerimos [adquirir un número de teléfono a través de Infobip](https://www.infobip.com/docs/numbers/getting-started) por conveniencia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Configuración {#set-up}

Antes de configurar el conector BYO WhatsApp, confirma que los envíos anteriores de tu cuenta de WhatsApp Business no se hayan realizado a través de Infobip.

### Casos compatibles {#supported-cases}

- La cuenta de WhatsApp Business y el número de teléfono nunca se han conectado a un partner antes.
- La cuenta de WhatsApp Business está conectada directamente a Braze a través de la integración nativa.
    - Sigue los pasos en [Migrar entre cuentas de WhatsApp Business]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number#migrate-between-whatsapp-business-accounts) para migrar tus números de teléfono a una nueva cuenta de WhatsApp Business, un número de teléfono a la vez.
- La cuenta de WhatsApp Business está conectada a un proveedor de soluciones diferente de Braze e Infobip.
    - Sigue los pasos en [Migrar entre cuentas de WhatsApp Business]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number#migrate-between-whatsapp-business-accounts) para migrar tus números de teléfono a una nueva cuenta de WhatsApp Business, un número de teléfono a la vez.

## Paso 1: Recuperar la información de la cuenta de Infobip {#step-1}

1. En Infobip, identifica la cuenta que deseas usar con tu cuenta de WhatsApp Business.
2. Ve a **Developer Tools** > **API Keys** y selecciona **Create API Key**.

![Página "Create API key" con una fecha de creación de "16/12/2025" y una fecha de caducidad de "16/12/36".]({% image_buster /assets/img/whatsapp/byo_connector/create_api_key.png %})

{: start="3"}
3. Dale a la clave un nombre significativo, como "Braze - Mi nombre de espacio de trabajo - Mi nombre de WABA".
4. Agrega una fecha de caducidad lejana en el futuro para evitar problemas con la expiración del token.
    - Toma nota de generar una nueva clave de API y reconectar tu WABA antes de la fecha de caducidad.
5. Selecciona estos alcances:
- `Message:send`
- `Whatsapp:manage`
- `Whatsapp:message:send`
- `Account-management:manage`
- `Subscriptions:manage`
- `Metrics:manage`
6. Después de crear la clave, copia la clave de API.
    - La clave solo se puede copiar durante un tiempo limitado después de la creación. Puedes repetir estos pasos para crear una nueva clave si necesitas conectar otra cuenta de WhatsApp Business en el futuro.

!["Braze Example API Key" con 6 alcances agregados.]({% image_buster /assets/img/whatsapp/byo_connector/api_key.png %})

{: start="7"}
7. Copia la URL base de la API de la cuenta.

![Página "API keys" con una URL base de API resaltada.]({% image_buster /assets/img/whatsapp/byo_connector/api_base_url.png %})

## Paso 2: Iniciar el registro integrado {#step-2-start-the-embedded-signup}

1. En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** > **WhatsApp**.
2. Selecciona la pestaña **BYO Connector - Infobip**.

![La página de socios tecnológicos de WhatsApp.]({% image_buster /assets/img/whatsapp/byo_connector/byo_tab_tech_parners.png %})

{: start="3"}
3. Ingresa la clave de API y la URL base del [Paso 1](#step-1).
4. Selecciona **Connect**.
5. Continúa con el [flujo de trabajo de registro integrado]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup#whatsapp-embedded-signup-workflow) con estas consideraciones:
- No puedes seleccionar el mismo portafolio de negocios que utiliza un proveedor de soluciones de negocio diferente.
- No puedes seleccionar un número de teléfono que esté siendo utilizado por otro proveedor de soluciones de negocio.
- Debes crear un nuevo WABA, no seleccionar uno existente.

{% alert note %}
Para recibir el código de verificación, ve a tu panel de Infobip > **Analyze** > **Logs** y obtén el código del mensaje SMS entrante.
{% endalert %}

![Registros de mensajes que muestran un mensaje SMS entrante con el código de verificación.]({% image_buster /assets/img/whatsapp/byo_connector/verification_code.png %})

Después de completar la configuración, tu número de teléfono aparece como un grupo de suscripción dentro de tu grupo de WhatsApp Business. El grupo de WhatsApp Business contiene el nombre de la cuenta de Infobip y la URL base de la API a la que está conectado. Las cuentas conectadas a través de la integración nativa no tienen un nombre de cuenta de Infobip.

{% alert note %}
Conecta cada cuenta de WhatsApp Business a una sola cuenta de Infobip. Cada vez que conectes un número de teléfono o grupo de suscripción adicional, si la cuenta de WhatsApp Business ya está conectada a una cuenta de Infobip, debes volver a ingresar las credenciales de API de la cuenta existente.
{% endalert %}

## Paso 3: Envío de mensajes {#step-3-sending-messages}

Sigue el proceso de envío de la integración nativa, incluyendo:
- [Suscribir usuarios al grupo de suscripción]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)
- [Crear un mensaje de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)

## Solución de problemas de configuración {#troubleshooting-setup}

### No se pudo recuperar el ID de la cuenta de WhatsApp Business {#couldnt-retrieve-whatsapp-business-account-id}

Confirma que tu cuenta de WhatsApp Business no esté conectada a un espacio de trabajo de Braze diferente.

### No se pudo compartir el ID de la cuenta de WhatsApp Business con Infobip {#couldnt-share-whatsapp-business-account-id-with-infobip}

1. Confirma que tu cuenta de WhatsApp Business no esté conectada a Braze o a otro partner.
2. Confirma que ningún número de teléfono en tu cuenta de WhatsApp Business esté conectado a una cuenta de Infobip diferente. Para números importados, puedes encontrar el número en Infobip y seleccionar **Cancel number**.

## Consideraciones {#considerations}

Si bien toda la funcionalidad existente con Braze es compatible, estos casos de uso actualmente no son compatibles.

| Caso de uso | Razón |
| --- | --- |
| Procesamiento de mensajes entrantes en Braze e Infobip | Esto evita cadenas lógicas que se desencadenan por cualquiera de los dos sistemas, generando consecuentemente hilos de mensajes duplicados y potencialmente contradictorios. |
| Envío de mensajes desde Braze e Infobip | Para las cuentas de WhatsApp Business conectadas a Braze, todos los envíos se originan desde Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Consideraciones" }