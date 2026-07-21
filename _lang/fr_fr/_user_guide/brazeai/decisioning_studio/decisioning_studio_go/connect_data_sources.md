---
nav_title: Connecter les sources de données
article_title: Connecter les sources de données
page_order: 1
description: "Découvrez comment BrazeAI Decisioning Studio Go se connecte à vos données clients via votre plateforme d'engagement client."
---

# Connecter les sources de données {#connect-data-sources}

> BrazeAI Decisioning Studio™ Go se connecte à vos données clients via votre plateforme d'engagement client (CEP). Cet article explique quelles données sont utilisées et comment la connexion fonctionne.

## Comment Go accède aux données clients {#how-go-accesses-customer-data}

Contrairement à Decisioning Studio Pro, qui prend en charge l'intégration directe de données provenant de diverses sources, Decisioning Studio Go accède aux données clients via votre CEP. Cela signifie :

- **Les données d'audience** sont extraites directement des segments ou des listes définis dans votre CEP (Braze ou Salesforce Marketing Cloud) et ne peuvent inclure que certains attributs prédéfinis (pas de données 1P).
- **Les données d'engagement** (ouvertures, clics, envois) sont collectées via des requêtes automatisées ou des intégrations natives avec votre CEP.
- **Aucune configuration supplémentaire du pipeline de données** n'est nécessaire au-delà de celle que vous avez définie dans votre CEP.

## Modèles d'intégration pris en charge {#supported-integration-patterns}

Decisioning Studio Go prend en charge les CEP suivants pour l'accès aux données :

| CEP | Source de l'audience | Données d'engagement |
|-----|-----------------|-----------------|
| **Braze** | Segments | Exportation Braze Currents |
| **Salesforce Marketing Cloud** | Extensions de données | Automatisation des requêtes SQL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Modèles d'intégration pris en charge" }

## Exigences en matière de données par CEP {#data-requirements-by-cep}

{% tabs %}
{% tab Braze %}

### Exigences relatives aux données Braze {#braze-data-requirements}

Pour les intégrations Braze, Decisioning Studio Go requiert :

1. **Braze Currents :** Braze Currents doit être activé et configuré pour exporter les données d'engagement vers Decisioning Studio Go. Cela permet à l'agent de tirer des enseignements des réponses des clients.

2. **Accès aux segments :** La clé API que vous créez doit disposer des autorisations nécessaires pour accéder aux segments qui définissent votre audience cible.

3. **Données du profil utilisateur :** Tous les attributs de profil utilisateur ou attributs personnalisés que vous souhaitez que l'agent prenne en compte doivent être accessibles via l'API Braze.

{% alert important %}
Assurez-vous que votre exportation Braze Currents inclut les données de toutes les campagnes que vous souhaitez comparer (y compris les campagnes BAU).
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

### Exigences relatives aux données SFMC {#sfmc-data-requirements}

Pour les intégrations Salesforce Marketing Cloud, Decisioning Studio Go requiert :

1. **Extensions de données :** Votre audience doit être définie dans une extension de données accessible par Decisioning Studio Go. Utilisez la SubscriberKey comme identifiant utilisateur principal.
2. **Accès aux événements de suivi :** Tant que le package d'application installé prend en charge la configuration automatisée de bout en bout, aucune configuration supplémentaire n'est nécessaire.

Les extensions de données et les requêtes SQL sont configurées dans le cadre de la [configuration de votre agent Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup).

{% endtab %}
{% endtabs %}

## Bonnes pratiques {#best-practices}

- **Maintenir les données à jour :** Mettez régulièrement à jour vos segments d'audience et vos données clients (au minimum quotidiennement) afin que l'agent puisse travailler avec des informations actuelles.
- **Inclure les attributs pertinents :** Réfléchissez aux caractéristiques des clients susceptibles d'influencer les messages qui trouvent un écho : les données démographiques, l'historique d'engagement, le comportement d'achat et le stade du cycle de vie sont autant de signaux précieux.

## Étapes suivantes {#next-steps}

Maintenant que vous comprenez comment Go se connecte aux données, configurez votre agent dans le tableau de bord de Braze :

- [Configurer votre agent Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup)