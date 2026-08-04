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

Este tipo de mensaje está disponible tanto en el [editor de arrastrar y soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) como en el [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).

{% tabs %}
{% tab Vertical %}

![Dos mensajes dentro de la aplicación a pantalla completa en orientación vertical, uno junto al otro, detallando las recomendaciones de imagen y texto. Consulta las siguientes secciones para más detalles.]({% image_buster /assets/img/full-screen-spec.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Horizontal %}

![Dos mensajes dentro de la aplicación a pantalla completa en orientación horizontal, uno junto al otro, detallando las recomendaciones de imagen y texto. Consulta las siguientes secciones para más detalles.]({% image_buster /assets/img/full-screen-spec-landscape.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

## Imágenes {#images}

Los mensajes dentro de la aplicación a pantalla completa llenarán toda la altura de un dispositivo y se recortarán horizontalmente (lados izquierdo y derecho) según sea necesario. Los mensajes a pantalla completa con imagen y texto llenarán el 50% de la altura de un dispositivo. Todos los mensajes dentro de la aplicación a pantalla completa llenarán la barra de estado en dispositivos con "muesca".

{% multi_lang_include in-app_messages/image_requirements.md %}

{% alert tip %} ¡Crea activos con confianza! Nuestras plantillas de imágenes para mensajes dentro de la aplicación y las superposiciones de zona segura están diseñadas para funcionar correctamente con dispositivos de todos los tamaños. [Descargar ZIP de plantillas de diseño]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

### Vertical {#portrait}

| diseño | tamaño del activo | notas |
|--- | --- | --- |
| Imagen y texto | Relación de aspecto 6:5<br> Alta resolución 1200 x 1000&nbsp;px<br> Mínimo 600 x 500&nbsp;px | Puede producirse recorte en todos los lados, pero la imagen siempre llenará el 50% superior de la ventana de visualización |
| Solo imagen | Relación de aspecto 3:5<br> Alta resolución 1200 x 2000&nbsp;px<br> Mínimo 600 x 1000&nbsp;px | Puede producirse recorte en el lado principal y en los bordes derechos en dispositivos más altos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Vertical" }

### Horizontal {#landscape}

| diseño | tamaño del activo | notas |
|--- | --- | --- |
| Imagen y texto | Relación de aspecto 10:3<br> Alta resolución 2000 x 600px<br> Mínimo 1000 x 300&nbsp;px | Puede producirse recorte en todos los lados, pero la imagen siempre llenará el 50% superior de la ventana de visualización |
| Solo imagen | Relación de aspecto 5:3<br> Alta resolución 2000 x 1200px<br> Mínimo 1000 x 600&nbsp;px | Puede producirse recorte en el lado principal y en los bordes derechos en dispositivos más altos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Horizontal" }

### Zona segura de imagen {#image-safe-zone}

Al previsualizar un mensaje dentro de la aplicación a pantalla completa en la plataforma Braze, puedes habilitar la zona segura de imagen para proteger un área del mensaje del recorte cuando se muestra en distintos dispositivos. La zona segura afecta solo a la imagen; el botón de cierre siempre es visible para los usuarios, incluso si aparece fuera de la zona segura en la vista previa.

Además de probar la zona segura de imagen en el panel de vista previa, siempre recomendamos que [pruebes tu mensaje]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message).

![Vista previa de un mensaje dentro de la aplicación en Braze con "Mostrar zona segura de imagen" habilitado. La zona segura de imagen es una superposición sobre la imagen que visualiza qué partes de la imagen estarán protegidas del recorte.]({% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %})

## Pantallas más grandes {#larger-screens}

En una tableta o un navegador de escritorio, un mensaje dentro de la aplicación a pantalla completa se ubicará en el centro de la pantalla de la aplicación, como se muestra en la siguiente captura de pantalla.

{% tabs %}
{% tab Vertical %}

![Mensaje dentro de la aplicación a pantalla completa tal como aparecería en una pantalla grande en orientación vertical. El mensaje aparece como un modal grande que se ubica en el centro de la pantalla.]({% image_buster /assets/img/full-screen-large-viewport.png %}){: style="border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Horizontal %}

![Mensaje dentro de la aplicación a pantalla completa tal como aparecería en una pantalla grande en orientación horizontal. El mensaje aparece como un modal grande que se ubica en el centro de la pantalla.]({% image_buster /assets/img/full-screen-large-viewport-landscape.png %}){: style="max-width:80%;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}