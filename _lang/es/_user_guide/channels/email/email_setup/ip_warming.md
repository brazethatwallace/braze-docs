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

> El calentamiento de IP es la práctica de acostumbrar a los proveedores de buzones de correo electrónico a recibir mensajes desde tus direcciones IP dedicadas. Es una parte extremadamente importante del envío de correo electrónico con cualquier proveedor de servicios de correo electrónico (ESP) y una práctica estándar en Braze para confirmar que tus mensajes llegan a los buzones de entrada de destino a una tasa consistentemente alta.

El calentamiento de IP está diseñado para ayudarte a establecer una reputación positiva con los proveedores de servicios de Internet (ISP). Cada vez que se utiliza una nueva dirección IP para enviar un correo electrónico, los ISP supervisan programáticamente esos correos para verificar que no se estén utilizando para enviar correo no deseado a los usuarios. Piensa en la reputación de tu IP y dominio como una puntuación crediticia: los ISP utilizan esta reputación para determinar si tu correo llega al buzón de entrada o a la carpeta de correo no deseado. Al igual que una puntuación crediticia, lleva tiempo construir una reputación positiva y aún más tiempo reconstruir una mala.

## Entrega y capacidad de entrega del correo electrónico {#email-delivery-and-deliverability}

La **entrega** es la proporción de correos electrónicos que fueron aceptados y no tuvieron un rebote duro. La **capacidad de entrega** se refiere a si el correo llega al buzón de entrada en lugar de a correo no deseado; los proveedores de buzones no exponen eso como una métrica única.

Una tasa de entrega saludable suele estar alrededor del 99 % entregado con una tasa de rebote no superior al 1 % aproximadamente. Las tasas pueden parecer sólidas en papel y aún así ocultar problemas (por ejemplo, muchos rebotes de un solo dominio, o correo entregado pero filtrado a correo no deseado). Observa las aperturas y los clics, no solo la entrega. Incluso una pequeña tasa reportada de correo no deseado puede justificar una revisión más profunda.

### Recomendaciones antes del calentamiento de IP {#recommendations-before-ip-warming}

Antes de comenzar el calentamiento de IP:

1. En **Settings** > **Email Preferences**, establece tu dominio de envío predeterminado, añade un enlace válido para cancelar suscripción en tu [pie de página personalizado]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer/), activa el [encabezado list-unsubscribe]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/#list-unsubscribe) y considera páginas personalizadas de cancelación de suscripción/adhesión voluntaria donde sea necesario.
2. Configura la [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/) para correo electrónico.
3. Crea las plantillas necesarias yendo a **Content** > **Email**.

## ¿Qué pasa si no tengo tiempo para calentar las IP? {#what-if-i-dont-have-time-to-warm-ips}

**El calentamiento de IP es obligatorio.** Si no calientas las IP adecuadamente y el patrón de tu correo electrónico genera alguna sospecha, la velocidad de entrega de tu correo electrónico podría reducirse o ralentizarse significativamente. Tu dominio o IP también podría ser bloqueado por los ISP, lo que puede resultar en que tus correos electrónicos vayan directamente a la carpeta de correo no deseado del buzón de entrada de tu usuario. Por eso, es importante calentar tus IP correctamente.

Los ISP limitan la entrega de correo electrónico cuando surge sospecha de correo no deseado para proteger a sus usuarios. Por ejemplo, si envías a 100.000 usuarios, el ISP podría entregar el correo electrónico solo a 5.000 de esos usuarios durante la primera hora. Luego, el ISP monitorea medidas de interacción como tasas de apertura, tasas de clics, cancelaciones de suscripción e informes de correos no deseados. Entonces, si se produce un número significativo de informes de correo no deseado, podrían optar por relegar el resto de ese envío a la carpeta de correo no deseado en lugar de entregarlo al buzón de entrada del usuario.

Si la interacción es moderada, pueden continuar limitando tu correo electrónico para recopilar más datos de interacción y determinar con mayor certeza si el correo electrónico es correo no deseado o no. Si el correo electrónico tiene métricas de interacción muy altas, pueden dejar de limitar este correo electrónico por completo. Utilizan esos datos para crear una reputación de correo electrónico que eventualmente determinará si tus correos electrónicos se filtran automáticamente como correo no deseado.

Si tu dominio o IP es bloqueado por un ISP, los registros de mensajes en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) contendrán información sobre qué sitios web visitar para apelar ante estos ISP y salir de esas listas.

## Programas de calentamiento de IP {#ip-warming-schedules}

Recomendamos encarecidamente seguir estrictamente un programa de calentamiento de IP para apoyar la capacidad de entrega. También es importante que no te saltes días, ya que el escalado consistente mejora las métricas de entrega. Elige un programa basado en tu historial de envío de correo electrónico existente y tus métricas de capacidad de entrega.

{% alert tip %}
Si te interesa tener un recurso dedicado de capacidad de entrega como parte de tu equipo de cuenta, ponte en contacto con tu director de cuentas de Braze para obtener más información.
{% endalert %}

{% tabs local %}
{% tab Conservador %}

El programa conservador es un enfoque más lento y cauteloso que ayuda a establecer una sólida reputación de envío desde cero. Se recomienda si eres nuevo en el envío de correo electrónico, estás migrando desde una IP compartida o has experimentado problemas de capacidad de entrega como limitación o bloqueo por parte de un proveedor de buzones de entrada.

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
10 | 1.000
11 | 1.000
12 | 1.000
13 | 2.000
14 | 2.000
15 | 2.000
16 | 4.000
17 | 4.000
18 | 4.000
19 | 8.000
20 | 8.000
21 | 8.000
22+ | Duplicar cada 3 días hasta alcanzar el volumen deseado

{% endtab %}
{% tab Moderado %}

El programa moderado es un enfoque equilibrado que aumenta el volumen de envío a un ritmo constante. Se recomienda para la mayoría de los remitentes, incluidos aquellos con algo de historial de envío de correo electrónico que están haciendo la transición a una nueva IP.

Día | Número de correos electrónicos a enviar
----|---------------------
1 | 50
2 | 100
3 | 500
4 | 1.000
5 | 2.000
6 | 4.000
7 | 8.000
8 | 16.000
9 | 25.000
10 | 35.000
11 | 50.000
12 | 75.000
13 | 100.000
14 | 150.000
15 | 200.000
16 | 275.000
17 | 375.000
18 | 500.000
19 | 650.000
20 | 825.000
21 | 1.000.000
22+ | Duplicar cada 2 días hasta alcanzar el volumen deseado

{% endtab %}
{% tab Agresivo %}

{% alert important %}
El programa agresivo es el enfoque más rápido y solo se recomienda para remitentes con un historial de envío establecido y positivo y métricas de capacidad de entrega que se alineen con las buenas prácticas, incluyendo altas tasas de apertura, altas tasas de clics y bajas tasas de rebote. Usar este programa sin un historial comprobado puede dañar tu reputación como remitente.
{% endalert %}

Día | Número de correos electrónicos a enviar
----|---------------------
1 | 50
2 | 100
3 | 500
4 | 1.000
5 | 2.500
6 | 5.000
7 | 9.000
8 | 16.000
9 | 29.000
10 | 52.000
11 | 98.000
12 | 160.000
13 | 225.000
14 | 315.000
15 | 450.000
16 | 615.000
17 | 875.000
18 | 1.200.000
19 | 1.750.000
20 | 2.750.000
21+ | Duplicar diariamente hasta alcanzar el volumen deseado

{% endtab %}
{% endtabs %}

En la mayoría de los casos, calienta hasta tu volumen de envío diario promedio en lugar de tu pico. Los ISP principalmente observan las últimas semanas de comportamiento de envío para evaluar tu reputación, así que si alcanzas el volumen pico solo cada pocos meses (por ejemplo, 7 millones durante un período estacional), puedes aumentar gradualmente hacia ese pico más cerca de la fecha de envío. Sin embargo, si alcanzas el volumen pico cada una o dos semanas, calienta hasta ese pico desde el principio.

Una vez que el calentamiento de IP esté completo y hayas alcanzado tu volumen diario deseado, debes intentar mantener ese volumen diariamente. Se espera cierta fluctuación, pero alcanzar el volumen deseado y luego solo hacer un envío masivo una vez por semana puede afectar negativamente tus métricas de entrega y tu reputación como remitente.

{% alert important %}
La mayoría de los ISP solo almacenan datos de reputación durante 30 días. Si pasas un mes sin enviar ningún mensaje, debes repetir el proceso de calentamiento de IP.
{% endalert %}

### Direcciones IP {#ip-addresses}

Después de tres meses sin uso, Braze puede reciclar y reasignar direcciones IP. Independientemente del historial previo de una dirección IP, se recomienda un calentamiento de IP completo para todas las IP recién asignadas, ya que la mayoría de los ISP solo almacenan datos de reputación durante 30 días. Para la mayoría de los ISP, esto significa que un período de inactividad de tres meses restablece efectivamente la reputación. Si tienes más preguntas sobre el historial de una dirección IP específica, ponte en contacto con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support/).

## Cómo limitar los envíos durante el calentamiento {#how-to-limit-sends-during-warming}

Nuestra función integrada de limitación de usuarios sirve como una herramienta útil para ayudarte con el calentamiento de tu dirección IP. Después de elegir los segmentos de mensajería deseados durante la creación de la campaña, en el paso [Target Users]({{site.baseurl}}/user_guide/channels/email/html_editor/#step-4-build-the-remainder-of-your-campaign-or-canvas), selecciona el desplegable **Advanced Options** para limitar tus usuarios. A medida que continúa tu programa de calentamiento, puedes aumentar gradualmente este límite para incrementar el volumen de correos electrónicos que envías.

![]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Segmentación de subdominios {#subdomain-segmentation}

Muchos ISP y proveedores de acceso a correo electrónico ya no filtran solo por la reputación de la dirección IP. Estas tecnologías de filtrado ahora también tienen en cuenta la reputación basada en el dominio. Esto significa que los filtros examinarán todos los datos asociados con el dominio del remitente y no solo aislarán la dirección IP. Por esta razón, además de calentar tu IP de correo electrónico, también recomendamos tener dominios o subdominios separados para correo de marketing, transaccional y corporativo.

{% alert important %}
La segmentación de subdominios es especialmente importante para remitentes de gran volumen. Estos remitentes deben trabajar con un representante de Braze al configurar su cuenta para confirmar que siguen esta práctica.
{% endalert %}

Recomendamos segmentar tus dominios de modo que el correo corporativo se envíe a través de tu dominio de nivel superior, y el correo de marketing y transaccional se envíe a través de diferentes dominios o subdominios.

## Buenas prácticas {#best-practices}

Puedes evitar todas las consecuencias de no calentar las IP siguiendo estas buenas prácticas:

### Comienza con volúmenes pequeños de envío de correo electrónico {#start-with-small-sending-volumes-of-email}

Aumenta la cantidad que envías cada día de la forma más gradual posible. Las campañas de correo electrónico abruptas y de alto volumen son vistas con mayor escepticismo por los ISP. Por lo tanto, debes comenzar enviando pequeñas cantidades de correo electrónico y escalar gradualmente hacia el volumen de correo electrónico que finalmente pretendes enviar. Ten en cuenta que estás calentando tu IP en cada ISP individualmente: los ISP no comparten datos de reputación entre sí. Al planificar tus volúmenes de calentamiento, asegúrate de no aumentar el volumen demasiado rápido en ningún ISP individual. Independientemente del volumen, sugerimos calentar tu IP para estar seguro. Consulta los [programas de calentamiento de IP](#ip-warming-schedules).

### Ten contenido introductorio atractivo {#have-engaging-introductory-content}

Confirma que tu primer contenido sea altamente atractivo y maximice la probabilidad de que los usuarios hagan clic, abran e interactúen con tu correo electrónico. Siempre prefiere correos electrónicos bien segmentados a envíos indiscriminados al calentar las IP.

### Establece una cadencia de envío consistente {#set-a-consistent-sending-cadence}

Una vez que el calentamiento de IP esté completo, crea una cadencia de envío, asegurándote también de distribuir tus correos electrónicos a lo largo de un día o varios días. Al crear un programa lo más consistente posible, puedes prevenir un enfriamiento de IP, que puede ocurrir si el volumen de envío se detiene o disminuye significativamente durante más de unos pocos días.

Consulta nuestro [programa de calentamiento de IP](#ip-warming-schedules) para distribuir tu envío a lo largo de un período de tiempo más largo, en lugar de enviar un envío masivo en un único momento específico.

### Limpia tus listas de correo electrónico {#clean-your-email-lists}

Confirma que tu lista de correo electrónico esté limpia y no tenga correos electrónicos antiguos o no verificados. Asegurarte de cumplir con [CASL y CAN-SPAM]({{site.baseurl}}/user_guide/administer/global/privacy/spam_regulations/) es lo ideal.

### Monitorea tu reputación como remitente {#monitor-your-sender-reputation}

Al realizar el proceso de calentamiento de IP, asegúrate de monitorear cuidadosamente tu reputación como remitente. Estas métricas específicas son importantes de observar:
- **Tasas de rebote:** Si alguna campaña rebota a más del 3-5 %, debes evaluar la limpieza de tu lista siguiendo las directrices de nuestro artículo [Keep It Clean: The Importance of Email List Hygiene](https://www.braze.com/blog/email-list-hygiene/). Además, debes considerar implementar una [política de desactivación]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/) para dejar de enviar correos electrónicos a direcciones de correo electrónico no comprometidas o inactivas.
- **Informes de correos no deseados:** Si alguna campaña es reportada como correo no deseado a una tasa superior al 0,08 %, debes reevaluar el contenido que estás enviando, verificar que esté dirigido a una audiencia interesada y asegurarte de que tus correos electrónicos estén redactados adecuadamente para despertar su interés.
- **Tasas de apertura:** Las tasas de apertura son un indicador útil de la ubicación en el buzón de entrada. Si tus tasas de apertura únicas superan el 25 %, es probable que estés experimentando una alta ubicación en el buzón de entrada, lo que indica una reputación positiva como remitente.

{% alert tip %}
Braze no recomienda usar [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/) para calentar tus IP. Dado que las campañas de calentamiento de IP son algunas de las primeras campañas que envías, Braze no tendrá suficiente información sobre tus usuarios para calcular un momento de envío óptimo. En este caso, todos los mensajes con Intelligent Timing se enviarían por defecto a la hora alternativa y se enviarían al mismo tiempo de todos modos.
{% endalert %}

{% alert tip %}
Es normal que el correo se envíe a la carpeta de correo no deseado durante el calentamiento de IP porque tu dominio e IP aún no han establecido una reputación positiva. Si el correo llega a tu carpeta de correo no deseado, es posible que tu administrador de correo necesite añadir tu dominio de envío de Braze y tu IP a la lista de permitidos de tu empresa.
{% endalert %}