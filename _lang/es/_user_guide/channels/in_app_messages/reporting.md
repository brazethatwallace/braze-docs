---
nav_title: Informes
article_title: Informes de mensajes dentro de la aplicación
page_order: 21
description: "Este artículo de referencia cubre los informes y análisis de mensajes dentro de la aplicación, incluidos los detalles de la campaña, el rendimiento del mensaje y el rendimiento histórico."
channel:
  - in-app messages
tool:
  - Reports

---

# Informes de mensajes dentro de la aplicación {#iam-reporting}

> Este artículo de referencia cubre los informes y análisis de mensajes dentro de la aplicación, incluidos los detalles de la campaña, el rendimiento del mensaje y el rendimiento histórico.

{% multi_lang_include analytics/campaign_analytics.md channel="in-app message" %}

## Métricas de mensajes dentro de la aplicación {#in-app-message-metrics}

Estas son las métricas clave de mensajes dentro de la aplicación que puedes ver en tus análisis. Para obtener las definiciones de todas las métricas utilizadas en Braze, consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

{% alert note %}
Para los mensajes dentro de la aplicación, esta página define las impresiones únicas utilizando un límite de día calendario en la zona horaria de tu espacio de trabajo.
{% endalert %}

| Término | Definición |
| --- | --- |
| Impresiones únicas | El número total de personas que realmente vieron el mensaje dentro de la aplicación. Si un usuario recibe el mensaje más de una vez en el mismo día calendario en la zona horaria de tu espacio de trabajo, solo se cuenta una impresión única ese día. <br><br> **Si la reelegibilidad está activada:** Las impresiones únicas pueden incrementarse de nuevo en un nuevo día calendario en la zona horaria de tu espacio de trabajo si el usuario realiza la acción desencadenante otra vez. Para los mensajes dentro de la aplicación, *Impresiones únicas* equivale a *Destinatarios únicos* porque ambas se incrementan en un nuevo día calendario. |
| Impresiones totales | El número de veces que se visualiza el mensaje dentro de la aplicación. Se registra una impresión cuando el mensaje se hace visible en pantalla. Si un usuario ve el mensaje dos veces, se cuenta dos veces. <br><br> **Si hay varios dispositivos y la reelegibilidad está desactivada:** El usuario ve el mensaje dentro de la aplicación solo una vez. Aunque el usuario utilice varios dispositivos, solo lo ve en el primer dispositivo al que se dirige. Esto supone que el perfil tiene dispositivos consolidados y que el usuario ha iniciado sesión con un único ID de usuario en todos los dispositivos. <br><br> **Si la reelegibilidad está activada:** Se registra una impresión cada vez que el usuario ve el mensaje dentro de la aplicación. <br><br> **Nota:** *Impresiones totales* cuenta cada visualización. *Destinatarios únicos* es una métrica independiente que se rastrea utilizando un límite de día calendario en la zona horaria de tu espacio de trabajo. |
| Conversiones | El seguimiento de conversiones comienza después de que un usuario registra una impresión de un mensaje dentro de la aplicación. Se cuenta una conversión si el usuario ha recibido y visto la Campaign de mensaje dentro de la aplicación y posteriormente realiza el evento de conversión específico dentro de la ventana de conversión definida, independientemente de si hizo clic en el mensaje o no. <br><br> Las conversiones se atribuyen al mensaje recibido más recientemente. Si la reelegibilidad está habilitada, la conversión se asigna al último mensaje dentro de la aplicación recibido, siempre que ocurra dentro de la ventana de conversión definida. Sin embargo, si el mensaje dentro de la aplicación ya tiene una conversión asignada, no se puede registrar una nueva conversión para ese mensaje específico. Esto garantiza que cada entrega de mensaje dentro de la aplicación se asocie con una sola conversión. |
| Conversiones totales | Cuando un usuario ve una Campaign de mensaje dentro de la aplicación solo una vez, solo se cuenta una conversión, incluso si realiza el evento de conversión varias veces después. Sin embargo, si la reelegibilidad está activada y el usuario ve la Campaign de mensaje dentro de la aplicación varias veces, las *Conversiones totales* pueden aumentar una vez por cada vez que el usuario registra una impresión para una nueva instancia de la Campaign de mensaje dentro de la aplicación. <br><br> Por ejemplo, si un usuario desencadena un mensaje dentro de la aplicación dos veces y convierte después de cada impresión (lo que resulta en dos conversiones), las *Conversiones totales* aumentan en dos. Sin embargo, si solo hubo una impresión seguida de dos eventos de conversión, solo se registra una conversión y las *Conversiones totales* aumentan en uno. |
| Tasa de conversión | La métrica de impresiones únicas diarias totales (*Impresiones únicas*) se utiliza para calcular la tasa de conversión. <br><br> Tasa de conversión = (Conversiones primarias) / (Impresiones únicas) <br><br> Para los mensajes dentro de la aplicación, las *Impresiones únicas* solo se pueden contar una vez por día calendario en la zona horaria de tu espacio de trabajo. El número de veces que un usuario completa una acción deseada (una "conversión") puede aumentar dentro de ese mismo día calendario. Por lo tanto, si un usuario completa una conversión varias veces en un día, la *Tasa de conversión* puede aumentar en consecuencia, pero las *Impresiones únicas* solo se cuentan una vez para ese día calendario. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas de mensajes dentro de la aplicación" }

{% alert tip %}
Las *Impresiones totales* pueden superar a las *Impresiones únicas* cuando un usuario ve el mensaje más de una vez en el mismo día calendario (consulta las definiciones de métricas en la tabla anterior). Para investigar usuarios con recuentos de impresiones inflados, crea un Segment con el filtro **Device Count** configurado en **more than** `1`, y el filtro **Received Message from Campaign** para la Campaign específica.
{% endalert %}

### Seguimiento de clics {#click-tracking}

Braze registra una impresión cuando un mensaje dentro de la aplicación se hace visible en pantalla. Para los mensajes dentro de la aplicación creados con el [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional), la siguiente tabla describe qué cuenta como un clic.

| Acción del usuario | Clic registrado |
|-------------|--------------|
| El usuario hace clic en el cuerpo del mensaje cuando el mensaje no tiene botones | Sí (clic en el cuerpo) |
| El usuario hace clic en un botón | Sí (clic en el botón) |
| El usuario hace clic en el botón de cerrar (X) | No |
| El usuario toca o hace clic fuera del mensaje para descartarlo (cuando está habilitado) | No |
| El usuario cierra la aplicación mientras se muestra el mensaje | No |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Seguimiento de clics" }

#### Métricas de mensajes a pantalla completa por acción del usuario {#fullscreen-metrics-by-user-action}

Para los mensajes dentro de la aplicación [a pantalla completa]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/fullscreen) creados con el editor tradicional, la siguiente tabla muestra lo que Braze registra para las acciones comunes del usuario. Se registra una impresión cuando el mensaje se hace visible en pantalla.

| Acción del usuario | Pantalla completa con botones | Pantalla completa sin botones |
| --- | --- | --- |
| El usuario ve un mensaje dentro de la aplicación, no hace clic en nada y cierra la aplicación | 1 impresión | 1 impresión |
| El usuario ve un mensaje dentro de la aplicación y hace clic en el botón de cerrar | 1 impresión | 1 impresión |
| El usuario ve un mensaje dentro de la aplicación y hace clic en un botón CTA | 1 clic en el botón y 1 impresión | N/A |
| El usuario ve un mensaje dentro de la aplicación y toca la pantalla pero no un botón | 1 impresión<br><br>Tocar el mensaje dentro de la aplicación no cierra el mensaje | 1 clic en el cuerpo y 1 impresión<br><br>Tocar el mensaje dentro de la aplicación cierra el mensaje o desencadena el comportamiento al hacer clic |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Métricas de mensajes dentro de la aplicación a pantalla completa por comportamiento del usuario" }

{% alert note %}
Los clics en el cuerpo no se recopilan automáticamente para los mensajes dentro de la aplicación creados con el [editor de arrastrar y soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop). Para registrar clics en el cuerpo, añade un bloque de **Custom code** y llama a `brazeBridge.logClick()`. Para más detalles, consulta [Seguimiento de botones]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#button-tracking-improvements) y [Puente JavaScript]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge).
{% endalert %}

Para las definiciones de clics en el cuerpo y clics en botones, consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

Para los desequilibrios de impresiones entre el grupo de control y la variante en las pruebas A/B, consulta [Discrepancias entre el grupo de control y la variante]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#discrepancies-between-the-control-group-and-variant).

## ¿Cómo se incrementan las conversiones con la reelegibilidad? {#how-do-conversions-increment-with-re-eligibility}

Braze asigna solo una conversión a cada entrega de mensaje dentro de la aplicación y la atribuye al mensaje recibido más recientemente.

Con la reelegibilidad activada, cada nueva entrega puede generar su propia conversión. Por ejemplo, si un usuario ve el mismo mensaje dentro de la aplicación cinco veces y convierte después de cada impresión, se cuentan cinco conversiones. Si un usuario ve el mensaje solo una vez pero convierte varias veces después, solo se cuenta una conversión.

Si un usuario ve un mensaje dentro de la aplicación en dos días distintos pero convierte en el tercer día, Braze registra la conversión contra la impresión del segundo día. Para los Canvas, las conversiones se rastrean por entrada al Canvas, no por paso. Si un usuario convierte en varios pasos durante la misma entrada, solo se cuenta como una conversión.

{% tabs local %}
{% tab Escenario 1 %}

*Un usuario recibe el mismo mensaje dentro de la aplicación cinco veces en un solo día y convierte cinco veces ese mismo día.*

Sarah recibe un mensaje dentro de la aplicación de una app de compras sobre una oferta por tiempo limitado en su marca favorita de zapatos. Hace clic en el mensaje y compra dos pares de zapatos.

Unas horas después, recibe el mismo mensaje dentro de la aplicación de nuevo y decide comprar otro par de zapatos. Esto ocurre un total de cinco veces en un solo día, y Sarah termina realizando cinco compras separadas, cada vez después de hacer clic en el mensaje dentro de la aplicación.

**Resultados:** *Total de conversiones* y *Total de impresiones* para Sarah se incrementan en cinco para ese único día. Dado que las *Impresiones únicas* solo pueden incrementarse de nuevo después de un límite de día calendario en la zona horaria del espacio de trabajo, las *Impresiones únicas* permanecen iguales. Esto hace que la *Tasa de conversión* aumente dentro de ese período.

{% alert note %}
Cada impresión y conversión en este escenario se procesa como un evento de SDK or kit de desarrollo de software separado. Si tu SDK or kit de desarrollo de software agrupa un evento de impresión y uno de conversión juntos, el recuento de conversiones puede diferir.
{% endalert %}

{% endtab %}
{% tab Escenario 2 %}

*Un usuario recibe un mensaje dentro de la aplicación y convierte en un solo día.*

Lena recibe un mensaje dentro de la aplicación sobre un nuevo curso de aprendizaje. Hace clic en el mensaje y comienza el curso. Mientras está en la aplicación, también se inscribe en cuatro cursos más. Todo esto ocurre el mismo día después de recibir solo un mensaje.

**Resultados:** *Total de conversiones* y *Total de impresiones* para Lena se incrementan en uno.

{% endtab %}
{% tab Escenario 3 %}

*Un usuario recibe un mensaje dentro de la aplicación y convierte un día después.*

Tom es un cliente habitual de una aplicación de comercio electrónico. Recibe un mensaje dentro de la aplicación que promociona un descuento por tiempo limitado en un producto que le interesa. Tom hace clic en el mensaje pero decide no comprar de inmediato. Al día siguiente, Tom recuerda el descuento y realiza la compra, que se atribuye al mensaje dentro de la aplicación que recibió el día anterior.

**Resultados:** *Total de conversiones* y *Total de impresiones* para Tom se incrementan en uno.

{% endtab %}
{% tab Escenario 4 %}

*Un usuario recibe un mensaje dentro de la aplicación y convierte dos veces un día después.*

Alex descargó recientemente una aplicación de juegos arcade. Un día, Alex recibe un mensaje dentro de la aplicación que le anima a completar un nivel en un juego nuevo. Alex hace clic en el mensaje pero se distrae y no completa ningún nivel. Al día siguiente, Alex completa dos niveles en el mismo juego.

**Resultados:** Dado que completar un nivel es el evento de conversión, Alex convirtió dos veces en el segundo día. Sin embargo, como solo recibió un mensaje dentro de la aplicación, *Total de conversiones* y *Total de impresiones* para Alex se incrementan en uno.

{% endtab %}
{% tab Escenario 5 %}

*Un usuario recibe el mismo mensaje dentro de la aplicación dos veces en un solo día y convierte dos veces al día siguiente.*

John es un profesional ocupado que depende de una aplicación de entregas para pedir comida de sus restaurantes favoritos. En su trayecto al trabajo, activa una geovalla y recibe un mensaje dentro de la aplicación que promociona restaurantes cercanos. Cuando regresa a casa más tarde, recibe ese mismo mensaje de nuevo porque la reelegibilidad está activada. Aunque le gustan las ofertas, decide no pedir nada ese día.

Al día siguiente, John pide almuerzo y cena a través de la aplicación, realizando el evento de conversión dos veces.

**Resultados:** *Total de conversiones* para John se incrementa en uno, y *Total de impresiones* se incrementa en dos. Dado que la reelegibilidad está activada, la conversión se asigna al último mensaje dentro de la aplicación que John recibió (la segunda impresión). Solo se puede registrar una conversión por cada entrega de mensaje dentro de la aplicación.

{% endtab %}
{% endtabs %}