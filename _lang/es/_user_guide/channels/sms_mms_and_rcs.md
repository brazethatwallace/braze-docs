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

> SMS (servicio de mensajes cortos), MMS (servicio de mensajería multimedia) y RCS (servicios de comunicación enriquecida) ofrecen una forma más directa de llegar a tus usuarios que la mayoría de los demás canales de mensajería, ya que utilizan números de teléfono para un alcance en tiempo real.

SMS sigue siendo uno de los canales más utilizados en todo el mundo —miles de millones de mensajes de texto se envían cada día— porque es rápido, directo y familiar para los clientes.

## Requisitos previos {#prerequisites}

La disponibilidad de SMS, MMS y RCS depende de tu paquete de Braze. Ponte en contacto con tu director de cuentas o administrador del éxito del cliente para comenzar.

Antes de empezar, asegúrate de tener lo siguiente:

- Códigos abreviados, códigos largos o identificadores de remitente alfanuméricos configurados. Para más información, consulta [Configuración del remitente]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/).
- Familiaridad con las leyes y regulaciones de SMS, incluidos los requisitos de TCPA y de los operadores. Para más información, consulta [Leyes y regulaciones]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/).
- Consentimiento explícito de adhesión voluntaria recopilado de los usuarios. Para más información, consulta [Recopilar adhesiones voluntarias de usuarios]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins/).

## Casos de uso {#use-cases}

| Caso de uso | Explicación |
| --- | --- |
| Recordatorios de citas | Envía recordatorios oportunos antes de las citas programadas, reduciendo las ausencias y manteniendo informados a los clientes. |
| Actualizaciones de pedidos | Notifica a los clientes sobre confirmaciones de pedidos, estado de envío y actualizaciones de entrega en tiempo real. |
| Autenticación de dos factores | Entrega códigos de verificación de un solo uso para el inicio de sesión en cuentas y la confirmación de transacciones. |
| Ofertas promocionales | Llega a los clientes con promociones de tiempo limitado, ventas flash y descuentos personalizados directamente en su teléfono. |
| Soporte al cliente | Habilita conversaciones bidireccionales para resolver consultas de clientes, recopilar comentarios o confirmar solicitudes de servicio. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso" }

## Comparación entre SMS, MMS y RCS {#sms-mms-and-rcs-compared}

- **SMS** entrega mensajes de solo texto de hasta 160 caracteres (o 70 caracteres con Unicode). Es compatible de forma universal con todos los dispositivos móviles y operadores.
- **MMS** amplía SMS con soporte para contenido multimedia, incluidas imágenes, GIF y audio. MMS requiere compatibilidad del operador y del dispositivo.
- **RCS** es la próxima generación de mensajería empresarial, y ofrece características enriquecidas como perfiles de remitente con marca, respuestas sugeridas, carruseles y confirmaciones de lectura. La disponibilidad de RCS depende de la compatibilidad del operador y del dispositivo.

### ¿Por qué usar RCS? {#why-use-rcs}

RCS (servicios de comunicación enriquecida) se basa en SMS con una experiencia más rica y similar a una aplicación en la aplicación de mensajería predeterminada de los dispositivos compatibles. Las marcas usan RCS para:

- Entregar imágenes y video de alta resolución en lugar de solo texto plano.
- Agregar respuestas y acciones sugeridas para que los clientes puedan responder con un solo toque.
- Mostrar un perfil de remitente verificado con marca para que los mensajes resulten fáciles de confiar.
- Admitir confirmaciones de lectura e indicadores de escritura donde los operadores lo permitan.

RCS es adecuado para casos de uso como actualizaciones transaccionales (envíos, citas), promociones con contenido creativo enriquecido, soporte al cliente con rutas de respuesta rápida, e incorporación o tutoriales que se benefician de medios y acciones estructuradas. Para la configuración y migración desde SMS, consulta [Configuración de RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup/).

## Próximos pasos {#next-steps}

- [Configuración de mensajes]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/)
- [Crear un mensaje]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/)