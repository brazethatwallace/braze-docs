---
nav_title: Merkury
article_title: Merkury
description: "이 참조 문서에서는 Braze와 Merkury 간의 파트너십을 설명합니다. Merkury는 앱을 위한 엔터프라이즈 ID 플랫폼으로, `MerkuryID`를 활용하여 Braze 고객의 사이트 방문자 인식률을 높일 수 있습니다."
page_type: partner
search_tag: Partner
---

# Merkury

> [Merkury](https://merkury.merkleinc.com/)는 Merkle의 엔터프라이즈 ID 플랫폼으로, 퍼스트파티 쿠키리스 ID 기능을 통해 브랜드가 소비자 참여, 경험, 매출을 극대화할 수 있도록 지원합니다. `MerkuryID`는 브랜드의 알려진 고객과 알려지지 않은 고객 및 잠재 고객 기록, 사이트/앱 방문, 소비자 데이터를 하나의 영구적인 개인 ID로 통합합니다.

_이 통합은 Merkury에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Merkury 통합을 사용하면 `MerkuryID`를 활용하여 Braze 고객의 사이트 방문자 인식률을 높일 수 있습니다. 브랜드 이메일 가입자인 방문자를 인식하면 Merkury는 Braze 프로필을 업데이트하여 해당 가입자의 이메일 주소를 포함시킵니다. `MerkuryID`의 향상된 인식 기능은 인게이지먼트 및 개인화 기회를 개선하고, 사이트 이탈 이메일 발송량과 관련 매출을 즉시 증가시킵니다.

## 사전 요구 사항 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| Merkle 계정 | 이 파트너십을 활용하려면 Merkle 계정이 필요합니다. |
| Merkle 클라이언트 ID | Merkle 담당자에게 클라이언트 ID를 요청하세요. |
| Merkury 태그 | 웹사이트에 Merkle의 Merkury 태그를 설치하세요. |
| Braze REST 및 SDK 엔드포인트 | REST 또는 SDK 엔드포인트 URL입니다. 엔드포인트는 [인스턴스의 Braze URL]({{site.baseurl}}/api/basics#endpoints)에 따라 달라집니다. |
| Braze REST API 키 | `users.track, users.export.ids, users.export.segment, and segments.list` 권한이 있는 Braze REST API 키가 필요합니다. <br><br>이 키는 **Braze 대시보드 > 개발자 콘솔 > REST API 키 > 새 API 키 생성**에서 만들 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사전 요구 사항" }

{% alert important %}
Merkury 신원 커넥터의 Braze 요청은 Braze API 사용량 제한 사양 내에서 작동합니다. 질문이 있는 경우 Braze 또는 Merkle 계정 매니저에게 문의하세요.<br><br>Merkury는 정상적인 세션이 종료될 때 최소 하나의 요청을 전송합니다.
{% endalert %}

## 사이드바이사이드 SDK 통합 {#side-by-side-sdk-integration}

Merkle의 클라이언트 측 Merkury 태그를 사용하여 Braze 기기를 캡처하고, 이를 Merkury ID 커넥터 엔드포인트로 전달하여 식별합니다.

### 1단계: Braze 웹 SDK 태그 설정 {#step-1-setup-braze-web-sdk-tag}

이 통합을 사용하려면 웹사이트에 [Braze 웹 SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-gtm)가 배포되어 있어야 합니다.

### 2단계: Merkle의 Merkury 태그 배포 {#step-2-deploy-merkles-merkury-tag}

웹사이트에 Merkury 태그를 배포하여 Merkury ID 커넥터를 웹사이트에서 사용할 수 있도록 합니다. Merkle 계정 매니저가 자세한 안내 가이드를 제공해 드립니다.

### 3단계: 커스텀 속성 생성 {#step-3-create-custom-attributes}

Merkury ID 커넥터는 다음 필드를 채우며, Braze에서 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)으로 생성해야 합니다.

| 속성 이름 | 데이터 유형 | 설명 |
| --- | --- | --- |
| `hmid` | 문자열 | Merkle의 Merkury ID |
| `confidence_score` | 숫자 | Merkury가 식별할 수 있었던 신뢰도 (1-8, 낮을수록 우수) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="3단계: 커스텀 속성 생성" }

### 4단계: Merkle에 사용자 이메일 유니버스 제공 {#step-4-provide-merkle-with-user-email-universe}

Merkle은 허용 가능한 이메일 유니버스의 세분화 내보내기를 권장합니다. 이후 허용 가능한 활성 사용자의 일별 내보내기를 추가로 진행할 수 있습니다.

다음 필드가 필수입니다:

- `braze_id`
- `external_id`
- 이메일 주소

자세한 내용은 Braze 담당자에게 문의하세요.