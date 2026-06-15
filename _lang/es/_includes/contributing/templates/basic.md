Puedes utilizar esta plantilla para crear cualquier página o sección para Braze Docs. Para la configuración del entorno, vistas previas y tipos de contenido, quienes tengan acceso al repositorio deben seguir el manual en `docs/contributing/` (por ejemplo, `generating_a_preview.md` y `content_types.md`). El resto puede usar [Comentarios sobre la documentación]({{site.baseurl}}/feedback/) para contactar al equipo de documentación.

{% details Mostrar plantilla %}
{% raw %}
`````markdown
---
nav_title: NAV_TITLE
article_title: ARTICLE_TITLE
description: "SHORT_DESCRIPTION."
alias: /OPTIONAL_SHORT_ARTICLE_TITLE/
page_type: reference
layout: OPTIONAL_LAYOUT_FILE
---

<!-- El título de tu página, utilizado para renderizar el título dentro de la página. -->
# ARTICLE_TITLE

<!-- El resumen comienza con un carácter '>' y describe lo que se cubrirá. En un párrafo siguiente opcional, contextualiza el tema a alto nivel en una introducción. -->
> DESCRIPTION.

INTRODUCTION.

<!-- Los requisitos previos para esta tarea. Si no se necesitan requisitos previos, puedes eliminar esta sección. -->
## Requisitos previos

Antes de empezar, tendrás que completar lo siguiente:

- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE

<!-- Una explicación breve y opcional de cómo funciona el flujo de trabajo de la característica. -->
## Cómo funciona

CONTENT.

<!-- Guía al usuario a través de la integración y activación de la característica. -->
 ## Integración
CONTENT.

<!-- Una guía práctica con pasos anidados. -->
## TASK_TO_COMPLETE

<!-- Resumen opcional de la tarea. -->
CONTENT.

<!-- Encabezado orientado a la acción que describe el objetivo del paso. -->
### Paso 1: ACTION_TO_COMPLETE

<!-- Usa viñetas numeradas o párrafos para describir cómo completar esta acción. -->
CONTENT.

### Paso 2: ACTION_TO_COMPLETE

CONTENT.
<!-- Referencias opcionales, como tipos de datos compatibles, campos, definiciones y similares. -->
### REFERENCE_TO_ASSIST_WITH_ACTION

CONTENT.

<!-- Para pasos opcionales, añade "(opcional)" al final del encabezado. -->
### Paso 3: OPTIONAL_ACTION_TO_COMPLETE (opcional)

CONTENT.
<!-- Una sección opcional para lo que es compatible. Añade encabezados anidados para ser más específico. -->
## Tipos de datos compatibles / Atributos compatibles / Eventos compatibles / ETC. compatibles
CONTENT.
<!-- Una sección opcional con consideraciones importantes que los usuarios deben revisar antes de usar la característica. -->
## Consideraciones

CONTENT.

<!-- Una sección opcional que guía a los usuarios en la solución de problemas comunes. -->
## Solución de problemas

### ISSUE_TO_TROUBLESHOOT
CONTENT.

`````
{% endraw %}
{% enddetails %}