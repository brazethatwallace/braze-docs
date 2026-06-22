---
nav_title: "Notificación push web"
article_title: Notificaciones push web
page_order: 8.5
page_type: reference
description: "Esta página de referencia cubre brevemente las notificaciones push web y enlaza a los pasos necesarios para crear una."
platform: Web
channel:
  - push

---

# Notificaciones push web {#web-push}

> Aprende sobre las notificaciones push web en Braze y encuentra recursos para crear las tuyas.

Las notificaciones push web son otra excelente forma de interactuar con los usuarios de tu aplicación web. Los clientes que visitan tu sitio web desde [navegadores compatibles](#supported-browsers) pueden optar por recibir notificaciones push web de tu aplicación web, independientemente de si la página web está cargada o no.

## Requisitos previos {#prerequisites}

Antes de poder crear y enviar cualquier mensaje push con Braze, necesitas trabajar con tus desarrolladores para integrar push en tu sitio web. Para conocer los pasos detallados, consulta nuestra [guía de integración de notificaciones push web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

### Permiso de push {#push-permission}

Cualquier marca puede integrar y utilizar notificaciones push web en su sitio web. Las notificaciones pueden llegar tanto a visitantes web actuales como anteriores, siempre que tengan un navegador web abierto, pero los visitantes deben [optar por recibir notificaciones]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/#push-permission), al igual que con las notificaciones push tradicionales de aplicaciones móviles.

{% alert tip %}
Considera usar un mensaje en el explorador para preparar a los usuarios para que opten por recibir notificaciones push web, también conocido como [push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/).
{% endalert %}

## Resumen {#overview}

Las notificaciones push web entregan actualizaciones urgentes y accionables que impulsan conversiones rápidas. Con las notificaciones push web, puedes:

- Desencadenar mensajes justo cuando cambian datos importantes, como cuando baja un precio
- Atraer a las personas de vuelta a tu sitio web con botones de llamada a la acción claros
- Personalizar tus notificaciones push con información de productos y clientes para hacer tu mensaje relevante

Las notificaciones push web funcionan de la misma manera que las notificaciones push de aplicaciones en tu teléfono. Para más información sobre cómo componer una notificación push web, consulta [Crear una notificación push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/#creating-a-push-message).

![Ejemplo de notificación push web con el mismo mensaje push mostrado en una laptop y un teléfono.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## Posibles casos de uso {#potential-use-cases}

Aquí tienes algunos ejemplos de casos de uso comunes de mensajes push web.

| Caso de uso | Descripción |
| --- | --- |
| Prueba gratuita | Anima a los nuevos visitantes de tu sitio web a registrarse para pruebas gratuitas. Al enganchar a los usuarios con la oportunidad de experimentar lo que te hace especial, puedes hacer más probable que se conviertan en clientes de pago. |
| Descarga de la aplicación | Atrae a los usuarios web a tu aplicación móvil para ayudarles a obtener aún más valor de tus productos. Considera aprovechar la personalización para destacar los beneficios de la aplicación según sus patrones de interacción actuales. |
| Descuentos y ofertas | Aumenta el conocimiento de los clientes sobre eventos y promociones con tiempo limitado. Envía mensajes a través de múltiples canales, incluidas las notificaciones push web, para aumentar el conocimiento de las promociones de tu marca. |
| Abandono del carrito de compras | Envía recordatorios automatizados a los usuarios que no han completado sus transacciones para traerlos de vuelta al flujo de pago. <br><br>Una investigación realizada por Braze encontró que las notificaciones push web son un 53 % más efectivas que el correo electrónico y un 23 % más impactantes que las notificaciones push móviles para lograr que los destinatarios regresen y completen una compra. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Posibles casos de uso" }

## Navegadores compatibles {#supported-browsers}

Los siguientes navegadores son compatibles con las notificaciones push web.

{% multi_lang_include alerts/important_alerts.md alert='Web push private browsing' %}

- Chrome (y Chrome para Android móvil)
- Safari (versión 16 o posterior)
- Firefox (y Firefox para Android móvil)
- Opera
- Edge

Para más información sobre los estándares del protocolo push y la compatibilidad de navegadores, puedes consultar recursos según tu navegador:

- [Safari (escritorio)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari (móvil)]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)

## 410 (Gone) y puntos de conexión de push web no válidos {#410-gone-and-invalid-web-push-endpoints}

Los navegadores y servicios push pueden devolver **410 Gone** (u otros errores similares de "punto de conexión no válido") cuando una suscripción de push web ya no es aceptada. Las causas comunes incluyen:

- El usuario desactivó las notificaciones para tu sitio en la configuración del navegador o del sistema operativo.
- Un perfil de usuario diferente se suscribió en el mismo perfil de navegador, por lo que el punto de conexión se rotó al nuevo suscriptor.
- La suscripción expiró después de un largo período sin interacción; después de que el usuario opte por recibirlas de nuevo, se crea una nueva suscripción en la siguiente sesión.

Después de que el usuario vuelva a activar las notificaciones, activa de nuevo el flujo normal de registro de push web de tu sitio para que Braze almacene el nuevo punto de conexión de suscripción.