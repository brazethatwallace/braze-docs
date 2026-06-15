---
nav_title: Deslizamiento hacia arriba
article_title: Mensajes dentro de la aplicación de deslizamiento hacia arriba
page_order: 3
channel:
  - in-app messages
tool:
  - Media
description: "Este artículo de referencia cubre los requisitos de mensaje y diseño de los mensajes dentro de la aplicación de deslizamiento hacia arriba."

---

# Mensajes dentro de la aplicación de deslizamiento hacia arriba {#slideup-in-app-messages}

> Nuestros deslizamientos hacia arriba suelen aparecer en la parte superior o inferior de la pantalla de la aplicación (puedes configurar esto cuando creas tu mensaje). Son ideales para alertar a tus usuarios sobre nuevos términos de servicio, cookies y otros fragmentos de información. No son intrusivos y permiten que tus usuarios sigan interactuando con tu aplicación mientras se muestra el mensaje.

Este tipo de mensaje está disponible en el [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/).

![Dos mensajes dentro de la aplicación de deslizamiento hacia arriba, uno apareciendo desde la parte superior de la pantalla y el otro desde la parte inferior, detallando las recomendaciones de imagen y texto. Consulta las siguientes secciones para más detalles.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width: 40%; border: none;"}

## Comportamiento de imagen y texto {#image-and-copy-behavior}

Los mensajes de deslizamiento hacia arriba pueden contener hasta tres líneas de texto antes de truncarse con puntos suspensivos. Las imágenes en los deslizamientos hacia arriba nunca se recortarán ni se cortarán; siempre se reducirán para ajustarse dentro del contenedor de imagen de 50 x 50 píxeles.

- Todas las imágenes deben pesar menos de 5&nbsp;MB.
- Solo aceptamos archivos de tipo PNG, JPEG y GIF.
- Recomendamos que tus imágenes pesen 500&nbsp;KB.

{% alert tip %} ¡Crea activos con confianza! Nuestras plantillas de imágenes para mensajes dentro de la aplicación y las superposiciones de zona segura están diseñadas para funcionar correctamente con dispositivos de todos los tamaños. [Descargar ZIP de plantillas de diseño]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

| Diseño | Tamaño del activo | Notas |
|--- | --- | --- |
| Imagen + texto | Relación de aspecto 1:1<br>Alta resolución 150 x 150&nbsp;px<br> Mínimo 50 x 50&nbsp;px | Las imágenes de diversas relaciones de aspecto se ajustarán a un contenedor de imagen cuadrado, sin recorte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comportamiento de imagen y texto" }

Siempre debes [previsualizar y probar tus mensajes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=in-app%20message) en una variedad de dispositivos para asegurarte de que las áreas más importantes de tu imagen y mensaje aparezcan como se espera. Ten en cuenta que al previsualizar tu mensaje en el compositor, la representación real en los dispositivos puede diferir.

## Hipervínculos y texto de anclaje {#hyperlinks-and-anchor-text}

Para añadir un enlace en un deslizamiento hacia arriba, introduce el texto del mensaje en el campo **Cuerpo** y configura el destino en **Comportamiento de clic** (por ejemplo, **Redirigir a URL**). Cuando se configura el **Comportamiento de clic**, tocar en cualquier parte del mensaje excepto el control de cerrar desencadena esa acción.

Para mensajes dentro de la aplicación con HTML personalizado, puedes usar enlaces HTML directamente. Consulta [Mensajes dentro de la aplicación con HTML personalizado]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html/).

## Dispositivos móviles {#mobile-devices}

En dispositivos móviles, los deslizamientos hacia arriba aparecen en la parte superior o inferior de la pantalla de la aplicación. Puedes especificar esto cuando creas tu mensaje. Los usuarios pueden deslizar para descartar el deslizamiento hacia arriba, o tocar para abrirlo si se incluye una acción de clic. Si se añade una acción de clic al deslizamiento hacia arriba, se muestra un chevrón ">".

## Pantallas más grandes {#larger-screens}

{% tabs %}
{% tab Escritorio %}

En un navegador de escritorio, un mensaje dentro de la aplicación de deslizamiento hacia arriba se ubicará en la esquina de la pantalla como se muestra en la siguiente captura de pantalla (a menos que se designe de otra manera al crear el mensaje dentro de la aplicación). Los usuarios pueden hacer clic en el botón de cerrar "X" para descartar el deslizamiento hacia arriba.

![Mensaje dentro de la aplicación de deslizamiento hacia arriba tal como aparece en un navegador de escritorio. El mensaje aparece en la esquina inferior derecha de la pantalla y no ocupa todo el ancho de la pantalla.]({% image_buster /assets/img/slideup-large-viewport.png %}){: style="border: none;"}

{% endtab %}
{% tab Tableta %}

En una tableta, un mensaje dentro de la aplicación de deslizamiento hacia arriba aparece en la parte inferior de la pantalla. De manera similar a los dispositivos móviles, los usuarios pueden deslizar para descartar el deslizamiento hacia arriba, o tocar para abrirlo si se incluye una acción de clic. Si se añade una acción de clic al deslizamiento hacia arriba, se muestra un chevrón ">". El botón de cerrar "X" no se muestra de forma predeterminada.

![Mensaje dentro de la aplicación de deslizamiento hacia arriba tal como aparece en la pantalla de una tableta. El mensaje aparece en la parte inferior central de la pantalla y no ocupa todo el ancho de la pantalla.]({% image_buster /assets/img/slideup-tablet.png %}){: style="border: none;"}

{% endtab %}
{% endtabs %}