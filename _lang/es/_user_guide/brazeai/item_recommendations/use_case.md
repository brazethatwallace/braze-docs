---
nav_title: Casos de uso
article_title: "Caso de uso: impulsar el descubrimiento de contenido tras la visualización"
description: "Este ejemplo muestra cómo una marca ficticia utiliza las Recomendaciones de elementos de IA de Braze para entregar contenido personalizado y sugerencias de productos en momentos clave para los clientes."
page_type: tutorial
---

# Caso de uso: impulsar el descubrimiento de contenido tras la visualización {#use-case-drive-content-discovery-after-viewing}

> Este ejemplo muestra cómo una marca ficticia utiliza las Recomendaciones de elementos de IA de Braze para entregar contenido personalizado y sugerencias de productos en momentos clave para los clientes. Descubre cómo la lógica de recomendación puede mejorar la interacción, aumentar las conversiones y reducir el esfuerzo manual.

Supongamos que Camila es administradora de CRM en MovieCanon, una plataforma de streaming que ofrece películas y series seleccionadas.

El objetivo de Camila es mantener la interacción de los espectadores después de que terminen de ver algo. Históricamente, los mensajes «También te puede interesar» de MovieCanon se basaban en una amplia coincidencia de géneros y se enviaban en momentos arbitrarios, a menudo horas o días después de una sesión. La interacción era baja, y su equipo sabía que podía hacerlo mejor.

Mediante las [Recomendaciones de elementos de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/), Camila configura un sistema que recomienda automáticamente nuevos títulos en función del historial de visualización de cada espectador, entregados inmediatamente después de que el usuario termine de ver una película o un episodio. Es una forma más inteligente y personalizada de ayudar a los usuarios a descubrir contenido que realmente querrán ver a continuación y mantenerlos en interacción con la plataforma.

![Mensaje dentro de la aplicación que dice «Lo siguiente, solo para ti. Porque viste "Nomads of the Sun"», con una imagen, el nombre del título, una descripción y una llamada a la acción para «Ver ahora» o «Saltar» a la siguiente recomendación.]({% image_buster /assets/img/ai_use_cases/recommendation_rendered.png %})

Este tutorial explica cómo Camila:

- Crea un mensaje personalizado que se activa cuando un usuario termina de ver algo
- Configura recomendaciones adaptadas a las preferencias del espectador, extraídas automáticamente del catálogo de MovieCanon e insertadas en el mensaje

## Paso 1: Crear una recomendación {#step-1-create-a-churn-prediction-model}

Camila comienza creando una recomendación que mostrará títulos relevantes cada vez que un usuario termine de ver algo. Quiere que sea dinámica, para que los usuarios reciban diferentes sugerencias basadas en lo que han visto recientemente.

1. En el dashboard de Braze, Camila accede a **Recomendaciones de elementos de IA**.
2. Crea una nueva recomendación y la titula «Sugerencias tras la visualización».
3. Para el tipo de recomendación, elige **AI Personalized**, de modo que cada usuario vea recomendaciones personalizadas basadas en comportamientos anteriores.
4. Selecciona **Do not recommend items users have previously interacted with** para que no reciban recomendaciones de algo que ya hayan visto.
5. Selecciona el catálogo que contiene la biblioteca de contenidos actual de MovieCanon. Camila no añade una selección de catálogo, ya que quiere que todos los elementos del catálogo sean elegibles para recomendación.
6. Camila vincula la recomendación al evento personalizado `Watched Content`, que realiza un seguimiento de las visualizaciones completadas, y establece el **Property Name** como el título del contenido.
7. Crea la recomendación.

## Paso 2: Configurar un mensaje dentro de la aplicación {#step-2-set-up-an-in-app-message}

Una vez finalizado el entrenamiento de la recomendación, Camila crea un flujo de mensajería que llega al usuario en el momento adecuado: inmediatamente después de que termine un título. El mensaje incluye una lista de tres sugerencias personalizadas extraídas directamente del catálogo.

1. Camila crea una Campaign de mensajes dentro de la aplicación utilizando el editor de arrastrar y soltar.
2. Configura el desencadenante con su evento personalizado: `Watched Content`.
3. Diseña un mensaje dentro de la aplicación de varias páginas con imágenes de título, nombres y una llamada a la acción «Ver ahora».

![Modal «Add Personalization» abierto en el editor de Braze, con «Item recommendation» seleccionado como tipo de personalización.]({% image_buster /assets/img/ai_use_cases/recommendation_add_personalization.png %})

{: start="4"}

4. En el cuerpo del mensaje, Camila utiliza el [modal Add Personalization]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/#inserting-pre-formatted-variables) para añadir variables como el nombre, la descripción y la miniatura del título recomendado utilizando Liquid, que rellena dinámicamente el contenido del catálogo. Crea una plantilla con un atributo personalizado para `Last Watched Movie` para que los usuarios sepan que esta recomendación se basa en su historial de visualizaciones.

![Editor de mensajes dentro de la aplicación con Liquid sin procesar para crear plantillas en campos específicos a partir de elementos del catálogo de la recomendación.]({% image_buster /assets/img/ai_use_cases/recommendation_liquid.png %})

{% details Mostrar el Liquid utilizado en la imagen %}

{% raw %}

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].name }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].description }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].thumbnail }}
```

{% endraw %}

{% enddetails %}

{: start="5"}

5. A continuación, Camila duplica su página e incrementa la matriz Liquid {% raw %}(`{{ items[0]}}` a `{{items[1]}}`){% endraw %} en cada variable para crear una plantilla con el siguiente elemento de la lista de recomendaciones.

## Paso 3: Medir y optimizar {#step-3-measure-and-optimize}

Una vez lanzada la Campaign, Camila supervisa las tasas de apertura, los CTR y el comportamiento de visualización posterior. Compara el rendimiento con Campaigns de recomendación estáticas anteriores y observa una mayor interacción y más sesiones de contenido por usuario.

También tiene previsto realizar pruebas A/B:

- Momento de envío (inmediato frente a 10 minutos después de la visualización)
- Diseño del contenido (carrusel frente a lista)
- Variaciones de CTA («Ver ahora» frente a «Añadir a la cola»)

Al combinar la mensajería basada en eventos con las Recomendaciones de elementos de IA, Camila convierte el descubrimiento de contenido en una experiencia automática y personalizada. MovieCanon mantiene la interacción de los usuarios sin conjeturas, entregando contenido relevante en el momento adecuado para impulsar la profundidad de la sesión y reducir la tasa de abandonos.