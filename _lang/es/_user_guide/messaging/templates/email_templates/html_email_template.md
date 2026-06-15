---
nav_title: Cargar una plantilla de correo electrónico HTML
article_title: Cargar una plantilla de correo electrónico HTML
page_order: 2
description: "Este artículo de referencia explica cómo crear, administrar y solucionar problemas de una plantilla de correo electrónico HTML usando el dashboard de Braze."
tool:
  - Templates
channel:
  - email

---

# Cargar una plantilla de correo electrónico HTML {#upload-an-html-email-template}

> El dashboard de Braze te permite cargar tus propias plantillas de correo electrónico HTML y guardarlas para usarlas más adelante en campañas. También puedes [crear una plantilla de correo electrónico]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template/) usando nuestro editor.

## Requisitos {#upload-requirements}

Primero, necesitarás crear tu plantilla de correo electrónico HTML. Debe ser un archivo ZIP que contenga lo siguiente:

* Un único archivo HTML: el cuerpo de tu correo electrónico
* Una carpeta de imágenes referenciadas en el archivo HTML
* Menos de 50 archivos de imagen
* Un tamaño inferior a 5&nbsp;MB

## Cargar tu plantilla {#uploading-your-template}

### Paso 1: Ve al editor de plantillas de correo electrónico {#step-1-go-to-the-email-template-editor}

Ve a **Content** > **Email**. Selecciona **Create email template**.

### Paso 2: Agrega los detalles de la plantilla {#step-2-add-template-details}

Proporciona un nombre para la plantilla. Opcionalmente, agrega una descripción, equipos y etiquetas.

### Paso 3: Carga tu plantilla {#step-3-upload-your-template}

En la sección **Template content**, selecciona **Upload file** debajo del mosaico **HTML code editor**. Selecciona tu plantilla desde tu computadora. Consulta la sección [Requisitos](#upload-requirements) para asegurarte de que tu plantilla cumple con los requisitos de carga.

### Paso 4: Finaliza y guarda tu plantilla {#step-4-finish-and-save-your-template}

Asegúrate de guardar tu plantilla seleccionando **Save template**. ¡Ya puedes usar esta plantilla en cualquier campaña o Canvas que elijas!

{% alert note %}
Si realizas alguna edición en una plantilla existente, esos cambios no se reflejarán en las campañas que se crearon usando versiones anteriores de esa plantilla.
{% endalert %}

## Usar tus plantillas en campañas de API {#api_for_upload_email_templates}

Para usar tu correo electrónico en una campaña de API, necesitas el `email_template_id`, que se encuentra en la parte inferior de cualquier plantilla de correo electrónico creada en Braze.

![Sección del identificador de API de una plantilla de correo electrónico HTML.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## Administrar plantillas de correo electrónico {#managing-email-templates}

Puedes [duplicar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/) y [archivar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/) plantillas de correo electrónico. Obtén más información sobre cómo crear y administrar plantillas y contenido creativo en [Plantillas]({{site.baseurl}}/user_guide/messaging/templates/).

## Solución de problemas {#troubleshooting}

Hay varios mensajes de error de correo electrónico que puedes recibir al cargar un archivo de plantilla HTML. Si recibes un error, consulta la siguiente tabla para ver los problemas comunes y sus correcciones recomendadas:

| Error | Corrección |
|------|---|
| `.zip over 5&nbsp;MB` | Reduce el tamaño de tu archivo e intenta cargarlo de nuevo.|
| `.zip corrupt` | Inspecciona tu archivo e intenta cargarlo de nuevo. |
| `Missing HTML` | Agrega el archivo HTML a tu archivo ZIP e intenta cargarlo de nuevo.|
| `Multiple HTML` | Elimina uno de los archivos HTML e intenta cargarlo de nuevo.|
| `Images over 5&nbsp;MB` | Reduce el número de imágenes e intenta cargarlo de nuevo. |
| `Extra Images` | Puede haber imágenes adicionales en tu archivo que no están referenciadas en tu archivo HTML. Esto no causa un error de fallo, pero las imágenes adicionales se descartan. Si esas imágenes debían estar referenciadas en el archivo HTML, revisa el contenido, corrige cualquier error e intenta cargarlo de nuevo.|
| `Missing Images` | Si hay imágenes referenciadas en tu archivo HTML, pero esas imágenes no están incluidas en la carpeta de imágenes del archivo ZIP, recibirás un error de archivo. Inspecciona tu archivo y corrige cualquier error (como errores ortográficos), o agrega las imágenes faltantes a tu archivo ZIP e intenta cargarlo de nuevo.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas" }

Ten en cuenta que al descargar los archivos de campañas HTML, pasos en Canvas con mensajes de correo electrónico o plantillas en una máquina Windows, el carácter `|` (barra vertical) no es compatible, por lo que es posible que necesites usar una aplicación diferente para extraer el contenido descargado del archivo ZIP.

## Preguntas frecuentes {#frequently-asked-questions}

Para obtener respuestas a preguntas frecuentes sobre plantillas de correo electrónico, consulta nuestra página de [preguntas frecuentes sobre plantillas de correo electrónico y enlaces]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq/).