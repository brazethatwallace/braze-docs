# Preguntas frecuentes {#frequently-asked-questions}

> Estas son respuestas a las preguntas frecuentes sobre Banners en Braze. Para obtener información más general, consulta [Acerca de Banners]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}/).

## ¿Cuándo aparecen las actualizaciones de los Banners para los usuarios? {#when-do-banner-updates-appear-for-users}

Los Banners se actualizan con los datos más recientes cada vez que llamas al método de actualización&#8212;no es necesario reenviar ni actualizar tu Campaign de Banners.

## ¿Cuántas ubicaciones puedo solicitar en una sesión? {#how-many-placements-can-i-request-in-a-session}

En una sola solicitud de actualización, puedes solicitar un máximo de 10 ubicaciones. Por cada una que solicites, Braze devolverá el Banner con mayor prioridad para el que el usuario sea elegible. Las solicitudes adicionales devolverán un error.

Para obtener más información, consulta [Solicitudes de ubicación]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %}).

## ¿Cuántas Campaigns de Banners pueden estar activas simultáneamente? {#how-many-banner-campaigns-can-be-active-simultaneously}

Cada espacio de trabajo puede admitir hasta 200 Campaigns de Banners activas. Si se alcanza este límite, tendrás que [archivar o desactivar]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) una Campaign existente antes de crear una nueva.

## En las Campaigns que comparten una ubicación, ¿qué Banner se muestra primero? {#for-campaigns-sharing-a-placement-which-banner-is-displayed-first}

Si un usuario cumple los requisitos para varias Campaigns de Banners que comparten la misma ubicación, se mostrará el Banner con mayor prioridad. Para obtener más información, consulta [Prioridad de Banners]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %}).

## ¿Puedo utilizar Banners en mi fuente de Content Cards existente? {#can-i-use-banners-in-my-existing-content-card-feed}

Los Banners son diferentes de las Content Cards, lo que significa que no puedes usar Banners y Content Cards en la misma fuente. Para sustituir las fuentes de Content Cards existentes por Banners, tendrás que [crear ubicaciones en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/placements/).

## ¿Pueden los Banners incluir video? {#can-banners-include-video}

El compositor estándar de Banners admite imágenes, texto y botones. Para incluir un video en un Banner, puedes usar un bloque de **Custom Code** y renderizar un video o un reproductor integrado en tu aplicación o sitio web.

## ¿Puedo desencadenar un Banner basado en las acciones del usuario? {#can-i-trigger-a-banner-based-on-user-actions}

Aunque los Banners no admiten la [entrega basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/), puedes dirigirte a los usuarios en función de sus acciones pasadas utilizando la segmentación y la prioridad.

Por ejemplo, para mostrar un Banner especial solo a los usuarios que hayan completado un evento `purchase`:
1. **Segmentación:** En tu Campaign, dirígete a un segmento de usuarios que hayan realizado el evento personalizado `purchase` al menos una vez.
2. **Prioridad:** Si tienes un Banner general para todos los usuarios y este Banner específico para compradores dirigido a la misma ubicación, establece la prioridad del Banner específico en **High** y la del Banner general en **Medium** o **Low**.

Cuando el usuario inicia una nueva sesión o actualiza los Banners después de realizar la acción, Braze evalúa su elegibilidad. Si coincide con el segmento "Compra", se mostrará el Banner de alta prioridad.


## ¿Pueden los usuarios cerrar manualmente un Banner? {#can-users-dismiss-a-banner}

Sí. Puedes permitir que los usuarios cierren manualmente un Banner habilitando el comportamiento de cierre en el compositor de Banners. Consulta [Configurar el comportamiento de cierre]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#dismiss-behavior) para obtener más detalles sobre cómo habilitar el cierre y personalizar el botón de cierre.

Los usuarios pueden cerrar manualmente los Banners solo si el comportamiento de cierre está habilitado. Si el cierre no está habilitado, puedes controlar la visibilidad de los Banners administrando la elegibilidad de los segmentos de usuarios. Cuando un usuario ya no cumple los criterios de segmentación de una Campaign de Banners, no lo verá de nuevo en su próxima sesión.

Cuando un usuario cierra un Banner, deja de ser elegible para esa Campaign de forma predeterminada. Para permitir que los usuarios que cerraron el Banner lo vean de nuevo, [configura la reelegibilidad]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#re-eligibility) en el paso de **Controles de entrega** de la Campaign. Los pasos de Banner en Canvas utilizan la configuración de reentrada de Canvas para controlar la reelegibilidad en su lugar.

Por ejemplo, si muestras un Banner promocional hasta que un usuario realiza una compra, registrar un evento como `purchase_completed` puede eliminar a ese usuario del segmento objetivo, ocultando efectivamente el Banner en sesiones posteriores.

## ¿Puedo exportar los análisis de Campaigns de Banners utilizando la API de Braze? {#can-i-export-banners-campaign-analytics-using-the-braze-api}

Sí. Puedes utilizar el [punto de conexión `/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) para obtener datos sobre cuántas Campaigns de Banners se visualizaron, recibieron clics o generaron conversiones.

## ¿Cuándo se realiza la segmentación de los usuarios? {#when-are-users-segmented}

Los usuarios se segmentan al inicio de la sesión. Si los segmentos objetivo de una Campaign dependen de atributos personalizados, eventos personalizados u otros atributos de segmentación, estos deben estar presentes en el usuario al inicio de la sesión.

## ¿Cómo puedo componer Banners para garantizar la menor latencia posible? {#how-can-i-compose-banners-to-ensure-the-lowest-latency}

Cuanto más sencillo sea el mensaje de tu Banner, más rápido se renderizará. Lo mejor es probar tu Campaign de Banners comparándola con la latencia prevista para tu caso de uso. Por ejemplo, asegúrate de probar atributos de Liquid como `catalog_items`.

## ¿Se admiten todas las etiquetas de Liquid? {#are-all-liquid-tags-supported}

No. Sin embargo, la mayoría de las etiquetas de Liquid son compatibles con los mensajes de Banners, excepto `catalog_items` que se vuelven a renderizar utilizando la [etiqueta `:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid).

## ¿Puedo capturar eventos de clic? {#can-i-capture-click-events}

Sí. La forma en que se capturan los eventos de clic depende de cómo se renderiza tu Banner:

- **Componentes estándar del editor:** Si tu Banner utiliza componentes de editor estándar (imágenes, botones, texto), el seguimiento de los clics se realiza automáticamente cuando se utilizan los métodos de inserción del SDK.
- **Bloques de código personalizado:** Si deseas realizar el seguimiento de los clics en elementos dentro de un bloque de editor de código personalizado, debes llamar a `brazeBridge.logClick()` desde tu HTML personalizado para registrar los clics. Esto se aplica incluso cuando se utilizan los métodos del SDK para insertar y renderizar el Banner. Para obtener la referencia completa, consulta [Código personalizado y puente JavaScript para Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/custom_code/#javascript-bridge).
- **Interfaz de usuario personalizada (headless):** Si estás creando una interfaz de usuario totalmente personalizada utilizando las propiedades personalizadas del Banner en lugar de renderizar el HTML del Banner, llama a `logClick()` en el objeto Banner desde el código de tu aplicación.

Para obtener más información, consulta [Registro de clics]({{site.baseurl}}/developer_guide/banners/placements/#logging-clicks).