---
nav_title: Sémantique de livraison des événements
article_title: Sémantique de livraison des événements
page_order: 2
page_type: reference
description: "Cet article de référence décrit et définit la manière dont Currents gère les données d'événements en fichier plat que nous envoyons aux partenaires de stockage de l'entrepôt de données."
tool: Currents

---

# Sémantique de livraison des événements {#event-delivery-semantics}

> Cette page décrit et définit la manière dont Currents gère les données d'événements sous forme de fichiers plats que nous envoyons aux partenaires de stockage de l'entrepôt de données.

Currents for Data Storage permet un flux continu de données de notre plateforme vers un compartiment de stockage de l'un de nos [partenaires d'entrepôt de données]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/). Currents écrit les fichiers Avro dans votre compartiment de stockage à des seuils réguliers, ce qui vous permet de traiter et d'analyser les données d'événements en utilisant vos propres outils d'aide à la décision.

{% alert important %}
Ce contenu **s'applique uniquement aux données d'événements de fichiers plats que nous envoyons aux partenaires de stockage de l'entrepôt de données (Google Cloud Storage, Amazon S3 et Microsoft Azure Blob Storage)**. <br><br>Pour le contenu qui s'applique aux autres partenaires, reportez-vous à notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/) et consultez leurs pages respectives.
{% endalert %}

## Événements de test {#test-events}

Lorsque vous configurez une intégration Currents, cliquez sur **Send Test Events** pour vérifier la connexion avec votre compartiment de stockage. Ces événements de test permettent de vérifier que votre intégration peut recevoir et traiter correctement les données.

{% alert important %}
**Format des données des événements de test :** les événements de test contiennent des valeurs de marque substitutive qui correspondent aux types de données corrects pour chaque champ, mais ne contiennent pas de données réalistes ou exactes. Par exemple, un champ `timezone` peut contenir une chaîne de caractères de type UUID au lieu d'un identifiant de fuseau horaire valide (tel que « America/Chicago »), et d'autres champs comme `campaign_name` et `ip_pool` peuvent également contenir des valeurs de marque substitutive plutôt que des données réelles.<br>

Il s'agit d'un comportement attendu. Les événements de test servent principalement à tester la connexion et la configuration de l'intégration, et non à valider l'exactitude des données. Pour voir des événements réels avec des données exactes, utilisez une intégration Currents de test pour envoyer des données d'événements réels à travers votre pipeline.
{% endalert %}

## Livraison « au moins une fois » {#at-least-once-delivery}

En tant que système à haut débit, Currents fournit une livraison « au moins une fois » des événements, ce qui signifie que des événements en double peuvent occasionnellement être écrits dans votre compartiment de stockage. Cela peut se produire lorsque des événements sont retraités depuis notre file d'attente pour une raison quelconque.

Si vos cas d'utilisation nécessitent une livraison « exactement une fois », vous pouvez utiliser le champ d'identifiant unique envoyé avec chaque événement (`id`) pour dédupliquer les événements. Étant donné que le fichier échappe à notre contrôle une fois écrit dans votre compartiment de stockage, nous ne pouvons pas garantir la déduplication de notre côté.

## Horodatages {#timestamps}

Tous les horodatages exportés par Currents sont envoyés dans le fuseau horaire UTC. Pour certains événements où il est disponible, un champ de fuseau horaire est également inclus, qui fournit le format IANA (Internet Assigned Numbers Authority) du fuseau horaire local de l'utilisateur au moment de l'événement.

### Latence {#latency}

Les événements envoyés à Braze via le SDK ou l'API peuvent inclure un horodatage du passé. L'exemple le plus courant est lorsque les données du SDK sont mises en file d'attente, par exemple en l'absence de connectivité mobile. Dans ce cas, l'horodatage de l'événement reflète le moment où l'événement a été généré. Cela signifie qu'un pourcentage d'événements semblera avoir une latence élevée.

## Format Apache Avro {#apache-avro-format}

Les intégrations de stockage de données de Braze Currents produisent des données au format `.avro`. Nous avons choisi [Apache Avro](https://avro.apache.org/) car il s'agit d'un format de données flexible qui prend nativement en charge l'évolution des schémas et est compatible avec une grande variété de produits de données :

- Avro est pris en charge par la quasi-totalité des principaux entrepôts de données.
- Si vous souhaitez conserver vos données dans S3, Avro offre une meilleure compression que CSV et JSON, ce qui réduit vos coûts de stockage et peut potentiellement nécessiter moins de CPU pour analyser les données.
- Avro exige des schémas lors de l'écriture ou de la lecture des données. Les schémas peuvent évoluer au fil du temps pour gérer l'ajout de champs sans provoquer de rupture.

Currents crée un fichier pour chaque type d'événement en utilisant le format suivant :

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>/event_type=<event-type>/date=<date>/version=<currents_version>/<environment>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>+<partition>+<offset>.avro
```

{% alert tip %}
Vous ne voyez pas le code à cause de la barre de défilement ? Découvrez comment résoudre ce problème [ici]({{site.baseurl}}/user_guide/).
{% endalert %}

Par exemple, le chemin d'un événement d'envoi de notification push peut ressembler à ceci :

```
currents-export/dataexport.prod-01.S3.integration.69cadaaed2d51b7c75b1a3e5/event_type=users.messages.pushnotification.Send/date=2025-04-01-17/version=6/us-01/dataexport.prod-01.S3.integration.69cadaaed2d51b7c75b1a3e5+0+123456.avro
```

Le segment de chemin `version` est un simple entier représentant la version de Currents, par exemple `version=6`.

| Segment du nom de fichier | Définition |
|---|---|
| `<your-bucket-prefix>` | Le préfixe défini pour cette intégration Currents. |
| `<cluster-identifier>` | Réservé à l'usage interne de Braze. Il s'agit d'une chaîne de caractères telle que « prod-01 », « prod-02 », « prod-03 » ou « prod-04 ». Tous les fichiers auront le même identifiant de cluster. |
| `<connection-type-identifier>` | L'identifiant du type de connexion. Les options sont « S3 », « AzureBlob » ou « GCS ». |
| `<integration-id>` | L'ID unique de cette intégration Currents. |
| `<event-type>` | Le type d'événement contenu dans le fichier. |
| `<date>` | L'heure à laquelle les événements sont mis en file d'attente dans notre système pour traitement, dans le fuseau horaire UTC. Format AAAA-MM-JJ-HH. |
| `version=<currents_version>` | La version de Currents pour le chemin du pipeline. Cette valeur est un simple entier tel que `6`. |
| `<environment>` | Réservé à l'usage interne de Braze. |
| `<partition>` | Réservé à l'usage interne de Braze. Entier. |
| `<offset>` | Réservé à l'usage interne de Braze. Entier. Notez que différents fichiers envoyés au cours de la même heure auront un paramètre `<offset>` différent. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Format Apache Avro" }

{% alert tip %}
Les conventions de nommage des fichiers peuvent changer. Braze recommande de rechercher toutes les clés de votre compartiment ayant le préfixe &lt;your-bucket-prefix&gt;.
{% endalert %}

### Seuil d'écriture Avro {#avro-write-threshold}

Dans des conditions normales, Braze écrit des fichiers de données dans votre compartiment de stockage toutes les 5 minutes ou tous les 15 000 événements, selon la condition remplie en premier. En cas de charge élevée, nous pouvons écrire des fichiers de données plus volumineux contenant jusqu'à 100 000 événements par fichier.

{% alert important %}
Currents n'écrira jamais de fichiers vides.
{% endalert %}

### Modifications du schéma Avro {#avro-schema-changes}

De temps en temps, Braze peut apporter des modifications au schéma Avro lorsque des champs sont ajoutés, modifiés ou supprimés. Pour nos besoins ici, il existe deux types de modifications : avec rupture et sans rupture. Toutes les modifications de schéma sont regroupées dans les versions de Currents, et chaque version fait avancer le segment `version=<currents_version>` dans le chemin de stockage (par exemple, de `version=6` à `version=7`). Les événements Currents écrits dans Azure Blob Storage, Google Cloud Storage et Amazon S3 utilisent le format de chemin suivant :

```
<your-bucket-prefix>/<currents-integration-id>/event_type=<event-type>/date=<date>/version=<currents_version>/<environment>/<avro-file>
```

#### Modifications sans rupture {#non-breaking-changes}

Lorsqu'un champ est ajouté au schéma Avro, nous considérons qu'il s'agit d'une modification sans rupture. Les champs ajoutés seront toujours des champs Avro « optionnels » (par exemple avec une valeur par défaut de `null`), de sorte qu'ils « correspondent » aux anciens schémas selon la [spécification de résolution de schéma Avro](http://avro.apache.org/docs/current/spec.html#schema+resolution). Ces ajouts ne devraient pas affecter les processus ETL (extraire, transformer, charger) existants, car le champ sera simplement ignoré jusqu'à ce qu'il soit ajouté à votre processus ETL.

{% alert important %}
Nous recommandons que votre configuration ETL soit explicite quant aux champs qu'elle traite afin d'éviter toute interruption du flux lorsque de nouveaux champs sont ajoutés.
{% endalert %}

#### Modifications avec rupture {#breaking-changes}

Lorsqu'un champ est supprimé ou modifié dans le schéma Avro, nous considérons qu'il s'agit d'une modification avec rupture. Les modifications avec rupture peuvent nécessiter des ajustements des processus ETL existants, car des champs précédemment utilisés peuvent ne plus être enregistrés comme prévu.

Toutes les modifications avec rupture seront communiquées avant la publication de la version.

Pour un historique complet des modifications par version, consultez le [journal des modifications de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/).