---
nav_title: Zapier
article_title: Zapier
alias: /partners/zapier/
description: "Cet article de référence décrit le partenariat entre Braze et Zapier, un outil Web d'automatisation qui vous permet de partager des données entre des applications Web et d'utiliser ces informations pour automatiser des actions."
page_type: partner
search_tag: Partner

---
# Intégration de Zapier {#zapier-integration}

> [Zapier](https://zapier.com/) est un outil Web d'automatisation qui vous permet de partager des données entre des applications Web, puis d'utiliser ces informations pour automatiser des actions.

Le partenariat entre Braze et Zapier s'appuie sur l'API Braze et les [webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook#creating-a-webhook) Braze pour se connecter à des applications tierces, telles que Google Workplace, Slack, Salesforce, WordPress, etc., afin d'automatiser diverses actions.

## Conditions préalables {#prerequisites}

| Exigences | Description |
|---|---|
| Compte Zapier | Un compte Zapier est nécessaire pour bénéficier de ce partenariat. |
| Endpoint REST de Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/api/basics#api-definitions). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Dans l'exemple Zapier suivant, nous allons envoyer des informations depuis WordPress à Braze à l'aide d'un webhook POST. Ces informations peuvent ensuite être utilisées pour créer un Canvas Braze.

### Étape 1 : Créer un déclencheur Zapier {#step-1-create-a-zapier-trigger}

Selon la terminologie de Zapier, un « zap » est un flux de travail automatisé qui connecte vos applications et vos services. La première partie de tout zap consiste à désigner un déclencheur. Une fois votre zap activé, Zapier effectuera automatiquement les actions correspondantes chaque fois que votre déclencheur est détecté.

En utilisant notre exemple WordPress, sur la plateforme Zapier, nous allons configurer notre zap pour qu'il se déclenche lorsqu'une nouvelle publication WordPress est ajoutée et nous sélectionnerons **Published** et **Posts** comme **Post Status** et **Post Type**.

![Sur la plateforme Zapier, dans un zap, sélectionnez le déclencheur comme « nouveau commentaire », « n'importe quel webhook » ou « nouvelle publication ». Pour cet exemple, « nouvelle publication » est sélectionné.] [5]

![Sur la plateforme Zapier, dans un zap, configurez le déclencheur en sélectionnant le statut et le type de publication souhaités. Pour cet exemple, « Published » et « Posts » sont sélectionnés.] [6]

### Étape 2 : Ajouter un webhook d'action {#step-2-add-an-action-webhook}

Définissez ensuite l'action du zap. Lorsque votre zap est activé et que votre déclencheur est détecté, l'action se produit automatiquement.

Toujours dans le cadre de notre exemple, nous voulons envoyer une requête POST au format JSON à un endpoint Braze. Pour cela, sélectionnez l'option **Webhooks** sous **Apps**.

![Étape Apps de Zapier avec Webhooks sélectionné pour l'action.]({% image_buster /assets/img_archive/zapier3.png %})

### Étape 3 : Configurer le POST Braze {#step-3-set-up-braze-post}

Lorsque vous configurez votre webhook, utilisez les paramètres suivants et indiquez votre endpoint REST Braze dans l'URL du webhook. Une fois terminé, sélectionnez **Publish**.

- **Method** : POST
- **Webhook URL** : `https://rest.iad-01.braze.com/canvas/trigger/send`
- **Data Pass-Through** : False
- **Unflatten** : No
- **Request Header** :
  - **Content-Type** : application/json
  - **Authorization** : Bearer YOUR-API-KEY
- **Data** :

```json
{
  "canvas_id": "your_canvas_identifier",
  "recipients": [
    {
      "external_user_id": "external_user_identifier",
      "context":{
        "string_property": "Your example string",
        "example_integer_property": 1
      }
    }
  ]
}
```

![Configuration du webhook Zapier avec l'endpoint Braze, les en-têtes et les champs du payload.]({% image_buster /assets/img/zapier.png %}){: style="max-width:70%;"}

### Étape 4 : Créer une campagne Braze {#step-4-create-a-braze-campaign}

Une fois que vous avez configuré votre zap avec succès, vous pouvez personnaliser vos Campaigns ou Canvas Braze avec les données de WordPress en utilisant le formatage Liquid pour afficher les informations dans vos messages.

## Utiliser Zapier avec l'endpoint `/users/track` {#using-zapier-with-the-userstrack-endpoint}

Pour envoyer des données à l'endpoint Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) (par exemple, lorsque vous utilisez un déclencheur comme **New or Updated Spreadsheet Row** dans Google Sheets), utilisez **Webhooks by Zapier** avec une **Custom Request** — n'utilisez pas l'action standard **POST**. L'action POST standard formate la requête d'une manière qui n'est pas compatible avec l'endpoint `/users/track`.

1. Dans Zapier, choisissez votre déclencheur (par exemple, **New or Updated Spreadsheet Row** dans Google Sheets).
2. Pour l'action, sélectionnez **Webhooks by Zapier** et choisissez **Custom Request** (pas POST).
3. Définissez la **Method** sur POST, saisissez l'URL de votre endpoint REST Braze (par exemple, `https://rest.iad-01.braze.com/users/track`) et formatez le corps de la requête avec des guillemets doubles autour de chaque élément, comme vous le feriez dans Postman ou un appel API. Associez les champs de votre déclencheur (par exemple, les colonnes de la feuille de calcul) aux emplacements appropriés dans le corps JSON.
4. Ajoutez les en-têtes requis :
   - **Content-Type** : `application/json`
   - **Authorization** : `Bearer YOUR-REST-API-KEY` (utilisez votre clé REST API Braze sans crochets ni guillemets)
5. Testez l'étape et activez votre zap.

[5]: {% image_buster /assets/img_archive/zapier1.png %}
[6]: {% image_buster /assets/img_archive/zapier2.png %}