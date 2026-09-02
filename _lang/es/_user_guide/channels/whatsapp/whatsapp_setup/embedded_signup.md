---
nav_title: Registro integrado
article_title: Registro integrado de WhatsApp
page_order: 1
description: "Este artículo de referencia explica cómo acceder al flujo de trabajo de registro integrado de WhatsApp en Braze, qué preparar antes del registro en Meta y qué sucede una vez completado el registro."
page_type: reference
channel:
  - WhatsApp
---

# Registro integrado de WhatsApp {#whatsapp-embedded-signup}

> Usa el registro integrado para conectar Braze a una cuenta de WhatsApp Business (WABA) a través del flujo de registro alojado en Meta.

El flujo de trabajo de registro integrado de WhatsApp se abre cuando [integras WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) por primera vez en tu espacio de trabajo de Braze, y cuando [añades una cuenta de WhatsApp Business o un número de teléfono]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) a una integración existente.

{% alert note %}
Puedes añadir [múltiples cuentas de WhatsApp Business]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/multiple_business_accounts) a un espacio de trabajo de Braze. Sin embargo, cada cuenta de WhatsApp Business específica solo puede añadirse a un único espacio de trabajo de Braze.
{% endalert %}

## Acceder al flujo de trabajo {#accessing-the-workflow}

1. Ve a **Integraciones de partners** > **Partners tecnológicos**.
2. Busca y selecciona **WhatsApp**.
3. Selecciona la opción que se ajuste a tu caso de uso:
   - **Primera integración:** Selecciona **Begin Integration**.
   - **Cuenta o número adicional:** En la página **WhatsApp Messaging Integration**, selecciona **Add account or number** o **Add WhatsApp Business Account**.

El flujo de registro integrado de Meta es el mismo independientemente del punto de entrada desde el que lo inicies. Tu espacio de trabajo también puede mostrar pestañas de integración, como **Native Integration** o **BYO Connector - Infobip**, según tu configuración. Selecciona la pestaña que corresponda a tu configuración antes de comenzar.

## Preparación para el registro {#prepare-for-signup}

Cuando selecciones **Begin Integration**, Braze abre una ventana de incorporación. Revisa cada diapositiva, luego selecciona **Begin Integration** de nuevo para iniciar el registro integrado de Meta.

Antes de comenzar, prepara lo siguiente:

- **Acceso a Meta Business Manager:** La mayoría de las empresas utilizan Meta Business Manager para gestionar páginas de Facebook, anuncios y activos empresariales relacionados. Si no tienes acceso, pide a un administrador que te otorgue permisos o crea una cuenta de Business Manager durante el registro.
- **Número de teléfono:** Usa un número que cumpla con los [requisitos de número de teléfono de WhatsApp de Meta](https://developers.facebook.com/docs/whatsapp/phone-numbers). Recibirás un código de verificación único por mensaje de texto o llamada telefónica durante el registro.

{% alert important %}
Solo completarás el registro integrado inicial una vez por ruta de integración, así que introduce los datos de tu empresa con la mayor precisión posible.
{% endalert %}

## Flujo de trabajo de registro integrado de WhatsApp {#whatsapp-embedded-signup-workflow}

Después de que Braze inicie el registro integrado de Meta, inicia sesión con una cuenta de Meta que tenga acceso al Business Manager de tu empresa. Meta aloja las pantallas de registro; Braze no controla su diseño ni sus etiquetas.

{% alert note %}
Meta puede cambiar las pantallas de registro integrado sin previo aviso. Si el flujo de trabajo difiere de este artículo, sigue las indicaciones de Meta y consulta la [documentación de registro integrado de Meta](https://developers.facebook.com/docs/whatsapp/embedded-signup/embed-the-flow).
{% endalert %}

En general, Meta te guía a través de lo siguiente:

1. **Iniciar sesión y otorgar permisos.** Autentícate con Meta y permite que Braze se conecte a tu cuenta de WhatsApp Business.
2. **Seleccionar tu portafolio de empresa.** Conecta el portafolio de Business Manager que debe ser propietario de la cuenta de WhatsApp Business. Si no ves el portafolio esperado, confirma tus permisos de Meta.
3. **Conectar o crear una cuenta de WhatsApp Business.** Crea una cuenta nueva o selecciona una cuenta no utilizada cuando se te solicite. No selecciones una cuenta de WhatsApp Business que esté conectada activamente a otro proveedor de mensajería; esa conexión no tendrá éxito en Braze. Para [migrar un número desde otro proveedor]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number), contacta con tu equipo de cuenta de Braze antes de comenzar.
4. **Proporcionar detalles de la empresa y de visualización.** Introduce el nombre de la cuenta, el nombre de visualización y la categoría que Meta solicita para tu cuenta de WhatsApp Business.
5. **Verificar tu número de teléfono.** Añade el número que quieras usar para la mensajería de WhatsApp y completa la verificación por mensaje de texto o llamada telefónica.

Cuando Meta finalice el registro integrado, el control regresa a Braze.

## Completa la integración de Braze {#complete-the-braze-integration}

Después del registro integrado, Braze ejecuta los pasos de configuración automáticamente. En la página **WhatsApp Messaging Integration**, es posible que veas mensajes de progreso como **Sign-up flow completed, integration with WhatsApp in progress** mientras Braze realiza lo siguiente:

- Recupera el ID de tu cuenta de WhatsApp Business y los números de teléfono de Meta
- Añade el usuario del sistema de Braze a tu cuenta de WhatsApp Business
- Registra los números de teléfono y se suscribe a los eventos de webhook
- Crea un [grupo de suscripción]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) de Braze para cada número conectado

Espera a que la integración se complete antes de enviar mensajes. Si la configuración falla, revisa el error en la página de integración y consulta [Configuración de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) para obtener orientación general.

## Próximos pasos {#next-steps}

- [Adquirir o migrar un número de teléfono de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers)
- [Crear un mensaje de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)
- [Gestionar grupos de suscripción]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)