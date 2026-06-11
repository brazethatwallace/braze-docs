---
nav_title: Amazon S3
article_title: Amazon S3
alias: /partners/amazon_s3/
description: "Este artículo de referencia describe la asociación entre Braze y Amazon S3, un sistema de almacenamiento altamente escalable ofrecido por Amazon Web Services."
page_type: partner
search_tag: Partner

---

# Amazon S3

> [Amazon S3](https://aws.amazon.com/s3/) es un sistema de almacenamiento altamente escalable ofrecido por Amazon Web Services.

{% alert important %}
Si vas a cambiar de proveedor de almacenamiento en la nube, ponte en contacto con tu administrador del éxito del cliente de Braze para que te ayude a configurar y validar tu nueva integración.
{% endalert %}

La integración de Braze y Amazon S3 presenta dos estrategias de integración:

- Aprovecha [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), que te permite almacenar datos allí hasta que quieras conectarlos a otras plataformas, herramientas y ubicaciones.
- Utiliza las exportaciones de datos del dashboard (como las exportaciones CSV y los informes de interacción).

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Amazon S3 | Necesitas una cuenta de Amazon S3 para aprovechar esta asociación. |
| Contenedor de S3 dedicado | Antes de integrarte con Amazon S3, debes crear un contenedor de S3 para tu aplicación.<br><br>Si ya tienes un contenedor de S3, te recomendamos que crees un nuevo contenedor específico para Braze, de modo que puedas limitar los permisos. Consulta las siguientes instrucciones sobre cómo crear un nuevo contenedor. |
| Currents | Para volver a exportar datos a Amazon S3, necesitas tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) para tu cuenta. Currents no es necesario si solo estás configurando el archivado de mensajes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Crear un nuevo contenedor de S3 {#creating-a-new-s3-bucket}

Para crear un contenedor para tu aplicación, haz lo siguiente:

1. Abre la [consola de Amazon S3](https://console.aws.amazon.com/s3/) y sigue las instrucciones para **Sign in** o **Create an Account with AWS**.
2. Tras iniciar sesión, selecciona **S3** en la categoría **Storage & Content Delivery**.
3. Selecciona **Create Bucket** en la siguiente pantalla.
4. Cuando se te solicite, crea tu contenedor y selecciona una región de AWS.

Braze no te permite elegir ni configurar una región en el dashboard. La región de AWS se fija en el lugar donde creas el contenedor en la consola de AWS. La integración envía datos al nombre de contenedor que proporcionas, y AWS enruta automáticamente las solicitudes a la región del contenedor. Si tu conector intenta conectarse a una región diferente a la que deseas (por ejemplo, `eu-west-1` en lugar de `eu-central-1`), crea o utiliza un contenedor de S3 en la región deseada en AWS. No hay nada que cambiar en el lado de Braze.

{% alert note %}
Currents no admite contenedores con [Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) configurado.
{% endalert %}

## Integración {#integration}

Braze tiene dos estrategias diferentes de integración con Amazon S3: una para [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) y otra para todas las exportaciones de datos del dashboard (como exportaciones CSV o informes de interacción). Ambas integraciones admiten dos métodos diferentes de autenticación o autorización:

- [Método de clave de acceso secreta de AWS](#aws-secret-key-auth-method)
- [Método ARN del rol de AWS](#aws-role-arn-auth-method)

## Método de autenticación de clave secreta de AWS {#aws-secret-key-auth-method}

Este método de autenticación genera una clave secreta y un ID de clave de acceso que permite a Braze autenticarse como usuario en tu cuenta de AWS para escribir datos en tu contenedor.

### Paso 1: Crear usuario {#secret-key-1}

{% alert note %}
Si solo vas a configurar el archivado de mensajes, sigue los pasos de la pestaña **Dashboard Data Export**.
{% endalert %}

Para recuperar tu ID de clave de acceso y tu clave de acceso secreta, [crea un usuario IAM y un grupo de administradores en AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).

### Paso 2: Obtener credenciales {#secret-key-2}

Tras crear un nuevo usuario, selecciona **Show User Security Credentials** para revelar tu ID de clave de acceso y tu clave de acceso secreta. A continuación, anota estas credenciales en algún sitio o selecciona el botón **Download Credentials**, ya que tendrás que introducirlas en el dashboard de Braze más adelante.

![]({% image_buster /assets/img_archive/S3_Credentials.png %})

### Paso 3: Crear política {#secret-key-3}

Ve a **Policies** > **Get Started** > **Create Policy** para añadir permisos a tu usuario. A continuación, selecciona **Create Your Own Policy**. Esto otorga permisos limitados, de modo que Braze solo puede acceder a los contenedores especificados.

![]({% image_buster /assets/img_archive/S3_CreatePolicy.png %})

{% alert note %}
Se necesitan políticas diferentes para Currents y la exportación de datos del dashboard. `s3:GetObject` es necesario para permitir que el backend de Braze realice la gestión de errores.
{% endalert %}

Especifica un nombre de política de tu elección e introduce el siguiente fragmento de código en la sección **Policy Document**. Asegúrate de sustituir `INSERTBUCKETNAME` por el nombre de tu contenedor. Sin estos permisos, la integración no superará la comprobación de credenciales y no se creará.

{% alert note %}
Si solo vas a configurar el archivado de mensajes, utiliza el fragmento de código de la pestaña **Dashboard Data Export**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```
{% endtab %}
{% tab Dashboard Data Export %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
        }
    ]
}
```
{% endtab %}
{% endtabs %}

### Paso 4: Adjuntar política {#secret-key-4}

Después de crear una nueva política, ve a **Users** y selecciona tu usuario específico. En la pestaña **Permissions**, selecciona **Attach Policy** y selecciona la nueva política que has creado. Ahora estás listo para vincular tus credenciales de AWS a tu cuenta de Braze.

![]({% image_buster /assets/img_archive/S3_AttachPolicy.png %})

### Paso 5: Vincular Braze a AWS {#secret-key-5}

{% alert note %}
Si solo vas a configurar el archivado de mensajes, sigue los pasos de la pestaña **Dashboard Data Export**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

En Braze, ve a **Partner Integrations** > **Currents**.

A continuación, selecciona **Create New Current** y luego **Amazon S3 Data Export**.

Ponle nombre a tu Current. En la sección **Credentials**, asegúrate de que está seleccionada **AWS Secret Access Key** y, a continuación, introduce tu ID de acceso a S3, la clave de acceso secreta de AWS y el nombre de contenedor de AWS S3 en los campos designados.

![]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
Mantén actualizados tu ID de clave de acceso a AWS y tu clave de acceso secreta. Si las credenciales de tu conector caducan, el conector deja de enviar eventos. Si esto persiste durante más de **5 días**, los eventos del conector se eliminan y los datos se pierden permanentemente.
{% endalert %}

También puedes añadir las siguientes personalizaciones en función de tus necesidades:

- **Ruta de la carpeta:** De forma predeterminada, `currents`. Si esta carpeta no existe, Braze la crea automáticamente.
- **Encriptación AES-256 del lado del servidor, en reposo:** Está predeterminada en OFF e incluye el encabezado `x-amz-server-side-encryption`.

Selecciona **Launch Current** para continuar.

Una notificación te informa de si tus credenciales se han validado correctamente. AWS S3 ya está configurado para Braze Currents.

{% endtab %}
{% tab Dashboard Data Export %}

En Braze, ve a **Partner Integrations** > **Technology Partners** y selecciona **Amazon S3**.

En la página de **AWS Credentials**, asegúrate de que está seleccionada **AWS Secret Access Key** y, a continuación, introduce tu ID de acceso a AWS, la clave de acceso secreta de AWS y el nombre de contenedor de AWS S3 en los campos designados. Cuando introduzcas tu clave secreta, selecciona primero **Test Credentials** para asegurarte de que tus credenciales funcionan y, a continuación, selecciona **Save** cuando lo consigas.

![]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
Siempre puedes recuperar nuevas credenciales navegando hasta tu usuario y seleccionando **Create Access Key** en la pestaña **Security Credentials** de la consola de AWS.
{% endalert %}

Una notificación te informa de si tus credenciales se han validado correctamente. AWS S3 ya está integrado en tu cuenta de Braze.

{% endtab %}
{% endtabs %}

## Método de autenticación ARN del rol de AWS {#aws-role-arn-auth-method}

Este método de autenticación genera un nombre de recurso de Amazon (ARN) de rol que permite a la cuenta de Amazon de Braze autenticarse como miembro del rol que creaste para escribir datos en tu contenedor.

### Paso 1: Crear política {#role-arn-1}

Para comenzar, inicia sesión en la consola de administración de AWS como administrador de cuenta. Ve a la sección IAM de la consola de AWS, selecciona **Policies** en la barra de navegación y selecciona **Create Policy**.

![]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
Se necesitan políticas diferentes para Currents y la exportación de datos del dashboard. `s3:GetObject` es necesario para permitir que el backend de Braze realice la gestión de errores.
{% endalert %}

Abre la pestaña **JSON** e introduce el siguiente fragmento de código en la sección **Policy Document**. Asegúrate de sustituir `INSERTBUCKETNAME` por el nombre de tu contenedor. Selecciona **Review Policy** cuando hayas terminado.

{% alert note %}
Si solo vas a configurar el archivado de mensajes, utiliza el fragmento de código de la pestaña **Dashboard Data Export**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% tab Dashboard Data Export %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject","s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% endtabs %}

A continuación, dale un nombre y una descripción a la política y selecciona **Create Policy**.

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Paso 2: Crear rol {#role-arn-2}

Dentro de la misma sección IAM de la consola, selecciona **Roles** > **Create Role**.

![]({{site.baseurl}}/assets/img/create_role_1_list.png)

Recupera el ID de tu cuenta de Braze y el ID externo de tu cuenta de Braze:

- **Currents:** En Braze, ve a **Partner Integrations** > **Currents**. A continuación, selecciona **Create New Current** y luego **Amazon S3 Data Export**. Aquí encontrarás los identificadores necesarios para crear tu rol.
- **Exportación de datos del dashboard:** En Braze, ve a **Partner Integrations** > **Technology Partners** y selecciona **Amazon S3**. Aquí encontrarás los identificadores necesarios para crear tu rol. (Crea aquí tus roles si solo vas a configurar el archivado de mensajes).

De vuelta en la consola de AWS, selecciona **Another AWS Account** como tipo de selector de entidad de confianza. Proporciona el ID de tu cuenta de Braze, marca la casilla **Require external ID** e introduce el ID externo de Braze. Selecciona **Next** cuando hayas terminado.

![La página "Create Role" de S3. Esta página tiene campos para el nombre del rol, la descripción del rol, las entidades de confianza, las políticas y el límite de permisos.]({{site.baseurl}}/assets/img/create_role_2_another.png)

### Paso 3: Adjuntar política {#role-arn-3}

A continuación, adjunta al rol la política que creaste anteriormente. Busca la política en la barra de búsqueda y coloca una marca de verificación junto a la política para adjuntarla. Selecciona **Next** cuando hayas terminado.

![ARN del rol]({{site.baseurl}}/assets/img/create_role_3_attach.png)

Dale al rol un nombre y una descripción, y selecciona **Create Role**.

![ARN del rol]({{site.baseurl}}/assets/img/create_role_4_name.png)

Ahora verás tu rol recién creado en la lista.

### Paso 4: Vincular a Braze AWS {#role-arn-4}

En la consola de AWS, busca en la lista el rol que acabas de crear. Selecciona el nombre para abrir los detalles de ese rol.

![]({{site.baseurl}}/assets/img/create_role_5_created.png)

Toma nota del **Role ARN** en la parte superior de la página de resumen del rol.

![]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Vuelve a tu cuenta de Braze y copia el ARN del rol en el campo correspondiente.

{% alert note %}
Si solo vas a configurar el archivado de mensajes, sigue los pasos de la pestaña **Dashboard Data Export**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

En Braze, ve a **Partner Integrations** > **Currents**. A continuación, selecciona **Create New Current** y selecciona **Amazon S3 Data Export**.

![]({{site.baseurl}}/assets/img/currents-role-arn.png)

Dale un nombre a tu Current. A continuación, en la sección **Credentials**, asegúrate de que está seleccionado **AWS Role ARN** y proporciona tu ARN de rol y el nombre de contenedor de AWS S3 en los campos designados.

También puedes añadir las siguientes personalizaciones en función de tus necesidades:

- Ruta de la carpeta (predeterminada a `currents`)
- Encriptación AES-256 del lado del servidor, en reposo (predeterminada en OFF) - Incluye el encabezado `x-amz-server-side-encryption`

Selecciona **Launch Current** para continuar. Una notificación indica si tus credenciales se han validado correctamente. AWS S3 ya está configurado para Braze Currents.

{% alert important %}
Si recibes un error "S3 credentials are invalid", puede deberse a una integración demasiado rápida después de crear un rol en AWS. Espera y vuelve a intentarlo. Si el mensaje menciona acceso a `PutObject` o encriptación del lado del servidor en las exportaciones de datos del dashboard, consulta [Solución de problemas de errores de credenciales de S3](#troubleshooting).
{% endalert %}

{% endtab %}
{% tab Dashboard Data Export %}

En Braze, ve a la página de **Technology Partners** en **Integrations** y selecciona **Amazon S3**.

![]({{site.baseurl}}/assets/img/data-export-role-arn.png)

En la página de **AWS Credentials**, asegúrate de que el botón de opción **AWS Role ARN** está seleccionado y, a continuación, introduce el ARN de tu rol y el nombre de contenedor de AWS S3 en los campos designados. Selecciona primero **Test Credentials** para confirmar que tus credenciales funcionan correctamente y, a continuación, selecciona **Save** cuando lo consigas.

{% alert tip %}
Siempre puedes recuperar nuevas credenciales navegando hasta tu usuario y seleccionando **Create Access Key** en la pestaña **Security Credentials** de la consola de AWS.
{% endalert %}

Una notificación te informa de si tus credenciales se han validado correctamente. AWS S3 ya está integrado en tu cuenta de Braze.

{% endtab %}
{% endtabs %}

## Actualización de credenciales de Amazon S3 para Currents {#updating-currents-credentials}

Puedes actualizar las credenciales de Amazon S3 en un conector de Braze Currents existente sin detener la integración ni perder los datos ya exportados a tu contenedor.

Para actualizar las credenciales, o para cambiar entre **AWS Secret Access Key** y **AWS Role ARN**, completa los pasos de IAM y AWS para el método elegido descritos anteriormente en este artículo (políticas, usuario o rol, e identificadores según sea necesario).

Cuando hayas terminado de preparar las credenciales en AWS, ve a **Partner Integrations** > **Currents** en Braze, localiza tu conector de Amazon S3 en la lista, selecciona **Edit**, actualiza las **Credentials** y selecciona **Update Current**. Braze valida las credenciales que introduces; tu conector sigue funcionando y los datos que ya están en tu contenedor permanecen disponibles. Para más información, consulta [Actualización de Currents en Configurar Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/#updating-currents).

## Comportamiento de la exportación {#export-behavior}

Los usuarios que han integrado una solución de almacenamiento en la nube y exportan API, informes del dashboard o informes CSV experimentan lo siguiente:

- Todas las exportaciones de la API no devuelven una URL de descarga en el cuerpo de la respuesta y deben recuperarse a través del almacenamiento de datos.
- Todos los informes del dashboard y los informes CSV se envían al correo electrónico del usuario para su descarga (sin necesidad de permisos de almacenamiento) y se guardan en el almacenamiento de datos.

### Error `Unable to connect to S3, please validate that your credentials are correct` {#unable-to-connect-to-s3-please-validate-that-your-credentials-are-correct-error}

Si ves este error al descargar una exportación CSV, abre la integración de [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) en la página de **Technology Partners** y selecciona **Test Credentials**. El resultado explica qué falló en la validación; por ejemplo, la clave podría no tener el permiso `GetObject`, lo que impide que Braze genere enlaces de descarga.

Actualiza tu política IAM para que el usuario o rol de la integración pueda llamar a `s3:GetObject` en el contenedor de S3 y la ruta de objetos configurados en tu integración de Braze. Para más problemas de exportación, consulta [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/).

{% alert important %}
**Requisito de formato JSON:** Para las exportaciones JSON, Braze utiliza el formato JSONL (JSON delimitado por nuevas líneas), en el que cada línea contiene un objeto JSON independiente. Este formato difiere del JSON estándar, que es una única matriz u objeto JSON. Cada línea del archivo exportado es un objeto JSON válido, pero el archivo en su conjunto no es un único documento JSON válido. Al procesar estos archivos, analiza cada línea individualmente como un objeto JSON distinto, en lugar de intentar analizar todo el archivo como un único documento JSON.

Las exportaciones de Currents utilizan el formato Apache Avro (archivos `.avro`), no JSON. Este requisito de formato JSON se aplica a las exportaciones de datos del dashboard y a las exportaciones de la API.
{% endalert %}

## Conectores múltiples {#multiple-connectors}

Si pretendes crear más de un conector de Currents para enviarlo a tu contenedor de S3, puedes utilizar las mismas credenciales, pero debes especificar una ruta de carpeta diferente para cada uno. Puedes crearlos en el mismo espacio de trabajo, o dividirlos y crearlos dentro de varios espacios de trabajo. También tienes la opción de crear una única política para cada integración, o crear una política que cubra ambas integraciones.

Si piensas utilizar el mismo contenedor de S3 tanto para Currents como para la exportación de datos, deberás crear dos políticas distintas, ya que cada integración requiere permisos diferentes.

## Solución de problemas {#troubleshooting}

### Error: la cuenta no tiene acceso a `PutObject` {#error-account-does-not-have-putobject-access}

Si ves el siguiente error al guardar las credenciales de Amazon S3 para las exportaciones de datos del dashboard, puede deberse a permisos incorrectos o a la configuración de encriptación del lado del servidor.

```
S3 Credentials are invalid because this account does not have 'PutObject access'. Please check the permissions and ensure that this key has access to 'PutObject' in the 'CUSTOMER-BUCKET-HERE' bucket.
```

Para resolver este problema, verifica las siguientes áreas.

#### Política de contenedor incorrecta {#incorrect-bucket-policy}

Confirma que creaste una política con los permisos correctos como se describe en [Integración de Amazon S3](#integration) (utiliza la política de **Dashboard Data Export** para tu método de autenticación).

#### Encriptación del lado del servidor {#server-side-encryption}

```
User: arn:aws:sts::XXX:assumed-role/braze-iam-role/braze is not authorized to perform: kms:GenerateDataKey on resource: arn:aws:XXX because no identity-based policy allows the kms:GenerateDataKey action
```

Si recibes este mensaje de error de [soporte de Braze]({{site.baseurl}}/braze_support/) o en tus registros de AWS, tu contenedor de S3 está configurado con encriptación de AWS Key Management Service (SSE-KMS). Braze no admite SSE-KMS para Currents ni para las exportaciones de datos del dashboard. Para resolver esto, desactiva SSE-KMS en tu contenedor de S3.

{% alert note %}
Braze admite la encriptación del lado del servidor utilizando claves administradas por S3 (SSE-S3), que es compatible tanto con Currents como con las exportaciones de datos del dashboard.
{% endalert %}

#### Verificar permisos adicionales {#check-additional-permissions}

Asegúrate de que tienes los permisos necesarios, incluyendo `s3:GetBucketLocation` y `s3:PutObject`.