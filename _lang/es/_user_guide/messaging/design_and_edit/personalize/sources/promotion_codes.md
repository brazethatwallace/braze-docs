---
nav_title: Códigos promocionales
article_title: Códigos promocionales
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "Aprende sobre las listas de códigos promocionales para poder añadirlos a tus campañas y Canvas."
---

# Códigos promocionales

> Aprende sobre las listas de códigos promocionales para poder añadirlos a tus campañas y Canvas.

## Acerca de los códigos promocionales

Los códigos promocionales te permiten insertar valores únicos y con tiempo limitado en los mensajes para impulsar las conversiones. Cada lista puede contener hasta 20 millones de códigos, y cada código puede durar hasta seis meses antes de expirar.

Cuando Braze envía un mensaje con un código promocional, el código se descuenta antes de que el mensaje salga. Para garantizar que los códigos sean consistentes, únicos y nunca se reutilicen:

- Un mensaje fallido igualmente consume el código.
- En envíos multicanal, el mismo código se aplica en todos los canales.
- Con Liquid condicional, todas las listas referenciadas tienen códigos descontados, incluso si solo se muestra una rama.
- Entrar o volver a entrar en un paso en Canvas consume un nuevo código.

Si colocas múltiples fragmentos de código de la misma lista en un mensaje, Braze aplicará el mismo código en todos los fragmentos. Para evitar quedarte sin códigos, te recomendamos cargar más códigos de los que esperas usar.

{% tabs local %}
{% tab Ejemplo %}
Piensa en los códigos promocionales como cupones en una oficina de correos. Una vez que el empleado saca un cupón de la pila para tu carta, desaparece, incluso si la carta nunca llega.

Por ejemplo, en el siguiente Liquid condicional, los códigos de ambas listas (`vip-deal` y `regular-deal`) se descuentan, aunque cada usuario solo ve una rama:

{% raw %}
```liquid
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert important %}
Los códigos promocionales no se pueden enviar en mensajes dentro de la aplicación en Canvas.
{% endalert %}

## Próximos pasos

¿Buscas los próximos pasos? Empieza aquí:

- [Crear una lista de códigos promocionales]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create/)
- [Usar códigos promocionales]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage/#using-promotion-codes)
- [Ver el uso de códigos promocionales]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage/#viewing-promotion-code-usage)

## Preguntas frecuentes

### ¿Qué canales de mensajería puedo usar con los códigos promocionales?

Los códigos promocionales son compatibles actualmente con correo electrónico, push móvil, notificación push web, Tarjetas de contenido, webhook, SMS y WhatsApp. Las campañas de correo electrónico transaccional de Braze y los mensajes dentro de la aplicación no son compatibles actualmente con los códigos promocionales.

### ¿Los envíos de prueba y los envíos de grupo semilla cuentan para el uso?

De forma predeterminada, los envíos de prueba y los envíos de correo electrónico de grupo semilla usarán códigos promocionales por usuario, por envío de prueba. Sin embargo, puedes ponerte en contacto con tu director de cuentas de Braze para actualizar este comportamiento y no usar códigos promocionales durante las pruebas.

### ¿Qué sucede cuando múltiples canales de mensajería usan el mismo fragmento de código promocional?

Si un usuario en particular es elegible para recibir un código a través de múltiples canales, recibirá el mismo código a través de cada canal. Solo se usará un código promocional independientemente de los canales recibidos.

### ¿Puedo usar múltiples fragmentos de código Liquid para hacer referencia a la misma lista de códigos promocionales en un mensaje?

Sí. Braze aplicará el mismo código promocional en todas las instancias de ese fragmento en el mensaje, asegurando que el usuario solo reciba un código único.

### ¿Qué sucede cuando una lista de códigos promocionales está expirada o vacía?

Los códigos expirados se eliminan después de seis meses.

Si el mensaje debía contener un código promocional de una lista vacía o expirada, el mensaje se cancelará.

Si el mensaje contiene lógica Liquid que inserta condicionalmente un código promocional, el mensaje solo se cancelará si debía contener un código promocional. Si el mensaje no debía contener un código promocional, el mensaje se enviará normalmente.

### Si cargué los códigos promocionales incorrectos, ¿puedo actualizarlos?

Sí. Puedes resolver esto descontinuando la lista completa o usando un marcador de posición para eliminar la lista. Para más información, consulta [Actualizar una lista de códigos promocionales]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create/#updating-a-promotion-code-list).

### ¿Puedo guardar un código promocional en el perfil de un usuario para mensajes futuros?

Sí. Puedes guardar códigos promocionales en el perfil de un usuario a través de un paso de Actualización de usuario. Para más información, consulta [Guardar códigos promocionales en perfiles de usuario]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage/#save-to-profile).