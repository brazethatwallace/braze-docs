---
nav_title: Exportación de eventos de seguridad con S3
article_title: Exportación de configuración de seguridad con S3
page_order: 1
page_type: reference
description: "Este artículo de referencia explica cómo exportar automáticamente los eventos de seguridad cada día a medianoche UTC a Amazon S3."
---

# Exportación de eventos de seguridad con Amazon S3 {#security-events-export-with-amazon-s3}

> Puedes exportar automáticamente los eventos de seguridad a Amazon S3, un proveedor de almacenamiento en la nube, con una tarea diaria que se ejecuta a medianoche UTC. Una vez configurado, no necesitas exportar manualmente los eventos de seguridad desde el dashboard. La tarea exporta los eventos de seguridad de las últimas 24 horas en formato CSV al almacenamiento S3 que hayas configurado. El archivo CSV utiliza las mismas columnas que un informe exportado manualmente, además de una columna `Version`.

{% alert note %}
El límite de 10 000 filas solo se aplica a la descarga manual de informes CSV desde el dashboard. Las exportaciones de eventos de seguridad a S3 no están sujetas a este límite de filas.
{% endalert %}

Braze admite dos métodos diferentes de autenticación y autorización de S3 para configurar la exportación a Amazon S3:

- Método de clave de acceso secreta de AWS
- Método ARN del rol de AWS

## Método de clave de acceso secreta de AWS {#aws-secret-access-key-method}

Este método genera una clave secreta y un ID de clave de acceso que permite a Braze autenticarse como usuario en tu cuenta de AWS para escribir datos en tu contenedor.

### Paso 1: Crear un usuario de gestión de identidades y accesos (IAM) {#step-1-create-an-identity-and-access-management-iam-user}

Para recuperar tu clave de acceso secreta y tu ID de clave de acceso, deberás crear un usuario de IAM siguiendo las instrucciones en [Configurar tu cuenta de AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin).

### Paso 2: Obtener credenciales {#step-2-get-credentials}

1. Después de crear un nuevo usuario, genera la clave de acceso y descarga tu ID de clave de acceso y la clave de acceso secreta.

![Una página de resumen para un rol llamado "liyu-chen-test".]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2. Toma nota de estas credenciales en algún lugar o descarga los archivos de credenciales, ya que necesitarás ingresarlas en Braze más adelante.

![Campos que contienen la clave de acceso y la clave de acceso secreta.]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### Paso 3: Crear política {#step-3-create-policy}

1. Ve a **IAM** (gestión de identidades y accesos) > **Policies** > **Create Policy** para agregar permisos a tu usuario.
2. Selecciona **Create Your Own Policy**, que otorga permisos limitados para que Braze solo pueda acceder a los contenedores especificados.
3. Especifica un nombre de política de tu elección.
4. Ingresa el siguiente fragmento de código en la sección **Policy Document**. Asegúrate de reemplazar "INSERTBUCKETNAME" con el nombre de tu contenedor. Sin estos permisos, la integración fallará en la verificación de credenciales y no se creará.

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

### Paso 4: Adjuntar política {#step-4-attach-policy}

1. Después de crear una nueva política, ve a **Users** y selecciona tu usuario específico.
2. En la pestaña **Permissions**, selecciona **Add Permissions**, adjunta directamente la política y luego selecciona esa política.

¡Ahora estás listo para vincular tus credenciales de AWS a tu cuenta de Braze!

### Paso 5: Vincular Braze a AWS {#step-5-link-braze-to-aws}

1. En Braze, ve a **Configuración** > **Configuración de empresa** > **Configuración de administrador** > **Configuración de seguridad** y desplázate hasta la sección **Security Event Download**.
2. Activa **Export to AWS S3** en **Export to cloud storage** y selecciona **AWS secret access key**, lo que habilita la exportación a S3.
3. Ingresa lo siguiente:

- ID de clave de acceso de AWS
- Nombre de contenedor de AWS
- Clave de acceso secreta de AWS
    - Al ingresar esta clave, primero selecciona **Test Credentials** para confirmar que tus credenciales funcionan.

![La página "Security Event Download" con los campos de cuenta de Braze e ID externo de Braze completados.]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4. Selecciona **Guardar cambios**.

¡Has integrado AWS S3 en tu cuenta de Braze!

## Método ARN del rol de AWS {#aws-role-arn-method}

El método ARN del rol de AWS genera un nombre de recurso de Amazon (ARN) del rol que permite a la cuenta de Amazon de Braze autenticarse como miembro de ese rol.

### Paso 1: Crear política {#step-1-create-policy}

1. Inicia sesión en la consola de administración de AWS como administrador de la cuenta.
2. En la consola de AWS, ve a la sección **IAM** (gestión de identidades y accesos) > **Policies** y luego selecciona **Create Policy**.

![Una página con una lista de políticas y un botón para "Create policy".]({% image_buster /assets/img/security_export/policies.png %})

{: start="3"}
3. Abre la pestaña **JSON** e ingresa el siguiente fragmento de código en la sección **Policy Document**. Asegúrate de reemplazar `INSERTBUCKETNAME` con el nombre de tu contenedor.

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

{: start="4"}
4. Selecciona **Next** después de revisar la política.

![Una página que te permite revisar tu política y opcionalmente agregar permisos.]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5. Dale un nombre y una descripción a la política, y luego selecciona **Create Policy**.

![Una página para revisar y crear tu política.]({% image_buster /assets/img/security_export/review_and_create.png %})

### Paso 2: Crear rol {#step-2-create-role}

1. En Braze, ve a **Configuración** > **Configuración de empresa** > **Configuración de administrador** > **Configuración de seguridad** y desplázate hasta la sección **Security Event Download**.
2. Selecciona **AWS Role ARN**.
3. Toma nota de los identificadores, el ID de cuenta de Braze y el ID externo de Braze necesarios para crear tu rol.

![La página "Security Event Download" con los campos de cuenta de Braze e ID externo de Braze completados.]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. En la consola de AWS, ve a la sección **IAM** (gestión de identidades y accesos) > **Roles** > **Create Role**.
5. Selecciona **Another AWS Account** como tipo de SELECTOR de entidad de confianza.
6. Proporciona tu ID de cuenta de Braze, marca la casilla **Require external ID** y luego ingresa tu ID externo de Braze.
7. Selecciona **Next** cuando hayas terminado.

![Una página con opciones para seleccionar un tipo de entidad de confianza y proporcionar información sobre tu cuenta de AWS.]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### Paso 3: Adjuntar política {#step-3-attach-policy}

1. Busca la política que creaste anteriormente en la barra de búsqueda y luego marca la casilla junto a la política para adjuntarla.
2. Selecciona **Next**.

![Una lista de políticas con columnas para su tipo y descripción.]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3. Dale un nombre y una descripción al rol, y selecciona **Create Role**.

![Campos para proporcionar detalles del rol, como el nombre, la descripción, la política de confianza, los permisos y las etiquetas.]({% image_buster /assets/img/security_export/name_review_create.png %})

¡Tu rol recién creado aparecerá en la lista!

### Paso 4: Vincular a Braze AWS {#step-4-link-to-braze-aws}

1. En la consola de AWS, busca tu rol recién creado en la lista. Selecciona el nombre para abrir los detalles de ese rol y toma nota del **ARN**.

![La página de resumen para un rol llamado "security-event-export-olaf".]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2. En Braze, ve a **Configuración** > **Configuración de empresa** > **Configuración de administrador** > **Configuración de seguridad** y desplázate hasta la sección **Security Event Download**.

![Sección "Security Event Download" con un interruptor activado para "Export to AWS S3".]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3. Asegúrate de que **AWS role ARN** esté seleccionado, luego ingresa tu ARN del rol y el nombre del contenedor de AWS S3 en los campos designados.
4. Selecciona **Test Credentials** para confirmar que tus credenciales funcionan correctamente.
5. Selecciona **Guardar cambios**.

¡Has integrado AWS S3 en tu cuenta de Braze!