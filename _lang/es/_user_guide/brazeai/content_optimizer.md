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
El Optimizador de contenidos se encuentra actualmente en fase beta y solo está disponible para estos canales: correo electrónico, notificaciones push y mensajes servicio de mensajes cortos/MMS/RCS. Para obtener ayuda para empezar, ponte en contacto con tu CSM or administrador de éxito de cliente or administrador de éxito de cliente.
{% endalert %}

## Acerca del Otimizador de Contenido {#about-content-optimizer}

El Otimizador de Contenido se ejecuta en un paso en Canvas. Te ayuda a definir los componentes del mensaje que quieres probar, generar variantes utilizando IA generativa o entrada manual, y optimizar automáticamente qué combinaciones de contenido se envían a los usuarios. Esta característica te ayuda a:

- Optimizar líneas del asunto, encabezados del cuerpo, contenido del cuerpo o CTA principal para correos electrónicos.
- Optimizar títulos y mensajes para notificaciones push.
- Optimizar ganchos, cuerpos y CTAs para mensajes servicio de mensajes cortos, MMS y RCS.
- Mejorar continuamente el rendimiento de los mensajes sin configuración manual de pruebas A/B.
- Probar grandes volúmenes de variantes de contenido rápidamente, aprovechando la IA para la generación de ideas.
- Retirar automáticamente el contenido de bajo rendimiento y escalar las variantes ganadoras.

Aprende a crear un [paso de Otimizador de Contenido]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step).

{% multi_lang_include brazeai/generative_ai/policy.md %}

### OpenAI y el Otimizador de Contenido {#openai-and-content-optimizer}

El Otimizador de Contenido usa OpenAI solo cuando solicitas explícitamente sugerencias de variantes generadas por IA. No utiliza OpenAI para elegir qué variante recibe cada usuario ni para asignar el tráfico de envío.

- **Usa OpenAI:** Cuando seleccionas **Generate AI suggestions** para un componente de contenido, Braze envía tu variante semilla, instrucciones, una [directriz de marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) opcional y (para pasos lanzados con datos de envío suficientes) contexto de rendimiento agregado a OpenAI para generar ideas de variantes.
- **Optimización bandit:** El algoritmo propietario de bandit multibrazo de Braze se encarga de la asignación de tráfico, la selección de variantes en el momento del envío y la optimización basada en rendimiento. Consulta [Cómo funciona](#how-it-works).
- **Entrada manual:** Puedes definir variantes escribiéndolas tú mismo sin enviar contenido a OpenAI.

## Ejemplos {#use-cases}

### Correo electrónico {#email}

| Ejemplo de optimización | Objetivo | Descripción |
| --- | --- | --- |
| Variaciones de línea del asunto | Aumentar la tarifa abierta | Prueba el tono, la urgencia, la personalización y el uso de emojis. |
| Estilos de mensajería en el encabezado | Impulsar la participación | Compara mensajería emocional, orientada al valor y clara en el encabezado del cuerpo. |
| Formato del contenido del cuerpo | Mejorar la legibilidad y la participación | Prueba narrativa frente a listas de características, viñetas frente a párrafos y longitud del contenido. |
| Texto y tono del CTA | Aumentar los click-throughs | Compara frases de CTA orientadas a la acción, centradas en el beneficio y en primera persona. |
| Combinaciones de contenido temático | Descubrir combinaciones de alto rendimiento | Mezcla y combina componentes temáticos de asunto, cuerpo y CTA para encontrar la mejor combinación general. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Correo electrónico" }

### Notificaciones push {#push-notifications}

| Ejemplo de optimización | Objetivo | Descripción |
| --- | --- | --- |
| Variaciones de título | Aumentar la tarifa abierta | Prueba la claridad, la urgencia, la personalización y el tono en el título del push. |
| Estilos de texto del cuerpo | Mejorar la participación | Compara mensajería concisa, orientada al beneficio y orientada a la acción en el cuerpo del push. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Notificaciones push" }

### Mensajes servicio de mensajes cortos, MMS y RCS {#sms-mms-and-rcs-messages}

| Ejemplo de optimización | Objetivo | Descripción |
| --- | --- | --- |
| Variaciones de gancho | Aumentar la participación | Prueba la urgencia, la personalización y el tono en la primera línea que se muestra en las vistas previas de servicio de mensajes cortos, los subtítulos de MMS o las introducciones de RCS. |
| Estilos de texto del cuerpo | Mejorar la participación | Compara mensajería concisa y orientada a la acción en el cuerpo, incluyendo el texto que acompaña a los medios en MMS y RCS. |
| Variaciones de texto del CTA | Aumentar los click-throughs | Compara frases de CTA orientadas a la acción y conversacionales para enlaces y solicitudes de siguiente paso en servicio de mensajes cortos, MMS y RCS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mensajes servicio de mensajes cortos, MMS y RCS" }

## Cómo funciona {#how-it-works}

El algoritmo bandido de Braze gestiona la optimización descrita en esta sección.

El Optimizador de contenidos utiliza un algoritmo [bandido multiarma](https://en.wikipedia.org/wiki/Multi-armed_bandit) no contextual para asignar más envíos a las variantes de alto rendimiento y reducir la asignación a las de bajo rendimiento. Con el tiempo, esto se traduce en una mejora continua del contenido de tus mensajes, con una intervención manual mínima.

El algoritmo de optimización bandido propietario de Braze se ha diseñado específicamente para la naturaleza combinatoria del paso del Optimizador de contenidos. Dado que cada mensaje se compone de varios componentes, el bandido aprende simultáneamente sobre el rendimiento de cada componente (como la línea del asunto, el cuerpo del mensaje o la llamada a la acción) y sobre sus interacciones cuando se combinan en un mensaje. Más concretamente, cuando se envía una combinación determinada, todas las combinaciones que comparten los mismos componentes se benefician de los datos de ese envío. Esto permite que el bandido aprenda mucho más rápido con la misma cantidad de datos, en comparación con un algoritmo bandido estándar.

Cuando se inicia el paso por primera vez, el Optimizador de contenidos envía variantes aleatoriamente para recopilar datos de rendimiento iniciales. Tras este periodo inicial de exploración, el algoritmo comienza a desviar el tráfico hacia combinaciones de contenido con mejor rendimiento, reduciendo gradualmente la asignación a las opciones con peor rendimiento. Durante el periodo de exploración, el tráfico se distribuye generalmente entre las variantes disponibles para permitir que el algoritmo aprenda de su rendimiento relativo.

El Optimizador de contenidos es similar al paso Mensaje de Canvas, con características como horas tranquilas, [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) y registro de eventos. Puedes configurar un paso de Optimizador de contenidos creando un mensaje base y definiendo qué componentes del contenido (como la línea del asunto, el cuerpo del texto o la llamada a la acción) deseas optimizar. Las variantes de cada componente pueden generarse con IA o introducirse manualmente, y deben añadirse etiquetas de Liquid al mensaje base para mapear los componentes al contenido del mensaje.

Cada usuario recibe un mensaje por cada entrada en el paso del Optimizador de contenidos. Las reentradas se tratan como nuevas, sin memoria de variantes anteriores.

Para atribuir el comportamiento posterior en tus propias herramientas de análisis, añade una etiqueta de Liquid a tu mensaje que registre qué combinación recibió cada usuario. Para más información, consulta [Token de combinación]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step#combination-token).

## Configuración de entrada en Canvas {#canvas-entry-setup}

Para obtener los mejores resultados, utiliza el Otimizador de Conteúdo en Canvas donde los usuarios entran al paso de forma gradual y regular a lo largo del tiempo, como en Canvas recurrentes o siempre activos con un volumen diario constante. Si todos los usuarios entran al paso a la vez, Content Optimizer no tendrá tiempo para aprender de los primeros resultados. El paso se comportará más como una prueba A/B estática que como un motor de optimización en vivo.

La mejor opción para Content Optimizer son los Canvas con entrada recurrente diaria, así como los Canvas activados por eventos y por API con entradas de usuarios diarias relativamente constantes. Si utilizas Content Optimizer en Canvas de envío único o Canvas con entradas "irregulares" (como los recurrentes mensuales), considera usar [controles de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) para distribuir las entradas de usuarios a lo largo de varios días.

### Conceptos clave {#key-concepts}

| Término                    | Descripción |
|-------------------------|-------------|
| Mensaje base   | La plantilla de mensaje principal a partir de la cual se crean las variantes, incluyendo toda la configuración de envío. |
| Componentes de contenido  | Elementos dentro de un mensaje (por ejemplo, línea del asunto o CTA principal) que se pueden probar y optimizar. Los especialistas en marketing deben insertar la etiqueta de Liquid correspondiente en el mensaje donde debe aparecer el componente. |
| Variantes de contenido    | Los diferentes valores que un componente de contenido puede adoptar. |
| Combinaciones de contenido| Mensajes únicos creados al mezclar y combinar variantes de contenido. |
| Evento de optimización       | Determina cómo Content Optimizer evalúa el rendimiento y asigna tráfico a las combinaciones de contenido a lo largo del tiempo, como clics o aperturas para correo electrónico. Se aplica a todos los componentes de contenido en un paso. Content Optimizer aprende continuamente de este evento y redirige automáticamente la entrega hacia las combinaciones de contenido con mejor rendimiento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conceptos clave" }

## Consideraciones {#considerations}

- Content Optimizer se encuentra actualmente en versión beta y solo está disponible para estos canales: correo electrónico, notificaciones push y mensajes servicio de mensajes cortos/MMS/RCS.
- Para correo electrónico, Content Optimizer puede generar hasta 125 combinaciones por paso:
   - Hasta 3 componentes por paso
   - Hasta 5 variantes para cada componente
- Para notificaciones push, Content Optimizer puede generar hasta 25 combinaciones por paso:
   - Hasta 2 componentes por paso
   - Hasta 5 variantes para cada componente
- Para mensajes servicio de mensajes cortos, MMS y RCS, Content Optimizer puede generar hasta 25 combinaciones por paso:
   - Hasta 2 componentes por paso
   - Hasta 5 variantes para cada componente
- Solo se envía un mensaje por usuario por entrada. No hay memoria de envíos anteriores para las reentradas.
- Los especialistas en marketing deben insertar manualmente las etiquetas de Liquid para cada componente en el creador de mensajes donde las variantes de componentes de contenido definidos deben renderizarse.

## Próximos pasos {#next-steps}

- Contacta a tu CSM or administrador de éxito de cliente or administrador de éxito de cliente para unirte a la beta o para recibir soporte de incorporación.
- Aprende a crear un [paso del Otimizador de Contenido]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step).