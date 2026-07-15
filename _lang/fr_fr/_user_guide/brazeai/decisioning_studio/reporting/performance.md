---
nav_title: Performance
article_title: Rapport de performance
page_order: 1
description: "Découvrez comment utiliser le rapport de performance pour comparer les groupes de traitement et les groupes de contrôle dans BrazeAI Decisioning Studio."
---

# Rapport de performance {#performance-report}

> Le rapport de performance montre comment votre agent de décision se comporte par rapport aux groupes de contrôle. Ce guide explique ce que représente chaque section du rapport, comment les indicateurs sont calculés et comment interpréter les résultats.

## Comment le rapport est construit {#how-the-report-is-built}

Votre rapport de performance est construit par couches, entièrement personnalisé selon votre cas d'usage. En collaboration avec votre équipe :

1. Braze définit ce qui constitue une action (comme un envoi, un clic, un achat ou une conversion).
2. Braze définit comment mesurer cette action quotidiennement (volume, chiffre d'affaires, personnes uniques, etc.).
3. Braze définit l'indicateur métier que vous souhaitez visualiser (comme le taux de conversion ou le chiffre d'affaires par utilisateur).
4. Les règles temporelles et la segmentation sont appliquées.
5. L'onglet **Performance** affiche les résultats.

Rien dans le tableau de bord ne crée de nouvelles données. Il visualise les résultats quotidiens stockés en fonction de ces définitions.

## Plage de dates et groupes de comparaison {#date-range-and-comparison-groups}

En haut du tableau de bord, vous choisissez :

- **Date range :** la période couverte par le rapport.
- **Comparison groups :** les groupes comparés (par exemple, Decisioning Studio versus Business as Usual).
- **Aggregation :** le paramètre d'agrégation du graphique (Daily, 7-day rolling ou 30-day rolling).
- **Segments :** tous les Segments appliqués. Ceux-ci sont configurés sur mesure avec votre équipe AI Expert Services.
- **Timeline events :** permet de superposer des événements configurés sur le graphique pour vous aider à comprendre les changements ou événements susceptibles d'impacter la performance.

![Rapport de performance montrant les groupes de comparaison, l'agrégation, les Segments et les filtres d'événements de la chronologie en haut, ainsi que le sélecteur de plage de dates en haut à droite.]({% image_buster /assets/img/decisioning_studio/reporting_performance_date_range.png %})

Ces sélections déterminent quels jours sont inclus, quels groupes sont comparés, comment la courbe de tendance est lissée et quelle population vous consultez.

{% alert important %}
Modifier le paramètre d'agrégation (par exemple, moyenne glissante sur 7 jours) n'affecte que l'affichage du graphique. Cela ne modifie pas les données stockées.
{% endalert %}

Si vous ne pouvez pas sélectionner une date récente dans le sélecteur de dates, cette date est probablement désactivée en raison de délais configurés pour la disponibilité des données. Il existe deux types de délais pouvant limiter la disponibilité des dates :

- **Délais du pipeline de données :** le temps nécessaire pour ingérer et traiter les données de votre CDP dans Decisioning Studio. Cela garantit que les rapports n'affichent que des données complètes et fiables.
- **Délais d'activation des recommandations :** le temps entre le moment où le moteur de Decisioning Studio prédit une recommandation et celui où vous l'activez dans vos Campaigns. Le reporting n'inclura pas les jours où les recommandations n'ont pas encore été activées.

Ces délais sont configurés pour votre cas d'usage. Si vous avez besoin de comprendre votre fenêtre de reporting spécifique, contactez votre AI Success Manager.

## Cartes KPI {#kpi-cards}

Les cartes KPI situées sur le côté principal du rapport affichent les indicateurs clés de performance configurés pour votre cas d'usage, tels que :

- LTV incrémentale / Client
- Conversions / Client
- Désabonnements / Client

Chaque carte représente le KPI calculé sur l'ensemble de la plage de dates sélectionnée. Il s'agit d'une valeur sur la période complète, et non d'une moyenne quotidienne. Par exemple, si vous voyez « LTV incrémentale / Client = 3,192 », cela reflète la performance sur l'ensemble de la fenêtre sélectionnée.

![Rapport de performance montrant les cartes récapitulatives KPI à gauche, incluant des indicateurs comme LTV incrémentale / Client, Conversions / Client et Désabonnements / Client.]({% image_buster /assets/img/decisioning_studio/reporting_performance_kpi_cards.png %})

## Graphique de tendance KPI {#kpi-trend-chart}

Utilisez le graphique pour comprendre les tendances dans le temps, les évolutions de performance et les effets de saisonnalité ou de timing. Utilisez la carte KPI pour comprendre l'impact global sur l'ensemble de la fenêtre. Le graphique central affiche le même KPI que la carte du haut, mais calculé par jour. Chaque point représente la valeur du KPI pour ce jour. Si vous avez sélectionné la moyenne glissante sur 7 jours, chaque point reflète une moyenne glissante, ce qui lisse la volatilité quotidienne.

![Rapport de performance montrant le graphique de tendance central intitulé LTV incrémentale / Client, avec des courbes pour Decisioning Studio et le groupe Business as Usual (BAU) tracées dans le temps.]({% image_buster /assets/img/decisioning_studio/reporting_performance_trend_chart.png %})

Le graphique et la carte KPI sont conçus pour montrer des choses différentes. Le graphique montre la performance quotidienne (« Quelle a été votre performance chaque jour ? »). La carte KPI montre la performance sur la période complète (« Quelle a été votre performance sur l'ensemble de la période ? »). Pour les indicateurs de taux, ils répondent à des questions différentes.

Prenons l'exemple suivant avec ces taux de conversion :

- Jour 1 : 10 conversions sur 100 clients = 10 %
- Jour 2 : 2 conversions sur 10 clients = 20 %

Le graphique affiche les deux. La carte KPI recalcule sur les deux jours combinés (12 conversions / 110 clients = 10,9 %), et non une moyenne de 10 % et 20 %.

## Graphique d'uplift {#uplift-chart}

Le graphique d'uplift montre la différence en pourcentage entre vos groupes de comparaison. Il est calculé ainsi : **(Groupe principal - Groupe de comparaison) / Groupe de comparaison**. Ce calcul est effectué dynamiquement à partir des valeurs du graphique KPI.

![Rapport de performance montrant le graphique de pourcentage d'uplift à droite, affichant la différence en pourcentage entre Decisioning Studio et le groupe BAU dans le temps.]({% image_buster /assets/img/decisioning_studio/reporting_performance_uplift.png %})

{% alert important %}
L'uplift n'est pas stocké. Il est calculé à partir des résultats KPI. Si l'uplift change, c'est parce que le KPI sous-jacent a changé.
{% endalert %}

## Tableau agrégé {#aggregate-table}

Le tableau en bas du rapport affiche les totaux bruts sur la plage de dates sélectionnée, tels que :

- LTV incrémentale totale
- Nombre total de clients
- Valeur KPI dérivée

Cette section renforce la relation entre les différentes vues :

- La carte KPI est un calcul au niveau de la fenêtre.
- Le graphique est un calcul quotidien.
- Le tableau montre les totaux sous-jacents qui alimentent le KPI.

![Rapport de performance montrant le tableau agrégé en bas, avec des colonnes pour Groupe, LTV incrémentale, Client et LTV incrémentale / Client pour chaque groupe de comparaison.]({% image_buster /assets/img/decisioning_studio/reporting_performance_aggregate_table.png %})

## Arbre des facteurs {#driver-tree}

L'arbre des facteurs décompose un KPI en ses composants. Par exemple, LTV incrémentale / Client peut se décomposer en :

- Conversions / Client
- Chiffre d'affaires par conversion

![Rapport de performance en vue Arbre des facteurs, montrant un diagramme hiérarchique qui décompose les KPI comme LTV incrémentale / Client en composants tels que Conversions / Client et Clics / Client.]({% image_buster /assets/img/decisioning_studio/reporting_performance_driver_tree.png %})

Les arbres des facteurs utilisent les mêmes définitions de KPI que le reste du tableau de bord et n'introduisent aucun nouveau calcul. Ils aident à expliquer ce qui influence la performance. Si une définition de KPI change, les graphiques, les cartes, l'uplift et les arbres des facteurs se mettent tous à jour ensemble.

## Questions fréquentes {#frequently-asked-questions}

### Comment fonctionnent les Segments ? {#how-do-segments-work}

Les Segments vous permettent de ventiler la performance par groupes définis, tels que les niveaux d'engagement, les caractéristiques client, le type d'appareil ou d'autres attributs configurés.

L'appartenance à un Segment est configurée sur mesure pour votre cas d'usage et calculée quotidiennement. Cela signifie que le Segment passé d'un client reflète qui il était ce jour-là. Si son comportement change par la suite, les jours historiques restent inchangés. Cela préserve la précision historique et empêche les rapports de se modifier rétroactivement.

### Le rapport de performance diffère-t-il entre les agents Go et Pro ? {#does-the-performance-report-for-go-versus-pro-agents-differ}

Les KPI pour les cas d'usage Go sont définis automatiquement et standardisés, car tous les cas d'usage Go ont le même indicateur cible : les clics uniques.

### Pourquoi ne puis-je pas sélectionner certaines dates récentes ? {#why-cant-i-select-certain-recent-dates}

Le sélecteur de dates peut ne pas permettre de sélectionner les jours les plus récents. C'est intentionnel. Les rapports peuvent appliquer les contraintes suivantes pour empêcher l'affichage de données incomplètes ou instables :

- **Délais du pipeline de données :** configurés pour tenir compte du temps nécessaire à l'ingestion et au traitement des données de votre CDP. Cela garantit que toutes les données d'un jour donné sont complètes avant que ce jour n'apparaisse dans le reporting.
- **Délais d'activation des recommandations :** configurés pour tenir compte du décalage entre le moment où les recommandations sont générées et celui où elles sont activées dans vos Campaigns. Les jours où les recommandations n'ont pas encore été activées n'apparaîtront pas dans le reporting.
- **Dates explicitement exclues :** dates que vous avez manuellement exclues dans les paramètres de reporting.

Si vous avez besoin de précisions sur votre fenêtre de reporting ou vos règles de disponibilité des données, contactez votre AI Success Manager.

### Quelle est la différence entre les KPI de « volume » et de « taux » ? {#whats-the-difference-between-volume-and-rate-kpis}

Les KPI se répartissent généralement en deux catégories :

- **Indicateurs de volume** (comme le total des conversions, le chiffre d'affaires total ou le total des clics) répondent à la question : « Combien cela représente-t-il ? »
- **Indicateurs de taux** (comme le taux de conversion, le chiffre d'affaires par utilisateur ou le taux de clics) répondent à la question : « Avec quelle efficacité cela s'est-il produit ? »

Volume et taux racontent des histoires différentes. Une campagne peut générer un volume plus élevé mais une efficacité moindre, ou inversement. Lorsque vous interprétez les résultats, vérifiez toujours quel type de KPI vous consultez.

### Que signifie « unique » (ou « distinct ») ? {#what-does-unique-or-distinct-mean}

Lorsqu'un indicateur est défini comme « unique », les individus sont dédupliqués à l'aide d'un identifiant spécifique (généralement le client). Chaque personne est comptée une seule fois par jour.

« Unique par jour » est différent de « unique sur l'ensemble de la plage de dates ». Si vous voyez des comptages uniques quotidiens additionnés sur plusieurs jours, le même individu peut apparaître plus d'une fois (une fois par jour où il a interagi). C'est intentionnel.

Si vous avez besoin de comprendre comment l'unicité a été définie dans votre configuration, contactez votre AI Success Manager.

### Pourquoi ce rapport peut-il différer d'un autre système ? {#why-might-this-report-differ-from-another-system}

Si votre rapport de performance ne correspond pas à un autre tableau de bord (comme un ESP, un outil d'analyse ou un rapport BI interne), cela ne signifie pas nécessairement qu'il y a un problème. Les différents systèmes appliquent souvent des définitions et des règles différentes. Voici les raisons les plus courantes :

- **Règles d'attribution :** certains indicateurs appliquent une logique d'attribution, ce qui signifie que seule l'activité répondant à des critères définis est comptabilisée. Si un autre système comptabilise toute l'activité sans logique d'attribution, les totaux peuvent différer.
- **Filtrage des engagements de machines et de bots :** les engagements connus provenant de machines ou de bots (comme les scans de sécurité automatisés ou les clics non humains) sont filtrés pour garantir que la performance reflète le comportement humain réel. Certaines plateformes incluent ces interactions dans leurs totaux.
- **Définitions différentes de « unique » :** dans ce rapport, l'unicité est généralement appliquée par jour. Un autre système peut calculer l'unicité sur l'ensemble d'une fenêtre de Campaign. Ce sont des questions métier différentes qui produisent des chiffres différents.
- **Plage de dates et règles de disponibilité des données :** les rapports peuvent appliquer des délais d'activation, des délais de disponibilité des données ou des dates exclues. Un autre système peut inclure des données très récentes ou incomplètes, créant des écarts temporaires.
- **Différences entre volume et taux :** un système peut afficher le volume total (comme le total des conversions), tandis qu'un autre affiche un taux (comme les conversions par client). Vérifiez toujours que vous comparez le même type d'indicateur.

### Pourquoi le chiffre du graphique ne correspond-il pas à la carte récapitulative ? {#why-doesnt-the-number-in-the-chart-match-the-summary-card}

Le graphique et la carte récapitulative répondent à des questions différentes :

- **Graphique :** montre la performance quotidienne. Chaque point reflète le KPI calculé pour ce jour individuel.
- **Carte récapitulative :** montre la performance sur la période complète. Elle recalcule le KPI sur l'ensemble de la plage de dates sélectionnée.

Utilisez le graphique pour comprendre la volatilité au jour le jour, les effets de timing et les évolutions de performance dans le temps. Utilisez la carte récapitulative pour comprendre l'impact global sur la période.

Prenons cet exemple avec le taux de conversion suivant :

- Jour 1 : 10 conversions sur 100 clients = 10 %
- Jour 2 : 2 conversions sur 10 clients = 20 %

Le graphique affiche 10 % au Jour 1 et 20 % au Jour 2. La carte récapitulative calcule la performance sur les deux jours combinés : 12 conversions au total sur 110 clients = 10,9 %. Elle ne fait pas la moyenne de 10 % et 20 %.

### Quelle est l'approche recommandée pour les comptages « uniques » ? {#whats-the-recommended-approach-for-unique-counts}

Lorsque vous mesurez un comportement unique (comme les cliqueurs ou convertisseurs uniques), l'unicité est appliquée par jour. Par exemple :

- Jour 1 : Clients ayant cliqué : A, B, C = 3 uniques
- Jour 2 : Clients ayant cliqué : B, C, D = 3 uniques

Le graphique affiche 3 au Jour 1 et 3 au Jour 2. Sur les deux jours, vous obtenez 3 + 3 = 6. Les clients B et C sont comptés une fois par jour, ce qui est intentionnel.

Cette configuration répond à la question : « Combien d'engagements clients uniques se sont produits sur l'ensemble des jours ? » Elle ne répond pas à : « Combien de clients individuels se sont engagés au moins une fois sur l'ensemble de la période ? »

Si votre objectif est l'unicité au niveau de la fenêtre (individus uniques sur l'ensemble d'une Campaign ou d'un trimestre), il s'agit d'une approche de modélisation différente. Contactez votre AI Success Manager pour obtenir des conseils sur sa conception.