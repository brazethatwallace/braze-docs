---
nav_title: Historial de versiones de Canvas
article_title: Historial de versiones de Canvas
alias: "/canvas_version_history/"
page_order: 2
description: "Este artículo de referencia explica cómo administrar el historial de versiones de tu Canvas."
page_type: reference
tool: Canvas
---

# Historial de versiones de Canvas {#canvas-version-history}

> El historial de versiones te permite ver y acceder a los análisis de Canvas y a los recorridos de usuario de cualquier versión anterior de tu Canvas.

Consultar el historial de versiones de tu Canvas puede ser especialmente útil para mantener un registro de la evolución de un Canvas. Por ejemplo, si realizas un cambio a gran escala, puedes consultar versiones anteriores del Canvas para comprender mejor cómo han progresado tus flujos de trabajo.

{% alert tip %}
Para obtener una lista completa de los Canvas en tu espacio de trabajo (por ejemplo, para una auditoría), usa el [punto de conexión Exportar lista de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) y pagina a través de los resultados.
{% endalert %}

## Administrar versiones {#managing-versions}

![]({% image_buster /assets/img_archive/canvas_version_history.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Para crear una nueva versión, haz clic en **Actualizar Canvas**. Esto te permite realizar cambios sin sobrescribir la configuración anterior del Canvas. Cuando se crea una nueva versión del Canvas, los usuarios que ya están en el Canvas avanzarán a través del flujo de trabajo de la nueva versión. Los usuarios que entren al Canvas también ingresarán a la nueva versión.

Para acceder al historial de versiones, ve a los detalles de tu Canvas en la parte superior de tu Canvas y selecciona **# Versiones**. Aquí tienes acceso a la barra lateral del **Historial de versiones**. Selecciona cualquiera de las versiones del Canvas en la barra lateral para ver y comparar los detalles del Canvas. Para alternar entre los análisis del Canvas y la configuración del Canvas, haz clic en **Ver análisis** o **Ver Canvas** en la barra de herramientas inferior.

{% alert note %}
Los Canvas que aparecen en el **Historial de versiones** son de solo lectura.
{% endalert %}

Para ver una lista de los cambios realizados en una versión mientras estaba activa, selecciona **Ver cambios** en la barra lateral del historial de versiones. También puedes ver todos los cambios asociados a una versión en el registro de cambios del Canvas.

Ten en cuenta que si no realizaste ninguna edición entre el lanzamiento de un Canvas y la creación de una segunda versión, no aparecerán cambios en **Ver cambios** para la primera versión del Canvas.

A medida que aumenta el número de versiones en tu historial, también puedes renombrar cada versión en la barra lateral para mantenerte organizado. De forma predeterminada, los nombres de las versiones se generan como un número basado en cuántas versiones se han creado previamente. Si renombras una versión mientras ya no está activa, esto aparecerá en el registro de cambios del Canvas, pero no en el registro de cambios de la versión dentro de la vista del historial de versiones.

![Ejemplo de registro de cambios de Canvas que muestra que se han creado dos nuevas versiones de Canvas.]({% image_buster /assets/img_archive/canvas_version_history_changelog.png %}){: style="max-width:85%" }

### Descartar versiones {#discarding-versions}

Puedes crear hasta 10 versiones por Canvas. Si alcanzas este límite, puedes descartar una versión para hacer espacio para una nueva. Ten en cuenta que las versiones se descartan al hacer clic en **Descartar**, no cuando actualizas el Canvas. Descartar una versión se refleja en el registro de cambios general del Canvas, no en el registro de cambios de una versión específica.

Si descartas una versión, la configuración del Canvas se perderá de inmediato, pero los análisis asociados a la versión descartada se conservarán.

## Ver análisis {#viewing-analytics}

Dentro del historial de versiones, puedes ver análisis a nivel de Canvas y a nivel de pasos. En la vista de versión del Canvas, los datos se completarán para todo el rango de fechas, no solo para el rango de fechas de esa versión. Sin embargo, a nivel de paso, los análisis solo se mostrarán para los pasos que existían mientras esa versión estaba activa. Estos análisis se completarán usando días de calendario que corresponden a la zona horaria de tu empresa, por lo que los análisis no serán específicos de la hora exacta del día en que se creó la versión.