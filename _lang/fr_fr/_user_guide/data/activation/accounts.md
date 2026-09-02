---
nav_title: Comptes
article_title: Objets de compte
page_order: 7
page_type: reference
description: "Utilisez les objets de compte pour segmenter les utilisateurs, personnaliser les messages avec des données de compte et gérer les enregistrements de compte."
---

# Objets de compte {#account-objects}

> Utilisez les objets de compte pour segmenter et personnaliser les communications avec des données de compte.

{% alert important %}
La fonctionnalité Comptes est en accès anticipé. Ces instructions peuvent évoluer au fur et à mesure du développement de la fonctionnalité.
{% endalert %}

Avec les objets de compte, vous pouvez :

- Créer des segments avec des critères de compte
- Personnaliser les messages avec des attributs de compte via Liquid
- Gérer les enregistrements de compte en un seul endroit

Les objets de compte sont des modèles de données au niveau de l'espace de travail, connectés aux profils utilisateur. Un enregistrement de compte correspond à un compte spécifique et aux données de champs qui lui sont associées.
Utilisez les objets de compte lorsque le contexte du compte, comme les attributs d'entreprise, vous aide à cibler et personnaliser vos communications.
Vous pouvez également modéliser des hiérarchies de comptes (comme des comptes parents et enfants) et associer un profil utilisateur à plusieurs comptes.

## Pourquoi utiliser les objets de compte ? {#why-use-account-objects}

Certains cas d'usage nécessitent un contexte au niveau du compte, même lorsque vos Campaigns et Canvas sont envoyés à des utilisateurs individuels.

Les objets de compte vous permettent de stocker les données de compte une seule fois et de les réutiliser pour la segmentation et la personnalisation dans Braze.

Cela vous permet de :

- Segmenter par attributs de compte
- Personnaliser les messages avec un contexte de compte partagé (comme le nom de l'entreprise ou le secteur d'activité)
- Modéliser les relations entre les comptes et connecter un profil utilisateur à plusieurs comptes

Cette approche remplace la duplication des mêmes attributs de compte sur de nombreux profils utilisateurs.

## Prérequis {#prerequisites}

Avant de commencer :

- Votre espace de travail doit être activé pour l'accès anticipé à Accounts. Contactez votre équipe de compte Braze.
- Vous devez déjà avoir des utilisateurs dans Braze.
- Une fois Accounts activé, il apparaît dans **Data Settings** > **Accounts**. Si c'est la première fois que vous utilisez Accounts, suivez les instructions d'initialisation à l'écran.

## Modèle de données des comptes {#account-data-model}

Chaque compte nécessite un ID externe (`id`) et un nom (`name`).

Les champs de compte de cette section définissent le schéma de l'objet Account. Ces champs s'appliquent à chaque enregistrement de compte individuel que vous stockez dans Braze.

Braze inclut des objets de compte avec des champs standard par défaut. Vous pouvez ajouter et supprimer des champs personnalisés en fonction de votre cas d'usage.

| Nom du champ | Type de champ | Obligatoire | Description |
| --- | --- | --- | --- |
| `id` | chaîne de caractères | Oui | L'ID système de votre compte (par exemple, l'ID CRM). Doit être unique dans votre espace de travail. |
| `name` | chaîne de caractères | Oui | Nom du compte. |
| `type` | chaîne de caractères | Non | Type de compte, tel que client, partenaire ou revendeur. |
| `annual_revenue` | nombre | Non | Chiffre d'affaires annuel du compte. |
| `industry` | chaîne de caractères | Non | Secteur d'activité du compte. |
| `number_of_employees` | nombre | Non | Nombre d'employé or salariés. |
| `address` | chaîne de caractères | Non | Adresse postale. |
| `city` | chaîne de caractères | Non | Ville. |
| `state` | chaîne de caractères | Non | État ou province. |
| `postal_code` | chaîne de caractères | Non | Code postal. |
| `country` | chaîne de caractères | Non | Pays. |
| `notes` | chaîne de caractères | Non | Notes supplémentaires. |
| `website` | chaîne de caractères | Non | URL du site web. |
| `main_phone` | chaîne de caractères | Non | Numéro de téléphone principal. |
| `created_date` | heure | Non | Horodatage de la création du compte. |
| `sic_code` | chaîne de caractères | Non | Code de classification industrielle standard (SIC). |
| Champs personnalisés | personnalisé | Non | Champs que vous définissez et gérez. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Champs du modèle de données des comptes" }

## Options d'intégration de données {#data-integration-options}

Vous pouvez gérer les enregistrements de comptes via :

- Les endpoints REST API pour les enregistrements de comptes
- La modification dans le navigateur dans **Paramètres des données** > **Comptes** pour les enregistrements individuels

## Premiers pas {#get-started}

### Étape 1 : Activer les Accounts {#step-1-enable-accounts}

Les Accounts sont activés au niveau de l'entreprise. Pendant l'accès anticipé, votre équipe de compte Braze se charge de l'activation unique.

Lorsque les Accounts sont activés, accédez à **Data Settings** > **Accounts** et complétez le flux d'initialisation unique si vous y êtes invité.

### Étape 2 : Ajouter des enregistrements de compte {#step-2-add-account-records}

Ajoutez ou mettez à jour des enregistrements de compte via la REST API ou l'édition dans le navigateur.

### Étape 3 : Créer un filtre calculé pour les critères de compte {#step-3-create-a-calculated-filter-for-account-criteria}

Avant de segmenter sur les données de compte, créez un filtre calculé qui définit vos critères de compte :

1. Accédez à **Audience** > **Calculated Filters**.
2. Sélectionnez **Create filter**, puis sélectionnez **Data Object filters**.
3. Définissez vos critères de compte.

Pour plus de détails, consultez [Filtres calculés]({{site.baseurl}}/user_guide/audience/segments/calculated_filters#create-a-calculated-filter).

### Étape 4 : Utiliser le filtre calculé dans le Segment Builder {#step-4-use-the-calculated-filter-in-segment-builder}

Dans le Segment Builder, sélectionnez le filtre calculé que vous avez créé, puis ajoutez tout filtre d'attribut utilisateur supplémentaire qui soutient le ciblage de votre Campaign ou Canvas.

## Créer des Segments basés sur les comptes {#build-account-based-segments}

Une fois que vos enregistrements de compte et votre filtre calculé sont prêts :

1. Accédez au [générateur de Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).
2. Ajoutez votre filtre calculé préconfiguré pour les critères de compte.
3. Ajoutez tout filtre d'attribut utilisateur supplémentaire.
4. Enregistrez votre Segment.

Par exemple :

- **Filtre calculé :** le champ `industry` du compte est exactement `healthcare`
- **Filtre d'attribut utilisateur :** `days_since_last_login` est inférieur à `30`

## Personnaliser avec Liquid {#personalize-with-liquid}

Utilisez l'étiquette Liquid `{% raw %}{% data_object account %}{% endraw %}` pour charger les données de compte de l'utilisateur dans le tableau `data_objects`.

{% alert note %}
Lorsque vous utilisez **Aperçu et test**, utilisez un Segment qui inclut des données de compte afin que la personnalisation puisse se résoudre correctement.
{% endalert %}

{% raw %}
```liquid
{% data_object account %}
Hi {{${first_name}}},
We'd love to invite you and your peers at {{ data_objects[0].name }}.
```
{% endraw %}

Pour itérer sur tous les comptes correspondants :

{% raw %}
```liquid
{% data_object account %}
{% for acct in data_objects %}
- {{ acct.name }}
{% endfor %}
```
{% endraw %}

## Principes de base de l'API {#api-basics}

Vous pouvez utiliser la REST API pour gérer les enregistrements de compte pendant l'accès anticipé.

Pour plus de détails sur les endpoints, consultez [Endpoints Data Objects]({{site.baseurl}}/api/endpoints/data_objects).

Pour l'authentification et les principes de base des endpoints REST, consultez [Aperçu de l'API Braze]({{site.baseurl}}/api/basics).

## Questions fréquentes {#frequently-asked-questions}

### Puis-je ajouter des champs personnalisés aux comptes ? {#can-i-add-custom-fields-to-accounts}

Oui. Vous pouvez définir et gérer des champs de compte personnalisés dans votre espace de travail. Pour les exigences relatives aux champs, consultez [Modèle de données de compte](#account-data-model).

### Accounts est-il un module complémentaire payant ? {#is-accounts-a-paid-add-on}

Non. Accounts n'est pas un module complémentaire payant et est disponible sur tous les forfaits. Pendant l'accès anticipé, votre équipe de compte Braze doit l'activer pour votre espace de travail.