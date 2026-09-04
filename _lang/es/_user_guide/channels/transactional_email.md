---
nav_title: Correo electrónico transaccional
article_title: Correo electrónico transaccional
page_order: 4
page_type: landing
channel:
  - email
search_rank: 3
description: "Envía correos electrónicos transaccionales para notificaciones críticas y urgentes desencadenadas por llamadas a la API en Braze."
---

# Correo electrónico transaccional {#transactional-email}

> Los correos electrónicos transaccionales están diseñados específicamente para enviar mensajes automatizados y no promocionales que facilitan una transacción acordada entre tú y tus clientes. Usa campañas de correo electrónico transaccional en Braze para enviar notificaciones críticas y urgentes desencadenadas por llamadas a la API, como confirmaciones de pedidos, restablecimientos de contraseña y actualizaciones de envío.

## Requisitos previos {#prerequisites}

El correo electrónico transaccional solo está disponible como parte de paquetes selectos de Braze. Ponte en contacto con tu CSM de Braze o abre un [ticket de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support) para más detalles.

Antes de empezar, asegúrate de tener lo siguiente:

- [Configuración de correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup) completada, incluyendo la configuración de IP y dominio, autenticación y calentamiento de IP
- Una **clave de API REST de Braze** con el permiso `transactional.send`

## Ejemplos {#use-cases}

El correo electrónico transaccional está diseñado para enviar mensajes no promocionales desencadenados por un servicio. Los ejemplos más comunes incluyen los siguientes:

| Ejemplo | Explicación |
| --- | --- |
| Confirmaciones de pedidos | Confirmar que la compra de un cliente se ha recibido y se está procesando. |
| Restablecimiento de contraseñas | Entregar enlaces seguros y de tiempo limitado para que los clientes restablezcan las credenciales de su cuenta. |
| Notificaciones de envío | Notificar a los clientes cuando su pedido ha sido enviado, incluyendo información de seguimiento y fechas estimadas de entrega. |
| Alertas de cuenta | Enviar notificaciones críticas relacionadas con la cuenta, como fallos en pagos, cambios de suscripción o alertas de seguridad. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ejemplos" }

## Diferencias entre el correo electrónico transaccional y el correo electrónico de marketing {#how-transactional-email-differs-from-marketing-email}

Los correos electrónicos transaccionales se envían a través de una [API HTTP transaccional]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email) dedicada de Braze, que está optimizada para la velocidad y la fiabilidad. A diferencia de los correos electrónicos de marketing, los correos electrónicos transaccionales:

- No requieren que el usuario haya dado su consentimiento para recibir comunicaciones de marketing
- Se desencadenan mediante llamadas a la API en lugar de desencadenantes programados o basados en acciones
- Admiten la entrega casi en tiempo real para contenido con plazos críticos

## Próximos pasos {#next-steps}

{% article_tiles %}
- name: Crear un correo electrónico transaccional
  link: /docs/user_guide/channels/transactional_email/create_a_transactional_email
- name: Seguimiento
  link: /docs/user_guide/channels/transactional_email/tracking
{% endarticle_tiles %}