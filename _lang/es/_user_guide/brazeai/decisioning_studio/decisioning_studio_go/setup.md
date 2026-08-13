---
nav_title: Configura tu agente
article_title: Configura tu agente de Decisioning Studio Go
page_order: 0
page_type: reference
description: "Este artículo describe el flujo de configuración de Decisioning Studio Go para configurar la audiencia, el horario, los creativos, las restricciones y lanzar tu agente."
toc_headers: h2
---

# Configura tu agente de Decisioning Studio Go {#set-up-your-decisioning-studio-go-agent}

> Este artículo describe cómo configurar un agente de Decisioning Studio Go con el flujo de configuración de autoservicio en el panel de Braze.

Para obtener un resumen de cómo funciona Decisioning Studio Go, consulta [BrazeAI Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go). Para confirmar que tu programa es adecuado antes de configurar un agente, consulta [Ejemplos para Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples).

## Requisitos previos {#prerequisites}

Confirma que tienes lo siguiente listo:

- Un [segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) para tu público de entrada que no esté en uso activo en otro Canvas o campaña
- Al menos una plantilla de correo electrónico
- El contenido de variantes que deseas probar, como líneas del asunto alternativas, CTAs e imágenes principales. Puedes crear variantes durante la configuración, pero tenerlas listas acelera el proceso
- Acceso al espacio de trabajo con permisos para configurar agentes de AI Decisioning

Si tu espacio de trabajo no ha sido aprovisionado para Decisioning Studio Go, no verás la opción de configuración de agentes en la pestaña **AI Decisioning**. Contacta a tu administrador de éxito de cliente para obtener acceso.

## Paso 1: Configura tu agente {#step-1-set-up-your-agent}

1. En el panel de Braze, ve a la pestaña **AI Decisioning**.
2. Selecciona **Create Agent**.
3. Dale a tu agente un nombre que lo distinga de otros en tu espacio de trabajo. Un ejemplo es "Miembros de fidelización—Participación semanal" en lugar de "Agente de correo electrónico".
4. (Opcional) Agrega una descripción para proporcionar contexto que tú o un compañero de equipo puedan necesitar más adelante. Esto puede incluir para qué es el agente, a qué segmento se dirige y cómo se define el éxito.

El agente optimiza tu creativo de correo electrónico para maximizar la participación genuina, medida por la actividad de clics significativos por usuario. Los clics pasan por múltiples filtros de validación independientes que filtran la actividad automatizada y los clics relacionados con la cancelación de suscripción, de modo que la señal refleja el interés real del cliente en lugar del volumen bruto de clics.

## Paso 2: Selecciona la audiencia objetivo {#step-2-select-the-target-audience}

Selecciona el segmento de Braze al que tu agente envía. Los usuarios en este segmento se dividen automáticamente en dos grupos:

- **Grupo de Decisioning Studio:** Recibe contenido de correo electrónico optimizado por IA. El agente elige la mejor combinación de variantes para cada usuario.
- **Grupo de control aleatorio:** Mínimo 5 % del segmento. Recibe combinaciones seleccionadas aleatoriamente de las mismas opciones en días seleccionados aleatoriamente. Este grupo es obligatorio.

![Un segmento seleccionado con 1100 usuarios estimados.]({% image_buster /assets/img/decisioning_studio_go/audience_details.png %})

### Por qué es importante un segmento dedicado {#why-a-dedicated-segment-matters}

Si los usuarios en tu segmento seleccionado también reciben mensajes de otros Canvas o campañas, la participación que el agente observa se ve afectada por esos otros mensajes. El agente no puede determinar si un usuario hizo clic debido a sus decisiones o por otra razón. Aparece una advertencia si tu segmento seleccionado está en uso en otro lugar; puedes continuar, pero espera resultados más ruidosos.

### Búsqueda de usuarios {#user-lookup}

Usa **User Lookup** para verificar si usuarios específicos cumplen con los criterios de tu segmento. Esto es útil para verificar la definición de tu segmento.

### Filtros de audiencia {#audience-filters}

Los filtros de audiencia no son compatibles en esta versión. Si necesitas criterios de segmentación adicionales, [crea un segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) con esos filtros aplicados y luego selecciona ese segmento como tu público de entrada.

### Integración con Canvas existentes {#integrate-with-existing-canvases}

Para usar Decisioning Studio Go dentro de un recorrido más amplio:

1. Crea un segmento dedicado para los usuarios que deben estar en el agente.
2. En tu [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas), usa un paso de actualización de usuario para agregar al usuario a ese segmento en el punto adecuado del recorrido.
3. Confirma que los usuarios salen del Canvas para que el agente (no el Canvas) se encargue del envío de correo electrónico para todos en el segmento a partir de ese momento.

## Paso 3: Configura el horario {#step-3-configure-the-schedule}

Determina cuándo el agente tiene permitido enviar.

### Paso 3.1: Determina la frecuencia de envío {#step-31-determine-the-send-frequency}

Selecciona con qué frecuencia los usuarios reciben correos electrónicos de este agente, por ejemplo, tres veces por semana. Esta es una selección única. El agente no optimiza entre diferentes frecuencias; elige días y horarios dentro de la frecuencia que establezcas.

### Paso 3.2: Selecciona los días de la semana {#step-32-select-the-days-of-the-week}

Elige en qué días el agente puede enviar. Debes seleccionar al menos tantos días como requiera tu frecuencia (si el agente envía tres veces por semana, selecciona al menos tres días; seleccionar más días le da al agente más flexibilidad). El agente optimiza dentro de ese conjunto, eligiendo los mejores días para cada usuario. Para máxima flexibilidad, selecciona los siete días.

### Paso 3.3: Establece las horas tranquilas {#step-33-set-quiet-hours}

Especifica los horarios en los que el agente no debe enviar. Las horas tranquilas usan la zona horaria local del usuario. El uso más común es bloquear envíos a altas horas de la noche y muy temprano en la mañana. Fuera de las horas tranquilas, el agente programa los envíos en los horarios con mayor probabilidad de generar clics para cada usuario.

### Paso 3.4: Establece reglas de limitación de frecuencia {#step-34-set-frequency-capping-rules}

Tus reglas de limitación de frecuencia se pueden aplicar a nivel del agente:

- **Aplicar límite de frecuencia:** Evita que el agente envíe a un usuario una vez que se haya alcanzado su límite de frecuencia. Dependiendo de cómo estén configuradas tus reglas, este límite puede aplicarse a nivel de usuario individual o a nivel general de la cuenta. En cualquier caso, no se envían mensajes a ese usuario mientras el límite esté alcanzado.
- **Contar hacia el límite:** Elige si los envíos de este agente cuentan para el límite general del usuario.

{% alert tip %}
Si tu límite de frecuencia protege la experiencia del usuario, los envíos del agente ya están dirigidos y es posible que no necesites contarlos hacia el límite. Si tu límite controla el volumen general de envíos o el gasto, probablemente quieras que se cuenten. Tu administrador de éxito de cliente o consultor de soluciones puede ayudarte a confirmar el enfoque correcto para tu espacio de trabajo.
{% endalert %}

## Paso 4: Agrega contenido y plantillas {#step-4-add-content-and-templates}

Define con qué tiene que trabajar el agente:

- **Creativos base:** Las plantillas de correo electrónico completas. El agente primero elige qué creativo base enviar a un usuario determinado.
- **Componentes creativos:** Los elementos específicos dentro de un creativo base (línea del asunto, CTA e imagen principal) que el agente personaliza por usuario.

Puedes crear creativos base de las siguientes maneras:

- Usando el creador estándar de correo electrónico de Braze.
- Importando un correo electrónico de un Canvas o una campaña existente.

Usa un solo creativo base o varios. Con un creativo base, el agente personaliza solo los componentes dentro de él. Con múltiples creativos base, por ejemplo, uno casual, uno formal y uno promocional, el agente también elige qué creativo base es el adecuado para cada usuario. El agente también puede elegir entre varios creativos base sin componentes creativos adicionales.

### Paso 4.1: Marca los puntos de personalización con etiquetas de Liquid {#step-41-mark-personalization-points-with-liquid-tags}

Para cada componente que quieras que el agente personalice, reemplaza el contenido estático en tu creativo base con una etiqueta de Liquid del menú de personalización. Luego proporciona las opciones de variantes en la sección **Creative Components**.

Los componentes compatibles en esta versión son:

- **Línea del asunto:** Reemplaza la línea del asunto en **Sending Settings** con la etiqueta de Liquid para la línea del asunto.
- **CTA:** Reemplaza el texto del botón en el cuerpo del correo electrónico con la etiqueta de Liquid para CTA.
- **Imagen:** Reemplaza la URL de la imagen principal con la etiqueta de Liquid para imagen.

{% alert note %}
Los [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) no son compatibles como puntos de sustitución para componentes personalizados. Coloca tu línea del asunto, CTA e imagen personalizados directamente en el cuerpo del correo electrónico en lugar de dentro de un bloque de contenido.
{% endalert %}

### Paso 4.2: Agrega variantes {#step-42-add-variants}

En la sección **Creative Components**, agrega las opciones de variantes para cada punto de personalización:

- Múltiples opciones de línea del asunto
- Múltiples opciones de texto de CTA
- Múltiples URLs de imagen

Cada variante puede asociarse con creativos base específicos o estar disponible en todos los creativos base. Por ejemplo, si tienes un creativo base que promociona una oferta y otro que promociona novedades, puedes restringir tu línea del asunto `Don't miss our biggest savings of the year` solo al creativo de la oferta, mientras mantienes tu CTA `Just dropped` disponible en ambos.

Las imágenes deben seleccionarse de la biblioteca de medios de Braze. Si hay una imagen que deseas usar, súbela primero a la biblioteca de medios.

### Paso 4.3: Vista previa y prueba {#step-43-preview-and-test}

A medida que agregas más contenido, previsualiza y prueba tu mensaje usando la vista previa dinámica que muestra cómo se renderizan las diferentes combinaciones de variantes. Esto es útil para detectar y resolver problemas de renderizado antes del lanzamiento. Después de que tus creativos base y variantes estén configurados, puedes ver una lista completa de todas las combinaciones que el agente tiene permitido enviar.

También puedes enviar un mensaje de prueba a ti mismo o a un compañero de equipo. Los envíos de prueba muestran la combinación de variantes específica que selecciones, no lo que el agente elegiría para un usuario en particular.

## Paso 5: Define las restricciones {#step-5-define-constraints}

Las restricciones evitan que el agente envíe contenido repetitivo al mismo usuario. Los siguientes niveles están disponibles:

- **Nivel de creativo base:** Evita que el mismo creativo base se envíe a un usuario más de una vez dentro de una ventana que definas. Útil cuando cada creativo base es lo suficientemente distinto como para que repetirlo dentro de, por ejemplo, una semana resulte obsoleto.
- **Nivel de línea del asunto:** Evita que la misma línea del asunto se envíe a un usuario más de una vez dentro de una ventana que definas. Útil cuando las líneas del asunto son la señal de repetición más visible.

Las restricciones a nivel de variante para imágenes o CTAs específicos no son compatibles en esta versión.

## Paso 6: Revisa y lanza {#step-6-review-and-launch}

La pantalla **Review** muestra tu configuración completa: audiencia y división del grupo de control aleatorio, horario, creativos base, recuentos de variantes y restricciones activas. Revisa y resuelve cualquier advertencia de validación (por ejemplo, superposición de segmento con otra campaña) que se muestre en esta sección.

Selecciona **Launch** para activar el agente. Pasa de **Draft** a **Live** y comienza a enviar en el siguiente día elegible.

## Después del lanzamiento {#after-launch}

### Período de entrenamiento {#training-period}

Cuando tu agente se lanza, entra en un período de entrenamiento. Un indicador de entrenamiento se muestra en la interfaz de informes. El rendimiento puede fluctuar en los primeros días mientras el agente explora combinaciones. Los correos electrónicos continúan enviándose mientras aprende. No hay período de espera.

Los cambios significativos en el rendimiento aparecen después de que el agente sale del entrenamiento y entra en la personalización activa. Los informes indican cuándo ocurre esa transición, para que siempre sepas en qué etapa se encuentra tu agente.

### Vistas de informes {#reporting-views}

La interfaz de informes ofrece tres vistas principales:

| Vista | Descripción |
|---|---|
| **Rendimiento** | Tasas de clics, métricas de participación y la mejora del grupo de Decisioning Studio frente al control aleatorio. |
| **Configuración** | La configuración actual del agente, útil para confirmar qué está en ejecución. |
| **Preferencias del agente** | Recuentos de la frecuencia con la que el agente ha elegido cada variante, mostrando hacia qué se inclina el agente para tu audiencia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vistas de informes" }

Los desgloses a nivel de elemento muestran cómo se desempeñan las líneas del asunto, CTAs e imágenes individuales en todas las combinaciones.

### Editar un agente en vivo {#edit-a-live-agent}

Ve a la vista **Configuration** para modificar la audiencia, el horario, los creativos o las restricciones después del lanzamiento. La vista de configuración muestra un resumen de los cambios. Promueve los cambios antes de que surtan efecto. Agregar nuevas variantes no restablece el entrenamiento del agente en las variantes existentes; agrega nuevas opciones al menú del agente.

### Pausar o detener {#pause-or-stop}

El ciclo de vida de un agente es **Draft** > **Live** > **Stopped**. Selecciona **Stop** en cualquier momento para detener un agente; deja de enviar y se reanuda cuando lo reactives.

## Referencia {#reference}

La siguiente tabla resume las áreas de Decisioning Studio Go y los detalles relacionados.

| Área | Detalles |
|---|---|
| **Canal** | Solo correo electrónico |
| **Métrica de conversión** | Solo clics (clics diarios únicos por usuario) |
| **Puntos de personalización** | Línea del asunto, CTA, imagen principal (por creativo base) |
| **Audiencia** | Un segmento de Braze, con control aleatorio obligatorio (mínimo 5 %) |
| **Frecuencia** | Selección única (sin decisión de frecuencia) |
| **Envíos de prueba** | A través del creador de Braze |
| **Informes** | Vistas de rendimiento, configuración y preferencias del agente, más desgloses a nivel de elemento |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Alcance de Decisioning Studio Go" }

### Consideraciones {#considerations}

- Los Content Blocks no son compatibles como puntos de sustitución de personalización.
- Las URLs de imagen deben agregarse manualmente. Actualmente, la integración con la biblioteca de medios no es compatible.
- Los filtros de audiencia no son compatibles más allá de la selección de segmento.
- La personalización del cuerpo del texto, preencabezado y encabezado aún no está disponible.

## Solución de problemas {#troubleshooting}

Contacta a tu administrador de éxito de cliente o consultor de soluciones para obtener ayuda con la configuración del agente, la revisión de rendimiento o el diseño del programa.

Para preguntas frecuentes, consulta las [Preguntas frecuentes de Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq).