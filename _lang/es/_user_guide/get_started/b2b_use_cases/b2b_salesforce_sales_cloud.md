---
nav_title: Salesforce Sales Cloud
article_title: Administrar clientes potenciales con Salesforce Sales Cloud
page_order: 3
page_type: reference
description: "Aprende a utilizar webhooks de Braze para crear y actualizar clientes potenciales en Salesforce Sales Cloud a través del punto de conexión Salesforce sobjects/Lead."
---

# Administrar clientes potenciales con Salesforce Sales Cloud {#manage-leads-with-salesforce-sales-cloud}

> [Salesforce](https://www.salesforce.com/) es una de las principales plataformas de administración de las relaciones con el cliente (CRM) en la nube del mundo, diseñada para ayudar a las empresas a gestionar todo su proceso de ventas, incluida la generación de clientes potenciales, el seguimiento de oportunidades y la administración de cuentas.<br><br>Esta página muestra cómo utilizar webhooks de Braze para crear y actualizar clientes potenciales en Salesforce Sales Cloud mediante una integración enviada por la comunidad.

{% alert important %}
Se trata de una integración enviada por la comunidad y no cuenta con soporte directo de Braze. Solo las plantillas oficiales de webhook proporcionadas por Braze cuentan con soporte de Braze.
{% endalert %}

## Cómo funciona {#how-it-works}

La integración de Braze y Salesforce Sales Cloud utiliza webhooks de Braze para crear y actualizar clientes potenciales en Salesforce Sales Cloud a través del punto de conexión de Salesforce [sobjects/Lead](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.html).

Braze ofrece actualmente dos integraciones con Salesforce Sales Cloud para los siguientes casos de uso:
1. [Crear un cliente potencial en Salesforce Sales Cloud](#creating-lead)
2. [Actualizar un cliente potencial en Salesforce Sales Cloud](#updating-lead)

{% alert note %}
Esta integración es exclusivamente para actualizar Salesforce desde Braze como parte de tus esfuerzos de captación y nutrición de clientes potenciales. Para sincronizar datos de Salesforce de vuelta a Braze, consulta el [modelo de datos B2B]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models/) o ponte en contacto con uno de nuestros [socios tecnológicos]({{site.baseurl}}/partners/home/).
{% endalert %}

## Requisitos previos {#prerequisites}

Antes de poder continuar con esta integración, el soporte de Salesforce debe darte la capacidad de crear aplicaciones conectadas. Puedes solicitarlo enviando una [solicitud de soporte de Salesforce](https://help.salesforce.com/s/articleView?id=005167035&type=1).

Una vez que el soporte de Salesforce te otorgue la capacidad de crear una aplicación conectada en Salesforce Sales Cloud, sigue los pasos de la documentación de Salesforce: [Configure a Connected App for the OAuth 2.0 Client Credentials Flow](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5).

Cuando configures los ajustes OAuth necesarios para la aplicación conectada, mantén todos los ajustes OAuth con sus valores y selecciones predeterminados, excepto los siguientes:
1. Selecciona **Enable for device flow**. Puedes dejar **Callback URL** en blanco, ya que se establecerá de forma predeterminada a un marcador de posición.
2. Para los **OAuth Scopes** seleccionados, añade **Manage user data via APIs (api)**.
3. Selecciona **Enable Client Credentials Flow**.

## Crear un cliente potencial en Salesforce Sales Cloud {#creating-lead}

Como plataforma de interacción con los clientes, Braze puede generar nuevos clientes potenciales basándose en flujos de usuario, como rellenar un formulario en una página de inicio. Cuando eso ocurra, puedes utilizar un webhook de Braze para Salesforce Sales Cloud para crear un cliente potencial correspondiente en Salesforce.

### Paso 1: Recopila tu `client_id` y `client_secret` {#step-1-collect-your-client_id-and-client_secret}

1. En Salesforce, ve a **Platform Tools** > **Apps** > **App Manager**.
2. Busca tu aplicación Braze recién creada y selecciona **View**.
3. En **Consumer Key and Secret**, selecciona **Manage Consumer Details**.
4. En la página resultante, toma nota de tu **Consumer Key** y tu **Consumer Secret**. La **Consumer Key** es tu `client_id`, y el **Consumer Secret** es tu `client_secret`.

### Paso 2: Configura tu plantilla de webhook {#step-2-set-up-your-webhook-template}

Utiliza plantillas para reutilizar rápidamente este webhook en toda la plataforma Braze.

1. En Braze, ve a **Plantillas**, selecciona **Plantillas de Webhook** y luego selecciona **+ Crear plantilla de webhook**.
2. Proporciona un nombre para la plantilla, como "Salesforce Sales Cloud > Crear cliente potencial".
3. En la pestaña **Redactar**, introduce los siguientes datos:

#### Redactar webhook {#compose-webhook}

| Campo | Detalles |
| --- | --- |
| URL del webhook | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/`{% endraw %} |
| Método HTTP | `POST` |
| Cuerpo de la solicitud | Pares clave-valor de JSON |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Redactar webhook" }

#### Valores clave de la propiedad del cuerpo {#body-property-key-values}

Selecciona **+ Add New Body Property** para cada uno de los pares clave-valor que quieras mapear de Braze a Salesforce. Puedes mapear cualquier campo que desees, así que la siguiente tabla es solo un ejemplo.

| Clave | Valor |
| --- | --- |
| firstName | {% raw %}`{{${first_name}}}`{% endraw %} |
| lastName | {% raw %}`{{${last_name}}}`{% endraw %} |
| email | {% raw %}`{{${email_address}}}`{% endraw %} |
| company | {% raw %}`{{custom_attribute.${company}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Valores clave de la propiedad del cuerpo" }

#### Encabezados de solicitud {#request-headers}

Selecciona **+ Add New Header** para cada uno de los siguientes encabezados de solicitud.

| Clave | Valor |
| --- | --- |
| Authorization | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Type | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Encabezados de solicitud" }

{: start="4" }
4. Selecciona **Save Template**.

![Una plantilla de webhook completada para crear un cliente potencial.]({% image_buster /assets/img/b2b/create_lead_webhook.png %}){: style="max-width:70%;"}

## Actualizar un cliente potencial en Salesforce Sales Cloud {#updating-lead}

Para configurar un webhook de Braze para Salesforce Sales Cloud que actualice clientes potenciales en Salesforce, necesitas un identificador común entre Salesforce Sales Cloud y Braze. El ejemplo siguiente utiliza el `lead_id` de Salesforce como el `external_id` de Braze, pero también puedes lograrlo utilizando un `user_alias`. Para más detalles, consulta [Datos B2B]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models/).

Este ejemplo muestra específicamente cómo actualizar la etapa de un cliente potencial a "MQL" (Marketing Qualified Lead) después de que un cliente potencial supere un determinado umbral. Esta es una parte fundamental de nuestro caso de uso del [flujo de trabajo de puntuación de clientes potenciales B2B]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring/).

### Paso 1: Recopila tu `client_id` y `client_secret`

1. En Salesforce, ve a **Platform Tools** > **Apps** > **App Manager**.
2. Busca tu aplicación Braze recién creada y selecciona **View**.
3. En **Consumer Key and Secret**, selecciona **Manage Consumer Details**.
4. En la página resultante, toma nota de tu **Consumer Key** y tu **Consumer Secret**.
    - La **Consumer Key** es tu `client_id`, y el **Consumer Secret** es tu `client_secret`.

### Paso 2: Configura tu plantilla de webhook

1. En Braze, ve a **Plantillas**, selecciona **Plantillas de Webhook** y luego selecciona **+ Crear plantilla de webhook**.
2. Proporciona un nombre para la plantilla, como "Salesforce Sales Cloud > Actualizar cliente potencial a MQL".
3. En la pestaña **Redactar**, introduce los siguientes datos:

#### Redactar webhook

| Campo | Detalles |
| --- | --- |
| URL del webhook | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} |
| Método HTTP | `PATCH` |
| Cuerpo de la solicitud | Pares clave-valor de JSON |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Redactar webhook" }

#### Valores clave de la propiedad del cuerpo

Selecciona **+ Add New Body Property** para el siguiente par clave-valor. Ten en cuenta que `Lead_Stage__c` es un nombre de ejemplo. El campo personalizado que utilizas para hacer seguimiento de los MQL en Salesforce puede tener un nombre diferente, así que asegúrate de que coincidan.

| Clave | Valor |
| --- | --- |
| `Lead_Stage__c` | `MQL` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Valores clave de la propiedad del cuerpo" }

#### Encabezados de solicitud

Selecciona **+ Add New Header** para cada uno de los siguientes encabezados de solicitud.

| Clave | Valor |
| --- | --- |
| Authorization | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Type | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Encabezados de solicitud" }

{: start="4"}
4. Selecciona **Save Template**.

![Una plantilla de webhook completada para actualizar un cliente potencial.]({% image_buster /assets/img/b2b/update_lead_webhook.png %}){: style="max-width:70%;"}

## Usar estos webhooks en un flujo de trabajo operativo {#using-these-webhooks-in-an-operational-workflow}

Puedes añadir rápidamente tus plantillas a tus flujos de trabajo operativos en Braze, por ejemplo:

1. Como parte de una [campaña de nuevo cliente potencial](#new-lead) que crea un cliente potencial en Salesforce
2. Como parte de un [Canvas de puntuación de clientes potenciales](#lead-scoring) que actualiza a los usuarios que han superado tu umbral de MQL a "MQL", y que actualiza Salesforce Sales Cloud con la misma información

### Campaña de nuevo cliente potencial {#new-lead}

Para crear un cliente potencial en Salesforce cuando un usuario proporcione su dirección de correo electrónico, puedes crear una campaña que utilice la plantilla de webhook "Actualizar cliente potencial" y se desencadene cuando un usuario añada su dirección de correo electrónico (por ejemplo, al rellenar un formulario web).

![Paso 2 de la creación de una campaña basada en acciones con la acción desencadenante "Añadir una dirección de correo electrónico".]({% image_buster /assets/img/b2b/salesforce_create_campaign.png %}){: style="max-width:70%;"}

### Canvas de puntuación de clientes potenciales para superar el umbral de Marketing Qualified Lead (MQL) {#lead-scoring}

Este webhook se trata en el caso de uso de [puntuación de clientes potenciales]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring/#lead-handoff), pero también puedes comprobar los MQL y actualizar directamente Salesforce dentro del Canvas de puntuación de clientes potenciales (en lugar de crear una campaña de webhook independiente):

Añade un paso posterior a tu actualización de usuario para comprobar si un usuario ha superado el umbral de MQL que hayas definido. Si lo ha superado, actualiza el estado del usuario a "MQL" y luego actualiza Salesforce con el mismo estado "MQL" utilizando esta plantilla de webhook. Salesforce se encarga del resto, enrutando este cliente potencial a los equipos de ventas adecuados mediante las reglas de enrutamiento de clientes potenciales que hayas definido.

#### Añadir un paso en Canvas para comprobar los usuarios que superaron el umbral de MQL {#adding-canvas-step-to-check-for-users-who-passed-the-mql-threshold}

1. Añade un paso de **ruta de audiencia** con dos grupos: "MQL Threshold" y "El resto".
2. En el grupo "MQL Threshold", busca a los usuarios que actualmente no tengan un estado de "MQL" (por ejemplo, `lead_stage` es igual a "Lead"), pero que tengan una puntuación de cliente potencial superior al umbral que hayas definido (por ejemplo, `lead_score` mayor que 50). Si es así, avanzan al siguiente paso; si no, salen.

![El grupo de ruta de audiencia "MQL Threshold" con filtros para un `lead_stage` igual a "Lead" y un `lead_score` superior a "50".]({% image_buster /assets/img/b2b/salesforce_check_mql.png %}){: style="max-width:70%;"}

{: start="3" }
3. Añade un paso de **Actualización de usuario** que actualice el valor del atributo `lead_stage` del usuario a "MQL".

![El paso de Actualización de usuario "Update to MQL" que actualiza el atributo `lead_stage` para que tenga el valor "MQL".]({% image_buster /assets/img/b2b/salesforce_update_mql.png %}){: style="max-width:70%;"}

{: start="4" }
4. Añade un paso de webhook que actualice Salesforce con la nueva etapa MQL.

![El paso de webhook "Update Salesforce" con los detalles completados.]({% image_buster /assets/img/b2b/salesforce_webhook.png %}){: style="max-width:70%;"}

¡Ahora tu flujo de Canvas actualizará a los usuarios que hayan superado tu umbral de MQL!

![Un paso de Canvas de actualización de usuario que comprueba si un usuario supera el umbral de MQL y, si lo supera, actualiza Salesforce.]({% image_buster /assets/img/b2b/salesforce_canvas.png %}){: style="max-width:50%;"}

## Solución de problemas {#troubleshooting}

Estos flujos de trabajo tienen una capacidad de depuración limitada dentro de Salesforce, por lo que recomendamos consultar el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/#message-activity-log) de Braze para averiguar por qué falló un webhook y si se produjo algún error.

Por ejemplo, un error causado por una URL no válida utilizada para la recuperación del token OAuth se mostraría como `https://[insert_instance_name].my.salesforce.com/services/oauth2/token is not a valid URL`.

![Un cuerpo de respuesta de error que indica que la URL no es válida.]({% image_buster /assets/img/b2b/error_message_invalid_url.png %})