---
nav_title: Utilisation de l'API
article_title: Tableau de bord d'utilisation de l'API
alias: "/api_usage/"
page_order: 5
description: "Cet article fournit un aperçu du tableau de bord d'utilisation de l'API."
---

# Tableau de bord d'utilisation de l'API {#api-usage-dashboard}

> Le tableau de bord d'utilisation de l'API vous permet de surveiller le trafic entrant de l'API REST vers Braze, de comprendre les tendances d'utilisation de nos API REST et de résoudre d'éventuels problèmes.

## À propos du tableau de bord d'utilisation de l'API {#about-the-api-usage-dashboard}

Pour afficher votre tableau de bord d'utilisation de l'API, accédez à **Paramètres** > **Clés API**, puis sélectionnez **Dashboard**.

Par défaut, le tableau de bord affiche l'ensemble des requêtes entrantes de l'API REST pour votre espace de travail au cours de la dernière journée (24 heures). Selon votre cas d'utilisation, vous pouvez ajuster les contrôles du tableau de bord pour filtrer ou regrouper le trafic, ainsi que configurer la plage temporelle.

![Tableau de bord d'utilisation de l'API avec 130 requêtes au total, un taux de réussite de 70 % et un taux d'échec de 30 %.]({% image_buster /assets/img/api_usage_dashboard/api_usage_dashboard.png %})

## Indicateurs disponibles {#available-metrics}

Le tableau de bord d'utilisation de l'API comprend les statistiques suivantes :

| Indicateur | Description |
|----------------|-------------|
| Total des requêtes | Le nombre total de requêtes envoyées à Braze pour votre espace de travail actuel, en fonction des filtres et contrôles appliqués au tableau de bord. |
| Taux de réussite | Le pourcentage de requêtes totales pour lesquelles Braze a renvoyé une réponse de succès `2XX`. |
| Taux d'erreur | Le pourcentage de requêtes totales pour lesquelles Braze a renvoyé une réponse d'erreur `4XX` ou `5XX`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Indicateurs disponibles" }

## Utiliser le tableau de bord {#using-the-dashboard}

![Filtres à appliquer au tableau de bord, notamment : clé API, endpoint, codes de réponse, regroupement des données et date.]({% image_buster /assets/img/api_usage_dashboard/filters.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

### Filtres {#filters}

Sélectionnez **Filters** pour affiner la vue du trafic de l'API REST pour votre espace de travail. Les filtres disponibles sont :

- Clé API
- Endpoint
- Code de réponse

### Regrouper les données {#group-data}

Vous pouvez regrouper les données en différentes séries pour explorer divers schémas d'utilisation :

- Codes de réponse (par défaut)
- Endpoint API
- Clé API
- Réussites et échecs uniquement

### Date {#date}

Ajustez le filtre de date pour afficher une plage temporelle plus courte ou plus longue selon vos besoins. Les options disponibles sont :

- Aujourd'hui (par défaut)
- Personnalisé
- 3 dernières heures
- 6 dernières heures
- 12 dernières heures
- 24 dernières heures
- Hier
- 7 derniers jours
- 14 derniers jours
- 30 derniers jours
- Mois en cours

{% alert note %}
Les options **3 dernières heures** et **6 dernières heures** affichent le trafic par minute. Les périodes plus longues affichent le trafic toutes les cinq minutes, par heure ou par jour.
{% endalert %}

## Remarques {#considerations}

Le tableau de bord d'utilisation de l'API inclut toutes les requêtes de l'API REST reçues par Braze et pour lesquelles une réponse `2XX`, `4XX` ou `5XX` a été renvoyée. Cela comprend les sorties de Transformation des données et les synchronisations d'Ingestion de données cloud. Le trafic SDK et les étapes de Mise à jour utilisateur ne sont pas inclus dans ce tableau de bord.

Les données affichées peuvent présenter un léger délai pour le trafic récent. En période de forte utilisation, vous pouvez actualiser le tableau de bord jusqu'à 4 fois par minute. Il peut être nécessaire d'attendre quelques minutes avant de pouvoir l'actualiser à nouveau.

## Articles connexes {#related-articles}

- [Alertes d'utilisation de l'API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts/)
- [Limites de débit]({{site.baseurl}}/api/api_limits/)