---
nav_title: Calificación de calidad y límites de mensajería
article_title: Calificación de calidad y límites de mensajería
description: "Este artículo de referencia cubre cómo Meta influye en tu calificación de calidad y los límites de mensajería para el canal de WhatsApp."
page_type: partner
search_tag: Partner
page_order: 1
channel:
  - WhatsApp
---

# Calificación de calidad y límites de mensajería {#quality-rating-and-messaging-limits}

> Meta influye en tu calificación de calidad y en los [límites de mensajería](https://developers.facebook.com/docs/whatsapp/messaging-limits) desde el momento en que comienzas a usar el canal de WhatsApp, y seguirá influyendo en ellos en función de tu uso de WhatsApp.

## Definiciones {#definitions}

| Palabra | Definición |
| --- | --- |
| Calificación de calidad | Una calificación basada en los mensajes recientes que tus clientes han recibido durante los últimos siete días. Esta calificación se determina a partir de los comentarios de tus clientes, como el motivo para bloquear tu número de teléfono y otros problemas reportados. Consulta la documentación de Meta para obtener más información [sobre tu calificación de calidad](https://www.facebook.com/business/help/896873687365001).|
| Límite de mensajería | El número máximo de conversaciones iniciadas por la empresa que puedes comenzar con cada uno de tus números de teléfono en un período continuo de 24 horas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definitions" }

## Incorporación {#onboarding}

Cuando se crea una nueva cuenta de WhatsApp Business, Meta utiliza una variedad de factores para determinar el límite de envío inicial. Puedes encontrar este límite en tu WhatsApp Business Administrador, y detalles adicionales en tu página de Phone Number Insights.

Consulta la documentación de Meta para obtener más información sobre [cómo verificar tu límite](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit) y los [requisitos de número de teléfono](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers).

## Rendimiento {#throughput}

Meta inicia cada número de teléfono empresarial registrado con un rendimiento de 80 MPS or mensajes por segundo or mensajes por segundo. Las actualizaciones a 1000 MPS or mensajes por segundo or mensajes por segundo pueden ocurrir automáticamente o bajo solicitud. Información.

Consulta la documentación de Meta para obtener más información sobre tu [rendimiento](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput).

## Ritmo de plantillas {#template-pacing}

Las plantillas de marketing creadas recientemente y las plantillas de marketing pausadas que se reactivan están potencialmente sujetas a un ritmo de envío controlado. Los criterios de selección de ritmo de Meta se basan principalmente en el historial de calidad de tus plantillas. Cuando usas una plantilla de marketing creada recientemente o una plantilla de marketing reactivada recientemente, los mensajes se enviarán con normalidad hasta que se alcance un umbral no especificado. Una vez alcanzado este umbral, los mensajes posteriores que utilicen esa plantilla se retendrán para permitir tiempo suficiente para recibir comentarios de los clientes.

Consulta la documentación de Meta para obtener más información sobre el [ritmo de plantillas](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing).