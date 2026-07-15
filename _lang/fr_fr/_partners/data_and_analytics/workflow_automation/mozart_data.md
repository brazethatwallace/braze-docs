---
nav_title: Mozart Data
article_title: Mozart Data
description: "Cet article de référence présente le partenariat entre Braze et Mozart Data, une plateforme de données moderne tout-en-un, vous permettant d'utiliser Fivetran pour importer des données vers Snowflake, créer des transformations, combiner des données, et plus encore."
alias: /partners/mozart_data/
page_type: partner
search_tag: Partner

---

# Mozart Data

{% multi_lang_include video.html id="HU6dSOClcQ0" align="right" %}

> [Mozart Data](https://mozartdata.com/) est une plateforme de données moderne tout-en-un alimentée par Fivetran, Portable et Snowflake.

L'intégration de Braze et Mozart Data vous permet de :
- Utiliser Fivetran pour importer les données de Braze dans Snowflake
- Créer des transformations en combinant les données Braze avec les données d'autres applications et analyser efficacement les comportements des utilisateurs
- Importer les données de Snowflake dans Braze pour créer de nouvelles opportunités d'engagement client
- Combiner les données Braze avec les données d'autres applications pour obtenir une compréhension plus globale des comportements des utilisateurs
- S'intégrer à un outil d'aide à la décision pour explorer davantage les données stockées dans Snowflake

## Conditions préalables {#prerequisites}

<style>
table th:nth-child(1) {
    width: 25%;
}
table th:nth-child(2) {
    width: 75%;
}
table td {
    word-break: break-word;
}
</style>

| Condition | Description |
| ----------- | ----------- |
| Compte Mozart Data | Un compte Mozart Data est nécessaire pour profiter de ce partenariat. [Inscrivez-vous ici.](https://app.mozartdata.com/signup)|
| Compte Snowflake<br>Option 1 : Nouveau compte | Sélectionnez **Create a New Snowflake Account** pendant le processus de création du compte Mozart Data pour que Mozart Data crée un nouveau compte Snowflake pour vous. |
| Compte Snowflake<br>Option 2 : Compte existant | Si votre entreprise possède déjà un compte Snowflake, vous pouvez utiliser l'option Mozart Data Connected.<br><br>Sélectionnez l'option **Already Have a Snowflake Account** pour connecter un compte Snowflake existant. Pour mettre en œuvre cette option, un utilisateur disposant d'autorisations au niveau du compte doit [suivre ces étapes](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

L'intégration est prise en charge à la fois pour la synchronisation des données de [Braze vers Mozart Data](#syncing-data-from-braze-to-mozart-data) et de [Mozart Data vers Braze](#syncing-data-from-mozart-data-to-braze).

### Synchronisation des données de Braze vers Mozart Data {#syncing-data-from-braze-to-mozart-data}

#### Étape 1 : Configurer le connecteur Braze {#step-1-set-up-braze-connector}

1. Dans Mozart Data, allez dans **Connectors** et sélectionnez **Add Connector**.
2. Recherchez « Braze » et sélectionnez la carte du connecteur.
3. Saisissez un nom de schéma de destination où seront stockées toutes les données synchronisées depuis Braze. Nous vous recommandons d'utiliser le nom de schéma par défaut `braze`.
4. Sélectionnez **Add Connector**.

#### Étape 2 : Remplir le formulaire du connecteur Fivetran {#step-2-fill-out-the-fivetran-connector-form}

La page du connecteur Fivetran s'ouvre une fois l'étape 1 terminée. Remplissez les champs indiqués, puis sélectionnez **Continue** > **Save & Test** pour terminer la configuration du connecteur Fivetran.

Fivetran commencera à synchroniser les données de votre compte Braze vers votre entrepôt de données Snowflake. Vous pourrez accéder aux données de requête depuis Mozart Data une fois que le connecteur aura terminé la synchronisation.

### Synchronisation des données de Mozart Data vers Braze {#syncing-data-from-mozart-data-to-braze}

#### Étape 1 : Configurer un entrepôt de données Snowflake {#step-1-set-up-a-snowflake-data-warehouse}

Suivez les instructions relatives à l'[Ingestion de données cloud]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake) pour configurer une table, un utilisateur et des autorisations depuis l'interface Snowflake. Notez que cette étape nécessite un accès de niveau administrateur à Snowflake.

#### Étape 2 : Configurer votre intégration Snowflake dans Braze {#step-2-set-up-your-snowflake-integration-in-braze}

Après avoir configuré votre entrepôt Snowflake, dans Mozart Data, allez sur la page **Integration** et sélectionnez **Braze**. La vue d'intégration **Braze** affiche les identifiants à copier dans Braze.

![Page d'intégration Mozart Data avec Braze sélectionné et les identifiants de connexion Snowflake à utiliser dans Braze.]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

Ensuite, tout en étant connecté à Braze, allez dans **Integrations > Technology Partners > Snowflake** pour commencer le processus d'intégration. Copiez les identifiants depuis Mozart Data et ajoutez-les à la page d'importation de données Snowflake. Sélectionnez **Set up sync details** et saisissez les informations relatives à votre compte Snowflake et à votre table source.

![Formulaire d'intégration partenaire Snowflake dans Braze avec les champs compte, entrepôt, base de données et schéma renseignés à partir des identifiants Mozart Data.]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

Ensuite, sur l'écran de configuration d'importation Snowflake dans Braze, choisissez un nom pour votre synchronisation, fournissez les e-mails de contact et sélectionnez un type de données et une fréquence de synchronisation.

#### Étape 3 : Ajouter une clé publique à l'utilisateur Braze {#step-3-add-a-public-key-to-the-braze-user}
À ce stade, retournez dans Snowflake pour terminer la configuration. Ajoutez la clé publique affichée sur le tableau de bord de Braze à l'utilisateur que vous avez créé pour que Braze se connecte à Snowflake.

Pour plus d'informations sur la manière de procéder, consultez la [documentation de Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si vous souhaitez effectuer une rotation des clés, Mozart Data peut générer une nouvelle paire de clés et vous fournir la nouvelle clé publique.

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### Étape 4 : Tester la connexion {#step-4-test-connection}

Une fois l'utilisateur mis à jour avec la clé publique, retournez dans le tableau de bord de Braze et sélectionnez **Test connection**. Si l'opération réussit, un aperçu des données s'affiche. Si, pour une raison quelconque, la connexion échoue, un message d'erreur s'affiche pour vous aider à résoudre le problème.

![Résultat du test de connexion de l'intégration Snowflake dans Braze montrant un aperçu réussi après l'application de la clé publique.]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
Vous devez avoir testé une intégration avec succès avant qu'elle ne puisse passer de l'état Brouillon à l'état Actif. Si vous devez fermer la page de création, votre intégration sera sauvegardée et vous pourrez revenir à la page de détails pour effectuer des modifications et relancer les tests.
{% endalert %}

## Utiliser cette intégration {#using-this-integration}

### Comment accéder aux données de Braze en tant qu'utilisateur Mozart Data {#how-to-access-braze-data-as-a-mozart-data-user}
Après avoir créé avec succès un compte Mozart Data, vous pouvez accéder à vos données Braze synchronisées avec votre entrepôt de données Snowflake depuis Mozart Data.

#### Transformations {#transforms}
Mozart Data propose une couche de transformation SQL permettant aux utilisateurs de créer une vue ou une table. Vous pouvez créer une table de dimension au niveau de l'utilisateur (par exemple, `dim_users`) pour résumer les données d'utilisation du produit, l'historique des transactions et les activités d'engagement de chaque utilisateur avec les messages Braze.

#### Analyse {#analysis}
À l'aide des modèles de transformation ou des données brutes synchronisées depuis Braze, vous pouvez analyser l'engagement des utilisateurs vis-à-vis des messages de Braze. En outre, vous pouvez combiner les données de Braze avec d'autres données d'application et analyser comment les informations obtenues à partir de l'interaction des utilisateurs avec les messages de Braze sont liées à d'autres données que vous pourriez avoir sur les utilisateurs. Par exemple, leurs informations démographiques, l'historique de leurs achats, l'utilisation des produits et l'engagement du service client.

Cela peut vous aider à prendre des décisions plus éclairées sur les stratégies d'engagement afin d'améliorer la rétention des utilisateurs. Tout cela peut être fait dans l'interface de Mozart Data à l'aide de l'outil de requête, où vous pouvez exporter les résultats dans une feuille Google ou un fichier CSV pour préparer une présentation.

#### Aide à la décision (BI) {#business-intelligence-bi}
Vous êtes prêt à visualiser et à partager vos informations avec les autres membres de l'équipe ? Mozart Data s'intègre à presque tous les outils d'aide à la décision. Si vous ne disposez pas encore d'un outil de BI, contactez Mozart Data pour créer un compte Metabase gratuit.