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

Un [perfil de usuario]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/) actúa como una fuente única de verdad para todo lo que Braze sabe sobre esa persona, incluyendo:

- Identificadores (como ID de usuario o ID externos)
- Dispositivos y canales de mensajería
- Datos de comportamiento y eventos
- Atributos y preferencias
- Historial de interacción con mensajes

Un único perfil de usuario puede estar asociado a múltiples dispositivos y canales, lo que te permite comprender y enviar mensajes a alguien de forma integral en todas las plataformas.

## Usuarios anónimos y usuarios identificados {#anonymous-users-and-identified-users}

Los usuarios en Braze generalmente se encuentran en uno de dos estados.

### Usuarios anónimos {#anonymous-users}

Un [usuario anónimo]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users/) es alguien que ha interactuado con tu aplicación o sitio web pero aún no se le ha asignado un identificador de tu sistema (como un `external_id`).

- Los usuarios anónimos se crean automáticamente cuando el SDK de Braze se inicializa
- Aún puedes rastrear eventos, atributos e interacción con mensajes
- Estos usuarios pueden recibir mensajes, dependiendo del canal y el estado de adhesión voluntaria

### Usuarios identificados {#identified-users}

Un [usuario identificado]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#identified-user-profiles) es aquel que ha sido asociado con un `external_id` que tú proporcionas (por ejemplo, un ID de cliente o un ID de cuenta).

Identificar a un usuario te permite:

- Fusionar la actividad entre dispositivos y sesiones
- Enviar mensajes de forma consistente en todos los canales
- Segmentar y personalizar usando datos de usuario a largo plazo
- Gestionar perfiles a través de API e integraciones

Cuando un usuario anónimo es identificado posteriormente, Braze fusiona los datos elegibles en el perfil identificado de acuerdo con [este comportamiento de fusión]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior). Por ejemplo, los tokens de notificaciones push y el historial de mensajes se transfieren, y muchos campos del perfil anónimo se fusionan solo cuando no están ya establecidos en el perfil identificado; cuando los valores entran en conflicto, se conserva el perfil identificado.

## Enviar mensajes a los usuarios a través de canales {#message-users-through-channels}

Un [canal]({{site.baseurl}}/user_guide/channels/) es una forma específica en la que Braze puede entregar un mensaje a un usuario. Los canales más comunes incluyen:

- [Push (web o móvil)]({{site.baseurl}}/user_guide/channels/push/)
- [Correo electrónico]({{site.baseurl}}/user_guide/channels/email/)
- [SMS, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/)
- [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/)
- [Mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/)
- [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/)
- [Banners]({{site.baseurl}}/user_guide/channels/banners/)
- [LINE]({{site.baseurl}}/user_guide/channels/line/)
- [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks/)

Un único perfil de usuario puede tener múltiples canales asociados, como una dirección de correo electrónico y un dispositivo móvil. Braze utiliza este modelo para coordinar la mensajería en todos los canales manteniendo una vista unificada del usuario.

Cada canal tiene sus propias reglas de entrega, requisitos de adhesión voluntaria y metadatos, pero todos están asociados al mismo perfil de usuario.

## Formas en que los usuarios entran en Braze {#ways-users-enter-braze}

Los usuarios se crean en Braze cada vez que alguien interactúa con tu marca a través de una integración o canal compatible. La forma en que se añaden depende de cómo hayas implementado Braze.

{% tabs %}
{% tab Aplicaciones móviles %}
- Cuando un usuario abre tu aplicación por primera vez, el SDK de Braze crea un perfil de usuario.
- Los dispositivos y los tokens de notificaciones push se registran automáticamente.
- Los eventos y atributos se pueden registrar de inmediato.
{% endtab %}

{% tab Web %}
- Los usuarios se crean cuando el SDK web se inicializa.
- Las suscripciones a notificaciones push web registran un navegador como canal de mensajería.
{% endtab %}

{% tab Correo electrónico y SMS %}
- Los usuarios se pueden crear cuando cargas datos, llamas a API o recopilas adhesiones voluntarias.
- Las direcciones de correo electrónico y los números de teléfono se almacenan como identificadores de canal.
- El estado de adhesión voluntaria se rastrea por canal y por región.
{% endtab %}

{% tab API e integraciones %}
- Puedes crear o actualizar usuarios directamente a través de [REST API]({{site.baseurl}}/api/endpoints/user_data/) o [importando un CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/).
- Las herramientas externas (como CDP, CRM o almacenes de datos) pueden sincronizar usuarios en Braze automáticamente.
{% endtab %}
{% endtabs %}

## Fuentes de datos de audiencia {#audience-data-sources}

Los datos de usuario en Braze generalmente provienen de una combinación de fuentes.

{% tabs %}
{% tab Recopilación automática %}
Los SDK de Braze recopilan automáticamente datos contextuales como:

- Tipo de dispositivo y sistema operativo
- Idioma y zona horaria
- Versión de la aplicación y actividad de sesión
{% endtab %}

{% tab Comportamiento del usuario %}
Cuando los usuarios interactúan con tu aplicación o mensajes, Braze registra:

- [Eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) (por ejemplo, compras o uso de características)
- Aperturas de mensajes, clics y conversiones
- Actividad de sesión y tendencias de interacción
{% endtab %}

{% tab Tus sistemas %}
Puedes enviar datos desde tus propias herramientas a Braze usando:

- [REST API]({{site.baseurl}}/api/endpoints/user_data/)
- [Cargas de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/)
- Sincronizaciones de datos programadas

Esto a menudo incluye identificadores, datos de cuenta o contexto histórico.
{% endtab %}
{% endtabs %}

### Datos proporcionados por el usuario {#user-provided-input}

Los usuarios pueden proporcionar datos directamente a través de:

- [Centros de preferencias]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/)
- Formularios o cuestionarios (SDK o integraciones)
- Experiencias dentro de la aplicación

### Integraciones {#integrations}

Braze se integra con plataformas como [Segment]({{site.baseurl}}/partners/segment/), almacenes de datos y socios tecnológicos de análisis a través de integraciones, lo que permite que los datos de usuario fluyan automáticamente hacia los perfiles de usuario.

## Gestionar datos de usuario {#manage-user-data}

Puedes añadir, actualizar o eliminar datos de usuario de varias formas:

- **Herramientas del dashboard** para ediciones manuales o cargas de CSV
- **API** para actualizaciones en tiempo real o programáticas
- **SDK** para capturar comportamiento directamente en tu aplicación o sitio web
- **Integraciones** para sincronización continua

Los datos se pueden eliminar mediante:

- Borrar valores de atributos
- Eliminar etiquetas
- Actualizar estados de suscripción
- Restablecer usuarios al cerrar sesión (para casos de uso anónimos)

## Características de datos de audiencia {#audience-data-features}

Una vez que los datos de usuario están en Braze, potencian prácticamente todas las capacidades de interacción. Cuanto más completos y precisos sean tus datos de usuario, más eficazmente podrás utilizar las siguientes características.

| Característica | Descripción |
| ---- | ---- |
| [Segmentación]({{site.baseurl}}/user_guide/audience/segments/) | Crea audiencias basadas en: {::nomarkdown}<ul><li>Atributos y campos personalizados</li> <li>Eventos y comportamientos</li> <li>Interacción con mensajes</li> <li>Propiedades de dispositivo y canal</li></ul>{:/} <br>Los segmentos se pueden reutilizar en Campaigns y Canvas. |
| [Personalización]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/) | Usa datos de usuario para adaptar el contenido, como: {::nomarkdown}<ul><li>Nombres y preferencias en el texto del mensaje</li> <li>Recomendaciones dinámicas</li> <li>Contenido específico por ubicación o idioma</li></ul>{:/} |
| Automatización y orquestación  | Desencadena mensajes y recorridos basados en: {::nomarkdown}<ul><li>Acciones del usuario</li> <li>Cambios de atributos</li> <li>Condiciones basadas en el tiempo</li></ul>{:/} |
| Coordinación entre canales | Llega a los usuarios en el canal más apropiado respetando: {::nomarkdown}<ul><li>Estado de adhesión voluntaria</li> <li>Límites de frecuencia</li> <li>Preferencias de canal</li></ul>{:/} |
| [Análisis e información]({{site.baseurl}}/user_guide/analytics/) | Comprende cómo se comportan las diferentes audiencias analizando: {::nomarkdown}<ul><li>Tasas de interacción</li> <li>Rutas de conversión</li> <li>Rendimiento de segmentos a lo largo del tiempo</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Características de datos de audiencia" }