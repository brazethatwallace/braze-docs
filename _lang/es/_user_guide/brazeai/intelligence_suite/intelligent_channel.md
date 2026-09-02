---
nav_title: Filtro de canal
article_title: Filtro de canal inteligente
page_order: 1.5
description: "Este artículo cubre el filtro de canal inteligente, un filtro que selecciona la parte de tu audiencia para la que el canal de mensajería seleccionado es su mejor canal. En este caso, mejor significa que tiene la mayor probabilidad de participación, dado el historial del usuario."
search_rank: 11
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"} Filtro de canal inteligente {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecommost-engaged-channel-stylefloatrightwidth120pxborder0-classnoimgborderintelligent-channel-filter}

> El filtro `Intelligent Channel` (anteriormente `Most Engaged`) selecciona la parte de tu audiencia para la que el canal de mensajería seleccionado es el «mejor» canal.

## Acerca del filtro {#about-the-filter}

![El filtro de canal inteligente con un desplegable para los distintos canales que se pueden seleccionar.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

En este caso, mejor significa el canal que tiene la mayor probabilidad de participación, dado el historial del usuario. Puedes seleccionar como canal correo electrónico, SMS, WhatsApp, notificación push web o push móvil (incluyendo cualquier SO o dispositivo móvil disponible).

El canal inteligente calcula una tasa de participación para cada usuario en cada canal compatible, clasifica esos canales y trata el canal con la clasificación más alta como el mejor canal de ese usuario.

Para habilitar el filtro de canal inteligente, selecciona el filtro **Intelligent Channel** en la página **Target Audiences** al crear una Campaign o un Canvas.

## Cómo se calcula la participación por canal {#how-engagement-is-calculated-by-channel}

El canal inteligente compara los canales utilizando una tasa de participación: el número de interacciones con mensajes dividido entre el número de mensajes recibidos. Braze evalúa hasta los últimos 100 mensajes recibidos por canal en los últimos seis meses.

Cada vez que se envía un mensaje a un usuario o un usuario interactúa con un mensaje, la tasa de participación se recalcula en cuestión de segundos. Un usuario solo puede contabilizarse como que ha interactuado con un mensaje una vez (por ejemplo, una apertura y un clic en el mismo correo electrónico hacen que ese mensaje se marque como interactuado solo una vez, no dos).

### Datos de interacción por canal {#interaction-data-by-channel}

Braze rastrea los siguientes eventos al calcular las tasas de participación:

- **Correo electrónico:** aperturas (se excluyen las [aperturas automáticas]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens)). Los clics en correos electrónicos no se incluyen.
- **Push móvil:** Direct Opens. Cada plataforma móvil (como iOS, Android y Kindle) se puntúa por separado. Las Influenced Opens no se incluyen.
- **Notificación push web:** aperturas
- **SMS:** clics en enlaces acortados
- **WhatsApp:** lecturas de mensajes o clics en enlaces rastreados

Las Influenced Opens, los clics en correos electrónicos y la actividad de sesión no se utilizan para el canal inteligente. La actividad de sesión la utiliza la [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#about-intelligent-timing).

El canal inteligente no es compatible con webhooks, LINE, Kakao Talk, In-App Messages ni Content Cards.

{% alert important %}
Para calcular la tasa de participación del canal SMS, activa [el acortamiento de enlaces SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) con seguimiento avanzado y seguimiento de clics. Sin este seguimiento, los SMS pueden seleccionarse como el canal inteligente con una tasa de participación del 0 % debido a nuestro [comportamiento de desempate]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel#tie-breaking).
{% endalert %}

## Datos insuficientes {#not-enough-data}

Para que Braze determine qué canal es «el mejor», tiene que haber datos suficientes. Esto significa que un usuario debe haber recibido al menos tres o más mensajes en un canal antes de que ese canal pueda clasificarse, y debe tener datos suficientes en al menos dos canales compatibles.

Si los usuarios no han recibido suficientes mensajes a través de los canales, esos usuarios entrarán en la opción «Not Enough Data» de este filtro. Esto te permite utilizar cualquier canal de mensajería compatible para dirigirte a estos usuarios.

Por ejemplo, supongamos que quieres que los usuarios que prefieren los mensajes push reciban un push y que los usuarios que no tienen suficientes datos reciban el mismo mensaje push. En ese caso, podrías establecer el filtro de canal inteligente en **Mobile push** y utilizar **OR** para añadir un segundo filtro de canal inteligente establecido en **Not Enough Data**. Una Campaign independiente con el filtro de canal inteligente ajustado a correo electrónico podría dirigirse a los usuarios que prefieren el correo electrónico.

![Filtros de canal inteligente para push móvil o datos insuficientes.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
Las Campaigns y los pasos en Canvas que ignoren la [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-rules) no serán tenidos en cuenta por el canal inteligente y no podrán contribuir a los requisitos de datos.
{% endalert %}

## Push móvil {#mobile-push}

El push móvil incorpora Android, iOS, Kindle y otros canales de dispositivos móviles disponibles en Braze. Braze puntúa cada plataforma móvil por separado al calcular las tasas de participación.

Cuando utilizas el filtro de canal inteligente establecido en **Mobile push**, un usuario coincide si el push de iOS o el push de Android es su canal con la clasificación más alta. Esto no obliga al usuario a recibir notificaciones push en un dispositivo específico. La clasificación solo se utiliza para determinar si el push móvil es el mejor canal de ese usuario en comparación con el correo electrónico, la notificación push web, SMS y WhatsApp.

## Filtro de probabilidad de apertura de mensajes para canales individuales {#individual-channels}

En lugar de dejar que Braze elija el mejor canal para un usuario, puedes utilizar el [filtro de segmentación «Probabilidad de apertura de mensajes»]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#message-open-likelihood) para filtrar a los usuarios en función de si es probable que abran un mensaje en un canal específico que tú elijas. Este filtro se calcula dividiendo el porcentaje de interacciones entre el total de mensajes recibidos para los últimos 100 mensajes enviados por canal.

La probabilidad de apertura de mensajes utiliza los mismos datos de participación subyacentes que el canal inteligente, pero te permite establecer un umbral para un solo canal en lugar de seleccionar el mejor canal del usuario. Está disponible para correo electrónico, push móvil, SMS y notificación push web.

Ten en cuenta que un usuario debe haber recibido al menos tres mensajes en un canal específico antes de poder obtener una puntuación de probabilidad para ese canal. Los usuarios sin datos suficientes para medir la probabilidad de un canal pueden seleccionarse mediante «está en blanco».

## Mejores prácticas y estrategia de uso eficaz {#best-practices-and-effective-use-strategy}

### Desempate {#tie-breaking}

Como algunos usuarios reciben pocos mensajes, no es raro que haya empates en las tasas de participación entre los canales disponibles para un usuario determinado (por ejemplo, un solo usuario puede tener una tasa de participación del 20 % tanto para el correo electrónico como para el push móvil). En tales casos, los empates se deshacen dando prioridad (otorgando una clasificación más alta) al canal con los eventos de interacción más recientes.

Si los canales empatados tienen ambos una tasa de participación del 0 %, Braze deshace el empate utilizando el canal con el mensaje recibido más reciente.

### Canales inalcanzables {#unreachable-channels}

Un usuario puede tener datos suficientes para que Braze determine una clasificación de canales, pero luego volverse inalcanzable en su canal de mayor clasificación. Por ejemplo, un usuario cuyo mejor canal histórico es el correo electrónico puede haberse dado de baja recientemente del correo electrónico. Si envías un mensaje por ese canal, no se le entregará a ese usuario. Los usuarios que no son alcanzables en canales específicos deben segmentarse o enrutarse por separado.

### Dimensionamiento de la audiencia {#audience-sizing}

El canal inteligente te permite dirigirte selectivamente y por adelantado a la fracción de usuarios que tienen muchas más probabilidades de interactuar con un mensaje que el resto de tu audiencia. No es probable que represente a la mayoría de los usuarios de una audiencia típica. Más bien, puedes esperar que este filtro encuentre entre el 5 y el 20 % de tu audiencia habitual que tiene un historial establecido de participación en un canal concreto.