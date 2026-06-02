---
nav_title: "POST : Renommer des ID externes"
article_title: "POST : Renommer l'ID externe"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Renommer des ID externes."

---
{% api %}
# Renommer des ID externes {#rename-external-id}
{% apimethod post %}
/users/external_ids/rename
{% endapimethod %}

> Utilisez cet endpoint pour renommer les ID externes de vos utilisateurs.

Vous pouvez envoyer jusqu'à 50 objets de renommage par requête.

Cet endpoint définit un nouvel `external_id` (principal) pour l'utilisateur et rend son `external_id` existant obsolète. Cela signifie que l'utilisateur peut être identifié par l'un ou l'autre des `external_id` jusqu'à ce que celui qui est obsolète soit supprimé. Le fait de disposer de plusieurs ID externes permet de prévoir une période de migration, de sorte que les versions antérieures de vos applications qui utilisent l'ancien schéma de dénomination des ID externes ne soient pas interrompues.

Une fois que votre ancien schéma de nommage n'est plus utilisé, nous vous recommandons vivement de supprimer les ID externes obsolètes à l'aide de l'[endpoint `/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/).

{% alert warning %}
Assurez-vous de supprimer les ID externes obsolètes à l'aide de l'endpoint `/users/external_ids/remove` plutôt que `/users/delete`. L'envoi d'une requête à `/users/delete` avec l'ID externe obsolète supprime entièrement le profil utilisateur et cette action ne peut pas être annulée.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l'autorisation `users.external_ids.rename`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## Corps de la requête {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_id_renames" : (required, array of external ID rename objects)
}
```

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `external_id_renames` | Requis | Tableau d'objets de renommage d'identifiants externes | Consultez l'exemple de requête et les limitations suivantes concernant la structure de l'objet de renommage d'identifiant externe. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

Notez ce qui suit :

- Le `current_external_id` doit être l'ID principal de l'utilisateur et ne peut pas être un ID obsolète.
- Le `new_external_id` ne doit pas être déjà utilisé en tant qu'ID principal ou ID obsolète.
- Le `current_external_id` et le `new_external_id` ne peuvent pas être identiques.

## Exemple de requête {#request-example}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/rename' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_id_renames" :[
    {
      "current_external_id": "existing_external_id",
      "new_external_id" : "new_external_id"
    }
  ]
}'
```

## Réponse {#response}

La réponse confirmera tous les renommages réussis, ainsi que les renommages échoués avec les erreurs associées. Les messages d'erreur dans le champ `rename_errors` font référence à l'index de l'objet dans le tableau de la requête d'origine.

```
{
  "message" : (string) status message,
  "external_ids" : (array of strings) successful rename operations,
  "rename_errors": (array of arrays) <minor error message>
}
```

Le champ `message` renverra `success` pour toute requête valide. Des erreurs plus spécifiques sont capturées dans le tableau `rename_errors`. Le champ `message` renvoie une erreur dans les cas suivants :

- Clé API non valide
- Tableau `external_id_renames` vide
- Tableau `external_id_renames` contenant plus de 50 objets
- Limite de débit atteinte (plus de 1 000 requêtes par minute)

## Foire aux questions {#frequently-asked-questions}

### Cela a-t-il un impact sur les MAU ? {#does-this-impact-mau}
Non, car le nombre d'utilisateurs reste le même ; ils ont simplement un nouvel `external_id`.

### Le comportement des utilisateurs change-t-il rétroactivement ? {#does-user-behavior-change-historically}
Non, car l'utilisateur est toujours le même et tout son comportement historique lui reste associé.

### Peut-on l'exécuter sur des espaces de travail de développement ou de mise à l'essai ? {#can-it-be-run-on-development-or-staging-workspaces}
Oui. En fait, nous vous recommandons vivement d'effectuer un test de migration sur un espace de travail de développement ou de mise à l'essai, et de vous assurer que tout s'est bien déroulé avant d'exécuter la migration sur les données de production.

### Cette fonctionnalité enregistre-t-elle des points de données ? {#does-this-log-data-points}
Cette fonctionnalité n'enregistre pas de points de données.

### Quel est le délai d'obsolescence recommandé ? {#what-is-the-recommended-deprecation-period}
Nous n'imposons pas de limite stricte quant à la durée pendant laquelle vous pouvez conserver des ID externes obsolètes, mais nous vous recommandons vivement de les supprimer dès qu'il n'est plus nécessaire de référencer les utilisateurs par l'ID obsolète.

{% endapi %}