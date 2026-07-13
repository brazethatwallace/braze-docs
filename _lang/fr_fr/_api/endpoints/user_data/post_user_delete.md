---
nav_title: "POST : Supprimer les utilisateurs"
article_title: "POST : Supprimer les utilisateurs"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Cet article décrit les détails de l'endpoint Braze pour supprimer des utilisateurs."

---
{% api %}
# Supprimer les utilisateurs {#delete-users}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/users/delete
{% endapimethod %}

> Utilisez cet endpoint pour supprimer un profil utilisateur en spécifiant un identifiant utilisateur connu.

Jusqu'à 50 `external_ids`, `user_aliases`, `braze_ids`, `email_addresses` ou `phone_numbers` peuvent être inclus dans une seule requête. Un seul type parmi `external_ids`, `user_aliases`, `braze_ids`, `email_addresses` ou `phone_numbers` peut être inclus dans une seule requête.

Si vous avez un cas d'utilisation qui ne peut pas être résolu par la suppression en bloc d'utilisateurs via l'API, contactez l'[équipe d'assistance Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) pour obtenir de l'aide.

{% alert warning %}
La suppression de profils utilisateur est irréversible. Cette action supprime définitivement les utilisateurs, ce qui peut entraîner des écarts dans vos données. Pour en savoir plus, consultez la section [Effets de la suppression de profils utilisateur](#effects-of-deleting-user-profiles).
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key) avec l'autorisation `users.delete`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='users delete' %}

## Corps de la requête {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_ids" : (optional, array of string) External IDs to be deleted,
  "user_aliases" : (optional, array of user alias objects) User aliases to be deleted,
  "braze_ids" : (optional, array of string) Braze user identifiers to be deleted,
  "email_addresses": (optional, array of string) User emails to be deleted,
  "phone_numbers": (optional, array of string) User phone numbers to be deleted
}
```
### Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
|-------------------|----------|----------------------------|--------------------------------------------------------------------------------------------------|
| `external_ids` | Facultatif | Tableau de chaînes de caractères | Identifiants externes à supprimer. |
| `user_aliases` | Facultatif | Tableau d'objets alias d'utilisateur | [Alias d'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object) à supprimer. |
| `braze_ids` | Facultatif | Tableau de chaînes de caractères | Identifiants utilisateur Braze à supprimer. |
| `email_addresses` | Facultatif | Tableau de chaînes de caractères | Adresses e-mail des utilisateurs à supprimer. Pour plus d'informations, reportez-vous à la section [Suppression d'utilisateurs par e-mail](#deleting-users-by-email). |
| `phone_numbers` | Facultatif | Tableau de chaînes de caractères | Numéros de téléphone des utilisateurs à supprimer. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

### Suppression d'utilisateurs par adresses e-mail et numéros de téléphone {#deleting-users-by-email-addresses-and-phone-numbers}

Si une adresse e-mail ou un numéro de téléphone est spécifié comme identifiant, une valeur supplémentaire `prioritization` est requise dans l'identifiant. `prioritization` doit être un tableau ordonné qui spécifie quel utilisateur supprimer lorsque plusieurs utilisateurs correspondent. La suppression n'aura donc pas lieu si plus d'un utilisateur correspond à une priorisation donnée.

Les valeurs autorisées pour le tableau sont les suivantes :

- `identified`
- `unidentified`
- `most_recently_updated` (donne la priorité à l'utilisateur mis à jour le plus récemment)

Une seule des options suivantes peut figurer à la fois dans le tableau `prioritization` :

- `identified` donne la priorité à un utilisateur possédant un `external_id`
- `unidentified` donne la priorité à un utilisateur ne possédant pas d'`external_id`

## Exemple de requête {#example-request}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "external_ids": ["external_identifier1", "external_identifier2"],
  "braze_ids": ["braze_identifier1", "braze_identifier2"],
  "user_aliases": [
    {
      "alias_name": "user_alias1", "alias_label": "alias_label1"
    },
    {
      "alias_name": "user_alias2", "alias_label": "alias_label2"
    }
  ],
  "email_addresses": [
    {
      "email": "john.smith@example.com",
      "prioritization": ["unidentified", "most_recently_updated"]
    }
  ]
}'
```

## Réponse {#response}

```json
{
  "deleted" : (required, integer) number of user IDs queued for deletion
}
```

## Effets de la suppression de profils utilisateur {#effects-of-deleting-user-profiles}

Lorsque vous supprimez un utilisateur avec cet endpoint, les événements suivants se produisent :

- Le profil utilisateur est supprimé (mis à null).
- Le nombre d'utilisateurs de l'espace de travail (tel que le nombre total d'utilisateurs sur la [page d'accueil analytique]({{site.baseurl}}/user_guide/analytics/dashboards/home)) est mis à jour pour tenir compte des utilisateurs supprimés.
- L'utilisateur supprimé est toujours comptabilisé dans le pourcentage de conversion agrégé. Les compteurs d'événements personnalisés et d'achats ne sont pas mis à jour pour les utilisateurs supprimés.

### Profils multiples partageant une même adresse e-mail {#multiple-profiles-with-a-shared-email-address}

Pour fusionner des profils utilisateur partageant la même adresse e-mail, appelez l'[endpoint `/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge).

## Résolution des problèmes {#troubleshooting}

### Une réponse de succès a été renvoyée mais l'utilisateur apparaît toujours {#a-success-response-was-returned-but-the-user-still-appears}

Une réponse réussie confirme que la requête a été mise en file d'attente, et non que la suppression est terminée. La suppression s'effectue généralement en moins d'une seconde, mais la propagation à travers tous les caches peut prendre jusqu'à cinq minutes. Si vous recherchez immédiatement l'utilisateur dans le tableau de bord ou exportez ses données via l'API, il est possible que des résultats apparaissent encore pendant cette fenêtre de propagation.

Si l'utilisateur existe toujours après plusieurs minutes, vérifiez que l'identifiant de votre requête correspond bien au profil réel de l'utilisateur :

- **Tableau `external_ids` :** confirmez que chaque valeur correspond exactement à l'ID externe d'un utilisateur.
- **`braze_id` :** vous pouvez trouver le `braze_id` d'un utilisateur en exportant ses données avec l'[endpoint `/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) ou en exportant un segment au format CSV (où le `braze_id` apparaît sous le nom « Appboy ID »).
- **Profils avec alias uniquement ou e-mail uniquement :** si le profil ne possède pas d'`external_id`, créez un segment filtrant sur **External User ID is blank** combiné avec l'adresse e-mail ou le numéro de téléphone connu, puis exportez au format CSV pour récupérer le `braze_id`.

Pour confirmer qu'un utilisateur a bien été supprimé, appelez l'[endpoint `/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) en utilisant le même type d'identifiant que celui utilisé dans la requête de suppression (par exemple, en incluant la valeur dans `external_ids`, `braze_id` ou `user_aliases`). Si l'utilisateur n'existe plus, la réponse contient `"users": []` et peut inclure `"invalid_user_ids"` listant cet identifiant.

{% endapi %}