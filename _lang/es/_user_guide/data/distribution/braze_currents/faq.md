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

### ¿Puedo exportar datos de Campaign o Canvas para un período de fechas específico? {#can-i-export-campaign-or-canvas-data-for-a-specific-date-window}

Para obtener métricas de Campaign o Canvas en un rango de fechas definido, utiliza uno de los siguientes enfoques:

- Envía una [solicitud de producto](https://portal.braze.com/) para exportaciones alineadas por fecha cuando necesites informes de estilo dashboard fuera de las ventanas estándar de la API.
- Llama a los puntos finales de [análisis de Campaign]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) o [análisis de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) con los parámetros `ending_at` y `length` (o usa [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) y [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/)) para datos de series temporales.
- Transmite eventos a tu almacén de datos con [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) cuando necesites datos continuos y consultables de interacción con mensajes en Amazon S3, Azure Blob Storage u otro destino compatible.

### ¿Cómo edito una integración de Currents en vivo? {#how-do-i-edit-a-live-currents-integration}

Para modificar un conector de Currents en vivo, abre la integración y haz clic en **Editar** en la parte inferior izquierda de la página. Sin **Editar**, la interfaz de la integración permanece en modo de solo lectura y no puedes modificar la configuración del conector solo desde los iconos.

### ¿Cómo gestiona Braze los archivos Avro de Azure Blob Storage después de la carga? {#how-does-braze-handle-azure-blob-storage-avro-files-after-upload}

Braze no modifica los archivos Avro en [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) después de que se completa la carga. Azure puede bloquear la eliminación de un blob mientras una carga aún está en curso.

### ¿Cómo obtengo datos históricos? {#how-do-i-get-historical-data}

Currents es una transmisión de datos en vivo y en tiempo real, lo que significa que los eventos no pueden reproducirse. Sin embargo, puedes almacenar los datos de Currents en un almacén de datos como [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) o [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/), para que puedas actuar sobre eventos pasados según te convenga. Los datos se conservan durante 30 días, pero para obtener más datos históricos, puedes consultar [Snowflake]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/s3_to_snowflake/).

### ¿Por qué Currents emite los datos en formato Avro y no JSON? {#why-does-currents-output-data-in-the-avro-format-not-json}

Avro, a diferencia de JSON sin esquema, admite de forma nativa la evolución del esquema. También te beneficiarás de la posibilidad de enviar archivos Avro con menos ancho de banda y ahorrando espacio de almacenamiento, porque Avro es altamente compresible.

### ¿Cómo gestiona Braze la sobrecarga de archivos? {#how-does-braze-handle-file-overhead}

Creamos un proceso de extraer, transformar, cargar (ETL), que te permite extraer grandes cantidades de datos de una base de datos para colocarlos y almacenarlos en otra.

### ¿Dónde debo almacenar estos datos para realizar consultas? {#where-should-i-store-this-data-for-querying}

Braze está asociado con varios almacenes de datos en los que puedes guardar tus datos para realizar consultas. Recomendamos utilizar:
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).

### ¿Qué tan fiables son los datos de Currents? {#how-reliable-is-currents-data}

Currents garantiza la entrega «al menos una vez», lo que significa que ocasionalmente pueden escribirse eventos duplicados en tu contenedor de almacenamiento. Si tu caso de uso requiere entrega exactamente una vez, puedes deduplicar eventos utilizando el campo de identificador único (`id`) que se envía con cada evento. Para más detalles, consulta [Semántica de entrega de eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/).

### ¿Con qué frecuencia se sincronizan los datos con Currents? {#how-often-is-data-synced-to-currents}

Los datos se transmiten de forma continua. Braze envía un lote de eventos cada vez que hay un lote completo listo para enviar, o cada 5 minutos, lo que ocurra primero. Para conectores de alto volumen, los datos llegan casi en tiempo real. Para conectores de bajo volumen, espera que los datos lleguen en un plazo de 5 a 30 minutos. Para más detalles, consulta [Umbral de escritura Avro]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/#avro-write-threshold).

{% alert note %}
Si un dispositivo no está conectado a internet, puede haber un retraso en la creación del evento. Esto es más común en los eventos de mensajes dentro de la aplicación, ya que los mensajes dentro de la aplicación pueden desencadenarse sin conexión.
{% endalert %}

### ¿Cómo puedo saber qué eventos están disponibles para Currents? {#how-do-i-find-which-events-are-available-for-currents}

Para obtener una lista completa de los eventos que registra Currents, consulta los glosarios de [Eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) y [Eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/). Puedes filtrar estos glosarios por tipo de evento (como envíos, entregas o aperturas).

### ¿Por qué el `external_id` en mi evento de apertura o clic de correo electrónico en Currents difiere del perfil de usuario en el panel de Braze? {#why-does-the-external_id-in-my-currents-email-open-or-click-event-differ-from-the-user-profile-in-the-braze-dashboard}

- **En el panel de Braze:** cuando un usuario asociado a una dirección de correo electrónico abre o hace clic en un correo electrónico, todos los perfiles de usuario que comparten esa dirección de correo electrónico se marcan como que abrieron o hicieron clic en ese correo electrónico. Para más información, consulta [¿Qué ocurre cuando se envía un correo electrónico y varios perfiles tienen la misma dirección de correo electrónico?]({{site.baseurl}}/user_guide/channels/email/faq/#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address).
- **En Currents:** esa misma apertura o clic se almacena en un solo perfil. Braze lo atribuye al perfil que fue originalmente el objetivo del envío, si ese perfil aún comparte la dirección de correo electrónico. De lo contrario, Braze lo atribuye a un perfil seleccionado aleatoriamente entre los que comparten la dirección de correo electrónico.

Debido a esto, el `external_id` en un evento de apertura o clic de correo electrónico en Currents puede no coincidir con el perfil de usuario que esperas cuando comparas Currents con el panel de Braze.

### ¿Se registran todos los eventos de envío en Currents? {#are-all-send-events-logged-to-currents}

Todos los eventos se registran en Currents. No hay escenarios en los que un evento se suprima intencionalmente de la transmisión de Currents.

### ¿Pueden corromperse los datos en Currents? {#can-data-be-corrupted-in-currents}

En circunstancias normales, los datos de Currents no se corrompen. Aunque siempre existe la posibilidad de un problema poco frecuente, no se conocen condiciones en las que los datos se corrompan de forma sistemática.

### ¿Por qué veo datos de eventos personalizados con fechas anteriores a la configuración de mi integración de Currents? {#why-do-i-see-custom-event-data-dated-before-my-currents-integration-was-set-up}

Braze no rellena eventos retroactivamente en Currents. Sin embargo, los eventos personalizados pueden registrarse con una marca de tiempo pasada (por ejemplo, si un dispositivo estaba sin conexión cuando ocurrió el evento y se sincronizó después). En estos casos, la marca de tiempo del evento refleja cuándo ocurrió originalmente, lo que puede ser anterior a la configuración de la integración de Currents.

### ¿Puedo incluir atributos personalizados en los eventos de envío de Currents? {#can-i-include-custom-attributes-in-currents-send-events}

No. Currents no incluye atributos personalizados en los eventos de envío. Currents registra eventos personalizados y eventos de interacción con mensajes. Para obtener una lista completa de los campos disponibles, consulta los [glosarios de eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/).

### ¿Currents incluye etiquetas de Campaign o pares clave-valor? {#does-currents-include-campaign-tags-or-key-value-pairs}

No. Currents no incluye etiquetas de Campaign ni pares clave-valor a nivel de mensaje. Como alternativa, puedes usar un canal webhook en la campaña para enviar esta información a tu propio punto de conexión, utilizando [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) para incluir los datos de etiquetas y pares clave-valor mediante plantillas.

### ¿Cómo notifica Braze a los clientes sobre cambios en Currents? {#how-does-braze-notify-customers-of-changes-to-currents}

Cuando se producen cambios en Currents (como nuevos campos de eventos o tipos de eventos), Braze envía un correo electrónico a todos los clientes con integraciones de Currents activas que hayan utilizado el dashboard en los últimos 30 días. También puedes consultar el [registro de cambios de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/) para ver los últimos cambios.

### ¿Cuánto almacenamiento necesito para los datos de Currents? {#how-much-storage-do-i-need-for-currents-data}

Los requisitos de almacenamiento dependen del volumen de eventos y los tipos de eventos que estés exportando. Braze proporciona [eventos de ejemplo en formato Avro](https://github.com/appboy/currents-examples/tree/master/sample-data) que puedes usar para estimar el tamaño de los archivos para tu caso de uso.

### ¿Por qué el nombre de la Campaign o del paso en Canvas aparece como `NULL` en mis datos de Currents? {#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data}

Cuando creas una nueva Campaign o Canvas, el nombre puede tardar un tiempo en propagarse por todos los sistemas de Braze. Los eventos enviados a través de Currents durante este período pueden tener `NULL` en los campos de nombre (como `campaign_name` o `canvas_step_name`). Esto también es esperado si el nombre se modificó poco antes de que se registraran los eventos. Para evitar esto, espera un tiempo después de crear o renombrar una Campaign o un paso en Canvas antes de realizar envíos.

### ¿Por qué los eventos de fin de sesión se retrasan o faltan en Currents? {#why-are-session-end-events-delayed-or-missing-in-currents}

Los eventos de fin de sesión siguen la programación de carga normal del SDK. El SDK de Braze almacena en caché los datos de sesión localmente y los envía periódicamente en función de la calidad de la red; por ejemplo, aproximadamente cada 10 segundos en una conexión estable. Hasta que el SDK carga el evento, este no aparece en Currents.

Si un usuario cierra la aplicación de forma forzada o se queda sin conexión antes del siguiente envío, el evento de fin de sesión puede llegar tarde o no llegar en absoluto. En iOS, los eventos de fin de sesión a menudo no se envían hasta que la aplicación se vuelve a abrir, porque el SDK no puede enviar datos mientras la aplicación está en segundo plano.

Cuando necesites límites de sesión más oportunos en Currents, llama a `requestImmediateDataFlush()` en puntos del ciclo de vida, como cuando la aplicación pasa a segundo plano o vuelve a primer plano. Para más información, consulta [Carga y descarga de datos]({{site.baseurl}}/developer_guide/getting_started/sdk_overview/#data-upload-and-download) y [El fin de sesión y el inicio de sesión tienen marcas de tiempo similares (iOS)]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log/#session-end-and-session-start-have-similar-timestamps-ios).

### ¿Qué sucede si mi contenedor de almacenamiento no está disponible cuando Currents intenta escribir datos? {#what-happens-if-my-storage-bucket-is-unavailable-when-currents-tries-to-write-data}

Si tu contenedor de almacenamiento no está disponible en el momento de la transferencia de datos, esos datos se pierden. Braze no puede rellenar retroactivamente los eventos que no se entregaron correctamente. Para evitar la pérdida de datos, asegúrate de que tu contenedor de almacenamiento esté disponible y correctamente configurado en todo momento.

### ¿Por qué veo «No tienes derechos restantes de eventos de comportamiento del cliente» al editar mi integración de Currents? {#why-do-i-see-you-do-not-have-any-remaining-customer-behavior-events-entitlements-when-editing-my-currents-integration}

Este mensaje puede aparecer cuando actualizas una integración de Currents existente y tu espacio de trabajo ha alcanzado el límite de derechos para eventos de comportamiento del cliente. Ponte en contacto con tu director de cuentas de Braze para solicitar un derecho o ajustar tu configuración.

### ¿Con qué frecuencia cambia la versión de Currents en la ruta de almacenamiento? {#how-often-does-the-currents-version-in-the-storage-path-change}

El segmento `version=<currents_version>` en la ruta de almacenamiento avanza con cada lanzamiento de Currents en una cadencia mensual (por ejemplo, de `version=6` a `version=7`). Recomendamos leer los archivos de forma recursiva desde la ruta raíz en lugar de codificar un segmento de versión específico, para que tu pipeline recoja automáticamente los datos después de un cambio de versión. Para más detalles sobre el formato de la ruta, consulta [Semántica de entrega de eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/). Para un historial de cambios por versión, consulta el [registro de cambios de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/).

### ¿Por qué faltan `campaign_id` o `canvas_id` en un evento de interacción con mensajes? {#why-are-campaign_id-or-canvas_id-missing-from-a-message-engagement-event}

Dependiendo del tipo de evento y el contexto, un evento de interacción con mensajes puede no estar vinculado a una Campaign o paso en Canvas específico. En esos casos, `campaign_id`, `canvas_id` y los campos de nombre relacionados pueden omitirse de la carga útil del evento. Si no ves esos campos en un evento determinado, verifica si ese tipo de evento y contexto normalmente incluyen identificadores de Campaign o Canvas.