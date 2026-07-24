---
nav_title: Mayo
page_order: 8
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de mayo de 2019."
---

# Mayo de 2019 {#may-2019}

## Content Cards

Content Cards son contenidos persistentes que aparecen en las experiencias de aplicación y web de los clientes.

Con Content Cards, puedes enviar a tus clientes un flujo dinámico y muy específico de contenido enriquecido directamente desde las aplicaciones que les gustan, sin interrumpir su experiencia. También puedes combinar Content Cards con otros canales, como el correo electrónico o las notificaciones push, para habilitar estrategias de marketing cohesionadas.

![Fuente de Content Cards]({% image_buster /assets/img/cc-feed.png %}){: height="50%" width="50%"}

Además, Content Cards admiten más características personalizadas, como la fijación de tarjetas, el descarte de tarjetas, la entrega basada en API, tiempos de caducidad de tarjetas personalizados y análisis de tarjetas.

Utilízalas para crear centros de notificaciones, fuentes de páginas de inicio y fuentes de promociones.

Tendrás que actualizarte a una versión compatible del SDK de Braze:
- iOS: 3.8.0 o posterior
- Android: 2.6.0 o posterior
- Web: 2.2.0 o posterior

[¡Obtén más información sobre Content Cards aquí!]({{site.baseurl}}/user_guide/channels/content_cards)

{% alert update %}
Content Cards para Currents y la documentación de nuestra API para Content Cards se lanzarán a finales de esta semana. ¡Mantente al día!
{% endalert %}

## Incorporación a la plataforma Roku {#roku-platform-addition}

¡Braze ha añadido un nuevo canal a nuestras capacidades! Al expandirnos a nuevos canales, podemos habilitar a nuestros clientes para enriquecer sus datos mediante la comprensión del comportamiento del espectador o proporcionar experiencias significativas a sus consumidores en todos los canales relevantes.

Ahora puedes [recuperar datos de dispositivos Roku]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku) para el enriquecimiento de datos y el seguimiento de eventos personalizados.

## Preferencias de notificación para actualizaciones de Canvas o Campaigns {#notification-preferences-for-canvas-or-campaign-updates}

Esta [nueva notificación]({{site.baseurl}}/user_guide/administrative/company_settings/notification_preferences#notification-preferences) te avisará por correo electrónico cuando se active, actualice, reactive o desactive una Campaign o un Canvas. Actívala en **Preferencias de notificación** en tu cuenta de Braze.

## Documentación del partner tecnológico Jampp {#jampp-technology-partner-documentation}

Jampp es una plataforma de marketing del rendimiento para captar y reorientar clientes móviles. Combina datos de comportamiento con tecnología predictiva y programática para generar ingresos para los anunciantes mostrando anuncios personales y relevantes que inspiran a los consumidores a comprar por primera vez, o más a menudo.

Los clientes de Braze pueden [integrarse con Jampp]({{site.baseurl}}/partners/jampp) configurando el canal webhook de Braze para transmitir eventos a Jampp. Como resultado, los clientes tienen la posibilidad de añadir conjuntos de datos más ricos a sus iniciativas de reorientación con Jampp dentro del ecosistema de publicidad móvil.

## Selector de plataforma para mensajes dentro de la aplicación {#platform-picker-for-in-app-messages}

Hemos facilitado la selección de dónde van tus mensajes dentro de la aplicación y para qué plataformas se han creado con nuestro selector de plataformas, que enfatiza este paso en el proceso de creación de la Campaign.

![Selector de plataforma]({% image_buster /assets/img/iam_platforms.gif %})

## Campo de ID de envío de Currents para correo electrónico {#dispatch-id-currents-field-for-email}

{% alert update %}
El comportamiento de `dispatch_id` difiere entre Canvas y las Campaigns porque Braze trata los pasos en Canvas (excepto los pasos de entrada, que pueden programarse) como eventos desencadenados, incluso cuando están "programados". Más información sobre el [comportamiento de `dispatch_id`]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id) en Canvas y las Campaigns.

_Actualización anotada en agosto de 2019._
{% endalert %}

En nuestro esfuerzo por seguir mejorando las capacidades de Currents, vamos a añadir `dispatch_id` como campo a los eventos de correo electrónico de Currents en todos los tipos de conectores.

El `dispatch_id` es el ID único generado para cada transmisión, o envío, enviado desde la plataforma Braze.

Mientras que todos los clientes a los que se envía un mensaje programado reciben el mismo `dispatch_id`, los clientes que reciben mensajes basados en acciones o desencadenados por la API recibirán un `dispatch_id` único por mensaje. El campo `dispatch_id` te permite identificar qué instancia de una Campaign recurrente es responsable de la conversión, dotándote así de más información sobre qué tipos de Campaigns están ayudando a impulsar tus objetivos de negocio.

## Característica de clasificación "Mostrar solo las mías" en Campaigns {#only-show-mine-campaign-sorting-feature}

Cuando un usuario marca la casilla `Only Show Mine` en la cuadrícula de Campaigns, los resultados se filtrarán para mostrar únicamente las Campaigns creadas por el usuario conectado. Además, el usuario puede utilizar la barra de búsqueda introduciendo `created_by_me:true`.

¡Además, la barra lateral de la cuadrícula de Campaigns ahora es redimensionable!

## Eliminar usuarios por alias {#delete-users-by-alias}

¡Ahora puedes utilizar el endpoint `users/delete` para [eliminar usuarios por alias]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)!

## Cálculo único de clics y aperturas de correo electrónico {#unique-calculation-for-email-clicks-and-opens}

Los Unique Opens y los clics únicos para el correo electrónico ahora se capturan y muestran en un marco temporal de 7 días por usuario e incrementan un recuento de 1 dentro de esa ventana de 7 días, por cada `dispatch_id`.

El uso de `dispatch_id` permite que los mensajes recurrentes reflejen el verdadero recuento único de aperturas o clics de cada mensaje. Será fácil para los clientes hacer coincidir estos datos, ahora que `dispatch_id` está disponible en Currents.

Los usuarios que también utilicen Mailjet verán un repunte en estas cifras, ya que el plazo de unicidad anterior era de más de 30 días. Deberías haber sido informado de este cambio hace tres (3) semanas. Los clientes de SendGrid no deberían notar ninguna diferencia.

Puedes buscar estos términos actualizados en nuestro [glosario de métricas de informes]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

{% alert update %}
El comportamiento de `dispatch_id` difiere entre Canvas y las Campaigns porque Braze trata los pasos en Canvas (excepto los pasos de entrada, que pueden programarse) como eventos desencadenados, incluso cuando están "programados". [Más información sobre el comportamiento de `dispatch_id`]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id) en Canvas y las Campaigns.

_Actualización anotada en agosto de 2019._
{% endalert %}

## Canal más interactivo {#most-engaged-channel}

{% alert update %}
A partir de [la versión del producto de noviembre de 2019]({{site.baseurl}}/help/release_notes/2019/november#intelligence-suite), "Canal más interactivo" ha pasado a llamarse ["Canal inteligente"]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel).
{% endalert %}

El filtro Canal más interactivo selecciona la parte de tu audiencia para la que el canal de mensajería seleccionado es su "mejor" canal. En este caso, "mejor" significa "tiene la mayor probabilidad de participación, dado el historial del usuario". Puedes seleccionar como canal el correo electrónico, la notificación push web o la notificación push móvil (que incluye cualquier SO o dispositivo móvil disponible).

Echa un vistazo a este nuevo filtro en nuestra [biblioteca de filtros de segmentación]({{site.baseurl }}/user_guide/engagement_tools/segments/segmentation_filters/).