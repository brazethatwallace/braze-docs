---
nav_title: Amplitude et Contenu connecté
article_title: Amplitude et Contenu connecté
page_order: 0
alias: /partners/amplitude_api_endpoints/
page_type: partner
description: "L'API de profil utilisateur d'Amplitude fournit les profils des utilisateurs d'Amplitude. Cela inclut les propriétés utilisateur, les propriétés utilisateur calculées, une liste des identifiants de cohortes auxquelles l'utilisateur appartient, ainsi que des recommandations."
search_tag: Partner

---

# Amplitude et Contenu connecté {#amplitude-and-connected-content}

> L'API de profil utilisateur d'Amplitude fournit les profils des utilisateurs d'Amplitude. Cela inclut les propriétés utilisateur, les propriétés utilisateur calculées, une liste des identifiants de cohortes auxquelles l'utilisateur appartient, ainsi que des recommandations. Vous trouverez ci-dessous une liste des endpoints courants de l'API Amplitude pouvant être utilisés avec le Contenu connecté.

## Paramètres de l'endpoint {#endpoint-parameters}

Le tableau suivant présente les paramètres que vous pouvez utiliser dans vos appels à l'API de profil utilisateur.

| Paramètre | Requis | Description |
| --------- | -------- | ----------- |
| `user_id` | Facultatif | ID utilisateur (ID externe de la base de données) à interroger, requis sauf si `device_id` est défini. |
| `device_id` | Facultatif | ID de l'appareil (ID anonyme) à interroger, requis sauf si `user_id` est défini. |
| `get_recs` | Facultatif<br>(Valeur par défaut : false) | Renvoie un résultat de recommandation pour cet utilisateur. |
| `rec_id` | Facultatif | Recommandation(s) à récupérer, requis si `get_recs` est vrai. Vous pouvez récupérer plusieurs recommandations en séparant les `rec_ids` par des virgules. |
| `rec_type` | Facultatif | Remplace le paramètre de contrôle expérimental par défaut. `rec_type=model` renvoie des recommandations modélisées et `rec_type=random` renvoie des recommandations aléatoires. D'autres options pourraient être disponibles à l'avenir. |
| `get_amp_props` | Facultatif<br>(Valeur par défaut : false) | Renvoie l'ensemble complet des propriétés utilisateur pour cet utilisateur, à l'exclusion des calculs. |
| `get_cohort_ids` | Facultatif<br>(Valeur par défaut : false) | Renvoie la liste de tous les ID de cohorte dont cet utilisateur fait partie et qui ont été configurés pour faire l'objet d'un suivi. Par défaut, l'appartenance à une cohorte n'est pas suivie pour les utilisateurs, quelle que soit la cohorte. |
| `get_computations` | Facultatif<br>(Valeur par défaut : false) | Renvoie la liste de tous les calculs activés pour cet utilisateur. |
| `comp_id` | Facultatif | Renvoie un calcul unique qui pourrait être activé pour cet utilisateur. La valeur renvoyée sera nulle s'il n'existe pas. Si `get_computations` est vrai, toutes les valeurs seront récupérées, y compris celle-ci (à moins qu'elle ne soit archivée ou supprimée).|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Endpoint parameters" }

Le tableau suivant présente les paramètres que vous pouvez le plus souvent vous attendre à voir dans les réponses d'Amplitude.

| Paramètre de réponse | Description |
| ------------------ | ----------- |
| `rec_id` | L'ID de recommandation demandé. |
| `child_rec_id` | Un ID de recommandation plus détaillé qu'Amplitude peut utiliser en backend dans le cadre d'une expérience interne visant à améliorer les performances du modèle. Dans la plupart des cas, il sera identique à `rec_id`. |
| `items` | Liste des recommandations pour cet utilisateur. |
| `is_control` | true si cet utilisateur fait partie du groupe de contrôle. |
| `recommendation_source` | Nom du modèle utilisé pour générer cette recommandation. |
| `last_updated` | Horodatage de la dernière génération et synchronisation de cette recommandation. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Endpoint parameters" }

## Endpoints Amplitude courants {#common-amplitude-endpoints}

### Obtenir une recommandation {#get-a-recommendation}

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId`
{% endraw %}
#### Exemple de réponse {#example-response}
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### Obtenir plusieurs recommandations {#get-multiple-recommendations}

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId,testRecId2`
{% endraw %}
#### Exemple de réponse
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      },
            {
        "rec_id": "testRecId2",
        "child_rec_id": "testRecId2",
        "items": [
          "bulgogi",
          "bibimbap",
          "kimchi",
          "croffles",
          "samgyeopsal"
        ],
        "is_control": false,
        "recommendation_source": "model2",
        "last_updated": 1608670658
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### Obtenir les propriétés utilisateur {#get-user-properties}

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_amp_props=true`
{% endraw %}
#### Exemple de réponse
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "library": "http/1.0",
      "first_used": "2020-01-13",
      "last_used": "2021-03-24",
      "number_property": 12,
      "boolean_property": true
    },
    "cohort_ids": null
  }
}
```

### Obtenir les ID de cohortes {#get-cohort-ids}

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_cohort_ids=true`
{% endraw %}
#### Exemple de réponse
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": ["cohort1", "cohort3", "cohort7"]
  }
}
```

### Obtenir un calcul unique {#get-a-single-computation}

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&comp_id=testCompId`
{% endraw %}
#### Exemple de réponse
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

### Obtenir tous les calculs {#get-all-computations}

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_computations=true`
{% endraw %}
#### Exemple de réponse
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-1": "5000000.0",
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

