---
nav_title: Adikteev
article_title: Adikteev 고객이탈 예측
description: "이 참조 문서에서는 고객이탈 예측과 풀 서비스 앱 리타겟팅을 결합한 사용자 리텐션 엔진인 Adikteev와 Braze 간의 파트너십에 대해 설명합니다."
alias: /partners/adikteev/
page_type: partner
search_tag: Partner

---

# Adikteev 고객이탈 예측 {#adikteev-churn-prediction}

> [Adikteev](https://www.adikteev.com/churn-prediction)는 고객이탈 예측과 풀 서비스 앱 리타겟팅을 결합한 사용자 리텐션 엔진입니다.

_이 통합은 Adikteev에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Braze와 Adikteev 통합을 사용하면 Braze CRM Campaign 내에서 Adikteev의 고객이탈 예측 기술을 활용하여 이탈 위험이 높은 사용자 세그먼트를 우선적으로 타겟팅함으로써 사용자 리텐션을 높일 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| Adikteev 계정 | 이 파트너십을 활용하려면 Adikteev 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 활용 사례 {#use-cases}

{% tabs %}
{% tab 오디언스 필터링 %}
고객이탈 위험도에 따라 오디언스 세그먼트를 세분화합니다.<br> Adikteev에서 전송하는 커스텀 속성의 이름과 값은 구성할 수 있습니다.

![Adikteev에서 보낸 커스텀 속성을 오디언스 세그먼트 필터로 사용하는 방법을 보여주는 스크린샷입니다.]({% image_buster /assets/img/adikteev/audience.png %})
{% endtab %}
{% tab 메시지 타겟팅 %}
수신자의 고객이탈 위험도에 따라 Braze 메시징 Campaign을 커스터마이즈합니다.

![Adikteev에서 보낸 커스텀 속성을 Campaign 타겟팅 필터로 사용하는 예시를 보여주는 스크린샷입니다.]({% image_buster /assets/img/adikteev/campaign.png %})
{% endtab %}
{% endtabs %}

## 통합 {#integration}

### 1단계: 앱의 이벤트 스트림 공유 {#step-1-share-the-event-stream-of-your-app}

앱 오디언스에 대한 고객이탈 예측을 시작하려면 모바일 측정 플랫폼에서 이벤트 포스트백을 활성화해야 합니다. [Adikteev 지원 웹사이트](https://help.adikteev.com/hc/en-us/sections/8185123408914-Data-stream-activation)의 가이드라인을 따라 설정하세요.

### 2단계: Braze REST API 키 생성 {#step-2-create-your-braze-rest-api-key}

Braze에서 **설정** > **API 키**로 이동합니다. **새 API 키 생성**을 선택하고 원하는 API 키 이름을 입력한 후 다음 권한이 추가되었는지 확인합니다:

- `users.track`

### 3단계: Adikteev 팀에 정보 제공 {#step-3-provide-information-to-the-adikteev-team}

통합을 완료하려면 REST API 키와 REST 엔드포인트 URL을 Adikteev 계정 매니저에게 제공해야 합니다. Adikteev가 연결을 설정하고 설정이 완료되면 통합 검증을 위해 연락드립니다.

## 배치 처리 및 사용량 제한 {#batching-and-rate-limits}

`user.track` 엔드포인트는 사용자 세부 정보를 업데이트하는 데 사용됩니다. 엔드포인트의 사용량 제한, 배치 요청 및 요청 세부 정보에 대한 전체 내용은 [API 설명서]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 참조하세요.

{% alert tip %}
API 호출은 변경된 데이터만 업데이트하여 전체 API 호출 수를 줄이는 방식으로 수행해야 합니다. 즉, 고객이탈 세그먼트가 변경된 사용자만 업데이트하세요.
{% endalert %}

## 사용자 및 기기 식별자 {#user-and-device-identifiers}

Braze의 고객 프로필은 모든 유형의 사용자 또는 기기 식별자와 연결할 수 있으며, 사용 가능한 옵션 목록은 Braze와의 데이터 수집 통합 방식에 따라 달라집니다. Adikteev의 경우, 고객이탈 세그먼트 정보를 올바르게 전송하려면 MMP와 Braze의 고객 프로필 간에 공통 식별자를 찾아야 합니다.

## 데이터 보존 및 삭제 {#data-retention-and-deletion}

업데이트가 이루어지지 않으면 속성과 해당 값은 Braze 고객 프로필에 무기한 보존됩니다.

프로필 속성을 제거하려면 `null`로 설정하세요.

## 요청 페이로드 {#request-payloads}

Adikteev에서 Braze로 전송되는 페이로드는 커스터마이즈 가능하며 고객의 요구에 맞게 구성할 수 있습니다. 여기에는 사용되는 식별자, 커스텀 속성의 이름, 그리고 Adikteev가 Braze에서 새 사용자를 생성할 수 있는지 또는 기존 사용자만 업데이트할 수 있는지 여부를 구성하는 것이 포함됩니다.

## 고객지원 및 문제 해결 {#support-and-troubleshooting}

통합과 관련된 질문이나 활용 사례에 대한 지원이 필요하면 Adikteev 계정 매니저에게 문의하세요.