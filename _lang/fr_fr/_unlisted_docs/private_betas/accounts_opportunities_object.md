---
nav_title: Objets de compte
article_title: Objets de compte
page_type: reference
permalink: /account_object/
hidden: true
description: "Découvrez comment utiliser les objets de compte pour créer des segments d'utilisateurs en fonction du compte auquel ils appartiennent, puis envoyer des messages personnalisés à l'aide d'étiquettes Liquid."
---

# Objets de compte {#account-objects}

> Découvrez comment utiliser les objets de compte pour créer des segments d'utilisateurs en fonction du compte auquel ils appartiennent, puis envoyer des messages personnalisés à l'aide d'étiquettes Liquid.

Pour importer des données de compte, utilisez un [fichier CSV](#using-a-csv-file) ou l'API Braze. Avec l'API Braze, vous pouvez [créer plusieurs comptes](#create-multiple-accounts), [créer un seul compte](#create-one-account), [supprimer plusieurs comptes](#delete-multiple-accounts) et [supprimer un seul compte](#delete-one-account).

| Audience | Comment vous utiliserez cet article |
|----------|----------------------------|
| Marketeurs | Importez des données d'utilisateurs et de comptes via CSV, créez des segments basés sur les attributs de compte et personnalisez les messages avec les informations de compte dans Braze. |
| Développeurs | Utilisez la REST API Braze pour créer, mettre à jour et supprimer des enregistrements de compte de manière programmatique et maintenir Braze synchronisé avec vos données. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Les objets de compte sont actuellement en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cette bêta.
{% endalert %}

## Fonctionnement {#how-it-works}

Les objets de compte sont des structures de données personnalisées qui représentent l'entreprise d'un utilisateur. Ils se connectent aux profils utilisateur, ce qui vous permet de créer des Segments de type B2B et de personnaliser les messages. Utilisez les champs de compte tels que le nom de l'entreprise, le secteur d'activité, le rôle ou le statut de l'opportunité avec les catalogues Braze, les filtres de segmentation et les étiquettes Liquid.

Par exemple, vous pouvez cibler les utilisateurs qui travaillent dans le secteur de la santé et envoyer des messages personnalisés aux médecins et aux administrateurs hospitaliers pour rendre votre message encore plus pertinent.

Pour utiliser les objets de compte, vous importez trois types de données dans Braze :

- **Données utilisateur :** les profils utilisateur individuels utilisés pour identifier chaque personne dans Braze (par exemple, via `external_id`, e-mail, téléphone ou alias d'utilisateur). Importez les données utilisateur via CSV.
- **Données de relation utilisateur-compte :** la relation entre un utilisateur et un compte, y compris l'entreprise à laquelle il appartient et le rôle qu'il occupe dans ce compte. Importez ces données de relation via CSV.
- **Données de compte :** les enregistrements de l'entreprise eux-mêmes, tels que le nom de l'entreprise, le secteur d'activité, le chiffre d'affaires annuel et d'autres détails firmographiques. Ce sont les enregistrements que vous ciblez et contre lesquels vous personnalisez dans les Segments et les messages. Importez les données de compte via CSV ou la REST API Braze.

Ces trois types de données doivent être importés pour que les objets de compte fonctionnent. Les données utilisateur identifient les personnes dans Braze, les données de relation utilisateur-compte connectent ces utilisateurs à des comptes et des rôles spécifiques, et les données de compte fournissent les attributs au niveau de l'entreprise utilisés pour la segmentation et la personnalisation.

## Prérequis {#prerequisites}

Avant de pouvoir utiliser cette fonctionnalité, vous devez déjà avoir des utilisateurs dans Braze.

## Importer des données dans Braze {#import-data-to-braze}

Pour utiliser les objets de compte dans vos messages, vos données utilisateur doivent déjà exister dans Braze. À partir de là, effectuez deux imports : d'abord, importez les données de relation utilisateur-compte pour établir les associations de comptes et les rôles (actuellement via CSV uniquement). Ensuite, importez les données de compte avec les détails au niveau de l'entreprise utilisés pour la segmentation et la personnalisation (via CSV ou la REST API de Braze).

### Étape 1 : Importer les données de relation utilisateur-compte {#step-1-import-user-account-relationship-data}

Commencez par importer vos données de relation utilisateur-compte dans Braze sous forme de fichier CSV avec les champs suivants. Cela aide Braze à associer les utilisateurs existants aux comptes et rôles appropriés.

<style>
table td {
    word-break: break-word;
}
</style>

| Nom du champ     | Type de champ | Obligatoire | Description                                                                                           |
|------------------|---------------|-------------|-------------------------------------------------------------------------------------------------------|
| `account_id`       | String     | Oui      | Le compte auquel l'utilisateur appartient. Il s'agit du même champ que le champ `id` de l'objet de compte (ID CRM). |
| `external_id`      | String     | Oui      | L'[ID externe](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle/#identified-user-profiles) de l'utilisateur dans Braze. |
| `user_alias_name`  | String     | Non*      | Le [nom d'alias](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle#user-aliases) de l'utilisateur dans Braze. |
| `user_alias_label` | String     | Non*      | Le [libellé d'alias](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle/#what-happens-when-you-identify-anonymous-users) de l'utilisateur dans Braze. |
| `email`            | String     | Non*     | L'adresse e-mail de l'utilisateur. |
| `phone`            | String     | Non*      | Le numéro de téléphone de l'utilisateur. |
| `user_role`             | String     | Non       | Le rôle de l'utilisateur au sein du compte, par exemple « directory » ou « employee ». |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }
<sup>Un des champs `external_id`, `email`, `phone` ou `user_alias` est requis pour identifier un utilisateur.</sup>

#### Utiliser un fichier CSV {#using-a-csv-file}

Chargez votre CSV contenant les relations utilisateur-compte dans Braze :

1. Accédez à **Data Settings** > **Accounts**.
2. Sélectionnez **Update data**.
3. Sous **CSV upload**, sélectionnez **Users**, puis chargez votre fichier dans Braze.

![Le menu déroulant « Upload data » sur la page « Accounts » dans Braze.]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/update_account_data_csv.png %})

### Étape 2 : Importer les données de compte {#step-2-import-account-data}

Les comptes sont les entreprises auxquelles vos utilisateurs appartiennent. Importez vos données de compte dans Braze sous forme de fichier CSV avec les champs suivants. Gardez à l'esprit que chaque compte doit se voir attribuer un ID et un nom.

<style>
table td {
    word-break: break-word;
}
</style>

| Nom du champ                  | Type de champ | Obligatoire | Description                                                                        |
|-----------------------------|--------------|----------|------------------------------------------------------------------------------------|
| `id`                          | String     | Oui      | L'ID du compte dans votre plateforme de gestion de la relation client (CRM). |
| `name`                        | String     | Oui      | Le nom du compte.                                                                |
| `type`                        | String     | Non       | Le type de compte, par exemple client, partenaire ou revendeur.                                                                                   |
| `annual_revenue`              | String     | Non       | Le chiffre d'affaires annuel du compte.                                                      |
| `industry`                    | String     | Non       | Le secteur d'activité dans lequel le compte opère.                                             |
| `number_of_employees`         | String     | Non       | Le nombre d'employés, prend en charge les plages.                                           |
| `address`                     | String     | Non       | L'adresse postale du compte.                                                      |
| `city`                        | String     | Non       | La ville où se trouve le compte.                                                  |
| `state`                       | String     | Non       | L'état ou la région où se trouve le compte.                                                 |
| `postal_code`                 | String     | Non       | Le code postal de l'adresse du compte.                                              |
| `country`                     | String     | Non       | Le pays où se trouve le compte.                                               |
| `notes`                       | String     | Non       | Notes supplémentaires concernant le compte.                                                 |
| `website`                     | String     | Non       | L'URL du site web du compte.                                                        |
| `main_phone`                  | String     | Non       | Le numéro de téléphone principal du compte.                                                  |
| `created_date`                | Time       | Non       | La date de création du compte.                                                  |
| `account_owner_email_address` | String     | Non       | Un propriétaire de compte interne (par exemple « Tom de l'équipe commerciale de l'entreprise A gère l'entreprise B »).      |
| `parent_account_id`           | String     | Non       | L'ID du compte parent, le cas échéant (par exemple un lien vers l'ID de la société mère). |
| `sic_code`                    | String     | Non       | Le code de classification industrielle standard.                                              |
| Champs personnalisés                 | N/A        | Non       | Champs personnalisés définis et gérés par vous.                                                             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }
{% alert note %}
Bien que certains champs soient facultatifs, incluez-les dans la mesure du possible, car ce sont des noms de champs réservés qui aident à garder vos données organisées.
{% endalert %}

Ensuite, importez vos données de compte dans Braze en chargeant un fichier CSV ou en utilisant la REST API de Braze. Vous pouvez consulter ces données dans **Data Settings**. Vous ne pouvez pas modifier ces données dans l'éditeur intégré au navigateur.

#### Utiliser un fichier CSV

Pour importer vos données via CSV :

1. Accédez à **Data Settings** > **Accounts**.
2. Sélectionnez **Update data**.
3. Sous **CSV upload**, sélectionnez **Account Data**, puis chargez votre fichier dans Braze.

![Le menu déroulant « Upload data » sur la page « Accounts » dans Braze.]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/update_account_data_csv.png %})

### Résolution des problèmes d'import CSV {#troubleshooting-csv-imports}

#### Lignes vides dans les imports CSV d'objets de compte {#empty-rows-in-account-objects-csv-imports}

Si vous importez des données d'objets de compte et que vous constatez des lignes vides sur la page **Accounts**, vérifiez si les valeurs des champs de compte contiennent des virgules.

Dans les imports CSV d'objets de compte, les virgules dans les valeurs peuvent être interprétées comme des séparateurs. Cela peut entraîner une analyse incorrecte des valeurs et générer des lignes vides sur le tableau de bord.

Pour résoudre ce problème, supprimez les virgules du fichier CSV d'origine et chargez-le à nouveau. Par exemple, remplacez `"$5,000,000"` par `"$5000000"` ou `"$5 million"` avant de recharger le fichier.

## Utiliser l'API Braze {#using-the-braze-api}

Les API (interfaces de programmation d'applications) permettent à différents systèmes logiciels de communiquer de manière programmatique. Lorsque vous interagissez avec l'API Braze, vous envoyez des requêtes HTTP à des endpoints spécifiques. Les endpoints sont des URL structurées qui acceptent des instructions et renvoient des réponses. La méthode HTTP indique à Braze quelle action effectuer, et le corps de la requête contient les données.

Pour la gestion des comptes, l'API Braze utilise ces méthodes HTTP :

| Méthode | Objectif | Comportement |
|--------|---------|----------|
| `PUT` | Créer ou mettre à jour des ressources | Ajoute un nouvel enregistrement de compte s'il n'en existe pas. Met à jour l'enregistrement existant s'il en existe un. `PUT` est conçu pour être idempotent, vous pouvez donc synchroniser les mêmes données plusieurs fois sans créer de doublons. |
| `DELETE` | Supprimer des ressources | Supprime définitivement l'enregistrement de compte spécifié et ses associations de Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

L'API Braze vous donne un contrôle programmatique sur les données de compte à grande échelle. Vous pouvez automatiser les workflows de gestion des comptes, synchroniser les informations de compte directement depuis vos sources de données et maintenir Braze aligné avec votre source de vérité sans téléchargements ni modifications manuels. Cela contribue à réduire la charge opérationnelle et à maintenir des données de compte précises et à jour pour la segmentation et la personnalisation.

Pour plus d'informations sur les méthodes HTTP et le fonctionnement des API REST, consultez les ressources suivantes :
- [Méthodes de requête HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods) sur MDN Web Docs
- [Tutoriel REST API](https://restapitutorial.com/)
- [Aperçu de l'API Braze]({{site.baseurl}}/api/basics)

{% alert note %}
Utilisez une clé API avec les autorisations de catalogues pour authentifier les requêtes vers l'endpoint `/business/accounts`.
{% endalert %}

Cette section explique comment utiliser l'API Braze pour :
- [Créer plusieurs comptes](#create-multiple-accounts)
- [Créer un seul compte](#create-one-account)
- [Supprimer plusieurs comptes](#delete-multiple-accounts)
- [Supprimer un seul compte](#delete-one-account)

### Créer plusieurs comptes {#create-multiple-accounts}

Comme `PUT` est idempotent, vous pouvez envoyer la même requête plusieurs fois et Braze met à jour les enregistrements existants plutôt que de créer des doublons. Cela en fait un choix fiable pour maintenir les enregistrements de compte à jour dans Braze.

L'extrait de code suivant envoie une requête `PUT` à l'endpoint `/business/accounts`. Le tableau `accounts` contient plusieurs objets d'entreprise, chacun mappé aux champs de compte définis dans [Étape 2 : Importer les données de compte](#step-2-import-account-data). Braze traite chaque objet et crée ou met à jour l'enregistrement correspondant dans votre page **Accounts**. Cette opération est asynchrone. Braze met la requête en file d'attente et la traite en arrière-plan, ce qui la rend adaptée aux importations en masse où une confirmation immédiate n'est pas nécessaire.

Pour créer plusieurs comptes, envoyez une requête `PUT` à `/business/accounts`. Si un compte n'existe pas, Braze ajoute un nouvel élément dans la page **Accounts**. Chaque requête peut prendre en charge jusqu'à 50 comptes. Notez que cette opération est asynchrone.

Votre requête devrait ressembler à ceci :

```plaintext
curl -X PUT https://YOUR_REST_API_URL/business/accounts \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
          "accounts": [
              {
                  "id": "ACC001",
                  "name": "Acme Corporation",
                  "type": "Customer",
                  "annual_revenue": "$5,000,000",
                  "industry": "Manufacturing",
                  "number_of_employees": "150",
                  "address": "123 Industrial Way",
                  "city": "Metropolis",
                  "state": "NY",
                  "postal_code": "10001",
                  "country": "USA",
                  "notes": "Key client in the manufacturing sector",
                  "website": "http://www.acme.com",
                  "main_phone": "+1-212-555-1234",
                  "created_date": "2023-01-15T09:30:00Z",
                  "account_owner_email_address": "owner@example.com",
                  "parent_account_id": "",
                  "sic_code": "2011"
              },
              {
                  "id": "ACC002",
                  "name": "Global Solutions",
                  "type": "Partner",
                  "annual_revenue": "$10,000,000",
                  "industry": "Technology",
                  "number_of_employees": "500",
                  "address": "456 Tech Park",
                  "city": "Silicon Valley",
                  "state": "CA",
                  "postal_code": "94043",
                  "country": "USA",
                  "notes": "Important partner for software solutions",
                  "website": "http://www.globalsolutions.com",
                  "main_phone": "+1-650-555-5678",
                  "created_date": "2023-02-20T14:45:00Z",
                  "account_owner_email_address": "partner@example.com",
                  "parent_account_id": "ACC001",
                  "sic_code": "7372"
              },
              {
                  "id": "ACC003",
                  "name": "Oceanic Ventures",
                  "type": "Customer",
                  "annual_revenue": "$3,200,000",
                  "industry": "Retail",
                  "number_of_employees": "75",
                  "address": "789 Ocean Blvd",
                  "city": "Miami",
                  "state": "FL",
                  "postal_code": "33101",
                  "country": "USA",
                  "notes": "Expanding presence in retail markets",
                  "website": "http://www.oceanicventures.com",
                  "main_phone": "+1-305-555-6789",
                  "created_date": "2023-03-05T08:15:00Z",
                  "account_owner_email_address": "contact@example.com",
                  "parent_account_id": "",
                  "sic_code": "5941"
              }
          ]
      }'
```

### Créer un seul compte {#create-one-account}

Comme pour la création de plusieurs comptes, cette opération utilise la méthode `PUT`. La différence est que l'ID du compte est inclus directement dans l'URL de l'endpoint plutôt que dans le corps de la requête. Cela vous donne un contrôle précis sur un seul enregistrement.

L'extrait de code suivant envoie une requête `PUT` à `/business/accounts/ACC001`, où `ACC001` est l'identifiant unique du compte. Cette opération est synchrone. Braze traite la requête immédiatement et renvoie une réponse dès qu'elle est terminée. Cela convient bien aux intégrations en temps réel. Par exemple, lorsque les informations d'un compte changent dans votre système, vous pouvez refléter cette mise à jour dans Braze immédiatement pour le ciblage ou la personnalisation.

Pour créer un seul compte, envoyez une requête `PUT` à `/business/accounts/:account_id`. Si le compte n'existe pas, Braze crée un nouvel enregistrement de compte. Cette opération est synchrone.

Votre requête devrait ressembler à ceci :

```plaintext
curl -X PUT https://YOUR_REST_API_URL/business/accounts/ACC001 \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
        "accounts": [
            {
                "name": "Braze",
                "type": "Customer",
                "annual_revenue": "$5,000,000",
                "industry": "Manufacturing",
                "number_of_employees": "150",
                "address": "123 Industrial Way",
                "city": "Metropolis",
                "state": "NY",
                "postal_code": "10001",
                "country": "USA",
                "notes": "Key client in the manufacturing sector",
                "website": "http://www.acme.com",
                "main_phone": "+1-212-555-1234",
                "created_date": "2023-01-15T09:30:00Z",
                "account_owner_email_address": "owner@example.com",
                "parent_account_id": "",
                "sic_code": "2011"
            }
        ]
      }'
```

### Supprimer plusieurs comptes {#delete-multiple-accounts}

La méthode `DELETE` supprime les enregistrements de compte de Braze. Contrairement à `PUT`, les requêtes `DELETE` ne sont pas réversibles. Une fois un compte supprimé, l'association entre les utilisateurs et ce compte est supprimée.

L'extrait de code suivant envoie une requête `DELETE` à `/business/accounts` avec une liste d'ID de compte dans le corps de la requête. Braze traite chaque ID et supprime l'enregistrement de compte correspondant. Cette opération est asynchrone. Braze met les suppressions en file d'attente et les traite en arrière-plan. Utilisez ceci pour les tâches de nettoyage en masse, par exemple lorsqu'un groupe de comptes a été perdu, consolidé ou n'est plus pertinent pour la segmentation dans Braze.

Pour supprimer plusieurs comptes, envoyez une requête `DELETE` à `/business/accounts` avec un corps contenant une liste d'ID de compte. Notez que cette opération est asynchrone.

Votre requête devrait ressembler à ceci :

```plaintext
curl -X DELETE https://YOUR_REST_API_URL/business/accounts \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "accounts": [
      { "id": "ACC001" },
      { "id": "ACC002" },
      { "id": "ACC003" }
    ]
  }'
```

### Supprimer un seul compte {#delete-one-account}

Comme pour la création d'un seul compte, cette opération cible un compte spécifique en incluant son ID directement dans l'URL de l'endpoint. Cela vous donne un contrôle précis sur un seul enregistrement sans affecter les autres.

L'extrait de code suivant envoie une requête `DELETE` à `/business/accounts/ACC001`. Cette opération est synchrone. Braze traite la requête immédiatement et renvoie une réponse dès qu'elle est terminée. Utilisez ceci lorsqu'un compte individuel est fermé, fusionné ou doit être supprimé de Braze pour des raisons de conformité ou d'hygiène des données.

Pour supprimer un seul compte, envoyez une requête `DELETE` à `/business/accounts/:account_id`. Notez que cette opération est synchrone.

Votre requête devrait ressembler à ceci :

```plaintext
curl -X DELETE https://YOUR_REST_API_URL/business/accounts/ACC001 \
  -H "Authorization: Bearer YOUR-REST-API-KEY"
```

## Utiliser des objets dans les messages {#using-objects-in-messages}

Après avoir [importé vos données dans Braze](#importing-data-to-braze), vous pouvez utiliser des objets de compte pour créer un segment et envoyer des messages personnalisés aux utilisateurs à l'aide de Liquid.

### Étape 1 : Créer un segment {#step-1-build-a-segment}

Ensuite, créez un segment qui combine les données utilisateur et les données de compte. Dans cet exemple, vous ciblez les directeurs d'entreprises du secteur de la santé pour augmenter les inscriptions à un nouveau webinaire de votre entreprise de promotion de la santé.

1. Accédez à **Audience** > **Segments**, puis sélectionnez **Create Segment**.
2. Donnez un nom à votre segment.
3. Dans le **Segment Builder**, sélectionnez le filtre **Business** et configurez les filtres de segmentation suivants. Lorsque vous avez terminé, sélectionnez **Save**.

| Filtre                          | Description                                      |
|---------------------------------|--------------------------------------------------|
| `Role is exactly director`      | Cible les utilisateurs dont le rôle est spécifiquement directeur |
| `Accounts industry matches regex healthcare` | Correspond aux utilisateurs dans des comptes dont le secteur est lié à la santé |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Actuellement, pour utiliser plusieurs filtres de compte, sélectionnez **Add Criteria** au lieu d'utiliser le menu déroulant **OR/AND**.
{% endalert %}

![Filtres de segmentation configurés pour créer un segment d'utilisateurs qui sont directeurs dans des entreprises du secteur de la santé.]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/build_segment.png %})

{% alert note %}
La segmentation fonctionne uniquement sur les 1 000 premiers enregistrements de compte correspondant aux critères. Vous pouvez avoir au maximum un filtre business par segment, et tous les critères doivent se trouver dans un seul filtre.
{% endalert %}

### Étape 2 : Utiliser Liquid pour personnaliser {#step-2-use-liquid-to-personalize}

Vous pouvez maintenant personnaliser votre message pour envoyer aux utilisateurs des informations sur les opportunités. Dans cet exemple, rédigez un message à l'attention de vos directeurs et incluez un lien vers le webinaire. Vous pouvez également utiliser un catalogue Braze pour récupérer des images spécifiques au secteur pour la personnalisation.

#### Étape 2.1 : Personnaliser avec les informations de compte {#step-21-personalize-with-account-information}

Sélectionnez **Business** comme type de personnalisation, puis sélectionnez **Name** pour personnaliser le message avec le nom de l'entreprise de l'utilisateur.

Le contenu suivant est copié dans votre presse-papiers.

{% raw %}
```javascript
{% business %}
{{ business_accounts[0].name }}
```
{% endraw %}

Braze génère la balise {% raw %}`{% business %}`{% endraw %}, qui définit un tableau nommé `business_accounts` contenant les informations de compte pour le compte associé.

Ajustez la sortie générée automatiquement pour créer votre message.

Dans l'exemple suivant, déplacez l'appel à la balise {% raw %}`{% business %}`{% endraw %} en haut du message et personnalisez avec le prénom de l'utilisateur. Utilisez le nom du compte pour personnaliser le message. La sortie Liquid reste la même, mais vous la placez dans différentes parties du message.

{% raw %}
```javascript
{% business %}

Hi {{${first_name}}},

We would love to invite you and your peers at {{ business_accounts[0].name }} to join our latest webinar named "Creating Optimal Health Outcomes for Patients".  Click the link below to register.
```
{% endraw %}

La sortie est similaire à ce qui suit :

{% raw %}
```javascript
Hi John,

We would love to invite you and your peers at Sunshine Health to join our latest webinar named "Creating Optimal Health Outcomes for Patients". Click the link below to register.
```
{% endraw %}

#### Étape 2.2 : Connecter avec les catalogues {#step-22-connect-with-catalogs}

Ensuite, personnalisez davantage votre message en utilisant les catalogues Braze pour ajouter et stocker une image correspondant à l'entreprise du secteur de la santé.

Pour cet exemple, supposons que vous disposez des éléments suivants :

- Un catalogue configuré appelé `industry_assets`
- L'ID de chaque entrée de catalogue est le nom d'un secteur qui correspond aux secteurs de vos comptes
- Les liens URL d'image pour une image principale et une image secondaire.

Voici un exemple du Liquid utilisé pour cette personnalisation.
{% raw %}
```javascript
//Make a call to the business tag.  This sets the accounts array and prepares us to pull account data out.
{% business %}

//Assign the user's accounts industry to a variable called industry.  This step isn't required but it makes everything easier to read.
{% assign industry = {{business_accounts[0].industry}} %}

//Make a catalog_items call to the industry_assets catalog and ask for the industry item (in this case, it will ask for "healthcare")
{% catalog_items industry_assets industry %}

// Get the hero image for the "healthcare" industry
{{items[0].hero_image}}
```
{% endraw %}

## Foire aux questions (FAQ) {#faq}

### Puis-je ajouter des champs personnalisés ? {#can-i-add-custom-fields}

Oui. Vous pouvez ajouter des champs personnalisés aux comptes. Si vous avez votre propre méthode de scoring des prospects, vous pouvez également utiliser un champ personnalisé sur votre objet de compte pour suivre cela.

### Un utilisateur peut-il être associé à plus d'un compte ? {#can-a-user-be-associated-with-more-than-one-account}

Non. Actuellement, chaque utilisateur ne peut avoir qu'une seule association de compte.

### Un profil utilisateur peut-il contenir plusieurs e-mails ? {#can-one-user-profile-contain-multiple-emails}

Non. Un profil utilisateur ne peut pas avoir plus d'un e-mail, comme un e-mail personnel et un e-mail professionnel.