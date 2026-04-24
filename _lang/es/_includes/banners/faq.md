# Preguntas frecuentes

> Estas son las respuestas a las preguntas más frecuentes sobre los banners en Braze. Para obtener información más general, consulta [Acerca de los banners]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}).

## ¿Cuándo aparecen las actualizaciones de los banners para los usuarios?

Los banners se actualizan con los datos más recientes cada vez que llamas al método de actualización&#8212;no es necesario reenviar ni actualizar tu campaña de banners.

## ¿Cuántas ubicaciones puedo solicitar en una sesión?

En una sola solicitud de actualización, puedes solicitar un máximo de 10 ubicaciones. Por cada una que solicites, Braze devolverá el banner con mayor prioridad para el que el usuario sea elegible. Las solicitudes adicionales devolverán un error.

Para obtener más información, consulta [Solicitudes de ubicación]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %}).

## ¿Cuántas campañas de banners pueden estar activas simultáneamente?

Cada espacio de trabajo puede admitir hasta 200 campañas activas de banners. Si se alcanza este límite, tendrás que [archivar o desactivar]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) una campaña existente antes de crear una nueva.

## En las campañas que comparten una ubicación, ¿qué banner se muestra primero?

Si un usuario cumple los requisitos para varias campañas de banners que comparten la misma ubicación, se mostrará el banner con mayor prioridad. Para obtener más información, consulta [Prioridad de los banners]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %}).

## ¿Puedo utilizar banners en mi fuente de Tarjetas de contenido existente?

Los banners son diferentes de las Tarjetas de contenido, lo que significa que no puedes usar banners y Tarjetas de contenido en la misma fuente. Para sustituir las fuentes de Tarjetas de contenido existentes por banners, tendrás que [crear ubicaciones en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/placements/).

## ¿Pueden los banners incluir video?

El compositor estándar de banners admite imágenes, texto y botones. Para incluir un video en un banner, puedes usar un bloque de **código personalizado** y renderizar un video o un reproductor integrado en tu aplicación o sitio web.

## ¿Puedo desencadenar un banner basado en las acciones del usuario?

Aunque los banners no admiten la [entrega basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery), puedes dirigirte a los usuarios en función de sus acciones pasadas utilizando la segmentación y la prioridad.

Por ejemplo, para mostrar un banner especial solo a los usuarios que hayan completado un evento `purchase`:
1. **Segmentación:** En tu campaña, dirígete a un segmento de usuarios que hayan realizado el evento personalizado `purchase` al menos una vez.
2. **Prioridad:** Si tienes un banner general para todos los usuarios y este banner específico para compradores dirigido a la misma ubicación, establece la prioridad del banner específico en **Alta** y la del banner general en **Media** o **Baja**.

Cuando el usuario inicia una nueva sesión o actualiza los banners después de realizar la acción, Braze evalúa su elegibilidad. Si coincide con el segmento "Compra", se mostrará el banner de alta prioridad.


## ¿Pueden los usuarios cerrar manualmente un banner?

{% alert important %}
Permitir que los usuarios cierren manualmente un banner está en acceso anticipado. Consulta [Configurar el comportamiento de cierre]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#dismiss-behavior) para obtener más detalles. Si te interesa participar en el acceso anticipado, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

Los usuarios pueden cerrar manualmente los banners solo si el comportamiento de cierre está habilitado y tu espacio de trabajo participa en el acceso anticipado. Si el cierre no está habilitado o no está disponible para tu espacio de trabajo, puedes controlar la visibilidad de los banners administrando la elegibilidad de los segmentos de usuarios. Cuando un usuario ya no cumple los criterios de segmentación de una campaña de banners, no lo verá de nuevo en su próxima sesión.

Por ejemplo, si muestras un banner promocional hasta que un usuario realiza una compra, registrar un evento como `purchase_completed` puede eliminar a ese usuario del segmento objetivo, ocultando efectivamente el banner en sesiones posteriores.

## ¿Puedo exportar los análisis de campañas de banners utilizando la API de Braze?

Sí. Puedes utilizar el [punto de conexión `/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) para obtener datos sobre cuántas campañas de banners se visualizaron, recibieron clics o generaron conversiones.

## ¿Cuándo se realiza la segmentación de los usuarios?

Los usuarios se segmentan al inicio de la sesión. Si los segmentos objetivo de una campaña dependen de atributos personalizados, eventos personalizados u otros atributos de segmentación, estos deben estar presentes en el usuario al inicio de la sesión.

## ¿Cómo puedo componer banners para garantizar la menor latencia posible?

Cuanto más sencillo sea el mensaje de tu banner, más rápido se renderizará. Lo mejor es probar tu campaña de banners comparándola con la latencia prevista para tu caso de uso. Por ejemplo, asegúrate de probar atributos de Liquid como `catalog_items`.

## ¿Se admiten todas las etiquetas de Liquid?

No. Sin embargo, la mayoría de las etiquetas de Liquid son compatibles con los mensajes de banners, excepto `catalog_items` que se vuelven a renderizar utilizando la [etiqueta `:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid).

## ¿Puedo capturar eventos de clic?

Sí. La forma en que se capturan los eventos de clic depende de cómo se renderiza tu banner:

- **Componentes estándar del editor:** Si tu banner utiliza componentes de editor estándar (imágenes, botones, texto), el seguimiento de los clics se realiza automáticamente cuando se utilizan los métodos de inserción del SDK.
- **Bloques de código personalizado:** Si deseas realizar el seguimiento de los clics en elementos dentro de un bloque de editor de código personalizado, debes llamar a `brazeBridge.logClick()` desde tu HTML personalizado para registrar los clics. Esto se aplica incluso cuando se utilizan los métodos del SDK para insertar y renderizar el banner. Para obtener la referencia completa, consulta [Código personalizado y puente JavaScript para banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/custom_code/#javascript-bridge).
- **Interfaz de usuario personalizada (headless):** Si estás creando una interfaz de usuario totalmente personalizada utilizando las propiedades personalizadas del banner en lugar de renderizar el HTML del banner, llama a `logClick()` en el objeto Banner desde el código de tu aplicación.

Para obtener más información, consulta [Registro de clics]({{site.baseurl}}/developer_guide/banners/placements/#logging-clicks).