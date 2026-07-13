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

Cet endpoint définit un nouvel `external_id` (principal) pour l'utilisateur et rend son `external_id` existant obsolète. Cela signifie que l'utilisateur peut être identifié par l'un ou l'autre des `external_id` jusqu'à ce que celui qui est obsolète soit supprimé. Le fait de disposer de plusieurs ID externes permet de prévoir une période de migration, de sorte que les versions antérieures de vos applications qui utilisent l'ancien schéma de dénomination des ID externes ne soient pas interrompues. Le profil reste pleinement fonctionnel sous les deux identifiants pendant la fenêtre de migration : le SDK Braze, la REST API et les pipelines de communication peuvent continuer à référencer l'utilisateur par l'un ou l'autre des ID jusqu'à ce que celui qui est obsolète soit explicitement supprimé.

Une fois que votre ancien schéma de nommage n'est plus utilisé, nous vous recommandons vivement de supprimer les ID externes obsolètes à l'aide de l'[endpoint `/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove).

{% alert warning %}
Assurez-vous de supprimer les ID externes obsolètes à l'aide de l'endpoint `/users/external_ids/remove` plutôt que `/users/delete`. L'envoi d'une requête à `/users/delete` avec l'ID externe obsolète supprime entièrement le profil utilisateur et cette action ne peut pas être annulée.
{% endalert %}

## Fonctionnement du renommage {#how-renaming-works}

Lorsque vous appelez cet endpoint, il attribue un nouvel `external_id` principal à un profil utilisateur tout en convertissant simultanément l'ancien `external_id` principal en un ID externe obsolète. Après un renommage réussi, le profil utilisateur contient exactement un `external_id` principal (la nouvelle valeur) et un ID externe obsolète (l'ancienne valeur).

Les appels de renommage successifs sur le même profil sont autorisés : chaque renommage crée un ID externe obsolète supplémentaire, de sorte qu'un profil peut accumuler un `external_id` principal et plusieurs ID externes obsolètes au fil du temps. Cependant, la valeur de `new_external_id` ne doit pas déjà exister sur un profil Braze, que ce soit en tant qu'ID principal ou en tant qu'ID externe obsolète.

L'endpoint n'enregistre pas de points de données et n'affecte pas le nombre de MAU. Toutes les données historiques de l'utilisateur (événements, achats, attributs, engagement dans les campagnes) restent rattachées au même profil.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key) avec l'autorisation `users.external_ids.rename`.

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

| Paramètre | Obligatoire | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `external_id_renames` | Obligatoire | Tableau d'objets de renommage d'identifiants externes | Consultez l'exemple de requête et les limitations suivantes concernant la structure de l'objet de renommage d'identifiant externe. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

Notez ce qui suit :

- Le `current_external_id` doit être l'ID principal de l'utilisateur et ne peut pas être un ID obsolète. Si la valeur transmise en tant que `current_external_id` est elle-même un ID obsolète sur le profil, l'appel échouera. Avant de réessayer un renommage échoué, utilisez l'[endpoint `/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) pour confirmer quel ID est actuellement le principal.
- Le `new_external_id` ne doit pas être déjà utilisé en tant qu'ID principal ou ID obsolète. Tenter de renommer vers un ID déjà stocké en tant qu'ID obsolète renvoie une erreur « new_external_id is already in use ».
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

## Migrations en masse {#bulk-migrations}

Pour les migrations impliquant de grandes populations d'utilisateurs, regroupez les utilisateurs par lots de 50 maximum et envoyez chaque lot sous forme d'appel API distinct. L'endpoint est soumis à une limite de débit de 1 000 requêtes par minute. À la taille de lot maximale (50 objets par requête), cela permet jusqu'à 50 000 renommages d'utilisateurs par minute.

Chaque objet de renommage dans le lot est traité indépendamment. Un échec sur un objet ne bloque pas les autres dans la même requête. Le corps de la réponse distingue les renommages réussis (listés dans le tableau `external_ids`) des échecs (listés dans le tableau `rename_errors` avec une référence d'index vers la position de l'objet en échec dans le tableau de la requête).

Lors de l'exécution de migrations en masse :

1. Parcourez l'ensemble de la population d'utilisateurs par lots de 50 paires maximum.
2. À chaque réponse, inspectez à la fois `external_ids` (succès) et `rename_errors` (échec) pour identifier les utilisateurs qui doivent faire l'objet d'une nouvelle tentative.
3. Collectez les objets en échec et planifiez des lots de nouvelle tentative séparément. Les causes d'échec courantes incluent le fait que le `new_external_id` est déjà utilisé, ou que le `current_external_id` est un ID obsolète plutôt qu'un ID principal.
4. Enregistrez les succès et les échecs dans vos propres registres afin que l'état de la migration soit suivi en dehors de Braze.

## Vérification de l'ID externe actuel {#verifying-the-current-external-id}

Pendant une migration, vous pouvez avoir besoin de confirmer quel ID externe est l'identifiant principal actif sur un profil donné, par exemple pour déterminer si un utilisateur spécifique a déjà été migré, ou pour résoudre un problème de renommage échoué. Utilisez l'[endpoint `/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) à cette fin.

L'endpoint d'exportation résout à la fois les ID externes principaux et obsolètes vers le même profil sous-jacent et renvoie toujours l'`external_id` principal actuel dans la réponse. Cela signifie que vous pouvez interroger n'importe quel identifiant connu pour un utilisateur, ancien ou nouveau, et la réponse contiendra l'ID principal canonique. C'est un moyen fiable de déterminer l'état de la migration.

Pour vérifier uniquement l'ID externe (plutôt que de récupérer le profil complet), transmettez `fields_to_export` avec uniquement le champ `external_id`.

## Flux de travail de migration recommandé {#recommended-migration-workflow}

Pour la plupart des cas d'usage de migration, la séquence recommandée est la suivante :

1. **Tester en environnement de pré-production** — Exécutez le flux complet de renommage et de vérification sur un espace de travail de développement ou de pré-production avant de toucher à la production.
2. **Renommer par lots** — Utilisez l'endpoint `/users/external_ids/rename` par lots de 50 maximum, en traitant les `rename_errors` à chaque réponse et en mettant en file d'attente les paires en échec pour nouvelle tentative.
3. **Vérifier** — Après chaque lot (ou à la fin de la migration), vérifiez ponctuellement les profils à l'aide de `/users/export/ids` pour confirmer que l'`external_id` principal attendu est bien défini.
4. **Maintenir la fenêtre d'obsolescence** — Conservez les ID externes obsolètes actifs aussi longtemps qu'un système (y compris les versions d'applications héritées en circulation) peut encore référencer les anciens ID. Ne précipitez pas cette étape.
5. **Supprimer les ID obsolètes** — Une fois que tous les systèmes utilisent les nouveaux ID, utilisez [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove) par lots de 50 maximum pour effectuer le nettoyage.

Si vous migrez également votre intégration SDK (par exemple, en modifiant la valeur transmise à `changeUser`), coordonnez le renommage côté API avec le calendrier de publication de l'application afin que le nouvel ID externe soit utilisé à la fois côté serveur et côté client avant que les ID obsolètes ne soient supprimés.

## Foire aux questions {#frequently-asked-questions}

### Cela a-t-il un impact sur les MAU ? {#does-this-impact-mau}
Non, car le nombre d'utilisateurs reste le même ; ils ont simplement un nouvel `external_id`.

### Le comportement des utilisateurs change-t-il rétroactivement ? {#does-user-behavior-change-historically}
Non, car l'utilisateur est toujours le même et tout son comportement historique lui reste associé.

### Peut-on l'exécuter sur des espaces de travail de développement ou de pré-production ? {#can-it-be-run-on-development-or-staging-workspaces}
Oui. En fait, nous vous recommandons vivement d'effectuer un test de migration sur un espace de travail de développement ou de pré-production, et de vous assurer que tout s'est bien déroulé avant d'exécuter la migration sur les données de production.

### Cette fonctionnalité enregistre-t-elle des points de données ? {#does-this-log-data-points}
Cette fonctionnalité n'enregistre pas de points de données.

### Quel est le délai d'obsolescence recommandé ? {#what-is-the-recommended-deprecation-period}
Nous n'imposons pas de limite stricte quant à la durée pendant laquelle vous pouvez conserver des ID externes obsolètes, mais nous vous recommandons vivement de les supprimer dès qu'il n'est plus nécessaire de référencer les utilisateurs par l'ID obsolète.

### Combien d'ID externes obsolètes un profil peut-il avoir ? {#how-many-deprecated-external-ids-can-a-profile-have}
Un profil utilisateur peut contenir un `external_id` principal et un nombre illimité d'ID externes obsolètes accumulés au fil des opérations de renommage successives. Il n'existe pas de limite documentée quant au nombre d'ID obsolètes qu'un seul profil peut contenir, mais Braze recommande de les supprimer dès qu'ils ne sont plus nécessaires.

{% endapi %}