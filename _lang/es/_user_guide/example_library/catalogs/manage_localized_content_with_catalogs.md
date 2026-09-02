---
nav_title: Contenido localizado en catálogos
article_title: Gestionar contenido localizado con catálogos de Braze
page_order: 3
page_type: reference
description: "Almacena textos de productos localizados, precios y URL de imágenes en catálogos de Braze y resuelve el idioma correcto en el momento del envío."
---

# Gestionar contenido localizado con catálogos de Braze {#manage-localized-content-with-braze-catalogs}

> Almacena cadenas localizadas y URL en catálogos para que cada usuario reciba el texto en su idioma desde una única Campaign o Canvas, sin variantes separadas por idioma.

## Acerca de este ejemplo {#about-this-example}

PantsLabyrinth, un comercio minorista de ropa ficticio, vende sus productos en Norteamérica y Europa. Los nombres de productos, precios e imágenes principales varían según el idioma, pero el equipo de marketing quiere una sola plantilla de correo electrónico o push que personalice en el momento del envío.

Este ejemplo cubre tres patrones de catálogo que leen el {% raw %}`${language}`{% endraw %} [atributo estándar]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) del usuario (recopilado por el SDK or kit de desarrollo de software a partir del idioma del dispositivo):

- Campos de objeto JSON: todos los idiomas en una sola fila por artículo
- Columnas planas por idioma: `header_en`, `header_fr`, etc.
- Catálogo separado por idioma: nombre de catálogo dinámico como `pantslabyrinth-promo-en`

Usa catálogos cuando el contenido localizado sea datos estructurados (productos, promociones, URL de imágenes). Para textos de mensaje de formato libre en correo electrónico o push, prefiere los [mensajes multilingües]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) cuando tus canales los soporten. Para comparar patrones de localización de forma más amplia, consulta [Gestión de traducciones]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#translation-management).

## Consideraciones {#considerations}

- Los ejemplos son ilustrativos. Confirma las mayúsculas y el formato de {% raw %}`${language}`{% endraw %} en tu base de usuarios antes de nombrar claves o sufijos de catálogo.
- Para los métodos 1 y 2, si {% raw %}`${language}`{% endraw %} está vacío o no coincide con una clave o campo del catálogo, el resultado localizado puede quedar vacío; verifica cada campo de forma independiente y recurre a un valor predeterminado (por ejemplo, inglés).
- Para el método 3, define una lista de códigos de idioma admitidos antes de construir el nombre del catálogo; un catálogo inexistente cancela el mensaje.
- Los [objetos JSON]({{site.baseurl}}/user_guide/data/activation/catalogs/create#supported-data-types) en catálogos se pueden crear o actualizar a través de la API o mediante [ingesta de datos en la nube (CDI) para catálogos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data), no mediante carga de CSV.
- El método 2 admite mantenimiento por CSV, pero multiplica las columnas a medida que se agregan idiomas. Los archivos CSV admiten hasta [1000 columnas]({{site.baseurl}}/user_guide/data/activation/catalogs/create#step-1-review-your-csv-file).
- El método 3 requiere un catálogo para cada código de idioma que llegue a la etiqueta `catalog_items`. Si el catálogo no existe, Braze cancela el mensaje. Un ID de artículo inexistente en un catálogo existente devuelve un array de artículos vacío.
- Las etiquetas de Liquid de catálogo no se pueden usar de forma [recursiva]({{site.baseurl}}/user_guide/data/activation/catalogs/use#using-liquid).
- Las [selecciones de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) admiten hasta 10 filtros y devuelven hasta 50 artículos; valida los filtros contra el esquema de tu catálogo.
- Revisa los [niveles de almacenamiento de catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/create#tiers) si mantienes fuentes de productos grandes con múltiples idiomas.

## Configuración {#setup}

### Paso 1: Elige una estructura de catálogo {#step-1-choose-a-catalog-structure}

Elige una estructura de catálogo usando la guía de esta tabla.

| Método | Ideal cuando | Contrapartida |
| --- | --- | --- |
| Campos de objeto JSON | Catálogo de tamaño mediano; una fila por artículo; actualizaciones mediante API o CDI | Agregar un idioma actualiza cada artículo mediante API; no se puede usar CSV para campos JSON |
| Campos planos por idioma | Pocos idiomas y campos; equipos sin perfil de ingeniería usan CSV | Cada nuevo idioma agrega columnas; los nombres de campos deben mantenerse consistentes |
| Catálogo por idioma | Fuentes grandes por idioma o propietarios de idioma separados; CSV por idioma | Cada código de idioma admitido necesita un catálogo; los catálogos inexistentes cancelan el envío |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Elige una estructura de catálogo" }

### Paso 2: Crea el catálogo y los artículos {#step-2-create-the-catalog-and-items}

1. Ve a **Configuración de datos** > **Catálogos** y crea un catálogo (o varios catálogos para el método 3).
2. Agrega campos y artículos según la estructura elegida. Consulta [Crear un catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create).
3. (Opcional) Crea una [selección de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) para filtrar artículos, por ejemplo por `category` que coincida con un atributo personalizado del usuario.

{% tabs local %}
{% tab Método 1: Campos JSON %}
Ejemplo de artículo en el catálogo `PantsLabyrinth_Product_Copy`:

| Artículo | Valor |
| --- | --- |
| `id` | `trail-runner-001` |
| `name` | `{"EN":"Trail Runner","FR":"Chaussure de trail","DE":"Trailrunner"}` |
| `category` | `footwear` |
| `url` | `https://pantslabyrinth.shop/products/trail-runner-001` |
| `price` | `{"EN":"$120 USD","FR":"112 EUR","DE":"112 EUR"}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ejemplo de artículo de catálogo con campos JSON de idioma" }

{% endtab %}
{% tab Método 2: Campos planos %}
Ejemplo de artículo en el catálogo `PantsLabyrinth_Promo_Copy`:

| Artículo | Valor |
| --- | --- |
| `id` | `spring-sale` |
| `header_en` | `Spring trail sale` |
| `header_fr` | `Soldes de printemps` |
| `body_en` | `Save on trail runners this week.` |
| `body_fr` | `Économisez sur les chaussures de trail cette semaine.` |
| `cta_text_en` | `Shop now` |
| `cta_text_fr` | `Acheter` |
| `img_src_en` | `https://cdn.pantslabyrinth.shop/en/spring.jpg` |
| `img_src_fr` | `https://cdn.pantslabyrinth.shop/fr/spring.jpg` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ejemplo de artículo de catálogo con campos planos por idioma" }

{% endtab %}
{% tab Método 3: Catálogo por idioma %}
Crea un catálogo por idioma con los mismos campos. Por ejemplo, repite el mismo `id` y los mismos campos en `pantslabyrinth-promo-fr` y `pantslabyrinth-promo-de` con valores localizados.

Ejemplo de artículo en `pantslabyrinth-promo-en`:

| Artículo | Valor |
| --- | --- |
| `id` | `spring-sale` |
| `header` | `Spring trail sale` |
| `body` | `Save on trail runners this week.` |
| `cta_text` | `Shop now` |
| `img_src` | `https://cdn.pantslabyrinth.shop/en/spring.jpg` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ejemplo de artículo en un catálogo por idioma en inglés" }

{% endtab %}
{% endtabs %}

### Paso 3: Agrega Liquid a tu mensaje {#step-3-add-liquid-to-your-message}

Selecciona el patrón de Liquid que corresponda a la estructura de catálogo que elegiste en el paso 1.

{% tabs local %}
{% tab Método 1: Campos JSON %}
Almacena todos los idiomas en campos de objeto JSON en una sola fila de catálogo y luego usa el filtro `property_accessor` para leer las claves `name` y `price` que coincidan con {% raw %}`${language}`{% endraw %} (normalizado a mayúsculas). Verifica cada campo de forma independiente y recurre a `EN` cuando ese campo esté vacío, de modo que un idioma con nombre pero sin precio reciba igualmente un precio en inglés.

{% raw %}
```liquid
{% catalog_items PantsLabyrinth_Product_Copy trail-runner-001 %}
{% assign lang = ${language} | upcase %}
{% assign localized_name = items[0].name | property_accessor: lang %}
{% assign localized_price = items[0].price | property_accessor: lang %}
{% if localized_name == blank %}
  {% assign localized_name = items[0].name | property_accessor: 'EN' %}
{% endif %}
{% if localized_price == blank %}
  {% assign localized_price = items[0].price | property_accessor: 'EN' %}
{% endif %}
Product: {{ localized_name }}
Price: {{ localized_price }}
```
{% endraw %}

Consulta [Filtro property accessor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#property-accessor-filter).
{% endtab %}
{% tab Método 2: Campos planos %}
Construye nombres de campo dinámicos a partir de {% raw %}`${language}`{% endraw %} (normalizado a minúsculas) y luego lee esos campos del artículo con búsqueda por corchetes. Por ejemplo, {% raw %}`items[0][header_field]`{% endraw %} lee el encabezado del idioma resuelto. Verifica cada campo de forma independiente y recurre a la columna en inglés cuando ese campo esté vacío, de modo que un idioma con encabezado pero sin cuerpo reciba igualmente el texto del cuerpo en inglés.

{% raw %}
```liquid
{% catalog_items PantsLabyrinth_Promo_Copy spring-sale %}
{% assign lang = ${language} | downcase %}
{% assign header_field = 'header_' | append: lang %}
{% assign body_field = 'body_' | append: lang %}
{% assign cta_field = 'cta_text_' | append: lang %}
{% assign img_field = 'img_src_' | append: lang %}
{% assign header_val = items[0][header_field] %}
{% assign body_val = items[0][body_field] %}
{% assign cta_val = items[0][cta_field] %}
{% assign img_val = items[0][img_field] %}
{% if header_val == blank %}
  {% assign header_val = items[0].header_en %}
{% endif %}
{% if body_val == blank %}
  {% assign body_val = items[0].body_en %}
{% endif %}
{% if cta_val == blank %}
  {% assign cta_val = items[0].cta_text_en %}
{% endif %}
{% if img_val == blank %}
  {% assign img_val = items[0].img_src_en %}
{% endif %}
<img src="{{ img_val }}" alt="" />
<h2>{{ header_val }}</h2>
<p>{{ body_val }}</p>
<a href="#">{{ cta_val }}</a>
```
{% endraw %}
{% endtab %}
{% tab Método 3: Catálogo por idioma %}
{% alert warning %}
Si el nombre de catálogo que pasas a `catalog_items` no existe, Braze cancela el mensaje. Define una lista de códigos de idioma admitidos antes de construir el nombre del catálogo. Un ID de artículo inexistente en un catálogo existente devuelve un array de artículos vacío; puedes recurrir al catálogo en inglés solo en ese caso.
{% endalert %}

Define una lista de los códigos de idioma que tienen catálogos correspondientes (aquí `en`, `fr` y `de`), asigna los valores no admitidos o vacíos a `en` y luego busca el artículo. Si el ID del artículo no existe en ese catálogo, recurre al catálogo en inglés.

{% raw %}
```liquid
{% assign lang = ${language} | downcase %}
{% assign supported = 'en,fr,de' | split: ',' %}
{% if supported contains lang %}{% else %}{% assign lang = 'en' %}{% endif %}
{% assign theCatalog = 'pantslabyrinth-promo-' | append: lang %}
{% catalog_items {{ theCatalog }} spring-sale %}
{% if items[0] == blank %}
  {% catalog_items pantslabyrinth-promo-en spring-sale %}
{% endif %}
<img src="{{ items[0].img_src }}" alt="" />
<h2>{{ items[0].header }}</h2>
<p>{{ items[0].body }}</p>
<a href="#">{{ items[0].cta_text }}</a>
```
{% endraw %}

Consulta [Uso de plantillas en nombres de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create#template-catalog-names) y [Cancelar mensajes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).
{% endtab %}
{% endtabs %}

#### Selección de catálogo opcional por categoría {#optional-catalog-selection-by-category}

Filtra artículos antes de la personalización, por ejemplo promociones de calzado para usuarios con `preferred_category = footwear`:

{% raw %}
```liquid
{% catalog_selection_items PantsLabyrinth_Product_Copy footwear_promos %}
{% for item in items %}
  {{ item.name }}
{% endfor %}
```
{% endraw %}

Define la selección en el panel con filtros en tu columna `category` y atributos del usuario según sea necesario.

### Paso 4: Vista previa y pruebas {#step-4-preview-and-test}

1. Usa **Vista previa como usuario** con perfiles de usuario que tengan diferentes valores de {% raw %}`${language}`{% endraw %}.
2. Confirma el texto alternativo cuando el idioma esté ausente o no sea compatible, incluidos los casos de localización parcial (por ejemplo, un nombre sin precio).
3. Para el método 3, confirma que cada idioma admitido tenga un catálogo correspondiente y que los códigos de idioma no admitidos se asignen a tu catálogo predeterminado sin cancelar el envío.

## Artículos relacionados {#related-articles}

- [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [Usar catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/use)
- [Selecciones]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- [Crear un catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create)
- [Filtros avanzados de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#property-accessor-filter)
- [Localización]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)
- [Mensajes multilingües]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)
- [Sincronizar y eliminar datos de catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)
- [Cancelar mensajes de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)