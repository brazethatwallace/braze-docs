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

# Comprendre les installations utilisateur

> Le suivi de l'attribution d'installation est un excellent moyen d'améliorer votre relation initiale avec vos utilisateurs. Savoir comment, où, et surtout pourquoi un utilisateur installe votre application vous permet de mieux comprendre qui il est et comment lui présenter votre application de la meilleure façon.

Braze ne fournit pas directement le suivi de l'attribution d'installation, mais peut s'intégrer à des [services]({{site.baseurl}}/partners/message_orchestration/) tels que Branch et AppsFlyer pour vous fournir de façon fluide des données d'installation.

## Segmenter vos utilisateurs

Une fois que l'utilisateur a installé votre application, vous pouvez commencer à le segmenter en fonction des [filtres d'attribution d'installation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#install-attribution) suivants. Par exemple, une application de voyage pourrait ajouter les utilisateurs provenant d'une publicité sur des offres de vacances à la plage dans un segment « Amoureux de la plage ». De la même manière, une application musicale pourrait segmenter les utilisateurs en fonction du genre musical affiché dans la publicité ayant conduit à l'installation.

## Bonnes pratiques

### Onboarding personnalisé

Maintenant que vous disposez de plus d'informations sur vos utilisateurs, vous pouvez personnaliser leur processus d'onboarding. Cela peut être aussi simple que de modifier les images de vos messages pour correspondre à leurs préférences, ou aussi complexe que de créer un parcours d'onboarding unique pour chaque publicité susceptible de mener à une installation. Pour déployer une séquence complète de messages prenant en compte le comportement des utilisateurs, consultez notre documentation sur [Canvas]({{site.baseurl}}/developer_guide/rest_api/messaging/#canvas).

### Exploiter les données de la publicité

Les utilisateurs peuvent être attirés par votre application grâce à une offre promotionnelle ou un cadeau. Les données d'attribution d'installation vous permettent d'envoyer des campagnes contenant des codes de réduction ou des offres uniquement aux utilisateurs ayant installé l'application grâce à ces promotions. De la même façon, si votre publicité contient des informations sur un produit particulier (comme un film spécifique dans une application vidéo ou une promotion dans une application e-commerce), vous pouvez envoyer des campagnes dirigeant les utilisateurs vers la bonne page de votre application.

## Évaluer l'efficacité de vos efforts publicitaires

Les données d'attribution d'installation sont précieuses pour évaluer l'efficacité de vos différentes campagnes marketing. Analyser quelles publicités et campagnes génèrent le plus d'installations, et lesquelles sont en retrait, vous permet de concentrer vos ressources sur les publicités les plus performantes.