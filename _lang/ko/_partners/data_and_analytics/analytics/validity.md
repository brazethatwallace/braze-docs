---
nav_title: Validity
article_title: Validity
alias: /partners/validity/
description: "이 참조 문서에서는 이메일 전달 가능성 플랫폼인 Validity와 Braze 간의 파트너십에 대해 설명합니다. 이 통합은 Everest 시드 목록을 Braze에 동기화하고 Campaigns 및 Canvases에 대한 받은편지함 배치 테스트를 자동화합니다."
page_type: partner
search_tag: Partner
---

# Validity

> [Validity Everest](https://www.validity.com/everest/)는 받은편지함 배치를 측정하고 발신 평판을 보호하는 데 도움이 되는 이메일 전달 가능성 플랫폼입니다. Braze와 Validity 통합은 Everest 시드 목록을 Braze에 동기화하고, 적격한 Campaigns 및 Canvases에 자동으로 시드를 추가하며, 인게이지먼트 측정기준을 Validity Inbox로 가져와 시드 기반 배치와 실제 가입자 인게이지먼트를 비교할 수 있도록 합니다.

_이 통합은 Validity에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Validity는 Braze에서 이메일 시드 목록 사용자를 생성하고 유지 관리하여 시드 주소가 활성 상태이고 억제되지 않도록 합니다. Campaign 또는 Canvas에 시드를 추가할 준비가 되면, Validity는 해당 시드 목록에 사본을 보내고 전달, 반송, 열람, 클릭, 탈퇴 등의 인게이지먼트 측정기준을 받은편지함 배치 데이터와 함께 Validity Inbox에 표시합니다.

## 사용 사례 {#use-cases}

### 자동 시딩 {#auto-seeding}

Validity 자동 시딩을 사용하면, Validity가 Braze Campaign 또는 Canvas가 적격 발송량에 도달하는 시점을 감지하고 해당 Campaign 콘텐츠의 사본을 Validity 시드 목록으로 보냅니다. 시드 발송은 `validity_seed` 커스텀 속성이 `true`로 설정된 사용자를 대상으로 합니다.

## 전제 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다:

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Validity 계정 | 이 파트너십을 활용하려면 Validity 계정이 필요합니다. |
| Braze REST API 키 | 다음 권한이 있는 Braze REST API 키: `users.track`, `users.delete`, `email.bounce.remove`, `email.spam.remove`, `campaigns.list`, `campaigns.details`, `campaigns.data_series`, `canvas.list`, `canvas.details`, `canvas.data_series`, `content_blocks.list`, `content_blocks.info`, `messages.send`. <br><br> Braze 대시보드의 **설정** > **API 및 식별자**에서 이 키를 생성합니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/api/basics#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. 예: `rest.iad-01.braze.com`. |
| Braze 앱 식별자 | 시드 발송이 귀속되어야 하는 Braze 앱 식별자입니다. **설정** > **API 및 식별자** > **앱 식별자**에서 찾을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## Validity 통합하기 {#integrating-validity}

### 1단계: Braze 자격 증명을 Validity와 공유하기 {#step-1-share-braze-credentials-with-validity}

Validity는 Braze 대시보드의 **설정** > **API 및 식별자**에서 세 가지 자격 증명이 필요합니다:

- REST API 키([전제 조건](#prerequisites)에 나열된 권한 포함)
- REST 엔드포인트
- 앱 식별자

이러한 자격 증명을 Validity 담당자에게 공유하면, 담당자가 통합 설정을 완료합니다. Validity는 통합을 활성화하기 전에 Braze에 대한 실시간 테스트 호출로 자격 증명을 검증합니다. Validity 담당자가 누구인지 모르는 경우 [support@validity.com](mailto:support@validity.com)으로 이메일을 보내세요.

통합이 활성화되면 Validity는 반복 주기(10분마다)로 Everest 시드 목록을 Braze에 동기화합니다. Validity는 Braze에서 시드 사용자를 생성, 업데이트 및 제거하여 Everest의 현재 시드 목록과 일치하도록 유지합니다.

### 2단계: 선택적으로 Validity 시드 사용자를 위한 Braze Segment 생성하기 {#step-2-optionally-create-a-braze-segment-for-validity-seed-users}

Segment 생성은 선택 사항입니다. 자동 시딩은 적격 발송이 감지될 때마다 `validity_seed` 커스텀 속성으로 필터링된 [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience) 객체를 사용하여 테스트 이메일을 보냅니다. Segment를 구축하거나 Campaigns에 첨부할 필요가 없습니다.

Braze 내에서 이 오디언스를 참조용으로 보려면 **오디언스** > **Segments**에서 `validity_seed`가 `true`인 필터로 Segment를 생성합니다.

Validity는 다음 스키마를 사용하여 [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 엔드포인트를 통해 사용자를 생성합니다:

```bash
curl -X POST "https://YOUR_API_ENDPOINT/users/track" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_BRAZE_API_KEY" \
  -d '{
    "attributes": [
      {
        "email": "example1@example.com",
        "validity_seed": true
      },
      {
        "email": "example2@example.com",
        "validity_seed": true
      }
    ],
    "events": [
      {
        "email": "example1@example.com",
        "name": "validity_seed_event",
        "time": "2026-07-02T18:00:00.000Z"
      }
    ]
  }'
```

이러한 사용자에는 항상 부울 값 `true`가 설정된 커스텀 속성 `validity_seed`가 포함됩니다. Validity는 또한 각 시드 사용자에 대해 `validity_seed_event` 커스텀 이벤트를 전송하여 Braze 계정에서 활성 사용자로 등록되도록 합니다.

## 고려 사항 {#considerations}

### 시드 발송 작동 방식 {#how-seed-sends-work}

Validity는 Campaign 및 Canvas 세부 정보 엔드포인트를 통해 Campaign 본문, 제목, 발신 주소를 가져온 다음, Braze [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) 엔드포인트를 통해 해당 콘텐츠의 사본을 시드 목록에 전달합니다. Braze 대시보드에는 원래 Campaign만 계속 표시됩니다.

### 자동 시딩 임계값 {#auto-seeding-threshold}

Validity는 Campaign 또는 Canvas가 구성된 발송량 임계값(기본값 10,000건)을 초과하는 시점을 감지하고 해당 시점에 시드 테스트를 보냅니다. Campaigns 또는 Canvases에 시드 오디언스를 추가할 필요가 없습니다.

시드 테스트는 시드 목록의 주소로 이메일 Campaign을 보내고, 배치 데이터를 수집하며, 오디언스에게 발송하기 전이나 발송과 동시에 문제를 식별하는 데 도움이 됩니다. 받은편지함 배치 측정기준은 Campaign이 받은편지함, 스팸 폴더에 도착하는지 또는 누락되는지를 보여줍니다. 이러한 측정기준을 사용하여 받은편지함 배치를 확인하고 전달 가능성 문제를 파악합니다.

시드 테스트는 이메일이 스팸 폴더에 들어가거나 누락되는 이유를 진단하는 데도 도움이 됩니다. 헤더 데이터, 인증(SPF, DKIM, DMARC), 링크 유효성 검사, 디자인 렌더링을 확인하면 받은편지함 배치율을 개선하기 위해 어떤 조치를 취해야 하는지 알 수 있습니다.

### 시드 목록 상태 {#seed-list-health}

Validity는 시드 목록 사용자를 모니터링하며, 효과가 떨어지기 시작하면(예: 이메일 서비스 공급자(ESP)가 시드 목록 오디언스 구성원을 스팸으로 표시하기 시작하는 경우) 업데이트하거나 제거할 수 있습니다. 이러한 권한을 통해 Validity는 시드 목록 상태를 모니터링하고 그에 따라 목록을 업데이트할 수 있습니다.

### 동적 콘텐츠 처리 방식 {#how-dynamic-content-is-handled}

Braze 이메일은 종종 실제 수신자의 프로필에 연결된 Liquid 개인화를 사용합니다. 시드 주소에는 해당 프로필 데이터가 없기 때문에, Validity는 시딩하기 전에 각 이메일을 새니타이저를 통해 처리합니다. 새니타이저는 Content Blocks를 확인하고, 기본 Liquid 로직을 평가하며, 확인할 수 없는 항목(예: 이름)을 표시되는 `[REDACTED]` 입력 안내로 대체합니다. 실시간 연결된 콘텐츠 API로만 구성된 섹션은 시드에서 빈 상태로 렌더링됩니다.

새니타이저를 켜거나 끌 수 있습니다. 꺼져 있으면 Braze는 실제 수신자에게 하는 것과 동일한 방식으로 시드 발송에 대한 Liquid 개인화를 처리합니다.

### Inbox Aggregate

자동 시딩을 활성화하면 Inbox Aggregate도 활성화됩니다. 이 기능은 실제 Braze 발송(시드 발송과 별도)에서 발송, 전달, 반송, 열람, 클릭, 탈퇴 등의 인게이지먼트 측정기준을 가져와 받은편지함 배치 데이터와 함께 Validity Inbox에 표시합니다. 두 기능은 독립적인 스케줄로 실행되며 별도로 관리할 필요가 없습니다.