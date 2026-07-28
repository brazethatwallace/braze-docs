---
nav_title: Catálogos
article_title: Catálogos
page_order: 3
layout: dev_guide

guide_top_header: "Catálogos"
guide_top_text: "Los catálogos acceden a datos de archivos CSV importados y endpoints de API para enriquecer tus mensajes, de forma similar a como accederías a atributos personalizados o propiedades de eventos personalizados a través de Liquid."

description: "Esta página de inicio alberga catálogos. Utiliza catálogos y conjuntos filtrados para aprovechar datos que no son de usuario en tus campañas de Braze y enviar mensajes personalizados."

guide_featured_title: "Artículos de la sección"
guide_featured_list:
- name: Crear un catálogo
  link: /docs/user_guide/data/activation/catalogs/create
  image: /assets/img/braze_icons/users-01.svg
- name: Uso de catálogos
  link: /docs/user_guide/data/activation/catalogs/use
  image: /assets/img/braze_icons/users-01.svg
- name: Notificaciones de reposición de existencias
  link: /docs/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Notificaciones de bajada de precio
  link: /docs/price_drop_notifications
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Selecciones
  link: /docs/user_guide/data/activation/catalogs/selections
  image: /assets/img/braze_icons/list.svg

guide_menu_title: "Otros artículos"
guide_menu_list:
- name: Endpoints de la API de catálogos
  link: /docs/api/endpoints/catalogs
  image: /assets/img/braze_icons/server-01.svg
- name: Bloques de producto de arrastrar y soltar
  link: /docs/dnd_product_blocks
  image: /assets/img/braze_icons/columns-01.svg
---
<br><br>

## Casos de uso de catálogos {#catalog-use-cases}

Puedes incorporar cualquier tipo de datos en un catálogo. Normalmente, los datos son metadatos sobre ofertas, como productos, descuentos, promociones, eventos y similares. Consulta los siguientes casos de uso para ver algunos ejemplos de cómo puedes utilizar estos datos para dirigirte a los usuarios con mensajería altamente relevante.

### Comercio minorista y comercio electrónico {#retail-and-ecommerce}

- **Promociones de temporada:** importa colecciones de productos de temporada y personaliza los mensajes para reflejar las tendencias actuales.
- **Mensajes localizados:** importa las direcciones, horarios y servicios de tus ubicaciones físicas y, a continuación, personaliza las notificaciones en función de la ubicación de los usuarios.
- **Notificaciones de reposición de existencias:** importa información de productos que incluya la cantidad de inventario y, a continuación, utiliza las [notificaciones de reposición de existencias]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) y los eventos personalizados de Braze para desencadenar una Campaign o un Canvas que envíe a los usuarios una notificación de que un producto ya está disponible.
- **Notificaciones de bajada de precio:** importa información de productos que incluya los precios y, a continuación, utiliza las [notificaciones de bajada de precio]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications) y los eventos personalizados de Braze para desencadenar un Canvas que envíe a los usuarios una notificación de que el precio de un producto ha bajado.

### Entretenimiento {#entertainment}

- **Planes de suscripción:** importa planes de suscripción y promociona complementos a tus usuarios en función de sus patrones de uso y los tipos de contenido que consumen con más frecuencia.
- **Próximos eventos:** importa listados de próximos eventos con sus ubicaciones y edades de la audiencia, y envía notificaciones personalizadas a los usuarios que se encuentren en la zona y tengan las edades objetivo.
- **Preferencias multimedia:** importa información sobre películas y series, y recomienda contenido a tus usuarios en función de sus títulos favoritos y los géneros más vistos.

### Viajes y hostelería {#travel-and-hospitality}

- **Destinos:** importa destinos de viaje y sus atracciones, restaurantes y actividades más populares, y personaliza las recomendaciones a tus usuarios en función de sus viajes anteriores.
- **Alojamiento:** importa establecimientos hoteleros y sus servicios, tipos de habitación y precios, y envía promociones a tus usuarios en función de las preferencias que hayan seleccionado.
- **Métodos de viaje:** importa ofertas y promociones para modalidades de viaje (como vuelos, trenes, coches de alquiler y otros) y envíalas a tus usuarios en función de su historial de búsqueda reciente.
- **Preferencias alimentarias:** importa información sobre la oferta de comidas y utiliza las [selecciones]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) para enviar mensajes personalizados a los usuarios que tengan preferencias de comida específicas en función de la categoría de comida que hayan consultado más recientemente.

## Cómo funcionan juntos los catálogos y Liquid {#how-catalogs-and-liquid-work-together}

Los catálogos son una característica de almacenamiento de datos. Contienen grandes conjuntos de datos a los que puedes hacer referencia en tus mensajes para personalización. Para hacer referencia a los datos, utilizarás [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) como lenguaje de plantillas. En otras palabras, los catálogos son el almacenamiento donde se guardan los datos, y Liquid es el lenguaje que extrae los datos relevantes del almacenamiento.

Para ver ejemplos de cómo puedes usar Liquid para extraer información de catálogos, consulta los casos de uso adicionales en [Crear un catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create#use-cases).

## Limitaciones de almacenamiento de datos {#data-storage-limitations}

El almacenamiento de datos para catálogos está limitado en función del tamaño de los elementos del catálogo, que puede ser diferente de los tamaños de los archivos CSV cargados.

Para la versión gratuita de catálogos, la cantidad de almacenamiento permitida es de hasta 500&nbsp;MB. Puedes tener elementos ilimitados siempre que el espacio de almacenamiento no supere los 500&nbsp;MB.

Para Catalogs Pro, las opciones de tamaño de almacenamiento son: 5&nbsp;GB, 10&nbsp;GB, 15&nbsp;GB o 50&nbsp;GB. Ten en cuenta que el almacenamiento de la versión gratuita (500&nbsp;MB) está incluido en cada uno de estos planes.

Si necesitas ampliar el almacenamiento de tu catálogo, ponte en contacto con tu director de cuentas de Braze. Para obtener detalles del plan y notas sobre derechos, consulta [Almacenamiento de catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/create#tiers).