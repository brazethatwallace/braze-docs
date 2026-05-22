---
nav_title: Google Cloud Storage
article_title: Google Cloud Storage
alias: /partners/google_cloud_storage_for_currents/
description: "Este artículo de referencia describe la asociación entre Braze y Google Cloud Storage, un almacenamiento de objetos masivamente escalable para datos no estructurados."
page_type: partner
tool: Currents
search_tag: Partner

---

# Google Cloud Storage

> [Google Cloud Storage](https://cloud.google.com/storage/) es un sistema de almacenamiento de objetos masivo y escalable para datos no estructurados ofrecido por Google como parte de la línea de productos Cloud Computing.

{% alert important %}
Si vas a cambiar de proveedor de almacenamiento en la nube, ponte en contacto con tu administrador del éxito del cliente de Braze para que te ayude a configurar y validar tu nueva integración.
{% endalert %}

La integración de Braze y Google Cloud Storage te permite transmitir datos de Currents a Google Cloud Storage. Posteriormente, puedes utilizar un proceso ETL (extraer, transformar, cargar) para transferir tus datos a otras ubicaciones, como Google BigQuery.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Google Cloud Storage | Se necesita una cuenta de Google Cloud Storage para beneficiarse de esta asociación. |
| Currents | Para volver a exportar datos a Google Cloud Storage, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) en tu cuenta. Currents no es necesario si solo estás configurando el archivado de mensajes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración {#integration}

Para integrarte con Google Cloud Storage, debes configurar las credenciales adecuadas que permitan a Braze obtener información sobre los contenedores de almacenamiento en los que se está escribiendo (`storage.buckets.get`) y crear objetos dentro de ese contenedor (`storage.objects.create`).

{% alert note %}
Workload Identity Federation (WIF) no es compatible como método de autenticación para Currents. Debes utilizar una cuenta de servicio con una clave privada JSON.
{% endalert %}

Para ello, sigue las siguientes instrucciones, que te guiarán a través de la creación de un rol y una cuenta de servicio que generarán una clave privada para utilizarla en tu integración de Currents.

### Paso 1: Crear rol {#step-1-create-role}

Crea un nuevo rol en tu consola de Google Cloud Platform accediendo a **IAM & admin** > **Roles** > **+ Create Role**.

![]({% image_buster /assets/img/gcs1.png %})

Dale un nombre al rol, luego selecciona **+Add Permissions** y elige lo siguiente:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

{% alert note %}
El permiso `storage.objects.delete` es opcional. Permite a Braze limpiar los archivos incompletos.<br><br>En raras circunstancias, Google Cloud puede finalizar las conexiones antes de tiempo, lo que provoca que Braze escriba archivos incompletos en Google Cloud Storage. En la mayoría de los casos, Braze volverá a intentarlo y creará un nuevo archivo con los datos correctos, dejando el archivo antiguo en Google Cloud Storage.
{% endalert %}

Cuando hayas terminado, selecciona **Create**.

![]({% image_buster /assets/img/gcs2.png %})

### Paso 2: Crear una nueva cuenta de servicio {#step-2-create-a-new-service-account}

#### Paso 2.1: Crear la cuenta de servicio {#step-21-create-the-service-account}

Crea una nueva cuenta de servicio en tu consola de Google Cloud Platform accediendo a **IAM & admin** > **Service Accounts** y seleccionando **Create Service Account**.

![]({% image_buster /assets/img/gcs3.png %})

A continuación, asigna un nombre a la cuenta de servicio y concédele acceso al rol personalizado que acabas de crear.

![En Google Cloud Platform, en la página de creación de servicios, escribe el nombre de tu rol en el campo "Select a Role".]({% image_buster /assets/img/gcs4.png %})

#### Paso 2.2: Crear una clave {#step-22-create-a-key}

En la parte inferior de la página, utiliza el botón **Create Key** para crear una clave privada **JSON** y utilizarla en Braze. Una vez creada la clave, se descargará en tu máquina.

![]({% image_buster /assets/img/gcs5.png %})

### Paso 3: Configurar Currents en Braze {#step-3-set-up-currents-in-braze}

En Braze, ve a **Currents** > **+ Create Current** > **Google Cloud Storage Data Export** e indica tu nombre de integración y tu correo electrónico de contacto.

A continuación, sube tu clave privada JSON en **GCS JSON Credentials** e indica tu nombre de contenedor GCS y el prefijo GCS (opcional). Ten en cuenta que debes generar estas credenciales a través de Google Cloud Platform, como se describe en los pasos anteriores.

{% alert important %}
Es importante que mantengas actualizado tu archivo de credenciales; si las credenciales de tu conector caducan, el conector dejará de enviar eventos. Si esto persiste durante más de **5 días**, los eventos del conector se eliminarán y los datos se perderán permanentemente.
{% endalert %}

![La página de Google Cloud Storage Currents en Braze. En esta página existen campos para el nombre de la integración, el correo electrónico de contacto, la credencial JSON de GCS, el nombre de contenedor de GCS y el prefijo.]({% image_buster /assets/img/gcs6.png %})

Por último, desplázate hasta la parte inferior de la página y selecciona los eventos de interacción con mensajes o los eventos de comportamiento del cliente que deseas exportar. Cuando hayas terminado, lanza tu Current.

### Paso 4: Configurar las exportaciones de Google Cloud Storage {#step-4-set-up-google-cloud-storage-exports}

Para configurar las exportaciones de Google Cloud Storage (GCS), ve a **Socios tecnológicos** > **Google Cloud Storage**, introduce tus credenciales de GCS y selecciona **Make this the default data export destination**.

Ten en cuenta que la organización y el contenido de los archivos exportados serán idénticos en todas las integraciones de AWS S3, Microsoft Azure y Google Cloud Storage.

{% alert important %}
Asegúrate de introducir el valor JSON completo [generado por Google Cloud](https://cloud.google.com/iam/docs/keys-create-delete).
{% endalert %}

![La página de Google Cloud Storage en el panel de Braze.]({% image_buster /assets/img/gcs7.png %}){: style="max-width:70%;"}

### Paso 5: Comprueba las credenciales de tu cuenta de servicio (opcional) {#step-5-test-your-service-account-credentials-optional}

Tu cuenta del servicio IAM de Google Cloud debe tener los siguientes permisos:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Para verificar estos permisos en el panel de Braze, ve a la página **Google Cloud Storage** y, a continuación, selecciona **Test Credentials**.

![La sección de credenciales de Google Cloud Storage en el panel de Braze.]({% image_buster /assets/img/gcs8.png %}){: style="max-width:70%;"}

## Comportamiento de la exportación {#export-behavior}

Los usuarios que hayan integrado una solución de almacenamiento en la nube y estén intentando exportar API, informes del dashboard o informes CSV experimentarán lo siguiente:

- Todas las exportaciones de la API no devolverán una URL de descarga en el cuerpo de la respuesta y deberán recuperarse a través del almacenamiento de datos.
- Todos los informes del dashboard y los informes CSV se enviarán al correo electrónico del usuario para su descarga (sin necesidad de permisos de almacenamiento) y se realizará una copia de seguridad en el almacenamiento de datos.

{% alert important %}
**Requisito de formato JSON**: Para las exportaciones JSON, Braze utiliza el formato JSONL (JSON delimitado por nuevas líneas), en el que cada línea contiene un objeto JSON independiente. Este formato difiere del JSON estándar, que es una única matriz u objeto JSON. Cada línea del archivo exportado es un objeto JSON válido, pero el archivo en su conjunto no es un único documento JSON válido. Al procesar estos archivos, analiza cada línea individualmente como un objeto JSON distinto, en lugar de intentar analizar todo el archivo como un único documento JSON.

Las exportaciones de Currents utilizan el formato Apache Avro (archivos `.avro`), no JSON. Este requisito de formato JSON se aplica a las exportaciones de datos del dashboard y a las exportaciones de API que utilizan el formato JSON.
{% endalert %}

## Solución de problemas {#troubleshooting}

### Las credenciales de Google Cloud Storage no son válidas {#google-cloud-storage-credentials-are-invalid}

Si recibes el siguiente error al intentar introducir tus credenciales:

```
Google Cloud Storage Credentials are invalid. Please ensure that your credentials string, bucket name, and prefix are valid. You do not have read permission.
```

Asegúrate de que tu cuenta del servicio IAM de Google Cloud tiene los siguientes permisos:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Tras la verificación, puedes [comprobar tus credenciales en el panel de Braze](#step-5-test-your-service-account-credentials-optional).