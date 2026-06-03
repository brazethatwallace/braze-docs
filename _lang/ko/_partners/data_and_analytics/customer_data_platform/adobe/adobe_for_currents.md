---
nav_title: Adobe for Currents
article_title: Adobe for Currents
alias: /partners/adobe_for_currents/
description: "이 참조 문서에서는 Braze 커런츠와 Adobe 간의 파트너십에 대해 설명합니다. Adobe는 브랜드가 Adobe 데이터(커스텀 속성 및 Segments)를 실시간으로 Braze에 연결하고 매핑할 수 있는 고객 데이터 플랫폼입니다."
page_type: partner
tool: Currents
search_tag: Partner
---

# Adobe for Currents

> [Adobe](https://www.adobe.com/)는 브랜드가 Adobe 데이터(커스텀 속성 및 Segments)를 실시간으로 Braze에 연결하고 매핑할 수 있는 고객 데이터 플랫폼입니다.

Braze와 Adobe 통합을 통해 두 시스템 간의 정보 흐름을 원활하게 제어할 수 있습니다. [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)를 사용하면 데이터를 Adobe에 연결하여 전체 성장 스택에서 활용할 수도 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Currents | 데이터를 Adobe로 다시 내보내려면 계정에 [Braze 커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)가 설정되어 있어야 합니다. |
| Adobe Experience Platform 계정 | 이 파트너십을 활용하려면 [Adobe Experience Platform 계정](https://experience.adobe.com/#/platform/home)이 필요합니다. |
| 커넥터 생성 권한 | 이 통합을 사용하려면 스트리밍 소스 연결을 생성할 수 있는 권한이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

### 1단계: Adobe에서 XDM 스키마 생성 {#step-1-create-an-xdm-schema-in-adobe}

1. Adobe Experience Platform에서 **Schemas** > **Create schema** 선택 > **Experience Event** 선택 > **Next** 선택으로 이동합니다.<br><br>!["Braze Currents Walk-Through"라는 스키마에 대한 Adobe 스키마 페이지.]({% image_buster /assets/img/adobe/currents_sources.png %})<br><br>
2. 스키마의 이름과 설명을 입력합니다.
3. **Composition** 패널에서 스키마 속성을 구성합니다:
- **Field groups**에서 **Add**를 선택한 다음 **Braze Currents User Event** 필드 그룹을 추가합니다.
- **Save**를 선택합니다.

스키마에 대한 자세한 내용은 Adobe의 [스키마 생성](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui) 설명서를 참조하세요.

### 2단계: Braze를 Adobe Experience Platform에 연결 {#step-2-connect-braze-to-the-adobe-experience-platform}

1. Adobe Experience Platform에서 **Sources** > **Catalog** > **Marketing automation**으로 이동합니다.
2. Braze 커런츠에 대해 **Add data**를 선택합니다.
3. [Braze 커런츠 샘플 파일](https://github.com/Appboy/currents-examples/blob/master/sample-data/Adobe/adobe_examples.json)을 업로드합니다.<br><br>![Adobe "데이터 추가" 페이지.]({% image_buster /assets/img/adobe/currents_add_data.png %})<br><br>
4. 파일이 업로드된 후, 데이터셋 및 매핑할 스키마에 대한 정보를 포함하여 데이터 흐름 세부 정보를 입력합니다.
    - Braze 커런츠 소스를 처음 연결하는 경우, 새 데이터셋을 생성하고 [1단계](#step-1-create-an-xdm-schema-in-adobe)에서 생성한 스키마를 사용해야 합니다.
    - 처음이 아닌 경우, Braze 스키마를 참조하는 기존 데이터셋을 사용합니다.
5. 데이터에 대한 매핑을 구성하고 문제를 해결합니다.
    - `id`의 매핑을 `to _braze.appID`에서 스키마의 루트 수준에 있는 `_id`로 변경합니다.
    - `properties.is_amp`가 `_braze.messaging.email.isAMP`에 매핑되어 있는지 확인합니다.
    - `time` 및 `timestamp` 매핑을 삭제한 다음, 추가 아이콘 > **Add calculated field**를 선택하고 **time * 1000**을 입력합니다. **Save**를 선택합니다.
    - 새로운 소스 필드 옆에 있는 **Map target field**를 선택하고 스키마의 루트 수준에서 **timestamp**에 매핑합니다. <br><br>![매핑이 포함된 Adobe "데이터 추가" 페이지.]({% image_buster /assets/img/adobe/currents_mapping.png %})<br><br>
6. **Validate**를 선택하여 문제가 해결되었는지 확인합니다.

{% alert important %}
Braze 타임스탬프는 초 단위로 표현됩니다. Adobe Experience Platform에서 타임스탬프를 정확하게 반영하려면 계산 필드가 밀리초 단위여야 합니다. 초를 밀리초로 변환하려면 **time * 1000** 계산을 사용합니다.
{% endalert %}

{: start="7"}
7. **Next**를 선택하고, 데이터 흐름 세부 정보를 검토한 후 **Finish**를 선택합니다.<br><br>![매핑 오류가 없는 Adobe "데이터 추가" 페이지.]({% image_buster /assets/img/adobe/currents_no_errors.png %})

### 3단계: 자격 증명 수집 {#step-3-gather-credentials}

Braze가 Adobe Experience Platform으로 데이터를 전송할 수 있도록 다음 자격 증명을 수집하여 Braze에 입력합니다.

| 필드         | 설명                          |
|---------------|-------------------------------------|
| Client ID     | Adobe Experience Platform 소스와 연결된 클라이언트 ID입니다. |
| Client Secret | Adobe Experience Platform 소스와 연결된 클라이언트 시크릿입니다. |
| Tenant ID     | Adobe Experience Platform 소스와 연결된 테넌트 ID입니다. |
| Sandbox Name  | Adobe Experience Platform 소스와 연결된 샌드박스입니다.   |
| Dataflow ID   | Adobe Experience Platform 소스와 연결된 데이터 흐름 ID입니다.   |
| Streaming Endpoint  | Adobe Experience Platform 소스와 연결된 스트리밍 엔드포인트입니다. Braze는 이를 자동으로 배치 스트리밍 엔드포인트로 변환합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3: Gather credentials" }

### 4단계: 데이터 소스로 데이터를 스트리밍하도록 Currents 구성 {#step-4-configure-currents-to-stream-data-to-your-data-source}

1. Braze에서 **Partner Integrations** > **Data Export**로 이동한 다음 **Create New Current**를 선택합니다.
2. 다음 정보를 입력합니다:
    - 커넥터 이름
    - 커넥터에 대한 알림을 위한 연락처 정보
    - [3단계](#step-3-gather-credentials)에서 수집한 자격 증명
3. 수신할 이벤트를 선택합니다.
4. 필요에 따라 원하는 필드 제외 또는 변환을 구성합니다.
5. **Launch Current**를 선택합니다.