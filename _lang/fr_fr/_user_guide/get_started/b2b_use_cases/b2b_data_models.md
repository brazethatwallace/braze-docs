---
nav_title: Modèles de données
article_title: Créer un modèle de données B2B
page_order: 0
page_type: reference
description: "Découvrez comment utiliser les outils de données de Braze pour créer des modèles B2B."
---

# Créer un modèle de données B2B {#create-a-b2b-data-model}

> Ce cas d'utilisation montre comment utiliser les outils de données de Braze pour créer un modèle de données B2B efficace et performant, qui vous aide à cibler, déclencher, personnaliser et envoyer des messages à vos utilisateurs professionnels.

{% alert note %}
Ces recommandations sont susceptibles d'évoluer au fil du temps, à mesure que Braze développe ses capacités B2B.
{% endalert %}

Avant d'aborder la mise en place de votre modèle de données B2B, passons en revue plusieurs concepts et termes essentiels.

Quatre objets B2B principaux sont nécessaires pour exécuter des campagnes B2B.

| Objet | Description |
| --- | --- |
| Prospects | Un enregistrement de clients potentiels ayant manifesté de l'intérêt pour un produit ou un service, mais n'ayant pas encore été qualifiés comme opportunité. |
| Contacts | En général, des personnes qui ont été qualifiées et converties d'un prospect en contact afin de poursuivre une opportunité de vente. |
| Opportunités | Un enregistrement qui suit les détails d'une vente potentielle ou d'une transaction en cours.
| Comptes | L'enregistrement d'une organisation qui est un client potentiel qualifié, un client existant, un partenaire ou un concurrent entretenant une relation d'importance similaire. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Créer un modèle de données B2B" }

Dans Braze, ces quatre objets sont combinés et réduits en deux objets : les profils utilisateurs et les objets métier.

| Objet B2B Braze | Description | Objets B2B d'origine  |
| --- | --- | --- |
| Profils utilisateur | Ils correspondent directement aux prospects et contacts de votre système CRM de vente. Les prospects capturés par Braze sont automatiquement créés en tant que prospects dans votre système CRM de vente. Lorsqu'ils sont convertis en contacts, les ID et les détails des contacts sont synchronisés vers Braze. | Prospects<br> Contacts |
| Objets métier | Ils correspondent à tous les objets non-utilisateur de votre système CRM de vente, y compris vos objets spécifiques aux ventes, tels que les objets de compte et les objets d'opportunité. | Comptes<br> Opportunités |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Créer un modèle de données B2B" }

## Étape 1 : Créer vos objets métier dans Braze {#step-1-create-your-business-objects-in-braze}

Les objets métier sont tous les ensembles de données non centrés sur l'utilisateur. Dans un contexte B2B, il s'agit notamment des données relatives aux comptes et aux opportunités, ainsi que de tout autre ensemble de données pertinent non centré sur l'utilisateur que votre entreprise suit.

Il existe deux méthodes pour créer et gérer vos objets métier dans Braze : les catalogues et les sources connectées.

| Méthode | Description |
| --- | --- |
| [Catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs/) | Il s'agit d'objets de données indépendants (objets de données supplémentaires) associés au profil utilisateur principal dans Braze. Dans un contexte B2B, vous aurez probablement des catalogues pour vos comptes et vos opportunités. |
| [Sources connectées]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/) | Elles permettent à Braze d'interroger directement votre entrepôt de données. Vous synchronisez probablement déjà régulièrement vos prospects, contacts, opportunités et comptes vers votre entrepôt de données. Vous pouvez donc faire pointer la segmentation de Braze directement vers cet entrepôt et l'activer dans un environnement sans copie. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 1 : Créer vos objets métier dans Braze" }

{% tabs %}
{% tab Catalogs %}

### Option 1 : Utiliser des catalogues pour les comptes et les opportunités {#option-1-use-catalogs-for-accounts-and-opportunities}

Les catalogues sont des tables de données hébergées et gérées dans Braze. Alors que les données relatives aux comptes et aux opportunités proviennent du système CRM de vente de votre choix, vous les dupliquez dans Braze pour les utiliser à des fins marketing : segmentation basée sur les comptes, marketing basé sur les comptes, gestion des prospects, etc.

Pour cette option, nous vous recommandons de créer un catalogue pour vos comptes et un autre pour vos opportunités, et de les mettre à jour fréquemment en envoyant des mises à jour à Braze via notre [API catalogues]({{site.baseurl}}/api/endpoints/catalogs/) ou l'[Ingestion de données cloud (CDI) pour les catalogues]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/). Lors de la création de ces catalogues, assurez-vous que le `id` (première colonne) de votre catalogue correspond au `id` de votre système CRM de vente.

#### Mapper les champs de votre CRM {#map-over-your-crm-fields}

Les tableaux ci-dessous présentent quelques exemples de champs que vous pouvez mapper à partir des objets compte et opportunité de votre CRM.

{% subtabs %}
{% subtab Account catalog %}

Dans ce cas d'utilisation, Salesforce est l'exemple de système CRM. Vous pouvez mapper n'importe quel champ inclus dans les objets de votre CRM.

<table aria-label="Mapper les champs de votre CRM" border="1">
  <caption>Mapper les champs de votre CRM</caption>
  <thead>
  <tr>
    <th><b>Objet Braze</b></th>
    <th><b>Champ Braze</b></th>
    <th><b>Objet CRM (Salesforce)</b></th>
    <th><b>Champ CRM (Salesforce)</b></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td rowspan="4">Catalogue &gt; Catalogue de comptes</td>
    <td><code>id</code></td>
    <td><code>account</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>AccountName</code></td>
    <td><code>account</code></td>
    <td><code>Account Name</code></td>
  </tr>
  <tr>
    <td><code>Type</code></td>
    <td><code>account</code></td>
    <td><code>Type</code></td>
  </tr>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>account</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tbody>
</table>

##### Exemple de tableau des champs de compte mappés {#example-table-of-mapped-account-fields}

![Tableau des comptes Salesforce avec les informations correspondantes, telles que l'adresse de facturation et le propriétaire du compte.]({% image_buster /assets/img/b2b/sf_accounts.png %})

{% endsubtab %}
{% subtab Opportunity catalog %}

Dans ce cas d'utilisation, Salesforce est l'exemple de système CRM. Vous pouvez mapper n'importe quel champ inclus dans les objets de votre CRM.

<table aria-label="Exemple de tableau des champs de compte mappés" border="1">
  <caption>Exemple de tableau des champs de compte mappés</caption>
  <thead>
  <tr>
    <th><b>Objet Braze</b></th>
    <th><b>Champ Braze</b></th>
    <th><b>Objet CRM (Salesforce)</b></th>
    <th><b>Champ CRM (Salesforce)</b></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td rowspan="4">Catalogue &gt; Catalogue d'opportunités</td>
    <td><code>id</code></td>
    <td><code>opportunity</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>OpportunityName</code></td>
    <td><code>opportunity</code></td>
    <td><code>Opportunity Name</code></td>
  </tr>
  <tr>
    <td><code>Territory</code></td>
    <td><code>opportunity</code></td>
    <td><code>Territory</code></td>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>opportunity</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tr>
  </tbody>
</table>

##### Exemple de tableau des champs d'opportunité mappés {#example-table-of-mapped-opportunity-fields}

![Tableau des opportunités Salesforce avec les informations correspondantes, telles que l'adresse de facturation et le propriétaire du compte.]({% image_buster /assets/img/b2b/sf_opportunities.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Connected sources %}

### Option 2 : Utiliser des sources connectées pour les comptes et les opportunités {#option-2-use-connected-sources-for-accounts-and-opportunities}

Les sources connectées sont des tables de données hébergées dans votre propre entrepôt de données et interrogées par les [Extensions de segments CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments/) de Braze. Contrairement aux catalogues, au lieu de dupliquer vos objets métier (comptes et opportunités) dans Braze, vous les conservez dans votre entrepôt de données et utilisez ce dernier comme source de vérité.

Pour configurer les sources connectées, consultez [Intégration des sources connectées]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/#integrating-connected-sources).

{% endtab %}
{% endtabs %}

## Étape 2 : Relier vos objets métier aux profils utilisateurs {#step-2-relate-your-business-objects-to-user-profiles}

Les profils utilisateurs sont l'objet principal dans Braze. Ils alimentent la majorité de votre segmentation démographique, de vos déclencheurs et de votre personnalisation. Les profils utilisateurs comprennent les [données utilisateur par défaut]({{site.baseurl}}/user_guide/data/unification/user_data/) collectées par notre SDK et d'autres sources, y compris les [données personnalisées]({{site.baseurl}}/user_guide/data/activation/), qui prennent la forme d'attributs (données démographiques), d'événements (données comportementales) ou d'achats (données transactionnelles).

### Étape 2.1 : Mapper les ID du CRM de vente vers Braze {#step-21-map-sales-crm-ids-to-braze}

Tout d'abord, assurez-vous que Braze et le CRM de votre choix disposent d'un identifiant commun pour partager les données. Nous vous suggérons d'utiliser le tableau suivant pour mapper les champs d'ID de votre CRM de vente vers l'objet utilisateur de Braze. Le tableau ci-dessous utilise Salesforce comme système CRM, mais cette opération peut être réalisée avec n'importe quel CRM.

#### Objet Braze : Utilisateur {#braze-object-user}

| Champ Braze | Objet CRM (Salesforce) | Champ CRM (Salesforce) | Informations supplémentaires |
| --- | --- | --- | --- |
| `Aliases.salesforce_lead_id` | Lead | `id` | - Libellé d'alias utilisateur : `salesforce_lead_id` <br>- Nom de l'alias utilisateur : `lead_id` |
| `Aliases.salesforce_contact_id` | Contact | `id` | - Libellé d'alias utilisateur : `salesforce_contact_id` <br>- Nom de l'alias utilisateur : `contact_id` |
| `AccountId` | Contact | `AccountId` |
| `OpportunityId` (facultatif, scalaire) <br>ou<br> `Opportunities` (facultatif, tableau) | Opportunity | `id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Objet Braze : Utilisateur" }

{% alert note %}
Nous vous recommandons d'utiliser des [alias]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#user-aliases) plutôt que `external_id` pour mapper les identifiants de prospects et de contacts Salesforce vers Braze. Cela réduit le nombre de recherches nécessaires lors de l'identification et de l'exécution de vos initiatives de croissance axée sur le produit.
{% endalert %}

Une fois vos ID synchronisés, vous devez relier vos profils utilisateurs Braze à vos objets métier.

### Étape 2.2 : Créer une relation entre les profils utilisateurs et vos objets métier {#step-22-create-a-relationship-between-user-profiles-and-your-business-objects}

{% tabs %}
{% tab Catalogs %}

#### Option 1 : Avec les catalogues {#option-1-when-using-catalogs}

Maintenant que les détails de vos opportunités et comptes sont enregistrés en tant que catalogues Braze, vous devez créer une relation entre ces catalogues et les profils utilisateurs auxquels vous souhaitez envoyer des messages. Pour l'instant, cela nécessite deux étapes :

1. Incluez le compte (par exemple `account_id (string)`), l'ID d'opportunité (par exemple `opportunity_ids (array)`) ou les deux dans le profil utilisateur en tant qu'attributs.
2. Enregistrez un événement (par exemple `account_linked`) qui inclut l'ID du compte en tant que propriété de l'événement.

```json
{
  "attributes" : [
    {
      "external_id" : "user1",
      "accountId" : "001J7000004K7AF",
      "opportunityIds" : [
"0064J000004EU59",
"0064J000004EU5G"
]
    }
  ],
  "events" : [
    {
      "external_id" : "user1",
      "name" : "account_linked",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "account_id": "001J7000004K7AF"
      }
    }
  ]
}
```

{% endtab %}
{% tab Connected sources %}

#### Option 2 : Avec les sources connectées {#option-2-when-using-connected-sources}

L'une des tables de votre source connectée doit inclure un `user_id` qui correspond au `external_user_id` défini dans Braze pour vos utilisateurs. La configuration du profil utilisateur décrite ci-dessus utilise vos identifiants de prospect et `contact_ids` comme `external_id`. Vous devez donc vous assurer que vos tables de prospects/contacts incluent ces ID.

En plus de vérifier la correspondance des ID, nous vous recommandons d'écrire des données de base au niveau du compte, telles que `account_id`, `opportunity_id`, et même des attributs firmographiques courants comme `industry`, dans les profils utilisateurs pour une segmentation et une personnalisation efficaces.

{% endtab %}
{% endtabs %}