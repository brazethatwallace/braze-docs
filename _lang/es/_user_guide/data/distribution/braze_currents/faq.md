---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre Currents
page_order: 4
page_type: reference
description: "Este artículo aborda algunas de las preguntas más frecuentes que surgen al configurar Braze Currents."
tool: Currents
---

# Preguntas frecuentes {#frequently-asked-questions}

> Esta página ofrece respuestas a algunas preguntas frecuentes sobre Currents.

## ¿Puedo exportar datos de Campaign o Canvas para un periodo de fechas específico? {#can-i-export-campaign-or-canvas-data-for-a-specific-date-window}

Para obtener métricas de Campaign o Canvas en un rango de fechas definido, utiliza uno de los siguientes enfoques:

- {% multi_lang_include product_feedback_cta.md context="gap" feature="date-aligned campaign or Canvas exports for dashboard-style reporting outside standard API windows" %}
- Llama a los endpoints de [análisis de Campaign]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) o [análisis de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) con los parámetros `ending_at` y `length` (o utiliza [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) y [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics)) para obtener datos de series temporales.
- Transmite eventos a tu almacén de datos con [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) cuando necesites datos de participación de mensajes continuos y consultables en Amazon S3, Azure Blob Storage u otro destino compatible.

## ¿Cómo edito una integración de Currents en vivo? {#how-do-i-edit-a-live-currents-integration}

Para modificar un conector de Currents en vivo, abre la integración y selecciona **Editar**. Sin **Editar**, la interfaz de la integración permanece en modo de solo lectura y no puedes modificar la configuración del conector únicamente desde los iconos.

## ¿Cómo gestiona Braze los archivos Avro de Azure Blob Storage después de la carga? {#how-does-braze-handle-azure-blob-storage-avro-files-after-upload}

Braze no modifica los archivos Avro en [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents) una vez completada la carga. Azure puede bloquear la eliminación de un blob mientras una carga todavía está en curso.

## ¿Cómo obtengo datos históricos? {#how-do-i-get-historical-data}

Currents es una transmisión de datos en tiempo real y en vivo, lo que significa que los eventos no se pueden reproducir. Sin embargo, puedes almacenar los datos de Currents en un almacén de datos como [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3) o [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents), para que puedas actuar sobre eventos pasados como desees. Los datos se conservan durante 30 días, pero para datos más históricos, puedes consultar [Snowflake]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/s3_to_snowflake).

## ¿Por qué Currents genera datos en formato Avro y no en JSON? {#why-does-currents-output-data-in-the-avro-format-not-json}

Avro, a diferencia de JSON (que no tiene esquema), admite de forma nativa la evolución de esquemas. También te beneficias de la capacidad de enviar archivos Avro con menos ancho de banda y ahorro de espacio de almacenamiento, ya que Avro es altamente comprimible.

## ¿Cómo gestiona Braze la carga de archivos? {#how-does-braze-handle-file-overhead}

Construimos un proceso de extraer, transformar y cargar (ETL), que te permite extraer grandes cantidades de datos de una base de datos para colocarlos y almacenarlos en otra.

## ¿Dónde debo almacenar estos datos para consultarlos? {#where-should-i-store-this-data-for-querying}

Braze tiene partnerships con varios almacenes de datos en los que puedes almacenar tus datos para realizar consultas. Recomendamos usar:
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents).

## ¿Qué tan confiables son los datos de Currents? {#how-reliable-is-currents-data}

Currents garantiza la entrega "al menos una vez", lo que significa que ocasionalmente pueden escribirse eventos duplicados en tu contenedor de almacenamiento. Si tu caso de uso requiere la entrega exactamente una vez, puedes deduplicar eventos utilizando el campo de identificador único (`id`) que se envía con cada evento. Para más detalles, consulta [Semántica de entrega de eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics).

## ¿Con qué frecuencia se sincronizan los datos con Currents? {#how-often-is-data-synced-to-currents}

Los datos se transmiten de forma continua. Braze envía un lote de eventos cada vez que hay un lote completo listo para enviar, o cada 5 minutos, lo que ocurra primero. Para conectores de alto volumen, los datos llegan casi en tiempo real. Para conectores de bajo volumen, los datos pueden tardar entre 5 y 30 minutos en llegar. Para más detalles, consulta [Umbral de escritura Avro]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics#avro-write-threshold).

{% alert note %}
Si un dispositivo no está conectado a Internet, puede haber un retraso en la creación del evento. Esto es más común en los eventos de mensajes dentro de la aplicación, ya que los mensajes dentro de la aplicación pueden activarse sin conexión.
{% endalert %}

## ¿Cómo puedo saber qué eventos están disponibles para Currents? {#how-do-i-find-which-events-are-available-for-currents}

Para obtener una lista completa de los eventos que Currents registra, consulta los glosarios de [eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) y [eventos de participación en mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events). Puedes filtrar estos glosarios por tipo de evento (como envíos, entregas o aperturas).

## ¿Por qué los recuentos de eventos de Currents no coinciden con las métricas de mi panel o mi informe de participación? {#why-do-my-currents-event-counts-not-match-my-dashboard-or-engagement-report-metrics}

Currents y el panel de Braze calculan ciertas métricas de forma diferente, por lo que no se esperan coincidencias exactas entre los eventos de Currents y las métricas del panel.

**Clics únicos:** Para el correo electrónico, el panel rastrea los clics únicos durante un período de siete días y los mide por `dispatch_id`. Currents registra cada evento de clic sin procesar. Para alinear los recuentos de clics únicos basados en Currents con las métricas del panel, filtra los eventos en los que `is_unique` sea `true`.

**Cancelaciones de suscripción:** La métrica *Unsub* del panel refleja los clics en el enlace estándar de cancelación de suscripción de Braze. Las páginas personalizadas de cancelación de suscripción no incrementan esta métrica a menos que actualices el usuario a través de la API. El evento `users.messages.email.Unsubscribe` de Currents es un evento de clic especializado que se activa cuando un usuario hace clic en un enlace de cancelación de suscripción en el cuerpo o pie del correo electrónico, o a través del encabezado list-unsubscribe. No representa todos los cambios de estado de suscripción de correo electrónico.

**Marcas de tiempo y zonas horarias:** Todas las marcas de tiempo de Currents están en UTC. Las métricas del panel siguen la zona horaria de tu empresa. Agregar datos de Currents por día calendario sin convertirlos a la zona horaria de tu empresa puede hacer que los recuentos caigan en distintos intervalos de fecha respecto a lo que aparece en el panel.

**Eventos duplicados:** Currents ofrece una entrega de al menos una vez, lo que significa que ocasionalmente pueden escribirse eventos duplicados. Deduplica por el campo único `id` de cada evento antes de comparar los totales con las métricas del panel.

## ¿Por qué el `external_user_id` (esquema de Braze: `external_id`) en mi evento de apertura o clic de correo electrónico de Currents difiere del perfil de usuario en el panel de Braze? {#why-does-the-external_user_id-braze-schema-external_id-in-my-currents-email-open-or-click-event-differ-from-the-user-profile-in-the-braze-dashboard}

- **En el panel de Braze:** Cuando un usuario asociado a una dirección de correo electrónico abre o hace clic en un correo electrónico, todos los perfiles de usuario que comparten esa dirección de correo electrónico se marcan como si hubieran abierto o hecho clic en ese correo electrónico. Para más información, consulta [¿Qué sucede cuando se envía un correo electrónico y varios perfiles tienen la misma dirección de correo electrónico?]({{site.baseurl}}/user_guide/channels/email/faq#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address).
- **En Currents:** Esa misma apertura o clic se almacena en un solo perfil. Braze lo atribuye al perfil que fue originalmente destinatario del envío, si ese perfil aún comparte la dirección de correo electrónico. De lo contrario, Braze lo atribuye a un perfil seleccionado aleatoriamente entre los que comparten la dirección de correo electrónico.

Debido a esto, el valor de `external_user_id` (denominado `external_id` en la tabla de mapeado del esquema de Braze) en un evento de apertura o clic de correo electrónico de Currents puede no coincidir con el perfil de usuario que esperas cuando comparas Currents con el panel de Braze.

## ¿Se registran todos los eventos de envío en Currents? {#are-all-send-events-logged-to-currents}

Todos los eventos se registran en Currents. No existen escenarios en los que un evento se suprima intencionalmente del flujo de Currents.

## ¿Pueden corromperse los datos en Currents? {#can-data-be-corrupted-in-currents}

En circunstancias normales, los datos de Currents no se corrompen. Aunque siempre existe la posibilidad de que surja un problema poco frecuente, no se conocen condiciones en las que los datos se corrompan de forma sistemática.

## ¿Por qué veo datos de eventos personalizados con fechas anteriores a la configuración de mi integración de Currents? {#why-do-i-see-custom-event-data-dated-before-my-currents-integration-was-set-up}

Braze no rellena eventos retroactivamente en Currents. Sin embargo, los eventos personalizados pueden registrarse con una marca de tiempo pasada (por ejemplo, si un dispositivo estaba sin conexión cuando ocurrió el evento y se sincronizó después). En estos casos, la marca de tiempo del evento refleja cuándo ocurrió originalmente el evento, lo que puede ser anterior a la configuración de la integración de Currents.

## ¿Qué identificadores de usuario se incluyen en los eventos de Currents? {#what-user-identifiers-are-included-in-currents-events}

Los eventos de participación de mensajes (envíos, aperturas, clics, etc.) incluyen el ID de usuario de Braze (`user_id`) y, cuando está presente en el perfil, el identificador externo (`external_user_id` en las cargas útiles de los eventos, etiquetado como `external_id` en la tabla de mapeado del esquema de Braze). Algunos eventos de participación de mensajes de correo electrónico también incluyen `email_address`. Los atributos personalizados no se incluyen.

Si estás enrutando datos de Currents a un almacén de datos o CRM y necesitas hacer un join con los datos del perfil, realiza ese join en tu sistema downstream utilizando `user_id` o `external_user_id`.

## ¿Puedo incluir atributos personalizados en los eventos de envío de Currents? {#can-i-include-custom-attributes-in-currents-send-events}

No. Currents no incluye atributos personalizados en los eventos de envío. Currents registra eventos personalizados y eventos de participación en mensajes. Para consultar una lista completa de los campos disponibles, consulta los [glosarios de eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary).

## ¿Currents incluye etiquetas de Campaign o Canvas o pares clave-valor? {#does-currents-include-campaign-or-canvas-tags-or-key-value-pairs}

No. Currents no incluye etiquetas de Campaign o Canvas ni pares clave-valor a nivel de mensaje. Para recuperar datos de etiquetas, utiliza la [REST API de exportación]({{site.baseurl}}/api/endpoints/export). Como alternativa, puedes usar un canal de webhook en una Campaign para enviar datos de etiquetas o pares clave-valor a tu propio endpoint, utilizando [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) para crear plantillas con los valores.

## ¿Cómo notifica Braze a los clientes sobre los cambios en Currents? {#how-does-braze-notify-customers-of-changes-to-currents}

En la rara circunstancia de que se produzcan cambios que rompan la compatibilidad, Braze envía un correo electrónico con antelación al contacto de cualquier integración activa y a todos los administradores con integraciones activas de Currents que hayan utilizado el panel en los últimos 30 días. Para cambios que no rompen la compatibilidad, como nuevos eventos o nuevos campos en un evento existente, Braze no envía una notificación. Puedes consultar el [registro de cambios de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) para ver los últimos cambios.

## ¿Cuánto almacenamiento necesito para los datos de Currents? {#how-much-storage-do-i-need-for-currents-data}

Los requisitos de almacenamiento dependen de tu volumen de eventos y de los tipos de eventos que exportas. Braze proporciona [eventos de ejemplo en formato Avro](https://github.com/appboy/currents-examples/tree/master/sample-data) que puedes usar para estimar los tamaños de archivo en tu caso de uso.

## ¿Por qué el nombre de la Campaign o del paso en Canvas es `NULL` en mis datos de Currents? {#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data}

Cuando creas una nueva Campaign o un Canvas, el nombre puede tardar un tiempo en propagarse por todos los sistemas de Braze. Los eventos enviados a través de Currents durante este período pueden tener `NULL` en los campos de nombre (como `campaign_name` o `canvas_step_name`). Esto también es esperado si el nombre se modificó poco antes de que se registraran los eventos. Para evitarlo, espera un tiempo después de crear o cambiar el nombre de una Campaign o un paso en Canvas antes de enviar.

## ¿Por qué los eventos de fin de sesión se retrasan o faltan en Currents? {#why-are-session-end-events-delayed-or-missing-in-currents}

Los eventos de fin de sesión siguen la programación normal de carga del SDK. El SDK de Braze almacena en caché los datos de sesión de forma local y los envía periódicamente en función de la calidad de la red; por ejemplo, aproximadamente cada 10 segundos con una conexión fuerte. Hasta que el SDK carga el evento, este no aparece en Currents.

Si un usuario fuerza el cierre de la aplicación o se queda sin conexión antes del siguiente envío, el evento de fin de sesión puede llegar tarde o no llegar en absoluto. En iOS, los eventos de fin de sesión a menudo no se envían hasta que la aplicación se vuelve a abrir, porque el SDK no puede enviar datos mientras la aplicación está en segundo plano.

Cuando necesites límites de sesión más oportunos en Currents, llama a `requestImmediateDataFlush()` en puntos del ciclo de vida, como cuando la aplicación pasa a segundo plano o vuelve a primer plano. Para más información, consulta [Carga y descarga de datos]({{site.baseurl}}/developer_guide/getting_started/sdk_overview#data-upload-and-download) y [El fin de sesión y el inicio de sesión tienen marcas de tiempo similares (iOS)]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log#session-end-and-session-start-have-similar-timestamps-ios).

## ¿Qué sucede si mi contenedor de almacenamiento no está disponible cuando Currents intenta escribir datos? {#what-happens-if-my-storage-bucket-is-unavailable-when-currents-tries-to-write-data}

Si tu contenedor de almacenamiento no está disponible en el momento de la transferencia de datos, esos datos se pierden. Braze no puede rellenar eventos que no se entregaron correctamente. Para evitar la pérdida de datos, asegúrate de que tu contenedor de almacenamiento esté disponible y correctamente configurado en todo momento.

## ¿Por qué veo mensajes de límite de derechos al crear o editar una integración de Currents? {#why-do-i-see-entitlement-limit-messages-when-creating-or-editing-a-currents-integration}

Currents utiliza grupos de derechos separados para las diferentes capacidades de los conectores:

- **Eventos de participación**: necesarios para crear o actualizar un conector estándar de Currents.
- **Eventos de comportamiento del cliente**: necesarios para habilitar **Track Customer Behavior and User Events**.
- **Perfiles y atributos de usuario**: necesarios para habilitar **Track user profiles and attributes**.

Si algún grupo se agota, Braze muestra una advertencia de derechos y bloquea esa acción. Ponte en contacto con tu director de cuentas de Braze para solicitar derechos adicionales o ayuda para ajustar tu configuración.

## ¿Con qué frecuencia cambia la versión de Currents en la ruta de almacenamiento? {#how-often-does-the-currents-version-in-the-storage-path-change}

El segmento `version=<currents_version>` en la ruta de almacenamiento avanza con cada lanzamiento de Currents en una cadencia mensual (por ejemplo, de `version=6` a `version=7`). Recomendamos leer los archivos de forma recursiva desde la ruta raíz en lugar de codificar un segmento de versión específico, de modo que tu pipeline recoja los datos automáticamente tras un cambio de versión. Para más detalles sobre el formato de la ruta, consulta [Semántica de entrega de eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics). Para un historial de cambios por versión, consulta el [Registro de cambios de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs).

## ¿Por qué faltan `campaign_id` o `canvas_id` en un evento de participación de mensajes? {#why-are-campaign_id-or-canvas_id-missing-from-a-message-engagement-event}

Dependiendo del tipo de evento y el contexto, un evento de participación de mensajes puede no estar vinculado a una Campaign o un paso en Canvas específicos. En esos casos, `campaign_id`, `canvas_id` y los campos de nombre relacionados pueden omitirse de la carga útil del evento. Si no ves esos campos en un evento determinado, comprueba si ese tipo de evento y contexto normalmente incluyen identificadores de Campaign o Canvas.

## ¿Por qué las marcas de tiempo de Currents están limitadas a precisión de segundos? {#why-are-currents-timestamps-limited-to-second-precision}

El campo `time` en los eventos de Currents se almacena como un entero de 32 bits y, por lo tanto, está limitado a precisión de segundos. Algunos eventos también incluyen un campo separado de marca de tiempo con precisión de milisegundos de 64 bits; consulta el [glosario de eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary) para conocer los campos disponibles en cada tipo de evento.

## ¿Por qué el evento `users.canvas.Conversion` de Currents tiene una hora diferente a la de Canvas? {#why-does-the-userscanvasconversion-event-from-currents-have-a-different-time-than-the-canvas}

La hora del evento `users.canvas.Conversion` en Currents refleja la ventana de conversión total —la duración de Canvas más el plazo de conversión— medida desde la entrada en Canvas.

## ¿Qué sucede cuando los informes de participación se envían a S3? {#what-happens-when-engagement-reports-are-sent-to-s3}

Si las credenciales de S3 están configuradas para la exportación de datos pero no para Currents, Braze sube los informes de participación al contenedor de S3 especificado. El usuario que aparece en el campo **Send Report To** recibe un correo electrónico con un enlace al informe en S3.

## ¿Se pueden enviar datos de usuarios anónimos a Amplitude a través de Braze Currents? {#can-anonymous-user-data-be-sent-to-amplitude-through-braze-currents}

Los datos de usuarios anónimos, identificados por `device_id`, se pueden enviar a Amplitude a través de Currents. Esto requiere la habilitación de la característica por parte de tu equipo de cuentas de Braze.

## ¿Cómo se registran en Currents las impresiones del grupo de control para Content Cards y mensajes dentro de la aplicación? {#how-are-control-group-impressions-for-content-cards-and-in-app-messages-logged-in-currents}

Cuando se asigna un usuario a un grupo de control para una Campaign de Content Cards o mensajes dentro de la aplicación, Currents emite un evento `users.campaigns.EnrollInControl` en lugar de un evento de impresión.

## ¿Qué sucede cuando se dirige a un usuario inexistente a través de la API? {#what-happens-when-you-target-a-non-existent-user-through-the-api}

Cuando se dirige a un usuario que no existe, la API devuelve una respuesta `200`, pero el envío se cancela con el resultado "Unknown external ID". No se generan eventos de Currents para ese envío. Ten en cuenta que el parámetro `send_to_existing_only` tiene como valor predeterminado `true`, por lo que los envíos a usuarios desconocidos se omiten silenciosamente a menos que lo establezcas explícitamente en `false`.