---
nav_title: Notificaciones push
article_title: Notificaciones push
page_order: 2.3
description: "Esta página de destino es el hogar de todo lo relacionado con las notificaciones push."
---

# Notificaciones push {#push-notifications}

> Las [notificaciones push]({{site.baseurl}}/user_guide/channels/push) te permiten enviar notificaciones desde tu aplicación cuando se producen eventos importantes. Puedes enviar una notificación push cuando tengas nuevos mensajes instantáneos que entregar, alertas de noticias de última hora que enviar o el último episodio del programa de TV favorito de tu usuario listo para que lo descargue para verlo sin conexión. También son más eficientes que la obtención en segundo plano, ya que la aplicación solo se inicia cuando es necesario.

{% alert note %}
Si **Redirect to web URL** con **Open web URL inside app** no está seleccionado, pero el enlace aún se abre dentro de la aplicación, es posible que la aplicación esté gestionando la URL (por ejemplo, con enlaces universales en iOS o App Links en Android). Para abrir el enlace en el navegador, confirma que tu aplicación delega la URL al navegador del sistema cuando el usuario toca la notificación, o ajusta la gestión de URL de tu aplicación para que la acción de clic coincida con la configuración del panel de Braze. Consulta la documentación push de tu plataforma para saber cómo se configuran las acciones de clic y la gestión de URL.
{% endalert %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/push_notifications.md %}
{% endsdktab %}

{% sdktab android tv %}
## Acerca de las notificaciones push para Android TV {#about-push-notifications-for-android-tv}

![Ilustración de un dispositivo Android TV utilizada para la guía de notificaciones push de Android TV.]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

Aunque no es una característica nativa, la integración de notificaciones push en Android TV es posible aprovechando el SDK de Braze para Android y Firebase Cloud Messaging para registrar un token push para Android TV. Sin embargo, debes crear una interfaz de usuario para mostrar la carga útil de la notificación una vez recibida.

## Requisitos previos {#prerequisites}

Para utilizar esta característica, debes completar lo siguiente:

- [Integrar el SDK de Braze para Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)
- [Configurar las notificaciones push para el SDK de Braze para Android]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)

## Configurar las notificaciones push {#setting-up-push-notifications}

Para configurar las notificaciones push en Android TV:

1. Crea una vista personalizada en tu aplicación para mostrar tus notificaciones.
2. Crea una [fábrica de notificaciones personalizada]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_customization-display). Esto anula el comportamiento predeterminado del SDK y te permite mostrar las notificaciones manualmente. Al devolver `null`, se evita que el SDK procese la notificación y se requiere código personalizado para mostrarla. Después de completar estos pasos, puedes empezar a enviar notificaciones push a Android TV.<br><br>
3. (Opcional) Para realizar un seguimiento eficaz de los análisis de clics, configura el seguimiento de análisis de clics. Esto se puede lograr creando una [devolución de llamada push]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_push-callback) para escuchar las intenciones de push abierto y recibido de Braze.

{% alert note %}
Estas notificaciones no persisten y solo son visibles para el usuario cuando el dispositivo las muestra. Esto se debe a que el centro de notificaciones de Android TV no admite notificaciones históricas.
{% endalert %}

## Probar las notificaciones push de Android TV {#testing-android-tv-push-notifications}

Para comprobar si tu implementación de push es correcta, envía una notificación desde el panel de Braze como lo harías normalmente para un dispositivo Android.

- **Si la aplicación está cerrada**: El mensaje push muestra una notificación de tipo toast en la pantalla.
- **Si la aplicación está abierta**: Tienes la oportunidad de mostrar el mensaje en tu propia interfaz de usuario alojada. Sigue el estilo de interfaz de usuario de los mensajes dentro de la aplicación del SDK de Android para móviles.

## Mejores prácticas {#best-practices}

Para los especialistas en marketing que utilizan Braze, lanzar una campaña a Android TV es idéntico a lanzar una notificación push a aplicaciones móviles de Android. Para dirigirte exclusivamente a estos dispositivos, selecciona la aplicación de Android TV en la segmentación.

La respuesta de entrega y clic devuelta por FCM sigue la misma convención que un dispositivo Android móvil; por lo tanto, cualquier error es visible en el registro de actividad de mensajes.

{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/push_notifications.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/push_notifications.md %}
{% endsdktab %}

{% sdktab huawei %}
{% multi_lang_include developer_guide/huawei/push_notifications.md %}
{% endsdktab %}

{% sdktab React Native %}
{% multi_lang_include developer_guide/react_native/push_notifications.md %}
{% endsdktab %}

{% sdktab safari %}
{% multi_lang_include developer_guide/safari/push_notifications.md %}
{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/push_notifications.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin)%}
{% multi_lang_include developer_guide/xamarin/push_notifications.md %}
{% endsdktab %}
{% endsdktabs %}