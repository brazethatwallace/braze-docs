---
nav_title: Connecter vos données
article_title: Connecter vos données
page_order: 6
description: "Découvrez comment connecter les sources de données clients à BrazeAI Decisioning Studio pour une prise de décision IA personnalisée."
---

# Connecter vos données {#connect-your-data}

> Les agents BrazeAI Decisioning Studio™ doivent comprendre pleinement le contexte client pour prendre des décisions efficaces. Cet article explique comment connecter les sources de données clients à Decisioning Studio.

{% alert tip %}
Votre équipe AI Decisioning Services vous accompagnera dans la configuration des connexions de données pour des performances optimales.
{% endalert %}

## Modèles d'intégration pris en charge {#supported-integration-patterns}

Decisioning Studio prend en charge plusieurs modèles d'intégration pour connecter les données clients :

| Modèle d'intégration | Idéal pour | Complexité de configuration |
|---------------------|----------|------------------|
| **Braze Data Platform** | Les clients utilisant déjà Braze | Faible |
| **Ingestion de données cloud Braze (CDI)** | Connecter des entrepôts de données externes | Moyenne |
| **Stockage cloud (GCS, AWS, Azure)** | Exports de données directs depuis d'autres plateformes | Moyenne |
| **Intégrations CEP** | Extensions de données SFMC, Klaviyo | Moyenne |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Modèles d'intégration pris en charge" }

## Types de données clients {#customer-data-types}

Les ressources de données clients suivantes aident les agents à personnaliser plus efficacement :

| Type de données | Description | Exemples |
|-----------|-------------|----------|
| **Profil client** | Attributs statiques et à évolution lente | Ancienneté en tant que client, géographie, canal d'acquisition, niveau de satisfaction, estimation de la valeur vie client |
| **Comportement client** | Activité et schémas d'engagement | Connexions au compte, type d'appareil, interactions avec le service client, utilisation du produit |
| **Historique des transactions** | Données d'achat et de conversion | Produits achetés, montants des transactions, méthodes de paiement, canaux d'achat |
| **Engagement marketing** | Réponses aux communications | Ouvertures/clics d'e-mails, engagement SMS, activité web et mobile, réponses aux enquêtes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Types de données clients" }

{% alert tip %}
Plus les agents disposent d'informations sur vos clients, meilleures seront leurs performances. Pensez à inclure des données sur les informations particulièrement importantes pour votre activité (par exemple, souhaitez-vous voir comment l'IA traite différemment vos clients fidèles ? Assurez-vous que le statut de fidélité figure dans les données clients).
{% endalert %}

## Connecter les données par plateforme {#connect-data-by-platform}

{% tabs %}
{% tab Braze %}

### Envoyer les données clients via Braze {#send-customer-data-through-braze}

BrazeAI Decisioning Studio peut utiliser toutes les données que vous envoyez déjà à la Braze Data Platform.

S'il existe des données clients que vous souhaitez utiliser pour Decisioning Studio et qui ne sont pas actuellement stockées dans le profil utilisateur ou les attributs personnalisés, l'approche recommandée est d'utiliser l'[Ingestion de données cloud Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) pour ingérer des données provenant d'autres sources.

CDI prend en charge les intégrations directes avec :

- Snowflake
- Redshift
- BigQuery
- Databricks
- Microsoft Fabric
- AWS S3

Pour la liste complète des sources prises en charge, consultez [Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Une fois que vous êtes satisfait des données que vous envoyez à la Braze Data Platform, contactez votre équipe AI Decisioning Services pour discuter des champs du profil utilisateur ou des attributs personnalisés à utiliser pour la décision automatisée par IA.

Pour simplifier ce processus, créez une liste des attributs du profil utilisateur Braze qui représentent le mieux les comportements de vos clients et qui devraient être utilisés dans Decisioning Studio (consultez la [liste des champs disponibles]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#fields-to-export)). Votre équipe Services peut également vous aider à mener des sessions de découverte pour déterminer quels champs sont les plus appropriés pour la décision automatisée par IA.

Les autres options pour envoyer des données incluent :

- L'envoi d'événements personnalisés Braze via le SDK
- L'envoi d'événements via l'endpoint REST ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))

Ces approches nécessitent davantage d'efforts d'ingénierie, mais sont parfois préférables selon votre configuration Braze actuelle. Contactez l'équipe AI Decisioning Services pour en savoir plus.

{% endtab %}
{% tab SFMC %}

### Envoyer les données clients via SFMC {#send-customer-data-through-sfmc}

Pour les intégrations Salesforce Marketing Cloud :

1. Configurez les extensions de données SFMC pour vos données clients.
2. Mettez en place un package installé SFMC pour l'intégration API avec les autorisations appropriées requises par Decisioning Studio.
3. Assurez-vous que les extensions de données sont actualisées quotidiennement, car Decisioning Studio extraira les dernières données incrémentielles disponibles.

Fournissez l'ID de l'extension et la clé API à votre équipe AI Decisioning Services. Elle vous assistera pour les étapes suivantes de l'ingestion des données clients.

{% endtab %}
{% tab Klaviyo %}

### Envoyer les données clients via Klaviyo {#send-customer-data-through-klaviyo}

Pour les intégrations Klaviyo :

1. Confirmez que les données de profil client sont disponibles dans les profils Klaviyo.
2. Générez une clé API privée avec un accès complet aux profils.
3. Fournissez la clé API à votre équipe AI Decisioning Services.

Consultez la [documentation Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908) pour plus d'informations sur la configuration des clés API.

{% endtab %}
{% tab Cloud Storage %}

### Autres solutions cloud (Google Cloud Storage, Azure, AWS) {#other-cloud-solutions-google-cloud-storage-azure-aws}

Si les données clients ne sont pas actuellement stockées dans Braze, SFMC ou Klaviyo, la meilleure étape suivante est de configurer un export automatisé directement vers un compartiment Google Cloud Storage contrôlé par Braze. Nous pouvons également prendre en charge l'export vers AWS ou Azure (bien que GCS soit préférable). Pour ces plateformes, exportez vers leur stockage cloud interne et Braze pourra ensuite récupérer ces données.

Pour déterminer si cela est faisable, consultez la documentation de votre plateforme Martech. Par exemple :

- mParticle propose une [intégration native avec Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/)
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

Si cela est faisable, nous pouvons fournir un compartiment GCS dédié à Decisioning Studio pour y exporter les données clients.

{% endtab %}
{% endtabs %}

## Bonnes pratiques {#best-practices}

- **Noms de colonnes descriptifs :** les données clients doivent avoir des noms de colonnes clairs et descriptifs. Idéalement, un dictionnaire de données devrait être fourni.
- **Mises à jour incrémentielles :** les fichiers incrémentiels sont préférables aux instantanés de l'ensemble de l'historique client chaque jour.
- **Identifiants cohérents :** chaque enregistrement doit contenir un identifiant client unique et cohérent à travers toutes les ressources de données.
- **Inclure des horodatages :** les enregistrements doivent avoir des horodatages associés pour une attribution précise et l'entraînement des agents.

## Intégrations personnalisées {#custom-integrations}

D'autres options ou des pipelines de données entièrement personnalisés sont possibles. Ceux-ci peuvent nécessiter des travaux supplémentaires de la part de l'équipe Services ou de l'équipe d'ingénierie de votre côté. Pour déterminer ce qui est faisable et optimal, travaillez avec votre équipe AI Decisioning Services.

{% alert important %}
Ce guide explique les modèles d'intégration les plus courants. L'équipe Sécurité de l'information devra encore valider tous les points de connexion et les consultants en solutions seront disponibles pour conseiller sur l'implémentation.
{% endalert %}

## Étapes suivantes {#next-steps}

Après avoir connecté vos sources de données, procédez à la mise en place de l'orchestration :

- [Configurer l'orchestration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/orchestration_setup)