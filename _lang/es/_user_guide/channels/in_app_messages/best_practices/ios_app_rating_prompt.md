---
nav_title: Solicitud de valoración en la aplicación para iOS
article_title: Solicitud de valoración en la aplicación para iOS
page_order: 6
description: "Este artículo describe los enfoques e implicaciones de usar Braze para pedir a los usuarios que valoren tu aplicación."
channel:
  - in-app messages

---

# Solicitud de valoración en la aplicación para iOS {#in-app-rating-prompt-for-ios}

> Este artículo describe los enfoques e implicaciones de usar Braze para pedir a los usuarios que valoren tu aplicación. Para obtener consejos sobre cómo crear una Campaign de valoración de aplicación eficaz, consulta [Lo que debes y no debes hacer en las valoraciones de aplicaciones de clientes](https://www.braze.com/resources/articles/the-dos-and-donts-of-customer-app-ratings).

Apple ofrece una solicitud nativa, introducida con iOS 10.3, que permite a los usuarios valorar aplicaciones desde dentro de la propia aplicación. Si quieres solicitar valoraciones de la aplicación a los usuarios mediante un mensaje dentro de la aplicación en iOS, debes usar la solicitud nativa, ya que Apple no permite solicitudes de valoración personalizadas (consulta las [Directrices de revisión del App Store](https://developer.apple.com/app-store/review/guidelines/#code-of-conduct), sección 5.6.1).

Según las directrices de Apple, las solicitudes de valoración de la aplicación pueden mostrarse a un usuario hasta tres veces al año, por lo que cualquier Campaign de valoración de la aplicación debería aprovechar la [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping). Los usuarios también pueden optar por no ver las solicitudes de valoración de la aplicación en la configuración de su aplicación. Para más información sobre las valoraciones del App Store, consulta el artículo de Apple sobre [Valoraciones, reseñas y respuestas](https://developer.apple.com/app-store/ratings-and-reviews/).

## Usar Braze para pedir a los usuarios que valoren la aplicación {#using-braze-to-ask-users-for-app-reviews}

Aunque Apple requiere que uses la solicitud nativa, puedes aprovechar las Campaigns de Braze para pedir a los usuarios que valoren y reseñen tu aplicación en el momento adecuado. Hay dos enfoques principales que puedes adoptar.

### Enfoque 1: vínculo profundo al App Store {#approach-1-deep-linking-to-the-app-store}

Con este enfoque, quieres animar a los usuarios a visitar el App Store para añadir una reseña. Para ello, crea una Campaign de mensaje dentro de la aplicación que tenga un [vínculo profundo]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls) al App Store.

![Dos pantallas de móvil una al lado de la otra. La primera es un mensaje dentro de la aplicación que pide al usuario que valore la aplicación en el App Store. La segunda es la página del App Store de iOS para esa aplicación.]({% image_buster /assets/img_archive/app_store_app_review.png %})

### Enfoque 2: preparación previa {#approach-2-soft-priming}

Si no quieres que los usuarios abandonen tu aplicación, puedes preparar primero a los usuarios con un mensaje dentro de la aplicación independiente. La preparación previa es una forma de pedir permiso a los usuarios antes de enviarles la solicitud nativa de valoración del App Store. Para ello, crea una Campaign de mensaje dentro de la aplicación y añade un vínculo profundo personalizado que llame al método `requestReview` cuando se haga clic.

Para ver los pasos detallados, consulta [Solicitud personalizada de valoración del App Store]({{site.baseurl}}/developer_guide/in_app_messages/customization#swift_customizing-the-app-store-review-prompt).

![Dos mensajes dentro de la aplicación uno al lado del otro. El primero prepara al usuario para valorar la aplicación preguntándole si tiene un momento para valorarla. El segundo es el mensaje nativo de valoración del App Store de iOS, que muestra una escala de cinco estrellas que el usuario puede seleccionar para valorar la aplicación.]({% image_buster /assets/img_archive/prime_app_review.png %})

Los usuarios enviarán una valoración a través de la solicitud nativa de valoración del App Store, y podrán escribir y enviar una reseña sin salir de la aplicación.

### Consideraciones {#considerations}

Como alternativa a la preparación previa, también podrías mostrar la solicitud de valoración de la aplicación de iOS directamente sin que se muestre antes ningún mensaje de preparación de Braze. La ventaja de esto es que, si el usuario ha optado por no recibir solicitudes de valoración de la aplicación, no se produciría la experiencia de usuario subóptima de intentar valorar la aplicación sin que aparezca ninguna solicitud para hacerlo.

{% alert important %}
No crees mensajes HTML personalizados dentro de la aplicación que imiten una solicitud nativa de valoración de la aplicación de iOS, ya que esto viola las directrices de Apple.
{% endalert %}