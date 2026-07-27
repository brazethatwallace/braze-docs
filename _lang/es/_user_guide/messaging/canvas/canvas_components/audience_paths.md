---
nav_title: Rutas de audiencia
article_title: Rutas de audiencia
alias: /audience_paths/
page_order: 3
page_type: reference
description: "Este artículo de referencia describe cómo usar las Rutas de audiencia en tu Canvas para filtrar y segmentar usuarios de forma intuitiva a gran escala, enviando a cada usuario por la primera rama que coincida."
tool: Canvas

---

# Rutas de audiencia {#audience-paths}

> Las Rutas de audiencia de Canvas te permiten filtrar y segmentar usuarios de forma intuitiva a gran escala, enviando a cada usuario por la primera ruta cuyos criterios cumpla.

Este componente de Canvas reemplaza la necesidad de crear pasos completos excesivos basados en audiencia, permitiéndote combinar lo que podrían haber sido ocho componentes completos en uno solo. Esto te ayuda a simplificar la segmentación de usuarios mientras mantienes tus Canvas libres de desorden y complejidad innecesarios.

## Cómo funciona {#how-it-works}

![Una ruta de audiencia con dos grupos: usuarios comprometidos y todos los demás.]({% image_buster /assets/img/audience_path/audience_path.png %}){: style="float:right;max-width:45%;margin-left:15px;margin-top:15px;"}

Los usuarios avanzan por la primera rama cuyos criterios cumplen, así que coloca la ruta más importante primero. Esto reduce la ambigüedad sobre a dónde van los usuarios y qué mensajes reciben. Ten en cuenta que este orden no es [editable después del lanzamiento]({{site.baseurl}}/post-launch_edits).

Con las Rutas de Audiencia, puedes:

- Enviar a los usuarios por diferentes recorridos de Canvas según criterios de audiencia.
- Colocar tus grupos de audiencia más importantes primero; los usuarios toman la primera ruta para la que califican.
- Segmentar usuarios con precisión a gran escala.
  - Puedes crear hasta ocho grupos de audiencia (dos predeterminados y seis grupos adicionales) por paso de Rutas de Audiencia, pero es posible que quieras conectar varios pasos de Rutas de Audiencia para clasificar aún más a tus usuarios.

Dentro de un solo paso de Rutas de Audiencia, los usuarios se evalúan en función de los grupos de audiencia en orden y avanzan por la primera ruta para la que califican. Si conectas varios pasos de Rutas de Audiencia en un Canvas, los usuarios se evalúan de nuevo cada vez que llegan a un nuevo paso de Rutas de Audiencia.

### Cómo se evalúan los usuarios {#how-users-are-evaluated}

![Canvas que muestra un retraso de 24 horas después de un paso de mensaje, seguido de una ruta de audiencia.]({% image_buster /assets/img/audience_path/audience_path5.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Los usuarios se evalúan en función de filtros y pertenencia a Segments **en el momento en que llegan al paso de ruta de audiencia**, no cuando entraron al Canvas. Después de la evaluación, avanzan inmediatamente a la ruta correspondiente. Cuando un usuario se coloca en un grupo de audiencia, permanece en ese grupo incluso si su perfil de usuario cambia después.

<div style="clear: both;"></div>

{% alert important %}
Las Rutas de Audiencia evalúan en función de los atributos actuales del usuario, filtros y pertenencia a Segments en el momento de la evaluación. No evalúan en función del evento específico que desencadenó la entrada al Canvas. Para dirigir a los usuarios en función de una acción que realizan (como un evento personalizado), usa [Rutas de Acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) en su lugar.
{% endalert %}

### Permitir tiempo para las evaluaciones de usuarios {#allowing-time-for-user-evaluations}

Dado que la evaluación es inmediata, es importante añadir un retraso antes de la ruta de audiencia si los criterios de la ruta dependen de una interacción del usuario con un paso anterior.

Por ejemplo, si a los usuarios se les envía el Mensaje A y el siguiente paso es una ruta de audiencia que evalúa si interactuaron con ese mensaje, todos los usuarios avanzarán al paso para aquellos que no han interactuado con ese mensaje. Esto se debe a que los usuarios avanzaron inmediatamente al paso de ruta de audiencia sin tiempo para interactuar con el mensaje. En otras palabras, los usuarios se evalúan para una interacción con el mensaje casi inmediatamente después de que se envía el mensaje.

Para dar a los usuarios tiempo de interactuar con un mensaje enviado, añade un retraso entre el paso de mensaje y la ruta de audiencia. Por ejemplo, un retraso de 24 horas les da a los usuarios 24 horas después del envío del mensaje para interactuar con el Mensaje A antes de la evaluación.

## Creación de una ruta de audiencia {#creating-an-audience-path}

Para añadir un paso de rutas de audiencia, haz lo siguiente:

1. Añade un paso a tu Canvas.
2. Arrastra y suelta el componente desde la barra lateral, o selecciona <i class="fas fa-plus-circle"></i> **Añadir** en la parte inferior de un paso y selecciona **Rutas de audiencia**.

El componente predeterminado de rutas de audiencia contiene dos grupos de audiencia predeterminados, **Grupo 1** y **Todos los demás**. El grupo **Todos los demás** incluye a cualquier usuario que no pertenezca a un grupo de audiencia definido. Este grupo siempre es el último en el orden.

### Definición de grupos de audiencia {#defining-audience-groups}

La siguiente captura de pantalla muestra el diseño de un paso de rutas de audiencia expandido. Aquí puedes definir hasta ocho grupos de audiencia (uno preestablecido y siete personalizables). Para definir un grupo de audiencia, selecciona el nombre del grupo en el editor de rutas de audiencia. Puedes renombrar tu grupo de audiencia, elegir los filtros y Segments que se aplican a tu grupo, y añadir o eliminar grupos. Por ejemplo, si quisieras dirigir mensajes de incorporación a un grupo de usuarios, podrías seleccionar filtros de reorientación, como "Ha hecho clic en correo electrónico" y "Ha hecho clic en mensaje dentro de la aplicación".

![Una ruta de audiencia expandida con grupos para "Le encanta la cocina asiática", "Le encanta la cocina latina", "Le encanta la cocina europea" y "Todos los demás".]({% image_buster /assets/img/audience_path/audience_path3.png %})

Una vez completado el paso de rutas de audiencia, cada grupo de audiencia tendrá una rama separada. Puedes continuar usando rutas de audiencia para filtrar aún más tu audiencia, o continuar tu recorrido en Canvas con los pasos estándar de Canvas.

![Dos rutas de audiencia con diferentes grupos basados en la participación.]({% image_buster /assets/img/audience_path/audience_path4.png %}){: style="max-width:50%"}

#### Uso de filtros de comparación con variables de contexto {#using-comparison-filters-with-context-variables}

Al dividir por una variable de contexto que contiene una fecha, consulta [Filtros de día del año y hora para variables de contexto de fecha]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#day-of-year-and-time-filters-for-date-context-variables) para elegir el tipo de comparación correcto.

### Prueba de grupos de audiencia {#testing-audience-groups}

Después de añadir Segments y filtros a tu audiencia, puedes probar si tus grupos de audiencia están configurados como se espera [buscando un usuario]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) para confirmar que coincide con los criterios de audiencia.

![La sección "Búsqueda de usuario".]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

## Uso de las rutas de audiencia {#using-audience-paths}

El verdadero poder de las rutas de audiencia reside en colocar las rutas que más te importan **primero**. Aunque esta característica no necesita utilizarse de forma estratégica, algunos especialistas en marketing pueden encontrarse promocionando ciertos productos a los usuarios, como ofertas especiales o lanzamientos de edición limitada.

Al colocar esos Segments primero en la lista, puedes segmentar a los usuarios que coinciden con filtros y Segments específicos, y al mismo tiempo segmentar a los usuarios que podrían no cumplir esos criterios específicos, todo en un único paso en Canvas.

![Una ruta de audiencia con grupos para "Le gustan los zapatos de Big Brand", "Le gusta Big Brand" y "Todos los demás".]({% image_buster /assets/img/audience_path/audience_path2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Por ejemplo, supongamos que quisieras enviar a un grupo de usuarios anuncios de nuevos productos. Empezarías colocando los filtros que corresponden a esos productos **primero** en la ruta de audiencia. Si estuvieras creando una Campaign de marketing para la empresa "Big Brand" y una nueva marca de comercio minorista acabara de lanzarse, podrías seleccionar filtros como "Le gustan los zapatos de Big Brand" o "Le gustan los bolsos de Big Brand", y enviar diferentes mensajes de correo electrónico según el grupo filtrado en el que se encuentren.

Cuando los usuarios entren en este componente de rutas de audiencia, primero serán evaluados para el grupo de audiencia 1 "Le gustan los zapatos de Big Brand", la primera ruta de la lista. Si coinciden, continuarán al siguiente componente definido en tu Canvas. Si no "les gustan los zapatos de Big Brand", serán evaluados para el siguiente grupo de audiencia, grupo de audiencia 2 "Le gustan los bolsos de Big Brand", y continuarán al siguiente paso si se cumplen los criterios. Por último, los usuarios que no coincidan con los grupos anteriores entrarán en el grupo "Todos los demás" y también continuarán al siguiente paso en Canvas que definas para esa ruta.

También puedes ver el rendimiento de este paso utilizando los [análisis de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics#performance-visualization).

### Segmentar rutas de audiencia con números de contenedor aleatorio {#segmenting-audience-paths-with-random-bucket-numbers}

Si tu Canvas utiliza un [límite de velocidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) (como limitar el número total de usuarios que recibirán el Canvas), Braze recomienda que no utilices números de contenedor aleatorio para segmentar tus rutas de audiencia.

Un [número de contenedor aleatorio]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) es un atributo de usuario que puede utilizarse para crear Segments de usuarios aleatorios distribuidos uniformemente. Braze utiliza el número de contenedor aleatorio para agrupar a los usuarios durante la fase de segmentación de la entrada en Canvas, y cada grupo se procesa por separado. Dependiendo de qué grupos terminen de procesarse primero, algunos usuarios pueden quedar limitados en la entrada debido al límite de velocidad, lo que podría causar una distribución desigual de usuarios cuando lleguen al paso de rutas de audiencia.

En este escenario, intenta utilizar [recorridos de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) en su lugar.

### Uso del filtro de canal inteligente con rutas de audiencia {#using-intelligent-channel-filter-with-audience-paths}

Utilizando una combinación de pasos de rutas de audiencia y filtros de canal inteligente, puedes adaptar tu experiencia de mensajería a las preferencias y comportamientos de cada usuario. De esta forma, tus usuarios recibirán los mensajes más relevantes a través de los canales apropiados.

Por ejemplo, en un paso de rutas de audiencia, puedes crear tres audiencias: correo electrónico, push móvil y todos los demás. Para la audiencia de correo electrónico, añade el filtro `Intelligent Channel is Email`. Para la audiencia de push móvil, añade el filtro `Intelligent Channel is Mobile Push`. Luego, puedes añadir un paso de mensaje para cada una de las rutas de audiencia para entregar mensajes personalizados y relevantes.

{% alert tip %}
Consulta nuestras [plantillas de Braze Canvas]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) para ver ejemplos de cómo puedes personalizar estas plantillas prediseñadas a tu favor.
{% endalert %}