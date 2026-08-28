---
nav_title: Inicio
article_title: Novedades en Braze
description: "Las notas de la versión de Braze se publican mensualmente para que puedas estar al día de los principales lanzamientos de producto, las mejoras continuas del producto y las asociaciones de Braze."
page_order: 0
search_rank: 1
page_type: reference
---

# Novedades en Braze {#whats-new-in-braze}

{% alert tip %}
Para obtener más información sobre cualquiera de las actualizaciones enumeradas en esta página, ponte en contacto con tu director de cuentas o [abre un ticket de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support). También puedes consultar nuestros [registros de cambios del SDK]({{site.baseurl}}/developer_guide/changelogs) para obtener más información sobre nuestras versiones mensuales del SDK, mejoras y cambios de última hora.
{% endalert %}

{% details 20 de agosto de 2026 %}

## Lanzamiento del 20 de agosto de 2026 {#august-20-2026-release}

### Datos e informes {#data-reporting}

#### Editor SQL de ingesta de datos en la nube {#cloud-data-ingestion-sql-editor}

{% multi_lang_include release_type.md release="General availability" %}

El [editor SQL]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sql_editor) te permite crear y editar sincronizaciones de ingesta de datos en la nube (CDI) escribiendo una consulta SQL contra cualquier tabla o vista en tu almacén de datos, en lugar de construir y mantener una tabla dedicada específica para Braze. Está disponible para todos los tipos de datos de sincronización en todas las fuentes de almacén de datos CDI: Snowflake, Redshift, BigQuery, Databricks y Fabric.

#### Mapeador visual de ingesta de datos en la nube {#cloud-data-ingestion-visual-mapper}

{% multi_lang_include release_type.md release="Beta" %}

El [mapeador visual]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/visual_mapper) te permite crear una sincronización de ingesta de datos en la nube (CDI) mapeando las columnas de una tabla existente del almacén de datos a campos de Braze directamente en el panel, sin necesidad de SQL ni de una tabla dedicada. Esta versión beta admite sincronizaciones de atributos de usuario en todas las fuentes de almacén de datos CDI. El mapeador visual y el editor SQL son complementarios: usa el mapeador visual para el mapeado directo de columna a campo, y el editor SQL para casos avanzados como transformaciones, uniones y lógica condicional.

#### Ingesta de datos en la nube para Google Cloud Storage y Azure Blob Storage {#cloud-data-ingestion-for-google-cloud-storage-and-azure-blob-storage}

{% multi_lang_include release_type.md release="General availability" %}

La ingesta de datos en la nube (CDI) admite dos nuevas fuentes de almacenamiento de archivos: Google Cloud Storage, disponible de forma general ahora, y Azure Blob Storage, disponible la semana del 31 de agosto de 2026. Ambas fuentes funcionan como la fuente existente de Amazon S3 — Braze ingiere los archivos tan pronto como se escriben en el contenedor — para que los clientes en Google Cloud o Azure obtengan la misma velocidad y fiabilidad sin replicar archivos en S3 ni construir una integración personalizada.

#### Ingesta de datos en la nube a BrazeAI Decisioning Studio {#cloud-data-ingestion-to-brazeai-decisioning-studio}

{% multi_lang_include release_type.md release="Early access" %}

La ingesta de datos en la nube (CDI) ahora puede sincronizar datos del almacén de datos directamente a BrazeAI Decisioning Studio para los clientes que usan ambos productos, para que puedas incorporar datos más allá de tu espacio de trabajo de Braze para el aprendizaje por refuerzo y la toma de decisiones con IA sin construir trabajos ETL personalizados. Esta versión de acceso anticipado admite fuentes de Snowflake, con fuentes de almacén de datos adicionales próximamente.

### BrazeAI<sup>TM</sup>

#### Operator puede navegar por el panel por ti {#operator-can-navigate-the-dashboard-for-you}

{% multi_lang_include release_type.md release="General availability" %}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard) puede navegar a una página diferente del panel para completar tu solicitud. Cuando una indicación necesita una parte diferente del panel, Operator identifica el destino, propone la navegación y te lleva allí antes de continuar su trabajo.

Esto permite a Operator encadenar trabajo de varios pasos desde una sola indicación. Por ejemplo, si le pides a Operator desde la página de inicio que configure los ajustes de tu editor de arrastrar y soltar para que coincidan con las directrices de tu marca, te navega a la configuración de correo electrónico correspondiente y continúa ayudándote desde allí.

De forma predeterminada, Operator te pide que apruebes una navegación propuesta antes de moverte a una nueva página. Para permitir que Operator navegue sin esperar tu aprobación cada vez, activa [Aprobación automática de acciones]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions#auto-approve-actions).

#### Operator puede actuar en más páginas del panel {#operator-can-act-on-more-dashboard-pages}

{% multi_lang_include release_type.md release="General availability" %}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) puede completar trabajo desde páginas adicionales del panel cuando describes el resultado en lenguaje natural. Los ejemplos incluyen la creación de informes y dashboards, el trabajo desde páginas de listas de plantillas de correo electrónico y Content Blocks, la importación o gestión de usuarios, la creación de predicciones y la actualización de más superficies de administración y configuración.

Por ejemplo, en la página del generador de informes, pide a Operator que cree un informe que muestre la participación de SMS del espacio de trabajo en los últimos 30 días.

Para una cobertura representativa, consulta [Lo que puedes hacer con Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities). Pregunta a Operator en la página en la que te encuentras para obtener la respuesta más actualizada.

#### Operator puede crear y editar Canvas {#operator-can-create-and-edit-canvases}

{% multi_lang_include release_type.md release="General availability" %}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) puede crear un borrador de Canvas a partir de una descripción en lenguaje natural, y editar un Canvas existente de la misma manera. Describe el recorrido que deseas — criterios de entrada, retrasos y mensajes — y Operator ensambla un borrador que revisas y perfeccionas antes de lanzarlo.

Por ejemplo, pide a Operator que cree un recorrido de carrito abandonado que espere una hora después del abandono del carrito, envíe un recordatorio por correo electrónico y luego un push después de 24 horas si el usuario aún no ha comprado.

Para conocer los pasos compatibles y las limitaciones, consulta [Lo que puedes hacer con Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities).

#### Actualizaciones del paso del optimizador de contenidos {#content-optimizer-step-updates}

{% multi_lang_include release_type.md release="Beta" %}

El paso del [optimizador de contenidos]({{site.baseurl}}/user_guide/brazeai/content_optimizer) incluye las siguientes actualizaciones:

- **Estados del paso:** Los pasos del optimizador de contenidos muestran si están en **Aprendizaje**, **Optimizando** o **Acción recomendada**, para que puedas ver en qué punto se encuentra cada paso.
- **Comprobaciones de configuración previas al lanzamiento:** El optimizador de contenidos comprueba las configuraciones incorrectas clave mientras redactas, para que puedas detectar problemas antes de lanzar.
- **Rastrear qué combinación recibió cada usuario:** Una nueva etiqueta de Liquid y la visibilidad del perfil de usuario te permiten rastrear qué combinación de variantes recibió cada usuario, de principio a fin.
- **Nuevos datos de Currents:** Tres nuevos tipos de eventos te permiten extraer datos del optimizador de contenidos a tu almacén: `users.canvas.costep.Send`, `users.canvas.costep.Conversion` y `contentoptimizer.ComponentStore`.

Para detalles de configuración, consulta [Paso del optimizador de contenidos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step).

### Orquestación {#orchestration}

#### Horas tranquilas del espacio de trabajo {#workspace-quiet-hours}

{% multi_lang_include release_type.md release="Early access" %}

Las [horas tranquilas del espacio de trabajo]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours) te permiten establecer una ventana predeterminada de horas tranquilas para un canal de mensajería en todo tu espacio de trabajo. Cada campaña y Canvas en ese canal respeta la ventana en la zona horaria local de cada destinatario. Puedes mantener el valor predeterminado del espacio de trabajo, o excluirte y aplicar una ventana específica de campaña o Canvas en su lugar.

Los mensajes que se enviarían durante la ventana se retienen para su entrega posterior o se cancelan, dependiendo del tipo de campaña. Las horas tranquilas del espacio de trabajo nunca modifican el contenido del mensaje.

#### Alertas de umbral de Canvas {#canvas-threshold-alerts}

{% multi_lang_include release_type.md release="Early access" %}

Las [alertas de umbral de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/canvas_threshold_alerts) te notifican cuando las entradas de usuarios o los mensajes enviados caen fuera del volumen que esperas. Establece un umbral, elige con qué frecuencia Braze lo comprueba (cada 3 a 12 horas, o cada 24 horas) y recibe notificaciones por correo electrónico, webhook o ambos cuando se cumple una regla. Puedes crear múltiples alertas para el mismo Canvas, incluyendo en borradores — la alerta comienza a comprobar después de que el Canvas se lance.

#### Asignación automática de equipos {#automatic-team-assignment}

{% multi_lang_include release_type.md release="General availability" %}

Para los usuarios con permisos solo a nivel de equipo, Braze puede asignar un [equipo]({{site.baseurl}}/user_guide/administer/global/user_management/teams#automatic-team-assignment) automáticamente durante la creación de objetos.

### Canales y puntos de intervención {#channels-touchpoints}

#### Depurador de contenido conectado {#connected-content-debugger}

{% multi_lang_include release_type.md release="Early access" %}

El [depurador de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/debugger) muestra la solicitud y respuesta en vivo para cada llamada de contenido conectado en **Vista previa y prueba**, para que puedas verificar tu endpoint, encabezados y etiquetas de Liquid antes de lanzar una campaña o Canvas. Abre **Ver detalles** para inspeccionar la URL, el método, el código de estado, los encabezados de solicitud y respuesta, la carga útil, la duración y si la respuesta se sirvió desde la caché.

Durante el acceso anticipado, el depurador está disponible para Content Cards, correo electrónico, mensajes dentro de la aplicación, push, SMS/MMS/RCS, webhooks y WhatsApp.

#### Encuestas en mensajes dentro de la aplicación y páginas de destino {#in-app-message-and-landing-page-surveys}

{% multi_lang_include release_type.md release="General availability" %}

Las encuestas de Braze recopilan comentarios en [mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys) y [páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys) que puedes analizar y usar en mensajería de seguimiento.

#### Mensaje de carrusel de KakaoTalk {#kakaotalk-carousel-message}

{% multi_lang_include release_type.md release="General availability" %}

Un [mensaje de carrusel de KakaoTalk]({{site.baseurl}}/user_guide/channels/kakaotalk/create_kakaotalk_message#step-2-compose-your-kakaotalk-message) incluye hasta seis tarjetas desplazables. Cada tarjeta tiene una imagen, encabezado, mensaje, URL de sitio web opcional y al menos un botón.

#### Mejoras del constructor de plantillas de WhatsApp {#whatsapp-template-builder-improvements}

{% multi_lang_include release_type.md release="General availability" %}

El [constructor de plantillas de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder) admite más rutas de creación y opciones de plantillas:

- **Crear plantillas mientras construyes campañas y Canvas:** Crea una nueva plantilla de WhatsApp directamente en el creador en lugar de solo seleccionar plantillas existentes desde Contenido.
- **Mensajes de respuesta en carrusel:** Crea diseños de carrusel como mensajes de respuesta, no solo como plantillas de salida.
- **Nuevos tipos de plantillas: Utilidad y Flujo:** El constructor de plantillas admite plantillas de utilidad y plantillas de flujo, incluyendo cuando creas plantillas desde campañas, Canvas o la experiencia independiente de plantillas de contenido.

#### Bloques de formulario personalizados y puente JavaScript para páginas de destino {#custom-form-blocks-and-javascript-bridge-for-landing-pages}

{% multi_lang_include release_type.md release="General availability" %}

Las páginas de destino ahora admiten [bloques de formulario personalizados]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks) y un [puente JavaScript]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge), para que puedas capturar entradas de formulario personalizadas y sincronizar eventos y atributos del lado del cliente a través de tu experiencia de página de destino.

#### Formularios de páginas de destino de varios pasos {#multi-step-landing-page-forms}

{% multi_lang_include release_type.md release="General availability" %}

Los [formularios de páginas de destino de varios pasos]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms) te permiten dividir un formulario largo en varios pasos dentro de una sola fila de **Formulario**, con un paso de confirmación integrado después del envío.

#### Bloque Gestionar suscripciones para páginas de destino {#manage-subscriptions-block-for-landing-pages}

{% multi_lang_include release_type.md release="General availability" %}

El bloque [Gestionar suscripciones]({{site.baseurl}}/user_guide/messaging/landing_pages/manage_subscriptions) permite a los usuarios ver, suscribirse y actualizar los grupos de suscripción de correo electrónico en una página de destino.

### Asociaciones {#partnerships}

#### Audience Sync: API de Google Data Manager {#audience-sync-google-data-manager-api}

{% multi_lang_include release_type.md release="Early access" %}

[Audience Sync con Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) admite la API de Google Data Manager en acceso anticipado.

#### Amazon Bedrock - Proveedor de modelos de IA {#amazon-bedrock-ai-model-provider}

[Amazon Bedrock](https://aws.amazon.com/bedrock/) es un servicio de AWS totalmente gestionado que proporciona acceso a modelos fundacionales de las principales empresas de IA a través de una API unificada, para que las marcas puedan construir y escalar aplicaciones de IA generativa en AWS.

Para más información, consulta [Amazon Bedrock]({{site.baseurl}}/partners/amazon_bedrock).

#### Bynder - Orquestación de mensajes - CMS y DAM {#bynder-message-orchestration-cms-and-dam}

[Bynder](https://www.bynder.com) es una plataforma de gestión de activos digitales (DAM) que ayuda a los clientes a crear, gestionar, encontrar y distribuir activos digitales aprobados (imágenes, videos y otros creativos) desde una única fuente de verdad. Cuando se integra con Braze, la extensión Universal Compact View (UCV) de Google Chrome de Bynder permite a los especialistas en marketing buscar y seleccionar activos de Bynder sin salir del panel de Braze. Inserta enlaces a esos activos directamente en campañas y Canvas.

Para más información, consulta [Bynder]({{site.baseurl}}/partners/bynder).

#### Multiplied Media - Personalización de mensajes - Contenido visual e interactivo {#multiplied-media-message-personalization-visual-and-interactive-content}

[Multiplied Media](https://multiplied.media) es un estudio de creatividad y automatización que utiliza tus datos de CRM para crear imágenes, GIF y videos personalizados — un activo único para cada cliente. La integración de Multiplied Media y Braze te permite enviar este contenido multimedia a través de correo electrónico, notificaciones push, mensajes dentro de la aplicación, Content Cards y WhatsApp.

Para más información, consulta [Multiplied Media]({{site.baseurl}}/partners/multiplied_media).

### SDK

Se han publicado las siguientes actualizaciones del SDK. Para más detalles, consulta los [registros de cambios del SDK]({{site.baseurl}}/developer_guide/changelogs).

#### Actualizaciones de última hora del SDK {#sdk-breaking-updates}

Se han publicado las últimas actualizaciones del SDK. Las actualizaciones de última hora se enumeran en la sección de actualizaciones del SDK; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- Unity SDK 12.0.0
    - Se actualizó el puente nativo de iOS [de Braze Swift SDK 14.1.0 a 18.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/14.1.0...18.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Se actualizó el puente nativo de Android [de Braze Android SDK 42.2.0 a 43.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v42.2.0...v43.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- Flutter SDK 22.0.0
    - Actualiza el puente nativo de Android [de Braze Android SDK 42.3.1 a 43.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v42.3.1...v43.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualiza el puente nativo de iOS [de Braze Swift SDK 17.0.0 a 18.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/17.0.0...18.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- Swift SDK 18.0.0-18.1.0
    - Renombra `Braze.Ecommerce.ProductViewedEvent.typeIdentifiers` a `type` en las superficies de API de Swift y Objective-C.
    Renombra los eventos de actualización push-to-start de Live Activities en `Braze.LiveActivities.UpdateEvent.ActivityType`, que se emiten al usar `Braze.LiveActivities.subscribeToStateUpdates(_:)`:
        - `pushToStartOptedOut` a `pushToStartUnregistered`
        - `pushToStartOptOutFlushed` a `pushToStartUnregisterFlushed`

#### Resumen de las características y correcciones recientes del SDK {#summary-of-recent-sdk-features-and-fixes}

- **Swift SDK v18.1.0:** Añade métodos de cierre de sesión de token de notificaciones push, además del método de cierre de sesión push existente, para admitir casos de uso de cierre de sesión adicionales. También actualiza el tipo de evento de comercio electrónico.
- **Flutter SDK v22.0.0:** Actualiza el puente nativo para heredar la funcionalidad de los SDK de Android y Swift.
- **Unity SDK v12.0.0:** Actualiza el puente nativo para heredar la funcionalidad de los SDK de Android y Swift.

Para más detalles, consulta los [registros de cambios del SDK]({{site.baseurl}}/developer_guide/changelogs).
{% enddetails %}
{% details 23 de julio de 2026 %}

## Lanzamiento del 23 de julio de 2026 {#july-23-2026-release}

### Datos e informes

#### Dashboard de diagnóstico de mensajería {#messaging-diagnostics-dashboard}

{% multi_lang_include release_type.md release="General availability" %}

El [dashboard de diagnóstico de mensajería]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) proporciona un desglose de alto nivel de los resultados de envío de mensajes, permitiéndote detectar tendencias y diagnosticar posibles problemas en tu configuración de mensajería. Este dashboard puede ayudarte a entender por qué los mensajes de tus campañas o Canvas pueden no haberse enviado como se esperaba. Ponte en contacto con tu administrador de éxito de cliente para acceder a la característica.

#### Mapeador de eventos personalizados en la importación CSV {#csv-custom-events-mapper}

{% multi_lang_include release_type.md release="General availability" %}

El [flujo de importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#about-csv-import) para eventos personalizados ahora incluye un mapeador que te permite mapear nombres de eventos y encabezados de propiedades de eventos a campos de Braze antes de la importación. Esta actualización alinea la experiencia de eventos personalizados con el flujo de atributos personalizados y reduce la necesidad de reformatear archivos antes de la carga. El flujo incluye subir un CSV, mapear campos y eventos obligatorios, mapear propiedades de eventos y luego seleccionar preferencias de segmentación antes de la importación. Si tu archivo ya coincide con el formato esperado, puedes continuar por el flujo sin realizar cambios de mapeado.

#### El almacenamiento gratuito de catálogos ahora admite hasta 500 MB {#catalogs-free-storage-now-supports-up-to-500-mb}

{% multi_lang_include release_type.md release="General availability" %}

La versión gratuita de los [catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/create#tiers) ahora admite hasta 500 MB de almacenamiento en todos los archivos CSV.

### BrazeAI<sup>TM</sup>

#### Operator ahora puede actualizar las páginas de configuración por ti {#operator-can-now-update-settings-pages-for-you}

{% multi_lang_include release_type.md release="General availability" %}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) ahora puede realizar cambios directamente en más páginas de configuración, para que puedas describir un cambio en lenguaje natural en lugar de navegar por las pantallas de configuración. Las páginas compatibles incluyen:

- Horas tranquilas
- Configuración de push
- Límites de velocidad de mensajería
- Reglas de mensajería y flujos de trabajo de aprobación siempre activos
- Otros identificadores y límites de API
- Información de contacto

Por ejemplo, en la página de horas tranquilas, pide a Operator que configure las horas tranquilas de 9 PM a 8 AM para SMS.

#### Servidor MCP remoto de Braze {#remote-braze-mcp-server}

{% multi_lang_include release_type.md release="Early access" %}

El [servidor MCP de Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server) es una conexión alojada de forma remota que te permite conectar agentes de IA como Claude, ChatGPT, Cursor, VSCode, Codex, Google Antigravity y Claude Code directamente a Braze. A través de lenguaje natural, los agentes pueden leer análisis de campañas, Canvas y segmentos, atributos personalizados, eventos, KPI y catálogos, y crear o actualizar plantillas de correo electrónico, Content Blocks y activos de la biblioteca multimedia. No se expone información personal identificable de perfiles de usuario.

Para conectarte, pega una única URL de endpoint en tu cliente MCP — `https://mcp.braze.com/mcp` para EE. UU. o `https://mcp.braze.eu/mcp` para la UE — y luego inicia sesión con OAuth, incluyendo SSO. El servidor se inicia con las herramientas disponibles.

### Orquestación

#### Alcance de audiencia por equipos {#teams-audience-scoping}

{% multi_lang_include release_type.md release="General availability" %}

La configuración de audiencia de [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) ahora admite múltiples filtros.

### Canales y puntos de intervención

#### Escala de valoración en encuestas para mensajes dentro de la aplicación y páginas de destino {#survey-rating-scale-for-in-app-messages-and-landing-pages}

{% multi_lang_include release_type.md release="Early access" %}

Añade una escala de valoración numérica a un bloque de formulario tanto en [encuestas de páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale) como en [encuestas de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#rating-scale) para capturar sentimiento, satisfacción y probabilidad de recomendación sin código personalizado. Se admiten tres rangos: 1–10, 1–5 y 0–10 (el rango estándar de NPS).

#### Plantillas de oferta por tiempo limitado de WhatsApp {#whatsapp-limited-time-offer-templates}

{% multi_lang_include release_type.md release="General availability" %}

Las [plantillas de oferta por tiempo limitado de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/message_and_image_formats#limited-time-offer-templates) muestran una oferta promocional con límite de tiempo con una cuenta regresiva opcional a medida que la oferta se acerca a su vencimiento. Usa este diseño para promociones con límite de tiempo, como ventas de temporada u ofertas personalizadas según un atributo de usuario.

#### Actualización autoservicio de la versión del SDK de Shopify {#shopify-self-serve-sdk-version-upgrade}

{% multi_lang_include release_type.md release="General availability" %}

Los nuevos clientes de [Shopify]({{site.baseurl}}/partners/ecommerce/shopify) se aprovisionan con las últimas versiones del SDK web de Braze y del SDK de JavaScript durante la configuración. Los clientes existentes pueden ver su versión actual del SDK en la configuración de integración, recibir notificaciones cuando haya una versión más reciente disponible y realizar actualizaciones de autoservicio desde la configuración de integración.

#### Editor HTML para Banners {#html-editor-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

Cuando compones un Banner, ahora puedes crearlo [usando el editor HTML]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#compose-a-banner). El editor HTML es ideal para equipos que ya mantienen sus propias plantillas HTML o desean un control total sobre el marcado y el estilo de los Banners. Puedes escribir o pegar HTML personalizado directamente en el editor.

#### Reemplazar un archivo en la biblioteca multimedia {#replace-a-file-in-the-media-library}

{% multi_lang_include release_type.md release="General availability" %}

Ahora puedes [reemplazar el archivo de un activo existente en la biblioteca multimedia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#replace-a-file) manteniendo estables su URL e ID de activo. Dado que la URL no cambia, cualquier campaña, Canvas, Content Block o plantilla que haga referencia a ese activo refleja automáticamente el archivo actualizado, por lo que no tienes que volver a subirlo ni volver a vincularlo manualmente en todos los lugares donde se usa.

#### Vista de cuadrícula para la biblioteca multimedia {#grid-view-for-the-media-library}

{% multi_lang_include release_type.md release="General availability" %}

La biblioteca multimedia y las bibliotecas de plantillas seleccionadas ahora ofrecen una vista de cuadrícula junto con la vista de lista existente. La vista de cuadrícula muestra los activos como miniaturas con metadatos clave (nombre, tipo, última modificación), lo que facilita encontrar imágenes y creatividades de un vistazo en lugar de por nombre de archivo. El filtrado y la búsqueda funcionan igual en ambas vistas.

#### Compatibilidad de vista previa compartible para más canales {#shareable-preview-support-for-more-channels}

{% multi_lang_include release_type.md release="General availability" %}

La [vista previa compartible]({{site.baseurl}}/user_guide/channels/email/html_editor#step-3b-preview-and-test-your-message) ahora admite los siguientes canales adicionales:

- SMS, MMS y RCS
- WhatsApp
- Push
- Content Cards
- LINE

Desde una campaña o mensaje, genera un enlace y compártelo con revisores que no tengan acceso al panel de Braze — por ejemplo, el equipo de marca, legal o una agencia externa. Los destinatarios abren el enlace en cualquier navegador para ver el mensaje renderizado como lo vería un cliente, incluyendo cualquier personalización de prueba.

#### API de actualización de credenciales push {#push-credentials-update-api}

{% multi_lang_include release_type.md release="General availability" %}

Ahora puedes actualizar las credenciales push de forma programática con el [endpoint de actualización de credenciales push]({{site.baseurl}}/api/endpoints/apps/post_update_push_credential). Cada solicitud actualiza una aplicación y una plataforma (`apple`, `firebase`, `huawei` o `kindle`) y acepta cargas útiles de credenciales como valores codificados en Base64. Esto ayuda a los equipos a gestionar grandes carteras de aplicaciones y políticas de rotación de credenciales sin depender de cargas manuales en el panel.

### Asociaciones

#### Refiner - Encuestas {#refiner-surveys}

[Refiner](https://refiner.io) es una plataforma de encuestas dentro de la aplicación para aplicaciones SaaS y móviles. Permite a los equipos de producto y de voz del cliente lanzar encuestas dirigidas dentro de la aplicación y recopilar continuamente datos de NPS, CSAT, CES, comentarios sobre el producto y datos de usuario de primera mano.

#### Stayfilm - Contenido visual e interactivo {#stayfilm-visual-and-interactive-content}

[Stayfilm](https://www.stayfilm.com/) es una REST API para la producción automatizada y personalizada de video a escala. La plataforma integra datos, imágenes, texto, bandas sonoras, narración y efectos visuales para generar contenido de video personalizado para comercio electrónico, marketplaces, flujos de trabajo de CRM y campañas de marketing.

#### Validity - Datos y análisis {#validity-data-and-analytics}

[Validity Everest](https://www.validity.com/everest/) es una plataforma de capacidad de entrega de correo electrónico que te ayuda a medir la colocación en la bandeja de entrada y proteger tu reputación de envío. La integración de Braze y Validity sincroniza tu lista de semillas de Everest con Braze, siembra automáticamente las campañas y Canvas que califican, y extrae las métricas de participación de vuelta a Validity Inbox para que puedas comparar la colocación basada en semillas con la participación real de los suscriptores.

### SDK

Se han publicado las siguientes actualizaciones del SDK. Para más detalles, consulta los [registros de cambios del SDK]({{site.baseurl}}/developer_guide/changelogs).

#### Actualizaciones de última hora del SDK

Se han publicado las últimas actualizaciones del SDK. Las actualizaciones de última hora se enumeran en la sección de actualizaciones del SDK; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [Android SDK 43.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v43.0.0)
    - Añade los métodos `unregisterPush` y logout.
    - Añade campos adicionales a los eventos de comercio electrónico.
    - Añade retirada exponencial para la carga de imágenes de notificaciones push.
- [Swift SDK 17.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Añade campos adicionales a los eventos de comercio electrónico.
    - Hace que los estados de datos sean predecibles después de la inicialización.
    - Añade accesores no bloqueantes para identificadores de dispositivo y usuario.
    - Elimina la API obsoleta de actualización push-to-start en `Braze.LiveActivities`.
- [Web SDK 6.10.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - Añade los métodos `unregisterPush` y logout.
    - Añade campos adicionales a los eventos de comercio electrónico.
    - Corrige un problema de Banner y Content Cards relacionado con actualizaciones redundantes al inicio.
    - Añade un método público para el descarte de Banners.
- [Flutter SDK 21.0.0](https://github.com/braze-inc/braze-flutter-sdk/releases/tag/v21.0.0)
    - Actualiza el puente nativo de iOS.
    - Elimina métodos obsoletos.
    - Actualiza los controladores `changeUser`, `enableSDK` y `disableSDK` para devolver resultados de finalización.
- [Expo SDK 5.2.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/v5.2.0)
    - Actualiza la aplicación de ejemplo a Expo SDK 56.
- [React Native SDK 22.0.0](https://www.npmjs.com/package/@braze/react-native-sdk/v/22.0.0)
    - Añade compatibilidad con el descarte de Banners.
    - Incluye actualizaciones de bindings.

{% enddetails %}
{% details 25 de junio de 2026 %}

## Lanzamiento del 25 de junio de 2026 {#june-25-2026-release}

### Datos e informes

#### Actualización del nombre de la métrica para Content Cards y Banners {#metric-name-update-for-content-cards-and-banners}

La métrica _Destinatarios únicos_ se ha renombrado a _Impresiones diarias únicas_ para Content Cards y Banners. Las _impresiones diarias únicas_ se refieren al número recibido de Braze y se basan en el `user_id`. Las impresiones diarias únicas se cuentan a nivel de campaña o paso en Canvas. Para más detalles, consulta el [Glosario de métricas]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

#### Eliminación de usuarios {#user-deletion}

{% multi_lang_include release_type.md release="General availability" %}

La [eliminación de usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users) te permite gestionar tu base de datos eliminando perfiles que ya no son necesarios, que se crearon por error o que deben eliminarse por cumplimiento normativo (como GDPR o CCPA).

#### Exclusiones de puntos de datos {#data-point-exclusions}

{% multi_lang_include release_type.md release="General availability" %}

Los [eventos recomendados de comercio electrónico]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events) ya no cuentan como puntos de datos facturables. Puedes adoptar los eventos de comercio electrónico de Braze (`ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started`, `ecommerce.order_placed`, `ecommerce.order_cancelled`, `ecommerce.order_refunded`) sin consumo de puntos de datos.

#### Pestaña Historial de eventos {#event-history-tab}

{% multi_lang_include release_type.md release="General availability" %}

La pestaña **Historial de eventos** en los [perfiles de usuario]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) muestra los eventos personalizados y las compras del usuario de los últimos 30 días (hasta los 100 más recientes). Úsala para confirmar que una integración del SDK o la API está enviando eventos como se espera, depurar por qué un usuario entró (o no) en una campaña o Canvas desencadenados por eventos, o investigar una escalación de soporte sobre un usuario específico.

#### El Centro de capacidad de entrega muestra datos de Microsoft SNDS para clientes de Amazon SES {#deliverability-center-surfaces-microsoft-snds-data-for-amazon-ses-customers}

Para los espacios de trabajo que envían correo electrónico a través de Amazon SES, el [Centro de capacidad de entrega]({{site.baseurl}}/deliverability_center) muestra las métricas de Microsoft SNDS para tus IP de envío dedicadas. Braze rellena hasta 90 días de datos históricos de SNDS cuando esta característica se activa para tu espacio de trabajo.

### BrazeAI<sup>TM</sup>

#### Asistentes unificados de BrazeAI en Operator {#unified-brazeai-assistants-in-operator}

Los asistentes independientes de BrazeAI que se encuentran en todo el panel se han unificado en [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator), estableciendo a Operator como el asistente de IA único para la asistencia de IA generativa orientada al especialista en marketing en todo el panel. Los siguientes asistentes ahora se canalizan a través de Operator:

{% multi_lang_include releases/brazeai_operator_legacy_assistants.md %}

Los puntos de entrada existentes permanecen donde solía estar cada botón de asistente heredado. En lugar de abrir un asistente independiente, estos puntos de entrada ahora abren el panel de Operator con indicaciones dinámicas que están preconfiguradas para tu tarea. Estos puntos de entrada proporcionan una ruta directa a Operator para que puedas usar estas capacidades sin ajustar tus flujos de trabajo existentes.

#### Compatibilidad de Operator con la creación y edición de campañas {#operator-support-for-campaign-creation-and-editing}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator) ahora puede crear y editar campañas completas, no solo componer mensajes. Desde una única indicación en lenguaje natural o un resumen de campaña, Operator construye una campaña lista para revisión de principio a fin — componiendo el mensaje, programando la entrega, segmentando la audiencia y asignando eventos de conversión — y luego resume lo que construyó en el paso de revisión. Anteriormente, Operator podía componer el mensaje (uno de los cinco pasos de creación de una campaña); ahora tiene visibilidad y control sobre los pasos restantes de programación, segmentación, asignación y revisión.

Esta funcionalidad está disponible desde la página **Campaigns** o desde cualquier campaña existente. Como resultado, Operator puede:

{% multi_lang_include releases/brazeai_operator_campaign_creation_prompts.md %}

#### Compatibilidad de Operator con Content Blocks {#operator-support-for-content-blocks}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator) ahora puede crear y editar [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) — los fragmentos reutilizables que construyes una vez y referencias en múltiples mensajes — directamente desde una indicación en lenguaje natural. Desde la página **Content Blocks**, pide a Operator que cree un nuevo Content Block desde cero o edite uno existente, y Operator genera o actualiza el contenido para que lo revises.

#### Plantillas de la consola de agentes creadas con Operator {#agent-console-templates-built-with-operator}

Al crear un agente en la **consola de agentes**, puedes elegir crear un agente personalizado o seleccionar una opción en **Crear un agente con Operator** para usar BrazeAI Operator y aplicar una plantilla inicial. Operator puede preconfigurar instrucciones, campos de salida y contexto para las siguientes plantillas iniciales de la consola de agentes.

Para más detalles, consulta [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).

#### Mejoras en la consola de agentes {#agent-console-enhancements}

Puedes hacer lo siguiente en la [consola de agentes]({{site.baseurl}}/user_guide/brazeai/agents):

{% multi_lang_include releases/brazeai_agent_console_enhancements.md %}

#### Editar un paso del optimizador de contenidos ya lanzado {#edit-a-launched-content-optimizer-step}

{% multi_lang_include release_type.md release="Beta" %}

Después de que tu Canvas se haya lanzado, ahora puedes [actualizar un paso del optimizador de contenidos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step#edit-a-launched-step) para:

{% multi_lang_include messaging/canvas/content_optimizer_launched_step_actions.md %}

### Canales y puntos de intervención

#### Descartes de usuario para Banners {#user-dismissals-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

Puedes permitir que los usuarios descarten manualmente un Banner seleccionando **El Banner se puede descartar** al configurar el comportamiento de descarte. Esta opción es beneficiosa en escenarios en los que deseas promocionar una venta por tiempo limitado para todos los usuarios de la aplicación, pero permitirles descartar el mensaje si no están interesados.

Consulta [Configurar el comportamiento de descarte]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#dismiss-behavior) para obtener detalles sobre cómo habilitar el descarte y personalizar el botón de descarte.

#### Seguimiento de clics personalizado para Banners {#custom-click-tracking-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

Para un seguimiento de clics más granular en Banners, puedes [asignar un identificador personalizado]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#step-32-define-on-click-behavior-optional) a cada elemento interactivo usando el campo **Identificador para informes** en su panel de propiedades.

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

### Asociaciones

#### Convercus - Datos y análisis - Fidelización {#convercus-data-and-analytics-loyalty}

[Convercus]({{site.baseurl}}/partners/data_and_analytics/loyalty/convercus) es una plataforma SaaS de fidelización y cupones que ayuda a las marcas y minoristas a aumentar la frecuencia de compra, el valor del carrito y las tasas de recompra a través de programas de fidelización omnicanal y campañas de cupones personalizadas.

#### Copy Pastd - Orquestación de mensajes - Plantillas {#copy-pastd-message-orchestration-templates}

[Copy Pastd]({{site.baseurl}}/partners/copy_pastd) Building Blocks es un creador de correo electrónico de arrastrar y soltar que envía Content Blocks con Liquid y plantillas completas directamente a tu espacio de trabajo de Braze. Diseña una vez, sincroniza con Braze y reutiliza los mismos componentes en campañas, Canvas y flujos desencadenados sin reconstruir HTML cada vez.

#### Databricks Mosaic - Proveedores de modelos de IA {#databricks-mosaic-ai-model-providers}

[Databricks Mosaic]({{site.baseurl}}/partners/ai_model_providers/databricks_mosaic) es la plataforma unificada de Databricks para construir, desplegar y gestionar modelos de IA y aprendizaje automático a escala en la plataforma de inteligencia de datos de Databricks.

#### DinMo - Datos y análisis - ETL inverso {#dinmo-data-and-analytics-reverse-etl}

[DinMo]({{site.baseurl}}/partners/dinmo) es una plataforma de datos de los clientes (CDP) componible que conecta tu almacén de datos en la nube con Braze a través de ETL inverso (extraer, transformar, cargar). Los equipos de marketing pueden crear segmentos de audiencia a partir de datos del almacén, sincronizar atributos de usuario y eventos en Braze, y mantener los estados de suscripción actualizados sin cargas de CSV ni soporte de ingeniería.

#### EmailShepherd - Orquestación de mensajes - Plantillas {#emailshepherd-message-orchestration-templates}

[EmailShepherd]({{site.baseurl}}/partners/emailshepherd) es una plataforma de creación de correo electrónico agéntica construida sobre tu sistema de diseño de correo electrónico que permite a todo tu equipo de marketing — y a los agentes de IA — producir correos electrónicos alineados con la marca y listos para producción sin cuellos de botella. La integración con Braze publica los correos electrónicos aprobados directamente en tu espacio de trabajo de Braze, para que los especialistas en marketing puedan escalar la producción de correo electrónico en Braze sin sacrificar la consistencia de marca.

#### Talkable - Personalización de mensajes - Referidos {#talkable-message-personalization-referrals}

[Talkable]({{site.baseurl}}/partners/talkable) ayuda a las marcas de consumo a convertir a los clientes satisfechos en un canal de referidos escalable. Con la integración de Braze, las adhesiones voluntarias de correo electrónico de marketing capturadas en las campañas de referidos de Talkable fluyen hacia Braze en tiempo real, proporcionando a tu equipo el consentimiento, el contexto y los datos de campaña que necesitas para dar la bienvenida, segmentar e interactuar con cada nuevo defensor y amigo.

### SDK

Se han publicado las siguientes actualizaciones del SDK. Para más detalles, consulta los [registros de cambios del SDK]({{site.baseurl}}/developer_guide/changelogs).

#### Actualizaciones de última hora del SDK

Se han publicado las últimas actualizaciones del SDK. Las actualizaciones de última hora se enumeran en la sección de actualizaciones del SDK; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

{% multi_lang_include releases/sdk/2026_6_25_26_updates.md %}

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

Puedes usar el [optimizador de contenidos]({{site.baseurl}}/user_guide/brazeai/content_optimizer) para optimizar ganchos, cuerpos y CTA para mensajes SMS, MMS y RCS. El optimizador de contenidos te ayuda a probar y optimizar el contenido de los mensajes a escala, utilizando IA para generar y evaluar grandes volúmenes de variantes de contenido automáticamente.

### Orquestación

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

Se han publicado las últimas actualizaciones del SDK. Las actualizaciones de última hora se enumeran en la sección de actualizaciones del SDK; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

{% multi_lang_include releases/sdk/2026_5_28_26_updates.md %}

{% enddetails %}
{% details 30 de abril de 2026 %}

## Lanzamiento del 30 de abril de 2026 {#april-30-2026-release}

### Datos e informes

#### Adición rápida de usuario para la creación de perfiles individuales {#quick-user-add-for-individual-profile-creation}

{% multi_lang_include release_type.md release="General availability" %}

Ahora puedes crear un perfil de usuario individual desde **Importar usuarios** seleccionando **Adición rápida de usuario** e introduciendo un correo electrónico o un ID externo.

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

Gestionar quién puede acceder a tu cuenta y realizar acciones específicas es fundamental tanto para la seguridad como para la eficiencia operativa. Para darte más control, Braze está introduciendo [permisos granulares]({{site.baseurl}}/user_guide/administer/global/user_management/permissions), una forma más flexible y precisa de gestionar el acceso de los usuarios en toda tu cuenta.

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

Las [validaciones de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) proporcionan una comprobación adicional para confirmar que tu audiencia cumple los criterios de entrega en el momento del envío del mensaje. Si un usuario no cumple las validaciones de entrega establecidas para un paso de mensaje, puedes usar la configuración **Comportamiento de avance de validación de entrega** para determinar si el usuario debe avanzar al siguiente paso o salir del Canvas.

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

Se han publicado las últimas actualizaciones del SDK. Las actualizaciones de última hora se enumeran en la sección de actualizaciones del SDK; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

{% multi_lang_include releases/sdk/2026_4_30_26_updates.md %}

{% enddetails %}
{% details 2 de abril de 2026 %}

## Lanzamiento del 2 de abril de 2026 {#april-2-2026-release}

### Datos e informes

#### Nuevos campos del canal Banner en eventos de Currents y Datashare {#new-banner-channel-fields-in-currents-and-datashare-events}

Braze añadió campos para los eventos existentes del canal Banner en las exportaciones de Currents y Datashare. Para ver una lista de estas actualizaciones de eventos y campos, consulta [Cambios en la versión 7]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-for-storage).

#### Compatibilidad con los centros de datos de Mixpanel en la UE e India para Currents {#mixpanel-eu-and-india-data-center-support-for-currents}

La integración de Currents con Mixpanel ahora es compatible con los centros de datos de Mixpanel en la UE e India. Cuando configures una integración con Mixpanel, puedes elegir a qué región de Mixpanel envía Braze tus datos. Esta actualización es compatible con la creciente presencia internacional de Mixpanel para los clientes mutuos. Para más información, consulta [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel).

#### Fuentes y sincronizaciones reutilizables de ingesta de datos en la nube (CDI) {#reusable-cloud-data-ingestion-cdi-sources-and-syncs}

{% multi_lang_include release_type.md release="Early access" %}

La ingesta de datos en la nube (CDI) tiene un nuevo diseño que separa las fuentes de las sincronizaciones, para que puedas reutilizar una fuente en múltiples sincronizaciones. Las sincronizaciones existentes se migran automáticamente al nuevo modelo de fuentes y sincronizaciones sin tiempo de inactividad. Ve a **Cloud Data Ingestion** > **Sources** para ver, editar o crear fuentes, y luego selecciona una fuente del menú desplegable al crear una sincronización. Este cambio reduce la configuración repetitiva y crea una base para futuras mejoras. Para más información, consulta [Configuración de integraciones de almacén de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#setting-up-data-warehouse-integrations).

### BrazeAI<sup>TM</sup>

#### Enviar tickets de soporte desde BrazeAI Operator<sup>TM</sup> {#file-support-tickets-from-brazeai-operatortm}

{% multi_lang_include release_type.md release="General availability" %}

[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) ahora incluye un flujo para enviar tickets de soporte de Braze sin salir del panel. Para conocer los pasos, el contexto incluido automáticamente y los consejos para una resolución más rápida, consulta [Enviar tickets de soporte con BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets).

### Orquestación

#### Traducciones multilingües

{% multi_lang_include release_type.md release="General availability" %}

Después de añadir locales a tu espacio de trabajo, usa las [traducciones multilingües]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) para dirigirte a usuarios en diferentes idiomas, todo dentro de un solo push, correo electrónico, Banner, mensaje dentro de la aplicación o Content Block.

![Vistas previas de locales]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

#### Mejoras en el contexto de Canvas

{% multi_lang_include release_type.md release="General availability" %}

En Canvas, ahora puedes hacer referencia a variables de contexto para configurar:

- Una [expiración]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) para Banners y mensajes dentro de la aplicación en un paso de mensaje
- [Retrasos personalizados]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) para los pasos de Rutas de Acción

En el campo de nombre de variable de contexto, también puedes escribir el nombre de la variable de contexto o seleccionarlo del menú desplegable en el editor de pasos. Para más detalles, consulta [Contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) y [Variables de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).

### Canales y puntos de intervención

#### KakaoTalk

{% multi_lang_include release_type.md release="General availability" %}

[KakaoTalk]({{site.baseurl}}/kakaotalk) es un canal de mensajería que permite la mensajería de difusión y el chat 1:1 con los usuarios. Crea una experiencia de usuario personalizada utilizando Liquid y otro contenido dinámico para construir un entorno que fomente y mejore una experiencia de usuario enriquecida con tu marca.

![Un mensaje de elemento de lista de KakaoTalk.]({% image_buster /assets/img/kakaotalk/wide_image.png %}){: style="max-width:70%;"}

#### Banners en Canvas {#banners-in-canvas}

{% multi_lang_include release_type.md release="General availability" %}

Puedes usar [Banners]({{site.baseurl}}/user_guide/channels/banners) como canal de mensajería en los [pasos de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) de Canvas. Los Banners te permiten personalizar el contenido de la aplicación o el sitio web de forma dinámica, reflejando la elegibilidad y el comportamiento del usuario en tiempo real.

### Asociaciones

#### CataBoom - Personalización de mensajes - Contenido visual e interactivo {#cataboom-message-personalization-visual-and-interactive-content}

[CataBoom]({{site.baseurl}}/partners/cataboom) es una plataforma de gamificación. Las marcas la utilizan para crear y lanzar experiencias digitales interactivas, como juegos de girar y ganar, cuestionarios y juegos de premio instantáneo. Esas experiencias profundizan la participación y recopilan datos propios.

#### Denada - Orquestación de mensajes - Plantillas {#denada-message-orchestration-templates}

[Denada]({{site.baseurl}}/partners/denada) es una plataforma creativa de marketing impulsada por IA que permite a los expertos en la materia crear materiales de marketing alineados con la marca a través de una conversación natural. Con Denada, los equipos pueden pasar de la ideación al contenido de correo electrónico terminado sin necesidad de experiencia en diseño.

#### Poq - Comercio electrónico - Plataforma de aplicaciones móviles {#poq-ecommerce-mobile-app-platform}

[Poq]({{site.baseurl}}/partners/poq) permite a las empresas lanzar, gestionar y escalar rápidamente aplicaciones nativas completas para iOS y Android, ofreciendo experiencias móviles de alto rendimiento que impulsan el comercio y dan vida a la promesa de tu marca.

#### The Trade Desk – Sincronización de audiencias en Canvas {#the-trade-desk-canvas-audience-sync}

Con la [sincronización de audiencias de Braze con The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync), puedes sincronizar dinámicamente tus datos de usuario propios desde Braze directamente en The Trade Desk para retargeting de anuncios, modelado de audiencias similares y supresión.

### SDK

#### Conecta tu entorno de desarrollo integrado (IDE) al MCP de Docs {#connect-your-integrated-development-environment-ide-to-the-docs-mcp}

Usa asistentes de codificación con IA para acelerar tu flujo de trabajo de integración con Braze conectando tu entorno de desarrollo integrado (IDE) al MCP de Braze Docs a través de Context7. Esto le da a tu asistente acceso directo a la documentación actual de Braze, para que pueda generar orientación más precisa sobre el SDK, ejemplos de código y ayuda para la solución de problemas en tu entorno de desarrollo. Para los pasos de configuración en Cursor, Claude Desktop y VS Code, consulta [Construir con un LLM]({{site.baseurl}}/developer_guide/getting_started/build_with_llm#connecting-to-the-braze-docs-mcp).

#### Actualizaciones de última hora del SDK

Se han publicado las últimas actualizaciones del SDK. Las actualizaciones de última hora se enumeran en la sección de actualizaciones del SDK; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

{% multi_lang_include releases/sdk/2026_4_2_26_updates.md %}

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

#### Fuentes de ingesta de datos en la nube {#cloud-data-ingestion-sources}

{% multi_lang_include release_type.md release="Early access" %}

La [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#setting-up-cloud-data-ingestion-in-braze) tiene una nueva interfaz que separa las fuentes de las sincronizaciones, permitiéndote reutilizar una sola fuente en cualquier número de sincronizaciones. Esto reduce la configuración duplicada y simplifica la configuración cuando tienes múltiples sincronizaciones. Si tienes sincronizaciones existentes, se migran automáticamente a la nueva estructura de fuentes y sincronizaciones sin tiempo de inactividad. Para empezar, ve a **Cloud Data Ingestion** > **Sources** para ver, editar o crear fuentes, y luego selecciona una fuente del menú desplegable al crear una sincronización.

#### Campos adicionales para eventos de Currents y Data Share {#additional-fields-for-currents-and-data-share-events}

{% multi_lang_include release_type.md release="General availability" %}

Los [eventos de Currents y Data Share]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04) ahora incluyen los siguientes campos nuevos para profundizar los datos disponibles para análisis y sistemas posteriores:

{% multi_lang_include releases/currents/2026_3_5_26_field_changes.md %}

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

Las [importaciones de usuarios en CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users) ahora admiten validación previa a la importación y reportes de errores detallados. Antes de importar, selecciona **Validar archivo antes de importar** en la página **Importar usuarios** — Braze escaneará tu archivo y generará un informe identificando las filas que fallarán completamente (errores) y las filas que tendrán éxito con algunos valores omitidos (advertencias). Puedes descargar el informe, corregir tu CSV y volver a subirlo, o continuar tal cual. Después de que se complete la importación, también estará disponible un informe descargable de las filas que fallaron, con la razón exacta de cada problema.

#### Dashboard de diagnóstico de mensajería

{% multi_lang_include release_type.md release="Early access" %}

El [dashboard de diagnóstico de mensajería]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) proporciona un desglose de alto nivel de los resultados de envío de mensajes, permitiéndote detectar tendencias y diagnosticar posibles problemas en tu configuración de mensajería. Este dashboard puede ayudarte a entender por qué los mensajes de tus campañas o Canvas pueden no haberse enviado como se esperaba.

### BrazeAI<sup>TM</sup>

#### Agentes de Braze en la consola de agentes {#braze-agents-in-agent-console}

{% multi_lang_include release_type.md release="General availability" %}

Los [agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents) son ayudantes impulsados por IA que puedes crear dentro de Braze. Los agentes pueden generar contenido, tomar decisiones inteligentes y enriquecer tus datos para que puedas ofrecer experiencias del cliente más personalizadas. Cuando creas un agente, defines su propósito y estableces las directrices sobre cómo debe comportarse. Una vez activo, el agente puede [desplegarse]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents) en Braze para generar textos personalizados, tomar decisiones en tiempo real o actualizar campos de catálogo.

### Orquestación

#### Permisos granulares de usuario {#granular-user-permissions}

{% multi_lang_include release_type.md release="Early access" %}

Braze está introduciendo [permisos granulares]({{site.baseurl}}/user_guide/administer/global/user_management/permissions), una forma más flexible de gestionar el acceso de los usuarios. Consulta [Migración a permisos granulares]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para conocer el proceso de migración, incluyendo cómo se mapean los permisos heredados a los permisos granulares.

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

Se han publicado las últimas actualizaciones del SDK. Las actualizaciones de última hora se enumeran en la sección de actualizaciones del SDK; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

{% multi_lang_include releases/sdk/2026_3_5_26_updates.md %}

{% enddetails %}

{% details 5 de febrero de 2026 %}

## Lanzamiento del 5 de febrero de 2026 {#february-5-2026-release}

### BrazeAI<sup>TM</sup>

#### Optimizador de contenidos {#content-optimizer}

{% multi_lang_include release_type.md release="Beta" %}

El [optimizador de contenidos]({{site.baseurl}}/user_guide/brazeai/content_optimizer) es un paso en Canvas de pruebas de contenido continuo y altamente variante que entrega una optimización automatizada de la participación. Utilizando una interfaz de arrastrar y soltar similar al paso de mensajes, puedes definir los componentes que quieres probar, generar variantes utilizando IA (o introducirlas manualmente) y utilizar etiquetas de Liquid para mapear estos componentes al contenido de tu mensaje.

Basado en un optimizador bandido de brazos múltiples no contextual, el optimizador de contenidos envía un único mensaje por usuario, determinando qué combinación de variantes de componentes entregar basándose en recomendaciones predictivas. A medida que el paso recopila datos con el tiempo, las variantes de alto rendimiento aumentan de forma natural la asignación de envíos, mientras que las variantes de bajo rendimiento disminuyen. El optimizador de contenidos funciona mejor con Canvas de envío repetido que tengan un volumen de usuarios diario constante (al menos unos miles de usuarios al día) para habilitar la optimización continua.

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

![Una flecha de doble sentido con una opción para editar la anchura.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### Usa el calentamiento de IP automatizado {#use-automated-ip-warming}

{% multi_lang_include release_type.md release="Early access" %}

Usa el [calentamiento de IP automatizado]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming#automated-ip-warming) para aumentar gradualmente tu volumen de envíos diarios, permitiendo que los proveedores de buzones de entrada aprendan y confíen en tus patrones de envío. Braze envía primero a tus suscriptores más comprometidos, lo que permite que el volumen diario crezca a un ritmo acorde con las mejores prácticas.

### Asociaciones

#### LinkedIn – Sincronización de audiencias en Canvas {#linkedin-canvas-audience-sync}

Con la [sincronización de audiencias de Braze con LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync), puedes añadir datos de usuarios de tu integración con Braze a las listas de clientes de LinkedIn para entregar anuncios basados en desencadenantes de comportamiento, segmentación y más. Cualquier criterio que normalmente utilizarías para desencadenar un mensaje (como push, correo electrónico, SMS y webhook) en un Canvas de Braze basado en tus datos de usuario puede ahora desencadenar un anuncio para ese usuario en tus listas de clientes de LinkedIn.

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

#### Eventos de la consola de agentes para destinos de almacenamiento y Datashare {#agent-console-events-for-storage-destinations-and-datashare}

{% multi_lang_include release_type.md release="General availability" %}

Ya están disponibles dos nuevos [eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) para los destinos de almacenamiento (AWS S3, GCS y Azure Blob Storage) y Snowflake Datashare: `agentconsole.AgentExecuted` y `agentconsole.ToolInvocation`. Estos eventos te permiten analizar el uso y los detalles de la consola de agentes en tus sistemas posteriores, ayudándote a comprender y sacar el máximo partido del uso de tus agentes. Los agentes te permiten crear y desplegar agentes inteligentes que pueden realizar tareas específicas en Braze, como generar contenido en Canvas o catálogos y dirigir a los usuarios por diferentes rutas basándose en la toma de decisiones inteligente. Para más información, consulta el [registro de cambios de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Nuevos eventos de reintento para canales individuales {#new-retry-events-for-individual-channels}

{% multi_lang_include release_type.md release="General availability" %}

Ahora hay nuevos [eventos de reintento]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) disponibles para los canales de correo electrónico, LINE, notificaciones push, SMS, webhooks y WhatsApp. Estos eventos proporcionan visibilidad sobre cuándo la limitación de frecuencia provoca que un mensaje programado se retrase en lugar de cancelarse. Cuando un mensaje pierde prioridad o tiene una limitación de frecuencia, ahora se puede volver a intentar dentro de una ventana de reintento configurada, lo que te da una mejor información sobre los patrones de entrega de mensajes y los impactos de la limitación de frecuencia. Para más información, consulta el [registro de cambios de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Nuevo campo `time_ms` en el evento TokenStateChange {#add-new-time_ms-field-to-tokenstatechange-event}

{% multi_lang_include release_type.md release="General availability" %}

Se ha añadido un nuevo campo `time_ms` al evento [`users.behaviors.pushnotification.TokenStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) que proporciona una granularidad de milisegundos para el seguimiento de los cambios de estado del token de notificaciones push. Esta precisión mejorada te ayuda a conocer el estado más reciente de un token de notificaciones push cuando se producen varios cambios en el mismo segundo, lo que te da la seguridad en los sistemas posteriores de que tienes el estado de suscripción correcto. Para más información, consulta el [registro de cambios de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Enviar usuario anónimo a destinos de Tealium {#send-anonymous-user-to-tealium-destinations}

{% multi_lang_include release_type.md release="General availability" %}

Los eventos que no tienen definido un ID externo de usuario ahora se pueden transmitir a los destinos de [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1). Cuando seleccionas la casilla "Include events from anonymous users" en tu integración de Currents, los eventos sin ID externo de usuario se enviarán al destino en lugar de suprimirse. Esta capacidad es fundamental para los análisis posteriores y los casos de uso que implican a usuarios no identificados y anónimos.

##### Enviar usuario anónimo a destinos CustomHTTP {#send-anonymous-user-to-customhttp-destinations}

{% multi_lang_include release_type.md release="Beta" %}

Los eventos que no tienen definido un ID externo de usuario ahora se pueden transmitir a destinos CustomHTTP. Cuando seleccionas la casilla "Include events from anonymous users" en tu integración de Currents, los eventos sin ID externo de usuario se enviarán al destino en lugar de suprimirse. Esta capacidad es fundamental para los análisis posteriores y los casos de uso que implican a usuarios no identificados y anónimos.

#### Evento de apertura de correo electrónico — campo "machine_open" {#email-open-event-machine_open-field}

El [evento de apertura de correo electrónico]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events) ahora genera el valor del campo "machine_open" para informar sobre la métrica [_Apertura automática_]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

### SDK

Se han publicado las siguientes actualizaciones del SDK. Swift SDK v14.0.1 corrige un problema con el manejo de los enlaces universales. Android SDK v40.2.0 corrige una posible fuga de memoria y resuelve un problema con la apertura de varias sesiones cuando hay actividades transparentes. Expo SDK v3.2.0 añade la opción `forwardUniversalLinks` (predeterminada: false) para configurar el manejo nativo del SDK Swift de los enlaces universales.

#### Actualizaciones de última hora del SDK

Se han publicado las últimas actualizaciones del SDK. Las actualizaciones de última hora se enumeran en la sección de actualizaciones del SDK; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

{% multi_lang_include releases/sdk/2026_2_5_26_updates.md %}

{% enddetails %}