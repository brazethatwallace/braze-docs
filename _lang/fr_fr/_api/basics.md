---
nav_title: "Aperçu de l'API"
article_title: "Aperçu de l'API"
page_order: 2.1
description: "Cet article de référence couvre les fondamentaux de l'API, y compris ce qu'est une API REST, sa terminologie et un aperçu des clés API."
page_type: reference
alias: /api/api_key/
---

# Aperçu de l'API {#api-overview}

> Cet article de référence couvre les bases de l'API, y compris la terminologie courante et un aperçu des clés de l'API REST, des autorisations et de la manière de les sécuriser.

## Collection REST API de Braze {#braze-rest-api-collection}

| Collection                                                                 | Objectif                                                                                             |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [Catalogues]({{site.baseurl}}/api/endpoints/catalogs)                      | Créer et gérer des catalogues et des éléments de catalogue à référencer dans vos Campaigns Braze.    |
| [Ingestion de données cloud]({{site.baseurl}}/api/endpoints/cdi)           | Gérer vos intégrations et synchronisations d'entrepôt de données.                                    |
| [Listes et adresses e-mail]({{site.baseurl}}/api/endpoints/email)          | Configurer et gérer la synchronisation bidirectionnelle entre Braze et vos systèmes d'e-mail.        |
| [Export]({{site.baseurl}}/api/endpoints/export)                            | Accéder à diverses informations sur vos Campaigns, Canvas, KPI, et plus encore, et les exporter.     |
| [Bibliothèque multimédia]({{site.baseurl}}/api/endpoints/media_library)    | Gérer les ressources dans Braze.                                                                     |
| [Messages]({{site.baseurl}}/api/endpoints/messaging)                       | Planifier, envoyer et gérer vos Campaigns et Canvas.                                                 |
| [Centre de préférences]({{site.baseurl}}/api/endpoints/preference_center)  | Créer votre centre de préférences et mettre à jour son style.                                        |
| [SCIM]({{site.baseurl}}/api/endpoints/scim)                                | Gérer les identités utilisateur dans les applications et services cloud.                             |
| [SMS]({{site.baseurl}}/api/endpoints/sms)                                  | Gérer les numéros de téléphone de vos utilisateurs dans vos groupes d'abonnement.                    |
| [Groupes d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups) | Répertorier et mettre à jour les groupes d'abonnement SMS et e-mail stockés dans le tableau de bord de Braze. |
| [Modèles]({{site.baseurl}}/api/endpoints/templates)                        | Créer et mettre à jour des modèles pour l'envoi d'e-mails et les Content Blocks.                    |
| [Données utilisateur]({{site.baseurl}}/api/endpoints/user_data)            | Identifier, suivre et gérer vos utilisateurs.                                                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Collection REST API de Braze" }

## Définitions de l'API {#api-definitions}

Voici un aperçu des termes que vous pouvez rencontrer dans la documentation de la REST API de Braze.

### Endpoints

Braze gère un certain nombre d'instances différentes pour notre tableau de bord et nos endpoints REST. Lorsque votre compte est provisionné, vous vous connectez à l'une des URL suivantes. Utilisez le bon endpoint REST en fonction de l'instance à laquelle vous êtes provisionné. Si vous n'êtes pas sûr, ouvrez un [ticket d'assistance]({{site.baseurl}}/user_guide/administer/personal/braze_support) ou utilisez le tableau suivant pour faire correspondre l'URL du tableau de bord que vous utilisez au bon endpoint REST.

Pour trouver votre endpoint REST dans Braze :

1. Connectez-vous à Braze et accédez à **Paramètres** > **API et identifiants** > **Clés API**.
2. Sélectionnez une clé API existante, ou sélectionnez **Créer une clé API** pour en créer une nouvelle.
3. Copiez l'endpoint REST affiché dans cet onglet et utilisez-le pour vos requêtes API.

{% alert important %}
Lorsque vous utilisez des endpoints pour des appels API, utilisez l'endpoint REST.

Pour l'intégration SDK, utilisez l'[endpoint SDK]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints), et non l'endpoint REST.
{% endalert %}

{% multi_lang_include administer/data_centers.md datacenters='instances' %}

### Limites de l'API {#api-limits}

Pour la plupart des API, Braze applique une limite de débit par défaut de 250 000 requêtes par heure. Cependant, certains types de requêtes ont leur propre limite de débit afin de mieux gérer les volumes élevés de données à travers la base de clients. Pour plus de détails, consultez [Limites de débit de l'API]({{site.baseurl}}/api/api_limits).

### ID utilisateur {#user-ids}

- **ID externe** : L'`external_id` sert d'identifiant unique pour l'utilisateur pour lequel vous soumettez des données. Cet identifiant doit être le même que celui que vous avez défini dans le SDK de Braze afin d'éviter de créer plusieurs profils pour le même utilisateur.
- **ID utilisateur Braze** : Le `braze_id` sert d'identifiant utilisateur unique défini par Braze. Vous pouvez utiliser cet identifiant pour supprimer des utilisateurs via la REST API en plus des external_ids.

Pour plus d'informations, consultez les articles suivants en fonction de votre plateforme : [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android) et [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web).

## À propos des clés API REST {#about-rest-api-keys}

Une clé API REST (clé d'API or interface de programmation d'applications REST) est un code unique que vous transmettez à une API pour authentifier l'appel API et identifier l'application ou l'utilisateur appelant. Vous accédez à l'API en utilisant des requêtes web HTTPS vers l'endpoint REST API de votre entreprise. Les clés API REST fonctionnent en tandem avec les clés d'identifiant d'application pour suivre, accéder, envoyer, exporter et analyser les données afin de s'assurer que tout fonctionne correctement.

Les espaces de travail et les clés API vont de pair chez Braze. Les espaces de travail sont conçus pour héberger les versions d'une même application sur plusieurs plateformes. De nombreux clients utilisent également les espaces de travail pour contenir les versions gratuites et premium de leurs applications sur la même plateforme. Comme vous pouvez le constater, ces espaces de travail utilisent également la REST API et disposent de leurs propres clés API REST. Ces clés peuvent être individuellement limitées pour inclure l'accès à des endpoints spécifiques de l'API. Chaque appel à l'API doit inclure une clé ayant accès à l'endpoint ciblé.

Nous désignons à la fois la clé API REST et la clé API d'espace de travail sous le nom `api_key`. La `api_key` est incluse dans chaque requête en tant qu'en-tête de requête et sert de clé d'authentification qui vous permet d'utiliser nos REST API. Ces REST API sont utilisées pour suivre les utilisateurs, envoyer des messages, exporter des données utilisateur et bien plus encore. Lorsque vous créez une nouvelle clé API REST, vous devez lui accorder l'accès à des endpoints spécifiques. En attribuant des permissions spécifiques à une clé API, vous pouvez limiter précisément les appels qu'une clé API peut authentifier.

![Panneau des clés API REST dans l'onglet Clés API.]({% image_buster /assets/img_archive/rest-api-key.png %})

{% alert tip %}
En plus des clés API REST, il existe également un type de clé appelé clés d'identifiant qui peut être utilisé pour référencer des éléments spécifiques tels que les applications, les modèles, les Canvas, les Campaigns, les Content Cards et les Segments depuis l'API. Pour plus d'informations, consultez [Types d'identifiants API]({{site.baseurl}}/api/identifier_types).
{% endalert %}

### Créer des clés API REST {#creating-rest-api-keys}

Pour créer une nouvelle clé API REST :

1. Allez dans **Paramètres** > **API et identifiants**.
2. Sélectionnez **Créer une clé API**.
3. Donnez un nom à votre nouvelle clé pour l'identifier d'un coup d'œil.
4. Spécifiez les [adresses IP autorisées](#api-ip-allowlisting) et les sous-réseaux pour la nouvelle clé.
5. Sélectionnez les [permissions](#rest-api-key-permissions) que vous souhaitez associer à votre nouvelle clé.

{% alert important %}
Gardez à l'esprit qu'après avoir créé une nouvelle clé API, vous ne pouvez pas modifier la portée des permissions ni les adresses IP autorisées. Cette limitation est en place pour des raisons de sécurité. Si vous devez modifier la portée d'une clé, créez une nouvelle clé avec les permissions mises à jour et implémentez cette clé à la place de l'ancienne. Une fois votre implémentation terminée, vous pouvez supprimer l'ancienne clé.
{% endalert %}

### Permissions des clés API REST {#rest-api-key-permissions}

Les permissions de clé API sont des permissions que vous pouvez attribuer à un utilisateur ou un groupe pour limiter leur accès à certains appels API. Pour afficher votre liste de permissions de clé API, allez dans **Paramètres** > **API et identifiants**, et sélectionnez votre clé API.

{% tabs %}
{% tab Données utilisateur %}

| Permission | Endpoint | Description |
|---|---|---|
| `users.track` | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) | Enregistrer les attributs utilisateur, les événements personnalisés et les achats. |
| `users.delete` | [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) | Supprimer n'importe quel utilisateur. |
| `users.alias.new` | [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias) | Créer un nouvel alias pour un utilisateur existant. |
| `users.identify` | [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) | Identifier un utilisateur alias uniquement avec un ID externe. |
| `users.export.ids` | [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) | Interroger les informations du profil utilisateur par ID utilisateur. |
| `users.export.segment` | [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) | Interroger les informations du profil utilisateur par Segment. |
| `users.merge` | [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) | Fusionner deux utilisateurs existants. |
| `users.external_ids.rename` | [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename) | Modifier l'ID externe d'un utilisateur existant. |
| `users.external_ids.remove` | [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove) | Supprimer l'ID externe d'un utilisateur existant. |
| `users.alias.update` | [`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update) | Mettre à jour un alias pour un utilisateur existant. |
| `users.export.global_control_group` | [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group) | Interroger les informations du profil utilisateur dans le groupe de contrôle global. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissions des clés API REST" }

 {% endtab %}
 {% tab E-mail %}

| Permission | Endpoint | Description |
|---|---|---|
| `email.unsubscribe` | [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses) | Interroger les adresses e-mail désabonnées. |
| `email.status` | [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status) | Modifier le statut d'une adresse e-mail. |
| `email.hard_bounces` | [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces) | Interroger les adresses e-mail ayant subi un échec d'envoi définitif. |
| `email.bounce.remove` | [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces) | Supprimer des adresses e-mail de votre liste d'échecs d'envoi définitifs. |
| `email.spam.remove` | [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam) | Supprimer des adresses e-mail de votre liste de spam. |
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist) | Ajouter des adresses e-mail à la liste de blocage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissions des clés API REST" }

{% endtab %}
{% tab Messages %}

| Permission | Endpoint | Description |
|---|---|---|
| `messages.send` | [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) | Envoyer un message immédiat à des utilisateurs spécifiques. |
| `messages.schedule.create` | [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages) | Planifier l'envoi d'un message à une heure spécifique. |
| `messages.schedule.update` | [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages) | Mettre à jour un message planifié. |
| `messages.schedule.delete` | [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages) | Supprimer un message planifié. |
| `messages.schedule_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | Interroger tous les messages de diffusion planifiés. |
| `messages.live_activity.update` | [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) | Mettre à jour une activité en direct or en ligne/en production/instantané iOS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissions des clés API REST" }

{% endtab %}
{% tab Campaigns %}

| Permission | Endpoint | Description |
|---|---|---|
| `campaigns.trigger.send` | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) | Déclencher l'envoi d'une Campaign existante. |
| `campaigns.trigger.schedule.create` | [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns) | Planifier l'envoi d'une Campaign avec une distribution déclenchée par API. |
| `campaigns.trigger.schedule.update` | [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns) | Mettre à jour une Campaign planifiée avec une distribution déclenchée par API. |
| `campaigns.trigger.schedule.delete` | [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages) | Supprimer une Campaign planifiée avec une distribution déclenchée par API. |
| `campaigns.list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | Interroger une liste de Campaigns. |
| `campaigns.data_series` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | Interroger les analyses d'une Campaign sur une période donnée. |
| `campaigns.details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | Interroger les détails d'une Campaign spécifique. |
| `sends.data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | Interroger les analyses d'envoi de messages sur une période donnée. |
| `sends.id.create` | [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids) | Créer un ID d'envoi pour le suivi des envois en masse. |
| `campaigns.url_info.details` | [`/campaigns/url_info/details`]({{site.baseurl}}) | Interroger les détails d'URL d'une variation de message spécifique au sein d'une Campaign. |
| `transactional.send` | [`/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) | Permet d'envoyer des messages transactionnels en utilisant l'endpoint de messagerie transactionnelle. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissions des clés API REST" }

{% endtab %}
{% tab Canvas %}

| Permission | Endpoint | Description |
|---|---|---|
| `canvas.trigger.send` | [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) | Déclencher l'envoi d'un Canvas existant. |
| `canvas.trigger.schedule.create` | [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases) | Planifier l'envoi d'un Canvas avec une distribution déclenchée par API. |
| `canvas.trigger.schedule.update` | [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases) | Mettre à jour un Canvas planifié avec une distribution déclenchée par API. |
| `canvas.trigger.schedule.delete` | [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases) | Supprimer un Canvas planifié avec une distribution déclenchée par API. |
| `canvas.list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | Interroger une liste de Canvas. |
| `canvas.data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | Interroger les analyses d'un Canvas sur une période donnée. |
| `canvas.details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | Interroger les détails d'un Canvas spécifique. |
| `canvas.data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | Interroger les récapitulatifs des analyses d'un Canvas sur une période donnée. |
| `canvas.url_info.details` | [`/canvas/url_info/details`]({{site.baseurl}}/get_canvas_link_alias) | Interroger les détails d'URL d'une variation de message spécifique au sein d'une étape Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissions des clés API REST" }

{% endtab %}
{% tab Segments %}

| Permission | Endpoint | Description |
|---|---|---|
| `segments.list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | Interroger une liste de Segments. |
| `segments.data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | Interroger les analyses d'un Segment sur une période donnée. |
| `segments.details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | Interroger les détails d'un Segment spécifique. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissions des clés API REST" }

{% endtab %}
{% tab Achats %}

| Permission | Endpoint | Description |
|---|---|---|
| `purchases.product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | Interroger une liste de produits achetés dans votre application. |
| `purchases.revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | Interroger le total d'argent dépensé par jour dans votre application sur une période donnée. |
| `purchases.quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | Interroger le nombre total d'achats par jour dans votre application sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissions des clés API REST" }

{% endtab %}
{% tab Événements %}

| Permission | Endpoint | Description |
|---|---|---|
| `events.list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | Interroger une liste d'événements personnalisés. |
| `events.data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | Interroger les occurrences d'un événement personnalisé sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissions des clés API REST" }

{% endtab %}
{% tab Sessions %}

| Permission | Endpoint | Description |
|---|---|---|
| `sessions.data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | Interroger les sessions par jour sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissions des clés API REST" }

{% endtab %}
{% tab KPI %}

| Permission | Endpoint | Description |
|---|---|---|
| `kpi.dau.data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | Interroger les utilisateurs actifs uniques par jour sur une période donnée. |
| `kpi.mau.data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | Interroger le total d'utilisateurs actifs uniques sur une fenêtre glissante de 30 jours sur une période donnée. |
| `kpi.new_users.data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | Interroger les nouveaux utilisateurs par jour sur une période donnée. |
| `kpi.uninstalls.data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | Interroger les désinstallations d'application par jour sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissions des clés API REST" }

{% endtab %}
{% tab Modèles %}

| Permission | Endpoint | Description |
|---|---|---|
| `templates.email.create` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | Créer un nouveau modèle d'e-mail sur le tableau de bord. |
| `templates.email.info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | Interroger les informations d'un modèle spécifique. |
| `templates.email.list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | Interroger une liste de modèles d'e-mail. |
| `templates.email.update` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | Mettre à jour un modèle d'e-mail stocké sur le tableau de bord. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissions des clés API REST" }

{% endtab %}
{% tab authentification unique %}

| Permission | Description |
| --- | --- |
| `sso.saml.login` | Configurer la connexion initiée par le fournisseur d'identité. Pour plus d'informations, consultez [Connexion initiée par le fournisseur de service (SP)]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permissions des clés API REST" }

{% endtab %}
{% tab Content Blocks %}

| Permission | Endpoint | Description |
|---|---|---|
| `content_blocks.info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | Interroger les informations d'un modèle spécifique. |
| `content_blocks.list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | Interroger une liste de Content Blocks. |
| `content_blocks.create` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | Créer un nouveau Content Block sur le tableau de bord. |
| `content_blocks.update` | [`/content_blocks_update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | Mettre à jour un Content Block existant sur le tableau de bord. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissions des clés API REST" }

{% endtab %}
{% tab Centre de préférences %}

| Permission | Endpoint | Description |
|---|---|---|
| `preference_center.get` | [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | Obtenir un centre de préférences. |
| `preference_center.list` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | Lister les centres de préférences. |
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center) | Créer ou mettre à jour un centre de préférences. |
| `preference_center.user.get` | [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | Obtenir un lien de centre de préférences pour un utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissions des clés API REST" }

{% endtab %}
{% tab Abonnement %}

| Permission | Endpoint | Description |
|---|---|---|
| `subscription.status.set` | [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) | Définir le statut du groupe d'abonnement. |
| `subscription.status.get` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | Obtenir le statut du groupe d'abonnement. |
| `subscription.groups.get` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | Obtenir le statut des groupes d'abonnement auxquels des utilisateurs spécifiques sont explicitement abonnés et désabonnés. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissions des clés API REST" }

{% endtab %}
{% tab SMS %}

| Permission | Endpoint | Description |
|---|---|---|
| `sms.invalid_phone_numbers` | [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers) | Interroger les numéros de téléphone invalides. |
| `sms.invalid_phone_numbers.remove` | [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers) | Supprimer le marqueur de numéro de téléphone invalide des utilisateurs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissions des clés API REST" }

{% endtab %}
{% tab Catalogues %}

| Permission | Endpoint | Description |
|---|---|---|
| `catalogs.add_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk) | Ajouter plusieurs éléments à un catalogue existant. |
| `catalogs.update_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk) | Mettre à jour plusieurs éléments dans un catalogue existant. |
| `catalogs.delete_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | Supprimer plusieurs éléments d'un catalogue existant. |
| `catalogs.get_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | Obtenir un seul élément d'un catalogue existant. |
| `catalogs.update_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item) | Mettre à jour un seul élément dans un catalogue existant. |
| `catalogs.create_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item) | Créer un seul élément dans un catalogue existant. |
| `catalogs.delete_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item) | Supprimer un seul élément d'un catalogue existant. |
| `catalogs.replace_item` | [` /catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item) | Remplacer un seul élément d'un catalogue existant. |
| `catalogs.create` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog) | Créer un catalogue. |
| `catalogs.get` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | Obtenir une liste de catalogues. |
| `catalogs.delete` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog) | Supprimer un catalogue. |
| `catalogs.get_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | Obtenir un aperçu des éléments d'un catalogue existant. |
| `catalogs.replace_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items) | Remplacer des éléments dans un catalogue existant. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissions des clés API REST" }

{% endtab %}
{% tab Authentification SDK %}

| Permission | Endpoint | Description |
|---|---|---|
| `sdk_authentication.create` | [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key) | Créer une nouvelle clé d'authentification SDK pour votre application. |
| `sdk_authentication.primary` | [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key) | Marquer une clé d'authentification SDK comme clé principale pour votre application. |
| `sdk_authentication.delete` | [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key) | Supprimer une clé d'authentification SDK pour votre application. |
| `sdk_authentication.keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | Obtenir toutes les clés d'authentification SDK pour votre application. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissions des clés API REST" }

{% endtab %}
{% endtabs %}

### Gérer les clés API REST {#managing-rest-api-keys}

Vous pouvez consulter les détails ou supprimer des clés API REST existantes depuis **Paramètres** > **API et identifiants** > onglet **Clés API**. Notez que vous ne pouvez pas modifier les clés API REST après les avoir créées.

L'onglet **Clés API** inclut les informations suivantes pour chaque clé :

| Champ | Description |
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
| Nom de la clé API | Le nom donné à la clé lors de sa création. |
| Identifiant | La clé API. |
| Créée par | L'adresse e-mail de l'utilisateur qui a créé la clé. Ce champ affiche « N/A » pour les clés créées avant juin 2023. |
| Date de création | La date à laquelle cette clé a été créée. |
| Dernière utilisation | La date à laquelle cette clé a été utilisée pour la dernière fois. Ce champ affiche « N/A » pour les clés qui n'ont jamais été utilisées. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gérer les clés API REST" }

Pour afficher les détails d'une clé API, survolez la clé et sélectionnez <i class="fa-solid fa-eye" alt="Voir"></i> **Voir**. Cela inclut toutes les permissions de cette clé, les adresses IP autorisées (le cas échéant) et si cette clé est activée pour la liste d'autorisation IP de Braze.

![La liste des permissions de clé API dans le tableau de bord de Braze.]({% image_buster /assets/img_archive/view-api-key.png %})

Notez que lors de la [suppression d'un utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users), Braze ne supprime pas les clés API associées que cet utilisateur a créées. Pour supprimer une clé, survolez la clé et sélectionnez <i class="fa-solid fa-trash-can" alt="Supprimer"></i> **Supprimer**.

![Une clé API nommée « Dernière utilisation » avec l'icône de corbeille mise en évidence, affichant « Supprimer ».]({% image_buster /assets/img_archive/api-key-options.png %}){: style="max-width:30%;"}

### Sécurité des clés API REST {#rest-api-key-security}

Les clés API sont utilisées pour authentifier un appel API. Lorsque vous créez une nouvelle clé API REST, vous devez lui accorder l'accès à des endpoints spécifiques. En attribuant des permissions spécifiques à une clé API, vous pouvez limiter précisément les appels qu'une clé API peut authentifier.

Étant donné que les clés API REST permettent l'accès à des endpoints REST API potentiellement sensibles, sécurisez ces clés et ne les partagez qu'avec des partenaires de confiance. Elles ne doivent jamais être exposées publiquement. Par exemple, n'utilisez pas cette clé pour effectuer des appels AJAX depuis votre site web et ne l'exposez d'aucune autre manière publique.

Une bonne pratique de sécurité consiste à n'accorder à un utilisateur que l'accès nécessaire à l'accomplissement de ses tâches : ce principe peut également être appliqué aux clés API en attribuant des permissions à chaque clé. Ces permissions vous offrent un meilleur contrôle de la sécurité sur les différentes zones de votre compte.

{% alert warning %}
Étant donné que les clés API REST permettent l'accès à des endpoints REST API potentiellement sensibles, assurez-vous qu'elles sont stockées et utilisées de manière sécurisée. Par exemple, n'utilisez pas cette clé pour effectuer des appels AJAX depuis votre site web et ne l'exposez d'aucune autre manière publique.
{% endalert %}

Si vous exposez accidentellement une clé, vous pouvez la supprimer depuis la console de développement. Pour obtenir de l'aide avec ce processus, ouvrez un [ticket de support]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Sécurité des clés API REST et des clés API SDK {#security-of-rest-api-keys-and-sdk-api-keys}

Les clés API REST et les clés API SDK ont des profils de sécurité différents.

| | Clés API REST | Clés API SDK |
|---|---|---|
| Objectif | Authentification côté serveur pour la REST API (envoi de messages, exportation de données, gestion des utilisateurs) | Identification côté client pour le SDK Braze (ingestion de données, In-App Messages, Content Cards) |
| Visibilité | **Doivent rester privées**. Ne jamais les exposer dans du code côté client, des dépôts publics ou des applications utilisateur. | Conçues pour être publiques. Intégrées dans le binaire de votre application ou visibles dans le JavaScript du navigateur web, similairement à un identifiant de suivi Google Analytics. |
| Solution en cas d'exposition | Révoquez immédiatement la clé et créez un remplacement dans **Paramètres** > **API et identifiants** > **Clés API**. Une clé API REST exposée peut être utilisée pour envoyer des messages, exporter des données utilisateur ou modifier les paramètres du compte. | Aucune action requise. Une clé API SDK ne peut qu'ingérer des données et récupérer les messages côté client (tels que les In-App Messages et les Content Cards). Elle ne peut pas exporter des données utilisateur, envoyer des messages en votre nom ou modifier des Campaigns. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sécurité des clés API REST et des clés API SDK" }

### Liste d'autorisation IP pour l'API {#api-ip-allowlisting}

Pour une sécurité renforcée, vous pouvez spécifier une liste d'adresses IP et de sous-réseaux autorisés à effectuer des requêtes REST API pour une clé API REST donnée. C'est ce qu'on appelle la liste d'autorisation (allowlisting ou whitelisting). Pour autoriser des adresses IP ou des sous-réseaux spécifiques, ajoutez-les dans la section **Whitelist IPs** lors de la création d'une nouvelle clé API REST :

![Option pour autoriser des adresses IP lors de la création d'une clé API.]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Si vous n'en spécifiez aucune, les requêtes pourront être envoyées depuis n'importe quelle adresse IP.

{% alert tip %}
Si vous créez un webhook Braze vers Braze et utilisez une liste d'autorisation, consultez la liste des [adresses IP à autoriser]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook).
{% endalert %}

## Authentification et sécurité de l'API {#api-authentication-and-security}

### Authentification par jeton Bearer {#bearer-token-authentication}

Braze authentifie les requêtes de l'API REST à l'aide de la clé API REST transmise en tant que jeton Bearer dans l'en-tête de requête `Authorization`. Lorsque vous envoyez une requête, incluez votre clé API au format suivant :

```bash
Authorization: Bearer YOUR_REST_API_KEY
```

À chaque requête, Braze effectue les vérifications de validation côté serveur suivantes :

1. **Validité du jeton :** Vérifie que la clé API REST existe dans Braze et qu'elle est active (par exemple, qu'elle n'a pas été révoquée ou désactivée).
2. **Autorisation du jeton :** Confirme que la clé API dispose des permissions requises pour l'endpoint demandé.

Si l'authentification échoue, l'API renvoie une réponse d'erreur avec un code de statut HTTP. Par exemple, `401 Unauthorized` indique une clé invalide ou manquante, tandis que `403 Forbidden` indique que la clé ne dispose pas des permissions nécessaires pour l'endpoint demandé. Pour en savoir plus, consultez la section [Erreurs API]({{site.baseurl}}/api/errors).

### Casse des en-têtes de requête {#header-casing}

Les noms d'en-têtes HTTP ne sont pas sensibles à la casse, donc `Authorization` et `authorization` sont équivalents. Il en va de même pour les autres en-têtes de requête standard, tels que `Content-Type`. Envoyez la casse que votre client HTTP produit.

Braze accepte également toute casse du schéma `Bearer` (`Bearer`, `bearer` ou `BEARER`). Envoyez la clé API REST exactement telle qu'elle a été émise.

### Sécurité au niveau du réseau {#network-level-security}

Les requêtes de l'API REST vers Braze sont protégées par le chiffrement TLS (sécurité de la couche de transport) sur l'ensemble du chemin de la requête. Le tableau suivant décrit le flux réseau d'une requête API depuis votre serveur vers Braze :

| Étape | Composant | Description |
| --- | --- | --- |
| 1 | Votre serveur | Initie une requête HTTPS avec chiffrement TLS. |
| 2 | Cloudflare | Met fin à la connexion TLS du client et applique les protections au niveau du réseau. |
| 3 | Network Load Balancer (NLB) | Transfère les paquets vers l'infrastructure applicative. Les NLB opèrent au niveau de la couche 4, ce qui signifie qu'il n'y a pas de proxy au niveau de la couche 7. Les paquets sont transmis sans inspection ni modification au niveau HTTP. |
| 4 | NGINX ingress | Met fin à la connexion TLS interne et route la requête. |
| 5 | Unicorn (serveur d'application) | Traite la requête authentifiée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sécurité au niveau du réseau" }

Le chiffrement TLS couvre chaque maillon de la chaîne. Votre serveur se connecte à Cloudflare via TLS, et Cloudflare établit une connexion TLS distincte à travers le NLB vers le NGINX ingress, de sorte que votre clé API et les données de la requête restent chiffrées en transit.

## Ressources supplémentaires {#additional-resources}

### Bibliothèque client Ruby {#ruby-client-library}

Si vous déployez Braze avec Ruby, vous pouvez utiliser la [bibliothèque client Ruby](https://github.com/braze-inc/braze-api-client-ruby) pour réduire le temps d'importation de vos données. Une bibliothèque client est un ensemble de code spécifique à un langage de programmation — dans ce cas, Ruby — qui facilite l'utilisation d'une API.

La bibliothèque client Ruby prend en charge les [endpoints User]({{site.baseurl}}/api/endpoints/user_data).

{% alert important %}
Cette bibliothèque client est en version bêta. Pour nous aider à l'améliorer, envoyez vos commentaires à [smb-product@braze.com](mailto:smb-product@braze.com).
{% endalert %}