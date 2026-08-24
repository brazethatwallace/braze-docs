---
nav_title: Enviar a destino
article_title: Enviar a destino
alias: "/send_to_destination/"
page_order: 11.5
page_type: reference
description: "Este artículo de referencia cubre el componente Enviar a destino y cómo usarlo en tus Canvas."
tool: Canvas
---

# Paso Enviar a destino {#send-to-destination-step}

> El paso Enviar a destino te permite enviar usuarios de un Canvas a otro. Por ejemplo, puedes conectar Canvas que comparten mensajería para ofertas promocionales.

## Cómo funciona {#how-it-works}

![Un paso Enviar a destino para enviar usuarios a un nuevo Canvas.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Tu Canvas actual con el paso Enviar a destino es el origen. Dentro del paso, puedes elegir el Canvas de destino. Los usuarios del Canvas de origen deben cumplir los criterios de audiencia del Canvas de destino. Supongamos que tienes dos Canvas:

- **Origen:** Canvas 1, incluye un paso Enviar a destino que envía usuarios al Canvas 2
- **Destino:** Canvas 2, con criterios de audiencia para admitir usuarios que hayan realizado un pedido

Este paso permite que los usuarios del Canvas 1 sean enviados al Canvas 2. Cuando los usuarios del Canvas 1 entran en el paso Enviar a destino, se evalúan según los criterios de audiencia del Canvas 2 para determinar si son elegibles para entrar en el Canvas. En este caso, los usuarios que hayan realizado un pedido pueden entrar en el Canvas 2 y también continuar su recorrido en el Canvas 1. Los usuarios que no hayan realizado un pedido continúan su recorrido únicamente en el Canvas 1.

### Comportamiento de entrada {#entry-behavior}

El paso Enviar a destino hace que los usuarios entren en el Canvas de destino en cuanto alcanzan este paso. Este paso actúa como un punto de entrada único en el Canvas de destino. Los usuarios que cumplen los criterios de audiencia del Canvas de destino comienzan ese recorrido del Canvas. Los usuarios que no cumplen esos criterios en ese momento no entran en el Canvas de destino y continúan en el Canvas de origen.

Enviar a destino también respeta la [configuración de reentrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) del Canvas de destino en **Entry Controls**. Si un usuario no es elegible para volver a entrar en el Canvas de destino, no se le envía a él y continúa en el Canvas de origen.

Si el Canvas de destino usa un calendario de entrada programado, el paso Enviar a destino omite ese calendario de entrada. También omite [**Limit entrance volume**]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) en **Entry Controls** del Canvas de destino cuando está configurado como **Every time Canvas is schedule**. Los usuarios enviados desde este paso no esperan a la siguiente ventana de evaluación programada: se evalúan según los criterios de audiencia del Canvas de destino y entran de inmediato cuando alcanzan el paso Enviar a destino.

Si el Canvas de destino usa una entrada basada en acciones, el paso Enviar a destino omite el requisito de que los usuarios realicen la acción de entrada configurada para entrar en ese Canvas.

## Crear un paso de Enviar a destino {#create-a-send-to-destination-step}

### Paso 1: Agregar un paso {#step-1-add-a-step}

Arrastra y suelta el componente **Enviar a destino** desde la barra lateral, o selecciona el botón de más <i class="fas fa-plus-circle"></i> en la parte inferior de un paso y selecciona **Enviar a destino**.

### Paso 2: Elegir tu destino {#step-2-choose-your-destination}

Selecciona el menú desplegable o introduce el nombre del Canvas en el campo **Destino**. Luego, selecciona **Listo**.

![Un paso de Enviar a destino configurado para enviar usuarios de un Canvas llamado "Feature Adoption" a "New Canvas".]({% image_buster /assets/img/send_to_destination2.png %})

### Paso 3: Previsualizar tu destino {#step-3-preview-your-destination}

Puedes seleccionar **Vista previa del destino** para ver el Canvas al que estás enviando usuarios.

Después de configurar este paso en Canvas, puedes [previsualizar la ruta del usuario]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) para ver si un usuario avanza al siguiente paso en el Canvas actual y si también avanza al Canvas de destino.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Puedo configurar el destino como un Canvas en borrador? {#can-i-set-the-destination-to-a-draft-canvas}

Sí. El Canvas de destino puede tener un estado de borrador o inactivo.

### ¿Se conservan las variables de contexto? {#are-context-variables-preserved}

Sí. El [contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) del Canvas de origen se pasa al Canvas de destino. Sin embargo, las variables de contexto deben invocarse dentro del Canvas de origen para que se pasen al Canvas de destino.

### ¿Puedo usar el paso Enviar al destino para conectar Canvas en lugar de usar soluciones alternativas con API o actualización de usuarios? {#can-i-use-the-send-to-destination-step-to-connect-canvases-instead-of-using-api-or-user-update-workarounds}

Sí. Puedes conectar Canvas con el paso Enviar al destino cuando los usuarios deben pasar directamente a otro recorrido en Canvas.

No necesitas pasos separados de actualización de usuarios, desencadenantes de API ni webhooks solo para mover usuarios entre Canvas, siempre que cumplan los criterios de audiencia del Canvas de destino cuando se envían.

### ¿Los usuarios entran al inicio del Canvas de destino? {#do-users-enter-at-the-start-of-the-destination-canvas}

Los usuarios elegibles entran inmediatamente en el primer paso del Canvas de destino. No esperan a una hora de entrada programada posterior en el Canvas de destino. No puedes vincular a un paso en Canvas específico dentro del Canvas de destino.

### ¿El paso Enviar al destino respeta el programa de entrada programada del Canvas de destino? {#does-the-send-to-destination-step-respect-a-scheduled-destination-canvas-entry-schedule}

No. Si el Canvas de destino usa un tipo de entrada programada, los usuarios enviados desde el paso Enviar al destino no esperan a la siguiente ventana de evaluación programada. Se evalúan contra los criterios de audiencia y entran inmediatamente cuando alcanzan el paso Enviar al destino.

### ¿Cómo funciona el comportamiento de avance en los pasos Enviar al destino? {#how-does-advancement-behavior-work-for-send-to-destination-steps}

Los usuarios que entran en el paso Enviar al destino continúan su recorrido de usuario si hay pasos adicionales en el Canvas de origen. Si los usuarios también cumplen con los criterios de audiencia del Canvas de destino, pueden entrar en ese Canvas y comenzar ese recorrido.

### ¿El paso Enviar al destino está sujeto a límites de velocidad de API? {#is-the-send-to-destination-step-subject-to-api-rate-limits}

No. Los usuarios se envían entre Canvas dentro de Braze sin realizar llamadas externas a la API.