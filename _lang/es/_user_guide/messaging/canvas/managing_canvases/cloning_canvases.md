---
nav_title: Clonar Canvas
article_title: Clonar Canvas
page_order: 3
alias: "/cloning_canvases/"
description: "Este artículo de referencia describe cómo clonar un Canvas del editor original de Canvas al flujo de trabajo de Canvas Flow."
tool: Canvas
---

# Clonar Canvas a Canvas Flow {#clone-canvases-to-canvas-flow}

> Si tienes un Canvas existente del editor original, puedes clonar este Canvas para crear una copia en Canvas Flow. Al cambiar al flujo de trabajo actual de Canvas, obtienes acceso a [componentes de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/) ligeros, [propiedades de entrada persistentes]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#canvas-entry-properties) y [edición posterior al lanzamiento]({{site.baseurl}}/post-launch_edits/). Tu Canvas original no se modificará ni eliminará.

{% alert important %}
Ya no puedes crear ni duplicar Canvas con la experiencia original de Canvas. Braze recomienda que los clientes que usan la experiencia original de Canvas migren a Canvas Flow, la experiencia actual de Canvas.
{% endalert %}

Para clonar tu Canvas, haz lo siguiente:

1. Ve al dashboard de Canvas.
2. Identifica el Canvas del que quieres crear una copia en el flujo de trabajo de Canvas Flow. Puedes clonar Canvas con estado **Draft**, **Active** o **Stopped**.
3. Haz clic en <i class="fas fa-ellipsis-vertical"></i> **More actions** y selecciona **Clone to Canvas Flow**.

![]({% image_buster /assets/img_archive/clone_to_v2_workflow.png %}){: style="max-width:25%;"}

{: start="4"}
4. Introduce el nombre de tu nuevo Canvas y haz clic en **Clone to Canvas Flow**.

![]({% image_buster /assets/img_archive/clone_to_v2_modal.png %}){: style="max-width:70%;"}

Ahora tienes dos versiones de tu Canvas: el Canvas original y la versión de Canvas Flow. Tu Canvas original conserva su estado original, y el Canvas clonado tiene un estado de **Draft**. Aún puedes acceder al Canvas original, pero Braze recomienda usar el flujo de trabajo de Canvas Flow para seguir construyendo tus Canvas.

Anteriormente, algunos Canvas con ramificaciones no se podían clonar. Ahora puedes clonar Canvas con ramificaciones. Ten en cuenta que clonar Canvas con ramificaciones puede generar pasos desconectados. Resuelve estos pasos desconectados (pasos que no tienen un paso anterior conectado a ellos) para asegurarte de que el recorrido de tu Canvas esté mapeado correctamente.

{% alert note %}
Si clonas un Canvas activo, Braze seguirá enviando usuarios a través del Canvas original. Recomendamos detener un Canvas antes de clonarlo para evitar enviar mensajes duplicados a los usuarios desde ambos Canvas.
{% endalert %}

![Dashboard de Canvas con dos Canvas listados: V2 Copy of Canvas V1 y Canvas V1. La copia V2 de Canvas V1 tiene un icono que indica que está usando el flujo de trabajo de Canvas Flow.]({% image_buster /assets/img_archive/clone_to_v2_dashboard.png %})

¡Has completado la clonación de tu Canvas al flujo de trabajo de Canvas Flow! Ahora puedes seguir construyendo tus Canvas en esta experiencia actualizada.

## Recomendaciones {#recommendations}

Para permitir que los usuarios existentes continúen su recorrido después de haber clonado tu Canvas original a Canvas Flow, puedes añadir filtros a tu Canvas existente que impidan que nuevos usuarios entren al nuevo Canvas.

Si la reelegibilidad está desactivada, añade el filtro "Entered Canvas Variation". Si la reelegibilidad está activada, estos son los métodos posibles a considerar para asegurarte de que los usuarios no entren al mismo Canvas dos veces:
- Actualiza el Canvas existente para incluir una etiqueta única. Para el nuevo Canvas, añade un filtro "Last Received Message from Campaign or Canvas with Tag". Esto evita que los usuarios entren al Canvas dos veces después de una fecha de entrada específica (número total de días después de que se envía el último mensaje del Canvas original más la ventana de conversión).
- **El siguiente método registrará puntos de datos.** Actualiza el Canvas original para incluir un webhook de Braze a Braze que desencadene un atributo personalizado de marca de tiempo de fecha al entrar. Este atributo se puede usar para evitar que los usuarios entren al nuevo Canvas después de la fecha especificada (número total de días después de que se envía el último mensaje del Canvas original más la ventana de conversión).

Para Canvas desencadenados por API, coordina con tu equipo de ingeniería para asegurarte de que estos Canvas estén usando el nuevo ID de Canvas cuando los nuevos Canvas estén listos para lanzar.

Para más información sobre las diferencias entre el editor original de Canvas y la experiencia de Canvas Flow, consulta las [preguntas frecuentes de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/faqs/#what-are-the-main-differences-between-canvas-flow-and-the-original-canvas-editor).