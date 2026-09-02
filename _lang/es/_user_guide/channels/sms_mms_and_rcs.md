---
nav_title: "SMS, MMS y RCS"
article_title: "SMS, MMS y RCS"
page_order: 8
page_type: landing
channel:
  - SMS
  - MMS
  - RCS
search_rank: 3
description: "Aprende sobre SMS, MMS y RCS en Braze, incluyendo la configuración, el cumplimiento y las mejores prácticas para llegar a los usuarios por número de teléfono."
---

# SMS, MMS y RCS {#sms-mms-and-rcs}

> SMS (servicio de mensajes cortos), MMS (servicio de mensajería multimedia) y RCS (servicios de comunicación enriquecida) ofrecen una forma directa de llegar a los usuarios a través de sus números de teléfono en tiempo real. SMS sigue siendo uno de los canales más utilizados en todo el mundo porque es rápido, familiar y eficaz para las actualizaciones urgentes. Este centro cubre la configuración de remitentes, el cumplimiento, la recopilación de adhesiones voluntarias, la creación de mensajes y los informes de SMS, MMS y RCS en Braze. Revisa [Leyes y regulaciones]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) y [Recopilación de adhesiones voluntarias de usuarios]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins) antes de enviar tu primer mensaje.

## Requisitos previos {#prerequisites}

La disponibilidad de SMS, MMS y RCS depende de tu paquete de Braze. Ponte en contacto con tu director de cuentas o administrador de éxito de cliente para empezar.

Antes de empezar, asegúrate de tener lo siguiente:

- Códigos abreviados, códigos largos o ID de remitente alfanuméricos configurados. Para obtener más información, consulta [Configuración del remitente]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).
- Familiaridad con las leyes y regulaciones de SMS, incluidos los requisitos de TCPA y de los operadores. Para obtener más información, consulta [Leyes y regulaciones]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).
- Consentimiento de adhesión voluntaria explícito recopilado de los usuarios. Para obtener más información, consulta [Recopilación de adhesiones voluntarias de los usuarios]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins).

## Ejemplos {#use-cases}

| Ejemplo | Explicación |
| --- | --- |
| Recordatorios de citas | Envía recordatorios oportunos antes de las citas programadas, reduciendo las ausencias y manteniendo informados a los clientes. |
| Actualizaciones de pedidos | Notifica a los clientes sobre confirmaciones de pedidos, estado de envío y actualizaciones de entrega en tiempo real. |
| Autenticación de dos factores | Entrega códigos de verificación de un solo uso para el inicio de sesión en la cuenta y la confirmación de transacciones. |
| Ofertas promocionales | Llega a los clientes con promociones de tiempo limitado, ventas flash y descuentos personalizados directamente en su teléfono. |
| Atención al cliente | Habilita conversaciones bidireccionales para resolver consultas de los clientes, recopilar comentarios o confirmar solicitudes de servicio. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ejemplos" }

## Comparación entre SMS, MMS y RCS {#sms-mms-and-rcs-compared}

- **SMS** entrega mensajes de solo texto de hasta 160 caracteres (o 70 caracteres con Unicode). Es compatible de forma universal con todos los dispositivos móviles y operadores.
- **MMS** amplía SMS con soporte para contenido multimedia, incluyendo imágenes, GIF y audio. MMS requiere compatibilidad del operador y del dispositivo.
- **RCS** es la próxima generación de mensajería empresarial, ofreciendo características enriquecidas como perfiles de remitente de marca, respuestas sugeridas, carruseles y confirmaciones de lectura. La disponibilidad de RCS depende de la compatibilidad del operador y del dispositivo.

### ¿Por qué usar RCS? {#why-use-rcs}

RCS (Rich Communication Services) se basa en SMS con una experiencia más rica y similar a una aplicación en la aplicación de mensajería predeterminada de los dispositivos compatibles. Las marcas usan RCS para:

- Entregar imágenes y video de alta resolución en lugar de solo texto sin formato.
- Añadir respuestas y acciones sugeridas para que los clientes puedan responder con un solo toque.
- Mostrar un perfil de remitente verificado con marca para que los mensajes sean fáciles de confiar.
- Admitir confirmaciones de lectura e indicadores de escritura donde los operadores lo permitan.

RCS es ideal para ejemplos como actualizaciones transaccionales (envíos, citas), promociones con contenido enriquecido, atención al cliente con opciones de respuesta rápida, e incorporación o tutoriales que se benefician de contenido multimedia y acciones estructuradas. Para la configuración y la migración desde SMS, consulta [Configuración de RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Necesito el consentimiento de adhesión voluntaria antes de enviar SMS en Braze? {#do-i-need-opt-in-consent-before-sending-sms-in-braze}

Sí. Recopila el consentimiento explícito de adhesión voluntaria y cumple con las leyes aplicables, como la TCPA y los requisitos del operador. Consulta [Recopilar adhesiones voluntarias de los usuarios]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins) y [Leyes y regulaciones]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).

### ¿Cuál es la diferencia entre SMS, MMS y RCS? {#what-is-the-difference-between-sms-mms-and-rcs}

SMS envía mensajes de solo texto, MMS añade contenido multimedia como imágenes, y RCS añade características enriquecidas como perfiles de remitente con marca y respuestas sugeridas en dispositivos compatibles. Consulta **Comparación de SMS, MMS y RCS** más arriba en esta página.

### ¿Cómo configuro los números de remitente para SMS? {#how-do-i-configure-sender-numbers-for-sms}

Configura códigos abreviados, códigos largos o identificadores de remitente alfanuméricos en Braze antes de lanzar campañas. Consulta [Configuración del remitente]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).

## Próximos pasos {#next-steps}

- [Configuración del mensaje]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup)
- [Crear un mensaje]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create)