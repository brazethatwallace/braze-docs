---
nav_title: Extensión de reenvío de eventos
article_title: Adobe
description: "Este artículo de referencia cubre la extensión de reenvío de eventos de Braze, que te permite aprovechar los datos capturados en Adobe Experience Platform Edge Network y enviarlos a Braze en forma de eventos del lado del servidor."
page_type: partner
page_order: 2
search_tag: Partner
---

# Extensión de reenvío de eventos de la API Track Events {#track-events-api-event-forwarding-extension}

> La extensión de [reenvío de eventos](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en) de la API Braze Track Events te permite aprovechar los datos capturados en Adobe Experience Platform Edge Network y enviarlos a Braze en forma de eventos del lado del servidor utilizando la API [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

Este documento cubre los casos de uso de la extensión, cómo instalarla en tus bibliotecas de reenvío de eventos y cómo emplear sus capacidades en una [regla](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) de reenvío de eventos.

{% alert note %}
El uso del reenvío de eventos de Adobe puede aumentar tu uso de puntos de datos de Braze. Consulta la documentación de Braze sobre [puntos de datos]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#billable-data-points) para obtener más información.
{% endalert %}

## Ejemplos {#use-cases}

Esta extensión debe utilizar datos de Edge Network en Braze para aprovechar sus capacidades de análisis de clientes y segmentación.

Por ejemplo, considera una organización de comercio minorista con presencia multicanal (sitio web y móvil) que captura entradas transaccionales o conversacionales como datos de eventos desde su sitio web y plataformas móviles.

Mediante diversas reglas de [etiquetas](https://experienceleague.adobe.com/docs/experience-platform/tags/home.html?lang=en), estos datos se envían a Edge Network en tiempo real. Desde aquí, la extensión de reenvío de eventos de Braze envía automáticamente los eventos relevantes a Braze desde el lado del servidor.

## Límites de velocidad {#rate-limits}

| API | Límites de velocidad |
| --- | --- |
| User Track | 50.000 solicitudes por minuto.<br><br>Consulta la [documentación de la API de User Track]({{site.baseurl}}/api/endpoints/user_data/post_user_track#rate-limit) para más detalles.
{: .reset-td-br-1 .reset-td-br-2 aria-label="Límites de velocidad" }

## Integración {#integration}

### Paso 1: Recopilar los detalles de configuración necesarios {#step-1-gather-required-configuration-details}

Para conectar Edge Network a Braze, se necesita lo siguiente:

| Tipo de clave | Descripción |
| --- | --- |
| Instancia de Braze | Tu instancia de Braze puede obtenerse de tu administrador de incorporación de Braze o puede encontrarse en la [página de resumen de la API]({{site.baseurl}}/api/basics#endpoints). |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con todos los permisos. <br><br> Esta puede crearse en el panel de Braze desde **Configuración** > **Claves de API**.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 1: Recopilar los detalles de configuración necesarios" }

### Paso 2: Crear un secreto {#step-2-create-a-secret}

Crea un nuevo [secreto de reenvío de eventos](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/secrets.html?lang=en) y establece el valor en tu [clave de API de Braze](https://experienceleague.adobe.com/docs/experience-platform/tags/extensions/server/braze/overview.html?lang=en#configuration-details). Esto se utilizará para autenticar la conexión a tu cuenta manteniendo el valor seguro.

### Paso 3: Instalar y configurar la extensión de Braze {#step-3-install-and-configure-the-braze-extension}

1. Para instalar la extensión, [crea una propiedad de reenvío de eventos](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en#properties) o elige una propiedad existente para editarla.
2. A continuación, selecciona **Extensions** en la navegación izquierda. En la pestaña **Catalog**, selecciona **Install** en la tarjeta de la extensión de Braze.
3. En la siguiente pantalla, introduce tu instancia REST or transferencia de estado representacional y la clave de API, y selecciona **Save** cuando hayas terminado.

### Paso 4: Crear una regla de envío de eventos {#step-4-create-a-send-event-rule}

Después de instalar la extensión, crea una nueva [regla](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) de reenvío de eventos y configura sus condiciones como desees. Al configurar las acciones de la regla, selecciona la extensión **Braze** y luego selecciona **Send Event** como tipo de acción.

![Acción de regla de reenvío de eventos de Adobe configurada para utilizar Braze Send Event.]({% image_buster /assets/img/efe.png %})

{% tabs local %}
{% tab Identificación de usuario %}

| Entrada | Descripción |
| --- | --- |
| ID de usuario externo | Un UUID o GUID largo, aleatorio y bien distribuido. Si eliges un método diferente para nombrar tus ID de usuario, estos también deben ser largos, aleatorios y estar bien distribuidos. Más información sobre las [convenciones sugeridas para nombrar ID de usuario]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web#naming-best-practices). |
| ID de usuario de Braze | Identificador de usuario de Braze. |
| Alias de usuario | Un alias sirve como identificador de usuario único alternativo. Utiliza alias para identificar usuarios a lo largo de dimensiones diferentes a tu ID de usuario principal.<br><br>El objeto de alias de usuario consta de dos partes: un `alias_name` para el identificador en sí y un `alias_label` que indica el tipo de alias. Los usuarios pueden tener múltiples alias con diferentes etiquetas, pero solo un `alias_name` por cada `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 4: Crear una regla de envío de eventos" }

{% alert note %}
Para vincular el evento a un usuario, debes completar el campo `External User ID`, el campo `Braze User Identifier` o la sección `User Alias`.
{% endalert %}

{% endtab %}
{% tab Datos del evento %}

| Entrada | Descripción | Obligatorio |
| --- | --- | --- |
| Nombre del evento | Nombre del evento. | Sí |
| Hora del evento | Fecha-hora como cadena en formato ISO 8601 o en formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. | Sí |
| Identificador de aplicación | El identificador de la aplicación o `app_id` es un parámetro que asocia la actividad con una aplicación específica en tu espacio de trabajo. Designa con qué aplicación dentro del espacio de trabajo estás interactuando. | No |
| Propiedades del evento | Un objeto JSON que contiene propiedades personalizadas del evento. | No |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 4: Crear una regla de envío de eventos" }

{% alert note %}
La acción **Braze Send Event** solo requiere que se especifique un **Event Name** y un **Event Time**, pero debes incluir tanta información como sea posible en el campo de propiedades personalizadas. Consulta el [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object) para más detalles.
{% endalert %}

{% endtab %}
{% tab Atributo de usuario %}

Los atributos de usuario pueden ser un objeto JSON que contiene campos que crearán o actualizarán un atributo con el nombre y valor proporcionados en el perfil de usuario especificado. Se admiten las siguientes propiedades:

| Atributo de usuario | Descripción |
| --- | --- |
| Nombre | Nombre del usuario. |
| Apellido | Apellido del usuario. |
| Teléfono | Número de teléfono del usuario. |
| Correo electrónico | Dirección de correo electrónico del usuario. |
| Género | Una de las siguientes cadenas: "M", "F", "O" (otro), "N" (no aplica), "P" (prefiere no decir). |
| Ciudad | La ciudad del usuario. |
| País | El país del usuario como una cadena en formato [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| Idioma | El idioma del usuario como una cadena en formato [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| Fecha de nacimiento | La fecha de nacimiento del usuario como cadena en formato "AAAA-MM-DD" (por ejemplo, 1980-12-21). |
| Zona horaria | Nombre de la zona horaria de la base de datos [IANA Time Zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (por ejemplo, 'America/New_York' o 'Eastern Time (US & Canada)'). |
| Facebook | Un hash que contiene cualquiera de `id` (cadena), `likes` (matriz de cadenas), `num_friends` (entero). |
| Twitter | Un hash que contiene cualquiera de id (entero), `screen_name` (cadena, identificador de X (anteriormente Twitter)), `followers_count` (entero), `friends_count` (entero), `statuses_count` (entero). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 4: Crear una regla de envío de eventos" }

{% alert note %}
Todos los atributos añadidos dentro de la configuración se enviarán cada vez que el evento se envíe a Braze, independientemente de si el valor del atributo ha cambiado. Al configurar atributos de usuario, asegúrate de saber cómo esto afectará tu uso de puntos de datos.
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 5: Crear una regla de envío de evento de compra {#step-5-create-a-send-purchase-event-rule}

Después de instalar la extensión, crea una nueva [regla](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) de reenvío de eventos y configura sus condiciones como desees. Al configurar las acciones de la regla, selecciona la extensión **Braze** y luego selecciona **Send Purchase Event** como tipo de acción.

![Acción de regla de reenvío de eventos de Adobe configurada para utilizar Braze Send Purchase Event.]({% image_buster /assets/img/efe2.png %})

{% tabs local %}
{% tab Identificación de usuario %}

| Entrada | Descripción |
| --- | --- |
| ID de usuario externo | Un UUID o GUID largo, aleatorio y bien distribuido. Si eliges un método diferente para nombrar tus ID de usuario, estos también deben ser largos, aleatorios y estar bien distribuidos. Más información sobre las [convenciones sugeridas para nombrar ID de usuario]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web#naming-best-practices). |
| ID de usuario de Braze | Identificador de usuario de Braze. |
| Alias de usuario | Un alias sirve como identificador de usuario único alternativo. Utiliza alias para identificar usuarios a lo largo de dimensiones diferentes a tu ID de usuario principal.<br><br>El objeto de alias de usuario consta de dos partes: un `alias_name` para el identificador en sí y un `alias_label` que indica el tipo de alias. Los usuarios pueden tener múltiples alias con diferentes etiquetas, pero solo un `alias_name` por cada `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 5: Crear una regla de envío de evento de compra" }

{% alert note %}
Para vincular el evento a un usuario, debes completar el campo `External User ID`, el campo `Braze User Identifier` o la sección `User Alias`.
{% endalert %}

{% endtab %}
{% tab Datos de compra %}

| Entrada | Descripción | Obligatorio |
| --- | --- | --- |
| ID de producto | Identificador de la compra (por ejemplo, nombre del producto o categoría del producto). | Sí |
| Hora de compra | Fecha-hora como cadena en formato ISO 8601 o en formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. | Sí |
| Moneda | Moneda como cadena en formato de código de moneda alfabético [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217). | Sí |
| Precio | El precio del objeto. | Sí |
| Cantidad | La cantidad comprada. Si no se proporciona, el valor predeterminado será 1. El valor máximo debe ser inferior a 100. | No |
| Identificador de aplicación | El identificador de la aplicación o `app_id` es un parámetro que asocia la actividad con una aplicación específica en tu espacio de trabajo. Designa con qué aplicación dentro del espacio de trabajo estás interactuando. | No |
| Propiedades de la compra | Un objeto JSON que contiene propiedades personalizadas de la compra. | No |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 5: Crear una regla de envío de evento de compra" }

{% alert note %}
La acción **Send Purchase Event** solo requiere que se especifiquen un `Product ID`, `Purchase Time`, `Currency` y `Price`, pero debes incluir tanta información como sea posible en el campo de propiedades de compra. Consulta el [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object) para más detalles.
{% endalert %}

{% endtab %}
{% tab Atributos de usuario %}

Puedes elegir si enviar atributos con cada evento dentro de la vista de configuración.

Los atributos de usuario pueden ser un objeto JSON que contiene campos que crearán o actualizarán un atributo con el nombre y valor proporcionados en el perfil de usuario especificado. Se admiten las siguientes propiedades:

| Atributo de usuario | Descripción |
| --- | --- |
| Nombre | Nombre del usuario. |
| Apellido | Apellido del usuario. |
| Teléfono | Número de teléfono del usuario. |
| Correo electrónico | Dirección de correo electrónico del usuario. |
| Género | Una de las siguientes cadenas: "M", "F", "O" (otro), "N" (no aplica), "P" (prefiere no decir). |
| Ciudad | La ciudad del usuario. |
| País | El país del usuario como una cadena en formato [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| Idioma | El idioma del usuario como una cadena en formato [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| Fecha de nacimiento | La fecha de nacimiento del usuario como cadena en formato "AAAA-MM-DD" (por ejemplo, 1980-12-21). |
| Zona horaria | Nombre de la zona horaria de la base de datos [IANA Time Zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (por ejemplo, 'America/New_York' o 'Eastern Time (US & Canada)'). |
| Facebook | Un hash que contiene cualquiera de `id` (cadena), `likes` (matriz de cadenas), `num_friends` (entero). |
| Twitter | Un hash que contiene cualquiera de id (entero), `screen_name` (cadena, identificador de X (anteriormente Twitter)), `followers_count` (entero), `friends_count` (entero), `statuses_count` (entero). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 5: Crear una regla de envío de evento de compra" }

{% alert note %}
Todos los atributos añadidos dentro de la configuración se enviarán cada vez que el evento se envíe a Braze, independientemente de si el valor del atributo ha cambiado. Al configurar atributos de usuario, asegúrate de saber cómo esto afectará tu uso de puntos de datos.
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 6: Validar los datos dentro de Braze {#step-6-validate-data-within-braze}

Si la recopilación de eventos y la integración con Adobe Experience Platform fueron exitosas, verás eventos dentro de la consola de Braze al [visualizar perfiles de usuario]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles). Específicamente, los nuevos datos de eventos enviados a Braze se reflejan en la sección **Purchases** o **Custom Events** de la [pestaña de resumen]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#overview-tab) de un usuario en particular.