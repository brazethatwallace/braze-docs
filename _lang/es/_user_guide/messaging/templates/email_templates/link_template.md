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

Las plantillas de enlaces se usan con mayor frecuencia en los siguientes casos:

- Añadir parámetros de consulta de Google Analytics a todos los enlaces en un mensaje de correo electrónico determinado
- Anteponer una URL a todos los enlaces en un mensaje de correo electrónico determinado

Supongamos que estás ejecutando una Campaign de correo electrónico promocional para el lanzamiento de un nuevo producto. Puedes usar una plantilla de enlaces que dirija a los usuarios a la página del producto y personalizar el enlace para incluir el nombre de tu usuario o un código promocional específico. Esto te permite rastrear cuántos usuarios han hecho clic en el enlace y han realizado una compra. De esta manera, puedes crear consistencia en tus enlaces y hacer un mejor seguimiento de tus análisis.

## Crear una plantilla de enlace {#creating-a-link-template}

Puedes crear un número ilimitado de plantillas de enlace para satisfacer tus diversas necesidades. Para crear una plantilla de enlace, haz lo siguiente:

1. Ve a **Contenido** > **Enlace de correo electrónico**.
2. Selecciona **Crear plantilla de enlace de correo electrónico**.
3. Dale un nombre a tu plantilla de enlace.
4. (Opcional) Agrega una descripción, equipo o etiqueta para añadir detalles sobre la plantilla de enlace.
5. (Opcional) Selecciona el alternar para agregar automáticamente la plantilla de enlace a los enlaces en Campaigns de correo electrónico y Canvas. Esto se aplica al agregar un nuevo enlace a cualquier correo electrónico nuevo o existente.

Hay dos tipos de plantillas de enlace que puedes crear:

- [Plantilla de enlace que se inserta antes de una URL](#prepend-link-template)
- [Plantilla de enlace que se inserta después de una URL](#append-link-template)

Al usar plantillas de enlace y [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), Liquid solo debe añadirse dentro de la etiqueta body para garantizar una representación consistente.

### Anteponer: Crear una plantilla de enlace que se inserta antes de una URL {#prepend-link-template}

Para agregar una cadena o URL antes de los enlaces en tu mensaje de correo electrónico, haz lo siguiente:

1. Crea una nueva plantilla de enlace.
2. Establece la **Template Position** en **Before URL**.
3. Introduce una cadena que siempre se antepondrá a tu URL.

La **vista previa de la plantilla** se proporciona para darte un ejemplo de cómo se insertará la plantilla de enlace antes de una URL.

![Campos de posición de la plantilla, URL antepuesta y vista previa de la plantilla para el proceso de inserción de plantilla de enlace antes de una URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### Adjuntar: Crear una plantilla de enlace que se inserta después de una URL {#append-link-template}

Si deseas agregar parámetros de consulta después de una URL en tu mensaje de correo electrónico:

1. Crea una nueva plantilla de enlace.
2. Establece la **Template Position** en **After URL**.
3. Introduce los parámetros de consulta (`value=example`) al final de cada URL. Puedes tener múltiples parámetros adjuntados al final de una URL.

![Campos de posición de la plantilla, parámetros de consulta y vista previa de la plantilla para el proceso de inserción de plantilla de enlace después de una URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

#### Etiquetas de Liquid para `utm_campaign` {#liquid-tags-for-utm_campaign}

Las etiquetas de Liquid para `utm_campaign` difieren entre Campaigns y Canvas.

En Campaigns, usa:

{% raw %}
- `{{campaign.${name}}}` para obtener el nombre de la Campaign
- `{{campaign.${message_name}}}` para obtener el nombre de la variante del mensaje
{% endraw %}

En Canvas, usa:

{% raw %}
- `{{canvas.${name}}}` para obtener el nombre del Canvas
- `{{campaign.${name}}}` para obtener el nombre del paso en Canvas (solo pasos de mensaje)
{% endraw %}

Para una comparación completa de estos atributos en Liquid, la REST or transferencia de estado representacional API y Currents, consulta [Atributos de Campaign y Canvas en distintas fuentes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/campaign_and_canvas_attributes_across_sources). Para orientación sobre la codificación de URL, consulta [Nombres de Campaign en URL]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#campaign-names-in-urls).

## Usar plantillas de enlaces en Campaigns de correo electrónico {#using-link-templates-in-email-campaigns}

Después de configurar tus plantillas de enlaces, puedes aplicarlas en tu correo electrónico.

Para aplicar una plantilla de enlaces en el editor HTML o en el editor de arrastrar y soltar, sigue estos pasos:

{% alert note %}
Si las plantillas de enlaces de correo electrónico o el [aliasing de enlaces]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing) están habilitados para tu espacio de trabajo, puedes acceder a la pestaña **Link Management** en el editor HTML actualizado y en el editor de arrastrar y soltar.
{% endalert %}

- **Editor HTML actualizado:** En la pestaña **Content**, selecciona **Link Management**, selecciona **Add a Link Template**, elige tu plantilla de enlaces y luego selecciona **Add**.
- **Editor de arrastrar y soltar:** En la pestaña **Content**, selecciona **Link Management**, selecciona **Add a Link Template**, elige tu plantilla de enlaces y luego selecciona **Add**.

![Pestaña Link Management en el editor de arrastrar y soltar con una lista de ejemplo de plantillas de enlaces.]({% image_buster /assets/img_archive/link_template_messagecomposer2.png %})

{% alert note %}
Las plantillas de enlaces no se aplican al texto sin formato. Esto significa que Currents puede mostrar clics que no incluyen los parámetros de las plantillas de enlaces, ya que esos clics pueden provenir de la versión de texto sin formato del correo electrónico.
{% endalert %}

A medida que añades plantillas de enlaces en la pestaña **Link Management**, cada plantilla aparece como una columna adicional en la tabla. Si los enlaces existentes dentro de un correo electrónico ya tienen una plantilla de enlaces añadida, los enlaces nuevos que se añadan también tendrán la plantilla de enlaces añadida de forma predeterminada.

{% alert tip %}
Cuando incluyas enlaces en tu mensaje, asegúrate de que las URL comiencen con `http://` o `https://`.
{% endalert %}

## Gestión de plantillas de enlaces {#managing-link-templates}

También puedes [duplicar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates) plantillas de enlaces. Obtén más información sobre cómo crear y gestionar plantillas y contenido creativo en [Plantillas y medios]({{site.baseurl}}/user_guide/messaging/templates).

{% alert important %}
Archivar plantillas no está disponible actualmente para las plantillas de enlaces.
{% endalert %}

## Solución de problemas {#troubleshooting}

### Faltan parámetros UTM {#missing-utm-parameters}

Las plantillas de enlaces no se aplican a los enlaces en comentarios HTML estándar (`<!-- ... -->`). Para los comentarios condicionales de Outlook (por ejemplo, `<!--[if mso]>`), las plantillas de enlaces se aplican cuando el aliasing de enlaces está habilitado para tu espacio de trabajo. Los espacios de trabajo sin aliasing de enlaces habilitado siguen omitiendo los comentarios condicionales.

### Los parámetros UTM aparecen en el navegador pero faltan en los enlaces {#utm-parameters-present-in-browser-but-missing-from-links}

Esto puede ocurrir cuando la ruta de la URL en tu correo electrónico no coincide con la ruta completa que pretendes utilizar (por ejemplo, una ruta acortada o diferente a la URL completa del sitio web).

- **Qué verificar:** El `href` en el correo electrónico incluye la ruta completa a la página (no solo una ruta parcial que depende de redirecciones).
- **Qué esperar:** Si la ruta en el correo electrónico está incompleta o es diferente, es posible que los parámetros UTM de tu plantilla de enlaces no se apliquen a ese enlace cuando se hace clic en él, aunque el sitio web pueda redirigir al visitante a la página correcta.

Por ejemplo, si el enlace completo es `https://www.somewebsite.com/women/designer/johnjane` pero el correo electrónico usa `https://www.somewebsite.com/designer/johnjane`, es de esperar que los parámetros UTM no se añadan al enlace del correo electrónico.

### Faltan parámetros UTM en enlaces generados con Liquid {#utm-parameters-missing-from-liquid-rendered-links}

Al aplicar plantillas de enlaces, Braze analiza cada URL para determinar dónde añadir los parámetros. Si una etiqueta de Liquid genera una URL que no se puede analizar como una URI válida, la plantilla de enlaces se omite silenciosamente. Comprueba que tu salida de Liquid produce una URL bien formada. Verifica previsualizando el mensaje para un usuario específico y confirmando que la URL generada es válida. Si la URL incluye variables de Liquid en la ruta o la cadena de consulta, confirma que la salida no contiene caracteres no válidos o una codificación incorrecta.

### Faltan valores UTM en los envíos de prueba {#utm-values-missing-in-test-sends}

Al enviar de prueba plantillas de enlaces, {% raw %}`{{${user_id}}}`{% endraw %} no se genera. En su lugar, duplica la Campaign y configúrala para dirigirla al correo electrónico o `external_id` de tus usuarios internos y lanza la Campaign para verificar que todos los parámetros UTM de la plantilla de enlaces se hayan completado.

## Preguntas frecuentes {#frequently-asked-questions}

Para obtener respuestas a las preguntas frecuentes sobre plantillas de enlaces, consulta nuestra página de [preguntas frecuentes sobre plantillas]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq).