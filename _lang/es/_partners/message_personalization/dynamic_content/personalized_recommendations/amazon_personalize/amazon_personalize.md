---
nav_title: Amazon Personalizar
article_title: Amazon Personalizar
alias: "/partners/amazon_personalize_overview/"
description: "Este artículo de referencia describe una arquitectura de referencia para la integración entre Braze y Amazon Personalize. Este artículo de referencia te ayudará a comprender los casos de uso que ofrece Amazon Personalize, los datos con los que trabaja, cómo configurar el servicio y cómo integrarlo con Braze."
page_type: partner
search_tag: Partner
---

# Amazon Personalizar {#amazon-personalize}
<!--
{% multi_lang_include video.html id="xFZ3HMleYYE" align="right" %}
-->
> [Amazon Personalize](https://aws.amazon.com/personalize/) es como tener tu propio sistema de recomendación de aprendizaje automático de Amazon durante todo el día. Basado en más de 20 años de experiencia en recomendaciones, Amazon Personalize te permite mejorar la interacción con los clientes mediante recomendaciones personalizadas de productos y contenidos en tiempo real y promociones de marketing específicas.

_Esta integración es mantenida por Amazon Personalize._

## Sobre la integración {#about-the-integration}

Mediante el aprendizaje automático y un algoritmo que tú ayudas a definir, Amazon Personalize puede ayudarte a entrenar un modelo que produzca recomendaciones de alta calidad para tus sitios web y aplicaciones. Estos modelos te permitirán crear listas de recomendaciones basadas en los comportamientos anteriores de los usuarios, ordenar los elementos por relevancia y recomendar otros elementos en función de la similitud. Las listas obtenidas de la API de Amazon Personalize pueden utilizarse en contenido conectado de Braze para ejecutar campañas de recomendación personalizadas de Braze. Al integrarse con Amazon Personalize, los clientes tienen libertad para controlar los parámetros utilizados para entrenar los modelos y definir objetivos empresariales opcionales que optimicen el resultado del algoritmo.

Este artículo de referencia te ayudará a comprender los casos de uso que ofrece Amazon Personalize, los datos con los que trabaja, cómo configurar el servicio y cómo integrarlo con Braze.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta de Amazon Web Service | Se necesita una cuenta de AWS para beneficiarse de esta asociación. Después de tener una cuenta de AWS, puedes acceder a Amazon Personalize a través de la consola de Amazon Personalize, la interfaz de línea de comandos de AWS (CLI de AWS) o los SDK or kit de desarrollo de software de AWS. |
| Casos de uso definidos | Antes de crear un modelo, debes determinar tu caso de uso para esta integración. Consulta la siguiente lista de casos de uso comunes. |
| Conjuntos de datos | Los modelos de recomendación de Amazon Personalize requieren tres tipos diferentes de conjuntos de datos: interacciones, usuarios y artículos. Consulta los siguientes detalles para ver los requisitos de cada conjunto de datos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

{% tabs %}
{% tab Use Cases %}

**Casos de uso**

Antes de crear un modelo, debes determinar tu caso de uso para esta integración. Algunos casos de uso habituales son:
- Recomendar artículos a los usuarios basándose en sus interacciones anteriores, creando una experiencia verdaderamente personalizada para tus usuarios.
- Proporcionar una lista de artículos o resultados de búsqueda adaptados a cada usuario, aumentando la interacción al mostrar artículos por relevancia para el usuario.
- Encontrar recomendaciones de artículos similares, ayudando a los usuarios a descubrir cosas nuevas.

En la siguiente guía, nos centraremos en la receta de recomendaciones personalizadas para el usuario.

{% endtab %}
{% tab Datasets %}

**Conjuntos de datos**

Para comenzar a utilizar los modelos de recomendación de Amazon Personalize, necesitas tres tipos de conjuntos de datos:

- Interacciones
  - Almacena el historial de interacciones entre usuarios y artículos
  - Requiere los valores `USER_ID`, `ITEM_ID`, `EVENT_TYPE` y `TIMESTAMP` y opcionalmente acepta metadatos sobre el evento
- Usuarios
  - Almacena metadatos sobre los usuarios
  - Requiere un valor `USER_ID` y al menos un campo de metadatos (cadena o numérico) como sexo, edad, fidelización
- Elementos
  - Almacena metadatos sobre los artículos
  - Requiere un `ITEM_ID` y al menos un campo de metadatos (textual, categórico o numérico) que describa el artículo

Para una receta de recomendaciones de usuario, debes proporcionar un conjunto de datos de interacciones que contenga al menos 1000 puntos de datos de interacción de al menos 25 usuarios únicos con al menos dos interacciones cada uno. Estos conjuntos de datos pueden cargarse en bloque utilizando archivos CSV almacenados en S3 o de forma incremental a través de la API.

{% endtab %}
{% endtabs %}

## Creación de modelos {#creating-models}

### Paso 1: Entrenamiento {#step-1-training}

Una vez importados los conjuntos de datos, puedes crear una solución. Una solución utiliza una de las [recetas](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html) (algoritmos) de Amazon Personalize para entrenar un modelo. En nuestro caso, utilizaremos la receta `USER_PERSONALIZATION`. El entrenamiento de la solución crea una versión de la solución (modelo entrenado) que puedes evaluar en función de las métricas de rendimiento del modelo.

Amazon Personalize te permite ajustar los hiperparámetros que el modelo utiliza para entrenarse. Por ejemplo:
- El parámetro "User history length percentile" que se encuentra en la consola de Amazon Personalize permite ajustar el percentil del historial de usuario que se incluirá en el entrenamiento:<br><br>![Configuración del perfil de usuario mín./máx.]({% image_buster /assets/img/amazon_personalize/min_and_max_user_percentile.png %})
  - `min_user_history_length_percentile`: excluye un porcentaje de usuarios con historiales muy cortos, lo que puede ser útil para eliminar artículos populares y elaborar recomendaciones basadas en patrones subyacentes más profundos.
  - `max_user_history_length_percentile`: ajusta el porcentaje de usuarios a tener en cuenta cuando se entrena con longitudes de historial muy largas.

El número de dimensiones ocultas ayuda a detectar patrones más complicados para conjuntos de datos complejos, mientras que la técnica de retropropagación a través del tiempo (BPTT) ajusta las recompensas para un evento temprano después de que se produjera una cadena de eventos que dio lugar a una acción de alto valor.

Además, Amazon Personalize ofrece un ajuste automático de hiperparámetros mediante la ejecución simultánea de varias versiones de la solución con diferentes valores. Para utilizar el ajuste, activa **Perform HPO** al crear una solución.

### Paso 2: Evaluar y comparar {#step-2-evaluate-and-compare}

Una vez finalizado el entrenamiento de una solución, estás listo para evaluarla y comparar diferentes versiones. Cada versión de la solución muestra las métricas calculadas. Algunas de las métricas disponibles son:

- **Ganancia acumulada descontada normalizada:** compara el orden recomendado de los elementos con la lista real de elementos y asigna a cada elemento un peso correspondiente a su posición en la lista.
- **Precisión @k:** la cantidad de artículos recomendados correctamente dividida por la cantidad de todos los artículos recomendados, donde `k` es el número de artículos.
- **Rango recíproco medio:** se centra en la primera recomendación mejor clasificada y calcula cuántos artículos recomendados se ven antes de que aparezca la primera recomendación coincidente.
- **Cobertura:** proporción de elementos únicos recomendados con respecto al número total de elementos únicos del conjunto de datos.

## Obtener recomendaciones {#getting-recommendations}

Una vez que hayas creado una versión de la solución con la que estés satisfecho, es hora de poner en práctica las recomendaciones. Hay dos formas de acceder a las recomendaciones:

1. Campaña en tiempo real<br>Una campaña es una versión de la solución desplegada con un rendimiento mínimo de transacciones definido. Una transacción es una única llamada a la API para obtener la salida de la recomendación, y se define como TPS, o transacciones por segundo, con un valor mínimo de uno. La campaña escalará recursos en caso de un aumento de la carga, pero no caerá por debajo de tu valor mínimo. Puedes consultar las recomendaciones en la consola, en la CLI de AWS o a través de los SDK or kit de desarrollo de software de AWS en tu código.<br><br>
2. Trabajo por lotes<br>Un trabajo por lotes exporta las recomendaciones a un contenedor de S3. La tarea toma como entrada un archivo JSON con una lista de ID de usuario para los que deseas exportar las recomendaciones. A continuación, tras especificar los permisos correctos y el destino de salida, estarás listo para ejecutar el trabajo. El tiempo de ejecución depende del tamaño de los conjuntos de datos y de la longitud de la lista de recomendaciones.

### Filtros {#filters}

Los filtros permiten ajustar el resultado de la recomendación excluyendo elementos en función del ID del elemento, el tipo de evento o los metadatos. También puedes filtrar a los usuarios en función de sus metadatos, como la edad o el estado de fidelización. Los filtros pueden resultar útiles para evitar que se recomienden artículos con los que el usuario ya ha interactuado.

## Integración de resultados con Braze {#integrating-results-with-braze}

Con el modelo creado y la campaña de recomendaciones, estás listo para ejecutar una campaña de Braze para tus usuarios utilizando Content Cards y contenido conectado.
Antes de ejecutar una campaña de Braze, debes crear un servicio que pueda servir estas recomendaciones a través de una API. Puedes seguir [el paso 3 del artículo del taller]({{site.baseurl}}/partners/amazon_personalize_workshop#step-3-send-personalized-emails-from-braze) para desplegar el servicio utilizando los servicios de AWS. También puedes desplegar tu propio servicio backend independiente que proporcione las recomendaciones.

### Caso de uso de la campaña de Content Cards {#content-card-campaign-use-case}

Realicemos una campaña de Content Cards con el primer elemento recomendado de la lista.<br><br>
En los siguientes ejemplos, vamos a consultar
el endpoint `GET http://<service-endpoint.com>/recommendations?user_id=user123` con un parámetro `user_id` que devolverá una lista de elementos recomendados:

```json
[
  {
    "id": "abc123",
    "url": "http://productpage.com/product/abc123",
    "name": "First Item",
    "price": 39.99,
    "image": "http://pp.cdn.com/abvh3321pjb1j"
  },
  {
    "id": "xyz987",
    "url": "http://productpage.com/product/xyz987",
    "name": "Great Item",
    "price": 19.99,
    "image": "http://pp.cdn.com/234bjl1gioj1b2b"
  },
  ...
]
```

En el panel de Braze, crea una nueva [campaña de Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card). En el campo de texto del mensaje, crea un bloque Liquid de contenido conectado para consultar la API y guardar la respuesta en la variable `recommendations`:

{% raw %}

```liquid
{% connected_content https:/<service-endpoint.com>/recommendations?user_id={{${user_id}}} :save recommendations %}
```

A continuación, puedes hacer referencia al primer elemento de la matriz resultante y mostrar el contenido al usuario:

```liquid
This seems like a great fit for you:
{% recommendations[0].name %}
{% recommendations[0].price %}
```

{% endraw %}

Incluyendo el título, la imagen y enlazando la URL, así es como quedaría la Content Card completa:

![Una imagen de una campaña con contenido conectado añadido al cuerpo del mensaje y al campo "Añadir imagen". Esta imagen también muestra la lógica de contenido conectado añadida al campo "Redirect to Web URL", que enlaza a los usuarios con una URL de recomendación.]({% image_buster /assets/img/amazon_personalize/content-card-campaign.png %})