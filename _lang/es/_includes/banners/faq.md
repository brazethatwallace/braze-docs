# Preguntas frecuentes {#frequently-asked-questions}

> Estas son respuestas a las preguntas frecuentes sobre Banners en Braze. Para obtener información más general, consulta [Acerca de Banners]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}).

## ¿Cuándo aparecen las actualizaciones de los Banners para los usuarios? {#when-do-banner-updates-appear-for-users}

Los Banners se actualizan con sus datos más recientes cada vez que llamas al método de actualización&#8212;no es necesario reenviar ni actualizar tu Campaign de Banner.

## ¿Cuántas ubicaciones puedo solicitar en una sesión? {#how-many-placements-can-i-request-in-a-session}

En una única solicitud de actualización, puedes solicitar un máximo de 10 ubicaciones. Para cada una que solicites, Braze devuelve el Banner de mayor prioridad para el que el usuario es elegible. Las solicitudes adicionales devuelven un error.

Para más información, consulta [Solicitudes de ubicación]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %}).

## ¿Cuántas Campaigns de Banner pueden estar activas simultáneamente? {#how-many-banner-campaigns-can-be-active-simultaneously}

Cada espacio de trabajo puede soportar hasta 200 Campaigns de Banner activas. Si se alcanza este límite, tendrás que [archivar o desactivar]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses#changing-the-status) una Campaign existente antes de crear una nueva.

## En el caso de Campaigns que comparten una ubicación, ¿qué Banner se muestra primero? {#for-campaigns-sharing-a-placement-which-banner-is-displayed-first}

Si un usuario es elegible para varias Campaigns de Banner que comparten la misma ubicación, se muestra el Banner con la prioridad más alta. Para más información, consulta [Prioridad de Banner]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %}).

## ¿Puedo usar Banners en mi fuente de Content Cards existente? {#can-i-use-banners-in-my-existing-content-card-feed}

Banners son diferentes de Content Cards, lo que significa que no puedes usar Banners y Content Cards en la misma fuente. Para reemplazar fuentes de Content Cards existentes con Banners, tendrás que [crear ubicaciones en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/placements).

## ¿En qué se diferencian los Banners de los mensajes dentro de la aplicación? {#how-are-banners-different-from-in-app-messages}

Los Banners y los [mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages) llegan a los usuarios dentro de tu aplicación o sitio web, pero utilizan modelos de entrega diferentes. Si estás comparando los Banners con una configuración existente de mensajes dentro de la aplicación, espera diferencias en los desencadenantes, los tiempos de actualización y las pruebas, no un intercambio directo.

| Tema | Banners | Mensajes dentro de la aplicación |
| --- | --- | --- |
| Dónde aparecen los mensajes | En línea en las [ubicaciones]({{site.baseurl}}/developer_guide/banners/placements) que defines en tu aplicación o sitio | Superposiciones de pantalla completa, modal o deslizantes gestionadas por el SDK |
| Cuándo se actualiza el contenido | Cuando tu aplicación o sitio solicita una actualización de Banner (por ejemplo, al inicio de sesión o a mitad de sesión) | Los mensajes con plantilla evalúan Liquid cuando se desencadena el mensaje dentro de la aplicación (por ejemplo, con un evento personalizado o al inicio de sesión), después de que la carga útil se almacene en caché en el dispositivo |
| Desencadenantes basados en acciones | Sin [entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery); usa segmentos, prioridad y tiempos de actualización en su lugar | Admite entrega basada en acciones y activada por API |
| Pruebas | Previsualiza un usuario y luego confirma que la actualización de la ubicación en tu aplicación o sitio muestra el Banner esperado | Usa **Envío de prueba** o flujos de vista previa de mensajes dentro de la aplicación para la visualización basada en desencadenantes |
| Informes | Las visualizaciones y clics de los Banners siguen los análisis de Banners | Las impresiones y clics dentro de la aplicación siguen los análisis de mensajes dentro de la aplicación |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="¿En qué se diferencian los Banners de los mensajes dentro de la aplicación?" }

## ¿Pueden los Banners incluir video? {#can-banners-include-video}

El constructor estándar de Banners admite imágenes, texto y botones. Para incluir un video en un Banner, puedes usar un bloque de **código personalizado** en el constructor, o crear el Banner completo con el editor HTML e incrustar un reproductor de video directamente en tu HTML.

## ¿Puedo activar un banner basándome en las acciones del usuario? {#can-i-trigger-a-banner-based-on-user-actions}

Aunque los banners no admiten la [entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery), puedes segmentar a los usuarios en función de sus acciones pasadas mediante la segmentación y la prioridad.

Por ejemplo, para mostrar un banner especial solo a los usuarios que hayan completado un evento `purchase`:
1. **Segmentación:** En tu Campaign, dirige la comunicación a un Segment de usuarios que hayan realizado el evento personalizado `purchase` al menos una vez.
2. **Prioridad:** Si tienes un banner general para todos los usuarios y este banner específico para compradores dirigido a la misma ubicación, establece la prioridad del banner específico en **High** y la del banner general en **Medium** o **Low**.

Cuando el usuario inicia una nueva sesión o actualiza los banners después de realizar la acción, Braze evalúa su elegibilidad. Si coincide con el Segment "Purchase", se muestra el banner de alta prioridad.

## ¿Pueden los usuarios descartar un banner? {#can-users-dismiss-a-banner}

Sí. Puedes permitir que los usuarios descarten manualmente un banner. Consulta [Configurar el comportamiento de descarte]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#dismiss-behavior) para obtener detalles sobre cómo configurar el descarte tanto en el constructor como en el editor HTML.

Los usuarios solo pueden descartar banners manualmente si el comportamiento de descarte está habilitado. Si el descarte no está habilitado, puedes controlar la visibilidad del banner gestionando la elegibilidad del Segment del usuario. Cuando un usuario deja de cumplir los criterios de segmentación de una Campaign de banner, no lo verá de nuevo en su siguiente sesión.

Cuando un usuario descarta un banner, no es elegible para esa Campaign de forma predeterminada. Para permitir que los usuarios que lo descartaron vuelvan a ver el banner, [configura la reelegibilidad]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#re-eligibility) en el paso **Delivery Controls** de la Campaign. Los pasos de banner en Canvas utilizan la configuración de reentrada de Canvas para controlar la reelegibilidad.

Por ejemplo, si muestras un banner promocional hasta que un usuario realice una compra, registrar un evento como `purchase_completed` puede eliminar a ese usuario del Segment objetivo, ocultando efectivamente el banner en las sesiones posteriores.

## ¿Puedo exportar análisis de Campaigns de Banners usando la API de Braze? {#can-i-export-banners-campaign-analytics-using-the-braze-api}

Sí. Puedes usar el [endpoint `/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) para obtener datos sobre cuántas Campaigns de Banners fueron vistas, clicadas o convertidas.

## ¿Cuándo se segmentan los usuarios? {#when-are-users-segmented}

Los usuarios se segmentan al inicio de la sesión. Si los Segments objetivo de una Campaign dependen de atributos personalizados, eventos personalizados u otros atributos de segmentación, estos deben estar presentes en el usuario al inicio de la sesión.

## ¿Cómo puedo componer Banners para garantizar la menor latencia? {#how-can-i-compose-banners-to-ensure-the-lowest-latency}

Cuanto más simple sea la mensajería de tu Banner, más rápido se renderiza. Es mejor probar tu Campaign de Banner en función de la latencia esperada para tu caso de uso. Por ejemplo, asegúrate de probar atributos de Liquid como `catalog_items`.

Si usas [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) (en acceso anticipado), ten en cuenta que cada llamada cuenta contra un presupuesto de renderizado compartido de aproximadamente dos segundos entre todas las ubicaciones en una sola actualización. Si se supera el presupuesto o una llamada agota el tiempo de espera, el resultado de contenido conectado se trata como nulo y los Banners no reintentan. Para minimizar la latencia:

- Mantén tus endpoints rápidos y [almacena en caché las respuestas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) siempre que sea posible.
- Limita el número de URLs únicas de contenido conectado entre las ubicaciones que se renderizan juntas.
- Evita encadenar llamadas donde una respuesta de contenido conectado determine la URL de la siguiente.
- Usa sentencias de protección de Liquid o el [filtro `default`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) para manejar resultados nulos y evitar Banners en blanco.

## ¿Se admiten todas las etiquetas de Liquid? {#are-all-liquid-tags-supported}

No. Sin embargo, la mayoría de las etiquetas de Liquid son compatibles con los mensajes de Banner, excepto `catalog_items` que se vuelven a renderizar utilizando la [etiqueta `:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs#using-liquid).

## ¿Puedo capturar eventos de clic? {#can-i-capture-click-events}

Sí. La forma en que se capturan los eventos de clic depende de cómo se renderiza tu Banner:

- **Constructor — componentes estándar:** Si tu Banner utiliza componentes estándar del editor (imágenes, botones, texto), los clics se rastrean automáticamente cuando se usan los métodos de inserción del SDK.
- **Constructor — bloques de código personalizado:** Si deseas rastrear clics en elementos dentro de un bloque del editor de código personalizado, debes llamar a `brazeBridge.logClick()` desde tu HTML personalizado. Esto aplica incluso cuando se usan los métodos del SDK para insertar y renderizar el Banner.
- **Editor HTML:** El seguimiento de clics no es automático. Debes llamar a `brazeBridge.logClick()` para cada elemento con clic que desees rastrear. Para la referencia completa, consulta [Código personalizado y puente JavaScript para Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge).
- **Interfaz personalizada (headless):** Si estás construyendo una interfaz completamente personalizada usando las propiedades personalizadas del Banner en lugar de renderizar el HTML del Banner, llama a `logClick()` en el objeto Banner desde el código de tu aplicación.

Para más información, consulta [Registro de clics]({{site.baseurl}}/developer_guide/banners/placements#logging-clicks).