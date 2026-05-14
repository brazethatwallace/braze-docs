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
Tealium AudienceStreams y EventStreams ofrecen acciones de conector por lotes y no por lotes. El conector no por lotes debe utilizarse cuando las solicitudes en tiempo real sean importantes para el caso de uso y no haya preocupación por alcanzar las especificaciones del límite de velocidad de la API de Braze. Ponte en contacto con el [soporte]({{site.baseurl}}/braze_support/) de Braze o con tu administrador del éxito del cliente si tienes alguna pregunta.
{% endalert %}

## Requisitos previos {#prerequisites}

| Nombre | Descripción |
| ---- | ----------- |
| Cuenta Tealium | Se necesita una [cuenta Tealium](https://my.tealiumiq.com/) con acceso del lado del servidor. Recomendamos utilizar también las integraciones del lado del cliente para aprovechar esta asociación. |
| Clave de API REST | Una clave de API REST de Braze con permisos `users.track`, `users.delete` y `subscription.status.set`.<br><br>Se puede crear en **panel de Braze > Consola para desarrolladores > Clave de API REST > Crear nueva clave de API** |
| [Punto de conexión REST de Braze]({{site.baseurl}}/api/basics/#endpoints) | La URL de tu punto de conexión REST. Tu punto de conexión dependerá de la [URL de Braze de tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración {#integration}

### Paso 1: Configurar atributos y señales {#step-1-set-up-attributes-and-badges}

#### Comprensión de los atributos {#understanding-attributes}

El primer paso para utilizar AudienceStream es crear atributos. Los atributos te permiten definir las características importantes que representan los hábitos, preferencias, acciones e interacción de un visitante con tu marca.

**Atributos de la visita**: Los atributos de visita se refieren a la visita (o sesión) actual del usuario. Los datos almacenados en estos atributos persisten mientras dura la visita. Algunos ejemplos de atributos de visita son:
- Duración de la visita (número)
- Navegador actual (cadena)
- Dispositivo actual (cadena)
- Número de páginas vistas (número)

**Atributos del visitante**: Los atributos del visitante se refieren al usuario actual. Los datos almacenados en estos atributos persisten durante toda la vida del usuario. Algunos ejemplos de atributos del visitante son:
- Valor de pedido de por vida (número)
- Nombre (cadena)
- Fecha de nacimiento (fecha)
- Marcas de compras (Tally)

Visita [Tealium](https://docs.tealium.com/server-side/attributes/about/) para consultar la lista completa de tipos de datos disponibles.

##### Enriquecimiento de atributos {#attribute-enrichment}

Una vez identificados los atributos deseados, puedes configurarlos con [enriquecimientos](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/attributes-enrichments/): reglas empresariales que determinan cuándo y cómo actualizar los valores de los atributos. Cada tipo de dato ofrece su propia selección de enriquecimientos para manipular el valor del atributo. Esto está asociado a la configuración "WHEN". Las siguientes opciones están disponibles para cada atributo de visita y visitante:

- New Visitor: se produce la primera vez que un visitante entra en tu sitio.
- New Visit: se produce en una nueva visita de un visitante.
- Any Event: se produce en cualquier evento.
- Visit Ended: se produce cuando termina una visita.

También puedes crear una condición personalizada, llamada regla, que determinará cuándo se producirá el enriquecimiento.

#### Señales {#badges}

Las señales son atributos especiales de los visitantes que representan patrones de comportamiento valiosos. Las señales se asignan o retiran a los visitantes en función de la lógica de sus enriquecimientos. Esta lógica suele combinar varias condiciones para captar segmentos de visitantes o establece un umbral para cuando se alcanza un valor concreto.

#### Ejemplo de atributo y señal {#attribute-and-badge-example}

{% tabs local %}
{% tab Atributo %}

Crea un atributo de visitante "Lifetime Order Value" que calcule el importe acumulado gastado (`order_total`) por el cliente para todos los pedidos completados (evento de compra). Para configurar el valor de pedido de por vida en tu cuenta de Tealium, sigue las siguientes instrucciones:

1. Ve a **AudienceStream > Visitor/Visit Attributes** y haz clic en **Add Attribute**.
2. Selecciona el ámbito como **Visitor** y haz clic en **Continue**.
3. Selecciona el tipo de dato **Number** y haz clic en **Continue**.
4. Introduce el nombre del atributo, "Lifetime Order Value".
5. Haz clic en **Add Enrichment** y selecciona **Increment or Decrement Number**.
6. Selecciona el atributo que contiene el valor a incrementar (`order_total`).
7. Deja "WHEN" en "Any Event" y, a continuación, haz clic en **Create a New Rule**.
8. Crea una regla que identifique cuándo se ha producido un evento de compra.
9. Haz clic en **Save** y luego en **Finish**.

Ahora, todos los clientes tendrán un atributo de valor de pedido de por vida vinculado a ellos.

{% endtab %}
{% tab Señal %}

Puedes crear señales que te ayuden a clasificar y dirigirte a tus usuarios por determinados atributos que comparten. En el siguiente ejemplo, creamos una señal VIP para usuarios con un "Lifetime Order Value" superior a 500 $.

1. Ve a **AudienceStream > Visitor/Visit Attributes** y haz clic en **Add Attribute**.
2. Selecciona el ámbito como **Visitor** y haz clic en **Continue**.
3. Selecciona el tipo de dato **Badge** y haz clic en **Continue**.
4. Introduce el nombre de la señal, "VIP".
5. Haz clic en **Add Enrichment** y selecciona **Assign Badge**.
6. Deja "WHEN" en "Any Event".
7. Crea una regla para asignar la señal seleccionando **Create Rule**. Asigna un título a esta regla y, utilizando el atributo creado anteriormente, establece la regla como "...has attribute "Lifetime Order Value greater than 500".
8. Haz clic en **Save** y luego en **Finish**.

{% endtab %}
{% endtabs %}

### Paso 2: Crear una audiencia {#step-2-create-an-audience}

En la página de inicio de Tealium, selecciona **Audiences** en **AudienceStream** en la barra lateral de navegación. Aquí puedes crear una audiencia de usuarios con atributos comunes. La entrada o salida de un usuario de esta audiencia será el desencadenante de la acción del conector, configurada en el paso siguiente, que pasa esta información al perfil de usuario en Braze.

En primer lugar, nombra tu audiencia y, a continuación, considera qué atributos se aplicarían al tipo de audiencia que intentas crear. Por ejemplo, para crear una audiencia de usuarios VIP, podrías crear una audiencia de visitantes que tengan la **señal VIP**.

Asegúrate de **Save / Publish** tu audiencia cuando hayas terminado.

### Paso 3: Crear un conector de eventos {#step-3-create-an-event-connector}

Un conector es una integración entre Tealium y otro proveedor utilizada para transmitir datos. Estos conectores contienen acciones que representan las API compatibles de su socio.

1. En la barra lateral de Tealium, en **Server-Side**, ve a **AudienceStream > Audience Connectors**.
2. Selecciona el botón azul **+ Add Connector** para buscar en el mercado de conectores. En el nuevo cuadro de diálogo que aparece, utiliza la búsqueda rápida para encontrar el conector **Braze**.
3. Para añadir este conector, haz clic en la ficha del conector **Braze**. Al hacer clic, puedes ver el resumen de la conexión y una lista de la información necesaria, las acciones admitidas y las instrucciones de configuración. La configuración consta de tres pasos: origen, configuración y acción.

#### Fuente {#source}

En el cuadro de diálogo **Source** que aparece, selecciona la audiencia que creaste en el paso anterior y un desencadenante que consideres adecuado para tu situación. También puedes activar el límite de frecuencia para controlar la frecuencia con la que se desencadena esta acción.

![]({% image_buster /assets/img/tealium/create_source.png %}){: style="max-width:90%;"}

#### Configuración {#configuration}

A continuación, aparecerá un diálogo de **Configuration**. Selecciona **Add Connector** en la parte inferior de la página. Da un nombre a tu conector y proporciona aquí tu punto de conexión de la API de Braze y tu clave de API REST de Braze.

![]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

Si ya has creado un conector anteriormente, puedes utilizar uno existente de la lista de conectores disponibles y modificarlo para adaptarlo a tus necesidades con el icono del lápiz o eliminarlo con el icono de la papelera.

Cuando hayas creado o seleccionado un conector para vincular esta audiencia, haz clic en Done para continuar.

#### Acción {#action}

A continuación, asigna un nombre a tu acción de conector y selecciona un tipo de acción que envíe datos según el mapeado que configures. Aquí mapearás atributos de Braze con nombres de atributos de Tealium. Dependiendo del tipo de acción que elijas, habrá una selección variada de campos requeridos por Tealium. A continuación se dan ejemplos y explicaciones de estos campos.

{% alert important %}
No todos los campos ofrecidos son obligatorios.

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Track User - Batch and Non-Batch %}

Esta acción te permite realizar un seguimiento de los atributos de usuario, evento y compra en una sola acción. Aunque la acción Track User es la misma para AudienceStream y EventStream, Tealium recomienda configurar los mapeados de atributos de usuario con acciones de AudienceStream y los mapeados de eventos y compras con acciones de EventStream.

| Parámetros | Descripción |
| ---------- | ----------- |
| ID de usuario | Utiliza este campo para mapear el campo de ID de usuario de Tealium a su equivalente en Braze. Mapea uno o más atributos de ID de usuario. Cuando se especifican varios ID, se elige el primer valor que no está en blanco según el siguiente orden de prioridad: ID externo, ID de Braze, nombre de alias y etiqueta de alias.<br><br>- El ID externo y el ID de Braze no deben especificarse si se importan tokens de notificaciones push.<br>- Si se especifica un alias de usuario, deben establecerse el nombre de alias y la etiqueta de alias. <br><br>Para más información, consulta el [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze. |
| Atributos del usuario | Utiliza los nombres de campo de perfil de usuario de Braze existentes para actualizar los valores de perfil de usuario en el panel de Braze o añade tus propios datos de [atributo de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens) personalizado a los perfiles de usuario.<br><br>- Por defecto, se crearán nuevos usuarios si no existe ninguno.<br>- Si configuras **Update Existing Only** en `true`, solo se actualizarán los usuarios existentes y no se creará ningún usuario nuevo.<br>- Si un atributo de Tealium está vacío, se convertirá en nulo y se eliminará del perfil de usuario de Braze. Los enriquecimientos deben utilizarse si no deben enviarse valores nulos a Braze para eliminar un atributo de usuario. |
| Modificar los atributos del usuario | Utiliza este campo para aumentar o disminuir ciertos atributos de usuario<br><br>- Los atributos enteros pueden incrementarse con enteros positivos o negativos.<br>- Los atributos de matrices pueden modificarse añadiendo o eliminando valores de las matrices existentes. |
| Evento | Un evento representa una ocurrencia única de un evento personalizado por un usuario particular en una marca de tiempo. Utiliza este campo para rastrear y mapear atributos de evento como los del [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object/) de Braze. <br><br>- El atributo de evento `Name` es obligatorio para cada evento mapeado.<br>- El atributo de evento `Time` se establece automáticamente en now a menos que se mapee explícitamente. <br>- Por defecto, se crearán nuevos eventos si no existe ninguno. Si configuras `Update Existing Only` en `true`, solo se actualizarán los eventos existentes y no se creará ningún evento nuevo.<br>- Mapea atributos de tipo array para añadir múltiples eventos. Los atributos de tipo array deben tener la misma longitud.<br>- Se pueden utilizar atributos de valor único y aplicarlos a cada evento. |
| Plantilla de eventos | Proporciona plantillas de eventos a las que hacer referencia en los datos del cuerpo. Las plantillas pueden utilizarse para transformar los datos antes de enviarlos a Braze. Consulta la [guía de plantillas](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) de Tealium para obtener más información. |
| Variable de plantilla de evento | Proporciona variables de plantilla de eventos como entrada de datos. Consulta la [guía de variables de plantilla](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) de Tealium para obtener más información. |
| Compra | Utiliza este campo para rastrear y mapear atributos de compra del usuario como los del [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) de Braze.<br><br>- Los atributos de compra `Product ID`, `Currency` y `Price` son obligatorios para cada compra mapeada.<br>- El atributo de compra `Time` se establece automáticamente en now a menos que se mapee explícitamente.<br>- Por defecto, se crearán nuevas compras si no existe ninguna. Si configuras `Update Existing Only` en `true`, solo se actualizarán las compras existentes y no se creará ninguna compra nueva.<br>- Mapea atributos de tipo array para añadir múltiples artículos de compra. Los atributos de tipo array deben tener la misma longitud.<br>- Se pueden utilizar atributos de valor único y se aplicarán a cada artículo. |
| Plantilla de compra | Las plantillas pueden utilizarse para transformar los datos antes de enviarlos a Braze.<br>- Define una plantilla de compra si necesitas compatibilidad con objetos anidados.<br>- Cuando se define una plantilla de compra, la configuración establecida en la sección de compras de tu acción será ignorada.<br>- Consulta la [guía de plantillas](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) de Tealium para obtener más información. |
| Variable de plantilla de compra | Proporciona variables de plantilla de productos como entrada de datos. Consulta la [guía de variables de plantilla](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) de Tealium para obtener más información. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_example2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Delete User - Non-Batch %}

Esta acción te permite eliminar usuarios del panel de Braze.

| Parámetros | Descripción |
| ---------- | ----------- |
| ID de usuario | Utiliza este campo para mapear el campo de ID de usuario de Tealium a su equivalente en Braze.<br><br>- Mapea uno o más atributos de ID de usuario. Cuando se especifican varios ID, se elige el primer valor que no está en blanco según el siguiente orden de prioridad: ID externo, ID de Braze, nombre de alias y etiqueta de alias.<br>- Al especificar un alias de usuario, deben establecerse tanto el nombre de alias como la etiqueta de alias.<br><br>Para más información, consulta el [punto de conexión `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) de Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_delete2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Update User Subscription Group Status - Non-Batch %}
Esta acción te permite añadir o eliminar usuarios de los grupos de suscripción por SMS o correo electrónico de Braze.

| Parámetros | Descripción |
| ---------- | ----------- |
| Tipo de grupo | Utiliza este campo para indicar si se trata de un grupo de suscripción por SMS o correo electrónico. |
| Tipo de actualización | Mapea esta acción a un evento de cancelación de suscripción o de suscripción. |
| Atributos | - ID del grupo de suscripción (obligatorio): el ID del grupo de suscripción relacionado con el tipo de grupo mapeado en el campo anterior.<br>- ID externo: el ID externo del usuario.<br><br>Específico del grupo de correo electrónico:<br>- Correo electrónico: la dirección de correo electrónico del usuario.<br>**Si el ID externo no está definido, se requerirá el correo electrónico.**<br><br>Específico del grupo de SMS:<br>- Teléfono: el número de teléfono en formato E.164. Por ejemplo, +14155552671.<br>**Si el ID externo no está definido, se requerirá el teléfono.** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/update_subscription.png %}){: style="max-width:90%"}

{% endtab %}
{% endtabs %}

Selecciona **Finish**.

#### Resumen {#summary}

Visualiza el resumen del conector que has creado. Si quieres modificar las opciones elegidas, selecciona **Back** para editar o **Finish** para terminar.

Tu conector aparece ahora en la lista de conectores de tu página de inicio de Tealium.

Asegúrate de guardar o publicar tu conector cuando hayas terminado. Las acciones que configuraste se dispararán ahora cuando se cumplan las conexiones desencadenantes.

### Paso 4: Prueba tu conector de Tealium {#step-4-test-your-tealium-connector}

Una vez que el conector esté en funcionamiento, debes probarlo para asegurarte de que funciona correctamente. La forma más sencilla de comprobarlo es utilizar la herramienta **Trace** de Tealium. Para empezar a utilizar Trace, asegúrate de que has añadido la extensión de navegador Tealium Tools.

1. Para iniciar un nuevo rastreo, selecciona **Trace** en la barra lateral, en las opciones de **Server-Side**. Haz clic en **Start** y captura el ID de Trace.
2. Abre la extensión del navegador e introduce el ID de Trace en AudienceStream Trace.
3. Examina el registro en tiempo real.
4. Comprueba la acción que deseas validar haciendo clic en la entrada **Actions Triggered** para expandirla.
5. Busca la acción que quieras validar y visualiza el estado del registro.

Consulta la [documentación de Trace](https://docs.tealium.com/server-side/connectors/trace/about/) de Tealium para obtener instrucciones más detalladas sobre la implementación de la herramienta Trace de Tealium.

## Demostración de integración {#integration-demo}

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" title="Demostración de integración de Tealium AudienceStream" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Posibles excedentes de puntos de datos {#potential-data-point-overages}

Hay tres formas principales en las que puedes incurrir accidentalmente en excedentes de datos al integrar Braze a través de Tealium:

#### Envío de datos duplicados: envía solo deltas de atributos a Braze {#sending-duplicate-data-only-send-braze-deltas-of-attributes}
Tealium no envía deltas de atributos de usuario a Braze. Por ejemplo, si tienes una acción de EventStream que realiza un seguimiento del nombre, correo electrónico y número de móvil de un usuario, Tealium enviará los tres atributos a Braze cada vez que se desencadene la acción. Tealium no buscará lo que ha cambiado o se ha actualizado para enviar solo esa información.<br><br>
**Solución**: <br>Puedes comprobar tu backend para evaluar si un atributo ha cambiado o no y, en caso afirmativo, llamar a los métodos pertinentes de Tealium para actualizar el perfil del usuario. **Esto es lo que suelen hacer los usuarios que integran Braze directamente.** <br>**O**<br> Si no almacenas tu propia versión de un perfil de usuario en tu backend y no puedes saber si los atributos cambian o no, puedes utilizar AudienceStream y [crear enriquecimientos](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/) para enviar solo los atributos de usuario cuando los valores hayan cambiado.

#### Enviar datos irrelevantes o sobrescribir datos innecesariamente {#sending-irrelevant-data-or-needlessly-overwriting-data}
Si tienes varios EventStreams dirigidos a la misma fuente de eventos, **todas las acciones habilitadas para ese conector** se dispararán automáticamente cada vez que se desencadene una sola acción, **lo que también podría provocar que los datos se sobrescribieran en Braze.**<br><br>
**Solución**: <br>Configura una especificación de evento o fuente independiente para realizar un seguimiento de cada acción. <br>**O**<br> Desactiva las acciones (o conectores) que no quieras que se activen utilizando los botones del dashboard de Tealium.

#### Inicializar Braze demasiado pronto {#initializing-braze-too-early}
Los usuarios que se integren con Tealium utilizando la etiqueta del SDK web de Braze pueden ver un aumento espectacular de sus MAU. **Si Braze se inicializa al cargar la página, Braze creará un perfil anónimo cada vez que un usuario web navegue por el sitio web por primera vez.** Esto incluye el tráfico de bots, lo que puede inflar tu recuento de usuarios activos. Algunos pueden querer rastrear el comportamiento del usuario solo cuando los usuarios han completado alguna acción, como "Iniciar sesión" o "Ver vídeo", para reducir su recuento de MAU. <br><br>
**Solución**: <br>Configura [reglas de carga](https://docs.tealium.com/iq-tag-management/load-rules/about/) para determinar exactamente cuándo y dónde se carga una etiqueta en tu sitio. Para obtener orientación más completa sobre el filtrado de tráfico de bots y la inicialización condicional del SDK, consulta [Filtrado de tráfico de bots]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_bot-filtering).