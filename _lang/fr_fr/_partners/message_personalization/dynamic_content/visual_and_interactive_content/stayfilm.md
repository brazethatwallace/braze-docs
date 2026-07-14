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

- **Parcours d'onboarding et de bienvenue :** accueillez les nouveaux utilisateurs avec des vidéos personnalisées en fonction de leur profil ou de leur contexte d'inscription
- **Contenu produit et marketplace :** générez des vidéos axées sur les produits à partir de catalogues ou de médias fournis par les utilisateurs
- **Conversion et activation :** renforcez les actions clés avec des messages vidéo contextuels
- **Fidélisation et ventes additionnelles :** mettez en avant des offres personnalisées ou des jalons d'utilisation au format vidéo
- **Reconquête et prévention de l'attrition :** réengagez les utilisateurs inactifs avec du contenu vidéo sur mesure

## Prérequis {#prerequisites}

Avant de commencer, vérifiez que vous disposez des éléments suivants :

| Condition | Description |
| --------- | ----------- |
| Accès à l'API Stayfilm | Contactez Stayfilm pour obtenir les identifiants de votre projet, notamment `idproject`, `Subscription-Key`, les identifiants client OAuth et l'URL de base de l'API Stayfilm. Pour les détails d'authentification et d'endpoint, consultez la [documentation de l'API Stayfilm](https://apidoc.stayfilm.com). |
| Transformation de données Braze | Utilisez la [transformation de données Braze]({{site.baseurl}}/user_guide/data/unification/data_transformation) pour recevoir les rappels Stayfilm et les associer aux profils utilisateur Braze via l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). |
| Identifiant utilisateur Braze | Ce guide utilise `external_id` pour corréler les tâches Stayfilm avec les profils utilisateur Braze. La valeur que vous transmettez dans `CallbackRelayData` doit correspondre à l'`external_id` de l'utilisateur dans Braze. |
| Sandbox Braze (recommandé) | Testez l'intégration dans un espace de travail sandbox Braze avant de la déployer en production. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Fonctionnement de l'intégration {#how-the-integration-works}

Cette intégration utilise un flux webhook bidirectionnel :

1. **Sortant :** une [Campaign webhook]({{site.baseurl}}/user_guide/channels/webhooks) Braze envoie une tâche de rendu à l'endpoint Stayfilm `POST /Job`. La requête inclut les médias de l'utilisateur, la configuration du modèle et `CallbackRelayData` défini sur l'`external_id` de l'utilisateur Braze.
2. **Entrant :** lorsque Stayfilm termine le rendu, il envoie un rappel à l'URL webhook de votre transformation de données Braze. La transformation associe la réponse à des [attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) et des événements personnalisés sur le profil utilisateur correspondant.
3. **Diffusion :** utilisez l'attribut `stayfilm_video_url` stocké dans les canaux de communication, par exemple un [message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages) avec du HTML personnalisé.

La transformation de données de ce guide écrit les attributs personnalisés suivants :

| Attribut | Description |
| -------- | ----------- |
| `stayfilm_video_status` | `ready` lorsque le rendu réussit, ou `failed` lorsque Stayfilm signale une erreur |
| `stayfilm_video_url` | URL de la vidéo MP4 rendue |
| `stayfilm_job_id` | Identifiant de la tâche Stayfilm |
| `stayfilm_render_error` | Message d'erreur en cas d'échec du rendu |
| `stayfilm_callback_received_at` | Horodatage ISO du rappel |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Attributs personnalisés" }

La transformation enregistre également des événements personnalisés nommés `stayfilm_video_ready` ou `stayfilm_video_failed`.

## Intégration {#integration}

Les étapes suivantes vous guident à travers une preuve de concept. Après avoir validé le flux, adaptez le payload de la tâche, les attributs et la communication à votre cas d'usage.

### Étape 1 : Créer un utilisateur test {#step-1-create-a-test-user}

Créez un profil utilisateur test à utiliser pendant la construction et la validation de l'intégration. Pour plus d'informations, consultez [Importer des utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/import_users).

1. Accédez à **Audience** > **Importer des utilisateurs**.
2. Sélectionnez **Ajout rapide d'utilisateur**.
3. Saisissez un `external_id` et tout autre champ requis, puis sélectionnez **Créer un nouvel utilisateur**.

{% alert important %}
N'utilisez pas de données personnelles — telles que l'e-mail, le numéro de téléphone, le nom complet, le numéro d'identification gouvernemental, l'adresse ou les détails de commande — comme `external_id`. Traitez `external_id` comme sensible à la casse tout au long de cette intégration.
{% endalert %}

Ce guide utilise `stayfilm-poc-001` comme exemple d'`external_id`. Notez la valeur que vous choisissez, car vous l'utiliserez dans les étapes suivantes.

### Étape 2 : Créer une transformation de données {#step-2-create-a-data-transformation}

Créez une transformation de données pour recevoir les rappels Stayfilm et mettre à jour les profils utilisateur.

1. Accédez à **Paramètres des données** > **Transformation de données**.
2. Sélectionnez **Créer une transformation**.
3. Saisissez un nom, par exemple `Stayfilm Callback Data Transformation`.
4. Sous **Expérience d'édition**, sélectionnez **Partir de zéro**.
5. Sous **Sélectionner la destination** > **Destination**, sélectionnez **POST: Track users**.
6. Sélectionnez **Créer une transformation**.
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
8. Sélectionnez **Enregistrer**, puis copiez l'URL webhook générée.
9. Envoyez une requête `POST` de test à l'URL webhook avec le JSON de rappel Stayfilm suivant. Définissez `RelayedData` sur l'`external_id` de l'utilisateur test que vous avez créé à l'étape 1.

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
10. Accédez à **Paramètres des données** > **Transformation de données** et rechargez la page si votre transformation n'apparaît pas dans la liste.
11. Ouvrez la transformation et sélectionnez **Valider**. Confirmez que la validation réussit dans **Sortie**.
12. Sélectionnez **Activer**.
13. Fournissez l'URL webhook copiée à Stayfilm comme URL de rappel.

{% alert note %}
Si vous stockez plus que l'`external_id` Braze dans `CallbackRelayData`, mettez à jour le code de transformation pour analyser `RelayedData` en conséquence.
{% endalert %}

### Étape 3 : Créer une Campaign webhook pour envoyer des tâches à Stayfilm {#step-3-create-a-webhook-campaign-to-send-jobs-to-stayfilm}

Créez une [Campaign webhook]({{site.baseurl}}/user_guide/channels/webhooks) qui soumet des tâches de rendu à Stayfilm.

{% alert important %}
Avant de tester la Campaign, confirmez que Stayfilm a configuré votre projet avec l'URL de rappel de la transformation de données de l'étape 2.
{% endalert %}

1. Accédez à **Messagerie** > **Campaigns**.
2. Sélectionnez **Créer une Campaign** > **Webhook**.
3. Saisissez un nom de Campaign, par exemple `Stayfilm Webhook Integration`.
4. Sélectionnez **Composer un webhook** > **Partir de zéro**.
5. Sous **Composer un webhook** > **URL du webhook**, saisissez l'URL de l'endpoint Stayfilm `POST /Job` fournie par Stayfilm. Remplacez *`{BASE_URL}`* dans l'exemple suivant : `https://{BASE_URL}/stg/v3/job`
6. Définissez la **Méthode HTTP** sur **POST**.
7. Sous **Corps de la requête**, sélectionnez **Texte brut**, puis collez le payload de tâche fourni par Stayfilm. Vous pouvez utiliser le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) pour rendre le corps dynamique.

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
| `Authorization` | Jeton porteur OAuth récupéré via le contenu connecté (voir l'exemple suivant) |
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
8. Sélectionnez **Enregistrer le brouillon**.

{% alert note %}
Si vous quittez la page Campaigns et y revenez, définissez le **Statut** sur **Tous** pour retrouver les Campaigns encore en **Brouillon**.
{% endalert %}

### Étape 4 : Tester la Campaign webhook {#step-4-test-the-webhook-campaign}

1. Depuis le compositeur de webhook, sélectionnez l'onglet **Test**.
2. Sous **Prévisualiser le message en tant qu'utilisateur**, sélectionnez **Sélectionner un utilisateur existant**, puis recherchez votre utilisateur test (par exemple, `stayfilm-poc-001`).
3. Sélectionnez **Envoyer le test**.

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

Stayfilm effectue le rendu de la vidéo de manière asynchrone et envoie un rappel à votre transformation de données lorsque le traitement est terminé. Surveillez le statut de la tâche via les endpoints de l'API Stayfilm décrits dans la [documentation de l'API Stayfilm](https://apidoc.stayfilm.com).

1. Accédez à **Paramètres des données** > **Transformation de données**.
2. Sélectionnez l'onglet **Journaux** de votre transformation.
3. Confirmez qu'un rappel apparaît avec le statut **Succès**.

### Étape 6 : Afficher la vidéo dans un message in-app {#step-6-display-the-video-in-an-in-app-message}

Une fois que `stayfilm_video_url` est renseigné sur le profil utilisateur, affichez la vidéo rendue dans une Campaign ou un Canvas.

1. Accédez à **Messagerie** > **Campaigns**.
2. Sélectionnez **Créer une Campaign** > **Message in-app**.
3. Saisissez un nom de Campaign, par exemple `Stayfilm Video Show`.
4. Dans le compositeur de messages, sélectionnez l'**Éditeur traditionnel**.
5. Sous **Envoyer à**, sélectionnez **Navigateurs web**.
6. Définissez le **Type de message** sur **Code personnalisé**.
7. Collez le HTML suivant dans le champ **HTML** :

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
8. Sélectionnez **Enregistrer le brouillon**.
9. Sélectionnez l'onglet **Test**.
10. Sous **Prévisualiser le message en tant qu'utilisateur**, sélectionnez **Sélectionner un utilisateur existant**, puis recherchez l'`external_id` de votre utilisateur test.

La vidéo rendue apparaît et se lit dans l'aperçu lorsque `stayfilm_video_url` est défini sur le profil.

## Étendre l'intégration {#extend-the-integration}

Ce guide couvre un sous-ensemble de l'API Stayfilm. Pour adapter les modèles de tâches, les entrées médias ou la communication en aval, consultez la [documentation de l'API Stayfilm](https://apidoc.stayfilm.com) et mettez à jour votre payload webhook, le mappage de la transformation de données et la logique de Campaign en conséquence.

## Considérations {#considerations}

- **Rendu asynchrone :** la génération vidéo n'est pas immédiate. Déclenchez la communication de suivi à partir de l'événement personnalisé `stayfilm_video_ready` ou d'un segment basé sur `stayfilm_video_status` au lieu d'envoyer le message in-app dans le même flux que le webhook.
- **Cohérence des identifiants :** la valeur dans `CallbackRelayData` doit correspondre exactement à l'`external_id` de l'utilisateur Braze.
- **Mise en cache du jeton OAuth :** l'exemple de contenu connecté met en cache le jeton OAuth pendant 3 000 secondes. Ajustez `cache_max_age` si Stayfilm modifie les exigences de durée de vie du jeton.
- **Tests en sandbox :** validez la boucle complète de rappel dans un sandbox Braze avant le lancement en production.
- **Capacité des attributs personnalisés :** confirmez que votre espace de travail dispose de la capacité nécessaire pour les attributs personnalisés et les événements créés par cette intégration.

## Résolution des problèmes {#troubleshooting}

Consultez le tableau suivant si vous rencontrez des problèmes avec l'intégration Stayfilm.

| Problème | Résolution |
| -------- | ---------- |
| La validation de la transformation de données échoue | Confirmez que `RelayedData` dans votre payload de test correspond à un `external_id` Braze valide, puis rechargez la page **Transformation de données** avant de sélectionner **Valider**. |
| Le test du webhook renvoie une réponse autre que 201 | Vérifiez les identifiants Stayfilm dans vos en-têtes de requête, confirmez que le bloc de contenu connecté OAuth utilise des valeurs encodées en URL et vérifiez que votre URL `POST /Job` est correcte. |
| Le rappel n'apparaît pas dans les journaux de transformation | Confirmez que Stayfilm dispose de votre URL webhook de transformation de données active et laissez le temps au rendu vidéo de se terminer. |
| L'aperçu in-app n'affiche pas la vidéo | Confirmez que `stayfilm_video_url` est défini sur le profil de l'utilisateur test et que le message in-app cible les **Navigateurs web** avec le **Code personnalisé**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }