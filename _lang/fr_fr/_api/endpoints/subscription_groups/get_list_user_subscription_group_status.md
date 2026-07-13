---
nav_title: "GET : Afficher le statut du groupe d'abonnement des utilisateurs"
article_title: "GET : Afficher le statut du groupe d'abonnement des utilisateurs"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Afficher le statut du groupe d'abonnement des utilisateurs."

---
{% api %}
# Afficher le statut du groupe d'abonnement de l'utilisateur {#list-users-subscription-group-status}
{% apimethod get %}
/subscription/status/get
{% endapimethod %}

> Utilisez cet endpoint pour obtenir l'état d'abonnement d'un utilisateur dans un groupe d'abonnement.

Ces groupes seront disponibles sur la page **Groupe d'abonnement**. La réponse de cet endpoint inclura l'ID externe ainsi que le statut abonné, désabonné ou inconnu pour le groupe d'abonnement spécifique demandé dans l'appel d'API. Cela peut être utilisé pour mettre à jour l'état du groupe d'abonnement dans des appels d'API ultérieurs ou pour l'afficher sur une page web hébergée.

Si vous souhaitez voir des exemples ou tester cet endpoint pour les **Groupes d'abonnement e-mail** :

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2 {% endapiref %}

Si vous souhaitez voir des exemples ou tester cet endpoint pour les **Groupes d'abonnement SMS** :

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

Si vous souhaitez voir des exemples ou tester cet endpoint pour les **groupes WhatsApp** :

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key) avec l'autorisation `subscription.status.get`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types?tab=subscription%20group%20ids) | Requis | Chaîne de caractères | L'`id` de votre groupe d'abonnement. |
| `external_id` | Requis* | Chaîne de caractères | L'`external_id` de l'utilisateur (doit inclure au minimum un et au maximum 50 `external_ids`). <br><br>Lorsqu'un `external_id` et un `email`/`phone` sont soumis, seul(s) le(s) `external_id`(s) fourni(s) seront appliqués à la requête. |
| `email` | Requis* | Chaîne de caractères | L'adresse e-mail de l'utilisateur. Elle peut être transmise sous forme de tableau de chaînes de caractères avec un maximum de 50.<br><br> Soumettre à la fois une adresse e-mail et un numéro de téléphone (sans `external_id`) entraînera une erreur. |
| `phone` | Requis* | Chaîne de caractères au format [E.164](https://en.wikipedia.org/wiki/E.164) | Le numéro de téléphone de l'utilisateur. Si l'e-mail n'est pas inclus, vous devez fournir au moins un numéro de téléphone (avec un maximum de 50).<br><br> Soumettre à la fois une adresse e-mail et un numéro de téléphone (sans `external_id`) entraînera une erreur. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête" }

*Un `external_id`, un `email` ou un `phone` est requis pour chaque utilisateur.

- Pour les groupes d'abonnement SMS et WhatsApp, un `external_id` ou un `phone` est requis. Lorsque les deux sont soumis, seul l'`external_id` est utilisé pour l'interrogation et le numéro de téléphone est appliqué à cet utilisateur.
- Pour les groupes d'abonnement e-mail, un `external_id` ou un `email` est requis. Lorsque les deux sont soumis, seul l'`external_id` est utilisé pour la requête et l'adresse e-mail est appliquée à cet utilisateur.

## Exemple de requête {#example-request}

{% tabs %}
{% tab Multiple Users %}
{% raw %}
```
https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&external_id[]=1&external_id[]=2
```
{% endraw %}
{% endtab %}
{% tab SMS and WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&email=example@example.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Réponse {#response}

Toutes les réponses réussies renverront `Subscribed`, `Unsubscribed` ou `Unknown` en fonction du statut et de l'historique de l'utilisateur avec le groupe d'abonnement.

```json
{
  "status": {
    "1": "Unsubscribed",
    "2": "Subscribed"
  },
  "message": "success"
}
```

{% alert important %}
Cet endpoint renvoie le statut du groupe d'abonnement indépendamment de l'état d'abonnement global de l'utilisateur. Si un utilisateur est globalement désabonné, le tableau de bord de Braze l'affiche comme désabonné de chaque groupe d'abonnement. Cependant, cet endpoint renvoie toujours le dernier statut enregistré du groupe d'abonnement (par exemple, `Subscribed`) car l'état d'abonnement global remplace les groupes d'abonnement individuels sans les écraser.<br><br>Braze conserve les statuts individuels des groupes d'abonnement afin que, si l'utilisateur se réabonne globalement, chaque groupe d'abonnement revienne à son statut précédemment enregistré. Pour déterminer l'état d'abonnement effectif d'un utilisateur, vérifiez à la fois son statut d'abonnement global et le statut du groupe d'abonnement renvoyé par cet endpoint.
{% endalert %}

{% endapi %}