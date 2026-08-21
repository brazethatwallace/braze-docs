---
nav_title: Tableaux de bord SQL Order Placed
article_title: Créer des rapports sur les événements eCommerce Order Placed dans le générateur de tableaux de bord
page_order: 1
page_type: reference
description: "Utilisez le SQL du générateur de requêtes sur les événements ecommerce.order_placed pour créer des tuiles de chiffre d'affaires et de commandes dans le générateur de tableaux de bord pour le reporting eCommerce."
tool: Reports
---

# Créer des rapports sur les événements eCommerce Order Placed dans le générateur de tableaux de bord {#report-on-ecommerce-order-placed-events-in-dashboard-builder}

> Créez des graphiques personnalisés de chiffre d'affaires et de commandes à partir des événements recommandés `ecommerce.order_placed` en enregistrant des requêtes SQL dans le générateur de requêtes et en visualisant les résultats dans le générateur de tableaux de bord.

## À propos de cet exemple {#about-this-example}

Flash et Thread, une marque fictive de vêtements, enregistre les commandes avec les [événements recommandés eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events). Son équipe marketing souhaite disposer du chiffre d'affaires quotidien, de la valeur moyenne de commande (AOV) et du volume de commandes dans un seul tableau de bord, et pas uniquement de la vue d'attribution au dernier point de contact préconfigurée.

Ce modèle utilise le générateur de requêtes pour interroger `ecommerce.order_placed` à partir des tables d'événements partagées Snowflake, puis ajoute la requête enregistrée en tant que tuile **Custom Queries** dans le générateur de tableaux de bord. Vous pouvez reproduire ce flux de travail pour des indicateurs supplémentaires (nouveaux acheteurs versus acheteurs récurrents, catégories de produits ou chiffre d'affaires par segment).

Utilisez cette approche lorsque les tableaux de bord eCommerce intégrés ne couvrent pas votre combinaison d'indicateurs. Pour le chiffre d'affaires attribué au dernier point de contact, consultez plutôt le tableau de bord [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#revenue---last-touch-attribution).

## Considérations {#considerations}

- **Déploiement de l'événement :** `ecommerce.order_placed` doit être déployé et envoyer `total_value` (ainsi que les données produit si nécessaire) avant que les requêtes ne renvoient des données. Si vous utilisez le [connecteur Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), les événements recommandés peuvent déjà être disponibles.
- **Accès au générateur de requêtes :** Vous avez besoin de la [permission utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) « View PII » pour utiliser le générateur de requêtes.
- **Conservation des données :** Le générateur de requêtes renvoie par défaut les données des 60 derniers jours. Avec le [partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake), vous pouvez interroger jusqu'à deux ans de données conservées. Consultez [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder).
- **Délais d'expiration :** Les requêtes qui s'exécutent pendant plus de six minutes expirent. Réduisez la plage de dates, filtrez sur `TIME` ou diminuez la taille de l'audience si un rapport échoue. Les tables d'événements sont regroupées sur `TIME` ; privilégiez le filtrage sur le moment où l'événement s'est produit.
- **Champ de chiffre d'affaires :** Les exemples de requêtes additionnent `total_value` à partir des `properties` de l'événement. Le chiffre d'affaires eCommerce standardisé de Braze dans les rapports produit est souvent dérivé du `price` et de la `quantity` de chaque produit. Alignez `total_value` avec vos lignes de produits, ou ajustez le SQL pour correspondre à votre schéma.
- **Libellés de colonnes :** Encadrez les noms de colonnes affichés entre guillemets doubles (par exemple `"Date"`, `"Total Revenue"`) afin que le générateur de tableaux de bord affiche des en-têtes d'axes et de tableaux lisibles.
- **Tests :** Le SQL de cet article est fourni à titre d'exemple. Validez les requêtes dans votre espace de travail avant de partager largement les tableaux de bord.

## Configuration {#setup}

### Étape 1 : Créer une requête SQL pour le chiffre d'affaires quotidien {#step-1-create-a-sql-query-for-daily-revenue}

1. Accédez à **Analytics** > **Query Builder**.
2. Sélectionnez **Create SQL Query**, puis **SQL Editor**.
3. Nommez la requête (par exemple, `Flash Thread — daily eCommerce revenue`).
4. Collez et adaptez la requête suivante pour le chiffre d'affaires total par jour calendaire sur les 60 derniers jours :

{% raw %}
```sql
SELECT
  DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME))::DATE AS "Date",
  SUM(PARSE_JSON(PROPERTIES):total_value::NUMBER(18, 2)) AS "Total Revenue"
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED
WHERE NAME = 'ecommerce.order_placed'
  AND TO_TIMESTAMP_NTZ(TIME) >= DATEADD(day, -60, CURRENT_TIMESTAMP())
  AND TO_TIMESTAMP_NTZ(TIME) <= CURRENT_TIMESTAMP()
GROUP BY 1
ORDER BY 1;
```
{% endraw %}

{:start="5"}
5. Sélectionnez **Run Query**, puis sélectionnez **Save**.

Pour plus de détails sur la configuration du générateur de requêtes, consultez [Exécuter des rapports dans le générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder#running-reports-in-the-query-builder).

### Étape 2 : Ajouter la requête à une tuile du générateur de tableaux de bord {#step-2-add-the-query-to-a-dashboard-builder-tile}

1. Accédez à **Analytics** > **Dashboard Builder**.
2. Sélectionnez **Create Dashboard** (ou ouvrez un tableau de bord existant).
3. Pour la source de données, sélectionnez **Custom Queries**.
4. Sélectionnez **+ Add Tile**, puis choisissez la requête que vous avez enregistrée à l'étape 1.
5. Sélectionnez l'icône de crayon pour modifier la tuile :
   - Définissez le type de graphique sur **Line graph**.
   - Définissez l'**axe X** sur `Date`.
   - Définissez l'**axe Y** sur `Total Revenue`.
6. Redimensionnez la tuile selon vos besoins, puis sélectionnez **Save**.
7. Sélectionnez **View Dashboard** > **Run Dashboard**.

La génération du tableau de bord peut prendre quelques minutes. Consultez [Créer un tableau de bord personnalisé]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#creating-a-custom-dashboard).

### Étape 3 : Ajouter des indicateurs *Order Placed* supplémentaires (facultatif) {#step-3-add-additional-_order-placed_-metrics-optional}

Créez des requêtes enregistrées séparées, puis ajoutez chacune en tant que tuile individuelle (jusqu'à 10 tuiles par tableau de bord).

#### Valeur moyenne de commande et nombre de commandes par jour {#average-order-value-and-order-count-per-day}

{% raw %}
```sql
SELECT
  DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME))::DATE AS "Date",
  AVG(PARSE_JSON(PROPERTIES):total_value::NUMBER(18, 2)) AS "Average Order Value",
  COUNT(*) AS "No. of Orders"
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED
WHERE NAME = 'ecommerce.order_placed'
  AND TO_TIMESTAMP_NTZ(TIME) >= DATEADD(day, -60, CURRENT_TIMESTAMP())
  AND TO_TIMESTAMP_NTZ(TIME) <= CURRENT_TIMESTAMP()
GROUP BY 1
ORDER BY 1;
```
{% endraw %}

Utilisez un graphique en courbes ou en barres avec `Date` sur l'axe X et les deux indicateurs sur l'axe Y (désélectionnez les colonnes que vous ne souhaitez pas afficher).

#### Nouveaux acheteurs versus acheteurs récurrents par jour {#new-versus-returning-purchasers-per-day}

Ce modèle compare le premier jour d'achat `ecommerce.order_placed` de chaque utilisateur aux jours d'achat ultérieurs. Il est plus précis lorsque la fenêtre de votre générateur de requêtes couvre l'intégralité de la période de reporting (par exemple, la fenêtre par défaut de 60 jours).

{% raw %}
```sql
WITH order_days AS (
  SELECT DISTINCT
    USER_ID,
    DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME))::DATE AS purchase_day
  FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED
  WHERE NAME = 'ecommerce.order_placed'
),
first_purchase AS (
  SELECT
    USER_ID,
    MIN(purchase_day) AS first_day
  FROM order_days
  GROUP BY USER_ID
),
per_day_purchasers AS (
  SELECT DISTINCT
    USER_ID,
    purchase_day
  FROM order_days
)
SELECT
  p.purchase_day AS "Date",
  COUNT(DISTINCT CASE
    WHEN f.first_day = p.purchase_day THEN p.USER_ID
  END) AS "New Purchasers",
  COUNT(DISTINCT CASE
    WHEN f.first_day < p.purchase_day THEN p.USER_ID
  END) AS "Returning Purchasers"
FROM per_day_purchasers AS p
INNER JOIN first_purchase AS f
  ON p.USER_ID = f.USER_ID
GROUP BY 1
ORDER BY 1;
```
{% endraw %}

#### Catégorie de produit à partir des lignes de commande {#product-category-from-order-line-items}

Aplatissez le tableau `products` et filtrez sur votre champ de catégorie. Remplacez `metadata.category` si vous utilisez une clé de métadonnées produit différente.

{% raw %}
```sql
SELECT
  f.value:metadata:category::STRING AS "Product Category",
  COUNT(*) AS "Line Items"
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED,
  LATERAL FLATTEN(INPUT => PARSE_JSON(PROPERTIES):products) f
WHERE NAME = 'ecommerce.order_placed'
  AND f.value:metadata:category::STRING IS NOT NULL
  AND TRIM(f.value:metadata:category::STRING) != ''
  AND LOWER(TRIM(f.value:metadata:category::STRING)) != 'undefined'
GROUP BY 1
ORDER BY 2 DESC;
```
{% endraw %}

#### Achats et chiffre d'affaires par segment (analyse de segment) {#purchases-and-revenue-by-segment-segment-analytics}

Cela nécessite le [suivi analytique de segment]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) sur les segments sur lesquels vous créez des rapports. Utilisez les [variables SQL]({{site.baseurl}}/user_guide/analytics/reports/query_builder/sql_variables) pour les sélecteurs de dates.

{% raw %}
```sql
WITH event_conversions AS (
  SELECT
    user_id,
    time,
    TRY_CAST(GET_PATH(PARSE_JSON(PROPERTIES), 'total_value')::string AS FLOAT) AS price,
    id AS purchase_event_id,
    f.value::string AS user_segment_membership_id
  FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED,
    LATERAL FLATTEN(input => user_segment_membership_ids) AS f
  WHERE NAME = 'ecommerce.order_placed'
    AND time > {{start_date.${Start Date}}}
    AND time < {{end_date.${End Date}}}
)
SELECT
  user_segment_membership_id AS "Segment Analytics Id",
  COUNT(DISTINCT purchase_event_id) AS "Total Purchases",
  ROUND(SUM(price), 2) AS "Total Revenue"
FROM event_conversions
GROUP BY 1
ORDER BY 3 DESC;
```
{% endraw %}

### Autres rapports eCommerce intégrés {#other-built-in-ecommerce-reporting}

| Rapport | À utiliser quand |
| --- | --- |
| [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#revenue---last-touch-attribution) | Chiffre d'affaires attribué au dernier point de contact par Campaign ou Canvas |
| [Rapport d'événements personnalisés]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report) | Volume et fréquence des événements recommandés |
| Conversions de Campaign ou Canvas | `ecommerce.order_placed` est l'événement de conversion principal |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Autres rapports eCommerce intégrés" }

## Articles connexes {#related-articles}

- [Événements recommandés eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)
- [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder)
- [Variables SQL dans le générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder/sql_variables)
- [Générateur de tableaux de bord]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder)
- [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#revenue---last-touch-attribution)
- [Référence des tables SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_BEHAVIORS_CUSTOMEVENT_SHARED)
- [Suivi analytique de segment]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)