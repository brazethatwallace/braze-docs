---
nav_title: Zapier
article_title: Zapier
alias: /partners/zapier/
description: "이 참조 문서에서는 웹 앱 간에 데이터를 공유하고 해당 정보를 사용하여 동작을 자동화할 수 있는 자동화 웹 도구인 Zapier와 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---
# Zapier 통합 {#zapier-integration}

> [Zapier](https://zapier.com/)는 웹 앱 간에 데이터를 공유하고 해당 정보를 사용하여 동작을 자동화할 수 있는 자동화 웹 도구입니다.

Braze와 Zapier 파트너십은 Braze API 및 Braze [웹훅]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook)을 활용하여 Google Workplace, Slack, Salesforce, WordPress 등과 같은 서드파티 애플리케이션에 연결하고 다양한 동작을 자동화합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Zapier 계정 | 이 파트너십을 활용하려면 Zapier 계정이 필요합니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL입니다. 엔드포인트는 [인스턴스의 Braze URL]({{site.baseurl}}/api/basics/#api-definitions)에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

다음 Zapier 예제에서는 POST 웹훅을 사용하여 WordPress에서 Braze로 정보를 전송합니다. 이 정보를 사용하여 Braze Canvas를 생성할 수 있습니다.

### 1단계: Zapier 트리거 생성 {#step-1-create-a-zapier-trigger}

Zapier 용어에서 "zap"은 앱과 서비스를 연결하는 자동화된 워크플로입니다. 모든 zap의 첫 번째 부분은 트리거를 지정하는 것입니다. zap이 활성화되면 트리거가 감지될 때마다 Zapier가 자동으로 해당 동작을 수행합니다.

WordPress 예제를 사용하여 Zapier 플랫폼에서 새 WordPress 게시물이 추가될 때 트리거되도록 zap을 설정하고 **Post Status** 및 **Post Type**으로 **Published**와 **Posts**를 선택합니다.

![Zapier 플랫폼에서 zap 내에서 트리거를 "new comment", "any webhook" 또는 "new post"로 선택합니다. 이 예에서는 "new post"가 선택되어 있습니다.] [5]

![Zapier 플랫폼에서 zap 내에서 원하는 게시물 상태와 게시물 유형을 선택하여 트리거를 구성합니다. 이 예에서는 "Published"와 "Posts"가 선택되어 있습니다.] [6]

### 2단계: 동작 웹훅 추가 {#step-2-add-an-action-webhook}

다음으로 zap 동작을 정의합니다. zap이 활성화되고 트리거가 감지되면 동작이 자동으로 수행됩니다.

예제를 계속 진행하면, JSON 형식의 POST 요청을 Braze 엔드포인트로 전송하려고 합니다. **Apps** 아래에서 **Webhooks** 옵션을 선택하면 됩니다.

![]({% image_buster /assets/img_archive/zapier3.png %})

### 3단계: Braze POST 설정 {#step-3-set-up-braze-post}

웹훅을 설정할 때 다음 설정을 사용하고 웹훅 URL에 Braze REST 엔드포인트를 입력합니다. 완료되면 **Publish**를 선택합니다.

- **Method**: POST
- **Webhook URL**: `https://rest.iad-01.braze.com/canvas/trigger/send`
- **Data Pass-Through**: False
- **Unflatten**: No
- **Request Header**:
  - **Content-Type**: application/json
  - **Authorization**: Bearer YOUR-API-KEY
- **Data**:

```json
{
  "canvas_id": "your_canvas_identifier",
  "recipients": [
    {
      "external_user_id": "external_user_identifier",
      "context":{
        "string_property": "Your example string",
        "example_integer_property": 1
      }
    }
  ]
}
```

![]({% image_buster /assets/img/zapier.png %}){: style="max-width:70%;"}

### 4단계: Braze Campaign 생성 {#step-4-create-a-braze-campaign}

zap을 성공적으로 설정한 후에는 Liquid 형식을 사용하여 메시지에 정보를 표시함으로써 WordPress 데이터로 Braze Campaigns 또는 Canvases를 커스터마이즈할 수 있습니다.

## `/users/track` 엔드포인트에서 Zapier 사용하기 {#using-zapier-with-the-userstrack-endpoint}

Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 엔드포인트로 데이터를 전송하려면(예: Google Sheets에서 **New or Updated Spreadsheet Row**와 같은 트리거를 사용하는 경우) **Custom Request**와 함께 **Webhooks by Zapier**를 사용하세요. 표준 **POST** 동작은 사용하지 마세요. 표준 POST 동작은 `/users/track` 엔드포인트와 호환되지 않는 형식으로 요청을 포맷합니다.

1. Zapier에서 트리거를 선택합니다(예: Google Sheets의 **New or Updated Spreadsheet Row**).
2. 동작으로 **Webhooks by Zapier**를 선택하고 **Custom Request**(POST가 아님)를 선택합니다.
3. **Method**를 POST로 설정하고, Braze REST 엔드포인트 URL(예: `https://rest.iad-01.braze.com/users/track`)을 입력한 다음, Postman이나 API 호출에서와 마찬가지로 각 요소를 큰따옴표로 감싸서 요청 본문을 포맷합니다. 트리거의 필드(예: 스프레드시트 열)를 JSON 본문의 적절한 위치에 매핑합니다.
4. 필수 헤더를 추가합니다:
   - **Content-Type**: `application/json`
   - **Authorization**: `Bearer YOUR-REST-API-KEY`(대괄호나 따옴표 없이 Braze REST API 키를 사용합니다)
5. 단계를 테스트하고 zap을 활성화합니다.

[5]: {% image_buster /assets/img_archive/zapier1.png %}
[6]: {% image_buster /assets/img_archive/zapier2.png %}