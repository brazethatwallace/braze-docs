---
nav_title: Biblioteca de medios
article_title: Biblioteca de medios
page_order: 2
page_type: reference
description: "Este artículo de referencia cubre la biblioteca de medios. Aquí puedes aprender a administrar tus activos en una única ubicación centralizada, generar imágenes con IA y acceder a los medios en tu creador de mensajes."
tool: Media

---

# Biblioteca de medios {#media-library}

> La biblioteca de medios te permite administrar tus activos en una única ubicación centralizada.

## Requisitos previos {#prerequisites}

| Requisitos | Descripción |
|---|---|
| Permiso "View Media Library Assets" | Ver activos de la biblioteca de medios |
| Permiso "Edit Media Library Assets" | Crear y actualizar activos de la biblioteca de medios |
| Permiso "Delete Media Library Assets" | Eliminar activos de la biblioteca de medios de la interfaz. Los activos eliminados siguen alojados en Braze para evitar que se rompan los mensajes que los referencian. Para eliminar permanentemente un activo, contacta con soporte de Braze. |
| Permiso "Replace Media Library Assets" | Reemplazar el archivo de un activo existente de la biblioteca de medios manteniendo estables su URL e ID de activo |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permisos de la biblioteca de medios" }

Para más información, consulta [Permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

## Biblioteca de medios frente a CDN {#media-library-versus-cdn}

Usar la biblioteca de medios en lugar de una red de entrega de contenido (CDN) proporciona un mejor almacenamiento en caché y rendimiento para los mensajes dentro de la aplicación. Todos los activos de la biblioteca de medios que se encuentren en un mensaje dentro de la aplicación se almacenarán previamente en caché para una visualización más rápida y estarán disponibles para su visualización sin conexión. Además, la biblioteca de medios está integrada con los creadores de Braze, lo que permite a los especialistas en marketing seleccionar o etiquetar imágenes en lugar de copiar y pegar las URL de las imágenes.

## Acceso a la biblioteca de medios {#accessing-the-media-library}

Dentro de la biblioteca de medios, puedes ver el tipo de activo, el tamaño, las dimensiones, la URL, la fecha en que se añadió a la biblioteca y otra información. Para acceder a tu biblioteca de medios de Braze, ve a **Contenido** > **Biblioteca de medios**. Aquí puedes:

* Cargar varias imágenes a la vez
* Cargar archivos de contacto virtual (.vcf)
* Cargar archivos de video para usar en mensajes de WhatsApp
* Cargar una carpeta con tus imágenes (hasta 50 imágenes)
* [Generar una imagen usando IA](#generate-ai) y almacenarla en la biblioteca de medios
* Recortar una imagen existente para crear la proporción adecuada para tus mensajes
* Reemplazar el archivo de un activo existente manteniendo su URL estable
* Añadir etiquetas o equipos para organizar mejor tus imágenes
* Buscar por etiquetas o equipos en la cuadrícula de la biblioteca de medios
* Arrastrar y soltar imágenes o carpetas para cargarlas
* Eliminar imágenes

![Página de la biblioteca de medios que incluye una sección "Cargar a la biblioteca" para arrastrar y soltar o cargar archivos. También hay una lista del contenido cargado en la biblioteca de medios.]({% image_buster /assets/img_archive/media_library_main.png %})

Más adelante, al redactar un mensaje en Braze, puedes incorporar tus imágenes desde la biblioteca de medios.

![Dos formas comunes de acceder a la biblioteca de medios según el creador de mensajes. Una muestra el editor de arrastrar y soltar de correo electrónico con el título "Imágenes y GIF" y un botón para "Añadir desde la biblioteca de medios". La otra muestra los editores estándar, como push y mensajes dentro de la aplicación, con el título "Medios" y un botón para "Añadir imagen".]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Para obtener más ayuda con la biblioteca de medios, consulta nuestras [Preguntas frecuentes sobre la biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/faq). {% endalert %}

## Carga de archivos ZIP {#zip-file-uploads}

Cuando cargas un archivo ZIP en la biblioteca de medios, todos los archivos deben estar en la raíz de la carpeta ZIP; no incluyas subdirectorios.

Esto se aplica a todos los archivos del archivo comprimido, incluidos los archivos de fuentes (`.ttf`, `.woff`, `.otf`, `.woff2`), HTML, CSS, JavaScript e imágenes. Coloca cada archivo en la raíz del ZIP junto con los demás.

Como alternativa, carga los activos individualmente en la biblioteca de medios sin comprimirlos.

## Reemplazar un archivo {#replace-a-file}

Puedes reemplazar el archivo de un activo existente en la biblioteca de medios manteniendo estables su URL y su ID de activo. Dado que la URL no cambia, cualquier mensaje o Campaign que haga referencia a ese activo, incluidos los correos electrónicos ya enviados, reflejará automáticamente el archivo actualizado. Esto es útil cuando deseas actualizar un activo compartido (como un logotipo) en un solo lugar en lugar de actualizar cada Campaign individualmente.

Para reemplazar un activo, debes tener el permiso "Replace Media Library Assets":

1. Ve a **Contenido** > **Biblioteca de medios**.
2. Selecciona el activo que deseas reemplazar.
3. En el modal, selecciona **Reemplazar archivo**.
4. Carga el archivo de reemplazo.

![Modal de edición de la biblioteca de medios que muestra los botones Reemplazar archivo, Recortar imagen y Eliminar para un activo.]({% image_buster /assets/img_archive/media_library_replace_file.png %}){: style="max-width:60%;border:none"}

### Requisitos y limitaciones {#requirements-and-limitations}

- El archivo de reemplazo debe tener la misma extensión de archivo que el original. Por ejemplo, no puedes reemplazar un activo `.png` con un archivo `.jpg`.
- Los activos de video no se pueden reemplazar.
- Después del reemplazo, el archivo actualizado puede tardar un tiempo en mostrarse para todos los consumidores debido al almacenamiento en caché del CDN.

### Canales con copias de imagen procesadas {#channels-with-processed-image-copies}

Algunos canales crean una copia optimizada de la imagen cuando se configura el mensaje, lo que genera una URL independiente. Reemplazar el activo original de la biblioteca de medios no actualiza lo que los consumidores ven en los mensajes creados con esos canales, incluidos los mensajes dentro de la aplicación, Content Cards, notificaciones push y banners.

También puedes reemplazar un activo de forma programática utilizando el endpoint [`PUT /media_library/replace_file`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/replace_file).

## Especificaciones de imágenes {#image-specifications}

Todas las imágenes cargadas en la biblioteca de medios deben tener un tamaño inferior a 5&nbsp;MB. Los tipos de archivo compatibles son PNG, JPEG, GIF, SVG y WebP. Para conocer los tamaños y especificaciones de imagen recomendados por canal de mensajería, consulta [Especificaciones de imágenes]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications).

{% alert important %}
Los GIF con formas muy alargadas (por ejemplo, 3000 x 2 píxeles) o con 300 o más fotogramas pueden fallar al cargarse, incluso si el tamaño total del archivo es pequeño.
{% endalert %}

## Generar imágenes con BrazeAI<sup>TM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Antes de usar esta característica, revisa [cómo se usan y envían tus datos a OpenAI]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#data-privacy-and-security).
{% endalert %}

Si no ves **AI Image Generator** en la página de la **Biblioteca de medios**, confirma que tienes el permiso **Edit Media Library Assets**. Si la opción sigue sin aparecer, ponte en contacto con tu equipo de Braze para confirmar que tu espacio de trabajo tiene acceso a la generación de imágenes de BrazeAI. Si la generación falla, revisa la [política de contenido de OpenAI]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#data-privacy-and-security).