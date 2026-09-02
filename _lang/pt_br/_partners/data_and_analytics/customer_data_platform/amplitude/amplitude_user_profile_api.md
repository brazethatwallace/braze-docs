---
nav_title: Amplitude e Conteúdo conectado
article_title: Amplitude e Conteúdo conectado
page_order: 0
alias: /partners/amplitude_api_endpoints/
page_type: partner
description: "A API or interface de programação do aplicativo (API) de Perfil de usuário da Amplitude fornece perfis de usuário da Amplitude. Isso inclui propriedades do usuário, propriedades computadas do usuário, uma lista de IDs de coortes que incluem o usuário e recomendações."
search_tag: Partner

---

# Amplitude e Conteúdo conectado {#amplitude-and-connected-content}

> A API or interface de programação do aplicativo (API) de perfil de usuário da Amplitude fornece perfis de usuário da Amplitude. Isso inclui propriedades do usuário, propriedades computadas do usuário, uma lista de IDs de coortes que incluem o usuário e recomendações. A seguir, estão listados os endpoints comuns da API or interface de programação do aplicativo (API) da Amplitude que podem ser usados com Conteúdo conectado.

## Parâmetros do endpoint {#endpoint-parameters}

A tabela a seguir apresenta os parâmetros que podem ser usados em suas chamadas para a API or interface de programação do aplicativo (API) de perfil de usuário.

| Parâmetro | Obrigatório | Descrição |
| --------- | -------- | ----------- |
| `user_id` | Opcional | ID do usuário (ID do banco de dados externo) a ser consultado, obrigatório a menos que `device_id` esteja definido. |
| `device_id` | Opcional | ID do dispositivo (ID anônimo) a ser consultado, obrigatório a menos que `user_id` esteja definido. |
| `get_recs` | Opcional<br>(O padrão é false) | Retorna um resultado de recomendação para esse usuário. |
| `rec_id` | Opcional | Recomendação(ões) a ser(em) recuperada(s), obrigatória(s) se `get_recs` for verdadeiro. Várias recomendações podem ser obtidas separando os `rec_ids` com vírgulas. |
| `rec_type` | Opcional | Substitui a configuração de controle experimental padrão; `rec_type=model` retorna recomendações modeladas, e `rec_type=random` retorna recomendações aleatórias. Outras opções podem existir no futuro. |
| `get_amp_props` | Opcional<br>(O padrão é false) | Retorna um conjunto completo de propriedades do usuário para esse usuário, sem incluir cálculos. |
| `get_cohort_ids` | Opcional<br>(O padrão é false) | Retorna uma lista de todos os IDs de coorte dos quais esse usuário faz parte e que foram configurados para rastreamento. Por padrão, a participação na coorte não é rastreada para usuários de qualquer coorte. |
| `get_computations` | Opcional<br>(O padrão é false) | Retorna uma lista de todos os cálculos que estão ativados para esse usuário. |
| `comp_id` | Opcional | Retorna um único cálculo que pode estar ativado para esse usuário. Retornará um valor nulo se não existir. Se `get_computations` for verdadeiro, todos os valores serão buscados, inclusive esse (a menos que seja arquivado ou excluído). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Endpoint parameters" }

A tabela a seguir abrange os parâmetros que você normalmente espera ver nas respostas da Amplitude.

| Parâmetro de resposta | Descrição |
| ------------------ | ----------- |
| `rec_id` | O ID da recomendação solicitada. |
| `child_rec_id` | Um ID de recomendação mais detalhado que a Amplitude pode usar no backend como parte de um experimento interno para melhorar o desempenho do modelo. Na maioria dos casos, será igual a `rec_id`. |
| `items` | Lista de recomendações para esse usuário. |
| `is_control` | true se esse usuário fizer parte do grupo de controle. |
| `recommendation_source` | Nome do modelo que foi usado para gerar essa recomendação. |
| `last_updated` | Registro de data e hora de quando essa recomendação foi gerada e sincronizada pela última vez. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Endpoint parameters" }

## Endpoints comuns da Amplitude {#common-amplitude-endpoints}

### Obter uma recomendação {#get-a-recommendation}

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId`
{% endraw %}
#### Exemplo de resposta {#example-response}
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

### Obter várias recomendações {#get-multiple-recommendations}

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId,testRecId2`
{% endraw %}
#### Exemplo de resposta
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

### Obter propriedades do usuário {#get-user-properties}

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_amp_props=true`
{% endraw %}
#### Exemplo de resposta
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

### Obter IDs de coorte {#get-cohort-ids}

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_cohort_ids=true`
{% endraw %}
#### Exemplo de resposta
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

### Obter um único cálculo {#get-a-single-computation}

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&comp_id=testCompId`
{% endraw %}
#### Exemplo de resposta
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

### Obter todos os cálculos {#get-all-computations}

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_computations=true`
{% endraw %}
#### Exemplo de resposta
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

