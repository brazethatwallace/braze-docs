---
nav_title: Limbik
article_title: Limbik
description: "Cet article de référence décrit le partenariat entre Braze et Limbik, une couche de résonance IA qui prédit comment les audiences interprètent et réagissent aux messages à l'aide d'audiences synthétiques et de prévisions."
alias: /partners/limbik/
page_type: partner
search_tag: Partner
---

# Limbik

> [Limbik](https://limbik.com/cognitive-ai) est votre couche de résonance IA : elle prédit comment les audiences réelles interprètent et réagissent aux messages, concepts et résultats d'IA avant leur mise sur le marché. Alimenté par une recherche primaire continue dans plus de 60 pays et plus de 25 langues, Limbik fournit des audiences synthétiques validées par des humains — des populations numériques qui simulent la réponse d'une audience réelle à la vitesse d'une machine et avec une précision de niveau recherche (95 % de confiance, marge d'erreur de 1,5 % à 3 %). Limbik vous permet de vous assurer immédiatement que vos messages résonnent avec ce que votre audience cible croit et ressent.

_Cette intégration est maintenue par Limbik._

## Conditions préalables {#prerequisites}

Les éléments suivants sont requis pour utiliser Limbik avec Braze :

| Conditions requises | Description |
| --- | --- |
| `account_id` Limbik | Contactez votre équipe de compte Limbik, ou effectuez une requête GET vers l'endpoint `/rest/api/organizations` de Limbik. |
| Jeton d'accès Limbik (`access_token`) | Effectuez une requête POST vers l'endpoint `login` de Limbik et utilisez la valeur `access_token` retournée comme jeton Bearer dans l'en-tête `Authorization`. |
| Clé REST API Braze | Une clé REST API Braze avec les autorisations « Messages ». Créez-en une dans le tableau de bord de Braze sous **Settings** > **API Keys**. |
| `campaign_id` Braze | Accédez à **Messaging** > **Campaigns** et sélectionnez une Campaign. Si la Campaign souhaitée n'existe pas encore, créez-en une et enregistrez-la. En bas de la page de la Campaign, trouvez l'identifiant API de la Campaign. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

Avant d'utiliser l'un des endpoints de prévision, vous devez d'abord identifier à quelle organisation (`account_id`) vous avez accès. Bien que la plupart des clients n'aient qu'une seule organisation, certains comptes peuvent avoir plusieurs organisations disponibles.

{% details Récupérer les organisations disponibles %}

Interrogez l'endpoint des organisations pour récupérer vos organisations disponibles :

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/organizations' \
  -H 'accept: application/json'
```

{% enddetails %}

{% details Exemple de réponse %}

```json
{
  "data": [
    {
      "uid": "aca61bd5-7132-499c-946e-42d092cc1156",
      "name": "Braze API"
    }
  ]
}
```

Sélectionnez le `uid` de l'organisation souhaitée pour l'utiliser comme en-tête `account_id` dans toutes les requêtes API suivantes.

{% enddetails %}

## Authentification {#authentication}

Pour accéder aux endpoints de l'API, vous avez besoin d'un jeton Bearer pour l'authentification. Obtenez votre jeton en vous authentifiant avec vos identifiants.

{% details Requête de connexion %}

```sh
curl -X 'POST' \
  'https://cortex.prod.limbik.com/rest/api/auth/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "your_username",
  "password": "your_password"
}'
```

{% enddetails %}

{% details Exemple de réponse %}

La réponse contient un `access_token` que vous pouvez utiliser comme jeton Bearer dans toutes les requêtes API suivantes :

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer"
}
```

Incluez ce jeton dans l'en-tête `Authorization` pour toutes les requêtes API :

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

{% alert note %}
Vous pouvez utiliser des plateformes API comme Postman pour configurer des workflows automatisés qui appellent plusieurs endpoints REST API de différentes organisations, comme le workflow suivant.
{% endalert %}

{% enddetails %}

## Cas d'utilisation – Générer du contenu de message {#use-case-generating-message-copy}

En utilisant les endpoints REST API de Braze et de Limbik, vous pouvez exploiter les prévisions génératives de Limbik pour créer du contenu de message et l'envoyer via les canaux de communication de Braze, ou ajuster un contenu existant pour améliorer l'impact auprès de votre audience. Les deux plateformes exposent des fonctionnalités que vous pouvez appeler de manière programmatique pour construire des workflows sophistiqués.

Cette documentation présente deux exemples : générer du contenu de message dans Limbik et utiliser ce contenu dans un message envoyé ensuite via Braze, ainsi qu'utiliser Limbik pour évaluer la qualité d'un message donné pour l'audience choisie.

{% details Requête de prévision générative Limbik %}

Utilisez cet endpoint pour générer un message et le retourner dans un modèle de prévision. Exemple de requête :

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/forecasts/generate/template?prompt=YOUR_PROMPT' \
  -H 'account_id: YOUR_ACCOUNT_ID' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'accept: application/json'
```

Remplacez `YOUR_PROMPT`, `YOUR_ACCOUNT_ID` et `YOUR_ACCESS_TOKEN` par votre texte de prompt, l'ID de l'organisation (depuis l'endpoint des organisations) et le jeton Bearer obtenu depuis l'endpoint de connexion.

{% enddetails %}

{% details Exemple de réponse %}

Exemple de réponse de modèle de prévision Limbik :

```json
[
  {
    "type": "Message",
    "displayText": "Formula one next race",
    "additionalDetail": "The latest dev in Formula...",
    "messages": [
      {
        "body": "The latest dev in Formula ..."
      }
    ],
    "population": {
      "id": 56,
      "name": "us2",
      "org_enabled": true,
      "org_visible": true,
      "categories": [],
      "display_name": "US Adults",
      "composite_key": "us2",
      "enabled": true
    }
  }
]
```

L'élément clé pour ce cas d'utilisation est le champ `additionalDetail`, qui contient le contenu du message généré par Limbik.

Utilisez cette valeur pour remplir un message envoyé à Braze. Par exemple, avec l'endpoint POST `/campaigns/trigger/send`, utilisez `additionalDetail` pour remplir un champ du payload. Avec l'endpoint POST `/messages/send`, utilisez-le pour remplir l'objet message de votre choix.

{% enddetails %}

### Champs de la réponse {#response-fields}

La réponse contient les champs clés suivants :

- **`type` :** Le type de message (par exemple, `"Generate"` pour du contenu généré par IA, `"Message"` pour des messages validés)
- **`displayText` :** Un titre court ou un résumé du message
- **`additionalDetail` :** **Le contenu complet du message généré par IA** – C'est le champ principal contenant le texte intégral du message que vous pouvez envoyer via votre plateforme de communication
- **`population` :** La population cible et les segments pour ce message

### Utilisation avec Braze {#using-with-braze}

Le champ `additionalDetail` de la réponse de Limbik contient le contenu du message que vous envoyez à Braze. Un schéma d'intégration courant consiste à transmettre cette valeur dans `trigger_properties.payload` lors de l'appel à l'endpoint d'envoi déclenché de Braze. Dans l'exemple suivant, remplacez `{{additionalDetail}}` par la chaîne de caractères réelle du champ `additionalDetail` de Limbik, et remplacez `{{YOUR_CAMPAIGN_ID}}` par l'ID de votre Campaign.

### Exemple de requête de message déclenché Braze {#braze-trigger-message-request-example}

```json
{
  "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
  "trigger_properties": {
    "payload": "{{additionalDetail}}"
  },
  "broadcast": true
}
```

## Cas d'utilisation – Détails de l'audience synthétique {#use-case-synthetic-audience-details}

Pour approfondir le premier cas d'utilisation, utilisez l'endpoint de Limbik `/rest/api/populations/{account_id}/{population_id}`.

Cet endpoint retourne des points de donnée clés qui décrivent la composition des audiences synthétiques de Limbik, comme le genre, l'emplacement, etc. Vous pouvez utiliser ces valeurs pour remplir des objets Connected Audience lors de l'appel aux endpoints de communication de Braze.

{% alert note %}
Les objets Connected Audience ne peuvent pas cibler les utilisateurs en fonction des attributs « par défaut » de Braze. Vous devez donc stocker tous les attributs que vous souhaitez cibler dans Braze en tant qu'attributs personnalisés.
{% endalert %}

Pour obtenir des scores de prévision pour des segments spécifiques, identifiez les pays disponibles et leurs segments correspondants.

### Étape 1 : Lister les pays disponibles {#step-1-list-available-countries}

Récupérez la liste des pays disponibles pour votre compte :

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/populations/list/aca61bd5-7132-499c-946e-42d092cc1156' \
  -H 'accept: application/json'
```

À partir de la réponse, identifiez le pays que vous souhaitez utiliser. Par exemple, les États-Unis ont un `id` de `56`.

### Étape 2 : Récupérer les segments disponibles {#step-2-retrieve-available-segments}

Après avoir récupéré l'ID du pays, récupérez la liste complète des segments pour ce pays.

{% details Exemple d'appel %}

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/populations/aca61bd5-7132-499c-946e-42d092cc1156/56' \
  -H 'accept: application/json'
```

{% alert note %}
La réponse peut être volumineuse. Mettez ces données en cache (par exemple, dans Redis) par nom ou par clé pour de meilleures performances.
{% endalert %}

{% enddetails %}

{% details Exemple de réponse %}

Par exemple, pour cibler les femmes dans la population adulte américaine :

```json
[
  {
    "id": 56,
    "name": "us2",
    "composite_key": "us2",
    "categories": [
      {
        "id": 9331,
        "name": "gender",
        "composite_key": "us2::gender",
        "segments": [
          {
            "id": 63793,
            "name": "female",
            "composite_key": "us2::gender::female"
          }
        ]
      }
    ]
  }
]
```

{% alert note %}
- Les segments sont spécifiés à l'aide d'un format de clé composite simplifié (par exemple, `gender::female`).
- La clé composite complète de la réponse API (`us2::gender::female`) est raccourcie au nom de la catégorie et du segment uniquement.
- Pour une référence complète des populations et segments disponibles, consultez [Limbik audiences](https://audiences.limbik.com/).
{% endalert %}

En utilisant la valeur de la clé composite pour le message de prévision choisi, vous pouvez mapper ces descripteurs d'audience synthétique aux valeurs des profils utilisateur réels dans Braze.

Par exemple, vous pouvez utiliser la clé composite (`fr1::education_level::master_s_degree`) dans un objet Connected Audience de Braze comme suit :

```json
{
  "AND": [
    {
      "custom_attribute": {
        "custom_attribute_name": "education_level",
        "comparison": "equals",
        "value": "masters"
      }
    }
  ]
}
```

{% enddetails %}

## Cas d'utilisation – Évaluer le score de prévision {#use-case-evaluating-forecast-score}

Vous pouvez utiliser Limbik pour créer un score estimé pour un message auprès d'une audience synthétique. Faites-le de manière programmatique avec l'endpoint `forecasts/synchronous` de Limbik.

### Option 1 – Prévision synchrone {#option-1-synchronous-forecast}

Vous pouvez utiliser le payload de réponse de la génération de modèle directement avec l'endpoint de prévision synchrone :

{% details Exemple de requête générique %}

```sh
curl -X 'POST' \
  'https://cortex.prod.limbik.com/rest/api/forecasts/synchronous' \
  -H 'accept: application/json' \
  -H 'account_id: aca61bd5-7132-499c-946e-42d092cc1156' \
  -H 'Content-Type: application/json' \
  -d '{
  "type": "Generate",
  "displayText": "Formula one season testing 2026",
  "additionalDetail": "Day 1 of the 2026 Formula 1 Bahrain testing session has concluded. Lando Norris recorded the fastest time in the McLaren, with Ferrari in second place. Cadillac drivers Sergio Perez and Valtteri Bottas completed 107 laps, nearly two race distances, and Audi introduced significant upgrades. Which team do you expect to perform best in Australia? #F12026 #BahrainTesting #LandoNorris",
  "population": {
    "population": "us2",
    "segments": []
  }
}'
```

{% enddetails %}

{% details Exemple de réponse (abrégée) %}

```json
{
  "uid": "6c5e28ef-8796-4659-a743-d842a06c9bf7",
  "datetime": "2026-02-11T20:04:06.545+00:00",
  "userId": "9cdd921c-f62f-46a6-902f-a6b0d1702f99",
  "accountId": "aca61bd5-7132-499c-946e-42d092cc1156",
  "name": "Formula one season t...",
  "user_message_context": "",
  "population": [
    {
      "name": "us2",
      "display_name": "US Adults",
      "categories": []
    }
  ],
  "privacy_compliant": false,
  "model_outputs": {
    "belmetrics": {
      "metrics": {
        "moe": 0.02144,
        "pfi": "0.3611",
        "min_val": 0.2941,
        "mean_val": 0.41831
      }
    },
    "virmetrics": {
      "metrics": {
        "moe": 0.02381,
        "pfi": "0.3611",
        "min_val": 0.2,
        "mean_val": 0.30395
      }
    },
    "model_variant": "v4_0_0"
  }
}
```

{% enddetails %}

### Option 2 : Préparer le payload de prévision avec des segments {#option-2-prepare-forecast-payload-with-segments}

Créez votre payload de prévision en utilisant les segments sélectionnés. Les segments utilisent un format de clé composite simplifié.

{% details Exemple de requête spécifique à un segment %}

```json
{
  "type": "Generate",
  "displayText": "Formula one season testing 2026",
  "additionalDetail": "🚀 Day 1 of 2026 F1 Bahrain testing just dropped BOMBS! Lando Norris edged out Max Verstappen for P1 in McLaren's beast, with Ferrari hot on their heels 🔥. But the real shocker? Cadillac's debutants Sergio Perez & Valtteri Bottas smashed 107 laps – nearly TWO race distances! New kids on the block are HERE to stay. Audi's radical upgrades already turning heads too. Who's your early fave for Australia? 👀 #F12026 #BahrainTesting #LandoNorris",
  "population": {
    "population": "us2",
    "segments": [
      "gender::female"
    ]
  }
}
```

{% enddetails %}