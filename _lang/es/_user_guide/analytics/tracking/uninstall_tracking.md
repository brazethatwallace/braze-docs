---
nav_title: Uninstall Tracking
article_title: Uninstall Tracking
page_order: 1
page_type: reference
description: "Este artículo de referencia cubre la implementación de Uninstall Tracking para estadísticas a nivel de Campaign y a nivel de aplicación."
tool: Reports

---

# Uninstall Tracking

> Este artículo muestra cómo puedes ver las desinstalaciones de aplicaciones agregadas a lo largo del tiempo para localizar tendencias y anomalías, y realizar un seguimiento de las desinstalaciones a nivel de Campaign para determinar si una Campaign específica está impulsando o impidiendo las instalaciones de aplicaciones.

Uninstall Tracking en Braze proporciona los siguientes detalles:

1. Estadísticas diarias de desinstalación de aplicaciones en un gráfico de series temporales en la página de **inicio**.
2. Estadísticas de desinstalación a nivel de Campaign en un gráfico de series temporales en la página **Detalles de Campaign** de una Campaign específica. Esta estadística especifica el número de destinatarios de la Campaign que desinstalan cada día.

{% alert note %}
Debes realizar la adhesión voluntaria para Uninstall Tracking en tu panel de Braze. Esta característica está disponible para aplicaciones en iOS, Android y Fire OS.
{% endalert %}

## Cómo funciona {#how-it-works}

Braze recopila automáticamente un nivel básico de información de desinstalación de tus campañas push regulares. Sin embargo, debido a que la frecuencia con la que los diferentes usuarios reciben campañas push puede variar, ofrecemos Uninstall Tracking para proporcionar una instantánea más precisa de la actividad de desinstalación entre tus usuarios.

Cuando Braze detecta una desinstalación, el usuario se etiqueta como desinstalado. Si utilizas el filtro **No ha desinstalado** en una Campaign, estos usuarios etiquetados se excluyen. Si un usuario reinstala la aplicación pero no la abre, la etiqueta de desinstalación permanece en su perfil. La etiqueta solo se elimina cuando el usuario inicia una nueva sesión en la aplicación reinstalada. Esto significa que un usuario que reinstala pero nunca abre la aplicación sigue apareciendo como desinstalado.

Para obtener más información sobre el uso de Uninstall Tracking, consulta nuestra entrada de blog [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Activar Uninstall Tracking {#turning-on-uninstall-tracking}

Puedes activar Uninstall Tracking en la página **Configuración de la aplicación**, en **Configuración**, para cada aplicación que quieras rastrear.

Cuando activas Uninstall Tracking para una aplicación, Braze envía un mensaje push nocturno en segundo plano a los usuarios que no han registrado una sesión ni recibido un push en las últimas 24 horas.

### Configuración {#configuration}

Para configurar Uninstall Tracking para tu aplicación iOS, utiliza un [método de utilidad]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls?sdktab=swift). Para tu aplicación Android, utiliza [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html). Cuando Braze detecta una desinstalación, ya sea a partir de Uninstall Tracking o de la entrega normal de campañas push, registraremos la mejor hora estimada de la desinstalación en el usuario. Este tiempo se almacena en el perfil de usuario como un atributo estándar y puede utilizarse para definir un segmento de usuarios para campañas de recuperación.

## Filtrado de segmentos por desinstalaciones {#filtering-segments-by-uninstalls}

El filtro **Desinstalados** selecciona a los usuarios que desinstalaron tu aplicación en un intervalo de tiempo determinado. Como es difícil determinar la hora exacta de una desinstalación, recomendamos que los filtros de desinstalación tengan rangos de tiempo más amplios para asegurarnos de que todos los que desinstalan entran en el segmento en algún momento.

Las estadísticas diarias de desinstalaciones se encuentran en la página de **inicio**.

![Segmento de desinstalaciones.]({% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment")

El gráfico puede desglosarse por aplicación y segmento, de forma similar a otras estadísticas que ofrece Braze. En la sección **Resumen del rendimiento**, selecciona el intervalo de fechas y, si lo deseas, una aplicación. A continuación, desplázate hasta el gráfico **Rendimiento en el tiempo** y haz lo siguiente:

1. En el menú desplegable **Statistics For**, selecciona **Uninstalls**.
2. En el desplegable **Breakdown**, selecciona **By Segment**.
3. En el desplegable **Breakdown Values**, selecciona los segmentos que deseas incluir en el gráfico.

{% alert note %}
Las aplicaciones sin Uninstall Tracking habilitado informarán de las desinstalaciones de solo un subconjunto de sus usuarios (aquellos a los que se dirigieron las notificaciones push), por lo que los totales diarios de desinstalaciones pueden ser superiores a los que se muestran.
{% endalert %}

## Uninstall Tracking para Campaigns {#uninstall-tracking-for-campaigns}

El seguimiento de desinstalaciones de Campaigns muestra el número de usuarios que recibieron una Campaign específica y posteriormente desinstalaron tu aplicación en el periodo de tiempo seleccionado. Esta herramienta ofrece información sobre cómo las campañas pueden estar fomentando comportamientos negativos no deseados de los usuarios y ayuda a medir la eficacia general de las campañas.

Las estadísticas de desinstalación de campañas se encuentran en la página **Campaign Analytics** de una Campaign específica. Para las campañas multicanal y multivariantes, las desinstalaciones pueden desglosarse por canal y variante, respectivamente.

![Desinstalaciones a nivel de Campaign.]({% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %})

### Cómo funciona

Braze rastrea las desinstalaciones observando cuándo los mensajes push enviados a los dispositivos de los usuarios devuelven una señal, ya sea de Firebase Cloud Messaging (FCM) o del servicio de notificaciones push de Apple (APN), de que la aplicación ya no está instalada. Si activas Uninstall Tracking global para una aplicación, Braze envía un mensaje push silencioso diario a los usuarios para detectar si la han desinstalado. Braze envía este push «silencioso» a todos los usuarios (a menos que el usuario haya desactivado las notificaciones silenciosas en la configuración de la aplicación); el push no aparece a los usuarios. Si Braze detecta que un usuario ha desinstalado la aplicación:

* Aumenta en uno el recuento total de desinstalaciones de la aplicación.
* Incrementa en uno el recuento de desinstalaciones de cada Campaign que el usuario haya recibido correctamente en las últimas 24 horas.
* Si un usuario recibe tres campañas en un periodo de 24 horas y luego desinstala, incrementamos el recuento de «desinstalaciones» de las tres campañas.

FCM y APN imponen restricciones a Uninstall Tracking. Braze solo incrementa el recuento de desinstalaciones cuando FCM o APN nos informan de que un usuario ha desinstalado la aplicación, pero estos sistemas de terceros pueden notificarnos las desinstalaciones en cualquier momento. Utiliza Uninstall Tracking para detectar tendencias direccionales en lugar de estadísticas precisas.

Braze trata las siguientes respuestas de FCM como respuestas de eliminación de token (desinstalación): `DEVICE_UNREGISTERED`, `BAD_REGISTRATION` y `SENDER_ID_MISMATCH`.

Para obtener más información sobre el uso de Uninstall Tracking, consulta nuestra entrada de blog [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Solución de problemas {#troubleshooting}

### ¿Cuándo se marca el perfil de un usuario como desinstalado? ¿Cuándo se elimina la etiqueta de desinstalación? {#when-is-a-users-profile-flagged-as-uninstalled-when-is-the-uninstall-tag-cleared}

Braze marca a un usuario como desinstalado cuando detecta que la aplicación ya no está en el dispositivo (consulta [Cómo funciona](#how-it-works) para la detección con push regular y Uninstall Tracking opcional). Después de que alguien reinstala tu aplicación, la etiqueta de desinstalación puede permanecer en su perfil hasta que **abra la aplicación e inicie una nueva sesión**: reinstalar por sí solo no elimina la etiqueta. Hasta esa sesión, los segmentos y filtros que utilizan el estado de desinstalación (por ejemplo, **No ha desinstalado**) siguen tratando al usuario como desinstalado.

### ¿Por qué de repente veo un pico de desinstalaciones? {#why-am-i-suddenly-seeing-a-spike-in-uninstalls}

Si observas un pico de desinstalaciones de aplicaciones, puede deberse a que Firebase Cloud Messaging (FCM) y el servicio de notificaciones push de Apple (APN) revocan tokens antiguos con una frecuencia diferente.

{% alert note %}
Por motivos de privacidad, los proveedores de notificaciones push de Braze pueden revocar los tokens a intervalos irregulares, lo que significa que el número de desinstalaciones puede dispararse en un periodo de tiempo determinado.<br><br>Para validar estos cambios, supervisa Uninstall Tracking junto con una métrica de acción del usuario, como la tasa de apertura directa de notificaciones push. Si las desinstalaciones aumentan considerablemente, pero las aperturas directas se mantienen estables, es probable que el pico refleje la revocación de tokens antiguos por parte de un proveedor, en lugar del comportamiento real de los usuarios.
{% endalert %}

### ¿Cómo puedo determinar si una Campaign específica causó desinstalaciones? {#how-do-i-determine-if-a-specific-campaign-caused-uninstalls}

Revisa los análisis de las campañas que enviaron mensajes en torno al mismo momento en que se produjo el pico de desinstalaciones. Si un mensaje en particular se correlaciona con un aumento de desinstalaciones, puede estar influyendo en los usuarios para que desinstalen.

Para ver las desinstalaciones por segmento:
1. Ve a la página de **inicio** del panel.
2. En la sección **Performance Over Time**, selecciona **Uninstalls** en **Statistics For** y **By Segment** en **Breakdown**.

Si tienes un segmento que rastrea usuarios inactivos con [seguimiento de análisis]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) habilitado, compara su tendencia de desinstalaciones con la tendencia general de la aplicación.

### ¿Cómo puedo confirmar que las desinstalaciones son genuinas? {#how-do-i-confirm-uninstalls-are-genuine}

Para APN, revisa los perfiles de usuario en busca del error push `BadDeviceToken`. Si ves este error de forma masiva en torno al mismo periodo de tiempo que el pico de desinstalaciones, es probable que las desinstalaciones sean genuinas. `BadDeviceToken` indica que el token de notificaciones push del dispositivo ya no es válido, lo que normalmente ocurre cuando la aplicación se desinstala.

### ¿Por qué el número de desinstalaciones de aplicaciones difiere del que aparece en APN? {#why-are-the-number-of-app-uninstalls-different-from-whats-in-apns}

La diferencia es esperable.

Apple utiliza un calendario aleatorio para retrasar la notificación cuando un token de notificaciones push deja de ser válido, lo que significa que, incluso después de que un usuario desinstale una aplicación, APN puede seguir devolviendo respuestas satisfactorias a las notificaciones push durante un periodo de tiempo. Este retraso es intencionado y está diseñado para proteger la privacidad de los usuarios. No se informará de ningún rebote o fallo hasta que APN devuelva un estado `410` para un token no válido.

### ¿Cómo se relaciona Uninstall Tracking con el push silencioso o en segundo plano? {#how-does-uninstall-tracking-relate-to-silent-or-background-push}

La detección de desinstalaciones puede utilizar notificaciones push en segundo plano de baja prioridad que no se muestran como una notificación visible. Estas son independientes de los [**envíos**]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics) de Campaign en los análisis de mensajería estándar. Al analizar las tendencias de desinstalación, revisa los gráficos de desinstalaciones junto con las métricas de participación push en lugar de comparar los push de desinstalación directamente con los totales de envíos de marketing.