---
nav_title: Integraciones de almacenamiento de archivos
article_title: Integraciones de almacenamiento de archivos
description: "Esta página trata sobre la ingesta de datos en el cloud de Braze y cómo sincronizar datos relevantes de Amazon S3 o Google Cloud Storage con Braze."
page_order: 4
page_type: reference

---

# Integraciones de almacenamiento de archivos {#file-storage-integrations}

> Esta página explica cómo configurar la ingesta de datos en el cloud para sincronizar datos de Amazon S3 o Google Cloud Storage con Braze.

## Cómo funciona {#how-it-works}

Puedes usar la ingesta de datos en el cloud (CDI) para integrar directamente uno o más contenedores de almacenamiento en tu cuenta en el cloud con Braze. Cuando agregas un archivo nuevo a un contenedor, tu proveedor de cloud publica una notificación y la ingesta de datos en el cloud de Braze sincroniza los datos.

El mecanismo de notificación depende de tu proveedor:

- **Amazon S3:** Cuando se publican archivos nuevos en S3, se envía un mensaje a una cola de Amazon Simple Queue Service (SQS), y Braze consume ese mensaje para ingestar el archivo nuevo.
- **Google Cloud Storage (GCS):** Cuando se finalizan archivos nuevos en el contenedor, GCS publica una notificación `OBJECT_FINALIZE` en un tema de Pub/Sub. Braze consume esas notificaciones desde una suscripción de Pub/Sub para ingestar el archivo nuevo.

La ingesta de datos en el cloud es compatible con lo siguiente:

- Archivos JSON
- Archivos CSV
- Archivos Parquet
- Datos de atributos, eventos personalizados, eventos de compra, eliminación de usuarios y catálogos

## Configuración de la ingesta de datos en la nube {#setting-up-cloud-data-ingestion}

Los pasos de configuración dependen de tu proveedor de almacenamiento de archivos. Selecciona la pestaña de tu proveedor y luego completa la configuración compartida en las secciones que siguen.

{% tabs %}
{% tab Amazon S3 %}

La integración requiere los siguientes recursos:

- Contenedor de S3 para almacenamiento de datos
- Cola SQS para notificaciones de nuevos archivos
- Rol IAM para acceso de Braze

### Definiciones de AWS {#aws-definitions}

| Término | Definición |
| --- | --- |
| Amazon Resource Name (ARN) | El ARN es un identificador único para los recursos de AWS. |
| Identity and Access Management (IAM) | IAM es un servicio web que te permite controlar de forma segura el acceso a los recursos de AWS. En este tutorial, crea una política IAM y asígnala a un rol IAM para integrar tu contenedor de S3 con la ingesta de datos en la nube de Braze. |
| Amazon Simple Queue Service (SQS) | SQS es una cola alojada que te permite integrar sistemas y componentes de software distribuidos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definiciones de AWS" }

## Configuración de la ingesta de datos en la nube en AWS {#setting-up-cloud-data-ingestion-in-aws}

### Paso 1: Crear un contenedor de origen {#step-1-create-a-source-bucket}

Crea un contenedor de S3 de uso general con la configuración predeterminada en tu cuenta de AWS. Los contenedores de S3 se pueden reutilizar en distintas sincronizaciones siempre que la carpeta sea única.

La configuración predeterminada es:

- ACL deshabilitadas
- Bloquear todo el acceso público
- Deshabilitar el versionado del contenedor
- Cifrado SSE-S3
  - SSE-S3 es el único tipo de cifrado del lado del servidor compatible. El cifrado con Amazon KMS no es compatible.

Toma nota de la región en la que creaste el contenedor, ya que crearás una cola SQS en la misma región en el siguiente paso.

### Paso 2: Crear una cola SQS {#step-2-create-sqs-queue}

Crea una cola SQS para rastrear cuándo se añaden objetos al contenedor que has creado. Usa la configuración predeterminada por ahora.

Una cola SQS debe ser única a nivel global (por ejemplo, solo se puede usar una para una sincronización de CDI y no se puede reutilizar en otro espacio de trabajo).

{% alert important %}
Asegúrate de crear esta cola SQS en la misma región en la que creaste el contenedor.
{% endalert %}

Toma nota del ARN y la URL de la cola SQS, ya que los necesitarás con frecuencia durante esta configuración.

![Selección de "Advanced" con un ejemplo de objeto JSON para definir quién puede acceder a una cola.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### Paso 3: Configurar la política de acceso {#step-3-set-up-access-policy}

Para configurar la política de acceso, elige **Opciones avanzadas**.

Añade la siguiente declaración a la política de acceso de la cola, teniendo cuidado de reemplazar `YOUR-BUCKET-NAME-HERE` con el nombre de tu contenedor, `YOUR-SQS-ARN` con el ARN de tu cola SQS y `YOUR-AWS-ACCOUNT-ID` con tu ID de cuenta de AWS:

``` json
{
  "Sid": "braze-cdi-s3-sqs-publish",
  "Effect": "Allow",
  "Principal": {
    "Service": "s3.amazonaws.com"
  },
  "Action": "SQS:SendMessage",
  "Resource": "YOUR-SQS-ARN",
  "Condition": {
    "StringEquals": {
      "aws:SourceAccount": "YOUR-AWS-ACCOUNT-ID"
    },
    "ArnLike": {
      "aws:SourceArn": "arn:aws:s3:::YOUR-BUCKET-NAME-HERE"
    }
  }
}
```

### Paso 4: Añadir una notificación de eventos al contenedor de S3 {#step-4-add-an-event-notification-to-the-s3-bucket}

1. En el contenedor creado en el paso 1, ve a **Properties** > **Event notifications**.
2. Dale un nombre a la configuración. Opcionalmente, especifica un prefijo o sufijo de destino si solo quieres que Braze ingiera un subconjunto de archivos.
3. En **Destination**, selecciona **SQS queue** y proporciona el ARN de la cola SQS que creaste en el paso 2.

{% alert note %}
Si subes tus archivos a la carpeta raíz de un contenedor de S3 y luego mueves algunos de los archivos a una carpeta específica dentro del contenedor, es posible que encuentres un error inesperado. En su lugar, puedes cambiar las notificaciones de eventos para que se envíen solo para los archivos en el prefijo, evitar colocar archivos en el contenedor de S3 fuera de ese prefijo, o actualizar la integración sin prefijo, lo que entonces ingiere todos los archivos.
{% endalert %}

### Paso 5: Crear una política IAM {#step-5-create-an-iam-policy}

Crea una política IAM para permitir que Braze interactúe con tu contenedor de origen. Para empezar, inicia sesión en la consola de administración de AWS como administrador de la cuenta.

1. Ve a la sección IAM de la consola de AWS, selecciona **Policies** en la barra de navegación y luego selecciona **Create Policy**.<br><br>![El botón "Create policy" en la consola de AWS.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. Abre la pestaña **JSON** e introduce el siguiente fragmento de código en la sección **Policy Document**, teniendo cuidado de reemplazar `YOUR-BUCKET-NAME-HERE` con el nombre de tu contenedor y `YOUR-SQS-ARN-HERE` con el nombre de tu cola SQS:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE/*"]
        },
        {
            "Effect": "Allow",
            "Action": [
                "sqs:DeleteMessage",
                "sqs:GetQueueUrl",
                "sqs:ReceiveMessage",
                "sqs:GetQueueAttributes"
            ],
            "Resource": "YOUR-SQS-ARN-HERE"
        }
    ]
}

```

{: start="3"}
3. Selecciona **Review Policy** cuando hayas terminado.

4. Dale un nombre y una descripción a la política, y luego selecciona **Create Policy**.

![Un ejemplo de política llamada "new-policy-name".]({% image_buster /assets/img/create_policy_3_name.png %})

![El campo de descripción de la política.]({% image_buster /assets/img/create_policy_4_created.png %})

### Paso 6: Crear un rol IAM {#step-6-create-an-iam-role}

Para completar la configuración en AWS, crea un rol IAM y adjúntale la política IAM del paso 5.

1. Dentro de la misma sección IAM de la consola donde creaste la política IAM, ve a **Roles** > **Create Role**.

![El botón "Create role".]({% image_buster /assets/img/create_role_1_list.png %})

{: start="2"}
2. En AWS, selecciona **Another AWS Account** como tipo de SELECTOR de entidad de confianza. Proporciona tu ID de cuenta de Braze. Selecciona la casilla **Require external ID**.
3. En Braze, ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Orígenes**, selecciona **Añadir origen de datos** y selecciona **Amazon S3** en la sección de orígenes de archivos.
4. Copia el **ID de cuenta de Braze** generado automáticamente.

![La página "Añadir nuevo origen" que muestra las secciones de nombre del origen y detalles de conexión de S3.]({% image_buster /assets/img/braze_account_id.png %})

{: start="6"}
5. En AWS, pega el ID de cuenta y luego selecciona **Next**.

![La página "Create Role" de S3. Esta página tiene campos para el nombre del rol, la descripción del rol, las entidades de confianza, las políticas y el límite de permisos.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="7"}
6. Adjunta la política creada en el paso 4 al rol. Busca la política en la barra de búsqueda y selecciona la marca de verificación junto a la política para adjuntarla. Selecciona **Next** cuando hayas terminado.

![ARN del rol con new-policy-name seleccionada.]({% image_buster /assets/img/create_role_3_attach.png %})

Dale un nombre y una descripción al rol, y selecciona **Create Role**.

![Un ejemplo de rol llamado "new-role-name".]({% image_buster /assets/img/create_role_4_name.png %})

{: start="8"}
7. Toma nota del ARN del rol que creaste y del ID externo que generaste, ya que los necesitarás para crear la integración de ingesta de datos en la nube.

## Configuración de la ingesta de datos en la nube en Braze {#setting-up-cloud-data-ingestion-in-braze}

1. Primero, crea un nuevo origen en el panel de Braze. Ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Orígenes**, selecciona **Añadir origen de datos** y luego selecciona **Amazon S3**.
2. Elige un nombre para tu origen e introduce la información del proceso de configuración de AWS para crear un nuevo origen. Especifica lo siguiente:

  - ARN del rol
  - ID externo
  - Nombre del contenedor
  - Región

![La sección de detalles de conexión de S3 que muestra los campos de credenciales (configuración de AWS y configuración de Braze) y configuración.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. Selecciona **Probar conexión** para confirmar que Braze puede acceder a tu contenedor. Después de una prueba exitosa, selecciona **Conectar al origen**. Si la conexión falla, aparece un mensaje de error para ayudarte a solucionar el problema.

{: start="4"}
4. A continuación, crea una nueva sincronización. Ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Sincronizaciones** y selecciona **Crear sincronización de datos**.

{: start="5"}
5. Elige un nombre para tu sincronización. Luego, selecciona cualquier origen de S3 activo e introduce tu tabla de origen para la sincronización. Selecciona un tipo de datos y selecciona **Probar conexión**.

![Una opción para probar la conexión con una vista previa de los datos.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. Introduce la información restante del proceso de configuración de AWS. Especifica lo siguiente:
- URL de SQS (debe ser única para cada nueva integración)
- Ruta de la carpeta (opcional, debe ser única en todas las sincronizaciones de un espacio de trabajo)

7. Selecciona un tipo de datos y selecciona **Probar conexión** para confirmar que Braze puede listar los archivos disponibles para ingerir (no los datos dentro de esos archivos). Una vez exitoso, selecciona **Siguiente: Notificaciones**.
8. Añade correo(s) electrónico(s) de contacto para notificaciones si la sincronización se interrumpe por problemas de acceso o permisos. Opcionalmente, activa las notificaciones para errores a nivel de usuario y sincronizaciones exitosas.
9. Crea la sincronización.

{% endtab %}
{% tab Google Cloud Storage %}

La integración requiere los siguientes recursos:

- Un contenedor de Cloud Storage para almacenamiento de datos
- Un tema y una suscripción de Pub/Sub para notificaciones de nuevos archivos
- Una cuenta de servicio cuya clave JSON subes a Braze

### Definiciones de GCP {#gcp-definitions}

| Término | Definición |
| --- | --- |
| Proyecto de Google Cloud | Un proyecto organiza todos tus recursos de Google Cloud y se identifica mediante un ID de proyecto y un número de proyecto únicos. |
| Contenedor de Cloud Storage | Un contenedor es el recipiente que almacena los archivos de datos que quieres que Braze ingiera. |
| Tema de Pub/Sub | Un tema es el recurso con nombre que recibe notificaciones de nuevos archivos de tu contenedor de Cloud Storage. |
| Suscripción de Pub/Sub | Una suscripción se conecta a un tema y entrega sus mensajes. Braze consume notificaciones de nuevos archivos desde una suscripción de tipo pull. |
| Cuenta de servicio | Una cuenta de servicio es una identidad no humana que Braze usa para acceder a tu contenedor y suscripción. Subes su clave JSON a Braze. |
| Rol IAM | Un rol de Identity and Access Management (IAM) es una colección de permisos que asignas a la cuenta de servicio en tu contenedor y suscripción. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definiciones de GCP" }

## Configuración de la ingesta de datos en la nube en Google Cloud {#setting-up-cloud-data-ingestion-in-google-cloud}

### Paso 1: Crear un contenedor de Cloud Storage {#step-1-create-a-cloud-storage-bucket}

En la consola de Google Cloud, ve a **Cloud Storage** > **Buckets** > **Create**. Toma nota del ID del proyecto y del nombre del contenedor, ya que los necesitarás cuando configures el origen en Braze. Recomendamos habilitar el acceso uniforme a nivel de contenedor para que los permisos se gestionen con IAM.

Alternativamente, crea el contenedor con gcloud:

```shell
gcloud storage buckets create gs://YOUR-BUCKET-NAME \
  --project=YOUR-PROJECT-ID \
  --location=YOUR-REGION \
  --uniform-bucket-level-access
```

### Paso 2: Crear un tema y una suscripción de Pub/Sub {#step-2-create-a-pubsub-topic-and-subscription}

En la consola de Google Cloud, ve a **Pub/Sub** > **Topics** > **Create topic**. Puedes dejar que Google cree una suscripción predeterminada o crear una por separado. Luego, crea una suscripción de tipo **pull** en ese tema.

Alternativamente, usa gcloud:

```shell
gcloud pubsub topics create YOUR-TOPIC --project=YOUR-PROJECT-ID
gcloud pubsub subscriptions create YOUR-SUBSCRIPTION \
  --topic=YOUR-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
```

Toma nota del **ID de suscripción**: Braze necesita la suscripción (no el tema) cuando creas la sincronización. La suscripción debe ser de tipo pull.

{% alert warning %}
No configures una cola de mensajes no entregados en esta suscripción. Braze no admite colas de mensajes no entregados para suscripciones de ingesta de datos en la nube. Para obtener más información, consulta [Dead-letter topics](https://cloud.google.com/pubsub/docs/dead-letter-topics) en la documentación de Google Cloud.
{% endalert %}

### Paso 3: Enviar notificaciones del contenedor al tema {#step-3-send-bucket-notifications-to-the-topic}

{% alert important %}
La creación de una notificación de Cloud Storage a Pub/Sub no está disponible en la consola de Google Cloud. Debes usar gcloud (como se muestra aquí), Terraform o la API JSON. Para obtener más información, consulta [Configure Pub/Sub notifications for Cloud Storage](https://cloud.google.com/storage/docs/reporting-changes#enabling) en la documentación de Google Cloud.
{% endalert %}

Primero, asigna al agente de servicio de Cloud Storage el permiso para publicar en el tema, luego crea la notificación para `OBJECT_FINALIZE`. El evento `OBJECT_FINALIZE` se dispara cada vez que se crea o finaliza un nuevo objeto en el contenedor.

```shell
# Get the Cloud Storage service agent for your project
gcloud storage service-agent --project=YOUR-PROJECT-ID

# Assign it Pub/Sub Publisher on the topic
gcloud pubsub topics add-iam-policy-binding YOUR-TOPIC \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:service-YOUR-PROJECT-NUMBER@gs-project-accounts.iam.gserviceaccount.com" \
  --role="roles/pubsub.publisher"

# Create the OBJECT_FINALIZE notification (optionally scope to a folder with --object-prefix)
gcloud storage buckets notifications create gs://YOUR-BUCKET-NAME \
  --topic=YOUR-TOPIC \
  --event-types=OBJECT_FINALIZE \
  --payload-format=json
```

Reemplaza los siguientes marcadores de posición en estos comandos:

- `YOUR-PROJECT-ID`: el ID de tu proyecto de Google Cloud, el identificador legible (por ejemplo, `my-gcp-project`).
- `YOUR-TOPIC`: el tema de Pub/Sub que creaste en el [paso 2](#step-2-create-a-pubsub-topic-and-subscription).
- `YOUR-BUCKET-NAME`: el nombre de tu contenedor de Cloud Storage.
- `YOUR-PROJECT-NUMBER`: el número de tu proyecto, el identificador numérico utilizado en la dirección de correo electrónico del agente de servicio de Cloud Storage. Es diferente del ID del proyecto. Puedes encontrarlo en el **Dashboard** de la consola de Google Cloud, o ejecutar el siguiente comando:

```shell
gcloud projects describe YOUR-PROJECT-ID --format="value(projectNumber)"
```

### Paso 4: Crear una cuenta de servicio {#step-4-create-a-service-account}

En la consola de Google Cloud, ve a **IAM & Admin** > **Service Accounts** > **Create service account**.

Alternativamente, usa gcloud:

```shell
gcloud iam service-accounts create braze-cdi-gcs \
  --project=YOUR-PROJECT-ID \
  --display-name="Braze CDI GCS"
```

### Paso 5: Asignar permisos {#step-5-assign-permissions}

El conector necesita exactamente estos permisos: `storage.buckets.get`, `storage.objects.get` y `storage.objects.list` en el contenedor, y `pubsub.subscriptions.consume` en la suscripción. Puedes asignarlos con un rol personalizado o con roles predefinidos.

**Rol personalizado:** crea un rol personalizado con exactamente esos permisos y vincúlalo al contenedor y a la suscripción:

```shell
gcloud iam roles create brazeCdiGcs --project=YOUR-PROJECT-ID \
  --title="Braze CDI GCS" \
  --permissions=storage.buckets.get,storage.objects.get,storage.objects.list,pubsub.subscriptions.consume \
  --stage=GA

gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"

gcloud pubsub subscriptions add-iam-policy-binding YOUR-SUBSCRIPTION \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"
```

**Roles predefinidos:** asigna `roles/storage.objectViewer` y `roles/storage.legacyBucketReader` en el contenedor, y `roles/pubsub.subscriber` en la suscripción. El rol `objectViewer` proporciona `storage.objects.get` y `storage.objects.list`, y `legacyBucketReader` proporciona `storage.buckets.get`:

```shell
gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="roles/storage.objectViewer"
gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="roles/storage.legacyBucketReader"
gcloud pubsub subscriptions add-iam-policy-binding YOUR-SUBSCRIPTION \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="roles/pubsub.subscriber"
```

### Paso 6: Crear una clave JSON {#step-6-create-a-json-key}

En la consola de Google Cloud, abre la cuenta de servicio, ve a **Keys** > **Add key** > **Create new key** y selecciona **JSON**.

Alternativamente, usa gcloud:

```shell
gcloud iam service-accounts keys create braze-cdi-gcs-key.json \
  --iam-account=braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com
```

## Configuración de la ingesta de datos en la nube en Braze

1. En Braze, ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Orígenes**, selecciona **Añadir origen de datos** y luego selecciona **Google Cloud Storage**.

![La pantalla "Añadir nuevo origen" con Google Cloud Storage seleccionado en la lista de orígenes de datos.]({% image_buster /assets/img/cloud_ingestion/gcs_source_picker.png %})

{: start="2"}
2. Completa los campos del origen:
    - **Bucket**: el nombre de tu contenedor
    - **Project ID**: el ID de tu proyecto de GCP
    - **Service account JSON key**: sube el archivo de clave del paso 6 y dale un nombre a la credencial

![El formulario de origen de Google Cloud Storage que muestra los campos de Bucket, Project ID y carga de credenciales.]({% image_buster /assets/img/cloud_ingestion/gcs_source_form.png %})

{: start="3"}
3. Selecciona **Probar conexión** y luego selecciona **Conectar al origen**.
4. Crea una sincronización. Ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Sincronizaciones** y selecciona **Crear sincronización de datos**. Elige un nombre de sincronización y un **tipo de datos** (como **Atributos de usuario**, **Eventos personalizados**, **Eventos de compra**, **Catálogo** o **Eliminar usuarios**), luego selecciona **Siguiente**.
5. En el paso de **Definición de datos**, selecciona tu origen de GCS y luego especifica lo siguiente:
    - **ID de suscripción de Pub/Sub**: el ID de suscripción del paso 2 (no el tema)
    - **Ruta de la carpeta** (opcional): un prefijo de ruta dentro del contenedor (consulta [Sincronizar una carpeta en un contenedor compartido](#syncing-a-folder-in-a-shared-bucket))

![El formulario de sincronización de Google Cloud Storage que muestra los campos de ID de suscripción de Pub/Sub y ruta de la carpeta.]({% image_buster /assets/img/cloud_ingestion/gcs_sync_form.png %})

{: start="6"}
6. Selecciona **Vista previa y validar** para confirmar que Braze puede acceder a la suscripción y listar los archivos disponibles para ingerir. Una prueba exitosa listará los archivos existentes en el contenedor, pero esos archivos no se sincronizarán automáticamente.
7. Añade correo(s) electrónico(s) de contacto para notificaciones de errores. Las sincronizaciones de Google Cloud Storage están basadas en eventos, por lo que no se requiere un horario: Braze ingiere nuevos archivos a medida que se suben. Revisa el resumen y luego selecciona **Crear sincronización**.

### Sincronizar una carpeta en un contenedor compartido {#syncing-a-folder-in-a-shared-bucket}

Puedes reutilizar un contenedor en múltiples sincronizaciones, pero cada sincronización debe apuntar a una carpeta distinta **y** tener su propia suscripción de Pub/Sub dedicada.


{% alert important %}
La ruta de la carpeta y la suscripción deben ser únicas en todas las sincronizaciones de un espacio de trabajo cuando múltiples sincronizaciones comparten el mismo contenedor de origen. Como en el [paso 2](#step-2-create-a-pubsub-topic-and-subscription), no configures una cola de mensajes no entregados en ninguna de estas suscripciones.
{% endalert %}

Para cada carpeta que quieras sincronizar en un contenedor compartido:

1. Establece el campo **Folder** de la sincronización en el prefijo de ruta (por ejemplo, `attributes/`). Braze solo lista e ingiere objetos cuya ruta comience con ese prefijo.
2. Crea un tema dedicado y una notificación con alcance de prefijo para esa carpeta, luego crea una suscripción en ese tema:

    ```shell
    # One topic per folder
    gcloud pubsub topics create YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID

    # Assign the Cloud Storage service agent publisher on the topic
    gcloud pubsub topics add-iam-policy-binding YOUR-ATTRIBUTES-TOPIC \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:service-YOUR-PROJECT-NUMBER@gs-project-accounts.iam.gserviceaccount.com" \
      --role="roles/pubsub.publisher"

    # Notification scoped to the folder with --object-prefix
    gcloud storage buckets notifications create gs://YOUR-BUCKET-NAME \
      --topic=YOUR-ATTRIBUTES-TOPIC --event-types=OBJECT_FINALIZE \
      --payload-format=json --object-prefix=attributes/

    # One subscription per sync
    gcloud pubsub subscriptions create YOUR-ATTRIBUTES-SUBSCRIPTION \
      --topic=YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
    ```

3. Asigna a la cuenta de servicio de Braze el permiso de consumo en esa suscripción, como en el [paso 5](#step-5-assign-permissions):

    ```shell
    gcloud pubsub subscriptions add-iam-policy-binding YOUR-ATTRIBUTES-SUBSCRIPTION \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
      --role="roles/pubsub.subscriber"
    ```

    Si creaste el rol personalizado en el [paso 5](#step-5-assign-permissions), usa `--role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"` en su lugar.
4. Cuando crees la sincronización en Braze, introduce el nuevo **ID de suscripción de Pub/Sub** y la **ruta de la carpeta** de esta carpeta para que la sincronización ingiera solo los archivos de esa carpeta.


{% endtab %}
{% endtabs %}

## Formatos de archivo requeridos {#required-file-formats}

Los formatos de archivo requeridos son los mismos para Amazon S3 y Google Cloud Storage. La ingesta de datos en el cloud admite archivos JSON, CSV y Parquet. Las columnas requeridas dependen del tipo de datos:

- Los datos de usuario (atributos, eventos personalizados, eventos de compra) utilizan identificadores de usuario y una carga útil
- Los datos de catálogo utilizan identificadores de catálogo

Si utilizas almacenamiento de archivos para datos de catálogo, usa esta página junto con [Sincronizar y eliminar datos de catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) para conocer los requisitos y el comportamiento específicos de los catálogos.

Braze no impone requisitos adicionales de nombres de archivo más allá de los que exige tu proveedor de almacenamiento de archivos. Los nombres de archivo deben ser únicos. Agregar una marca de tiempo ayuda a garantizar la unicidad.

Para ver ejemplos de todos los tipos de archivo admitidos (atributos, eventos personalizados, compras, catálogos y eliminaciones de usuarios), consulta los archivos de muestra en [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).

### Identificadores de usuario {#user-identifiers}

Para las sincronizaciones de datos de usuario (atributos, eventos personalizados, eventos de compra), cada fila de tu archivo de origen requiere exactamente un identificador de usuario y una columna `PAYLOAD`. Un archivo de origen puede contener filas con diferentes tipos de identificadores, pero cada fila individual solo debe usar uno.

| Identificador | Descripción |
| --- | --- |
| `EXTERNAL_ID` | Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. |
| `ALIAS_NAME` y `ALIAS_LABEL` | Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener múltiples alias con diferentes etiquetas, pero solo un `alias_name` por cada `alias_label`. |
| `BRAZE_ID` | El identificador de usuario de Braze. Es generado por el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un Braze ID a través de la ingesta de datos en el cloud. Para crear nuevos usuarios, especifica un ID externo o un alias de usuario. |
| `EMAIL` | La dirección de correo electrónico del usuario. Si existen múltiples perfiles con la misma dirección de correo electrónico, se prioriza el perfil actualizado más recientemente. Si incluyes tanto correo electrónico como teléfono, Braze utiliza el correo electrónico como identificador principal. |
| `PHONE` | El número de teléfono del usuario. Si existen múltiples perfiles con el mismo número de teléfono, se prioriza el perfil actualizado más recientemente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identificadores de usuario" }

Además de un identificador, cada fila debe incluir una columna `PAYLOAD` que contenga una cadena JSON de los campos que deseas sincronizar con el usuario en Braze.

{% alert note %}
A diferencia de los orígenes de datos de almacén de datos, la columna `UPDATED_AT` no es necesaria ni está admitida para las sincronizaciones de almacenamiento de archivos.
{% endalert %}

### Identificadores de catálogo {#catalog-identifiers}

Para las sincronizaciones de catálogo, tu archivo de origen debe contener las siguientes columnas. Los archivos de catálogo utilizan identificadores diferentes a los de los archivos de datos de usuario.

| Columna | Obligatorio | Descripción |
| --- | --- | --- |
| `ID` | Sí | El identificador único del elemento del catálogo. Se utiliza para crear, actualizar o eliminar el elemento en Braze. |
| `PAYLOAD` | Sí | Una cadena JSON de los campos y valores del catálogo que se van a sincronizar. Debe coincidir con el esquema de tu catálogo en Braze. |
| `DELETED` | No | Cuando es `true`, el elemento del catálogo con el `ID` correspondiente se elimina del catálogo en Braze. Omite esta columna o establécela en `false` para operaciones de creación o actualización. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Identificadores de catálogo" }

### Ejemplos {#examples}

{% tabs %}
{% tab Atributos JSON %}
``` json
{"external_id":"s3-qa-0","payload":"{\"name\": \"GT896\", \"age\": 74, \"subscriber\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"external_id":"s3-qa-1","payload":"{\"name\": \"HSCJC\", \"age\": 86, \"subscriber\": false, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600824\"}"}
{"external_id":"s3-qa-2","payload":"{\"name\": \"YTMQZ\", \"age\": 43, \"subscriber\": false, \"retention\": {\"previous_purchases\": 23, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600831\"}"}
{"external_id":"s3-qa-3","payload":"{\"name\": \"5P44M\", \"age\": 15, \"subscriber\": true, \"retention\": {\"previous_purchases\": 7, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600838\"}"}
{"external_id":"s3-qa-4","payload":"{\"name\": \"WMYS7\", \"age\": 11, \"subscriber\": true, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600844\"}"}
{"external_id":"s3-qa-5","payload":"{\"name\": \"KCBLK\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 11, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600850\"}"}
{"external_id":"s3-qa-6","payload":"{\"name\": \"T93MJ\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 10, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600856\"}"}
```
{% alert important %}
Cada línea de tu archivo de origen debe contener JSON válido, o el archivo se omitirá.
{% endalert %}
{% endtab %}
{% tab Eventos personalizados JSON %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```
{% alert important %}
Cada línea de tu archivo de origen debe contener JSON válido, o el archivo se omitirá.
{% endalert %}
{% endtab %}
{% tab Eventos de compra JSON %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```
{% alert important %}
Cada línea de tu archivo de origen debe contener JSON válido, o el archivo se omitirá.
{% endalert %}

{% endtab %}
{% tab Atributos CSV %}
```plaintext
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% tab Catálogos CSV  %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
Incluye una columna `DELETED` opcional. Cuando `DELETED` es `true`, ese elemento del catálogo se elimina del catálogo en Braze. Para ver la lista completa de columnas requeridas, consulta [Identificadores de catálogo](#catalog-identifiers). Para conocer el comportamiento de eliminación, consulta [Eliminación de elementos de catálogo](#deleting-catalog-items). Para un flujo de configuración de catálogo de extremo a extremo (incluyendo la creación del catálogo de destino y el comportamiento de sincronización), consulta [Sincronizar y eliminar datos de catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).
{% endtab %}

{% endtabs %}

## Eliminación de datos {#deleting-data}

La ingesta de datos en el cloud para almacenamiento de archivos permite eliminar usuarios y elementos de catálogo mediante cargas de archivos. Utiliza sincronizaciones y formatos de archivo separados para cada uno.

- **[Eliminación de usuarios](#deleting-users)**: crea una sincronización con el tipo de datos **Delete Users** y carga archivos que contengan solo identificadores de usuario (sin carga útil).
- **[Eliminación de elementos de catálogo](#deleting-catalog-items)**: usa tu sincronización de catálogo existente y añade una columna `deleted` (o `DELETED`) para marcar los elementos que se van a eliminar.

### Eliminación de usuarios {#deleting-users}

Para eliminar perfiles de usuario en Braze usando archivos en tu contenedor de origen:

1. Crea una nueva sincronización de ingesta de datos en el cloud (la misma configuración que para otras sincronizaciones).
2. Al configurar la sincronización en Braze, establece **Data Type** en **Delete Users**.
3. Carga archivos en tu contenedor de origen que contengan solo columnas de identificadores de usuario. No incluyas una columna `PAYLOAD`: la sincronización falla si hay carga útil presente, para evitar eliminaciones accidentales.

Cada fila del archivo debe identificar exactamente a un usuario utilizando uno de los siguientes:

| Identificador | Descripción |
| --- | --- |
| `EXTERNAL_ID` | Coincide con el `external_id` utilizado en Braze. |
| `ALIAS_NAME` y `ALIAS_LABEL` | Ambas columnas juntas identifican al usuario por alias. |
| `BRAZE_ID` | ID de usuario generado por Braze (solo usuarios existentes). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eliminación de usuarios" }

{% alert important %}
La eliminación de usuarios es permanente y no se puede deshacer. Incluye solo los usuarios que tengas la intención de eliminar. Para más detalles, consulta [Eliminar usuarios con ingesta de datos en el cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users).
{% endalert %}

**Ejemplo – JSON (eliminación de usuarios):**
```jsonl
{"external_id":"user-to-delete-001"}
{"external_id":"user-to-delete-002"}
{"braze_id":"braze-id-from-profile"}
```

**Ejemplo – CSV (eliminación de usuarios):**
```plaintext
external_id
user-to-delete-001
user-to-delete-002
```

Cuando se ejecuta la sincronización, Braze procesa los archivos nuevos en el contenedor y elimina los perfiles de usuario correspondientes.

### Eliminación de elementos de catálogo {#deleting-catalog-items}

Para eliminar elementos de un catálogo usando almacenamiento de archivos:

1. Usa la misma sincronización que utilizas para [sincronizar datos de catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) (tipo de datos **Catalogs**).
2. En tus archivos CSV o JSON, añade una columna opcional **`deleted`** (o **`DELETED`**).
3. Establece `deleted` en `true` para cualquier elemento de catálogo que quieras eliminar del catálogo en Braze.

Cada fila sigue necesitando `ID` y `PAYLOAD`. Para las filas marcadas para eliminación, la carga útil puede ser mínima; Braze elimina el elemento por `ID`.

**Ejemplo – JSON (eliminación de elemento de catálogo):**
```jsonl
{"id":"85","payload":"{\"product_name\": \"Product 85\", \"price\": 85.85}"}
{"id":"1","payload":"{\"product_name\": \"Product 1\", \"price\": 1.01}","deleted":true}
```

**Ejemplo – CSV (eliminación de elemento de catálogo):**
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```

Cuando se ejecuta la sincronización, las filas con `deleted: true` provocan que el elemento de catálogo correspondiente se elimine en Braze. Para conocer el comportamiento completo de sincronización y eliminación de catálogos, consulta [Sincronizar y eliminar datos de catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).

## Aspectos a tener en cuenta {#things-to-know}

- Los archivos añadidos al contenedor de origen no deben superar los 512&nbsp;MB. Este límite se aplica tanto a Amazon S3 como a Google Cloud Storage. Los archivos de más de 512&nbsp;MB generan un error y no se sincronizan con Braze.
- Aunque no hay un límite adicional en el número de filas por archivo, recomendamos usar archivos más pequeños para mejorar la velocidad de ejecución de tus sincronizaciones. Por ejemplo, un archivo de 500&nbsp;MB tardaría considerablemente más en ingerirse que cinco archivos separados de 100&nbsp;MB.
- No hay un límite adicional en el número de archivos cargados en un periodo de tiempo determinado.
- No se admite el ordenamiento dentro de los archivos ni entre ellos. Recomendamos agrupar las actualizaciones periódicamente si estás monitorizando posibles condiciones de carrera.

## Solución de problemas {#troubleshooting}

### Carga y procesamiento de archivos {#uploading-files-and-processing}

CDI solo procesará archivos que se hayan añadido después de crear la sincronización. En este proceso, Braze busca nuevos archivos que se añadan, lo que desencadena una nueva notificación. Esto inicia una nueva sincronización para procesar el nuevo archivo. En el caso de Amazon S3, la notificación es un mensaje a SQS. En el caso de Google Cloud Storage, es un mensaje `OBJECT_FINALIZE` a Pub/Sub.

Puedes utilizar archivos existentes para validar que Braze pueda acceder a tu contenedor y detectar archivos para ingerir, pero no se sincronizan con Braze. Para que CDI los procese, debes volver a cargar en el contenedor de origen cualquier archivo existente que quieras sincronizar.

### Gestión de errores inesperados en archivos (Amazon S3) {#handling-unexpected-file-errors-amazon-s3}

Si observas un número elevado de errores o archivos fallidos, es posible que otro proceso esté añadiendo archivos al contenedor de S3 en una carpeta diferente a la carpeta de destino de CDI.

Cuando los archivos se cargan en el contenedor de origen pero no en la carpeta de origen, CDI procesará la notificación de SQS, pero no realizará ninguna acción sobre el archivo, por lo que esto puede aparecer como un error.

Si tu problema está relacionado con las notificaciones de S3 o los permisos de destino de SQS (por ejemplo, errores de validación de destino), consulta la documentación de AWS:

- [Habilitación y configuración de notificaciones de eventos mediante la consola de Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html)
- [Concesión de permisos para publicar mensajes de notificación de eventos en un destino](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)
- [Solución de problemas en Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting.html)

### Gestión de errores inesperados en archivos (Google Cloud Storage) {#handling-unexpected-file-errors-google-cloud-storage}

Al igual que Amazon S3, CDI solo procesa archivos cargados después de crear la sincronización. Cada nuevo objeto desencadena un mensaje `OBJECT_FINALIZE` en tu tema de Pub/Sub. Para ingerir archivos que ya existen en el contenedor, vuélvelos a cargar.

Si los archivos no se ingieren, verifica lo siguiente:

- La notificación del contenedor existe. Enumera las notificaciones del contenedor con `gcloud storage buckets notifications list gs://YOUR-BUCKET-NAME`.
- El agente de servicio de Cloud Storage tiene `roles/pubsub.publisher` en el tema.
- La cuenta de servicio de Braze tiene permiso de consumo en la suscripción (`pubsub.subscriptions.consume`, asignado a través del rol personalizado o `roles/pubsub.subscriber`).
- La suscripción no tiene configurada una cola de mensajes no entregados. Braze no es compatible con colas de mensajes no entregados para las suscripciones de Cloud Data Ingestion.

Para obtener más información, consulta [Notificaciones de Pub/Sub para Cloud Storage](https://cloud.google.com/storage/docs/pubsub-notifications) en la documentación de Google Cloud.