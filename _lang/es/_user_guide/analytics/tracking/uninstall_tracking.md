---
nav_title: Uninstall Tracking
article_title: Uninstall Tracking
page_order: 1
page_type: reference
description: "Este artículo de referencia cubre la implementación de Uninstall Tracking para estadísticas a nivel de Campaign y a nivel de aplicación."
tool: Reports

---

# Uninstall Tracking {#uninstall-tracking}

> Este artículo muestra cómo puedes ver las desinstalaciones de aplicaciones agregadas a lo largo del tiempo para localizar tendencias y anomalías, y realizar un seguimiento de las desinstalaciones a nivel de Campaign para determinar si una Campaign específica está impulsando o impidiendo las instalaciones de aplicaciones.

Uninstall Tracking en Braze proporciona los siguientes detalles:

1. Estadísticas diarias de desinstalación de aplicaciones en un gráfico de series temporales en la página de **inicio**.
2. Estadísticas de desinstalación a nivel de Campaign en un gráfico de series temporales en la página **Detalles de Campaign** de una Campaign específica. Esta estadística especifica el número de destinatarios de la Campaign que desinstalan cada día.

{% alert note %}
Debes realizar la adhesión voluntaria para Uninstall Tracking en tu panel de Braze. Esta característica está disponible para aplicaciones en iOS, Android y Fire OS.
{% endalert %}

## Cómo funciona {#how-it-works}

Braze recopila automáticamente un nivel base de información de desinstalaciones a partir de tus Campaigns de push habituales. Sin embargo, dado que la frecuencia con la que diferentes usuarios reciben Campaigns de push puede variar, ofrecemos Uninstall Tracking para proporcionar una instantánea más precisa de la actividad de desinstalación entre tus usuarios.

Cuando Braze detecta una desinstalación, el usuario se etiqueta como desinstalado. Si utilizas el filtro **Has Not Uninstalled** en una Campaign, estos usuarios etiquetados quedan excluidos. Si un usuario reinstala la aplicación pero no la abre, la etiqueta de desinstalación permanece en su perfil. La etiqueta solo se elimina cuando el usuario inicia una nueva sesión en la aplicación reinstalada. Esto significa que un usuario que reinstala pero nunca abre la aplicación sigue apareciendo como desinstalado.

Para más información sobre el uso de Uninstall Tracking, consulta nuestra publicación del blog [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Activar Uninstall Tracking {#turning-on-uninstall-tracking}

Puedes activar Uninstall Tracking en la página **Configuración de la aplicación**, en **Configuración**, para cada aplicación que desees rastrear.

Cuando activas Uninstall Tracking para una aplicación, Braze envía un mensaje push en segundo plano cada noche a los usuarios que no han registrado una sesión ni recibido un push en las últimas 24 horas.

### Configuración {#configuration}

Para configurar Uninstall Tracking en tu aplicación iOS, utiliza un [método de utilidad]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls?sdktab=swift). Para tu aplicación Android, utiliza [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html). Cuando Braze detecta una desinstalación, ya sea a través de Uninstall Tracking o de la entrega normal de una Campaign push, registramos la hora más aproximada de la desinstalación en el perfil del usuario. Esta hora se almacena en el perfil de usuario como un atributo estándar y puede utilizarse para definir un Segment de usuarios para Campaigns de recuperación.

## Filtrar Segments por desinstalaciones {#filtering-segments-by-uninstalls}

El filtro **Desinstalados** selecciona a los usuarios que desinstalaron tu aplicación dentro de un rango de tiempo. Dado que es difícil determinar el momento exacto de una desinstalación, recomendamos que los filtros de desinstalación tengan rangos de tiempo más amplios para asegurarte de que todos los que desinstalan caigan en el Segment en algún momento.

Las estadísticas diarias sobre desinstalaciones se encuentran en la página de **Inicio**.

![Segment de desinstalaciones.]({% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment")

El gráfico se puede desglosar por aplicación y Segment, de forma similar a otros análisis que proporciona Braze. En la sección **Resumen de rendimiento**, selecciona tu rango de fechas y, si lo deseas, una aplicación. Luego, desplázate hasta el gráfico **Rendimiento a lo largo del tiempo** y haz lo siguiente:

1. En el menú desplegable **Statistics For**, selecciona **Uninstalls**.
2. En el menú desplegable **Breakdown**, selecciona **By segment**.
3. En el menú desplegable **Breakdown Values**, selecciona los Segments que deseas incluir en el gráfico.

{% alert note %}
Las aplicaciones sin Uninstall Tracking habilitado solo reportarán las desinstalaciones de un subconjunto de sus usuarios (aquellos a los que se les dirigieron notificaciones push), por lo que los totales diarios de desinstalaciones pueden ser más altos de lo que se muestra.
{% endalert %}

## Uninstall Tracking para Campaigns {#uninstall-tracking-for-campaigns}

Uninstall Tracking para Campaigns muestra el número de usuarios que recibieron una Campaign específica y posteriormente desinstalaron tu aplicación dentro del período de tiempo seleccionado. Esta herramienta ofrece información sobre cómo las Campaigns pueden estar fomentando comportamientos negativos no deseados de los usuarios y ayuda a medir la eficacia general de la Campaign.

Las estadísticas de desinstalación para Campaigns se encuentran en la página **Campaign Analytics** de una Campaign específica. Para Campaigns multicanal y multivariantes, las desinstalaciones se pueden desglosar por canal y variante, respectivamente.

![Desinstalación a nivel de Campaign.]({% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %})

### Cómo funciona

Braze realiza el seguimiento de desinstalaciones observando cuándo los mensajes push enviados a los dispositivos de los usuarios devuelven una señal de Firebase Cloud Messaging (FCM) o del servicio de notificaciones push de Apple (APN) indicando que la aplicación ya no está instalada. Si activas Global Uninstall Tracking para una aplicación, Braze envía un push silencioso diario a los usuarios para detectar si han desinstalado la aplicación. Braze envía este push "silencioso" a todos los usuarios (a menos que el usuario haya deshabilitado los push silenciosos en la configuración de su aplicación); el push no es visible para los usuarios. Si Braze detecta que un usuario ha desinstalado la aplicación:

* Incrementa en uno el recuento total de desinstalaciones de la aplicación.
* Incrementa en uno el recuento de desinstalaciones de cada Campaign que el usuario recibió con éxito en las últimas 24 horas.
* Si un usuario recibe tres Campaigns en un período de 24 horas y luego desinstala la aplicación, incrementamos el recuento de "desinstalaciones" de las tres Campaigns.

FCM y APN imponen restricciones sobre Uninstall Tracking. Braze solo incrementa el recuento de desinstalaciones cuando FCM o APN nos informan de que un usuario ha desinstalado la aplicación, pero estos sistemas de terceros pueden notificarnos de las desinstalaciones en cualquier momento. Utiliza Uninstall Tracking para detectar tendencias direccionales en lugar de estadísticas precisas.

Braze trata una respuesta de FCM como una respuesta de eliminación de token (desinstalación) cuando FCM informa de que el token de registro ya no es válido, como `DEVICE_UNREGISTERED` o `NotRegistered`. Braze registra otros errores de push como rebotes sin eliminar el token.

Para más información sobre el uso de Uninstall Tracking, consulta nuestra publicación en el blog [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Solución de problemas {#troubleshooting}

### ¿Cuándo se marca el perfil de un usuario como desinstalado? ¿Cuándo se elimina la etiqueta de desinstalación? {#when-is-a-users-profile-flagged-as-uninstalled-when-is-the-uninstall-tag-cleared}

Braze marca a un usuario como desinstalado cuando detecta que la aplicación ya no está en el dispositivo (consulta [Cómo funciona](#how-it-works) para conocer la detección con push regular y Uninstall Tracking opcional). Después de que alguien reinstala tu aplicación, la etiqueta de desinstalación puede permanecer en su perfil hasta que **abra la aplicación e inicie una nueva sesión**; reinstalar por sí solo no elimina la etiqueta. Hasta esa sesión, los Segments y filtros que utilizan el estado de desinstalación (por ejemplo, **Has Not Uninstalled**) siguen tratando al usuario como desinstalado.

### ¿Por qué estoy viendo un pico repentino en las desinstalaciones? {#why-am-i-suddenly-seeing-a-spike-in-uninstalls}

Si ves un pico en las desinstalaciones de la aplicación, puede deberse a que Firebase Cloud Messaging (FCM) y el servicio de notificaciones push de Apple (APN) están revocando tokens antiguos con una frecuencia diferente.

{% alert note %}
Por razones de privacidad, los proveedores de push de Braze pueden revocar tokens a intervalos irregulares, lo que significa que los conteos de desinstalaciones a veces pueden presentar picos en un período de tiempo determinado.<br><br>Para validar estos cambios, monitorea Uninstall Tracking junto con una métrica de acción del usuario, como la tarifa abierta de push directa. Si las desinstalaciones aumentan drásticamente pero las aperturas de push directo permanecen estables, es probable que el pico refleje la revocación de tokens antiguos por parte de un partner en lugar de un comportamiento real del usuario.
{% endalert %}

### ¿Cómo determino si una Campaign específica causó desinstalaciones? {#how-do-i-determine-if-a-specific-campaign-caused-uninstalls}

Revisa los análisis de las Campaigns que enviaron mensajes alrededor del mismo momento en que ocurrió el pico de desinstalaciones. Si un mensaje en particular se correlaciona con un aumento en las desinstalaciones, puede estar influyendo en los usuarios para desinstalar.

Para ver las desinstalaciones por Segment:
1. Ve a la página **Inicio** del panel.
2. En la sección **Performance Over Time**, selecciona **Uninstalls** en **Statistics For** y **By Segment** en **Breakdown**.

Si tienes un Segment que hace seguimiento de usuarios inactivos con el [seguimiento de análisis]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) habilitado, compara su tendencia de desinstalaciones con la tendencia general de la aplicación.

### ¿Cómo confirmo que las desinstalaciones son genuinas? {#how-do-i-confirm-uninstalls-are-genuine}

Para APN, revisa los perfiles de usuario en busca del error de push `BadDeviceToken`. Si ves este error de forma masiva alrededor del mismo período que el pico de desinstalaciones, es probable que las desinstalaciones sean genuinas. `BadDeviceToken` indica que el token de push del dispositivo ya no es válido, lo que generalmente ocurre cuando la aplicación se desinstala.

### ¿Por qué el número de desinstalaciones de la aplicación es diferente de lo que aparece en APN? {#why-are-the-number-of-app-uninstalls-different-from-whats-in-apns}

La diferencia es esperada.

Apple utiliza un calendario aleatorio para retrasar la notificación cuando un token de push deja de ser válido, lo que significa que incluso después de que un usuario desinstala una aplicación, APN puede seguir devolviendo respuestas exitosas a las notificaciones push durante un período de tiempo. Este retraso es intencional y está diseñado para proteger la privacidad del usuario. No se reportará ningún rebote o fallo hasta que APN devuelva un estado `410` para un token no válido.

### ¿Cómo se relaciona Uninstall Tracking con el push silencioso o en segundo plano? {#how-does-uninstall-tracking-relate-to-silent-or-background-push}

La detección de desinstalaciones puede utilizar pushes en segundo plano de baja prioridad que no se muestran como una notificación visible. Estos son independientes de los [**envíos**]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics) de Campaigns en los análisis de mensajería estándar. Al analizar las tendencias de desinstalaciones, revisa los gráficos de desinstalaciones junto con las métricas de participación de push en lugar de comparar los pushes de desinstalación directamente con los totales de envíos de marketing.