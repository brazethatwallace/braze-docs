---
nav_title: Profils utilisateur
layout: user_profiles_event_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire répertorie les mises à jour de profils utilisateur que Braze peut suivre et envoyer vers les entrepôts de données de votre choix à l'aide de Currents."
tool: Currents
search_rank: 7
---

{% alert tip %}
Ces événements sont également disponibles sous forme de tables SQL dans le [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder/), les [Extensions de segments SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) et le [Partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/). Pour consulter les schémas de tables SQL et les détails des colonnes, reportez-vous à la [référence des tables SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/sql_segments/sql_segments_tables/).
{% endalert %}

Contactez votre conseiller Braze ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/) si vous avez besoin d'accéder à des droits d'événements supplémentaires. Si vous ne trouvez pas ce que vous cherchez sur cette page, consultez la [bibliothèque des événements de comportement client]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/), la [bibliothèque des événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) ou les [exemples de données Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explication de la structure des événements de mise à jour de profil utilisateur %}

### Structure des événements {#event-structure}

Cette analyse des événements de comportement client et des événements utilisateur présente le type d'informations généralement incluses dans un événement de mise à jour de profil utilisateur. En comprenant bien ses composants, vos équipes de développement et d'aide à la décision pourront exploiter les données d'événements Currents entrantes pour créer des rapports et des graphiques basés sur les données, et tirer parti d'autres indicateurs précieux.

{% alert important %}
Les schémas de stockage s'appliquent aux données d'événements en fichiers plats envoyées aux partenaires de stockage en entrepôt de données, tels que Google Cloud Storage, Amazon S3 et Microsoft Azure Blob Storage. Certaines combinaisons d'événements et de destinations répertoriées ici ne sont pas encore disponibles de manière générale. Pour en savoir plus sur les événements pris en charge par partenaire, consultez les [partenaires disponibles]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) et les pages partenaire associées.

Currents supprime les événements dont le payload dépasse 900 Ko.
{% endalert %}