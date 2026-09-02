---
nav_title: "Référence des tables SQL"
article_title: "Référence des tables SQL"
page_order: 3
page_type: reference
toc_headers: h2
description: "Cette page est une référence des tables et colonnes SQL Snowflake utilisées dans le générateur de requêtes, les extensions de segments SQL et le partage de données Snowflake."
tool: Segments
---

<style>
table td {
   word-break: keep-all;
}
</style>

# Référence des tables SQL {#sql-table-reference}

Cette page est une référence des tables et colonnes SQL Snowflake disponibles dans les outils Braze suivants :

- [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder)
- [Extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)
- [Partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)

La plupart des tables sont disponibles dans les trois outils. Les tables marquées **Partage de données Snowflake uniquement** sont exclusives au partage de données Snowflake et ne sont pas accessibles dans le générateur de requêtes ni dans les extensions de segments SQL.

{% alert tip %}
Ces tables SQL correspondent aux événements documentés dans le [glossaire des événements Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events). Par exemple, la table SQL `USERS_MESSAGES_EMAIL_SEND_SHARED` correspond à l'événement Currents `users.messages.email.Send`. Si vous avez besoin de schémas d'événements JSON ou de formats spécifiques aux partenaires (Amplitude, Mixpanel, Segment), consultez le glossaire Currents.
{% endalert %}

## Table des matières {#table-of-contents}

Table | Description
------|------------
[AGENTCONSOLE_AGENTEXECUTED_SHARED](#AGENTCONSOLE_AGENTEXECUTED_SHARED) | Lorsqu'un agent Agent Console est exécuté (**Snowflake Data Sharing uniquement**)
[AGENTCONSOLE_RAWLLMREQUEST_SHARED](#AGENTCONSOLE_RAWLLMREQUEST_SHARED) | Informations brutes de chaque appel LLM (**Snowflake Data Sharing uniquement**)
[AGENTCONSOLE_TOOLINVOCATION_SHARED](#AGENTCONSOLE_TOOLINVOCATION_SHARED) | Lorsqu'un outil est exécuté (**Snowflake Data Sharing uniquement**)
[USER_CUSTOM_ATTRIBUTES_VIEW_SHARED](#USER_CUSTOM_ATTRIBUTES_VIEW_SHARED) | Instantané périodique des attributs personnalisés de profil par utilisateur
[USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED](#USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED) | Historique des attributs de profil par défaut avec plages de dates d'effet
[USER_DEFAULT_ATTRIBUTES_VIEW_SHARED](#USER_DEFAULT_ATTRIBUTES_VIEW_SHARED) | Instantané périodique des attributs de profil par défaut par utilisateur
[USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED](#USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED) | Attributs de profil par défaut par utilisateur en quasi temps réel
[USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED](#USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED) | Historique des attributs personnalisés de profil avec plages de dates d'effet (**Snowflake Data Sharing uniquement**)
[USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED](#USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED) | Attributs personnalisés de profil par utilisateur en quasi temps réel (**Snowflake Data Sharing uniquement**)
[CATALOGS_ITEMS_SHARED](#CATALOGS_ITEMS_SHARED) | Éléments de catalogue non supprimés
[CHANGELOGS_CAMPAIGN_SHARED](#CHANGELOGS_CAMPAIGN_SHARED) | Lorsqu'une Campaign est modifiée (**Snowflake Data Sharing uniquement**)
[CHANGELOGS_CANVAS_SHARED](#CHANGELOGS_CANVAS_SHARED) | Lorsqu'un Canvas est modifié (**Snowflake Data Sharing uniquement**)
[CHANGELOGS_GLOBALCONTROLGROUP_SHARED](#CHANGELOGS_GLOBALCONTROLGROUP_SHARED) | Lorsque le groupe de contrôle global est modifié
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | Lorsqu'un utilisateur effectue un événement personnalisé
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | Lorsqu'un utilisateur installe une application et que l'installation est attribuée à un partenaire
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | Lorsqu'un utilisateur enregistre un emplacement
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | Lorsqu'un utilisateur effectue un achat
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | Lorsqu'un utilisateur désinstalle une application
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | Lorsqu'un utilisateur met à jour l'application
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | Lorsqu'un utilisateur a sa première session
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | Lorsqu'un utilisateur consulte le News Feed
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | Lorsqu'un utilisateur termine une session sur une application
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | Lorsqu'un utilisateur démarre une session sur une application
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | Lorsqu'un utilisateur déclenche une zone de géorepérage — par exemple, en entrant ou en sortant d'un géorepérage. Cet événement est regroupé avec d'autres événements et reçu via l'endpoint d'événements standard, il peut donc ne pas apparaître en temps réel.<br><br>Pour enregistrer l'activité de géorepérage dans ce tableau, sélectionnez **Enable Analytics for Enter** et **Enable Analytics for Exit** dans les paramètres avancés de chaque géorepérage. Consultez l'étape 3 dans [Créer manuellement des géorepérages]({{site.baseurl}}/user_guide/audience/locations_and_geofences/creating_geofences#manually-create-geofences) pour plus de détails.
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | Lorsqu'un utilisateur déclenche une zone de géorepérage (par exemple, lorsqu'il entre ou sort d'un géorepérage). Cet événement est reçu via l'endpoint dédié au géorepérage et est donc reçu en temps réel dès que l'appareil de l'utilisateur détecte qu'il a déclenché un géorepérage. <br><br>De plus, en raison de la limitation du débit sur l'endpoint de géorepérage, il est possible que certains événements de géorepérage ne soient pas reflétés en tant que RecordEvent. Cependant, tous les événements de géorepérage sont représentés par DataEvent (mais potentiellement avec un certain délai dû au regroupement).
[USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED) | Lorsqu'un jeton push-to-start de en direct or en ligne/en production/instantané Activity change
[USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED) | Lorsqu'un jeton de mise à jour de en direct or en ligne/en production/instantané Activity change
[USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED](#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED) | Lorsque l'état d'un jeton de notification push change
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | Lorsqu'un utilisateur est abonné ou désabonné globalement d'un canal tel que l'e-mail
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | Lorsqu'un utilisateur est abonné ou désabonné d'un groupe d'abonnement
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | Lorsqu'un utilisateur effectue une conversion pour une Campaign
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | Lorsqu'un utilisateur est inscrit dans le groupe de contrôle d'une Campaign
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | Lorsqu'un utilisateur est soumis à une limitation de fréquence pour une Campaign
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | Lorsqu'un utilisateur génère du chiffre d'affaires pendant la période de conversion principale
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | Lorsqu'un utilisateur progresse vers une étape du Canvas
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | Lorsqu'un utilisateur effectue une conversion pour un événement de conversion Canvas
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | Lorsqu'un utilisateur entre dans un Canvas
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | Lorsqu'un utilisateur sort d'un Canvas parce qu'il correspond aux critères de sortie d'audience
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | Lorsqu'un utilisateur sort d'un Canvas parce qu'il a effectué un événement d'exception
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | Lorsqu'un utilisateur effectue une conversion pour une étape d'expérience Canvas
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | Lorsqu'un utilisateur entre dans le chemin d'une étape d'expérience
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | Lorsqu'un utilisateur est soumis à une limitation de fréquence pour une étape du Canvas
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | Lorsqu'un utilisateur génère du chiffre d'affaires pendant la période de l'événement de conversion principal
[USERS_MESSAGES_BANNER_ABORT_SHARED](#USERS_MESSAGES_BANNER_ABORT_SHARED) | Un message de bannière initialement planifié a été abandonné pour une raison quelconque
[USERS_MESSAGES_BANNER_CLICK_SHARED](#USERS_MESSAGES_BANNER_CLICK_SHARED) | Lorsqu'un utilisateur clique sur une bannière
[USERS_MESSAGES_BANNER_IMPRESSION_SHARED](#USERS_MESSAGES_BANNER_IMPRESSION_SHARED) | Lorsqu'un utilisateur visualise une bannière
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | Un message Content Card initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | Lorsqu'un utilisateur clique sur une Content Card
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | Lorsqu'un utilisateur ferme une Content Card
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | Lorsqu'un utilisateur visualise une Content Card
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | Lorsque nous envoyons une Content Card à un utilisateur
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | Un e-mail initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | Un fournisseur de services d'e-mail marketing or e-mailing a renvoyé un échec d'envoi définitif. Un échec d'envoi définitif indique un problème permanent de livrabilité.
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | Lorsqu'un utilisateur clique sur un lien dans un e-mail
[USERS_MESSAGES_EMAIL_DEFERRAL_SHARED](#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED) | Lorsqu'un e-mail est différé
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | Lorsqu'un e-mail est distribué
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | Lorsqu'un e-mail est signalé comme courrier indésirable
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | Lorsqu'un utilisateur ouvre un e-mail
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | Lorsque nous envoyons un e-mail à un utilisateur
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | Lorsqu'un e-mail subit un échec provisoire d'envoi
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | Lorsqu'un utilisateur se désabonne des e-mails
[USERS_MESSAGES_EMAIL_RETRY_SHARED](#USERS_MESSAGES_EMAIL_RETRY_SHARED) | Lorsqu'un e-mail est réessayé après avoir été dépriorisé ou soumis à une limitation de fréquence (**Snowflake Data Sharing uniquement**)
[USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED](#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED) | Lorsqu'un utilisateur visualise un feature flag
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | Un message in-app initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | Lorsqu'un utilisateur clique sur un message in-app
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | Lorsqu'un utilisateur visualise un message in-app
[USERS_MESSAGES_LINE_ABORT_SHARED](#USERS_MESSAGES_LINE_ABORT_SHARED) | Lorsqu'un message LINE planifié ne peut pas être distribué, avant l'envoi à LINE
[USERS_MESSAGES_LINE_CLICK_SHARED](#USERS_MESSAGES_LINE_CLICK_SHARED) | Lorsqu'un utilisateur clique sur un lien dans un message LINE
[USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED) | Lorsqu'un message LINE est reçu d'un utilisateur
[USERS_MESSAGES_LINE_SEND_SHARED](#USERS_MESSAGES_LINE_SEND_SHARED) | Lorsqu'un message LINE est envoyé à LINE
[USERS_MESSAGES_LINE_RETRY_SHARED](#USERS_MESSAGES_LINE_RETRY_SHARED) | Lorsqu'un message LINE est réessayé après avoir été dépriorisé ou soumis à une limitation de fréquence (**Snowflake Data Sharing uniquement**)
[USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED](#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED) | Lorsqu'une en direct or en ligne/en production/instantané Activity a un événement de résultat
[USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED](#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED) | Lorsqu'un message en direct or en ligne/en production/instantané Activity est envoyé
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | Un message de carte News Feed initialement planifié a été abandonné pour une raison quelconque
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | Lorsqu'un utilisateur clique sur une carte News Feed
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | Lorsqu'un utilisateur visualise une carte News Feed
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | Un message de notification push initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | Lorsqu'une notification push rebondit
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | Lorsqu'un utilisateur ouvre l'application après avoir reçu une notification sans cliquer sur la notification
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | Lorsqu'un utilisateur reçoit une notification push alors que l'application est ouverte. <br><br>Cet événement n'est pas pris en charge par le [SDK Swift](https://github.com/braze-inc/braze-swift-sdk) et est obsolète dans le [SDK Obj-C](https://github.com/Appboy/appboy-ios-sdk).
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | Lorsqu'un utilisateur ouvre une notification push ou clique sur un bouton de notification push (y compris un bouton FERMER qui n'ouvre PAS l'application). <br><br> Les actions des boutons de notification push ont plusieurs résultats possibles. No, Decline et Cancel sont des « clics », tandis que les actions Accept sont des « ouvertures ». Les deux sont représentés dans ce tableau, mais ils peuvent être distingués dans la colonne **BUTTON_ACTION_TYPE**. Par exemple, une requête peut être utilisée pour regrouper par un `BUTTON_ACTION_TYPE` qui n'est pas No, Decline ou Cancel.
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | Lorsque nous envoyons une notification push à un utilisateur
[USERS_MESSAGES_RCS_ABORT_SHARED](#USERS_MESSAGES_RCS_ABORT_SHARED) | Lorsqu'un envoi RCS est interrompu en raison d'une erreur détectée dans Braze et que le message est abandonné
[USERS_MESSAGES_RCS_CLICK_SHARED](#USERS_MESSAGES_RCS_CLICK_SHARED) | Lorsque l'utilisateur final interagit avec un message RCS en appuyant ou en cliquant sur un élément d'interface
[USERS_MESSAGES_RCS_DELIVERY_SHARED](#USERS_MESSAGES_RCS_DELIVERY_SHARED) | Lorsqu'un message RCS est distribué avec succès sur l'appareil mobile de l'utilisateur final
[USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED) | Lorsque Braze reçoit un message RCS provenant de l'utilisateur final
[USERS_MESSAGES_RCS_READ_SHARED](#USERS_MESSAGES_RCS_READ_SHARED) | Lorsque l'utilisateur final ouvre un message RCS sur son appareil
[USERS_MESSAGES_RCS_REJECTION_SHARED](#USERS_MESSAGES_RCS_REJECTION_SHARED) | Lorsqu'un message RCS n'est pas distribué en raison d'une intervention de l'opérateur
[USERS_MESSAGES_RCS_SEND_SHARED](#USERS_MESSAGES_RCS_SEND_SHARED) | Lorsqu'un message RCS est envoyé depuis les systèmes de Braze vers les partenaires de distribution finale
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | Un message SMS initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | Lorsqu'un message SMS est envoyé à l'opérateur
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | Lorsqu'un message SMS est distribué
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Lorsque Braze ne parvient pas à distribuer le message SMS au fournisseur de services SMS
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | Lorsqu'un message SMS est reçu d'un utilisateur
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | Lorsqu'un message SMS n'est pas distribué à un utilisateur
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | Lorsqu'un message SMS est envoyé
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | Lorsqu'un utilisateur clique sur une URL raccourcie Braze incluse dans un message SMS
[USERS_MESSAGES_SMS_RETRY_SHARED](#USERS_MESSAGES_SMS_RETRY_SHARED) | Lorsqu'un message SMS est réessayé après avoir été dépriorisé ou soumis à une limitation de fréquence (**Snowflake Data Sharing uniquement**)
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | Un message webhook initialement planifié a été abandonné pour une raison quelconque
[USERS_MESSAGES_WEBHOOK_FAILURE_SHARED](#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED) | Lorsqu'un message webhook est distribué mais échoue avec une réponse d'erreur de l'endpoint
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | Lorsque nous envoyons un webhook pour un utilisateur
[USERS_MESSAGES_WEBHOOK_RETRY_SHARED](#USERS_MESSAGES_WEBHOOK_RETRY_SHARED) | Lorsqu'un message webhook est réessayé après avoir été dépriorisé ou soumis à une limitation de fréquence (**Snowflake Data Sharing uniquement**)
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | Un message WhatsApp initialement planifié a été abandonné pour une raison quelconque
[USERS_MESSAGES_WHATSAPP_CLICK_SHARED](#USERS_MESSAGES_WHATSAPP_CLICK_SHARED) | Lorsqu'un utilisateur clique sur un lien ou un bouton dans un message WhatsApp
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) | Lorsqu'un message WhatsApp est distribué
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | Lorsqu'un message WhatsApp n'est pas distribué à un utilisateur
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | Lorsqu'un message WhatsApp est reçu d'un utilisateur
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | Lorsqu'un utilisateur ouvre un message WhatsApp
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | Lorsque nous envoyons un message WhatsApp pour un utilisateur
[USERS_MESSAGES_WHATSAPP_RETRY_SHARED](#USERS_MESSAGES_WHATSAPP_RETRY_SHARED) | Lorsqu'un message WhatsApp est réessayé après avoir été dépriorisé ou soumis à une limitation de fréquence (**Snowflake Data Sharing uniquement**)
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | Lorsque le numéro de compartiment aléatoire d'un utilisateur est modifié
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | Lorsqu'un utilisateur est supprimé à la demande d'un client
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | Lorsqu'un utilisateur est fusionné avec le profil d'un autre utilisateur et que le profil d'origine devient orphelin
[SNAPSHOTS_APP_SHARED](#SNAPSHOTS_APP_SHARED) | Instantanés d'application (**Snowflake Data Sharing uniquement**)
[SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED](#SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED) | Instantanés de variantes de messages de Campaign (**Snowflake Data Sharing uniquement**)
[SNAPSHOTS_CANVAS_FLOW_STEP_SHARED](#SNAPSHOTS_CANVAS_FLOW_STEP_SHARED) | Instantanés d'étapes Canvas Flow (**Snowflake Data Sharing uniquement**)
[SNAPSHOTS_CANVAS_STEP_SHARED](#SNAPSHOTS_CANVAS_STEP_SHARED) | Instantanés d'étapes Canvas (**Snowflake Data Sharing uniquement**)
[SNAPSHOTS_CANVAS_VARIATION_SHARED](#SNAPSHOTS_CANVAS_VARIATION_SHARED) | Instantanés de variantes Canvas (**Snowflake Data Sharing uniquement**)
[SNAPSHOTS_EXPERIMENT_STEP_SHARED](#SNAPSHOTS_EXPERIMENT_STEP_SHARED) | Instantanés d'étapes d'expérience (**Snowflake Data Sharing uniquement**)

## Console des agents {#agent-console}

{% alert note %}
Les tables de la Console des agents sont disponibles uniquement dans le partage de données Snowflake.
{% endalert %}

### AGENTCONSOLE_AGENTEXECUTED_SHARED {#AGENTCONSOLE_AGENTEXECUTED_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global pour cet événement
`invocation_id` | `string` | ID unique global pour ce message
`request_id` | `string` | ID unique pour cette requête LLM globale et l'exécution complète
`duration` | `int` | Durée de la session en secondes
`prompt_tokens` | `int` | Nombre de jetons de prompt utilisés par cette requête
`completion_tokens` | `int` | Nombre de jetons de complétion utilisés par cette requête
`total_tokens` | `int` | Nombre total de jetons utilisés par cette requête
`cache_tokens` | `int` | Nombre de jetons mis en cache utilisés par cette requête
`reasoning_tokens` | `int` | Nombre de jetons de raisonnement utilisés par cette requête
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_group_id` | `string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`agent_id` | `string` | ID BSON du CustomerDefinedAgent
`agent_name` | `string` | Nom du CustomerDefinedAgent
`model_provider` | `string` | Nom du fournisseur du modèle LLM
`model_name` | `string` | Nom du modèle LLM utilisé dans cette requête
`provider_request_id` | `string` | Tout ID de requête fourni par le fournisseur du modèle pour l'appel API
`cache_hit` | `boolean` | Indique si cette requête a utilisé le cache pour renvoyer la réponse
`llm_owned_by_customer` | `boolean` | Si vrai, la clé API du client a été utilisée ; si faux, la clé de Braze a été utilisée
`is_error` | `boolean` | Indique si cette requête a généré une erreur
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`user_id` | `string` | [PII] ID utilisateur Braze de l'utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`input` | `null,`&nbsp;`string` | [PII] Entrée envoyée au LLM
`output` | `null,`&nbsp;`string` | [PII] Réponse du LLM
`invocation_source` | `null,`&nbsp;`string` | Quel objet Ruby a invoqué la requête LLM
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="AGENTCONSOLEAGENTEXECUTEDSHARED #AGENTCONSOLEAGENTEXECUTEDSHARED" }

### AGENTCONSOLE_RAWLLMREQUEST_SHARED {#AGENTCONSOLE_RAWLLMREQUEST_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global pour cet événement
`invocation_id` | `string` | ID unique global pour ce message
`request_id` | `string` | ID unique pour cette requête LLM globale et l'exécution complète
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_group_id` | `string` | ID BSON du groupe d'applications auquel cet événement appartient
`agent_id` | `string` | ID BSON du CustomerDefinedAgent
`agent_name` | `string` | Nom du CustomerDefinedAgent
`model_provider` | `string` | Nom du fournisseur du modèle LLM
`model_name` | `string` | Nom du modèle LLM utilisé dans cette requête
`duration` | `int`,&nbsp;`null` | Durée de la session en secondes
`request` | `string` | [PII] Prompt utilisé dans la requête
`http_status_code` | `int`,&nbsp;`null` | Code de statut HTTP de la réponse
`response_body` | `string`,&nbsp;`null` | [PII] Réponse du LLM
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="AGENTCONSOLERAWLLMREQUESTSHARED #AGENTCONSOLERAWLLMREQUESTSHARED" }

### AGENTCONSOLE_TOOLINVOCATION_SHARED {#AGENTCONSOLE_TOOLINVOCATION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global pour cet événement
`tool_call_id` | `string` | ID unique global pour cet appel d'outil
`duration` | `int` | Durée de la session en secondes
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_group_id` | `string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`agent_id` | `string` | ID BSON du CustomerDefinedAgent
`agent_name` | `string` | Nom du CustomerDefinedAgent
`is_error` | `boolean` | Indique si cette requête a généré une erreur
`tool_name` | `string` | Nom de l'outil
`tool_arguments` | `null,`&nbsp;`string` | [PII] JSON des arguments de l'outil
`invocation_source` | `null,`&nbsp;`string` | Quel objet Ruby a invoqué la requête LLM
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="AGENTCONSOLETOOLINVOCATIONSHARED #AGENTCONSOLETOOLINVOCATIONSHARED" }

## Vues des attributs de profil utilisateur {#user-profile-attribute-views}

### USER_CUSTOM_ATTRIBUTES_VIEW_SHARED {#USER_CUSTOM_ATTRIBUTES_VIEW_SHARED}

Champ | Type | Description
------|------|------------
`app_group_id` | `string` | ID BSON de l'espace de travail
`app_id` | `string` | ID BSON de l'application
`user_id` | `string` | [PII] ID utilisateur Braze
`time` | `int` | Horodatage UNIX en secondes de la mise à jour du profil (pour les lignes rétro-remplies, l'heure du rétro-remplissage)
`time_ms` | `int` | Horodatage UNIX en millisecondes de la mise à jour du profil (pour les lignes rétro-remplies, l'heure du rétro-remplissage)
`update_source` | `string` | Source de la mise à jour du profil
`sf_updated_at` | `timestamp` | Date à laquelle cette ligne a été mise à jour dans Snowflake
`custom_attributes` | `variant` | [PII] Attributs personnalisés sous forme d'objet JSON
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERCUSTOMATTRIBUTESVIEWSHARED #USERCUSTOMATTRIBUTESVIEWSHARED" }

### USER_DEFAULT_ATTRIBUTES_VIEW_SHARED {#USER_DEFAULT_ATTRIBUTES_VIEW_SHARED}

Champ | Type | Description
------|------|------------
`app_group_id` | `string` | ID BSON de l'espace de travail
`app_id` | `string` | ID BSON de l'application
`user_id` | `string` | [PII] ID utilisateur Braze
`time` | `int` | Horodatage UNIX en secondes de la mise à jour du profil (pour les lignes rétro-remplies, l'heure du rétro-remplissage)
`time_ms` | `int` | Horodatage UNIX en millisecondes de la mise à jour du profil (pour les lignes rétro-remplies, l'heure du rétro-remplissage)
`update_source` | `string` | Source de la mise à jour du profil
`sf_updated_at` | `timestamp` | Date à laquelle cette ligne a été mise à jour dans Snowflake
`external_user_id` | `string` | [PII] ID externe de l'utilisateur
`first_name` | `string` | [PII] Prénom
`last_name` | `string` | [PII] Nom de famille
`email_address` | `string` | [PII] Adresse e-mail
`gender` | `string` | [PII] Genre
`phone_number` | `string` | [PII] Numéro de téléphone
`dob` | `string` | [PII] Date de naissance
`TIME_ZONE` | `string` | [PII] Fuseau horaire
`home_city` | `string` | [PII] Ville de résidence
`country` | `string` | [PII] Pays
`language` | `string` | [PII] Langue
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESVIEWSHARED #USERDEFAULTATTRIBUTESVIEWSHARED" }

### USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED {#USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED}

Champ | Type | Description
------|------|------------
`app_group_id` | `string` | ID BSON de l'espace de travail
`user_id` | `string` | [PII] ID utilisateur Braze
`app_id` | `string` | ID BSON de l'application
`time` | `int` | Horodatage UNIX en secondes de la mise à jour du profil (pour les lignes rétro-remplies, l'heure du rétro-remplissage)
`time_ms` | `int` | Horodatage UNIX en millisecondes de la mise à jour du profil (pour les lignes rétro-remplies, l'heure du rétro-remplissage)
`update_source` | `string` | Source de la mise à jour du profil
`sf_updated_at` | `timestamp` | Date à laquelle cette ligne a été mise à jour dans Snowflake
`external_user_id` | `string` | [PII] ID externe de l'utilisateur
`first_name` | `string` | [PII] Prénom
`last_name` | `string` | [PII] Nom de famille
`email_address` | `string` | [PII] Adresse e-mail
`gender` | `string` | [PII] Genre
`phone_number` | `string` | [PII] Numéro de téléphone
`dob` | `string` | [PII] Date de naissance
`TIME_ZONE` | `string` | [PII] Fuseau horaire
`home_city` | `string` | [PII] Ville de résidence
`country` | `string` | [PII] Pays
`language` | `string` | [PII] Langue
`eff_dt` | `timestamp` | Début de l'intervalle pendant lequel cet état d'attribut était en vigueur
`end_dt` | `timestamp` | Fin de cet intervalle
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESHISTORYVIEWSHARED #USERDEFAULTATTRIBUTESHISTORYVIEWSHARED" }

### USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED {#USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED}

Champ | Type | Description
------|------|------------
`app_group_id` | `string` | ID BSON de l'espace de travail
`app_id` | `string` | ID BSON de l'application
`user_id` | `string` | [PII] ID utilisateur Braze
`time` | `int` | Horodatage UNIX en secondes de la mise à jour du profil (pour les lignes rétro-remplies, l'heure du rétro-remplissage)
`time_ms` | `int` | Horodatage UNIX en millisecondes de la mise à jour du profil (pour les lignes rétro-remplies, l'heure du rétro-remplissage)
`update_source` | `string` | Source de la mise à jour du profil
`sf_updated_at` | `timestamp` | Date à laquelle cette ligne a été mise à jour dans Snowflake
`external_user_id` | `string` | [PII] ID externe de l'utilisateur
`first_name` | `string` | [PII] Prénom
`last_name` | `string` | [PII] Nom de famille
`email_address` | `string` | [PII] Adresse e-mail
`gender` | `string` | [PII] Genre
`phone_number` | `string` | [PII] Numéro de téléphone
`dob` | `string` | [PII] Date de naissance
`home_city` | `string` | [PII] Ville de résidence
`country` | `string` | [PII] Pays
`language` | `string` | [PII] Langue
`TIME_ZONE` | `string` | [PII] Fuseau horaire
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED #USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED" }

### USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED {#USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

{% multi_lang_include partners/snowflake_user_attributes_custom_view_schemas.md schema="history" %}

Pour des conseils d'utilisation et des exemples de requêtes, consultez [Attributs utilisateur Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes#historical-change-logs).

### USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED {#USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

{% multi_lang_include partners/snowflake_user_attributes_custom_view_schemas.md schema="latest" %}

Pour des conseils d'utilisation et des exemples de requêtes, consultez [Attributs utilisateur Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes#real-time-user-profile-views).

## Catalogues {#catalogs}

### CATALOGS_ITEMS_SHARED {#CATALOGS_ITEMS_SHARED}

Champ | Type | Description
------|------|------------
`catalog_id` | `string` | ID BSON du catalogue
`item_id` | `string` | ID BSON de l'élément du catalogue
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications
`field_name` | `null,`&nbsp;`string` | Nom du champ
`field_value` | `null,`&nbsp;`string` | Valeur du champ
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CATALOGSITEMSSHARED #CATALOGSITEMSSHARED" }

## Journaux des modifications {#changelogs}

### CHANGELOGS_GLOBALCONTROLGROUP_SHARED {#CHANGELOGS_GLOBALCONTROLGROUP_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`time` | `int` | Horodatage UNIX du moment où l'événement s'est produit
`random_bucket_number` | `null, int` | Nouveau numéro de compartiment aléatoire
`global_control_group` | `null, boolean` | Avec cette modification, le numéro de compartiment est inclus dans le groupe de contrôle global
`previous_global_control_group` | `null, boolean` | Avant cette modification, le numéro de compartiment était inclus dans le groupe de contrôle global, mais il ne l'est plus
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CHANGELOGSGLOBALCONTROLGROUPSHARED #CHANGELOGSGLOBALCONTROLGROUPSHARED" }

### CHANGELOGS_CAMPAIGN_SHARED {#CHANGELOGS_CAMPAIGN_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX du moment où l'événement s'est produit
`app_group_id` | `string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`api_id` | `string` | ID API de la Campaign
`name` | `null,`&nbsp;`string` | Nom de la Campaign
`conversion_behaviors` | `null,`&nbsp;`string` | Comportements de conversion pour la Campaign
`actions` | `null,`&nbsp;`string` | Actions pour la Campaign
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CHANGELOGSCAMPAIGNSHARED #CHANGELOGSCAMPAIGNSHARED" }

### CHANGELOGS_CANVAS_SHARED {#CHANGELOGS_CANVAS_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX du moment où l'événement s'est produit
`app_group_id` | `string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`api_id` | `string` | ID API du Canvas
`name` | `null,`&nbsp;`string` | Nom du Canvas
`conversion_behaviors` | `null,`&nbsp;`string` | Comportements de conversion pour le Canvas
`variations` | `null,`&nbsp;`string` | Variations pour le Canvas
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CHANGELOGSCANVASSHARED #CHANGELOGSCANVASSHARED" }

## Comportements {#behaviors}

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | Identifiant unique global de cet événement
`user_id` | `string` | Identifiant Braze de l'utilisateur ayant effectué l'événement
`external_user_id` | `null,`&nbsp;`string` | [PII] Identifiant utilisateur externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | Identifiant API de l'espace de travail auquel cet utilisateur appartient
`app_api_id` | `null,`&nbsp;`string` | Identifiant API de l'application sur laquelle cette action s'est produite
`time` | `int` | Horodatage Unix auquel l'utilisateur a effectué l'événement
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`device_id` | `null,`&nbsp;`string` | Identifiant de l'appareil sur lequel l'événement personnalisé s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`name` | `string` | Nom de l'événement personnalisé
`properties` | `string` | Propriétés personnalisées de l'événement stockées sous forme de chaîne de caractères JSON encodée
`ad_id` | `null,`&nbsp;`string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Indique si le suivi publicitaire est activé pour l'appareil
`app_group_id` | `null,`&nbsp;`string` | Identifiant BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSCUSTOMEVENTSHARED #USERSBEHAVIORSCUSTOMEVENTSHARED" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | Identifiant unique global de cet événement
`user_id` | `string` | Identifiant Braze de l'utilisateur ayant effectué l'installation
`external_user_id` | `null,`&nbsp;`string` | [PII] Identifiant utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | Identifiant API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix auquel l'utilisateur a effectué l'installation
`source` | `string` | Source de l'attribution
`app_group_id` | `null,`&nbsp;`string` | Identifiant BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSINSTALLATTRIBUTIONSHARED #USERSBEHAVIORSINSTALLATTRIBUTIONSHARED" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | Identifiant unique global de cet événement
`user_id` | `string` | Identifiant Braze de l'utilisateur ayant enregistré la localisation
`external_user_id` | `null,`&nbsp;`string` | [PII] Identifiant utilisateur externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | Identifiant API de l'espace de travail auquel cet utilisateur appartient
`app_api_id` | `null,`&nbsp;`string` | Identifiant API de l'application sur laquelle cette localisation a été enregistrée
`time` | `int` | Horodatage Unix auquel la localisation a été enregistrée
`latitude` | `float` | [PII] Latitude de la localisation enregistrée
`longitude` | `float` | [PII] Longitude de la localisation enregistrée
`altitude` | `null, float` | [PII] Altitude de la localisation enregistrée
`ll_accuracy` | `null, float` | Précision de la latitude et de la longitude de la localisation enregistrée
`alt_accuracy` | `null, float` | Précision de l'altitude de la localisation enregistrée
`device_id` | `null,`&nbsp;`string` | Identifiant de l'appareil sur lequel la localisation a été enregistrée
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'enregistrement de la localisation
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`ad_id` | `null,`&nbsp;`string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Indique si le suivi publicitaire est activé pour l'appareil
`app_group_id` | `null,`&nbsp;`string` | Identifiant BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSLOCATIONSHARED #USERSBEHAVIORSLOCATIONSHARED" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | Identifiant unique global de cet événement
`user_id` | `string` | Identifiant Braze de l'utilisateur ayant effectué un achat
`external_user_id` | `null,`&nbsp;`string` | [PII] Identifiant utilisateur externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | Identifiant API de l'espace de travail auquel cet utilisateur appartient
`app_api_id` | `null,`&nbsp;`string` | Identifiant API de l'application sur laquelle l'achat a été effectué
`time` | `int` | Horodatage Unix auquel l'utilisateur a effectué l'achat
`device_id` | `null,`&nbsp;`string` | Identifiant de l'appareil sur lequel l'achat a été effectué
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'achat
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`product_id` | `string` | Identifiant du produit acheté
`price` | `float` | Prix de l'achat
`currency` | `string` | Devise de l'achat
`properties` | `string` | Propriétés personnalisées de l'achat stockées sous forme de chaîne de caractères JSON encodée
`ad_id` | `null,`&nbsp;`string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Indique si le suivi publicitaire est activé pour l'appareil
`app_group_id` | `null,`&nbsp;`string` | Identifiant BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSPURCHASESHARED #USERSBEHAVIORSPURCHASESHARED" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | Identifiant unique global de cet événement
`user_id` | `string` | Identifiant Braze de l'utilisateur ayant désinstallé l'application
`external_user_id` | `null,`&nbsp;`string` | [PII] Identifiant utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | Identifiant API de l'espace de travail auquel cet utilisateur appartient
`app_api_id` | `null,`&nbsp;`string` | Identifiant API de l'application qui a été désinstallée
`time` | `int` | Horodatage Unix auquel l'utilisateur a désinstallé l'application
`app_group_id` | `null,`&nbsp;`string` | Identifiant BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSUNINSTALLSHARED #USERSBEHAVIORSUNINSTALLSHARED" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | Identifiant unique global de cet événement
`user_id` | `string` | Identifiant Braze de l'utilisateur ayant mis à jour l'application
`external_user_id` | `null,`&nbsp;`string` | [PII] Identifiant utilisateur externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | Identifiant API de l'espace de travail auquel cet utilisateur appartient
`app_api_id` | `null,`&nbsp;`string` | Identifiant API de l'application que l'utilisateur a mise à jour
`time` | `int` | Horodatage Unix auquel l'utilisateur a mis à jour l'application
`device_id` | `null,`&nbsp;`string` | Identifiant de l'appareil sur lequel l'utilisateur a mis à jour l'application
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`old_app_version` | `null,`&nbsp;`string` | Ancienne version de l'application
`new_app_version` | `null,`&nbsp;`string` | Nouvelle version de l'application
`app_group_id` | `null,`&nbsp;`string` | Identifiant BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSUPGRADEDAPPSHARED #USERSBEHAVIORSUPGRADEDAPPSHARED" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | Identifiant unique global de cet événement
`user_id` | `string` | Identifiant Braze de l'utilisateur ayant effectué cette action
`external_user_id` | `null,`&nbsp;`string` | [PII] Identifiant utilisateur externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | Identifiant API de l'espace de travail auquel cet utilisateur appartient
`app_api_id` | `null,`&nbsp;`string` | Identifiant API de l'application sur laquelle cette session s'est produite
`time` | `int` | Horodatage Unix auquel la session a commencé
`session_id` | `string` | UUID de la session
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`device_id` | `null,`&nbsp;`string` | Identifiant de l'appareil sur lequel la session s'est produite
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée pendant la session
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`app_group_id` | `null,`&nbsp;`string` | Identifiant BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPFIRSTSESSIONSHARED #USERSBEHAVIORSAPPFIRSTSESSIONSHARED" }


### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | Identifiant unique global de cet événement
`user_id` | `string` | Identifiant Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] Identifiant externe de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | Identifiant BSON du groupe d'applications auquel cet utilisateur appartient
`app_group_api_id` | `null,`&nbsp;`string` | Identifiant API du groupe d'applications auquel cet utilisateur appartient
`app_api_id` | `null,`&nbsp;`string` | Identifiant API de l'application sur laquelle cet événement s'est produit
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`device_id` | `null,`&nbsp;`string` | Identifiant de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPNEWSFEEDIMPRESSIONSHARED #USERSBEHAVIORSAPPNEWSFEEDIMPRESSIONSHARED" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | Identifiant unique global de cet événement
`user_id` | `string` | Identifiant Braze de l'utilisateur ayant effectué cette action
`external_user_id` | `null,`&nbsp;`string` | [PII] Identifiant utilisateur externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | Identifiant API de l'espace de travail auquel cet utilisateur appartient
`app_api_id` | `null,`&nbsp;`string` | Identifiant API de l'application sur laquelle cette session s'est produite
`time` | `int` | Horodatage Unix auquel la session s'est terminée
`duration` | `null, float` | Durée de la session en secondes
`session_id` | `string` | UUID de la session
`device_id` | `null,`&nbsp;`string` | Identifiant de l'appareil sur lequel la session s'est produite
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée pendant la session
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`app_group_id` | `null,`&nbsp;`string` | Identifiant BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPSESSIONENDSHARED #USERSBEHAVIORSAPPSESSIONENDSHARED" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | Identifiant unique global de cet événement
`user_id` | `string` | Identifiant Braze de l'utilisateur ayant effectué cette action
`external_user_id` | `null,`&nbsp;`string` | [PII] Identifiant utilisateur externe de l'utilisateur
`app_api_id` | `null,`&nbsp;`string` | Identifiant API de l'application sur laquelle cette session s'est produite
`app_group_api_id` | `null,`&nbsp;`string` | Identifiant API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix auquel la session a commencé
`session_id` | `string` | UUID de la session
`device_id` | `null,`&nbsp;`string` | Identifiant de l'appareil sur lequel la session s'est produite
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée pendant la session
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`app_group_id` | `null,`&nbsp;`string` | Identifiant BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPSESSIONSTARTSHARED #USERSBEHAVIORSAPPSESSIONSTARTSHARED" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | Identifiant unique global de cet événement
`user_id` | `string` | Identifiant Braze de l'utilisateur ayant effectué l'événement
`external_user_id` | `null,`&nbsp;`string` | [PII] Identifiant utilisateur externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | Identifiant API de l'espace de travail auquel cet utilisateur appartient
`app_api_id` | `null,`&nbsp;`string` | Identifiant API de l'application sur laquelle cette action s'est produite
`time` | `int` | Horodatage Unix auquel l'utilisateur a effectué l'événement
`device_id` | `null,`&nbsp;`string` | Identifiant de l'appareil sur lequel l'événement personnalisé s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`event_type` | `string` | Type d'événement de géorepérage déclenché (par exemple, « enter » ou « exit »)
`location_set_id` | `string` | Identifiant de l'ensemble de localisations du géorepérage déclenché
`geofence_id` | `string` | Identifiant du géorepérage déclenché
`app_group_id` | `null,`&nbsp;`string` | Identifiant BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSGEOFENCEDATAEVENTSHARED #USERSBEHAVIORSGEOFENCEDATAEVENTSHARED" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | Identifiant unique global de cet événement
`user_id` | `string` | Identifiant Braze de l'utilisateur ayant effectué l'événement
`external_user_id` | `null,`&nbsp;`string` | [PII] Identifiant utilisateur externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | Identifiant API de l'espace de travail auquel cet utilisateur appartient
`app_api_id` | `null,`&nbsp;`string` | Identifiant API de l'application sur laquelle cette action s'est produite
`time` | `int` | Horodatage Unix auquel l'utilisateur a effectué l'événement
`device_id` | `null,`&nbsp;`string` | Identifiant de l'appareil sur lequel l'événement personnalisé s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`event_type` | `string` | Type d'événement de géorepérage déclenché (par exemple, « enter » ou « exit »)
`location_set_id` | `string` | Identifiant de l'ensemble de localisations du géorepérage déclenché
`geofence_id` | `string` | Identifiant du géorepérage déclenché
`app_group_id` | `null,`&nbsp;`string` | Identifiant BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSGEOFENCERECORDEVENTSHARED #USERSBEHAVIORSGEOFENCERECORDEVENTSHARED" }


### USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | Identifiant unique global de cet événement
`user_id` | `string` | Identifiant Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] Identifiant externe de l'utilisateur
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_group_id` | `null,`&nbsp;`string` | Identifiant BSON du groupe d'applications auquel cet utilisateur appartient
`activity_attributes_type` | `null,`&nbsp;`string` | Type d'attribut de l'activité en direct or en ligne/en production/instantané
`push_to_start_token` | `null,`&nbsp;`string` | Jeton push-to-start de l'activité en direct or en ligne/en production/instantané
`device_id` | `null,`&nbsp;`string` | Identifiant de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`ios_push_token_apns_gateway` | `null, int` | Passerelle APNS du jeton push ; s'applique uniquement aux jetons push iOS : 1 pour le développement, 2 pour la production
`push_token_state_change_type` | `null,`&nbsp;`string` | Description du type de changement d'état du jeton push
`app_group_api_id` | `null,`&nbsp;`string` | Identifiant API du groupe d'applications auquel cet utilisateur appartient
`app_api_id` | `null,`&nbsp;`string` | Identifiant API de l'application sur laquelle cet événement s'est produit
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSLIVEACTIVITYPUSHTOSTARTTOKENCHANGESHARED #USERSBEHAVIORSLIVEACTIVITYPUSHTOSTARTTOKENCHANGESHARED" }


### USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | Identifiant unique global de cet événement
`user_id` | `string` | Identifiant Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] Identifiant externe de l'utilisateur
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_group_id` | `null,`&nbsp;`string` | Identifiant BSON du groupe d'applications auquel cet utilisateur appartient
`activity_id` | `null,`&nbsp;`string` | Identifiant de l'activité en direct or en ligne/en production/instantané
`update_token` | `null,`&nbsp;`string` | Jeton de mise à jour de l'activité en direct or en ligne/en production/instantané
`device_id` | `null,`&nbsp;`string` | Identifiant de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`ios_push_token_apns_gateway` | `null, int` | Passerelle APNS du jeton push ; s'applique uniquement aux jetons push iOS : 1 pour le développement, 2 pour la production
`push_token_state_change_type` | `null,`&nbsp;`string` | Description du type de changement d'état du jeton push
`app_group_api_id` | `null,`&nbsp;`string` | Identifiant API du groupe d'applications auquel cet utilisateur appartient
`app_api_id` | `null,`&nbsp;`string` | Identifiant API de l'application sur laquelle cet événement s'est produit
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSLIVEACTIVITYUPDATETOKENCHANGESHARED #USERSBEHAVIORSLIVEACTIVITYUPDATETOKENCHANGESHARED" }


### USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED {#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | Identifiant unique global de cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`time_ms` | `int` | Temps en millisecondes auquel l'événement s'est produit
`user_id` | `string` | Identifiant Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] Identifiant externe de l'utilisateur
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`app_group_id` | `null,`&nbsp;`string` | Identifiant BSON du groupe d'applications auquel cet utilisateur appartient
`push_token` | `null,`&nbsp;`string` | Jeton push de l'événement
`push_token_created_at` | `null, int` | Horodatage UNIX auquel le jeton push a été créé
`push_token_updated_at` | `null, int` | Horodatage UNIX de la dernière mise à jour du jeton push
`push_token_foreground_push_disabled` | `null, boolean` | Indicateur de désactivation du push au premier plan pour le jeton push
`push_token_device_id` | `null,`&nbsp;`string` | Identifiant de l'appareil associé au jeton push
`push_token_provisionally_opted_in` | `null, boolean` | Indicateur d'abonnement provisoire du jeton push
`ios_push_token_apns_gateway` | `null, int` | Passerelle APNS du jeton push ; s'applique uniquement aux jetons push iOS : 1 pour le développement, 2 pour la production
`web_push_token_public_key` | `null,`&nbsp;`string` | Clé publique du jeton push ; s'applique uniquement aux jetons push Web
`web_push_token_user_auth` | `null,`&nbsp;`string` | Authentification utilisateur du jeton push ; s'applique uniquement aux jetons push Web
`web_push_token_vapid_public_key` | `null,`&nbsp;`string` | Clé publique VAPID du jeton push ; s'applique uniquement aux jetons push Web
`push_token_state_change_type` | `null,`&nbsp;`string` | Description du type de changement d'état du jeton push
`app_group_api_id` | `null,`&nbsp;`string` | Identifiant API du groupe d'applications auquel cet utilisateur appartient
`app_api_id` | `null,`&nbsp;`string` | Identifiant API de l'application sur laquelle cet événement s'est produit
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSPUSHNOTIFICATIONTOKENSTATECHANGESHARED #USERSBEHAVIORSPUSHNOTIFICATIONTOKENSTATECHANGESHARED" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | Identifiant unique global de cet événement
`user_id` | `string` | Identifiant Braze de l'utilisateur concerné
`external_user_id` | `null,`&nbsp;`string` | [PII] Identifiant utilisateur externe de l'utilisateur
`email_address` | `null,`&nbsp;`string` | [PII] Adresse e-mail de l'utilisateur
`state_change_source` | `null,`&nbsp;`string` | Source du changement d'état (REST, SDK, tableau de bord, etc.)
`subscription_status` | `string` | Statut d'abonnement : « Subscribed », « Unsubscribed » ou « Opted In »
`channel` | `null,`&nbsp;`string` | Canal de l'état d'abonnement global, par exemple e-mail
`time` | `int` | Horodatage Unix auquel l'état d'abonnement a changé
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | Identifiant API de l'espace de travail auquel cet utilisateur appartient
`app_api_id` | `null,`&nbsp;`string` | Identifiant API de l'application à laquelle l'événement appartient
`campaign_id` | `null,`&nbsp;`string` | Identifiant Braze interne de la Campaign à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | Identifiant API de la Campaign à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | Identifiant API de la variante de message à laquelle cet événement appartient
`canvas_id` | `null,`&nbsp;`string` | Identifiant Braze interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | Identifiant API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | Identifiant API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | Identifiant API de l'étape Canvas à laquelle cet événement appartient
`send_id` | `null,`&nbsp;`string` | Identifiant d'envoi du message à l'origine de ce changement d'état d'abonnement
`app_group_id` | `null,`&nbsp;`string` | Identifiant BSON du groupe d'applications auquel cet utilisateur appartient
`channel_identifier` | `null,`&nbsp;`string` | [PII] Identifiant de l'utilisateur sur le canal concerné par l'événement
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSSUBSCRIPTIONGLOBALSTATECHANGESHARED #USERSBEHAVIORSSUBSCRIPTIONGLOBALSTATECHANGESHARED" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | Identifiant unique global de cet événement
`user_id` | `string` | Identifiant Braze de l'utilisateur concerné
`external_user_id` | `null,`&nbsp;`string` | [PII] Identifiant utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | Identifiant API de l'espace de travail auquel cet utilisateur appartient
`email_address` | `null,`&nbsp;`string` | [PII] Adresse e-mail de l'utilisateur
`phone_number` | `null,`&nbsp;`string` | [PII] Numéro de téléphone de l'utilisateur au format e164
`app_api_id` | `null,`&nbsp;`string` | Identifiant API de l'application à laquelle l'événement appartient
`campaign_id` | `null,`&nbsp;`string` | Identifiant Braze interne de la Campaign à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | Identifiant API de la Campaign à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | Identifiant API de la variante de message à laquelle cet événement appartient
`canvas_id` | `null,`&nbsp;`string` | Identifiant Braze interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | Identifiant API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | Identifiant API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | Identifiant API de l'étape Canvas à laquelle cet événement appartient
`subscription_group_api_id` | `string` | Identifiant API du groupe d'abonnement
`channel` | `null,`&nbsp;`string` | Canal : « email » ou « sms », selon le type de canal du groupe d'abonnement
`subscription_status` | `string` | Statut d'abonnement : « Subscribed », « Unsubscribed » ou « Opted In »
`time` | `int` | Horodatage Unix auquel l'état d'abonnement a changé
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`send_id` | `null,`&nbsp;`string` | Identifiant d'envoi du message à l'origine de ce changement d'état d'abonnement
`state_change_source` | `null,`&nbsp;`string` | Source du changement d'état (REST, SDK, tableau de bord, etc.)
`app_group_id` | `null,`&nbsp;`string` | Identifiant BSON du groupe d'applications auquel cet utilisateur appartient
`dispatch_id` | `null,`&nbsp;`string` | Identifiant de distribution auquel ce message appartient
`channel_identifier` | `null,`&nbsp;`string` | [PII] Identifiant de l'utilisateur sur le canal concerné par l'événement
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSSUBSCRIPTIONGROUPSTATECHANGESHARED #USERSBEHAVIORSSUBSCRIPTIONGROUPSTATECHANGESHARED" }

## Campaigns {#campaigns}

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`conversion_behavior_index` | `null, int` | Index du comportement de conversion
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date et heure de récupération de cet événement par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSCONVERSIONSHARED #USERSCAMPAIGNSCONVERSIONSHARED" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date et heure de récupération de cet événement par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSENROLLINCONTROLSHARED #USERSCAMPAIGNSENROLLINCONTROLSHARED" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`channel` | `null,`&nbsp;`string` | Canal auquel cet événement appartient
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date et heure de récupération de cet événement par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSFREQUENCYCAPSHARED #USERSCAMPAIGNSFREQUENCYCAPSHARED" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`revenue` | `long` | Montant du chiffre d'affaires en centimes USD généré
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date et heure de récupération de cet événement par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSREVENUESHARED #USERSCAMPAIGNSREVENUESHARED" }

## Canvas {#canvas}

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| Champ                                  | Type                     | Description                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | ID globalement unique pour cet événement                                                                        |
| `user_id`                              | `string`,&nbsp;`null`    | ID Braze de l'utilisateur qui a effectué cet événement                                                          |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ID externe de l'utilisateur                                                                               |
| `device_id`                            | `string`,&nbsp;`null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme                                            |
| `app_group_id`                         | `string`,&nbsp;`null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                                               |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | ID API de l'espace de travail auquel cet utilisateur appartient                                                 |
| `time`                                 | `int`,&nbsp;`null`       | Horodatage Unix auquel l'événement s'est produit                                                                |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Pour usage interne Braze uniquement) ID du Canvas auquel appartient cet événement                              |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | ID API du Canvas auquel appartient cet événement                                                                |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | ID API de la variante Canvas à laquelle appartient cet événement                                                |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | ID API de l'étape Canvas à laquelle appartient cet événement                                                    |
| `progression_type`                     | `string`,&nbsp;`null`    | Type d'événement de progression d'étape                                                                         |
| `is_canvas_entry`                      | `boolean`,&nbsp;`null`   | Indique s'il s'agit d'une entrée dans une première étape d'un Canvas                                            |
| `exit_reason`                          | `string`,&nbsp;`null`    | S'il s'agit d'une sortie, la raison pour laquelle l'utilisateur a quitté le Canvas au cours de cette étape      |
| `canvas_entry_id`                      | `string`,&nbsp;`null`    | Identifiant unique de cette instance d'un utilisateur dans un Canvas                                            |
| `next_step_id`                         | `string`,&nbsp;`null`    | ID BSON de l'étape suivante dans le Canvas                                                                      |
| `next_step_api_id`                     | `string`,&nbsp;`null`    | ID API de l'étape suivante dans le Canvas                                                                       |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASSTEPPROGRESSIONSHARED #USERSCANVASSTEPPROGRESSIONSHARED" }

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| Champ                                  | Type                     | Description                                                                                                                              |
| -------------------------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | ID globalement unique pour cet événement                                                                                                 |
| `user_id`                              | `string`,&nbsp;`null`    | ID Braze de l'utilisateur qui a effectué cet événement                                                                                   |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ID externe de l'utilisateur                                                                                                        |
| `device_id`                            | `string`,&nbsp;`null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme                                                                     |
| `app_group_id`                         | `string`,&nbsp;`null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                                                                        |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | ID API de l'espace de travail auquel cet utilisateur appartient                                                                          |
| `time`                                 | `int`,&nbsp;`null`       | Horodatage Unix auquel l'événement s'est produit                                                                                         |
| `app_api_id`                           | `string`,&nbsp;`null`    | ID API de l'application sur laquelle cet événement s'est produit                                                                         |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Pour usage interne Braze uniquement) ID du Canvas auquel appartient cet événement                                                       |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | ID API du Canvas auquel appartient cet événement                                                                                         |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | ID API de la variante Canvas à laquelle appartient cet événement                                                                         |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | ID API de l'étape Canvas à laquelle appartient cet événement                                                                             |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | ID API de la variante de message de l'étape Canvas que cet utilisateur a reçue                                                           |
| `conversion_behavior_index`            | `int`,&nbsp;`null`       | Type d'événement de conversion effectué par l'utilisateur, où « 0 » est une conversion principale et « 1 » une conversion secondaire    |
| `gender`                               | `string`,&nbsp;`null`    | [PII] Genre de l'utilisateur                                                                                                             |
| `country`                              | `string`,&nbsp;`null`    | [PII] Pays de l'utilisateur                                                                                                              |
| `timezone`                             | `string`,&nbsp;`null`    | Fuseau horaire de l'utilisateur                                                                                                          |
| `language`                             | `string`,&nbsp;`null`    | [PII] Langue de l'utilisateur                                                                                                            |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe                                                                                |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASCONVERSIONSHARED #USERSCANVASCONVERSIONSHARED" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| Champ                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | ID globalement unique pour cet événement                             |
| `user_id`                 | `string`,&nbsp;`null`    | ID Braze de l'utilisateur qui a effectué cet événement               |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ID externe de l'utilisateur                                    |
| `device_id`               | `string`,&nbsp;`null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme |
| `app_group_id`            | `string`,&nbsp;`null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient    |
| `app_group_api_id`        | `string`,&nbsp;`null`    | ID API de l'espace de travail auquel cet utilisateur appartient      |
| `time`                    | `int`,&nbsp;`null`       | Horodatage Unix auquel l'événement s'est produit                     |
| `canvas_id`               | `string`,&nbsp;`null`    | (Pour usage interne Braze uniquement) ID du Canvas auquel appartient cet événement |
| `canvas_api_id`           | `string`,&nbsp;`null`    | ID API du Canvas auquel appartient cet événement                     |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | ID API de la variante Canvas à laquelle appartient cet événement     |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | [Obsolète] ID API de l'étape Canvas à laquelle appartient cet événement |
| `gender`                  | `string`,&nbsp;`null`    | [PII] Genre de l'utilisateur                                         |
| `country`                 | `string`,&nbsp;`null`    | [PII] Pays de l'utilisateur                                          |
| `timezone`                | `string`,&nbsp;`null`    | Fuseau horaire de l'utilisateur                                       |
| `language`                | `string`,&nbsp;`null`    | [PII] Langue de l'utilisateur                                        |
| `in_control_group`        | `boolean`,&nbsp;`null`   | Vrai si l'utilisateur a été inscrit dans le groupe de contrôle       |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASENTRYSHARED #USERSCANVASENTRYSHARED" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| Champ                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | ID globalement unique pour cet événement                             |
| `user_id`                 | `string`,&nbsp;`null`    | ID Braze de l'utilisateur qui a effectué cet événement               |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ID externe de l'utilisateur                                    |
| `app_group_id`            | `string`,&nbsp;`null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient    |
| `app_group_api_id`        | `string`,&nbsp;`null`    | ID API de l'espace de travail auquel cet utilisateur appartient      |
| `time`                    | `int`,&nbsp;`null`       | Horodatage Unix auquel l'événement s'est produit                     |
| `canvas_id`               | `string`,&nbsp;`null`    | (Pour usage interne Braze uniquement) ID du Canvas auquel appartient cet événement |
| `canvas_api_id`           | `string`,&nbsp;`null`    | ID API du Canvas auquel appartient cet événement                     |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | ID API de la variante Canvas à laquelle appartient cet événement     |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | ID API de l'étape Canvas à laquelle appartient cet événement         |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXITMATCHEDAUDIENCESHARED" }

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXITMATCHEDAUDIENCESHARED #USERSCANVASEXITMATCHEDAUDIENCESHARED" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| Champ                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | ID globalement unique pour cet événement                             |
| `user_id`                 | `string`,&nbsp;`null`    | ID Braze de l'utilisateur qui a effectué cet événement               |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ID externe de l'utilisateur                                    |
| `app_group_id`            | `string`,&nbsp;`null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient    |
| `app_group_api_id`        | `string`,&nbsp;`null`    | ID API de l'espace de travail auquel cet utilisateur appartient      |
| `time`                    | `int`,&nbsp;`null`       | Horodatage Unix auquel l'événement s'est produit                     |
| `canvas_id`               | `string`,&nbsp;`null`    | (Pour usage interne Braze uniquement) ID du Canvas auquel appartient cet événement |
| `canvas_api_id`           | `string`,&nbsp;`null`    | ID API du Canvas auquel appartient cet événement                     |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | ID API de la variante Canvas à laquelle appartient cet événement     |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | ID API de l'étape Canvas à laquelle appartient cet événement         |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXITPERFORMEDEVENTSHARED #USERSCANVASEXITPERFORMEDEVENTSHARED" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| Champ                       | Type                     | Description                                                                                                                           |
| --------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | ID globalement unique pour cet événement                                                                                              |
| `user_id`                   | `string`,&nbsp;`null`    | ID Braze de l'utilisateur qui a effectué cet événement                                                                                |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] ID externe de l'utilisateur                                                                                                     |
| `app_group_id`              | `string`,&nbsp;`null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                                                                     |
| `time`                      | `int`,&nbsp;`null`       | Horodatage Unix auquel l'événement s'est produit                                                                                      |
| `app_api_id`                | `string`,&nbsp;`null`    | ID API de l'application sur laquelle cet événement s'est produit                                                                      |
| `canvas_id`                 | `string`,&nbsp;`null`    | (Pour usage interne Braze uniquement) ID du Canvas auquel appartient cet événement                                                    |
| `canvas_api_id`             | `string`,&nbsp;`null`    | ID API du Canvas auquel appartient cet événement                                                                                      |
| `canvas_variation_api_id`   | `string`,&nbsp;`null`    | ID API de la variante Canvas à laquelle appartient cet événement                                                                      |
| `canvas_step_api_id`        | `string`,&nbsp;`null`    | ID API de l'étape Canvas à laquelle appartient cet événement                                                                          |
| `experiment_step_api_id`    | `string`,&nbsp;`null`    | ID API de l'étape d'expérience à laquelle appartient cet événement                                                                    |
| `conversion_behavior_index` | `int`,&nbsp;`null`       | Type d'événement de conversion effectué par l'utilisateur, où « 0 » est une conversion principale et « 1 » une conversion secondaire |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe                                                                             |
| `experiment_split_api_id` | `string`,&nbsp;`null` | ID API de la branche d'expérience dans laquelle l'utilisateur a été inscrit |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXPERIMENTSTEPCONVERSIONSHARED #USERSCANVASEXPERIMENTSTEPCONVERSIONSHARED" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| Champ                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | ID globalement unique pour cet événement                             |
| `user_id`                 | `string`,&nbsp;`null`    | ID Braze de l'utilisateur qui a effectué cet événement               |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ID externe de l'utilisateur                                    |
| `app_group_id`            | `string`,&nbsp;`null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient    |
| `time`                    | `int`,&nbsp;`null`       | Horodatage Unix auquel l'événement s'est produit                     |
| `canvas_id`               | `string`,&nbsp;`null`    | (Pour usage interne Braze uniquement) ID du Canvas auquel appartient cet événement |
| `canvas_api_id`           | `string`,&nbsp;`null`    | ID API du Canvas auquel appartient cet événement                     |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | ID API de la variante Canvas à laquelle appartient cet événement     |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | ID API de l'étape Canvas à laquelle appartient cet événement         |
| `experiment_step_api_id`  | `string`,&nbsp;`null`    | ID API de l'étape d'expérience à laquelle appartient cet événement   |
| `in_control_group`        | `boolean`,&nbsp;`null`   | Vrai si l'utilisateur a été inscrit dans le groupe de contrôle       |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXPERIMENTSTEPSPLITENTRYSHARED" }

| `experiment_split_api_id` | `string`,&nbsp;`null` | ID API de la branche d'expérience dans laquelle l'utilisateur a été inscrit |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXPERIMENTSTEPSPLITENTRYSHARED #USERSCANVASEXPERIMENTSTEPSPLITENTRYSHARED" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| Champ                                  | Type                     | Description                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | ID globalement unique pour cet événement                             |
| `user_id`                              | `string`,&nbsp;`null`    | ID Braze de l'utilisateur qui a effectué cet événement               |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ID externe de l'utilisateur                                    |
| `device_id`                            | `string`,&nbsp;`null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme |
| `app_group_id`                         | `string`,&nbsp;`null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient    |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | ID API de l'espace de travail auquel cet utilisateur appartient      |
| `time`                                 | `int`,&nbsp;`null`       | Horodatage Unix auquel l'événement s'est produit                     |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Pour usage interne Braze uniquement) ID du Canvas auquel appartient cet événement |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | ID API du Canvas auquel appartient cet événement                     |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | ID API de la variante Canvas à laquelle appartient cet événement     |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | ID API de l'étape Canvas à laquelle appartient cet événement         |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | ID API de la variante de message de l'étape Canvas que cet utilisateur a reçue |
| `channel`                              | `string`,&nbsp;`null`    | Canal de communication auquel appartient cet événement (e-mail, notification push, etc.) |
| `gender`                               | `string`,&nbsp;`null`    | [PII] Genre de l'utilisateur                                         |
| `country`                              | `string`,&nbsp;`null`    | [PII] Pays de l'utilisateur                                          |
| `timezone`                             | `string`,&nbsp;`null`    | Fuseau horaire de l'utilisateur                                       |
| `language`                             | `string`,&nbsp;`null`    | [PII] Langue de l'utilisateur                                        |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASFREQUENCYCAPSHARED #USERSCANVASFREQUENCYCAPSHARED" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| Champ                                  | Type                     | Description                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | ID globalement unique pour cet événement                             |
| `user_id`                              | `string`,&nbsp;`null`    | ID Braze de l'utilisateur qui a effectué cet événement               |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ID externe de l'utilisateur                                    |
| `device_id`                            | `string`,&nbsp;`null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme |
| `app_group_id`                         | `string`,&nbsp;`null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient    |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | ID API de l'espace de travail auquel cet utilisateur appartient      |
| `time`                                 | `int`,&nbsp;`null`       | Horodatage Unix auquel l'événement s'est produit                     |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Pour usage interne Braze uniquement) ID du Canvas auquel appartient cet événement |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | ID API du Canvas auquel appartient cet événement                     |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | ID API de la variante Canvas à laquelle appartient cet événement     |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | ID API de l'étape Canvas à laquelle appartient cet événement         |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | ID API de la variante de message de l'étape Canvas que cet utilisateur a reçue |
| `gender`                               | `string`,&nbsp;`null`    | [PII] Genre de l'utilisateur                                         |
| `country`                              | `string`,&nbsp;`null`    | [PII] Pays de l'utilisateur                                          |
| `timezone`                             | `string`,&nbsp;`null`    | Fuseau horaire de l'utilisateur                                       |
| `language`                             | `string`,&nbsp;`null`    | [PII] Langue de l'utilisateur                                        |
| `revenue`                              | `int`,&nbsp;`null`       | Montant du chiffre d'affaires généré en USD, affiché en centimes     |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe            |
| `app_api_id` | `string`,&nbsp;`null` | ID API de l'application sur laquelle cet événement s'est produit |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASREVENUESHARED #USERSCANVASREVENUESHARED" }

## Messages {#messages}


### USERS_MESSAGES_BANNER_ABORT_SHARED {#USERS_MESSAGES_BANNER_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel appartient cet utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel appartient cet utilisateur
`time` | `int` | Horodatage UNIX de l'événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`resolution` | `null,`&nbsp;`string` | Résolution de l'appareil
`carrier` | `null,`&nbsp;`string` | Opérateur de l'appareil
`browser` | `null,`&nbsp;`string` | Navigateur de l'appareil — extrait du user_agent — sur lequel l'ouverture s'est produite
`ad_id` | `null,`&nbsp;`string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Indique si le suivi publicitaire est activé pour l'appareil
`abort_type` | `null,`&nbsp;`string` | Type d'abandon. Pour une liste des valeurs, voir [Types d'abandon](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Message de journal décrivant les détails de l'abandon (jusqu'à 128 caractères)
`banner_placement_id` | `null,`&nbsp;`string` | ID d'emplacement du banner spécifié par le client
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESBANNERABORTSHARED #USERSMESSAGESBANNERABORTSHARED" }


### USERS_MESSAGES_BANNER_CLICK_SHARED {#USERS_MESSAGES_BANNER_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel appartient cet utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel appartient cet utilisateur
`time` | `int` | Horodatage UNIX de l'événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`resolution` | `null,`&nbsp;`string` | Résolution de l'appareil
`carrier` | `null,`&nbsp;`string` | Opérateur de l'appareil
`browser` | `null,`&nbsp;`string` | Navigateur de l'appareil — extrait du user_agent — sur lequel l'ouverture s'est produite
`button_id` | `null,`&nbsp;`string` | ID du bouton cliqué, s'il s'agit d'un clic sur un bouton
`ad_id` | `null,`&nbsp;`string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Indique si le suivi publicitaire est activé pour l'appareil
`banner_placement_id` | `null,`&nbsp;`string` | ID d'emplacement du banner spécifié par le client
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESBANNERCLICKSHARED #USERSMESSAGESBANNERCLICKSHARED" }


### USERS_MESSAGES_BANNER_IMPRESSION_SHARED {#USERS_MESSAGES_BANNER_IMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel appartient cet utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel appartient cet utilisateur
`time` | `int` | Horodatage UNIX de l'événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`resolution` | `null,`&nbsp;`string` | Résolution de l'appareil
`carrier` | `null,`&nbsp;`string` | Opérateur de l'appareil
`browser` | `null,`&nbsp;`string` | Navigateur de l'appareil — extrait du user_agent — sur lequel l'ouverture s'est produite
`ad_id` | `null,`&nbsp;`string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Indique si le suivi publicitaire est activé pour l'appareil
`banner_placement_id` | `null,`&nbsp;`string` | ID d'emplacement du banner spécifié par le client
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESBANNERIMPRESSIONSHARED #USERSMESSAGESBANNERIMPRESSIONSHARED" }

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`abort_type` | `null,`&nbsp;`string` | Type d'abandon. Pour une liste des valeurs, voir [Types d'abandon](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Message de journal décrivant les détails de l'abandon (2 000 caractères maximum)
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDABORTSHARED #USERSMESSAGESCONTENTCARDABORTSHARED" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`content_card_id` | `string` | ID de la carte ayant généré cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`resolution` | `null,`&nbsp;`string` | Résolution de l'appareil
`carrier` | `null,`&nbsp;`string` | Opérateur de l'appareil
`browser` | `null,`&nbsp;`string` | Navigateur de l'appareil
`ad_id` | `null,`&nbsp;`string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` ou `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Indique si le suivi publicitaire est activé pour l'appareil
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDCLICKSHARED #USERSMESSAGESCONTENTCARDCLICKSHARED" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`content_card_id` | `string` | ID de la carte ayant généré cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`resolution` | `null,`&nbsp;`string` | Résolution de l'appareil
`carrier` | `null,`&nbsp;`string` | Opérateur de l'appareil
`browser` | `null,`&nbsp;`string` | Navigateur de l'appareil
`ad_id` | `null,`&nbsp;`string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` ou `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Indique si le suivi publicitaire est activé pour l'appareil
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDDISMISSSHARED #USERSMESSAGESCONTENTCARDDISMISSSHARED" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`content_card_id` | `string` | ID de la carte ayant généré cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`resolution` | `null,`&nbsp;`string` | Résolution de l'appareil
`carrier` | `null,`&nbsp;`string` | Opérateur de l'appareil
`browser` | `null,`&nbsp;`string` | Navigateur de l'appareil
`ad_id` | `null,`&nbsp;`string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` ou `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Indique si le suivi publicitaire est activé pour l'appareil
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDIMPRESSIONSHARED #USERSMESSAGESCONTENTCARDIMPRESSIONSHARED" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`content_card_id` | `string` | ID de la carte ayant généré cet événement
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`message_extras` | `null,`&nbsp;`string` | [PII] Chaîne JSON des paires clé-valeur étiquetées lors du rendu Liquid
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDSENDSHARED #USERSMESSAGESCONTENTCARDSENDSHARED" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`email_address` | `string` | [PII] Adresse e-mail de l'utilisateur
`ip_pool` | `null,`&nbsp;`string` | Pool IP à partir duquel l'e-mail a été envoyé
`abort_type` | `null,`&nbsp;`string` | Type d'abandon. Pour une liste des valeurs, voir [Types d'abandon](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Message de journal décrivant les détails de l'abandon (2 000 caractères maximum)
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILABORTSHARED #USERSMESSAGESEMAILABORTSHARED" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`email_address` | `string` | [PII] Adresse e-mail de l'utilisateur
`sending_ip` | `null,`&nbsp;`string` | Adresse IP à partir de laquelle l'e-mail a été envoyé
`ip_pool` | `null,`&nbsp;`string` | Pool IP à partir duquel l'e-mail a été envoyé
`bounce_reason` | `null,`&nbsp;`string` | [PII] Code de raison SMTP et message lisible reçu pour cet événement de rebond
`esp` | `null,`&nbsp;`string` | fournisseur de services d'e-mailing lié à l'événement (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Domaine d'envoi de l'e-mail
`is_drop` | `null, boolean` | Indique que cet événement est comptabilisé comme un événement de suppression
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILBOUNCESHARED #USERSMESSAGESEMAILBOUNCESHARED" }

{% alert note %}
Il est possible d'observer plusieurs lignes pour le même utilisateur autour d'un même échec d'envoi définitif. Cela peut se produire lorsque les événements sont traités de manière asynchrone ou lorsque des envois liés possèdent des valeurs `dispatch_id` différentes. Lors de la déduplication ou de l'analyse des exports, pensez à prendre en compte `dispatch_id`, `time` et `id` ensemble.
{% endalert %}

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`email_address` | `string` | [PII] Adresse e-mail de l'utilisateur
`url` | `null,`&nbsp;`string` | URL sur laquelle l'utilisateur a cliqué
`user_agent` | `null,`&nbsp;`string` | User agent sur lequel le clic s'est produit
`ip_pool` | `null,`&nbsp;`string` | Pool IP à partir duquel l'e-mail a été envoyé
`link_id` | `null,`&nbsp;`string` | ID unique du lien cliqué, tel que créé par Braze
`link_alias` | `null,`&nbsp;`string` | Alias associé à cet ID de lien
`esp` | `null,`&nbsp;`string` | fournisseur de services d'e-mailing lié à l'événement (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Domaine d'envoi de l'e-mail
`is_amp` | `null, boolean` | Indique qu'il s'agit d'un événement AMP
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`is_suspected_bot_click` | `null, boolean` | Indique si cet événement a été traité comme un événement de bot
`suspected_bot_click_reason` | `null, object` | Raison pour laquelle cet événement a été classé comme provenant d'un bot
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILCLICKSHARED #USERSMESSAGESEMAILCLICKSHARED" }


### USERS_MESSAGES_EMAIL_DEFERRAL_SHARED {#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX de l'événement
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel appartient cet utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel appartient cet utilisateur
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID BSON du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`email_address` | `null,`&nbsp;`string` | [PII] Adresse e-mail de l'utilisateur
`recipient_domain` | `null,`&nbsp;`string` | Domaine e-mail du destinataire
`esp` | `null,`&nbsp;`string` | fournisseur de services d'e-mailing lié à l'événement (Sparkpost, Sendgrid ou Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Domaine d'envoi de l'e-mail
`ip_pool` | `null,`&nbsp;`string` | Pool IP à partir duquel l'e-mail a été envoyé
`sending_ip` | `null,`&nbsp;`string` | Adresse IP à partir de laquelle l'e-mail a été envoyé
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`deferral_reason` | `null,`&nbsp;`string` | [PII] Code de raison SMTP et message lisible reçu pour cet événement de report
`attempt_count` | `null, int` | Nombre de tentatives d'envoi du message
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILDEFERRALSHARED #USERSMESSAGESEMAILDEFERRALSHARED" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`email_address` | `string` | [PII] Adresse e-mail de l'utilisateur
`sending_ip` | `null,`&nbsp;`string` | Adresse IP à partir de laquelle l'e-mail a été envoyé
`ip_pool` | `null,`&nbsp;`string` | Pool IP à partir duquel l'e-mail a été envoyé
`esp` | `null,`&nbsp;`string` | fournisseur de services d'e-mailing lié à l'événement (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Domaine d'envoi de l'e-mail
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILDELIVERYSHARED #USERSMESSAGESEMAILDELIVERYSHARED" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`email_address` | `string` | [PII] Adresse e-mail de l'utilisateur
`user_agent` | `null,`&nbsp;`string` | User agent sur lequel le signalement de courrier indésirable s'est produit
`ip_pool` | `null,`&nbsp;`string` | Pool IP à partir duquel l'e-mail a été envoyé
`esp` | `null,`&nbsp;`string` | fournisseur de services d'e-mailing lié à l'événement (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Domaine d'envoi de l'e-mail
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILMARKASSPAMSHARED #USERSMESSAGESEMAILMARKASSPAMSHARED" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`email_address` | `string` | [PII] Adresse e-mail de l'utilisateur
`user_agent` | `null,`&nbsp;`string` | User agent sur lequel l'ouverture s'est produite
`ip_pool` | `null,`&nbsp;`string` | Pool IP à partir duquel l'e-mail a été envoyé
`machine_open` | `null,`&nbsp;`string` | Renseigné à « true » si l'événement d'ouverture est déclenché sans interaction de l'utilisateur, par exemple par un appareil Apple avec la protection de la confidentialité dans Mail activée. La valeur peut évoluer pour fournir plus de granularité.
`esp` | `null,`&nbsp;`string` | fournisseur de services d'e-mailing lié à l'événement (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Domaine d'envoi de l'e-mail
`is_amp` | `null, boolean` | Indique qu'il s'agit d'un événement AMP
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILOPENSHARED #USERSMESSAGESEMAILOPENSHARED" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`email_address` | `string` | [PII] Adresse e-mail de l'utilisateur
`ip_pool` | `null,`&nbsp;`string` | Pool IP à partir duquel l'e-mail a été envoyé
`message_extras` | `null,`&nbsp;`string` | [PII] Chaîne JSON des paires clé-valeur étiquetées lors du rendu Liquid
`esp` | `null,`&nbsp;`string` | fournisseur de services d'e-mailing lié à l'événement (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Domaine d'envoi de l'e-mail
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILSENDSHARED #USERSMESSAGESEMAILSENDSHARED" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`email_address` | `string` | [PII] Adresse e-mail de l'utilisateur
`sending_ip` | `null,`&nbsp;`string` | Adresse IP à partir de laquelle l'e-mail a été envoyé
`ip_pool` | `null,`&nbsp;`string` | Pool IP à partir duquel l'e-mail a été envoyé
`bounce_reason` | `null,`&nbsp;`string` | [PII] Code de raison SMTP et message lisible reçu pour cet événement de rebond
`esp` | `null,`&nbsp;`string` | fournisseur de services d'e-mailing lié à l'événement (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Domaine d'envoi de l'e-mail
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILSOFTBOUNCESHARED #USERSMESSAGESEMAILSOFTBOUNCESHARED" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

Ce tableau enregistre les désabonnements e-mail au niveau du message côté destinataire : clic sur un lien de désabonnement, désabonnement en un clic via le client de messagerie (List-Unsubscribe), soumissions via le centre de préférences et désabonnements signalés par l'fournisseur de services d'e-mailing. Les désabonnements effectués via la REST API ne sont pas inclus ; ceux-ci émettent des événements [`users.behaviors.subscriptiongroup.StateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#subscription-group-state-change-events) ou [`users.behaviors.subscription.GlobalStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#global-subscription-state-change-events) à la place.

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`email_address` | `string` | [PII] Adresse e-mail de l'utilisateur
`ip_pool` | `null,`&nbsp;`string` | Pool IP à partir duquel l'e-mail a été envoyé
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILUNSUBSCRIBESHARED #USERSMESSAGESEMAILUNSUBSCRIBESHARED" }

### USERS_MESSAGES_EMAIL_RETRY_SHARED {#USERS_MESSAGES_EMAIL_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Cet événement se produit lorsqu'un message est dépriorisé ou soumis à une limitation de fréquence, puis fait l'objet d'une nouvelle tentative dans la fenêtre de réessai configurée.

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | [PII] ID utilisateur Braze de l'utilisateur ayant déclenché cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`time` | `int` | Horodatage UNIX de l'événement
`retry_type` | `null,`&nbsp;`string` | Type de nouvelle tentative
`retry_log` | `null,`&nbsp;`string` | Message de log décrivant les détails de la nouvelle tentative
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`dispatch_id` | `null,`&nbsp;`string` | ID de la distribution à laquelle ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID BSON du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`email_address` | `null,`&nbsp;`string` | [PII] Adresse e-mail de l'utilisateur
`ip_pool` | `null,`&nbsp;`string` | Pool IP à partir duquel l'envoi d'e-mail a été effectué
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILRETRYSHARED #USERSMESSAGESEMAILRETRYSHARED" }

### USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED {#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campagne à laquelle cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_id` | `null,`&nbsp;`string` | ID BSON du Canvas auquel cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`feature_flag_id_name` | `null,`&nbsp;`string` | Identifiant du déploiement de Feature Flag
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`time` | `int` | Horodatage UNIX de l'événement
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`browser` | `null,`&nbsp;`string` | Navigateur de l'appareil — extrait de user_agent — sur lequel l'ouverture s'est produite
`carrier` | `null,`&nbsp;`string` | Opérateur de l'appareil
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`resolution` | `null,`&nbsp;`string` | Résolution de l'appareil
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant déclenché cet événement
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESFEATUREFLAGIMPRESSIONSHARED #USERSMESSAGESFEATUREFLAGIMPRESSIONSHARED" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant déclenché cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`card_api_id` | `null,`&nbsp;`string` | ID API de la carte
`dispatch_id` | `null,`&nbsp;`string` | ID de la distribution à laquelle ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`resolution` | `null,`&nbsp;`string` | Résolution de l'appareil
`carrier` | `null,`&nbsp;`string` | Opérateur de l'appareil
`browser` | `null,`&nbsp;`string` | Navigateur de l'appareil
`version` | `string` | Version du message in-app : legacy ou triggered
`ad_id` | `null,`&nbsp;`string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` ou `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Indique si le suivi publicitaire est activé sur l'appareil
`abort_type` | `null,`&nbsp;`string` | Type d'abandon. Pour la liste des valeurs, consultez [Types d'abandon](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Message de log décrivant les détails de l'abandon (2 000 caractères maximum)
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESINAPPMESSAGEABORTSHARED #USERSMESSAGESINAPPMESSAGEABORTSHARED" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant déclenché cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`card_api_id` | `null,`&nbsp;`string` | ID API de la carte
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`resolution` | `null,`&nbsp;`string` | Résolution de l'appareil
`carrier` | `null,`&nbsp;`string` | Opérateur de l'appareil
`browser` | `null,`&nbsp;`string` | Navigateur de l'appareil
`version` | `string` | Version du message in-app : legacy ou triggered
`button_id` | `null,`&nbsp;`string` | ID du bouton cliqué, si ce clic correspond à un clic sur un bouton
`ad_id` | `null,`&nbsp;`string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` ou `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Indique si le suivi publicitaire est activé sur l'appareil
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESINAPPMESSAGECLICKSHARED #USERSMESSAGESINAPPMESSAGECLICKSHARED" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant déclenché cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`card_api_id` | `null,`&nbsp;`string` | ID API de la carte
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`resolution` | `null,`&nbsp;`string` | Résolution de l'appareil
`carrier` | `null,`&nbsp;`string` | Opérateur de l'appareil
`browser` | `null,`&nbsp;`string` | Navigateur de l'appareil
`version` | `string` | Version du message in-app : legacy ou triggered
`ad_id` | `null,`&nbsp;`string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` ou `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Indique si le suivi publicitaire est activé sur l'appareil
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`message_extras` | `null,`&nbsp;`string` | [PII] Chaîne JSON des paires clé-valeur étiquetées lors du rendu Liquid
`locale_key` | `null,`&nbsp;`string` | [PII] Clé correspondant aux traductions (par exemple « en-us ») utilisées pour composer ce message (null pour la valeur par défaut).
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESINAPPMESSAGEIMPRESSIONSHARED #USERSMESSAGESINAPPMESSAGEIMPRESSIONSHARED" }


### USERS_MESSAGES_LINE_ABORT_SHARED {#USERS_MESSAGES_LINE_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique global de cet événement
`time` | `int` | Horodatage UNIX de l'événement
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant déclenché cet événement
`abort_log` | `null,`&nbsp;`string` | [PII] Message de log décrivant les détails de l'abandon (128 caractères maximum)
`abort_type` | `null,`&nbsp;`string` | Type d'abandon. Pour la liste des valeurs, consultez [Types d'abandon](#abort-types).
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de la distribution à laquelle ce message appartient
`line_channel_id` | `null,`&nbsp;`string` | ID du canal LINE depuis lequel le message a été envoyé ou reçu
`line_channel_name` | `null,`&nbsp;`string` | Nom du canal LINE depuis lequel le message a été envoyé ou reçu
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`native_line_id` | `null,`&nbsp;`string` | [PII] ID LINE de l'utilisateur depuis lequel le message a été envoyé ou reçu
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`subscription_group_api_id` | `string` | ID API du groupe d'abonnement
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`campaign_name` | `null,`&nbsp;`string` | Nom de la campagne
`canvas_step_name` | `null,`&nbsp;`string` | Nom de l'étape Canvas
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINEABORTSHARED #USERSMESSAGESLINEABORTSHARED" }


### USERS_MESSAGES_LINE_CLICK_SHARED {#USERS_MESSAGES_LINE_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique global de cet événement
`time` | `int` | Horodatage UNIX de l'événement
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant déclenché cet événement
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`native_line_id` | `null,`&nbsp;`string` | [PII] ID LINE de l'utilisateur depuis lequel le message a été envoyé ou reçu
`line_channel_id` | `null,`&nbsp;`string` | ID du canal LINE depuis lequel le message a été envoyé ou reçu
`line_channel_name` | `null,`&nbsp;`string` | Nom du canal LINE depuis lequel le message a été envoyé ou reçu
`subscription_group_api_id` | `string` | ID API du groupe d'abonnement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`campaign_name` | `null,`&nbsp;`string` | Nom de la campagne
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`canvas_step_name` | `null,`&nbsp;`string` | Nom de l'étape Canvas
`dispatch_id` | `null,`&nbsp;`string` | ID de la distribution à laquelle ce message appartient
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`is_suspected_bot_click` | `null, boolean` | Indique si cet événement a été traité comme un événement de bot
`short_url` | `null,`&nbsp;`string` | URL raccourcie ayant été cliquée
`url` | `null,`&nbsp;`string` | URL sur laquelle l'utilisateur a cliqué
`user_agent` | `null,`&nbsp;`string` | User agent sur lequel le signalement de courrier indésirable s'est produit
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINECLICKSHARED #USERSMESSAGESLINECLICKSHARED" }


### USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique global de cet événement
`time` | `int` | Horodatage UNIX de l'événement
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant déclenché cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`campaign_name` | `null,`&nbsp;`string` | Nom de la campagne
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`canvas_step_name` | `null,`&nbsp;`string` | Nom de l'étape Canvas
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de la distribution à laquelle ce message appartient
`line_channel_id` | `null,`&nbsp;`string` | ID du canal LINE depuis lequel le message a été envoyé ou reçu
`line_channel_name` | `null,`&nbsp;`string` | Nom du canal LINE depuis lequel le message a été envoyé ou reçu
`media_id` | `null,`&nbsp;`string` | ID généré par LINE pouvant être utilisé pour récupérer les médias entrants depuis LINE
`message_body` | `null,`&nbsp;`string` | Réponse saisie par l'utilisateur
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`native_line_id` | `null,`&nbsp;`string` | [PII] ID LINE de l'utilisateur depuis lequel le message a été envoyé ou reçu
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`subscription_group_api_id` | `string` | ID API du groupe d'abonnement
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINEINBOUNDRECEIVESHARED #USERSMESSAGESLINEINBOUNDRECEIVESHARED" }


### USERS_MESSAGES_LINE_SEND_SHARED {#USERS_MESSAGES_LINE_SEND_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique global de cet événement
`time` | `int` | Horodatage UNIX de l'événement
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant déclenché cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`campaign_name` | `null,`&nbsp;`string` | Nom de la campagne
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`canvas_step_name` | `null,`&nbsp;`string` | Nom de l'étape Canvas
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de la distribution à laquelle ce message appartient
`line_channel_id` | `null,`&nbsp;`string` | ID du canal LINE depuis lequel le message a été envoyé ou reçu
`line_channel_name` | `null,`&nbsp;`string` | Nom du canal LINE depuis lequel le message a été envoyé ou reçu
`message_extras` | `null,`&nbsp;`string` | [PII] Chaîne JSON des paires clé-valeur étiquetées lors du rendu Liquid
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`native_line_id` | `null,`&nbsp;`string` | [PII] ID LINE de l'utilisateur depuis lequel le message a été envoyé ou reçu
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`subscription_group_api_id` | `string` | ID API du groupe d'abonnement
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINESENDSHARED #USERSMESSAGESLINESENDSHARED" }

### USERS_MESSAGES_LINE_RETRY_SHARED {#USERS_MESSAGES_LINE_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Cet événement se produit lorsqu'un message est dépriorisé ou soumis à une limitation de fréquence, puis fait l'objet d'une nouvelle tentative dans la fenêtre de réessai configurée.

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | [PII] ID utilisateur Braze de l'utilisateur ayant déclenché cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`time` | `int` | Horodatage UNIX de l'événement
`retry_type` | `null,`&nbsp;`string` | Type de nouvelle tentative
`retry_log` | `null,`&nbsp;`string` | Message de log décrivant les détails de la nouvelle tentative
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`dispatch_id` | `null,`&nbsp;`string` | ID de la distribution à laquelle ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID BSON du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`line_channel_id` | `null,`&nbsp;`string` | ID du canal LINE depuis lequel le message a été envoyé ou reçu
`line_channel_name` | `null,`&nbsp;`string` | Nom du canal LINE depuis lequel le message a été envoyé ou reçu
`native_line_id` | `null,`&nbsp;`string` | [PII] ID LINE de l'utilisateur depuis lequel le message a été envoyé ou reçu
`subscription_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'abonnement
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINERETRYSHARED #USERSMESSAGESLINERETRYSHARED" }


### USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED {#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant déclenché cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`time` | `int` | Horodatage UNIX de l'événement
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`activity_id` | `null,`&nbsp;`string` | Identifiant de la en direct or en ligne/en production/instantané Activity
`activity_attributes_type` | `null,`&nbsp;`string` | Type d'attribut de la en direct or en ligne/en production/instantané Activity
`push_to_start_token` | `null,`&nbsp;`string` | Jeton push to start de la en direct or en ligne/en production/instantané Activity
`update_token` | `null,`&nbsp;`string` | Jeton de mise à jour de la en direct or en ligne/en production/instantané Activity
`live_activity_event_type` | `null,`&nbsp;`string` | Type d'événement de la en direct or en ligne/en production/instantané Activity. Un parmi ['start', 'update', 'end']
`live_activity_event_outcome` | `null,`&nbsp;`string` | Résultat de l'événement en direct or en ligne/en production/instantané Activity
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLIVEACTIVITYOUTCOMESHARED #USERSMESSAGESLIVEACTIVITYOUTCOMESHARED" }


### USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED {#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant déclenché cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`time` | `int` | Horodatage UNIX de l'événement
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`activity_id` | `null,`&nbsp;`string` | Identifiant de la en direct or en ligne/en production/instantané Activity
`activity_attributes_type` | `null,`&nbsp;`string` | Type d'attribut de la en direct or en ligne/en production/instantané Activity
`push_to_start_token` | `null,`&nbsp;`string` | Jeton push to start de la en direct or en ligne/en production/instantané Activity
`update_token` | `null,`&nbsp;`string` | Jeton de mise à jour de la en direct or en ligne/en production/instantané Activity
`live_activity_event_type` | `null,`&nbsp;`string` | Type d'événement de la en direct or en ligne/en production/instantané Activity. Un parmi ['start', 'update', 'end']
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLIVEACTIVITYSENDSHARED #USERSMESSAGESLIVEACTIVITYSENDSHARED" }


### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant déclenché cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`time` | `int` | Horodatage UNIX de l'événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`card_api_id` | `null,`&nbsp;`string` | ID API de la carte
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`resolution` | `null,`&nbsp;`string` | Résolution de l'appareil
`carrier` | `null,`&nbsp;`string` | Opérateur de l'appareil
`browser` | `null,`&nbsp;`string` | Navigateur de l'appareil — extrait de user_agent — sur lequel l'ouverture s'est produite
`abort_type` | `null,`&nbsp;`string` | Type d'abandon. Pour la liste des valeurs, consultez [Types d'abandon](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Message de log décrivant les détails de l'abandon (128 caractères maximum)
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESNEWSFEEDCARDABORTSHARED #USERSMESSAGESNEWSFEEDCARDABORTSHARED" }


### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant déclenché cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`time` | `int` | Horodatage UNIX de l'événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`card_api_id` | `null,`&nbsp;`string` | ID API de la carte
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`resolution` | `null,`&nbsp;`string` | Résolution de l'appareil
`carrier` | `null,`&nbsp;`string` | Opérateur de l'appareil
`browser` | `null,`&nbsp;`string` | Navigateur de l'appareil — extrait de user_agent — sur lequel l'ouverture s'est produite
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESNEWSFEEDCARDCLICKSHARED #USERSMESSAGESNEWSFEEDCARDCLICKSHARED" }


### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant déclenché cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`time` | `int` | Horodatage UNIX de l'événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`card_api_id` | `null,`&nbsp;`string` | ID API de la carte
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`resolution` | `null,`&nbsp;`string` | Résolution de l'appareil
`carrier` | `null,`&nbsp;`string` | Opérateur de l'appareil
`browser` | `null,`&nbsp;`string` | Navigateur de l'appareil — extrait de user_agent — sur lequel l'ouverture s'est produite
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESNEWSFEEDCARDIMPRESSIONSHARED #USERSMESSAGESNEWSFEEDCARDIMPRESSIONSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant déclenché cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` vers lequel une tentative de livraison a été effectuée
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de la distribution à laquelle ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`platform` | `string` | Plateforme de l'appareil
`abort_type` | `null,`&nbsp;`string` | Type d'abandon. Pour la liste des valeurs, consultez [Types d'abandon](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Message de log décrivant les détails de l'abandon (2 000 caractères maximum)
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONABORTSHARED #USERSMESSAGESPUSHNOTIFICATIONABORTSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant déclenché cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`push_token` | `null,`&nbsp;`string` | Jeton push ayant rebondi
`device_id` | `null,`&nbsp;`string` | `device_id` vers lequel une tentative de livraison ayant rebondi a été effectuée
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de la distribution à laquelle ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`ad_id` | `null,`&nbsp;`string` | [PII] Identifiant publicitaire de l'appareil vers lequel une tentative de livraison a été effectuée
`ad_id_type` | `null,`&nbsp;`string` | Type de l'identifiant publicitaire
`ad_tracking_enabled` | `null, boolean` | Indique si le suivi publicitaire est activé
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONBOUNCESHARED #USERSMESSAGESPUSHNOTIFICATIONBOUNCESHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant déclenché cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de la distribution à laquelle ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`resolution` | `null,`&nbsp;`string` | Résolution de l'appareil
`carrier` | `null,`&nbsp;`string` | Opérateur de l'appareil
`browser` | `null,`&nbsp;`string` | Navigateur de l'appareil
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été capté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONINFLUENCEDOPENSHARED #USERSMESSAGESPUSHNOTIFICATIONINFLUENCEDOPENSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

{% alert important %}
Cet événement n'est pas pris en charge par le [SDK Swift](https://github.com/braze-inc/braze-swift-sdk) et est obsolète dans le [SDK Obj-C](https://github.com/Appboy/appboy-ios-sdk).
{% endalert %}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du workspace auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix du moment où l'événement s'est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la Campaign à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la Campaign à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`resolution` | `null,`&nbsp;`string` | Résolution de l'appareil
`carrier` | `null,`&nbsp;`string` | Opérateur de l'appareil
`browser` | `null,`&nbsp;`string` | Navigateur de l'appareil
`ad_id` | `null,`&nbsp;`string` | [PII] Identifiant publicitaire de l'appareil vers lequel une tentative de distribution a été effectuée
`ad_id_type` | `null,`&nbsp;`string` | Type de l'identifiant publicitaire
`ad_tracking_enabled` | `null, boolean` | Indique si le suivi publicitaire est activé ou non
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONIOSFOREGROUNDSHARED #USERSMESSAGESPUSHNOTIFICATIONIOSFOREGROUNDSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du workspace auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix du moment où l'événement s'est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la Campaign à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la Campaign à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,`&nbsp;`string` | Version du SDK Braze utilisée lors de l'événement
`platform` | `null,`&nbsp;`string` | Plateforme de l'appareil
`os_version` | `null,`&nbsp;`string` | Version du système d'exploitation de l'appareil
`device_model` | `null,`&nbsp;`string` | Modèle de l'appareil
`resolution` | `null,`&nbsp;`string` | Résolution de l'appareil
`carrier` | `null,`&nbsp;`string` | Opérateur de l'appareil
`browser` | `null,`&nbsp;`string` | Navigateur de l'appareil
`button_string` | `null,`&nbsp;`string` | Identifiant (button_string) du bouton de notification push cliqué. null si le clic ne provient pas d'un bouton
`button_action_type` | `null,`&nbsp;`string` | Type d'action du bouton de notification push. L'une des valeurs suivantes : [URI, DEEP_LINK, NONE, CLOSE]. null si le clic ne provient pas d'un bouton
`slide_id` | `null,`&nbsp;`string` | Identifiant de la diapositive du carrousel push sur laquelle l'utilisateur a cliqué
`slide_action_type` | `null,`&nbsp;`string` | Type d'action de la diapositive du carrousel push
`ad_id` | `null,`&nbsp;`string` | [PII] Identifiant publicitaire de l'appareil vers lequel une tentative de distribution a été effectuée
`ad_id_type` | `null,`&nbsp;`string` | Type de l'identifiant publicitaire
`ad_tracking_enabled` | `null, boolean` | Indique si le suivi publicitaire est activé ou non
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONOPENSHARED #USERSMESSAGESPUSHNOTIFICATIONOPENSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`push_token` | `null,`&nbsp;`string` | Jeton push vers lequel une tentative de distribution a été effectuée
`device_id` | `null,`&nbsp;`string` | `device_id` vers lequel une tentative de distribution a été effectuée
`app_group_api_id` | `null,`&nbsp;`string` | ID API du workspace auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix du moment où l'événement s'est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l'application sur laquelle cet événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la Campaign à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la Campaign à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`platform` | `string` | Plateforme de l'appareil
`ad_id` | `null,`&nbsp;`string` | [PII] Identifiant publicitaire de l'appareil vers lequel une tentative de distribution a été effectuée
`ad_id_type` | `null,`&nbsp;`string` | Type de l'identifiant publicitaire
`ad_tracking_enabled` | `null, boolean` | Indique si le suivi publicitaire est activé ou non
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`message_extras` | `null,`&nbsp;`string` | [PII] Chaîne JSON des paires clé-valeur balisées lors du rendu Liquid
`is_sampled` | `null,`&nbsp;`string` | Indique si l'envoi push a été échantillonné et si un événement de distribution était attendu
`locale_key` | `null,`&nbsp;`string` | [PII] Clé correspondant aux traductions (par exemple 'en-us') utilisées pour composer ce message (null par défaut).
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONSENDSHARED #USERSMESSAGESPUSHNOTIFICATIONSENDSHARED" }


### USERS_MESSAGES_RCS_ABORT_SHARED {#USERS_MESSAGES_RCS_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX du moment où l'événement s'est produit
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant effectué cet événement
`abort_log` | `null,`&nbsp;`string` | [PII] Message de journal décrivant les détails de l'abandon (jusqu'à 128 caractères)
`abort_type` | `null,`&nbsp;`string` | Type d'abandon. Pour la liste des valeurs, consultez [Types d'abandon](#abort-types).
`campaign_name` | `null,`&nbsp;`string` | Nom de la Campaign
`canvas_id` | `null,`&nbsp;`string` | ID BSON du Canvas auquel cet événement appartient
`canvas_name` | `null,`&nbsp;`string` | Nom du Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nom de l'étape du Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Nom de la variante Canvas reçue par cet utilisateur
`message_variation_name` | `null,`&nbsp;`string` | Nom de la variante de message
`subscription_group_api_id` | `string` | ID API du groupe d'abonnement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la Campaign à laquelle cet événement appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSABORTSHARED #USERSMESSAGESRCSABORTSHARED" }


### USERS_MESSAGES_RCS_CLICK_SHARED {#USERS_MESSAGES_RCS_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX du moment où l'événement s'est produit
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant effectué cet événement
`campaign_name` | `null,`&nbsp;`string` | Nom de la Campaign
`canvas_id` | `null,`&nbsp;`string` | ID BSON du Canvas auquel cet événement appartient
`canvas_name` | `null,`&nbsp;`string` | Nom du Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nom de l'étape du Canvas
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`is_suspected_bot_click` | `null, boolean` | Indique si cet événement a été traité comme un événement de bot
`message_variation_name` | `null,`&nbsp;`string` | Nom de la variante de message
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`short_url` | `null,`&nbsp;`string` | URL raccourcie sur laquelle l'utilisateur a cliqué
`suspected_bot_click_reason` | `null,`&nbsp;`string` | Raison pour laquelle cet événement a été classifié comme provenant d'un bot
`user_agent` | `null,`&nbsp;`string` | Agent utilisateur sur lequel le signalement de courrier indésirable s'est produit
`user_phone_number` | `null,`&nbsp;`string` | [PII] Numéro de téléphone de l'utilisateur depuis lequel le message a été reçu
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`interaction_type` | `null,`&nbsp;`string` | Type d'interaction ayant généré le clic. Exemples de valeurs de chaîne : Text URL, Reply, OpenURL
`element_label` | `null,`&nbsp;`string` | Détails facultatifs sur l'élément cliqué, comme le texte d'une réponse suggérée ou d'un bouton
`element_type` | `null,`&nbsp;`string` | Précise si un interaction_type commun aux suggestions et boutons provient d'une suggestion ou d'un bouton. Exemples : Suggestion, Button
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la Campaign à laquelle cet événement appartient
`url` | `null,`&nbsp;`string` | URL sur laquelle l'utilisateur a cliqué
`subscription_group_api_id` | `string` | ID API du groupe d'abonnement
`canvas_variation_name` | `null,`&nbsp;`string` | Nom de la variante Canvas reçue par cet utilisateur
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSCLICKSHARED #USERSMESSAGESRCSCLICKSHARED" }


### USERS_MESSAGES_RCS_DELIVERY_SHARED {#USERS_MESSAGES_RCS_DELIVERY_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX du moment où l'événement s'est produit
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant effectué cet événement
`campaign_name` | `null,`&nbsp;`string` | Nom de la Campaign
`canvas_id` | `null,`&nbsp;`string` | ID BSON du Canvas auquel cet événement appartient
`canvas_name` | `null,`&nbsp;`string` | Nom du Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nom de l'étape du Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Nom de la variante Canvas reçue par cet utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`message_variation_name` | `null,`&nbsp;`string` | Nom de la variante de message
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`subscription_group_api_id` | `string` | ID API du groupe d'abonnement
`to_phone_number` | `null,`&nbsp;`string` | [PII] Numéro de téléphone de l'utilisateur recevant le message au format e.164 (par exemple +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la Campaign à laquelle cet événement appartient
`from_rcs_sender` | `null,`&nbsp;`string` | ID de l'expéditeur RCS ou nom de l'agent utilisé pour envoyer le message
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSDELIVERYSHARED #USERSMESSAGESRCSDELIVERYSHARED" }


### USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX du moment où l'événement s'est produit
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant effectué cet événement
`action` | `null,`&nbsp;`string` | Action effectuée en réponse à ce message (par exemple Subscribed, Unsubscribed ou None).
`campaign_name` | `null,`&nbsp;`string` | Nom de la Campaign
`canvas_id` | `null,`&nbsp;`string` | ID BSON du Canvas auquel cet événement appartient
`canvas_name` | `null,`&nbsp;`string` | Nom du Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nom de l'étape du Canvas
`media_urls` | `null,`&nbsp;`string` | URL des médias envoyés par l'utilisateur
`message_variation_name` | `null,`&nbsp;`string` | Nom de la variante de message
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`user_phone_number` | `null,`&nbsp;`string` | [PII] Numéro de téléphone de l'utilisateur depuis lequel le message a été reçu
`subscription_group_api_id` | `string` | ID API du groupe d'abonnement
`message_body` | `null,`&nbsp;`string` | Réponse saisie par l'utilisateur
`to_rcs_sender` | `null,`&nbsp;`string` | L'expéditeur RCS entrant auquel le message a été envoyé
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la Campaign à laquelle cet événement appartient
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la Campaign à laquelle cet événement appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSINBOUNDRECEIVESHARED #USERSMESSAGESRCSINBOUNDRECEIVESHARED" }


### USERS_MESSAGES_RCS_READ_SHARED {#USERS_MESSAGES_RCS_READ_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX du moment où l'événement s'est produit
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant effectué cet événement
`campaign_name` | `null,`&nbsp;`string` | Nom de la Campaign
`canvas_id` | `null,`&nbsp;`string` | ID BSON du Canvas auquel cet événement appartient
`canvas_name` | `null,`&nbsp;`string` | Nom du Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nom de l'étape du Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Nom de la variante Canvas reçue par cet utilisateur
`message_variation_name` | `null,`&nbsp;`string` | Nom de la variante de message
`to_phone_number` | `null,`&nbsp;`string` | [PII] Numéro de téléphone de l'utilisateur recevant le message au format e.164 (par exemple +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la Campaign à laquelle cet événement appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSREADSHARED #USERSMESSAGESRCSREADSHARED" }


### USERS_MESSAGES_RCS_REJECTION_SHARED {#USERS_MESSAGES_RCS_REJECTION_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX du moment où l'événement s'est produit
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant effectué cet événement
`campaign_name` | `null,`&nbsp;`string` | Nom de la Campaign
`canvas_id` | `null,`&nbsp;`string` | ID BSON du Canvas auquel cet événement appartient
`canvas_name` | `null,`&nbsp;`string` | Nom du Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nom de l'étape du Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Nom de la variante Canvas reçue par cet utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`error` | `null,`&nbsp;`string` | Nom de l'erreur
`from_rcs_sender` | `null,`&nbsp;`string` | ID de l'expéditeur RCS ou nom de l'agent utilisé pour envoyer le message
`is_sms_fallback` | `null, boolean` | Indique si un repli SMS a été tenté pour ce message RCS rejeté. Cet événement est lié/associé à l'événement de distribution SMS
`message_variation_name` | `null,`&nbsp;`string` | Nom de la variante de message
`provider_error_code` | `null,`&nbsp;`string` | Code d'erreur du fournisseur
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`subscription_group_api_id` | `string` | ID API du groupe d'abonnement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`to_phone_number` | `null,`&nbsp;`string` | [PII] Numéro de téléphone de l'utilisateur recevant le message au format e.164 (par exemple +14155552671)
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la Campaign à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSREJECTIONSHARED #USERSMESSAGESRCSREJECTIONSHARED" }


### USERS_MESSAGES_RCS_SEND_SHARED {#USERS_MESSAGES_RCS_SEND_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX du moment où l'événement s'est produit
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant effectué cet événement
`campaign_name` | `null,`&nbsp;`string` | Nom de la Campaign
`canvas_id` | `null,`&nbsp;`string` | ID BSON du Canvas auquel cet événement appartient
`canvas_name` | `null,`&nbsp;`string` | Nom du Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nom de l'étape du Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Nom de la variante Canvas reçue par cet utilisateur
`category` | `null,`&nbsp;`string` | Nom de la catégorie de mot-clé, renseigné uniquement pour les messages de réponse automatique : 'opt-in', 'opt-out', 'help' ou une valeur personnalisée
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`from_rcs_sender` | `null,`&nbsp;`string` | ID de l'expéditeur RCS ou nom de l'agent utilisé pour envoyer le message
`message_extras` | `null,`&nbsp;`string` | Chaîne JSON des paires clé-valeur balisées lors du rendu Liquid
`message_variation_name` | `null,`&nbsp;`string` | Nom de la variante de message
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`subscription_group_api_id` | `string` | ID API du groupe d'abonnement
`to_phone_number` | `null,`&nbsp;`string` | [PII] Numéro de téléphone de l'utilisateur recevant le message au format e.164 (par exemple +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la Campaign à laquelle cet événement appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSSENDSHARED #USERSMESSAGESRCSSENDSHARED" }

## Événements de messages SMS et profils utilisateur supprimés {#sms-message-events-and-deleted-user-profiles}

{% alert note %}
Pour les tables partagées `USERS_MESSAGES_SMS_*` (y compris [`USERS_MESSAGES_SMS_REJECTION_SHARED`](#USERS_MESSAGES_SMS_REJECTION_SHARED), [`USERS_MESSAGES_SMS_DELIVERY_SHARED`](#USERS_MESSAGES_SMS_DELIVERY_SHARED) et [`USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED`](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED)), Braze n'écrit une ligne que lorsque le profil utilisateur Braze existe encore dans l'espace de travail au moment du traitement de l'événement pour Snowflake Data Sharing et Currents. Si l'utilisateur a été supprimé avant la fin du traitement, l'événement n'apparaît pas dans Snowflake ni dans votre export Currents, même si les indicateurs SMS de l'espace de travail dans le tableau de bord reflètent toujours les comptages agrégés issus du chemin de reporting de Braze. Pour le comportement Currents correspondant, consultez [Événements de rejet SMS]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-rejection-events) et les types d'événements SMS associés dans le même glossaire.
{% endalert %}

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externe du groupe d'abonnement
`abort_type` | `null,`&nbsp;`string` | Type d'abandon. Pour la liste des valeurs, consultez [Types d'abandon](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Message de journal décrivant les détails de l'abandon (maximum 2 000 caractères)
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSABORTSHARED #USERSMESSAGESSMSABORTSHARED" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`to_phone_number` | `null,`&nbsp;`string` | [PII] Numéro de téléphone du destinataire
`from_phone_number` | `null,`&nbsp;`string` | Numéro de téléphone à partir duquel le message SMS a été envoyé
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externe du groupe d'abonnement
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSCARRIERSENDSHARED #USERSMESSAGESSMSCARRIERSENDSHARED" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`to_phone_number` | `null,`&nbsp;`string` | [PII] Numéro de téléphone du destinataire
`from_phone_number` | `null,`&nbsp;`string` | Numéro de téléphone à partir duquel le message SMS a été envoyé
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externe du groupe d'abonnement
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`is_sms_fallback` | `null, boolean` | Indique si un repli SMS a été tenté pour ce message RCS rejeté. Il est lié/associé à l'événement SMS Delivery
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSDELIVERYSHARED #USERSMESSAGESSMSDELIVERYSHARED" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`to_phone_number` | `null,`&nbsp;`string` | [PII] Numéro de téléphone du destinataire
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externe du groupe d'abonnement
`error` | `null,`&nbsp;`string` | Nom de l'erreur
`provider_error_code` | `null,`&nbsp;`string` | Code d'erreur du fournisseur de services SMS
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`is_sms_fallback` | `null, boolean` | Indique si un repli SMS a été tenté pour ce message RCS rejeté. Il est lié/associé à l'événement SMS Delivery
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSDELIVERYFAILURESHARED #USERSMESSAGESSMSDELIVERYFAILURESHARED" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `null,`&nbsp;`string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail associé au numéro de téléphone entrant
`time` | `int` | Horodatage Unix de l'événement
`user_phone_number` | `string` | [PII] Numéro de téléphone de l'utilisateur à partir duquel le message a été reçu
`subscription_group_id` | `null,`&nbsp;`string` | ID du groupe d'abonnement ciblé pour ce message SMS
`subscription_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'abonnement ciblé pour ce message SMS
`inbound_phone_number` | `string` | Numéro entrant auquel le message a été envoyé
`action` | `string` | Action effectuée en réponse à ce message. Par exemple, `Subscribed`, `Unsubscribed` ou `None`.
`message_body` | `string` | Réponse de l'utilisateur
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | URL multimédias de l'utilisateur
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message à laquelle cet événement appartient
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas à laquelle cet événement appartient
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSINBOUNDRECEIVESHARED #USERSMESSAGESSMSINBOUNDRECEIVESHARED" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`to_phone_number` | `null,`&nbsp;`string` | [PII] Numéro de téléphone du destinataire
`from_phone_number` | `null,`&nbsp;`string` | Numéro de téléphone à partir duquel le message SMS a été envoyé
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externe du groupe d'abonnement
`error` | `null,`&nbsp;`string` | Nom de l'erreur
`provider_error_code` | `null,`&nbsp;`string` | Code d'erreur du fournisseur de services SMS
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`is_sms_fallback` | `null, boolean` | Indique si un repli SMS a été tenté pour ce message RCS rejeté. Il est lié/associé à l'événement SMS Delivery
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSREJECTIONSHARED #USERSMESSAGESSMSREJECTIONSHARED" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`to_phone_number` | `null,`&nbsp;`string` | [PII] Numéro de téléphone du destinataire
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externe du groupe d'abonnement
`category` | `null,`&nbsp;`string` | Nom de la catégorie de mot-clé, renseigné uniquement pour les messages de réponse automatique : 'Opt-in', 'Opt-out', 'Help' ou une valeur personnalisée
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`message_extras` | `null,`&nbsp;`string` | [PII] Chaîne JSON des paires clé-valeur balisées lors du rendu Liquid
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSSENDSHARED #USERSMESSAGESSMSSENDSHARED" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `null,`&nbsp;`string` | ID Braze de l'utilisateur ciblé par short_url, null si short_url n'utilise pas le suivi des clics par utilisateur
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur ciblé par short_url s'il en existe un, null si short_url n'utilise pas le suivi des clics par utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail utilisé pour générer short_url
`time` | `int` | Horodatage Unix du clic sur short_url
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`campaign_id` | `null,`&nbsp;`string` | ID Braze de la campagne pour laquelle short_url a été généré, null si ne provient pas d'une campagne
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne pour laquelle short_url a été généré, null si ne provient pas d'une campagne
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message pour laquelle short_url a été généré, null si ne provient pas d'une campagne
`canvas_id` | `null,`&nbsp;`string` | ID Braze du Canvas pour lequel short_url a été généré, null si ne provient pas d'un Canvas
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas pour lequel short_url a été généré, null si ne provient pas d'un Canvas
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas pour laquelle short_url a été généré, null si ne provient pas d'un Canvas
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas pour laquelle short_url a été généré, null si ne provient pas d'un Canvas
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas pour laquelle short_url a été généré, null si ne provient pas d'un Canvas
`url` | `string` | URL d'origine contenue dans le message vers laquelle short_url redirige
`short_url` | `string` | URL raccourcie ayant été cliquée
`user_agent` | `null,`&nbsp;`string` | Agent utilisateur ayant demandé short_url
`user_phone_number` | `string` | [PII] Numéro de téléphone de l'utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`is_suspected_bot_click` | `null, boolean` | Indique si cet événement a été traité comme un événement de bot
`suspected_bot_click_reason` | `null, object` | Raison pour laquelle cet événement a été classé comme provenant d'un bot
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSSHORTLINKCLICKSHARED #USERSMESSAGESSMSSHORTLINKCLICKSHARED" }

### USERS_MESSAGES_SMS_RETRY_SHARED {#USERS_MESSAGES_SMS_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Cet événement se produit lorsqu'un message est dépriorisé ou soumis à une limitation de fréquence, puis réessayé ultérieurement dans la fenêtre de nouvelle tentative configurée.

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | [PII] ID utilisateur Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`time` | `int` | Horodatage UNIX de l'événement
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID BSON du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`subscription_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'abonnement
`retry_type` | `null,`&nbsp;`string` | Type de nouvelle tentative
`retry_log` | `null,`&nbsp;`string` | Message de journal décrivant les détails de la nouvelle tentative
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSRETRYSHARED #USERSMESSAGESSMSRETRYSHARED" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`abort_type` | `null,`&nbsp;`string` | Type d'abandon. Pour la liste des valeurs, consultez [Types d'abandon](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Message de journal décrivant les détails de l'abandon (maximum 2 000 caractères)
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKABORTSHARED #USERSMESSAGESWEBHOOKABORTSHARED" }


### USERS_MESSAGES_WEBHOOK_FAILURE_SHARED {#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED}

Champ | Type | Description
------|------|------------
`http_status_code` | `null, int` | Code de statut HTTP de la réponse
`endpoint_url` | `null,`&nbsp;`string` | URL de l'endpoint interrogé
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campagne à laquelle cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_id` | `null,`&nbsp;`string` | ID BSON du Canvas auquel cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`content_length` | `null, int` | Longueur du contenu de la réponse
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`host` | `null,`&nbsp;`string` | Hôte de la requête
`id` | `string` | ID unique global de cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`raw_response` | `null,`&nbsp;`string` | Réponse brute tronquée de l'endpoint
`retry_count` | `null, int` | Nombre de nouvelles tentatives effectuées
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`time` | `int` | Horodatage UNIX de l'événement
`url_path` | `null,`&nbsp;`string` | Chemin de l'URL interrogée
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant effectué cet événement
`webhook_duration` | `null, int` | Durée totale de cette requête en millisecondes
`webhook_failure_source` | `null,`&nbsp;`string` | Indique si une erreur a été créée par Braze ou par l'endpoint lui-même. Le champ source peut être External Endpoint, Treat no status code to host unreachable
`is_terminal` | `null, boolean` | Indique si cet événement était la dernière tentative d'envoi
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKFAILURESHARED #USERSMESSAGESWEBHOOKFAILURESHARED" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`time` | `int` | Horodatage Unix de l'événement
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`campaign_name` | `null,`&nbsp;`string` | Nom de la campagne
`message_variation_name` | `null,`&nbsp;`string` | Nom de la variante de message
`canvas_name` | `null,`&nbsp;`string` | Nom du Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Nom de la variante du Canvas reçue par cet utilisateur
`canvas_step_name` | `null,`&nbsp;`string` | Nom de l'étape du Canvas
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`message_extras` | `null,`&nbsp;`string` | [PII] Chaîne JSON des paires clé-valeur balisées lors du rendu Liquid
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKSENDSHARED #USERSMESSAGESWEBHOOKSENDSHARED" }

### USERS_MESSAGES_WEBHOOK_RETRY_SHARED {#USERS_MESSAGES_WEBHOOK_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Cet événement se produit lorsqu'un message est dépriorisé ou soumis à une limitation de fréquence, puis réessayé ultérieurement dans la fenêtre de nouvelle tentative configurée.

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | [PII] ID utilisateur Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`time` | `int` | Horodatage UNIX de l'événement
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID BSON du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`gender` | `null,`&nbsp;`string` | [PII] Genre de l'utilisateur
`country` | `null,`&nbsp;`string` | [PII] Pays de l'utilisateur
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`language` | `null,`&nbsp;`string` | [PII] Langue de l'utilisateur
`retry_type` | `null,`&nbsp;`string` | Type de nouvelle tentative
`retry_log` | `null,`&nbsp;`string` | Message de journal décrivant les détails de la nouvelle tentative
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKRETRYSHARED #USERSMESSAGESWEBHOOKRETRYSHARED" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`time` | `int` | Horodatage Unix de l'événement
`to_phone_number` | 	`null,`&nbsp;`string` | [PII] Numéro de téléphone du destinataire
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | ID de l'espace de travail auquel cet utilisateur appartient
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`subscription_group_api_id` | `string` | ID API du groupe d'abonnement
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`abort_type` | `null,`&nbsp;`string` | Type d'abandon. Pour la liste des valeurs, consultez [Types d'abandon](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Message de journal décrivant les détails de l'abandon (maximum 2 000 caractères)
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPABORTSHARED #USERSMESSAGESWHATSAPPABORTSHARED" }


### USERS_MESSAGES_WHATSAPP_CLICK_SHARED {#USERS_MESSAGES_WHATSAPP_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`user_id` | `string` | ID utilisateur Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`time` | `int` | Horodatage UNIX de l'événement
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID BSON du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`url` | `null,`&nbsp;`string` | URL sur laquelle l'utilisateur a cliqué
`short_url` | `null,`&nbsp;`string` | URL raccourcie ayant été cliquée
`user_agent` | `null,`&nbsp;`string` | Agent utilisateur sur lequel le signalement de courrier indésirable a eu lieu
`user_phone_number` | `null,`&nbsp;`string` | [PII] Numéro de téléphone de l'utilisateur à partir duquel le message a été reçu
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPCLICKSHARED #USERSMESSAGESWHATSAPPCLICKSHARED" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`time` | `int` | Horodatage Unix de l'événement
`to_phone_number` | `null,`&nbsp;`string` | [PII] Numéro de téléphone du destinataire
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`from_phone_number` | `null,`&nbsp;`string` | Numéro de téléphone à partir duquel le message WhatsApp a été envoyé
`app_group_id` | `null,`&nbsp;`string` | ID de l'espace de travail auquel cet utilisateur appartient
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`subscription_group_api_id` | `string` | ID API du groupe d'abonnement
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`flow_id` | `null,`&nbsp;`string` | ID unique du Flow dans le WhatsApp gestionnaire. Présent si l'utilisateur répond à un WhatsApp Flow.
`template_name` | `null,`&nbsp;`string` | [PII] Nom du modèle dans le WhatsApp gestionnaire. Présent en cas d'envoi d'un message de type Template
`message_id` | `null,`&nbsp;`string` | ID unique généré par Meta pour ce message
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPDELIVERYSHARED #USERSMESSAGESWHATSAPPDELIVERYSHARED" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`time` | `int` | Horodatage Unix de l'événement
`to_phone_number` | `null,`&nbsp;`string` | [PII] Numéro de téléphone du destinataire
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`from_phone_number` | `null,`&nbsp;`string` | Numéro de téléphone à partir duquel le message WhatsApp a été envoyé
`app_group_id` | `null,`&nbsp;`string` | ID de l'espace de travail auquel cet utilisateur appartient
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`subscription_group_api_id` | `string` | ID API du groupe d'abonnement
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`provider_error_code` | `null,`&nbsp;`string` | Code d'erreur de WhatsApp
`provider_error_title` | `null, `&nbsp;`string` | Titre de l'erreur de WhatsApp
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`message_id` | `null,`&nbsp;`string` | ID unique généré par Meta pour ce message
`template_name` | `null,`&nbsp;`string` | [PII] Nom du modèle dans le WhatsApp gestionnaire. Présent en cas d'envoi d'un message de type Template
`flow_id` | `null,`&nbsp;`string` | ID unique du Flow dans le WhatsApp gestionnaire. Présent si l'utilisateur répond à un WhatsApp Flow.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPFAILURESHARED #USERSMESSAGESWHATSAPPFAILURESHARED" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`time` | `int` | Horodatage Unix de l'événement
`user_phone_number` | `string` | [PII] Numéro de téléphone de l'utilisateur à partir duquel le message a été reçu
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`inbound_phone_number` | `string` | Numéro entrant auquel le message a été envoyé
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | ID de l'espace de travail auquel cet utilisateur appartient
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`subscription_group_api_id` | `string` | ID API du groupe d'abonnement
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`message_body` | `string` | Réponse de l'utilisateur
`quick_reply_text` | `string` | Texte du bouton appuyé par l'utilisateur
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | URL multimédias de l'utilisateur
`action` | `string` | Action effectuée en réponse à ce message. Par exemple, `Subscribed`, `Unsubscribed` ou `None`.
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
`catalog_id` | `null,`&nbsp;`string` | ID du catalogue d'un produit si un produit est référencé dans le message entrant. Vide dans le cas contraire.
`product_id` | `null,`&nbsp;`string` | ID du produit acheté
`flow_id` | `null,`&nbsp;`string` | ID unique du Flow dans le WhatsApp gestionnaire. Présent si l'utilisateur répond à un WhatsApp Flow.
`flow_response_json` | `null,`&nbsp;`string` | [PII] Valeurs du formulaire avec lesquelles l'utilisateur a répondu. Présent si l'utilisateur répond à un WhatsApp Flow.
`message_id` | `null,`&nbsp;`string` | ID unique généré par Meta pour ce message
`in_reply_to` | `null,`&nbsp;`string` | Le message_id du message auquel ce message répondait
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPINBOUNDRECEIVESHARED #USERSMESSAGESWHATSAPPINBOUNDRECEIVESHARED" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`time` | `int` | Horodatage Unix de l'événement
`to_phone_number` | `null,`&nbsp;`string` | [PII] Numéro de téléphone du destinataire
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`from_phone_number` | `null,`&nbsp;`string` | Numéro de téléphone à partir duquel le message WhatsApp a été envoyé
`app_group_id` | `null,`&nbsp;`string` | ID de l'espace de travail auquel cet utilisateur appartient
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`subscription_group_api_id` | `string` | ID API du groupe d'abonnement
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`template_name` | `null,`&nbsp;`string` | [PII] Nom du modèle dans le WhatsApp gestionnaire. Présent en cas d'envoi d'un message de type Template
`message_id` | `null,`&nbsp;`string` | ID unique généré par Meta pour ce message
`flow_id` | `null,`&nbsp;`string` | ID unique du Flow dans le WhatsApp gestionnaire. Présent si l'utilisateur répond à un WhatsApp Flow.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPREADSHARED #USERSMESSAGESWHATSAPPREADSHARED" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique global de cet événement
`time` | `int` | Horodatage Unix de l'événement
`to_phone_number` | `null,`&nbsp;`string`	| [PII] Numéro de téléphone du destinataire
`user_id` | `string` | ID Braze de l'utilisateur ayant effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID utilisateur externe de l'utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` lié à cet utilisateur si l'utilisateur est anonyme
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`from_phone_number` | `null,`&nbsp;`string` | Numéro de téléphone à partir duquel le message WhatsApp a été envoyé
`app_group_id` | `null,`&nbsp;`string` | ID de l'espace de travail auquel cet utilisateur appartient
`app_group_api_id` | `null,`&nbsp;`string` | ID API de l'espace de travail auquel cet utilisateur appartient
`subscription_group_api_id` | `string` | ID API du groupe d'abonnement
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message reçue par cet utilisateur
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante du Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape du Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`message_extras` | `null,`&nbsp;`string` | [PII] Chaîne JSON des paires clé-valeur balisées lors du rendu Liquid
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
`send_id` | `null,`&nbsp;`string` | ID d'envoi du message auquel ce message appartient
`flow_id` | `null,`&nbsp;`string` | ID unique du Flow dans le WhatsApp gestionnaire. Présent si l'utilisateur répond à un WhatsApp Flow.
`template_name` | `null,`&nbsp;`string` | [PII] Nom du modèle dans le WhatsApp gestionnaire. Présent en cas d'envoi d'un message de type Template
`message_id` | `null,`&nbsp;`string` | ID unique généré par Meta pour ce message
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPSENDSHARED #USERSMESSAGESWHATSAPPSENDSHARED" }

### USERS_MESSAGES_WHATSAPP_RETRY_SHARED {#USERS_MESSAGES_WHATSAPP_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Cet événement se produit lorsqu'un message est dépriorisé ou soumis à une limitation de fréquence, puis réessayé ultérieurement dans la fenêtre de réessai configurée.

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau global pour cet événement
`user_id` | `string` | [PII] ID utilisateur Braze de l'utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,`&nbsp;`string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'applications auquel cet utilisateur appartient
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`to_phone_number` | `null,`&nbsp;`string` | [PII] Numéro de téléphone de l'utilisateur recevant le message au format e.164
`device_id` | `null,`&nbsp;`string` | ID de l'appareil sur lequel l'événement s'est produit
`timezone` | `null,`&nbsp;`string` | Fuseau horaire de l'utilisateur
`subscription_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d'abonnement
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message que cet utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID BSON du Canvas auquel cet événement appartient
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel cet événement appartient
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l'étape Canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variante de message de l'étape Canvas que cet utilisateur a reçue
`dispatch_id` | `null,`&nbsp;`string` | ID de l'envoi auquel ce message appartient
`retry_type` | `null,`&nbsp;`string` | Type de réessai
`retry_log` | `null,`&nbsp;`string` | Message de log décrivant les détails du réessai
`sf_created_at` | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été collecté par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPRETRYSHARED #USERSMESSAGESWHATSAPPRETRYSHARED" }

## Utilisateurs {#users}

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| Champ                       | Type                     | Description                                                                        |
| --------------------------- | ------------------------ | ---------------------------------------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | ID unique global pour cet événement                                                |
| `app_group_id`              | `string`,&nbsp;`null`    | ID Braze de l'espace de travail auquel appartient cet utilisateur                  |
| `app_group_api_id`          | `string`,&nbsp;`null`    | ID API de l'espace de travail auquel appartient cet utilisateur                    |
| `user_id`                   | `string`,&nbsp;`null`    | ID Braze de l'utilisateur ayant effectué cet événement                             |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] ID externe de l'utilisateur                                                  |
| `time`                      | `int`,&nbsp;`null`       | Horodatage Unix auquel l'événement s'est produit                                   |
| `random_bucket_number`      | `int`,&nbsp;`null`       | Numéro de compartiment aléatoire actuellement attribué à l'utilisateur             |
| `prev_random_bucket_number` | `int`,&nbsp;`null`       | Numéro de compartiment aléatoire précédemment attribué à l'utilisateur             |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSRANDOMBUCKETNUMBERUPDATESHARED #USERSRANDOMBUCKETNUMBERUPDATESHARED" }

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| Champ              | Type                     | Description                                                                          |
| ------------------ | ------------------------ | ------------------------------------------------------------------------------------ |
| `id`               | `string`,&nbsp;`null`    | ID unique global pour cet événement                                                  |
| `user_id`          | `string`,&nbsp;`null`    | ID Braze de l'utilisateur supprimé                                                   |
| `app_group_id`     | `string`,&nbsp;`null`    | ID Braze de l'espace de travail auquel appartient cet utilisateur                    |
| `app_group_api_id` | `string`,&nbsp;`null`    | ID API de l'espace de travail auquel appartient cet utilisateur                      |
| `time`             | `int`,&nbsp;`null`       | Horodatage Unix auquel la demande de suppression de l'utilisateur a été traitée      |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSUSERDELETEREQUESTSHARED #USERSUSERDELETEREQUESTSHARED" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| Champ              | Type                     | Description                                                                                                   |
| ------------------ | ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | ID unique global pour cet événement                                                                           |
| `user_id`          | `string`,&nbsp;`null`    | ID Braze de l'utilisateur devenu orphelin                                                                     |
| `external_user_id` | `string`,&nbsp;`null`    | [PII] ID externe de l'utilisateur                                                                             |
| `device_id`        | `string`,&nbsp;`null`    | ID de l'appareil associé à cet utilisateur, si l'utilisateur est anonyme                                      |
| `app_group_id`     | `string`,&nbsp;`null`    | ID Braze de l'espace de travail auquel appartient cet utilisateur                                             |
| `app_group_api_id` | `string`,&nbsp;`null`    | ID API de l'espace de travail auquel appartient cet utilisateur                                               |
| `app_api_id`       | `string`,&nbsp;`null`    | ID API de l'application à laquelle appartenait l'utilisateur orphelin                                         |
| `time`             | `int`,&nbsp;`null`       | Horodatage Unix auquel l'utilisateur est devenu orphelin                                                      |
| `orphaned_by_id`   | `string`,&nbsp;`null`    | ID Braze de l'utilisateur dont le profil a été fusionné avec celui de l'utilisateur orphelin                   |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | Date à laquelle cet événement a été récupéré par le Snowpipe                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSUSERORPHANSHARED #USERSUSERORPHANSHARED" }

## Instantanés {#snapshots}

{% alert note %}
Les tables d'instantanés sont disponibles uniquement dans le partage de données Snowflake.
{% endalert %}

### SNAPSHOTS_APP_SHARED {#SNAPSHOTS_APP_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau global pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_group_id` | `string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`api_id` | `string` | ID API de l'application
`name` | `null,`&nbsp;`string` | Nom de l'application
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSAPPSHARED #SNAPSHOTSAPPSHARED" }

### SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED {#SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau global pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_group_id` | `string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`api_id` | `string` | ID API de la variante de message de Campaign
`name` | `null,`&nbsp;`string` | Nom de la variante de message de Campaign
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSCAMPAIGNMESSAGEVARIATIONSHARED #SNAPSHOTSCAMPAIGNMESSAGEVARIATIONSHARED" }

### SNAPSHOTS_CANVAS_FLOW_STEP_SHARED {#SNAPSHOTS_CANVAS_FLOW_STEP_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau global pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_group_id` | `string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`type` | `null,`&nbsp;`string` | Type de l'étape Canvas Flow
`api_step_id` | `string` | ID API de l'étape Canvas
`experiment_splits` | `null,`&nbsp;`string` | Répartitions d'expérience pour l'étape
`conversion_behaviors` | `null,`&nbsp;`string` | Comportements de conversion pour l'étape
`name` | `null,`&nbsp;`string` | Nom de l'étape Canvas Flow
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSCANVASFLOWSTEPSHARED #SNAPSHOTSCANVASFLOWSTEPSHARED" }

### SNAPSHOTS_CANVAS_STEP_SHARED {#SNAPSHOTS_CANVAS_STEP_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau global pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_group_id` | `string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`api_id` | `string` | ID API de l'étape Canvas
`name` | `null,`&nbsp;`string` | Nom de l'étape Canvas
`actions` | `null,`&nbsp;`string` | Actions pour l'étape Canvas
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSCANVASSTEPSHARED #SNAPSHOTSCANVASSTEPSHARED" }

### SNAPSHOTS_CANVAS_VARIATION_SHARED {#SNAPSHOTS_CANVAS_VARIATION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau global pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_group_id` | `string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`api_id` | `string` | ID API de la variante Canvas
`name` | `null,`&nbsp;`string` | Nom de la variante Canvas
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSCANVASVARIATIONSHARED #SNAPSHOTSCANVASVARIATIONSHARED" }

### SNAPSHOTS_EXPERIMENT_STEP_SHARED {#SNAPSHOTS_EXPERIMENT_STEP_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau global pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_group_id` | `string` | ID BSON du groupe d'applications auquel cet utilisateur appartient
`type` | `null,`&nbsp;`string` | Type de l'étape d'expérience
`api_step_id` | `string` | ID API de l'étape d'expérience
`experiment_splits` | `null,`&nbsp;`string` | Répartitions d'expérience pour l'étape
`conversion_behaviors` | `null,`&nbsp;`string` | Comportements de conversion pour l'étape
`name` | `null,`&nbsp;`string` | Nom de l'étape d'expérience
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSEXPERIMENTSTEPSHARED #SNAPSHOTSEXPERIMENTSTEPSHARED" }

## Types d'abandon {#abort-types}

{% include currents/abort_types_reference.md combined_content_rendering=true %}