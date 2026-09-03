---
nav_title: Detalles creativos
article_title: Detalles creativos para Content Cards
page_order: 2
description: "Este artículo cubre detalles creativos como recomendaciones de tamaño de imagen y comportamiento de descarte en los tres tipos estándar de Content Cards."
channel:
  - content cards
tool: Media

---

# Detalles creativos para Content Cards {#creative-details-for-content-cards}

> La personalización de las Content Cards y la fuente en la que se encuentran no se puede realizar durante el proceso de creación de la Campaign; debes trabajar con tus ingenieros y desarrolladores para construir y personalizar tus tarjetas. Para detalles técnicos, visita nuestra [documentación para desarrolladores]({{site.baseurl}}/developer_guide/getting_started/customization_overview).

## Tipos de Content Cards {#content-card-types}

{% tabs %}
{% tab Clásica %}

La tarjeta clásica es ideal para mensajes y notificaciones estándar, o incluso para categorizar visualmente los mensajes con iconos. La imagen es opcional, pero debe tener una proporción de 1:1.

![Imagen de una tarjeta clásica con detalles recomendados y un ejemplo de tarjeta clásica]({% image_buster /assets/img/content_card_classic.png %}){: width="1358" height="2871" style="max-width:45%;border:0;"}

| Capacidad de la tarjeta | Detalles |
| --- | ---|
| Texto del encabezado | 18 px; Negrita <br> Lo ideal es una línea de texto. <br> Puedes usar Liquid aquí para personalizar tu mensaje. |
| Texto del mensaje | 13 px; Peso normal <br> Lo ideal son de dos a cuatro líneas de texto. <br> Puedes usar Liquid aquí para personalizar tu mensaje. |
| Texto del enlace | Opcional. <br> 13&nbsp;px <br> Enlace a una página web o vínculo profundo dentro de tu aplicación. |
| Imagen | Opcional. <br> Debe tener una proporción de 1:1. <br> Recomendamos una calidad de imagen de 60 x 60&nbsp;px. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de Content Cards" }

{% endtab %}
{% tab Imagen con subtítulo %}

La tarjeta de imagen con subtítulo es una excelente forma de destacar y llamar la atención sobre contenido importante, como una gran oferta o una nueva característica de la aplicación.

![Imagen de una tarjeta de imagen con subtítulo con detalles recomendados y un ejemplo de tarjeta de imagen con subtítulo]({% image_buster /assets/img/content_card_captioned.png %}){: width="2880" height="2877" style="max-width:90%;border:0;"}

| Capacidad de la tarjeta | Detalles |
| --- | ---|
| Texto del encabezado | 18 px; Negrita <br> Lo ideal es una línea de texto. <br> Puedes usar Liquid aquí para personalizar tu mensaje. |
| Texto del mensaje | 13 px; Peso normal <br> Lo ideal son de dos a cuatro líneas de texto. <br> Puedes usar Liquid aquí para personalizar tu mensaje. |
| Texto del enlace | Opcional. <br> 13&nbsp;px <br> Enlace a una página web o vínculo profundo dentro de tu aplicación. |
| Imagen | Se sugiere una proporción de 4:3. <br> 600&nbsp;px de ancho mínimo.  <br> Compatible con PNG, JPEG y GIF de alta resolución. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de Content Cards" }

{% endtab %}
{% tab Solo imagen %}

Si quieres más control creativo, la tarjeta de solo imagen es para ti. Crea tu imagen con cualquier herramienta que prefieras y súbela a este tipo de tarjeta.

![Imagen de una Content Card de solo imagen con detalles recomendados y un ejemplo de solo imagen]({% image_buster /assets/img/content_card_banner.png %}){: width="1358" height="2871" style="max-width:45%;border:0;"}

| Capacidad de la tarjeta | Detalles |
| --- | ---|
| Tarjeta con enlace | Opcional. <br> 13&nbsp;px <br> Al hacer clic, enlaza a una página web o un vínculo profundo dentro de tu aplicación. |
| Imagen | Compatible con cualquier proporción de aspecto. <br> 600&nbsp;px de ancho mínimo.  <br> Compatible con PNG, JPEG y GIF de alta resolución. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de Content Cards" }

{% endtab %}
{% endtabs %}

## Detalles creativos generales {#general}

Content Cards admite texto e imágenes, incluidos GIF, de forma nativa. Actualmente, el estilo personalizado para la tarjeta, como diferentes colores de fuente o múltiples imágenes, no se puede configurar en el panel. Puedes aplicar estilo personalizado a tu Content Card y fuente durante la integración. Para más detalles, consulta [Personalizar tarjetas]({{site.baseurl}}/developer_guide/content_cards/customizing_cards) del SDK de Braze.

### Comportamiento de descarte {#dismissal-behavior}

Para que un usuario descarte una tarjeta, puede deslizarla en el móvil o usar la función de `close X`, como se muestra en la siguiente captura de pantalla. La `x` aparecerá al pasar el cursor solo en el SDK Web.

![Imagen que muestra los comportamientos de descarte por deslizamiento o cierre de una tarjeta]({% image_buster /assets/img/dismissal-cc.png %}){: width="1800" height="504"}

Si un usuario ha descartado todas sus tarjetas o no has enviado nuevas actualizaciones, la fuente del usuario normalmente se verá así:

![Imagen de una fuente de Content Cards vacía]({% image_buster /assets/img/empty-cc.png %}){: width="832" height="1478" style="max-width:45%"}

{% alert tip %}
Mantén las Content Cards relevantes configurándolas para que se descarten cuando un usuario realice acciones relevantes. Por ejemplo, configura las Content Cards promocionales para que se descarten tan pronto como los usuarios realicen una compra, de modo que no sigan viendo una oferta de algo que ya compraron.
{% endalert %}

### Uso de GIF en Content Cards {#using-gifs-in-content-cards}

| Content Cards para Android | Content Cards para iOS | Content Cards para Web |
| --- | --- |---|
| El SDK de Android no proporciona compatibilidad con GIF animados de forma predeterminada. Para más detalles sobre cómo activar la compatibilidad con GIF, consulta [GIF]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs?sdktab=android). | El SDK de Swift no proporciona compatibilidad con GIF animados de forma predeterminada. Para más detalles sobre cómo activar la compatibilidad con GIF, consulta el [tutorial de compatibilidad con GIF](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support). | La compatibilidad con GIF está incluida de forma predeterminada en la integración del SDK Web. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Uso de GIF en Content Cards" }