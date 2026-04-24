Los mensajes dentro de la aplicación se entregan como mensajes dentro de la aplicación con plantilla cuando se selecciona **Reevaluar la elegibilidad de la campaña antes de mostrar** o si alguna de las siguientes etiquetas de Liquid existe en el mensaje:

- `canvas_entry_properties`
- `connected_content`
- Variables de SMS como {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Esto significa que durante el inicio de sesión, el dispositivo recibirá el desencadenante de ese mensaje dentro de la aplicación en lugar del mensaje completo. Cuando el usuario desencadene el mensaje dentro de la aplicación, su dispositivo realizará una solicitud de red para obtener el mensaje real.

{% alert note %}
El mensaje no se entregará si el dispositivo no tiene acceso a internet. Es posible que el mensaje no se entregue si la lógica de Liquid tarda demasiado en resolverse.
{% endalert %}