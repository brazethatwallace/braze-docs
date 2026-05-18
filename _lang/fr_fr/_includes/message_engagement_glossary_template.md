---
nav_title: Événements d'engagement lié aux messages
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire répertorie les différents événements d'engagement lié aux messages que Braze peut suivre et envoyer vers les entrepôts de données de votre choix à l'aide de Currents."
tool: Currents
search_rank: 6
---

Les schémas de stockage s'appliquent aux données d'événements sous forme de fichiers plats que nous envoyons aux partenaires de stockage d'entrepôt de données (Google Cloud Storage, Amazon S3 et Microsoft Azure Blob Storage). Pour les schémas qui s'appliquent aux autres partenaires, consultez notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/) et reportez-vous à leurs pages respectives.

{% alert tip %}
Ces événements sont également disponibles sous forme de tables SQL dans le [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder/), les [Extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/) et le [Partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/). Pour les schémas de tables SQL et les détails des colonnes, consultez la [référence des tables SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables/).
{% endalert %}

Contactez votre gestionnaire de compte ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/) si vous avez besoin d'accéder à des droits d'événements supplémentaires. Si vous ne trouvez pas ce dont vous avez besoin dans cet article, consultez notre [bibliothèque d'événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) ou nos [exemples de données Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explication de la structure des événements d'engagement lié aux messages et des valeurs de plateforme %}

### Structure d'événement {#event-structure}

Cette ventilation des événements montre le type d'informations généralement incluses dans un événement d'engagement lié aux messages. Grâce à une bonne compréhension de ses composants, vos développeurs et votre équipe d'aide à la décision peuvent exploiter les données d'événements Currents entrantes pour créer des rapports et des graphiques basés sur les données, et tirer parti d'autres indicateurs précieux.

![Ventilation d'un événement d'engagement lié aux messages montrant un événement de désabonnement par e-mail avec les propriétés répertoriées, regroupées par propriétés spécifiques à l'utilisateur, propriétés de suivi de campagne ou de Canvas, et propriétés spécifiques à l'événement]({% image_buster /assets/img/message_engagement_event.png %})

Les événements d'engagement lié aux messages se composent de propriétés **spécifiques à l'utilisateur**, de propriétés de **suivi de campagne/Canvas** et de propriétés **spécifiques à l'événement**.

### Schéma d'ID utilisateur {#user-id-schema}

Notez les conventions de nommage pour les ID utilisateur.

| Schéma Braze | Schéma Currents | Description |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | L'identifiant unique attribué automatiquement par Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | L'identifiant unique du profil d'un utilisateur, défini par le client. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schéma d'ID utilisateur" }

### Valeurs de plateforme {#platform-values}

Certains événements renvoient une valeur `platform` qui spécifie la plateforme de l'appareil de l'utilisateur.
<br>Le tableau suivant détaille les valeurs pouvant être renvoyées :

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

{% alert important %}
Currents abandonnera les événements dont le payload est excessivement volumineux (supérieur à 900&nbsp;Ko).
{% endalert %}

{% alert note %}
Les objets liés à Canvas Flow possèdent des ID qui peuvent être utilisés pour le regroupement et convertis en noms lisibles via l'[endpoint Exporter les détails du Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/).
{% endalert %}

{% alert note %}
Certains champs peuvent mettre plus de temps à afficher leur état le plus récent après la mise à jour d'une campagne ou d'un Canvas. Ces champs sont les suivants :
<ul>
  <li>"campaign_name"</li>
  <li>"canvas_name"</li>
  <li>"canvas_step_name"</li>
  <li>"conversion_behavior"</li>
  <li>"canvas_variation_name"</li>
  <li>"experiment_split_name"</li>
  <li>"message_variation_name"</li>
</ul>
Si une cohérence totale est requise, nous vous recommandons d'attendre une heure après la dernière mise à jour de ces champs avant d'envoyer vos messages à vos utilisateurs.
{% endalert %}