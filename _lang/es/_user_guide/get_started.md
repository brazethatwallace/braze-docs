---
nav_title: Comenzar
article_title: "Cómo empezar: Visión general de Braze"
page_order: 1
page_type: reference
description: "Familiarízate con los conceptos básicos que necesitarás conocer para trabajar con Braze."
---

# Cómo empezar: Visión general de Braze {#get-started-braze-overview}

> ¡Te damos la bienvenida a Braze! Esta colección de artículos te ayudará a iniciarte en nuestra plataforma y te presentará los términos, características y funcionalidades clave de Braze. Esta página presenta los conceptos básicos que necesitas para trabajar en Braze.

{% alert tip %}
Te recomendamos encarecidamente que consultes nuestro curso gratuito [Practitioner Learning Path](https://learning.braze.com/page/practitioner) junto con estos artículos. No se necesita ningún inicio de sesión ni cuenta especial. Si eres desarrollador y buscas un resumen técnico de Braze, consulta también <a href="/docs/developer_guide/getting_started/platform_overview">Cómo empezar para desarrolladores</a>.
{% endalert %}

En las secciones de Cómo empezar, nos centramos en las implementaciones habituales de Braze. Sin embargo, Braze es increíblemente flexible y puede personalizarse para aportar valor a tu organización de diversas maneras. Para mayor claridad y brevedad, hemos proporcionado una descripción general de la configuración predeterminada en lugar de ofrecer instrucciones rígidas. Reconocemos que cada organización tiene sus propias necesidades, y Braze está diseñado para satisfacer una amplia gama de opciones de personalización que pueden adaptarse a tus requisitos específicos.

Exploremos juntos el poder de Braze.

## Cómo funciona Braze {#how-braze-works}

Braze es una plataforma de interacción con los clientes que ayuda a marcas de todos los tamaños a crear campañas personalizadas y segmentadas a través de diversos canales. Braze te ofrece la capacidad de escuchar a tus clientes, comprender qué señala su comportamiento y luego actuar enviándoles el mensaje correcto, a través del canal adecuado, en el momento oportuno.

{% alert tip %}
Asegúrate de [añadir a tus compañeros a Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users) para que puedan explorar la plataforma contigo.
{% endalert %}

## Usuarios y Segments {#users-and-segments}

Los usuarios son tus clientes: las personas que reciben los mensajes que envías con Braze. Todos los datos que recopilas sobre un usuario e ingieres en Braze se almacenan en su perfil de usuario, como sus datos demográficos, información personal, preferencias y comportamientos. Esta información impulsa tu mensajería y es la forma en que puedes adaptar tus mensajes al usuario adecuado.

![Captura de pantalla relacionada con usuarios y Segments.]({% image_buster /assets/img/getting_started/user_profile.png %})

Los Segments dividen tu base de clientes en grupos más pequeños a los que luego puedes dirigirte con mensajes específicos. Puedes utilizar diferentes variables para crear Segments, que van desde características como género, ubicación y edad, hasta comportamientos como patrones de interacción con Campaigns anteriores o en qué punto del recorrido del cliente se encuentran.

Los Segments son dinámicos: los usuarios pueden entrar y salir de los Segments en tiempo real en función de su comportamiento y de su relación con tu marca. Esto garantiza que tus clientes reciban los mensajes más relevantes para ellos en todo momento. Puedes crear tantos Segments como necesites para tus propósitos de segmentación y mensajería.

![Los Segments son dinámicos: los usuarios pueden entrar y salir de los Segments en tiempo real en función de su comportamiento y de su relación con tu marca. Esto garantiza que tus clientes reciban los mensajes más relevantes para ellos en todo momento. Puedes crear tantos Segments como necesites para tus propósitos de segmentación y mensajería.]({% image_buster /assets/img/getting_started/segment.png %})

Para más información, consulta: [Cómo empezar: Usuarios y Segments]({{site.baseurl}}/user_guide/get_started/users_and_segments).

## Campaigns y Canvas {#campaigns-and-canvases}

Campaigns y Canvas son la forma en que envías mensajes a tus usuarios.

Las Campaigns son ideales para mensajes únicos enviados a un Segment de audiencia específico a través de varios canales. Puedes aprovechar cualquiera de nuestros canales de mensajería compatibles en tu Campaign (correo electrónico, push, In-App Messages, SMS y más).

Los Canvas son flujos de trabajo avanzados de Campaigns que te permiten automatizar y orquestar recorridos del cliente personalizados a través de múltiples canales. Dentro de un Canvas, puedes configurar lógica de ramificación, retrasos, puntos de decisión y eventos de conversión para guiar a los clientes a través de una serie de interacciones. Los Canvas ayudan a garantizar una comunicación consistente y fluida en diferentes puntos de intervención, aumentando las posibilidades de participación y conversión de los clientes.

Para más información, consulta: [Cómo empezar: Campaigns y Canvas]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases).

## Espacios de trabajo {#workspaces}

Los espacios de trabajo agrupan tus datos —usuarios, Segments, Campaigns y Canvas— en un solo lugar. La información no se comparte entre espacios de trabajo, así que tenlo en cuenta al añadir sitios web y aplicaciones a tus espacios de trabajo. Como buena práctica, te sugerimos agrupar solo versiones diferentes de las mismas aplicaciones o de aplicaciones muy similares en un mismo espacio de trabajo.

Ejemplos de uso de los espacios de trabajo:

- Diferentes líneas de producto o aplicaciones
- Diferentes audiencias (como repartidores frente a clientes)
- Negocios independientes
- Entorno de pruebas

Para más información, consulta: [Cómo empezar: Espacios de trabajo]({{site.baseurl}}/user_guide/get_started/workspaces).

## Integración de Braze {#integrating-braze}

Braze está diseñado para ponerse en marcha de forma rápida y sencilla. Nuestro tiempo medio de generación de valor es de seis semanas en nuestra base de clientes de cientos de marcas.

![Captura de pantalla relacionada con la integración de Braze.]({% image_buster /assets/img/getting_started/timetovalue.png %})

Este es el marco de Braze para estimar la duración de tu integración en función de cuatro componentes en los que puedes trabajar en paralelo. El rango típico es de 30 a 180 días, y la mayoría de las cuentas completan su integración en un plazo de 45 a 60 días.

- **Nivel de complejidad de la migración de Campaigns:** El tiempo que se tarda en migrar Campaigns depende de cuántas tengas, cuán personalizadas sean y de tus recursos. Si tienes menos de diez Campaigns que migrar, tardará menos de 60 días. Pero si tienes más de 100 Campaigns, será más complicado. No es lo mismo que una sola persona migre 100 Campaigns a que lo hagan 10 personas.

{% alert tip %}
¿Necesitas ayuda con tu migración? ¡Nuestros [partners certificados de Braze](https://www.braze.com/partners/solutions-partners) pueden ayudarte!
{% endalert %}

- **Volumen de correo electrónico:** Para enviar correos electrónicos, necesitarás calentar tus IP. El [calentamiento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) es el proceso de construir la reputación del remitente con tus direcciones IP recién asignadas. Si envías menos de 2-3 millones de correos electrónicos al día, tu calentamiento de IP debería tardar 30 días o menos. Ten en cuenta tu pico de envío. Si normalmente envías 2 millones de correos electrónicos al día pero planeas enviar 7 millones en un periodo estacional, ese envío "pico" es al que deberías calentar. Los remitentes de alto volumen pueden usar múltiples IP para acelerar el proceso de calentamiento.
- **Complejidad organizativa:** Nuestro proceso de incorporación puede adaptarse a las necesidades de tu negocio. Ya sea que tengas una sola unidad de negocio, un Centro de Excelencia, múltiples unidades independientes o uses agencias para reforzar tus equipos, Braze tiene experiencia trabajando en todos los escenarios.
- **Sofisticación de la infraestructura de datos:** Si solo estás implementando el SDK de Braze o ya tienes una plataforma de datos de los clientes (CDP), es posible tener todo configurado en solo 30 días. Usar una CDP moderna puede acelerar el proceso. Pero si tienes muchos sistemas de backend, herramientas o bases de datos que conectar con Braze, podría llevar más tiempo y necesitar más recursos dedicados para completar la configuración.

Para más información, consulta: [Cómo empezar: Resumen de la integración]({{site.baseurl}}/user_guide/get_started/integrations).