---
nav_title: Scuba
article_title: Scuba Analytics
description: "Esta referencia técnica de Scuba y Braze describe cómo activar la información de datos en tiempo real de Scuba mediante Segments de Braze."
page_type: partner
search_tag: Partner
noindex: true
hidden: true
---

# Scuba Analytics

>[Scuba Analytics](https://scuba.io) es una plataforma de colaboración de datos de pila completa, impulsada por aprendizaje automático y diseñada para datos de series temporales de alta velocidad. Scuba te permite exportar selectivamente usuarios (también llamados actores) y cargarlos en tu plataforma Braze. En Scuba, las propiedades de actor personalizadas se utilizan para analizar tendencias de comportamiento, activar tus datos en varias plataformas y realizar modelos predictivos mediante aprendizaje automático.

_Esta integración es mantenida por Scuba Analytics._

## Requisitos previos {#prerequisites}

Para usar Scuba Analytics con Braze, necesitarás lo siguiente:

| Requisito | Descripción |
|---|---|
| Token de API de Scuba | Un token de API de Scuba que puedes obtener desde el endpoint `https://{scuba_hostname}/api/create_token`. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos de `users.track`. <br><br> Puedes crearla en el panel de Braze desde **Configuración** > **Claves de API**. |
| Endpoint REST de Braze | La URL de tu endpoint REST. Tu endpoint dependerá de la [URL de Braze para tu instancia](https://scuba.io). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Carga de datos de Scuba en Braze {#uploading-your-scuba-data-to-braze}

{% alert important %}
La siguiente solicitud utiliza curl. Para una mejor gestión de solicitudes de API, recomendamos usar un cliente de API, como Postman.
{% endalert %}

Para cargar tus datos de Scuba en Braze, realiza una solicitud POST a `https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation` utilizando el tipo de contenido `application/json`:

```bash
curl -X POST "https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation" \
-H "content-type: application/json" \
-d '{"braze_host":"BRAZE_API_ENDPOINT", \
"braze_api_key":"BRAZE_API_KEY", \
"scuba_host":"HOSTNAME", \
"scuba_token":"SCUBA_API_TOKEN", \
"scuba_table_name":"TABLE_NAME", \
"scuba_actor_property_name":"ACTOR_PROPERTY_NAME", \
"scuba_actor_property_value_filter":"ACTOR_PROPERTY_FILTER" \
"scuba_actor_id":"ACTOR_ID", \
"scuba_period_start":"PERIOD_START", \
"scuba_period_end":"PERIOD_END", \
"scuba_record_limit":"RECORD_LIMIT"}'
```

Sustituye los siguientes valores:

| Marcador de posición | Descripción |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT` | La URL del endpoint REST de Braze de tu instancia actual de Braze. Para más información, consulta [Claves de API REST]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). |
| `BRAZE_API_KEY` | Tu clave de API REST de Braze con el permiso `users.track`. |
| `HOSTNAME` | El nombre de host de tu instancia actual de Scuba. |
| `SCUBA_API_TOKEN` | Tu token de API de Scuba. |
| `TABLE_NAME` | La tabla a la que pertenece tu conjunto de datos. Para más información, consulta [Glosario: tabla de conjunto de datos](https://docs.scuba.io/glossary/dataset-table). |
| `ACTOR_PROPERTY_NAME` | La propiedad de actor a la que pertenece tu conjunto de datos. Solo se devolverán los datos que coincidan con este nombre. Para más información, consulta [Glosario: propiedad de actor](https://docs.scuba.io/glossary/actor-property). |
| `ACTOR_PROPERTY_FILTER` | El filtro de búsqueda de audiencia para tu propiedad de actor. |
| `ACTOR_ID` | El ID de la propiedad de actor a la que pertenece tu conjunto de datos. Este ID coincide con tu `external_id` en Braze. Para más información, consulta [Glosario: actor](https://docs.scuba.io/glossary/actor). |
| `PERIOD_START` | El período de inicio como una fecha compatible con BQL. Para más información, consulta [Sintaxis y uso de BQL](https://docs.scuba.io/guides/bql-syntax-and-usage). |
| `PERIOD_END` | El período de fin como una fecha compatible con BQL. Para más información, consulta [Sintaxis y uso de BQL](https://docs.scuba.io/guides/bql-syntax-and-usage). |
| `RECORD_LIMIT` | **Opcional**: El número máximo de registros a devolver. Si se omite `scuba_record_limit`, Scuba devolverá un máximo de 100 registros. Para cambiar esto, asigna cualquier número no negativo a `scuba_record_limit`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Carga de datos de Scuba en Braze" }

### Comportamiento predeterminado {#default-behavior}

De forma predeterminada, `update_existing_only` está configurado como `false`, lo que actualizará tus registros existentes en Braze, así como creará nuevos registros para aquellos que no existan. Para evitar que Scuba cree nuevos registros, configura `update_existing_only` como `true`.

### Límite de velocidad {#rate-limit}

Scuba aplica un límite de velocidad de 50 000 solicitudes por minuto a este endpoint.

## Creación de segmentos con datos de comportamiento de Scuba {#creating-segments-using-scubas-behavioral-data}

Después de [cargar tus datos](#uploading-your-scuba-data-to-braze), puedes crear segmentos de usuarios en Braze utilizando los datos de comportamiento de Scuba.

### Paso 1: Crea un nuevo segmento {#step-1-create-a-new-segment}

En Braze, ve a **Audiencia** > **Segments** y selecciona **Create Segment**. A continuación, introduce un nombre para tu segmento.

![Creación de un nuevo segmento en Braze.]({% image_buster /assets/img/scuba/analytics/segment_name.png %})

### Paso 2: Busca y selecciona el atributo de Scuba {#step-2-find-and-select-the-scuba-attribute}

En **Segment Details** > **Filters**, selecciona **Custom Attributes**.

![Selección del filtro "Custom Attribute" en "Segment Details".]({% image_buster /assets/img/scuba/analytics/filter_attribute.png %})

Selecciona **Search custom attributes** y elige el nombre de la propiedad del actor que utilizaste en tu solicitud POST anterior.

![Selección de la propiedad del actor como atributo personalizado.]({% image_buster /assets/img/scuba/analytics/select_property.png %})

### Paso 3: Configura el atributo {#step-3-configure-the-attribute}

Junto al nombre de la propiedad del actor, elige un operador y un valor (si corresponde). Estos valores están determinados por las propiedades del actor que hayas definido en Scuba. Cuando termines, selecciona **Save**.

![Elección de un operador y un valor para el atributo seleccionado.]({% image_buster /assets/img/scuba/analytics/operator_end.png %})