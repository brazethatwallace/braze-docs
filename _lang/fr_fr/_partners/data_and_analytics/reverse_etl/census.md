---
nav_title: Census
article_title: Census
description: "Cet article de référence présente le partenariat entre Braze et Census, une plateforme d'intégration de données qui vous permet de créer dynamiquement des segments d'utilisateurs ciblés avec les données de votre entrepôt de données cloud."
alias: /partners/census/
page_type: partner
search_tag: Partner

---

# Census

> [Census](https://www.getcensus.com/) est une plateforme d'activation des données qui connecte les entrepôts de données cloud comme Snowflake et BigQuery à Braze. Les équipes marketing peuvent exploiter la puissance de leurs données first-party pour créer des segments d'audience dynamiques, synchroniser les attributs des clients pour personnaliser les campagnes et maintenir à jour toutes leurs données dans Braze. Il est plus facile que jamais d'agir grâce à des données fiables et exploitables — pas besoin de télécharger des fichiers CSV ou de faire appel à des ingénieurs.

L'intégration entre Braze et Census vous permet d'importer dynamiquement des audiences ou des données produit dans Braze afin d'envoyer des campagnes personnalisées. Par exemple, vous pouvez créer une cohorte dans Braze pour les « abonnés à la newsletter avec CLV > 1000 » afin de cibler les clients à forte valeur ajoutée, ou les « utilisateurs actifs au cours des 30 derniers jours » afin de cibler des utilisateurs spécifiques pour tester une fonctionnalité bêta à venir.

## Prérequis {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte Census | Un [compte Census](https://www.getcensus.com/) est nécessaire pour profiter de ce partenariat. |
| Clé REST API de Braze | Une clé REST API de Braze avec toutes les autorisations relatives aux données utilisateur (à l'exception de `users.delete`) et les autorisations `segments.list`. L'ensemble des autorisations peut évoluer à mesure que Census ajoute la prise en charge de nouveaux objets Braze. Il est donc conseillé d'accorder davantage d'autorisations dès maintenant ou de prévoir une mise à jour ultérieure. <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). |
| Entrepôt de données et modèle de données | Avant de commencer l'intégration, vous devez avoir configuré un entrepôt de données dans Census et défini un modèle du sous-ensemble de données que vous souhaitez synchroniser avec Braze. Consultez la [documentation de Census](https://docs.getcensus.com/destinations/braze) pour obtenir la liste des sources de données disponibles et des conseils sur la création de modèles. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Créer une connexion de service Braze {#step-1-create-braze-service-connection}

Pour intégrer Census dans la plateforme Census, accédez à l'onglet **Connections** et sélectionnez **New Destination** pour créer une nouvelle connexion de service Braze.

Dans l'invite qui s'affiche, nommez cette connexion et indiquez l'URL de votre endpoint Braze et la clé REST API de Braze (et, éventuellement, votre clé d'importation des données pour synchroniser les cohortes).

![Boîte de dialogue Census de nouvelle destination configurée pour les identifiants de connexion Braze.]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### Étape 2 : Créer une synchronisation Census {#step-2-create-a-census-sync}

Pour synchroniser les clients avec Braze, vous devez créer une synchronisation. Ici, vous définissez où synchroniser les données et comment vous souhaitez mapper les champs entre les deux plateformes.

1. Accédez à l'onglet **Syncs** et sélectionnez **New Sync**.<br><br>
2. Dans le composeur, sélectionnez le modèle de données source à partir de votre entrepôt de données.<br><br>
3. Configurez la destination de synchronisation du modèle. Sélectionnez **Braze** comme destination et le [type d'objet pris en charge](#supported-objects) à synchroniser.<br>![Dans l'invite « Select a Destination », « Braze » est sélectionné comme connexion et divers objets sont répertoriés.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. Sélectionnez la règle de synchronisation que vous souhaitez appliquer (**Update or Create** est le choix le plus courant, mais vous pouvez choisir des règles plus avancées pour gérer la suppression de données, par exemple).<br><br>
5. Ensuite, à des fins de correspondance des enregistrements, choisissez une clé de synchronisation pour [mapper](#supported-objects) votre objet Braze sur un champ du modèle.<br>![Dans l'invite « Select a Sync Key », « External User ID » de Braze est associé à « user_id » dans la source.]({% image_buster /assets/img/census/census_1.png %}){: style="max-width:80%;"}<br><br>
6. Enfin, mappez les champs de données Census sur les champs Braze équivalents.<br>![Mappage Census]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
7. Confirmez les détails et créez la synchronisation.

Une fois la synchronisation exécutée, les données utilisateur se trouvent dans Braze. Vous pouvez créer et ajouter un Segment Braze aux futures Campaigns et Canvas Braze pour cibler ces utilisateurs.

{% alert note %}
Lors de l'utilisation de l'intégration Census et Braze, Census n'envoie que les deltas (données modifiées) à chaque synchronisation vers Braze.
{% endalert %}

## Objets pris en charge {#supported-objects}

Census prend actuellement en charge la synchronisation des objets Braze suivants :

| Nom de l'objet | Comportements de synchronisation |
| --- | --- |
| User | Update, Create, Mirror, Delete |
| Cohort | Update, Create, Mirror |
| Catalog | Update, Create, Mirror |
| Subscription Group Membership | Mirror |
| Event | Append |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Objets pris en charge" }

De plus, Census prend en charge l'envoi de [données structurées](https://docs.getcensus.com/destinations/braze#supported-objects) à Braze. Pour envoyer des jetons push d'utilisateurs, vos données doivent être structurées sous forme de tableau d'objets comportant 2 à 3 valeurs : `app_id`, `token` et un `device_id` facultatif.