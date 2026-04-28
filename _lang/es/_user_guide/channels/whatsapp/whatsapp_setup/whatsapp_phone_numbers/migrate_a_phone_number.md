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

## Migrar tu número de teléfono de WhatsApp {#migrating-your-whatsapp-phone-number}

1. En el WhatsApp Manager, selecciona la cuenta de WhatsApp Business (WABA) asociada a tu número de teléfono y luego ve a **Account tools** > **Phone numbers**.
2. Selecciona **Turn off two-step verification** y completa los pasos que siguen.<br><br>![WhatsApp Business Manager abierto en la página "Phone numbers".]({% image_buster /assets/img/whatsapp/waba_manager.png %}){: style="max-width:80%;"} <br><br> Si estás migrando un número de teléfono a un grupo de WhatsApp Business diferente y el registro integrado de Meta requiere que el nombre para mostrar coincida, toma nota del nombre para mostrar existente en la página **Phone Numbers**. Ingresarás ese nombre durante el siguiente paso.<br><br>![La página Phone Numbers del WhatsApp Business Manager con un nombre para mostrar "Braze" junto a un número de teléfono.]({% image_buster /assets/img/whatsapp/phone_numbers.png %}){: style="max-width:80%;"}<br><br>
3. Continúa el flujo de registro integrado de Meta hasta completarlo.