---
nav_title: Définir votre audience
article_title: Définir votre audience
page_order: 3
page_type: reference
description: "Découvrez comment définir et configurer l'audience de votre agent BrazeAI Decisioning Studio, y compris les groupes de traitement et les étapes de configuration spécifiques à chaque plateforme."
---

# Définir votre audience {#define-your-audience}

> Les audiences de cas d'utilisation sont généralement définies dans une plateforme d'engagement client (telle que Braze ou Salesforce Marketing Cloud), puis envoyées à l'agent Decisioning Studio. L'agent répartit ensuite les clients en groupes de traitement afin de mener des essais contrôlés randomisés.

## Groupes de traitement {#treatment-groups}

| Groupe | Description |
|--------|-------------|
| **Decisioning Studio** | Clients qui reçoivent des recommandations optimisées par l'intelligence artificielle |
| **Contrôle aléatoire** | Clients qui reçoivent des options sélectionnées aléatoirement (comparaison de référence) |
| **Business-as-Usual (facultatif)** | Clients qui reçoivent le parcours marketing actuel (pour comparer avec les performances existantes) |
| **Holdout (facultatif)** | Clients qui ne reçoivent aucune communication (pour mesurer l'impact global de la campagne) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Groupes de traitement" }

## Configurer votre audience {#configure-your-audience}

{% tabs %}
{% tab Braze %}

1. Créez un segment pour l'audience que vous souhaitez cibler.
2. Fournissez l'ID du segment à votre équipe AI Decisioning Services.

{% alert note %}
Pour Braze, il est possible d'ingérer plusieurs segments et de les combiner pour créer l'audience. Decisioning Studio peut également ingérer un segment pour une campagne de comparaison Business-as-Usual. Tous ces schémas sont acceptables.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

1. Configurez une extension de données SFMC pour votre audience et fournissez l'ID de l'extension de données.
2. Configurez un package installé SFMC pour l'intégration API avec les autorisations appropriées requises par Decisioning Studio.
3. Confirmez que cette extension de données est actualisée quotidiennement, car Decisioning Studio extrait les dernières données incrémentielles disponibles.

Fournissez l'ID de l'extension et la clé API à notre équipe AI Decisioning Services, qui vous assistera pour les prochaines étapes d'ingestion des données clients.

{% endtab %}
{% tab Autres plateformes %}

### Google Cloud Storage

Si l'audience n'est pas actuellement stockée dans Braze ou Salesforce Marketing Cloud, la meilleure étape suivante consiste à configurer un export automatisé directement vers un compartiment Google Cloud Storage (GCS) contrôlé par Braze.

Pour déterminer si cela est faisable, consultez la documentation de votre plateforme. Par exemple, mParticle propose une [intégration native avec Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/). Si c'est le cas, nous pouvons fournir un compartiment GCS vers lequel exporter les données d'audience.

### Ressources supplémentaires {#additional-resources}

- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## Prochaines étapes {#next-steps}

Après avoir défini votre audience, passez à la configuration de l'orchestration :

- [Configurer l'orchestration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/orchestration_setup)