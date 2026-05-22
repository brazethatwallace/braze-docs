---
nav_title: Concevoir des agents de décision
article_title: Concevoir des agents de décision
page_order: 1
page_type: reference
description: "Cet article de référence couvre les concepts clés et les bonnes pratiques pour concevoir et configurer votre agent de décision."
---

# Concevoir des agents de décision {#design-decisioning-agents}

> Cet article de référence couvre les concepts clés et les bonnes pratiques pour concevoir et configurer votre agent de décision.

## À propos des agents de décision {#about-decisioning-agents}

La conception de votre agent de décision est la première étape de la mise en place de Decisioning Studio. Pour que l'agent de décision puisse prendre des décisions, vous devez définir le résultat que vous souhaitez maximiser, ainsi que les actions que l'agent peut entreprendre pour y parvenir.

### Concepts clés {#key-concepts}

Les termes suivants sont utilisés tout au long du guide Decisioning Studio.

| Terme | Définition |
| --- | --- |
| **Agent de décision** | Un agent de décision est une configuration personnalisée pour BrazeAI Decisioning Studio™, conçue sur mesure pour atteindre un objectif métier spécifique. Il est défini par l'indicateur de réussite, les dimensions et les options que vous choisissez. |
| **Indicateur de réussite** | L'indicateur métier spécifique que vous souhaitez optimiser, comme le chiffre d'affaires, les conversions ou le chiffre d'affaires moyen par utilisateur (ARPU). C'est l'indicateur que l'agent de décision cherchera à maximiser par ses actions. |
| **Dimensions** | Les dimensions peuvent être considérées comme les *types de leviers* que l'agent de décision peut actionner pour maximiser l'indicateur de réussite. Les dimensions courantes incluent l'offre, la ligne d'objet, le créatif, le canal ou le moment d'envoi. |
| **Banque d'actions** | La banque d'actions définit les *options spécifiques* auxquelles l'agent de décision a accès pour chaque « levier » de dimension. Par exemple, pour une dimension de canal, vous définissez les canaux spécifiques auxquels l'agent de décision a accès. Pour une dimension d'offre, vous définissez les offres spécifiques que l'agent de décision peut tester. |
| **Contraintes** | En général, l'agent de décision peut prendre n'importe quelle combinaison d'actions que vous placez dans la banque d'actions. Cependant, vous pouvez également définir des contraintes pour limiter les actions de l'agent de décision afin de respecter des règles métier essentielles. Par exemple, cela peut consister à empêcher la sélection d'une offre spécifique pour des clients situés dans une zone géographique non éligible, ou à fixer un budget maximum que l'agent de décision peut dépenser. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Concepts clés" }

![Vue d'ensemble d'un agent de décision]({% image_buster /assets/img/decisioning_studio/decisioning_studio_high_level_agent.png %})

{% alert important %}
L'agent de décision ne peut entreprendre que les actions que *vous* configurez et ajoutez à la banque d'actions. Cela signifie que toutes les actions possibles sont définies par les combinaisons de ce que vous placez dans la banque d'actions.
{% endalert %}

## Comment concevoir votre agent de décision {#how-to-design-your-decisioning-agent}

Lors de la mise en place d'un agent de décision, vous devrez réfléchir à quatre éléments de conception principaux :

### L'« objectif » : définir votre indicateur de réussite {#the-goal-define-your-success-metric}

*Quel résultat souhaitez-vous que l'agent maximise ?*

Votre indicateur de réussite est le résultat métier que l'agent optimisera. Il doit être directement aligné avec vos objectifs métier — non pas des indicateurs intermédiaires comme les clics ou les ouvertures, mais de véritables résultats métier comme le chiffre d'affaires, les conversions, l'ARPU ou la valeur vie client.

### Le « qui » : sélectionner votre audience {#the-who-select-your-audience}

*Qui l'agent de décision va-t-il engager ?*

Définissez l'audience que votre agent servira. Il peut s'agir de tous les clients, d'un segment spécifique (comme les membres d'un programme de fidélité) ou de clients à un stade particulier de leur cycle de vie (comme les acheteurs récents ou les abonnés à risque).

### Le « quoi » : configurer votre banque d'actions {#the-what-configure-your-action-bank}

*Parmi quelles options l'agent peut-il choisir pour atteindre le résultat ?*

La banque d'actions définit tous les leviers que l'agent peut actionner : les dimensions (comme le canal, l'offre, le moment et la fréquence) et les options spécifiques au sein de chaque dimension. L'agent expérimente différentes combinaisons de ces options pour trouver ce qui fonctionne le mieux pour chaque client.

### Le « comment » : configurer vos contraintes {#the-how-configure-your-constraints}

*Quelles règles l'agent doit-il suivre ?*

Les contraintes sont les règles que l'agent doit respecter. Cela peut consister à empêcher la sélection d'une offre spécifique pour des clients situés dans une zone géographique non éligible, ou à fixer un budget maximum que l'agent de décision peut dépenser.

## Bonnes pratiques et exemples {#best-practices-and-examples}

Pour maximiser l'impact de votre agent de décision, vous devriez :

- Choisir un indicateur de réussite étroitement aligné avec vos objectifs métier, comme le chiffre d'affaires, les conversions ou l'ARPU.
- Vous concentrer sur les dimensions, ou « leviers » à tester, comme l'offre, la ligne d'objet, le créatif, le canal ou le moment d'envoi, qui sont les plus susceptibles d'avoir un impact significatif sur l'indicateur de réussite.
- Sélectionner les options pour chaque dimension, comme l'e-mail par rapport au SMS, ou une fréquence quotidienne par rapport à hebdomadaire, qui sont les plus susceptibles d'avoir un impact significatif sur l'indicateur de réussite.

Voici quelques exemples d'agents de décision que vous pourriez créer :

{% tabs %}
{% tab Agent de réachat %}
Vous pourriez créer un agent de réachat pour augmenter les conversions de suivi après une première vente :

- Définissez l'audience et le message dans Braze
- Decisioning Studio exécute automatiquement des expériences quotidiennes, testant différentes combinaisons d'offres produit, de moments d'envoi et de fréquences pour chaque client
- Au fil du temps, BrazeAI<sup>TM</sup> apprend ce qui fonctionne le mieux pour chaque client
- Orchestre des envois personnalisés via Braze pour maximiser les taux de réachat
{% endtab %}
{% tab Agent de vente croisée ou montée en gamme %}
Vous pourriez créer un agent de vente croisée ou de montée en gamme pour maximiser le chiffre d'affaires moyen par utilisateur (ARPU) des abonnements internet :

- Définissez l'audience et le message dans Braze
- Decisioning Studio exécute automatiquement des expériences quotidiennes, testant différentes combinaisons de messages, de moments d'envoi, de remises et d'offres de forfaits pour chaque client
- BrazeAI<sup>TM</sup> apprend quels clients sont réceptifs aux offres de montée en gamme directe et lesquels nécessitent des remises ou d'autres incitations pour passer à un forfait supérieur
- Orchestre des envois personnalisés via Braze pour maximiser l'ARPU
{% endtab %}
{% tab Agent de renouvellement et de rétention %}
Vous pourriez créer un agent de renouvellement et de rétention pour sécuriser les renouvellements de contrats, en maximisant à la fois la durée du contrat et la valeur actuelle nette (VAN) :

- Définissez l'audience et le message dans Braze
- Decisioning Studio exécute automatiquement des expériences quotidiennes, testant différentes offres de renouvellement pour chaque client
- BrazeAI<sup>TM</sup> identifie les clients moins sensibles au prix et nécessitant des remises moins importantes pour renouveler
- Orchestre des envois personnalisés via Braze pour maximiser les renouvellements de contrats et la VAN
{% endtab %}
{% tab Agent de reconquête %}
Vous pourriez créer un agent de reconquête pour augmenter la réactivation en encourageant les anciens abonnés à se réabonner :

- Définissez l'audience et le message dans Braze
- Decisioning Studio exécute automatiquement des expériences quotidiennes, testant des milliers de variables simultanément, y compris le créatif, le message, le canal et la cadence
- BrazeAI<sup>TM</sup> découvre la meilleure combinaison pour chaque client individuel
- Orchestre des envois personnalisés via Braze pour maximiser les taux de réactivation
{% endtab %}
{% tab Agent de recommandation %}
Vous pourriez créer un agent de recommandation pour maximiser les nouveaux comptes ouverts grâce aux recommandations de cartes de crédit professionnelles par les clients existants :

- Définissez l'audience et le message dans Braze
- Decisioning Studio exécute automatiquement des expériences quotidiennes, testant différents e-mails, créatifs, moments d'envoi et offres de cartes de crédit pour chaque client
- BrazeAI<sup>TM</sup> détermine la combinaison idéale pour des clients spécifiques
- Orchestre des envois personnalisés via Braze pour maximiser les conversions de recommandation
{% endtab %}
{% tab Agent de nurturing et de conversion de prospects %}
Vous pourriez créer un agent de nurturing et de conversion de prospects pour générer du chiffre d'affaires incrémental et payer le juste prix pour chaque client :

- Définissez l'audience et le message dans Braze
- Decisioning Studio exécute automatiquement des expériences quotidiennes, testant différents segments de clients, méthodologies d'enchères, niveaux d'enchères et créatifs
- BrazeAI<sup>TM</sup> exploite des données first-party robustes pour optimiser les performances publicitaires payantes à mesure que les politiques de confidentialité évoluent
- Orchestre des envois personnalisés via Braze pour maximiser le chiffre d'affaires tout en optimisant le coût par client
{% endtab %}
{% tab Agent de fidélité et d'engagement %}
Vous pourriez créer un agent de fidélité et d'engagement pour maximiser les achats des nouveaux inscrits à un programme de fidélité client :

- Définissez l'audience et le message dans Braze
- Decisioning Studio exécute automatiquement des expériences quotidiennes, testant différentes offres par e-mail, moments d'envoi et fréquences pour chaque client
- BrazeAI<sup>TM</sup> apprend ce qui fonctionne le mieux pour chaque nouvel inscrit au programme de fidélité
- Orchestre des envois personnalisés via Braze pour maximiser les taux d'achat et de réachat
{% endtab %}
{% endtabs %}

## Étapes suivantes {#next-steps}

Prêt à créer votre propre agent de décision ? Consultez [Premiers pas avec Decisioning Studio]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/get_started/) pour un guide qui vous accompagne dans la connexion des sources de données, la mise en place de l'orchestration, la conception de votre agent et le lancement en production.