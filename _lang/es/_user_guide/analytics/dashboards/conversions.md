---
nav_title: Conversiones
article_title: Dashboard de conversiones
alias: "/conversions_dashboard_v2/"
description: "El dashboard de conversiones te permite analizar conversiones en campañas, Canvas y canales, utilizando diferentes métodos de atribución."
page_order: 3
page_type: reference
tool:
  - Reports
---

# Dashboard de conversiones {#conversions-dashboard}

> El dashboard de conversiones analiza conversiones en campañas, Canvas y canales, utilizando varios [métodos de atribución](#attribution-methods). Al medir tus conversiones, puedes especificar el periodo de tiempo, el evento de conversión y la ventana de conversión.

## Configurar tu informe {#setting-up-your-report}

Para configurar tu informe del dashboard de conversiones:

1. Ve a **Analytics** > **Conversions**.
2. Selecciona un **Date Range** para tu informe, con una ventana de hasta 90 días.
3. Selecciona las campañas o Canvas (o ambos) a analizar.
   - (opcional) Filtra campañas y Canvas seleccionando una etiqueta.
4. Selecciona los **Channel(s)** a analizar para tus mensajes.
5. Selecciona una capa de **Breakdown by** para ver diferentes dimensiones de datos, como por variante, paso en Canvas, país o idioma.
6. (Opcional) Si quieres calcular conversiones de un evento que no se configuró como evento de conversión en la campaña o Canvas, activa [Usar eventos personalizados](#using-custom-events).
7. Selecciona un [método de atribución](#attribution-methods) con el cual analizar los mensajes seleccionados.

{% alert note %}
Si estás analizando conversiones para múltiples canales, tu **Attribution Method** se establecerá de forma predeterminada en **Last-Touch Attribution**.
{% endalert %}

{:start="8"}
8. Selecciona **Create** para ejecutar el informe.

Después de que se cargue la página, selecciona un **Conversion Event** para filtrar el informe por datos de conversión. Las selecciones disponibles incluirán los eventos que fueron preconfigurados en los Canvas y campañas. Si seleccionaste un evento personalizado al configurar tu informe (paso 6), esta opción no estará disponible.

### Usar eventos personalizados {#using-custom-events}

Para que las métricas de eventos personalizados aparezcan en el dashboard de conversiones, debes tener un evento de conversión y un evento de entrada de Canvas en el rango de fechas especificado en la página.

Para calcular conversiones de un evento que no se configuró como evento de conversión en la campaña o Canvas, selecciona un evento personalizado específico para usarlo como evento de conversión.

1. Al configurar tu informe, activa **Use custom events**.
2. Selecciona un evento personalizado para usarlo como evento de conversión.
3. Selecciona la ventana de conversión dentro de la cual ese evento debería haber ocurrido para ser contado como una conversión.

{% alert note %}
Si seleccionas un evento personalizado, no verás el desplegable **Conversion Event** en la página y tendrás que volver a ejecutar el informe para ver conversiones de diferentes eventos personalizados.
{% endalert %}

### Consideraciones {#considerations}

Para que un usuario sea contado en el informe, debe cumplir los siguientes criterios dentro del rango de fechas seleccionado:
1. Entrar en el Canvas o la campaña.
2. Registrar un [método de atribución]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#attribution-methods).
3. Realizar el evento de conversión.

Por ejemplo, supongamos que un usuario hace lo siguiente:
1. Entra en el Canvas el 30 de septiembre.
2. Registra un método de atribución el 1 de octubre.
3. Realiza el evento de conversión el 2 de octubre.

Este usuario **no aparecerá** en un informe con un rango de fechas del 1 al 7 de octubre. Esto se debe a que el usuario entró en el Canvas antes del periodo del informe, aunque el evento de conversión ocurrió dentro del rango de fechas definido. Para que el usuario aparezca en un informe, el rango de fechas debe incluir el 30 de septiembre.

## Comprender tu informe {#understanding-your-report}

Tu informe se divide en tres secciones:

- [Detalles de conversión](#conversion-details)
- [Embudo de conversión](#conversion-funnel)
- [Conversiones a lo largo del tiempo](#conversions-over-time)

### Detalles de conversión {#conversion-details}

La tabla de detalles de conversión siempre muestra una columna para *Destinatarios* y otra para *Conversiones* (tasa y total). Las dos columnas restantes de la tabla que aparecen dependen de las opciones que seleccionaste al configurar tu informe.

![Tabla de detalles de conversión que muestra puntos de intervención como método de atribución para las columnas tres y cuatro.]({% image_buster /assets/img_archive/conversions2_details.png %}){: style="border:none"}

La siguiente tabla describe las posibles métricas.

| Métrica mostrada | Descripción |
| --- | --- |
| Destinatarios | El número de usuarios que recibieron un mensaje a través del canal seleccionado dentro del rango de fechas del informe |
| Tasa de conversión (Destinatarios) | Se calcula como: (Número de conversiones) / (Número de destinatarios) |
| Método de atribución | Definido por el [método de atribución](#attribution-methods) que seleccionaste al configurar el informe. Para la atribución de último punto de intervención o si se seleccionan múltiples canales, esto aparece como [Puntos de intervención](#terms-to-know). |
| Tasa de conversión (Método de atribución) | Definido por el [método de atribución](#attribution-methods) que seleccionaste al configurar el informe. Si se seleccionan múltiples canales, se establece de forma predeterminada la atribución de último punto de intervención. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Detalles de conversión" }

Si seleccionaste detalles a nivel de desglose para campañas o Canvas al [configurar tu informe](#setting-up-your-report) (paso 5), puedes seleccionar <i class="fas fa-angle-down"></i> **Expandir** para expandir la tabla.

### Embudo de conversión {#conversion-funnel}

Este gráfico de barras muestra los conteos absolutos para cada [evento de interacción]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) basado en el canal seleccionado. El conteo de conversiones se definirá según el método de atribución seleccionado.

De forma predeterminada, se muestran todas las campañas y Canvas seleccionados. Para deseleccionar una campaña o Canvas, selecciona el nombre de la campaña o Canvas que deseas excluir. Para obtener detalles adicionales sobre el evento de interacción, puedes pasar el cursor sobre cada barra.

Para descargar los datos de la serie temporal, selecciona una opción de descarga: PNG, JPEG, PDF, SVG o CSV.

{% alert note %}
Este gráfico solo muestra datos para un canal a la vez. Usa el desplegable **Channel** en el gráfico para seleccionar un solo canal.
{% endalert %}

![Gráfico de barras del embudo de conversión para dos campañas de correo electrónico que muestran resultados similares para correo electrónico entregado, correo electrónico abierto, clic en correo electrónico y conversiones.]({% image_buster /assets/img_archive/conversions2_funnel.png %})

### Conversiones a lo largo del tiempo {#conversions-over-time}

Este gráfico de serie temporal incluye una representación de las conversiones por campaña o Canvas a lo largo del tiempo. De forma predeterminada, se muestran todas las campañas y Canvas seleccionados. Para deseleccionar una campaña o Canvas, haz clic en el nombre de la campaña o Canvas que deseas excluir.

Para descargar los datos de la serie temporal, selecciona <i class="fas fa-bars" title="Menú contextual del gráfico"></i> **Menú contextual del gráfico** y luego selecciona tu opción de descarga. Las opciones disponibles son PNG, JPEG, PDF, SVG o CSV.

![Gráfico de serie temporal de conversiones a lo largo del tiempo para dos campañas de correo electrónico, mostrando conversiones por día.]({% image_buster /assets/img_archive/conversions2_over_time.png %})

### Métodos de atribución {#attribution-methods}

| Método de atribución | Definición | Cálculo de la tasa | Opciones específicas del canal |
| --- | --- | --- | --- |
| Al recibir | Número total de conversiones que ocurrieron después de recibir el mensaje | Se calcula como (Conversiones únicas al recibir) / (Destinatarios únicos) | {::nomarkdown}<ul><li>Al entregar correo electrónico</li><li>Al entregar SMS</li></ul>{:/} |
| Al enviar | Número total de conversiones que ocurrieron después del envío del mensaje | Se calcula como (Conversiones únicas al enviar) / (Destinatarios únicos) | {::nomarkdown}<ul><li>Al enviar push</li><li>Al enviar tarjeta de contenido</li><li>Al enviar SMS</li></ul>{:/} |
| Al abrir | Número total de conversiones que ocurrieron después de abrir el mensaje | Se calcula como (Conversiones únicas al abrir) / (Destinatarios únicos) | {::nomarkdown}<ul><li>Al abrir correo electrónico</li><li>Al abrir push</li></ul>{:/} |
| Al hacer clic | Número total de conversiones que ocurrieron después de hacer clic en el mensaje | Se calcula como (Conversiones únicas al hacer clic) / (Destinatarios únicos) | {::nomarkdown}<ul><li>Al hacer clic en correo electrónico</li><li>Al hacer clic en tarjeta de contenido</li><li>Al hacer clic en IAM</li></ul>{:/} |
| Al generar impresión | Número total de conversiones que ocurrieron después de una impresión | Se calcula como (Conversiones únicas por impresión) / (Destinatarios únicos) | {::nomarkdown}<ul><li>Al generar impresión de IAM</li><li>Al generar impresión de tarjeta de contenido</li></ul>{:/} |
| Al último punto de intervención | Conversiones que otorgan todo el crédito al último mensaje tocado o en el que se hizo clic durante la ventana de conversión. | Se calcula como (Número de puntos de intervención) / (Destinatarios únicos) | La atribución de último punto de intervención se selecciona automáticamente si se agregan múltiples canales al informe.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Métodos de atribución" }

## Términos que debes conocer {#terms-to-know}

| Término | Definición |
| --- | --- |
| Punto de intervención | Una interacción física o punto de intervención con un mensaje.<br><br>Los puntos de intervención pueden incluir:<br>{::nomarkdown}<ul><li>Clic en correo electrónico</li><li>Apertura de push</li><li>Clic en tarjeta de contenido</li><li>Clic en mensaje dentro de la aplicación</li><li>Clic en SMS</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Términos que debes conocer" }

## Solución de problemas {#troubleshooting}

### ¿Por qué tengo pocas conversiones en mi campaña o Canvas? {#why-do-i-have-low-campaign-or-canvas-conversions}

Tus conversiones podrían no ser tan altas como esperas en comparación con campañas anteriores o tus expectativas. Las conversiones dependen de dos funciones clave: el seguimiento de eventos y los plazos de conversión.

Para solucionar problemas, verifica tu seguimiento de eventos y los plazos de conversión.

#### Seguimiento de eventos {#event-tracking}

Cuando una campaña desencadena un inicio de sesión o un evento personalizado, debes asegurarte de que este evento, o sesión, ocurra con la frecuencia suficiente para desencadenar el mensaje. Consulta el [dashboard de inicio]({{site.baseurl}}/user_guide/analytics/dashboards/home) para datos de sesión, o tu informe de [eventos personalizados]({{site.baseurl}}/user_guide/analytics/reports/configure_reporting).

#### Plazos de conversión {#conversion-deadlines}

Para cada evento de conversión que selecciones por campaña, estableces el [plazo]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#creating-a-campaign-with-conversion-tracking). Esto significa que estás estableciendo un límite de tiempo dentro del cual debe ocurrir una conversión para que cuente para cada campaña respectiva.

Verifica que hayas revisado la información sobre las [reglas de seguimiento de conversiones]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules) para comprender las métricas de tu campaña. Para conversiones de usuarios en Canvas, consulta las [preguntas frecuentes de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/faqs#how-are-user-conversions-tracked-in-a-canvas).