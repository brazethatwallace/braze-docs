---
page_order: 10
nav_title: Términos que debes conocer
article_title: Términos de Braze que debes conocer

layout: glossary_page
glossary_top_header: "Términos que debes conocer"
glossary_top_text: "Estos términos te ayudarán a iniciar tu camino hacia una mejor relación con tus clientes y usuarios gracias a Braze. Lee esto antes de comenzar tu incorporación."
page_type: glossary
description: "Este glosario incluye términos importantes que debes conocer durante el proceso de incorporación a Braze."

glossaries:
  - name: Active user
    description: "Para la segmentación de Campaigns, Braze define un <a href=\"/docs/user_guide/messaging/campaigns/ideas_and_strategies/active_user_campaigns\">usuario activo</a> en un periodo determinado como cualquier persona que tenga una sesión en ese periodo (los usuarios actualizados a través de la API también cuentan para ese periodo). Para el <a href=\"/docs/user_archival#active-users\">archivado de usuarios</a> y las estadísticas de alcance, Braze utiliza una definición más amplia que también incluye actualizaciones de perfil, mensajes enviados al usuario e interacciones con mensajes."
  - name: Alloys
    description: "Alloys son nuestros <a href=\"/docs/partners/home\">partners tecnológicos</a>."
  - name: Anonymous users
    description: "Cuando se reconoce un perfil de usuario a través del SDK or kit de desarrollo de software, se crea un perfil de usuario anónimo con el <a href=\"/docs/api/basics#user-ids\">ID de usuario de Braze</a> asociado."
  - name: API campaigns
    description: "Las <a href=\"/docs/api/api_campaigns\">Campaigns de API</a> utilizan el panel de Braze para generar un <code>campaign_id</code> (e ID de variante) mientras tú proporcionas el texto, la audiencia, la planificación y los activos a través de las <a href=\"/docs/api/endpoints/messaging\">API de mensajería</a>. Se diferencian de las <a href=\"/docs/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery\">Campaigns activadas por API</a>, en las que desencadenas una Campaign completamente configurada desde el panel a través de la API."
  - name: Application program interface (API)
    description: "La <a href=\"/docs/api/basics\">API de Braze</a> proporciona un servicio web que permite registrar las acciones realizadas por los usuarios directamente a través de HTTP, en lugar de a través de los SDK or kit de desarrollo de software para móviles. Esto te permite, por ejemplo, pasar datos de usuario a Braze que no se rastrean dentro de tu aplicación o sitio web."
  - name: App instance
    description: Las instancias de la aplicación se refieren a los diferentes sitios y aplicaciones que se reúnen en un espacio de trabajo.
  - name: Braze (the product)
    description: "A veces denominado panel, este producto controla todos los datos e interacciones que constituyen el núcleo de la plataforma Braze. Los clientes de Braze lo utilizan para gestionar notificaciones, configurar Campaigns de mensajería específicas y consultar análisis. Los desarrolladores lo utilizan para gestionar los ajustes de integración de las aplicaciones, como las claves de API y las credenciales de las notificaciones push."
  - name: Team
    description: "Los administradores de Braze pueden dividir un subconjunto de usuarios del panel en <a href=\"/docs/user_guide/administer/global/user_management/teams\">equipos</a> con distintos roles y permisos de usuario. Esto permite a los administradores de Braze limitar el acceso a determinadas características por pertenencia a un grupo."
  - name: Campaign
    description: "Las Campaigns son métodos de mensajería personalizables para entregar una respuesta personalizada a tus clientes. Puedes <a href=\"/docs/user_guide/messaging/campaigns\">crear Campaigns</a> utilizando diferentes canales de mensajería para enviar tus mensajes exclusivos."
  - name: Canvas
    description: "<a href=\"/docs/user_guide/messaging/Canvas\">Canvas</a> es una única interfaz unificada en la que los especialistas en marketing pueden configurar Campaigns con múltiples mensajes y pasos para formar un recorrido cohesivo. Canvas te permite comparar y optimizar esas experiencias utilizando análisis exhaustivos para la experiencia completa del usuario."
  - name: Connected Content
    description: "<a href=\"/docs/user_guide/messaging/design_and_edit/personalize/connected_content\">Connected Content</a> amplía la personalización del marketing para impulsar la interacción con los clientes y las conversiones. Puedes insertar cualquier información accesible mediante API directamente en los mensajes que envíes a los usuarios. Connected Content permite extraer contenidos directamente de tu servidor web o de API de acceso público."
  - name: Content Cards
    description: "<a href=\"/docs/user_guide/channels/content_cards\">Content Cards</a> te permiten enviar a tus clientes un flujo dinámico y muy específico de contenido enriquecido directamente desde las aplicaciones que más les gustan, sin interrumpir su experiencia. Las Content Cards pueden enviarse a usuarios de iOS, Android y web."
  - name: Conversion event
    description: "Un <a href=\"/docs/user_guide/messaging/messaging_fundamentals/conversion_events\">evento de conversión</a> es una métrica de éxito que registra si un destinatario realizó una acción de alto valor dentro de una ventana de conversión después de recibir tu mensaje (o después de entrar en un Canvas o grupo de control, según el canal y la configuración). Utiliza los eventos de conversión para medir el rendimiento de Campaigns y Canvas más allá de los envíos."
  - name: Currents
    description: "<a href=\"/docs/user_guide/data/distribution/braze_currents\">Currents</a>, nuestra exportación de transmisión de datos, está incluida en algunos paquetes de Braze. Braze Currents te permite integrarte a través del almacenamiento de datos mediante archivos planos o con nuestros partners de análisis del comportamiento y datos de clientes mediante cargas útiles JSON por lotes a un endpoint designado."
  - name: Custom attributes
    description: "Los <a href=\"/docs/user_guide/data/activation/attributes/custom_attributes\">atributos personalizados</a> son una colección de rasgos únicos de tus usuarios. Son ideales para almacenar atributos sobre los usuarios o información sobre acciones de poco valor dentro de tu aplicación. Puedes asignar atributos personalizados a los usuarios dentro del panel. Puedes filtrar y segmentar a tus usuarios en función de estos atributos tanto para Campaigns en <a href=\"/docs/developer_guide/analytics/setting_user_attributes?sdktab=swift\">Swift</a> como en <a href=\"/docs/developer_guide/analytics/setting_user_attributes?sdktab=android\">Android</a>."
  - name: Custom events
    description: "Los <a href=\"/docs/user_guide/data/activation/events/custom_events\">eventos personalizados</a> son acciones que realizan tus usuarios; son los más adecuados para hacer un seguimiento de las interacciones de alto valor de los usuarios con tu aplicación."
  - name: Data point
    description: "Se cuenta un punto de datos cuando se establece o actualiza un <a href=\"/docs/user_guide/data/activation/attributes/custom_attributes\">atributo personalizado</a> (aunque lo estés actualizando con el mismo valor), se registra un <a href=\"/docs/user_guide/data/activation/events/custom_events\">evento personalizado</a> o de compra, se registra cualquier dato estándar (por ejemplo, <code>email</code>, <code>first_name</code>, <code>last_name</code>, <code>country</code> o <code>home_city</code>), cuando se inicia una sesión y cuando finaliza."
  - name: Deep linking
    description: "Los <a href=\"/docs/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls\">vínculos profundos</a> se utilizan para dirigir a los clientes a su siguiente acción o interacción. Mediante los vínculos profundos, puedes conectar un mensaje con un contenido específico dentro de un sitio web o una aplicación móvil."
  - name: Dormant users
    description: "Se considera que un usuario está <a href=\"/docs/user_archival#dormant-users\">inactivo de forma prolongada</a> cuando no ha tenido ninguna actividad cualificada en los últimos doce meses: no ha utilizado ninguna aplicación ni sitio web en el espacio de trabajo, no ha recibido ningún mensaje del espacio de trabajo y no ha sido actualizado en más de doce meses. De forma predeterminada, Braze utiliza una ventana de doce meses para el archivado por inactividad prolongada; la configuración de tu empresa puede modificar el número de días."
  - name: Endpoint
    description: "En la API de mensajería de Braze se utiliza un extremo de un canal de comunicación, también conocido como <a href=\"/docs/api/endpoints\">endpoint</a> de API, para enviar y programar mensajes."
  - name: Exception event
    description: "En Canvas, los <a href=\"/docs/user_guide/messaging/Canvas/create_a_canvas/exit_criteria#exception-events\">eventos de excepción</a> son acciones específicas que eliminan a un usuario del recorrido cuando se producen (por ejemplo, realizar un pedido). Mantienen los mensajes de seguimiento relevantes después de que el usuario complete tu objetivo. Consulta <a href=\"/docs/user_guide/messaging/Canvas/create_a_canvas/exit_criteria\">Criterios de salida</a> para saber cómo se evalúan y programan las salidas."
  - name: External ID
    description: "El <code>external_id</code> es el identificador principal de usuario en un perfil de usuario de Braze. Vincula a la misma persona a través de canales y dispositivos cuando asignas ID de tus propios sistemas. Los perfiles anónimos pueden no tener un <code>external_id</code> hasta que identifiques al usuario. Para más información, consulta <a href=\"/docs/user_guide/get_started/users_and_segments\">Usuarios y segmentos</a> y <a href=\"/docs/api/basics#user-ids\">ID de usuario</a>."
  - name: Frequency capping
    description: "La <a href=\"/docs/user_guide/messaging/messaging_fundamentals/frequency_capping\">limitación de frecuencia</a> te permite gestionar la comunicación sin abrumar a tu audiencia. Es un límite automatizado de mensajes para evitar que los usuarios reciban demasiadas comunicaciones en poco tiempo."
  - name: HIPAA
    description: "HIPAA es el acrónimo de Health Insurance Portability and Accountability Act (Ley de Portabilidad y Responsabilidad de los Seguros Sanitarios). Braze <a href=\"/docs/developer_guide/disclosures/security_qualifications#hipaa\">cumple la HIPAA</a>. Los requisitos de la HIPAA implican seguridad administrativa, física y técnica."
  - name: In-app message
    description: "Los <a href=\"/docs/user_guide/channels/in_app_messages\">mensajes dentro de la aplicación</a> son mensajes de móvil que aparecen dentro de tu aplicación. Te ayudan a hacer llegar el contenido a tu usuario sin interrumpir su día con una notificación push. Los mensajes personalizados y adaptados dentro de la aplicación mejoran la experiencia del usuario y ayudan a tu audiencia a obtener el máximo valor de tu aplicación."
  - name: Inactive users
    description: "Se considera que un usuario está <a href=\"/docs/user_archival#inactive-users\">inactivo</a> cuando no es alcanzable a través de los principales canales de mensajería (por ejemplo, correo electrónico, servicio de mensajes cortos, push, WhatsApp y LINE según tu configuración), no ha utilizado ninguna aplicación ni sitio web en el espacio de trabajo en más de seis meses, no ha recibido ningún mensaje del espacio de trabajo en más de seis meses y no ha sido actualizado en más de seis meses. Los usuarios inactivos son candidatos al archivado junto con los usuarios sin actividad prolongada. De forma predeterminada, Braze utiliza una ventana de seis meses para el archivado por inactividad; la configuración de tu empresa puede modificar el número de días."
  - name: IP warming
    description: "El <a href=\"/docs/user_guide/channels/email/email_setup/ip_warming\">calentamiento de IP</a> es la práctica de aumentar gradualmente la cantidad de correo enviado desde una IP dedicada. Esto ayuda a establecer una reputación con los proveedores de servicios de Internet, minimizando la probabilidad de que tus mensajes sean marcados."
  - name: Key-value pairs
    description: "Los <a href=\"/docs/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs\">pares clave-valor</a> son elementos de datos enlazados en los que la clave es un identificador único y el valor es el contenido. Pueden utilizarse para enviar cargas útiles de datos adicionales a los dispositivos de los usuarios."
  - name: Liquid
    description: "Liquid es un lenguaje de plantillas para clientes de uso común creado por Shopify y escrito en Ruby. <a href=\"/docs/user_guide/messaging/design_and_edit/personalize/liquid\">Liquid</a> se utiliza para cargar y extraer contenido dinámico. Liquid te permite utilizar objetos, etiquetas y filtros para <a href=\"/docs/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags\">añadir personalización</a>."
  - name: Messaging channel
    description: "Los <a href=\"/docs/user_guide/channels\">canales de mensajería</a> son formas de comunicarte virtualmente con tus clientes: a través de notificaciones push en su teléfono o navegador web, correo electrónico, mensajes dentro de la aplicación, ¡y mucho más!"
  - name: Monthly active user (MAU)
    description: Se trata de usuarios que han tenido una sesión en los últimos 30 días.
  - name: Multichannel messaging
    description: "Envío de mensajes a un usuario a través de varios medios, como una combinación de correo electrónico, notificaciones push web y notificaciones push para móviles. Los <a href=\"/docs/developer_guide/getting_started/platform_overview#multichannel-messaging\">canales de mensajería</a> se utilizan mejor en conjunto y con regularidad para volver a captar a los usuarios perdidos, retener a los usuarios activos y dinamizar a los embajadores de tu marca."
  - name: Multivariate testing
    description: "Las <a href=\"/docs/user_guide/messaging/ab_testing\">pruebas A/B</a> comparan un conjunto más pequeño de versiones de mensajes; las <a href=\"/docs/user_guide/messaging/ab_testing/create_tests\">pruebas multivariantes</a> comparan múltiples variables a la vez para ver qué combinación funciona mejor. Puedes configurar ambas desde el panel para los tipos de Campaign compatibles."
  - name: New user
    description: Braze considera nuevo usuario a todo aquel que acaba de instalar tu aplicación. Alternativamente, un nuevo usuario también puede definirse como un usuario con un ID de usuario que no ha sido previamente identificado dentro de Braze.
  - name: Personalization
    description: "Utilizar la tecnología para tener en cuenta las preferencias y tendencias individuales de cada usuario a la hora de comunicarse con él. Los <a href=\"/docs/user_guide/messaging/design_and_edit/personalize\">mensajes personalizados</a> ayudan a crear experiencias valiosas para los clientes adaptándose a sus preferencias."
  - name: Push message
    description: "Un <a href=\"/docs/user_guide/channels/push\">mensaje push</a>, o notificación push, es una notificación que aparece desde una aplicación móvil. Las notificaciones push suelen aparecer como cuadros de diálogo emergentes y banners tanto para iOS como para Android."
  - name: Push token
    description: "Un token de notificaciones push es una clave única, creada y asignada por Apple o Google para crear una conexión entre una aplicación y un dispositivo iOS, Android o web. La <a href=\"/docs/api/objects_filters/user_attributes_object#migrate-push-tokens\">migración de tokens push</a> consiste en importar a Braze esas claves ya generadas."
  - name: Push time to live (TTL)
    description: "También conocido como <a href=\"/docs/user_guide/administer/global/workspace_settings/push_settings\">TTL or tiempo de vida para notificación push</a>, el TTL or tiempo de vida or tiempo de vida se refiere al periodo durante el cual las Campaigns seguirán intentando ser entregadas a un usuario desconectado."
  - name: Race condition
    description: "Una <a href=\"/docs/user_guide/messaging/ab_testing/concepts/race_conditions\">condición de carrera</a> es un concepto de ingeniería de software que describe una situación no deseada que se produce cuando un sistema intenta realizar varias operaciones simultáneamente, pero, debido a la naturaleza del sistema, las operaciones deben realizarse en la secuencia correcta para ejecutarse correctamente. <br><br>En la plataforma Braze, la segmentación de una Campaign desencadenada en función de los datos de usuario registrados en el momento del evento puede provocar una condición de carrera. Esto ocurre cuando un cambio en el atributo del usuario sobre el que se segmenta la Campaign aún no se ha procesado para el usuario en el momento en que se determina la pertenencia al segmento y se envía la Campaign, y puede provocar que el usuario no reciba la Campaign."
  - name: Rate limiting
    description: "La <a href=\"/docs/user_guide/messaging/messaging_fundamentals/frequency_capping\">limitación de velocidad</a> controla la rapidez con la que los mensajes salen de Braze (por ejemplo, velocidad de entrega por minuto o límites centrados en el usuario mediante filtros de segmento). Funciona junto con la limitación de frecuencia en la misma página, que limita cuántos mensajes recibe un usuario en una ventana de tiempo."
  - name: Segmentation
    description: "La <a href=\"/docs/user_guide/audience/segments\">segmentación</a> del panel te permite crear grupos o extensiones de usuarios basándote en potentes filtros de su comportamiento dentro de la aplicación, datos demográficos y mucho más."
  - name: Software development kit (SDK)
    description: "Los <a href=\"/docs/developer_guide/getting_started/sdk_overview\">SDK or kit de desarrollo de software</a> se integran en tus aplicaciones móviles, sitios web y experiencias conectadas, y proporcionan herramientas de marketing, mensajería y análisis. Braze publica guías de integración de SDK or kit de desarrollo de software para plataformas como <a href=\"/docs/developer_guide/sdk_integration?sdktab=swift\">Swift</a> y <a href=\"/docs/developer_guide/sdk_integration?sdktab=android\">Android</a>; para Web y otras plataformas, sigue las rutas de integración enlazadas desde el resumen del SDK or kit de desarrollo de software."
  - name: Subscription groups
    description: "Los <a href=\"/docs/user_guide/audience/subscription_preferences/subscription_groups\">grupos de suscripción</a> se superponen a los estados de suscripción globales para que puedas ofrecer opciones de adhesión voluntaria granulares (por ejemplo, boletines frente a promociones). Existen patrones similares para canales como servicio de mensajes cortos y WhatsApp; siempre dirige a un grupo de suscripción cuando tu canal lo requiera."
  - name: Sunsetting
    description: "La extinción se refiere al proceso de identificar a los usuarios desvinculados y cesar la mensajería activa a estos usuarios sin que tengan que realizar ninguna acción. La creación de políticas de extinción para tus mensajes de <a href=\"/docs/user_guide/channels/email/best_practices/sunset_policies\">correo electrónico</a> y <a href=\"/docs/user_guide/channels/push/best_practices#implement-a-sunset-policy-for-unresponsive-users\">push</a> puede ayudar a frenar el impacto en tus tasas de apertura."
  - name: Tag
    description: "Las <a href=\"/docs/user_guide/administer/global/workspace_settings/tags\">etiquetas</a> son una herramienta que te ayuda a categorizar, organizar y clasificar tu interacción en una o varias Campaigns."
  - name: User alias
    description: "Los <a href=\"/docs/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users#assigning-user-aliases\">alias de usuario</a> son identificadores alternativos que puedes asignar a perfiles anónimos antes de que exista un <code>external_id</code>, para que puedas hacer referencia a la misma persona a través de dispositivos o canales hasta que inicie sesión."
  - name: User archival
    description: "El <a href=\"/docs/user_archival\">archivado de usuarios</a> se refiere a los usuarios que han sido archivados. En Braze, esto incluye tanto a los usuarios inactivos como a los usuarios sin actividad prolongada. El archivado evalúa las reglas de inactividad en los servicios de Braze (consulta Archivado de usuarios para la programación, la elegibilidad del espacio de trabajo, como los umbrales de recuento de usuarios, y cómo personalizar las ventanas con la configuración de la empresa o Canvas)."
  - name: User profile
    description: "Un <a href=\"/docs/user_guide/audience/manage_audience/user_profiles\">perfil de usuario</a> es el registro central de cada persona en Braze, que incluye identificadores, atributos, eventos, compras, dispositivos, historial de interacción e historial de mensajes. Los perfiles potencian la segmentación, la personalización y los flujos de trabajo de cumplimiento en todos los canales."
  - name: Webhook
    description: "Los <a href=\"/docs/user_guide/channels/webhooks\">webhooks</a> te permiten desencadenar acciones ajenas a la aplicación, como el envío de mensajes de texto servicio de mensajes cortos. Puedes utilizar webhooks para proporcionar a otros sistemas y aplicaciones información en tiempo real. La flexibilidad de esta característica te permite enviar información a cualquier endpoint."
  - name: Workspace
    description: "Un <a href=\"/docs/user_guide/get_started/workspaces\">espacio de trabajo</a> es el contenedor donde Braze almacena datos y donde tu equipo crea Campaigns, Canvas y Segments. Cada espacio de trabajo contiene una o más <a href=\"/docs/user_guide/get_started/workspaces#understanding-workspaces\">instancias de la aplicación</a> (las aplicaciones y sitios individuales que envían datos a ese espacio de trabajo)."

---