---
nav_title: Notificaciones push
article_title: Notificaciones push para Windows Universal
platform: Windows Universal
page_order: 1
description: "En este artículo se cubren las instrucciones de integración de notificaciones push para la plataforma Universal de Windows."
channel: push
hidden: true
---

# Integración de notificaciones push {#push-notification-integration}
{% multi_lang_include archive/windows_deprecation.md %}

![Un ejemplo de push universal de Windows.]({% image_buster /assets/img_archive/windows_uni_push_sample.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Una notificación push es una alerta fuera de la aplicación que aparece en la pantalla del usuario cuando se produce una actualización importante. Las notificaciones push son una forma valiosa de proporcionar a tus usuarios contenido relevante y urgente, o de reactivar su interacción con tu aplicación.

Visita nuestra [documentación]({{site.baseurl}}/user_guide/channels/push/best_practices/) para conocer otras buenas prácticas.

## Paso 1: Configura tu aplicación para push {#step-1-configure-your-application-for-push}

Asegúrate de que en tu archivo `Package.appxmanifest` están configurados los siguientes ajustes:

Dentro de la pestaña **Application**, asegúrate de que `Toast Capable` está configurado como `YES`.

## Paso 2: Configurar el panel de Braze {#step-2-configure-the-braze-dashboard}

1. [Encuentra tu SID y tu secreto de cliente](http://msdn.microsoft.com/en-us/library/windows/apps/hh465407.aspx)
2. En la página **Settings** del panel de Braze, añade el SID y el secreto de cliente en tu configuración.<br>![]({% image_buster /assets/img_archive/windows_sid.png %} "Windows SID dashboard")

## Paso 3: Actualización para el registro de apertura en segundo plano {#step-3-update-for-background-open-logging}

En tu método `OnLaunched`, después de haber llamado a `OpenSession`, añade el siguiente fragmento de código.

```
string campaignId = e.Arguments.Split(new[] { "_ab_pn_cid" }, StringSplitOptions.None)[0];
if (!string.IsNullOrEmpty(campaignId))
{
Appboy.SharedInstance.PushManager.LogPushNotificationOpened(campaignId);
}
```

## Paso 4: Crear controladores de eventos {#step-4-creating-event-handlers}

Para escuchar los eventos que se disparan cuando se recibe el push y se activa (clic del usuario), crea controladores de eventos y añádelos a los eventos de `PushManager`:

- `Appboy.SharedInstance.PushManager.PushReceivedEvent += YourPushReceivedEventHandler;`
- `Appboy.SharedInstance.PushManager.ToastActivatedEvent += YourToastActivatedEventHandler;`

Tus controladores de eventos deben tener las siguientes firmas:

- `void YourPushReceivedEventHandler(PushNotificationChannel sender, AppboyPushNotificationReceivedEventArgs args);`
- `void YourToastActivatedEventHandler(ToastNotification sender, AppboyToastActivatedEventArgs args);`

## Paso 5: Vinculación en profundidad desde push a tu aplicación {#step-5-deep-linking-from-push-into-your-app}

### Parte 1: Crear vínculos profundos para tu aplicación {#part-1-creating-deep-links-for-your-app}

Los vínculos profundos se utilizan para dirigir a los usuarios desde fuera de tu aplicación directamente a una determinada pantalla o página de tu aplicación. Normalmente, esto se hace registrando un esquema de URL (por ejemplo, myapp://mypage) en un sistema operativo y registrando tu aplicación para que gestione ese esquema; cuando se pide al sistema operativo que abra una URL de ese formato, transfiere el control a tu aplicación.

El soporte de vínculos profundos de WNS difiere de esto, ya que lanza tu aplicación con datos sobre dónde enviar al usuario. Cuando se crea un push WNS, puede incluir una cadena de lanzamiento que se transmite al `OnLaunched` de tu aplicación cuando se hace clic en el push y se abre tu aplicación. Ya utilizamos esta cadena de lanzamiento para hacer el seguimiento de campañas, y damos a los usuarios la posibilidad de añadir sus propios datos, que pueden ser analizados y utilizados para dirigir al usuario cuando se lanza la aplicación.

Si especificas una cadena de lanzamiento adicional en el dashboard o en la REST or transferencia de estado representacional API, se añadirá al final de la cadena de lanzamiento que creemos, después de la clave "abextras=". Así, un ejemplo de cadena de lanzamiento podría ser `ab_cn_id=_trackingid_abextras=page=settings`, en la que has especificado `page=settings` en el parámetro extra de la cadena de lanzamiento para poder analizarla y dirigir al usuario a la página de configuración.

### Parte 2: Vinculación en profundidad a través del dashboard {#part-2-deep-linking-through-the-dashboard}

Especifica la cadena que se añadirá a la cadena de lanzamiento en el campo "Additional Launch String Configuration" de la configuración de notificaciones push.

![]({% image_buster /assets/img_archive/windows_deep_link_click_action.png %} "Deep Link Click Action")

### Parte 3: Vinculación en profundidad a través de la REST or transferencia de estado representacional API {#part-3-deep-linking-through-the-rest-api}

Braze también permite enviar vínculos profundos a través de la REST or transferencia de estado representacional API. [Los objetos push de Windows Universal]({{site.baseurl}}/api/objects_filters/) aceptan un parámetro opcional `extra_launch_string`.