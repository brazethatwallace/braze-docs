---
nav_title: Condiciones de carrera
article_title: Condiciones de carrera
alias: /race_conditions/
page_order: 9
page_type: reference
description: "Este artículo cubre las mejores prácticas para evitar que las condiciones de carrera afecten a tus campañas de mensajería."
toc_headers: h2
---

# Condiciones de carrera {#race-conditions}

> Una condición de carrera se produce cuando un resultado depende de la secuencia o la sincronización de varios eventos. Por ejemplo, si la secuencia deseada de eventos es "Evento A" y luego "Evento B", pero a veces "Evento A" llega primero y otras veces "Evento B" llega primero, eso se conoce como condición de carrera. Esto puede provocar resultados inesperados o errores, porque estos eventos compiten por acceder a recursos o datos compartidos.

{% multi_lang_include video.html id="LyJaxDoMtMs" align="right" %}

En Braze, pueden darse condiciones de carrera cuando se desencadenan varias acciones al mismo tiempo basándose en datos de usuario o eventos. Por ejemplo, si un usuario desencadena varias campañas (como registrarse en un boletín o realizar una compra), puede que no reciba los mensajes en el orden correcto.

## Tipos de condiciones de carrera {#types-of-race-conditions}

Los tipos más comunes de condiciones de carrera pueden ocurrir cuando haces lo siguiente:

- Segmentar a nuevos usuarios
- Usar múltiples endpoints de API
- Hacer coincidir desencadenantes basados en acciones y filtros de audiencia
- Usar el desencadenante "Interactuar con paso"

Considera los siguientes escenarios y aplica las mejores prácticas para evitar estas condiciones de carrera.

## Escenario 1: Segmentar a nuevos usuarios {#scenario-1-targeting-new-users}

En Braze, una de las condiciones de carrera más comunes se produce con los mensajes dirigidos a usuarios recién creados. El orden esperado de eventos es:

1. Se crea un usuario;
2. El mismo usuario es inmediatamente objetivo de un mensaje, realiza un evento personalizado o registra un atributo personalizado.

Sin embargo, en algunos casos, el segundo evento se desencadena primero. Esto significa que se intenta enviar un mensaje a un usuario que aún no existe. Como resultado, el usuario nunca lo recibe. Esto también aplica a eventos o atributos, donde el evento o atributo intenta registrarse en un perfil de usuario que aún no se ha creado.

En el caso de los mensajes dentro de la aplicación, el mensaje dentro de la aplicación debe cargarse en el dispositivo del usuario antes de ser desencadenado. Si el evento desencadenante es parte del proceso de incorporación, o el usuario sale del segmento para el evento personalizado como parte de su primera sesión, es probable que el usuario no vea el mensaje dentro de la aplicación.

### Mensajes dentro de la aplicación {#in-app-messages}

Con los mensajes dentro de la aplicación, la situación puede ser más matizada. Un mensaje dentro de la aplicación debe ser entregado y almacenado en caché en el SDK, generalmente al inicio de una sesión, antes de poder ser desencadenado. Si el evento desencadenante es parte del proceso de creación del usuario, o si la campaña de mensaje dentro de la aplicación se entrega antes de que el usuario cumpla (o después de que ya no cumpla) los criterios de audiencia durante su primera sesión, es posible que no vea el mensaje dentro de la aplicación.

### Mejores prácticas {#best-practices}

#### Introduce retrasos {#introduce-delays}

Después de crear un nuevo usuario, puedes añadir un retraso antes de enviar cualquier campaña o Canvas dirigido. Este retraso permite que se cree el perfil de usuario y que se actualicen los atributos relevantes que puedan determinar su elegibilidad para recibir el mensaje.

Por ejemplo, después de que un usuario se registre en tu aplicación, puedes enviar una oferta promocional después de 24 horas. O, si estás creando un usuario o registrando un atributo personalizado, puedes añadir un retraso de un minuto antes de continuar con tu proceso para evitar esta condición de carrera.

También puedes añadir este retraso en el [SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration) para el evento personalizado específico que desencadena que un nuevo usuario entre en un Canvas.

## Escenario 2: Usar múltiples endpoints de API {#scenario-2-using-multiple-api-endpoints}

{% alert important %}
Usamos procesamiento asíncrono para maximizar la velocidad y la flexibilidad. Esto significa que cuando las llamadas a la API se nos envían por separado, no podemos garantizar que se procesen en el orden en que fueron enviadas.
{% endalert %}

Hay algunos escenarios en los que múltiples endpoints de API también pueden resultar en esta condición de carrera, como cuando:

- Se usan endpoints de API separados para crear usuarios y desencadenar Canvas o campañas
- Se hacen múltiples llamadas separadas al endpoint `/users/track` para actualizar atributos personalizados, eventos o compras

Cuando la información del usuario se envía a Braze usando el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), ocasionalmente puede tardar unos segundos en procesarse. Esto significa que cuando se hacen solicitudes simultáneamente a los endpoints `/users/track` y de mensajería como `/campaign/trigger/send`, no hay garantía de que la información del usuario se actualice antes de que se envíe un mensaje.

{% alert note %}
Si los atributos de usuario y los eventos se envían en la misma solicitud (ya sea desde `/users/track` o desde el SDK), Braze procesa los atributos antes que los eventos o antes de intentar enviar cualquier mensaje.
{% endalert %}

### Mejores prácticas

#### Cuando uses múltiples endpoints, envía tus solicitudes una a la vez {#when-using-multiple-endpoints-send-your-requests-one-at-a-time}

Si estás usando múltiples endpoints, puedes intentar escalonar tus solicitudes para que cada solicitud se complete antes de que comience la siguiente. Esto puede reducir la probabilidad de una condición de carrera. Por ejemplo, si necesitas actualizar atributos de usuario y enviar un mensaje, primero espera a que el perfil de usuario se actualice completamente antes de enviar un mensaje usando un endpoint.

Si estás enviando una solicitud de API de mensaje planificado, estas solicitudes deben ser separadas, y el usuario debe ser creado antes de enviar la solicitud de API planificada.

#### Incluye datos clave con el desencadenante {#include-key-data-with-the-trigger}

En lugar de usar múltiples endpoints, puedes incluir los [atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object#object-body) y las [propiedades del desencadenante]({{site.baseurl}}/api/objects_filters/trigger_properties_object) en una sola llamada a la API usando el [endpoint `campaign/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns).

Cuando estos objetos se incluyen con el desencadenante, los atributos se procesan primero, antes de que se desencadene el mensaje, eliminando posibles condiciones de carrera. Ten en cuenta que las propiedades del desencadenante no actualizan el perfil de usuario, sino que se usan solo en el contexto del mensaje.

#### Usa el endpoint POST: Rastrear usuarios (sincrónico) {#use-the-post-track-users-sync-endpoint}

Usa el [endpoint `/users/track/sync/`]({{site.baseurl}}/api/endpoints/user_data/post_user_track_synchronous) para registrar eventos personalizados y compras, y actualizar atributos del perfil de usuario de forma sincrónica. Usar este endpoint para actualizar perfiles de usuario al mismo tiempo y en una sola llamada puede ayudar a prevenir posibles condiciones de carrera.

{% multi_lang_include alerts/early_access_beta_alert.md feature='This endpoint' type='beta' %}

## Escenario 3: Hacer coincidir desencadenantes basados en acciones y filtros de audiencia {#scenario-3-matching-action-based-triggers-and-audience-filters}

Otra condición de carrera común puede ocurrir si configuras una campaña o Canvas basado en acciones con el mismo desencadenante que el filtro de audiencia (como un atributo cambiado o un evento personalizado realizado). El usuario puede no estar en la audiencia en el momento en que realiza el evento desencadenante, lo que significa que no recibirá la campaña ni entrará en el Canvas.

### Mejores prácticas

#### Verifica tu audiencia después de un retraso {#check-your-audience-after-a-delay}

Para evitar usar filtros de audiencia que contengan los criterios del desencadenante, te recomendamos verificar tu audiencia antes de la entrega. Por ejemplo, puedes [usar validaciones de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#step-2-edit-delivery-settings) en los pasos de mensaje de Canvas como una verificación adicional para confirmar que tu audiencia cumple los criterios de entrega en el momento del envío del mensaje. También puedes aprovechar los criterios de salida de Canvas para hacer salir a cualquier usuario en cualquier punto del recorrido del usuario si cumple tus criterios.

Para las campañas, puedes usar eventos de salida para permitir que las campañas con un evento desencadenante cancelen mensajes a usuarios que realicen el evento de salida mientras están en el retraso.

#### Usa filtros únicos con el evento desencadenante {#use-unique-filters-with-the-trigger-event}

Al configurar tus filtros, es posible que quieras añadir un filtro redundante "por si acaso". Sin embargo, esta redundancia puede llevar a más problemas. En su lugar, evita usar cualquier filtro que contenga el desencadenante cuando sea posible. Esta es la ruta más segura para evitar una condición de carrera.

Por ejemplo, si el desencadenante de tu campaña es "Ha realizado una compra" y tu filtro de audiencia es "Ha realizado alguna compra", esta redundancia puede causar una condición de carrera.

#### Evita filtros de audiencia que asuman que el evento desencadenante se ha actualizado {#avoid-audience-filters-that-assume-the-trigger-event-has-been-updated}

Esta mejor práctica es similar a evitar filtros redundantes con el evento desencadenante. Normalmente, un filtro que asume que el evento desencadenante se ha actualizado en el perfil de usuario falla.

#### Usa cancelaciones con Liquid (solo atributos) {#use-liquid-aborts-attributes-only}

En campañas y pasos de Canvas, usa cancelaciones con Liquid para evitar usar filtros de audiencia que contengan los atributos del desencadenante en el horario de entrada. Por ejemplo, supongamos que tienes un atributo de array "colores favoritos" y quieres dirigirte a cualquier usuario que actualice el array del atributo con cualquier valor, y que también tenga el color "azul" en el array después de que se haya completado la actualización. Si usas los filtros de audiencia en este ejemplo, encontrarás una condición de carrera y perderás a los usuarios que añaden "azul" en el array por primera vez.

En este caso, puedes implementar un retraso del desencadenante en una campaña o usar un paso de retraso en Canvas para permitir que el perfil de usuario se actualice durante un período de tiempo, y luego usar la siguiente lógica de cancelación con Liquid:

{% raw %}
```liquid
{%assign colors={{custom_attribute.$(Favorite Color)|split:”,”}}%}
{%unless colors contains ‘Blue’%}
{%abort_message(Blue not present)%}
{%endunless%}
```
{% endraw %}

#### Confirma cómo se gestionan los datos de usuario {#confirm-how-user-data-is-being-managed}

Si hay una condición de carrera durante la evaluación de entrada del Canvas, los usuarios pueden entrar en un Canvas en el que no estaban destinados a entrar. Por ejemplo, el perfil del usuario podría estar configurado para ser incluido en la audiencia y posteriormente actualizarse después de que el Canvas haya puesto en cola a los usuarios para que ya no sean elegibles en la audiencia.

Si un usuario desencadena el evento de entrada del Canvas múltiples veces dentro del mismo segundo, Braze solo permite una entrada para ese segundo (incluso si la reentrada está habilitada). Esto previene entradas duplicadas, por lo que el número total de entradas al Canvas puede ser menor que el total de eventos desencadenantes.

Recomendamos confirmar cómo se gestionan y actualizan los datos de usuario, específicamente cuándo y cómo se actualizan atributos específicos, como por SDK, API, API por lotes y otros métodos. Esto puede ayudar a identificar y aclarar por qué un usuario ha entrado en una campaña o Canvas en comparación con cuándo se actualizó el perfil del usuario.

## Escenario 4: Usar el desencadenante "Interactuar con paso" {#scenario-4-using-the-interact-with-step-trigger}

En un Canvas, cuando un paso de mensaje va seguido inmediatamente de un paso de ruta de acción que usa el desencadenante "Interactuar con paso", puede ocurrir una condición de carrera. Dado que los usuarios pueden interactuar con un mensaje tan pronto como se entrega, es posible que un usuario complete la acción rastreada antes de entrar oficialmente en el paso de ruta de acción.

En este caso, el paso de ruta de acción no registra la interacción, ya que solo evalúa eventos que ocurren después de la entrada en el paso, lo que significa que el usuario puede ser dirigido por una ruta no deseada.

Un Canvas envía una notificación push en un paso de mensaje, seguido de un paso de ruta de acción que verifica si el usuario abre esa notificación push. Si un usuario abre la notificación push inmediatamente al recibirla (antes de entrar en el paso de ruta de acción), el evento de apertura puede no ser capturado. El usuario podría entonces ser dirigido incorrectamente por la ruta "no abrió", aunque sí interactuó con el mensaje.

### Mejores prácticas

#### Rastrea la participación usando un evento personalizado {#track-engagement-using-a-custom-event}

Evita depender de "Interactuar con paso" inmediatamente después de un paso de mensaje cuando se espera que las interacciones del usuario ocurran rápidamente. En su lugar, rastrea la participación usando un evento personalizado (por ejemplo, desencadenado desde la aplicación o el sitio web después de la interacción) y evalúa ese evento en un paso posterior. Esto asegura que el evento se registre después de que el usuario haya entrado en el paso.

#### Evita ramificaciones que dependan de la interacción {#avoid-branches-that-are-dependent-on-interaction}

Diseña tu Canvas de modo que perder una interacción inmediata no rompa la experiencia del usuario. Por ejemplo, evita decisiones de ramificación críticas que dependan únicamente de si la interacción se captura en el siguiente paso, o añade lógica de seguimiento que pueda corregir las rutas de los usuarios.