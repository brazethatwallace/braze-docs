## Ver análisis {#viewing-analytics}

Una vez que hayas lanzado tu campaña, puedes volver a la página de detalles de esa campaña para ver las métricas clave. Ve a la página **Campaigns** y selecciona tu campaña para abrir la página de detalles.{% if include.channel != "banner" %} Para {% if include.channel == "Content Card" %}Content Cards {% elsif include.channel == "banner" %}banners {% elsif include.channel == "email" %}correos electrónicos {% elsif include.channel == "in-app message" %}mensajes dentro de la aplicación {% elsif include.channel == "KakaoTalk" %}mensajes de KakaoTalk {% elsif include.channel == "push" %}mensajes push {% elsif include.channel == "SMS" %}mensajes SMS {% elsif include.channel == "whatsapp" %}mensajes de WhatsApp {% elsif include.channel == "webhook" %}webhooks {% endif %}enviados en Canvas, consulta [Análisis de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).{% endif %}

{% alert tip %}
¿Buscas definiciones de los términos y métricas que aparecen en tu informe? Consulta nuestro
  {% if include.channel == "email" %}[Glosario de análisis de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary)
  {% elsif include.channel == "banner" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics) y filtra por Banners.
  {% elsif include.channel == "Content Card" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics) y filtra por Content Cards.
  {% elsif include.channel == "in-app message" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics) y filtra por mensaje dentro de la aplicación.
  {% elsif include.channel == "push" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics) y filtra por Push.
  {% elsif include.channel == "SMS" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics) y filtra por SMS/MMS y RCS.
  {% elsif include.channel == "whatsapp" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics) y filtra por WhatsApp.
  {% elsif include.channel == "webhook" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics) y filtra por Webhook.{% endif %}
{% endalert %}

Desde la pestaña **Campaign Analytics**, puedes ver tus informes en una serie de paneles. Puede que veas más o menos de los que se enumeran en las secciones siguientes, pero cada uno tiene su propia utilidad.

### Intervalo de fechas {#time-range}

De forma predeterminada, el intervalo de tiempo para **Campaign Analytics** mostrará los últimos 90 días desde el momento actual. Esto significa que si la campaña se lanzó hace más de 90 días, los análisis mostrarán "0" para el intervalo de tiempo indicado. Para ver todos los análisis de campañas anteriores, ajusta el intervalo de tiempo del informe.

### Detalles de la campaña {#campaign-details}

El panel **Campaign Details** muestra un resumen de alto nivel del rendimiento general de tu
  {% if include.channel == "banner" %}banner.
  {% elsif include.channel == "Content Card" %}tarjeta de contenido.
  {% elsif include.channel == "email" %}correo electrónico.
  {% elsif include.channel == "in-app message" %}mensaje dentro de la aplicación.
  {% elsif include.channel == "KakaoTalk" %}mensaje de KakaoTalk.
  {% elsif include.channel == "push" %}mensaje push.
  {% elsif include.channel == "SMS" %}SMS, MMS y RCS.
  {% elsif include.channel == "whatsapp" %}mensajes de WhatsApp.
  {% elsif include.channel == "webhook" %}webhook.
  {% endif %}

Revisa este panel para ver métricas generales como el número de mensajes enviados a los destinatarios, la tasa de conversión primaria y los ingresos totales generados por este mensaje. También puedes revisar la configuración de entrega, audiencia y conversión desde esta página.

{% alert note %}
Las cifras de análisis en el dashboard y en Snowflake pueden diferir ligeramente. Braze mide las cifras en el dashboard y registra las filas en Snowflake por separado. Snowflake es la fuente de datos más precisa, por lo que si ves discrepancias entre estas fuentes, te recomendamos consultar los datos de Snowflake.
{% endalert %}

{% if include.channel == "whatsapp" %}
{% alert note %}
El canal de WhatsApp incluye la tasa de lectura. Esta métrica solo se entrega a los usuarios que tienen activados los recibos de lectura, lo que puede variar.
{% endalert %}
{% endif %}

{% if include.channel == "Content Card" %}
![Panel Campaign Details con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/cc-campaign-details.png %})

{% elsif include.channel == "banner" %}
![Panel Campaign Details con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/banners/campaign_details.png %})

{% elsif include.channel == "email" %}
![Panel Campaign Details con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/campaign_details_email.png %})

{% elsif include.channel == "push" %}
![Panel Campaign Details con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/campaign_details_push.png %})

{% elsif include.channel == "SMS" %}
![Panel Campaign Details con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/campaign_details_sms.png %})

{% elsif include.channel == "in-app message" %}
![Panel Campaign Details con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/campaign_details_iam.png %})

En Canvas, verás el rendimiento de los mensajes dentro de la aplicación mapeado en el Canvas que has creado. Puedes utilizar el panel de control de la parte superior de la página para borrar otros tipos de mensajería (canales) y ver solo los mensajes dentro de la aplicación en tu Canvas.

![Una opción para seleccionar el canal, con la casilla de verificación de mensaje dentro de la aplicación seleccionada.]({% image_buster /assets/img/in-app_message_canvas_reporting.png %})

{% elsif include.channel == "KakaoTalk" %}
![La sección Campaign Details.]({% image_buster /assets/img/kakaotalk/campaign_details.png %})

{% elsif include.channel == "webhook" %}
![Panel Campaign Details con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/campaign_details_webhook.png %})

{% endif %}

#### Estimated Audience y Current Audience {#estimated-audience-and-current-audience}

Dependiendo del tamaño de tu espacio de trabajo, el panel **Campaign Details** puede etiquetar las estadísticas de audiencia como **Estimated Audience** o **Current Audience**.

La siguiente tabla resume lo que significa cada etiqueta.

| Etiqueta del pie | Cuándo se utiliza |
| --- | --- |
| **Estimated Audience** | Braze no ejecuta un recuento completo de la base de datos de forma predeterminada. El tamaño de la audiencia se estima a partir de una muestra y se extrapola, de forma similar al rango de **Reachable users** en el generador de segmentos. Se esperan márgenes de error, especialmente para espacios de trabajo grandes o segmentos pequeños como proporción del espacio de trabajo. |
| **Current Audience** | Braze puede calcular la estadística predeterminada con un escaneo completo de los perfiles del espacio de trabajo, por lo que el tamaño de audiencia mostrado es un recuento actual y sin muestreo (aunque sigue sujeto a la accesibilidad del canal, las reglas de suscripción y otras opciones de segmentación). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estimated Audience y Current Audience" }

Para más detalles sobre el comportamiento de muestreo, **Calculate exact statistics** y la segmentación de **Reachable users**, consulta [Medir el tamaño del segmento]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

{% if include.channel == "Content Card" %}

#### Grupos de control {#cc-control-group}

Para medir el impacto de una tarjeta de contenido individual, puedes añadir un [grupo de control]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants) a una prueba A/B. El panel de **Campaign Details** de nivel superior no incluye métricas de la variante del grupo de control.

{% elsif include.channel == "SMS" %}

#### Grupos de control {#sms-control-group}

Para medir el impacto de un mensaje SMS, MMS o RCS individual, puedes añadir un [grupo de control]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants) a una prueba A/B. El panel de **Campaign Details** de nivel superior no incluye métricas de la variante del grupo de control.

{% elsif include.channel == "whatsapp" %}

#### Grupos de control {#whatsapp-control-group}

Para medir el impacto de un mensaje individual de WhatsApp, puedes añadir un [grupo de control]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants) a una prueba A/B. El panel de **Campaign Details** de nivel superior no incluye métricas de la variante del grupo de control.

{% elsif include.channel == "webhook" %}

#### Grupos de control {#webhook-control-group}

Para medir el impacto de un mensaje de webhook individual, puedes añadir un [grupo de control]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants) a una prueba A/B. El panel de **Campaign Details** de nivel superior no incluye métricas de la variante del grupo de control.

{% endif %}

#### Changes Since Last Viewed

El número de actualizaciones de la campaña por parte de otros miembros de tu equipo se registra mediante la métrica *Changes Since Last Viewed* en la página de resumen de la campaña. Selecciona **Changes Since Last Viewed** para ver un registro de cambios de las actualizaciones del nombre de la campaña, la planificación, las etiquetas, el mensaje, la audiencia, el estado de aprobación o la configuración de acceso del equipo. Para cada actualización, puedes ver quién la realizó y cuándo. Puedes utilizar este registro de cambios para auditar los cambios en tu campaña.

<!--
### Message Performance

The **Message Performance** panel outlines how well your message has performed across various dimensions. The metrics in this panel vary depending on your chosen messaging channel, and whether or not you are running a multivariate test. You can click on the <i class="fa fa-eye preview-icon"></i> **Preview** icon to view your message for each variant or channel.
-->
{% if include.channel == "Content Card" %}
### Rendimiento de la tarjeta de contenido {#content-card-performance}

El panel **Content Card Performance** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Preview** para ver tu mensaje para cada variante o canal.

![Análisis del rendimiento de los mensajes de las tarjetas de contenido]({% image_buster /assets/img/cc-message-performance.png %})

{% elsif include.channel == "email" %}
### Rendimiento del correo electrónico {#email-performance}

El panel **Email Performance** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes seleccionar el icono <i class="fa fa-eye preview-icon"></i> **Preview** para ver tu mensaje para cada variante o canal.

![Análisis del rendimiento de los mensajes de correo electrónico]({% image_buster /assets/img_archive/email_message_performance.png %})

{% elsif include.channel == "in-app message" %}
### Rendimiento de los mensajes dentro de la aplicación {#in-app-message-performance}

El panel **In-App Message Performance** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Preview** para ver tu mensaje para cada variante o canal.

![Análisis del rendimiento de los mensajes dentro de la aplicación]({% image_buster /assets/img_archive/iam_message_performance.png %})

{% elsif include.channel == "push" %}
### Rendimiento de push {#push-performance}

El panel **Push Performance** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Preview** para ver tu mensaje para cada variante o canal.

![Análisis del rendimiento de los mensajes push]({% image_buster /assets/img_archive/push_message_performance.png %})

{% elsif include.channel == "SMS" %}
### Rendimiento de SMS/MMS/RCS {#smsmmsrcs-performance}

El panel **SMS/MMS/RCS Performance** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Preview** para ver tu mensaje para cada variante o canal.

![Panel de rendimiento de SMS/MMS/RCS que incluye una tabla de métricas para un grupo de control, la variante 1 y la variante 2.]({% image_buster /assets/img_archive/sms_message_performance.png %})

{% elsif include.channel == "banner" %}
### Rendimiento del banner {#banner-performance}

El panel **Banner Performance** muestra el rendimiento de tu mensaje en varias dimensiones. Estas métricas varían en función del canal de mensajería y de si estás realizando una prueba multivariante o no.

![Panel de rendimiento de SMS/MMS que incluye una tabla de métricas para un grupo de control, la variante 1 y la variante 2.]({% image_buster /assets/img/banners/banner_performance.png %})

{% elsif include.channel == "KakaoTalk" %}
### Rendimiento de KakaoTalk {#kakaotalk-performance}

El panel **KakaoTalk Performance** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Preview** para ver tu mensaje para cada variante o canal.

{% elsif include.channel == "webhook" %}
### Rendimiento del webhook {#webhook-performance}

El panel **Webhook Performance** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Preview** para ver tu mensaje para cada variante o canal.

![Panel de rendimiento de webhooks que incluye una tabla de métricas para un grupo de control y la variante 1.]({% image_buster /assets/img/webhook_message_performance.png %})

{% elsif include.channel == "whatsapp" %}
### Rendimiento de WhatsApp {#whatsapp-performance}

El panel **WhatsApp Performance** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Preview** para ver tu mensaje para cada variante o canal.

![Panel de rendimiento de WhatsApp que incluye una tabla de métricas para la variante 1.]({% image_buster /assets/img/whatsapp_message_performance.png %})

{% endif %}

Si quieres simplificar la vista, haz clic en <i class="fas fa-plus"></i> **Add/Remove Columns** y desmarca las métricas que desees. De forma predeterminada, se muestran todas las métricas.

{% if include.channel == "email" %}

#### Mapas de calor {#heatmaps}

Con los mapas de calor, puedes ver el éxito de los distintos enlaces de una misma campaña de correo electrónico. En la sección **Message Analytics**, ve al panel **Email Performance**. Selecciona **Preview & Heatmap** para ver una vista previa de tu campaña de correo electrónico y el mapa de calor. También puedes seleccionar el hipervínculo del nombre de la variante para ver el mapa de calor.

{% alert note %}
Los análisis de campaña muestran datos de clics para un máximo de 100 URL únicas por variante, ordenadas por clics totales. Las URL se agrupan por su forma normalizada, que no incluye parámetros de consulta. Si una variante tiene más de 100 URL normalizadas únicas, solo se muestran las 100 principales por número de clics. Los datos de clics de las URL que superan este límite siguen existiendo, pero no aparecerán en el dashboard ni en el mapa de calor. Cuando el aliasing de enlaces está habilitado, los clics se rastrean por ID de enlace en lugar de por URL sin procesar, lo que normalmente da como resultado menos entradas únicas y hace que sea menos probable alcanzar este límite.
{% endalert %}

En esta vista, puedes usar la opción **Show Heatmap** para obtener una vista visual de tu correo electrónico que muestre la frecuencia general y la ubicación de los clics dentro de la duración de la campaña. En el panel **Link Table by Total Clicks**, puedes ver todos los enlaces de tu campaña de correo electrónico y ordenarlos por clics totales. Esto puede proporcionar información adicional sobre por dónde navegan tus usuarios. Para guardar una copia del mapa de calor como referencia, selecciona el botón de descarga.

{% alert note %}
Si los enlaces utilizan Liquid para URL dinámicas, las URL en las que se hizo clic pueden no coincidir lo suficiente con el enlace renderizado en el mensaje como para que el mapa de calor asocie los clics con ese enlace, por lo que esos enlaces podrían no aparecer en el mapa de calor. Utiliza los datos de clics del panel **Link Table by Total Clicks** para obtener una imagen completa.
{% endalert %}

![Ejemplo de la página Preview & Heatmap, que incluye una campaña por correo electrónico y un panel con ejemplos de alias de enlaces con su total de clics.]({% image_buster /assets/img_archive/email_heatmap_example.png %})

#### Imágenes {#images}

Te recomendamos habilitar CORS en las URL de tus imágenes para evitar que se rompan en las vistas previas y exportaciones de mapas de calor.

Si faltan imágenes en una exportación, trabaja con tus desarrolladores para que los activos de imagen permitan el acceso entre orígenes: el servidor debe devolver el encabezado `Access-Control-Allow-Origin` con `*` o el dominio de tu dashboard de Braze.

{% endif %}

{% if include.channel == "Content Card" %}

#### Métricas de la tarjeta de contenido {#content-card-metrics}

Aquí tienes un desglose de algunas métricas clave que puedes ver al revisar el rendimiento de tus mensajes. Para ver las definiciones completas de todas las métricas de Content Cards, consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics) y filtra por Content Cards.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Métricas de las tarjetas de contenido">
    <caption class="sr-only">Métricas de rendimiento de las tarjetas de contenido</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#messages-sent">Messages Sent</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Messages Sent' %} <br><br>
                Se calcula de forma diferente según lo que hayas seleccionado para
                <a href="/docs/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression">Creación de tarjetas</a>:<br><br>
                <ul>
                    <li><b>En el lanzamiento o en la entrada del paso:</b> El número de tarjetas creadas y disponibles para ver. Esto no cuenta si los usuarios vieron la tarjeta.</li>
                    <li><b>En la primera impresión:</b> El número de tarjetas mostradas a los usuarios.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#total-impressions">Total Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Esto puede incrementarse varias veces para el mismo usuario.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-impressions">Unique Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">Este recuento</span> no se incrementa la segunda vez que un usuario ve una tarjeta de contenido.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-daily-impressions">Unique Daily Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Daily Impressions' %} <br><br> Dado que un usuario puede tener una impresión diaria única cada día, es de esperar que esta cifra sea superior a <i>Unique Impressions</i>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-clicks">Unique Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Esto incluye los clics en los enlaces de cancelación de suscripción proporcionados por Braze.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-dismissals">Unique Dismissals</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}</td>
        </tr>
    </tbody>
</table>

{% alert note %}
En cuanto a cómo se registran las impresiones, hay algunos matices entre web, Android e iOS. En términos generales, Braze registra una impresión cuando se ve una tarjeta, es decir, después de que un usuario se desplace hasta la tarjeta de contenido específica en su feed.
{% endalert %}

#### Impresiones diarias únicas frente a impresiones únicas {#unique-daily-impressions-versus-unique-impressions}

Hay algunas métricas disponibles que cubren la visibilidad de tu mensaje. Esto incluye _Unique Daily Impressions_ e _Unique Impressions_. Veamos algunos escenarios de ejemplo para comprender mejor estas métricas.

Supongamos que ves una tarjeta de contenido hoy, luego recibes una nueva tarjeta de la misma campaña mañana, y otra más pasado mañana: se te contará como _Unique Daily Impression_ tres veces. Sin embargo, solo se te contabilizará una _Unique Impression_. También se te incluirá en el número de _Messages Sent_, ya que la tarjeta estaba disponible en tu dispositivo.

Como otro ejemplo, supongamos que ves cinco _Unique Impressions_ en una campaña de tarjeta de contenido que muestra 150 000 _Messages Sent_. Esto significa que la tarjeta se puso a disposición (en el backend) de una audiencia de 150 000 usuarios, pero solo los dispositivos de cinco usuarios realizaron todos los pasos siguientes después de que se produjera ese envío:

1. Iniciaron una sesión o la aplicación solicitó explícitamente una sincronización de Content Cards (o ambas cosas)
2. Navegaron a la vista de Content Cards
3. El SDK registró una impresión y la envió al servidor

Tus _Messages Sent_ se refieren a las Content Cards disponibles para ser vistas, mientras que _Unique Daily Impressions_ se refiere a las Content Cards que fueron vistas realmente.

{% elsif include.channel == "banner" %}

### Métricas de los banners {#banner-metrics}

Estas son las métricas clave de seguimiento al revisar el rendimiento de tu campaña de banner. Los clics y las impresiones de los banners se registran automáticamente con el SDK.

Para obtener las definiciones completas de todas las métricas de banners, consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics) y filtra por Banners.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Métricas de los banners">
    <caption class="sr-only">Métricas de rendimiento de los banners</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Total Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} En el caso de los banners, las impresiones se registran una vez por sesión de usuario. Si el mismo banner se ve varias veces dentro de la misma sesión, solo se registra una impresión.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Unique Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">Cada usuario solo se cuenta una vez.</span></td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Total Clicks</a></td>
            <td class="no-split"><i>Total Clicks</i> es el número total (y el porcentaje) de usuarios que hicieron clic en el mensaje entregado, independientemente de si el mismo usuario hace clic varias veces.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-dismissals">Total Dismissals</a></td>
            <td class="no-split"><i>Total Dismissals</i> es el número total de veces que los usuarios descartaron el banner. Solo está disponible para banners con el comportamiento de descarte habilitado.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Unique Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks No Dispatch ID' %} Cada usuario solo se cuenta una vez.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#primary-conversions">Primary Conversions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-daily-impressions">Unique Daily Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Daily Impressions' %} <br><br> Dado que un espectador puede tener una impresión diaria única cada día, es de esperar que esta cifra sea superior a <i>Unique Impressions</i>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#revenue">Revenue</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confidence">Confidence</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Confidence' %}</td>
        </tr>
    </tbody>
</table>

#### Ejemplos de cálculo de métricas de banners {#banner-metrics-calculation-examples}

Hay algunas métricas disponibles que cubren la visibilidad de tu mensaje. Esto incluye _Unique Daily Impressions_ e _Unique Impressions_. Veamos algunos escenarios de ejemplo para comprender mejor estas métricas.

Supongamos que ves un banner hoy, luego ves el mismo banner mañana y de nuevo pasado mañana: se te contará como _Unique Daily Impression_ tres veces. Sin embargo, solo se te contabilizará una _Unique Impression_.

Como otro ejemplo, supongamos que ves cinco _Unique Impressions_ en una campaña de banners. Esto significa que solo los dispositivos de cinco usuarios realizaron todos los pasos siguientes:

1. Iniciaron una sesión o la aplicación solicitó explícitamente una sincronización de banners (o ambas cosas)
2. Navegaron a la vista de banners
3. El SDK registró una impresión y la envió al servidor

_Unique Daily Impressions_ se refiere a los banners que realmente se vieron.

{% elsif include.channel == "email" %}

#### Métricas de correo electrónico {#email-metrics}

Aquí tienes algunas métricas clave específicas del correo electrónico que no verás en otros canales. Para ver las definiciones completas de todas las métricas de correo electrónico utilizadas en Braze, consulta nuestro [Glosario de análisis de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Métricas de correo electrónico">
    <caption class="sr-only">Métricas de rendimiento del correo electrónico</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Unique Clicks</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Este seguimiento se realiza durante un periodo de siete días para el correo electrónico y se mide mediante <a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/messaging/messaging_fundamentals/dispatch_id/'>dispatch_id</a>. Esto incluye los clics en los enlaces de cancelación de suscripción proporcionados por Braze. Esta cifra debería estar entre el 5-10 %. ¡Todo lo que supere el 10 % es excepcional!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-opens">Unique Opens</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Opens' %} En el caso del correo electrónico, se realiza un seguimiento durante un periodo de 7 días. Esta cifra debería estar entre el 30-40 %. ¡Todo lo que supere el 40 % es excepcional!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#click-to-open-rate">Click-to-Open Rate</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#spam">Spam Rate</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Spam' %} Si esta métrica es superior a 0,08, podría ser una señal de que el texto de tu mensaje es demasiado comercial o de que deberías reconsiderar tus métodos de recopilación de direcciones de correo electrónico (para confirmar que estás enviando mensajes a personas interesadas en tu correspondencia).
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unsubscribers-or-unsub">Unsubscribers or Unsub</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#other-opens">Other Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Other Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#estimated-real-opens">Estimated Real Opens</a></td>
            <td class="no-split"> {% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %} Consulta la siguiente sección para más detalles.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#machine-opens">Machine Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Machine Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Bounces</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#hard-bounce">Hard Bounce</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#soft-bounce">Soft Bounce</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deferral">Deferral</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deferral' %}</td>
        </tr>
    </tbody>
</table>

##### Entregas y rebotes {#deliveries-and-bounces}

El dashboard resalta los _rebotes duros_. Algunos _rebotes_ pueden ser rebotes blandos y no coincidirán con ese recuento por sí solos. Puedes aproximar los rebotes blandos con esta fórmula:

_Envíos − (Entregas + Rebotes duros) ≈ Rebotes blandos_

Las _entregas_ pueden aumentar durante la ventana de reintentos de tu proveedor de servicios de correo electrónico (ESP) a medida que los reintentos tienen éxito, mientras que los _envíos_ y los rebotes duros de un envío único se mantienen fijos una vez que se completa el envío. SendGrid y SparkPost reintentan durante un máximo de 72 horas; Amazon SES reintenta durante un máximo de 14 horas.

###### Escenarios comunes de solución de problemas de entrega {#common-delivery-troubleshooting-scenarios}

Al revisar tus análisis de correo electrónico, ten en cuenta estos patrones:

- **Diferencia entre _envíos_ y (_entregas_ + _rebotes duros_):** Durante la ventana de reintentos del ESP después de un envío único, esta diferencia a menudo refleja rebotes blandos o aplazamientos que aún se están reintentando. Después de que finalizan los reintentos, cualquier diferencia restante generalmente significa mensajes que rebotaron de forma blanda y nunca se entregaron; esos envíos no se contabilizan en las _entregas_ ni en los _rebotes_ de la campaña. Utiliza la fórmula anterior para aproximar los rebotes blandos en curso.
- **_Entregas_ bajas después de que finalizan los reintentos:** Si las tasas de entrega siguen siendo bajas una vez que los reintentos han finalizado, compara el volumen de este envío con tus patrones habituales. Los proveedores de buzón pueden aplazar, limitar o rebotar de forma blanda el correo cuando el volumen aumenta en relación con tu reputación de remitente. Puedes ver mensajes como `Email was deferred due to the following reason(s): [IPs were throttled by recipient server]` en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log). Utiliza la [limitación de velocidad de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) para dosificar los envíos grandes, y consulta [IP limitadas]({{site.baseurl}}/user_guide/channels/email/reporting#throttled-ips) para pasos adicionales de solución de problemas.
- **Rebotes blandos y aplazamientos no mostrados en los análisis de campaña:** Los análisis de campaña resaltan los _rebotes duros_ pero no incluyen los _rebotes blandos_ ni los _aplazamientos_ como columnas separadas. Monitoriza estos eventos en el Registro de actividad de mensajes, con el [filtro de segmento de rebote blando]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced), o a través de los eventos de aplazamiento de Currents. Para saber cómo funcionan los reintentos, consulta [Aplazamientos](#deferrals) a continuación.
- **Los porcentajes de entrega pueden no sumar el 100 %:** El _% de entregas_, el _% de rebotes_ y el _% de spam_ pueden no sumar el 100 % de los _envíos_. Los mensajes que rebotan de forma blanda y nunca se entregan después de la ventana de reintentos del ESP no se contabilizan en las _entregas_ ni en los _rebotes_ de la campaña, por lo que pueden dejar una parte de los _envíos_ sin contabilizar en esas tasas. Espera a que finalicen los reintentos antes de juzgar el rendimiento final de la entrega, o utiliza la fórmula anterior para estimar cuántos envíos aún están en reintento.

##### Clics sin un evento de apertura {#clicks-without-an-open-event}

Se puede registrar un clic sin una apertura cuando el píxel de apertura nunca se carga. Por ejemplo, el mensaje está recortado en Gmail o el usuario ha desactivado las imágenes (el píxel de apertura suele estar en el pie de página). Algunos clientes actúan como proxy de las imágenes (como Apple Mail), por lo que la apertura puede registrarse cuando el servidor obtiene el píxel por primera vez, no cuando el usuario lee el correo.

Un clic y una apertura también pueden caer en días diferentes: un usuario podría hacer clic el 16 de mayo con las imágenes desactivadas (sin apertura), y luego abrir en el correo web el 17 de mayo (la apertura se registra entonces).

##### _Clics únicos_ superiores a _aperturas únicas_ {#higher-unique-clicks-than-unique-opens}

Es posible que los _clics únicos_ superen con creces a las _aperturas únicas_ (por ejemplo, varios clics únicos por cada apertura única) incluso cuando esperas una proporción más baja de tu audiencia. Ese patrón suele significar que las aperturas están infrarregistradas, los clics están inflados, o ambas cosas. Sin embargo, esto no significa que Braze esté contando mal los clics de forma aislada.

Braze registra una apertura de correo electrónico cuando se carga el píxel de seguimiento de apertura. Ese píxel es una pequeña imagen transparente (a menudo descrita como de 1 x 1&nbsp;px) que Braze añade al HTML del mensaje. Si el píxel nunca se carga, no se registra ninguna apertura para esa visualización, pero los clics en los enlaces sí pueden registrarse, por lo que tu tasa de clic-a-apertura y el equilibrio entre estas dos métricas pueden parecer sesgados.

**El buzón nunca cargó el píxel de seguimiento de apertura**

El píxel podría no cargarse cuando:

- **El mensaje está recortado.** Un HTML largo empuja el contenido, incluido el píxel en la parte inferior, detrás de un corte del tipo "Ver mensaje completo". En Gmail, los mensajes de más de aproximadamente [102&nbsp;KB]({{site.baseurl}}/user_guide/channels/email/best_practices/email_styling#email-size) suelen recortarse, lo que puede impedir que el píxel se cargue hasta que se abra el mensaje completo (y a veces ni siquiera entonces, dependiendo del cliente).
- **Las imágenes están bloqueadas o restringidas.** Una seguridad de buzón más estricta (habitual en cuentas corporativas) puede bloquear las imágenes remotas hasta que el destinatario elija cargarlas, por lo que el píxel de apertura no se activa aunque hagan clic en los enlaces rastreados.
- **El mensaje está en la carpeta de correo no deseado o masivo.** Muchos proveedores no cargan las imágenes remotas (incluido el píxel de apertura) en esas carpetas de forma predeterminada.

**Qué puedes hacer**

- **Recorte:** Acorta y simplifica el HTML, elimina estilos o activos no utilizados y mantén el tamaño total del mensaje dentro de los límites del cliente. Para Gmail, intenta que sea inferior a unos 102&nbsp;KB como se describe en [Tamaño del correo electrónico]({{site.baseurl}}/user_guide/channels/email/best_practices/email_styling#email-size).
- **Seguridad del buzón y carga de imágenes:** Solo el destinatario (o su política de TI) puede cambiar si las imágenes se cargan de forma predeterminada.
- **Ubicación en correo no deseado:** Céntrate en [mejorar la capacidad de entrega del correo electrónico]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability) y la higiene de la lista. Si el correo llega constantemente a la carpeta de correo no deseado y las métricas parecen incorrectas, ponte en contacto con el [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).

**Actividad de seguridad o bots en los enlaces**

Algunos productos de seguridad de correo electrónico siguen los enlaces para buscar amenazas. Esas solicitudes pueden registrar un clic sin cargar las imágenes, por lo que puedes ver actividad de clics sin una apertura correspondiente.

##### Aplazamientos {#deferrals}

Diferido o aplazamiento es cuando un correo electrónico no se entregó inmediatamente, pero Braze reintenta el correo electrónico a través de tu ESP después de este fallo de entrega temporal para maximizar las posibilidades de entrega exitosa antes de que se detengan los intentos para esa campaña específica. SendGrid y SparkPost reintentan durante un máximo de 72 horas; Amazon SES reintenta durante un máximo de 14 horas. Las razones típicas de los aplazamientos incluyen la limitación de la tasa de volumen de correo electrónico basada en la reputación por parte del proveedor de correo, problemas temporales de conectividad o errores de DNS.

Los _aplazamientos_ difieren de los _rebotes blandos_. Si no se entregó correctamente ningún correo electrónico durante este periodo de reintento, Braze enviará un evento de rebote blando por cada intento de envío de campaña. Antes del 25 de febrero de 2025, estos reintentos se contabilizaban como múltiples rebotes blandos para 1 envío de campaña.

Ten en cuenta que los _aplazamientos_ actualmente solo están disponibles utilizando las características de Currents o Braze Snowflake (como el Generador de consultas, SQL Segment, Snowflake Data Sharing). Si quieres incluirlo en los análisis de Campaign o Canvas, [envía tus comentarios sobre el producto]({{site.baseurl}}/user_guide/administrative/access_braze/portal).

##### Estimación de la tasa de apertura real {#estimated-real-open-rate}

Esta estadística utiliza un modelo de análisis propio creado por Braze para reconstruir una estimación de la tasa de apertura única de la campaña como si las aperturas automáticas no existieran. Aunque recibimos etiquetas de *Machine Opens* en algunos eventos de apertura de los remitentes de correo electrónico (véase más arriba), estas etiquetas a menudo pueden etiquetar aperturas reales como aperturas automáticas. En otras palabras, las *Other Opens* son probablemente una subestimación de las aperturas reales (por usuarios reales). En su lugar, Braze utiliza los datos de clics de cada campaña para deducir la tasa a la que los humanos reales abrieron el mensaje. Esto compensa varios mecanismos de apertura automática, incluido el MPP de Apple.

La _Estimated Real Open Rate_ se calcula 24 horas después del inicio del envío del correo electrónico y se recalcula cada 72 horas a partir de entonces.

Dado que esta métrica se recalcula de forma continua, el valor de la _Estimated Real Open Rate_ puede cambiar con el tiempo a medida que se reciben nuevas señales de interacción (como aperturas y clics) y se incorporan al modelo. En la práctica, la _Estimated Real Open Rate_ puede seguir actualizándose diariamente mientras la campaña permanezca activa.

Normalmente se necesitan unos 10 000 correos electrónicos entregados para que la estadística se calcule correctamente, aunque ese número puede variar en función de la tasa de clics. Si no se puede calcular la estadística, la columna muestra "--".

###### Consideraciones {#considerations}

La Estimated Real Open Rate solo está disponible en campañas y no se informa en eventos de Currents. Esta métrica solo se calcula retroactivamente para las campañas activas lanzadas antes del 14 de noviembre de 2023.

##### Gestión del aumento de las tasas de clics {#handling-increases-in-click-rates}

Las tasas de apertura pueden ser una métrica útil para el seguimiento de tus campañas de correo electrónico. Sin embargo, estas tasas de apertura no son necesariamente indicadores precisos de la interacción humana con las campañas de correo electrónico. Un evento de apertura, por definición, se produce cuando un usuario abre un correo electrónico, lo que significa que se ha descargado correctamente un píxel transparente de seguimiento de apertura.

Además, el uso de herramientas de escaneo de seguridad puede inflar las tasas de apertura. Algunas de estas herramientas protegen a sus usuarios escaneando los correos electrónicos entrantes en busca de contenido malicioso, haciendo clic en los enlaces para verificar su legitimidad. Estos clics suelen denominarse "clics de bots" o "interacción no humana" (INH).

En última instancia, una vez que un correo electrónico sale de nuestros servidores, tenemos una visibilidad limitada de lo que ocurre a continuación, pero aquí tienes algunas recomendaciones para gestionar la INH que afecta a tus resultados:

1. Ten en cuenta que esto puede ocurrirle a cualquier remitente y a casi cualquier destinatario. Los clics, al igual que las aperturas, no son indicadores del todo fiables de la interacción humana con tus mensajes, lo que significa que la INH no se puede prevenir.
2. Una mayor interacción positiva tiende a correlacionarse con una INH más baja, por lo que es importante seguir las [mejores prácticas]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices) de mensajería por correo electrónico. Esto incluye obtener el permiso explícito de tus usuarios para enviar correos electrónicos y dar de baja a los suscriptores no comprometidos con una cadencia regular.
3. Utiliza enlaces HTTPS en tus correos electrónicos siempre que sea posible. La INH es menos frecuente para los remitentes que utilizan enlaces seguros.
4. Si utilizas un proceso para cancelar la suscripción con un solo clic, considera la posibilidad de crear un [centro de preferencias]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview) que dirija a los usuarios a una página para editar y administrar sus preferencias de notificación. Esto puede ser útil porque la INH puede cancelar suscripciones de usuarios inadvertidamente.
5. Considera la posibilidad de utilizar [otras métricas]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-performance) para medir el éxito de tu marketing por correo electrónico, como las conversiones, las sesiones de la aplicación o las visitas al sitio web.
6. Añade un enlace oculto en tus campañas de correo electrónico. Este enlace sería algo que un humano no notaría, como texto blanco sobre blanco o un signo de puntuación. Los bots tienden a hacer clic en todos los enlaces, por lo que puedes concluir que los usuarios que generan eventos de clic en el enlace invisible son en realidad el resultado de INH, por lo que la apertura o el clic no indican necesariamente una interacción positiva.

{% elsif include.channel == "in-app message" %}

#### Métricas de mensajes dentro de la aplicación {#in-app-message-metrics}

Aquí tienes algunas métricas clave de los mensajes dentro de la aplicación que puedes ver en tus análisis. Para ver las definiciones completas de todas las métricas de mensajes dentro de la aplicación utilizadas en Braze, consulta nuestro [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics).

{% alert note %}
Los informes sobre _Button 1 Clicks_ y _Button 2 Clicks_ solo funcionan cuando especificas el **Identifier for Reporting** como "0" y "1" respectivamente en el mensaje dentro de la aplicación.

![El campo "Identifier for Reporting" con el valor "0".]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Métricas de mensajes dentro de la aplicación">
    <caption class="sr-only">Métricas de rendimiento de los mensajes dentro de la aplicación</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#body-clicks">Body Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Body Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-1-clicks">Button 1 Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-2-clicks">Button 2 Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Unique Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Total Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversions-b-c-d">Conversions (B, C, D)</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-conversions">Total Conversions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversion-rate">Conversion Rate</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#close-message">Close Message</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Close Message' %}</td>
        </tr>
    </tbody>
</table>

#### Discrepancias entre grupos de control y variantes {#discrepancies-between-control-groups-and-variants}

Cuando una campaña de mensajes dentro de la aplicación tiene una división de variantes 50-50, a veces el grupo de control tendrá un porcentaje ligeramente superior al de la variante (como 51 % para el grupo de control y 49 % para la variante). Esta discrepancia se debe a una diferencia en el tiempo de renderizado.

La distribución entre los grupos de control y variante está pensada para ser aproximadamente uniforme, pero la asignación a una variante ocurre cuando el mensaje dentro de la aplicación se envía realmente al dispositivo. Algunos usuarios pueden no desencadenar nunca el mensaje dentro de la aplicación (por ejemplo, nunca realizan la acción que desencadena el evento personalizado requerido), lo que puede causar diferencias en el tamaño de los grupos.

{% elsif include.channel == "KakaoTalk" %}

### Métricas de KakaoTalk {#kakaotalk-metrics}

Aquí tienes algunas métricas clave de KakaoTalk que puedes ver en tus análisis. Para más detalles, consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics).

{% alert note %}
Actualmente, las estadísticas de audiencia estimada o exacta no están disponibles para las Campaigns de KakaoTalk.
{% endalert %}

| Término | Definición |
| --- | --- |
| Audiencia | _Audiencia_ es el porcentaje de usuarios que recibieron un mensaje en particular. <br><br>_(Número de destinatarios en la variante) / (Destinatarios únicos)_ |
| Destinatarios únicos | _Destinatarios únicos_ es el número de destinatarios diarios únicos, o usuarios que recibieron un nuevo mensaje en un día. Para que este recuento se incremente para un usuario más de una vez, el usuario debe recibir un nuevo mensaje en un día diferente. Este número se basa en el `user_id`. Para más detalles, consulta [Destinatarios únicos en el Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics#unique-recipients). |
| Envíos | El número total de mensajes enviados en una campaña. Esto no significa que el mensaje fue recibido o entregado a un dispositivo, solo que el mensaje fue enviado. |
| Clics totales | El número total de veces que los usuarios hicieron clic en los mensajes de KakaoTalk enviados. |
| Errores | _Errores_ es el número de errores devueltos por el proveedor de KakaoTalk (se incrementa durante el proceso de envío). |
| Ingresos | _Ingresos_ son los ingresos en dólares de los destinatarios de la campaña dentro de la ventana de conversión primaria establecida. |
| Conversiones primarias | _Conversiones primarias_ es el número de veces que ocurrió un evento definido después de interactuar con o ver un mensaje recibido de una Campaign de Braze. Este evento definido lo determinas tú al crear la campaña. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas de KakaoTalk" }

{% elsif include.channel == "push" %}

#### Métricas push {#push-metrics}

Aquí tienes un desglose de algunas métricas clave que puedes ver al revisar el rendimiento de tus mensajes. Para ver las definiciones completas de todas las métricas push, consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics) y filtra por push.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Métricas push">
    <caption class="sr-only">Métricas de rendimiento push</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Descripción</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Bounces</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %} Consulta <a href="#bounced-push">Notificaciones push rebotadas</a>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#direct-opens">Direct Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opens">Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opens' %}</td>
        </tr>
    </tbody>
</table>

> La entrega de notificaciones es un "mejor esfuerzo" por parte de los servicios de notificaciones push de Apple (APNs). No está destinada a entregar datos a tu aplicación, solo a notificar al usuario que hay nuevos datos disponibles. La distinción importante es que mostraremos cuántos mensajes entregamos con éxito a APNs, no necesariamente cuántos APNs entregó con éxito a los dispositivos.

##### Seguimiento de cancelaciones de suscripción {#tracking-unsubscribes}

Las cancelaciones de suscripción push no se incluyen como métrica en los análisis de campañas y dependen de las actualizaciones del estado push de los usuarios por parte de proveedores como Apple o Google. Estas actualizaciones pueden ser poco frecuentes e impredecibles. Como resultado, las cancelaciones de suscripción push no se incluyen como métrica en los análisis de las campañas push.

Sin embargo, el seguimiento manual de las cancelaciones de suscripción push puede proporcionar información valiosa sobre la respuesta de los usuarios a la frecuencia de tus notificaciones y la relevancia del contenido. Aquí tienes dos opciones para realizar el seguimiento de las cancelaciones de suscripción push: usando filtros de segmento o filtros personalizados.

{% tabs local %}
{% tab Filtros de segmento %}

Puedes crear un segmento para identificar a los usuarios que no tienen habilitada la función push, lo que significa que no están suscritos ni han dado su adhesión voluntaria y no tienen un [token de notificaciones push en primer plano]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration#push-tokens). Por ejemplo, para ver el número de cancelaciones de suscripción en tu aplicación, utilizarías una combinación "O" de los siguientes segmentos:

- `Background or Foreground Push Enabled is false`
- `Has Uninstalled`

![La sección del generador de segmentos con el filtro "Background or Foreground Push Enabled for App" para una aplicación es falso, y el filtro "Has Uninstalled" están seleccionados.]({% image_buster /assets/img/push_unsub_segment_example.png %})

Ten en cuenta que los filtros de segmentación son aproximados y no pueden vincularse específicamente a una fecha y una campaña.

{% endtab %}
{% tab Filtros personalizados %}

{% alert important %}
Al registrar un evento personalizado para el cambio de suscripción, se registrarán [puntos de datos]({{site.baseurl}}/user_guide/data_and_analytics/data_points#consumption-count). Alternativamente, utiliza filtros de segmento para identificar y dirigirte a los usuarios que no están habilitados para push.
{% endalert %}

Para una solución diferente, también recomendamos crear un evento personalizado para las cancelaciones de suscripción push en función de si el estado de habilitación push de un usuario es `true` o `false`, con el fin de hacer un seguimiento de esta métrica.

{% endtab %}
{% endtabs %}

##### Comprender las aperturas {#understanding-opens}

Aunque _Direct Opens_ e _Influenced Opens_ incluyen la palabra "opens" (aperturas), en realidad son métricas diferentes. _Direct Opens_ se refiere a la apertura directa de una notificación push, como se indica en la tabla anterior. _Influenced Opens_ se refiere a la apertura de una aplicación sin abrir una notificación push dentro de un plazo de tiempo determinado tras recibirla. Por tanto, _Influenced Opens_ se refiere a las aperturas de la aplicación, no a las aperturas de las notificaciones push.

##### Botones de acción push e informes {#push-action-buttons-and-reporting}

Cuando añades [botones de acción push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons), el panel **Push Performance** puede incluir **Body Clicks**, **Button 1 Clicks** y **Button 2 Clicks** junto con métricas como **Direct Opens**. Estas columnas miden interacciones diferentes, así que compáralas cuando interpretes la interacción.

_Direct Opens_ refleja las métricas del dashboard para las interacciones que cuentan como una apertura directa de tu mensaje. Los eventos **Push Notification Open** en [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) o Snowflake describen las interacciones push de forma más amplia y pueden incluir campos opcionales como `button_action_type` (por ejemplo, `close`) y `button_string`. Para las definiciones de los campos, consulta [Eventos Push Notification Open]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#push-notification-open-events).

Para **iOS**, las categorías de notificación predeterminadas de Braze (como **Yes** / **No**, **Accept** / **Decline** o **Confirm** / **Cancel**) utilizan un emparejamiento fijo: la primera acción admite `OPEN_APP`, un URI o un vínculo profundo (alineado con **On-Click Behavior** en el compositor). La acción complementaria utiliza `CLOSE` de forma predeterminada: descarta la notificación y no abre la aplicación. Consulta el mapeo predeterminado en [Objeto de botón de acción push de Apple]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-action-button-object-for-braze-default-buttons).

Debido a esto, los toques en el botón preestablecido de descarte (por ejemplo, **No** o **Decline**) normalmente **no** cuentan para _Direct Opens_. Esos toques pueden seguir apareciendo en las exportaciones de **Push Notification Open** cuando se registran, con `button_action_type` establecido en `close` y `button_string` identificando la acción tocada. Cuando compares los análisis de Campaign con los datos del almacén, utiliza esos campos de la carga útil para no tratar los toques de descarte de la misma manera que los toques en el cuerpo de la notificación o la acción principal.

Para **Android**, tú configuras el **On-Click Behavior** por botón (**Open App**, **Redirect to Web URL** o **Deep Link**), por lo que los informes siguen las acciones que configures en lugar de la división predeterminada `OPEN_APP` / `CLOSE` de iOS.

##### Por qué los envíos push pueden superar los destinatarios únicos {#why-push-sends-can-exceed-unique-recipients}

El número de _envíos_ puede superar el número de _destinatarios únicos_ debido a las siguientes razones:

- **La reelegibilidad está activada:** Cuando se habilita la reelegibilidad en la configuración de tu Campaign o Canvas, los usuarios que cumplan los criterios de segmento y entrega pueden recibir la misma notificación push varias veces. El resultado es un mayor número de envíos totales.
- **Los usuarios tienen varios dispositivos:** Si no se habilita la reelegibilidad, la diferencia puede explicarse porque los usuarios tienen varios dispositivos asociados a su perfil. Por ejemplo, un usuario puede tener un smartphone y una tableta, y la notificación push se envía a todos los dispositivos registrados. Cada entrega cuenta como un envío, pero solo se registra un destinatario único.
- **Los usuarios están asignados a varias aplicaciones:** Si los usuarios están asociados a más de una aplicación (como cuando prueban una aplicación nueva), pueden recibir la misma notificación push en cada aplicación. Esto contribuye a un mayor número de envíos.

##### Por qué se producen los rebotes {#bounced-push}

{% tabs %}
{% tab Apple Push Notification service %}

Los rebotes se producen en los servicios de notificaciones push de Apple (APNs) cuando una notificación push intenta entregarse a un dispositivo que no tiene instalada la aplicación prevista. APNs también tiene derecho a cambiar los tokens de los dispositivos arbitrariamente. Si intentas enviar al dispositivo de un usuario en el que su token de notificaciones push ha cambiado entre el momento en que registramos previamente su token (como al principio de cada sesión, cuando registramos a un usuario para obtener un token push) y el momento del envío, se produciría un rebote.

Si un usuario desactiva push en la configuración de su dispositivo, al abrir la aplicación posteriormente el SDK detectará que se ha desactivado push y lo notificará a Braze. En este punto actualizaremos el estado de habilitación de push para que esté deshabilitado. Cuando un usuario deshabilitado recibe una Campaign push antes de tener una nueva sesión, la campaña se enviaría correctamente y aparecería como entregada. El push no rebotará para este usuario. Tras una sesión posterior, cuando intentas enviar un push al usuario, Braze ya sabe si tenemos un token de primer plano, por lo que no se envía ninguna notificación.

Las notificaciones push que caducan antes de la entrega no se consideran fallidas y no se registrarán como rebotadas.

{% endtab %}
{% tab Firebase Cloud Messaging %}

Firebase Cloud Messaging (FCM) puede rebotar en tres casos:

| Escenario | Descripción |
| -- | -- |
| Aplicaciones desinstaladas | Cuando se intenta entregar un mensaje a un dispositivo y la aplicación prevista está desinstalada en ese dispositivo, el mensaje se descartará y se invalidará el ID de registro del dispositivo. Cualquier intento futuro de mensajería con el dispositivo devolverá un error NotRegistered. |
| Copia de seguridad de la aplicación | Cuando se hace una copia de seguridad de una aplicación, su ID de registro podría dejar de ser válido antes de que se restaure la aplicación. En este caso, FCM dejará de almacenar el ID de registro de la aplicación y esta dejará de recibir mensajes. Por ello, los ID de registro **no** deben guardarse cuando se hace una copia de seguridad de una aplicación. |
| Aplicación actualizada | Cuando se actualiza una aplicación, el ID de registro de la versión anterior puede dejar de funcionar. Como tal, una aplicación actualizada debe sustituir su ID de registro existente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Por qué se producen los rebotes" }

{% endtab %}
{% endtabs %}


{% elsif include.channel == "SMS" %}

#### Métricas de SMS, MMS y RCS {#sms-mms-and-rcs-metrics}

Aquí tienes un desglose de algunas métricas clave que puedes ver al revisar el rendimiento de tus mensajes. Para obtener las definiciones completas de todas las métricas de SMS, MMS y RCS, consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics) y filtra por SMS/MMS y RCS.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Métricas de SMS, MMS y RCS">
    <caption class="sr-only">Métricas de rendimiento de SMS, MMS y RCS</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sent">Sent</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sent' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#delivery-failures">Delivery Failures</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confirmed-delivery">Confirmed Delivery</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#rejections">Rejections</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Rejections' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opt-out">Opt-Out</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opt-Out' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#help">Help</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Total Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "webhook" %}

#### Métricas del webhook {#webhook-metrics}

Aquí tienes algunas métricas clave de webhook que puedes ver en tus análisis. Para ver las definiciones completas de todas las métricas de webhook utilizadas en Braze, consulta nuestro [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Métricas del webhook">
    <caption class="sr-only">Métricas de rendimiento del webhook</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">Unique Recipients</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Sends</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#errors">Errors</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Errors' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "whatsapp" %}

#### Métricas de WhatsApp {#whatsapp-metrics}

Aquí tienes algunas métricas clave de WhatsApp que puedes ver en tus análisis. Para ver las definiciones completas de todas las métricas de WhatsApp utilizadas en Braze, consulta nuestro [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Métricas de WhatsApp">
    <caption class="sr-only">Métricas de rendimiento de WhatsApp</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Sends</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deliveries">Deliveries</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#reads">Reads</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Reads' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#failures">Failures</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Failures' %}</td>
        </tr>
    </tbody>
</table>

#### Métricas de bloqueo e informes de usuarios finales {#end-user-blocking-and-reporting-metrics}

Se puede acceder a métricas adicionales a través del [panel del administrador de WhatsApp](https://www.facebook.com/business/help/683499390267496?content_id=NZUBj7XjkYjYuWx), aunque es necesario [confirmar tu acceso](https://www.facebook.com/business/help/218116047387456) para acceder a toda la información disponible.

{% endif %}

### Rendimiento histórico {#historical-performance}

El panel **Historical Performance** te permite ver las métricas del panel **Message Performance** como un gráfico a lo largo del tiempo. Utiliza los filtros de la parte superior del panel para modificar las estadísticas y los canales que aparecen en el gráfico. El intervalo de tiempo de este gráfico siempre reflejará el intervalo de tiempo especificado en la parte superior de la página.

Para obtener un desglose día a día, haz clic en el menú hamburguesa <i class="fas fa-bars"></i> y selecciona **Download CSV** para recibir una exportación CSV del informe.

![Gráfico del panel Historical Performance con estadísticas de ejemplo para un correo electrónico desde febrero de 2021 hasta mayo de 2022.]({% image_buster /assets/img/cc-historical-performance.png %})

{% if include.channel == "in-app message" %}

{% alert note %}
Si seleccionas enviar solo a usuarios que puedan ver la última versión de Braze de mensajes dentro de la aplicación (Generación 3), tu **Target Audience** no se ajusta para reflejar tu elección.
{% endalert %}

{% endif %}

{% if include.channel == "SMS" %}

### Respuestas a palabras clave {#keyword-responses}

El panel **Keyword Responses** te muestra una cronología de las palabras clave entrantes con las que los usuarios respondieron tras recibir tu mensaje.

![Panel de respuestas a palabras clave SMS/MMS/RCS a nivel de Campaign que incluye un gráfico lineal de la distribución de palabras clave a lo largo del tiempo y una sección de categorías de palabras clave con casillas de verificación seleccionadas para adhesión voluntaria, cancelación de suscripción, ayuda, otros, más y asesoramiento.]({% image_buster /assets/img/sms/keyword_responses.png %})

Aquí también puedes ver la distribución de la respuesta de cada categoría de palabras clave para determinar los próximos pasos para [reorientar]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns) y [crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) cómodamente.

![La tabla situada debajo del gráfico de líneas tiene columnas para categoría de palabras clave, distribución de respuestas y reorientación, donde se te ofrece la opción de crear un segmento con la categoría de palabras clave.]({% image_buster /assets/img/sms/keyword_segments.png %})

{% endif %}

### Detalles del evento de conversión {#conversion-event-details}

El panel **Conversion Event Details** te muestra el rendimiento de los eventos de conversión de tu campaña. Para más información, consulta [Eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events#step-3-view-results).

![El panel Conversion Event Details.]({% image_buster /assets/img/cc-conversion.png %})

### Correlación de conversión {#conversion-correlation}

El panel **Conversion Correlation** te da información sobre qué atributos y comportamientos de los usuarios ayudan o perjudican los resultados que estableces para las campañas. Para más información, consulta [Correlación de conversión]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation).

![El panel Conversion Correlation con un análisis de los atributos y el comportamiento de los usuarios a partir del evento de conversión primaria - A.]({% image_buster /assets/img/convcorr.png %})

{% if include.channel == "KakaoTalk" %}

## Generador de informes {#report-builder}

También puedes usar el [Generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder) para crear informes personalizados para tus Campaigns de KakaoTalk. Al crear un informe, puedes filtrar para incluir solo Campaigns de KakaoTalk seleccionando **KakaoTalk** en **Channels**, o filtrando por cualquier etiqueta que hayas aplicado a tus Campaigns de KakaoTalk.

{% endif %}

{% if include.channel == "whatsapp" %}

### Análisis de Meta {#meta-analytics}

Además de los análisis de Braze, se puede acceder a los análisis a nivel de plantilla en el administrador de WhatsApp Business. Para más información, consulta [la documentación de Meta](https://www.facebook.com/business/help/218116047387456).

{% endif %}

{% if include.channel == "SMS" %}

### Eventos SMS de Currents {#sms-currents-events}

Al igual que el correo electrónico, Braze recibe eventos a nivel de usuario relacionados con un mensaje SMS a medida que hace su recorrido hasta un usuario. Cualquier evento SMS entrante también se enviará como evento de Currents a través del evento [SMS InboundReceived]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events). Esto te permite realizar acciones adicionales o informes sobre los mensajes que envían tus usuarios fuera de la plataforma Braze.

{% alert note %}
Los mensajes entrantes se truncan a partir de 1600 caracteres.
{% endalert %}

{% endif %}

{% if include.channel != "whatsapp" %}

## Informe de retención {#retention-report}

Los informes de retención muestran las tasas a las que tus usuarios han realizado un evento de retención seleccionado a lo largo de períodos de tiempo en una Campaign específica{% if include.channel != "banner" %} o Canvas{% endif %}. Para más información, consulta [Informes de retención]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports).

## Informe de embudo {#funnel-report}

Los informes de embudo ofrecen un informe visual que te permite analizar los recorridos que realizan tus clientes después de recibir una Campaign{% if include.channel != "banner" %} o Canvas{% endif %}. Si tu Campaign {% if include.channel != "banner" %}o Canvas {% endif %}utiliza un grupo de control o varias variantes, podrás comprender cómo las diferentes variantes han influido en el embudo de conversión a un nivel más detallado y optimizar en función de estos datos.

Para más información, consulta [Informes de embudo]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports).

{% endif %}