---
nav_title: Iterate
article_title: Iterate
alias: /partners/iterate/
description: "이 참조 문서에서는 Braze와 Iterate 간의 파트너십을 설명하며, 설문조사를 사용하여 추가 인사이트를 확보함으로써 고객 데이터를 강화할 수 있습니다."
page_type: partner
search_tag: Partner

---

# Iterate

> [Iterate](https://iteratehq.com)는 설문조사 및 피드백 도구를 제공하여 브랜드에 맞는 사용자 친화적인 리서치 경험을 제공함으로써 고객으로부터 학습할 수 있도록 도와줍니다.

_이 통합은 Iterate에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Iterate와 Braze의 통합을 통해 제품이나 캠페인 내에서 Iterate 설문조사를 네이티브하고 원활하게 전달할 수 있습니다. 설문조사 응답은 Braze에서 커스텀 사용자 속성으로 기록되어, 사용자에 대한 완전한 그림을 구축하거나 강력한 새 오디언스 및 세그먼트를 생성할 수 있습니다.

앱이나 웹사이트에 Braze SDK가 설치되어 있으면, Braze에서 제공하는 세분화 및 타겟팅 도구를 사용하여 트리거 또는 커스텀 세그먼트를 기반으로 오디언스의 특정 부분에 인앱 메시지를 통해 설문조사를 전달할 수 있습니다. Iterate 설문조사는 이메일 캠페인에 직접 삽입하거나 푸시 또는 기타 캠페인 유형에 링크로 포함할 수도 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 출처 |
|---|---|
| Iterate 계정 | 이 파트너십을 활용하려면 [Iterate 계정](https://iteratehq.com)이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. Braze 인앱 메시지를 통해 설문조사를 보내려면 `kpi.mau.data_series` 권한도 필요합니다.<br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL]({{site.baseurl}}/api/basics/#endpoints)에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 활용 사례 {#use-cases}

Iterate를 사용하면 거의 모든 유형의 데이터를 수집할 수 있습니다. 개인 정보(이름, 나이, 이메일), 성과 데이터(순고객추천지수, 고객 만족, 별점), 선호도(선호 기기, 선호 커뮤니케이션 빈도), 성격(좋아하는 책, 강아지파 또는 고양이파) 등 다양한 데이터를 수집할 수 있습니다. 무엇을 물어볼지는 전적으로 여러분에게 달려 있으며, 어떤 종류의 데이터를 수집하거나 어떤 오디언스를 구축할지도 마찬가지입니다.

## 통합 {#integration}

### 시작하기: Braze와 Iterate 연결 {#getting-started-connect-braze-with-iterate}

Iterate 계정에 로그인하고 **회사 설정** 페이지에서 Braze REST 엔드포인트와 REST API 키를 추가합니다.

### 인앱 메시지로 설문조사 전달 {#deliver-surveys-as-an-in-app-message}

#### 1단계: 설문조사 생성 {#step-1-create-your-survey}

설문조사를 생성하기 전에 Iterate 설정에서 **Enable in-app message surveys** 토글을 켭니다.

다음으로 Iterate에서 새 설문조사를 생성하고 관련 설문조사 질문을 추가합니다. 적절한 경우 설문조사 전에 표시할 프롬프트 메시지를 포함할 수도 있습니다. 설문조사 유형으로 **Send via Braze In-App Message**를 선택합니다.

설문조사가 완료되면 **Publish** 탭에서 **Copy and paste your embed code** 아래의 코드 스니펫을 복사합니다.

#### 2단계: 설문조사 공유 {#step-2-share-your-survey}

Braze에서 새 인앱 메시징 캠페인을 생성하고, 메시징 유형으로 **Custom Code**를 선택한 다음 코드 스니펫을 메시지에 붙여넣습니다. 그런 다음 클릭 시 메시지 동작으로 **Wait for User to Dismiss**를 선택합니다.

다른 인앱 메시징 캠페인과 마찬가지로 전달 방법을 선택하고 오디언스를 타겟팅하여 캠페인 설정을 계속합니다.

### 이메일 또는 푸시를 통한 설문조사 전달 {#deliver-surveys-through-email-or-push}

#### 1단계: 설문조사 생성

Iterate에서 새 이메일 또는 링크 설문조사를 생성하고 관련 설문조사 질문을 추가합니다. 질문을 작성하고 디자인을 커스터마이즈한 후 **Send survey > Integrations > Braze**를 선택합니다.

그러면 Braze로 응답을 보내기 위한 구성 옵션이 표시됩니다. 통합을 토글하여 해당 설문조사의 응답을 Braze로 전송하도록 활성화합니다.

#### 2단계: 설문조사 공유

설문조사는 두 가지 방법으로 공유할 수 있습니다. 첫 번째 질문을 메시지에 삽입하거나 Iterate 플랫폼에서 설문조사에 대한 직접 링크를 포함시키는 것입니다.

![Iterate 링크 옵션]({% image_buster /assets/img/iterate.png %})

- **코드 삽입**
  - **Send survey** 탭의 Braze 통합 섹션에서 **Email embed code** 아래의 코드 스니펫을 복사합니다. 설문조사의 시작 부분이 표시되기를 원하는 Braze 이메일의 HTML에 코드를 삽입합니다.
  - 설문조사 질문이 렌더링되지 않거나 형식이 올바르지 않게 보이는 경우, 메시지 작성기의 **Sending Info** 탭으로 이동하여 **Inline CSS**를 선택 해제해야 합니다.
- **링크 포함**
  - **Send survey** 탭의 Braze 통합 섹션에서 **Survey Link** 아래의 링크를 복사합니다. 링크에 포함된 Liquid {% raw %}`?user_braze_id={{${braze_id}}}`{% endraw %}는 발송 시 각 사용자에 대해 자동으로 대체됩니다.

### 다음 단계: 후속 캠페인 구축 {#next-steps-build-follow-up-campaigns}

사용자가 응답하면 실시간 데이터가 프로필에 채워지는 것을 확인할 수 있습니다. 이 데이터를 사용하여 사용자를 세분화하고 개인화된 후속 캠페인을 보낼 수 있습니다. 예를 들어, "저희 제품을 즐기고 계신가요?"라는 질문을 보낸 경우, 커스텀 사용자 속성 `Do you enjoy our products?`에 "Yes" 또는 "No"로 응답한 사용자의 세그먼트를 생성하고 이 사용자들을 타겟팅할 수 있습니다.

## Braze 커스텀 이벤트 {#braze-custom-events}

사용자가 설문조사 질문에 답변하면 Iterate는 Braze 내에서 `survey-question-response`라는 커스텀 이벤트를 트리거합니다. 커스텀 이벤트를 사용하면 원하는 수와 유형의 후속 캠페인을 트리거할 수 있습니다.

## 사용자 속성 이름 커스터마이즈 {#customize-user-attribute-names}

기본적으로 질문에 대해 생성되는 사용자 속성은 프롬프트와 동일합니다.
경우에 따라 이를 커스터마이즈하고 싶을 수 있습니다. 이를 위해 **Create your Survey** 단계에서 **Customize user attribute names** 드롭다운을 클릭하고 원하는 커스텀 이름을 입력합니다.