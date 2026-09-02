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

> El panel de Braze tiene un editor de plantillas de correo electrónico que te permite crear correos electrónicos personalizados y llamativos, y guardarlos para usarlos más tarde en Campaigns. También puedes cargar tu propia [plantilla de correo electrónico HTML]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template).

## Paso 1: Navega al editor de plantillas de correo electrónico {#step-1-navigate-to-the-email-template-editor}

En el panel de Braze, ve a **Contenido** > **Correo electrónico**.

## Paso 2: Selecciona tu experiencia de edición {#step-2-select-your-editing-experience}

Selecciona entre el **editor de arrastrar y soltar** o el **editor de código HTML** para tu experiencia de edición.

También puedes elegir entre plantillas prediseñadas de Braze, crear una nueva plantilla o editar una plantilla existente (simple o [adaptable a dispositivos móviles]({{site.baseurl}}/releases/2018/may#mobile-responsive-email-templates)).

![Una plantilla de correo electrónico para la venta de primavera de una empresa con opciones para seleccionar el editor de arrastrar y soltar o el editor HTML, o para seleccionar entre las plantillas de Braze.]({% image_buster /assets/img/email_templates/template2.png %})

{% alert note %}
Cualquier plantilla HTML personalizada existente debe recrearse utilizando el editor de arrastrar y soltar.
{% endalert %}

## Paso 3: Personaliza tu plantilla {#step-3-customize-your-template}

Después de seleccionar tu experiencia de editor, esta es tu oportunidad de ser creativo al personalizar tu plantilla de correo electrónico. Puedes usar HTML para crear y emular tu imagen de marca en el editor HTML, o incluir una variedad de [detalles creativos]({{site.baseurl}}/user_guide/channels/email/drag_and_drop) en el editor de arrastrar y soltar.

### Incluir un enlace para cancelar suscripción {#include-an-unsubscribe-link}

Al diseñar tu plantilla de correo electrónico, si no incluyes un enlace para cancelar suscripción, Braze te pedirá que lo añadas a tu correo electrónico, ya que es obligatorio por ley en todos los correos electrónicos de marketing. Puedes añadir este enlace para cancelar suscripción como pie de página en la parte inferior de tus correos electrónicos utilizando la etiqueta de Liquid {% raw %}``${email_footer}``{% endraw %}, o [personalizando el pie de página]({{site.baseurl}}/user_guide/channels/email/subscriptions#custom-footer) en tu plantilla.

## Paso 4: Comprueba si hay errores en el correo electrónico {#step-4-check-for-email-errors}

Los errores de correo electrónico se presentan en la pestaña **Redactar** del flujo de trabajo del mensaje. Los errores te impiden avanzar. Las "advertencias" indican recordatorios para ayudarte a seguir las mejores prácticas. Dependiendo de tu negocio, puedes optar por ignorarlas.

![Lista de errores y advertencias de un ejemplo de correo electrónico.]({% image_buster /assets/img/dnd_compose_error.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

A continuación, se muestra una lista de errores que se contemplan en nuestro editor:

- Sintaxis de Liquid incorrecta
- [Cuerpos de correo electrónico de más de 400 kb; se recomienda encarecidamente que los cuerpos sean inferiores a 102 kb]({{site.baseurl}}/user_guide/channels/email/best_practices)
- Plantillas sin un enlace para cancelar suscripción
- Correos electrónicos con el **Cuerpo** o el **Asunto** en blanco
- Correos electrónicos sin un enlace para cancelar suscripción

## Paso 5: Previsualiza y prueba tu mensaje {#step-5-preview-and-test-your-message}

Cuando termines de componer tu plantilla, puedes probarla antes de enviarla.

Desde la parte inferior de la pantalla de resumen, selecciona **Vista previa y prueba**. Aquí puedes previsualizar cómo aparecerá tu correo electrónico en el buzón de entrada de un cliente. Con **Previsualizar como usuario** seleccionado, puedes previsualizar tu correo electrónico como un usuario aleatorio, seleccionar un usuario específico o crear un usuario personalizado. Esto te permite probar que tu contenido conectado y las llamadas de personalización funcionan como deberían.

Luego, puedes usar **Copiar enlace de vista previa** para generar y copiar un enlace de vista previa compartible que muestre cómo se ve el correo electrónico para un usuario aleatorio. Para más información, consulta [Vista previa compartible]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).

También puedes alternar entre las vistas de escritorio, móvil y texto plano para tener una idea de cómo aparece tu mensaje en diferentes contextos.

{% alert tip %}
¿Tienes curiosidad por saber cómo se ve tu correo electrónico para los usuarios del modo oscuro? Selecciona el conmutador **Vista previa del modo oscuro** ubicado en la sección **Vista previa y prueba** (solo en el editor de arrastrar y soltar).
{% endalert %}

Cuando estés listo para una revisión final, selecciona **Envío de prueba** y envía un mensaje de prueba a ti mismo o a un grupo de testers de contenido para asegurarte de que tu correo electrónico se muestra correctamente en una variedad de dispositivos y clientes de correo electrónico.

![Ejemplo de vista previa de correo electrónico que se enviará para prueba.]({% image_buster /assets/img_archive/newEmailTest.png %})

Si ves algún problema con tu plantilla o quieres hacer algún cambio, selecciona **Editar correo electrónico** para volver al editor. Ten en cuenta que los cambios realizados en el editor **Clásico** pueden no reflejarse en el editor HTML ni en la vista previa del correo electrónico.

## Paso 6: Guarda tu plantilla {#step-6-save-your-template}

Asegúrate de guardar tu plantilla seleccionando **Guardar plantilla**. Ahora estás listo para usar esta plantilla en cualquier Campaign o componente de Canvas que elijas. Para acceder a tu plantilla, selecciona la experiencia de edición con la que la creaste y luego selecciónala de la lista de plantillas disponibles.

{% alert note %}
Si realizas alguna edición en una plantilla existente, esos cambios no se reflejarán en las Campaigns creadas con versiones anteriores de esa plantilla.
{% endalert %}

### Gestiona tus plantillas {#manage-your-templates}

Puedes ver las plantillas de correo electrónico en **Plantillas** > **Plantillas de correo electrónico**, filtrando por estado, tipo, etiquetas, el usuario que la creó, o buscando por nombre de plantilla. Necesitas los permisos de usuario relevantes, como **Ver plantillas de correo electrónico**, para ver estas plantillas. Para más detalles, consulta [Permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

A medida que crees más plantillas de correo electrónico, puedes [duplicar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#duplicating-templates) y [archivar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#archiving-templates) plantillas de correo electrónico. Obtén más información sobre cómo crear y gestionar tu biblioteca de plantillas y contenido creativo en [Plantillas y medios]({{site.baseurl}}/user_guide/messaging/templates).

### Usa tus plantillas en Campaigns de API {#use-your-templates-in-api-campaigns}

Para usar tu correo electrónico en una Campaign de API, necesitas un `email_template_id`, que se encuentra en la parte inferior de cualquier plantilla de correo electrónico creada en Braze.

![Identificador de API ubicado en la parte inferior de una plantilla de correo electrónico.]({% image_buster /assets/img/email_templates/template5.png %})

### Comenta en las plantillas de correo electrónico {#comment-on-email-templates}

Puedes colaborar y comentar en las plantillas de correo electrónico en el editor de arrastrar y soltar.

1. Selecciona el bloque de contenido o la fila en el cuerpo del correo electrónico en la que deseas comentar.
2. Selecciona el icono de comentario <i class="fas fa-comment" aria-label="Comentario"></i>.
3. Ingresa tu comentario en la barra lateral y luego selecciona **Enviar**.
4. Después de ingresar tus comentarios, selecciona **Listo**.
5. Selecciona **Guardar plantilla** para guardar tus comentarios.

Después de guardar tu plantilla, los usuarios pueden ver iconos sobre los comentarios no resueltos. Selecciona **Resolver** para resolver estos comentarios.

![Un comentario en una plantilla de correo electrónico que dice "Me parece bien".]({% image_buster /assets/img/email_templates/template_comment.png %})

Para respuestas a las preguntas frecuentes sobre plantillas de correo electrónico, consulta nuestras [Preguntas frecuentes sobre plantillas]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq).