---
nav_title: Correo electrónico
article_title: Correo electrónico
page_order: 3
page_type: landing
description: "Crea campañas de correo electrónico personalizadas en Braze con editores de arrastrar y soltar y HTML, gestión de suscripciones y más."
channel:
  - email
search_rank: 2
---

# Correo electrónico {#email}

> Con el correo electrónico en Braze, creas mensajes de correo electrónico personalizados en Campaigns o Canvas que llegan a los usuarios fuera de tu aplicación o sitio web. Este centro cubre la configuración del correo electrónico, los editores de arrastrar y soltar y HTML, la gestión de suscripciones, las plantillas y las pruebas para que puedas lanzar programas de correo electrónico conformes y alineados con tu marca. Usa las plantillas de correo electrónico de Braze o HTML personalizado para adaptar la voz y el diseño de tu marca. Empieza con [Configuración del correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup) si estás configurando un nuevo dominio de envío. Para ver ejemplos de campañas de correo electrónico, consulta los [casos de estudio](https://www.braze.com/customers/) de Braze.

## Requisitos previos {#prerequisites}

Antes de poder enviar correos electrónicos con Braze, necesitas configurar tus IP dedicadas, dominios, autenticación de correo electrónico y calentamiento de IP. Para una guía completa, consulta [Configuración del correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup).

## Personaliza tus correos electrónicos {#customize-your-emails}

Puedes personalizar tu mensajería de correo electrónico de diversas maneras, incluyendo:

- [Plantillas de correo electrónico de Braze]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template)
- [Plantillas HTML personalizadas]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template)
- [Bloques del editor (correo electrónico)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email)
- [Suscripciones de usuario]({{site.baseurl}}/user_guide/channels/email/subscriptions)
- [Grupos de suscripción]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups)

## Prueba tus correos electrónicos {#test-your-emails}

Los [grupos semilla]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups) envían automáticamente copias de tus campañas de correo electrónico a usuarios internos para realizar controles de calidad. Los correos electrónicos semilla incluyen `[SEED]` antepuesto a la línea del asunto para ayudarte a identificarlos.

## Ejemplos {#use-cases}

| Ejemplo | Explicación |
| --- | --- |
| Reactivación | Llega a los usuarios fuera de tu aplicación, incluidos aquellos que no la han instalado. |
| Incorporación | Incorpora y anima a los nuevos usuarios a activar las notificaciones push o a compartir la aplicación en las redes sociales. |
| Mensajes enriquecidos | Permite mensajes HTML enriquecidos y dinámicos. |
| Contenido multimedia | Facilita la colocación de contenido multimedia que atrae a los usuarios, como videos e imágenes. |
| Boletines informativos | Envía cómodamente boletines informativos mensuales o semanales para mantener la participación de los usuarios. |
| Transacciones | Notifica a los usuarios sobre compras recientes y entrega información importante sobre productos y envíos con [correos transaccionales]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email).
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ejemplos" }

## Servicios de correo electrónico {#email-services}

Si necesitas soporte adicional con tu programa de correo electrónico, Braze ofrece servicios recurrentes y puntuales con un coste adicional. Para más información, ponte en contacto con tu director de cuentas de Braze.

### Servicios de capacidad de entrega de correo electrónico {#email-deliverability-services}

Braze ofrece dos niveles de soporte recurrente de correo electrónico:
1. Deluxe
2. Estándar

Estos servicios pueden incluir:

- Auditoría de las prácticas históricas y actuales de envío de correo electrónico con una revisión de las estrategias de segmentación, cadencia y mensajería
- Configuración de lista de permitidos y plan personalizado de calentamiento de IP creado por un experto en capacidad de entrega de correo electrónico
  - Llamadas de seguimiento regulares durante tu primer mes (tres veces por semana para Deluxe y una vez por semana para Estándar)
- Llamadas regulares con un experto en capacidad de entrega (dos veces al mes para Deluxe y mensualmente para Estándar) para proporcionar:
  - Monitoreo del rendimiento de la capacidad de entrega por dominio
  - Recomendaciones para mejorar el rendimiento y los resultados del programa de correo electrónico utilizando datos y mejores prácticas establecidas
- Mitigar y remediar el triaje de crisis para eventos que generen problemas, como una lista de bloqueo de capacidad de entrega

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cómo configuro el envío de correo electrónico en Braze? {#how-do-i-set-up-email-sending-in-braze}

Configura las IP dedicadas, los dominios, la autenticación y el calentamiento de IP antes de tu primer envío. Consulta [Configuración del correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup) para ver la lista de verificación completa.

### ¿Cuál es la diferencia entre las suscripciones de usuario y los grupos de suscripción? {#what-is-the-difference-between-user-subscriptions-and-subscription-groups}

Las suscripciones de usuario controlan el estado global de adhesión voluntaria para un canal (por ejemplo, suscrito o cancelado de correo electrónico). Los grupos de suscripción permiten a los usuarios elegir categorías de mensajes específicas dentro de ese canal. Consulta [Suscripciones de usuario]({{site.baseurl}}/user_guide/channels/email/subscriptions) y [Grupos de suscripción]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).

### ¿Cómo puedo probar un correo electrónico antes de enviar una campaña? {#how-can-i-test-an-email-before-i-send-a-campaign}

Usa [grupos semilla]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups) para enviar copias de vista previa a revisores internos y confirmar la representación en diferentes clientes de correo electrónico.

## Próximos pasos {#next-steps}

- [Configuración del correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup)
- [Crear un correo electrónico con el editor de arrastrar y soltar]({{site.baseurl}}/user_guide/channels/email/drag_and_drop)
- [Crear un correo electrónico con el editor HTML]({{site.baseurl}}/user_guide/channels/email/html_editor)