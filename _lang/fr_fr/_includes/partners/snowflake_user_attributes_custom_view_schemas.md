{% if include.schema == "history" %}

| Nom de la colonne | Type de donnée | Description |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | L'identifiant de votre espace de travail Braze |
| `USER_ID` | VARCHAR | L'identifiant utilisateur unique Braze |
| `APP_ID` | VARCHAR | L'application spécifique au sein de votre espace de travail |
| `EXTERNAL_USER_ID` | VARCHAR | Votre propre identifiant utilisateur (s'il est défini) |
| `TIME` | NUMBER | Horodatage unix (secondes) de la mise à jour du profil |
| `TIME_MS` | NUMBER | Horodatage unix (millisecondes) de la mise à jour du profil |
| `UPDATE_SOURCE` | VARCHAR | La source de la mise à jour de l'attribut (API, SDK, tableau de bord, etc.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Date de la dernière mise à jour des données dans Snowflake |
| `CUSTOM_ATTRIBUTES` | VARIANT | Objet JSON contenant tous les attributs personnalisés (paires clé-valeur) |
| `ARCHIVED` | BOOLEAN | Indique si le profil utilisateur est archivé |
| `EFF_DT` | TIMESTAMP_NTZ | Date d'effet : date à laquelle cet état d'attribut a commencé |
| `END_DT` | TIMESTAMP_NTZ | Date de fin : date à laquelle cet état d'attribut s'est terminé (NULL pour l'état actuel) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schéma USERCUSTOMATTRIBUTESHISTORYVIEWSHARED" }

{% elsif include.schema == "latest" %}

| Nom de la colonne | Type de donnée | Description |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | L'identifiant de votre espace de travail Braze |
| `USER_ID` | VARCHAR | L'identifiant utilisateur unique Braze |
| `EXTERNAL_USER_ID` | VARCHAR | Votre propre identifiant utilisateur (s'il est défini) |
| `TIME` | NUMBER | Horodatage unix (secondes) de la mise à jour du profil |
| `TIME_MS` | NUMBER | Horodatage unix (millisecondes) de la mise à jour du profil |
| `UPDATE_SOURCE` | VARCHAR | La source de la mise à jour de l'attribut (API, SDK, tableau de bord, etc.) |
| `ARCHIVED` | BOOLEAN | Indique si le profil utilisateur est archivé |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Date de la dernière mise à jour des données dans Snowflake |
| `APP_ID` | VARCHAR | L'application spécifique au sein de votre espace de travail |
| `CUSTOM_ATTRIBUTES` | OBJECT | Objet JSON contenant tous les attributs personnalisés (paires clé-valeur) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schéma USERLATESTSTATECUSTOMATTRIBUTEVIEWSHARED" }

{% alert note %}
Cette vue utilise le type `OBJECT` pour `CUSTOM_ATTRIBUTES` au lieu de `VARIANT`. Utilisez la même syntaxe d'accesseur JSON (`:attribute_name::TYPE`) pour interroger les attributs individuels.
{% endalert %}

{% endif %}