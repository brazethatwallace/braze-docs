---
nav_title: Celebrus
article_title: Intégration de Celebrus
description: "Intégration de Braze et Celebrus."
---

# Celebrus

> Celebrus s'intègre de façon fluide au SDK Braze sur les canaux web et les applications mobiles, facilitant ainsi l'alimentation de Braze avec les données d'activité des canaux. Cela inclut des informations complètes sur le trafic de visiteurs sur les actifs numériques au cours de périodes spécifiées. <br><br>En outre, Celebrus collecte des données de profil riches pour chaque client individuel, qui peuvent être synchronisées avec Braze. Cela vous permet de créer des stratégies d'analyse et de communication efficaces avec Braze, basées sur des données first-party complètes, précises et détaillées. Cette fonctionnalité est renforcée par les signaux pilotés par le machine learning de Celebrus, qui permettent une capture de données sans tracas, sans avoir besoin d'un balisage approfondi. Grâce à un graphe d'identité first-party robuste, toutes les données deviennent instantanément accessibles pour une utilisation immédiate.

_Cette intégration est maintenue par Celebrus._

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Celebrus | Un compte Celebrus est nécessaire pour bénéficier de ce partenariat. |
| Entrepôt de données (facultatif) | Lorsque vous utilisez le connecteur Celebrus pour les attributs personnalisés de Braze, vous devez disposer d'un entrepôt de données pris en charge par l'intégration Braze Cloud Data Ingestion (CDI) et configurer le CDI dans le tableau de bord de Braze. |
| Paramètres de configuration du SDK Braze (facultatif) | Lorsque vous utilisez le connecteur Celebrus pour le SDK Braze, vous devez transmettre l'endpoint du SDK et la clé API du SDK. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Mise en œuvre {#implementation}
Après avoir installé votre implémentation Celebrus, utilisez les connecteurs Celebrus pour Braze afin d'intégrer les données Celebrus dans Braze. L'intégration de Celebrus pour Braze comporte deux éléments : le SDK Braze et les attributs personnalisés de Braze. Vous pouvez déployer l'un ou l'autre, ou les deux, selon la façon dont vous utilisez Braze et les cas d'utilisation dont vous avez besoin.

Si le SDK Braze n'est pas encore déployé sur votre canal web, vous pouvez utiliser Celebrus pour déployer le SDK Braze. Celebrus ajoutera le SDK Braze aux pages web et configurera l'identité Braze pour le visiteur web à l'aide du graphe d'identité Celebrus. Les attributs des clients peuvent être synchronisés avec Braze via l'ingestion de données cloud (CDI). Cela nécessite un entrepôt de données pris en charge par le CDI Braze et la configuration du CDI dans Braze.

### Connecteur Celebrus pour le SDK Braze {#celebrus-connector-for-braze-sdk}

Le connecteur Celebrus pour le SDK Braze fournit des données de haut niveau sur les canaux web et les applications mobiles pour Braze. Dans le SDK Braze, le paramètre `System Identity` du graphe d'identité de Celebrus sera utilisé comme identifiant pour l'intégration Braze. D'autres identifiants sont pris en charge pour la synchronisation des attributs personnalisés via le connecteur Celebrus pour les attributs personnalisés de Braze.

Dans la mesure où le connecteur déploie et configure le SDK Braze dans votre canal, il vous faudra configurer certains paramètres dans le flux de données du SDK Braze et fournir les valeurs de ces trois paramètres :

```
    response.addParameter("sdk_endpoint", "sdk.xxxxxx.braze.com");
    response.addParameter("api_key", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
    response.addParameter("app_id", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
```

{% alert important %}
Le connecteur Celebrus pour le SDK Braze insère et initialise le SDK Braze pour identifier l'utilisateur et ajouter l'identifiant au graphe d'identité de Celebrus. Ce connecteur n'enregistre pas les données dans le profil utilisateur et ne déclenche pas d'autres méthodes du SDK Braze. <br><br>Vous pouvez appeler toutes les méthodes souhaitées directement dans votre base de code pour enregistrer des données via le [SDK Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) ou tirer parti d'autres fonctionnalités prises en charge par le SDK Braze.
{% endalert%}

### Connecteur Celebrus pour les attributs personnalisés de Braze {#celebrus-connector-for-braze-custom-attributes}

#### Étape 1 : Configurer les détails de connexion dans Celebrus {#step-1-configure-connected-details-in-celebrus}

Le connecteur Celebrus pour les attributs personnalisés de Braze envoie des attributs personnalisés à une base de données intermédiaire, préformatée de la manière dont Braze s'attend à les recevoir. Dans Celebrus, vous configurez les détails de connexion à la base de données, qui dépendent du type de base de données que vous utilisez (comme Snowflake ou Redshift).

#### Étape 2 : Configurer l'ingestion de données cloud dans votre tableau de bord de Braze {#step-2-configure-cloud-data-ingestion-in-your-braze-dashboard}

Cette intégration utilise l'ingestion de données cloud de Braze. Suivez les instructions de la section [Intégrations des entrepôts de données]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/) pour configurer les [paramètres d'ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/) en fonction du type d'entrepôt que vous utilisez.

#### Étape 3 : Synchroniser les données de Celebrus vers Braze {#step-3-sync-data-from-celebrus-to-braze}

Celebrus capture et attribue des identifiants uniques à une personne, tels qu'un e-mail, un numéro de téléphone, un `external_id` ou un alias d'utilisateur, et les envoie à Braze via le CDI. Cela permet de synchroniser les données avec Braze pour la même personne.

Celebrus utilisera les identifiants définis pour envoyer les attributs clients définis dans le générateur de profils Celebrus, mais uniquement lorsque les valeurs des attributs changent. Notez que les noms d'attributs définis dans le générateur de profils Celebrus seront utilisés par défaut dans Braze. Veillez donc à mettre à jour ces noms pour respecter les [conventions de dénomination de Braze]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens).

{% alert important %}
Pour l'instant, cette version ne prend pas en charge les événements et les achats.<br><br> Cette intégration envoie les attributs sous forme de valeurs de chaîne de caractères. Certains attributs sont donc des listes (comme les signaux). Pour l'instant, les listes ne peuvent pas être converties en tableaux. Il n'existe aucun attribut imbriqué.
{% endalert%}