---
nav_title: Optimizador de contenidos
article_title: Optimizador de contenidos
alias: "/content_optimizer/"
description: "El Optimizador de contenidos te ayuda a probar y optimizar el contenido de los mensajes a gran escala, utilizando la IA para generar y evaluar grandes volúmenes de variantes de contenido."
page_type: reference
page_order: 3
---

# Optimizador de contenidos {#content-optimizer}

> El Optimizador de contenidos te ayuda a probar y optimizar el contenido de los mensajes a gran escala, utilizando la IA para generar y evaluar automáticamente grandes volúmenes de variantes de contenido.

{% alert important %}
El Optimizador de contenidos se encuentra actualmente en fase beta y solo está disponible para estos canales: correo electrónico, notificaciones push y mensajes SMS/MMS/RCS. Para obtener ayuda para empezar, ponte en contacto con tu administrador de éxito de cliente.
{% endalert %}

## Acerca del Otimizador de Contenido {#about-content-optimizer}

Content Optimizer se ejecuta en un paso en Canvas. Te ayuda a definir los componentes de un mensaje para probar, generar variantes usando IA generativa o introducción manual, y optimizar automáticamente qué combinaciones de contenido se envían a los usuarios. Esta característica te ayuda a:

- Optimizar líneas del asunto, encabezados del cuerpo, contenido del cuerpo o CTA principal para correos electrónicos.
- Optimizar títulos y mensajes para notificaciones push.
- Optimizar ganchos, cuerpos y CTAs para mensajes de SMS, MMS y RCS.
- Mejorar continuamente el rendimiento de los mensajes sin configuración manual de pruebas A/B.
- Probar grandes volúmenes de variantes de contenido rápidamente, aprovechando la IA para la ideación.
- Eliminar automáticamente el contenido con bajo rendimiento y escalar las variantes ganadoras.

Aprende a crear un [paso de Content Optimizer]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step).

{% multi_lang_include brazeai/generative_ai/policy.md %}

### OpenAI y Content Optimizer {#openai-and-content-optimizer}

Content Optimizer utiliza OpenAI solo cuando solicitas explícitamente sugerencias de variantes generadas por IA. No utiliza OpenAI para elegir qué variante recibe cada usuario ni para asignar el tráfico de envío.

- **Utiliza OpenAI:** Cuando seleccionas **Generar sugerencias de IA** para un componente de contenido, Braze envía tu variante semilla, instrucciones, [directriz de marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) opcional y (para pasos lanzados con suficientes datos de envío) contexto de rendimiento agregado a OpenAI para generar ideas de variantes.
- **Optimización bandit:** El algoritmo propietario de bandit multibrazo de Braze gestiona la asignación de tráfico, la selección de variantes en el momento del envío y la optimización basada en el rendimiento. Consulta [Cómo funciona](#how-it-works).
- **Entrada manual:** Puedes definir variantes escribiéndolas tú mismo sin enviar contenido a OpenAI.

## Ejemplos {#use-cases}

### Correo electrónico {#email}

| Ejemplo de optimización | Objetivo | Descripción |
| --- | --- | --- |
| Variaciones en la línea del asunto | Aumentar la tarifa abierta | Prueba el tono, la urgencia, la personalización y el uso de emojis. |
| Estilos de mensajería en el encabezado | Aumentar la participación | Compara mensajes emocionales, orientados al valor y claros en el encabezado del cuerpo. |
| Formato del contenido del cuerpo | Mejorar la legibilidad y la participación | Prueba narrativa frente a listas de características, viñetas frente a párrafos y la longitud del contenido. |
| Texto y tono de la CTA | Aumentar los click-throughs | Compara frases de CTA orientadas a la acción, centradas en los beneficios y en primera persona. |
| Combinaciones de contenido temático | Descubrir combinaciones de alto rendimiento | Mezcla y combina componentes temáticos de asunto, cuerpo y CTA para encontrar la mejor combinación general. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Correo electrónico" }

### Notificaciones push {#push-notifications}

| Ejemplo de optimización | Objetivo | Descripción |
| --- | --- | --- |
| Variaciones en el título | Aumentar la tarifa abierta | Prueba la claridad, la urgencia, la personalización y el tono en el título de la notificación push. |
| Estilos de texto del cuerpo | Mejorar la participación | Compara mensajes concisos, orientados al beneficio y orientados a la acción en el cuerpo de la notificación push. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Notificaciones push" }

### Mensajes SMS, MMS y RCS {#sms-mms-and-rcs-messages}

| Ejemplo de optimización | Objetivo | Descripción |
| --- | --- | --- |
| Variaciones en el gancho | Aumentar la participación | Prueba la urgencia, la personalización y el tono en la primera línea que se muestra en las vistas previas de SMS, los subtítulos de MMS o las introducciones de RCS. |
| Estilos de texto del cuerpo | Mejorar la participación | Compara mensajes concisos y orientados a la acción en el cuerpo, incluyendo el texto que acompaña a los medios en MMS y RCS. |
| Variaciones de texto de la CTA | Aumentar los click-throughs | Compara frases de CTA orientadas a la acción y conversacionales para enlaces y avisos de siguientes pasos en SMS, MMS y RCS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mensajes SMS, MMS y RCS" }

## Cómo funciona {#how-it-works}

El algoritmo bandido de Braze gestiona la optimización descrita en esta sección.

El Optimizador de contenidos utiliza un algoritmo [bandido multiarma](https://en.wikipedia.org/wiki/Multi-armed_bandit) no contextual para asignar más envíos a las variantes de alto rendimiento y reducir la asignación a las de bajo rendimiento. Con el tiempo, esto se traduce en una mejora continua del contenido de tus mensajes, con una intervención manual mínima.

El algoritmo de optimización bandido propietario de Braze se ha diseñado específicamente para la naturaleza combinatoria del paso del Optimizador de contenidos. Dado que cada mensaje se compone de varios componentes, el bandido aprende simultáneamente sobre el rendimiento de cada componente (como la línea del asunto, el cuerpo del mensaje o la llamada a la acción) y sobre sus interacciones cuando se combinan en un mensaje. Más concretamente, cuando se envía una combinación determinada, todas las combinaciones que comparten los mismos componentes se benefician de los datos de ese envío. Esto permite que el bandido aprenda mucho más rápido con la misma cantidad de datos, en comparación con un algoritmo bandido estándar.

Cuando se inicia el paso por primera vez, el Optimizador de contenidos envía variantes aleatoriamente para recopilar datos de rendimiento iniciales. Tras este periodo inicial de exploración, el algoritmo comienza a desviar el tráfico hacia combinaciones de contenido con mejor rendimiento, reduciendo gradualmente la asignación a las opciones con peor rendimiento. Durante el periodo de exploración, el tráfico se distribuye generalmente entre las variantes disponibles para permitir que el algoritmo aprenda de su rendimiento relativo.

El Optimizador de contenidos es similar al paso Mensaje de Canvas, con características como horas tranquilas, [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) y registro de eventos. Puedes configurar un paso de Optimizador de contenidos creando un mensaje base y definiendo qué componentes del contenido (como la línea del asunto, el cuerpo del texto o la llamada a la acción) deseas optimizar. Las variantes de cada componente pueden generarse con IA o introducirse manualmente, y deben añadirse etiquetas de Liquid al mensaje base para mapear los componentes al contenido del mensaje.

Cada usuario recibe un mensaje por cada entrada en el paso del Optimizador de contenidos. Las reentradas se tratan como nuevas, sin memoria de variantes anteriores.

## Configuración de entrada en Canvas {#canvas-entry-setup}

Para obtener los mejores resultados, utiliza el Otimizador de Contenido en Canvas donde los usuarios entran al paso de forma gradual y regular a lo largo del tiempo, como en Canvas recurrentes o siempre activos con un volumen diario constante. Si todos los usuarios entran al paso a la vez, el Otimizador de Contenido no tendrá tiempo de aprender de los primeros resultados. El paso se comportará más como una prueba A/B estática que como un motor de optimización en vivo.

El mejor ajuste para el Otimizador de Contenido es en Canvas de entrada diaria recurrente, así como en Canvas activados por eventos y activados por API con entradas de usuarios diarias relativamente constantes. Si usas el Otimizador de Contenido en Canvas de envío único o Canvas con entradas "irregulares" (como los recurrentes mensuales), considera usar [controles de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) para distribuir las entradas de usuarios a lo largo de varios días.

### Conceptos clave {#key-concepts}

| Término                    | Descripción |
|-------------------------|-------------|
| Mensaje base   | La plantilla de mensaje principal a partir de la cual se construyen las variantes, incluyendo toda la configuración de envío. |
| Componentes de contenido  | Elementos dentro de un mensaje (por ejemplo, línea del asunto o CTA principal) que se pueden probar y optimizar. Los especialistas en marketing deben insertar la etiqueta de Liquid correspondiente en el mensaje donde debe aparecer el componente. |
| Variantes de contenido    | Los diferentes valores que puede tomar un componente de contenido. |
| Combinaciones de contenido| Mensajes únicos creados al mezclar y combinar variantes de contenido. |
| Evento de optimización       | Determina cómo el Otimizador de Contenido evalúa el rendimiento y asigna tráfico a las combinaciones de contenido a lo largo del tiempo, como clics o aperturas para correo electrónico. Se aplica a todos los componentes de contenido en un paso. El Otimizador de Contenido aprende continuamente de este evento y desplaza automáticamente la entrega hacia las combinaciones de contenido de mayor rendimiento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conceptos clave" }

## Consideraciones {#considerations}

- Content Optimizer se encuentra actualmente en fase beta y solo está disponible para estos canales: correo electrónico, notificaciones push y mensajes SMS/MMS/RCS.
- Para correo electrónico, Content Optimizer puede generar hasta 125 combinaciones por paso:
   - Hasta 3 componentes por paso
   - Hasta 5 variantes por cada componente
- Para notificaciones push, Content Optimizer puede generar hasta 25 combinaciones por paso:
   - Hasta 2 componentes por paso
   - Hasta 5 variantes por cada componente
- Para mensajes SMS, MMS y RCS, Content Optimizer puede generar hasta 25 combinaciones por paso:
   - Hasta 2 componentes por paso
   - Hasta 5 variantes por cada componente
- Solo se envía un mensaje por usuario por entrada. No se guarda un registro de envíos anteriores para las reentradas.
- Los especialistas en marketing deben insertar manualmente etiquetas de Liquid para cada componente en el creador de mensajes donde las variantes de componentes de contenido definidas deben renderizarse.

## Próximos pasos {#next-steps}

- Ponte en contacto con tu administrador de éxito de cliente para unirte a la beta o para recibir soporte de incorporación.
- Aprende a crear un [paso del Optimizador de Contenido]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step).