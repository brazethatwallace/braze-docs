---
nav_title: Datos de segmentos
article_title: Exportar datos de segmentos
page_order: 4
page_type: reference
description: "Este artículo de referencia explica cómo exportar datos de segmentos a CSV, los permisos necesarios de exportación de datos de usuario, las exportaciones de pasos en Canvas y los campos incluidos en la exportación."
---

# Exportar datos de segmentos a CSV {#export-segment-data-to-csv}

> Esta página explica cómo solicitar una exportación CSV de los datos de usuario de un segmento, y los datos incluidos en la exportación.

{% alert note %}
Las opciones de exportación CSV aparecen en el desplegable **User Data** solo para los usuarios de la empresa que tienen el [permiso "Export User Data"]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para ese espacio de trabajo.
{% endalert %}

Para exportar los datos de un segmento a un CSV, selecciona el menú desplegable **User Data** mientras editas un segmento y elige exportar los datos de usuario o las direcciones de correo electrónico del segmento.

![Sección de detalles del segmento con el desplegable User Data que muestra las opciones de exportación.]({% image_buster /assets/img_archive/csvexport.png %})

También puedes solicitar una exportación CSV desde la página principal de **Segments** seleccionando el desplegable <i class="fas fa-gear" aria-label="Configuración"></i> **Settings** para un segmento:

![Desplegable de configuración en la página principal de Segments.]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
Para exportar los datos de todos tus perfiles de usuario, crea un segmento sin filtros y, a continuación, solicita una exportación CSV.
{% endalert %}

La salida CSV contiene los datos de cada perfil de usuario capturado en el segmento en el momento de la exportación. Puedes exportar cualquier segmento seleccionando el icono de engranaje y la exportación CSV. Braze generará el informe en segundo plano y lo enviará por correo electrónico al usuario que esté conectado en ese momento.

## Detalles de la exportación CSV de Segment {#segment-csv-export-details}

{% alert note %}
Los usuarios del panel necesitan el permiso **Exportar datos de usuario** para usar las opciones de exportación CSV. Si no tienen este permiso, las opciones de exportación CSV no aparecen.
{% endalert %}

**CSV Export Email Addresses** solo incluye filas de los usuarios del Segment que tienen una dirección de correo electrónico. Por ejemplo, si tu Segment tiene 100,000 usuarios pero solo 50,000 tienen una dirección de correo electrónico, **CSV Export Email Addresses** produce aproximadamente 50,000 filas. **CSV Export User Data** exporta todos los datos de usuario del Segment.

{% alert important %}
Debido a restricciones en el tamaño de los archivos, tu exportación puede fallar si el tamaño estimado de tu Segment supera los 500,000 usuarios. Ten en cuenta que esta restricción utiliza el tamaño estimado de tu Segment, y no el cálculo exacto. Para más detalles, consulta [Exportar Segments grandes](#exporting-large-segments).
{% endalert %}

Si has vinculado tus [credenciales de Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3#integration) a Braze, el CSV se cargará en tu contenedor de S3 bajo la clave `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip`. Debes haber iniciado sesión en el panel para acceder al enlace de descarga que se te envía por correo electrónico.

{% multi_lang_include alerts/important_alerts.md alert='S3 file bucket export' %}

## Datos incluidos en la exportación {#data-included-in-export}

Lo siguiente se incluye en tu exportación dependiendo de tu selección.

### Exportación CSV de datos de usuario {#csv-export-user-data}

| Nombre del campo            | Descripción                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | ID interno (no se puede cambiar)                          |
| country                     | País                                                     |
| created_at                  | Fecha y hora en que se creó el perfil de usuario          |
| created_from                | Método utilizado para crear el perfil de usuario (por ejemplo, REST or transferencia de estado representacional API, SDK or kit de desarrollo de software o importación CSV) |
| devices                     | Información del dispositivo                              |
| date_of_birth               | Fecha de nacimiento                                      |
| email                       | Dirección de correo electrónico                          |
| unsubscribed_from_emails_at | Fecha de cancelación de suscripción de correos electrónicos |
| user_id                     | ID externo                                               |
| first_name                  | Nombre                                                   |
| first_session               | Fecha y hora de la primera sesión                        |
| gender                      | Género                                                   |
| google_ad_ids               | ID de publicidad de Google asociados al usuario          |
| city                        | Ciudad                                                   |
| IDFAs                       | Valores del identificador para publicidad (IDFA)         |
| IDFVs                       | Valores del identificador para proveedor (IDFV)          |
| language                    | Idioma en el estándar ISO-639-1                          |
| last_app_version_used       | Última versión de la aplicación utilizada                |
| last_name                   | Apellido                                                 |
| last_session                | Fecha y hora de la última sesión                         |
| number_of_google_ad_ids     | Cantidad de ID de publicidad de Google asociados         |
| number_of_IDFAs             | Cantidad de IDFA asociados                               |
| number_of_IDFVs             | Cantidad de IDFV asociados                               |
| number_of_push_tokens       | Cantidad de tokens de notificación push asociados        |
| number_of_roku_ad_ids       | Cantidad de ID de publicidad de Roku asociados           |
| number_of_windows_ad_ids    | Cantidad de ID de publicidad de Windows asociados        |
| phone_number                | Número de teléfono                                       |
| opted_into_push_at          | Fecha de adhesión voluntaria a notificaciones push       |
| unsubscribed_from_push_at   | Fecha de cancelación de suscripción de notificaciones push |
| random_bucket               | Número de contenedor aleatorio                           |
| roku_ad_ids                 | ID de publicidad de Roku                                 |
| session_count               | Número total de sesiones                                 |
| timezone                    | Zona horaria del usuario en el mismo formato que la base de datos de zonas horarias de IANA |
| in_app_purchase_total       | Monto total gastado en compras dentro de la aplicación   |
| user_aliases                | Alias de usuario, si los hay                             |
| windows_ad_ids              | ID de publicidad de Windows                              |
| Custom events               | Según la selección en la exportación                     |
| Custom attributes           | Según la selección en la exportación                     |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exportación CSV de datos de usuario" }

{% alert note %}
Cuando exportas datos de usuario desde un paso en Canvas, el CSV incluye a todos los usuarios que han pasado por ese paso durante la vida útil del paso en Canvas. No puedes limitar la exportación a un rango de fechas u otra ventana de tiempo. Para saber cómo ejecutar estas exportaciones, consulta [Exportar datos de Canvas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data).
{% endalert %}

### Exportación CSV de direcciones de correo electrónico {#csv-export-email-addresses}

| Nombre del campo            | Descripción                          |
| --------------------------- | ------------------------------------ |
| user_id                     | ID externo del usuario               |
| first_name                  | Nombre                               |
| last_name                   | Apellido                             |
| email                       | Correo electrónico                   |
| unsubscribed_from_emails_at | Fecha de cancelación de suscripción de correo electrónico |
| opted_in_to_emails_at       | Fecha de adhesión voluntaria al correo electrónico |
| user_aliases                | Alias de usuario, si los hay         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exportación CSV de direcciones de correo electrónico" }

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y de API, visita nuestro artículo de [solución de problemas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% alert note %}
Los datos de grupos de suscripción no están disponibles a través de exportaciones de Segments. Para identificar usuarios por estado de suscripción, crea un Segment separado basado en la membresía del grupo de suscripción y exporta ese Segment.
{% endalert %}

## Exportar Segments grandes {#exporting-large-segments}

Existen varios métodos para exportar un Segment de usuarios grande que contiene más de 500.000 usuarios.

{% tabs %}
{% tab Múltiples Segments %}

Puedes dividir un Segment grande en Segments más pequeños y luego exportar cada uno de los Segments más pequeños desde Braze.

{% endtab %}
{% tab Números de contenedor aleatorio %}

También puedes utilizar [números de contenedor aleatorio]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) para dividir tu base de usuarios en múltiples Segments y luego combinarlos después de la exportación. Por ejemplo, si necesitas dividir tu Segment en dos Segments diferentes, puedes hacerlo con los siguientes filtros:
- Segment 1: el número de contenedor aleatorio es menor que 5000 (incluye 0-4999)
- Segment 2: el número de contenedor aleatorio es mayor que 4999 (incluye 5000-9999)

{% endtab %}
{% tab Endpoints %}

También puedes aprovechar los siguientes endpoints para exportar datos de usuario de un Segment específico. Ten en cuenta que estos endpoints están sujetos a límites de datos y [límites de velocidad]({{site.baseurl}}/api/basics).
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group)

Si has conectado [credenciales de Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3#integration), las exportaciones grandes se pueden entregar a tu contenedor de S3 además del enlace de descarga enviado por correo electrónico, como se describe en [Detalles de exportación CSV de Segment](#segment-csv-export-details).

{% endtab %}
{% endtabs %}