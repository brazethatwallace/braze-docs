---
nav_title: Informes de embudo
article_title: Informes de embudo para Campaigns y Canvas
page_order: 8
page_type: reference
description: "Esta página cubre los beneficios de los informes de embudo, cómo configurarlos y cómo interpretar tu informe."
tool: Reports
---

# Informes de embudo {#funnel-reports}

> La página **Informe de embudo** ofrece un informe visual que te permite analizar los recorridos que siguen tus clientes después de recibir una Campaign o Canvas, incluyendo las diferentes acciones que los clientes realizan en su camino hacia la conversión y dónde se producen los abandonos. ![Captura de pantalla de la página Informe de embudo mostrando un embudo de conversión para el rendimiento de una Campaign o Canvas]({% image_buster /assets/img/funnel_report/funnel_report2.png %}){: style="float:right;max-width:15%;margin-bottom:15px; border: 0"}

Si tu Campaign o Canvas utiliza un grupo de control o múltiples variantes, puedes comprender cómo las diferentes variantes han impactado el embudo de conversión a un nivel más granular y optimizar en función de estos datos.

![Informe de embudo 1]({% image_buster /assets/img/funnel_report/funnel_report1.jpg %}){: style="max-width:80%;"}

## Casos de uso {#use-cases}

Los informes de embudo pueden responder preguntas como:

- **Incorporación:** Después de enviar un Canvas "¡Bienvenido, recién llegado!", ¿cuántos usuarios completaron cada paso del recorrido de incorporación?
- **Finalización de compra:** ¿Dónde se produjeron los abandonos de compra en una promoción de temporada?
- **Conversiones personalizadas:** ¿Qué porcentaje de usuarios inició una sesión, escuchó una pista y creó una lista de reproducción después de un push de "Nuevo lanzamiento"?
- **Abandonos de upsell:** En un Canvas de upsell, ¿dónde abandonaron los usuarios antes de suscribirse?
- **Comportamientos post-interacción:** ¿Qué variante de correo electrónico generó más compras después de que los usuarios lo abrieron?
- **Frecuencia de conversión:** ¿Qué porcentaje de usuarios refirió a un amigo al menos tres veces después de recibir una Campaign?

## Configurar informes de embudo {#setting-up-funnel-reports}

![Informe de embudo 5]({% image_buster /assets/img/funnel_report/canvas_campaign.png %}){: style="float:right;max-width:40%;border:0;margin-left:15px;"}

Puedes ejecutar informes de embudo para Campaigns y Canvas activos existentes. Estos informes muestran una serie de eventos por los que progresa un destinatario de la campaña durante un período de 1 a 30 días desde la fecha en que ingresa al Canvas o la Campaign. Un usuario se considera convertido a través de un paso en el embudo si realiza el evento en el orden especificado.

Los informes de embudo están disponibles desde las siguientes ubicaciones en el dashboard:

- La página **Campaign Analytics** para una Campaign específica
- La página **Canvas Details** para un Canvas específico, seleccionando el botón **Analyze Variants**

{% alert important %}
Los informes de embudo no están disponibles para [Campaigns de API]({{site.baseurl}}/api/api_campaigns).
{% endalert %}

### Paso 1: Selecciona un rango de fechas {#step-1-select-a-date-range}

Puedes seleccionar un período de tiempo para tu informe (dentro de los últimos seis meses) y refinar los datos para ver usuarios que, al ingresar a la Campaign o Canvas, completaron los eventos del embudo dentro de una ventana establecida (máximo de 30 días). En el siguiente ejemplo, tu embudo buscaría usuarios que recibieron esta Campaign o Canvas en los últimos siete días y completaron el embudo dentro de tres días.

{% alert note %}
Si estableces la ventana para completar el embudo en un día, entonces el evento del embudo debe ocurrir dentro de las 24 horas posteriores a la recepción del mensaje. Sin embargo, si seleccionas varios días, la ventana de tiempo se cuenta como días calendario en la zona horaria de la empresa.
{% endalert %}

![Informe de embudo para un Canvas con "Últimos 7 días" seleccionado en el menú desplegable de período de tiempo.]({% image_buster /assets/img/funnel_report/funnel_report5.png %}){: style="max-width:90%;"}

### Paso 2: Selecciona eventos para los pasos del embudo {#step-2-select-events-for-funnel-steps}

Para cada informe de embudo, el primer evento es cuando el usuario recibe tu mensaje. A partir de ahí, los eventos subsiguientes que elijas filtran el número de usuarios que realizaron esos eventos, así como los eventos anteriores.

#### Eventos disponibles para informes de embudo {#available-funnel-report-events}

| Campaign | Inició sesión, Realizó compra, Realizó evento personalizado, Evento de interacción con mensaje |
| Canvas | Inició sesión, Realizó compra, Realizó evento personalizado, Recibió paso en Canvas, Interactuó con paso |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos disponibles para informes de embudo" }

{% alert note %}
El evento de informe **Interactuó con paso** solo se puede usar con pasos en Canvas que utilicen los canales de mensajería de correo electrónico o push.
{% endalert %}

![Informe de embudo para un Canvas con un menú desplegable de los eventos de informe disponibles.]({% image_buster /assets/img/funnel_report/funnel_report3.png %}){: style="max-width:80%;"}

Los informes de embudo te permiten comparar el éxito de tus mensajes más allá de los eventos de conversión o los eventos de interacción con mensajes que configuraste inicialmente. Así que si hay un evento de conversión que no agregaste inicialmente, aún puedes rastrear las conversiones para ese evento usando un embudo.

Por ejemplo, si seleccionas una ventana de tiempo de informe de 14 días, seguida de los eventos `Added to cart` y `Made purchase`, verás tanto el número de usuarios que agregaron al carrito dentro de los 14 días posteriores a la recepción del mensaje como el número de usuarios que agregaron al carrito y luego realizaron una compra dentro de los 14 días posteriores a la recepción de la Campaign.

Como otro ejemplo, es posible que quieras ver el porcentaje de usuarios que convirtieron en un correo electrónico después de hacer clic en él. Para calcular esto, podrías crear un informe donde el segundo evento sea hacer clic en tu correo electrónico y el tercer evento sea realizar tu evento de conversión.

Después de seleccionar **Build Report**, el informe de embudo puede tardar varios minutos en generarse. Durante este tiempo, puedes navegar fuera del informe a otras páginas en el dashboard. Recibirás una notificación en el dashboard cuando tu informe esté listo.

## Interpretar tu informe de embudo {#interpreting-your-funnel-report}

En tu informe de embudo, puedes comparar directamente el grupo de control junto con las variantes que hayas configurado. Cada evento consecutivo mostrará qué porcentaje de los usuarios anteriores realizó esa acción y convirtió a través del embudo.

### Componentes del informe de embudo {#funnel-report-components}

- **Eje horizontal**: Muestra el porcentaje de destinatarios del mensaje que realizaron esas acciones.
- **Gráfico**: Muestra el número de mensajes recibidos, el número de usuarios que realizaron las acciones anteriores, así como la acción que elegiste, la tasa de conversión y el cambio porcentual respecto al control.
- **Opción de regenerar**: Te permite regenerar tu informe e indica cuándo se generó por última vez el informe actual.
- **Variantes**: Representadas por columnas de colores, los informes de embudo permiten hasta 8 variantes y un grupo de control. Por defecto, el **gráfico** solo mostrará tres variantes. Para ver más, puedes seleccionar manualmente el resto de las variantes.

![Gráfico de informe de embudo.]({% image_buster /assets/img/funnel_report/funnel_report4.jpg %})

**Para Campaigns con múltiples variantes**: Braze mostrará una tabla con métricas para cada evento y variante y el cambio porcentual respecto al control. La tasa de conversión es el número de usuarios que realizaron el evento (y los subsiguientes) por destinatario del mensaje.

**Para Campaigns con reelegibilidad**: Si un usuario recibe la Campaign más de una vez en la ventana de tiempo del informe, Braze determinará si el usuario debe incluirse en el embudo en función de las acciones que este usuario realizó después de la primera vez que recibió la Campaign dentro de la ventana de tiempo.
- Ten en cuenta que puede haber una discrepancia entre los valores de conversión del embudo y los estándar, ya que los usuarios pueden convertir más de una vez con la reelegibilidad, pero los informes de embudo convertirán un máximo de una vez incluso si un usuario realiza el evento más de una vez.

**Para Campaigns multivariantes con reelegibilidad**: Si un usuario recibe múltiples variantes de la Campaign durante la ventana de tiempo del informe, Braze determinará si debe incluirse en el embudo de la variante en función de las acciones que este usuario realizó después de la primera vez que recibió la variante de la Campaign. Esto significa que el mismo usuario podría contar para múltiples variantes diferentes si recibió múltiples variantes durante la ventana de tiempo del embudo.

{% alert important %}
Los usuarios huérfanos no se rastrean en los informes de embudo. Cuando un usuario anónimo ingresa a un Canvas o una Campaign y luego se identifica a través del método `changeUser()`, su ID de Braze cambia. Los informes de embudo solo rastrean eventos de seguimiento que coinciden con el ID de usuario en el momento de la entrada y no tienen en cuenta los eventos realizados por el usuario después de que su ID cambia. Esto significa que los eventos de conversión realizados por el usuario después de ser identificado no se incluirán en el informe de embudo.
{% endalert %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Un usuario sale del informe si se salta un evento? {#does-a-user-fall-out-of-the-report-if-they-skip-an-event}

Sí. Un usuario abandona el embudo en el primer paso donde no realiza el siguiente evento en la secuencia exacta que configuraste.

### ¿Cuántos eventos puedo incluir en un informe de embudo? {#how-many-events-can-i-include-in-a-funnel-report}

No hay un límite estricto, pero de cuatro a seis eventos cubre la mayoría de los casos de uso. Los embudos muy largos pueden ejecutarse lentamente o agotar el tiempo de espera.

### ¿Qué canales admiten el evento de embudo **Interactuó con paso**? {#what-channels-support-the-interacted-with-step-funnel-event}

**Interactuó con paso** está disponible para pasos en Canvas que utilicen canales de **correo electrónico** o **push**.

### ¿Por qué mi informe de embudo tarda mucho en cargar? {#why-is-my-funnel-report-taking-a-long-time-to-load}

Las consultas grandes pueden agotar el tiempo de espera. Intenta con una ventana de informe más corta, menos pasos en el embudo, o ambos.

### ¿Por qué los análisis del Canvas son diferentes del informe de embudo? {#why-are-the-analytics-on-the-canvas-different-from-the-funnel-report}

Los análisis de pasos en Canvas pueden mostrar conteos más altos que el embudo para las mismas fechas calendario porque los análisis de pasos incluyen interacciones y conversiones más amplias, mientras que el embudo aplica reglas de orden y temporalidad de eventos.

#### Análisis de Canvas (Analyze Variants) {#canvas-analytics-analyze-variants}

El rango de fechas filtra eventos por **cuándo ocurrieron**. Si seleccionas del 1 al 7 de enero, verás todas las entradas y eventos de conversión que ocurrieron durante esa ventana, independientemente de cuándo el usuario ingresó al Canvas. Un usuario que ingresó el 1 de enero pero convirtió el 8 de enero mostraría una entrada y cero conversiones, porque la conversión cayó fuera de las fechas seleccionadas. La ventana de conversión configurada en el paso del Canvas puede extenderse más allá de la ventana máxima de seguimiento del embudo, por lo que los análisis a nivel de paso pueden capturar conversiones en un horizonte más largo.

#### Informes de embudo

El rango de fechas filtra usuarios por **cuándo ingresaron** al Canvas. Si seleccionas del 1 al 7 de enero, el informe incluye a cada usuario que ingresó durante esa ventana, y luego rastrea sus acciones durante la ventana de finalización del embudo que configures (hasta 30 días después de la entrada). El mismo usuario que ingresó el 1 de enero y convirtió el 8 de enero mostraría una entrada y una conversión, porque la conversión ocurrió dentro de la ventana posterior a la entrada.

Además, los informes de embudo requieren que los eventos ocurran en el orden especificado y cuentan a cada usuario como máximo una vez, mientras que los análisis de Canvas cuentan todas las conversiones e interacciones sin una restricción de orden.