---
nav_title: Limites de débit
article_title: Limites de débit
page_order: 4.5
description: "Cet article de référence couvre les limites de débit de l'API pour l'infrastructure API de Braze."
page_type: reference
---

# Limites de débit {#rate-limits}

> L'infrastructure API de Braze est conçue pour gérer des volumes élevés de données sur l'ensemble de notre base de clients. C'est pourquoi nous appliquons des limites de débit à l'API par espace de travail.

Une limite de débit correspond au nombre de requêtes que l'API peut recevoir sur une période donnée. De nombreux incidents de déni de service liés à la charge dans les grands systèmes sont involontaires — causés par des erreurs dans les logiciels ou les configurations — et non par des attaques malveillantes. Les limites de débit garantissent que de telles erreurs ne privent pas nos clients des ressources de l'API de Braze. Si trop de requêtes sont envoyées dans un délai donné, vous risquez de recevoir des réponses d'erreur avec un code d'état `429`, indiquant que la limite de débit a été atteinte.

{% alert warning %}
Les limites de débit de l'API sont susceptibles d'évoluer en fonction de l'utilisation appropriée de notre système. Nous vous encourageons à définir des limites raisonnables lors de vos appels API afin d'éviter tout dommage ou toute mauvaise utilisation.
{% endalert %}

## Limites de débit par type de requête {#rate-limits-by-request-type}

Consultez les informations suivantes pour connaître les limites de débit API par défaut selon les différents types de requêtes. Ces limites par défaut peuvent être augmentées sur demande. Contactez votre gestionnaire de la satisfaction client pour plus d'informations.

### Requêtes avec des limites de débit différentes {#requests-with-different-rate-limits}

| Type de requête | Limite de débit API par défaut |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) | **Requêtes :** les limites de débit varient en fonction de votre contrat. Pour les clients dont la tarification inclut des points de donnée, Braze applique une limite de rafale de 3 000 requêtes par trois secondes. Pour tous les autres clients, les limites sont configurées conformément aux conditions de votre contrat. Contactez le support Braze ou votre gestionnaire de la satisfaction client pour toute question sur vos limites.<br><br>**Regroupement :** jusqu'à 75 objets au total combinés entre `attributes`, `events` et `purchases` par requête API. Les clients soumis aux anciennes limites de débit peuvent inclure jusqu'à 75 objets par tableau de manière indépendante. Pour plus d'informations, consultez [Regroupement des requêtes User Track](#batch-user-track).<br><br>**Limites pour les utilisateurs actifs mensuels CY 24-25, MAU universels, MAU web et MAU mobile :** consultez [Limites des utilisateurs actifs mensuels CY 24-25]({{site.baseurl}}/api/endpoints/user_data/post_user_track#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau). |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) | **Si vous avez intégré Braze à partir du 22 août 2024 :** 250 requêtes par minute. <br><br> **Si vous avez intégré Braze avant le 22 août 2024 :** 2 500 requêtes par minute. |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)<br>[`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias)<br>[`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update)<br>[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)<br>[`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) | 20 000 requêtes par minute, partagées entre les endpoints. |
| [`/users/external_id/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename) | 1 000 requêtes par minute. |
| [`/users/external_id/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove) | 1 000 requêtes par minute. |
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | 1 000 requêtes par heure, partagées avec l'endpoint `/purchases/product_list`. |
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | 1 000 requêtes par heure, partagées avec l'endpoint `/events/list`. |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | 50 000 requêtes par minute. |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)<br>[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)<br>[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)<br>[`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns)<br>[`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases) | Pour les appels de diffusion (ciblant largement des Segments, des filtres ou une audience connectée), 250 requêtes par minute toutes audiences confondues, et 10 requêtes par minute par [audience unique]({{site.baseurl}}/api/api_limits#what-counts-as-the-same-unique-audience) (la première limite atteinte s'applique).<br><br>Dans le cas contraire, lorsque des destinataires individuels sont ciblés, la requête est incluse dans la [limite de débit partagée]({{site.baseurl}}/api/api_limits#requests-with-shared-rate-limits) de 250 000 requêtes par heure. |
| [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids) | 100 requêtes par jour. |
| [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) | 5 000 requêtes par minute. |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center)<br>[`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | 1 000 requêtes par minute. |
| [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center) | 10 requêtes par minute. |
| [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog) | 50 requêtes par minute partagées entre les endpoints. |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk) | 16 000 requêtes par minute partagées entre les endpoints. |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item) | 50 requêtes par minute partagées entre les endpoints. |
| [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)<br>[`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)<br>[`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)<br>[`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | 50 requêtes par minute partagées entre les endpoints. |
| [`/scim/v2/Users/{id}`]({{site.baseurl}}/get_see_user_account_information)<br>[`/scim/v2/Users?filter={userName@example.com}`]({{site.baseurl}}/get_search_existing_dashboard_user_email)<br>[`/scim/v2/Users/{id}`]({{site.baseurl}}/post_update_existing_user_account)<br>[`/scim/v2/Users/{id}}`]({{site.baseurl}}/delete_existing_dashboard_user)<br>[`/scim/v2/Users/`]({{site.baseurl}}/post_create_user_account) | 20 000 requêtes par jour, par entreprise, partagées entre les endpoints. |
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | 50 requêtes par minute. |
| [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | 20 requêtes par minute. |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync) | 100 requêtes par minute. |
| [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | 100 requêtes par heure. |
| [`/media_library/replace_file`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/replace_file) | 100 requêtes par heure. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requêtes avec des limites de débit différentes" }

### Requêtes avec des limites de débit partagées {#requests-with-shared-rate-limits}

Les requêtes suivantes ont une limite de débit de 250 000 requêtes par heure, partagée entre elles.

- [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key)
- [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys)
- [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details)
- [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) (uniquement pour les appels non diffusés — ceux qui spécifient `external_user_ids` ou `aliases`)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns) (uniquement pour les appels non diffusés)
- [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages)
- [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns)
- [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics)
- [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary)
- [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details)
- [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) (uniquement pour les appels non diffusés)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases) (uniquement pour les appels non diffusés)
- [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases)
- [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases)
- [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block)
- [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information)
- [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks)
- [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block)
- [`/email/blocklist`]({{site.baseurl}}/api/endpoints/email/post_blocklist)
- [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist)
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)
- [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status)
- [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses)
- [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics)
- [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date)
- [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days)
- [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date)
- [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date)
- [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start)
- [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) (uniquement pour les appels non diffusés)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)
- [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages)
- [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages)
- [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled)
- [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics)
- [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details)
- [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment)
- [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics)
- [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics)
- [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers)
- [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers)
- [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status)
- [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups)
- [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template)
- [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information)
- [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates)
- [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group)
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

### Qu'est-ce qui constitue la même audience unique ? {#what-counts-as-the-same-unique-audience}

Cela s'applique aux endpoints suivants : [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages), [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns), [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases), [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns) et [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases).

Pour ces endpoints, les requêtes de diffusion sont considérées comme ciblant la même audience unique lorsque tous les éléments suivants correspondent :

- La Campaign ou le Canvas déclenché (le `campaign_id` ou `canvas_id` dans votre requête API, s'il est spécifié)
- L'audience ciblée (les Segments ou les filtres, ou pour les Campaigns API, le `segment_id` dans votre requête API)
- Les filtres d'audience connectée (l'objet `audience` dans votre requête API, s'il est spécifié)

Chaque combinaison unique de ces attributs est considérée comme une audience distincte, de sorte que la limite de débit supplémentaire pour chaque audience unique s'applique indépendamment à chaque combinaison.

## Regroupement des requêtes API {#batching-api-requests}

Les API de Braze sont conçues pour prendre en charge le regroupement (batching). Grâce au regroupement, Braze peut ingérer autant de données que possible en un seul appel API, ce qui vous évite d'effectuer un grand nombre d'appels. Il est plus efficace pour Braze de traiter les données par lots que de les traiter appel par appel. Par exemple, le traitement de 1 000 appels API regroupés nécessite moins de ressources que le traitement de 75 000 appels individuels. Le regroupement est extrêmement important pour toute application susceptible de nécessiter plus de 75 000 appels par heure.

{% alert note %}
Les augmentations de la limitation du débit de la REST API sont envisagées en fonction des besoins des clients qui utilisent les fonctionnalités de regroupement de l'API.
{% endalert %}

### Regroupement des requêtes pour l'endpoint de création et de mise à jour des utilisateurs {#batch-user-track}

Chaque requête `/users/track` peut contenir jusqu'à 75 objets au total, répartis entre `attributes`, `events` et `purchases`. Chaque objet peut mettre à jour un utilisateur. Un seul profil utilisateur peut être mis à jour par plusieurs objets.

{% details Anciennes limites de débit %}
Pour les clients soumis aux anciennes limites de débit, chaque tableau (`attributes`, `events` et `purchases`) peut contenir jusqu'à 75 objets indépendamment, pour un maximum combiné de 225 objets par requête.
{% enddetails %}

Pour plus d'informations sur les limites de débit de `/users/track`, consultez [POST : Créer et mettre à jour des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

Les requêtes envoyées à cet endpoint commencent généralement à être traitées dans l'ordre suivant :

1. Attributs
2. Événements
3. Achats

### Regroupement des requêtes vers les endpoints de messaging {#batching-messaging-endpoint-requests}

Une seule requête vers les [endpoints de messaging]({{site.baseurl}}/api/endpoints/messaging) peut atteindre l'un des éléments suivants :

- Jusqu'à 50 `external_ids` spécifiques, chacun avec des paramètres de message individuels
- Un Segment de n'importe quelle taille créé dans le tableau de bord de Braze, spécifié par son `segment_id`
- Des utilisateurs correspondant à des filtres d'audience supplémentaires de n'importe quelle taille, définis dans la requête en tant qu'objet d'[audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience)

### Exemple de requête regroupée {#example-batch-request}

L'exemple suivant utilise `external_id` pour effectuer un seul appel API pour l'e-mail et le SMS.

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@example.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@example.com"]
    }
  ]
}
```

## Surveillance de vos limites de débit {#monitoring-your-rate-limits}

Chaque requête API envoyée à Braze renvoie les informations suivantes dans les en-têtes de réponse :

| Nom de l'en-tête        | Description                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | Le nombre maximum de requêtes que vous pouvez effectuer dans un intervalle donné (votre limite de débit). |
| `X-RateLimit-Remaining` | Le nombre de requêtes restantes dans la fenêtre actuelle de limitation du débit.            |
| `X-RateLimit-Reset`     | L'heure à laquelle la fenêtre actuelle de limitation du débit se réinitialise, en secondes epoch UTC. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Surveillance de vos limites de débit" }

Ces informations sont intentionnellement incluses dans l'en-tête de la réponse à la requête API plutôt que dans le tableau de bord de Braze. Cela permet à votre système de mieux réagir en temps réel lorsque vous interagissez avec notre API. Par exemple, si la valeur de `X-RateLimit-Remaining` descend en dessous d'un certain seuil, vous pouvez ralentir les envois pour vous assurer que tous les e-mails transactionnels sont bien délivrés. Ou, si elle atteint zéro, vous pouvez suspendre tous les envois jusqu'à ce que le délai spécifié dans `X-RateLimit-Reset` soit écoulé.

{% alert note %}
Les en-têtes HTTP sont renvoyés entièrement en minuscules. Ce comportement est conforme au protocole HTTP/2 qui impose que tous les noms de champs d'en-tête soient en minuscules. Cela diffère de HTTP/1.X où les noms d'en-tête n'étaient pas sensibles à la casse, mais étaient couramment écrits avec différentes capitalisations.
{% endalert %}

Si vous avez des questions sur les limites de l'API, contactez votre gestionnaire de la satisfaction client ou ouvrez un [ticket d'assistance]({{site.baseurl}}/user_guide/administer/personal/braze_support).

{% alert tip %}
Vous pouvez utiliser le [tableau de bord d'utilisation de l'API]({{site.baseurl}}/user_guide/analytics/dashboards/api_usage) pour visualiser et comparer le trafic entrant par rapport à vos limites de débit.
{% endalert %}

### Délai optimal entre les endpoints {#optimal-delay-between-endpoints}

{% alert note %}
Nous vous recommandons de prévoir un délai de 5 minutes entre les appels consécutifs aux endpoints afin de minimiser les erreurs.
{% endalert %}

Comprendre le délai optimal entre les endpoints est essentiel lorsque vous effectuez des appels consécutifs à l'API Braze. Des problèmes surviennent lorsque certains endpoints dépendent du traitement réussi d'autres endpoints, et s'ils sont appelés trop tôt, des erreurs peuvent se produire. Par exemple, si vous attribuez un alias à des utilisateurs via notre endpoint `/user/alias/new`, puis que vous utilisez cet alias pour envoyer un événement personnalisé via notre endpoint `/users/track`, combien de temps devez-vous attendre ?

Dans des conditions normales, le temps nécessaire à la cohérence éventuelle de nos données est de 10 à 100 ms (1/10 de seconde). Cependant, dans certains cas, cette cohérence peut prendre plus de temps. Nous recommandons donc de prévoir un délai de 5 minutes entre les appels consécutifs afin de minimiser la probabilité d'erreur.

## Limites de taille du payload {#payload-size-limits}

Les requêtes de l'API Braze sont soumises à des limites de taille du payload, distinctes des limites de débit. La plupart des endpoints acceptent des corps de requête jusqu'à 4&nbsp;Mo. Lorsqu'une requête dépasse la limite applicable, Braze peut la rejeter avec un code HTTP `413 Request Entity Too Large` ou HTTP `400 Bad Request`, selon l'endpoint.

L'endpoint [`/users/track/bulk`]({{site.baseurl}}/api/endpoints/user_data/post_user_track_bulk) a une limite de payload de 2&nbsp;Mo et renvoie un code HTTP `400` lorsque le corps de la requête dépasse cette limite. Pour les limites spécifiques à chaque endpoint et la gestion des erreurs, consultez [Endpoints de données utilisateur]({{site.baseurl}}/api/endpoints/user_data).

### Réinitialisation de la limite de débit {#rate-limit-reset}

Les limites de débit se réinitialisent à chaque heure pleine, et non sur une fenêtre glissante. Par exemple, si la limite est de 250 000 requêtes par heure, vous pourriez effectuer 50 000 requêtes entre 22 h 00 et 22 h 59, puis 250 000 requêtes supplémentaires entre 23 h 00 et 23 h 59, car le compteur se réinitialise au début de chaque heure.