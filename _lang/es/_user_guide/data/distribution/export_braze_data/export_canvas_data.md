---
nav_title: Datos de Canvas
article_title: Exportar datos de Canvas
page_order: 3
page_type: reference
description: "Este artículo de referencia explica cómo exportar los análisis de Canvas."
tool:
  - Canvas
  - Reports

---

# Exportar datos de Canvas {#export-canvas-data}

> Los datos de usuario pueden exportarse a un CSV. En esta página se explica cómo exportar datos de todo el Canvas o de un componente específico de Canvas.

## Exportar datos de un Canvas {#exporting-data-for-a-canvas}

Para exportar los datos de un Canvas, haz lo siguiente:

1. Ve a **Mensajería** > **Canvas** y selecciona tu Canvas.
2. Selecciona el menú desplegable **Datos de usuario** en la sección **Detalles de Canvas**.
3. Selecciona una de las siguientes opciones de exportación:
  - **Exportación de datos de usuario a CSV** o
  - **Exportar dirección de correo electrónico a CSV**.

También puedes exportar los datos de usuario de todos los participantes de un Canvas como archivo CSV.

## Exportar usuarios que entraron o volvieron a entrar en un Canvas {#export-users-who-entered-or-re-entered-a-canvas}

Cuando la [reelegibilidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) está habilitada, los usuarios pueden entrar en el mismo Canvas más de una vez. La opción **Exportación de datos de usuario a CSV** en la página de detalles de Canvas exporta los usuarios que entraron en el Canvas, pero no incluye cuántas veces entró cada usuario ni la marca de tiempo de cada entrada.

Para analizar cuándo los usuarios entraron o volvieron a entrar en un Canvas, utiliza una de las siguientes opciones:

- **Entrada más reciente por usuario:** Exporta un segmento con el campo [`canvases_received`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) usando el endpoint [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment). Para cada Canvas, la exportación incluye las marcas de tiempo `last_entered` y `last_exited` de ese usuario. El campo `canvases_received` contiene datos de los últimos 90 días.
- **Cada entrada, incluidas las reentradas:** Usa los [eventos de entrada en Canvas]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#canvas-entry-events) en Braze Currents o Snowflake Data Sharing. Cada evento `users.canvas.Entry` representa una entrada en Canvas e incluye una marca de tiempo `time`. Cuenta los eventos por usuario para determinar cuántas veces entraron.
- **Crear una lista de usuarios en el panel:** Crea un segmento con un filtro **Entered Canvas Variation** y luego exporta el segmento a CSV. Consulta [Solución de problemas de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/troubleshooting#user-didnt-enter-the-canvas).

{% alert note %}
Si no tienes Currents integrado y necesitas cada marca de tiempo de entrada histórica, contacta con tu administrador de éxito de cliente de Braze.
{% endalert %}

Para un paso en Canvas específico en el flujo de trabajo original, usa **Exportación de datos de usuario a CSV** en la página de detalles del paso.

## Exportar datos de un componente (solo flujo de trabajo original) {#exporting-data-for-a-component-original-workflow-only}

Los resultados de Canvas se pueden exportar por componentes individuales para el flujo de trabajo original de Canvas. Para ello, selecciona el componente específico y, a continuación, selecciona el desplegable **Datos de usuario** en la página **Detalles del paso en Canvas**.

![Menú desplegable de datos de usuario en la página de detalles de Canvas.]({% image_buster /assets/img/canvas_csv_export.png %})

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita nuestro artículo de [solución de problemas de exportación]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}