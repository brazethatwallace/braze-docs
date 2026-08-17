---
nav_title: Calentamiento de IP
article_title: Calentamiento de IP
page_order: 1
page_type: reference
description: "Este artículo de referencia trata el tema del calentamiento de IP y las buenas prácticas."
channel: email
local_redirect:
  automated-ip-warming: '/docs/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming'
---

# Calentamiento de IP {#ip-warming}

> El calentamiento de IP es la práctica de acostumbrar a los proveedores de buzones de correo electrónico a recibir mensajes desde tus direcciones IP dedicadas. Es una parte extremadamente importante del envío de correo electrónico con cualquier proveedor de servicios de correo electrónico (ESP) y una práctica estándar en Braze para confirmar que tus mensajes llegan a los buzones de entrada de destino a una tasa consistentemente alta. Si utilizas el [calentamiento de IP automatizado]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming), consulta las [Preguntas frecuentes sobre el calentamiento de IP automatizado]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/faq).

El calentamiento de IP está diseñado para ayudarte a establecer una reputación positiva con los proveedores de servicios de Internet (ISP). Cada vez que se utiliza una nueva dirección IP para enviar un correo electrónico, los ISP supervisan programáticamente esos correos para verificar que no se estén utilizando para enviar correo no deseado a los usuarios. Piensa en la reputación de tu IP y dominio como una puntuación crediticia: los ISP utilizan esta reputación para determinar si tu correo llega al buzón de entrada o a la carpeta de correo no deseado. Al igual que una puntuación crediticia, lleva tiempo construir una reputación positiva y aún más tiempo reconstruir una mala.

## Entrega y capacidad de entrega de correo electrónico {#email-delivery-and-deliverability}

La **entrega** es la proporción de correos electrónicos que fueron aceptados y no tuvieron un rebote duro. La **capacidad de entrega** se refiere a si el correo llega al buzón de entrada en lugar de a correo no deseado; los proveedores de buzón de entrada no exponen eso como una métrica única.

Una tasa de entrega saludable suele rondar el 99 % de entrega con una tasa de rebote no superior a aproximadamente el 1 %. Las tasas pueden parecer sólidas sobre el papel y aun así ocultar problemas (por ejemplo, muchos rebotes de un solo dominio, o correo entregado pero filtrado como correo no deseado). Observa las aperturas y los clics, no solo la entrega. Incluso una tasa de informes de correos no deseados pequeña puede justificar una revisión más profunda.

### Recomendaciones antes del calentamiento de IP {#recommendations-before-ip-warming}

Antes de comenzar el calentamiento de IP:

1. En **Configuración** > **Preferencias de correo electrónico**, establece tu dominio de envío predeterminado, añade un enlace de cancelación de suscripción válido en tu [pie de página personalizado]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer), activa el [encabezado de cancelación de suscripción de lista]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe) y considera páginas personalizadas de cancelación de suscripción o adhesión voluntaria donde sea necesario.
2. Configura la [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) para correo electrónico.
3. Crea tus plantillas necesarias yendo a **Contenido** > **Correo electrónico**.

## ¿Qué pasa si no tengo tiempo para calentar las IP? {#what-if-i-dont-have-time-to-warm-ips}

**El calentamiento de IP es obligatorio.** Si no calientas las IP de forma adecuada y el patrón de tu correo electrónico genera alguna sospecha, la velocidad de entrega de tu correo electrónico podría verse significativamente limitada o ralentizada. Tu dominio o IP también podría ser bloqueado por los ISP, lo que puede provocar que tus correos electrónicos vayan directamente a la carpeta de correo no deseado del buzón de entrada de tu usuario. Por eso, es importante calentar tus IP correctamente.

Los ISP limitan la entrega de correo electrónico cuando surge sospecha de correo no deseado para proteger a sus usuarios. Por ejemplo, si envías a 100.000 usuarios, el ISP podría entregar el correo electrónico solo a 5.000 de esos usuarios durante la primera hora. Luego, el ISP monitorea métricas de participación como las tarifas abiertas, las tasas de clics, las cancelaciones de suscripción y los informes de correos no deseados. Entonces, si se produce un número significativo de informes de correos no deseados, podrían optar por relegar el resto de ese envío a la carpeta de correo no deseado en lugar de entregarlo al buzón de entrada del usuario.

Si la participación es moderada, pueden continuar limitando tu correo electrónico para recopilar más datos de participación y determinar con mayor certeza si el correo electrónico es o no correo no deseado. Si el correo electrónico tiene métricas de participación muy altas, pueden dejar de limitar este correo electrónico por completo. Utilizan esos datos para crear una reputación de correo electrónico que determina si tus correos electrónicos se filtran automáticamente como correo no deseado.

Si tu dominio o IP es bloqueado por un ISP, los registros de mensajes en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) contendrán información sobre qué sitios web visitar para apelar ante estos ISP y salir de esas listas.

## Programaciones de calentamiento de IP {#ip-warming-schedules}

Recomendamos encarecidamente seguir estrictamente una programación de calentamiento de IP para favorecer la capacidad de entrega. También es importante que no te saltes días, ya que el escalado constante mejora las métricas de entrega. Elige una programación en función de tu historial de envío de correo electrónico y tus métricas de capacidad de entrega.

{% alert tip %}
Si te interesa contar con un recurso dedicado de capacidad de entrega como parte de tu equipo de cuentas, ponte en contacto con tu director de cuentas de Braze para obtener más información.
{% endalert %}

{% tabs local %}
{% tab Conservadora %}

La programación conservadora es un enfoque más lento y cauteloso que ayuda a establecer una sólida reputación de envío desde cero. Se recomienda si eres nuevo en el envío de correo electrónico, estás migrando desde una IP compartida o has experimentado problemas de capacidad de entrega, como limitación o bloqueo por parte de un proveedor de buzón de entrada.

Día | Número de correos electrónicos a enviar
----|---------------------
1 | 50
2 | 50
3 | 50
4 | 100
5 | 100
6 | 100
7 | 500
8 | 500
9 | 500
10 | 1,000
11 | 1,000
12 | 1,000
13 | 2,000
14 | 2,000
15 | 2,000
16 | 4,000
17 | 4,000
18 | 4,000
19 | 8,000
20 | 8,000
21 | 8,000
22+ | Duplicar cada 3 días hasta alcanzar el volumen deseado

{% endtab %}
{% tab Moderada %}

La programación moderada es un enfoque equilibrado que aumenta el volumen de envío a un ritmo constante. Se recomienda para la mayoría de los remitentes, incluidos aquellos con cierto historial de envío de correo electrónico que están haciendo la transición a una nueva IP.

Día | Número de correos electrónicos a enviar
----|---------------------
1 | 50
2 | 100
3 | 500
4 | 1,000
5 | 2,000
6 | 4,000
7 | 8,000
8 | 16,000
9 | 25,000
10 | 35,000
11 | 50,000
12 | 75,000
13 | 100,000
14 | 150,000
15 | 200,000
16 | 275,000
17 | 375,000
18 | 500,000
19 | 650,000
20 | 825,000
21 | 1,000,000
22+ | Duplicar cada 2 días hasta alcanzar el volumen deseado

{% endtab %}
{% tab Agresiva %}

{% alert important %}
La programación agresiva es el enfoque más rápido y solo se recomienda para remitentes con un historial de envío establecido y positivo, y métricas de capacidad de entrega que se ajusten a las mejores prácticas, incluidas altas tasas de apertura, altas tasas de clics y bajas tasas de rebote. Usar esta programación sin un historial probado puede perjudicar tu reputación del remitente.
{% endalert %}

Día | Número de correos electrónicos a enviar
----|---------------------
1 | 50
2 | 100
3 | 500
4 | 1,000
5 | 2,500
6 | 5,000
7 | 9,000
8 | 16,000
9 | 29,000
10 | 52,000
11 | 98,000
12 | 160,000
13 | 225,000
14 | 315,000
15 | 450,000
16 | 615,000
17 | 875,000
18 | 1,200,000
19 | 1,750,000
20 | 2,750,000
21+ | Duplicar diariamente hasta alcanzar el volumen deseado

{% endtab %}
{% endtabs %}

En la mayoría de los casos, calienta hasta tu volumen de envío diario promedio en lugar de tu volumen máximo. Los ISP evalúan principalmente las últimas semanas de comportamiento de envío para determinar tu reputación, por lo que si alcanzas el volumen máximo solo cada pocos meses (por ejemplo, 7 millones durante un periodo estacional), puedes aumentar gradualmente hacia ese pico más cerca de la fecha de envío. Sin embargo, si alcanzas el volumen máximo cada una o dos semanas, calienta hasta ese pico desde el principio.

Una vez que el calentamiento de IP se haya completado y hayas alcanzado el volumen diario deseado, debes intentar mantener ese volumen a diario. Se esperan algunas fluctuaciones, pero alcanzar el volumen deseado y luego hacer un envío masivo solo una vez por semana puede afectar negativamente tus métricas de entrega y la reputación del remitente.

{% alert important %}
La mayoría de los ISP solo almacenan datos de reputación durante 30 días. Si pasas un mes sin enviar ningún mensaje, debes repetir el proceso de calentamiento de IP.
{% endalert %}

### Direcciones IP {#ip-addresses}

Después de tres meses sin uso, Braze puede reciclar y reasignar direcciones IP. Independientemente del historial previo de una dirección IP, se recomienda un calentamiento de IP completo para todas las IP recién asignadas, ya que la mayoría de los ISP solo almacenan datos de reputación durante 30 días. Para la mayoría de los ISP, esto significa que un periodo de inactividad de tres meses restablece efectivamente la reputación. Si tienes más preguntas sobre el historial de una dirección IP específica, ponte en contacto con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Cómo limitar los envíos durante el calentamiento {#how-to-limit-sends-during-warming}

Nuestra función integrada de limitación de usuarios es una herramienta útil para ayudarte con el calentamiento de tu dirección IP. Después de elegir los Segments de mensajería deseados durante la creación de la campaña, en el paso [Usuarios objetivo]({{site.baseurl}}/user_guide/channels/email/html_editor#step-4-build-the-remainder-of-your-campaign-or-canvas), selecciona el desplegable **Advanced Options** para limitar tus usuarios. A medida que avanza tu programación de calentamiento, puedes aumentar gradualmente este límite para incrementar el volumen de correos electrónicos que envías.

![Nuestra función integrada de limitación de usuarios es una herramienta útil para ayudarte con el calentamiento de tu dirección IP. Después de elegir los segmentos de mensajería deseados durante la creación de la campaña, en el paso Usuarios objetivo, selecciona el desplegable Opciones avanzadas para limitar tus usuarios. A medida que avanza tu programación de calentamiento, puedes aumentar gradualmente este límite para incrementar el volumen de correos electrónicos que envías.]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Segmentación de subdominios {#subdomain-segmentation}

Muchos ISP y proveedores de acceso al correo electrónico ya no filtran únicamente por la reputación de la dirección IP. Estas tecnologías de filtrado ahora también tienen en cuenta la reputación basada en el dominio. Esto significa que los filtros analizarán todos los datos asociados con el dominio del remitente y no solo la dirección IP de forma aislada. Por esta razón, además de calentar tu IP de correo electrónico, también recomendamos tener dominios o subdominios separados para correo de marketing, transaccional y corporativo.

{% alert important %}
La segmentación de subdominios es especialmente importante para los remitentes de gran volumen. Estos remitentes deben trabajar con un representante de Braze al configurar su cuenta para confirmar que siguen esta práctica.
{% endalert %}

Recomendamos segmentar tus dominios de modo que el correo corporativo se envíe a través de tu dominio de nivel superior, y el correo de marketing y transaccional se envíe a través de diferentes dominios o subdominios.

## Mejores prácticas {#best-practices}

Puedes evitar todas las consecuencias de no realizar el calentamiento de IP siguiendo estas mejores prácticas:

### Comienza con volúmenes pequeños de envío de correo electrónico {#start-with-small-sending-volumes-of-email}

Aumenta la cantidad que envías cada día de la forma más gradual posible. Las campañas de correo electrónico abruptas y de alto volumen son las que generan más desconfianza por parte de los ISP. Por lo tanto, debes comenzar enviando pequeñas cantidades de correo electrónico y escalar gradualmente hacia el volumen de correo electrónico que finalmente pretendes enviar. Ten en cuenta que estás calentando tu IP en cada ISP de forma individual: los ISP no comparten datos de reputación entre sí. Al planificar tus volúmenes de calentamiento, asegúrate de no aumentar el volumen demasiado rápido en ningún ISP individual. Independientemente del volumen, te sugerimos calentar tu IP para estar seguro. Consulta [Programaciones de calentamiento de IP](#ip-warming-schedules).

### Ten contenido introductorio atractivo {#have-engaging-introductory-content}

Confirma que tu primer contenido sea altamente atractivo y maximice la probabilidad de que los usuarios hagan clic, abran e interactúen con tu correo electrónico. Siempre prefiere correos electrónicos bien segmentados a envíos masivos indiscriminados al calentar las IP.

### Establece una cadencia de envío consistente {#set-a-consistent-sending-cadence}

Una vez que el calentamiento de IP esté completo, crea una cadencia de envío, asegurándote también de distribuir tus correos electrónicos a lo largo de un día o varios días. Al crear un calendario lo más consistente posible, puedes prevenir un enfriamiento de IP, que puede ocurrir si el volumen de envío se detiene o disminuye significativamente durante más de unos pocos días.

Consulta nuestra [programación de calentamiento de IP](#ip-warming-schedules) para distribuir tu envío a lo largo de un período de tiempo más prolongado, en lugar de enviar un envío masivo en un único momento específico.

### Limpia tus listas de correo electrónico {#clean-your-email-lists}

Confirma que tu lista de correo electrónico esté limpia y no contenga correos electrónicos antiguos o no verificados. Asegurarte de cumplir con las [normativas CASL y CAN-SPAM]({{site.baseurl}}/user_guide/administer/global/privacy/spam_regulations) es lo ideal.

### Supervisa tu reputación del remitente {#monitor-your-sender-reputation}

Al llevar a cabo el proceso de calentamiento de IP, asegúrate de supervisar cuidadosamente tu reputación del remitente durante el proceso. Estas métricas específicas son importantes de vigilar:
- **Tasas de rebote:** Si alguna campaña rebota a más del 3-5 %, debes evaluar la limpieza de tu lista siguiendo las directrices de nuestro artículo [Keep It Clean: The Importance of Email List Hygiene](https://www.braze.com/blog/email-list-hygiene/). Además, deberías considerar implementar una [política de desactivación]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies) para dejar de enviar correos electrónicos a direcciones de correo electrónico inactivas o sin participación.
- **Informes de correos no deseados:** Si alguna campaña es reportada como correo no deseado a una tasa superior al 0,08 %, debes reevaluar el contenido que estás enviando, verificar que esté dirigido a una audiencia interesada y asegurarte de que tus correos electrónicos estén redactados de forma adecuada para despertar su interés.
- **Tarifas abiertas:** Las tarifas abiertas son un indicador útil de la ubicación en el buzón de entrada. Si tus tarifas abiertas únicas superan el 25 %, es probable que estés experimentando una alta ubicación en el buzón de entrada, lo que indica una reputación del remitente positiva.

{% alert tip %}
Braze no recomienda usar la [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) para calentar tus IP. Dado que las campañas de calentamiento de IP son algunas de las primeras campañas que envías, Braze no tendrá suficiente información sobre tus usuarios para calcular un momento de envío óptimo. En este caso, todos los mensajes con sincronización inteligente usarían de forma predeterminada la hora alternativa y se enviarían al mismo tiempo de todos modos.
{% endalert %}

{% alert tip %}
Es normal que el correo se envíe a la carpeta de correo no deseado durante el calentamiento de IP porque tu dominio e IP aún no han establecido una reputación positiva. Si el correo llega a tu carpeta de correo no deseado, es posible que tu administrador de correo necesite agregar tu dominio de envío de Braze y tu IP a la lista de permitidos de tu empresa.
{% endalert %}