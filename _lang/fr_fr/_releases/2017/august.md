---
nav_title: août
page_order: 5
noindex: true
page_type: update
description: "Cet article contient les notes de version d'août 2017."
---

# Août 2017 {#august-2017}

## Mise à jour des boutons d'action push {#update-to-push-action-buttons}

Nous avons ajouté la prise en charge des [boutons d'action push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_action_buttons/#how-to-use-action-buttons) à nos endpoints de messages de la REST API.

## Mise à jour du templating Liquid {#update-to-liquid-templating}

Vous pouvez désormais [personnaliser un message]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/) en fonction de :
- L'appareil auquel il a été envoyé,
- L'ID d'appareil,
- L'opérateur,
- L'IDFA,
- Le modèle,
- L'OS et
- La plateforme

## Canvas déclenché par API {#api-triggered-canvas}

Vous pouvez désormais déclencher un [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) via des endpoints API (envoyer, planifier, mettre à jour, supprimer) qui correspondent à ceux existants pour les campagnes, ce qui vous permet d'automatiser et d'optimiser davantage votre marketing.

## Boutons d'action push Web {#web-push-action-buttons}

Nous avons ajouté la prise en charge des boutons d'action push sur le SDK Web pour Chrome, ce qui vous permet d'augmenter votre engagement en offrant aux utilisateurs des choix contextuels qui leur simplifient la vie. Consultez les [meilleures pratiques en matière de notifications push]({{site.baseurl}}/user_guide/channels/push/best_practices/).

## Nouveaux endpoints API {#new-api-endpoints}

Nous avons exposé de nouveaux endpoints API, /email/hard_bounces, qui vous permet d'extraire les échecs d'envoi définitifs par adresse e-mail ou dans une plage de dates donnée, et /messages/scheduled_broadcasts, qui vous permet d'extraire la prochaine heure de début des campagnes planifiées et des Canvas à entrée planifiée. Ces nouveaux endpoints vous permettent de personnaliser et d'optimiser davantage vos campagnes. En savoir plus sur nos [endpoints API]({{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api).

## Géorepérages {#geofences}

Nous avons ajouté une nouvelle fonctionnalité, les géorepérages, qui vous permet de déclencher des messages en temps réel lorsque les clients entrent et sortent de zones géographiques définies, ce qui permet des communications personnalisées et pertinentes avec vos clients. En savoir plus sur le [marketing de localisation]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).

## Mise à jour de l'éditeur d'e-mail {#update-to-email-editor}

Pour vous faciliter la vie, nous avons ajouté l'autocomplétion dynamique à notre nouvel éditeur d'e-mails, pour renseigner automatiquement les attributs et les événements personnalisés réels de vos clients lorsque vous utilisez Liquid. En savoir plus sur les [meilleures pratiques en matière d'e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices/).

## Mise à jour des filtres de date {#update-to-date-filters}

Nous avons ajouté un filtre de date « jamais » pour que vous puissiez cibler les clients qui n'ont jamais reçu ou interagi avec l'un de vos messages, ce qui vous permet d'avoir des listes de clients propres et de garantir la livrabilité des e-mails. En savoir plus sur les [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters).

## Mise à jour de Canvas {#update-to-canvas}

Nous avons ajouté des pourcentages en haut de chaque variante de Canvas, pour que vous puissiez voir en un coup d'œil quelles variantes fonctionnent le mieux. En savoir plus sur [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/).

## Canvas avec Sélection intelligente {#canvas-with-intelligent-selection}

Canvas dispose désormais de la Sélection intelligente, ce qui vous permet de tester vos Canvas avec plus d'efficacité. En savoir plus sur notre [Intelligence Suite]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/).

## Mise à jour des noms d'affichage des e-mails {#update-to-email-display-names}

Nous avons ajouté la prise en charge des caractères UTF-8 spéciaux dans les noms d'affichage des e-mails, afin que vous puissiez créer des e-mails encore plus personnalisés pour vos clients. En savoir plus sur les [meilleures pratiques en matière d'e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices/).

## Agrégation CSV des rapports d'engagement {#engagement-reports-csv-aggregation}

Vous pouvez désormais recevoir des données consolidées pour chaque campagne et chaque Canvas dans deux fichiers distincts, quel que soit le nombre de campagnes ou de Canvas sélectionnés, pour avoir toutes les données dont vous avez besoin quand vous en avez besoin. En savoir plus sur les [rapports d'engagement]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/).

> Comme indiqué dans nos [notes de version de septembre 2017]({{site.baseurl}}/releases/2017/september/), vous pouvez désormais agréger les données d'une période spécifique ainsi que planifier des exportations à exécuter de manière récurrente.