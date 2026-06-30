---
nav_title: Temas de modo oscuro
article_title: Temas de modo oscuro
page_order: 2
description: "Este artículo de referencia cubre el soporte de modo oscuro en los mensajes dentro de la aplicación de Braze, incluyendo cómo configurar un tema de modo oscuro y consideraciones de compatibilidad."
channel:
  - in-app messages

---

# Temas de modo oscuro {#dark-mode-themes}

> Este artículo aplica al [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional). El modo oscuro ofrece a los usuarios la oportunidad de establecer una preferencia de color a nivel del sistema (introducida en [Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) e [iOS 13](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/)). Los temas "oscuros" están diseñados para conservar la vida de la batería y reducir la fatiga visual de los usuarios, al tiempo que proporcionan a los desarrolladores de aplicaciones una forma de implementar temas de colores oscuros.

Los mensajes dentro de la aplicación de Braze admiten agregar un tema oscuro alternativo para entregar el mensaje con los colores adecuados a tus usuarios según su preferencia y mantener la coherencia con el diseño de tu aplicación.

## Cómo funciona el modo oscuro {#how-dark-mode-works}

Los usuarios con versiones de al menos Android 10 o iOS 13 y posteriores pueden activar o desactivar el modo oscuro en la configuración de su dispositivo.

Cuando el modo oscuro está habilitado, los menús y pantallas nativos del dispositivo (notificaciones push, configuración del dispositivo, etc.) cambiarán a un gris oscuro. Las aplicaciones también pueden optar por admitir el modo oscuro especificando los temas alternativos en el código de la aplicación.

## Configurar un tema de modo oscuro {#setting-a-dark-mode-theme}

El modo oscuro, ubicado en la pestaña **Diseñar** al [crear un mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional), te permite agregar un tema de color alternativo para los usuarios que están en modo oscuro en su dispositivo.

![Usuario alternando entre los estilos de modo claro y modo oscuro en la pestaña de estilo al crear un mensaje dentro de la aplicación.]({% image_buster /assets/img_archive/iam-dark-mode.gif %})

Cuando esta opción está habilitada, puedes elegir colores de tema oscuro para tu mensaje dentro de la aplicación usando el selector de color, o seleccionando [perfiles de color]({{site.baseurl}}/user_guide/channels/in_app_messages/customize#color-profile) existentes para reutilizar temas oscuros o claros ya creados.

{% alert note %}
Puedes usar esta característica incluso si tu aplicación no ofrece su propio tema oscuro. Sin embargo, los dispositivos que no admiten el modo oscuro mostrarán el tema claro de forma predeterminada. Cambiar el tema del dispositivo en Android mientras se muestra un mensaje dentro de la aplicación no cambiará el tema utilizado para ese mensaje dentro de la aplicación.
{% endalert %}

### Usar el modo oscuro de forma consistente {#using-dark-mode-consistently}

Para usar el modo oscuro en todos los mensajes dentro de la aplicación, primero crea un perfil de color que se alinee con tu tema de modo oscuro.

1. Ve a **Contenido** > **Mensaje dentro de la aplicación**.
2. Selecciona **Crear plantillas** y elige [Perfil de color]({{site.baseurl}}/user_guide/channels/in_app_messages/customize#color-profile) en el menú desplegable.
3. Crea y guarda tu perfil de color.

Al crear una versión de modo oscuro de un mensaje dentro de la aplicación, puedes seleccionar ese perfil de color para mantener la apariencia de tus mensajes dentro de la aplicación de forma consistente.

## Compatibilidad {#compatibility}

- Tus usuarios deben estar en dispositivos iOS versión 13 o superior, o dispositivos Android versión 10 o superior.
- Se requiere Braze iOS SDK v3.21.0+ y Braze Android SDK v3.8.0+.

{% alert note %}
Las aplicaciones con modo oscuro se introdujeron con Android 10 e iOS 13. Los usuarios que no hayan actualizado sus teléfonos al menos a estas versiones solo verán el tema claro. <br><br>Las campañas seguirán entregándose a todos los usuarios que sean elegibles para la audiencia que hayas seleccionado, independientemente de la configuración de modo oscuro o la versión del sistema operativo de los usuarios.
{% endalert %}

## Usar mensajes dentro de la aplicación HTML {#using-html-in-app-messages}

Para crear un tema oscuro y claro para mensajes dentro de la aplicación HTML, puedes usar la característica de medios CSS [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) para detectar la preferencia del usuario.

Por ejemplo:

```css
@media (prefers-color-scheme: dark) {
  body {
    background: #333;
    color: white;
  }
}

@media (prefers-color-scheme: light) {
  body {
    background: white;
    color: #555;
  }
}
```

