---
nav_title: Données
article_title: Données
page_order: 3
description: "Découvrez la plateforme de données Braze, notamment comment unifier, activer et distribuer vos données."
---

# Plateforme de données Braze {#braze-data-platform}

> Découvrez la plateforme de données Braze, notamment comment unifier, activer et distribuer vos données.

La plateforme de données Braze (BDP) est un ensemble complet et composable de fonctionnalités de données et d'intégrations partenaires qui vous permet de créer des expériences personnalisées pour vos clients. Chez Braze, nous envisageons les données sous l'angle de trois missions clés : l'[unification]({{site.baseurl}}/user_guide/data/unification/), l'[activation]({{site.baseurl}}/user_guide/data/activation/) et la [distribution]({{site.baseurl}}/user_guide/data/distribution/).

En combinant les fonctionnalités de la plateforme de données Braze, vous pouvez exploiter vos données pour créer des messages pertinents et ciblés qui réagissent en temps réel aux actions de vos clients.

## Fonctionnement {#how-it-works}

### Unifier vos données {#unify-your-data}

Les données utilisateur affluent dans Braze par de nombreux points d'entrée. Collectez et consolidez vos données first-party depuis n'importe quelle source grâce aux [API]({{site.baseurl}}/api/home/) et aux [SDK]({{site.baseurl}}/developer_guide/sdk_integration/). Vous pouvez également utiliser des outils d'ingestion intégrés comme l'[Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/) pour créer une intégration directe entre votre entrepôt de données ou votre solution de stockage de fichiers et Braze, ou utiliser la [Transformation des données]({{site.baseurl}}/user_guide/data/unification/data_transformation/) pour créer et gérer des intégrations webhook afin de transférer des données vers Braze.

### Activer vos données {#activate-your-data}

Nettoyez, organisez et préparez vos données pour les exploiter. Cela implique de comprendre les comportements et les préférences de vos clients en temps réel grâce aux profils utilisateurs et aux segments. Consultez le [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/analytics/metrics_glossary/) lorsque vous créez des messages ciblés, et utilisez les [catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs/) pour enrichir vos messages avec des données produit ou de contenu. Identifiez comment vos clients réagissent à ces expériences personnalisées.

### Distribuer vos données {#distribute-your-data}

Diffusez et [exportez vos données]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/) vers des systèmes externes pour approfondir vos analyses et éclairer vos décisions. Utilisez [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) pour diffuser les données d'événements Braze vers un entrepôt de données et alimenter vos outils d'aide à la décision. Vous pouvez également étendre vos capacités en matière de données grâce aux [intégrations partenaires technologiques]({{site.baseurl}}/partners/data_and_analytics/).

## Infrastructure de données {#data-infrastructure}

L'infrastructure de données de Braze comprend des [centres de données]({{site.baseurl}}/user_guide/data/infrastructure/data_centers/) qui contribuent à minimiser la latence, c'est-à-dire le temps nécessaire pour que les données transitent entre le serveur et l'utilisateur. Cette répartition géographique permet à nos services d'être fiables et évolutifs. Nous proposons également le [chiffrement au niveau des champs]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption/) pour protéger les données sensibles et limiter les informations personnellement identifiables (PII) partagées dans Braze. Pour en savoir plus sur l'utilisation et la facturation, consultez [Points de données]({{site.baseurl}}/user_guide/data/infrastructure/data_points/).

## Principes fondamentaux {#core-principles}

Les données jouent un rôle crucial dans l'amélioration de votre stratégie d'engagement client en vous permettant de créer des expériences personnalisées, de comprendre le comportement des clients et d'optimiser vos stratégies d'envoi de messages. Chez Braze, nous développons toutes nos fonctionnalités de données en gardant à l'esprit trois principes fondamentaux :

{% details Renforcer l'efficacité de vos données %}
- **Flexible et modulaire :** Notre objectif principal est de vous aider à utiliser vos données de manière plus efficace et plus complète. Grâce à une architecture composable, vous pouvez exploiter les technologies dont vous avez besoin pour tirer le meilleur parti de vos données, sans intergiciel superflu.
- **Intégrations partenaires :** Braze privilégie les intégrations avec les meilleures technologies de l'écosystème (et propose des API) qui facilitent le partage bidirectionnel des données en temps réel.
- **Architecture de traitement en continu :** Vous pouvez déclencher des actions sur n'importe quel point de donnée ingéré dans Braze à des fins de segmentation, d'orchestration et de personnalisation.
{% enddetails %}

{% details Améliorer l'agilité des données pour favoriser la performance %}
- **Construction d'audience flexible :** Réduisez la dépendance vis-à-vis des équipes techniques pour créer des audiences et offrir un engagement client personnalisé à grande échelle.
- **Vitesse et performance :** Les données et les informations relatives à l'engagement sont fournies en temps réel, ce qui favorise un engagement client itératif et efficace, ainsi qu'une prise de décision plus éclairée à l'échelle de l'entreprise.
{% enddetails %}

{% details Garantir la sécurité, la protection et la conformité de vos données %}
- **Des pratiques de sécurité à la pointe du secteur :** Nous réalisons régulièrement des audits par des tiers, notamment SOC 2 Type 2 et ISO 27001, afin de respecter les normes les plus strictes du secteur. Nous maintenons un programme public de bug bounty pour remédier de manière proactive aux vulnérabilités potentielles et disposons d'une équipe de sécurité dédiée qui s'engage à protéger vos données.
- **Conformité réglementaire :** Nous fournissons des outils qui favorisent le respect des réglementations en matière de protection des données, notamment le RGPD et le CCPA.
- **Confidentialité des données :** Vous pouvez gérer le consentement de l'utilisateur final, traiter les demandes et agir sur les droits des consommateurs.
{% enddetails %}