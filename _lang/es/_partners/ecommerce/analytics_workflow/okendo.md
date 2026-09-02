---
nav_title: Okendo
article_title: Okendo
description: "Aprende a integrar Okendo con Braze."
page_type: partner
search_tag: Partner
alias: /partners/okendo/
---

# Okendo

> [Okendo](https://okendo.io/) es una plataforma unificada de marketing del cliente que proporciona herramientas para cultivar la promoción, ampliar el boca a boca y maximizar el LTV or valor de duración del ciclo de vida or valor de duración del ciclo de vida para movilizar a tus clientes y conseguir un crecimiento más rápido y eficiente.

*Esta integración está mantenida por Okendo.*

## Sobre la integración {#about-the-integration}

La integración de Braze con Okendo funciona en múltiples productos de la plataforma de Okendo, incluyendo reseñas, fidelización, referidos, cuestionarios y quizzes. Okendo envía eventos personalizados y atributos de usuario a Braze, que pueden utilizarse para personalizar y desencadenar mensajes.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|------------------------|-----------------------------------------------------------------------------|
| Cuenta de Okendo | Se necesita una cuenta de Okendo para beneficiarse de esta asociación. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos `users.track`. Puede crearse en el panel de Braze desde **Settings** > **API Keys**. |
| Punto de conexión REST or transferencia de estado representacional de Braze | [La URL de tu punto de conexión REST or transferencia de estado representacional]({{site.baseurl}}/api/basics/#endpoints). Tu punto de conexión depende de la URL de Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Configurar el conector de Braze en Okendo {#step-1-set-up-braze-connector-in-okendo}

1. En Okendo, ve a **Settings** > **Integrations** > **Email & servicio de mensajes cortos** > **Braze**.
2. Añade el punto de conexión de la API y la clave de API a la configuración de **Integration**.

### Paso 2: Configura tu identificador {#step-2-configure-your-identifier}

El campo `external_id` se utiliza para identificar al usuario asociado a cada evento. Activa **Use Shopify Customer ID for Braze user identification** para asociar el campo con los ID de cliente de Shopify. De lo contrario, desactívalo para asociarlo con la dirección de correo electrónico de cada usuario.

## Sincronización de eventos y atributos de Okendo con Braze {#syncing-okendo-events-and-attributes-to-braze}

### Eventos personalizados {#custom-events}

{% alert note %}
Para ver ejemplos de datos de eventos, consulta [la documentación de Okendo](https://support.okendo.io/en/articles/10396885-getting-started-with-braze-and-okendo#h_679a212e3c).
{% endalert %}

#### Eventos de reseñas {#review-events}

- Okendo Review Created
- Okendo Review Request

#### Eventos de referidos {#referral-events}

- Sent Okendo Referral
- Opted In to Okendo Referrals
- Okendo Referral Invitation
- Received Okendo Referral Coupon
- Redeemed Okendo Referral Coupon
- Okendo Referral Rejected

#### Eventos de fidelización {#loyalty-events}

- Enrolled in Okendo Loyalty
- Okendo Loyalty Points Awarded
- Okendo Loyalty Points Redeemed
- Okendo Loyalty Tier Changed
- Okendo Loyalty Points Adjusted

#### Evento de cuestionario {#survey-event}

- Submitted Okendo Survey

#### Evento de quiz {#quiz-event}

- Submitted Okendo Quiz

### Atributos personalizados {#custom-attributes}

Okendo envía datos de perfil de usuario como atributos personalizados en Braze, que pueden utilizarse para crear segmentos de audiencia. Algunos ejemplos son:

- Preguntas de perfil realizadas en cuestionarios y durante el envío de una reseña, como la edad, la fecha de nacimiento, el tipo de piel y el color del pelo
- Métricas de reseñas como _la valoración media de reseñas_ y el _sentimiento medio de reseñas_
- Métricas de fidelización como _saldo de puntos_ y _nivel VIP_
- Métricas de referidos como el _número de referidos exitosos_ y los _ingresos totales por referidos_
- Puntuación NPS obtenida de un cuestionario

## Utilizar Braze con productos de Okendo {#using-braze-with-okendo-products}

Dependiendo del producto de Okendo, deberás completar pasos adicionales para utilizar Braze y Okendo juntos. Consulta los siguientes artículos para más detalles:

- [Integración de reseñas con Braze](https://support.okendo.io/en/articles/10509722-integrating-reviews-with-braze#h_09c4575b39)
- [Integración de fidelización con Braze](https://support.okendo.io/en/articles/10509615-integrating-loyalty-with-braze#h_47129ea105)
- [Integración de referidos con Braze](https://support.okendo.io/en/articles/10509748-build-a-canvas-in-braze-to-trigger-referral-emails#h_32fb5ba542)
- [Integración de cuestionarios con Braze](https://support.okendo.io/en/articles/11546662-integrating-surveys-with-braze)
- [Integración de quizzes con Braze](https://support.okendo.io/en/articles/10509739-build-a-canvas-in-braze-to-send-quiz-recommendations#h_53748cb121)

{% alert note %}
Si necesitas ayuda para configurar la integración, ponte en contacto con el equipo de soporte de Okendo.
{% endalert %}