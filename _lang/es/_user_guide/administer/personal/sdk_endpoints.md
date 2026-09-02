---
nav_title: Puntos finales de API y SDK or kit de desarrollo de software
article_title: Puntos finales de API y SDK or kit de desarrollo de software
page_order: 5
page_type: reference
description: "Busca la URL correcta del panel, el endpoint de REST or transferencia de estado representacional API y el punto final de SDK or kit de desarrollo de software para tu instancia de Braze."

---

# Puntos finales de API y SDK or kit de desarrollo de software {#api-and-sdk-endpoints}

> Busca la URL correcta del panel, el endpoint de REST or transferencia de estado representacional API y el punto final de SDK or kit de desarrollo de software para tu instancia de Braze. Necesitas estas URL para iniciar sesión, realizar llamadas a la API e integrar el SDK or kit de desarrollo de software.

Braze administra varias instancias diferentes para nuestro panel, SDK or kit de desarrollo de software y endpoints REST or transferencia de estado representacional, que llamamos "clústeres". Tu administrador de incorporación de Braze te indicará en qué clúster te encuentras. Para obtener más información sobre el SDK or kit de desarrollo de software de Braze, consulta el [Braze 101](https://learning.braze.com/braze-101), un curso de Braze Learning.

Iniciar sesión en [dashboard.braze.com](https://dashboard.braze.com) te enviará automáticamente a la dirección de clúster correcta.

{% multi_lang_include administer/data_centers.md datacenters='instances' %}

{% alert important %}
Al integrar tu SDK or kit de desarrollo de software, usa el punto final de SDK or kit de desarrollo de software. Al realizar llamadas a nuestra REST or transferencia de estado representacional API, usa el endpoint REST or transferencia de estado representacional.
{% endalert %}

Para obtener más detalles sobre el acceso a la API, consulta nuestro [artículo de resumen de la API]({{site.baseurl}}/api/basics).