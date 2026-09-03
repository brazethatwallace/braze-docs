---
nav_title: Uso de catálogos
article_title: Uso de catálogos
page_order: 1.5
description: "En este artículo de referencia se explica cómo utilizar catálogos para hacer referencia a datos de no usuarios en tus Campaigns de Braze a través de Liquid."
---

# Uso de catálogos {#using-catalogs}

> Después de crear un catálogo, puedes hacer referencia a datos de no usuarios en tus Campaigns de Braze a través de [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid). Puedes utilizar catálogos en todos tus canales de mensajería, incluso en cualquier parte del editor de arrastrar y soltar donde se admita Liquid.

## Uso de catálogos en un mensaje {#using-catalogs-in-a-message}

El siguiente video muestra cómo usar catálogos en un mensaje.

{% multi_lang_include video.html id="4yc2jkyn6w" source="wistia" %}

### Paso 1: Añadir tipo de personalización {#step-one-personalization}

En el creador de mensajes de tu elección, selecciona <i class="fas fa-plus-circle"></i> **Añadir personalización** y selecciona **Elementos del catálogo** para el **Tipo de personalización**. A continuación, selecciona el nombre de tu catálogo. Usando nuestro ejemplo anterior, seleccionaremos el catálogo "Games".

![Modal Añadir personalización con Elementos del catálogo seleccionado, el catálogo Games elegido, y una vista previa de Liquid mostrando la etiqueta catalog_items.]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

Podemos ver inmediatamente la siguiente vista previa de Liquid:

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

### Paso 2: Seleccionar elementos del catálogo {#step-2-select-catalog-items}

A continuación, ¡es momento de añadir tus elementos del catálogo! Usando el desplegable, selecciona los elementos del catálogo y la información a mostrar. Esta información corresponde a las columnas del archivo CSV cargado que se usó para generar tu catálogo.

Por ejemplo, para hacer referencia al título y al precio de nuestro juego Tales, podríamos seleccionar el `id` de Tales (1234) como el elemento del catálogo y solicitar `title` y `price` para la información mostrada.

{% raw %}
```liquid
{% catalog_items Games 1234 %}

Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

Esto se muestra de la siguiente manera:

> Get Tales for just 7.49!

## Exportar catálogos {#exporting-catalogs}

Hay dos formas de exportar catálogos desde el panel:

- Pasa el cursor sobre la fila del catálogo en la sección **Catálogos**. Luego, selecciona el botón **Exportar catálogo**.
- Selecciona tu catálogo. Luego, selecciona el botón **Exportar catálogo** en la pestaña **Vista previa** del catálogo.

Recibirás un correo electrónico para descargar el archivo CSV después de iniciar la exportación. Tendrás hasta cuatro horas para recuperar este archivo.

## Casos de uso adicionales {#additional-use-cases}

### Múltiples elementos {#multiple-items}

No estás limitado a un solo elemento en un mensaje. Usa el modal **Añadir personalización** para agregar hasta tres elementos del catálogo a la vez. Para agregar más, selecciona **Añadir personalización** de nuevo en el creador y selecciona elementos del catálogo e información adicionales para mostrar.

Consulta este ejemplo donde agregamos el `id` de tres juegos, Tales, Teslagrad y Acaratus, para **Elementos del catálogo** y seleccionamos `title` para **Información a mostrar**.

![Modal de Añadir personalización que muestra tres IDs de elementos del catálogo seleccionados y title elegido para Información a mostrar, con una vista previa de Liquid listando el título de cada elemento.]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

Podemos personalizar aún más nuestro mensaje agregando algo de texto alrededor de nuestro Liquid:

{% raw %}
```liquid
Get the ultimate trio {% catalog_items Games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

Esto se muestra de la siguiente manera:

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

En este ejemplo, la etiqueta `catalog_items` obtiene el elemento `1234` del catálogo `Games`, y luego la sentencia `if` verifica el campo `on_sale` para mostrar mensajes diferentes.

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

En este ejemplo, se muestran mensajes diferentes según si el campo `venue_name` tiene más o menos de 10 caracteres. Si `venue_name` está en blanco, el mensaje se aborta.

Para obtener cuántos elementos devuelve una selección, usa el filtro Liquid `size` en el array `items` después de la etiqueta, no en un campo individual:

{% raw %}
```liquid
{% catalog_selection_items item-list selections %}{{ items | size }}
```
{% endraw %}

{% alert tip %}
Para evitar errores de sintaxis en Liquid, selecciona el botón **+** (más) en el creador de mensajes para insertar etiquetas de Liquid del catálogo automáticamente.
{% endalert %}

### Uso de imágenes {#using-images}

También puedes referenciar imágenes en el catálogo para usarlas en tu mensajería. Para hacerlo, usa la etiqueta `catalogs` y el objeto `item` en el campo de Liquid para imágenes.

Por ejemplo, para agregar el `image_link` de nuestro catálogo Games a nuestro mensaje promocional para Tales, selecciona el `id` para el campo **Elementos del catálogo** e `image_link` para el campo **Información a mostrar**. Esto agrega las siguientes etiquetas de Liquid a nuestro campo de imagen:

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

![Creador de tarjeta de contenido con la etiqueta de Liquid del catálogo usada en el campo de imagen.]({% image_buster /assets/img_archive/catalog_image_link1.png %})

Así es como se ve cuando se renderiza el Liquid:

![Ejemplo de tarjeta de contenido con las etiquetas de Liquid del catálogo renderizadas.]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

{% alert important %}
En canales **HTML** como el correo electrónico, evita espacios adicionales o saltos de línea entre la etiqueta de cierre `{% raw %}{% catalog_items ... %}{% endraw %}` y el Liquid que imprime la URL de la imagen (por ejemplo, `{% raw %}{{ items[0].image_link }}{% endraw %}`). Los espacios en blanco adicionales en la plantilla pueden impedir que la URL de la imagen se resuelva correctamente en el mensaje renderizado. Mantén la expresión de la URL inmediatamente adyacente a la etiqueta del catálogo, como en: `{% raw %}<img src="{% catalog_items Games 1234 %}{{ items[0].image_link }}">{% endraw %}`.
{% endalert %}

### Plantillas de elementos del catálogo

También puedes usar plantillas para obtener dinámicamente elementos del catálogo basándote en atributos personalizados. Por ejemplo, supongamos que un usuario tiene el atributo personalizado `wishlist`, que contiene un array de IDs de juegos de tu catálogo.

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
Los objetos JSON en catálogos solo se ingieren a través de la API. No puedes cargar un objeto JSON usando un archivo CSV.
{% endalert %}

Usando plantillas de Liquid, puedes obtener dinámicamente los IDs de la lista de deseos y luego usarlos en tu mensaje. Para hacerlo, [asigna una variable]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/dashboard_tools#assign-variables) a tu atributo personalizado, luego usa el modal **Añadir personalización** para obtener un elemento específico del array. Las variables referenciadas como el ID del elemento del catálogo deben estar envueltas en llaves para ser referenciadas correctamente, como `{{result}}`.

{% alert tip %}
Recuerda, los arrays comienzan en `0`, no en `1`.
{% endalert %}

Por ejemplo, para informar a un usuario que Tales (un elemento en nuestro catálogo que ha deseado) está en oferta, podemos agregar lo siguiente a nuestro creador de mensajes:

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now for {{ items[0].price }}!
```
{% endraw %}

Lo cual se mostrará de la siguiente manera:
> Get Tales now for just 7.49!

Con las plantillas, puedes renderizar un elemento del catálogo diferente para cada usuario basándote en sus atributos personalizados individuales, propiedades del evento o cualquier otro campo que admita plantillas.

### Carga de un CSV

Puedes cargar un CSV con nuevos elementos del catálogo para agregar o elementos del catálogo para actualizar. Para eliminar una lista de elementos, puedes cargar un CSV con los IDs de los elementos para eliminarlos.

### Uso de Liquid

También puedes armar manualmente catálogos con lógica de Liquid. Sin embargo, ten en cuenta que si escribes un ID que no existe, Braze seguirá devolviendo un array de elementos sin objetos. Recomendamos que incluyas manejo de errores, como verificar el tamaño del array y usar una sentencia `if` para contemplar un caso de array vacío.

#### Plantillas de elementos del catálogo que incluyen Liquid

De manera similar al [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), debes usar el indicador `:rerender` en una etiqueta de Liquid para renderizar el contenido de Liquid de un elemento del catálogo. Ten en cuenta que el indicador `:rerender` tiene solo un nivel de profundidad, lo que significa que no se aplicará a ninguna llamada de etiqueta de Liquid anidada.

Si un elemento del catálogo contiene campos del perfil de usuario (dentro de una etiqueta de personalización de Liquid), estos valores deben definirse en Liquid antes en el mensaje y antes de la plantilla para renderizar el Liquid correctamente. Si no se proporciona el indicador `:rerender`, se renderizará el contenido de Liquid sin procesar.

Por ejemplo, si un catálogo llamado "Messages" tiene un elemento con este Liquid:

![Fila de tabla del catálogo con id greet_msg y columna Welcome_Message que contiene un saludo de bienvenida a la tienda con una variable de Liquid de nombre.]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

Para renderizar el siguiente contenido de Liquid:

{% raw %}
```liquid
Hi ${first_name},

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

Esto se mostrará de la siguiente manera:

{% raw %}
```
Hi Peter,

Welcome to our store, Peter!
```
{% endraw %}

{% alert note %}
Las etiquetas de Liquid del catálogo no se pueden usar de forma recursiva dentro de los catálogos.
{% endalert %}

## Solución de problemas de personalización de catálogos

Si el Liquid de catálogo o selección no se muestra como esperas en un mensaje o paso en Canvas, comprueba lo siguiente:

| Síntoma | Qué comprobar |
| --- | --- |
| La vista previa muestra elementos, pero los envíos en vivo están vacíos | Confirma que los **ID de elementos** del catálogo existen en el momento del envío. Si el ID en tu Liquid no coincide con una fila, Braze devuelve un array de elementos vacío; consulta [Uso de Liquid](#using-liquid). Comprueba si hay errores tipográficos y si las fuentes de ID (como las propiedades del evento) faltan en el desencadenador o el perfil de usuario. |
| La vista previa del creador funciona en una Campaign pero no en Canvas | Confirma que estás usando el contexto de Liquid correcto—**propiedades de contexto de Canvas** frente a **propiedades del evento**—y que esos campos existen en el desencadenador. Consulta [Propiedades de contexto y de evento]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties). |
| Una selección no devuelve elementos | Revisa los [filtros de selección]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) y los límites; confirma que los datos del catálogo están sincronizados y que los nombres de columna coinciden con tus filtros. |
| `:rerender` o la entrega con plantillas se ve incorrecta | Para Liquid anidado dentro de campos de catálogo, necesitas `:rerender` y un orden correcto de variables; consulta [Uso de plantillas en elementos de catálogo que incluyen Liquid](#templating-catalog-items-including-liquid). Los mensajes dentro de la aplicación con plantillas se resuelven en el momento del desencadenamiento; consulta [¿Qué son los mensajes dentro de la aplicación con plantillas?]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages). Algunos canales restringen las etiquetas de catálogo (por ejemplo, ciertos usos de **:rerender** con Banners); consulta [¿Se admiten todas las etiquetas de Liquid?]({{site.baseurl}}/user_guide/channels/banners/faq#are-all-liquid-tags-supported) en las preguntas frecuentes de Banners. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas de personalización de catálogos" }

Para el comportamiento general de Liquid, consulta [Ejemplos de uso de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases) y [Uso de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid).

## Estructurar los datos de tu catálogo

Al planificar cómo estructurar los datos de tu catálogo, parte de tu caso de uso previsto y diseña el catálogo en torno a él. Cada fila del catálogo representa un elemento (con un `id` único). Las columnas deben contener los atributos de ese elemento, como URL, texto descriptivo, URL de imágenes, precio, valoración, talla o color.

### Cuándo usar llamadas estándar de catálogo

Con las llamadas estándar de catálogo, haces coincidir un valor con la columna `id`. Al insertar un atributo personalizado o una propiedad del evento (como una cadena de ID) en la etiqueta de Liquid del catálogo, puedes extraer múltiples atributos de un solo elemento en tu mensaje. Los casos de uso más comunes incluyen:

- Producto o servicio visto recientemente
- Elementos de la lista de deseos
- Ofertas por ubicación
- Producto comprado
- Contenido de etapa del ciclo de vida
- Producto o servicio buscado más recientemente

### Cuándo usar selecciones de catálogo

Las [selecciones de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) te permiten filtrar en cualquier columna de tu catálogo y devolver hasta 50 elementos coincidentes. Al insertar atributos personalizados o propiedades del evento en los filtros de selección, los resultados se personalizan para cada usuario. Los casos de uso más comunes incluyen:

- Elementos en los que la categoría coincide con la preferencia de un usuario
- Elementos que coinciden con la marca, cocina o talla preferida de un usuario
- Contenido de tipo de suscripción o nivel de fidelización
- Productos dentro del rango de valor medio de pedido de un usuario

La diferencia clave es que las llamadas estándar de catálogo buscan un solo elemento conocido por `id`, mientras que las selecciones de catálogo consultan a lo largo del catálogo y devuelven múltiples elementos que coinciden con tus criterios de filtro.

[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}