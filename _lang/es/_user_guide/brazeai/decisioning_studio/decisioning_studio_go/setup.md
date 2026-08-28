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

- Un [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) para tu público de entrada que no se esté utilizando activamente en otro Canvas o Campaign
- Al menos una plantilla de correo electrónico
- El contenido de las variantes que quieras probar, como líneas del asunto alternativas, CTAs e imágenes principales. Puedes crear variantes durante la configuración, pero tenerlas listas acelera el proceso
- Acceso al espacio de trabajo con permisos para configurar agentes de AI Decisioning

Si tu espacio de trabajo no ha sido aprovisionado para Decisioning Studio Go, no verás la opción de configuración de agentes en la pestaña **AI Decisioning**. Ponte en contacto con tu administrador de éxito de cliente para obtener acceso.

## Paso 1: Configura tu agente {#step-1-set-up-your-agent}

1. En el panel de Braze, ve a la pestaña **AI Decisioning**.
2. Selecciona **Create Agent**.
3. Dale a tu agente un nombre que lo distinga de otros en tu espacio de trabajo. Un ejemplo es "Miembros de fidelización: participación semanal" en lugar de "Agente de correo electrónico".
4. (Opcional) Añade una descripción para proporcionar contexto que tú o un compañero de equipo puedan necesitar más adelante. Puede incluir para qué es el agente, a qué Segment se dirige y cómo se define el éxito.


El agente optimiza el contenido creativo de tu correo electrónico para maximizar la participación genuina, medida por la actividad de clics significativos por usuario. Los clics pasan por múltiples filtros de validación independientes que filtran la actividad automatizada y los clics relacionados con la exclusión, de modo que la señal refleja el interés real del cliente en lugar del volumen bruto de clics.

## Paso 2: Selecciona el público objetivo {#step-2-select-the-target-audience}

Selecciona el Segment de Braze al que tu agente envía mensajes. Los usuarios de este Segment se dividen automáticamente en dos grupos:

- **Grupo de Decisioning Studio:** Recibe contenido de correo electrónico optimizado por IA. El agente elige la mejor combinación de variantes para cada usuario.
- **Grupo de control aleatorio:** Mínimo un 5 % del Segment. Recibe combinaciones seleccionadas aleatoriamente de las mismas opciones en días seleccionados aleatoriamente. Este grupo es obligatorio.

![Un Segment seleccionado con 1100 usuarios estimados.]({% image_buster /assets/img/decisioning_studio_go/audience_details.png %})

### Por qué es importante un Segment dedicado {#why-a-dedicated-segment-matters}

Si los usuarios de tu Segment seleccionado también reciben mensajes de otros Canvas o Campaigns, la participación que el agente observa se ve afectada por esos otros mensajes. El agente no puede distinguir si un usuario hizo clic debido a sus decisiones o por algún otro motivo. Aparece una advertencia si tu Segment seleccionado está en uso en otro lugar; puedes continuar, pero los resultados serán más ruidosos.

### Búsqueda de usuarios {#user-lookup}

Utiliza **User Lookup** para verificar si usuarios específicos cumplen los criterios de tu Segment. Esto es útil para verificar la definición de tu Segment.

### Filtros de audiencia {#audience-filters}

Los filtros de audiencia no son compatibles en esta versión. Si necesitas criterios de segmentación adicionales, [crea un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) con esos filtros aplicados y, a continuación, selecciona ese Segment como tu público de entrada.

### Integración con Canvas existentes {#integrate-with-existing-canvases}

Para usar Decisioning Studio Go dentro de un recorrido más amplio:

1. Crea un Segment dedicado para los usuarios que deberían estar en el agente.
2. En tu [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas), utiliza un paso de actualización de usuario para añadir al usuario a ese Segment en el punto adecuado del recorrido.
3. Confirma que los usuarios salen del Canvas para que el agente (no el Canvas) se encargue del envío de correo electrónico para todos los usuarios del Segment a partir de ese momento.

## Paso 3: Configurar el horario {#step-3-configure-the-schedule}

Determina cuándo el agente tiene permiso para enviar.

### Paso 3.1: Determinar la frecuencia de envío {#step-31-determine-the-send-frequency}

Selecciona con qué frecuencia los usuarios reciben correos electrónicos de este agente, por ejemplo, tres veces por semana. Se trata de una selección única. El agente no optimiza entre distintas frecuencias; elige días y horas dentro de la frecuencia que establezcas.

### Paso 3.2: Seleccionar los días de la semana {#step-32-select-the-days-of-the-week}

Elige en qué días el agente puede enviar. Debes seleccionar al menos tantos días como requiera tu frecuencia (si el agente envía tres veces por semana, selecciona al menos tres días; seleccionar más días le da al agente más flexibilidad). El agente optimiza dentro de ese conjunto, eligiendo los mejores días para cada usuario. Para obtener la máxima flexibilidad, selecciona los siete días.

### Paso 3.3: Establecer horas tranquilas {#step-33-set-quiet-hours}

Especifica los horarios en los que el agente no debe enviar. Las horas tranquilas utilizan la zona horaria local del usuario. El uso más común es bloquear envíos a altas horas de la noche y muy temprano por la mañana. Fuera de las horas tranquilas, el agente programa los envíos en los horarios con mayor probabilidad de generar clics para cada usuario.

### Paso 3.4: Establecer reglas de limitación de frecuencia {#step-34-set-frequency-capping-rules}

Tus reglas de limitación de frecuencia pueden aplicarse a nivel del agente:

- **Aplicar limitación de frecuencia:** Evita que el agente envíe a un usuario una vez que se ha alcanzado su límite de frecuencia. Dependiendo de cómo estén configuradas tus reglas, este límite puede aplicarse a nivel de usuario individual o a nivel de cuenta general. En cualquier caso, los mensajes no se envían a ese usuario mientras el límite esté alcanzado.
- **Contar para el límite:** Elige si los envíos de este agente cuentan para el límite general del usuario.

{% alert tip %}
Si tu limitación de frecuencia protege la experiencia del usuario, los envíos del agente ya están segmentados y es posible que no necesites contarlos para el límite. Si tu límite controla el volumen total de envíos o el gasto, probablemente quieras que se contabilicen. Tu administrador de éxito de cliente o consultor de soluciones puede ayudarte a confirmar el enfoque adecuado para tu espacio de trabajo.
{% endalert %}

## Paso 4: Añade contenido y plantillas {#step-4-add-content-and-templates}

Define con qué tiene que trabajar el agente:

- **Creativos base:** Las plantillas de correo electrónico completas. El agente primero elige qué creativo base enviar a un usuario determinado.
- **Componentes creativos:** Los elementos específicos dentro de un creativo base (línea del asunto, CTA e imagen principal) que el agente personaliza por usuario.

Puedes crear creativos base de las siguientes formas:

- Usando el creador estándar de correo electrónico de Braze.
- Importando un correo electrónico de un Canvas o Campaign existente.

Usa un solo creativo base o varios. Con un solo creativo base, el agente personaliza únicamente los componentes dentro de él. Con varios creativos base (por ejemplo, uno casual, uno formal y uno promocional), el agente también elige qué creativo base es el adecuado para cada usuario. El agente también puede elegir entre varios creativos base sin componentes creativos adicionales.

### Paso 4.1: Marca los puntos de personalización con etiquetas de Liquid {#step-41-mark-personalization-points-with-liquid-tags}

Para cada componente que quieras que el agente personalice, reemplaza el contenido estático en tu creativo base con una etiqueta de Liquid del menú de personalización. Luego proporciona las opciones de variantes en la sección **Creative Components**.

Los componentes compatibles en esta versión son:

- **Línea del asunto:** Reemplaza la línea del asunto en **Sending Settings** con la etiqueta de Liquid para la línea del asunto.
- **CTA:** Reemplaza el texto del botón en el cuerpo del correo electrónico con la etiqueta de Liquid para CTA.
- **Imagen:** Reemplaza la URL de la imagen principal con la etiqueta de Liquid para imagen.

{% alert note %}
Los [bloques de contenido]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) no son compatibles como puntos de sustitución para componentes personalizados. Coloca tu línea del asunto, CTA e imagen personalizados directamente en el cuerpo del correo electrónico en lugar de dentro de un bloque de contenido.
{% endalert %}

### Paso 4.2: Añade variantes {#step-42-add-variants}

En la sección **Creative Components**, añade las opciones de variantes para cada punto de personalización:

- Múltiples opciones de línea del asunto
- Múltiples opciones de texto de CTA
- Múltiples URLs de imagen

Cada variante puede asociarse con creativos base específicos o estar disponible en todos los creativos base. Por ejemplo, si tienes un creativo base que promociona una oferta y otro que promociona novedades, puedes restringir tu línea del asunto `Don't miss our biggest savings of the year` solo al creativo de la oferta, mientras mantienes tu CTA `Just dropped` disponible en ambos.

Las imágenes deben seleccionarse de la biblioteca de medios de Braze. Si hay una imagen que quieres usar, súbela primero a la biblioteca de medios.

### Paso 4.3: Vista previa y prueba {#step-43-preview-and-test}

A medida que añadas más contenido, previsualiza y prueba tu mensaje usando la vista previa dinámica que muestra cómo se renderizan las diferentes combinaciones de variantes. Esto es útil para detectar y resolver problemas de renderizado antes del lanzamiento. Después de configurar tus creativos base y variantes, puedes ver una lista completa de todas las combinaciones que el agente tiene permitido enviar.

También puedes enviar un mensaje de prueba a ti mismo o a un compañero de equipo. Los envíos de prueba muestran la combinación de variantes específica que selecciones, no lo que el agente elegiría para un usuario en particular.

## Paso 5: Definir restricciones {#step-5-define-constraints}

Las restricciones evitan que el agente envíe contenido repetitivo al mismo usuario. Los siguientes niveles están disponibles:

- **Nivel de creatividad base:** Evita que la misma creatividad base se envíe a un usuario más de una vez dentro de un período que tú defines. Útil cuando cada creatividad base es lo suficientemente diferente como para que repetirla dentro de, por ejemplo, una semana resulte redundante.
- **Nivel de línea del asunto:** Evita que la misma línea del asunto se envíe a un usuario más de una vez dentro de un período que tú defines. Útil cuando las líneas del asunto son la señal de repetición más visible.

Las restricciones a nivel de variante sobre imágenes específicas o CTA no son compatibles en esta versión.

## Paso 6: Revisar y lanzar {#step-6-review-and-launch}

La pantalla **Revisar** muestra tu configuración completa: audiencia y división del grupo de control aleatorio, programación, creatividades base, recuento de variantes y restricciones activas. Revisa y resuelve cualquier advertencia de validación (por ejemplo, superposición de Segments con otra Campaign) que aparezca en esta sección.

Selecciona **Launch** para activar el agente. Este pasa de **Draft** a **Active** y comienza a enviar en el siguiente día elegible.

## Después del lanzamiento {#after-launch}

### Período de entrenamiento {#training-period}

Cuando tu agente se lanza, entra en un período de entrenamiento. Un indicador de entrenamiento se muestra en la interfaz de informes. El rendimiento puede fluctuar en los primeros días mientras el agente explora combinaciones. Los correos electrónicos continúan enviándose mientras aprende. No hay período de espera.

Los cambios significativos en el rendimiento aparecen después de que el agente sale del entrenamiento y pasa a la personalización activa. Los informes indican cuándo ocurre esa transición, para que siempre sepas en qué etapa se encuentra tu agente.

### Vistas de informes {#reporting-views}

La interfaz de informes ofrece tres vistas principales:

| Vista | Descripción |
|---|---|
| **Rendimiento** | Tasas de clics, métricas de participación y el incremento del grupo de Decisioning Studio en comparación con el grupo de control aleatorio. |
| **Configuración** | La configuración actual del agente, útil para confirmar lo que se está ejecutando. |
| **Preferencias del agente** | Recuentos de la frecuencia con la que el agente ha elegido cada variante, mostrando hacia qué se inclina el agente para tu audiencia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vistas de informes" }

Los desgloses a nivel de elemento muestran cómo las líneas del asunto, los CTA y las imágenes individuales rinden en todas las combinaciones.

### Editar un agente activo {#edit-an-active-agent}

Ve a la vista de **Configuración** para modificar la audiencia, el calendario, los creativos o las restricciones después del lanzamiento. La vista de Configuración muestra un resumen de los cambios. Promueve los cambios antes de que surtan efecto. Añadir nuevas variantes no reinicia el entrenamiento del agente en las variantes existentes; añade nuevas opciones al menú del agente.

### Pausar o detener {#pause-or-stop}

El ciclo de vida de un agente es **Borrador** > **Activo** > **Detenido**. Selecciona **Detener** en cualquier momento para detener un agente; deja de enviar y se reanuda cuando lo reactivas.

## Referencia {#reference}

La siguiente tabla resume las áreas de Decisioning Studio Go y los detalles relacionados.

| Área | Detalles |
|---|---|
| **Canal** | Solo correo electrónico |
| **Métrica de conversión** | Solo clics (clics diarios únicos por usuario) |
| **Puntos de personalización** | Línea del asunto, CTA, imagen principal (por creatividad base) |
| **Audiencia** | Un Segment de Braze, con control aleatorio obligatorio (mínimo 5%) |
| **Frecuencia** | Selección única (sin decisión de frecuencia) |
| **Envíos de prueba** | A través del creador de Braze |
| **Informes** | Vistas de rendimiento, configuración y preferencias del agente, además de desgloses a nivel de elemento |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Alcance de Decisioning Studio Go" }

### Consideraciones {#considerations}

- Los Content Blocks no son compatibles como puntos de sustitución de personalización.
- Las URL de las imágenes deben añadirse manualmente. Actualmente, la integración con la biblioteca de medios no es compatible.
- Los filtros de audiencia no son compatibles más allá de la selección de Segment.
- La personalización del cuerpo del texto, el preencabezado y el encabezado aún no están disponibles.

## Solución de problemas {#troubleshooting}

Contacta a tu administrador de éxito de cliente o consultor de soluciones para obtener ayuda con la configuración de agentes, la revisión de rendimiento o el diseño de programas.

Para preguntas frecuentes, consulta las [Preguntas frecuentes de Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq).