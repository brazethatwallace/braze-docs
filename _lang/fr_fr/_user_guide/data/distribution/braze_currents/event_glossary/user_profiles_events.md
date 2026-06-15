---
nav_title: Profils utilisateur
layout: user_profiles_event_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire répertorie les mises à jour de profils utilisateur que Braze peut suivre et envoyer aux entrepôts de données de votre choix à l'aide de Currents."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% alert important %}
Les événements de profils utilisateur sont en version bêta. Contactez votre gestionnaire de la satisfaction client ou votre gestionnaire de compte pour y accéder.
{% endalert %}

{% alert tip %}
Ces événements sont également disponibles sous forme de tables SQL dans le [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder/), les [Extensions de segments SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) et le [Partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/). Pour les schémas de tables SQL et les détails des colonnes, consultez la [référence des tables SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/sql_segments/sql_segments_tables/).
{% endalert %}

Contactez votre conseiller Braze ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/) si vous avez besoin d'accéder à des droits d'événements supplémentaires. Si vous ne trouvez pas ce que vous cherchez sur cette page, consultez la [bibliothèque des événements de comportement client]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/), la [bibliothèque des événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) ou les [exemples de données Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explication de la structure des événements de mise à jour de profil utilisateur %}

### Structure des événements {#event-structure}

Cette analyse des événements de comportement client et des événements utilisateur montre le type d'informations généralement incluses dans un événement de mise à jour de profil utilisateur. Grâce à une bonne compréhension de ses composants, vos développeurs et votre équipe d'aide à la décision peuvent exploiter les données d'événements Currents entrantes pour créer des rapports et des graphiques basés sur les données, et tirer parti d'autres indicateurs précieux.

{% alert important %}
Les schémas de stockage s'appliquent aux données d'événements de fichiers plats envoyées aux partenaires de stockage en entrepôt de données, tels que Google Cloud Storage, Amazon S3 et Microsoft Azure Blob Storage. Certaines combinaisons d'événements et de destinations répertoriées ici ne sont pas encore disponibles de manière générale. Pour plus d'informations sur les événements pris en charge par partenaire, consultez les [partenaires disponibles]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) et les pages partenaire associées.

Currents supprime les événements dont les payloads dépassent 900 Ko.
{% endalert %}

{% enddetails %}

</div>

<!--overview-end-->

{% api %}
## Événements de mise à jour de profil utilisateur {#user-profile-update-events}

{% apitags %}
Profile
{% endapitags %}

Cet événement représente les mises à jour de profil d'un utilisateur.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.profile.Update

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "archived" : "(optional, boolean) When set to True, indicates that this user was archived within Braze",
  "country" : "(optional, string) [PII] Country of the user",
  "custom_attributes" : "(optional, string) Valid JSON string of the updated custom attributes",
  "dob" : "(optional, string) [PII] Date of birth of the user in format \"YYYY-MM-DD\"",
  "email_address" : "(optional, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "first_name" : "(optional, string) [PII] First name of the user",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "home_city" : "(optional, string) [PII] Home city of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "last_name" : "(optional, string) [PII] Last name of the user",
  "phone_number" : "(optional, string) [PII] Phone number of the user in e.164 format",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "time_ms" : "(required, long) Time in milliseconds when the update happened",
  "timezone" : "(optional, string) Time zone of the user",
  "update_source" : "(required, string) The source of this update",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}