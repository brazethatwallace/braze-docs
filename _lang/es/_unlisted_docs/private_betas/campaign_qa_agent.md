---
nav_title: Agente de QA de Campaign
article_title: Agente de QA de Campaign
permalink: /campaign_qa_agent/
description: "Este artículo de referencia cubre los agentes de QA de Campaign, incluyendo cómo funcionan estos agentes y las mejores prácticas."
hidden: true
---

# Agente de QA de Campaign {#campaign-qa-agent}

> Los agentes de QA de Campaign son asistentes impulsados por IA que ejecutan comprobaciones automatizadas en la configuración de tu Campaign. Estos agentes actúan como una salvaguarda final, validando tu configuración contra las directrices de marca, las convenciones organizativas y los requisitos técnicos antes de que lances.

Al usar agentes de QA de Campaign, puedes reducir la supervisión manual y asegurar que cada mensaje enviado desde la plataforma Braze sea preciso, conforme y listo para lanzar.

{% alert important %}
Los agentes de QA de Campaign para la Consola de Agente están actualmente en beta. Ponte en contacto con tu director de cuentas de Braze si te interesa participar en esta beta.
{% endalert %}

## Cómo funciona {#how-it-works}

Cuando creas un agente de QA de Campaign, defines reglas específicas, agrupadas en "conjuntos de reglas", que el agente usa para evaluar una Campaign. Puedes elegir entre conjuntos de reglas predefinidos que cubren necesidades comunes de marketing o crear reglas personalizadas específicas para tu equipo.

Una vez configurado, puedes probar el agente en el panel de vista previa contra cualquier Campaign existente en tu espacio de trabajo. El agente proporciona un informe detallado, categorizando sus hallazgos en Correcto, Advertencia o Fallo.

## Crear un agente de QA de Campaign {#create-a-campaign-qa-agent}

### Paso 1: Elige el tipo de agente {#step-1-choose-the-agent-type}

Para crear tu agente, ve a **Consola de Agente** > **Gestión de agentes**. Selecciona **Crear agente** y elige **Campaign QA** en el menú desplegable.

### Paso 2: Configura los detalles {#step-2-set-up-details}

A continuación, configura los detalles de tu agente:

1. Introduce un nombre y una descripción para ayudar a tu equipo a entender su propósito.
2. (opcional) Añade etiquetas para filtrar tu agente.
3. Elige el modelo que tu agente usará. Esto impulsa el razonamiento del agente.

![Un agente de QA de Campaign llamado "Campaign QA for copy" que comprobará la calidad del mensaje de la Campaign, usando el modelo Braze Auto.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_details.png %}){: style="max-width:80%;"}

### Paso 3: Configura las instrucciones y reglas {#step-3-configure-instructions-and-rules}

En la pestaña **Instrucciones**, define las reglas que el agente comprueba. Puedes añadir hasta 10 conjuntos de reglas por agente y hasta 20 reglas por conjunto de reglas.

1. Selecciona **Añadir conjunto de reglas** para ver una lista de las siguientes categorías:

- **Configuración de Campaign:** Valida convenciones de nomenclatura, etiquetas y seguimiento de conversiones.
- **Audiencia y segmentación:** Comprueba Segments, exclusiones y tamaño de la audiencia.
- **Contenido y texto:** Evalúa la calidad del texto, los límites de caracteres y la completitud del mensaje.
- **Enlaces y seguimiento:** Verifica URLs, CTAs, vínculos profundos y parámetros UTM.
- **Personalización y contenido dinámico:** Comprueba la lógica Liquid y los valores alternativos.
- **Cumplimiento y capacidad de entrega:** Asegura que se cumplan los requisitos legales y las salvaguardas de envío.
- **Generar con Operator:** Si no estás seguro de cómo formular una regla, selecciona Generar con Operator para que nuestro asistente de IA te ayude a redactar una lógica específica basada en tus requisitos.
- **Reglas personalizadas:** Selecciona Crear conjunto de reglas personalizado para definir comprobaciones únicas que no encajan claramente en ninguna de las categorías preconfiguradas.

![Seis reglas configuradas para la categoría de Contenido y texto.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_instructions.png %}){: style="max-width:80%;"}

### Paso 4: Prueba tu agente {#step-4-test-your-agent}

Antes de desplegar tu agente, usa el panel de **vista previa** para simular una respuesta y confirmar que la lógica funciona como se espera.

1. Elige una Campaign existente del menú desplegable para usarla como caso de prueba.
2. Elige probar todos los conjuntos de reglas o uno específico.
3. Selecciona el botón **Simular respuesta**.

A continuación, revisa los resultados. El agente evalúa la Campaign y muestra los resultados en las siguientes categorías:

- **Correcto:** Estas reglas se cumplieron con éxito. Por ejemplo, el agente podría confirmar que tus convenciones de nomenclatura coinciden con los patrones esperados.
- **Advertencia:** Estos son problemas no críticos que pueden requerir atención. Por ejemplo, si estás probando un conjunto de reglas de correo electrónico contra una Campaign de webhook, el agente puede emitir una advertencia de que los nombres de remitente no aplican.
- **Fallo:** Estos son problemas críticos que deben corregirse antes del lanzamiento. Ejemplos incluyen fechas planificadas que están en el pasado o etiquetas organizativas obligatorias faltantes.

## Usar agentes de QA de Campaign {#use-campaign-qa-agents}

Después de haber configurado un agente de QA de Campaign, puedes usarlo para auditar cualquier Campaign durante el proceso de revisión final. Esto asegura que tu Campaign cumpla con todos los requisitos antes de que se envíe a tus usuarios.

### Ejecutar una auditoría {#run-an-audit}

Para ejecutar una comprobación automatizada, ve al paso **Resumen de revisión** del flujo de trabajo de creación de tu Campaign.

1. Ve a la sección **Agente de QA** y selecciona el agente deseado del menú desplegable.
3. Selecciona **Ejecutar agente de QA**.

Si realizas cambios en tu Campaign después de ejecutar una comprobación inicial, puedes seleccionar **Volver a ejecutar agente de QA** para actualizar los resultados.

### Revisar los resultados de la auditoría {#review-audit-results}

Después de que la evaluación se complete, el agente proporciona un resumen de sus hallazgos categorizados en estas pestañas: **Correcto**, **Fallo** y **Advertencia**.

La pestaña **Fallo** lista las reglas que no se cumplieron. Para cada fallo, el agente proporciona:

- **Regla:** Los criterios específicos que se comprobaron, como "Comprobación de ortografía y gramática".
- **Razonamiento:** Una explicación detallada de por qué la comprobación falló. Por ejemplo, el agente podría identificar que se usó "personalized" en lugar de la ortografía en inglés australiano "personalised".
- **Correcciones directas:** Cambios específicos de texto o configuración sugeridos por el agente para corregir el problema.

La pestaña **Correcto** lista todas las reglas que tu Campaign siguió con éxito. Esto confirma que comprobaciones como **Detección de lenguaje ofensivo** o **Validación de convención de nomenclatura** se han superado.

La pestaña **Advertencia** lista problemas no críticos que pueden requerir atención. Por ejemplo, si estás probando un conjunto de reglas de correo electrónico contra una Campaign de webhook, el agente puede emitir una advertencia de que los nombres de remitente no aplican.

### Resolver o ignorar problemas {#resolve-or-ignore-issues}

Para cada fallo o advertencia identificados, puedes decidir cómo proceder antes de lanzar. Selecciona **Resolver** junto a un problema, luego selecciona entre las siguientes opciones:

- **He corregido el problema:** Selecciona esto después de haber actualizado la configuración o el texto de tu Campaign basándote en los comentarios del agente.
- **Ignorar este problema:** Selecciona esto para hacer una excepción a la regla. Esto es útil para desviaciones intencionales o casos límite donde la sugerencia del agente puede no aplicar.

Después de que todos los problemas críticos se resuelvan o ignoren, puedes proceder a lanzar tu Campaign.

## Mejores prácticas {#best-practices}

- **Comienza con plantillas:** Usa los conjuntos de reglas predefinidos para configuración de Campaign y enlaces y seguimiento primero, ya que estos cubren los errores manuales más comunes y aseguran que el agente tenga el contexto adecuado para comprobar.
- **Sé específico:** Al escribir reglas personalizadas, proporciona ejemplos claros de cómo se ve lo "correcto". Por ejemplo, en lugar de escribir "Comprobar la convención de nomenclatura", intenta "Asegurar que el nombre de la Campaign comience con el año actual (por ejemplo, 2026_)."
- **Itera con frecuencia:** A medida que tus directrices de marca o procesos internos cambien, actualiza los conjuntos de reglas de tu agente de QA de Campaign para mantener tus comprobaciones automatizadas relevantes.