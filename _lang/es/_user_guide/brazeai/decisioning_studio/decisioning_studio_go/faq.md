---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre Decisioning Studio Go
page_order: 8
page_type: FAQ
description: "Esta página ofrece respuestas a preguntas frecuentes sobre Decisioning Studio Go."
---

# Preguntas frecuentes {#frequently-asked-questions}

## General {#general}

### ¿Qué es Decisioning Studio Go? {#what-is-decisioning-studio-go}

Decisioning Studio Go es un agente de decisión con IA integrado en el panel de Braze. Tú seleccionas un menú de opciones —variantes creativas, horarios de envío, días de la semana— y el agente elige la combinación adecuada para cada usuario individual, optimizando para clics. Ofrece personalización uno a uno sin necesidad de un científico de datos ni una integración personalizada. La primera versión es compatible con correo electrónico; los canales adicionales se incorporarán en betas separadas, y cada canal será gestionado por su propio agente.

### ¿En qué se diferencia de las pruebas A/B? {#how-is-this-different-from-ab-testing}

Las pruebas A/B encuentran la variante que mejor funciona en promedio para toda una audiencia o dentro de un segmento, y despliegan esa única variante para todos en ese grupo. Decisioning Studio Go elige la mejor variante para cada usuario individual, basándose en con qué ha interactuado ese usuario anteriormente. Diferentes usuarios pueden recibir diferentes variantes en el mismo envío. En lugar de desplegar una variante ganadora para un grupo, Decisioning Studio Go personaliza el contenido a nivel individual.

### ¿En qué se diferencia de Decisioning Studio Pro? {#how-is-this-different-from-decisioning-studio-pro}

Go es el nivel de autoservicio. Es el punto de partida ideal para especialistas en marketing que desean personalización uno a uno en correo electrónico sin una implementación compleja. Optimiza para clics y funciona con las opciones que configuras directamente dentro de Braze.

Pro es el nivel de servicios integrales. Optimiza para cualquier métrica de negocio, se conecta a cualquier origen de datos propios, es compatible con múltiples canales e incluye soporte dedicado del equipo de Braze AI Decisioning Services.

### ¿Qué tipo de IA es? ¿Es generativa? {#what-kind-of-ai-is-this-is-it-generative}

No. El agente que decide qué enviar a cada usuario es un agente de decisión, no uno generativo. No escribe contenido por ti. Tú proporcionas las opciones y el agente aprende cuál funciona mejor para cada usuario individual.

Decisioning Studio Go está basado en aprendizaje por refuerzo. El agente trata cada envío como una oportunidad de aprender: prueba combinaciones de las opciones que has aprobado, observa si cada usuario interactúa y actualiza su comprensión de qué funciona para quién. Con el tiempo, se vuelve cada vez más preciso al emparejar a cada usuario individual con la opción de tu menú que tiene más probabilidades de generar un clic.

## Audiencias y grupos de control {#audiences-and-control-groups}

### ¿Cuál es la diferencia entre el grupo de Decisioning Studio y el grupo de control aleatorio? {#whats-the-difference-between-the-decisioning-studio-group-and-the-random-control-group}

El grupo de Decisioning Studio recibe contenido de correo electrónico optimizado por IA; el agente elige la mejor variante para cada usuario. El grupo de control aleatorio recibe combinaciones aleatorias de las mismas opciones, sin optimización. Ambos grupos respetan las restricciones que has configurado (por ejemplo, si has indicado que no se repita una línea del asunto en 15 días, esa regla también se aplica al control aleatorio). Comparar los dos grupos te da una medida limpia del incremento del agente.

### ¿El control aleatorio es un grupo de exclusión de usuarios que no reciben correo electrónico? {#is-the-random-control-a-holdout-group-of-users-who-receive-no-email}

No. Los usuarios del control aleatorio siguen recibiendo correos electrónicos. Reciben combinaciones seleccionadas aleatoriamente de las opciones que configuraste, enviadas en días seleccionados aleatoriamente dentro de tu programación. Esto te permite comparar "personalizado por IA" contra "el mismo contenido, enviado aleatoriamente" en lugar de contra "ningún correo electrónico".

### ¿Por qué es obligatorio el control aleatorio? {#why-is-the-random-control-required}

Por dos razones. Primero, te proporciona una medición continua y en tiempo real de cuánto está superando el agente a una línea base aleatoria. Segundo, el agente utiliza el comportamiento del control aleatorio como parte de su señal de aprendizaje. El tamaño mínimo del control aleatorio es del 5 %, que es el mínimo necesario para que el agente aprenda de forma fiable y para que la medición del rendimiento sea significativa.

### ¿Puedo usar un segmento que ya se utiliza en otro Canvas o Campaign? {#can-i-use-a-segment-thats-already-used-in-another-canvas-or-campaign}

Puedes, pero se desaconseja encarecidamente y aparece una advertencia. Cuando los mismos usuarios reciben mensajes de Decisioning Studio Go y de otros Canvas o Campaigns al mismo tiempo, los otros mensajes afectan la participación de formas que el agente no puede tener en cuenta. La configuración más limpia es un segmento dedicado al agente.

## Configuración {#configuration}

### ¿Qué puedo personalizar? {#what-can-i-personalize}

Dentro de cada creatividad base, puedes marcar la línea del asunto, el CTA y una imagen como puntos de personalización usando etiquetas de Liquid. El agente entonces elige entre las variantes que proporcionas para cada componente, por usuario. También puedes tener múltiples creatividades base; el agente también elige cuál usar.

### ¿Puedo usar Content Blocks para los componentes personalizados? {#can-i-use-content-blocks-for-the-personalized-components}

No. Los Content Blocks no funcionan como puntos de sustitución de componentes creativos en este momento. Coloca tu línea del asunto, CTA e imagen personalizados directamente en el cuerpo del correo electrónico en lugar de dentro de un bloque de contenido.

### ¿Puedo usar plantillas basadas en imágenes sin elementos clicables? {#can-i-use-image-based-templates-with-no-clickable-elements}

Las plantillas basadas en imágenes son compatibles, pero limitan lo que el agente puede optimizar. Si todo el correo electrónico es una sola imagen, el agente aún puede decidir qué imagen enviar, pero no puede optimizar la línea del asunto, el CTA ni el diseño dentro del correo electrónico. Obtienes más incremento con plantillas basadas en HTML con múltiples puntos de personalización.

### ¿Puedo cambiar el evento de conversión? {#can-i-change-the-conversion-event}

Para el nivel de autoservicio, el evento de conversión compatible es clics. En Decisioning Studio Pro, puedes optimizar para cualquier métrica de negocio personalizada.

### ¿Cómo funciona la frecuencia de envío? {#how-does-send-frequency-work}

Seleccionas una única frecuencia, como tres envíos por semana. El agente no decide entre frecuencias. Dentro de esa frecuencia, elige qué días (de los días que permitiste) y qué horarios (dentro de tus horas tranquilas, en la zona horaria local del usuario) enviar.

### ¿Cómo funciona la limitación de frecuencia? {#how-do-frequency-caps-work}

Durante la configuración, puedes aplicar las reglas de limitación de frecuencia de tu espacio de trabajo al agente y elegir si los envíos del agente cuentan para el límite de frecuencia global de cada usuario. Tu CSM o consultor de soluciones puede ayudarte a decidir el enfoque adecuado para tu programa según cómo estén configurados los límites de frecuencia en tu espacio de trabajo.

### ¿Puede el agente enviar a través de múltiples canales? {#can-the-agent-send-across-multiple-channels}

Cada agente es de un solo canal, y el canal compatible actualmente es correo electrónico. Puedes ejecutar múltiples agentes en paralelo para diferentes programas, pero cada agente gestiona un canal.

## Pruebas y lanzamiento {#testing-and-launch}

### ¿Cómo pruebo antes de ponerlo en vivo? {#how-do-i-test-before-going-live}

Usa la función nativa de envío de prueba en el creador de Braze. Los envíos de prueba muestran combinaciones de variantes específicas que seleccionas; son para revisar el correo electrónico en sí, no para predecir lo que el agente realmente enviaría a un usuario real. La vista previa dinámica en el creador también te permite ver cómo se renderizan diferentes combinaciones de variantes.

### ¿Qué sucede justo después del lanzamiento? {#what-happens-right-after-i-launch}

El agente entra en un período de entrenamiento. Los correos electrónicos se envían desde el primer día sin un período de espera, pero el rendimiento puede fluctuar mientras el agente explora combinaciones. Los informes indican cuándo el agente aún está en entrenamiento frente a cuándo ha pasado a personalización activa, para que siempre sepas en qué etapa se encuentra.

### ¿Puedo editar el agente después del lanzamiento? {#can-i-edit-the-agent-after-launch}

Sí. La audiencia, la programación, las creatividades y las restricciones pueden actualizarse después del lanzamiento. Debes promover los cambios antes de que surtan efecto.

### ¿Qué pasa si actualizo las opciones de contenido después del lanzamiento? {#what-if-i-update-content-options-after-launch}

Puedes agregar, eliminar o cambiar variantes de la misma forma en que las configuraste originalmente. Los cambios deben promoverse antes de que surtan efecto. Agregar una nueva variante no reinicia el entrenamiento del agente sobre las variantes existentes.

## Informes y resultados {#reporting-and-results}

### ¿Los informes de Decisioning Studio Go coinciden con lo que veo en mis análisis de correo electrónico en otras partes de Braze? {#does-decisioning-studio-go-reporting-match-what-i-see-in-my-email-analytics-elsewhere-in-braze}

Los números pueden diferir. Decisioning Studio aplica un filtrado de clics más agresivo que los informes estándar de correo electrónico, por lo que los totales pueden ser menores. La comparación relativa entre el grupo de Decisioning Studio y el control aleatorio es consistente dentro de los informes de Decisioning Studio, ya que el filtrado de clics se aplica a cada grupo por igual.

### ¿Para qué métricas optimiza el agente? {#what-metrics-does-the-agent-optimize-for}

Clics únicos diarios por usuario. El objetivo del agente es maximizar el número de usuarios distintos que hacen clic, no el volumen bruto de clics.

### ¿Puedo ver qué combinaciones están funcionando mejor? {#can-i-see-which-combinations-are-performing-best}

Sí. Los informes incluyen la distribución de elementos individuales —como líneas del asunto, CTAs e imágenes— que el agente envía.

### ¿Quién es responsable del contenido que envía el agente? {#whos-accountable-for-the-content-the-agent-sends}

Tú. El agente solo envía contenido que has agregado como variante. El agente decide la combinación para cada usuario, pero cada elemento individual proviene de las variantes que proporcionaste.

## Soporte {#support}

### ¿Dónde puedo obtener ayuda con mi agente? {#where-do-i-get-help-with-my-agent}

Contacta a tu CSM o consultor de soluciones de Braze para obtener ayuda con la configuración, la revisión del rendimiento o el diseño del programa.