---
nav_title: Información general de Shopify
article_title: Información general de Shopify
description: "Este artículo de referencia describe la asociación entre Braze y Shopify, una empresa de comercio global que te permite conectar fácilmente tu tienda Shopify con Braze para pasar determinados webhooks de Shopify a Braze. Aprovecha las estrategias multicanal de Braze y Canvas para animar a los clientes a completar sus compras o reorientar a los usuarios en función de sus compras anteriores."
page_type: partner
search_tag: Partner
alias: /shopify_overview/
page_order: 0
---

# Información general de Shopify {#shopify-overview}

> [Shopify](https://www.shopify.com/) es una empresa líder en comercio global que proporciona herramientas de confianza para iniciar, hacer crecer, comercializar y administrar un negocio de cualquier tamaño. Shopify hace que el comercio sea mejor para todos con una plataforma y unos servicios diseñados para ser fiables y ofrecer una mejor experiencia de compra a los consumidores de todo el mundo.

La integración de Braze con Shopify proporciona una potente solución para las empresas de comercio electrónico que buscan mejorar la interacción con los clientes e impulsar esfuerzos de marketing personalizados. Esta integración conecta fácilmente las sólidas capacidades de comercio electrónico de Shopify con nuestra avanzada plataforma de interacción con los clientes, lo que te permite entregar mensajes específicos, relevantes y oportunos a tus usuarios, basados en comportamientos de compra en tiempo real y datos de transacciones.

## Requisitos {#requirements}

| Requisito | Descripción |
| --- | --- |
| Tienda Shopify | Tienes una tienda Shopify activa. |
| Permisos de propietario o miembro del personal de la tienda Shopify | {::nomarkdown}<ul><li>Acceso a toda la configuración General y de la Tienda en línea.</li><li> Permisos de administrador adicionales:<ul><li>Pedidos: Ver</li><li>Cliente: Lectura y escritura</li><li>Ver eventos de clientes (Web Pixels)</li><li>Administrar configuración</li><li>Ver aplicaciones desarrolladas por personal/colaboradores</li><li>Administrar/instalar aplicaciones y canales</li><li>Administrar/añadir píxeles personalizados</li></ul></li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Cómo integrar {#how-to-integrate}

Braze ofrece dos opciones de integración para comerciantes de Shopify que están diseñadas para satisfacer las diversas necesidades de los negocios de comercio electrónico: **Integración estándar** e **Integración personalizada**.

{% multi_lang_include partners/shopify.md section='Integration Tabs' %}

## Cómo funciona la integración {#how-the-integration-works}

Si ya configuraste y activaste el [relleno de datos históricos]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill) en tus ajustes de configuración, la sincronización inicial de datos comenzará de inmediato.

{% multi_lang_include partners/shopify.md section='Custom external ID historical backfill' %}

Después de la sincronización inicial de datos, Braze rastreará continuamente nuevos datos y actualizaciones, directamente desde Shopify y los SDK de Braze.

{% alert note %}
Si ya eres cliente de Braze con Campaigns o Canvas activos, revisa [Relleno de datos históricos de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill) para obtener información importante. Para ver qué datos específicos de clientes se están rellenando, consulta [Características de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features).
{% endalert %}

### Sincronización de usuarios y datos {#user-and-data-syncing}

Una vez que la integración está en vivo, Braze recopilará datos de usuario de dos fuentes clave a través de la integración con Shopify:
- **API de Shopify Web Pixel e inserciones de la aplicación:** Esto alimenta el SDK web de Braze y el SDK de Javascript para admitir el seguimiento en el sitio, la gestión de identidad, los datos de comportamiento de eCommerce y los canales de mensajería como los In-App Messages.
- **Webhooks de Shopify:** datos de comportamiento de eCommerce, sincronización de productos y recopilación de suscriptores

Durante la incorporación de la integración, deberás seleccionar cuándo los SDK de Braze se inicializan y cargan tu sitio de Shopify:
- Al visitar el sitio (como el inicio de sesión)
    - **Qué hace:** Rastrea usuarios anónimos, como compradores invitados, para acceder a más datos y lograr una personalización más profunda
- Al registrarse en la cuenta (como el inicio de sesión en la cuenta)
    - **Qué hace:** Evita el seguimiento de usuarios anónimos para un enfoque más conservador y orientado a la privacidad, de modo que la actividad del usuario se rastrea *después* de que el usuario inicia sesión en su cuenta

{% alert note %}
- Las visitas al sitio web (sesiones) cuentan para tus asignaciones de MAU (MAU).
- Las versiones del SDK web de Braze y del SDK de JavaScript se configuran automáticamente en v6.8.0. Puedes actualizar la versión de tu SDK en cualquier momento desde la configuración de la integración.
{% endalert %}

Braze utiliza la integración con Shopify para admitir múltiples identificadores que rastrean a tus usuarios desde su experiencia de compra como invitados hasta que se convierten en usuarios identificados:

| Identificador de Braze | Descripción |
| --- | --- |
| `device_id` de Braze | Un ID generado aleatoriamente almacenado en el navegador que rastrea la actividad de usuarios anónimos a través de los SDK de Braze. |
| Alias de usuario de token de carrito | Un alias que Braze crea para rastrear eventos de actualización de carrito. Este token se crea utilizando el token de carrito de Shopify. |
| Alias de usuario de token de checkout | Un alias que Braze crea cuando el usuario inicia el proceso de checkout. Este token se crea utilizando el token de checkout de Shopify.<br><br> Si un cliente utiliza Shop Pay como opción de checkout acelerado, Shopify puede omitir ciertos eventos estándar de checkout e impedir que Braze reciba los datos necesarios para agregar el alias del token de checkout. |
| Alias de ID de cliente de Shopify | El ID de cliente de Shopify se asigna como alias cuando el ID externo se asigna durante el inicio de sesión en la cuenta o cuando se realiza un pedido. |
| `external_id` de Braze | Un identificador único que ayuda a rastrear clientes a través de dispositivos y plataformas. Esto mantiene una experiencia de usuario consistente y mejora los análisis al prevenir múltiples perfiles cuando los usuarios cambian de dispositivo o reinstalan la aplicación.<br><br>La integración con Shopify admite los siguientes tipos de `external_id`: <br><br>{::nomarkdown}<ul><li>ID de cliente de Shopify (predeterminado)</li><li>ID externo personalizado</li><li>Correo electrónico con hash (SHA-256)</li><li>Correo electrónico con hash (SHA-1)</li><li>Correo electrónico con hash (MD5)</li><li>Correo electrónico</li></ul>{:/}Braze asigna un `external_id` a tus usuarios llamando al método changeUser dentro de los SDK cuando: <br><br>{::nomarkdown}<ul><li>Un usuario inicia sesión o crea una cuenta</li><li>Se realiza un pedido</li></ul>{:/}<br> Para obtener más información sobre lo que sucede cuando asignas un `external_id` a un perfil anónimo, consulta [Ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users).<br><br>Braze también aprovechará el `external_id` para atribuir datos de comportamiento de eCommerce posteriores provenientes de los webhooks de Shopify.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sincronización de usuarios y datos" }

La integración requiere que los SDK de Braze y los servicios de Shopify trabajen juntos para rastrear y atribuir adecuadamente los datos de Shopify a los usuarios correctos en tiempo casi real. Para encontrar más detalles sobre los datos rastreados a través de la integración, consulta [Datos de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features).

{% alert note %}
- Si estás probando la integración, te aconsejamos usar el modo incógnito o borrar tus cookies para restablecer el `device_id` de Braze y simular el comportamiento de un usuario anónimo.
- Aunque se genera un ID de cliente de Shopify cuando se ingresa un correo electrónico en el pie de página del boletín de Shopify o durante el proceso de checkout antes de realizar un pedido, ese ID de cliente no es accesible a través de Shopify Web Pixels. Debido a esto, Braze no puede usar el método `changeUser` en estas dos situaciones.
{% endalert %}

### Sincronización de las adhesiones voluntarias de marketing por correo electrónico y SMS de Shopify {#syncing-shopify-email-and-sms-marketing-opt-ins}

Si habilitas la recopilación de suscriptores en tus ajustes de configuración, debes asignar un grupo de suscripción para cada tienda que conectes a Braze. Esto significa que tus clientes serán categorizados como "suscritos" o "cancelaron su suscripción" en el grupo de suscripción de tu tienda.

El estado de adhesión voluntaria de marketing de Shopify para correo electrónico y marketing por SMS se puede actualizar de las siguientes maneras:
- **Actualización manual:** Puedes cambiar manualmente el estado de adhesión voluntaria de marketing por correo electrónico o SMS de un usuario en tu administrador de Shopify.
- **Pie de página del boletín de Shopify:** Si un usuario ingresa su correo electrónico en el pie de página predeterminado del boletín de Shopify, se actualiza su estado de adhesión voluntaria.
- **Checkout:** El consentimiento del usuario se captura en el checkout cuando los usuarios seleccionan la casilla de verificación de marketing y proceden con el checkout seleccionando **Pay now** en el checkout de una página o **Continue to shipping** en el checkout de tres páginas.

{% alert note %}
El estado de adhesión voluntaria de marketing por correo electrónico de Shopify no cambiará el [estado de suscripción global de correo electrónico]({{site.baseurl}}/user_guide/channels/email/subscriptions) de un usuario en Braze. El estado de suscripción predeterminado cuando se crea un perfil de usuario es "suscrito". Recuerda usar el grupo de suscripción como parte de los criterios de entrada de tu Campaign o Canvas.
{% endalert %}

Esta tabla muestra qué estados de adhesión voluntaria de marketing de Shopify se correlacionan con los estados dentro de tu grupo de suscripción de Braze.

| Estado de adhesión voluntaria de marketing de Shopify | Estado del grupo de suscripción de Braze |
| --- | --- |
| Correo electrónico suscrito | Suscrito |
| Correo electrónico canceló suscripción | Canceló suscripción |
| Correo electrónico pendiente de confirmación | Canceló suscripción |
| Correo electrónico no válido | Canceló suscripción |
| SMS suscrito | Suscrito |
| SMS canceló suscripción | Canceló suscripción |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sincronización de las adhesiones voluntarias de marketing por correo electrónico y SMS de Shopify" }

### Formularios de registro {#sign-up-forms}

#### Pie de página del boletín de Shopify {#shopify-newsletter-footer}

Los usuarios que ingresen su dirección de correo electrónico en el pie de página del boletín de Shopify experimentarán uno de estos flujos de trabajo:

##### Usuarios que no han iniciado sesión en su cuenta {#users-who-havent-logged-into-their-account}

1. Braze recibe un webhook entrante de Shopify cada vez que se crea o actualiza un cliente.
2. Braze crea un perfil de usuario que contiene la dirección de correo electrónico y el alias de ID de cliente de Shopify asociados con ese usuario.
3. El SDK de Braze actualiza el perfil anónimo con la dirección de correo electrónico.

{% alert note %}
Esto podría resultar en un perfil duplicado hasta que el usuario se identifique creando su cuenta, iniciando sesión en su cuenta o realizando un pedido. Braze ofrece herramientas de fusión masiva para ayudarte a automatizar la conciliación de perfiles duplicados. Consulta [Usuarios duplicados]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users) para más detalles.
{% endalert %}

##### Usuarios que ya han iniciado sesión en su cuenta {#users-who-have-already-logged-into-their-account}

Braze creará un perfil de usuario que contiene la dirección de correo electrónico y el alias de ID de cliente de Shopify asociados con ese usuario. Braze no actualizará la dirección de correo electrónico del usuario que ha iniciado sesión, ya que asumimos que Shopify ya proporcionó esta información.

#### Formularios de registro de Braze {#braze-sign-up-forms}

Braze proporciona dos tipos de plantillas de formularios de registro:
- **[Formularios de registro por correo electrónico]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/email_capture):** Crea estos usando el editor de arrastrar y soltar.
- **[Formulario de captura de correo electrónico del editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/email_capture_form):** Un formulario más sencillo para capturar direcciones de correo electrónico.

Cuando usas estas plantillas de formularios de registro, Braze actualiza automáticamente el estado de suscripción global de correo electrónico en el perfil de usuario. Para obtener más detalles sobre cómo se gestiona el estado de suscripción global de correo electrónico, incluida información sobre la validación de correo electrónico, consulta la documentación de cada tipo de plantilla de formulario.

{% alert note %}
- Asegúrate de incluir criterios de entrada en tu Campaign o Canvas que incluyan tanto el estado de suscripción global de correo electrónico como el grupo de suscripción que están conectados a tu tienda Shopify. Esto te ayudará a garantizar que estés segmentando a la audiencia correcta.
- Braze recopila información de los visitantes, como direcciones de correo electrónico y números de teléfono, a través de mensajes en el explorador. Esta información se envía luego a la API de visitantes de Shopify, pero no crea un perfil de cliente en Shopify. Para más detalles, consulta [Visitor API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

#### Formularios de registro de terceros {#third-party-sign-up-forms}

Si estás utilizando una plataforma de terceros o un plugin de Shopify para tus formularios de registro, debes trabajar con tus desarrolladores para integrar el código del SDK de Braze a fin de capturar la dirección de correo electrónico y el estado de suscripción global de correo electrónico de los envíos de formularios. Para obtener más información, revisa [Configuración de la integración estándar de Shopify]({{site.baseurl}}/shopify_standard_integration) y [Configuración de la integración personalizada de Shopify]({{site.baseurl}}/shopify_custom_integration).

### Sincronización de productos {#product-syncing}

Braze admite la capacidad de sincronizar los productos de tu tienda Shopify en un catálogo de Braze. Para más detalles, consulta [Sincronización de productos de Shopify]({{site.baseurl}}/shopify_catalogs).

## Solicitudes de los interesados {#data-subject-requests}

Como parte de la integración de Shopify en la plataforma Braze, Braze recibe automáticamente los [webhooks de cumplimiento de Shopify](https://shopify.dev/docs/apps/build/privacy-law-compliance/). Sin embargo, dado que los clientes son los responsables del tratamiento de los datos de sus usuarios finales, los clientes deben llevar a cabo cualquier acción necesaria para atender las solicitudes de los interesados recibidas con respecto a los datos de los usuarios finales en Braze (incluidos los datos de los usuarios finales recibidos a través de la integración de Shopify). Consulta nuestra documentación de [Asistencia técnica en protección de datos]({{site.baseurl}}/dp-technical-assistance) para más información.