---
nav_title: Envío de servicio de mensajes cortos
article_title: Envío de servicio de mensajes cortos
page_order: 4
alias: /sms_message_sending/
description: "Consulta los grupos de suscripción, la facturación de mensajes y los fundamentos de palabras clave para el envío de mensajes servicio de mensajes cortos."
page_type: reference
channel:
  - SMS

---

# Envío de mensajes servicio de mensajes cortos {#sms-message-sending}

> Consulta los fundamentos de suscripción, facturación y palabras clave que aplican cuando envías mensajes servicio de mensajes cortos con Braze.

## Conceptos básicos del envío de servicio de mensajes cortos {#sms-sending-basics}

### Selecciona tu grupo de suscripción {#select-your-subscription-group}

Envía mensajes servicio de mensajes cortos desde un [grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups). Un grupo de suscripción contiene números de teléfono de envío, como códigos abreviados, códigos largos e ID de remitente alfanuméricos, para un propósito específico de mensajería. Usa grupos de suscripción separados para casos como mensajería transaccional y promocional.

### Redacta el mensaje {#compose-the-message}

Para campos de mensaje, límites de caracteres, personalización, medios y acortamiento de enlaces, consulta [Crear un mensaje servicio de mensajes cortos, MMS o RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create#sms-and-mms-fields-and-settings).

### Comprende los segmentos del mensaje y los límites de caracteres {#understand-message-segments-and-character-limits}

Los mensajes servicio de mensajes cortos usan codificación GSM-7 o UCS-2 y se cobran por segmento del mensaje. Para las reglas de codificación, tamaños de segmento y la calculadora de segmentos, consulta [Calculadoras de facturación de servicio de mensajes cortos y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator).

### Personalización de palabras clave (opcional) {#keyword-customization-optional}

Las regulaciones requieren respuestas a palabras clave de adhesión voluntaria, cancelación y ayuda o información. Define palabras clave, respuestas y conjuntos de palabras clave específicos del idioma a través del [procesamiento de palabras clave]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing).

Para conocer las mejores prácticas de envío, incluida la orientación sobre envíos a varios países y de alto volumen, consulta [Mejores prácticas para servicio de mensajes cortos, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/best_practices).