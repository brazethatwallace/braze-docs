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

![Una Ruta de audiencia con dos grupos: usuarios comprometidos y el resto.]({% image_buster /assets/img/audience_path/audience_path.png %}){: style="float:right;max-width:45%;margin-left:15px;margin-top:15px;"}

Los usuarios avanzan por la primera rama cuyos criterios cumplan, así que coloca la ruta más importante primero. Esto reduce la ambigüedad sobre a dónde van los usuarios y qué mensajes reciben. Ten en cuenta que este orden no es [editable después del lanzamiento]({{site.baseurl}}/post-launch_edits).

Con las Rutas de audiencia, puedes:

- Enviar usuarios por diferentes rutas de Canvas según criterios de audiencia.
- Colocar tus grupos de audiencia más importantes primero; los usuarios toman la primera ruta para la que califican.
- Segmentar usuarios con precisión a gran escala.
  - Puedes crear hasta ocho grupos de audiencia (dos predeterminados y seis adicionales) por paso de Rutas de audiencia, pero es posible que quieras conectar múltiples pasos de Rutas de audiencia para clasificar aún más a tus usuarios.

Dentro de un solo paso de Rutas de audiencia, los usuarios se evalúan en orden según los grupos de audiencia y avanzan por la primera ruta para la que califican. Si conectas múltiples pasos de Rutas de audiencia en un Canvas, los usuarios se evalúan nuevamente cada vez que llegan a un nuevo paso de Rutas de audiencia.

### Cómo se evalúan los usuarios {#how-users-are-evaluated}

![Canvas que muestra un retraso de 24 horas después de un paso de Mensaje, seguido de una Ruta de audiencia.]({% image_buster /assets/img/audience_path/audience_path5.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Los usuarios se evalúan según filtros y pertenencia a segmentos **en el momento en que llegan al paso de Ruta de audiencia**, no cuando entraron al Canvas. Después de la evaluación, avanzan inmediatamente a la ruta correspondiente. Cuando un usuario es colocado en un grupo de audiencia, permanece en ese grupo incluso si su perfil de usuario cambia después.

<div style="clear: both;"></div>

{% alert important %}
Las Rutas de audiencia evalúan según los atributos actuales del usuario, filtros y pertenencia a segmentos en el momento de la evaluación. No evalúan según el evento específico que desencadenó la entrada al Canvas. Para dirigir usuarios según una acción que realizan (como un evento personalizado), usa [Rutas de acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) en su lugar.
{% endalert %}

### Dar tiempo para las evaluaciones de usuarios {#allowing-time-for-user-evaluations}

Dado que la evaluación es inmediata, es importante agregar un retraso antes de la Ruta de audiencia si los criterios de la ruta dependen de una interacción del usuario con un paso anterior.

Por ejemplo, si se envía a los usuarios el Mensaje A y el siguiente paso es una Ruta de audiencia que evalúa si interactuaron con ese mensaje, todos los usuarios avanzarán al paso para aquellos que no han interactuado con ese mensaje. Esto se debe a que los usuarios avanzaron inmediatamente al paso de Ruta de audiencia sin tiempo para interactuar con el mensaje. En otras palabras, los usuarios se evalúan para una interacción con el mensaje casi inmediatamente después de que se envía el mensaje.

Para dar tiempo a los usuarios de interactuar con un mensaje enviado, agrega un retraso entre el paso de Mensaje y la Ruta de audiencia. Por ejemplo, un retraso de 24 horas les da a los usuarios 24 horas después del envío del mensaje para interactuar con el Mensaje A antes de la evaluación.

## Crear una Ruta de audiencia {#creating-an-audience-path}

Para agregar un paso de Rutas de audiencia, haz lo siguiente:

1. Agrega un paso a tu Canvas.
2. Arrastra y suelta el componente desde la barra lateral, o selecciona <i class="fas fa-plus-circle"></i> **Agregar** en la parte inferior de un paso y selecciona **Rutas de audiencia**.

El componente predeterminado de Rutas de audiencia contiene dos grupos de audiencia predeterminados, **Grupo 1** y **El resto**. El grupo **El resto** incluye a cualquier usuario que no pertenezca a un grupo de audiencia definido. Este grupo siempre es el último en el orden.

### Definir grupos de audiencia {#defining-audience-groups}

La siguiente captura de pantalla muestra el diseño de un paso de Rutas de audiencia expandido. Aquí puedes definir hasta ocho grupos de audiencia (uno preestablecido y siete personalizables). Para definir un grupo de audiencia, selecciona el nombre del grupo en el editor de Rutas de audiencia. Puedes renombrar tu grupo de audiencia, elegir los filtros y segmentos que aplican a tu grupo, y agregar o eliminar grupos.

Por ejemplo, si quisieras dirigir mensajes de incorporación a un grupo de usuarios, podrías seleccionar filtros de reorientación, como "Ha hecho clic en correo electrónico" y "Ha hecho clic en mensaje dentro de la aplicación".

![Una Ruta de audiencia expandida con grupos para "Le encanta la cocina asiática", "Le encanta la cocina latina", "Le encanta la cocina europea" y "El resto".]({% image_buster /assets/img/audience_path/audience_path3.png %})

Una vez completado el paso de Rutas de audiencia, cada grupo de audiencia tendrá una rama separada. Puedes continuar usando Rutas de audiencia para filtrar aún más tu audiencia, o continuar tu recorrido en Canvas con los pasos estándar de Canvas.

![Dos Rutas de audiencia con diferentes grupos basados en la interacción.]({% image_buster /assets/img/audience_path/audience_path4.png %}){: style="max-width:50%"}

### Probar grupos de audiencia {#testing-audience-groups}

Después de agregar segmentos y filtros a tu audiencia, puedes probar si tus grupos de audiencia están configurados como se espera [buscando un usuario]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) para confirmar que coincide con los criterios de audiencia.

![La sección "Búsqueda de usuario".]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

## Usar Rutas de audiencia {#using-audience-paths}

El verdadero poder de las Rutas de audiencia radica en colocar las rutas que más te importan **primero**. Aunque esta característica no necesita usarse estratégicamente, algunos especialistas en marketing pueden encontrarse promoviendo ciertos productos a usuarios, como ofertas especiales o lanzamientos de edición limitada.

Al colocar esos segmentos primero en la lista, puedes dirigirte a usuarios que caen en filtros y segmentos específicos mientras también te diriges a usuarios que podrían no cumplir esos criterios específicos, todo en un solo paso de Canvas.

![Una Ruta de audiencia con grupos para "Le gustan los zapatos de Big Brand", "Le gusta Big Brand" y "El resto".]({% image_buster /assets/img/audience_path/audience_path2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Por ejemplo, supongamos que quieres enviar a un grupo de usuarios anuncios de nuevos productos. Empezarías colocando los filtros que corresponden a esos productos **primero** en la Ruta de audiencia. Si estuvieras creando una campaña de marketing para la empresa "Big Brand" y una nueva marca de comercio minorista acabara de lanzarse, podrías seleccionar filtros como "Le gustan los zapatos de Big Brand" o "Le gustan los bolsos de Big Brand", y enviar diferentes mensajes de correo electrónico según el grupo filtrado en el que caigan.

Cuando los usuarios entran en este componente de Rutas de audiencia, primero se evalúan para el Grupo de audiencia 1 "Le gustan los zapatos de Big Brand", la primera ruta en la lista. Si califican, continuarán al siguiente componente definido en tu Canvas. Si no "Les gustan los zapatos de Big Brand", entonces se evaluarán para el siguiente grupo de audiencia, Grupo de audiencia 2 "Le gustan los bolsos de Big Brand", y continuarán al siguiente paso si se cumplen los criterios. Por último, los usuarios que no caigan en los grupos anteriores caerán en el grupo "El resto" y también continuarán al siguiente paso de Canvas que definas para esa ruta.

También puedes ver el rendimiento de este paso usando [análisis de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics#performance-visualization).

### Segmentar Rutas de audiencia con números de contenedor aleatorio {#segmenting-audience-paths-with-random-bucket-numbers}

Si tu Canvas usa un [límite de velocidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) (como limitar el número total de usuarios que recibirán el Canvas), Braze recomienda que no uses números de contenedor aleatorio para segmentar tus Rutas de audiencia.

Un [número de contenedor aleatorio]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) es un atributo de usuario que se puede usar para crear segmentos uniformemente distribuidos de usuarios aleatorios. Braze usa el número de contenedor aleatorio para agrupar usuarios durante la fase de segmentación de la entrada al Canvas, y cada grupo se procesa por separado. Dependiendo de qué grupos terminen de procesarse primero, algunos usuarios pueden ser limitados en la entrada debido al límite de velocidad, lo que podría causar una distribución desigual de usuarios cuando llegan al paso de Rutas de audiencia.

En este escenario, intenta usar [Recorridos de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) en su lugar.

### Usar el filtro de canal inteligente con Rutas de audiencia {#using-intelligent-channel-filter-with-audience-paths}

Usando una combinación de pasos de Rutas de audiencia y filtros de canal inteligente, puedes adaptar tu experiencia de mensajería a las preferencias y comportamientos de cada usuario. De esta manera, tus usuarios recibirán los mensajes más relevantes a través de los canales apropiados.

Por ejemplo, en un paso de Rutas de audiencia, puedes crear tres audiencias: correo electrónico, push móvil y el resto. Para la audiencia de correo electrónico, agrega el filtro `Intelligent Channel is Email`. Para la audiencia de push móvil, agrega el filtro `Intelligent Channel is Mobile Push`. Luego, puedes agregar un paso de Mensaje para cada una de las rutas de audiencia para entregar mensajes personalizados y relevantes.

{% alert tip %}
Consulta nuestras [plantillas de Braze Canvas]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) para ver ejemplos de cómo puedes personalizar estas plantillas prediseñadas a tu favor.
{% endalert %}