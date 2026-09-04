---
nav_title: Stayfilm
article_title: Stayfilm
description: "Découvrez comment intégrer le rendu vidéo personnalisé de Stayfilm avec Braze à l'aide de Campaigns webhook, du contenu connecté et de la transformation de données."
alias: /partners/stayfilm/
page_type: partner
search_tag: Partner
---

# Stayfilm

> [Stayfilm](https://www.stayfilm.com/) est une REST API pour la production automatisée et personnalisée de vidéos à grande échelle. La plateforme intègre des données, des images, du texte, des bandes sonores, de la narration et des effets visuels pour générer du contenu vidéo personnalisé pour le eCommerce, les marketplaces, les workflows CRM et les campagnes marketing.
>
> Cette intégration envoie des tâches de rendu depuis Braze vers l'API Stayfilm, reçoit des rappels lorsque les vidéos sont prêtes, et stocke les URL des vidéos ainsi que leur statut sur les profils utilisateur pour une utilisation dans les Campaigns et les Canvas.

_Cette intégration est maintenue par Stayfilm._

## Cas d'usage {#use-cases}

Stayfilm prend en charge la diffusion de vidéos personnalisées tout au long du cycle de vie client, notamment :

- **Onboarding et parcours de bienvenue :** Accueillez les nouveaux utilisateurs avec des vidéos personnalisées en fonction de leur profil ou de leur contexte d'inscription
- **Contenu produit et marketplace :** Générez des vidéos axées sur les produits à partir du catalogue ou de médias fournis par l'utilisateur
- **Conversion et activation :** Renforcez les actions clés avec des messages vidéo contextuels
- **Fidélisation et upsell :** Mettez en avant des offres personnalisées ou des jalons d'utilisation au format vidéo
- **Reconquête et prévention de l'attrition :** Réengagez les utilisateurs inactifs avec du contenu vidéo sur mesure

## Prérequis {#prerequisites}

Avant de commencer, vérifiez que vous disposez des éléments suivants :

| Exigence | Description |
| ----------- | ----------- |
| Accès à l'API Stayfilm | Contactez Stayfilm pour obtenir les identifiants de votre projet, y compris `idproject`, `Subscription-Key`, les identifiants client OAuth et l'URL de base de l'API Stayfilm. Pour les détails d'authentification et des endpoints, consultez la [documentation de l'API Stayfilm](https://apidoc.stayfilm.com). |
| Braze Data Transformation | Utilisez [Braze Data Transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation) pour recevoir les rappels de Stayfilm et les associer aux profils utilisateur Braze via l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). |
| Identifiant utilisateur Braze | Ce guide utilise `external_id` pour associer les tâches Stayfilm aux profils utilisateur Braze. La valeur que vous transmettez dans `CallbackRelayData` doit correspondre à l'`external_id` de l'utilisateur dans Braze. |
| Sandbox Braze (recommandé) | Testez l'intégration dans un espace de travail sandbox Braze avant de déployer en production. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Fonctionnement de l'intégration {#how-the-integration-works}

Cette intégration utilise un flux de webhooks bidirectionnel :

1. **Sortant :** Une [Campaign webhook]({{site.baseurl}}/user_guide/channels/webhooks) Braze envoie une tâche de rendu à l'endpoint Stayfilm `POST /Job`. La requête inclut les médias de l'utilisateur, la configuration du modèle et `CallbackRelayData` défini sur l'`external_id` de l'utilisateur Braze.
2. **Entrant :** Lorsque Stayfilm termine le rendu, il envoie un rappel à l'URL de votre webhook de transformation de données Braze. La transformation associe la réponse à des [attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) et des événements personnalisés sur le profil utilisateur correspondant.
3. **Distribution :** Utilisez l'attribut `stayfilm_video_url` stocké dans les canaux de communication, par exemple un [message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages) avec du HTML personnalisé.

La transformation de données présentée dans ce guide écrit les attributs personnalisés suivants :

| Attribut | Description |
| --------- | ----------- |
| `stayfilm_video_status` | `ready` lorsque le rendu réussit, ou `failed` lorsque Stayfilm signale une erreur |
| `stayfilm_video_url` | URL de la vidéo MP4 rendue |
| `stayfilm_job_id` | Identifiant de la tâche Stayfilm |
| `stayfilm_render_error` | Message d'erreur lorsque le rendu échoue |
| `stayfilm_callback_received_at` | Horodatage ISO du rappel |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Attributs personnalisés" }

La transformation enregistre également des événements personnalisés nommés `stayfilm_video_ready` ou `stayfilm_video_failed`.

## Intégration {#integration}

Les étapes suivantes vous guident dans une preuve de concept. Une fois le flux validé, adaptez le payload du job, les attributs et les messages à votre cas d'usage.

### Étape 1 : Créer un utilisateur test {#step-1-create-a-test-user}

Créez un profil utilisateur test à utiliser pendant la construction et la validation de l'intégration. Pour plus d'informations, consultez [Importer des utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/import_users).

1. Accédez à **Audience** > **Import Users**.
2. Sélectionnez **Quick User Add**.
3. Saisissez un `external_id` ainsi que tous les autres champs requis, puis sélectionnez **Create new user**.

{% alert important %}
N'utilisez pas de données personnelles (telles que l'e-mail, le numéro de téléphone, le nom complet, un numéro d'identification gouvernemental, l'adresse ou les détails de commande) comme `external_id`. Traitez `external_id` comme sensible à la casse tout au long de cette intégration.
{% endalert %}

Ce guide utilise `stayfilm-poc-001` comme exemple d'`external_id`. Notez la valeur choisie, car vous l'utiliserez dans les étapes suivantes.

### Étape 2 : Créer une transformation de données {#step-2-create-a-data-transformation}

Créez une transformation de données pour recevoir les rappels Stayfilm et mettre à jour les profils utilisateur.

1. Accédez à **Data Settings** > **Data Transformation**.
2. Sélectionnez **Create transformation**.
3. Saisissez un nom, par exemple `Stayfilm Callback Data Transformation`.
4. Sous **Editing experience**, sélectionnez **Start from scratch**.
5. Sous **Select destination** > **Destination**, sélectionnez **POST: Track users**.
6. Sélectionnez **Create transformation**.
7. Remplacez le code de transformation par défaut par le suivant :

```javascript
const brazeExternalId = payload.RelayedData;
if (!brazeExternalId) {
  throw new Error("Missing RelayedData. Expected Stayfilm callback to relay the Braze external_id from CallbackRelayData.");
}

const idJob = payload.IdJob || null;
const producedFiles = payload.ProducedFiles || {};
const videoUrl = producedFiles?.Videos?.VideoMP4?.Url || null;
const errorMessage = payload.ErrorMessage || null;
const hasError = payload.HasError === true || Boolean(errorMessage);
const isReady = !hasError && Boolean(videoUrl);
const now = new Date().toISOString();

let brazecall = {
  attributes: [
    {
      external_id: brazeExternalId,
      _update_existing_only: true,
      stayfilm_video_status: isReady ? "ready" : "failed",
      stayfilm_video_url: videoUrl || null,
      stayfilm_job_id: idJob,
      stayfilm_render_error: errorMessage,
      stayfilm_callback_received_at: now
    }
  ],
  events: [
    {
      external_id: brazeExternalId,
      _update_existing_only: true,
      name: isReady ? "stayfilm_video_ready" : "stayfilm_video_failed",
      time: now,
      properties: {
        stayfilm_job_id: idJob,
        stayfilm_video_url: videoUrl || null,
        stayfilm_render_error: errorMessage,
        stayfilm_status: payload.Status || payload.status || null
      }
    }
  ]
};

return brazecall;
```

{: start="8"}
8. Sélectionnez **Save**, puis copiez l'URL de webhook générée.
9. Envoyez une requête `POST` de test à l'URL du webhook avec l'exemple de JSON de rappel Stayfilm suivant. Définissez `RelayedData` sur l'`external_id` de l'utilisateur test créé à l'étape 1.

```json
{
  "IdJob": "debug-job-001",
  "HasError": false,
  "Status": "DRAFT_DONE",
  "ProducedFiles": {
    "Videos": {
      "VideoMP4": {
        "Url": "https://example.com/stayfilm-poc-video.mp4"
      }
    }
  },
  "RelayedData": "stayfilm-poc-001"
}
```

Envoyez la requête avec cURL, Postman ou un outil similaire. Une réponse réussie renvoie le statut HTTP `201` avec `{"message": "success"}`.

{: start="10"}
10. Accédez à **Data Settings** > **Data Transformation** et rechargez la page si votre transformation n'apparaît pas dans la liste.
11. Ouvrez la transformation et sélectionnez **Validate**. Confirmez que la validation réussit dans **Output**.
12. Sélectionnez **Activate**.
13. Fournissez l'URL de webhook copiée à Stayfilm comme URL de rappel.

{% alert note %}
Si vous stockez plus que l'`external_id` Braze dans `CallbackRelayData`, mettez à jour le code de transformation pour analyser `RelayedData` en conséquence.
{% endalert %}

### Étape 3 : Créer une Campaign webhook pour envoyer des jobs à Stayfilm {#step-3-create-a-webhook-campaign-to-send-jobs-to-stayfilm}

Créez une [Campaign webhook]({{site.baseurl}}/user_guide/channels/webhooks) qui soumet des jobs de rendu à Stayfilm.

{% alert important %}
Avant de tester la Campaign, confirmez que Stayfilm a configuré votre projet avec l'URL de rappel de la transformation de données de l'étape 2.
{% endalert %}

1. Accédez à **Messaging** > **Campaigns**.
2. Sélectionnez **Create campaign** > **Webhook**.
3. Saisissez un nom de Campaign, par exemple `Stayfilm Webhook Integration`.
4. Sélectionnez **Compose webhook** > **Start from scratch**.
5. Sous **Compose Webhook** > **Webhook URL**, saisissez l'URL de l'endpoint Stayfilm `POST /Job` fournie par Stayfilm. Remplacez *`{BASE_URL}`* dans l'exemple suivant : `https://{BASE_URL}/stg/v3/job`
6. Définissez **HTTP method** sur **POST**.
7. Sous **Request Body**, sélectionnez **Raw Text**, puis collez le payload de job fourni par Stayfilm. Vous pouvez utiliser le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) pour rendre le corps dynamique.

Incluez `CallbackRelayData` défini sur l'`external_id` de l'utilisateur Braze. Stayfilm renvoie cette valeur dans le rappel sous la forme `RelayedData`.

{% raw %}
```json
{
  "SmartTags": ["Setup-Template"],
  "Medias": [
    {
      "Group": "userMedia",
      "URL": "https://{BASE_URL}/some_media.png"
    }
  ],
  "Videos": [{}],
  "CallbackRelayData": "stayfilm-poc-001"
}
```
{% endraw %}

Ajoutez les en-têtes de requête suivants :

| Clé | Valeur |
| --- | ------ |
| `idproject` | La valeur `idproject` fournie par Stayfilm |
| `Subscription-Key` | La `Subscription-Key` fournie par Stayfilm |
| `Content-Type` | `application/json` |
| `Authorization` | Jeton bearer OAuth récupéré via le contenu connecté (voir l'exemple suivant) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="En-têtes de requête" }

Dans le bloc de contenu connecté suivant, remplacez *`{TENANT_ID}`*, *`{CLIENT_ID}`*, *`{CLIENT_SECRET_URL_ENCODED}`* et *`{SCOPE_URL_ENCODED}`* par les valeurs fournies par Stayfilm. Encodez en URL *`{CLIENT_SECRET_URL_ENCODED}`* et *`{SCOPE_URL_ENCODED}`* avant de les coller dans le bloc. Pour les exigences OAuth, consultez la [documentation de l'API Stayfilm](https://apidoc.stayfilm.com).

{% raw %}
```
{% connected_content https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token
  :method post
  :body grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET_URL_ENCODED}&scope={SCOPE_URL_ENCODED}
  :content_type application/x-www-form-urlencoded
  :cache_max_age 3000
  :save stayfilm_auth
%}Bearer {{stayfilm_auth.access_token}}
```
{% endraw %}

{: start="8"}
8. Sélectionnez **Save Draft**.

{% alert note %}
Si vous quittez la page des Campaigns et y revenez, définissez **Status** sur **All** pour retrouver les Campaigns encore à l'état **Draft**.
{% endalert %}

### Étape 4 : Tester la Campaign webhook {#step-4-test-the-webhook-campaign}

1. Depuis le composeur de webhook, sélectionnez l'onglet **Test**.
2. Sous **Preview message as user**, sélectionnez **Select existing user**, puis recherchez votre utilisateur test (par exemple, `stayfilm-poc-001`).
3. Sélectionnez **Send test**.

Une réponse réussie renvoie le statut HTTP `201` avec un corps JSON similaire au suivant :

```json
{
  "IdJob": "4557a77e-f56c-48be-81f7-2d8c5e558cb1",
  "Videos": [
    {
      "IdVideo": "87287b25-7814-4fa1-ad1a-f2ea89822d0f",
      "IdGenre": "f07a1334-5904-420a-9f31-92644f245c5a",
      "IdVideoTemplate": "7b77c3df-12a1-4636-a9b4-bc227f4c233f",
      "IdProject": "73ea3e73-b41e-4676-b674-51731d3bf49c",
      "Status": "DRAFT_RENDERING_PENDING",
      "DurationInSeconds": null,
      "URL": null,
      "ErrorMessage": null,
      "CreatedAt": "2026-06-16T00:35:28.7736263Z",
      "UpdatedAt": "2026-06-16T00:35:28.7736264Z",
      "IdVideoFather": null,
      "IdVideoSon": null,
      "ProducingStatus": "PENDING"
    }
  ],
  "Images": []
}
```

### Étape 5 : Confirmer le rappel Stayfilm {#step-5-confirm-the-stayfilm-callback}

Stayfilm effectue le rendu de la vidéo de manière asynchrone et envoie un rappel à votre transformation de données lorsque le traitement est terminé. Suivez le statut du job via les endpoints de l'API Stayfilm décrits dans la [documentation de l'API Stayfilm](https://apidoc.stayfilm.com).

1. Accédez à **Data Settings** > **Data Transformation**.
2. Sélectionnez l'onglet **Logs** de votre transformation.
3. Confirmez qu'un rappel apparaît avec le statut **Success**.

### Étape 6 : Afficher la vidéo dans un message in-app {#step-6-display-the-video-in-an-in-app-message}

Une fois `stayfilm_video_url` renseigné sur le profil utilisateur, affichez la vidéo rendue dans une Campaign ou un Canvas.

1. Accédez à **Messaging** > **Campaigns**.
2. Sélectionnez **Create campaign** > **In-app message**.
3. Saisissez un nom de Campaign, par exemple `Stayfilm Video Show`.
4. Dans le composeur de messages, sélectionnez le **Traditional Editor**.
5. Sous **Send To**, sélectionnez **Web Browsers**.
6. Définissez **Message Type** sur **Custom Code**.
7. Collez le code HTML suivant dans le champ **HTML** :

{% raw %}
```html
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
<div id="stayfilm-video-url" style="display: none;">{{custom_attribute.${stayfilm_video_url}}}</div>
<video id="stayfilm-video" controls preload="metadata" playsinline style="width: 100%; max-width: 420px; border-radius: 12px; background: #000;">
Your browser does not support HTML5 video.
</video>
<script>
(function () {
  var urlElement = document.getElementById("stayfilm-video-url");
  var video = document.getElementById("stayfilm-video");
  var videoUrl = urlElement ? urlElement.textContent.trim() : "";
  if (!videoUrl || videoUrl.indexOf("http") !== 0) {
    return;
  }
  var source = document.createElement("source");
  source.src = videoUrl;
  source.type = "video/mp4";
  video.appendChild(source);
  video.load();
})();
</script>
</body>
</html>
```
{% endraw %}

{: start="8"}
8. Sélectionnez **Save Draft**.
9. Sélectionnez l'onglet **Test**.
10. Sous **Preview message as user**, sélectionnez **Select existing user**, puis recherchez l'`external_id` de votre utilisateur test.

La vidéo rendue s'affiche et se lit dans l'aperçu lorsque `stayfilm_video_url` est défini sur le profil.

## Étendre l'intégration {#extend-the-integration}

Ce guide couvre un sous-ensemble de l'API Stayfilm. Pour adapter les modèles de tâches, les entrées média ou la communication en aval, consultez la [documentation de l'API Stayfilm](https://apidoc.stayfilm.com) et mettez à jour le payload de votre webhook, le mappage de la Data Transformation et la logique de votre Campaign en conséquence.

## Considérations {#considerations}

- **Rendu asynchrone :** La génération vidéo n'est pas immédiate. Déclenchez les messages de suivi à partir du custom event `stayfilm_video_ready` ou d'un Segment basé sur `stayfilm_video_status`, au lieu d'envoyer le message in-app dans le même flux que le webhook.
- **Cohérence des identifiants :** La valeur dans `CallbackRelayData` doit correspondre exactement à l'`external_id` de l'utilisateur Braze.
- **Mise en cache du jeton OAuth :** L'exemple de contenu connecté met en cache le jeton OAuth pendant 3000 secondes. Ajustez `cache_max_age` si Stayfilm modifie les exigences de durée de vie du jeton.
- **Tests en sandbox :** Validez la boucle de rappel complète dans un sandbox Braze avant le lancement en production.
- **Capacité des attributs personnalisés :** Vérifiez que votre espace de travail dispose de la capacité nécessaire pour les attributs personnalisés et les événements personnalisés créés par cette intégration Stayfilm.

## Résolution des problèmes {#troubleshooting}

Consultez le tableau suivant si vous rencontrez des problèmes avec l'intégration Stayfilm.

| Problème | Résolution |
| ----- | ---------- |
| La validation de la Data Transformation échoue | Confirmez que `RelayedData` dans votre payload de test correspond à un `external_id` Braze valide, puis rechargez la page **Data Transformation** avant de sélectionner **Validate**. |
| Le test du webhook renvoie une réponse autre que 201 | Vérifiez les identifiants Stayfilm dans les en-têtes de votre requête, confirmez que le bloc OAuth de contenu connecté utilise des valeurs encodées en URL et vérifiez que votre URL `POST /Job` est correcte. |
| Le rappel n'apparaît pas dans les logs de transformation | Confirmez que Stayfilm dispose de l'URL de webhook de votre Data Transformation active et laissez le temps au rendu vidéo de se terminer. |
| L'aperçu in-app n'affiche pas la vidéo | Confirmez que `stayfilm_video_url` est défini sur le profil utilisateur test et que le message in-app cible les **navigateurs web** avec du **code personnalisé**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }