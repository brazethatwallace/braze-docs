---
nav_title: Recomendaciones basadas en reglas
article_title: Crear recomendaciones de elementos basadas en reglas
description: "Este artículo de referencia explica cómo crear una recomendación de elementos basada en reglas para los elementos de un catálogo."
page_order: 2
---

# Crear recomendaciones de elementos basadas en reglas {#create-rules-based-item-recommendations}

> Aprende a crear una herramienta de recomendaciones basada en reglas a partir de los elementos de tu catálogo.

## Acerca de las recomendaciones de elementos basadas en reglas {#about-rules-based-item-recommendations}

Una herramienta de recomendaciones basada en reglas utiliza datos de usuario e información sobre productos para sugerir elementos relevantes a los usuarios dentro de los mensajes. Utiliza [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) y los [catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs) de Braze o [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) para personalizar dinámicamente el contenido en función del comportamiento y los atributos de los usuarios.

{% alert important %}
Las recomendaciones basadas en reglas se basan en una lógica fija que debes establecer manualmente. Esto significa que tus recomendaciones no se ajustarán al historial de compras y gustos de un usuario a menos que actualices la lógica.<br><br>Para crear recomendaciones de IA personalizadas que se ajusten automáticamente al historial del usuario, consulta [Recomendaciones de elementos de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai).
{% endalert %}

## Opciones de la herramienta de recomendaciones {#recommendation-engine-options}

Cuando decidas qué herramienta de recomendaciones se adapta a tus recursos disponibles y a tus casos de uso, consulta esta tabla de consideraciones:

<table aria-label="Opciones de la herramienta de recomendaciones" style="text-align: center;">
  <caption>Opciones de la herramienta de recomendaciones</caption>
  <thead>
    <tr>
      <th>Herramienta de recomendaciones</th>
      <th>Sin puntos de datos registrados</th>
      <th>Solución sin código</th>
      <th>Sin Liquid avanzado</th>
      <th>Actualiza automáticamente la fuente de productos</th>
      <th>Generado con la interfaz de Braze</th>
      <th>Sin alojamiento de datos ni solución de problemas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Catálogos CSV</strong></td>
      <td>&#10004;</td>
      <td>Sí, si usas Liquid pregenerado.</td>
      <td>&#10004;</td>
      <td>Sí, si las recomendaciones <strong>no</strong> se actualizan con frecuencia.</td>
      <td>&#10004;</td>
      <td>&#10004;</td>
    </tr>
    <tr>
      <td><strong>API de catálogos</strong></td>
      <td>&#10004;</td>
      <td></td>
      <td>&#10004;</td>
      <td>Sí, si las recomendaciones se actualizan cada hora.</td>
      <td>&#10004;</td>
      <td>&#10004;</td>
    </tr>
    <tr>
      <td><strong>Contenido conectado</strong></td>
      <td>&#10004;</td>
      <td></td>
      <td></td>
      <td>&#10004;<br>(Recomendaciones actualizadas en tiempo real)</td>
      <td>Sí, si se genera fuera de Braze.</td>
      <td></td>
    </tr>
    <tr>
      <td><strong>Liquid</strong></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>&#10004;</td>
      <td>&#10004;</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="Opciones de la herramienta de recomendaciones" }

## Creación de una herramienta de recomendaciones {#creating-a-recommendation-engine}

Crea tu herramienta de recomendaciones utilizando un catálogo o contenido conectado:

{% tabs local %}
{% tab using a catalog %}
Para crear tu herramienta de recomendaciones utilizando un catálogo:

1. [Crea un catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create) de productos.
2. Para cada producto, añade una lista de productos recomendados como una cadena separada por un delimitador (como una barra vertical `|`) en una columna llamada "product_recommendations".
3. Pasa al catálogo el ID del producto para el que quieres encontrar recomendaciones.
4. Obtén el valor `product_recommendations` de ese elemento del catálogo y divídelo por el delimitador con un filtro de división Liquid.
5. Vuelve a pasar uno o varios de esos ID al catálogo para recoger los demás detalles del producto.

### Ejemplo {#example}

Supongamos que tienes una aplicación de comida saludable y quieres crear una campaña de tarjeta de contenido que envíe recetas diferentes en función del tiempo que un usuario lleva registrado en tu aplicación. En primer lugar, crea y sube un catálogo mediante un archivo CSV que incluya la siguiente información:

| Campo | Descripción |
|-----|-----------|
| **id** | Un número único que se correlaciona con el número de días transcurridos desde que el usuario se registró en tu aplicación. Por ejemplo, `3` se correlaciona con tres días. |
| **type** | La categoría de la receta, como `comfort`, `fresh` y otras. |
| **title** | El título de la tarjeta de contenido que se enviará para cada ID, como "Prepárate para comer esta semana" o "Hablemos de tacos". |
| **link** | El enlace al artículo de la receta. |
| **image_url** | La imagen que corresponde a la receta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ejemplo" }

Una vez cargado el catálogo en Braze, confirma que la información se importó correctamente seleccionando tu catálogo en la página de catálogos y abriendo la pestaña **Preview**. Aparecerá un número selecto de elementos en la vista previa, y pueden estar en orden aleatorio, pero esto no afecta al resultado de la herramienta de recomendaciones.

Con el catálogo listo, [crea una campaña de tarjeta de contenido]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card). En el creador, introduce la lógica Liquid para determinar qué usuarios deben recibir la campaña, y qué receta e imagen deben mostrarse. En este caso de uso, Braze obtiene el `start_date` (o fecha de registro) del usuario y lo compara con la fecha actual. La diferencia en días determina qué tarjeta de contenido se envía.

{% subtabs local %}
{% subtab title %}
{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].title }}
```
{% endraw %}
{% endsubtab %}

{% subtab message %}
{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{% if items[0].title != blank %}
{{ items[0].body }}
{% else %}
{% abort_message('no card for today') %}
{% endif %}
```
{% endraw %}
{% endsubtab %}

{% subtab image %}
{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].image_url }}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}

Por ejemplo:

![Ejemplo de creador de mensajes de una campaña de tarjeta de contenido.]({% image_buster /assets/img/recs/content_card_preview.png %})

En la sección **On click behavior**, introduce la lógica Liquid para saber a dónde deben ser redirigidos los usuarios cuando hacen clic en la tarjeta de contenido en dispositivos iOS, Android y Web.

{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].link }}
```
{% endraw %}

Por ejemplo:

![Ejemplo de bloque de comportamiento al hacer clic en el creador de mensajes.]({% image_buster /assets/img/recs/on_click_behavior.png %}){: style="max-width:60%;"}<br><br>

Ve a la pestaña **Test** y selecciona **Custom user** en **Preview message as user**. Introduce una fecha en el campo **Custom attribute** para obtener una vista previa de la tarjeta de contenido que se enviaría a un usuario que se hubiera registrado en esa fecha. <br><br>

![Ejemplo de atributo personalizado denominado "start_date".]({% image_buster /assets/img/recs/custom_attributes_test.png %})
{% endtab %}

{% tab using Connected Content %}
Para crear tu herramienta de recomendaciones utilizando contenido conectado, primero crea un nuevo endpoint utilizando uno de los siguientes métodos:

| Opción | Descripción |
|------|-----------|
| **Convertir una hoja de cálculo** | Convierte una hoja de cálculo en un endpoint de API JSON utilizando un servicio como SheetDP y toma nota de la URL de la API que se genera. |
| **Crear un endpoint personalizado** | Crea, aloja y mantén un endpoint interno personalizado. |
| **Utilizar una herramienta de terceros** | Utiliza una herramienta de recomendaciones de terceros, como uno de nuestros [partners de Alloy]({{site.baseurl}}/partners/message_personalization), entre los que se incluyen [Amazon Personalise]({{site.baseurl}}/partners/amazon_personalize), [Certona]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalized_recommendations/certona), [Dynamic Yield]({{site.baseurl}}/partners/dynamic_yield) y otros. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ejemplo" }

A continuación, utiliza Liquid en tu mensaje que llame a tu endpoint para hacer coincidir un valor de atributo personalizado con el perfil de un usuario y extraer la recomendación correspondiente.

{% raw %}
```liquid
{% connected_content YOUR_API_URL :save items %}

{% assign recommended_item_ids_from_user_profile = custom_attribute.${RECOMMENDED_ITEM_IDS} | split: ';' %}

{% for item_id in recommended_item_ids_from_user_profile %}
  {% assign recommended_item = items | where: "ITEM_ID", ITEM_ID | first %}
  recommended_item.item_name
{% endfor %}
```
{% endraw %}

Sustituye lo siguiente:

| Atributo | Sustitución |
| --- | --- |
| `YOUR_API_URL` | Sustitúyelo por la URL real de tu API. |
| `RECOMMENDED_ITEM_IDS` | Sustitúyelo por el nombre real de tu atributo personalizado que contiene los ID de los elementos recomendados. Se espera que este atributo sea una cadena de ID separados por punto y coma. |
| `ITEM_ID` | Sustitúyelo por el nombre real del atributo en la respuesta de tu API que corresponde al ID del elemento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ejemplo" }

{% alert note %}
Este es un ejemplo básico y puede que tengas que modificarlo en función de tus necesidades específicas y de la estructura de tus datos. Para obtener información más detallada, consulta la [documentación de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) o consulta con un desarrollador.
{% endalert %}

### Ejemplo

Supongamos que quieres extraer recomendaciones de restaurantes de la base de datos Zomato Restaurants y guardar el resultado como una variable local llamada `restaurants`. Puedes hacer la siguiente llamada de contenido conectado:

{% raw %}
```liquid

{% connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

A continuación, supongamos que quieres obtener recomendaciones de restaurantes en función de la ciudad y el tipo de comida de un usuario. Puedes hacerlo insertando dinámicamente los atributos personalizados para la ciudad y el tipo de comida del usuario al principio de la llamada, y asignando después el valor de `restaurants` a la variable `city_food.restaurants`.

La llamada de contenido conectado tendría el siguiente aspecto:

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

Si quieres adaptar la respuesta para recuperar solo el nombre y la valoración del restaurante, puedes añadir filtros al final de la llamada, de esta forma:

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0].restaurant.name}}
{{city_food.restaurants[0].restaurant.user_rating.rating_text}}
```
{% endraw %}

Por último, supongamos que quieres agrupar las recomendaciones de restaurantes por valoración. Haz lo siguiente:

1. Utiliza `assign` para crear matrices en blanco para las categorías de valoración "excellent", "very good" y "good".
2. Añade un bucle `for` que examine la valoración de cada restaurante de la lista.
- Si la valoración es "Excellent", añade el nombre del restaurante a la cadena `excellent_restaurants` y, a continuación, añade un carácter * al final para separar cada nombre de restaurante.
- Si la valoración es "Very Good", añade el nombre del restaurante a la cadena `very_good_restaurants` y, a continuación, añade un carácter * al final.
- Si la valoración es "Good", añade el nombre del restaurante a la cadena `good_restaurants` y, a continuación, añade un carácter * al final.
3. Limita el número de recomendaciones de restaurantes devueltas a cuatro por categoría.

Así sería la llamada final:

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}
{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}
{% assign excellent_restaurants = “” %}
{% assign very_good_resturants = “” %}
{% assign good_restaurants = “” %}
{% for list in restaurants %}
{% if {{list.restaurant.user_rating.rating_text}} == `Excellent` %}
{% assign excellent_restaurants = excellent_restaurants | append: list.restaurant.name | append: `*` %}
{% elsif {{list.restaurant.user_rating.rating_text}} == `Very Good` %}
{% assign very_good_restaurants = very_good_restaurants | append: list.restaurant.name | append: `*` %}
{% elsif {{list.restaurant.user_rating.rating_text}} == `Good` %}
{% assign good_restaurants = good_restaurants | append: list.restaurant.name | append: `*` %}
{% endif %}
{% endfor %}
{% assign excellent_array = excellent_restaurants | split: `*` %}
{% assign very_good_array = very_good_restaurants | split: `*` %}
{% assign good_array = good_restaurants | split: `*` %}

Excellent places
{% for list in excellent_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

Very good places
{% for list in very_good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

Good places
{% for list in good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}
```
{% endraw %}

Mira la siguiente captura de pantalla para ver un ejemplo de cómo se muestra la respuesta en el dispositivo de un usuario.

![Representación de una lista de restaurantes generada por la llamada final del ejemplo.]({% image_buster /assets/img/recs/sample_response.png %}){: style="max-width:30%;"}
{% endtab %}
{% endtabs %}