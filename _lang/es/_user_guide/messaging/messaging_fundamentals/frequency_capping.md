---
nav_title: Límite de velocidad y limitación de frecuencia
article_title: Límite de velocidad y limitación de frecuencia
page_order: 6
tool: Campaigns
page_type: reference
description: "Este artículo de referencia analiza el concepto de límite de velocidad y limitación de frecuencia en las campañas, y cómo puedes gestionar la presión de marketing para mejorar la experiencia del usuario."
---

# Límite de velocidad y limitación de frecuencia {#rate-limiting-and-frequency-capping}

> El límite de velocidad y la limitación de frecuencia se pueden usar juntos para asegurarte de que tus usuarios reciban los mensajes que necesitan.

## Acerca de los límites de velocidad {#about-rate-limiting}

Braze te permite controlar la presión de marketing limitando la velocidad de tus Campaigns y regulando la cantidad de tráfico saliente de tu plataforma. Puedes implementar dos tipos diferentes de límites de velocidad para tus Campaigns:

1. [Límite de velocidad centrado en el usuario:](#user-centric-rate-limiting) se centra en proporcionar la mejor experiencia para el usuario.
2. [Límite de velocidad de entrega:](#delivery-speed-rate-limiting) tiene en cuenta el ancho de banda de tus servidores.

Braze no admite un límite de velocidad por segundo. Braze intenta distribuir uniformemente los envíos de mensajes a lo largo del minuto, pero no puede garantizarlo. Por ejemplo, si tienes una Campaign con un límite de velocidad de 5000 mensajes por minuto, intentamos distribuir las 5000 solicitudes uniformemente a lo largo del minuto (alrededor de 84 mensajes por segundo), pero puede haber cierta variación en la tasa por segundo.

### Límite de velocidad centrado en el usuario {#user-centric-rate-limiting}

A medida que crees más Segments, habrá casos en los que la pertenencia a esos Segments se solape. Si estás enviando Campaigns a esos Segments, querrás asegurarte de que no estás enviando mensajes a tus usuarios con demasiada frecuencia. Si un usuario recibe demasiados mensajes en un periodo de tiempo corto, se sentirá sobrecargado y desactivará las notificaciones push o desinstalará tu aplicación.

#### Filtros de Segment relevantes {#relevant-segment-filters}

Braze proporciona los siguientes filtros para ayudarte a limitar la velocidad a la que tus usuarios reciben mensajes:

- Última interacción con mensaje
- Último mensaje recibido
- Última notificación push recibida
- Último correo electrónico recibido
- Último SMS recibido

#### Implementación de filtros {#implementing-filters}

Supongamos que hemos creado un Segment llamado "Retargeting Filter Showcase" con un filtro "Última vez que usó la app hace más de 7 días" para dirigirnos a los usuarios. Este sería un Segment estándar de reactivación.

Si tienes otros Segments más específicos que recibieron notificaciones recientemente, puede que no quieras que tus usuarios sean objetivo de Campaigns más genéricas dirigidas a este Segment. Al añadir el filtro "Última notificación push recibida" a este Segment, el usuario se asegura de que, si ha recibido otra notificación en las últimas 24 horas, saldrá de este Segment durante las siguientes 24 horas. Si sigue cumpliendo los otros criterios del Segment 24 horas después y no ha recibido más notificaciones, volverá a entrar en el Segment.

![Un Segment llamado "Retargeting Filter Showcase" con el grupo de filtros "Última vez que usó la app hace más de 7 días".]({% image_buster /assets/img_archive/rate_limit_daily.png %}){: style="max-width:80%;"}

Añadir este filtro a todos los Segments a los que se dirigen las Campaigns haría que tus usuarios recibieran un máximo de una notificación push cada 24 horas. Luego podrías priorizar tu mensajería asegurándote de que tus mensajes más importantes se entreguen antes que los menos importantes.

#### Establecer un límite máximo de usuarios {#setting-a-maximum-user-cap}

En el paso **Target Audiences** del creador de tu Campaign, también puedes limitar el número total de usuarios que recibirán tu mensaje. Esto sirve como una verificación independiente de los filtros de tu Campaign.

![Resumen de audiencia con una casilla seleccionada para limitar el número de personas que reciben la Campaign.]({% image_buster /assets/img_archive/total_limit.png %}){: style="max-width:50%;"}

Al seleccionar el límite máximo de usuarios, puedes limitar el volumen de mensajes enviados por canal o globalmente en todos los tipos de mensajes. Braze no envía mensajes a los usuarios asignados a grupos de control, por lo que no cuentan para el límite.

{% alert note %}
El límite máximo de usuarios limita el número de usuarios enviados, no el número de mensajes entregados con éxito. Dado que los mensajes abortados cuentan para este límite, el número real de mensajes enviados puede ser inferior al límite configurado. Por ejemplo, si estableces un límite de 10 000 y 2000 mensajes se abortan debido a la lógica de Liquid u otras condiciones, solo se envían 8000 mensajes.
{% endalert %}

##### Límite máximo de usuarios para Campaigns multicanal {#maximum-user-cap-for-multichannel-campaigns}

Para Campaigns multicanal, Braze selecciona primero una audiencia hasta tu límite máximo de usuarios configurado. Luego, Braze evalúa a cada usuario en esa audiencia limitada para cada canal de la Campaign.

Como resultado, el tamaño de la audiencia limitada se mantiene igual, pero los envíos por canal pueden diferir según la elegibilidad del canal. Por ejemplo, si estableces un límite máximo de usuarios de 500 000 y un usuario solo es elegible para push y Content Cards, ese usuario recibe esos canales pero no correo electrónico.

Si divides esos canales en Campaigns separadas que se dirigen al mismo Segment y cada una tiene su propio límite máximo de usuarios, cada Campaign evalúa y limita usuarios de forma independiente. Braze no garantiza que cada Campaign seleccione exactamente el mismo subconjunto de usuarios.

Si necesitas Campaigns de seguimiento dirigidas a usuarios que recibieron una Campaign anterior, crea un Segment utilizando el filtro **Received Campaign** y luego utiliza ese Segment para las Campaigns de seguimiento.

##### Límite máximo de usuarios con optimizaciones {#maximum-user-cap-with-optimizations}

Para una Campaign de envío único que utilice **Optimizar con BrazeAI<sup>TM</sup>**, la Campaign consta de dos envíos: el experimento inicial y el envío optimizado.

Para configurar un límite máximo de usuarios en este escenario, selecciona **Limitar volumen de envío**, luego selecciona **Duración de la Campaign** e introduce un valor para **Envíos máximos**. Tu límite de audiencia se divide según los porcentajes mostrados en el panel de **A/B Testing**.

Si seleccionas **Cada vez que se programe la Campaign**, esas dos fases se limitarán por separado al número establecido. Esto normalmente no es lo deseado.

#### Establecer un límite máximo de impresiones en Campaigns {#setting-a-maximum-impression-cap-on-campaigns}

Para los mensajes dentro de la aplicación, puedes controlar la presión de marketing estableciendo un número máximo de impresiones que se mostrarán a tu base de usuarios, después del cual Braze no enviará más mensajes a tus usuarios. Sin embargo, es importante señalar que este límite no es exacto.

Las reglas de mensajes dentro de la aplicación se envían a una aplicación al inicio de la sesión, lo que significa que Braze puede enviar un mensaje al usuario antes de que se alcance el límite, pero para cuando el usuario activa el mensaje, el límite ya se ha alcanzado. En esta situación, el dispositivo seguirá mostrando el mensaje.

Por ejemplo, supongamos que tienes un juego con un mensaje dentro de la aplicación que se activa cuando un usuario supera un nivel, y lo limitas a 100 impresiones. Ha habido 99 impresiones hasta ahora. Alice y Bob abren el juego, y Braze indica a sus dispositivos que son elegibles para recibir el mensaje cuando superen un nivel. Alice supera un nivel primero y recibe el mensaje. Bob supera el nivel después, pero como su dispositivo no se ha comunicado con los servidores de Braze desde que inició su sesión, su dispositivo no sabe que el mensaje ha alcanzado su límite, y él también recibe el mensaje. Sin embargo, cuando se ha alcanzado un límite de impresiones, la próxima vez que cualquier dispositivo solicite la lista de mensajes dentro de la aplicación elegibles, el sistema no enviará ese mensaje y lo eliminará de ese dispositivo.

### Límites de velocidad y pruebas A/B {#rate-limiting-and-ab-testing}

Al utilizar límites de velocidad con una prueba A/B, el límite de velocidad no se aplica al grupo de control de la misma manera que al grupo de prueba, lo cual es una fuente potencial de sesgo temporal. Para evitar este sesgo, utiliza ventanas de conversión adecuadas.

### Límite de velocidad de entrega {#delivery-speed-rate-limiting}

Si anticipas que Campaigns grandes provocarán un pico en la actividad de los usuarios y sobrecargarán tus servidores, puedes especificar un límite de velocidad por minuto para el envío de mensajes, lo que significa que Braze no envía más que tu configuración de límite de velocidad en un minuto.

Al dirigirte a los usuarios durante la creación de la Campaign, puedes ir a **Target Audiences** (para Campaigns) o **Send Settings** (para Canvas) para seleccionar un límite de velocidad (en varios incrementos desde tan bajo como 10 hasta tan alto como 500 000 mensajes por minuto).

Ten en cuenta que las Campaigns sin límite de velocidad pueden superar estos límites de entrega. Sin embargo, ten en cuenta que los mensajes se abortarán si se retrasan 72 horas o más debido a un límite de velocidad bajo. Si el límite de velocidad es demasiado bajo, el creador de la Campaign recibirá alertas en el panel y por correo electrónico.

{% alert tip %}
Establece un [límite de velocidad de mensajería del espacio de trabajo]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) para aplicar un límite de velocidad en todo un espacio de trabajo.
{% endalert %}

#### Ejemplo {#example}

Si estás intentando enviar 75 000 mensajes con un límite de velocidad de 10 000 por minuto, la entrega se distribuirá a lo largo de ocho minutos. Tu Campaign entregará no más de 10 000 mensajes en cada uno de los primeros siete minutos, y 5000 en el último minuto.

#### Número de envíos {#number-of-sends}

Ten en cuenta que los mensajes con límite de velocidad pueden no enviarse uniformemente a lo largo de cada minuto. Usando el ejemplo de un límite de velocidad de 10 000 por minuto, esto significa que Braze se asegura de que no se envíen más de 10 000 mensajes por minuto. Esto podría significar que un porcentaje mayor de los 10 000 mensajes se envía durante la primera mitad del minuto frente a la última mitad.

El límite de velocidad se aplica al inicio del intento de envío del mensaje. Cuando hay fluctuaciones en el tiempo que tarda en completarse el envío, el número de envíos completados puede superar ligeramente el límite de velocidad durante unos pocos minutos. Con el tiempo, el número de envíos por minuto se promediará a no más del límite de velocidad.

{% alert important %}
Ten cuidado con el retraso de mensajes urgentes con esta forma de limitación de velocidad en relación con el número total de usuarios en un Segment. Por ejemplo, si el Segment contiene 30 millones de usuarios pero establecemos el límite de velocidad en 10 000 por minuto, una gran parte de tu base de usuarios no recibirá el mensaje hasta el día siguiente.
{% endalert %}

#### Campaigns y Canvas multicanal {#multichannel-campaigns-and-canvases}

Al establecer un límite de velocidad de entrega para una Campaign multicanal o Canvas, puedes elegir establecer un límite de velocidad compartido o un límite basado en el canal.

Cuando una Campaign multicanal o Canvas utiliza un límite de velocidad compartido, esto significa que el número total de mensajes enviados por minuto desde la Campaign o Canvas no supera el límite de velocidad. Por ejemplo, si tu Canvas tiene un límite de velocidad de 500 000 por minuto y contiene pasos de mensaje de correo electrónico y SMS, Braze envía un total de 500 000 mensajes por minuto entre correo electrónico y SMS.

![Opción para limitar la velocidad a la que la Campaign envía, seleccionada con 500 000 mensajes por minuto.]({% image_buster /assets/img_archive/multichannel_campaigns_rate_limit.png %}){: style="max-width:50%;"}

Cuando una Campaign multicanal o Canvas utiliza límites de velocidad basados en canal, el límite de velocidad se aplicará a cada uno de tus canales seleccionados. Por ejemplo, puedes configurar tu Campaign o Canvas para enviar un máximo de 5000 webhooks y 2500 mensajes SMS por minuto en toda la Campaign o Canvas.

![Límites de velocidad separados para dos canales, webhook y SMS/MMS/RCS, con 5000 y 2500 mensajes por minuto respectivamente.]({% image_buster /assets/img_archive/channel_rate_limits.png %}){: style="max-width:70%;"}

##### Notificaciones push {#push-notifications}

Para Campaigns o Canvas con plataformas push (como Android, iOS, notificación push web o Kindle), puedes seleccionar **Notificaciones push** para aplicar un límite de velocidad compartido entre todas las plataformas push en tu Campaign o Canvas.

![Menú desplegable de canal con opciones para plataformas push y notificaciones push.]({% image_buster /assets/img_archive/push_notifications_rate_limit.png %}){: style="max-width:30%;"}

Si seleccionas un límite para notificaciones push, no puedes establecer límites de velocidad individuales por canal push. Del mismo modo, si seleccionas límites para canales push individuales, no puedes establecer límites compartidos de notificaciones push.

{% alert important %}
**Actualizaciones en la interfaz de límites de velocidad**<br>
Braze actualizó la interfaz de límites de velocidad para proporcionar más transparencia y control sobre cómo se aplican los límites de velocidad a Campaigns y Canvas multicanal.<br><br>

- **Campaigns y Canvas existentes:** todas las Campaigns y Canvas existentes se han migrado a esta interfaz. Su comportamiento de entrega sigue siendo el mismo. El panel muestra si la Campaign utiliza lógica compartida o por canal.<br>
- **Nuevas Campaigns y Canvas:** para todas las nuevas Campaigns y Canvas, hay un interruptor manual para elegir tu lógica de límite de velocidad preferida. Asegúrate de seleccionar el comportamiento de limitación de velocidad que se alinee con tu intención al configurar o actualizar un límite de velocidad de Campaign o Canvas.
{% endalert %}

##### Consideraciones sobre los límites de velocidad {#rate-limiting-considerations}

Algunas notas a tener en cuenta al configurar límites de velocidad y el comportamiento que debes esperar:

- Los envíos de SMS están sujetos a un límite de velocidad de 50 000 por grupo de suscripción. Algunos proveedores de SMS pueden aplicar otros límites.
- Los siguientes mensajes no serán limitados ni contados en el límite de velocidad:
    - Envíos de prueba
    - Grupos semilla
    - Content Cards configuradas para crearse "en la primera impresión" (esto se controlará por la tasa de impresiones de la aplicación. Consulta [Creación de tarjetas]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences) para obtener más información sobre las diferencias entre las opciones de creación de tarjetas.)
- Los límites de velocidad de entrega no son compatibles con lo siguiente:
    - Respuestas automáticas de SMS
    - Mensajes respaldados por SLA (como [correo transaccional]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email))
    - In-App Messages
    - Conmutadores de características
    - Banners

#### Límites de velocidad y reintentos de contenido conectado {#rate-limiting-and-connected-content-retries}

Cuando el [reintento de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries) está activado, Braze reintentará las llamadas fallidas respetando el límite de velocidad que hayas establecido para cada reenvío. Consideremos el escenario de enviar 75 000 mensajes con un límite de velocidad de 10 000 por minuto. Imagina que en el primer minuto, la llamada falla o es lenta y solo envía 4000 mensajes.

En lugar de intentar compensar el retraso y enviar los 6000 mensajes restantes en el segundo minuto o añadirlos a los 10 000 que ya están programados para enviarse, Braze moverá esos 6000 mensajes al "final de la cola" y añadirá un minuto, si es necesario, al total de minutos que tardaría en enviar tu mensaje.

| Minuto | Sin fallo | 6000 fallos en el minuto 1 |
|--------|-----------|----------------------------|
| 1      | 10 000    | 4000                       |
| 2      | 10 000    | 10 000                     |
| 3      | 10 000    | 10 000                     |
| 4      | 10 000    | 10 000                     |
| 5      | 10 000    | 10 000                     |
| 6      | 10 000    | 10 000                     |
| 7      | 10 000    | 10 000                     |
| 8      | 5000      | 10 000                     |
| 9      | 0         | 6000                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Límites de velocidad y reintentos de contenido conectado" }

Las solicitudes de contenido conectado no tienen límites de velocidad independientes y seguirán el límite de velocidad del webhook. Esto significa que si hay una llamada de contenido conectado a un endpoint único por webhook, esperarías 5000 webhooks y también 5000 llamadas de contenido conectado por minuto. Ten en cuenta que el almacenamiento en caché puede afectar esto y reducir el número de llamadas de contenido conectado. Además, los reintentos pueden aumentar las llamadas de contenido conectado, por lo que recomendamos verificar que el endpoint de contenido conectado pueda manejar cierta fluctuación.

{% alert note %}
**Los límites de velocidad son límites de velocidad y no definen una velocidad de envío exacta.** Generalmente, los mensajes se distribuyen uniformemente dentro de cualquier minuto dado, y en la gran mayoría de los casos, se envían al límite configurado o muy cerca de él. Esto no siempre es así; por ejemplo, cuando los mensajes son muy grandes (como correos electrónicos con muchos Content Blocks, etiquetas de contenido conectado o etiquetas de elementos de catálogo), o cuando hay muchos abortos de Liquid (los mensajes abortados aún consumen un espacio y pueden reducir las tasas de envío efectivas).<br><br>
En la práctica, la tasa de envío sostenida (mensajes completados por minuto) puede ser inferior al límite de velocidad configurado debido a reintentos, variabilidad de la red, latencia del endpoint de destino y suavización por minuto. Si observas de forma consistente un rendimiento significativamente inferior al esperado, verifica los tiempos de respuesta del contenido conectado, las tasas de error (como `429`) y el comportamiento de reintentos.
{% endalert %}

## Acerca de la limitación de frecuencia {#about-frequency-capping}

A medida que tu base de usuarios sigue creciendo y tu mensajería se amplía para incluir Campaigns de ciclo de vida, desencadenadas, transaccionales y de conversión, es importante evitar que tus notificaciones parezcan correo no deseado o resulten molestas. Al proporcionarte un mayor control sobre la experiencia de tus usuarios, la limitación de frecuencia te permite crear las Campaigns que desees sin saturar a tu audiencia.

### Usa los límites de velocidad y la limitación de frecuencia juntos {#use-rate-limiting-and-frequency-capping-together}

Cuando habilitas tanto el límite de velocidad como la limitación de frecuencia en una Campaign, Braze los aplica en el siguiente orden:

1. **El límite de velocidad** se aplica primero para seleccionar el grupo inicial de usuarios que pueden recibir mensajes.
2. **La limitación de frecuencia** se aplica en segundo lugar para filtrar usuarios de ese grupo.
3. **Los mensajes se envían** a los usuarios restantes.

{% alert important %}
Si muchos usuarios de tu grupo con límite de velocidad están limitados por frecuencia, es posible que envíes menos mensajes que el valor de tu límite de velocidad. Braze no rellena con usuarios adicionales del límite de velocidad una vez que la limitación de frecuencia los elimina del grupo de envío.
{% endalert %}

#### Ejemplo

Con un límite de velocidad de 500 usuarios y la limitación de frecuencia habilitada, si 200 de esos 500 usuarios con límite de velocidad están limitados por frecuencia, solo se envían 300 mensajes, no 500.

#### Recomendaciones {#recommendations}

Si necesitas llegar a un número específico de usuarios al usar ambas características juntas, considera los siguientes enfoques:

- **Aumenta tu límite de velocidad:** para tener en cuenta a los usuarios que están limitados por frecuencia. Por ejemplo, si deseas llegar a 500 usuarios pero esperas que algunos estén limitados por frecuencia, establece tu límite de velocidad más alto (como 1000 usuarios).
- **Usa solo los límites de velocidad:** si tu objetivo es controlar el volumen de mensajes enviados por Campaign.
- **Contacta a tu administrador de éxito de cliente:** para obtener ayuda en el diseño de una estrategia de mensajería sólida que equilibre las necesidades del negocio y las consideraciones técnicas.

### Resumen de la característica {#freq-cap-feat-over}

La limitación de frecuencia se aplica a nivel de envío de Campaign o componente de Canvas y se puede configurar para cada espacio de trabajo desde **Configuración** > **Reglas de limitación de frecuencia**.

De forma predeterminada, la limitación de frecuencia está activada cuando se crean nuevas Campaigns. Desde aquí, puedes elegir lo siguiente:

- El canal de mensajería que deseas limitar: push, correo electrónico, SMS, webhook, WhatsApp, LINE o cualquiera de esos canales.
- Cuántas veces cada usuario debe recibir una Campaign o componente de Canvas enviado desde un canal dentro de un período de tiempo determinado.
- Cuántas veces cada usuario debe recibir una Campaign o componente de Canvas enviado por [etiqueta](#frequency-capping-by-tag) dentro de un período de tiempo determinado.

Este período de tiempo puede medirse en minutos, días o semanas (siete días), con una duración máxima de 30 días.

Cada línea de limitación de frecuencia está conectada mediante el operador `AND`, y puedes agregar hasta 10 reglas por espacio de trabajo. Puedes incluir múltiples límites para los mismos tipos de mensajes. Por ejemplo, puedes limitar a los usuarios a no más de una notificación push por día y no más de tres notificaciones push por semana. Ten en cuenta que los mensajes abortados no cuentan para la limitación de frecuencia.

![Sección de limitación de frecuencia con listas de Campaigns y Canvas a los que las reglas se aplicarán y no se aplicarán.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %}){: style="max-width:90%;"}

#### Comportamiento cuando los usuarios están limitados por frecuencia o se aborta un mensaje en un paso en Canvas {#behavior-when-users-are-frequency-capped-or-a-message-is-aborted-on-a-canvas-step}

La limitación de frecuencia global por sí sola no hace salir a los usuarios de un Canvas. En los [pasos de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step), los usuarios siguen avanzando cuando un mensaje no se envía debido a la limitación de frecuencia global, de acuerdo con [cómo avanzan los usuarios]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance) a través del paso. Lo mismo ocurre cuando un mensaje se aborta (por ejemplo, por una condición de aborto de Liquid): el usuario continúa a través del Canvas como si el mensaje se hubiera enviado.

Esto es independiente de las **Validaciones de entrega** en un paso de mensaje. Si un usuario no cumple con los criterios de validación de entrega en el momento del envío, puede salir del Canvas en ese paso.

### Reglas de entrega {#delivery-rules}

Puede haber algunas Campaigns, como los mensajes transaccionales, que quieres que siempre lleguen al usuario, incluso si ya han alcanzado su límite de frecuencia. Por ejemplo, una aplicación de entregas puede querer enviar un correo electrónico o una notificación push cuando se entrega un artículo, independientemente de cuántas Campaigns haya recibido el usuario.

Si quieres que una Campaign en particular anule las reglas de limitación de frecuencia, puedes configurar esto en el panel de Braze al programar la entrega de esa Campaign alternando **Limitación de frecuencia** a **DESACTIVADO**.

Después de esto, se te preguntará si aún deseas que esta Campaign cuente para tu limitación de frecuencia. Los mensajes que cuentan para la limitación de frecuencia se incluyen en los cálculos del filtro de canal inteligente.

Al enviar [Campaigns de API]({{site.baseurl}}/api/endpoints/messaging), que a menudo son transaccionales, tendrás la capacidad de especificar que una Campaign debe ignorar las reglas de limitación de frecuencia configurando `override_frequency_capping` a `true` en la solicitud de API.

De forma predeterminada, las nuevas Campaigns y Canvas que no obedecen los límites de frecuencia tampoco cuentan para ellos. Esto es configurable para cada Campaign y Canvas.

{% alert note %}
Este comportamiento cambia el comportamiento predeterminado cuando desactivas la limitación de frecuencia para una Campaign o Canvas. Los cambios son retrocompatibles y no afectan a los mensajes que están actualmente en vivo.
{% endalert %}

![Sección de controles de entrega con la limitación de frecuencia activada.]({% image_buster /assets/img_archive/frequencycappingupdate.png %}){: style="max-width:90%;"}

#### Cómo cuentan los envíos para los límites {#how-sends-count-toward-caps}

La limitación de frecuencia se aplica por despacho: cada vez que Braze envía una Campaign o componente de Canvas a un usuario cuenta para tus límites, no cada variante de mensaje o plataforma dentro de ese envío. Por ejemplo, si los usuarios están limitados a cinco Campaigns de push por semana, no reciben ninguna Campaign de push después del quinto despacho hasta que el límite se restablezca.

##### Envíos multicanal {#multichannel-sends}

Cuando un solo despacho utiliza múltiples canales, ese despacho cuenta como máximo una vez por cada regla de limitación de frecuencia que se aplique. Por ejemplo, si creas una Campaign multicanal que envía correo electrónico, push de iOS y push de Android en una sola entrega y tu espacio de trabajo tiene reglas para push y correo electrónico, y una regla que se aplica a todos los canales, esa entrega cuenta una vez para la regla de push, una vez para la regla de correo electrónico y una vez para la regla de todos los canales; no cuenta una vez por plataforma de push o por mensaje dentro del envío. Si los usuarios están limitados a una Campaign de push y una de correo electrónico por día y reciben esta Campaign multicanal, no son elegibles para Campaigns de push o correo electrónico adicionales durante el resto del día, a menos que una Campaign ignore las reglas de limitación de frecuencia.

In-App Messages y Content Cards no se cuentan como ni para los límites de Campaigns o componentes de Canvas de ningún tipo.

##### Notificaciones push con múltiples dispositivos {#push-notifications-with-multiple-devices}

Para las Campaigns de push, la limitación de frecuencia cuenta a nivel de Campaign o componente de Canvas, no por dispositivo individual. Si un perfil de usuario tiene varios dispositivos registrados para push (por ejemplo, un iPhone y un iPad), un límite de frecuencia a nivel de Campaign cuenta eso como un envío, independientemente de cuántos dispositivos reciban la notificación. Esto es similar a cómo una Campaign recurrente con cadencia diaria cuenta como un envío por día, incluso si se repite varias veces a lo largo de la semana.

{% alert important %}
La limitación de frecuencia global se programa según la zona horaria del usuario y se calcula por días calendario, no por períodos de 24 horas. Por ejemplo, si configuras una regla de limitación de frecuencia de enviar no más de una Campaign por día, un usuario puede recibir un mensaje a las 11 pm en su zona horaria local y sería elegible para recibir otro mensaje una hora después.
{% endalert %}

#### Ejemplos {#use-cases}

{% tabs %}
{% tab Ejemplo 1 %}

Supongamos que configuras una regla de limitación de frecuencia para que tus usuarios no reciban más de tres Campaigns de notificación push o pasos en Canvas por semana de todas las Campaigns o pasos en Canvas.

Si tu usuario está programado para recibir tres notificaciones push, dos In-App Messages y una Content Card esta semana, recibirá todos esos mensajes.

{% endtab %}
{% tab Ejemplo 2 %}

Este escenario utiliza una regla de limitación de frecuencia para que los usuarios no reciban más de dos Campaigns de notificación push o pasos en Canvas por semana de todas las Campaigns o pasos en Canvas.

**Cuando ocurre el siguiente escenario:**

- Un usuario desencadena la misma Campaign `Campaign ABC` tres veces en el transcurso de una semana.
- Este usuario desencadena `Campaign ABC` una vez el lunes, una vez el miércoles y una vez el jueves.

![Sección de limitación de frecuencia con la regla de enviar no más de 2 Campaigns de notificación push o pasos en Canvas de todas las Campaigns o pasos en Canvas a un usuario cada semana.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Entonces, el comportamiento esperado es que:**

- Este usuario recibirá los envíos de Campaign desencadenados el lunes y el miércoles.
- Este usuario no recibirá el tercer envío de Campaign el jueves porque ya ha recibido dos envíos de Campaign de push esa semana.

{% endtab %}
{% endtabs %}

### Limitación de frecuencia por etiqueta {#frequency-capping-by-tag}

Las [reglas de limitación de frecuencia](#delivery-rules) se pueden aplicar a los espacios de trabajo utilizando etiquetas específicas que hayas aplicado a tus Campaigns y Canvas, lo que te permite basar esencialmente tu limitación de frecuencia en grupos con nombres personalizados.

Con la limitación de frecuencia por etiqueta, las reglas se pueden establecer en las etiquetas principales y anidadas, por lo que Braze tendrá en cuenta todas las etiquetas. Por ejemplo, si has seleccionado usar la etiqueta principal A como limitación de frecuencia, también incluiremos información de todas las etiquetas anidadas (por ejemplo, las etiquetas B y C) al determinar el límite.

También puedes combinar la limitación de frecuencia regular con la limitación de frecuencia por etiquetas. Considera las siguientes reglas:

1. No más de tres Campaigns de notificación push o componentes de Canvas por semana de todas las Campaigns y pasos en Canvas. <br>**Y**
2. No más de dos Campaigns de notificación push o componentes de Canvas por semana con la etiqueta `promotional`.

![Sección de limitación de frecuencia con dos reglas que limitan cuántas Campaigns de notificación push o Canvas se pueden enviar a un usuario cada semana.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Como resultado, tus usuarios no recibirán más de tres envíos de Campaign por semana de todas las Campaigns y pasos en Canvas, y no más de dos Campaigns de notificación push o componentes de Canvas con la etiqueta `promotional`.

{% alert important %}
Los Canvas se etiquetan a nivel de Canvas, a diferencia del etiquetado por componente. Así que cada componente de Canvas heredará todas las etiquetas a nivel de Canvas.
{% endalert %}

#### Reglas en conflicto {#conflicting-rules}

Cuando las reglas entran en conflicto, se aplica la regla de limitación de frecuencia más restrictiva y aplicable a tus usuarios. Por ejemplo, supongamos que tienes las siguientes reglas:

1. No más de una Campaign de notificación push o componente de Canvas por semana de todas las Campaigns y componentes de Canvas. <br>**Y**
2. No más de tres Campaigns de notificación push o componentes de Canvas por semana con la etiqueta `promotional`.

![Sección de limitación de frecuencia con reglas en conflicto para limitar cuántas Campaigns de notificación push o pasos en Canvas se envían a un usuario cada semana.]({% image_buster /assets/img/global_rules.png %} "global rules")

En este ejemplo, tu usuario no recibirá más de una Campaign de notificación push o componente de Canvas con la etiqueta "promotional" en una semana determinada, porque has especificado que los usuarios no deben recibir más de una Campaign de notificación push o componente de Canvas de todas las Campaigns y componentes de Canvas. En otras palabras, la regla de frecuencia más restrictiva aplicable es la regla que se aplicará a un usuario determinado.

#### Recuento de etiquetas {#tag-count}

Las reglas de limitación de frecuencia por etiqueta se calculan en el momento en que se envía un mensaje. Esto significa que la limitación de frecuencia por etiqueta solo cuenta las etiquetas que están actualmente en las Campaigns o Canvas que un usuario recibió en el pasado. No cuenta las etiquetas que estaban en las Campaigns o Canvas en el momento en que se enviaron, pero que desde entonces se han eliminado. Sí cuenta si una etiqueta se agrega posteriormente a un mensaje que un usuario recibió en el pasado, pero antes de que se envíe el mensaje etiquetado más reciente.

##### Ejemplo {#use-case}

Considera las siguientes Campaigns y la regla de limitación de frecuencia por etiqueta:

**Campaigns**:

- **Campaign A** es una Campaign de push etiquetada como `promotional`. Está programada para enviarse a las 9 am del lunes.
- **Campaign B** es una Campaign de push etiquetada como `promotional`. Está programada para enviarse a las 9 am del miércoles.

**Regla de limitación de frecuencia por etiqueta:**

- Tu usuario no debe recibir más de una Campaign de notificación push por semana con la etiqueta `promotional`.<br><br>

| Acción | Resultado |
|---|---|
| La etiqueta `promotional` se elimina de **Campaign A** después de que tu usuario recibió el mensaje, pero antes de que **Campaign B se haya enviado.** | Tu usuario recibe **Campaign B**. |
| La etiqueta `promotional` se elimina por error de **Campaign A** después de que tu usuario recibió el mensaje. <br> La etiqueta se agrega de nuevo a **Campaign A** el martes, antes de que **Campaign B** se envíe. | Tu usuario no recibe **Campaign B**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ejemplo" }

#### Envío a gran escala {#sending-at-large-scales}

Las reglas de limitación de frecuencia por etiqueta podrían no aplicarse correctamente a gran escala, como 100 mensajes por canal de Campaigns o componentes de Canvas.

Por ejemplo, si tu regla de limitación de frecuencia por etiqueta es:

> No más de dos Campaigns de correo electrónico o componentes de Canvas con la etiqueta `Promotional` a un usuario cada semana.

Y envías al usuario más de 100 correos electrónicos de Campaigns y pasos en Canvas con la limitación de frecuencia activada durante el transcurso de una semana, es posible que se envíen más de dos correos electrónicos al usuario.

Dado que 100 mensajes por canal son más mensajes de los que la mayoría de las marcas envían a sus usuarios, es poco probable que te veas afectado por esta limitación. Para evitar esta limitación, puedes establecer un límite para el número máximo de correos electrónicos que deseas que reciban tus usuarios durante el transcurso de una semana.

Por ejemplo, podrías configurar la siguiente regla:

> No más de tres Campaigns de correo electrónico o componentes de Canvas por semana de todas las Campaigns y pasos en Canvas.

Esta regla determina que ningún usuario reciba más de 100 correos electrónicos por semana, ya que, como máximo, los usuarios reciben tres correos electrónicos por semana de Campaigns o componentes de Canvas con la limitación de frecuencia activada.

## Preguntas frecuentes {#frequently-asked-questions}

### Si cambio la limitación de envío en un Canvas activo, ¿afecta a los usuarios que ya están en el Canvas? {#if-i-change-a-send-throttle-on-an-active-canvas-does-it-affect-users-already-in-the-canvas}

Sí, cuando aumentas o reduces un límite de velocidad de Canvas, el límite actualizado entra en vigor para los nuevos mensajes en aproximadamente 30 segundos después del cambio debido al almacenamiento en caché.

### ¿La limitación de frecuencia hace que los usuarios salgan de un Canvas? {#does-frequency-capping-cause-users-to-exit-a-canvas}

No. Si un usuario de Canvas tiene limitación de frecuencia debido a la configuración global de limitación de frecuencia, el usuario avanza inmediatamente al siguiente paso en Canvas. El usuario **no** sale del Canvas a causa de la limitación de frecuencia.

### ¿Cómo puedo identificar a los usuarios que fueron limitados por frecuencia en un Canvas? {#how-can-i-identify-users-who-were-frequency-capped-in-a-canvas}

Los usuarios que tienen limitación de frecuencia no generan un evento de envío para ese paso. Para identificar a estos usuarios, puedes usar [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) para rastrear los eventos de limitación de frecuencia de mensajes. Como alternativa, puedes crear una [Segment Extension]({{site.baseurl}}/user_guide/audience/segments/segment_extension) para analizar a los usuarios que entraron en el Canvas pero no recibieron el mensaje esperado.

### ¿Por qué el panel muestra un error de límite de velocidad para mi Campaign? {#why-does-the-dashboard-show-a-rate-limit-error-for-my-campaign}

Esto suele significar que el [límite de velocidad de entrega](#delivery-speed-rate-limiting) de la Campaign está configurado demasiado bajo para el tamaño de la audiencia, por lo que completar el envío llevaría más tiempo del permitido y Braze muestra una advertencia. Aumenta el límite de velocidad de entrega, reduce la audiencia o usa **Limitar volumen de envío** para que cada ocurrencia programada termine dentro de la ventana de envío permitida. También puedes establecer un [límite de velocidad de mensajería del espacio de trabajo]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) para aplicar un tope en todas las Campaigns.

**Limitar volumen de envío** controla cuántos usuarios son elegibles para un envío, no cuántos mensajes envía Braze por minuto. Solo un límite de velocidad de entrega establece el rendimiento por minuto.

Si ya estás en el límite de velocidad de entrega máximo disponible para tu empresa, contacta a tu administrador de éxito de cliente para solicitar un aumento.

### ¿Qué significa "Enviado" para la limitación de frecuencia? {#what-does-sent-mean-for-frequency-capping}

En análisis y limitación de frecuencia, _Enviado_ se refiere al momento en que Braze despacha el mensaje (el envío se registra), no a la entrega final garantizada al dispositivo o buzón de entrada. La limitación de frecuencia y los conteos de envío usan estos eventos de envío registrados, que pueden diferir de las métricas de "entregado" en destino.

### ¿Por qué estoy viendo rebotes o aplazamientos de correo electrónico? {#why-am-i-seeing-email-bounces-or-deferrals}

Los mensajes de rebote y aplazamiento de correo electrónico usan muchos códigos diferentes y texto específico del proveedor. No trates un código en particular como señal de un problema de límite de velocidad, ya que la causa depende de tu contexto de envío y los comentarios del proveedor de buzón de correo.

Si los mensajes se aplazan temporalmente, enviar menos puede ayudar a corto plazo. Usa un [límite de velocidad de entrega](#delivery-speed-rate-limiting), **Limitar volumen de envío**, o ambos.

Para una solución a largo plazo, trabaja con un experto en capacidad de entrega para revisar tus datos de rebotes y aplazamientos.