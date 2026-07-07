---
nav_title: FAQ
article_title: FAQ sur Currents
page_order: 4
page_type: reference
description: "Cet article aborde certaines des questions les plus fréquemment posées lors de la mise en place de Braze Currents."
tool: Currents
---

# Questions fréquemment posées {#frequently-asked-questions}

> Cette page fournit des réponses à certaines questions fréquemment posées au sujet de Currents.

## Puis-je exporter les données d'une campagne ou d'un Canvas pour une période spécifique ? {#can-i-export-campaign-or-canvas-data-for-a-specific-date-window}

Pour récupérer les indicateurs d'une campagne ou d'un Canvas sur une période définie, utilisez l'une des approches suivantes :

- Soumettez une [demande produit](https://portal.braze.com/) pour des exports alignés sur des dates lorsque vous avez besoin de rapports de type tableau de bord en dehors des fenêtres API standard.
- Appelez les endpoints d'[analyse de campagne]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) ou d'[analyse de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) avec les paramètres `ending_at` et `length` (ou utilisez [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) et [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics)) pour obtenir des données de séries temporelles.
- Diffusez les événements vers votre entrepôt de données avec [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) lorsque vous avez besoin de données d'engagement lié aux messages en continu et interrogeables dans Amazon S3, Azure Blob Storage ou une autre destination prise en charge.

## Comment modifier une intégration Currents en production ? {#how-do-i-edit-a-live-currents-integration}

Pour modifier un connecteur Currents en production, ouvrez l'intégration et sélectionnez **Modifier**. Sans **Modifier**, l'interface de l'intégration reste en lecture seule et vous ne pouvez pas modifier les paramètres du connecteur à partir des icônes seules.

## Comment Braze gère-t-il les fichiers Avro dans Azure Blob Storage après le téléchargement ? {#how-does-braze-handle-azure-blob-storage-avro-files-after-upload}

Braze ne modifie pas les fichiers Avro dans [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents) une fois le téléchargement terminé. Azure peut bloquer la suppression d'un blob tant qu'un téléchargement est encore en cours.

## Comment obtenir des données historiques ? {#how-do-i-get-historical-data}

Currents est un flux de données en continu et en temps réel, ce qui signifie que les événements ne peuvent pas être rejoués. Toutefois, vous pouvez stocker les données Currents dans un entrepôt de données tel qu'[Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3) ou [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents), afin de pouvoir agir sur les événements passés comme bon vous semble. Les données sont conservées pendant 30 jours, mais pour obtenir des données plus anciennes, vous pouvez interroger [Snowflake]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/s3_to_snowflake).

## Pourquoi Currents fournit-il des données au format Avro et non JSON ? {#why-does-currents-output-data-in-the-avro-format-not-json}

Avro, contrairement à JSON qui ne repose pas sur un schéma, supporte nativement l'évolution des schémas. Vous bénéficierez également de la possibilité d'envoyer des fichiers Avro en utilisant moins de bande passante et en économisant de l'espace de stockage, car Avro est hautement compressible.

## Comment Braze gère-t-il la surcharge des fichiers ? {#how-does-braze-handle-file-overhead}

Nous mettons en place un processus ETL (extraire, transformer, charger) qui vous permet d'extraire de grandes quantités de données d'une base de données pour les placer et les stocker dans une autre.

## Où dois-je stocker ces données pour pouvoir les interroger ? {#where-should-i-store-this-data-for-querying}

Braze est partenaire de plusieurs entrepôts de données dans lesquels vous pouvez stocker vos données pour les interroger. Nous vous recommandons d'utiliser :
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents).

## Quelle est la fiabilité des données Currents ? {#how-reliable-is-currents-data}

Currents garantit une livraison « au moins une fois » (at-least-once), ce qui signifie que des événements en double peuvent occasionnellement être écrits dans votre compartiment de stockage. Si votre cas d'usage nécessite une livraison exactement une fois, vous pouvez dédupliquer les événements à l'aide du champ d'identifiant unique (`id`) envoyé avec chaque événement. Pour plus de détails, consultez la section [Sémantique de livraison des événements]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics).

## À quelle fréquence les données sont-elles synchronisées avec Currents ? {#how-often-is-data-synced-to-currents}

Les données sont diffusées en continu. Braze envoie un lot d'événements chaque fois qu'un lot complet est prêt, ou toutes les 5 minutes, selon ce qui se produit en premier. Pour les connecteurs à fort volume, les données arrivent quasiment en temps réel. Pour les connecteurs à faible volume, comptez un délai de 5 à 30 minutes. Pour plus de détails, consultez la section [Seuil d'écriture Avro]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics#avro-write-threshold).

{% alert note %}
Si un appareil n'est pas connecté à Internet, la création de l'événement peut être retardée. C'est le cas le plus fréquent pour les événements de messages in-app, car les messages in-app peuvent être déclenchés hors ligne.
{% endalert %}

## Comment savoir quels événements sont disponibles pour Currents ? {#how-do-i-find-which-events-are-available-for-currents}

Pour obtenir la liste complète des événements enregistrés par Currents, consultez les glossaires des [événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) et des [événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events). Vous pouvez filtrer ces glossaires par type d'événement (envois, réceptions ou ouvertures, par exemple).

## Pourquoi les comptages d'événements Currents ne correspondent-ils pas aux indicateurs de mon tableau de bord ou de mes rapports d'engagement ? {#why-do-my-currents-event-counts-not-match-my-dashboard-or-engagement-report-metrics}

Currents et le tableau de bord de Braze calculent certains indicateurs différemment, de sorte que des correspondances exactes entre les événements Currents et les indicateurs du tableau de bord ne sont pas attendues.

**Clics uniques :** Pour les e-mails, le tableau de bord suit les clics uniques sur une période de sept jours et les mesure par `dispatch_id`. Currents enregistre chaque événement de clic brut. Pour aligner les comptages de clics uniques basés sur Currents avec les indicateurs du tableau de bord, filtrez les événements pour lesquels `is_unique` est `true`.

**Désabonnements :** L'indicateur *Désabonnement* du tableau de bord reflète les clics sur le lien de désabonnement standard de Braze. Les pages de désabonnement personnalisées n'incrémentent pas cet indicateur, sauf si vous mettez à jour l'utilisateur via l'API. L'événement Currents `users.messages.email.Unsubscribe` est un événement de clic spécialisé qui se déclenche lorsqu'un utilisateur clique sur un lien de désabonnement dans le corps ou le pied de page de l'e-mail, ou via l'en-tête list-unsubscribe. Il ne représente pas chaque changement d'état d'abonnement aux e-mails.

**Horodatages et fuseaux horaires :** Tous les horodatages Currents sont en UTC. Les indicateurs du tableau de bord suivent le fuseau horaire de votre entreprise. L'agrégation des données Currents par jour calendaire sans conversion vers le fuseau horaire de votre entreprise peut entraîner un décalage des comptages dans des tranches de dates différentes de celles affichées dans le tableau de bord.

**Événements en double :** Currents fournit une livraison « au moins une fois », ce qui signifie que des événements en double peuvent occasionnellement être écrits. Dédupliquez à l'aide du champ unique `id` de chaque événement avant de comparer les totaux aux indicateurs du tableau de bord.

## Pourquoi l'`external_user_id` (schéma Braze : `external_id`) de mon événement d'ouverture ou de clic d'e-mail dans Currents diffère-t-il du profil utilisateur dans le tableau de bord de Braze ? {#why-does-the-external_user_id-braze-schema-external_id-in-my-currents-email-open-or-click-event-differ-from-the-user-profile-in-the-braze-dashboard}

- **Dans le tableau de bord de Braze :** Lorsqu'un utilisateur associé à une adresse e-mail ouvre ou clique sur un e-mail, tous les profils utilisateur partageant cette adresse e-mail sont marqués comme ayant ouvert ou cliqué sur cet e-mail. Pour en savoir plus, consultez [Que se passe-t-il lorsqu'un e-mail est envoyé et que plusieurs profils partagent la même adresse e-mail ?]({{site.baseurl}}/user_guide/channels/email/faq#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address).
- **Dans Currents :** Cette même ouverture ou ce même clic est stocké sur un seul profil. Braze l'attribue au profil qui a été initialement ciblé pour l'envoi, si ce profil partage toujours l'adresse e-mail. Sinon, Braze l'attribue à un profil sélectionné aléatoirement parmi ceux qui partagent cette adresse e-mail.

Pour cette raison, la valeur `external_user_id` (nommée `external_id` dans la table de mappage du schéma Braze) d'un événement d'ouverture ou de clic d'e-mail dans Currents peut ne pas correspondre au profil utilisateur attendu lorsque vous comparez Currents au tableau de bord de Braze.

## Tous les événements d'envoi sont-ils enregistrés dans Currents ? {#are-all-send-events-logged-to-currents}

Tous les événements sont enregistrés dans Currents. Il n'existe aucun scénario dans lequel un événement serait intentionnellement supprimé du flux Currents.

## Les données peuvent-elles être corrompues dans Currents ? {#can-data-be-corrupted-in-currents}

Dans des conditions normales, les données Currents ne sont pas corrompues. Bien qu'un problème rare soit toujours possible, il n'existe aucune condition connue dans laquelle les données seraient systématiquement corrompues.

## Pourquoi est-ce que je vois des données d'événements personnalisés datant d'avant la mise en place de mon intégration Currents ? {#why-do-i-see-custom-event-data-dated-before-my-currents-integration-was-set-up}

Braze ne remplit pas rétroactivement les événements dans Currents. Cependant, les événements personnalisés peuvent être enregistrés avec un horodatage passé (par exemple, si un appareil était hors ligne au moment de l'événement et s'est synchronisé plus tard). Dans ces cas, l'horodatage de l'événement reflète le moment où l'événement s'est réellement produit, ce qui peut être antérieur à la configuration de l'intégration Currents.

## Quels identifiants utilisateur sont inclus dans les événements Currents ? {#what-user-identifiers-are-included-in-currents-events}

Les événements d'engagement lié aux messages (envois, ouvertures, clics, etc.) incluent l'ID utilisateur Braze (`user_id`) et, lorsqu'il est présent sur le profil, l'identifiant externe (`external_user_id` dans les payloads d'événements, nommé `external_id` dans la table de mappage du schéma Braze). Certains événements d'engagement lié aux e-mails incluent également `email_address`. Les attributs personnalisés ne sont pas inclus.

Si vous envoyez les données Currents vers un entrepôt de données ou un CRM et que vous devez effectuer une jointure sur les données de profil, réalisez cette jointure dans votre système en aval en utilisant `user_id` ou `external_user_id`.

## Puis-je inclure des attributs personnalisés dans les événements d'envoi Currents ? {#can-i-include-custom-attributes-in-currents-send-events}

Non. Currents n'inclut pas d'attributs personnalisés dans les événements d'envoi. Currents enregistre les événements personnalisés et les événements d'engagement lié aux messages. Pour obtenir la liste complète des champs disponibles, consultez les [glossaires des événements]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary).

## Currents inclut-il les étiquettes de campagne ou de Canvas, ou les paires clé-valeur ? {#does-currents-include-campaign-or-canvas-tags-or-key-value-pairs}

Non. Currents n'inclut pas les étiquettes de campagne ou de Canvas, ni les paires clé-valeur au niveau du message. Pour récupérer les données d'étiquettes, utilisez l'[API REST d'exportation]({{site.baseurl}}/api/endpoints/export). En guise de solution de contournement, vous pouvez également utiliser un canal webhook dans une campagne pour envoyer les données d'étiquettes ou de paires clé-valeur vers votre propre endpoint, en utilisant [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) pour modéliser les valeurs.

## Comment Braze informe-t-il ses clients des modifications apportées à Currents ? {#how-does-braze-notify-customers-of-changes-to-currents}

Dans les rares cas où des modifications majeures sont apportées, Braze envoie un e-mail anticipé au contact de toute intégration active ainsi qu'à tous les administrateurs disposant d'intégrations Currents actives et ayant utilisé le tableau de bord au cours des 30 derniers jours. Pour les modifications non majeures, comme de nouveaux événements ou de nouveaux champs sur un événement existant, Braze n'envoie pas de notification. Vous pouvez consulter le [journal des modifications de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) pour connaître les dernières modifications.

## De combien d'espace de stockage ai-je besoin pour les données Currents ? {#how-much-storage-do-i-need-for-currents-data}

Les besoins en stockage dépendent de votre volume d'événements et des types d'événements que vous exportez. Braze fournit des [exemples d'événements au format Avro](https://github.com/appboy/currents-examples/tree/master/sample-data) que vous pouvez utiliser pour estimer la taille des fichiers correspondant à votre cas d'usage.

## Pourquoi le nom de la campagne ou le nom de l'étape du Canvas est-il `NULL` dans mes données Currents ? {#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data}

Lorsque vous créez une nouvelle campagne ou un nouveau Canvas, le nom peut mettre un certain temps à se propager dans tous les systèmes Braze. Les événements envoyés via Currents pendant cette période peuvent contenir `NULL` dans les champs de nom (tels que `campaign_name` ou `canvas_step_name`). C'est également le comportement attendu si le nom a été modifié peu avant l'enregistrement des événements. Pour éviter cela, attendez un moment après la création ou le renommage d'une campagne ou d'une étape du Canvas avant de procéder à l'envoi.

## Pourquoi les événements de fin de session sont-ils retardés ou absents dans Currents ? {#why-are-session-end-events-delayed-or-missing-in-currents}

Les événements de fin de session suivent le calendrier normal de téléchargement du SDK. Le SDK Braze met en cache les données de session localement et les envoie périodiquement en fonction de la qualité du réseau — par exemple, environ toutes les 10 secondes sur une connexion stable. Tant que le SDK n'a pas téléchargé l'événement, celui-ci n'apparaît pas dans Currents.

Si un utilisateur force la fermeture de l'application ou passe hors ligne avant le prochain envoi, l'événement de fin de session peut arriver en retard ou ne pas arriver du tout. Sur iOS, les événements de fin de session ne sont souvent envoyés que lorsque l'application est rouverte, car le SDK ne peut pas transmettre de données lorsque l'application est en arrière-plan.

Lorsque vous avez besoin de limites de session plus réactives dans Currents, appelez `requestImmediateDataFlush()` à des moments clés du cycle de vie, par exemple lorsque l'application passe en arrière-plan ou revient au premier plan. Pour en savoir plus, consultez [Téléchargement et téléversement de données]({{site.baseurl}}/developer_guide/getting_started/sdk_overview#data-upload-and-download) et [Les horodatages de fin et de début de session sont similaires (iOS)]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log#session-end-and-session-start-have-similar-timestamps-ios).

## Que se passe-t-il si mon compartiment de stockage est indisponible lorsque Currents tente d'écrire des données ? {#what-happens-if-my-storage-bucket-is-unavailable-when-currents-tries-to-write-data}

Si votre compartiment de stockage est indisponible au moment du transfert de données, ces données sont perdues. Braze n'est pas en mesure de renvoyer rétroactivement les événements qui n'ont pas été livrés avec succès. Pour éviter toute perte de données, assurez-vous que votre compartiment de stockage est disponible et correctement configuré en permanence.

## Pourquoi le message « You do not have any remaining Customer Behavior Events entitlements » s'affiche-t-il lorsque je modifie mon intégration Currents ? {#why-do-i-see-you-do-not-have-any-remaining-customer-behavior-events-entitlements-when-editing-my-currents-integration}

Ce message peut apparaître lorsque vous mettez à jour une intégration Currents existante et que votre espace de travail a atteint sa limite de droits pour les événements de comportement client. Contactez votre gestionnaire de compte Braze pour demander une extension de droits ou ajuster votre configuration.

## À quelle fréquence la version de Currents dans le chemin de stockage change-t-elle ? {#how-often-does-the-currents-version-in-the-storage-path-change}

Le segment `version=<currents_version>` dans le chemin de stockage est incrémenté à chaque nouvelle version de Currents, selon une cadence mensuelle (par exemple, `version=6` vers `version=7`). Nous vous recommandons de lire les fichiers de manière récursive à partir du chemin racine plutôt que de coder en dur un segment de version spécifique, afin que votre pipeline récupère automatiquement les données après un changement de version. Pour plus de détails sur le format du chemin, consultez la section [Sémantique de livraison des événements]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics). Pour un historique des modifications par version, consultez le [journal des modifications de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs).

## Pourquoi `campaign_id` ou `canvas_id` sont-ils absents d'un événement d'engagement lié aux messages ? {#why-are-campaign_id-or-canvas_id-missing-from-a-message-engagement-event}

Selon le type d'événement et le contexte, un événement d'engagement lié aux messages peut ne pas être associé à une campagne ou une étape du Canvas spécifique. Dans ces cas, les champs `campaign_id`, `canvas_id` et les champs de nom associés peuvent être omis du payload de l'événement. Si vous ne voyez pas ces champs pour un événement donné, vérifiez si ce type d'événement et ce contexte incluent normalement les identifiants de campagne ou de Canvas.

## Pourquoi les horodatages Currents sont-ils limités à la précision de la seconde ? {#why-are-currents-timestamps-limited-to-second-precision}

Le champ `time` dans les événements Currents est stocké sous forme d'entier 32 bits et est donc limité à la précision de la seconde. Certains événements incluent également un champ d'horodatage distinct en 64 bits avec une précision à la milliseconde ; consultez le [glossaire des événements]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary) pour connaître les champs disponibles pour chaque type d'événement.

## Pourquoi l'événement `users.canvas.Conversion` de Currents a-t-il un horodatage différent de celui du Canvas ? {#why-does-the-userscanvasconversion-event-from-currents-have-a-different-time-than-the-canvas}

L'horodatage de l'événement `users.canvas.Conversion` dans Currents reflète la fenêtre de conversion totale — la durée du Canvas plus la date limite de conversion — mesurée à partir de l'entrée dans le Canvas.

## Que se passe-t-il lorsque des rapports d'engagement sont envoyés vers S3 ? {#what-happens-when-engagement-reports-are-sent-to-s3}

Si des identifiants S3 sont configurés pour l'exportation de données mais pas pour Currents, Braze télécharge les rapports d'engagement vers le compartiment S3 spécifié. L'utilisateur indiqué dans le champ **Send Report To** reçoit un e-mail contenant un lien vers le rapport dans S3.

## Les données d'utilisateurs anonymes peuvent-elles être envoyées à Amplitude via Braze Currents ? {#can-anonymous-user-data-be-sent-to-amplitude-through-braze-currents}

Les données d'utilisateurs anonymes, identifiées par `device_id`, peuvent être envoyées à Amplitude via Currents. Cela nécessite l'activation de la fonctionnalité par votre équipe de compte Braze.

## Comment les impressions du groupe de contrôle pour les Content Cards et les messages in-app sont-elles enregistrées dans Currents ? {#how-are-control-group-impressions-for-content-cards-and-in-app-messages-logged-in-currents}

Lorsqu'un utilisateur est affecté à un groupe de contrôle pour une campagne de Content Cards ou de messages in-app, Currents émet un événement `users.campaigns.EnrollInControl` au lieu d'un événement d'impression.

## Que se passe-t-il lorsque vous ciblez un utilisateur inexistant via l'API ? {#what-happens-when-you-target-a-non-existent-user-through-the-api}

Lorsque vous ciblez un utilisateur qui n'existe pas, l'API renvoie une réponse `200`, mais l'envoi est annulé avec le résultat « Unknown external ID ». Aucun événement Currents n'est généré pour cet envoi. Notez que le paramètre `send_to_existing_only` est défini par défaut sur `true`, de sorte que les envois vers des utilisateurs inconnus sont silencieusement ignorés, sauf si vous le définissez explicitement sur `false`.