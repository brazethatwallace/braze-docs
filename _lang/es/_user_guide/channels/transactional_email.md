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

El correo electrónico transaccional solo está disponible como parte de paquetes selectos de Braze. Ponte en contacto con tu administrador del éxito del cliente de Braze o abre un [ticket de soporte]({{site.baseurl}}/braze_support/) para más detalles.

Antes de empezar, asegúrate de tener lo siguiente:

- [Configuración de correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup/) completada, incluyendo la configuración de IP y dominio, autenticación y calentamiento de IP
- Una **clave de API REST de Braze** con el permiso `transactional.send`

## Casos de uso {#use-cases}

El correo electrónico transaccional está diseñado para enviar mensajes no promocionales desencadenados por servicios. Los casos de uso más comunes incluyen los siguientes:

| Caso de uso | Explicación |
| --- | --- |
| Confirmaciones de pedido | Confirma que la compra de un cliente se ha recibido y está siendo procesada. |
| Restablecimientos de contraseña | Entrega enlaces seguros y urgentes para que los clientes restablezcan las credenciales de su cuenta. |
| Notificaciones de envío | Notifica a los clientes cuando su pedido ha sido enviado, incluyendo información de seguimiento y fechas de entrega estimadas. |
| Alertas de cuenta | Envía notificaciones críticas relacionadas con la cuenta, como fallos de pago, cambios de suscripción o alertas de seguridad. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso" }

## En qué se diferencia el correo electrónico transaccional del correo electrónico de marketing {#how-transactional-email-differs-from-marketing-email}

Los correos electrónicos transaccionales se envían a través de una [API HTTP transaccional]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) dedicada de Braze, que está optimizada para velocidad y fiabilidad. A diferencia de los correos electrónicos de marketing, los correos electrónicos transaccionales:

- No requieren que un usuario haya dado su consentimiento para recibir comunicaciones de marketing
- Se desencadenan mediante llamadas a la API en lugar de desencadenantes planificados o basados en acciones
- Admiten entrega casi en tiempo real para contenido urgente

## Próximos pasos {#next-steps}

- [Crear un correo electrónico transaccional]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email/)
- [Configurar el seguimiento]({{site.baseurl}}/user_guide/channels/transactional_email/tracking/)