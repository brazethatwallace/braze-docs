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

Braze cuenta con un sistema de detección propietario que utiliza múltiples entradas para identificar clics sospechosos de bots, también conocidos como interacciones no humanas (NHI). Los clics de bots pueden inflar las tasas de clics, distorsionando las métricas de interacción. Al filtrarlos, Braze facilita la captura de datos fiables para la toma de decisiones.

Nuestro sistema analiza los agentes de usuario asociados con rastreadores web, vistas previas de enlaces de Android e iOS, o software de seguridad CPaaS. Algunos ejemplos de agentes de usuario filtrados incluyen `GoogleBot`, `GoogleMessages/20`, `python-requests/2.32.3` y `Barracuda Sentinel (EE)`.

## Métricas y flujos de trabajo afectados {#affected-metrics-and-workflows}

Las siguientes métricas y flujos de trabajo de Braze se ven afectados por los clics de bots:

- **_Clics totales_:** Los análisis de Campaigns y los análisis de Canvas excluirán los clics de bots, reflejando solo las interacciones humanas.
- **Filtros de segmentación:** Los filtros de Segment que hacen referencia a interacciones de enlaces SMS excluirán los clics de bots para una reorientación más precisa en Campaigns y Canvas.
- **Orquestación:** Los clics de bots se filtran de los desencadenadores basados en acciones y las rutas de acción de Canvas que hacen referencia a interacciones de enlaces SMS, lo que permite que los desencadenadores reflejen el comportamiento humano.
- **Braze Intelligence:**
    - **Intelligent Selection:** Excluye los clics de bots al optimizar la selección de variantes.
    - **Canal inteligente:** Excluye los clics de bots cuando se selecciona SMS o RCS para una selección de canal precisa.
    - **Pasos de experimento:** Excluye los clics de bots para obtener resultados de experimentos fiables.
    - **Exportaciones de datos de Currents:** Incluye los campos `is_suspected_bot_click` y `suspected_bot_click_reason` para ayudar a analizar los clics humanos frente a los de bots. Estos campos están disponibles en [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) y [Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder).

Las cancelaciones de suscripción derivadas de clics sospechosos de bots no se ven afectadas. Braze procesa todas las solicitudes de cancelación de suscripción de la forma habitual. Para bloquear estas cancelaciones de suscripción, [envía comentarios sobre el producto]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Campos de Currents en eventos de clics de SMS {#currents-fields-in-sms-click-events}

Braze incluye los siguientes campos de Currents para eventos de clics de SMS:

| Campo | Tipo de datos | Descripción |
| --- | --- | --- |
| `is_suspected_bot_click` | Booleano | Indica si el clic es un clic sospechoso de bot. Devuelve `null` para todos los usuarios hasta que se habilite el filtrado de clics de bots para tu empresa. Cuando se habilite, se rellenará con `true` o `false` para todos los nuevos clics en adelante. |
| `suspected_bot_click_reason` | Cadena, Array | Indica el motivo de un clic sospechoso de bot (como `user_agent`). Se rellena incluso si el filtrado está deshabilitado, proporcionando información sobre la actividad potencial de bots. Este campo está disponible globalmente y se rellena con un motivo para todos los usuarios, incluso si el filtrado de clics de bots aún no está habilitado. Esto proporciona información sobre la actividad potencial de bots antes de que habilites el filtrado de clics de bots. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos de Currents en eventos de clics de SMS" }

## Plantilla del Generador de consultas {#query-builder-template}

Para ayudarte a analizar tus datos, puedes usar la plantilla móvil preconstruida **SMS click events by bots** en el [Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cómo afecta el filtrado de clics de bots al rendimiento de las Campaigns? {#how-does-bot-click-filtering-impact-campaign-performance}

El filtrado no afecta a las Campaigns enviadas anteriormente. Cuando se habilita, reduce las tasas de clics a partir de ese momento al excluir los clics de bots.

### ¿El filtrado de clics de bots evita que los bots hagan clic en los enlaces de cancelación de suscripción? {#does-bot-click-filtering-prevent-bots-from-clicking-unsubscribe-links}

No. Todas las solicitudes de cancelación de suscripción se procesan de la forma habitual.

### ¿Las vistas previas de enlaces se incluyen en el filtrado de clics de bots? {#are-link-previews-included-in-bot-click-filtering}

Sí. Las vistas previas de enlaces (como las vistas previas de enlaces de Android e iOS) se marcan como clics de bots y se filtran.

### ¿Cómo habilito el filtrado de clics de bots? {#how-do-i-enable-bot-click-filtering}

Debes ponerte en contacto con tu equipo de cuenta de Braze para habilitar el filtrado de clics de bots durante el acceso anticipado. Cuando el filtrado de clics de bots tenga disponibilidad general, la característica estará habilitada de forma predeterminada para todos los usuarios de SMS y RCS.

Asegúrate también de haber habilitado el seguimiento avanzado de clics para el [acortamiento de enlaces]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening). Esto te permite recibir los análisis de clics de bots, ya que rastreamos estos datos a nivel de usuario individual.

{% alert note %}
Para obtener más ayuda, [ponte en contacto con Soporte]({{site.baseurl}}/braze_support).
{% endalert %}