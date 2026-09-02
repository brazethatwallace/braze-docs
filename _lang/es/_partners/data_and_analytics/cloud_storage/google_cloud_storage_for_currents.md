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
Si vas a cambiar de proveedor de almacenamiento en el cloud, ponte en contacto con tu CSM de Braze para que te ayude a configurar y validar tu nueva integración.
{% endalert %}

La integración de Braze y Google Cloud Storage te permite transmitir datos de Currents a Google Cloud Storage. Posteriormente, puedes utilizar un proceso ETL (ETL) para transferir tus datos a otras ubicaciones, como Google BigQuery.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Google Cloud Storage | Se requiere una cuenta de Google Cloud Storage para aprovechar esta integración. |
| Currents | Para exportar datos de vuelta a Google Cloud Storage, necesitas tener [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) configurado para tu cuenta. Currents no es necesario si solo estás configurando el archivado de mensajes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Para integrarte con Google Cloud Storage, debes configurar las credenciales adecuadas que permitan a Braze obtener información sobre los contenedores de almacenamiento en los que se escribe (`storage.buckets.get`) y crear objetos dentro de ese contenedor (`storage.objects.create`).

{% alert note %}
Workload Identity Federation (WIF) no es compatible como método de autenticación para Currents. Debes utilizar una cuenta de servicio con una clave privada JSON.
{% endalert %}

Esto se puede hacer siguiendo las instrucciones a continuación, que te guiarán para crear un rol y una cuenta de servicio que generará una clave privada para usar en tu integración de Currents.

### Paso 1: Crear un rol {#step-1-create-role}

Crea un nuevo rol en tu consola de Google Cloud Platform navegando a **IAM & admin** > **Roles** > **+ Create Role**.

![Página de roles de IAM de Google Cloud con la acción Crear rol.]({% image_buster /assets/img/gcs1.png %})

Dale un nombre al rol, luego selecciona **+Add Permissions** y elige los siguientes:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

{% alert note %}
El permiso `storage.objects.delete` es opcional. Permite a Braze limpiar archivos incompletos.<br><br>En circunstancias excepcionales, Google Cloud puede terminar las conexiones antes de tiempo, lo que provoca que Braze escriba archivos incompletos en Google Cloud Storage. En la mayoría de los casos, Braze reintentará y creará un nuevo archivo con los datos correctos, dejando el archivo antiguo en Google Cloud Storage.
{% endalert %}

{% alert important %}
Si tu contenedor utiliza [espacio de nombres jerárquico](https://cloud.google.com/storage/docs/hns-overview), también debes añadir el permiso `storage.folders.create`. En estos contenedores, las carpetas son recursos gestionados, por lo que Braze necesita este permiso para crear la estructura de carpetas de tus archivos exportados. Sin él, Braze no puede escribir en el contenedor y la integración no logra exportar datos.
{% endalert %}

Cuando hayas terminado, selecciona **Create**.

![Editor de roles personalizados de Google Cloud con permisos de almacenamiento seleccionados.]({% image_buster /assets/img/gcs2.png %})

### Paso 2: Crear una nueva cuenta de servicio {#step-2-create-a-new-service-account}

#### Paso 2.1: Crear la cuenta de servicio {#step-21-create-the-service-account}

Crea una nueva cuenta de servicio en tu consola de Google Cloud Platform navegando a **IAM & admin** > **Service Accounts** y seleccionando **Create Service Account**.

![Página de cuentas de servicio de Google Cloud con Crear cuenta de servicio seleccionado.]({% image_buster /assets/img/gcs3.png %})

A continuación, dale un nombre a la cuenta de servicio y concédele acceso a tu rol personalizado recién creado.

![En Google Cloud Platform, en la página de creación de servicios, escribe el nombre de tu rol en el campo "Select a Role".]({% image_buster /assets/img/gcs4.png %})

#### Paso 2.2: Crear una clave {#step-22-create-a-key}

En la parte inferior de la página, usa el botón **Create Key** para crear una clave privada **JSON** para usar en Braze. Una vez creada la clave, se descargará en tu máquina.

![Diálogo de creación de clave de cuenta de servicio de Google Cloud configurado con tipo de clave JSON.]({% image_buster /assets/img/gcs5.png %})

### Paso 3: Configurar Currents en Braze {#step-3-set-up-currents-in-braze}

En Braze, navega a **Currents** > **+ Create Current** > **Google Cloud Storage Data Export** y proporciona el nombre de tu integración y el correo electrónico de contacto.

{% multi_lang_include currents/contact_email_notifications.md %}

A continuación, sube tu clave privada JSON en **GCS JSON Credentials** y proporciona el nombre de tu contenedor GCS y el prefijo GCS (opcional). Ten en cuenta que debes generar estas credenciales a través de Google Cloud Platform, como se describe en los pasos anteriores.

{% alert important %}
Es importante mantener tu archivo de credenciales actualizado; si las credenciales de tu conector caducan, el conector dejará de enviar eventos. Si esto persiste durante más de **5 días**, los eventos del conector se descartarán y los datos se perderán permanentemente.
{% endalert %}

![La página de Currents de Google Cloud Storage en Braze. En esta página existen campos para el nombre de la integración, correo electrónico de contacto, credencial JSON de GCS, nombre del contenedor GCS y prefijo.]({% image_buster /assets/img/gcs6.png %})

Por último, desplázate hasta la parte inferior de la página y selecciona qué eventos de participación de mensajes o eventos de comportamiento del cliente deseas exportar. Cuando hayas terminado, lanza tu Current.

### Paso 4: Configurar las exportaciones de Google Cloud Storage {#step-4-set-up-google-cloud-storage-exports}

Para configurar las exportaciones de Google Cloud Storage (GCS), ve a **Technology Partners** > **Google Cloud Storage**, introduce tus credenciales de GCS y selecciona **Make this the default data export destination**.

Ten en cuenta que la organización y el contenido de los archivos exportados serán idénticos en las integraciones de AWS S3, Microsoft Azure y Google Cloud Storage.

{% alert important %}
Asegúrate de introducir el valor JSON completo que es [generado por Google Cloud](https://cloud.google.com/iam/docs/keys-create-delete).
{% endalert %}

![La página de Google Cloud Storage en el panel de Braze.]({% image_buster /assets/img/gcs7.png %}){: style="max-width:70%;"}

### Paso 5: Probar las credenciales de tu cuenta de servicio (opcional) {#step-5-test-your-service-account-credentials-optional}

Tu cuenta de servicio de IAM de Google Cloud debe tener los siguientes permisos:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Para verificar estos permisos en el panel de Braze, ve a la página de **Google Cloud Storage** y selecciona **Test Credentials**.

![La sección de credenciales de Google Cloud Storage en el panel de Braze.]({% image_buster /assets/img/gcs8.png %}){: style="max-width:70%;"}

## Comportamiento de exportación {#export-behavior}

Los usuarios que hayan integrado una solución de almacenamiento de datos en el cloud e intenten exportar API, informes del panel o informes CSV experimentarán lo siguiente:

- Todas las exportaciones de API no devolverán una URL de descarga en el cuerpo de la respuesta y deben recuperarse a través del almacenamiento de datos.
- Todos los informes del panel e informes CSV se enviarán al correo electrónico del usuario para su descarga (no se requieren permisos de almacenamiento) y se respaldarán en el almacenamiento de datos.

{% alert important %}
**Requisito de formato JSON**: Para las exportaciones JSON, Braze utiliza el formato JSONL (JSON delimitado por saltos de línea), donde cada línea contiene un objeto JSON independiente. Este formato difiere del JSON estándar, que es un único array u objeto JSON. Cada línea del archivo exportado es un objeto JSON válido, pero el archivo en su conjunto no es un único documento JSON válido. Al procesar estos archivos, analiza cada línea individualmente como un objeto JSON independiente en lugar de intentar analizar el archivo completo como un único documento JSON.

Las exportaciones de Currents utilizan el formato Apache Avro (archivos `.avro`), no JSON. Este requisito de formato JSON se aplica a las exportaciones de datos del panel y a las exportaciones de API que utilizan formato JSON.
{% endalert %}

## Solución de problemas {#troubleshooting}

### Las credenciales de Google Cloud Storage no son válidas {#google-cloud-storage-credentials-are-invalid}

Si recibes el siguiente error al intentar introducir tus credenciales:

```
Google Cloud Storage Credentials are invalid. Please ensure that your credentials string, bucket name, and prefix are valid. You do not have read permission.
```

Asegúrate de que tu cuenta de servicio de Google Cloud IAM tenga los siguientes permisos:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Después de verificarlo, puedes [probar tus credenciales en el panel de Braze](#step-5-test-your-service-account-credentials-optional).