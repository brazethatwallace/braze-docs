---
nav_title: Usar códigos
article_title: Usar códigos promocionales
page_order: 0.2
description: "Aprende a usar códigos promocionales y a consultar el uso en tus campañas y Canvas."
---

# Usar códigos promocionales

> Aprende a usar códigos promocionales y a consultar el uso en tus campañas y Canvas.

## Requisitos previos

Antes de poder usar códigos promocionales, necesitarás [crear una lista de códigos promocionales]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create/).

## Uso de códigos promocionales

Para enviar un código promocional en un mensaje, selecciona **Copiar fragmento de código** junto a la lista de códigos promocionales [que creaste anteriormente]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create/#create).

![Opción para copiar el fragmento de código y pegarlo en tu mensaje.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

Pega los fragmentos de código en uno de tus mensajes en Braze y luego usa [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) para insertar uno de los códigos promocionales únicos de tu lista. Ese código se marca como enviado, lo que garantiza que ningún otro mensaje envíe el mismo código.

![Un mensaje de ejemplo "Date un capricho esta primavera con nuestra oferta exclusiva" seguido del fragmento de código.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

### Entre pasos en Canvas

Cuando se usa un fragmento de código en una campaña o Canvas con mensajes multicanal, cada usuario recibe un código único. En un Canvas con múltiples pasos que hacen referencia a códigos promocionales, un usuario obtiene un nuevo código por cada paso en el que entra.

Para asignar un código promocional en un Canvas y reutilizarlo entre pasos:

1. Asigna el código promocional como atributo personalizado en el primer paso (Actualización de usuario).
2. Usa Liquid en los pasos posteriores para hacer referencia a ese atributo personalizado en lugar de generar un nuevo código.

Cuando un usuario califica para un código en múltiples canales, recibe el mismo código en cada canal. Por ejemplo, si recibe mensajes por correo electrónico y push, el mismo código se envía a ambos. Los informes también reflejan un único código.

{% alert note %}
Si no hay códigos promocionales disponibles, los mensajes de prueba o en vivo que dependen de códigos no se envían.
{% endalert %}

### Campañas de mensajes dentro de la aplicación {#promotion-codes-iam-campaigns}

Después de crear una [campaña de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages), puedes insertar un [fragmento de código de lista de códigos promocionales]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage/#using-promotion-codes-1) en el cuerpo de tu mensaje dentro de la aplicación. Los códigos promocionales en mensajes dentro de la aplicación se deducen y se usan solo cuando un usuario desencadena la visualización del mensaje dentro de la aplicación.

### Mensajes de prueba

Los envíos de prueba y los envíos de correo electrónico a grupos semilla consumen códigos promocionales a menos que se solicite lo contrario. Ponte en contacto con tu director de cuentas de Braze para actualizar el comportamiento de esta característica y que los códigos promocionales no se usen durante los envíos de prueba y los envíos de correo electrónico a grupos semilla.

### Con extras de mensaje para Currents

{% multi_lang_include partners/shopify.md section='Liquid promotion codes with Currents' %}

## Guardar códigos promocionales en perfiles de usuario {#save-to-profile}

Para hacer referencia al mismo código promocional en mensajes posteriores, el código debe guardarse en el perfil de usuario como un atributo personalizado. Esto se puede hacer a través de un [paso de Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/) que asigna el código de descuento a un atributo personalizado, como "Promo Code", directamente antes de un paso de Mensaje.

Primero, selecciona lo siguiente para cada campo en el paso de Actualización de usuario:

- **Nombre del atributo:** Promo Code
- **Acción:** Actualizar
- **Valor clave:** El fragmento de código Liquid del código promocional, como {% raw %}`{% promotion('spring25') %}`{% endraw %}

Segundo, añade el atributo personalizado (en este ejemplo, {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %}) a un mensaje. El código de descuento se inserta mediante plantilla.

## Consultar el uso de códigos promocionales

Puedes encontrar el recuento de códigos restantes en la columna **Restantes** de la lista de códigos promocionales en la página **Códigos promocionales**.

![Ejemplo de un código promocional con códigos sin usar.]({% image_buster /assets/img/promocodes/promocode11.png %})

Este recuento de códigos también se puede encontrar al volver a visitar una página de lista de códigos promocionales existente. También puedes exportar los códigos sin usar como un archivo CSV.

![Un código promocional llamado "Black Friday Sale" con 992 códigos restantes.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

## Envíos multicanal y de canal único

Para campañas y Canvas multicanal y de envío único, todos los códigos promocionales referenciados en el Liquid de un mensaje se deducen para ser usados **antes** de que el mensaje se envíe, para garantizar lo siguiente:

- Los mismos códigos promocionales se usan en todos los canales en un mensaje multicanal.
- Los códigos promocionales adicionales no se usan si un mensaje falla o se cancela.

Si un usuario tiene dos listas de códigos promocionales referenciadas en un mensaje que se divide por una etiqueta de lógica condicional de Liquid, todos los códigos promocionales se deducen igualmente, independientemente del flujo condicional que siga el usuario.

Si un usuario entra en un nuevo paso en Canvas o vuelve a entrar en un Canvas, y el fragmento de código Liquid del código promocional se aplica de nuevo para un mensaje a ese usuario, se usa un nuevo código promocional.

### Ejemplo

En el siguiente ejemplo, ambas listas de códigos promocionales `vip-deal` y `regular-deal` se deducen. Este es el Liquid:

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %}
```
{% endraw %}

Braze recomienda cargar más códigos promocionales de los que estimas usar. Si una lista de códigos promocionales caduca o se queda sin códigos promocionales, los mensajes posteriores se cancelan.

{% alert tip %}
**Aquí tienes una analogía de cómo se consumen los códigos promocionales en Braze.** <br><br>Imagina que enviar tu mensaje es como enviar una carta en la oficina de correos. Le das la carta a un empleado, y este ve que tu carta debería incluir un cupón. El empleado toma el primer cupón de la pila y lo añade al sobre. El empleado envía la carta, pero por alguna razón, la carta se pierde en el correo (y el cupón también se pierde). <br><br>En este escenario, Braze es el empleado de correos y tu código promocional es el cupón. No podemos recuperarlo después de que se haya tomado de la pila de códigos promocionales, independientemente del resultado del webhook.
{% endalert %}