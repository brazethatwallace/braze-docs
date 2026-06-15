---
nav_title: Almacenar respuestas en caché
article_title: Almacenar en caché las respuestas de Contenido conectado
page_order: 2.5
description: "Este artículo explica cómo almacenar en caché las respuestas de Contenido conectado en diferentes campañas o mensajes dentro del mismo espacio de trabajo para optimizar las velocidades de envío."
---

# Almacenar en caché las respuestas de Contenido conectado {#cache-connected-content-responses}

> Las respuestas de Contenido conectado se pueden almacenar en caché en diferentes campañas o mensajes (en el mismo espacio de trabajo) para optimizar las velocidades de envío.

Braze no registra ni almacena de forma permanente los **cuerpos de respuesta** de Contenido conectado. Durante la representación de mensajes, las respuestas se pueden mantener temporalmente (por ejemplo, en memoria y en caché) para que Braze pueda representar Liquid y enviar el mensaje.

Para evitar el almacenamiento en caché, puedes especificar `:no_cache`, lo que puede provocar un aumento del tráfico de red. Para ayudar con la solución de problemas y la supervisión del estado del sistema, Braze registra los metadatos de las solicitudes de Contenido conectado (como la URL de solicitud completamente representada y el código de estado de la respuesta) para las llamadas exitosas y fallidas. Estos registros se conservan durante un máximo de 30 días.

{% details Representación de Contenido conectado y manejo de datos (avanzado) %}
Esta sección proporciona una vista más detallada y de extremo a extremo de cómo Braze representa Liquid y Contenido conectado, y dónde pueden existir temporalmente los datos antes de que se envíe un mensaje. Esto puede ser útil para revisiones de privacidad y manejo de datos.

## Qué se almacena y qué no {#what-is-and-isnt-stored}

- **Cuerpo de respuesta de Contenido conectado:** No se almacena de forma permanente en Braze. Se puede mantener temporalmente en memoria y, cuando el almacenamiento en caché está habilitado, se almacena en caché con un tiempo de vida (TTL).
- **Metadatos de solicitud de Contenido conectado:** Los metadatos de solicitud, como la URL completamente representada, el código de estado HTTP y la duración de la respuesta, se registran para la solución de problemas y la supervisión. Estos registros se conservan durante un máximo de 30 días.
- **Mensaje final representado:** Existe en memoria durante la representación. También puede almacenarse en otro lugar dependiendo de tu configuración y canal (por ejemplo, Archivado de mensajes o Content Cards).

## Flujo de representación (nivel alto) {#rendering-flow-high-level}

El siguiente flujo describe cómo Braze representa y envía mensajes para canales basados en proveedores, como correo electrónico, SMS y push. Los canales entregados por SDK, como Content Cards, utilizan la misma representación subyacente de Liquid y Contenido conectado, pero difieren en cuándo se genera el contenido y cómo se entrega.

1. Un proceso en segundo plano representa la plantilla Liquid de un mensaje cuando el mensaje se prepara para ser entregado.
2. Las etiquetas de Contenido conectado se evalúan durante la representación de Liquid.
3. Para cada etiqueta de Contenido conectado, Braze verifica una caché de múltiples niveles. Si no existe un valor en caché (o el almacenamiento en caché está deshabilitado), Braze llama a tu punto de conexión y recibe la respuesta.
4. La respuesta se inyecta en la plantilla Liquid y el mensaje se representa completamente.
5. Para canales basados en proveedores, el mensaje representado se envía al proveedor del canal y luego al usuario. Para canales entregados por SDK, como Content Cards, el contenido representado se sincroniza con el SDK de Braze y puede generarse en la primera impresión o en el momento de visualización, momento en el cual se muestra al usuario.

## Dónde pueden existir temporalmente las respuestas de Contenido conectado {#where-connected-content-responses-can-live-temporarily}

Braze utiliza una caché de múltiples niveles para las respuestas de Contenido conectado con TTL entre cinco minutos y cuatro horas, dependiendo de tu uso de `:cache_max_age` y otras reglas de almacenamiento en caché:

- **Caché de memoria en proceso:** Caché transitoria dentro del proceso del trabajador. Los datos solo pueden existir durante la duración del trabajo (hasta ~11 minutos según el tiempo de espera del trabajador).
- **Caché de máquina local:** Una caché por trabajador, como una instancia local de Memcached.
- **Caché a nivel de clúster:** Una caché distribuida compartida entre trabajadores, como un clúster de Memcached.

Estas capas de caché son volátiles y pueden desalojar datos antes del TTL configurado.

## Qué cambia cuando usas `:no_cache` {#what-changes-when-you-use-no_cache}

Para puntos de conexión que no están alojados dentro de la infraestructura de Braze, usar `:no_cache` evita que el cuerpo de respuesta de Contenido conectado se almacene en Memcached. En estos casos, la respuesta solo existe en la memoria del proceso del trabajador durante la duración del trabajo de representación (hasta ~11 minutos). Para puntos de conexión que resuelven a hosts internos de Braze, las respuestas aún pueden almacenarse en caché como se describe en [Invalidación de caché](#cache-busting).

## Dónde puede existir la salida final representada {#where-the-final-rendered-output-can-live}

- **Archivado de mensajes:** Si el Archivado de mensajes está habilitado, Braze puede escribir el mensaje final representado en tu contenedor de almacenamiento en la nube configurado. Si tu respuesta de Contenido conectado está incluida en el mensaje representado, se incluirá en la copia archivada.
- **Dispositivos de los usuarios:** Después de la entrega, el contenido del mensaje completamente representado puede persistir en los dispositivos de los usuarios durante un período de tiempo indeterminado.
- **Content Cards:** El contenido representado para Content Cards se almacena en una base de datos de Braze hasta que la tarjeta expire.
{% enddetails %}

## Configuración predeterminada de caché {#default-cache-settings}

La duración de la caché es de hasta cinco minutos (300 segundos). Puedes actualizar esto añadiendo el parámetro `:cache_max_age` a la llamada de Contenido conectado. Un ejemplo es:

{% raw %}
```
{{ {% connected_content [https://example.com/webservice.json] :cache_max_age 900 %}}}
```
{% endraw %}

Las solicitudes GET se almacenan en caché de forma predeterminada. Puedes deshabilitar el almacenamiento en caché añadiendo el parámetro `:no_cache` a la llamada de Contenido conectado.

Las solicitudes POST no se almacenan en caché de forma predeterminada, pero puedes habilitar el almacenamiento en caché añadiendo el parámetro `:cache_max_age` a la llamada de Contenido conectado. El tiempo mínimo de caché es de 5 minutos y el tiempo máximo de caché es de 4 horas.

{% alert note %}
La configuración de caché no está garantizada. El almacenamiento en caché puede reducir las llamadas a tus puntos de conexión, por lo que recomendamos usar múltiples llamadas por punto de conexión dentro de la duración de la caché en lugar de depender excesivamente del almacenamiento en caché.
{% endalert %}

### Límite de tamaño de caché {#cache-size-limit}

El cuerpo de respuesta de Contenido conectado puede tener hasta 1&nbsp;MB. Si el cuerpo de respuesta es mayor de 1&nbsp;MB, no se almacenará en caché.

## Tiempo de caché {#cache-time}

Contenido conectado almacenará en caché el valor que devuelve de los puntos de conexión GET durante un mínimo de cinco minutos. Si no se especifica un tiempo de caché, el tiempo predeterminado es de cinco minutos.

El tiempo de caché de Contenido conectado se puede configurar para que sea más largo con `:cache_max_age`, como se muestra en el siguiente ejemplo. El tiempo mínimo de caché es de cinco minutos y el tiempo máximo de caché es de cuatro horas. Los datos de Contenido conectado se almacenan en caché en memoria utilizando un sistema de caché volátil, como Memcached.

Como resultado, independientemente del tiempo de caché especificado, los datos de Contenido conectado pueden ser desalojados de la caché en memoria de Braze antes de lo especificado. Esto significa que las duraciones de caché son sugerencias y pueden no representar realmente la duración durante la cual se garantiza que los datos estén almacenados en caché por Braze, y es posible que veas más solicitudes de Contenido conectado de las que esperarías con una duración de caché determinada.

### Caché por segundos especificados {#cache-for-specified-seconds}

Este ejemplo almacenará en caché durante 900 segundos (o 15 minutos).

{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}

### Invalidación de caché {#cache-busting}

Para evitar que Contenido conectado almacene en caché el valor que devuelve de una solicitud GET, puedes usar la configuración `:no_cache`. Sin embargo, las respuestas de hosts internos de Braze seguirán almacenándose en caché.

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Asegúrate de que el punto de conexión de Contenido conectado proporcionado pueda manejar grandes ráfagas de tráfico antes de usar esta opción, o probablemente verás una mayor latencia de envío (mayores retrasos o intervalos de tiempo más amplios entre la solicitud y la respuesta) debido a que Braze realiza solicitudes de Contenido conectado para cada mensaje individual.
{% endalert %}

Con un POST no necesitas invalidar la caché, ya que las solicitudes POST no se almacenan en caché de forma predeterminada. Para almacenar en caché una respuesta POST, añade `:cache_max_age`; para evitar el almacenamiento en caché de un POST, omite `:cache_max_age`.

## Cosas que debes saber {#things-to-know}

{% raw %}
- El almacenamiento en caché puede ayudar a reducir las llamadas duplicadas de Contenido conectado. Sin embargo, no se garantiza que siempre resulte en una única llamada de Contenido conectado por usuario.
- El almacenamiento en caché de Contenido conectado se basa en el espacio de trabajo, la URL de solicitud, el tipo de contenido de la solicitud y el cuerpo de la solicitud. Si la llamada de Contenido conectado es a la misma URL, se puede almacenar en caché entre campañas y Canvas.
- La caché se basa en una combinación única de URL, tipo de contenido y cuerpo de la solicitud, no en un ID de usuario o una campaña. Esto significa que la versión en caché de una llamada de Contenido conectado podría usarse entre múltiples usuarios y campañas en un espacio de trabajo si la URL, el tipo de contenido y el cuerpo de la solicitud son los mismos.
- El almacenamiento en caché de Contenido conectado puede omitirse si el marcado de la etiqueta incluye alguno de los siguientes fragmentos de alta cardinalidad:
    - `{{${user_id}}}`
    - `{{${braze_id}}}`
    - `{{${email}}}`
    - `{{${email_address}}}`
    - `{{${phone_number}}}`
    - `{{${date_of_birth}}}`
{% endraw %}