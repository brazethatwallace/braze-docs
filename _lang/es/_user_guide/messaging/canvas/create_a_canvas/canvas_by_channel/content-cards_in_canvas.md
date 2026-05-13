---
nav_title: Content Cards
article_title: Content Cards en Canvas
page_order: 1
page_type: reference
description: "Este artículo de referencia describe las características y matices específicos del uso de Content Cards como canal de mensajería dentro de Canvas."
tool: Canvas
channel: content cards

---

# Content Cards en Canvas {#content-cards-in-canvas}

> Las Content Cards pueden enviarse a tus clientes como parte de su recorrido en Canvas. Este artículo describe las características y matices específicos del uso de Content Cards como canal de mensajería dentro de Canvas.

Al igual que con otros canales de mensajería de Canvas, las Content Cards se enviarán al dispositivo del usuario cuando cumpla los criterios de audiencia y segmentación especificados para ese paso. Una vez enviada la Content Card, estará disponible en la fuente de cada usuario elegible la próxima vez que se actualice su fuente de tarjetas.

![Content Cards seleccionadas como canal de mensajería para un paso de mensaje.]({% image_buster /assets/img_archive/content-cards-in-canvas.png %})

Dos opciones que cambiarán la forma en que el paso de Content Card interactúa con Canvas son su [expiración](#content-card-expiration) y [eliminación](#removal).

## Expiración de Content Cards {#content-card-expiration}

Al componer una nueva Content Card, puedes elegir cuándo debe expirar de la fuente del usuario en función de su hora de envío. La cuenta regresiva para la expiración de una Content Card comienza cuando el usuario llega al paso de mensaje en el Canvas donde se envía la tarjeta. La tarjeta estará activa en la fuente del usuario desde ese momento hasta que expire. Una tarjeta puede existir en la fuente de un usuario durante un máximo de 30 días.

![Configuración de expiración para una Content Card de un paso de mensaje que se eliminará después de tres horas en la fuente del usuario.]({% image_buster /assets/img_archive/content-cards-in-canvas-expiration.png %})

### Tipos de expiración {#types-of-expiration}

Tienes dos formas de establecer cuándo una tarjeta debe desaparecer de la fuente de un usuario: una fecha relativa o una fecha absoluta.

#### Fechas relativas {#relative-dates}

Cuando eliges una fecha relativa, como "Quitar tarjetas enviadas después de 5 días en la fuente del usuario", puedes establecer una fecha de expiración de hasta 30 días.

#### Fechas absolutas {#absolute-dates}

Cuando eliges una fecha absoluta, como "Quitar tarjetas enviadas el 1 de diciembre de 2023 a las 4 pm", hay algunos matices a tener en cuenta.

Aunque puedes especificar una duración de expiración superior a 30 días, la Content Card existirá en la fuente del usuario durante un máximo de 30 días. Especificar una duración superior a 30 días te permite tener en cuenta cualquier retraso antes de desencadenar el paso de mensaje, pero no extiende la vida máxima de la tarjeta en la fuente del usuario.

Ten precaución al establecer una fecha de expiración con más de 30 días de anticipación respecto al lanzamiento del Canvas. Si un usuario llega al paso de mensaje más de 30 días antes de la fecha de expiración especificada, la tarjeta no se enviará.

### Comportamiento de expiración {#expiration-behavior}

La Content Card permanece disponible en la fuente del usuario hasta que alcanza su fecha de expiración, incluso si el usuario avanza a pasos posteriores en el recorrido de Canvas. Si no quieres que la Content Card esté activa cuando se entreguen los siguientes pasos del Canvas, asegúrate de que la expiración sea más corta que el retraso en los pasos posteriores.

Después de que una Content Card expire, se eliminará automáticamente de la fuente del usuario durante la siguiente actualización, incluso si no la ha visto todavía.

## Eliminación de Content Cards {#removal}

Las Content Cards pueden eliminarse cuando los usuarios completan una compra o realizan un evento personalizado. Puedes seleccionar uno de los siguientes como evento de eliminación: **Perform Custom Event** y **Place Order**. Luego, selecciona **Add Trigger**.

!["Quitar tarjetas cuando los usuarios completen una compra o realicen un evento personalizado." seleccionado con el desencadenante para quitar tarjetas de usuarios que realizan una compra específica.]({% image_buster /assets/img_archive/content-cards-in-canvas-removal-event.png %})

## Informes y análisis {#reporting-and-analytics}

Después de lanzar un paso de Content Cards en Canvas, puedes comenzar a analizar varias métricas diferentes para este paso. Estas métricas incluyen el número de mensajes enviados, destinatarios únicos, tasas de conversión, ingresos totales y más.

![Análisis de un paso de mensaje con el rendimiento del mensaje de Content Card.]({% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %})

Para más información sobre las métricas disponibles y sus definiciones, consulta nuestro [Glosario de métricas de informes]({{site.baseurl}}/user_guide/analytics/metrics_glossary/).

## Casos de uso {#use-cases}

#### Ofertas promocionales {#promotional-offers}

Añade tarjetas a la fuente de un usuario a medida que califique para promociones y anuncios específicos. Por ejemplo, si un usuario se vuelve elegible para una nueva oferta después de realizar una acción o hacer una compra, usando Canvas puedes enviarle una Content Card, además de otros canales de mensajería, para que la próxima vez que abra la aplicación la oferta esté disponible.

#### Buzón de entrada de notificaciones push {#push-notification-inbox}

Hay ocasiones en las que un usuario puede descartar una notificación push o eliminar un correo electrónico, pero quieres recordarle o promocionar la oferta en caso de que cambie de opinión.

Usando Canvas, puedes añadir un componente que envíe tanto una Content Card como una notificación push para dar a los usuarios un "buzón de entrada" persistente de tarjetas que se alineen con los mensajes promocionales enviados a través de push.

#### Múltiples fuentes basadas en categorías {#multiple-feeds-based-on-categories}

Puedes separar tus Content Cards en múltiples fuentes basadas en categorías, como diferentes temas que los usuarios pueden examinar, o fuentes transaccionales y de marketing. Para más información sobre cómo crear múltiples fuentes usando pares clave-valor, consulta nuestra guía para [Personalizar fuentes de Content Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).