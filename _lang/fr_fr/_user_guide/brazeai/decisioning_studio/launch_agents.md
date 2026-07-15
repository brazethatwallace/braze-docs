---
nav_title: Lancer votre agent
article_title: Lancer votre agent
page_order: 5
page_type: reference
description: "Découvrez comment lancer votre agent Decisioning Studio et boucler la boucle de décision automatisée par IA pour une optimisation auto-apprenante."
---

# Lancer votre agent {#launch-your-agent}

> Après avoir connecté vos sources de données, configuré l'orchestration et conçu votre agent, vous êtes prêt à le lancer. Cet article explique comment activer votre agent et boucler la boucle de décision automatisée par IA afin que l'agent puisse apprendre et s'améliorer en continu.

## Étapes de lancement {#launch-steps}

Après avoir terminé toutes les étapes de configuration avec votre équipe AI Decisioning Services :

1. Vérifiez la configuration de votre agent pour vous assurer que tous les paramètres sont corrects.
2. Vérifiez que vos connexions de données et vos intégrations d'orchestration sont actives.
3. Travaillez avec votre équipe AI Decisioning Services pour activer l'agent.

Une fois lancé, votre agent va :
- Commencer à recevoir les données d'audience et de clients
- Commencer à formuler des recommandations personnalisées pour chaque client
- Orchestrer des actions via votre plateforme d'engagement client configurée
- Collecter des données de retour pour apprendre et s'améliorer au fil du temps

## Boucler la boucle de décision automatisée par IA {#close-the-ai-decisioning-loop}

Une fois lancé, votre agent a besoin de données de retour pour apprendre et s'améliorer. Cela inclut les données de conversions, les données d'engagement et les données d'activations qui indiquent à l'agent ce qui s'est passé après l'envoi des décisions d'engagement client.

Pour connaître les exigences détaillées concernant la préparation de ces ressources de données de retour essentielles, consultez [Préparer vos sources de données]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data).

{% alert note %}
Si l'agent est nativement intégré à la plateforme d'engagement client (comme Braze ou Salesforce Marketing Cloud), il se peut qu'aucune étape de configuration supplémentaire ne soit nécessaire pour les données de retour, car celles-ci peuvent être envoyées automatiquement avec les données client.
{% endalert %}

## Surveiller votre agent {#monitor-your-agent}

Après le lancement, travaillez avec votre équipe AI Decisioning Services pour surveiller les performances :

- **Indicateurs de performance :** suivez votre indicateur de réussite à travers les groupes d'expérience
- **Progression de l'apprentissage :** observez comment les recommandations de l'agent évoluent au fil du temps
- **Informations :** identifiez quelles dimensions et options génèrent des résultats pour différents segments de clients

## Optimisation continue {#ongoing-optimization}

Votre équipe AI Decisioning Services continuera à travailler avec vous pour :

- Analyser les performances de l'agent et identifier les opportunités d'optimisation
- Étendre les dimensions ou les options selon les besoins
- Ajuster les contraintes en fonction des changements de règles métier
- Déployer les agents performants vers des cas d'utilisation supplémentaires

{% alert tip %}
L'agent apprend et s'améliore continuellement au fil du temps. Laissez suffisamment de temps à l'agent pour collecter des données et optimiser ses recommandations avant d'apporter des modifications significatives à la configuration.
{% endalert %}