---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre plantillas de correo electrónico y de enlaces
page_order: 10

page_type: FAQ
description: "Esta página cubre las preguntas frecuentes sobre las plantillas de correo electrónico y las plantillas de enlaces."
tool:
  - Templates
channel: email

---

# Preguntas frecuentes {#frequently-asked-questions}

> Esta página ofrece respuestas a algunas preguntas frecuentes sobre las plantillas de correo electrónico y las plantillas de enlaces.

## Plantillas de correo electrónico {#email-templates}

### ¿Puedo añadir un enlace de "ver este correo electrónico en un navegador" a mis correos electrónicos? {#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails}

No, Braze no ofrece esta funcionalidad. Esto se debe a que una mayoría creciente de correos electrónicos se abren en dispositivos móviles y clientes de correo electrónico modernos, que renderizan imágenes y contenido sin ningún problema.

**Solución alternativa:** Para lograr este mismo resultado, puedes alojar el contenido de tu correo electrónico en una página de destino externa (como tu sitio web), a la que luego puedes enlazar desde la Campaign de correo electrónico que estás creando utilizando la herramienta **Link** al editar el cuerpo del correo electrónico.

### ¿Cómo creo un enlace de cancelación de suscripción personalizado para mis plantillas de correo electrónico? {#how-do-i-create-a-custom-unsubscribe-link-for-my-email-templates}

Existe una opción de redirección para la página de cancelación de suscripción.

Podrías cambiar el enlace de cancelación de suscripción en el pie de página personalizado de {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} a un enlace a tu propio sitio web con un parámetro de consulta que incluya el ID de usuario. Un ejemplo es:
{% raw %}
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

A continuación, podrías llamar al [punto de conexión `/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status) para actualizar el estado de suscripción del usuario. Para más detalles, consulta nuestra documentación sobre [cambiar el estado de suscripción de correo electrónico]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions).

Para guardar este nuevo enlace, la etiqueta predeterminada de cancelación de suscripción de Braze {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} debe estar en el pie de página. Esto significa que tendrás que incluir el enlace predeterminado "ocultándolo", ya sea colocando la etiqueta en un comentario o en una etiqueta `<div>` oculta.

- **Ejemplo de etiqueta en comentario:** ejemplo de colocar la etiqueta en un comentario: `<!-- ${set_user_to_unsubscribed_url} -->`
- **Ejemplo de comentario en etiqueta `<div>` oculta:** {%raw%}`<div style="display:none;max-height:0px;overflow:hidden;">${set_user_to_unsubscribed_url}</div>`{%endraw%}

### ¿Qué sucede si edito una plantilla de correo electrónico que se está utilizando actualmente en una Campaign? {#what-happens-if-i-edit-an-email-template-that-is-currently-being-used-in-a-campaign}

Las ediciones realizadas en una plantilla existente no se reflejarán en las Campaigns que se crearon utilizando versiones anteriores de esa plantilla. Para las Campaigns de API que utilizan una plantilla en el cuerpo de la REST API, Braze utilizará la última versión de la plantilla en el momento del envío.

## Plantillas de enlaces {#link-templates}

### ¿Puedo cargar varias plantillas de enlaces en mi correo electrónico? {#can-i-upload-multiple-link-templates-to-my-email}

Sí, puedes insertar tantas plantillas como desees en tus mensajes de correo electrónico. Como práctica recomendada, deberías probar tus correos electrónicos para asegurarte de que los enlaces no superen los 2000 caracteres, ya que la mayoría de los navegadores acortarán o cortarán los enlaces.

### ¿Cómo previsualizo mis enlaces con todas las etiquetas aplicadas? {#how-do-i-preview-my-links-with-all-of-the-tags-applied}

Hay varias formas de previsualizar tus enlaces. Después de haber aplicado la [plantilla de enlaces]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template), puedes enviarte un [correo electrónico de prueba]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages) para ver todos los enlaces.

Desde el panel de vista previa en una nueva pestaña, también puedes abrir los enlaces para verlos. También puedes pasar el cursor sobre los enlaces en el panel de vista previa y verlos en la parte inferior de tu navegador.

### ¿Cómo funciona la creación de plantillas de enlaces con Liquid? {#how-does-link-templating-work-with-liquid}

Las plantillas de enlaces se expanden y se añaden a cada URL antes de que ocurra cualquier expansión de Liquid. Si parte de tu URL se genera utilizando un fragmento de código Liquid, recomendamos que la URL base y el signo de interrogación (?) estén codificados de forma fija para que las plantillas de enlaces se expandan correctamente.

Evita añadir el signo de interrogación (?) a tu Liquid, ya que esto hará que las plantillas de enlaces primero añadan un signo de interrogación (?) y luego el proceso de expansión de Liquid añada un segundo signo de interrogación (?).

## Aliasing de enlaces {#link-aliasing}

### ¿Cómo afectará la habilitación del aliasing de enlaces a mis Content Blocks y plantillas de enlaces? {#how-will-enabling-link-aliasing-impact-my-content-blocks-and-link-templates}

Para todos los nuevos Content Blocks que se creen, el aliasing de enlaces se aplica en todos los espacios de trabajo, ya que es una característica a nivel de empresa.

Los Content Blocks existentes no se modificarán cuando se habilite el aliasing de enlaces. Aunque las plantillas de enlaces existentes no se modificarán, la sección de plantilla de enlaces existente en un mensaje se eliminará. Consulta [Aliasing de enlaces en Content Blocks]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing#link-aliasing-in-content-blocks) para más información.

### ¿Puedo usar lógica condicional de Liquid completamente dentro de una etiqueta de anclaje HTML? {#can-i-use-liquid-conditional-logic-entirely-within-an-html-anchor-tag}

No, el aliasing de enlaces de Braze no reconocerá el HTML correctamente.

Cuando se usa una lógica como esta junto con características que necesitan analizar el HTML (como un preencabezado o la creación de plantillas de enlaces), la biblioteca utilizada para escanear el HTML puede modificar la etiqueta de anclaje de una manera que impedirá que el `href` adecuado se aplique como plantilla. La biblioteca entonces determinará que el HTML no es válido porque es agnóstica al código Liquid.

En su lugar, usa lógica Liquid que contenga una etiqueta de anclaje completa en cada etapa. Esto no interferirá con el análisis del HTML porque la lógica incluye múltiples instancias de HTML válido. También puedes simplificar tu lógica asignando y luego aplicando como plantilla una variable en la etiqueta de anclaje apropiada.