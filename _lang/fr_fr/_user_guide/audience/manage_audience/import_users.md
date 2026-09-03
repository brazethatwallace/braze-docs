---
nav_title: Importer des utilisateurs
article_title: Importer des utilisateurs
page_order: 3
description: "Découvrez les différentes options d'importation d'utilisateurs de Braze, comme l'importation CSV, la REST API, l'Ingestion de données cloud, et plus encore."

---
# Importer des utilisateurs {#import-users}

> Découvrez les différentes options d'importation d'utilisateurs de Braze, comme l'importation CSV, la REST API, l'Ingestion de données cloud, et plus encore.

## Options d'importation {#import-options}

Vous pouvez télécharger des attributs utilisateur et des événements par le biais d'une importation CSV dans Braze, d'un script Lambda S3 serverless d'importation CSV, d'appels API directs ou de l'ingestion de données Cloud depuis votre entrepôt de données.

### Importation CSV Braze {#braze-csv-import}

Vous pouvez utiliser l'importation CSV pour enregistrer et mettre à jour les attributs utilisateur et événements personnalisés suivants. Pour commencer, consultez [Importation CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import).

| Type | Définition | Exemple | Taille maximale du fichier |
|---|---|---|---|
| Attributs par défaut | Attributs utilisateur réservés reconnus par Braze. | `first_name`, `email` | 500 Mo |
| Attributs personnalisés | Attributs utilisateur propres à votre entreprise. | `last_destination_searched` | 500 Mo |
| Événements personnalisés | Événements propres à votre entreprise qui représentent des actions utilisateur. | `trip_booked` | 50 Mo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Importation CSV Braze" }

#### Construire votre CSV {#constructing-your-csv}

Braze accepte les données utilisateur au format CSV standard. Les importations d'attributs par défaut et personnalisés prennent en charge des fichiers jusqu'à 500 Mo ; les importations d'événements personnalisés prennent en charge des fichiers jusqu'à 50 Mo. Pour les identifiants, les en-têtes de colonnes, les règles de validation et les exemples, consultez [Importation CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import).

Lorsque vous téléchargez un fichier CSV volumineux via **Import Users** dans le tableau de bord, la page peut sembler ne pas répondre ou réagir lentement pendant que Braze reçoit le fichier et exécute l'étape de calcul. Laissez le téléchargement et le calcul se terminer — la durée totale varie de quelques minutes à quelques heures selon la taille du fichier, et les fichiers plus volumineux prennent plus de temps à calculer.

{% alert note %}
Lorsque vous importez des événements personnalisés avec des propriétés, vous devez utiliser la notation par points dans les en-têtes de colonnes de votre CSV. Pour plus d'informations sur le formatage des événements personnalisés, consultez [Comprendre le formatage des événements personnalisés]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import?tab=custom%20events#understanding-custom-event-formatting).
{% endalert %}

### Importation CSV Lambda d'utilisateurs {#lambda-user-csv-import}

Utilisez notre script Lambda S3 serverless d'importation CSV pour télécharger des attributs utilisateur vers Braze. Cette solution fonctionne comme un outil de téléchargement CSV : vous déposez vos fichiers CSV dans un compartiment S3, et les scripts les téléchargent via notre API.

Les temps d'exécution estimés pour un fichier de 1 000 000 de lignes sont d'environ cinq minutes. Consultez [Importation d'attributs utilisateur CSV vers Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) pour plus d'informations.

### REST API

Utilisez l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) pour enregistrer des événements personnalisés, des attributs utilisateur et des achats pour les utilisateurs.

### Ingestion de données Cloud {#cloud-data-ingestion}

Utilisez l'[ingestion de données Cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) de Braze pour importer et maintenir les attributs utilisateur.

## Validation HTML {#html-validation}

Gardez à l'esprit que Braze ne nettoie pas, ne valide pas et ne reformate pas les données HTML lors de l'importation, ce qui signifie que les balises script doivent être supprimées de toutes les données d'importation que vous utilisez pour la personnalisation web.

Lors de l'importation de données dans Braze spécifiquement destinées à la personnalisation dans un navigateur web, assurez-vous qu'elles sont débarrassées de tout HTML, JavaScript ou toute autre balise script qui pourrait potentiellement être exploitée de manière malveillante lors du rendu dans un navigateur web.

Alternativement, pour le HTML, vous pouvez utiliser les filtres Liquid de Braze (`strip_html`) pour supprimer le HTML du texte rendu. Par exemple :

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}