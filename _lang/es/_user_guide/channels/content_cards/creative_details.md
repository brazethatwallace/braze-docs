---
nav_title: Detalles creativos
article_title: Detalles creativos para tarjetas de contenido
page_order: 2
description: "Este artículo cubre detalles creativos como recomendaciones de tamaño de imagen y comportamiento de descarte en los tres tipos estándar de tarjetas de contenido."
channel:
  - content cards
tool: Media

---

# Detalles creativos para tarjetas de contenido

> La personalización de las tarjetas de contenido y la fuente en la que se encuentran no se puede realizar durante el proceso de creación de la campaña; debes trabajar con tus ingenieros y desarrolladores para construir y personalizar tus tarjetas. Para detalles técnicos, visita nuestra [documentación para desarrolladores]({{site.baseurl}}/developer_guide/getting_started/customization_overview).

## Tipos de tarjetas de contenido

{% tabs %}
{% tab Classic %}

La tarjeta clásica es ideal para mensajería y notificaciones estándar, o incluso para categorizar visualmente los mensajes con iconos. La imagen es opcional, pero debe tener una proporción de 1:1.

![Imagen de una tarjeta clásica con detalles recomendados y un ejemplo de tarjeta clásica]({% image_buster /assets/img/content_card_classic.png %}){: style="max-width:45%;border:0;"}

| Capacidad de la tarjeta | Detalles |
| --- | ---|
| Texto del encabezado | 18px; Negrita <br> Una línea de texto es lo ideal. <br> Puedes usar Liquid aquí para personalizar tu mensaje. |
| Texto del mensaje | 13px; Peso regular <br> De dos a cuatro líneas de texto es lo ideal. <br> Puedes usar Liquid aquí para personalizar tu mensaje. |
| Texto del enlace | Opcional. <br> 13&nbsp;px <br> Enlace a una página web o vínculo profundo dentro de tu aplicación. |
| Imagen | Opcional. <br> Debe tener proporción 1:1. <br> Recomendamos una calidad de imagen de 60 x 60&nbsp;px. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Captioned Image %}

La tarjeta de imagen con subtítulo es una excelente manera de mostrar y atraer la atención hacia contenido importante, como una gran oferta o una nueva característica de la aplicación.

![Imagen de una tarjeta de imagen con subtítulo con detalles recomendados y un ejemplo de tarjeta de imagen con subtítulo]({% image_buster /assets/img/content_card_captioned.png %}){: style="max-width:90%;border:0;"}

| Capacidad de la tarjeta | Detalles |
| --- | ---|
| Texto del encabezado | 18px; Negrita <br> Una línea de texto es lo ideal. <br> Puedes usar Liquid aquí para personalizar tu mensaje. |
| Texto del mensaje | 13px; Peso regular <br> De dos a cuatro líneas de texto es lo ideal. <br> Puedes usar Liquid aquí para personalizar tu mensaje. |
| Texto del enlace | Opcional. <br> 13&nbsp;px <br> Enlace a una página web o vínculo profundo dentro de tu aplicación. |
| Imagen | Se sugiere una proporción de 4:3. <br> 600&nbsp;px de ancho mínimo.  <br> Compatible con PNG, JPEG y GIF de alta resolución. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Image-only %}

Si quieres más control creativo, la tarjeta de solo imagen es para ti. Crea tu imagen usando cualquier herramienta que prefieras y cárgala en este tipo de tarjeta.

![Imagen de una tarjeta de contenido de solo imagen con detalles recomendados y un ejemplo de solo imagen]({% image_buster /assets/img/content_card_banner.png %}){: style="max-width:45%;border:0;"}

| Capacidad de la tarjeta | Detalles |
| --- | ---|
| Tarjeta con enlace | Opcional. <br> 13&nbsp;px <br> Comportamiento al hacer clic: enlace a una página web o vínculo profundo dentro de tu aplicación. |
| Imagen | Cualquier proporción es compatible. <br> 600&nbsp;px de ancho mínimo.  <br> Compatible con PNG, JPEG y GIF de alta resolución. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Detalles creativos generales {#general}

Las tarjetas de contenido admiten texto e imágenes, incluidos GIF, de forma predeterminada. Actualmente, el estilo personalizado para la tarjeta, como diferentes colores de fuente o múltiples imágenes, no se puede realizar en el dashboard. Puedes aplicar estilo personalizado a tu tarjeta de contenido y fuente durante la integración. Para más detalles, consulta [Personalizar tarjetas]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/) del SDK de Braze.

### Comportamiento de descarte

Para que un usuario descarte una tarjeta, puede deslizarla en el móvil o usar la función de `cerrar X`, como se muestra en la siguiente captura de pantalla. La `x` aparecerá al pasar el cursor solo en el SDK Web.

![Imagen que muestra los comportamientos de descarte por deslizamiento o cierre de una tarjeta]({% image_buster /assets/img/dismissal-cc.png %})

Si un usuario ha descartado todas sus tarjetas o no has enviado nuevas actualizaciones, la fuente del usuario normalmente se verá así:

![Imagen de una fuente de tarjetas de contenido vacía]({% image_buster /assets/img/empty-cc.png %}){: style="max-width:45%"}

{% alert tip %}
Mantén las tarjetas de contenido relevantes configurándolas para que se descarten cuando un usuario realice acciones relevantes. Por ejemplo, configura las tarjetas de contenido promocionales para que se descarten tan pronto como los usuarios realicen una compra, de modo que no sigan viendo una oferta de algo que ya compraron.
{% endalert %}

### Uso de GIF en tarjetas de contenido

| Tarjetas de contenido para Android | Tarjetas de contenido para iOS | Tarjetas de contenido para Web |
| --- | --- |---|
| El SDK de Android no proporciona compatibilidad con GIF animados de forma predeterminada. Para más detalles sobre cómo activar la compatibilidad con GIF, consulta [GIF]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs/?sdktab=android). | El SDK SWIFT no proporciona compatibilidad con GIF animados de forma predeterminada. Para más detalles sobre cómo activar la compatibilidad con GIF, consulta el [tutorial de compatibilidad con GIF](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support). | La compatibilidad con GIF está incluida de forma predeterminada en la integración del SDK Web. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }