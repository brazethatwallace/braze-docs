---
nav_title: Grupos de suscripción
article_title: Puntos de conexión de grupos de suscripción
page_order: 7
layout: dev_guide

#Required
description: "Esta página de inicio explica y enumera los puntos de conexión de los grupos de suscripción de Braze para correo electrónico y SMS."
page_type: landing
search_tag: Endpoint

guide_top_header: "Puntos de conexión de grupos de suscripción"
guide_top_text: "Utiliza las API REST de grupos de suscripción para gestionar de forma programática los grupos de suscripción que hayas almacenado en el panel de Braze, en la página **Subscription Group**. Esto se aplica tanto a los grupos de suscripción por SMS como por correo electrónico.<br><br> ¿Buscas orientación para crear grupos de suscripción? Consulta nuestros artículos sobre <a href='/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/'>grupos de suscripción por SMS</a> y <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/'>grupos de suscripción por correo electrónico</a>."

guide_featured_title: ""
guide_featured_list:
  - name: "GET: Listar el estado del grupo de suscripción del usuario"
    link: /docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET: Lista de grupos de suscripción de usuarios"
    link: /docs/api/endpoints/subscription_groups/get_list_user_subscription_groups
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Actualizar el estado del grupo de suscripción del usuario"
    link: /docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status
    image: /assets/img/braze_icons/user-plus-01.svg
  - name: "POST: Actualizar el estado del grupo de suscripción del usuario V2"
    link: /docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2
    image: /assets/img/braze_icons/user-edit.svg
---
<br>
<br>


## Comprender las series temporales de los grupos de suscripción {#understand-subscription-group-timeseries}

En la página **Subscription Group**, los gráficos de series temporales informan sobre:

- **Tamaño del grupo de suscripción:** usuarios suscritos a ese grupo en una fecha determinada
- **Tamaño de cancelaciones de suscripción del grupo:** usuarios que cancelaron la suscripción de ese grupo en una fecha determinada

Para obtener orientación sobre el dashboard, consulta [Ver tamaños de los grupos de suscripción]({{site.baseurl}}/user_guide/channels/email/subscriptions#viewing-subscription-group-sizes).

Estas métricas son específicas de cada grupo. Pueden diferir del filtro de segmento `Email Subscription Status is Unsubscribed`, que refleja el estado global de suscripción de correo electrónico en lugar de un único grupo de suscripción. Para espacios de trabajo muy grandes, Braze puede mostrar recuentos estimados cuando los recuentos exactos no están disponibles.

## Evitar usuarios duplicados en formularios de captura de correo electrónico {#avoid-duplicate-users-from-email-capture-forms}

Antes de crear un usuario a partir de un formulario de captura de correo electrónico, llama a [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) para comprobar si el perfil ya existe. Si la respuesta es "User not found", crea el usuario con [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). De lo contrario, actualiza el perfil existente en lugar de crear un duplicado.

## Eventos `USERS_MESSAGES_EMAIL_UNSUBSCRIBE` de Snowflake {#snowflake-users_messages_email_unsubscribe-events}

La tabla de Snowflake `USERS_MESSAGES_EMAIL_UNSUBSCRIBE` registra las cancelaciones de suscripción de correo electrónico a nivel de mensaje que se originan del lado del destinatario: hacer clic en un enlace de cancelación de suscripción, la opción de cancelación de suscripción con un clic (List-Unsubscribe) del cliente de correo electrónico, envíos del centro de preferencias y cancelaciones de suscripción reportadas por el ESP. Las cancelaciones de suscripción realizadas a través de la REST API no se incluyen en esta tabla; en su lugar, emiten eventos [`users.behaviors.subscriptiongroup.StateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#subscription-group-state-change-events) o [`users.behaviors.subscription.GlobalStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#global-subscription-state-change-events).

## Mensajes de prueba SMS y grupos de suscripción {#sms-test-messages-and-subscription-groups}

Para recibir un mensaje de prueba SMS, el destinatario debe pertenecer al grupo de suscripción SMS que selecciones al enviar la prueba.