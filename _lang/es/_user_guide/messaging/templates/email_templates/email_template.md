---
nav_title: Crear una plantilla de correo electrónico
article_title: Crear una plantilla de correo electrónico
page_order: 0
description: "Este artículo de referencia explica cómo crear, personalizar y administrar plantillas de correo electrónico."
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"
search_rank: 1
---

# Crear una plantilla de correo electrónico {#create-an-email-template}

> El dashboard de Braze tiene un editor de plantillas de correo electrónico que te permite crear correos electrónicos personalizados y llamativos, y guardarlos para usarlos más tarde en Campaigns. También puedes cargar tu propia [plantilla de correo electrónico HTML]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template).

## Paso 1: Navega al editor de plantillas de correo electrónico {#step-1-navigate-to-the-email-template-editor}

En el dashboard de Braze, ve a **Contenido** > **Correo electrónico**.

## Paso 2: Selecciona tu experiencia de edición {#step-2-select-your-editing-experience}

Selecciona entre el **editor de arrastrar y soltar** o el **editor de código HTML** para tu experiencia de edición.

También puedes elegir entre plantillas prediseñadas de Braze, crear una nueva plantilla o editar una plantilla existente (simple o [adaptable a dispositivos móviles]({{site.baseurl}}/help/release_notes/2018/may#mobile-responsive-email-templates)).

![Una plantilla de correo electrónico para la venta de primavera de una empresa con opciones para seleccionar el editor de arrastrar y soltar o el editor HTML, o para seleccionar entre plantillas de Braze.]({% image_buster /assets/img/email_templates/template2.png %})

{% alert note %}
Cualquier plantilla HTML personalizada existente debe recrearse usando el editor de arrastrar y soltar.
{% endalert %}

## Paso 3: Personaliza tu plantilla {#step-3-customize-your-template}

Después de seleccionar tu experiencia de edición, esta es tu oportunidad de ser creativo personalizando tu plantilla de correo electrónico. Puedes usar HTML para crear y emular tu marca en el editor HTML, o incluir una variedad de [detalles creativos]({{site.baseurl}}/user_guide/channels/email/drag_and_drop#creative-details) en el editor de arrastrar y soltar.

### Incluir un enlace para cancelar suscripción {#include-an-unsubscribe-link}

Al diseñar tu plantilla de correo electrónico, si no incluyes un enlace para cancelar suscripción, Braze te pedirá que lo agregues en tu correo electrónico, ya que es obligatorio por ley en todos los correos electrónicos de marketing. Puedes agregar este enlace para cancelar suscripción como pie de página en la parte inferior de tus correos electrónicos usando la etiqueta de Liquid {% raw %}``${email_footer}``{% endraw %}, o [personalizando el pie de página]({{site.baseurl}}/user_guide/channels/email/subscriptions#custom-footer) en tu plantilla.

## Paso 4: Verifica errores en el correo electrónico {#step-4-check-for-email-errors}

Los errores de correo electrónico se presentan en la pestaña **Redactar** del flujo de trabajo del mensaje. Los errores te impiden avanzar. Las "advertencias" indican recordatorios para ayudarte a seguir las mejores prácticas. Dependiendo de tu negocio, podrías optar por ignorarlas.

![Lista de errores y advertencias de un correo electrónico de ejemplo.]({% image_buster /assets/img/dnd_compose_error.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Aquí tienes una lista de errores que se contemplan en nuestro editor:

- Sintaxis de Liquid incorrecta
- [Cuerpos de correo electrónico mayores a 400 kb; se recomienda encarecidamente que los cuerpos sean menores a 102 kb]({{site.baseurl}}/user_guide/channels/email/best_practices)
- Plantillas sin un enlace para cancelar suscripción
- Correos electrónicos con un **Cuerpo** o **Asunto** en blanco
- Correos electrónicos sin enlace para cancelar suscripción

## Paso 5: Previsualiza y prueba tu mensaje {#step-5-preview-and-test-your-message}

Después de terminar de redactar tu plantilla, puedes probarla antes de enviarla.

Desde la parte inferior de la pantalla de resumen, selecciona **Preview and Test**. Aquí puedes previsualizar cómo aparecerá tu correo electrónico en la bandeja de entrada de un cliente. Con **Preview as User** seleccionado, puedes previsualizar tu correo electrónico como un usuario aleatorio, seleccionar un usuario específico o crear un usuario personalizado. Esto te permite probar que tu contenido conectado y las llamadas de personalización funcionan como deberían.

Luego, puedes seleccionar **Copy preview link** para generar y copiar un enlace de vista previa compartible que muestra cómo se ve el correo electrónico para un usuario aleatorio. El enlace dura siete días antes de que necesite ser regenerado.

También puedes alternar entre las vistas de escritorio, móvil y texto plano para tener una idea de cómo aparece tu mensaje en diferentes contextos.

{% alert tip %}
¿Tienes curiosidad por saber cómo se ve tu correo electrónico para los usuarios en modo oscuro? Selecciona el interruptor **Dark Mode Preview** ubicado en la sección **Preview and Test** (solo en el editor de arrastrar y soltar).
{% endalert %}

Cuando estés listo para una verificación final, selecciona **Test Send** y envía un mensaje de prueba a ti mismo o a un grupo de evaluadores de contenido para asegurarte de que tu correo electrónico se muestra correctamente en una variedad de dispositivos y clientes de correo electrónico.

![Ejemplo de vista previa de correo electrónico para enviar como prueba.]({% image_buster /assets/img_archive/newEmailTest.png %})

Si ves algún problema con tu plantilla o quieres hacer algún cambio, selecciona **Edit Email** para volver al editor. Ten en cuenta que las ediciones realizadas en el editor **Classic** pueden no reflejarse en el editor HTML o en la vista previa del correo electrónico.

## Paso 6: Guarda tu plantilla {#step-6-save-your-template}

Asegúrate de guardar tu plantilla seleccionando **Save Template**. Ahora estás listo para usar esta plantilla en cualquier campaña o componente de Canvas que elijas. Para acceder a tu plantilla, selecciona la experiencia de edición con la que la creaste y luego selecciónala de la lista de plantillas disponibles.

{% alert note %}
Si realizas ediciones en una plantilla existente, esos cambios no se reflejarán en las campañas creadas con versiones anteriores de esa plantilla.
{% endalert %}

### Administrar tus plantillas {#manage-your-templates}

Puedes ver las plantillas de correo electrónico en **Plantillas** > **Plantillas de correo electrónico**, filtrando por estado, tipo, etiquetas, el usuario que la creó, o buscando por nombre de plantilla. Necesitas los permisos de usuario correspondientes, como **View Email Templates**, para ver estas plantillas. Para más detalles, consulta [Permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

A medida que crees más plantillas de correo electrónico, puedes [duplicar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#duplicate-templates) y [archivar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#archive-templates) plantillas de correo electrónico. Obtén más información sobre cómo crear y administrar tu biblioteca de plantillas y contenido creativo en [Plantillas y medios]({{site.baseurl}}/user_guide/messaging/templates).

### Usar tus plantillas en campañas de API {#use-your-templates-in-api-campaigns}

Para usar tu correo electrónico en una campaña de API, necesitas un `email_template_id`, que se puede encontrar en la parte inferior de cualquier plantilla de correo electrónico creada en Braze.

![Identificador de API ubicado en la parte inferior de una plantilla de correo electrónico.]({% image_buster /assets/img/email_templates/template5.png %})

### Comentar en plantillas de correo electrónico {#comment-on-email-templates}

Puedes colaborar y comentar en plantillas de correo electrónico en el editor de arrastrar y soltar.

1. Selecciona el bloque de contenido o la fila en el cuerpo del correo electrónico en la que deseas comentar.
2. Selecciona el icono de comentario <i class="fas fa-comment"></i>.
3. Ingresa tu comentario en la barra lateral y luego selecciona **Submit**.
4. Después de ingresar tus comentarios, selecciona **Done**.
5. Selecciona **Save Template** para guardar tus comentarios.

Después de guardar tu plantilla, los usuarios pueden ver iconos sobre los comentarios sin resolver. Selecciona **Resolve** para resolver estos comentarios.

![Un comentario en una plantilla de correo electrónico que dice "Looks good to me".]({% image_buster /assets/img/email_templates/template_comment.png %})

Para respuestas a preguntas frecuentes sobre plantillas de correo electrónico, consulta nuestras [Preguntas frecuentes sobre plantillas]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq).