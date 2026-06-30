---
nav_title: Générateur de requêtes
article_title: Générateur de requêtes
page_order: 4
description: "Cet article de référence décrit comment créer des rapports à partir des données de Braze dans Snowflake à l'aide du Générateur de requêtes."
tool: Reports
alias: /query_builder/
---

# Générateur de requêtes {#query-builder}

> Le Générateur de requêtes génère des rapports à partir des données de Braze dans Snowflake. Il est fourni avec des [modèles de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates) SQL prédéfinis pour vous aider à démarrer, ou vous pouvez écrire vos propres requêtes SQL personnalisées pour obtenir encore plus d'informations.

Étant donné que le Générateur de requêtes permet un accès direct à certaines données client, vous ne pouvez y accéder que si vous disposez de l'[autorisation]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) « View PII ».

## Tables de données disponibles {#available-data-tables}

Le Générateur de requêtes utilise les mêmes tables SQL Snowflake que les [Extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) et le [Partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). Pour une liste complète des tables disponibles et de leurs colonnes, consultez la [référence des tables SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables).

## Exécuter des rapports dans le Générateur de requêtes {#running-reports-in-the-query-builder}

Pour exécuter un rapport dans le Générateur de requêtes :

1. Accédez à **Analytics** > **Query Builder**.
2. Sélectionnez **Create SQL Query**. Si vous avez besoin d'inspiration ou d'aide pour rédiger votre requête, sélectionnez **Query Template** et choisissez un modèle dans la liste. Sinon, sélectionnez **SQL Editor** pour accéder directement à l'éditeur.
3. Votre rapport reçoit automatiquement un nom avec la date et l'heure actuelles. Survolez le nom et sélectionnez <i class="fas fa-pencil" alt="Modifier"></i> pour donner un nom significatif à votre requête SQL.
4. Écrivez votre requête SQL dans l'éditeur ou [obtenez l'aide de l'IA](#ai-query-builder) depuis l'onglet **AI Query Builder**. Si vous écrivez votre propre SQL, consultez [Écrire des requêtes SQL personnalisées](#custom-sql) pour les exigences et les ressources.
5. Sélectionnez **Run Query**.
6. Enregistrez votre requête.
7. Pour télécharger un CSV de votre rapport, sélectionnez **Export**.

![Le Générateur de requêtes affichant les résultats de la requête modèle « Channel engagement and revenue for the last 30 days ».]({% image_buster /assets/img_archive/query_builder.png %})

Les résultats de chaque rapport peuvent être générés une fois par jour. Si vous exécutez le même rapport plus d'une fois dans une même journée calendaire, vous verrez les mêmes résultats dans les deux rapports.

### Modèles de requêtes {#query-templates}

Accédez aux modèles de requêtes en sélectionnant **Create SQL Query** > **Query Template** lors de la création initiale d'un rapport.

Consultez [Modèles de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates) pour une liste des modèles disponibles.

### Période des données {#data-timeframe}

Les requêtes renvoient les données des 60 derniers jours. Si vous utilisez Currents ou le [Partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake), vous pourrez peut-être interroger jusqu'à deux ans de données, ce qui correspond à la durée de conservation de vos données dans Snowflake. Pour plus de détails sur la conservation étendue des données, contactez votre gestionnaire de la satisfaction client.

### Fuseau horaire du Générateur de requêtes {#query-builder-time-zone}

Le fuseau horaire par défaut pour interroger notre base de données Snowflake est UTC. Par conséquent, il peut y avoir des écarts de données entre votre page **Email Channel Engagement** (qui suit le fuseau horaire de votre entreprise) et les résultats de votre Générateur de requêtes.

Pour convertir le fuseau horaire dans les résultats de votre requête, ajoutez le SQL suivant à votre requête et personnalisez-le pour le fuseau horaire de votre entreprise :

{% raw %}
```sql
SELECT
DATE_TRUNC(
'day',
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME))
) AS send_date_sydney,
COUNT(ID) AS emails_sent
USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE
-- Apply the date range in Sydney time as well
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) >= '2025-03-25 00:00:00'
AND CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) < '2025-03-29 00:00:00'
AND APP_GROUP_ID = 'your app group ID'
GROUP BY
send_date_sydney
ORDER BY
send_date_sydney;
```
{% endraw %}

### Historique des requêtes {#query-history}

La section **Query history** du Générateur de requêtes affiche vos requêtes précédemment exécutées pour vous aider à suivre et réutiliser votre travail. L'historique des requêtes est conservé pendant sept jours, ce qui signifie que les requêtes de plus de sept jours sont automatiquement supprimées.

Si vous devez auditer l'utilisation des requêtes sur des périodes plus longues ou conserver des enregistrements au-delà de sept jours, nous vous recommandons d'exporter ou d'enregistrer les résultats de requêtes importants avant leur expiration.

## Générer du SQL avec l'AI Query Builder {#ai-query-builder}

L'AI Query Builder s'appuie sur [GPT](https://openai.com/gpt-4), propulsé par OpenAI, pour recommander du SQL pour votre requête.

![L'AI Query Builder SQL.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

Pour générer du SQL avec l'AI Query Builder :

1. Après avoir créé un rapport dans le Générateur de requêtes, sélectionnez l'onglet **AI Query Builder**.
2. Saisissez votre prompt ou sélectionnez un exemple de prompt, puis sélectionnez **Generate** pour traduire votre prompt en SQL.
3. Vérifiez le SQL généré pour vous assurer qu'il est correct, puis sélectionnez **Insert into Editor**.

### Conseils {#tips}

- Familiarisez-vous avec les tables et colonnes disponibles dans la [référence des tables SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables). Demander des données qui n'existent pas dans ces tables peut amener ChatGPT à inventer une fausse table.
- Familiarisez-vous avec les [règles d'écriture SQL]({{site.baseurl}}/user_guide/analytics/reports/query_builder#custom-sql) pour cette fonctionnalité. Le non-respect de ces règles entraînera une erreur.
- Vous pouvez envoyer jusqu'à 20 prompts par minute avec l'AI Query Builder.

#{% multi_lang_include brazeai/generative_ai/policy.md %}

## Écrire des requêtes SQL personnalisées {#custom-sql}

Écrivez votre requête SQL en utilisant la [syntaxe Snowflake](https://docs.snowflake.com/en/sql-reference). Consultez la [référence des tables]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) pour une liste complète des tables et colonnes disponibles pour les requêtes.

Pour afficher les détails des tables dans le Générateur de requêtes :

1. Depuis la page **Query Builder**, ouvrez le panneau **Reference** et sélectionnez **Available Data Tables** pour afficher les tables de données disponibles et leurs noms.
3. Sélectionnez <i class="fas fa-chevron-down" alt=""></i> **See Details** pour afficher la description de la table et les informations sur les colonnes, telles que les types de données.
4. Pour insérer le nom de la table dans votre SQL, sélectionnez <i class="fas fa-copy" title="Copier le nom de la table dans l'éditeur SQL"></i> **Copy table name to SQL editor**.

Pour utiliser des requêtes pré-écrites fournies par Braze, sélectionnez **Query Template** lors de la création initiale d'un rapport dans le Générateur de requêtes.

Restreindre votre requête à une période spécifique vous aidera à générer des résultats plus rapidement. Voici un exemple de requête qui obtient le nombre d'achats et le chiffre d'affaires généré au cours de la dernière heure.

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

Cette requête récupère le nombre d'envois d'e-mails au cours du dernier mois :

```sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

Si vous interrogez `CANVAS_ID`, `CANVAS_VARIATION_API_ID` ou `CAMPAIGN_ID`, les colonnes de noms associées seront automatiquement incluses dans le tableau de résultats. Vous n'avez pas besoin de les inclure dans la requête `SELECT` elle-même.

| Nom de l'ID | Colonne de nom associée |
| --- | --- |
| `CANVAS_ID` | Canvas Name |
| `CANVAS_VARIATION_API_ID` | Canvas Variant Name |
| `CAMPAIGN_ID` | Campaign Name |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Écrire des requêtes SQL personnalisées" }

Cette requête récupère les trois ID et leurs colonnes de noms associées avec un maximum de 100 lignes :

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

### Remplir automatiquement le nom de la variante de campagne {#automatically-populate-the-campaign-variant-name}

Si vous souhaitez que le nom de la variante de campagne soit automatiquement rempli, incluez le nom de colonne `MESSAGE_VARIATION_API_ID` dans votre requête, comme dans cet exemple :

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID, MESSAGE_VARIATION_API_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

### Résolution des problèmes {#troubleshooting}

Votre requête peut échouer pour l'une des raisons suivantes :

- Erreurs de syntaxe dans votre requête SQL
- Délai de traitement dépassé (après 6 minutes)
    - Les rapports dont l'exécution prend plus de 6 minutes expireront.
    - Si un rapport expire, essayez de limiter la période sur laquelle vous interrogez les données ou d'interroger un ensemble de données plus spécifique.

## Utiliser des variables {#using-variables}

Utilisez des variables pour employer des types de variables prédéfinis en SQL afin de référencer des valeurs sans avoir à copier manuellement la valeur. Par exemple, au lieu de copier manuellement l'ID d'une campagne dans l'éditeur SQL, vous pouvez utiliser {% raw %}`{{campaign.${My campaign}}}`{% endraw %} pour sélectionner directement une campagne depuis un menu déroulant dans l'onglet **Variables**.

Une fois une variable créée, elle apparaîtra dans l'onglet **Variables** de votre rapport du Générateur de requêtes. Les avantages de l'utilisation de variables SQL incluent :

- Gagner du temps en créant une variable Campaign à sélectionner dans une liste lors de la création de votre rapport, au lieu de coller des identifiants Campaign.
- Permuter les valeurs en ajoutant des variables qui vous permettent de réutiliser le rapport pour des cas d'utilisation légèrement différents à l'avenir (comme un événement personnalisé différent).
- Réduire les erreurs utilisateur lors de la modification de votre SQL en diminuant la quantité de modifications nécessaires pour chaque rapport. Les collègues plus à l'aise avec SQL peuvent créer des rapports que des collègues moins techniques peuvent ensuite utiliser.

### Directives {#guidelines}

Les variables doivent respecter la syntaxe Liquid suivante : {% raw %}`{{ type.${name}}}`{% endraw %}, où `type` doit être l'un des types acceptés et `name` peut être ce que vous souhaitez. Les libellés de ces variables correspondent par défaut au nom de la variable.

Par défaut, toutes les variables sont obligatoires (et votre rapport ne s'exécutera pas tant que les valeurs des variables ne seront pas sélectionnées), à l'exception de la plage de dates, qui prend par défaut les 30 derniers jours lorsque la valeur n'est pas fournie.

### Types de variables {#variable-types}

Les types de variables suivants sont acceptés :

- [Nombre](#number)
- [Plage de dates](#date-range)
- [Envoi de messages](#messaging)
- [Produits](#products)
- [Événements personnalisés](#custom-events)
- [Propriétés d'événements personnalisés](#custom-event-properties)
- [Espace de travail](#workspace)
- [Catalogues](#catalogs)
- [Champs de catalogue](#catalog-fields)
- [Options](#options)
- [Segments](#segments)
- [Chaîne de caractères](#string)
- [Étiquettes](#tags)

#### Nombre {#number}

- **Valeur de remplacement :** La valeur fournie, telle que `5.5`
- **Exemple d'utilisation :** {% raw %}`some_number_column < {{number.${some name}}}`{% endraw %}

#### Plage de dates {#date-range}

Si vous utilisez à la fois `start_date` et `end_date`, ils doivent avoir le même nom afin de pouvoir les utiliser comme plage de dates.

##### Exemples de valeurs {#example-values}

Le type plage de dates peut être relatif, date de début, date de fin ou plage de dates.

Les quatre types sont affichés si `start_date` et `end_date` sont utilisés avec le même nom. Si un seul est utilisé, seuls les types pertinents seront affichés.

| Type de plage de dates | Description | Valeurs requises |
| --- | --- | --- |
| Relatif | Spécifie les X derniers jours | Nécessite `start_date` |
| Date de début | Spécifie une date de début | Nécessite `start_date` |
| Date de fin | Spécifie une date de fin | Nécessite `end_date` |
| Plage de dates | Spécifie à la fois une date de début et une date de fin | Nécessite à la fois `start_date` et `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Exemples de valeurs" }

- **Valeur de remplacement :** Remplace `start_date` et `end_date` par un horodatage Unix en secondes pour une date spécifiée en UTC, tel que `1696517353`.
- **Exemple d'utilisation :** Pour toutes les variables relatives, date de début, date de fin et plage de dates :
    - {% raw %}`time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}` {% endraw %}
        - Vous pouvez utiliser soit `start_date` soit `end_date` si vous ne souhaitez pas de plage de dates.

#### Envoi de messages {#messaging}

Toutes les variables d'envoi de messages doivent partager le même identifiant lorsque vous souhaitez lier leur état dans un même groupe.

##### Canvas

Pour sélectionner un Canvas. Partager le même nom avec une Campaign entraînera un bouton radio dans l'onglet **Variables** permettant de sélectionner soit Canvas soit Campaign.

- **Valeur de remplacement :** ID BSON du Canvas
- **Exemple d'utilisation :** {% raw %}`canvas_id = '{{canvas.${some name}}}'`{% endraw %}

##### Canvas (multiples) {#canvases}

Pour sélectionner plusieurs Canvas. Partager le même nom avec une Campaign entraînera un bouton radio dans l'onglet **Variables** permettant de sélectionner soit Canvas soit Campaign.

- **Valeur de remplacement :** ID BSON des Canvas
- **Exemple d'utilisation :** {% raw %}`canvas_id IN ({{canvases.${some name}}})`{% endraw %}

##### Campaign

Pour sélectionner une Campaign. Partager le même nom avec un Canvas entraînera un bouton radio dans l'onglet **Variables** permettant de sélectionner soit Canvas soit Campaign.

- **Valeur de remplacement :** ID BSON de la Campaign
- **Exemple d'utilisation :** {% raw %}`campaign_id = '{{campaign.${some name}}}'`{% endraw %}

##### Campaigns

Pour sélectionner plusieurs Campaigns. Partager le même nom avec un Canvas entraînera un bouton radio dans l'onglet **Variables** permettant de sélectionner soit Canvas soit Campaign.

- **Valeur de remplacement :** ID BSON des Campaigns
- **Exemple d'utilisation :** {% raw %}`campaign_id IN ({{campaigns.${some name}}})`{% endraw %}

##### Variantes de Campaign {#campaign-variants}

Pour sélectionner les variantes de Campaign appartenant à la Campaign sélectionnée. Doit être utilisé conjointement avec une variable Campaign ou Campaigns.

- **Valeur de remplacement :** ID API des variantes de Campaign, chaînes de caractères délimitées par des virgules telles que `api-id1, api-id2`.
- **Exemple d'utilisation :** {% raw %}`message_variation_api_id IN ({{campaign_variants.${some name}}})`{% endraw %}

##### Variantes de Canvas {#canvas-variants}

Pour sélectionner les variantes de Canvas appartenant à un Canvas choisi. Doit être utilisé avec une variable Canvas ou Canvas (multiples).

- **Valeur de remplacement :** ID API des variantes de Canvas, chaînes de caractères délimitées par des virgules telles que `api-id1, api-id2`.
- **Exemple d'utilisation :** {% raw %}`canvas_variation_api_id IN ({{canvas_variants.${some name}}})`{% endraw %}

##### Étape du Canvas {#canvas-step}

Pour sélectionner une étape du Canvas appartenant à un Canvas choisi. Doit être utilisé avec une variable Canvas.

- **Valeur de remplacement :** ID API de l'étape du Canvas
- **Exemple d'utilisation :** {% raw %}`canvas_step_api_id = '{{canvas_step.${some name}}}'`{% endraw %}

##### Étapes du Canvas {#canvas-steps}

Pour sélectionner les étapes du Canvas appartenant aux Canvas choisis. Doit être utilisé avec une variable Canvas ou Canvas (multiples).

- **Valeur de remplacement :** ID API des étapes du Canvas
- **Exemple d'utilisation :** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}