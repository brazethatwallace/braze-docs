---
nav_title: Paso de IA
article_title: Paso de IA
permalink: /ai_step/
description: "Este artículo de referencia cubre el paso de IA en Canvas."
tool:
  - Canvas
hidden: true
---

# Paso de IA {#ai-step}

> El paso de IA dentro de Canvas aprovecha ChatGPT para automatizar el marketing personalizado interpretando las entradas generadas por los usuarios (como comentarios de cuestionarios), determinando la respuesta adecuada y desencadenando mensajes, todo dentro de Braze. ChatGPT funciona con OpenAI, un tercero.

{% alert note %}
El paso de IA está disponible actualmente como característica beta. Ponte en contacto con tu administrador del éxito del cliente si te interesa participar en esta prueba beta.
{% endalert %}

## Crear un paso de IA {#create-ai-step}

1. Añade un nuevo paso a tu Canvas y selecciona **Paso de IA**. <br><br>![Paso de IA en el constructor de Canvas][1]{: style="max-width: 30%;"}<br><br>
2. Crea un prompt que indique a la IA cómo responder a las distintas acciones de los usuarios. Las respuestas pueden incluir la actualización de un atributo personalizado o el envío de un mensaje. Este prompt puede utilizar Liquid para asignar diferentes resultados de respuesta en función de distintos atributos o entradas de los usuarios. <br><br>Para asignar resultados que luego puedan utilizarse para personalizar futuros mensajes dentro del mismo Canvas, crea un prompt que guarde variables con nombres específicos (por ejemplo, "message" y "sentiment score"). <br><br> ![Ejemplo de prompt de IA utilizado en la configuración del paso de IA para enviar un mensaje personalizado basado en una puntuación de sentimiento generada. Este ejemplo se indica en la sección "Respuestas de sentimiento del cliente".][2] <br><br>
3. Usa la pestaña **Vista previa** para probar lo que la IA podría generar para usuarios específicos.<br><br> ![La pestaña Vista previa de la configuración del paso de IA mostrando un mensaje personalizado generado por IA para tres parámetros: un nombre de Cameron, un nombre de producto de shoes y el texto "decent but my shoe lace already broke"][3]

## Hacer referencia a la salida de IA usando Liquid {#referencing-ai-output-using-liquid}

Haz referencia a la salida de IA en pasos posteriores insertando la lógica Liquid `{% raw %}{{ai_step_output.${key_name}}}{% endraw %}`. Puedes establecer el `key_name` dentro del prompt en el paso de IA.

Por ejemplo, si utilizas las variables "message" y "sentiment score", puedes usar `{% raw %}{{ai_step_output.${message}}}{% endraw %}` para personalizar un mensaje posterior en ese mismo Canvas.

También puedes registrar la salida de cualquier paso de IA como un atributo personalizado utilizando el paso en Canvas de Actualización de usuario, donde lees la salida del paso de IA (por ejemplo, `{% raw %}{{ai_step_output.${sentiment_score}}}{% endraw %}`). Si la salida no se almacena como un atributo personalizado, no podrá utilizarse en ningún otro lugar aparte de los pasos posteriores del mismo Canvas.

### Usar pasos de contexto {#using-context-steps}

Puedes aprovechar los [pasos de contexto de Canvas](https://www.braze.com/docs/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works) para hacer referencia fácilmente a las salidas más adelante en tu Canvas.

A continuación se muestra un ejemplo de paso de contexto que podrías configurar después de tu paso de IA. En este ejemplo, un paso de IA anterior contiene las salidas del paso de IA para la puntuación de sentimiento y el mensaje, y este paso de contexto crea las variables `sentiment_score` y `message`, que pueden utilizarse en pasos posteriores.

![Paso de contexto con las dos variables: "sentiment_score" y "message".][6]

También podrías crear un paso de Rutas de audiencia que envíe a los usuarios por diferentes rutas en función del valor de sus variables de contexto. En este ejemplo, podrías dirigirte a los usuarios de forma diferente según su puntuación de sentimiento. También puedes usar Liquid para incorporar la variable de mensaje en el cuerpo de un correo electrónico insertando la variable con {% raw %}`{{context.${message}}}`{% endraw %}.

![Un paso de ruta de audiencia con un grupo de audiencia llamado "Group 1" con el filtro "sentiment_score is more than 80".][7]

## Métricas del paso de IA {#ai-step-metrics}

Los pasos de IA tienen las siguientes métricas a nivel de paso:

| Métrica | Descripción |
| _Avanzó al siguiente paso_ | Número de usuarios que avanzaron a los pasos siguientes en el Canvas |
| _Salió del Canvas_ | Número de usuarios que salieron del Canvas si tu paso de IA fue el último paso |
| _Salida generada correctamente_ | Número de usuarios para los que el paso de IA generó una salida correctamente |
| _Error en la generación de salida_ | Número de usuarios para los que el paso de IA no pudo generar una salida; en ese caso, los usuarios seguirán avanzando a los pasos posteriores |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comprender las salidas de tu paso de IA {#understanding-your-ai-step-outputs}

Hay algunos escenarios en los que Braze descartará la salida del paso de IA y enviará al cliente al siguiente paso:

- Si la salida supera los 1024 caracteres
- Si la salida no está en formato JSON
- Si el prompt no cumple los requisitos de [moderación](https://platform.openai.com/docs/guides/moderation/overview) de OpenAI, que marca el contenido inapropiado generado por los usuarios

## Casos de uso del paso de IA {#ai-step-use-cases}

### Respuestas de sentimiento del cliente {#customer-sentiment-responses}

Como se demuestra en el ejemplo de [Crear un paso de IA](#create-ai-step), puedes pedir a la IA que envíe mensajes de seguimiento basados en puntuaciones de sentimiento generadas a partir de los comentarios de los clientes.

- **Puntuaciones de sentimiento positivas:** Desencadenar una notificación push que pida a los usuarios que dejen una reseña
- **Puntuaciones de sentimiento medias:** Desencadenar un correo electrónico que pregunte a los usuarios si desean ayuda adicional
- **Puntuaciones de sentimiento bajas:** Desencadenar un webhook que notifique al servicio de asistencia al usuario para que un representante de soporte pueda elaborar un seguimiento detallado

#### Ejemplo de prompt de IA {#example-ai-prompt}

Este ejemplo se utilizó en [Crear un paso de IA](#create-ai-step).

A customer has purchased "`{% raw %}{{canvas_entry_properties.${product_name}}}{% endraw %}`", and given the product feedback: "`{% raw %}{{canvas_entry_properties.${text}}}{% endraw %}`". Create a sentiment score as an integer between 0 to 100. Then create a personalized message. This should return two variables, "message" and "sentiment score."

### Seguimientos de cuestionarios {#survey-follow-ups}

Si ejecutas un cuestionario dentro de la aplicación o del navegador con una sección de respuesta libre, puedes usar pasos de IA para analizar las respuestas libres y hacer un seguimiento adecuado.

Por ejemplo, si un comercio minorista de maquillaje tiene un cuestionario que pregunta "¿Qué productos te gustaría nominar para los premios de belleza de este año?", podría usar un prompt que identifique y asigne un atributo para los tipos de productos y marcas favoritos del usuario, y luego personalizar el contenido futuro basándose en estos datos.

#### Ejemplo de prompt de IA

Identify the user's favorite brand using their response. Then create a message that thanks users for filling out the survey and mentions how Beauty Experts also love their favorite brand. This should return two variables, "message" and "favorite brand."

![Pestaña Vista previa de la configuración del paso de IA mostrando un mensaje personalizado generado por IA para el parámetro de respuesta del cuestionario "I love Beauty Brand face creams" que agradece al usuario por completar el cuestionario y luego recomienda una crema facial.][4]

### Recomendaciones basadas en el comportamiento {#behavior-driven-recommendations}

Los clientes pueden pedir a la IA que analice los comportamientos de los usuarios y envíe mensajes de recomendación.

Por ejemplo, puedes crear un prompt para analizar las 50 compras más recientes de los usuarios y establecer su categoría más comprada como un nuevo atributo personalizado. Luego, puedes enviar recomendaciones personalizadas por correo electrónico para la categoría favorita de cada usuario.

#### Ejemplo de prompt de IA

A customer has purchased the following products: "`{% raw %}{{custom_attribute.${Products Purchased}}}{% endraw %}`". Identify the user's most purchased product category. This should return a new variable for "most purchased category."

![Pestaña Vista previa de la configuración del paso de IA mostrando la variable generada por IA de "book" para el parámetro de categoría más comprada.][5]

## Límites de velocidad {#rate-limits}

Hay un límite de 10 solicitudes por minuto (RPM) por empresa. Esto significa que para cualquier paso de IA, hasta 10 usuarios pueden recibir ese paso durante un minuto determinado y cualquier usuario que supere los 10 avanzará automáticamente al siguiente paso. Cuando comience el siguiente minuto, los usuarios podrán recibir de nuevo el paso de IA, pero los usuarios anteriores que activaron el límite de velocidad no se reintentarán.

## Limitaciones del paso de IA {#ai-step-limitations}

- Esta característica aprovecha GPT-3.5.
- Esta característica utiliza la clave de API de OpenAI de Braze. No puedes usar tu propia clave de API de OpenAI.
- Hay un límite de 5 solicitudes por minuto (RPM) por espacio de trabajo y 10 RPM por empresa.
- Esta característica no cumple con HIPAA y los clientes no deben enviar ninguna información de identificación personal (PII) ni información de salud protegida (PHI).

## ¿Cómo se utilizan y envían mis datos a OpenAI? {#how-is-my-data-used-and-sent-to-openai}

Para generar salidas de IA a través de las características de BrazeAI que Braze identifica como que aprovechan OpenAI ("Salida"), Braze enviará tu prompt, como el contenido del mensaje, el sentimiento del usuario final, las directrices de marca, los datos de campañas anteriores o cualquier otra entrada, según corresponda ("Entrada") a [OpenAI](https://openai.com/). Si se envían datos personales a OpenAI cuando utilizas la integración de ChatGPT de Braze con el paso de IA, OpenAI actuará como subprocesador de Braze, según lo establecido en el DPA entre tú y Braze. Si integras tu propio modelo de lenguaje grande (LLM) con el paso de IA, cualquier proveedor de dicho LLM se considerará un proveedor externo y el procesamiento de cualquier dato personal estará sujeto a los términos entre tú y dicho proveedor externo. Según los [compromisos de la plataforma API de OpenAI](https://openai.com/enterprise-privacy/), los datos enviados a la API de OpenAI a través de Braze no se utilizan para entrenar ni mejorar los modelos de OpenAI y serán eliminados por OpenAI de sus sistemas después de 30 días. Entre tú y Braze, la Salida es tu propiedad intelectual. Braze no reclamará ningún derecho de autor sobre dicha Salida. Braze no ofrece ninguna garantía de ningún tipo con respecto a cualquier contenido generado por IA en general, incluida la Salida.

[1]: {% image_buster /assets/unlisted_docs/img/ai_step1.png %}
[2]: {% image_buster /assets/unlisted_docs/img/ai_step2.png %}
[3]: {% image_buster /assets/unlisted_docs/img/ai_step3.png %}
[4]: {% image_buster /assets/unlisted_docs/img/ai_step4.png %}
[5]: {% image_buster /assets/unlisted_docs/img/ai_step5.png %}
[6]: {% image_buster /assets/unlisted_docs/img/ai_step6.png %}
[7]: {% image_buster /assets/unlisted_docs/img/ai_step7.png %}