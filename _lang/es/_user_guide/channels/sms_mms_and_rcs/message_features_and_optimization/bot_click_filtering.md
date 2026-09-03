---
nav_title: "Filtrado de clics de bots"
article_title: "Filtrado de clics de bots en SMS y RCS"
description: "Este artículo de referencia cubre el filtrado de clics de bots en SMS y RCS."
alias: /sms_rcs_bot_click_filtering/
page_type: reference
page_order: 5
channel:
  - SMS
  - RCS
---

# Filtrado de clics de bots en SMS y RCS {#sms-and-rcs-bot-click-filtering}

> El filtrado de clics de bots en SMS y RCS mejora los análisis de Campaigns y los flujos de trabajo al excluir los clics sospechosos de bots. Un "clic de bot" se refiere a clics automatizados en enlaces acortados en mensajes SMS y RCS, como los de rastreadores web, vistas previas de enlaces de Android e iOS, o software de seguridad CPaaS. Esta característica facilita la elaboración de informes precisos, la segmentación y la orquestación para interactuar con usuarios reales. <br><br> Para el filtrado de clics de bots en Campaigns de correo electrónico, consulta [Filtrado de bots para correos electrónicos]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/bot_filtering).

## Cómo funciona {#how-it-works}

Braze cuenta con un sistema de detección propietario que utiliza múltiples entradas para identificar clics sospechosos de bots, también conocidos como interacciones no humanas (NHI). Los clics de bots pueden inflar las tasas de clics, distorsionando las métricas de participación. Al filtrarlos, Braze facilita la captura de datos fiables para la toma de decisiones.

Nuestro sistema analiza los agentes de usuario asociados con rastreadores web, vistas previas de enlaces de Android e iOS, o software de seguridad CPaaS. Algunos ejemplos de agentes de usuario filtrados incluyen `GoogleBot`, `GoogleMessages/20`, `python-requests/2.32.3` y `Barracuda Sentinel (EE)`.

## Métricas y flujos de trabajo afectados {#affected-metrics-and-workflows}

Las siguientes métricas y flujos de trabajo de Braze se ven afectados por los clics de bots:

- **_Clics totales_:** Los análisis de Campaign y los análisis de Canvas excluyen los clics de bots, reflejando solo las interacciones humanas.
- **Filtros de segmentación:** Los filtros de Segment que hacen referencia a interacciones con enlaces SMS excluyen los clics de bots para una reorientación más precisa en Campaigns y Canvas.
- **Orquestación:** Los clics de bots se filtran de los desencadenadores basados en acciones y de las Rutas de Acción de Canvas que hacen referencia a interacciones con enlaces SMS, lo que permite que los desencadenadores reflejen el comportamiento humano.
- **Braze Intelligence:**
    - **Optimizar con BrazeAI<sup>TM</sup>:** Excluye los clics de bots al optimizar la selección de variantes.
    - **Canal inteligente:** Excluye los clics de bots cuando se selecciona SMS o RCS para una selección de canal precisa.
    - **Pasos de experimento:** Excluye los clics de bots para obtener resultados de experimentos fiables.
    - **Exportaciones de datos de Currents:** Incluye los campos `is_suspected_bot_click` y `suspected_bot_click_reason` para ayudar a analizar los clics humanos frente a los de bots. Estos campos están disponibles en [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) y [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder).

Las cancelaciones de suscripción por clics sospechosos de bots no se ven afectadas. Braze procesa todas las solicitudes de cancelación de suscripción con normalidad. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="blocking unsubscribes from suspected bot clicks" %}

## Campos de Currents en eventos de clic de SMS {#currents-fields-in-sms-click-events}

Braze incluye los siguientes campos de Currents para eventos de clic de SMS:

| Campo | Tipo de datos | Descripción |
| --- | --- | --- |
| `is_suspected_bot_click` | Booleano | Indica si el clic es un clic sospechoso de bot. Para clics en enlaces cortos de SMS y RCS, Braze evalúa la detección de bots en cada clic y completa este campo con `true` o `false`. |
| `suspected_bot_click_reason` | Cadena, Array | Indica el motivo de un clic sospechoso de bot (como `user_agent`). Se completa cuando la detección de bots se ejecuta para clics en enlaces cortos de SMS y RCS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos de Currents en eventos de clic de SMS" }

## Plantilla del Query Builder {#query-builder-template}

Para obtener ayuda con el análisis de tus datos, puedes usar la plantilla prediseñada para móvil **Eventos de clics de SMS por bots** en el [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cómo afecta el filtrado de clics de bots al rendimiento de una Campaign? {#how-does-bot-click-filtering-impact-campaign-performance}

El filtrado de clics de bots se ejecuta automáticamente para los clics en enlaces acortados de SMS y RCS. Las tasas de clics del panel excluyen los clics sospechosos de bots, de modo que las tasas reportadas reflejan interacciones humanas en lugar de vistas previas automatizadas de enlaces o tráfico de rastreadores.

### ¿El filtrado de clics de bots evita que los bots hagan clic en los enlaces de cancelar suscripción? {#does-bot-click-filtering-prevent-bots-from-clicking-unsubscribe-links}

No. Todas las solicitudes de cancelación de suscripción se procesan con normalidad.

### ¿Las vistas previas de enlaces se incluyen en el filtrado de clics de bots? {#are-link-previews-included-in-bot-click-filtering}

Sí. Las vistas previas de enlaces (como las vistas previas de enlaces de Android e iOS) se marcan como clics de bots y se filtran.