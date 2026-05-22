---
nav_title: Cas d'utilisation
article_title: "Cas d'utilisation : Decisioning Studio"
description: "Cet exemple illustre comment une marque fictive utilise BrazeAI Decisioning Studio et un agent de décision pour proposer des messages personnalisés de reconquête et optimiser le chiffre d'affaires à des moments clés pour les clients."
---

# Cas d'utilisation : reconquérir les clients inactifs grâce à un agent de décision axé sur le chiffre d'affaires {#use-case-win-back-lapsed-customers-with-a-revenue-focused-decisioning-agent}

> Cet exemple illustre comment une marque fictive utilise BrazeAI Decisioning Studio™ et un agent de décision pour orienter chaque client vers une décision optimale à partir de la banque d'actions, personnaliser les messages de reconquête et optimiser le chiffre d'affaires. Il relie la conception de l'agent, l'audience et les expériences, l'orchestration via Braze, et l'apprentissage post-lancement.

Supposons que Poppy occupe le poste de gestionnaire CRM chez Kitchenerie, une marque fictive de vente en ligne spécialisée dans les ustensiles de cuisine.

De nombreux clients ne consultent les collections saisonnières qu'une ou deux fois avant de quitter le site. Les programmes de reconquête précédents reposaient sur des parcours figés et des tests A/B manuels, utiles pour tester les accroches, mais insuffisants pour déterminer quelle combinaison d'offre, de canal, de cadence et de timing maximise le chiffre d'affaires par client. La priorité de la direction est claire : ramener un maximum d'acheteurs inactifs et augmenter le chiffre d'affaires sans dépasser les limites fixées en matière de remises ou de fréquence d'envoi.

Ce tutoriel explique comment Poppy :

- Cible les clients inactifs ou à risque comme audience de l'agent tout en structurant des groupes d'expérience pour une comparaison équitable
- Permet à l'agent de choisir les actions les plus adaptées parmi une banque d'actions riche, afin que les messages restent personnalisés à grande échelle
- Met en place l'orchestration pour que les décisions transitent par Braze en tant que plateforme d'engagement client
- Lance l'agent, lui permettant d'apprendre de manière autonome ce qui génère du chiffre d'affaires en reconquête

## Étape 1 : Définir les indicateurs de réussite et l'audience ciblée par l'agent {#step-1-define-success-metrics-and-who-the-agent-targets}

Poppy confirme l'indicateur de réussite que l'agent doit maximiser : le chiffre d'affaires issu des rachats parmi les clients qui ont cessé d'acheter.

Elle définit qui entre dans le programme : un segment Braze de clients n'ayant plus effectué d'achat ou d'utilisateurs dormants à forte valeur. Poppy n'a plus qu'à indiquer à l'équipe AI Decisioning Services quel segment l'agent doit cibler. L'intégration permettant d'extraire les données de ce segment s'effectue en arrière-plan, sans que Poppy ait besoin de configurer une intégration.

## Étape 2 : Construire la banque d'actions et les contraintes {#step-2-build-the-action-bank-and-constraints}

Poppy identifie les dimensions importantes pour les stratégies de reconquête :

- Offre : livraison gratuite, pourcentage de réduction ou lot de produits
- Canal : e-mail, push ou SMS
- Heure d'envoi ou cadence
- Création : petites illustrations ou texte axé sur l'utilité

Pour chaque dimension, elle liste les options concrètes dans la banque d'actions — les seules actions que l'agent est autorisé à effectuer (tout le reste est exclu par conception). L'agent expérimente ensuite les combinaisons autorisées pour découvrir ce qui fonctionne pour chaque client, tout en optimisant l'indicateur de réussite choisi.

## Étape 3 : Préparer les données et connecter l'orchestration à Braze {#step-3-prepare-data-and-connect-orchestration-to-braze}

En suivant la documentation [Connecter vos données]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/connect_data_sources/), Poppy s'assure que des signaux first-party riches (incluant l'historique d'achat, l'affinité par catégorie, le comportement de navigation et l'engagement) alimentent l'agent afin que chaque décision repose sur des comportements réels.

Pour l'orchestration, elle utilise le chemin natif Braze : Decisioning Studio décide quoi envoyer et quand ; Braze assure la livraison. Elle prépare des modèles de base (Campaigns déclenchées par API) par canal avec des champs dynamiques pour les offres et les créations, et configure la rééligibilité.

## Étape 4 : Lancer, surveiller et optimiser le chiffre d'affaires {#step-4-launch-monitor-and-optimize-for-revenue}

Après une revue de configuration avec l'équipe AI Decisioning Services, Poppy lance l'agent. L'agent commence à recommander des actions par utilisateur et à orchestrer les envois via Braze, s'améliorant au fil du temps.

En associant un indicateur de réussite axé sur le chiffre d'affaires à un agent de décision qui teste en continu les actions autorisées, Kitchenerie passe d'envois de reconquête statiques à des décisions individualisées qui s'adaptent à chaque client, dans le but de reconquérir davantage de clients et d'augmenter le chiffre d'affaires tout en respectant les règles métier définies par Poppy.