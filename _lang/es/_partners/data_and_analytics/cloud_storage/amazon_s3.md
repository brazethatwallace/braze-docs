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
Si vas a cambiar de proveedor de almacenamiento en el cloud, ponte en contacto con tu administrador de éxito de cliente de Braze para que te ayude a configurar y validar tu nueva integración.
{% endalert %}

La integración de Braze y Amazon S3 presenta dos estrategias de integración:

- Aprovecha [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), que te permite almacenar datos allí hasta que quieras conectarlos a otras plataformas, herramientas y ubicaciones.
- Utiliza las exportaciones de datos del panel (como las exportaciones CSV y los informes de participación).

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Amazon S3 | Necesitas una cuenta de Amazon S3 para aprovechar esta integración. |
| Contenedor de S3 dedicado | Antes de integrar con Amazon S3, debes crear un contenedor de S3 para tu aplicación.<br><br>Si ya tienes un contenedor de S3, te recomendamos crear uno nuevo específicamente para Braze para poder limitar los permisos. Consulta las siguientes instrucciones sobre cómo crear un nuevo contenedor. |
| Currents | Para exportar datos de vuelta a Amazon S3, necesitas tener [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) configurado para tu cuenta. Currents no es obligatorio si solo estás configurando el archivado de mensajes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Crear un nuevo contenedor de S3 {#creating-a-new-s3-bucket}

Para crear un contenedor para tu aplicación, haz lo siguiente:

1. Abre la [consola de Amazon S3](https://console.aws.amazon.com/s3/) y sigue las instrucciones para **Iniciar sesión** o **Crear una cuenta con AWS**.
2. Después de iniciar sesión, selecciona **S3** en la categoría **Storage & Content Delivery**.
3. Selecciona **Create Bucket** en la siguiente pantalla.
4. Cuando se te solicite, crea tu contenedor y selecciona una región de AWS.

Braze no te permite elegir ni configurar una región en el panel. La región de AWS se fija en función de dónde crees el contenedor en la consola de AWS. La integración envía datos al nombre de contenedor que proporciones, y AWS enruta automáticamente las solicitudes a la región del contenedor. Si tu conector intenta conectarse a una región diferente a la que deseas (por ejemplo, `eu-west-1` en lugar de `eu-central-1`), crea o utiliza un contenedor de S3 en la región deseada en AWS. No hay nada que cambiar en el lado de Braze.

{% alert note %}
Currents no es compatible con contenedores que tengan configurado [Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html).
{% endalert %}

## Integración {#integration}

Braze tiene dos estrategias de integración diferentes con Amazon S3: una para [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) y otra para todas las exportaciones de datos del panel (como exportaciones CSV o informes de participación). Ambas integraciones admiten dos métodos diferentes de autenticación o autorización:

- [Método de clave de acceso secreta de AWS](#aws-secret-key-auth-method)
- [Método de ARN de rol de AWS](#aws-role-arn-auth-method)

## Método de autenticación con clave secreta de AWS {#aws-secret-key-auth-method}

Este método de autenticación genera una clave secreta y un ID de clave de acceso que permite a Braze autenticarse como usuario en tu cuenta de AWS para escribir datos en tu contenedor.

### Paso 1: Crear usuario {#secret-key-1}

{% alert note %}
Si solo estás configurando el archivado de mensajes, sigue los pasos en la pestaña **Dashboard Data Export**.
{% endalert %}

Para obtener tu ID de clave de acceso y tu clave de acceso secreta, [crea un usuario de IAM y un grupo de administradores en AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).

### Paso 2: Obtener credenciales {#secret-key-2}

Después de crear un nuevo usuario, selecciona **Show User Security Credentials** para revelar tu ID de clave de acceso y tu clave de acceso secreta. A continuación, anota estas credenciales en algún lugar o selecciona el botón **Download Credentials**, ya que necesitarás ingresarlas en el panel de Braze más adelante.

![Página de credenciales de seguridad del usuario de AWS IAM que muestra el ID de clave de acceso y la clave de acceso secreta.]({% image_buster /assets/img_archive/S3_Credentials.png %})

### Paso 3: Crear política {#secret-key-3}

Navega a **Policies** > **Get Started** > **Create Policy** para agregar permisos a tu usuario. A continuación, selecciona **Create Your Own Policy**. Esto otorga permisos limitados, de modo que Braze solo pueda acceder a los contenedores especificados.

![Pantalla de creación de política de AWS IAM con opciones de política para la integración de S3.]({% image_buster /assets/img_archive/S3_CreatePolicy.png %})

{% alert note %}
Se requieren políticas diferentes para Currents y Dashboard Data Export. `s3:GetObject` es necesario para permitir que el backend de Braze realice el manejo de errores.
{% endalert %}

Especifica un nombre de política de tu elección e ingresa el siguiente fragmento de código en la sección **Policy Document**. Asegúrate de reemplazar `INSERTBUCKETNAME` con el nombre de tu contenedor. Sin estos permisos, la integración no pasará la verificación de credenciales y no se creará.

{% alert note %}
Si solo estás configurando el archivado de mensajes, usa el fragmento de código en la pestaña **Dashboard Data Export**.
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

Después de crear una nueva política, ve a **Users** y selecciona tu usuario específico. En la pestaña **Permissions**, selecciona **Attach Policy** y selecciona la nueva política que creaste. Ahora estás listo para vincular tus credenciales de AWS a tu cuenta de Braze.

![Pestaña de permisos del usuario de AWS IAM con la acción Attach Policy seleccionada.]({% image_buster /assets/img_archive/S3_AttachPolicy.png %})

### Paso 5: Vincular Braze a AWS {#secret-key-5}

{% alert note %}
Si solo estás configurando el archivado de mensajes, sigue los pasos en la pestaña **Dashboard Data Export**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

En Braze, ve a **Partner Integrations** > **Currents**.

A continuación, selecciona **Create New Current** y luego **Amazon S3 Data Export**.

Asigna un nombre a tu Current. En la sección **Credentials**, asegúrate de que **AWS Secret Access Key** esté seleccionado, y luego ingresa tu ID de acceso de S3, la clave de acceso secreta de AWS y el nombre del contenedor de AWS S3 en los campos designados.

{% multi_lang_include currents/contact_email_notifications.md %}

![Formulario de creación de nuevo Current en Braze para Amazon S3 con campos de credenciales de clave secreta de AWS.]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
Mantén tu ID de clave de acceso de AWS y tu clave de acceso secreta actualizados. Si las credenciales de tu conector expiran, el conector dejará de enviar eventos. Si esto persiste durante más de **5 días**, los eventos del conector se descartarán y los datos se perderán permanentemente.
{% endalert %}

También puedes agregar las siguientes personalizaciones según tus necesidades:

- **Ruta de carpeta:** El valor predeterminado es `currents`. Si esta carpeta no existe, Braze la creará automáticamente.
- **Cifrado AES-256 del lado del servidor en reposo:** El valor predeterminado es OFF e incluye el encabezado `x-amz-server-side-encryption`.

Selecciona **Launch Current** para continuar.

Una notificación te informará si tus credenciales se han validado correctamente. AWS S3 ya está configurado para Braze Currents.

{% endtab %}
{% tab Dashboard Data Export %}

En Braze, ve a **Partner Integrations** > **Technology Partners** y selecciona **Amazon S3**.

En la página **AWS Credentials**, asegúrate de que **AWS Secret Access Key** esté seleccionado, y luego ingresa tu ID de acceso de AWS, la clave de acceso secreta de AWS y el nombre del contenedor de AWS S3 en los campos designados. Al ingresar tu clave secreta, selecciona primero **Test Credentials** para asegurarte de que tus credenciales funcionen, y luego selecciona **Save** cuando sea exitoso.

![Página de credenciales del partner tecnológico Amazon S3 en Braze con acciones de prueba y guardado.]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
Siempre puedes obtener nuevas credenciales navegando a tu usuario y seleccionando **Create Access Key** en la pestaña **Security Credentials** dentro de la consola de AWS.
{% endalert %}

Una notificación te informará si tus credenciales se han validado correctamente. AWS S3 ahora está integrado en tu cuenta de Braze.

{% endtab %}
{% endtabs %}

## Método de autenticación con ARN de rol de AWS {#aws-role-arn-auth-method}

Este método de autenticación genera un nombre de recurso de Amazon (ARN) de rol que permite a la cuenta de Amazon de Braze autenticarse como miembro del rol que creaste para escribir datos en tu contenedor.

### Paso 1: Crear política {#role-arn-1}

Para empezar, inicia sesión en la consola de administración de AWS como administrador de la cuenta. Navega a la sección IAM de la consola de AWS, selecciona **Políticas** en la barra de navegación y selecciona **Crear política**.

![Página de políticas de IAM de AWS con el botón Crear política seleccionado.]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
Se requieren políticas diferentes para Currents y la exportación de datos del panel. `s3:GetObject` es necesario para permitir que el backend de Braze realice el manejo de errores.
{% endalert %}

Abre la pestaña **JSON** e introduce el siguiente fragmento de código en la sección **Documento de política**. Asegúrate de reemplazar `INSERTBUCKETNAME` con tu nombre de contenedor. Selecciona **Revisar política** cuando hayas terminado.

{% alert note %}
Si solo estás configurando el archivado de mensajes, utiliza el fragmento de código en la pestaña **Exportación de datos del panel**.
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
{% tab Exportación de datos del panel %}

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

A continuación, asigna un nombre y una descripción a la política y selecciona **Crear política**.

![Paso de revisión de política de IAM de AWS con campos para nombre y descripción de la política.]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![Lista de políticas de IAM de AWS mostrando la política de S3 recién creada.]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Paso 2: Crear rol {#role-arn-2}

Dentro de la misma sección IAM de la consola, selecciona **Roles** > **Crear rol**.

![Página de roles de IAM de AWS con el botón Crear rol seleccionado.]({{site.baseurl}}/assets/img/create_role_1_list.png)

Obtén tu ID de cuenta de Braze y tu ID externo desde tu cuenta de Braze:

- **Currents:** En Braze, ve a **Integraciones de partners** > **Currents**. A continuación, selecciona **Crear nuevo Current** y luego **Exportación de datos de Amazon S3**. Aquí encontrarás los identificadores necesarios para crear tu rol.
- **Exportación de datos del panel:** En Braze, ve a **Integraciones de partners** > **Partners tecnológicos** y selecciona **Amazon S3**. Aquí encontrarás los identificadores necesarios para crear tu rol. (Crea tus roles aquí si solo estás configurando el archivado de mensajes).

De vuelta en la consola de AWS, selecciona **Otra cuenta de AWS** como tipo de selector de entidad de confianza. Proporciona tu ID de cuenta de Braze, marca la casilla **Requerir ID externo** e introduce el ID externo de Braze. Selecciona **Siguiente** cuando hayas terminado.

![La página "Crear rol" de S3. Esta página tiene campos para nombre del rol, descripción del rol, entidades de confianza, políticas y límite de permisos.]({{site.baseurl}}/assets/img/create_role_2_another.png)

### Paso 3: Adjuntar política {#role-arn-3}

A continuación, adjunta la política que creaste anteriormente al rol. Busca la política en la barra de búsqueda y marca la casilla junto a la política para adjuntarla. Selecciona **Siguiente** cuando hayas terminado.

![ARN de rol]({{site.baseurl}}/assets/img/create_role_3_attach.png)

Asigna un nombre y una descripción al rol, y selecciona **Crear rol**.

![ARN de rol]({{site.baseurl}}/assets/img/create_role_4_name.png)

Ahora verás tu rol recién creado en la lista.

### Paso 4: Vincular a Braze AWS {#role-arn-4}

En la consola de AWS, busca tu rol recién creado en la lista. Selecciona el nombre para abrir los detalles de ese rol.

![Página de detalles del rol de IAM de AWS para el rol recién creado.]({{site.baseurl}}/assets/img/create_role_5_created.png)

Toma nota del **ARN de rol** en la parte superior de la página de resumen del rol.

![Resumen del rol de IAM de AWS mostrando el valor del ARN de rol.]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Regresa a tu cuenta de Braze y copia el ARN de rol en el campo proporcionado.

{% alert note %}
Si solo estás configurando el archivado de mensajes, sigue los pasos en la pestaña **Exportación de datos del panel**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

En Braze, ve a **Integraciones de partners** > **Currents**. A continuación, selecciona **Crear nuevo Current** y selecciona **Exportación de datos de Amazon S3**.

![Pantalla de configuración de Amazon S3 en Braze Currents con los campos de ARN de rol de AWS y contenedor.]({{site.baseurl}}/assets/img/currents-role-arn.png)

Asigna un nombre a tu Current. Luego, en la sección **Credenciales**, asegúrate de que **ARN de rol de AWS** esté seleccionado y proporciona tu ARN de rol y el nombre del contenedor de AWS S3 en los campos designados.

{% multi_lang_include currents/contact_email_notifications.md %}

También puedes añadir la siguiente personalización según tus necesidades:

- Ruta de carpeta (predeterminada: `currents`)
- Cifrado AES-256 en reposo del lado del servidor (predeterminado: DESACTIVADO) - Incluye el encabezado `x-amz-server-side-encryption`

Selecciona **Lanzar Current** para continuar. Una notificación indica si tus credenciales se han validado correctamente. AWS S3 está ahora configurado para Braze Currents.

{% alert important %}
Si recibes un error "Las credenciales de S3 no son válidas", esto puede deberse a que la integración se realizó demasiado rápido después de crear un rol en AWS. Espera e inténtalo de nuevo. Si el mensaje menciona acceso a `PutObject` o cifrado del lado del servidor en las exportaciones de datos del panel, consulta [Solución de problemas de errores de credenciales de S3](#troubleshooting).
{% endalert %}

{% endtab %}
{% tab Exportación de datos del panel %}

En Braze, ve a la página **Partners tecnológicos** en **Integraciones** y selecciona **Amazon S3**.

![Página del partner tecnológico Amazon S3 en Braze con las credenciales de ARN de rol de AWS seleccionadas.]({{site.baseurl}}/assets/img/data-export-role-arn.png)

En la página **Credenciales de AWS**, asegúrate de que el botón de opción **ARN de rol de AWS** esté seleccionado y luego introduce tu ARN de rol y el nombre del contenedor de AWS S3 en los campos designados. Selecciona **Probar credenciales** primero para confirmar que tus credenciales funcionan correctamente, y luego selecciona **Guardar** cuando sea exitoso.

{% alert tip %}
Siempre puedes obtener nuevas credenciales navegando a tu usuario y seleccionando **Crear clave de acceso** en la pestaña **Credenciales de seguridad** dentro de la consola de AWS.
{% endalert %}

Una notificación te informa si tus credenciales se han validado correctamente. AWS S3 está ahora integrado en tu cuenta de Braze.

{% endtab %}
{% endtabs %}

## Actualización de credenciales de Amazon S3 para Currents {#updating-currents-credentials}

Puedes actualizar las credenciales de Amazon S3 en un conector de Braze Currents existente sin detener la integración ni perder los datos ya exportados a tu contenedor.

Para actualizar las credenciales, o para cambiar entre **AWS Secret Access Key** y **AWS Role ARN**, completa los pasos de IAM y AWS para el método elegido descritos anteriormente en este artículo (políticas, usuario o rol, e identificadores según sea necesario).

Cuando hayas terminado de preparar las credenciales en AWS, ve a **Partner Integrations** > **Currents** en Braze, localiza tu conector de Amazon S3 en la lista, selecciona **Edit**, actualiza las **Credentials** y selecciona **Update Current**. Braze valida las credenciales que introduces; tu conector sigue funcionando y los datos que ya están en tu contenedor permanecen disponibles. Para más información, consulta [Actualización de Currents en Configurar Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#updating-currents).

## Comportamiento de la exportación {#export-behavior}

Los usuarios que han integrado una solución de almacenamiento de datos en el cloud y exportan API, informes del panel o informes CSV experimentan lo siguiente:

- Todas las exportaciones de API no devuelven una URL de descarga en el cuerpo de la respuesta y deben recuperarse a través del almacenamiento de datos.
- Todos los informes del panel e informes CSV se envían al correo electrónico del usuario para su descarga (no se requieren permisos de almacenamiento) y se respaldan en el almacenamiento de datos.

### Error `Unable to connect to S3, please validate that your credentials are correct` {#unable-to-connect-to-s3-please-validate-that-your-credentials-are-correct-error}

Si ves este error al descargar una exportación CSV, abre la integración de [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3) en la página **Technology Partners** y selecciona **Test Credentials**. El resultado explica qué falló en la validación; por ejemplo, la clave podría no tener el permiso `GetObject`, lo que impide que Braze genere enlaces de descarga.

Actualiza tu política de IAM para que el usuario o rol de la integración pueda llamar a `s3:GetObject` en el contenedor de S3 y la ruta de objetos configurada en tu integración de Braze. Para más problemas de exportación, consulta [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).

{% alert important %}
**Requisito de formato JSON:** Para las exportaciones JSON, Braze utiliza el formato JSONL (JSON delimitado por saltos de línea), donde cada línea contiene un objeto JSON independiente. Este formato difiere del JSON estándar, que es un único array u objeto JSON. Cada línea del archivo exportado es un objeto JSON válido, pero el archivo en su conjunto no es un único documento JSON válido. Al procesar estos archivos, analiza cada línea individualmente como un objeto JSON independiente en lugar de intentar analizar el archivo completo como un único documento JSON.

Las exportaciones de Currents utilizan el formato Apache Avro (archivos `.avro`), no JSON. Este requisito de formato JSON se aplica a las exportaciones de datos del panel y a las exportaciones de API.
{% endalert %}

## Múltiples conectores {#multiple-connectors}

Si tienes la intención de crear más de un conector de Currents para enviar a tu contenedor de S3, puedes usar las mismas credenciales, pero debes especificar una ruta de carpeta diferente para cada uno. Puedes crearlos en el mismo espacio de trabajo, o dividirlos y crearlos en múltiples espacios de trabajo. También tienes la opción de crear una política única para cada integración, o crear una política que cubra ambas integraciones.

Si planeas usar el mismo contenedor de S3 tanto para Currents como para exportaciones de datos, necesitas crear dos políticas separadas, ya que cada integración requiere permisos diferentes.

## Solución de problemas {#troubleshooting}

### Error: La cuenta no tiene acceso a `PutObject` {#error-account-does-not-have-putobject-access}

Si ves el siguiente error al guardar las credenciales de Amazon S3 para las exportaciones de datos del panel, puede deberse a permisos incorrectos o a la configuración de cifrado del lado del servidor.

```
S3 Credentials are invalid because this account does not have 'PutObject access'. Please check the permissions and ensure that this key has access to 'PutObject' in the 'CUSTOMER-BUCKET-HERE' bucket.
```

Para resolver este problema, comprueba las siguientes áreas.

#### Política de contenedor incorrecta {#incorrect-bucket-policy}

Confirma que creaste una política con los permisos correctos como se describe en [Integración con Amazon S3](#integration) (usa la política de **Dashboard Data Export** para tu método de autenticación).

#### Cifrado del lado del servidor {#server-side-encryption}

```
User: arn:aws:sts::XXX:assumed-role/braze-iam-role/braze is not authorized to perform: kms:GenerateDataKey on resource: arn:aws:XXX because no identity-based policy allows the kms:GenerateDataKey action
```

Si recibes este mensaje de error de [soporte de Braze]({{site.baseurl}}/braze_support) o en tus registros de AWS, tu contenedor de S3 está configurado con cifrado de AWS Key Management Service (SSE-KMS). Braze no es compatible con SSE-KMS para Currents ni para las exportaciones de datos del panel. Para resolverlo, desactiva SSE-KMS en tu contenedor de S3.

{% alert note %}
Braze es compatible con el cifrado del lado del servidor mediante claves administradas por S3 (SSE-S3), que es compatible tanto con Currents como con las exportaciones de datos del panel.
{% endalert %}

#### Comprueba los permisos adicionales {#check-additional-permissions}

Asegúrate de tener los permisos necesarios, incluidos `s3:GetBucketLocation` y `s3:PutObject`.