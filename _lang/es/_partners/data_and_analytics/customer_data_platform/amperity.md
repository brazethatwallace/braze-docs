---
nav_title: Amperity
article_title: Amperity
alias: /partners/amperity/
description: "Este artículo de referencia describe la asociación entre Braze y Amperity, una plataforma integral de datos de clientes empresariales, que te permite sincronizar usuarios de Amperity, unificar datos, enviar datos mediante contenedores de AWS S3 a Braze y mucho más."
page_type: partner
search_tag: Partner

---

# Amperity

> [Amperity](https://amperity.com/) es una plataforma integral de datos de clientes empresariales que ayuda a las marcas a conocer a sus clientes, tomar decisiones estratégicas y adoptar sistemáticamente las medidas adecuadas para servir mejor a sus consumidores. Amperity proporciona funciones inteligentes de unificación de la gestión de datos, análisis, información y activación.

_Esta integración está mantenida por Amperity._

{% multi_lang_include video.html id="06G0lxaSjgk" align="right" %}

La integración de Braze y Amperity ofrece una visión unificada de tus clientes en las dos plataformas. Esta integración te permite:
- **Sincronizar perfiles de clientes**: Mapea datos de usuario y atributos personalizados de Amperity a Braze.
- **Crear y enviar audiencias**: Crea segmentos que devuelvan listas de clientes activos y sus atributos personalizados asociados a Braze, y envíalos a Braze.
- **Gestionar actualizaciones de datos**: Controla la frecuencia de envío de actualizaciones de atributos personalizados a Braze.
- **Unificar datos**: Unifica datos en varias plataformas compatibles con Amperity y Braze.
- **Sincronizar datos de Braze con Amazon S3**: Utiliza Braze Currents para integrar los datos de interacción de las Campaigns de Braze, lo que te permite sincronizar datos con Amazon S3 en formato Apache Avro.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Amperity | Se necesita una [cuenta de Amperity](https://amperity.com/request-a-demo) para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br> Puede crearse en el panel de Braze navegando a **Consola para desarrolladores** > **Clave de API REST** > **Crear nueva clave de API**. |
| Instancia de Braze | Tu instancia de Braze puede obtenerse a través de tu administrador de incorporación a Braze o en la [página de resumen de la API]({{site.baseurl}}/api/basics/#endpoints). |
| Punto de conexión REST de Braze | La URL de tu punto de conexión de Braze. Tu punto de conexión dependerá de tu instancia de Braze. |
| Conector de Currents (opcional) | El conector S3 de Currents. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Mapeado de datos {#data-mapping}

Tanto los atributos estándar como los personalizados pueden enviarse de Amperity a Braze, lo que te permite enriquecer los perfiles de los clientes en Braze con datos de diversas fuentes a través de Amperity. Los atributos específicos que puedes enviar dependerán de los datos de tu sistema Amperity y de los atributos que hayas configurado en Braze.

Lee a continuación para conocer estos atributos.

### Atributos estándar {#standard-attributes}

[Los atributos del perfil]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) describen quiénes son tus clientes. A menudo se asocian a la identidad del cliente, como:
- Nombres
- Fechas de nacimiento
- Direcciones de correo electrónico
- Números de teléfono

### Atributos personalizados {#custom-attributes}

[Los atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) en Braze son campos determinados por tu marca. Si deseas que Amperity gestione atributos personalizados que ya existen en Braze, alinea la salida que se envía desde Amperity con los nombres que ya están en tu espacio de trabajo de Braze. Esto puede incluir lo siguiente:
- Historiales de compras
- Estado de fidelización
- Niveles de valor
- Datos recientes de interacción

Verifica los nombres de los atributos personalizados que se enviarán a Braze desde Amperity. Amperity añadirá un atributo personalizado siempre que no haya un nombre coincidente.

Los atributos personalizados solo se actualizarán para aquellos usuarios que tengan un `external_id` o `braze_id` coincidente en Braze.

### Audiencias de Amperity {#amperity-audiences}

Las audiencias sincronizadas desde Amperity a Braze se registrarán en los perfiles de usuario como atributos personalizados. Estos pueden utilizarse para dirigirse a esos usuarios en Braze.

![Lista desplegable de filtros con atributos personalizados que se muestran en la categoría de datos personalizados.]({% image_buster /assets/img/amperity/custom_attributes_filters.png %}){: style="max-width:60%;"}

![Lista desplegable de atributos personalizados como "l12m_frequency" y "l12m_monetary".]({% image_buster /assets/img/amperity/search_custom_attributes_filters.png %}){: style="max-width:40%;"}

### Tipos de datos {#data-types}

Los tipos de datos admitidos son:
- Booleano
- Fecha
- Fecha y hora
- Decimal
- Flotante
- Entero
- Cadena
- Varchar

El tipo de datos utilizado depende de la naturaleza del atributo. Por ejemplo, una dirección de correo electrónico sería una cadena, mientras que la edad de un cliente podría ser un entero.

### Duplicación de atributos {#duplication-of-attributes}

Evita enviar atributos personalizados que dupliquen campos predeterminados del perfil de usuario. Por ejemplo, las fechas de nacimiento deben enviarse a Braze como un campo de perfil de usuario llamado "dob" para que coincida con el atributo estándar de Braze. Si se envían como "birthday", "Birthdate" o cualquier otra cadena, se creará un atributo personalizado y los valores del campo "dob" no se actualizarán.

### Puntos de datos {#data-points}

Amperity realiza un seguimiento de los cambios entre las sincronizaciones con Braze y el estado de los envíos en general. Amperity solo enviará a Braze los miembros de la lista y otros atributos elegidos que hayan cambiado desde la última sincronización.

## Integración {#integration}

### Paso 1: Capturar detalles de configuración para Braze {#step-1-capture-configuration-details-for-braze}

1. Crea una clave de API REST de Braze para tu espacio de trabajo de Braze con los permisos `users.track` en **Datos de usuario**. El punto de conexión `users.track` sincroniza la audiencia de Amperity con Braze como un atributo personalizado.
2. Determina el [punto de conexión de la REST API]({{site.baseurl}}/api/basics/#endpoints) para tu instancia de Braze. Por ejemplo, si tu URL de Braze es `https://dashboard-03.braze.com`, tu punto de conexión de la REST API es `https://rest.iad-03.braze.com` y tu instancia es "US-03".
3. Determina una lista de [campos de perfil de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) y [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) que pueden enviarse a Braze desde Amperity.

### Paso 2: Configurar Braze como destino — Operator DataGrid {#step-2-set-up-braze-as-a-destinationdatagrid-operator}

#### Paso 2a: Construir la tabla de perfiles de clientes {#step-2a-build-the-customer-profiles-table}

Crea una nueva tabla llamada "Braze Customer Attributes" dentro de tu base de datos Customer 360 en Amperity. Esta tabla debe contener todos los atributos de Braze que tu marca desea gestionar desde Amperity, incluidos tanto los campos de perfil de usuario predeterminados requeridos por Braze como cualquier atributo personalizado. Utiliza SQL para definir la estructura de esta tabla como se muestra en [la documentación de Amperity](https://docs.amperity.com/datagrid/destination_braze.html#customer-profiles-table).

#### Paso 2b: Nombrar, validar y guardar la tabla {#step-2b-name-validate-and-save-the-table}

Nombra la tabla "Braze Customer Attributes" y guárdala. Verifica que la tabla sea accesible para el **Segment Editor** y el editor **Edit Attributes** dentro de las campañas.

#### Paso 2c: Añadir Braze como destino {#step-2c-add-braze-as-a-destination}

En la plataforma Amperity, ve a la pestaña **Destinations**. Busca la opción de añadir un nuevo destino. Entre las opciones disponibles, selecciona **Braze**.

![La sección Nuevo destino con el nombre "Braze API", la descripción "Send audience attributes to Braze." y el plugin "Braze".]({% image_buster /assets/img/amperity/destination_name.png %}){: style="max-width:60%;"}

#### Paso 2d: Configurar los detalles del destino {#step-2d-configure-destination-details}

En **Braze settings**, proporciona las credenciales de Braze y la configuración de destino, como se muestra en [la documentación de Amperity](https://docs.amperity.com/datagrid/destination_braze.html#add-destination). Introduce los datos de configuración recogidos en el paso anterior y define el identificador de Braze. Los identificadores disponibles para la coincidencia son:
- `braze_id`: Un identificador de Braze asignado automáticamente, inalterable y asociado a un usuario concreto cuando se crea en Braze.
- `external_id`: Un identificador asignado por el cliente, normalmente un UUID.

![La sección Braze Settings con una instancia de "US-03", identificador de usuario de "external_id", nombre de segmento en blanco, contenedor de S3 de "amperity-training-abc123" y carpeta de S3 de "braze-attributes".]({% image_buster /assets/img/amperity/braze_settings.png %}){: style="max-width:60%;"}

#### Paso 2e: Añadir una plantilla de datos {#step-2e-add-a-data-template}

En la pestaña **Destinations**, abre el menú del destino Braze y selecciona **Add data template**. Introduce un nombre y una descripción para la plantilla (por ejemplo, "Braze" y "Send custom attributes to Braze"), verifica el acceso de los usuarios empresariales y comprueba todos los ajustes de configuración.

Si alguna configuración necesaria no se configuró como parte del destino, configúrala como parte de la plantilla de datos. Guarda la plantilla de datos.

![La sección Data Template Name con el nombre "Braze Audience Attributes" y la descripción "Send audience attributes to Braze."]({% image_buster /assets/img/amperity/data_template_name.png %}){: style="max-width:60%;"}

#### Paso 2f: Guardar la configuración {#step-2f-save-the-configuration}

Después de completar los datos necesarios, guarda la configuración. Ahora que Braze está configurado como destino, los usuarios de Amp360 y AmpIQ pueden sincronizar datos con Braze.

### Paso 3: Sincronizar datos con Braze {#step-3-sync-data-to-braze}

Asegúrate de que Braze esté habilitado para tu tenant de Amperity. Si no es así, ponte en contacto con tu Operator de DataGrid o con un representante de Amperity para obtener ayuda.

A continuación, sigue las instrucciones de sincronización de Amp360 o AmpIQ según corresponda a tu empresa.

#### Opción de sincronización 1: Enviar resultados de consulta a Braze a través de Amp360 {#syncing-option-1-send-query-results-to-braze-via-amp360}

Los usuarios de Amp360 pueden utilizar SQL para escribir consultas de forma libre y, a continuación, configurar una programación que envíe los resultados a Braze.

##### Paso 1: Crear una consulta en Amperity {#step-1-create-a-query-in-amperity}

Ve a la función de consulta de Amperity y crea una consulta SQL que genere el conjunto de datos de clientes deseado. Los resultados deben incluir los atributos específicos que deseas enviar a Braze. Consulta este ejemplo de consulta de Amperity para obtener una lista de usuarios con sus historiales de compra.

##### Paso 2: Añadir una nueva orquestación en Amperity {#step-2-add-a-new-orchestration-in-amperity}

1. Ve a la sección **Orchestration** y haz clic en la opción para añadir una nueva orquestación.
2. Especifica qué debe hacer la orquestación. Esto suele implicar especificar la consulta SQL que debe ejecutarse y dónde deben enviarse los resultados. En este caso, selecciona la consulta SQL que creaste para generar la lista de clientes activos y especifica Braze como destino de los resultados.
3. Define cuándo y con qué frecuencia debe ejecutarse la orquestación. Por ejemplo, puedes ejecutar la orquestación diariamente a una hora determinada.
4. Guarda la orquestación después de configurarla a tu gusto. Se añadirá a tu lista de orquestaciones en Amperity.
5. Prueba la orquestación para asegurarte de que funciona como se espera. Puedes hacerlo activando manualmente la orquestación y comprobando los resultados en Braze.

##### Paso 3: Ejecutar la orquestación {#step-3-run-the-orchestration}

Ejecuta la orquestación para ejecutar la consulta y enviar los resultados a Braze. Esto puede hacerse manualmente o según la programación que hayas establecido en los ajustes de orquestación.

#### Opción de sincronización 2: Enviar audiencias a Braze mediante AmpIQ {#syncing-option-2-send-audiences-to-braze-via-ampiq}

Los usuarios de AmpIQ pueden crear segmentos en Amperity a través de una interfaz no SQL y sincronizarlos con destinos posteriores como Braze. Los usuarios pueden seleccionar destinos y, a continuación, configurar una lista de atributos que se enviarán a cada destino.

##### Paso 1: Crear un segmento en Amperity {#step-1-create-a-segment-in-amperity}

Crea un segmento en Amperity que devuelva una lista de clientes. Este segmento debe estar asociado a los atributos personalizados que deseas actualizar en Braze.

{% alert note %}
Consulta la documentación de Amperity para ver ejemplos de los distintos tipos de segmentos que puedes enviar a Braze.
{% endalert %}

##### Paso 2: Crear una campaña en Amperity {#step-2-build-a-campaign-in-amperity}

1. Ve a la sección **Campaign** y haz clic en la opción para crear una nueva campaña.
2. Dale a tu campaña un nombre descriptivo y único que te ayude a identificarla más adelante, sobre todo si tienes varias campañas.
3. Selecciona el segmento de clientes al que deseas dirigirte con esta campaña. Este debería ser el segmento que creaste anteriormente. <br>![El campo desplegable de los segmentos a excluir de la segmentación.]({% image_buster /assets/img/amperity/select_segments.png %}){: style="max-width:50%;"}<br><br>
4. Elige los datos que deseas enviar como parte de la campaña. Esto puede incluir una serie de atributos del cliente. ![El modal Editar atributos de la campaña permite seleccionar un destino y atributos del cliente.]({% image_buster /assets/img/amperity/edit_campaign_attributes.png %}){: style="max-width:90%;"}<br><br>
5. Selecciona **Braze** como destino al que se enviarán los datos de la campaña.
6. Elige cuándo y con qué frecuencia deseas que se ejecute la campaña. Puede ser un evento puntual o una programación recurrente.
7. Guarda tu campaña y ejecuta una prueba para asegurarte de que funciona como se espera.

##### Paso 3: Ejecutar la campaña {#step-3-run-the-campaign}

Ejecuta la campaña para enviar el segmento a Braze. Esto puede hacerse manualmente o según la programación que hayas establecido en la configuración de la campaña.


### Uso de Amperity con Braze Currents {#using-amperity-with-braze-currents}
Para enviar los datos de Braze Currents a Amperity:
1. [Configura un Braze Current]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/) para enviar datos a un contenedor de Amazon S3.
2. Configura Amperity para [leer archivos Apache Avro de ese contenedor de Amazon S3](https://docs.amperity.com/datagrid/source_amazon_s3.html).
3. Configura las fuentes y automatiza las cargas de datos mediante flujos de trabajo estándar.