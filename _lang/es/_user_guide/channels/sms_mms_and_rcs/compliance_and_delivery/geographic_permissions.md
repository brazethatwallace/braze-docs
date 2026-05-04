---
nav_title: "Permisos geográficos"
article_title: "Permisos geográficos"
description: "Este artículo cubre la lista de países permitidos para los permisos geográficos, que te permite elegir a qué países se pueden entregar SMS, MMS y RCS."
page_order: 4
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/

---

# Permisos geográficos {#geographic-permissions}

> Los permisos geográficos mejoran la seguridad y protegen contra el tráfico fraudulento de SMS, MMS y RCS al aplicar controles sobre los países a los que puedes enviar mensajes. Puedes especificar una lista de países permitidos para asegurarte de que los mensajes SMS, MMS y RCS solo se envíen a regiones aprobadas. Solo los administradores pueden realizar cambios en la lista de países permitidos. Los usuarios que no son administradores tienen acceso a una versión de solo lectura de la lista que indica a qué países puede enviar un grupo de suscripción.

Si eres administrador, puedes configurar los países que están en la lista de permitidos. La lista de países permitidos se configura a nivel de [grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups/). Puedes acceder a ella yendo a **Audience** > **Subscriptions** y seleccionando un grupo de suscripción de SMS, MMS o RCS. La lista de permitidos se encuentra en **Geographic Permissions**.

![La sección editable de permisos geográficos de SMS para un administrador con varios países seleccionados en la "lista de países permitidos".]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

### Seleccionar países {#selecting-countries}

Añade países a la lista de permitidos con el menú desplegable. Los países más comunes de SMS y RCS se muestran en la parte superior, con los demás debajo. También puedes buscar países escribiendo en el campo de texto.

![El menú desplegable de la "lista de países permitidos" con los países más comunes mostrándose en la parte superior.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

Elimina países previamente seleccionados desmarcando las casillas correspondientes junto a ellos.

### Guardar tus cambios {#saving-your-changes}

Los cambios entrarán en vigor después de que selecciones **Save**. Eliminar países de tu lista de permitidos impedirá que todos los mensajes SMS, MMS y RCS se envíen a números en esos países.

![Modal de advertencia que confirma los países que se eliminarán de la lista de permitidos.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## Países de riesgo alto {#high-risk-countries}

Ciertos países tienen un mayor riesgo de bombeo de tráfico de SMS y RCS. Estos países se indican con una etiqueta de **High Risk** en el menú desplegable de países.

![El menú desplegable de países con Azerbaiyán mostrando una etiqueta de "High Risk".]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

Si permites el envío a estos países, primero debes reconocer el riesgo de hacerlo antes de que el país se añada a tu lista de permitidos.

{% alert note %}
Limita los países en tu lista de permitidos solo a aquellos necesarios para respaldar tus necesidades comerciales. Esto minimizará tu potencial de tráfico fraudulento. Para más orientación sobre cómo prevenir el bombeo de tráfico de SMS, consulta las [preguntas frecuentes sobre fraude de bombeo de tráfico de SMS]({{site.baseurl}}/sms_traffic_pumping_fraud/).
{% endalert %}

## Visibilidad de envíos bloqueados {#visibility-of-blocked-sends}

Los intentos de envío a países que no están en tu lista de permitidos serán cancelados. Los mensajes cancelados se registrarán en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) y dentro del [evento de interacción de mensajes SMS cancelados]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).

Los mensajes cancelados causados por envíos bloqueados se muestran como **Aborted Message Errors** y tienen el mensaje "The recipient's phone number is in a blocked country".

![Registro de cancelaciones que muestra varios envíos de SMS que fueron bloqueados porque el número de teléfono está en un país bloqueado.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}