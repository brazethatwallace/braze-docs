---
nav_title: "Permisos geográficos"
article_title: "Permisos geográficos"
description: "Este artículo cubre la lista de países permitidos para los permisos geográficos, que te permite elegir a qué países se pueden entregar SMS, MMS y RCS."
page_order: 0
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/

---

# Permisos geográficos {#geographic-permissions}

> Los permisos geográficos mejoran la seguridad y protegen contra el tráfico fraudulento de SMS, MMS y RCS al aplicar controles sobre los países a los que puedes enviar mensajes. Puedes especificar una lista de países permitidos para enviar mensajes SMS, MMS y RCS solo a regiones aprobadas. Los mensajes solo se envían a números de teléfono con los códigos de marcación de esos países.<br><br> Solo los administradores pueden realizar cambios en la lista de países permitidos. Los usuarios que no son administradores tienen acceso a una versión de solo lectura de la lista que indica a qué países puede enviar un grupo de suscripción.

Si eres administrador, puedes configurar los países que están en la lista de permitidos. La lista de países permitidos se configura a nivel de [grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups). Puedes acceder a ella yendo a **Audiencia** > **Administración del grupo de suscripción** y seleccionando un grupo de suscripción de SMS, MMS o RCS. La lista de permitidos se encuentra en **Geographic Permissions**.

![La sección editable de permisos geográficos para un administrador con varios países seleccionados en la "lista de países permitidos".]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

## Seleccionar países {#selecting-countries}

Añade países a la lista de permitidos con el menú desplegable. Los países más comunes de SMS, MMS y RCS se muestran en la parte superior, y los demás aparecen en la sección siguiente. También puedes buscar países escribiendo en el campo de texto.

![El menú desplegable de la "lista de países permitidos" con los países más comunes en la parte superior.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

Elimina países previamente seleccionados desmarcando las casillas correspondientes junto a ellos.

### Guardar los cambios {#saving-your-changes}

Los cambios entrarán en vigor después de guardar. Eliminar países de tu lista de permitidos impedirá que todos los mensajes SMS, MMS y RCS se envíen a números de teléfono con los códigos de marcación de esos países.

![Modal de advertencia que confirma los países que se eliminarán de la lista de permitidos.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## Países con alto riesgo de fraude {#high-fraud-risk-countries}

Ciertos países tienen un mayor riesgo de bombeo de tráfico de SMS, MMS y RCS. Estos países se indican con una etiqueta de **High Fraud Risk** en el menú desplegable de países.

![El menú desplegable de países con Azerbaiyán mostrando una etiqueta de "High Fraud Risk".]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

Si permites el envío a estos países, primero debes reconocer el riesgo de hacerlo antes de que el país se añada a tu lista de permitidos.

{% alert note %}
Limita los países en tu lista de permitidos solo a aquellos necesarios para respaldar las necesidades de tu negocio. Esto minimizará tu potencial de tráfico fraudulento. Para más orientación sobre cómo prevenir el bombeo de tráfico de SMS, MMS y RCS, consulta [Preguntas frecuentes sobre el fraude de bombeo de tráfico de SMS]({{site.baseurl}}/sms_traffic_pumping_fraud).
{% endalert %}

## Visibilidad de envíos fuera de la lista de permitidos {#visibility-of-sends-outside-the-allowlist}

Los intentos de envío a países que no están en tu lista de países permitidos serán cancelados. Los mensajes cancelados se registrarán en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) y dentro del [evento de participación de mensajes SMS cancelados]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

Los mensajes cancelados para destinatarios en países que no están en tu lista de permitidos se muestran como **Aborted Message Errors** y tienen el mensaje "The recipient's phone number is in a blocked country".

![Registro de cancelaciones que muestra varios envíos de SMS, MMS y RCS cancelados porque el país del número de teléfono no está en la lista de países permitidos.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}

## Aviso importante sobre países con alto riesgo de fraude y fraude de bombeo de tráfico {#important-notice-for-high-fraud-risk-countries-and-traffic-pumping-fraud}

### ¿Qué es el bombeo de tráfico de SMS, MMS y RCS? {#what-is-sms-mms-and-rcs-traffic-pumping}

El bombeo de tráfico de SMS, MMS y RCS (también conocido como tráfico inflado artificialmente) es un esquema de fraude en aumento que puede resultar en una exposición financiera significativa para los clientes. Los estafadores pueden explotar tus formularios web públicos desprotegidos, flujos de autenticación o endpoints de API para desencadenar grandes volúmenes de envíos de SMS, MMS y RCS (como confirmaciones de adhesión voluntaria, contraseñas de un solo uso o notificaciones) a números de teléfono que controlan o influyen. Los atacantes luego cobran una participación en los ingresos de redes móviles cómplices o desprevenidas por generar ese tráfico artificial. El impacto posterior introduce una exposición financiera significativa.

### ¿Qué son los países con alto riesgo de fraude? {#what-are-high-fraud-risk-countries}

Un país o territorio se designa como de alto riesgo de fraude si posee una densidad inusualmente alta de operadores locales pequeños de itinerancia con tarifas premium o carece de una supervisión regulatoria estricta. Los actores malintencionados atacan sistemáticamente estas redes de operadores con tarifas altas porque maximizan el pago de participación en los ingresos por mensaje generado.

Además, las restricciones de enrutamiento del sistema se aplican en función de los códigos de país de destino en lugar de la ubicación física real del destinatario. Esto significa que si tienes clientes que viajan con frecuencia, no necesitas añadir sus ubicaciones de viaje a tu lista de países permitidos, ya que los mensajes se enrutarán según el código de país de destino original, no su ubicación física actual. Por ejemplo, los territorios que comparten un código de país con regiones de menor riesgo (como Jersey o Guernsey que comparten el código de país +44 con el Reino Unido) aún conllevan una alta exposición a tarifas de operadores y se gestionan bajo estas mismas condiciones del marco de alto riesgo de fraude.

### Responsabilidad del cliente y responsabilidad financiera {#customer-responsibility-and-financial-liability}

El cliente es responsable y se le facturará por todos los mensajes móviles enviados a través de los servicios en su nombre, incluidos los mensajes resultantes del bombeo de tráfico de SMS, MMS y RCS. Las medidas de seguridad de la plataforma, como la lista de países permitidos, te ayudarán a restringir la entrega a regiones de confianza. Sin embargo, en última instancia, proteger tus endpoints externos y prevenir daños financieros devastadores sigue siendo responsabilidad exclusiva del cliente.

### Cómo prevenir el bombeo de tráfico {#how-to-prevent-traffic-pumping}

No limitar la distribución de tus mensajes estrictamente a las regiones geográficas donde residen tus clientes reales crea una vulnerabilidad inmediata al fraude y un daño financiero grave. Para proteger tu empresa, debes restringir proactivamente tus regiones de entrega utilizando la lista de países permitidos. Además, y lo más importante, debes proteger cualquier formulario de solicitud de número de teléfono en línea o endpoint de API que desencadene envíos de SMS, MMS y RCS de acuerdo con las mejores prácticas de la industria, como se describe en [Comprender y prevenir el fraude de bombeo de tráfico de SMS, MMS y RCS]({{site.baseurl}}/sms_traffic_pumping_fraud).