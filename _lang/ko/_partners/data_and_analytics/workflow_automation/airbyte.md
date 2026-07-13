---
nav_title: Airbyte
article_title: Airbyte
description: "이 참조 문서에서는 Braze와 Airbyte 통합에 대해 다룹니다. Airbyte는 데이터 웨어하우스, 레이크, 데이터베이스에 데이터를 통합하고 Airbyte에서 Braze로 실시간 이벤트를 전달하는 데 도움이 되는 오픈소스 데이터 통합 엔진입니다."
alias: /partners/airbyte/
page_type: partner
search_tag: Airbyte

---

# Airbyte

> [Airbyte](https://airbyte.com/)는 데이터 웨어하우스, 레이크, 데이터베이스에 데이터를 통합하는 데 도움이 되는 오픈소스 데이터 통합 엔진입니다.

_이 통합은 Airbyte에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Airbyte 통합을 사용하면 모든 애플리케이션과 데이터베이스를 중앙 웨어하우스에 연결하여 Braze 데이터를 수집하고 분석하는 데이터 파이프라인을 생성할 수 있습니다. 중앙 웨어하우스에 데이터가 수집되면 데이터 팀은 선호하는 비즈니스 인텔리전스 도구를 사용하여 Braze 데이터를 효과적으로 탐색할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Airbyte Cloud 계정 | 이 통합을 활용하려면 [Airbyte Cloud](https://cloud.airbyte.io/workspaces) 계정이 필요합니다. |
| Braze REST API 키 | 모든 권한이 포함된 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합 {#integration}

1. Airbyte Cloud 계정에서 **Sources > + New Source > Set up the Source**로 이동합니다.
2. 소스 이름으로 "Braze"를 입력하고 소스 드롭다운에서 **Braze**를 선택합니다.
3. 엔드포인트 URL, Braze REST API 키, 시작 날짜를 입력합니다. **Set up Source**를 클릭합니다.

### 지원되는 동기화 모드 {#supported-sync-modes}

Airbyte의 Braze 소스 커넥터는 다음 [동기화 모드](https://docs.airbyte.com/cloud/core-concepts#connection-sync-modes)를 지원합니다:
- **Full Refresh | Overwrite**: 소스에서 모든 레코드를 동기화하고 대상의 데이터를 덮어씁니다.
- **Incremental Sync | Append**: 소스에서 새 레코드를 동기화하고 기존 데이터를 삭제하지 않고 대상에 추가합니다.

### 지원되는 스트림 {#supported-streams}

- [`campaigns`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18)
- [`campaigns_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1)
- [`canvases`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1)
- [`canvases_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0fd61e93-7edf-4d87-a8dc-052420aefb73)
- [`events`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1)
- [`events_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c)
- [`kpi_daily_new_users`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#07756c39-cfa0-40a0-8101-03f8791cec01)
- [`kpi_daily_active_users`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#90a64560-65aa-4f71-a8ef-1edf49321986)
- [`kpi_daily_app_uninstalls`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#59c4d592-3e77-42f8-8ff1-d5d250acbeae)
- [`cards`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9fa7a3bc-4a02-4de2-bc4c-8f111750665e)
- [`cards_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8)
- [`segments`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f)
- [`segments_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e)

{% alert note %}
사용량 제한은 스트림에 따라 다릅니다. 자세한 내용은 [사용량 제한 표]({{site.baseurl}}/api/api_limits/#rate-limits-by-request-type)를 참조하세요.
{% endalert %}