---
nav_title: Reelegibilidad
article_title: Reelegibilidad
page_order: 10
page_type: reference
description: "Este artículo de referencia define la reelegibilidad para campañas y Canvas."
tool:
    - Campaigns
    - Canvas
toc_headers: h2
---

# Reelegibilidad para campañas y Canvas {#re-eligibility-for-campaigns-and-canvas}

> Cuando planificas una campaña o Canvas recurrente o desencadenada, tienes la opción de permitir que los usuarios vuelvan a ser elegibles. La reelegibilidad significa que los usuarios pueden entrar en la campaña o Canvas varias veces en función del desencadenante.

## Cómo funciona {#how-it-works}

De forma predeterminada, Braze envía un mensaje a un usuario solo una vez, incluso si vuelve a cumplir los requisitos varias veces, ya que la reelegibilidad debe activarse por separado. Una vez activada, los miembros que cumplan los requisitos podrán recibir mensajes de nuevo después de haber recibido la primera instancia de la campaña o Canvas. Puedes establecer el plazo en el que los usuarios volverán a ser elegibles.

## Activar la reelegibilidad {#turning-on-re-eligibility}

{% tabs local %}
{% tab campaign %}
Para activar la reelegibilidad de una campaña, selecciona la casilla **Permitir que los usuarios vuelvan a ser elegibles para recibir la campaña** en la sección **Controles de entrega**. El tiempo máximo de reelegibilidad para una campaña es de 720 días.

Para campañas desencadenadas con la reelegibilidad activada, los usuarios que [no recibieron realmente el mensaje de la campaña]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#why-did-a-user-not-receive-my-triggered-campaign) (a pesar de completar el evento desencadenante) cumplirán automáticamente los requisitos para el mensaje la próxima vez que completen el evento desencadenante. Esto se debe a que la reelegibilidad se basa en la recepción del mensaje y no en la entrada a la campaña. Al hacer que los usuarios sean reelegibles para una campaña desencadenada, les permites recibir realmente (y no simplemente desencadenar) el mensaje más de una vez.

{% alert note %}
"Recepción" incluye la atribución a través de identificadores de canal compartidos: cuando un mensaje se entrega, se abre o se hace clic en él, Braze actualiza los datos de todos los perfiles que comparten el mismo correo electrónico o número de teléfono, por lo que un usuario al que nunca se le envió directamente el mensaje puede quedar marcado como que lo recibió y puede no volver a ser elegible.
{% endalert %}

Además, si intentas enviar un mensaje de forma inmediata con una reelegibilidad de cero minutos, siempre intentaremos planificarlo de inmediato, independientemente de cómo un usuario haya recibido versiones anteriores de la campaña o Canvas.

### Reelegibilidad con campañas desencadenadas por API {#re-eligibility-with-api-triggered-campaigns}

El número de veces que un usuario recibe una campaña desencadenada por API puede limitarse mediante la configuración de reelegibilidad. Esto significa que el usuario recibirá la campaña solo una vez o una vez en un período determinado, independientemente de cuántas veces se active el desencadenante de API.

Por ejemplo, supongamos que estás utilizando una campaña desencadenada por API para enviar al usuario una campaña sobre un artículo que vio recientemente. En este caso, puedes limitar la campaña a enviar como máximo un mensaje por día, independientemente de cuántos artículos haya visto, mientras activas el desencadenante de API para cada artículo. Por otro lado, si tu campaña desencadenada por API es transaccional, querrás asegurarte de que el usuario reciba la campaña cada vez que realice la transacción, estableciendo el retraso en cero minutos.
{% endtab %}

{% tab canvas %}

Para activar la reelegibilidad de un Canvas, selecciona **Permitir que los usuarios vuelvan a entrar en este Canvas** en la sección **Controles de entrada**. Puedes elegir entre permitir que los usuarios vuelvan a entrar después de la duración máxima del Canvas o después de un período especificado.

La reelegibilidad para las variantes en Canvas está vinculada a la entrada al Canvas en lugar de a la recepción del mensaje. Los usuarios que entran en un Canvas y no reciben ningún mensaje no podrán volver a entrar en el Canvas a menos que la reelegibilidad esté activada.

Ten en cuenta que un usuario no necesita salir de un Canvas antes de volver a entrar si la reelegibilidad está configurada en cero segundos, lo que significa que un usuario puede entrar en el mismo Canvas de nuevo. Como otro ejemplo, si la duración del Canvas está configurada en 7 días y el período de reelegibilidad está configurado en 3 días, un usuario puede volver a entrar en el Canvas antes de completar su primer recorrido.

Puedes añadir filtros adicionales para evitar que los usuarios reciban el mismo paso o mensaje varias veces. Sin embargo, cuando un usuario vuelve a entrar en un Canvas por segunda vez, los pasos recibidos previamente durante su primera vez en el Canvas no son visibles para el usuario. Esto significa que el usuario puede seguir recibiendo el mismo mensaje de nuevo. Para evitar esto, puedes configurar el Canvas para impedir la reentrada o establecer la reelegibilidad para la duración máxima del Canvas.

También puedes usar un [paso de Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) para que el usuario que recibe el paso lo registre como un atributo personalizado, que puede usarse para filtrar a los usuarios que ya han recibido el paso durante su recorrido en Canvas.

### Ejemplo {#example}

Por ejemplo, supongamos que un usuario sin dirección de correo electrónico entra en un Canvas recurrente diario que contiene un paso en el recorrido del usuario. Este paso solo contiene un mensaje de correo electrónico, por lo que el usuario no recibe la interacción. Este usuario no podrá volver a entrar en el Canvas a menos que el Canvas tenga la reelegibilidad activada.

Si tienes un Canvas recurrente o desencadenado activo sin reelegibilidad y te gustaría que los usuarios vuelvan a entrar en el Canvas hasta que reciban un mensaje de él, puedes considerar permitir que los usuarios sean reelegibles para la entrada añadiendo un filtro a los criterios de entrada que excluya a los clientes que ya han recibido un mensaje del Canvas.

Si la reelegibilidad de un Canvas está configurada con un período más corto que la duración del Canvas, es posible que los usuarios entren en el Canvas más de una vez, lo que puede provocar un comportamiento engañoso para Canvas que usan mensajes dentro de la aplicación con retrasos particularmente largos. Dado que varios mensajes dentro de la aplicación de Canvas podrían desencadenarse por el mismo inicio de sesión, el usuario podría tener la experiencia de recibir el mismo mensaje repetidamente si un componente específico se renderiza más rápido que otros.
{% endtab %}
{% endtabs %}

## Cálculos del retraso de reelegibilidad {#re-eligibility-delay-calculations}

La reelegibilidad tanto para campañas como para Canvas se calcula en segundos, no en días calendario. Esto significa que un día cuenta como 24 horas (u 86.400 segundos) desde que un usuario recibe el mensaje, no el siguiente día calendario a medianoche. De manera similar, un mes cuenta como exactamente 2.592.000 segundos, equivalente a aproximadamente 30 días.

### Ejemplo

Considera el siguiente escenario:

* Una campaña está configurada para enviarse mensualmente el día 15 con la reelegibilidad configurada en 30 días.
* Hay menos de 30 días entre el 15 de febrero y el 15 de marzo.

Esto significa que los usuarios que recibieron la campaña el 15 de febrero no son elegibles para la campaña que se envía el 15 de marzo. (Un usuario puede quedar marcado como que "recibió" la campaña debido a identificadores de canal compartidos; por ejemplo, si comparte un correo electrónico o número de teléfono con alguien que recibió, abrió o hizo clic en el mensaje). Si la campaña está configurada para enviarse diariamente a las 8 am con una reelegibilidad de 1 día, y hay una latencia en el envío del mensaje, los usuarios que recibieron la campaña a las 8:30 am aún no son reelegibles al día siguiente a las 8 am.

## Reelegibilidad para Content Cards {#re-eligibility-for-content-cards}

Cuando la reelegibilidad está habilitada para campañas de Content Cards o pasos en Canvas, un usuario puede recibir otra tarjeta mientras una tarjeta anterior de la misma campaña todavía está en su fuente, lo que puede parecer tarjetas duplicadas. Para reducir los duplicados, desactiva la reelegibilidad o amplía el período de reelegibilidad para que la primera tarjeta [expire de la fuente]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#the-30-day-expiration-and-re-eligibility) antes de que el usuario cumpla los requisitos para otro envío.

A diferencia de otros canales (como push y correo electrónico) donde la reelegibilidad se calcula a partir de la marca de tiempo de entrega del mensaje, la reelegibilidad de Content Cards se calcula en función de la marca de tiempo de la impresión, que es cuando el usuario realmente ve la tarjeta. Esto significa que si hay un desfase entre el momento en que se entrega una tarjeta y el momento en que el usuario abre su sesión para verla, es posible que no vuelva a ser elegible como se esperaba.

Por ejemplo, si una campaña diaria de Content Cards tiene un período de reelegibilidad de 24 horas y un usuario ve una tarjeta varias horas después de que se entregó, es posible que no reciba la tarjeta del día siguiente porque no han pasado 24 horas desde la impresión. Para tener esto en cuenta, considera acortar ligeramente tu período de reelegibilidad para campañas recurrentes de Content Cards.

## Reelegibilidad para banners {#re-eligibility-for-banners}

Cuando la reelegibilidad está habilitada para campañas de Banner, los usuarios que descarten un banner pueden volver a ser elegibles después de un período de espera configurable que comienza en el momento del descarte. Si la reelegibilidad no está activada, los usuarios que descartaron el banner permanecen no elegibles. Para configurar la reelegibilidad, consulta [Configurar la reelegibilidad]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#re-eligibility). Ten en cuenta que los pasos de Banner en Canvas usan la configuración de reentrada de Canvas en su lugar.

## Pruebas multivariante {#multivariate-testing}

Para las pruebas multivariante, Braze determina la reelegibilidad de variante para todas las campañas, mensajes dentro de la aplicación desencadenados y Canvas utilizando las siguientes reglas:

- Cuando los porcentajes de variante no se modifican, cada usuario siempre entrará en la misma variante de una campaña, mensaje dentro de la aplicación desencadenado o entrada de Canvas cada vez que sea reelegible.
- Si los porcentajes de variante cambian, los usuarios pueden redistribuirse a otras variantes.
- Los grupos de control permanecerán consistentes si el porcentaje de variante no cambia, y ningún usuario que haya recibido mensajes previamente entrará en el grupo de control en un envío posterior, ni ningún usuario en el grupo de control recibirá un mensaje.