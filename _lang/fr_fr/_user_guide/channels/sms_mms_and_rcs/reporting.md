---
nav_title: "Rapports"
article_title: "Rapports"
page_order: 21
description: "Cet article de référence présente les indicateurs SMS, MMS et RCS utilisés dans Braze, ainsi que la manière de les consulter dans vos campagnes SMS, MMS et RCS."
alias: /sms_mms_rcs_reporting/
page_type: reference
tool:
  - Reports
channel:
  - SMS
  - MMS
  - RCS

---

# Rapports pour les SMS, MMS et RCS {#reporting-for-sms-mms-and-rcs}

> Cet article de référence présente les indicateurs SMS, MMS et RCS utilisés dans Braze, ainsi que la manière de les consulter dans vos campagnes SMS, MMS et RCS.

{% multi_lang_include analytics/campaign_analytics.md channel="SMS" %}

## Suivre les abonnements et désabonnements SMS {#track-sms-opt-ins-and-opt-outs}

Vous pouvez suivre les abonnements et désabonnements SMS à l'aide des méthodes suivantes :

| Méthode | Description |
|--------|-------------|
| Segmenteur | Le segmenteur affiche le nombre d'utilisateurs dans un [groupe d'abonnement]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#subscription-group) spécifique. Il ne déduplique pas par numéro de téléphone : si plusieurs utilisateurs partagent le même numéro de téléphone, chaque instance est comptée séparément. |
| Série temporelle du groupe d'abonnement | Fournit un instantané quotidien des abonnements pour les e-mails et les numéros de téléphone. La série temporelle comptabilise les abonnements, les désabonnements et les réabonnements. Par exemple, si un utilisateur s'abonne, se désabonne, puis se réabonne, il est compté comme un seul utilisateur abonné. |
| Currents | Utilisez Currents pour exporter les [événements d'abonnement et d'engagement]({{site.baseurl}}/message_events_glossary) pour vos propres rapports. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Suivre les abonnements et désabonnements SMS" }

{% alert note %}
Les statistiques _Abonnement_ et _Désabonnement_ dans le panneau **SMS/MMS/RCS Performance** reflètent les utilisateurs qui s'abonnent ou se désabonnent via des mots-clés entrants (par exemple, en envoyant « START » pour s'abonner ou « STOP » pour se désabonner). Ces chiffres sont généralement inférieurs à ceux affichés dans le segmenteur, car ils comptent le nombre de fois où ces mots-clés ont été envoyés par SMS, et non le nombre total d'utilisateurs abonnés aux SMS.
{% endalert %}

### Suivre les désabonnements SMS au niveau de la campagne {#track-sms-campaign-opt-outs}

Suivez les désabonnements SMS au niveau de la campagne en utilisant la table de réception entrante plutôt que la table de changement d'état du groupe d'abonnement. Par exemple, dans le [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder) ou votre entrepôt de données, vous pouvez exécuter une requête qui référence la table `USERS_MESSAGES_SMS_INBOUNDRECEIVE` ou [`USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED`]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED).

Cet exemple de requête référence la table `USERS_MESSAGES_SMS_INBOUNDRECEIVE` :

```sql
SELECT *
FROM USERS_MESSAGES_SMS_INBOUNDRECEIVE
WHERE app_group_id = 'app-group-id'
AND subscription_group_api_id = 'subscription_group_api_id'
AND action = 'Unsubscribed'
AND (campaign_id IS NOT NULL OR canvas_id IS NOT NULL);
```

Cette requête renvoie les utilisateurs qui se sont désabonnés des communications SMS pour l'espace de travail et le groupe d'abonnement donnés, filtrés pour ne retenir que ceux associés à des campagnes ou des Canvas.

### Moment du désabonnement {#opt-out-timing}

Les événements de mots-clés et de messages entrants dans Currents ou votre entrepôt de données, tels que les horodatages sur [`users.messages.sms.InboundReceive`]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) ou les événements de changement d'état du groupe d'abonnement, constituent la source de référence pour savoir quand Braze a enregistré le désabonnement.

{% alert note %}
Les horodatages des événements reflètent le moment où Braze a reçu ou traité le message entrant, et pas nécessairement le moment où l'utilisateur a envoyé le SMS ou celui où un opérateur ou un fournisseur SMS l'a reçu. Si votre analyse considère les désabonnements comme le moment où Braze a traité le parcours de désabonnement entrant, ces horodatages correspondent à cette définition.
{% endalert %}

Le profil utilisateur affiche l'état d'abonnement actuel, mais ne fait pas nécessairement apparaître un champ unique « SMS désabonné le » à moins que vous ne définissiez un [attribut personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes) ou un mécanisme similaire lors du traitement des désabonnements.

## Frais appliqués aux résultats d'envoi SMS {#charges-applied-to-sms-sending-outcomes}

Ce tableau reflète la facturation de Braze, et non celle de votre fournisseur. Les résultats non facturés par Braze peuvent être facturés par votre fournisseur.

| Résultat | Définition | Facturé par Braze |
|--------|------------|--------|
| Envoyé | Une campagne ou une étape du Canvas a été lancée ou déclenchée, et un payload SMS a été envoyé au fournisseur SMS. | Aucun frais |
| Échec de distribution | Le payload SMS n'a pas pu être envoyé au fournisseur SMS. Cela peut se produire en raison de files d'attente saturées, de comptes suspendus ou d'erreurs média (dans le cas des MMS). | Aucun frais |
| Distribué | Le fournisseur SMS a reçu une confirmation de distribution du message de la part de l'opérateur en amont (et, lorsque disponible, de l'appareil de destination). | Facturé |
| Rejeté | Le fournisseur SMS a reçu un accusé de rejet indiquant que le message n'a pas été distribué. Cela peut se produire pour plusieurs raisons, notamment le filtrage de contenu par l'opérateur ou l'indisponibilité de l'appareil de destination. | Facturé |
| Envoyé à l'opérateur | {% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} | Des frais peuvent s'appliquer en fonction des résultats d'envoi de chaque message |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Frais appliqués aux résultats d'envoi SMS" }

## Rapprocher les *rejets* avec Snowflake ou Currents {#reconcile-rejections-with-snowflake-or-currents}

L'indicateur *Rejets* dans le tableau de bord est un décompte agrégé au niveau de l'espace de travail. Il ne s'agit pas d'un export ligne par ligne, ce qui signifie que vous ne pouvez pas toujours faire correspondre chaque rejet à une ligne unique dans Snowflake ou à un événement `users.messages.sms.Rejection` unique dans Currents. Par exemple, si le profil utilisateur a été supprimé avant que Braze n'ait terminé le traitement du rejet pour l'export vers l'entrepôt de données, ce rejet n'apparaît pas dans votre table `USERS_MESSAGES_SMS_REJECTION_SHARED` ni dans le payload Currents, alors que les rapports SMS agrégés peuvent toujours refléter le résultat. Pour en savoir plus, consultez la [référence des tables SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#sms-message-events-and-deleted-user-profiles) et les [événements de rejet SMS]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#sms-rejection-events) dans le glossaire des événements Currents.