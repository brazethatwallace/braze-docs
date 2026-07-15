---
nav_title: Recomendaciones de elementos
article_title: Recomendaciones de elementos en Braze
page_order: 10
search_rank: 1
description: "Descubre todo lo que necesitas saber sobre las herramientas de recomendaciones de elementos en Braze."
---

# Recomendaciones de elementos {#item-recommendations}

> Mejora tus recomendaciones con Braze creando una herramienta de recomendaciones que pueda sugerir a tus usuarios los elementos y contenidos que realmente desean. Desde personalizar experiencias con IA hasta construir tus propias herramientas con Liquid o Contenido conectado, encontrarás todo lo que necesitas para que cada recomendación cuente.

## Requisitos previos {#prerequisites}

Antes de poder crear o utilizar recomendaciones de elementos en Braze, deberás [crear al menos un catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create)&#8212;solo se recomendarán a los usuarios los elementos de ese catálogo.

## Tipos y casos de uso {#types-and-use-cases}

### Personalización de IA {#ai}

Como parte de la característica de [Recomendaciones de elementos de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai), las recomendaciones personalizadas de IA aprovechan el aprendizaje profundo para predecir lo que más les puede interesar a tus usuarios en función de lo que les ha interesado en el pasado. Este método proporciona un sistema de recomendación dinámico y a medida que se adapta al comportamiento del usuario.

Las recomendaciones personalizadas de IA utilizan los datos de los últimos 6 meses de interacción con los elementos, como compras o eventos personalizados, para construir el modelo de recomendación. Para los usuarios que no disponen de datos suficientes para crear una lista personalizada, los elementos más populares sirven como alternativa, de modo que los usuarios siguen recibiendo sugerencias relevantes.

Con las Recomendaciones de elementos de IA, también puedes filtrar aún más los elementos disponibles con
[selecciones]({{site.baseurl}}/user_guide/data/activation/catalogs/selections). Sin embargo, las selecciones con Liquid no pueden utilizarse en las recomendaciones de IA, así que tenlo en cuenta cuando construyas las selecciones de tu catálogo.

{% alert tip %}
Las recomendaciones personalizadas con IA funcionan mejor con cientos o miles de elementos y, normalmente, al menos 30 000 usuarios con datos de compra o interacción. Esto es solo una guía aproximada y puede variar. Los otros tipos de recomendación pueden funcionar con menos datos.
{% endalert %}

#### Casos de uso {#use-cases}

Según los datos de interacción que se estén rastreando, los casos de uso de este modelo podrían incluir:

{% tabs local %}
{% tab Con más probabilidades de comprar a continuación %}
Predecir y recomendar los elementos que un usuario tiene más probabilidades de comprar a continuación, basándose en eventos de compra o eventos personalizados relacionados con las compras. Por ejemplo:

- Un sitio de viajes podría sugerir paquetes de vacaciones, vuelos o estancias en hoteles basándose en el historial de navegación y las reservas anteriores de un usuario, anticipándose a su próximo destino de viaje y facilitándole la planificación del mismo.
- Una plataforma de streaming puede analizar los hábitos de visionado para recomendar programas o películas que un usuario tiene más probabilidades de ver a continuación, manteniéndolo interactuando y reduciendo las tasas de abandono.

{% details Requisitos %}
- Recomendaciones de elementos de IA
- Catálogo de elementos relevantes
- Un método para realizar el seguimiento de las compras: un objeto de compra, un evento personalizado o un [evento de pedido realizado]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events?tab=ecommerce.order_placed)
{% enddetails %}

{% details Configuración %}
1. Crea una [recomendación de elementos de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai).
2. Configura el **Tipo** como **AI Personalized**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación solo a los elementos relevantes.
5. Elige cómo realizas actualmente el seguimiento de los eventos de compra y la propiedad de evento correspondiente.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Elemento más popular {#most-popular}

El modelo de recomendación "Most popular" muestra los elementos con los que los usuarios tienen más interacciones.

#### Casos de uso

Según los datos de interacción que se estén rastreando, los casos de uso de este modelo podrían incluir la recomendación de:

{% tabs local %}
{% tab Más populares %}
Anima a los usuarios a explorar los elementos más populares de tu catálogo en función de sus compras. Para asegurarte de que solo aparece contenido relevante, te recomendamos filtrar con una selección. Por ejemplo, un servicio de entrega de comida podría destacar los platos o restaurantes mejor valorados dentro de la zona de un usuario, basándose en la popularidad de los pedidos en toda la plataforma, fomentando la prueba y el descubrimiento.

{% details Requisitos %}
- Recomendaciones de elementos de IA
- Catálogo de elementos relevantes
- Un objeto de compra, un evento de pedido realizado o cualquier evento personalizado
{% enddetails %}

{% details Configuración %}
1. Crea una [recomendación de elementos de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai).
2. Establece el **Tipo** en **Most popular**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación solo a los elementos relevantes. Por ejemplo, el servicio de entrega de comida podría tener una selección para filtrar por ubicación del restaurante o tipo de plato.
5. Elige cómo realizas actualmente el seguimiento de los eventos y la propiedad de evento correspondiente.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}

{% tab Con más "Me gusta" %}
Anima a los usuarios a explorar elementos que les han gustado recientemente o elementos que son populares, basándote en un evento personalizado para los "Me gusta". Por ejemplo, una aplicación de streaming de música podría crear listas de reproducción personalizadas o sugerir el lanzamiento de nuevos álbumes basándose en los géneros o artistas que le han gustado a un usuario en el pasado, mejorando la interacción del usuario y el tiempo que pasa en la aplicación.

{% details Requisitos %}
- Recomendaciones de elementos de IA
- Catálogo de elementos relevantes
- Evento personalizado para likes
{% enddetails %}

{% details Configuración %}
1. Crea una [recomendación de elementos de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai).
2. Configura el **Tipo** como **Most recent**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación solo a los elementos relevantes.
5. Elige **Custom Event** y selecciona tu evento personalizado para likes de la lista.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}

{% tab Más vistos %}
Destaca los elementos que han llamado la atención de tu base de usuarios a través de las visualizaciones para fomentar la interacción o las compras. Por ejemplo, un sitio web inmobiliario podría mostrar los anuncios más vistos en la zona de búsqueda de un usuario para destacar las propiedades que atraen mucha atención, lo que podría indicar buenas ofertas o ubicaciones deseables.

{% details Requisitos %}
- Recomendaciones de elementos de IA
- Catálogo de elementos relevantes
- Evento personalizado para vistas
{% enddetails %}

{% details Configuración %}
1. Crea una [recomendación de elementos de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai).
2. Establece el **Tipo** en **Most popular**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación solo a los elementos relevantes.
5. Elige **Custom Event** y selecciona tu evento personalizado para vistas de la lista.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}

{% tab Populares en el carrito %}
Muestra elementos añadidos a los carritos por muchos otros compradores, proporcionando a los usuarios una visión de las tendencias actuales entre tus ofertas.

Por ejemplo, un comercio minorista de moda podría promocionar ropa y accesorios que estén de moda basándose en las adiciones populares a los carritos por parte de otros clientes. A continuación, pueden crear una sección dinámica de "Tendencias actuales" en su página de inicio y aplicación móvil, que se actualiza en tiempo real para animar a los compradores a comprar antes de que se agoten los elementos.

{% details Requisitos %}
- Recomendaciones de elementos de IA
- Catálogo de elementos relevantes
- Evento personalizado para añadido al carrito
{% enddetails %}

{% details Configuración %}
1. Crea una [recomendación de elementos de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai).
2. Establece el **Tipo** en **Most popular**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación solo a los elementos relevantes.
5. Elige **Custom Event** y selecciona de la lista tu evento personalizado para añadir al carrito.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Elemento más reciente {#most-recent}

El modelo de recomendación "Most recent" muestra los elementos con los que los usuarios han interactuado más recientemente. Utiliza este modelo para reducir el abandono animando a los usuarios inactivos a volver a interactuar con contenidos relevantes.

#### Casos de uso

Según los datos de interacción que se estén rastreando, los casos de uso de este modelo podrían incluir la recomendación de:

{% tabs local %}
{% tab Clics recientes %}
Anima a los usuarios a volver a visitar los elementos en los que han hecho clic recientemente, basándote en un evento personalizado para los clics. Por ejemplo, un minorista de moda online podría crear una recomendación para enviar correos electrónicos de seguimiento o notificaciones push con prendas por las que un usuario ha mostrado interés al hacer clic en ellas, animándole a volver a visitar el elemento y realizar una compra.

{% details Requisitos %}
- Recomendaciones de elementos de IA
- Catálogo de elementos relevantes
- Evento personalizado para los clics
{% enddetails %}

{% details Configuración %}
1. Crea una [recomendación de elementos de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai).
2. Configura el **Tipo** como **Most recent**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación solo a los elementos relevantes.
5. Elige **Custom Event** y selecciona tu evento personalizado para clics de la lista.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}

{% endtab %}
{% tab "Me gusta" recientes %}
Anima a los usuarios a explorar elementos que les han gustado recientemente o elementos que son populares, basándote en un evento personalizado para los "Me gusta". Por ejemplo, una aplicación de streaming de música podría crear listas de reproducción personalizadas o sugerir el lanzamiento de nuevos álbumes basándose en los géneros o artistas que le han gustado a un usuario en el pasado, mejorando la interacción del usuario y el tiempo que pasa en la aplicación.

{% details Requisitos %}
- Recomendaciones de elementos de IA
- Catálogo de elementos relevantes
- Evento personalizado para likes
{% enddetails %}

{% details Configuración %}
1. Crea una [recomendación de elementos de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai).
2. Configura el **Tipo** como **Most recent**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación solo a los elementos relevantes.
5. Elige **Custom Event** y selecciona tu evento personalizado para likes de la lista.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}

{% tab Interacciones recientes %}
Promociona elementos con los que los usuarios hayan interactuado recientemente, incluyendo visualizaciones, clics o compras. Este enfoque mantiene tus recomendaciones actualizadas y alineadas con los intereses más recientes del usuario. Por ejemplo:

- **Educación:** Una plataforma de educación en línea podría animar a los usuarios que han visto recientemente un video educativo, pero no se han matriculado en un curso, a consultar cursos similares o temas de interés para mantener al usuario interactuando y motivado para empezar a aprender.
- **Fitness:** Una aplicación de fitness puede sugerir entrenamientos o retos similares a los que el usuario ha completado o con los que ha interactuado recientemente, manteniendo su rutina de ejercicios variada y atractiva.
- **Comercio minorista de mejoras para el hogar:** Después de que un cliente compre una herramienta eléctrica, un comercio minorista puede recomendarle accesorios relacionados o equipos de seguridad basados en su compra reciente, mejorando la experiencia y la seguridad del usuario.

{% details Requisitos %}
- Recomendaciones de elementos de IA
- Catálogo de elementos relevantes
- Un objeto de compra, un evento de pedido realizado o cualquier evento personalizado para una interacción
{% enddetails %}

{% details Configuración %}
1. Crea una [recomendación de elementos de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai).
2. Configura el **Tipo** como **Most recent**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación solo a los elementos relevantes.
5. Elige **Custom Event** y selecciona tu evento personalizado para clics de la lista.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}

{% tab Añadidos recientemente %}
Recuerda a los usuarios su interés por elementos que han añadido recientemente a su carrito, pero que aún no han comprado. Por ejemplo, un comercio minorista online podría enviar recordatorios u ofrecer descuentos por tiempo limitado en los elementos de su carrito, animando a los usuarios a completar sus compras antes de que caduquen las ofertas.
{% details Requisitos %}

- Recomendaciones de elementos de IA
- Catálogo de elementos relevantes
- Evento personalizado para añadido al carrito
{% enddetails %}

{% details Configuración %}
1. Crea una [recomendación de elementos de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai).
2. Configura el **Tipo** como **Most recent**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación solo a los elementos relevantes.
5. Elige **Custom Event** y selecciona de la lista tu evento personalizado para añadir al carrito.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Elemento en tendencia {#trending}

El modelo de recomendaciones "Trending" presenta los elementos que han mostrado un impulso más positivo en las interacciones recientes de los usuarios. Calculamos esto utilizando un análisis ponderado de aproximadamente 10 semanas de historial de eventos, aplicando la mayor ponderación a las últimas 2 semanas aproximadas. Para evitar que las pequeñas fluctuaciones afecten a la calidad de las recomendaciones, aplicamos un umbral de actividad y técnicas de suavizado estadístico.

A diferencia del modelo "Most popular", que presenta elementos con una interacción alta y constante, este modelo presenta elementos que han experimentado un repunte en las interacciones. Puedes utilizarlo para recomendar productos prometedores que actualmente están ganando tracción.

#### Casos de uso

Según los datos de interacción que se estén rastreando, los casos de uso de este modelo podrían incluir la recomendación de:

{% tabs local %}
{% tab Compras en tendencia %}
Destaca los elementos que tus usuarios han comprado recientemente con mayor frecuencia. Por ejemplo, una empresa de comercio electrónico podría recomendar elementos de temporada de los que los usuarios están empezando a abastecerse durante sus preparativos para la próxima temporada.

{% details Requisitos %}
- Recomendaciones de elementos de IA
- Catálogo de elementos relevantes
- Un método para realizar el seguimiento de las compras (ya sea un objeto de compra, un evento de pedido realizado o un evento personalizado)
{% enddetails %}

{% details Configuración %}
1. Crea una [recomendación de elementos de IA]({{site.baseurl}}/ai_item_recommendations).
2. Establece el **Tipo** en **Trending**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación solo a los elementos relevantes.
5. Elige un evento de compra o un evento personalizado que realice un seguimiento de las compras, junto con la propiedad correspondiente.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería.]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations)
{% enddetails %}
{% endtab %}

{% tab "Me gusta" en tendencia %}
Destaca los elementos que han gustado recientemente a tus usuarios con mayor frecuencia. Por ejemplo, una aplicación de música podría presentar artistas prometedores que hayan experimentado un reciente aumento de los "Me gusta" de los usuarios.

{% details Requisitos %}
- Recomendaciones de elementos de IA
- Catálogo de elementos relevantes
- Evento personalizado para el seguimiento de los "Me gusta"
{% enddetails %}

{% details Configuración %}
1. Crea una [recomendación de elementos de IA]({{site.baseurl}}/ai_item_recommendations).
2. Establece el **Tipo** en **Trending**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación solo a los elementos relevantes.
5. Elige tu evento personalizado para el seguimiento de los "Me gusta", junto con la propiedad correspondiente.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería.]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations)
{% enddetails %}
{% endtab %}
{% endtabs %}

### Basado en selecciones {#selections-based}

[Las selecciones]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) son grupos específicos de datos del catálogo. Cuando utilizas una selección, básicamente estás configurando filtros personalizados basados en columnas específicas de tu catálogo. Esto podría incluir filtros por marca, tamaño, ubicación, fecha de adición, etc. Te da el control sobre lo que recomiendas, permitiéndote definir los criterios que deben cumplir los elementos para mostrarse a los usuarios.

Los tres tipos anteriores implican la configuración y el entrenamiento de un modelo de recomendación en Braze. Aunque también puedes utilizar selecciones en esos modelos, también puedes llevar a cabo algunos casos de uso de recomendaciones solo con selecciones de catálogo y personalización de Liquid.

{% alert note %}
Si utilizas selecciones, el campo de clasificación y cualquier límite no se utilizarán con las Recomendaciones de elementos de IA. Esto significa que si creas una selección con un campo de clasificación específico y limitas el número de elementos devueltos, esas restricciones no se utilizarán cuando se procesen las Recomendaciones de elementos de IA.
{% endalert %}

#### Casos de uso

Según los datos de interacción que se estén rastreando, los casos de uso de este modelo podrían incluir la recomendación de:

{% tabs local %}
{% tab Elementos nuevos %}
Este escenario no se basa directamente en las acciones del usuario, sino en los datos del catálogo. Puedes filtrar los elementos nuevos en función de su fecha de incorporación al catálogo y promocionarlos mediante Campaigns dirigidas o Canvas sin necesidad de entrenar un modelo de recomendación.

Por ejemplo, una plataforma de comercio electrónico de tecnología podría alertar a los entusiastas de la tecnología sobre los últimos gadgets o los próximos pedidos anticipados, utilizando filtros para dirigirse a los elementos que se han añadido recientemente al catálogo.

{% details Requisitos %}
- Catálogo de elementos relevantes con un campo para la fecha de adición
{% enddetails %}

{% details Configuración %}
1. Crea una selección basada en tu catálogo. Asegúrate de que tu catálogo tiene un campo de hora (campo con un **Tipo de datos** establecido en **Time**) que corresponde a la fecha en que se añadió el elemento.
2. (Opcional) Añade filtros si lo deseas.
3. Asegúrate de que **Randomize Sort Order** está desactivado.
4. En **Sort Field**, selecciona tu campo de fecha de adición.
5. Establece **Sort Order** en descendente.
6. [Utiliza la selección en mensajería]({{site.baseurl}}/user_guide/data/activation/catalogs/selections#using-selections-in-messaging).
{% enddetails %}
{% endtab %}

{% tab Elementos aleatorios %}
Para una experiencia de usuario diversa, recomendar elementos al azar puede introducir variedad y despertar potencialmente el interés por las áreas menos visitadas del catálogo. Este método no requiere modelos o eventos específicos, sino que utiliza una selección de catálogo para garantizar que los elementos se muestren aleatoriamente.

Por ejemplo, una librería online podría ofrecer la característica "Sorpréndeme", que recomienda un libro al azar basándose en las compras anteriores del usuario o en sus hábitos de navegación, fomentando la exploración fuera de sus géneros de lectura habituales.

{% details Requisitos %}
- Catálogo de elementos relevantes
- Selección con **Randomize Sort Order** activado
{% enddetails %}

{% details Configuración %}
1. [Crea una selección]({{site.baseurl}}/user_guide/data/activation/catalogs/selections#creating-a-selection) basada en tu catálogo.
2. (Opcional) Añade filtros si lo deseas.
3. Activa **Randomize Sort Order**.
4. [Utiliza la selección en mensajería]({{site.baseurl}}/user_guide/data/activation/catalogs/selections#using-selections-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Basado en reglas {#rules-based}

Una herramienta de [recomendaciones basada en reglas]({{site.baseurl}}/rules_based_recommendations) utiliza datos de usuario e información sobre productos para sugerir a los usuarios elementos relevantes dentro de los mensajes. Utiliza Liquid y los catálogos de Braze o Contenido conectado para personalizar dinámicamente el contenido en función del comportamiento y los atributos del usuario.

Las recomendaciones basadas en reglas se basan en una lógica fija que debes establecer manualmente. Esto significa que tus recomendaciones no se ajustarán al historial de compras y los gustos individuales de los usuarios a menos que actualices la lógica; por lo tanto, este método es el más adecuado para recomendaciones que no necesitan actualizaciones frecuentes.

#### Casos de uso

Según los datos de interacción que se estén rastreando, los casos de uso de este modelo podrían incluir:

- **Recordatorios de reabastecimiento:** Enviar recordatorios de reposición de elementos con un ciclo de uso predecible, como las vitaminas mensuales o los comestibles semanales, basándose en su última fecha de compra.
- **Compradores primerizos:** Recomendar kits de iniciación u ofertas introductorias a los compradores primerizos para animarles a una segunda compra.
- **Programas de fidelización:** Destacar los productos que maximizarían los puntos de fidelización o las recompensas de un cliente en función de su saldo de puntos actual.
- **Contenido educativo:** Sugerir nuevos cursos o contenidos basados en los temas de materiales consumidos o adquiridos previamente.

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## Preguntas más frecuentes {#faq}

### ¿Qué hace que los elementos "Most popular" se mezclen con las recomendaciones de otros modelos? {#what-causes-most-popular-items-to-be-mixed-into-other-models-recommendations}

Cuando nuestra herramienta de recomendaciones selecciona una lista para ti, primero da prioridad a las selecciones personalizadas basadas en el modelo específico que has elegido, como "Most recent" o "AI Personalized". Si este modelo no puede completar la lista de 30 recomendaciones por cualquier motivo, se añaden algunos de tus elementos más populares entre todos los usuarios para asegurar que cada usuario tenga siempre un conjunto completo de recomendaciones.

Esto ocurre en algunas condiciones específicas:

- El modelo encuentra menos de 30 elementos que coinciden con tus criterios.
- Los elementos relevantes ya no están disponibles o en stock.
- Los elementos no cumplen los criterios de selección actuales, quizás debido a un cambio en las existencias o en las preferencias del usuario.

Ten en cuenta que las recomendaciones funcionan de forma independiente y no tienen conocimiento de lo que recomiendan los demás modelos. Esto significa que cada sección puede tener elementos duplicados que ya se muestran en otras secciones de recomendaciones de IA en el mismo correo electrónico.

### ¿Cómo puedo evitar elementos duplicados en varias secciones de recomendaciones? {#how-do-i-prevent-duplicate-items-across-multiple-recommendation-sections}

Dado que cada recomendación funciona de forma independiente, el mismo elemento puede aparecer en más de una sección del mismo mensaje. Para eliminar duplicados, utiliza Liquid para hacer seguimiento de los ID de elementos que ya has mostrado y omitirlos en las secciones siguientes.

### ¿Las recomendaciones existentes se entrenan semanalmente después de actualizar a Item Recommendations Pro? {#do-existing-recommendations-train-weekly-after-upgrading-to-item-recommendations-pro}

Sí, pero solo después de la próxima actualización programada. Las recomendaciones existentes no cambian a entrenamiento semanal y predicción diaria inmediatamente después de actualizar a Item Recommendations Pro. Sin embargo, adoptarán el nuevo calendario automáticamente en su próximo ciclo de reentrenamiento. Por ejemplo, si una recomendación se entrenó por última vez el 1 de febrero y está configurada para volver a entrenarse cada 30 días, adoptará el nuevo calendario semanal después de su próxima actualización el 2 de marzo.

### ¿Cómo puedo hacer que todas las recomendaciones que duran varios días caduquen a la vez? {#how-can-i-make-all-recommendations-that-last-multiple-days-expire-at-once}

Si deseas que todas las recomendaciones de varios días caduquen en una fecha específica (para que todas las recomendaciones activas reciban nuevas predicciones a la vez), ponte en contacto con el soporte de Braze o con tu administrador del éxito del cliente para obtener ayuda. Los expertos de BrazeAI realizan esta tarea manualmente para garantizar el máximo rendimiento del modelo.

### ¿Qué ocurre si actualizo el nombre de la propiedad de una recomendación de elementos de IA activa? {#what-happens-if-i-update-the-property-name-for-an-active-ai-item-recommendation}

Cuando actualizas el nombre de la propiedad (ruta del ID del elemento) y seleccionas **Guardar y construir**, Braze inicia un trabajo de reentrenamiento en segundo plano que analiza los últimos seis meses de datos de interacción utilizando el nuevo mapeado.

Mientras el modelo se reentrena, los usuarios siguen viendo las recomendaciones de la versión anterior. Las recomendaciones no cambian hasta que el nuevo modelo finaliza el entrenamiento con éxito. Esto significa:

- Los usuarios ven elementos personalizados del modelo anterior (o la alternativa global si no tienen recomendaciones específicas).
- No hay tiempo de inactividad ni vacíos en las recomendaciones durante el proceso de reentrenamiento.
- La transición del modelo anterior al nuevo es fluida una vez que el entrenamiento se completa con éxito.

Los eventos con la ruta de ID de elemento anterior se ignoran para el nuevo modelo. Solo se incluyen en el reentrenamiento los eventos que utilizan el nuevo mapeado de nombre de propiedad.

### ¿Qué ocurre si el trabajo de reentrenamiento falla después de cambiar el nombre de la propiedad? {#what-happens-if-the-retraining-job-fails-after-changing-the-property-name}

{% alert important %}
Si el trabajo de reentrenamiento falla, toda la recomendación de elementos entra en un estado deshabilitado (no activo). Dado que Braze actualmente no recurre al último modelo entrenado con éxito en caso de fallo del entrenamiento, cualquier Liquid que haga referencia a esta recomendación fallará y los mensajes asociados no se enviarán.
{% endalert %}

Para reducir este riesgo, considera el siguiente enfoque:

1. Crea una nueva recomendación de elementos con la configuración de nombre de propiedad deseada.
2. Verifica que el entrenamiento se complete con éxito.
3. Actualiza tu mensajería para hacer referencia a la nueva recomendación en lugar de modificar directamente una recomendación activa.

Este enfoque te permite probar la nueva configuración sin arriesgar la interrupción de los mensajes que hacen referencia a tu recomendación existente.