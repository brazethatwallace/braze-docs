---
nav_title: Lemnisk
article_title: Lemnisk와 Braze 통합
description: "이 참조 문서에서는 AI 기반 고객 데이터 플랫폼 주도 마케팅 자동화 플랫폼인 Braze와 Lemnisk의 파트너십에 대해 자세히 설명하며, 다양한 소스에서 Lemnisk에 수집한 사용자 데이터를 Braze로 스트리밍하여 Braze의 도구를 사용해 다양한 채널과 대상에서 활성화할 수 있도록 지원합니다."
alias: /partners/lemnisk/
page_type: partner
search_tag: Partner

---

# Lemnisk

> [Lemnisk](https://www.lemnisk.co/)는 인공지능 기반의 고객 데이터 플랫폼(CDP) 및 마케팅 자동화 솔루션으로, 사일로화된 다양한 소스로부터 고객 데이터를 실시간으로 캡처, 통합, 활성화할 수 있도록 지원합니다. 이 통합 데이터는 다양한 MarTech 및 비즈니스 플랫폼에 원활하게 전달되며, 고객 데이터 생애주기의 모든 단계를 추적할 수 있는 강력한 실시간 분석 기능을 제공합니다.

_이 통합은 Lemnisk에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Lemnisk와 Braze의 통합을 통해 브랜드와 기업은 여러 플랫폼에서 사용자 데이터를 실시간으로 통합하고, 수집된 사용자 정보와 행동 데이터를 실시간으로 Braze로 전송하는 CDP 주도 인텔리전스 레이어 역할을 함으로써 Braze의 잠재력을 최대한 활용할 수 있습니다. Lemnisk는 행동 신호와 개인 속성을 결합하여 보다 심층적인 컨텍스트로 메시징을 개인화할 수 있는 풍부한 고객 프로필을 Braze에 직접 제공합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| Lemnisk 계정 | 이 파트너십을 이용하려면 [Lemnisk](https://www.lemnisk.co/) 계정이 필요합니다. |
| Lemnisk의 외부 API | Lemnisk 고객 성공 매니저에게 문의하여 계정에 **외부 API**를 활성화하세요. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [계정의 Braze URL]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## Lemnisk 통합하기 {#integrating-lemnisk}

### 1단계: Braze 외부 API 만들기 {#create-a-braze-external-api}

Lemnisk에서 외부 API 채널로 이동합니다. **Add New External API**를 선택합니다. 이제 [사용자 추적]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 엔드포인트를 외부 API로 설정하겠습니다.

![Lemnisk에서 외부 API 생성 프로세스 시작하기]({% image_buster /assets/img/lemnisk/open_external_api.png %})

**Basic Details**에서 이름, 설명, 채널, 채널 식별자를 입력합니다.

![Lemnisk에서 새 외부 API에 대한 기본 구성 세부 정보 입력하기]({% image_buster /assets/img/lemnisk/ext_api_basic_details.png %})

**External API details**에서 `users.track` 엔드포인트에 대한 관련 세부 정보를 입력합니다. {% raw %}`{{}}`{% endraw %}을 사용하여 여러 인게이지먼트 수준 필드를 정의할 수 있으며, 이를 통해 캠페인마다 다른 값을 설정할 수 있습니다.

![외부 API 엔드포인트 및 페이로드 세부 정보 작성하기]({% image_buster /assets/img/lemnisk/ext_api_ext_api_details.png %})

사용자 추적 구성 설정을 완료하려면 **Save**를 선택합니다. 자동으로 **Test API** 페이지로 리디렉션됩니다.

### 2단계: 구성 테스트 {#step-2-test-the-configuration}

**Test API** 페이지의 JSON 트리 보기에서 API 매개변수에 대한 테스트 값을 입력한 다음 **Test Configuration**을 선택합니다.

자격 증명과 API 정의가 정확하면 Braze가 성공 응답을 반환합니다.

![샘플 페이로드 및 성공 응답으로 외부 API 구성 테스트하기]({% image_buster /assets/img/lemnisk/test_ext_api.png %})

다음으로, 이벤트가 Braze에 성공적으로 전송되었는지 확인합니다. Braze 대시보드에서 **오디언스** > **사용자 검색**으로 이동한 다음 외부 API 구성의 식별자 중 하나(예: 사용자 이메일 주소)를 입력합니다. 모든 것이 올바르게 작동하면 테스트 API 트리거를 수신한 프로필이 나열됩니다.

![Braze에서 사용자 프로필 및 활동 개요 보기]({% image_buster /assets/img/lemnisk/braze_cov.png %})

### 3단계: Braze에서 사용자 이벤트 트리거하기 {#step-3-trigger-user-events-in-braze}

1. Lemnisk에서 새 Segment를 만듭니다. 예를 들어, 사용자가 리드 양식을 제출하는 즉시 정보를 Braze에 전송하는 Segment를 만들 수 있습니다.
2. 새 Segment에서 **External API** > **Add Engagement**로 이동합니다.
3. **Engagement Creation**에서 기본 세부 정보를 입력하고 [이전에 만든](#create-a-braze-external-api) 구성을 선택합니다.
4. **Configure Parameters**에서 인게이지먼트 수준에서 노출하도록 선택한 Braze 매개변수에 대한 입력을 확인할 수 있습니다. 다음 예에서는 _Name of the User_, _Product ID_, _Event Time_이 표시됩니다.
    ![사용자 데이터를 Braze로 전송하기 위한 인게이지먼트 만들기]({% image_buster /assets/img/lemnisk/create_an_engagement.png %})
5. 선택한 매개변수에 대한 관련 개인화 변수를 입력한 다음 **Save**를 선택합니다.
6. 완료했으면 인게이지먼트를 활성화합니다.