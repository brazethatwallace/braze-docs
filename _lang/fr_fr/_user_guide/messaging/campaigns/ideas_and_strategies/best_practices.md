---
nav_title: Bonnes pratiques
article_title: Bonnes pratiques pour les campagnes
page_order: 0
description: "Cet article présente les bonnes pratiques pour créer et personnaliser vos campagnes."
tool: Campaign

---

# Bonnes pratiques pour les campagnes {#campaign-best-practices}

> Cet article présente les bonnes pratiques pour créer et personnaliser vos campagnes.

## Les quatre T de Braze {#four-ts-of-braze}

Braze vous recommande de n'envoyer que les données client que vous avez l'intention d'utiliser sur la plateforme Braze. Inspirez-vous de la philosophie des « quatre T de Braze » pour vous assurer de n'envoyer que les données qui vous serviront à :

- **Target (Cibler)** vos audiences en créant des [segments d'audience]({{site.baseurl}}/user_guide/audience/segments/).
- **Trigger (Déclencher)** vos messages avec une distribution [basée sur des actions]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/#action-based-delivery) ou [déclenchée par API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/).
- **Template (Modéliser)** et personnaliser vos messages grâce à la [logique conditionnelle Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/).
- **Track (Suivre)** l'efficacité de vos campagnes avec le [suivi des conversions]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/).

Cela vous permet d'optimiser les données envoyées à Braze et de simplifier l'envoi de messages à vos utilisateurs, tout en évitant de suivre des points de donnée que votre équipe ne jugera pas utiles à long terme.

## Ciblage des utilisateurs {#user-targeting}

Au fil du développement de vos campagnes, vous pourriez constater un déclin de votre audience. À ce moment crucial, vous pouvez cibler vos [utilisateurs en perte d'engagement]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/capturing_lapsing_users/) avec une campagne spécialisée utilisant la segmentation.

### Identifiez votre audience {#identify-your-audience}

Tirez parti des segments et des filtres en définissant votre audience. Réfléchissez à qui votre campagne et vos messages s'adressent. Grâce à ces informations clés, vous pouvez créer des [campagnes multicanales]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/#multichannel-campaigns) offrant la flexibilité de concevoir vos messages sur différents canaux en fonction des préférences de notification de votre audience.

Il est également important de bien comprendre vos [utilisateurs actifs]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/active_user_campaigns/) afin de montrer votre reconnaissance envers vos utilisateurs les plus fidèles.

## Campagnes multicanales {#multichannel-campaigns}

### Mise en avant des fonctionnalités {#feature-awareness}

Si votre objectif est d'attirer l'attention de vos utilisateurs sur une nouvelle fonctionnalité ou une nouvelle version de l'application, adoptez une stratégie multicanale axée sur les canaux in-app. Les [messages in-app]({{site.baseurl}}/in-app_messages/) et les [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/) sont généralement moins intrusifs si l'utilisateur ne souhaite pas effectuer la mise à jour immédiatement.

N'oubliez pas d'inclure des [liens profonds]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/) vers la boutique d'applications appropriée.

Convaincre les utilisateurs de mettre à jour leur application ou de changer leurs habitudes d'utilisation peut s'avérer difficile. Présentez-leur tous les avantages de la nouvelle version ou des nouvelles fonctionnalités, et montrez-leur en quoi cela améliorera leur expérience.

### Moment d'envoi {#send-timing}

Le timing est essentiel ! Lorsque votre objectif est de convaincre les utilisateurs de mettre à jour leur application, attendez qu'ils vivent une expérience positive au sein de l'application avant de leur faire la demande. Pour maintenir l'engagement de votre audience, évitez les messages répétitifs qui pourraient paraître intrusifs.

Avec le temps, vos utilisateurs peuvent oublier certaines fonctionnalités ou ne pas remarquer les nouveautés. Lorsque de nouvelles fonctionnalités sont ajoutées, informez-en vos utilisateurs à l'aide de [messages in-app]({{site.baseurl}}/in-app_messages/). Si les utilisateurs n'interagissent pas avec des fonctionnalités majeures de l'application, il peut être judicieux de leur envoyer un rappel lorsqu'ils utilisent votre application et que cette nouvelle fonctionnalité leur serait utile. Notre article sur l'[abonnement aux données]({{site.baseurl}}/user_guide/channels/content_cards/) contient plus d'informations pour vous assurer que votre demande s'intègre bien dans le flux de travail de vos utilisateurs.

## Obtenir de bonnes notes {#high-ratings}

Obtenir des notes de cinq étoiles sur les boutiques d'applications figure sur la liste de souhaits de chaque marketeur mobile. Cependant, obtenir des avis positifs n'est pas chose facile, car cela demande un effort supplémentaire de la part de vos utilisateurs. En exploitant nos fonctionnalités de manière astucieuse, nous pouvons vous aider à renforcer votre engagement client.

### Cibler les utilisateurs les plus actifs {#targeting-power-users}

Les utilisateurs les plus actifs peuvent devenir de véritables ambassadeurs de votre application. Ils interagissent régulièrement avec votre application et peuvent fournir des retours précieux pour l'améliorer. Bien qu'ils varient d'une application à l'autre, ces utilisateurs ont généralement les caractéristiques suivantes :

- Un grand nombre de sessions enregistrées
- Une utilisation récente de l'application
- Des dépenses et des achats effectués

Pour obtenir de meilleures notes, demandez à vos utilisateurs les plus actifs de laisser un avis sur la boutique d'applications, car ils sont plus susceptibles d'avoir des choses positives à dire. Par exemple, vous pourriez créer un segment nommé « Utilisateurs les plus actifs » avec les filtres suivants :
- A utilisé ces applications plus de 10 fois au cours des 14 derniers jours
- A dépensé plus de 50 dollars

![Exemple de segment ciblant les utilisateurs les plus actifs d'une application.]({% image_buster /assets/img_archive/ratings_power_users.png %})

Se rendre sur la boutique d'applications prend du temps à vos utilisateurs. Pour maximiser la probabilité qu'ils fassent cet effort supplémentaire, demandez-leur de laisser une note ou un avis juste après une expérience positive avec votre application. Par exemple, demandez-leur après avoir terminé un niveau de jeu ou après un achat effectué avec un code de réduction. Notre article sur l'[abonnement aux données]({{site.baseurl}}/user_guide/channels/email/subscriptions/#subscription-states) contient plus d'informations sur les moyens de vous assurer que votre demande s'intègre bien dans le flux de travail de vos utilisateurs.

## Planifier vos campagnes {#scheduling-your-campaigns}

Lorsque vous modifiez la planification ou l'audience d'une campagne, gardez à l'esprit les bonnes pratiques suivantes :

- **Campagnes planifiées ponctuelles :** vous pouvez modifier la campagne jusqu'à l'heure d'envoi prévue.
- **Campagnes planifiées récurrentes :** vous pouvez modifier la campagne jusqu'à l'heure d'envoi prévue.
- **Campagnes avec heure d'envoi locale :** n'effectuez pas de modifications dans les 24 heures précédant l'heure d'envoi prévue.
- **Campagnes avec heure d'envoi optimale :** n'effectuez pas de modifications dans les 24 heures précédant minuit le jour où la campagne est planifiée.

{% alert note %}
Modifier une campagne en production et changer la distribution en **Heure d'envoi locale** entraînera la mise en file d'attente d'un nouveau lot de messages, ce qui signifie que vos utilisateurs recevront le message deux fois en raison de la double mise en file d'attente. Pour éviter cela, arrêtez d'abord la campagne d'origine, puis lancez un duplicata après avoir mis à jour la planification.
{% endalert %}