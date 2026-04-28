---
nav_title: Puntos finales de API y SDK
article_title: Puntos finales de API y SDK
page_order: 5
page_type: reference
description: "Busca la URL correcta del dashboard, el punto de conexión de REST API y el punto final de SDK para tu instancia de Braze."

---

# Puntos finales de API y SDK {#api-and-sdk-endpoints}

> Busca la URL correcta del dashboard, el punto de conexión de REST API y el punto final de SDK para tu instancia de Braze. Necesitas estas URL para iniciar sesión, realizar llamadas a la API e integrar el SDK.

Braze administra varias instancias diferentes para nuestro dashboard, SDK y puntos de conexión REST, que llamamos "clústeres". Tu administrador de incorporación de Braze te indicará en qué clúster te encuentras. Para obtener más información sobre el SDK de Braze, consulta el curso de Braze Learning [Braze 101](https://learning.braze.com/braze-101).

Iniciar sesión en [dashboard.braze.com](https://dashboard.braze.com) te enviará automáticamente a la dirección de clúster correcta.

{% multi_lang_include data_centers.md datacenters='instances' %}

{% alert important %}
Al integrar tu SDK, usa el punto final de SDK. Al realizar llamadas a nuestra REST API, usa el punto de conexión REST.
{% endalert %}

Para obtener más detalles sobre el acceso a la API, consulta nuestro [artículo de resumen de la API]({{site.baseurl}}/api/basics/).