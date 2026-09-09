---
nav_title: Octubre
page_order: 4
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de octubre de 2018."
---
# Octubre de 2018 {#october-2018}

{% comment %}
  Añádelos más adelante...
  Alternar grupo de control de Intelligent Selection
  El cuadro Selección Inteligente tiene ahora una casilla de verificación que te permite [alternar entre activar o desactivar el uso de un grupo de control]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing#including-a-control-group). Cuando esté activado, el grupo de control será el 20% del tamaño de la audiencia y cambiará a medida que la característica Intelligent Selection optimice los tamaños de audiencia por variante.
  Asistente de configuración de entrada en Canvas (Beta)
  La interfaz de usuario de Canvas se simplificará para evitar la omisión de tareas y los errores resultantes. Las configuraciones de Canvas, en concreto, se mostrarán ahora en un asistente, similar al diseño del asistente de campañas. Esto no se refleja actualmente en nuestra documentación, ya que se está implementando gradualmente. ¡Vuelve pronto para saber más sobre esto!
  API de grupo de suscripción (oculta)
  Braze ha puesto a tu disposición una nueva llamada GET para habilitar la solicitud basada en un ID externo o en una dirección de correo electrónico. A continuación, se te proporcionarán todos los grupos de suscripción asociados a ese usuario.
{% endcomment %}

## Calcular estadísticas exactas de audiencia para Campaigns {#calculate-exact-audience-stats-for-campaigns}

Ahora puedes ir a **Campaign Analytics** y calcular las estadísticas exactas de tu audiencia. Haz clic en **Calculate Exact Stats** en el pie de la sección **Target Audiences**, y se completarán las estadísticas exactas de audiencia. Tendrás que guardar la Campaign antes de calcularlas (las Campaigns en borrador se guardarán como borradores).

## Obsolescencia de Windows 8 {#windows-8-deprecation}

Braze dejó de ser compatible con Windows 8 a partir del 10 de octubre de 2018.

## Centro de partners {#partnerships-hub}

Ahora puedes encontrar una lista de tus integraciones en la plataforma Braze en **Integraciones**, junto con las claves de integración e instrucciones.

## Cálculos de análisis de correo electrónico {#email-analytics-calculations}

Braze ahora calcula todos los análisis de correo electrónico utilizando los datos de eventos de nuestro partner de envío de correo electrónico (ESP) para mejorar significativamente la precisión de nuestros análisis de correo electrónico. Esta solución utiliza Postgres, una solución de base de datos de código abierto, para garantizar la integridad de los datos.

{% alert important %}
Unique Opens y Unique Clicks actualmente siguen dependiendo de los datos agregados proporcionados por nuestros partners de envío de correo electrónico. Se está trabajando para calcular estas estadísticas de unicidad utilizando la misma infraestructura introducida en esta versión.
{% endalert %}

## Controles del panel del creador {#composer-panel-controls}

Los controles del creador de mensajes se han actualizado para incluir texto asociado a los iconos y así mejorar la usabilidad y la navegación.

## Azure para Currents {#azure-for-currents}

Los clientes de Braze que utilizan Currents ahora pueden ver [Azure]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents) como una integración potencial.

## Expansiones del campo de entrada {#input-field-expansions}

Ahora puedes expandir los cuadros de entrada para las líneas del asunto del correo electrónico y los títulos push.