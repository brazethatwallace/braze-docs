---
nav_title: 오케스트레이션 설정
article_title: 오케스트레이션 설정
page_order: 2
description: "BrazeAI Decisioning Studio Go를 고객 참여 플랫폼에 연결하여 개인화된 커뮤니케이션을 활성화하는 방법을 알아보세요."
toc_headers: h2
---

# 오케스트레이션 설정 {#set-up-orchestration}

> BrazeAI Decisioning Studio™ Go는 개인화된 커뮤니케이션을 오케스트레이션하기 위해 고객 참여 플랫폼(CEP)에 연결해야 합니다. 이 문서에서는 지원되는 각 CEP에 대한 통합 설정 방법을 설명합니다.

## 지원되는 CEP {#supported-ceps}

Decisioning Studio Go는 다음 고객 참여 플랫폼을 지원합니다:

| CEP | 통합 유형 | 주요 기능 |
|-----|-----------------|--------------|
| **Braze** | API 트리거 캠페인 | 네이티브 통합, 실시간 트리거링 |
| **Salesforce Marketing Cloud** | API 이벤트를 지원하는 Journey Builder | SQL 쿼리 자동화, 데이터 확장 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="지원되는 CEP" }

아래에서 CEP를 선택하여 통합 설정을 시작하세요.

{% tabs %}
{% tab Braze %}

## Braze 통합 설정 {#set-up-braze-integration}

Decisioning Studio Go를 Braze와 통합하려면 API 키를 생성하고, API 트리거 캠페인을 구성한 후, 필요한 식별자를 Decisioning Studio Go 포털에 제공해야 합니다.

### 1단계: REST API 키 생성 {#step-1-create-a-rest-api-key}

1. Braze 대시보드에서 **설정** > **API 및 식별자** > **API 키**로 이동하세요.
2. **API 키 생성**을 선택합니다.
3. API 키의 이름을 입력하세요. 예를 들어 "DecisioningStudioGoEmail"과 같이 입력할 수 있습니다.
4. 다음 카테고리에 따라 권한을 선택하세요:
    - **사용자 데이터:** `users.track`, `users.delete`, `users.export.ids`, `users.export.segment` 선택
    - **메시지:** `messages.send` 선택
    - **Campaigns:** 나열된 모든 권한 선택
    - **Canvas:** 나열된 모든 권한 선택
    - **Segments:** 나열된 모든 권한 선택
    - **템플릿:** 나열된 모든 권한 선택

{: start="5"}
5. **API 키 생성**을 선택합니다.
6. API 키를 복사하여 BrazeAI Decisioning Studio™ Go 포털에 붙여넣으세요.

### 2단계: 이메일 표시 이름 찾기 {#step-2-locate-your-email-display-name}

1. Braze 대시보드에서 **설정** > **이메일 환경설정**으로 이동하세요.
2. BrazeAI Decisioning Studio™ Go와 함께 사용할 표시 이름을 찾으세요.
3. **From Display Name**을 복사하여 BrazeAI Decisioning Studio™ Go 포털의 **Email Display Name**에 붙여넣으세요.
4. 관련 이메일 주소를 BrazeAI Decisioning Studio™ Go 포털의 **From email address**에 복사하여 붙여넣으세요. 이 주소는 로컬 부분과 도메인을 결합한 것입니다.

### 3단계: Braze URL과 앱 ID 찾기 {#step-3-find-your-braze-url-and-app-id}

**Braze URL을 찾으려면:**
1. Braze 대시보드로 이동하세요.
2. 브라우저 창에서 Braze URL은 `https://`로 시작하고 `braze.com`으로 끝납니다. Braze URL의 예시는 `https://dashboard-01.braze.com`입니다.

**앱 ID(API 키)를 찾으려면:**

{% alert note %}
Braze는 추적 목적으로 사용할 수 있는 앱 ID(Braze 대시보드에서는 API 키로 지칭됨)를 제공합니다. 예를 들어, 워크스페이스 내 특정 앱과 활동을 연결하는 데 활용할 수 있습니다. 앱 ID를 사용하는 경우, BrazeAI Decisioning Studio™ Go는 각 실험 담당자와 앱 ID를 연결하는 기능을 지원합니다.<br><br>앱 ID를 사용하지 않는 경우, 임의의 문자열을 플레이스홀더로 입력할 수 있습니다.
{% endalert %}

1. Braze 대시보드에서 **설정** > **앱 설정**으로 이동하세요.
2. 추적하려는 앱으로 이동하세요.
3. **API 키**를 복사하여 BrazeAI Decisioning Studio™ Go 포털에 붙여넣으세요.

### 4단계: API 트리거 캠페인 생성 {#step-4-create-an-api-triggered-campaign}

1. Braze 대시보드에서 **메시징** > **Campaigns**로 이동하세요.
2. **캠페인 생성**을 선택하세요.
3. 캠페인 유형으로 **API campaign**을 선택하세요.
4. 캠페인 이름을 입력하세요. 예를 들어 "Decisioning Studio Go Email"과 같이 입력할 수 있습니다.

!["Decisioning Studio Go Email"이라는 이름의 API 캠페인.]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5. 메시징 채널로 **이메일**을 선택하세요.

![API 캠페인용 메시징 채널 선택 옵션.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6. **추가 옵션**에서 **사용자가 캠페인 수신 자격을 다시 획득할 수 있도록 허용** 확인란을 선택하세요.
7. 재자격 획득 시간으로 **1**을 입력하고 드롭다운에서 **시간**을 선택하세요.

![선택된 API 캠페인의 재자격 설정.]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8. **캠페인 저장**을 선택하세요.

### 5단계: 캠페인 및 메시지 ID 복사 {#step-5-copy-your-campaign-and-message-ids}

1. API 캠페인에서 **Campaign ID**를 복사하세요. 그런 다음 BrazeAI Decisioning Studio™ Go 포털로 이동하여 **Campaign ID**를 붙여넣으세요.

![복사하여 붙여넣을 예시 메시지 변형 ID.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2. **Message Variation ID**를 복사하세요. 그런 다음 BrazeAI Decisioning Studio™ Go 포털로 이동하여 **Message Variation ID**를 붙여넣으세요.

### 6단계: 테스트 사용자 ID 찾기 {#step-6-locate-a-test-user-id}

통합을 테스트하려면 사용자 ID가 필요합니다:

워크스페이스에서 [식별자 필드 수준 암호화]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption/)를 사용하는 경우, `/users/track` 엔드포인트로 생성하는 새 테스트 사용자는 암호화된 워크스페이스의 이메일 요구 사항을 따라야 합니다. `email` 필드는 소문자로 변환된 이메일 값의 Base64 인코딩 HMAC-SHA256 해시로 전송하고, `email_encrypted`는 구성된 PII 암호화 키로 생성된 암호화된 이메일 값으로 전송하세요.

1. Braze 대시보드에서 **오디언스** > **사용자 검색**으로 이동하세요.
2. 외부 사용자 ID, 사용자 별칭, 이메일, 전화번호 또는 푸시 토큰으로 사용자를 검색하세요.
3. 설정 시 참조할 수 있도록 사용자 ID를 복사하세요.

![ID로 사용자를 찾은 예시 고객 프로필.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## SFMC 통합 설정 {#set-up-sfmc-integration}

Decisioning Studio Go를 Salesforce Marketing Cloud와 통합하려면 앱 패키지를 설정하고, 데이터 쿼리 자동화를 생성하며, 트리거된 발송을 처리하기 위한 여정을 구축해야 합니다.

### 1부: SFMC 앱 패키지 설정 {#part-1-set-up-an-sfmc-app-package}

1. Marketing Cloud 홈페이지로 이동하세요.
2. 글로벌 헤더에서 메뉴를 열고 **Setup**을 선택하세요.
3. 사이드 패널 탐색에서 **Platform Tools** 아래의 **Apps**로 이동한 후 **Installed Packages**를 선택하세요.
4. **New**를 선택하여 앱 패키지를 생성합니다.
5. 앱 패키지에 이름과 설명을 지정하세요.

!["Experimenter 1 - Test 5"라는 이름의 앱 패키지.]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6. **Add Component**를 선택하세요.
7. **Component Type**에서 **API Integration**을 선택하세요. 그런 다음 **Next**를 선택하세요.
8. **Integration Type**에서 **Server-to-server**를 선택하세요. 그런 다음 **Next**를 선택하세요.
9. 앱 패키지에 대해 다음 권장 범위만 선택하세요:
    - Channels > Email > Read, Write, Send
    - Channels > OTT > Read
    - Channels > Push > Read
    - Channels > SMS > Read
    - Channels > Social > Read
    - Channels > Web > Read
    - Assets > Documents and Images > Read, Write
    - Assets > Saved Content > Read, Write
    - Automation > Automations > Read, Write, Execute
    - Automation > Journeys > Read, Write, Execute, Activate/Stop/Pause/Send/Schedule
    - Contacts > Audiences > Read
    - Contacts > List and Subscribers > Read, Write
    - Cross Cloud Platform > Market Audience > View
    - Cross Cloud Platform > Market Audience Member > View
    - Cross Cloud Platform > Marketing Cloud Connect > Read
    - Data > Data Extensions > Read, Write
    - Data > File Locations > Read
    - Data > Tracking Events > Read, Write
    - Event notifications > Callbacks > Read
    - Event notifications > Subscriptions > Read

{% details 권장 범위 이미지 보기 %}

![Salesforce Marketing Cloud 앱 패키지에 권장되는 범위.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10. **Save**를 선택하세요.
11. 다음 필드를 BrazeAI Decisioning Studio™ Go 포털에 복사하여 붙여넣으세요: **Client Id**, **Client Secret**, **Authentication Base URI**, **REST Base URI**, **SOAP Base URI**.

### 2부: 데이터 쿼리 자동화 설정 {#part-2-set-up-a-data-query-automation}

#### 1단계: 새 자동화 생성 {#step-1-create-a-new-automation}

1. Salesforce Marketing Cloud 홈에서 **Journey Builder**로 이동한 후 **Automation Studio**를 선택하세요.

![Journey Builder 탐색 메뉴의 Automation Studio 옵션.]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2. **New Automation**을 선택하세요.
3. **Starting Source**로 **Schedule** 노드를 드래그 앤 드롭하세요.

!["Schedule"을 여정의 시작 소스로 설정합니다.]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4. **Schedule** 노드에서 **Configure**를 선택하세요.
5. 스케줄에 대해 다음을 설정하세요:
    - **Start Date:** 내일 날짜
    - **Time:** **12:00 AM**
    - **Time Zone:** **(GMT-05:00) Eastern (US & Canada)**
6. **Repeat**에서 **Daily**를 선택하세요.
7. 이 스케줄을 종료 없이 계속 실행되도록 설정하세요.
8. **Done**을 선택하여 스케줄을 저장하세요.

![2024년 1월 25일 오전 12시(미국 동부 시간)에 정의된 예시 스케줄로, 매일 반복됩니다.]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### 2단계: SQL 쿼리 생성 {#step-2-create-your-sql-queries}

다음으로, 가입자 쿼리와 참여 쿼리라는 2개의 SQL 쿼리를 생성하세요. 이 쿼리를 통해 BrazeAI Decisioning Studio™ Go는 오디언스를 구성하고 참여 이벤트를 수집하기 위한 데이터를 가져올 수 있습니다.

**가입자 쿼리:**

1. **SQL Query**를 캔버스로 드래그 앤 드롭하세요.
2. **Choose**를 선택하세요.
3. **Create New Query Activity**를 선택하세요.
4. 쿼리에 이름과 외부 키를 지정하세요. BrazeAI Decisioning Studio™ Go 포털에서 제공된 가입자 쿼리의 권장 이름과 외부 키를 사용하는 것을 권장합니다.

![예시 "OFE_Subscribers_query_Test5"와 외부 키.]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5. **Next**를 선택하세요.
6. BrazeAI Decisioning Studio™ Go 포털에서 **Subscriber Query Resources** 아래에 있는 시스템 데이터 SQL 쿼리를 찾으세요.
7. 쿼리를 텍스트 상자에 복사하여 붙여넣고 **Next**를 선택하세요.

![SQL Query 섹션의 예시 쿼리.]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8. BrazeAI Decisioning Studio™ Go 포털의 **Resources to use** 섹션에서 대상 데이터 확장의 외부 키를 찾으세요. 그런 다음 검색창에 붙여넣어 검색하세요.

![검색창에 붙여넣은 외부 키.]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9. 검색한 외부 키와 일치하는 데이터 확장을 선택하세요. 대상 데이터 확장 이름은 교차 참조를 위해 BrazeAI Decisioning Studio™ Go 포털에도 제공됩니다. 가입자 쿼리의 **Data Extension**은 `BASE_AUDIENCE_DATA` 접미사로 끝나야 합니다.

![예시 외부 키와 일치하는 데이터 확장 이름.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10. **Overwrite**를 선택한 다음 **Next**를 선택하세요.

**참여 쿼리:**

1. **SQL Query**를 캔버스로 드래그 앤 드롭하세요.

!["SQL Query"가 여정에 활동으로 추가되었습니다.]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2. **Choose**를 선택하세요.
3. **Create New Query Activity**를 선택하세요.
4. 쿼리에 이름과 외부 키를 지정하세요. BrazeAI Decisioning Studio™ Go 포털에서 제공된 참여 쿼리의 권장 이름과 외부 키를 사용하는 것을 권장합니다.

![예시 "OFE_Engagement_query"와 외부 키.]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5. **Next**를 선택하세요.
6. BrazeAI Decisioning Studio™ Go 포털에서 **Engagement Query Resources** 아래에 있는 시스템 데이터 SQL 쿼리를 찾으세요.
7. 쿼리를 텍스트 상자에 복사하여 붙여넣고 **Next**를 선택하세요.

![SQL Query 섹션의 예시 쿼리.]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8. BrazeAI Decisioning Studio™ Go 포털에서 지정된 참여 쿼리의 대상 데이터 확장을 찾아 선택하세요.

{% alert tip %}
대상 데이터 확장 이름은 교차 참조를 위해 BrazeAI Decisioning Studio™ Go 포털에도 제공됩니다. 참여 쿼리의 대상 Data Extension을 확인하고 있는지 반드시 확인하세요. 참여 쿼리의 **Data Extension**은 ENGAGEMENT_DATA 접미사로 끝나야 합니다.
{% endalert %}

{: start="9"}
9. **Overwrite**를 선택한 다음 **Next**를 선택하세요.

![예시 외부 키와 일치하는 데이터 확장 이름.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### 3단계: 자동화 실행 {#step-3-run-the-automation}

1. 자동화에 이름을 지정한 후 **Save**를 선택하세요.

![예시 자동화 "OFE_Experimenter_Test5_Automation".]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

{: start="2"}
2. 다음으로, **Run Once**를 선택하여 모든 것이 예상대로 작동하는지 확인하세요.
3. 두 쿼리를 모두 선택하고 **Run**을 선택하세요.

![선택된 SQL 쿼리 활동 목록을 실행하는 "OFE_Experimenter_Test5_Automation" 자동화.]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4. **Run Now**를 선택하세요.

![선택된 SQL Query 활동.]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

이제 자동화가 성공적으로 실행되고 있는지 확인할 수 있습니다. 자동화가 예상대로 실행되지 않는 경우 Braze 고객지원팀에 문의하여 추가 지원을 받으세요.

### 3부: SFMC 여정 생성 {#part-3-create-your-sfmc-journey}

#### 1단계: 여정 설정 {#step-1-set-up-the-journey}

1. Salesforce Marketing Cloud에서 **Journey Builder** > **Journey Builder**로 이동하세요.
2. **Create New Journey**를 선택하세요.
3. 여정 유형으로 **Multi-Step Journey**를 선택한 후 **Create**를 선택하세요.

![결정 분할 노드와 여러 이메일 노드에 연결된 API 이벤트 진입 소스.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### 2단계: 여정 구축 {#step-2-build-the-journey}

**진입 소스 생성:**

1. 진입 소스로 **API Event**를 Journey Builder로 드래그하세요.

![진입 소스로 "API Event"가 선택되었습니다.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2. **API Event**에서 **Create an event**를 선택하세요.

![API Event의 "이벤트 생성" 옵션.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3. **Select Data Extension**을 선택하세요. BrazeAI Decisioning Studio™ Go가 추천을 기록할 데이터 확장을 찾아 선택하세요.
4. 변경 사항을 저장하려면 **Summary**를 선택하세요.
5. **Done**을 선택하여 API 이벤트를 저장하세요.

![API 이벤트 요약.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**결정 분할 추가:**

1. **API Entry Event** 뒤에 **Decision Split**을 드래그 앤 드롭하세요.
2. **Decision Split** 세부 정보에서 첫 번째 경로에 대해 **Edit**를 선택하세요.

!["Edit" 버튼이 있는 결정 분할 세부 정보.]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3. 추천 데이터 확장에서 전달된 템플릿 ID를 사용하도록 **Decision Split**을 업데이트하세요. **Journey Data** 아래에서 적절한 필드를 찾으세요.

![결정 분할의 경로 1에 있는 Journey Data 섹션.]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4. 진입 이벤트를 선택하고 원하는 템플릿 ID 필드를 찾은 후 워크스페이스로 드래그하세요.

![포함할 이메일 템플릿 ID.]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5. 첫 번째 이메일 템플릿의 템플릿 ID를 입력한 후 **Done**을 선택하세요.
6. **Summary**를 선택하여 이 경로를 저장하세요.
7. 각 이메일 템플릿에 대한 경로를 추가한 후, 위의 4~6단계를 반복하여 템플릿 ID가 각 템플릿의 ID 값과 일치하도록 필터 기준을 설정하세요.
8. **Done**을 선택하여 **Decision Split** 노드를 저장하세요.

![각 이메일 템플릿 ID에 대한 결정 분할의 두 가지 경로.]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**각 결정 분할에 이메일 추가:**

1. **Email** 노드를 **Decision Split**의 각 경로로 드래그하세요.
2. **Email**을 선택한 후, 각 경로에 적용될 적절한 템플릿을 선택하세요(즉, ID 값이 있는 템플릿이 Decision Split의 로직과 일치해야 합니다).

![여정에 이메일 노드가 추가되었습니다.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### 3단계: 여정 활성화 {#step-3-activate-the-journey}

여정을 설정한 후 활성화하고 다음 세부 정보를 BrazeAI Decisioning Studio™ Go 팀과 공유하세요:

* Journey ID
* Journey name
* API event definition key
* Recommendations data extension external key

{% alert note %}
BrazeAI Decisioning Studio™ Go 포털은 가입자 및 참여 데이터를 하루에 한 번 내보내기 위해 프로비저닝한 SFMC 자동화를 보여줍니다. 이 자동화를 SFMC에서 열 경우, 일시 중지를 해제하고 다시 활성 상태로 전환해야 합니다.
{% endalert %}

1. BrazeAI Decisioning Studio™ Go 포털에서 **Journey name**을 복사하세요.
2. 다음으로 Salesforce Marketing Cloud Journey Builder에서 검색창에 여정 이름을 붙여넣으세요.
3. 여정 이름을 선택하세요. 여정은 현재 초안 상태입니다.
4. **Validate**를 선택하세요.

![활성화할 완료된 여정.]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5. 검증 결과를 검토하고 **Activate**를 선택하세요.

![검증 규칙 섹션에 나열된 추천 항목.]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6. **Activate Journey** 요약에서 다시 **Activate**를 선택하세요.

![여정 요약.]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

모든 설정이 완료되었습니다! 이제 BrazeAI Decisioning Studio™ Go를 통해 발송을 트리거할 수 있습니다.

{% endtab %}
{% endtabs %}

## 다음 단계 {#next-steps}

오케스트레이션 설정을 완료했으니, 이제 에이전트 설계를 진행하세요:

- [에이전트 설계]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)