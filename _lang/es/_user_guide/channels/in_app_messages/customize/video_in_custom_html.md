---
nav_title: "Video en HTML personalizado"
article_title: "Video en HTML personalizado"
page_order: 4
page_type: reference
description: "Este artículo describe cómo incrustar videos en tus mensajes dentro de la aplicación HTML."
channel:
  - in-app messages
---

# Video en mensajes dentro de la aplicación HTML personalizados {#video}

> Este artículo aplica a los [mensajes HTML personalizados]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html/) en el [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/).

## Incrustar videos {#embed-videos}

Para reproducir un video en un mensaje dentro de la aplicación HTML, incluye el siguiente elemento `<video>` en tu HTML y reemplaza los nombres de video con el nombre de tu archivo (o la URL del activo remoto). Puedes encontrar otras opciones posibles de `<video>` en [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video).

```html
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Your device does not support playing this video.
</video>
```

Para usar un activo de video local, asegúrate de incluir este archivo al cargar activos a tu campaña.

{% alert note %}
El contenido de video solo está disponible cuando el dispositivo tiene una velocidad de red razonable, a menos que el video se obtenga localmente desde el dispositivo.
{% endalert %}

## Consideraciones para Android {#android-considerations}

Para incrustar video y otro contenido HTML5 en mensajes dentro de la aplicación HTML en Android, se requiere que la aceleración por hardware esté habilitada en la Activity donde se muestra el mensaje dentro de la aplicación. Para más información, consulta la [guía para desarrolladores de Android]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/#android_embedding-youtube-content).

**Reproducción automática**: Incluso con la aceleración por hardware habilitada, los WebViews de Android pueden requerir un gesto del usuario para iniciar la reproducción de medios. Si necesitas reproducción automática, configura el WebView utilizado para renderizar mensajes dentro de la aplicación HTML para desactivar el requisito de gesto del usuario estableciendo [`WebSettings.setMediaPlaybackRequiresUserGesture(false)`](https://developer.android.com/reference/android/webkit/WebSettings#setMediaPlaybackRequiresUserGesture(boolean)). Esto requiere personalización a nivel de SDK de cómo se muestran los mensajes dentro de la aplicación HTML. Para orientación sobre la configuración, consulta [Personalizar mensajes dentro de la aplicación para el SDK de Braze]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android).

## Consideraciones para iOS {#ios-considerations}

Para dar soporte a dispositivos iOS:

- Debes incluir el atributo `playsinline` porque la reproducción a pantalla completa no es compatible.
- **La reproducción automática no está garantizada en iOS**. El comportamiento de reproducción en iOS depende de `WKWebView` y las políticas de medios a nivel del sistema operativo, y puede requerir un gesto del usuario incluso cuando `autoplay` y `muted` están configurados. Prueba tu mensaje dentro de la aplicación HTML en tus versiones y dispositivos iOS objetivo.

Si la reproducción automática es necesaria y tus pruebas muestran que no funciona de forma predeterminada, puedes personalizar la `WKWebViewConfiguration` utilizada por los mensajes dentro de la aplicación HTML para ajustar el requisito de acción del usuario para la reproducción de medios, por ejemplo, estableciendo la propiedad `mediaTypesRequiringUserActionForPlayback`. Esto requiere personalización a nivel de SDK. Para recursos de Swift, consulta [Personalizar mensajes dentro de la aplicación para el SDK de Braze]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift) y [Agregar la interfaz JavaScript de Braze a WebViews para Swift]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/?sdktab=swift).

## Consideraciones para Web {#web-considerations}

La mayoría de los navegadores modernos permiten la reproducción automática solo bajo ciertas condiciones (comúnmente cuando el video está silenciado). Si usas `autoplay` en un mensaje dentro de la aplicación web, incluye `muted` y prueba en tus navegadores y dispositivos compatibles, ya que las políticas de los navegadores varían y pueden requerir un gesto del usuario en algunos casos.

Para reproducir automáticamente videos de YouTube en un mensaje dentro de la aplicación web, agrega el parámetro de URL `&autoplay=1`. Por ejemplo, el siguiente video se reproducirá automáticamente, estará silenciado (`&mute=1`) y no mostrará controles (`&controls=0`):

```html
<iframe class="video" src="https://www.youtube.com/embed/VPIPAc4oQqw?autoplay=1&mute=1&controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Cómo se muestran los videos de YouTube {#how-youtube-videos-display}

- Los mensajes dentro de la aplicación con YouTube incrustado pueden mostrarse directamente dentro de la aplicación o en una pestaña separada dentro de la aplicación, dependiendo de la plataforma.
- Es posible que el texto del mensaje dentro de la aplicación no se muestre cuando se presenta el video incrustado de YouTube.

## Solución de problemas {#troubleshooting}

Si tu mensaje dentro de la aplicación no muestra tu video:

- Confirma que tu URL es válida.
- Confirma que no falta la declaración `type="video/mp4"` (para video que no sea de YouTube).
- Agrega cualquier etiqueta de cierre faltante y corrige errores tipográficos.