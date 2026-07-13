---
nav_title: Uso del recuento de señales
article_title: Uso del recuento de señales
page_order: 8

page_type: reference
description: "Este artículo cubre el uso del recuento de señales de iOS para reactivar la interacción con usuarios que no notaron una notificación push o que han desactivado las notificaciones push en primer plano."
platform: iOS
channel:
- push
- in-app messages

---

# Uso del recuento de señales {#utilizing-badge-count}

> El recuento de señales de iOS muestra el número de notificaciones no leídas dentro de tu aplicación, en forma de un círculo rojo en la parte superior del icono de la aplicación. En los últimos años, las señales se han convertido en un medio eficaz para reactivar la interacción con los usuarios de la aplicación.

El recuento de señales se puede utilizar para reactivar la interacción con tus usuarios que no notaron una notificación push o que han desactivado las notificaciones push en primer plano. De manera similar, se puede utilizar para notificar a tus usuarios sobre mensajes no vistos, como actualizaciones dentro de la aplicación.

## Recuento de señales con Braze {#badge-count-with-braze}

Puedes especificar el recuento de señales deseado cuando redactas una notificación push a través del panel de Braze. Esto se puede configurar como un atributo de usuario con mensajería personalizada, lo que permite una lógica de personalización infinita. Si deseas enviar una notificación push silenciosa que actualice el recuento de señales sin molestar al usuario, añade la marca "Content-Available" a tu push y deja el contenido del mensaje vacío.

{% alert note %}
¿Te preguntas cómo configurar los recuentos de señales para Android? Android gestiona automáticamente las señales de la aplicación para push, por lo que no hay configuración de personalización para señales en Braze.
{% endalert %}

### Eliminar el recuento de señales {#removing-the-badge-count}

Establece el recuento de señales en 0 o "" para eliminar el recuento de señales del icono de la aplicación. Braze también borrará automáticamente la señal cuando se reciba una notificación push mientras la aplicación está en primer plano.

## Buenas prácticas {#best-practices}

Para optimizar el poder de reactivación de las señales, es crucial que configures los ajustes de señales de una manera que simplifique al máximo la experiencia del usuario.

### Mantén el recuento de señales bajo {#keep-the-badge-count-low}
Las investigaciones muestran que después de que el recuento de señales supera las dos cifras, los usuarios generalmente pierden interés en las actualizaciones y a menudo dejan de usar la aplicación por completo.

> Puede haber excepciones a esta regla dependiendo de la naturaleza de tu aplicación (por ejemplo, aplicaciones de correo electrónico y mensajería grupal).

### Limita lo que un recuento de señales puede representar {#limit-the-things-a-badge-count-can-represent}
Al usar señales, quieres que las notificaciones sean lo más claras y directas posible. Al limitar el número de cosas que una notificación de señal puede representar, puedes proporcionar a tus usuarios una sensación de familiaridad con las características y actualizaciones de tu aplicación.