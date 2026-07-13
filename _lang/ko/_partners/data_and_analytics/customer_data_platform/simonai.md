---
nav_title: Simon AI
article_title: Simon AI
description: "Braze와 Simon AI 통합을 사용하여 정교한 오디언스를 생성하고 코드 없이 실시간으로 Braze에 동기화하여 오케스트레이션할 수 있습니다."
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# Simon AI

> [Simon AI][1] 에이전틱 마케팅 플랫폼은 마케팅 팀이 진정한 일대일 개인화를 달성할 수 있도록 지원합니다. 컴포저블 CDP와 Snowflake AI Data Cloud에서 직접 작동하는 AI 에이전트를 결합하여 마케터의 데이터 및 실행 팀 역할을 수행합니다.

Braze와 Simon AI 통합을 사용하여 고급 오디언스를 구축하고 Braze에 동기화하여 실시간, 노코드 오케스트레이션을 수행할 수 있습니다. 이 통합을 통해 Simon AI의 ID 확인, 고객 데이터 통합, AI 기반 세분화를 활용하여 다운스트림에서 더욱 개인화되고 효과적인 Braze 캠페인(Campaign)을 구동할 수 있습니다.

## 필수 조건 {#prerequisites}

시작하려면 Simon AI 계정 내에서 Braze 계정을 인증해야 합니다.

| 요구 사항 | 설명 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simon AI | Simon AI 내에서 Braze 통합을 활용하려면 기존 Simon AI 계정이 있어야 합니다. |
| Braze REST API 키 | `users.track`, `campaigns.trigger.schedule.create`, `campaigns.trigger.send` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze 대시보드 URL | [REST 엔드포인트 URL][3]. 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 사용 사례 {#use-cases}

- Braze Canvas 또는 이메일 트리거
- Segment 속성 전달 및 유지
- 특성 및 연락처 속성 동기화

{% alert note %}
Simon과 Braze 통합을 사용할 때 Simon은 각 동기화 시 Braze에 델타만 전송하여 불필요한 데이터에 대한 비용을 방지합니다. 자세한 내용은 [특성 및 연락처 속성 동기화](#sync-traits-and-contact-properties)를 참조하세요.
{% endalert %}

## 통합 {#integration}

### Simon AI에서 Braze 계정 인증 {#authenticate-your-braze-account-in-simon-ai}

Braze 통합을 사용하려면 먼저 Simon에서 Braze 계정을 인증하세요:

1. 내비게이션 메뉴에서 **Integrations**를 클릭한 다음 Braze로 스크롤합니다.
2. Braze [REST API 키][2]와 [대시보드 URL][3]을 입력합니다.
3. **Save Changes**를 클릭합니다.

연결에 성공하면 창에 **Connected**가 표시됩니다.

![Simon AI의 통합 화면][8]{: style="max-width:70%"}

### Simon AI의 플로우 또는 여정에 Braze 액션 추가 {#add-braze-actions-to-flows-or-journeys-in-simon-ai}

Simon AI에서 Braze 계정을 인증한 후 [플로우][4] 및 [여정][5]에 Braze 액션을 추가할 수 있습니다.

세 가지 액션을 사용할 수 있습니다:

- **Simon Segment 속성 동기화**: Segment 세부 정보를 Braze의 신규 또는 기존 커스텀 속성과 동기화합니다.
- **Braze Canvas 트리거**: Simon Segment 데이터를 활용하는 Braze Canvas를 트리거합니다.
- **Braze Campaign 전송**: Simon에서 전체 Braze Campaign을 시작합니다.

![Simon AI에서 사용 가능한 Braze 액션 목록을 보여주는 드롭다운.][9]{: style="max-width:60%"}

일부 액션은 특정 플로우 유형 또는 여정에서만 사용할 수 있습니다. 자세한 내용은 [docs.simondata.com][6]에서 확인하세요.

### 특성 및 연락처 속성 동기화 {#sync-traits-and-contact-properties}

데이터 소비를 최소화하기 위해 Segment의 모든 고객에 대해 모든 필드를 업데이트하는 대신 기본적으로 동기화할 특정 특성을 선택할 수 있습니다.

{% alert note %}
특성 동기화를 시작하려면 [Simon 고객지원 센터](https://docs.simondata.com/docs/support-center)에서 요청을 제출하세요. 계정 매니저가 다음 단계를 진행할 수 있을 때 알려드립니다.
{% endalert %}

계정 매니저가 연락처 특성을 활성화한 후:

1. Simon에서 왼쪽 내비게이션의 **Admin Center**를 확장하고 **Sync Contact Traits**를 선택합니다.
2. **Braze**를 선택합니다. 연락처 속성이 데이터셋별로 중첩되어 표시됩니다.
3. Simon과 Braze 통합을 사용할 때 동기화할 필드를 선택합니다:
   1. **Number of traits**는 해당 데이터셋에서 선택할 수 있는 특성의 수를 나타냅니다. 전체를 선택하거나 행을 확장하여 개별 필드를 선택할 수 있습니다.
   2. 필드 이름이 Braze에 도착할 때 다르게 표시되도록 하려면 **Downstream name**을 편집합니다.
   3. Simon에서 Braze와 처음 통합하는 경우 **Backfill all contacts**를 클릭합니다. 백필은 플로우 또는 여정에서 액션을 처음 사용할 때 모든 데이터 포인트를 Braze에 전송하여 모든 데이터가 완전히 동기화되도록 합니다. 이후 동기화에서는 이 화면에서 선택한 특성만 Braze에 전송됩니다. 이를 통해 필요한 데이터에 대해서만 비용이 청구되도록 할 수 있습니다.

![Simon AI에서 동기화 특성 선택.][10]

[1]: https://www.simon.ai/
[2]: {{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys
[3]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
[4]: https://docs.simondata.com/docs/campaigns-flows
[5]: https://docs.simondata.com/docs/campaigns-journeys-two
[6]: https://docs.simondata.com
[7]: https://docs.simondata.com/docs/support-center
[8]: {% image_buster /assets/img/simon_data/ConnecttoBraze.png %}
[9]: {% image_buster /assets/img/simon_data/BrazeActions.png %}
[10]: {% image_buster /assets/img/simon_data/BrazeTraitSyncing.png %}