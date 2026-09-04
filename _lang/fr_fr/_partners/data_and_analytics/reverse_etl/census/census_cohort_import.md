---
nav_title: Census
article_title: Importation de la cohorte Census
description: "Cet article de référence présente la fonctionnalité d'importation de cohortes de Census, une plateforme d'intégration de données qui vous permet de créer dynamiquement des segments d'utilisateurs ciblés avec les données de votre entrepôt de données cloud."
page_type: partner
search_tag: Partner

---

# Importation de la cohorte Census {#census-cohort-import}

> Cet article décrit comment importer des cohortes d'utilisateurs depuis [Census](https://www.getcensus.com/) vers Braze. Pour plus d'informations sur l'intégration de Census, consultez l'[article principal sur Census]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/census).

## Intégration de l'importation de cohortes {#cohort-import-integration}

### Étape 1 : Créer une connexion de service Braze {#step-1-create-braze-service-connection}

Pour intégrer Census dans la plateforme Census, accédez à l'onglet **Connections** et sélectionnez **New Destination** pour créer une nouvelle connexion de service Braze.

Dans l'invite qui s'affiche, nommez cette connexion et indiquez l'URL de votre endpoint Braze, la clé REST API de Braze et la clé d'importation des données. La clé d'importation des données est nécessaire pour synchroniser les cohortes et peut être trouvée dans Braze en accédant à **Intégrations partenaires** > **Partenaires technologiques** > **Census**.

![Boîte de dialogue Census de nouvelle destination configurée pour les identifiants d'importation de cohorte Braze.]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### Étape 2 : Créer une synchronisation Census {#step-2-create-a-census-sync}

Pour synchroniser les clients avec Braze, vous devez créer une synchronisation. Vous définirez ici où synchroniser les données et comment mapper les champs entre les deux plateformes.

1. Accédez à l'onglet **Syncs** et sélectionnez **New Sync**.<br><br>
2. Dans le compositeur, sélectionnez le modèle de données source de votre entrepôt de données.<br><br>
3. Configurez la destination de synchronisation du modèle. Sélectionnez **Braze** comme destination et **User & Cohort** comme objet à synchroniser.<br>![Dans l'invite « Select a Destination », « Braze » est sélectionné comme connexion, et divers objets sont répertoriés.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. Sélectionnez la **Source Column** qui identifie les utilisateurs à ajouter à une cohorte et sélectionnez **External User ID** comme **Identifier Type**.<br><br>
5. Dans le menu déroulant **Cohort Name**, sélectionnez une cohorte, créez une cohorte ou sélectionnez une colonne source pour remplir le nom de la cohorte.<br><br>
6. Utilisez le menu déroulant **When a record is removed from source data** pour sélectionner ce qui arrive aux utilisateurs lorsqu'ils sont supprimés de l'ensemble de données source, par exemple **Do nothing** ou **Remove matching record from cohort**.<br><br>
7. Enfin, mappez les champs de données Census aux champs équivalents de Braze.<br>![Mappage Census]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
8. Confirmez les détails et créez la synchronisation.

Vous pouvez maintenant lancer votre synchronisation !

Lors d'une synchronisation, tous les champs que vous mappez seront d'abord synchronisés avec l'objet utilisateur afin de mettre à jour ce qui existe déjà dans Braze. Ensuite, l'utilisateur mis à jour sera ajouté à la cohorte spécifiée.

Après la synchronisation, vous pouvez créer et ajouter un segment Braze avec un filtre de cohorte Census aux futures Campaigns et Canvas Braze pour cibler ces utilisateurs.

{% alert note %}
Lorsque vous utilisez l'intégration Census et Braze, Census n'envoie à Braze que les deltas (données modifiées) à chaque synchronisation.
{% endalert %}

{% alert important %}
Seuls les utilisateurs qui existent déjà dans Braze pourront être ajoutés ou supprimés d'une cohorte. L'importation de cohorte ne créera pas de nouveaux utilisateurs dans Braze.
{% endalert %}

## Correspondance des utilisateurs {#user-matching}

Les utilisateurs identifiés peuvent être associés par leur `external_id` ou leur `alias`. Les utilisateurs anonymes peuvent être associés par leur `device_id`. Les utilisateurs identifiés qui ont été créés à l'origine en tant qu'utilisateurs anonymes ne peuvent pas être identifiés par leur `device_id` et doivent être identifiés par leur `external_id` ou leur `alias`.