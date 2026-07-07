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
Te recomendamos encarecidamente que consultes nuestro curso gratuito [Practitioner Learning Path](https://learning.braze.com/page/practitioner) junto con estos artículos. No se necesita ningún inicio de sesión ni cuenta especial. Si eres desarrollador y buscas un resumen técnico de Braze, consulta también [Cómo empezar para desarrolladores]({{site.baseurl}}/developer_guide/getting_started/platform_overview).
{% endalert %}

En las secciones de Cómo empezar, nos centramos en las implementaciones habituales de Braze. Sin embargo, Braze es increíblemente flexible y puede personalizarse para aportar valor a tu organización de diversas maneras. Para mayor claridad y brevedad, hemos proporcionado una descripción general de la configuración predeterminada en lugar de ofrecer instrucciones rígidas. Reconocemos que cada organización tiene sus propias necesidades, y Braze está diseñado para satisfacer una amplia gama de opciones de personalización que pueden adaptarse a tus requisitos específicos.

Exploremos juntos el poder de Braze.

## Cómo funciona Braze {#how-braze-works}

Braze es una plataforma de interacción con los clientes que ayuda a marcas de todos los tamaños a crear campañas personalizadas y dirigidas a través de diversos canales. Braze te ofrece la posibilidad de escuchar a tus clientes, comprender lo que su comportamiento está indicando y, a continuación, actuar enviándoles el mensaje adecuado, a través del canal adecuado, en el momento adecuado.

{% alert tip %}
Asegúrate de [añadir a tus colegas a Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users) para que puedan explorar la plataforma contigo.
{% endalert %}

## Usuarios y segmentos {#users-and-segments}

Los usuarios son tus clientes, las personas que reciben los mensajes que envías con Braze. Todos los datos que recopilas sobre un usuario e ingieres en Braze se almacenan en su perfil de usuario, como sus datos demográficos, información personal, preferencias y comportamientos. Esta información potencia tu mensajería y es la forma en que puedes adaptar tus mensajes al usuario adecuado.

![Captura de pantalla relacionada con usuarios y segmentos.]({% image_buster /assets/img/getting_started/user_profile.png %})

Los segmentos dividen tu base de clientes en grupos más pequeños a los que puedes dirigirte con mensajes específicos. Puedes utilizar diferentes variables para crear segmentos, desde características como género, ubicación y edad hasta comportamientos como patrones de interacción con Campaigns anteriores o en qué punto del recorrido del cliente se encuentran.

Los segmentos son dinámicos: los usuarios pueden entrar y salir de ellos en tiempo real en función de su comportamiento y de su relación con tu marca. Esto garantiza que tus clientes reciban los mensajes más relevantes para ellos en cada momento. Puedes crear tantos segmentos como necesites para tus objetivos de segmentación y mensajería.

![Los segmentos son dinámicos: los usuarios pueden entrar y salir de ellos en tiempo real en función de su comportamiento y de su relación con tu marca. Esto garantiza que tus clientes reciban los mensajes más relevantes para ellos en cada momento. Puedes crear tantos segmentos como necesites para tus objetivos de segmentación y mensajería.]({% image_buster /assets/img/getting_started/segment.png %})

Para más información, consulta: [Cómo empezar: Usuarios y segmentos]({{site.baseurl}}/user_guide/get_started/users_and_segments).

## Campaigns y Canvas {#campaigns-and-canvases}

Campaigns y Canvas son la forma de enviar mensajes a tus usuarios.

Las Campaigns son ideales para mensajes únicos enviados a un segmento de audiencia específico a través de varios canales. Puedes aprovechar cualquiera de nuestros canales de mensajería compatibles en tu Campaign (correo electrónico, push, In-App Messages, SMS y más).

Los Canvas son flujos de trabajo avanzados de Campaigns que te permiten automatizar y orquestar recorridos personalizados del cliente a través de múltiples canales. Dentro de un Canvas, puedes configurar lógica de ramificación, retrasos, puntos de decisión y eventos de conversión para guiar a los clientes a través de una serie de interacciones. Los Canvas ayudan a garantizar una comunicación coherente y fluida en los distintos puntos de intervención, lo que aumenta las posibilidades de interacción y conversión de los clientes.

Para más información, consulta: [Cómo empezar: Campaigns y Canvas]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases).

## Espacios de trabajo {#workspaces}

Los espacios de trabajo agrupan tus datos —usuarios, segmentos, Campaigns y Canvas— en una única ubicación. La información no se comparte entre espacios de trabajo, así que tenlo en cuenta cuando añadas sitios web y aplicaciones a tus espacios de trabajo. Como práctica recomendada, sugerimos agrupar en un mismo espacio de trabajo solo diferentes versiones de la misma aplicación o de aplicaciones muy similares.

Ejemplos de uso de los espacios de trabajo:

- Diferentes líneas de productos o aplicaciones
- Diferentes audiencias (como conductores de reparto frente a clientes)
- Empresas separadas
- Entorno de pruebas

Para más información, consulta: [Cómo empezar: Espacios de trabajo]({{site.baseurl}}/user_guide/get_started/workspaces).

## Integración de Braze {#integrating-braze}

Braze está diseñado para ponerse en marcha rápida y fácilmente. Nuestro tiempo medio de creación de valor es de seis semanas en nuestra base de clientes de cientos de marcas.

![Captura de pantalla relacionada con la integración de Braze.]({% image_buster /assets/img/getting_started/timetovalue.png %})

Este es el marco de Braze para estimar la duración de tu integración basándose en cuatro componentes en los que puedes trabajar en paralelo. El intervalo típico es de 30 a 180 días, y la mayoría de las cuentas completan su integración en un plazo de 45 a 60 días.

- **Nivel de complejidad de la migración de Campaigns:** El tiempo que se tarda en migrar las Campaigns depende de cuántas tengas, de lo personalizadas que estén y de tus recursos. Si tienes menos de diez Campaigns que migrar, tardarás menos de 60 días. Pero si tienes más de 100 Campaigns, será más complicado. No es lo mismo que una sola persona migre 100 Campaigns a que lo hagan 10 personas.

{% alert tip %}
¿Necesitas ayuda con tu migración? Nuestros [socios certificados de Braze](https://www.braze.com/partners/solutions-partners) pueden ayudarte.
{% endalert %}

- **Volumen de correo electrónico:** Para enviar correos electrónicos, tendrás que calentar tus IP. El [calentamiento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) es el proceso de construir la reputación del remitente con tus direcciones IP recién asignadas. Si envías menos de 2-3 millones de correos electrónicos al día, el calentamiento de tu IP debería tardar 30 días o menos. Ten en cuenta tu pico de envío. Si normalmente envías 2 millones de correos electrónicos al día pero planeas enviar 7 millones durante un período estacional, ese «pico» de envíos es al que deberías calentar. Los remitentes de gran volumen pueden utilizar varias IP para acelerar el proceso de calentamiento.
- **Complejidad organizativa:** Nuestro proceso de incorporación puede adaptarse a las necesidades de tu empresa. Tanto si se trata de una única unidad de negocio, como si tienes un Centro de Excelencia, varias unidades independientes o utilizas agencias para reforzar tus equipos, Braze tiene experiencia trabajando en todos los escenarios.
- **Sofisticación de la infraestructura de datos:** Si solo estás implementando el SDK de Braze o ya tienes una plataforma de datos de los clientes (CDP), es posible tenerlo todo configurado en solo 30 días. Usar un CDP moderno puede acelerar el proceso. Pero si tienes muchos sistemas backend, herramientas o bases de datos que conectar con Braze, puede llevar más tiempo y necesitar más recursos dedicados para terminar la configuración.

Para más información, consulta: [Cómo empezar: Resumen de la integración]({{site.baseurl}}/user_guide/get_started/integrations).