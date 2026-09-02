---
nav_title: Febrero
page_order: 11
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de febrero de 2018."
---
# Febrero de 2018 {#february-2018}

## Conteo de señales push en iOS {#ios-push-badge-count}

Ahora puedes [actualizar el conteo de señales]({{site.baseurl}}/help/best_practices/utilizing_badge_count#utilizing-badge-count) dentro del creador push de Braze.
Para cada mensaje push, puedes especificar qué conteo de señales desencadena esa notificación.

## Exportación de usuarios a través de la API mediante direcciones de correo electrónico {#exporting-users-via-api-using-email-addresses}

Ahora puedes [exportar datos de perfil de usuario a través de la API]({{site.baseurl}}/developer_guide/rest_api/export#user-export) especificando direcciones de correo electrónico.
Esta exportación incluye todos los perfiles asociados a esa dirección de correo electrónico.

## API de plantillas de correo electrónico {#email-template-apis}

Ahora puedes crear y actualizar [plantillas de correo electrónico a través de la API]({{site.baseurl}}/developer_guide/rest_api/email_templates#email-templates). Cada plantilla tendrá un **email_template_id** que puede referenciarse en otras llamadas a la API.

## Permisos de claves de API REST {#rest-api-keys-permissions}

Ahora puedes crear [varias claves de API REST]({{site.baseurl}}/api/basics#creating-rest-api-keys) y configurar permisos de acceso para cada una. Cada clave puede configurarse para conceder acceso a determinados endpoints.

También puedes especificar una [lista blanca de direcciones IP]({{site.baseurl}}/developer_guide/rest_api/basics#api-ip-whitelisting) y subredes que pueden realizar solicitudes de API REST para una clave de API REST determinada.