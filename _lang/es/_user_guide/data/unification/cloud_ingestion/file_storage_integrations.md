---
nav_title: Integraciones de almacenamiento de archivos
article_title: Integraciones de almacenamiento de archivos
description: "Esta página trata sobre la ingesta de datos en la nube de Braze y cómo sincronizar datos relevantes de S3 con Braze."
page_order: 4
page_type: reference

---

# Integraciones de almacenamiento de archivos {#file-storage-integrations}

> Esta página explica cómo configurar la compatibilidad con la ingesta de datos en la nube y sincronizar datos relevantes de S3 con Braze.

## Cómo funciona {#how-it-works}

Puedes usar la ingesta de datos en la nube (CDI) para S3 para integrar directamente uno o más contenedores de S3 en tu cuenta de AWS con Braze. Cuando se publican nuevos archivos en S3, se envía un mensaje a SQS y la ingesta de datos en la nube de Braze incorpora esos nuevos archivos.

La ingesta de datos en la nube es compatible con lo siguiente:

- Archivos JSON
- Archivos CSV
- Archivos Parquet
- Datos de atributos, eventos personalizados, eventos de compra, eliminación de usuarios y catálogos

## Requisitos previos {#prerequisites}

La integración requiere los siguientes recursos:

 - Contenedor de S3 para el almacenamiento de datos
 - Cola SQS para notificaciones de archivos nuevos
 - Rol IAM para el acceso de Braze

### Definiciones de AWS {#aws-definitions}

Primero, define los términos utilizados durante esta tarea.

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
2. En AWS, selecciona **Another AWS Account** como tipo de selector de entidad de confianza. Proporciona tu ID de cuenta de Braze. Selecciona la casilla **Require external ID**.
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

  - Role ARN
  - ID externo
  - Nombre de contenedor
  - Región

![La sección de detalles de conexión de S3 que muestra las credenciales (configuración de AWS y configuración de Braze) y los campos de configuración.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. Selecciona **Probar conexión** para confirmar que Braze puede acceder a tu contenedor. Después de una prueba exitosa, selecciona **Conectar al origen**. Si la conexión falla, aparece un mensaje de error para ayudar a solucionar el problema.

{: start="4"}
4. A continuación, crea una nueva sincronización. Ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Sincronizaciones** y selecciona **Crear sincronización de datos**.

{: start="5"}
5. Elige un nombre para tu sincronización. Luego, selecciona cualquier origen de S3 activo e introduce tu tabla de origen para la sincronización. Selecciona un tipo de datos y selecciona **Probar conexión**.

![Una opción para probar la conexión con una vista previa de los datos.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. Introduce la información restante del proceso de configuración de AWS. Especifica lo siguiente:
- URL de SQS (debe ser única para cada nueva integración)
- Ruta de carpeta (opcional, debe ser única entre las sincronizaciones de un espacio de trabajo)

7. Selecciona un tipo de datos y selecciona **Probar conexión** para confirmar que Braze puede listar los archivos disponibles para ingestar (no los datos dentro de esos archivos). Una vez que sea exitoso, selecciona **Siguiente: Notificaciones**.
8. Añade correo(s) electrónico(s) de contacto para recibir notificaciones si la sincronización se interrumpe por problemas de acceso o permisos. Opcionalmente, activa las notificaciones para errores a nivel de usuario y sincronizaciones exitosas.
9. Crea la sincronización.

## Formatos de archivo requeridos {#required-file-formats}

La ingesta de datos en la nube admite archivos JSON, CSV y Parquet. Las columnas requeridas dependen del tipo de datos:

- Los datos de usuario (atributos, eventos personalizados, eventos de compra) utilizan identificadores de usuario y una carga útil
- Los datos de catálogo utilizan identificadores de catálogo

Si usas S3 para datos de catálogo, utiliza esta página junto con [Sincronizar y eliminar datos de catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) para conocer los requisitos y el comportamiento específicos de los catálogos.

Braze no impone requisitos adicionales de nombre de archivo más allá de los que aplica AWS. Los nombres de archivo deben ser únicos. Agregar una marca de tiempo ayuda a garantizar la unicidad.

Para ver ejemplos de todos los tipos de archivo admitidos (atributos, eventos personalizados, compras, catálogos y eliminaciones de usuarios), consulta los archivos de ejemplo en [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).

### Identificadores de usuario {#user-identifiers}

Para las sincronizaciones de datos de usuario (atributos, eventos personalizados, eventos de compra), cada fila en tu archivo de origen requiere exactamente un identificador de usuario y una columna `PAYLOAD`. Un archivo de origen puede contener filas con diferentes tipos de identificadores, pero cada fila individual solo debe usar uno.

| Identificador | Descripción |
| --- | --- |
| `EXTERNAL_ID` | Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. |
| `ALIAS_NAME` y `ALIAS_LABEL` | Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener múltiples alias con diferentes etiquetas, pero solo un `alias_name` por `alias_label`. |
| `BRAZE_ID` | El identificador de usuario de Braze. Es generado por el SDK de Braze, y no se pueden crear nuevos usuarios usando un Braze ID a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID externo o un alias de usuario. |
| `EMAIL` | La dirección de correo electrónico del usuario. Si existen múltiples perfiles con la misma dirección de correo electrónico, se prioriza el perfil actualizado más recientemente. Si incluyes tanto correo electrónico como teléfono, Braze usa el correo electrónico como identificador principal. |
| `PHONE` | El número de teléfono del usuario. Si existen múltiples perfiles con el mismo número de teléfono, se prioriza el perfil actualizado más recientemente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identificadores de usuario" }

Además de un identificador, cada fila debe incluir una columna `PAYLOAD` que contenga una cadena JSON con los campos que deseas sincronizar con el usuario en Braze.

{% alert note %}
A diferencia de los orígenes de almacén de datos, la columna `UPDATED_AT` no es requerida ni compatible para las sincronizaciones de almacenamiento de archivos.
{% endalert %}

### Identificadores de catálogo {#catalog-identifiers}

Para las sincronizaciones de catálogo, tu archivo de origen debe contener las siguientes columnas. Los archivos de catálogo utilizan identificadores diferentes a los archivos de datos de usuario.

| Columna | Obligatorio | Descripción |
| --- | --- | --- |
| `ID` | Sí | El identificador único del elemento del catálogo. Se utiliza para crear, actualizar o eliminar el elemento en Braze. |
| `PAYLOAD` | Sí | Una cadena JSON con los campos y valores del catálogo a sincronizar. Debe coincidir con el esquema de tu catálogo en Braze. |
| `DELETED` | No | Cuando es `true`, el elemento del catálogo con el `ID` correspondiente se elimina del catálogo en Braze. Omite esta columna o establécela en `false` para operaciones de creación o actualización. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Identificadores de catálogo" }

### Ejemplos {#examples}

{% tabs %}
{% tab JSON Attributes %}
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
Cada línea en tu archivo de origen debe contener JSON válido, o el archivo será omitido.
{% endalert %}
{% endtab %}
{% tab JSON Custom Events %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```
{% alert important %}
Cada línea en tu archivo de origen debe contener JSON válido, o el archivo será omitido.
{% endalert %}
{% endtab %}
{% tab JSON Purchase Events %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```
{% alert important %}
Cada línea en tu archivo de origen debe contener JSON válido, o el archivo será omitido.
{% endalert %}

{% endtab %}
{% tab CSV Attributes %}
```plaintext
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% tab CSV Catalogs  %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
Incluye una columna `DELETED` opcional. Cuando `DELETED` es `true`, ese elemento del catálogo se elimina del catálogo en Braze. Para ver la lista completa de columnas requeridas, consulta [Identificadores de catálogo](#catalog-identifiers). Para conocer el comportamiento de eliminación, consulta [Eliminar elementos del catálogo](#deleting-catalog-items). Para un flujo de configuración de catálogo de extremo a extremo (incluyendo la creación del catálogo de destino y el comportamiento de sincronización), consulta [Sincronizar y eliminar datos de catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).
{% endtab %}

{% endtabs %}

## Eliminación de datos {#deleting-data}

La ingesta de datos en la nube para S3 permite eliminar usuarios y elementos de catálogo mediante la carga de archivos. Usa sincronizaciones y formatos de archivo independientes para cada caso.

- **[Eliminación de usuarios](#deleting-users)**: crea una sincronización con el tipo de datos **Delete Users** y carga archivos que contengan solo identificadores de usuario (sin carga útil).
- **[Eliminación de elementos de catálogo](#deleting-catalog-items)**: usa tu sincronización de catálogo existente y añade una columna `deleted` (o `DELETED`) para marcar los elementos que deseas eliminar.

### Eliminación de usuarios {#deleting-users}

Para eliminar perfiles de usuario en Braze mediante archivos en S3:

1. Crea una nueva sincronización de ingesta de datos en la nube (la misma [configuración de AWS y Braze](#setting-up-cloud-data-ingestion-in-aws) que para otras sincronizaciones).
2. Al configurar la sincronización en Braze, establece **Data Type** en **Delete Users**.
3. Carga archivos en tu contenedor de S3 que contengan solo columnas de identificadores de usuario. No incluyas una columna `PAYLOAD`: la sincronización falla si hay carga útil presente, para evitar eliminaciones accidentales.

Cada fila del archivo debe identificar exactamente a un usuario mediante uno de los siguientes:

| Identificador | Descripción |
| --- | --- |
| `EXTERNAL_ID` | Coincide con el `external_id` utilizado en Braze. |
| `ALIAS_NAME` y `ALIAS_LABEL` | Ambas columnas juntas identifican al usuario por alias. |
| `BRAZE_ID` | ID de usuario generado por Braze (solo usuarios existentes). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eliminación de usuarios" }

{% alert important %}
La eliminación de usuarios es permanente y no se puede deshacer. Incluye solo los usuarios que deseas eliminar. Para más detalles, consulta [Eliminar usuarios con la ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users).
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

Para eliminar elementos de un catálogo mediante almacenamiento de archivos:

1. Usa la misma sincronización de S3 que utilizas para [sincronizar datos de catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) (tipo de datos **Catalogs**).
2. En tus archivos CSV o JSON, añade una columna opcional **`deleted`** (o **`DELETED`**).
3. Establece `deleted` en `true` para cualquier elemento de catálogo que desees eliminar del catálogo en Braze.

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

## Cosas que debes saber {#things-to-know}

- Los archivos añadidos al contenedor de S3 de origen no deben superar los 512&nbsp;MB. Los archivos de más de 512&nbsp;MB generan un error y no se sincronizan con Braze.
- Aunque no hay un límite adicional en el número de filas por archivo, recomendamos usar archivos más pequeños para mejorar la velocidad de ejecución de tus sincronizaciones. Por ejemplo, un archivo de 500&nbsp;MB tardaría considerablemente más en ingerirse que cinco archivos separados de 100&nbsp;MB.
- No hay un límite adicional en el número de archivos cargados en un periodo de tiempo determinado.
- No se admite el ordenamiento dentro de los archivos ni entre ellos. Recomendamos agrupar las actualizaciones periódicamente si estás monitorizando posibles condiciones de carrera.

## Solución de problemas {#troubleshooting}

### Carga de archivos y procesamiento {#uploading-files-and-processing}

CDI solo procesará los archivos que se añadan después de crear la sincronización. En este proceso, Braze busca nuevos archivos que se añadan, lo que desencadena un nuevo mensaje a SQS. Esto inicia una nueva sincronización para procesar el nuevo archivo.

Puedes usar archivos existentes para validar que Braze puede acceder a tu contenedor y detectar archivos para ingestar, pero no se sincronizan con Braze. Para que CDI los procese, debes volver a cargar en S3 cualquier archivo existente que quieras sincronizar.

### Gestión de errores inesperados en archivos {#handling-unexpected-file-errors}

Si observas un número elevado de errores o archivos fallidos, es posible que otro proceso esté añadiendo archivos al contenedor de S3 en una carpeta distinta a la carpeta de destino de CDI.

Cuando los archivos se cargan en el contenedor de origen pero no en la carpeta de origen, CDI procesará la notificación de SQS, pero no realiza ninguna acción sobre el archivo, por lo que esto puede aparecer como un error.

Si tu problema está relacionado con las notificaciones de S3 o los permisos de destino de SQS (por ejemplo, errores de validación de destino), consulta la documentación de AWS:

- [Habilitar y configurar notificaciones de eventos mediante la consola de Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html)
- [Conceder permisos para publicar mensajes de notificación de eventos en un destino](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)
- [Solución de problemas en Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting.html)