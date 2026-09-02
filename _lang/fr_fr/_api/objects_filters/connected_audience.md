---
nav_title: "Objet et filtre d'audience connectée"
article_title: Objet Audience connectée de l'API
page_order: 3
page_type: reference
description: "Cet article explique l'objet Audience connectée, son fonctionnement, ses cas d'usage et les différents filtres qui le composent."
---

# Objet Audience connectée {#connected-audience-object}

> Une audience connectée est un filtre d'audience dynamique que vous définissez directement dans votre requête API, ce qui vous permet de cibler les bons utilisateurs au moment de l'envoi sans avoir à créer ou gérer des Segments dans le tableau de bord de Braze.

Au lieu de créer à l'avance un Segment pour chaque combinaison d'audience possible, vous transmettez les critères de filtrage directement dans votre appel API. Selon l'endpoint, cet objet est transmis en tant que `audience` ou `custom_audience`. Braze évalue chaque utilisateur par rapport à ces critères en temps réel et délivre le message uniquement aux utilisateurs correspondants. Ainsi, une seule Campaign, un seul Canvas ou une seule définition de message API peut servir un nombre illimité de variations d'audience, entièrement piloté par votre logique métier.

## Comment ça fonctionne {#how-it-works}

1. Définissez votre message en créant soit une Campaign déclenchée par API, soit un Canvas dans le tableau de bord de Braze, ou définissez le contenu du message entièrement en ligne à l'aide des [objets de messagerie]({{site.baseurl}}/api/objects_filters#messaging-objects) dans votre requête API. Utilisez les [propriétés de déclenchement]({{site.baseurl}}/api/objects_filters/trigger_properties_object) ou le [contexte Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) pour la personnalisation dynamique.
2. Appelez un endpoint pris en charge et incluez vos filtres d'audience connectée dans le paramètre `audience`, ou dans `custom_audience` pour `/messages/live_activity/start`. Vous pouvez filtrer par attributs personnalisés, statut d'abonnement aux notifications push, statut d'abonnement aux e-mails et date de dernière utilisation de l'application.
3. Braze évalue les filtres au moment de l'envoi, en ne délivrant le message qu'aux utilisateurs correspondant à vos critères.

{% alert tip %}
Un `campaign_id` n'est pas requis lorsque vous utilisez le paramètre `audience`. Les endpoints [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) et [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages) vous permettent de définir le contenu du message en ligne sans Campaign préalablement créée. Toutefois, si vous souhaitez suivre les indicateurs au niveau de la Campaign (tels que les envois, les clics ou les rebonds) dans le tableau de bord, incluez un `campaign_id`.
{% endalert %}

Comme l'audience est définie par requête, vos systèmes back-end peuvent déclencher des messages contextuellement pertinents en réponse à n'importe quel événement métier (un changement de prix, une alerte météo, une mise à jour de score en direct or en ligne/en production/instantané) sans intervention dans le tableau de bord.

### Endpoints compatibles {#compatible-endpoints}

Vous pouvez utiliser l'objet d'audience connectée sur ces endpoints :

- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)
- [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) (utilise `custom_audience`)

Notez que le paramètre `audience` ne prend pas en charge les tableaux d'objets.

## Cas d'usage {#use-cases}

Utilisez les audiences connectées pour les scénarios où vos systèmes back-end détectent un événement et doivent notifier un ensemble d'utilisateurs déterminé dynamiquement :

| Catégorie | Exemple |
| --- | --- |
| Alertes météo | Un fournisseur de données météorologiques détecte un phénomène météorologique grave et envoie des notifications push aux utilisateurs dont l'attribut `preferred_city` correspond à la zone touchée. |
| Sports et événements en direct or en ligne/en production/instantané | Une application sportive envoie des mises à jour de scores en temps réel ou des alertes de match aux utilisateurs dont l'attribut `favorite_team` correspond à l'une des équipes en jeu. |
| Contenu et divertissement | Un service de streaming notifie les utilisateurs dont le tableau `favorite_shows` inclut le titre d'une série dès qu'un nouvel épisode est disponible. |
| E-commerce | Un détaillant en ligne envoie des alertes de baisse de prix ou de retour en stock aux utilisateurs dont le tableau `wishlisted_products` inclut l'ID du produit concerné. |
| Voyage | Une application de voyage envoie des notifications de retard de vol aux utilisateurs dont l'attribut `booked_flight` correspond au numéro de vol affecté. |
| Services financiers | Une plateforme de trading alerte les utilisateurs dont le tableau `watchlist` inclut un symbole boursier ayant franchi un seuil de prix. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cas d'usage" }

Dans chaque cas, une seule Campaign ou un seul message API-only gère toutes les variations. Votre back-end détermine les valeurs de filtre et les transmet dans la requête API, de sorte que vous n'avez pas besoin de créer un Segment ou une Campaign distinct(e) pour chaque produit, série, équipe ou emplacement.

## Exemple de requête {#example-request}

L'exemple suivant utilise l'endpoint [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) pour cibler les utilisateurs qui ont ajouté une émission spécifique à leurs favoris et qui ont accepté de recevoir des notifications push :

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_shows",
          "comparison": "includes_value",
          "value": "Example Show"
        }
      },
      {
        "push_subscription_status": {
          "comparison": "is",
          "value": "opted_in"
        }
      }
    ]
  },
  "trigger_properties": {
    "show_title": "Example Show",
    "episode_title": "Season 3, Episode 1",
    "deep_link": "https://example.com/shows/example-show/s3e1"
  },
  "broadcast": false
}
```

## Corps de l'objet {#object-body}

L'objet d'audience connectée est composé d'un seul filtre d'audience connectée ou de plusieurs filtres d'audience connectée combinés avec les opérateurs `AND` et `OR`.

**Exemple avec plusieurs filtres :**

```json
{
  "AND":
    [
      Connected Audience Filter,
      {
        "OR" :
          [
            Connected Audience Filter,
            Connected Audience Filter
          ]
      },
      Connected Audience Filter
    ]
}
```

## Filtres d'audience connectés {#connected-audience-filters}

Combinez plusieurs filtres à l'aide des opérateurs `AND` et `OR` pour créer un filtre d'audience connecté.

### Considérations {#considerations}

Les audiences connectées ne permettent pas de filtrer les utilisateurs en fonction de :

 - Attributs par défaut
 - Événements personnalisés
 - Segments
 - Événements d'engagement liés aux messages
 - Attributs personnalisés imbriqués

Pour utiliser ces filtres, nous vous recommandons de les intégrer dans un Segment d'audience, puis de spécifier ce Segment dans le paramètre `segment_id` de l'[endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters). Lorsque vous utilisez d'autres endpoints, vous devez d'abord ajouter le Segment à la Campaign ou au Canvas déclenchés par API dans le tableau de bord de Braze. Si vous devez filtrer sur des attributs imbriqués, utilisez plutôt un [Segment standard]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).


### Filtre d'attribut personnalisé {#custom-attribute-filter}

Ce filtre vous permet de segmenter en fonction d'un attribut personnalisé de l'utilisateur. Ces filtres contiennent jusqu'à trois champs :

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": (String) the name of the custom attribute to filter on,
      "comparison": (String) one of the allowed comparisons to make against the provided value,
      "value": (String, Numeric, Boolean) the value to be compared using the provided comparison
    }
}
```

#### Comparaisons autorisées par type de donnée {#allowed-comparisons-by-data-type}

Le type de donnée de l'attribut personnalisé détermine les comparaisons valides pour un filtre donné.

| Type d'attribut personnalisé | Comparaisons autorisées |
| ---------------------| --------------- |
| String | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist`, `is_any_of`, `is_none_of` |
| Array | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist`, `is_any_of`, `is_none_of` |
| Numeric | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| Boolean | `equals`, `not_equal`, `exists`, `does_not_exist` |
| Time | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparaisons autorisées par type de donnée" }

#### Précautions relatives aux comparaisons d'attributs {#attribute-comparison-caveats}

| Comparaison | Considérations supplémentaires |
| --- | --- |
| `value` | Le champ `value` n'est pas requis lorsque vous utilisez les comparaisons `exists` ou `does_not_exist`. `value` doit être une chaîne de caractères datetime au format ISO 8601 lorsque vous utilisez les comparaisons `before` et `after`. |
| `matches_regex` | Lorsque vous utilisez la comparaison `matches_regex`, la valeur transmise doit être une chaîne de caractères. Pour en savoir plus sur l'utilisation des expressions régulières avec Braze, consultez [Expressions régulières]({{site.baseurl}}/user_guide/audience/segments/regex) et [Types de données des attributs personnalisés]({{site.baseurl}}/developer_guide/analytics#custom-attribute-data-types). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Précautions relatives aux comparaisons d'attributs" }

#### Comparaisons multi-valeurs {#multi-value-comparisons}

Les opérateurs `is_any_of` et `is_none_of` permettent de comparer plusieurs valeurs en une seule opération. Ces comparaisons fonctionnent avec les attributs personnalisés de type string et de type array.

- `is_any_of` : correspond aux utilisateurs dont la valeur d'attribut est égale à l'une des valeurs fournies. Le champ `value` peut être une chaîne de caractères unique ou un tableau de chaînes de caractères.
- `is_none_of` : correspond aux utilisateurs dont la valeur d'attribut ne correspond à aucune des valeurs fournies. Le champ `value` peut être une chaîne de caractères unique ou un tableau de chaînes de caractères. Notez que les utilisateurs dont le profil ne possède pas cet attribut sont toujours éligibles à cette comparaison.

Pour les attributs de type array :

- `includes_value` peut également accepter un tableau de valeurs pour vérifier si le tableau de l'utilisateur contient l'une des valeurs spécifiées.
- Lorsque vous utilisez `is_any_of` ou `is_none_of` avec des attributs de type array, ils fonctionnent respectivement comme `includes_value` et `does_not_include_value`.

{% alert tip %}
Pour la correspondance multi-valeurs, utilisez `is_any_of` plutôt que `includes_value`.
{% endalert %}

#### Exemples d'attributs personnalisés {#custom-attribute-examples}

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": "eye_color",
      "comparison": "equals",
      "value": "blue"
    }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "last_purchase_time",
    "comparison": "less_than_x_days_ago",
    "value": 2
  }
}
```

#### Exemples de comparaisons multi-valeurs {#multi-value-comparison-examples}

##### `is_any_of` avec un tableau de chaînes de caractères {#is_any_of-with-an-array-of-strings}

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_color",
    "comparison": "is_any_of",
    "value": ["red", "blue", "green"]
  }
}
```

##### `is_none_of` avec un tableau de chaînes de caractères {#is_none_of-with-an-array-of-strings}

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "subscription_tier",
    "comparison": "is_none_of",
    "value": ["bronze", "silver"]
  }
}
```

##### `includes_value` avec un tableau (attribut de type array) {#includes_value-with-an-array-array-attribute}

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "subscribed_products",
    "comparison": "includes_value",
    "value": ["1001", "1002", "1003"]
  }
}
```

Cet exemple correspond aux utilisateurs dont le tableau `subscribed_products` contient l'une des valeurs `"1001"`, `"1002"` ou `"1003"`.

### Filtre d'abonnement aux notifications push {#push-subscription-filter}

Ce filtre vous permet de segmenter en fonction du statut d'abonnement aux notifications push d'un utilisateur.

#### Corps du filtre {#filter-body}

```json
{
  "push_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Comparaisons autorisées :** `is`, `is_not`
- **Valeurs autorisées :** `opted_in`, `subscribed`, `unsubscribed`

### Filtre d'abonnement e-mail {#email-subscription-filter}

Ce filtre vous permet de segmenter en fonction du statut d'abonnement e-mail d'un utilisateur.

#### Corps du filtre

```json
{
  "email_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Comparaisons autorisées :** `is`, `is_not`
- **Valeurs autorisées :** `opted_in`, `subscribed`, `unsubscribed`

### Filtre de dernière utilisation de l'application {#last-used-app-filter}

Ce filtre vous permet de segmenter en fonction de la dernière utilisation de l'application par l'utilisateur. Ces filtres contiennent deux champs :

#### Corps du filtre

```json
{
  "last_used_app":
  {
    "comparison": (String) one of the allowed comparisons listed,
    "value": (String) the value to be compared using the provided comparison
  }
}
```

- **Comparaisons autorisées :** `after`, `before`
- **Valeurs autorisées :** datetime (chaîne de caractères ISO 8601)