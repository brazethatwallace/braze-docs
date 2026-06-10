---
nav_title: Asistente de plantillas de mensajes
article_title: Asistente de plantillas de mensajes
permalink: "/template_assistant/"
description: "Este artículo de referencia explica cómo usar el asistente de plantillas de mensajes para generar plantillas para tu mensajería de correo electrónico."
page_type: reference
---

# Asistente de plantillas de mensajes {#message-template-assistant}

> El asistente de plantillas de mensajes te ayuda a iterar sobre una plantilla de correo electrónico HTML existente utilizando GenAI para generar plantillas basadas en tus necesidades específicas. Esta funcionalidad puede ayudarte a optimizar tu contenido para un caso de uso, audiencia o conversión específicos, y a reducir el tiempo y el esfuerzo al redactar correos electrónicos.

{% alert important %}
El asistente de plantillas de mensajes se encuentra en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente si te interesa participar en este acceso anticipado. <br><br>Actualmente, esta funcionalidad solo es compatible con el canal de correo electrónico y solo en el editor HTML, no en otros editores (como arrastrar y soltar o AMP).
{% endalert %}

## Cómo funciona {#how-it-works}

El asistente de plantillas de mensajes utiliza tus [directrices de marca](https://www.braze.com/docs/user_guide/administrative/app_settings/brand_guidelines) y la [configuración de estilo global](https://www.braze.com/docs/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings) para adaptar el contenido y el estilo del mensaje a tu marca.

Por ejemplo, si tienes configurados los ajustes de estilo global, el asistente de plantillas de mensajes incorporará los colores y estilos de tu marca. Si tienes directrices de marca definidas en Braze, el asistente también puede hacer referencia a ellas para crear textos con el tono y la personalidad de tu marca.

El asistente de plantillas de mensajes puede recordar tu historial de chat solo mientras sigas en la misma ventana de chat. Esto significa que puede hacer referencia a prompts anteriores utilizados para generar los futuros. El asistente también intentará iterar tu plantilla para que sea adaptable a dispositivos móviles.

Por ejemplo, si pasas de un prompt específico sobre una marca de fitness a una marca genérica en tus prompts posteriores, el asistente de plantillas de mensajes puede informar a la plantilla de que se trata de esa misma marca de fitness. Para iniciar un nuevo chat, selecciona **Borrar historial** en la ventana de chat y abre de nuevo el asistente de plantillas de mensajes.

## Crear una plantilla {#creating-a-template}

1. En el dashboard, ve a **Plantillas** > **Plantillas de correo electrónico**.
2. Selecciona una plantilla de correo electrónico existente.
3. En la sección **Crear con IA** del editor HTML, selecciona **Plantilla**.
4. Desde aquí, puedes introducir una variedad de prompts o hacer preguntas sobre tu contenido.
5. El asistente de plantillas de mensajes proporcionará una respuesta y determinará qué cambios son necesarios en tu plantilla.
6. Selecciona **Generar** para aplicar las sugerencias.

{% alert important %}
Recomendamos encarecidamente probar el resultado generado para asegurarte de que coincide con tu mensajería.
{% endalert %}

![Un ejemplo de prompt para crear una plantilla con múltiples secciones que se usará para varios correos electrónicos. El asistente de plantillas de mensajes explica las modificaciones a la plantilla actual.]({% image_buster /assets/unlisted_docs/img/ai_message_template_assistant1.png %}){: style="width:70%;"}

### Ejemplos de prompts {#example-prompts}

Aquí tienes algunos ejemplos de prompts para empezar:

- Añadir un cuestionario de opinión al final del correo electrónico
- Cambiar la fuente a {% raw %}`{{font name}}` y el tamaño de fuente del párrafo a tamaño `{{number}}`{% endraw %}
- Hacer que todas las imágenes tengan esquinas redondeadas
- Añadir otra sección con una imagen y una llamada a la acción

{% alert note %}
Dependiendo de tu prompt y la respuesta, el asistente de plantillas de mensajes puede añadir imágenes de marcador de posición al generar la nueva plantilla.
{% endalert %}