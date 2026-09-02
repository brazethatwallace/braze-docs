---
nav_title: Resumen de la plataforma
article_title: Resumen de la plataforma
page_order: 1
description: "En este artículo se cubren las partes básicas y las capacidades de la plataforma Braze. Los enlaces de este artículo conectan con temas esenciales de Braze."
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer){: style="float:right;width:120px;border:0;" class="noimgborder"}Primeros pasos: Resumen de la plataforma {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecompathdeveloper-stylefloatrightwidth120pxborder0-classnoimgbordergetting-started-platform-overview}

> En este artículo se cubren las partes básicas y las capacidades de la plataforma Braze. Los enlaces de este artículo conectan con temas esenciales de Braze.

{% alert tip %}
Echa un vistazo a nuestro curso gratuito [Ruta de aprendizaje para desarrolladores](https://learning.braze.com/path/developer) junto con estos artículos.
{% endalert %}

## ¿Qué es Braze? {#what-is-braze}

Braze es una plataforma de interacción con los clientes. Ingesta datos de usuario, muestra sus acciones y comportamientos, y te permite actuar en consecuencia. La plataforma tiene tres componentes principales: el SDK or kit de desarrollo de software, el dashboard y la REST or transferencia de estado representacional API.

Si eres especialista en marketing y buscas un resumen más general de Braze, consulta la [sección Primeros pasos para especialistas en marketing]({{site.baseurl}}/user_guide/get_started).

![Braze tiene diferentes capas. En total, consta del SDK, la API, el dashboard y las integraciones de socios. Cada una de ellas aporta partes de una capa de ingesta de datos, una capa de clasificación, una capa de orquestación, una capa de personalización y una capa de acción. La capa de acción tiene varios canales, como push, mensajes dentro de la aplicación, Catálogo conectado, webhook, SMS y correo electrónico.]({% image_buster /assets/img/getting-started/getting-started-vertically-integrated-stack.png %}){: style="max-width:55%;float:right;margin-left:15px;"}

### SDK or kit de desarrollo de software

Los [SDK or kit de desarrollo de software de Braze](#integrating-braze) pueden integrarse en tus aplicaciones móviles y web para proporcionar potentes herramientas de marketing, gestión de usuarios y análisis.

En resumen, cuando está totalmente integrado, el SDK or kit de desarrollo de software:

* Recoge y sincroniza los datos de usuario en un perfil de usuario consolidado
* Recoge automáticamente datos de sesión, información del dispositivo y tokens de notificaciones push
* Captura datos de interacción de marketing y datos personalizados específicos de tu empresa
* Está diseñado para la seguridad y sometido a pruebas de penetración por terceros
* Está optimizado para dispositivos con poca batería o red lenta
* Admite firmas JWT en el servidor para mayor seguridad
* Tiene acceso de solo escritura a tus sistemas (no puede recuperar datos de usuario)
* Potencia las notificaciones push, los mensajes dentro de la aplicación y los canales de mensajería de Content Cards

### Interfaz de usuario del dashboard {#dashboard-user-interface}

El dashboard es la interfaz de usuario que controla todos los datos e interacciones en el corazón de la plataforma Braze. Los especialistas en marketing utilizarán el dashboard para hacer su trabajo y crear contenidos. Los desarrolladores utilizan el dashboard para administrar la configuración para integrar aplicaciones, como claves de API y credenciales de notificación push.

Si acabas de empezar, el administrador de tu equipo debería añadirte a ti (y a todos los demás miembros del equipo que necesiten acceso a Braze) como [usuarios en tu dashboard]({{site.baseurl}}/user_guide/administer/personal).

### REST or transferencia de estado representacional API

La API de Braze te permite mover datos dentro y fuera de Braze a escala. Utiliza la API para traer actualizaciones de tu backend, almacenes de datos y otras fuentes propias y de terceros. Además, utiliza la API para añadir eventos personalizados con fines de segmentación directamente desde aplicaciones basadas en web. Puedes desencadenar y enviar mensajes a través de la API, lo que permite a los recursos técnicos incluir metadatos JSON complejos como parte de tus campañas.

La API también proporciona un servicio web en el que puedes registrar las acciones realizadas por tus usuarios directamente a través de HTTP, en lugar de a través de los SDK or kit de desarrollo de software móviles y web. Combinado con webhooks, esto significa que puedes hacer un seguimiento de las acciones y desencadenar actividades para los usuarios dentro y fuera de la experiencia de la aplicación. La [guía de la API]({{site.baseurl}}/api/home) enumera los puntos finales de la API de Braze disponibles y sus usos.

Para saber más sobre las partes y piezas de Braze, consulta: [Primeros pasos: Resumen de la arquitectura]({{site.baseurl}}/developer_guide/getting_started/architecture_overview).

## Análisis de datos y acción {#data-analysis-and-action}

Los datos almacenados en Braze se conservan y pueden utilizarse para segmentación, personalización y orientación mientras seas cliente de Braze. Eso te permite actuar sobre los datos de perfil de usuario (por ejemplo, la actividad de la sesión o las compras) hasta que decidas eliminar esa información. Por ejemplo, un servicio de streaming podría hacer un seguimiento de los contenidos vistos por cada suscriptor desde su primer día en el servicio (aunque fuera hace muchos años) y utilizar esos datos para impulsar la mensajería relevante.

![Un segmento en el dashboard de Braze llamado «Compradores recientes» yuxtapuesto junto a una pantalla de teléfono que muestra un correo electrónico de «Principales recomendaciones para Linda».]({% image_buster /assets/img/getting-started/getting-started-segment.png %}){: style="max-width:80%"}

### Análisis de la aplicación {#app-analytics}

El dashboard de Braze muestra gráficos actualizados en tiempo real basados en métricas de análisis y eventos personalizados que tú implementas. La medición y optimización constantes mediante pruebas A/B, informes personalizados, análisis e inteligencia automatizada te ayudan a fomentar la interacción con los clientes y la diferenciación.

### Segmentación de usuarios {#user-segmentation}

La segmentación te permite crear grupos de usuarios basados en potentes filtros de su comportamiento dentro de la aplicación, datos demográficos y similares. Braze también te permite definir cualquier acción del usuario dentro de la aplicación como un «evento personalizado» si la acción deseada no se captura de forma predeterminada. Lo mismo ocurre con las características del usuario mediante «atributos personalizados». Una vez creado un segmento de usuarios en el dashboard, tus usuarios entrarán y saldrán del segmento a medida que cumplan (o no) los criterios definidos. Por ejemplo, puedes crear un segmento que incluya a todos los usuarios que han gastado dinero in-app y que utilizaron la aplicación por última vez hace más de dos semanas.

Para saber más sobre nuestros modelos de datos, consulta: [Primeros pasos: Resumen de análisis]({{site.baseurl}}/developer_guide/getting_started/architecture_overview).

## Mensajería multicanal {#multichannel-messaging}

Después de definir un segmento, las herramientas de mensajería de Braze te permiten interactuar con tus usuarios de forma dinámica y personalizada. Braze se diseñó con un modelo de datos independiente del canal y centrado en el usuario. La mensajería se realiza dentro de tu aplicación o sitio web (como el envío de mensajes dentro de la aplicación o a través de elementos gráficos como carruseles de Content Cards y banners) o fuera de la experiencia de la aplicación (como el envío de notificaciones push o correos electrónicos). Por ejemplo, tus especialistas en marketing pueden enviar una notificación push y un correo electrónico al segmento de ejemplo definido en la sección anterior.

![Crea y desencadena mensajes personalizados en cualquier canal, ya sea fuera o dentro de tu aplicación o sitio web.]({% image_buster /assets/img/getting-started/messaging-channels.png %}){: style="border:none" }

| Canal                                                                                              | Descripción                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)* | Envía notificaciones in-app dinámicas y altamente segmentadas sin interrumpir al cliente. |
| [Correo electrónico]({{site.baseurl}}/user_guide/channels/email) | Envía mensajes HTML enriquecidos creando tu correo electrónico con el editor de texto enriquecido, nuestro editor de arrastrar y soltar, o cargando una de tus plantillas HTML existentes. |
| [In-App Messages]({{site.baseurl}}/in-app_messages) | Envía notificaciones discretas dentro de la aplicación utilizando la interfaz de usuario nativa personalizada de Braze. |
| [Push]({{site.baseurl}}/user_guide/channels/push) | Desencadena automáticamente notificaciones push de campañas de mensajería o noticias utilizando el servicio de notificaciones push de Apple (APNs) para iOS o Firebase Cloud Messaging (FCM) para Android. |
| [servicio de mensajes cortos, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)* | Utiliza servicio de mensajes cortos, MMS o RCS para enviar notificaciones transaccionales, compartir promociones, enviar recordatorios y mucho más. |
| [Notificación push web]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web) | Envía notificaciones al navegador web, aunque tus usuarios no estén activos en tu sitio. |
| [Webhooks]({{site.baseurl}}/about_webhooks) | Utiliza webhooks para desencadenar acciones no relacionadas con la aplicación, proporcionando a otros sistemas y aplicaciones datos en tiempo real. |
| [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)* | Conecta directamente con tus usuarios y clientes aprovechando la popular plataforma de mensajería entre iguales: WhatsApp. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mensajería multicanal" }

<sup>*Disponible como característica adicional.*</sup>

### Componentes personalizables {#customizable-components}

{% gallery %}
{{site.baseurl}}/assets/img/getting-started/crawl-example.png <br> Todos los componentes de Braze están diseñados para ser accesibles, adaptables y personalizables. Puedes empezar con Braze utilizando los componentes predeterminados de `BrazeUI` y personalizándolos para adaptarlos a las necesidades de tu marca y a tus casos de uso.
{{site.baseurl}}/assets/img/getting-started/walk-example.png <br> Para ir más allá de las opciones predeterminadas, puedes escribir código personalizado para actualizar el aspecto de un canal de mensajería para que se ajuste más a tu marca. Esto incluye cambiar el tipo de letra, el tamaño de letra y los colores de un componente. Los especialistas en marketing mantienen el control de la audiencia, el contenido, el comportamiento al hacer clic y la caducidad directamente en el dashboard de Braze.
{{site.baseurl}}/assets/img/getting-started/run-example.png <br> También puedes crear componentes completamente personalizados para controlar el aspecto de tu mensajería, cómo se comporta y cómo interactúa con otros canales de mensajería (por ejemplo, desencadenar una Content Card basada en una notificación push). Braze proporciona métodos del SDK que te permiten registrar métricas como impresiones, clics y descartes en el dashboard de Braze. Cada canal de mensajería dispone de un artículo de análisis para facilitar esta tarea.
{% endgallery %}

<br>
<br>

## Integración de Braze {#integrating-braze}

Braze está diseñado para una integración rápida. El tiempo medio de obtención de valor es de seis semanas en toda nuestra base de clientes. Para obtener más información sobre el proceso de integración, consulta [Primeros pasos: Resumen de la integración]({{site.baseurl}}/developer_guide/getting_started/integration_overview).

## Recursos para marcar {#resources-to-bookmark}

Como recurso técnico, participarás en muchos de los aspectos prácticos de Braze. Aquí tienes buenos recursos para agregar a marcadores fuera de nuestra documentación. A medida que vayas avanzando, ten a mano nuestro glosario de [Términos que debes conocer]({{site.baseurl}}/user_guide/get_started/terms_to_know) en caso de que tengas preguntas sobre términos de Braze.

| Recurso | Lo que aprenderás |
|---|---|
| [Depuración del SDK or kit de desarrollo de software]({{site.baseurl}}/developer_guide/sdk_integration/debugging) | A la hora de solucionar problemas de integración, la herramienta de depuración del SDK or kit de desarrollo de software te resultará muy útil. ¡Asegúrate de tenerla a mano! |
| [GitHub público de Braze](https://github.com/braze-inc/) | Encontrarás información detallada sobre la integración y código de muestra en nuestro repositorio de GitHub. |
| [Repositorio de GitHub del SDK or kit de desarrollo de software de Android](https://github.com/braze-inc/braze-android-sdk/) | El repositorio de GitHub del SDK or kit de desarrollo de software de Android. |
| [Referencia del SDK or kit de desarrollo de software de Android](https://appboy.github.io/appboy-android-sdk/kdoc/index.html) | Documentación de clases para el SDK or kit de desarrollo de software de Android. |
| [Repositorio de GitHub del SDK or kit de desarrollo de software para iOS (Swift)](https://github.com/braze-inc/braze-swift-sdk) | El repositorio de GitHub del SDK or kit de desarrollo de software de Swift. |
| [Referencia del SDK or kit de desarrollo de software de iOS (Swift)](https://braze-inc.github.io/braze-swift-sdk/) | Documentación de clases para el SDK or kit de desarrollo de software de iOS. |
| [Repositorio de GitHub del SDK or kit de desarrollo de software Web](https://github.com/braze-inc/braze-web-sdk) | El repositorio de GitHub del SDK or kit de desarrollo de software Web. |
| [Referencia del SDK or kit de desarrollo de software Web](https://js.appboycdn.com/web-sdk/5.0/doc/modules/braze.html) | Documentación de clases para el SDK or kit de desarrollo de software Web. |
| [Registros de cambios del SDK or kit de desarrollo de software]({{site.baseurl}}/developer_guide/changelogs) | Braze tiene lanzamientos mensuales predecibles, además de lanzamientos para cualquier problema crítico y actualizaciones importantes del SO. |
| [Colección Postman de la API de Braze](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest) | Descarga aquí nuestra colección de Postman.  |
| [Monitor de estado del sistema Braze](https://braze.statuspage.io/) | Nuestra página de estado se actualiza siempre que hay incidentes o interrupciones. Ve a esta página para suscribirte a las alertas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Recursos para marcar" }