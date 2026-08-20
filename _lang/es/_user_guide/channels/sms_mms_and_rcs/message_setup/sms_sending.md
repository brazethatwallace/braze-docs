---
nav_title: Envío de SMS
article_title: Envío de SMS
page_order: 4
alias: /sms_message_sending/
description: "Este artículo de referencia cubre los conceptos básicos y las mejores prácticas del envío de SMS."
page_type: reference
channel:
  - SMS


---

# Envío de mensajes SMS {#sms-message-sending}

> La mensajería puede ser complicada, pero no tiene por qué serlo. Las siguientes secciones describen los fundamentos del envío de mensajes SMS en Braze, incluyendo la importancia de los grupos de suscripción, los requisitos para los segmentos del mensaje y los cuerpos de los mensajes, así como las opciones avanzadas de personalización disponibles.

## Conceptos básicos del envío de SMS {#sms-sending-basics}

### Selecciona tu grupo de suscripción {#select-your-subscription-group}

Los mensajes SMS deben enviarse desde un [grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups). Un grupo de suscripción es un conjunto de números de teléfono de envío (como códigos abreviados, códigos largos y/o ID de remitente alfanuméricos) que se utilizan para un tipo específico de mensajería. Debes designar un grupo de suscripción para asegurarte de que solo se dirijan a los usuarios suscritos. Algunos clientes pueden tener varios grupos de suscripción para diferentes ejemplos, como mensajería SMS transaccional y mensajería SMS promocional.<br><br>

### Introduce el cuerpo del mensaje {#input-message-body}

El cuerpo de un mensaje SMS acepta hasta 1600 caracteres, incluidos emojis, Liquid y contenido conectado. Un solo envío de Campaign puede generar muchos envíos de segmentos del mensaje. Los cuerpos de los mensajes SMS de Braze pueden componerse con los estándares de codificación [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) o [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set). En caso de que se utilice un carácter UCS-2 (por ejemplo, un emoji), el cuerpo del mensaje se formateará automáticamente para ese estándar de codificación.<br><br>

### Comprende los segmentos del mensaje y los límites de caracteres {#understand-message-segments-and-character-limits}

Los segmentos del mensaje SMS son la forma en que la industria de SMS cuenta los mensajes. Un segmento del mensaje es una agrupación de hasta un número definido de caracteres (160 para codificación GSM-7; 67 para codificación UCS-2) enviados en un solo despacho de SMS. Si tu mensaje utiliza caracteres de la tabla de extensión GSM-7 (como `{`, `}` o `~`), cada segmento puede contener menos caracteres. Si envías un SMS con 161 caracteres usando codificación GSM-7, se envían dos segmentos del mensaje. Enviar múltiples segmentos del mensaje puede generar cargos adicionales.<br><br>

### Personalización de palabras clave (opcional) {#keyword-customization-optional}

Las regulaciones exigen que haya respuestas a todas las respuestas de palabras clave de SMS de adhesión voluntaria, cancelación de suscripción y ayuda/información. Con Braze, puedes definir tus propias palabras clave para desencadenar respuestas de adhesión voluntaria, cancelación de suscripción y ayuda, gestionar tus propias respuestas que se envían a los usuarios y definir conjuntos de palabras clave para diferentes idiomas. Para más información, consulta nuestra colección sobre [Procesamiento de palabras clave]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing).

{% alert tip %}
¿Quieres aprender a crear una campaña de SMS? Consulta nuestra guía paso a paso sobre [Crear un mensaje SMS, MMS o RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create).
{% endalert %}

Para conocer las mejores prácticas de envío, incluida la orientación sobre envíos multinacionales y de alto volumen, consulta [Mejores prácticas para SMS, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/best_practices).