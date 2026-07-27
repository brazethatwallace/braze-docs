---
page_order: 3
nav_title: Filtros de segmentación
article_title: Filtros de segmentación
layout: glossary_page
glossary_top_header: "Filtros de segmentación"
glossary_top_text: "El SDK de Braze te proporciona un potente arsenal de filtros para segmentar y dirigirte a tus usuarios en función de características y atributos específicos. Puedes buscar o acotar estos filtros por categoría de filtro.<br><br>Para conocer los diferentes tipos de datos de atributos personalizados que puedes utilizar para segmentar usuarios, consulta <a href=\"/docs/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types\">Tipos de datos de atributos personalizados</a>. Ten en cuenta que los filtros de intervalo están limitados a 100 años."

page_type: glossary
tool: Segments
description: "Este glosario enumera los filtros disponibles para segmentar y dirigirte a tus usuarios."
search_rank: 2
glossary_tag_name: Categoría de filtro
glossary_filter_text: "Selecciona una categoría para acotar el glosario:"

glossary_tags:
  - name: Segment or CSV membership
  - name: Custom attribute
  - name: Custom events
  - name: Sessions
  - name: Retargeting
  - name: Channel subscription behavior
  - name: Purchase behavior
  - name: eCommerce
  - name: Demographic attributes
  - name: App
  - name: Uninstall
  - name: Devices
  - name: Location
  - name: Cohort membership
  - name: Install attribution
  - name: Intelligence and predictive
  - name: Social activity
  - name: Other Filters
  - name: Advertising use cases
  - name: User Attributes

glossaries:
  - name: Segment Membership
    description: Te permite filtrar en función de la pertenencia a un segmento en cualquier lugar donde se utilicen filtros (como segmentos, campañas y otros) y dirigirte a múltiples segmentos diferentes dentro de una sola campaña. <br><br>Para capturar la pertenencia a un segmento en un momento específico, exporta los usuarios del segmento en el panel o llama al <a href="/docs/api/endpoints/export/user_data/post_users_segment/">endpoint <code>/users/export/segment</code></a> antes de enviar una campaña o Canvas. Braze no almacena el historial de segmentación por usuario, por lo que no puedes comprobar retroactivamente si un usuario estaba en un segmento en un momento pasado. Para más información, consulta <a href="/docs/user_guide/data/distribution/export_braze_data/segment_data_to_csv/">Exportar datos de segmento a CSV</a>.<br><br>Ten en cuenta que los segmentos que ya utilizan este filtro no pueden incluirse ni anidarse dentro de otros segmentos, ya que esto podría crear un ciclo en el que el segmento A incluye al segmento B, que a su vez intenta incluir al segmento A de nuevo. Si eso ocurriera, el segmento seguiría referenciándose a sí mismo, haciendo imposible calcular quién pertenece realmente a él. Además, anidar segmentos de esta forma añade complejidad y puede ralentizar las cosas. En su lugar, recrea el segmento que intentas incluir utilizando los mismos filtros.<br><br>Si un segmento no aparece en el desplegable del filtro **Segment Membership**, recréalo con los mismos filtros y selecciona el nuevo segmento, o confirma que no depende ya de esta audiencia de una forma que crearía un ciclo.
    tags:
      - Segment or CSV membership
  - name: Braze Segment Extensions
    description: Después de crear una extensión de segmento en el panel de Braze, puedes elegir incluir o excluir esas extensiones en tu segmento.
    tags:
      - Segment or CSV membership
  - name: Updated/Imported from CSV
    description: Segmenta a tus usuarios en función de si formaron parte de una carga CSV o no.
    tags:
      - Segment or CSV membership
  - name: Custom Attributes
    description: Determina si un usuario coincide o no con un valor de atributo personalizado registrado. <br><br>Zona horaria:<br>Zona horaria de la empresa
    tags:
      - Custom attribute
  - name: Created At
    description: Segmenta a los usuarios por la fecha en que se creó su perfil de usuario. Si un usuario fue añadido mediante CSV o API, este filtro refleja la fecha en que fue añadido. Si el usuario no fue añadido mediante CSV o API y su primera sesión fue registrada por el SDK, este filtro refleja la fecha de esa primera sesión.
    tags:
      - Other Filters
  - name: Created From
    description: "Segmenta a los usuarios por el origen de creación de su perfil de usuario.<br><br>Se admiten los siguientes valores:<br>- SDK (<code>sdk</code>): perfil de usuario creado a través del SDK de Braze.<br>- REST API (<code>rest</code>): perfil de usuario creado a través de la REST API de Braze.<br>- Importación de token de push (<code>pti</code>): perfil de usuario creado mediante la importación de tokens de push.<br>- CSV (<code>csv</code>): perfil de usuario creado mediante importación CSV.<br>- Demo (<code>demo</code>): perfil de usuario creado con datos de demostración.<br>- SMS (<code>sms</code>): perfil de usuario creado a través de SMS.<br>- Shopify (<code>shopify</code>): perfil de usuario creado a través de Shopify.<br>- WhatsApp (<code>whats_app</code>): perfil de usuario creado a través de WhatsApp.<br>- Evento de proveedor (<code>provider_event</code>): perfil de usuario creado a través de un evento de proveedor.<br>- Sincronización de proveedor (<code>provider_sync</code>): perfil de usuario creado a través de una sincronización de proveedor.<br>- Página de destino (<code>landing_page</code>): perfil de usuario creado a través de una página de destino."
    tags:
      - Other Filters
  - name: Nested Custom Attributes
    description: Atributos que son propiedades de atributos personalizados.<br><br>Al filtrar un atributo personalizado anidado de tipo tiempo, puedes elegir filtrar en función de "Día del año" o "Hora". "Día del año" compara solo el mes y el día. "Hora" compara la marca de tiempo completa, incluido el año. La misma lógica se aplica al filtrar variables de contexto en las rutas de audiencia de Canvas; consulta <a href="/docs/user_guide/messaging/design_and_edit/personalize/sources/context_variables/#day-of-year-and-time-filters-for-date-context-variables">Filtros de día del año y hora para variables de contexto de fecha</a> para más detalles.
    tags:
      - Custom attribute
  - name: Day of Recurring Event
    description: Este filtro examina el mes y el día de un atributo personalizado con el tipo de datos "fecha", pero no examina el año. Este filtro es útil para eventos anuales.<br><br>Zona horaria&#58;<br>Este filtro se ajusta a la zona horaria del usuario, siempre que el mensaje se envíe utilizando la opción de programación en hora local; de lo contrario, este filtro utiliza la zona horaria de tu empresa.
    tags:
      - Custom attribute
  - name: Custom Event
    description: Determina si un usuario ha realizado o no un evento registrado especialmente.<br><br> Ejemplo:<br>Actividad completada con la propiedad activity_name.<br><br>Zona horaria:<br>UTC - Día natural = 1 día natural examina de 24 a 48 horas del historial del usuario
    tags:
      - Custom events
  - name: First Did Custom Event
    description: Determina la primera vez que un usuario realizó un evento registrado especialmente. (período de 24 horas) <br><br>Ejemplo:<br> Primer carrito abandonado hace menos de 1 día<br><br>Zona horaria:<br>Zona horaria de la empresa
    tags:
      - Custom events
  - name: Last Did Custom Event
    description: Determina la última vez que un usuario realizó un evento registrado especialmente. Este filtro admite decimales, como 0,25 horas. (período de 24 horas) <br><br>Ejemplo:<br> Último carrito abandonado hace menos de 1 día<br><br>Zona horaria:<br>Zona horaria de la empresa
    tags:
      - Custom events
  - name: X Custom Event In Y Days
    description: Determina si un usuario ha realizado o no un evento registrado especialmente entre 0 y 50 veces en el último número especificado de días naturales entre 1 y 30. (Día natural = 1 día natural examina de 24 a 48 horas del historial del usuario)<br> <a href="/docs/x-in-y-behavior">Más información sobre el comportamiento X en Y aquí.</a> <br><br>Ejemplo:<br>Carrito abandonado exactamente 0 veces en el último 1 día natural<br><br>Zona horaria:<br>UTC - Para tener en cuenta todas las zonas horarias, 1 día natural examina de 24 a 48 horas del historial del usuario, dependiendo de la hora en que se evalúe el segmento; para 2 días naturales, examina de 48 a 72 horas del historial del usuario, y así sucesivamente.
    tags:
      - Custom events
  - name: X Custom Event Property In Y Days
    description: Determina si un usuario ha realizado o no un evento registrado especialmente en relación con una propiedad específica entre 0 y 50 veces en el último número especificado de días naturales entre 1 y 30. (Día natural = 1 día natural examina de 24 a 48 horas del historial del usuario)<br><a href="/docs/x-in-y-behavior">Más información sobre el comportamiento X en Y aquí.</a> <br><br>Ejemplo:<br> Añadido a favoritos con la propiedad "event_name" exactamente 0 veces en el último 1 día natural<br><br>Zona horaria:<br>UTC - Para tener en cuenta todas las zonas horarias, 1 día natural examina de 24 a 48 horas del historial del usuario, dependiendo de la hora en que se evalúe el segmento; para 2 días naturales, examina de 48 a 72 horas del historial del usuario, y así sucesivamente.
    tags:
      - Custom events
  - name: Email Address
    description: Te permite designar a los destinatarios de tu campaña por direcciones de correo electrónico individuales para pruebas. También se puede utilizar para enviar correos transaccionales a todos tus usuarios (incluidos los que cancelaron su suscripción) utilizando el especificador "La dirección de correo electrónico no está en blanco" dentro del filtro, para que puedas maximizar la entrega de correos electrónicos independientemente del estado de adhesión voluntaria. <br><br>Este filtro solo comprueba si los perfiles de usuario tienen una dirección de correo electrónico, mientras que el filtro <a href="/docs/user_guide/audience/segments/segmentation_filters#email-available">Correo electrónico disponible</a> comprueba criterios adicionales.
    tags:
      - Other Filters
  - name: External User ID
    description: Te permite designar a los destinatarios de tu campaña por ID de usuario individuales para pruebas.
    tags:
      - Other Filters
  - name: "Random Bucket #"
    description: Segmenta a tus usuarios por un número asignado aleatoriamente (de 0 a 9999 inclusive). Puede permitir la creación de segmentos uniformemente distribuidos de usuarios verdaderamente aleatorios para pruebas A/B y multivariantes.
    tags:
      - Other Filters
  - name: Session Count
    description: Segmenta a tus usuarios por el número de sesiones que han tenido en cualquiera de tus aplicaciones dentro de tu espacio de trabajo.
    tags:
      - Sessions
  - name: Session Count For App
    description: Segmenta a tus usuarios por el número de sesiones que han tenido en una aplicación específica designada.
    tags:
      - Sessions
  - name: X Sessions In Last Y Days
    description: Segmenta a tus usuarios por el número de sesiones (entre 0 y 50) que han tenido en tu aplicación en el último número especificado de días naturales entre 1 y 30. <br> <a href="/docs/x-in-y-behavior">Más información sobre el comportamiento X en Y aquí.</a>
    tags:
      - Sessions
  - name: First Used App
    description: Segmenta a tus usuarios por la primera vez registrada en que abrieron tu aplicación. <em>Esto captura la primera sesión que tuvieron usando una versión de tu aplicación con el SDK de Braze integrado.</em> (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa
    tags:
      - Sessions
  - name: First Used Specific App
    description: Segmenta a tus usuarios por la primera vez registrada en que abrieron cualquiera de tus aplicaciones dentro de tu espacio de trabajo. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa
    tags:
      - Sessions
  - name: Last Used App
    description: Segmenta a tus usuarios por la última vez que abrieron tu aplicación. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa
    tags:
      - Sessions
  - name: Last Used Specific App
    description: Segmenta a tus usuarios por la última vez que abrieron una aplicación específica designada. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa
    tags:
      - Sessions
  - name: Median Session Duration
    description: Segmenta a tus usuarios por la duración mediana de sus sesiones en tu aplicación.
    tags:
      - Sessions
  - name: Received Message from Campaign
    description: Segmenta a tus usuarios en función de si han recibido una campaña específica. <br><br>Para Content Cards, banners y mensajes dentro de la aplicación, esto es cuando un usuario registra una impresión, no cuando se envía la tarjeta o el mensaje dentro de la aplicación.<br><br> Para push y webhooks, esto es cuando el mensaje se envía al usuario.<br><br> Para WhatsApp, esto es cuando se envía la última solicitud de API de mensaje a WhatsApp, no cuando el mensaje se entrega en el dispositivo del usuario.<br><br> Para correos electrónicos, el perfil de usuario objetivo coincide con este filtro cuando se envía una solicitud de correo electrónico al proveedor de servicios de correo electrónico (independientemente de si realmente se entrega).<br><br> Para SMS y RCS, se considera que los usuarios han "recibido" un mensaje en el momento del envío. Incluso si el mensaje no llega al dispositivo del usuario, el usuario sigue coincidiendo con este filtro.<br><br> Cuando un mensaje se entrega, abre o se hace clic en él, Braze actualiza los datos de todos los perfiles que comparten el mismo identificador de canal (por ejemplo, correo electrónico o número de teléfono), por lo que los usuarios que comparten un identificador con alguien que recibió el mensaje pueden coincidir con este filtro aunque su perfil no haya recibido directamente la campaña.
    tags:
      - Retargeting
  - name: Received Campaign Variant
    description: Segmenta a tus usuarios por la variante de una campaña multivariante que han recibido.<br><br>Este filtro se aplica a campañas multivariantes y campañas de push rápido multivariantes. Las campañas de API, las campañas multicanal estándar y las campañas de experimento con conmutadores de características no aparecen en el selector de campañas. Las campañas solo de webhook no aparecen en el selector de campañas.<br><br>Para Content Cards, banners y mensajes dentro de la aplicación, esto es cuando un usuario registra una impresión, no cuando se envía la tarjeta o el mensaje dentro de la aplicación.<br><br> Para push y webhooks, esto es cuando el mensaje se envía al usuario.<br><br> Para WhatsApp, esto es cuando se envía la última solicitud de API de mensaje a WhatsApp, no cuando el mensaje se entrega en el dispositivo del usuario.<br><br> Para correos electrónicos, el perfil de usuario objetivo coincide con este filtro cuando se envía una solicitud de correo electrónico al proveedor de servicios de correo electrónico (independientemente de si realmente se entrega).<br><br> Para SMS y RCS, se considera que los usuarios han "recibido" un mensaje en el momento del envío. Incluso si el mensaje no llega al dispositivo del usuario, el usuario sigue coincidiendo con este filtro.<br><br> Cuando un mensaje se entrega, abre o se hace clic en él, Braze actualiza los datos de todos los perfiles que comparten el mismo identificador de canal (por ejemplo, correo electrónico o número de teléfono), por lo que los usuarios que comparten un identificador con alguien que recibió el mensaje pueden coincidir con este filtro aunque su perfil no haya recibido directamente la campaña.
    tags:
      - Retargeting
  - name: Received Message from Canvas Step
    description: Segmenta a tus usuarios en función de si han recibido un componente específico de Canvas.<br><br>Para Content Cards y mensajes dentro de la aplicación, esto es cuando un usuario registra una impresión, no cuando se envía la tarjeta o el mensaje dentro de la aplicación.<br><br> Para push y webhooks, esto es cuando el mensaje se envía al usuario.<br><br> Para WhatsApp, esto es cuando se envía la última solicitud de API de mensaje a WhatsApp, no cuando el mensaje se entrega en el dispositivo del usuario.<br><br> Para correos electrónicos, el perfil de usuario objetivo coincide con este filtro cuando se envía una solicitud de correo electrónico al proveedor de servicios de correo electrónico (independientemente de si realmente se entrega).<br><br> Para SMS y RCS, se considera que los usuarios han "recibido" un mensaje en el momento del envío. Incluso si el mensaje no llega al dispositivo del usuario, el usuario sigue coincidiendo con este filtro.<br><br> Cuando un mensaje se entrega, abre o se hace clic en él, Braze actualiza los datos de todos los perfiles que comparten el mismo identificador de canal (por ejemplo, correo electrónico o número de teléfono), por lo que los usuarios que comparten un identificador con alguien que recibió el mensaje pueden coincidir con este filtro aunque su perfil no haya recibido directamente la campaña.
    tags:
      - Retargeting
  - name: Last Received Message from Specific Canvas Step
    description: Segmenta a tus usuarios por cuándo recibieron un componente específico de Canvas.<br><br> Dado que los datos se actualizan para todos los perfiles que comparten el mismo identificador de canal (por ejemplo, correo electrónico o teléfono) cuando se produce una entrega, apertura o clic, un usuario que comparte un identificador con alguien que recibió un mensaje puede no coincidir con este filtro aunque nunca se le haya enviado explícitamente el mensaje. Utiliza "Entered Canvas Variation" para aislar perfiles de usuario de duplicados.<br><br> Este filtro no tiene en cuenta cuándo los usuarios recibieron otros componentes de Canvas.
    tags:
      - Retargeting
  - name: Last Received Message from Specific Campaign
    description: Segmenta a tus usuarios en función de si han recibido una campaña específica.<br><br> Dado que los datos se actualizan para todos los perfiles que comparten el mismo identificador de canal (por ejemplo, correo electrónico o teléfono) cuando se produce una entrega, apertura o clic, un usuario que comparte un identificador con alguien que recibió un mensaje puede no coincidir con este filtro aunque nunca se le haya enviado explícitamente el mensaje.<br><br> Este filtro no tiene en cuenta cuándo los usuarios recibieron otras campañas.
    tags:
      - Retargeting
  - name: Received Message from Campaign or Canvas with Tag
    description: Segmenta a tus usuarios en función de si han recibido una campaña o Canvas específico con una etiqueta específica.<br><br>Braze evalúa solo las últimas 200 campañas y Canvas enviados que utilizan la etiqueta seleccionada cuando se ejecuta este filtro.<br><br> Para Content Cards, banners (solo Campaigns) y mensajes dentro de la aplicación, esto es cuando un usuario registra una impresión, no cuando se envía la tarjeta o el mensaje dentro de la aplicación.<br><br> Para push y webhooks, esto es cuando el mensaje se envía al usuario.<br><br> Para WhatsApp, esto es cuando se envía la última solicitud de API de mensaje a WhatsApp, no cuando el mensaje se entrega en el dispositivo del usuario.<br><br> Para correos electrónicos, el perfil de usuario objetivo coincide con este filtro cuando se envía una solicitud de correo electrónico al proveedor de servicios de correo electrónico (independientemente de si realmente se entrega).<br><br> Para SMS y RCS, se considera que los usuarios han "recibido" un mensaje en el momento del envío. Incluso si el mensaje no llega al dispositivo del usuario, el usuario sigue coincidiendo con este filtro.<br><br> Cuando un mensaje se entrega, abre o se hace clic en él, Braze actualiza los datos de todos los perfiles que comparten el mismo identificador de canal (por ejemplo, correo electrónico o número de teléfono), por lo que los usuarios que comparten un identificador con alguien que recibió el mensaje pueden coincidir con este filtro aunque su perfil no haya recibido directamente la campaña.
    tags:
      - Retargeting
  - name: Last Received Message from Campaign or Canvas With Tag
    description: Segmenta a tus usuarios por cuándo recibieron una campaña o Canvas específico con una etiqueta específica. Este filtro no tiene en cuenta cuándo los usuarios recibieron otras campañas o Canvas. (período de 24 horas)
    tags:
      - Retargeting
  - name: Has Never Received a Message from Campaign or Canvas Step
    description: Segmenta a tus usuarios en función de si han recibido alguna campaña o componente de Canvas.
    tags:
      - Retargeting
  - name: Last Received Email
    description: Segmenta a tus usuarios por la última vez que recibieron uno de tus mensajes de correo electrónico. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa
    tags:
      - Retargeting
  - name: Last Received Push
    description: Segmenta a tus usuarios por la última vez que recibieron una de tus notificaciones push. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa
    tags:
      - Retargeting
  - name: Last In App Message Impression
    description: Segmenta a tus usuarios por la última vez que vieron un mensaje dentro de la aplicación.
    tags:
      - Retargeting
  - name: Last Received SMS
    description: Segmenta a tus usuarios por la hora en que el último mensaje SMS, MMS o RCS fue entregado al proveedor de SMS o RCS. Esto no garantiza que el mensaje haya sido entregado en el dispositivo del usuario. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa
    tags:
      - Retargeting
  - name: Last Received Webhook
    description: Segmenta a tus usuarios por la última vez que Braze envió un webhook para ese usuario. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa
    tags:
      - Retargeting
  - name: Last Received WhatsApp
    description: Segmenta a tus usuarios por la última vez que recibieron un mensaje de WhatsApp. Esto es cuando se envía la última solicitud de API de mensaje a WhatsApp, no cuando el mensaje se entrega en el dispositivo del usuario. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa
    tags:
      - Retargeting
  - name: Live Activities Push to Start Registered for App
    description: Segmenta a tus usuarios en función de si están registrados para iniciar una Live Activity a través de notificaciones push de iOS para una aplicación específica.
    tags:
      - Devices
  - name: Clicked/Opened Campaign
    description: Filtra por interacción con una campaña específica. Para mensajes dentro de la aplicación, los clics en mensajes dentro de la aplicación incluyen clics en el cuerpo y en los botones. No cuenta las acciones de descarte ni el cierre del mensaje con la X.<br><br>Para correos electrónicos, el evento de apertura incluye tanto aperturas automáticas como aperturas no automáticas. Este filtro también incluye la opción de filtrar por "abrió cualquier correo electrónico (aperturas automáticas)" y "abrió cualquier correo electrónico (otras aperturas)". Los clics en enlaces de cancelación de suscripción y centros de preferencias no cuentan para este filtro. Si varios usuarios comparten la misma dirección de correo electrónico:<br>- Cuando el correo electrónico se abre o se hace clic en él, todos los demás usuarios con esa misma dirección de correo electrónico también tienen sus perfiles actualizados. <br>- Si el usuario original cambia su dirección de correo electrónico después de que se envía el mensaje y antes de la apertura o el clic, la apertura o el clic se aplica a todos los usuarios restantes con esa dirección de correo electrónico en lugar del usuario original.<br><br>Para SMS y RCS, una interacción se define como:<br>- El usuario envió por última vez una respuesta SMS o RCS que coincide con una categoría de palabra clave determinada. Esto se atribuye a la campaña más reciente recibida por todos los usuarios con este número de teléfono. La campaña debe haberse recibido en las últimas cuatro horas.<br>- El usuario seleccionó por última vez cualquier enlace acortado en un mensaje SMS o RCS que tiene activado el seguimiento de clics del usuario, de una campaña determinada.
    tags:
      - Retargeting
  - name: Clicked/Opened Campaign or Canvas With Tag
    description: Filtra por interacción con una campaña específica que tiene una etiqueta específica. Para mensajes dentro de la aplicación, los clics en mensajes dentro de la aplicación incluyen clics en el cuerpo y en los botones. No cuenta las acciones de descarte ni el cierre del mensaje con la X.<br><br>Para correos electrónicos, el evento de apertura incluye tanto aperturas automáticas como aperturas no automáticas. Este filtro también incluye la opción de filtrar por "abrió cualquier correo electrónico (aperturas automáticas)" y "abrió cualquier correo electrónico (otras aperturas)". Si varios usuarios comparten la misma dirección de correo electrónico:<br>- Cuando el correo electrónico se abre o se hace clic en él, todos los demás usuarios con esa misma dirección de correo electrónico también tienen sus perfiles actualizados. <br>- Si el usuario original cambia su dirección de correo electrónico después de que se envía el mensaje y antes de la apertura o el clic, la apertura o el clic se aplica a todos los usuarios restantes con esa dirección de correo electrónico en lugar del usuario original.<br><br>Para SMS y RCS, una interacción se define como:<br>- El usuario envió por última vez una respuesta SMS o RCS que coincide con una categoría de palabra clave determinada. Esto se atribuye a la campaña más reciente recibida por todos los usuarios con este número de teléfono. La campaña debe haberse recibido en las últimas cuatro horas.<br>- Cuando el usuario seleccionó por última vez cualquier enlace acortado en un mensaje SMS o RCS que tiene activado el seguimiento de clics del usuario, de una campaña o paso en Canvas determinado con etiqueta.
    tags:
      - Retargeting
  - name: Clicked/Opened Step
    description: Filtra por interacción con un componente específico de Canvas. Para mensajes dentro de la aplicación, los clics en mensajes dentro de la aplicación también cuentan los clics en el cuerpo y en los botones. No cuenta las acciones de descarte ni el cierre del mensaje con la X.<br><br>Para correos electrónicos, el evento de apertura incluye tanto aperturas automáticas como aperturas no automáticas. Este filtro también incluye la opción de filtrar por "abrió cualquier correo electrónico (aperturas automáticas)" y "abrió cualquier correo electrónico (otras aperturas)".<br><br>Para SMS y RCS, una interacción se define como:<br>- El usuario envió por última vez una respuesta SMS o RCS que coincide con una categoría de palabra clave determinada. Esto se atribuye a la campaña más reciente recibida por todos los usuarios con este número de teléfono. La campaña debe haberse recibido en las últimas cuatro horas. <br>- El usuario seleccionó por última vez cualquier enlace acortado en un mensaje SMS o RCS que tiene activado el seguimiento de clics del usuario, de un paso en Canvas determinado.
    tags:
      - Retargeting
  - name: Clicked Alias in Campaign
    description: Filtra a tus usuarios en función de si hicieron clic en un alias específico en una campaña específica. Esto solo se aplica a mensajes de correo electrónico. <br><br> Si varios usuarios comparten la misma dirección de correo electrónico:<br>- Cuando el correo electrónico se abre o se hace clic en él, todos los demás usuarios con esa misma dirección de correo electrónico también tienen sus perfiles actualizados. <br>- Si el usuario original cambia su dirección de correo electrónico después de que se envía el mensaje y antes de la apertura o el clic, la apertura o el clic se aplica a todos los usuarios restantes con esa dirección de correo electrónico en lugar del usuario original.
    tags:
      - Retargeting
  - name: Clicked Alias in Canvas Step
    description: Filtra a tus usuarios en función de si hicieron clic en un alias específico en un Canvas específico. Esto solo se aplica a mensajes de correo electrónico. <br><br> Si varios usuarios comparten la misma dirección de correo electrónico:<br>- Cuando el correo electrónico se abre o se hace clic en él, todos los demás usuarios con esa misma dirección de correo electrónico también tienen sus perfiles actualizados. <br>- Si el usuario original cambia su dirección de correo electrónico después de que se envía el mensaje y antes de la apertura o el clic, la apertura o el clic se aplica a todos los usuarios restantes con esa dirección de correo electrónico en lugar del usuario original.
    tags:
      - Retargeting
  - name: Clicked Alias in Any Campaign or Canvas Step
    description: Filtra a tus usuarios en función de si hicieron clic en un alias específico en cualquier campaña o Canvas. Esto solo se aplica a mensajes de correo electrónico. <br><br> Si varios usuarios comparten la misma dirección de correo electrónico:<br>- Cuando el correo electrónico se abre o se hace clic en él, todos los demás usuarios con esa misma dirección de correo electrónico también tienen sus perfiles actualizados. <br>- Si el usuario original cambia su dirección de correo electrónico después de que se envía el mensaje y antes de la apertura o el clic, la apertura o el clic se aplica a todos los usuarios restantes con esa dirección de correo electrónico en lugar del usuario original.
    tags:
      - Retargeting
  - name: Hard Bounced
    description: Segmenta a tus usuarios en función de si su dirección de correo electrónico ha tenido un rebote duro (por ejemplo, la dirección de correo electrónico no es válida). Para exportar usuarios con correos electrónicos no válidos, llama al <a href="/docs/api/endpoints/email/get_list_hard_bounces/">endpoint <code>/email/hard_bounces</code></a> o crea un segmento con filtros como la dirección de correo electrónico no está en blanco, el correo electrónico no está disponible y el estado de suscripción de correo electrónico no es cancelado.
    tags:
      - Retargeting
  - name: Soft Bounced
    description: Segmenta a tus usuarios en función de si tuvieron un rebote blando X veces en Y días. Los filtros de segmento solo pueden mirar hacia atrás 30 días, pero puedes mirar más atrás con las extensiones de segmento.<br><br>Este filtro funciona de manera diferente a un evento de rebote blando en Currents. El filtro de segmento de rebote blando cuenta un rebote blando si no hubo una entrega exitosa durante el período de reintento de 72 horas. En Currents, cada reintento fallido se envía como un evento de rebote blando.
    tags:
      - Retargeting
  - name: Has Marked You As Spam
    description: Segmenta a tus usuarios en función de si han marcado tus mensajes como correo no deseado.
    tags:
      - Retargeting
  - name: Invalid Phone Number
    description: Segmenta a tus usuarios en función de si su número de teléfono no es válido.
    tags:
      - Retargeting
  - name: Last Sent Specific SMS Inbound Keyword Category
    description: Segmenta a tus usuarios por cuándo enviaron por última vez un SMS, MMS o RCS a un grupo de suscripción específico dentro de una categoría de palabra clave específica.
    tags:
      - Retargeting
  - name: Converted From Campaign
    description: Segmenta a tus usuarios en función de si convirtieron en una campaña específica. Este filtro no incluye a los usuarios que están en el grupo de control.
    tags:
      - Retargeting
  - name: Converted From Canvas
    description: Segmenta a tus usuarios en función de si convirtieron en un Canvas específico. Este filtro no incluye a los usuarios que están en el grupo de control.
    tags:
      - Retargeting
  - name: In Campaign Control Group
    description: Segmenta a tus usuarios en función de si estaban en el grupo de control de una campaña multivariante específica.
    tags:
      - Retargeting
  - name: In Canvas Control Group
    description: Segmenta a tus usuarios en función de si estaban en el grupo de control de un Canvas específico. Este filtro solo evalúa a los usuarios que han entrado en el Canvas, por lo que los usuarios que nunca entraron se excluyen completamente de los resultados.<br><br>Por ejemplo, si filtras por usuarios que no están en el grupo de control de un Canvas, solo recibirás usuarios que entraron en el Canvas y fueron asignados a una variante que no es de control; los usuarios que nunca entraron en el Canvas no se incluyen. Para incluir a todos los usuarios independientemente de la entrada al Canvas, utiliza el filtro <code>Entered Canvas Variation</code> en su lugar.
    tags:
      - Retargeting
  - name: Last Enrolled in Any Control Group
    description: Segmenta a tus usuarios por la última vez que cayeron en el grupo de control de una campaña. <br><br>Zona horaria:<br>Zona horaria de la empresa
    tags:
      - Retargeting
  - name: Entered Canvas Variation
    description: Segmenta a tus usuarios en función de si han entrado en una ruta de variación de un Canvas específico. Este filtro evalúa a todos los usuarios.<br><br>Por ejemplo, si filtras por usuarios que no han entrado en un grupo de control de variación de Canvas, recibirás a todos los usuarios que no están en el grupo de control independientemente de si entraron en el Canvas.
    tags:
      - Retargeting
  - name: Last Received Any Message
    description: Segmenta a tus usuarios determinando el último mensaje que fue recibido. (período de 24 horas)<br><br>Para Content Cards, banners y mensajes dentro de la aplicación, esto es cuando un usuario registró por última vez una impresión, no cuando se envió por última vez la tarjeta o el mensaje dentro de la aplicación.<br><br>Para push y webhooks, esto es cuando cualquier mensaje fue enviado al usuario.<br><br> Para WhatsApp, esto es cuando se envió la última solicitud de API de mensaje a WhatsApp, no cuando el mensaje fue entregado en el dispositivo del usuario.<br><br> Para correos electrónicos, el perfil de usuario objetivo coincide con este filtro cuando se envía una solicitud de correo electrónico al proveedor de servicios de correo electrónico (independientemente de si realmente se entrega).<br><br> Para SMS y RCS, se considera que los usuarios han "recibido" un mensaje en el momento del envío. Incluso si el mensaje no llega al dispositivo del usuario, el usuario sigue coincidiendo con este filtro.<br><br> Cuando un mensaje se entrega, abre o se hace clic en él, Braze actualiza los datos de todos los perfiles que comparten el mismo identificador de canal (por ejemplo, correo electrónico o número de teléfono), por lo que los usuarios que comparten un identificador con alguien que recibió el mensaje pueden coincidir con este filtro aunque su perfil no haya recibido directamente la campaña.<br><br>Ejemplo:<br>Último mensaje recibido hace menos de 1 día = hace menos de 24 horas<br><br>Zona horaria:<br>Zona horaria de la empresa
    tags:
      - Retargeting
  - name: Last Engaged With Message
    description: Segmenta a tus usuarios por la última vez que hicieron clic o abrieron uno de tus canales de mensajería (banners, Content Cards, correo electrónico, dentro de la aplicación, SMS, RCS, push, WhatsApp).<br><br>Para Content Cards, banners y mensajes dentro de la aplicación, esto es cuando un usuario registra una impresión, no cuando se envía la tarjeta o el mensaje dentro de la aplicación.<br><br> Para push y webhooks, esto es cuando el mensaje se envía al usuario.<br><br> Para WhatsApp, esto es cuando se envía la última solicitud de API de mensaje a WhatsApp, no cuando el mensaje se entrega en el dispositivo del usuario.<br><br> Para mensajes de correo electrónico, el evento de apertura incluye tanto aperturas automáticas como aperturas no automáticas. (período de 24 horas)<br><br>Para correos electrónicos, el perfil de usuario objetivo coincide con este filtro cuando se envía una solicitud de correo electrónico al proveedor de servicios de correo electrónico (independientemente de si realmente se entrega). Esto también incluye la opción de filtrar por "abrió cualquier correo electrónico (aperturas automáticas)" y "abrió cualquier correo electrónico (otras aperturas)".<br><br> Para SMS y RCS, esto es cuando el usuario seleccionó por última vez cualquier enlace acortado en un mensaje que tiene activado el seguimiento de clics del usuario.<br><br> Cuando un mensaje se entrega, abre o se hace clic en él, Braze actualiza los datos de todos los perfiles que comparten el mismo identificador de canal (por ejemplo, correo electrónico o número de teléfono), por lo que los usuarios que comparten un identificador con alguien que recibió el mensaje pueden coincidir con este filtro aunque su perfil no haya recibido directamente la campaña.<br><br>Zona horaria:<br>Zona horaria de la empresa
    tags:
      - Retargeting
  - name: Clicked card
    description: Segmenta a tus usuarios en función de si han hecho clic en una Content Card específica. Este filtro está disponible como subfiltro de "Hizo clic/abrió campaña", "Hizo clic/abrió campaña o Canvas con etiqueta" y "Hizo clic/abrió paso".
    tags:
      - Retargeting
  - name: Feature Flags
    description: El segmento de tus usuarios que tienen un <a href="/docs/developer_guide/feature_flags">conmutador de características</a> particular habilitado actualmente.
    tags:
      - Retargeting
  - name: Subscription Group
    description: Segmenta a tus usuarios por su grupo de suscripción para correo electrónico, SMS, MMS, RCS o WhatsApp. Los grupos archivados no aparecen y no se pueden utilizar.
    tags:
      - Channel subscription behavior
  - name: Email Available
    description: Segmenta a tus usuarios en función de si tienen una dirección de correo electrónico válida y si están suscritos u optados para recibir correo electrónico. Este filtro comprueba tres criterios&#58; si el usuario canceló su suscripción a correos electrónicos, si Braze ha recibido un rebote duro y si el correo electrónico fue marcado como correo no deseado. Si se cumple alguno de estos criterios, o si no existe un correo electrónico para un usuario, el usuario no se incluye.<br><br>Los usuarios cuyo correo electrónico disponible es <code>false</code> se excluyen de la audiencia de la campaña y no reciben el correo electrónico, incluso si tus ajustes de envío están configurados para enviar a todos los usuarios (incluidos los usuarios que cancelaron su suscripción).<br><br>Para correos electrónicos donde el estado de adhesión voluntaria importa, utiliza Correo electrónico disponible en lugar de <a href="/docs/user_guide/audience/segments/segmentation_filters#email-address">Dirección de correo electrónico</a>. Los criterios adicionales te ayudan a dirigirte a usuarios que son elegibles para recibir correo electrónico.
    tags:
      - Channel subscription behavior
  - name: Email Opt In Date
    description: Segmenta a tus usuarios por la fecha en que optaron por recibir correo electrónico.
    tags:
      - Channel subscription behavior
  - name: Email Subscription Status
    description: Segmenta a tus usuarios por su estado de suscripción de correo electrónico.
    tags:
      - Channel subscription behavior
  - name: Email Unsubscribed Date
    description: Segmenta a tus usuarios por la fecha en que cancelaron su suscripción a futuros correos electrónicos.
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled
    description: Segmenta a tus usuarios que tienen autorización provisional de push o están habilitados para push en primer plano. Específicamente, este recuento incluye:<br>1. Usuarios de iOS que están provisionalmente autorizados para push. <br>2. Usuarios que están habilitados para push en primer plano y cuyo estado de suscripción push no es cancelado, para cualquiera de tus aplicaciones. Para estos usuarios, este recuento incluye solo push en primer plano.<br><br>Push en primer plano habilitado no incluye a los usuarios que han cancelado su suscripción. <br><br>Después de segmentar con este filtro, puedes ver un desglose de quién está en ese segmento para Android, iOS y web en el panel inferior, llamado <em>Usuarios alcanzables</em>.
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled for App
    description: Segmenta en función de si los usuarios tienen push habilitado para tu aplicación en su dispositivo. Usuarios que están habilitados para push en primer plano para una aplicación. Esto no tiene en cuenta el estado de suscripción push. Este recuento incluye a los usuarios que han autorizado provisionalmente tokens de push en primer plano y en segundo plano.
    tags:
      - Channel subscription behavior
  - name: Background or Foreground Push Enabled
    description: Segmenta en función de si los usuarios tienen un token de push y no han cancelado su suscripción. Usuarios que están habilitados para push en segundo plano o en primer plano para cualquiera de tus aplicaciones.
    tags:
      - Channel subscription behavior
  - name: Push Opt In Date
    description: Segmenta a tus usuarios por la fecha en que optaron por recibir push.
    tags:
      - Channel subscription behavior
  - name: Push Subscription Status
    description: Segmenta a tus usuarios por su <a href="/docs/user_guide/channels/push/push_setup/push_subscription_states">estado de suscripción</a> para push.
    tags:
      - Channel subscription behavior
  - name: Push Unsubscribed Date
    description: Segmenta a tus usuarios por la fecha en que cancelaron su suscripción a futuras notificaciones push.
    tags:
      - Channel subscription behavior
  - name: Purchased Product
    description: Segmenta a tus usuarios por productos comprados en tu aplicación.
    tags:
      - Purchase behavior
  - name: Total Number of Purchases
    description: Segmenta a tus usuarios por cuántas compras han realizado en tu aplicación.
    tags:
      - Purchase behavior
  - name: X Product Purchased In Y Days
    description: Filtra a los usuarios por las veces que se compró un producto específico.
    tags:
      - Purchase behavior
  - name: X Purchases in Last Y Days
    description: Segmenta a tus usuarios por el número de veces (entre 0 y 50) que han realizado una compra en el último número especificado de días naturales entre 1 y 30. <br> <a href="/docs/x-in-y-behavior">Más información sobre el comportamiento X en Y aquí.</a>
    tags:
      - Purchase behavior
  - name: X Purchase Property In Y Days
    description: Segmenta a tus usuarios por el número de veces que se realizó una compra en relación con una propiedad de compra determinada en el último número especificado de días naturales entre 1 y 30. <br> <a href="/docs/x-in-y-behavior">Más información sobre el comportamiento X en Y aquí.</a>
    tags:
      - Purchase behavior
  - name: First Made Purchase
    description: Segmenta a tus usuarios por la primera vez que un usuario realizó una compra en tu aplicación.
    tags:
      - Purchase behavior
  - name: First Purchase For App
    description: Segmenta a tus usuarios por la primera vez que un usuario realizó una compra desde tu aplicación.
    tags:
      - Purchase behavior
  - name: Last Made Purchase
    description: Filtra a los usuarios por la última vez que realizaron una compra.
    tags:
      - Purchase behavior
  - name: Last Purchased Product
    description: Filtra a los usuarios por cuándo compraron por última vez un producto específico.
    tags:
      - Purchase behavior
  - name: Money Spent
    description: Segmenta a tus usuarios por la cantidad de dinero que han gastado en tu aplicación.
    tags:
      - Purchase behavior
  - name: X Money Spent in Y Days
    description: Segmenta a tus usuarios por la cantidad de dinero que han gastado en tu aplicación en el último número especificado de días naturales entre 1 y 30. Esta cantidad incluye solo la suma de las últimas 50 compras. <br> <a href="/docs/x-in-y-behavior">Más información sobre el comportamiento X en Y aquí.</a>
    tags:
      - Purchase behavior
  - name: Last order placed (last 730 days)
    description: Segmenta a tus usuarios por cuándo realizaron su último pedido, que se basa en el <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de comercio electrónico</a> para pedido realizado (los espacios de trabajo que no rastrean eventos de comercio electrónico no tienen datos para este filtro). Los usuarios se evalúan para este filtro una vez al día, y la ventana máxima de retrospección es de los últimos 2 años.<br><br>Este filtro está en beta. Ponte en contacto con tu director de cuentas de Braze si te interesa utilizar este filtro.
    tags:
      - eCommerce
  - name: Total orders count (last 730 days)
    description: Segmenta a tus usuarios por el recuento total de pedidos de un usuario en los últimos 2 años, basado en el <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de comercio electrónico</a> para pedido realizado (los espacios de trabajo que no rastrean eventos de comercio electrónico no tienen datos para este filtro). Este recuento excluye los pedidos cancelados, que deben rastrearse utilizando el <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de comercio electrónico</a> para pedido cancelado. Los usuarios se evalúan para este filtro una vez al día.<br><br>Este filtro está en beta. Ponte en contacto con tu director de cuentas de Braze si te interesa utilizar este filtro.
    tags:
      - eCommerce
  - name: Total orders count
    description: Segmenta a tus usuarios por el recuento total de pedidos de un usuario a lo largo de su vida, basado en el <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de comercio electrónico</a> para pedido realizado (los espacios de trabajo que no rastrean eventos de comercio electrónico no tienen datos para este filtro). Este recuento excluye los pedidos cancelados, que deben rastrearse utilizando el <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de comercio electrónico</a> para pedido cancelado. Los usuarios se evalúan para este filtro en tiempo real.<br><br>Este filtro está en beta. Ponte en contacto con tu director de cuentas de Braze si te interesa utilizar este filtro.
    tags:
      - eCommerce
  - name: Total canceled orders count (last 730 days)
    description: Segmenta a tus usuarios por el recuento total de pedidos que un usuario canceló en los últimos 2 años, basado en el <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de comercio electrónico</a> para pedido realizado (los espacios de trabajo que no rastrean eventos de comercio electrónico no tienen datos para este filtro). Los usuarios se evalúan para este filtro una vez al día.<br><br>Este filtro está en beta. Ponte en contacto con tu director de cuentas de Braze si te interesa utilizar este filtro.
    tags:
      - eCommerce
  - name: Customer lifetime value (last 730 days)
    description: Segmenta a tus usuarios por los ingresos totales que se espera que un usuario genere a lo largo de su historial de compras con tu marca. El cálculo considera los últimos 730 días y toma el valor medio del pedido (AOV), lo multiplica por el número total de pedidos realizados y luego tiene en cuenta la duración de compra activa del usuario (el período de tiempo entre su primer y su pedido más reciente). Este filtro utiliza datos rastreados en <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eventos recomendados de comercio electrónico</a> (los espacios de trabajo que no rastrean eventos de comercio electrónico no tienen datos para este filtro). Los usuarios se evalúan para este filtro una vez al día.<br><br>Este filtro está en beta. Ponte en contacto con tu director de cuentas de Braze si te interesa utilizar este filtro.
    tags:
      - eCommerce
  - name: Total refund value (last 730 days)
    description: Segmenta a tus usuarios por el valor de los reembolsos otorgados a un usuario en los últimos 2 años, basado en el <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de comercio electrónico</a> para pedido reembolsado (los espacios de trabajo que no rastrean eventos de comercio electrónico no tienen datos para este filtro). Los usuarios se evalúan para este filtro una vez al día.<br><br>Este filtro está en beta. Ponte en contacto con tu director de cuentas de Braze si te interesa utilizar este filtro.
    tags:
      - eCommerce
  - name: Total refund value
    description: Segmenta a tus usuarios por el valor total de los reembolsos otorgados a un usuario a lo largo de su vida, basado en el <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de comercio electrónico</a> para pedido reembolsado (los espacios de trabajo que no rastrean eventos de comercio electrónico no tienen datos para este filtro). Los usuarios se evalúan para este filtro en tiempo real.<br><br>Este filtro está en beta. Ponte en contacto con tu director de cuentas de Braze si te interesa utilizar este filtro.
    tags:
      - eCommerce
  - name: Total revenue (last 730 days)
    description: Segmenta a tus usuarios por los ingresos totales generados a partir de los pedidos de un usuario en los últimos 2 años, calculados restando los ingresos asociados con el <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de comercio electrónico</a> para pedido reembolsado de los ingresos asociados con el evento de comercio electrónico para pedido realizado (los espacios de trabajo que no rastrean eventos de comercio electrónico no tienen datos para este filtro). Los usuarios se evalúan para este filtro una vez al día.<br><br>Este filtro está en beta. Ponte en contacto con tu director de cuentas de Braze si te interesa utilizar este filtro.
    tags:
      - eCommerce
  - name: Total revenue
    description: Segmenta a tus usuarios por los ingresos totales generados a partir de los pedidos de un usuario a lo largo de su vida, calculados restando los ingresos asociados con el <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de comercio electrónico</a> para pedido reembolsado de los ingresos asociados con el evento de comercio electrónico para pedido realizado (los espacios de trabajo que no rastrean eventos de comercio electrónico no tienen datos para este filtro). Los usuarios se evalúan para este filtro en tiempo real.<br><br>Este filtro está en beta. Ponte en contacto con tu director de cuentas de Braze si te interesa utilizar este filtro.
    tags:
      - eCommerce
  - name: Average order value (last 730 days)
    description: Segmenta a tus usuarios por el valor medio de los pedidos de un usuario en los últimos 2 años, basado en el <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de comercio electrónico</a> para pedido realizado (los espacios de trabajo que no rastrean eventos de comercio electrónico no tienen datos para este filtro). Los usuarios se evalúan para este filtro una vez al día.<br><br>Este filtro está en beta. Ponte en contacto con tu director de cuentas de Braze si te interesa utilizar este filtro.
    tags:
      - eCommerce
  - name: Country
    description: Segmenta a tus usuarios por la última ubicación de país indicada.
    tags:
      - Demographic attributes
  - name: City
    description: Segmenta a tus usuarios por la última ubicación de ciudad indicada.
    tags:
      - Demographic attributes
  - name: Language
    description: Segmenta a tus usuarios por su idioma preferido.
    tags:
      - Demographic attributes
  - name: Age
    description: Segmenta a tus usuarios por su edad, según lo indicaron dentro de tu aplicación.
    tags:
      - Demographic attributes
  - name: Birthday
    description: Segmenta a tus usuarios por su fecha de cumpleaños, según lo indicaron dentro de tu aplicación. <br> Los usuarios con cumpleaños el 29 de febrero se incluyen en los segmentos que incluyen el 1 de marzo.<br><br>Para dirigirte a cumpleaños de diciembre o enero, solo inserta la lógica de filtro dentro del período de 12 meses del año al que te diriges. En otras palabras, no insertes lógica que mire hacia atrás al diciembre del año calendario anterior o hacia adelante al enero del año siguiente. Por ejemplo, para dirigirte a cumpleaños de diciembre, puedes filtrar por "el 31 de diciembre", "antes del 31 de diciembre" o "después del 30 de noviembre".
    tags:
      - Demographic attributes
  - name: Gender
    description: Segmenta a tus usuarios por género, según lo indicaron dentro de tu aplicación.
    tags:
      - Demographic attributes
  - name: Unformatted Phone Number
    description: Segmenta a tus usuarios por su número de teléfono sin formato. No incluye paréntesis, guiones ni otros símbolos.
    tags:
      - Demographic attributes
  - name: First Name
    description: Segmenta a tus usuarios por su nombre, según lo indicaron dentro de tu aplicación.
    tags:
      - Demographic attributes
  - name: Last Name
    description: Segmenta a tus usuarios por su apellido, según lo indicaron dentro de tu aplicación.
    tags:
      - Demographic attributes
  - name: Has App
    description: Segmenta en función de si un usuario ha instalado alguna vez tu aplicación. Esto incluye a los usuarios que actualmente tienen tu aplicación instalada y a los que la desinstalaron en el pasado. Generalmente, esto requiere que los usuarios abran la aplicación (iniciar una sesión) para ser incluidos en este filtro. Sin embargo, hay algunas excepciones, como si un usuario fue importado a Braze y asociado manualmente con tu aplicación.
    tags:
      - App
  - name: Most Recent App Version Name
    description: Segmenta por el nombre más reciente de la versión de la aplicación del usuario.<br><br>Al usar "menor que" o "menor o igual que", si la versión principal de la aplicación no existe, este filtro devuelve `true` porque el usuario es más antiguo que la versión de la aplicación. Esto significa que si la última versión principal de la aplicación del usuario no existe, coincide automáticamente con el filtro.
    tags:
      - App
  - name: Most Recent App Version Number
    description: Segmenta por el número de versión más reciente de la aplicación del usuario. El número de versión dentro de los paréntesis se utiliza para filtrar, mientras que el número que lo precede es de referencia; por ejemplo, en "3.7.0(134.0.0.0)", "134.0.0.0" es el número de versión filtrado.<br><br>Al usar "menor que" o "menor o igual que", si la versión principal de la aplicación no existe, este filtro devuelve `true` porque el usuario es más antiguo que la versión de la aplicación. Esto significa que si la última versión principal de la aplicación del usuario no existe, coincide automáticamente con el filtro.<br><br>Puede tomar tiempo para que las versiones actuales de la aplicación se completen. La versión de la aplicación en el perfil del usuario se actualiza cuando la información es capturada por el SDK, lo cual depende de cuándo los usuarios abren sus aplicaciones. Si el usuario no abre la aplicación, la versión actual no se actualizará. Estos filtros tampoco se aplican retroactivamente. Es recomendable usar "mayor que" o "igual" a las versiones actuales y futuras, pero usar filtros de versiones pasadas puede causar comportamientos inesperados.
    tags:
      - App
  - name: Uninstalled
    description: Segmenta a tus usuarios en función de si actualmente están marcados como desinstalados en el backend. Los usuarios que desinstalaron y luego reinstalaron la aplicación no se incluyen. Este filtro refleja el estado actual de desinstalación, no un registro histórico de cada evento de desinstalación.
    tags:
      - Uninstall
  - name: Device Carrier
    description: Segmenta a tus usuarios por su operador de dispositivo.
    tags:
      - Devices
  - name: Device Count
    description: Segmenta a tus usuarios por cuántos dispositivos han utilizado tu aplicación.
    tags:
      - Devices
  - name: Device Model
    description: Segmenta a tus usuarios por la versión del modelo de su teléfono móvil.
    tags:
      - Devices
  - name: Device OS
    description: Segmenta a tus usuarios que tienen uno o más dispositivos con el sistema operativo especificado. Para segmentar usuarios por un rango de sistemas operativos, utiliza el filtro <a href="/docs/user_guide/audience/segments/segmentation_filters#device-os-version-number">Número de versión del SO del dispositivo</a>.
    tags:
      - Devices
  - name: Device OS Version Number
    description: Segmenta a tus usuarios que tienen uno o más dispositivos con una versión de sistema operativo que está dentro de un rango especificado. Por ejemplo, puedes dirigirte a usuarios que tienen una versión del sistema operativo iOS que es superior o igual a 26.0.
    tags:
      - Devices
  - name: Most Recent Device Locale
    description: Segmenta a tus usuarios por la <a href="/docs/user_guide/messaging/messaging_fundamentals/localization">información de configuración regional</a> del dispositivo utilizado más recientemente.
    tags:
      - Devices
  - name: Most Recent Watch Model
    description: Segmenta a tus usuarios por su modelo de reloj inteligente más reciente.
    tags:
      - Devices
  - name: Provisionally Authorized on iOS
    description: Te permite encontrar usuarios que están provisionalmente autorizados en iOS 12 para una aplicación determinada.
    tags:
      - Devices
  - name: Web Browser
    description: Segmenta a tus usuarios por el navegador web que utilizan para acceder a tu sitio web. Este filtro coincide con cualquier navegador en el historial de dispositivos del usuario, no solo con el navegador utilizado más recientemente.
    tags:
      - Devices
  - name: Device IDFA
    description: Te permite designar a los destinatarios de tu campaña por IDFA para pruebas.
    tags:
      - Advertising use cases
  - name: Device IDFV
    description: Te permite designar a los destinatarios de tu campaña por IDFV para pruebas.
    tags:
      - Advertising use cases
  - name: Device Google Ad ID
    description: Segmenta a tus usuarios por el ID de anuncio de Google.
    tags:
      - Advertising use cases
  - name: Device Roku Ad ID
    description: Segmenta a tus usuarios por el ID de anuncio de Roku.
    tags:
      - Advertising use cases
  - name: Device Windows Ad ID
    description: Segmenta a tus usuarios por el ID de anuncio de Windows.
    tags:
      - Advertising use cases
  - name: Ad Tracking Enabled
    description: Te permite filtrar en función de si tus usuarios han optado por el seguimiento de anuncios. El seguimiento de anuncios se relaciona con el IDFA o "identificador para anunciantes" asignado a todos los dispositivos iOS por Apple, que puede ser configurado por los SDK. Este identificador permite a los anunciantes rastrear a los usuarios y mostrarles anuncios dirigidos.
    tags:
      - Advertising use cases
  - name: Most Recent Location
    description: Segmenta a tus usuarios por la última ubicación registrada en la que utilizaron tu aplicación.
    tags:
      - Location
  - name: Location Available
    description: Segmenta a tus usuarios en función de si han reportado sus ubicaciones. Para utilizar este filtro, tu aplicación necesita tener <a href="/docs/search?query=location%20tracking">el seguimiento de ubicación integrado.</a>
    tags:
      - Location
  - name: Amplitude Cohorts
    description: Los clientes que utilizan Amplitude pueden complementar sus segmentos eligiendo e importando sus cohortes en Amplitude.
    tags:
      - Cohort membership
  - name: Census Cohorts
    description: Los clientes que utilizan Census pueden complementar sus segmentos eligiendo e importando sus cohortes en Census.
    tags:
      - Cohort membership
  - name: Heap Cohorts
    description: Los clientes que utilizan Heap pueden complementar sus segmentos eligiendo e importando sus cohortes en Heap.
    tags:
      - Cohort membership
  - name: Hightouch Cohorts
    description: Los clientes que utilizan Hightouch pueden complementar sus segmentos eligiendo e importando sus cohortes en Hightouch.
    tags:
      - Cohort membership
  - name: Kubit Cohorts
    description: Los clientes que utilizan Kubit pueden complementar sus segmentos eligiendo e importando sus cohortes en Kubit.
    tags:
      - Cohort membership
  - name: Mixpanel Cohorts
    description: Los clientes que utilizan Mixpanel pueden complementar sus segmentos eligiendo e importando sus cohortes en Mixpanel.
    tags:
      - Cohort membership
  - name: Segment Cohorts
    description: Los clientes que utilizan Segment pueden complementar sus segmentos eligiendo e importando sus cohortes en Segment.
    tags:
      - Cohort membership
  - name: Tinyclues Cohorts
    description: Los clientes que utilizan Tinyclues pueden complementar sus segmentos eligiendo e importando sus cohortes en Tinyclues.
    tags:
      - Cohort membership
  - name: Install Attribution Ad
    description: Segmenta a tus usuarios por el anuncio al que se atribuyó su instalación.
    tags:
      - User Attributes
  - name: Install Attribution Adgroup
    description: Segmenta a tus usuarios por el grupo de anuncios al que se atribuyó su instalación.
    tags:
      - Install attribution
  - name: Install Attribution Campaign
    description: Segmenta a tus usuarios por la campaña publicitaria a la que se atribuyó su instalación.
    tags:
      - Install attribution
  - name: Install Attribution Source
    description: Segmenta a tus usuarios por la fuente a la que se atribuyó su instalación.
    tags:
      - Install attribution
  - name: Churn Risk Category
    description: Segmenta a tus usuarios por categoría de riesgo de cancelación según una predicción específica.
    tags:
      - Intelligence and predictive
  - name: Churn Risk Score
    description: Segmenta a tus usuarios por puntuación de riesgo de cancelación según una predicción específica.
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Category
    description: Segmenta a tus usuarios por la probabilidad de realizar un evento según una predicción específica.
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Score
    description: Segmenta a tus usuarios por la puntuación de probabilidad de realizar un evento según una predicción específica.
    tags:
      - Intelligence and predictive
  - name: Intelligent Channel
    description: Segmenta a tus usuarios por su canal más activo en los últimos tres meses.
    tags:
      - Intelligence and predictive
  - name: Message Open Likelihood
    description: Filtra a tus usuarios en función de su <a href="/docs/user_guide/brazeai/intelligence_suite/intelligent_channel#individual-channels">probabilidad de abrir un mensaje en un canal especificado</a> en una escala de 0 a 100 %. Los usuarios sin datos suficientes para medir una probabilidad para un canal pueden seleccionarse usando "está en blanco".<br><br>Para correo electrónico, las aperturas automáticas se excluyen del cálculo de probabilidad.
    tags:
      - Intelligence and predictive
  - name: Number of Facebook Friends Using App
    description: Segmenta a tus usuarios por cuántos amigos de Facebook tienen que usan la misma aplicación.
    tags:
      - Social activity
  - name: Connected Facebook
    description: Segmenta a tus usuarios en función de si conectaron tu aplicación con Facebook.
    tags:
      - Social activity
  - name: Connected Twitter
    description: Segmenta a tus usuarios en función de si conectaron tu aplicación con X (anteriormente Twitter).
    tags:
      - Social activity
  - name: Number of Twitter Followers
    description: Segmenta a tus usuarios por cuántos seguidores de X (anteriormente Twitter) tienen.
    tags:
      - Social activity
  - name: Phone Number
    description: Segmenta a tus usuarios por el campo de número de teléfono en formato E.164.<br><br> Cuando se envía un número de teléfono a Braze, Braze intenta convertirlo al <a href="/docs/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#import-phone-numbers">formato E.164</a> que se utiliza para enviar a través de los canales SMS, RCS y WhatsApp. El proceso de conversión puede fallar si el número no tiene el formato adecuado, lo que resulta en que el perfil del usuario tenga un número de teléfono sin formato pero no un número de teléfono de envío. Este filtro de segmento devuelve usuarios por su número de teléfono en formato E.164 (cuando está disponible).<br><br>Ejemplos:<br> - Utiliza este filtro para comprender el tamaño más preciso de la audiencia objetivo al enviar mensajes SMS, RCS o WhatsApp.  <br>- Utiliza expresiones regulares (regex) con este filtro para segmentar por números de teléfono con un código de país específico. <br>- Utiliza este filtro para segmentar usuarios por números de teléfono que fallaron en el proceso de conversión a E.164.
    tags:
      - Other Filters
---