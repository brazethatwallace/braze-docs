---
nav_title: Données
article_title: "Plateforme de données Braze"
page_order: 3
description: "Découvrez la plateforme de données Braze, notamment comment unifier, activer et distribuer vos données."
---

# Plateforme de données Braze {#braze-data-platform}

> Découvrez la plateforme de données Braze, notamment comment unifier, activer et distribuer vos données.

La plateforme de données Braze (BDP) est un ensemble complet et composable de fonctionnalités de données et d'intégrations partenaires qui vous permet de créer des expériences personnalisées pour vos clients. Chez Braze, nous envisageons les données sous l'angle de trois missions clés : l'[unification]({{site.baseurl}}/user_guide/data/unification), l'[activation]({{site.baseurl}}/user_guide/data/activation) et la [distribution]({{site.baseurl}}/user_guide/data/distribution).

En combinant les fonctionnalités de la plateforme de données Braze, vous pouvez exploiter vos données pour créer des messages pertinents et ciblés qui réagissent en temps réel aux actions de vos clients.

## Fonctionnement {#how-it-works}

### Unifier vos données {#unify-your-data}

Les données utilisateur affluent dans Braze par de nombreux points d'entrée. Collectez et consolidez vos données first-party depuis n'importe quelle source à l'aide des [API]({{site.baseurl}}/api/home) et des [SDK]({{site.baseurl}}/developer_guide/sdk_integration). Vous pouvez également utiliser des outils d'ingestion intégrés comme l'[ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) pour créer une intégration directe entre votre entrepôt de données ou votre solution de stockage de fichiers et Braze, ou utiliser la [transformation de données]({{site.baseurl}}/user_guide/data/unification/data_transformation) pour créer et gérer des intégrations webhook afin de transférer des données dans Braze.

### Activer vos données {#activate-your-data}

Nettoyez, organisez et préparez vos données en vue de leur utilisation. Cela implique de comprendre les comportements et les préférences de vos clients en temps réel grâce aux profils utilisateurs et aux Segments. Consultez le [glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/analytics/metrics_glossary) lorsque vous créez des messages ciblés, et utilisez les [catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs) pour enrichir vos messages avec des données produit ou de contenu. Identifiez la manière dont vos clients réagissent à ces expériences personnalisées.

### Distribuer vos données {#distribute-your-data}

Diffusez et [exportez vos données]({{site.baseurl}}/user_guide/data/distribution/export_braze_data) vers des systèmes externes pour des informations et des décisions complémentaires. Utilisez [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) pour diffuser les données d'événements Braze vers un entrepôt de données afin d'alimenter vos outils d'aide à la décision. Vous pouvez également étendre vos capacités en matière de données grâce aux [intégrations de partenaires technologiques]({{site.baseurl}}/partners/data_and_analytics).

## Infrastructure de données {#data-infrastructure}

L'infrastructure de données de Braze comprend des [centres de données]({{site.baseurl}}/user_guide/data/infrastructure/data_centers) qui permettent de minimiser la latence, c'est-à-dire le temps que mettent les données à transiter entre le serveur et l'utilisateur. Cette répartition géographique permet à nos services d'être fiables et évolutifs. Nous proposons également le [chiffrement au niveau des champs]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption) pour protéger les données sensibles et minimiser les données d'identification partagées dans Braze. Pour en savoir plus sur l'utilisation et la facturation, consultez [Points de données]({{site.baseurl}}/user_guide/data/infrastructure/data_points).

## Principes fondamentaux {#core-principles}

Les données jouent un rôle crucial dans l'amélioration de votre stratégie d'engagement client en vous permettant de créer des expériences personnalisées, de comprendre le comportement des clients et d'optimiser vos stratégies de communication. Chez Braze, nous développons toutes nos capacités de données en gardant à l'esprit trois principes fondamentaux :

{% details Faire travailler vos données plus efficacement %}
- **Flexibilité et approche modulaire :** Notre objectif principal est de vous aider à exploiter vos données de manière plus efficace et plus complète. Grâce à une architecture composable, vous pouvez tirer parti des technologies dont vous avez besoin pour faire travailler vos données plus efficacement, sans middleware superflu.
- **Intégrations partenaires :** Braze privilégie les intégrations avec les meilleures technologies de l'écosystème (et propose des API) qui rendent le partage de données bidirectionnel en temps réel simple et direct.
- **Architecture de traitement de flux :** Vous pouvez déclencher des actions sur n'importe quel point de donnée ingéré dans Braze à des fins de segmentation, d'orchestration et de personnalisation.
{% enddetails %}

{% details Renforcer l'agilité des données pour améliorer les performances %}
- **Construction d'audiences flexible :** Réduisez votre dépendance aux équipes techniques pour créer des audiences et offrir un engagement client personnalisé à grande échelle.
- **Rapidité et performance :** Les données d'engagement et les informations sont livrées en temps réel, ce qui favorise un engagement client itératif et efficace, ainsi qu'une prise de décision plus large pour l'entreprise.
{% enddetails %}

{% details Garantir la sécurité, la protection et la conformité de vos données %}
- **Pratiques de sécurité de référence dans l'industrie :** Nous réalisons régulièrement des audits par des tiers, notamment SOC 2 Type 2 et ISO 27001, pour respecter les normes les plus exigeantes du secteur. Nous maintenons un programme public de bug bounty pour identifier proactivement les vulnérabilités potentielles et disposons d'une équipe de sécurité dédiée à la protection de vos données.
- **Conformité sectorielle :** Nous fournissons des outils qui favorisent le respect des réglementations en matière de protection des données, notamment le RGPD et le CCPA.
- **Confidentialité des données :** Vous pouvez gérer le consentement des utilisateurs finaux, traiter les demandes et appliquer les droits des consommateurs.
{% enddetails %}