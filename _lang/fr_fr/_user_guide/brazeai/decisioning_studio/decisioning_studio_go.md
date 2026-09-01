---
nav_title: Decisioning Studio Go
article_title: BrazeAI Decisioning Studio Go
page_order: 5.5
description: "Découvrez comment configurer et intégrer BrazeAI Decisioning Studio<sup>TM</sup> Go dans Braze."
---

# BrazeAI Decisioning Studio™ Go

> Découvrez comment configurer et intégrer BrazeAI Decisioning Studio™ Go dans Braze.

## À propos de Decisioning Studio Go {#about-decisioning-studio-go}

Decisioning Studio Go est un agent décisionnel basé sur l'IA pour les programmes e-mail récurrents. Au lieu de choisir une seule ligne d'objet, un horaire d'envoi ou une image gagnante pour l'ensemble d'une audience, l'agent sélectionne la meilleure combinaison pour chaque destinataire en fonction de son engagement passé.

Vous définissez les variantes parmi lesquelles l'agent peut choisir, comme les lignes d'objet, les CTA, les images, les jours d'envoi et les horaires d'envoi. Pour chaque utilisateur de votre Segment, l'agent sélectionne l'option la plus susceptible de générer de l'engagement, dans le cadre des contraintes et de la planification que vous configurez.

Cela diffère du test A/B au niveau d'une Campaign avec [Optimiser avec BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection), qui optimise les variantes pour l'ensemble de l'audience. Decisioning Studio Go personnalise au niveau individuel à chaque envoi du programme.

### Comment ça fonctionne {#how-it-works}

L'agent divise un Segment Braze en deux groupes : un groupe Decisioning Studio qui reçoit du contenu e-mail optimisé par l'IA, et un groupe de contrôle aléatoire (minimum 5 %) qui reçoit des combinaisons aléatoires des mêmes options. Le groupe de contrôle aléatoire vous fournit une mesure continue et comparable de l'amélioration apportée par l'agent ; vous pouvez toujours voir comment l'expérience personnalisée se compare au même contenu envoyé sans personnalisation.

Pour chaque utilisateur du groupe Decisioning Studio, l'agent choisit parmi les options que vous avez fournies : quel créatif envoyer (y compris la ligne d'objet, le CTA et l'image spécifiques qu'il contient), et quand l'envoyer (jour de la semaine et heure de la journée, en respectant les heures calmes et le fuseau horaire local de l'utilisateur). [Configurer votre agent Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup) détaille chacun de ces éléments.

Au fur et à mesure que les utilisateurs interagissent — ou non — l'agent apprend. Les rapports indiquent quand l'agent est encore en période d'apprentissage par rapport au moment où il personnalise activement, afin que vous sachiez toujours à quelle étape se trouve l'agent.

### Ce que vous configurez {#what-you-configure}

| Configuration | Description |
|---|---|
| **Audience** | Un seul Segment Braze comme audience d'entrée. L'agent divise automatiquement le Segment entre le groupe de décision et le groupe de contrôle aléatoire. |
| **Planification** | Fréquence d'envoi (par exemple, une seule sélection trois fois par semaine), jours de la semaine autorisés, heures calmes dans le fuseau horaire local de l'utilisateur, et respect des règles de limite de fréquence au niveau de l'agent. |
| **Créatifs** | Un ou plusieurs créatifs de base conçus dans le compositeur Braze. Au sein de chaque créatif de base, vous pouvez marquer une ligne d'objet, un CTA et une image comme points de personnalisation à l'aide d'étiquettes Liquid, puis fournir une liste de variantes pour chacun. L'agent décide quel créatif de base et quelle variante utiliser pour chaque destinataire. |
| **Contraintes** | Des limites qui empêchent l'agent d'envoyer le même créatif de base ou la même ligne d'objet à un utilisateur plus d'une fois dans une fenêtre que vous définissez. |
| **Vérification et lancement** | Un écran de validation final fait apparaître les avertissements à traiter avant le lancement. L'agent passe de **Brouillon** à **Actif** et commence les envois. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuration de Decisioning Studio Go" }

### Quand utiliser Decisioning Studio Go {#when-to-use-decisioning-studio-go}

Les cas les plus adaptés sont les programmes e-mail récurrents avec des audiences stables et du contenu cliquable, comme les calendriers permanents (récompenses, sorties de contenu, rappels de cycle de vie), les programmes evergreen (reconquête, réengagement) et les promotions multi-e-mails. Ces programmes fournissent à l'agent suffisamment de volume et de variété pour apprendre de manière significative.

Consultez [Exemples pour Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples) pour des recommandations détaillées par type de programme.

### Où se situe Decisioning Studio Go dans la suite Decisioning Studio {#where-decisioning-studio-go-sits-in-the-decisioning-studio-suite}

Decisioning Studio Go est le niveau d'entrée de BrazeAI Decisioning Studio. Il est conçu pour les marketeurs qui souhaitent une personnalisation e-mail individuelle sans la charge de configuration d'une implémentation complète de Decisioning Studio Pro.

Decisioning Studio Pro ajoute :
- L'optimisation pour tout indicateur métier (pas uniquement les clics)
- La connexion à toute source de données first-party
- La prise de décision multicanale
- Des modèles d'orchestration étendus
- Un accompagnement dédié de l'équipe Braze AI Decisioning Services

## Étapes suivantes {#next-steps}

- [Configurez votre agent Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup) et paramétrez l'audience, la planification, les créatifs et les contraintes
- [Passez en revue les exemples pour Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples) pour vérifier que votre programme est adapté
- Consultez la [FAQ]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq) pour les questions fréquentes