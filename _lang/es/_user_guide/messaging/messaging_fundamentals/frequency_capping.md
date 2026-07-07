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

## Acerca del límite de velocidad {#about-rate-limiting}

Braze te permite controlar la presión de marketing limitando la velocidad de tus campañas, regulando la cantidad de tráfico saliente de tu plataforma. Puedes implementar dos tipos diferentes de límite de velocidad para tus campañas:

1. [Límite de velocidad centrado en el usuario:](#user-centric-rate-limiting) se centra en proporcionar la mejor experiencia para el usuario.
2. [Límite de velocidad de entrega:](#delivery-speed-rate-limiting) tiene en cuenta el ancho de banda de tus servidores.

Braze no admite un límite de velocidad por segundo. Braze intenta distribuir uniformemente los envíos de mensajes a lo largo del minuto, pero no puede garantizarlo. Por ejemplo, si tienes una campaña con un límite de velocidad de 5000 mensajes por minuto, intentamos distribuir las 5000 solicitudes de manera uniforme a lo largo del minuto (aproximadamente 84 mensajes por segundo), pero puede haber alguna variación en la tasa por segundo.

### Límite de velocidad centrado en el usuario {#user-centric-rate-limiting}

A medida que creas más segmentos, habrá casos en los que la pertenencia a esos segmentos se superponga. Si estás enviando campañas a esos segmentos, querrás asegurarte de que no estás enviando mensajes a tus usuarios con demasiada frecuencia. Si un usuario recibe demasiados mensajes en un período corto de tiempo, se sentirá abrumado y desactivará las notificaciones push o desinstalará tu aplicación.

#### Filtros de segmento relevantes {#relevant-segment-filters}

Braze proporciona los siguientes filtros para ayudarte a limitar la velocidad a la que tus usuarios reciben mensajes:

- Last Engaged With Message
- Last Received Any Message
- Last Received Push
- Last Received Email
- Last Received SMS

#### Implementación de filtros {#implementing-filters}

Supongamos que hemos creado un segmento llamado "Escaparate de filtros de reorientación" con un filtro "Última vez que usó la aplicación hace más de 7 días" para dirigirnos a los usuarios. Este sería un segmento estándar de reactivación de la interacción.

Si tienes otros segmentos más específicos que reciben notificaciones recientemente, es posible que no quieras que tus usuarios sean objetivo de campañas más genéricas dirigidas a este segmento. Al añadir el filtro "Last Received Push" a este segmento, el usuario se ha asegurado de que, si ha recibido otra notificación en las últimas 24 horas, saldrá de este segmento durante las próximas 24 horas. Si aún cumple los demás criterios del segmento 24 horas después y no ha recibido más notificaciones, volverá a entrar en el segmento.

![Un segmento llamado "Escaparate de filtros de reorientación" con el grupo de filtros "Última vez que usó la aplicación hace más de 7 días".]({% image_buster /assets/img_archive/rate_limit_daily.png %}){: style="max-width:80%;"}

Añadir este filtro a todos los segmentos objetivo de campañas haría que tus usuarios recibieran un máximo de un push cada 24 horas. Entonces podrías priorizar tu mensajería asegurándote de que tus mensajes más importantes se entreguen antes que los menos importantes.

#### Establecer un límite máximo de usuarios {#setting-a-maximum-user-cap}

En el paso **Target Audiences** del compositor de tu campaña, también puedes limitar el número total de usuarios que recibirán tu mensaje. Esto sirve como una verificación independiente de los filtros de tu campaña.

![Resumen de audiencia con una casilla seleccionada para limitar el número de personas que reciben la campaña.]({% image_buster /assets/img_archive/total_limit.png %}){: style="max-width:50%;"}

Al seleccionar el límite máximo de usuarios, puedes limitar el volumen de mensajes enviados por canal o globalmente en todos los tipos de mensajes. Braze no envía mensajes a los usuarios asignados a grupos de control, por lo que no cuentan para el límite.

{% alert note %}
El límite máximo de usuarios limita el número de usuarios despachados, no el número de mensajes enviados con éxito. Dado que los mensajes abortados cuentan para este límite, el número real de mensajes enviados puede ser inferior al límite configurado. Por ejemplo, si estableces un límite de 10 000 y se abortan 2000 mensajes debido a lógica Liquid u otras condiciones, solo se enviarán 8000 mensajes.
{% endalert %}

##### Límite máximo de usuarios con optimizaciones {#maximum-user-cap-with-optimizations}

Si estás utilizando una optimización como variante ganadora o variante personalizada, la campaña constará de dos envíos: el experimento inicial y el envío final.

Para configurar un límite máximo de usuarios en este escenario, selecciona **Limit the number of people who will receive this campaign**, luego selecciona **In total this campaign should** e introduce un límite de audiencia. Tu límite de audiencia se dividirá según los porcentajes mostrados en el panel **A/B Testing**.

Si seleccionas **Every time the campaign is scheduled**, esas dos fases se limitarán por separado al número establecido. Esto normalmente no es deseable.

#### Establecer un límite máximo de impresiones en campañas {#setting-a-maximum-impression-cap-on-campaigns}

Para los mensajes dentro de la aplicación, puedes controlar la presión de marketing estableciendo un número máximo de impresiones que se mostrarán a tu base de usuarios, después del cual Braze dejará de enviar más mensajes a tus usuarios. Sin embargo, es importante tener en cuenta que este límite no es exacto.

Las reglas de mensajes dentro de la aplicación se envían a una aplicación al inicio de la sesión, lo que significa que Braze puede enviar un mensaje al usuario antes de que se alcance el límite, pero para cuando el usuario activa el mensaje, el límite ya se ha alcanzado. En esta situación, el dispositivo seguirá mostrando el mensaje.

Por ejemplo, supongamos que tienes un juego con un mensaje dentro de la aplicación que se activa cuando un usuario supera un nivel, y lo limitas a 100 impresiones. Ha habido 99 impresiones hasta ahora. Alice y Bob abren el juego, y Braze indica a sus dispositivos que son elegibles para recibir el mensaje cuando superen un nivel. Alice supera un nivel primero y recibe el mensaje. Bob supera el nivel después, pero como su dispositivo no se ha comunicado con los servidores de Braze desde que comenzó su sesión, su dispositivo no sabe que el mensaje ha alcanzado su límite, y también recibe el mensaje. Sin embargo, cuando se ha alcanzado un límite de impresiones, la próxima vez que cualquier dispositivo solicite la lista de mensajes dentro de la aplicación elegibles, el sistema no enviará ese mensaje y lo eliminará de ese dispositivo.

### Límite de velocidad y pruebas A/B {#rate-limiting-and-ab-testing}

Al usar el límite de velocidad con una prueba A/B, el límite de velocidad no se aplica al grupo de control de la misma manera que al grupo de prueba, lo cual es una fuente potencial de sesgo temporal. Para evitar este sesgo, utiliza ventanas de conversión apropiadas.

### Límite de velocidad de entrega {#delivery-speed-rate-limiting}

Si anticipas que campañas grandes provocarán un pico en la actividad de los usuarios y sobrecargarán tus servidores, puedes especificar un límite de velocidad por minuto para el envío de mensajes, lo que significa que Braze no enviará más de tu configuración de límite de velocidad en un minuto.

Al dirigirte a usuarios durante la creación de una campaña, puedes navegar a **Target Audiences** (para Campaigns) o **Send Settings** (para Canvas) para seleccionar un límite de velocidad (en varios incrementos desde tan bajo como 10 hasta tan alto como 500 000 mensajes por minuto).

Ten en cuenta que las campañas sin límite de velocidad pueden superar estos límites de entrega. Sin embargo, ten en cuenta que los mensajes se abortarán si se retrasan 72 horas o más debido a un límite de velocidad bajo. Si el límite de velocidad es demasiado bajo, el creador de la campaña recibirá alertas en el dashboard y por correo electrónico.

{% alert tip %}
Establece un [límite de velocidad de mensajería del espacio de trabajo]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) para aplicar un límite de velocidad en todo un espacio de trabajo.
{% endalert %}

#### Ejemplo {#example}

Si intentas enviar 75 000 mensajes con un límite de velocidad de 10 000 por minuto, la entrega se distribuirá a lo largo de ocho minutos. Tu campaña entregará no más de 10 000 mensajes en cada uno de los primeros siete minutos, y 5000 en el último minuto.

#### Número de envíos {#number-of-sends}

Ten en cuenta que los mensajes con límite de velocidad pueden no enviarse de manera uniforme a lo largo de cada minuto. Usando el ejemplo de un límite de velocidad de 10 000 por minuto, esto significa que Braze se asegura de que no se envíen más de 10 000 mensajes por minuto. Esto podría significar que un porcentaje mayor de los 10 000 mensajes se envía en la primera mitad del minuto en comparación con la segunda mitad.

El límite de velocidad se aplica al inicio del intento de envío del mensaje. Cuando hay fluctuaciones en el tiempo que tarda en completarse el envío, el número de envíos completados puede superar ligeramente el límite de velocidad durante unos minutos. Con el tiempo, el número de envíos por minuto se promediará a no más del límite de velocidad.

{% alert important %}
Ten cuidado de no retrasar mensajes sensibles al tiempo con esta forma de límite de velocidad en relación con el número total de usuarios en un segmento. Por ejemplo, si el segmento contiene 30 millones de usuarios pero establecemos el límite de velocidad en 10 000 por minuto, una gran parte de tu base de usuarios no recibirá el mensaje hasta el día siguiente.
{% endalert %}

#### Campañas multicanal y Canvas {#multichannel-campaigns-and-canvases}

Al establecer un límite de velocidad de entrega para una campaña multicanal o Canvas, puedes elegir establecer un límite de velocidad compartido o un límite basado en canal.

Cuando una campaña multicanal o Canvas usa un límite de velocidad compartido, esto significa que el número total de mensajes enviados por minuto desde la campaña o Canvas no supera el límite de velocidad. Por ejemplo, si tu Canvas tiene un límite de velocidad de 500 000 por minuto y contiene pasos de mensaje de correo electrónico y SMS, Braze envía un total de 500 000 mensajes por minuto entre correo electrónico y SMS.

![La opción de limitar la velocidad a la que la campaña envía, seleccionada con 500 000 mensajes por minuto.]({% image_buster /assets/img_archive/multichannel_campaigns_rate_limit.png %}){: style="max-width:50%;"}

Cuando una campaña multicanal o Canvas usa un límite de velocidad basado en canal, el límite de velocidad se aplicará a cada uno de tus canales seleccionados. Por ejemplo, puedes configurar tu campaña o Canvas para enviar un máximo de 5000 webhooks y 2500 mensajes SMS por minuto en toda la campaña o Canvas.

![Límites de velocidad separados para dos canales, webhook y SMS/MMS/RCS, con 5000 y 2500 mensajes por minuto respectivamente.]({% image_buster /assets/img_archive/channel_rate_limits.png %}){: style="max-width:70%;"}

##### Notificaciones push {#push-notifications}

Para campañas o Canvas con plataformas push (como Android, iOS, notificación push web o Kindle), puedes seleccionar **Push notifications** para aplicar un límite de velocidad compartido entre todas las plataformas push en tu campaña o Canvas.

![El menú desplegable de canal con opciones para plataformas push y notificaciones push.]({% image_buster /assets/img_archive/push_notifications_rate_limit.png %}){: style="max-width:30%;"}

Si seleccionas un límite para notificaciones push, no puedes establecer límites de velocidad individuales por canal push. Del mismo modo, si seleccionas límites para canales push individuales, no puedes establecer límites compartidos de notificaciones push.

{% alert important %}
**Actualizaciones de la interfaz de límite de velocidad**<br>
Braze actualizó la interfaz de límite de velocidad para proporcionar más transparencia y control sobre cómo se aplican los límites de velocidad a las campañas multicanal y Canvas.<br><br>

- **Campañas y Canvas existentes:** todas las campañas y Canvas existentes se han migrado a esta interfaz. Su comportamiento de entrega sigue siendo el mismo. El dashboard muestra si la campaña usa lógica compartida o por canal.<br>
- **Nuevas campañas y Canvas:** para todas las nuevas campañas y Canvas, hay un interruptor manual para elegir tu lógica de límite de velocidad preferida. Asegúrate de seleccionar el comportamiento de límite de velocidad que se alinee con tu comportamiento previsto al establecer o actualizar un límite de velocidad de campaña o Canvas.
{% endalert %}

##### Consideraciones sobre el límite de velocidad {#rate-limiting-considerations}

Algunas notas a tener en cuenta al configurar límites de velocidad y qué comportamiento debes esperar:

- Los envíos de SMS están sujetos a un límite de velocidad de 50 000 por grupo de suscripción. Algunos proveedores de SMS pueden aplicar otros límites.
- Los siguientes mensajes no serán limitados ni contarán para el límite de velocidad:
    - Envíos de prueba
    - Grupos semilla
    - Content Cards configuradas para crearse "en la primera impresión" (esto será controlado por la tasa de impresiones de la aplicación. Consulta [Creación de tarjetas]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences) para más información sobre las diferencias entre las opciones de creación de tarjetas.)
- Los límites de velocidad de entrega no son compatibles con lo siguiente:
    - Respuestas automáticas de SMS
    - Mensajes respaldados por SLA (como [correo electrónico transaccional]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email))
    - Mensajes dentro de la aplicación
    - Conmutadores de características
    - Banners

#### Límite de velocidad y reintentos de contenido conectado {#rate-limiting-and-connected-content-retries}

Cuando el [reintento de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries) está activado, Braze reintentará las llamadas fallidas respetando el límite de velocidad que hayas establecido para cada reenvío. Consideremos el escenario de enviar 75 000 mensajes con un límite de velocidad de 10 000 por minuto. Imagina que en el primer minuto, la llamada falla o es lenta y solo envía 4000 mensajes.

En lugar de intentar compensar el retraso y enviar los 6000 mensajes restantes en el segundo minuto o añadirlos a los 10 000 que ya están programados para enviar, Braze moverá esos 6000 mensajes al "final de la cola" y añadirá un minuto, si es necesario, al total de minutos que tardaría en enviar tu mensaje.

| Minuto | Sin fallo | 6000 fallos en el minuto 1 |
|--------|------------|---------------------------|
| 1      | 10 000     | 4000                     |
| 2      | 10 000     | 10 000                    |
| 3      | 10 000     | 10 000                    |
| 4      | 10 000     | 10 000                    |
| 5      | 10 000     | 10 000                    |
| 6      | 10 000     | 10 000                    |
| 7      | 10 000     | 10 000                    |
| 8      | 5000      | 10 000                    |
| 9      | 0          | 6000                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Límite de velocidad y reintentos de contenido conectado" }

Las solicitudes de contenido conectado no tienen un límite de velocidad independiente y seguirán el límite de velocidad del webhook. Esto significa que si hay una llamada de contenido conectado a un punto de conexión único por webhook, esperarías 5000 webhooks y también 5000 llamadas de contenido conectado por minuto. Ten en cuenta que el almacenamiento en caché puede afectar esto y reducir el número de llamadas de contenido conectado. Además, los reintentos pueden aumentar las llamadas de contenido conectado, por lo que recomendamos verificar que el punto de conexión de contenido conectado pueda manejar cierta fluctuación aquí.

{% alert note %}
**Los límites de velocidad son límites de velocidad y no definen una velocidad de envío exacta.** Generalmente, los mensajes se distribuyen uniformemente dentro de cualquier minuto dado, y en la gran mayoría de los casos, se envían al límite configurado o muy cerca de él. Esto no siempre es así, por ejemplo, cuando los mensajes son muy grandes (como correos electrónicos con muchos Content Blocks, etiquetas de contenido conectado o etiquetas de elementos de catálogo), o cuando hay muchos abortos de Liquid (los mensajes abortados aún consumen un espacio y pueden reducir las tasas de envío efectivas).<br><br>
En la práctica, la tasa de envío sostenida (mensajes completados por minuto) puede ser inferior al límite de velocidad configurado debido a reintentos, variabilidad de la red, latencia del punto de conexión posterior y suavizado por minuto. Si ves consistentemente un rendimiento significativamente inferior al esperado, verifica los tiempos de respuesta del contenido conectado, las tasas de error (como `429`) y el comportamiento de reintentos.
{% endalert %}

## Acerca de la limitación de frecuencia {#about-frequency-capping}

A medida que tu base de usuarios continúa creciendo y tu mensajería se escala para incluir campañas de ciclo de vida, activadas, transaccionales y de conversión, es importante evitar que tus notificaciones parezcan correo no deseado o disruptivas. Al proporcionar un mayor control sobre la experiencia de tus usuarios, la limitación de frecuencia te permite crear las campañas que desees sin abrumar a tu audiencia.

### Usar el límite de velocidad y la limitación de frecuencia juntos {#use-rate-limiting-and-frequency-capping-together}

Cuando habilitas tanto el límite de velocidad como la limitación de frecuencia en una campaña, Braze los aplica en el siguiente orden:

1. **El límite de velocidad** se aplica primero para seleccionar el grupo inicial de usuarios que pueden recibir mensajes.
2. **La limitación de frecuencia** se aplica después para filtrar usuarios de ese grupo.
3. **Los mensajes se envían** a los usuarios restantes.

{% alert important %}
Si muchos usuarios en tu grupo con límite de velocidad tienen limitación de frecuencia, es posible que envíes menos mensajes que el valor de tu límite de velocidad. Braze no rellena con usuarios adicionales del límite de velocidad una vez que la limitación de frecuencia elimina usuarios del grupo de envío.
{% endalert %}

#### Ejemplo

Con un límite de velocidad de 500 usuarios y la limitación de frecuencia habilitada, si 200 de esos 500 usuarios con límite de velocidad tienen limitación de frecuencia, solo se enviarán 300 mensajes, no 500.

#### Recomendaciones {#recommendations}

Si necesitas llegar a un número específico de usuarios al usar ambas características juntas, considera los siguientes enfoques:

- **Aumenta tu límite de velocidad:** para tener en cuenta a los usuarios que tienen limitación de frecuencia. Por ejemplo, si quieres llegar a 500 usuarios pero esperas que algunos tengan limitación de frecuencia, establece tu límite de velocidad más alto (como 1000 usuarios).
- **Usa solo el límite de velocidad:** si tu objetivo es controlar el volumen de mensajes enviados por campaña.
- **Contacta a tu administrador del éxito del cliente:** para obtener ayuda en el diseño de una estrategia de mensajería sólida que equilibre tanto las necesidades del negocio como las consideraciones técnicas.

### Resumen de la característica {#freq-cap-feat-over}

La limitación de frecuencia se aplica a nivel de envío de campaña o componente de Canvas, y se puede configurar para cada espacio de trabajo desde **Settings** > **Frequency Capping Rules**.

De forma predeterminada, la limitación de frecuencia está activada cuando se crean nuevas campañas. Desde aquí, puedes elegir lo siguiente:

- El canal de mensajería que deseas limitar: push, correo electrónico, SMS, webhook, WhatsApp, LINE o cualquiera de esos canales.
- Cuántas veces cada usuario debe recibir una campaña o componente de Canvas enviado desde un canal dentro de un período de tiempo determinado.
- Cuántas veces cada usuario debe recibir una campaña o componente de Canvas enviado por [etiqueta](#frequency-capping-by-tag) dentro de un período de tiempo determinado.

Este período de tiempo se puede medir en minutos, días o semanas (siete días), con una duración máxima de 30 días.

Cada línea de límites de frecuencia está conectada usando el operador `AND`, y puedes añadir hasta 10 reglas por espacio de trabajo. Puedes incluir múltiples límites para los mismos tipos de mensajes. Por ejemplo, puedes limitar a los usuarios a no más de un push por día y no más de tres pushes por semana. Ten en cuenta que los mensajes abortados no cuentan para la limitación de frecuencia.

![Sección de limitación de frecuencia con listas de campañas y Canvas a las que las reglas se aplicarán y no se aplicarán.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %}){: style="max-width:90%;"}

#### Comportamiento cuando los usuarios alcanzan el límite de frecuencia o un mensaje se aborta en un paso de Canvas {#behavior-when-users-are-frequency-capped-or-a-message-is-aborted-on-a-canvas-step}

La limitación de frecuencia global por sí sola no hace que los usuarios salgan de un Canvas. En los [pasos de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step), los usuarios siguen avanzando cuando un mensaje no se envía debido a la limitación de frecuencia global, en línea con [cómo avanzan los usuarios]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance) a través del paso. Lo mismo aplica cuando un mensaje se aborta (por ejemplo, por una condición de aborto de Liquid): el usuario continúa a través del Canvas como si el mensaje se hubiera enviado.

Esto es independiente de las **validaciones de entrega** en un paso de mensaje. Si un usuario no cumple con los criterios de validación de entrega en el momento del envío, puede salir del Canvas en ese paso.

### Reglas de entrega {#delivery-rules}

Puede haber algunas campañas, como los mensajes transaccionales, que quieras que siempre lleguen al usuario, incluso si ya han alcanzado su límite de frecuencia. Por ejemplo, una aplicación de entregas puede querer enviar un correo electrónico o push cuando se entrega un artículo, independientemente de cuántas campañas haya recibido el usuario.

Si quieres que una campaña en particular anule las reglas de limitación de frecuencia, puedes configurar esto en el dashboard de Braze al planificar la entrega de esa campaña alternando **Frequency Capping** a **OFF**.

Después de esto, se te preguntará si aún quieres que esta campaña cuente para tu límite de frecuencia. Los mensajes que cuentan para la limitación de frecuencia se incluyen en los cálculos del filtro de canal inteligente.

Al enviar [campañas de API]({{site.baseurl}}/developer_guide/rest_api/messaging#messaging), que a menudo son transaccionales, tendrás la capacidad de especificar que una campaña debe ignorar las reglas de limitación de frecuencia estableciendo `override_frequency_capping` en `true` en la solicitud de API.

De forma predeterminada, las nuevas campañas y Canvas que no obedecen los límites de frecuencia tampoco contarán para ellos. Esto es configurable para cada campaña y Canvas.

{% alert note %}
Este comportamiento cambia el comportamiento predeterminado cuando desactivas la limitación de frecuencia para una campaña o Canvas. Los cambios son retrocompatibles y no afectan a los mensajes que están actualmente en vivo.
{% endalert %}

![Sección de controles de entrega con la limitación de frecuencia activada.]({% image_buster /assets/img_archive/frequencycappingupdate.png %}){: style="max-width:90%;"}

#### Cómo cuentan los envíos para los límites {#how-sends-count-toward-caps}

La limitación de frecuencia se aplica por despacho: cada vez que Braze envía una campaña o componente de Canvas a un usuario cuenta para tus límites, no cada variante de mensaje o plataforma dentro de ese envío. Por ejemplo, si los usuarios están limitados a cinco campañas push por semana, no recibirán ninguna campaña push después del quinto despacho hasta que se restablezca el límite.

##### Envíos multicanal {#multichannel-sends}

Cuando un solo despacho usa múltiples canales, ese despacho cuenta como máximo una vez por cada regla de limitación de frecuencia que aplique. Por ejemplo, si creas una campaña multicanal que envía correo electrónico, push de iOS y push de Android en una sola entrega y tu espacio de trabajo tiene reglas para push y correo electrónico, y una regla que aplica a todos los canales, esa entrega cuenta una vez para la regla de push, una vez para la regla de correo electrónico y una vez para la regla de todos los canales; no cuenta una vez por plataforma push ni por mensaje dentro del envío. Si los usuarios están limitados a una campaña push y una de correo electrónico por día y reciben esta campaña multicanal, no son elegibles para campañas push o de correo electrónico adicionales durante el resto del día, a menos que una campaña ignore las reglas de limitación de frecuencia.

Los mensajes dentro de la aplicación y Content Cards no se cuentan como ni para los límites de campañas o componentes de Canvas de ningún tipo.

{% alert important %}
La limitación de frecuencia global se planifica según la zona horaria del usuario y se calcula por días calendario, no por períodos de 24 horas. Por ejemplo, si configuras una regla de limitación de frecuencia de no enviar más de una campaña por día, un usuario puede recibir un mensaje a las 11 pm en su zona horaria local, y sería elegible para recibir otro mensaje una hora después.
{% endalert %}

#### Casos de uso {#use-cases}

{% tabs %}
{% tab Caso de uso 1 %}

Supongamos que estableces una regla de limitación de frecuencia para que tus usuarios no reciban más de tres campañas o pasos de Canvas de notificaciones push por semana de todas las campañas o pasos de Canvas.

Si tu usuario está programado para recibir tres notificaciones push, dos mensajes dentro de la aplicación y una Content Card esta semana, recibirá todos esos mensajes.

{% endtab %}
{% tab Caso de uso 2 %}

Este escenario usa una regla de limitación de frecuencia para que los usuarios no reciban más de dos campañas o pasos de Canvas de notificaciones push por semana de todas las campañas o pasos de Canvas.

**Cuando ocurre el siguiente escenario:**

- Un usuario activa la misma campaña `Campaign ABC` tres veces a lo largo de una semana.
- Este usuario activa `Campaign ABC` una vez el lunes, una vez el miércoles y una vez el jueves.

![Sección de limitación de frecuencia con la regla de no enviar más de 2 campañas/pasos de Canvas de notificaciones push de todas las campañas/pasos de Canvas a un usuario cada 1 semana.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Entonces, el comportamiento esperado es que:**

- Este usuario recibirá los envíos de campaña que se activaron el lunes y el miércoles.
- Este usuario no recibirá el tercer envío de campaña el jueves porque ya ha recibido dos envíos de campaña push esa semana.

{% endtab %}
{% endtabs %}

### Limitación de frecuencia por etiqueta {#frequency-capping-by-tag}

Las [reglas de limitación de frecuencia](#delivery-rules) se pueden aplicar a los espacios de trabajo usando etiquetas específicas que hayas aplicado a tus campañas y Canvas, lo que te permite basar esencialmente tu limitación de frecuencia en grupos con nombres personalizados.

Con la limitación de frecuencia por etiqueta, las reglas se pueden establecer en las etiquetas principales y anidadas, por lo que Braze tendrá en cuenta todas las etiquetas. Por ejemplo, si has seleccionado usar la etiqueta principal A como límite de frecuencia, también incluiremos información de todas las etiquetas anidadas (por ejemplo, las etiquetas B y C) al determinar el límite.

También puedes combinar la limitación de frecuencia regular con la limitación de frecuencia por etiquetas. Considera las siguientes reglas:

1. No más de tres campañas o componentes de Canvas de notificaciones push por semana de todas las campañas y pasos de Canvas. <br>**Y**
2. No más de dos campañas o componentes de Canvas de notificaciones push por semana con la etiqueta `promotional`.

![Sección de limitación de frecuencia con dos reglas que limitan cuántas campañas/Canvas de notificaciones push se pueden enviar a un usuario cada 1 semana.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Como resultado, tus usuarios no recibirán más de tres envíos de campaña por semana en todas las campañas y pasos de Canvas, y no más de dos campañas o componentes de Canvas de notificaciones push con la etiqueta `promotional`.

{% alert important %}
Los Canvas se etiquetan a nivel de Canvas, a diferencia del etiquetado por componente. Por lo tanto, cada componente de Canvas heredará todas las etiquetas a nivel de Canvas.
{% endalert %}

#### Reglas en conflicto {#conflicting-rules}

Cuando las reglas entran en conflicto, se aplica la regla de limitación de frecuencia más restrictiva y aplicable a tus usuarios. Por ejemplo, supongamos que tienes las siguientes reglas:

1. No más de una campaña o componente de Canvas de notificaciones push por semana de todas las campañas y componentes de Canvas. <br>**Y**
2. No más de tres campañas o componentes de Canvas de notificaciones push por semana con la etiqueta `promotional`.

![Sección de limitación de frecuencia con reglas en conflicto para limitar cuántas campañas/pasos de Canvas de notificaciones push se envían a un usuario cada 1 semana.]({% image_buster /assets/img/global_rules.png %} "global rules")

En este ejemplo, tu usuario no recibirá más de una campaña o componente de Canvas de notificaciones push con la etiqueta "promotional" en una semana determinada, porque has especificado que los usuarios no deben recibir más de una campaña o componente de Canvas de notificaciones push de todas las campañas y componentes de Canvas. En otras palabras, la regla de frecuencia más restrictiva aplicable es la regla que se aplicará a un usuario determinado.

#### Recuento de etiquetas {#tag-count}

Las reglas de limitación de frecuencia por etiqueta se calculan en el momento en que se envía un mensaje. Esto significa que la limitación de frecuencia por etiqueta solo cuenta las etiquetas que están actualmente en las campañas o Canvas que un usuario recibió en el pasado. No cuenta las etiquetas que estaban en las campañas o Canvas en el momento en que se enviaron, pero que desde entonces se han eliminado. Sí cuenta si una etiqueta se añade posteriormente a un mensaje que un usuario recibió en el pasado, pero antes de que se envíe el mensaje etiquetado más reciente.

##### Caso de uso {#use-case}

Considera las siguientes campañas y la regla de limitación de frecuencia por etiqueta:

**Campañas**:

- **Campaign A** es una campaña push etiquetada como `promotional`. Está programada para enviarse a las 9 am del lunes.
- **Campaign B** es una campaña push etiquetada como `promotional`. Está programada para enviarse a las 9 am del miércoles.

**Regla de limitación de frecuencia por etiqueta:**

- Tu usuario no debe recibir más de una campaña de notificaciones push por semana con la etiqueta `promotional`.<br><br>

| Acción | Resultado |
|---|---|
| La etiqueta `promotional` se elimina de **Campaign A** después de que tu usuario recibió el mensaje, pero antes de que **Campaign B se haya enviado.** | Tu usuario recibe **Campaign B**. |
| La etiqueta `promotional` se elimina por error de **Campaign A** después de que tu usuario recibió el mensaje. <br> La etiqueta se vuelve a añadir a **Campaign A** el martes, antes de que se envíe **Campaign B**. | Tu usuario no recibe **Campaign B**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Caso de uso" }

#### Envío a gran escala {#sending-at-large-scales}

Las reglas de limitación de frecuencia por etiqueta pueden no aplicarse correctamente a gran escala, como 100 mensajes por canal de campañas o componentes de Canvas.

Por ejemplo, si tu regla de limitación de frecuencia por etiqueta es:

> No más de dos campañas o componentes de Canvas de correo electrónico con la etiqueta `Promotional` a un usuario cada semana.

Y envías al usuario más de 100 correos electrónicos de campañas y pasos de Canvas con la limitación de frecuencia activada a lo largo de una semana, es posible que se envíen más de dos correos electrónicos al usuario.

Dado que 100 mensajes por canal son más mensajes de los que la mayoría de las marcas envían a sus usuarios, es poco probable que te veas afectado por esta limitación. Para evitar esta limitación, puedes establecer un límite para el número máximo de correos electrónicos que deseas que tus usuarios reciban a lo largo de una semana.

Por ejemplo, podrías configurar la siguiente regla:

> No más de tres campañas o componentes de Canvas de correo electrónico por semana de todas las campañas y pasos de Canvas.

Esta regla determina que ningún usuario reciba más de 100 correos electrónicos por semana porque, como máximo, los usuarios reciben tres correos electrónicos por semana de campañas o componentes de Canvas con la limitación de frecuencia activada.

## Preguntas frecuentes {#frequently-asked-questions}

### Si cambio la limitación de envío en un Canvas activo, ¿afecta a los usuarios que ya están en el Canvas? {#if-i-change-a-send-throttle-on-an-active-canvas-does-it-affect-users-already-in-the-canvas}

Sí, cuando aumentas o reduces un límite de velocidad de Canvas, el límite actualizado se aplica a los nuevos mensajes en aproximadamente 30 segundos desde el cambio debido al almacenamiento en caché.

### ¿La limitación de frecuencia hace que los usuarios salgan de un Canvas? {#does-frequency-capping-cause-users-to-exit-a-canvas}

No. Si un usuario de Canvas tiene limitación de frecuencia debido a la configuración de limitación de frecuencia global, el usuario avanza inmediatamente al siguiente paso de Canvas. El usuario **no** sale del Canvas debido al límite de frecuencia.

### ¿Cómo puedo identificar a los usuarios que fueron limitados por frecuencia en un Canvas? {#how-can-i-identify-users-who-were-frequency-capped-in-a-canvas}

Los usuarios con limitación de frecuencia no generan un evento de envío para ese paso. Para identificar a estos usuarios, puedes usar [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) para rastrear eventos de limitación de frecuencia de mensajes. Alternativamente, puedes crear una [extensión de Segment]({{site.baseurl}}/user_guide/audience/segments/segment_extension) para analizar a los usuarios que entraron en el Canvas pero no recibieron el mensaje esperado.

### ¿Por qué el dashboard muestra un error de límite de velocidad para mi campaña? {#why-does-the-dashboard-show-a-rate-limit-error-for-my-campaign}

Esto generalmente significa que el [límite de velocidad de entrega](#delivery-speed-rate-limiting) de la campaña está configurado demasiado bajo para el tamaño de la audiencia, por lo que completar el envío tardaría más de la ventana permitida y Braze muestra una advertencia. Aumenta el límite de velocidad de entrega, reduce la audiencia o usa **Limit send volume** para que cada envío planificado se complete dentro de la ventana de envío permitida. También puedes establecer un [límite de velocidad de mensajería del espacio de trabajo]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) para aplicar un límite en todas las campañas.

**Limit send volume** controla cuántos usuarios son elegibles para un envío, no cuántos mensajes envía Braze por minuto. Solo un límite de velocidad de entrega establece el rendimiento por minuto.

### ¿Qué significa "Enviado" para la limitación de frecuencia? {#what-does-sent-mean-for-frequency-capping}

En análisis y limitación de frecuencia, _Enviado_ se refiere a cuando Braze despacha el mensaje (el envío se registra), no a la entrega final garantizada al dispositivo o buzón de entrada. La limitación de frecuencia y los recuentos de envío usan estos eventos de envío registrados, que pueden diferir de las métricas de "entregado" posteriores.

### ¿Por qué veo rebotes o aplazamientos de correo electrónico? {#why-am-i-seeing-email-bounces-or-deferrals}

Los mensajes de rebote y aplazamiento de correo electrónico usan muchos códigos diferentes y texto específico del proveedor. No trates un código en particular como señal de un problema de límite de velocidad, ya que la causa depende de tu contexto de envío y la retroalimentación del proveedor de buzón.

Si los mensajes se aplazan temporalmente, enviar menos puede ayudar a corto plazo. Usa un [límite de velocidad de entrega](#delivery-speed-rate-limiting), **Limit send volume**, o ambos.

Para una solución a largo plazo, trabaja con un experto en capacidad de entrega para revisar tus datos de rebotes y aplazamientos.