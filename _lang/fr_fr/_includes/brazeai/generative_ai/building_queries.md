> Apprenez à utiliser le Générateur de requêtes pour générer des rapports à partir des données de Braze dans Snowflake. Le Générateur de requêtes inclut des [modèles de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) SQL prédéfinis pour vous aider à démarrer, mais vous pouvez aussi écrire vos propres requêtes SQL personnalisées pour obtenir encore plus d'informations.

## Conditions préalables {#prerequisites}

Vous aurez besoin des [autorisations « Voir les informations confidentielles »]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) pour utiliser le Générateur de requêtes, car il permet d'accéder directement à certaines données clients.

## Utilisation du Générateur de requêtes {#using-the-query-builder}

### Étape 1 : Créer une requête SQL {#step-1-create-an-sql-query}

Pour créer une nouvelle requête, accédez à **Analytics** > **Query Builder**, puis sélectionnez **Create SQL Query**.

![Les options « Query Template » et « SQL Editor » dans la liste déroulante « Create SQL Query ».]({% image_buster /assets/img_archive/create_sql_query_button.png %}){: style="max-width:60%;"}

Si vous avez besoin d'inspiration ou d'aide pour rédiger votre requête, choisissez **Query Template** et sélectionnez un [modèle préétabli]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/). Pour commencer avec une requête vierge, sélectionnez **SQL Editor**.

Votre rapport reçoit automatiquement un nom basé sur la date et l'heure actuelles. Survolez le nom et sélectionnez <i class="fas fa-pencil" alt="Modifier"></i> pour donner un nom pertinent à votre requête SQL.

![Un exemple de nom de rapport : « Channel engagement for May 2025 ».]({% image_buster /assets/img_archive/report_name_example.png %}){: style="max-width:80%;"}

### Étape 2 : Créer votre requête {#step-2-build-your-query}

Lors de la création de votre requête, vous pouvez choisir de vous faire aider par l'intelligence artificielle ou de la construire vous-même.

{% tabs local %}
{% tab Using BrazeAI %}
Le générateur de requêtes par IA s'appuie sur [GPT](https://openai.com/gpt-4) d'OpenAI pour recommander du SQL adapté à votre requête. Pour générer du SQL avec le générateur de requêtes par IA :

1. Après avoir créé un rapport dans le Générateur de requêtes, sélectionnez l'onglet **AI Query Builder**.
2. Saisissez votre prompt ou sélectionnez un exemple de prompt, puis sélectionnez **Generate** pour le traduire en SQL.
3. Vérifiez le SQL généré pour vous assurer qu'il est correct, puis sélectionnez **Insert into Editor**.

![Le générateur de requêtes SQL par intelligence artificielle.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

#### Conseils {#tips}

- Familiarisez-vous avec les [tables de données Snowflake]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) disponibles. Si vous demandez des données qui n'existent pas dans ces tables, ChatGPT risque d'inventer une fausse table.
- Familiarisez-vous avec les [règles d'écriture SQL]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) de cette fonctionnalité. Le non-respect de ces règles entraînera une erreur.
- Vous pouvez envoyer jusqu'à 20 prompts par minute avec le générateur de requêtes par IA.

##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}

{% tab On My Own %}
Rédigez votre requête SQL en utilisant la [syntaxe Snowflake](https://docs.snowflake.com/en/sql-reference). Consultez la [référence des tables]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) pour obtenir la liste complète des tables et colonnes disponibles.

Pour afficher les détails d'une table dans le Générateur de requêtes :

1. Depuis la page **Query Builder**, ouvrez le panneau **Reference** et sélectionnez **Available Data Tables** pour afficher les tables de données disponibles et leurs noms.
3. Sélectionnez <i class="fas fa-chevron-down" alt=""></i> **See Details** pour afficher la description de la table et des informations sur ses colonnes, comme les types de données.
4. Pour insérer le nom de la table dans votre SQL, sélectionnez <i class="fas fa-copy" title="Copier le nom de la table dans l'éditeur SQL"></i>.

Restreindre votre requête à une période spécifique vous aidera à obtenir des résultats plus rapidement. Voici un exemple de requête qui récupère le nombre d'achats et le chiffre d'affaires généré au cours de la dernière heure.

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

Si vous effectuez une requête sur `CANVAS_ID`, `CANVAS_VARIATION_API_ID` ou `CAMPAIGN_ID`, les colonnes de noms associées seront automatiquement incluses dans le tableau des résultats. Il n'est pas nécessaire de les inclure dans la requête `SELECT` elle-même.

| Nom de l'ID | Colonne de nom associée |
| --- | --- |
| `CANVAS_ID` | Canvas Name |
| `CANVAS_VARIATION_API_ID` | Canvas Variant Name |
| `CAMPAIGN_ID` | Campaign Name |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conseils" }

Cette requête récupère les trois ID et leurs colonnes de noms associées, avec un maximum de 100 lignes :

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

#### Résolution des problèmes {#troubleshooting}

Votre requête peut échouer pour l'une des raisons suivantes :

- Erreurs de syntaxe dans votre requête SQL
- Dépassement du délai de traitement (après 6 minutes)
    - Les rapports dont l'exécution dépasse 6 minutes seront interrompus.
    - Si un rapport expire, essayez de restreindre la plage temporelle de votre requête ou d'interroger un ensemble de données plus spécifique.
{% endtab %}
{% endtabs %}

### Étape 3 : Générer votre rapport {#step-3-generate-your-report}

Une fois votre requête finalisée, sélectionnez **Run Query**. En l'absence d'erreurs ou de [dépassements de délai](#report-timeouts), un fichier CSV sera généré à partir de la requête.

Pour télécharger le rapport CSV, sélectionnez **Export**.

![Générateur de requêtes affichant les résultats de la requête modélisée « Channel engagement and revenue for the last 30 days ».]({% image_buster /assets/img_archive/query_builder.png %})

{% alert important %}
Chaque rapport ne peut générer des résultats qu'une seule fois par jour. Si vous exécutez le même rapport plusieurs fois au cours d'une même journée calendaire, vous obtiendrez les mêmes résultats à chaque fois.
{% endalert %}

## Dépassements de délai des rapports {#report-timeouts}

Les rapports dont l'exécution dépasse six minutes sont interrompus. S'il s'agit de la première requête que vous exécutez depuis un certain temps, le traitement peut prendre plus de temps et le risque de dépassement de délai est donc plus élevé. Si cela se produit, essayez d'exécuter le rapport à nouveau.

Si votre rapport continue d'expirer après plusieurs tentatives, [contactez l'assistance]({{site.baseurl}}/help/support/#braze-support).

## Interroger les raisons d'abandon {#querying-abort-reasons}

Vous pouvez interroger la colonne `ABORT_TYPE` de n'importe quelle table `USERS_MESSAGES_*_ABORT_SHARED` pour analyser les raisons pour lesquelles des messages n'ont pas été envoyés. Le champ `ABORT_TYPE` contient une valeur de chaîne de caractères décrivant la raison spécifique de l'abandon, et le champ complémentaire `ABORT_LOG` fournit des détails supplémentaires (comme la règle de limite de fréquence qui a été déclenchée).

Par exemple, pour compter les abandons d'e-mails par type au cours des 30 derniers jours :

```sql
SELECT ABORT_TYPE, COUNT(*) as abort_count
FROM USERS_MESSAGES_EMAIL_ABORT_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('day', -30, CURRENT_DATE())
GROUP BY ABORT_TYPE
ORDER BY abort_count DESC
```

Pour la liste complète des valeurs `ABORT_TYPE` et leurs descriptions, consultez [Types d'abandon]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/#abort-types).

## Données et résultats {#data-and-results}

Toutes les requêtes portent sur les données des 60 derniers jours. Lorsque vous exportez vos résultats, le fichier ne contient pas plus de 1 000 lignes. Pour les rapports nécessitant de plus grandes quantités de données, vous pouvez utiliser des outils tels que [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) ou l'[endpoint API d'exportation]({{site.baseurl}}/api/endpoints/export/).

## Crédits Snowflake {#snowflake-credits}

Chaque société dispose de 5 crédits Snowflake par mois, partagés entre tous les espaces de travail. Une petite partie d'un crédit Snowflake est consommée chaque fois que vous exécutez une requête ou prévisualisez une table.

{% alert note %}
Les crédits Snowflake ne sont pas partagés entre les fonctionnalités. Par exemple, les crédits des extensions de segments SQL et du Générateur de requêtes sont indépendants les uns des autres.
{% endalert %}

La consommation de crédits est proportionnelle à la durée d'exécution de votre requête SQL. Plus la durée d'exécution est longue, plus la part de crédit Snowflake consommée sera élevée. La durée d'exécution peut varier en fonction de la complexité et de la taille de vos requêtes au fil du temps. Plus vous exécutez des requêtes complexes et fréquentes, plus votre allocation de ressources augmente et plus votre temps d'exécution diminue.

Les crédits ne sont pas consommés lorsque vous rédigez, modifiez ou enregistrez des rapports dans l'éditeur SQL de Braze. Vos crédits sont réinitialisés à 5 le premier de chaque mois à 00 h 00 UTC. Vous pouvez suivre votre consommation mensuelle de crédits en haut de la page du Générateur de requêtes.

![Générateur de requêtes indiquant le nombre de crédits utilisés pendant le mois en cours.]({% image_buster /assets/img_archive/query_builder_credits.png %}){: style="max-width:60%;"}

Lorsque vous atteignez le plafond de crédits, vous ne pouvez plus exécuter de requêtes, mais vous pouvez toujours créer, modifier et enregistrer des rapports SQL. Si vous souhaitez acheter des crédits supplémentaires pour le Générateur de requêtes, contactez votre gestionnaire de compte.