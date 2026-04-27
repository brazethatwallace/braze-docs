---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre la Biblioteca de medios
page_order: 2
page_type: FAQ
tool: Media
description: "Este artículo ofrece respuestas a las preguntas frecuentes sobre la Biblioteca de medios en Braze."

---

# Preguntas frecuentes

> Esta página ofrece respuestas a las preguntas frecuentes sobre la Biblioteca de medios en Braze.

### ¿Hay límites de almacenamiento para las imágenes en la Biblioteca de medios?

No, no hay límites de almacenamiento para los activos en la Biblioteca de medios. Sin embargo, hay límites de tamaño para los activos (máximo 5 MB).

### ¿Los activos cargados tienen fecha de vencimiento?

No, los activos cargados en la Biblioteca de medios se conservarán durante toda la duración de tu contrato con Braze.

### ¿Puedo cargar activos de video?

No, la Biblioteca de medios no admite archivos de video. Te recomendamos alojarlos externamente o en una plataforma como YouTube.

### ¿Puedo recortar todos los tipos de imágenes?

No, la Biblioteca de medios no admite el recorte de imágenes GIF.

### ¿Cómo recorto una imagen existente?

Puedes recortar una imagen existente seleccionándola en la Biblioteca de medios y haciendo clic en **Crop & Save New Image**.

![Vista previa de una imagen de la Biblioteca de medios.]({% image_buster /assets/img_archive/media_library_crop1.png %}){: height="75%" width="75%"}

Luego serás redirigido a un compositor de recorte donde puedes seleccionar el tipo de proporción y editar el nombre de la nueva imagen. Cuando selecciones **Save**, tu nueva imagen estará lista para usar.

![Ventana para recortar y guardar una imagen de la Biblioteca de medios.]({% image_buster /assets/img_archive/media_library_crop2.png %}){: height="75%" width="75%"}

### Mi imagen agota el tiempo de espera cuando intento cargarla. ¿Qué puedo hacer?

Esto puede ocurrir por diversas razones, pero una solución común es asegurarte de que tu imagen esté optimizada antes de intentar cargarla. Esto implica pasar tu imagen por un optimizador de imágenes como [ImageOptim](https://imageoptim.com/mac).

Además, si tu imagen fue creada en Photoshop (o un software similar) y tiene muchas capas, fusionar y reducir el número de capas también puede ayudar.

### Veo un "Error inesperado" al cargar una imagen aunque pesa menos de 5 MB y está en un formato compatible. ¿Qué ocurre?

Esto puede suceder por dos razones principales:

1. **Metadatos no válidos en el archivo:** El software que Braze utiliza para procesar imágenes puede rechazar archivos con metadatos no válidos o incompatibles. En algunos casos, el archivo también puede procesarse de una manera que supere el límite de 5 MB. Intenta usar una imagen diferente (por ejemplo, vuelve a exportar o guardar la imagen desde tu editor de imágenes) o una imagen de otra fuente.
2. **Caracteres especiales en el nombre del archivo:** Los nombres de archivo que contienen caracteres especiales (como `&` o `%`) pueden provocar que la carga falle. Renombra el archivo para usar solo letras, números, guiones o guiones bajos, y luego intenta cargarlo de nuevo.

### ¿Por qué no puedo cargar cualquier imagen en los compositores de push?

Esto se debe a que la mayoría de los compositores tienen restricciones en la proporción de tamaño de imagen permitida.