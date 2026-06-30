---
nav_title: "POST : Envoyer des messages Canvas via la réception/distribution déclenchée par l'API"
article_title: "POST : Envoyer des messages Canvas via la réception/distribution déclenchée par l'API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze permettant d'envoyer des Canvas via la réception/distribution déclenchée par l'API."

---
{% api %}
# Envoyer des messages Canvas via la réception/distribution déclenchée par l'API {#send-canvas-messages-using-api-triggered-delivery}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/canvas/trigger/send
{% endapimethod %}

> Utilisez cet endpoint pour envoyer des messages Canvas avec la réception/distribution déclenchée par l'API.

La réception/distribution déclenchée par l'API vous permet de stocker le contenu des messages dans le tableau de bord de Braze tout en déterminant quand un message est envoyé et à qui, à l'aide de votre API.

Avant de pouvoir envoyer des messages avec cet endpoint, vous devez disposer d'un [ID Canvas]({{site.baseurl}}/api/identifier_types#canvas-api-identifier) (qui est créé lorsque vous créez un Canvas).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous devrez générer une clé API avec l'autorisation `canvas.trigger.send`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## Corps de la demande {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "context": (optional, object) Canvas context properties that apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if `recipients` is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message sends to the entire segment targeted by the Canvas)
    [{
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "context": (optional, object) Canvas context properties for this user; key-value pairs override any keys that conflict with the parent `context`,
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an `attributes` object must also be included,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }],
    ...
}
```

## Paramètres de demande {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | Requis | Chaîne de caractères | Voir [Identifiant Canvas]({{site.baseurl}}/api/identifier_types). |
| `context` | Facultatif | Objet | Propriétés de contexte Canvas pour tous les destinataires de cette requête. Les paires clé-valeur de personnalisation s'appliquent à chaque utilisateur, sauf si un `context` par destinataire remplace une clé. L'objet `context` peut atteindre une taille maximale de 50 Ko. |
| `broadcast` | Facultatif | Valeur booléenne | Vous devez définir `broadcast` sur true lorsque vous envoyez un message à l'ensemble du segment configuré comme audience cible du Canvas dans le tableau de bord de Braze. Ce paramètre est défini sur false par défaut (depuis le 31 août 2017). <br><br> Si `broadcast` est défini sur true, une liste `recipients` ne peut pas être incluse. Toutefois, soyez prudent lorsque vous définissez `broadcast: true`, car en activant involontairement cet indicateur, vous risquez d'envoyer votre message à une audience plus large que prévu. |
| `audience` | Facultatif | Objet audience connectée | Voir [Audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience). Lorsque vous incluez `audience`, le message est envoyé uniquement aux utilisateurs qui correspondent aux filtres définis, tels que les attributs personnalisés et les statuts d'abonnement. |
| `recipients` | Facultatif | Tableau | Voir [Objet destinataires]({{site.baseurl}}/api/objects_filters/recipient_object). <br><br> Si `send_to_existing_only` est `false`, un objet `attributes` doit être inclus pour le destinataire. <br><br> Si cette option n'est pas fournie et que `broadcast` est défini sur `true`, le message est envoyé à l'ensemble du segment configuré comme audience cible du Canvas dans le tableau de bord de Braze.<br><br> Le tableau `recipients` peut contenir jusqu'à 50 objets. Chaque objet doit inclure exactement un des éléments suivants : `external_user_id`, `user_alias` ou `email`, et peut inclure un objet `context` par destinataire pour les propriétés de contexte Canvas (les clés par destinataire remplacent le `context` de niveau parent en cas de conflit). <br><br> Si `email` est l'identifiant, vous devez inclure [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email) dans l'objet destinataire. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de demande" }

## Exemple de demande {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "context": {"product_name" : "shoes", "product_price" : 79.99},
  "broadcast": false,
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
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
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "recipients": [
    {
      "user_alias": {
        "alias_name" : "example_name",
        "alias_label" : "example_label"
      },
      "external_user_id": "user_identifier",
      "send_to_existing_only": true,
      "attributes": {
          "first_name" : "Alex"
      }
    }
  ]
}'
```

## Détails de la réponse {#response-details}

Les réponses des endpoints d'envoi de messages incluent le `dispatch_id` du message, qui sert de référence pour la distribution du message. Le `dispatch_id` est l'ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Consultez [Comportement du Dispatch ID]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id) pour plus d'informations.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `201` pourrait renvoyer le corps de réponse suivant. Si le Canvas est archivé, arrêté ou mis en pause, il n'est pas envoyé via cet endpoint.

```
{
  "notice": "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.",
  "dispatch_id": "example_dispatch_id",
  "message": "success"
}
```

Si votre Canvas est archivé, vous verrez ce message `notice` : "The Canvas is archived. Unarchive the Canvas to ensure trigger requests will take effect." Si votre Canvas n'est pas actif, vous verrez ce message `notice` : "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect."

Si votre demande rencontre une erreur fatale, reportez-vous à la section [Erreurs et réponses]({{site.baseurl}}/api/errors#fatal-errors) pour connaître le code d'erreur et sa description.

## Considérations {#considerations}

Tenez compte des éléments suivants lorsque vous effectuez des appels API pour envoyer des messages Canvas via la réception/distribution déclenchée par l'API :

- **Envoi aux utilisateurs existants** : Lorsque `send_to_existing_only` est défini sur `true` (valeur par défaut), le message est envoyé uniquement aux utilisateurs existants dans Braze.
- **Création de nouveaux utilisateurs** : Lorsque `send_to_existing_only` est défini sur `false`, vous devez inclure un objet `attributes`. Si un utilisateur avec l'ID spécifié n'existe pas, Braze crée un utilisateur avec cet ID et ces attributs avant d'envoyer le message.
- **Les nouveaux profils nécessitent `attributes` avec `send_to_existing_only: false`.** Braze exécute la création ou la mise à jour pré-envoi à partir de l'objet `attributes` dans le même destinataire. Si vous définissez `send_to_existing_only` sur `false` mais omettez `attributes` (ou envoyez un objet vide), Braze n'hydrate pas les données du profil de la même manière, et vous n'obtenez donc pas le comportement combiné « créer ou mettre à jour l'utilisateur, puis envoyer » prévu par ce modèle.
- **Adressage e-mail et SMS.** Pour la plupart des envois e-mail ou SMS déclenchés par l'API à une personne qui n'est pas encore dans Braze, incluez les champs de distribution dont vous avez besoin dans `attributes` (par exemple `email`, ou les attributs de téléphone que votre espace de travail utilise pour les SMS). Vous pouvez également y définir l'appartenance à un groupe d'abonnement ou le statut d'abonnement lorsque l'état d'abonnement doit changer dans le même appel.
- **Éligibilité au Canvas.** Une fois le profil créé ou mis à jour, cet utilisateur doit toujours correspondre à l'audience cible du Canvas dans le tableau de bord et aux règles d'envoi du canal (par exemple, être abonné aux e-mails), sinon Braze n'envoie pas le message.
- **Limitation des alias d'utilisateur** : L'indicateur `send_to_existing_only` ne peut pas être utilisé avec les alias d'utilisateur. Pour envoyer un message à un utilisateur disposant uniquement d'un alias, celui-ci doit déjà exister dans Braze.
- **Ciblage par segment** : Le paramètre `segment_id` n'est pas pris en charge pour cet endpoint. Pour cibler un segment, configurez-le dans les paramètres d'audience cible du Canvas dans le tableau de bord de Braze et utilisez `broadcast: true`, ou utilisez le paramètre `audience` avec les filtres d'[audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience).
- **Ciblage combiné** : Lorsque vous incluez à la fois le paramètre `recipients` et configurez un segment cible dans le tableau de bord, le message est envoyé uniquement aux profils utilisateurs spécifiés dans l'appel API et qui correspondent également aux filtres du segment.
- **Appels de serveur à serveur** : Si vous effectuez des appels de serveur à serveur, il peut être nécessaire d'ajouter l'URL de l'API appropriée à votre liste d'autorisation si vous êtes derrière un pare-feu.

## Objet Attributes pour Canvas {#attributes-object-for-canvas}

Utilisez l'objet de message `attributes` pour ajouter, créer ou mettre à jour les attributs et les valeurs d'un utilisateur avant de lui envoyer un Canvas déclenché par l'API à l'aide de l'endpoint `canvas/trigger/send`. Cet appel API traite l'objet des attributs de l'utilisateur avant de traiter et d'envoyer le Canvas. Cela permet de minimiser le risque de problèmes causés par des [conditions de concurrence]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions). Toutefois, par défaut, les groupes d'abonnement ne peuvent pas être mis à jour de cette manière.

{% alert note %}
Vous cherchez la version Campaign de cet endpoint ? Consultez [Envoi de messages Campaign via la réception/distribution déclenchée par l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns).
{% endalert %}

{% endapi %}