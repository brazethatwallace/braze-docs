---
nav_title: De vuelta en stock
article_title: De vuelta en stock
page_order: 2
page_type: reference
description: "Este artículo describe cómo utilizar una plantilla de Braze Canvas para impulsar las compras notificando a tus usuarios cuando un artículo vuelve a estar en stock con mensajería personalizada."
tool: Canvas
---

# De vuelta en stock {#back-in-stock}

> Utiliza la plantilla de vuelta en stock para crear mensajes dirigidos a usuarios que previamente han visto o expresado interés en un artículo que estaba agotado pero que ahora está disponible para su compra. Esto ayuda a los usuarios a obtener los productos que desean al interactuar con ellos en el momento crítico en que un producto vuelve a estar disponible.

Este artículo te guiará a través de un caso de uso de la plantilla **De vuelta en stock**, que está diseñada para la etapa de conversión del ciclo de vida del usuario. Cuando termines, habrás creado un Canvas que envía una notificación push (web o móvil), SMS o correo electrónico a los usuarios cuando un artículo vuelve a estar en stock, y hasta dos recordatorios.

## Requisitos previos {#prerequisites}

Para utilizar esta plantilla con éxito, necesitarás lo siguiente:

- Un [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create/) que contenga información sobre tu artículo
- Las [notificaciones de vuelta en stock]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/#how-back-in-stock-notifications-work) deben estar configuradas para el artículo sobre el que deseas enviar mensajes a los usuarios

## Adaptar la plantilla a tus necesidades {#tailoring-the-template-to-your-needs}

Supongamos que trabajamos para PantsLabyrinth, un minorista de ropa directo al consumidor que se especializa en pantalones de vestir, jeans, culottes y muchos otros tipos de pantalones. Podemos usar la plantilla de vuelta en stock para notificar a los clientes en varios canales cuando unos jeans populares, los Classic Straight Leg, vuelven a estar en stock.

Antes de crear el Canvas, [configuramos un catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create/) que contiene información sobre nuestro inventario de pantalones de pierna recta y [configuramos las notificaciones de vuelta en stock]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/#setting-up-back-in-stock-notifications) para los jeans Classic Straight Leg. Lo configuramos para que los usuarios se suscriban a las notificaciones después de realizar el evento personalizado de marcar como favoritos los jeans Classic Straight Leg en la aplicación.

Para acceder a la plantilla de vuelta en stock, al crear un nuevo Canvas, selecciona **Use a Canvas template** > **Braze templates**. Luego, junto a **Back in Stock**, selecciona **Apply Template**. Ahora podemos recorrer la plantilla para adaptarla a nuestras necesidades.

### Paso 1: Configurar los detalles {#step-1-set-up-the-details}

Ajustemos los detalles del Canvas para reflejar nuestro objetivo.

1. Selecciona **Edit** junto al nombre de la plantilla.

![El título y la descripción actuales del Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2. Actualiza el nombre del Canvas para especificar que el Canvas está dirigido a usuarios cuando nuestro producto Classic Straight Leg vuelve a estar en stock.
3. Actualiza la descripción para explicar que este Canvas contiene mensajería personalizada.
4. Añade la etiqueta **Back in Stock**, que está anidada bajo la etiqueta **Promotional**, para que podamos filtrar por ella en la página de inicio de Canvas.

![Paso "Set Up Canvas Details" con un nombre de Canvas "Back in Stock - Classic Straight Leg" y una breve descripción del Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_1.png %})

### Paso 2: Asignar eventos de conversión {#step-2-assign-conversion-events}

Cambia el **Primary Conversion Event - A** a **Make a specific purchase** y selecciona **Classic Straight Leg** como nombre del producto.

![Sección "Assign Conversion Events" para el tipo de evento de conversión de compra del producto Classic Straight Leg con un plazo de conversión de 7 días.]({% image_buster /assets/img/canvas_templates/back_in_stock_2.png %})

### Paso 3: Adaptar el horario de entrada {#step-3-tailor-the-entry-schedule}

Mantengamos el horario de entrada como **Action-Based** para que los usuarios entren en nuestro Canvas cuando realicen una acción, que la plantilla ya tiene configurada como **Perform a Back in Stock Event**.

Haremos dos ajustes en este paso:

1. Selecciona el catálogo que incluye información sobre nuestros jeans Classic Straight Leg, que hemos llamado "Straight Leg Pants".

![Paso "Entry Schedule" para un Canvas basado en acciones.]({% image_buster /assets/img/canvas_templates/back_in_stock_3.png %})

{: start="2"}
2. Establece la **Start Time (Required)** en la fecha y hora de inicio deseadas.

![Sección "Entry Window" con una hora de inicio del 2 de enero de 2025 a las 12 am.]({% image_buster /assets/img/canvas_templates/back_in_stock_4.png %})

### Paso 4: Seleccionar la audiencia objetivo {#step-4-select-the-target-audience}

Definiremos nuestra audiencia objetivo como los usuarios que creemos que tienen más probabilidades de comprar los jeans Classic Straight Leg.

1. Selecciona nuestro segmento objetivo, "Favorited - Classic Straight Leg Jeans", que consiste en usuarios que han marcado como favoritos nuestros jeans Classic Straight Leg en nuestra aplicación o sitio web.
2. Selecciona un filtro para incluir usuarios que hayan comprado "Jeans" más de "0" veces.

![Paso "Target Audience" con el segmento "Favorited - Classic Straight Leg Jeans".]({% image_buster /assets/img/canvas_templates/back_in_stock_5.png %})

{: start="3"}
3. Ajusta los controles de entrada para permitir que los usuarios vuelvan a entrar en el Canvas después de la duración máxima del Canvas, para reducir la probabilidad de que los usuarios activen el mismo paso de forma concurrente.

![Sección "Entry Controls" con una casilla de verificación para permitir que los usuarios vuelvan a entrar en este Canvas con una duración máxima del Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_6.png %})

{: start="4"}
4. Ajusta los criterios de salida para eliminar a los usuarios que realizaron el evento personalizado de quitar de favoritos los jeans Classic Straight Leg.

![Sección "Exit Criteria" con una excepción para usuarios que realizan el evento personalizado de "Unfavorited".]({% image_buster /assets/img/canvas_templates/back_in_stock_7.png %})

### Paso 5: Seleccionar los ajustes de envío {#step-5-select-your-send-settings}

Mantendremos la configuración de suscripción predeterminada, de modo que solo enviemos a usuarios que se hayan suscrito u optado por recibir mensajes o notificaciones, y omitiremos las demás configuraciones (limitación de frecuencia, horas tranquilas y grupos semilla).

![Paso "Send Settings" dirigido a usuarios que están suscritos u optados.]({% image_buster /assets/img/canvas_templates/back_in_stock_8.png %})

### Paso 6: Personalizar tu Canvas {#step-6-customize-your-canvas}

Ahora construiremos nuestro Canvas personalizando los canales y el contenido que se enviará a los usuarios. Como estamos usando los cuatro canales de la plantilla (push móvil y web, SMS y correo electrónico) y usando el filtro de [canal inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/), no necesitamos añadir ni quitar ninguno.

{% alert tip %}
Puedes usar las [propiedades de entrada de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/) para personalizar los mensajes en tu Canvas según el producto al que te refieras.
{% endalert %}

Comenzaremos nuestra personalización recorriendo cada paso de mensaje para actualizar el contenido.

1. Reemplaza `!!YOURCATALOGHERE!!` con el nombre de nuestro catálogo ("Straight_Leg_Pants").
2. Reemplaza `[0]` con el número de índice de los jeans Classic Straight Leg, que es "9" porque los jeans son el décimo artículo en el array `items` de nuestro catálogo. (Los arrays tienen índice cero en Liquid, por lo que el primer artículo es `0` y no `1`.)
3. Repite los pasos 1 y 2 para todos los pasos de mensaje restantes, incluyendo:
    - El mensaje "In-Product Msg & Email" que se envía después del retraso de un día
    - Los mensajes "Push+Email Alert" que se envían a los usuarios que no han realizado una compra
4. Actualiza el paso de rutas de acción seleccionando el grupo de acción **Purchase**. Luego, selecciona **Make a specific purchase** y elige los jeans Classic Straight Leg como producto.

![Paso de Canvas de push móvil con un mensaje notificando a los usuarios que un producto vuelve a estar en stock.]({% image_buster /assets/img/canvas_templates/back_in_stock_9.png %})

### Paso 7: Probar y lanzar tu Canvas {#step-7-test-and-launch-your-canvas}

Después de probar y revisar nuestro Canvas para asegurarnos de que funciona como se espera, lo lanzaremos seleccionando **Launch Canvas**. ¡Ahora nuestros usuarios que han marcado como favoritos nuestros jeans Classic Straight Leg y se han suscrito a nuestros canales de mensajería recibirán notificaciones cuando vuelvan a estar en stock!

{% alert tip %}
Consulta nuestra [lista de verificación previa y posterior al lanzamiento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para conocer las cosas a considerar antes y después de lanzar un Canvas.
{% endalert %}