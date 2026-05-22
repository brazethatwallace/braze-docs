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

> El paso Enviar a destino te permite enviar usuarios de un Canvas a otro. Por ejemplo, si tienes dos Canvas que comparten mensajería para ofertas promocionales, puedes usar Enviar a destino para conectar estos Canvas.

## Cómo funciona {#how-it-works}

![Un paso Enviar a destino para enviar usuarios a un nuevo Canvas.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Tu Canvas actual con el paso Enviar a destino es la fuente. En el paso, puedes elegir el Canvas de destino. Los usuarios entrantes del Canvas de origen deben seguir las reglas de entrada del Canvas de destino. Supongamos que tienes dos Canvas:

- **Fuente:** Canvas 1, incluye un paso Enviar a destino que envía usuarios al Canvas 2
- **Destino:** Canvas 2, con los criterios de entrada para admitir usuarios que hayan realizado un pedido

Este paso permite que los usuarios del Canvas 1 sean enviados al Canvas 2. Cuando los usuarios del Canvas 1 entran en el paso Enviar a destino, son evaluados por las reglas de entrada del Canvas 2 para determinar si son elegibles para entrar en el Canvas. En este caso, los usuarios que hayan realizado un pedido pueden entrar en el Canvas 2 y también continuar su recorrido en el Canvas 1. Para los usuarios que no hayan realizado un pedido, continúan su recorrido solo en el Canvas 1.

## Crear un paso Enviar a destino {#create-a-send-to-destination-step}

### Paso 1: Añadir un paso {#step-1-add-a-step}

Arrastra y suelta el componente **Send to Destination** desde la barra lateral, o selecciona el botón de signo más <i class="fas fa-plus-circle"></i> en la parte inferior de un paso y selecciona **Send to Destination**.

### Paso 2: Elegir tu destino {#step-2-choose-your-destination}

Selecciona el menú desplegable o introduce el nombre del Canvas en el campo **Destination**. Luego, selecciona **Done**.

![Un paso Enviar a destino configurado para enviar usuarios desde un Canvas llamado "Feature Adoption" a "New Canvas".]({% image_buster /assets/img/send_to_destination2.png %})

### Paso 3: Vista previa de tu destino {#step-3-preview-your-destination}

Puedes seleccionar **Preview destination** para ver el recorrido de los usuarios que cumplen los criterios de entrada del Canvas de destino.

Después de configurar este paso en Canvas, puedes [previsualizar la ruta del usuario]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths/) para ver si un usuario avanza al siguiente paso en el Canvas actual y si también avanza al Canvas de destino.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Puedo establecer como destino un Canvas en borrador? {#can-i-set-the-destination-to-a-draft-canvas}

Sí. El Canvas de destino puede tener un estado de borrador o inactivo.

### ¿Se conservan las variables de contexto? {#are-context-variables-preserved}

Sí. El [contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/) del Canvas de origen siempre se pasa al Canvas de destino.

### ¿Los usuarios entran al inicio del Canvas de destino? {#do-users-enter-at-the-start-of-the-destination-canvas}

Los usuarios entran al inicio del Canvas de destino. En este momento, no puedes vincular a un paso en Canvas específico dentro del Canvas de destino.

### ¿Cómo funciona el comportamiento de avance en los pasos Enviar a destino? {#how-does-advancement-behavior-work-for-send-to-destination-steps}

Los usuarios que entran en el paso Enviar a destino continúan su recorrido si hay pasos adicionales en el Canvas de origen. Si los usuarios también cumplen las reglas de entrada del Canvas de destino, pueden entrar en ese Canvas y comenzar ese recorrido.