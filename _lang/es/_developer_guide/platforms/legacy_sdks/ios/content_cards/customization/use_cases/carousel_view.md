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

Esta sección explica cómo implementar una fuente de carrusel de varias tarjetas en la que el usuario puede deslizar horizontalmente el dedo para ver más tarjetas destacadas. Para integrar una vista de carrusel, tendrás que utilizar una implementación de Content Cards totalmente personalizada: la fase "correr" del [enfoque "rastrear, caminar, correr"]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize#customization-approaches).

Con este enfoque, no utilizarás las vistas de Braze ni la lógica predeterminada, sino que mostrarás las Content Cards de forma totalmente personalizada utilizando tus propias vistas pobladas con datos de los modelos de Braze.

En términos de nivel de esfuerzo de desarrollo, las diferencias clave entre la implementación básica y la implementación de carrusel incluyen:

- Construir tus propias vistas
- Registrar análisis de Content Cards
- Introducir lógica adicional en el lado del cliente para dictar cuántas y qué tarjetas mostrar en el carrusel

## Implementación {#implementation}

### Paso 1: Crear un controlador de vista personalizado {#step-1-create-a-custom-view-controller}

Para crear el carrusel de Content Cards, crea tu propio controlador de vista personalizado (como `UICollectionViewController`) y [suscríbete para recibir actualizaciones de datos]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration#getting-the-data). Ten en cuenta que no podrás ampliar o subclasificar nuestro `ABKContentCardTableViewController` predeterminado, ya que solo puede gestionar los tipos de Content Cards predeterminados.

### Paso 2: Implementar análisis {#step-2-implement-analytics}

Al crear un controlador de vista totalmente personalizado, las impresiones, los clics y los rechazos de Content Cards no se registran automáticamente. Debes implementar los métodos de análisis respectivos para asegurarte de que las impresiones, los eventos de rechazo y los clics se registran correctamente en los análisis del dashboard de Braze.

Para obtener información sobre los métodos de análisis, consulta [Métodos de tarjeta]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration#card-methods).

{% alert note %}
En la misma página también se detallan las distintas propiedades heredadas de nuestra clase modelo genérica de Content Cards, que pueden resultarte útiles durante la implementación de tu vista.
{% endalert %}

### Paso 3: Crear un observador de Content Cards {#step-3-create-a-content-card-observer}

Crea un [observador de Content Cards]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds#step-2-set-up-a-content-card-listener) que se encargue de gestionar la llegada de Content Cards e implementa una lógica condicional para mostrar un número específico de tarjetas en el carrusel en un momento dado. Por defecto, las Content Cards se ordenan por fecha de creación (la más reciente primero), y el usuario ve todas las tarjetas para las que es elegible.

Dicho esto, podrías ordenar y aplicar lógica de visualización adicional de varias formas. Por ejemplo, podrías seleccionar los cinco primeros objetos de Content Cards de la matriz o introducir pares clave-valor (la propiedad `extras` en el modelo de datos) para construir una lógica condicional en torno a ellos.

Si estás implementando un carrusel como fuente secundaria de Content Cards, consulta [Utilizar múltiples fuentes de Content Cards]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds) para asegurarte de que ordenas las tarjetas en la fuente correcta basándote en los pares clave-valor.

{% alert important %}
Es importante asegurarse de que tus equipos de marketing y desarrollo se coordinan para decidir qué pares clave-valor se utilizarán (por ejemplo, `feed_type = brand_homepage`), ya que cualquier par clave-valor que los especialistas en marketing introduzcan en el dashboard de Braze debe coincidir exactamente con los pares clave-valor que los desarrolladores incorporen a la lógica de la aplicación.
{% endalert %}

Para obtener documentación específica para desarrolladores de iOS sobre la clase, los métodos y los atributos de Content Cards, consulta la [referencia de la clase `ABKContentCard`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html) de iOS.

## Consideraciones {#considerations}

- Al utilizar vistas completamente personalizadas, no podrás ampliar ni subclasificar los métodos utilizados en `ABKContentCardsController`. En su lugar, tendrás que integrar tú mismo los métodos y propiedades del modelo de datos.
- La lógica y la implementación de la vista de carrusel no es un tipo predeterminado de Content Cards en Braze, y por lo tanto la lógica para lograr el caso de uso debe ser proporcionada y mantenida por tu equipo de desarrollo.
- Tendrás que implementar la lógica del lado del cliente para mostrar un número específico de tarjetas en el carrusel en un momento dado.