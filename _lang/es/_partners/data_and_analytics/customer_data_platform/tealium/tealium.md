---
nav_title: Tealium
article_title: Tealium
page_order: 1
alias: /partners/tealium/
description: "Este artículo de referencia describe la asociación entre Braze y Tealium, un centro de datos universal que te permite conectar datos móviles, web y alternativos con otras fuentes de terceros."
page_type: partner
search_tag: Partner

---

# Tealium

> [Tealium](https://tealium.com/) es un centro de datos universal y una plataforma de datos de los clientes compuesta por EventStream, AudienceStream e iQ Tag Management que te permite conectar datos móviles, web y alternativos de fuentes de terceros. La conexión de Tealium con Braze permite un flujo de datos de eventos personalizados, atributos de usuario y compras que te permiten actuar sobre tus datos en tiempo real.

![Un gráfico resumen de Tealium que muestra cómo encajan los distintos productos de Tealium y la plataforma Braze para activar campañas multicanal en tiempo real.]({% image_buster /assets/img/tealium/tealium_overview.png %}){: style="border:0;"}

La integración de Braze y Tealium te permite realizar un seguimiento de tus usuarios y enviar datos a varios proveedores de análisis de usuarios. Tealium te permite:
- Sincronizar las audiencias de Tealium con [AudienceStream]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_audience_stream/) a Braze para utilizarlas en la personalización de Campaigns y Canvas de Braze o en la creación de segmentos.
- [Importar datos entre plataformas](#choose-your-integration-type). Braze ofrece tanto una integración [en paralelo](#side-by-side-sdk-integration) de SDK para tus aplicaciones Android, iOS y web, como una integración [de servidor a servidor](#server-to-server-integration) que puede utilizarse en cualquier plataforma que pueda informar de datos de eventos.<br><br>

{% tabs %}
{% tab EventStream %}
Tealium EventStream es un centro de recopilación de datos y API que se sitúa en el centro de tus datos. EventStream gestiona toda la cadena de suministro de datos, desde la configuración y la instalación hasta la identificación, validación y mejora de los datos de usuario entrantes. EventStream actúa en tiempo real con fuentes de eventos y conectores. Las siguientes son las características que componen el [EventStream](https://docs.tealium.com/server-side/getting-started/eventstream-api-hub/introduction/).
- Fuentes de datos (instalación y recopilación de datos)
- Eventos en directo (inspección de datos en tiempo real)
- Especificaciones y atributos de los eventos (requisitos y validación de la capa de datos)
- Fuentes de eventos (tipos de eventos filtrados)
- Conectores de eventos (acciones del centro de API)

{% endtab %}
{% tab AudienceStream %}

Tealium AudienceStream es un motor omnicanal de segmentación de clientes y acción en tiempo real. AudienceStream toma los datos que fluyen hacia EventStream y crea perfiles de visitantes que representan los atributos más importantes de la interacción de tus clientes con tu marca. Consulta nuestro artículo sobre [AudienceStream]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_audience_stream/) para conocer los pasos de configuración.

{% endtab %}
{% tab iQ Tag Management %}
Tealium iQ te permite activar código en tus aplicaciones utilizando una etiqueta en la interfaz de usuario de gestión de etiquetas de Tealium iQ. Esta etiqueta recopilará, controlará y entregará datos de eventos de plataformas móviles y web, lo que te permitirá configurar una implementación nativa de Braze sin añadir código específico de Braze a tus aplicaciones. Los usuarios pueden optar por integrar Mobile Remote Commands a través de iQ Tag Management o archivos de configuración JSON (enfoque recomendado de Tealium). Los usuarios que utilicen Braze Web SDK deben realizar la integración a través de la etiqueta web iQ.

Para saber más sobre los pros y los contras de cada método, consulta la siguiente sección del [administrador de etiquetas Tealium iQ](#mobile-remote-commands).
{% endtab %}
{% endtabs %}

{% alert important %}
Tealium ofrece acciones de conector por lotes y no por lotes. El conector no por lotes debe utilizarse cuando las solicitudes en tiempo real sean importantes para el caso de uso y no haya preocupación por alcanzar las especificaciones del límite de velocidad de la API de Braze. Ponte en contacto con soporte de Braze o con tu administrador del éxito del cliente si tienes alguna pregunta.<br><br>

En el caso de los conectores por lotes, las solicitudes se ponen en cola hasta que se alcanza uno de los siguientes umbrales:<br><br>
- Número máximo de solicitudes: 75
- Tiempo máximo desde la solicitud más antigua: 10 minutos
- Tamaño máximo de las solicitudes: 1 MB

Tealium no procesa por lotes los eventos de consentimiento (preferencias de suscripción) ni los eventos de eliminación de usuarios de forma predeterminada.
{% endalert %}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Tealium | Para beneficiarse de esta asociación, es necesario disponer de una [cuenta Tealium](https://my.tealiumiq.com/) con acceso al servidor y/o al cliente. |
| Fuente instalada y [bibliotecas](https://docs.tealium.com/platforms/) fuente de Tealium | El origen de los datos enviados a Tealium, como aplicaciones móviles, sitios web o servidores backend.<br><br>Debes instalar las bibliotecas en tu aplicación, sitio o servidor antes de poder configurar correctamente un conector Tealium. |
| Punto de conexión REST y SDK de Braze | La URL de tu punto de conexión REST o SDK. Tu punto de conexión dependerá de la [URL de Braze de tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
| Clave de identificación de la aplicación Braze (solo en paralelo) | La clave de identificación de tu aplicación. <br><br>Se encuentra en **panel de Braze > Administrar configuración > Clave de API**. |
| Versión del código (solo en paralelo) | Corresponde a la versión del SDK y debe estar en formato major.minor (por ejemplo, 3.2 y no 3.0.1). La versión del código debe ser 3.0 o superior. |
| Clave de API REST (solo de servidor a servidor) | Una clave de API REST de Braze con permisos `users.track` y `users.delete`. <br><br>Se puede crear en **panel de Braze > Consola para desarrolladores > Clave de API REST > Crear nueva clave de API**.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Elige tu tipo de integración {#choose-your-integration-type}

| Integración | Detalles |
| ----------- | ------- |
| [En paralelo](#side-by-side-sdk-integration) | Utiliza el SDK de Tealium para traducir los eventos a las llamadas nativas de Braze, lo que permite acceder a características más profundas y un uso más completo de Braze que la integración de servidor a servidor.<br><br>Si piensas utilizar comandos remotos de Braze, ten en cuenta que Tealium no admite todos los métodos de Braze (por ejemplo, Content Cards). Para utilizar un método de Braze que no esté mapeado a través de un comando remoto correspondiente, tendrás que invocar el método añadiendo código nativo de Braze a tu código base.|
| [De servidor a servidor](#server-to-server-integration) | Reenvía los datos de Tealium a los puntos finales de la REST API de Braze.<br><br>No es compatible con las funciones de la interfaz de usuario de Braze, como la mensajería dentro de la aplicación, Content Cards o las notificaciones push. También existen datos capturados automáticamente, como los campos a nivel de dispositivo, que no están disponibles a través de este método.<br><br>Considera una integración en paralelo si deseas utilizar estas características.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración de SDK en paralelo {#side-by-side-sdk-integration}

### Comandos remotos {#remote-commands}

Los comandos remotos son una función de las bibliotecas Tealium para iOS y Android que permiten realizar llamadas desde el SDK de Tealium —a través de los servidores de Braze— a Braze. El módulo de comandos remotos de Braze instalará y creará automáticamente las bibliotecas de Braze necesarias y se encargará de toda la renderización de mensajes y el seguimiento analítico. Para utilizar el comando remoto móvil de Braze, necesitarás tener instaladas las bibliotecas de Tealium en tus aplicaciones.

Tealium ofrece dos formas de integrar Mobile Remote Command; no hay pérdida de funcionalidad entre los tipos de integración y el código nativo subyacente es idéntico.

| Método de comando remoto móvil | Pros | Contras |
| --- | --- | --- |
| **Etiqueta de comando remoto** | Modifica fácilmente los mapeados y los datos enviados al comando remoto mediante la interfaz de usuario de Tealium iQ.<br><br>Esto nos permite enviar datos o eventos adicionales a un SDK de terceros después de que la aplicación ya esté en la tienda de aplicaciones, sin que el cliente tenga que actualizar la aplicación. | El módulo de gestión de etiquetas de la aplicación se basa en una webview oculta para procesar JavaScript. |
| **Archivo de configuración JSON**<br>([Recomendado](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#how-it-works)) | Utilizar el método JSON elimina la necesidad de tener una webview oculta en la aplicación y reduce enormemente el consumo de memoria.<br><br>El archivo JSON puede alojarse de forma remota o local dentro de la aplicación del cliente. | Por el momento, no hay interfaz de usuario para gestionar esto, por lo que requiere un poco de esfuerzo adicional.<br><br>Nota: Tealium está trabajando en la adición de una interfaz de usuario de gestión que resolverá este problema y aportará el mismo nivel de flexibilidad a los comandos remotos JSON que tienen con la versión de gestión de iQ Tag. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Utiliza los mapeados de datos de comandos remotos móviles de Braze para establecer atributos de usuario predeterminados y atributos personalizados, y realizar un seguimiento de las compras y los eventos personalizados. Consulta la tabla siguiente para conocer los métodos de Braze correspondientes.

| Comando remoto | Método de Braze |
| -------------- | ------------ |
| appendcustomarrayattribute | addToCustomAttributeArrayWithKey()|
| emailnotification | setEmailNotificationSubscriptionType() |
| incrementcustomattribute | incrementCustomAttribute() |
| initialize | startWithApiKey() |
| logcustomevent | logCustomEvent() |
| logpurchase | logPurchase() |
| pushnotification | setPushNotificationSubscriptionType() |
| removecustomattribute | setCustomAttributeWithKey() |
| setcustomattribute | setCustomAttributeArrayWithKey() |
| setcustomarrayattribute | setCustomAttributeArrayWithKey() |
| setlastknownlocation | setLastKnownLocationWithLatitude() |
| unsetcustomattribute | unsetCustomAttributeWithKey() |
| useralias | addAlias() |
| userattribute | ABKUser() |
| useridentifier | changeUser() |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Puedes encontrar más detalles sobre cómo configurar el comando remoto móvil de Braze y una descripción general de los métodos compatibles en la documentación para desarrolladores de Tealium:
- [Comando remoto](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#json-template)
- [Etiqueta de comando remoto](https://docs.tealium.com/client-side-tags/braze-mobile-remote-command-tag/)

{% alert important %}
Los comandos remotos móviles de Braze no son compatibles con todos los métodos y canales de mensajería de Braze (por ejemplo, Content Cards). Para utilizar un método de Braze que no esté mapeado a través de un comando remoto correspondiente, tendrás que invocar el método directamente añadiendo código nativo de Braze a tu código base.
{% endalert%}

### Etiqueta de Braze Web SDK {#braze-web-sdk-tag}

Utiliza la etiqueta de Braze Web SDK para desplegar el SDK de Braze Web en tu sitio web. [Tealium iQ Tag Management](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/) permite a los clientes añadir Braze como etiqueta dentro del dashboard de Tealium para realizar un seguimiento de la actividad de los visitantes. Los especialistas en marketing suelen utilizar las etiquetas para conocer la eficacia de la publicidad en línea, el marketing por correo electrónico y la personalización de sitios web.

1. En Tealium, ve a **iQ > Tags > + Add Tag > Braze Web SDK**.
2. En el cuadro de diálogo de configuración de etiquetas, introduce la clave de API (tu clave de identificador de la aplicación Braze), la URL base (punto de conexión del SDK de Braze) y la [versión del código del SDK de Braze Web](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md). También puedes habilitar el registro para registrar información en la consola web con fines de depuración.
3. En el cuadro de diálogo de [reglas de carga](https://docs.tealium.com/iq-tag-management/load-rules/about/), elige "Load on All Pages" o selecciona **Create Rule** para determinar cuándo y dónde cargar una instancia de esta etiqueta en tu sitio.
4. En el cuadro de diálogo de **[Data Mappings](https://docs.tealium.com/iq-tag-management/data-mappings/about/)**, selecciona **Create Mappings** para asignar datos de Tealium a Braze. Las variables de destino de la etiqueta de Braze Web SDK están integradas en la pestaña **Data Mapping** de la etiqueta. En [las tablas siguientes](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/) se enumeran las categorías de destino disponibles y se describe cada nombre de destino.
5. Selecciona **Finish**.

### Recursos de integración en paralelo {#side-by-side-integrations-resources}

- Comando remoto iOS: [Documentación de Tealium](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [repositorio GitHub de Tealium](https://github.com/Tealium/tealium-ios-braze-remote-command)
- Comando remoto Android: [Documentación de Tealium](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [repositorio GitHub de Tealium](https://github.com/Tealium/tealium-android-braze-remote-command)
- Etiqueta Web SDK: [Documentación de Tealium](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)

## Integración de servidor a servidor {#server-to-server-integration}

Esta integración reenvía datos de Tealium a la REST API de Braze.

La integración de servidor a servidor no es compatible con las funciones de la interfaz de usuario de Braze, como la mensajería dentro de la aplicación, Content Cards o las notificaciones push. También existen datos capturados automáticamente (como los campos a nivel de dispositivo) que no están disponibles a través de este método.

Si deseas utilizar estos datos y estas características, considera nuestra integración de SDK [en paralelo]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium/#side-by-side-sdk-integration).

### Paso 1: Configurar una fuente {#step-1-set-up-a-source}

Tealium requiere que primero configures una fuente de datos válida para que tu conector se nutra de ella.
1. En la barra lateral de Tealium, en **Server-Side**, ve a **Sources > Data Sources > + Add Data Source**.
2. Localiza la plataforma que desees dentro de las categorías disponibles y nombra tu fuente; este es un campo obligatorio.<br>![]({% image_buster /assets/img/tealium/data_source.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
3. En las opciones de **Event Specifications**, elige las [especificaciones de eventos](https://docs.tealium.com/server-side/event-specifications/about/) que deseas incluir. Las especificaciones de eventos te ayudan a identificar los nombres de los eventos y los atributos necesarios para realizar un seguimiento en tu instalación. Estas especificaciones se aplicarán a los eventos entrantes.<br>![]({% image_buster /assets/img/tealium/event_specs.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>Tómate un tiempo para pensar qué datos son más valiosos para ti y qué especificaciones parecen las más adecuadas para tu caso de uso. También hay disponibles [especificaciones personalizadas de eventos](https://docs.tealium.com/iq-tag-management/events/about/). <br>
4. El siguiente diálogo avanza al paso **Get Code**. El código base y el código de seguimiento de eventos proporcionados aquí te servirán de guía para la instalación. Descarga el PDF proporcionado si deseas compartir estas instrucciones con tu equipo. Selecciona **Save & Continue** cuando hayas terminado.<br>
5. Ahora podrás ver tu fuente guardada, así como añadir o eliminar especificaciones de eventos. <br>![]({% image_buster /assets/img/tealium/braze_connection.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>Desde la vista detallada de la fuente de datos puedes realizar las siguientes acciones:
- Ver y copiar la clave de la fuente de datos
- Ver instrucciones de instalación
- Volver a la página **Get Code**
- Añadir o eliminar especificaciones de eventos
- Navegar para ver los eventos en directo relacionados con una especificación de evento
- Y más...<br>
6. Por último, selecciona **Save / Publish** en la parte superior de la página. Si no publicas tu fuente, no podrás encontrarla al configurar tu conector de Braze.

Consulta [Data Sources](https://docs.tealium.com/server-side/data-sources/about-data-sources/) para obtener más instrucciones sobre cómo configurar y editar tu fuente de datos.

### Paso 2: Crear un conector de eventos {#step-2-create-an-event-connector}

Un conector es una integración entre Tealium y otro proveedor utilizada para transmitir datos. Estos conectores contienen acciones que representan las API compatibles de sus socios.

1. Desde la barra lateral en Tealium, en **Server-Side**, ve a **EventStream > Event Connectors**.
2. Selecciona el botón azul **+ Add Connector** para buscar en el mercado de conectores. En el nuevo cuadro de diálogo que aparece, utiliza la búsqueda rápida para encontrar el conector **Braze**.
3. Para añadir este conector, haz clic en la ficha del conector **Braze**. Al hacer clic, puedes ver el resumen de la conexión y una lista de la información necesaria, las acciones admitidas y las instrucciones de configuración. La configuración consta de tres pasos: fuente, configuración y acción.

#### Fuente {#source}

Una vez configurada la fuente, vuelve a la página del conector de Braze en **EventStream** > **Event Connectors** > **+ Add Connector** > **Braze**.

A continuación, selecciona la fuente de datos que acabas de crear y, en **Event Feed**, selecciona **All Events** o una especificación de eventos concreta, la ruta recomendada para enviar a Braze solo los valores modificados. Selecciona **Continue**.

#### Configuración {#configuration}

A continuación, selecciona **Add Connector** en la parte inferior de la página. Da un nombre a tu conector y proporciona aquí tu punto de conexión de la API de Braze y tu clave de API REST de Braze.

![]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

Si ya has creado un conector anteriormente, puedes utilizar uno existente de la lista de conectores disponibles y modificarlo para adaptarlo a tus necesidades con el icono del lápiz o eliminarlo con el icono de la papelera.

#### Acción {#action}

A continuación, asigna un nombre a tu acción de conector y selecciona un tipo de acción que enviará datos según el mapeado que configures. Aquí, asignarás atributos, eventos y compras de Braze a nombres de atributos, eventos y compras de Tealium.

{% alert important %}
No todos los campos ofrecidos son obligatorios.

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Seguimiento de usuario - Por lotes y no por lotes %}

Esta acción te permite realizar un seguimiento de los atributos de usuario, evento y compra en una sola acción.

| Parámetros | Descripción |
| ---------- | ----------- |
| ID de usuario | Utiliza este campo para asignar el campo de ID de usuario de Tealium a su equivalente en Braze. Asigna uno o más atributos de ID de usuario. Cuando se especifican varios ID, se elige el primer valor que no está en blanco según el siguiente orden de prioridad: ID externo, ID de Braze, nombre de alias y etiqueta de alias.<br><br>- El ID externo y el ID de Braze no deben especificarse si se importan tokens de notificaciones push.<br>- Si se especifica un alias de usuario, deben establecerse el nombre de alias y la etiqueta de alias. <br><br>Para más información, consulta el [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze. |
| Atributos del usuario | Utiliza los nombres de campo de perfil de usuario de Braze existentes para actualizar los valores de perfil de usuario en el dashboard de Braze o añade tus propios datos de [atributo de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens) personalizado a los perfiles de usuario.<br><br>- De forma predeterminada, se crearán nuevos usuarios si no existe ninguno.<br>- Si configuras **Update Existing Only** en `true`, solo se actualizarán los usuarios existentes y no se creará ningún usuario nuevo.<br>- Si un atributo de Tealium está vacío, se convertirá en nulo y se eliminará del perfil de usuario de Braze. Los enriquecimientos deben utilizarse si no deben enviarse valores nulos a Braze para eliminar un atributo de usuario. |
| Modificar los atributos del usuario | Utiliza este campo para aumentar o disminuir ciertos atributos de usuario.<br><br>- Los atributos enteros pueden incrementarse con enteros positivos o negativos.<br>- Los atributos de matrices pueden modificarse añadiendo o eliminando valores de las matrices existentes. |
| Evento | Un evento representa una ocurrencia única de un evento personalizado por un usuario particular en una marca de tiempo. Utiliza este campo para rastrear y asignar atributos de evento como los del [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object/) de Braze. <br><br>- El atributo de evento `Name` es obligatorio para cada evento asignado.<br>- El atributo de evento `Time` se establece automáticamente en la hora actual a menos que se asigne explícitamente. <br>- De forma predeterminada, se crearán nuevos eventos si no existe ninguno. Si configuras `Update Existing Only` en `true`, solo se actualizarán los eventos existentes y no se creará ningún evento nuevo.<br>- Asigna atributos de tipo array para añadir múltiples eventos. Los atributos de tipo array deben tener la misma longitud.<br>- Se pueden utilizar atributos de valor único y se aplicarán a cada evento. |
| Plantilla de eventos | Proporciona plantillas de eventos a las que hacer referencia en los datos del cuerpo. Las plantillas pueden utilizarse para transformar los datos antes de enviarlos a Braze. Consulta la [guía de plantillas](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) de Tealium para obtener más información. |
| Variable de plantilla de evento | Proporciona variables de plantilla de eventos como entrada de datos. Consulta la [guía de variables de plantilla](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) de Tealium para obtener más información. |
| Compra | Utiliza este campo para rastrear y asignar atributos de compra del usuario como los del [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) de Braze.<br><br>- Los atributos de compra `Product ID`, `Currency` y `Price` son obligatorios para cada compra mapeada.<br>- El atributo de compra `Time` se establece automáticamente en la hora actual a menos que se asigne explícitamente.<br>- De forma predeterminada, se crearán nuevas compras si no existe ninguna. Si configuras `Update Existing Only` en `true`, solo se actualizarán las compras existentes y no se creará ninguna compra nueva.<br>- Asigna atributos de tipo array para añadir múltiples artículos de compra. Los atributos de tipo array deben tener la misma longitud.<br>- Se pueden utilizar atributos de valor único y se aplicarán a cada artículo.|
| Plantilla de compra | Las plantillas pueden utilizarse para transformar los datos antes de enviarlos a Braze.<br>- Define una plantilla de compra si necesitas compatibilidad con objetos anidados.<br>- Cuando se define una plantilla de compra, la configuración establecida en la sección de compras de tu acción será ignorada.<br>- Consulta la [guía de plantillas](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) de Tealium para obtener más información.|
| Variable de plantilla de compra | Proporciona variables de plantilla de productos como entrada de datos. Consulta la [guía de variables de plantilla](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) de Tealium para obtener más información. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_example.png %})

{% endtab %}
{% tab Eliminar usuario - No por lotes %}

Esta acción te permite eliminar usuarios del dashboard de Braze.

| Parámetros | Descripción |
| ---------- | ----------- |
| ID de usuario | Utiliza este campo para asignar el campo de ID de usuario de Tealium a su equivalente en Braze. <br><br>- Asigna uno o más atributos de ID de usuario. Cuando se especifican varios ID, se elige el primer valor que no está en blanco según el siguiente orden de prioridad: ID externo, ID de Braze, nombre de alias y etiqueta de alias.<br>- Al especificar un alias de usuario, deben establecerse tanto el nombre de alias como la etiqueta de alias.<br><br>Para más información, consulta el [punto de conexión `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) de Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_delete.png %})

Si deseas modificar las opciones elegidas, selecciona **Back** para editar o **Finish** para completar.

{% endtab %}
{% endtabs %}

Selecciona **Continue**.

Tu conector aparece ahora en la lista de conectores de tu página de inicio de Tealium. <br>![]({% image_buster /assets/img/tealium/summary_list.png %}){: style="max-width:80%;"}

Asegúrate de seleccionar **Save / Publish** para tu conector cuando hayas terminado. Las acciones que configuraste se dispararán ahora cuando se cumplan las conexiones desencadenantes.

### Paso 3: Prueba tu conector de Tealium {#step-3-test-your-tealium-connector}

Una vez que el conector esté en funcionamiento, debes probarlo para asegurarte de que funciona correctamente. La forma más sencilla de comprobarlo es utilizar la herramienta **Trace** de Tealium. Para empezar a utilizar Trace, asegúrate de que has añadido la extensión de navegador Tealium Tools.

1. Para iniciar una nueva traza, selecciona **Trace** en la barra lateral, en las opciones de **Server-Side**. Selecciona **Start** y captura el ID de rastreo.
2. Abre la extensión del navegador e introduce el ID de rastreo en AudienceStream Trace.
3. Examina el registro en tiempo real.
4. Busca la acción que quieras validar seleccionando la entrada **Actions Triggered** para ampliarla.
5. Busca la acción que quieras validar y visualiza el estado del registro.

Consulta la [documentación de Trace](https://docs.tealium.com/server-side/connectors/trace/about/) de Tealium para obtener instrucciones más detalladas sobre la implementación de la herramienta Trace de Tealium.

## Demostración de integración {#integration-demo}

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1mP84vVWifzNMN7eMYNORNy0y-WZurzBs/view?usp=sharing" title="Demostración de integración de Tealium" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Posibles excedentes de puntos de datos {#potential-data-point-overages}

Hay tres formas principales de registrar accidentalmente puntos de datos innecesarios al integrar Braze a través de Tealium:

#### Envío de datos duplicados: envía solo deltas de atributos de Braze {#sending-duplicate-data-only-send-braze-deltas-of-attributes}

Tealium no envía deltas de atributos de usuario a Braze. Por ejemplo, si tienes una acción de EventStream que rastrea el nombre, el correo electrónico y el número de teléfono móvil de un usuario, Tealium enviará los tres atributos a Braze cada vez que se active la acción. Tealium no buscará lo que ha cambiado o se ha actualizado para enviar solo esa información.

**Solución**: <br>Puedes comprobar tu backend para evaluar si un atributo ha cambiado o no y, en caso afirmativo, llamar a los métodos pertinentes de Tealium para actualizar el perfil del usuario. **Esto es lo que suelen hacer los usuarios que integran Braze directamente.** <br>**O**<br> Si no almacenas tu propia versión de un perfil de usuario en tu backend y no puedes saber si los atributos cambian o no, puedes utilizar AudienceStream y
[crear enriquecimientos](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/) para enviar atributos de usuario solo cuando los valores hayan cambiado. Consulta la documentación de Tealium sobre las [reglas de enriquecimiento](https://docs.tealium.com/server-side-connectors/braze-connector/).

#### Envío de datos irrelevantes o sobrescritura innecesaria de datos {#sending-irrelevant-data-or-needlessly-overwriting-data}

Si tienes varios EventStreams dirigidos a la misma fuente de eventos, **todas las acciones habilitadas para ese conector** se dispararán automáticamente cada vez que se desencadene una sola acción. Esto también podría provocar que se sobrescribieran datos en Braze y se registraran puntos de datos innecesarios.

**Solución**: <br>Configura una especificación de evento o fuente independiente para realizar un seguimiento de cada acción. <br>**O**<br> Desactiva las acciones (o conectores) que no quieras que se activen utilizando los botones del dashboard de Tealium.

#### Inicializar Braze demasiado pronto {#initializing-braze-too-early}

Si te integras con Tealium utilizando la etiqueta de Braze Web SDK, puedes ver un aumento espectacular de tus MAU. **Si Braze se inicializa al cargar la página, Braze creará un perfil anónimo cada vez que un usuario web navegue por el sitio web por primera vez.** Esto incluye el tráfico de bots, lo que puede inflar tu recuento de usuarios activos. Algunos pueden querer rastrear el comportamiento del usuario solo cuando los usuarios han completado alguna acción, como "Iniciar sesión" o "Ver vídeo", para reducir su recuento de MAU.

**Solución**: <br>Configura [reglas de carga](https://docs.tealium.com/iq-tag-management/load-rules/about/) para determinar exactamente cuándo y dónde se carga una etiqueta en tu sitio. Para obtener una guía más completa sobre el filtrado de tráfico de bots y la inicialización condicional del SDK, consulta [Filtrado de tráfico de bots]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_bot-filtering).