---
nav_title: ActionIQ
article_title: ActionIQ
description: "이 참조 문서에서는 Braze와 ActionIQ 통합에 대해 다룹니다. ActionIQ는 마케터, 분석가, 기술자를 위한 엔터프라이즈 고객 데이터 플랫폼입니다. 이 통합을 통해 브랜드는 ActionIQ 데이터를 Braze에 직접 동기화하고 매핑할 수 있습니다."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

> [ActionIQ](https://www.actioniq.com/)는 엔터프라이즈 브랜드를 위한 고객 데이터 플랫폼으로, 마케터가 고객 경험의 모든 접점에서 데이터를 쉽고 안전하게 활성화할 수 있는 방법을 제공합니다. ActionIQ의 고유한 컴포저블 아키텍처를 통해 데이터는 원래 위치에 안전하게 보관되며, 마케팅 팀은 필요한 도구만 사용할 수 있습니다.

_이 통합은 ActionIQ에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 ActionIQ 통합을 통해 브랜드는 ActionIQ 데이터를 Braze에 직접 동기화하고 매핑하여, 전체 고객 데이터를 기반으로 탁월한 고객 경험을 전달할 수 있습니다. 사용 가능한 통합을 통해 사용자는 다음을 수행할 수 있습니다:

- ActionIQ에서 직접 오디언스 멤버십 정보 및 모든 속성으로 Braze의 고객 프로필을 업데이트
- ActionIQ에서 추적한 이벤트를 실시간으로 Braze에 전달하여 개인화된 타겟 Campaign을 트리거
- ActionIQ 여정의 터치포인트에서 직접 Braze의 API 트리거 Campaign을 전달

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| ActionIQ 계정 | 이 통합을 활용하려면 ActionIQ 계정이 필요합니다. |
| Braze REST API 키 | 해당 통합에 필요한 권한이 있는 Braze REST API 키. 자세한 내용은 각 요구 사항 섹션을 참조하세요. <br><br>이 키는 Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integrations}

### 오디언스 멤버십 {#audience-membership}

이 통합은 Braze 프로필이 Segment에 속하는지 여부를 나타내는 커스텀 속성을 생성하여 ActionIQ 오디언스 멤버십을 Braze에 동기화하는 데 사용됩니다. 각 ActionIQ 오디언스는 고유한 부울 커스텀 속성에 해당합니다.

생성되는 커스텀 속성의 표준 명명 규칙은 다음과 같습니다: `AIQ_<Audience ID>_<Split ID>`.

이러한 사용자의 Segment를 생성하려면 다음을 수행하세요:
1. Braze에서 **Segments**로 이동합니다.
2. 새 Segment를 생성합니다.
3. 필터로 **커스텀 속성**를 선택합니다.
4. 여기에서 ActionIQ 커스텀 속성을 선택합니다.
5. Segment가 생성되면 Campaign 또는 Canvas를 생성할 때 오디언스 필터로 선택할 수 있습니다.

또한 이 통합은 Braze 고객 프로필의 모든 커스텀 또는 표준 속성을 ActionIQ 속성 값으로 업데이트합니다.

#### 요구 사항 {#requirements}

`users.track` 및 `user.export.ids` 권한이 있는 Braze REST API 키가 필요합니다. 이 키는 Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다.

ActionIQ에서 REST API 키와 Braze REST 엔드포인트를 제공하여 Braze 연결을 설정합니다.

Braze 플랫폼의 소비자와 매칭하려면 활성화 설정에 다음 식별자가 포함되어야 합니다:
- `braze_id`
- `external_id`

### 이벤트 {#events}

ActionIQ 플랫폼을 구성하여 스트리밍 수집 서비스를 통해 이벤트 정보를 수신할 수 있습니다. 이 통합 옵션은 이러한 이벤트를 Braze에 전달하여 마케터가 오케스트레이션이나 마케팅 캠페인 트리거에 사용할 수 있도록 합니다. 이벤트 통합은 이벤트 페이로드의 등록정보 일부로 추가 ActionIQ 속성을 전송할 수 있습니다.

#### 요구 사항

`users.track` 및 `user.export.ids` 권한이 있는 Braze REST API 키가 필요합니다. 이 키는 Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다.

이벤트 통합은 다음 정보를 Braze에 전송합니다:
- 이벤트 이름
- 소비자 식별자(`braze_id` 또는 `external_id`)
- 타임스탬프
- 이벤트 등록정보(내보내기 설정의 추가 속성으로 채워짐)

### 트리거된 Campaign {#triggered-campaigns}

이 통합은 ActionIQ Segment의 모든 사용자를 대상으로 Braze에서 Campaign을 트리거합니다. Campaign의 문구, 다변량 테스트 및 재자격 규칙을 구성한 후, 내보내기 설정에 Braze Campaign ID를 추가하여 모든 ActionIQ 여정 터치포인트에서 트리거할 수 있습니다.

선택적으로, 내보내기에 다른 ActionIQ 속성을 포함하여 Campaign 문구를 채울 수 있습니다. 이러한 속성은 `trigger_properties` 오브젝트와 함께 전송됩니다.

#### 요구 사항

`campaigns.trigger.send` 및 `campaigns.list` 권한이 있는 Braze REST API 키가 필요합니다. 이 키는 Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다.

ActionIQ에서 Braze로 내보내기 시 다음 값을 전송해야 합니다:
- 소비자 식별자(`braze_id` 또는 `external_id`)
- Campaign ID