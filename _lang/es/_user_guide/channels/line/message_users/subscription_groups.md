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

> Hay dos estados de suscripción para los usuarios de LINE: suscrito y dado de baja. LINE puede tener hasta 100 grupos de suscripción por espacio de trabajo, y cada grupo de suscripción está conectado a su propio canal de LINE.

| Estado | Definición |
| --- | --- |
| Suscrito | El usuario siguió el canal de LINE desde su aplicación de LINE. Los usuarios se suscriben automáticamente cuando siguen el canal después de que hayas completado los pasos de integración. |
| Dado de baja | El usuario no siguió el canal de LINE desde su aplicación de LINE, o el usuario dejó de seguir explícitamente el canal de LINE. <br><br> Los usuarios dados de baja de un grupo de suscripción de LINE dejarán de recibir cualquier mensaje de LINE de los canales de envío que pertenezcan al grupo de suscripción. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE subscription groups" }

## Configurar el grupo de suscripción de LINE de un usuario {#setting-a-users-line-subscription-group}

LINE aloja el estado de suscripción de los usuarios. Braze procesa los eventos de seguimiento y cancelación de seguimiento que actualizan el estado de suscripción.