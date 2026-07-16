---
nav_title: Configuración de tablas
article_title: Configuración de tablas de ingesta de datos en la nube
toc_headers: h2
page_order: 2
page_type: reference
description: "Aprende a configurar tu tabla de origen de CDI y en qué se diferencia esa configuración de los requisitos de formato de la carga útil."
---

# Configuración de tablas de ingesta de datos en la nube {#cloud-data-ingestion-table-setup}

> Usa esta página para separar dos requisitos relacionados pero diferentes de la ingesta de datos en la nube (CDI): la configuración de la tabla de origen y el formato de la carga útil.

## Comprender la configuración de tablas en comparación con el formato de la carga útil {#understand-table-setup-compared-to-payload-formatting}

Para las sincronizaciones de datos de usuario de CDI, configura ambos:

| Capa | Qué controla |
| --- | --- |
| Configuración de la tabla de origen | Columnas obligatorias, identificadores de usuario y comportamiento de sincronización de `UPDATED_AT` |
| Formato de la carga útil | Campos JSON en `PAYLOAD`, incluida la forma del objeto para atributos, eventos y compras |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprender la configuración de tablas en comparación con el formato de la carga útil" }

Braze lee las filas de tu tabla de origen primero y luego valida el campo `PAYLOAD` en función del tipo de datos seleccionado.

## Configurar tu tabla de origen {#set-up-your-source-table}

Para las sincronizaciones de datos de usuario del almacén de datos, tu tabla o vista de origen debe incluir:

- `UPDATED_AT`
- `PAYLOAD`
- Una o más columnas de identificador de usuario compatibles:
  - `EXTERNAL_ID`
  - `ALIAS_NAME` y `ALIAS_LABEL`
  - `BRAZE_ID`
  - `EMAIL`
  - `PHONE`

Cada fila debe incluir un tipo de identificador a la vez, incluso si tu tabla contiene múltiples columnas de identificador.

### Requisitos de `UPDATED_AT` {#updated_at-requirements}

- Almacena los valores de `UPDATED_AT` en UTC para evitar problemas con el horario de verano.
- Braze sincroniza las filas en las que `UPDATED_AT` es posterior al último valor sincronizado.
- Las filas en la marca de tiempo exacta del límite pueden volver a sincronizarse si nuevas filas comparten esa marca de tiempo.

Para orientación sobre marcas de tiempo duplicadas y actualizaciones incrementales, consulta [Mejores prácticas de ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#avoid-resyncing-rows-with-duplicate-timestamps).

{% alert note %}
Las fuentes de almacenamiento de archivos utilizan requisitos de configuración diferentes y no son compatibles con `UPDATED_AT`. Para más detalles, consulta [Integraciones de almacenamiento de archivos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#required-file-formats).
{% endalert %}

## Configurar la columna `PAYLOAD` {#set-up-the-payload-column}

El valor de `PAYLOAD` sigue los mismos formatos de objeto utilizados por el endpoint `/users/track` de Braze para el tipo de datos seleccionado.

| Tipo de datos | Referencia de formato |
| --- | --- |
| `attributes` | [Objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens) |
| `events` | [Objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object) |
| `purchases` | [Objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurar la columna PAYLOAD" }

Para atributos anidados, incluye las fechas utilizando el formato en [Capturar fechas como propiedades de objeto]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#capturing-dates-as-object-properties).

### Ejemplos de carga útil {#payload-examples}

{% tabs local %}
{% tab Atributos personalizados anidados %}
Puedes incluir atributos personalizados anidados en la columna de carga útil para una sincronización de atributos personalizados.

```json
{
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
}
```

{% endtab %}
{% tab Evento %}
Para sincronizar eventos, se requiere un nombre de evento. Formatea el campo `time` como una cadena ISO 8601 o en formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Si el campo `time` no está presente, Braze utiliza el valor de la columna `UPDATED_AT` como la hora del evento. Otros campos, incluidos `app_id` y `properties`, son opcionales.

Puedes sincronizar un evento por fila.

```json
{
    "app_id" : "your-app-id",
    "name" : "rented_movie",
    "time" : "2013-07-16T19:20:45+01:00",
    "properties": {
        "movie": "The Sad Egg",
        "director": "Alex Smith"
    }
}
```

{% endtab %}
{% tab Compra %}
Para sincronizar eventos de compra, se requieren `product_id`, `currency` y `price`. Formatea el campo opcional `time` como una cadena ISO 8601 o en formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Si el campo `time` no está presente, Braze utiliza el valor de la columna `UPDATED_AT` como la hora del evento. Otros campos, incluidos `app_id`, `quantity` y `properties`, son opcionales.

Puedes sincronizar un evento de compra por fila.

```json
{
    "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
    "product_id" : "Completed Order",
    "currency" : "USD",
    "price" : 219.98,
    "time" : "2013-07-16T19:20:30+01:00",
    "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99 },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99 }
        ]
    }
}
```

{% endtab %}
{% tab Grupos de suscripción %}
Para sincronizar estados de grupos de suscripción, incluye uno o más pares de `subscription_group_id` y `subscription_state` en cada fila.
```json
{
    "subscription_groups" : [
        {
            "subscription_group_id": "subscription_group_identifier_1",
            "subscription_state": "unsubscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_2",
            "subscription_state": "subscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_3",
            "subscription_state": "subscribed"
        }
      ]
}
```
{% endtab %}
{% endtabs %}

## Documentación relacionada de configuración de CDI {#related-cdi-setup-docs}

- Para ejemplos de DDL específicos de cada fuente, consulta [Integraciones de almacén de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).
- Para la configuración basada en archivos, consulta [Integraciones de almacenamiento de archivos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations).
- Para orientación sobre el comportamiento de sincronización y optimización, consulta [Mejores prácticas de ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices).