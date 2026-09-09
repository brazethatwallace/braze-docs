---
nav_title: Event Forwarding Extension
article_title: Adobe
description: "이 참조 문서에서는 Adobe Experience Platform Edge Network에서 캡처한 데이터를 활용하여 서버 측 이벤트 형태로 Braze에 전송할 수 있는 Braze 이벤트 전달 확장 기능을 다룹니다."
page_type: partner
page_order: 2
search_tag: Partner
---

# Track Events API 이벤트 전달 확장 기능 {#track-events-api-event-forwarding-extension}

> Braze Track Events API [이벤트 전달](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en) 확장 기능을 사용하면 Adobe Experience Platform Edge Network에서 캡처한 데이터를 활용하여 [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) API를 통해 서버 측 이벤트 형태로 Braze에 전송할 수 있습니다.

이 문서에서는 확장 기능의 사용 사례, 이벤트 전달 라이브러리에 설치하는 방법, 이벤트 전달 [규칙](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en)에서 기능을 활용하는 방법을 다룹니다.

{% alert note %}
Adobe 이벤트 전달을 사용하면 Braze 데이터 포인트 사용량이 증가할 수 있습니다. 자세한 내용은 [데이터 포인트]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#billable-data-points)에 대한 Braze 설명서를 참조하세요.
{% endalert %}

## 사용 사례 {#use-cases}

이 확장 프로그램은 Braze의 고객 분석 및 타겟팅 기능을 활용하기 위해 Edge Network의 데이터를 Braze에서 사용해야 합니다.

예를 들어, 다채널 환경(웹사이트 및 모바일)을 갖추고 웹사이트와 모바일 플랫폼에서 트랜잭션 또는 대화형 입력을 이벤트 데이터로 수집하는 소매 조직을 생각해 보세요.

다양한 [태그](https://experienceleague.adobe.com/docs/experience-platform/tags/home.html?lang=en) 규칙을 사용하여 이 데이터는 실시간으로 Edge Network로 전송됩니다. 이후 Braze 이벤트 포워딩 확장 프로그램이 서버 측에서 관련 이벤트를 자동으로 Braze에 전송합니다.

## 사용량 제한 {#rate-limits}

| API | 사용량 제한 |
| --- | --- |
| User Track | 분당 50,000건의 요청.<br><br>자세한 내용은 [User Track API 설명서]({{site.baseurl}}/api/endpoints/user_data/post_user_track#rate-limit)를 참조하세요.
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용량 제한" }

## 통합 {#integration}

### 1단계: 필수 구성 세부 정보 수집 {#step-1-gather-required-configuration-details}

Edge Network를 Braze에 연결하려면 다음 항목이 필요합니다:

| 키 유형 | 설명 |
| --- | --- |
| Braze 인스턴스 | Braze 인스턴스는 Braze 온보딩 매니저에게 문의하거나 [API 개요 페이지]({{site.baseurl}}/api/basics#endpoints)에서 확인할 수 있습니다. |
| Braze REST API 키 | 모든 권한이 부여된 Braze REST API 키입니다. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="1단계: 필수 구성 세부 정보 수집" }

### 2단계: 시크릿 생성 {#step-2-create-a-secret}

새로운 [이벤트 포워딩 시크릿](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/secrets.html?lang=en)을 생성하고 값을 [Braze API 키](https://experienceleague.adobe.com/docs/experience-platform/tags/extensions/server/braze/overview.html?lang=en#configuration-details)로 설정합니다. 이렇게 하면 값을 안전하게 유지하면서 계정 연결을 인증하는 데 사용됩니다.

### 3단계: Braze 확장 프로그램 설치 및 구성 {#step-3-install-and-configure-the-braze-extension}

1. 확장 프로그램을 설치하려면 [이벤트 포워딩 속성을 생성](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en#properties)하거나 기존 속성을 선택하여 편집합니다.
2. 그런 다음 왼쪽 내비게이션에서 **Extensions**를 선택합니다. **Catalog** 탭에서 Braze 확장 프로그램 카드의 **Install**을 선택합니다.
3. 다음 화면에서 REST 인스턴스와 API 키를 입력하고 완료되면 **Save**를 선택합니다.

### 4단계: 이벤트 전송 규칙 생성 {#step-4-create-a-send-event-rule}

확장 프로그램을 설치한 후 새로운 이벤트 포워딩 [규칙](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en)을 생성하고 원하는 대로 조건을 구성합니다. 규칙에 대한 액션을 구성할 때 **Braze** 확장 프로그램을 선택한 다음 액션 유형으로 **Send Event**를 선택합니다.

![Braze Send Event를 사용하도록 구성된 Adobe 이벤트 포워딩 규칙 액션.]({% image_buster /assets/img/efe.png %})

{% tabs local %}
{% tab 사용자 식별 %}

| 입력 | 설명 |
| --- | --- |
| 외부 사용자 ID | 길고 무작위적이며 균등하게 분포된 UUID 또는 GUID입니다. 사용자 ID를 다른 방법으로 지정하려는 경우에도 마찬가지로 길고 무작위적이며 균등하게 분포되어야 합니다. [권장되는 사용자 ID 명명 규칙]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web#naming-best-practices)에 대해 자세히 알아보세요. |
| Braze 사용자 ID | Braze 사용자 식별자입니다. |
| 사용자 별칭 | 별칭은 대체 고유 사용자 식별자 역할을 합니다. 별칭을 사용하여 코어 사용자 ID와 다른 차원에서 사용자를 식별할 수 있습니다.<br><br>사용자 별칭 객체는 두 부분으로 구성됩니다: 식별자 자체에 해당하는 `alias_name`과 별칭 유형을 나타내는 `alias_label`입니다. 사용자는 다른 레이블로 여러 별칭을 가질 수 있지만 `alias_label`당 하나의 `alias_name`만 가질 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="4단계: 이벤트 전송 규칙 생성" }

{% alert note %}
이벤트를 사용자에게 연결하려면 `External User ID` 필드, `Braze User Identifier` 필드 또는 `User Alias` 섹션 중 하나를 입력해야 합니다.
{% endalert %}

{% endtab %}
{% tab 이벤트 데이터 %}

| 입력 | 설명 | 필수 |
| --- | --- | --- |
| 이벤트 이름 | 이벤트의 이름입니다. | 예 |
| 이벤트 시간 | ISO 8601 형식 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식의 날짜-시간 문자열입니다. | 예 |
| 앱 식별자 | 앱 식별자 또는 `app_id`는 워크스페이스 내 특정 앱에 활동을 연결하는 파라미터입니다. 워크스페이스 내에서 상호 작용할 앱을 지정합니다. | 아니요 |
| 이벤트 속성정보 | 이벤트의 커스텀 속성정보를 포함하는 JSON 객체입니다. | 아니요 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="4단계: 이벤트 전송 규칙 생성" }

{% alert note %}
**Braze Send Event** 액션에는 **Event Name**과 **Event Time**만 필수로 지정하면 되지만 커스텀 속성정보 필드에 가능한 한 많은 정보를 포함하는 것이 좋습니다. 자세한 내용은 [이벤트 객체]({{site.baseurl}}/api/objects_filters/event_object)를 참조하세요.
{% endalert %}

{% endtab %}
{% tab 사용자 속성 %}

사용자 속성은 지정된 고객 프로필에서 제공된 이름과 값으로 속성을 생성하거나 업데이트하는 필드를 포함하는 JSON 객체일 수 있습니다. 다음 속성정보가 지원됩니다:

| 사용자 속성 | 설명 |
| --- | --- |
| 이름 | 사용자의 이름입니다. |
| 성 | 사용자의 성입니다. |
| 전화번호 | 사용자의 전화번호입니다. |
| 이메일 | 사용자의 이메일 주소입니다. |
| 성별 | 다음 문자열 중 하나: "M", "F", "O"(기타), "N"(해당 없음), "P"(밝히고 싶지 않음). |
| 구/군/시 | 사용자의 구/군/시입니다. |
| 국가 | [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) 형식의 문자열로 된 사용자 국가입니다. |
| 언어 | [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) 형식의 문자열로 된 사용자 언어입니다. |
| 생년월일 | "YYYY-MM-DD" 형식의 문자열로 된 사용자 생년월일입니다(예: 1980-12-21). |
| 시간대 | [IANA 시간대](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) 데이터베이스의 시간대 이름입니다(예: 'America/New_York' 또는 'Eastern Time (US & Canada)'). |
| Facebook | `id`(문자열), `likes`(문자열 배열), `num_friends`(정수) 중 하나를 포함하는 해시입니다. |
| Twitter | id(정수), `screen_name`(문자열, X(이전 Twitter) 핸들), `followers_count`(정수), `friends_count`(정수), `statuses_count`(정수) 중 하나를 포함하는 해시입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="4단계: 이벤트 전송 규칙 생성" }

{% alert note %}
구성 내에서 추가된 모든 속성은 속성 값의 변경 여부와 관계없이 이벤트가 Braze로 전송될 때마다 함께 전송됩니다. 사용자 속성을 구성할 때 이것이 데이터 포인트 사용량에 어떤 영향을 미치는지 확인하세요.
{% endalert %}

{% endtab %}
{% endtabs %}

### 5단계: 구매 이벤트 전송 규칙 생성 {#step-5-create-a-send-purchase-event-rule}

확장 프로그램을 설치한 후 새로운 이벤트 포워딩 [규칙](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en)을 생성하고 원하는 대로 조건을 구성합니다. 규칙에 대한 액션을 구성할 때 **Braze** 확장 프로그램을 선택한 다음 액션 유형으로 **Send Purchase Event**를 선택합니다.

![Braze Send Purchase Event를 사용하도록 구성된 Adobe 이벤트 포워딩 규칙 액션.]({% image_buster /assets/img/efe2.png %})

{% tabs local %}
{% tab 사용자 식별 %}

| 입력 | 설명 |
| --- | --- |
| 외부 사용자 ID | 길고 무작위적이며 균등하게 분포된 UUID 또는 GUID입니다. 사용자 ID를 다른 방법으로 지정하려는 경우에도 마찬가지로 길고 무작위적이며 균등하게 분포되어야 합니다. [권장되는 사용자 ID 명명 규칙]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web#naming-best-practices)에 대해 자세히 알아보세요. |
| Braze 사용자 ID | Braze 사용자 식별자입니다. |
| 사용자 별칭 | 별칭은 대체 고유 사용자 식별자 역할을 합니다. 별칭을 사용하여 코어 사용자 ID와 다른 차원에서 사용자를 식별할 수 있습니다.<br><br>사용자 별칭 객체는 두 부분으로 구성됩니다: 식별자 자체에 해당하는 `alias_name`과 별칭 유형을 나타내는 `alias_label`입니다. 사용자는 다른 레이블로 여러 별칭을 가질 수 있지만 `alias_label`당 하나의 `alias_name`만 가질 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="5단계: 구매 이벤트 전송 규칙 생성" }

{% alert note %}
이벤트를 사용자에게 연결하려면 `External User ID` 필드, `Braze User Identifier` 필드 또는 `User Alias` 섹션 중 하나를 입력해야 합니다.
{% endalert %}

{% endtab %}
{% tab 구매 데이터 %}

| 입력 | 설명 | 필수 |
| --- | --- | --- |
| 제품 ID | 구매 식별자입니다(예: 제품 이름 또는 제품 카테고리). | 예 |
| 구매 시간 | ISO 8601 형식 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식의 날짜-시간 문자열입니다. | 예 |
| 통화 | [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) 알파벳 통화 코드 형식의 문자열로 된 통화입니다. | 예 |
| 가격 | 객체의 가격입니다. | 예 |
| 수량 | 구매 수량입니다. 제공되지 않은 경우 기본값은 1입니다. 최대값은 100 미만이어야 합니다. | 아니요 |
| 앱 식별자 | 앱 식별자 또는 `app_id`는 워크스페이스 내 특정 앱에 활동을 연결하는 파라미터입니다. 워크스페이스 내에서 상호 작용할 앱을 지정합니다. | 아니요 |
| 구매 속성정보 | 구매의 커스텀 속성정보를 포함하는 JSON 객체입니다. | 아니요 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="5단계: 구매 이벤트 전송 규칙 생성" }

{% alert note %}
**Send Purchase Event** 액션에는 `Product ID`, `Purchase Time`, `Currency`, `Price`만 필수로 지정하면 되지만 구매 속성정보 필드에 가능한 한 많은 정보를 포함하는 것이 좋습니다. 자세한 내용은 [구매 객체]({{site.baseurl}}/api/objects_filters/purchase_object)를 참조하세요.
{% endalert %}

{% endtab %}
{% tab 사용자 속성 %}

구성 보기에서 각 이벤트와 함께 속성을 전송할지 여부를 선택할 수 있습니다.

사용자 속성은 지정된 고객 프로필에서 제공된 이름과 값으로 속성을 생성하거나 업데이트하는 필드를 포함하는 JSON 객체일 수 있습니다. 다음 속성정보가 지원됩니다:

| 사용자 속성 | 설명 |
| --- | --- |
| 이름 | 사용자의 이름입니다. |
| 성 | 사용자의 성입니다. |
| 전화번호 | 사용자의 전화번호입니다. |
| 이메일 | 사용자의 이메일 주소입니다. |
| 성별 | 다음 문자열 중 하나: "M", "F", "O"(기타), "N"(해당 없음), "P"(밝히고 싶지 않음). |
| 구/군/시 | 사용자의 구/군/시입니다. |
| 국가 | [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) 형식의 문자열로 된 사용자 국가입니다. |
| 언어 | [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) 형식의 문자열로 된 사용자 언어입니다. |
| 생년월일 | "YYYY-MM-DD" 형식의 문자열로 된 사용자 생년월일입니다(예: 1980-12-21). |
| 시간대 | [IANA 시간대](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) 데이터베이스의 시간대 이름입니다(예: 'America/New_York' 또는 'Eastern Time (US & Canada)'). |
| Facebook | `id`(문자열), `likes`(문자열 배열), `num_friends`(정수) 중 하나를 포함하는 해시입니다. |
| Twitter | id(정수), `screen_name`(문자열, X(이전 Twitter) 핸들), `followers_count`(정수), `friends_count`(정수), `statuses_count`(정수) 중 하나를 포함하는 해시입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="5단계: 구매 이벤트 전송 규칙 생성" }

{% alert note %}
구성 내에서 추가된 모든 속성은 속성 값의 변경 여부와 관계없이 이벤트가 Braze로 전송될 때마다 함께 전송됩니다. 사용자 속성을 구성할 때 이것이 데이터 포인트 사용량에 어떤 영향을 미치는지 확인하세요.
{% endalert %}

{% endtab %}
{% endtabs %}

### 6단계: Braze 내에서 데이터 검증 {#step-6-validate-data-within-braze}

이벤트 수집 및 Adobe Experience Platform 통합이 성공적이었다면 [고객 프로필 보기]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) 시 Braze 콘솔에서 이벤트를 확인할 수 있습니다. 구체적으로, Braze로 전송된 새로운 이벤트 데이터는 특정 사용자의 [개요 탭]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#overview-tab)에 있는 **Purchases** 또는 **Custom Events** 섹션에 반영됩니다.