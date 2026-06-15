---
nav_title: Catálogo
article_title: Catálogo
page_order: 2
description: "Aprende a usar catálogos como origen de datos para personalizar tus mensajes de Braze con datos que no son de usuario, como detalles de productos, fuentes de contenido y precios."
---

# Catálogo {#catalog}

> Haz referencia a datos que no son de usuario en tus mensajes conectándote a catálogos. Los catálogos almacenan conjuntos de datos estructurados, como información de productos, listados de restaurantes o fuentes de contenido, a los que puedes acceder a través de Liquid para personalizar cualquier mensaje.

## Cómo funciona {#how-it-works}

{% raw %}
Después de importar datos a un catálogo (a través de CSV o API), haz referencia a los elementos del catálogo en tus mensajes usando la etiqueta de Liquid `items`. Por ejemplo, para obtener el nombre de un producto de un catálogo llamado `products`:

```liquid
{% catalog_items products {{${product_id}}} %}
{{items[0].name}} is back in stock!
```
{% endraw %}

Los catálogos admiten hasta 1000 campos por elemento y pueden almacenar millones de filas, lo que los hace adecuados para grandes inventarios de productos y bibliotecas de contenido.

## Casos de uso comunes {#common-use-cases}

| Caso de uso | Descripción |
| --- | --- |
| Detalles de productos | Inserta nombres, descripciones, precios e imágenes de un catálogo de productos |
| Listados de restaurantes o tiendas | Personaliza mensajes con detalles específicos de la ubicación |
| Recomendaciones de contenido | Haz referencia a artículos, videos u otros elementos multimedia |
| Información de eventos | Incluye fechas de eventos, lugares y descripciones en los mensajes |
| Ofertas basadas en niveles | Asocia promociones al nivel de membresía o segmento de un usuario |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso comunes" }

## Desencadenadores de catálogo {#catalog-triggers}

Los catálogos también potencian la mensajería automatizada a través de desencadenadores de catálogo. Configura notificaciones de vuelta en stock y notificaciones de bajada de precio para enviar mensajes automáticamente a los usuarios cuando los elementos del catálogo cambien.

Para más información, consulta [Desencadenadores de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/).

## Selecciones {#selections}

Usa las selecciones para agrupar elementos del catálogo según los filtros que definas. Por ejemplo, crea una selección de elementos por debajo de $20 o elementos en una categoría específica, y luego haz referencia al conjunto filtrado en tus mensajes.

Para más información, consulta [Selecciones]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/).

## Primeros pasos {#getting-started}

Para crear y administrar catálogos, consulta [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/). Para aprender a hacer referencia a datos de catálogo en tus mensajes, consulta [Uso de catálogos en un mensaje]({{site.baseurl}}/user_guide/data/activation/catalogs/use/).