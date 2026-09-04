---
nav_title: "Configuración de RCS"
article_title: "Configuración de RCS"
page_order: 1
alias: /rcs_setup/
description: "Este artículo de referencia cubre los requisitos necesarios para poner en marcha RCS."
page_type: reference
channel:
  - RCS
---

# Configurar RCS {#set-up-rcs}

> Este artículo cubre los requisitos necesarios para poner en marcha tu canal RCS.

Configurar RCS es tan sencillo como configurar SMS. Sigue leyendo para aprender cómo puedes empezar a enviar mensajes enriquecidos e interactivos.

## Paso 1: Cumplir los criterios de elegibilidad {#step-1-meet-the-eligibility-criteria}

Para ser elegible para enviar RCS con Braze, tu empresa debe cumplir tres criterios de antemano:

1. Tu contrato actual de Braze debe incluir créditos de mensaje o de acción.
2. Debes enviar tus mensajes RCS a uno de los siguientes países compatibles con Braze:
- Estados Unidos
- Reino Unido
- Alemania
- México
- Suecia
- España
- Singapur
- Brasil
- Francia
- Italia
- Colombia
3. Debes adquirir uno o más SKU de RCS en tu contrato.

## Paso 2: Registrar un remitente verificado de RCS {#step-2-register-an-rcs-verified-sender}

Antes de poder enviar mensajes RCS, debes registrar un remitente verificado de RCS. Esta es la representación de tu marca que los usuarios ven en sus dispositivos móviles, e incluye el nombre de tu marca, el logotipo, una señal de verificación y un eslogan opcional. El remitente verificado de RCS refuerza la confianza del cliente y confirma que tus mensajes provienen de una fuente autenticada.

![Un ejemplo de remitente verificado de RCS en un mensaje RCS llamado "Cat Failz Cafe".]({% image_buster /assets/img/rcs/rcs_sender.png %}){: style="max-width:60%;"}

Después de que hayas añadido los SKU de RCS a tu formulario de pedido, Braze recibe la notificación y se pone en contacto contigo con la información de registro del remitente de RCS. El formato de estos depende de los países a los que desees enviar mensajes RCS.

Cuando hayas enviado tus formularios completados a Braze, Braze completa el proceso de registro en tu nombre.

### Paso 2.1: Configurar alternativas de SMS para los grupos de suscripción de RCS {#step-21-set-up-sms-fallbacks-for-rcs-subscription-groups}

Dado que la cobertura actual de los operadores varía según el país, y el hardware y software de los usuarios varían según cada individuo, la alternativa de SMS es un componente clave para tener un programa de RCS exitoso hoy en día. Recomendamos configurar la alternativa de SMS. Si un operador no es compatible con RCS o el dispositivo de un usuario no puede recibir mensajes RCS, la alternativa de SMS envía tu mensaje de todas formas, para que nunca pierdas un momento importante con tus usuarios.

Recomendamos encarecidamente revisar tu experiencia actual de adhesión voluntaria a SMS, los grupos de suscripción y la segmentación de audiencia antes de desplegar tu primera Campaign de RCS. Si es necesario, tu CSM siempre está disponible para orientarte y ayudarte a navegar el proceso de configuración.

#### Cómo funciona la alternativa de SMS con eventos y segmentación {#how-sms-fallback-works-with-events-and-segmentation}

{% tabs %}
{% tab Comportamiento de eventos %}

Cuando utilizas la alternativa de SMS con RCS, el comportamiento de los eventos depende de si el mensaje se envía correctamente a través de RCS o recurre a SMS:

- **Si el envío de RCS tiene éxito:** Recibes un evento de envío de RCS y un evento de entrega de RCS.
- **Si el envío de RCS recurre a SMS:** Recibes un evento de envío de RCS, un evento de rechazo de RCS y un evento de entrega de SMS. El evento de entrega de SMS tiene `IS_SMS_FALLBACK=TRUE`.

{% endtab %}
{% tab Comportamiento de segmentación %}

Para SMS y RCS, los [filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) de mensajes recibidos (como [Mensaje recibido de Campaign]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-campaign) y [Mensaje recibido de paso en Canvas]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-canvas-step)) se evalúan cuando se envía un mensaje, no cuando llega al dispositivo del usuario. Con la alternativa de SMS habilitada, los usuarios aún pueden coincidir con estos filtros si un mensaje RCS es rechazado y recurre a SMS, o si el SMS alternativo no se entrega al dispositivo del usuario.

{% endtab %}
{% endtabs %}

### Plazo para la aprobación del operador {#timeline-for-carrier-approval}

El plazo para la aprobación del operador varía según el país y también puede variar dentro de un mismo país. Ten en cuenta que el mercado de RCS aún está en sus inicios, por lo que los procesos de los operadores y agregadores están evolucionando rápidamente. En Estados Unidos, Braze estima que el tiempo de respuesta para la aprobación de un remitente verificado de RCS por parte del operador generalmente se encuentra en el rango de 4 a 6 semanas, con un remitente de prueba que normalmente se aprueba en una semana.

Cuando tu remitente verificado de RCS sea aprobado, nuestro equipo de operaciones actualiza tus grupos de suscripción según sea necesario para confirmar que incluyen el remitente de RCS.

## Paso 3: Configurar grupos de suscripción {#step-3-set-up-subscription-groups}

Dependiendo de tu integración, Braze puede añadir remitentes verificados de RCS a tus grupos de suscripción de SMS existentes o configurar nuevos. Para obtener instrucciones detalladas de configuración, consulta [Grupos de suscripción de SMS y RCS]({{site.baseurl}}/sms_rcs_subscription_groups).

## Migración del tráfico de SMS a RCS {#migrating-sms-traffic-to-rcs}

Si tienes grupos de suscripción de SMS y RCS separados, puedes migrar usuarios de SMS a RCS utilizando un Canvas de un solo paso. Para obtener instrucciones paso a paso, consulta [Migrar el tráfico de SMS a RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#migrate-sms-traffic-to-rcs).