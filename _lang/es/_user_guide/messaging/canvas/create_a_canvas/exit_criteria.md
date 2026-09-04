---
nav_title: Criterios de salida
article_title: Criterios de salida
page_order: 4.1
alias: /exit_criteria/
page_type: reference
description: "Este artículo de referencia cubre los criterios de salida y cómo los usuarios pueden salir de tu Canvas en función de los criterios seleccionados."
tool: Canvas
---

# Criterios de salida {#exit-criteria}

> Al añadir eventos de excepción directamente a las reglas de entrada de tu Canvas, puedes eliminar usuarios del recorrido cuando realizan una acción específica.
> Braze registra la salida en cuanto ocurre el evento.
> La rapidez con la que un usuario abandona completamente el Canvas depende del paso en el que se encuentre, especialmente en los pasos de demora.
> Para más información, consulta [Cómo salen los usuarios](#how-users-exit).

## Cómo salen los usuarios {#how-users-exit}

Cuando un usuario realiza el evento de salida, Braze lo marca de inmediato para salir del Canvas. Después de eso, no avanza a ningún paso posterior.

Si está en un paso de demora, permanece en ese paso hasta que finalice el período de demora. No continúa a los pasos siguientes cuando la demora termina; en su lugar, abandona completamente el Canvas. Dependiendo de dónde revises los datos del Canvas, es posible que veas actividad relacionada con la salida tanto cuando ocurre el evento de salida como cuando el paso de demora se completa y el usuario sale completamente del Canvas.

Por ejemplo, si un usuario está en un paso de demora de 30 días y realiza el evento de salida el primer día del paso de demora, se le marca para salir de inmediato, pero no abandona completamente el Canvas hasta que el paso de demora finaliza (29 días después).

Consideremos otro ejemplo con criterios de salida basados en el tiempo. Un usuario entra en un paso de demora configurado en 24 horas el 1 de julio a las 12 am. Durante este período de demora, realiza el evento de salida "Realizó un pedido por última vez hace menos de 1 hora" a las 3 am. Este usuario será evaluado con los criterios de salida el 2 de julio a las 12 am, que es la conclusión de la duración del paso de demora. Dado que han pasado 21 horas desde que realizó su pedido el 1 de julio a las 3 am, no saldrá del Canvas porque no realizó un pedido dentro de la hora previa a la salida del paso de demora el 2 de julio. Esto afecta a "Total Exits by Exit Criteria" en los análisis de tu Canvas, que solo se actualizan después de que un usuario haya salido completamente del Canvas.

## Configuración de criterios de salida {#setting-up-exit-criteria}

En el paso **Público objetivo** del creador de Canvas, puedes configurar criterios de salida para identificar qué usuarios deseas que salgan de tu Canvas.

Los criterios de salida incluyen un evento de excepción, que es la acción específica que puede hacer que los usuarios salgan del Canvas.

![Los criterios de salida configurados para volver a captar usuarios que han explorado productos pero aún no los han añadido a su carrito ni han realizado un pedido.]({% image_buster /assets/img/exit_criteria.png %}){: style="max-width:90%;"}

### Seleccionar eventos de excepción {#exception-events}

Cuando un usuario realiza el evento de excepción, Braze lo marca para salir según [Cómo salen los usuarios](#how-users-exit). Los eventos de excepción se aplican mientras un usuario está en el Canvas, incluso cuando está esperando en un paso como un paso de retraso.

Supongamos que tienes un Canvas configurado para promocionar un nuevo producto. En este caso, el pedido del producto sería el evento de excepción. De esta forma, después de que un usuario realice el pedido, no recibirá más mensajes sobre un producto que ya compró. Los eventos de excepción mantienen tu mensajería relevante y personalizada.

Los eventos de excepción adicionales incluyen:

- Realizar un pedido
- Iniciar una sesión
- Realizar un evento personalizado
- Realizar un evento de conversión
- Añadir una dirección de correo electrónico
- Cambiar el valor de un atributo personalizado
- Actualizar un estado de suscripción
- Actualizar un estado del grupo de suscripción
- Interactuar con una Campaign
- Entrar en una ubicación
- Desencadenar una geovalla
- Enviar un mensaje SMS entrante
- Enviar un mensaje WhatsApp entrante
- Enviar un mensaje LINE entrante
- Realizar un evento de carrito actualizado

#### Pasos programados {#scheduled-steps}

Para los pasos en Canvas que no mantienen al usuario en un paso de retraso hasta un momento futuro, el usuario normalmente sale del Canvas tan pronto como se completa el paso actual. Esa finalización suele ocurrir inmediatamente después del evento de excepción, porque no hay un temporizador de retraso restante en ese paso. Esto difiere de un paso de retraso, donde el usuario permanece hasta que el retraso termina, incluso después de haber sido marcado para salir (consulta [Cómo salen los usuarios](#how-users-exit)).

#### Pasos desencadenados {#triggered-steps}

Si un paso en Canvas se desencadena por un evento, el último envío programado en cola a partir de ese desencadenante se cancelará, pero el usuario permanecerá dentro del Canvas durante la duración de la ventana. Esto significa que el usuario aún puede recibir el paso si realiza el evento desencadenante nuevamente dentro de la ventana. Después de que la ventana finalice, el usuario saldrá del Canvas.

### Uso de segmentos y filtros {#using-segments-and-filters}

También puedes añadir segmentos y filtros en los criterios de salida. Esto significa que los usuarios que coincidan con el segmento y el filtro saldrán del Canvas y no recibirán más mensajes.

Por ejemplo, si el primer paso en un Canvas es un paso de retraso con un retraso de cinco días, los criterios de salida se evalúan cuando ese paso se completa. Si un usuario cumple los criterios de salida mientras está en el paso de retraso, se le marca para salir inmediatamente, pero sale completamente del Canvas al final de los cinco días (y no avanza a ningún paso posterior al retraso).

{% alert note %}
Los atributos de tipo array no están actualmente soportados como criterios de salida en eventos de excepción.
{% endalert %}

### Tener el mismo evento de salida y evento de conversión {#having-the-same-exit-event-and-conversion-event}

Cuando el evento de salida y el evento de conversión son los mismos, tanto la conversión como los eventos de salida se contabilizarán. Por ejemplo, si un Canvas tiene un paso de retraso y un usuario cumple los criterios de salida mientras está en ese paso de retraso, el evento de salida se incrementará tan pronto como el usuario salga del paso de retraso. La conversión también se incrementará tan pronto como el evento se registre en el perfil de usuario.

Las conversiones se rastrean incluso después de que el Canvas finalice, pero las salidas no se rastrean una vez que el usuario sale del Canvas. La ventana de conversión se extiende tres días más allá de la duración máxima del Canvas. Esto significa que las conversiones seguirán rastreándose después de que las salidas dejen de rastrearse.

El tiempo mínimo para una ventana de conversión es de cinco minutos. Configura las ventanas de conversión en cinco minutos para tus eventos de conversión para acercarte lo más posible a la paridad con los eventos de salida. También recomendamos configurar la ventana de conversión para que al menos coincida con la ruta más larga del Canvas.

Considera el siguiente ejemplo sobre cómo se calculan los análisis:

1. Diez usuarios pasan por el Canvas.
2. Tres usuarios realizan el evento de conversión en cinco minutos (el número de eventos de salida es tres y el número de eventos de conversión es tres).
3. Otros cinco usuarios salen del Canvas después de cinco minutos, pero realizan el evento de conversión después de dos días (el número de eventos de salida se mantiene igual, pero el evento de conversión aumenta a ocho).
4. Los últimos dos usuarios salen del Canvas después de cinco minutos, pero no realizan el evento de conversión, o lo realizan después de tres días y cinco minutos (no se cuentan ni en las métricas de eventos de salida ni en las de eventos de conversión).

## Ejemplo {#example}

Supongamos que queremos dirigirnos a usuarios que aún no han realizado un pedido en nuestra empresa de mochilas. Para configurar los criterios de salida, haríamos lo siguiente:

1. Selecciona **Place an Order** como el evento de excepción.
2. Selecciona **Add Trigger**.
3. Para **Segments**, selecciona **Used in last day** para que, cuando se lance nuestro Canvas, la audiencia excluya a los usuarios que hayan realizado alguna compra.
4. Para **Filters**, selecciona **Purchase behavior** > **Number of purchases** > **Purchased product**.
5. Establece el grupo de filtros en `backpack-example exactly 1`. Esto significa que los usuarios que hayan comprado nuestro producto de mochila saldrían del Canvas.

![Configuración de los criterios de salida con "Makes Any Purchase" como evento de excepción, de modo que si un usuario realiza cualquier compra, saldrá de este Canvas.]({% image_buster /assets/img_archive/exit_criteria_example.png %}){: style="max-width:80%;"}

{% alert tip %}
Para configurar criterios de salida que comparen propiedades del evento con las propiedades de entrada de Canvas (por ejemplo, salir solo cuando un usuario compra el artículo específico que abandonó), consulta [Hacer coincidir los criterios de salida con los eventos de entrada]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/matching_entry_and_exit_criteria).
{% endalert %}