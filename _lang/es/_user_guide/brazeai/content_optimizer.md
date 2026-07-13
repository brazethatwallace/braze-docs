---
nav_title: Optimizador de contenidos
article_title: Optimizador de contenidos
alias: "/content_optimizer/"
description: "El Optimizador de contenidos es un agente que te ayuda a probar y optimizar el contenido de los mensajes a gran escala, utilizando la inteligencia artificial para generar y evaluar automáticamente grandes volúmenes de variantes de contenido."
page_type: reference
page_order: 3
---

# Optimizador de contenidos {#content-optimizer}

> El Optimizador de contenidos es un agente que te ayuda a probar y optimizar el contenido de los mensajes a gran escala, utilizando la inteligencia artificial para generar y evaluar automáticamente grandes volúmenes de variantes de contenido.

{% alert important %}
El Optimizador de contenidos se encuentra actualmente en fase beta y solo está disponible para estos canales: correo electrónico, notificaciones push y mensajes SMS/MMS/RCS. Para obtener ayuda para empezar, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

## Acerca del Optimizador de contenidos {#about-content-optimizer}

El Optimizador de contenidos es un agente que se ejecuta en un paso en Canvas. Te ayuda a definir los componentes del mensaje que deseas probar, generar variantes mediante IA generativa o entrada manual, y optimizar automáticamente las combinaciones de contenido que se envían a los usuarios. Esta característica te ayuda a:

- Optimizar las líneas del asunto, el encabezado del cuerpo, el contenido del cuerpo o la llamada a la acción principal de los correos electrónicos.
- Optimizar títulos y mensajes de las notificaciones push.
- Optimizar ganchos, cuerpos y llamadas a la acción de los mensajes SMS, MMS y RCS.
- Mejorar continuamente el rendimiento de los mensajes sin necesidad de configurar pruebas A/B manuales.
- Probar rápidamente grandes volúmenes de variantes de contenido, aprovechando la inteligencia artificial para la ideación.
- Eliminar automáticamente el contenido de bajo rendimiento y ampliar el contenido más exitoso.

Aprende a crear un [paso de Optimizador de contenidos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step).

## Casos de uso {#use-cases}

### Correo electrónico {#email}

| Caso de uso de optimización | Objetivo | Descripción |
| --- | --- | --- |
| Variaciones en la línea del asunto | Aumentar la tasa de apertura | Prueba el tono, la urgencia, la personalización y el uso de emojis. |
| Estilos de mensajería del encabezado | Aumentar la interacción | Compara los mensajes emocionales, basados en valores y claros en el encabezado del cuerpo. |
| Formato del contenido del cuerpo | Mejorar la legibilidad y la interacción | Prueba la narración frente a las listas de características, las viñetas frente a los párrafos y la longitud del contenido. |
| Texto y tono de la llamada a la acción (CTA) | Aumentar los click-throughs | Compara frases de llamada a la acción orientadas a la acción, centradas en los beneficios y en primera persona. |
| Combinaciones de contenidos temáticos | Descubrir combinaciones de alto rendimiento | Combina y mezcla los componentes temáticos del asunto, el cuerpo y la llamada a la acción para encontrar la mejor combinación global. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Correo electrónico" }

### Notificaciones push {#push-notifications}

| Caso de uso de optimización | Objetivo | Descripción |
| --- | --- | --- |
| Variaciones del título | Aumentar la tasa de apertura | Prueba la claridad, la urgencia, la personalización y el tono en el título de la notificación push. |
| Estilos del texto del cuerpo | Mejorar la interacción | Compara mensajes concisos, orientados a los beneficios y orientados a la acción en el cuerpo de la notificación push. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Notificaciones push" }

### Mensajes SMS, MMS y RCS {#sms-mms-and-rcs-messages}

| Caso de uso de optimización | Objetivo | Descripción |
| --- | --- | --- |
| Variaciones del gancho | Aumentar la interacción | Prueba la urgencia, la personalización y el tono en la primera línea que se muestra en las vistas previas de SMS, los pies de foto de MMS o las introducciones de RCS. |
| Estilos del texto del cuerpo | Mejorar la interacción | Compara mensajes concisos y orientados a la acción en el cuerpo, incluyendo el texto que acompaña a los medios en MMS y RCS. |
| Variaciones del texto de la llamada a la acción (CTA) | Aumentar los click-throughs | Compara frases de llamada a la acción orientadas a la acción y conversacionales para enlaces y solicitudes de siguiente paso en SMS, MMS y RCS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mensajes SMS, MMS y RCS" }

## Cómo funciona {#how-it-works}

El Optimizador de contenidos utiliza un algoritmo [bandido multiarma](https://en.wikipedia.org/wiki/Multi-armed_bandit) no contextual para asignar más envíos a las variantes de alto rendimiento y reducir la asignación a las de bajo rendimiento. Con el tiempo, esto se traduce en una mejora continua del contenido de tus mensajes, con una intervención manual mínima.

El algoritmo de optimización bandido patentado de Braze se ha diseñado específicamente para la naturaleza combinatoria del paso del Optimizador de contenidos. Dado que cada mensaje se compone de varios componentes, el bandido aprende simultáneamente sobre el rendimiento de cada componente (como la línea del asunto, el cuerpo del mensaje o la llamada a la acción) y sobre sus interacciones cuando se combinan en un mensaje. Más concretamente, cuando se envía una combinación determinada, todas las combinaciones que comparten los mismos componentes se benefician de los datos de ese envío. Esto permite que el bandido aprenda mucho más rápido con la misma cantidad de datos, en comparación con un algoritmo bandido estándar.

Cuando se inicia el paso por primera vez, el Optimizador de contenidos envía variantes aleatoriamente para recopilar datos de rendimiento iniciales. Tras este periodo inicial de exploración, el algoritmo comienza a desviar el tráfico hacia combinaciones de contenido con mejor rendimiento, reduciendo gradualmente la asignación a las opciones con peor rendimiento. Durante el periodo de exploración, el tráfico se distribuye generalmente entre las variantes disponibles para permitir que el algoritmo aprenda de su rendimiento relativo.

El Optimizador de contenidos es similar al paso Mensaje de Canvas, con características como horas tranquilas, [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) y registro de eventos. Puedes configurar un paso de Optimizador de contenidos creando un mensaje base y definiendo qué componentes del contenido (como la línea del asunto, el cuerpo del texto o la llamada a la acción) deseas optimizar. Las variantes de cada componente pueden generarse con IA o introducirse manualmente, y deben añadirse etiquetas de Liquid al mensaje base para mapear los componentes al contenido del mensaje.

Cada usuario recibe un mensaje por cada entrada en el paso del Optimizador de contenidos. Las reentradas se tratan como nuevas, sin memoria de variantes anteriores.

## Configuración de entrada en Canvas {#canvas-entry-setup}

Para obtener los mejores resultados, utiliza el Optimizador de contenidos en Canvas donde los usuarios entren en el paso de forma gradual y regular a lo largo del tiempo, como en Canvas recurrentes o siempre activos con un volumen diario constante. Si todos los usuarios entran en el paso a la vez, el agente no tendrá tiempo para aprender de los primeros resultados. El paso se comportará más como una prueba A/B estática que como un motor de optimización en vivo.

La mejor opción para el Optimizador de contenidos son los Canvas con entrada recurrente diaria, así como los Canvas desencadenados por eventos y desencadenados por API con entradas de usuarios diarias relativamente constantes. Si utilizas el Optimizador de contenidos en Canvas de envío único o Canvas con entradas "irregulares" (como recurrentes mensuales), considera usar los [controles de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) para distribuir las entradas de usuarios a lo largo de varios días.

### Conceptos clave {#key-concepts}

| Término                    | Descripción |
|-------------------------|-------------|
| Mensaje base   | La plantilla del mensaje principal a partir de la cual se crean las variantes, incluyendo todos los ajustes de envío. |
| Componentes de contenido  | Elementos dentro de un mensaje (por ejemplo, la línea del asunto o la llamada a la acción principal) que pueden probarse y optimizarse. Los especialistas en marketing deben insertar la etiqueta de Liquid correspondiente en el mensaje, en el lugar donde debe aparecer el componente. |
| Variantes de contenido    | Los diferentes valores que puede adoptar un componente de contenido. |
| Combinaciones de contenido | Mensajes únicos creados mediante la combinación y el emparejamiento de variantes de contenido. |
| Evento de optimización       | Determina cómo el Optimizador de contenidos evalúa el rendimiento y asigna el tráfico a combinaciones de contenido a lo largo del tiempo, como clics o aperturas de correos electrónicos. Se aplica a todos los componentes de contenido de un paso. El Optimizador de contenidos aprende continuamente de este evento y cambia automáticamente la entrega hacia combinaciones de contenido de mayor rendimiento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conceptos clave" }

## Consideraciones {#considerations}

- El Optimizador de contenidos se encuentra actualmente en fase beta y solo está disponible para estos canales: correo electrónico, notificaciones push y mensajes SMS/MMS/RCS.
- Para correo electrónico, el agente puede generar hasta 125 combinaciones por paso:
   - Hasta 3 componentes por paso
   - Hasta 5 variantes para cada componente
- Para notificaciones push, el agente puede generar hasta 25 combinaciones por paso:
   - Hasta 2 componentes por paso
   - Hasta 5 variantes para cada componente
- Para mensajes SMS, MMS y RCS, el agente puede generar hasta 25 combinaciones por paso:
   - Hasta 2 componentes por paso
   - Hasta 5 variantes para cada componente
- Solo se envía un mensaje por usuario y por entrada. No hay memoria de envíos anteriores para reentradas.
- Los especialistas en marketing deben insertar manualmente etiquetas de Liquid para cada componente en el creador de mensajes donde deben mostrarse las variantes de contenido definidas.

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Próximos pasos {#next-steps}

- Ponte en contacto con tu administrador del éxito del cliente para unirte a la versión beta o para obtener asistencia con la incorporación.
- Aprende a crear un [paso de Optimizador de contenidos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step).