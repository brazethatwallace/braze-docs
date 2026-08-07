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

![Un paso Enviar al destino para enviar usuarios a un nuevo Canvas.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Tu Canvas actual con el paso Enviar al destino es el origen. Dentro del paso, puedes elegir el Canvas de destino. Los usuarios del Canvas de origen deben cumplir los criterios de audiencia del Canvas de destino. Supongamos que tienes dos Canvas:

- **Origen:** Canvas 1, incluye un paso Enviar al destino que envía usuarios al Canvas 2
- **Destino:** Canvas 2, con criterios de audiencia para que entren usuarios que hayan realizado un pedido

Este paso permite que los usuarios del Canvas 1 sean enviados al Canvas 2. Cuando los usuarios del Canvas 1 llegan al paso Enviar al destino, se evalúan según los criterios de audiencia del Canvas 2 para determinar si son elegibles para entrar en el Canvas. En este caso, los usuarios que hayan realizado un pedido pueden entrar en el Canvas 2 y también continuar su recorrido en el Canvas 1. Los usuarios que no hayan realizado un pedido continúan su recorrido únicamente en el Canvas 1.

### Comportamiento de entrada {#entry-behavior}

El paso Enviar al destino hace que los usuarios entren en el Canvas de destino en cuanto llegan a este paso. Este paso actúa como un punto de entrada único al Canvas de destino. Los usuarios que cumplen los criterios de audiencia del Canvas de destino comienzan ese recorrido en Canvas. Los usuarios que no cumplen esos criterios en ese momento no entran en el Canvas de destino y continúan en el Canvas de origen.

Enviar al destino también respeta la [configuración de reentrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) del Canvas de destino en **Entry Controls**. Si un usuario no es elegible para reingresar al Canvas de destino, no se le envía a él y continúa en el Canvas de origen.

Si el Canvas de destino utiliza una programación de entrada programada, el paso Enviar al destino omite esa programación de entrada. También omite [**Limit entrance volume**]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) en **Entry Controls** del Canvas de destino cuando está configurado como **Every time Canvas is schedule**. Los usuarios enviados desde este paso no esperan a la siguiente ventana de evaluación programada: se evalúan según los criterios de audiencia del Canvas de destino y entran de inmediato cuando llegan al paso Enviar al destino.

Si el Canvas de destino utiliza una entrada basada en acciones, el paso Enviar al destino omite el requisito de que los usuarios realicen la acción de entrada configurada para entrar en ese Canvas.

## Crea un paso Enviar a destino {#create-a-send-to-destination-step}

### Paso 1: Añade un paso {#step-1-add-a-step}

Arrastra y suelta el componente **Enviar a destino** desde la barra lateral, o selecciona el botón de signo más <i class="fas fa-plus-circle"></i> en la parte inferior de un paso y selecciona **Enviar a destino**.

### Paso 2: Elige tu destino {#step-2-choose-your-destination}

Selecciona el menú desplegable o introduce el nombre del Canvas en el campo **Destino**. Luego, selecciona **Listo**.

![Un paso Enviar a destino configurado para enviar usuarios desde un Canvas llamado "Feature Adoption" a "New Canvas".]({% image_buster /assets/img/send_to_destination2.png %})

### Paso 3: Previsualiza tu destino {#step-3-preview-your-destination}

Puedes seleccionar **Vista previa del destino** para ver el Canvas al que estás enviando a los usuarios.

Después de configurar este paso en Canvas, puedes [previsualizar la ruta del usuario]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) para ver si un usuario avanza al siguiente paso en el Canvas actual y si también avanza al Canvas de destino.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Puedo establecer el destino como un Canvas en borrador? {#can-i-set-the-destination-to-a-draft-canvas}

Sí. El Canvas de destino puede tener un estado de borrador o inactivo.

### ¿Se conservan las variables de contexto? {#are-context-variables-preserved}

Sí. El [contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) del Canvas de origen se pasa al Canvas de destino. Sin embargo, las variables de contexto deben invocarse dentro del Canvas de origen para que se pasen al Canvas de destino.

### ¿Puedo usar el paso Enviar al destino para conectar Canvas en lugar de usar soluciones alternativas con API o Actualización de usuario? {#can-i-use-the-send-to-destination-step-to-connect-canvases-instead-of-using-api-or-user-update-workarounds}

Sí. Puedes conectar Canvas con el paso Enviar al destino cuando los usuarios deban pasar directamente a otro recorrido de Canvas.

No necesitas pasos separados de Actualización de usuario, desencadenadores de API ni webhooks únicamente para mover usuarios entre Canvas, siempre que cumplan los criterios de audiencia del Canvas de destino en el momento del envío.

### ¿Los usuarios entran al inicio del Canvas de destino? {#do-users-enter-at-the-start-of-the-destination-canvas}

Los usuarios elegibles entran inmediatamente en el primer paso del Canvas de destino. No esperan a un horario de entrada programado posterior en el Canvas de destino. No puedes vincular a un paso en Canvas específico dentro del Canvas de destino.

### ¿El paso Enviar al destino respeta el calendario de entrada programado del Canvas de destino? {#does-the-send-to-destination-step-respect-a-scheduled-destination-canvas-entry-schedule}

No. Si el Canvas de destino usa un tipo de entrada programada, los usuarios enviados desde el paso Enviar al destino no esperan a la siguiente ventana de evaluación programada. Se evalúan según los criterios de audiencia y entran inmediatamente cuando alcanzan el paso Enviar al destino.

### ¿Cómo funciona el comportamiento de avance en los pasos Enviar al destino? {#how-does-advancement-behavior-work-for-send-to-destination-steps}

Los usuarios que entran en el paso Enviar al destino continúan su recorrido de usuario si hay pasos adicionales en el Canvas de origen. Si los usuarios también cumplen los criterios de audiencia del Canvas de destino, pueden entrar en ese Canvas y comenzar ese recorrido.