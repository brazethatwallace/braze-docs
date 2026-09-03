---
nav_title: Estándares agénticos
article_title: Estándares agénticos
permalink: /campaign_qa_agent/
description: "Este artículo de referencia cubre los estándares agénticos, incluyendo cómo funcionan los estándares de Campaign y las mejores prácticas."
hidden: true
---

# Estándares agénticos {#agentic-standards}

> Los estándares agénticos son reglas y conjuntos de reglas para aplicar políticas empresariales y límites de seguridad en Campaigns en Braze. Operator los sigue durante el proceso de creación y edición. Estos estándares pueden evaluarse de forma agéntica antes de que se lance una Campaign para actuar como una protección final que valide las directrices de marca, las convenciones organizacionales y los requisitos técnicos antes del lanzamiento.

Los estándares agénticos reducen la supervisión manual para que cada mensaje que Braze envíe sea preciso, conforme y esté listo para su lanzamiento.

{% alert important %}
Los estándares agénticos para Agent Console están actualmente en beta. Ponte en contacto con tu director de cuentas de Braze si te interesa participar en esta beta.
{% endalert %}

## Cómo funciona {#how-it-works}

Cuando creas un estándar de Campaign, defines reglas específicas, agrupadas en "conjuntos de reglas", que Operator sigue y evalúa antes de que lances una Campaign. Puedes elegir entre conjuntos de reglas predefinidos que cubren necesidades de marketing comunes o crear reglas personalizadas específicas para tu equipo.

Una vez configurado, puedes probar el estándar de Campaign en el panel **Vista previa de evaluación** contra cualquier Campaign existente en tu espacio de trabajo. La evaluación agéntica proporciona un informe detallado con categorías de sus hallazgos.

## Crear un estándar de Campaign {#create-a-campaign-standard}

### Paso 1: Elige el tipo de estándar {#step-1-choose-the-standard-type}

Para crear tu estándar, ve a **Agent Console** > **Agentic Standards**. Selecciona **Crear estándar de agente** y elige **Estándares de campaña** en el menú desplegable.

### Paso 2: Configura los detalles {#step-2-set-up-details}

A continuación, configura los detalles de tu estándar:

1. Ingresa un nombre y una descripción para ayudar a tu equipo a entender su propósito.
2. (Opcional) Agrega etiquetas para filtrar tu estándar.
3. Elige el modelo de evaluación que tu estándar utilizará. Este impulsa la evaluación agéntica de un estándar.

![Un estándar de Campaign "Abandoned Cart Campaign Standards" que define las reglas y conjuntos de reglas para Campaigns de carrito abandonado en Braze.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_details.png %}){: style="max-width:80%;"}

### Paso 3: Configura las reglas de Campaign {#step-3-configure-campaign-rules}

En el paso **Reglas de la campaña**, define las reglas que deben aplicarse como parte de este estándar. Puedes agregar hasta 10 conjuntos de reglas por estándar y hasta 20 reglas por conjunto de reglas.

Selecciona **Añadir conjunto de reglas** para ver una lista de las siguientes categorías:

- **Configuración de la campaña:** Valida convenciones de nomenclatura, etiquetas y seguimiento de conversiones.
- **Audiencia y segmentación:** Verifica Segments, exclusiones y tamaño de la audiencia.
- **Contenido y texto:** Define requisitos para la calidad del texto, límites de caracteres y completitud del mensaje.
- **Enlaces y seguimiento:** Verifica URLs, CTAs, vínculos profundos y parámetros UTM.
- **Personalización y contenido dinámico:** Define comprobaciones para la lógica Liquid y valores de alternativa.
- **Cumplimiento y capacidad de entrega:** Define requisitos para obligaciones legales y protecciones de envío.
- **Reglas personalizadas:** Selecciona **Crear un conjunto de reglas personalizado** para definir requisitos únicos que no encajan claramente en ninguna de las categorías preconfiguradas.

Si no estás seguro de cómo redactar una regla, selecciona **Generar con Operator** para que Operator te ayude a redactar la lógica específica según tus requisitos.

![Cuatro reglas configuradas para la categoría de audiencia y segmentación.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_instructions.png %}){: style="max-width:80%;"}

### Paso 4: Prueba tu estándar {#step-4-test-your-standard}

Antes de usar tu estándar para Campaigns en Braze, usa el panel **Vista previa de evaluación** para simular una evaluación agéntica.

1. Elige una Campaign existente del menú desplegable para usarla como caso de prueba.
2. Elige probar todos los conjuntos de reglas o uno específico.
3. Selecciona el botón **Simular respuesta**.

A continuación, revisa los resultados. La evaluación se ejecuta contra la Campaign y muestra los resultados en las siguientes categorías:

- **Aprobar:** Estas reglas se cumplieron con éxito. Por ejemplo, la evaluación puede confirmar que tus convenciones de nomenclatura coinciden con los patrones esperados.
- **Advertencia:** Estos son problemas no críticos que pueden requerir atención. Por ejemplo, si estás probando un conjunto de reglas de correo electrónico contra una Campaign de webhook, la evaluación agéntica puede emitir una advertencia de que los nombres de remitente no aplican.
- **Fallo:** Estos son problemas críticos que deben corregirse antes del lanzamiento. Algunos ejemplos incluyen fechas programadas que están en el pasado o etiquetas organizacionales requeridas que faltan.

## Usar estándares agénticos {#use-agentic-standards}

Después de haber configurado un estándar de Campaign, puedes usarlo para evaluar cualquier Campaign durante el proceso de revisión final. Esto confirma que tu Campaign cumple con todos los requisitos antes de que se envíe a tus usuarios.

### Ejecutar una evaluación {#run-an-evaluation}

Para ejecutar una evaluación automatizada, ve al paso **Resumen de revisión** del flujo de trabajo de creación de tu Campaign.

1. Ve a la sección **Estándares de agente** y selecciona el estándar deseado del menú desplegable.
2. Selecciona **Ejecutar evaluación**.

Si realizas cambios en tu Campaign después de ejecutar una evaluación inicial, selecciona **Volver a ejecutar la evaluación** para actualizar los resultados.

### Revisar los resultados de la evaluación {#review-evaluation-results}

Una vez completada la evaluación, un resumen muestra los hallazgos en estas categorías: **Aprobar**, **Fallo** y **Advertencia**.

La pestaña **Fallo** enumera las reglas que no se cumplieron. Para cada fallo, el estándar proporciona:

- **Rule:** Los criterios específicos que se verifican, como "Spelling & Grammar Check".
- **Reason:** Una explicación de por qué la verificación falló. Por ejemplo, la evaluación podría identificar que se usó "personalized" en lugar de la ortografía del inglés australiano "personalised".

La pestaña **Aprobar** enumera todas las reglas que tu Campaign siguió con éxito. Esto confirma que comprobaciones como **Offensive Language Detection** o **Naming Convention Validation** se han superado.

La pestaña **Advertencia** enumera problemas no críticos que pueden requerir atención. Por ejemplo, si estás probando un conjunto de reglas de correo electrónico contra una Campaign de webhook, la evaluación del estándar puede generar una advertencia de que los nombres de remitente no aplican.

### Resolver o ignorar problemas {#resolve-or-ignore-issues}

Para cada fallo o advertencia identificados, puedes decidir cómo proceder antes del lanzamiento. Selecciona **Resolver** junto a un problema y luego selecciona una de las siguientes opciones:

- **Marcar como resuelto:** Selecciona esta opción después de haber actualizado la configuración o el texto de tu Campaign basándote en la sugerencia de la evaluación.
- **Ignorar este problema:** Selecciona esta opción para omitir el problema solo para esta ejecución. Esto es útil para desviaciones intencionales o casos excepcionales donde la sugerencia de la evaluación puede no aplicar.
- **Pregúntale a Operator de BrazeAI:** Selecciona esta opción para corregir el problema usando Operator.

Después de que todos los problemas críticos se hayan resuelto o ignorado, puedes proceder a lanzar tu Campaign.

## Mejores prácticas {#best-practices}

- **Comienza con plantillas:** Usa los conjuntos de reglas predefinidos para la configuración de Campaign y enlaces y seguimiento primero, ya que cubren los errores manuales más comunes y proporcionan a la evaluación agéntica el contexto adecuado.
- **Sé específico:** Al escribir reglas personalizadas, proporciona ejemplos claros de cómo se ve lo "correcto". Por ejemplo, en lugar de escribir "Verificar la convención de nomenclatura", intenta "El nombre de la Campaign comienza con el año actual (por ejemplo, 2026_)".
- **Itera a menudo:** A medida que las directrices de tu marca o los procesos internos cambien, actualiza los conjuntos de reglas de tu estándar de Campaign para mantener tus comprobaciones automatizadas relevantes.