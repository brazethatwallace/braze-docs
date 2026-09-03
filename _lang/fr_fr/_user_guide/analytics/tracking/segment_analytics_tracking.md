---
nav_title: Suivi analytique des segments
article_title: Suivi analytique des segments
page_order: 3
page_type: reference
description: "Cet article de référence couvre le suivi analytique des segments et explique comment afficher le chiffre d'affaires et les achats au fil du temps, les sessions au fil du temps et les événements personnalisés au fil du temps."
tool:
  - Segments
  - Reports
---

# Suivi analytique des segments {#segment-analytics-tracking}

> Lorsque le suivi analytique est activé pour un segment, vous pouvez afficher les sessions, les événements personnalisés et le chiffre d'affaires au fil du temps pour ce segment.

Si vous n'activez pas le suivi analytique pour un segment, vous pouvez toujours accéder aux [statistiques en temps réel]({{site.baseurl}}/user_guide/audience/segments/segment_data#segment-statistics) de ce segment et cibler ses utilisateurs avec des Campaigns. La seule différence réside dans l'accès aux outils d'analyse spécifiques mentionnés sur cette page.

## Activer l'analyse des segments {#turning-on-segment-analytics}

Dans la section **Segment Details** de la page d'un segment, activez **Analytics Tracking**.

![Bouton d'activation du suivi analytique pour un segment]({% image_buster /assets/img_archive/A_Tracking_2.png %})

Un espace de travail peut activer le suivi pour un maximum de 25 segments. Braze recommande de suivre les segments importants pour analyser l'impact de vos Campaigns sur les sessions, le chiffre d'affaires et les achats.

{% alert note %}
Après avoir activé le suivi analytique, un délai est à prévoir avant que les données du segment n'apparaissent dans vos rapports. Si les données ne s'affichent pas dans les 24 heures, [contactez le support]({{site.baseurl}}/user_guide/administer/personal/braze_support).
{% endalert %}

## Afficher le chiffre d'affaires et les achats au fil du temps {#viewing-revenue-and-purchases-over-time}

Accédez à **Analytics** > **Revenue Report** pour consulter les données sur [le chiffre d'affaires et les achats au fil du temps pour ce segment]({{site.baseurl}}/user_guide/analytics/reports/revenue_report).

Les graphiques de chiffre d'affaires et d'achats reflètent l'activité enregistrée après l'activation du suivi analytique pour ce segment. L'activation du suivi ne rétroalimente pas les achats antérieurs dans ces rapports. Lorsque vous comparez des segments, utilisez uniquement des plages temporelles pendant lesquelles le suivi était activé pour chaque segment sélectionné.

![Données de chiffre d'affaires par segment]({% image_buster /assets/img_archive/Revenue.png %})

Pour comparer visuellement les données de segments sur une plage temporelle personnalisée, ajoutez ou supprimez des segments du graphique. Sélectionnez **By Segment** dans le menu déroulant **Breakdown**, puis sélectionnez vos segments dans **Breakdown values**.

Sélectionnez le nom d'un segment dans la légende du graphique pour activer ou désactiver la visibilité des indicateurs de ce segment.

![Chiffre d'affaires pour plusieurs segments]({% image_buster /assets/img_archive/segment_revenue_multiple.png %})

## Sessions au fil du temps {#sessions-over-time}

De la même manière, vous pouvez trouver des données sur les [sessions au fil du temps pour ce segment particulier]({{site.baseurl}}/user_guide/analytics/dashboards/home) sur la page **Accueil**.

![Données de session par segment]({% image_buster /assets/img_archive/events_over_time2.png %})

## Afficher les événements personnalisés au fil du temps {#view-custom-events-over-time}

Consultez les données sur les [événements personnalisés au fil du temps pour les Segments]({{site.baseurl}}/user_guide/data/activation/events/custom_events#analytics) en accédant à **Analytics** > **Rapport d'événements personnalisés**.

## Utiliser les modèles du Query Builder {#using-query-builder-templates}

Lorsque le suivi analytique est activé, vous pouvez utiliser les modèles de rapports du Query Builder pour décomposer les indicateurs de performance par Segments pour les Campaigns, les Canvas, les variantes et les étapes. Pour en savoir plus, consultez [Données de Segment]({{site.baseurl}}/user_guide/audience/segments/segment_data#viewing-performance-data-by-segment).

## Questions fréquentes {#frequently-asked-questions}

### Que dois-je vérifier si le suivi analytique semble incorrect ou vide ? {#what-should-i-check-if-analytics-tracking-looks-wrong-or-empty}

Confirmez que le **suivi analytique** est toujours activé dans les **détails du Segment**, que vous n'avez pas dépassé la limite par espace de travail (25 segments avec suivi), et attendez jusqu'à 24 heures pour que les données se remplissent après la première activation du suivi. Si le problème persiste, vérifiez la définition du Segment et la plage de dates du rapport, puis [contactez le support]({{site.baseurl}}/user_guide/administer/personal/braze_support).