---
nav_title: SessionM
article_title: SessionM
description: "Cet article de référence présente le partenariat entre Braze et SessionM, une plateforme d'engagement client et de fidélisation."
alias: /partners/sessionm/
page_type: partner
search_tag: Partner
---

# Plateforme de fidélisation SessionM {#sessionm-loyalty-platform}

> [SessionM](https://sessionm.com/) est une plateforme d'engagement client et de fidélisation, faisant partie de Capillary Technologies, qui offre des fonctionnalités de gestion de campagne et des solutions de gestion de la fidélisation pour aider les marketeurs à mener des actions de ciblage afin d'augmenter l'engagement et la rentabilité.

## Conditions préalables {#prerequisites}

| Source | Condition | Description |
| --- | --- | --- |
| Braze | Une clé API REST de Braze | Une clé API REST de Braze avec les autorisations `trigger_send`. Elle peut être créée dans le tableau de bord de Braze depuis **Settings** > **API Keys**. |
| Braze | Un endpoint REST de Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'URL de Braze pour [votre instance]({{site.baseurl}}/api/basics/#endpoints). |
| Braze et SessionM | Identifiant correspondant | Pour utiliser l'intégration, assurez-vous que SessionM et Braze disposent tous deux d'un enregistrement des identifiants utilisés par chaque plateforme. Les références à `user_id` correspondent à l'identifiant utilisateur de SessionM généré au moment de la création du profil dans SessionM. |
| SessionM | Un compte SessionM | Un compte SessionM est nécessaire pour profiter de ce partenariat. |
| SessionM | Un endpoint REST SessionM Core | Votre endpoint dépendra de l'URL SessionM de votre instance. Il peut être créé dans le tableau de bord SessionM depuis **Digital Properties**. |
| SessionM | Une clé API REST SessionM Core | La clé API SessionM associée à votre instance et à l'intégration Braze. Cette clé peut être utilisée pour tous les appels de base, y compris les étiquettes. Elle peut être créée dans le tableau de bord SessionM depuis **Digital Properties**. |
| SessionM | Un secret API REST SessionM Core | Le secret API SessionM associé à votre instance et à l'intégration Braze. Cette clé peut être utilisée pour tous les appels de base, y compris les étiquettes. Elle peut être créée dans le tableau de bord SessionM depuis **Digital Properties**. |
| SessionM | Un endpoint REST SessionM Connect | Votre endpoint dépendra de l'URL SessionM de votre instance. Contactez votre gestionnaire de compte technique SessionM ou l'équipe Delivery pour l'obtenir. |
| SessionM | Une chaîne d'autorisation REST SessionM Connect | La chaîne d'autorisation Basic de SessionM Connect associée à votre instance. Cette chaîne d'authentification peut être utilisée pour tous les appels basés sur Connect, y compris get_user_offers. Veuillez contacter votre gestionnaire de compte technique SessionM ou l'équipe Delivery pour l'obtenir. |
| SessionM | Un Retailer ID REST SessionM Connect | Un identifiant GUID unique du client spécifique associé à votre instance. Contactez votre gestionnaire de compte technique SessionM ou l'équipe Delivery pour l'obtenir. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prerequisites" }

## Cas d'utilisation {#use-cases}

Les cas d'utilisation suivants illustrent quelques façons de tirer parti de l'intégration de SessionM et de Braze.

- Créez une segmentation qui intègre les données de toutes les plateformes de fidélisation, de gestion de la clientèle et d'envoi de messages.
- Utilisez une segmentation robuste pour cibler des ensembles d'utilisateurs spécifiques avec des offres et des promotions.
- Profitez des informations les plus récentes sur les utilisateurs, les offres et la fidélité lors de l'envoi de messages.
- Fournissez des notifications détaillées aux clients sur l'avancement et l'achèvement des activités promotionnelles et de fidélisation.
- Notifiez les clients lorsqu'une nouvelle offre est attribuée et fournissez les détails de l'offre.

## Intégration de SessionM avec Braze {#integrating-sessionm-with-braze}

### Étape 1 : Créer un segment dans Braze {#step-1-create-a-segment-in-braze}

Dans Braze, créez un segment d'utilisateurs à cibler avec des promotions et des offres SessionM.

![Le générateur de segments avec le filtre « Attributs personnalisés » sélectionné.]({% image_buster /assets/img/sessionm/CreateSegment.png %})

### Étape 2 : Importer des segments Braze dans SessionM {#step-2-import-braze-segments-into-sessionm}

#### Option 1 : Exporter vers l'endpoint Tag de SessionM (recommandé) {#option-1-export-to-the-sessionm-tag-endpoint-recommended}

Tout d'abord, créez une campagne webhook dans Braze et définissez l'URL du webhook sur {% raw %}`{{endpoint_core}}/priv/v1/apps/{{appkey_core}}/users/{{${user_id}}}/tags`{% endraw %}. Utilisez Liquid pour définir le `user_id` dans l'URL.

En utilisant un **corps de requête** en texte brut, composez le corps du webhook pour inclure les étiquettes souhaitées à ajouter au profil utilisateur dans SessionM et la durée de vie souhaitée. Voici un exemple :

 ```
 {
   "tags":[
    "braze_test"
   ],
   "ttl":2592000
}
 ```

![]({% image_buster /assets/img/sessionm/SessionMWebhookComposer.png %}){: style="max-width:85%;"}

Dans l'onglet **Settings**, ajoutez les paires clé-valeur pour chaque champ d'en-tête de requête :
    - Créez une clé `Content-Type` avec la valeur correspondante `application/json`
    - Créez une clé `Authorization` avec la valeur correspondante `Basic YOUR-ENCODED-STRING-KEY`. Contactez votre équipe SessionM pour obtenir la clé de chaîne encodée pour votre endpoint.

![Paramètres du webhook.]({% image_buster /assets/img/sessionm/SessionMWebhookSettings.png %}){: style="max-width:85%;"}

Planifiez votre envoi, définissez vos **Target Audiences** pour cibler le segment [que vous avez créé précédemment](#step-1-create-a-segment-in-braze), puis lancez votre campagne.

{% alert important %}
Ce processus peut également être effectué via un client API, tel que Postman, en effectuant une requête directement vers l'[endpoint SessionM Tag](https://docs.sessionm.com/developer/APIs/Core/Customers/customers_tags.htm#create-or-increment-a-customer-tag) en spécifiant le client, le nom de l'étiquette et une durée de vie pour chaque utilisateur dans l'appel (un seul utilisateur par appel).
<br><br>
L'exemple de requête suivant utilise cURL.

{% raw %}
```bash
curl --location -g --request POST '{{endpoint_core}}/priv/v1/apps/{{apikey_core}}/users/{{user_id}}/tags' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic {{base64_encoded_string}}' \
--data-raw '{
"tags":[
"tagname1",
"tagname2"
],
"ttl":20000
}'
```
{% endraw %}
{% endalert %}

#### Option 2 : Importation CSV {#option-2-csv-import}

Exportez votre segment Braze à l'aide du segmenteur Braze et fournissez à SessionM un fichier CSV contenant les clients à étiqueter, le nom de l'étiquette et la durée de vie pour chaque utilisateur du fichier.

## Récupération du portefeuille d'offres en temps réel avec Braze {#retrieving-real-time-offer-wallet-with-braze}

L'intégration de SessionM avec Braze permet d'extraire en temps réel les données utilisateur de SessionM au moment de l'envoi du message, en utilisant le contenu connecté, afin d'éliminer le risque de communiquer aux clients des offres de fidélité obsolètes, expirées ou déjà utilisées.

L'exemple suivant montre l'utilisation du contenu connecté pour intégrer les données du portefeuille d'offres dans un message. Cependant, le contenu connecté peut être utilisé avec n'importe quel endpoint Connect de SessionM.

### Étape 1 : Émettre une offre dans SessionM {#step-1-issue-offer-in-sessionm}

SessionM émet des offres aux clients à partir de plusieurs leviers internes différents qui peuvent être configurés. Après avoir été émises, les offres sont placées dans un état que SessionM appelle le « portefeuille d'offres ».

Le client doit effectuer l'action requise ou répondre au ciblage et reçoit l'offre dans SessionM.

SessionM ajoute ensuite l'offre au portefeuille du client dans l'état émis.

### Étape 2 : Appeler l'API du portefeuille d'offres SessionM {#step-2-call-sessionm-offer-wallet-api}

Dans une campagne ou une étape Canvas avec les offres SessionM, utilisez le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/) pour effectuer un appel API vers l'[endpoint SessionM `get_user_offers`](https://domains-connecteast1.ent-sessionm.com/offers/swagger/ui/index#!/InfoV232583210323232323232323232323232This32API32allows32for32the32querying32of32information32about32offers32in32a32read45only32fashion4610323232323232323232323232May32be32initiated32by32the32dashboard32or32the32mobile32app4610323232323232323232323232/InfoV2_GetUserOffers/).

Dans la requête de contenu connecté, spécifiez le `user_id` SessionM de l'utilisateur et votre `retailer_id` pour récupérer la liste complète des offres actives que le client a dans son portefeuille. Chaque requête vers cet endpoint ne peut concerner qu'un seul utilisateur. Contactez l'équipe SessionM pour obtenir la clé de chaîne encodée pour l'en-tête d'autorisation Basic dans votre appel de contenu connecté.

Dans le corps de la requête, `culture` est défini par défaut sur `en-US`, mais vous pouvez utiliser Liquid pour définir la langue d'un utilisateur pour les offres multilingues de SessionM (par exemple, en utilisant {% raw %}`"culture":"{{${language}}}"`{% endraw %}).

{% raw %}
```
{% capture postbody %}
{"retailer_id":"YOUR-RETAIL-ID","user_id":"{{${user_id}}}","skip":0,"take":1000,"include_pending_extended_data":false,"culture":"en-US"}
{% endcapture %}

{% connected_content
     {{endpoint_connect}}/offers/api/2.0/offers/get_user_offers
:method post
:headers {
       "Content-Type": "application/json",
       "Authorization": "Basic YOUR-BASE64-ENCODED-KEY"
  }
     :body {{postbody}}
     :save wallet
%}
```
{% endraw %}

### Étape 3 : Intégrer le portefeuille d'offres dans les messages Braze {#step-3-populate-offer-wallet-to-braze-messaging}

Lorsqu'une requête est envoyée à l'endpoint, SessionM renvoie la liste complète des offres dans l'état émis, ainsi que les détails complets de chaque offre. Voici un exemple de réponse renvoyée :

{% raw %}
```
{
    "status": "ok",
    "payload": {
      "user": {
        "opted_in": false,
        "activated": false,
        ...
      },
      "user_id": "00000000-0000-0000-0000-000000000000",
      "user_offers": [
        {
          "offer_id": "1a2b3324-1da6-4e49-b921-afc386dabb60",
          "offer_group_id": "00000000-0000-0000-0000-000000000000",
          "offer_type": "manual_fulfillment",
          ...
        }
      ],
      "total_records": 1,
      "offer_groups": [
        {
          "id": "00000000-0000-0000-0000-000000000000",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "offer_categories": [
        {
          "id": "9a82f973-aae6-4e10-839b-7117a852cf9e",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "total_points": 1000,
      "available_points": 100
    }
}
```
{% endraw %}

En utilisant la notation par points Liquid, ces données peuvent être intégrées dans le message. Par exemple, pour personnaliser le message avec le résultat `offer_id`, vous pouvez exploiter le payload de retour en utilisant {% raw %}`{{wallet.payload.available_points}}`{% endraw %}, qui renvoie `100`.

{% alert note %}
Il s'agit d'une API individuelle. Si vous avez l'intention d'envoyer un lot de plus de 500 utilisateurs, contactez votre équipe de compte SessionM pour savoir comment incorporer les données en masse dans l'intégration.
{% endalert %}

## Mise en place de l'envoi de messages déclenchés {#setting-up-triggered-messaging}

L'intégration entre SessionM et Braze permet aux données du profil utilisateur, aux détails de l'offre et aux soldes de points d'être dynamiquement intégrés dans les messages et envoyés en temps réel au client au moment de l'action.

### Étape 1 : L'équipe Delivery de SessionM configure les modèles {#step-1-sessionm-delivery-team-configures-templates}

Collaborez avec votre équipe Delivery de SessionM pour développer des modèles à utiliser dans vos envois de messages déclenchés. SessionM insérera les données du profil utilisateur, les détails de l'offre et les soldes de points dans les messages et les déclenchera dans Braze pour un envoi de messages en temps réel au client.

Les champs standard présents dans tous les modèles de SessionM sont les suivants :
- `canvas_id`
- `campaign_id`
- `broadcast flag`
- `customer identifier`
- `email address`

{% alert note %}
Lorsque vous définissez `broadcast flag` sur `true`, le message sera envoyé à l'ensemble du segment que la campagne ou le Canvas cible dans Braze.
{% endalert %}

Des champs supplémentaires peuvent être configurés en fonction des besoins spécifiques :

- **Données de l'offre :** `offer_id`, `offer title`, `user offer id`, `description`, `terms and conditions`, `logo`, `pos discount id`, `expiration date`
- **Données d'attribution de points :** `point award amount`, `point account name`
- **Données de déclenchement d'événement :** toute donnée dans l'événement de déclenchement qui utilise le résultat du webhook trigger/send
- **Données spécifiques à la campagne :** `campaign runtime`, `campaign_id`, `campaign name`, `campaign custom data`

Les champs supplémentaires sont envoyés à Braze en tant que `trigger_properties` pour la personnalisation du message.

### Étape 2 : Créer une campagne ou un Canvas dans Braze {#step-2-create-a-braze-campaign-or-canvas}

Créez dans Braze une campagne ou un Canvas déclenché par API qui sera déclenché par SessionM. Si des champs supplémentaires ont été configurés, tels que `offer_id` ou `offer title`, utilisez Liquid (par exemple {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %}) pour ajouter les champs personnalisés dans votre message.

![Propriétés du déclencheur API.]({% image_buster /assets/img/sessionm/apiTriggerProperties.png %})

Dans l'onglet **Schedule Delivery**, notez l'ID de la campagne ou du Canvas car il sera ajouté aux **Advanced Settings** de la campagne SessionM.

![Campagne déclenchée par API.]({% image_buster /assets/img/sessionm/apiTriggerCampaign.png %})

Finalisez les détails de votre campagne ou de votre Canvas et sélectionnez **Launch**.

### Étape 3 : Créer une campagne promotionnelle ou de messages dans SessionM {#step-3-create-a-sessionm-promotional-or-messaging-campaign}

Ensuite, créez votre campagne dans SessionM.

![Création de campagne SessionM.]({% image_buster /assets/img/sessionm/SessionMCampaignCreation.png %})

Mettez à jour les paramètres avancés de la campagne SessionM afin d'inclure le payload JSON suivant contenant le `braze_campaign_id` ou le `braze_canvas_id`.

{% raw %}
```
{
"braze_campaign_id": "{{CAMPAIGN ID}}",
"braze_canvas_id": "{{CANVAS ID}}",
}
```
{% endraw %}

![Paramètres avancés de SessionM.]({% image_buster /assets/img/sessionm/SessionMAdvancedSettings.png %}){: style="max-width:85%;"}

Créez un déclencheur de message selon la planification ou le comportement souhaité. Ensuite, sélectionnez **Braze Messaging Variant** comme **Messaging Variant** dans le menu **External Message** pour utiliser le modèle.

![Message externe SessionM.]({% image_buster /assets/img/sessionm/SessionMExternalMessage.png %})

Ce modèle extrait les attributs statiques et dynamiques pertinents et fait appel à l'endpoint de Braze.

![Modèle Braze de SessionM.]({% image_buster /assets/img/sessionm/SessionMBrazeTemplate.png %}){: style="max-width:85%;"}