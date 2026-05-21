---
nav_title: Selecciones
article_title: Selecciones
page_order: 5
alias: /catalog_selections/
description: "Este artículo de referencia explica cómo crear y usar selecciones con tus catálogos para referenciar datos en tus campañas de Braze."
---

# Selecciones {#selections}

> Esta página explica cómo crear y usar selecciones con tus [catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/).

## Cómo funciona {#how-it-works}

Las selecciones son grupos de datos que pueden usarse para personalizar un mensaje para cada usuario en tu campaña. Cuando usas una selección, básicamente estás configurando filtros personalizados basados en columnas específicas de tu catálogo. Esto puede incluir filtros por marca, tamaño, ubicación, fecha de adición y más. Te da control sobre lo que muestras a los usuarios al permitirte definir criterios que los artículos deben cumplir primero.

Después de crear un catálogo, puedes seguir haciendo referencia a los datos de tu catálogo incorporando selecciones en tus Campaigns o recomendaciones de Braze.

![La sección Selecciones en un catálogo de ejemplo.]({% image_buster /assets/img_archive/catalog_selections1.png %})

## Lo que debes saber {#things-to-know}

- Puedes crear hasta 30 selecciones por catálogo.
- Puedes añadir hasta 10 filtros por selección.
- Las selecciones son ideales para refinar las recomendaciones a partir de los datos de catálogo de Braze. Si buscas inspiración, consulta [Acerca de las recomendaciones de artículos]({{site.baseurl}}/user_guide/brazeai/item_recommendations/) para ver ejemplos de casos de uso.

## Operadores compatibles {#supported-operators}

Al crear un filtro de selección, los operadores disponibles dependen del tipo de campo que selecciones.

| Tipo de campo | Operadores disponibles |
| --- | --- |
| Cadena | `equals`, `does not equal`, `is any of`, `is none of` |
| Número | `equals`, `does not equal`, `greater than`, `less than` |
| Booleano | `is` |
| Hora | `before`, `after` |
| Array | `includes value`, `does not include value` |
| Geo | `geo within`, `geo outside` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Supported operators" }

Los operadores `is any of` e `is none of` están disponibles para campos de cadena y cada uno admite hasta 10 valores.

## Crear una selección {#creating-a-selection}

Para crear una selección, haz lo siguiente.

1. Ve a **Catalogs** y selecciona tu catálogo de la lista.
2. Selecciona la pestaña **Selection** y haz clic en **Create Selection**.
3. Dale a tu selección un nombre y una descripción opcional.
4. En **Filter Field**, selecciona la columna del catálogo por la que deseas filtrar. Los campos de cadena con más de 1000 caracteres no se pueden seleccionar para filtros.
5. Termina de definir los criterios de filtrado seleccionando el operador y el atributo correspondientes. Para ver una lista completa de operadores por tipo de campo, consulta [Operadores compatibles](#supported-operators).
6. En la sección **Sort type**, determina cómo se ordenan los resultados. De forma predeterminada, los resultados se devuelven sin un orden particular. Para especificar la ordenación por un campo concreto, desactiva **Randomize Sort Order** y especifica el **Sort Field** y el **Sort Order** (ascendente o descendente).
7. En la sección **Results limit**, introduce los resultados (hasta 50).
8. Selecciona **Create Selection**.

### Probar y previsualizar {#test-and-preview}

Después de crear una selección, puedes usar la sección **Preview for user** para ver lo que devolvería una selección para un usuario aleatorio o un usuario específico. Para las selecciones que usan personalización, solo puedes ver la vista previa después de seleccionar un usuario.

### Liquid en los resultados de la selección {#liquid-in-selection-results}

El uso de cualquier Liquid en los catálogos, como atributos personalizados y eventos personalizados, puede hacer que se devuelvan resultados diferentes para cada usuario en tu selección.

{% alert note %}
El Liquid de Contenido conectado no es compatible con esta configuración de filtros.
{% endalert %}

![Configuración de filtros para la selección de catálogo donde el atributo se establece como un atributo personalizado de Liquid.]({% image_buster /assets/img_archive/catalog_selections7.png %})

## Usar selecciones en la mensajería {#using-selections-in-messaging}

Después de crear tu selección, personaliza tus mensajes con Liquid para insertar los elementos filtrados de ese catálogo. Puedes hacer que Braze genere el Liquid por ti desde la ventana de personalización que se encuentra en los creadores de mensajes:

1. En cualquier creador de mensajes que admita personalización, selecciona <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Añadir personalización"></i> para abrir la ventana de personalización.
2. En **Personalization Type**, selecciona **Catalog Items**.
3. Selecciona el nombre de tu catálogo.
4. En **Item selection method**, selecciona **Use a selection**.
4. Selecciona tu selección de la lista.
5. En **Information to Display**, selecciona qué campos del catálogo deben incluirse para cada artículo.
6. Selecciona el icono **Copy** y pega el Liquid donde sea necesario en tu mensaje.

![El modal Add Personalization con las siguientes selecciones: "Catalog Items" para "Personalization Type", "Games" para "Catalog Name", "Selections" para "Selection Type", "game_selection" para "Selection", y "title" y "description_en" para "Information to Display".]({% image_buster /assets/img_archive/catalog_selections6.png %}){: style="max-width:70%;"}

## Caso de uso {#use-case}

Supongamos que tienes un servicio de reparto de comida a domicilio y quieres enviar un mensaje personalizado a tus usuarios que tienen preferencias específicas de comida basadas en la categoría de alimentos que consultaron más recientemente.

Usando un catálogo con la información de tu servicio de reparto de comidas para el nombre de la comida, el precio, la imagen y la categoría de la comida, puedes crear una selección para recomendar tres comidas basadas en la categoría que el usuario consultó más recientemente.

![Un ejemplo de selección para un servicio de reparto de comidas con dos filtros: uno que identifica un tipo de producto como comida, y otro que identifica la categoría como la consultada más recientemente. La selección está configurada para aleatorizar el orden en que se devuelven los tres resultados.]({% image_buster /assets/img_archive/catalog_selections2.png %}){: style="max-width:90%;"}

Para usar este catálogo y esta selección en una campaña, utiliza el modal **Add Personalization** en la sección de composición de mensajes al crear una Campaign. En este ejemplo, hemos seleccionado el catálogo con la información de tu servicio de reparto de comidas, y la selección para recomendaciones de comidas basadas en la categoría consultada más recientemente. Esto nos permite mostrar el nombre de la comida y el precio. Para enriquecer aún más tu mensaje, puedes usar la selección para añadir también una imagen de la primera comida recomendada.

![Una tarjeta de contenido con el encabezado "¡Te ENCANTARÁN estas comidas tan valoradas!" con la selección "recommendations_be_recent_category" en la sección de composición del mensaje.]({% image_buster /assets/img_archive/catalog_selections3.png %}){: style="max-width:90%;"}

Por ejemplo, supongamos que tienes un usuario cuya categoría consultada más recientemente es "Pollo". Usando la personalización configurada y una campaña de tarjeta de contenido, puedes enviar tres recomendaciones de comidas que incluyan pollo para este usuario.

![Una tarjeta de contenido con una imagen de pollo al limón a la parrilla, y una lista de tres recomendaciones de comidas que incluyen pollo basadas en la categoría que el usuario consultó más recientemente.]({% image_buster /assets/img_archive/catalog_selections4.png %}){: style="max-width:90%;"}

Usando la misma personalización, también puedes enviar tres recomendaciones de comidas para un usuario cuya categoría consultada más recientemente sea "Carne de vacuno".

![Una tarjeta de contenido con una imagen de stroganoff de ternera, y una lista de dos recomendaciones de comidas que incluyen ternera basadas en la categoría que el usuario consultó más recientemente.]({% image_buster /assets/img_archive/catalog_selections5.png %}){: style="max-width:90%;"}