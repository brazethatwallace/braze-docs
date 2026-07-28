---
page_order: 0
nav_title: Accueil
article_title: Partenaires technologiques
alias: /partners/partners/
layout: dev_guide
search_tag: Partner
description: "Explorez les partenaires technologiques de Braze (Alloys) par catégorie. Retrouvez la documentation d'intégration pour la personnalisation, l'orchestration, les données, le eCommerce, Audience Sync et bien plus."

guide_top_header: "Partenaires technologiques"
guide_top_text: "Bienvenue dans la documentation des partenaires technologiques Braze Alloys. Parcourez les catégories de partenaires pour accéder aux guides d'intégration technique.<br><br>Pour une liste complète et filtrable de tous les partenaires technologiques de Braze, consultez le <a href='https://marketplace.braze.com/t/type/technology-partner'>Braze Marketplace</a>. Vous souhaitez rejoindre notre communauté de clients qui utilisent Braze pour moderniser leur expérience client ? Découvrez notre <a href='https://brazefirebrands.splashthat.com/'>programme Customer Champions</a>."

guide_featured_title: "Catégories de partenaires"
guide_featured_list:
  - name: Personnalisation des messages
    link: /docs/partners/message_personalization
    image: /assets/img/braze_icons/magic-wand-02.svg
  - name: Orchestration des messages
    link: /docs/partners/message_orchestration
    image: /assets/img/braze_icons/send-01.svg
  - name: Données et analyse
    link: /docs/partners/data_and_analytics
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: Canvas Audience Sync
    link: /docs/partners/canvas_audience_sync
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: eCommerce
    link: /docs/partners/ecommerce
    image: /assets/img/braze_icons/shopping-cart-03.svg
  - name: Canaux et extensions supplémentaires
    link: /docs/partners/additional_channels_and_extensions
    image: /assets/img/braze_icons/puzzle-piece-01.svg
  - name: Fournisseurs de modèles d'IA
    link: /docs/partners/ai_model_providers
    image: /assets/img/braze_icons/stars-01.svg
---

## Résolution des problèmes de connexion aux partenaires {#troubleshooting-partner-connections}

Si l'intégration nécessite une configuration côté Braze, connectez-vous à votre tableau de bord de Braze et accédez à **Intégrations partenaires** > **Partenaires technologiques**.

{% alert note %}
Les intégrations entièrement gérées par le partenaire peuvent ne pas être répertoriées ici. Consultez la documentation spécifique au partenaire pour vérifier la propriété de l'intégration et les étapes de configuration.
{% endalert %}

Si vous voyez **Identifiants non valides** pour un partenaire dans Braze alors que l'intégration semble correcte dans le tableau de bord de ce partenaire, déconnectez puis reconnectez l'intégration sur la page Partenaires technologiques et vérifiez les clés API, les jetons OAuth et les autorisations côté partenaire.

Certains tableaux de bord externes (par exemple, les outils de livrabilité ou de surveillance de la boîte de réception) peuvent afficher un état de connexion ou de vérification différent de celui de la page Partenaires technologiques de Braze. Utilisez la vignette du partenaire dans Braze pour connaître l'état de connexion sur lequel Braze s'appuie pour la synchronisation et l'envoi.