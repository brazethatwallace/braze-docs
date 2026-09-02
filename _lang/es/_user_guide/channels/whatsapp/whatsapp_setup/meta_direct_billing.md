---
nav_title: Facturación directa de Meta
article_title: Facturación directa de Meta
page_order: 7
description: "Este artículo de referencia explica cómo configurar la facturación directa de Meta para que pagues los costes de mensajería de WhatsApp con tu propia tarjeta de débito o crédito en lugar de una línea de crédito de Braze o de un partner."
page_type: reference
channel:
  - WhatsApp
alias: /whatsapp_meta_direct_billing/
hidden: true
noindex: true
---

# Facturación directa de Meta {#meta-direct-billing}

> La facturación directa de Meta te permite pagar los costes de mensajería de WhatsApp directamente con tu propia tarjeta de débito o crédito, en lugar de facturar a través de una línea de crédito de Braze o de un partner.

## Requisitos previos {#prerequisites}

Antes de configurar la facturación directa de Meta, asegúrate de tener lo siguiente:

| Requisito | Descripción |
| --- | --- |
| Acceso al espacio de trabajo de Braze | Necesitarás acceso a **Integraciones de partners** > **Partners tecnológicos** en Braze para iniciar el flujo de registro integrado. |
| Cuenta de Meta Business Administrador | La facturación se configura en Meta Business Administrador, en **Facturación y pagos**. |
| Tarjeta de débito o crédito | Se requiere una tarjeta válida para completar la configuración. La facturación mensual puede aparecer como opción en algunas cuentas, pero no está garantizada. |
| Información comercial completa | El nombre de tu empresa, la dirección y la moneda deben estar completos y ser precisos. Meta revisa esta información antes de habilitar la mensajería. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Configuración {#setup}

### Paso 1: Selecciona la facturación directa de Meta {#step-1-select-meta-direct-billing}

1. En Braze, ve a **Integraciones de partners** > **Partners tecnológicos**, busca **WhatsApp** y abre la página **WhatsApp Messaging Integration**.
2. Selecciona la pestaña **Meta Direct Billing**. Esto significa que tu relación de facturación es directamente con Meta, en lugar de a través de Braze o una línea de facturación de Infobip, por lo que es importante seleccionar esta pestaña antes de continuar, en lugar de intentar cambiarla después.
3. En **Add a WhatsApp Business Account or phone number**, selecciona **Add account or number**. Esto inicia el registro integrado de Meta, donde iniciarás sesión en Meta, seleccionarás tu portafolio de negocios, crearás o seleccionarás tu cuenta de WhatsApp Business (WABA) y verificarás tu número de teléfono.

### Paso 2: Ve a Facturación y pagos {#step-2-go-to-billing-payments}

Después de completar el registro integrado de Meta, haz una de las siguientes acciones:

- Selecciona **Add payment method**, que te lleva a Meta Business Administrador.
- En Meta Business Administrador, ve a **Billing & payments** > **Accounts** y selecciona tu WABA.

### Paso 3: Añade un método de pago {#step-3-add-a-payment-method}

1. Selecciona **Add payment method**.
2. En la ventana que se abre, confirma la **Business location and currency** (por ejemplo, **Canada, US Dollars USD**), que determina la moneda en la que se te factura. Selecciona **Edit** si necesitas cambiarla.
3. En **Select payment method**, es posible que veas líneas de crédito existentes. No están disponibles para tu uso; no las selecciones. Para más detalles, consulta [restricciones de líneas de facturación](#billing-line-restrictions).

![La ventana de selección de método de pago con la opción de tarjeta de débito o crédito seleccionada y las líneas de crédito existentes de Infobip y Braze sin seleccionar.]({% image_buster /assets/img/whatsapp/payment_methods.png %}){: style="max-width:40%;"}

{: start="4"}
4. En **Add payment method**, selecciona **Debit or credit card** y luego selecciona **Next**.
5. Introduce los datos de tu tarjeta y selecciona **Save**.
6. Tu tarjeta aparece en **Payment methods**, marcada como **Default**, con el número de tarjeta enmascarado y la fecha de vencimiento visibles.

{% alert note %}
Cerrar la ventana de configuración después de añadir tu método de pago no desconecta tu número de teléfono. El número vinculado se conserva.
{% endalert %}

### Paso 4: Confirma tu información comercial {#step-4-confirm-your-business-information}

Meta revisa el nombre de tu empresa, la dirección y la moneda antes de habilitar la mensajería. La información comercial incompleta o inexacta puede provocar que los mensajes fallen o un error de información comercial no válida.

## Restricciones de líneas de facturación {#billing-line-restrictions}

Las líneas de crédito que aparecen en la lista de métodos de pago (por ejemplo, "Infobip Limited" o "BRAZE INC.") pertenecen a esa empresa específica, no a ti. Aparecen debido a cómo está conectada tu cuenta, pero no se pueden seleccionar.

## Recursos de Meta {#meta-resources}

- [Centro de ayuda de Meta Business: Facturación y pagos](https://business.facebook.com/business/help/535561817791563)
- [Centro de ayuda de Meta Business: Añadir un método de pago](https://www.facebook.com/business/help/832746984379005)