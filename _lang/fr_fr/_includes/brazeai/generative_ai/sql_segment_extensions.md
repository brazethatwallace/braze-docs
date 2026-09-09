# Extensions de segments SQL {#sql-segment-extensions}

> Vous pouvez générer une extension de segment à l'aide de requêtes SQL Snowflake sur des données [Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). Le SQL vous aide à exploiter de nouveaux cas d'usage de segments, car il offre la flexibilité nécessaire pour décrire les relations entre les données d'une manière qui n'est pas réalisable avec les autres fonctionnalités de segmentation.
>
> Comme les extensions de segments standard, vous pouvez interroger les événements des deux dernières années (730 jours) dans votre extension de segment SQL. Contrairement aux extensions de segments standard, les extensions de segments SQL [consomment des crédits](#credits).

## Prérequis {#prerequisites}

Étant donné qu'il est possible d'accéder à des données d'identification via cette fonctionnalité, vous devez disposer des autorisations PII pour exécuter des requêtes SQL de segments.

## Création d'une extension de segment {#creating-a-segment-extension}

### Étape 1 : Choisir un éditeur {#step-1-choose-an-editor}

Deux types d'éditeurs SQL sont disponibles lors de la création de votre extension de segment SQL : l'éditeur SQL et l'éditeur SQL incrémentiel.

- **Actualisation complète :** À chaque actualisation de votre segment, Braze interroge toutes les données disponibles pour mettre à jour votre segment, ce qui consomme davantage de crédits qu'une actualisation incrémentielle. Les extensions à actualisation complète peuvent régénérer automatiquement les membres quotidiennement, mais ne peuvent pas être actualisées de manière incrémentielle.
- **Actualisation incrémentielle :** L'actualisation incrémentielle est un moyen plus rentable de configurer votre requête, bien que la mise en place implique quelques [étapes](#step-2-write-your-sql) supplémentaires. Si vous êtes en mesure de réaliser ces étapes supplémentaires lors de la construction de votre segment, cette option vaut la peine d'être choisie car votre requête consommera moins de crédits.
- **Générateur SQL par IA :** Le générateur SQL par IA vous permet de rédiger une demande en langage naturel et de la convertir en requête SQL pour votre segment. C'est un moyen rapide de démarrer sans avoir à écrire le SQL vous-même.

{% alert tip %}
Vous pouvez effectuer une actualisation complète manuelle sur tous les segments SQL créés dans l'un ou l'autre des éditeurs SQL.
{% endalert %}

{% tabs local %}
{% tab Actualisation complète %}

Pour créer une extension de segment SQL à actualisation complète :

1. Accédez à **Audience** > **Extensions de segments**.
2. Sélectionnez **Créer une nouvelle extension**, puis sélectionnez **Actualisation complète**.<br><br>
   ![Fenêtre modale de création d'une nouvelle extension avec les options Actualisation complète et Actualisation incrémentielle.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Ajoutez un nom pour votre extension de segment et saisissez votre SQL. Reportez-vous à l'[étape 2](#step-2-write-your-sql) pour les exigences et les ressources.<br><br>
   ![Éditeur SQL montrant un exemple d'extension de segment SQL.]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. Enregistrez votre extension de segment.

{% endtab %}
{% tab Actualisation incrémentielle %}

Pour créer une extension de segment SQL à actualisation incrémentielle :

1. Accédez à **Audience** > **Extensions de segments**.
2. Sélectionnez **Créer une nouvelle extension** et sélectionnez **Actualisation incrémentielle**.<br><br>
   ![Fenêtre modale de création d'une nouvelle extension avec les options Actualisation complète et Actualisation incrémentielle.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Ajoutez un nom pour votre extension de segment et saisissez votre SQL. Reportez-vous à la section [Écrire votre SQL](#writing-sql) pour les exigences et les ressources.<br><br>
   ![Éditeur SQL montrant un exemple d'extension de segment SQL incrémentielle.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4. Si vous le souhaitez, sélectionnez **Régénérer l'extension quotidiennement**.<br><br>
   ![Case à cocher pour régénérer l'extension quotidiennement.]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   Lorsque cette option est sélectionnée, Braze met automatiquement à jour les membres du segment chaque jour. Cela signifie que chaque jour, à minuit dans le fuseau horaire de votre entreprise (avec un délai potentiel d'une heure), Braze vérifie les nouveaux utilisateurs dans votre segment et les y ajoute automatiquement. Si une extension de segment n'a pas été utilisée pendant 7 jours, Braze suspend automatiquement la régénération quotidienne. Une extension de segment inutilisée est une extension qui ne fait partie d'aucune campagne ni d'aucun Canvas (la campagne ou le Canvas n'a pas besoin d'être actif pour que l'extension soit considérée comme « utilisée »).<br><br>
5. Enregistrez votre extension de segment.

{% endtab %}

{% tab Générateur SQL par IA %}

{% alert note %}
Le générateur SQL par IA est actuellement disponible en tant que fonctionnalité bêta. Contactez votre gestionnaire de la satisfaction client si vous souhaitez participer à cet essai bêta.
{% endalert %}

Le générateur SQL par IA tire parti de [GPT](https://openai.com/gpt-4), développé par OpenAI, pour recommander du SQL pour votre segment SQL.

![Générateur SQL par IA avec la demande « Utilisateurs ayant reçu une notification le mois dernier »]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

Pour utiliser le générateur SQL par IA, procédez comme suit :

1. Sélectionnez **Lancer le générateur SQL par IA** après avoir créé un [segment SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) en utilisant l'actualisation complète ou incrémentielle.
2. Saisissez votre demande et sélectionnez **Générer** pour convertir votre demande en SQL.
3. Vérifiez le SQL généré pour vous assurer qu'il est correct, puis enregistrez votre segment.

#### Exemples de demandes {#example-prompts}

- Utilisateurs ayant reçu un e-mail au cours du dernier mois
- Utilisateurs ayant effectué moins de cinq achats au cours de la dernière année

#### Conseils {#tips}

- Familiarisez-vous avec les [tables de données Snowflake]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) disponibles. Demander des données qui n'existent pas dans ces tables peut amener ChatGPT à inventer une fausse table.
- Familiarisez-vous avec les [règles d'écriture SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql) pour cette fonctionnalité. Ne pas respecter ces règles entraînera une erreur. Par exemple, votre code SQL doit sélectionner la colonne `user_id`. Commencer votre demande par « utilisateurs qui » peut aider.
- Vous pouvez envoyer jusqu'à 20 demandes par minute avec le générateur SQL par IA.

##{% multi_lang_include brazeai/generative_ai/policy.md %}

{% endtab %}
{% endtabs %}

{% alert note %}
Les requêtes SQL dont l'exécution dépasse 20 minutes seront interrompues pour dépassement de délai.
{% endalert %}

Lorsque l'extension a terminé le traitement, vous pouvez [créer un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment) en utilisant votre extension de segment et cibler ce nouveau segment avec vos Campaigns et Canvas.

### Étape 2 : Écrire votre SQL {#step-2-write-your-sql}

Votre requête SQL doit être rédigée en utilisant la [syntaxe Snowflake](https://docs.snowflake.com/en/sql-reference.html). Consultez la [référence des tables]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) pour obtenir la liste complète des tables et colonnes disponibles pour les requêtes.

{% alert important %}
Notez que les tables disponibles pour les requêtes contiennent uniquement des données d'événements. Si vous souhaitez interroger des attributs utilisateur, vous devez combiner votre segment SQL avec des filtres d'attributs personnalisés du [segmenteur classique]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).
{% endalert %}

{% tabs %}
{% tab Éditeur SQL %}

Votre SQL doit également respecter les règles suivantes :

- Écrivez une seule instruction SQL. N'incluez aucun point-virgule.
- Votre SQL doit sélectionner une seule colonne : la colonne `user_id`. Cela signifie que votre SQL doit contenir :

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- Il n'est pas possible d'interroger les utilisateurs n'ayant aucun événement, ce qui signifie que toute requête ciblant les utilisateurs ayant effectué un événement moins de X fois doit suivre cette méthode de contournement :
   1. Écrivez une requête pour sélectionner les utilisateurs ayant l'événement PLUS de X fois.
   2. Lorsque vous référencez votre extension de segment dans votre segment, sélectionnez `doesn't include` pour inverser le résultat.

#### Règles supplémentaires {#additional-rules}

De plus, votre requête SQL standard doit respecter les règles suivantes :

- Vous ne pouvez pas utiliser d'instructions `DECLARE`.
{% endtab %}
{% tab Éditeur SQL incrémentiel %}

Toutes les requêtes d'actualisation incrémentielle se composent de deux parties : une requête et des détails de schéma.

1. Dans l'éditeur, écrivez une requête qui sélectionne les `user_id` de la table souhaitée.
2. Ajoutez les détails du schéma en sélectionnant un **Opérateur**, un **Nombre de fois** et une **Période** dans les champs situés en haut de l'éditeur. La requête vérifie si la somme de la colonne agrégée respecte la condition que vous avez définie avec ces champs. Cela fonctionne de manière similaire au processus de création des extensions de segments classiques.<br><br>
   - **Opérateur :** Indiquez si l'événement s'est produit plus de, moins de ou exactement un certain nombre de fois.<br>
   ![Champ Opérateur avec « Plus de » sélectionné.]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **Nombre de fois :** Combien de fois vous souhaitez évaluer l'événement par rapport à l'opérateur.<br>
   ![Champ Nombre de fois avec « 5 » saisi.]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **Période :** Nombre de jours, de 1 à 730, pendant lesquels vous souhaitez vérifier les occurrences de l'événement. Cette période fait référence aux jours passés par rapport au jour actuel. L'exemple suivant montre une requête ciblant les utilisateurs ayant effectué l'événement plus de 5 fois au cours des 365 derniers jours.<br>
   ![Champ Période avec « 365 » saisi.]({% image_buster /assets/img_archive/sql_segments_period.png %})

Dans l'exemple suivant, le segment résultant contiendrait les utilisateurs ayant effectué l'événement `favorited` plus de 3 fois au cours des 30 derniers jours, après une date spécifiée.

![Éditeur SQL montrant un exemple d'extension de segment SQL incrémentielle.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![Aperçu SQL d'une extension de segment SQL incrémentielle.]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

{% alert tip %}
L'actualisation incrémentielle prend en compte les événements tardifs, c'est-à-dire les événements arrivés après la fenêtre d'actualisation quotidienne, comme les événements SDK qui n'ont pas été envoyés au moment de leur capture. Lors de l'actualisation du segment, Braze retraite les dates auxquelles ces événements tardifs appartiennent.
{% endalert %}

#### Comment l'actualisation incrémentielle suit les utilisateurs au fil du temps {#how-incremental-refresh-tracks-users-over-time}

Lorsque vous utilisez l'actualisation incrémentielle, Braze stocke les comptages quotidiens pour chaque utilisateur dans une table de comptages interne afin de pouvoir évaluer votre segment sur toute votre période sans réinterroger l'ensemble des données historiques chaque jour.

**Ce qui est stocké :** Braze maintient une table de comptages (similaire à une table de cohortes de segments) qui accumule les comptages de qualification quotidiens des utilisateurs au format `(date, user_id, count)`. Cette table conserve les données historiques en dehors de la fenêtre glissante d'actualisation de deux jours.

**Ce qui se passe à chaque actualisation :** Lors d'une actualisation incrémentielle, Braze efface uniquement les enregistrements de la fenêtre glissante de deux jours dans la table de comptages. Il réexécute ensuite votre requête SQL avec des paramètres de temps mis à jour (en utilisant `$start_date`) pour insérer de nouvelles lignes pour ces dates. Les lignes historiques en dehors de la fenêtre glissante de deux jours restent intactes dans la table de comptages.

**Comment Braze détermine qui fait partie du segment :** Braze évalue vos critères d'appartenance au segment par rapport à l'ensemble de la table de comptages accumulée, et non uniquement par rapport au payload le plus récent de la fenêtre glissante de deux jours. Cela signifie que les utilisateurs qualifiés il y a plus de deux jours restent dans le segment, sauf si les comptages agrégés ne remplissent plus vos critères.

**Écrire du SQL qui s'actualise de manière fiable :** Lors de l'écriture de SQL pour l'actualisation incrémentielle, évitez les modèles de requête pouvant produire des résultats incohérents lors d'actualisations partielles. Par exemple, les agrégations fenêtrées comme `MAX(time)` qui dépendent de données traversant les limites de `$start_date` peuvent modifier l'état des lignes de manière inattendue lorsque seul un sous-ensemble de dates est recalculé. Structurez vos requêtes de sorte que la sortie de chaque date dépende uniquement des événements de cette date, ce qui maintient des résultats cohérents, que la requête traite 2 ou 730 jours de données.

#### Règles supplémentaires

De plus, votre requête d'actualisation incrémentielle doit respecter les règles suivantes :

- Écrivez une seule instruction SQL. N'incluez aucun point-virgule.
- Votre segment SQL incrémentiel ne peut faire référence qu'à un seul événement. Vos menus déroulants pour la date et le comptage s'appliquent à cet événement.
- Votre SQL doit inclure l'alias `$date()` (par exemple, `$date(time)`), sélectionner `user_id` et une agrégation `COUNT()`, grouper par date et `user_id`, et filtrer avec `$start_date` sur votre colonne temporelle (par exemple, `time > $start_date`). Enregistrer du SQL sans `$date()` ou ces champs renvoie une erreur.
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

Avant d'enregistrer, vous pouvez exécuter un aperçu de votre requête. Les aperçus de requêtes sont automatiquement limités à 100 lignes et expireront après 60 secondes. L'exigence de la colonne `user_id` ne s'applique pas lors de l'exécution d'un aperçu.

Pour les extensions de segments SQL incrémentielles, l'aperçu n'inclut pas les critères supplémentaires liés à votre opérateur, au nombre de fois et à la période.

### Étape 4 : Déterminer si vous devez inverser le SQL {#step-4-determine-if-you-need-to-invert-sql}

Ensuite, déterminez si vous devez inverser le SQL. Bien qu'il ne soit pas possible d'interroger directement les utilisateurs n'ayant aucun événement, vous pouvez utiliser **Inverser le SQL** pour cibler ces utilisateurs.

{% alert note %}
Par défaut, **Inverser le SQL** n'est pas activé. Cependant, si vous utilisez le générateur SQL par IA pour générer une instruction SQL qui doit être inversée, ChatGPT pourrait renvoyer un résultat qui active automatiquement cette fonctionnalité.
{% endalert %}

Par exemple, pour cibler les utilisateurs ayant effectué moins de trois achats, écrivez d'abord une requête pour sélectionner les utilisateurs ayant effectué trois achats ou plus. Ensuite, sélectionnez **Inverser le SQL** pour cibler les utilisateurs ayant effectué moins de trois achats (y compris ceux n'ayant aucun achat).

{% alert important %}
Sauf si vous cherchez spécifiquement à cibler les utilisateurs n'ayant aucun événement, vous n'aurez pas besoin d'inverser le SQL. Si **Inverser le SQL** est sélectionné, confirmez que la fonctionnalité est nécessaire et que le segment correspond à l'audience souhaitée. Par exemple, si une requête cible les utilisateurs ayant au moins un événement, elle ne ciblera que les utilisateurs sans aucun événement lorsqu'elle est inversée.
{% endalert %}

![Extension de segment nommée « A cliqué sur 1 à 4 e-mails au cours des 30 derniers jours » avec l'option Inverser le SQL sélectionnée.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:90%;"}

## Actualisation de l'appartenance à un segment {#refreshing-segment-membership}

Pour actualiser l'appartenance à un segment de toute extension de segment créée à l'aide de SQL, ouvrez l'extension de segment et sélectionnez **Refresh**.

{% alert tip %}
Si vous avez créé un segment dans lequel vous vous attendez à ce que des utilisateurs entrent et sortent régulièrement, actualisez manuellement l'extension de segment qu'il utilise avant de cibler ce segment dans une Campaign ou un Canvas.
{% endalert %}

## Gestion de vos extensions de segments {#managing-your-segment-extensions}

Sur la page **Extensions de segments**, les segments générés à l'aide de SQL sont signalés par l'icône <i class="fas fa-code" alt="Extension de segment SQL"></i> à côté de leur nom.

Sélectionnez une extension de segment SQL pour voir où l'extension est utilisée, archiver l'extension ou [actualiser manuellement l'appartenance au segment](#refreshing-segment-membership).

![Section d'utilisation de la messagerie de l'éditeur SQL montrant où le segment SQL est utilisé.]({% image_buster /assets/img_archive/sql_segments_usage.png %}){: style="max-width:70%;"}

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