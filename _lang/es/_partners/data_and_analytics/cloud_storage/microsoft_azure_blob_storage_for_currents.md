---
nav_title: Microsoft Azure Blob Storage
article_title: Microsoft Azure Blob Storage
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "Este artículo de referencia describe la asociación entre Braze Currents y Microsoft Azure Blob Storage, un almacenamiento de objetos masivamente escalable para datos no estructurados."
page_type: partner
tool: Currents
search_tag: Partner

---

# Microsoft Azure Blob Storage

> [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) es un almacenamiento de objetos masivamente escalable para datos no estructurados ofrecido por Microsoft como parte de la línea de productos Azure.

{% alert important %}
Si vas a cambiar de proveedor de almacenamiento en la nube, ponte en contacto con tu administrador del éxito del cliente de Braze para que te ayude a configurar y validar tu nueva integración.
{% endalert %}

La integración de Braze y Microsoft Azure Blob Storage te permite exportar datos a Azure y transmitir datos a Currents. Más tarde, puedes utilizar un proceso ETL or extraer, transformar, cargar (ETL or extraer, transformar, cargar or extraer, transformar, cargar) para transferir tus datos a otras ubicaciones.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Microsoft Azure y cuenta de almacenamiento en Azure | Se requieren una cuenta de Microsoft Azure y una cuenta de almacenamiento en Azure para aprovechar esta integración. |
| Currents | Para exportar datos a Currents, debes tener [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) configurado en tu cuenta. Currents no es necesario si solo estás configurando el archivado de mensajes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Para integrarte con Microsoft Azure Blob Storage, debes tener una cuenta de almacenamiento y un contenedor que permita a Braze exportar datos de vuelta a Azure o transmitir datos de Currents. Braze admite dos métodos de autenticación:

- [Método de cadena de conexión](#connection-string-auth-method)
- [Método de entidad de servicio con certificado](#certificate-service-principal-auth-method) (solo Currents)

## Método de autenticación con cadena de conexión {#connection-string-auth-method}

### Paso 1: Crear una cuenta de almacenamiento {#step-1-create-a-storage-account}

En Microsoft Azure, navega a **Storage Accounts** en la barra lateral y haz clic en **+ Add** para crear una nueva cuenta de almacenamiento. A continuación, proporciona un nombre para la cuenta de almacenamiento. No será necesario actualizar otras configuraciones predeterminadas. Por último, selecciona **Review + create**.

Aunque ya tengas una cuenta de almacenamiento, te recomendamos crear una nueva específicamente para tus datos de Braze.

![La página de creación de cuenta de almacenamiento de Microsoft Azure en la pestaña Basics, con el campo de nombre de la cuenta de almacenamiento resaltado.]({% image_buster /assets/img/azure-currents-step-1.png %})

### Paso 2: Obtener la cadena de conexión {#step-2-get-the-connection-string}

Una vez desplegada la cuenta de almacenamiento, navega al menú **Access Keys** desde la cuenta de almacenamiento y toma nota de la cadena de conexión.

Microsoft proporciona dos claves de acceso para mantener las conexiones usando una clave mientras se regenera la otra. Solo necesitas la cadena de conexión de una de ellas.

{% alert note %}
Braze utiliza la cadena de conexión de este menú, no la clave.
{% endalert %}

![La página de claves de acceso de una cuenta de almacenamiento de Azure, con el campo de cadena de conexión bajo key1 resaltado.]({% image_buster /assets/img/azure-currents-step-2.png %})

### Paso 3: Crear un contenedor de servicio de blobs {#step-3-create-a-blob-service-container}

Navega al menú **Blobs** en la sección **Blob Service** de tu cuenta de almacenamiento. Crea un contenedor de servicio de blobs dentro de la cuenta de almacenamiento que creaste anteriormente.

Proporciona un nombre para tu contenedor de servicio de blobs. No será necesario actualizar otras configuraciones predeterminadas.

![La página de blobs de una cuenta de almacenamiento de Azure en Blob Service, con la opción de añadir un contenedor.]({% image_buster /assets/img/azure-currents-step-3.png %})

### Paso 4: Configurar Currents {#step-4-set-up-currents}

En Braze, navega a **Currents > + Create Current > Azure Blob Data Export** y proporciona el nombre de tu integración y el correo electrónico de contacto.

{% multi_lang_include currents/contact_email_notifications.md %}

A continuación, proporciona tu cadena de conexión, nombre del contenedor y prefijo de BlobStorage (opcional).

![La página de Currents de almacenamiento de blobs de Microsoft Azure en Braze. En esta página existen campos para nombre de integración, correo electrónico de contacto, cadena de conexión, nombre del contenedor y prefijo.]({% image_buster /assets/img/maz.png %})

Por último, desplázate hasta la parte inferior de la página y selecciona qué eventos de participación de mensajes o eventos de comportamiento del cliente deseas exportar. Cuando hayas terminado, lanza tu Current.

### Paso 5: Configurar la exportación de datos de Azure {#step-5-set-up-azure-data-export}

Lo siguiente configura las credenciales que se utilizan para:
1. Exportaciones de Segment a través de la API
2. Exportaciones CSV (exportación de datos de usuario de Campaign, Segment y Canvas a través del panel)
3. Informes de participación

En Braze, navega a **Partner Integrations** > **Technology Partners** > **Microsoft Azure** y proporciona tu cadena de conexión, nombre del contenedor de almacenamiento de Azure y prefijo de almacenamiento de Azure.

A continuación, asegúrate de que la casilla **Make this the default data export destination** esté marcada, esto garantizará que tus datos exportados se envíen a Azure. Cuando hayas terminado, guarda tu integración.

![La página de exportación de datos de Microsoft Azure en Braze. En esta página existen campos para cadena de conexión, nombre del contenedor y prefijo.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
Es importante mantener tu cadena de conexión actualizada; si las credenciales de tu conector caducan, el conector dejará de enviar eventos. Si esto persiste durante más de 48 horas, los eventos del conector se descartarán y los datos se perderán permanentemente.
{% endalert %}

## Método de autenticación con entidad de servicio de certificado {#certificate-service-principal-auth-method}

Este método se autentica en Microsoft Entra ID mediante un certificado y luego escribe en tu contenedor usando el control de acceso basado en roles (RBAC) de Azure sin una clave de cuenta compartida. Está disponible solo para Braze Currents.

{% alert note %}
Solo subes el certificado público a Microsoft Entra ID; tu clave privada nunca se envía a Azure. Braze almacena tu certificado y clave privada cifrados en reposo, concede acceso únicamente a través del rol [Storage Blob Data Contributor](#cert-sp-4) que asignas, y puedes revocar ese acceso en cualquier momento eliminando el certificado del registro de tu aplicación en Azure.
{% endalert %}

Antes de comenzar, [crea una cuenta de almacenamiento](#step-1-create-a-storage-account) y un [contenedor de servicio de blobs](#step-3-create-a-blob-service-container) como se describe en el [Método de cadena de conexión](#connection-string-auth-method).

### Paso 1: Registrar una aplicación {#cert-sp-1}

En Microsoft Azure, navega a **Microsoft Entra ID** > **App registrations** > **+ New registration**. Proporciona un nombre (por ejemplo, `braze-currents`) y selecciona **Register**. Para pasos detallados, consulta la documentación de Microsoft [Register an application with the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app).

En la página **Overview** del registro de tu nueva aplicación, toma nota de los siguientes valores. Proporcionarás ambos a Braze en el [Paso 6](#cert-sp-6).

- **Application (client) ID**
- **Directory (tenant) ID**

### Paso 2: Crear un certificado {#cert-sp-2}

Braze se autentica usando un certificado: subes el **certificado público** a Azure y proporcionas a Braze el **certificado junto con su clave privada**.

Para generar un certificado autofirmado y una clave privada RSA de 2048 bits sin cifrar, ejecuta:

```bash
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem \
  -days 730 -nodes -subj "/CN=braze-currents"
```

Esto crea dos archivos:

| Archivo | Propósito |
| ---- | ------- |
| `cert.pem` | Tu certificado público. Súbelo a Azure en el siguiente paso. |
| `key.pem` | Tu clave privada. Nunca subas esto a Azure. Lo proporcionarás a Braze en el [Paso 6](#cert-sp-6). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Archivos de certificado" }

{% alert important %}
La clave privada debe estar sin cifrar; no puede estar protegida por una frase de contraseña. Solo sube el certificado público a Azure; nunca subas tu clave privada.
{% endalert %}

**¿Ya tienes un certificado?** Si tienes un certificado existente como archivo `.pfx` —por ejemplo, de Azure Key Vault, tu autoridad de certificación o el [método PowerShell de Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-self-signed-certificate)— conviértelo al formato que Braze requiere en lugar de generar uno nuevo:

```bash
# The public certificate to upload to Azure (Step 3)
openssl pkcs12 -in your-cert.pfx -nokeys -out cert.pem

# The certificate and its unencrypted private key to give to Braze (Step 6)
openssl pkcs12 -in your-cert.pfx -nodes -out braze-currents.pem
```

Ingresa tu contraseña `.pfx` cuando se te solicite. La opción `-nodes` exporta la clave privada sin cifrar, como lo requiere Braze.

### Paso 3: Subir el certificado {#cert-sp-3}

En el registro de tu aplicación, navega a **Certificates & secrets** > **Certificates** > **Upload certificate** y sube el archivo `cert.pem` que creaste en el paso anterior. Agrega una descripción y selecciona **Add**. Para pasos detallados, consulta la documentación de Microsoft [Add and manage app credentials in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials).

Toma nota de la fecha de expiración de tu certificado. Consulta [Actualización de credenciales de Azure para Currents](#updating-currents-credentials).

### Paso 4: Conceder acceso a tu cuenta de almacenamiento {#cert-sp-4}

A continuación, otorga permiso a tu registro de aplicación para escribir en tu contenedor.

Navega a tu cuenta de almacenamiento y selecciona **Access Control (IAM)** > **+ Add** > **Add role assignment**. Luego:

1. En la pestaña **Role**, selecciona **[Storage Blob Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/storage#storage-blob-data-contributor)**.
2. En la pestaña **Members**, selecciona **User, group, or service principal**, selecciona **+ Select members** y busca el nombre del registro de aplicación que creaste en el [Paso 1](#cert-sp-1).
3. Selecciona **Review + assign**.

Para pasos detallados, consulta la documentación de Microsoft [Assign an Azure role for access to blob data](https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access).

![La pestaña de asignaciones de roles de Access Control (IAM) para una cuenta de almacenamiento, mostrando una entidad de servicio y un grupo con el rol Storage Blob Data Contributor asignado.]({% image_buster /assets/img/azure-currents-cert-sp-1.png %})

{% alert note %}
Asigna el rol a nivel de la **cuenta de almacenamiento** en lugar de en un contenedor individual.
{% endalert %}

{% alert important %}
Sin esta asignación de rol, Braze puede autenticarse en Microsoft Entra ID pero no podrá escribir en tu contenedor.
{% endalert %}

### Paso 5: Obtener el endpoint de tu cuenta {#cert-sp-5}

Desde tu cuenta de almacenamiento, navega a **Settings** > **Endpoints** y toma nota del endpoint de **Blob service**. Se ve como `https://<your-storage-account>.blob.core.windows.net`.

![La página de endpoints de la cuenta de almacenamiento con el endpoint de Blob service resaltado.]({% image_buster /assets/img/azure-currents-cert-sp-2.png %})

{% alert note %}
La autenticación con entidad de servicio de certificado solo es compatible con la nube pública de Azure. Tu endpoint de blobs debe terminar en `.blob.core.windows.net`.
{% endalert %}

### Paso 6: Configurar Currents {#cert-sp-6}

Braze necesita un único archivo PEM que contenga tu certificado y su clave privada sin cifrar. Si generaste un nuevo certificado en el [Paso 2](#cert-sp-2), combina los dos archivos en uno:

```bash
cat cert.pem key.pem > braze-currents.pem
```

Si convertiste un archivo `.pfx` existente en el [Paso 2](#cert-sp-2), ya tienes este archivo `braze-currents.pem`.

En Braze, navega a **Currents** > **+ Create Current** > **Azure Blob Data Export** y proporciona el nombre de tu integración y el correo electrónico de contacto.

{% multi_lang_include currents/contact_email_notifications.md %}

En **Credentials**, selecciona **Certificate Service Principal** y proporciona lo siguiente:

| Campo | Valor |
| ----- | ----- |
| Tenant ID | El **Directory (tenant) ID** del [Paso 1](#cert-sp-1). |
| Client ID | El **Application (client) ID** del [Paso 1](#cert-sp-1). |
| Account Endpoint | El endpoint de **Blob service** del [Paso 5](#cert-sp-5). |
| Certificate | El archivo `braze-currents.pem` que contiene tu certificado y su clave privada sin cifrar. |
| Container Name | El nombre de tu contenedor de blobs. |
| Prefix | Opcional. Un prefijo de ruta para tus datos exportados dentro del contenedor. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos de entidad de servicio de certificado" }

![La página de Azure Blob Data Export en Braze con Certificate Service Principal seleccionado, mostrando los campos Tenant ID, Client ID, Account Endpoint, Certificate, Container Name y Prefix.]({% image_buster /assets/img/azure-currents-cert-sp-3.png %})

Cuando guardes, Braze validará las credenciales que ingresaste.

Finalmente, desplázate hasta la parte inferior de la página y selecciona qué eventos de participación de mensajes o eventos de comportamiento del cliente deseas exportar. Cuando hayas terminado, lanza tu Current.

## Actualización de credenciales de Azure para Currents {#updating-currents-credentials}

Puedes actualizar las credenciales de Azure en un conector de Braze Currents existente sin detener la integración ni perder datos ya exportados a tu contenedor.

Para actualizar las credenciales, o para cambiar entre los métodos de **cadena de conexión** y **entidad de servicio de certificado**, completa los pasos del lado de Azure para el método elegido descritos anteriormente en este artículo. Luego, en Braze, ve a **Currents**, localiza tu conector de Azure Blob en la lista, selecciona **Edit Current**, actualiza las **credenciales** y selecciona **Update Current**. Braze valida las credenciales que introduzcas; tu conector sigue funcionando y los datos que ya están en tu contenedor permanecen disponibles. Para más información, consulta [Actualización de Currents en Configurar Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#updating-currents).

{% alert important %}
Es importante mantener tu certificado actualizado. Si tu certificado expira, el conector deja de enviar eventos hasta que proporciones un certificado válido, y una interrupción prolongada puede provocar la pérdida de datos.
{% endalert %}

## Comportamiento de la exportación {#export-behavior}

Los usuarios que hayan integrado una solución de almacenamiento de datos en el cloud e intenten exportar API, informes del panel o informes CSV experimentarán lo siguiente:

- Todas las exportaciones de API no devolverán una URL de descarga en el cuerpo de la respuesta y deben recuperarse a través del almacenamiento de datos.
- Todos los informes del panel e informes CSV se enviarán al correo electrónico del usuario para su descarga (no se requieren permisos de almacenamiento) y se respaldarán en el almacenamiento de datos.

{% alert important %}
**Requisito de formato JSON**: Para las exportaciones JSON, Braze utiliza el formato [JSONL](https://jsonlines.org/) (JSON delimitado por saltos de línea), donde cada línea contiene un objeto JSON independiente. Este formato difiere del JSON estándar, que es un único array u objeto JSON. Cada línea del archivo exportado es un objeto JSON válido, pero el archivo en su conjunto no es un único documento JSON válido. Al procesar estos archivos, analiza cada línea individualmente como un objeto JSON independiente en lugar de intentar analizar el archivo completo como un único documento JSON. <br><br> Las exportaciones de Currents utilizan el formato [Apache Avro](https://avro.apache.org/) (archivos `.avro`), no JSON. Este requisito de formato JSON se aplica a las exportaciones de datos del panel y a las exportaciones de API que utilizan formato JSON.
{% endalert %}

## Preguntas frecuentes {#faq}

### ¿Puede Braze proporcionar direcciones IP para incluir en la lista de permitidos del almacenamiento Azure Blob? {#can-braze-provide-ip-addresses-to-allowlist-for-azure-blob-storage}

Braze no publica una lista fija de IP permitidas para Currents ni para las exportaciones del panel al almacenamiento Azure Blob. Braze escribe en tu contenedor utilizando las credenciales y el nombre de contenedor que proporcionas, y Azure controla el acceso a la red a través de la configuración de tu cuenta de almacenamiento (por ejemplo, reglas de firewall en la cuenta de almacenamiento o endpoints privados).

Si tu equipo de seguridad requiere restricciones basadas en IP, utiliza las características de red de Azure en tu cuenta de almacenamiento en lugar de una lista de IP de Braze. Para conocer los pasos de configuración, consulta la [documentación de Microsoft sobre la protección de Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security).