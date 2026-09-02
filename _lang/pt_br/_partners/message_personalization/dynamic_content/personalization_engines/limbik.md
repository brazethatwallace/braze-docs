---
nav_title: Limbik
article_title: Limbik
description: "Este artigo de referência descreve a parceria entre a Braze e a Limbik, uma camada de ressonância de IA que prevê como os públicos interpretam e respondem a mensagens usando públicos sintéticos e previsões."
alias: /partners/limbik/
page_type: partner
search_tag: Partner
---

# Limbik

> A [Limbik](https://limbik.com/cognitive-ai) é sua camada de ressonância de IA — prevendo como públicos reais interpretam e respondem a mensagens, conceitos e saídas de IA antes que cheguem ao mercado. Alimentada por pesquisas primárias contínuas em mais de 60 países e mais de 25 idiomas, a Limbik oferece públicos sintéticos validados por humanos — populações digitais que simulam a resposta real do público na velocidade de máquina e com precisão de nível de pesquisa (intervalo de confiança de 95%, margem de erro de 1,5% a 3%). A Limbik oferece a capacidade de garantir imediatamente que suas mensagens ressoem com o que seu público-alvo acredita e sente.

_Essa integração é mantida pela Limbik._

## Pré-requisitos {#prerequisites}

Os itens a seguir são necessários para usar a Limbik com a Braze:

| Requisitos | Descrição |
| --- | --- |
| `account_id` da Limbik | Fale com a equipe de conta da Limbik ou faça uma solicitação GET para o endpoint `/rest/api/organizations` da Limbik |
| Token de acesso da Limbik (`access_token`) | Faça uma solicitação POST para o endpoint `login` da Limbik e use o valor `access_token` retornado como token Bearer no cabeçalho `Authorization`. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões de "Messages". Crie uma no dashboard da Braze em **Settings** > **API Keys**. |
| `campaign_id` da Braze | Acesse **Messaging** > **Campaigns** e selecione uma Campaign. Se a Campaign desejada ainda não existir, crie uma e salve-a. Na parte inferior da página da Campaign, encontre o identificador de API da Campaign. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

Antes de usar qualquer um dos endpoints de previsão, você deve primeiro identificar a qual organização (`account_id`) você tem acesso. Embora a maioria dos clientes tenha apenas uma organização, algumas contas podem ter várias organizações disponíveis.

{% details Recuperar organizações disponíveis %}

Consulte o endpoint de organizações para recuperar suas organizações disponíveis:

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/organizations' \
  -H 'accept: application/json'
```

{% enddetails %}

{% details Exemplo de resposta %}

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

Selecione o `uid` da organização desejada para usar como cabeçalho `account_id` em todas as solicitações de API subsequentes.

{% enddetails %}

## Autenticação {#authentication}

Para acessar os endpoints da API, você precisa de um token bearer para autenticação. Obtenha seu token autenticando-se com suas credenciais.

{% details Solicitação de login %}

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

{% details Exemplo de resposta %}

A resposta contém um `access_token` que você pode usar como token bearer em todas as solicitações de API subsequentes:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer"
}
```

Inclua esse token no cabeçalho `Authorization` para todas as solicitações de API:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

{% alert note %}
Você pode usar plataformas de API como o Postman para configurar fluxos de trabalho automatizados que chamam vários endpoints da REST API de diferentes organizações, como o fluxo de trabalho a seguir.
{% endalert %}

{% enddetails %}

## Caso de uso - Geração de texto de mensagem {#use-case-generating-message-copy}

Usando os endpoints da REST API da Braze e da Limbik, você pode usar as previsões generativas da Limbik para criar textos de mensagem e enviá-los pelos canais de envio de mensagens da Braze, ou ajustar textos existentes para melhorar o impacto no seu público. Ambas as plataformas expõem funcionalidades que você pode chamar programaticamente para construir fluxos de trabalho sofisticados.

Esta documentação descreve dois exemplos: gerar texto de mensagem na Limbik e usar esse texto em uma mensagem subsequente enviada pela Braze, bem como usar a Limbik para avaliar a qualidade de uma determinada mensagem para o público escolhido.

{% details Solicitação de previsão generativa da Limbik %}

Use esse endpoint para gerar uma mensagem e retorná-la em um modelo de previsão. Exemplo de solicitação:

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/forecasts/generate/template?prompt=YOUR_PROMPT' \
  -H 'account_id: YOUR_ACCOUNT_ID' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'accept: application/json'
```

Substitua `YOUR_PROMPT`, `YOUR_ACCOUNT_ID` e `YOUR_ACCESS_TOKEN` pelo texto do seu prompt, ID da organização (do endpoint de organizações) e token bearer do endpoint de login.

{% enddetails %}

{% details Exemplo de resposta %}

Exemplo de resposta do modelo de previsão da Limbik:

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

O elemento-chave para esse caso de uso é o campo `additionalDetail`, que contém o texto da mensagem gerado pela Limbik.

Use esse valor para preencher uma mensagem enviada à Braze. Por exemplo, com o endpoint POST `/campaigns/trigger/send`, use `additionalDetail` para preencher um campo de carga útil. Com o endpoint POST `/messages/send`, use-o para preencher o objeto de mensagem de sua escolha.

{% enddetails %}

### Campos de resposta {#response-fields}

A resposta contém os seguintes campos principais:

- **`type`:** O tipo de mensagem (por exemplo, `"Generate"` para conteúdo gerado por IA, `"Message"` para mensagens validadas)
- **`displayText`:** Um título curto ou resumo da mensagem
- **`additionalDetail`**: **O texto completo da mensagem gerada por IA** — Este é o campo principal que contém o texto completo da mensagem que você pode enviar pela sua plataforma de envio de mensagens
- **`population`:** O público-alvo e os segmentos para esta mensagem

### Uso com a Braze {#using-with-braze}

O campo `additionalDetail` da resposta da Limbik contém o texto da mensagem que você envia à Braze. Um padrão de integração comum é passar esse valor em `trigger_properties.payload` ao chamar o endpoint de envio por gatilho da Braze. No exemplo a seguir, substitua `{{additionalDetail}}` pela string real do campo `additionalDetail` da Limbik e substitua `{{YOUR_CAMPAIGN_ID}}` pelo ID da sua Campaign.

### Exemplo de solicitação de mensagem por gatilho da Braze {#braze-trigger-message-request-example}

```json
{
  "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
  "trigger_properties": {
    "payload": "{{additionalDetail}}"
  },
  "broadcast": true
}
```

## Caso de uso - Detalhes do público sintético {#use-case-synthetic-audience-details}

Para expandir o primeiro caso de uso, utilize o endpoint da Limbik `/rest/api/populations/{account_id}/{population_id}`.

Esse endpoint retorna pontos de dados importantes que descrevem a composição dos públicos sintéticos da Limbik, como gênero, local e assim por diante. Você pode usar esses valores para preencher objetos de Connected Audience ao chamar os endpoints de envio de mensagens da Braze.

{% alert note %}
Os objetos de Connected Audience não podem segmentar usuários com base nos atributos "padrão" da Braze, então você deve armazenar quaisquer atributos que deseja segmentar na Braze como atributos personalizados.
{% endalert %}

Para obter pontuações de previsão para segmentos específicos, identifique os países disponíveis e seus segmentos correspondentes.

### Etapa 1: Listar países disponíveis {#step-1-list-available-countries}

Recupere a lista de países disponíveis para sua conta:

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/populations/list/aca61bd5-7132-499c-946e-42d092cc1156' \
  -H 'accept: application/json'
```

Na resposta, identifique o país que deseja usar. Por exemplo, os Estados Unidos têm um `id` de `56`.

### Etapa 2: Recuperar segmentos disponíveis {#step-2-retrieve-available-segments}

Após recuperar o ID do país, recupere a lista completa de segmentos para esse país.

{% details Exemplo de chamada %}

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/populations/aca61bd5-7132-499c-946e-42d092cc1156/56' \
  -H 'accept: application/json'
```

{% alert note %}
A resposta pode ser grande. Armazene esses dados em cache (por exemplo, no Redis) por nome ou chave para melhor desempenho.
{% endalert %}

{% enddetails %}

{% details Exemplo de resposta %}

Por exemplo, para segmentar mulheres na população adulta dos EUA:

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
- Os segmentos são especificados usando um formato simplificado de chave composta (por exemplo, `gender::female`).
- A chave composta completa da resposta da API (`us2::gender::female`) é abreviada para apenas o nome da categoria e do Segment.
- Para uma referência completa de populações e segmentos disponíveis, consulte [Limbik audiences](https://audiences.limbik.com/).
{% endalert %}

Usando o valor da chave composta para a mensagem de previsão escolhida, você pode mapear esses descritores de público sintético para valores em perfis de usuários reais na Braze.

Por exemplo, você pode usar a chave composta (`fr1::education_level::master_s_degree`) em um objeto de Connected Audience da Braze da seguinte forma:

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

## Caso de uso - Avaliação da pontuação de previsão {#use-case-evaluating-forecast-score}

Você pode usar a Limbik para criar uma pontuação estimada para uma mensagem em relação a um público sintético. Faça isso programaticamente com o endpoint `forecasts/synchronous` da Limbik.

### Opção 1 - Previsão síncrona {#option-1-synchronous-forecast}

Você pode usar a carga útil de resposta da geração de modelo diretamente com o endpoint de previsão síncrona:

{% details Exemplo de solicitação genérica %}

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

{% details Exemplo de resposta (abreviada) %}

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

### Opção 2: Preparar carga útil de previsão com segmentos {#option-2-prepare-forecast-payload-with-segments}

Crie sua carga útil de previsão usando os segmentos selecionados. Os segmentos usam um formato simplificado de chave composta.

{% details Exemplo de solicitação específica por Segment %}

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