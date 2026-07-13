---
nav_title: Plantillas de enlaces
article_title: Plantillas de enlaces
page_order: 4
description: "Este artículo explica cómo crear diferentes tipos de plantillas de enlaces en tus correos electrónicos."
tool:
  - Templates
channel:
  - email

---

# Plantillas de enlaces {#link-templates}

> Con las plantillas de enlaces, puedes crear enlaces dinámicos y reutilizables para tus campañas de correo electrónico añadiendo parámetros o anteponiendo URL. Esto puede crear consistencia en las URL de tus campañas y mensajes.

{% alert note %}
Las plantillas de enlaces son una característica opcional. Si **Plantillas de enlaces de correo electrónico** no aparece en la sección **Plantillas**, ponte en contacto con tu director de cuentas para activar la característica.
{% endalert %}

## Cómo funciona {#how-it-works}

Las plantillas de enlaces se utilizan con mayor frecuencia en los siguientes casos de uso:

- Añadir parámetros de consulta de Google Analytics a todos los enlaces de un mensaje de correo electrónico determinado
- Anteponer una URL a todos los enlaces de un mensaje de correo electrónico determinado

Supongamos que estás ejecutando una campaña promocional de correo electrónico para el lanzamiento de un nuevo producto. Puedes usar una plantilla de enlaces que dirija a los usuarios a la página del producto y personalizar el enlace para incluir el nombre de tu usuario o un código promocional específico. Esto te permite rastrear cuántos usuarios han hecho clic en el enlace y han realizado una compra. De esta forma, puedes crear consistencia en tus enlaces y hacer un mejor seguimiento de tus análisis.

## Crear una plantilla de enlaces {#creating-a-link-template}

Puedes crear un número ilimitado de plantillas de enlaces para cubrir tus diversas necesidades. Para crear una plantilla de enlaces, haz lo siguiente:

1. Ve a **Contenido** > **Enlace de correo electrónico**.
2. Selecciona **Crear plantilla de enlace de correo electrónico**.
3. Dale un nombre a tu plantilla de enlaces.
4. (Opcional) Añade una descripción, equipo o etiqueta para agregar detalles sobre la plantilla de enlaces.
5. (Opcional) Selecciona el conmutador para añadir automáticamente la plantilla de enlaces a los enlaces en campañas de correo electrónico y Canvas. Esto se aplica al añadir un nuevo enlace a cualquier correo electrónico nuevo o existente.

Hay dos tipos de plantillas de enlaces que puedes crear:

- [Plantilla de enlaces que se inserta antes de una URL](#prepend-link-template)
- [Plantilla de enlaces que se inserta después de una URL](#append-link-template)

Al usar plantillas de enlaces y [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), Liquid solo debe añadirse dentro de la etiqueta body para garantizar una representación consistente.

### Anteponer: crear una plantilla de enlaces que se inserta antes de una URL {#prepend-link-template}

Para añadir una cadena o URL antes de los enlaces en tu mensaje de correo electrónico, haz lo siguiente:

1. Crea una nueva plantilla de enlaces.
2. Establece la **Posición de la plantilla** en **Antes de URL**.
3. Introduce una cadena que siempre se antepondrá a tu URL.

La **Vista previa de la plantilla** te ofrece un ejemplo de cómo se insertará la plantilla de enlaces antes de una URL.

![Campos de posición de la plantilla, URL antepuesta y vista previa de la plantilla para el proceso de inserción de la plantilla de enlaces antes de una URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### Añadir: crear una plantilla de enlaces que se inserta después de una URL {#append-link-template}

Si quieres añadir parámetros de consulta después de una URL en tu mensaje de correo electrónico:

1. Crea una nueva plantilla de enlaces.
2. Establece la **Posición de la plantilla** en **Después de URL**.
3. Introduce los parámetros de consulta (`value=example`) al final de cada URL. Puedes tener múltiples parámetros añadidos al final de una URL.

![Campos de posición de la plantilla, parámetros de consulta y vista previa de la plantilla para el proceso de inserción de la plantilla de enlaces después de una URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## Usar plantillas de enlaces en campañas de correo electrónico {#using-link-templates-in-email-campaigns}

Después de configurar tus plantillas de enlaces, puedes aplicarlas en tu correo electrónico.

Para aplicar una plantilla de enlaces en el editor HTML o en el editor de arrastrar y soltar, sigue estos pasos:

{% alert important %}
Para acceder a la pestaña **Gestión de enlaces** en el editor HTML actualizado o en el editor de arrastrar y soltar, debes tener activado el aliasing de enlaces. Para activar el aliasing de enlaces, ponte en contacto con tu director de cuentas. Para más información, consulta [Aliasing de enlaces]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing).
{% endalert %}

- **Editor HTML actualizado:** En la pestaña **Contenido**, selecciona **Gestión de enlaces**, selecciona **Añadir una plantilla de enlaces**, elige tu plantilla de enlaces y luego selecciona **Añadir**.
- **Editor de arrastrar y soltar:** En la pestaña **Contenido**, selecciona **Gestión de enlaces**, selecciona **Añadir una plantilla de enlaces**, elige tu plantilla de enlaces y luego selecciona **Añadir**.

![Pestaña Gestión de enlaces en el editor de arrastrar y soltar con una lista de ejemplo de plantillas de enlaces.]({% image_buster /assets/img_archive/link_template_messagecomposer2.png %})

{% alert note %}
Las plantillas de enlaces no se aplican al texto sin formato. Esto significa que Currents puede mostrar clics que no incluyen los parámetros de las plantillas de enlaces, ya que esos clics pueden provenir de la versión de texto sin formato del correo electrónico.
{% endalert %}

A medida que añades plantillas de enlaces en la pestaña **Gestión de enlaces**, desplázate hacia la derecha para ver las plantillas que has añadido. Si los enlaces existentes dentro de un correo electrónico ya tienen una plantilla de enlaces añadida, los enlaces recién añadidos también tendrán la plantilla de enlaces añadida de forma predeterminada.

## Administrar plantillas de enlaces {#managing-link-templates}

También puedes [duplicar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates) plantillas de enlaces. Obtén más información sobre cómo crear y administrar plantillas y contenido creativo en [Plantillas y medios]({{site.baseurl}}/user_guide/messaging/templates).

{% alert important %}
Archivar plantillas no está disponible actualmente para las plantillas de enlaces.
{% endalert %}

## Preguntas frecuentes {#frequently-asked-questions}

Para obtener respuestas a las preguntas frecuentes sobre plantillas de enlaces, consulta nuestra página de [Preguntas frecuentes sobre plantillas]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq).