---
nav_title: Redpoint
article_title: Redpoint
description: "La integración de Redpoint con Braze te permite incorporar y enriquecer los perfiles de usuario de Braze con tus datos propios."
alias: /partners/redpoint/
page_type: partner
search_tag: Redpoint
---

# Redpoint

> [Redpoint](https://www.redpointglobal.com) es una plataforma tecnológica que ofrece a los especialistas en marketing una plataforma de orquestación de campañas totalmente integrada. Aprovecha las funciones de segmentación, programación y automatización de Redpoint para controlar cómo y cuándo se importan los datos CDP a Braze.

_Esta integración está mantenida por Redpoint._

## Sobre la integración {#about-the-integration}

La integración de Braze y Redpoint te permite crear Segments de Braze basados en tus datos CDP de Redpoint. Redpoint proporciona dos modos para pasar datos a Braze:

1. Modo **Braze Onboarding and Upsert**: Realiza un "upsert" de un perfil de usuario de Redpoint en Braze. Está pensado para incorporar o actualizar registros de usuarios cuando los datos han cambiado.
2. Modo **Braze Append**: Actualiza el perfil de un usuario si ese usuario ya existe en Braze.

Configurarás una plantilla de exportación y un canal de salida para cada modo.

{% alert note %}
"Upsert" es una combinación de las palabras "update" (actualizar) e "insert" (insertar). Se utiliza cuando quieres insertar un nuevo registro en una tabla de la base de datos si aún no existe, o actualizar el registro si ya existe. Básicamente, upsert comprueba si un registro concreto está presente en la base de datos. Si el registro está presente, se actualiza, y si no lo está, se inserta un nuevo registro.
{% endalert %}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br>Se puede crear en el dashboard de Braze desde **Settings** > **API Keys**. |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto de conexión dependerá de la URL de Braze de tu instancia. |
| Artefactos de Redpoint Data Management | La integración de Braze se apoya en un conjunto de artefactos de Redpoint Data Management. Ponte en contacto con el [soporte de Redpoint](https://support.redpointglobal.com/hc/en-us/restricted?return_to=https%3A%2F%2Fsupport.redpointglobal.com%2Fhc%2Fen-us) para solicitar los artefactos correspondientes a tu versión de Redpoint Data Management. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Atributos personalizados de Redpoint CDP {#redpoint-cdp-custom-attributes}

Los siguientes atributos personalizados de Redpoint pueden añadirse a un perfil de usuario de Braze.

| Campo               | Descripción                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `rpi_cdp_attributes` | El objeto de atributo de perfil CDP de Redpoint                                                                                  |
| `rpi_audience_outputs`| Conjunto de etiquetas de salida de audiencia en las que el usuario es objetivo en una ejecución del canal Redpoint Outbound Delivery Braze         |
| `rpi_offers`         | Conjunto de etiquetas de oferta en las que el usuario es objetivo en una ejecución del canal Redpoint Outbound Delivery Braze                   |
| `rpi_contact_ids`    | Conjunto de ID de contacto del historial de ofertas en los que el usuario es objetivo en una ejecución del canal Redpoint Outbound Delivery Braze     |
| `rpi_channel_exec_ids`| Conjunto de ID de ejecución de canal en los que el usuario es objetivo en una ejecución del canal Redpoint Outbound Delivery Braze       |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos personalizados de Redpoint CDP" }

![]({% image_buster /assets/img/redpoint/rpi_to_braze_custom_attributes.png %}){: style="max-width:75%;"}

## Integración {#integration}

### Paso 1: Configurar plantillas {#step-1-set-up-templates}

#### Paso 1a: Crear la plantilla Braze Onboarding and Upsert {#step-1a-create-the-braze-onboarding-and-upsert-template}

En Redpoint Interaction (RPI), crea una nueva plantilla de exportación y nómbrala **Braze Onboarding and Upsert**. Esta plantilla define los mapeados principales entre el CDP de Redpoint y el perfil de usuario de Braze, junto con cualquier atributo personalizado adicional que quieras añadir a tus perfiles de usuario en Braze.

Arrastra los atributos de Redpoint CDP a la columna **Attribute**. Establece cada **Header Row Value** en el [atributo de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) de Braze correspondiente.

La siguiente tabla enumera los atributos CDP de Redpoint y sus correspondientes atributos de Braze:

| Atributo Redpoint | Valor de la fila de cabecera |
|--------------------|------------------|
| PID                | `external_id`    |
| First Name          | `first_name`     |
| Last Name          | `last_name`      |
| Primary Email      | `email`          |
| Primary Country    | `country`        |
| DOB                | `dob`            |
| Gender             | `gender`         |
| Primary City       | `home_city`      |
| Primary Phone      | `phone`          |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 1a: Crear la plantilla Braze Onboarding and Upsert" }

Añade el atributo **Output Name** de la tabla **Offer History**. Por último, añade cualquier atributo personalizado adicional de Redpoint que quieras fusionar en Braze. Por ejemplo, la siguiente es una plantilla de incorporación y upsert con educación, ingresos y estado civil como atributos adicionales.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_upsert_export_format.png %}){: style="max-width:75%;"}

#### Paso 1b: Crear la plantilla Braze Append {#step-1b-create-the-braze-append-template}

Crea una segunda plantilla de exportación para operaciones de solo adición llamada **Braze Append**.

Solo establecerás dos atributos para esta plantilla. Para **PID**, establece el **Header Row Value** como `external_id`. Para **Output Name**, establece la **Header Row** como `output_name`.

![Una plantilla de exportación de ejemplo con los atributos `external_id` y nombre de salida.]({% image_buster /assets/img/redpoint/rpi_to_braze_append_export_format.png %}){: style="max-width:75%;"}

#### Paso 1c: Establecer formato de fecha {#step-1c-set-date-format}

Para ambas plantillas de exportación, ve a la pestaña **Options** y establece el **Date Format** en el valor **Custom Format**. Establece el formato como **yyyy-MM-dd**.

![La pestaña de opciones muestra el formato de fecha establecido en yyyy-MM-dd.]({% image_buster /assets/img/redpoint/rpi_to_braze_export_format_config.png %}){: style="max-width:75%;"}

### Paso 2: Crear canales de salida {#step-2-create-outbound-channels}

En RPI, crea dos nuevos canales. Establece ambos canales en **Outbound Delivery**. Nombra un canal **Braze Onboarding and Upsert** y el otro **Braze Append**.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_general.png %}){: style="max-width:75%;"}

{% alert note %}
Tras la incorporación inicial de tus registros de CDP a Braze, comprueba si los flujos de trabajo posteriores de Redpoint Interaction que utilizan el canal Braze Onboarding and Upsert están diseñados para seleccionar únicamente los registros que han cambiado desde la sincronización inicial de incorporación.
{% endalert %}

### Paso 3: Configurar los canales {#step-3-configure-the-channels}

#### Paso 3a: Establecer plantilla y formato de ruta de exportación {#step-3a-set-template-and-export-path-format}

Ve a la pestaña **General** en la pantalla de **Configuration** de canales. Establece la plantilla de exportación para cada canal respectivo.

A continuación, define un **Export path format** en ambos canales que apunte a una red compartida, un protocolo de transferencia de archivos o una ubicación de proveedor de contenidos externo que sea accesible tanto para Redpoint Interaction como para Redpoint Data Management.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_specific.png %}){: style="max-width:75%;"}

El formato del directorio de exportación en ambos canales será idéntico y deberá terminar en `\\[Channel]\\[Offer]\\[Workflow ID]`.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_export_directory_setup.png %}){: style="max-width:50%;"}

#### Paso 3b: Configurar la post ejecución {#step-3b-configure-post-execution}

Ve a la pestaña **Post Execution** en la pantalla de **Configuration** de canales.

Marca la casilla de verificación **Post-execution** para llamar a una URL de servicio después de la ejecución del canal. Introduce la URL de tu servicio web de Redpoint Data Management. Esta entrada será idéntica tanto en tu canal de Onboarding como en el de Append.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_post_execution.png %}){: style="max-width:75%;"}

### Paso 4: Configurar los componentes de Braze en Redpoint Data Management {#step-4-set-up-braze-components-in-redpoint-data-management}

El archivo que contiene los artefactos de Redpoint Data Management (RPDM) para soportar la integración de Braze incluye un README con instrucciones detalladas para configurar los componentes necesarios. Ten en cuenta los siguientes detalles al configurar tu integración.

#### Paso 4a: Actualizar la automatización RPI a Braze con tu punto de conexión REST de Braze y el directorio de salida RPI base {#step-4a-update-the-rpi-to-braze-automation-with-your-braze-rest-endpoint-and-base-rpi-output-directory}

Tras importar los artefactos relacionados con Braze en Redpoint Data Management, abre la automatización denominada **AUTO_Process_RPI_to_Braze** y actualiza las dos variables de automatización siguientes con los valores de tu entorno:

* **BRAZE_API_URL**: El punto de conexión REST de Braze
* **BASE_OUTPUT_DIRECTORY**: El directorio de salida compartido entre Redpoint Interaction y Redpoint Data Management

![]({% image_buster /assets/img/redpoint/rpi_to_braze_auto_variables.png %}){: style="max-width:40%;"}

#### Paso 4b: Actualizar el proyecto de adición de RPI a Braze {#step-4b-update-the-rpi-to-braze-append-project}

El proyecto de Redpoint Data Management llamado **PROJ_RPI_to_Braze_Append** contiene el esquema del archivo de exportación de entrega saliente y los mapeados del objeto de atributo personalizado `rpi_cdp_attributes` en Braze.

Actualiza el esquema de entrada de archivos y la herramienta de inyección de documentos denominada **RPI to Braze Document Injector** con cualquier atributo CDP personalizado adicional definido en tu plantilla de archivo de exportación. Este ejemplo muestra el mapeado adicional de educación, ingresos y estado civil:

![]({% image_buster /assets/img/redpoint/rpi_to_braze_doc_injector_mappings.png %}){: style="max-width:40%;"}

## Uso de la integración {#using-the-integration}

El canal Braze de Outbound Delivery puede aprovecharse ahora dentro de los flujos de trabajo de Redpoint Interaction. Sigue las prácticas estándar para crear reglas de selección y audiencias en RPI, así como para crear programas de flujo de trabajo y desencadenantes asociados.

Para habilitar la sincronización de una salida de audiencia de RPI con Braze, crea una oferta de entrega saliente y asóciala al canal **Braze Onboarding and Upsert** o **Braze Append**. Esto depende de si la intención es crear o fusionar nuevos registros en Braze, o solo añadir datos de Campaign si el registro ya existe en Braze.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_rpi_canvas.png %}){: style="max-width:80%;"}

Una vez que el flujo de trabajo se ha ejecutado correctamente en RPI, los datos de orquestación y CDP procedentes de RPI pueden utilizarse ahora para crear Segments en Braze.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_build_braze_segment.png %}){: style="max-width:80%;"}

Puedes ver las propiedades asociadas a Redpoint en el perfil del usuario.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_record_example.png %}){: style="max-width:80%;"}