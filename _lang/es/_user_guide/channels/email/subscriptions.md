---
nav_title: "Suscripciones"
article_title: "Suscripciones"
page_order: 5
description: "Este artículo de referencia cubre los diferentes estados de suscripción de los usuarios, cómo crear y administrar grupos de suscripción, y cómo segmentar usuarios en función de sus suscripciones."
channel:
  - email

---

# Suscripciones de correo electrónico {#email-subscriptions}

> Aprende sobre los estados de suscripción de los usuarios, cómo crear y administrar grupos de suscripción, y cómo segmentar usuarios en función de sus suscripciones.

Este documento es solo para fines informativos. No pretende proporcionar, ni se puede confiar en él como fuente de asesoramiento legal en ningún sentido. El envío de correos electrónicos de marketing y transaccionales puede estar sujeto a requisitos legales específicos. Para asegurarte de que lo haces en cumplimiento con todas las leyes, normas y regulaciones aplicables específicas de tu empresa, debes buscar el asesoramiento de tu equipo legal y/o de cumplimiento normativo.

## Estados de suscripción {#subscription-states}

Braze tiene tres estados de suscripción globales para los usuarios de correo electrónico. Estos estados controlan el envío de mensajes a los usuarios. Por ejemplo, los usuarios en el estado `unsubscribed` no reciben mensajes dirigidos a `subscribed` u `opted-in`.

| Estado | Definición |
| ----- | ---------- |
| Adhesión voluntaria | Un usuario ha confirmado explícitamente que desea recibir correo electrónico. Recomendamos un proceso de adhesión voluntaria explícito para obtener el consentimiento de los usuarios para enviar correos electrónicos. |
| Suscrito | Un usuario no ha cancelado su suscripción ni ha optado explícitamente por recibir correos electrónicos. Este es el estado de suscripción predeterminado cuando se crea un perfil de usuario. |
| Canceló suscripción | Un usuario ha cancelado explícitamente la suscripción a tus correos electrónicos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de suscripción" }

{% alert note %}
Braze no cuenta los cambios de estado de suscripción como puntos de datos, ni a nivel global ni en los grupos de suscripción.
{% endalert %}

### Direcciones de correo electrónico con suscripción cancelada {#unsubscribed-email-addresses}

Braze cancela automáticamente la suscripción de cualquier usuario que la cancele manualmente a través de un [pie de página personalizado]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer/). Si el usuario actualiza su dirección de correo electrónico y **Volver a suscribir a los usuarios cuando actualicen su correo electrónico** está habilitado en **Enviando configuración**, se reanuda el envío normal.

Si un usuario marca uno o más de tus correos electrónicos como correo no deseado, Braze solo envía correos electrónicos transaccionales a ese usuario. Los correos electrónicos transaccionales se refieren a la opción **Enviar a todos los usuarios, incluidos los que cancelaron su suscripción** en **Público objetivo**.

{% alert tip %}
Consulta nuestras mejores prácticas de [calentamiento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/) para obtener orientación sobre cómo volver a interactuar con tus usuarios de manera efectiva.
{% endalert %}

### Rebotes y correos electrónicos no válidos {#bounces-and-invalid-emails}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} {% multi_lang_include analytics/metrics.md metric='Soft Bounce' %}

Cuando una dirección de correo electrónico tiene un rebote duro, Braze no cambia automáticamente el estado de suscripción del usuario a "canceló suscripción". Si una dirección tiene un rebote duro (no es válida o no existe), Braze la marca como no válida y no intenta más envíos. Si el usuario cambia su dirección de correo electrónico, Braze reanuda el envío. Braze reintenta los rebotes blandos durante 72 horas.

### Actualización de los estados de suscripción de correo electrónico {#updating-email-subscription-states}

Hay cuatro formas de actualizar el estado de suscripción de correo electrónico de un usuario:

#### Integración de SDK {#sdk-integration}

Usa el SDK de Braze para actualizar el estado de suscripción de un usuario.

#### REST API

Usa el [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para actualizar el [atributo `email_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens) de un usuario. Por ejemplo, para establecer el estado de suscripción de correo electrónico de un usuario como cancelado cuando utiliza un enlace de cancelación de suscripción personalizado, incluye `email_subscribe: "unsubscribed"` en los atributos de usuario de tu solicitud.

#### Perfil de usuario {#user-profile}

1. Busca al usuario a través de **Buscar usuarios**.
2. En **Interacción**, selecciona **Canceló suscripción**, **Suscrito** o **Adhesión voluntaria** para cambiar el estado de suscripción del usuario.

El perfil de usuario también muestra una marca de tiempo de cuándo se cambió por última vez la suscripción del usuario. Se registra una marca de tiempo cuando el estado es **Adhesión voluntaria** o **Canceló suscripción**, pero no cuando el estado es **Suscrito**; por ejemplo, un perfil recién creado que nunca ha optado explícitamente por recibir o dejar de recibir no tiene marca de tiempo de suscripción.

#### Centro de preferencias {#preference-center}

Incluye Liquid del [centro de preferencias](#email-preference-center) en la parte inferior de tus correos electrónicos para permitir que los usuarios opten por recibir o dejar de recibir mensajes. Braze administra las actualizaciones del estado de suscripción desde el centro de preferencias.

### Verificación del estado de suscripción de correo electrónico {#checking-email-subscription-state}

![Perfil de usuario de John Doe con su estado de suscripción de correo electrónico establecido en Suscrito.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Usa cualquiera de los siguientes métodos para verificar el estado de suscripción de correo electrónico de un usuario:

1. **Exportación de REST API:** Usa los puntos de conexión [Exportar usuarios por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) o [Exportar usuarios por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para exportar perfiles de usuario individuales en formato JSON.
2. **Perfil de usuario:** Busca el perfil del usuario en la página [Buscar usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/), luego selecciona la pestaña **Interacción** para ver y actualizar manualmente el estado de suscripción de un usuario.

Cuando un usuario actualiza su dirección de correo electrónico, su estado de suscripción se establece como suscrito. Si la dirección de correo electrónico actualizada ya existe en otro lugar dentro de un espacio de trabajo de Braze, el usuario hereda el estado de suscripción de ese usuario existente, a menos que **Volver a suscribir a los usuarios cuando actualicen su configuración de correo electrónico** esté activado en **Enviando configuración**.

Para solucionar problemas con los cambios de estado de suscripción, revisa **Cambios en el estado de suscripción de correo electrónico** en los registros del perfil de usuario para ver el historial y la fuente. Las siguientes fuentes pueden desencadenar un cambio en el estado de suscripción de correo electrónico:

| Fuente | Descripción |
| ------ | ----------- |
| SDK | Actualización de atributo de usuario enviada a través de un SDK de Braze |
| REST API | Actualización de atributo de usuario enviada a través del punto de conexión [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) |
| Dashboard | Estado de suscripción cambiado manualmente en la página del perfil de usuario |
| Importación CSV | Estado de suscripción establecido durante una importación CSV de usuarios |
| Centro de preferencias | El usuario actualizó su preferencia desde un centro de preferencias alojado en Braze |
| Página de suscripción | El usuario seleccionó un enlace de cancelación de suscripción en un correo electrónico y llegó a la página de suscripción de Braze |
| List-Unsubscribe | El usuario canceló la suscripción a través del encabezado nativo list-unsubscribe del cliente de correo electrónico |
| Paso de actualización de usuario en Canvas | Estado de suscripción actualizado por un [paso de actualización de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) en un Canvas |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fuentes de actualización del estado de suscripción de correo electrónico" }

Cuando el estado de suscripción global de correo electrónico de un usuario cambia, Braze propaga ese estado a otros perfiles que comparten la misma dirección de correo electrónico, hasta 100 perfiles por cambio. Braze no garantiza la propagación cuando más de 100 perfiles comparten la misma dirección de correo electrónico. Si los usuarios que comparten un correo electrónico muestran diferentes estados de suscripción, ponte en contacto con soporte de Braze.

## Grupos de suscripción {#subscription-groups}

Los grupos de suscripción son filtros de segmento que pueden reducir aún más tu audiencia a partir de los [estados de suscripción globales](#subscription-states). Estos grupos te permiten presentar opciones de suscripción más detalladas a los usuarios finales.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

Por ejemplo, supongamos que envías múltiples categorías de Campaigns de correo electrónico (promocionales, boletines informativos o actualizaciones de producto). En ese caso, puedes usar grupos de suscripción para permitir que tus clientes elijan de qué categorías de correo electrónico desean suscribirse o cancelar la suscripción de forma masiva desde una sola página, usando un [centro de preferencias de correo electrónico](#email-preference-center). Alternativamente, podrías usar grupos de suscripción para permitir que tus clientes elijan con qué frecuencia desean recibir correos electrónicos, creando grupos de suscripción para correos electrónicos diarios, semanales o mensuales.

Usa los [puntos de conexión de grupos de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups/) para administrar programáticamente los grupos de suscripción que has almacenado en el dashboard de Braze en la página **Grupo de suscripción**.

### Creación de un grupo de suscripción {#creating-a-subscription-group}

1. Ve a **Audiencia** > **Administración del grupo de suscripción**.
2. Selecciona **Crear grupo de suscripción de correo electrónico**.
3. Dale un nombre y una descripción a tu grupo de suscripción.
4. Selecciona **Guardar**.

Todos los grupos de suscripción se añaden automáticamente a tu centro de preferencias.

![Campos para crear un grupo de suscripción.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

### Segmentación con un grupo de suscripción {#segmenting-with-a-subscription-group}

Al crear tus segmentos, establece el nombre del grupo de suscripción como filtro para dirigirte a los usuarios que han optado por tu grupo. Esto es ideal para boletines mensuales, cupones, niveles de membresía y más.

![Ejemplo de segmentación de usuarios en el segmento "Usuarios inactivos" con el filtro para usuarios en el grupo de suscripción "Correos electrónicos semanales".]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

### Archivado de grupos de suscripción {#archiving-subscription-groups}

Los grupos de suscripción archivados no se pueden editar y ya no aparecen en los filtros de segmento ni en tu centro de preferencias. Si intentas archivar un grupo que se está utilizando como filtro de segmento en cualquier correo electrónico, Campaign o Canvas, recibirás un mensaje de error que te impedirá archivar el grupo hasta que elimines todos los usos del mismo.

Para archivar tu grupo desde la página **Grupos de suscripción**, haz lo siguiente:

1. Busca tu grupo en la lista de grupos de suscripción.
2. Selecciona **Archivar** en el menú desplegable <i class="fa-solid fa-ellipsis-vertical" aria-label="Abrir menú de opciones"></i>&nbsp;.

Braze no procesa cambios de estado para los usuarios en grupos archivados. Por ejemplo, si archivas el Grupo de suscripción 1 mientras Alex está suscrito a él, Alex permanece "suscrito" incluso si hace clic en un enlace de cancelación de suscripción. Esto no importa porque el Grupo de suscripción 1 está archivado y no puedes enviar mensajes usándolo.

#### Visualización del tamaño de los grupos de suscripción {#viewing-subscription-group-sizes}

Puedes consultar el gráfico **Serie temporal del grupo de suscripción** en la página **Grupos de suscripción** para ver el tamaño del grupo de suscripción basado en el número de usuarios a lo largo de un período de tiempo. Estos tamaños de grupos de suscripción también son consistentes con otras áreas de Braze, como el cálculo del tamaño de segmento.

![Un ejemplo del gráfico "Serie temporal del grupo de suscripción" con fechas del 2 al 11 de diciembre. El gráfico muestra un aumento de ~10 millones en el número de usuarios del 6 al 7.]({% image_buster /assets/img_archive/subscription_group_graph.png %})

Si el recuento de la serie temporal diverge significativamente de un segmento que usa **El estado de suscripción de correo electrónico es Canceló suscripción**, recuerda que el gráfico cuenta la membresía en ese **grupo de suscripción**, mientras que ese filtro refleja el estado de suscripción de correo electrónico **global**; por ejemplo, los usuarios pueden estar suscritos globalmente pero haber cancelado la suscripción de un grupo específico.

#### Visualización de grupos de suscripción en los análisis de Campaign {#viewing-subscription-groups-in-campaign-analytics}

Puedes ver los recuentos de usuarios que cambiaron su estado de suscripción (suscrito o canceló suscripción) desde una Campaign de correo electrónico específica en la página de análisis de esa Campaign.

1. Desde la página de **análisis de Campaign** de tu Campaign, desplázate hacia abajo hasta la sección **Rendimiento del mensaje de correo electrónico**.
2. Selecciona la flecha debajo de **Grupos de suscripción** para ver el recuento agregado de cambios de estado, según lo enviado por tus clientes.

![La página "Rendimiento del mensaje de correo electrónico" que muestra el recuento agregado de cambios de estado enviados por los clientes.]({% image_buster /assets/img/campaign_analytics_sub_groups.png %})

### Verificación del grupo de suscripción de correo electrónico de un usuario {#checking-a-users-email-subscription-group}

- **Perfil de usuario:** Se puede acceder a los perfiles de usuario individuales a través del dashboard de Braze desde la página [Buscar usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/#access-profiles). Aquí puedes buscar perfiles de usuario por dirección de correo electrónico, número de teléfono o ID de usuario externo. También puedes ver los grupos de suscripción de correo electrónico de un usuario en la pestaña **Interacción**.
- **REST API de Braze:** Usa el [punto de conexión Listar grupos de suscripción del usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) o el [punto de conexión Listar estado del grupo de suscripción del usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) para ver los grupos de suscripción del perfil de usuario individual.

## Centro de preferencias de correo electrónico {#email-preference-center}

El centro de preferencias de correo electrónico te permite administrar qué usuarios reciben boletines de grupos de suscripción. Encuéntralo en el dashboard en **Grupos de suscripción**. Cada grupo de suscripción que crees se añade a la lista del centro de preferencias.

Para obtener más información sobre cómo añadir o personalizar un centro de preferencias, consulta [Centro de preferencias]({{site.baseurl}}/user_guide/channels/email/subscriptions/).

## Cambio de suscripciones de correo electrónico {#changing-email-subscriptions}

En la mayoría de los casos, los usuarios administran su suscripción de correo electrónico a través de enlaces incluidos en los correos electrónicos que reciben. Inserta un pie de página legalmente conforme con un enlace de cancelación de suscripción en la parte inferior de cada correo electrónico. Cuando los usuarios seleccionan la URL de cancelación de suscripción, Braze cancela su suscripción y muestra una página de confirmación del cambio. Incluye esta etiqueta de Liquid: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

Cuando un usuario selecciona "Cancelar suscripción de todos los tipos de correos electrónicos anteriores" en el centro de preferencias, Braze establece su estado de suscripción global de correo electrónico como `unsubscribed` y cancela su suscripción de todos los grupos.

### Creación de pies de página personalizados {#custom-footer}

Si no deseas usar el pie de página predeterminado, crea un pie de página de correo electrónico personalizado a nivel de espacio de trabajo y úsalo como plantilla en cada correo electrónico usando {% raw %}`{{${email_footer}}}`{% endraw %}.

Esto te evita crear un nuevo pie de página para cada plantilla de correo electrónico o Campaign de correo electrónico. Para ver los pasos, consulta [Pie de página de correo electrónico personalizado]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer/).

#### Administración de estados de suscripción para direcciones IP chinas {#managing-subscription-states-for-chinese-ip-addresses}

Si anticipas direcciones IP chinas, no dependas únicamente de un enlace de cancelación de suscripción para mantener las listas de `unsubscribed`. Proporciona rutas alternativas de cancelación de suscripción, como un ticket de soporte o un correo electrónico de un representante de atención al cliente.

### Creación de una página personalizada para cancelar la suscripción {#creating-a-custom-unsubscribe-page}

Cuando los usuarios seleccionan una URL de cancelación de suscripción en un correo electrónico, abren una página de inicio predeterminada que confirma el cambio de suscripción.

Para usar una página de inicio personalizada en su lugar:

1. Ve a **Preferencias de correo electrónico** > **Páginas de suscripción y pies de página**.
2. Añade el HTML de tu página personalizada.

Incluye un enlace de resuscripción (por ejemplo {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}) para que los usuarios puedan deshacer una cancelación de suscripción accidental.

También puedes enviar a los usuarios a tu sitio y actualizar el estado con la REST API de Braze (por ejemplo, un enlace con {% raw %}`?user_id={{${user_id}}}`{% endraw %} y luego llamar a [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/).

{% alert note %}
Si usas el pie de página del dashboard en lugar de solo un bloque de contenido HTML, la plantilla aún debe contener {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} para guardarse. Para usar una URL de cancelación de suscripción diferente temporalmente, puedes comentar la etiqueta predeterminada. Un ejemplo es: {% raw %}`<!-- {{${set_user_to_unsubscribed_url}}} -->`{% endraw %}.
{% endalert %}

![Página personalizada para cancelar la suscripción con una vista previa que dice "¡Lamentamos verte partir!".]({% image_buster /assets/img/custom_unsubscribe.png %})

### Creación de una página personalizada de adhesión voluntaria {#creating-a-custom-opt-in-page}

Usa una página personalizada de adhesión voluntaria para permitir que los usuarios reconozcan y controlen las preferencias de notificación antes de suscribirse. Esta comunicación adicional puede ayudar a que las Campaigns de correo electrónico no terminen en las carpetas de correo no deseado.

1. Ve a **Configuración** > **Preferencias de correo electrónico**.
2. Selecciona **Páginas de suscripción y pies de página**.
3. Personaliza el estilo en la sección **Página personalizada de adhesión voluntaria** para ver cómo indica a tus usuarios que se han suscrito.

Los usuarios llegan a esta página a través de la etiqueta {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %}.

{% alert tip %}
Usa un proceso de doble adhesión voluntaria para mejorar el alcance. Braze envía un correo electrónico de confirmación adicional donde el usuario confirma las preferencias de notificación a través de un enlace. Después de la confirmación, el usuario queda con adhesión voluntaria.
{% endalert %}

![Correo electrónico personalizado de adhesión voluntaria con un mensaje "Nos alegra que sigas queriendo saber de nosotros".]({% image_buster /assets/img/custom_optin.png %})

## Suscripciones y segmentación de Campaigns {#subscriptions-and-campaign-targeting}

De forma predeterminada, Braze dirige las Campaigns con mensajes push o de correo electrónico a los usuarios que están suscritos o con adhesión voluntaria. Cambia esto en **Público objetivo** seleccionando el menú desplegable junto a **Enviar a estos usuarios:**.

Braze admite tres estados de segmentación:

- Usuarios que están suscritos o con adhesión voluntaria (predeterminado).
- Solo usuarios con adhesión voluntaria.
- Todos los usuarios, incluidos los que cancelaron su suscripción.

{% alert important %}
Es tu responsabilidad cumplir con todas las [leyes de correo no deseado]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) aplicables al usar esta configuración de segmentación.
{% endalert %}

## Segmentación por suscripciones de usuario {#segmenting-by-user-subscriptions}

Usa los filtros "Estado de suscripción de correo electrónico" y "Estado de suscripción push" para segmentar usuarios por estado de suscripción.

Usa esto para dirigirte a usuarios que no han optado ni por recibir ni por dejar de recibir mensajes, y fomenta una adhesión voluntaria explícita. Crea un segmento con el filtro "El estado de suscripción de correo electrónico/push es Suscrito" y envía Campaigns a usuarios que están suscritos pero no con adhesión voluntaria.

![Estado de suscripción de correo electrónico utilizado como filtro de segmento.]({% image_buster /assets/img_archive/not_optin.png %})