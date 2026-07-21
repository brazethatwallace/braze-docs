---
nav_title: Solución de problemas
article_title: Solución de problemas de mensajes dentro de la aplicación para el SDK de Braze
page_order: 50
description: "Diagnostica por qué los mensajes dentro de la aplicación no se entregan o no se muestran utilizando un índice de síntomas, una ruta de investigación estándar, notas sobre Canvas e IAM, y comprobaciones específicas del SDK por plataforma."
channel:
  - in-app messages

---

# Solución de problemas de mensajes dentro de la aplicación {#troubleshoot-in-app-messages}

> Usa esta página para diagnosticar por qué los mensajes dentro de la aplicación no se entregan o no se muestran en un dispositivo. Para la configuración del panel (prioridad, desencadenantes, Segments y reelegibilidad), consulta las [preguntas frecuentes sobre mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

Antes de depurar, añádete como [usuario de prueba]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users) y revisa [Envío de mensajes de prueba]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages).

## Empieza aquí: identifica tu síntoma {#start-here-match-your-symptom}

| Síntoma | Ir a |
| --- | --- |
| El mensaje dentro de la aplicación no se mostró para un usuario | [Un usuario](#in-app-message-not-shown-for-one-user) |
| El mensaje dentro de la aplicación no se mostró en una plataforma (Android, iOS o Web) | [Una plataforma](#in-app-message-not-shown-on-one-platform) |
| El mensaje dentro de la aplicación de un paso de **Canvas** no se mostró | [Mensajes dentro de la aplicación en Canvas](#canvas-in-app-messages) |
| El mensaje dentro de la aplicación se mostró tarde o con retraso | [Temporización y visualización retrasada](#timing-and-delayed-display) |
| Las impresiones o los clics parecen incorrectos | [Impresiones y análisis](#impressions-and-analytics) |
| `triggers` faltantes o vacíos en los registros de eventos de usuario | [Solución de problemas de entrega](#delivery-troubleshooting) |
| Los desencadenantes se devolvieron pero nada se muestra en el dispositivo | [Solución de problemas de visualización específica por plataforma](#platform-specific-display-troubleshooting) |
| Los activos del mensaje dentro de la aplicación no se cargan (iOS, `NSURLError` -1008) | [Carga de activos (pestaña Swift)](?sdktab=swift#swift_asset-loading) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Síntoma de mensaje dentro de la aplicación" }

## Ruta de investigación estándar {#standard-investigation-path}

Usa este flujo de trabajo para cada incidente. Comienza en el paso 1.

1. Confirma que se registra un **inicio de sesión** para el dispositivo de prueba. Los mensajes dentro de la aplicación se solicitan al inicio de sesión.
2. Abre los [registros de eventos de usuario]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) y busca la solicitud del SDK para ese inicio de sesión. En **Response Data**:
   - En el JSON sin procesar, confirma que `respond_with` incluye `"triggers": true`.
   - La fila **Requested Responses** debe incluir **`triggers`**.
   - Las filas **Trigger In-App Message** enumeran cada mensaje dentro de la aplicación devuelto para esa solicitud.
   - Si no hay una clave `triggers` ni filas **Trigger In-App Message**, ve a [Solución de problemas de mensajes no solicitados](#troubleshoot-messages-not-being-requested).
   - Si `triggers` está presente pero vacío (`[]`), ve a [Solución de problemas de mensajes no devueltos](#troubleshoot-messages-not-being-returned).
   - Si hay filas **Trigger In-App Message** pero nada se muestra, ve a [Solución de problemas de visualización específica por plataforma](#platform-specific-display-troubleshooting).
   - Cada carga útil de desencadenante incluye un `type`: `inapp` (estándar) o `templated_iam` (requiere una solicitud de plantilla antes de mostrarse). Consulta [Tipos de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#types-of-in-app-messages).
3. Para la elegibilidad del lado del panel (Segment, reelegibilidad, límites de frecuencia, prioridad, grupos de control), consulta [Solución de problemas de entrega](#delivery-troubleshooting) y las [preguntas frecuentes sobre mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).
4. Para problemas de visualización del lado del dispositivo (delegados, límites de velocidad, orientación, tiempo de espera de sesión), selecciona la pestaña de tu SDK en [Solución de problemas de visualización específica por plataforma](#platform-specific-display-troubleshooting).

## Mensajes dentro de la aplicación en Canvas {#canvas-in-app-messages}

**Síntoma:** Un usuario entró en un paso de mensaje dentro de la aplicación en Canvas pero no vio el mensaje cuando se esperaba.

Tres comportamientos generan la mayoría de los tickets de Canvas y mensajes dentro de la aplicación:

1. **Visualización en la siguiente sesión:** Los mensajes dentro de la aplicación en Canvas son elegibles en el *siguiente* inicio de sesión después de que se procese el paso, no inmediatamente a mitad de sesión. Consulta [¿Cuándo se envían los mensajes dentro de la aplicación en Canvas?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent) en las preguntas frecuentes de Canvas.
2. **Validaciones de entrega en la entrada del paso:** Si **Validar audiencia al enviar el mensaje** está habilitado en el paso de mensaje, la pertenencia al Segment y los límites de frecuencia se evalúan cuando el usuario **entra en el paso**, no en el momento de la visualización. Consulta [Validaciones de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).
3. **Retraso y tiempo de espera de sesión:** Si un usuario entra en un paso de retraso más largo que el tiempo de espera de sesión de tu SDK, puede iniciar una nueva sesión antes del paso de mensaje dentro de la aplicación. Es posible que el mensaje no se obtenga en el inicio de sesión cuando esperas que se muestre.

Para ventanas de disponibilidad, expiración y cero _Envíos_ en los análisis de Canvas, consulta [Mensajes dentro de la aplicación y entrega]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery) en las preguntas frecuentes de Canvas.

{% alert important %}
Los mensajes dentro de la aplicación en Canvas solo pueden ser desencadenados por eventos enviados a través del SDK, no por la REST API.
{% endalert %}

## El mensaje dentro de la aplicación no se mostró para un usuario {#in-app-message-not-shown-for-one-user}

**Síntoma:** Un usuario no recibió un mensaje dentro de la aplicación esperado; otros usuarios pueden no estar afectados.

Comprueba lo siguiente:

- ¿Estaba el usuario en el Segment al **inicio de sesión**, cuando el SDK solicita nuevos mensajes dentro de la aplicación?
- ¿Era el usuario elegible o reelegible según las reglas de segmentación de la Campaign o Canvas? Consulta [Reelegibilidad para Campaigns y Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).
- ¿Se aplicó un [límite de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)?
- ¿Estaba el usuario en un grupo de control de la Campaign? Comprueba si la Campaign está configurada para pruebas A/B.
- ¿Se mostró en su lugar un mensaje dentro de la aplicación de mayor prioridad? Consulta [¿Pueden mostrarse varios mensajes dentro de la aplicación en la misma sesión?]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session) en las preguntas frecuentes de In-App Messages.
- ¿Estaba el dispositivo en la orientación especificada por la Campaign?
- ¿Fue suprimido el mensaje por el intervalo mínimo predeterminado de 30 segundos entre desencadenantes? Consulta [Anular el límite de velocidad predeterminado]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#overriding-the-default-rate-limit).

Luego sigue la [ruta de investigación estándar](#standard-investigation-path).

## El mensaje dentro de la aplicación no se mostró en una plataforma {#in-app-message-not-shown-on-one-platform}

**Síntoma:** Los mensajes dentro de la aplicación no se muestran en Android, iOS o Web, pero pueden funcionar en otras plataformas.

| Causa probable | Qué comprobar |
| --- | --- |
| Objetivo de **Send To** incorrecto | Confirma que la Campaign o el paso de Canvas apunta a **Mobile Apps** o **Web Browsers** según corresponda. Una Campaign solo para Web no se enviará a dispositivos Android. |
| Una UI personalizada o un controlador suprime la visualización | Revisa los delegados (móvil) o [`braze.subscribeToInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) (Web). Consulta [Personalización]({{site.baseurl}}/developer_guide/in_app_messages/customization) y la pestaña de tu SDK para tu plataforma. |
| La integración nunca funcionó en esta plataforma | Confirma que esta plataforma y versión de la aplicación han mostrado mensajes dentro de la aplicación anteriormente. |
| El desencadenante no se activó en el dispositivo | El desencadenante debe ocurrir localmente a través del SDK. Una llamada a la REST API no puede desencadenar un mensaje dentro de la aplicación en el SDK. Consulta [Desencadenar mensajes]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages). |
| `triggers` vacíos en los registros de eventos de usuario | Segment, reelegibilidad, límite de frecuencia o grupo de control. Consulta [Solución de problemas de mensajes no devueltos](#troubleshoot-messages-not-being-returned). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Causa del síntoma por plataforma" }

## El mensaje dentro de la aplicación no se mostró para ningún usuario {#in-app-message-not-shown-for-all-users}

**Síntoma:** Ningún usuario o menos usuarios de los esperados recibieron el mensaje dentro de la aplicación.

Comprueba lo siguiente:

- ¿Está la acción desencadenante configurada correctamente en el panel y en la integración de la aplicación?
- ¿Interceptó un mensaje dentro de la aplicación de mayor prioridad la Campaign? Consulta las [preguntas frecuentes sobre In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session).
- ¿Estás usando una versión reciente del SDK? Algunos tipos de mensajes dentro de la aplicación tienen requisitos mínimos de SDK.
- ¿Están las sesiones integradas correctamente? Confirma que los análisis de sesión funcionan para esta aplicación.
- ¿Está una biblioteca de UI personalizada interfiriendo con la visualización? Consulta [Personalización]({{site.baseurl}}/developer_guide/in_app_messages/customization).

Luego sigue la [ruta de investigación estándar](#standard-investigation-path).

## Temporización y visualización retrasada {#timing-and-delayed-display}

**Síntoma:** El mensaje dentro de la aplicación apareció más tarde de lo esperado o no hasta una nueva sesión.

Causas comunes:

- **Precarga en el inicio de sesión de la Campaign:** Los mensajes dentro de la aplicación se almacenan en caché al inicio de sesión y se muestran cuando se activa el desencadenante. Un desencadenante que ocurre antes del siguiente inicio de sesión no se mostrará hasta esa sesión. Consulta [Desencadenar mensajes]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages).
- **Comportamiento de siguiente sesión en Canvas:** Consulta [Mensajes dentro de la aplicación en Canvas](#canvas-in-app-messages).
- **Retraso planificado en el panel:** Confirma si hay un retraso configurado en la Campaign o el paso.
- **Condiciones de carrera en la sincronización de desencadenantes:** Si los usuarios registran un evento inmediatamente después del inicio de sesión, es posible que los desencadenantes aún no se hayan sincronizado. Considera desencadenar a partir del inicio de sesión y segmentar por el evento deseado para que la entrega ocurra en la siguiente sesión después del evento.
- **Mensajes dentro de la aplicación secuenciales:** Si estás aplazando o restaurando mensajes en un recorrido, consulta [Aplazar mensajes dentro de la aplicación desencadenados]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages).
- **Activos grandes o CDN lento:** Optimiza las imágenes y el video para mensajes dentro de la aplicación HTML. En dispositivos móviles, las imágenes pueden descargarse antes de mostrarse en redes lentas; selecciona la pestaña de tu SDK para notas específicas de la plataforma.

{% alert note %}
Si tu mensaje dentro de la aplicación se desencadena por el inicio de sesión y has configurado un tiempo de espera de sesión extendido, cerrar y volver a abrir la aplicación dentro de esa ventana no actualizará la sesión. Por ejemplo, con un tiempo de espera de 300 segundos, un mensaje dentro de la aplicación desencadenado por inicio de sesión no se mostrará hasta que la sesión se actualice realmente. Ajusta el tiempo de espera de sesión o el tipo de desencadenante si esto afecta tu prueba.
{% endalert %}

## Solución de problemas de entrega {#delivery-troubleshooting}

La mayoría de los problemas con mensajes dentro de la aplicación son de **entrega** (el dispositivo no recibió los desencadenantes) o de **visualización** (los desencadenantes llegaron pero no se mostraron). Confirma primero la [entrega](#troubleshooting-in-app-message-delivery) y luego comprueba la [visualización](#platform-specific-display-troubleshooting).

### Solución de problemas de entrega {#troubleshooting-in-app-message-delivery}

El SDK solicita mensajes dentro de la aplicación a los servidores de Braze al inicio de sesión. Confirma que el SDK está solicitando desencadenantes y que Braze los está devolviendo.

#### Comprueba si los mensajes se solicitan y se devuelven {#check-if-messages-are-requested-and-returned}

1. Añádete como [usuario de prueba]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users).
2. Configura una Campaign de mensaje dentro de la aplicación dirigida a tu usuario.
3. Inicia una nueva sesión en tu aplicación.
4. En los [registros de eventos de usuario]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log), busca la solicitud del SDK para el evento de inicio de sesión. En **Response Data**:
   - En el JSON sin procesar, confirma que `respond_with` incluye `"triggers": true`.
   - La fila **Requested Responses** enumera las claves de nivel superior en la respuesta. Para mensajes dentro de la aplicación, espera **`triggers`**.
   - Las filas **Trigger In-App Message** enumeran cada mensaje dentro de la aplicación devuelto para esa solicitud.

   Luego clasifica:
   - Si no hay una clave `triggers` ni filas **Trigger In-App Message**, consulta [Solución de problemas de mensajes no solicitados](#troubleshoot-messages-not-being-requested).
   - Si `triggers` está presente pero vacío (`[]`), consulta [Solución de problemas de mensajes no devueltos](#troubleshoot-messages-not-being-returned).
   - Si hay filas **Trigger In-App Message** pero nada se muestra en el dispositivo, consulta [Solución de problemas de visualización específica por plataforma](#platform-specific-display-troubleshooting).
   - Cada carga útil de desencadenante incluye un `type`: `inapp` (estándar) o `templated_iam` (requiere una solicitud de plantilla antes de mostrarse). Consulta [Tipos de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#types-of-in-app-messages).
5. Confirma que los mensajes dentro de la aplicación correctos aparecen en los datos de respuesta.

![Registro de eventos de usuario con solicitudes del SDK y datos de respuesta.]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### Solución de problemas de mensajes no solicitados {#troubleshoot-messages-not-being-requested}

Si los mensajes dentro de la aplicación no se están solicitando, es posible que tu aplicación no esté rastreando las sesiones correctamente; los mensajes dentro de la aplicación se actualizan al inicio de sesión. Confirma que la aplicación está iniciando una sesión según la semántica de tiempo de espera de sesión:

![La solicitud del SDK encontrada en los registros de eventos de usuario mostrando un evento de inicio de sesión exitoso.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### Solución de problemas de mensajes no devueltos {#troubleshoot-messages-not-being-returned}

Si los mensajes dentro de la aplicación no se están devolviendo, es probable que haya un problema de segmentación o elegibilidad:

1. Tu Segment no contiene a tu usuario.
   - Comprueba la pestaña [**Interacción**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab) del usuario para el Segment esperado.
2. Tu usuario ya recibió el mensaje y no era reelegible.
   - Comprueba la [configuración de reelegibilidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) y las [preguntas frecuentes sobre In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#campaigns).
3. Tu usuario alcanzó el límite de frecuencia.
   - Comprueba la [configuración de límites de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).
4. Tu usuario cayó en un grupo de control.
   - Crea un Segment con un filtro **Received campaign variant** establecido en **Control**, o excluye los grupos de control durante las pruebas de integración.
5. Un mensaje dentro de la aplicación de mayor prioridad tuvo precedencia. Consulta las [preguntas frecuentes sobre In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session).

Para Campaigns archivadas, configuración de desencadenantes y horas tranquilas, consulta las [preguntas frecuentes sobre In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

## Impresiones y análisis {#impressions-and-analytics}

**Síntoma:** Los recuentos de impresiones o clics no coinciden con las expectativas.

- **_Impresiones_ mayores que _Impresiones únicas_:** Es esperado cuando los usuarios tienen varios dispositivos o cuando un retraso planificado hace que el mismo usuario califique más de una vez. Consulta [Reelegibilidad para Campaigns y Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).
- **Impresiones menores de lo esperado:** Es posible que los usuarios no hayan visto el mensaje (las impresiones se registran al mostrarse), que varios mensajes de alta prioridad se intercepten entre sí, o que se apliquen condiciones de carrera en la sincronización de desencadenantes. Para mensajes dentro de la aplicación en Canvas, consulta [Mensajes dentro de la aplicación en Canvas](#canvas-in-app-messages). Para definiciones completas de métricas, consulta [Informes de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) y las [preguntas frecuentes sobre In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).
- **Impresiones menores que antes:** Revisa los registros de cambios del Segment y la Campaign. Confirma que no reutilizaste el mismo evento desencadenante en una Campaign de mayor prioridad.

![Enlace para ver el registro de cambios en la página de detalles de la Campaign con siete cambios desde la última vez que el usuario vio la Campaign.]({% image_buster /assets/img_archive/trouble4.png %})

Si usas un delegado o un controlador personalizado para mostrar mensajes dentro de la aplicación manualmente, debes registrar las impresiones y los clics tú mismo. Consulta la pestaña de tu SDK en [Solución de problemas de visualización específica por plataforma](#platform-specific-display-troubleshooting) para detalles de Swift y Android, o [Registrar datos de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data) para Web.

## Solución de problemas de visualización específica por plataforma {#platform-specific-display-troubleshooting}

Si aparecen filas **Trigger In-App Message** en los registros de eventos de usuario pero nada se muestra en el dispositivo, selecciona la pestaña de tu SDK para comprobaciones de visualización (delegados, límites de velocidad, orientación y controladores personalizados).

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/in_app_messages/troubleshooting.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/in_app_messages/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/in_app_messages/troubleshooting.md %}
{% endsdktab %}
{% endsdktabs %}