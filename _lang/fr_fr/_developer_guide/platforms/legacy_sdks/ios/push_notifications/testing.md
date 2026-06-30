---
nav_title: Test
article_title: Test de notification push pour iOS
platform: iOS
page_order: 29
description: "Cet article de référence couvre les tests de notification push en ligne de commande pour vos notifications push iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Test {#push-testing}

Si vous souhaitez tester des notifications push et in-app via la ligne de commande, vous pouvez envoyer une seule notification par le terminal via cURL et l'[API d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging). Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test :

Champs requis :

- `YOUR-API-KEY-HERE` — disponible dans **Paramètres** > **Clés API**. Assurez-vous que la clé est autorisée à envoyer des messages via l'endpoint REST API `/messages/send`.
- `EXTERNAL_USER_ID` — disponible sur la page **Rechercher des utilisateurs**.
- `REST_API_ENDPOINT_URL` — répertorié sur la page Braze [Instances]({{site.baseurl}}/api/basics#endpoints. Ensure using the endpoint corresponds to the Braze instance your workspace is on.

Optional fields:
- `YOUR_KEY1` (optional). Assurez-vous que l'endpoint utilisé correspond à l'instance Braze sur laquelle se trouve votre espace de travail.

Champs facultatifs :
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR-API-KEY-HERE" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://{REST_API_ENDPOINT_URL}/messages/send
```
