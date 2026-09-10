---
nav_title: Decisioning Studio Go
article_title: BrazeAI Decisioning Studio Go
page_order: 5.5
description: "Découvrez comment configurer et intégrer BrazeAI Decisioning Studio<sup>TM</sup> Go dans Braze."
---

# BrazeAI Decisioning Studio™ Go

> Découvrez comment configurer et intégrer BrazeAI Decisioning Studio™ Go dans Braze.

## À propos de Decisioning Studio Go {#about-decisioning-studio-go}

Decisioning Studio Go est un agent décisionnel basé sur l'IA pour les programmes e-mail récurrents. Au lieu de choisir une seule ligne d'objet, un seul horaire d'envoi ou une seule image gagnante pour l'ensemble d'une audience, l'agent sélectionne la meilleure combinaison pour chaque destinataire en fonction de son engagement passé.

Vous définissez les variantes parmi lesquelles l'agent peut choisir — comme les lignes d'objet, les CTA, les images, les jours d'envoi et les horaires d'envoi. Pour chaque utilisateur de votre Segment, l'agent sélectionne l'option la plus susceptible de générer de l'engagement, dans le cadre des contraintes et de la planification que vous configurez.

Cela diffère du test A/B au niveau d'une Campaign avec [Optimiser avec BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection), qui optimise les variantes pour l'audience. Decisioning Studio Go personnalise au niveau individuel à chaque envoi du programme.

### Comment ça fonctionne {#how-it-works}

L'agent divise un Segment Braze en deux groupes : un groupe Decisioning Studio qui reçoit du contenu e-mail optimisé par l'IA, et un groupe de contrôle aléatoire (minimum 5 %) qui reçoit des combinaisons aléatoires des mêmes options. Le groupe de contrôle aléatoire vous offre une mesure continue et comparable de l'amélioration apportée par l'agent ; vous pouvez toujours voir comment l'expérience personnalisée se comporte par rapport au même contenu envoyé sans personnalisation.

Pour chaque utilisateur du groupe Decisioning Studio, l'agent choisit parmi les options que vous avez fournies : quel créatif envoyer (y compris la ligne d'objet, le CTA et l'image spécifiques qu'il contient), et quand l'envoyer (jour de la semaine et heure de la journée, en respectant les heures calmes et le fuseau horaire local de l'utilisateur). [Configurer votre agent Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup) couvre chacun de ces aspects en détail.

À mesure que les utilisateurs interagissent — ou non — l'agent apprend. Les rapports indiquent quand l'agent est encore dans sa période d'apprentissage et quand il personnalise activement, afin que vous sachiez toujours à quelle étape se trouve l'agent.

### Ce que vous configurez {#what-you-configure}

| Configuration | Description |
|---|---|
| **Audience** | Un Segment Braze unique comme audience d'entrée. L'agent divise automatiquement le Segment entre le groupe décisionnel et le groupe de contrôle aléatoire. |
| **Planification** | Fréquence d'envoi (par exemple, un envoi unique trois fois par semaine), jours de la semaine autorisés, heures calmes dans le fuseau horaire local de l'utilisateur, et respect des règles de limite de fréquence au niveau de l'agent. |
| **Créatifs** | Un ou plusieurs créatifs de base construits dans le compositeur Braze. Dans chaque créatif de base, vous pouvez marquer une ligne d'objet, un CTA et une image comme points de personnalisation à l'aide d'étiquettes Liquid, puis fournir une liste de variantes pour chacun. L'agent décide quel créatif de base et quelle variante utiliser pour chaque destinataire. |
| **Contraintes** | Des limites qui empêchent l'agent d'envoyer le même créatif de base ou la même ligne d'objet à un utilisateur plus d'une fois dans une fenêtre que vous définissez. |
| **Revue et lancement** | Un écran de validation final signale les avertissements à traiter avant le lancement. L'agent passe de **Brouillon** à **Actif** et commence à envoyer. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuration de Decisioning Studio Go" }

### Quand utiliser Decisioning Studio Go {#when-to-use-decisioning-studio-go}

Les cas les plus adaptés sont les programmes e-mail récurrents avec des audiences stables et du contenu cliquable, comme les calendriers permanents (récompenses, sorties de contenu, rappels de cycle de vie), les programmes pérennes (reconquête, réengagement) et les promotions multi-e-mails. Ceux-ci offrent à l'agent suffisamment de volume et de variété pour apprendre de manière significative.

Consultez [Exemples pour Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples) pour des recommandations détaillées d'adéquation par type de programme.

### Où se situe Decisioning Studio Go dans la suite Decisioning Studio {#where-decisioning-studio-go-sits-in-the-decisioning-studio-suite}

Decisioning Studio Go est le niveau d'entrée de BrazeAI Decisioning Studio. Il est conçu pour les marketeurs qui souhaitent une personnalisation e-mail individuelle sans la complexité de mise en place d'une implémentation complète de Decisioning Studio Pro.

Decisioning Studio Pro ajoute :
- L'optimisation pour n'importe quel indicateur métier (pas seulement les clics)
- La connexion à n'importe quelle source de données first-party
- La prise de décision multicanal
- Des modèles d'orchestration étendus
- Un accompagnement dédié par l'équipe Braze AI Decisioning Services

## Prochaines étapes {#next-steps}

{% article_tiles %}
- name: Configurer votre agent Decisioning Studio Go
  link: /docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup/
- name: Exemples pour Decisioning Studio Go
  link: /docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples/
- name: FAQ
  link: /docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq/
{% endarticle_tiles %}