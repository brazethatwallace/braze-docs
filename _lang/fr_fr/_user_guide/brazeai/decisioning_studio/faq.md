---
nav_title: FAQ
article_title: FAQ sur Decisioning Studio
page_order: 8
page_type: FAQ
description: "Cette page fournit des réponses aux questions fréquemment posées concernant Decisioning Studio."
---

# Questions fréquemment posées {#frequently-asked-questions}

> Cet article fournit des réponses à certaines questions fréquemment posées concernant Decisioning Studio.

### Qu'est-ce qu'un agent décisionnel ? {#what-is-a-decisioning-agent}

Un agent décisionnel est une configuration personnalisée pour BrazeAI Decisioning Studio™, conçue sur mesure pour répondre à un objectif métier spécifique. Il est défini par l'indicateur de réussite, les dimensions et les options que vous sélectionnez. L'agent décisionnel identifie automatiquement l'action optimale pour chaque client afin de maximiser l'indicateur métier que vous avez choisi.

### Quels indicateurs puis-je optimiser ? {#what-metrics-can-i-optimize-for}

Vous pouvez optimiser n'importe quel indicateur métier qui correspond à vos objectifs, tel que le chiffre d'affaires, les conversions, le chiffre d'affaires moyen par utilisateur (ARPU), la valeur vie client (CLV), le bénéfice, les renouvellements de contrat ou tout autre indicateur clé de performance.

### Que sont les dimensions dans Decisioning Studio ? {#what-are-dimensions-in-decisioning-studio}

Les dimensions peuvent être considérées comme les *types de leviers* que l'agent décisionnel peut actionner pour maximiser l'indicateur de réussite. Les dimensions courantes comprennent l'offre, la ligne d'objet, le contenu créatif, le canal ou l'heure d'envoi.

### Qu'est-ce qu'une banque d'actions ? {#what-is-an-action-bank}

La banque d'actions définit les *options spécifiques* auxquelles l'agent décisionnel a accès pour chaque « levier » de dimension. Par exemple, pour une dimension de canal, vous définissez les canaux spécifiques auxquels l'agent décisionnel a accès. Pour une dimension d'offre, vous définissez les offres spécifiques que l'agent décisionnel peut tester.

### L'agent décisionnel peut-il effectuer des actions que je n'ai pas configurées ? {#can-the-decisioning-agent-take-actions-i-havent-configured}

Non. L'agent décisionnel ne peut effectuer que les actions que vous avez configurées et ajoutées à la banque d'actions. Cela signifie que toutes les actions possibles sont définies par les combinaisons de ce que vous avez enregistré dans la banque d'actions.

### Que sont les contraintes ? {#what-are-constraints}

Les contraintes limitent les actions de l'agent décisionnel afin de respecter les règles métier essentielles. Par exemple, cela peut empêcher une offre spécifique d'être sélectionnée pour des clients situés dans une zone géographique non éligible, ou fixer un budget maximal que l'agent décisionnel est autorisé à dépenser.

### Quelle est la différence entre Decisioning Studio Go et Decisioning Studio Pro ? {#what-is-the-difference-between-decisioning-studio-go-and-decisioning-studio-pro}

Decisioning Studio Pro inclut l'assistance AI Decisioning Services fournie par l'équipe de science des données déployée en amont de Braze, qui vous aidera à concevoir et à configurer votre agent afin d'optimiser vos résultats métier. Pour plus d'informations, consultez [la comparaison entre Decisioning Studio Go et Decisioning Studio Pro]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/#decisioning-studio-go-vs-decisioning-studio-pro).