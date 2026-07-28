---
nav_title: septembre
page_order: 4
noindex: true
page_type: update
description: "Cet article contient les notes de version de septembre 2017."
---

# Septembre 2017 {#september-2017}

## Nouvelle fonctionnalité pour les rapports d'engagement {#new-functionality-for-engagement-reports}

Vous pouvez désormais utiliser les [rapports d'engagement]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports#engagement-reports) pour regrouper les indicateurs d'une campagne sur des périodes spécifiques. Par exemple, vous pouvez exporter le nombre total d'ouvertures d'un trimestre ou le nombre total de clics de toute la durée de vie d'une campagne ou d'un Canvas. Tout ce que vous avez à faire, c'est :
- Sélectionner une période pour l'exportation des données,
- Planifier un rapport d'engagement envoyé régulièrement à un ou plusieurs destinataires, et
- Ajouter des campagnes et des Canvas à votre rapport en fonction de leurs étiquettes.

## Mises à jour de la page de profil utilisateur {#updates-to-user-profile-page}

La [page du profil utilisateur]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles) a été mise à jour.

## Notifications push Web nécessitant une action de l'utilisateur pour le rejet {#web-push-notifications-that-require-user-action-to-dismiss}

Vous pouvez maintenant configurer le comportement de fermeture des messages push Web sur Chrome de façon à exiger que le destinataire interagisse avec le message pour pouvoir le fermer. Cette fonctionnalité nécessite la version 1.6.13 ou ultérieure du SDK Web.

## Accroches d'e-mail {#email-preheaders}

Lors de la création d'un e-mail dans Braze, vous pouvez désormais facilement insérer une accroche dans la section **Sending Info**.

## Nouvel endpoint d'API pour l'exportation d'événements bruts {#new-api-endpoint-for-raw-event-export}

Nous avons ajouté un nouvel [endpoint d'API]({{site.baseurl}}/developer_guide/rest_api/api_network_connectivity_issues#whitelisting-brazes-api-endpoint-ip-ranges), `/raw_data/status`, qui vous permet de vérifier si les données d'un jour donné ont été chargées dans l'exportation d'événements bruts (Raw Event Export). Vous pouvez l'utiliser pour vérifier si les données brutes d'un jour particulier sont disponibles, afin de faciliter le débogage et l'automatisation.