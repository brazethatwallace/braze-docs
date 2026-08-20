---
nav_title: Filtrado de bots para correos electrónicos
article_title: Filtrado de bots para correos electrónicos
page_type: reference
page_order: 1
toc_headers: h2
alias: "/bot_filtering/"
description: "Este artículo ofrece un resumen del filtrado de bots para el correo electrónico."
---

# Filtrado de bots para correos electrónicos {#bot-filtering-for-emails}

> Configura el filtrado de bots en tus [Preferencias de correo electrónico]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) para excluir todos los clics sospechosos de máquina o bot. Un "clic de bot" en correo electrónico se refiere a un clic en hipervínculos dentro de un correo electrónico generado por un programa automatizado. Al filtrar estos clics de bot, puedes desencadenar y entregar mensajes intencionadamente a destinatarios que estén interactuando.

{% alert important %}
A partir del 9 de julio de 2025, todos los espacios de trabajo nuevos que se creen tendrán activada la configuración de filtrado de bots para obtener informes de clics más precisos en Braze.
{% endalert %}

## Acerca de los clics de bots {#about-bot-clicks}

Braze cuenta con un sistema de detección que emplea múltiples entradas para identificar clics sospechosos de bots, también conocidos como interacciones no humanas (NHI). Los clics de bots pueden distorsionar tus métricas de participación de correo electrónico al inflar artificialmente las tasas de clics. Este enfoque nos permite diferenciar entre interacciones humanas genuinas y actividad sospechosa de bots para mantener la integridad de las métricas e información de participación de clics.

## Métricas afectadas por clics de bots {#metrics-affected-by-bot-clicks}

{% alert note %}
El filtrado de bots bloquea activamente los clics automatizados sospechosos para mejorar la precisión de tus métricas de participación. Sin embargo, los escáneres y bots evolucionan continuamente con el tiempo, por lo que Braze no puede garantizar la eliminación de todas las interacciones no humanas.
{% endalert %}

Las siguientes métricas de Braze pueden verse afectadas por clics de bots:

- Tasa de clics total
- Tasa de clics únicos
- Tasa de clics sobre aperturas
- Tasa de conversión (si se selecciona "Clics en Campaign" como evento de conversión)
- Mapa de calor
- Ciertos filtros de Segment

Cuando el filtrado de bots está activado, los clics sospechosos de bots se excluyen de los datos de clics. Las siguientes [características de Braze Intelligence]({{site.baseurl}}/user_guide/brazeai/intelligence_suite) pueden reflejar volúmenes más bajos relacionados con clics como resultado:

- Selección inteligente
- Canal inteligente
- Sincronización inteligente
- Paso de experimento
    - Ruta ganadora
    - Ruta personalizada
- Campaign
    - Variante ganadora
    - Variante personalizada
- Tasa de apertura real estimada

Las cancelaciones de suscripción derivadas de clics sospechosos de bots no se verán afectadas. Braze seguirá procesando todas las solicitudes de cancelación de suscripción de la forma habitual. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="blocking unsubscribes from suspected bot clicks" %}

## Filtros de segmentación afectados por el filtrado de bots {#segmentation-filters-affected-by-bot-filtering}

Los siguientes [filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) pueden verse afectados por el filtrado de bots en los mensajes de correo electrónico:

- [Hizo clic/abrió Campaign o Canvas con etiqueta]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-campaign-or-canvas-with-tag)
- [Hizo clic/abrió paso]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-step)
- [Hizo clic en alias en Campaign]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-campaign)
- [Hizo clic en alias en paso en Canvas]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-canvas-step)
- [Hizo clic en alias en cualquier Campaign o paso en Canvas]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-any-campaign-or-canvas-step)
- [Última interacción con mensaje]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#last-engaged-with-message)
- [Canal inteligente]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#intelligent-channel)

## Activar el filtrado de bots {#turning-on-bot-filtering}

Ve a **Configuración** > **Preferencias de correo electrónico**. Luego, selecciona **Eliminar clics de bots**. Esta configuración se aplica a nivel del espacio de trabajo.

Los clics sospechosos de bots solo se eliminarán después de activar la configuración, y no se aplica de forma retroactiva a las métricas de tu espacio de trabajo.

![Configuración de filtrado de bots activada en Preferencias de correo electrónico.]({% image_buster /assets/img/bot_tracking_email.png %})

{% alert important %}
Si activas esta configuración y luego la desactivas, Braze no podrá restaurar ninguna actividad de bots previamente eliminada en tus análisis.
{% endalert %}

## Campos en los eventos de clic de correo electrónico para Currents y Snowflake {#fields-in-email-click-events-for-currents-and-snowflake}

Braze enviará los campos `is_suspected_bot_click` y `suspected_bot_click_reason` en Currents y Snowflake para un evento de clic de correo electrónico.

| Campo | Tipo de datos | Descripción |
| `is_suspected_bot_click` | Boolean | Indica que se trata de un clic sospechoso de bot. Se enviará como valores nulos hasta que actives la configuración del espacio de trabajo **Eliminar clics de bots**. Este enfoque te permite comprender de forma programática cuándo ha comenzado el filtrado de clics sospechosos de bots en tu espacio de trabajo, para que puedas compararlo con precisión con los datos en Currents y Snowflake. |
| `suspected_bot_click_reason` | Array | Indica el motivo por el que se trata de un clic sospechoso de bot. Se completará con valores, como `user_agent` e `ip_address`, incluso si la configuración del espacio de trabajo de filtrado de bots está desactivada. Este campo puede proporcionar información sobre el impacto potencial de activar esta configuración, comparando el número de clics provenientes de clics sospechosos de bots con las interacciones humanas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos en los eventos de clic de correo electrónico para Currents y Snowflake" }

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cómo afectará el filtrado de bots al rendimiento de mi Campaign? {#how-will-bot-filtering-impact-my-campaigns-performance}

Esto no afectará a las métricas de ninguna Campaign anterior ya enviada. Cuando el filtrado de bots está activado en tu espacio de trabajo, Braze comenzará a filtrar los clics sospechosos de bots de todos los clics. Es posible que notes una caída en las tasas de clics, pero la tasa de clics será una representación más precisa de la participación de tus usuarios con sus mensajes de correo electrónico.

### ¿El filtrado de bots evitará que los bots que hacen clic en el enlace de cancelar suscripción de Braze cancelen la suscripción? {#will-bot-filtering-prevent-bots-clicking-on-the-braze-unsubscribe-link-from-unsubscribing}

No. Todas las solicitudes de cancelación de suscripción seguirán siendo procesadas.

### ¿Se consideran las aperturas de máquina en el filtrado de clics de bots? {#are-machine-opens-considered-in-the-bot-click-filtering}

No.