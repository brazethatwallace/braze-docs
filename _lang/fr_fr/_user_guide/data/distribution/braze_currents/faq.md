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

## Puis-je exporter les données d'une Campaign ou d'un Canvas pour une période spécifique ? {#can-i-export-campaign-or-canvas-data-for-a-specific-date-window}

Pour récupérer les indicateurs d'une Campaign ou d'un Canvas sur une plage de dates définie, utilisez l'une des approches suivantes :

- {% multi_lang_include product_feedback_cta.md context="gap" feature="date-aligned campaign or Canvas exports for dashboard-style reporting outside standard API windows" %}
- Appelez les endpoints [d'analyse de Campaign]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) ou [d'analyse de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) avec les paramètres `ending_at` et `length` (ou utilisez [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) et [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics)) pour obtenir des données de séries temporelles.
- Diffusez les événements vers votre entrepôt de données avec [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) lorsque vous avez besoin de données d'engagement de messages continues et interrogeables dans Amazon S3, Azure Blob Storage ou une autre destination prise en charge.

## Comment modifier une intégration Currents en direct ? {#how-do-i-edit-a-live-currents-integration}

Pour modifier un connecteur Currents en direct, ouvrez l'intégration et sélectionnez **Edit**. Sans **Edit**, l'interface de l'intégration reste en lecture seule, et vous ne pouvez pas modifier les paramètres du connecteur à partir des icônes uniquement.

## Comment Braze gère-t-il les fichiers Avro dans Azure Blob Storage après le téléchargement ? {#how-does-braze-handle-azure-blob-storage-avro-files-after-upload}

Braze ne modifie pas les fichiers Avro dans [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents) une fois le téléchargement terminé. Azure peut bloquer la suppression d'un blob pendant qu'un téléchargement est encore en cours.

## Comment obtenir des données historiques ? {#how-do-i-get-historical-data}

Currents est un flux de données en temps réel et en direct, ce qui signifie que les événements ne peuvent pas être rejoués. Cependant, vous pouvez stocker les données Currents dans un entrepôt de données tel qu'[Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3) ou [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents), afin d'exploiter les événements passés comme bon vous semble. Les données sont conservées pendant 30 jours, mais pour des données plus anciennes, vous pouvez interroger [Snowflake]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/s3_to_snowflake).

## Pourquoi Currents produit-il des données au format Avro plutôt qu'en JSON ? {#why-does-currents-output-data-in-the-avro-format-not-json}

Contrairement à JSON, qui ne dispose pas de schéma natif, Avro prend en charge l'évolution de schéma de manière native. Vous bénéficiez également de la possibilité d'envoyer des fichiers Avro avec moins de bande passante et un espace de stockage réduit, car Avro est hautement compressible.

## Comment Braze gère-t-il la surcharge liée aux fichiers ? {#how-does-braze-handle-file-overhead}

Nous mettons en place un processus d'extraction, de transformation et de chargement (ETL), qui vous permet d'extraire de grandes quantités de données d'une base de données pour les placer et les stocker dans une autre.

## Où stocker ces données pour les interroger ? {#where-should-i-store-this-data-for-querying}

Braze est partenaire de plusieurs entrepôts de données dans lesquels vous pouvez stocker vos données pour les interroger. Nous recommandons d'utiliser :
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents).

## Quelle est la fiabilité des données Currents ? {#how-reliable-is-currents-data}

Currents garantit une distribution « au moins une fois », ce qui signifie que des événements en double peuvent occasionnellement être écrits dans votre compartiment de stockage. Si votre cas d'usage nécessite une distribution exactement une fois, vous pouvez dédupliquer les événements à l'aide du champ d'identifiant unique (`id`) envoyé avec chaque événement. Pour plus de détails, consultez [Sémantique de distribution des événements]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics).

## À quelle fréquence les données sont-elles synchronisées avec Currents ? {#how-often-is-data-synced-to-currents}

Les données sont diffusées en continu. Braze envoie un lot d'événements chaque fois qu'un lot complet est prêt à être envoyé, ou toutes les 5 minutes, selon ce qui survient en premier. Pour les connecteurs à fort volume, les données arrivent quasiment en temps réel. Pour les connecteurs à faible volume, prévoyez un délai de 5 à 30 minutes. Pour plus de détails, consultez [Seuil d'écriture Avro]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics#avro-write-threshold).

{% alert note %}
Si un appareil n'est pas connecté à Internet, la création de l'événement peut être retardée. Cela est plus fréquent pour les événements de messages in-app, car les messages in-app peuvent être déclenchés hors ligne.
{% endalert %}

## Comment trouver les événements disponibles pour Currents ? {#how-do-i-find-which-events-are-available-for-currents}

Pour obtenir la liste complète des événements enregistrés par Currents, consultez les glossaires des [événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) et des [événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events). Vous pouvez filtrer ces glossaires par type d'événement (comme les envois, les réceptions ou les ouvertures).

## Pourquoi le nombre de mes événements Currents ne correspond-il pas aux indicateurs de mon tableau de bord ou de mon rapport d'engagement ? {#why-do-my-currents-event-counts-not-match-my-dashboard-or-engagement-report-metrics}

Currents et le tableau de bord de Braze calculent certains indicateurs de manière différente, de sorte qu'une correspondance exacte entre les événements Currents et les indicateurs du tableau de bord n'est pas attendue.

**Clics uniques :** Pour les e-mails, le tableau de bord suit les clics uniques sur une période de sept jours et les mesure par `dispatch_id`. Currents enregistre chaque événement de clic brut. Pour aligner les comptages de clics uniques basés sur Currents avec les indicateurs du tableau de bord, filtrez les événements où `is_unique` est `true`.

**Désabonnements :** L'indicateur *Unsub* du tableau de bord reflète les clics sur le lien de désabonnement standard de Braze. Les pages de désabonnement personnalisées n'incrémentent pas cet indicateur, sauf si vous mettez à jour l'utilisateur via l'API. L'événement Currents `users.messages.email.Unsubscribe` est un événement de clic spécialisé qui se déclenche lorsqu'un utilisateur clique sur un lien de désabonnement dans le corps ou le pied de page de l'e-mail, ou via l'en-tête list-unsubscribe. Il ne représente pas chaque changement d'état d'abonnement aux e-mails.

**Horodatages et fuseaux horaires :** Tous les horodatages de Currents sont en UTC. Les indicateurs du tableau de bord suivent le fuseau horaire de votre entreprise. L'agrégation des données Currents par jour calendaire sans conversion vers le fuseau horaire de votre entreprise peut entraîner un classement des comptages dans des périodes différentes de celles affichées dans le tableau de bord.

**Événements en double :** Currents fournit une distribution « au moins une fois » (*at-least-once*), ce qui signifie que des événements en double peuvent occasionnellement être enregistrés. Dédupliquez à l'aide du champ `id` unique de chaque événement avant de comparer les totaux aux indicateurs du tableau de bord.

## Pourquoi le `external_user_id` (schéma Braze : `external_id`) dans mon événement d'ouverture ou de clic d'e-mail Currents diffère-t-il du profil utilisateur dans le tableau de bord de Braze ? {#why-does-the-external_user_id-braze-schema-external_id-in-my-currents-email-open-or-click-event-differ-from-the-user-profile-in-the-braze-dashboard}

- **Dans le tableau de bord de Braze :** Lorsqu'un utilisateur associé à une adresse e-mail ouvre ou clique sur un e-mail, tous les profils utilisateur partageant cette adresse e-mail sont marqués comme ayant ouvert ou cliqué sur cet e-mail. Pour plus d'informations, consultez [Que se passe-t-il lorsqu'un e-mail est envoyé et que plusieurs profils partagent la même adresse e-mail ?]({{site.baseurl}}/user_guide/channels/email/faq#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address).
- **Dans Currents :** Cette même ouverture ou ce même clic est enregistré sur un seul profil. Braze l'attribue au profil initialement ciblé pour l'envoi si ce profil partage toujours l'adresse e-mail. Dans le cas contraire, Braze l'attribue à un profil sélectionné aléatoirement parmi ceux qui partagent l'adresse e-mail.

Pour cette raison, la valeur `external_user_id` (nommée `external_id` dans la table de correspondance du schéma Braze) sur un événement d'ouverture ou de clic d'e-mail Currents peut ne pas correspondre au profil utilisateur attendu lorsque vous comparez Currents au tableau de bord de Braze.

## Tous les événements d'envoi sont-ils enregistrés dans Currents ? {#are-all-send-events-logged-to-currents}

Tous les événements sont enregistrés dans Currents. Il n'existe aucun scénario dans lequel un événement serait intentionnellement supprimé du flux Currents.

## Les données peuvent-elles être corrompues dans Currents ? {#can-data-be-corrupted-in-currents}

Dans des circonstances normales, les données de Currents ne sont pas corrompues. Bien qu'il existe toujours une possibilité de problème rare, aucune condition connue ne provoque de corruption systématique des données.

## Pourquoi est-ce que je vois des données d'événements personnalisés datant d'avant la mise en place de mon intégration Currents ? {#why-do-i-see-custom-event-data-dated-before-my-currents-integration-was-set-up}

Braze ne remplit pas rétroactivement les événements dans Currents. Cependant, les événements personnalisés peuvent être enregistrés avec un horodatage passé (par exemple, si un appareil était hors ligne au moment de l'événement et s'est synchronisé ultérieurement). Dans ces cas, l'horodatage de l'événement reflète le moment où l'événement s'est initialement produit, ce qui peut être antérieur à la configuration de l'intégration Currents.

## Quels identifiants utilisateur sont inclus dans les événements Currents ? {#what-user-identifiers-are-included-in-currents-events}

Les événements d'engagement liés aux messages (envois, ouvertures, clics, etc.) incluent l'identifiant utilisateur Braze (`user_id`) et, lorsqu'il est présent sur le profil, l'identifiant externe (`external_user_id` dans les payloads des événements, libellé `external_id` dans la table de mappage du schéma Braze). Certains événements d'engagement liés aux e-mails incluent également `email_address`. Les attributs personnalisés ne sont pas inclus.

Si vous routez les données Currents vers un entrepôt de données ou un CRM et que vous devez effectuer une jointure sur les données de profil, réalisez cette jointure dans votre système en aval en utilisant `user_id` ou `external_user_id`.

## Puis-je inclure des attributs personnalisés dans les événements d'envoi de Currents ? {#can-i-include-custom-attributes-in-currents-send-events}

Non. Currents n'inclut pas les attributs personnalisés dans les événements d'envoi. Currents enregistre les événements personnalisés et les événements d'engagement liés aux messages. Pour obtenir la liste complète des champs disponibles, consultez les [glossaires des événements]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary).

## Currents inclut-il les tags de Campaign ou de Canvas, ou les paires clé-valeur ? {#does-currents-include-campaign-or-canvas-tags-or-key-value-pairs}

Non. Currents n'inclut pas les tags de Campaign ou de Canvas, ni les paires clé-valeur au niveau des messages. Pour récupérer les données de tags, utilisez l'[API REST d'exportation]({{site.baseurl}}/api/endpoints/export). Comme autre solution de contournement, vous pouvez utiliser un canal webhook dans une Campaign pour envoyer les données de tags ou de paires clé-valeur vers votre propre endpoint, en utilisant [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) pour modéliser les valeurs.

## Comment Braze notifie-t-il les clients des modifications apportées à Currents ? {#how-does-braze-notify-customers-of-changes-to-currents}

Dans les rares cas où des changements majeurs (breaking changes) surviennent, Braze envoie un e-mail préalable au contact associé à toute intégration active, ainsi qu'à tous les administrateurs disposant d'intégrations Currents actives et ayant utilisé le tableau de bord au cours des 30 derniers jours. Pour les changements non majeurs, tels que de nouveaux événements ou de nouveaux champs ajoutés à un événement existant, Braze n'envoie pas de notification. Vous pouvez consulter le [journal des modifications de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) pour connaître les dernières modifications.

## De combien d'espace de stockage ai-je besoin pour les données Currents ? {#how-much-storage-do-i-need-for-currents-data}

Les besoins en stockage dépendent de votre volume d'événements et des types d'événements que vous exportez. Braze fournit des [exemples d'événements au format Avro](https://github.com/appboy/currents-examples/tree/master/sample-data) que vous pouvez utiliser pour estimer la taille des fichiers en fonction de votre cas d'usage.

## Pourquoi le nom de la Campaign ou de l'étape du Canvas est-il `NULL` dans mes données Currents ? {#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data}

Lorsque vous créez une nouvelle Campaign ou un nouveau Canvas, le nom peut mettre un certain temps à se propager dans tous les systèmes Braze. Les événements envoyés via Currents pendant cette période peuvent afficher `NULL` dans les champs de nom (tels que `campaign_name` ou `canvas_step_name`). Ce comportement est également attendu si le nom a été modifié peu avant l'enregistrement des événements. Pour éviter ce problème, attendez un certain temps après avoir créé ou renommé une Campaign ou une étape du Canvas avant de procéder à l'envoi.

## Pourquoi les événements de fin de session sont-ils retardés ou manquants dans Currents ? {#why-are-session-end-events-delayed-or-missing-in-currents}

Les événements de fin de session suivent le calendrier d'envoi normal du SDK. Le SDK Braze met en cache les données de session localement et les transmet périodiquement en fonction de la qualité du réseau — par exemple, environ toutes les 10 secondes sur une connexion stable. Tant que le SDK n'a pas envoyé l'événement, celui-ci n'apparaît pas dans Currents.

Si un utilisateur force la fermeture de l'application ou passe hors ligne avant le prochain envoi, l'événement de fin de session peut arriver en retard, voire ne jamais arriver. Sur iOS, les événements de fin de session ne sont souvent transmis que lorsque l'application est rouverte, car le SDK ne peut pas envoyer de données lorsque l'application est en arrière-plan.

Lorsque vous avez besoin de délimitations de session plus réactives dans Currents, appelez `requestImmediateDataFlush()` à des moments clés du cycle de vie, par exemple lorsque l'application passe en arrière-plan ou revient au premier plan. Pour en savoir plus, consultez [Envoi et téléchargement de données]({{site.baseurl}}/developer_guide/getting_started/sdk_overview#data-upload-and-download) et [Les horodatages de fin et de début de session sont similaires (iOS)]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log#session-end-and-session-start-have-similar-timestamps-ios).

## Que se passe-t-il si mon compartiment de stockage est indisponible lorsque Currents tente d'écrire des données ? {#what-happens-if-my-storage-bucket-is-unavailable-when-currents-tries-to-write-data}

Si votre compartiment de stockage est indisponible au moment du transfert de données, ces données sont perdues. Braze n'est pas en mesure de récupérer rétroactivement les événements qui n'ont pas été livrés avec succès. Pour éviter toute perte de données, assurez-vous que votre compartiment de stockage est disponible et correctement configuré en permanence.

## Pourquoi des messages de limite de droits s'affichent-ils lors de la création ou de la modification d'une intégration Currents ? {#why-do-i-see-entitlement-limit-messages-when-creating-or-editing-a-currents-integration}

Currents utilise des pools de droits distincts pour les différentes fonctionnalités de connecteur :

- **Événements d'engagement** : requis pour créer ou mettre à niveau un connecteur Currents standard.
- **Événements de comportement client** : requis pour activer **Track Customer Behavior and User Events**.
- **Profils et attributs utilisateur** : requis pour activer **Track user profiles and attributes**.

Si l'un de ces pools est épuisé, Braze affiche un avertissement relatif aux droits et bloque l'action concernée. Contactez votre gestionnaire de compte Braze pour demander des droits supplémentaires ou obtenir de l'aide pour ajuster votre configuration.

## À quelle fréquence la version de Currents dans le chemin de stockage change-t-elle ? {#how-often-does-the-currents-version-in-the-storage-path-change}

Le segment `version=<currents_version>` dans le chemin de stockage est mis à jour à chaque version de Currents selon une cadence mensuelle (par exemple, de `version=6` à `version=7`). Nous recommandons de lire les fichiers de manière récursive à partir du chemin racine plutôt que de coder en dur un segment de version spécifique, afin que votre pipeline récupère automatiquement les données après un changement de version. Pour plus de détails sur le format du chemin, consultez la section [Sémantique de distribution des événements]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics). Pour un historique des modifications par version, consultez le [journal des modifications de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs).

## Pourquoi `campaign_id` ou `canvas_id` sont-ils absents d'un événement d'engagement lié aux messages ? {#why-are-campaign_id-or-canvas_id-missing-from-a-message-engagement-event}

Selon le type d'événement et le contexte, un événement d'engagement lié aux messages peut ne pas être associé à une Campaign ou à une étape Canvas spécifique. Dans ces cas, les champs `campaign_id`, `canvas_id` et les champs de nom associés peuvent être omis du payload de l'événement. Si vous ne voyez pas ces champs pour un événement donné, vérifiez si ce type d'événement et ce contexte incluent normalement des identifiants de Campaign ou de Canvas.

## Pourquoi les horodatages de Currents sont-ils limités à la précision à la seconde ? {#why-are-currents-timestamps-limited-to-second-precision}

Le champ `time` dans les événements Currents est stocké sous forme d'entier 32 bits et est donc limité à la précision à la seconde. Certains événements incluent également un champ d'horodatage séparé en 64 bits avec une précision à la milliseconde ; consultez le [glossaire des événements]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary) pour connaître les champs disponibles pour chaque type d'événement.

## Pourquoi l'événement `users.canvas.Conversion` de Currents affiche-t-il une heure différente de celle du Canvas ? {#why-does-the-userscanvasconversion-event-from-currents-have-a-different-time-than-the-canvas}

L'heure de l'événement `users.canvas.Conversion` dans Currents reflète la fenêtre de conversion totale — la durée du Canvas plus la date limite de conversion — mesurée à partir de l'entrée dans le Canvas.

## Que se passe-t-il lorsque les rapports d'engagement sont envoyés vers S3 ? {#what-happens-when-engagement-reports-are-sent-to-s3}

Si les identifiants S3 sont configurés pour l'exportation de données mais pas pour Currents, Braze charge les rapports d'engagement dans le compartiment S3 spécifié. L'utilisateur indiqué dans le champ **Send Report To** reçoit un e-mail contenant un lien vers le rapport dans S3.

## Les données d'utilisateurs anonymes peuvent-elles être envoyées à Amplitude via Braze Currents ? {#can-anonymous-user-data-be-sent-to-amplitude-through-braze-currents}

Les données d'utilisateurs anonymes, identifiées par `device_id`, peuvent être envoyées à Amplitude via Currents. Cette fonctionnalité nécessite une activation par votre équipe de compte Braze.

## Comment les impressions du groupe de contrôle pour les Content Cards et les messages in-app sont-elles enregistrées dans Currents ? {#how-are-control-group-impressions-for-content-cards-and-in-app-messages-logged-in-currents}

Lorsqu'un utilisateur est affecté à un groupe de contrôle pour une Campaign de Content Cards ou de messages in-app, Currents émet un événement `users.campaigns.EnrollInControl` plutôt qu'un événement d'impression.

## Que se passe-t-il lorsque vous ciblez un utilisateur inexistant via l'API ? {#what-happens-when-you-target-a-non-existent-user-through-the-api}

Lorsque vous ciblez un utilisateur qui n'existe pas, l'API renvoie une réponse `200`, mais l'envoi est annulé avec le résultat « Unknown external ID ». Aucun événement Currents n'est généré pour cet envoi. Notez que le paramètre `send_to_existing_only` est défini par défaut sur `true`, de sorte que les envois vers des utilisateurs inconnus sont ignorés silencieusement, sauf si vous le définissez explicitement sur `false`.