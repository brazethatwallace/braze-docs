---
nav_title: SCIM
article_title: Puntos de conexión SCIM
search_tag: Endpoint
page_order: 5
layout: dev_guide
alias: /scim/

description: "Esta página de destino enumera los puntos de conexión SCIM de Braze."
page_type: landing

guide_top_header: "Puntos de conexión SCIM"
guide_top_text: "La especificación <a href=\"http://www.simplecloud.info/\">System for Cross-domain Identity Management (SCIM)</a> está diseñada para facilitar la gestión de las identidades de los usuarios en aplicaciones y servicios basados en la nube, proporcionando un esquema definido para representar a usuarios y grupos. Utiliza los puntos de conexión SCIM de Braze para gestionar el aprovisionamiento automatizado de usuarios."

guide_featured_title: ""
guide_featured_list:
  - name: "POST: Crear una nueva cuenta de usuario en el dashboard"
    link: /docs/post_create_user_account/
    image: /assets/img/braze_icons/plus-circle.svg
  - name: "GET: Buscar una cuenta de usuario existente en el dashboard por ID de recurso"
    link: /docs/get_see_user_account_information/
    image: /assets/img/braze_icons/eye.svg
  - name: "GET: Buscar cuenta de usuario existente en el dashboard por correo electrónico"
    link: /docs/api/endpoints/scim/get_search_existing_dashboard_user/
    image: /assets/img/braze_icons/eye.svg
  - name: "PUT: Actualizar cuenta de usuario del dashboard"
    link: /docs/post_update_existing_user_account/
    image: /assets/img/braze_icons/pencil-01.svg
  - name: "DELETE: Eliminar cuenta de usuario del panel"
    link: /docs/delete_existing_dashboard_user/
    image: /assets/img/braze_icons/trash-01.svg
---


## Cómo exportar una lista de usuarios con acceso al dashboard {#how-to-export-a-list-of-users-with-dashboard-access}

Utiliza este flujo de trabajo para auditar a los usuarios que tienen acceso a tu panel de Braze.

1. Descarga el informe de eventos de seguridad desde **Settings** > **Admin Settings** > **Security Settings** > **Security Event Download**.
2. Extrae los correos electrónicos de los usuarios del informe.
3. Para cada correo electrónico, utiliza [GET: Buscar cuenta de usuario existente en el dashboard por correo electrónico]({{site.baseurl}}/api/endpoints/scim/get_search_existing_dashboard_user/) para obtener los detalles del usuario.
4. Si es necesario, utiliza el `id` de recurso devuelto con [GET: Buscar una cuenta de usuario existente en el dashboard por ID de recurso]({{site.baseurl}}/api/endpoints/scim/get_see_user_account_information/) para obtener detalles adicionales del usuario.

Para consultar la lista completa de puntos de conexión SCIM, visita [Puntos de conexión SCIM]({{site.baseurl}}/api/endpoints/scim/). Para más información sobre la fuente del informe, consulta [Descargar un informe de eventos de seguridad]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#security-event-report).