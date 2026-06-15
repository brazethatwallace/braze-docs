---
nav_title: Databricks
article_title: Databricks
description: "Cet article présente le partage Delta de Databricks avec Braze (bêta fermée), qui vous permet d'accéder aux données d'engagement et de campagne Braze dans votre compte Databricks."
page_type: partner
search_tag: Partner
permalink: /databricks/
hidden: true
---

# Databricks

> [Databricks](https://www.databricks.com/) est une plateforme d'analyse ouverte et unifiée permettant de créer, déployer, partager et maintenir des solutions de données, d'analyse et d'intelligence artificielle de niveau entreprise à grande échelle. La plateforme Databricks Data Intelligence s'intègre au stockage cloud et à la sécurité de votre compte cloud, et gère et déploie l'infrastructure cloud pour vous.

{% alert important %}
Le partage Delta de Databricks avec Braze est en **bêta fermée**. La disponibilité, les régions prises en charge et le comportement du produit peuvent changer. Contactez votre gestionnaire de la satisfaction client Braze pour participer ou pour confirmer si cette fonctionnalité est activée pour votre espace de travail.
{% endalert %}

## Partage Delta (de Braze vers Databricks) {#delta-sharing-braze-to-databricks}

Le [partage Delta](https://docs.databricks.com/en/delta-sharing/index.html) de Databricks vous permet de partager des données de manière sécurisée avec des unités commerciales et des filiales à travers les clouds ou les régions, sans copier ni répliquer les données.

**Utilisez le partage Delta lorsque vous souhaitez :**
- Interroger les données d'événements et de campagne Braze à l'aide de Databricks SQL
- Créer des rapports complexes et effectuer une modélisation d'attribution
- Joindre les données Braze à d'autres données dans votre compte Databricks
- Comparer vos données d'engagement entre les canaux, les secteurs et les plateformes d'appareils

Pour les instructions de configuration, consultez [Partage Delta de Databricks]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/databricks/delta_sharing/).

Pour en savoir plus sur le partage Delta sur Databricks, consultez [Qu'est-ce que le partage Delta ?](https://www.databricks.com/product/delta-sharing).

## Conditions préalables {#prerequisites}

Avant de pouvoir utiliser cette fonctionnalité, effectuez les étapes suivantes :

| Condition | Description |
| ----------- | ----------- |
| Accès à Braze | Pour accéder à cette fonctionnalité dans Braze, contactez votre gestionnaire de compte ou de la satisfaction client Braze. |
| Compte Databricks | Un compte Databricks avec les autorisations `admin`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

Lorsque vous êtes prêt à configurer le partage et à interroger les données partagées, passez à [Partage Delta de Databricks]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/databricks/delta_sharing/).