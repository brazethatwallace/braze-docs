---
nav_title: DinMo
article_title: DinMo
description: "Este artículo de referencia describe la asociación entre Braze y DinMo, una CDP componible que utiliza ETL inverso para sincronizar datos del almacén de datos en Braze."
alias: /partners/dinmo/
page_type: partner
search_tag: Partner

---

# DinMo

> [DinMo](https://www.dinmo.com/) es una CDP (CDP) componible que conecta tu almacén de datos en la nube con Braze mediante ETL (ETL) inverso. Los equipos de marketing pueden crear segmentos de audiencia a partir de datos del almacén, sincronizar atributos de usuario y eventos en Braze, y mantener los estados de suscripción actualizados sin cargas de CSV ni soporte de ingeniería.

_Esta integración está gestionada por DinMo._

La integración de Braze y DinMo envía segmentos y modelos de datos desde tu almacén de datos a Braze a través de la REST API de Braze. Cuando conectas un destino de Braze en DinMo, las activaciones envían datos desde tus modelos o segmentos a Braze.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta de DinMo | Se requiere una [cuenta de DinMo](https://www.dinmo.com/) con permiso para crear destinos para aprovechar esta integración. |
| Clave de API REST de Braze | Una clave de API REST de Braze con los [permisos](#api-key-permissions) necesarios para los servicios de destino que planeas utilizar. Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Endpoint REST de Braze | La URL de tu endpoint REST. Tu endpoint depende de los [endpoints de API]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints) de tu instancia de Braze. |
| URL del panel de Braze | La URL de tu panel de Braze para tu instancia (por ejemplo, `https://dashboard.iad-01.braze.com`). Para más información, consulta [Puntos finales de SDK disponibles]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). |
| Almacén de datos y modelo de datos | Antes de comenzar la integración, conecta tu almacén de datos en DinMo y define un modelo o segmento para los datos que deseas sincronizar con Braze. Para más información, consulta la [guía de integración de DinMo con Braze](https://docs.dinmo.io/integrations/destination-platforms/braze). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Ejemplos {#use-cases}

Con esta integración, puedes:

* Sincronizar atributos de usuario desde tu almacén de datos en Braze para personalizar Campaigns y Canvas.
* Enviar eventos personalizados y eventos de compra desde los datos del almacén de datos a Braze para segmentación por comportamiento.
* Mantener la membresía de grupos de suscripción de Braze alineada con los segmentos de audiencia definidos en DinMo.
* Exportar segmentos de DinMo como atributos de usuario de Braze y crear Segments de Braze a partir de esos atributos.

## Permisos de la clave de API {#api-key-permissions}

Otorga los siguientes permisos a tu clave de API REST de Braze en función de los servicios de destino que utilices:

| Permiso | Obligatorio para |
| --- | --- |
| `users.track` | Sincronizar atributos de usuario, enviar eventos de seguimiento y validar la conexión de destino |
| `users.export.ids` | Exportar ID de usuario para operaciones masivas |
| `users.alias.update` | Actualizar alias de usuario |
| `subscription.status.set` | Sincronizar estados de suscripción |
| `users.delete` | Solo modo de sincronización espejo (opcional para otros servicios de destino) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permisos de la clave de API" }

## Integración {#integration}

### Paso 1: Configura el destino de Braze en DinMo {#step-1-configure-the-braze-destination-in-dinmo}

1. En DinMo, ve a **Destinos** en la navegación lateral.
2. Selecciona **Add a new destination** > **Connect a new platform** > **Braze**.
3. En el formulario de conexión, introduce los siguientes datos:
   * **Platform Name**: Por ejemplo, `Braze – Your Company`
   * **REST API URL**: El endpoint REST de tu instancia (por ejemplo, `https://rest.eu-01.braze.com`)
   * **Dashboard URL**: La URL del panel de tu instancia (por ejemplo, `https://dashboard.eu-01.braze.com`)
   * **API Key**: La clave que copiaste de Braze
4. Selecciona **Connect** para validar tus credenciales.

{% alert note %}
Debes especificar tanto la URL de la REST API como la URL del panel. No incluyas una barra diagonal final en la URL de la REST API.
{% endalert %}

### Paso 2: Verifica la conexión {#step-2-verify-the-connection}

Después de guardar el destino, DinMo realiza una llamada de prueba (por ejemplo, `users.track`) para confirmar que tu clave de API y el endpoint funcionan.

Si la validación falla, confirma lo siguiente:

* La URL de la REST API es correcta y no tiene una barra diagonal final.
* La clave de API es válida y tiene los permisos necesarios.
* Si tu espacio de trabajo de Braze utiliza una lista de IP permitidas, las direcciones IP de DinMo están incluidas.

## Servicios de destino compatibles {#supported-destination-services}

Cada servicio de destino en DinMo sigue el mismo flujo de trabajo general: crear un destino de Braze, construir un modelo o Segment de DinMo y, a continuación, crear una activación para enviar datos a Braze. Para obtener orientación paso a paso sobre la activación, consulta [Servicios de destino de DinMo para Braze](https://docs.dinmo.io/integrations/destination-platforms/braze).

Los siguientes servicios de destino están disponibles:

| Servicio de destino | Descripción |
| --- | --- |
| [Sincronizar atributos de usuario](https://docs.dinmo.io/integrations/destination-platforms/braze/synchronize-users-attributes) | Actualiza atributos del perfil de usuario en Braze y, opcionalmente, inserta usuarios nuevos. |
| [Enviar eventos de seguimiento](https://docs.dinmo.io/integrations/destination-platforms/braze/send-track-events) | Envía eventos personalizados y eventos de compra a Braze. |
| [Sincronizar estados de suscripción](https://docs.dinmo.io/integrations/destination-platforms/braze/synchronize-subscription-statuses) | Suscribe o cancela la suscripción de usuarios en un grupo de suscripción de Braze en función de la pertenencia a un Segment de DinMo. |
| [Exportar listas de usuarios](https://docs.dinmo.io/integrations/destination-platforms/braze/export-user-lists) | Sincroniza la pertenencia a un Segment con un atributo de usuario de Braze para su uso en la segmentación de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Servicios de destino compatibles" }

### Sincronizar atributos de usuario {#synchronize-user-attributes}

Utiliza este servicio de destino para actualizar atributos en perfiles de usuario de Braze existentes y, opcionalmente, insertar usuarios nuevos.

Cuando ejecutas una activación:

* Si habilitas el modo de inserción, los usuarios nuevos del modelo se crean en Braze (comportamiento UPSERT).
* Los valores de atributos que hayan cambiado desde la última activación se actualizan en Braze.

Si no habilitas el modo de inserción, DinMo solo actualiza los usuarios que ya existen en Braze y tienen un ID externo coincidente.

Durante la configuración de la activación, mapea el campo de tu modelo de DinMo que corresponde al [ID externo]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web) del usuario o al ID de Braze. Mapea cada campo de DinMo con el nombre exacto del atributo en Braze. Si un atributo no existe en Braze, DinMo lo crea.

Los siguientes modos de sincronización están disponibles para las activaciones de atributos de usuario:

| Modo de sincronización | Descripción |
| --- | --- |
| UPDATE | Actualiza los registros modificados para usuarios que ya existen en Braze. No inserta ni elimina registros. |
| UPSERT | Inserta registros nuevos y actualiza los registros modificados. No elimina registros. |
| MIRROR | Inserta, actualiza y elimina registros en Braze para reflejar la fuente. Requiere que el conector sea compatible con operaciones de eliminación. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modos de sincronización de atributos de usuario" }

{% alert warning %}
El modo de sincronización MIRROR elimina permanentemente los registros de Braze cuando ya no están presentes en la fuente de DinMo. Utiliza el modo MIRROR solo cuando tu almacén de datos sea la única fuente de verdad y las eliminaciones sean intencionales. Valida las reglas de eliminación antes de ejecutar sincronizaciones MIRROR en producción.
{% endalert %}

### Enviar eventos de seguimiento {#send-track-events}

Utiliza este servicio de destino para enviar eventos personalizados o eventos de compra desde un modelo de eventos o Segment de DinMo a Braze. DinMo trata los eventos personalizados y las compras como servicios de destino independientes porque Braze utiliza API diferentes para cada tipo.

Cada registro del modelo representa un tipo de evento único (por ejemplo, `Purchase`). DinMo envía solo los eventos nuevos en cada ejecución de la activación y no actualiza los eventos enviados previamente.

Durante la configuración de la activación:

1. Especifica el nombre del evento exactamente como debe aparecer en Braze. Si el evento no existe, DinMo lo crea.
2. Mapea los campos obligatorios:
   * **Hora del evento**: marca de tiempo en la que ocurrió el evento
   * **ID externo**: ID externo del usuario asociado al evento
3. Mapea las propiedades del evento opcionales con nombres de atributos de Braze.
4. Configura la programación de la frecuencia con la que se envían los eventos nuevos a Braze.

### Sincronizar estados de suscripción {#synchronize-subscription-statuses}

Utiliza este servicio de destino para mantener un grupo de suscripción de Braze alineado con un Segment o modelo de DinMo.

Antes de activar este servicio:

1. Crea el grupo de suscripción de destino (SMS o correo electrónico) en Braze.
2. Construye un modelo o Segment de DinMo que contenga los usuarios que deben pertenecer a ese grupo de suscripción.

Durante la configuración de la activación, introduce el ID exacto del grupo de suscripción de Braze. Para sincronizar varios grupos de suscripción, crea una activación por grupo.

Cuando se ejecuta la activación:

* Si los usuarios ya existen en Braze, los usuarios que entran en el Segment de DinMo se marcan como suscritos al grupo de suscripción de destino.
* Los usuarios que salen del Segment de DinMo se marcan con la suscripción cancelada en el grupo de suscripción.

DinMo no modifica a los usuarios que nunca formaron parte del Segment ni crea usuarios nuevos en Braze con este servicio de destino.

### Exportar listas de usuarios {#export-user-lists}

Utiliza este servicio de destino para representar un Segment de DinMo como un atributo de usuario de Braze. Debido a una limitación de Braze, DinMo no crea una lista de Braze directamente. En su lugar, establece un atributo de usuario con el valor `true` para los usuarios del Segment y `false` para los usuarios que salen del Segment.

Durante la configuración de la activación, especifica el nombre de la audiencia. DinMo utiliza este nombre como atributo de Braze (los espacios se reemplazan con guiones bajos). Confirma que no exista ya un atributo con el mismo nombre en Braze. Mapea el campo de DinMo que corresponde al ID externo del usuario.

Después de que se ejecute la activación, crea un Segment de Braze que filtre a los usuarios cuyo atributo sincronizado sea igual a `true`.

Solo se actualizan los usuarios con un ID externo que coincida con un usuario de Braze existente. Este servicio de destino no crea usuarios nuevos.