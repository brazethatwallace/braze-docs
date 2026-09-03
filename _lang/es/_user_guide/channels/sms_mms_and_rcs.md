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
description: "Esta página de inicio alberga SMS (servicio de mensajes cortos), MMS (servicio de mensajería multimedia) y RCS (servicios de comunicación enriquecida). Estos servicios ofrecen una forma más directa de llegar a tus usuarios que la mayoría de los demás canales de mensajería, ya que utilizan su número de teléfono, lo que te permite contactarlos en tiempo real."
---

# SMS, MMS y RCS {#sms-mms-and-rcs}

> SMS (servicio de mensajes cortos), MMS (servicio de mensajería multimedia) y RCS (servicios de comunicación enriquecida) ofrecen una forma directa de llegar a los usuarios a través de sus números de teléfono en tiempo real. SMS sigue siendo uno de los canales más utilizados en todo el mundo porque es rápido, familiar y eficaz para las actualizaciones urgentes. Este centro cubre la configuración de remitentes, el cumplimiento, la recopilación de adhesiones voluntarias, la creación de mensajes y los informes de SMS, MMS y RCS en Braze. Revisa [Leyes y regulaciones]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) y [Recopilación de adhesiones voluntarias de usuarios]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins) antes de enviar tu primer mensaje.

## Requisitos previos {#prerequisites}

La disponibilidad de SMS, MMS y RCS depende de tu paquete de Braze. Ponte en contacto con tu director de cuentas o administrador de éxito de cliente para comenzar.

Antes de empezar, asegúrate de tener lo siguiente:

- Códigos abreviados, códigos largos o ID de remitente alfanuméricos configurados. Para más información, consulta [Configuración del remitente]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).
- Familiaridad con las leyes y regulaciones de SMS, incluidos los requisitos de la TCPA y de los operadores. Para más información, consulta [Leyes y regulaciones]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).
- Consentimiento explícito de adhesión voluntaria recopilado de los usuarios. Para más información, consulta [Recopilación de adhesiones voluntarias de usuarios]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins).

## Ejemplos {#use-cases}

| Ejemplo | Explicación |
| --- | --- |
| Recordatorios de citas | Envía recordatorios oportunos antes de las citas programadas, reduciendo las ausencias y manteniendo a los clientes informados. |
| Actualizaciones de pedidos | Notifica a los clientes sobre confirmaciones de pedidos, estado del envío y actualizaciones de entrega en tiempo real. |
| Autenticación de dos factores | Entrega códigos de verificación de un solo uso para el inicio de sesión en cuentas y la confirmación de transacciones. |
| Ofertas promocionales | Llega a los clientes con promociones por tiempo limitado, ventas flash y descuentos personalizados directamente en su teléfono. |
| Atención al cliente | Habilita conversaciones bidireccionales para resolver consultas de los clientes, recopilar comentarios o confirmar solicitudes de servicio. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ejemplos" }

## Comparación entre SMS, MMS y RCS {#sms-mms-and-rcs-compared}

- **SMS** envía mensajes de solo texto de hasta 160 caracteres (o 70 caracteres con Unicode). Es compatible con todos los dispositivos móviles y operadores.
- **MMS** amplía el SMS con soporte para contenido multimedia, como imágenes, GIF y audio. MMS requiere compatibilidad del operador y del dispositivo.
- **RCS** es la siguiente generación de mensajería empresarial y ofrece características avanzadas como perfiles de remitente con marca, respuestas sugeridas, carruseles y confirmaciones de lectura. La disponibilidad de RCS depende del soporte del operador y del dispositivo.

### ¿Por qué usar RCS? {#why-use-rcs}

RCS (Rich Communication Services) se basa en SMS y ofrece una experiencia más rica y similar a una aplicación en la aplicación de mensajería predeterminada de los dispositivos compatibles. Las marcas usan RCS para:

- Entregar imágenes y video en alta resolución en lugar de solo texto sin formato.
- Añadir respuestas y acciones sugeridas para que los clientes puedan responder con un solo toque.
- Mostrar un perfil de remitente verificado con la marca para que los mensajes sean fáciles de identificar como confiables.
- Admitir confirmaciones de lectura e indicadores de escritura donde los operadores lo permitan.

RCS es adecuado para ejemplos como actualizaciones transaccionales (envíos, citas), promociones con creatividades enriquecidas, atención al cliente con rutas de respuesta rápida, e incorporación o tutoriales que se benefician de medios y acciones estructuradas. Para la configuración y la migración desde SMS, consulta [Configuración de RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Necesito consentimiento de adhesión voluntaria antes de enviar SMS en Braze? {#do-i-need-opt-in-consent-before-sending-sms-in-braze}

Sí. Recopila el consentimiento explícito de adhesión voluntaria y cumple con las leyes aplicables, como la TCPA y los requisitos del operador. Consulta [Recopilar adhesiones voluntarias de usuarios]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins) y [Leyes y regulaciones]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).

### ¿Cuál es la diferencia entre SMS, MMS y RCS? {#what-is-the-difference-between-sms-mms-and-rcs}

SMS envía mensajes de solo texto, MMS añade contenido multimedia como imágenes, y RCS añade características enriquecidas como perfiles de remitente con marca y respuestas sugeridas en dispositivos compatibles. Consulta **Comparación de SMS, MMS y RCS** en una sección anterior de esta página.

### ¿Cómo configuro los números de remitente para SMS? {#how-do-i-configure-sender-numbers-for-sms}

Configura códigos abreviados, códigos largos o ID de remitente alfanuméricos en Braze antes de lanzar campañas. Consulta [Configuración de remitente]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).

## Próximos pasos {#next-steps}

- [Configuración de mensajes]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup)
- [Crear un mensaje]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create)