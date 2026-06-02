---
nav_title: Biblioteca de medios
article_title: Biblioteca de medios
page_order: 2
page_type: reference
description: "Este artículo de referencia cubre la Biblioteca de medios. Aquí puedes aprender a administrar tus activos en una única ubicación centralizada, generar imágenes con IA y acceder a los medios en tu creador de mensajes."
tool: Media

---

# Biblioteca de medios {#media-library}

> La Biblioteca de medios te permite administrar tus activos en una única ubicación centralizada.

## Biblioteca de medios frente a CDN {#media-library-versus-cdn}

Usar la Biblioteca de medios en lugar de una red de entrega de contenido (CDN) proporciona mejor almacenamiento en caché y rendimiento para los mensajes dentro de la aplicación. Todos los activos de la Biblioteca de medios que se encuentren en un mensaje dentro de la aplicación se almacenarán previamente en caché para una visualización más rápida y estarán disponibles para su visualización sin conexión. Además, la Biblioteca de medios está integrada con los compositores de Braze, lo que permite a los especialistas en marketing seleccionar o etiquetar imágenes en lugar de copiar y pegar las URL de las imágenes.

## Acceder a la Biblioteca de medios {#accessing-the-media-library}

En la Biblioteca de medios, puedes ver el tipo de activo, el tamaño, las dimensiones, la URL, la fecha en que se añadió a la biblioteca y otra información. Para acceder a tu Biblioteca de medios de Braze, ve a **Contenido** > **Biblioteca de medios**. Aquí puedes:

* Cargar varias imágenes a la vez
* Cargar archivos de contacto virtual (.vcf)
* Cargar archivos de video para usar en mensajes de WhatsApp
* Cargar una carpeta con tus imágenes (hasta 50 imágenes)
* [Generar una imagen con IA](#generate-ai) y almacenarla en la Biblioteca de medios
* Recortar una imagen existente para crear la proporción adecuada para tus mensajes
* Añadir etiquetas o equipos para organizar mejor tus imágenes
* Buscar por etiquetas o equipos en la cuadrícula de la Biblioteca de medios
* Arrastrar y soltar imágenes o carpetas para cargarlas
* Eliminar imágenes

![Página de la Biblioteca de medios que incluye una sección "Cargar a la biblioteca" para arrastrar y soltar o cargar archivos. También hay una lista del contenido cargado en la Biblioteca de medios.]({% image_buster /assets/img_archive/media_library_main.png %})

Más adelante, al redactar un mensaje en Braze, puedes incorporar tus imágenes desde la Biblioteca de medios.

![Dos formas comunes de acceder a la Biblioteca de medios según el creador de mensajes. Una muestra el editor de arrastrar y soltar de correo electrónico con el título "Imágenes y GIF" y un botón para "Añadir desde la Biblioteca de medios". La otra muestra los editores estándar, como push y mensajes dentro de la aplicación, con el título "Medios" y un botón para "Añadir imagen".]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Para obtener más ayuda con la Biblioteca de medios, consulta nuestras [Preguntas frecuentes sobre la Biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/faq/). {% endalert %}

## Especificaciones de imagen {#image-specifications}

Todas las imágenes cargadas en la Biblioteca de medios deben tener un tamaño inferior a 5&nbsp;MB. Los tipos de archivo compatibles son PNG, JPEG, GIF, SVG y WebP. Para conocer los tamaños y especificaciones de imagen recomendados por canal de mensajería, consulta [Especificaciones de imágenes]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications/).

{% alert important %}
Los GIF con formas muy alargadas (por ejemplo, 3000 x 2 píxeles) o con 300 o más fotogramas pueden fallar al cargarse, incluso si el tamaño total del archivo es pequeño.
{% endalert %}

## Generar imágenes con BrazeAI<sup>TM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Antes de usar esta característica, revisa [cómo se usan y envían tus datos a OpenAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}