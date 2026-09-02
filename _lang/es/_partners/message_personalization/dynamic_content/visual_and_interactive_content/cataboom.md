---
nav_title: CataBoom
article_title: CataBoom
description: "Aprende a conectar las experiencias gamificadas de CataBoom con Braze usando Catapult, Request Unique URLs y contenido conectado."
alias: /partners/cataboom/
page_type: partner
search_tag: Partner
---

# CataBoom

> [CataBoom](https://www.cataboom.com/) es una plataforma de gamificación. Las marcas la utilizan para crear y lanzar experiencias digitales interactivas, como juegos de girar y ganar, cuestionarios y juegos de premio instantáneo. Estas experiencias profundizan la participación y recopilan datos propios.

*Esta integración es mantenida por CataBoom.*

## Acerca de esta integración {#about-this-integration}

Usa la integración de Braze y CataBoom para agregar enlaces de juegos personalizados a tus mensajes. Puedes pasar identificadores de usuario y atributos entre Campaigns de Catapult y Braze en tiempo real. Luego puedes impulsar Campaigns personalizadas, desencadenadores y recorridos de seguimiento con esos datos.

## Requisitos previos {#prerequisites}

Antes de empezar, necesitas lo siguiente:

| Requisito previo | Descripción |
| --- | --- |
| Cuenta de Catapult | Se requiere una cuenta de Catapult para usar esta integración. |
| Clave de API REST de Braze (opcional) | Si usas webhooks de Catapult, necesitas una clave de API REST de Braze con los permisos de datos de usuario que requiera tu caso de uso. Crea la clave en Braze en **Configuración** > **APIs e identificadores** > **Claves de API**. |
| Endpoint REST de Braze (opcional) | Si usas webhooks de Catapult, utiliza la URL del endpoint REST que coincida con la URL de Braze para [tu instancia de Braze]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Paso 1: Crea tu experiencia de juego {#step-1-create-your-game-experience}

Crea tu experiencia de juego en la plataforma Catapult. Los siguientes pasos muestran una configuración simple de ruleta que utiliza la API Request Unique URL en la página **Link Configuration**. CataBoom ofrece más de 200 opciones de juego, incluyendo mecánicas basadas en azar, mecánicas basadas en habilidad y utilidades como tarjetas de sellos y colecciona-y-gana. Puedes seguir un flujo similar para otros tipos de juego. Para más información sobre CataBoom y Catapult, consulta [el sitio web de CataBoom](https://www.cataboom.com).

1. Crea la campaña.

Selecciona **New Campaign** en el área de navegación superior. Introduce un nombre de campaña, elige un slug de URL y selecciona la categoría y el tipo de juego.

![Formulario New Campaign del panel de CataBoom con campos de nombre de campaña, URL, categoría de juego y tipo de juego.]({% image_buster /assets/img/cataboom/new_campaign.png %})

{: start="2"}
2. Habilita la API Request Unique URL.

En el menú de navegación, selecciona **Link Configuration**.

En la página **Link Configuration**, habilita **Request Unique URL API**. Esta opción crea una URL de sistema a sistema que puedes usar posteriormente en Braze, por ejemplo, en una tarjeta de contenido.

![Página Link Configuration de CataBoom con la API Request Unique URL habilitada y la URL de la API visible.]({% image_buster /assets/img/cataboom/link_configuration.png %})

{: start="3"}
3. Configura el seguimiento de jugadas con Account ID.

En el menú de navegación, selecciona **Play Control**.

En la página **Play Control**, en **Play Tracking**, establece **Play Count Tracked By** en **Account ID Parameter**.

Puedes pasar un Account ID para cada jugador para seguimiento, límites de jugadas, webhooks y otros comportamientos específicos del jugador. Otros sistemas a menudo llaman al Account ID como member ID, player ID, loyalty ID u otro nombre similar.

![Página Play Control de CataBoom con Play Count Tracked By configurado como Account ID Parameter.]({% image_buster /assets/img/cataboom/play_control.png %})

Ahora tienes la configuración suficiente para ejecutar una prueba en Braze. Los pasos opcionales en esta sección completan una configuración de juego completa típica. Catapult también ofrece muchas otras configuraciones que puedes usar para personalizar la experiencia de juego.

{: start="4"}
4. Agrega tus creatividades (opcional).

En el menú de navegación, selecciona **Creative**.

Sube tus activos. Catapult permite un control completo de marca para tu experiencia de juego.

![Página Creative de CataBoom con acciones de descarga y subida de gráficos y una vista previa del juego.]({% image_buster /assets/img/cataboom/creative.png %})

{: start="5"}
5. Configura los premios para juegos basados en azar (opcional).

En el menú de navegación, selecciona **Summary**.

En la página **Summary**, expande **Prize Options**.

Catapult admite premios por tiempo, premios por probabilidad, o ambos. Para configurarlos, usa **Timed Prizes and Codes**, **Prize Control and Odds Setup**, o ambos, según sea necesario.

Las siguientes capturas de pantalla muestran **Prize Options** en el resumen de la campaña y una configuración simple de probabilidades con un 50% de probabilidad de ganar en el nivel 1.

![Página Summary de CataBoom con la sección Prize Options expandida.]({% image_buster /assets/img/cataboom/prize_options_summary.png %})

![Página Odds de CataBoom con niveles de premios, porcentajes y controles de nivel.]({% image_buster /assets/img/cataboom/prize_odds.png %})

## Paso 2: Crea un mensaje en Braze {#step-2-create-a-message-in-braze}

Este ejemplo muestra cómo crear una **tarjeta de contenido** que usa la URL única de solicitud de la página **Link Configuration**.

1. Agrega contenido conectado para la URL de juego.

En tu tarjeta de contenido, agrega el texto y el contenido dinámico que necesites. Envuelve tu URL única de solicitud de CataBoom en una etiqueta de [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content). Agrega un parámetro de consulta `AccountID` que use una etiqueta de personalización de Braze que coincida con el identificador que usas en Catapult. El ejemplo usa {% raw %}`{{${user_id}}}`{% endraw %}.

Reemplaza la URL base y los parámetros de consulta `username` y `password` con los valores de la página **Link Configuration** de tu campaña en Catapult.

{% raw %}
```liquid
{% connected_content https://secure.cataboom.com/dplayurl/YOUR_CAMPAIGN_SLUG?username=YOUR_API_USERNAME&password=YOUR_API_PASSWORD&AccountID={{${user_id}}} :save result %}
```
{% endraw %}

Usa el `result` guardado en tu tarjeta (por ejemplo, como la URL del enlace o en el cuerpo del mensaje). Sigue el formato de respuesta de la API de CataBoom para tu campaña. Para obtener más información sobre parámetros de consulta y Liquid en URLs, consulta [Realizar una llamada a la API]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call).

![Creador de tarjetas de contenido de Braze mostrando contenido conectado en el campo de mensaje y una vista previa móvil de la tarjeta.]({% image_buster /assets/img/cataboom/braze_content_card.png %})

El contenido conectado solicita un enlace de juego único cuando el usuario abre la tarjeta de contenido. Puedes agregar otros parámetros de consulta para experiencias más personalizadas.