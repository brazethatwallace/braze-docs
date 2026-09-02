---
nav_title: Migrar datos entre espacios de trabajo
article_title: Migrar datos entre espacios de trabajo e instancias
page_order: 1
page_type: reference
description: "Descubre cómo se aíslan los datos del espacio de trabajo, qué puede copiar o importar Braze entre espacios de trabajo y cómo planificar traslados entre entornos de staging, producción o paneles independientes."
---

# Migrar datos entre espacios de trabajo e instancias {#migrate-data-between-workspaces-and-instances}

> Los espacios de trabajo mantienen tus datos de Braze separados. Esta página explica cómo ese aislamiento afecta a la migración, qué puedes mover con las características del producto y las API, y qué necesitas reconstruir o gestionar fuera de Braze. La migración suele ser un esfuerzo multifuncional, no solo una tarea del administrador de la empresa. Los administradores suelen encargarse de la configuración del espacio de trabajo y la configuración de canales; los desarrolladores gestionan los cambios en el SDK y la API; los especialistas en marketing reconstruyen los segmentos y copian el contenido de mensajería. Cada paso requiere los [permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) correspondientes en los espacios de trabajo de origen y destino.

Todo lo que almacenas en Braze —perfiles de usuario, segmentos, contenido de mensajería e historial de participación— vive dentro de un espacio de trabajo. Un segmento, una Campaign o un Canvas no pueden leer ni dirigirse a datos de otro espacio de trabajo. Los usuarios del panel a menudo utilizan múltiples espacios de trabajo en el mismo panel de la empresa para staging y producción, para diferentes marcas o para divisiones regionales. Esa configuración te da aislamiento, pero también significa que no hay una única acción en el panel que mueva todos los datos de un espacio de trabajo a otro espacio de trabajo o a otra instancia de Braze.

Para contexto de planificación, consulta [Primeros pasos: Espacios de trabajo]({{site.baseurl}}/user_guide/get_started/workspaces) y [Crear y administrar espacios de trabajo]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces).

## Lo que Braze no migra automáticamente entre espacios de trabajo {#what-braze-does-not-automatically-migrate-between-workspaces}

Lo siguiente no se migra de forma masiva cuando apuntas los SDK o las API a un nuevo espacio de trabajo (o a un nuevo entorno de panel de Braze con sus propios espacios de trabajo):

| Área | Comportamiento |
| --- | --- |
| **Perfiles de usuario** | Los perfiles no se transfieren como una unidad empaquetada. Recrea o importa usuarios en el espacio de trabajo de destino (consulta [Datos del perfil de usuario](#user-profile-data)). |
| **Segmentos y filtros** | Las definiciones de segmentos permanecen en el espacio de trabajo de origen. Reconstruye los segmentos en el espacio de trabajo de destino utilizando la misma lógica cuando sea posible. |
| **Historial de mensajes** | El historial de recepción de Campaigns y Canvas en un perfil está vinculado al espacio de trabajo de origen. No aparece en un nuevo perfil en otro espacio de trabajo a menos que lo modeles tú mismo (por ejemplo, mediante atributos personalizados), como se indica en las [Preguntas frecuentes de incorporación a Braze]({{site.baseurl}}/onboarding_faq). |
| **Configuración específica del canal** | Los dominios de envío, las suscripciones de SMS, los números de WhatsApp y configuraciones similares tienen alcance de espacio de trabajo. Reconfigúralos en el espacio de trabajo de destino cuando corresponda. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Lo que Braze no migra automáticamente entre espacios de trabajo" }

{% alert important %}
Si utilizas espacios de trabajo separados para staging y producción, recuerda que los conectores de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) no se comparten entre espacios de trabajo. Planifica qué espacio de trabajo es el propietario de las exportaciones de producción. Para más detalles, consulta [Primeros pasos: Espacios de trabajo]({{site.baseurl}}/user_guide/get_started/workspaces#currents-connectors).
{% endalert %}

## Lo que puedes mover o recrear {#what-you-can-move-or-recreate}

### Contenido de Campaigns, Canvas y páginas de destino {#campaign-canvas-and-landing-page-content}

Puedes copiar muchas definiciones de Campaigns, Canvas y páginas de destino a otro espacio de trabajo como borradores. Los canales compatibles, los campos omitidos y las advertencias sobre Liquid están documentados en [Copiar Campaigns, Canvas y páginas de destino entre espacios de trabajo]({{site.baseurl}}/user_guide/messaging/governance/copy_across_workspaces). Después de copiar, actualiza los segmentos, los desencadenantes y cualquier referencia específica del espacio de trabajo antes de lanzar o publicar.

### Datos del perfil de usuario {#user-profile-data}

Enfoques habituales:

- **REST API:** Usa [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para crear o actualizar usuarios en el espacio de trabajo de destino con los identificadores y atributos que necesites. Este es el mismo patrón descrito para [migrar datos de usuario heredados]({{site.baseurl}}/developer_guide/getting_started/integration_overview#migrating-legacy-user-data) al incorporar datos históricos a Braze.
- **Importación CSV:** Para importaciones dirigidas por especialistas en marketing, consulta [Importar usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/import_users) e [Importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import).
- **Ingesta de datos en la nube:** Para sincronizar atributos desde un almacén de datos al espacio de trabajo de destino, consulta [Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).
- **Exportaciones desde el espacio de trabajo de origen:** Usa [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) o [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) para extraer los datos que tienes permitido mover, y luego mapéalos en `users/track` o CSV para el destino. Respeta tus obligaciones de retención de datos, privacidad y contractuales al exportar y recargar datos.

{% alert note %}
La fusión de perfiles duplicados con el endpoint [Fusionar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) o [usuarios duplicados]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users) en el panel se aplica dentro de un único espacio de trabajo, no entre dos espacios de trabajo.
{% endalert %}

### Campos de exportación de usuarios que no se mapean a las API estándar de perfil {#user-export-fields-that-dont-map-to-standard-profile-apis}

Cuando reconstruyes usuarios en un espacio de trabajo de destino a partir de una [exportación de usuarios]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier), algunos campos de exportación no se pueden escribir de vuelta en los campos estándar de perfil de Braze a través de la REST API o CSV (de la forma en que el SDK y el servidor los rellenan). A menudo puedes conservar los valores como atributos personalizados en su lugar. Ten en cuenta las siguientes limitaciones.

#### Información del dispositivo (`devices`) {#device-information-devices}

Los registros de dispositivo en la exportación son rellenados por el SDK. No puedes migrar esos datos a los campos estándar de dispositivo de Braze a través de la REST API.

Si necesitas esa información antes de que el usuario inicie una sesión en una aplicación que apunte al espacio de trabajo de destino, envíala como atributos personalizados cuando importes al usuario. Los filtros de segmentación estándar y las referencias de Liquid que dependen de los datos de dispositivo integrados no utilizan la carga útil de dispositivo exportada hasta que el usuario abra una sesión en una instancia de la aplicación conectada al nuevo espacio de trabajo (cuando el SDK actualiza los campos estándar de dispositivo).

{% alert note %}
Esto es independiente de la [migración de tokens de notificaciones push](#push-tokens), que utiliza el campo `push_tokens` en [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).
{% endalert %}

#### Total de sesiones y datos de sesión por aplicación (`apps` y `sessions` anidados) {#total-sessions-and-per-app-session-data-apps-and-nested-sessions}

Los totales de sesiones y los datos de sesión anidados del objeto `apps` en una exportación no se pueden reimportar a los mismos campos integrados. Para preservar conteos heredados (por ejemplo, el total de sesiones del espacio de trabajo de origen), almacénalos en atributos personalizados y segmenta sobre esos campos en el espacio de trabajo de destino.

Puedes establecer `date_of_first_session` y `date_of_last_session` a través de [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) o importación CSV. Para los formatos aceptados, consulta el [Objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) e [Importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import).

#### Contenedor aleatorio (`random_bucket`) {#random-bucket-random_bucket}

A cada usuario se le asigna un [número de contenedor aleatorio]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-update-events) en su espacio de trabajo. Ese valor no se puede reimportar; el usuario obtiene un nuevo contenedor aleatorio en el espacio de trabajo de destino.

Si dependes del número anterior para grupos de exclusión o muestreo (por ejemplo, excluir usuarios cuyo `random_bucket` está por debajo de un umbral), guarda el valor exportado como un atributo personalizado y construye segmentos o filtros sobre ese atributo en lugar del campo integrado de contenedor aleatorio.

#### Campos de atribución de partners (`attributed_*`) {#partner-attribution-fields-attributed_}

Los campos de atribución de integraciones de partners (los campos `attributed_*` en una exportación) no se pueden establecer en los campos estándar de atribución de Braze a través de la REST API. Mapéalos a atributos personalizados en el espacio de trabajo de destino si necesitas conservarlos para segmentación o mensajería.

### Tokens de notificaciones push {#push-tokens}

Cuando los usuarios ya tienen tokens de notificaciones push de un proveedor anterior o una versión anterior de la aplicación, puedes importar tokens para aplicaciones móviles a través de la API, o confiar en el SDK después de la integración. Los tokens de notificaciones push web tienen limitaciones de API. Para detalles completos y ejemplos, consulta [Migrar tokens de notificaciones push]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens).

### WhatsApp

Los números de teléfono y los grupos de suscripción se pueden mover entre espacios de trabajo con un flujo de transferencia específico. Consulta [Transferir números de teléfono y grupos de suscripción de WhatsApp entre espacios de trabajo]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/transfer_between_workspaces).

### Datos de participación y análisis fuera de Braze {#engagement-and-analytics-data-outside-braze}

Si necesitas un registro histórico de envíos, aperturas o clics al consolidar entornos, [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) y otras exportaciones son la forma compatible de llevar esos datos a tu almacén de datos o herramientas. Esos datos no se reingestan en Braze como historial de mensajes nativo por usuario en otro espacio de trabajo.

## Antes de cambiar las claves del SDK o la API {#before-you-change-sdk-or-api-keys}

Cuando hayas apuntado tu aplicación o sitio a un nuevo espacio de trabajo:

- Los usuarios que abran la aplicación o el sitio pueden crear nuevos perfiles en el nuevo espacio de trabajo. No trasladan automáticamente el historial específico del espacio de trabajo anterior.
- Si la misma persona pudiera existir en ambos espacios de trabajo, puedes encontrar [escenarios similares a duplicados]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces#should-i-create-a-new-workspace-when-im-releasing-an-updated-app) (por ejemplo, alcance de push superpuesto). Prefiere un plan deliberado de datos y segmentación en lugar de compartir claves de producción y staging de forma involuntaria.

{% alert tip %}
Para límites de eliminación de espacios de trabajo o instancias de aplicación, traslados especiales de cuentas o planificación de migraciones a gran escala, [ponte en contacto con soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) con los enlaces de tu panel y un resumen de los espacios de trabajo de origen y destino.
{% endalert %}