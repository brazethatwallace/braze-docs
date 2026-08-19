---
nav_title: Hacer coincidir artículos del catálogo con un arreglo de atributos
article_title: Hacer coincidir artículos del catálogo con un arreglo de atributos personalizados
page_order: 2
page_type: reference
description: "Usa una selección de catálogo y Liquid para mostrar filas del catálogo cuyos nombres o ID aparecen en un arreglo de atributos personalizados, como una lista de deseos."
---

# Hacer coincidir artículos del catálogo con un arreglo de atributos personalizados {#match-catalog-items-to-a-custom-attribute-array}

> Cuando cada usuario guarda una lista de nombres de productos en su perfil, usa una selección de catálogo junto con Liquid para mostrar solo las filas del catálogo que aparecen en esa lista; por ejemplo, un correo electrónico de lista de deseos.

## Acerca de este ejemplo {#about-this-example}

Flash & Thread almacena los nombres de productos guardados de cada cliente en un atributo personalizado de tipo arreglo de cadenas (`saved_product_names`). Su catálogo contiene los detalles completos del producto (categoría, precio, URL de imagen, inventario).

Las selecciones de catálogo pueden filtrar columnas del catálogo contra valores estáticos o de Liquid, incluidos campos de arreglo en las filas del catálogo. No filtran una fila del catálogo contra valores almacenados en un arreglo del perfil de usuario. Para personalizar a partir de la lista del usuario, devuelve un conjunto amplio de artículos del catálogo con una selección y luego usa Liquid para conservar solo las filas que coincidan con el arreglo del perfil.

Este patrón:

1. Asigna el atributo personalizado de tipo arreglo del usuario a una variable Liquid.
2. Llama a `catalog_selection_items` para una selección de catálogo prefiltrada (hasta 50 artículos).
3. Itera sobre `items` y usa `contains` para hacer coincidir cada campo del catálogo (por ejemplo, `name` o `id`) con el arreglo.

{% alert important %}
Este patrón funciona solo cuando el conjunto de resultados de la selección (hasta 50 filas del catálogo) puede contener de forma plausible los artículos guardados de cada usuario; por ejemplo, catálogos pequeños o catálogos donde los filtros reducen la selección lo suficiente como para cubrir una lista típica. Si los artículos guardados de un usuario quedan fuera de las 50 filas devueltas, el bucle no encuentra coincidencias y el mensaje no muestra nada para esos artículos; ningún filtro resuelve esto en el caso general, porque la selección no puede hacer coincidir contra el arreglo del perfil del usuario.
{% endalert %}

## Consideraciones {#considerations}

- Prueba los datos de Liquid y del catálogo en un espacio de trabajo de pruebas antes de enviar a los clientes.
- Dado que una selección devuelve como máximo 50 filas del catálogo, agrega filtros (por ejemplo, en existencia, categoría activa o rango de precio) que mantengan los artículos guardados probables de cada usuario dentro de ese conjunto de resultados.
- Este ejemplo usa un arreglo de cadenas en el perfil de usuario.
- Para un arreglo de objetos, haz coincidir con una propiedad dentro de cada objeto (por ejemplo, `product_id`) y ajusta la verificación `contains` o usa un bucle `for` sobre los objetos. Consulta [Arreglo de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects).
- El comportamiento de `contains` depende del tipo de atributo; para arreglos, usa `contains` en lugar de `==`. Consulta [Lógica condicional]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic).
- Haz coincidir con identificadores estables (por ejemplo, el `id` del catálogo) cuando los nombres de productos puedan cambiar o duplicarse.
- Los fragmentos de código Liquid en este artículo son ejemplos. Valida la representación en tus canales (HTML de correo electrónico, push, etc.).

## Configuración {#setup}

Este ejemplo asume:

| Activo | Detalles |
| --- | --- |
| Atributo personalizado | `saved_product_names` — arreglo de cadenas (por ejemplo, `["linen_shirt", "trail_jacket", "canvas_tote"]`) |
| Catálogo | `apparel_products` con columnas `id`, `category`, `name`, `price`, `inventory`, `image_url` |
| Selección | `in_stock_apparel` en `apparel_products`, límite de resultados 50, con filtros que excluyen filas irrelevantes (por ejemplo, `inventory` mayor que `0`) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuración" }

### Paso 1: Crear el catálogo y la selección {#step-1-create-the-catalog-and-selection}

1. Importa o sincroniza las filas de productos en un catálogo llamado `apparel_products`.
2. Crea una selección (por ejemplo, `in_stock_apparel`) que devuelva tantas filas relevantes como necesites, hasta el límite de 50 artículos.
3. Agrega filtros a la selección para descartar filas que nunca quieras en el mensaje (sin existencia, categoría incorrecta, etc.).

Para la configuración de selecciones, consulta [Selecciones]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

### Paso 2: Agregar Liquid en tu mensaje {#step-2-add-liquid-in-your-message}

Asigna el arreglo del perfil, carga la selección e itera con `contains`:

{% raw %}
```liquid
{% assign saved_product_names = custom_attribute.${saved_product_names} %}
{% catalog_selection_items apparel_products in_stock_apparel %}
{% for item in items %}
{% if saved_product_names contains item.name %}
Product: {{ item.name }}
Category: {{ item.category }}
Price: ${{ item.price }}
Image: {{ item.image_url }}
{% endif %}
{% endfor %}
```
{% endraw %}

Reemplaza `item.name` con `item.id` (u otra columna) si tu arreglo almacena ID en lugar de nombres para mostrar. Agrega espaciado o HTML entre los campos según tu canal. En {% raw %}`${{ item.price }}`{% endraw %}, el `$` es un símbolo de moneda literal que se imprime antes de la salida de Liquid; no forma parte de la sintaxis de personalización {% raw %}`${}`{% endraw %} de Braze.

Para generar este Liquid automáticamente, abre el modal **Agregar personalización** (**Artículos del catálogo** > **Usar una selección**). Consulta [Uso de catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/use).

### Paso 3: Vista previa y prueba {#step-3-preview-and-test}

Envía mensajes de prueba a perfiles con diferentes valores de `saved_product_names`. Confirma que solo aparezcan las filas del catálogo que coincidan y que un arreglo vacío no produzca líneas de productos.

## Artículos relacionados {#related-articles}

- [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [Selecciones]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- [Uso de catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/use)
- [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)
- [Lógica condicional]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic)
- [Biblioteca de casos de uso de Liquid: encontrar una cadena dentro de un arreglo]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases#misc-string-in-array)