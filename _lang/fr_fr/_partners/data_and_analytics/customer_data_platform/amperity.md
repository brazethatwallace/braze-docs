---
nav_title: Amperity
article_title: Amperity
alias: /partners/amperity/
description: "Cet article de référence décrit le partenariat entre Braze et Amperity, une plateforme de données client complète pour les entreprises, vous permettant de synchroniser les utilisateurs d'Amperity, d'unifier les données, d'envoyer des données en utilisant des compartiments AWS S3 vers Braze, et plus encore."
page_type: partner
search_tag: Partner

---

# Amperity

> [Amperity](https://amperity.com/) est une plateforme de données client complète pour les entreprises, aidant les marques à mieux connaître leurs clients, à prendre des décisions stratégiques et à adopter systématiquement la bonne démarche pour mieux servir leurs consommateurs. Amperity fournit des capacités intelligentes dans l'unification de la gestion des données, l'analytique, les informations et l'activation.

_Cette intégration est maintenue par Amperity._

{% multi_lang_include video.html id="06G0lxaSjgk" align="right" %}

L'intégration de Braze et Amperity offre une vue unifiée de vos clients sur les deux plateformes. Cette intégration vous permet de :
- **Synchroniser les profils clients** : Mapper les données utilisateur et les attributs personnalisés d'Amperity vers Braze.
- **Créer et envoyer des audiences** : Créer des segments qui renvoient des listes de clients actifs et leurs attributs personnalisés associés vers Braze, et les envoyer à Braze.
- **Gérer les mises à jour des données** : Contrôler la fréquence d'envoi des mises à jour des attributs personnalisés vers Braze.
- **Unifier les données** : Unifier les données sur diverses plateformes prises en charge par Amperity et Braze.
- **Synchroniser les données de Braze vers Amazon S3** : Utiliser Braze Currents pour intégrer les données d'engagement des campagnes Braze, vous permettant de synchroniser les données vers Amazon S3 au format Apache Avro.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Amperity | Un [compte Amperity](https://amperity.com/request-a-demo) est requis pour profiter de ce partenariat. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations `users.track`. <br> Elle peut être créée dans le tableau de bord de Braze en accédant à **Console de développement** > **Clé API REST** > **Créer une nouvelle clé API**. |
| Instance Braze | Votre instance Braze peut être obtenue auprès de votre gestionnaire d'onboarding Braze ou sur la [page d'aperçu de l'API]({{site.baseurl}}/api/basics/#endpoints). |
| Endpoint REST Braze | Votre URL d'endpoint Braze. Votre endpoint dépendra de votre instance Braze. |
| Connecteur Currents (facultatif) | Le connecteur S3 Currents. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Mappage des données {#data-mapping}

Les attributs standard et personnalisés peuvent être envoyés d'Amperity vers Braze, vous permettant d'enrichir les profils clients dans Braze avec des données provenant de diverses sources via Amperity. Les attributs spécifiques que vous pouvez envoyer dépendront des données dans votre système Amperity et des attributs que vous avez configurés dans Braze.

Lisez ci-dessous pour en savoir plus sur ces attributs.

### Attributs standard {#standard-attributes}

Les [attributs de profil]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) décrivent qui sont vos clients. Ils sont souvent associés à l'identité du client, tels que :
- Noms
- Dates de naissance
- Adresses e-mail
- Numéros de téléphone

### Attributs personnalisés {#custom-attributes}

Les [attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) dans Braze sont des champs déterminés par votre marque. Si vous souhaitez qu'Amperity gère des attributs personnalisés qui existent déjà dans Braze, alignez la sortie envoyée par Amperity avec les noms déjà présents dans votre espace de travail Braze. Cela peut inclure les éléments suivants :
- Historiques d'achats
- Statut de fidélité
- Niveaux de valeur
- Données d'engagement récentes

Vérifiez les noms des attributs personnalisés qui seront envoyés à Braze depuis Amperity. Amperity ajoutera un attribut personnalisé chaque fois qu'il n'y aura pas de nom correspondant.

Les attributs personnalisés ne seront mis à jour que pour les utilisateurs ayant un `external_id` ou un `braze_id` correspondant dans Braze.

### Audiences Amperity {#amperity-audiences}

Les audiences synchronisées d'Amperity vers Braze seront enregistrées dans les profils utilisateurs en tant qu'attributs personnalisés. Elles peuvent ensuite être utilisées pour cibler ces utilisateurs dans Braze.

![Liste déroulante de filtres avec des attributs personnalisés affichés dans la catégorie de données personnalisées.]({% image_buster /assets/img/amperity/custom_attributes_filters.png %}){: style="max-width:60%;"}

![Liste déroulante d'attributs personnalisés tels que « l12m_frequency » et « l12m_monetary ».]({% image_buster /assets/img/amperity/search_custom_attributes_filters.png %}){: style="max-width:40%;"}

### Types de données {#data-types}

Les types de données pris en charge incluent :
- Valeur booléenne
- Date
- Date et heure
- Décimal
- Float
- Entier
- Chaîne de caractères
- Varchar

Le type de données utilisé dépend de la nature de l'attribut. Par exemple, une adresse e-mail serait une chaîne de caractères, tandis que l'âge d'un client pourrait être un entier.

### Duplication des attributs {#duplication-of-attributes}

Évitez d'envoyer des attributs personnalisés qui dupliquent les champs de profil utilisateur par défaut. Par exemple, les dates de naissance doivent être envoyées à Braze sous la forme d'un champ de profil utilisateur nommé « dob » pour correspondre à l'attribut standard de Braze. S'ils sont envoyés comme « birthday », « Birthdate » ou toute autre chaîne de caractères, un attribut personnalisé sera créé, et les valeurs dans le champ « dob » ne seront pas mises à jour.

### Points de données {#data-points}

Amperity suit les changements entre les synchronisations avec Braze et l'état des envois dans l'ensemble. Amperity n'enverra à Braze que l'appartenance à la liste et les autres attributs choisis qui ont changé depuis la dernière synchronisation.

## Intégration {#integration}

### Étape 1 : Capturer les détails de configuration de Braze {#step-1-capture-configuration-details-for-braze}

1. Créez une clé API REST Braze pour votre espace de travail Braze avec les autorisations `users.track` sous **User Data**. L'endpoint `users.track` synchronise l'audience Amperity avec Braze en tant qu'attribut personnalisé.
2. Déterminez l'[endpoint de la REST API]({{site.baseurl}}/api/basics/#endpoints) pour votre instance Braze. Par exemple, si votre URL Braze est `https://dashboard-03.braze.com`, votre endpoint REST API est `https://rest.iad-03.braze.com` et votre instance est « US-03 ».
3. Déterminez une liste de [champs de profil utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) et d'[attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) qui peuvent être envoyés à Braze depuis Amperity.

### Étape 2 : Configurer Braze en tant que destination — Opérateur DataGrid {#step-2-set-up-braze-as-a-destinationdatagrid-operator}

#### Étape 2a : Créer la table des profils clients {#step-2a-build-the-customer-profiles-table}

Créez une nouvelle table nommée « Braze Customer Attributes » dans votre base de données Customer 360 dans Amperity. Cette table doit contenir tous les attributs de Braze que votre marque souhaite gérer depuis Amperity, y compris les champs de profil utilisateur par défaut requis par Braze et tous les attributs personnalisés. Utilisez SQL pour définir la structure de cette table comme indiqué dans [la documentation Amperity](https://docs.amperity.com/datagrid/destination_braze.html#customer-profiles-table).

#### Étape 2b : Nommer, valider et enregistrer la table {#step-2b-name-validate-and-save-the-table}

Nommez la table « Braze Customer Attributes » et enregistrez-la. Vérifiez que la table est accessible à l'**éditeur de segments** et à l'éditeur **Modifier les attributs** dans les campagnes.

#### Étape 2c : Ajouter Braze comme destination {#step-2c-add-braze-as-a-destination}

Dans la plateforme Amperity, accédez à l'onglet **Destinations**. Cherchez l'option pour ajouter une nouvelle destination. Parmi les options disponibles, sélectionnez **Braze**.

![La section Nouvelle destination avec un nom « Braze API », une description « Send audience attributes to Braze. » et un plugin « Braze ».]({% image_buster /assets/img/amperity/destination_name.png %}){: style="max-width:60%;"}

#### Étape 2d : Configurer les détails de la destination {#step-2d-configure-destination-details}

Sous **Braze settings**, fournissez les identifiants Braze et les paramètres de destination, comme indiqué dans [la documentation Amperity](https://docs.amperity.com/datagrid/destination_braze.html#add-destination). Saisissez les détails de configuration collectés à l'étape précédente et définissez l'identifiant Braze. Les identifiants disponibles pour la correspondance sont :
- `braze_id` : un identifiant Braze attribué automatiquement qui est immuable et associé à un utilisateur particulier lorsqu'il est créé dans Braze.
- `external_id` : un identifiant attribué par le client, généralement un UUID.

![La section Braze settings avec une instance « US-03 », un identifiant utilisateur « external_id », un nom de segment vide, un compartiment S3 « amperity-training-abc123 » et un dossier S3 « braze-attributes ».]({% image_buster /assets/img/amperity/braze_settings.png %}){: style="max-width:60%;"}

#### Étape 2e : Ajouter un modèle de données {#step-2e-add-a-data-template}

Dans l'onglet **Destinations**, ouvrez le menu pour la destination Braze et sélectionnez **Add data template**. Entrez un nom et une description pour le modèle (par exemple, « Braze » et « Send custom attributes to Braze »), vérifiez l'accès utilisateur et vérifiez tous les paramètres de configuration.

Si des paramètres requis n'ont pas été configurés dans le cadre de la destination, configurez-les dans le cadre du modèle de données. Enregistrez le modèle de données.

![La section Nom du modèle de données avec le nom « Braze Audience Attributes » et la description « Send audience attributes to Braze. »]({% image_buster /assets/img/amperity/data_template_name.png %}){: style="max-width:60%;"}

#### Étape 2f : Enregistrer la configuration {#step-2f-save-the-configuration}

Après avoir rempli les détails nécessaires, enregistrez la configuration. Maintenant que Braze est configuré comme destination, les utilisateurs d'Amp360 et d'AmpIQ peuvent synchroniser des données vers Braze.

### Étape 3 : Synchroniser les données avec Braze {#step-3-sync-data-to-braze}

Assurez-vous que Braze est activé pour votre locataire Amperity. Si ce n'est pas le cas, contactez votre opérateur DataGrid ou votre conseiller Amperity pour obtenir de l'aide.

Ensuite, suivez les instructions de synchronisation pour Amp360 ou AmpIQ, selon ce qui est applicable à votre entreprise.

#### Option de synchronisation 1 : Envoyer les résultats de la requête à Braze via Amp360 {#syncing-option-1-send-query-results-to-braze-via-amp360}

Les utilisateurs d'Amp360 peuvent utiliser SQL pour écrire des requêtes libres, puis configurer une planification qui envoie les résultats à Braze.

##### Étape 1 : Créer une requête dans Amperity {#step-1-create-a-query-in-amperity}

Accédez à la fonction de requête dans Amperity et construisez une requête SQL qui produira l'ensemble de données client souhaité. Les résultats doivent inclure les attributs spécifiques que vous souhaitez envoyer à Braze. Consultez cet exemple de requête Amperity pour renvoyer une liste d'utilisateurs avec leurs historiques d'achats.

##### Étape 2 : Ajouter une nouvelle orchestration dans Amperity {#step-2-add-a-new-orchestration-in-amperity}

1. Accédez à la section **Orchestration** et cliquez sur l'option pour ajouter une nouvelle orchestration.
2. Spécifiez ce que l'orchestration doit faire. Cela implique généralement de spécifier la requête SQL qui doit être exécutée et où les résultats doivent être envoyés. Dans ce cas, sélectionnez la requête SQL que vous avez créée pour générer la liste des clients actifs et spécifiez Braze comme destination pour les résultats.
3. Définissez quand et à quelle fréquence l'orchestration doit s'exécuter. Par exemple, vous pouvez exécuter l'orchestration quotidiennement à une heure précise.
4. Enregistrez l'orchestration après l'avoir configurée à votre convenance. Elle sera ajoutée à votre liste d'orchestrations dans Amperity.
5. Testez l'orchestration pour vous assurer qu'elle fonctionne comme prévu. Vous pouvez le faire en déclenchant manuellement l'orchestration et en vérifiant les résultats dans Braze.

##### Étape 3 : Exécuter l'orchestration {#step-3-run-the-orchestration}

Exécutez l'orchestration pour lancer la requête et envoyer les résultats à Braze. Cela peut être fait manuellement ou selon la planification que vous avez définie dans les paramètres d'orchestration.

#### Option de synchronisation 2 : Envoyer des audiences à Braze via AmpIQ {#syncing-option-2-send-audiences-to-braze-via-ampiq}

Les utilisateurs d'AmpIQ peuvent créer des segments dans Amperity via une interface non-SQL et les synchroniser vers des destinations en aval telles que Braze. Les utilisateurs peuvent sélectionner des destinations, puis configurer une liste d'attributs à envoyer à chaque destination.

##### Étape 1 : Créer un segment dans Amperity {#step-1-create-a-segment-in-amperity}

Créez un segment dans Amperity qui renvoie une liste de clients. Ce segment doit être associé aux attributs personnalisés que vous souhaitez mettre à jour dans Braze.

{% alert note %}
Consultez la documentation d'Amperity pour des exemples de différents types de segments que vous pourriez vouloir envoyer à Braze.
{% endalert %}

##### Étape 2 : Créer une campagne dans Amperity {#step-2-build-a-campaign-in-amperity}

1. Accédez à la section **Campaign** et cliquez sur l'option pour créer une nouvelle campagne.
2. Donnez à votre campagne un nom descriptif et unique qui vous aidera à l'identifier plus tard, surtout si vous avez plusieurs campagnes.
3. Sélectionnez le segment de clients que vous souhaitez cibler avec cette campagne. Il doit s'agir du segment que vous avez créé précédemment. <br>![Le champ déroulant pour les segments à exclure du ciblage.]({% image_buster /assets/img/amperity/select_segments.png %}){: style="max-width:50%;"}<br><br>
4. Choisissez les données que vous souhaitez envoyer dans le cadre de la campagne. Cela peut inclure une gamme d'attributs client. ![La fenêtre modale Edit Campaign Attributes permet de sélectionner une destination et des attributs client.]({% image_buster /assets/img/amperity/edit_campaign_attributes.png %}){: style="max-width:90%;"}<br><br>
5. Sélectionnez **Braze** comme destination où les données de la campagne seront envoyées.
6. Choisissez quand et à quelle fréquence vous souhaitez que la campagne s'exécute. Cela peut être un événement unique ou une planification récurrente.
7. Enregistrez votre campagne et exécutez un test pour vous assurer qu'elle fonctionne comme prévu.

##### Étape 3 : Lancer la campagne {#step-3-run-the-campaign}

Exécutez la campagne pour envoyer le segment à Braze. Cela peut être fait manuellement ou en fonction de la planification que vous avez définie dans les paramètres de la campagne.


### Utilisation d'Amperity avec Braze Currents {#using-amperity-with-braze-currents}
Pour envoyer des données Braze Currents dans Amperity :
1. [Configurez un Braze Current]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/) pour envoyer des données vers un compartiment Amazon S3.
2. Configurez Amperity pour [lire les fichiers Apache Avro depuis ce compartiment Amazon S3](https://docs.amperity.com/datagrid/source_amazon_s3.html).
3. Configurez les flux et automatisez les chargements de données en utilisant des flux de travail standard.