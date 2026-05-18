---
nav_title: BlueConic
article_title: BlueConic
description: "Este artículo de referencia describe la asociación entre Braze y BlueConic, una plataforma líder de datos de clientes, que permite unificar datos en perfiles individuales persistentes y sincronizarlos en los dos sistemas para objetivos de importación a través de un servidor S3 de Amazon Web Services."
alias: /partners/blueconic/
page_type: partner
search_tag: Partner

---

# BlueConic

> [BlueConic](https://www.blueconic.com/), la principal plataforma de datos de clientes, libera los datos propios de las empresas de sistemas dispares y los hace accesibles donde y cuando se necesitan para transformar las relaciones con los clientes e impulsar el crecimiento del negocio.

_Esta integración está mantenida por Blueconic._

## Sobre la integración {#about-the-integration}

La integración de Braze y BlueConic permite a los usuarios unificar datos a través de perfiles individuales persistentes y luego sincronizarlos entre los dos sistemas para objetivos de importación a través de un servidor S3 de Amazon Web Services. Los objetivos potenciales incluyen iniciativas centradas en el crecimiento, orquestación del ciclo de vida del cliente, modelado y análisis, productos y experiencias digitales, monetización basada en la audiencia, y más. Esta integración permite tanto la importación como la exportación programadas por lotes.

{% alert important %}
Al utilizar la integración, BlueConic enviará deltas (datos cambiantes) en cada sincronización. Esto incluye cualquier perfil que haya cambiado desde el último envío y todos los atributos de ese perfil. Controla el uso de puntos de datos en consecuencia.
{% endalert %}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta BlueConic | Se requiere una [cuenta BlueConic](https://www.blueconic.com/) para beneficiarse de esta asociación. Necesitarás acceso para [ver y editar conexiones](https://support.blueconic.com/hc/en-us/articles/202607121-BlueConic-Roles) dentro de tu cuenta BlueConic para acceder a los plugins. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`, `users.export.segment`, `campaigns.list`, `campaigns.details`, `segments.lists` y `segments.details`. <br><br> Se puede crear en el panel de Braze desde **Settings** > **API Keys**. |
| Punto de conexión REST de Braze | La URL de tu punto de conexión REST. Tu punto de conexión dependerá de la [URL de Braze para tu instancia](https://portal.aws.amazon.com/billing/signup#/start). |
| Autenticación S3 | Necesitarás acceso a un servidor de Amazon Web Services (S3) para exportar e importar los datos. |
| ID de la clave de acceso<br>Clave de acceso secreta | El ID de la clave de acceso y la clave de acceso secreta te permitirán autenticar tu servidor S3 para importar y exportar. |
| Contenedor AWS | Tendrás que conectarte a S3 dentro del plugin. Tras la autenticación, los contenedores disponibles aparecerán en un menú desplegable. Aquí se almacenan los archivos que se van a importar o exportar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crear una conexión Braze {#step-1-creating-a-braze-connection}

En BlueConic, selecciona **Connections** en la barra de navegación y, a continuación, **Add Connection**. En la ventana que aparece, busca **Braze** y selecciona **Braze connection**.

Despliega o contrae los campos de metadatos disponibles en la conexión haciendo clic en el icono del chevron gris. En estos campos, puedes marcar esta conexión como favorita, asignarle un nombre, añadir etiquetas, incluir una descripción y optar por recibir notificaciones por correo electrónico si la conexión [se ejecuta o no](https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ).

Guarda tu configuración.

### Paso 2: Configurar una conexión Braze {#step-2-configuring-a-braze-connection}

Para configurar la conexión entre BlueConic y Braze, debes añadir las credenciales de tu cuenta Braze y la información de la cuenta de Amazon Web Services (S3) para autenticar la conexión.

1. En BlueConic, selecciona **Set up and run** en la sección **Setup** del panel izquierdo.<br><br>
2. En la página de autenticación de Braze que se abre, introduce tu punto de conexión de la API REST de Braze y tu clave de API de Braze.<br>
![]({% image_buster /assets/img/blueconic/braze2.png %}){: style="max-width:80%;"}<br><br>
3. En la sección de configuración y autenticación de S3, introduce estas credenciales: ID de la clave de acceso, clave de acceso secreta y contenedor de S3 de Amazon Web Services (S3). Deben ser las [mismas credenciales]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) que configuraste al establecer la integración de Braze y Amazon S3. Guarda tu configuración. <br>![]({% image_buster /assets/img/blueconic/braze3.png %}){: style="max-width:80%;"}

### Paso 3: Crear objetivos de importación o exportación (mapeado de importaciones) {#step-3-creating-import-or-export-goals-import-mapping}

Una vez completada la autenticación, debes crear al menos un objetivo de importación o exportación, activar la conexión y programar o ejecutar la conexión.

{% tabs %}
{% tab Import %}

1. Selecciona **Import data into BlueConic** en el panel izquierdo para abrir la página de configuración de datos de Braze.<br><br>
2. Selecciona la ubicación de los datos en Braze. Aquí puedes indicar a BlueConic dónde encontrar los datos a importar seleccionando tu audiencia de Braze.<br>![La audiencia de BlueConic Braze configurada como "BlueConic Test Users".]({% image_buster /assets/img/blueconic/braze4.png %}){: style="max-width:80%;"}<br><br>
3. A continuación, mapea los identificadores entre Braze y BlueConic. <br>![El campo "External ID" de Braze configurado para mapearse con el campo "Braze external ID" de BlueConic.]({% image_buster /assets/img/blueconic/braze5.png %}){: style="max-width:80%;"}<br><br> Para vincular los datos del cliente entre los dos sistemas, introduce uno o varios identificadores de cliente.<br>Utiliza la casilla **Allow creation...** para permitir que BlueConic cree nuevos perfiles para datos que no coincidan con un perfil BlueConic existente.<br><br>
4. A continuación, haz coincidir los campos de datos de BlueConic que vas a exportar con los campos de Braze. Utiliza los campos desplegables para seleccionar el identificador de perfil de BlueConic o una propiedad de perfil a la izquierda y selecciona el identificador de perfil de Braze correspondiente. A continuación, utiliza el menú desplegable para especificar cómo debe añadirse el contenido importado a los valores existentes: añadido, sumado, establecido solo si la propiedad del perfil está vacía o establecido para borrar (si el campo de Braze está vacío).<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>Utiliza el botón **Add Mapping** para crear filas de mapeado adicionales según sea necesario. Puedes añadir varias filas de mapeado con la opción **Add remaining fields**. BlueConic detecta los campos de Braze restantes y los empareja con las propiedades del perfil de BlueConic. Puedes establecer la estrategia de fusión para las importaciones (set, add, sum, set if empty o clear) y proporcionar un prefijo personalizado a los nombres de las propiedades del perfil de BlueConic.<br><br>
5. Por último, selecciona **Run the connection** para iniciar la conexión. Visita [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections) para obtener más información sobre la programación y ejecución de conexiones.
{% endtab %}
{% tab Export %}

1. Selecciona **Export data to Braze** en el panel izquierdo para configurar tu exportación de datos de BlueConic a Braze.<br><br>
2. Elige un segmento de BlueConic para la exportación. Solo se exportarán los perfiles de este segmento con identificadores coincidentes en Braze.<br>![Un segmento de BlueConic de 20.000 perfiles.]({% image_buster /assets/img/blueconic/braze8.png %}){: style="max-width:80%;"}<br><br>
3. A continuación, vincula los identificadores entre los perfiles de BlueConic y los campos de Braze. Opcionalmente, puedes dejar que BlueConic cree nuevos registros si no encuentra ninguna coincidencia.<br>![El campo "External ID" de Braze configurado para mapearse con el campo "Braze external ID" de BlueConic.]({% image_buster /assets/img/blueconic/braze7.png %}){: style="max-width:80%;"}<br><br>
4. A continuación, haz coincidir los campos de datos de BlueConic que vas a exportar con los campos de Braze. Utiliza el menú desplegable del icono de BlueConic para elegir el tipo de [información](https://support.blueconic.com/hc/en-us/articles/4405501836955-Braze-Connection#creating-export-goals) que deseas exportar. La información disponible incluye las propiedades del perfil, los identificadores de perfil de BlueConic, los segmentos asociados, todas las interacciones vistas, los niveles de permiso y un valor de texto estático.<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>
5. Por último, haz clic en **Run the connection** para iniciar la conexión. Visita [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections) para obtener más información sobre la programación y ejecución de conexiones.
{% endtab %}
{% endtabs %}

## Paso 4: Activar o desactivar la conexión {#step-4-toggle-connection-on}

Utiliza el conmutador situado junto al título de la conexión Braze para activar o desactivar la conexión. Una conexión debe estar activada para funcionar durante las horas programadas.