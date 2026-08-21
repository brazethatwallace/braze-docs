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

- Añadir parámetros de consulta de Google Analytics a todos los enlaces en un mensaje de correo electrónico determinado
- Anteponer una URL a todos los enlaces en un mensaje de correo electrónico determinado

Supongamos que estás ejecutando una Campaign de correo electrónico promocional para el lanzamiento de un nuevo producto. Puedes usar una plantilla de enlace que dirija a los usuarios a la página del producto y personalizar el enlace para incluir el nombre de tu usuario o un código promocional específico. Esto te permite rastrear cuántos usuarios han hecho clic en el enlace y han realizado una compra. De esta manera, puedes crear consistencia en tus enlaces y hacer un mejor seguimiento de tus análisis.

## Crear una plantilla de enlace {#creating-a-link-template}

Puedes crear un número ilimitado de plantillas de enlace para cubrir tus diversas necesidades. Para crear una plantilla de enlace, haz lo siguiente:

1. Ve a **Contenido** > **Enlace de correo electrónico**.
2. Selecciona **Crear plantilla de enlace de correo electrónico**.
3. Dale un nombre a tu plantilla de enlace.
4. (Opcional) Añade una descripción, equipo o etiqueta para agregar detalles sobre la plantilla de enlace.
5. (Opcional) Selecciona el conmutador para añadir automáticamente la plantilla de enlace a los enlaces en Campaigns de correo electrónico y Canvas. Esto se aplica al añadir un nuevo enlace a cualquier correo electrónico nuevo o existente.

Hay dos tipos de plantillas de enlace que puedes crear:

- [Plantilla de enlace que se inserta antes de una URL](#prepend-link-template)
- [Plantilla de enlace que se inserta después de una URL](#append-link-template)

Al usar plantillas de enlace y [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), Liquid solo debe añadirse dentro de la etiqueta body para garantizar una representación consistente.

### Anteponer: crear una plantilla de enlace que se inserta antes de una URL {#prepend-link-template}

Para añadir una cadena o URL antes de los enlaces en tu mensaje de correo electrónico, haz lo siguiente:

1. Crea una nueva plantilla de enlace.
2. Establece la **Posición de la plantilla** en **Antes de la URL**.
3. Introduce una cadena que siempre se antepondrá a tu URL.

La **Vista previa de la plantilla** te ofrece un ejemplo de cómo se insertará la plantilla de enlace antes de una URL.

![Campos de posición de la plantilla, URL antepuesta y vista previa de la plantilla para el proceso de inserción de la plantilla de enlace antes de una URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### Añadir: crear una plantilla de enlace que se inserta después de una URL {#append-link-template}

Si deseas añadir parámetros de consulta después de una URL en tu mensaje de correo electrónico:

1. Crea una nueva plantilla de enlace.
2. Establece la **Posición de la plantilla** en **Después de la URL**.
3. Introduce los parámetros de consulta (`value=example`) al final de cada URL. Puedes tener múltiples parámetros añadidos al final de una URL.

![Campos de posición de la plantilla, parámetros de consulta y vista previa de la plantilla para el proceso de inserción de la plantilla de enlace después de una URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## Uso de plantillas de enlaces en campañas de correo electrónico {#using-link-templates-in-email-campaigns}

Después de configurar tus plantillas de enlaces, puedes aplicarlas en tu correo electrónico.

Para aplicar una plantilla de enlace en el editor HTML o en el editor de arrastrar y soltar, sigue estos pasos:

{% alert note %}
Si las plantillas de enlaces de correo electrónico o el [aliasing de enlaces]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing) están habilitados para tu espacio de trabajo, puedes acceder a la pestaña **Link Management** en el editor HTML actualizado y en el editor de arrastrar y soltar.
{% endalert %}

- **Editor HTML actualizado:** En la pestaña **Content**, selecciona **Link Management**, selecciona **Add a Link Template**, elige tu plantilla de enlace y luego selecciona **Add**.
- **Editor de arrastrar y soltar:** En la pestaña **Content**, selecciona **Link Management**, selecciona **Add a Link Template**, elige tu plantilla de enlace y luego selecciona **Add**.

![Pestaña Link Management en el editor de arrastrar y soltar con una lista de ejemplo de plantillas de enlaces.]({% image_buster /assets/img_archive/link_template_messagecomposer2.png %})

{% alert note %}
Las plantillas de enlaces no se aplican al texto sin formato. Esto significa que Currents puede mostrar clics que no incluyen los parámetros de las plantillas de enlaces, ya que esos clics pueden provenir de la versión de texto sin formato del correo electrónico.
{% endalert %}

A medida que agregas plantillas de enlaces en la pestaña **Link Management**, cada plantilla aparece como una columna adicional en la tabla. Si los enlaces existentes dentro de un correo electrónico ya tienen una plantilla de enlace agregada, los enlaces recién agregados también tendrán la plantilla de enlace agregada de forma predeterminada.

{% alert tip %}
Al incluir enlaces en tu mensaje, asegúrate de que las URL comiencen con `http://` o `https://`.
{% endalert %}

## Gestión de plantillas de enlaces {#managing-link-templates}

También puedes [duplicar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates) plantillas de enlaces. Obtén más información sobre cómo crear y gestionar plantillas y contenido creativo en [Plantillas y medios]({{site.baseurl}}/user_guide/messaging/templates).

{% alert important %}
Archivar plantillas no está disponible actualmente para las plantillas de enlaces.
{% endalert %}

## Solución de problemas {#troubleshooting}

### Parámetros UTM faltantes {#missing-utm-parameters}

Las plantillas de enlaces no se aplican a los enlaces en comentarios HTML estándar (`<!-- ... -->`). Para los comentarios condicionales de Outlook (por ejemplo, `<!--[if mso]>`), las plantillas de enlaces se aplican cuando el aliasing de enlaces está habilitado para tu espacio de trabajo. Los espacios de trabajo sin aliasing de enlaces habilitado siguen omitiendo los comentarios condicionales.

### Parámetros UTM presentes en el navegador pero ausentes en los enlaces {#utm-parameters-present-in-browser-but-missing-from-links}

Esto puede ocurrir cuando la ruta de la URL en tu correo electrónico no coincide con la ruta completa que pretendes (por ejemplo, una ruta acortada o diferente a la URL completa del sitio web).

- **Qué verificar:** El `href` en el correo electrónico incluye la ruta completa a la página (no solo una ruta parcial que depende de redirecciones).
- **Qué esperar:** Si la ruta en el correo electrónico está incompleta o es diferente, es posible que los parámetros UTM de tu plantilla de enlaces no se apliquen a ese enlace cuando se haga clic, aunque el sitio web pueda redirigir al visitante a la página correcta.

Por ejemplo, si el enlace completo es `https://www.somewebsite.com/women/designer/johnjane` pero el correo electrónico usa `https://www.somewebsite.com/designer/johnjane`, es esperable que los parámetros UTM no se añadan al enlace del correo electrónico.

### Parámetros UTM faltantes en enlaces renderizados con Liquid {#utm-parameters-missing-from-liquid-rendered-links}

Al aplicar plantillas de enlaces, Braze analiza cada URL para determinar dónde añadir los parámetros. Si una etiqueta de Liquid renderiza una URL que no puede analizarse como un URI válido, la plantilla de enlaces se omite silenciosamente. Verifica que tu salida de Liquid produzca una URL bien formada. Prueba previsualizando el mensaje para un usuario específico y verificando que la URL renderizada sea válida. Si la URL incluye variables de Liquid en la ruta o la cadena de consulta, confirma que la salida no contenga caracteres no válidos o codificación incorrecta.

### Valores UTM faltantes en envíos de prueba {#utm-values-missing-in-test-sends}

Al enviar plantillas de enlaces de prueba, {% raw %}`{{${user_id}}}`{% endraw %} no se renderiza. En su lugar, duplica la Campaign y configúrala para dirigirte al correo electrónico o `external_id` de tus usuarios internos y lanza la Campaign para verificar que todos los parámetros UTM de la plantilla de enlaces estén completos.

## Preguntas frecuentes {#frequently-asked-questions}

Para obtener respuestas a las preguntas frecuentes sobre plantillas de enlaces, consulta nuestra página de [preguntas frecuentes sobre plantillas]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq).