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

> Las notificaciones push envían llamadas a la acción urgentes a dispositivos móviles y web, y vuelven a captar a usuarios que no han abierto tu aplicación recientemente. Dirigen directamente al contenido relevante y demuestran el valor continuo de tu producto. Este centro cubre la integración push, la estrategia de adhesión voluntaria, los tipos de mensajes, las mejores prácticas y la configuración específica de cada plataforma para iOS, Android y Web. Considera los [mensajes dentro de la aplicación de push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) antes de solicitar el permiso del sistema. Consulta las guías de integración para [iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android) y [Web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web) para empezar.

[![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"}

## Requisitos previos {#prerequisites}

Antes de empezar, asegúrate de tener lo siguiente:

- **Push integrado en tu aplicación o sitio web.** Trabaja con tus desarrolladores para configurarlo. Para conocer los pasos detallados, consulta las guías de integración para [iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications?tab=android) y [Web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web).
- **Una estrategia de adhesión voluntaria a push.** Los usuarios deben conceder permiso de push en su dispositivo. Considera usar [mensajes dentro de la aplicación de push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) para explicar el valor antes de solicitar el permiso.

## Ejemplos {#use-cases}

| Ejemplo | Explicación |
| --- | --- |
| Incorporación inicial | Hasta que los usuarios completen los pasos iniciales para usar tu aplicación (como registrar una cuenta), su valor es muy limitado. Usa notificaciones push para animar a los usuarios a completar estos pasos y que puedan comenzar a usar tu aplicación en su totalidad. |
| Primeras compras | Una vez que los usuarios se sientan cómodos usando tu aplicación, puedes usar notificaciones push para ayudar a convertirlos en compradores dentro de la aplicación. |
| Nuevas características | Las notificaciones push pueden ser eficaces para informar a los usuarios inactivos sobre nuevas características que podrían atraerlos de vuelta a tu aplicación. |
| Ofertas con tiempo limitado | Si tienes una oferta con tiempo limitado, push es una excelente manera de informar a tus usuarios antes de que expire. Estos mensajes generalmente transmiten un alto sentido de urgencia y son ideales para recordar a los usuarios que se han alejado recientemente sobre tu aplicación. Por ejemplo, si tu aplicación es un juego y ofreces un bono de moneda del juego por una racha de juego diario, alertar a un usuario de que su racha está en riesgo puede ser un push eficaz después de que haya alcanzado un cierto número de días. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ejemplos" }

## Regulaciones para mensajes push {#push-message-regulations}

Las notificaciones push llegan directamente al dispositivo de tu cliente, por lo que las políticas de las aplicaciones y las tiendas restringen cómo puedes utilizarlas.

{% alert important %}
Tus mensajes push deben cumplir las [Directrices de revisión del App Store de Apple](https://developer.apple.com/app-store/review/guidelines/) y las [políticas de Google Play](https://support.google.com/googleplay/android-developer/answer/9888379). Esto incluye normas sobre el uso de push para anuncios, correo no deseado, promociones y temas relacionados.
{% endalert %}

| Fuente de la política | Resumen |
| --- | --- |
| Apple [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) | Los usos inaceptables incluyen crear una interfaz para mostrar aplicaciones, extensiones o complementos de terceros de forma similar al App Store o como una colección de interés general. |
| Apple [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) | Las notificaciones push no deben ser un requisito para el funcionamiento de la aplicación y no deben contener información personal sensible o confidencial. No uses push para promociones o marketing directo, a menos que los clientes opten explícitamente por la adhesión voluntaria mediante un lenguaje de consentimiento en la interfaz de tu aplicación y puedan darse de baja dentro de la misma. |
| Apple [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) | No puedes monetizar capacidades integradas como las notificaciones push, la cámara o el giroscopio, ni servicios de Apple como Apple Music o iCloud. |
| Google Play — [Uso no autorizado o imitación de funcionalidades del sistema](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) | Las aplicaciones no deben imitar ni interferir con las notificaciones del sistema. Las notificaciones a nivel del sistema son solo para características esenciales de la aplicación (por ejemplo, una aplicación de aerolínea que notifica a los usuarios sobre ofertas, o un juego que notifica a los usuarios sobre promociones dentro del juego). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Regulaciones para mensajes push" }

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuándo registra Braze un envío exitoso de push? {#when-does-braze-record-a-successful-send-for-push}

Braze normalmente registra un **envío** una vez que el mensaje se despacha desde Braze hacia Apple, Google o tu servicio de push web. Las entregas (**Delivered**), aperturas, rebotes y señales de desinstalación se rastrean por separado y pueden llegar más tarde. Usa los análisis a nivel de paso y de Campaign junto con la [solución de problemas de push]({{site.baseurl}}/user_guide/channels/push/troubleshooting) cuando los **envíos** y las métricas posteriores parezcan desalineados.

## Próximos pasos {#next-steps}

- [Configuración push]({{site.baseurl}}/user_guide/channels/push/push_setup)
- [Crear un mensaje push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)