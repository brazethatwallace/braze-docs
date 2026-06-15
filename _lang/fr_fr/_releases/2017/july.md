---
nav_title: juillet
page_order: 6
noindex: true
page_type: update
description: "Cet article contient les notes de version de juillet 2017."
---

# Juillet 2017 {#july-2017}

## Grandes images dans les notifications push Web {#large-images-in-web-push}

Nous avons ajouté la prise en charge des grandes images pour les notifications push Web sur Chrome pour Windows et Android, vous permettant de créer des expériences client riches et engageantes. En savoir plus sur les [notifications push Web]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web/).

## Mises à jour des champs d'e-mail {#updates-to-email-fields}

Vous pouvez maintenant verrouiller les e-mails sur un ensemble spécifique d'adresses d'expédition, afin d'éviter de saisir accidentellement une adresse erronée. Le formulaire de composition d'e-mail sera prérempli avec les adresses utilisées au cours des 6 derniers mois pour simplifier le processus. Pour plus d'informations, consultez les [bonnes pratiques en matière d'e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices/).

## Mises à jour de l'endpoint /campaign/details de l'API {#updates-to-campaign-details-api}

L'endpoint `/campaign/details` fournit désormais des informations sur ses messages, ce qui vous permet d'extraire les champs sujet, corps HTML, adresse d'expédition et adresse de réponse à l'aide de l'API. En savoir plus sur les [API de Braze]({{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api).

## Mises à jour du templating Liquid {#updates-to-liquid-templating}

Nous avons ajouté la possibilité de modéliser des attributs de variante dans les Canvas et les campagnes. Dans Canvas, vous pouvez maintenant modéliser l'ID API de la variante ainsi que le nom de la variante, et dans les campagnes, vous pouvez maintenant modéliser le `message_api_id` et le `message_name` d'un message. Ces deux mises à jour vous offrent plus de flexibilité dans vos communications, en vous permettant de créer des campagnes personnalisées. En savoir plus sur l'[envoi de messages personnalisés]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/).

## Nouvel éditeur HTML pour les e-mails {#new-html-email-editor}

Vous pouvez désormais écrire et tester facilement des e-mails avec un éditeur HTML plein écran qui permet la prévisualisation instantanée, la personnalisation via Liquid et un éditeur de texte plein écran amélioré avec des numéros de lignes et une coloration syntaxique. En savoir plus sur la [composition des e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template).

## Mises à jour de la prévisualisation {#updates-to-previews}

Vous pouvez maintenant suivre la fenêtre d'écran lorsque vous faites défiler les aperçus des messages dans les campagnes et les Canvas, afin de toujours voir les modifications reflétées. En savoir plus sur la [prévisualisation et les tests]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message).

## Nouveau filtre d'appartenance à un segment {#new-segment-membership-filter}

Nous avons ajouté le [filtre d'appartenance à un segment]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters), qui vous permet de cibler les utilisateurs en fonction de leur appartenance à l'un de vos segments existants. De plus, nous avons ajouté la possibilité d'utiliser les opérateurs « Et » et « Ou » dans les filtres de segment, ainsi que la capacité d'imbriquer des segments les uns dans les autres. Ces mises à jour vous permettent d'envoyer des messages personnalisés à vos clients avec plus de précision.

## Mise à jour de la prévisualisation Android {#update-to-android-preview}

Nous avons mis à jour l'[aperçu Android]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message) pour refléter les versions plus récentes d'Android depuis Android N.