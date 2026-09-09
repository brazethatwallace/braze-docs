---
nav_title: Vista de carrusel
article_title: Vista de carrusel de Content Cards para iOS
platform: iOS
page_order: 5
description: "Este artículo explica cómo implementar un caso de uso de vista de carrusel de Content Cards para aplicaciones iOS."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Caso de uso: vista de carrusel {#use-case-carousel-view}

![Ejemplo de aplicación de noticias que muestra un carrusel de Content Cards en un artículo.]({% image_buster/assets/img_archive/cc_politer_carousel.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Esta sección explica cómo implementar una fuente de carrusel de varias tarjetas en la que el usuario puede deslizar horizontalmente el dedo para ver más tarjetas destacadas. Para integrar una vista de carrusel, tendrás que utilizar una implementación de Content Cards totalmente personalizada: la fase "correr" del [enfoque "rastrear, caminar, correr"]({{site.baseurl}}/developer_guide/getting_started/customization_overview).

Con este enfoque, no utilizarás las vistas de Braze ni la lógica predeterminada, sino que mostrarás las Content Cards de forma totalmente personalizada utilizando tus propias vistas pobladas con datos de los modelos de Braze.

En términos de nivel de esfuerzo de desarrollo, las diferencias clave entre la implementación básica y la implementación de carrusel incluyen:

- Construir tus propias vistas
- Registrar análisis de Content Cards
- Introducir lógica adicional en el lado del cliente para dictar cuántas y qué tarjetas mostrar en el carrusel

## Implementación {#implementation}

### Paso 1: Crear un controlador de vista personalizado {#step-1-create-a-custom-view-controller}

Para crear el carrusel de Content Cards, crea tu propio controlador de vista personalizado (como `UICollectionViewController`) y [suscríbete a las actualizaciones de datos]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration#getting-the-data). Ten en cuenta que no podrás extender o heredar de nuestro `ABKContentCardTableViewController` predeterminado, ya que solo es capaz de manejar nuestros tipos de Content Cards predeterminados.

### Paso 2: Implementar análisis {#step-2-implement-analytics}

Al crear un controlador de vista completamente personalizado, las impresiones, los clics y los descartes de Content Cards no se registran automáticamente. Debes implementar los métodos de análisis correspondientes para asegurar que las impresiones, los eventos de descarte y los clics se registren correctamente en los análisis del panel de Braze.

Para obtener información sobre los métodos de análisis, consulta [Métodos de tarjeta]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration#card-methods).

{% alert note %}
La misma página también detalla las diferentes propiedades heredadas de nuestra clase genérica del modelo de Content Cards, que pueden resultarte útiles durante la implementación de tu vista.
{% endalert %}

### Paso 3: Crear un observador de Content Cards {#step-3-create-a-content-card-observer}

Crea un [observador de Content Cards]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds#step-2-set-up-a-content-card-listener) que sea responsable de gestionar la llegada de Content Cards e implementa lógica condicional para mostrar un número específico de tarjetas en el carrusel en cualquier momento. De forma predeterminada, las Content Cards se ordenan por fecha de creación (las más recientes primero) y el usuario ve todas las tarjetas para las que es elegible.

Dicho esto, podrías ordenar y aplicar lógica de visualización adicional de varias maneras. Por ejemplo, podrías seleccionar los primeros cinco objetos de Content Cards del array o introducir pares clave-valor (la propiedad `extras` en el modelo de datos) para construir lógica condicional.

Si estás implementando un carrusel como una fuente secundaria de Content Cards, consulta [Usar múltiples fuentes de Content Cards]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds) para asegurarte de ordenar las tarjetas en la fuente correcta según los pares clave-valor.

{% alert important %}
Es importante asegurar que tus equipos de marketing y desarrolladores coordinen qué pares clave-valor se utilizarán (por ejemplo, `feed_type = brand_homepage`), ya que cualquier par clave-valor que los especialistas en marketing introduzcan en el panel de Braze debe coincidir exactamente con los pares clave-valor que los desarrolladores integren en la lógica de la aplicación.
{% endalert %}

Para consultar la documentación específica de iOS para desarrolladores sobre la clase, los métodos y los atributos de Content Cards, consulta la [referencia de la clase `ABKContentCard` de iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html).

## Consideraciones {#considerations}

- Al usar vistas completamente personalizadas, no podrás extender ni crear subclases de los métodos utilizados en `ABKContentCardsController`. En su lugar, tendrás que integrar tú mismo los métodos y propiedades del modelo de datos.
- La lógica e implementación de la vista de carrusel no es un tipo predeterminado de Content Cards en Braze, por lo que la lógica para lograr el caso de uso debe ser proporcionada y soportada por tu equipo de desarrollo.
- Tendrás que implementar lógica del lado del cliente para mostrar un número específico de tarjetas en el carrusel en un momento dado.