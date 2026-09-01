---
nav_title: Grupos de suscripción
article_title: Grupos de suscripción
page_order: 1
description: "Este artículo cubre los grupos de suscripción de mensajes LINE."
page_type: reference
channel:
 - LINE
alias: /line/subscription_groups/
---

# Grupos de suscripción de LINE {#line-subscription-groups}

> Hay dos estados de suscripción para los usuarios de LINE: suscrito y dado de baja. Cada grupo de suscripción está conectado a su propio canal de LINE. Para un resumen multicanal de los grupos de suscripción, consulta [Grupos de suscripción]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).

| Estado | Definición |
| --- | --- |
| Suscrito | El usuario siguió el canal de LINE desde su aplicación de LINE. Los usuarios se suscriben automáticamente cuando siguen el canal después de que hayas completado los pasos de integración. |
| Dado de baja | El usuario no siguió el canal de LINE desde su aplicación de LINE, o el usuario dejó de seguir explícitamente el canal de LINE. <br><br> Los usuarios dados de baja de un grupo de suscripción de LINE dejarán de recibir cualquier mensaje de LINE de los canales de envío que pertenezcan al grupo de suscripción. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Grupos de suscripción de LINE" }

## Configurar el grupo de suscripción de LINE de un usuario {#set-a-users-line-subscription-group}

LINE aloja el estado de suscripción de los usuarios. Braze procesa los eventos de seguimiento y cancelación de seguimiento que actualizan el estado de suscripción.

{% alert important %}
Los grupos de suscripción de LINE no se pueden mover entre espacios de trabajo. Si reintegras un canal de LINE en otro espacio de trabajo después de archivar su grupo de suscripción, Braze crea un nuevo grupo de suscripción en el espacio de trabajo de destino; el original permanece en el primer espacio de trabajo.
{% endalert %}

## Comportamiento del archivado {#archive-behavior}

- **Archivado estándar:** Si archivas un grupo de suscripción de LINE y no vuelves a integrar el canal en otro espacio de trabajo, puedes desarchivar el grupo de suscripción más tarde.
- **Archivado permanente:** Si vuelves a integrar el canal de LINE en un espacio de trabajo diferente después de archivar su grupo de suscripción, el grupo de suscripción original se archiva de forma permanente y no se puede desarchivar a través del panel.

Para conocer los pasos de reintegración del canal, consulta [Configuración de LINE]({{site.baseurl}}/user_guide/channels/line/line_setup#re-integrate-a-line-channel-in-another-workspace).