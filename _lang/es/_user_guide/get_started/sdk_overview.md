---
nav_title: Visión general del SDK
article_title: Resumen del SDK
page_order: 9
page_type: reference
description: "Este artículo de referencia cubre los aspectos básicos del SDK de Braze."
---

# Visión general del SDK {#sdk-overview}

> El SDK de Braze recopila datos de sesión, identifica a los usuarios y registra las compras y los eventos personalizados a través de tu sitio web o aplicación. También puedes utilizar el SDK para interactuar con los usuarios enviando mensajes dentro de la aplicación y notificaciones push directamente desde el dashboard de Braze.

En resumen, el SDK de Braze:
* Recoge y sincroniza los datos de los usuarios en un perfil de usuario consolidado
* Captura datos de interacción de marketing y datos personalizados específicos de tu empresa
* Potencia las notificaciones push, los mensajes dentro de la aplicación y los canales de mensajería de Content Cards

## ¿Qué es un SDK? {#what-is-an-sdk}
Un SDK (SDK) es un conjunto de herramientas prefabricadas&mdash;pequeños bloques de código&mdash;que pueden añadirse a las aplicaciones digitales para dar soporte a nuevas capacidades. El SDK de Braze se utiliza para enviar y obtener información desde y hacia tu aplicación o sitio web. Está diseñado para ofrecer funciones esenciales desde el principio: creación de perfiles de usuario, registro de eventos personalizados, activación de notificaciones push, etc.

Como esta funcionalidad viene por defecto de Braze, tus desarrolladores quedan libres para centrarse en tu negocio principal. Sin un SDK, cada cliente de Braze tendría que crear toda la infraestructura y herramientas para el procesamiento de datos, lógica de segmentación, opciones de entrega, gestión de usuarios anónimos, análisis de campañas y mucho más completamente desde cero. Eso llevaría mucho más tiempo y sería mucho más molesto que la hora aproximada que se tarda en incorporar nuestro SDK.

## Implementación {#implementation}

Para incorporar un SDK a tu aplicación o sitio web, alguien tendrá que añadir el código del SDK a la base de código general de la aplicación. Esto significa que tu equipo de ingeniería estará implicado, básicamente uniendo nuestras aplicaciones para que la información y las acciones fluyan entre ellas. Pero aunque tus desarrolladores estén implicados, el SDK está diseñado para ser ligero y fácil de integrar.

Para ahorrarte tiempo y garantizar una integración sin problemas, te recomendamos que tú y tu equipo de ingeniería configuren los eventos personalizados, los atributos personalizados y el SDK al mismo tiempo. Obtén más información sobre los pasos que tus equipos de marketing e ingeniería tendrán que pensar juntos leyendo nuestro [artículo sobre implementación]({{site.baseurl}}/user_guide/get_started/integrations).

## Agregación de datos {#data-aggregation}

El SDK de Braze captura automáticamente datos a nivel de usuario, lo que te proporciona métricas clave para tu aplicación y tu base de usuarios. Agrupa aplicaciones similares en un único espacio de trabajo (por ejemplo, las versiones para iOS y Android juntas) para ver los datos recopilados en todas las plataformas y obtener una visión completa de la actividad de los usuarios. Para más información, consulta el artículo de la [página de inicio]({{site.baseurl}}/user_guide/analytics/dashboards/home).

## Mensajería dentro de la aplicación {#in-app-messaging}

Utiliza el SDK para redactar y enviar mensajes dentro de la aplicación directamente. Puedes elegir mensajes de deslizamiento hacia arriba, modales o a pantalla completa en función de la estrategia de tu campaña. Para obtener más información sobre la composición, consulta [Crear un mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).

![Notificación push visualizada en un navegador web]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## Notificaciones push {#push-notifications}

Las notificaciones push son otra gran opción para interactuar con tus usuarios y son especialmente útiles para gestionar llamadas a la acción urgentes. Las notificaciones push móviles aparecen en los dispositivos de tus usuarios, y las notificaciones push web aparecen incluso cuando tu sitio no está abierto. Para más información sobre el uso de las notificaciones push, consulta nuestro [artículo sobre notificaciones push]({{site.baseurl}}/user_guide/channels/push).

Los usuarios de tu sitio web o aplicación deben aceptar recibir notificaciones push. Para más detalles, consulta [preparación para las notificaciones push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

## Reglas de segmentación y entrega {#segmentation-and-delivery-rules}

Por defecto, una campaña que contenga mensajes dentro de la aplicación se enviará a todas las versiones de la aplicación en ese espacio de trabajo. Por ejemplo, el mensaje se enviará tanto a usuarios web como de móvil. Para enviar un mensaje dentro de la aplicación solo a web o móvil, tendrás que segmentar tu campaña en consecuencia, lo que se admite por defecto a través del SDK de Braze.

Puedes crear un segmento de tus usuarios web configurando **Apps and websites targeted** a **Users from specific apps** y, a continuación, seleccionando solo tu sitio web para las **Specific Apps**.

![Página de detalles del segmento con la aplicación web en primer plano]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

Esto te permitirá dirigirte a los usuarios en función de su comportamiento de forma inteligente. Si quisieras dirigirte a usuarios web para animarles a descargar tu aplicación móvil, crearías este segmento como tu audiencia objetivo. Si quisieras enviar una campaña de mensajería que incluya un mensaje dentro de la aplicación en móvil, pero no en web, tendrías que desmarcar el icono de tu sitio web en tu segmento.

## Plataformas compatibles {#supported-platforms}

Braze ofrece SDK para múltiples plataformas, como Web, Android y Swift. Para ver la lista completa, consulta la [Guía para desarrolladores de Braze]({{site.baseurl}}/developer_guide/home).