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

La integración de Braze y Microsoft Azure Blob Storage te permite exportar datos a Azure y transmitir datos a Currents. Más tarde, puedes utilizar un proceso ETL (extraer, transformar, cargar) para transferir tus datos a otras ubicaciones.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de almacenamiento de Microsoft Azure y Azure | Se necesita una cuenta de Microsoft Azure y de almacenamiento Azure para aprovechar esta asociación. |
| Currents | Para exportar datos a Currents, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) para tu cuenta. Currents no es necesario si solo estás configurando el archivado de mensajes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Para integrarte con Microsoft Azure Blob Storage, debes tener una cuenta de almacenamiento y una cadena de conexión que permita a Braze exportar datos a Azure o transmitir datos a Currents.

### Paso 1: Crear una cuenta de almacenamiento {#step-1-create-a-storage-account}

En Microsoft Azure, ve a **Storage Accounts** en la barra lateral y haz clic en **+ Add** para crear una nueva cuenta de almacenamiento. A continuación, proporciona un nombre de cuenta de almacenamiento. No será necesario actualizar otras configuraciones predeterminadas. Por último, selecciona **Review + create**.

Aunque ya tengas una cuenta de almacenamiento, te recomendamos que crees una nueva específicamente para tus datos de Braze.

![]({% image_buster /assets/img/azure-currents-step-1.png %})

### Paso 2: Obtener la cadena de conexión {#step-2-get-the-connection-string}

Una vez desplegada la cuenta de almacenamiento, ve al menú **Access Keys** desde la cuenta de almacenamiento y toma nota de la cadena de conexión.

Microsoft proporciona dos claves de acceso para mantener las conexiones utilizando una clave mientras se regenera la otra. Solo necesitas la cadena de conexión de una de ellas.

{% alert note %}
Braze utiliza la cadena de conexión de este menú, no la clave.
{% endalert %}

![]({% image_buster /assets/img/azure-currents-step-2.png %})

### Paso 3: Crear un contenedor de servicio blob {#step-3-create-a-blob-service-container}

Navega hasta el menú **Blobs** en la sección **Blob Service** de tu cuenta de almacenamiento. Crea un contenedor de servicio blob dentro de la cuenta de almacenamiento que creaste anteriormente.

Proporciona un nombre para tu contenedor de servicio blob. No será necesario actualizar otras configuraciones predeterminadas.

![]({% image_buster /assets/img/azure-currents-step-3.png %})

### Paso 4: Configurar Currents {#step-4-set-up-currents}

En Braze, ve a **Currents > + Create Current > Azure Blob Data Export** e indica el nombre de tu integración y tu correo electrónico de contacto.

A continuación, proporciona tu cadena de conexión, el nombre del contenedor y el prefijo BlobStorage (opcional).

![La página de Microsoft Azure Blob Storage de Currents en Braze. En esta página existen campos para el nombre de la integración, el correo electrónico de contacto, la cadena de conexión, el nombre del contenedor y el prefijo.]({% image_buster /assets/img/maz.png %})

Por último, desplázate hasta la parte inferior de la página y selecciona los eventos de interacción con mensajes o los eventos de comportamiento del cliente que deseas exportar. Cuando hayas terminado, lanza tu Current.

### Paso 5: Configurar la exportación de datos a Azure {#step-5-set-up-azure-data-export}

A continuación se configuran las credenciales que se utilizan para:
1. Exportaciones de Segment a través de la API
2. Exportaciones de CSV (Campaign, Segment, exportación de datos de usuario de Canvas a través del dashboard)
3. Informes de interacción

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** > **Microsoft Azure** y proporciona tu cadena de conexión, el nombre del contenedor de almacenamiento Azure y el prefijo de almacenamiento Azure.

A continuación, asegúrate de que está marcada la casilla **Make this the default data export destination**, así te asegurarás de que los datos exportados se envían a Azure. Cuando hayas terminado, guarda tu integración.

![La página de exportación de datos de Microsoft Azure en Braze. En esta página existen campos para la cadena de conexión, el nombre del contenedor y el prefijo.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
Es importante que mantengas actualizada tu cadena de conexión; si las credenciales de tu conector caducan, este dejará de enviar eventos. Si esto persiste durante más de **48 horas**, los eventos del conector se eliminarán y los datos se perderán permanentemente.
{% endalert %}

## Comportamiento de la exportación {#export-behavior}

Los usuarios que hayan integrado una solución de almacenamiento de datos en la nube e intenten exportar API, informes del dashboard o informes CSV experimentarán lo siguiente:

- Todas las exportaciones de la API no devolverán una URL de descarga en el cuerpo de la respuesta y deberán recuperarse a través del almacenamiento de datos.
- Todos los informes del dashboard y los informes CSV se enviarán al correo electrónico del usuario para su descarga (sin necesidad de permisos de almacenamiento) y se realizará una copia de seguridad en el almacenamiento de datos.

{% alert important %}
**Requisito de formato JSON**: Para las exportaciones JSON, Braze utiliza el formato JSONL (JSON delimitado por nuevas líneas), en el que cada línea contiene un objeto JSON independiente. Este formato difiere del JSON estándar, que es una única matriz u objeto JSON. Cada línea del archivo exportado es un objeto JSON válido, pero el archivo en su conjunto no es un único documento JSON válido. Al procesar estos archivos, analiza cada línea individualmente como un objeto JSON distinto, en lugar de intentar analizar todo el archivo como un único documento JSON.

Las exportaciones de Currents utilizan el formato Apache Avro (archivos `.avro`), no JSON. Este requisito de formato JSON se aplica a las exportaciones de datos del dashboard y a las exportaciones de API que utilizan el formato JSON.
{% endalert %}

## Preguntas frecuentes {#faq}

### ¿Puede Braze proporcionar direcciones IP para incluir en la lista de permitidos de Azure Blob Storage? {#can-braze-provide-ip-addresses-to-allowlist-for-azure-blob-storage}

Braze no publica una lista fija de IP permitidas para Currents ni para las exportaciones del dashboard a Azure Blob Storage. Braze escribe en tu contenedor utilizando la cadena de conexión y el nombre del contenedor que proporcionas, y Azure controla el acceso a la red a través de la configuración de tu cuenta de almacenamiento (por ejemplo, reglas de firewall en la cuenta de almacenamiento o puntos de conexión privados).

Si tu equipo de seguridad requiere restricciones basadas en IP, utiliza las características de red de Azure en tu cuenta de almacenamiento en lugar de una lista de IP de Braze. Para conocer los pasos de configuración, consulta la [documentación de Microsoft sobre la protección de Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security).