---
nav_title: "Múltiples cuentas de empresa"
article_title: "Múltiples cuentas de empresa"
page_order: 5
description: "Este artículo de referencia cubre los pasos para añadir cuentas de empresa de WhatsApp y números de teléfono."
page_type: reference
channel:
  - WhatsApp
---

# Múltiples cuentas de empresa y números de teléfono de WhatsApp {#multiple-whatsapp-business-accounts-and-phone-numbers}

> Puedes añadir múltiples cuentas de empresa de WhatsApp y grupos de suscripción (y números de teléfono) a cada espacio de trabajo. <br><br>Cada grupo de suscripción está conectado a un número de teléfono único, por lo que no puedes conectar el mismo número de teléfono a múltiples grupos de suscripción ni conectar múltiples números de teléfono a un grupo de suscripción.

## Múltiples cuentas de empresa de WhatsApp {#multiple-whatsapp-business-accounts}

Tener múltiples cuentas de empresa de WhatsApp es útil si quieres enviar mensajes de WhatsApp a usuarios en un espacio de trabajo de Braze que tiene múltiples marcas. Esto se debe a que cada cuenta de empresa opera de forma independiente dentro de WhatsApp y tiene su propio número de teléfono, plantilla de mensaje y calificación de calidad.

Las cuentas de empresa que están anidadas dentro del mismo Meta Business Administrador también compartirán la gestión de permisos de acceso de usuarios y catálogos (aún no compatible en Braze).

![Diagrama del ecosistema de Braze y WhatsApp, que muestra cómo los espacios de trabajo y las cuentas de empresa de WhatsApp se conectan entre sí: puedes conectar un grupo de suscripción a un número de teléfono, múltiples cuentas de empresa de WhatsApp a un espacio de trabajo, y un espacio de trabajo a múltiples Meta Business Portfolios.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})

### Añadir una cuenta de empresa de WhatsApp {#adding-a-whatsapp-business-account}

Puedes añadir hasta 10 cuentas de empresa de WhatsApp por espacio de trabajo. Las cuentas de empresa pueden estar anidadas en diferentes Meta Business Managers. Para añadir una cuenta:

1. Ve a **Socios tecnológicos** > **WhatsApp** y selecciona **Add WhatsApp Business Account**.

![Sección de integración de mensajería de WhatsApp con opciones para añadir una cuenta de empresa o añadir un grupo de suscripción y número.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2. Sigue el flujo de trabajo de registro. Para un recorrido detallado paso a paso, consulta [Registro integrado de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup).

{% alert important %}
Tu número de teléfono debe cumplir con todos los requisitos de cualquier número de teléfono de WhatsApp, incluyendo no estar registrado en ninguna otra cuenta de WhatsApp.
{% endalert %}

## Múltiples grupos de suscripción y números de teléfono {#multiple-subscription-groups-and-phone-numbers}

Las plantillas de mensaje se comparten entre todos los números de teléfono de la misma cuenta de empresa de WhatsApp. Para más detalles sobre los grupos de suscripción de WhatsApp, consulta [Grupos de suscripción]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups).

Cada número de teléfono de WhatsApp aparecerá como un chat de WhatsApp separado para los usuarios. Cada número de teléfono dentro de una cuenta de empresa de WhatsApp opera de forma independiente de los demás, por lo que pueden tener los mismos o diferentes valores para lo siguiente:
- Nombre para mostrar
- Estado
- Calificación de calidad
- Límite de mensajería

### Añadir un grupo de suscripción y número de teléfono {#adding-a-subscription-group-and-phone-number}

Puedes añadir hasta 20 grupos de suscripción (y números de teléfono de envío) por cuenta de empresa de WhatsApp. Para añadir un grupo de suscripción y número de teléfono:

1. Ve a **Socios tecnológicos** > **WhatsApp** y selecciona **Add Subscription Group and Number**.

![Sección de integración de mensajería de WhatsApp con opciones para añadir una cuenta de empresa o añadir un grupo de suscripción y número.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2. Sigue el flujo de trabajo de registro. <br><br> En el paso **Select your WhatsApp Business Account**, selecciona tu cuenta de empresa de WhatsApp existente y añade un nuevo número de teléfono. Este número debe cumplir con todos los requisitos de cualquier número de teléfono de WhatsApp, incluyendo no estar registrado en ninguna otra cuenta de WhatsApp.

### Eliminar un grupo de suscripción y número de teléfono {#removing-a-subscription-group-and-phone-number}

1. Ve a **Audiencia** > **Suscripciones** y archiva el grupo de suscripción.
2. Ve a tu Meta Business Administrador y elimina el número de teléfono.