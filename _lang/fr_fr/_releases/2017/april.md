---
nav_title: avril
page_order: 9
noindex: true
page_type: update
description: "Cet article contient les notes de version d'avril 2017."
---

# Avril 2017 {#april-2017}

## Messages HTML dans le navigateur {#html-in-browser-messages}

Nous prenons désormais en charge les types de messages interactifs dans le navigateur, y compris les formats HTML personnalisés et de capture d'e-mail, vous permettant d'atteindre vos clients où qu'ils se trouvent. En savoir plus sur les [messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices).

## Message in-app personnalisé avec contenu connecté {#personalized-in-app-message-with-connected-content}

Nous avons ajouté les blocs {% raw %} {%connected_content%} {% endraw %} dans les messages in-app déclenchés, ce qui vous permet d'ajouter une personnalisation riche en insérant toute information accessible via l'API directement dans vos messages. Vous pouvez maintenant utiliser le contenu connecté à l'intérieur de votre application en plus de vos notifications push, e-mails et webhooks. En savoir plus sur le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content).

## Navigation améliorée pour les cartes de fil d'actualité {#improved-navigation-for-news-feed-cards}

Nous avons amélioré l'interface utilisateur pour la création de cartes de fil d'actualité afin de faciliter la navigation et la création de vos campagnes. En savoir plus sur les [cartes de fil d'actualité]({{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item#news-feed-cards).

## Prévisualisation améliorée pour les notifications riches iOS {#improved-preview-for-ios-rich-notifications}

Notre prévisualisation des notifications sur iOS affiche désormais les notifications riches, vous offrant une vue claire de ce que vous envoyez exactement à vos clients, jusqu'à la taille de police. En savoir plus sur les [notifications riches iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#ios-10-rich-notifications).

## Ajout des « ouvertures influencées » aux statistiques push {#added-influenced-opens-to-push-statistics}

Nous avons ajouté les « ouvertures influencées » à notre liste de statistiques standard pour les Campaigns et Canvas proposées dans Braze, facilitant ainsi la répartition de vos ouvertures influencées, directes et totales. En savoir plus sur les [ouvertures influencées]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens).

## Mise à niveau des groupes internes {#upgrade-to-internal-groups}

Vous pouvez maintenant créer plusieurs groupes internes et attribuer des propriétés indiquant si le groupe sera utilisé pour la journalisation SDK, la journalisation REST API ou les tests de contenu des messages. En savoir plus sur les [journaux des événements utilisateurs]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab#event-user-log-tab).

> Mise à jour : les groupes internes peuvent également être utilisés pour [envoyer des e-mails initiateurs]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console#seed-groups).

## Nouvelles options pour les URL web {#new-options-for-web-urls}

Vous avez maintenant la possibilité d'ouvrir des URL web dans un navigateur web externe pour les messages push, les messages in-app et dans le navigateur, ainsi que les cartes de fil d'actualité. L'action « Deep link dans l'application » est désormais compatible avec les deep links HTTP/HTTPS. Si vous utilisez un partenaire comme Branch or branche ou les Universal Links d'Apple, une personnalisation du SDK sera nécessaire. En savoir plus sur la [création de liens profonds]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#what-is-deep-linking).

## Nouvel événement « Performed Conversion » dans Canvas {#new-performed-conversion-event-canvas}

Nous avons ajouté un nouvel événement « Performed Conversion » et un filtre « In Canvas Control » pour améliorer vos options de reciblage. En savoir plus sur l'utilisation des [filtres de reciblage]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns).