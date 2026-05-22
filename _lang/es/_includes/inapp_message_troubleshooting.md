## Comprobaciones básicas {#basic-checks}

### Mi mensaje dentro de la aplicación no se mostró para un usuario {#my-in-app-message-wasnt-shown-for-one-user}

1. ¿Estaba el usuario en el segmento al inicio de la sesión, cuando el SDK solicita nuevos mensajes dentro de la aplicación?
2. ¿El usuario era elegible o reelegible para recibir el mensaje dentro de la aplicación según las reglas de segmentación de la Campaign?
3. ¿Se vio afectado el usuario por un límite de frecuencia?
4. ¿Estaba el usuario en un grupo de control? Comprueba si tu Campaign está configurada para pruebas AB.
5. ¿Se mostró un mensaje dentro de la aplicación diferente y de mayor prioridad en lugar del mensaje esperado?
6. ¿Mi dispositivo estaba en la orientación correcta especificada por la Campaign?
7. ¿Mi mensaje fue suprimido por el intervalo de tiempo mínimo predeterminado de 30 segundos entre desencadenamientos, impuesto por el SDK?

### Mi mensaje dentro de la aplicación no se mostró a todos los usuarios de esta plataforma {#my-in-app-message-wasnt-shown-to-all-users-on-this-platform}

1. ¿Tu Campaign está configurada para dirigirse a aplicaciones móviles o navegadores web, según corresponda? Por ejemplo, si tu Campaign solo se dirige a navegadores web, no se enviará a dispositivos Android.
2. ¿Implementaste una interfaz de usuario personalizada y funciona según lo previsto? ¿Hay algún otro manejo personalizado o supresión del lado de la aplicación que pueda estar interfiriendo con la visualización?
3. ¿Alguna vez esta plataforma y versión de aplicación en particular ha mostrado mensajes dentro de la aplicación con éxito?
4. ¿El desencadenamiento tuvo lugar localmente en el dispositivo? Ten en cuenta que no se puede utilizar una llamada REST para desencadenar un mensaje dentro de la aplicación en el SDK.

### Mi mensaje dentro de la aplicación no se mostró para todos los usuarios {#my-in-app-message-wasnt-shown-for-all-users}

1. ¿Se configuró correctamente la acción desencadenante en el dashboard, así como en la integración de la aplicación?
2. ¿Se mostró un mensaje dentro de la aplicación diferente y de mayor prioridad en lugar del mensaje esperado?
3. ¿Tienes una versión reciente del SDK? Algunos tipos de mensajes dentro de la aplicación tienen requisitos de versión del SDK.
4. ¿Se han integrado correctamente las sesiones en tu integración? ¿Funcionan los análisis de sesión en esta aplicación?
5. ¿Estás usando una biblioteca de componentes personalizada que pueda interferir con la forma en que se muestran los mensajes dentro de la aplicación?

### Mi mensaje dentro de la aplicación tardó mucho en aparecer {#my-in-app-message-took-a-lot-of-time-to-appear}

1. Si sirves archivos grandes de imagen o video desde tu CDN a un mensaje dentro de la aplicación basado en HTML, comprueba que tus archivos estén optimizados para ser lo más pequeños posible y que tu CDN tenga un buen rendimiento.
2. Comprueba si has configurado un `delay` para tu mensaje dentro de la aplicación en el dashboard.
{% case include.sdk %}
  {% when "iOS", "Android" %}
3. Dependiendo de las circunstancias, los mensajes dentro de la aplicación descargarán o cargarán las imágenes relevantes del disco antes de su visualización. Si tienes una conexión de red lenta o un dispositivo de muy bajo rendimiento, este proceso puede tardar. Asegúrate de que tus imágenes estén optimizadas para ser lo más pequeñas posible.
{% endcase %}

Para profundizar en estos escenarios, visita <a id="troubleshooting-in-app-advanced">la sección de solución de problemas avanzada</a>.

## Problemas con los análisis de impresiones y clics {#issues-with-impressions-and-click-analytics}

{% if include.sdk == "iOS" %}
### Las impresiones y los clics no se registran {#impressions-and-clicks-arent-being-logged}

Si has configurado un delegado de mensajes dentro de la aplicación para gestionar manualmente la visualización del mensaje o las acciones de clic, debes [registrar los clics](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) y las [impresiones](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:)) manualmente en el mensaje dentro de la aplicación.
{% elsif include.sdk == "Android" %}
### Las impresiones y los clics no se registran {#impressions-and-clicks-arent-being-logged}
Si has configurado un delegado de mensajes dentro de la aplicación para gestionar manualmente la visualización del mensaje o las acciones de clic, debes registrar manualmente los clics y las impresiones en el mensaje dentro de la aplicación.
{% endif %}

### Las *impresiones* son mayores que las *impresiones únicas* {#impressions-are-greater-than-unique-impressions}

Este es un comportamiento esperado y puede ocurrir cuando:

- Aunque la reelegibilidad esté desactivada, los usuarios que recibieron la Campaign pueden tener más de un dispositivo. El desencadenamiento de la Campaign se actualiza en el siguiente inicio de sesión, por lo que un dispositivo no sabrá si otro dispositivo ya ha desencadenado la Campaign hasta que el usuario inicie una nueva sesión.
- Si tu mensaje dentro de la aplicación tiene un retraso programado de unos minutos después de que ocurra el evento desencadenante, los usuarios pueden haber recibido el mensaje más de una vez.

Para más información sobre la reelegibilidad, consulta [Reelegibilidad para Campaigns y Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/).

### Las impresiones son inferiores a lo esperado {#impressions-are-lower-than-expected}

1. Los desencadenantes tardan en sincronizarse con el dispositivo al iniciar la sesión, por lo que puede darse una condición de carrera si los usuarios registran un evento o una compra justo después de iniciar la sesión. Una posible solución podría ser cambiar la Campaign para que se desencadene al inicio de la sesión y luego segmentar en función del evento o la compra previstos. Ten en cuenta que esto entregaría el mensaje dentro de la aplicación en el siguiente inicio de sesión tras producirse el evento.

2. Si la Campaign se desencadena por el inicio de una sesión o un evento personalizado, debes asegurarte de que este evento o sesión se produce con la frecuencia suficiente para desencadenar el mensaje. Comprueba estos datos en las páginas [Resumen]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data) (para datos de sesión) o [Eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting):

![Página de eventos personalizados que muestra un gráfico del número de veces que se produjo el evento personalizado Añadido a Favoritos durante un periodo de un mes]({% image_buster /assets/img_archive/trouble5.png %})

Otras razones incluyen:

- Los usuarios no han visto el mensaje dentro de la aplicación, por lo que las impresiones no se registran.
- Varios mensajes dentro de la aplicación se interceptan entre sí (como varios mensajes de alta prioridad).
- Si el mensaje está en un Canvas, los usuarios pueden estar entrando en un paso de retraso que es más largo que el tiempo de espera de sesión antes de recibir el mensaje dentro de la aplicación.

### Las impresiones son más bajas que antes {#impressions-are-lower-than-they-used-to-be}

1. Asegúrate de que nadie haya alterado involuntariamente el segmento o la Campaign desde su lanzamiento. Nuestros registros de cambios de segmentos y Campaigns te darán información sobre los cambios que se han hecho, quién los hizo y cuándo ocurrieron.

![Enlace para ver el registro de cambios en la página Detalles de la Campaign con siete cambios desde la última vez que el usuario vio la Campaign]({% image_buster /assets/img_archive/trouble4.png %})

{: start="2"}
2. Asegúrate de no reutilizar tu evento desencadenante en otra Campaign de mensajes dentro de la aplicación con una prioridad mayor.

## Solución de problemas avanzada {#troubleshooting-in-app-advanced}

La mayoría de los problemas de mensajes dentro de la aplicación pueden dividirse en dos categorías principales: entrega y visualización. Para solucionar por qué un mensaje dentro de la aplicación esperado no se mostró en tu dispositivo, confirma que el <a id="troubleshooting-in-app-message-delivery">mensaje dentro de la aplicación se entregó al dispositivo</a> y luego <a id="troubleshooting-in-app-message-display">soluciona el problema de visualización del mensaje</a>.

### Solución de problemas de entrega {#troubleshooting-in-app-message-delivery}

El SDK solicita mensajes dentro de la aplicación a los servidores de Braze al iniciar la sesión. Para comprobar si los mensajes dentro de la aplicación se están entregando a tu dispositivo, tendrás que asegurarte de que los mensajes dentro de la aplicación están siendo solicitados por el SDK y devueltos por los servidores de Braze.

#### Comprueba si los mensajes se solicitan y se devuelven {#check-if-messages-are-requested-and-returned}

1. Añádete como [usuario de prueba]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) en el dashboard.
2. Configura una Campaign de mensajes dentro de la aplicación dirigida a tu usuario.
3. Asegúrate de que se produce una nueva sesión en tu aplicación.
4. Utiliza los [registros de eventos de usuario]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) para comprobar que tu dispositivo solicita mensajes dentro de la aplicación al inicio de la sesión. Busca la solicitud del SDK asociada al evento de inicio de sesión de tu usuario de prueba.
  - Si tu aplicación debía solicitar mensajes dentro de la aplicación desencadenados, deberías ver `trigger` en el campo **Requested Responses**, en **Response Data**.
  - Si tu aplicación debía solicitar mensajes originales dentro de la aplicación, deberías ver `in_app` en el campo **Requested Responses**, en **Response Data**.
5. Utiliza los [registros de eventos de usuario]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) para comprobar si los mensajes correctos dentro de la aplicación se devuelven en los datos de respuesta.<br>![]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### Solución de problemas de mensajes no solicitados {#troubleshoot-messages-not-being-requested}

Si tus mensajes dentro de la aplicación no se solicitan, es posible que tu aplicación no esté haciendo un seguimiento correcto de las sesiones, ya que los mensajes dentro de la aplicación se actualizan al iniciar la sesión. Además, asegúrate de que tu aplicación está iniciando realmente una sesión según la semántica de tiempo de espera de sesión de tu aplicación:

![La solicitud del SDK encontrada en los registros de eventos de usuario muestra un evento de inicio de sesión correcto.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### Solución de problemas de mensajes no devueltos {#troubleshoot-messages-not-being-returned}

Si tus mensajes dentro de la aplicación no se devuelven, es probable que estés experimentando un problema de segmentación de la Campaign:

1. Tu segmento no contiene a tu usuario.
  - Comprueba la pestaña [**Interacción**]({{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) de tu usuario para ver si el segmento correcto aparece en **Segments**.
2. Tu usuario ha recibido previamente el mensaje dentro de la aplicación y no era reelegible para volver a recibirlo.
  - Comprueba la [configuración de reelegibilidad de la Campaign]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) en el paso **Delivery** del **Campaign Composer** y asegúrate de que la configuración de reelegibilidad se ajusta a tu configuración de prueba.
3. Tu usuario alcanzó el límite de frecuencia de la Campaign.
  - Comprueba la [configuración de límite de frecuencia]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) de la Campaign y asegúrate de que se ajusta a tu configuración de prueba.
4. Si había un grupo de control en la Campaign, tu usuario puede haber caído en el grupo de control.
  - Puedes comprobar si esto ha ocurrido creando un segmento con un filtro de variante de Campaign recibida, en el que la variante de Campaign esté configurada como **Control**, y comprobando si tu usuario cayó en ese segmento.
  - Cuando crees Campaigns para realizar pruebas de integración, asegúrate de no añadir un grupo de control.


### Solución de problemas de visualización {#troubleshooting-in-app-message-display}

Si tu aplicación solicita y recibe correctamente mensajes dentro de la aplicación, pero no se muestran, es posible que la lógica del dispositivo esté impidiendo la visualización:

1. ¿Se desencadena el evento como se espera? Para comprobarlo, intenta configurar el mensaje para que se desencadene mediante una acción diferente (como el inicio de sesión) y verifica si se muestra.
{% if include.sdk == "iOS" %}
2. Los mensajes desencadenados dentro de la aplicación tienen una tasa limitada en función del [intervalo de tiempo mínimo entre desencadenamientos]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), que es de 30 segundos de forma predeterminada.
{% elsif include.sdk == "Android" %}
2. Los mensajes desencadenados dentro de la aplicación tienen una tasa limitada en función del [intervalo de tiempo mínimo entre desencadenamientos]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), que es de 30 segundos de forma predeterminada.
{% elsif include.sdk == "Web" %}
2. Los mensajes desencadenados dentro de la aplicación tienen una tasa limitada en función del [intervalo de tiempo mínimo entre desencadenamientos]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), que es de 30 segundos de forma predeterminada.
{% endif %}
3. Las descargas de imágenes fallidas impedirán que se muestren los mensajes dentro de la aplicación con imágenes. Comprueba los registros de tu dispositivo para asegurarte de que las descargas de imágenes no están fallando. Prueba a eliminar temporalmente la imagen de tu mensaje para ver si así se muestra.
{% case include.sdk %}
  {% when "iOS", "Android" %}
4. Si has configurado un delegado para personalizar la gestión de mensajes dentro de la aplicación, comprueba tu delegado para asegurarte de que no está afectando a la visualización de mensajes dentro de la aplicación.
  {% when "Web" %}
5. Si tienes una gestión personalizada de mensajes dentro de la aplicación a través de `braze.subscribeToInAppMessage` o `appboy.subscribeToNewInAppMessages`, comprueba esa suscripción para asegurarte de que no está afectando a la visualización de mensajes dentro de la aplicación.
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
6. Si la orientación del dispositivo no coincide con la orientación especificada por el mensaje dentro de la aplicación, el mensaje dentro de la aplicación no se mostrará. Asegúrate de que tu dispositivo está en la orientación correcta.
{% endcase %}
7. Si tu mensaje dentro de la aplicación se desencadena al iniciar la sesión y has configurado un tiempo de espera de sesión ampliado, esto afectará a la rapidez con la que puedes mostrar mensajes. Por ejemplo, si el tiempo de espera de tu sesión está configurado en 300 segundos, cerrar y volver a abrir la aplicación en menos de ese tiempo no actualizará la sesión, por lo que un mensaje dentro de la aplicación desencadenado por el inicio de una sesión no se mostrará.