---
nav_title: "POST : Envoyer des campagnes via une distribution déclenchée par API"
article_title: "POST : Envoyer des campagnes via une distribution déclenchée par API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Braze permettant d'envoyer des campagnes via une distribution déclenchée par API."

---
{% api %}
# Envoyer des messages de Campaign via une distribution déclenchée par API {#send-campaign-messages-using-api-triggered-delivery}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/trigger/send
{% endapimethod %}

> Utilisez cet endpoint pour envoyer des messages immédiats et ponctuels à des utilisateurs désignés via une distribution déclenchée par API.

La distribution déclenchée par API vous permet d'héberger le contenu des messages dans le tableau de bord de Braze tout en contrôlant, via votre API, quand un message est envoyé et à qui.

Si vous ciblez un Segment, un enregistrement de votre requête est conservé dans la [console de développement](https://dashboard.braze.com/app_settings/developer_console/activitylog/). Pour envoyer des messages avec cet endpoint, vous devez disposer d'un [ID de Campaign]({{site.baseurl}}/api/identifier_types) créé lors de la création d'une [Campaign déclenchée par API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous devez générer une clé API avec l'autorisation `campaigns.trigger.send`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## Corps de la requête {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to all users in this request,
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' sends to only users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to `false`, message sends to the entire segment targeted by the campaign)
    [
      {
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "trigger_properties": (optional, object) personalization key-value pairs that apply to this user (these key-value pairs override any keys that conflict with the parent trigger_properties),
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an attributes object must also be included,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
  ],
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name", "url", and optionally "basic_auth_credential",
    [
      {
       "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
       "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension is detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
       "basic_auth_credential": (optional, string) the name of the stored basic authentication credential to use when the attachment URL requires a login,
      }
    ]
}
```

## Paramètres de la requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Requis | Chaîne de caractères | Voir [identifiant de Campaign]({{site.baseurl}}/api/identifier_types). |
| `send_id` | Facultatif | Chaîne de caractères | Voir [identifiant d'envoi]({{site.baseurl}}/api/identifier_types). |
| `trigger_properties` | Facultatif | Objet | Voir [propriétés du déclencheur]({{site.baseurl}}/api/objects_filters/trigger_properties_object). Les paires clé-valeur de personnalisation s'appliquent à tous les utilisateurs de cette requête. |
| `broadcast` | Facultatif | Valeur booléenne | Vous devez définir `broadcast` sur true lorsque vous envoyez un message à l'ensemble du Segment configuré comme audience cible de la Campaign dans le tableau de bord de Braze. Ce paramètre est défini sur false par défaut (depuis le 31 août 2017). <br><br> Si `broadcast` est défini sur true, une liste `recipients` ne peut pas être incluse. Toutefois, soyez prudent lorsque vous définissez `broadcast: true`, car en activant involontairement cet indicateur, vous risquez d'envoyer votre message à une audience plus large que prévu. |
| `audience` | Facultatif | Objet audience connectée | Voir [audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience). Lorsque vous incluez `audience`, le message est envoyé uniquement aux utilisateurs qui correspondent aux filtres définis, tels que les attributs personnalisés et les statuts d'abonnement. |
| `recipients` | Facultatif | Tableau | Voir [objet destinataire]({{site.baseurl}}/api/objects_filters/recipient_object).<br><br>Si `send_to_existing_only` est `false`, un objet `attributes` doit être inclus.<br><br>Vous pouvez mettre à jour le statut du groupe d'abonnement d'un utilisateur en incluant `subscription_groups` dans l'objet `attributes` imbriqué. Pour plus de détails, consultez [Objet attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object).<br><br>Si `recipients` n'est pas fourni et que `broadcast` est défini sur true, le message est envoyé à l'ensemble du Segment configuré comme audience cible de la Campaign dans le tableau de bord de Braze.<br><br>Si `email` est l'identifiant, vous devez inclure [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers) dans l'objet destinataire. |
| `attachments` | Facultatif | Tableau | Si `broadcast` est défini sur true, la liste `attachments` ne peut pas être incluse. <br><br>Lorsqu'une URL de pièce jointe nécessite une connexion, incluez `basic_auth_credential` sur cette pièce jointe et définissez-le avec le nom d'un identifiant d'authentification basique enregistré. Pour configurer un identifiant, consultez [Authentification pour les pièces jointes d'e-mails]({{site.baseurl}}/api/objects_filters/messaging/email_object#authentication-for-email-file-attachments). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de la requête" }

### Comportement de résolution des destinataires {#recipient-resolution-behavior}

Cette section explique comment Braze sélectionne un profil utilisateur pour l'envoi et ce qui se passe lorsqu'aucun profil n'est sélectionné.

Le statut du groupe d'abonnement d'un utilisateur peut être mis à jour en incluant un paramètre `subscription_groups` dans l'objet `attributes`. Pour plus de détails, consultez [Objet attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object).

#### Limites de destinataires et création de profils {#recipient-limits-and-profile-creation}

Découvrez comment les limites de destinataires et la création de profils fonctionnent pour cet endpoint.

- Le tableau `recipients` peut contenir jusqu'à 50 objets, chacun contenant une seule chaîne `external_user_id` et un objet `trigger_properties`.
- Lorsque `send_to_existing_only` est `true` (valeur par défaut), Braze envoie le message uniquement aux utilisateurs existants.
- Lorsque `send_to_existing_only` est `false` et qu'un objet `attributes` est fourni, Braze crée un nouvel utilisateur s'il n'en existe pas.
- **Les nouveaux profils nécessitent `attributes` avec `send_to_existing_only: false`.** Braze exécute la création ou la mise à jour pré-envoi à partir de l'objet `attributes` dans le même destinataire. Si vous définissez `send_to_existing_only` sur `false` mais omettez `attributes` (ou envoyez un objet vide), Braze n'hydrate pas les données du profil de la même manière, et vous n'obtenez donc pas le comportement combiné « créer ou mettre à jour l'utilisateur, puis envoyer » pour lequel ce modèle est conçu.
- **Adressage e-mail et SMS.** Pour la plupart des envois par e-mail ou SMS déclenchés par API à une personne qui n'est pas encore dans Braze, incluez les champs de distribution nécessaires dans `attributes` (par exemple `email`, ou les attributs téléphoniques utilisés par votre espace de travail pour le SMS). Vous pouvez également y définir l'appartenance à un groupe d'abonnement ou le statut d'abonnement lorsque l'état d'abonnement doit être modifié dans le même appel.
- **Éligibilité à la Campaign.** Une fois le profil créé ou mis à jour, cet utilisateur doit toujours correspondre à l'audience cible de la Campaign dans le tableau de bord et aux règles d'envoi du canal (par exemple, être abonné aux e-mails), sinon Braze n'envoie pas le message.
- Définir `send_to_existing_only` sur `false` n'est pas pris en charge pour les alias d'utilisateur. Les nouveaux utilisateurs disposant uniquement d'un alias ne peuvent pas être créés via cet endpoint. Pour envoyer un message à un utilisateur disposant uniquement d'un alias, celui-ci doit déjà exister dans Braze.

#### Identifiant e-mail et résolution des égalités de priorisation {#email-identifier-and-prioritization-ties}

Lorsque vous identifiez les destinataires par e-mail, Braze utilise `prioritization`. Braze envoie uniquement lorsque `prioritization` renvoie un seul profil.

- Si vous utilisez `email` comme identifiant, Braze résout le destinataire à l'aide de `prioritization`.
- Si `prioritization` renvoie une égalité, Braze n'envoie pas.
- Braze envoie une fois l'égalité résolue et lorsque `prioritization` renvoie un seul profil. Par exemple, si des mises à jour de profil modifient les champs de classement d'un utilisateur, Braze envoie dès que `prioritization` peut identifier un profil de manière unique (voir [Comportement de nouvelle tentative et `send_to_existing_only`](#retry-behavior-and-send_to_existing_only)).
- Braze n'envoie pas non plus lorsque `prioritization` ne renvoie aucun profil.

#### Comportement de nouvelle tentative et send_to_existing_only {#retry-behavior-and-send_to_existing_only}

Découvrez ce qui se passe lorsque `prioritization` ne renvoie pas exactement un seul profil.

- Lorsque `prioritization` ne renvoie pas exactement un seul profil utilisateur, Braze retente la résolution jusqu'à 40 fois. Ce comportement de nouvelle tentative est attendu.
- Le paramètre `send_to_existing_only` ne modifie pas le comportement en cas d'égalité de `prioritization`. Le même comportement d'égalité et de nouvelle tentative s'applique, que ce paramètre soit défini sur `true` ou `false`.

Si vous déclenchez une Campaign e-mail uniquement pour un destinataire identifié par `external_user_id` ou `user_alias`, et que ce profil utilisateur ne possède pas d'adresse e-mail au moment de l'appel, Braze retente l'envoi pendant environ 2 heures. Cela couvre le cas courant où un utilisateur est créé et son adresse e-mail est définie dans un court laps de temps. Pour envoyer sans délai, incluez l'attribut `email` dans `recipients[].attributes` afin que l'adresse soit définie dans le même appel que le déclencheur.

{% alert note %}
Le paramètre `segment_id` n'est pas pris en charge pour cet endpoint. Pour cibler un Segment, configurez-le dans les paramètres d'audience cible de la Campaign dans le tableau de bord de Braze et utilisez `"broadcast": true`, ou utilisez le paramètre `audience` avec les filtres [audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience).
{% endalert %}

## Exemple de requête {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "trigger_properties": "",
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
      "external_user_id": "external_user_identifier",
      "trigger_properties": "",
      "send_to_existing_only": true,
      "attributes": {
        "first_name" : "Alex"
      }
    }
  ],
  "attachments": [
    {
      "file_name" : "YourFileName",
      "url" : "https://exampleurl.com/YourFileName.pdf",
      "basic_auth_credential": "company_basic_auth_credential_name"
    }
  ]
}'
```

## Détails de la réponse {#response-details}

Les réponses des endpoints d'envoi de messages incluent le `dispatch_id` du message, qui sert de référence pour le suivi de l'envoi. Le `dispatch_id` est l'identifiant de l'envoi, un ID unique pour chaque transmission effectuée depuis Braze. Lorsque vous utilisez cet endpoint, vous recevez un seul `dispatch_id` pour l'ensemble du lot d'utilisateurs. Pour en savoir plus sur le `dispatch_id`, consultez notre documentation sur le [comportement du Dispatch ID]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id).

Si votre requête rencontre une erreur fatale, consultez la section [Erreurs et réponses]({{site.baseurl}}/api/errors#fatal-errors) pour connaître le code d'erreur et sa description.

## Objet attributs pour les Campaigns {#attributes-object-for-campaigns}

Braze dispose d'un objet de messagerie appelé `attributes` qui vous permet d'ajouter, de créer ou de mettre à jour les attributs et les valeurs d'un utilisateur avant de lui envoyer une Campaign déclenchée par API. L'utilisation de l'endpoint `campaign/trigger/send` permet de traiter l'objet des attributs utilisateur avant de traiter et d'envoyer la Campaign. Cela permet de minimiser le risque de problèmes causés par des [conditions de concurrence]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions).

{% alert tip %}
Vous recherchez la version Canvas de cet endpoint ? Consultez [Envoyer des messages Canvas via une distribution déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).
{% endalert %}

### Pourquoi Liquid ne s'affiche-t-il pas lorsque je l'insère directement dans le corps JSON ? {#why-doesnt-liquid-render-when-i-put-it-directly-in-my-json-body}

Lorsque le corps de votre requête est un JSON valide, Braze évalue tout Liquid contenu dans le payload côté serveur. Si vous intégrez du Liquid sous forme de chaînes brutes, mettez ces chaînes entre guillemets et échappez-les afin que le corps reste un JSON valide — par exemple, échappez les guillemets doubles à l'intérieur des chaînes. Si le corps échoue à l'analyse JSON, Braze renvoie une erreur `400` avant d'évaluer le moindre Liquid. Lorsque cela est possible, transmettez les valeurs dynamiques via [`trigger_properties`]({{site.baseurl}}/api/objects_filters/trigger_properties_object) au lieu d'intégrer du Liquid directement dans le payload.

{% endapi %}