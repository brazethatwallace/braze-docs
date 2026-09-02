---
nav_title: Aprobaciones
article_title: Aprobaciones
page_order: 1
page_type: reference
description: "Este artículo de referencia ofrece un resumen de los distintos estados que pueden tener una campaña y un Canvas, y lo que significan."
tool:
    - Campaigns
    - Canvas
---

# Aprobaciones para campañas y Canvas {#approvals-for-campaigns-and-canvases}

> Usa las aprobaciones para añadir un punto de control final a tus campañas y Canvas antes del lanzamiento. Con este flujo de trabajo, puedes verificar y aprobar el contenido en todas las secciones requeridas de tu mensaje.

## Cómo funciona {#how-it-works}

Puedes revisar los detalles de tu Campaign o Canvas en el paso final de edición.

Tanto para Canvas como para Campaigns, debes guardar todos los cambios antes de aprobar, incluso si son tus propios cambios. Un usuario con los permisos adecuados debe aprobar cada sección del resumen antes de que el mensaje pueda lanzarse. El estado predeterminado de cada sección es **Pending Approval**.

{% tabs %}
{% tab campaign %}
Para lanzar una Campaign, debes aprobar estos componentes:

- **Messages:** Este es el mensaje de la Campaign.
- **Delivery:** Este es el tipo de entrega y determina cuándo los usuarios reciben la Campaign.
- **Target Audience:** Esto determina quién recibirá la Campaign.
- **Conversion Events:** Esta es la métrica que estás rastreando con fines de participación e informes.
{% endtab %}

{% tab Canvas %}
Para lanzar un Canvas, debes aprobar estos componentes clave:

- **Conversion Events:** Esta es la métrica que estás rastreando con fines de participación e informes.
- **Entry Schedule:** Esto incluye el tipo de horario de entrada y cuándo los usuarios entran al Canvas.
- **Target Audience:** Esto determina quién entrará en este Canvas.
- **Send Settings:** Estas son las opciones de envío para todos los pasos del Canvas.
- **Build Canvas:** Este es el recorrido del usuario en el Canvas.
{% endtab %}
{% endtabs %}

## Activar el flujo de trabajo de aprobación {#turning-on-the-approval-workflow}

De forma predeterminada, la configuración del flujo de trabajo de aprobación está desactivada para Campaigns y Canvas. Para activar esta característica, ve a **Configuración** > **Flujo de trabajo de aprobación** y selecciona la opción correspondiente:

- **Usar el flujo de trabajo de aprobación para todas las Campaigns en [tu espacio de trabajo]**
- **Usar el flujo de trabajo de aprobación para todos los Canvas en [tu espacio de trabajo]**

{% alert important %}
La aprobación de Campaigns no es compatible con las [campañas de API]({{site.baseurl}}/api/api_campaigns) ni con las [campañas de correo transaccional]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email).
{% endalert %}

## Configurar permisos de usuario {#setting-user-permissions}

Después de activar el flujo de trabajo de aprobación, debes configurar los permisos de usuario para que los usuarios de tu empresa puedan aprobar o rechazar Campaigns y Canvas. Ambos permisos también se pueden aplicar a espacios de trabajo o [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams), o añadirse a un [conjunto de permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#create-a-permission-set).

{% tabs %}
{% tab campaign %}
Debes tener el [permiso "Approve and Deny Campaigns"]({{site.baseurl}}/user_guide/administer/global/user_management/permissions). Este permiso controla quién puede actualizar el estado de aprobación de una Campaign. Con este permiso, puedes hacer lo siguiente:

- Autoaprobar la Campaign
- Aprobar y lanzar la Campaign
- Aprobar pero no lanzar la Campaign (un usuario diferente con el permiso "Send Campaigns, Canvases" puede lanzar la Campaign)
- No aprobar ni lanzar la Campaign

Después de que los estados de aprobación se establezcan en el paso **Summary**, cualquier cambio posterior realizado en la Campaign restablece todos los estados de aprobación al guardar. Esto se aplica a cualquier cambio realizado tanto en un borrador de Campaign como en una campaña posterior al lanzamiento. Por ejemplo, si solo realizas cambios en el público objetivo, el paso **Summary** revierte los estados de aprobación de todas las secciones al estado predeterminado, **Pending Approval**.

{% endtab %}

{% tab Canvas %}
Debes tener el [permiso "Approve and Deny Canvases"]({{site.baseurl}}/user_guide/administer/global/user_management/permissions). Este permiso controla quién puede actualizar el estado de aprobación de un Canvas. Con este permiso, puedes hacer lo siguiente:

- Autoaprobar el Canvas
- Aprobar y lanzar el Canvas
- Aprobar pero no lanzar el Canvas (un usuario diferente con el permiso "Send Campaigns, Canvases" puede lanzar el Canvas)
- No aprobar ni lanzar el Canvas

Después de que los estados de aprobación se establezcan en el paso **Summary**, cualquier cambio posterior realizado en el Canvas restablece todos los estados de aprobación al guardar. Esto se aplica a cualquier cambio realizado tanto en un borrador de Canvas como en un Canvas posterior al lanzamiento. Por ejemplo, si solo realizas cambios en el público objetivo, el paso **Summary** revierte los estados de aprobación de todas las secciones al estado predeterminado, **Pending Approval**.

{% alert note %}
**Estado de aprobación y guardado**

- Cuando haces clic en **Approve** en una sección del paso **Summary**, esa aprobación se guarda inmediatamente.
- El botón **Save** guarda los cambios en el contenido y la configuración del Canvas, no el estado de aprobación.

Para evitar perder aprobaciones:

1. Realiza las ediciones que necesites en el Canvas y luego haz clic en **Save**.
2. Después de que el Canvas termine de guardarse, aprueba las secciones relevantes en el paso **Summary**.
3. Haz clic en **Save** de nuevo solo si realizas cambios adicionales en el Canvas después de la aprobación. Si cambias el Canvas y guardas, todos los estados de aprobación se restablecen a **Pending Approval**.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert important %}
Para editar una campaña en vivo, necesitas el permiso "Approve and Deny Campaigns". Un usuario debe aprobar sus cambios porque aún no está disponible una versión en borrador de las Campaigns. Este no es el caso para Canvas, ya que un usuario puede realizar cambios y guardar como borrador, y otro usuario puede aprobar y lanzar el Canvas.
{% endalert %}