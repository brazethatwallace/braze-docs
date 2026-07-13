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

## Sobre los clics de los bots {#about-bot-clicks}

Braze tiene un sistema de detección que emplea múltiples entradas para identificar presuntos clics de bots, también denominados interacciones no humanas (NHI). Los clics de los bots pueden distorsionar tus métricas de interacción por correo electrónico inflando artificialmente las tasas de clics. Este enfoque nos permite diferenciar entre las interacciones humanas auténticas y la actividad sospechosa de los bots, para mantener la integridad de las métricas y la información sobre la interacción de los clics.

## Métricas afectadas por los clics de los bots {#metrics-affected-by-bot-clicks}

{% alert note %}
El filtrado de bots bloquea activamente los clics automatizados sospechosos para mejorar la precisión de tus métricas de interacción. Sin embargo, los escáneres y bots evolucionan continuamente con el tiempo, por lo que Braze no puede garantizar la eliminación de todas las interacciones no humanas.
{% endalert %}

Las siguientes métricas de Braze pueden verse afectadas por los clics de los bots:

- Tasa de clics total
- Tasa de clics únicos
- Tasa de clics sobre aperturas
- Tasa de conversión (si se selecciona "Clics en Campaign" como evento de conversión)
- Mapa de calor
- Ciertos filtros de segmentación

Las [características de Braze Intelligence]({{site.baseurl}}/user_guide/brazeai/intelligence_suite) que aprovechan los datos de clics sobre nuestros sistemas de detección pueden verse afectadas. Activar la configuración tiene el potencial de interrumpir temporalmente nuestros sistemas de detección, lo que puede resultar en una disminución de la métrica o entrada debido a esta exclusión de clics sospechosos de bots:

- Selección inteligente
- Canal inteligente
- Sincronización inteligente
- Paso de experimento
    - Winning Path
    - Personalized Path
- Campaign
    - Variante ganadora
    - Variante personalizada
- Tasa estimada de aperturas reales

Las cancelaciones de suscripción derivadas de clics sospechosos de bots no se verán afectadas. Braze seguirá procesando todas las solicitudes de cancelación de suscripción con normalidad. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="blocking unsubscribes from suspected bot clicks" %}

## Filtros de segmentación afectados por el filtrado de bots {#segmentation-filters-affected-by-bot-filtering}

Los siguientes [filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) pueden verse afectados por el filtrado de bots para mensajes de correo electrónico:

- [Hizo clic/abrió Campaign o Canvas con etiqueta]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-campaign-or-canvas-with-tag)
- [Hizo clic/abrió paso]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-step)
- [Hizo clic en alias en Campaign]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-campaign)
- [Hizo clic en alias en paso en Canvas]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-canvas-step)
- [Hizo clic en alias en cualquier Campaign o paso en Canvas]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-any-campaign-or-canvas-step)
- [Última interacción con mensaje]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#last-engaged-with-message)
- [Canal inteligente]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#intelligent-channel)

## Activar el filtrado de bots {#turning-on-bot-filtering}

Ve a **Configuración** > **Preferencias de correo electrónico**. Luego, selecciona **Remove bot clicks**. Esta configuración se aplica a nivel del espacio de trabajo.

Los clics sospechosos de bots solo se eliminarán después de activar la configuración, y no se aplica de forma retroactiva a las métricas de tu espacio de trabajo.

![Configuración de filtrado de bots para correo electrónico activada en Preferencias de correo electrónico.]({% image_buster /assets/img/bot_tracking_email.png %})

{% alert important %}
Si activas esta configuración y luego la desactivas, Braze no podrá restaurar ninguna actividad de bots previamente eliminada en tus análisis.
{% endalert %}

## Campos en eventos de clic de correo electrónico para Currents y Snowflake {#fields-in-email-click-events-for-currents-and-snowflake}

Braze enviará los campos `is_suspected_bot_click` y `suspected_bot_click_reason` en Currents y Snowflake para un evento de clic de correo electrónico.

| Campo | Tipo de datos | Descripción |
| `is_suspected_bot_click` | Booleano | Indica que se trata de un clic sospechoso de bot. Se enviará como valores nulos hasta que actives la configuración del espacio de trabajo **Remove bots clicks**. Este enfoque te permite comprender de forma programática cuándo ha comenzado el filtrado de clics sospechosos de bots en tu espacio de trabajo para que puedas compararlo con precisión con los datos en Currents y Snowflake. |
| `suspected_bot_click_reason` | Array | Indica el motivo por el que se considera un clic sospechoso de bot. Se completará con valores, como `user_agent` e `ip_address`, incluso si la configuración del espacio de trabajo de filtrado de bots está desactivada. Este campo puede proporcionar información sobre el impacto potencial de activar esta configuración al comparar la cantidad de clics derivados de clics sospechosos de bots con las interacciones humanas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos en eventos de clic de correo electrónico para Currents y Snowflake" }

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cómo afectará el filtrado de bots al rendimiento de mi campaña? {#how-will-bot-filtering-impact-my-campaigns-performance}

Esto no afectará las métricas de ninguna campaña anterior ya enviada. Cuando el filtrado de bots esté activado en tu espacio de trabajo, Braze comenzará a filtrar los clics sospechosos de bots de todos los clics. Es posible que notes una disminución en las tasas de clics, pero la tasa de clics será una representación más precisa de la interacción de tus usuarios con sus mensajes de correo electrónico.

### ¿El filtrado de bots evitará que los bots que hacen clic en el enlace de cancelación de suscripción de Braze cancelen la suscripción? {#will-bot-filtering-prevent-bots-clicking-on-the-braze-unsubscribe-link-from-unsubscribing}

No. Todas las solicitudes de cancelación de suscripción seguirán procesándose.

### ¿Se consideran las aperturas de máquina en el filtrado de clics de bots? {#are-machine-opens-considered-in-the-bot-click-filtering}

No.