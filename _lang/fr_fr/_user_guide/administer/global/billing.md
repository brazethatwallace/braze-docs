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

## Abonnements et utilisation {#subscriptions-and-usage}

L'onglet **Abonnements et utilisation** comprend des graphiques d'utilisation et les détails de votre contrat. Les données de cette page sont mises à jour quotidiennement à 22 h 00, heure de l'Est (ET). Elles ne reflètent pas l'activité en temps réel.

### Graphiques d'utilisation {#usage-graphs}

Vous trouverez ici des graphiques d'utilisation qui s'appliquent à vos espaces de travail. Votre propre tableau de bord peut afficher des indicateurs d'utilisation différents en fonction des produits que vous avez achetés.

![Graphique d'utilisation montrant les visiteurs uniques mensuels]({% image_buster /assets/img/subscription_and_billing4.png %}){: style="max-width:90%;"}

Ces graphiques peuvent afficher les utilisateurs actifs mensuels, les visiteurs uniques mensuels et les envois d'e-mails. Ce type de graphiques d'utilisation est particulièrement utile pour planifier votre consommation et mieux comprendre la contribution de chaque espace de travail à l'utilisation globale.

### Détails du contrat {#contract-details}

Les détails du contrat indiquent les dates de début et de fin de votre contrat actuel avec Braze.

#### Considérations {#considerations}

Si votre contrat utilise les visiteurs uniques mensuels (MUV) et que vous passez à un contrat utilisant uniquement les utilisateurs actifs mensuels (MAU), vos données historiques continuent d'apparaître dans le graphique MUV et vos nouvelles données apparaissent uniquement dans le graphique MAU. Par exemple, si votre contrat se termine en octobre, le graphique MUV affiche les données jusqu'à la fin du mois de septembre.

## Événements et attributs les plus utilisés par application {#most-used-events-and-attributes-by-app}

Sous **Most Used Events and Attributes By App**, vous pouvez consulter les facteurs qui influencent votre consommation de points de donnée liés aux attributs et aux événements personnalisés.

![Événements et attributs les plus utilisés par application]({% image_buster /assets/img/most_used_events_attributes_time.png %})

Pour chaque application, vous pouvez sélectionner **See breakdown** pour afficher un décompte estimé de chaque attribut personnalisé, attribut de profil et événement personnalisé pour la période sélectionnée, ainsi que le pourcentage des mises à jour d'attributs et d'événements de cette application qui ont été générées par cet attribut ou événement.

![Onglet de ventilation des événements et attributs les plus utilisés par application]({% image_buster /assets/img/most_used_events_attributes_2.png %}){: style="max-width:60%"}

Ces ventilations de données peuvent vous aider à comprendre quels points de donnée spécifiques représentent un pourcentage important de votre allocation. Nous vous recommandons de surveiller ces informations régulièrement afin de vous assurer que vous ne dépensez pas de points de donnée de manière accidentelle ou inutile. Votre gestionnaire de la satisfaction client peut vous fournir des conseils pour tirer le meilleur parti de votre forfait actuel ou vous proposer des options offrant une plus grande flexibilité.

## Tableau de bord du total des points de données {#total-data-points-dashboard}

L'onglet **Total Data Points Usage** fournit un aperçu détaillé de votre utilisation des points de données. Vous pouvez visualiser toutes les données de cette section agrégées par semaines ou par mois.

{% alert note %}
Les informations relatives aux points de données sont mises en cache toutes les 24 heures.
{% endalert %}

Si vous êtes administrateur et que vous ne pouvez pas voir l'onglet **Total Data Points Usage**, assurez-vous que votre navigateur autorise les cookies tiers pour le domaine de votre tableau de bord de Braze et qu'il n'est pas en mode navigation privée.

![Filtrage de l'utilisation des points de données par semaines]({% image_buster /assets/img/subscription_and_billing2.png %})

### Détails du contrat

Vous trouverez ici des informations sur les dates de début et de fin de votre contrat Braze actuel, ainsi que les points de données alloués et un total de tous les points de données utilisés jusqu'à présent dans le cadre de votre contrat actuel.

Les champs de cette section sont définis comme suit :

- **Contract Type :** Structure du terme de facturation, annuelle ou pluriannuelle.
- **Contract Start and End Date :** Date de début et de fin de l'ensemble du contrat.
- **Allotted Data Points :** Le nombre de points de données alloués dans le contrat par période de facturation.
- **Contract Data Point Usage :** Un total cumulé de tous les points de données enregistrés au cours de la durée de vie du contrat, qui ne se réinitialise pas lors de la période de facturation suivante.

### Données de facturation de l'entreprise {#company-billing-data}

#### Utilisation totale des points de données au niveau de l'application {#app-level-total-data-point-usage}

Ce graphique montre votre utilisation des points de données pour chaque application.

![L'utilisation totale des points de données au niveau de l'application montre les points de données utilisés pour chaque application.]({% image_buster /assets/img/app_level_total.png %})

Sélectionnez l'un des totaux pour afficher le tableau **Data Point Usage Over Time**, qui présente vos totaux hebdomadaires de points de données pour chaque espace de travail. Les lignes dont la colonne **App Name** est vide représentent des points de données qui ne sont associés à aucune application (comme les points de données utilisés dans des requêtes qui ne spécifient pas d'`app_id`).

![L'utilisation des points de données au fil du temps montrant les totaux hebdomadaires de points de données pour deux espaces de travail.]({% image_buster /assets/img/data_point_usage_time.png %})

#### Utilisation des points de données par espace de travail {#workspace-data-point-usage}

Ce graphique vous permet d'évaluer l'utilisation totale des points de données d'une entreprise par espace de travail. Il vous donne la possibilité d'évaluer la contribution de chaque espace de travail à l'utilisation des points de données de l'entreprise.

![Graphique de l'utilisation des points de données par espace de travail pour deux espaces de travail]({% image_buster /assets/img/appgroup_datapoint_usage.png %}){: style="max-width:90%;"}

#### Utilisation des points de données du cycle de facturation par source d'événement {#billing-cycle-data-point-usage-by-event-source}

Ce graphique vous permet de visualiser la répartition de l'utilisation des points de données entre les différentes sources d'événements, telles que les différents attributs d'API, les événements personnalisés et les sessions.

![L'utilisation des points de données du cycle de facturation par source d'événement affichant la répartition des points de données entre les différentes sources d'événements.]({% image_buster /assets/img/event_source_stats.png %})

#### Utilisation des points de données au fil du temps {#data-point-usage-over-time}

Ce graphique vous permet de visualiser rapidement votre utilisation totale des points de données par rapport à la quantité de points de données qui vous est allouée.

![L'utilisation des points de données au fil du temps comparant les points de données alloués pour le cycle de facturation en cours avec le total cumulé]({% image_buster /assets/img/company_data_point_usage_time.png %}){: style="max-width:90%;"}

## Étapes suivantes {#next-steps}

{% article_tiles %}
- name: Préférences de notification
  link: /docs/user_guide/administer/global/admin_settings/notification_preferences
- name: Tableau de bord de l'utilisation des crédits
  link: /docs/credits_usage_dashboard
{% endarticle_tiles %}