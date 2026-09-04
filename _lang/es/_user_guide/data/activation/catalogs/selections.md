---
nav_title: Selecciones
article_title: Selecciones
page_order: 5
alias: /catalog_selections/
description: "Este artículo de referencia explica cómo crear y usar selecciones con tus catálogos para referenciar datos en tus campañas de Braze."
---

# Selecciones {#selections}

> Las selecciones son grupos de datos que puedes usar para personalizar un mensaje para cada usuario en tu campaña. Cuando usas una selección, básicamente estás configurando filtros personalizados basados en columnas específicas de tu catálogo. Esto puede incluir filtros por marca, tamaño, ubicación, fecha de adición y más. Te da control sobre lo que muestras a los usuarios al permitirte definir criterios que los artículos deben cumplir primero.<br><br>Esta página explica cómo crear y usar selecciones con tus catálogos.

Después de crear un [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs), puedes seguir haciendo referencia a los datos de tu catálogo incorporando selecciones en tus campañas o recomendaciones de Braze.

![La sección Selecciones en un catálogo de ejemplo.]({% image_buster /assets/img_archive/catalog_selections1.png %})

## Lo que debes saber {#things-to-know}

- Puedes crear hasta 30 selecciones por catálogo.
- Puedes añadir hasta 10 filtros por selección.
- Las selecciones son ideales para refinar recomendaciones a partir de datos de catálogos de Braze. Si buscas inspiración, consulta [Acerca de las recomendaciones de artículos]({{site.baseurl}}/user_guide/brazeai/item_recommendations) para ver ejemplos.

## Filtros de geolocalización {#geolocation-filters}

Si tu catálogo incluye un [tipo de campo de geolocalización]({{site.baseurl}}/user_guide/data/activation/catalogs/create#supported-data-types), puedes usar filtros basados en geolocalización en tus selecciones para mostrar elementos del catálogo según su proximidad a un punto geográfico.

Hay dos operadores de geolocalización disponibles:

| Operador | Descripción |
| -------- | ----------- |
| `geo within` | Devuelve elementos cuyo campo de geolocalización se encuentra dentro de un radio especificado de un punto central. |
| `geo outside` | Devuelve elementos cuyo campo de geolocalización se encuentra fuera de un radio especificado de un punto central. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Cuando se aplica un filtro de geolocalización, los resultados se ordenan por distancia, con el elemento más cercano en primer lugar.

### Configurar el punto central con Liquid {#setting-the-center-point-with-liquid}

Puedes establecer el punto central de forma dinámica usando Liquid. Por ejemplo, para filtrar elementos en relación con la ubicación más reciente de cada usuario, usa el atributo {% raw %}`{{${most_recent_location}}}`{% endraw %} como valor del filtro:

{% raw %}
```
{{${most_recent_location}}}
```
{% endraw %}

### Ejemplo: mostrar las ubicaciones de tiendas más cercanas {#use-case-show-the-nearest-store-locations}

Supongamos que tu catálogo contiene un campo `store_location` de tipo Geolocation. Puedes crear una selección que use el operador `geo within` para devolver ubicaciones de tiendas dentro de un radio determinado de la ubicación más reciente de cada usuario. Establece el valor del filtro en {% raw %}`{{${most_recent_location}}}`{% endraw %} para que el punto central se actualice por usuario. Como los resultados se ordenan por distancia, el primer elemento devuelto es siempre la tienda más cercana.

## Crear una selección {#creating-a-selection}

Para crear una selección, haz lo siguiente.

1. Ve a **Catálogos** y selecciona tu catálogo de la lista.
2. Selecciona la pestaña **Selección** y haz clic en **Crear selección**.
3. Dale un nombre a tu selección y una descripción opcional.
4. En **Campo de filtro**, selecciona la columna del catálogo por la que quieres filtrar. Los campos de cadena con más de 1.000 caracteres no se pueden seleccionar como filtros.
5. Termina de definir tus criterios de filtro seleccionando el operador relevante (por ejemplo, "es igual a" o "no es igual a") y el atributo.
6. En la sección **Tipo de ordenación**, determina cómo se ordenan los resultados. Por defecto, los resultados se devuelven sin un orden particular. Para especificar la ordenación por un campo específico, desactiva **Aleatorizar orden de clasificación** y especifica el **Campo de ordenación** y el **Orden de clasificación** (ascendente o descendente).
7. En la sección **Límite de resultados**, introduce los resultados (hasta 50).
8. Selecciona **Crear selección**.

### Probar y previsualizar {#test-and-preview}

Después de crear una selección, puedes usar la sección **Vista previa para usuario** para ver lo que devolvería una selección para un usuario aleatorio o un usuario específico. Para selecciones que usan personalización, solo puedes ver la vista previa después de seleccionar un usuario.

### Liquid en los resultados de selección {#liquid-in-selection-results}

El uso de cualquier Liquid en los catálogos, como atributos personalizados y eventos personalizados, puede dar lugar a diferentes resultados devueltos para cada usuario en tu selección.

{% alert note %}
Liquid de contenido conectado no es compatible con esta configuración de filtros.
{% endalert %}

![Configuración de filtros para la selección del catálogo donde el atributo está establecido como un atributo personalizado de Liquid.]({% image_buster /assets/img_archive/catalog_selections7.png %})

## Uso de selecciones en la mensajería {#using-selections-in-messaging}

Después de crear tu selección, personaliza tus mensajes con Liquid para insertar los elementos filtrados de ese catálogo. Puedes hacer que Braze genere el Liquid por ti desde la ventana de personalización que se encuentra en los creadores de mensajes:

1. En cualquier creador de mensajes que admita personalización, selecciona <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Añadir personalización"></i> **Añadir personalización** para abrir la ventana de personalización.
2. En **Tipo de personalización**, selecciona **Elementos del catálogo**.
3. Selecciona el nombre de tu catálogo.
4. En **Método de selección de elementos**, selecciona **Usar una selección**.
4. Selecciona tu selección de la lista.
5. En **Información a mostrar**, selecciona qué campos del catálogo deben incluirse para cada elemento.
6. Selecciona el icono **Copiar** y pega el Liquid donde sea necesario en tu mensaje.

![El modal Añadir personalización con las siguientes selecciones: "Elementos del catálogo" para "Tipo de personalización", "Games" para "Nombre del catálogo", "Selecciones" para "Tipo de selección", "game_selection" para "Selección", y "title" y "description_en" para "Información a mostrar".]({% image_buster /assets/img_archive/catalog_selections6.png %}){: style="max-width:70%;"}

{% alert note %}
La vista previa de personalización en el panel de composición de Liquid muestra hasta tres selecciones de catálogo, independientemente del límite de resultados que hayas configurado. Este es el comportamiento esperado: el mensaje real enviado a los usuarios respeta el límite de resultados configurado.
{% endalert %}

## Ejemplo {#use-case}

Supongamos que tienes un servicio de entrega de comidas y quieres enviar un mensaje personalizado a tus usuarios que tienen preferencias específicas de comida basadas en su categoría de alimentos vista más recientemente.

Usando un catálogo con la información de tu servicio de entrega de comidas para el nombre del platillo, precio, imagen y categoría del platillo, puedes crear una selección para recomendar tres platillos basados en la categoría vista más recientemente por un usuario.

![Un ejemplo de una selección para un servicio de entrega de comidas con dos filtros: uno que identifica un tipo de producto como platillo, y uno que identifica la categoría como la vista más recientemente. La selección está configurada para aleatorizar el orden en que se devuelven los tres resultados.]({% image_buster /assets/img_archive/catalog_selections2.png %}){: style="max-width:90%;"}

Para usar este catálogo y selección en una campaña, usa el modal **Añadir personalización** en la sección de composición de mensajes al crear una campaña. En este ejemplo, hemos seleccionado el catálogo con la información de tu servicio de entrega de comidas, y la selección para recomendaciones de platillos basadas en la categoría vista más recientemente. Esto nos permite mostrar el nombre del platillo y el precio. Para construir aún más tu mensaje, puedes usar la selección para también añadir una imagen del primer platillo recomendado.

![Una tarjeta de contenido con el encabezado "¡Te ENCANTARÁN estos platillos altamente calificados!" con la selección "recommendations_be_recent_category" en la sección de composición de mensajes.]({% image_buster /assets/img_archive/catalog_selections3.png %}){: style="max-width:90%;"}

Por ejemplo, supongamos que tienes un usuario cuya categoría vista más recientemente es "Pollo". Usando la personalización configurada y una campaña de tarjeta de contenido, puedes enviar tres recomendaciones de platillos que incluyan pollo para este usuario.

![Una tarjeta de contenido con una imagen de pollo al limón a la parrilla, y una lista de tres recomendaciones de platillos que incluyen pollo basadas en la categoría vista más recientemente del usuario.]({% image_buster /assets/img_archive/catalog_selections4.png %}){: style="max-width:90%;"}

Usando la misma personalización, también puedes enviar tres recomendaciones de platillos para un usuario cuya categoría vista más recientemente es "Res".

![Una tarjeta de contenido con una imagen de estroganoff de res, y una lista de dos recomendaciones de platillos que incluyen res basadas en la categoría vista más recientemente del usuario.]({% image_buster /assets/img_archive/catalog_selections5.png %}){: style="max-width:90%;"}