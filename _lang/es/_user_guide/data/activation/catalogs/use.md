---
nav_title: Uso de catálogos
article_title: Usar catálogos
page_order: 1.5
description: "En este artículo de referencia se explica cómo utilizar catálogos para hacer referencia a datos de no usuarios en tus Campaigns de Braze a través de Liquid."
---

# Uso de catálogos {#using-catalogs}

> Después de crear un catálogo, puedes hacer referencia a datos de no usuarios en tus Campaigns de Braze a través de [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid). Puedes utilizar catálogos en todos tus canales de mensajería, incluso en cualquier parte del editor de arrastrar y soltar donde se admita Liquid.

## Utilización de catálogos en un mensaje {#using-catalogs-in-a-message}

El siguiente video muestra cómo utilizar catálogos en un mensaje.

{% multi_lang_include video.html id="4yc2jkyn6w" source="wistia" %}

### Paso 1: Añadir tipo de personalización {#step-one-personalization}

En el creador de mensajes que elijas, selecciona <i class="fas fa-plus-circle"></i> **Añadir personalización** y selecciona **Catalog Items** como **Tipo de personalización**. A continuación, selecciona el nombre de tu catálogo. Utilizando nuestro ejemplo anterior, seleccionaremos el catálogo "Games".

![Modal de Añadir personalización con Catalog Items seleccionado, el catálogo Games elegido y una vista previa de Liquid mostrando la etiqueta catalog_items.]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

Podemos ver inmediatamente la siguiente vista previa de Liquid:

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

### Paso 2: Selecciona elementos del catálogo {#step-2-select-catalog-items}

A continuación, ¡es hora de añadir los elementos de tu catálogo! Utiliza el menú desplegable para seleccionar los elementos del catálogo y la información que deseas mostrar. Esta información corresponde a las columnas del archivo CSV cargado para generar el catálogo.

Por ejemplo, para consultar el título y el precio de nuestro juego Tales, podríamos seleccionar el `id` de Tales (1234) como elemento del catálogo y solicitar `title` y `price` para la información mostrada.

{% raw %}
```liquid
{% catalog_items Games 1234 %}

Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

Esto se muestra de la siguiente manera:

> ¡Consigue Tales por solo 7,49!

## Exportación de catálogos {#exporting-catalogs}

Hay dos formas de exportar catálogos desde el dashboard:

- Coloca el cursor sobre la fila del catálogo en la sección **Catálogos**. A continuación, selecciona el botón **Exportar catálogo**.
- Selecciona tu catálogo. A continuación, selecciona el botón **Exportar catálogo** en la pestaña **Vista previa** del catálogo.

Recibirás un correo electrónico para descargar el archivo CSV después de iniciar la exportación. Tendrás hasta cuatro horas para recuperar este archivo.

## Casos de uso adicionales {#additional-use-cases}

### Varios elementos {#multiple-items}

No estás limitado a un solo elemento por mensaje. Utiliza el modal **Añadir personalización** para añadir hasta tres elementos del catálogo a la vez. Para añadir más, selecciona de nuevo **Añadir personalización** en el compositor y selecciona los elementos adicionales del catálogo y la información que deseas mostrar.

Echa un vistazo a este ejemplo en el que añadimos el `id` de tres juegos, Tales, Teslagrad y Acaratus, para **Catalog Items** y seleccionamos `title` para **Information to Display**.

![Modal de Añadir personalización mostrando tres ID de elementos del catálogo seleccionados y título elegido para Information to Display, con una vista previa de Liquid listando el título de cada elemento.]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

Podemos personalizar aún más nuestro mensaje añadiendo algo de texto alrededor de nuestro Liquid:

{% raw %}
```liquid
Get the ultimate trio {% catalog_items Games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

El resultado es el siguiente:

```Get the ultimate trio Tales, Teslagrad, and Acaratus today!```

{% alert tip %}
Check out [selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) to create groups of data for more personalized messaging!
{% endalert %}

### Using Liquid `if` statements

You can use catalog items to create conditional statements. For example, you can trigger a certain message to display when a specific item is selected in your campaign. You must declare the catalog (and, if applicable, the selection) before referencing `items` in an `if` statement.

#### With catalog items

{% raw %}
```liquid
{% catalog_items Games 1234 %}
{% if items[0].on_sale == true %}
  {{ items[0].title }} is on sale! Get it for {{ items[0].price }}.
{% else %}
  Check out {{ items[0].title }} at full price.
{% endif %}
```
{% endraw %}

En este ejemplo, la etiqueta `catalog_items` obtiene el elemento `1234` del catálogo `Games`, y luego la sentencia `if` comprueba el campo `on_sale` para mostrar diferentes mensajes.

#### Con selecciones de catálogo

{% raw %}
```liquid
{% catalog_selection_items item-list selections %}
{% if items[0].venue_name.size > 10 %}
Message if the venue name's size is more than 10 characters.
{% elsif items[0].venue_name.size <= 10 %}
Message if the venue name's size is 10 characters or fewer.
{% else %}
{% abort_message('no venue_name') %}
{% endif %}
```
{% endraw %}

En este ejemplo, se muestran diferentes mensajes en función de si el campo `venue_name` tiene más o menos de 10 caracteres. Si `venue_name` está en blanco, el mensaje se cancela.

Para obtener cuántos elementos devuelve una selección, utiliza el filtro `size` de Liquid en la matriz `items` después de la etiqueta, no en un campo individual:

{% raw %}
```liquid
{% catalog_selection_items item-list selections %}{{ items | size }}
```
{% endraw %}

{% alert tip %}
Para evitar errores de sintaxis de Liquid, selecciona el botón **+** más en el creador de mensajes para insertar automáticamente las etiquetas de Liquid del catálogo.
{% endalert %}

### Utilizar imágenes {#using-images}

También puedes hacer referencia a imágenes del catálogo para utilizarlas en tus mensajes. Para ello, utiliza la etiqueta `catalogs` y el objeto `item` en el campo de Liquid para imágenes.

Por ejemplo, para añadir el `image_link` de nuestro catálogo de Games a nuestro mensaje promocional para Tales, selecciona el `id` para el campo **Catalog Items** y `image_link` para el campo **Information to Display**. Esto añade las siguientes etiquetas de Liquid a nuestro campo de imagen:

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

![Compositor de tarjetas de contenido con la etiqueta de Liquid del catálogo utilizada en el campo de imagen.]({% image_buster /assets/img_archive/catalog_image_link1.png %})

Así es como se ve cuando se renderiza el Liquid:

![Ejemplo de tarjeta de contenido con etiquetas de Liquid del catálogo renderizadas.]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

{% alert important %}
En canales **HTML** como el correo electrónico, evita espacios adicionales o saltos de línea entre la etiqueta de cierre `{% raw %}{% catalog_items ... %}{% endraw %}` y el Liquid que imprime la URL de la imagen (por ejemplo, `{% raw %}{{ items[0].image_link }}{% endraw %}`). Los espacios en blanco adicionales en la plantilla pueden impedir que la URL de la imagen se resuelva correctamente en el mensaje renderizado. Mantén la expresión de la URL inmediatamente adyacente a la etiqueta del catálogo, como en: `{% raw %}<img src="{% catalog_items Games 1234 %}{{ items[0].image_link }}">{% endraw %}`.
{% endalert %}

### Plantillas de elementos de catálogo

También puedes utilizar plantillas para extraer dinámicamente elementos del catálogo en función de atributos personalizados. Por ejemplo, supongamos que un usuario tiene el atributo personalizado `wishlist`, que contiene una matriz de ID de juegos de tu catálogo.

```json
{
    "attributes": [
        {
            "external_id": "user_id",
            "wishlist": ["1234", "1235"]
        }
    ]
}
```

{% alert note %}
Los objetos JSON de los catálogos solo se ingieren a través de la API. No puedes cargar un objeto JSON utilizando un archivo CSV.
{% endalert %}

Utilizando plantillas de Liquid, puedes extraer dinámicamente los ID de la lista de deseos y utilizarlos en tu mensaje. Para ello, [asigna una variable]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#assigning-variables) a tu atributo personalizado y, a continuación, utiliza el modal **Añadir personalización** para extraer un elemento específico de la matriz. Las variables a las que se hace referencia como ID de elemento del catálogo deben escribirse entre llaves para que se puedan referenciar correctamente, como por ejemplo `{{result}}`.

{% alert tip %}
Recuerda que las matrices empiezan en `0`, no en `1`.
{% endalert %}

Por ejemplo, para avisar a un usuario de que Tales (un elemento de nuestro catálogo que ha deseado) está en oferta, podemos añadir lo siguiente a nuestro creador de mensajes:

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now for {{ items[0].price }}!
```
{% endraw %}

Que se mostrará de la siguiente manera:
> ¡Consigue Tales ahora por solo 7,49!

Con las plantillas, puedes renderizar un elemento de catálogo diferente para cada usuario en función de sus atributos personalizados, propiedades del evento o cualquier otro campo que admita plantillas.

### Cargar un CSV

Puedes cargar un CSV de nuevos elementos de catálogo para añadir o elementos de catálogo para actualizar. Para eliminar una lista de elementos, puedes cargar un CSV con los ID de los elementos para eliminarlos.

### Utilizar Liquid

También puedes crear catálogos manualmente con lógica de Liquid. Sin embargo, ten en cuenta que si escribes un ID que no existe, Braze seguirá devolviendo una matriz de elementos sin objetos. Te recomendamos que incluyas gestión de errores, como la comprobación del tamaño de la matriz y el uso de una sentencia `if` para tener en cuenta el caso de una matriz vacía.

#### Elementos del catálogo con plantillas que incluyen Liquid

De forma similar al [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), debes utilizar la marca `:rerender` en una etiqueta de Liquid para renderizar el contenido Liquid de un elemento del catálogo. Ten en cuenta que la marca `:rerender` solo tiene un nivel de profundidad, lo que significa que no se aplicará a ninguna llamada anidada de etiquetas de Liquid.

Si un elemento del catálogo contiene campos de perfil de usuario (dentro de una etiqueta de personalización de Liquid), estos valores deben definirse en Liquid antes en el mensaje y antes de la plantilla para que el Liquid se renderice correctamente. Si no se proporciona la marca `:rerender`, se mostrará el contenido sin procesar de Liquid.

Por ejemplo, si un catálogo llamado "Messages" tiene un elemento con este Liquid:

![Fila de tabla del catálogo con id greet_msg y columna Welcome_Message que contiene un saludo de bienvenida a la tienda con una variable de Liquid de nombre.]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

Para renderizar el siguiente contenido Liquid:

{% raw %}
```liquid
Hi ${first_name},

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

Aparecerá lo siguiente:

{% raw %}
```
Hi Peter,

Welcome to our store, Peter!
```
{% endraw %}

{% alert note %}
Las etiquetas de Liquid de catálogos no pueden utilizarse recursivamente dentro de los catálogos.
{% endalert %}

## Solución de problemas de personalización de catálogos

Si el Liquid del catálogo o de la selección no se muestra como esperas en un mensaje o paso en Canvas, comprueba lo siguiente:

| Síntoma | Qué verificar |
| --- | --- |
| La vista previa muestra elementos, pero los envíos en vivo están vacíos | Confirma que los **ID de elementos** del catálogo existen en el momento del envío. Si el ID en tu Liquid no coincide con una fila, Braze devuelve una matriz de elementos vacía; consulta [Utilizar Liquid](#using-liquid). Comprueba si hay errores tipográficos y si las fuentes de ID (como las propiedades del evento) faltan en el desencadenador o en el perfil de usuario. |
| La vista previa del compositor funciona en una Campaign pero no en Canvas | Confirma que estás utilizando el contexto de Liquid correcto: **propiedades de contexto de Canvas** frente a **propiedades del evento**, y que esos campos existen en el desencadenador. Consulta [Propiedades de contexto y del evento]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties). |
| Una selección no devuelve elementos | Revisa los [filtros de selección]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) y los límites; confirma que los datos del catálogo están sincronizados y que los nombres de las columnas coinciden con tus filtros. |
| `:rerender` o la entrega con plantillas se ve incorrecta | Para Liquid anidado dentro de campos del catálogo, necesitas `:rerender` y el orden correcto de las variables; consulta [Elementos del catálogo con plantillas que incluyen Liquid](#templating-catalog-items-including-liquid). Los mensajes dentro de la aplicación con plantillas se resuelven en el momento del desencadenamiento; consulta [¿Qué son los mensajes dentro de la aplicación con plantillas?]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages). Algunos canales restringen las etiquetas de catálogo (por ejemplo, ciertos usos de **:rerender** con Banners); consulta [¿Se admiten todas las etiquetas de Liquid?]({{site.baseurl}}/user_guide/channels/banners/faq#are-all-liquid-tags-supported) en las preguntas frecuentes de Banners. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas de personalización de catálogos" }

Para el comportamiento general de Liquid, consulta [Casos de uso de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases) y [Utilizar Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid).

## Estructurar los datos de tu catálogo

Al planificar cómo estructurar los datos de tu catálogo, parte del caso de uso previsto y diseña el catálogo en torno a él. Cada fila del catálogo representa un elemento (con un `id` único). Las columnas deben contener los atributos de ese elemento, como URLs, texto descriptivo, URLs de imágenes, precio, valoración, talla o color.

### Cuándo usar llamadas estándar de catálogo

Con las llamadas estándar de catálogo, haces coincidir un valor con la columna `id`. Al insertar un atributo personalizado o una propiedad del evento (como cadena de ID) en la etiqueta de Liquid del catálogo, puedes extraer múltiples atributos de un solo elemento en tu mensaje. Los casos de uso más comunes incluyen:

- Producto o servicio visto recientemente
- Elementos de la lista de deseos
- Ofertas por ubicación
- Producto comprado
- Contenido por etapa del ciclo de vida
- Producto o servicio buscado más recientemente

### Cuándo usar selecciones de catálogo

Las [selecciones de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) te permiten filtrar por cualquier columna de tu catálogo y devolver hasta 50 elementos coincidentes. Al insertar atributos personalizados o propiedades del evento en los filtros de selección, los resultados se personalizan para cada usuario. Los casos de uso más comunes incluyen:

- Elementos cuya categoría coincide con la preferencia del usuario
- Elementos que coinciden con la marca, cocina o talla preferida del usuario
- Contenido por tipo de suscripción o nivel de fidelización
- Productos dentro del rango de valor medio de pedido del usuario

La diferencia clave es que las llamadas estándar de catálogo buscan un solo elemento conocido por `id`, mientras que las selecciones de catálogo consultan todo el catálogo y devuelven múltiples elementos que coinciden con tus criterios de filtro.

[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}