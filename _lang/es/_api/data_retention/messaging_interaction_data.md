---
nav_title: "Datos de interacción de mensajería"
article_title: "Datos de interacción de mensajería"
alias: "/messaging_interaction_data/"
page_order: 1
description: "Este artículo de referencia cubre los datos de interacción de Campaigns y Canvas y su disponibilidad."
page_type: reference
---

# Acerca de la disponibilidad de los datos de interacción de mensajería {#about-messaging-interaction-data-availability}

> Aprende sobre los datos de interacción de mensajería para Campaigns y Canvas, incluyendo cuánto tiempo los conserva Braze y qué características los utilizan para reorientar.

## ¿Qué son los datos de interacción de mensajería? {#what-is-messaging-interaction-data}

Los datos de interacción de mensajería se refieren a cómo un usuario interactúa con una Campaign o un Canvas que recibió (por ejemplo, cuando un usuario abre la Campaign A o un usuario recibe la variante A). Estos datos se utilizan para reorientar.

## ¿Cuándo están disponibles los datos de interacción de mensajería? {#when-is-messaging-interaction-data-available}

Los datos de interacción siempre están disponibles. Para Campaigns y Canvas activos, los datos de interacción siempre están disponibles en tiempo real.

Para Campaigns y Canvas detenidos, sus datos de interacción caducan después de tres meses a menos que se utilicen en filtros de reorientación por parte de Campaigns o Canvas activos. Los datos de interacción caducados se trasladan al almacenamiento a largo plazo y no están disponibles para su uso a menos que se restauren mediante el proceso descrito.

Los datos de interacción caducados nunca se eliminan y pueden restaurarse en cualquier momento.

### Características que utilizan datos de interacción {#features-that-use-interaction-data}

Las siguientes características utilizan datos de interacción de mensajería:

- Filtros de reorientación que reorientan en una Campaign o Canvas específico
    - Clicked Alias in Campaign
    - Clicked Alias in Canvas Step
    - Clicked/Opened Campaign
    - Clicked/Opened Step
    - Converted From Campaign
    - Converted From Canvas
    - Entered Canvas Variation
    - In Campaign Control Group
    - In Canvas Control Group
    - Last Received Message from Specific Campaign
    - Last Received Message from Specific Canvas Step
    - Received Campaign Variant
    - Received Message from Campaign
    - Received Message from Canvas Step
- Filtros de reorientación que reorientan en Campaigns o Canvas de una etiqueta determinada
    - Received Message from Campaign or Canvas with Tag
    - Clicked/Opened Campaign or Canvas With Tag
    - Last Received Message from Campaign or Canvas With Tag
- Listas de **Campaigns Received** y **Canvas Messages Received** en el perfil de usuario
- Endpoint `/users/export`
- Exportaciones CSV de **datos de usuario** en las páginas de resumen de Campaign y Canvas

Estas características no incluyen datos de interacción caducados en sus resultados. Para incluir datos de interacción caducados en los resultados de estas características, restaura la Campaign o el Canvas con datos caducados.

Por ejemplo, los Canvas no pueden lanzarse si los datos de interacción han caducado, lo que significa que una edición como añadir un equipo al Canvas no puede guardarse.

### Características que no utilizan datos de interacción {#features-that-dont-use-interaction-data}

Las siguientes características **no** utilizan datos de interacción de mensajería, lo que significa que estas características no se ven afectadas por la caducidad de los datos de interacción de mensajería:

- Configuración de Campaign y Canvas
- Análisis de Campaign y Canvas
- Informes de análisis (como el generador de informes, el generador de consultas e informes de participación)
- Currents
- Snowflake Data Share
- Extensiones de segmento
- Puntos de datos
- Los siguientes filtros de reorientación:
    - Clicked Alias in Any Campaign or Canvas Step
    - Feature Flags
    - Hard Bounced
    - Has Marked You As Spam
    - Has Never Received a Message from Campaign or Canvas Step
    - Invalid Phone Number
    - Last Engaged With Message
    - Last Enrolled in Any Control Group
    - Last In App Message Impression
    - Last Received Any Message
    - Last Received Email
    - Last Received Push
    - Last Received SMS
    - Last Received Webhook
    - Last Received WhatsApp
    - Last Sent Specific SMS Inbound Keyword Category
    - Last Viewed News Feed
    - News Feed View Count

## ¿Cómo restauro los datos de interacción de mensajería? {#how-do-i-restore-messaging-interaction-data}

Para restaurar tus datos de interacción, sigue estos pasos:

1. Ve a la Campaign o Canvas caducado.
2. En la parte superior de la página de destino de la Campaign o Canvas, selecciona **Restaurar datos de interacción** en el banner.

También puedes restaurar datos de interacción para varias Campaigns desde la página **Campaigns** seleccionando las Campaigns y luego seleccionando **Restaurar datos de interacción**.

El tiempo para restaurar los datos de interacción puede variar, pero en la mayoría de los casos, este proceso puede tardar entre 5 y 15 minutos. Una vez completada la restauración, recibirás un correo electrónico.

### Restaurar por etiqueta {#restoring-by-tag}

También puedes restaurar datos de interacción para Campaigns o Canvas caducados con una etiqueta determinada.

1. Ve a la página **Campaigns** o **Canvas** y busca por la etiqueta correspondiente.
2. Selecciona tus Campaigns o Canvas.
3. Selecciona **Restaurar datos de interacción** para restaurar los datos de esas Campaigns o Canvas.

Después de otros tres meses de inactividad, estas Campaigns o Canvas caducan de nuevo.

### Reorientar por etiqueta {#retargeting-by-tag}

Las Campaigns que utilizan filtros de reorientación que reorientan por etiqueta no están exentas de la caducidad. Los filtros de reorientación que reorientan por etiqueta incluyen:

- Received Message from Campaign or Canvas with Tag
- Clicked/Opened Campaign or Canvas With Tag
- Last Received Message from Campaign or Canvas With Tag

## ¿Cuándo estuvieron disponibles los datos de interacción de mensajería en el pasado? {#when-was-messaging-interaction-data-available-in-the-past}

Anteriormente, los datos de interacción de mensajes se eliminaban cuando una Campaign o un Canvas:

- No había enviado mensajes en 25 meses calendario, Y
- No se utilizaba para reorientar en ninguna Campaign, Canvas o Content Cards activos.

Las Campaigns y Canvas con datos de interacción de mensajería previamente eliminados no se pueden utilizar en filtros de reorientación para Campaigns, Canvas y Segments.

## Solución de problemas {#troubleshooting}

### ¿Por qué la fecha de expiración de una Campaign o un Canvas sigue mostrando mañana? {#why-does-a-campaign-or-canvas-expiration-date-keep-showing-tomorrow}

Si una Campaign o un Canvas detenido todavía está referenciado por un filtro de reorientación activo (por ejemplo, en un Segment activo, una Campaign, un Canvas o una Content Card), Braze aún no descarga sus datos de interacción.

En este caso, la fecha de expiración que se muestra en la interfaz de usuario refleja la próxima ejecución de limpieza programada, por lo que puede aparecer como "mañana" y seguir avanzando mientras existan referencias.

Después de eliminar todas las referencias de reorientación activas, los datos de interacción se descargan en el siguiente ciclo de limpieza (normalmente al día siguiente).

Es posible que encuentres los siguientes mensajes de error al intentar reanudar o desarchivar Campaigns, Canvas o Content Cards con datos de interacción expirados:

| Mensaje de error | Cuándo aparece | Solución de problemas |
| --- | --- | --- |
| "Can't resume Canvases because at least one Canvas is using filters or segments that have expired data. Remove these and try again." | Cuando intentas reanudar uno o más Canvas (acción masiva) que usan filtros o Segments con datos de interacción expirados | [Restaurar datos de interacción](#how-do-i-restore-messaging-interaction-data) para las Campaigns o Canvas referenciados en los filtros, o eliminar los filtros afectados del Canvas |
| "Can't resume {name} because it is using filters or segments that have expired data. Remove these and try again." | Cuando intentas reanudar un solo Canvas que usa filtros o Segments con datos de interacción expirados | [Restaurar datos de interacción](#how-do-i-restore-messaging-interaction-data) para las Campaigns o Canvas referenciados en los filtros, o eliminar los filtros afectados del Canvas |
| "Resume is only available for stopped Canvases with available interaction data" | Cuando intentas reanudar un Canvas desde el menú de acción masiva, pero el Canvas tiene datos de interacción expirados | [Restaurar datos de interacción](#how-do-i-restore-messaging-interaction-data) para el Canvas |
| "You can't resume these Campaigns. One or more Campaigns include expired filters." | Cuando intentas reanudar una o más Campaigns que usan filtros con datos de interacción expirados | [Restaurar datos de interacción](#how-do-i-restore-messaging-interaction-data) para las Campaigns o Canvas referenciados en los filtros, o eliminar los filtros afectados de la Campaign |
| "You can't unarchive these Cards. One or more Cards include expired filters." | Cuando intentas desarchivar una o más Content Cards que usan filtros con datos de interacción expirados | [Restaurar datos de interacción](#how-do-i-restore-messaging-interaction-data) para las Campaigns o Canvas referenciados en los filtros, o eliminar los filtros afectados de la tarjeta |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mensajes de error comunes" }