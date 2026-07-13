---
nav_title: "POST : Fusionner les utilisateurs"
article_title: "POST : Fusionner les utilisateurs"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Fusionner les utilisateurs."

---
{% api %}
# Fusionner les utilisateurs {#merge-users}
{% apimethod post %}
/users/merge
{% endapimethod %}

> Utilisez cet endpoint pour fusionner un utilisateur avec un autre utilisateur.

Vous pouvez spécifier jusqu'à 50 fusions par requête. Cet endpoint est asynchrone.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d262b86d-cf84-46e2-b9d0-f882bb7078de {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key) avec l'autorisation `users.merge`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='users merge' %}

## Corps de la requête {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "merge_updates" : (required, array of objects)
}
```

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `merge_updates` | Requis | Tableau | Un tableau d'objets. Chaque objet doit contenir un objet `identifier_to_merge` et un objet `identifier_to_keep`, qui doivent chacun référencer un utilisateur par `external_id`, `user_alias`, `phone` ou `email`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête" }

### Comportement de fusion {#merge-behavior}

Le comportement documenté ci-dessous s'applique à toutes les fonctionnalités de Braze qui **ne sont pas** alimentées par Snowflake. Les fusions d'utilisateurs ne seront pas prises en compte pour l'onglet **Messaging History**, les extensions de segments, le générateur de requêtes et Currents.

{% alert important %}
Cet endpoint ne garantit pas l'ordre de mise à jour des objets `merge_updates`.
{% endalert %}

Cet endpoint fusionne les champs suivants s'ils ne sont pas trouvés chez l'utilisateur cible.

- Prénom
- Nom
- Adresses e-mail (à moins qu'elles ne soient [chiffrées]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption))
- Genre
- Date de naissance
- Numéro de téléphone
- Fuseau horaire
- Ville d'origine
- Pays
- Langue
- Informations sur l'appareil
- Nombre de sessions (la somme des sessions des deux profils)
- Date de la première session (Braze sélectionne la date la plus ancienne des deux)
- Date de la dernière session (Braze sélectionne la date la plus récente des deux)
- Attributs personnalisés (Braze conserve les attributs personnalisés existants sur le profil cible et inclut les attributs personnalisés qui n'existaient pas sur le profil cible)
- Données d'événements personnalisés et d'événements d'achat
- Propriétés d'événements personnalisés et d'événements d'achat pour la segmentation « X fois en Y jours » (où X<=50 et Y<=30)
- Résumé des événements personnalisés segmentables
  - Nombre d'événements (la somme des deux profils)
  - Date de première occurrence de l'événement (Braze sélectionne la date la plus ancienne des deux)
  - Date de dernière occurrence de l'événement (Braze sélectionne la date la plus récente des deux)
- Total des achats in-app en centimes (la somme des deux profils)
- Nombre total d'achats (la somme des deux profils)
- Date du premier achat (Braze sélectionne la date la plus ancienne des deux)
- Date du dernier achat (Braze sélectionne la date la plus récente des deux)
- Résumés des applications
- Champs Last_X_at (Braze met à jour les champs si ceux du profil orphelin sont plus récents)
- Données d'interaction de Campaign (Braze sélectionne les champs de date les plus récents)
- Résumés de flux de travail (Braze sélectionne les champs de date les plus récents)
- Historique des messages et de l'engagement des messages
- Braze fusionne les données de session uniquement si l'application est présente sur les deux profils utilisateurs.

{% alert note %}
Lors de la fusion d'utilisateurs, l'utilisation de l'endpoint `/users/merge` fonctionne de la même manière que la [méthode `changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser).
{% endalert %}

Braze gère trois types d'utilisateurs différemment lors de la fusion : les utilisateurs marqués pour suppression, les utilisateurs test et les utilisateurs du groupe de contrôle global. Pour plus de détails, consultez [Comportement de fusion des utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior).

#### Comportement des dates d'événements personnalisés et d'événements d'achat {#custom-event-date-and-purchase-event-date-behavior}

Ces champs fusionnés mettent à jour les filtres « pour X événements en Y jours ». Pour les événements d'achat, ces filtres incluent « nombre d'achats en Y jours » et « argent dépensé au cours des Y derniers jours ».

### Fusionner les utilisateurs par e-mail ou par numéro de téléphone {#merging-users-by-email-or-phone-number}

Si un `email` ou un `phone` est spécifié comme identifiant, vous devez inclure une valeur `prioritization` supplémentaire dans l'identifiant. La `prioritization` doit être un tableau ordonné indiquant quel utilisateur fusionner si plusieurs utilisateurs sont trouvés. Cela signifie que si plusieurs utilisateurs correspondent à partir d'une priorisation, la fusion n'aura pas lieu.

Les valeurs autorisées pour le tableau sont les suivantes :

- `identified`
- `unidentified`
- `most_recently_updated` (donne la priorité à l'utilisateur le plus récemment mis à jour)
- `least_recently_updated` (donne la priorité à l'utilisateur le moins récemment mis à jour)

Une seule des options suivantes peut exister à la fois dans le tableau de priorisation :

- `identified` donne la priorité à un utilisateur ayant un `external_id`
- `unidentified` donne la priorité à un utilisateur n'ayant pas d'`external_id`

{% alert important %}
Si les deux profils ont des numéros de téléphone invalides, Braze ne les fusionne pas. Les numéros invalides ne sont pas stockés au format E.164, et la tâche de fusion ne combine pas ces profils. L'endpoint renvoie tout de même `202 Accepted` avec un message de succès, de sorte que la réponse HTTP n'indique pas que la fusion a été ignorée. Corrigez les numéros de téléphone sur l'un ou les deux profils avant de procéder à la fusion.
{% endalert %}

## Exemples de requêtes {#example-requests}

### Requête de base {#basic-request}

Voici un corps de requête basique pour illustrer le modèle de la requête.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "external_id": "old-user1"
      },
      "identifier_to_keep": {
        "external_id": "current-user1"
      }
    },
    {
      "identifier_to_merge": {
        "email": "user1@example.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep":  {
        "email": "user2@example.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    },
    {
      "identifier_to_merge": {
        "user_alias": {
          "alias_name": "old-user2@example.com",
          "alias_label": "email"
        }
      },
      "identifier_to_keep": {
        "user_alias": {
          "alias_name": "current-user2@example.com",
          "alias_label": "email"
        }
      }
    }
  ]
}'
```

### Fusionner un utilisateur non identifié {#merging-unidentified-user}

La requête suivante fusionnerait l'utilisateur non identifié le plus récemment mis à jour avec l'adresse e-mail `john.smith@example.com` avec l'utilisateur ayant l'ID externe `john`. Dans cet exemple, l'utilisation de `most_recently_updated` filtre la requête à un seul utilisateur non identifié. Ainsi, s'il y avait deux utilisateurs non identifiés avec cette adresse e-mail, un seul serait fusionné avec l'utilisateur disposant de l'ID externe `john`.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@example.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

### Fusionner un utilisateur non identifié avec un utilisateur identifié {#merging-unidentified-user-into-identified-user}

L'exemple suivant fusionne l'utilisateur non identifié le plus récemment mis à jour avec l'adresse e-mail `john.smith@example.com` avec l'utilisateur identifié le plus récemment mis à jour avec l'adresse e-mail `john.smith@example.com`.

L'utilisation de `most_recently_updated` filtre les requêtes à un seul utilisateur (un utilisateur non identifié pour `identifier_to_merge` et un utilisateur identifié pour `identifier_to_keep`).

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@example.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "email": "john.smith@example.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    }
  ]
}'
```

### Fusionner un utilisateur non identifié sans inclure la priorisation most_recently_updated {#merging-an-unidentified-user-without-including-the-most_recently_updated-prioritization}

S'il existe deux utilisateurs non identifiés avec l'adresse e-mail `john.smith@example.com`, cette requête ne fusionne aucun utilisateur, car il y a deux utilisateurs non identifiés avec cette adresse e-mail. Cette requête ne fonctionne que s'il n'y a qu'un seul utilisateur non identifié avec l'adresse e-mail `john.smith@example.com`.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@example.com",
        "prioritization": ["unidentified"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

## Réponse {#response}

Deux codes de statut de réponse existent pour cet endpoint : `202` et `400`.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `202` pourrait renvoyer le corps de réponse suivant.

```json
{
  "message": "success"
}
```

### Exemple de réponse en erreur {#example-error-response}

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la section [Résolution des problèmes](#troubleshooting) pour plus d'informations concernant les erreurs que vous pourriez rencontrer.

```json
{
  "message": "'merge_updates' must be an array of objects"
}
```

## Résolution des problèmes {#troubleshooting}

### Une réponse de succès a été renvoyée mais l'utilisateur fusionné est toujours consultable {#a-success-response-was-returned-but-the-merged-user-is-still-searchable}

Une réponse de succès confirme que la requête a été acceptée, mais l'opération de fusion comporte deux étapes : la fusion des profils, puis la suppression du profil source. De ce fait, le profil `identifier_to_merge` peut rester consultable dans le tableau de bord pendant une courte période après une réponse de succès. Il s'agit d'un comportement attendu — patientez quelques minutes, puis vérifiez que la fusion est terminée.

Si l'utilisateur fusionné existe toujours après plusieurs minutes, vérifiez que les identifiants de votre requête sont corrects et appartiennent à des utilisateurs du même espace de travail que la clé API utilisée pour la requête.

### Référence des erreurs {#error-reference}

Le tableau suivant répertorie les messages d'erreur possibles.

| Erreur | Résolution des problèmes |
| --- | --- |
| `'merge_updates' must be an array of objects` | Vérifiez que `merge_updates` est un tableau d'objets. |
| `a single request may not contain more than 50 merge updates` | Vous pouvez spécifier jusqu'à 50 fusions dans une seule requête. |
| `identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, 'email' property that is a string, or 'phone' property that is a string` | Vérifiez les identifiants dans votre requête. |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | Vérifiez que `merge_updates` ne contient que les deux objets `identifier_to_merge` et `identifier_to_keep`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }

{% endapi %}