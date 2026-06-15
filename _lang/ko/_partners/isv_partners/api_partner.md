---
nav_title: API 파트너 통합
alias: /api_partner_integration/
hidden: true
---

# API 파트너 통합 {#api-partner-integration}

> `User-Agent` 헤더 구문 등 파트너 API 통합의 요구 사항에 대해 알아보세요.

{% alert important %}
이전에는 파트너가 API 요청의 파트너 필드에 자신의 이름을 추가해야 했습니다. 이 형식은 더 이상 지원되지 않으며 이제 `User-Agent` 헤더가 필수입니다.
{% endalert %}

## User agents

트래픽의 소스를 명확하게 식별하는 `User-Agent` 헤더를 포함해야 합니다. 이를 통해 공동 고객이 Braze의 API 사용 보고서에서 파트너 트래픽을 확인할 수 있으며, Braze 엔지니어가 모범 사례를 따르지 않는 통합을 식별할 수 있습니다. 일반적으로 모든 트래픽에 대해 단일 user agent만 사용해야 합니다.

### 구문 {#syntax}

`User-Agent` 헤더는 다음 형식을 준수해야 합니다([RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231#page-46) 표준과 유사합니다):

```bash
User-Agent: partner-OrganizationName
```

다음을 교체하세요:

| 입력 안내 | 설명 |
|-------------|-------------|
| `OrganizationName` | 파스칼 케이스로 형식화된 조직 이름입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Syntax" }

### 예시 {#examples}

예를 들어, 다음은 Snowflake의 클라우드 데이터 수집에 대한 올바른 user agent입니다:

```bash
User-Agent: partner-Snowflake
```

반면 다음은 트래픽의 소스를 명확하게 식별하지 않으므로 올바르지 않습니다:

```bash
User-Agent: axios/1.4.0
```
