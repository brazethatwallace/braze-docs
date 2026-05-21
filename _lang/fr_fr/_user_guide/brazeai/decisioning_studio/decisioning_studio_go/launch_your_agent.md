---
nav_title: Lancer votre agent
article_title: Lancer votre agent
page_order: 4
description: "Découvrez comment lancer votre agent BrazeAI Decisioning Studio Go et configurer les rapports Business as Usual (BAU) pour comparer les performances."
---

# Lancer votre agent {#launch-your-agent}

> Une fois que vous avez connecté vos sources de données, configuré l'orchestration et conçu votre agent, vous êtes prêt à le lancer. Cet article traite de l'activation de votre agent et de la configuration facultative des rapports BAU.

## Étapes de lancement {#launch-steps}

Après avoir effectué toutes les étapes de configuration dans le portail Decisioning Studio Go :

1. Vérifiez la configuration de votre agent pour vous assurer que tous les paramètres sont corrects.
2. Vérifiez que votre intégration CEP est active et que l'orchestration est prête.
3. Sélectionnez **Launch** (ou l'action équivalente) dans le portail Decisioning Studio Go pour activer votre agent.

Une fois lancé, votre agent va :
- Commencer à recevoir les données d'audience de votre CEP
- Formuler des recommandations personnalisées pour chaque client
- Orchestrer les envois via votre CEP configuré
- Collecter des données d'engagement pour apprendre et s'améliorer au fil du temps

## Configurer les rapports BAU {#set-up-bau-reporting}

Par défaut, les rapports du portail Decisioning Studio Go comparent le groupe Decisioning Studio Go au groupe de contrôle aléatoire. Si vous disposez d'une campagne Business as Usual (BAU) existante que vous souhaitez comparer, vous pouvez configurer les rapports BAU afin de visualiser les trois groupes en un seul endroit.

### Avantages des rapports BAU {#benefits-of-bau-reporting}

Le principal avantage de la mise en place des rapports BAU réside dans l'application du filtrage des clics non valides de Decisioning Studio Go. Lorsqu'il est appliqué aux trois groupes expérimentaux, cela permet la comparaison des performances de clics la plus précise et la plus équitable (« comparer ce qui est comparable ») en éliminant le bruit provenant :
- Des clics suspects générés par des machines
- Des clics sur le lien de désabonnement

### Exigences pour les rapports BAU {#requirements-for-bau-reporting}

Avant de configurer les rapports BAU, assurez-vous que la comparaison entre le groupe de traitement BAU, le groupe Decisioning Studio Go et le groupe de contrôle aléatoire est équitable :

- **Pas de chevauchement :** aucun destinataire ne peut appartenir à plus d'un groupe pendant toute la durée de l'expérience.
- **Attribution aléatoire :** les destinataires sont répartis de manière aléatoire dans les groupes, sans aucun biais.
- **Options équivalentes :** toutes les options disponibles pour le groupe BAU (créativité, fréquence, horaire, incitation ou offre) sont également disponibles pour les groupes Decisioning Studio Go et de contrôle aléatoire.

{% alert warning %}
Sans une conception expérimentale permettant de comparer ce qui est comparable, les rapports BAU peuvent être confus ou trompeurs.
{% endalert %}

### Informations requises {#required-information}

Après avoir validé la conception de votre expérience, rassemblez les informations suivantes pour configurer les rapports BAU :

**ID de Campaign provenant de votre CEP :**

| CEP | Types acceptés |
|-----|---------------|
| **Braze** | Campaigns et Canvas |
| **Salesforce Marketing Cloud** | Parcours uniquement |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Required information" }

**ID d'audience provenant de votre CEP :**

| CEP | Types acceptés |
|-----|---------------|
| **Braze** | Segments uniquement |
| **Salesforce Marketing Cloud** | Extensions de données uniquement |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Required information" }

Si vous ne disposez pas d'une audience existante qui suit votre audience BAU, vous devez en créer une.

### Points à prendre en compte {#considerations}

- **Indicateurs de clics uniquement :** à l'instar de Decisioning Studio Go de manière plus générale, les rapports BAU ne couvrent que les indicateurs clés de performance liés aux clics, et non ceux liés à la conversion.
- **Limitations de Canvas :** nous ne prenons actuellement pas en charge le filtrage par ID d'étape Canvas spécifique. Les événements de toutes les étapes Canvas seront inclus dans les données BAU. Cela peut invalider les comparaisons avec le BAU si seules certaines étapes Canvas devaient être incluses.

### Configurer les rapports BAU

Suivez les instructions dans votre portail Decisioning Studio Go. Vous devez disposer de :
- Un ou plusieurs ID de Campaign pour lesquels toutes les communications sont des communications BAU
- Un ID d'audience qui suit quotidiennement les destinataires dans l'audience BAU

## Surveiller votre agent {#monitor-your-agent}

Après le lancement, surveillez les performances de votre agent dans le portail Decisioning Studio Go :

- **Indicateurs d'engagement :** suivez les taux de clics entre les groupes expérimentaux.
- **Progression de l'apprentissage :** observez comment les recommandations de l'agent évoluent au fil du temps.
- **Comparaisons entre groupes :** comparez les performances de Decisioning Studio Go par rapport au contrôle aléatoire et au BAU (si configuré).

{% alert tip %}
Prévoyez au moins deux à quatre semaines de collecte de données avant de tirer des conclusions sur les performances. L'agent a besoin d'interactions suffisantes pour apprendre et s'optimiser efficacement.
{% endalert %}

## Résolution des problèmes {#troubleshooting}

Si votre agent ne fonctionne pas comme prévu :

1. **Vérifiez l'orchestration :** confirmez que votre intégration CEP est active, que les campagnes et les parcours sont en cours d'exécution et qu'aucune limite globale ou règle similaire n'interfère avec l'orchestration.
2. **Vérifiez le flux de données :** confirmez que les données d'audience et d'engagement sont correctement enregistrées.
3. **Examinez les groupes expérimentaux :** assurez-vous que la répartition aléatoire est correcte et qu'il n'y a pas de chevauchement entre les groupes.
4. **Contactez l'assistance :** contactez l'assistance Braze pour obtenir de l'aide.