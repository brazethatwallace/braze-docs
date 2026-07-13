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

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte Census | Un [compte Census](https://www.getcensus.com/) est nécessaire pour profiter de ce partenariat. |
| Clé d'API REST Braze | Une clé API REST Braze avec toutes les autorisations relatives aux données utilisateur (à l'exception de `users.delete`) et les autorisations `segments.list`. Le jeu d'autorisations peut changer au fur et à mesure que Census prend en charge d'autres objets Braze. Vous pouvez donc soit accorder plus d'autorisations maintenant, soit prévoir de les mettre à jour à l'avenir. <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). |
| Entrepôt de données et modèle de données | Avant de commencer l'intégration, vous devez disposer d'un entrepôt de données configuré dans Census et définir un modèle du sous-ensemble de données que vous souhaitez synchroniser avec Braze. Consultez la [documentation Census](https://docs.getcensus.com/destinations/braze) pour obtenir une liste des sources de données disponibles et des conseils sur la création de modèles. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Créer un branchement de service Braze {#step-1-create-braze-service-connection}

Pour intégrer Census dans la plateforme Census, accédez à l'onglet **Connexions** et sélectionnez **Nouvelle destination** pour créer une nouvelle connexion de service Braze.

Dans l'invite qui s'affiche, donnez un nom à cette connexion et indiquez l'URL de votre endpoint Braze ainsi que la clé API REST de Braze (et, éventuellement, votre clé d'importation des données pour synchroniser les cohortes).

![Boîte de dialogue Census de nouvelle destination configurée pour les identifiants de connexion Braze.]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### Étape 2 : Créer une synchronisation Census {#step-2-create-a-census-sync}

Pour synchroniser les clients avec Braze, vous devez créer une synchronisation. Ici, vous définirez où synchroniser les données et comment vous souhaitez que les champs soient mappés entre les deux plateformes.

1. Accédez à l'onglet **Syncs** et sélectionnez **New Sync**.<br><br>
2. Dans le compositeur, sélectionnez le modèle de données source de votre entrepôt de données.<br><br>
3. Configurez l'endroit où le modèle sera synchronisé. Sélectionnez **Braze** comme destination et le [type d'objet pris en charge](#supported-objects) à synchroniser.<br>![Dans l'invite « Select a Destination », « Braze » est sélectionné comme connexion et divers objets sont répertoriés.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. Sélectionnez la règle de synchronisation que vous souhaitez appliquer (**Update or Create** est le choix le plus courant, mais vous pouvez choisir des règles plus avancées pour gérer la suppression de données, par exemple).<br><br>
5. Ensuite, à des fins de correspondance des enregistrements, choisissez une clé de synchronisation pour [mapper](#supported-objects) votre objet Braze à un champ de modèle.<br>![Dans l'invite « Select a Sync Key », « External User ID » de Braze correspond à « user_id » dans la source.]({% image_buster /assets/img/census/census_1.png %}){: style="max-width:80%;"}<br><br>
6. Enfin, mappez les champs de données Census aux champs équivalents de Braze.<br>![Mappage Census]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
7. Confirmez les détails et créez la synchronisation.

Une fois la synchronisation effectuée, les données utilisateur seront disponibles dans Braze. Vous pouvez désormais créer et ajouter un segment Braze aux futures Campaigns et Canvas Braze afin de cibler ces utilisateurs.

{% alert note %}
Lorsque vous utilisez l'intégration Census et Braze, Census n'envoie à Braze que les deltas (données modifiées) à chaque synchronisation.
{% endalert %}

## Objets pris en charge {#supported-objects}

Census prend actuellement en charge la synchronisation des objets Braze suivants :

| Nom de l'objet | Comportements de synchronisation |
| --- | --- |
| Utilisateur | Mise à jour, création, miroir, suppression |
| Cohorte | Mise à jour, création, miroir |
| Catalogue | Mise à jour, création, miroir |
| Groupe d'abonnement | Miroir |
| Événement | Ajout |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Objets pris en charge" }

De plus, Census prend en charge l'envoi de [données structurées](https://docs.getcensus.com/destinations/braze#supported-objects) à Braze :
- Jetons de notification push utilisateur : pour envoyer des jetons de notification push, vos données doivent être structurées sous forme d'un tableau d'objets avec 2 à 3 valeurs : `app_id`, `token` et un `device_id` facultatif.
- Attributs personnalisés imbriqués : les objets et les tableaux sont pris en charge. En avril 2022, cette fonctionnalité est encore en accès anticipé. Il se peut que vous deviez contacter votre gestionnaire de compte Braze pour y accéder.