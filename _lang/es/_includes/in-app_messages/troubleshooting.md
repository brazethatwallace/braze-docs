### Solución de problemas de visualización {#troubleshooting-in-app-message-display}

Si tu aplicación solicita y recibe correctamente mensajes dentro de la aplicación, pero no se muestran, es posible que la lógica del dispositivo esté impidiendo la visualización:

1. ¿Se desencadena el evento como se espera? Para comprobarlo, configura el mensaje para que se desencadene mediante una acción diferente (como el inicio de sesión) y verifica si se muestra.
{% if include.sdk == "iOS" %}
2. Los mensajes desencadenados dentro de la aplicación tienen una tasa limitada en función del [intervalo de tiempo mínimo entre desencadenamientos]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=swift#overriding-the-default-rate-limit), que es de 30 segundos de forma predeterminada.
{% elsif include.sdk == "Android" %}
2. Los mensajes desencadenados dentro de la aplicación tienen una tasa limitada en función del [intervalo de tiempo mínimo entre desencadenamientos]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=android#overriding-the-default-rate-limit), que es de 30 segundos de forma predeterminada.
{% elsif include.sdk == "Web" %}
2. Los mensajes desencadenados dentro de la aplicación tienen una tasa limitada en función del [intervalo de tiempo mínimo entre desencadenamientos]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web#overriding-the-default-rate-limit), que es de 30 segundos de forma predeterminada.
{% endif %}
3. Las descargas de imágenes fallidas impiden que se muestren los mensajes dentro de la aplicación con imágenes. Comprueba los registros del dispositivo en busca de fallos en las descargas. Prueba a eliminar temporalmente la imagen para ver si el mensaje se muestra.
{% case include.sdk %}
  {% when "iOS" %}
4. Si has configurado un delegado para personalizar la gestión de mensajes dentro de la aplicación, confirma que no está suprimiendo la visualización. Consulta [Personalización]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift).
  {% when "Android" %}
4. Si has configurado un delegado para personalizar la gestión de mensajes dentro de la aplicación, confirma que no está suprimiendo la visualización. Consulta [Personalización]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android).
  {% when "Web" %}
4. Si utilizas una gestión personalizada de mensajes dentro de la aplicación a través de [`braze.subscribeToInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage), verifica que la devolución de llamada no está suprimiendo la visualización. Consulta [Personalización]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=web).
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
5. Si la orientación del dispositivo no coincide con la configuración del mensaje dentro de la aplicación, el mensaje no se mostrará.
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
6. Dependiendo de las condiciones de la red, es posible que las imágenes tarden en descargarse antes de mostrarse. En conexiones lentas o dispositivos de bajo rendimiento, permite tiempo adicional u optimiza el tamaño de los activos.
{% endcase %}

{% if include.sdk == "iOS" %}
### Las impresiones y los clics no se registran {#impressions-and-clicks-arent-being-logged}

Si has configurado un delegado de mensajes dentro de la aplicación para gestionar manualmente la visualización del mensaje o las acciones de clic, debes [registrar los clics](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) y las [impresiones](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:)) manualmente en el mensaje dentro de la aplicación.
{% elsif include.sdk == "Android" %}
### Las impresiones y los clics no se registran

Si has configurado un delegado de mensajes dentro de la aplicación para gestionar manualmente la visualización del mensaje o las acciones de clic, debes registrar manualmente los clics y las impresiones en el mensaje dentro de la aplicación.
{% endif %}