---
nav_title: "GET : Répertorier les groupes d'abonnement d'un utilisateur"
article_title: "GET : Répertorier les groupes d'abonnement d'un utilisateur"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze permettant de répertorier les groupes d'abonnement d'un utilisateur."

---
{% api %}
# Répertorier les groupes d'abonnement d'un utilisateur {#list-users-subscription-groups}
{% apimethod get %}
/subscription/user/status
{% endapimethod %}

> Utilisez cet endpoint pour répertorier et obtenir les groupes d'abonnement avec l'historique d'un utilisateur donné.

Si vous souhaitez voir des exemples ou tester cet endpoint pour les **groupes d'abonnement e-mail** :

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470 {% endapiref %}

Si vous souhaitez voir des exemples ou tester cet endpoint pour les **groupes d'abonnement SMS** :

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

Si vous souhaitez voir des exemples ou tester cet endpoint pour les **groupes WhatsApp** :

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key) avec l'autorisation `subscription.groups.get`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `external_id` | Requis | Chaîne de caractères | L'`external_id` de l'utilisateur (doit inclure au moins un et au maximum 50 `external_ids`). |
| `email` | Requis* | Chaîne de caractères | L'adresse e-mail de l'utilisateur, qui peut être transmise sous forme de tableau de chaînes de caractères. Doit inclure au moins une adresse e-mail (maximum 50). |
| `phone` | Requis* | Chaîne de caractères au format [E.164](https://en.wikipedia.org/wiki/E.164) | Le numéro de téléphone de l'utilisateur. Doit inclure au moins un numéro de téléphone (maximum 50). |
| `limit` | Facultatif | Entier | La limite du nombre maximum de résultats renvoyés. La `limit` par défaut (et maximale) est de 100. |
| `offset` | Facultatif | Entier | Nombre de modèles à ignorer avant de renvoyer le reste des modèles correspondant aux critères de recherche. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

{% alert tip %}
S'il existe plusieurs utilisateurs (plusieurs `external_ids`) partageant la même adresse e-mail, tous les utilisateurs seront renvoyés en tant qu'utilisateurs distincts (même s'ils ont la même adresse e-mail ou le même groupe d'abonnement).
{% endalert %}

## Exemple de requête {#example-request}

{% tabs %}
{% tab Utilisateurs multiples %}
{% raw %}
`https://rest.iad-03.braze.com/subscription/user/status?external_id[]=1&external_id[]=2`
{% endraw %}
{% endtab %}
{% tab SMS et WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&limit=100&offset=1&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab E-mail %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&email=example@example.com&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Exemple de réponse {#example-response}

Seuls les groupes d'abonnement dont le statut d'abonnement a été mis à jour dans l'historique de l'utilisateur seront inclus dans une réponse réussie. Cela signifie que les groupes d'abonnement nouvellement créés ne seront pas répertoriés.

```json
{
    "users": [
        {
            "email": "test@example.com",
            "phone": "+11112223333",
            "external_id": "external_identifier",
            "subscription_groups": [
                {
                  "id": "ec2fcc919fca",
                  "name": "ActivationGroup",
                  "channel": "email",
                  "status": "Subscribed"
                },
                {
                  "id": "7d7af9dd5556",
                  "name": "ReactivationGroup",
                  "channel": "email",
                  "status": "Subscribed"
                },
                {
                  "id": "a5e84fd16220",
                  "name": "MarketingGroup",
                  "channel": "sms",
                  "status": "Unsubscribed"
                },
                {
                  "id": "64d8cad9176c",
                  "name": "TransactionalGroup",
                  "channel": "sms",
                  "status": "Unsubscribed"
                },
                {
                  "id": "b2134cd63942",
                  "name": "BankerMarketingGroup",
                  "channel": "sms",
                  "status": "Subscribed"
                }
            ]
        }
    ],
    "total_count": 1,
    "message": "success"
}
```

{% endapi %}