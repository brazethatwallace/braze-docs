{% multi_lang_include developer_guide/prerequisites/web.md %} Sin embargo, no es necesaria ninguna configuración adicional.

## Tipos de mensaje {#message-types}

Todos los mensajes dentro de la aplicación heredan su prototipo de [`InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html), que define el comportamiento y las características básicas de todos los mensajes dentro de la aplicación. Las subclases prototípicas son [`SlideUpMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html), [`ModalMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html), [`FullScreenMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) y [`HtmlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html).

Cada tipo de mensaje dentro de la aplicación es personalizable en cuanto a contenido, imágenes, iconos, acciones de clic, análisis, visualización y entrega.

{% tabs %}
{% tab Deslizamiento hacia arriba %}

Los mensajes dentro de la aplicación [`SlideUp`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html) se llaman así porque, tradicionalmente en plataformas móviles, "se deslizan hacia arriba" o "se deslizan hacia abajo" desde la parte superior o inferior de la pantalla. En el SDK or kit de desarrollo de software Web de Braze, estos mensajes se muestran más como una notificación de estilo Growl o Toast para alinearse con el paradigma dominante de la web. Cubren una pequeña parte de la pantalla y ofrecen una capacidad de mensajería eficaz y no intrusiva.

![Un mensaje dentro de la aplicación deslizándose desde la parte inferior de la pantalla de un teléfono que muestra "Humans are complicated. Custom engagement shouldn't be." En el fondo se muestra el mismo mensaje dentro de la aplicación en la esquina inferior de una página web.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

Los mensajes dentro de la aplicación [`Modal`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html) aparecen en el centro de la pantalla y están enmarcados por un panel translúcido. Son útiles para mensajes más importantes y pueden incluir hasta dos botones con acciones de clic y análisis habilitados.

![Un mensaje modal dentro de la aplicación en el centro de la pantalla de un teléfono que muestra "Humans are complicated. Custom engagement shouldn't be." En el fondo se muestra el mismo mensaje dentro de la aplicación en el centro de una página web.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Pantalla completa %}

Los mensajes dentro de la aplicación [`Full`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) son útiles para maximizar el contenido y el impacto de la comunicación con tus usuarios. En ventanas de navegador estrechas (por ejemplo, la web móvil), los mensajes dentro de la aplicación `full` ocupan toda la ventana del navegador. En ventanas de navegador más grandes, los mensajes dentro de la aplicación `full` se muestran de forma similar a los mensajes dentro de la aplicación `modal`. La mitad superior de un mensaje dentro de la aplicación `full` contiene una imagen, y la mitad inferior permite hasta ocho líneas de texto, así como hasta dos botones con acciones de clic y análisis habilitados.

![Un mensaje dentro de la aplicación a pantalla completa que se muestra en toda la pantalla de un teléfono con el texto "Humans are complicated. Custom engagement shouldn't be." En el fondo se muestra el mismo mensaje dentro de la aplicación de gran tamaño en el centro de una página web.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab HTML personalizado %}

Los mensajes dentro de la aplicación [`HTML`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html) son útiles para crear contenido de usuario totalmente personalizado. El HTML definido por el usuario se muestra en un iFrame y puede incluir contenido enriquecido, como imágenes, fuentes, videos y elementos interactivos, lo que permite un control total sobre la apariencia y la funcionalidad del mensaje. Estos admiten una interfaz JavaScript `brazeBridge` para llamar a métodos del SDK or kit de desarrollo de software Web de Braze desde tu HTML; consulta nuestras [buenas prácticas]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices) para más detalles.

{% alert important %}
Para habilitar los mensajes dentro de la aplicación HTML a través del SDK or kit de desarrollo de software Web, **debes** proporcionar la opción de inicialización `allowUserSuppliedJavascript` a Braze, por ejemplo, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Esto es por razones de seguridad. Los mensajes dentro de la aplicación HTML pueden ejecutar JavaScript, por lo que requerimos que un responsable del sitio los habilite.
{% endalert %}

El siguiente ejemplo muestra un mensaje dentro de la aplicación HTML paginado:

![Un mensaje dentro de la aplicación HTML con un carrusel de contenido y botones interactivos.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

{% endtab %}
{% endtabs %}