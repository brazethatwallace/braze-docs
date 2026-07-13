---
nav_title: "Attributs du profil utilisateur"
article_title: Vues d'attributs d'utilisateurs dans Snowflake
page_order: 10
page_type: partner
search_tag: Partner
toc_headers: h2
---

# Attributs du profil utilisateur {#user-profile-attributes}

> Cette page sert de référence pour les vues d'attributs par défaut et personnalisés dans Snowflake. Il existe trois vues pour les attributs par défaut et trois vues pour les attributs personnalisés, chacune étant conçue pour un cas d'usage spécifique avec ses propres considérations en matière de performances.

## Parité des données avec le tableau de bord {#data-parity-with-the-dashboard}

Dans de rares cas, les valeurs d'attributs par défaut et personnalisés dans les vues Snowflake de cette page peuvent ne pas correspondre à ce que vous voyez sur le profil d'un utilisateur dans le tableau de bord de Braze.

Par exemple, un attribut peut apparaître comme `NULL` dans Snowflake alors que le tableau de bord affiche une valeur pour cet utilisateur.

Si vous constatez des incohérences généralisées, contactez votre gestionnaire du succès des clients ou l'assistance Braze.

## Vues disponibles {#available-views}

<table aria-label="Vues disponibles">
  <caption>Vues disponibles</caption>
  <thead>
    <tr>
      <th>Type</th>
      <th>Vue</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Attribut par défaut</td>
      <td><code>USER_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Instantanés de profil utilisateur</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Profils utilisateurs en temps réel</td>
    </tr>
    <tr>
      <td><code>USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Historique des modifications</td>
    </tr>
    <tr>
      <td rowspan="3">Attribut personnalisé</td>
      <td><code>USER_CUSTOM_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Instantanés de profil utilisateur</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED</code></td>
      <td>Profils utilisateurs en temps réel</td>
    </tr>
    <tr>
      <td><code>USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Historique des modifications</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Vues disponibles" }

## Instantanés de profil utilisateur {#user-profile-snapshots}

Ces vues fournissent des instantanés périodiques des attributs du profil utilisateur. Les données sont différées de 12 heures maximum, ce qui les rend utiles pour les requêtes qui ne nécessitent pas de mises à jour en temps réel.

 - `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`
 - `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`

### Utilisation {#usage}

* Fournit un instantané des attributs utilisateur avec un **délai pouvant aller jusqu'à 12 heures**.
* Donne de bons résultats pour les requêtes qui ne nécessitent pas une précision en temps réel.
* L'exécution des requêtes est plus rapide, en particulier lors du filtrage sur des attributs autres que `USER_ID`.
* **Limitation :** les données ne sont pas actualisées en temps réel.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### Schéma `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` {#user_default_attributes_view_shared-schema}

| Nom de la colonne | Type de données | Description |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Identifiant de votre espace de travail Braze |
| `APP_ID` | VARCHAR | L'application spécifique au sein de votre espace de travail |
| `USER_ID` | VARCHAR | L'identifiant utilisateur unique de Braze |
| `TIME` | NUMBER | Horodatage Unix (secondes) de la mise à jour du profil |
| `TIME_MS` | NUMBER | Horodatage Unix (millisecondes) de la mise à jour du profil |
| `UPDATE_SOURCE` | VARCHAR | La source de la mise à jour de l'attribut (API, SDK, tableau de bord, etc.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Date de la dernière mise à jour des données dans Snowflake |
| `EXTERNAL_USER_ID` | VARCHAR | Votre propre identifiant utilisateur (si défini) |
| `FIRST_NAME` | VARCHAR | Prénom de l'utilisateur |
| `LAST_NAME` | VARCHAR | Nom de famille de l'utilisateur |
| `EMAIL_ADDRESS` | VARCHAR | Adresse e-mail de l'utilisateur |
| `GENDER` | VARCHAR | Genre de l'utilisateur |
| `PHONE_NUMBER` | VARCHAR | Numéro de téléphone de l'utilisateur |
| `DOB` | VARCHAR | Date de naissance de l'utilisateur |
| `TIME_ZONE` | VARCHAR | Fuseau horaire de l'utilisateur |
| `HOME_CITY` | VARCHAR | Ville de résidence de l'utilisateur |
| `COUNTRY` | VARCHAR | Pays de l'utilisateur |
| `LANGUAGE` | VARCHAR | Préférence linguistique de l'utilisateur |
| `ARCHIVED` | BOOLEAN | Indique si le profil utilisateur est archivé |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESVIEWSHARED schema" }


### Schéma `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` {#user_custom_attributes_view_shared-schema}

| Nom de la colonne | Type de données | Description |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Identifiant de votre espace de travail Braze |
| `APP_ID` | VARCHAR | L'application spécifique au sein de votre espace de travail |
| `USER_ID` | VARCHAR | L'identifiant utilisateur unique de Braze |
| `EXTERNAL_USER_ID` | VARCHAR | Votre propre identifiant utilisateur (si défini) |
| `TIME` | NUMBER | Horodatage Unix (secondes) de la mise à jour du profil |
| `TIME_MS` | NUMBER | Horodatage Unix (millisecondes) de la mise à jour du profil |
| `UPDATE_SOURCE` | VARCHAR | La source de la mise à jour de l'attribut (API, SDK, tableau de bord, etc.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Date de la dernière mise à jour des données dans Snowflake |
| `CUSTOM_ATTRIBUTES` | VARIANT | Objet JSON contenant tous les attributs personnalisés (paires clé-valeur) |
| `ARCHIVED` | BOOLEAN | Indique si le profil utilisateur est archivé |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERCUSTOMATTRIBUTESVIEWSHARED schema" }

#### Utiliser CUSTOM_ATTRIBUTES {#working-with-custom_attributes}

La colonne `CUSTOM_ATTRIBUTES` stocke tous vos attributs personnalisés sous forme d'objet JSON. Vous pouvez accéder aux attributs individuels à l'aide des fonctions JSON de Snowflake.

**Exemple : interroger des attributs personnalisés spécifiques**

```sql
-- Get users with a specific loyalty tier
SELECT
  USER_ID,
  EXTERNAL_USER_ID,
  CUSTOM_ATTRIBUTES:loyalty_tier::STRING as loyalty_tier,
  CUSTOM_ATTRIBUTES:points::NUMBER as points
FROM USER_CUSTOM_ATTRIBUTES_VIEW_SHARED
WHERE CUSTOM_ATTRIBUTES:loyalty_tier::STRING = 'gold';

-- Get users who made a purchase above a certain amount
SELECT
  USER_ID,
  CUSTOM_ATTRIBUTES:last_purchase_amount::NUMBER as last_purchase_amount
FROM USER_CUSTOM_ATTRIBUTES_VIEW_SHARED
WHERE CUSTOM_ATTRIBUTES:last_purchase_amount::NUMBER > 100;
```

**Exemple : analyser les données d'attributs personnalisés**

```sql
-- Count users by subscription status
SELECT
  CUSTOM_ATTRIBUTES:subscription_status::STRING as subscription_status,
  COUNT(*) as user_count
FROM USER_CUSTOM_ATTRIBUTES_VIEW_SHARED
GROUP BY CUSTOM_ATTRIBUTES:subscription_status::STRING;

-- Find average order value by customer segment
SELECT
  CUSTOM_ATTRIBUTES:customer_segment::STRING as segment,
  AVG(CUSTOM_ATTRIBUTES:lifetime_value::NUMBER) as avg_lifetime_value
FROM USER_CUSTOM_ATTRIBUTES_VIEW_SHARED
WHERE CUSTOM_ATTRIBUTES:customer_segment IS NOT NULL
GROUP BY CUSTOM_ATTRIBUTES:customer_segment::STRING;
```

## Vues de profil utilisateur en temps réel {#real-time-user-profile-views}

Ces vues fournissent des mises à jour quasi en temps réel des attributs du profil utilisateur, les données étant différées de 10 minutes au maximum après une mise à jour dans Braze.

  - `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`
  - `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`

### Utilisation

* Fournit des attributs utilisateur actualisés avec un délai minimal (~10 minutes).
* Utile pour les analyses en temps réel et les scénarios nécessitant des données récentes.
* **Considérations relatives aux performances :**
    * Les requêtes sur des utilisateurs individuels sont plus rapides (moins d'une minute avec un grand entrepôt).
    * Les requêtes sans filtre sur USER_ID nécessitent une agrégation pour tous les utilisateurs, ce qui allonge considérablement le temps d'exécution.
    * Les requêtes sur un grand ensemble de données (plus de 100 millions d'utilisateurs, par exemple) peuvent prendre plusieurs minutes.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### Schéma `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` {#user_latest_state_default_attributes_view_shared-schema}

| Nom de la colonne | Type de données | Description |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Identifiant de votre espace de travail Braze |
| `APP_ID` | VARCHAR | L'application spécifique au sein de votre espace de travail |
| `USER_ID` | VARCHAR | L'identifiant utilisateur unique de Braze |
| `TIME` | NUMBER | Horodatage Unix (secondes) de la mise à jour du profil |
| `TIME_MS` | NUMBER | Horodatage Unix (millisecondes) de la mise à jour du profil |
| `UPDATE_SOURCE` | VARCHAR | La source de la mise à jour de l'attribut (API, SDK, tableau de bord, etc.) |
| `ARCHIVED` | BOOLEAN | Indique si le profil utilisateur est archivé |
| `SF_UPDATED_AT` | TIMESTAMP_LTZ | Date de la dernière mise à jour des données dans Snowflake |
| `EXTERNAL_USER_ID` | VARCHAR | Votre propre identifiant utilisateur (si défini) |
| `FIRST_NAME` | VARCHAR | Prénom de l'utilisateur |
| `LAST_NAME` | VARCHAR | Nom de famille de l'utilisateur |
| `EMAIL_ADDRESS` | VARCHAR | Adresse e-mail de l'utilisateur |
| `GENDER` | VARCHAR | Genre de l'utilisateur |
| `PHONE_NUMBER` | VARCHAR | Numéro de téléphone de l'utilisateur |
| `DOB` | VARCHAR | Date de naissance de l'utilisateur |
| `HOME_CITY` | VARCHAR | Ville de résidence de l'utilisateur |
| `COUNTRY` | VARCHAR | Pays de l'utilisateur |
| `LANGUAGE` | VARCHAR | Préférence linguistique de l'utilisateur |
| `TIME_ZONE` | VARCHAR | Fuseau horaire de l'utilisateur |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED schema" }

### Schéma `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` {#user_latest_state_custom_attribute_view_shared-schema}

| Nom de la colonne | Type de données | Description |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Identifiant de votre espace de travail Braze |
| `USER_ID` | VARCHAR | L'identifiant utilisateur unique de Braze |
| `EXTERNAL_USER_ID` | VARCHAR | Votre propre identifiant utilisateur (si défini) |
| `TIME` | NUMBER | Horodatage Unix (secondes) de la mise à jour du profil |
| `TIME_MS` | NUMBER | Horodatage Unix (millisecondes) de la mise à jour du profil |
| `UPDATE_SOURCE` | VARCHAR | La source de la mise à jour de l'attribut (API, SDK, tableau de bord, etc.) |
| `ARCHIVED` | BOOLEAN | Indique si le profil utilisateur est archivé |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Date de la dernière mise à jour des données dans Snowflake |
| `APP_ID` | VARCHAR | L'application spécifique au sein de votre espace de travail |
| `CUSTOM_ATTRIBUTES` | OBJECT | Objet JSON contenant tous les attributs personnalisés (paires clé-valeur) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERLATESTSTATECUSTOMATTRIBUTEVIEWSHARED schema" }

{% alert note %}
Cette vue utilise le type `OBJECT` pour `CUSTOM_ATTRIBUTES` au lieu de `VARIANT`. Utilisez la même syntaxe d'accesseur JSON (`:attribute_name::TYPE`) pour interroger les attributs individuels.
{% endalert %}

## Historique des modifications {#historical-change-logs}

Ces vues stockent les journaux de modifications historiques des attributs utilisateur, capturant les changements avec une granularité de 12 heures.

- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`
- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`

### Utilisation

* Fournit un enregistrement des modifications historiques des attributs utilisateur sur une période glissante de 6 mois.
* Les données sont capturées toutes les 12 heures, ce qui signifie que les mises à jour multiples au cours de cette fenêtre sont combinées en un seul enregistrement. Les modifications individuelles au cours de cette période ne sont pas conservées séparément.
* `EFF_DT` et `END_DT` marquent le début et la fin de l'état des attributs d'un utilisateur.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### Schéma `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` {#user_default_attributes_history_view_shared-schema}

| Nom de la colonne | Type de données | Description |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Identifiant de votre espace de travail Braze |
| `USER_ID` | VARCHAR | L'identifiant utilisateur unique de Braze |
| `APP_ID` | VARCHAR | L'application spécifique au sein de votre espace de travail |
| `TIME` | NUMBER | Horodatage Unix (secondes) de la mise à jour du profil |
| `TIME_MS` | NUMBER | Horodatage Unix (millisecondes) de la mise à jour du profil |
| `UPDATE_SOURCE` | VARCHAR | La source de la mise à jour de l'attribut (API, SDK, tableau de bord, etc.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Date de la dernière mise à jour des données dans Snowflake |
| `EXTERNAL_USER_ID` | VARCHAR | Votre propre identifiant utilisateur (si défini) |
| `FIRST_NAME` | VARCHAR | Prénom de l'utilisateur |
| `LAST_NAME` | VARCHAR | Nom de famille de l'utilisateur |
| `EMAIL_ADDRESS` | VARCHAR | Adresse e-mail de l'utilisateur |
| `GENDER` | VARCHAR | Genre de l'utilisateur |
| `PHONE_NUMBER` | VARCHAR | Numéro de téléphone de l'utilisateur |
| `DOB` | VARCHAR | Date de naissance de l'utilisateur |
| `TIME_ZONE` | VARCHAR | Fuseau horaire de l'utilisateur |
| `HOME_CITY` | VARCHAR | Ville de résidence de l'utilisateur |
| `COUNTRY` | VARCHAR | Pays de l'utilisateur |
| `LANGUAGE` | VARCHAR | Préférence linguistique de l'utilisateur |
| `EFF_DT` | TIMESTAMP_NTZ | Date d'effet : début de cet état d'attribut |
| `END_DT` | TIMESTAMP_NTZ | Date de fin : fin de cet état d'attribut (NULL pour l'état actuel) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESHISTORYVIEWSHARED schema" }

### Schéma `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED` {#user_custom_attributes_history_view_shared-schema}

| Nom de la colonne | Type de données | Description |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Identifiant de votre espace de travail Braze |
| `USER_ID` | VARCHAR | L'identifiant utilisateur unique de Braze |
| `APP_ID` | VARCHAR | L'application spécifique au sein de votre espace de travail |
| `EXTERNAL_USER_ID` | VARCHAR | Votre propre identifiant utilisateur (si défini) |
| `TIME` | NUMBER | Horodatage Unix (secondes) de la mise à jour du profil |
| `TIME_MS` | NUMBER | Horodatage Unix (millisecondes) de la mise à jour du profil |
| `UPDATE_SOURCE` | VARCHAR | La source de la mise à jour de l'attribut (API, SDK, tableau de bord, etc.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Date de la dernière mise à jour des données dans Snowflake |
| `CUSTOM_ATTRIBUTES` | VARIANT | Objet JSON contenant tous les attributs personnalisés (paires clé-valeur) |
| `ARCHIVED` | BOOLEAN | Indique si le profil utilisateur est archivé |
| `EFF_DT` | TIMESTAMP_NTZ | Date d'effet : début de cet état d'attribut |
| `END_DT` | TIMESTAMP_NTZ | Date de fin : fin de cet état d'attribut (NULL pour l'état actuel) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERCUSTOMATTRIBUTESHISTORYVIEWSHARED schema" }

## Cas d'usage courants {#common-use-cases}

### Créer des segments d'utilisateurs {#building-user-segments}

```sql
-- Find active users in a specific city who haven't received an email recently
SELECT
  d.EXTERNAL_USER_ID,
  d.EMAIL_ADDRESS,
  d.HOME_CITY,
  c.CUSTOM_ATTRIBUTES:last_email_sent::TIMESTAMP as last_email_sent
FROM USER_DEFAULT_ATTRIBUTES_VIEW_SHARED d
JOIN USER_CUSTOM_ATTRIBUTES_VIEW_SHARED c
  ON d.USER_ID = c.USER_ID
WHERE d.HOME_CITY = 'New York'
  AND d.EMAIL_ADDRESS IS NOT NULL
  AND (c.CUSTOM_ATTRIBUTES:last_email_sent::TIMESTAMP < DATEADD(day, -30, CURRENT_TIMESTAMP())
       OR c.CUSTOM_ATTRIBUTES:last_email_sent IS NULL);
```

### Analyser le comportement des utilisateurs au fil du temps {#analyzing-user-behavior-over-time}

```sql
-- Track how a user's loyalty tier changed over the past 6 months
SELECT
  USER_ID,
  CUSTOM_ATTRIBUTES:loyalty_tier::STRING as loyalty_tier,
  EFF_DT,
  END_DT
FROM USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED
WHERE USER_ID = 'user_123'
  AND EFF_DT >= DATEADD(month, -6, CURRENT_TIMESTAMP())
ORDER BY EFF_DT DESC;
```

### Combiner attributs par défaut et attributs personnalisés {#combining-default-and-custom-attributes}

```sql
-- Get a complete user profile with both default and custom attributes
SELECT
  d.EXTERNAL_USER_ID,
  d.FIRST_NAME,
  d.LAST_NAME,
  d.EMAIL_ADDRESS,
  d.COUNTRY,
  c.CUSTOM_ATTRIBUTES:subscription_status::STRING as subscription_status,
  c.CUSTOM_ATTRIBUTES:lifetime_value::NUMBER as lifetime_value,
  c.CUSTOM_ATTRIBUTES:last_purchase_date::DATE as last_purchase_date
FROM USER_DEFAULT_ATTRIBUTES_VIEW_SHARED d
LEFT JOIN USER_CUSTOM_ATTRIBUTES_VIEW_SHARED c
  ON d.USER_ID = c.USER_ID
WHERE d.EXTERNAL_USER_ID = 'customer_456';
```

### Identifier les clients à forte valeur {#finding-high-value-customers}

```sql
-- Identify users with high lifetime value who are at risk of churning
SELECT
  d.EXTERNAL_USER_ID,
  d.EMAIL_ADDRESS,
  c.CUSTOM_ATTRIBUTES:lifetime_value::NUMBER as lifetime_value,
  c.CUSTOM_ATTRIBUTES:days_since_last_purchase::NUMBER as days_since_last_purchase
FROM USER_DEFAULT_ATTRIBUTES_VIEW_SHARED d
JOIN USER_CUSTOM_ATTRIBUTES_VIEW_SHARED c
  ON d.USER_ID = c.USER_ID
WHERE c.CUSTOM_ATTRIBUTES:lifetime_value::NUMBER > 1000
  AND c.CUSTOM_ATTRIBUTES:days_since_last_purchase::NUMBER > 90
ORDER BY c.CUSTOM_ATTRIBUTES:lifetime_value::NUMBER DESC;
```

## Bonnes pratiques {#best-practices}

### Utilisation recommandée des requêtes {#recommended-query-usage}

| Cas d'usage | Vues recommandées | Remarques |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **Requêtes générales** ne nécessitant pas de mises à jour récentes | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` et `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` | Exécution rapide, avec des données datant de 12 heures au maximum. |
| Requêtes nécessitant les **derniers attributs utilisateur** | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` et `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` | Fournit des mises à jour quasi en temps réel, mais peut être plus lent pour les grands ensembles de données. |
| **Suivi historique** des changements d'attributs | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` et `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED` | Enregistre les changements d'attributs avec une granularité de 12 heures. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Utilisation recommandée des requêtes" }

### Considérations relatives aux performances {#performance-considerations}

* Les requêtes sur `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` ou `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` devraient aboutir en moins de 10 secondes pour les grands ensembles de données (~1 milliard d'utilisateurs) sur un grand entrepôt.
* Les requêtes sur `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` ou `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED ` pour un seul utilisateur aboutissent en moins d'une minute, mais sont peu performantes sans filtrage par `USER_ID`.
* Les requêtes portant sur plus de 100 millions d'utilisateurs dans `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` ou `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` peuvent prendre plusieurs minutes en raison de l'agrégation par utilisateur.