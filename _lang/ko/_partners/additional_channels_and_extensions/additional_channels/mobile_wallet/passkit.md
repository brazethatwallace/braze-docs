---
nav_title: PassKit
article_title: PassKit
alias: /partners/passkit/
description: "이 참조 문서에서는 Braze와 PassKit 간의 파트너십에 대해 설명합니다. 이 파트너십을 통해 Apple Wallet 및 Google Pay 패스를 고객 경험에 통합하여 모바일 도달 범위를 확장할 수 있습니다."
page_type: partner
search_tag: Partner

---

# PassKit

> PassKit을 사용하면 Apple Wallet 및 Google Pay 패스를 고객 경험에 통합하여 모바일 도달 범위를 확장할 수 있습니다. 디지털 쿠폰, 로열티 카드, 멤버십 카드, 티켓 등을 쉽게 생성, 관리, 배포하고 성과를 분석할 수 있으며, 고객이 별도의 앱을 설치할 필요가 없습니다.

_이 통합은 Passkit에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Braze와 PassKit 통합을 통해 커스텀 Apple Wallet 및 Google Pay 패스를 즉시 전달하여 온라인 캠페인의 참여를 높이고 측정할 수 있습니다. 그런 다음 사용량을 분석하고 위치 기반 메시지와 고객의 모바일 지갑에 대한 개인화된 동적 업데이트를 트리거하여 매장 내 트래픽을 늘리기 위한 실시간 조정을 수행할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| PassKit 계정 | PassKit 계정과 PassKit 계정 매니저가 있어야 합니다. |
| `userDefinedID` | PassKit과 Braze 간에 커스텀 이벤트 및 커스텀 속성을 사용자에게 적절하게 업데이트하려면 Braze 외부 ID를 `userDefinedID`로 설정해야 합니다. 이 `userDefinedID`는 PassKit 엔드포인트에 API 호출을 할 때 사용됩니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL]({{site.baseurl}}/api/basics/#endpoints)에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

고객의 모바일 지갑 경험을 더욱 풍부하게 하기 위해 PassKit 대시보드 내에서 Braze [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint)를 통해 Braze로 데이터를 전달하도록 선택할 수 있습니다.

PassKit에서 공유할 데이터의 예시는 다음과 같습니다:
- **패스 생성**: 고객이 패스 링크를 클릭하고 처음으로 패스가 표시될 때.
- **패스 설치**: 고객이 패스를 지갑 앱에 추가하고 저장할 때.
- **패스 업데이트**: 패스가 업데이트될 때.
- **패스 삭제**: 고객이 지갑 앱에서 패스를 삭제할 때.

데이터가 Braze로 전달되면 오디언스를 구축하고, Liquid를 통해 콘텐츠를 개인화하며, 이러한 동작이 수행된 후 Campaign 또는 Canvas를 트리거할 수 있습니다.

## PassKit을 Braze에 연결 {#connect-passkit-to-braze}

PassKit에서 데이터를 전달하려면 Braze 외부 ID를 PassKit의 `externalId`로 설정했는지 확인하세요.

1. **Settings** 내 PassKit 패스 프로젝트 또는 프로그램의 **Integrations**에서 **Braze** 탭 아래 **Connect**를 클릭합니다.<br>![PassKit 플랫폼의 Braze 통합 타일.]({% image_buster /assets/img/passkit/passkit5.png %}){: style="max-width:80%"}<br><br>
2. Braze API 키와 엔드포인트 URL을 입력하고 커넥터의 이름을 제공합니다.<br><br>
3. **Enable Integration**을 토글하고 Braze에서 메시지를 트리거하거나 개인화할 이벤트를 선택합니다.<br>![API 키, 엔드포인트 URL, 통합 이름, 활성화 설정, 멤버십 설정 및 패스 설정을 허용하도록 확장된 PassKit Braze 통합 타일.]({% image_buster /assets/img/passkit/passkit4.png %}){: style="max-width:70%"}

## SmartPass 링크를 사용하여 패스 생성 {#create-pass-using-a-smartpass-link}

Braze 내에서 SmartPass 링크를 설정하여 고객이 Android 또는 iOS에 패스를 설치할 수 있는 고유 URL을 생성할 수 있습니다. 이를 위해 Braze 콘텐츠 블록에서 호출할 수 있는 암호화된 SmartPass 데이터 페이로드를 정의해야 합니다. 이 [콘텐츠 블록]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks)은 향후 패스 및 쿠폰에 재사용할 수 있습니다. 통합 과정에서 다음이 사용됩니다:

- **PassKit URL**: PassKit URL은 PassKit 프로그램의 고유 URL입니다.<br>각 프로그램에는 고유 URL이 있으며, PassKit 프로그램 또는 프로젝트의 **Distribution** 탭에서 찾을 수 있습니다. (예: https://pub1.pskt.io/c/ww0jir)<br><br>
- **PassKit 시크릿**: URL과 함께 이 프로그램을 위한 PassKit 키가 준비되어 있어야 합니다.<br>PassKit URL과 같은 페이지에서 찾을 수 있습니다.<br><br>
- **프로그램(또는 프로젝트) ID**: SmartPass URL을 생성하려면 PassKit 프로그램 ID가 필요합니다. <br>프로젝트 또는 프로그램의 **Settings** 탭에서 찾을 수 있습니다.

암호화된 SmartPass 링크 생성에 대한 자세한 내용은 이 [PassKit 문서](https://help.passkit.com/en/articles/3742778-hashed-smartpass-links)를 참조하세요.

### 1단계: 패스 데이터 페이로드 정의 {#passkit-integrations}

먼저 쿠폰 또는 멤버 페이로드를 정의해야 합니다.

페이로드에 포함할 수 있는 다양한 구성요소가 있지만, 여기서 주목해야 할 두 가지 중요한 항목이 있습니다:

| 구성요소 | 필수 | 유형 | 설명 |
| --------- | -------- | ---- | ----------- |
| `person.externalId` | 필수 | 문자열 | Braze 외부 ID로 설정되며, PassKit에서 Braze로의 콜백이 작동하는 데 중요합니다. 이를 통해 회사 사용자가 하나의 Campaign에서 여러 오퍼에 대한 쿠폰을 가질 수 있습니다. 고유성이 강제되지 않습니다. |
| `members.member.externalId` | 선택 사항 | 문자열 | Braze 외부 ID로 설정되며, 외부 ID를 사용하여 멤버십 패스를 업데이트할 수 있습니다. 이 필드를 설정하면 멤버십 프로그램 내에서 사용자가 고유하게 적용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Step 1: Define your pass data payload #passkit-integrations" }

사용 가능한 필드, 유형 및 유용한 설명의 전체 목록은 [PassKit GitHub 설명서](https://github.com/PassKit/smart-pass-link-from-csv-generator)를 참조하세요.

#### 페이로드 예시 {#example-payload}
{% raw %}
```liquid
{
  "members.member.externalId": "{{${user_id}}}",
  "members.member.points": "100",
  "members.tier.name": "current_customer",
  "person.displayName": "{{${first_name}}} {{${last_name}}}",
  "person.externalId": "{{${user_id}}}",
  "universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"
}
```
{% endraw %}

### 2단계: 정의되지 않은 페이로드 변수 생성 및 인코딩 {#step-2-create-and-encode-an-undefined-payload-variable}

Braze 대시보드에서 **콘텐츠** > **콘텐츠 블록**으로 이동하여 새 콘텐츠 블록을 생성하고 이름을 지정합니다.

**콘텐츠 블록 생성**을 선택하여 시작합니다.

다음으로 **콘텐츠 블록 Liquid 태그**를 정의해야 합니다. 이 콘텐츠 블록을 저장한 후 메시지를 작성할 때 이 Liquid 태그를 참조할 수 있습니다. 이 예시에서는 Liquid 태그를 {% raw %}`{{content_blocks.${passKit_SmartPass_url}}}`{% endraw %}로 할당했습니다.

이 콘텐츠 블록에서는 페이로드를 직접 포함하지 않고 {% raw %}`{{passData}}`{% endraw %} 변수에서 참조합니다. 콘텐츠 블록에 추가해야 하는 첫 번째 코드 스니펫은 {% raw %}`{{passData}}`{% endraw %} 변수의 Base64 인코딩을 캡처합니다.
{% raw %}
```liquid
{% capture base64JsonPayload %}{{passDatapassData|base64_encode}}{% endcapture %}
```
{% endraw %}

### 3단계: SHA1 HMAC 해시를 사용하여 암호화 서명 생성 {#step-3-create-your-encryption-signature-using-a-sha1-hmac-hash}

다음으로 프로젝트 URL과 페이로드의 [SHA1 HMAC](https://en.wikipedia.org/wiki/HMAC) 해시를 사용하여 암호화 서명을 생성합니다.

콘텐츠 블록에 추가해야 하는 두 번째 코드 스니펫은 해싱에 사용할 URL을 캡처합니다.
{% raw %}
```liquid
{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}
```
{% endraw %}

다음으로 이 해시와 `Project Secret`을 사용하여 서명을 생성해야 합니다. 세 번째 코드 스니펫을 포함하여 이를 수행할 수 있습니다:
{% raw %}
```liquid
{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}
```
{% endraw %}

마지막으로 다섯 번째 코드 스니펫을 사용하여 전체 URL에 서명을 추가합니다:
{% raw %}
```liquid
{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}{% endcapture %}
```
{% endraw %}

### 4단계: URL 출력 {#step-4-print-your-url}

마지막으로 최종 URL을 호출하여 메시지 내에 SmartPass URL이 출력되도록 합니다.
{% raw %}
```liquid
{{longURL}}
```
{% endraw %}

이 시점에서 다음과 같은 콘텐츠 블록을 만들었습니다:

{% raw %}
```liquid
{% capture base64JsonPayload %}{{passData|base64_encode}}{% endcapture %}

{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}

{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}

{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}&utm_source=braze&utm_campaign={{campaign.${name}}}{% endcapture %}{% capture longURL %}{{longURL | url_encode}}{% endcapture %}

{{longURL}}
```
{% endraw %}

이 예시에서는 이러한 설치의 소스를 Braze와 이 Campaign으로 추적하기 위해 UTM 매개변수가 추가되었습니다.

{% alert tip %}
페이지를 떠나기 전에 콘텐츠 블록을 저장하세요.
{% endalert %}

### 5단계: 모두 합치기 {#step-5-putting-it-all-together}

이 콘텐츠 블록이 만들어지면 향후에 다시 재사용할 수 있습니다.

예시 콘텐츠 블록에 정의되지 않은 두 개의 변수가 남아 있는 것을 알 수 있습니다.<br>
{% raw %}`{{passData}}`{% endraw %} - [1단계](#passkit-integrations)에서 정의한 JSON 패스 데이터 페이로드 <br>
{% raw %}`{{projectUrl}}`{% endraw %} - PassKit 프로젝트의 배포 탭에서 찾을 수 있는 프로젝트 또는 프로그램의 URL.

이 결정은 의도적이며 콘텐츠 블록의 재사용성을 지원합니다. 이러한 변수는 콘텐츠 블록 내에서 생성되는 것이 아니라 참조만 되기 때문에 콘텐츠 블록을 다시 만들지 않고도 변수를 변경할 수 있습니다.

예를 들어, 로열티 프로그램에 더 많은 초기 포인트를 포함하도록 소개 오퍼를 변경하거나 보조 멤버 카드 또는 쿠폰을 만들고 싶을 수 있습니다. 이러한 시나리오에서는 서로 다른 PassKit `projectURLs` 또는 서로 다른 패스 페이로드가 필요하며, Braze에서 Campaign별로 정의합니다.

#### 메시지 본문 작성 {#composing-the-message-body}

메시지 본문에서 이 두 변수를 모두 캡처한 다음 콘텐츠 블록을 호출해야 합니다.
[1단계](#passkit-integrations)에서 축소된 JSON 페이로드를 캡처합니다:

**프로젝트 URL 할당**
{% raw %}
```liquid
{% assign projectUrl = "https://pub1.pskt.io/c/ww0jir" %}
```
{% endraw %}

**JSON 캡처**
{% raw %}
```liquid
{% capture passData %}{"members.member.externalId": "{{${user_id}}}","members.member.points": "100","members.tier.name": "current_customer","person.displayName": "{{${first_name}}} {{${last_name}}}","person.externalId": "{{${user_id}}}","universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"}{% endcapture %}
```
{% endraw %}

**방금 만든 콘텐츠 블록 참조**
{% raw %}
```liquid
{{content_block.${passkit_SmartPass_url}}}
```
{% endraw %}

메시지 본문은 다음과 같이 표시되어야 합니다:
![캡처한 JSON 및 콘텐츠 블록 참조가 표시된 콘텐츠 블록 메시지 작성기의 이미지.]({% image_buster /assets/img/passkit/passkit1.png %}){: style="max-width:70%"}

샘플의 출력 URL은 다음과 같습니다:
![무작위로 생성된 긴 문자 및 숫자 문자열이 포함된 출력 URL.]({% image_buster /assets/img/passkit/passkit2.png %}){: style="max-width:70%"}

출력 URL이 길어집니다. 이는 모든 패스 데이터를 포함하고 URL 수정을 통한 데이터 무결성 및 변조 방지를 위해 최고 수준의 보안을 적용하기 때문입니다. SMS를 사용하여 이 URL을 배포하는 경우 [bit.ly](https://dev.bitly.com/v4/#operation/createFullBitlink)와 같은 링크 단축 프로세스를 통해 실행할 수 있습니다. 이는 bit.ly 엔드포인트에 대한 연결된 콘텐츠 호출을 통해 수행할 수 있습니다.

## PassKit 웹훅을 사용하여 패스 업데이트 {#update-pass-using-the-passkit-webhook}

Braze 내에서 웹훅 Campaign 또는 Canvas 내 웹훅을 설정하여 사용자의 동작에 따라 기존 패스를 업데이트할 수 있습니다. 유용한 PassKit 엔드포인트에 대한 정보는 다음 링크를 확인하세요.
- [멤버 프로젝트](https://docs.passkit.io/protocols/member/)
- [쿠폰 프로젝트](https://docs.passkit.io/protocols/coupon/)
- [항공편 프로젝트](https://docs.passkit.io/protocols/boarding/)

### 페이로드 매개변수 {#payload-parameters}

시작하기 전에 PassKit에 대한 생성 및 업데이트 웹훅에 포함할 수 있는 일반적인 JSON 페이로드 매개변수는 다음과 같습니다.

| 데이터 | 유형 | 설명 |
| ---- | ---- | ----------- |
| `externalId` | 문자열 | 고유 고객 식별자(예: 멤버십 번호)를 사용하는 기존 시스템과의 호환성을 제공하기 위해 패스 레코드에 고유 ID를 추가할 수 있습니다. 패스 ID 대신 `userDefinedId` 및 `campaignName`을 통해 이 엔드포인트를 사용하여 패스 데이터를 검색할 수 있습니다. 이 값은 Campaign 내에서 고유해야 하며, 이 값이 설정된 후에는 변경할 수 없습니다.<br><br>Braze 통합의 경우 Braze 외부 ID를 사용하는 것을 권장합니다: {% raw %}`{{${user_id}}}`{% endraw %} |
| `campaignId` (쿠폰) <br><br> `programId` (멤버십) | 문자열 | PassKit에서 생성한 Campaign 또는 프로그램 템플릿의 ID입니다. 이를 찾으려면 PassKit 패스 프로젝트의 **Settings** 탭으로 이동하세요. |
| `expiryDate` | IO8601 datetime | 패스 만료 날짜입니다. 만료 날짜 이후 패스는 자동으로 무효화됩니다(`isVoided` 참조). 이 값은 템플릿 및 Campaign 종료 날짜 값을 재정의합니다. |
| `status` | 문자열 | 쿠폰의 현재 상태(예: `REDEEMED` 또는 `UNREDEEMED`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Payload parameters" }

### 1단계: Braze 웹훅 템플릿 생성 {#step-1-create-your-braze-webhook-template}

향후 Campaign이나 Canvas에서 사용할 PassKit 웹훅 템플릿을 만들려면 Braze 대시보드의 **템플릿 및 미디어** 섹션으로 이동하세요. 일회성 PassKit 웹훅 Campaign을 만들거나 기존 템플릿을 사용하려면 새 Campaign을 만들 때 Braze에서 **Webhook**을 선택하세요.

PassKit 웹훅 템플릿을 선택하면 다음이 표시됩니다:
- **Webhook URL**: `https://api-pub1.passkit.io/coupon/singleUse/coupon`
- **Request Body**: Raw Text

#### 요청 헤더 및 메서드 {#request-headers-and-method}

PassKit은 base 64로 인코딩된 PassKit API 키를 포함하는 승인용 `HTTP Header`가 필요합니다. 다음은 이미 템플릿 내에 키-값 페어로 포함되어 있지만, **Settings** 탭에서 `<PASSKIT_LONG_LIVED_TOKEN>`을 PassKit 토큰으로 교체해야 합니다. 토큰을 검색하려면 PassKit 프로젝트/프로그램으로 이동한 다음 **Settings > Integrations > Long Lived Token**으로 이동하세요.

{% raw %}
- **HTTP Method**: PUT
- **Request Header**:
  - **Authorization**: Bearer `<PASSKIT_LONG_LIVED_TOKEN>`
  - **Content-Type**: application/json
{% endraw %}

#### 요청 본문 {#request-body}

웹훅을 설정하려면 사용 사례에 필요한 페이로드 매개변수를 포함하여 요청 본문에 새 이벤트 세부 정보를 입력합니다:

```json
{% raw %}{
  "externalId": "{{${user_id}}}",
  "campaignId": " 2xa1lRy8dBz4eEElBfmIz8",
  "expiryDate": "2020-05-10T00:00:00Z"
}{% endraw %}
```

### 2단계: 요청 미리보기 {#step-2-preview-your-request}

원시 텍스트는 적용 가능한 Braze 태그인 경우 자동으로 강조 표시됩니다.

**Preview** 패널에서 요청을 미리 보거나 **Test** 탭으로 이동하여 무작위 사용자, 기존 사용자를 선택하거나 직접 커스터마이즈하여 웹훅을 테스트할 수 있습니다.

{% alert important %}
페이지를 떠나기 전에 템플릿을 저장하세요! <br>업데이트된 웹훅 템플릿은 새 [웹훅 Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)을 만들 때 **저장된 웹훅 템플릿** 목록에서 찾을 수 있습니다.
{% endalert %}

## 연결된 콘텐츠를 통해 패스 세부 정보 검색 {#retrieve-pass-details-via-connected-content}

패스를 생성하고 업데이트하는 것 외에도 Braze [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/)를 통해 사용자의 패스 메타데이터를 검색하여 메시징 Campaign에 개인화된 패스 세부 정보를 포함할 수 있습니다.

**PassKit 연결된 콘텐츠 호출**

{% raw %}
```liquid
{% connected_content  https://api-pub1.passkit.io/coupon/singleUse/coupon/externalId/{{${user_id}}} :headers {"Authorization": "Bearer <PASSKIT_LONG_LIVED_TOKEN>","Content-Type": "application/json"} :save passes %}

{{passes.status}}
```
{% endraw %}

**Liquid 응답 예시**

{% tabs local %}
{% tab passes redemptionDetails %}

```json
{
    "redemptionDate": null,
    "redemptionCode": "",
    "lat": 0,
    "lon": 0,
    "alt": 0,
    "redemptionSource": "",
    "redemptionReference": "",
    "transactionReference": "",
    "transactionAmount": 0
}
```

{% endtab %}
{% tab passes status %}
```
UNREDEEMED
```
{% endtab %}
{% endtabs %}