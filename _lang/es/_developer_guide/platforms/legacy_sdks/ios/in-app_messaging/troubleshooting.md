---
nav_title: Solución de problemas
article_title: Solución de problemas de mensajería dentro de la aplicación para iOS
platform: iOS
page_order: 7
description: "Este artículo de referencia cubre posibles temas de solución de problemas de mensajes dentro de la aplicación de iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Solución de problemas con los mensajes dentro de la aplicación {#troubleshoot-in-app-messages}

## Impresiones {#impressions}

### No se registran los análisis de impresiones o clics {#impression-or-click-analytics-arent-being-logged}

Si has configurado un delegado de mensajes dentro de la aplicación para gestionar manualmente la visualización de mensajes o las acciones de clic, tendrás que registrar manualmente los clics y las impresiones en el mensaje dentro de la aplicación.

#### Las impresiones son más bajas de lo esperado {#impressions-are-lower-than-expected}

Los desencadenantes tardan en sincronizarse con el dispositivo al inicio de la sesión, por lo que puede haber una condición de carrera si los usuarios registran un evento o una compra justo después de iniciar una sesión. Una posible solución podría ser cambiar la Campaign para que se desencadene al inicio de la sesión y luego segmentar en función del evento o la compra previstos. Ten en cuenta que esto entregaría el mensaje dentro de la aplicación en el siguiente inicio de sesión después de que se haya producido el evento.

## El mensaje dentro de la aplicación esperado no se mostró {#expected-in-app-message-did-not-display}

La mayoría de los problemas con los mensajes dentro de la aplicación se pueden dividir en dos categorías principales: entrega y visualización. Para solucionar por qué un mensaje dentro de la aplicación esperado no se mostró en tu dispositivo, primero debes asegurarte de que el [mensaje dentro de la aplicación fue entregado al dispositivo](#troubleshooting-in-app-message-delivery) y luego [solucionar los problemas de visualización del mensaje](#troubleshooting-in-app-message-display).

### Entrega del mensaje dentro de la aplicación {#troubleshooting-in-app-message-delivery}

El SDK or kit de desarrollo de software solicita los mensajes dentro de la aplicación a los servidores de Braze al inicio de la sesión. Para comprobar si los mensajes dentro de la aplicación se están entregando a tu dispositivo, deberás asegurarte de que los mensajes dentro de la aplicación están siendo tanto solicitados por el SDK or kit de desarrollo de software como devueltos por los servidores de Braze.

#### Comprueba si los mensajes se solicitan y se devuelven {#check-if-messages-are-requested-and-returned}

1. Añádete como [usuario de prueba]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) en el panel.
2. Configura una campaña de mensajes dentro de la aplicación dirigida a tu usuario.
3. Asegúrate de que se produzca una nueva sesión en tu aplicación.
4. Usa los [registros de usuarios del evento]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) para comprobar que tu dispositivo está solicitando mensajes dentro de la aplicación al inicio de la sesión. Encuentra la solicitud del SDK or kit de desarrollo de software asociada con el evento de inicio de sesión de tu usuario de prueba.
  - Si tu aplicación debía solicitar mensajes dentro de la aplicación activados, deberías ver `trigger` en el campo **Requested Responses** bajo **Response Data**.
  - Si tu aplicación debía solicitar mensajes dentro de la aplicación originales, deberías ver `in_app` en el campo **Requested Responses** bajo **Response Data**.
5. Usa los [registros de usuarios del evento]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) para comprobar si los mensajes dentro de la aplicación correctos se están devolviendo en los datos de respuesta.<br>![Entradas del registro de usuarios del evento para solicitudes de mensajes dentro de la aplicación.]({% image_buster /assets/img_archive/event_user_log_iams.png %})

#### Solucionar problemas cuando los mensajes no se solicitan {#troubleshoot-messages-not-being-requested}

Si tus mensajes dentro de la aplicación no se están solicitando, es posible que tu aplicación no esté rastreando las sesiones correctamente, ya que los mensajes dentro de la aplicación se actualizan al inicio de la sesión. También asegúrate de que tu aplicación esté realmente iniciando una sesión según la semántica de tiempo de espera de sesión de tu aplicación:

![La solicitud del SDK or kit de desarrollo de software encontrada en los registros de usuarios del evento que muestra un evento de inicio de sesión exitoso.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

### Solucionar problemas cuando los mensajes no se devuelven {#troubleshoot-messages-not-being-returned}

Si tus mensajes dentro de la aplicación no se están devolviendo, probablemente estés experimentando un problema de segmentación de la campaña:

- Tu Segment no contiene a tu usuario.
  - Consulta la pestaña [**Engagement**]({{ site.baseurl }}/user_guide/audience/manage_audience/user_profiles/#engagement-tab) de tu usuario para ver si el Segment correcto aparece en **Segments**.
- Tu usuario ya recibió el mensaje dentro de la aplicación y no era elegible para recibirlo de nuevo.
  - Consulta la [configuración de reelegibilidad de la campaña]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) en el paso **Delivery** del **Campaign Composer** y asegúrate de que la configuración de reelegibilidad se alinee con tu configuración de prueba.
- Tu usuario alcanzó el límite de frecuencia de la campaña.
  - Consulta la [configuración del límite de frecuencia]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) de la campaña y asegúrate de que se alinee con tu configuración de prueba.
- Si había un grupo de control en la campaña, es posible que tu usuario haya caído en el grupo de control.
  - Puedes comprobar si esto ha sucedido creando un Segment con un filtro de variante de campaña recibida, donde la variante de campaña esté configurada como **Control**, y verificando si tu usuario cayó en ese Segment.
  - Al crear campañas con fines de pruebas de integración, asegúrate de desactivar la opción de añadir un grupo de control.

### Visualización del mensaje dentro de la aplicación {#troubleshooting-in-app-message-display}

Si tu aplicación está solicitando y recibiendo mensajes dentro de la aplicación correctamente pero no se están mostrando, es posible que alguna lógica del lado del dispositivo esté impidiendo la visualización:

- Los mensajes dentro de la aplicación activados tienen un límite de tasa basado en el [intervalo de tiempo mínimo entre activaciones]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/in-app_message_delivery#minimum-time-interval-between-triggers), que por defecto es de 30 segundos.
- Si has configurado un delegado para personalizar el manejo de los mensajes dentro de la aplicación, comprueba tu delegado para asegurarte de que no está afectando la visualización de los mensajes dentro de la aplicación.
- Las descargas de imágenes fallidas impedirán que se muestren los mensajes dentro de la aplicación que contengan imágenes. Las descargas de imágenes siempre fallarán si el framework `SDWebImage` no está integrado correctamente. Comprueba los registros de tu dispositivo para asegurarte de que las descargas de imágenes no están fallando.
- Si la orientación del dispositivo no coincidía con la orientación especificada por el mensaje dentro de la aplicación, el mensaje dentro de la aplicación no se mostrará. Asegúrate de que tu dispositivo esté en la orientación correcta.