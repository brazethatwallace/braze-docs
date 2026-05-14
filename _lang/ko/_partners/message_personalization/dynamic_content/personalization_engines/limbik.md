---
nav_title: Limbik
article_title: Limbik
description: "이 참조 문서에서는 Braze와 Limbik 간의 파트너십을 설명합니다. Limbik은 합성 오디언스와 예측을 사용하여 오디언스가 메시지를 어떻게 해석하고 반응하는지 예측하는 AI 공명 레이어입니다."
alias: /partners/limbik/
page_type: partner
search_tag: Partner
---

# Limbik

> [Limbik](https://limbik.com/cognitive-ai)은 실제 오디언스가 메시지, 개념, AI 출력을 시장에 도달하기 전에 어떻게 해석하고 반응하는지 예측하는 AI 공명 레이어입니다. 60개 이상의 국가와 25개 이상의 언어에 걸친 지속적인 1차 연구를 기반으로, Limbik은 인간 검증 합성 오디언스를 제공합니다. 이는 머신 속도와 연구 수준의 정확도(95% 신뢰도, 1.5%~3% 오차 범위)로 실제 오디언스 반응을 시뮬레이션하는 디지털 집단입니다. Limbik을 사용하면 메시지가 타겟 오디언스의 신념과 감정에 공감하는지 즉시 확인할 수 있습니다.

_이 통합은 Limbik에서 유지 관리합니다._

## 필수 조건 {#prerequisites}

Braze에서 Limbik을 사용하려면 다음이 필요합니다:

| 요구 사항 | 설명 |
| --- | --- |
| Limbik `account_id` | Limbik 계정 팀에 문의하거나, Limbik의 `/rest/api/organizations` 엔드포인트에 GET 요청을 보내세요. |
| Limbik 액세스 토큰(`access_token`) | Limbik의 `login` 엔드포인트에 POST 요청을 보내고, 반환된 `access_token` 값을 `Authorization` 헤더의 Bearer 토큰으로 사용하세요. |
| Braze REST API 키 | "Messages" 권한이 있는 Braze REST API 키. Braze 대시보드에서 **Settings** > **API Keys**로 이동하여 생성하세요. |
| Braze `campaign_id` | **Messaging** > **Campaigns**로 이동하여 Campaign을 선택하세요. 원하는 Campaign이 아직 없으면 새로 생성하고 저장하세요. Campaign 페이지 하단에서 Campaign API 식별자를 찾을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

예측 엔드포인트를 사용하기 전에 먼저 접근 가능한 조직(`account_id`)을 확인해야 합니다. 대부분의 고객은 하나의 조직만 가지고 있지만, 일부 계정에는 여러 조직이 있을 수 있습니다.

{% details 사용 가능한 조직 조회 %}

조직 엔드포인트를 쿼리하여 사용 가능한 조직을 조회하세요:

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/organizations' \
  -H 'accept: application/json'
```

{% enddetails %}

{% details 응답 예시 %}

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

원하는 조직의 `uid`를 선택하여 이후 모든 API 요청의 `account_id` 헤더로 사용하세요.

{% enddetails %}

## 인증 {#authentication}

API 엔드포인트에 접근하려면 인증을 위한 Bearer 토큰이 필요합니다. 자격 증명으로 인증하여 토큰을 발급받으세요.

{% details 로그인 요청 %}

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

{% details 응답 예시 %}

응답에는 이후 모든 API 요청에서 Bearer 토큰으로 사용할 수 있는 `access_token`이 포함됩니다:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer"
}
```

모든 API 요청의 `Authorization` 헤더에 이 토큰을 포함하세요:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

{% alert note %}
Postman과 같은 API 플랫폼을 사용하여 다음 워크플로와 같이 여러 조직의 REST API 엔드포인트를 호출하는 자동화된 워크플로를 설정할 수 있습니다.
{% endalert %}

{% enddetails %}

## 사용 사례 - 메시지 카피 생성 {#use-case-generating-message-copy}

Braze와 Limbik의 REST API 엔드포인트를 함께 사용하면, Limbik의 생성형 예측을 활용하여 메시지 카피를 만들고 Braze 메시징 채널을 통해 전송하거나, 기존 카피를 조정하여 오디언스에 대한 영향력을 높일 수 있습니다. 두 플랫폼 모두 프로그래밍 방식으로 호출할 수 있는 기능을 제공하여 정교한 워크플로를 구축할 수 있습니다.

이 문서에서는 두 가지 예시를 설명합니다: Limbik에서 메시지 카피를 생성하고 이를 Braze를 통해 전송하는 후속 메시지에 사용하는 방법, 그리고 Limbik을 사용하여 선택한 오디언스에 대한 특정 메시지의 품질을 평가하는 방법입니다.

{% details Limbik 생성형 예측 요청 %}

이 엔드포인트를 사용하여 메시지를 생성하고 예측 템플릿으로 반환합니다. 요청 예시:

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/forecasts/generate/template?prompt=YOUR_PROMPT' \
  -H 'account_id: YOUR_ACCOUNT_ID' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'accept: application/json'
```

`YOUR_PROMPT`, `YOUR_ACCOUNT_ID`, `YOUR_ACCESS_TOKEN`을 각각 프롬프트 텍스트, 조직 ID(조직 엔드포인트에서 확인), 로그인 엔드포인트에서 발급받은 Bearer 토큰으로 교체하세요.

{% enddetails %}

{% details 응답 예시 %}

Limbik 예측 템플릿 응답 예시:

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

이 사용 사례의 핵심 요소는 Limbik이 생성한 메시지 카피가 포함된 `additionalDetail` 필드입니다.

이 값을 사용하여 Braze로 전송하는 메시지를 채울 수 있습니다. 예를 들어, POST `/campaigns/trigger/send` 엔드포인트에서 `additionalDetail`을 사용하여 페이로드 필드를 채우거나, POST `/messages/send` 엔드포인트에서 원하는 메시지 오브젝트를 채울 수 있습니다.

{% enddetails %}

### 응답 필드 {#response-fields}

응답에는 다음과 같은 주요 필드가 포함됩니다:

- **`type`:** 메시지 유형(예: AI 생성 콘텐츠의 경우 `"Generate"`, 검증된 메시지의 경우 `"Message"`)
- **`displayText`:** 메시지의 짧은 제목 또는 요약
- **`additionalDetail`**: **완전한 AI 생성 메시지 카피** - 메시징 플랫폼을 통해 전송할 수 있는 전체 메시지 텍스트가 포함된 기본 필드입니다
- **`population`:** 이 메시지의 대상 집단 및 Segments

### Braze와 함께 사용하기 {#using-with-braze}

Limbik 응답의 `additionalDetail` 필드에는 Braze로 전송할 메시지 카피가 포함되어 있습니다. 일반적인 통합 패턴은 Braze 트리거 전송 엔드포인트를 호출할 때 해당 값을 `trigger_properties.payload`에 전달하는 것입니다. 다음 예시에서 `{{additionalDetail}}`을 Limbik의 `additionalDetail` 필드에서 가져온 실제 문자열로, `{{YOUR_CAMPAIGN_ID}}`를 Campaign ID로 교체하세요.

### Braze 트리거 메시지 요청 예시 {#braze-trigger-message-request-example}

```json
{
  "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
  "trigger_properties": {
    "payload": "{{additionalDetail}}"
  },
  "broadcast": true
}
```

## 사용 사례 - 합성 오디언스 세부 정보 {#use-case-synthetic-audience-details}

첫 번째 사용 사례를 확장하여 Limbik의 `/rest/api/populations/{account_id}/{population_id}` 엔드포인트를 사용하세요.

이 엔드포인트는 성별, 위치 등 Limbik 합성 오디언스의 구성을 설명하는 주요 데이터 포인트를 반환합니다. 이러한 값을 사용하여 Braze의 메시징 엔드포인트를 호출할 때 Connected Audience 오브젝트를 채울 수 있습니다.

{% alert note %}
Connected Audience 오브젝트는 Braze의 "기본" 속성을 기반으로 사용자를 타겟팅할 수 없으므로, 타겟팅하려는 속성을 Braze에 커스텀 속성으로 저장해야 합니다.
{% endalert %}

특정 Segments에 대한 예측 점수를 얻으려면 사용 가능한 국가와 해당 Segments를 확인하세요.

### 1단계: 사용 가능한 국가 목록 조회 {#step-1-list-available-countries}

계정에서 사용 가능한 국가 목록을 조회하세요:

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/populations/list/aca61bd5-7132-499c-946e-42d092cc1156' \
  -H 'accept: application/json'
```

응답에서 사용하려는 국가를 확인하세요. 예를 들어, 미국의 `id`는 `56`입니다.

### 2단계: 사용 가능한 Segments 조회 {#step-2-retrieve-available-segments}

국가 ID를 조회한 후 해당 국가의 전체 Segments 목록을 조회하세요.

{% details 호출 예시 %}

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/populations/aca61bd5-7132-499c-946e-42d092cc1156/56' \
  -H 'accept: application/json'
```

{% alert note %}
응답이 클 수 있습니다. 더 나은 성능을 위해 이 데이터를 이름이나 키로 캐시(예: Redis)하세요.
{% endalert %}

{% enddetails %}

{% details 응답 예시 %}

예를 들어, 미국 성인 집단에서 여성을 타겟팅하려면:

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
- Segments는 간소화된 복합 키 형식(예: `gender::female`)을 사용하여 지정됩니다.
- API 응답의 전체 복합 키(`us2::gender::female`)는 카테고리와 Segment 이름만으로 축약됩니다.
- 사용 가능한 집단 및 Segments의 전체 참조는 [Limbik 오디언스](https://audiences.limbik.com/)를 확인하세요.
{% endalert %}

선택한 예측 메시지의 복합 키 값을 사용하여 이러한 합성 오디언스 설명자를 Braze의 실제 고객 프로필 값에 매핑할 수 있습니다.

예를 들어, 복합 키(`fr1::education_level::master_s_degree`)를 Braze Connected Audience 오브젝트에서 다음과 같이 사용할 수 있습니다:

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

## 사용 사례 - 예측 점수 평가 {#use-case-evaluating-forecast-score}

Limbik을 사용하여 합성 오디언스에 대한 메시지의 예상 점수를 생성할 수 있습니다. Limbik의 `forecasts/synchronous` 엔드포인트를 사용하여 프로그래밍 방식으로 수행하세요.

### 옵션 1 - 동기식 예측 {#option-1-synchronous-forecast}

템플릿 생성의 응답 페이로드를 동기식 예측 엔드포인트에 직접 사용할 수 있습니다:

{% details 일반 요청 예시 %}

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

{% details 응답 예시(축약) %}

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

### 옵션 2: Segments를 포함한 예측 페이로드 준비 {#option-2-prepare-forecast-payload-with-segments}

선택한 Segments를 사용하여 예측 페이로드를 생성하세요. Segments는 간소화된 복합 키 형식을 사용합니다.

{% details Segment별 요청 예시 %}

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