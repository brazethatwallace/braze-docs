---
nav_title: "GET: Exportar atributos personalizados"
article_title: "GET: Exportar atributos personalizados"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint Exportar atributos personalizados de Braze."

---
{% api %}
# Exportar atributos personalizados {#export-custom-attributes}
{% apimethod get %}
/custom_attributes
{% endapimethod %}

> Utiliza este endpoint para exportar una lista de atributos personalizados registrados para tu aplicación. Los atributos se devuelven en grupos de 50, ordenados alfabéticamente.

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `custom_attributes.get`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='custom_attributes' %}

## Parámetros de consulta {#query-parameters}

Ten en cuenta que cada llamada a este endpoint devolverá 50 atributos. Para más de 50 atributos, utiliza el encabezado `Link` para recuperar los datos en la página siguiente, como se muestra en el siguiente ejemplo de respuesta.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `cursor` | Opcional | Cadena | Determina la paginación de los atributos personalizados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de consulta" }

## Ejemplos de solicitudes {#example-requests}

### Sin cursor {#without-cursor}

```
curl --location --request GET 'https://rest.iad-01.braze.com/custom_attributes' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Con cursor {#with-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/custom_attributes?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta {#response}

```json
{
    "message": (string) returns 'success' when the request completes without errors,
    "attributes" : [
        {
            "array_length": 100, (number) the maximum array length, or null if not applicable,
            "data_type": "Number", (string) the data type,
            "description": "The attribute description", (string) the attribute description,
            "name": "The attribute name", (string) the attribute name,
            "status": "Active", (string) the attribute status,
            "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the attribute formatted as strings,
        },
        ...
    ]
}
```

### Códigos de respuesta de error fatal {#fatal-export}

Para conocer los códigos de estado y los mensajes de error asociados que se devolverán si tu solicitud encuentra un error fatal, consulta [Errores fatales]({{site.baseurl}}/api/errors#fatal-errors).

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}