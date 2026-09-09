---
nav_title: API e identificadores
article_title: API e identificadores
page_order: 0
page_type: reference
description: "Este artículo cubre la página de API e identificadores, que muestra las identificaciones de API para tu espacio de trabajo."
---

# API e identificadores {#apis-and-identifiers}

> La página **API e identificadores** es tu centro centralizado para administrar todas tus claves de API REST en un solo lugar. Aquí puedes acceder al conjunto de claves de API e identificadores de aplicación de cada espacio de trabajo.

Puedes encontrar la página **API e identificadores** en **Configuración** > **Configuración y pruebas** > **API e identificadores**.

## Claves de API {#api-keys}

Esta sección proporciona las claves de API REST de tu espacio de trabajo, los identificadores únicos que te permiten acceder a los datos de un espacio de trabajo. Se requiere una clave de API REST con cada solicitud a la API de Braze. Para más información sobre cómo crear y utilizar claves de API, consulta nuestro [resumen de claves de API REST]({{site.baseurl}}/api/basics).

### Lista de IP permitidas de la API {#api-ip-allowlisting}

Para mayor seguridad, puedes especificar una lista de direcciones IP y subredes con permiso para realizar solicitudes de API REST para una clave de API REST determinada. Esto se conoce como lista de IP permitidas. Para permitir direcciones IP o subredes específicas, agrégalas a la sección **Allowlist IPs** al crear una nueva clave de API REST:

![Sección de lista de IP permitidas de la API al crear una nueva clave de API REST]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Si no especificas ninguna, las solicitudes se pueden enviar desde cualquier dirección IP.

{% alert tip %}
¿Estás creando un webhook de Braze a Braze y utilizas la lista de permitidos? Consulta nuestra lista de [IP de la lista blanca]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting).
{% endalert %}

### Alertas de uso de la API {#api-usage-alerts}

Configura alertas de uso de la API para supervisar la actividad clave de la API y detectar problemas de forma temprana. Estas alertas te ayudan a identificar patrones de tráfico inesperados antes de que afecten tu experiencia.

Puedes rastrear dos tipos de actividad de la API:

- **Endpoints de API REST:** Acciones como enviar mensajes, crear Campaigns o exportar datos.
- **Solicitudes de API del SDK:** Eventos de tu experiencia del cliente, como desencadenar mensajes dentro de la aplicación o sincronizar perfiles de usuario. *Esta característica está disponible si has adquirido usuarios activos al mes (CY 24–25).*

Una vez que elijas qué rastrear, puedes definir las condiciones de alerta. Por ejemplo, recibir una notificación si las respuestas de error aumentan un 20 % en una hora. Recibirás una notificación por correo electrónico, webhook o ambos, según tu configuración. Para empezar, consulta [Alertas de uso de la API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts).

## Identificadores de la aplicación {#app-identifiers}

Esta sección incluye una lista de identificadores utilizados para hacer referencia a aplicaciones específicas en las solicitudes realizadas a la API de Braze. Para obtener más información sobre los identificadores de aplicación, consulta [Clave de API del identificador de aplicación]({{site.baseurl}}/api/identifier_types).

## Otros identificadores {#other-identifiers}

Para integrarte con nuestra API, puedes buscar los identificadores relacionados con cualquier Segment, Campaign, Content Cards y más a los que quieras acceder desde la API externa de Braze. Todos los mensajes deben seguir la codificación [UTF-8](https://en.wikipedia.org/wiki/UTF-8). Después de seleccionar cualquiera de ellos, el identificador se mostrará debajo del menú desplegable.

Para más información, consulta [Tipos de identificadores de API]({{site.baseurl}}/api/identifier_types).