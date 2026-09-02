---
nav_title: juillet
page_order: 6
noindex: true
page_type: update
description: "Cet article contient les notes de version de juillet 2016."
---

# Juillet 2016 {#july-2016}

## Filtrage du journal des erreurs de la console de développement par type d'erreur {#filtering-the-developer-consoles-error-log-by-error-type}

Cette mise à niveau facilite l'utilisation du journal d'erreurs des messages sur la console de développement pour résoudre les problèmes liés aux intégrations Braze. Cette mise à jour vous permet de filtrer le journal d'erreurs des messages par type, ce qui simplifie considérablement la recherche et l'identification de problèmes d'intégration spécifiques.

## Horodatage ajouté pour la dernière notification push de suivi de désinstallation envoyée {#added-timestamp-for-last-uninstall-tracking-push-sent}

Braze détecte les désinstallations en envoyant un push silencieux aux applications d'un client pour voir quels appareils répondent. Cette fonctionnalité ajoute un horodatage discret indiquant la dernière exécution du suivi de désinstallation. Cet horodatage est disponible sur la page Paramètres où le suivi de désinstallation est configuré. En savoir plus sur le [suivi de désinstallation]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/).

![Case à cocher Suivi des désinstallations]({% image_buster /assets/img_archive/uninstall_tracking_checkbox.png %})

## Améliorations des tests de webhook {#added-webhook-testing-enhancements}

Vous pouvez maintenant envoyer un webhook de test en direct or en ligne/en production/instantané à partir de Braze avant de lancer une campagne. L'envoi d'un message de test vous permettra de vérifier que vos messages et vos endpoints serveur ont été configurés correctement dans un environnement sandbox sécurisé. En savoir plus sur les [webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook).

## Ajout de la variation de message reçue à l'exportation CSV des destinataires de campagne {#added-message-variation-received-to-campaign-recipients-csv-export}

Nous avons ajouté une colonne indiquant la variation de message reçue à l'exportation CSV des destinataires de campagne. En savoir plus sur l'[exportation de données]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/) depuis Braze.

## Limite approximative du nombre d'impressions {#approximate-limit-on-number-of-impressions}

Une fois qu'un message in-app a reçu un certain nombre d'impressions, Braze empêche les utilisateurs de devenir éligibles à la réception du message. En savoir plus sur la définition de [limites approximatives pour les impressions]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#setting-a-max-impression-cap).

![Limite d'impressions IAM]({% image_buster /assets/img_archive/approx_limit_for_IAM.png %})