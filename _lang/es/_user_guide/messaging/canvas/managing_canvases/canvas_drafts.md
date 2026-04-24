---
nav_title: Guardar borradores para Canvas
article_title: Guardar borradores para Canvas
alias: "/save_as_draft/"
page_order: 1
description: "Este artículo de referencia explica cómo guardar un borrador para un Canvas que ya se ha lanzado."
page_type: reference
tool: Canvas
---

# Guardar borradores para Canvas

> A medida que creas y lanzas Canvas, puedes editar un Canvas activo y guardarlo como borrador, lo que te permite probar tus cambios antes de otro lanzamiento. 

Si tienes un Canvas activo que requiere cambios a gran escala, puedes usar esta característica para crear, guardar y verificar la calidad **antes** de lanzar estos cambios en el Canvas activo. 

Como con cualquier Canvas, solo un usuario puede editar un borrador a la vez, y un Canvas solo puede tener un borrador a la vez. Estos borradores no tienen análisis porque los cambios del borrador aún no se han lanzado.

![Un ejemplo de borrador de Canvas con un banner que indica al usuario que está editando un borrador de Canvas con la opción de ver el Canvas activo. El pie de página tiene opciones para volver a la vista de análisis, guardar como borrador o lanzar el borrador.]({% image_buster /assets/img_archive/canvas_draft1.png %})

## Crear un borrador

Para crear un borrador:

1. Ve a un Canvas activo.
2. Selecciona el botón **Guardar como borrador** en el pie de página del Canvas. 

Ten en cuenta que no se pueden realizar ediciones en el Canvas activo mientras exista un borrador del Canvas. Puedes actualizar el Canvas para aplicar los cambios o descartar el borrador.

## Consultar el borrador activo

Para consultar el Canvas activo, selecciona **Ver Canvas activo** en el pie de página desde la vista de análisis o en el encabezado del Canvas desde el borrador. Para volver a un Canvas activo, selecciona **Modificar borrador** desde la vista de análisis o la vista del Canvas activo.

Solo puedes hacer referencia a pasos que ya se hayan lanzado antes de que se creara el borrador. Esto significa que si creaste un paso o canal **después** de que se creara el borrador, no se puede hacer referencia a él en tu borrador.

{% alert note %}
Si se hace referencia a un bloque de contenido en un borrador de Canvas, el Canvas se incluye en el recuento de inclusiones del bloque de contenido. Sin embargo, si se hace referencia al bloque de contenido en un borrador de un Canvas **activo**, el Canvas no se incluirá en el recuento de inclusiones del bloque de contenido.
{% endalert %}

### Priorización de mensajes dentro de la aplicación

Para borradores de un Canvas activo, la prioridad de los mensajes dentro de la aplicación en el generador de Canvas se actualizará inmediatamente cuando un usuario cambie la prioridad. Esto significa que la prioridad de los mensajes dentro de la aplicación a nivel de Canvas se aplica al Canvas activo de inmediato, incluso cuando existe un borrador. 

Sin embargo, los cambios de prioridad de los mensajes dentro de la aplicación a nivel de paso se guardan como borrador y se aplican cuando se actualiza el Canvas. Por ejemplo, en un paso de mensaje, el clasificador de prioridad se actualizará cuando un usuario lance el borrador, ya que la configuración del paso se aplica a nivel de paso.