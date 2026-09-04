---
# This file is a template consumed by the external `braze-currents-generate-docs` tool
# (braze-agent-plugins / braze-currents plugin) to generate the Currents event glossary
# docs. It is not referenced from within braze-docs, so do not delete it as "unused".
nav_title: Comportement des clients et événements utilisateur
article_title: Comportement des clients et événements utilisateur
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire répertorie les différents événements de comportement des clients et événements utilisateur que Braze peut suivre et envoyer vers les entrepôts de données de votre choix à l'aide de Currents."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% details Portée du schéma et ressources associées %}

Les schémas de stockage s'appliquent aux données d'événements en fichiers plats que nous envoyons aux partenaires de stockage en entrepôt de données (Google Cloud Storage, Amazon S3 et Microsoft Azure Blob Storage). Certaines combinaisons d'événements et de destinations répertoriées ici ne sont pas encore disponibles de manière générale. Pour savoir quels événements sont pris en charge par les différents partenaires, consultez notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) et vérifiez leurs pages respectives.

{% alert tip %}
Ces événements sont également disponibles sous forme de tables SQL dans le [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder), les [extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) et le [partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). Pour les schémas de tables SQL et les détails des colonnes, consultez la [référence des tables SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables).
{% endalert %}

Contactez votre conseiller Braze ou ouvrez un [ticket d'assistance]({{site.baseurl}}/user_guide/administer/personal/braze_support) si vous avez besoin d'accéder à des droits d'événements supplémentaires. Si vous ne trouvez pas ce que vous cherchez sur cette page, consultez notre [bibliothèque d'événements d'engagement liés aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) ou nos [exemples de données Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% enddetails %}

{% details Explication de la structure des événements de comportement des clients et événements utilisateur et des valeurs de plateforme %}

## Structure des événements {#event-structure}

Cette décomposition des événements de comportement des clients et événements utilisateur montre le type d'informations généralement incluses dans un événement de comportement client ou un événement utilisateur. Avec une bonne compréhension de ses composants, vos développeurs et votre équipe d'aide à la décision peuvent utiliser les données d'événements Currents entrantes pour créer des rapports et des graphiques basés sur les données, et tirer parti d'autres indicateurs précieux.

![Décomposition d'un événement utilisateur montrant un événement d'achat avec les propriétés répertoriées regroupées par propriétés spécifiques à l'utilisateur, propriétés spécifiques au comportement et propriétés spécifiques à l'appareil]({% image_buster /assets/img/customer_engagement_event.png %})

Les événements de comportement des clients et événements utilisateur sont composés de propriétés **spécifiques à l'utilisateur**, de propriétés **spécifiques au comportement** et de propriétés **spécifiques à l'appareil**.

### Valeurs de plateforme {#platform-values}

Certains événements renvoient une valeur `platform` qui spécifie la plateforme de l'appareil de l'utilisateur.
<br>Le tableau suivant détaille les valeurs possibles renvoyées :

| Appareil de l'utilisateur | Valeur de plateforme |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Valeurs de plateforme" }

{% enddetails %}

{% details Considérations relatives aux événements de comportement des clients et événements utilisateur %}

- Currents supprime les événements dont les payloads sont excessivement volumineux, c'est-à-dire supérieurs à 900&nbsp;Ko.
- De nombreux événements de ce glossaire sont initiés par le SDK. Certains événements, tels que `token_state_change`, peuvent être initiés soit par le SDK, soit par le backend (par exemple, en réponse à un rebond de notification push). Les champs `sdk_version`, `gender`, `language` et `country` ne sont définis que pour les événements initiés par le SDK ; pour les événements initiés par le backend, ou lorsque ces informations ne sont pas disponibles ou ne sont pas définies pour l'utilisateur, ces champs peuvent être `null`.

{% enddetails %}

</div>

<!--overview-end-->