---
page_order: 10.9
nav_title: Solución de problemas
article_title: Solución de problemas de notificaciones push para el SDK de Braze
description: "Diagnostica problemas de entrega y visualización de notificaciones push utilizando un índice de síntomas, una ruta de investigación estándar y comprobaciones específicas del SDK por plataforma."
channel:
  - push notifications
---

# Solución de problemas de notificaciones push {#troubleshoot-push-notifications}

> Usa esta página para diagnosticar problemas de entrega y visualización de notificaciones push en un dispositivo. Para comprobaciones de entrega del lado del panel (estado de suscripción, Segments, límites), consulta [Solución de problemas de push]({{site.baseurl}}/user_guide/channels/push/troubleshooting).

Antes de depurar, añádete como [usuario de prueba]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users) y revisa [Envío de mensajes de prueba]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages).

## Empieza aquí: identifica tu síntoma {#start-here-match-your-symptom}

Busca el comportamiento que estás viendo en la tabla y sigue los pasos de esa sección. Si no tienes claro qué sección aplica, utiliza la [ruta de investigación estándar](#standard-investigation-path).

| Síntoma | Ir a |
| --- | --- |
| Push no recibido en una plataforma | Selecciona la pestaña de tu SDK en [Solución de problemas específica de la plataforma](#platform-specific-troubleshooting) |
| Los saltos de línea alrededor de las etiquetas de Liquid se ven mal al guardar | [Saltos de línea en las notificaciones push](#push-linebreaks) |
| Comprobaciones de entrega en el panel (suscripción, Segment, límites) | [Solución de problemas de push]({{site.baseurl}}/user_guide/channels/push/troubleshooting) |
| El vínculo profundo desde push no se abre correctamente | [Solución de problemas de vinculación en profundidad]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting) |
| Códigos de error push comunes | [Mensajes de error push comunes]({{site.baseurl}}/user_guide/channels/push/push_error_codes) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Síntoma de push del SDK" }

## Ruta de investigación estándar {#standard-investigation-path}

Usa este flujo de trabajo para cada incidente de notificaciones push. Comienza en el paso 1.

1. Confirma que el dispositivo tiene un token de notificaciones push válido y que el permiso push está concedido en la configuración del dispositivo.
2. En el panel, confirma que el usuario de prueba coincide con el [Segment]({{site.baseurl}}/user_guide/channels/push/troubleshooting#segment) de la Campaign o Canvas y que no está en el [grupo de control]({{site.baseurl}}/user_guide/channels/push/troubleshooting#control-group-status).
3. Envía una [notificación push de prueba]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages) al dispositivo de prueba.
4. [Habilita el registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduce el problema y revisa la guía específica de la plataforma en tu [pestaña del SDK](#platform-specific-troubleshooting).
5. Si el problema persiste, ponte en contacto con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) con los registros detallados, la plataforma, la versión del SDK y el ID de la Campaign o Canvas.

## Los clics en push no se registran {#push-clicks-not-logged}

- Asegúrate de haber seguido los [pasos de integración push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling).
- Braze no gestiona las notificaciones push recibidas silenciosamente en primer plano (comportamiento predeterminado de push en primer plano antes del framework `UserNotifications`). Esto significa que los enlaces no se abrirán y los clics en push no se registrarán. Si tu aplicación aún no ha integrado el framework `UserNotifications`, Braze no gestionará las notificaciones push cuando el estado de la aplicación sea `UIApplicationStateActive`. Asegúrate de que tu aplicación no retrase las llamadas a los [métodos de gestión push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling); de lo contrario, el SDK de Swift puede tratar las notificaciones push como eventos push silenciosos en primer plano y no gestionarlos.

## Saltos de línea en las notificaciones push {#push-linebreaks}

Al redactar notificaciones push con etiquetas de Liquid, los saltos de línea adyacentes a las etiquetas de Liquid se eliminan automáticamente antes de que se envíe el mensaje. En el [creador de notificaciones push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message), estos saltos de línea se vuelven a añadir para que tu mensaje siga siendo legible mientras lo editas. Si notas saltos de línea alrededor de las etiquetas de Liquid al guardar tu mensaje, se trata de un comportamiento esperado.