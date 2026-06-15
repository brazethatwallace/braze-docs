---
nav_title: Buenas prácticas
article_title: Buenas prácticas para campañas
page_order: 0
description: "Este artículo ofrece buenas prácticas para crear y personalizar tus campañas."
tool: Campaign

---

# Buenas prácticas para campañas {#campaign-best-practices}

> Este artículo ofrece buenas prácticas para crear y personalizar tus campañas.

## Las cuatro T de Braze {#four-ts-of-braze}

Braze recomienda que solo envíes datos de clientes que tengas la intención de utilizar en la plataforma de Braze. Considera la filosofía de las "Cuatro T de Braze" para asegurarte de que solo envías datos que utilizarás para:

- **Target (segmentar)** tus audiencias creando [segmentos de audiencia]({{site.baseurl}}/user_guide/audience/segments/).
- **Trigger (desencadenar)** tus mensajes con entrega [basada en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/#action-based-delivery) o [desencadenada por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/).
- **Template (personalizar)** tus mensajes con [lógica condicional Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/).
- **Track (rastrear)** la eficacia de tus campañas con [seguimiento de conversiones]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/).

Esto te permite optimizar los datos que envías a Braze y agilizar tu capacidad de enviar mensajes a tus usuarios, al tiempo que evitas el seguimiento de puntos de datos que tu equipo podría no considerar útiles a largo plazo.

## Segmentación de usuarios {#user-targeting}

A medida que desarrollas tus campañas con el tiempo, es posible que notes caídas en tu audiencia. En este punto crucial, puedes dirigirte a tus [usuarios inactivos]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/capturing_lapsing_users/) con una campaña especializada utilizando segmentación.

### Identifica tu audiencia {#identify-your-audience}

Aprovecha los segmentos y filtros a tu favor definiendo tu audiencia. Considera a quién se dirigen tu campaña y tus mensajes. Con esta información clave, puedes crear [campañas multicanal]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/#multichannel-campaigns) que ofrecen la flexibilidad de construir tus mensajes en diferentes canales para adaptarse a las preferencias de notificación de tu audiencia.

También es importante comprender a tus [usuarios activos]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/active_user_campaigns/) para mostrar tu agradecimiento a tus usuarios más constantes.

## Campañas multicanal {#multichannel-campaigns}

### Conocimiento de características {#feature-awareness}

Si tu objetivo es atraer a tus usuarios hacia una nueva característica o versión de la aplicación, utiliza una estrategia multicanal con enfoque en canales dentro de la aplicación. Los [mensajes dentro de la aplicación]({{site.baseurl}}/in-app_messages/) y las [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/) son generalmente menos intrusivos si un usuario no desea actualizar de inmediato.

Asegúrate de incluir [vínculos profundos]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/) a la tienda de aplicaciones correspondiente.

Convencer a los usuarios de que actualicen su aplicación o cambien la forma en que la usan puede ser difícil, así que infórmales sobre todos los beneficios de la nueva versión o características y cómo mejorará su experiencia con tu aplicación.

### Momento de envío {#send-timing}

¡El momento es clave! Cuando tu objetivo es convencer a los usuarios de que actualicen su aplicación, espera hasta que tengan una experiencia positiva dentro de la aplicación para pedírselo. Para mantener a tu audiencia interesada, evita mensajes repetitivos que puedan parecer intrusivos.

Con el tiempo, tus usuarios pueden olvidar ciertas características o no notar las nuevas. Cuando se añadan nuevas características, asegúrate de informar a tus usuarios con [mensajes dentro de la aplicación]({{site.baseurl}}/in-app_messages/). Si los usuarios no están interactuando con características importantes dentro de la aplicación, puede ser mejor recordárselo cuando estén usando tu aplicación y cuando esta nueva característica les resulte útil. Nuestro artículo sobre [adhesión voluntaria de datos]({{site.baseurl}}/user_guide/channels/content_cards/) tiene más información sobre cómo asegurar que tu solicitud se ajuste a las expectativas del flujo de trabajo de los usuarios.

## Calificaciones altas {#high-ratings}

Obtener calificaciones de cinco estrellas en la tienda de aplicaciones está en la lista de deseos de todo especialista en marketing móvil. Sin embargo, lograr reseñas positivas no es tarea fácil, ya que requiere un esfuerzo adicional por parte de tus usuarios. Aplicando nuestra funcionalidad de manera inteligente, podemos ayudarte a aumentar la interacción con los clientes.

### Dirigirse a usuarios avanzados {#targeting-power-users}

Los usuarios avanzados pueden ser embajadores de tu aplicación. A menudo, interactúan con tu aplicación de manera constante y pueden proporcionar comentarios para mejorarla. Aunque varían de una aplicación a otra, los usuarios avanzados suelen tener las siguientes características:

- Han registrado muchas sesiones
- Han usado la aplicación recientemente
- Han gastado dinero y realizado compras

Para asegurar calificaciones más altas, pide a tus usuarios avanzados que reseñen tu aplicación en la tienda de aplicaciones, ya que es más probable que tengan cosas positivas que decir. Por ejemplo, podrías crear un segmento llamado "Usuarios avanzados" con estos filtros:
- Ha usado estas aplicaciones más de 10 veces en los últimos 14 días
- Ha gastado más de 50 dólares

![Un ejemplo de un segmento que se dirige a usuarios avanzados de una aplicación.]({% image_buster /assets/img_archive/ratings_power_users.png %})

Visitar la tienda de aplicaciones requiere tiempo por parte de tus usuarios. Para maximizar la probabilidad de que hagan ese esfuerzo adicional, solicita una calificación o reseña justo después de que hayan tenido una experiencia positiva con tu aplicación. Por ejemplo, pídelo después de que superen un nivel de juego o realicen una compra usando un código de descuento. Nuestro artículo sobre [adhesión voluntaria de datos]({{site.baseurl}}/user_guide/channels/email/subscriptions/#subscription-states) tiene más información sobre formas de asegurar que tu solicitud se ajuste a las expectativas del flujo de trabajo de los usuarios.

## Planificación de tus campañas {#scheduling-your-campaigns}

Al editar la planificación o las audiencias de una campaña, ten en cuenta las siguientes buenas prácticas:

- **Campañas programadas una sola vez:** puedes editar la campaña hasta el momento de envío programado.
- **Campañas programadas recurrentes:** puedes editar la campaña hasta el momento de envío programado.
- **Campañas con hora de envío local:** no hagas ediciones en las 24 horas previas al momento de envío programado.
- **Campañas con hora de envío óptima:** no hagas ediciones en las 24 horas previas a la medianoche del día en que la campaña está programada para enviarse.

{% alert note %}
Editar una campaña en vivo y cambiar la entrega a **Hora de envío local** provocará que se ponga en cola un nuevo lote de mensajes, lo que significa que tus usuarios recibirán el mensaje dos veces debido a que el mensaje se pone en cola dos veces. Para evitar esto, primero detén la campaña original y luego lanza un duplicado después de actualizar la planificación.
{% endalert %}