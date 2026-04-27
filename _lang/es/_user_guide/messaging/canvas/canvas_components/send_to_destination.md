---
nav_title: Enviar a destino
article_title: Enviar a destino
alias: "/send_to_destination/"
page_order: 11.5
page_type: reference
description: "Este artículo de referencia cubre el componente Enviar a destino y cómo usarlo en tus Canvas."
tool: Canvas
---

# Paso Enviar a destino

> El paso Enviar a destino te permite enviar usuarios de un Canvas a otro. Por ejemplo, si tienes dos Canvas que comparten mensajería para ofertas promocionales, puedes usar Enviar a destino para conectar estos Canvas.

## Cómo funciona

![Un paso Enviar a destino para enviar usuarios a un nuevo Canvas.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Tu Canvas actual con el paso Enviar a destino es la fuente. En el paso, puedes elegir el Canvas de destino. Desde aquí, los usuarios son enviados al Canvas de destino. Avanzarán por ese Canvas si cumplen los criterios de entrada y también continuarán fluyendo a través del Canvas de origen.

## Crear un paso Enviar a destino

### Paso 1: Añadir un paso

Arrastra y suelta el componente **Enviar a destino** desde la barra lateral, o selecciona el botón de signo más <i class="fas fa-plus-circle"></i> en la parte inferior de un paso y selecciona **Enviar a destino**.

### Paso 2: Elegir tu destino

Selecciona el menú desplegable o introduce el nombre del Canvas en el campo **Destino**. Luego, selecciona **Listo**.

![Un paso Enviar a destino configurado para enviar usuarios desde un Canvas llamado "Feature Adoption" a "New Canvas".]({% image_buster /assets/img/send_to_destination2.png %})

### Paso 3: Vista previa de tu destino

Puedes seleccionar **Vista previa del destino** para ver el recorrido de los usuarios que cumplen los criterios de entrada del Canvas de destino.

Después de configurar este paso en Canvas, puedes [previsualizar la ruta del usuario]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) para ver si un usuario avanza al siguiente paso en el Canvas actual y si también avanza al Canvas de destino.

## Preguntas frecuentes

### ¿Puedo establecer como destino un Canvas en borrador?

Sí. El Canvas de destino puede tener un estado de borrador o inactivo.

### ¿Se conservan las variables de contexto?

Sí. El [contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) del Canvas de origen siempre se pasa al Canvas de destino.