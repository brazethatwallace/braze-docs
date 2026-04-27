---
nav_title: Datos de Segment
article_title: Exportar datos de Segment
page_order: 4
page_type: reference
description: "Este artículo de referencia explica cómo exportar datos de Segment a CSV."

---

# Exportar datos de Segment a CSV

> Esta página explica cómo solicitar una exportación CSV de los datos de usuario de un Segment, y los datos incluidos en la exportación.

Para exportar los datos de un Segment a un CSV, selecciona el menú desplegable **User Data** mientras editas un Segment y elige exportar los datos de usuario o las direcciones de correo electrónico del Segment.

![Sección Detalles del Segment con el desplegable User Data que muestra las opciones de exportación.]({% image_buster /assets/img_archive/csvexport.png %})

También puedes solicitar una exportación CSV desde la página principal de **Segments** seleccionando el desplegable <i class="fas fa-gear"></i> **Settings** para un Segment:

![Desplegable de configuración en la página principal de Segments.]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
Para exportar los datos de todos tus perfiles de usuario, crea un Segment sin filtros y, a continuación, solicita una exportación CSV.
{% endalert %}

La salida CSV contiene los datos de cada perfil de usuario capturado en el Segment en el momento de la exportación. Puedes exportar cualquier Segment seleccionando el ícono de engranaje y la exportación CSV. Braze generará el informe en segundo plano y lo enviará por correo electrónico al usuario que esté conectado en ese momento.

{% alert important %}
Debido a las restricciones de tamaño de los archivos, la exportación puede fallar si el tamaño estimado de tu Segment es superior a 500 000 usuarios. Ten en cuenta que esta restricción utiliza el tamaño estimado de tu Segment, y no el cálculo exacto. Para más detalles, consulta [Exportar Segments grandes](#exporting-large-segments).
{% endalert %}

Si has vinculado tus [credenciales de Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration) a Braze, el CSV se cargará en tu contenedor de S3 con la clave `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip`. Debes haber iniciado sesión en el dashboard para acceder al enlace de descarga que se te ha enviado por correo electrónico.

{% multi_lang_include alerts/important_alerts.md alert='S3 file bucket export' %}

## Datos incluidos en la exportación

Dependiendo de tu selección, tu exportación incluirá lo siguiente.

### Exportación de datos de usuario a CSV

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
{: .reset-td-br-1 .reset-td-br-2 }

### Exportación de direcciones de correo electrónico a CSV

| Nombre del campo                  | Descripción            |
| --------------------------- | ---------------------- |
| user_id                     | ID externo del usuario     |
| first_name                  | Nombre             |
| last_name                   | Apellido              |
| email                       | Correo electrónico                  |
| unsubscribed_from_emails_at | Fecha de cancelación de suscripción de correos electrónicos |
| opted_in_to_emails_at       | Fecha de adhesión voluntaria a correos electrónicos      |
| user_aliases                | Alias de usuario, en su caso   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita nuestro artículo de [solución de problemas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/).
{% endalert %}

## Exportar Segments grandes {#exporting-large-segments}

Existen varios métodos para exportar un Segment grande de usuarios que contenga más de 500 000 usuarios.

{% tabs %}
{% tab Múltiples Segments %}

Puedes dividir un Segment grande en Segments más pequeños y luego exportar cada uno de los Segments más pequeños desde Braze.

{% endtab %}
{% tab Números de contenedor aleatorios %}

También puedes utilizar [números de contenedor aleatorios]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/) para dividir tu base de usuarios en varios Segments, y combinarlos después de la exportación. Por ejemplo, si necesitas dividir tu Segment en dos Segments diferentes, puedes hacerlo con los siguientes filtros:
- Segment 1: El número de contenedor aleatorio es inferior a 5000 (incluye 0-4999)
- Segment 2: El número de contenedor aleatorio es superior a 4999 (incluye 5000-9999)

{% endtab %}
{% tab Puntos de conexión %}

También puedes aprovechar los siguientes puntos de conexión para exportar datos de usuario de un Segment específico. Ten en cuenta que estos puntos de conexión están sujetos a límites de datos.
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

{% endtab %}
{% endtabs %}