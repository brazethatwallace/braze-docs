# Extensions de segments SQL {#sql-segment-extensions}

> Vous pouvez générer une extension de segment à l'aide de requêtes SQL Snowflake sur des données [Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). Le SQL vous aide à exploiter de nouveaux cas d'usage de segments, car il offre la flexibilité nécessaire pour décrire les relations entre les données d'une manière qui n'est pas réalisable avec les autres fonctionnalités de segmentation.
>
> Comme les extensions de segments standard, vous pouvez interroger les événements des deux dernières années (730 jours) dans votre extension de segment SQL. Contrairement aux extensions de segments standard, les extensions de segments SQL [consomment des crédits](#credits).

## Conditions préalables {#prerequisites}

Étant donné qu'il est possible d'accéder à des données d'identification via cette fonctionnalité, vous devez disposer des autorisations PII pour exécuter des requêtes de segments SQL.

## Création d'une extension de segment {#creating-a-segment-extension}

### Étape 1 : Choisir un éditeur {#step-1-choose-an-editor}

Vous avez le choix entre deux types d'éditeurs SQL lors de la création de votre extension de segment SQL : l'éditeur SQL et l'éditeur SQL incrémentiel.

- **Actualisation complète :** À chaque actualisation de votre segment, Braze interroge toutes les données disponibles pour mettre à jour votre segment, ce qui consomme plus de crédits que les actualisations incrémentielles. Les extensions à actualisation complète peuvent régénérer automatiquement l'appartenance chaque jour, mais ne peuvent pas être actualisées de manière incrémentielle.
- **Actualisation incrémentielle :** L'actualisation incrémentielle est un moyen plus économique de configurer votre requête, bien que la configuration nécessite quelques [étapes](#step-2-write-your-sql) supplémentaires. Si vous pouvez effectuer ces étapes supplémentaires lors de la construction de votre segment, il est recommandé de choisir cette option, car votre requête s'exécutera en utilisant moins de crédits.
- **Générateur SQL par IA :** Le générateur SQL par IA vous permet de rédiger une invite en langage courant et la transforme en requête SQL pour votre segment. C'est un moyen rapide de démarrer sans avoir à écrire le SQL vous-même.

{% alert tip %}
Vous pouvez effectuer une actualisation complète manuelle sur tous les segments SQL créés dans l'un ou l'autre des éditeurs SQL.
{% endalert %}

{% tabs local %}
{% tab Full refresh %}

Pour créer une extension de segment SQL à actualisation complète :

1. Accédez à **Audience** > **Segment Extensions**.
2. Sélectionnez **Create New Extension**, puis sélectionnez **Full refresh**.<br><br>
   ![Fenêtre modale de création d'une nouvelle extension avec les options d'actualisation complète et d'actualisation incrémentielle.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Ajoutez un nom pour votre extension de segment et saisissez votre SQL. Reportez-vous à l'[étape 2](#step-2-write-your-sql) pour les exigences et les ressources.<br><br>
   ![Éditeur SQL présentant un exemple d'extension de segment SQL.]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. Enregistrez votre extension de segment.

{% endtab %}
{% tab Incremental refresh %}

Pour créer une extension de segment SQL à actualisation incrémentielle :

1. Accédez à **Audience** > **Segment Extensions**.
2. Sélectionnez **Create New Extension**, puis sélectionnez **Incremental refresh**.<br><br>
   ![Fenêtre modale de création d'une nouvelle extension avec les options d'actualisation complète et d'actualisation incrémentielle.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Ajoutez un nom pour votre extension de segment et saisissez votre SQL. Reportez-vous à la section [Écriture de code SQL](#writing-sql) pour les exigences et les ressources.<br><br>
   ![Éditeur SQL présentant un exemple d'extension de segment SQL incrémentielle.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4. Si vous le souhaitez, sélectionnez **Regenerate Extension Daily**.<br><br>
   ![Case à cocher pour régénérer l'extension quotidiennement.]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   Lorsque cette option est sélectionnée, Braze met automatiquement à jour l'appartenance au segment chaque jour. Concrètement, chaque jour à minuit dans le fuseau horaire de votre entreprise (avec un retard potentiel d'une heure), Braze vérifie s'il y a de nouveaux utilisateurs dans votre segment et les ajoute automatiquement. Si une extension de segment n'a pas été utilisée depuis 7 jours, Braze interrompt automatiquement la régénération quotidienne. Une extension de segment inutilisée est une extension qui ne fait pas partie d'une Campaign ou d'un Canvas (la Campaign ou le Canvas n'a pas besoin d'être actif pour que l'extension soit considérée comme « utilisée »).<br><br>
5. Enregistrez votre extension de segment.

{% endtab %}

{% tab AI SQL Generator %}

{% alert note %}
Le générateur SQL par IA est actuellement disponible en tant que fonctionnalité bêta. Contactez votre gestionnaire du succès des clients si vous souhaitez participer à cet essai bêta.
{% endalert %}

Le générateur SQL par IA s'appuie sur [GPT](https://openai.com/gpt-4) d'OpenAI pour recommander du code SQL pour votre segment SQL.

![Générateur SQL par IA avec l'invite « Utilisateurs ayant reçu une notification le mois dernier »]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

Pour utiliser le générateur SQL par IA, procédez comme suit :

1. Sélectionnez **Launch AI SQL Generator** après avoir créé un [segment SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) en utilisant l'actualisation complète ou incrémentielle.
2. Saisissez votre invite et sélectionnez **Generate** pour la convertir en SQL.
3. Vérifiez le code SQL généré pour vous assurer qu'il est correct, puis enregistrez votre segment.

#### Exemples d'invites {#example-prompts}

- Utilisateurs ayant reçu un e-mail au cours du dernier mois
- Utilisateurs ayant effectué moins de cinq achats au cours de l'année écoulée

#### Conseils {#tips}

- Familiarisez-vous avec les [tables de données Snowflake]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables) disponibles. Si vous demandez des données qui n'existent pas dans ces tables, ChatGPT risque d'inventer une fausse table.
- Familiarisez-vous avec les [règles d'écriture SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql) pour cette fonctionnalité. Le non-respect de ces règles entraînera une erreur. Par exemple, votre code SQL doit sélectionner la colonne `user_id`. Commencer votre invite par « Utilisateurs qui » peut être utile.
- Vous pouvez envoyer jusqu'à 20 invites par minute avec le générateur SQL par IA.

##{% multi_lang_include brazeai/generative_ai/policy.md %}

{% endtab %}
{% endtabs %}

{% alert note %}
Les requêtes SQL dont l'exécution dépasse 20 minutes expireront.
{% endalert %}

Une fois le traitement de l'extension terminé, vous pouvez [créer un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment) à l'aide de votre extension de segment et cibler ce nouveau segment avec vos Campaigns et Canvas.

### Étape 2 : Rédiger votre requête SQL {#step-2-write-your-sql}

Votre requête SQL doit être écrite en utilisant la [syntaxe Snowflake](https://docs.snowflake.com/en/sql-reference.html). Consultez la [référence des tables]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables) pour obtenir la liste complète des tables et colonnes disponibles.

{% alert important %}
Notez que les tables disponibles ne contiennent que des données d'événements. Si vous souhaitez interroger des attributs utilisateur, vous devez combiner votre segment SQL avec des filtres d'attributs personnalisés du [segmenteur classique]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment).
{% endalert %}

{% tabs %}
{% tab SQL Editor %}

Votre SQL doit également respecter les règles suivantes :

- Rédigez une seule instruction SQL. N'incluez aucun point-virgule.
- Votre SQL ne doit sélectionner qu'une seule colonne : la colonne `user_id`. Cela signifie que votre SQL doit contenir :

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- Il n'est pas possible d'interroger les utilisateurs n'ayant aucun événement, ce qui signifie que toute requête portant sur des utilisateurs ayant effectué un événement moins de X fois devra suivre cette solution de contournement :
   1. Écrivez une requête pour sélectionner les utilisateurs ayant l'événement PLUS de X fois.
   2. Lorsque vous faites référence à votre extension de segment dans votre segment, sélectionnez `doesn't include` pour inverser le résultat.

#### Règles supplémentaires {#additional-rules}

De plus, votre requête SQL standard doit respecter les règles suivantes :

- Vous ne pouvez pas utiliser d'instructions `DECLARE`.
{% endtab %}
{% tab Incremental SQL Editor %}

Toutes les requêtes d'actualisation incrémentielle se composent de deux parties : une requête et les détails du schéma.

1. Dans l'éditeur, écrivez une requête qui sélectionne les `user_id` dans la table de votre choix.
2. Ajoutez les détails du schéma en sélectionnant un **opérateur**, un **nombre de fois** et une **période** dans les champs situés au-dessus de l'éditeur. La requête vérifie si la somme de la colonne agrégée remplit une certaine condition spécifiée par les marques substitutives {% raw %}`{{operator}}` et `{{number of times}}`{% endraw %}. Le fonctionnement est similaire à celui du processus de création des extensions de segments classiques.<br><br>
   - **Opérateur :** Indiquez si l'événement s'est produit plus de fois, moins de fois ou autant de fois qu'un nombre d'occurrences donné.<br>
   ![Champ opérateur avec « Plus de » sélectionné.]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **Nombre de fois :** Combien de fois vous souhaitez évaluer l'événement par rapport à l'opérateur.<br>
   ![Nombre de fois avec « 5 » saisi.]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **Période :** Nombre de jours, de 1 à 730, pendant lesquels vous souhaitez vérifier les occurrences de l'événement. Cette période se réfère aux jours passés par rapport au jour actuel. L'exemple suivant montre une requête pour les utilisateurs ayant effectué l'événement plus de 5 fois au cours des 365 derniers jours.<br>
   ![Champ « Période » avec la valeur « 365 » saisie.]({% image_buster /assets/img_archive/sql_segments_period.png %})

Dans l'exemple suivant, le segment résultant contiendra les utilisateurs ayant effectué l'événement `favorited` plus de 3 fois au cours des 30 derniers jours, après une date spécifiée.

![Éditeur SQL présentant un exemple d'extension de segment SQL incrémentielle.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![Aperçu SQL d'une extension de segment SQL incrémentielle.]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

{% alert tip %}
Les segments à actualisation incrémentielle prennent en compte les événements tardifs, c'est-à-dire les événements survenus il y a plus de 2 jours (par exemple, les événements SDK qui n'ont pas été envoyés au moment où ils ont été capturés).
{% endalert %}

#### Règles supplémentaires

De plus, votre requête d'actualisation incrémentielle doit respecter les règles suivantes :

- Rédigez une seule instruction SQL. N'incluez aucun point-virgule.
- Votre segment SQL incrémentiel ne peut faire référence qu'à un seul événement. Vos listes déroulantes pour la date et le nombre font référence à l'événement choisi.
- Votre code SQL doit comporter les colonnes suivantes : `user_id`, `$start_date` et une fonction d'agrégation (telle que `COUNT`). Tout SQL enregistré sans ces trois champs entraînera une erreur.
- Vous ne pouvez pas utiliser d'instructions `DECLARE`.
{% endtab %}
{% endtabs %}

{% alert note %}
Si vous créez un segment SQL qui utilise la table `CATALOGS_ITEMS_SHARED`, vous devez spécifier un ID de catalogue. Par exemple :

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### Étape 3 : Prévisualiser la requête {#step-3-preview-the-query}

Avant d'enregistrer, vous pouvez exécuter un aperçu de votre requête. Les aperçus de requêtes sont automatiquement limités à 100 lignes et expireront au bout de 60 secondes. L'exigence de la colonne `user_id` ne s'applique pas lors de l'exécution d'un aperçu.

Pour les extensions de segments SQL incrémentielles, l'aperçu n'inclut pas les critères supplémentaires de votre opérateur, nombre de fois et période.

### Étape 4 : Déterminer si vous devez inverser le SQL {#step-4-determine-if-you-need-to-invert-sql}

Ensuite, déterminez si vous devez inverser le SQL. Bien qu'il ne soit pas possible d'interroger directement les utilisateurs n'ayant aucun événement, vous pouvez utiliser **Invert SQL** pour cibler ces utilisateurs.

{% alert note %}
Par défaut, **Invert SQL** n'est pas activé. Toutefois, si vous utilisez le générateur SQL par IA pour créer une instruction SQL qui doit être niée, ChatGPT pourrait renvoyer un résultat qui active automatiquement cette fonctionnalité.
{% endalert %}

Par exemple, pour cibler les utilisateurs ayant effectué moins de trois achats, rédigez d'abord une requête pour sélectionner les utilisateurs ayant effectué trois achats ou plus. Ensuite, sélectionnez **Invert SQL** pour cibler les utilisateurs ayant effectué moins de trois achats (y compris ceux n'ayant effectué aucun achat).

{% alert important %}
À moins que vous ne souhaitiez spécifiquement cibler les utilisateurs n'ayant aucun événement, vous n'aurez pas besoin d'inverser le SQL. Si **Invert SQL** est sélectionné, vérifiez que cette fonctionnalité est nécessaire et que le segment correspond à l'audience souhaitée. Par exemple, si une requête cible les utilisateurs ayant au moins un événement, elle ne ciblera que les utilisateurs n'ayant aucun événement une fois inversée.
{% endalert %}

![Extension de segment intitulée « A cliqué sur 1 à 4 e-mails au cours des 30 derniers jours » avec l'option d'inverser le SQL sélectionnée.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:90%;"}

## Actualiser l'appartenance au segment {#refreshing-segment-membership}

Pour actualiser l'appartenance au segment d'une extension de segment créée à l'aide de SQL, ouvrez l'extension de segment et sélectionnez **Refresh**.

{% alert tip %}
Si vous avez créé un segment dans lequel vous vous attendez à ce que les utilisateurs entrent et sortent régulièrement, actualisez manuellement l'extension de segment qu'il utilise avant de cibler ce segment dans une Campaign ou un Canvas.
{% endalert %}

## Gestion de vos extensions de segments {#managing-your-segment-extensions}

Sur la page **Segment Extensions**, les segments générés à l'aide de SQL sont signalés par <i class="fas fa-code" alt="Extension de segment SQL"></i> à côté de leur nom.

Sélectionnez une extension de segment SQL pour voir où l'extension est utilisée, archiver l'extension ou [actualiser manuellement l'appartenance au segment](#refreshing-segment-membership).

![Section « Utilisation de la communication » de l'éditeur SQL indiquant où le segment SQL est utilisé.]({% image_buster /assets/img_archive/sql_segments_usage.png %}){: style="max-width:70%;"}

### Définir les paramètres d'actualisation {#designating-refresh-settings}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

## Crédits Snowflake {#credits}

Chaque espace de travail Braze dispose de 5 crédits Snowflake par mois. Si vous avez besoin de crédits supplémentaires, contactez votre gestionnaire de compte. Les crédits sont consommés chaque fois que vous actualisez, ou enregistrez et actualisez, l'appartenance d'un segment SQL. Les crédits ne sont pas utilisés lorsque vous exécutez des aperçus dans un segment SQL ou lorsque vous enregistrez ou actualisez une extension de segment classique.

{% alert note %}
Les crédits Snowflake ne sont pas partagés entre les fonctionnalités. Par exemple, les crédits des extensions de segments SQL et du générateur de requêtes sont indépendants les uns des autres.
{% endalert %}

La consommation de crédits est corrélée à la durée d'exécution de votre requête SQL. Plus la durée d'exécution est longue, plus la requête coûtera de crédits. La durée d'exécution peut varier en fonction de la complexité et de la taille de vos requêtes au fil du temps. Plus vous exécutez des requêtes complexes et fréquentes, plus votre allocation de ressources est importante et plus votre temps d'exécution diminue.

Pour économiser des crédits, prévisualisez votre requête pour vous assurer qu'elle est correcte avant d'enregistrer l'extension de segment SQL.

Vos crédits sont réinitialisés à 5 le premier de chaque mois à 00h00 UTC. Vous pouvez suivre votre consommation de crédits tout au long du mois dans le panneau d'utilisation des crédits. Depuis la page **Segment Extensions**, cliquez sur <i class="fa-solid fa-chart-column" aria-label="Voir l'utilisation des crédits SQL"></i> **View SQL Credit Usage**.

![Panneau d'utilisation des crédits SQL sur la page Extensions de segments SQL]({% image_buster /assets/img_archive/sql_segments_credits.png %}){: style="max-width:60%"}

Voici ce qui se passe lorsque vos crédits atteignent zéro :

- Toutes les extensions de segments SQL configurées pour s'actualiser automatiquement cessent de s'actualiser, ce qui impacte l'appartenance à ces segments ainsi que toutes les Campaigns ou Canvas qui ciblent ces segments.
- Vous ne pouvez enregistrer les nouvelles extensions de segments SQL qu'en tant que brouillons pour le reste du mois.

Tous les utilisateurs de l'entreprise ayant créé un segment SQL ainsi que les administrateurs de votre entreprise recevront un e-mail de notification lorsque vous aurez utilisé 50 %, 80 % et 100 % de vos crédits. Après la réinitialisation de vos crédits au début du mois suivant, vous pourrez créer de nouveaux segments SQL et les actualisations automatiques reprendront.

Si vous souhaitez acheter des crédits de segments SQL supplémentaires ou des extensions de segments supplémentaires, contactez votre gestionnaire de compte.