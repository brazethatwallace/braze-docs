---
nav_title: "Permisos geográficos"
article_title: "Permisos geográficos"
description: "Este artículo cubre la lista de países permitidos para los permisos geográficos, que te permite elegir a qué países se pueden entregar servicio de mensajes cortos, MMS y RCS."
page_order: 0
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/

---

# Permisos geográficos {#geographic-permissions}

> Los permisos geográficos mejoran la seguridad y protegen contra el tráfico fraudulento de servicio de mensajes cortos, MMS y RCS al aplicar controles sobre los países a los que puedes enviar mensajes. Puedes especificar una lista de países permitidos para enviar mensajes servicio de mensajes cortos, MMS y RCS solo a regiones aprobadas. Los mensajes solo se envían a números de teléfono con los códigos de marcación de esos países.<br><br> Solo los administradores pueden realizar cambios en la lista de países permitidos. Los usuarios que no son administradores tienen acceso a una versión de solo lectura de la lista que indica a qué países puede enviar un grupo de suscripción.

Si eres administrador, puedes configurar los países que están en la lista de permitidos. La lista de países permitidos se configura a nivel de [grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups). Puedes acceder a ella yendo a **Audiencia** > **Administración del grupo de suscripción** y seleccionando un grupo de suscripción de servicio de mensajes cortos, MMS o RCS. La lista de permitidos se encuentra en **Permisos geográficos**.

![La sección editable de permisos geográficos para un administrador con varios países seleccionados en la "lista de países permitidos".]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

## Selección de países {#selecting-countries}

Añade países a la lista de permitidos con el menú desplegable. Los países más comunes de servicio de mensajes cortos, MMS y RCS se muestran en la parte superior, y los demás aparecen en la sección siguiente. También puedes buscar países escribiendo en el campo de texto.

![El menú desplegable "Lista de países permitidos" con los países más comunes en la parte superior.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

Elimina los países seleccionados previamente desmarcando las casillas correspondientes junto a ellos.

### Guardar los cambios {#saving-your-changes}

Los cambios surten efecto después de guardarlos. Al eliminar países de tu lista de permitidos, se impide el envío de todos los mensajes servicio de mensajes cortos, MMS y RCS a números de teléfono con los códigos de marcación de esos países.

![Modal de advertencia que confirma los países que se eliminarán de la lista de permitidos.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## Países con alto riesgo de fraude {#high-fraud-risk-countries}

Ciertos países tienen un mayor riesgo de bombeo de tráfico de servicio de mensajes cortos, MMS y RCS. Estos países se indican con una etiqueta de **Alto riesgo de fraude** en el desplegable de países.

![El desplegable de países con Azerbaiyán mostrando una etiqueta de "Alto riesgo de fraude".]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

Si permites el envío a estos países, primero debes reconocer el riesgo de hacerlo antes de que el país se añada a tu lista de permitidos.

{% alert note %}
Limita los países de tu lista de permitidos solo a los necesarios para satisfacer tus necesidades empresariales. Esto minimiza tu potencial de tráfico fraudulento. Para obtener más orientación sobre cómo prevenir el bombeo de tráfico de servicio de mensajes cortos, MMS y RCS, consulta las [preguntas frecuentes sobre el fraude de bombeo de tráfico servicio de mensajes cortos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/sms_traffic_pumping_fraud).
{% endalert %}

## Visibilidad de envíos fuera de la lista de países permitidos {#visibility-of-sends-outside-the-allowlist}

Los intentos de envío a países que no están en tu lista de países permitidos se cancelarán. Los mensajes cancelados se registrarán en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) y en el [evento de participación de mensajes servicio de mensajes cortos cancelados]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

Los mensajes cancelados para destinatarios en países que no están en tu lista de permitidos se muestran como **Aborted Message Errors** y tienen el mensaje "The recipient's phone number is in a blocked country".

![Registro de cancelación que muestra varios envíos de SMS, MMS y RCS cancelados porque el país del número de teléfono no está en la lista de países permitidos.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}

## Aviso importante para países de alto riesgo de fraude y fraude de bombeo de tráfico {#important-notice-for-high-fraud-risk-countries-and-traffic-pumping-fraud}

### ¿Qué es el bombeo de tráfico de servicio de mensajes cortos, MMS y RCS? {#what-is-sms-mms-and-rcs-traffic-pumping}

El bombeo de tráfico de servicio de mensajes cortos, MMS y RCS (también conocido como tráfico inflado artificialmente) es un esquema de fraude en aumento que puede generar una exposición financiera significativa para los clientes. Los estafadores pueden explotar tus formularios web públicos desprotegidos, flujos de autenticación o endpoints de API para desencadenar grandes volúmenes de envíos de servicio de mensajes cortos, MMS y RCS (como confirmaciones de adhesión voluntaria, contraseñas de un solo uso o notificaciones) a números de teléfono que controlan o sobre los que tienen influencia. Los atacantes luego cobran una participación en los ingresos de redes móviles cómplices o desprevenidas por generar ese tráfico artificial. El impacto posterior introduce una exposición financiera significativa.

### ¿Qué son los países de alto riesgo de fraude? {#what-are-high-fraud-risk-countries}

Un país o territorio se designa como de alto riesgo de fraude si posee una densidad inusualmente alta de operadores locales de roaming de tarifa premium pequeños o carece de supervisión regulatoria estricta. Los actores maliciosos atacan sistemáticamente estas redes de operadores de alta tarifa porque maximizan el pago de participación en los ingresos por mensaje generado.

Además, las restricciones de enrutamiento del sistema se aplican en función de los códigos de país de destino en lugar de la ubicación física real del destinatario. Esto significa que si tienes clientes que viajan con frecuencia, no necesitas agregar sus ubicaciones de viaje a tu lista de países permitidos, ya que los mensajes se enrutarán según el código de país de destino original, no su ubicación física actual. Por ejemplo, los territorios que comparten un código de país con regiones de menor riesgo (como Jersey o Guernsey que comparten el código de país +44 con el Reino Unido) siguen teniendo una alta exposición a tarifas de operadores y se gestionan bajo las mismas condiciones del marco de alto riesgo de fraude.

### Responsabilidad del cliente y responsabilidad financiera {#customer-responsibility-and-financial-liability}

El cliente es responsable y será facturado por todos los mensajes móviles enviados a través de los servicios en su nombre, incluyendo cualquier mensaje resultante del bombeo de tráfico de servicio de mensajes cortos, MMS y RCS. Las salvaguardas de la plataforma, como la lista de países permitidos, te ayudan a restringir la entrega a regiones de confianza. Sin embargo, en última instancia, proteger tus endpoints expuestos externamente y prevenir daños financieros devastadores sigue siendo responsabilidad exclusiva del cliente.

### Cómo prevenir el bombeo de tráfico {#how-to-prevent-traffic-pumping}

No limitar la distribución de tus mensajes estrictamente a las regiones geográficas donde residen tus clientes reales crea una vulnerabilidad inmediata al fraude y un daño financiero grave. Para proteger tu empresa, debes restringir proactivamente tus regiones de entrega utilizando la lista de países permitidos. Además, y lo más importante, debes proteger cualquier formulario en línea de solicitud de número de teléfono o endpoint de API que desencadene envíos de servicio de mensajes cortos, MMS y RCS de acuerdo con las mejores prácticas de la industria, como se describe en [Comprender y prevenir el fraude de bombeo de tráfico de servicio de mensajes cortos, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/sms_traffic_pumping_fraud).