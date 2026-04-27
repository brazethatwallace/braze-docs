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
Para obtener más información sobre cualquiera de las actualizaciones enumeradas en esta página, ponte en contacto con tu director de cuentas o [abre un ticket de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support/). También puedes consultar nuestros [registros de cambios del SDK]({{site.baseurl}}/developer_guide/changelogs/) para obtener más información sobre nuestras versiones mensuales del SDK, mejoras y cambios de última hora.
{% endalert %}

{% details 2 de abril de 2026 %}

## Lanzamiento del 2 de abril de 2026 {#april-2-2026-release}

### Datos e informes {#data-reporting}

#### Nuevos campos del canal Banner en eventos de Currents y Datashare {#new-banner-channel-fields-in-currents-and-datashare-events}

Braze añadió campos para los eventos existentes del canal Banner en las exportaciones de Currents y Datashare. Para ver una lista de estas actualizaciones de eventos y campos, consulta [Cambios en la versión 7]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-storage).

#### Compatibilidad con los centros de datos de Mixpanel en la UE e India para Currents {#mixpanel-eu-and-india-data-center-support-for-currents}

La integración de Currents con Mixpanel ahora es compatible con los centros de datos de Mixpanel en la UE e India. Cuando configures una integración con Mixpanel, puedes elegir a qué región de Mixpanel envía Braze tus datos. Esta actualización es compatible con la creciente presencia internacional de Mixpanel para los clientes mutuos. Para más información, consulta [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/).

#### Fuentes y sincronizaciones reutilizables de Ingesta de datos en la nube (CDI) {#reusable-cloud-data-ingestion-cdi-sources-and-syncs}

{% multi_lang_include release_type.md release="Early access" %}

La Ingesta de datos en la nube (CDI) tiene un nuevo diseño que separa las fuentes de las sincronizaciones, para que puedas reutilizar una fuente en múltiples sincronizaciones. Las sincronizaciones existentes se migran automáticamente al nuevo modelo de fuentes y sincronizaciones sin tiempo de inactividad. Ve a **Cloud Data Ingestion** > **Sources** para ver, editar o crear fuentes, y luego selecciona una fuente del menú desplegable al crear una sincronización. Este cambio reduce la configuración repetitiva y crea una base para futuras mejoras. Para más información, consulta [Configuración de integraciones de almacén de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/#setting-up-data-warehouse-integrations).

### BrazeAI<sup>TM</sup>

#### Enviar tickets de soporte desde BrazeAI Operator<sup>TM</sup> {#file-support-tickets-from-brazeai-operatortm}

{% multi_lang_include release_type.md release="General availability" %}

[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/) ahora incluye un flujo para enviar tickets de soporte de Braze sin salir del dashboard. Para conocer los pasos, el contexto incluido automáticamente y los consejos para una resolución más rápida, consulta [Enviar tickets de soporte con BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets/).

### Orquestación {#orchestration}

#### Traducciones multilingües {#multi-language-translations}

{% multi_lang_include release_type.md release="General availability" %}

Después de añadir locales a tu espacio de trabajo, usa las [traducciones multilingües]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) para dirigirte a usuarios en diferentes idiomas, todo dentro de un solo push, correo electrónico, Banner, mensaje dentro de la aplicación o Content Block.

![Vistas previas de locales]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

#### Mejoras en el contexto de Canvas {#canvas-context-enhancements}

{% multi_lang_include release_type.md release="General availability" %}

En Canvas, ahora puedes hacer referencia a variables de contexto para configurar:

- Una [expiración]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_variables/#set-an-expiration) para Banners y mensajes dentro de la aplicación en un paso de mensaje
- [Retrasos personalizados]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_variables/#action-path-delays) para los pasos de rutas de acción

En el campo de nombre de variable de contexto, también puedes escribir el nombre de la variable de contexto o seleccionarlo del menú desplegable en el editor de pasos. Para más detalles, consulta [Contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/) y [Variables de contexto]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_variables/).

### Canales y puntos de intervención {#channels-touchpoints}

#### KakaoTalk

{% multi_lang_include release_type.md release="General availability" %}

[KakaoTalk]({{site.baseurl}}/kakaotalk/) es un canal de mensajería que permite la mensajería de difusión y el chat 1:1 con los usuarios. Crea una experiencia de usuario personalizada utilizando Liquid y otro contenido dinámico para construir un entorno que fomente y mejore una experiencia de usuario enriquecida con tu marca.

![Un mensaje de elemento de lista de KakaoTalk.]({% image_buster /assets/img/kakaotalk/wide_image.png %}){: style="max-width:70%;"}

#### Banners en Canvas {#banners-in-canvas}

{% multi_lang_include release_type.md release="General availability" %}

Puedes usar [Banners]({{site.baseurl}}/user_guide/channels/banners/) como canal de mensajería en los [pasos de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) de Canvas. Los Banners te permiten personalizar el contenido de la aplicación o el sitio web de forma dinámica, reflejando la elegibilidad y el comportamiento del usuario en tiempo real.

### Asociaciones {#partnerships}

#### CataBoom - Personalización de mensajes - Contenido visual e interactivo {#cataboom-message-personalization-visual-and-interactive-content}

[CataBoom]({{site.baseurl}}/partners/cataboom/) es una plataforma de gamificación. Las marcas la utilizan para crear y lanzar experiencias digitales interactivas, como juegos de girar y ganar, cuestionarios y juegos de premio instantáneo. Esas experiencias profundizan la interacción y recopilan datos propios.

#### Denada - Orquestación de mensajes - Plantillas {#denada-message-orchestration-templates}

[Denada]({{site.baseurl}}/partners/denada/) es una plataforma creativa de marketing impulsada por IA que permite a los expertos en la materia crear materiales de marketing alineados con la marca a través de una conversación natural. Con Denada, los equipos pueden pasar de la ideación al contenido de correo electrónico terminado sin necesidad de experiencia en diseño.

#### Poq - Comercio electrónico - Plataforma de aplicaciones móviles {#poq-ecommerce-mobile-app-platform}

[Poq]({{site.baseurl}}/partners/poq/) permite a las empresas lanzar, gestionar y escalar rápidamente aplicaciones nativas completas para iOS y Android, ofreciendo experiencias móviles de alto rendimiento que impulsan el comercio y dan vida a la promesa de tu marca.

#### The Trade Desk – Sincronización de audiencias en Canvas {#the-trade-desk-canvas-audience-sync}

Con la [Sincronización de audiencias de Braze con The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync/), puedes sincronizar dinámicamente tus datos de usuario propios desde Braze directamente en The Trade Desk para retargeting de anuncios, modelado de audiencias similares y supresión.

### SDK

#### Conecta tu entorno de desarrollo integrado (IDE) al MCP de Docs {#connect-your-integrated-development-environment-ide-to-the-docs-mcp}

Usa asistentes de codificación con IA para acelerar tu flujo de trabajo de integración con Braze conectando tu entorno de desarrollo integrado (IDE) al MCP de Braze Docs a través de Context7. Esto le da a tu asistente acceso directo a la documentación actual de Braze, para que pueda generar orientación más precisa sobre el SDK, ejemplos de código y ayuda para la solución de problemas en tu entorno de desarrollo. Para los pasos de configuración en Cursor, Claude Desktop y VS Code, consulta [Construir con un LLM]({{site.baseurl}}/developer_guide/getting_started/build_with_llm/#connecting-to-the-braze-docs-mcp).

#### Actualizaciones de última hora del SDK {#sdk-breaking-updates}

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

### Datos e informes {#data-reporting}

#### Nuevo centro de datos {#new-data-center}

{% multi_lang_include release_type.md release="General availability" %}

Braze ha lanzado un nuevo [centro de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_centers/): JP-01. Puedes registrarte en centros de datos específicos por región al configurar tu cuenta de Braze.

#### Variables de contexto {#context-variables}

{% multi_lang_include release_type.md release="General availability" %}

Las [variables de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/) son datos temporales que puedes crear y usar dentro del recorrido de un usuario a través de un Canvas específico. Cada vez que un usuario entra en el Canvas, incluso si ya ha entrado antes, las variables de contexto se redefinirán en función de los datos de entrada más recientes y la configuración del Canvas. Este enfoque permite que cada entrada al Canvas mantenga su propio contexto independiente, permitiendo que los usuarios tengan múltiples estados activos dentro del mismo recorrido mientras conservan el contexto específico de cada estado.

#### Fuentes de Ingesta de datos en la nube {#cloud-data-ingestion-sources}

{% multi_lang_include release_type.md release="Early access" %}

La [Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/#setting-up-cloud-data-ingestion-in-braze) tiene una nueva interfaz que separa las fuentes de las sincronizaciones, permitiéndote reutilizar una sola fuente en cualquier número de sincronizaciones. Esto reduce la configuración duplicada y simplifica la configuración cuando tienes múltiples sincronizaciones. Si tienes sincronizaciones existentes, se migran automáticamente a la nueva estructura de fuentes y sincronizaciones sin tiempo de inactividad. Para empezar, ve a **Cloud Data Ingestion** > **Sources** para ver, editar o crear fuentes, y luego selecciona una fuente del menú desplegable al crear una sincronización.

#### Campos adicionales para eventos de Currents y Data Share {#additional-fields-for-currents-and-data-share-events}

{% multi_lang_include release_type.md release="General availability" %}

Los [eventos de Currents y Data Share]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-in-version-5-release-date-2026-02-04) ahora incluyen los siguientes campos nuevos para profundizar los datos disponibles para análisis y sistemas posteriores:

- `agentconsole.AgentExecuted`: Se añadió `error` (string) — una descripción de cualquier error que haya ocurrido.
- `agentconsole.ToolInvocation`: Se añadió `request_id` (string) — un ID único para la solicitud general del LLM y la ejecución completa.
- `users.messages.rcs.InboundReceive`: Se añadió `canvas_variation_name` (string) — el nombre de la variación de Canvas que recibió el usuario.

#### Campos de Campaigns y Canvas para Snowflake Data Share {#campaign-and-canvas-fields-for-snowflake-data-share}

{% multi_lang_include release_type.md release="General availability" %}

[Snowflake Data Share]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-data-sharing-3) ahora incluye campos adicionales que reflejan información de Campaigns y Canvas en 66 tablas existentes, incluyendo:

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

#### Validación previa a la importación y reporte de errores de CSV {#csv-pre-import-validation-and-error-reporting}

{% multi_lang_include release_type.md release="General availability" %}

Las [importaciones de usuarios en CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/) ahora admiten validación previa a la importación y reportes de errores detallados. Antes de importar, selecciona **Validate file before importing** en la página **Import Users** — Braze escaneará tu archivo y generará un informe identificando las filas que fallarán completamente (errores) y las filas que tendrán éxito con algunos valores omitidos (advertencias). Puedes descargar el informe, corregir tu CSV y volver a subirlo, o continuar tal cual. Después de que se complete la importación, también estará disponible un informe descargable de las filas que fallaron, con la razón exacta de cada problema.

#### Dashboard de diagnóstico de mensajería {#messaging-diagnostics-dashboard}

{% multi_lang_include release_type.md release="Early access" %}

El [dashboard de diagnóstico de mensajería]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard/) proporciona un desglose de alto nivel de los resultados de envío de mensajes, permitiéndote detectar tendencias y diagnosticar posibles problemas en tu configuración de mensajería. Este dashboard puede ayudarte a entender por qué los mensajes de tus campañas o Canvas pueden no haberse enviado como se esperaba.

### BrazeAI<sup>TM</sup>

#### Agentes de Braze en la Consola de Agente {#braze-agents-in-agent-console}

{% multi_lang_include release_type.md release="General availability" %}

Los [agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents/) son ayudantes impulsados por IA que puedes crear dentro de Braze. Los agentes pueden generar contenido, tomar decisiones inteligentes y enriquecer tus datos para que puedas ofrecer experiencias del cliente más personalizadas. Cuando creas un agente, defines su propósito y estableces las directrices sobre cómo debe comportarse. Una vez activo, el agente puede [desplegarse]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/) en Braze para generar textos personalizados, tomar decisiones en tiempo real o actualizar campos de catálogo.

### Orquestación {#orchestration}

#### Permisos granulares de usuario {#granular-user-permissions}

{% multi_lang_include release_type.md release="Early access" %}

Braze está introduciendo [permisos granulares]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/), una forma más flexible de gestionar el acceso de los usuarios. Consulta [Migración a permisos granulares]({{site.baseurl}}/granular_permissions_migration/) para conocer el proceso de migración, incluyendo cómo se mapean los permisos heredados a los permisos granulares.

#### Limitación de velocidad basada en canal {#channel-based-rate-limiting}

{% multi_lang_include release_type.md release="General availability" %}

Al configurar un límite de velocidad de entrega para una campaña multicanal o Canvas, puedes elegir establecer un límite de velocidad compartido o un [límite basado en canal]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#multichannel-campaigns-and-canvases). Cuando una campaña multicanal o Canvas usa limitación de velocidad basada en canal, el límite de velocidad se aplica a cada uno de los canales seleccionados. Por ejemplo, puedes configurar tu campaña o Canvas para que envíe un máximo de 5.000 webhooks y 2.500 mensajes SMS por minuto en toda la campaña o Canvas.

#### Paso de contexto en Canvas {#canvas-context-step}

{% multi_lang_include release_type.md release="General availability" %}

Los [pasos de contexto en Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/) te permiten crear y actualizar una o más variables para un usuario a medida que avanza por un Canvas. Por ejemplo, si tienes un Canvas que gestiona descuentos de temporada, puedes usar una variable de contexto para almacenar un código de descuento diferente cada vez que un usuario entra en el Canvas.

### Canales y puntos de intervención {#channels-touchpoints}

#### Traducir locales en Content Blocks {#translate-locales-in-content-blocks}

{% multi_lang_include release_type.md release="Early access" %}

Después de añadir locales a tu espacio de trabajo, puedes [dirigirte a usuarios en diferentes idiomas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) todo dentro de un Content Block.

### Asociaciones {#partnerships}

#### Algolia - Búsqueda y recomendaciones {#algolia-search-recommendations}

[Algolia]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/algolia/) es una plataforma de búsqueda y descubrimiento que ayuda a los desarrolladores a crear experiencias de búsqueda rápidas, relevantes y escalables. Con un potente enfoque API-first, Algolia combina algoritmos de clasificación avanzados con información impulsada por IA para una búsqueda fluida en el sitio, navegación y descubrimiento de contenido personalizado.

#### Anthropic - Proveedor de modelos de IA {#anthropic-ai-model-provider}

[Anthropic]({{site.baseurl}}/partners/ai_model_providers/anthropic/) es una empresa de investigación y seguridad de IA que desarrolla Claude, un asistente de IA de próxima generación diseñado para ser útil, honesto y seguro para una amplia gama de tareas lingüísticas.

#### Canva - Personalización de mensajes - Estudio creativo {#canva-message-personalization-creative-studio}

[Canva]({{site.baseurl}}/partners/canva/) sincroniza tus imágenes en Canva directamente con la biblioteca multimedia de Braze, optimizando tu flujo de trabajo creativo y manteniendo tus activos visuales actualizados en todos tus canales de mensajería.

#### DOTS.ECO - Recompensas {#dotseco-rewards}

[DOTS.ECO]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/rewards/dots_eco/) te permite recompensar a los usuarios con un impacto medioambiental real a través de certificados digitales rastreables. Cada certificado puede incluir metadatos como una URL de certificado compartible y una URL de imagen, para que los usuarios puedan ver (y volver a ver) su prueba de impacto.

#### Figma - Personalización de mensajes - Estudio creativo {#figma-message-personalization-creative-studio}

[Figma]({{site.baseurl}}/partners/figma/) es una plataforma de diseño colaborativo que te permite construir, diseñar y crear prototipos de productos. Usa esta integración para enviar imágenes y activos visuales desde Figma directamente a la biblioteca multimedia de Braze.

#### Flybuy - Personalización de mensajes - Ubicación {#flybuy-message-personalization-location}

[Flybuy]({{site.baseurl}}/partners/message_personalization/location/flybuy/) de Radius Networks es la plataforma de ubicación omnicanal líder que aprovecha la tecnología impulsada por IA para optimizar la velocidad del servicio en recogida, entrega, autoservicio y servicio en mesa. A través de su Marketing Suite integrado, Flybuy también permite a las marcas entregar mensajes hiperdirigidos basados en el momento, ayudando a impulsar la interacción, aumentar el ticket promedio y apoyar iniciativas de fidelización más amplias.

#### Google Gemini - Proveedor de modelos de IA {#google-gemini-ai-model-provider}

[Google Gemini]({{site.baseurl}}/partners/ai_model_providers/google_gemini/) es la familia de modelos de IA de Google que combina razonamiento avanzado en texto, código e imágenes para ayudar a las marcas a ofrecer experiencias más inteligentes y personalizadas.

#### Limbik - Personalización de mensajes - Motores de personalización {#limbik-message-personalization-personalization-engines}

[Limbik]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalization_engines/limbik/) es tu capa de resonancia de IA — predice cómo las audiencias reales interpretan y responden a mensajes, conceptos y resultados de IA antes de que lleguen al mercado. Impulsado por investigación primaria continua en más de 60 países y más de 25 idiomas, Limbik ofrece audiencias sintéticas validadas por humanos — poblaciones digitales que simulan la respuesta real de la audiencia a velocidad de máquina y con precisión de grado de investigación (95% de confianza, 1,5% a 3% de margen de error). Limbik te da la capacidad de asegurar inmediatamente que tu mensajería resuena con lo que tu audiencia objetivo cree y siente.

#### Linkrunner - Orquestación de mensajes - Atribución {#linkrunner-message-orchestration-attribution}

[Linkrunner]({{site.baseurl}}/partners/message_orchestration/attribution/linkrunner/) es una plataforma de atribución y análisis móvil que te ayuda a rastrear y analizar tus campañas de adquisición de usuarios.

#### Mailizio - Orquestación de mensajes - Plantillas {#mailizio-message-orchestration-templates}

[Mailizio]({{site.baseurl}}/partners/message_orchestration/templates/Mailizio/) es una plataforma de creación y gestión de correo electrónico que facilita el diseño de contenido reutilizable y seguro para la marca mediante un editor visual intuitivo. Con la integración de Mailizio con Braze, puedes exportar tus bloques de contenido y plantillas de correo electrónico, y luego generar automáticamente mensajes dentro de la aplicación a partir de esos mismos activos, habilitando un despliegue de campaña rápido y totalmente controlado.

#### Open Loyalty - Datos y análisis - Fidelización {#open-loyalty-data-and-analytics-loyalty}

[Open Loyalty]({{site.baseurl}}/partners/data_and_analytics/loyalty/openloyalty/) es una plataforma de programas de fidelización basada en la nube que te permite crear y gestionar programas de recompensa y fidelización de clientes. La integración de Braze y Open Loyalty sincroniza los datos de fidelización — como el saldo de puntos, los cambios de nivel y las advertencias de caducidad — directamente en Braze en tiempo real. Esto te permite desencadenar mensajes personalizados (correo electrónico, push, SMS) cuando cambia el estado de fidelización de un usuario.

#### OpenAI - Proveedor de modelos de IA {#openai-ai-model-provider}

[OpenAI]({{site.baseurl}}/partners/ai_model_providers/openai/) crea modelos de IA avanzados, como GPT, que permiten la comprensión y generación de lenguaje natural, empoderando a las marcas para construir y escalar interacciones significativas con los clientes.

#### Shopgate - Canales {#shopgate-channels}

[Shopgate]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/shopgate/) es una plataforma de comercio móvil y omnicanal que ayuda a los comerciantes a crear aplicaciones de compras y mejorar la eficiencia de las tiendas físicas a través de herramientas de cumplimiento y clienteling, es decir, soporte personalizado al cliente en tienda basado en datos del cliente.

#### Splio - Datos y análisis - Importación de cohortes {#splio-data-and-analytics-cohort-import}

[Splio]({{site.baseurl}}/partners/data_and_analytics/cohort_import/splio/) es una herramienta de creación de audiencias que te permite aumentar el número de campañas e ingresos sin perjudicar la experiencia del cliente, y proporciona análisis para rastrear el rendimiento de las campañas de CRM tanto en línea como fuera de línea.

### SDK

#### Actualizaciones de última hora del SDK {#sdk-breaking-updates}

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

El [Optimizador de contenidos]({{site.baseurl}}/user_guide/brazeai/content_optimizer/) es un paso en Canvas de pruebas de contenido continuo y altamente variante que entrega una optimización automatizada de la interacción. Utilizando una interfaz de arrastrar y soltar similar al paso de mensajes, puedes definir los componentes que quieres probar, generar variantes utilizando IA (o introducirlas manualmente), y utilizar etiquetas de Liquid para mapear estos componentes al contenido de tu mensaje.

Basado en un optimizador bandido de brazos múltiples no contextual, el Optimizador de contenidos envía un único mensaje por usuario, determinando qué combinación de variantes de componentes entregar basándose en recomendaciones predictivas. A medida que el paso recopila datos con el tiempo, las variantes de alto rendimiento aumentan de forma natural la asignación de envíos, mientras que las variantes de bajo rendimiento disminuyen. El Optimizador de contenidos funciona mejor con Canvas de envío repetido que tengan un volumen de usuarios diario constante (al menos unos miles de usuarios al día) para habilitar la optimización continua.

### Datos e informes {#data-reporting}

#### Eventos recomendados de comercio electrónico {#ecommerce-recommended-events}

{% multi_lang_include release_type.md release="Early access" %}

Para hacer coincidir los eventos recomendados de comercio electrónico con el evento de compra existente, añadimos el [evento de conversión "Realiza pedido"]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/#conversions-report), que es similar a "Realiza compra".

### Canales y puntos de intervención {#channels-touchpoints}

#### Traducir locales en banners {#translate-locales-in-banners}

{% multi_lang_include release_type.md release="Early access" %}

Después de añadir locales a tu espacio de trabajo, puedes [dirigirte a usuarios en diferentes idiomas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/#translating-locales), todo dentro de un mismo banner.

#### Configurar la anchura de los Content Blocks de arrastrar y soltar {#configure-width-for-drag-and-drop-content-blocks}

[Ajusta la anchura de tu Content Block]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/dnd_editor_blocks/#using-the-editor-to-add-a-content-block) seleccionando el botón en el menú de navegación. La anchura predeterminada es del 100% cuando no se especifica en la configuración global de estilo de tu correo electrónico; de lo contrario, se respetará la configuración global.

![Una flecha de doble cara con una opción para editar la anchura.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### Usa el calentamiento de IP automatizado {#use-automated-ip-warming}

{% multi_lang_include release_type.md release="Early access" %}

Usa el [calentamiento de IP automatizado]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/#automated-ip-warming) para aumentar gradualmente tu volumen de envíos diarios, permitiendo que los proveedores de buzones de entrada aprendan y confíen en tus patrones de envío. Braze envía primero a tus suscriptores más comprometidos, lo que permite que el volumen diario crezca a un ritmo acorde con las mejores prácticas.

### Asociaciones {#partnerships}

#### LinkedIn – Sincronización de audiencias en Canvas {#linkedin-canvas-audience-sync}

Con la [Sincronización de audiencias de Braze con LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/), puedes añadir datos de usuarios de tu integración con Braze a las listas de clientes de LinkedIn para entregar anuncios basados en desencadenantes de comportamiento, segmentación y más. Cualquier criterio que normalmente utilizarías para desencadenar un mensaje (como push, correo electrónico, SMS y webhook) en un Canvas de Braze basado en tus datos de usuario puede ahora desencadenar un anuncio para ese usuario en tus listas de clientes de LinkedIn.

#### Oracle Crowdtwist - Datos y análisis {#oracle-crowdtwist-data-analytics}

[Oracle Crowdtwist]({{site.baseurl}}/partners/crowdtwist/) es una solución líder de fidelización de clientes nativa en la nube que permite a las marcas ofrecer experiencias del cliente personalizadas. Su solución ofrece más de 100 vías de interacción listas para usar, lo que permite a los especialistas en marketing desarrollar rápidamente una visión más completa del cliente.

#### Fullstory - Contenido dinámico {#fullstory-dynamic-content}

La plataforma de datos de comportamiento de [Fullstory]({{site.baseurl}}/partners/fullstory/) ayuda a los líderes tecnológicos a tomar decisiones mejores y más informadas. Al inyectar datos de comportamiento digital en su pila de análisis, la tecnología patentada de Fullstory libera el poder de los datos de comportamiento de calidad a escala, transformando cada visita digital en información accionable.

#### Open Loyalty - Datos y análisis {#open-loyalty-data-analytics}

[Open Loyalty]({{site.baseurl}}/partners/openloyalty/) es una plataforma de programas de fidelización basada en la nube que te permite crear y gestionar programas de recompensa y fidelización de clientes. La integración de Braze y Open Loyalty sincroniza los datos de fidelización — como el saldo de puntos, los cambios de nivel y las advertencias de caducidad — directamente en Braze en tiempo real. Esto te permite desencadenar mensajes personalizados (correo electrónico, push, SMS) cuando cambia el estado de fidelización de un usuario.

#### DOTS.ECO - Extensiones {#dotseco-extensions}

[DOTS.ECO]({{site.baseurl}}/partners/docs.eco) te permite recompensar a los usuarios con un impacto medioambiental real a través de certificados digitales rastreables. Cada certificado puede incluir metadatos como una URL de certificado compartible y una URL de imagen, para que los usuarios puedan ver (y volver a ver) su prueba de impacto.

#### Mailizio - Orquestación de mensajes {#mailizio-message-orchestration}

[Mailizio]({{site.baseurl}}/partners/mailizio/) es una plataforma de creación y gestión de correo electrónico que facilita el diseño de contenido reutilizable y seguro para la marca mediante un editor visual intuitivo. Con la integración de Mailizio con Braze, puedes exportar tus bloques de contenido y plantillas de correo electrónico, y luego generar automáticamente mensajes dentro de la aplicación a partir de esos mismos activos, habilitando un despliegue de campaña rápido y totalmente controlado.

### API {#apis}

#### API POST de la biblioteca multimedia {#media-library-post-apis}

{% multi_lang_include release_type.md release="General availability" %}

Ahora se pueden añadir activos de la biblioteca multimedia a través de la API, lo que permite a los clientes, socios y agencias automatizar más sus flujos de trabajo de creación de mensajes. Usa la [API]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create/) para subir un archivo de activos directamente o copiar un archivo de una URL existente. Esta característica desbloquea las capacidades de integración y automatización.

### Currents y Datashare {#currents-and-datashare}

#### Eventos de la Consola de Agente para destinos de almacenamiento y Datashare {#agent-console-events-for-storage-destinations-and-datashare}

{% multi_lang_include release_type.md release="General availability" %}

Ya están disponibles dos nuevos [eventos](http://braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) para los destinos de almacenamiento (AWS S3, GCS y Azure Blob Storage) y Snowflake Datashare: `agentconsole.AgentExecuted` y `agentconsole.ToolInvocation`. Estos eventos te permiten analizar el uso y los detalles de la Consola de Agente en tus sistemas posteriores, ayudándote a comprender y sacar el máximo partido del uso de tus agentes. Los agentes te permiten crear y desplegar agentes inteligentes que pueden realizar tareas específicas en Braze, como generar contenido en Canvas o catálogos y dirigir a los usuarios por diferentes rutas basándose en decisiones inteligentes. Para más información, consulta el [registro de cambios de Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Nuevos eventos "Retry" para canales individuales {#new-retry-events-for-individual-channels}

{% multi_lang_include release_type.md release="General availability" %}

Ahora hay nuevos [eventos de reintento](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) disponibles para los canales de correo electrónico, LINE, notificaciones push, SMS, webhooks y WhatsApp. Estos eventos proporcionan visibilidad sobre cuándo la limitación de frecuencia provoca que un mensaje programado se retrase en lugar de cancelarse. Cuando un mensaje pierde prioridad o tiene una limitación de frecuencia, ahora se puede volver a intentar dentro de una ventana de reintento configurada, lo que te da una mejor información sobre los patrones de entrega de mensajes y los impactos de la limitación de frecuencia. Para más información, consulta el [registro de cambios de Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Añadir el nuevo campo 'time_ms' al evento TokenStateChange {#add-new-timems-field-to-tokenstatechange-event}

{% multi_lang_include release_type.md release="General availability" %}

Se ha añadido un nuevo campo `time_ms` al evento [`users.behaviors.pushnotification.TokenStateChange`](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) que proporciona una granularidad de milisegundos para el seguimiento de los cambios de estado del token de notificaciones push. Esta precisión mejorada te ayuda a conocer el estado más reciente de un token de notificaciones push cuando se producen varios cambios en el mismo segundo, lo que te da la seguridad en los sistemas posteriores de que tienes el estado de suscripción correcto. Para más información, consulta el [registro de cambios de Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Enviar usuario anónimo a destinos de Tealium {#send-anonymous-user-to-tealium-destinations}

{% multi_lang_include release_type.md release="General availability" %}

Los eventos que no tienen definido un ID externo de usuario ahora se pueden transmitir a los destinos de [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1#tealium-for-currents). Cuando seleccionas la casilla "Include events from anonymous users" en tu integración de Currents, los eventos sin ID externo de usuario se enviarán al destino en lugar de suprimirse. Esta capacidad es fundamental para los análisis posteriores y los casos de uso que implican a usuarios no identificados y anónimos.

##### Enviar usuario anónimo a destinos CustomHTTP {#send-anonymous-user-to-customhttp-destinations}

{% multi_lang_include release_type.md release="Beta" %}

Los eventos que no tienen definido un ID externo de usuario ahora se pueden transmitir a destinos CustomHTTP. Cuando seleccionas la casilla "Include events from anonymous users" en tu integración de Currents, los eventos sin ID externo de usuario se enviarán al destino en lugar de suprimirse. Esta capacidad es fundamental para los análisis posteriores y los casos de uso que implican a usuarios no identificados y anónimos.

#### Evento de apertura de correo electrónico — campo "machine_open" {#email-open-event-machineopen-field}

El [evento de apertura de correo electrónico]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/#email-open-events) ahora genera el valor del campo "machine_open" para informar sobre la métrica [_Apertura automática_]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics/#machine-opens).

### SDK

Se han publicado las siguientes actualizaciones del SDK. Swift SDK v14.0.1 corrige un problema con el manejo de los enlaces universales. Android SDK v40.2.0 corrige una posible fuga de memoria y resuelve un problema con la apertura de varias sesiones cuando hay actividades transparentes. Expo SDK v3.2.0 añade la opción `forwardUniversalLinks` (predeterminada: false) para configurar el manejo nativo del SDK Swift de los enlaces universales.

#### Actualizaciones de última hora del SDK {#sdk-breaking-updates}

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

### Datos e informes {#data-reporting}

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

Consulta el [registro de cambios de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/) para ver los cambios en los eventos de cada versión.

#### Exportar registros de sincronización por todas las filas {#export-sync-logs-by-all-rows}

{% multi_lang_include release_type.md release="Early access" %}

En el [panel **Sync Log** de la Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs), puedes elegir exportar los registros a nivel de fila de una ejecución de sincronización por:

* **Rows with errors:** Descarga un archivo que contiene solo las filas que tenían un estado de **Error**.
* **All rows:** Descarga un archivo que contiene todas las filas procesadas en la ejecución.

### Canales y puntos de intervención {#channels-touchpoints}

#### Conector WhatsApp "Trae tu propio" (BYO) {#bring-your-own-byo-whatsapp-connector}

El [conector Bring Your Own (BYO) WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/byo_connector/) ofrece una asociación entre Braze e Infobip, en la que das acceso a Braze a tu administrador de negocios WhatsApp de Infobip (WABA). Esto te permite gestionar y pagar los costes de mensajería directamente con Infobip mientras utilizas Braze para la segmentación, personalización y orquestación de campañas.

#### Banners en Canvas {#banners-in-canvas}

{% multi_lang_include release_type.md release="Early access" %}

Selecciona **Banners** como canal de mensajería en un [paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) en Canvas. Usa el editor de arrastrar y soltar para crear mensajes personalizados en línea, proporcionando experiencias no intrusivas y contextualmente relevantes que se actualizan automáticamente al inicio de cada sesión de usuario.

#### CCO dinámico {#dynamic-bcc}

{% multi_lang_include release_type.md release="General availability" %}

Con el [CCO dinámico]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/?tab=bcc%20address#dynamic-bcc), puedes usar Liquid en tu dirección CCO. Ten en cuenta que esta característica solo está disponible en **Email Preferences** y no se puede configurar en la propia campaña. Solo se permite una dirección CCO por destinatario de correo electrónico.

#### Límites de velocidad basados en canal {#channel-based-rate-limits}

Como alternativa a un límite de velocidad que se comparte en toda una campaña multicanal o Canvas, puedes seleccionar un límite de velocidad específico por canal. En este caso, el límite de velocidad se aplicará a cada uno de tus canales seleccionados. Por ejemplo, puedes configurar tu campaña o Canvas para que envíe un máximo de 5.000 webhooks y 2.500 mensajes SMS por minuto en toda la campaña o Canvas. Para más detalles, consulta [Limitación de velocidad y limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/).

### Asociaciones {#partnerships}

#### LILT - Localización {#lilt-localization}

[LILT]({{site.baseurl}}/partners/lilt/) es la solución completa de IA para la traducción y la creación de contenidos empresariales. LILT permite a las organizaciones globales escalar y optimizar sus contenidos, productos, comunicaciones y operaciones de soporte, con agentes de IA y flujos de trabajo totalmente automatizados.

### Actualizaciones de última hora del SDK {#sdk-breaking-updates}

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

### Datos e informes {#data-reporting}

#### Añadir Google Tag Manager a una página de destino {#adding-google-tag-manager-to-a-landing-page}

Para añadir Google Tag Manager a tus páginas de destino, añade un bloque de código personalizado a tu página de destino en el editor de arrastrar y soltar, y luego [inserta el código de Tag Manager]({{site.baseurl}}/user_guide/messaging/landing_pages/#adding-google-tag-manager-to-a-landing-page) en el bloque.

### Orquestación {#orchestration}

#### Caso de uso de SMS con Liquid {#sms-liquid-use-case}

El caso de uso [Responder con mensajes diferentes en función de la palabra clave del SMS entrante]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases/#sms-keyword-response) incorpora el procesamiento dinámico de palabras clave del SMS para responder a mensajes entrantes específicos con una copia de mensaje diferente. Por ejemplo, puedes enviar respuestas diferentes cuando alguien envía un mensaje de texto "START" frente a "JOIN".

#### Lista de permitidos para contenido conectado {#allowlisting-for-connected-content}

Puedes añadir a la lista de permitidos URL específicas para usarlas con [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/). Para acceder a esta característica, ponte en contacto con tu administrador del éxito del cliente.

### Canales y puntos de intervención {#channels-touchpoints}

#### Codificación de caracteres SMS {#sms-character-encoding}

¡Nuestra [calculadora de segmentos SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/#segment-calculator) ahora tiene codificación de caracteres! Selecciona **Display Character Encoding** para identificar qué caracteres están codificados como GSM-7 o UCS-2.

![Calculadora de segmentos SMS con un mensaje SMS de muestra introducido en el cuadro de texto y la codificación de caracteres activada.]({% image_buster /assets/img/sms/character_encoding.png %}){: style="max-width:70%;"}

#### Mensajes de WhatsApp con optimización {#whatsapp-messages-with-optimization}

Dado que la API de MM para WhatsApp no ofrece una capacidad de entrega del 100%, es importante saber cómo reorientar a los usuarios que no hayan recibido tu mensaje en otros canales.

Para reorientar a los usuarios, recomendamos crear un segmento de usuarios que no recibieron un mensaje específico. Para ello, filtra por el código de error `131049`, que indica que no se ha enviado un mensaje de plantilla de marketing debido a la aplicación del límite de plantillas de marketing por usuario de WhatsApp. Puedes hacerlo [utilizando Braze Currents o extensiones de segmento SQL]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery/#retargeting-users-on-other-braze-channels).

### Asociaciones {#partnerships}

#### OtherLevels - Contenido dinámico {#otherlevels-dynamic-content}

[OtherLevels]({{site.baseurl}}/partners/otherlevels/) es una plataforma de experiencias que utiliza IA generativa para transformar el modo en que las marcas deportivas, los editores y los operadores conectan con sus clientes, transformando el contenido tradicional en experiencias de video y rich media personalizadas y a escala.

### SDK

#### Actualizaciones de última hora del SDK {#sdk-breaking-updates}

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [Web SDK 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details 11 de noviembre de 2025 %}

## 11 de noviembre de 2025 {#november-11-2025}

### Flexibilidad de los datos {#data-flexibility}

#### Filtro de segmentación `Live Activities Push to Start Registered for App` {#live-activities-push-to-start-registered-for-app-segmentation-filter}

El filtro `Live Activities Push to Start Registered for App` segmenta a tus usuarios en función de si están registrados para iniciar una actividad en vivo a través de notificaciones push de iOS para una aplicación específica.

#### Extensión de segmento RFM SQL {#rfm-sql-segment-extension}

Puedes crear una [extensión de segmento RFM (recencia, frecuencia, monetario)]({{site.baseurl}}/rfm_segments/) para dirigirte a tus mejores usuarios midiendo sus hábitos de compra.

El análisis RFM es una técnica de marketing que identifica a tus mejores usuarios puntuándolos en una escala de 0 a 3 para cada categoría (recencia, frecuencia, monetario), donde 3 es la mejor puntuación y 0 la peor. Los valores de recencia, frecuencia y monetario se basan en los datos de un intervalo de tiempo específico que tú elijas.

#### Atributos personalizados — Valores {#custom-attributes-values}

Cuando visualices un informe de uso, selecciona la [pestaña **Values**]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#values-tab) para ver los valores más altos de los atributos personalizados seleccionados, basados en una muestra de aproximadamente 250.000 usuarios.

#### Registros de sincronización y observabilidad para la Ingesta de datos en la nube {#sync-logs-and-observability-for-cloud-data-ingestion}

{% multi_lang_include release_type.md release="General availability" %}

El [panel de registro de sincronización]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) de la Ingesta de datos en la nube (CDI) te permite supervisar todos los datos procesados por CDI, verificar si los datos se sincronizaron correctamente y diagnosticar cualquier problema con datos "incorrectos" o ausentes.

#### Despliegues de conmutadores de características con múltiples reglas {#multi-rule-feature-flag-rollouts}

Usa [despliegues de conmutadores de características con múltiples reglas]({{site.baseurl}}/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts) para definir una secuencia de reglas para evaluar a los usuarios, lo que permite una segmentación precisa y lanzamientos de características controlados. Este método es ideal para desplegar la misma característica a diversas audiencias.

#### Mapeo a campos de catálogo para bloques de producto de arrastrar y soltar {#mapping-to-catalog-fields-for-drag-and-drop-product-blocks}

En la configuración de tu catálogo, puedes seleccionar el alternador **Product blocks** para [mapear a campos e información específicos]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks/#catalog-setup) de tu catálogo. Esto te permite seleccionar qué campos utilizar como título del producto, URL del producto y URL de la imagen.

#### Eventos de cancelación por limitación de frecuencia en Currents {#frequency-capping-abort-events-in-currents}

Al utilizar Currents, ahora puedes hacer referencia a `abort_type` en los eventos de cancelación del canal. Esto identifica que un mensaje se ha cancelado debido a la limitación de frecuencia e incluye la regla de limitación de frecuencia que ha provocado la cancelación. Esto te ayudará a configurar tus reglas de limitación de frecuencia. Consulta [Eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) para obtener detalles específicos de los eventos de Currents.

### Canales robustos {#robust-channels}

#### Imágenes de fondo de fila {#background-row-images}

{% multi_lang_include release_type.md release="General availability" %}

Puedes [añadir una imagen de fondo de fila]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/#background-image) a un mensaje dentro de la aplicación o a una página de destino en el panel de **Row properties**. Activa **Background image** y luego proporciona una URL de imagen o selecciona una imagen de la [biblioteca multimedia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/). Por último, configura el texto alternativo, el tamaño, la posición y si la imagen se repite para crear patrones en toda la fila.

![Una imagen de fondo en fila de una pizza que tiene un patrón de repetición horizontal.]({% image_buster /assets/img_archive/background_row.png %})

#### Copiar enlace de vista previa {#copy-preview-link}

Usa **Copy preview link** en tus [Banners]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#step-5-test-your-message-optional), [pies de página personalizados de correo electrónico]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer/#creating-your-custom-footer) y [páginas de adhesión voluntaria y cancelación de suscripción]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/?tab=custom%20footer#subscription-pages-and-footers) para generar un enlace compartible que muestre el aspecto que tendrá tu contenido para un usuario cualquiera.

#### Mensajes de WhatsApp con entrega optimizada {#whatsapp-messages-with-optimized-delivery}

Usa los avanzados sistemas de IA de Meta para entregar tus mensajes de marketing a más usuarios que tengan más probabilidades de interactuar con ellos, aumentando significativamente la capacidad de entrega y la interacción con los mensajes.

[Los mensajes de WhatsApp con entrega optimizada]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery/) se envían utilizando la nueva [Marketing Messages Lite API](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) de Meta, que proporciona un rendimiento superior en comparación con la API tradicional en la nube. Este nuevo canal de envío te ayuda a llegar mejor a los usuarios que valoran y quieren recibir tus mensajes.

#### WhatsApp Flows

Al incorporar un mensaje de WhatsApp Flow a un Canvas de Braze o a una campaña, puede que quieras capturar y utilizar información específica que los usuarios envíen a través del Flow. Braze necesita recibir información adicional sobre la estructura de la respuesta del usuario, concretamente sobre la forma prevista de la respuesta JSON, para generar el esquema de atributos personalizados anidados (NCA) requerido.

Ahora puedes dar a Braze la información sobre la estructura de la respuesta [guardando la respuesta del Flow como un atributo personalizado]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute) y completando un envío de prueba.

#### Vista previa de usuario editable {#editable-user-preview}

Puedes [editar campos individuales de un usuario aleatorio o existente]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=webhook#customizing-an-existing-user) para ayudar a probar el contenido dinámico dentro de tu mensaje. Selecciona **Edit** para convertir el usuario seleccionado en un usuario personalizado que puedas modificar.

![La pestaña "Preview as a User" con un botón "Edit".]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Automatización de IA y ML {#ai-and-ml-automation}

#### BrazeAI Decisioning Studio™ Go

Ya puedes configurar tu integración con [BrazeAI Decisioning Studio™ Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/) consultando estos artículos de configuración para:

- [Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)
- [Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)
- [Salesforce Marketing Cloud]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)

#### Nuevas características para los agentes de Braze {#new-features-for-braze-agents}

{% multi_lang_include release_type.md release="Beta" %}

Ahora puedes personalizar tu [agente de Braze]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/) de las siguientes formas:

- Aplicar [directrices de marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/) para que tu agente se adhiera a ellas en su respuesta.
- Hacer referencia a un catálogo para personalizar aún más tu mensaje.
- Estructurar la salida de un agente proporcionando el [formato de salida]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format).
- Ajustar la [temperatura]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature) para el nivel de desviación de la salida de tu agente.

### Modelos ChatGPT con BrazeAI Operator<sup>TM</sup> {#chatgpt-models-with-brazeai-operatortm}

{% multi_lang_include release_type.md release="Beta" %}

Puedes seleccionar entre estos modelos de GPT para utilizarlos en diferentes tipos de solicitudes con [Operator]({{site.baseurl}}/user_guide/brazeai/operator/):

- GPT-5 nano
- GPT-5 mini (predeterminado)
- GPT-5

### Nuevas asociaciones de Braze {#new-braze-partnerships}

#### StackAdapt - Publicidad {#stackadapt-advertising}

[StackAdapt]({{site.baseurl}}/partners/stackadapt/) es una plataforma de marketing impulsada por IA que entrega publicidad orientada al rendimiento. Te permite sincronizar los datos de perfil de usuario desde Braze al Data Hub de StackAdapt. Al conectar las dos plataformas, puedes crear una visión unificada de tus clientes y activar los datos propios para mejorar el rendimiento de los anuncios.

#### Cloudinary - Contenido dinámico {#cloudinary-dynamic-content}

[Cloudinary]({{site.baseurl}}/partners/cloudinary/) es una plataforma de imagen y video que te permite gestionar, editar, optimizar y entregar imágenes y video a gran escala a cualquier campaña a través de canales y recorridos del cliente. Una vez integrada y habilitada, la gestión de medios de Cloudinary potenciará y proporcionará una entrega de activos dinámica, contextual y personalizada para tus campañas y Canvas de Braze.

#### Kameleoon - Pruebas A/B {#kameleoon-ab-testing}

[Kameleoon]({{site.baseurl}}/partners/kameleoon/) es una solución de optimización con capacidades de experimentación, personalización impulsada por IA y gestión de características en una única plataforma unificada.

### Actualizaciones del SDK {#sdk-updates}

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [React Native SDK 18.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/16.1.0/CHANGELOG.md)
    - Corrige el tipo Typescript para la devolución de llamada de `subscribeToInAppMessage` y `addListener` para `Braze.Events.IN_APP_MESSAGE_RECEIVED`.
        - Estos listeners ahora devuelven correctamente una devolución de llamada con el nuevo tipo `InAppMessageEvent`. Antes, los métodos estaban anotados para devolver un tipo `BrazeInAppMessage`, pero en realidad devolvían un `String`.
         - Si utilizas cualquiera de las dos API de suscripción, asegúrate de que el comportamiento de tus mensajes dentro de la aplicación no cambia tras actualizar a esta versión. Consulta nuestro código de muestra en `BrazeProject.tsx`.
    - Las API `logInAppMessageClicked`, `logInAppMessageImpression` y `logInAppMessageButtonClicked` ahora solo aceptan un objeto `BrazeInAppMessage` para que coincida con su interfaz pública existente.
        - Anteriormente, aceptaba tanto un objeto `BrazeInAppMessage` como un `String`.
    - `BrazeInAppMessage.toString()` ahora devuelve una cadena legible por humanos en lugar de la representación de cadena JSON.
        - Para obtener la representación en cadena JSON de un mensaje dentro de la aplicación, usa `BrazeInAppMessage.inAppMessageJsonString`.
    - En iOS, `[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]` se ha trasladado a `[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]`.
        - Este nuevo método es ahora un método de clase en lugar de un método de instancia.
    - Añade anotaciones de nulabilidad a los métodos de `BrazeReactUtils`.
    - Elimina de la API los siguientes métodos y propiedades obsoletos:
        - `getInstallTrackingId(callback:)` a favor de `getDeviceId`.
        - `registerAndroidPushToken(token:)` a favor de `registerPushToken`.
        - `setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)` a favor de `setAdTrackingEnabled`.
        - `PushNotificationEvent.push_event_type` a favor de `payload_type`.
        - `PushNotificationEvent.deeplink` a favor de `url`.
        - `PushNotificationEvent.content_text` a favor de `body`.
        - `PushNotificationEvent.raw_android_push_data` a favor de `android`.
        - `PushNotificationEvent.kvp_data` a favor de `braze_properties`.
    - Actualiza los enlaces de la versión nativa del SDK de Android [de Braze Android SDK 39.0.0 a 40.0.2](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [.NET MAUI (Xamarin) SDK versión 8.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Actualizado el enlace de iOS de [Braze Swift SDK 12.1.0 a 13.3.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Esto incluye la compatibilidad con Xcode 26.
- [Flutter SDK 16.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Actualiza el puente nativo de Android [de Braze Android SDK 39.0.0 a 40.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Braze Swift SDK 13.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK 6.3.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Android SDK 40.0.0-40.0.2](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details 14 de octubre de 2025 %}

## Lanzamiento del 14 de octubre de 2025 {#october-14-2025-release}

### BrazeAI Decisioning Studio™

[BrazeAI Decisioning Studio™](https://www.braze.com/product/brazeai-decisioning-studio/) sustituye las pruebas A/B por la toma de decisiones con IA que lo personaliza todo y maximiza cualquier métrica: impulsa los ingresos, no los clics. Con BrazeAI Decisioning Studio™, puedes optimizar cualquier KPI empresarial. Consulta nuestra sección dedicada [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/) para ver ejemplos de casos de uso y características clave.

### Flexibilidad de los datos {#data-flexibility}

#### Nuevos eventos de Currents {#new-currents-events}

Estos nuevos eventos se han añadido al [glosario de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/):

- `users.messages.rcs.Click`
- `users.messages.rcs.Rejection`
- `users.messages.line.Abort`
- `users.messages.line.Send`
- `users.messages.line.InboundReceive`
- `users.messages.line.Click`
- `users.messages.rcs.Delivery`
- `users.messages.rcs.InboundReceive`
- `users.messages.rcs.Read`
- `users.messages.rcs.Send`
- `users.messages.rcs.Abort`
- `users.messages.inappmessage.Abort`

Estos nuevos campos se añadieron a los siguientes eventos de Currents:

- `is_sms_fallback`:
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.Rejection`
- `message_id`, `in_reply_to`, `flow_id`, `flow_response_json`, `product_id`, `catalog_id`:
  - `users.messages.whatsapp.InboundReceive`
- `message_id`, `flow_id`, `template_name`:
  - `users.messages.whatsapp.Send`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.Read`

#### Listas de supresión {#suppression-lists}

{% multi_lang_include release_type.md release="General availability" %}

Las [listas de supresión]({{site.baseurl}}/user_guide/audience/suppression_lists/) son grupos de usuarios que no reciben automáticamente ninguna campaña o Canvas. Las listas de supresión se definen mediante filtros de segmento, y los usuarios entran y salen de las listas de supresión a medida que cumplen los criterios de filtrado.

#### Personalización sin copia {#zero-copy-personalization}

{% multi_lang_include release_type.md release="Early access" %}

Sincroniza los desencadenantes de Canvas utilizando la Ingesta de datos en la nube para una [personalización sin copia]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/). Esta característica accede a información específica del usuario desde tu solución de almacenamiento de datos y la pasa a un Canvas de destino. Los pasos en Canvas pueden incluir opcionalmente campos de personalización que no persisten en los perfiles de usuario de Braze.

#### Variables de contexto de Canvas para rutas de audiencia y pasos de división de decisiones {#canvas-context-variables-for-audience-paths-and-decision-split-steps}

{% multi_lang_include release_type.md release="Early access" %}

Puedes [crear filtros de variables de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/#context-variable-filters) que utilicen variables de contexto previamente declaradas en las [rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/) y en los pasos de [división de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/).

### Desbloquear la creatividad {#unlocking-creativity}

#### Tarjetas de ofertas para correos electrónicos {#deal-cards-for-emails}

Usa las [tarjetas de ofertas]({{site.baseurl}}/user_guide/channels/email/html_editor/gmail_promotions_tab/) para proporcionar información clave sobre las ofertas directamente en la parte superior de los cuerpos de los correos electrónicos. Esto permite a los destinatarios comprender rápidamente los detalles de la oferta y pasar a la acción.

#### Plantillas para Banners {#templates-for-banners}

Cuando [compongas tu Banner]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/), ahora puedes empezar con una plantilla en blanco, usar una plantilla de Braze o seleccionar una plantilla de Banner guardada.

### Canales robustos {#robust-channels}

#### Listas de supresión {#suppression-lists}

{% multi_lang_include release_type.md release="General availability" %}

Las [listas de supresión]({{site.baseurl}}/user_guide/audience/suppression_lists/) especifican grupos de usuarios que nunca recibirán mensajes. Los administradores pueden crear listas de supresión con filtros de segmento para acotar un grupo de usuarios del mismo modo que lo harías para la segmentación.

#### Seguimiento de clics en LINE {#line-click-tracking}

{% multi_lang_include release_type.md release="General availability" %}

Cuando el [seguimiento de clics de LINE]({{site.baseurl}}/line/click_tracking/) está activado, Braze acorta automáticamente tus URL, añade mecanismos de seguimiento y registra los clics en tiempo real. Mientras que LINE ofrece datos agregados de clics, Braze proporciona información granular del usuario que es oportuna y procesable. Estos datos te permiten crear estrategias de segmentación y reorientación más específicas, como segmentar a los usuarios en función de su comportamiento al hacer clic y desencadenar mensajes en respuesta a clics concretos.

#### Filtrado de clics de bots en SMS y RCS {#sms-and-rcs-bot-click-filtering}

{% multi_lang_include release_type.md release="General availability" %}

El [filtrado de clics de bots en SMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/bot_click_filtering/) mejora el análisis y los flujos de trabajo de las campañas al excluir los clics sospechosos de bots. Un "clic de bot" se refiere a los clics automatizados en enlaces acortados en mensajes SMS y RCS, como los de rastreadores web, vistas previas de enlaces de Android e iOS o software de seguridad CPaaS. Esta característica facilita la elaboración de informes precisos, la segmentación y la orquestación para captar usuarios reales.

#### Transferir números de teléfono de WhatsApp {#transfer-whatsapp-phone-numbers}

Transfiere un número de teléfono de una cuenta de WhatsApp Business (WABA) y su grupo de suscripción asociado [de un espacio de trabajo a otro]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/transfer_between_workspaces/) dentro de Braze.

#### Mensajes de respuesta y vista previa de WhatsApp Flows {#whatsapp-flows-response-messages-and-preview}

En un Canvas, puedes crear un paso de mensaje de WhatsApp que utilice un [mensaje de respuesta]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/whatsapp_flows/?tab=response%20message#configuring-whatsapp-flow-messages-and-responses) y un mensaje de flujo. También puedes seleccionar **Preview Flow** para previsualizar el Flow directamente en Braze y confirmar que se comporta como se espera.

#### Mensajes de productos de WhatsApp {#whatsapp-product-messages}

Los [mensajes de producto]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/product_messages/) te permiten enviar mensajes de WhatsApp interactivos que muestran productos directamente desde tu catálogo de Meta.

#### Integración de Braze y WhatsApp con un sistema externo {#integrating-braze-and-whatsapp-with-an-external-system}

[Aprovecha el poder de los chatbots de IA y las entregas de agentes en vivo]({{site.baseurl}}/user_guide/channels/whatsapp/use_cases/whatsapp_and_external_systems/) en el canal de WhatsApp para agilizar tus operaciones de atención al cliente. Automatizando las consultas rutinarias y pasando fácilmente a agentes humanos cuando sea necesario, puedes mejorar significativamente los tiempos de respuesta y mejorar la experiencia general del cliente.

### Automatización de IA y ML {#ai-and-ml-automation}

#### Agentes de Braze {#braze-agents}

{% multi_lang_include release_type.md release="Beta" %}

Los [agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents/) son ayudantes impulsados por IA que puedes crear dentro de Braze. Los agentes pueden generar contenido, tomar decisiones inteligentes y enriquecer tus datos para que puedas ofrecer experiencias del cliente más personalizadas.

### Nuevas asociaciones de Braze {#new-braze-partnerships}

#### Jasper - Plantillas {#jasper-templates}

La integración de [Jasper]({{site.baseurl}}/partners/jasper/) con Braze te permite agilizar la creación de contenidos y la ejecución de campañas. Con Jasper, tus equipos de marketing pueden generar textos de alta calidad y adaptados a la marca en cuestión de minutos. A continuación, Braze facilita la entrega de estos mensajes a la audiencia adecuada en el momento óptimo. Esta integración fomenta flujos de trabajo fluidos, reduce el esfuerzo manual e impulsa resultados de interacción más sólidos.

#### Swym - Fidelización y reorientación {#swym-loyalty-and-retargeting}

[Swym]({{site.baseurl}}/partners/swym/) ayuda a las marcas de comercio electrónico a captar la intención de compra con listas de deseos, guardar para más tarde, registro de regalos y alertas de existencias. Utilizando datos ricos y basados en permisos, puedes crear campañas hiperdirigidas y entregar experiencias de compra personalizadas que impulsen la interacción, aumenten las conversiones e incrementen la fidelización.

### Actualizaciones del SDK {#sdk-updates}

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; puedes encontrar el resto de actualizaciones consultando los correspondientes registros de cambios del SDK.

- [Cordova SDK 14.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Actualizado el puente nativo de Android [de Braze Android SDK 37.0.0 a 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - La GradlePluginKotlinVersion mínima requerida es ahora 2.1.0.
    - Actualizado el puente nativo de iOS [de Braze Swift SDK 12.0.0 a 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Esto incluye la compatibilidad con Xcode 26.
    - Elimina la compatibilidad con News Feed. Se han eliminado las siguientes API:
        - `launchNewsFeed`
        - `getNewsFeed`
        - `getNewsFeedUnreadCount`
        - `getNewsFeedCardCount`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
- [React Native SDK 17.0.0-17.0.1](https://www.npmjs.com/package/@braze/react-native-sdk/v/17.0.1)
    - Actualiza los enlaces de la versión nativa del SDK de Android [de Braze Android SDK 37.0.0 a 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Elimina la compatibilidad con News Feed. Se han eliminado las siguientes API:
        - `launchNewsFeed`
        - `requestFeedRefresh`
        - `getNewsFeedCards`
        - `logNewsFeedCardClicked`
        - `logNewsFeedCardImpression`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
        - `Braze.Events.NEWS_FEED_CARDS_UPDATED`
        - `Braze.CardCategory`
- [Web SDK 6.2.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 15.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Unity SDK 10.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Actualizado el puente nativo de iOS [de Braze Swift SDK 12.0.0 a 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Esto incluye la compatibilidad con Xcode 26.

{% enddetails %}
{% details 16 de septiembre de 2025 %}

## Lanzamiento del 16 de septiembre de 2025 {#september-16-2025-release}

### Flexibilidad de los datos {#data-flexibility}

#### Plataforma de datos de Braze {#braze-data-platform}

La plataforma de datos de Braze es un conjunto completo y componible de capacidades de datos e integraciones de socios que te permite crear experiencias personalizadas e impactantes a lo largo del ciclo de vida del cliente. Obtén más información sobre los tres trabajos relacionados con los datos que hay que realizar:

- [Unificación de datos]({{site.baseurl}}/user_guide/data/unification/)
- [Activación de datos]({{site.baseurl}}/user_guide/data/activation/)
- [Distribución de datos]({{site.baseurl}}/user_guide/data/distribution/)

#### Propiedades personalizadas de Banner {#custom-banner-properties}

{% multi_lang_include release_type.md release="Early access" %}

Puedes usar propiedades personalizadas de tu campaña de Banner para recuperar datos clave-valor a través del SDK y modificar el comportamiento o la apariencia de tu aplicación. Para saber más, consulta [Propiedades personalizadas de Banner]({{site.baseurl}}/developer_guide/banners/placements/#custom-properties).

#### Autenticación por token {#token-authentication}

{% multi_lang_include release_type.md release="General availability" %}

Al utilizar contenido conectado de Braze, es posible que determinadas API requieran un token en lugar de un nombre de usuario y una contraseña. Braze puede almacenar credenciales que contengan [valores de encabezado de autenticación por token]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/#using-token-authentication).

#### Códigos promocionales {#promotion-codes}

Puedes guardar códigos promocionales en el perfil de un usuario mediante un paso de actualización de usuario. Para más información, consulta [Guardar códigos promocionales en perfiles de usuario]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/#save-to-profile).

### Desbloquear la creatividad {#unlocking-creativity}

#### Braze Pilot

[Braze Pilot]({{site.baseurl}}/user_guide/get_started/braze_pilot/) es una aplicación disponible públicamente para Android e iOS que te permite lanzar mensajes desde tu dashboard de Braze a tu teléfono. Consulta [Introducción a Braze Pilot]({{site.baseurl}}/user_guide/get_started/braze_pilot/getting_started/) para ver cómo descargar la aplicación, iniciar la conexión a tu dashboard de Braze y completar la configuración.

### Nuevas asociaciones de Braze {#new-braze-partnerships}

#### Blings - Contenido visual e interactivo {#blings-visual-and-interactive-content}

[Blings]({{site.baseurl}}/partners/blings/) es una plataforma de video personalizado de nueva generación que te permite entregar experiencias de video en tiempo real, interactivas y basadas en datos a través de canales a escala.

#### Integración estándar de Shopify con herramienta de terceros {#shopify-standard-integration-with-third-party-tool}

Para las tiendas en línea de Shopify, recomendamos usar el método de integración estándar de Braze para admitir los SDK de Braze en tu sitio.

Sin embargo, entendemos que tal vez prefieras usar una herramienta de terceros, como Google Tag Manager, por lo que hemos elaborado una guía sobre cómo hacerlo. Para empezar, consulta [Shopify: etiquetado de terceros]({{site.baseurl}}/shopify_standard_integration_third_party_tagging/).

### Actualizaciones del SDK {#sdk-updates}

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [Braze Flutter SDK 15.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/main/CHANGELOG.md#1500)
    - Actualiza el puente nativo de Android de Braze Android SDK `36.0.0` a `39.0.0`.
    - Actualiza el puente nativo de iOS de Braze Swift SDK `12.0.0` a `13.2.0`. Esto incluye la compatibilidad con Xcode 26.

- [Braze Swift SDK 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1300)
  - Actualiza los enlaces del SDK Swift de Braze para que requieran versiones de la denominación `13.0.0+` SemVer. Esto permite la compatibilidad con cualquier versión del SDK de Braze desde `13.0.0` hasta, pero sin incluir, `14.0.0`.

{% enddetails %}
{% details 19 de agosto de 2025 %}

## Lanzamiento del 19 de agosto de 2025 {#august-19-2025-release}

### Normalización de la coherencia horaria con el contexto de Canvas {#time-zone-consistency-standardization-to-canvas-context}

{% multi_lang_include release_type.md release="Early access" %}

Si participas en el [acceso anticipado al paso de contexto de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/), todas las marcas de tiempo con un tipo de fecha/hora de las propiedades del evento desencadenante en los Canvas basados en acciones se normalizarán siempre a [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). Para saber más sobre esto, consulta [Normalización de la coherencia horaria]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/#time-zone-consistency-standardization).

### Flexibilidad de los datos {#data-flexibility}

#### Dominios personalizados en autogestión {#self-serve-custom-domains}

{% multi_lang_include release_type.md release="General access" %}

Los [dominios personalizados en autogestión]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains/) te permiten configurar y gestionar tus propios dominios personalizados para SMS, RCS y WhatsApp, directamente desde tu dashboard de Braze. Puedes añadir, supervisar y gestionar fácilmente hasta 10 dominios personalizados en un solo lugar.

#### Estadísticas del embudo del segmento {#segment-funnel-statistics}

Selecciona [Ver estadísticas del embudo]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#viewing-funnel-statistics) para mostrar las estadísticas de ese grupo de filtros y ver cómo afecta cada filtro añadido a tus estadísticas de segmento. Verás un recuento estimado y el porcentaje de usuarios a los que se dirigen todos los filtros hasta ese momento. Una vez mostradas las estadísticas de un grupo de filtros, se actualizarán automáticamente cada vez que cambies los filtros.

#### Nuevos campos de respuesta para el endpoint `/campaigns/details` para notificaciones push {#new-response-fields-for-campaignsdetails-endpoint-for-push-notifications}

La respuesta `messages` para notificaciones push incluye ahora dos nuevos campos:

- `image_url`: Una URL de imagen para una imagen de notificación de Android, una imagen de notificación de iOS o una imagen de icono push web.
- `large_image_url`: Una URL de imagen de notificación web para las acciones push web de Android Chrome y Windows.

#### Definición de los campos PII {#defining-pii-fields}

Seleccionar y [definir determinados campos como campos PII]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#view-pii) solo afecta a lo que los usuarios pueden ver en el dashboard de Braze y no afecta a cómo se gestionan los datos del usuario final en dichos campos PII.

Consulta a tu equipo jurídico para alinear la configuración de tu dashboard con las normativas y políticas de privacidad aplicables a tu empresa, incluidas las relacionadas con la [retención de datos]({{site.baseurl}}/api/data_retention/).

#### Compartir un enlace de descarga del Generador de informes {#sharing-a-report-builder-download-link}

Puedes [compartir un enlace del dashboard]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report) al informe seleccionando **Share** y luego **Share a link** o **Send or schedule an email**.

### Desbloquear la creatividad {#unlocking-creativity}

#### Etiquetas de encabezado personalizadas para correos electrónicos de arrastrar y soltar {#custom-head-tags-for-drag-and-drop-emails}

Usa las etiquetas `<head>` para añadir CSS y metadatos en tu mensaje de correo electrónico. Por ejemplo, puedes usar estas etiquetas para añadir una hoja de estilos o un favicon. Liquid es compatible con las etiquetas `<head>`.

### Canales robustos {#robust-channels}

#### Mejores prácticas de exclusión difusa {#fuzzy-out-out-best-practices}

Hemos añadido una [sección de mejores prácticas]({{site.baseurl}}) para ayudarte a configurar cuidadosamente tu mensaje de exclusión difusa y crear una experiencia clara, conforme y positiva para tus suscriptores.

#### WhatsApp Flows

{% multi_lang_include release_type.md release="Early access" %}

[WhatsApp Flows]({{site.baseurl}}/whatsapp_flows/) es una mejora del canal de WhatsApp existente, que te permite crear experiencias de mensajería interactivas y dinámicas.

#### Preguntas sobre productos entrantes de WhatsApp {#whatsapp-inbound-product-questions}

Los usuarios pueden responder a tu mensaje de producto o catálogo con [preguntas sobre el producto]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/product_messages/#receiving-inbound-product-questions). Estas llegan como mensajes entrantes, que pueden clasificarse con una ruta de acción.

Además, Braze extrae el ID de producto y el ID de catálogo de estas preguntas, por lo que si deseas automatizar las respuestas o enviar preguntas a otro equipo (como el de atención al cliente), puedes incluir esos datos.

### Automatización de IA y ML {#ai-and-ml-automation}

#### Nuevos artículos sobre casos de uso de BrazeAI<sup>TM</sup> {#new-brazeai-use-case-articles}

Hemos añadido nuevos artículos sobre casos de uso para ayudarte a sacar el máximo partido de BrazeAI<sup>TM</sup>. Estas guías destacan formas prácticas de aplicar la IA a tus estrategias de interacción, entre ellas:

- [Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/use_case/): Identifica a los clientes en riesgo de abandono y actúa con prontitud.
- [Predictive Events]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/use_case/): Anticipa las acciones clave de los usuarios y da forma a las experiencias en tiempo real.
- [Recomendaciones]({{site.baseurl}}/user_guide/brazeai/recommendations/use_case /): Entrega contenidos y productos más relevantes en función del comportamiento del cliente.

#### Servidor MCP {#mcp-server}

{% multi_lang_include release_type.md release="Beta" %}

El [servidor Braze MCP]({{site.baseurl}}/user_guide/brazeai/mcp_server/), una conexión segura y de solo lectura, permite a herramientas de IA como Claude y Cursor acceder a datos de Braze no PII para responder preguntas, analizar tendencias y proporcionar información sin alterar los datos.

### Actualizaciones del SDK {#sdk-updates}

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [Swift SDK 13.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Amplía la funcionalidad de `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` para que se desencadene en caso de errores de autenticación "Opcional".
        - El método delegado `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` se desencadenará ahora para los errores de autenticación "Obligatorio" y "Opcional".
        - Si solo quieres gestionar errores de autenticación SDK "requeridos", añade una comprobación que asegure que `BrazeSDKAuthError.optional` es falso dentro de tu implementación de este método delegado.
    - Corrige el uso de `Braze.Configuration.sdkAuthentication` para que surta efecto cuando esté habilitado.
        - Antes, el SDK no consumía el valor de esta configuración y el token siempre se adjuntaba a las solicitudes si estaba presente.
        - Ahora, el SDK solo adjuntará el token de autenticación SDK a las solicitudes de red salientes cuando esta configuración esté habilitada.
    - Los definidores de todas las propiedades de `Braze.FeatureFlag` y de todas las propiedades de `Braze.Banner` se han convertido en `private`. Las propiedades de estas clases son ahora de solo lectura.
    - Elimina la propiedad `Braze.Banner.id`, que quedó obsoleta en la versión `11.4.0`.
        - En su lugar, usa `Braze.Banner.trackingId` para leer el ID de seguimiento de campaña de un banner.
- [React Native SDK 16.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Actualiza los enlaces de la versión nativa del SDK de Android de [Braze Android SDK 36.0.0 a 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualiza los enlaces de la versión nativa del SDK Swift de [Braze Swift SDK 12.0.0 a 13.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - El evento `sdkAuthenticationError` se desencadenará ahora para los errores de autenticación "Obligatorio" y "Opcional".
- [Xamarin SDK 7.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/7.0.0/CHANGELOG.md)
    - Se ha añadido compatibilidad con .NET 9.0 para los enlaces de iOS y Android.
        - Esto elimina la compatibilidad con .NET 8.0.
        - Esto requiere una [versión mínima de iOS 12.2](https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0).
    - Actualizado el enlace de Android de [Braze Android 32.0.0 a 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualizado el enlace de iOS de [Braze Swift SDK 10.0.0 a 12.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...12.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Esta versión contiene API para la característica Banners, pero actualmente no es totalmente compatible con este SDK. Si deseas usar Banners en tu aplicación .NET MAUI, ponte en contacto con tu administrador de atención al cliente antes de integrarlos en tu aplicación.
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Se ha actualizado la implementación interna de iOS del método `enableSdk` para usar `setEnabled`: en lugar de `_requestEnableSDKOnNextAppRun`, que estaba obsoleto en el SDK Swift.
    - Llamar a este método ya no requiere relanzar la aplicación para que surta efecto. El SDK quedará habilitado en cuanto se ejecute este método.
    - Actualizado el puente nativo de Android de [Braze Android SDK `36.0.0` a `37.0.0`](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).

{% enddetails %}