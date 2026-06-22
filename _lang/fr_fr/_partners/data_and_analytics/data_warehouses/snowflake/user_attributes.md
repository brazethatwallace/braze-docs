---
nav_title: "Attributs du profil utilisateur"
article_title: Vues d'attributs d'utilisateurs dans Snowflake
page_order: 10
page_type: partner
search_tag: Partner
toc_headers: h2
---

# Attributs du profil utilisateur {#user-profile-attributes}

> Cette page sert de référence pour les vues d'attributs par défaut et personnalisés dans Snowflake. Il existe trois vues pour les attributs par défaut et trois vues pour les attributs personnalisés, chacune étant conçue pour un cas d'utilisation spécifique avec ses propres considérations en matière de performances.

## Parité des données avec le tableau de bord {#data-parity-with-the-dashboard}

Dans de rares cas, les valeurs d'attributs par défaut et personnalisés dans les vues Snowflake de cette page peuvent ne pas correspondre à ce que vous voyez sur le profil d'un utilisateur dans le tableau de bord de Braze.

Par exemple, un attribut peut apparaître comme `NULL` dans Snowflake alors que le tableau de bord affiche une valeur pour cet utilisateur.

Si vous constatez des incohérences généralisées, contactez votre gestionnaire de la satisfaction client ou l'assistance Braze.

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

| Nom de la colonne | Type de données |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_USER_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL_ADDRESS` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE_NUMBER` | VARCHAR |
| `DOB` | VARCHAR |
| `TIMEZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `ARCHIVED` | BOOLEAN |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERDEFAULTATTRIBUTESVIEWSHARED schema" }


### Schéma `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` {#user_custom_attributes_view_shared-schema}

| Nom de la colonne | Type de données |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `EXTERNAL_USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANT |
| `ARCHIVED` | BOOLEAN |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERCUSTOMATTRIBUTESVIEWSHARED schema" }

## Vues de profil utilisateur en temps réel {#real-time-user-profile-views}

Ces vues fournissent des mises à jour quasi en temps réel des attributs du profil utilisateur, les données étant différées de 10 minutes au maximum après une mise à jour dans Braze.

  - `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`
  - `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`

### Utilisation

* Fournit des attributs utilisateur actualisés avec un délai minimal (~10 minutes).
* Utile pour les analyses en temps réel et les scénarios nécessitant des données récentes.
* **Considérations relatives aux performances :**
    * Les requêtes sur des utilisateurs individuels sont plus rapides (moins d'une minute avec un grand entrepôt).
    * Les requêtes sans filtre sur `USER_ID` nécessitent une agrégation pour tous les utilisateurs, ce qui allonge considérablement le temps d'exécution.
    * Les requêtes sur un grand ensemble de données (plus de 100 millions d'utilisateurs, par exemple) peuvent prendre plusieurs minutes.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### Schéma `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` {#user_latest_state_default_attributes_view_shared-schema}

| Nom de la colonne | Type de données |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `ARCHIVED` | BOOLEAN |
| `SF_UPDATED_AT` | TIMESTAMP_LTZ |
| `EXTERNAL_USER_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL_ADDRESS` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE_NUMBER` | VARCHAR |
| `DOB` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `TIMEZONE` | VARCHAR |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED schema" }

### Schéma `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` {#user_latest_state_custom_attribute_view_shared-schema}

| Nom de la colonne | Type de données |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `EXTERNAL_USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `ARCHIVED` | BOOLEAN |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `APP_ID` | VARCHAR |
| `CUSTOM_ATTRIBUTES` | OBJECT |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERLATESTSTATECUSTOMATTRIBUTEVIEWSHARED schema" }

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

| Nom de la colonne | Type de données |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_USER_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL_ADDRESS` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE_NUMBER` | VARCHAR |
| `DOB` | VARCHAR |
| `TIMEZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERDEFAULTATTRIBUTESHISTORYVIEWSHARED schema" }

### Schéma `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED` {#user_custom_attributes_history_view_shared-schema}

| Nom de la colonne | Type de données |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `EXTERNAL_USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANT |
| `ARCHIVED` | BOOLEAN |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERCUSTOMATTRIBUTESHISTORYVIEWSHARED schema" }

## Bonnes pratiques {#best-practices}

### Utilisation recommandée des requêtes {#recommended-query-usage}

| Cas d'utilisation | Vues recommandées | Remarques |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **Requêtes générales** ne nécessitant pas de mises à jour récentes | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` et `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` | Exécution rapide, avec des données datant de 12 heures au maximum. |
| Requêtes nécessitant les **derniers attributs utilisateur** | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` et `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` | Fournit des mises à jour quasi en temps réel, mais peut être plus lent pour les grands ensembles de données. |
| **Suivi historique** des changements d'attributs | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` et `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED` | Enregistre les changements d'attributs avec une granularité de 12 heures. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Utilisation recommandée des requêtes" }

### Considérations relatives aux performances {#performance-considerations}

* Les requêtes sur `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` ou `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` devraient aboutir en moins de 10 secondes pour les grands ensembles de données (~1 milliard d'utilisateurs) sur un grand entrepôt.
* Les requêtes sur `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` ou `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` pour un seul utilisateur aboutissent en moins d'une minute, mais sont peu performantes sans filtrage par `USER_ID`.
* Les requêtes portant sur plus de 100 millions d'utilisateurs dans `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` ou `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` peuvent prendre plusieurs minutes en raison de l'agrégation par utilisateur.