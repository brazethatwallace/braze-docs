---
nav_title: "Historias push"
article_title: "Historias push"
page_order: 2
page_type: reference
description: "Este artículo de referencia cubre qué son las historias push, cómo crear una, así como algunas preguntas frecuentes."
channel:
  - push

---

# Historias push {#push-stories}

> Las historias push toman la funcionalidad de carrusel de fotos popularizada en Instagram y Facebook y permiten a los especialistas en marketing crear un carrusel de páginas dentro de una notificación push que cuenta una historia rica y coherente. Estas páginas consisten en una imagen, una acción de clic, un título y una descripción. Tus usuarios pueden deslizar por estas páginas y ver la historia, tal como tú la cuentas.

| Ejemplo de Android (expandido) | Ejemplo de iOS (expandido) |
| :-----: | :----------: |
| ![Vista previa de historias push en Android.]({% image_buster /assets/img_archive/pushstories_android_preview.png %}) | ![Vista previa de historias push en iOS]({% image_buster /assets/img_archive/pushstories_ios_preview.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Historias push" }

{% alert note %}
En las versiones 3.13.0+ del SDK de iOS, debido a un cambio en la forma en que el SDK descarga las imágenes, no se mostrará una miniatura de la primera imagen en la vista condensada de la notificación push. Asegúrate de que el texto de tu mensaje invite a los usuarios a expandir la notificación push para ver las imágenes.
{% endalert %}

## Requisitos previos {#prerequisites}

Se requieren las siguientes versiones del SDK para recibir historias push:

{% sdk_min_versions swift:5.0.0 android:2.2.0 %}


## Cómo usar las historias push {#how-to-use-push-stories}

![Menú desplegable del compositor de historias push]({% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Para usar las historias push, haz lo siguiente:

1. Crea una [campaña push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/).
2. Para tu **Notification Type**, selecciona **Push Stories**.
3. Selecciona **iOS** o **Android**. Ten en cuenta que si seleccionas ambos para un mensaje push, la opción de crear una historia push no aparecerá.

### Compositor de historias push {#push-story-composer}

Para crear una página, realiza los siguientes pasos:

1. Selecciona **Add new page** desde el compositor principal.
2. Inserta una imagen para cada página, junto con el comportamiento de clic para esa imagen.
3. Si lo deseas, añade un **Title** y una **Description** para cada página. Si usas un título y una descripción para una página, deben insertarse para todas las páginas.

Las vistas previas se reflejarán y son interactivas.

![Compositor de historias push]({% image_buster /assets/img_archive/pushstories_composer.png %}){: style="max-width:60%"}

{% alert important %}
Si estás extrayendo imágenes con [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/#about-connected-content), asegúrate de que la URL de tu imagen comience con `https://`. Usar `http://` hará que tu aplicación se bloquee.
{% endalert %}

### Especificaciones de imagen y texto {#image-and-text-specifications}

Las siguientes especificaciones de imagen y texto se aplican a la parte del carrusel de fotos de las historias push. Para obtener información sobre la notificación push básica con la que los usuarios interactúan para activar la historia push, consulta [Formatos de mensajes push e imágenes]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/).

{% tabs %}
{% tab Imágenes %}

- **Relación de imagen:** 2:1 (obligatoria)
- **Tamaño de imagen recomendado:** 500 KB
- **Tamaño máximo de imagen:** 5 MB
- **Tipos de archivo:** PNG, JPEG

{% endtab %}
{% tab Texto %}

- **Título:** 30 caracteres (recomendado)
- **Descripción:** 30 caracteres (recomendado)

{% alert note %}
Aunque puede haber cierta variación en la longitud de caracteres de un dispositivo a otro, el título y la descripción de las historias push están limitados a una línea cada uno. El resto de tu mensaje se truncará. Siempre prueba tu mensaje en un dispositivo real.
{% endalert %}

{% endtab %}
{% endtabs %}

### Segmentación de historias push {#push-story-segmentation}

Cuando creas una campaña o Canvas, puedes filtrar qué usuarios deseas segmentar en función de si han hecho clic en una página de historia push. Luego, selecciona la campaña y la página que deseas usar para segmentar a tus usuarios.

### Análisis de historias push {#push-stories-analytics}

Los análisis se verán muy similares a la sección de análisis actual para notificaciones push. Para los análisis de historias push, puedes abrir la métrica **Direct Opens** para ver los clics por página.

![Tabla de rendimiento push de iOS con análisis de ejemplo y detalles expandidos para la métrica Direct Opens.]({% image_buster /assets/img_archive/pushstories_analytics.png %})

## Solución de problemas {#troubleshooting}

### iOS

#### Me envié una historia push pero no recibí la notificación {#i-sent-myself-a-push-story-but-didnt-receive-the-notification}

Apple tiene reglas específicas que impiden que ciertos tipos de notificaciones se envíen a un dispositivo en función de varios factores diferentes. Esto incluye la evaluación del plan de datos del cliente, el tamaño de la notificación y la capacidad de almacenamiento del cliente. Como resultado, a veces no se enviará ninguna notificación a tus clientes.

Estas son limitaciones impuestas por Apple que deben considerarse al diseñar tu historia push.

#### Me envié una historia push pero vi la vista condensada en su lugar {#i-sent-myself-a-push-story-but-saw-the-condensed-view-instead}

En ciertas situaciones en las que no se cargan todas las páginas, por ejemplo, debido a una pérdida de conexión de datos, la historia push solo mostrará la notificación condensada.

### Android

#### La historia push no se descarta después de hacer clic en la imagen {#push-story-doesnt-dismiss-after-clicking-the-image}

De forma predeterminada, las historias push no se descartan en Android después de que un usuario hace clic en la imagen. Si deseas descartar la notificación, llama a [`cancelNotification`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/index.html#-1466259649%2FFunctions%2F-1725759721).