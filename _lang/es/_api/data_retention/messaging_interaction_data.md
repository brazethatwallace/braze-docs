---
nav_title: "Datos de interacción de mensajería"
article_title: "Datos de interacción de mensajería"
alias: "/messaging_interaction_data/"
page_order: 1
description: "Este artículo de referencia cubre los datos de interacción de campañas y Canvas y su disponibilidad."
page_type: reference
---

# Acerca de la disponibilidad de los datos de interacción de mensajería {#about-messaging-interaction-data-availability}

> Aprende sobre los datos de interacción de mensajería para campañas y Canvas, incluyendo cuánto tiempo los conserva Braze y qué características los utilizan para reorientar.

### ¿Qué son los datos de interacción de mensajería? {#what-is-messaging-interaction-data}

Los datos de interacción de mensajería se refieren a cómo un usuario interactúa con una campaña o un Canvas que recibió (por ejemplo, cuando un usuario abre la campaña A o un usuario recibe la variante A). Estos datos se utilizan para reorientar.

### ¿Cuándo están disponibles los datos de interacción de mensajería? {#when-is-messaging-interaction-data-available}

Los datos de interacción siempre están disponibles. Para campañas y Canvas activos, los datos de interacción siempre están disponibles en tiempo real.

Para campañas y Canvas detenidos, sus datos de interacción expiran después de tres meses a menos que se utilicen en filtros de reorientación por campañas o Canvas activos. Los datos de interacción expirados se trasladan a almacenamiento a largo plazo y no están disponibles para su uso a menos que se restauren mediante el proceso descrito a continuación.

Los datos de interacción expirados nunca se eliminan y pueden restaurarse en cualquier momento.

#### Características que utilizan datos de interacción {#features-that-use-interaction-data}

Las siguientes características utilizan datos de interacción de mensajería:

- Filtros de reorientación que reorientan en una campaña o Canvas específico
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
- Filtros de reorientación que reorientan en campañas o Canvas con una etiqueta determinada
    - Received Message from Campaign or Canvas with Tag
    - Clicked/Opened Campaign or Canvas With Tag
    - Last Received Message from Campaign or Canvas With Tag
- Listas de **Campaigns Received** y **Canvas Messages Received** en el perfil de usuario
- Punto de conexión `/users/export`
- Exportaciones CSV de **User Data** en las páginas de resumen de campañas y Canvas

Estas características no incluyen datos de interacción expirados en sus resultados. Para incluir datos de interacción expirados en los resultados de estas características, restaura la campaña o el Canvas con datos expirados.

Por ejemplo, los Canvas no pueden lanzarse si los datos de interacción están expirados, lo que significa que una edición como agregar un equipo al Canvas no puede guardarse.

#### Características que no utilizan datos de interacción {#features-that-dont-use-interaction-data}

Las siguientes características **no** utilizan datos de interacción de mensajería, lo que significa que estas características no se ven afectadas por la expiración de los datos de interacción de mensajería:

- Configuración de campañas y Canvas
- Análisis de campañas y Canvas
- Informes de análisis (como el Generador de informes, el Generador de consultas y los Informes de participación)
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

### ¿Cómo restauro los datos de interacción de mensajería? {#how-do-i-restore-messaging-interaction-data}

Para restaurar tus datos de interacción, sigue estos pasos:

1. Ve a la campaña o el Canvas expirado.
2. En la parte superior de la página de destino de la campaña o el Canvas, selecciona **Restore interaction data** en el banner.

También puedes restaurar datos de interacción para múltiples campañas desde la página **Campaigns** seleccionando las campañas y luego seleccionando **Restore interaction data**.

El tiempo para restaurar los datos de interacción puede variar, pero en la mayoría de los casos, este proceso puede tardar entre 5 y 15 minutos. Una vez completada la restauración, recibirás un correo electrónico.

#### Restaurar por etiqueta {#restoring-by-tag}

También puedes restaurar datos de interacción para campañas o Canvas expirados con una etiqueta determinada.

1. Ve a la página de **Campaigns** o **Canvas** y busca por la etiqueta correspondiente.
2. Selecciona tus campañas o Canvas.
3. Selecciona **Restore interaction data** para restaurar los datos de esas campañas o Canvas.

Después de otros tres meses de inactividad, estas campañas o Canvas expiran de nuevo.

#### Reorientación por etiqueta {#retargeting-by-tag}

Las campañas que utilizan filtros de reorientación que reorientan por etiqueta no están exentas de la expiración. Los filtros de reorientación que reorientan por etiqueta incluyen:

- Received Message from Campaign or Canvas with Tag
- Clicked/Opened Campaign or Canvas With Tag
- Last Received Message from Campaign or Canvas With Tag

### ¿Cuándo estuvieron disponibles los datos de interacción de mensajería en el pasado? {#when-was-messaging-interaction-data-available-in-the-past}

Anteriormente, los datos de interacción de mensajería se eliminaban cuando una campaña o un Canvas:

- No había enviado mensajes en 25 meses calendario, Y
- No se utilizaba para reorientación en ninguna campaña, Canvas o Content Cards activos.

Las campañas y Canvas con datos de interacción de mensajería previamente eliminados no pueden utilizarse en filtros de reorientación para campañas, Canvas y segmentos.