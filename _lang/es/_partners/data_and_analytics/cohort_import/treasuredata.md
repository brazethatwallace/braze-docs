---
nav_title: Treasure Data
article_title: Importación de cohortes de Treasure Data
description: "Este artículo de referencia describe la funcionalidad de importación de cohortes de Treasure Data."
alias: /partners/treasure_data_cohort_import/
page_type: partner
search_tag: Partner

---
# Importación de cohortes de Treasure Data {#treasure-data-cohort-import}

> Este artículo describe cómo importar cohortes de usuarios de Treasure Data a Braze para que puedas enviar campañas segmentadas basadas en datos que solo pueden existir en tu almacén de datos.

{% alert important %}
Esta función está actualmente en fase beta. Para más información, ponte en contacto con tus representantes de Treasure Data y Braze.
{% endalert %}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Treasure Data | Se necesita una cuenta de [Treasure Data](https://www.treasuredata.com/) para aprovechar esta integración. |
| Clave de importación de datos de Braze | Se puede obtener en el panel de Braze desde **Integraciones de socios** > **Socios tecnológicos** y luego seleccionando **Treasure Data**. |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto de conexión dependerá de la URL de Braze de tu instancia. |
| Dirección IP estática de Treasure Data | La dirección IP estática de Treasure Data es el punto de acceso y la fuente del enlace para esta integración. Para determinar la dirección IP estática, ponte en contacto con tu representante de éxito del cliente de Treasure Data o con el soporte técnico de Treasure Data. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integración de la importación de datos {#data-import-integration}

### Paso 1: Obtén tu clave de importación de datos de Braze {#step-1-get-your-braze-data-import-key}

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Treasure Data**. Aquí encontrarás tu punto de conexión REST y podrás generar tu clave de importación de datos de Braze. Una vez generada la clave, puedes crear una nueva o invalidar una existente.

### Paso 2: Crea una conexión de datos {#step-2-create-a-data-connection}

Antes de crear tu conexión de datos en Treasure Data, tendrás que autenticarte. Primero, selecciona **Integrations Hub** y, a continuación, **Catalog**.

![Catálogo del centro de integraciones de Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort1.png %})

Busca la integración de Braze en el **Catalog**, pasa el cursor sobre el icono y selecciona **Create Authentication**. Introduce tus credenciales, asigna un nombre a la autenticación y selecciona **Done**.

![Catálogo del centro de integraciones de Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort2.png %})

### Paso 3: Define la audiencia de tu cohorte {#step-3-define-your-cohort-audience}

Sincroniza tus cohortes con Braze mediante una activación en **Audience Studio** o ejecutando una consulta en **Data Workbench**.

{% alert important %}
Solo se añaden o eliminan de una cohorte los usuarios que ya existen en Braze. La importación de cohortes no creará nuevos usuarios en Braze.
{% endalert %}

{% tabs local %}
{% tab Data Workbench %}
#### Paso 3.1: Define tu consulta {#step-31-define-your-query}

{% alert note %}
Las columnas de consulta deben especificarse con los nombres de columna y el tipo de datos exactos. Las columnas de consulta deben incluir al menos una de las columnas: `user_ids`, `device_ids`, o la columna de alias de Braze que coincida con la configuración en la interfaz de usuario. Solo se añadirán a una cohorte los perfiles de usuario que existan en Braze. La importación de cohortes no creará nuevos perfiles de usuario.
{% endalert %}

1. Ve a **Data Workbench** > **Queries**.
2. Selecciona **New Query**.
3. Ejecuta la consulta para validar el conjunto de resultados.

![Catálogo del centro de integraciones de Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort3.png %})

##### Caso de uso: Sincronización de cohortes por identificador {#use-case-syncing-cohorts-by-identifier}

{% subtabs local %}
{% subtab Syncing External IDs %}
Aquí tienes una tabla de ejemplo en Treasure Data:

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case: Syncing cohorts by identifier" }

{% alert warning %}
El nombre de la columna debe ser `user_ids` o la sincronización fallará.
{% endalert %}

Para sincronizar cohortes utilizando el ID externo, ejecuta la siguiente consulta:

```sql
SELECT
  external_id as user_ids
FROM
  example_cohort_table
```

Tras ejecutar la consulta, estos alias de usuario se añadirán a la cohorte en Braze:

 - `TDCohort1`
 - `TDCohort2`
 - `TDCohort3`
 - `TDCohort4`
{% endsubtab %}

{% subtab Syncing User Aliases %}
Aquí tienes una tabla de ejemplo en Treasure Data:

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case: Syncing cohorts by identifier" }

Para sincronizar cohortes utilizando el alias de usuario, ejecuta la siguiente consulta:

```sql
SELECT
  email
FROM
  example_cohort_table
```

Tras ejecutar la consulta, estos alias de usuario se añadirán a la cohorte en Braze:

 - `"alias_label":"email", "alias_name":"TDCohort1@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort2@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort3@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort4@gmail.com"`
{% endsubtab %}

{% subtab Syncing Device IDs %}
Aquí tienes una tabla de ejemplo en Treasure Data:

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case: Syncing cohorts by identifier" }

{% alert warning %}
El nombre de la columna debe ser `device_ids` o la sincronización fallará.
{% endalert %}

Para sincronizar cohortes utilizando el ID de dispositivo, ejecuta la siguiente consulta:

```sql
SELECT
  device_ids
FROM
  example_cohort_table
```

Tras ejecutar la consulta, estos ID de dispositivo se añadirán a la cohorte en Braze:

- `1a2b3c`
- `4d5f6g`
- `7h8j9k`
- `1ab2cd`
{% endsubtab %}
{% endsubtabs %}

#### Paso 3.2: Especifica el destino de la exportación de resultados {#step-32-specify-the-result-export-target}

Una vez creada la consulta, selecciona **Export Results**. Puedes seleccionar una autenticación existente, como la creada en los pasos anteriores, o crear una nueva autenticación que se utilizará para la salida.

![Catálogo del centro de integraciones de Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort5.png %})


| Mapeado de resultados de exportación | Descripción |
| ----------- | ----------- |
| ID de cohorte | Este es el identificador de cohorte del backend que se enviará a Braze. |
| Nombre de la cohorte (opcional) | Este es el nombre que aparecerá dentro del filtro de cohortes en la herramienta de segmentación de Braze. Si no se configura, se utilizará `Cohort ID` como `Cohort Name`. |
| Operación | Se utiliza para determinar si la consulta debe añadir o eliminar perfiles de la cohorte en Braze. |
| Alias (opcional) | Cuando se define, el nombre de la columna correspondiente dentro de tu consulta se enviará como `alias_label`, y los valores de cada fila de la columna se enviarán como `alias_name`. |
| Número de hilos | Número de llamadas concurrentes a la API. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3.2: Specify the result export target" }

Sigue [los pasos de Treasure Data](https://docs.treasuredata.com/articles/#!int/braze-cohort-export-integration/a/ExportIntegrationTemplate-SpecifytheResultExportTarget) para configurar tu exportación según tu caso de uso.

#### Paso 3.3: Ejecuta la consulta {#step-33-execute-the-query}

Guarda la consulta con un nombre y ejecútala, o simplemente ejecútala. Una vez completada con éxito la consulta, el resultado se exporta automáticamente a Braze.

{% endtab %}
{% tab Audience Studio %}
#### Paso 3.1: Crea una activación {#step-31-create-an-activation}

Crea un nuevo segmento o elige un segmento existente para sincronizarlo con Braze como cohorte. Dentro del segmento, selecciona **Create Activation**.

#### Paso 3.2: Completa los detalles de tu activación {#step-32-fill-out-your-activation-details}

![Detalles de activación de las integraciones de Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort7.png %})

| Configuración de detalles de activación | Descripción |
| ----------- | ----------- |
| Nombre de activación | El nombre de tu activación. |
| Descripción de la activación | Una breve descripción de la activación. |
| Autenticación | Elige la autenticación de cohorte de Braze creada en el paso 2. |
| ID de cohorte | Este es el identificador de cohorte del backend que se enviará a Braze. |
| Nombre de la cohorte (opcional) | Este es el nombre que aparecerá dentro del filtro de cohortes en la herramienta de segmentación de Braze. Si no se configura, se utilizará `Cohort ID` como `Cohort Name`. |
| Operación | Se utiliza para determinar si la consulta debe añadir o eliminar perfiles de la cohorte en Braze. |
| Alias (opcional) | Cuando se define, el nombre de la columna correspondiente dentro de tu consulta se enviará como `alias_label`, y los valores de cada fila de la columna se enviarán como `alias_name`. |
| Número de hilos | Número de llamadas concurrentes a la API. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3.2: Fill out your activation details" }

#### Paso 3.3: Configura el mapeado de salida {#step-33-set-up-output-mapping}

![Mapeado de salida de activación de integraciones de Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort6.png %})

| Mapeado de salida de activación | Descripción |
| ----------- | ----------- |
| Columnas de atributos | Determina las columnas de tu base de datos de segmentos que se mapearán como identificadores al sincronizar perfiles con una cohorte de Braze. |
| Constructor de cadenas | El constructor de cadenas no es necesario para la integración de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3.3: Set up output mapping" }

{% alert important %}
 - Si se utiliza `device_id` como identificador, el **Output Column Name** debe ser `device_ids`.
 - Cuando utilices alias como identificador, el **Output Column Name** debe ser el nombre de la columna correspondiente dentro de tu consulta, que se enviará como `alias_label`, y los valores de cada fila de la columna se enviarán como `alias_name`.
 - Si se utiliza `external_id` como identificador, el **Output Column Name** debe ser `user_ids`.
{% endalert %}

Se ignorarán todos los nombres de columnas no relevantes o con nombres erróneos. Puedes elegir utilizar más de un identificador en tus sincronizaciones.

#### Paso 3.4: Define tu calendario de activación {#step-34-define-your-activation-schedule}

Define el calendario de sincronización que desees y guarda la activación.

![Calendario de activación de las integraciones de Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort8.png %})
{% endtab %}
{% endtabs %}

### Paso 4: Crea un segmento de Braze a partir de la exportación de Treasure Data {#step-4-create-a-braze-segment-from-the-treasure-data-export}

En Braze, ve a **Segments**, crea un nuevo segmento y selecciona **Treasure Data Cohorts** como filtro. Desde aquí, puedes elegir qué cohorte de Treasure Data deseas incluir. Una vez creado tu segmento de cohorte de Treasure Data, puedes seleccionarlo como filtro de audiencia al crear una campaña o Canvas.

![Catálogo del centro de integraciones de Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort4.png %})

## Coincidencia de usuarios {#user-matching}

Los usuarios identificados pueden coincidir por su `external_id` o `alias`. Los usuarios anónimos pueden coincidir por su `device_id`. Los usuarios identificados que fueron creados originalmente como usuarios anónimos no pueden ser identificados por su `device_id`, y deben ser identificados por su `external_id` o `alias`.