---
nav_title: "Objet alias d'utilisateur"
article_title: Objet alias d'utilisateur API
page_order: 11
page_type: reference
description: "Cet article de référence explique les différents composants de l'objet alias d'utilisateur."

---

# Objet alias d'utilisateur {#user-alias-object}

> Un alias sert d'identifiant utilisateur unique alternatif. En utilisant un objet alias d'utilisateur, vous pouvez définir un identifiant cohérent pour l'analytique qui suivra un utilisateur donné avant et après qu'il se soit connecté à une application mobile ou à un site web. Vous pouvez également utiliser cet objet pour ajouter les identifiants utilisés par un fournisseur tiers aux utilisateurs de votre entreprise afin de faciliter le rapprochement de vos données en externe.

L'objet alias d'utilisateur se compose de deux parties : un `alias_name` pour l'identifiant lui-même et un `alias_label` indiquant le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais un seul `alias_name` par `alias_label`.

Cet objet est fréquemment utilisé dans tous nos endpoints, et souvent au sein d'autres objets.

## Corps de l'objet {#object-body}

```json
{
  "user_alias" : {
    "alias_name" : (required, string),
    "alias_label" : (required, string)
  }
}
```

| Champ | Type de données | Exemple | Description |
|---|---|---|---|
| `alias_name` | Chaîne de caractères | `john_doe_123` | Un identifiant unique pour l'utilisateur, tel qu'un ID provenant d'un système tiers. Cette valeur doit être non vide et ne pas dépasser 236 octets. |
| `alias_label` | Chaîne de caractères | `crm_id` | Une chaîne de caractères personnalisée non vide qui définit le type d'alias. Cette valeur n'est pas limitée à des options spécifiques. Vous pouvez utiliser n'importe quelle étiquette pertinente, telle que `email_id`, `amplitude_id`, `salesforce_lead_id`, ou toute autre valeur correspondant à votre cas d'utilisation. Cette valeur ne doit pas dépasser 236 octets. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Object body" }
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Object body" }

### Exemple {#example}

```json
{
  "user_alias": {
    "alias_name": "john_doe_123",
    "alias_label": "crm_id"
  },
  "external_id": "user_456"
}
```

Dans cet exemple, `crm_id` est une étiquette personnalisée indiquant que l'alias représente un identifiant de système CRM.

### Exemple supplémentaire {#additional-example}

```json
{
  "user_alias": {
    "alias_name": "a9f3c102",
    "alias_label": "amplitude_id"
  }
}
```

Dans cet exemple, `amplitude_id` est une valeur d'étiquette possible. Vous pouvez également utiliser des étiquettes telles que `email_id` ou `salesforce_lead_id`, ou toute autre étiquette personnalisée correspondant à votre schéma d'identifiants.