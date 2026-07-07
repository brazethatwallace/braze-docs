---
nav_title: Commencer
article_title: Premiers pas avec Decisioning Studio
layout: dev_guide
guide_top_header: "Premiers pas avec Decisioning Studio"
guide_top_text: ""
page_order: 0
search_rank: 2
page_type: landing
description: "Cette section présente Decisioning Studio et explique comment l'utiliser pour concevoir et déployer des agents de décision qui optimisent n'importe quel indicateur métier."

guide_featured_title: "Articles de la section"
guide_featured_list:
  - name: Concevoir votre agent
    link: /docs/user_guide/brazeai/decisioning_studio/design_agents
    image: /assets/img/braze_icons/settings-01.svg
  - name: Préparer vos données
    link: /docs/user_guide/brazeai/decisioning_studio/prepare_data
    image: /assets/img/braze_icons/database-01.svg
  - name: Définir votre audience
    link: /docs/user_guide/brazeai/decisioning_studio/audience
    image: /assets/img/braze_icons/users-01.svg
  - name: Configurer l'orchestration
    link: /docs/user_guide/brazeai/decisioning_studio/orchestration_setup
    image: /assets/img/braze_icons/dataflow-04.svg

guide_menu_title: "Ressources supplémentaires"
guide_menu_list:
  - name: À propos de Decisioning Studio
    link: /docs/user_guide/brazeai/decisioning_studio
    image: /assets/img/braze_icons/info-circle.svg
  - name: FAQ de Decisioning Studio
    link: /docs/user_guide/brazeai/decisioning_studio/faq
    image: /assets/img/braze_icons/annotation-question.svg
---

BrazeAI Decisioning Studio™ vous permet de concevoir et de déployer des agents de décision qui optimisent n'importe quel indicateur métier.

Cette référence donne un aperçu des étapes nécessaires à la mise en place de Decisioning Studio, notamment la conception de votre agent, la configuration et la connexion des sources de données, la mise en place de l'orchestration et l'évaluation des performances.

## Décisions clés de conception {#key-design-decisions}

Travaillez avec l'équipe AI Decisioning Services pour prendre les décisions suivantes :

| Décision | Description | Exemples |
|----------|-------------|----------|
| **Indicateur de réussite** | Que l'agent doit-il maximiser lors de la personnalisation de l'engagement client ? | Chiffre d'affaires, LTV, ARPU, conversions, rétention |
| **Audience** | Pour qui l'agent Decisioning Studio prendra-t-il des décisions d'engagement client ? | Tous les clients, membres fidélité, abonnés à risque |
| **Groupes d'expérience** | Comment les essais contrôlés randomisés de Decisioning Studio doivent-ils être structurés ? | Decisioning Studio, contrôle aléatoire, BAU, groupe de contrôle |
| **Dimensions** | Quelles décisions l'agent doit-il personnaliser ? | Heure de la journée, ligne d'objet, fréquence, offres, canal |
| **Options** | Quelles options l'agent a-t-il à sa disposition ? | Modèles spécifiques, offres, créneaux horaires |
| **Contraintes** | Quelles décisions l'agent ne doit-il jamais prendre ? | Restrictions géographiques, limites budgétaires, règles d'éligibilité |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Décisions clés de conception" }

Chacune de ces décisions a des implications sur le gain incrémental que l'agent peut générer, et sur la rapidité avec laquelle il y parvient. Notre équipe AI Decisioning Services travaillera avec vous pour concevoir un agent qui génère une valeur maximale tout en respectant l'ensemble de vos règles métier.

![Diagramme montrant comment les indicateurs de réussite, l'audience, les groupes d'expérience, les dimensions, les options et les contraintes alimentent la conception d'un agent Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## Fonctionnalités de Decisioning Studio {#decisioning-studio-capabilities}

| Fonctionnalité | Détails |
|------------|---------|
| **N'importe quel indicateur de réussite** | Optimisez le chiffre d'affaires, les conversions, l'ARPU, la LTV ou tout indicateur clé de performance métier |
| **Dimensions illimitées** | Personnalisez les offres, le canal, le timing, la fréquence, le contenu créatif, et bien plus encore |
| **N'importe quelle CEP** | Intégrations natives avec Braze, Salesforce Marketing Cloud, ou intégrations personnalisées pour toute plateforme |
| **AI Decisioning Services** | Accompagnement dédié par l'équipe de data science de Braze |
| **Conception avancée d'expériences** | Groupes de traitement et groupes de contrôle entièrement personnalisables |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fonctionnalités de Decisioning Studio" }

## Bonnes pratiques {#best-practices}

Voici quelques bonnes pratiques pour concevoir des agents Decisioning Studio :

- **Maximisez la richesse des données :** plus les agents disposent d'informations sur vos clients, meilleures seront leurs performances.
- **Diversifiez les actions :** plus l'ensemble d'actions que l'agent peut entreprendre est diversifié, plus il peut personnaliser sa stratégie pour chaque utilisateur.
- **Minimisez les contraintes :** moins il y a de contraintes sur vos agents, mieux c'est. Les contraintes doivent être conçues pour respecter les règles métier tout en libérant autant que possible l'expérimentation pilotée par l'agent.