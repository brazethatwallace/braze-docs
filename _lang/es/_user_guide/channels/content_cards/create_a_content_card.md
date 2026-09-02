---
nav_title: Crear una tarjeta de contenido
article_title: Crear una tarjeta de contenido
page_order: 1
description: "Este artículo de referencia explica cómo crear, redactar, configurar y enviar Content Cards mediante Campaigns y Canvas de Braze."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# Crear una tarjeta de contenido {#create-a-content-card}

> Este artículo explica cómo crear una tarjeta de contenido en Braze al construir Campaigns y Canvas. Aquí te guiaremos para elegir un tipo de mensaje, redactar tu tarjeta y planificar la entrega de tu mensaje.

## Paso 1: Elige dónde crear tu mensaje {#step-1-choose-where-to-build-your-message}

Usa Campaigns para mensajería simple y única (como informar a los usuarios sobre un producto con un solo mensaje). Usa Canvas para recorridos de usuario de varios pasos (como enviar sugerencias de productos personalizadas basadas en el comportamiento del usuario a lo largo del tiempo).

{% tabs %}
{% tab Campaign %}

1. Ve a **Mensajería** > **Campaigns** y selecciona **Crear Campaign**.
2. Selecciona **Content Cards** o, para campañas dirigidas a varios canales, selecciona **Multicanal**.
3. Dale a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) y [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) según sea necesario.
   * Las etiquetas facilitan encontrar tus campañas y generar informes a partir de ellas. Por ejemplo, al usar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reports/report_builder), puedes filtrar por las etiquetas relevantes.
5. Añade y nombra tantas variantes como desees para tu campaña. Puedes elegir diferentes plataformas, tipos de mensaje y diseños para cada una de las variantes añadidas. Para más información sobre variantes, consulta [Pruebas multivariante y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si todos los mensajes de tu campaña son similares o tienen el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. Después puedes seleccionar **Copiar de variante** en el menú desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crea tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) usando el creador de Canvas.
2. Después de configurar tu Canvas, añade un paso de mensaje en el constructor de Canvas. Dale a tu paso un nombre claro y significativo.
3. Selecciona **Content Cards** como tu canal de mensajería.
4. Elige cuándo Braze calcula la elegibilidad de la audiencia y la personalización para la Content Card. Esto puede ser en la entrada al paso o en la primera impresión (recomendado). Los pasos que contienen Content Cards pueden ser programados o basados en acciones.
5. Elige si deseas eliminar las Content Cards cuando los usuarios completen una compra o realicen un evento personalizado.
6. Establece una expiración para la Content Card (tiempo en la fuente). Esto puede ser después de un periodo de tiempo o en un momento específico.
7. Filtra tu audiencia, o los destinatarios, para este paso según sea necesario en la **Configuración de entrega**. Puedes refinar aún más tu audiencia especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se verifican después del retraso, en el momento en que se envían los mensajes.
8. Elige cualquier otro canal de mensajería que quieras emparejar con tu mensaje.

{% endtab %}
{% endtabs %}

## Paso 2: Especifica los tipos de mensaje {#step-2-specify-your-message-types}

Selecciona uno de los tres tipos esenciales de Content Cards: **Clásica**, **Imagen con subtítulo** e **Solo imagen**.

Para obtener más información sobre el comportamiento esperado y la apariencia de cada tipo, consulta [Detalles creativos]({{site.baseurl}}/user_guide/channels/content_cards/creative_details), o echa un vistazo a los enlaces de la siguiente tabla. Estos tipos de Content Cards son aceptados tanto por aplicaciones móviles como por aplicaciones web.

| Tipo de mensaje | Ejemplo | Descripción |
|---|---|---|
| [Clásica]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![Una tarjeta de contenido clásica con un pequeño icono y texto que invita a reservar una clase de entrenamiento.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) | La tarjeta clásica tiene un diseño sencillo con un título en negrita, texto del mensaje y una imagen opcional que se sitúa al inicio del título y el texto. Es mejor utilizar una imagen cuadrada o un icono con la tarjeta clásica. |
| [Imagen con subtítulo]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![Una tarjeta de contenido con subtítulo que muestra una imagen de un levantador de pesas y texto que invita a reservar una clase de entrenamiento.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | La tarjeta de imagen con subtítulo muestra tu contenido con texto e imágenes llamativas. |
| [Solo imagen]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![Una tarjeta de contenido de solo imagen con únicamente texto.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | La tarjeta de solo imagen capta la atención con espacio para imágenes, GIF y otro contenido creativo sin texto. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 2: Especifica los tipos de mensaje" }

## Paso 3: Redactar una Content Card {#step-3-compose-a-content-card}

Puedes editar todos los aspectos del contenido y comportamiento de tu mensaje en la pestaña **Redactar** del editor de mensajes.

![Ejemplo de detalles de Content Card en la pestaña Redactar del editor de mensajes.]({% image_buster /assets/img/content_card_compose.png %})

El contenido aquí varía según el **tipo de tarjeta** elegido en el paso anterior, pero puede incluir cualquiera de las siguientes opciones:

### Idioma {#language}

Selecciona **Añadir idiomas** para agregar los idiomas que desees de la lista proporcionada. Esto inserta [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) en tu mensaje. Te recomendamos seleccionar tus idiomas antes de redactar tu contenido para que puedas completar el texto en el lugar correspondiente del Liquid. Para ver nuestra lista completa de idiomas disponibles, consulta [Idiomas compatibles]({{site.baseurl}}/developer_guide/localization?tab=android).

![Una ventana con inglés, español y francés seleccionados como idiomas, y título, descripción y texto del enlace seleccionados como campos a internacionalizar.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

#### Crear mensajes de derecha a izquierda {#create-right-to-left-messages}

La apariencia final de los mensajes de derecha a izquierda depende en gran medida de cómo los proveedores de servicios los presentan. Para conocer las mejores prácticas sobre cómo redactar mensajes de derecha a izquierda que se muestren con la mayor precisión posible, consulta [Creación de mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Título y mensaje {#title-and-message}

Escribe lo que quieras. No hay límites, pero cuanto más rápido puedas transmitir tu mensaje y lograr que tu cliente haga clic, ¡mejor! Recomendamos títulos y contenido de mensajes claros y concisos. Ten en cuenta que estos campos no se proporcionan para las tarjetas de solo imagen.

#### Imagen {#image}

Para añadir una imagen a tu Content Card, puedes seleccionar **Añadir imagen** o proporcionar una URL de imagen. Al seleccionar **Añadir imagen** se abre la **Biblioteca multimedia**, donde puedes seleccionar una imagen cargada previamente o añadir una nueva.

Cada tipo de mensaje y plataforma puede tener sus propias proporciones y requisitos sugeridos, así que asegúrate de verificarlos antes de encargar o crear una imagen desde cero. Ten en cuenta que los campos de mensajes de Content Cards están limitados a 2&nbsp;KB de tamaño total.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Anclar en la parte superior {#pin-to-top}

Braze muestra una tarjeta anclada en la parte superior de la fuente de un usuario, y el usuario no puede descartarla. Si la fuente de un usuario tiene varias tarjetas ancladas, Braze las ordena cronológicamente. Cuando Braze entrega una Content Card, esta se presenta como anclada o no anclada, y ese estado no cambia durante la vigencia de la tarjeta. Si cambias la configuración de anclado en una Campaign, la actualización se aplica solo a las tarjetas enviadas después de la modificación. No cambia el estado de anclado de las tarjetas que ya se encuentran en la fuente de un usuario.

![Vista previa lado a lado de la Content Card en Braze para móvil y web con la opción "Anclar esta tarjeta en la parte superior de la fuente" seleccionada.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### Comportamiento al hacer clic {#on-click-behavior}

Cuando tu cliente hace clic en un enlace presentado en la tarjeta, el enlace puede dirigirlo a una parte más profunda de tu aplicación o a otro sitio. Si eliges un comportamiento al hacer clic para tu Content Card, recuerda actualizar tu **texto del enlace** de acuerdo.

Las siguientes acciones están disponibles para los enlaces de Content Cards:

| Acción | Descripción |
|---|---|
| Redirigir a URL web | Abre una página web no nativa. |
| [Vínculo profundo a la aplicación]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | Vínculo profundo a una pantalla existente de tu aplicación. |
| Registrar evento personalizado | Elige un [evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events) para desencadenar. Se puede usar para mostrar otra Content Card o desencadenar mensajería adicional. |
| Registrar atributo personalizado | Elige un [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) para establecer para el usuario actual. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportamiento al hacer clic" }

Las opciones **Registrar evento personalizado** y **Registrar atributo personalizado** requieren la siguiente compatibilidad de versiones del SDK or kit de desarrollo de software:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## Paso 4: Configurar ajustes adicionales (opcional) {#step-4-configure-additional-settings-optional}

Puedes usar [pares clave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) para crear categorías para tus tarjetas, crear [múltiples fuentes de Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed#implementing-multiple-feeds) y personalizar cómo se ordenan las tarjetas.

Para añadir pares clave-valor a tu mensaje, ve a la pestaña **Configuración** y selecciona **Añadir nuevo par**.

## Paso 5: Construye el resto de tu campaña o Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Construye el resto de tu campaña. Continúa con las secciones siguientes para obtener más detalles sobre cómo utilizar mejor nuestras herramientas para crear Content Cards.

### Elige un calendario de entrega o desencadenante {#choose-a-delivery-schedule-or-trigger}

Las Content Cards se pueden entregar en función de una hora programada, una acción o un desencadenante de API. Para más información, consulta [Programar tu campaña]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

También puedes establecer la duración de la campaña y las [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours), y determinar la expiración de la Content Card. Establece una fecha de expiración específica o los días hasta que una tarjeta expire, hasta un máximo de 30 días. Todas las variantes deben usar la misma expiración (duración o momento específico).

La cuenta regresiva de expiración comienza a partir del momento de envío de la tarjeta:

- **Campaigns programadas:** La cuenta regresiva comienza en el momento del lanzamiento programado.
- **Campaigns basadas en acciones:** La cuenta regresiva comienza cuando el usuario realiza la acción desencadenante.

Por ejemplo, si una Content Card basada en acciones se envía a las 2 pm de hoy con una expiración de 1 día, expira a las 2 pm del día siguiente.

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

Para la entrega basada en acciones, hay un breve retraso esperado antes de que aparezca la Content Card. Para más detalles sobre por qué sucede esto y cómo minimizarlo, consulta [¿Por qué las Content Cards no aparecen inmediatamente después de un evento desencadenante?]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#why-dont-content-cards-appear-immediately-after-a-trigger-event).

#### Entrega programada {#scheduled-delivery}

Para campañas de Content Cards con entrega programada, puedes elegir cuándo Braze evalúa la elegibilidad de la audiencia y la personalización para nuevas campañas de Content Cards especificando cuándo se crea la tarjeta. Para más información, consulta [creación de tarjetas]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation).

#### Elige a los usuarios objetivo {#choose-users-to-target}

A continuación, [segmenta a los usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) eligiendo Segments o filtros para acotar tu audiencia. Recibirás automáticamente una vista previa de cómo se ve esa población aproximada del Segment. Ten en cuenta que la pertenencia exacta al Segment siempre se calcula antes de que se envíe el mensaje.

{% multi_lang_include audience/target_audiences.md %}

#### Elige eventos de conversión {#choose-conversion-events}

Braze te permite hacer un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), después de recibir una campaña. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se cuenta una conversión si el usuario realiza la acción especificada.

{% endtab %}

{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu componente de Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, incluyendo las pruebas multivariante y [Optimizar con BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai), consulta [Construye tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas).

{% endtab %}
{% endtabs %}

## Paso 6: Revisar y desplegar {#step-6-review-and-deploy}

Cuando termines de crear tu Campaign o Canvas, revisa los detalles, [pruébalo]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) y luego envíalo. Para más información, consulta [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=content%20card).

{% alert note %}
Aunque las Content Cards no requieren notificaciones push en producción, los envíos de prueba requieren que push esté habilitado en tus dispositivos de prueba porque la tarjeta se entrega en la carga útil push. Las Content Cards de prueba caducan aproximadamente cinco minutos después de enviarse.
{% endalert %}

{% alert warning %}
Una vez que se lanza una Content Card, no se puede editar. Solo se puede detener su envío a nuevos usuarios y eliminarla de las fuentes de los usuarios. Consulta [Actualización de tarjetas enviadas]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-launched-cards) para entender cómo puedes abordar este escenario.
{% endalert %}

A continuación, consulta [Informes de Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/reporting) para aprender a acceder a los resultados de tus campañas de Content Cards.

## Cosas que debes saber {#things-to-know}

### Limitaciones de carga útil y fuente {#payload-and-feed-limitations}

Para mantener el rendimiento, Content Cards tiene dos restricciones clave: un límite en el tamaño de la carga útil de cada tarjeta y un número máximo de tarjetas que pueden aparecer en una fuente.

#### Limitaciones de tamaño para Content Cards {#size-limitations-for-content-cards}

La carga útil total de datos de una sola Content Card no puede superar los 2 KB **después** de que se haya procesado cualquier personalización con Liquid. Esto incluye:

* Título
* Mensaje
* URL de imagen (la longitud de la cadena de la URL en sí, no el tamaño del archivo de imagen)
* Texto del enlace
* URL de enlace para todas las plataformas especificadas (las URL separadas para iOS, Android y Web cuentan para el total)
* Pares clave-valor (tanto los nombres de las claves como sus valores)

Usar Liquid para incluir cadenas largas de texto (como de atributos personalizados) puede hacer que superes el límite.

El creador de la campaña muestra una advertencia si tu contenido estático supera el límite. No predecimos el tamaño del contenido dinámico con Liquid. Si el tamaño del mensaje supera los 2 KB, se cancela en el momento del envío. Puedes ver estas cancelaciones en el registro de actividad de mensajes con el motivo `Content card maximum size exceeded`.

{% alert important %}
Durante los envíos de prueba, las Content Cards que superen los 2 KB aún pueden entregarse y mostrarse correctamente.
{% endalert %}

A continuación, te presentamos algunas prácticas recomendadas para gestionar el tamaño de la carga útil de Content Cards:

* Usa acortadores de URL para enlaces largos. Las URL, especialmente las que incluyen parámetros de seguimiento extensos, pueden generar problemas con el límite de tamaño. Usar un servicio de acortamiento de URL puede reducir drásticamente el recuento de caracteres y liberar espacio en la carga útil.
* Trunca el contenido dinámico con Liquid. Al personalizar tarjetas con texto dinámico de atributos de usuario o llamadas a la API, la longitud del contenido puede ser impredecible. Usa proactivamente filtros de Liquid como `truncate` para limitar la longitud de cualquier texto dinámico.
* Sé eficiente con las URL multiplataforma. El límite de 2 KB incluye las URL de todas las plataformas que definas. Usar URL largas y únicas para cada plataforma puede multiplicar el tamaño de la carga útil. Si es posible, usa un único enlace que funcione en todas las plataformas, o usa acortadores de URL según sea necesario.
* Considera los Banners para contenido más enriquecido. Para casos de uso que requieren constantemente grandes cantidades de contenido, Content Cards puede no ser el canal adecuado. Los Banners no tienen la misma limitación de carga útil de 2 KB y son más adecuados para incrustar contenido más enriquecido directamente en una experiencia de aplicación o sitio web.

#### Número de tarjetas en la fuente {#number-of-cards-in-feed}

Cada usuario puede tener hasta 250 Content Cards no expiradas en su fuente en un momento dado. Cuando se supera este límite, Braze deja de devolver las tarjetas más antiguas, incluso si no se han leído. Las tarjetas descartadas también cuentan para este límite, lo que significa que un alto número de tarjetas descartadas puede reducir el espacio disponible para las más antiguas.

Para evitar problemas con el límite de tarjetas, te recomendamos las siguientes prácticas:

- **Usa fechas de expiración más cortas:** para Campaigns sensibles al tiempo (como una oferta de fin de semana), establece una fecha de expiración específica. De esta forma, las tarjetas se eliminan automáticamente de la fuente y ya no cuentan para el límite una vez que dejan de ser relevantes.
- **Aprovecha la eliminación basada en acciones:** configura eventos de eliminación para tarjetas transaccionales o basadas en objetivos. Por ejemplo, una tarjeta que solicita al usuario completar su perfil debe eliminarse tan pronto como se registre un evento `profile_completed`.
- **Audita las Campaigns de larga duración:** revisa las Campaigns recurrentes o en curso para asegurarte de que no estén generando una mala experiencia para tus usuarios al llenar la fuente con demasiadas tarjetas a lo largo del tiempo.

### Comprender la reelegibilidad para Content Cards {#understanding-re-eligibility-for-content-cards}

La reelegibilidad determina si un usuario puede recibir un mensaje de la misma Campaign más de una vez y cuándo. Para Content Cards, comprender cómo funciona esto es fundamental para gestionar Campaigns recurrentes y garantizar que los usuarios no reciban mensajes duplicados o desactualizados.

{% alert tip %}
¿Quieres que tu contenido dure más de 30 días? Prueba los [Banners]({{site.baseurl}}/user_guide/channels/banners).
{% endalert %}

#### Cómo se calcula la reelegibilidad {#how-re-eligibility-is-calculated}

Si activas la reelegibilidad, la cuenta regresiva para que un usuario pueda "reingresar" a una Campaign comienza después de que se le envía el mensaje. El momento específico en que esta cuenta regresiva inicia depende de la configuración de creación de la tarjeta:

- Las Content Cards que usan [en la primera impresión]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences) utilizan el momento de la impresión para calcular la reelegibilidad.
- Las Content Cards creadas en el lanzamiento de la Campaign, en Campaigns multicanal o en la entrada al paso en Canvas, utilizan el momento de envío o de impresión más reciente.

#### La expiración de 30 días y la reelegibilidad {#the-30-day-expiration-and-re-eligibility}

Una fuente común de confusión es la interacción entre la reelegibilidad de la Campaign y la expiración automática de 30 días de todas las Content Cards.

Todas las Content Cards se purgan automáticamente de los sistemas de Braze 30 días después de ser enviadas o eliminadas. Si tienes una Campaign recurrente de larga duración con la reelegibilidad **desactivada**, un usuario puede recibir la misma tarjeta de nuevo después de 30 días. Cuando la tarjeta original se purga, el sistema ya no tiene un registro de que ese usuario haya recibido la Campaign, lo que lo hace elegible de nuevo en su siguiente sesión.

Para que los usuarios solo reciban un mensaje de una Campaign específica una vez, añade un filtro de audiencia a tu Campaign o paso en Canvas para usuarios que no hayan recibido un mensaje de esta Campaign. Este filtro es la forma más confiable de evitar envíos duplicados en Campaigns de larga duración.

### Gestionar Content Cards en vivo {#managing-live-content-cards}

Después de que se envían las Content Cards, quedan esperando en un "buzón de entrada" listas para ser entregadas al usuario (similar a lo que sucede con los correos electrónicos). Una vez que el contenido se carga en la Content Card (en el momento de la visualización), no se puede cambiar durante su vida útil. Esto aplica incluso si llamas a una API a través de contenido conectado y los datos del endpoint cambian. Estos datos no se actualizan. Solo se puede detener el envío a nuevos usuarios y eliminarlo de las fuentes de los usuarios. Si modificas una Campaign, solo las tarjetas enviadas después de la modificación incluyen la actualización.

#### Actualizar tarjetas ya lanzadas {#updating-launched-cards}

Para cambiar una tarjeta para usuarios que ya la han recibido, debes utilizar uno de los siguientes métodos:

##### Opción 1: Duplicar la Campaign (recomendado para cambios inmediatos) {#option-1-duplicate-the-campaign-recommended-for-immediate-changes}

{% alert tip %}
Recomendamos esta opción para mensajes en los que estés mostrando el contenido más reciente en la tarjeta, los cambios deban mostrarse de inmediato o cuando la reelegibilidad esté desactivada.
{% endalert %}

El primer enfoque es archivar la Campaign y lanzar una nueva Campaign duplicada:

1. Detén la Campaign original y, cuando se te solicite, selecciona `Remove card after the next sync`.
2. Duplica la Campaign, haz tus ediciones y lanza la nueva versión.

Cuando duplicas la Campaign, debes definir la audiencia para la nueva versión. Usa filtros de segmentación para controlar quién recibe la tarjeta actualizada:
* Si los usuarios nunca deben ser reelegibles para una Content Card, puedes filtrar por usuarios que no hayan recibido la versión anterior de la Content Card estableciendo el filtro `Received Message from Campaign` con la condición `Has Not`.
* Si los usuarios que recibieron la tarjeta anterior deben ser reelegibles en X días, puedes establecer el filtro para `Last Received Message from specific campaign` a más de X días atrás **O** `Received Message from Campaign` con la condición `Has Not`.

###### Impacto {#impact}

- **Destinatarios existentes:** tanto los destinatarios nuevos como los existentes ven la tarjeta actualizada en la siguiente actualización de la fuente si son elegibles.
- **Informes:** cada versión de la tarjeta tiene análisis separados.

Supongamos que configuras una Campaign para que se active al inicio de sesión, y tiene la reelegibilidad establecida en 30 días. Un usuario recibió la Campaign hace dos días y quieres cambiar el texto. Primero, archiva la Campaign y elimina las tarjetas de la fuente. Segundo, duplica la Campaign y relánzala con el nuevo texto. Si el usuario tiene otra sesión, recibe inmediatamente la nueva tarjeta.

##### Opción 2: Detener y relanzar la misma Campaign {#option-2-stop-and-relaunch-the-same-campaign}

{% alert tip %}
Recomendamos usar esta opción para mensajes únicos en un centro de notificaciones o buzón de mensajes (como promociones), cuando es importante que los análisis estén unificados, o cuando la inmediatez del mensaje no es una preocupación (como cuando los destinatarios existentes pueden esperar la ventana de elegibilidad antes de ver las tarjetas actualizadas).
{% endalert %}

Este enfoque mantiene todos tus análisis unificados en una sola Campaign. Los usuarios recién elegibles reciben la nueva tarjeta, pero retrasa la actualización para los destinatarios existentes hasta que sean reelegibles:

1. Detén tu Campaign y, cuando se te solicite, selecciona **Remove card after the next sync**.
2. Edita tu Campaign según sea necesario.
3. Reinicia tu Campaign.

###### Impacto

* **Destinatarios existentes:** los usuarios que ya recibieron la tarjeta no reciben las tarjetas actualizadas hasta que se vuelvan reelegibles. Si la reelegibilidad está desactivada, nunca reciben la nueva tarjeta.
* **Informes:** una sola Campaign contiene todos los análisis de informes para las versiones de tarjetas lanzadas. Braze no diferencia entre las versiones lanzadas.

Supongamos que tienes una Campaign que se activa al inicio de sesión y tiene la reelegibilidad establecida en 30 días. Un usuario recibió la Campaign hace dos días y quieres cambiar el texto. Primero, detén la Campaign y elimina la tarjeta de la fuente. Segundo, vuelve a publicar la Campaign con el nuevo texto. Si el usuario tiene otra sesión, recibe la nueva tarjeta en 28 días.

{% alert note %}
Si detienes una Campaign, editas la configuración del evento de eliminación y reinicias la Campaign sin eliminar las tarjetas de la fuente, cualquier tarjeta existente en las fuentes de los usuarios usará la configuración actualizada del evento de eliminación. Las tarjetas no conservan la configuración original del evento de eliminación del momento en que se enviaron por primera vez.
{% endalert %}

#### Eliminar y expirar tarjetas {#removing-and-expiring-cards}

##### Eliminación manual de tarjetas {#manual-card-removal}

Puedes eliminar manualmente las tarjetas de las fuentes de todos los usuarios en cualquier momento deteniendo la Campaign.

1. Abre la Campaign de Content Cards y selecciona Stop Campaign.
2. Cuando se te solicite, selecciona **Remove card after the next sync**. La tarjeta se elimina en la siguiente actualización de la fuente.

##### Eliminación automatizada de tarjetas {#action-based-card-removal}

Puedes eliminar automáticamente una tarjeta cuando un usuario realiza una acción específica, como completar una compra o activar una característica.

En tu Campaign o paso en Canvas, especifica un evento de eliminación. Cuando un usuario realiza ese evento, la tarjeta se elimina de su fuente en una actualización posterior después de que Braze procese el evento.

{% alert note %}
Esta eliminación no es instantánea. Hay un retraso en el procesamiento, por lo que puede tomar varios minutos y más de una actualización de la fuente para que la tarjeta desaparezca.
{% endalert %}

{% alert tip %}
Puedes especificar múltiples eventos personalizados y compras que eliminen una tarjeta de la fuente de un usuario. Cuando el usuario realiza cualquiera de esas acciones, cualquier tarjeta existente enviada por las tarjetas de la Campaign se elimina. Las tarjetas elegibles continúan enviándose según el calendario del mensaje.
{% endalert %}

![Panel de condiciones de eliminación de Content Cards con la opción de evento de eliminación de Content Cards.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### Expiración de tarjetas {#card-expiration}

Las Content Cards permanecen disponibles hasta 30 días desde su envío; después de 30 días, Braze las elimina de las fuentes de los usuarios y las purga de los sistemas de Braze.

#### Hacer que las tarjetas duren más de 30 días {#making-cards-last-longer-than-30-days}

{% alert tip %}
Para casos de uso que requieren que los mensajes persistan más allá del límite de 30 días de Content Cards, considera usar Banners. Los Banners están diseñados para la persistencia y no tienen una fecha de expiración obligatoria, lo que les permite permanecer visibles durante el tiempo que se necesiten.
{% endalert %}

Si quieres que una tarjeta parezca estar siempre disponible, puedes crear una Campaign recurrente que reemplace efectivamente la tarjeta cada 30 días:

1. Establece la duración de la Content Card en 30 días.
2. Establece la reelegibilidad de la Campaign en 30 días.
3. Configura la Campaign para que se active en "Inicio de sesión".

### Sincronización y actualización de Content Cards {#content-card-sync-and-refresh}

Las Content Cards se sincronizan según un calendario y cuando tu aplicación actualiza la fuente. El comportamiento de sincronización difiere entre sincronizaciones completas y parciales, y tu integración de SDK or kit de desarrollo de software afecta cuándo se actualizan las tarjetas al inicio de sesión. Para detalles de implementación, consulta [Personalizar la fuente de Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed) y [Crear Content Cards]({{site.baseurl}}/developer_guide/content_cards/creating_cards).

### Impacto de detener Campaigns de Content Cards {#impact-of-stopping-content-cards-campaigns}

Cuando detienes una Campaign y seleccionas **Remove card after the next sync**, Braze elimina la tarjeta de las fuentes de los usuarios en la siguiente actualización. Los recuentos de impresiones pueden ser menores que los recuentos de envíos porque los usuarios no pueden registrar impresiones de tarjetas que se eliminan antes de que las vean.

## Solución de problemas {#troubleshooting}

### ¿Por qué las Content Cards no aparecen inmediatamente después de un evento desencadenante? {#why-dont-content-cards-appear-immediately-after-a-trigger-event}

Para las campañas de entrega basada en acciones (como el inicio de sesión), existe un breve retraso esperado entre el evento desencadenante y la disponibilidad de la tarjeta. Este retraso se produce porque:

- El evento desencadenante se envía a los servidores de Braze
- Se desencadena la Campaign y se registra la elegibilidad del usuario
- La Content Card se crea en la base de datos para ese usuario
- El SDK or kit de desarrollo de software se sincroniza y descarga todas las tarjetas disponibles en el dispositivo

Si la sincronización del SDK or kit de desarrollo de software ocurre antes de que se registre la elegibilidad del usuario, este no recibe la tarjeta.

Para los nuevos usuarios en su primera sesión, este retraso es inevitable. Para los usuarios existentes que necesitan disponibilidad inmediata, considera utilizar la entrega programada en su lugar.

Si necesitas minimizar los retrasos tanto para usuarios nuevos como existentes, puedes crear dos campañas:

- **Usuarios existentes con un recuento de sesiones mayor que 0:** usa una Campaign de entrega programada. Las tarjetas se crean previamente y están disponibles de inmediato.
- **Usuarios nuevos con un recuento de sesiones igual a 0:** usa una Campaign desencadenada por acción. Las tarjetas se crean después del primer desencadenante de sesión.

Este enfoque garantiza que los usuarios existentes vean las tarjetas de forma instantánea, mientras que los nuevos usuarios las reciben tras un breve retraso en su primera sesión. Para estrategias adicionales para mejorar la latencia, consulta [Mejorar la baja latencia para Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/best_practices/improving_low_latency_requirements).

### ¿Por qué las marcas de tiempo de impresión o descarte caen fuera del calendario de la Campaign? {#why-do-impression-or-dismiss-timestamps-fall-outside-the-campaign-schedule}

Las marcas de tiempo de impresión y descarte en los análisis y Currents reflejan cuándo un usuario ve o descarta una Content Card, no cuándo Braze la crea o la envía. Una tarjeta puede permanecer en la fuente de un usuario hasta que se actualicen las Content Cards, por lo que las marcas de tiempo de impresión y descarte pueden caer después de la ventana de envío de la Campaign.

Si los tiempos aún parecen inesperados:

- Confirma si estás viendo los análisis en la zona horaria de tu empresa o en la zona horaria del usuario en Currents.
- Verifica que el usuario realmente vio o descartó la tarjeta después de recibirla, en lugar de comparar únicamente con el momento de envío.

Para más información sobre las métricas de Content Cards, consulta [Informes de Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/reporting).

### Error "Todos los valores de caducidad de una Campaign deben coincidir" {#all-expiration-values-for-a-campaign-must-match-error}

Este error aparece cuando una Campaign de Content Cards multivariante utiliza diferentes configuraciones de caducidad entre variantes. Establece la misma caducidad (duración o momento específico) en cada variante, o reduce la Campaign a una sola variante, y luego guarda de nuevo. Para saber cómo configurar la caducidad al crear una Campaign, consulta [Elegir un calendario de entrega o desencadenante](#choose-a-delivery-schedule-or-trigger).