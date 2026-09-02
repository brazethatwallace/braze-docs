---
nav_title: Plantillas de Canvas
article_title: Crear una plantilla de Canvas
page_order: 2
alias: "/canvas_templates/"
description: "Crea y gestiona plantillas de Canvas reutilizables, o empieza con plantillas prediseñadas de Braze para casos de uso comunes."
---

# Crear una plantilla de Canvas {#create-a-canvas-template}

> Este artículo de referencia explica cómo crear y gestionar plantillas para Canvas. Usar plantillas puede mejorar tu mensajería creando un marco coherente que se puede personalizar fácilmente para adaptarse a tus objetivos específicos en tus Canvas.

{% alert tip %}
Ahorra tiempo y agiliza la creación de tu Canvas utilizando las [plantillas de BRAZE Canvas](#available-braze-templates). Explora nuestra biblioteca de plantillas prediseñadas para encontrar una que se ajuste a tu caso de uso y personalízala para satisfacer tus necesidades específicas.
{% endalert %}

## Método 1: Crear a partir de un Canvas existente {#method-1-create-from-an-existing-canvas}

### Paso 1: Selecciona tu Canvas existente {#step-1-select-your-existing-canvas}

En el dashboard de Braze, ve a **Mensajería** > **Canvas** y selecciona un Canvas existente que quieras usar como plantilla.

### Paso 2: Crea tu plantilla {#step-2-create-your-template}

En el editor de Canvas, selecciona **Modificar Canvas** o **Modificar borrador**, dependiendo de si tu Canvas está activo o en borrador. Expande el desplegable **Guardar como borrador** en el pie de página y selecciona **Guardar como plantilla**.


### Paso 3: Guarda tu plantilla {#step-3-save-your-template}

A continuación, dale un nombre a tu plantilla y añade las etiquetas relevantes. Luego, selecciona **Guardar**. Tu plantilla ya está lista para usarse al crear un Canvas, dándote una ventaja con la configuración básica y los pasos ya establecidos.

## Método 2: Crear a través del editor de plantillas de Canvas {#method-2-create-via-canvas-template-editor}

### Paso 1: Ve al editor de plantillas de Canvas {#step-1-go-to-the-canvas-template-editor}

En el dashboard de Braze, ve a **Contenido** > **Canvas**.

### Paso 2: Crea una nueva plantilla {#step-2-create-a-new-template}

Selecciona **Crear plantilla** y comienza a configurar los detalles de tu Canvas. Puedes empezar dándole un nombre a tu plantilla de Canvas.

![Un ejemplo de plantilla de Canvas llamada "Annual sale Canvas template" con la descripción "Use for annual spring promotion".]({% image_buster /assets/img/canvas_template_example.png %})

### Paso 3: Personaliza tu plantilla {#step-3-customize-your-template}

A continuación, personaliza tu plantilla [configurando tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas). Puedes decidir cuándo los usuarios deben entrar al Canvas, determinar qué usuarios pueden entrar a este Canvas, ajustar tus ajustes de envío y construir el recorrido del usuario para la plantilla.

### Paso 4: Guarda tu plantilla {#step-4-save-your-template}

Cuando hayas terminado de personalizar tu plantilla, selecciona el botón **Guardar plantilla**. En la página **Plantilla de Canvas**, puedes ver los detalles de tu plantilla de Canvas seleccionando <i class="fas fa-list"></i> **Detalles de la plantilla**.

## Uso de plantillas de Canvas {#using-canvas-templates}

Hay dos formas de usar tu plantilla al crear un Canvas:

- **Desde Mensajería**: Ve a **Mensajería** > **Canvas**. Selecciona el botón **Crear Canvas** y **Usar una plantilla de Canvas**.
- **Desde Contenido**: Ve a **Contenido** > **Canvas** y encuentra la plantilla deseada en **Plantillas de Canvas**. Luego, selecciona el menú <i class="fas fa-ellipsis-vertical"></i> seguido de **Aplicar plantilla**. Esto te llevará a un nuevo Canvas con la plantilla aplicada en el compositor de Canvas.

### Plantillas de Braze disponibles {#available-braze-templates}

Para ver una lista de las plantillas de Canvas disponibles, consulta [Plantillas de Canvas de Braze]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates). Para obtener detalles sobre el uso de plantillas de Canvas de comercio electrónico, consulta [Cómo usar eventos recomendados de comercio electrónico]({{site.baseurl}}/ecommerce_use_cases).

## Gestión de plantillas de Canvas {#managing-canvas-templates}

Las plantillas de Canvas se pueden duplicar y archivar, de forma similar a un Canvas real. Para editar una plantilla de Canvas, selecciona la plantilla y luego **<i class="fas fa-pencil-alt"></i>Editar**.

A nivel de espacio de trabajo, puedes actualizar los permisos de usuario para permitir o limitar el acceso para crear, editar, ver o archivar plantillas de Canvas.

### Permisos para equipos y espacios de trabajo {#permissions-for-teams-and-workspaces}

Para permitir que solo ciertos usuarios accedan y usen plantillas de Canvas específicas, [añade un equipo]({{site.baseurl}}/user_guide/administer/global/user_management/teams) a las plantillas y luego asigna permisos a nivel de equipo de "Acceder a Campaigns, Canvas, Content Cards, Content Blocks, conmutadores de características, Segments, Biblioteca de medios y centro de preferencias".

Si asignas alguno de los siguientes permisos a nivel de equipo, pero no a nivel de espacio de trabajo, solo podrás hacer lo siguiente asignado a tu equipo:

- Crear y editar plantillas de Canvas
- Ver plantillas de Canvas
- Archivar plantillas de Canvas

Si los permisos se otorgan tanto a nivel de espacio de trabajo como de equipo, los permisos a nivel de espacio de trabajo tendrán prioridad.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Puedo guardar un paso incompleto en una plantilla de Canvas? {#can-i-save-an-incomplete-step-in-a-canvas-template}

Sí, puedes guardar pasos incompletos como plantilla de Canvas. Sin embargo, cuando se use la plantilla, habrá un error en el botón **Guardar plantilla** que indicará lo que se necesita para lanzar el Canvas.

### ¿Puedo guardar la configuración de mi constructor de Canvas como plantilla, o solo puedo guardar pasos? {#can-i-save-my-canvas-builder-settings-as-a-template-or-can-i-only-save-steps}

Sí, puedes guardar la configuración del constructor de Canvas dentro de una plantilla de Canvas. Por ejemplo, si planeas usar una combinación de segmentos y filtros con frecuencia, puedes guardar esta configuración de **Público objetivo** como parte de tu plantilla de Canvas.