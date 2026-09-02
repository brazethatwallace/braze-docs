---
nav_title: Endpoints principais
permalink: "/core_endpoints/"
hidden: true
layout: dev_guide
---

# Endpoints principais da API or interface de programação do aplicativo (API) da Braze {#braze-core-api-endpoints}

<!-- This article is linked in our standard credits SLA exhibit, and was created to clarify what endpoints that are covered for SLA purposes. -->

Os endpoints principais da API or interface de programação do aplicativo (API) da Braze são endpoints específicos na REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze que possuem um tempo de inatividade permitido de acordo com o Acordo de Nível de Serviço (SLA) de uma conta da Braze. Para saber mais, consulte a documentação do seu SLA ou entre em contato com o gerente da sua conta.

Os endpoints principais incluem:
- [`/users/track`][1]
- [`/users/delete`][2]
- [`/email/status`][3]
- [`/email/blocklist`][4]
- [`/messages/send`][5]
- [`/messages/schedule/create`][6]
- [`/messages/schedule/update`][7]
- [`/messages/schedule/delete`][8]
- [`/campaigns/trigger/send`][9]
- [`/campaigns/trigger/schedule/create`][10]
- [`/campaigns/trigger/schedule/update`][11]
- [`/campaigns/trigger/schedule/delete`][12]
- [`/canvas/trigger/send`][13]
- [`/canvas/trigger/schedule/create`][14]
- [`/canvas/trigger/schedule/update`][15]
- [`/canvas/trigger/schedule/delete`][16]
- [`/subscription/status/set`][17]

[1]: {{site.baseurl}}/API or interface de programação do aplicativo (API)/endpoints/user_data/post_user_track
[2]: {{site.baseurl}}/API or interface de programação do aplicativo (API)/endpoints/user_data/post_user_delete
[3]: {{site.baseurl}}/API or interface de programação do aplicativo (API)/endpoints/email/post_email_subscription_status
[4]: {{site.baseurl}}/API or interface de programação do aplicativo (API)/endpoints/email/post_blocklist/
[5]: {{site.baseurl}}/API or interface de programação do aplicativo (API)/endpoints/messaging/send_messages/post_send_messages
[6]: {{site.baseurl}}/API or interface de programação do aplicativo (API)/endpoints/messaging/schedule_messages/post_schedule_messages/
[7]: {{site.baseurl}}/API or interface de programação do aplicativo (API)/endpoints/messaging/schedule_messages/post_update_scheduled_messages/
[8]: {{site.baseurl}}/API or interface de programação do aplicativo (API)/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/
[9]: {{site.baseurl}}/API or interface de programação do aplicativo (API)/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[10]: {{site.baseurl}}/API or interface de programação do aplicativo (API)/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/
[11]: {{site.baseurl}}/API or interface de programação do aplicativo (API)/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/
[12]: {{site.baseurl}}/API or interface de programação do aplicativo (API)/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/
[13]: {{site.baseurl}}/API or interface de programação do aplicativo (API)/endpoints/messaging/send_messages/post_send_triggered_canvases
[14]: {{site.baseurl}}/API or interface de programação do aplicativo (API)/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/
[15]: {{site.baseurl}}/API or interface de programação do aplicativo (API)/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/
[16]: {{site.baseurl}}/API or interface de programação do aplicativo (API)/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/
[17]: {{site.baseurl}}/API or interface de programação do aplicativo (API)/endpoints/subscription_groups/post_update_user_subscription_group_status/