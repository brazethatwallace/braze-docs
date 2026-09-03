> Découvrez comment utiliser le Générateur de requêtes pour générer des rapports à partir des données de Braze dans Snowflake. Le Générateur de requêtes inclut des [modèles de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates) SQL prédéfinis pour vous aider à démarrer, mais vous pouvez aussi écrire vos propres requêtes SQL personnalisées pour obtenir encore plus d'informations.

## Prérequis {#prerequisites}

Vous aurez besoin des [permissions « Voir les données d'identification »]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) pour utiliser le Générateur de requêtes, car il permet un accès direct à certaines données clients.

## Utiliser le Générateur de requêtes {#using-the-query-builder}

### Étape 1 : Créer une requête SQL {#step-1-create-an-sql-query}

Pour créer une nouvelle requête, accédez à **Analytics** > **Query Builder**, puis sélectionnez **Create SQL Query**.

![Les options « Query Template » et « SQL Editor » dans le menu déroulant « Create SQL Query ».]({% image_buster /assets/img_archive/create_sql_query_button.png %}){: style="max-width:60%;"}

Si vous avez besoin d'inspiration ou d'aide pour élaborer votre requête, choisissez **Query Template** et sélectionnez un [modèle prédéfini]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates). Pour commencer avec une requête vierge, sélectionnez **SQL Editor**.

Votre rapport reçoit automatiquement un nom avec la date et l'heure actuelles. Survolez le nom et sélectionnez <i class="fas fa-pencil" alt="Modifier"></i> pour donner un nom significatif à votre requête SQL.

![Un exemple de nom de rapport « Channel engagement for May 2025 ».]({% image_buster /assets/img_archive/report_name_example.png %}){: style="max-width:80%;"}

### Étape 2 : Construire votre requête {#step-2-build-your-query}

Lors de la construction de votre requête, vous pouvez choisir de vous faire aider par l'IA ou de la construire vous-même.

{% tabs local %}
{% tab Utiliser BrazeAI %}
Le Générateur de requêtes IA exploite [GPT](https://openai.com/gpt-4), alimenté par OpenAI, pour recommander du SQL pour votre requête. Pour générer du SQL avec le Générateur de requêtes IA :

1. Après avoir créé un rapport dans le Générateur de requêtes, sélectionnez l'onglet **AI Query Builder**.
2. Saisissez votre prompt ou sélectionnez un exemple de prompt, puis sélectionnez **Generate** pour traduire votre prompt en SQL.
3. Vérifiez le SQL généré pour vous assurer qu'il est correct, puis sélectionnez **Insert into Editor**.

![Le Générateur de requêtes SQL par IA.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

#### Conseils {#tips}

- Familiarisez-vous avec les [tables de données Snowflake]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) disponibles. Demander des données qui n'existent pas dans ces tables peut amener ChatGPT à inventer une fausse table.
- Familiarisez-vous avec les [règles d'écriture SQL]({{site.baseurl}}/user_guide/data_and_analytics/query_builder#custom-sql) pour cette fonctionnalité. Le non-respect de ces règles entraînera une erreur.
- Vous pouvez envoyer jusqu'à 20 prompts par minute avec le Générateur de requêtes IA.

##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}

{% tab Par moi-même %}
Écrivez votre requête SQL en utilisant la [syntaxe Snowflake](https://docs.snowflake.com/en/sql-reference). Consultez la [référence des tables]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) pour obtenir la liste complète des tables et colonnes disponibles pour les requêtes.

Pour afficher les détails des tables dans le Générateur de requêtes :

1. Depuis la page du **Générateur de requêtes**, ouvrez le panneau **Reference** et sélectionnez **Available Data Tables** pour afficher les tables de données disponibles et leurs noms.
3. Sélectionnez <i class="fas fa-chevron-down" alt=""></i> **See Details** pour afficher la description de la table et les informations sur les colonnes de la table, telles que les types de données.
4. Pour insérer le nom de la table dans votre SQL, sélectionnez <i class="fas fa-copy" title="Copier le nom de la table dans l'éditeur SQL"></i>.

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

Si vous interrogez le `CANVAS_ID`, le `CANVAS_VARIATION_API_ID` ou le `CAMPAIGN_ID`, les colonnes de noms associées seront automatiquement incluses dans le tableau de résultats. Vous n'avez pas besoin de les inclure dans la requête `SELECT` elle-même.

| Nom de l'ID | Colonne de nom associée |
| --- | --- |
| `CANVAS_ID` | Canvas Name |
| `CANVAS_VARIATION_API_ID` | Canvas Variant Name |
| `CAMPAIGN_ID` | Campaign Name |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conseils" }

Cette requête récupère les trois ID et leurs colonnes de noms associées avec un maximum de 100 lignes :

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

#### Résolution des problèmes {#troubleshooting}

Votre requête peut échouer pour l'une des raisons suivantes :

- Erreurs de syntaxe dans votre requête SQL
- Délai de traitement dépassé (après 6 minutes)
    - Les rapports dont l'exécution prend plus de 6 minutes expireront.
    - Si un rapport expire, essayez de limiter la plage temporelle dans laquelle vous interrogez les données ou interrogez un ensemble de données plus spécifique.
{% endtab %}
{% endtabs %}

### Étape 3 : Générer votre rapport {#step-3-generate-your-report}

Lorsque vous avez terminé de construire votre requête, sélectionnez **Run Query**. S'il n'y a pas d'erreurs ou de [délais d'expiration des rapports](#report-timeouts), un fichier CSV sera généré à partir de la requête.

Pour télécharger le rapport CSV, sélectionnez **Export**.

![Le Générateur de requêtes affichant les résultats pour la requête modèle « Channel engagement and revenue for the last 30 days ».]({% image_buster /assets/img_archive/query_builder.png %})

{% alert important %}
Chaque rapport ne peut générer des résultats qu'une seule fois par jour. Si vous exécutez le même rapport plusieurs fois au cours d'une même journée calendaire, vous verrez les mêmes résultats dans chaque rapport.
{% endalert %}

## Délais d'expiration des rapports {#report-timeouts}

Les rapports dont l'exécution dépasse six minutes expireront. S'il s'agit de la première requête que vous exécutez depuis un certain temps, le traitement peut prendre plus de temps et la probabilité d'expiration est donc plus élevée. Si cela se produit, essayez d'exécuter le rapport à nouveau.

Si votre rapport continue d'expirer après plusieurs tentatives, [contactez le support]({{site.baseurl}}/help/support#braze-support).

## Requêtes sur les raisons d'abandon {#querying-abort-reasons}

Vous pouvez interroger la colonne `ABORT_TYPE` de n'importe quelle table `USERS_MESSAGES_*_ABORT_SHARED` pour analyser les raisons pour lesquelles les messages n'ont pas été envoyés. Le champ `ABORT_TYPE` contient une valeur de chaîne de caractères décrivant la raison spécifique de l'abandon, et le champ complémentaire `ABORT_LOG` contient des détails supplémentaires (tels que la règle de limite de fréquence qui a été déclenchée).

Par exemple, pour compter les abandons d'e-mails par type au cours des 30 derniers jours :

```sql
SELECT ABORT_TYPE, COUNT(*) as abort_count
FROM USERS_MESSAGES_EMAIL_ABORT_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('day', -30, CURRENT_DATE())
GROUP BY ABORT_TYPE
ORDER BY abort_count DESC
```

Pour la liste complète des valeurs `ABORT_TYPE` et leurs descriptions, consultez [Types d'abandon]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables#abort-types).

## Données et résultats {#data-and-results}

Toutes les requêtes renvoient des données des 60 derniers jours. Lorsque vous exportez vos résultats, le fichier ne contient que 1 000 lignes au maximum. Pour les rapports nécessitant de plus grands volumes de données, vous pouvez utiliser des outils tels que [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) ou l'[endpoint d'exportation de l'API]({{site.baseurl}}/api/endpoints/export).

## Crédits Snowflake {#snowflake-credits}

Chaque entreprise dispose de 5 crédits Snowflake par mois, partagés entre tous les espaces de travail. Une petite fraction d'un crédit Snowflake est utilisée chaque fois que vous exécutez une requête ou prévisualisez un tableau.

{% alert note %}
Les crédits Snowflake ne sont pas partagés entre les fonctionnalités. Par exemple, les crédits des extensions de segments SQL et du Générateur de requêtes sont indépendants les uns des autres.
{% endalert %}

L'utilisation des crédits est corrélée au temps d'exécution de votre requête SQL. Plus le temps d'exécution est long, plus la part d'un crédit Snowflake utilisée par la requête est élevée. Le temps d'exécution peut varier en fonction de la complexité et de la taille de vos requêtes au fil du temps. Plus vos requêtes sont complexes et fréquentes, plus vos ressources allouées augmentent et plus votre temps d'exécution diminue.

Les crédits ne sont pas utilisés lors de la rédaction, de la modification ou de l'enregistrement de rapports dans l'éditeur SQL de Braze. Vos crédits sont réinitialisés à 5 le premier jour de chaque mois à 00 h 00 UTC. Vous pouvez suivre votre utilisation mensuelle de crédits en haut de la page du Générateur de requêtes.

![Le Générateur de requêtes affichant le nombre de crédits utilisés au cours du mois en cours.]({% image_buster /assets/img_archive/query_builder_credits.png %}){: style="max-width:60%;"}

Lorsque vous atteignez le plafond de crédits, vous ne pouvez plus exécuter de requêtes, mais vous pouvez toujours créer, modifier et enregistrer des rapports SQL. Si vous souhaitez acheter des crédits supplémentaires pour le Générateur de requêtes, veuillez contacter votre gestionnaire de compte.