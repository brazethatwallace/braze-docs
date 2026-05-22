---
nav_title: août
page_order: 6
noindex: true
page_type: update
description: "Cet article contient les notes de version d'août 2018."
---
# Août 2018 {#august-2018}

## Groupes de notification iOS 12 {#ios-12-notification-groups}

La version récente d'iOS 12 prend en charge le regroupement des notifications (similaire aux canaux de notification Android) pour les applications. [Braze vous permet d'utiliser cette fonctionnalité de regroupement dans iOS à l'aide de notre compositeur de messages.]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups)

## Déclenchement de Push Story {#push-story-triggering}

Vous pouvez désormais recibler les utilisateurs en fonction de clics sur des pages spécifiques des diapositives Push Story. Utilisez le filtre supplémentaire **Interacted with Campaign**.

## Événements de données S3 et Azure pour les utilisateurs anonymes {#s3-and-azure-data-events-from-anonymous-users}

 Les clients qui exportent des données vers Amazon S3 et Microsoft Azure peuvent désormais inclure des événements d'utilisateurs anonymes. Cette fonctionnalité sera activée par défaut pour toutes les intégrations nouvellement créées, mais restera désactivée pour toutes les intégrations existantes. Si vous avez des questions, contactez votre gestionnaire de compte ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/).

## Intégration des cohortes Mixpanel {#mixpanel-cohorts-integration}

Les clients de Braze et de Mixpanel peuvent désormais intégrer et [envoyer les cohortes Mixpanel vers Braze en tant que filtres de segment]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#mixpanel-cohort-import). Vous pouvez configurer une exportation manuelle unique ou une exportation dynamique toutes les deux heures. Chaque utilisateur mis à jour comptera comme un point de donnée, mais Mixpanel n'envoie que les modifications depuis la dernière synchronisation.