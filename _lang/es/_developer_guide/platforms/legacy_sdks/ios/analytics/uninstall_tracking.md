---
nav_title: Uninstall Tracking
article_title: Uninstall Tracking para iOS
platform: iOS
page_order: 7
description: "Este artículo explica cómo configurar Uninstall Tracking para tu aplicación iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Uninstall Tracking para iOS {#uninstall-tracking-for-ios}

> Este artículo explica cómo configurar Uninstall Tracking para tu aplicación iOS, y cómo hacer pruebas para que tu aplicación no realice ninguna acción automática no deseada al recibir un push de Uninstall Tracking de Braze.

Uninstall Tracking utiliza notificaciones push en segundo plano con una flag de Braze en la carga útil. Para más información, consulta [Uninstall Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking) en nuestra guía del usuario.

## Paso 1: Habilitar push en segundo plano {#step-1-enabling-background-push}

Asegúrate de haber habilitado la opción **Remote notifications** en la sección **Background Modes** de la pestaña **Capabilities** de tu proyecto de Xcode. Consulta nuestra documentación de [notificaciones push silenciosas]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications) para más detalles.

## Paso 2: Comprobar las notificaciones push en segundo plano de Braze {#step-2-checking-for-braze-background-push}

Braze utiliza notificaciones push en segundo plano para recopilar análisis de Uninstall Tracking. Asegúrate de que tu aplicación [no realice ninguna acción no deseada]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push) al recibir nuestras notificaciones de Uninstall Tracking.

## Paso 3: Prueba desde el panel {#step-3-test-from-the-dashboard}

A continuación, envíate una notificación push de prueba desde el panel. Esta push de prueba no actualizará tu perfil de usuario.

1. En la página **Campaigns**, crea una Campaign de notificación push y selecciona **iOS push** como tu plataforma.<br><br>
2. En la página **Configuración**, añade la clave `appboy_uninstall_tracking` con el valor correspondiente `true` y marca **Add Content-Available Flag**.<br><br>
3. Usa la página **Vista previa** para enviarte una push de prueba de Uninstall Tracking.<br><br>
4. Comprueba que tu aplicación no realiza ninguna acción automática no deseada al recibir la push.

{% alert important %}
Estos pasos de prueba son un sustituto del envío de una push de Uninstall Tracking desde Braze. Si tienes los conteos de señales habilitados, se enviará un número de señal junto con la push de prueba, pero las push de Uninstall Tracking de Braze no establecerán un número de señal en tu aplicación.
{% endalert %}

## Paso 4: Habilitar Uninstall Tracking {#step-4-enable-uninstall-tracking}

Sigue las instrucciones para [habilitar Uninstall Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).