---
nav_title: Concevoir votre agent
article_title: Concevoir votre agent
page_order: 3
description: "Découvrez comment concevoir un agent BrazeAI Decisioning Studio Go, y compris la définition de l'audience, les dimensions et les limitations spécifiques à Go."
---

# Concevoir votre agent {#design-your-agent}

> Cet article explique comment concevoir votre agent Decisioning Studio Go, notamment comment définir votre audience, sélectionner des dimensions et comprendre les capacités et les limites spécifiques à Go.

Pour les concepts fondamentaux relatifs aux agents décisionnels, notamment les indicateurs de réussite, les dimensions, les banques d'actions et les contraintes, consultez [Concevoir des agents décisionnels]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/design_agents).

## Fonctionnalités Go et Pro {#go-versus-pro-capabilities}

Decisioning Studio Go est une plateforme en libre-service dotée de fonctionnalités simplifiées par rapport à Decisioning Studio Pro. Comprendre ces différences vous aide à concevoir un agent efficace dans le cadre de Go.

| Capacité | Decisioning Studio Go | Decisioning Studio Pro |
|-----------|----------------------|------------------------|
| **Indicateur de réussite** | Clics uniquement | Tout indicateur commercial (chiffre d'affaires, conversions ou ARPU) |
| **Dimensions** | Banque d'actions restreinte | Dimensions illimitées |
| **CEP pris en charge** | Braze, SFMC | Tout CEP (natif et personnalisé) |
| **Données client** | Engagement uniquement | Toutes les données 1P |
| **Configuration** | Libre-service | Assistance des services AI Decisioning |
| **Groupes expérimentaux** | Go + Contrôle aléatoire + BAU facultatif | Entièrement personnalisable |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fonctionnalités Go et Pro" }

## Concevoir votre agent Go {#design-your-go-agent}

Lors de la conception d'un agent Decisioning Studio Go, vous prendrez des décisions dans les domaines suivants :

### Étape 1 : Définir votre audience {#step-1-define-your-audience}

Votre audience est l'ensemble des clients avec lesquels l'agent interagira. Dans Go, les audiences sont définies dans votre CEP :

{% tabs %}
{% tab Braze %}

**Définition de l'audience dans Braze :**

1. Créez un segment dans Braze qui définit les clients que vous souhaitez que l'agent cible.
2. Lors de la configuration de votre expérimentateur dans le portail Decisioning Studio Go, sélectionnez ce segment comme audience cible.

{% alert tip %}
Envisagez de créer un segment dédié pour votre expérimentateur Decisioning Studio Go afin de garantir l'isolation et la mesurabilité de vos tests.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

**Définition de l'audience dans SFMC :**

1. Configurez une Data Extension qui contient votre audience cible.
2. Assurez-vous que cette Data Extension est actualisée quotidiennement avec les dernières données clients.
3. Référencez cette Data Extension dans le portail Decisioning Studio Go lors de la configuration de votre expérimentateur.

{% endtab %}
{% endtabs %}

### Étape 2 : Sélectionner vos dimensions {#step-2-select-your-dimensions}

Les dimensions sont les « leviers » que l'agent peut actionner pour personnaliser l'expérience client. Il s'agit notamment de dimensions créatives telles que la ligne d'objet et l'image principale, ainsi que de dimensions liées au type d'envoi, telles que la fréquence des e-mails ou l'heure de la journée.

{% alert note %}
Les dimensions spécifiques disponibles dépendent de votre CEP et de la configuration de vos campagnes. Utilisez les modèles et le contenu que vous avez configurés dans votre CEP.
{% endalert %}

### Étape 3 : Configurer votre banque d'actions {#step-3-configure-your-action-bank}

La banque d'actions définit les options spécifiques parmi lesquelles l'agent peut choisir pour chaque dimension. Par exemple :

- **Modèles d'e-mails :** Sélectionnez les modèles que l'agent est autorisé à utiliser (ceux-ci doivent d'abord être configurés dans votre CEP).
- **Lignes d'objet :** Définissez les variantes de ligne d'objet que l'agent peut tester.
- **Heures d'envoi :** Indiquez les plages horaires parmi lesquelles l'agent peut faire son choix.

### Étape 4 : Constituer les groupes expérimentaux {#step-4-set-up-experiment-groups}

Decisioning Studio Go crée automatiquement des groupes d'expérimentation afin de mesurer les performances :

| Groupe | Description |
|-------|-------------|
| **Decisioning Studio Go** | Les clients qui reçoivent des recommandations optimisées par l'intelligence artificielle |
| **Contrôle aléatoire** | Les clients qui reçoivent des options sélectionnées de manière aléatoire (comparaison de référence) |
| **Activités habituelles (facultatif)** | Les clients qui reçoivent votre campagne actuelle (si l'on compare avec les performances actuelles) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 4 : Constituer les groupes expérimentaux" }

{% alert important %}
Pour une comparaison précise, assurez-vous qu'aucun client ne peut appartenir à plus d'un groupe d'expérimentation et que les clients sont répartis de manière aléatoire dans les groupes, sans biais.
{% endalert %}

## Restrictions à prendre en compte {#limitations-to-consider}

Lors de la conception de votre agent Go, gardez ces contraintes à l'esprit :

- **Clics uniquement :** Go optimise les taux de clics. Si vous avez besoin d'optimiser votre chiffre d'affaires, vos conversions ou d'autres indicateurs commerciaux, envisagez Decisioning Studio Pro.
- **Dimensions restreintes :** Go prend en charge un ensemble prédéfini de dimensions. Pour des dimensions personnalisées ou une personnalisation complexe, envisagez Decisioning Studio Pro.
- **Prise en charge limitée des CEP :** Go s'intègre uniquement avec Braze et Salesforce Marketing Cloud. Pour les autres plateformes, envisagez Decisioning Studio Pro.

## Bonnes pratiques {#best-practices}

- **Commencez par un périmètre restreint :** Utilisez deux à trois modèles ou variantes de ligne d'objet. Cela offre à l'agent suffisamment d'options pour apprendre tout en conservant une expérience gérable.
- **Laissez-lui du temps :** L'agent a besoin de données suffisantes pour apprendre. Prévoyez au moins deux à quatre semaines avant de tirer des conclusions sur les performances.
- **Variez le contenu :** Assurez-vous que vos options sont réellement différentes. Tester des variations mineures peut ne pas fournir d'informations significatives.
- **Surveillez régulièrement :** Consultez le portail Decisioning Studio Go pour suivre la progression des expériences et les indicateurs d'engagement.

## Étapes suivantes {#next-steps}

Une fois que vous avez conçu votre agent et l'avez configuré dans le portail Decisioning Studio Go, vous êtes prêt à le lancer :

- [Lancer votre agent]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/launch_your_agent)