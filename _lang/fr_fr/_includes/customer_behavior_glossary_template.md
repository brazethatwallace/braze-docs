---
nav_title: Comportement des clients et événements utilisateurs
article_title: Comportement des clients et événements utilisateurs
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire répertorie les différents comportements des clients et événements utilisateurs que Braze peut suivre et envoyer vers des entrepôts de données de votre choix via Currents."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% details Portée du schéma et ressources associées %}

Les schémas de stockage s'appliquent aux données d'événements sous forme de fichiers plats que nous envoyons aux partenaires de stockage d'entrepôt de données (Google Cloud Storage, Amazon S3 et Microsoft Azure Blob Storage). Certaines combinaisons d'événements et de destinations répertoriées ici ne sont pas encore disponibles de manière générale. Pour savoir quels événements sont pris en charge par les différents partenaires, consultez notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/) et leurs pages respectives.

{% alert tip %}
Ces événements sont également disponibles sous forme de tables SQL dans le [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder/), les [Extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/) et le [Partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/). Pour les schémas de tables SQL et le détail des colonnes, consultez la [référence des tables SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables/).
{% endalert %}

Contactez votre conseiller Braze ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/) si vous avez besoin d'accéder à des droits d'événements supplémentaires. Si vous ne trouvez pas ce dont vous avez besoin sur cette page, consultez notre [bibliothèque des événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) ou nos [exemples de données Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% enddetails %}

{% details Explication de la structure des comportements clients et événements utilisateurs, et des valeurs de plateforme %}

### Structure des événements {#event-structure}

Cette présentation des comportements des clients et des événements utilisateurs décrit le type d'informations généralement incluses dans un comportement client ou un événement utilisateur. Avec une bonne compréhension de ses composants, vos développeurs et votre équipe d'aide à la décision peuvent exploiter les données d'événements Currents entrantes pour créer des rapports et des graphiques axés sur les données, et tirer parti d'autres indicateurs précieux.

![Décomposition d'un événement utilisateur montrant un événement d'achat avec les propriétés répertoriées, regroupées par propriétés propres à l'utilisateur, propriétés propres au comportement et propriétés propres à l'appareil]({% image_buster /assets/img/customer_engagement_event.png %})

Les comportements des clients et les événements utilisateurs se composent de propriétés **propres à l'utilisateur**, de propriétés **propres au comportement** et de propriétés **propres à l'appareil**.

### Valeurs de plateforme {#platform-values}

Certains événements renvoient une valeur `platform` qui spécifie la plateforme de l'appareil de l'utilisateur.
<br>Le tableau suivant détaille les valeurs pouvant être renvoyées :

| Appareil de l'utilisateur | Valeur de la plateforme |
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

{% details Considérations relatives aux comportements des clients et aux événements utilisateurs %}

- Currents abandonne les événements dont le payload est excessivement volumineux (supérieur à 900&nbsp;Ko).
- De nombreux événements de ce glossaire sont initiés par le SDK. Certains événements, comme `token_state_change`, peuvent être initiés par le SDK ou par le backend (par exemple, en réponse à un rebond de notification push). Les champs `sdk_version`, `gender`, `language` et `country` ne sont renseignés que pour les événements initiés par le SDK ; pour les événements initiés par le backend, ou lorsque ces informations ne sont pas disponibles ou pas définies pour l'utilisateur, ces champs peuvent être `null`.

{% enddetails %}

</div>

<!--overview-end-->