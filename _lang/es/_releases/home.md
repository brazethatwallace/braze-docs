---
nav_title: Inicio
article_title: Novedades en Braze
description: "Las notas de la versión de Braze se publican mensualmente para que puedas estar al día de los principales lanzamientos de producto, las mejoras continuas del producto, las asociaciones de Braze, los cambios de última hora en el SDK y las características obsoletas."
page_order: 0
search_rank: 1
page_type: reference

---

# Novedades en Braze {#whats-new-in-braze}

{% alert tip %}
Para obtener más información sobre cualquiera de las actualizaciones enumeradas en esta página, ponte en contacto con tu director de cuentas o [abre un ticket de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support). También puedes consultar nuestros [registros de cambios del SDK]({{site.baseurl}}/developer_guide/changelogs) para obtener más información sobre nuestras versiones mensuales del SDK, mejoras y cambios de última hora.
{% endalert %}

{% details 25 de junio de 2026 %}

## Lanzamiento del 25 de junio de 2026 {#june-25-2026-release}

### Datos e informes {#data-reporting}

#### Actualización del nombre de la métrica para Content Cards y Banners {#metric-name-update-for-content-cards-and-banners}

La métrica _Destinatarios únicos_ se ha renombrado a _Impresiones diarias únicas_ para Content Cards y Banners. Las _Impresiones diarias únicas_ se refieren al número recibido de Braze y se basan en el `user_id`. Las impresiones diarias únicas se cuentan a nivel de Campaign o paso en Canvas. Para más detalles, consulta el [Glosario de métricas]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

#### Eliminación de usuarios {#user-deletion}

{% multi_lang_include release_type.md release="General availability" %}

La [eliminación de usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users) te permite gestionar tu base de datos eliminando perfiles que ya no son necesarios, que se crearon por error o que deben eliminarse por cumplimiento normativo (como GDPR o CCPA).

#### Exclusiones de puntos de datos {#data-point-exclusions}

{% multi_lang_include release_type.md release="General availability" %}

Los [eventos recomendados de comercio electrónico]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events) ya no cuentan como puntos de datos facturables. Puedes adoptar los eventos de comercio electrónico de Braze (`ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started`, `ecommerce.order_placed`, `ecommerce.order_cancelled`, `ecommerce.order_refunded`) sin consumo de puntos de datos.

#### Pestaña Historial de eventos {#event-history-tab}

{% multi_lang_include release_type.md release="General availability" %}

La pestaña **Event History** en los [perfiles de usuario]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) muestra los eventos personalizados y las compras del usuario de los últimos 30 días (hasta los 100 más recientes). Úsala para confirmar que una integración del SDK o la API está enviando eventos como se espera, depurar por qué un usuario entró (o no) en una Campaign o Canvas desencadenado por eventos, o investigar una escalación de soporte sobre un usuario específico.

#### El Centro de capacidad de entrega muestra datos de Microsoft SNDS para clientes de Amazon SES {#deliverability-center-surfaces-microsoft-snds-data-for-amazon-ses-customers}

Para los espacios de trabajo que envían correo electrónico a través de Amazon SES, el [Centro de capacidad de entrega]({{site.baseurl}}/deliverability_center) muestra las métricas de Microsoft SNDS para tus IP de envío dedicadas. Braze rellena hasta 90 días de datos históricos de SNDS cuando esta característica se activa para tu espacio de trabajo.

### BrazeAI<sup>TM</sup>

#### Asistentes unificados de BrazeAI en Operator {#unified-brazeai-assistants-in-operator}

Los asistentes independientes de BrazeAI que se encuentran en todo el panel se han unificado en [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator), estableciendo a Operator como el asistente de IA único para la asistencia de IA generativa orientada al especialista en marketing en todo el panel. Los siguientes asistentes ahora se canalizan a través de Operator:

- AI Liquid Agent
- AI Copywriter
- AI HTML Email Template agent
- AI Image generator
- Content QA with AI
- AI Copilot for Data Transformations

Los puntos de entrada existentes permanecen donde solía estar cada botón de asistente heredado. En lugar de abrir un asistente independiente, estos puntos de entrada ahora abren el panel de Operator con indicaciones dinámicas que están preconfiguradas para tu tarea. Estos puntos de entrada proporcionan una ruta directa a Operator para que puedas usar estas capacidades sin ajustar tus flujos de trabajo existentes.

#### Compatibilidad de Operator con la creación y edición de campañas {#operator-support-for-campaign-creation-and-editing}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator) ahora puede crear y editar campañas completas, no solo componer mensajes. Desde una única indicación en lenguaje natural o un resumen de campaña, Operator construye una campaña lista para revisión de principio a fin — componiendo el mensaje, programando la entrega, segmentando la audiencia y asignando eventos de conversión — y luego resume lo que construyó en el paso de revisión. Anteriormente, Operator podía componer el mensaje (uno de los cinco pasos de creación de campaña); ahora tiene visibilidad y control sobre los pasos restantes de Programación, Segmentación, Asignación y Revisión.

Esta funcionalidad está disponible desde la página **Campaigns** o desde cualquier campaña existente. Como resultado, Operator puede:

- Responder a indicaciones como "Quiero enviar a nuestros usuarios inactivos una notificación push con un código de promoción del 20% de descuento la próxima vez que abran la aplicación o registren un evento personalizado que cancele su suscripción".
- Asistirte en cada paso individual del asistente de campaña, con visibilidad completa de lo que estás trabajando y la capacidad de cambiar las entradas del formulario en la página.
- Navegar al paso correcto del asistente para comenzar a tomar acción, ya sea que empieces desde una campaña abierta o desde la página **Campaigns**.

#### Compatibilidad de Operator con Content Blocks {#operator-support-for-content-blocks}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator) ahora puede crear y editar [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) — los fragmentos reutilizables que construyes una vez y referencias en múltiples mensajes — directamente desde una indicación en lenguaje natural. Desde la página **Content Blocks**, pide a Operator que cree un nuevo Content Block desde cero o edite uno existente, y Operator genera o actualiza el contenido para que lo revises.

#### Plantillas de la Consola de Agente creadas con Operator {#agent-console-templates-built-with-operator}

Al crear un agente en la **Consola de Agente**, puedes elegir crear un agente personalizado o seleccionar una opción en **Create an agent with Operator** para usar BrazeAI Operator y aplicar una plantilla inicial. Operator puede preconfigurar instrucciones, campos de salida y contexto para las siguientes plantillas iniciales de la Consola de Agente.

Para más detalles, consulta [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).

#### Mejoras en la Consola de Agente {#agent-console-enhancements}

Puedes hacer lo siguiente en la [Consola de Agente]({{site.baseurl}}/user_guide/brazeai/agents):

- Configurar casos de uso preestablecidos con Operator a través del menú desplegable del botón **Create agent**.
- Duplicar agentes existentes desde la lista de agentes.
- Guardar agentes como borradores durante la creación y completar las configuraciones más tarde.
- Establecer valores de salida alternativos para agentes de Canvas para evitar que las variables de salida se establezcan como nulas si el agente produce un error.
- Establecer campos de entrada obligatorios para un campo agéntico de catálogo, de modo que el agente no se ejecute si el valor de un campo de entrada obligatorio está vacío o falta.
- Volver a ejecutar un agente para todas las celdas vacías de una columna agéntica para rellenar los valores faltantes sin volver a ejecutar toda la columna.

#### Editar un paso del Optimizador de contenidos ya lanzado {#edit-a-launched-content-optimizer-step}

{% multi_lang_include release_type.md release="Beta" %}

Después de que tu Canvas se haya lanzado, ahora puedes [actualizar un paso del Optimizador de contenidos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step#edit-a-launched-step) para:

- Añadir nuevas variantes a cualquier componente existente, ya sea manualmente o usando sugerencias generadas por IA, hasta el límite de cinco variantes por componente.
- Desactivar variantes para dejar de enviarlas a los usuarios.
- Reactivar variantes previamente desactivadas, siempre que hacerlo mantenga el componente en o por debajo del límite de cinco variantes.

### Canales y puntos de intervención {#channels-touchpoints}

#### Descartes de usuario para Banners {#user-dismissals-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

Puedes permitir que los usuarios descarten manualmente un Banner seleccionando **Banner can be dismissed** al configurar el comportamiento de descarte. Esta opción es beneficiosa en escenarios en los que deseas promocionar una venta por tiempo limitado para todos los usuarios de la aplicación, pero permitirles descartar el mensaje si no están interesados.

Consulta [Configurar el comportamiento de descarte]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#dismiss-behavior) para obtener detalles sobre cómo habilitar el descarte y personalizar el botón de descarte.

#### Seguimiento de clics personalizado para Banners {#custom-click-tracking-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

Para un seguimiento de clics más granular en Banners, puedes [asignar un identificador personalizado]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#step-32-define-on-click-behavior-optional) a cada elemento interactivo usando el campo **Identifier for Reporting** en su panel de propiedades.

#### Reelegibilidad para Banners {#re-eligibility-for-banners}

Cuando la reelegibilidad está habilitada para campañas de Banner, los usuarios que descarten un Banner pueden volver a ser elegibles después de una ventana de espera configurable que comienza en el momento del descarte. Si la reelegibilidad no está activada, los usuarios que descartaron el Banner permanecen no elegibles. Para configurar la reelegibilidad, consulta [Configurar la reelegibilidad]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#re-eligibility). Ten en cuenta que los pasos de Banner en Canvas usan la configuración de reentrada de Canvas en su lugar.

#### Pruebas A/B de Quick Push {#quick-push-ab-testing}

{% multi_lang_include release_type.md release="General availability" %}

Las pruebas A/B de Quick Push ahora admiten campañas push multiplataforma y pasos en Canvas a través de grupos de variantes, para que puedas probar variaciones de mensajes alineadas para iOS y Android en un solo flujo de trabajo. Para más información, consulta [Mensajes push multiplataforma]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push#use-cases).

#### Selección de variantes de BrazeAI<sup>TM</sup> {#brazeai-variant-selection}

{% multi_lang_include release_type.md release="Early access" %}

La selección de variantes de BrazeAI<sup>TM</sup> se activa automáticamente cuando añades múltiples variantes push, aplica los valores predeterminados de experimento recomendados y optimiza hacia la variante de mayor rendimiento para mejorar la participación. Puedes desactivarla si necesitas enviar inmediatamente. Para más información, consulta [Selección de variantes de BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

#### Resultados del envío de prueba de WhatsApp {#whatsapp-test-send-results}

Después de enviar un mensaje de prueba de WhatsApp, puedes ver un [informe de entrega detallado]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-4-view-test-send-results) directamente en el creador de mensajes. Esto te ayuda a confirmar que tu mensaje llegó al destinatario previsto y a solucionar problemas de fallos antes del lanzamiento.

### Asociaciones {#partnerships}

#### Convercus - Datos y análisis - Fidelización {#convercus-data-and-analytics-loyalty}

[Convercus]({{site.baseurl}}/partners/data_and_analytics/loyalty/convercus) es una plataforma SaaS de fidelización y cupones que ayuda a las marcas y minoristas a aumentar la frecuencia de compra, el valor del carrito y las tasas de recompra a través de programas de fidelización omnicanal y campañas de cupones personalizadas.

#### Copy Pastd - Orquestación de mensajes - Plantillas {#copy-pastd-message-orchestration-templates}

[Copy Pastd]({{site.baseurl}}/partners/copy_pastd) Building Blocks es un creador de correo electrónico de arrastrar y soltar que envía Content Blocks con Liquid y plantillas completas directamente a tu espacio de trabajo de Braze. Diseña una vez, sincroniza con Braze y reutiliza los mismos componentes en campañas, Canvas y flujos desencadenados sin reconstruir HTML cada vez.

#### Databricks Mosaic - Proveedores de modelos de IA {#databricks-mosaic-ai-model-providers}

[Databricks Mosaic]({{site.baseurl}}/partners/databricks_mosaic) es la plataforma unificada de Databricks para construir, desplegar y gestionar modelos de IA y aprendizaje automático a escala en la plataforma de inteligencia de datos de Databricks.

#### DinMo - Datos y análisis - ETL inverso {#dinmo-data-and-analytics-reverse-etl}

[DinMo]({{site.baseurl}}/partners/dinmo) es una plataforma de datos de los clientes (CDP) componible que conecta tu almacén de datos en la nube con Braze a través de ETL inverso (extraer, transformar, cargar). Los equipos de marketing pueden crear segmentos de audiencia a partir de datos del almacén, sincronizar atributos de usuario y eventos en Braze, y mantener los estados de suscripción actualizados sin cargas de CSV ni soporte de ingeniería.

#### EmailShepherd - Orquestación de mensajes - Plantillas {#emailshepherd-message-orchestration-templates}

[EmailShepherd]({{site.baseurl}}/partners/emailshepherd) es una plataforma de creación de correo electrónico agéntica construida sobre tu sistema de diseño de correo electrónico que permite a todo tu equipo de marketing — y a los agentes de IA — producir correos electrónicos alineados con la marca y listos para producción sin cuellos de botella. La integración con Braze publica los correos electrónicos aprobados directamente en tu espacio de trabajo de Braze, para que los especialistas en marketing puedan escalar la producción de correo electrónico en Braze sin sacrificar la consistencia de marca.

#### Talkable - Personalización de mensajes - Referidos {#talkable-message-personalization-referrals}

[Talkable]({{site.baseurl}}/partners/talkable) ayuda a las marcas de consumo a convertir a los clientes satisfechos en un canal de referidos escalable. Con la integración de Braze, las adhesiones voluntarias de correo electrónico de marketing capturadas en las campañas de referidos de Talkable fluyen hacia Braze en tiempo real, proporcionando a tu equipo el consentimiento, el contexto y los datos de campaña que necesitas para dar la bienvenida, segmentar e interactuar con cada nuevo defensor y amigo.

### SDK

#### Actualizaciones de última hora del SDK {#sdk-breaking-updates}

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [Swift SDK 14.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Android SDK 42.3.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.3.0)
    - `BannerView`: Los campos de `BannerDismissSnapshot` pasados a `onDismissCallback` ahora son no nulos. Si el SDK no puede resolver `placementId`, `stableKey` o `trackingId`, la devolución de llamada se omite y se registra una advertencia.
- [Web SDK 6.8.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - Añade compatibilidad con los nuevos métodos de eventos de comercio electrónico.
- [Swift SDK 14.2.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1421)
- [Swift SDK 15.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Banners: `onDismiss` ahora recibe `Braze/BannerDismissalEvent` en lugar de `Braze/Banner`.
    - Eleva la versión de Xcode a 26.0 (17A324).
    - Eleva el objetivo mínimo de despliegue de Mac Catalyst de iOS 13 (macOS 10.15 Catalina) a iOS 16 (macOS 13 Ventura).
        - Los usuarios de Mac Catalyst en macOS 12 Monterey o anterior ya no son compatibles.
    - Elimina la capacidad de controlar si el SDK evita mostrar mensajes dentro de la aplicación a diferentes usuarios en ciertos casos extremos.
        - Elimina la opción de configurar a través de `Braze.Configuration.preventInAppMessageDisplayForDifferentUser`.
        - El SDK ahora siempre se comportará como si esta opción de configuración estuviera establecida en true.
    - Actualiza el init de `Braze.WebViewBridge.ScriptMessageHandler` y `Braze.WebViewBridge.SchemeHandler` para tener un parámetro `channel` no opcional.
- [Android SDK 42.3.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4231)
    - Añade compatibilidad con los nuevos métodos de eventos de comercio electrónico.
    - Añade métodos de descarte de Banner para implementaciones de UI personalizadas.
    - Incluye correcciones de errores de mensajes dentro de la aplicación HTML.
- [Swift SDK 15.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1501)
- [React Native 21.0.0](https://www.npmjs.com/package/@braze/react-native-sdk/v/21.0.0)
    - Actualiza los enlaces de las versiones nativas del SDK Swift y Android.
    - Actualiza los enlaces de la versión nativa del SDK Swift [de Braze Swift SDK 14.0.4 a 15.0.1](https://github.com/braze-inc/braze-swift-sdk/compare/14.0.4...15.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Corrige la documentación JSDoc de Content Cards.
        - Eleva la versión de Xcode a 26.0 (17A324).
- [Swift SDK 15.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Añade compatibilidad con los nuevos métodos de eventos de comercio electrónico.
    - Añade métodos de descarte de Banner para implementaciones de UI personalizadas.
    - Añade implementaciones de ejemplo para construir UI personalizada con Banners.
    - Añade observabilidad de Live Activities de paso directo, permitiendo que los errores y eventos de actualización se rastreen con más precisión y granularidad.
    - Añade getters asíncronos basados en devolución de llamada para Content Cards y deprecia los getters anteriores.
    - Mejora la estabilidad de la gestión de estado.
- [Segment Swift 9.0.0](https://github.com/braze-inc/braze-segment-swift/releases/tag/9.0.0)
    - Actualiza los enlaces del SDK Swift de Braze para que requieran versiones de la denominación `15.0.0+` SemVer.
        - Esto permite la compatibilidad con cualquier versión del SDK de Braze desde `15.0.0` hasta, pero sin incluir, `16.0.0`.
        - Eleva la versión de Xcode a 26.0 (17A324).
        - Consulta la entrada del registro de cambios para [`15.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1500) para más información sobre posibles cambios de última hora.
- [React Native 21.1.0](https://www.npmjs.com/package/@braze/react-native-sdk/v/21.1.0)
- [Swift SDK 15.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}

{% details 28 de mayo de 2026 %}

## Lanzamiento del 28 de mayo de 2026 {#may-28-2026-release}

### Datos e informes

#### Dashboard de rendimiento de push {#push-performance-dashboard}

El [dashboard de rendimiento de push]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance?tab=push%20performance#push-performance-dashboard) te ofrece una vista única a nivel de canal de la participación push, incluyendo envíos, rebotes, entregas y tasas de apertura directas, influenciadas y totales en una ventana de tiempo configurable. Úsalo para comprender el estado general de tu canal push sin necesidad de agregar datos de campañas o Canvas individuales.

#### Campos de geolocalización en selecciones de catálogo {#geolocation-fields-in-catalog-selections}

{% multi_lang_include release_type.md release="General availability" %}

Los catálogos ahora admiten el filtrado basado en distancia con el nuevo tipo de campo de geolocalización y los operadores de selección de catálogo. Esto te ayuda a crear experiencias más relevantes basadas en la ubicación, como mostrar a cada usuario su restaurante más cercano, filtrar propiedades abiertas dentro de 50 km para una campaña inmobiliaria o dirigirte a tiendas cercanas a un evento específico. En lugar de aproximar la segmentación geográfica con códigos de ciudad o región, puedes filtrar elementos del catálogo por proximidad a un punto central, incluyendo un atributo de usuario de Liquid como la ubicación más reciente del usuario. Para más información, consulta [Selecciones]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

#### Banner y RCS para el generador de informes {#banner-and-rcs-for-report-builder}

El [generador de informes]({{site.baseurl}}/report_builder) admite Banner como canal y RCS como subcategoría bajo SMS, para que puedas medir el rendimiento de ambos directamente en tus informes personalizados junto con todos los demás canales de Braze.

#### Acciones del evento `ecommerce.cart_updated` {#ecommercecart_updated-event-actions}

El [evento `ecommerce.cart_updated`]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/?tab=ecommerce.cart_updated#code-examples) admite las acciones `add` y `remove` junto con `replace`, lo que te permite enviar cambios incrementales del carrito en lugar de una instantánea completa del carrito en cada actualización.

### BrazeAI<sup>TM</sup>

#### Optimizador de contenidos para mensajes SMS, MMS y RCS {#content-optimizer-for-sms-mms-and-rcs-messages}

{% multi_lang_include release_type.md release="Beta" %}

Puedes usar el [Optimizador de contenidos]({{site.baseurl}}/user_guide/brazeai/content_optimizer) para optimizar ganchos, cuerpos y CTA para mensajes SMS, MMS y RCS. El Optimizador de contenidos es un agente que te ayuda a probar y optimizar el contenido de los mensajes a escala, utilizando IA para generar y evaluar grandes volúmenes de variantes de contenido automáticamente.

### Orquestación {#orchestration}

#### Zonas horarias del espacio de trabajo {#workspace-time-zones}

{% multi_lang_include release_type.md release="General availability" %}

Usa las [zonas horarias del espacio de trabajo]({{site.baseurl}}/user_guide/administer/global/admin_settings/workspace_time_zone) para definir zonas horarias específicas para espacios de trabajo individuales. Esto hace que las campañas y Canvas programados (que no usen hora local o sincronización inteligente) se envíen según la zona horaria designada del espacio de trabajo, en lugar de la zona horaria general de la empresa.

Las zonas horarias del espacio de trabajo para el envío de mensajes se están implementando gradualmente, por lo que es posible que aún no veas estas configuraciones en tu panel.

### Canales y puntos de intervención

#### WhatsApp `inbound_profile_name`

Puedes capturar automáticamente el nombre para mostrar de WhatsApp de un usuario desde el webhook de mensajería entrante de Meta y escribirlo en el perfil de Braze del usuario. Cuando se recibe un mensaje entrante de WhatsApp, Braze expone el nombre del perfil como un nuevo atributo de Liquid de WhatsApp, [{% raw %}`{{whats_app.${inbound_profile_name}}}`{% endraw %}]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags), que puedes referenciar en un paso de actualización de usuario en Canvas para guardarlo en un campo del perfil.

#### Estados de suscripción SMS huérfanos {#orphaned-sms-subscription-states}

Braze [gestiona automáticamente los registros de estado de suscripción huérfanos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#how-braze-handles-orphaned-subscription-states) (datos de suscripción almacenados para un número de teléfono o dirección de correo electrónico no vinculados a ningún perfil de usuario) para evitar la herencia no intencionada del estado de suscripción. Esto protege a los usuarios de escenarios en los que un perfil de usuario recién creado hereda incorrectamente el estado de suscripción de un usuario previamente eliminado o no relacionado.

### Asociaciones

#### Chord - Plataforma de datos de los clientes {#chord-customer-data-platform}

[Chord](https://www.chord.co/) proporciona una plataforma de datos de los clientes que captura y estandariza eventos de tu tienda de comercio electrónico. Cuando conectas Chord a Braze, la actividad de compra, los eventos de comportamiento y las actualizaciones de identidad fluyen hacia Braze para que puedas desencadenar campañas y mantener los perfiles actualizados sin construir esos pipelines tú mismo.

Para más información, consulta [Chord]({{site.baseurl}}/partners/chord).

#### Better Email - Plantillas {#better-email-templates}

[Better Email](https://www.betteremail.dev) es una plataforma colaborativa de creación de correo electrónico construida alrededor de un sistema de diseño de correo electrónico. Los equipos pueden diseñar, gestionar y exportar correos electrónicos listos para producción desde un sistema compartido de bloques y estilos, asegurando la consistencia de marca a escala sin depender de desarrolladores o agencias.

Para más información, consulta [Better Email]({{site.baseurl}}/partners/better_email).

#### DailyPlay - Contenido dinámico {#dailyplay-dynamic-content}

[DailyPlay](https://dailyplay.ai/) es una plataforma de gamificación. Úsala para lanzar juegos personalizados y de marca con sistemas de recompensas integrados que profundizan la participación y mejoran la retención.

Para más información, consulta [DailyPlay]({{site.baseurl}}/partners/dailyplay).

### SDK

#### Actualizaciones de última hora del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [Flutter SDK 19.0.0](https://pub.dev/packages/braze_plugin/changelog#1900)
    - La versión mínima de Dart compatible es `2.17.0`.
    - El registro del SDK ahora se controla en la capa de Dart.
    - Actualiza los enlaces del SDK nativo, incluyendo el puente nativo de Android de [Braze Android SDK 41.1.1 a 42.2.0](https://github.com/braze-inc/braze-android-sdk/compare/v41.1.1...v42.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Corrige un fallo.
- [Cordova 16.0.1](https://github.com/braze-inc/braze-cordova-sdk/releases/tag/16.0.1)
    - Corrige la inicialización de iOS al usar `cordova-ios` 8 con la plantilla `SwiftDelegate`.
- [Unity SDK 11.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Actualiza los enlaces del SDK nativo, incluyendo el puente nativo de iOS de Braze [Swift SDK 13.2.0 a 14.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/13.2.0...14.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualiza el puente nativo de Android de [Braze Android SDK 36.0.0 a 42.2.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v42.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - La versión mínima requerida del SDK de Android es 23. Para más información, consulta [Información de versión del SDK de Android de Braze](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information).
    - Se actualizó la versión mínima requerida de Unity a Unity 6 ([6000.0.66f2](https://unity.com/releases/editor/whats-new/6000.0.66f2) o posterior).
    - Se eliminó News Feed.
        - Se eliminaron `RequestFeedRefresh()`, `RequestFeedRefreshFromCache()`, `LogFeedDisplayed()`, `LogCardImpression(string)`, `LogCardClicked(string)`.
    - Corrige errores menores.
- [React Native 20.1.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/20.1.0)
    - Actualiza los enlaces del SDK de Android.
    - Corrige un problema de vinculación en profundidad de notificaciones push.
- [Segment Swift 8.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#800)
    - Actualiza los enlaces del SDK Swift de Braze para que requieran versiones de la denominación `14.0.0+` SemVer.
        - Esto permite la compatibilidad con cualquier versión del SDK de Braze desde `14.0.0` hasta, pero sin incluir, `15.0.0`.
        - Consulta la [entrada del registro de cambios para `14.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1400) para más información sobre posibles cambios de última hora.
    - Añade compatibilidad con la autenticación SDK.

{% enddetails %}
{% details 30 de abril de 2026 %}

## Lanzamiento del 30 de abril de 2026 {#april-30-2026-release}

### Datos e informes

#### Adición rápida de usuario para la creación de perfiles individuales {#quick-user-add-for-individual-profile-creation}

{% multi_lang_include release_type.md release="General availability" %}

Ahora puedes crear un perfil de usuario individual desde **Import Users** seleccionando **Quick User Add** e introduciendo un correo electrónico o un ID externo.

Anteriormente, la creación de usuarios desde este flujo de trabajo requería la carga de un CSV o un método de ingesta automatizado.

Para más información, consulta [Importación de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import).

#### Sincronizaciones CDI sin copia para desencadenantes de Canvas {#zero-copy-cdi-syncs-for-canvas-triggers}

{% multi_lang_include release_type.md release="General availability" %}

CDI ahora admite el tipo de datos `Canvas triggers` para la personalización sin copia. Puedes desencadenar Canvas desde datos del almacén o de S3 y pasar campos de contexto sin persistir esos campos en los perfiles de usuario de Braze.

Anteriormente, las sincronizaciones CDI requerían que los datos se escribieran en los perfiles de Braze para este tipo de flujo de trabajo de personalización.

Para más información, consulta [Personalización sin copia usando CDI]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync).

#### Eventos recomendados de comercio electrónico {#ecommerce-recommended-events}

{% multi_lang_include release_type.md release="General availability" %}

Los [eventos recomendados de comercio electrónico]({{site.baseurl}}/user_guide/data/activation/events/recommended_events) cubren seis pasos en el recorrido de compra: `product_viewed`, `cart_updated`, `checkout_started`, `order_placed`, `order_cancelled` y `order_refunded`. Cuando envías estos eventos correctamente, Braze valida los datos y los pone a disposición de un conjunto creciente de características de la plataforma.

### Currents y Datashare {#currents-and-datashare}

#### Nuevas actualizaciones de Currents para Banner y WhatsApp {#new-banner-and-whatsapp-currents-updates}

{% multi_lang_include release_type.md release="General availability" %}

Currents y Datashare ahora incluyen un nuevo evento `Banner.Dismiss` y campos adicionales para los eventos existentes de WhatsApp.

Anteriormente, estos eventos de descarte de Banner y los campos de WhatsApp no estaban disponibles en los datos de exportación.

Para más información, consulta el [registro de cambios de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs).

### Orquestación

#### Traducciones multilingües {#multi-language-translations}

{% multi_lang_include release_type.md release="General availability" %}

Compón [mensajes multilingües]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) con una configuración rápida y única de locales que no requiere código complejo y te permite enviar a todos tus mercados con confianza.

#### Migración de permisos granulares {#granular-permissions-migration}

{% multi_lang_include release_type.md release="General availability" %}

Gestionar quién puede acceder a tu cuenta y realizar acciones específicas es fundamental tanto para la seguridad como para la eficiencia operativa. Para darte más control, Braze está introduciendo [permisos granulares]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/granular_permissions_migration), una forma más flexible y precisa de gestionar el acceso de los usuarios en toda tu cuenta.

#### Componente de Canvas Enviar a destino {#send-to-destination-canvas-component}

{% multi_lang_include release_type.md release="General availability" %}

El [paso Enviar a destino]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) te permite enviar usuarios de un Canvas a otro. Por ejemplo, si tienes dos Canvas que comparten mensajería para ofertas promocionales, puedes usar Enviar a destino para conectar estos Canvas.

#### Mejoras en el contexto de Canvas {#canvas-context-enhancements}

{% multi_lang_include release_type.md release="General availability" %}

En Canvas, ahora puedes hacer referencia a variables de contexto para configurar:

- Un evento de eliminación para Content Cards
- La expiración de Content Cards

Para más detalles, consulta [Creación de tarjetas]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation/?tab=canvas).

#### Comportamiento de avance de validación de entrega para pasos de mensaje {#delivery-validation-advancement-behavior-for-message-steps}

{% multi_lang_include release_type.md release="General availability" %}

Las [validaciones de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) proporcionan una comprobación adicional para confirmar que tu audiencia cumple los criterios de entrega en el momento del envío del mensaje. Si un usuario no cumple las validaciones de entrega establecidas para un paso de mensaje, puedes usar la configuración **Delivery validations advancement behavior** para determinar si el usuario debe avanzar al siguiente paso o salir del Canvas.

#### Límites de velocidad de mensajería del espacio de trabajo {#workspace-messaging-rate-limits}

{% multi_lang_include release_type.md release="General availability" %}

Usa los [límites de velocidad de mensajería del espacio de trabajo]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) para regular la velocidad de entrega de tus mensajes salientes desde tu plataforma y asegurarte de que tus usuarios reciben los mensajes que necesitan. Los límites de velocidad de mensajería del espacio de trabajo se están implementando gradualmente, por lo que es posible que aún no veas estas configuraciones en tu panel.

### Canales y puntos de intervención

#### Constructor de plantillas de WhatsApp {#whatsapp-template-builder}

{% multi_lang_include release_type.md release="Early access" %}

El [constructor de plantillas de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization) te permite crear y enviar plantillas de mensajes de WhatsApp directamente en Braze, sin necesidad de alternar entre Braze y el Meta Business Manager. Después de que Meta apruebe tu plantilla, úsala en tantas campañas y Canvas como desees.

#### Etiquetas de producto, metacampos y colecciones de Shopify {#shopify-product-tags-metafields-and-collections}

{% multi_lang_include release_type.md release="General availability" %}

Ahora puedes [sincronizar etiquetas de producto, colecciones y metacampos de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs) desde tu tienda Shopify a tu catálogo de Braze. Esto proporciona datos de producto más ricos para la personalización, segmentación y mensajería basada en catálogos sin soluciones personalizadas.

### Asociaciones

#### GRAVITY - Datos y análisis - Fidelización {#gravity-data-and-analytics-loyalty}

{% multi_lang_include release_type.md release="General availability" %}

[GRAVTY®](https://www.lji.io/) es una plataforma de fidelización de nivel empresarial de Loyalty Juggernaut Inc. (LJI) que permite a las marcas de comercio minorista, viajes, restaurantes (incluidos los de servicio rápido) y servicios financieros diseñar, gestionar y escalar programas de nueva generación, impulsando un crecimiento medible en la participación, la retención y el valor de duración del ciclo de vida del cliente a través de experiencias personalizadas y basadas en datos.

<!-- Use this section to list any new SDKs or SDK updates that are already released. -->
### SDK

Se han publicado las siguientes actualizaciones del SDK. Para más detalles, consulta los [registros de cambios del SDK]({{site.baseurl}}/releases/sdk_changelogs).

#### Actualizaciones de última hora del SDK

{% multi_lang_include release_type.md release="General availability" %}

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [React Native SDK 19.2.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/19.2.0)
    - Compatibilidad con la inicialización diferida.
- [Android SDK 42.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.0.0)
    - Correcciones de errores para In-App Messages y Banners.
- [Swift SDK 14.1.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/14.1.0)
    - Compatibilidad con descartes de Banner.
- [Web SDK 6.7.0](https://github.com/braze-inc/braze-web-sdk/releases/tag/v6.7.0)
    - Compatibilidad con descartes de Banner.
- [Android SDK 42.1.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.1.0)
    - Compatibilidad con descartes de Banner.
- [Braze Segment Android 17.0.0](https://github.com/braze-inc/braze-segment-android/releases/tag/v17.0.0)
    - Esta es la versión final del plugin Braze Segment Android porque utiliza Analytics-Android, que llegó al fin de soporte en marzo de 2026. Migra al [plugin Braze Segment Kotlin](https://github.com/braze-inc/braze-segment-kotlin), que utiliza [Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin).
    - Actualiza las versiones del SDK nativo.

{% enddetails %}
{% details 2 de abril de 2026 %}

## Lanzamiento del 2 de abril de 2026 {#april-2-2026-release}

### Datos e informes

#### Nuevos campos del canal Banner en eventos de Currents y Datashare {#new-banner-channel-fields-in-currents-and-datashare-events}

Braze añadió campos para los eventos existentes del canal Banner en las exportaciones de Currents y Datashare. Para ver una lista de estas actualizaciones de eventos y campos, consulta [Cambios en la versión 7]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-for-storage).

#### Compatibilidad con los centros de datos de Mixpanel en la UE e India para Currents {#mixpanel-eu-and-india-data-center-support-for-currents}

La integración de Currents con Mixpanel ahora es compatible con los centros de datos de Mixpanel en la UE e India. Cuando configures una integración con Mixpanel, puedes elegir a qué región de Mixpanel envía Braze tus datos. Esta actualización es compatible con la creciente presencia internacional de Mixpanel para los clientes mutuos. Para más información, consulta [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel).

#### Fuentes y sincronizaciones reutilizables de Ingesta de datos en la nube (CDI) {#reusable-cloud-data-ingestion-cdi-sources-and-syncs}

{% multi_lang_include release_type.md release="Early access" %}

La Ingesta de datos en la nube (CDI) tiene un nuevo diseño que separa las fuentes de las sincronizaciones, para que puedas reutilizar una fuente en múltiples sincronizaciones. Las sincronizaciones existentes se migran automáticamente al nuevo modelo de fuentes y sincronizaciones sin tiempo de inactividad. Ve a **Cloud Data Ingestion** > **Sources** para ver, editar o crear fuentes, y luego selecciona una fuente del menú desplegable al crear una sincronización. Este cambio reduce la configuración repetitiva y crea una base para futuras mejoras. Para más información, consulta [Configuración de integraciones de almacén de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#setting-up-data-warehouse-integrations).

### BrazeAI<sup>TM</sup>

#### Enviar tickets de soporte desde BrazeAI Operator<sup>TM</sup> {#file-support-tickets-from-brazeai-operatortm}

{% multi_lang_include release_type.md release="General availability" %}

[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) ahora incluye un flujo para enviar tickets de soporte de Braze sin salir del panel. Para conocer los pasos, el contexto incluido automáticamente y los consejos para una resolución más rápida, consulta [Enviar tickets de soporte con BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets).

### Orquestación

#### Traducciones multilingües

{% multi_lang_include release_type.md release="General availability" %}

Después de añadir locales a tu espacio de trabajo, usa las [traducciones multilingües]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales) para dirigirte a usuarios en diferentes idiomas, todo dentro de un solo push, correo electrónico, Banner, mensaje dentro de la aplicación o Content Block.

![Vistas previas de locales]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

#### Mejoras en el contexto de Canvas

{% multi_lang_include release_type.md release="General availability" %}

En Canvas, ahora puedes hacer referencia a variables de contexto para configurar:

- Una [expiración]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables#set-an-expiration) para Banners y mensajes dentro de la aplicación en un paso de mensaje
- [Retrasos personalizados]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables#action-path-delays) para los pasos de Rutas de Acción

En el campo de nombre de variable de contexto, también puedes escribir el nombre de la variable de contexto o seleccionarlo del menú desplegable en el editor de pasos. Para más detalles, consulta [Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) y [Variables de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables).

### Canales y puntos de intervención

#### KakaoTalk

{% multi_lang_include release_type.md release="General availability" %}

[KakaoTalk]({{site.baseurl}}/kakaotalk) es un canal de mensajería que permite la mensajería de difusión y el chat 1:1 con los usuarios. Crea una experiencia de usuario personalizada utilizando Liquid y otro contenido dinámico para construir un entorno que fomente y mejore una experiencia de usuario enriquecida con tu marca.

![Un mensaje de elemento de lista de KakaoTalk.]({% image_buster /assets/img/kakaotalk/wide_image.png %}){: style="max-width:70%;"}

#### Banners en Canvas {#banners-in-canvas}

{% multi_lang_include release_type.md release="General availability" %}

Puedes usar [Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners) como canal de mensajería en los [pasos de mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) de Canvas. Los Banners te permiten personalizar el contenido de la aplicación o el sitio web de forma dinámica, reflejando la elegibilidad y el comportamiento del usuario en tiempo real.

### Asociaciones

#### CataBoom - Personalización de mensajes - Contenido visual e interactivo {#cataboom-message-personalization-visual-and-interactive-content}

[CataBoom]({{site.baseurl}}/partners/cataboom) es una plataforma de gamificación. Las marcas la utilizan para crear y lanzar experiencias digitales interactivas, como juegos de girar y ganar, cuestionarios y juegos de premio instantáneo. Esas experiencias profundizan la participación y recopilan datos propios.

#### Denada - Orquestación de mensajes - Plantillas {#denada-message-orchestration-templates}

[Denada]({{site.baseurl}}/partners/denada) es una plataforma creativa de marketing impulsada por IA que permite a los expertos en la materia crear materiales de marketing alineados con la marca a través de una conversación natural. Con Denada, los equipos pueden pasar de la ideación al contenido de correo electrónico terminado sin necesidad de experiencia en diseño.

#### Poq - Comercio electrónico - Plataforma de aplicaciones móviles {#poq-ecommerce-mobile-app-platform}

[Poq]({{site.baseurl}}/partners/poq) permite a las empresas lanzar, gestionar y escalar rápidamente aplicaciones nativas completas para iOS y Android, ofreciendo experiencias móviles de alto rendimiento que impulsan el comercio y dan vida a la promesa de tu marca.

#### The Trade Desk – Sincronización de audiencias en Canvas {#the-trade-desk-canvas-audience-sync}

Con la [Sincronización de audiencias de Braze con The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync), puedes sincronizar dinámicamente tus datos de usuario propios desde Braze directamente en The Trade Desk para retargeting de anuncios, modelado de audiencias similares y supresión.

### SDK

#### Conecta tu entorno de desarrollo integrado (IDE) al MCP de Docs {#connect-your-integrated-development-environment-ide-to-the-docs-mcp}

Usa asistentes de codificación con IA para acelerar tu flujo de trabajo de integración con Braze conectando tu entorno de desarrollo integrado (IDE) al MCP de Braze Docs a través de Context7. Esto le da a tu asistente acceso directo a la documentación actual de Braze, para que pueda generar orientación más precisa sobre el SDK, ejemplos de código y ayuda para la solución de problemas en tu entorno de desarrollo. Para los pasos de configuración en Cursor, Claude Desktop y VS Code, consulta [Construir con un LLM]({{site.baseurl}}/developer_guide/getting_started/build_with_llm#connecting-to-the-braze-docs-mcp).

#### Actualizaciones de última hora del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [Cordova 15.0.0](https://github.com/braze-inc/braze-cordova-sdk/releases/tag/15.0.0)
    - Actualizado el puente nativo de Android [de Braze Android SDK 39.0.0 a 41.1.1](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v41.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualizado el puente nativo de iOS [de Braze Swift SDK 13.2.0 a 14.0.1](https://github.com/braze-inc/braze-swift-sdk/compare/13.2.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Corrige un problema con `subscribeToInAppMessage` relacionado con la devolución de llamada de éxito.
- [Roku SDK 2.2.1](https://github.com/braze-inc/braze-roku-sdk/releases/tag/v2.2.1)
    - Corrige un fallo al procesar una solicitud HTTP fallida para mensajes dentro de la aplicación con plantilla mientras el dispositivo tiene conectividad intermitente o nula.
- [Web SDK 6.6.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#660)
    - Añade la opción de inicialización `cookieExpiryInDays` para configurar la duración de las cookies desde el valor predeterminado de 400 días.
- [Flutter SDK 18.0.0](https://pub.dev/packages/braze_plugin/changelog#1800)
    - Añade compatibilidad con la inicialización diferida.
    - Simplifica el proceso de integración de iOS para que no sea necesario escribir código nativo para reenviar actualizaciones de Content Cards, Banners, conmutadores de características, mensajes dentro de la aplicación o notificaciones push desde el SDK nativo.
        - El SDK ahora configurará automáticamente estas suscripciones cuando se cree la instancia de Braze.
        - Esto coincide con el comportamiento existente en Android.
        - Para migrar, elimina cualquier llamada manual a `braze.contentCards.subscribeToUpdates()`, `braze.banners.subscribeToUpdates()`, `braze.notifications.subscribeToUpdates`, `braze.featureFlags.subscribeToUpdates` y `braze.inAppMessagePresenter` en el `AppDelegate`.
        - De forma predeterminada, los mensajes dentro de la aplicación se presentarán. Para anular esto, configura un presentador de mensajes dentro de la aplicación personalizado usando el cierre `postInitialization` en `BrazePlugin.configure(_:postInitialization:)`.
- [Swift SDK 14.0.4](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1404)
    - Corrige un error con la automatización push en la reinicialización del SDK.
    - Corrige un problema en el que las imágenes no válidas en Push Stories no se filtraban.
- [Swift SDK 14.0.3](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1403)

{% enddetails %}

{% details 5 de marzo de 2026 %}

## Lanzamiento del 5 de marzo de 2026 {#march-5-2026-release}

### Datos e informes

#### Nuevo centro de datos {#new-data-center}

{% multi_lang_include release_type.md release="General availability" %}

Braze ha lanzado un nuevo [centro de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_centers): JP-01. Puedes registrarte en centros de datos específicos por región al configurar tu cuenta de Braze.

#### Variables de contexto {#context-variables}

{% multi_lang_include release_type.md release="General availability" %}

Las [variables de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) son datos temporales que puedes crear y usar dentro del recorrido de un usuario a través de un Canvas específico. Cada vez que un usuario entra en el Canvas, incluso si ya ha entrado antes, las variables de contexto se redefinirán en función de los datos de entrada más recientes y la configuración del Canvas. Este enfoque permite que cada entrada al Canvas mantenga su propio contexto independiente, permitiendo que los usuarios tengan múltiples estados activos dentro del mismo recorrido mientras conservan el contexto específico de cada estado.

#### Fuentes de Ingesta de datos en la nube {#cloud-data-ingestion-sources}

{% multi_lang_include release_type.md release="Early access" %}

La [Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#setting-up-cloud-data-ingestion-in-braze) tiene una nueva interfaz que separa las fuentes de las sincronizaciones, permitiéndote reutilizar una sola fuente en cualquier número de sincronizaciones. Esto reduce la configuración duplicada y simplifica la configuración cuando tienes múltiples sincronizaciones. Si tienes sincronizaciones existentes, se migran automáticamente a la nueva estructura de fuentes y sincronizaciones sin tiempo de inactividad. Para empezar, ve a **Cloud Data Ingestion** > **Sources** para ver, editar o crear fuentes, y luego selecciona una fuente del menú desplegable al crear una sincronización.

#### Campos adicionales para eventos de Currents y Data Share {#additional-fields-for-currents-and-data-share-events}

{% multi_lang_include release_type.md release="General availability" %}

Los [eventos de Currents y Data Share]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04) ahora incluyen los siguientes campos nuevos para profundizar los datos disponibles para análisis y sistemas posteriores:

- `agentconsole.AgentExecuted`: Se añadió `error` (string) — una descripción de cualquier error que haya ocurrido.
- `agentconsole.ToolInvocation`: Se añadió `request_id` (string) — un ID único para la solicitud general del LLM y la ejecución completa.
- `users.messages.rcs.InboundReceive`: Se añadió `canvas_variation_name` (string) — el nombre de la variación de Canvas que recibió el usuario.

#### Campos de Campaign y Canvas para Snowflake Data Share {#campaign-and-canvas-fields-for-snowflake-data-share}

{% multi_lang_include release_type.md release="General availability" %}

[Snowflake Data Share]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) ahora incluye campos adicionales que reflejan información de Campaign y Canvas en 66 tablas existentes, incluyendo:

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

#### Validación previa a la importación y reporte de errores de CSV {#csv-pre-import-validation-and-error-reporting}

{% multi_lang_include release_type.md release="General availability" %}

Las [importaciones de usuarios en CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users) ahora admiten validación previa a la importación y reportes de errores detallados. Antes de importar, selecciona **Validate file before importing** en la página **Import Users** — Braze escaneará tu archivo y generará un informe identificando las filas que fallarán completamente (errores) y las filas que tendrán éxito con algunos valores omitidos (advertencias). Puedes descargar el informe, corregir tu CSV y volver a subirlo, o continuar tal cual. Después de que se complete la importación, también estará disponible un informe descargable de las filas que fallaron, con la razón exacta de cada problema.

#### Dashboard de diagnóstico de mensajería {#messaging-diagnostics-dashboard}

{% multi_lang_include release_type.md release="Early access" %}

El [dashboard de diagnóstico de mensajería]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) proporciona un desglose de alto nivel de los resultados de envío de mensajes, permitiéndote detectar tendencias y diagnosticar posibles problemas en tu configuración de mensajería. Este dashboard puede ayudarte a entender por qué los mensajes de tus campañas o Canvas pueden no haberse enviado como se esperaba.

### BrazeAI<sup>TM</sup>

#### Agentes de Braze en la Consola de Agente {#braze-agents-in-agent-console}

{% multi_lang_include release_type.md release="General availability" %}

Los [agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents) son ayudantes impulsados por IA que puedes crear dentro de Braze. Los agentes pueden generar contenido, tomar decisiones inteligentes y enriquecer tus datos para que puedas ofrecer experiencias del cliente más personalizadas. Cuando creas un agente, defines su propósito y estableces las directrices sobre cómo debe comportarse. Una vez activo, el agente puede [desplegarse]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents) en Braze para generar textos personalizados, tomar decisiones en tiempo real o actualizar campos de catálogo.

### Orquestación

#### Permisos granulares de usuario {#granular-user-permissions}

{% multi_lang_include release_type.md release="Early access" %}

Braze está introduciendo [permisos granulares]({{site.baseurl}}/user_guide/administer/global/user_management/permissions), una forma más flexible de gestionar el acceso de los usuarios. Consulta [Migración a permisos granulares]({{site.baseurl}}/granular_permissions_migration) para conocer el proceso de migración, incluyendo cómo se mapean los permisos heredados a los permisos granulares.

#### Limitación de velocidad basada en canal {#channel-based-rate-limiting}

{% multi_lang_include release_type.md release="General availability" %}

Al configurar un límite de velocidad de entrega para una campaña multicanal o Canvas, puedes elegir establecer un límite de velocidad compartido o un [límite basado en canal]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#multichannel-campaigns-and-canvases). Cuando una campaña multicanal o Canvas usa limitación de velocidad basada en canal, el límite de velocidad se aplica a cada uno de los canales seleccionados. Por ejemplo, puedes configurar tu campaña o Canvas para que envíe un máximo de 5.000 webhooks y 2.500 mensajes SMS por minuto en toda la campaña o Canvas.

#### Paso de contexto en Canvas {#canvas-context-step}

{% multi_lang_include release_type.md release="General availability" %}

Los [pasos de contexto en Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) te permiten crear y actualizar una o más variables para un usuario a medida que avanza por un Canvas. Por ejemplo, si tienes un Canvas que gestiona descuentos de temporada, puedes usar una variable de contexto para almacenar un código de descuento diferente cada vez que un usuario entra en el Canvas.

### Canales y puntos de intervención

#### Traducir locales en Content Blocks {#translate-locales-in-content-blocks}

{% multi_lang_include release_type.md release="Early access" %}

Después de añadir locales a tu espacio de trabajo, puedes [dirigirte a usuarios en diferentes idiomas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) todo dentro de un Content Block.

### Asociaciones

#### Algolia - Búsqueda y recomendaciones {#algolia-search-recommendations}

[Algolia]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/algolia) es una plataforma de búsqueda y descubrimiento que ayuda a los desarrolladores a crear experiencias de búsqueda rápidas, relevantes y escalables. Con un potente enfoque API-first, Algolia combina algoritmos de clasificación avanzados con información impulsada por IA para una búsqueda fluida en el sitio, navegación y descubrimiento de contenido personalizado.

#### Anthropic - Proveedor de modelos de IA {#anthropic-ai-model-provider}

[Anthropic]({{site.baseurl}}/partners/ai_model_providers/anthropic) es una empresa de investigación y seguridad de IA que desarrolla Claude, un asistente de IA de próxima generación diseñado para ser útil, honesto y seguro para una amplia gama de tareas lingüísticas.

#### Canva - Personalización de mensajes - Estudio creativo {#canva-message-personalization-creative-studio}

[Canva]({{site.baseurl}}/partners/canva) sincroniza tus imágenes en Canva directamente con la biblioteca multimedia de Braze, optimizando tu flujo de trabajo creativo y manteniendo tus activos visuales actualizados en todos tus canales de mensajería.

#### DOTS.ECO - Recompensas {#dotseco-rewards}

[DOTS.ECO]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/rewards/dots_eco) te permite recompensar a los usuarios con un impacto medioambiental real a través de certificados digitales rastreables. Cada certificado puede incluir metadatos como una URL de certificado compartible y una URL de imagen, para que los usuarios puedan ver (y volver a ver) su prueba de impacto.

#### Figma - Personalización de mensajes - Estudio creativo {#figma-message-personalization-creative-studio}

[Figma]({{site.baseurl}}/partners/figma) es una plataforma de diseño colaborativo que te permite construir, diseñar y crear prototipos de productos. Usa esta integración para enviar imágenes y activos visuales desde Figma directamente a la biblioteca multimedia de Braze.

#### Flybuy - Personalización de mensajes - Ubicación {#flybuy-message-personalization-location}

[Flybuy]({{site.baseurl}}/partners/message_personalization/location/flybuy) de Radius Networks es la plataforma de ubicación omnicanal líder que aprovecha la tecnología impulsada por IA para optimizar la velocidad del servicio en recogida, entrega, autoservicio y servicio en mesa. A través de su Marketing Suite integrado, Flybuy también permite a las marcas entregar mensajes hiperdirigidos basados en el momento, ayudando a impulsar la participación, aumentar el ticket promedio y apoyar iniciativas de fidelización más amplias.

#### Google Gemini - Proveedor de modelos de IA {#google-gemini-ai-model-provider}

[Google Gemini]({{site.baseurl}}/partners/ai_model_providers/google_gemini) es la familia de modelos de IA de Google que combina razonamiento avanzado en texto, código e imágenes para ayudar a las marcas a ofrecer experiencias más inteligentes y personalizadas.

#### Limbik - Personalización de mensajes - Motores de personalización {#limbik-message-personalization-personalization-engines}

[Limbik]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalization_engines/limbik) es tu capa de resonancia de IA — predice cómo las audiencias reales interpretan y responden a mensajes, conceptos y resultados de IA antes de que lleguen al mercado. Impulsado por investigación primaria continua en más de 60 países y más de 25 idiomas, Limbik ofrece audiencias sintéticas validadas por humanos — poblaciones digitales que simulan la respuesta real de la audiencia a velocidad de máquina y con precisión de grado de investigación (95% de confianza, 1,5% a 3% de margen de error). Limbik te da la capacidad de asegurar inmediatamente que tu mensajería resuena con lo que tu audiencia objetivo cree y siente.

#### Linkrunner - Orquestación de mensajes - Atribución {#linkrunner-message-orchestration-attribution}

[Linkrunner]({{site.baseurl}}/partners/message_orchestration/attribution/linkrunner) es una plataforma de atribución y análisis móvil que te ayuda a rastrear y analizar tus campañas de adquisición de usuarios.

#### Mailizio - Orquestación de mensajes - Plantillas {#mailizio-message-orchestration-templates}

[Mailizio]({{site.baseurl}}/partners/message_orchestration/templates/Mailizio) es una plataforma de creación y gestión de correo electrónico que facilita el diseño de contenido reutilizable y seguro para la marca mediante un editor visual intuitivo. Con la integración de Mailizio con Braze, puedes exportar tus bloques de contenido y plantillas de correo electrónico, y luego generar automáticamente mensajes dentro de la aplicación a partir de esos mismos activos, habilitando un despliegue de campañas rápido y totalmente controlado.

#### Open Loyalty - Datos y análisis - Fidelización {#open-loyalty-data-and-analytics-loyalty}

[Open Loyalty]({{site.baseurl}}/partners/data_and_analytics/loyalty/openloyalty) es una plataforma de programas de fidelización basada en la nube que te permite crear y gestionar programas de recompensa y fidelización de clientes. La integración de Braze y Open Loyalty sincroniza los datos de fidelización — como el saldo de puntos, los cambios de nivel y las advertencias de caducidad — directamente en Braze en tiempo real. Esto te permite desencadenar mensajes personalizados (correo electrónico, push, SMS) cuando cambia el estado de fidelización de un usuario.

#### OpenAI - Proveedor de modelos de IA {#openai-ai-model-provider}

[OpenAI]({{site.baseurl}}/partners/ai_model_providers/openai) crea modelos de IA avanzados, como GPT, que permiten la comprensión y generación de lenguaje natural, empoderando a las marcas para construir y escalar interacciones significativas con los clientes.

#### Shopgate - Canales {#shopgate-channels}

[Shopgate]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/shopgate) es una plataforma de comercio móvil y omnicanal que ayuda a los comerciantes a crear aplicaciones de compras y mejorar la eficiencia de las tiendas físicas a través de herramientas de cumplimiento y clienteling, es decir, soporte personalizado al cliente en tienda basado en datos del cliente.

#### Splio - Datos y análisis - Importación de cohortes {#splio-data-and-analytics-cohort-import}

[Splio]({{site.baseurl}}/partners/data_and_analytics/cohort_import/splio) es una herramienta de creación de audiencias que te permite aumentar el número de campañas e ingresos sin perjudicar la experiencia del cliente, y proporciona análisis para rastrear el rendimiento de las campañas de CRM tanto en línea como fuera de línea.

### SDK

#### Actualizaciones de última hora del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [Android SDK 41.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 17.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Swift SDK 14.0.2](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Xamarin SDK 9.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Actualizado el enlace de Android de [Braze Android SDK 37.0.0 a 41.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v41.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualizado el enlace de iOS de [Braze Swift SDK 13.3.0 a 14.0.1](https://github.com/braze-inc/braze-swift-sdk/compare/13.3.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Se añadieron nuevas dependencias transitivas de NuGet requeridas por el SDK de Android de Braze:
        - Xamarin.AndroidX.DataStore.Preferences (1.1.7.1)
        - Xamarin.KotlinX.Serialization.Json.Jvm (1.9.0.2)
        - Xamarin.Kotlin.StdLib se ha actualizado de 2.0.21.3 a 2.3.0.1. Si tu proyecto fija explícitamente este paquete a una versión anterior, necesitarás actualizarlo para evitar errores de restauración.
    - Se eliminó la característica News Feed.
        - Esta característica se eliminó del SDK nativo de Android en la versión [38.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v38.0.0).
        - Esta característica se eliminó del SDK nativo de Swift en la versión [14.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/14.0.0).
    - El caso de enumeración BRZInAppMessageDismissalReason.BRZInAppMessageDismissalReasonWipeData se ha renombrado a BRZInAppMessageDismissalReason.WipeData.
- [Expo Plugin 4.0.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/4.0.0)
    - Esta versión requiere la versión 19.0.0 del SDK de React Native de Braze.
    - (Android) Se corrigió una fuga de memoria en la capa de persistencia de datos.
    - (Android) Se añadió compatibilidad con `Braze.getInitialPushPayload()` para gestionar los vínculos profundos de notificaciones push cuando la aplicación se lanza desde un estado terminado. Esto resuelve un problema en el que los vínculos profundos de las notificaciones push no se gestionaban en Android cuando la aplicación se iniciaba en frío.
- [React Native SDK 19.0.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/19.0.0)
    - Actualiza los enlaces de la versión nativa del SDK Swift de Braze Swift SDK 13.3.0 a 14.0.1.
    - Actualiza los enlaces de la versión nativa del SDK de Android de Braze Android SDK 40.0.2 a 41.0.0.

{% enddetails %}

{% details 5 de febrero de 2026 %}

## Lanzamiento del 5 de febrero de 2026 {#february-5-2026-release}

### BrazeAI<sup>TM</sup>

#### Optimizador de contenidos {#content-optimizer}

{% multi_lang_include release_type.md release="Beta" %}

El [Optimizador de contenidos]({{site.baseurl}}/user_guide/brazeai/content_optimizer) es un paso en Canvas de pruebas de contenido continuo y altamente variante que entrega una optimización automatizada de la participación. Utilizando una interfaz de arrastrar y soltar similar al paso de mensajes, puedes definir los componentes que quieres probar, generar variantes utilizando IA (o introducirlas manualmente), y utilizar etiquetas de Liquid para mapear estos componentes al contenido de tu mensaje.

Basado en un optimizador bandido de brazos múltiples no contextual, el Optimizador de contenidos envía un único mensaje por usuario, determinando qué combinación de variantes de componentes entregar basándose en recomendaciones predictivas. A medida que el paso recopila datos con el tiempo, las variantes de alto rendimiento aumentan de forma natural la asignación de envíos, mientras que las variantes de bajo rendimiento disminuyen. El Optimizador de contenidos funciona mejor con Canvas de envío repetido que tengan un volumen de usuarios diario constante (al menos unos miles de usuarios al día) para habilitar la optimización continua.

### Datos e informes

#### Eventos recomendados de comercio electrónico

{% multi_lang_include release_type.md release="Early access" %}

Para hacer coincidir los eventos recomendados de comercio electrónico con el evento de compra existente, añadimos el [evento de conversión "Realiza pedido"]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases#conversions-dashboard), que es similar a "Realiza compra".

### Canales y puntos de intervención

#### Traducir locales en banners {#translate-locales-in-banners}

{% multi_lang_include release_type.md release="Early access" %}

Después de añadir locales a tu espacio de trabajo, puedes [dirigirte a usuarios en diferentes idiomas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#use-locales), todo dentro de un mismo banner.

#### Configurar la anchura de los Content Blocks de arrastrar y soltar {#configure-width-for-drag-and-drop-content-blocks}

[Ajusta la anchura de tu Content Block]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email) seleccionando el botón en el menú de navegación. La anchura predeterminada es del 100% cuando no se especifica en la configuración global de estilo de tu correo electrónico; de lo contrario, se respetará la configuración global.

![Una flecha de doble cara con una opción para editar la anchura.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### Usa el calentamiento de IP automatizado {#use-automated-ip-warming}

{% multi_lang_include release_type.md release="Early access" %}

Usa el [calentamiento de IP automatizado]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming#automated-ip-warming) para aumentar gradualmente tu volumen de envíos diarios, permitiendo que los proveedores de buzones de entrada aprendan y confíen en tus patrones de envío. Braze envía primero a tus suscriptores más comprometidos, lo que permite que el volumen diario crezca a un ritmo acorde con las mejores prácticas.

### Asociaciones

#### LinkedIn – Sincronización de audiencias en Canvas {#linkedin-canvas-audience-sync}

Con la [Sincronización de audiencias de Braze con LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync), puedes añadir datos de usuarios de tu integración con Braze a las listas de clientes de LinkedIn para entregar anuncios basados en desencadenantes de comportamiento, segmentación y más. Cualquier criterio que normalmente utilizarías para desencadenar un mensaje (como push, correo electrónico, SMS y webhook) en un Canvas de Braze basado en tus datos de usuario puede ahora desencadenar un anuncio para ese usuario en tus listas de clientes de LinkedIn.

#### Oracle Crowdtwist - Datos y análisis {#oracle-crowdtwist-data-analytics}

[Oracle Crowdtwist]({{site.baseurl}}/partners/crowdtwist) es una solución líder de fidelización de clientes nativa en la nube que permite a las marcas ofrecer experiencias del cliente personalizadas. Su solución ofrece más de 100 vías de participación listas para usar, lo que permite a los especialistas en marketing desarrollar rápidamente una visión más completa del cliente.

#### Fullstory - Contenido dinámico {#fullstory-dynamic-content}

La plataforma de datos de comportamiento de [Fullstory]({{site.baseurl}}/partners/fullstory) ayuda a los líderes tecnológicos a tomar decisiones mejores y más informadas. Al inyectar datos de comportamiento digital en su pila de análisis, la tecnología patentada de Fullstory libera el poder de los datos de comportamiento de calidad a escala, transformando cada visita digital en información accionable.

#### Open Loyalty - Datos y análisis {#open-loyalty-data-analytics}

[Open Loyalty]({{site.baseurl}}/partners/openloyalty) es una plataforma de programas de fidelización basada en la nube que te permite crear y gestionar programas de recompensa y fidelización de clientes. La integración de Braze y Open Loyalty sincroniza los datos de fidelización — como el saldo de puntos, los cambios de nivel y las advertencias de caducidad — directamente en Braze en tiempo real. Esto te permite desencadenar mensajes personalizados (correo electrónico, push, SMS) cuando cambia el estado de fidelización de un usuario.

#### DOTS.ECO - Extensiones {#dotseco-extensions}

[DOTS.ECO]({{site.baseurl}}/partners/dots.eco) te permite recompensar a los usuarios con un impacto medioambiental real a través de certificados digitales rastreables. Cada certificado puede incluir metadatos como una URL de certificado compartible y una URL de imagen, para que los usuarios puedan ver (y volver a ver) su prueba de impacto.

#### Mailizio - Orquestación de mensajes {#mailizio-message-orchestration}

[Mailizio]({{site.baseurl}}/partners/mailizio) es una plataforma de creación y gestión de correo electrónico que facilita el diseño de contenido reutilizable y seguro para la marca mediante un editor visual intuitivo. Con la integración de Mailizio con Braze, puedes exportar tus bloques de contenido y plantillas de correo electrónico, y luego generar automáticamente mensajes dentro de la aplicación a partir de esos mismos activos, habilitando un despliegue de campañas rápido y totalmente controlado.

### API {#apis}

#### API POST de la biblioteca multimedia {#media-library-post-apis}

{% multi_lang_include release_type.md release="General availability" %}

Ahora se pueden añadir activos de la biblioteca multimedia a través de la API, lo que permite a los clientes, partners y agencias automatizar más sus flujos de trabajo de creación de mensajes. Usa la [API]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) para subir un archivo de activos directamente o copiar un archivo de una URL existente. Esta característica desbloquea las capacidades de integración y automatización.

### Currents y Datashare

#### Eventos de la Consola de Agente para destinos de almacenamiento y Datashare {#agent-console-events-for-storage-destinations-and-datashare}

{% multi_lang_include release_type.md release="General availability" %}

Ya están disponibles dos nuevos [eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) para los destinos de almacenamiento (AWS S3, GCS y Azure Blob Storage) y Snowflake Datashare: `agentconsole.AgentExecuted` y `agentconsole.ToolInvocation`. Estos eventos te permiten analizar el uso y los detalles de la Consola de Agente en tus sistemas posteriores, ayudándote a comprender y sacar el máximo partido del uso de tus agentes. Los agentes te permiten crear y desplegar agentes inteligentes que pueden realizar tareas específicas en Braze, como generar contenido en Canvas o catálogos y dirigir a los usuarios por diferentes rutas basándose en la toma de decisiones inteligente. Para más información, consulta el [registro de cambios de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Nuevos eventos "Retry" para canales individuales {#new-retry-events-for-individual-channels}

{% multi_lang_include release_type.md release="General availability" %}

Ahora hay nuevos [eventos de reintento]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) disponibles para los canales de correo electrónico, LINE, notificaciones push, SMS, webhooks y WhatsApp. Estos eventos proporcionan visibilidad sobre cuándo la limitación de frecuencia provoca que un mensaje programado se retrase en lugar de cancelarse. Cuando un mensaje pierde prioridad o tiene una limitación de frecuencia, ahora se puede volver a intentar dentro de una ventana de reintento configurada, lo que te da una mejor información sobre los patrones de entrega de mensajes y los impactos de la limitación de frecuencia. Para más información, consulta el [registro de cambios de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Añadir el nuevo campo 'time_ms' al evento TokenStateChange {#add-new-time_ms-field-to-tokenstatechange-event}

{% multi_lang_include release_type.md release="General availability" %}

Se ha añadido un nuevo campo `time_ms` al evento [`users.behaviors.pushnotification.TokenStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) que proporciona una granularidad de milisegundos para el seguimiento de los cambios de estado del token de notificaciones push. Esta precisión mejorada te ayuda a conocer el estado más reciente de un token de notificaciones push cuando se producen varios cambios en el mismo segundo, lo que te da la seguridad en los sistemas posteriores de que tienes el estado de suscripción correcto. Para más información, consulta el [registro de cambios de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Enviar usuario anónimo a destinos de Tealium {#send-anonymous-user-to-tealium-destinations}

{% multi_lang_include release_type.md release="General availability" %}

Los eventos que no tienen definido un ID externo de usuario ahora se pueden transmitir a los destinos de [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1#tealium-for-currents). Cuando seleccionas la casilla "Include events from anonymous users" en tu integración de Currents, los eventos sin ID externo de usuario se enviarán al destino en lugar de suprimirse. Esta capacidad es fundamental para los análisis posteriores y los casos de uso que implican a usuarios no identificados y anónimos.

##### Enviar usuario anónimo a destinos CustomHTTP {#send-anonymous-user-to-customhttp-destinations}

{% multi_lang_include release_type.md release="Beta" %}

Los eventos que no tienen definido un ID externo de usuario ahora se pueden transmitir a destinos CustomHTTP. Cuando seleccionas la casilla "Include events from anonymous users" en tu integración de Currents, los eventos sin ID externo de usuario se enviarán al destino en lugar de suprimirse. Esta capacidad es fundamental para los análisis posteriores y los casos de uso que implican a usuarios no identificados y anónimos.

#### Evento de apertura de correo electrónico — campo "machine_open" {#email-open-event-machine_open-field}

El [evento de apertura de correo electrónico]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events) ahora genera el valor del campo "machine_open" para informar sobre la métrica [_Apertura automática_]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics#machine-opens).

### SDK

Se han publicado las siguientes actualizaciones del SDK. Swift SDK v14.0.1 corrige un problema con el manejo de los enlaces universales. Android SDK v40.2.0 corrige una posible fuga de memoria y resuelve un problema con la apertura de varias sesiones cuando hay actividades transparentes. Expo SDK v3.2.0 añade la opción `forwardUniversalLinks` (predeterminada: false) para configurar el manejo nativo del SDK Swift de los enlaces universales.

#### Actualizaciones de última hora del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [Android SDK 41.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v41.0.0)
    - Se cambió el nombre de `BrazeConfig.Builder.setIsLocationCollectionEnabled()` a `setIsAutomaticLocationCollectionEnabled()`.
    - Se cambió el nombre de `BrazeConfig.isLocationCollectionEnabled` a `isAutomaticLocationCollectionEnabled`.
    - Se cambió el nombre de `BrazeConfigurationProvider.isLocationCollectionEnabled` a `isAutomaticLocationCollectionEnabled`.
- [Android SDK 40.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4020)
- [Expo Plugin 3.2.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
- [Swift SDK 14.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}

{% details 8 de enero de 2026 %}
## Lanzamiento del 8 de enero de 2026 {#january-8-2026-release}

### Datos e informes

#### Actualizaciones de los eventos de Currents {#updates-to-currents-events}

{% multi_lang_include release_type.md release="General availability" %}

En la versión 4 se han introducido los siguientes cambios en Currents:

* Cambios de campo en el tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Se añadió el nuevo campo `string` `push_token`: Token de notificaciones push del evento
* Cambios de campo en el tipo de evento `users.messages.pushnotification.Bounce`:
    * Se añadió el nuevo campo `string` `push_token`: Token de notificaciones push del evento
* Cambios de campo en el tipo de evento `users.messages.pushnotification.Send`:
    * Se añadió el nuevo campo `string` `push_token`: Token de notificaciones push del evento
* Cambios de campo en el tipo de evento `users.messages.rcs.Click`:
    * Se añadió el nuevo campo `string` `canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * El campo `user_phone_number` es ahora *opcional*.
* Cambios de campo en el tipo de evento `users.messages.rcs.InboundReceive`:
    * El campo `user_id` es ahora *opcional*.
* Cambios de campo en el tipo de evento `users.messages.rcs.Rejection`:
    * Se añadió el nuevo campo `string` `canvas_step_message_variation_id`: API ID de la variación del mensaje del paso en Canvas que recibió este usuario

Consulta el [registro de cambios de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) para ver los cambios en los eventos de cada versión.

#### Exportar registros de sincronización por todas las filas {#export-sync-logs-by-all-rows}

{% multi_lang_include release_type.md release="Early access" %}

En el [panel **Sync Log** de la Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs#exporting-sync-logs), puedes elegir exportar los registros a nivel de fila de una ejecución de sincronización por:

* **Filas con errores:** Descarga un archivo que contiene solo las filas que tenían un estado de **Error**.
* **Todas las filas:** Descarga un archivo que contiene todas las filas procesadas en la ejecución.

### Canales y puntos de intervención

#### Conector WhatsApp "Trae tu propio" (BYO) {#bring-your-own-byo-whatsapp-connector}

El [conector Bring Your Own (BYO) WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/byo_connector) ofrece una asociación entre Braze e Infobip, en la que das acceso a Braze a tu administrador de negocios WhatsApp de Infobip (WABA). Esto te permite gestionar y pagar los costes de mensajería directamente con Infobip mientras utilizas Braze para la segmentación, personalización y orquestación de campañas.

#### Banners en Canvas

{% multi_lang_include release_type.md release="Early access" %}

Selecciona **Banners** como canal de mensajería en un [paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) en Canvas. Usa el editor de arrastrar y soltar para crear mensajes personalizados en línea, proporcionando experiencias no intrusivas y contextualmente relevantes que se actualizan automáticamente al inicio de cada sesión de usuario.

#### CCO dinámico {#dynamic-bcc}

{% multi_lang_include release_type.md release="General availability" %}

Con el [CCO dinámico]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/?tab=bcc%20address#dynamic-bcc), puedes usar Liquid en tu dirección CCO. Ten en cuenta que esta característica solo está disponible en **Email Preferences** y no se puede configurar en la propia campaña. Solo se permite una dirección CCO por destinatario de correo electrónico.

#### Límites de velocidad basados en canal {#channel-based-rate-limits}

Como alternativa a un límite de velocidad que se comparte en toda una campaña multicanal o Canvas, puedes seleccionar un límite de velocidad específico por canal. En este caso, el límite de velocidad se aplicará a cada uno de tus canales seleccionados. Por ejemplo, puedes configurar tu campaña o Canvas para que envíe un máximo de 5.000 webhooks y 2.500 mensajes SMS por minuto en toda la campaña o Canvas. Para más detalles, consulta [Limitación de velocidad y limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### Asociaciones

#### LILT - Localización {#lilt-localization}

[LILT]({{site.baseurl}}/partners/lilt) es la solución completa de IA para la traducción y la creación de contenidos empresariales. LILT permite a las organizaciones globales escalar y optimizar sus contenidos, productos, comunicaciones y operaciones de soporte, con agentes de IA y flujos de trabajo totalmente automatizados.

### Actualizaciones de última hora del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [Android 40.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4011)
- [Android SDK 40.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4010)
- [Swift SDK 14.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Elimina News Feed.
        - Esto elimina por completo todos los elementos de la interfaz de usuario, los modelos de datos y las acciones asociadas a News Feed.
- [Web SDK 6.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details 9 de diciembre de 2025 %}

## 9 de diciembre de 2025 {#december-9-2025}

### Datos e informes

#### Añadir Google Tag Manager a una página de destino {#adding-google-tag-manager-to-a-landing-page}

Para añadir Google Tag Manager a tus páginas de destino, añade un bloque de código personalizado a tu página de destino en el editor de arrastrar y soltar, y luego [inserta el código de Tag Manager]({{site.baseurl}}/user_guide/messaging/landing_pages#adding-google-tag-manager-to-a-landing-page) en el bloque.

### Orquestación

#### Caso de uso de SMS con Liquid {#sms-liquid-use-case}

El caso de uso [Responder con mensajes diferentes en función de la palabra clave del SMS entrante]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases#sms-keyword-response) incorpora el procesamiento dinámico de palabras clave del SMS para responder a mensajes entrantes específicos con una copia de mensaje diferente. Por ejemplo, puedes enviar respuestas diferentes cuando alguien envía un mensaje de texto "START" frente a "JOIN".

#### Lista de permitidos para contenido conectado {#allowlisting-for-connected-content}

Puedes añadir a la lista de permitidos URL específicas para usarlas con [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call). Para acceder a esta característica, ponte en contacto con tu administrador de éxito de cliente.

### Canales y puntos de intervención

#### Codificación de caracteres SMS {#sms-character-encoding}

¡Nuestra [calculadora de segmentos SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator) ahora tiene codificación de caracteres! Selecciona **Display Character Encoding** para identificar qué caracteres están codificados como GSM-7 o UCS-2.

![Calculadora de segmentos SMS con un mensaje SMS de muestra introducido en el cuadro de texto y la codificación de caracteres activada.]({% image_buster /assets/img/sms/character_encoding.png %}){: style="max-width:70%;"}

#### Mensajes de WhatsApp con optimización {#whatsapp-messages-with-optimization}

Dado que la API de MM para WhatsApp no ofrece una capacidad de entrega del 100%, es importante saber cómo reorientar a los usuarios que no hayan recibido tu mensaje en otros canales.

Para reorientar a los usuarios, recomendamos crear un segmento de usuarios que no recibieron un mensaje específico. Para ello, filtra por el código de error `131049`, que indica que no se ha enviado un mensaje de plantilla de marketing debido a la aplicación del límite de plantillas de marketing por usuario de WhatsApp. Puedes hacerlo [utilizando Braze Currents o extensiones de segmento SQL]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery#retargeting-users-on-other-braze-channels).

### Asociaciones

#### OtherLevels - Contenido dinámico {#otherlevels-dynamic-content}

[OtherLevels]({{site.baseurl}}/partners/otherlevels) es una plataforma de experiencias que utiliza IA generativa para transformar el modo en que las marcas deportivas, los editores y los operadores conectan con sus clientes, transformando el contenido tradicional en experiencias de video y rich media personalizadas y a escala.

### SDK

#### Actualizaciones de última hora del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [Web SDK 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}