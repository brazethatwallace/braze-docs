---
nav_title: Zeotap Symphony
description: "Este artículo de referencia describe la asociación entre Braze y Zeotap, una plataforma de datos de los clientes de nueva generación que proporciona resolución de identidades, información y enriquecimiento."
page_type: partner
search_tag: Partner
page_order: 2
---

# Zeotap Symphony

La integración de Braze y Zeotap Symphony te permite crear orquestaciones en tiempo real y ejecutar campañas de correo electrónico y notificaciones push.

- Envía nombres y apellidos a través de Zeotap, a partir de los cuales los usuarios pueden enviar correos electrónicos personalizados a través de Braze.
- Envía eventos personalizados o un evento de compra en tiempo real a través de Zeotap, a partir de los cuales los usuarios pueden crear activadores de campañas dentro de Braze para dirigirse a sus clientes.

{% alert note %}
Para crear campañas de marketing por correo electrónico, incorpora los correos electrónicos sin procesar a Zeotap asignándolos a `Email Raw` en el catálogo de Zeotap.
{% endalert %}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Nombre del cliente | Este es tu nombre de cliente para tu cuenta de Braze. Puedes encontrarlo navegando hasta la consola de Braze. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Instancia | Tu instancia de Braze se puede obtener a través de tu administrador de incorporación de Braze o en la [página de resumen de la API]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Esta sección proporciona información sobre los dos métodos de integración con Braze:

### Método 1 {#method-1}
En este método, tienes que realizar las siguientes tareas:
1. Integra el SDK de Braze en tu sitio web o aplicación.
2. Integra Braze con Zeotap a través de Symphony.

- `User traits` deben asignarse a los respectivos campos de Braze en la pestaña **Data To Send**. Si asignas los atributos `Event` y `Purchase`, se producirá una duplicación de eventos dentro de Braze.
- Asigna `External ID` a `User ID` configurado al configurar el SDK de Braze.

Cuando la integración se haya configurado correctamente, podrás crear campañas de correo electrónico y notificaciones push basadas en atributos personalizados enviados a Braze a través de Symphony.

### Método 2 {#method-2}
Con este método, puedes integrar Braze con Zeotap a través de Symphony.

- Este método no es compatible con las características de la interfaz de usuario de Braze, como la mensajería dentro de la aplicación, Content Cards o las notificaciones push.
- Zeotap recomienda asignar el `hashed email` disponible en el catálogo de Zeotap al `External ID`.

Cuando la integración se haya configurado correctamente, solo podrás crear campañas de correo electrónico basadas en atributos personalizados enviados a Braze a través de Symphony.

## Flujo de datos a Braze e identificadores compatibles {#data-flow-to-braze-and-supported-identifiers}

Los datos fluirán de Zeotap a Braze utilizando el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Los siguientes puntos resumen el flujo de datos:

1. Zeotap envía atributos de perfil de usuario, atributos personalizados, eventos personalizados y campos de compra.
2. Asignas todos los campos relevantes del catálogo de Zeotap a los campos de Braze en la pestaña **Data To Send**.
3. A continuación, los datos se cargan en Braze.

Puedes encontrar información detallada sobre los distintos atributos en la sección [Data To Send](#data-to-send-tab).

## Configuración del destino {#destination-setup}

Después de aplicar filtros o añadir una condición para tus usuarios en Symphony, puedes activarlos en Braze en **Send to Destinations**. Se abrirá una nueva ventana en la que podrás configurar tu destino. Puedes utilizar un destino existente de la lista de **Available Destinations** o crear uno nuevo.

### Añadir nuevo destino {#add-new-destination}
Realiza los siguientes pasos para añadir un nuevo destino:
1. Selecciona **Add New Destination**.
2. Busca **Braze**.
3. Añade el **Client Name**, la **API Key** y la **Instance** y guarda el destino.

El destino se crea y se pone a disposición en **Available Destinations**.

### Añadir entradas a nivel de flujo de trabajo {#add-workflow-level-inputs}
Después de crear un destino, lo siguiente es añadir entradas a nivel de flujo de trabajo, como se describe en esta sección.
1. Elige el destino en la lista de destinos disponibles utilizando la función de búsqueda.
2. Los campos **Client Name**, **API Key** e **Instance** se rellenan automáticamente en función del valor introducido al crear el destino.
3. Introduce el **Audience Name** que deseas crear para este nodo de flujo de trabajo. Se envía como **atributo personalizado** a Braze.
4. Completa la asignación de catálogo a destino en la pestaña **Data To Send**. A continuación encontrarás información detallada sobre cómo realizar la asignación.

### Pestaña Data To Send {#data-to-send-tab}
La pestaña **Data To Send** te permite asignar los campos del catálogo de Zeotap a los campos de Braze que pueden enviarse a Braze. La asignación puede realizarse de una de las siguientes maneras:
- **Asignación estática** - Hay determinados campos que Zeotap asigna automáticamente a los campos de Braze correspondientes, como correo electrónico, teléfono, nombre, apellidos, etc.<br>
- **Selección desplegable** - Asigna los campos relevantes ingestados en Zeotap a los campos de Braze proporcionados en el menú desplegable.<br>![Varios rasgos del usuario configurados en Zeotap, como idioma, ciudad, cumpleaños, etc.]({% image_buster /assets/img/zeotap/zeotap7.png %}){: style="max-width:70%;"}<br>
- **Entrada de datos personalizados** - Añade datos personalizados asignados al campo de Zeotap correspondiente y envíalos a Braze.<br>![Seleccionando "loyalty_points" como rasgo de usuario en Zeotap.]({% image_buster /assets/img/zeotap/zeotap8.png %}){: style="max-width:70%;"}

## Atributos admitidos {#supported-attributes}
En esta sección puedes encontrar información detallada sobre todos los campos de Braze.

| Campo de Braze | Tipo de asignación | Descripción |
| --- | --- | --- |
| ID externo | Selección desplegable | Este es el `User ID` persistente definido por Braze para rastrear a los usuarios a través de dispositivos y plataformas. Te recomendamos que asignes `User ID` a `External ID`; de lo contrario, Zeotap puede enviar el correo electrónico como alias de usuario.<br><br>Zeotap te recomienda que asignes el `hashed email` disponible en el catálogo de Zeotap al `External ID`. |
| Correo electrónico | Asignación estática | Está asignado a `Email Raw` en el catálogo de Zeotap. |
| Teléfono | Asignación estática | Está asignado a `Mobile Raw` en el catálogo de Zeotap.<br><br>• Braze acepta números de teléfono en formato `E.164`. Zeotap no realiza ninguna transformación. Por lo tanto, debes introducir los números de teléfono en el formato prescrito. Para más información, consulta [Números de teléfono de usuario]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers). |
| Nombre | Asignación estática | Está asignado a `First Name` en el catálogo de Zeotap. |
| Apellido | Asignación estática | Está asignado a `Last Name` en el catálogo de Zeotap. |
| Género | Asignación estática | Está asignado a `Gender` en el catálogo de Zeotap. |
| Nombre de evento personalizado | Asignación estática | Está asignado a `Event Name` en el catálogo de Zeotap.<br><br>Tanto el nombre del evento personalizado como la marca de tiempo del evento personalizado deben estar asignados para capturar eventos personalizados en Braze. El evento personalizado no se puede procesar si no se asigna alguno de los dos. Para más información, consulta el [objeto evento]({{site.baseurl}}/api/objects_filters/event_object#what-is-an-event-object). |
| Marca de tiempo de evento personalizado | Asignación estática | Está asignado a `Event Timestamp` en el catálogo de Zeotap.<br><br>Tanto el nombre del evento personalizado como la marca de tiempo del evento personalizado deben estar asignados para capturar eventos personalizados en Braze. El evento personalizado no se puede procesar si no se asigna alguno de los dos. Para más información, consulta el [objeto evento]({{site.baseurl}}/api/objects_filters/event_object#what-is-an-event-object). |
| Suscripción por correo electrónico | Selección desplegable | Incorpora un campo `Email Marketing Preference` y asígnalo.<br><br>Zeotap envía los tres valores siguientes:<br>• `opted_in` - Indica que el usuario se ha registrado explícitamente para la preferencia de marketing por correo electrónico.<br>• `unsubscribed` - Indica que el usuario ha optado explícitamente por no recibir mensajes de correo electrónico.<br>• `subscribed` - Indica que el usuario no se ha adherido ni se ha excluido voluntariamente. |
| Suscripción push | Selección desplegable | Incorpora un campo `Push Marketing Preference` y asígnalo.<br><br>Zeotap envía los tres valores siguientes:<br>• `opted_in` - Indica que el usuario se ha registrado explícitamente para la preferencia de marketing push.<br>• `unsubscribed` - Indica que el usuario ha optado explícitamente por no recibir mensajes push.<br>• `subscribed` - Indica que el usuario no ha optado ni por la adhesión ni por la exclusión voluntaria. |
| Habilitar el seguimiento de aperturas de correo electrónico | Selección desplegable | Asigna el campo `Marketing Preference` correspondiente.<br><br>Cuando se establece en true, permite añadir un píxel de seguimiento de apertura a todos los futuros correos electrónicos enviados a este usuario. |
| Habilitar el seguimiento de clics de correo electrónico | Selección desplegable | Asigna el campo `Marketing Preference` correspondiente.<br><br>Cuando se establece en true, habilita el seguimiento de clics para todos los enlaces dentro de todos los futuros correos electrónicos enviados a este usuario. |
| ID de producto | Selección desplegable | • Identificador de una acción de compra `(Product Name/Product Category)`. Para más detalles, consulta el [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object).<br>• Incorpora el atributo correspondiente al catálogo de Zeotap y asígnalo.<br><br>`Product ID`, `Currency` y `Price` deben asignarse obligatoriamente para capturar eventos de compra en Braze. El evento de compra no puede llevarse a cabo si falta alguno de los tres. Para más información, consulta el [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object#purchase-object). |
| Divisa | Selección desplegable | • Atributo de moneda para la acción de compra.<br>• El formato compatible es `ISO 4217 Alphabetic Currency Code`.<br>• Incorpora al catálogo de Zeotap los datos de divisa correctamente formateados y asígnalo.<br><br>`Product ID`, `Currency` y `Price` deben asignarse obligatoriamente para capturar eventos de compra en Braze. El evento de compra no puede llevarse a cabo si falta alguno de los tres. |
| Precio | Selección desplegable | • Atributo de precio para la acción de compra.<br>• Incorpora el atributo correspondiente al catálogo de Zeotap y asígnalo.<br><br>`Product ID`, `Currency` y `Price` deben asignarse obligatoriamente para capturar eventos de compra en Braze. El evento de compra no puede llevarse a cabo si falta alguno de los tres. |
| Cantidad | Selección desplegable | • Atributo de cantidad para la acción de compra.<br>• Incorpora el atributo correspondiente al catálogo de Zeotap y asígnalo. |
| País | Selección desplegable | Asígnalo al campo del catálogo `Country` que estás incorporando. |
| Ciudad | Selección desplegable | Asígnalo al campo del catálogo `City` que estás incorporando. |
| Idioma | Selección desplegable | • El formato aceptado es `ISO-639-1` estándar (por ejemplo, en).<br>• Incorpora el idioma correctamente formateado y asígnalo. |
| Fecha de nacimiento | Selección desplegable | Asígnalo al campo `Date of Birth` que estás incorporando. |
| Atributo personalizado | Entrada de datos personalizados | Asigna cualquier atributo de usuario a una entrada de datos personalizada, que luego se envía a Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Atributos admitidos" }

## Visualización de datos en la consola de Braze {#viewing-data-on-braze-console}

Una vez que hayas asignado los atributos relevantes que se enviarán y publicarán en el flujo de trabajo, los eventos empezarán a fluir a Braze en función de los criterios definidos. Puedes buscar por ID de correo electrónico o ID externo en la consola de Braze.

![Vista del perfil de usuario en Braze mostrando los atributos y eventos entrantes de Zeotap.]({% image_buster /assets/img/zeotap/zeotap6.jpg %})

Varios atributos se encuentran en diferentes secciones del panel de usuario en Braze.
- La pestaña **Profile** contiene los atributos del usuario.
- La pestaña **Custom Attributes** contiene los atributos personalizados definidos por el usuario.
- La pestaña **Custom Events** contiene los eventos personalizados definidos por el usuario.
- La pestaña **Purchases** contiene las compras realizadas durante un periodo de tiempo por el usuario.

## Creación de campañas {#campaign-creation}

Los usuarios pueden crear campañas dentro de Braze y activar usuarios en tiempo real o en función de la hora programada. Las campañas pueden activarse en función de las acciones realizadas por el usuario (evento personalizado, compra) o de los atributos del usuario.