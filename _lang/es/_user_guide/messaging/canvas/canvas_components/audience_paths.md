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

- Enviar a los usuarios por diferentes recorridos de Canvas basados en criterios de audiencia.
- Colocar tus grupos de audiencia más importantes primero; los usuarios toman la primera ruta para la que califican.
- Segmentar usuarios de manera precisa a gran escala.
  - Puedes crear hasta ocho grupos de audiencia (dos predeterminados y seis grupos adicionales) por paso de Rutas de Audiencia, pero es posible que quieras conectar múltiples pasos de Rutas de Audiencia para clasificar aún más a tus usuarios.

Dentro de un solo paso de Rutas de Audiencia, los usuarios son evaluados contra los grupos de audiencia en orden y avanzan por la primera ruta para la que califican. Si conectas múltiples pasos de Rutas de Audiencia en un Canvas, los usuarios son evaluados nuevamente cada vez que alcanzan un nuevo paso de Rutas de Audiencia.

### Cómo se evalúa a los usuarios {#how-users-are-evaluated}

![Canvas que muestra un retraso de 24 horas después de un paso de mensaje, seguido de una ruta de audiencia.]({% image_buster /assets/img/audience_path/audience_path5.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Los usuarios son evaluados contra filtros y pertenencia a Segments **en el momento en que alcanzan el paso de ruta de audiencia**, no cuando entraron al Canvas. Después de la evaluación, avanzan inmediatamente por la ruta correspondiente. Cuando un usuario es colocado en un grupo de audiencia, permanece en ese grupo incluso si su perfil de usuario cambia posteriormente.

<div style="clear: both;"></div>

{% alert important %}
Las Rutas de Audiencia evalúan en función de los atributos actuales del usuario, filtros y pertenencia a Segments en el momento de la evaluación. No evalúan en función del evento específico que desencadenó la entrada al Canvas. Para dirigir a los usuarios en función de una acción que realizan (como un evento personalizado), usa [Rutas de Acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) en su lugar.
{% endalert %}

Los usuarios no son reevaluados contra su grupo de audiencia después de avanzar por una ruta. Si el mensaje que sigue está retrasado por un paso de retraso, horas tranquilas, sincronización inteligente, límite de velocidad o entrega en zona horaria local, el perfil de un usuario puede cambiar antes de que se envíe ese mensaje.

Para confirmar que los usuarios aún cumplen con los criterios de Segment y filtro antes de que se envíe el paso de mensaje, activa **Validar audiencia al enviar el mensaje** en las [validaciones de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) del paso de mensaje. Las validaciones de entrega solo comprueban los Segments y filtros que añades a ese paso de mensaje, por lo que no reutilizan los criterios de tu ruta de audiencia. Para los mensajes dentro de la aplicación, las validaciones de entrega se comprueban cuando un usuario entra en el paso de mensaje, no cuando se muestra el mensaje.

### Dar tiempo para la evaluación de usuarios {#allowing-time-for-user-evaluations}

Debido a que la evaluación es inmediata, es importante añadir un retraso antes de la ruta de audiencia si los criterios de la ruta dependen de una interacción del usuario con un paso anterior.

Por ejemplo, si a los usuarios se les envía el Mensaje A y el siguiente paso es una ruta de audiencia que evalúa si interactuaron con ese mensaje, todos los usuarios avanzarán al paso para aquellos que no han interactuado con ese mensaje. Esto se debe a que los usuarios avanzaron inmediatamente al paso de ruta de audiencia sin tiempo para interactuar con el mensaje. En otras palabras, los usuarios son evaluados por una interacción con el mensaje casi inmediatamente después de que se envía el mensaje.

Para dar a los usuarios tiempo para interactuar con un mensaje enviado, añade un retraso entre el paso de mensaje y la ruta de audiencia. Por ejemplo, un retraso de 24 horas les da a los usuarios 24 horas después del envío del mensaje para interactuar con el Mensaje A antes de la evaluación.

## Creación de una ruta de audiencia {#creating-an-audience-path}

Para añadir un paso de Rutas de Audiencia, haz lo siguiente:

1. Añade un paso a tu Canvas.
2. Arrastra y suelta el componente desde la barra lateral, o selecciona <i class="fas fa-plus-circle"></i> **Añadir** en la parte inferior de un paso y selecciona **Rutas de Audiencia**.

El componente predeterminado de Rutas de Audiencia contiene dos grupos de audiencia predeterminados: **Grupo 1** y **Todos los demás**. El grupo **Todos los demás** incluye a cualquier usuario que no se encuentre en un grupo de audiencia definido. Este grupo siempre es el último en el orden.

### Definición de grupos de audiencia {#defining-audience-groups}

La siguiente captura de pantalla muestra el diseño de un paso de Rutas de Audiencia expandido. Aquí puedes definir hasta ocho grupos de audiencia (uno preestablecido y siete personalizables). Para definir un grupo de audiencia, selecciona el nombre del grupo en el editor de Rutas de Audiencia. Puedes cambiar el nombre de tu grupo de audiencia, elegir los filtros y Segments que se aplican a tu grupo, y añadir o eliminar grupos. Por ejemplo, si quisieras orientar la mensajería de incorporación a un grupo de usuarios, podrías seleccionar filtros de reorientación, como "Ha hecho clic en correo electrónico" y "Ha hecho clic en mensaje dentro de la aplicación".

![Una ruta de audiencia expandida con grupos para "Le encanta la cocina asiática", "Le encanta la cocina latina", "Le encanta la cocina europea" y "Todos los demás".]({% image_buster /assets/img/audience_path/audience_path3.png %})

Una vez que el paso de Rutas de Audiencia está completo, cada grupo de audiencia tendrá una rama separada. Puedes seguir utilizando Rutas de Audiencia para filtrar aún más tu audiencia, o continuar tu recorrido en Canvas con los pasos estándar de Canvas.

![Dos Rutas de Audiencia con diferentes grupos basados en la participación.]({% image_buster /assets/img/audience_path/audience_path4.png %}){: style="max-width:50%"}

#### Uso de filtros de comparación con variables de contexto {#using-comparison-filters-with-context-variables}

Al dividir por una variable de contexto que contiene una fecha, consulta [Filtros de día del año y hora para variables de contexto de fecha]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#day-of-year-and-time-filters-for-date-context-variables) para elegir el tipo de comparación correcto.

### Prueba de grupos de audiencia {#testing-audience-groups}

Después de añadir Segments y filtros a tu audiencia, puedes probar si tus grupos de audiencia están configurados como se espera [buscando un usuario]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) para confirmar que coincide con los criterios de audiencia.

![La sección "Búsqueda de usuarios".]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

## Uso de las Rutas de audiencia {#using-audience-paths}

El verdadero poder de las Rutas de audiencia radica en colocar las rutas que más te importan **primero**. Aunque esta característica no necesita usarse de forma estratégica, algunos especialistas en marketing pueden encontrarse promocionando ciertos productos a usuarios, como ofertas especiales o lanzamientos de edición limitada.

Al colocar esos Segments primero en la lista, puedes segmentar a los usuarios que cumplen con filtros y Segments específicos, y al mismo tiempo segmentar a usuarios que podrían no cumplir con esos criterios específicos, todo en un solo paso en Canvas.

![Una Ruta de audiencia con grupos para "Le gustan los zapatos de Big Brand", "Le gusta Big Brand" y "Todos los demás".]({% image_buster /assets/img/audience_path/audience_path2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Por ejemplo, supongamos que quisieras enviar anuncios de nuevos productos a un grupo de usuarios. Empezarías colocando los filtros correspondientes a esos productos **primero** en la Ruta de audiencia. Si estuvieras creando una Campaign de marketing para la empresa "Big Brand" y una nueva marca de comercio minorista acabara de lanzarse, podrías seleccionar filtros como "Le gustan los zapatos de Big Brand" o "Le gustan las bolsas de Big Brand", y enviar diferentes mensajes de correo electrónico según el grupo filtrado en el que se encuentren.

Cuando los usuarios entren en este componente de Rutas de audiencia, primero serán evaluados para el Grupo de audiencia 1, "Le gustan los zapatos de Big Brand", la primera ruta en la lista. Si es así, continuarán al siguiente componente definido en tu Canvas. Si no "les gustan los zapatos de Big Brand", serán evaluados para el siguiente grupo de audiencia, Grupo de audiencia 2, "Le gustan las bolsas de Big Brand", y continuarán al siguiente paso si se cumplen los criterios. Por último, los usuarios que no pertenezcan a los grupos anteriores caerán en el grupo "Todos los demás" y también continuarán al siguiente paso en Canvas que definas para esa ruta.

También puedes ver el rendimiento de este paso usando [análisis de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics#performance-visualization).

### Segmentación de Rutas de audiencia con números de contenedor aleatorio {#segmenting-audience-paths-with-random-bucket-numbers}

Si tu Canvas usa un [límite de velocidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) (como limitar el número total de usuarios que recibirán el Canvas), Braze recomienda que no uses números de contenedor aleatorio para segmentar tus Rutas de audiencia.

Un [número de contenedor aleatorio]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) es un atributo de usuario que puede usarse para crear Segments de usuarios aleatorios distribuidos de forma uniforme. Braze usa el número de contenedor aleatorio para agrupar usuarios durante la fase de segmentación de la entrada al Canvas, y cada grupo se procesa por separado. Dependiendo de qué grupos terminen de procesarse primero, algunos usuarios pueden quedar limitados en la entrada debido al límite de velocidad, lo que podría causar una distribución desigual de usuarios cuando lleguen al paso de Rutas de audiencia.

En este escenario, intenta usar [recorridos de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) en su lugar.

### Uso del filtro de canal inteligente con Rutas de audiencia {#using-intelligent-channel-filter-with-audience-paths}

Usando una combinación de pasos de Rutas de audiencia y filtros de canal inteligente, puedes adaptar tu experiencia de mensajería a las preferencias y comportamientos de cada usuario. De esta manera, tus usuarios recibirán los mensajes más relevantes a través de los canales apropiados.

Por ejemplo, en un paso de Rutas de audiencia, puedes crear tres audiencias: correo electrónico, push móvil y Todos los demás. Para la audiencia de correo electrónico, añade el filtro `Intelligent Channel is Email`. Para la audiencia de push móvil, añade el filtro `Intelligent Channel is Mobile Push`. Luego, puedes añadir un paso de mensaje para cada una de las rutas de audiencia para entregar mensajes personalizados y relevantes.

{% alert tip %}
Consulta nuestras [plantillas de Braze Canvas]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) para ver ejemplos de cómo puedes personalizar estas plantillas prediseñadas a tu favor.
{% endalert %}