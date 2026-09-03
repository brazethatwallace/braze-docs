---
nav_title: Campaigns et Canvas
article_title: "Pour commencer : Campaigns et Canvas"
page_order: 3
page_type: reference
description: "Cet article donne un aperçu des différentes façons d'envoyer des messages avec Braze."
---

# Pour commencer : Campaigns et Canvas {#get-started-campaigns-and-canvases}

> Cet article donne un aperçu des différentes façons d'envoyer des messages avec Braze. Dans Braze, vous pouvez envoyer des messages par le biais d'une [Campaign](#campaigns) ou d'un [Canvas](#canvas).

- Pour envoyer un message unique et ciblé à un groupe d'utilisateurs, choisissez une Campaign. Une Campaign est une étape de message unique pour entrer en contact avec vos utilisateurs sur différents canaux de communication.
- Pour envoyer une série de messages continus dans le cadre d'un parcours client global, choisissez Canvas, notre outil d'orchestration de parcours. Alors que les Campaigns sont idéales pour envoyer des messages simples et ciblés, les Canvas vous permettent de faire passer vos relations avec les clients au niveau supérieur.

## Campaigns {#campaigns}

Bien que les Campaigns puissent être conçues de manière unique en fonction du canal, il existe quatre principaux types de Campaigns dans Braze dont vous devriez avoir connaissance :

| Type de Campaign     | Description                                                                                                                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Standard             | Il s'agit du type de Campaign le plus courant. Vous pouvez cibler un ou plusieurs canaux en fonction de vos objectifs de communication, et concevoir, personnaliser et tester votre contenu directement dans Braze avec nos éditeurs visuels. Découvrez comment [créer une Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign). |
| Test A/B             | Pour les Campaigns ciblant un seul canal, vous pouvez envoyer plusieurs versions d'une même Campaign et voir laquelle obtient les meilleurs résultats. Vous pouvez tester le texte, la personnalisation et bien plus encore pour jusqu'à huit versions différentes avec une [Campaign multivariée]({{site.baseurl}}/user_guide/messaging/ab_testing). |
| API                  | Les [Campaigns API]({{site.baseurl}}/api/api_campaigns) vous permettent d'envoyer des messages opportuns aussi rapidement que possible. Contrairement aux autres types de Campaigns, vous ne spécifiez pas le message, les destinataires ou la planification dans le tableau de bord de Braze. Au lieu de cela, vous transmettez ces identifiants dans vos appels API. Elles sont généralement utilisées pour les messages transactionnels en temps réel ou les informations urgentes.  |
| E-mails transactionnels | Les [e-mails transactionnels]({{site.baseurl}}/user_guide/channels/email) de Braze sont spécialement conçus pour envoyer des messages e-mail automatisés et non promotionnels afin de faciliter une transaction convenue entre vous et vos clients. Ils envoient des notifications critiques pour l'activité à un seul utilisateur lorsque la rapidité est de la plus haute importance. *Disponible pour certains forfaits.* |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaigns" }

{% alert note %}
Les Campaigns standard et les Campaigns avec test A/B peuvent être planifiées (par exemple pour informer une liste d'utilisateurs d'un événement à venir) ou automatisées pour être envoyées en réponse à l'action d'un utilisateur (par exemple envoyer un e-mail lorsqu'une personne s'abonne à votre newsletter). En savoir plus sur la [planification des Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).
{% endalert %}

Quel que soit le type de Campaign que vous créez, vos Campaigns peuvent s'adapter aux besoins de vos utilisateurs et leur fournir une réponse réfléchie et personnalisée. Après avoir envoyé votre Campaign, utilisez nos [outils d'analyse intégrés]({{site.baseurl}}/user_guide/analytics/reports) pour voir ses performances et combien d'utilisateurs ont converti en fonction de vos [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events).

Consultez ces ressources supplémentaires pour en savoir plus sur les Campaigns dans Braze :

- Braze Learning : [Configuration des Campaigns](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [Créer une Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign)
- [Idées et stratégies]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies)

## Canvas {#canvas}

Plutôt que d'envoyer des messages sporadiques à travers plusieurs Campaigns, les Canvas créent une conversation fluide et continue avec les utilisateurs. En effet, le parcours d'un utilisateur dans un Canvas peut se diviser en différents chemins en fonction de ses actions (ou de son inaction) avec votre marque, ce qui vous permet de faire avancer automatiquement les utilisateurs à travers un flux spécifique en temps réel.

![Diagramme de flux du processus décrit.]({% image_buster /assets/img/getting_started/canvas_flow.png %})

De cette manière, les Canvas sont idéaux pour ratisser large et capturer les utilisateurs qui s'écartent du chemin vers la conversion, puis les placer dans les initiatives de communication les plus efficaces.

Lorsque vous créez un Canvas, vous suivez bon nombre des mêmes étapes que pour la configuration d'une Campaign : définir une audience globale, des conditions d'entrée et des paramètres d'envoi. Votre Canvas démarre lorsqu'une personne correspond à votre condition de déclenchement. Elle progresse ensuite à travers un chemin dans le Canvas jusqu'à ce qu'elle remplisse vos conditions de sortie.

Votre Canvas peut combiner des [messages]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step), des [délais]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), des [expériences]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step), et bien plus encore. Vous pouvez envoyer sur n'importe quel canal de communication pris en charge, et même [intégrer des plateformes sociales et publicitaires]({{site.baseurl}}/partners/canvas_audience_sync/overview) telles que Facebook, Google ou TikTok.

Consultez ces ressources supplémentaires pour en savoir plus sur Canvas :

- Braze Learning : [Orchestration de parcours avec Canvas Flow](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [Créer un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)
- [Modèles de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/canvas_outlines)

## Canaux de communication {#messaging-channels}

Les canaux de communication sont les différents moyens par lesquels vous pouvez interagir avec vos clients et leur envoyer des messages ciblés.

![Schéma des canaux de communication Braze disponibles via le SDK.]({% image_buster /assets/img/getting_started/channels.png %})

Le tableau suivant présente les canaux pris en charge.

| Canal                                                                                              | Description                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [E-mail]({{site.baseurl}}/user_guide/channels/email)                        | Envoyez des e-mails personnalisés dans les boîtes de réception de vos utilisateurs.                                                                                                       |
| [Notification push mobile]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)                   | Envoyez des messages directement sur les appareils mobiles de vos utilisateurs sous forme de notifications.                                                                                   |
| [Notification push Web]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web)                         | Envoyez des notifications sur les navigateurs web de vos utilisateurs, même lorsqu'ils ne sont pas activement sur votre site web.                                                         |
| [In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages)    | Affichez des messages dans votre application mobile pendant que les utilisateurs l'utilisent activement.                                                                             |
| [SMS, MMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)*                   | Envoyez des messages texte sur les téléphones mobiles de vos utilisateurs.                                                                                                            |
| [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)*              | Envoyez des messages via la plateforme de messagerie populaire WhatsApp pour contacter et interagir avec vos utilisateurs.                                                   |
| [Bannières]({{site.baseurl}}/user_guide/channels/banners)*       | Intégrez des messages directement dans votre application ou votre site web. |
| [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)*       | Fournissez une boîte de réception au sein de votre application ou de votre site web où les utilisateurs peuvent recevoir des messages et interagir avec, ou affichez des messages dans un carrousel, sous forme de bannière, et plus encore. |
| [TV connectée]({{site.baseurl}}/developer_guide/platforms/tv_and_ott)                           | Interagissez avec vos utilisateurs sur les plateformes de télévision connectée.                                                                                                   |
| [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks) | Permettez la communication en temps réel et l'intégration avec des systèmes externes grâce à des rappels HTTP personnalisés.                                                    |
| [LINE]({{site.baseurl}}/user_guide/channels/line) | Interagissez avec vos utilisateurs sur LINE, l'application de messagerie la plus populaire au Japon.                                                    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canaux de communication" }

<sup>*Disponible en tant que fonctionnalité complémentaire.*</sup>

{% alert tip %}
Pour les messages courts et urgents pouvant être communiqués via la plupart des canaux (e-mail, SMS, notification push), tirez parti du filtre [Canal intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel) pour envoyer automatiquement le message via le meilleur canal pour chaque utilisateur.
{% endalert %}