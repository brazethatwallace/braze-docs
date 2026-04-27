---
nav_title: Tarjetas de contenido
article_title: Tarjetas de contenido en Canvas
page_order: 1
page_type: reference
description: "Este artículo de referencia describe las características y matices específicos del uso de tarjetas de contenido como canal de mensajería dentro de Canvas."
tool: Canvas
channel: content cards

---

# Tarjetas de contenido en Canvas

> Las tarjetas de contenido pueden enviarse a tus clientes como parte de su recorrido en Canvas. Este artículo describe las características y matices específicos del uso de tarjetas de contenido como canal de mensajería dentro de Canvas.

Al igual que con otros canales de mensajería de Canvas, las tarjetas de contenido se enviarán al dispositivo del usuario cuando cumpla los criterios de audiencia y segmentación especificados para ese paso. Una vez enviada la tarjeta de contenido, estará disponible en la fuente de cada usuario elegible la próxima vez que se actualice su fuente de tarjetas.

![Tarjetas de contenido seleccionadas como canal de mensajería para un paso de mensaje.]({% image_buster /assets/img_archive/content-cards-in-canvas.png %})

Dos opciones que cambiarán la forma en que el paso de tarjeta de contenido interactúa con Canvas son su [expiración](#content-card-expiration) y [eliminación](#removal).

## Expiración de tarjetas de contenido {#content-card-expiration}

Al componer una nueva tarjeta de contenido, puedes elegir cuándo debe expirar de la fuente del usuario en función de su hora de envío. La cuenta regresiva para la expiración de una tarjeta de contenido comienza cuando el usuario llega al paso de mensaje en el Canvas donde se envía la tarjeta. La tarjeta estará activa en la fuente del usuario desde ese momento hasta que expire. Una tarjeta puede existir en la fuente de un usuario durante un máximo de 30 días.

![Configuración de expiración para una tarjeta de contenido de un paso de mensaje que se eliminará después de tres horas en la fuente del usuario.]({% image_buster /assets/img_archive/content-cards-in-canvas-expiration.png %})

### Tipos de expiración

Tienes dos formas de establecer cuándo una tarjeta debe desaparecer de la fuente de un usuario: una fecha relativa o una fecha absoluta.

#### Fechas relativas

Cuando eliges una fecha relativa, como "Quitar tarjetas enviadas después de 5 días en la fuente del usuario", puedes establecer una fecha de expiración de hasta 30 días.

#### Fechas absolutas

Cuando eliges una fecha absoluta, como "Quitar tarjetas enviadas el 1 de diciembre de 2023 a las 4 pm", hay algunos matices a tener en cuenta.

Aunque puedes especificar una duración de expiración superior a 30 días, la tarjeta de contenido existirá en la fuente del usuario durante un máximo de 30 días. Especificar una duración superior a 30 días te permite tener en cuenta cualquier retraso antes de desencadenar el paso de mensaje, pero no extiende la vida máxima de la tarjeta en la fuente del usuario.

Ten precaución al establecer una fecha de expiración con más de 30 días de anticipación respecto al lanzamiento del Canvas. Si un usuario llega al paso de mensaje más de 30 días antes de la fecha de expiración especificada, la tarjeta no se enviará.

### Comportamiento de expiración

La tarjeta de contenido permanece disponible en la fuente del usuario hasta que alcanza su fecha de expiración, incluso si el usuario avanza a pasos posteriores en el recorrido de Canvas. Si no quieres que la tarjeta de contenido esté en vivo cuando se entreguen los siguientes pasos del Canvas, asegúrate de que la expiración sea más corta que el retraso en los pasos posteriores.

Después de que una tarjeta de contenido expire, se eliminará automáticamente de la fuente del usuario durante la siguiente actualización, incluso si no la ha visto todavía.

## Eliminación de tarjetas de contenido {#removal}

Las tarjetas de contenido pueden eliminarse cuando los usuarios completan una compra o realizan un evento personalizado. Puedes seleccionar uno de los siguientes como evento de eliminación: **Realizar evento personalizado** y **Realizar compra**. Luego, selecciona **Añadir evento**.

!["Quitar tarjetas cuando los usuarios completen una compra o realicen un evento personalizado." seleccionado con el desencadenante para quitar tarjetas de usuarios que realizan una compra específica de "Bracelet".]({% image_buster /assets/img_archive/content-cards-in-canvas-removal-event.png %})

## Informes y análisis

Después de lanzar un paso de tarjetas de contenido en Canvas, puedes comenzar a analizar varias métricas diferentes para este paso. Estas métricas incluyen el número de mensajes enviados, destinatarios únicos, tasas de conversión, ingresos totales y más.

![Análisis de un paso de mensaje con el rendimiento del mensaje de tarjeta de contenido.]({% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %})

Para más información sobre las métricas disponibles y sus definiciones, consulta nuestro [Glosario de métricas de informes]({{site.baseurl}}/user_guide/analytics/metrics_glossary/).

## Casos de uso

#### Ofertas promocionales

Añade tarjetas a la fuente de un usuario a medida que califique para promociones y anuncios específicos. Por ejemplo, si un usuario se vuelve elegible para una nueva oferta después de realizar una acción o hacer una compra, usando Canvas puedes enviarle una tarjeta de contenido, además de otros canales de mensajería, para que la próxima vez que abra la aplicación la oferta esté disponible.

#### Buzón de entrada de notificaciones push

Hay ocasiones en las que un usuario puede descartar una notificación push o eliminar un correo electrónico, pero quieres recordarle o promocionar la oferta en caso de que cambie de opinión.

Usando Canvas, puedes añadir un componente que envíe tanto una tarjeta de contenido como una notificación push para dar a los usuarios un "buzón de entrada" persistente de tarjetas que se alineen con los mensajes promocionales enviados a través de push.

#### Múltiples fuentes basadas en categorías

Puedes separar tus tarjetas de contenido en múltiples fuentes basadas en categorías, como diferentes temas que los usuarios pueden examinar, o fuentes transaccionales y de marketing. Para más información sobre cómo crear múltiples fuentes usando pares clave-valor, consulta nuestra guía para [Personalizar fuentes de tarjetas de contenido]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).