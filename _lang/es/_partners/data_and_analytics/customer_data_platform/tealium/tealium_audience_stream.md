---
nav_title: Tealium AudienceStream
article_title: Tealium AudienceStream
page_order: 2
alias: /partners/tealium_audience_stream/
description: "Este artículo de referencia describe la asociación entre Braze y Tealium, un centro de datos universal que te permite conectar datos móviles, web y alternativos con otras fuentes de terceros."
page_type: partner
search_tag: Partner

---

# Tealium AudienceStream

> Tealium [AudienceStream](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/introduction/) es un motor omnicanal de segmentación de clientes y acción en tiempo real. AudienceStream toma los datos que fluyen hacia EventStream y crea perfiles de visitantes que representan los atributos más importantes de la interacción de tus clientes con tu marca.

La integración de Braze y Tealium aprovecha los perfiles de visitantes de AudienceStream. Los comportamientos compartidos segmentan estos perfiles para crear conjuntos de visitantes con rasgos comunes, conocidos como audiencias. Estas audiencias pueden ayudar a alimentar tu stack tecnológico de marketing en tiempo real mediante conectores.

{% alert important %}
Tealium AudienceStreams y EventStreams ofrecen acciones de conector por lotes y no por lotes. El conector no por lotes debe utilizarse cuando las solicitudes en tiempo real sean importantes para el caso de uso y no haya preocupación por alcanzar las especificaciones del límite de velocidad de la API de Braze. Ponte en contacto con el [soporte]({{site.baseurl}}/braze_support) de Braze o con tu administrador de éxito de cliente si tienes alguna pregunta.
{% endalert %}

## Requisitos previos {#prerequisites}

| Nombre | Descripción |
| ---- | ----------- |
| Cuenta de Tealium | Se requiere una [cuenta de Tealium](https://my.tealiumiq.com/) con acceso del lado del servidor. También recomendamos usar las integraciones del lado del cliente para aprovechar esta asociación. |
| Clave de API REST | Una clave de API REST de Braze con permisos `users.track`, `users.delete` y `subscription.status.set`.<br><br>Se puede crear en **Panel de Braze > Consola para desarrolladores > Clave de API REST > Crear nueva clave de API**|
| [Endpoint REST de Braze]({{site.baseurl}}/api/basics#endpoints) | La URL de tu endpoint REST. Tu endpoint dependerá de la [URL de Braze para tu instancia]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Configurar atributos y señales {#step-1-set-up-attributes-and-badges}

#### Comprender los atributos {#understanding-attributes}

El primer paso para usar AudienceStream es crear atributos. Los atributos te permiten definir las características importantes que representan los hábitos, preferencias, acciones y participación de un visitante con tu marca.

**Atributos de visita**: Los atributos de visita se refieren a la visita (o sesión) actual del usuario. Los datos almacenados en estos atributos persisten durante toda la visita. Algunos ejemplos de atributos de visita incluyen:
- Duración de la visita (Number)
- Navegador actual (String)
- Dispositivo actual (String)
- Recuento de páginas vistas (Number)

**Atributos de visitante**: Los atributos de visitante se refieren al usuario actual. Los datos almacenados en estos atributos persisten durante toda la vida del usuario. Algunos ejemplos de atributos de visitante incluyen:
- Valor de pedidos de por vida (Number)
- Nombre (String)
- Fecha de nacimiento (Date)
- Marcas de compras (Tally)

Visita [Tealium](https://docs.tealium.com/server-side/attributes/about/) para obtener una lista completa de los tipos de datos disponibles.

##### Enriquecimiento de atributos {#attribute-enrichment}

Una vez que identifiques los atributos que deseas, puedes configurarlos con [enriquecimientos](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/attributes-enrichments/): reglas de negocio que determinan cuándo y cómo actualizar los valores de los atributos. Cada tipo de dato ofrece su propia selección de enriquecimientos para manipular el valor del atributo. Esto se asocia con la configuración "WHEN". Las siguientes opciones están disponibles para cada atributo de visita y visitante:

- Nuevo visitante: ocurre la primera vez que un visitante llega a tu sitio.
- Nueva visita: ocurre en una nueva visita de un visitante.
- Cualquier evento: ocurre en cualquier evento.
- Visita finalizada: ocurre cuando una visita termina.

También puedes crear una condición personalizada, llamada regla, que determinará cuándo ocurrirá el enriquecimiento.

#### Señales {#badges}

Las señales son atributos especiales de visitante que representan patrones de comportamiento valiosos. Las señales se asignan o eliminan de los visitantes en función de la lógica de sus enriquecimientos. Esta lógica generalmente combina múltiples condiciones para capturar segmentos de visitantes o establece un umbral para cuando se alcanza un valor particular.

#### Ejemplo de atributo y señal {#attribute-and-badge-example}

{% tabs local %}
{% tab Atributo %}

Crea un atributo de visitante "Lifetime Order Value" que calcule el monto acumulativo gastado (`order_total`) por el cliente para todos los pedidos completados (evento de compra). Para configurar el valor de pedidos de por vida en tu cuenta de Tealium, sigue las siguientes instrucciones:

1. Navega a **AudienceStream > Visitor/Visit Attributes** y haz clic en **Add Attribute**.
2. Selecciona el ámbito como **Visitor** y haz clic en **Continue**.
3. Selecciona el tipo de dato **Number** y haz clic en **Continue**.
4. Introduce el nombre del atributo, "Lifetime Order Value".
5. Haz clic en **Add Enrichment** y selecciona **Increment or Decrement Number**.
6. Selecciona el atributo que contiene el valor a incrementar (`order_total`).
7. Deja el "WHEN" configurado en "Any Event", luego haz clic en **Create a New Rule**.
8. Crea una regla que identifique cuándo ha ocurrido un evento de compra.
9. Haz clic en **Save** y luego en **Finish**.

Ahora, todos los clientes tendrán un atributo de valor de pedidos de por vida asociado a ellos.

{% endtab %}
{% tab Señal %}

Puedes crear señales que te ayuden a clasificar y dirigirte a tus usuarios por ciertos atributos que comparten. En el siguiente ejemplo, creamos una señal VIP para usuarios con un "Lifetime Order Value" superior a $500.

1. Navega a **AudienceStream > Visitor/Visit Attributes** y haz clic en **Add Attribute**.
2. Selecciona el ámbito como **Visitor** y haz clic en **Continue**.
3. Selecciona el tipo de dato **Badge** y haz clic en **Continue**.
4. Introduce el nombre de la señal, "VIP".
5. Haz clic en **Add Enrichment** y selecciona **Assign Badge**.
6. Deja el "WHEN" configurado en "Any Event".
7. Crea una regla para la asignación de la señal seleccionando **Create Rule**. Asigna un título a esta regla y, usando el atributo creado anteriormente, configura la regla como "...has attribute "Lifetime Order Value greater than 500".
8. Haz clic en **Save** y luego en **Finish**.

{% endtab %}
{% endtabs %}

### Paso 2: Crear una audiencia {#step-2-create-an-audience}

Desde la página de inicio de Tealium, selecciona **Audiences** en **AudienceStream** en la barra de navegación lateral. Aquí puedes crear una audiencia de usuarios con atributos comunes. La entrada o salida de un usuario de esta audiencia será el desencadenador de la acción del conector, configurada en el siguiente paso, que pasa esta información al perfil de usuario en Braze.

Primero, nombra tu audiencia y luego considera qué atributos serían aplicables al tipo de audiencia que intentas crear. Por ejemplo, para crear una audiencia de usuarios VIP, podrías crear una audiencia de visitantes que tengan la **señal VIP**.

Asegúrate de hacer clic en **Save / Publish** en tu audiencia cuando termines.

### Paso 3: Crear un conector de eventos {#step-3-create-an-event-connector}

Un conector es una integración entre Tealium y otro proveedor utilizada para transmitir datos. Estos conectores contienen acciones que representan las API compatibles de su partner.

1. Desde la barra lateral en Tealium, en **Server-Side**, navega a **AudienceStream > Audience Connectors**.
2. Selecciona el botón azul **+ Add Connector** para explorar el marketplace de conectores. En el nuevo cuadro de diálogo que aparece, usa la búsqueda para encontrar el conector **Braze**.
3. Para agregar este conector, haz clic en el mosaico del conector **Braze**. Al hacer clic, puedes ver el resumen de la conexión y una lista de la información requerida, las acciones compatibles y las instrucciones de configuración. La configuración comprende tres pasos: origen, configuración y acción.

#### Origen {#source}

En el cuadro de diálogo **Source** que aparece, selecciona la audiencia que creaste en el paso anterior y un desencadenador que consideres apropiado para tu situación. También puedes activar el límite de frecuencia para controlar con qué frecuencia se desencadena esta acción.

![Configuración del origen del conector de Tealium AudienceStream con selección de audiencia y desencadenador.]({% image_buster /assets/img/tealium/create_source.png %}){: style="max-width:90%;"}

#### Configuración {#configuration}

A continuación, aparecerá un cuadro de diálogo de **Configuration**. Selecciona **Add Connector** en la parte inferior de la página. Nombra tu conector y proporciona aquí tu endpoint de API de Braze y tu clave de API REST de Braze.

![Cuadro de diálogo de configuración del conector de Tealium con campos de endpoint de Braze y clave de API REST.]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

Si has creado un conector anteriormente, opcionalmente puedes usar uno existente de la lista de conectores disponibles y modificarlo para adaptarlo a tus necesidades con el ícono del lápiz o eliminarlo con el ícono de la papelera.

Después de haber creado o seleccionado un conector para vincular esta audiencia, haz clic en Done para continuar.

#### Acción {#action}

A continuación, nombra la acción de tu conector y selecciona un tipo de acción que enviará datos de acuerdo con el mapeado que configures. Aquí, mapearás atributos de Braze con nombres de atributos de Tealium. Dependiendo del tipo de acción que elijas, habrá una selección variada de campos requeridos por Tealium. A continuación se muestran ejemplos y explicaciones de estos campos.

{% alert important %}
No todos los campos ofrecidos son obligatorios.

![Panel de mapeado de acciones de Tealium mostrando campos opcionales que se pueden minimizar.]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Seguimiento de usuario - Por lotes y sin lotes %}

Esta acción te permite rastrear atributos de usuario, eventos y compras, todo en una sola acción. Aunque la acción de seguimiento de usuario es la misma tanto para AudienceStream como para EventStream, Tealium recomienda configurar los mapeados de atributos de usuario con acciones de AudienceStream y los mapeados de eventos y compras con acciones de EventStream.

| Parámetros | Descripción |
| ---------- | ----------- |
| ID de usuario | Usa este campo para mapear el campo de ID de usuario de Tealium a su equivalente en Braze. Mapea uno o más atributos de ID de usuario. Cuando se especifican varios ID, se selecciona el primer valor no vacío en función del siguiente orden de prioridad: ID externo, Braze ID, nombre de alias y etiqueta de alias.<br><br>- El ID externo y el Braze ID no deben especificarse si se importan tokens de notificaciones push.<br>- Si se especifica un alias de usuario, se deben configurar tanto el nombre de alias como la etiqueta de alias. <br><br>Para más información, consulta el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) de Braze. |
| Atributos de usuario | Usa los nombres de campos existentes del perfil de usuario de Braze para actualizar los valores del perfil de usuario en el panel de Braze o agrega tus propios datos de [atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object) personalizados a los perfiles de usuario.<br><br>- Por defecto, se crean nuevos usuarios si no existe uno.<br>- Al configurar **Update Existing Only** en `true`, solo se actualizan los usuarios existentes y no se crea ningún usuario nuevo.<br>- Si un atributo de Tealium está vacío, se convierte en nulo y se elimina del perfil de usuario de Braze. Los enriquecimientos deben usarse si los valores nulos no deben enviarse a Braze para eliminar un atributo de usuario. |
| Modificar atributos de usuario | Usa este campo para incrementar o decrementar ciertos atributos de usuario.<br><br>- Los atributos de tipo entero pueden incrementarse con enteros positivos o negativos.<br>- Los atributos de tipo arreglo pueden modificarse agregando o eliminando valores de los arreglos existentes. |
| Evento | Un evento representa una ocurrencia única de un evento personalizado por un usuario particular en un momento dado. Usa este campo para rastrear y mapear atributos de eventos como los del [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object) de Braze. <br><br>- El atributo de evento `Name` es obligatorio para cada evento mapeado.<br>- El atributo de evento `Time` se configura automáticamente como ahora a menos que se mapee explícitamente. <br>- Por defecto, se crean nuevos eventos si no existe uno. Al configurar `Update Existing Only` en `true`, solo se actualizan los eventos existentes y no se crea ningún evento nuevo.<br>- Mapea atributos de tipo arreglo para agregar múltiples eventos. Los atributos de tipo arreglo deben tener la misma longitud.<br>- Los atributos de valor único pueden usarse y se aplican a cada evento. |
| Plantilla de evento | Proporciona plantillas de eventos para ser referenciadas en los datos del cuerpo. Las plantillas pueden usarse para transformar datos antes de enviarlos a Braze. Consulta la [Guía de plantillas](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) de Tealium para más información. |
| Variable de plantilla de evento | Proporciona variables de plantilla de evento como entrada de datos. Consulta la [Guía de variables de plantilla](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) de Tealium para más información. |
| Compra | Usa este campo para rastrear y mapear atributos de compra del usuario como los del [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object) de Braze.<br><br>- Los atributos de compra `Product ID`, `Currency` y `Price` son obligatorios para cada compra mapeada.<br>- El atributo de compra `Time` se configura automáticamente como ahora a menos que se mapee explícitamente.<br>- Por defecto, se crean nuevas compras si no existe una. Al configurar `Update Existing Only` en `true`, solo se actualizan las compras existentes y no se crea ninguna compra nueva.<br>- Mapea atributos de tipo arreglo para agregar múltiples artículos de compra. Los atributos de tipo arreglo deben tener la misma longitud.<br>- Los atributos de valor único pueden usarse y se aplican a cada artículo. |
| Plantilla de compra | Las plantillas pueden usarse para transformar datos antes de enviarlos a Braze.<br>- Define una plantilla de compra si necesitas soporte de objetos anidados.<br>- Cuando se define una plantilla de compra, se ignorará la configuración establecida en la sección de compras de tu acción.<br>- Consulta la [Guía de plantillas](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) de Tealium para más información. |
| Variable de plantilla de compra | Proporciona variables de plantilla de producto como entrada de datos. Consulta la [Guía de variables de plantilla](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) de Tealium para más información. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Acción" }

![Ejemplo de acción de seguimiento de usuario de Tealium con atributos de usuario mapeados y campos de evento.]({% image_buster /assets/img/tealium/track_user_example2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Eliminar usuario - Sin lotes %}

Esta acción te permite eliminar usuarios del panel de Braze.

| Parámetros | Descripción |
| ---------- | ----------- |
| ID de usuario | Usa este campo para mapear el campo de ID de usuario de Tealium a su equivalente en Braze.<br><br>- Mapea uno o más atributos de ID de usuario. Cuando se especifican varios ID, se selecciona el primer valor no vacío en función del siguiente orden de prioridad: ID externo, Braze ID, nombre de alias y etiqueta de alias.<br>- Al especificar un alias de usuario, se deben configurar tanto el nombre de alias como la etiqueta de alias.<br><br>Para más información, consulta el [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Acción" }

![Acción de eliminación de usuario de Tealium con mapeados de ID de usuario de Braze configurados.]({% image_buster /assets/img/tealium/track_user_delete2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Actualizar estado del grupo de suscripción de usuario - Sin lotes %}
Esta acción te permite agregar o eliminar usuarios de los grupos de suscripción de SMS o correo electrónico de Braze.

| Parámetros | Descripción |
| ---------- | ----------- |
| Tipo de grupo | Usa este campo para indicar si se trata de un grupo de suscripción de SMS o correo electrónico. |
| Tipo de actualización | Mapea esta acción a un evento de cancelación de suscripción o de suscripción. |
| Atributos | - ID del grupo de suscripción (obligatorio): el ID del grupo de suscripción relacionado con el tipo de grupo mapeado en el campo anterior.<br>- ID externo: el ID externo del usuario.<br><br>Específico del grupo de correo electrónico:<br>- Correo electrónico: la dirección de correo electrónico del usuario.<br>**Si el ID externo no está definido, el correo electrónico será obligatorio.**<br><br>Específico del grupo de SMS:<br>- Teléfono: el número de teléfono en formato E.164. Por ejemplo, +14155552671.<br>**Si el ID externo no está definido, el teléfono será obligatorio.** |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Acción" }

![Acción de actualización del estado del grupo de suscripción de Tealium con mapeados de tipo de grupo y tipo de actualización.]({% image_buster /assets/img/tealium/update_subscription.png %}){: style="max-width:90%"}

{% endtab %}
{% endtabs %}

Selecciona **Finish**.

#### Resumen {#summary}

Visualiza el resumen del conector que creaste. Si deseas modificar las opciones elegidas, selecciona **Back** para editar o **Finish** para completar.

Tu conector ahora se muestra en la lista de conectores en la página de inicio de Tealium.

Asegúrate de guardar o publicar tu conector cuando termines. Las acciones que configuraste ahora se activarán cuando se cumplan las conexiones de los desencadenadores.

### Paso 4: Probar tu conector de Tealium {#step-4-test-your-tealium-connector}

Después de que tu conector esté configurado y en funcionamiento, debes probarlo para asegurarte de que funciona correctamente. La forma más sencilla de probarlo es usar la herramienta **Trace** de Tealium. Para empezar a usar Trace, asegúrate de haber agregado la extensión de navegador de Tealium Tools.

1. Para iniciar una nueva traza, selecciona **Trace** en la barra lateral en las opciones de **Server-Side**. Haz clic en **Start** y captura el Trace ID.
2. Abre la extensión del navegador e introduce el Trace ID en AudienceStream Trace.
3. Examina el registro en tiempo real.
4. Busca la acción que deseas validar haciendo clic en la entrada de **Actions Triggered** para expandirla.
5. Busca la acción que deseas validar y visualiza el estado del registro.

Consulta la [documentación de Trace](https://docs.tealium.com/server-side/connectors/trace/about/) de Tealium para obtener instrucciones más detalladas sobre la implementación de la herramienta Trace de Tealium.

## Demostración de la integración {#integration-demo}

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" title="Demostración de la integración de Tealium AudienceStream" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Posibles excedentes de puntos de datos {#potential-data-point-overages}

Hay tres formas principales en las que podrías alcanzar accidentalmente excedentes de datos al integrar Braze a través de Tealium:

### Envío de datos duplicados: envía solo deltas de atributos a Braze {#sending-duplicate-data-only-send-braze-deltas-of-attributes}
Tealium no envía a Braze deltas de atributos de usuario. Por ejemplo, si tienes una acción de EventStream que rastrea el nombre, el correo electrónico y el número de teléfono móvil de un usuario, Tealium enviará los tres atributos a Braze cada vez que se desencadene la acción. Tealium no buscará qué cambió o se actualizó para enviar solo esa información.<br><br>
**Solución**: <br>Puedes revisar tu backend para evaluar si un atributo ha cambiado o no y, de ser así, llamar a los métodos relevantes de Tealium para actualizar el perfil de usuario. **Esto es lo que suelen hacer los usuarios que integran Braze directamente.** <br>**O**<br> Si no almacenas tu propia versión de un perfil de usuario en tu backend y no puedes saber si los atributos cambian o no, puedes usar AudienceStream y [crear enriquecimientos](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/) para enviar atributos de usuario solo cuando los valores hayan cambiado.

#### Envío de datos irrelevantes o sobrescritura innecesaria de datos {#sending-irrelevant-data-or-needlessly-overwriting-data}
Si tienes varios EventStreams que apuntan al mismo feed de eventos, **todas las acciones habilitadas para ese conector** se activarán automáticamente cada vez que se desencadene una sola acción, **lo que también podría resultar en la sobrescritura de datos en Braze.**<br><br>
**Solución**: <br>Configura una especificación de eventos o un feed separado para rastrear cada acción. <br>**O**<br> Desactiva las acciones (o conectores) que no quieras que se activen utilizando los alternadores en el panel de Tealium.

#### Inicializar Braze demasiado pronto {#initializing-braze-too-early}
Si estás integrando con Tealium usando la etiqueta del SDK Web de Braze, es posible que veas un aumento drástico en tus MAU. **Si Braze se inicializa al cargar la página, Braze creará un perfil anónimo cada vez que un usuario web navegue al sitio web por primera vez.** Esto incluye el tráfico de bots, lo que puede inflar tu recuento de usuarios activos. Algunos pueden querer rastrear el comportamiento de los usuarios solo cuando hayan completado alguna acción, como "Inició sesión" o "Vio un video", para reducir su recuento de MAU. <br><br>
**Solución**: <br>Configura [reglas de carga](https://docs.tealium.com/iq-tag-management/load-rules/about/) para determinar exactamente cuándo y dónde se carga una etiqueta en tu sitio. Para obtener orientación más completa sobre el filtrado de tráfico de bots y la inicialización condicional del SDK, consulta [Filtrado de tráfico de bots]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_bot-filtering).