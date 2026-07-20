---
nav_title: API d'exportation
article_title: API d'exportation
page_order: 5
page_type: reference
description: "Cet article de référence vous aide à déterminer quand utiliser les API d'exportation plutôt que les téléchargements CSV depuis le tableau de bord."
platform: API

---

# API d'exportation {#export-apis}

> Cette page vous aide à déterminer quand utiliser les API d'exportation plutôt que les téléchargements CSV depuis le tableau de bord.

Les API d'exportation de Braze vous permettent d'exporter par programme des données Braze au format JSON. Pour en savoir plus sur ce que vous pouvez exporter, les conditions préalables et le fonctionnement de la distribution, consultez les [endpoints d'exportation]({{site.baseurl}}/api/endpoints/export).

## Quand utiliser les API d'exportation plutôt que les téléchargements CSV {#when-to-use-export-apis-instead-of-csv-downloads}

Le tableau suivant décrit les scénarios courants dans lesquels l'utilisation de l'API d'exportation est préférable à un téléchargement CSV depuis le tableau de bord.

| Scénario | Détails |
| --- | --- |
| Votre exportation est trop volumineuse pour le tableau de bord | Les exportations CSV du tableau de bord sont limitées à 500 000 lignes. Si vous exportez des données sur un segment comptant plus de 500 000 utilisateurs, utilisez l'API d'exportation, qui n'impose aucune limite sur la quantité de données exportables. |
| Vous souhaitez automatiser des rapports récurrents | Planifiez des exportations API via une intégration pour récupérer des données à intervalles réguliers sans interaction manuelle avec le tableau de bord. |
| Vous devez alimenter des outils externes en données | Transmettez les données exportées directement vers des outils de BI, des entrepôts de données ou d'autres plateformes d'analyse. |
| Vous avez besoin de données non disponibles en téléchargement CSV depuis le tableau de bord | Certaines catégories de données, notamment les indicateurs clés de performance, les séries de chiffre d'affaires, l'analyse des événements personnalisés et les données de session, ne sont disponibles que via l'API. |
| Vous souhaitez interagir avec les données de manière programmatique | Utilisez la sortie JSON pour des traitements personnalisés, des transformations ou des intégrations. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Quand utiliser les API d'exportation plutôt que les téléchargements CSV" }

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez la [résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}