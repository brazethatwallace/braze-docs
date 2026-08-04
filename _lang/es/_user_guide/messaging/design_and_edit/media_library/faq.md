---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre la Biblioteca de medios
page_order: 2
page_type: FAQ
tool: Media
description: "Este artículo ofrece respuestas a las preguntas frecuentes sobre la biblioteca de medios en Braze."

---

# Preguntas frecuentes {#frequently-asked-questions}

> Esta página ofrece respuestas a las preguntas frecuentes sobre la biblioteca de medios en Braze.

## General {#general}

### ¿Existen límites de almacenamiento para las imágenes en la biblioteca de medios? {#are-there-storage-limits-for-images-within-the-media-library}

No, no hay límites de almacenamiento para los activos en la biblioteca de medios. Sin embargo, existen límites de tamaño para los activos (máximo 5 MB).

### ¿Los activos subidos tienen fecha de caducidad? {#are-there-expiration-dates-for-uploaded-assets}

No, los activos subidos a la biblioteca de medios se conservarán durante toda la duración de tu contrato con Braze.

### ¿Puedo subir activos de video? {#can-i-upload-video-assets}

No, la biblioteca de medios no admite archivos de video. Te recomendamos alojarlos externamente o en una plataforma como YouTube.

### ¿Puedo recortar todos los tipos de imagen? {#can-i-crop-all-image-types}

No, la biblioteca de medios no admite el recorte de imágenes GIF.

### ¿Cómo copio la URL de una imagen subida a la biblioteca de medios? {#how-do-i-copy-the-url-of-an-image-uploaded-to-the-media-library}

Para copiar la URL de una imagen subida a la biblioteca de medios, ve a **Contenido** > **Biblioteca de medios**. Pasa el cursor sobre la imagen que deseas referenciar y selecciona el icono **Copiar URL de imagen** para copiar la URL de la imagen a tu portapapeles.

### ¿Puedo usar imágenes SVG en correo electrónico? {#can-i-use-svg-images-in-email}

No se recomiendan las imágenes SVG para correo electrónico debido a la compatibilidad limitada entre los clientes de correo electrónico. Gmail y varios otros proveedores de correo electrónico importantes no renderizan imágenes SVG, lo que puede resultar en imágenes rotas o faltantes para los destinatarios. Para una renderización fiable del correo electrónico, usa los formatos PNG, JPEG o GIF en su lugar.

### ¿Cómo recorto una imagen existente? {#how-do-i-crop-an-existing-image}

Puedes recortar una imagen existente seleccionándola en la biblioteca de medios y haciendo clic en **Recortar y guardar nueva imagen**.

![Vista previa de una imagen de la biblioteca de medios.]({% image_buster /assets/img_archive/media_library_crop1.png %}){: height="75%" width="75%"}

Serás redirigido a un creador de recorte donde puedes seleccionar el tipo de proporción y editar el nombre de la nueva imagen. Cuando selecciones **Guardar**, tu nueva imagen estará lista para usarse.

![Ventana para recortar y guardar una imagen de la biblioteca de medios.]({% image_buster /assets/img_archive/media_library_crop2.png %}){: height="75%" width="75%"}

### Mi imagen sigue agotando el tiempo de espera cuando intento subirla. ¿Qué puedo hacer al respecto? {#my-image-keeps-timing-out-when-i-try-to-upload-it-what-can-i-do-about-this}

Esto puede ocurrir por diversas razones, pero una solución común es asegurarte de que tu imagen esté optimizada antes de intentar subirla. Esto significa pasar tu imagen por un optimizador de imágenes como [ImageOptim](https://imageoptim.com/mac).

Además, si tu imagen fue creada en Photoshop (o un software similar) y tiene muchas capas, combinar y reducir el número de capas también puede ayudar.

### Veo un "Error inesperado" al subir una imagen aunque pesa menos de 5 MB y está en un formato compatible. ¿Qué ocurre? {#i-see-an-unexpected-error-when-uploading-an-image-even-though-its-under-5-mb-and-in-a-supported-format-whats-wrong}

Esto puede suceder por dos razones principales:

1. **Metadatos no válidos en el archivo:** El software que Braze utiliza para procesar imágenes puede rechazar archivos con metadatos no válidos o incompatibles. En algunos casos, el archivo también puede procesarse de una manera que supere el límite de 5 MB. Intenta usar una imagen diferente (por ejemplo, vuelve a exportar o guardar la imagen desde tu editor de imágenes) o una imagen de otra fuente.
2. **Caracteres especiales en el nombre del archivo:** Los nombres de archivo que contienen caracteres especiales (como `&` o `%`) pueden provocar que la subida falle. Renombra el archivo para usar solo letras, números, guiones o guiones bajos, y luego intenta subirlo de nuevo.

### ¿Por qué no puedo subir cualquier imagen que quiera en los creadores de push? {#why-cant-i-upload-any-image-i-want-into-the-push-composers}

Esto se debe a que la mayoría de los creadores tienen restricciones en la proporción de tamaño de imagen permitida.

### Generar una imagen usando IA {#generate-an-image-using-ai}

Puedes generar imágenes desde **Contenido** > **Biblioteca de medios** seleccionando **Generador de imágenes con IA**. Necesitas el permiso **Editar activos de la biblioteca de medios**. Si no ves la opción, contacta a tu equipo de clientes de Braze. Para conocer los pasos y los detalles de la política, consulta [Generar imágenes con BrazeAI]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-images) y [Generación de imágenes con BrazeAI]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#generate-ai).

### ¿Puedo crear URLs personalizadas para los activos de imagen de la biblioteca de medios? {#can-i-create-vanity-urls-for-media-library-image-assets}

Las URLs personalizadas para los activos de la biblioteca de medios no son compatibles porque las URLs personalizadas interrumpirían la entrega del CDN. Puedes reemplazar una imagen en su URL existente cuando las Campaigns ya hacen referencia a esa URL. Para más información, consulta [Reemplazar un archivo]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#replace-a-file).

### ¿Por qué Chrome guarda las imágenes JPEG o PNG como archivos WebP? {#why-does-chrome-save-jpeg-or-png-images-as-webp-files}

Cuando usas Chrome para guardar imágenes de la biblioteca de medios, el navegador puede convertir automáticamente los archivos JPEG o PNG al formato WebP. Este es el comportamiento predeterminado de Chrome para la descarga de imágenes y no es específico de Braze. Si necesitas guardar las imágenes en su formato original, intenta usar un navegador diferente como Safari o Firefox.