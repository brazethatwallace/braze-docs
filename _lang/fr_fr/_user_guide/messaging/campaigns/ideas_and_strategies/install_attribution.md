---
nav_title: Comprendre les installations utilisateur
article_title: Comprendre les installations utilisateur
page_order: 7
page_type: reference
description: "Cet article de référence décrit les installations utilisateur (suivi de l'attribution d'installation) et les différentes façons d'exploiter ces informations dans vos campagnes."
tool:
  - Campaigns
  - Segments
---

# Comprendre les installations utilisateur {#understanding-user-installs}

> Le suivi de l'attribution d'installation est un excellent moyen d'améliorer votre relation initiale avec vos utilisateurs. Savoir comment, où, et surtout pourquoi un utilisateur installe votre application vous permet de mieux comprendre qui il est et comment lui présenter votre application de la meilleure façon.

Braze ne fournit pas directement le suivi de l'attribution d'installation, mais peut s'intégrer à des [services]({{site.baseurl}}/partners/message_orchestration) tels que Branch or branche et AppsFlyer pour vous fournir de façon fluide des données d'installation.

## Segmentez vos utilisateurs {#segment-your-users}

Une fois que votre utilisateur a installé votre application, vous pouvez commencer à le segmenter en fonction des [filtres d'attribution d'installation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#install-attribution) suivants. Par exemple, une application de voyage pourrait ajouter les utilisateurs provenant d'une publicité liée à des offres de vacances à la plage dans un Segment « Amoureux de la plage ». De même, une application musicale pourrait segmenter les utilisateurs en fonction du genre musical affiché dans la publicité ayant conduit à l'installation.

## Bonnes pratiques {#best-practices}

### Onboarding personnalisé {#personalized-onboarding}

Maintenant que vous disposez de plus d'informations sur votre utilisateur, vous pouvez personnaliser son processus d'onboarding. Cela peut être aussi simple que de modifier les images de vos messages pour correspondre à ses préférences, ou aussi complexe que de créer un onboarding unique pour chaque publicité susceptible de mener à une installation. Pour déployer une séquence complète de messages prenant en compte le comportement des utilisateurs, consultez notre documentation sur [Canvas]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).

### Exploiter les données publicitaires {#reference-data-from-the-ad}

Les utilisateurs peuvent être attirés par votre application grâce à une offre promotionnelle ou un cadeau. L'utilisation des données d'attribution d'installation vous permet d'envoyer des Campaigns contenant des codes de réduction ou des offres uniquement aux utilisateurs ayant installé l'application grâce à ces promotions. De la même manière, si votre publicité contient des informations sur un produit particulier (comme un film spécifique dans une application vidéo ou une vente dans une application d'e-commerce), vous pouvez envoyer des Campaigns dirigeant les utilisateurs vers la bonne page de votre application.

## Évaluer les efforts publicitaires {#evaluate-advertising-efforts}

Les données d'attribution d'installation peuvent s'avérer précieuses pour évaluer l'efficacité de différentes campagnes marketing. Examiner quelles publicités et campagnes génèrent le plus d'installations et lesquelles sont en retrait permet de concentrer vos ressources sur les publicités les plus performantes.