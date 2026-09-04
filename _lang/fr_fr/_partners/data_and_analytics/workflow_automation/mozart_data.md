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
{% multi_lang_include partners/workflow_automation/mozart_data_integration_bullets.md %}

## Prérequis {#prerequisites}

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
| Compte Mozart Data | Un compte Mozart Data est requis pour profiter de ce partenariat. [Créez un compte Mozart Data](https://app.mozartdata.com/signup)|
| Compte Snowflake<br>Option 1 : Nouveau compte | Sélectionnez **Create a New Snowflake Account** lors du processus de création de votre compte Mozart Data pour que Mozart Data provisionne un nouveau compte Snowflake pour vous. |
| Compte Snowflake<br>Option 2 : Compte existant | Si votre organisation dispose déjà d'un compte Snowflake, vous pouvez utiliser l'option Mozart Data Connected.<br><br>Sélectionnez l'option **Already Have a Snowflake Account** pour connecter un compte Snowflake existant. Pour utiliser cette option, un utilisateur disposant d'autorisations au niveau du compte doit [suivre ces étapes](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

L'intégration prend en charge la synchronisation des données de [Braze vers Mozart Data](#syncing-data-from-braze-to-mozart-data) et de [Mozart Data vers Braze](#syncing-data-from-mozart-data-to-braze).

### Synchroniser les données de Braze vers Mozart Data {#syncing-data-from-braze-to-mozart-data}

#### Étape 1 : Configurer le connecteur Braze {#step-1-set-up-braze-connector}

1. Dans Mozart Data, accédez à **Connectors** et sélectionnez **Add Connector**.
2. Recherchez « Braze » et sélectionnez la carte du connecteur.
3. Saisissez un nom de schéma de destination dans lequel toutes les données synchronisées depuis Braze seront stockées. Nous recommandons d'utiliser le nom de schéma par défaut `braze`.
4. Sélectionnez **Add Connector**.

#### Étape 2 : Remplir le formulaire du connecteur Fivetran {#step-2-fill-out-the-fivetran-connector-form}

La page du connecteur Fivetran s'ouvre une fois l'étape 1 terminée. Remplissez les champs indiqués, puis sélectionnez **Continue** > **Save & Test** pour finaliser le connecteur Fivetran.

Fivetran commence à synchroniser les données de votre compte Braze vers votre entrepôt de données Snowflake. Vous pouvez accéder aux données de requête depuis Mozart Data une fois que le connecteur a terminé la synchronisation.

### Synchroniser les données de Mozart Data vers Braze {#syncing-data-from-mozart-data-to-braze}

#### Étape 1 : Configurer un entrepôt de données Snowflake {#step-1-set-up-a-snowflake-data-warehouse}

Suivez les instructions d'[ingestion de données cloud]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake) pour configurer une table, un utilisateur et des permissions depuis l'interface Snowflake. Notez que cette étape nécessite un accès Snowflake de niveau administrateur.

#### Étape 2 : Configurer votre intégration Snowflake dans Braze {#step-2-set-up-your-snowflake-integration-in-braze}

Après avoir configuré votre entrepôt Snowflake, dans Mozart Data, accédez à la page **Integration** et sélectionnez **Braze**. La vue d'intégration **Braze** affiche les identifiants à copier dans Braze.

![Page d'intégration Mozart Data avec Braze sélectionné et les identifiants de connexion Snowflake à utiliser dans Braze.]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

Ensuite, une fois connecté à Braze, accédez à **Intégrations > Partenaires technologiques > Snowflake** pour lancer le processus d'intégration. Copiez les identifiants depuis Mozart Data et ajoutez-les à la page d'importation de données Snowflake. Sélectionnez **Set up sync details** et saisissez les informations de votre compte Snowflake et de votre table source.

![Formulaire d'intégration partenaire Snowflake dans Braze avec les champs compte, entrepôt, base de données et schéma remplis à partir des identifiants Mozart Data.]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

Ensuite, choisissez un nom pour votre synchronisation, fournissez des adresses e-mail de contact, puis sélectionnez un type de données et une fréquence de synchronisation sur l'écran de configuration d'importation Snowflake de Braze.

#### Étape 3 : Ajouter une clé publique à l'utilisateur Braze {#step-3-add-a-public-key-to-the-braze-user}
À ce stade, retournez dans Snowflake pour terminer la configuration. Ajoutez la clé publique affichée sur le tableau de bord de Braze à l'utilisateur que vous avez créé pour permettre à Braze de se connecter à Snowflake.

Pour plus d'informations sur la marche à suivre, consultez la [documentation Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si vous souhaitez effectuer une rotation des clés à tout moment, Mozart Data peut générer une nouvelle paire de clés et vous fournir la nouvelle clé publique.

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### Étape 4 : Tester la connexion {#step-4-test-connection}

Une fois l'utilisateur mis à jour avec la clé publique, retournez sur le tableau de bord de Braze et sélectionnez **Test connection**. En cas de succès, vous verrez un aperçu des données. Si, pour une raison quelconque, la connexion échoue, un message d'erreur s'affichera pour vous aider à résoudre le problème.

![Résultat du test de connexion de l'intégration Snowflake dans Braze montrant un aperçu réussi après l'application de la clé publique.]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
Vous devez tester une intégration avec succès avant de pouvoir la faire passer de l'état Brouillon à l'état Actif. Si vous devez quitter la page de création, votre intégration sera enregistrée et vous pourrez revenir à la page de détails pour apporter des modifications et effectuer le test.
{% endalert %}

## Utiliser cette intégration {#using-this-integration}

### Comment accéder aux données Braze en tant qu'utilisateur de Mozart Data {#how-to-access-braze-data-as-a-mozart-data-user}
Une fois votre compte Mozart Data créé avec succès, vous pouvez accéder à vos données Braze synchronisées avec votre entrepôt de données Snowflake depuis Mozart Data.

#### Transformations {#transforms}
Mozart Data propose une couche de transformation SQL permettant aux utilisateurs de créer une vue ou une table. Vous pouvez créer une table de dimensions au niveau utilisateur (par exemple, `dim_users`) pour résumer les données d'utilisation produit, l'historique transactionnel et les activités d'engagement avec les messages Braze de chaque utilisateur.

#### Analyse {#analysis}
En utilisant les modèles de transformation ou les données brutes synchronisées depuis Braze, vous pouvez analyser l'engagement des utilisateurs avec les messages Braze. De plus, vous pouvez combiner les données Braze avec d'autres données applicatives et analyser comment les informations tirées des interactions des utilisateurs avec les messages Braze sont liées aux autres données dont vous disposez sur ces utilisateurs. Par exemple, leurs informations démographiques, leur historique d'achats, leur utilisation du produit et leur engagement avec le service client.

Cela peut vous aider à prendre des décisions plus éclairées concernant les stratégies d'engagement afin d'améliorer la rétention des utilisateurs. Tout cela peut être réalisé depuis l'interface de Mozart Data à l'aide de l'outil Query, où vous pouvez exporter les résultats dans un Google Sheet ou un CSV pour préparer une présentation.

#### Aide à la décision (BI) {#business-intelligence-bi}
Prêt à visualiser et partager vos informations avec les autres membres de votre équipe ? Mozart Data s'intègre avec la quasi-totalité des outils de BI. Si vous ne disposez pas encore d'un outil de BI, contactez Mozart Data pour configurer un compte Metabase gratuit.