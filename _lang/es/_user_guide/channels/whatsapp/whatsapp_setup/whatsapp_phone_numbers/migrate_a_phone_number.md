---
nav_title: "Migrar un número"
article_title: "Migrar un número de teléfono de WhatsApp"
page_order: 2
description: "Este artículo de referencia explica cómo migrar tu número de teléfono de WhatsApp."
page_type: reference
channel:
  - WhatsApp
---

# Migrar un número de teléfono de WhatsApp {#migrate-a-whatsapp-phone-number}

> Migra tu número de teléfono de WhatsApp entre cuentas de WhatsApp Business utilizando el registro integrado (Embedded Signup) de Meta.

## Requisitos previos {#prerequisites}

Tu número de teléfono debe cumplir los requisitos de Meta para ser elegible para la migración:

- Tu cuenta Meta Business está verificada.
- Tu cuenta de WhatsApp Business existente está aprobada.
- Tu cuenta de WhatsApp Business existente tiene un método de pago válido en **Payment Settings**.
- Tu número de teléfono de empresa tiene la verificación en dos pasos desactivada. Si eres propietario de tu cuenta de WhatsApp Business, puedes desactivar la verificación en dos pasos en el número desde el WhatsApp Manager. De lo contrario, debes pedirle a tu proveedor de solución que la desactive por ti.

Para obtener información sobre cómo migrar tu número de teléfono de WhatsApp, consulta la documentación de Meta sobre [Migrar números de teléfono entre cuentas de WhatsApp Business a través de Embedded Signup](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/migrate-phone-to-different-waba/).

## Migrar entre cuentas de WhatsApp Business {#migrate-between-whatsapp-business-accounts}

1. En el WhatsApp Manager, selecciona la cuenta de WhatsApp Business (WABA) asociada a tu número de teléfono y luego ve a **Account tools** > **Phone numbers**.
2. Selecciona **Turn off two-step verification** y completa los pasos que siguen.<br><br>![WhatsApp Business Manager abierto en la página "Phone numbers".]({% image_buster /assets/img/whatsapp/waba_manager.png %}){: style="max-width:80%;"} <br><br> Si estás migrando un número de teléfono a un grupo de WhatsApp Business diferente y el registro integrado de Meta requiere que el nombre para mostrar coincida, toma nota del nombre para mostrar existente en la página **Phone Numbers**. Ingresarás ese nombre durante el siguiente paso.<br><br>![La página Phone Numbers del WhatsApp Business Manager con un nombre para mostrar "Braze" junto a un número de teléfono.]({% image_buster /assets/img/whatsapp/phone_numbers.png %}){: style="max-width:80%;"}<br><br>
3. Continúa el flujo de registro integrado de Meta hasta completarlo.

## Migrar desde otro proveedor de solución empresarial (BSP) {#migrate-from-another-business-solution-provider}

Si tu número de teléfono de WhatsApp está registrado con otro BSP, debes migrar el número a una cuenta de WhatsApp Business conectada a Braze antes de que Braze pueda enviar mensajes con ese número.

### Antes de migrar {#before-you-migrate}

- Ten en cuenta que un número de teléfono solo puede estar activo en un BSP a la vez. La migración traslada el envío a Braze; tu BSP anterior pierde el acceso al número.
- Revisa los contratos y la facturación con tu proveedor actual. El historial de mensajes y las plantillas pueden no transferirse automáticamente.
- Desactiva la verificación en dos pasos en el número según los requisitos de Meta.
- Si necesitas números separados para soporte y marketing, consulta [Integraciones, datos e informes]({{site.baseurl}}/user_guide/channels/whatsapp/faq#integrations-data-and-reporting) en las preguntas frecuentes de WhatsApp.

### Rutas de migración {#migration-paths}

| Configuración actual | Ruta recomendada |
|---|---|
| Número en otro BSP, migración completa a Braze | Migrar a través del [registro integrado]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup) a una WABA nueva o existente de Braze |
| Número en la integración nativa de Braze, migración a facturación de Infobip | [Conector BYO de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/byo_connector) (solo Infobip) |
| Marketing en Braze, soporte en otra WABA | Mantener WABAs y números de teléfono separados; consulta las [preguntas frecuentes de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/faq#integrations-data-and-reporting) y [WhatsApp y sistemas externos]({{site.baseurl}}/user_guide/channels/whatsapp/use_cases/whatsapp_and_external_systems) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rutas de migración" }

## Espacios de trabajo de desarrollo y producción {#development-and-production-workspaces}

Braze recomienda cuentas de WhatsApp Business separadas para desarrollo y producción siempre que sea posible:

- No vincules tu número de teléfono de producción a un espacio de trabajo de sandbox o desarrollo.
- Usa una WABA de prueba dedicada y un número de teléfono para las pruebas de integración.
- Las aprobaciones de plantillas se aplican por WABA; aprueba las plantillas en la WABA vinculada al espacio de trabajo desde el que envías.