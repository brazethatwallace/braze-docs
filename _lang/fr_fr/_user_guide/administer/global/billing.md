---
nav_title: Facturation
article_title: Facturation
alias: /subscription_and_usage/
page_order: 5
page_type: reference
description: "Cet article de référence couvre la page Facturation, où vous pouvez surveiller et vérifier votre consommation de données."
tool: Dashboard
search_rank: 5
---

# Facturation {#billing}

> Découvrez comment utiliser la page **Facturation** pour surveiller et vérifier votre consommation de données à travers les espaces de travail, les applications et les sources d'événements. Cet article présente les différentes sections de la page et les informations qu'elles mettent à votre disposition.

Pour accéder à la page **Facturation**, allez dans **Paramètres** > **Facturation**.

La page **Facturation** comprend les onglets suivants :

- [Abonnement et utilisation](#subscriptions-and-usage)
- [Événements et attributs les plus utilisés par application](#most-used-events-and-attributes-by-app)
- [Utilisation totale des points de données](#total-data-points-dashboard)

## Abonnement et utilisation {#subscriptions-and-usage}

L'onglet **Abonnement et utilisation** comprend des graphiques d'utilisation et les détails de votre contrat. Les données de cette page sont mises à jour quotidiennement à 22 h 00, heure de l'Est (ET). Elles ne reflètent pas l'activité en temps réel.

### Graphiques d'utilisation {#usage-graphs}

Vous trouverez ici des graphiques d'utilisation qui s'appliquent à vos espaces de travail. Votre propre tableau de bord peut afficher des indicateurs d'utilisation différents en fonction des produits que vous avez achetés.

![Graphique d'utilisation montrant les visiteurs uniques mensuels]({% image_buster /assets/img/subscription_and_billing4.png %}){: style="max-width:90%;"}

Ces graphiques peuvent afficher les utilisateurs actifs par mois, les visiteurs uniques mensuels et les envois d'e-mails. Ce type de graphiques est particulièrement utile pour planifier votre consommation et mieux comprendre quels espaces de travail contribuent à l'utilisation globale.

### Détails du contrat {#contract-details}

Les détails du contrat indiquent les dates de début et de fin de votre contrat actuel avec Braze.

#### Points d'attention {#considerations}

Si votre contrat utilise les visiteurs uniques mensuels (MUV) et que vous passez à un contrat utilisant uniquement les utilisateurs actifs par mois (MAU), vos données historiques apparaissent toujours dans le graphique MUV et vos nouvelles données apparaissent uniquement dans le graphique MAU. Par exemple, si votre contrat se termine en octobre, le graphique MUV affiche les données jusqu'à la fin du mois de septembre.

## Événements et attributs les plus utilisés par application {#most-used-events-and-attributes-by-app}

Sous **Événements et attributs les plus utilisés par application**, vous pouvez identifier les principaux facteurs de consommation de points de données liés à vos attributs et événements personnalisés.

![Événements et attributs les plus utilisés par application]({% image_buster /assets/img/most_used_events_attributes_time.png %})

Pour chaque application, vous pouvez sélectionner **See breakdown** pour afficher un décompte estimé de chaque attribut personnalisé, attribut de profil et événement personnalisé pour la période sélectionnée, ainsi que le pourcentage des mises à jour d'attributs et d'événements de cette application générées par cet attribut ou événement.

![Onglet de répartition des événements et attributs les plus utilisés par application]({% image_buster /assets/img/most_used_events_attributes_2.png %}){: style="max-width:60%"}

Ce type de répartition peut vous aider à comprendre quels points de données spécifiques représentent une part importante de votre allocation. Nous vous recommandons de consulter ces informations régulièrement pour vous assurer que vous ne consommez pas de points de données de manière accidentelle ou inutile. Votre gestionnaire de la satisfaction client peut vous guider pour tirer le meilleur parti de votre forfait actuel ou vous proposer des options offrant une plus grande flexibilité.

## Tableau de bord de l'utilisation totale des points de données {#total-data-points-dashboard}

L'onglet **Utilisation totale des points de données** offre un aperçu détaillé de votre consommation de points de données. Vous pouvez afficher toutes les données de cette section agrégées par semaines ou par mois.

{% alert note %}
Les informations relatives aux points de données sont mises en cache toutes les 24 heures.
{% endalert %}

Si vous êtes administrateur et que vous ne parvenez pas à afficher l'onglet **Utilisation totale des points de données**, assurez-vous que votre navigateur autorise les cookies tiers pour le domaine de votre tableau de bord de Braze et qu'il n'est pas en mode navigation privée.

![Filtrage de l'utilisation des points de données par semaines]({% image_buster /assets/img/subscription_and_billing2.png %})

### Détails du contrat

Vous trouverez ici les dates de début et de fin de votre contrat Braze actuel, ainsi que les points de données alloués et le total cumulé de tous les points de données utilisés jusqu'à présent dans le cadre de votre contrat.

Les champs de cette section sont définis comme suit :

- **Type de contrat :** Structure de la période de facturation, annuelle ou pluriannuelle.
- **Date de début et de fin du contrat :** Date de début et de fin de l'ensemble du contrat.
- **Points de données alloués :** Le nombre de points de données alloués dans le contrat par période de facturation.
- **Utilisation des points de données du contrat :** Total cumulé de tous les points de données enregistrés sur la durée de vie du contrat ; ce total ne se réinitialise pas lors de la période de facturation suivante.

![Section Détails du contrat de l'onglet Utilisation totale des points de données]({% image_buster /assets/img/contract_details.png %})

### Données de facturation de la société {#company-billing-data}

#### Utilisation totale des points de données au niveau de l'application {#app-level-total-data-point-usage}

Ce graphique affiche votre consommation de points de données par application.

![L'utilisation totale des points de données au niveau de l'application montre les points de données utilisés pour chaque application.]({% image_buster /assets/img/app_level_total.png %})

Sélectionnez l'un des totaux pour afficher le tableau **Utilisation des points de données au fil du temps**, qui présente les totaux hebdomadaires de points de données pour chaque espace de travail. Les lignes dont la colonne **Nom de l'application** est vide représentent des points de données qui ne sont associés à aucune application (par exemple, des points de données utilisés dans des requêtes qui ne spécifient pas d'`app_id`).

![Utilisation des points de données au fil du temps montrant les totaux hebdomadaires de points de données pour deux espaces de travail.]({% image_buster /assets/img/data_point_usage_time.png %})

#### Utilisation des points de données par espace de travail {#workspace-data-point-usage}

Ce graphique vous permet d'évaluer l'utilisation totale des points de données d'une société par espace de travail. Il vous aide à déterminer la contribution de chaque espace de travail à la consommation globale de points de données.

![Graphique d'utilisation des points de données par espace de travail pour deux espaces de travail]({% image_buster /assets/img/appgroup_datapoint_usage.png %}){: style="max-width:90%;"}

#### Utilisation des points de données du cycle de facturation par source d'événement {#billing-cycle-data-point-usage-by-event-source}

Ce graphique vous permet de visualiser la répartition de l'utilisation des points de données entre les différentes sources d'événements, telles que les attributs API, les événements personnalisés et les sessions.

![Utilisation des points de données du cycle de facturation par source d'événement affichant la répartition des points de données entre les différentes sources d'événements.]({% image_buster /assets/img/event_source_stats.png %})

#### Utilisation des points de données au fil du temps {#data-point-usage-over-time}

Ce graphique vous permet de visualiser rapidement votre consommation totale de points de données par rapport à votre allocation.

![Utilisation des points de données au fil du temps comparant les points de données alloués pour le cycle de facturation en cours avec le total cumulé]({% image_buster /assets/img/company_data_point_usage_time.png %}){: style="max-width:90%;"}

## Étapes suivantes {#next-steps}

- [Préférences de notification]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences/) pour configurer des alertes relatives aux événements de facturation et aux seuils d'utilisation.
- [Tableau de bord de l'utilisation des crédits]({{site.baseurl}}/credits_usage_dashboard/) pour surveiller la consommation de crédits de messages.