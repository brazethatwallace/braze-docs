---
nav_title: Crear una campaña
article_title: Crear una campaña
page_order: 1
page_type: tutorial
description: "Aprende a crear una campaña de mensajería en Braze, desde la redacción hasta el lanzamiento, incluyendo envíos multicanal, y cómo planificar la entrega, segmentar audiencias, asignar eventos de conversión, enviar pruebas y lanzar."
tool: Campaigns
---

# Crear una campaña {#create-a-campaign}

> Utiliza campañas cuando quieras llegar a los consumidores con un solo paso de mensajería a través de uno o más canales compatibles. Para recorridos de varios pasos, utiliza [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/).

## Requisitos previos {#prerequisites}

Para crear y lanzar una campaña, necesitas los permisos "Editar campañas" y "Lanzar campañas". Para ver una lista completa de los permisos del espacio de trabajo y cómo aparecen en el dashboard, consulta [Permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/).

### Antes de empezar {#before-you-begin}

- Crea o elige los [segmentos]({{site.baseurl}}/user_guide/audience/segments/) que definen quién debe recibir tus mensajes.
- Revisa los [conceptos básicos de campañas]({{site.baseurl}}/user_guide/messaging/campaigns/campaign_basics/) para que los canales de mensajería, los tipos de entrega y los objetivos de conversión se alineen con tu caso de uso.
- Para un recorrido guiado sobre entrega, segmentación y conversiones, realiza el curso de Braze Learning [Configuración de campañas](https://learning.braze.com/campaign-setup-delivery-targeting-conversions).

## Compositor de campañas {#campaign-composer}

El compositor de campañas es donde defines la entrega, las audiencias, las conversiones y la configuración de lanzamiento. Decide si vas a crear una campaña de un solo canal o multicanal antes de continuar.

{% tabs %}
{% tab Un solo canal %}

Una campaña de un solo canal llega a los usuarios a través de un canal de mensajería por lanzamiento.

### Qué es diferente {#whats-different}

#### Conversiones e informes {#single-channel-conversions}

Para campañas de un solo canal, Braze realiza el seguimiento de los [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) que asignas a la campaña en relación con los envíos de ese canal. Para las ventanas de atribución y las reglas de conteo, consulta [Reglas de seguimiento de conversiones]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/#conversion-tracking-rules).

La [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/) del espacio de trabajo y los límites de envío siguen aplicándose.

### Crear una campaña de un solo canal {#create-a-single-channel-campaign}

Para crear una campaña:

1. Ve a **Messaging** > **Campaigns**.
2. Selecciona **Create Campaign**.
3. Selecciona el [canal]({{site.baseurl}}/user_guide/channels/) que se ajuste a tu caso de uso.
4. En el [paso Redactar](#step-1-compose-messages), escribe y previsualiza el contenido para ese canal.

Cada campaña utiliza un tipo de canal a la vez. Añade variantes cuando quieras comparar divisiones creativas o ejecutar [pruebas A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% endtab %}
{% tab Multicanal %}

Una campaña multicanal llega a los usuarios a través de más de un canal de mensajería en un solo lanzamiento. Por ejemplo, enviar un correo electrónico y una notificación push juntos.

{% alert note %}
Los [mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/) no están disponibles en campañas multicanal. Crea una campaña de un solo canal o un Canvas en su lugar.
{% endalert %}

### Qué es diferente

#### Grupos de control {#multichannel-control-groups}

Los grupos de control de campañas comparan variantes dentro de un canal (por ejemplo, correo electrónico A frente a correo electrónico B). No se utilizan para comparar canales completos dentro de una campaña multicanal. Para probar canales, creatividades o tiempos juntos a lo largo de un recorrido, utiliza [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/).

#### Conversiones e informes {#multichannel-conversions}

Para campañas multicanal, Braze realiza el seguimiento de los [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) por canal. Cuando un usuario convierte después de recibir mensajes en más de un canal, Braze puede atribuir esa conversión a esos canales. Los recuentos de conversiones pueden superar a los *usuarios únicos*, y las tasas pueden superar el 100 %. Para las reglas completas, consulta [Reglas de seguimiento de conversiones]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/#conversion-tracking-rules).

Los límites de velocidad para envíos que abarcan canales se describen en [Campañas multicanal y Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#multichannel-campaigns-and-canvases). Para las reglas a nivel de espacio de trabajo (incluyendo cómo los envíos multicanal cuentan para los límites), consulta [Limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/).

### Crear una campaña multicanal {#create-a-multichannel-campaign}

1. Ve a **Messaging** > **Campaigns**.
2. Selecciona **Create Campaign**.
3. Selecciona **Multichannel**.
4. En el [paso Redactar](#step-1-compose-messages), selecciona **Add channel** y elige cada canal que necesites. Selecciona los iconos de canal para alternar entre compositores mientras redactas el contenido de cada canal.

{% endtab %}
{% endtabs %}

## Paso 1: Redactar mensajes {#step-1-compose-messages}

### Detalles de la campaña {#campaign-details}

Utiliza los siguientes campos para registrar metadatos que ayuden a tu equipo a encontrar y administrar la campaña.

| Campo | Propósito |
| --- | --- |
| Nombre | Usa un nombre claro que refleje el objetivo de la campaña. |
| Descripción | Opcional. Explica la intención o incluye enlaces a briefs para los colaboradores. |
| Equipo | Opcional. Asigna [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) para que los grupos adecuados puedan editar o generar informes sobre este envío. |
| Etiquetas | Opcional. Añade [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) para filtrar en listas y herramientas como el [Generador de informes]({{site.baseurl}}/user_guide/analytics/reports/report_builder/). |
| ID de campaña | Donde se muestre en el compositor o resumen, copia este identificador para llamadas a la API, informes e integraciones que hagan referencia a una campaña específica. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Detalles de la campaña" }

### Canales y editores {#channels-and-editors}

Redacta contenido específico del canal en este paso. Para una guía detallada, consulta [Canales]({{site.baseurl}}/user_guide/channels/) y abre el artículo del canal que seleccionaste.

### Variantes {#variants}

Añade variantes cuando quieras comparar divisiones creativas o de entrega. Para información sobre experimentos y controles, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% alert tip %}
Cuando cada variante utilice contenido similar, redacta el mensaje **antes** de añadir variantes adicionales. Luego usa **Copy from Variant** desde el menú **Add Variant** para reutilizar el trabajo entre variantes o canales.
{% endalert %}

## Paso 2: Planificar la entrega {#step-2-schedule-delivery}

Elige cuándo los usuarios se vuelven elegibles para recibir la campaña:

| Tipo de entrega | Resumen |
| --- | --- |
| [Entrega planificada]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery/) | Envía en un momento o cadencia especificados. |
| [Entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/) | Envía cuando los usuarios realizan comportamientos o cumplen condiciones que tú defines. |
| [Entrega activada por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/) | Envía cuando tus sistemas llaman a Braze para activar la campaña para los usuarios elegibles. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Planificar la entrega" }

Para conceptos de planificación en Braze, consulta [Planifica tu campaña]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).

### Controles de entrega {#delivery-controls}

Dependiendo del tipo de entrega, puedes ajustar la [reelegibilidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/) (si los usuarios pueden volver a entrar en la campaña) y respetar las reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/) del espacio de trabajo. También puedes configurar [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/) para que los mensajes no se envíen durante ventanas restringidas.

## Paso 3: Segmentar audiencias {#step-3-target-audiences}

En **Target Audiences**, define quién es elegible para recibir la campaña. Para todas las opciones de segmentación, recorridos de la interfaz y capturas de pantalla, consulta [Segmentar usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/).

### Opciones de segmentación {#targeting-options}

En esta sección, puedes segmentar usuarios eligiendo segmentos o filtros para delimitar tu audiencia. Los usuarios elegibles aún necesitan cumplir con el desencadenante o los criterios que definas en el paso **Planificación de entrega**. La audiencia objetivo es como una sala de espera: solo las personas que ya están dentro pueden avanzar cuando ocurre la siguiente acción.

Las [listas de supresión]({{site.baseurl}}/user_guide/audience/suppression_lists/) del espacio de trabajo excluyen automáticamente a los usuarios listados, a menos que permitas una excepción para esta campaña.

### Resumen de audiencia {#audience-summary}

Después de añadir segmentos o filtros, el **Resumen de audiencia** ofrece una vista previa de cómo se ve la población de ese segmento, incluyendo cuántos usuarios dentro de ese segmento son alcanzables a través de los canales seleccionados. Los recuentos de alcance reflejan los datos de tu espacio de trabajo, la configuración del canal y los filtros. Ten en cuenta que la membresía exacta del segmento siempre se calcula antes de que se envíe el mensaje. Para audiencias muy grandes, Braze puede mostrar estimaciones hasta que calcules las estadísticas exactas.

### Búsqueda de usuarios {#user-lookup}

Después de añadir segmentos o filtros, puedes comprobar si tu audiencia está configurada como se esperaba buscando un usuario para confirmar si coincide con los criterios del segmento. Para hacerlo, busca el `external_id` o `braze_id` de un usuario en la sección **User Lookup**. No puedes buscar por dirección de correo electrónico aquí. Consulta [Probar segmentos]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#testing-segments) para más información.

Cuando un usuario coincide con los criterios del segmento, filtro y aplicación, una alerta lo indica. Cuando un usuario no coincide con parte o la totalidad de los criterios del segmento, filtro o aplicación, se listan los criterios faltantes para fines de solución de problemas.

### Enviar a estos usuarios {#send-to-these-users}

Para canales basados en suscripción (correo electrónico, SMS y similares), usa **Send to these users** para enviar tu campaña solo a usuarios que tengan un estado de suscripción específico, como aquellos que están suscritos y han optado por recibir correo electrónico.

### Limitar el volumen de envío {#limit-send-volume}

Puedes limitar el número total de usuarios que reciben tu mensaje. Esto sirve como una verificación independiente de los filtros de tu campaña. Para más detalles, consulta [Establecer un límite máximo de usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#setting-a-maximum-user-cap).

### Limitar la velocidad de envío de esta campaña {#limit-the-rate-at-which-this-campaign-sends}

Si anticipas que campañas grandes generarán un pico en la actividad de los usuarios y sobrecargarán tus servidores, puedes especificar un límite de velocidad por minuto para el envío de mensajes, lo que significa que Braze no enviará más de tu configuración de límite de velocidad en un minuto. Para más detalles, consulta [Limitación de velocidad de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-speed-rate-limiting).

### Pruebas A/B {#ab-testing}

Puedes crear una [prueba multivariante o A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/) para cualquier campaña que se dirija a un solo canal, incluso si ese canal incluye múltiples dispositivos. Por ejemplo, si quieres usar pruebas multivariantes o A/B para una campaña push, puedes dirigirte solo a dispositivos iOS o solo a dispositivos Android, pero no a ambos tipos de dispositivo en la misma campaña.

Para campañas push, de correo electrónico y de webhook planificadas para enviarse una sola vez, también puedes usar una [optimización]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations/). Una optimización reserva una parte de tu audiencia objetivo de la prueba A/B y la retiene para un segundo envío optimizado basado en los resultados de la primera prueba.

## Paso 4: Asignar eventos de conversión {#step-4-assign-conversion-events}

Los [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) miden los resultados después de que un usuario recibe tu campaña (o entra en el grupo de control). Braze establece por defecto **Inicia sesión** dentro de una ventana corta (tres días). Puedes definir eventos de conversión que coincidan con tus KPI, hasta cuatro eventos por campaña.

Después del lanzamiento, usa el [dashboard de conversiones]({{site.baseurl}}/user_guide/analytics/dashboards/conversions/) para analizar tendencias de conversión en múltiples campañas o Canvas, comparar canales y ajustar rangos de fechas, métodos de atribución y desgloses en un solo lugar.

{% alert important %}
No puedes añadir ni eliminar eventos de conversión después de que la campaña se lance. Confirma los eventos antes de lanzar.
{% endalert %}

## Paso 5: Revisar resumen y lanzar {#step-5-review-summary-and-launch}

El paso **Revisar resumen** muestra la planificación, la audiencia, las variantes y las opciones de mensajería. Antes de lanzar tu campaña:

1. Confirma que los segmentos, las variantes y la configuración de entrega coincidan con tu intención.
2. [Envía mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/) para validar la representación y el comportamiento en tus dispositivos de prueba o destinatarios internos.

Cuando estés listo, selecciona **Launch Campaign**.

### Aprobaciones {#approvals}

Si tu espacio de trabajo utiliza aprobaciones, un compañero de equipo con permiso para aprobar campañas debe aprobarla antes del lanzamiento. Para más información, consulta [Aprobaciones para campañas y Canvas]({{site.baseurl}}/user_guide/messaging/governance/approvals/).

## Artículos relacionados {#related-articles}

- [Diseñar y editar]({{site.baseurl}}/user_guide/messaging/design_and_edit/)
- [Pruebas A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/)
- [Lo que debes saber antes de enviar]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/know_before_you_send/)
- [Análisis de campañas]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics/)