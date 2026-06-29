---
nav_title: OneTrust
article_title: OneTrust
description: "이 참조 문서에서는 데이터 프라이버시 및 보안 소프트웨어 제공업체인 OneTrust와 Braze 간의 파트너십을 설명하며, OneTrust 워크플로 빌더를 사용하여 제품에 대한 보안 워크플로를 생성할 수 있습니다."
alias: /partners/onetrust/
page_type: partner
search_tag: Partner

---

# OneTrust

> [OneTrust](https://www.onetrust.com/)는 신뢰 환경을 더 잘 이해하는 데 필요한 가시성, 강력한 인사이트를 활용하기 위한 실행력, 경쟁에서 앞서 나갈 수 있는 자동화를 제공하는 프라이버시 및 보안 소프트웨어 제공업체입니다.

_이 통합은 OneTrust에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 OneTrust 통합을 사용하면 OneTrust 워크플로 빌더를 사용하여 제품에 대한 보안 워크플로를 생성할 수 있습니다.
## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| OneTrust 계정 | 이 파트너십을 활용하려면 [OneTrust](https://www.onetrust.com/) 계정이 필요합니다. |
| Braze API 키 | OneTrust 동작에서 사용할 엔드포인트에 필요한 권한이 있는 Braze REST API 키입니다.<br><br>Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze 인스턴스 | Braze 인스턴스는 Braze 온보딩 매니저에게 문의하거나 [API 개요 페이지]({{site.baseurl}}/api/basics/#endpoints)에서 확인할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

다음 통합에서는 사용자 동의 업데이트 워크플로와 사용자 삭제 워크플로를 생성하는 방법을 안내합니다. 추가로 지원되는 Braze 엔드포인트에 대한 자세한 내용은 [기타 지원 동작](#Other-supported-actions)을 참조하세요.

### OneTrust에 Braze 자격 증명 추가 {#add-braze-credentials-to-onetrust}

OneTrust **Integrations** 메뉴에서 **Credentials** > **Add New** 버튼으로 이동하여 **Select System** 화면을 엽니다. 여기에서 **Braze**를 찾은 다음 **Next** 버튼을 클릭합니다.

**Enter Credential Details** 화면의 안내에 따라 다음 정보를 입력합니다. 완료되면 자격 증명을 저장합니다.
  - 자격 증명 이름
  - 커넥터 유형을 **Web App**으로 설정
  - 호스트 이름: `<your-braze-instance-url>`
  - **요청 헤더**:
    - **Authorization**: Bearer
    - **Content-Type**: application/json
  - 토큰: `<your-braze-api-key>`

### Braze를 시스템으로 추가 {#add-braze-as-a-system}

#### 1단계: 워크플로 생성 {#step-1-create-a-workflow}

{% tabs %}
{% tab 사용자 동의 업데이트 %}
1. OneTrust 통합 메뉴에서 **Gallery** > **Braze** > **Add**로 이동하여 새 워크플로를 생성합니다.![추가 버튼이 있는 Braze 통합을 보여주는 OneTrust 갤러리.]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. 워크플로 모달에서 이름과 알림 이메일을 입력합니다. **Create** 버튼을 클릭합니다. 생성이 완료되면 워크플로 빌더로 이동합니다. Braze 워크플로에는 삭제 요청을 처리하는 데 사용할 수 있는 API 호출과 동작이 시드됩니다. <br><br>
3. 워크플로 빌더에서 워크플로에서 트리거할 동작을 선택합니다.<br>![데이터 주체 동의 업데이트 이벤트에 대한 OneTrust 워크플로 빌더.]({% image_buster /assets/img/onetrust/onetrust2.png %})

{% endtab %}
{% tab 사용자 삭제 %}

1. OneTrust 통합 메뉴에서 **Gallery** > **Braze** > **Add**로 이동하여 새 워크플로를 생성합니다.![추가 버튼이 있는 Braze 통합을 보여주는 OneTrust 갤러리.]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. 워크플로 모달에서 이름과 알림 이메일을 입력합니다. **Create** 버튼을 클릭합니다. 생성이 완료되면 워크플로 빌더로 이동합니다. Braze 워크플로에는 삭제 요청을 처리하는 데 사용할 수 있는 API 호출과 동작이 시드됩니다. <br><br>
3. 워크플로 빌더에서 워크플로에서 트리거할 동작을 선택합니다.<br>![데이터 주체 삭제 이벤트에 대한 OneTrust 워크플로 빌더.]({% image_buster /assets/img/onetrust/onetrust8.png %})
{% endtab %}
{% endtabs %}

#### 2단계: 동작 선택 {#step-2-select-action}
{% tabs %}
{% tab 사용자 동의 업데이트 %}

1. 완료되면 **Done**을 클릭하고 **Add Action**을 선택합니다. 선택하는 동작은 업데이트되는 환경설정 유형과 선호하는 엔드포인트에 따라 달라집니다.
- 사용자의 글로벌 구독 환경설정을 업데이트하려면 **POST User track - attributes** 동작을 선택합니다.
- 사용자의 구독 그룹 환경설정을 업데이트하려면 **POST User Track - Attributes** 동작 또는 **POST Set Users Subscription Group Status** 동작을 선택합니다.<br>![POST User track - attributes를 보여주는 OneTrust 동작 추가 메뉴.]({% image_buster /assets/img/onetrust/onetrust4.png %})<br><br>
2. 원하는 동작을 선택하고, 이전에 생성한 Braze 자격 증명을 선택한 다음 **Next**를 클릭합니다.<br>![POST User track - attributes 동작에 대한 OneTrust 자격 증명 선택.]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% tab 사용자 삭제 %}

1. 완료되면 **Done**을 클릭하고 **Add Action**을 선택합니다.
- Braze에서 사용자를 삭제하려면 **POST User Delete Action** 동작을 선택합니다.
<br>![POST User Delete를 보여주는 OneTrust 동작 추가 메뉴.]({% image_buster /assets/img/onetrust/onetrust9.png %})<br><br>
2. 원하는 동작을 선택하고, 이전에 생성한 Braze 자격 증명을 선택한 다음 **Next**를 클릭합니다.<br>![POST User Delete 동작에 대한 OneTrust 자격 증명 선택.]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% endtabs %}
#### 3단계: 요청 본문 업데이트 {#step-3-update-request-body}
{% tabs %}
{% tab 사용자 동의 업데이트 %}

1. 필요한 동적 값을 포함하도록 본문을 업데이트합니다. 동작의 본문이 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 및 [`/subscription/status/set` 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)와 일치하는지 확인합니다.
2. 조직의 요구 사항에 맞게 추가 매개변수 또는 조건 로직으로 워크플로를 커스터마이즈합니다.
3. 편집이 완료되면 **Finish**를 클릭한 다음 **Activate**를 클릭하여 워크플로를 활성화합니다.

{% alert note %}
OneTrust 워크플로를 사용하여 Braze에서 구독 그룹 환경설정을 업데이트할 때, `subscription_group_id`는 구독 그룹이 생성될 때 Braze에서 설정한 ID와 일치해야 합니다. Braze 대시보드의 **구독 그룹** 페이지로 이동하여 구독 그룹의 `subscription_group_id`에 접근할 수 있습니다.
{% endalert %}

![구독 그룹 필드가 포함된 POST User track - attributes에 대한 OneTrust 요청 본문.]({% image_buster /assets/img/onetrust/onetrust6.png %})

{% endtab %}
{% tab 사용자 삭제 %}

1. 필요한 동적 값을 포함하도록 본문을 업데이트합니다. 동작의 본문이 [`/users/delete` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)와 일치하는지 확인합니다.
2. 편집이 완료되면 **Finish**를 선택한 다음 **Activate**를 선택하여 워크플로를 활성화합니다.

![external_id 필드가 포함된 POST User Delete에 대한 OneTrust 요청 본문.]({% image_buster /assets/img/onetrust/onetrust10.png %})

#### 데이터 주체 요청 워크플로 업데이트 {#update-the-data-subject-request-workflow}
1. **Privacy Rights Automation** 메뉴에서 **Workflows**를 선택합니다.
2. Braze 통합으로 업데이트할 워크플로를 선택합니다.
3. **Edit** 버튼을 선택하여 편집을 활성화합니다.
4. 다음으로, Braze 통합을 추가할 워크플로 단계를 선택하고 **Add Connection**을 클릭합니다.
5. 이전에 생성한 Braze 워크플로를 시스템 하위 작업으로 추가합니다.

{% endtab %}
{% endtabs %}

## 기타 지원 동작 {#other-supported-actions}

**POST User track - Attributes**, **POST Set Users Subscription Group Status**, **POST User Delete** 동작 외에도 Braze는 커스텀 워크플로를 생성하거나 기존 워크플로 내에서 하위 작업으로 사용할 수 있는 다른 엔드포인트를 지원합니다.

지원되는 동작의 전체 목록을 확인하려면:
1. OneTrust에서 **Integrations** 메뉴의 **Systems**를 클릭합니다.
2. **Braze** 시스템을 선택합니다.
3. **Actions** 탭으로 이동합니다.

![지원되는 API 동작 목록을 보여주는 OneTrust Braze 시스템 Actions 탭.]({% image_buster /assets/img/onetrust/onetrust7.png %})