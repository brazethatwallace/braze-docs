---
nav_title: "Pantalla completa"
article_title: Mensajes dentro de la aplicación a pantalla completa
description: "Este artículo de referencia cubre los requisitos de mensaje y diseño de los mensajes dentro de la aplicación a pantalla completa."
page_type: reference
page_order: 1
channel:
  - in-app messages
tool:
  - Media

---

# Mensajes dentro de la aplicación a pantalla completa {#fullscreen-in-app-messages}

> Los mensajes a pantalla completa ocupan toda la pantalla del dispositivo. Este tipo de mensaje es ideal cuando realmente necesitas la atención de tu usuario, como para actualizaciones obligatorias de la aplicación.

Este tipo de mensaje está disponible tanto en el [editor de arrastrar y soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/) como en el [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/).

{% tabs %}
{% tab Vertical %}

![Dos mensajes dentro de la aplicación a pantalla completa en orientación vertical, uno junto al otro, detallando las recomendaciones de imagen y texto. Consulta las siguientes secciones para más detalles.]({% image_buster /assets/img/full-screen-spec.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Horizontal %}

![Dos mensajes dentro de la aplicación a pantalla completa en orientación horizontal, uno junto al otro, detallando las recomendaciones de imagen y texto. Consulta las siguientes secciones para más detalles.]({% image_buster /assets/img/full-screen-spec-landscape.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

## Imágenes {#images}

Los mensajes dentro de la aplicación a pantalla completa llenarán toda la altura del dispositivo y se recortarán horizontalmente (lados izquierdo y derecho) según sea necesario. Los mensajes a pantalla completa con imagen y texto llenarán el 50 % de la altura del dispositivo. Todos los mensajes dentro de la aplicación a pantalla completa llenarán la barra de estado en dispositivos con "muesca".

- Todas las imágenes deben pesar menos de 5&nbsp;MB.
- Solo aceptamos archivos de tipo PNG, JPEG y [GIF]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/#gifs).
- Recomendamos que tus imágenes pesen 500&nbsp;KB.

{% alert tip %} ¡Crea activos con confianza! Nuestras plantillas de imágenes para mensajes dentro de la aplicación y las superposiciones de zona segura están diseñadas para funcionar correctamente en dispositivos de todos los tamaños. [Descargar plantillas de diseño en ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

### Vertical {#portrait}

| diseño | tamaño del activo | notas |
|--- | --- | --- |
| Imagen y texto | Relación de aspecto 6:5<br> Alta resolución 1200 x 1000&nbsp;px<br> Mínimo 600 x 500&nbsp;px | Puede haber recorte en todos los lados, pero la imagen siempre llenará el 50 % superior del viewport |
| Solo imagen | Relación de aspecto 3:5<br> Alta resolución 1200 x 2000&nbsp;px<br> Mínimo 600 x 1000&nbsp;px | Puede haber recorte en los bordes izquierdo y derecho en dispositivos más altos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Portrait" }

### Horizontal {#landscape}

| diseño | tamaño del activo | notas |
|--- | --- | --- |
| Imagen y texto | Relación de aspecto 10:3<br> Alta resolución 2000 x 600px<br> Mínimo 1000 x 300&nbsp;px | Puede haber recorte en todos los lados, pero la imagen siempre llenará el 50 % superior del viewport |
| Solo imagen | Relación de aspecto 5:3<br> Alta resolución 2000 x 1200px<br> Mínimo 1000 x 600&nbsp;px | Puede haber recorte en los bordes izquierdo y derecho en dispositivos más altos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Landscape" }

### Zona segura de imagen {#image-safe-zone}

Al previsualizar un mensaje dentro de la aplicación a pantalla completa en la plataforma Braze, puedes habilitar la zona segura de imagen en el área del mensaje que está protegida contra el recorte cuando se muestra en distintos dispositivos. Además de probar la zona segura de imagen en el panel de vista previa, te recomendamos [probar tu mensaje]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=in-app%20message) como siempre.

![Vista previa de un mensaje dentro de la aplicación en Braze con la opción "Mostrar zona segura de imagen" habilitada. La zona segura de imagen es una superposición sobre la imagen que visualiza qué partes de la imagen estarán protegidas contra el recorte.]({% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %})

## Pantallas más grandes {#larger-screens}

En una tableta o un navegador de escritorio, un mensaje dentro de la aplicación a pantalla completa se ubicará en el centro de la pantalla de la aplicación, como se muestra en la siguiente captura de pantalla.

{% tabs %}
{% tab Vertical %}

![Mensaje dentro de la aplicación a pantalla completa tal como aparecería en una pantalla grande en orientación vertical. El mensaje aparece como un modal grande ubicado en el centro de la pantalla.]({% image_buster /assets/img/full-screen-large-viewport.png %}){: style="border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Horizontal %}

![Mensaje dentro de la aplicación a pantalla completa tal como aparecería en una pantalla grande en orientación horizontal. El mensaje aparece como un modal grande ubicado en el centro de la pantalla.]({% image_buster /assets/img/full-screen-large-viewport-landscape.png %}){: style="max-width:80%;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}