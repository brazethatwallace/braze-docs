---
nav_title: Fivetran
article_title: Fivetran
alias: /partners/fivetran/
description: "Este artículo de referencia describe la asociación entre Braze y Fivetran, una herramienta de automatización del flujo de trabajo que puede ayudarte en la toma de decisiones basada en datos mediante la entrega de datos listos para consultar en tu almacén en la nube."
page_type: partner
search_tag: Partner
tool: Currents

---

# Fivetran

> [Fivetran](https://fivetran.com/) es una marca mundialmente reconocida cuyos productos centrados en el analista y pipelines totalmente gestionados permiten tomar decisiones basadas en datos mediante la entrega de datos listos para consultar en tu almacén en la nube.

La integración de Braze y Fivetran permite a los usuarios crear un pipeline sin mantenimiento que te permite recopilar y analizar datos de Braze conectando todas tus aplicaciones y bases de datos a un almacén central. Una vez recopilados los datos en el almacén central, los equipos de datos pueden explorar los datos de Braze con eficacia utilizando sus herramientas de inteligencia empresarial preferidas.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Fivetran | Se necesita una cuenta de [Fivetran](https://fivetran.com/login?next=%2Fdashboard) para beneficiarse de esta asociación. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con los siguientes permisos:<br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- Canvas.list<br>- Canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get <br><br> Puedes crearla en el dashboard de Braze desde **Settings** > **API Keys**. |
| Punto de conexión REST or transferencia de estado representacional de Braze  | La URL de tu punto de conexión REST or transferencia de estado representacional. Tu punto de conexión dependerá de la [URL de Braze de tu instancia]({{site.baseurl}}/api/basics/#api-definitions). |
| Braze Currents | [Braze Currents](https://www.braze.com/product/data-agility-management/currents/) debe estar conectado a Amazon S3 o Google Cloud Storage. |
| Amazon S3 o Google Cloud Storage | Esta integración requiere que tengas acceso a un Amazon S3 o Google Cloud Storage. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integración {#integration}

La siguiente integración de Currents es compatible tanto con [Amazon S3](#setting-up-braze-currents-for-s3) como con [Google Cloud Storage](#setting-up-braze-currents-for-google-cloud-storage).

### Configuración de Braze Currents para S3 {#setting-up-braze-currents-for-s3}

#### Paso 1: Localiza tu ID externo {#step-one}

En el [dashboard de Fivetran](https://fivetran.com/dashboard), selecciona **+ Connector** y, a continuación, selecciona el conector **Braze** para iniciar el formulario de configuración. A continuación, selecciona **Amazon S3**. Toma nota del ID externo proporcionado aquí; lo necesitarás para permitir que Fivetran acceda a tu contenedor de S3.

![El formulario de configuración del conector Braze en Fivetran. El campo de ID externo necesario para este paso se encuentra en el centro de la página, en un recuadro gris claro.]({% image_buster /assets/img/fivetran_braze_setupform_as3.png %})

#### Paso 2: Dar acceso a Fivetran a un contenedor de S3 especificado {#step-2-give-fivetran-access-to-a-specified-s3-bucket}

##### Creación de una política IAM {#creating-an-iam-policy}

Abre la [consola de Amazon IAM](https://console.aws.amazon.com/iam/home#home) y navega a **Policies > Create Policy**.

![Consola de Amazon IAM con la lista de políticas.]({% image_buster /assets/img/fivetran_as3_iam.png %})

A continuación, abre la pestaña **JSON** y pega la siguiente política. Asegúrate de sustituir `{your-bucket-name}` por el nombre de tu contenedor de S3.

{% raw %}
```json
{
"Version": "2012-10-17",
"Statement": [
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}/*"
    },
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}"
    }
  ]
}
```
{% endraw %}

Por último, selecciona **Review Policy** y asigna un nombre y una descripción únicos a la política. Selecciona **Create Policy** para crear tu política.

![Campos para nombrar la política y proporcionar una descripción.]({% image_buster /assets/img/fivetran_iam_policy_meta.png %})

##### Crear un rol IAM {#step-two}

En AWS, navega a **Roles** y selecciona **Create New Role**.

![La página "Roles" con el botón para crear un nuevo rol.]({% image_buster /assets/img/fivetran_iam_new_role.png %})

Selecciona **Another AWS Account** e introduce el ID de la cuenta de Fivetran `834469178297`. Asegúrate de marcar la casilla **Require external ID**. Aquí proporcionarás el ID externo encontrado en el paso 1.

![El campo para introducir tu "Account ID", una casilla de verificación para requerir el ID externo y un cuadro de texto en blanco para introducir tu "External ID".]({% image_buster /assets/img/fivetran_another_aws_account.png %})

A continuación, selecciona **Next: Permissions** para seleccionar la política que acabas de crear.

![Lista de políticas.]({% image_buster /assets/img/fivetran_as3_select_policy.png %})

Selecciona **Next: Review**, asigna un nombre a tu nuevo rol (como Fivetran) y selecciona **Create Role**. Una vez creado el rol, selecciónalo y anota el Role ARN que se muestra.

![El ARN de Amazon S3 que aparece en el rol.]({% image_buster /assets/img/fivetran_iam_role_arn.png %})

{% alert note %}
Puedes especificar permisos para el Role ARN que designes para Fivetran. Dar permisos selectivos a este rol permitirá a Fivetran sincronizar solo lo que tiene permiso para ver.
{% endalert %}

#### Paso 3: Completar el conector Fivetran {#step-3-complete-the-fivetran-connector}

En Fivetran, selecciona **+ Connector** y, a continuación, selecciona el conector **Braze** para iniciar el formulario de configuración. En el formulario, rellena los campos indicados con los valores adecuados:
- `Destination schema`: un nombre de esquema único.
- `API URL`: tu punto de conexión de la REST or transferencia de estado representacional API de Braze.
- `API Key`: tu clave de API REST or transferencia de estado representacional de Braze.
- `External ID`: el ID externo establecido en el [paso 2](#step-two) de las instrucciones de configuración de Currents. Este ID es un valor fijo.
- `Bucket`: se encuentra en tu cuenta de Braze navegando a **Partner Integrations** > **Data Export** > el nombre de tu Current.
- `Role ARN`: el Role ARN se encuentra en el [paso 1](#step-one) de las instrucciones de configuración de Current.

{% alert important %}
Asegúrate de que **Amazon S3** está seleccionado como opción de **Cloud Storage**.
{% endalert %}

Por último, selecciona **Save & Test**, ¡y Fivetran hará el resto sincronizándose con los datos de tu cuenta de Braze!

### Configuración de Braze Currents para Google Cloud Storage {#setting-up-braze-currents-for-google-cloud-storage}

#### Paso 1: Recupera tu correo electrónico de Fivetran de Google Cloud Storage {#step-one2}

En el [dashboard de Fivetran](https://fivetran.com/dashboard), selecciona **+ Connector** y, a continuación, selecciona el conector **Braze** para iniciar el formulario de configuración. A continuación, selecciona **Google Cloud Storage**. Anota la dirección de correo electrónico que aparece.

![El formulario de configuración del conector Braze en Fivetran. El campo de correo electrónico necesario para este paso se encuentra en el centro de la página, en un recuadro gris claro.]({% image_buster /assets/img/fivetran_braze_setupform_gcs.png %})

#### Paso 2: Conceder acceso al contenedor {#step-2-grant-bucket-access}

Navega a tu [consola de Google Storage](https://console.cloud.google.com/storage/browser) y selecciona el contenedor con el que configuraste Braze Currents, y selecciona **Edit bucket permissions**.

![Los contenedores disponibles en Google Storage Console. Localiza un contenedor y selecciona el icono vertical de tres puntos para abrir el desplegable que te permite editar los permisos del contenedor.]({% image_buster /assets/img/fivetran_edit_bucket_permissions_gcs.png %})

A continuación, concede acceso de `Storage Object Viewer` al correo electrónico del [paso 1](#step-one2) añadiéndolo como miembro. Anota el nombre del contenedor; lo necesitarás en el siguiente paso para configurar Fivetran.

![Contenedor con permisos.]({% image_buster /assets/img/fivetran_add_members_gcs.png %})

#### Paso 3: Completar el conector Fivetran

En Fivetran, selecciona **+ Connector** y, a continuación, selecciona el conector **Braze** para iniciar el formulario de configuración. En el formulario, rellena los campos indicados con los valores adecuados:
- `Destination schema`: un nombre de esquema único.
- `API URL`: tu punto de conexión de la REST or transferencia de estado representacional API de Braze.
- `API Key`: tu clave de API REST or transferencia de estado representacional de Braze.
- `Bucket Name`: se encuentra en tu cuenta de Braze navegando a **Partner Integrations** > **Data Export** > el nombre de tu Current.
- `Folder`: se encuentra en tu cuenta de Braze navegando a **Partner Integrations** > **Data Export** > el nombre de tu Current.

{% alert important %}
Asegúrate de que **Google Cloud Storage** está seleccionado como opción de **Cloud Storage**.
{% endalert %}

Por último, selecciona **Save & Test**, ¡y Fivetran hará el resto sincronizándose con los datos de tu cuenta de Braze!