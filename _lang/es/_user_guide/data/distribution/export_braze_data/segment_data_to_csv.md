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
Las opciones de exportación CSV aparecen en el desplegable **User Data** solo para los usuarios de la empresa que tienen el [permiso "Export User Data"]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) para ese espacio de trabajo.
{% endalert %}

Para exportar los datos de un segmento a un CSV, selecciona el menú desplegable **User Data** mientras editas un segmento y elige exportar los datos de usuario o las direcciones de correo electrónico del segmento.

![Sección de detalles del segmento con el desplegable User Data que muestra las opciones de exportación.]({% image_buster /assets/img_archive/csvexport.png %})

También puedes solicitar una exportación CSV desde la página principal de **Segments** seleccionando el desplegable <i class="fas fa-gear"></i> **Settings** para un segmento:

![Desplegable de configuración en la página principal de Segments.]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
Para exportar los datos de todos tus perfiles de usuario, crea un segmento sin filtros y, a continuación, solicita una exportación CSV.
{% endalert %}

La salida CSV contiene los datos de cada perfil de usuario capturado en el segmento en el momento de la exportación. Puedes exportar cualquier segmento seleccionando el ícono de engranaje y la exportación CSV. Braze generará el informe en segundo plano y lo enviará por correo electrónico al usuario que esté conectado en ese momento.

## Detalles de la exportación CSV de segmentos {#segment-csv-export-details}

{% alert note %}
Los usuarios del dashboard necesitan el permiso **Export user data** para utilizar las opciones de exportación CSV. Si no tienen este permiso, las opciones de exportación CSV no aparecen.
{% endalert %}

**Exportación de direcciones de correo electrónico a CSV** solo incluye filas para los usuarios del segmento que tienen una dirección de correo electrónico. Por ejemplo, si tu segmento tiene 100 000 usuarios pero solo 50 000 tienen una dirección de correo electrónico, **Exportación de direcciones de correo electrónico a CSV** produce aproximadamente 50 000 filas. **Exportación de datos de usuario a CSV** exporta todos los datos de usuario del segmento.

{% alert important %}
Debido a las restricciones de tamaño de los archivos, la exportación puede fallar si el tamaño estimado de tu segmento es superior a 500 000 usuarios. Ten en cuenta que esta restricción utiliza el tamaño estimado de tu segmento, y no el cálculo exacto. Para más detalles, consulta [Exportar segmentos grandes](#exporting-large-segments).
{% endalert %}

Si has vinculado tus [credenciales de Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration) a Braze, el CSV se cargará en tu contenedor de S3 con la clave `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip`. Debes haber iniciado sesión en el dashboard para acceder al enlace de descarga que se te ha enviado por correo electrónico.

{% multi_lang_include alerts/important_alerts.md alert='S3 file bucket export' %}

## Datos incluidos en la exportación {#data-included-in-export}

Dependiendo de tu selección, tu exportación incluirá lo siguiente.

### Exportación de datos de usuario a CSV {#csv-export-user-data}

| Nombre del campo                  | Descripción                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | ID interno (no se puede cambiar)                           |
| country                     | País                                    |
| created_at                  | Fecha y hora de creación del perfil de usuario                   |
| created_from                | Método utilizado para crear el perfil de usuario (por ejemplo, REST API, SDK o importación CSV)         |
| devices                     | Información sobre el dispositivo                           |
| date_of_birth               | Fecha de nacimiento                                            |
| email                       | Dirección de correo electrónico                                            |
| unsubscribed_from_emails_at | Fecha de cancelación de suscripción de correos electrónicos                            |
| user_id                     | ID externo                                              |
| first_name                  | Nombre                                               |
| first_session               | Fecha y hora de la primera sesión                           |
| gender                      | Género                                                   |
| google_ad_ids               | ID de publicidad de Google asociados al usuario                      |
| city                        | Ciudad                                     |
| IDFAs                       | Valores del identificador para publicidad (IDFA)                 |
| IDFVs                       | Valores del identificador de proveedor (IDFV)                      |
| language                    | Idioma en la norma ISO-639-1                                        |
| last_app_version_used       | Última versión de la aplicación utilizada                             |
| last_name                   | Apellido                                                |
| last_session                | Fecha y hora de la última sesión                            |
| number_of_google_ad_ids     | Recuento de ID de publicidad de Google asociados               |
| number_of_IDFAs             | Recuento de IDFA asociados                                |
| number_of_IDFVs             | Recuento de IDFV asociados                                |
| number_of_push_tokens       | Recuento de tokens de notificación push asociados             |
| number_of_roku_ad_ids       | Recuento de ID de publicidad de Roku asociados                 |
| number_of_windows_ad_ids    | Recuento de ID de publicidad de Windows asociados              |
| phone_number                | Número de teléfono                                             |
| opted_into_push_at          | Fecha de adhesión voluntaria a las notificaciones push                       |
| unsubscribed_from_push_at   | Fecha de baja de las notificaciones push                |
| random_bucket               | Número de contenedor aleatorio                                 |
| roku_ad_ids                 | ID de publicidad de Roku                          |
| session_count               | Número total de sesiones                                 |
| timezone                    | Zona horaria del usuario en el mismo formato que la base de datos de zonas horarias de IANA                                         |
| in_app_purchase_total       | Importe total gastado en compras dentro de la aplicación                   |
| user_aliases                | Alias de usuario, en su caso                                          |
| windows_ad_ids              | ID de publicidad de Windows                       |
| Eventos personalizados               | Basado en la selección en la exportación                             |
| Atributos personalizados           | Basado en la selección en la exportación                             |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CSV export user data" }

{% alert note %}
Cuando exportas datos de usuario de un paso en Canvas, el CSV incluye a todos los usuarios que han pasado por ese paso durante toda la vida útil del paso en Canvas. No puedes limitar la exportación a un rango de fechas u otra ventana de tiempo. Para saber cómo ejecutar estas exportaciones, consulta [Exportar datos de Canvas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data/).
{% endalert %}

### Exportación de direcciones de correo electrónico a CSV {#csv-export-email-addresses}

| Nombre del campo                  | Descripción            |
| --------------------------- | ---------------------- |
| user_id                     | ID externo del usuario     |
| first_name                  | Nombre             |
| last_name                   | Apellido              |
| email                       | Correo electrónico                  |
| unsubscribed_from_emails_at | Fecha de cancelación de suscripción de correos electrónicos |
| opted_in_to_emails_at       | Fecha de adhesión voluntaria a correos electrónicos      |
| user_aliases                | Alias de usuario, en su caso   |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CSV Export Email Addresses" }

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita nuestro artículo de [solución de problemas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/).
{% endalert %}

{% alert note %}
Los datos de los grupos de suscripción no están disponibles a través de las exportaciones de segmentos. Para identificar usuarios por estado de suscripción, crea un segmento aparte basado en la pertenencia a un grupo de suscripción y exporta ese segmento.
{% endalert %}

## Exportar segmentos grandes {#exporting-large-segments}

Existen varios métodos para exportar un segmento grande de usuarios que contenga más de 500 000 usuarios.

{% tabs %}
{% tab Múltiples segmentos %}

Puedes dividir un segmento grande en segmentos más pequeños y luego exportar cada uno de los segmentos más pequeños desde Braze.

{% endtab %}
{% tab Números de contenedor aleatorios %}

También puedes utilizar [números de contenedor aleatorios]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/) para dividir tu base de usuarios en varios segmentos, y combinarlos después de la exportación. Por ejemplo, si necesitas dividir tu segmento en dos segmentos diferentes, puedes hacerlo con los siguientes filtros:
- Segmento 1: El número de contenedor aleatorio es inferior a 5000 (incluye 0-4999)
- Segmento 2: El número de contenedor aleatorio es superior a 4999 (incluye 5000-9999)

{% endtab %}
{% tab Puntos de conexión %}

También puedes aprovechar los siguientes puntos de conexión para exportar datos de usuario de un segmento específico. Ten en cuenta que estos puntos de conexión están sujetos a límites de datos y [límites de velocidad]({{site.baseurl}}/api/basics/).
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

Si has vinculado tus [credenciales de Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration), las exportaciones grandes se pueden entregar en tu contenedor, además del enlace de descarga enviado por correo electrónico, como se describe en [Detalles de la exportación CSV de segmentos](#segment-csv-export-details).

{% endtab %}
{% endtabs %}