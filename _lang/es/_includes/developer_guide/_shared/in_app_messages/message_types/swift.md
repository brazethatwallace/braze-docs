{% tab swift %}
Cada tipo de mensaje dentro de la aplicación es altamente personalizable en cuanto a contenido, imágenes, iconos, acciones de clic, análisis, visualización y entrega. Son tipos enumerados de `Braze.InAppMessage`, que define el comportamiento y los rasgos básicos de todos los mensajes dentro de la aplicación. Para ver la lista completa de propiedades y usos de los mensajes dentro de la aplicación, consulta la [clase `InAppMessage`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

Estos son los tipos de mensajes dentro de la aplicación disponibles en Braze y cómo se verán para los usuarios finales.

{% subtabs %}
{% subtab Slideup %}

Los mensajes dentro de la aplicación [`Slideup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/slideup-swift.struct) reciben este nombre porque se "deslizan hacia arriba" o "hacia abajo" desde la parte superior o inferior de la pantalla. Cubren una pequeña parte de la pantalla y proporcionan una capacidad de mensajería eficaz y no intrusiva.

![Un mensaje de deslizamiento hacia arriba dentro de la aplicación en la parte inferior y superior de la pantalla del teléfono.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width:35%;border:none;"}


{% endsubtab %}
{% subtab Modal %}

Los mensajes dentro de la aplicación [`Modal`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modal-swift.struct) aparecen en el centro de la pantalla y están enmarcados por un panel translúcido. Útiles para una mensajería más crítica, pueden equiparse con hasta dos botones habilitados para análisis.

![Un mensaje modal dentro de la aplicación en el centro de la pantalla del teléfono.]({% image_buster /assets/img/modal-header-text.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Modal Image %}

Los mensajes dentro de la aplicación [`Modal Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modalimage-swift.struct) aparecen en el centro de la pantalla y están enmarcados por un panel translúcido. Estos mensajes son similares a los del tipo `Modal`, excepto que no tienen encabezado ni texto de mensaje. Útiles para una mensajería más crítica, pueden equiparse con hasta dos botones habilitados para análisis.

![Un mensaje modal de imagen dentro de la aplicación en el centro de la pantalla del teléfono.]({% image_buster /assets/img/modal-full-image.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Fullscreen %}

Los mensajes dentro de la aplicación [`Full`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/full-swift.struct) son útiles para maximizar el contenido y el impacto de tu comunicación con el usuario. La mitad superior de un mensaje dentro de la aplicación `Full` contiene una imagen, y la mitad inferior muestra texto y hasta dos botones habilitados para análisis.

![Un mensaje dentro de la aplicación a pantalla completa que se muestra en toda la pantalla del teléfono.]({% image_buster /assets/img/full-screen-header-text.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Full Screen Image %}

Los mensajes dentro de la aplicación [`Full Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/fullimage-swift.struct) son similares a los mensajes dentro de la aplicación `Full`, excepto que no tienen encabezado ni texto de mensaje. Este tipo de mensaje es útil para maximizar el contenido y el impacto de tu comunicación con el usuario. Un mensaje dentro de la aplicación `Full Image` contiene una imagen que abarca toda la pantalla, con la opción de mostrar hasta dos botones habilitados para análisis.

![Un mensaje dentro de la aplicación con una imagen a pantalla completa que se muestra en toda la pantalla del teléfono.]({% image_buster /assets/img/full-screen-image.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Custom HTML %}

Los mensajes dentro de la aplicación [`HTML`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/html-swift.struct) son útiles para crear contenido de usuario totalmente personalizado. El contenido HTML completo de los mensajes dentro de la aplicación, definido por el usuario, se muestra en un `WKWebView` y puede contener opcionalmente otros contenidos enriquecidos, como imágenes y fuentes, lo que permite un control total sobre el aspecto y la funcionalidad de los mensajes. <br><br>Los mensajes dentro de la aplicación de iOS admiten una interfaz JavaScript `brazeBridge` para llamar a métodos del SDK Web de Braze desde dentro de tu HTML; consulta nuestras [mejores prácticas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices) para obtener más detalles.

El siguiente ejemplo muestra un mensaje HTML completo paginado dentro de la aplicación:

![Un mensaje HTML dentro de la aplicación con un carrusel de contenido y botones interactivos.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

Ten en cuenta que actualmente no admitimos la visualización de mensajes HTML personalizados dentro de la aplicación en un iFrame en las plataformas iOS y Android.

{% endsubtab %}
{% subtab Control %}

Los mensajes dentro de la aplicación [`Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/control-swift.struct) no contienen un componente de interfaz de usuario y se utilizan principalmente con fines de análisis. Este tipo se utiliza para verificar la recepción de un mensaje dentro de la aplicación enviado a un grupo de control.

Para más detalles sobre la optimización automática de variantes y los grupos de control, consulta [Optimizar con BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

{% endsubtab %}
{% endsubtabs %}
{% endtab %}