---
nav_title: avril
page_order: 9
noindex: true
page_type: update
description: "Cet article contient les notes de version d'avril 2019."
---

# Avril 2019 {#april-2019}

## Nouveaux champs et événements dans Currents {#new-currents-events-fields}

En plus des corrections apportées à la section, un nouvel [événement d'abonnement]({{ site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/#subscription-events) a été ajouté à la page des événements d'engagement liés aux messages.

Vous pouvez désormais exporter les données de changement d'état des groupes d'abonnement depuis Braze vers [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents#integration-details) et [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents), ainsi que ces données et les événements d'attribution d'installation dans [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel).

En outre, la propriété `canvas_step_id` a été ajoutée aux [événements de conversion]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#conversion-events) disponibles.

{% alert important %}
Pour profiter de ces mises à jour, vous devrez modifier les paramètres de vos connecteurs Currents et activer les événements que vous souhaitez utiliser. Contactez votre gestionnaire de compte si vous avez des questions.
{% endalert %}

## Archivage des groupes d'abonnement {#subscription-groups-archiving}

Vous pouvez désormais [archiver les groupes d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#archiving-groups) ! Les groupes d'abonnement archivés ne peuvent pas être modifiés et n'apparaîtront plus dans les filtres de Segment. Si vous tentez d'archiver un groupe utilisé comme filtre de Segment dans un e-mail, une Campaign ou un Canvas, vous recevrez un message d'erreur qui vous empêchera d'archiver le groupe tant que vous n'en aurez pas supprimé toutes les utilisations.