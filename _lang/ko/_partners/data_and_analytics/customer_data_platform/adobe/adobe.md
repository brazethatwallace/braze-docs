---
nav_title: Adobe
article_title: Adobe
description: "이 페이지에서는 브랜드가 Adobe 데이터(커스텀 속성 및 Segments)를 Braze에 실시간으로 연결하고 매핑할 수 있도록 하는 고객 데이터 플랫폼인 Braze와 Adobe 간의 파트너십에 대해 설명합니다. 브랜드는 이 데이터를 기반으로 해당 사용자에게 개인화된 타겟 경험을 제공할 수 있습니다."
page_type: partner
page_order: 1
search_tag: Partner

---

# Adobe

> Adobe Experience Platform을 기반으로 구축된 Adobe의 실시간 고객 데이터 플랫폼은 여러 엔터프라이즈 소스에서 알려진 데이터와 익명 데이터를 통합하여 고객 프로필을 생성합니다. 이러한 프로필을 사용하여 모든 채널과 기기에서 실시간으로 개인화된 경험을 제공할 수 있습니다.

Braze와 Adobe 고객 데이터 플랫폼 통합은 브랜드의 Adobe 데이터(커스텀 속성 및 Segments)를 Braze에 실시간으로 연결하고 매핑합니다. 이 데이터를 기반으로 사용자에게 개인화된 타겟 경험을 제공할 수 있습니다. Adobe를 사용하면 통합이 직관적입니다. Adobe [ID](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en)를 가져와 Braze 외부 ID에 매핑하고 Braze 플랫폼으로 전송하기만 하면 됩니다. 전송된 모든 데이터는 새로운 `AdobeExperiencePlatformSegments` 속성을 통해 Braze에서 액세스할 수 있습니다.

{% alert important %}
Adobe Experience Platform 통합은 현재 동적 오디언스 멤버십을 지원하지 않습니다. 즉, 고객 프로필에 값을 추가할 수만 있고 제거할 수는 없습니다.
{% endalert %}

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Adobe 계정 | 이 파트너십을 활용하려면 [Adobe 계정](https://account.adobe.com/)이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze 인스턴스 | Braze 인스턴스는 Braze 온보딩 매니저에게 문의하거나 [API 개요 페이지]({{site.baseurl}}/api/basics#endpoints)에서 확인할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL]({{site.baseurl}}/api/basics#endpoints)에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

{% alert important %}
추가 커스텀 속성을 전송하면 데이터 포인트 사용량이 증가합니다. 잠재적인 데이터 포인트 증가를 더 잘 이해하려면 고객 성공 매니저에게 문의하는 것을 권장합니다.
{% endalert %}

## 통합 {#integration}

### 1단계: Braze 대상 구성 {#step-1-configure-braze-destination}

Adobe **Settings** 페이지에서 **Collections** 아래의 **Destinations**를 선택합니다. 거기에서 **Braze** 타일을 찾아 **Configure**를 선택합니다.

![Braze 대상 타일과 Configure 작업이 표시된 Adobe Destinations 카탈로그.]({% image_buster /assets/img/adobe/braze-destination-configure.png %})

{% alert note %}
Braze와의 연결이 이미 존재하는 경우 대상 카드에 **Activate** 버튼이 표시됩니다. 활성화와 구성의 차이점에 대한 자세한 내용은 Adobe 대상 워크스페이스 [설명서](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog)의 카탈로그 섹션을 참조하세요.
{% endalert %}

### 2단계: Braze 토큰 제공 {#step-2-provide-braze-token}

**Account** 단계에서 Braze API 키를 입력하고 **Connect to destination**을 선택합니다.

![API 키 입력 및 연결 작업이 표시된 Adobe Braze 대상 계정 단계.]({% image_buster /assets/img/adobe/braze-destination-account.png %}){: style="max-width:60%"}

### 3단계: 인증 {#step-3-authentication}

다음으로 **Authentication** 단계에서 Braze 연결 세부 정보를 입력합니다:
- **Name**: 향후 이 대상을 식별할 이름을 입력합니다.
- **Destination**: 이 대상을 식별하는 데 도움이 되는 설명을 입력합니다.
- **Endpoint instance**: Braze 엔드포인트 인스턴스를 입력합니다.
- **Marketing use case**: 마케팅 사용 사례는 데이터가 대상으로 내보내지는 의도를 나타냅니다. Adobe에서 정의한 마케팅 사용 사례 중에서 선택하거나 자체 마케팅 사용 사례를 생성할 수 있습니다. Adobe 마케팅 사용 사례에 대해 자세히 알아보려면 [Adobe Experience Platform의 데이터 거버넌스](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations)를 참조하세요.

![이름, 대상 및 엔드포인트 필드가 표시된 Adobe 대상 인증 단계.]({% image_buster /assets/img/adobe/braze-destination-authentication.png %}){: style="max-width:60%;"}

### 4단계: 대상 생성 {#step-4-create-destination}

**Create destination**을 선택합니다. 대상이 생성되었습니다. **Save & Exit**를 선택하여 나중에 Segments를 활성화하거나 **Next**를 선택하여 워크플로를 계속하고 활성화할 Segments를 선택할 수 있습니다.

### 5단계: Segments 활성화 {#step-5-activate-segments}

Segments를 Braze 대상에 매핑하여 Adobe 실시간 고객 데이터 플랫폼에 있는 데이터를 활성화합니다.

다음 목록은 Segment를 활성화하는 데 필요한 일반적인 단계를 설명합니다. Adobe Segments 및 Segment 활성화 워크플로에 대한 자세한 안내는 [Adobe](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites)를 참조하세요.

1. Braze 대상을 선택하고 활성화합니다.
2. 해당하는 Segments를 선택합니다.
4. 내보내는 각 Segment에 대해 스케줄링 및 파일 이름을 구성합니다.
5. Braze로 전송할 속성을 선택합니다.
6. 활성화를 검토하고 확인합니다.

### 6단계: 필드 매핑 {#step-6-field-mapping}

Adobe Experience Platform에서 Braze로 오디언스 데이터를 올바르게 전송하려면 필드 매핑 단계를 완료해야 합니다. 매핑은 Adobe Experience 데이터 모델 필드와 해당하는 Braze 플랫폼 필드 간의 연결을 생성합니다.

1. 매핑 단계에서 **Add new mapping**을 선택합니다.<br>![Add new mapping 버튼이 표시된 Adobe 필드 매핑 페이지.]({% image_buster /assets/img/adobe/braze-destination-mapping.png %}){: style="max-width:50%;"}<br><br>
2. 소스 필드 섹션에서 빈 필드 옆의 화살표 버튼을 선택하여 소스 필드 선택 창을 엽니다.<br>![대상 매핑을 위한 Adobe 소스 필드 선택기.]({% image_buster /assets/img/adobe/braze-destination-mapping-source.png %})<br><br>
3. 창에서 Braze 속성에 매핑할 Adobe 속성을 선택합니다. <br>![매핑을 위한 소스 속성이 표시된 Adobe 속성 선택기.]({% image_buster /assets/img/adobe/braze-destination-mapping-attributes.png %}){: style="max-width:70%;"}<br><br>다음으로 ID 네임스페이스를 선택합니다. 이 옵션은 플랫폼 ID 네임스페이스를 Braze 네임스페이스에 매핑하는 데 사용됩니다.<br>![Braze 매핑에 사용되는 Adobe ID 네임스페이스 선택기.]({% image_buster /assets/img/adobe/braze-destination-mapping-namespaces.png %}){: style="max-width:80%;"}<br> 소스 필드를 선택한 다음 **Select**를 선택합니다.<br><br>
4. 타겟 필드 섹션에서 필드 옆의 매핑 아이콘을 선택합니다.<br>![매핑 아이콘이 선택된 Adobe 타겟 필드 매핑 패널.]({% image_buster /assets/img/adobe/braze-destination-mapping-target.png %}){: style="max-width:90%;"} <br><br>
5. 타겟 필드 선택 창에서 세 가지 카테고리의 타겟 필드 중에서 선택할 수 있습니다:<br><br>• **Select identity namespace**: 이 옵션을 사용하여 플랫폼 ID 네임스페이스를 Braze ID 네임스페이스에 매핑합니다.<br>• **Select custom attributes**: 이 옵션을 사용하여 Adobe XDM 속성을 Braze 계정에서 정의한 커스텀 Braze 속성에 매핑합니다. <br><br>![ID 네임스페이스 및 커스텀 속성 옵션이 표시된 Adobe 타겟 필드 선택기.]({% image_buster /assets/img/adobe/braze-destination-mapping-target-fields.png %}){: style="max-width:60%;"}<br><br>**이 옵션을 사용하여 기존 XDM 속성의 이름을 Braze에서 변경할 수도 있습니다.** 예를 들어, `lastname` XDM 속성을 Braze의 커스텀 `Last_Name` 속성에 매핑하면, `Last_Name` 속성이 아직 존재하지 않는 경우 Braze에서 생성되고 `lastname` XDM 속성이 여기에 매핑됩니다. <br><br> 타겟 필드를 선택한 다음 **Select**를 선택합니다.<br><br>
6. 필드 매핑이 목록에 표시됩니다.<br>![대상 매핑 단계에 나열된 완료된 Adobe-Braze 필드 매핑.]({% image_buster /assets/img/adobe/braze-destination-mapping-complete.png %})<br><br>
7. 더 많은 매핑을 추가하려면 필요에 따라 1~6단계를 반복합니다.

## 사용 사례 {#use-case}

XDM 프로필 스키마와 Braze 인스턴스에 다음과 같은 속성과 ID가 포함되어 있다고 가정해 보겠습니다:

|     | XDM 프로필 스키마 | Braze 인스턴스 |
| --- | ------------------ | -------------- |
| 속성 | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number`| - `FirstName`<br>- `LastName`<br>- `PhoneNumber`|
| ID | - `Email`<br>- Google Ad ID (`GAID`)<br>- Apple ID For Advertisers (`IDFA`) | - `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case" }

올바른 매핑은 다음과 같습니다:

![대상 매핑: IdentityMap:IDFA가 IdentityMap:external_id에 매핑됨, IdentityMap:GAID가 IdentityMap:external_id에 매핑됨, IdentityMap:Email이 IdentityMap:external_id에 매핑됨, xdm:mobilePhone.number가 CustomAttribute:PhoneNumber에 매핑됨, xdm:person.name.lastName이 CustomAttribute:LastName에 매핑됨, xdm:person.name.firstName이 CustomAttribute:FirstName에 매핑됨]({% image_buster /assets/img/adobe/braze-destination-mapping-example.png %})

## 내보낸 데이터 {#exported-data}
데이터가 Braze로 성공적으로 내보내졌는지 확인하려면 Braze 계정을 확인하세요. Adobe Experience Platform Segments는 `AdobeExperiencePlatformSegments` 속성 아래에서 Braze로 내보내집니다.

## 데이터 사용 및 거버넌스 {#data-usage-and-governance}
모든 Adobe Experience Platform 대상은 데이터를 처리할 때 데이터 사용 정책을 준수합니다. Adobe Experience Platform이 데이터 거버넌스를 시행하는 방법에 대한 자세한 내용은 [실시간 고객 데이터 플랫폼의 데이터 거버넌스](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en)를 참조하세요.