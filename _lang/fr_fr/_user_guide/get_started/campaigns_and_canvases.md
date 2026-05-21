---
nav_title: Campagnes et Canvas
article_title: "Pour commencer : Campagnes et Canvas"
page_order: 3
page_type: reference
description: "Cet article donne un aperçu des différentes façons d'envoyer des messages avec Braze."

---

# Pour commencer : Campagnes et Canvas {#get-started-campaigns-and-canvases}

> Cet article donne un aperçu des différentes façons d'envoyer des messages avec Braze. Dans Braze, vous pouvez envoyer des messages par le biais d'une [campagne](#campaigns) ou d'un [Canvas](#canvas).

- Pour envoyer un message unique et ciblé à un groupe d'utilisateurs, choisissez une campagne. Une campagne est une étape de message unique pour entrer en contact avec vos utilisateurs sur différents canaux de communication.
- Pour envoyer une série de messages continus dans le cadre d'un parcours client global, choisissez Canvas, notre outil d'orchestration de parcours. Alors que les campagnes sont idéales pour envoyer des messages simples et ciblés, les Canvas vous permettent de faire passer vos relations avec les clients au niveau supérieur.

## Campagnes {#campaigns}

Bien que les campagnes puissent être conçues différemment selon le canal, il existe quatre types principaux de campagnes dans Braze que vous devez connaître :

| Type de campagne | Description |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Régulière | Il s'agit du type de campagne le plus courant. Vous pouvez cibler un ou plusieurs canaux en fonction de vos objectifs d'envoi de messages, et concevoir, personnaliser et tester votre contenu directement dans Braze grâce à nos éditeurs visuels. Découvrez comment [créer une campagne]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/). |
| Test A/B | Pour les campagnes ciblant un seul canal, vous pouvez envoyer plusieurs versions de la même campagne et voir laquelle obtient les meilleurs résultats. Vous pouvez tester le texte, la personnalisation et bien d'autres éléments pour un maximum de huit versions différentes dans le cadre d'une [campagne multivariée]({{site.baseurl}}/user_guide/messaging/ab_testing/). |
| API | Les [campagnes API]({{site.baseurl}}/api/api_campaigns/) vous permettent d'envoyer des messages opportuns le plus rapidement possible. Contrairement aux autres types de campagnes, vous ne spécifiez pas le message, les destinataires ou la planification dans le tableau de bord de Braze. Vous transmettez plutôt ces identifiants dans vos appels API. Elles sont généralement utilisées pour les messages transactionnels en temps réel ou les nouvelles de dernière minute. |
| E-mails transactionnels | Les [e-mails transactionnels]({{site.baseurl}}/user_guide/channels/email/) de Braze sont conçus pour envoyer des e-mails automatisés et non promotionnels afin de faciliter une transaction convenue entre vous et vos clients. Ils envoient à un seul utilisateur des notifications critiques où la rapidité est primordiale. *Disponible pour certains forfaits.* |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campagnes" }

{% alert note %}
Les campagnes régulières et les campagnes de test A/B peuvent être planifiées (par exemple, informer une liste d'utilisateurs d'un événement à venir) ou automatisées pour être envoyées en réponse à l'action d'un utilisateur (par exemple, envoyer un e-mail lorsqu'une personne s'abonne à votre newsletter). En savoir plus sur la [planification des campagnes]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).
{% endalert %}

Quel que soit le type de campagne que vous créez, vos campagnes peuvent être à l'écoute des besoins de vos utilisateurs et leur apporter une réponse réfléchie et personnalisée. Après avoir envoyé votre campagne, utilisez nos [outils analytiques intégrés]({{site.baseurl}}/user_guide/analytics/reports/) pour évaluer ses performances et mesurer le nombre d'utilisateurs ayant converti en fonction de vos [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/).

Consultez ces ressources supplémentaires pour en savoir plus sur les campagnes dans Braze :

- Braze Learning : [Configuration de la campagne](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [Créer une campagne]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/)
- [Idées et stratégies]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/)

## Canvas {#canvas}

Plutôt que d'envoyer des messages sporadiques au travers de plusieurs campagnes, les Canvas créent une conversation fluide et continue avec les utilisateurs. En effet, le parcours d'un utilisateur dans un Canvas peut se scinder en différents chemins en fonction de ses actions (ou inactions) avec votre marque, ce qui vous permet de faire avancer automatiquement les utilisateurs dans un flux spécifique en temps réel.

![]({% image_buster /assets/img/getting_started/canvas_flow.png %})

Ainsi, les Canvas sont parfaits pour rattraper les utilisateurs qui s'éloignent du chemin de la conversion et les orienter vers les initiatives de communication les plus efficaces.

Lorsque vous créez un Canvas, vous suivez en grande partie les mêmes étapes que pour la mise en place d'une campagne : spécification d'une audience globale, des conditions d'entrée et des paramètres d'envoi. Votre Canvas démarre lorsqu'un utilisateur correspond à votre condition de déclenchement. Il progresse ensuite dans le Canvas jusqu'à remplir vos conditions de sortie.

Votre Canvas peut comporter n'importe quelle combinaison de [messages]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/), de [délais]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/), d'[expériences]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/), et plus encore. Vous pouvez envoyer sur n'importe quel canal de communication pris en charge, et même [intégrer des plateformes sociales et publicitaires]({{site.baseurl}}/partners/canvas_audience_sync/overview/) telles que Facebook, Google ou TikTok.

Consultez ces ressources supplémentaires pour en savoir plus sur Canvas :

- Braze Learning : [Orchestration du parcours avec Canvas Flow](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [Créer un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/)
- [Grandes lignes du Canvas]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/canvas_outlines/)

## Canaux de communication {#messaging-channels}

Les canaux de communication sont les différents moyens par lesquels vous pouvez interagir avec vos clients et leur transmettre des messages ciblés.

![]({% image_buster /assets/img/getting_started/channels.png %})

Le tableau suivant présente les canaux pris en charge.

| Canal | Description |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [E-mail]({{site.baseurl}}/user_guide/channels/email/) | Envoyez des e-mails personnalisés dans la boîte de réception de vos utilisateurs. |
| [Notification push mobile]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/) | Envoyez des messages directement sur les appareils mobiles des utilisateurs sous forme de notifications. |
| [Notification push Web]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web/) | Envoyez des notifications aux navigateurs web des utilisateurs, même lorsqu'ils ne sont pas activement sur votre site web. |
| [Messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/) | Affichez des messages au sein de votre application mobile pendant que les utilisateurs l'utilisent activement. |
| [SMS, MMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/)* | Envoyez des messages textuels sur les téléphones mobiles des utilisateurs. |
| [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/)* | Envoyez des messages via la plateforme populaire WhatsApp pour atteindre et engager vos utilisateurs. |
| [Bannières]({{site.baseurl}}/user_guide/channels/banners/)* | Intégrez des messages directement dans votre application ou votre site web. |
| [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/)* | Proposez une boîte de réception au sein de votre application ou site web où les utilisateurs peuvent recevoir des messages et interagir avec eux, ou affichez des messages dans un carrousel, sous forme de bannière, et plus encore. |
| [Télévision connectée]({{site.baseurl}}/developer_guide/platforms/tv_and_ott/) | Interagissez avec les utilisateurs sur les plateformes de télévision connectées. |
| [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks/) | Permettez la communication et l'intégration en temps réel avec des systèmes externes grâce à des rappels HTTP personnalisés. |
| [LINE]({{site.baseurl}}/user_guide/channels/line/) | Interagissez avec les utilisateurs sur LINE, l'application de messagerie la plus populaire au Japon. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canaux de communication" }

<sup>*Disponible en tant que fonctionnalité supplémentaire.*</sup>

{% alert tip %}
Pour les messages courts et urgents qui peuvent être communiqués par la plupart des canaux (e-mail, SMS, push), profitez du filtre de [canal intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/) pour envoyer automatiquement le message par le meilleur canal pour chaque utilisateur.
{% endalert %}