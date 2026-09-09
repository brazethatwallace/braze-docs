---
nav_title: Tu audiencia
article_title: Tu audiencia en Braze
page_order: 0
page_type: reference
description: "Descubre cómo Braze define y gestiona a tus usuarios, los identifica y aprovecha los datos de usuario para potenciar la segmentación, la personalización y la mensajería en todos los canales."

---

# Tu audiencia en Braze {#your-braze-audience}

> Descubre cómo Braze define y gestiona a tus usuarios, los identifica y aprovecha los datos de usuario para potenciar la segmentación, la personalización y la mensajería en todos los canales.

En Braze, un usuario (y su perfil de usuario) representa a una persona individual a la que puedes enviar mensajes y analizar.

## Perfiles de usuario {#user-profiles}

Un [perfil de usuario]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) actúa como la única fuente de verdad de todo lo que Braze sabe sobre esa persona, incluyendo:

- Identificadores (como ID de usuario o ID externos)
- Dispositivos y canales de mensajería
- Datos de comportamiento y eventos
- Atributos y preferencias
- Historial de participación en mensajes

Un solo perfil de usuario puede estar asociado con múltiples dispositivos y canales, lo que te permite comprender y enviar mensajes a alguien de forma integral en todas las plataformas.

## Usuarios anónimos y usuarios identificados {#anonymous-users-and-identified-users}

Los usuarios en Braze generalmente se encuentran en uno de dos estados.

### Usuarios anónimos {#anonymous-users}

Un [usuario anónimo]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users) es alguien que ha interactuado con tu aplicación o sitio web, pero que aún no se le ha asignado un identificador de tu sistema (como un `external_id`).

- Los usuarios anónimos se crean automáticamente cuando se inicializa el SDK de Braze
- Aún puedes hacer seguimiento de eventos, atributos y participación en mensajes
- Estos usuarios pueden recibir mensajes, dependiendo del canal y del estado de adhesión voluntaria

#### Usuarios anónimos y consentimiento {#anonymous-users-and-consent}

Si necesitas envolver el SDK de Braze en un envoltorio de consentimiento para cumplir con tus políticas de consentimiento, puedes recopilar datos anónimos antes de que los usuarios otorguen su consentimiento. Cuando el SDK se inicializa, se crea un perfil de usuario anónimo, lo que te permite hacer seguimiento del comportamiento mientras se respetan los requisitos de consentimiento.

**Envío de mensajes a usuarios anónimos:**
Los usuarios anónimos pueden desencadenar y recibir mensajes siempre que el SDK de Braze permanezca inicializado. Esto incluye:

- [Mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages)
- [Notificaciones push]({{site.baseurl}}/user_guide/channels/push) (si los tokens de notificaciones push están registrados)
- [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)

Sin embargo, si deshabilitas o impides la inicialización del SDK cuando un usuario no otorga su consentimiento o lo retira, los canales activados por el SDK no funcionan para ese usuario.

**Segmentación de usuarios según el estado de consentimiento:**
Para enviar mensajes a los usuarios según su estado de consentimiento, establece un atributo de usuario personalizado (como `has_marketing_consent`) en su perfil. Luego puedes crear Segments basados en este atributo y mantener este valor sincronizado si los usuarios cambian sus preferencias de consentimiento fuera de Braze. Para más información sobre la segmentación de usuarios anónimos, consulta [Ejemplos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users#use-cases).

### Usuarios identificados {#identified-users}

Un [usuario identificado]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#identified-user-profiles) es aquel que ha sido asociado con un `external_id` que tú proporcionas (por ejemplo, un ID de cliente o un ID de cuenta).

Identificar a un usuario te permite:

- Fusionar la actividad entre dispositivos y sesiones
- Enviar mensajes de manera consistente a través de los canales
- Segmentar y personalizar usando datos de usuario a largo plazo
- Administrar perfiles a través de API e integraciones

Cuando un usuario anónimo es identificado posteriormente, Braze fusiona los datos elegibles en el perfil identificado de acuerdo con [este comportamiento de fusión]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior). Por ejemplo, los tokens de notificaciones push y el historial de mensajes se transfieren, y muchos campos del perfil anónimo se fusionan solo cuando no están ya establecidos en el perfil identificado; cuando los valores entran en conflicto, se conserva el perfil identificado.

## Envía mensajes a los usuarios a través de canales {#message-users-through-channels}

Un [canal]({{site.baseurl}}/user_guide/channels) es una forma específica en la que Braze puede entregar un mensaje a un usuario. Los canales más comunes incluyen:

- [Push (web o móvil)]({{site.baseurl}}/user_guide/channels/push)
- [Correo electrónico]({{site.baseurl}}/user_guide/channels/email)
- [SMS, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)
- [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp)
- [Mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages)
- [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)
- [Banners]({{site.baseurl}}/user_guide/channels/banners)
- [LINE]({{site.baseurl}}/user_guide/channels/line)
- [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks)

Un perfil de usuario individual puede tener múltiples canales asociados, como una dirección de correo electrónico y un dispositivo móvil. Braze utiliza este modelo para coordinar la mensajería entre canales manteniendo una vista unificada del usuario.

Cada canal tiene sus propias reglas de entrega, requisitos de adhesión voluntaria y metadatos, pero todos están asociados al mismo perfil de usuario.

## Formas en las que los usuarios entran en Braze {#ways-users-enter-braze}

Los usuarios se crean en Braze cada vez que alguien interactúa con tu marca a través de una integración o canal compatible. La forma en que se añaden depende de cómo hayas implementado Braze.

{% tabs %}
{% tab Aplicaciones móviles %}
- Cuando un usuario abre tu aplicación por primera vez, el SDK de Braze crea un perfil de usuario.
- Los dispositivos y los tokens de notificaciones push se registran automáticamente.
- Los eventos y atributos se pueden registrar de inmediato.
{% endtab %}

{% tab Web %}
- Los usuarios se crean cuando el SDK Web se inicializa.
- Las suscripciones de notificaciones push web registran un navegador como canal de mensajería.
{% endtab %}

{% tab Correo electrónico y SMS %}
- Los usuarios se pueden crear al cargar datos, llamar a las API o recopilar adhesiones voluntarias.
- Las direcciones de correo electrónico y los números de teléfono se almacenan como identificadores de canal.
- El estado de adhesión voluntaria se rastrea por canal y por región.
{% endtab %}

{% tab API e integraciones %}
- Puedes crear o actualizar usuarios directamente a través de las [REST API]({{site.baseurl}}/api/endpoints/user_data) o [importando un CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import).
- Las herramientas externas (como CDP, CRM o almacenes de datos) pueden sincronizar usuarios en Braze automáticamente.
{% endtab %}
{% endtabs %}

## Orígenes de datos de audiencia {#audience-data-sources}

Los datos de usuario en Braze suelen proceder de una combinación de orígenes.

{% tabs %}
{% tab Recopilación automática %}
Los SDK de Braze recopilan automáticamente datos contextuales como:

- Tipo de dispositivo y sistema operativo
- Idioma y zona horaria
- Versión de la aplicación y actividad de sesión
{% endtab %}

{% tab Comportamiento del usuario %}
Cuando los usuarios interactúan con tu aplicación o mensajes, Braze registra:

- [Eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) (por ejemplo, compras o uso de características)
- Aperturas de mensajes, clics y conversiones
- Actividad de sesión y tendencias de participación
{% endtab %}

{% tab Tus sistemas %}
Puedes enviar datos desde tus propias herramientas a Braze usando:

- [REST API]({{site.baseurl}}/api/endpoints/user_data)
- [Cargas de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)
- Sincronizaciones de datos programadas

Esto suele incluir identificadores, datos de cuenta o contexto histórico.
{% endtab %}
{% endtabs %}

### Datos proporcionados por el usuario {#user-provided-input}

Los usuarios pueden proporcionar datos directamente a través de:

- [Centros de preferencias]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)
- Formularios o cuestionarios (SDK o integraciones)
- Experiencias dentro de la aplicación

### Integraciones {#integrations}

Braze se integra con plataformas como [Segment]({{site.baseurl}}/partners/segment), almacenes de datos y partners de tecnología de análisis a través de integraciones, lo que permite que los datos de usuario fluyan automáticamente a los perfiles de usuario.

## Gestiona los datos de usuario {#manage-user-data}

Puedes añadir, actualizar o eliminar datos de usuario de varias formas:

- **Herramientas del panel** para ediciones manuales o cargas de CSV
- **API** para actualizaciones en tiempo real o programáticas
- **SDK** para capturar el comportamiento directamente en tu aplicación o sitio web
- **Integraciones** para sincronización continua

Los datos se pueden eliminar mediante:

- Borrado de valores de atributos
- Eliminación de etiquetas
- Actualización de estados de suscripción
- Restablecimiento de usuarios al cerrar sesión (para ejemplos de usuarios anónimos)

## Características de los datos de audiencia {#audience-data-features}

Una vez que los datos de usuario están en Braze, potencian prácticamente todas las capacidades de participación. Cuanto más completos y precisos sean tus datos de usuario, más eficazmente podrás utilizar las siguientes características.

| Característica | Descripción |
| ---- | ---- |
| [Segmentación]({{site.baseurl}}/user_guide/audience/segments) | Crea audiencias basadas en: {::nomarkdown}<ul><li>Atributos y campos personalizados</li> <li>Eventos y comportamientos</li> <li>Participación con mensajes</li> <li>Propiedades de dispositivo y canal</li></ul>{:/} <br>Los Segments se pueden reutilizar en Campaigns y Canvas. |
| [Personalización]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) | Utiliza los datos de usuario para adaptar el contenido, como: {::nomarkdown}<ul><li>Nombres y preferencias en el texto de los mensajes</li> <li>Recomendaciones dinámicas</li> <li>Contenido específico por ubicación o idioma</li></ul>{:/} |
| Automatización y orquestación  | Desencadena mensajes y recorridos basándote en: {::nomarkdown}<ul><li>Acciones del usuario</li> <li>Cambios de atributos</li> <li>Condiciones basadas en el tiempo</li></ul>{:/} |
| Coordinación multicanal | Llega a los usuarios en el canal más apropiado respetando: {::nomarkdown}<ul><li>Estado de adhesión voluntaria</li> <li>Límites de frecuencia</li> <li>Preferencias de canal</li></ul>{:/} |
| [Análisis e información]({{site.baseurl}}/user_guide/analytics) | Comprende cómo se comportan las distintas audiencias analizando: {::nomarkdown}<ul><li>Tasas de participación</li> <li>Rutas de conversión</li> <li>Rendimiento de los Segments a lo largo del tiempo</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Características de los datos de audiencia" }