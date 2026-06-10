---
nav_title: Push
article_title: Push
page_order: 7
page_type: landing
description: "Envía llamadas a la acción urgentes a través de notificaciones push en móvil y web para volver a captar usuarios e impulsar la acción."
channel:
  - push
search_rank: 3
---

# Push {#push}

> Las notificaciones push son una forma probada y eficaz de enviar llamadas a la acción urgentes a través de móvil o web, así como de volver a captar a usuarios que no han entrado en la aplicación desde hace tiempo. Dirigen al usuario directamente al contenido y demuestran el valor de tu aplicación.

[![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"}

## Requisitos previos {#prerequisites}

Antes de empezar, asegúrate de tener lo siguiente:

- **Push integrado en tu aplicación o sitio web.** Trabaja con tus desarrolladores para configurarlo. Para conocer los pasos detallados, consulta las guías de integración para [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android) y [Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).
- **Una estrategia de adhesión voluntaria a push.** Los usuarios deben conceder permiso de push en su dispositivo. Considera usar [mensajes de preparación para push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/) para explicar el valor antes de solicitarlo.

## Casos de uso {#use-cases}

| Caso de uso | Explicación |
| --- | --- |
| Incorporación inicial | Hasta que los usuarios completen los pasos iniciales para usar tu aplicación (como registrar una cuenta), su valor es muy limitado. Usa notificaciones push para animar a los usuarios a completar estos pasos y que puedan empezar a usar tu aplicación en su totalidad. |
| Primeras compras | Una vez que los usuarios se sientan cómodos usando tu aplicación, puedes usar notificaciones push para ayudar a convertirlos en compradores dentro de la aplicación. |
| Nuevas características | Las notificaciones push pueden ser eficaces para informar a usuarios inactivos sobre nuevas características que podrían atraerlos de vuelta a tu aplicación. |
| Ofertas con tiempo limitado | Si tienes una oferta con fecha de vencimiento, push es una excelente forma de avisar a tus usuarios antes de que expire. Estos mensajes generalmente transmiten un alto sentido de urgencia y son ideales para recordar a usuarios que se han alejado recientemente sobre tu aplicación. Por ejemplo, si tu aplicación es un juego y ofreces un bono de moneda del juego por una racha de juego diaria, alertar a un usuario de que su racha está en riesgo puede ser un push eficaz después de que haya alcanzado cierto número de días. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso" }

## Regulaciones de mensajes push {#push-message-regulations}

Push llega directamente al dispositivo de tu cliente, por lo que las políticas de aplicaciones y tiendas regulan cómo puedes usarlo.

{% alert important %}
Tus mensajes push deben cumplir con las [Directrices de revisión del App Store de Apple](https://developer.apple.com/app-store/review/guidelines/) y las [políticas de Google Play](https://support.google.com/googleplay/android-developer/answer/9888379). Esto incluye reglas sobre el uso de push para anuncios, correo no deseado, promociones y temas relacionados.
{% endalert %}

| Fuente de la política | Resumen |
| --- | --- |
| Apple [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) | Los usos inaceptables incluyen crear una interfaz para mostrar aplicaciones, extensiones o complementos de terceros similar al App Store o como una colección de interés general. |
| Apple [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) | Push no debe ser necesario para que la aplicación funcione y no debe contener información personal sensible o confidencial. No uses push para promociones o marketing directo a menos que los clientes acepten explícitamente mediante un lenguaje de consentimiento en la interfaz de tu aplicación y puedan darse de baja en la aplicación. |
| Apple [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) | No puedes monetizar capacidades integradas como las notificaciones push, la cámara o el giroscopio, ni servicios de Apple como Apple Music o iCloud. |
| Google Play — [Uso no autorizado o imitación de funcionalidades del sistema](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) | Las aplicaciones no deben imitar ni interferir con las notificaciones del sistema. Las notificaciones a nivel de sistema son solo para características integrales de la aplicación (por ejemplo, una aplicación de aerolínea que notifica a los usuarios sobre ofertas, o un juego que notifica a los usuarios sobre promociones dentro del juego). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Regulaciones de mensajes push" }

## Próximos pasos {#next-steps}

- [Configuración push]({{site.baseurl}}/user_guide/channels/push/push_setup/)
- [Crear un mensaje push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/)